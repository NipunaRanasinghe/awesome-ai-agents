#!/usr/bin/env python3
"""Prepend README entry changes between two commits to CHANGELOG.md.

Usage: update_changelog.py <base-sha> <head-sha> [--date YYYY-MM-DD]

Reads the README.md diff between the two commits, extracts added and
removed table entries (rows of the form `| [Name](url) | ... |`), and
writes them under a date heading in CHANGELOG.md. Rows whose link is
unchanged (formatting-only edits) are ignored; rows where the same name
appears with a different URL are recorded as link updates.
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

ENTRY_ROW = re.compile(r"^\| *\[([^\]]+)\]\((https?://[^)\s]+)\)")
HEADING = re.compile(r"^(#{2,3}) +(.*\S)")

CHANGELOG = Path("CHANGELOG.md")
HEADER = (
    "# Changelog\n"
    "\n"
    "Entries added to or removed from the list, generated automatically "
    "from README changes on each merge to main. Newest first.\n"
)


def git(*args):
    return subprocess.run(
        ["git", *args], check=True, capture_output=True, text=True
    ).stdout


def diff_entries(base, head):
    """Return ({url: name} added, {url: name} removed) between two commits."""
    diff = git("diff", base, head, "--", "README.md")
    added, removed = {}, {}
    for line in diff.splitlines():
        if line.startswith("+"):
            m = ENTRY_ROW.match(line[1:])
            if m:
                added[m.group(2)] = m.group(1)
        elif line.startswith("-"):
            m = ENTRY_ROW.match(line[1:])
            if m:
                removed[m.group(2)] = m.group(1)
    # Same URL on both sides = formatting-only change; drop it.
    for url in set(added) & set(removed):
        del added[url]
        del removed[url]
    return added, removed


def section_map(head):
    """Map entry URL -> nearest preceding section heading in README at head."""
    sections = {}
    current = ""
    for line in git("show", f"{head}:README.md").splitlines():
        h = HEADING.match(line)
        if h:
            current = h.group(2)
            continue
        m = ENTRY_ROW.match(line)
        if m:
            sections[m.group(2)] = current
    return sections


def build_lines(added, removed, sections):
    lines = []
    # Same name on both sides with different URLs = repo moved/renamed.
    renamed = {
        name: url
        for url, name in removed.items()
        if name in added.values()
    }
    for url, name in sorted(added.items(), key=lambda kv: kv[1].lower()):
        if name in renamed:
            lines.append(f"- Updated [{name}]({url}) link (repo moved)")
        elif sections.get(url):
            lines.append(f"- Added [{name}]({url}) to {sections[url]}")
        else:
            lines.append(f"- Added [{name}]({url})")
    for url, name in sorted(removed.items(), key=lambda kv: kv[1].lower()):
        if name not in renamed:
            lines.append(f"- Removed {name}")
    return lines


def update_changelog(date, lines):
    text = CHANGELOG.read_text() if CHANGELOG.exists() else HEADER
    date_heading = f"## {date}"
    body = text.splitlines()
    if date_heading in body:
        # Merge into the existing section for this date, skipping duplicates.
        start = body.index(date_heading)
        i = start + 1
        while i < len(body) and not body[i].startswith("## "):
            i += 1
        # Back up over the section's trailing blank lines.
        while i - 1 > start + 1 and body[i - 1] == "":
            i -= 1
        existing = set(body[start:i])
        body[i:i] = [l for l in lines if l not in existing]
    else:
        # Insert a new date section before the first existing one.
        insert_at = next(
            (i for i, l in enumerate(body) if l.startswith("## ")), len(body)
        )
        if insert_at == len(body) and body and body[-1] != "":
            body.append("")
            insert_at += 1
        body[insert_at:insert_at] = [date_heading, ""] + lines + [""]
    CHANGELOG.write_text("\n".join(body).rstrip() + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("base")
    parser.add_argument("head")
    parser.add_argument("--date", help="YYYY-MM-DD; defaults to head commit date")
    args = parser.parse_args()

    date = args.date or git(
        "log", "-1", "--format=%cs", args.head
    ).strip()
    added, removed = diff_entries(args.base, args.head)
    if not added and not removed:
        print("No entry changes; changelog untouched.")
        return
    lines = build_lines(added, removed, section_map(args.head))
    update_changelog(date, lines)
    print(f"Recorded {len(lines)} change(s) under {date}.")


if __name__ == "__main__":
    main()
