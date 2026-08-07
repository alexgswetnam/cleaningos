---
type: company
title: Review Queue
status: Developing
updated: 2026-08-06
---

# Review Queue

Decisions an unattended `/ingest-all` run declined to make. Each one is a place the agent
could have been wrong in a way the vault can't absorb, so it wrote down what it saw and
kept going.

**Work this after every run.** A parked decision is a live inconsistency: two pages that
may be one, or a claim the vault now teaches two ways. `/reconcile` handles the contested
ones; merges are a `/lint-vault` follow-up.

Delete an entry once it's resolved. Note the resolution in that session's log.

---

## Merge proposals

Two pages that may be one concept. The agent split them per Constitution §III — "when
genuinely unsure, they are two" — and flagged it rather than guessing.

*None yet.*

<!-- Format:
### `[[Page A]]` + `[[Page B]]`
- **Why flagged:** what made the confidence test ambiguous
- **From:** source file, date ingested
- **If merged, survivor should be:** proposed name
-->

---

## Superseded claims awaiting blast-radius audit

The old claim has been demoted on the concept page. What's still *teaching* it hasn't
been traced — that's §X's audit, and it's Alex's call because it means editing live
assets.

*None yet.*

<!-- Format:
### `[[Concept]]` — superseded YYYY-MM-DD
- **Was:** old claim
- **Now:** new claim
- **Replaced by:** source, date
- **Not yet checked:** which products/marketing still teach the old version
-->

---

## Unsourced claims

Assertions the vault makes that no file in `01 Sources/` supports. Distinct from a
contested claim: there aren't two sides here, there's one side and no evidence.
Constitution §IX — *"Never invent a quotation, statistic, student name, or result"* — and
§VII, which says an empty `sources:` means "the page asserts things nothing backs up."

### ✅ RESOLVED — [[When To Hire A VA]], the $45K/month figure

Alex confirmed 2026-08-06: **the number is real.** It's a friend of his, described from
personal knowledge — *"he hated his life lol"* — not a workshop claim. The audit was right
that nothing in `01 Sources/` supported it, and wrong to imply the figure was invented:
the *citation* was fabricated, not the fact.

Re-attributed to `Alex direct 2026-08-06` and the page rewritten so the 12-hour days carry
the point rather than sitting as a footnote. Lesson recorded on the page: a real fact with
a wrong citation is indistinguishable from a fabrication until someone asks the author.

---

## Contested claims

Written to the page as `> [!warning] Contested` with both sides intact. Neither is being
taught until Alex rules.

### ✅ RESOLVED — [[GBP Verification]]

Alex ruled 2026-08-06: **"skip to live call asap if possible."** Claim B wins — go straight
for the live video call, don't bother with the pre-recorded submission.

Neither source could be dated, so §X supersession couldn't settle it; the author did.
Written to the page as a `[!failure]-` block with the retired claim intact, `superseded:`
set, `contested:` removed, and the one-liner and Checklist rewritten to lead with the live
call. Blast-radius audit run: nothing live teaches the retired sequence.

### [[Close Rate By Channel]]
- **Claim A:** Meta/Facebook close rate is **3–5%**, converting over months rather than
  days — [[2025-02-03 Weekly Coaching Call]]
- **Claim B:** Meta close rate is **~10%** — [[Leads 101 Part 2]], "What's a healthy close
  rate?" lesson
- **What would settle it:** a dated, tracked Meta close-rate figure from
  [[KPI Tracking Sheet]] data. Both current figures are anecdotal ranges, not measured
  KPIs, and the course lesson carries no date, so it can't supersede the dated coaching
  call.
- **Contested since:** 2026-08-06

### [[Cleaner Pay Structure]] + [[Subcontractor Vs W-2]] — read this one first

Two of the company's own documents disagree about whether cleaners have a guaranteed
hourly floor. This is not a knowledge-tidiness problem: a guaranteed minimum is an
employee-like signal, so the two documents point at different worker classifications.

- **Claim A:** the cleaner-facing Cleaner Handbook promises a **$28.00/hr** "Minimum
  Earnings Adjustment," described as an actual floor — "we add a one-time MEA top-up so
  your Effective Hourly equals $28.00" — [[Premium Resources]]
- **Claim B:** the signed Subcontractor Agreement, Exhibit A, uses a **$25.00/hr**
  "Reference Effective Rate" for a supplement that is discretionary and non-automatic,
  and states explicitly that it is **"not a weekly floor"** — [[Premium Resources]]
- **What would settle it:** ask Alex which document is currently in force and which one
  cleaners actually receive. If both are live, they contradict each other in front of the
  people they govern. Neither is dated relative to the other, so this cannot be resolved
  by supersession.
- **Contested since:** 2026-08-06
- **Why it's here and not decided:** an agent picking a winner would be choosing the
  company's worker-classification posture. Not its call.
- **Update 2026-08-06, from Labor 101 ingestion — deepened, not settled.** A third
  artifact surfaced: the Labor 101 hiring interview script tells every candidate *"we do
  have a unique payment structure to help you get at least $25/hr... we'll pay the
  difference to make sure you got at least that much"* — floor language, matching
  Claim B's $25 figure but using Claim A's guarantee framing. A same-course coaching
  lesson ("Determining Cleaners' Pay") has the owner saying the opposite about the same
  $25 figure in the same breath: *"I want you making at least $25 an hour... but I'm not
  guaranteeing anything."* This means the "is there a floor" question isn't cleanly two
  documents disagreeing once — it's inconsistent across at least four company artifacts
  (Handbook, Subcontractor Agreement, interview script, coaching call), none dated
  relative to the others. Full statement in both pages' Conflict History. Does not change
  what would settle it, except to add: also ask whether the interview script's promise is
  actually said verbatim to candidates today, which would make $25 a de facto floor
  regardless of what Exhibit A says on paper.

<!-- Format:
### `[[Concept]]`
- **Claim A:** ... — source
- **Claim B:** ... — source
- **What would settle it:** ...
- **Contested since:** YYYY-MM-DD
-->

---

## Related Concepts

- [[CONSTITUTION]]
- [[ingest-run|Ingest Run]]
- [[ingestion-queue|Ingestion Queue]]
- [[canon-proposals]]
- `00 Inbox/to-ingest/` — where sources are staged
