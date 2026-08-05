---
description: Classify and file everything in 00 Inbox
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

Process every file in `00 Inbox/` (skip `canon-proposals.md`).

Read `CONSTITUTION.md` first.

## Classify each item

| Kind | Action |
|---|---|
| **Voice note / raw thought** | Extract the ideas. Run the Step 3 duplication check from `/ingest`. Update or create concepts. Mark Alex's own claims as his — see below. |
| **Raw material** (transcript, call, clipped article) | Move to `01 Sources/`, then ingest fully. |
| **Question** | Add to the FAQ section of the relevant concept, unanswered. Do not answer from your own knowledge — this vault holds what Alex teaches, not what you know. |
| **Canon change** | Write to `canon-proposals.md`. Never edit `02 Canon/`. |
| **Task / reminder** | Leave in place, flag in report. This is not a to-do list. |
| **Junk** | Move to `99 Scratchpad/`. |
| **Ambiguous** | Leave it. Ask me. |

## Mark provenance

Alex's own unsourced thinking is a different epistemic category from something taught
in a recorded call. Tag it:

```markdown
> [!note] Alex — YYYY-MM-DD, from inbox
> The claim, in his words.
```

This matters because in six months an agent writing a VSL needs to know which claims
have been tested with students and which were a shower thought.

## Clean up

Delete from `00 Inbox/` only after the content is verifiably written elsewhere. When in
doubt, leave it.

## Report

Per item: what it was, where it went, what it connected to. Then what you left behind
and why.
