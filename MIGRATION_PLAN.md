---
type: company
title: Migration Plan — CleaningOS v2
status: Proposal — Awaiting Alex
branch: refactor/cleaningos-v2
updated: 2026-08-07
---

# Migration Plan — CleaningOS v2

**Nothing in the vault has been edited yet.** The branch `refactor/cleaningos-v2` exists and this file is the only change on it. Every move below is a proposal.

**The goal:** one intellectual model — **Four Engines × Four Seasons**, governed by the **Five Laws**. Every structural decision below is judged against whether it makes that model clearer or muddier.

---

## What is actually in here

| | Count |
|---|---|
| Files tracked (excluding `.git`) | 641 |
| Canon pages | 6 |
| Concept pages (excl. `INDEX`, `_TEMPLATE`) | 117 |
| System pages | 5 |
| Product pages | 3 |
| Marketing pages | **0** |
| Raw transcripts (`.txt`) in Sources | 185 |
| Markdown files in Sources | 224 |
| Course lesson folders | 8 |

Two numbers worth pausing on: **zero marketing pages** — so the blast-radius risk from Canon changes is far lower than the Constitution assumes — and **224 markdown files in Sources**, most of which turn out not to be evidence at all. See Commit 6.

---

## Three decisions I need from you before Commit 1

### 1. The Canon lock

Changes 2 and 3 require editing `02 Canon/`. Two things block that:

- `CONSTITUTION.md` §II: *"Canon is edited by Alex only… There are no exceptions to this rule."*
- `.claude/settings.json` denies `Edit(02 Canon/**)` and `Write(02 Canon/**)` at the tool layer.

You are Alex and you are directing this, so the authority is fine. But I won't quietly step around a wall you built on purpose. **Options:** (a) I edit Canon under your written instruction and record it as a §XII amendment with your name on it, leaving `settings.json` locked so future agents still hit the wall; (b) you relax `settings.json` for this branch; (c) I write the proposed Canon text to `00 Inbox/canon-proposals.md` and you paste it in yourself.

I recommend (a).

### 2. 120 uncommitted files carried over from `main`

The working tree had 120 uncommitted changes when I branched — 74 modified, 44 untracked, 2 deleted (including `02 Canon/Glossary.md`, already moved to root). They came onto this branch with me. If I commit them mixed into refactor commits, the diff stops being reviewable.

I'd like to land them as one commit — `snapshot: pre-refactor working state` — as commit zero, so every commit after it is purely refactor.

### 3. Approval cadence

You wrote "before each major step, show Alex the proposed moves." That's 12 gates. Alternative: gate the five that carry judgment (Commits 1, 2, 4, 8, and the two crosswalks) and let the mechanical ones run.

---

## Commit 0 — snapshot

`snapshot: pre-refactor working state`

All 120 pre-existing working-tree changes, unmodified. No refactor content.

---

## Commit 1 — Diagnostic model correction

`fix(gps): constraint is set by the goal, not by the lowest Season`

**The error being fixed:** `03 Concepts/Business GPS.md` currently teaches, as step 3 of the method, *"The one lagging behind the others is your constraint."* That is the claim you're retiring.

| File | Change |
|---|---|
| `03 Concepts/Business GPS.md` | Replace the 6-step method with the 8-step goal-anchored sequence. Add the core rule in bold: **the lowest-Season Engine is not automatically the current bottleneck.** Add a collapsed `> [!failure]- Superseded — 2026-08-07` block recording the old wording verbatim, its source (`Premium Workshop — 4 Seasons, 4 Bottlenecks`), what replaced it, and why. Set `superseded: 2026-08-07`. Keep all six existing `sources:`. Keep the 16-cell action grid — it survives unchanged, since it says what to *do* in a cell, not how to pick the cell. |
| `02 Canon/Four Seasons.md` | One line changes: *"work on the one currently constraining the whole system"* → goal-anchored phrasing. Also in Commit 2. |
| `02 Canon/Philosophy.md` | Line 168 teaches diagnosing each Engine's Season and finding the constraint; re-word to match. |
| `00 Inbox/canon-proposals.md` | Log the amendment. |

