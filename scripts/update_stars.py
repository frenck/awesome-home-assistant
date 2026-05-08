#!/usr/bin/env python3
"""Update inline star counts in README.md.

For every entry that links to a GitHub repository, fetch the current
stargazer count and write `(N★)` at the end of the description, just
before the trailing period. Re-running updates counts in place.

To stay friendly to GitHub's rate limit, the script first pulls the
HACS public data index (one HTTPS request per category, no auth) and
uses it as the primary source of star counts. Only repos that are not
in HACS fall through to the GitHub API.

Usage:

    python scripts/update_stars.py             # updates README.md in place
    python scripts/update_stars.py --check     # dry run; nonzero exit if changes needed
    python scripts/update_stars.py --readme custom/path.md

Auth: reads `GITHUB_TOKEN` from the environment if set. Without it the
GitHub API gives you ~60 requests/hour, which is not enough for a full
sweep of this list. Locally:

    GITHUB_TOKEN=$(gh auth token) python scripts/update_stars.py
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

from _hacs import load_hacs_index

GITHUB_API = "https://api.github.com"
TOKEN = os.environ.get("GITHUB_TOKEN", "")

# Match a GitHub repo URL pointing at the repo root. Trailing `.git` or
# `#anchor` are accepted; subpaths like `/blob/...` or `/tree/...` are
# rejected because their star count would belong to the umbrella repo,
# not the linked thing (e.g. each Official App docs link returning the
# `hassio-addons` monorepo's count would be misleading).
REPO_RX = re.compile(
    r"^https?://github\.com/(?P<owner>[\w.-]+)/(?P<repo>[^/#?\s]+?)(?:\.git)?(?:/#.*|#.*|/)?$",
    re.IGNORECASE,
)

# Match an awesome-list entry line. Captures the prefix up to the link,
# the separator, the description text, an optional existing star group at
# the end (so re-runs can replace it), and the trailing period.
ENTRY_RX = re.compile(
    r"^(?P<prefix>\s*-\s*(?:\S+\s+)?\[(?P<name>[^\]]+)\]\((?P<url>https?://[^)\s]+)\))"
    r"(?P<sep>\s*-\s*)"
    r"(?P<desc>.*?)"
    r"(?:\s*\((?P<old_stars>[\d,]+)★\))?"
    r"(?P<period>\.\s*)$"
)


def fetch_stars(owner: str, repo: str) -> int | None:
    """Return the stargazer count for a repository, or None on 404."""
    url = f"{GITHUB_API}/repos/{owner}/{repo}"
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            return json.loads(r.read()).get("stargazers_count", 0)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


def update_text(text: str, dry_run: bool = False) -> tuple[str, int, int]:
    """Return (new_text, lines_updated, repos_seen)."""
    lines = text.splitlines()
    pending: dict[tuple[str, str], list[int]] = {}

    for idx, line in enumerate(lines):
        m = ENTRY_RX.match(line)
        if not m:
            continue
        rm = REPO_RX.match(m.group("url"))
        if not rm:
            continue
        key = (rm.group("owner").lower(), rm.group("repo").lower())
        pending.setdefault(key, []).append(idx)

    print(f"  {len(pending)} unique GitHub repos referenced.")

    # HACS-first: try to satisfy as many lookups as possible from the
    # HACS public data, falling back to the GitHub API only for repos
    # that HACS does not know about (awesome-* lists, blogs, tooling).
    print("  Loading HACS index...")
    hacs = load_hacs_index()
    print(f"  HACS index: {len(hacs)} repos.")

    star_by_repo: dict[tuple[str, str], int | None] = {}
    api_pending: list[tuple[str, str]] = []
    for key in pending:
        info = hacs.get(key)
        if info and info.get("stargazers_count") is not None:
            star_by_repo[key] = info["stargazers_count"]
        else:
            api_pending.append(key)
    print(f"  {len(star_by_repo)} resolved via HACS, {len(api_pending)} need GitHub API.")

    if api_pending:
        with ThreadPoolExecutor(max_workers=8) as ex:
            futures = {
                ex.submit(fetch_stars, owner, repo): (owner, repo)
                for (owner, repo) in api_pending
            }
            for fut in as_completed(futures):
                key = futures[fut]
                try:
                    star_by_repo[key] = fut.result()
                except Exception as e:
                    star_by_repo[key] = None
                    print(f"  ! error fetching {key[0]}/{key[1]}: {e}", file=sys.stderr)

    updated = 0
    for key, indices in pending.items():
        fresh = star_by_repo.get(key)
        for i in indices:
            old = lines[i]
            m = ENTRY_RX.match(old)
            if not m:
                continue
            # Prefer freshly-fetched stars; fall back to whatever count is
            # already on the line so format-only adjustments still apply
            # when a fetch fails (rate limits, 404s, etc.).
            if fresh is not None:
                count = fresh
            elif m.group("old_stars"):
                count = int(m.group("old_stars").replace(",", ""))
            else:
                continue
            new = (
                m.group("prefix")
                + m.group("sep")
                + m.group("desc").rstrip()
                + f" ({count:,}★)"
                + m.group("period")
            )
            if old != new:
                lines[i] = new
                updated += 1

    new_text = "\n".join(lines)
    if text.endswith("\n"):
        new_text += "\n"
    return new_text, updated, len(pending)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n", 1)[0])
    p.add_argument("--readme", default="README.md")
    p.add_argument("--check", action="store_true",
                   help="Dry run. Exits non-zero if any line would change.")
    args = p.parse_args()

    text = open(args.readme).read()
    print(f"Scanning {args.readme} ...")
    new_text, updated, repos = update_text(text)
    print(f"Lines that would change: {updated} (across {repos} repos).")

    if args.check:
        return 1 if updated else 0

    if updated:
        open(args.readme, "w").write(new_text)
        print(f"Wrote {args.readme}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
