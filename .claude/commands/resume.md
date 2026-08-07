---
description: Load where we left off — recent logs, open threads, blocked escalations
argument-hint: "[number of logs, default 3]"
allowed-tools: Read, Glob, Grep, Bash
---

Rebuild session context. **Read only. Change nothing.**

## 1. Read, in this order

1. `CONSTITUTION.md` and `02 Canon/Philosophy.md` — always, per §VIII
2. The most recent `$ARGUMENTS` logs in `08 Logs/` (default 3), newest first
3. `03 Concepts/INDEX.md` — the whole concept space in one file. Read this instead of
   searching `03 Concepts/` page by page.
4. `00 Inbox/canon-proposals.md` — anything here is blocking Alex
5. `00 Inbox/ingestion-queue.md` — what's waiting to be processed

Do **not** read individual concept pages at this stage. The index tells you what exists;
open a page only once you know which one you need.

## 2. Report

Short. Alex is reorienting, not reading a report.

- **Where we left off** — 2–3 sentences from the most recent log
- **Open threads** — carried forward from the logs, deduplicated, priority order.
  Drop any thread a later log shows was finished.
- **Waiting on you** — Canon proposals, contested claims, blast-radius audits reported
  but unfixed. Each with how long it's been sitting.
- **Queue depth** — how many sources are waiting in `00 Inbox/`

## 3. Then stop

End with the single most useful next action and ask whether to take it. Do not start
working. The point of `/resume` is to hand Alex the steering wheel with the map already
open.

## If `08 Logs/` is empty or missing

Say so plainly, read the index and inbox anyway, and report from those. Don't fabricate
a history.
