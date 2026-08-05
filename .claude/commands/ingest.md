---
description: Ingest raw material into Sources and compile it into canonical concepts
argument-hint: "<file path or URL> [source category]"
allowed-tools: WebFetch, Read, Write, Edit, Glob, Grep, Bash
---

Ingest `$ARGUMENTS` into CleaningOS.

Read `CONSTITUTION.md` first. Apply it — do not restate it.

## Step 1 — Archive to Sources

Place the raw material in the right `01 Sources/` subfolder. Transcripts, notes, and
clipped text go in verbatim.

**This file is now permanently immutable.** Never edit it again.

If a fetch returns a paywall, a JavaScript shell, or a fragment, stop and tell me. A
partial ingestion corrupts the vault silently.

## Step 2 — Extract concepts, not summaries

Read the source and list the **distinct ideas** in it. Not sections, not chapter
headings — ideas. A 40-minute coaching call might contain six.

For each idea, name it as it would be named as a page: `Hiring First Cleaner`, not
`Notes on hiring from call 17`.

Show me this list before writing anything.

## Step 3 — The duplication check (the critical step)

For **each** extracted idea, search the vault before deciding anything:

- Exact title match in `03 Concepts/`
- Full-text search for the idea's key terms across all of `02–07`
- Check [[Glossary]] for a term that already covers it
- Check for near-synonyms — the most common failure is creating `Cleaner Retention`
  when `Keeping Your First Cleaner` already exists

Then classify each idea:

| Finding | Action |
|---|---|
| Page exists | **UPDATE it.** Add evidence, nuance, or a contradiction. Never create a sibling. |
| No page, genuinely new idea | **CREATE** in `03 Concepts/` from `_TEMPLATE.md` |
| No page, but it's a *presentation* of an existing idea | Record in `05`/`06` and **link** to the concept |
| Unsure whether it's one idea or two | **Two.** Split now. Report it so `/lint-vault` can propose a merge later. |

Report your classification of every idea and wait for my confirmation if any call is
close. Duplicates are the one error this system cannot absorb.

## Step 4 — Write

For updates: add the new material to the right section, append the source to
`sources:`, bump `updated:`. Do not rewrite what's already there unless it's now wrong.

For new pages: use the full template. Keep every heading — write `*None yet.*` under
empty ones rather than deleting them.

Create **stubs** eagerly for ideas mentioned but not developed. Stubs are the content
roadmap.

## Step 5 — Conflict check

For every claim this source makes that the vault already addresses, classify per
`CONSTITUTION.md` §X before writing:

1. **Contradicts `02 Canon/`?** → **STOP.** Do not write anything further. Log to
   `00 Inbox/canon-proposals.md` and report. Do not ingest the rest of the source.
2. **Different season or engine?** → Not a conflict. Scope the claim by season.
3. **Source is simply wrong?** → Note its unreliability on the page. Source untouched.
4. **Alex, newer, changed his mind?** → Supersede. Newest wins. Write the
   `> [!failure]- Superseded` block with what/which source/replaced by/why. Set
   `superseded:` in frontmatter. **Then run the blast-radius audit** and report every
   live asset now teaching the old claim.
5. **Genuinely unresolved?** → `> [!warning] Contested`, both claims kept, set
   `contested: true`, and state what would settle it.

If you can't classify confidently, default to Contested and say so.

State the date of every source you supersede *with*. Undated material can never
supersede — it defaults to Contested.

## Step 6 — Propagate

- Add concepts to their [[Four Engines|engine]] hub index
- Add new terms to [[Glossary]]
- Ensure every touched page still has five or more Related Concepts

## Step 7 — Report

Every file created or updated, grouped, one line each on why. Then:

- Every conflict found, its type, and how you handled it
- Any claim superseded, plus the blast-radius table of live assets now wrong
- Stubs created, and which is most worth filling
- Anything you were unsure about

Never edit `02 Canon/`. If this source changes the Canon, write it to
`00 Inbox/canon-proposals.md` and tell me.
