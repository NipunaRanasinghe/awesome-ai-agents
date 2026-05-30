# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A curated "awesome list" of AI agent frameworks, tools, and resources. The repository has **no application code** — the substantive content lives entirely in `README.md` as a set of markdown tables. Contributions are PRs that add, update, or remove rows in those tables.

## Commands

- `npx awesome-lint` — the one local check that matters. Validates `README.md` against the [awesome-lint](https://github.com/sindresorhus/awesome-lint) ruleset (heading structure, link formatting, list order, etc.). This is what the `Lint` GitHub Action runs on every push/PR.
- Link rot is checked in CI by lychee on a daily schedule (`.github/workflows/links.yml`); it opens an issue automatically when links break. You usually don't need to run it locally.

## Adding or editing entries

Each row in a README table follows this exact shape:

```markdown
| [Project Name](https://github.com/owner/repo) | ![](https://img.shields.io/github/stars/owner/repo) | Short, one-line description |
```

Conventions to preserve when editing:

- The stars badge URL path (`owner/repo`) must match the link URL. A mismatch is a common bug in incoming PRs.
- One sentence, no trailing period in the description column — match neighboring rows.
- The **Programming Language Agents** table has a 4th `Language` column; don't drop it when copy-pasting from other sections.
- Sections are not strictly alphabetized — leave the existing order alone unless explicitly asked to sort. New entries typically go at the end of their section.
- Acceptance criteria (from `CONTRIBUTING.md`): project is actively maintained (updated in last 6 months), not already listed, relevant to AI agents.

## Table of contents

The `## Contents` block near the top of `README.md` is hand-maintained. If you add, remove, or rename a section, update both the heading and its TOC entry — awesome-lint will flag anchor mismatches.

## Repo layout

- `README.md` — the list itself; this is the only file most PRs touch.
- `CONTRIBUTING.md` — contributor-facing rules; keep in sync if you change the entry format.
- `.github/workflows/` — `lint.yml` (awesome-lint), `links.yml` (lychee, daily), `stale.yml` (auto-closes inactive issues/PRs after 30+7 days).
- `resources/images/` — README assets.
