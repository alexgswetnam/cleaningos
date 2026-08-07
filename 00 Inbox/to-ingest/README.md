---
type: company
title: To Ingest
status: Developing
---

# to-ingest

**Put source files here.** Then run `/ingest-all`.

Transcripts, course exports, call recordings' text, PDFs, zips — anything that should
become knowledge. Zips are treated as one source, not one per file inside, so a course
export stays a single unit the way `Every SOP We Use` did.

Nested folders are fine; the manifest walks them.

## What happens to them

`/ingest-all` archives each file into `01 Sources/` — where it becomes permanently
immutable, per Constitution Rule 3 — and compiles the ideas inside it into
`03 Concepts/`. The original stays here afterward. Nothing is deleted automatically.

Once a file shows `done` in `00 Inbox/ingest-run.md`, its content is fully archived in
`01 Sources/` and the copy here is safe to delete by hand.

## What doesn't go here

Ideas, notes, and drafts you wrote yourself. Those are already knowledge — they belong in
`03 Concepts/` via `/process-inbox`, not in the source archive. This folder is for **raw
material that arrived from somewhere**: something recorded, exported, or downloaded.

## Related Concepts

- [[CONSTITUTION]]
- [[ingest-run|Ingest Run]]
- [[ingestion-queue|Ingestion Queue]]
- [[review-queue|Review Queue]]
