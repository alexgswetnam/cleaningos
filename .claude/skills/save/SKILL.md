---
name: save
description: Close the session - write a log of what changed and what is still open, regenerate the index, and commit. Use at the end of a working session.
---

# Save

Write `08 Logs/YYYY-MM-DD-<description>.md`.

This is the only file written without asking. It is **a record, not knowledge** — it never
defines an idea and nothing links to it. Never cite a log as a source.

## Structure

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
Grouped created / updated, one line each on why. Use [[wikilinks]].

## Decisions Alex Made
Only decisions from Alex, quoted or closely paraphrased. This is the section that stops
the same question being re-litigated in three weeks. If none, say "None."

## Open Threads
What the next session picks up, in priority order. Specific enough to act on without
re-reading the log.

## Escalations Left Standing
Canon conflicts, unresolved contested claims, blast-radius audits reported but not fixed,
DO NOT USE claims still blocked. Anything waiting on Alex. If none, say "None."
```

## Rules

- **Never invent progress.** Half-finished is recorded as half-finished. A log that
  overstates what happened is worse than no log — the next session builds on a lie
- **Do not resolve anything while saving.** Notice an open contradiction? Record it under
  Escalations; don't fix it here
- Canon proposals written this session go under Escalations. They are blocking by definition
- If `03 Concepts/` or `04 Systems/` changed: `python3 .claude/scripts/build_index.py .`
- Then stage and commit with a message summarizing the session. **Do not push unless asked**

Report the log path and a two-line summary. Nothing else.
