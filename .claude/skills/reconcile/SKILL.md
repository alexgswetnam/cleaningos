---
name: reconcile
description: Work through contested and superseded claims and audit published content for retired claims. Use when conflict state needs resolving or a superseded claim needs a blast-radius audit.
---

# Reconcile

Resolve conflict state. Constitution §X holds the five contradiction types.

## 1. Inventory

- Pages with `contested: true`
- Pages containing a `> [!warning] Contested` callout
- Pages with `superseded:` in the last 90 days
- Pages containing `> [!failure]` Superseded blocks
- **Rows in `07 Company/Claim Register.md` marked DO NOT USE** — each is a live block on
  production

**Sort contested oldest first.** A dispute open six months is either unimportant or quietly
blocking content — either way it needs a decision.

## 2. Present each for a ruling

```
CONCEPT: <name>
Open since: YYYY-MM-DD (N days)

  A: <claim> — <source, date, who>
  B: <claim> — <source, date, who>

What would settle it: <the specific test>
Blocking: <pages that can't produce copy while this is open>
```

Then offer: **A wins** · **B wins** · **both true, different Seasons** (Type 2 — restructure
and the conflict dissolves) · **still contested** (update what would settle it) · **drop it**.

**Do not resolve anything without an answer.** This is the one workflow where guessing is
worse than waiting.

## 3. Blast-radius audit

Required on every Type 1 supersession, and for any `superseded:` in the last 90 days with no
audit recorded.

Trace forward: pages in `05`/`06` whose `renders:` includes this concept · pages linking to
it from `04`–`06` · the concept's own Presented In list.

| Asset | Channel | Live? | Teaches | Severity |
|---|---|---|---|---|

**Severity is exposure, not effort.** High = `live: true` and someone is acting on it now.
Medium = public but passive. Low = internal or archived. A live welcome email outranks a
two-year-old video.

## 4. Offer remediation

For each High item: draft a corrected version · add a pinned correction note · mark
`live: false`.

**Never edit a published asset automatically.** Regenerating copy that's already been sent
to people is Alex's call.

## 5. Report

Claims resolved and how · claims still contested, with age · High-severity assets teaching
superseded material · any Type 5 Canon conflict.

**A Canon conflict halts everything else. Surface it immediately** — do not work the rest of
the queue first.
