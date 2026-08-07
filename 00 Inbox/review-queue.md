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

## Parked for a proper ruling (2026-08-07)

### [[Marketing Budget]] — the ~10%-of-revenue figure

**Current page:** marketing budget ≈ 10% of revenue. Already flagged unproven in
`07 Company/Claim Register.md`.

**Alex, 2026-08-07, in passing:** *"the higher percent the more aggressive. its normal to go
very high in the beginning, this number is arbitrary and changes massively. don't even make
it a teaching point honestly, i'm not considering this really."*

**Not treated as a supersession.** He said himself he hasn't thought it through, and §X bars
superseding on an unconsidered remark. But the page currently teaches a fixed ratio and its
author has just called that ratio arbitrary.

**What would settle it:** Alex decides whether the page teaches (a) a ratio, (b) "spend is a
function of aggression and stage, not a fixed ratio," or (c) nothing — and the page is cut.

**Already actioned:** removed as a graduation criterion for Leads Scale.

### ✅ Resolved same day — the leadership layer is the VA

Raised and closed 2026-08-07. Recorded because the reasoning matters.

**Raised:** [[Business GPS]] records Faithful Cleaners at Leadership **Harvest**, owners at
~1 hr/week, while the grid's Harvest action reads *"install leaders (ops, training,
sales/admin)"* — and Alex runs no team leads.

**Resolved by Alex:** *"the team lead for cleaning isn't a thing. if you are saying team lead
in ops training sales admin etc, that is my VA."*

Two things were hiding under one phrase. A management layer over **cleaners** does not exist
here. A leadership layer over **ops, training, sales and admin** does — it's the VA, and the
vault already documents it across 5 concepts and 8 lessons.

**Open follow-up:** [[Picking The Right VA]], [[When To Hire A VA]] and [[When To Fire A VA]]
are tagged both Logistics and Leadership. If the VA is the leadership layer, VA hiring may be
a Leadership decision that happens to serve Logistics. Affects which cell teaches it.

**Open follow-up:** no page states that the VA *is* the leadership layer. The VA pages cover
hiring, picking, managing and firing one; none says what role it plays in the model. Possibly
the one genuinely missing concept in Leadership. **Not built — flagged.**

---

## Conflict-state defects found by lint (2026-08-07)

Three real findings from `lint_structure.py`. **Not fixed** — each needs a judgment that
isn't mine to make. Fixing them by inventing a resolution test or a supersession reason
would be worse than leaving them visible.

| Page | Defect | What's needed |
|---|---|---|
| [[Price Objection]] | Contested callout with no **"what would settle it"** | A specific test. Constitution §X: a contested callout without a resolution path is an argument stored forever |
| [[Cleaner Pay Structure]] | Superseded block with no **Reason** | Why the old claim was replaced. Six months on, a supersession without a reason is indistinguishable from a mistake |
| [[Subcontractor Vs W-2]] | Superseded block with no **Reason** | Same |

---

## Concept vs System — flagged, not moved (2026-08-07)

From the v2 refactor, Commit 4. Eighteen pages moved to `04 Systems/`. These four sat close
enough to the line that moving them silently would have been a guess. **They stayed in
`03 Concepts/`.** Each needs one decision from Alex: is the page's main value understanding
a principle, or following steps?

| Page | The case for moving | The case for keeping | Claude's lean |
|---|---|---|---|
| [[Cleaner Job Notes]] | It's a documentation standard — three fixed headers, applied to every client | The value is knowing *that* notes need structure, not the typing | Keep |
| [[Transitioning Clients To New Cleaners]] | It is a sequence: willing clients first, resistant ones later, holdouts last | The sequence encodes a judgment about client psychology, not a procedure | Keep, but it's the closest call of the four |
| [[Reactivating Past Clients]] | A campaign you run — segment, message, measure | Its core claim is *leads don't disappear*, which is a belief | Split later: the belief stays, the campaign becomes a System |
| [[Sales Pipeline Stages]] | Setting up pipeline stages is a build task | The page explains what the stages *mean* and why no lead gets lost | Keep |

Also noted, not acted on: `04 Systems/Cleaner Handbook.md` shares a basename with
`01 Sources/Course Videos/Labor 101/Cleaner Handbook.txt`. Constitution §VI bars a page in
`03–07` from sharing a filename with anything in `01 Sources/`. The rule's *purpose* —
ambiguous wikilinks — isn't violated, because Obsidian resolves `[[Cleaner Handbook]]` to
the `.md` and ignores the `.txt`. Pre-existing, not introduced by the move. Either narrow
§VI to `.md` collisions or rename the page.

---

## Merge proposals

Two pages that may be one concept.

> [!info] The rule that filled this section is retired — 2026-08-07
> These entries were created under the old Rule 2: *"when genuinely unsure, they are
> two"* — split first, merge later. That rule is gone. Agents now **default to update**,
> and log doubt in `00 Inbox/knowledge-gaps.md` instead of creating a second page.
>
> Existing entries here still need working. New ones should be rare.

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
