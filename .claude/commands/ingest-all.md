---
description: Ingest every staged source, one at a time, until the queue is empty
argument-hint: "[max sources this run]"
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, Task
---

Work `00 Inbox/to-ingest/` to empty. Read `CONSTITUTION.md` first. Apply it — do not
restate it.

This runs unattended. Everything below exists to make that safe.

## Setup, once

```
python3 .claude/scripts/build_manifest.py .
python3 .claude/scripts/build_index.py .
```

Read `00 Inbox/ingest-run.md`. If nothing is `pending`, say so and stop. If
`$ARGUMENTS` gives a number, process at most that many this run.

## The loop

For each `pending` file, oldest line first, **one at a time**:

### 1. Mark it `running` BEFORE you spawn anything

Edit its line in `00 Inbox/ingest-run.md` to:

```
- [~] `<name>` — running  started YYYY-MM-DD — if this line still says `running`, the run
  was interrupted: VERIFY what landed before re-ingesting
```

**Write this first, every time.** State is written after a subagent returns, so an
interrupt in the gap leaves the work done and the manifest saying `pending`. That
happened on the first real run: a course was fully ingested — source file, 42 archived
lessons, 3 new concepts — and its line still read `pending`. Re-running would have
ingested it a second time and duplicated all of it. A `running` marker turns a silent
double-ingest into a visible "check this."

### 2. Spawn a subagent for it

Use the Task tool. One source per subagent, with a fresh context. Do not batch two
sources into one subagent, and **never run two subagents concurrently** — see Serialization
below.

Brief it with: the file path, `CONSTITUTION.md`, `02 Canon/`, `Voice/Alex Voice.md`,
`03 Concepts/INDEX.md`, and the autonomy policy below. Tell it to follow
`.claude/commands/ingest.md` steps 1–6 with these modifications:

- Step 2's "show me this list before writing" — **do not wait.** Record the list in the
  report instead.
- Step 3's "wait for my confirmation if any call is close" — **do not wait.** Apply the
  confidence test below and park what fails it.

Require it to return: files created, files updated, ideas extracted, every parked
decision, and every conflict with its Type.

### 3. On return, in this order

1. **Regenerate the index** — `python3 .claude/scripts/build_index.py .`. Do this
   between *every* source, without exception. See Serialization.
2. Append any parked decisions to `00 Inbox/review-queue.md`
3. Change the line from `running` to `done`, `parked`, or `failed`, with a one-line result
4. Print one line to the conversation: filename, created/updated counts, parked count

### 4. Next file

No summary between files. No asking whether to continue. Keep going.

---

## Serialization — the rule that keeps this correct

**Process exactly one source at a time, and regenerate `INDEX.md` after each.**

Subagents can't see each other. The index is the only thing they share. If two run
concurrently, both read the same index, both find no page for an idea, and both create
one — the exact duplicate Rule 2 says this system cannot absorb, produced at machine
speed. If you run sequentially but skip the index regen, source #7 is deciding against
what the vault looked like before source #1 touched it.

This is why `/ingest-all` is not a parallel command and must not be made one. The
constraint is correctness, not cost.

---

## Autonomy policy

### Decide on your own

- Archiving to `01 Sources/` and choosing the subfolder
- Extracting ideas and naming them
- Updating a page when the match is unambiguous
- Creating a page when nothing in the index is close
- Creating stubs
- Type 2 (season-scoped) and Type 4 (bad data) conflicts — both are mechanical

### The confidence test

Before calling two things the same concept, ask: **would this page's `In one line` and
the new idea both be true about the same decision an Owner makes?**

- Same decision → same concept. Update.
- Different decisions → two concepts. Create.
- Can't tell → **create separately and park a merge proposal.** Per Constitution §III,
  an unnecessary split is visible and cheap; a wrong merge destroys a distinction you
  can't recover.

### Park it and keep going

Write to `00 Inbox/review-queue.md`, then continue the run:

- Any merge proposal from the test above
- **Type 1 supersessions.** Write the `> [!failure]-` block and set `superseded:` as
  normal, but the blast-radius audit gets parked — retiring a claim that's live in a
  product is Alex's call, not yours.
- **Type 3 contested.** Write the callout with what would settle it. Park the dispute.
- Anything you'd have asked about if a human were here.

### Halt

- **Type 5, Canon conflict** — halts *that source only*. Log to
  `00 Inbox/canon-proposals.md`, mark the line `skipped` with the reason, and move to the
  next file. Per §X you do not ingest the rest of that source; the rest of the queue is
  unaffected.
- **Three consecutive failures** — stop the whole run and report. Something structural is
  wrong and continuing will make a mess that's expensive to unpick.
- **A source that won't parse** — mark `failed`, continue. Don't ingest a fragment;
  §Step 1 of `/ingest` is right that partial ingestion corrupts silently.

Never invent content to fill a gap. A thin source producing two pages is a correct
outcome — the queue's own note on the April 15 call says as much.

---

## When the queue is empty

1. `/lint-vault` — **not optional.** A long unattended run produces near-duplicates no
   confidence test catches. This is where they surface.
2. `/save "unattended ingest run"` — log it
3. Report:
   - Sources ingested, skipped, failed
   - Concepts created vs. updated, totals
   - **Everything parked, grouped by type** — this is the real output. Lead with it.
   - What `/lint-vault` flagged
   - Which stub is now most worth filling

Then stop. Do not start resolving the parked decisions.
