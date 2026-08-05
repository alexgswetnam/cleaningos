---
description: Work through contested and superseded claims, and audit published content
argument-hint: "[concept name, or blank for all]"
allowed-tools: Read, Glob, Grep, Bash, Edit, Write
---

Resolve conflict state across the vault. Scope: `$ARGUMENTS` if given, else everything.

Read `CONSTITUTION.md` §X first — the five contradiction types and their handling.

## 1. Inventory

Find and list:

- Pages with `contested: true` in frontmatter
- Pages containing a `> [!warning] Contested` callout
- Pages with a `superseded:` date in the last 90 days
- Pages containing `> [!failure]` Superseded blocks

Sort contested items **oldest first**. A dispute open six months is either not
important or is quietly blocking content production — either way it needs a decision.

## 2. For each contested claim

Present it for a ruling:

```
CONCEPT: Hiring First Cleaner
Open since: 2026-05-02 (95 days)

  A: hire at three weeks of turned-away work
     Source: Coaching Call 88 (2026-07-02) — Alex, direct
  B: hire only after documenting the job
     Source: Book: Traction (2021) — outside

What would settle it: track the next 10 students who hired each way.

Blocking: 3 pages can't produce copy while this is open
          [[Hiring Flow]], [[Labor Engine]], Welcome Email 3
```

Then ask which of these I want:

1. **A wins** — B becomes a Superseded block, blast-radius audit runs
2. **B wins** — same, reversed
3. **Both true, different seasons** — you restructure the page as Type 2 and the
   conflict dissolves
4. **Still contested** — leave it, but update *what would settle it* if the test has
   changed
5. **Drop it** — the claim doesn't matter enough to track

Do not resolve anything without my answer. This is the one command where guessing is
worse than waiting.

## 3. Blast-radius audit

Run for every claim resolved this session, and for any `superseded:` in the last 90
days that has no audit recorded yet.

Trace forward from the concept:

- Pages in `05`/`06` whose `renders:` frontmatter includes this concept
- Pages linking to the concept from `04`–`06`
- The concept's own record of where it's been presented

Report:

| Asset | Channel | Live? | Teaches | Severity |
|---|---|---|---|---|

**Severity is about exposure, not effort.** Rank by whether someone is acting on wrong
information *right now*:

- **High** — `live: true` and someone acts on it. Running email sequences, current
  course lessons, active sales scripts.
- **Medium** — public but passive. Old YouTube videos, blog posts.
- **Low** — internal, archived, or `live: false`.

A live welcome email outranks a two-year-old video with 200 views, even though the
video feels more visible.

## 4. Offer remediation

For each High item, offer:

- `/draft` a corrected version
- Add a pinned correction note to the asset page
- Mark `live: false` if it should be pulled

Never edit a published asset's page automatically. Regenerating copy that's already
been sent to people is my call, not yours.

## 5. Report

- Claims resolved this session, and how
- Claims still contested, with age
- High-severity assets now teaching superseded material
- Any Type 5 Canon conflicts found — these halt everything else

If you find a Canon conflict at any point, stop and surface it immediately. Do not work
through the rest of the queue first.
