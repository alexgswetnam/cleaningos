---
type: company
title: Derived — What This Folder Is
status: Canonical
updated: 2026-08-07
---

# 09 Derived

**AI-generated interpretation of sources. Not evidence.**

`01 Sources/` is the evidentiary record — what was actually said, written, or signed.
This folder holds things a machine produced *about* those sources: summaries, extractions,
restructurings. They help you find your way around 80,000 words of transcript. They do not
prove anything.

## The rule

> **Never cite a derived summary as proof when the raw source exists.**

For a factual claim — a number, a quotation, a student result, a price, a date — verify
against the raw transcript. A summary paraphrases, compresses, and sometimes imposes
structure the speaker didn't use. Any of those can quietly change a fact.

This is enforced in the `draft` workflow and checked by lint.

## What's in here

| Path | What | Count |
|---|---|---|
| `Source Summaries/` | AI summaries extracted from `01 Sources/`, each tagged `type: derived-summary` with a pointer to its raw partner | 12 |
| `Derived Source Manifest.md` | The 171 AI summaries still sitting inside `01 Sources/Course Videos/`, listed against their raw `.txt` partners | 171 listed |

## What stays in `01 Sources/`

Source-record wrappers — the files that describe origin, date, participants, original
artifacts and provenance — are **not** derived. They are provenance, and they belong with
the evidence. `2026-04-01 Weekly Coaching Call.md` stays; its `-SUMMARY.md` moved here.

Raw transcripts never move and are never rewritten. Constitution Rule 3.

## Why the 171 haven't moved yet

They are the only navigable index of the course library, and the Legacy Content Crosswalk
is built from them. Moving 171 files mid-refactor would also make every subsequent diff
unreadable. They are catalogued in the manifest so lint and the claim register can tell
them apart from raw material; the physical move is scheduled for after the crosswalk
exists.

**Until then, treat any `.md` inside a `01 Sources/Course Videos/` course folder as
derived.** The `.txt` beside it is the evidence.
