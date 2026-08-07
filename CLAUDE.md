# CleaningOS — Agent Entry Point

**Read `CONSTITUTION.md` before doing anything.** It is the governing document. This file only tells you where to start and what tools exist.

## Start here

Run `/resume`. It loads everything below plus the open threads from last session.

If you're not using `/resume`, read in this order:

1. `CONSTITUTION.md` — rules, structure, how to think and update
2. `02 Canon/Philosophy.md` — what we believe
3. `Voice/Alex Voice.md` — how Alex sounds. Imitate the anchors, not the adjectives
4. `02 Canon/Language.md` — naming rules. Harvest CRM is always both words
5. `03 Concepts/INDEX.md` — **every concept in one line each.** Read this instead of searching `03 Concepts/` page by page. It is how Rule 2 gets obeyed cheaply

## The four rules, compressed

1. Organize by **concept**, never by artifact.
2. **Nothing exists twice.** Read the index before you create. Always.
3. `01 Sources/` is **immutable**. Read-only, forever.
4. The wiki **is** the product, not documentation of it.

## Never

- Edit anything in `01 Sources/` or `02 Canon/` — propose to `00 Inbox/canon-proposals.md`
- Create a second page for an idea that already has one
- Invent a quotation, statistic, student name, or result
- Give a page in `03–07` the same filename as anything in `01 Sources/` (§VI)
- Shorten "Harvest CRM" to "Harvest" — bare Harvest means the Season
- Write customer-facing copy from transcripts instead of concept pages
- Silently pick a winner between contradicting sources — classify per §X first
- Teach a contested claim as settled
- Cite a session log as a source

## Commands

|Command|Does|
|---|---|
|`/resume`|Load last session: recent logs, open threads, what's waiting on Alex|
|`/ingest <path\|url>`|One source → `01 Sources/` → canonical concepts|
|`/ingest-all`|Work `00 Inbox/to-ingest/` to empty, unattended. One source at a time, index regenerated between each. Parks judgment calls in `00 Inbox/review-queue.md`|
|`/process-inbox`|Classify and file `00 Inbox/`|
|`/lint-vault`|Duplicates, orphans, broken links, gaps, Canon drift|
|`/reconcile`|Resolve contested claims, audit published content for retired claims|
|`/draft <format> <concept>`|Render knowledge into a presentation asset|
|`/voice`|Turn a correction into a voice rule. Run after every edit Alex makes|
|`/save [description]`|Close the session: log what changed, regenerate the index, commit|

## Scripts

Run from the vault root. All are idempotent — safe to re-run.

|Script|Does|
|---|---|
|`python3 .claude/scripts/build_index.py .`|Rebuild `03 Concepts/INDEX.md`. **After any change to `03 Concepts/` or `04 Systems/`**|
|`python3 .claude/scripts/build_manifest.py .`|Rebuild `00 Inbox/ingest-run.md` from what's staged. Never resets a handled file|
|`python3 .claude/scripts/fix_wrapped_links.py .`|Find wikilinks broken across a line break. Add `--write` to repair|

## The three queues

Check these before starting work and after finishing:

- `00 Inbox/ingest-run.md` — what's staged, what's done, what's still pending
- `00 Inbox/review-queue.md` — decisions an unattended run declined to make. Merge proposals, contested claims, unsourced claims, blast-radius audits
- `00 Inbox/canon-proposals.md` — changes to `02 Canon/` waiting on Alex

## Where things go

Ideas → `03 Concepts/`. Sequences and SOPs → `04 Systems/`. Things sold → `05 Products/`. Things that promote → `06 Marketing/`. Internal → `07 Company/`. Session records → `08 Logs/` (written by `/save`, never linked to, never knowledge).

Unnumbered and outside the pipeline on purpose: `Glossary.md` and `Voice/Alex Voice.md`. Agents may write to both, under the policy stated at the top of each file.

If it defines an idea, it belongs in `03 Concepts/` and everything else links to it. See Constitution §V.

## Two things that will bite you

- **A wikilink wrapped across a line break does not resolve** — and the page still _reads_ as linked, so the failure is invisible. Don't wrap them. Repair with `fix_wrapped_links.py`.
- **`aliases:` in frontmatter are real links.** `Voice/Alex Voice.md` declares `aliases: [Voice]`, so `[[Voice]]` is valid. Any broken-link check must parse aliases.

## Parallel variants — do not use yet

`/ingest-fast` and `/lint-fast` do the same work with subagents running concurrently. They only pay off above roughly **200 concept pages**. Below that a subagent spends longer reading the Canon than it saves searching, so the sequential versions are faster _and_ cheaper. See `.claude/SCALING.md`.

**Note:** whatever the vault size, `/ingest-all` must stay serialized. Isolated agents share only `INDEX.md`, so running two at once produces duplicate concepts. That constraint is correctness, not cost — Constitution §VIII.