**Preserved, not overwritten:** the three worked student evaluations (Rick, Courtney, Alex) stay. Note that Courtney's diagnosis — Labor over Leads despite both being weak — is *evidence for the new rule*, not against it: the call picked Labor because it blocked her goal, not because it scored lowest.

**Risk:** Business GPS is `status: Canonical` and 10 pages link to it. None of them restate the algorithm; I checked. The blast radius is one page.

---

## Commit 2 — Canon cleanup

`refactor(canon): Seasons describe Engine maturity; Four Roles leaves Canon`

### 2a — Remove global Season revenue bands

| File | Change |
|---|---|
| `02 Canon/Four Seasons.md` | Rewrite the four Season definitions as the maturity questions you gave (produce at all / consistently / without proportional cost / without the owner as fuel). **Delete** *"Usually $0–5,000/month"* from Survival. **Delete** the "Still Needed" requests for revenue bands, headcount ranges, and recurring-client ranges — those requests are the bug, not a gap. Add an explicit line: there is no universal business-level Season. Replace the deleted asks with a **graduation criteria — NEEDS ALEX** flag per Engine × Season, pointing at the Curriculum Map. |
| `VERIFY.md` | Section 3 "Season revenue bands" is now retired as a question, not answered. Rewrite it to say the model no longer has universal bands, and move the open question to per-Engine graduation criteria. |
| `02 Canon/Philosophy.md` | Audit for whole-company Season language; re-scope to per-Engine. |
| `03 Concepts/Business GPS.md` | Same audit. |

**I will not invent numerical graduation criteria.** Every cell gets `NEEDS ALEX` until you supply one or a source does.

### 2b — Demote Four Roles

| File | Change |
|---|---|
| `02 Canon/Four Roles.md` | **Moved** (git mv, history preserved) → `03 Concepts/Owner Role Evolution.md`. Reframed: a model for how the *owner's leadership role* evolves. Progression kept: Self-Employed → Supervisor → General Manager → Owner. The Season↔Role one-to-one table is **removed** — it is what makes the model imply a universal business Season. Explicit note added: a Survival-stage Engine does not mean the owner personally cleans houses. Tagged `engine: [Leadership]`. |
| `CONSTITUTION.md` §II | "Six documents" → five. Remove the `[[Four Roles]]` row. Add a third row to the *left Canon* table with the reason. |
| `03 Concepts/Business GPS.md` | Update link. |
| `03 Concepts/Owner-Dependent Revenue.md` | Update link. |
| `03 Concepts/SOPs.md` | Update link. |
| `03 Concepts/Sales Happen On The Phone.md` | Update link. |
| `03 Concepts/What The Money Makes Possible.md` | Update link. |
| `03 Concepts/When To Hire A VA.md` | Update link. |
| `02 Canon/Philosophy.md` (line 114) | Update link. |
| `00 Inbox/canon-proposals.md` | Log. |

Obsidian resolves `[[Four Roles]]` by filename regardless of folder, so the *move* breaks nothing; the *rename* does. All 8 inbound links get repointed to `[[Owner Role Evolution]]`, or an `aliases: [Four Roles]` line is added — say which you prefer. I lean toward repointing and no alias, so the old name stops circulating.

---

## Commit 3 — Five Pillars → legacy crosswalk

`refactor(curriculum): Five Business Pillars becomes a legacy crosswalk`

| File | Change |
|---|---|
| `03 Concepts/Five Business Pillars.md` | **Renamed** → `03 Concepts/Legacy Curriculum Crosswalk — Five Pillars.md`. Reframed from "the beginner's map" to "how Cleaning Biz 101 material maps into Four Engines × Four Seasons." Records the mapping — Acquire → Leads; Convert → Leads; Fulfill → Labor + Logistics; Operate → Logistics + Leadership; Finances → measurement across all Engines — **explicitly marked approximate, not exact.** The existing "unreconciled relationship" Conflict History callout is *resolved*, not deleted: converted to a supersession noting Four Engines is now primary and this page's job is migration. Purpose line added: new curriculum uses Four Engines × Four Seasons. |
| `03 Concepts/Business Finances.md` | Update link + the Finances-as-pillar framing. |
| `03 Concepts/When To Hire A VA.md` | Update link. |
| `03 Concepts/INDEX.md` | Regenerated. |
| `00 Inbox/canon-proposals.md` | Close the open Five Pillars proposal. |

