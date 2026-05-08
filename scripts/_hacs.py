"""Helpers for the HACS public data index.

HACS publishes its default-store metadata as one plain JSON file per
category. No auth, no rate limit. Each entry has a `full_name`, a
`stargazers_count`, and a `last_updated` timestamp, which is exactly
what `update_stars.py` and `check_activity.py` both need.

Bonus: HACS removes archived projects from its public store, so any
repo present in this index is implicitly known to be active and not
archived. That lets the activity check skip the GitHub API for ~40% of
the listing.
"""
from __future__ import annotations

import json
import sys
import urllib.error
import urllib.request

HACS_DATA_BASE = "https://data-v2.hacs.xyz"
HACS_CATEGORIES = (
    "integration",
    "plugin",
    "theme",
    "appdaemon",
    "python_script",
    "netdaemon",
)


def load_hacs_index() -> dict[tuple[str, str], dict]:
    """Return a {(owner_lc, repo_lc): {stargazers_count, last_updated}} map.

    One HTTPS request per category, no auth required. Entries missing a
    `full_name` are skipped. Either field on the value dict may be None
    when HACS does not have that value for an entry.
    """
    table: dict[tuple[str, str], dict] = {}
    headers = {"User-Agent": "awesome-home-assistant-maintenance"}
    for category in HACS_CATEGORIES:
        url = f"{HACS_DATA_BASE}/{category}/data.json"
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                data = json.loads(r.read())
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as e:
            print(f"  ! HACS {category} unavailable: {e}", file=sys.stderr)
            continue
        for info in data.values():
            full = (info.get("full_name") or "").lower()
            if "/" not in full:
                continue
            owner, repo = full.split("/", 1)
            table[(owner, repo)] = {
                "stargazers_count": info.get("stargazers_count"),
                "last_updated": info.get("last_updated"),
            }
    return table
