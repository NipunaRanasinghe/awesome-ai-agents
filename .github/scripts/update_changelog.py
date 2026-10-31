#!/usr/bin/env python3
"""Prepend README entry changes between two commits to CHANGELOG.md.

Usage: update_changelog.py <base-sha> <head-sha> [--date YYYY-MM-DD]

Reads the README.md and EMERGING.md diffs between the two commits,
extracts added and removed table entries (rows of the form
`| [Name](url) | ... |`), and writes them under a date heading in
CHANGELOG.md. Rows whose link is unchanged within a file (formatting-only
edits) are ignored; rows whose link moves between the files are recorded
as moves; rows where the same name appears with a different URL are
recorded as link updates.
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

ENTRY_ROW = re.compile(r"^\| *\[([^\]]+)\]\((https?://[^)\s]+)\)")
HEADING = re.compile(r"^(#{2,3}) +(.*\S)")

CHANGELOG = Path("CHANGELOG.md")
LIST_FILES = ("README.md", "EMERGING.md")
HEADER = (
    "# Changelog\n"
    "\n"
    "Entries added to or removed from the list, generated automatically "
    "from README and EMERGING changes on each merge to main. Newest first.\n"
)


def git(*args):
    return subprocess.run(
        ["git", *args], check=True, capture_output=True, text=True
    ).stdout


def diff_entries(base, head):
    """Return ({url: name} added, {url: name} removed, {url: name} moved,
    {url: path} removed_in) between two commits, across README.md and
    EMERGING.md."""
    added, removed = {}, {}
    added_in, removed_in = {}, {}
    for path in LIST_FILES:
        diff = git("diff", base, head, "--", path)
        for line in diff.splitlines():
            if line.startswith("+"):
                m = ENTRY_ROW.match(line[1:])
                if m:
                    added[m.group(2)] = m.group(1)
                    added_in[m.group(2)] = path
            elif line.startswith("-"):
                m = ENTRY_ROW.match(line[1:])
                if m:
                    removed[m.group(2)] = m.group(1)
                    removed_in[m.group(2)] = path
    # Same URL on both sides = formatting-only change, or a move between files.
    moved = {}
    for url in set(added) & set(removed):
        if added_in[url] != removed_in[url]:
            moved[url] = added[url]
        del added[url]
        del removed[url]
    return added, removed, moved, removed_in


def section_map(head):
    """Map entry URL -> nearest preceding section heading at head.

    Entries in EMERGING.md map to "Emerging"."""
    sections = {}
    for path in LIST_FILES:
        try:
            text = git("show", f"{head}:{path}")
        except subprocess.CalledProcessError:
            continue
        current = ""
        for line in text.splitlines():
            h = HEADING.match(line)
            if h:
                current = h.group(2)
                continue
            m = ENTRY_ROW.match(line)
            if m:
                sections[m.group(2)] = "Emerging" if path == "EMERGING.md" else current
    return sections


def build_lines(added, removed, moved, sections, removed_in):
    lines = []
    for url, name in sorted(moved.items(), key=lambda kv: kv[1].lower()):
        if sections.get(url) == "Emerging":
            lines.append(f"- Moved [{name}]({url}) to Emerging")
        else:
            lines.append(f"- Moved [{name}]({url}) from Emerging to {sections.get(url, 'the main list')}")
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
            where = " from Emerging" if removed_in.get(url) == "EMERGING.md" else ""
            lines.append(f"- Removed {name}{where}")
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
    added, removed, moved, removed_in = diff_entries(args.base, args.head)
    if not added and not removed and not moved:
        print("No entry changes; changelog untouched.")
        return
    lines = build_lines(added, removed, moved, section_map(args.head), removed_in)
    update_changelog(date, lines)
    print(f"Recorded {len(lines)} change(s) under {date}.")


if __name__ == "__main__":
    main()