**Untouched:** all five `01 Sources/Course Videos/Cleaning Biz 101 — *.md` files. Nothing in Sources is deleted, reworded, or reclassified by this commit.

---

## Commit 4 — Concept vs System classification

`refactor(structure): move execution pages from Concepts to Systems`

Test applied per page: **main value = understanding a principle → Concepts. Main value = following steps to produce an outcome → Systems.** Title is not evidence — `Three-Strike System` stays in Concepts, `Cleaner Availability System` moves.

### Proposed moves — clear (14)

`A2P Verification` · `IVR Setup` · `Automated Hiring Pipeline` · `Cleaner Availability System` · `Hiring a Cleaner SOP` · `Post-Clean Review Script` · `Review Response Scripts` · `Importing Contacts Into Harvest CRM` · `GBP Verification` · `GBP Posting Cadence` · `Handling A Lockout` · `Testing A New Cleaner` · `Weekend Operations` · `Payment Verification & Collection`

The first five are the ones you named. The rest are the same shape: dated steps, a checklist that is the point of the page, an outcome you can verify.

### Proposed moves — borderline, my call flagged (6)

| Page | My read | Recommend |
|---|---|---|
| `SMS Opt-In Consent` | Compliance principle *and* a build-once procedure, paired with A2P | **Move** |
| `Client Expectation Setting` | The value is the message and its timing | **Move** |
| `Website Technical SEO Basics` | Pure checklist | **Move** |
| `Cleaner Handbook` | A document you hand someone, not an idea | **Move** |
| `Scheduling Cleans` | You listed "scheduling processes," but the page is a decision rule — *two per cleaner per day* | **Keep**, and build a real Scheduling SOP separately |
| `Google Business Profile Naming` | Principle (the pin and the name are what matter) with setup steps attached | **Keep** |

### Explicit keeps worth naming (4)

`Three-Strike System` (policy, not procedure) · `Systems Cost-Benefit Analysis` (judgment rule) · `SOPs` (what an SOP *is*) · `Smart Lists` (stub; revisit when written).

Tool pages — `Harvest CRM`, `BookingKoala`, `Zapier` — stay in Concepts. They explain what a tool is and when to adopt it; the procedures built on them are separate pages.

**The other ~93 concept pages stay put.** Engine hubs stay in `04 Systems/`.

Each moved page also gets `type: system` in frontmatter and appears under "Workflows & SOPs" on its Engine hub, which means all four hub pages plus `Buying A Cleaning Business` are touched. `INDEX.md` regenerated.

---

## Commit 5 — Template simplification

`refactor(templates): default to update; drop mandatory empty sections`

| File | Change |
|---|---|
| `03 Concepts/_TEMPLATE.md` | Rewritten. Required: Frontmatter · One Line · Definition · When This Matters · Key Ideas / Decision Rules · Sources. Optional-when-useful: Symptoms · Common Mistakes · Examples · FAQ · Proof · Related Concepts · Conflict History · Presented In. The "Template Rules" block at the bottom — which mandates keeping every empty heading — is **deleted**; it is the rule that produced ten `*None yet.*` sections per page. |
| `04 Systems/_TEMPLATE.md` | **New.** Frontmatter · Outcome · Use This When · Prerequisites · Steps · Checklist · Metrics / Done Criteria · Templates & Resources · Sources · Related Concepts, plus optional Troubleshooting · Examples · FAQ · Conflict History. |
| `CONSTITUTION.md` | Rule 2: delete *"When genuinely unsure… they are two. Split now, merge later."* Replace with **DEFAULT TO UPDATE** and the four creation criteria. §VII: delete *"create them eagerly"* on stubs. §VIII step 5: delete *"should touch 5–15 pages."* §VIII step 6: delete *"Minimum five links."* The confidence test's "can't tell → create separately" branch → "can't tell → log to knowledge-gaps, don't create." |
| `.claude/commands/ingest.md` | Delete the "Unsure → Two. Split now" row, "Create stubs eagerly," and "five or more Related Concepts." |
| `.claude/commands/lint-vault.md` | Delete the fewer-than-five-links check and the missing-sections check. |
| `.claude/commands/lint-fast.md` | Same. |
| `chatgpt/gpt-instructions-block.md` (line 62) | Same rule, same fix. |
| `00 Inbox/knowledge-gaps.md` | **New.** Where uncertain new-page candidates go, with the existing pages each might belong to. |

