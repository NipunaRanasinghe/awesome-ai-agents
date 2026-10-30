#!/usr/bin/env python3
"""Report EMERGING.md entries to move to the main list or remove.

Usage: check_emerging.py [--today YYYY-MM-DD] > report.md

For each row of the form `| [Name](https://github.com/owner/repo) | ... |`
in EMERGING.md, fetches the repo from the GitHub API (GITHUB_TOKEN is used
if set) and lists it as:

- ready to move: the repo has at least MOVE_STARS stars and a push in the
  last MAIN_STALE_DAYS days (the main list's activity bar);
- to remove: the repo is archived or not found, has no push for STALE_DAYS
  days, or was added (`Added` column, YYYY-MM) more than EXPIRE_MONTHS
  calendar months ago, so it has been listed at least EXPIRE_MONTHS months;
- to check by hand: the link is not a GitHub repo, or `Added` is malformed.

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
MAIN_STALE_DAYS = 182
EXPIRE_MONTHS = 6

ENTRY_ROW = re.compile(r"^\| *\[([^\]]+)\]\((https://github\.com/([^/\s)]+/[^/\s)#?]+))\)")


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def entries(text):
    """Yield (name, url, repo, added) for each entry row.

    The first table row is the header. For rows that do not link to a
    GitHub repo, url and repo are None and name is the raw first cell."""
    header = None
    for line in text.splitlines():
        if not line.startswith("|") or re.match(r"^[|\s\-]+$", line):
            continue
        row = cells(line)
        if header is None:
            header = [c.lower() for c in row]
            continue
        i = header.index("added") if "added" in header else len(row)
        added = row[i] if i < len(row) else ""
        m = ENTRY_ROW.match(line)
        if not m:
            yield row[0], None, None, added
            continue
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
    main_stale_before = (today - timedelta(days=MAIN_STALE_DAYS)).isoformat()

    move, remove, manual = [], [], []
    for name, url, repo, added in entries(Path("EMERGING.md").read_text()):
        if repo is None:
            manual.append(f"- {name}: not a GitHub repo link")
            continue
        link = f"[{name}]({url})"
        data = fetch_repo(repo)
        if data is None:
            remove.append(f"- {link}: repo not found")
            continue
        if data["pushed_at"] is None:
            remove.append(f"- {link}: empty repo")
            continue
        stars = data["stargazers_count"]
        pushed = data["pushed_at"][:10]
        age = months_between(added, today)
        if data["archived"]:
            remove.append(f"- {link}: archived")
        elif stars >= MOVE_STARS and pushed >= main_stale_before:
            move.append(f"- {link}: {stars} stars")
        elif pushed < stale_before:
            remove.append(f"- {link}: no push since {pushed}")
        elif age is None:
            manual.append(f"- {link}: `Added` column is not YYYY-MM ({added!r})")
        elif age > EXPIRE_MONTHS:
            remove.append(f"- {link}: {stars} stars, added {added}")

    if not move and not remove and not manual:
        return
    out = [f"Monthly check of [EMERGING.md](https://github.com/NipunaRanasinghe/awesome-ai-agents/blob/main/EMERGING.md) on {today}.", ""]
    if move:
        out += [f"### Ready to move to the main list ({MOVE_STARS}+ stars)", ""] + move + [""]
    if remove:
        out += [
            f"### To remove (archived, not found, no push for {STALE_DAYS} days, "
            f"or below the bar {EXPIRE_MONTHS}+ months after being added)",
            "",
        ] + remove + [""]
    if manual:
        out += ["### To check by hand", ""] + manual + [""]
    print("\n".join(out).rstrip())


if __name__ == "__main__":
    main()
