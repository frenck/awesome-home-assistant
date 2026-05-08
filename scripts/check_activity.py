#!/usr/bin/env python3
"""Flag README entries pointing at archived, gone, or stale GitHub repos.

Reports rather than edits. The weekly maintenance workflow includes the
markdown report in the PR body so a human can decide whether to drop,
replace, or keep the entry.

Smart use of HACS: HACS removes archived integrations and plugins from
its public store, so every repo present in HACS is implicitly active.
We only hit the GitHub API for repos that are not in HACS (awesome-*
lists, blogs, non-HACS-installable tooling), and for those we get
archived status, 404, and `pushed_at` in a single response.

A repo is flagged when:

    * GitHub returns 404 (deleted, renamed without redirect, made private),
    * the repo has been archived,
    * it has not received an update in 730 days (~24 months).

Output is markdown to stdout. Exit code is always 0 regardless of how
many repos were flagged. This is informational, not a gate.

Usage:

    python scripts/check_activity.py             # markdown report to stdout
    python scripts/check_activity.py --readme custom/path.md
"""
from __future__ import annotations

import argparse
import datetime as dt
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
STALE_DAYS = 730  # ~24 months

REPO_RX = re.compile(
    r"^https?://github\.com/(?P<owner>[\w.-]+)/(?P<repo>[^/#?\s]+?)(?:\.git)?(?:/#.*|#.*|/)?$",
    re.IGNORECASE,
)
ENTRY_RX = re.compile(
    r"^\s*-\s*(?:\S+\s+)?\[(?P<name>[^\]]+)\]\((?P<url>https?://[^)\s]+)\)"
)


def fetch_repo(owner: str, repo: str) -> dict:
    """GitHub /repos response, or {'_404': True} if the repo is gone."""
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
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return {"_404": True}
        raise


def parse_iso(value: str | None) -> dt.datetime | None:
    if not value:
        return None
    return dt.datetime.fromisoformat(value.replace("Z", "+00:00"))


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n", 1)[0])
    p.add_argument("--readme", default="README.md")
    args = p.parse_args()

    text = open(args.readme).read()
    by_repo: dict[tuple[str, str], list[tuple[int, str]]] = {}
    for idx, line in enumerate(text.splitlines(), start=1):
        m = ENTRY_RX.match(line)
        if not m:
            continue
        rm = REPO_RX.match(m.group("url"))
        if not rm:
            continue
        key = (rm.group("owner").lower(), rm.group("repo").lower())
        by_repo.setdefault(key, []).append((idx, m.group("name")))

    print(f"Activity check: {len(by_repo)} unique repos referenced.", file=sys.stderr)
    print("Loading HACS index...", file=sys.stderr)
    hacs = load_hacs_index()
    print(f"  HACS index: {len(hacs)} repos.", file=sys.stderr)

    now = dt.datetime.now(dt.timezone.utc)
    cutoff = now - dt.timedelta(days=STALE_DAYS)

    archived: list[tuple[str, list[tuple[int, str]]]] = []
    missing: list[tuple[str, list[tuple[int, str]]]] = []
    stale: list[tuple[str, int, list[tuple[int, str]]]] = []

    api_pending: list[tuple[str, str]] = []
    for key, occurrences in by_repo.items():
        info = hacs.get(key)
        if info is not None:
            # HACS knows this repo, so it is active and not archived.
            # Use HACS `last_updated` for the staleness check.
            ts = parse_iso(info.get("last_updated"))
            if ts and ts < cutoff:
                stale.append((f"{key[0]}/{key[1]}", (now - ts).days, occurrences))
        else:
            api_pending.append(key)

    print(
        f"  {len(by_repo) - len(api_pending)} resolved via HACS, "
        f"{len(api_pending)} need GitHub API.",
        file=sys.stderr,
    )

    if api_pending:
        with ThreadPoolExecutor(max_workers=8) as ex:
            futures = {ex.submit(fetch_repo, o, r): (o, r) for o, r in api_pending}
            for fut in as_completed(futures):
                key = futures[fut]
                occurrences = by_repo[key]
                full = f"{key[0]}/{key[1]}"
                try:
                    info = fut.result()
                except Exception as e:
                    print(f"  ! error fetching {full}: {e}", file=sys.stderr)
                    continue
                if info.get("_404"):
                    missing.append((full, occurrences))
                    continue
                if info.get("archived"):
                    archived.append((full, occurrences))
                    continue
                ts = parse_iso(info.get("pushed_at"))
                if ts and ts < cutoff:
                    stale.append((full, (now - ts).days, occurrences))

    def fmt_cite(occurrences: list[tuple[int, str]]) -> str:
        return ", ".join(f"L{ln} `{nm}`" for ln, nm in occurrences)

    print("## Activity check")
    print()
    if not (missing or archived or stale):
        print(
            f"All entries pass the activity check (no archived, missing, or "
            f"{STALE_DAYS}+ day stale repos)."
        )
        return 0

    if missing:
        print(f"### Missing or renamed ({len(missing)})")
        print()
        print(
            "These URLs return 404. Likely candidates for removal or "
            "replacement."
        )
        print()
        for full, occ in sorted(missing):
            print(f"- [{full}](https://github.com/{full}): {fmt_cite(occ)}")
        print()

    if archived:
        print(f"### Archived ({len(archived)})")
        print()
        print(
            "Owners have archived these repos. Not always a removal trigger. "
            "Some projects archive after reaching feature complete but still "
            "work fine. Review case by case."
        )
        print()
        for full, occ in sorted(archived):
            print(f"- [{full}](https://github.com/{full}): {fmt_cite(occ)}")
        print()

    if stale:
        print(f"### Stale ({len(stale)})")
        print()
        print(
            f"No update in {STALE_DAYS}+ days. Some smart-home tools simply "
            "do not need updates; others are abandoned. Spot-check before "
            "removing."
        )
        print()
        for full, age, occ in sorted(stale, key=lambda x: -x[1]):
            print(f"- [{full}](https://github.com/{full}): {age}d ago, {fmt_cite(occ)}")
        print()

    return 0


if __name__ == "__main__":
    sys.exit(main())