**Empty filler sections are deleted opportunistically** — when a page is being edited for another reason. No bulk sweep across 117 pages in this commit; that would bury every other diff.

---

## Commit 6 — Source / Derived separation

`refactor(sources): AI summaries are derived interpretation, not evidence`

### 6a — The 12 explicit summaries (proposed now)

Move to `09 Derived/Source Summaries/`, adding `type: derived-summary`, `source:`, `generated:`, `status: Derived — Not Evidence`:

10 × `01 Sources/Coaching Calls/*-SUMMARY.md` · `01 Sources/Course Videos/Free Thumbtack Leads + GBP Optimization-SUMMARY.md` · `01 Sources/Student Calls/Evaluating the Specifics of the Biz-SUMMARY.md`

Their RAW `.txt` partners stay in `01 Sources/`, untouched. The source-record wrapper `.md` files (`2026-04-01 Weekly Coaching Call.md` and siblings) also stay — they are provenance records, which is exactly what you said may remain.

### 6b — The finding you should see before deciding

**171 lesson `.md` files inside the course folders are also AI-generated derived summaries.** They are not transcripts. Example — `Labor 101/How To_ Test Cleans with New Cleaners.md` opens with `## Quick Summary`, `## Core Teaching`, `## Key Principles`, `## Step-by-Step Process`; its raw partner `.txt` is the actual spoken transcript. Every one of the 171 has a `.txt` partner (166 matched exactly; 5 matched loosely on filename and need a manual look, of which `Every SOP We Use/In-Depth Breakdown of GHL StagesResponsibilities.md` may genuinely have no raw).

So `01 Sources/` currently holds roughly **185 files of evidence and 183 files of AI interpretation, undifferentiated.** Under your rule, those 171 are derived and shouldn't be citable as proof.

**I am not moving them in this commit.** Three reasons: they are the only navigable index of the course library; the Legacy Content Crosswalk (Commit 12) is built from them; and moving 171 files mid-refactor makes every later diff unreadable. **Recommendation:** leave them in place for now, add `status: Derived — Not Evidence` frontmatter so the claim register and lint can tell them apart from raw, and schedule the physical move as its own pass after the crosswalk exists. Say the word if you'd rather move them now.

### 6c — Empty category

`01 Sources/Video Transcripts/` contains nothing but `.gitkeep`. Transcripts live under their real course categories. **Remove the folder.** No file is deleted.

---

## Commit 7 — Harvest CRM duplicate resolution

`fix(links): one unambiguous [[Harvest CRM]] target`

Right now `03 Concepts/Harvest CRM.md` and `05 Products/Harvest CRM.md` share a filename, so all **59 `[[Harvest CRM]]` links across 29 files resolve silently and arbitrarily** — precisely the failure Constitution §VI warns about.

