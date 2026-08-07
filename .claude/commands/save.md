---
description: Close the session — write a log of what changed and what's still open
argument-hint: "[short description]"
allowed-tools: Read, Glob, Grep, Bash, Write, Edit
---

Write a session log to `08 Logs/YYYY-MM-DD-$ARGUMENTS.md`. If no description was given,
name it from what actually happened this session.

This is the only file you write without asking. It is a record, not knowledge — it never
defines an idea, and nothing else in the vault links to it. Concepts still live in
`03 Concepts/`; this just says what was done to them and when.

## What goes in it

Use this structure. Leave a section present-and-empty rather than deleting it.

```markdown
---
type: log
date: YYYY-MM-DD
status: Complete | Interrupted
---

# YYYY-MM-DD — <what this session was>

## What I Did
One line per real change. Not a narration of the conversation.

## Files Touched
Grouped created / updated, one line each on why — per Constitution §IX.
Use [[wikilinks]] so the log is navigable.

## Decisions Alex Made
Only decisions that came from Alex, quoted or closely paraphrased. This is the
section that stops the same question being re-litigated in three weeks.
If none, say "None."

## Open Threads
What the next session should pick up, in priority order. Be specific enough
that /resume can act on it without re-reading this whole log.

## Escalations Left Standing
Type 5 Canon conflicts, unresolved contested claims, blast-radius audits reported
but not fixed. Anything waiting on Alex. If none, say "None."
```

## Rules

- **Never invent progress.** If a thread was left half-finished, say half-finished.
  A log that overstates what happened is worse than no log — the next session builds
  on a lie.
- **Do not resolve anything while saving.** If you notice an open contradiction as you
  write, record it under Escalations; don't fix it here.
- Record Canon proposals you wrote to `00 Inbox/canon-proposals.md` under Escalations
  too. They are blocking by definition.
- If `03 Concepts/` or `04 Systems/` changed this session, regenerate the index:
  `python3 .claude/scripts/build_index.py .`
- Then, if the repo is a git repo, stage and commit with a message summarizing the
  session. Do not push unless Alex asks.

Report the log path and a two-line summary. Nothing else.
