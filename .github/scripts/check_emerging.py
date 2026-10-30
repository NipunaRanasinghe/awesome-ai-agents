#!/usr/bin/env python3
"""Report EMERGING.md entries to move to the main list or remove.

Usage: check_emerging.py [--today YYYY-MM-DD] > report.md

For each row of the form `| [Name](https://github.com/owner/repo) | ... |`
in EMERGING.md, fetches the repo from the GitHub API (GITHUB_TOKEN is used
if set) and lists it as:

- ready to move: the repo has at least MOVE_STARS stars;
- to remove: no push for STALE_DAYS days, or added (`Added` column,
  YYYY-MM) at least EXPIRE_MONTHS months ago, or the repo is archived or
  not found.

Prints a markdown report, or nothing when there is nothing to report.
"""

import argparse
import json
import os
import re
import urllib.error
import urllib.request
from datetime import date, timedelta
from pathlib import Path

MOVE_STARS = 50
STALE_DAYS = 90
EXPIRE_MONTHS = 6

ENTRY_ROW = re.compile(r"^\| *\[([^\]]+)\]\((https://github\.com/([^/\s)]+/[^/\s)#?]+))\)")


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def entries(text):
    """Yield (name, url, repo, added) for each entry row."""
    header = None
    for line in text.splitlines():
        if not line.startswith("|") or re.match(r"^[|\s\-]+$", line):
            continue
        row = cells(line)
        m = ENTRY_ROW.match(line)
        if not m:
            header = [c.lower() for c in row]
            continue
        added = row[header.index("added")] if header and "added" in header else ""
        yield m.group(1), m.group(2), m.group(3), added


def fetch_repo(repo):
    req = urllib.request.Request(f"https://api.github.com/repos/{repo}")
    req.add_header("Accept", "application/vnd.github+json")
    if os.environ.get("GITHUB_TOKEN"):
        req.add_header("Authorization", f"Bearer {os.environ['GITHUB_TOKEN']}")
    try:
        with urllib.request.urlopen(req) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


def months_between(added, today):
    """Whole months from YYYY-MM to today, or None if `added` is malformed."""
    m = re.fullmatch(r"(\d{4})-(\d{2})", added)
    if not m:
        return None
    return (today.year - int(m.group(1))) * 12 + today.month - int(m.group(2))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--today", help="YYYY-MM-DD; defaults to today")
    args = parser.parse_args()
    today = date.fromisoformat(args.today) if args.today else date.today()
    stale_before = (today - timedelta(days=STALE_DAYS)).isoformat()

    move, remove = [], []
    for name, url, repo, added in entries(Path("EMERGING.md").read_text()):
        link = f"[{name}]({url})"
        data = fetch_repo(repo)
        if data is None:
            remove.append(f"- {link}: repo not found")
            continue
        stars = data["stargazers_count"]
        age = months_between(added, today)
        if data["archived"]:
            remove.append(f"- {link}: archived")
        elif data["pushed_at"][:10] < stale_before:
            remove.append(f"- {link}: no push since {data['pushed_at'][:10]}")
        elif stars >= MOVE_STARS:
            move.append(f"- {link}: {stars} stars")
        elif age is None:
            remove.append(f"- {link}: `Added` column is not YYYY-MM ({added!r}), fix by hand")
        elif age >= EXPIRE_MONTHS:
            remove.append(f"- {link}: {stars} stars after {age} months")

    if not move and not remove:
        return
    out = [f"Monthly check of [EMERGING.md](https://github.com/NipunaRanasinghe/awesome-ai-agents/blob/main/EMERGING.md) on {today}.", ""]
    if move:
        out += [f"### Ready to move to the main list ({MOVE_STARS}+ stars)", ""] + move + [""]
    if remove:
        out += [
            f"### To remove (no push for {STALE_DAYS} days, or below the bar "
            f"{EXPIRE_MONTHS} months after being added)",
            "",
        ] + remove + [""]
    print("\n".join(out).rstrip())


if __name__ == "__main__":
    main()
