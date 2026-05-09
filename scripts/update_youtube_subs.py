#!/usr/bin/env python3
"""Update inline subscriber counts in the YouTube Channels section of README.md.

For every entry inside `### 📺 YouTube Channels` (and its sub-subsections),
fetch the current subscriber count via the YouTube Data API v3 and write
`(N subs)` at the end of the description, just before the trailing period.
Re-running updates counts in place.

Channel URLs in any of these forms are resolved to a UC channel id:

    https://www.youtube.com/channel/UC...
    https://www.youtube.com/@handle
    https://www.youtube.com/c/CustomName
    https://www.youtube.com/user/LegacyName
    https://www.youtube.com/CustomName

The first hit is exact; the rest are resolved via the API or by scraping
the channel page (with a consent cookie so EU IPs see the actual page
instead of the consent wall). Resolved channel ids are cached in
`scripts/youtube_channel_cache.json` so subsequent runs only pay for the
statistics call (1 quota unit per 50 channels).

Usage:

    python scripts/update_youtube_subs.py             # updates README.md
    python scripts/update_youtube_subs.py --check     # dry run, nonzero on diff
    python scripts/update_youtube_subs.py --readme custom/path.md
    python scripts/update_youtube_subs.py --report    # print sub counts then exit

Auth: requires `YOUTUBE_API_KEY` in the environment. Get one from
https://console.cloud.google.com/ by enabling YouTube Data API v3.
The free tier is 10,000 quota units/day, which is far more than enough
to run this nightly.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

API_BASE = "https://www.googleapis.com/youtube/v3"
API_KEY = os.environ.get("YOUTUBE_API_KEY", "")

CACHE_PATH = Path(__file__).parent / "youtube_channel_cache.json"

# EU consent-wall bypass: pretend the user has already accepted cookies.
# Accept-Language forces English so scraped sub-count text is parseable.
CONSENT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
    ),
    "Cookie": "CONSENT=YES+cb.20210328-17-p0.en+FX+000",
    "Accept-Language": "en-US,en;q=0.9",
}

# Awesome-list entry pattern. Captures an optional flag prefix (e.g. 🇩🇪),
# a YouTube channel link, the description, and an optional existing
# `(N subs)` group so reruns can replace it.
ENTRY_RX = re.compile(
    r"^(?P<prefix>\s*-\s*(?:\S+\s+)?\[(?P<name>[^\]]+)\]"
    r"\((?P<url>https?://(?:www\.)?youtube\.com/[^)\s]+)\))"
    r"(?P<sep>\s*-\s*)"
    r"(?P<desc>.*?)"
    r"(?:\s*\((?P<old>[\d.]+[KM]?\s*subs)\))?"
    r"(?P<period>\.\s*)$"
)

# URL shape detection.
CHANNEL_ID_RX = re.compile(r"/channel/(UC[\w-]{20,24})", re.IGNORECASE)
HANDLE_RX = re.compile(r"/@([A-Za-z0-9._-]+)")
USER_RX = re.compile(r"/user/([A-Za-z0-9_-]+)", re.IGNORECASE)
LEGACY_C_RX = re.compile(r"/c/([A-Za-z0-9_-]+)", re.IGNORECASE)
VANITY_RX = re.compile(r"/(?!channel/|@|user/|c/|playlist|watch)([A-Za-z0-9_-]+)/?$")

# Match the channel id embedded in a YouTube channel page's HTML.
# `externalId` belongs to the page's own channel; `channelId` can refer
# to other channels (featured / recommended) so it is only a fallback.
PAGE_EXTERNAL_ID_RX = re.compile(r'"externalId":"(UC[\w-]{20,24})"')
PAGE_CHANNEL_ID_RX = re.compile(r'"channelId":"(UC[\w-]{20,24})"')

# Match the subscriber-count text on a channel page (English locale).
# YouTube renders other channels' counts via `simpleText`; the page's own
# channel uses `metadataParts` -> `content`. Anchoring to "content" picks
# only the canonical count and skips featured / recommended channels.
# Examples: "940 subscribers", "9.74K subscribers", "1.2M subscribers".
PAGE_SUBS_RX = re.compile(
    r'"content":"([0-9][0-9.,]*)\s*([KM])?\s*subscribers?"',
    re.IGNORECASE,
)


def load_cache() -> dict[str, str]:
    if CACHE_PATH.exists():
        try:
            return json.loads(CACHE_PATH.read_text())
        except json.JSONDecodeError:
            return {}
    return {}


def save_cache(cache: dict[str, str]) -> None:
    CACHE_PATH.write_text(
        json.dumps(dict(sorted(cache.items())), indent=2) + "\n",
    )


def api_get(path: str, **params: str) -> dict:
    """Call the YouTube Data API and return the parsed JSON body."""
    if not API_KEY:
        raise RuntimeError("YOUTUBE_API_KEY is not set in the environment.")
    params["key"] = API_KEY
    url = f"{API_BASE}/{path}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read())


def fetch_channel_page(url: str) -> str | None:
    """Fetch a YouTube channel page in English with the consent cookie set."""
    sep = "&" if "?" in url else "?"
    req = urllib.request.Request(url + sep + "hl=en", headers=CONSENT_HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            return r.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        print(f"  ! HTTP {e.code} fetching {url}", file=sys.stderr)
        return None


def scrape_channel_id(url: str) -> str | None:
    body = fetch_channel_page(url)
    if not body:
        return None
    m = PAGE_EXTERNAL_ID_RX.search(body) or PAGE_CHANNEL_ID_RX.search(body)
    return m.group(1) if m else None


def scrape_subs(url: str) -> int | None:
    """Pull the subscriber count off a channel page (fallback when no API key)."""
    body = fetch_channel_page(url)
    if not body:
        return None
    m = PAGE_SUBS_RX.search(body)
    if not m:
        return None
    raw, suffix = m.group(1), m.group(2)
    value = float(raw.replace(",", ""))
    if suffix and suffix.upper() == "K":
        value *= 1_000
    elif suffix and suffix.upper() == "M":
        value *= 1_000_000
    return int(value)


def resolve_channel_id(url: str, cache: dict[str, str]) -> str | None:
    """Resolve a YouTube URL to a UC channel id, using the cache when possible.

    Tries the API first when a key is available; falls back to scraping the
    channel page (which exposes `externalId` in its embedded JSON).
    """
    if url in cache:
        return cache[url]

    m = CHANNEL_ID_RX.search(url)
    if m:
        cache[url] = m.group(1)
        return cache[url]

    if API_KEY:
        m = HANDLE_RX.search(url)
        if m:
            try:
                data = api_get("channels", part="id", forHandle=f"@{m.group(1)}")
            except urllib.error.HTTPError as e:
                print(f"  ! API error for handle @{m.group(1)}: {e}", file=sys.stderr)
                data = {}
            items = data.get("items", [])
            if items:
                cache[url] = items[0]["id"]
                return cache[url]

        m = USER_RX.search(url)
        if m:
            try:
                data = api_get("channels", part="id", forUsername=m.group(1))
            except urllib.error.HTTPError as e:
                print(f"  ! API error for user {m.group(1)}: {e}", file=sys.stderr)
                data = {}
            items = data.get("items", [])
            if items:
                cache[url] = items[0]["id"]
                return cache[url]

    cid = scrape_channel_id(url)
    if cid:
        cache[url] = cid
        return cid
    return None


def fetch_subs(channel_ids: list[str]) -> dict[str, int]:
    """Return {channel_id: subscriber_count} for the given UC ids."""
    out: dict[str, int] = {}
    for chunk_start in range(0, len(channel_ids), 50):
        chunk = channel_ids[chunk_start:chunk_start + 50]
        try:
            data = api_get(
                "channels",
                part="statistics",
                id=",".join(chunk),
                maxResults="50",
            )
        except urllib.error.HTTPError as e:
            print(f"  ! API error fetching stats: {e}", file=sys.stderr)
            continue
        for item in data.get("items", []):
            stats = item.get("statistics", {})
            if stats.get("hiddenSubscriberCount"):
                continue
            try:
                out[item["id"]] = int(stats["subscriberCount"])
            except (KeyError, ValueError):
                continue
    return out


def format_subs(count: int) -> str:
    """Render a subscriber count YouTube-style."""
    if count < 1_000:
        return f"{count} subs"
    if count < 1_000_000:
        value = count / 1_000
        text = f"{value:.1f}".rstrip("0").rstrip(".")
        return f"{text}K subs"
    value = count / 1_000_000
    text = f"{value:.2f}".rstrip("0").rstrip(".")
    return f"{text}M subs"


def find_section_bounds(lines: list[str]) -> tuple[int, int]:
    """Return [start, end) line indices spanning the YouTube Channels section."""
    start = -1
    for i, line in enumerate(lines):
        if line.strip().startswith("### ") and "YouTube Channels" in line:
            start = i + 1
            break
    if start == -1:
        return (-1, -1)
    end = len(lines)
    for j in range(start, len(lines)):
        if lines[j].startswith("### "):
            end = j
            break
    return (start, end)


def update_text(text: str) -> tuple[str, int, int, dict[str, int]]:
    """Return (new_text, lines_updated, channels_seen, subs_by_url)."""
    lines = text.splitlines()
    section_start, section_end = find_section_bounds(lines)
    if section_start == -1:
        print("  ! YouTube Channels section not found.", file=sys.stderr)
        return text, 0, 0, {}

    cache = load_cache()
    pending: list[tuple[int, re.Match[str], str]] = []
    for i in range(section_start, section_end):
        m = ENTRY_RX.match(lines[i])
        if m:
            pending.append((i, m, m.group("url")))
    print(f"  {len(pending)} YouTube entries in section.")

    url_to_channel: dict[str, str] = {}
    for _, _, url in pending:
        cid = resolve_channel_id(url, cache)
        if cid:
            url_to_channel[url] = cid
        else:
            print(f"  ! could not resolve {url}", file=sys.stderr)
    save_cache(cache)
    print(f"  {len(url_to_channel)} channels resolved.")

    subs_by_url: dict[str, int] = {}
    if API_KEY:
        subs_by_id = fetch_subs(list(set(url_to_channel.values())))
        print(f"  {len(subs_by_id)} subscriber counts fetched via API.")
        subs_by_url = {
            url: subs_by_id[cid]
            for url, cid in url_to_channel.items()
            if cid in subs_by_id
        }
    else:
        print("  YOUTUBE_API_KEY not set, scraping subscriber counts ...")
        for url in url_to_channel:
            count = scrape_subs(url)
            if count is not None:
                subs_by_url[url] = count
        print(f"  {len(subs_by_url)} subscriber counts scraped.")

    updated = 0
    for i, m, url in pending:
        count = subs_by_url.get(url)
        if count is None:
            continue
        new = (
            m.group("prefix")
            + m.group("sep")
            + m.group("desc").rstrip()
            + f" ({format_subs(count)})"
            + m.group("period")
        )
        if lines[i] != new:
            lines[i] = new
            updated += 1

    new_text = "\n".join(lines)
    if text.endswith("\n"):
        new_text += "\n"
    return new_text, updated, len(pending), subs_by_url


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n", 1)[0])
    p.add_argument("--readme", default="README.md")
    p.add_argument("--check", action="store_true",
                   help="Dry run. Exits non-zero if any line would change.")
    p.add_argument("--report", action="store_true",
                   help="Print {url: subs} as JSON and exit without writing.")
    args = p.parse_args()

    text = Path(args.readme).read_text()
    print(f"Scanning {args.readme} ...")
    new_text, updated, seen, subs = update_text(text)

    if args.report:
        print(json.dumps(subs, indent=2, sort_keys=True))
        return 0

    print(f"Lines that would change: {updated} (across {seen} entries).")

    if args.check:
        return 1 if updated else 0

    if updated:
        Path(args.readme).write_text(new_text)
        print(f"Wrote {args.readme}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
