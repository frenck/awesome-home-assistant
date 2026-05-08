#!/usr/bin/env python3
"""Validate README.md entries against the awesome-home-assistant
acceptance criteria.

Designed for two modes:
- PR mode (default): only checks newly-added entries vs a base ref.
  Useful in CI: passes if the diff doesn't add anything broken.
- Full mode (--all): checks every entry. Useful for the weekly cron and
  for one-off audits.

Authentication: reads GITHUB_TOKEN from the environment.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Iterable

GITHUB_API = "https://api.github.com"
TOKEN = os.environ.get("GITHUB_TOKEN", "")

# OSI-approved SPDX identifiers (subset relevant to the HA ecosystem).
# Source: https://spdx.org/licenses/ filtered by isOsiApproved.
OSI_LICENSES: set[str] = {
    "0BSD", "AFL-3.0", "AGPL-3.0", "AGPL-3.0-only", "AGPL-3.0-or-later",
    "Apache-1.1", "Apache-2.0", "Artistic-2.0", "BSD-1-Clause", "BSD-2-Clause",
    "BSD-3-Clause", "BSD-3-Clause-Clear", "BSL-1.0", "CDDL-1.0", "ECL-2.0",
    "EFL-2.0", "EPL-1.0", "EPL-2.0", "EUPL-1.1", "EUPL-1.2", "GPL-2.0",
    "GPL-2.0-only", "GPL-2.0-or-later", "GPL-3.0", "GPL-3.0-only",
    "GPL-3.0-or-later", "ISC", "LGPL-2.1", "LGPL-2.1-only",
    "LGPL-2.1-or-later", "LGPL-3.0", "LGPL-3.0-only", "LGPL-3.0-or-later",
    "MIT", "MIT-0", "MPL-1.1", "MPL-2.0", "MS-PL", "NCSA", "OSL-3.0",
    "PostgreSQL", "Python-2.0", "RPL-1.5", "Unlicense", "UPL-1.0",
    "Vim", "W3C", "Zlib",
}

# Creative Commons identifiers acceptable for "Other Awesome Lists".
CC_LICENSES: set[str] = {
    "CC-BY-4.0", "CC-BY-3.0", "CC-BY-SA-4.0", "CC-BY-SA-3.0", "CC0-1.0",
}

# URL shorteners we refuse outright.
URL_SHORTENERS: set[str] = {
    "bit.ly", "t.co", "goo.gl", "tinyurl.com", "ow.ly", "is.gd",
    "buff.ly", "rebrand.ly", "cutt.ly", "shorturl.at", "tiny.cc",
    "rb.gy", "shorturl.com", "lnkd.in", "fb.me", "youtu.be",
}
# Note: youtu.be is a YouTube shortener but is so deeply established that
# rejecting it would be friction for no real benefit. We leave it allowed.
URL_SHORTENERS.discard("youtu.be")

# Tracking params we strip / warn on.
TRACKING_PARAMS = {
    "utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content",
    "fbclid", "gclid", "mc_eid", "mc_cid", "_ga", "yclid", "msclkid",
}

# Section path -> rule profile.
# Section path = tuple of (## heading, ### heading or None).
RULES: dict[tuple[str, str | None], str] = {
    # Apps
    ("Apps", "Official Apps"): "software",
    ("Apps", "Third Party Apps"): "software",
    # Dashboards
    ("Dashboards", None): "software",
    ("Dashboards", "Icon packs"): "software_hacs_plugin",
    ("Dashboards", "Themes"): "software",
    ("Dashboards", "Custom Cards"): "software_hacs_plugin",
    ("Dashboards", "Alternative Dashboards"): "software",
    # Integrations
    ("Custom Integrations", None): "software_hacs_integration",
    # DIY -- entries may link to a repo OR to a forum/blog
    ("DIY", None): "diy_optional_repo",
    ("DIY", "DIY Gateways"): "diy_optional_repo",
    ("DIY", "DIY Projects"): "diy_optional_repo",
    # Online Resources
    ("Online Resources", "Blogs"): "content_blog",
    ("Online Resources", "YouTube Channels"): "content_youtube",
    ("Online Resources", "Podcasts"): "content_podcast",
    ("Online Resources", "Twitter"): "skip",  # being deprecated
    # Misc
    ("Public Configurations", None): "public_config",
    ("Uncategorized", None): "universal_only",
    ("Alternative Home Automation Software", None): "software",
    ("Other Awesome Lists", None): "software_or_cc",
    # Communities (link to Discord/Reddit/etc.) - universal-only
    ("In case you need help", "Official Communities"): "universal_only",
    ("In case you need help", "Other Communities"): "universal_only",
    # Help / Installing - skip; these are not "entries" the way contributors think
    ("How to use", None): "skip",
    ("Installing", None): "skip",
    # Footer-ish sections - skip
    ("Contents", None): "skip",
    ("Contributing", None): "skip",
    ("Trademark Legal Notice", None): "skip",
}

REPO_RX = re.compile(
    r"^https?://github\.com/([\w.-]+)/([\w.-]+?)(?:[/#?]|$|\.git$)",
    re.IGNORECASE,
)
ENTRY_RX = re.compile(r"^\s*-\s*(?:\S+\s+)?\[([^\]]+)\]\((https?://[^)\s]+)\)\s*-?\s*(.*)$")


@dataclass
class Entry:
    raw: str
    name: str
    url: str
    description: str
    section: str
    subsection: str | None
    rule: str

    @property
    def section_label(self) -> str:
        return f"{self.section}" + (f" › {self.subsection}" if self.subsection else "")


@dataclass
class Findings:
    errors: list[tuple[Entry, str]] = field(default_factory=list)
    warnings: list[tuple[Entry, str]] = field(default_factory=list)

    def err(self, entry: Entry, msg: str) -> None:
        self.errors.append((entry, msg))

    def warn(self, entry: Entry, msg: str) -> None:
        self.warnings.append((entry, msg))


# ---- README parsing -----------------------------------------------------

def parse_readme(path: str) -> list[Entry]:
    entries: list[Entry] = []
    section: str | None = None
    subsection: str | None = None
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if line.startswith("## "):
                section = line[3:].strip()
                subsection = None
                continue
            if line.startswith("### "):
                subsection = line[4:].strip()
                continue
            if not line.lstrip().startswith("- ["):
                continue
            m = ENTRY_RX.match(line)
            if not m:
                continue
            name, url, desc = m.group(1), m.group(2), m.group(3).strip(" -")
            if not section:
                continue
            rule = RULES.get((section, subsection)) or RULES.get((section, None)) or "skip"
            entries.append(
                Entry(line, name, url, desc, section, subsection, rule)
            )
    return entries


def diff_added_lines(base_ref: str, path: str) -> set[str]:
    """Return the set of newly-added lines in `path` between base_ref and HEAD."""
    out = subprocess.run(
        ["git", "diff", "--unified=0", f"{base_ref}...HEAD", "--", path],
        capture_output=True, text=True, check=True,
    ).stdout
    added: set[str] = set()
    for line in out.splitlines():
        if line.startswith("+") and not line.startswith("+++"):
            added.add(line[1:])
    return added


def base_urls(base_ref: str, path: str) -> set[str]:
    """Return the canonicalised set of URLs that were already in `path` on
    the base ref. Used to grandfather entries that already existed: a
    restructure PR that moves an existing entry to a new section should
    not have its repo-level checks (archived, age, license) re-run."""
    try:
        text = subprocess.check_output(
            ["git", "show", f"{base_ref}:{path}"], text=True,
        )
    except subprocess.CalledProcessError:
        return set()
    urls: set[str] = set()
    for line in text.splitlines():
        m = ENTRY_RX.match(line)
        if m:
            urls.add(canon(m.group(2)))
    return urls


# URLs that are placeholder bullets, not real curated entries. They live in
# empty subsections to satisfy lint and act as a "suggest one" call to action.
# Skip them entirely.
PLACEHOLDER_URLS = {
    "https://github.com/frenck/awesome-home-assistant/issues/new/choose",
}


# ---- HTTP helpers -------------------------------------------------------

def gh_get(path: str) -> dict | None:
    url = f"{GITHUB_API}{path}"
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


# ---- Per-entry checks ---------------------------------------------------

def check_universal(e: Entry, f: Findings, all_urls: dict[str, list[Entry]]) -> None:
    parsed = urllib.parse.urlsplit(e.url)
    if parsed.scheme != "https":
        f.err(e, f"URL must use HTTPS, got `{parsed.scheme}://`.")
    host = (parsed.netloc or "").lower().lstrip("www.")
    if host in URL_SHORTENERS:
        f.err(e, f"URL uses shortener `{host}`. Submit the canonical URL.")
    # tracking params -> warn
    qs = urllib.parse.parse_qs(parsed.query, keep_blank_values=True)
    bad = sorted(set(qs) & TRACKING_PARAMS)
    if bad:
        f.warn(e, f"URL has tracking parameter(s): {', '.join(bad)} — strip them.")
    # duplicates
    dupes = [other for other in all_urls.get(canon(e.url), []) if other is not e]
    if dupes:
        labels = ", ".join(d.section_label for d in dupes)
        f.err(e, f"Duplicate URL — already listed under: {labels}.")


def canon(url: str) -> str:
    """Cheap canonical form: lowercase host, strip trailing slash + .git, drop fragment."""
    p = urllib.parse.urlsplit(url.rstrip("/"))
    path = re.sub(r"\.git$", "", p.path)
    return f"{p.scheme}://{p.netloc.lower()}{path}".rstrip("/")


def repo_from_url(url: str) -> tuple[str, str] | None:
    m = REPO_RX.match(url)
    if not m:
        return None
    return m.group(1), m.group(2).rstrip("/")


def check_software(e: Entry, f: Findings, *, allow_cc: bool = False, hacs: str | None = None) -> None:
    repo = repo_from_url(e.url)
    if repo is None:
        # Some entries in software-tagged sections link to a non-GitHub site
        # (project homepage). We let those through with a soft notice.
        f.warn(e, "Not a GitHub repository — repo-level checks skipped.")
        return
    owner, name = repo
    data = gh_get(f"/repos/{owner}/{name}")
    if data is None:
        f.err(e, f"Repository `{owner}/{name}` not found (404).")
        return
    if data.get("archived"):
        f.err(e, "Repository is archived.")
    # last push within 18 months
    pushed = data.get("pushed_at")
    if pushed:
        last = datetime.fromisoformat(pushed.replace("Z", "+00:00"))
        if datetime.now(timezone.utc) - last > timedelta(days=18 * 30):
            age_months = (datetime.now(timezone.utc) - last).days // 30
            f.err(e, f"No commits for {age_months} months (last push {pushed[:10]}); cap is 18.")
    # at least 6 months old
    created = data.get("created_at")
    if created:
        c = datetime.fromisoformat(created.replace("Z", "+00:00"))
        if datetime.now(timezone.utc) - c < timedelta(days=180):
            f.err(e, f"Repository created {created[:10]} — must be at least 6 months old.")
    # license
    spdx = ((data.get("license") or {}).get("spdx_id") or "")
    accepted = OSI_LICENSES | (CC_LICENSES if allow_cc else set())
    if not spdx or spdx in {"NOASSERTION", "Other"}:
        f.err(e, "No detectable open-source license.")
    elif spdx not in accepted:
        if spdx in CC_LICENSES and not allow_cc:
            f.err(e, f"License `{spdx}` is Creative Commons; this section requires an OSI-approved software license.")
        else:
            f.err(e, f"License `{spdx}` is not OSI-approved.")
    # README check
    readme = gh_get(f"/repos/{owner}/{name}/readme")
    if readme is None:
        f.err(e, "No README.md at repository root.")
    elif readme.get("content"):
        try:
            import base64
            body = base64.b64decode(readme["content"]).decode("utf-8", errors="replace").lower()
            if "home assistant" not in body:
                f.warn(e, "README does not mention 'Home Assistant'.")
        except Exception:
            pass
    # stars (warn only)
    stars = data.get("stargazers_count", 0)
    if stars < 10:
        f.warn(e, f"Repository has only {stars} stars — please justify in the PR description.")
    # HACS structure
    if hacs:
        hacs_data = gh_get(f"/repos/{owner}/{name}/contents/hacs.json")
        if hacs_data is None:
            f.err(e, "Missing `hacs.json` at repository root — required for HACS-installable entries.")


def check_universal_only(e: Entry, f: Findings) -> None:
    """Section requires only the universal checks."""
    pass  # universal already ran


def check_diy_optional_repo(e: Entry, f: Findings) -> None:
    repo = repo_from_url(e.url)
    if repo is None:
        return  # forum / blog link, universal-only
    check_software(e, f)


def check_public_config(e: Entry, f: Findings) -> None:
    """Like software, but no license check (personal HA configs)."""
    repo = repo_from_url(e.url)
    if repo is None:
        f.warn(e, "Not a GitHub repository — repo-level checks skipped.")
        return
    owner, name = repo
    data = gh_get(f"/repos/{owner}/{name}")
    if data is None:
        f.err(e, f"Repository `{owner}/{name}` not found.")
        return
    if data.get("archived"):
        f.err(e, "Repository is archived.")
    pushed = data.get("pushed_at")
    if pushed:
        last = datetime.fromisoformat(pushed.replace("Z", "+00:00"))
        if datetime.now(timezone.utc) - last > timedelta(days=18 * 30):
            age_months = (datetime.now(timezone.utc) - last).days // 30
            f.err(e, f"No commits for {age_months} months; cap is 18.")


CHECK_DISPATCH = {
    "software": lambda e, f: check_software(e, f),
    "software_hacs_integration": lambda e, f: check_software(e, f, hacs="integration"),
    "software_hacs_plugin": lambda e, f: check_software(e, f, hacs="plugin"),
    "software_or_cc": lambda e, f: check_software(e, f, allow_cc=True),
    "diy_optional_repo": check_diy_optional_repo,
    "public_config": check_public_config,
    "universal_only": check_universal_only,
    "content_blog": check_universal_only,    # freshness check is a separate cron job
    "content_youtube": check_universal_only, # ditto
    "content_podcast": check_universal_only, # ditto
    "skip": lambda e, f: None,
}


# ---- Driver -------------------------------------------------------------

def run(entries: Iterable[Entry], all_entries: list[Entry]) -> Findings:
    findings = Findings()
    by_url: dict[str, list[Entry]] = {}
    for e in all_entries:
        by_url.setdefault(canon(e.url), []).append(e)
    for e in entries:
        if e.rule == "skip":
            continue
        check_universal(e, findings, by_url)
        CHECK_DISPATCH.get(e.rule, lambda *_: None)(e, findings)
    return findings


def format_report(f: Findings, target: list[Entry], total: int, *, mode: str) -> str:
    """Render a Markdown report for the PR comment.

    Always returns a self-contained block, including the success case --
    contributors should see at a glance whether their PR is OK.
    """
    n = len(target)
    err = len(f.errors)
    warn = len(f.warnings)

    if n == 0:
        if mode == "pr":
            return (
                "## Awesome list validation\n\n"
                "ℹ️ **No new listing entries in this PR** -- nothing to "
                "validate.\n"
            )
        return (
            "## Awesome list validation\n\n"
            "ℹ️ No entries found in `README.md`. Did the file structure "
            "change?\n"
        )

    # Status line
    if err:
        status = (
            f"❌ **Blocking errors** -- validated {n} "
            f"{'entry' if n == 1 else 'entries'}: {err} error"
            f"{'s' if err != 1 else ''}, {warn} warning"
            f"{'s' if warn != 1 else ''}.\n\n"
            "Please address the errors below before this PR can be merged."
        )
    elif warn:
        status = (
            f"⚠️ **Passing with warnings** -- validated {n} "
            f"{'entry' if n == 1 else 'entries'}: 0 errors, {warn} warning"
            f"{'s' if warn != 1 else ''}.\n\n"
            "The warnings below are advisory, not blockers."
        )
    else:
        status = (
            f"✅ **All checks passed** -- validated {n} "
            f"{'entry' if n == 1 else 'entries'}."
        )

    parts = ["## Awesome list validation", "", status, ""]

    # Entries table (compact, easier to scan than a bullet list for >2 entries)
    parts.append("### Entries checked\n")
    parts.append("| Entry | Section | URL |")
    parts.append("|-------|---------|-----|")
    for e in target:
        nm = e.name.replace("|", "\\|")
        sec = e.section_label.replace("|", "\\|")
        parts.append(f"| {nm} | {sec} | {e.url} |")
    parts.append("")

    if f.errors:
        parts.append(f"### Errors ({err})\n")
        for e, msg in f.errors:
            parts.append(f"- **{e.name}** — *{e.section_label}*: {msg}")
            parts.append(f"  - {e.url}")
        parts.append("")

    if f.warnings:
        parts.append(f"### Warnings ({warn})\n")
        for e, msg in f.warnings:
            parts.append(f"- **{e.name}** — *{e.section_label}*: {msg}")
            parts.append(f"  - {e.url}")
        parts.append("")

    parts.extend([
        "<details>",
        "<summary>What was checked</summary>",
        "",
        "- URL hygiene (HTTPS, no shorteners, no duplicates, no tracking params)",
        "- Repository status (not archived, age ≥6 months, last push <18 months)",
        "- License (OSI-approved; CC accepted for *Other Awesome Lists*)",
        "- README presence and Home Assistant mention",
        "- HACS structure (`hacs.json`) for Custom Integrations and Custom Cards",
        "",
        "Full criteria: [.github/CONTRIBUTING.md]"
        "(https://github.com/frenck/awesome-home-assistant/blob/main/.github/"
        "CONTRIBUTING.md#acceptance-criteria).",
        "",
        "</details>",
        "",
    ])
    return "\n".join(parts)


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--readme", default="README.md")
    p.add_argument("--base", help="Base ref for diff mode (e.g. origin/main).")
    p.add_argument("--all", action="store_true",
                   help="Check every entry, not just newly-added ones.")
    args = p.parse_args()

    all_entries = parse_readme(args.readme)

    # Drop placeholder bullets (e.g. "Suggest one" links into the issue
    # tracker). They are framework, not curated entries.
    all_entries = [e for e in all_entries if e.url not in PLACEHOLDER_URLS]

    if args.all or not args.base:
        target = all_entries
    else:
        added_lines = diff_added_lines(args.base, args.readme)
        target = [e for e in all_entries if e.raw in added_lines]
        # Grandfather: in PR mode, an entry whose URL already existed on
        # the base ref is being moved/reformatted, not added. Repo-level
        # checks (archived, age, license, hacs.json) were valid when the
        # entry first landed; do not re-run them.
        existing = base_urls(args.base, args.readme)
        target = [e for e in target if canon(e.url) not in existing]
        if not target:
            print("No newly-added entries in this PR. Nothing to check.")
            return 0

    print(f"Checking {len(target)} entr{'y' if len(target) == 1 else 'ies'} "
          f"out of {len(all_entries)} total.")

    findings = run(target, all_entries)
    mode = "pr" if (args.base and not args.all) else "all"
    print(format_report(findings, target, len(all_entries), mode=mode))

    return 1 if findings.errors else 0


if __name__ == "__main__":
    sys.exit(main())