| File | Change |
|---|---|
| `05 Products/Harvest CRM.md` | **Renamed** → `05 Products/Harvest CRM Offer.md`. Keeps: pricing, DIY vs DFY setup paths, cancellation terms, eligibility. |
| `03 Concepts/Harvest CRM.md` | Keeps: what it is, how it works, when to adopt, its role vs BookingKoala. The `$197/mo` vs `$147/mo` note **moves to the Offer page** — it's a commercial fact — and stays flagged as unresolved, not merged. |
| 29 files containing `[[Harvest CRM]]` | Audited one by one. Links meaning *the software as knowledge* stay; links meaning *the thing you buy* → `[[Harvest CRM Offer]]`. Expected repoints: `05 Products/1-1 Coaching.md`, `05 Products/Group Coaching.md`, `Glossary.md`, `07 Company/The Faithful Cleaners.md`. |

Bare "Harvest" still means the Season. The product is always "Harvest CRM."

---

## Commit 8 — Product layer + claim register

`feat(products): product truth pages and a claim/proof register`

| File | Status |
|---|---|
| `05 Products/CleaningOS Free.md` | **New** — mostly `NEEDS ALEX`. I have no source describing it. |
| `05 Products/CleaningOS Membership.md` | **New** — $47/month, access to almost all core material. Sourced `Alex direct 2026-08-07`. |
| `05 Products/Group Coaching.md` | Rewritten — $297/month added. |
| `05 Products/1-1 Coaching.md` | $6,000 recorded as **current business direction**, held against the existing agreement (which says $6,000 via Klarna over 12 months — these agree; the *guarantee* wording is contract text and I won't touch it). |
| `05 Products/Harvest CRM Offer.md` | From Commit 7. |
| `07 Company/Claim Register.md` | **New** — Claim · Product · Source · Verification status · Permission status · Allowed in public marketing? · Notes. Statuses: VERIFIED / NEEDS VERIFICATION / DO NOT USE. |

**The 7-day free trial:** recorded as *historically existed; which tiers it currently applies to is unconfirmed* → `NEEDS ALEX`. I will not guess.

**Group Coaching's "$25k/month in 12 months":** entered as **DO NOT USE** until you classify it as contractual guarantee / target / aspirational / representative outcome, with qualifying conditions. It currently appears in `05 Products/Group Coaching.md`, `02 Canon/Philosophy.md` line 52, and `VERIFY.md`. All three get the register's status attached. It is not deleted.

**Student names** — Rick, Courtney, Keeley, Rashawn, Nicole, Jack, Melissa — all enter the register with permission status `UNCONFIRMED`. `VERIFY.md` already flags this. No name goes into customer-facing copy until you confirm.

No benefit, guarantee, or proof gets invented. Empty is recorded as empty.

---

## Commit 9 — Claude rules and Skills modernization

`refactor(agents): path-scoped rules, procedures into Skills`

| File | Change |
|---|---|
| `CLAUDE.md` | Slimmed. Stays concise. |
| `CONSTITUTION.md` | Reduced to identity, core model, core invariants, truth/evidence rules, folder meanings, governance. Multi-step procedure text moves out — §VIII's ingestion flow → the ingest Skill; §X's blast-radius mechanics → the reconcile Skill. The *rules* stay; the *steps* leave. |
| `.claude/rules/canon.md` · `sources.md` · `concepts.md` · `systems.md` · `products.md` · `marketing.md` | **New**, path-scoped to `02 Canon/**`, `01 Sources/**`, `03 Concepts/**`, `04 Systems/**`, `05 Products/**`, `06 Marketing/**`. |
| `.claude/skills/ingest/SKILL.md` · `draft/` · `reconcile/` · `process-inbox/` · `lint-vault/` · `save/` | **New.** Content migrated from the matching commands. |
| `.claude/commands/*.md` | Kept working. Reduced to thin pointers at the Skills. |
| `.claude/agents/evidence-auditor.md` | **New**, read-only (`Read, Grep, Glob`): locate original support for a claim, check permission state, report uncertainty. **Never creates proof.** |
| `.claude/agents/dedupe-scout.md`, `vault-auditor.md` | Kept. dedupe-scout's verdict language updated for default-to-update. |

Also in this commit — Changes 13 and 14, which are agent-behaviour changes:

- **Ingestion** (`ingest` Skill): preserve source → extract claims → search existing → prefer update → propose genuinely new pages → no automatic stubs → classify as concept / system / evidence / customer language / product fact / marketing idea / unresolved → update only what's materially improved → unresolved to Inbox → report. **No page quota.** One page or twenty, both valid.
- **Drafting** (`draft` Skill): remove the hard stop on missing non-essential sections (Student Examples, AI Prompts, FAQ). Drafting proceeds when the core teaching is verified. Factual proof, exact quotes, results and numbers still verify against **original Source material** — and explicitly **never** against an AI-generated summary alone. That gate is what makes Commit 6b matter.

---

## Commit 10 — Lint updates

`feat(lint): structural checks that matter; drop the volume metrics`

**Add:** broken wikilinks · exact duplicate titles across folders · pages whose `type:` contradicts their folder · invalid Engine values (not one of the four) · invalid Season values (not one of the four) · Canon conflicts · source files modified after ingestion (mtime vs. git) · customer-facing claims with no register status · ambiguous `[[Harvest CRM]]` links · orphaned Systems · contested claims unresolved past 60 days.

**Remove:** fewer-than-five-links · didn't-touch-enough-pages · missing optional template sections.

Files: `.claude/skills/lint-vault/SKILL.md`, `.claude/commands/lint-vault.md`, `.claude/commands/lint-fast.md`, `.claude/scripts/build_index.py` (Engine/Season validation), and a new `.claude/scripts/lint_structure.py` for the mechanical checks.

---

## Commit 11 — CleaningOS 4×4 Curriculum Map

`feat(curriculum): Engine × Season master planning matrix`

**New:** `05 Products/CleaningOS Curriculum Map.md`. All 16 cells. Per cell: desired outcome · graduation criteria · existing Concepts · existing Systems · existing course/video sources · existing resources/templates · what's missing · free or paid · confidence.

Built from what exists — the 117 concepts, the Systems after Commit 4, the 8 course folders, and the 16-cell action grid already on `03 Concepts/Business GPS.md`, which is the single best existing input.

**Graduation criteria are marked `NEEDS ALEX` wherever no source defines them.** Based on what I've read, that will be most of the 16.

---

## Commit 12 — Legacy Content Crosswalk

`feat(curriculum): map all legacy course material`

**New:** `05 Products/Legacy Content Crosswalk.md`. Rows: existing source/video · current legacy module · primary Engine · primary Season · secondary Engine · outcome taught · keep-as-is? · edit? · split? · merge? · retire? · candidate location in new CleaningOS · free/paid candidate · notes.

Coverage: **171 course lessons** across `Every SOP We Use` (31) · `Labor 101` (36) · `Leads 101 part 1` (35) · `Leads 101 Part 2` (22) · `Logistics Fundamental Course` (21) · `Free Resources and Mini Courses` (17) · `Google Biz Profile Setup and Growth` (5) · `Premium Resources` (4), plus 22 top-level course records and the 5 `Cleaning Biz 101` pillar files.

Skool is not reorganized. This commit only establishes what already exists.

---

## Verification

Before `MIGRATION_REPORT.md`: run the new lint · confirm no file in `01 Sources/` was deleted or content-edited (`git diff --stat` scoped to that folder must show only moves) · confirm zero broken wikilinks · confirm no new claim lacks a source · confirm Engine and Season values are valid vault-wide · confirm exactly one `[[Harvest CRM]]` target.

---

## Standing guarantees

- **No source material is deleted.** Not one file in `01 Sources/`. Moves preserve git history; RAW files are never rewritten.
- **No evidence is fabricated.** Missing numbers become `NEEDS ALEX`, never a plausible guess.
- **Your philosophy is not silently changed.** Every Canon edit is logged in `00 Inbox/canon-proposals.md` and listed in the final report as requiring your approval.
- **Nothing is silently overwritten.** Retired claims become collapsed `Superseded` blocks with what/source/replacement/reason — the Business GPS model included.
- **When uncertain: archive or flag.** Never delete, never guess.

---

*Clarity Creates Momentum.*
