# CleaningOS — Agent Entry Point

**Read `CONSTITUTION.md` before doing anything.** It is the governing document. This
file only tells you where to start.

## Order of operations, every session

1. `CONSTITUTION.md` — rules, structure, how to think and update
2. `02 Canon/Philosophy.md` — what we believe
3. `Voice/Alex Voice.md` — how Alex sounds. Imitate the anchors, not the adjectives.
   Outside Canon on purpose, and agents may write to it. Policy is at the top of the file.
4. `02 Canon/Language.md` — naming rules. Harvest CRM is always both words.
5. `03 Concepts/INDEX.md` — every concept in one line each. **Read this instead of
   searching `03 Concepts/` page by page.** It is how Rule 2 gets obeyed cheaply.

Or just run `/resume`, which does all five plus the open threads from last session.

## The four rules, compressed

1. Organize by **concept**, never by artifact.
2. **Nothing exists twice.** Search before you create. Always.
3. `01 Sources/` is **immutable**. Read-only, forever.
4. The wiki **is** the product, not documentation of it.

## Never

- Edit anything in `01 Sources/`
- Edit anything in `02 Canon/` — propose to `00 Inbox/canon-proposals.md`
- Create a second page for an idea that already has one
- Invent a quotation, statistic, student name, or result
- Shorten "Harvest CRM" to "Harvest" — bare Harvest means the Season
- Write customer-facing copy from transcripts instead of concept pages
- Silently pick a winner between contradicting sources — classify per §X first
- Teach a contested claim as settled

## Commands

- `/ingest <path|url>` — raw material → Sources → canonical concepts
- `/process-inbox` — classify and file `00 Inbox/`
- `/lint-vault` — duplicates, orphans, gaps, Canon drift
- `/reconcile` — resolve contested claims, audit published content for retired claims
- `/voice` — turn a correction into a voice rule (run after every edit you make)
- `/draft <format> <concept>` — render knowledge into a presentation asset
- `/resume` — load last session: recent logs, open threads, what's waiting on Alex
- `/save [description]` — close the session: log what changed, regenerate the index, commit

### Parallel variants — do not use yet

`/ingest-fast` and `/lint-fast` do the same work with subagents running concurrently.
They only pay off above roughly **200 concept pages**. Below that, a subagent spends
longer reading the Canon than it saves searching, so the sequential versions are faster
*and* cheaper. See `.claude/SCALING.md`.

## Where things go

Ideas → `03 Concepts/`. Sequences and SOPs → `04 Systems/`. Things sold →
`05 Products/`. Things that promote → `06 Marketing/`. Internal → `07 Company/`.
Session records → `08 Logs/` (written by `/save`, never linked to, never knowledge).

If it defines an idea, it belongs in `03 Concepts/` and everything else links to it.
See Constitution §V.
