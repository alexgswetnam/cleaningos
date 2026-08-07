---
type: company
title: Migration Report — CleaningOS v2
status: Complete
branch: refactor/cleaningos-v2
updated: 2026-08-07
---

# Migration Report — CleaningOS v2

**14 commits on `refactor/cleaningos-v2`.** Nothing merged to `main`. Fully revertable.

The goal was one intellectual model — **Four Engines × Four Seasons, governed by the Five
Laws** — and a vault that makes the next decision obvious.

---

## Verified before writing this

| Check | Result |
|---|---|
| Files in `01 Sources/` deleted | **0** |
| `.txt` files in `01 Sources/` modified | **0** |
| Files in `01 Sources/` content-edited | **0** — 13 entries, all moves or the one empty `.gitkeep` |
| Broken wikilinks in `02`–`09` | **0** |
| Wikilinks wrapped across a line break | **0** |
| `[[Harvest CRM]]` targets | **1** |
| Invalid Engine or Season values | **0** |
| `type:` contradicting its folder | **0** |
| Orphaned Systems | **0** |
| Structural lint | **1 error, 2 warnings — all pre-existing, none introduced** |

`python3 .claude/scripts/lint_structure.py .` reproduces this.

## Shape of the change

| | Before | After |
|---|---|---|
| Canon documents | 6 | **5** |
| Concepts | 117 | **100** |
| Systems | 5 | **23** |
| Products | 3 | **7** |
| Derived (new folder) | — | **14** |
| Path-scoped rule files | 0 | **6** |
| Skills | 0 | **6** |
| Subagents | 2 | **3** |

28 files created · 31 moved or renamed · 32 modified · 3 removed (one empty `.gitkeep`, two
folder placeholders).

---

## What changed, and why

### 1. Business GPS — the constraint is set by the goal

`fix(gps)`. The method taught *"the one lagging behind the others is your constraint."*
Replaced with the eight-step goal-anchored sequence and the rule in bold: **the
lowest-Season Engine is not automatically the current bottleneck.**

**Why:** it confused *maturity* with *relevance*. The old rule sends an owner to fix
Leadership while the thing actually stopping them is that nobody answers the phone.

The old method is preserved verbatim in a collapsed Superseded block. The 16-cell action
grid survives — it answers *what to do in a cell*, never *which cell you're in*, and that
distinction is now stated on the page.

**Your own workshop reading is the best evidence for the correction.** Every Engine reads
Scale or Harvest; Labor isn't the least mature — Leads sits at the same Season. Labor was
the constraint because the goal was more ad spend. The goal picked the Engine. The ranking
couldn't have.

### 2. Canon — Seasons describe Engine maturity

`refactor(canon)`. Four Seasons rewritten as four questions asked of **one Engine**.
Removed: `$0–5,000/month`, and the Still Needed asks for revenue bands, headcount ranges
and recurring-client ranges.

**Why:** those weren't a gap, they were a category error. If four Engines each sit in a
different Season, no single revenue figure indicates a Season. The old list requested
numbers that cannot exist.

Four Roles → `03 Concepts/Owner Role Evolution.md`. Progression, mechanism and the
$30K/month failure mode all survive; the one-Role-per-Season table does not, because it
implied one Season per business. **First Canon removal on grounds of correctness rather
than filing** — noted in §II so future readers see the distinction.

### 3. Five Pillars → legacy crosswalk

`refactor(curriculum)`. Reframed as a migration aid with mappings marked approximate.
Fulfill and Operate flagged as the weak rows — each spans two Engines.

**You had already decided this on 2026-08-06** — *"I almost never ever speak of it. I use
the 4 engines."* The page kept carrying a "do not teach these as the same model"
contradiction your own ruling had closed.

### 4. Concept vs System

`refactor(structure)`. 18 pages moved. Every page was read before it moved —
`Three-Strike System` is a policy and stayed; `Cleaner Availability System` is a weekly
routine and moved.

### 5–8. Templates, sources, Harvest CRM, products

Covered in the sections below and in the commit messages, which carry the full reasoning.

---

## Files moved

| From | To |
|---|---|
| `02 Canon/Four Roles.md` | `03 Concepts/Owner Role Evolution.md` |
| `03 Concepts/Five Business Pillars.md` | `03 Concepts/Legacy Curriculum Crosswalk — Five Pillars.md` |
| `05 Products/Harvest CRM.md` | `05 Products/Harvest CRM Offer.md` |
| 18 concept pages | `04 Systems/` |
| 12 `-SUMMARY.md` files | `09 Derived/Source Summaries/` |

**18 moved to Systems:** A2P Verification · IVR Setup · Automated Hiring Pipeline · Cleaner
Availability System · Hiring a Cleaner SOP · Post-Clean Review Script · Review Response
Scripts · Importing Contacts Into Harvest CRM · GBP Verification · GBP Posting Cadence ·
Handling A Lockout · Testing A New Cleaner · Weekend Operations · Payment Verification &
Collection · SMS Opt-In Consent · Client Expectation Setting · Website Technical SEO Basics
· Cleaner Handbook

## Files merged

**None.** No two pages were combined. Every merge candidate was flagged rather than acted
on — a wrong merge destroys a distinction that can't be recovered, and nothing here was
urgent enough to risk it.

## Files retired

**None deleted.** Three things were *reframed* while keeping their full prior text in
Superseded blocks: the Business GPS ranking rule, the universal Season revenue bands, and
Five Business Pillars as a customer-facing framework.

`01 Sources/Video Transcripts/` was removed — it contained only `.gitkeep`. The sandbox
cannot delete files, so the placeholder was relocated to `99 Scratchpad/`. **The empty
directory needs removing in Finder.**

---

## Canon changes requiring your approval

You approved these in session. They are recorded as §XII amendments at the top of
`CONSTITUTION.md` and as an EXECUTED entry in `00 Inbox/canon-proposals.md`. Listed here so
they're reviewable in one place:

1. **Canon: six documents → five.** Four Roles removed.
2. **Four Seasons rewritten** to per-Engine maturity; universal bands deleted.
3. **§II now states the model in one line** and requires your explicit approval before any
   second customer-facing business map exists.
4. **Rule 2 rewritten** to DEFAULT TO UPDATE with four creation criteria.
5. **Retired:** *"when unsure, they are two"* · *"create stubs eagerly"* · *"5–15 pages per
   ingestion"* · *"minimum five links."*
6. **Rule 3 gained "Evidence vs. interpretation"** — being *in* `01 Sources/` doesn't make a
   file evidence.
7. **§V gained a `09 Derived/` row.**
8. **Philosophy** — one warning marker on the $25k row. **The claim text is unchanged.**

> [!warning] The Canon lock does not work the way the Constitution claims
> §III says the lock is *"enforced at the tool layer… A prompt is a request; this is a
> wall."* The deny rules in `.claude/settings.json` did not block my writes — they bind
> Claude Code's tools inside this project, not every agent that can reach the folder. I
> wrote Canon with ordinary file tools.
>
> Left as-is and flagged. It's a governance decision, not a refactor step.

---

## Unverified claims

Full detail in `07 Company/Claim Register.md`.

### Blocked — DO NOT USE

**"$25,000/month in less than 12 months"** — [[Group Coaching]]. Legal status unresolved:
guarantee, target, aspiration, or representative outcome? The qualifying conditions behind
*"willing to make it work"* are undefined and currently doing legal work.

It also appears in `02 Canon/Philosophy.md`, which is now in **stated conflict** with the
register. I did not resolve that — editing a Canon page to match a product page is the drift
§X exists to prevent. Both pages carry a Contested callout naming the other.

### Needs verification

- **$47/month** and **"access to almost all core material"** — Membership. Your word only
- **$297/month** — Group Coaching. Your word only
- **$147 vs $197/month** — Harvest CRM. Two rates, no source reconciles them. The old page
  asserted they "read as two different things… not a contradiction." No source says that
- **7-day free trial** — existed historically; **which tiers it applies to now is unknown**
- **~$97/mo GoHighLevel** and the competitor pricing — third-party figures of unknown date

### Verified and safe

$6,000 program price · +$10k/mo in 3 months guarantee (**never without its Requirements to
Claim**) · the revenue-and-systems qualifier · VA sourcing and bootcamp inclusion.

### Permission — nine people, all UNCONFIRMED

Rick (32 pages) · Courtney (31) · Jack (29) · Elijah (21) · Melissa (9) · Rashawn (7) ·
Nicole (4) · Heidi (2) · Keeley (1).

**Verification and permission are different questions.** Every result traces to a call.
None is cleared to publish. Open in `VERIFY.md` since 2026-08-05.

### Asserted with no proof behind it

- **"95% of owners stuck under $20K/month are stuck on leads or sales"** — a stated
  proportion with no dataset, taught as fact on two pages
- Spanish-speaking labor cutting costs from ~50% to 30–35%
- Marketing budget ≈ 10% of revenue
- PPC display costing 4–6× per lead

Not blocked — they're teaching, not proof. But they must not harden into marketing
statistics.

---

## Remaining knowledge gaps

### Structural, logged in `00 Inbox/review-queue.md`

- **3 conflict-state defects, not fixed:** [[Price Objection]] contested with no resolution
  test; [[Cleaner Pay Structure]] and [[Subcontractor Vs W-2]] superseded with no reason.
  Inventing either to make a linter pass would fabricate the exact thing those fields record
- **4 borderline Concept/System calls** left in place: [[Cleaner Job Notes]],
  [[Transitioning Clients To New Cleaners]], [[Reactivating Past Clients]],
  [[Sales Pipeline Stages]]
- **`04 Systems/Cleaner Handbook.md`** shares a basename with a `.txt` in Sources. §VI bars
  it; the rule's purpose isn't violated since Obsidian resolves to the `.md`

### Content

- **Graduation criteria — all 16 cells.** The largest gap in CleaningOS
- **Membership exclusions.** "Almost all core material" can't be sold until you name what's
  excluded — the exclusion is what the next tier sells
- **Team leads.** Named as the action in three cells; defined nowhere
- **171 AI summaries still inside `01 Sources/`** — catalogued in
  `09 Derived/Derived Source Manifest.md`, physical move scheduled after the crosswalk
- **95 of 188 legacy lessons have no Season.** Half the library needs someone to watch it

---

## Curriculum coverage by Engine × Season

Pages tagged to each cell. Concepts + Systems.

| Engine | Survival | Stability | Scale | Harvest |
|---|---|---|---|---|
| **Leads** | 36 | 57 | 43 | **2** |
| **Labor** | 9 | 19 | 17 | **0** |
| **Logistics** | 7 | 28 | 30 | **2** |
| **Leadership** | 3 | 11 | 14 | 10 |

**Harvest is the promise of CleaningOS and the least documented part of it.** Labor ×
Harvest has zero pages — on the Engine [[Four Engines]] names as the first serious growth
ceiling, and the one you read as your own constraint. Leadership × Harvest is the only
populated Harvest cell and all ten pages are about *selling* a business, not running one
that doesn't need you.

Second pattern: **Leads Survival has 36 pages, Leadership Survival has 3.** A new owner gets
extensive marketing material and almost nothing on standards, boundaries, or refusing bad
work — which is what Leadership Survival actually is.

Per-cell detail: [[CleaningOS Curriculum Map]]. Legacy material: [[Legacy Content Crosswalk]].

---

## Recommended next three human decisions

### 1. Classify the $25k claim

Guarantee, target, aspiration, or representative outcome — and the qualifying conditions
behind "willing to make it work."

**Why first:** it's the only DO NOT USE in the register, it blocks Group Coaching from being
marketed at all, and it currently puts a Canon page in conflict with the register. One
sentence from you closes all three.

### 2. Name what CleaningOS Membership excludes

**Why second:** "almost all core material" is unsellable. Until the exclusion is named, both
[[CleaningOS Free]] and [[CleaningOS Membership]] are undefinable, the free/paid column is
`NEEDS ALEX` in all 16 curriculum cells, and no sales page can be written for a $47/month
product.

### 3. Write graduation criteria for four cells — not sixteen

Pick the four an owner actually moves through first: **Leads Survival → Stability**,
**Labor Survival → Stability**, **Logistics Survival → Stability**, **Leads Stability →
Scale.**

**Why third, and why only four:** sixteen is a project; four is an afternoon, and it covers
where most owners actually are. Without them the Seasons name a stage but can't move anyone
through one — which makes Business GPS a vocabulary rather than a diagnostic.

---

## Two housekeeping items

- **Turn Obsidian Git auto-backup back on** when you're done reviewing. It had crashed and
  left a stale `.git/index.lock` from 19:51 on 2026-08-06 — your backups had been silently
  failing since then. The lock is cleared.
- **Delete the empty `01 Sources/Video Transcripts/` folder** in Finder. Also `*.mp3` was
  added to `.gitignore`; an 82MB file in `00 Inbox/to-ingest/` was untracked and unignored.

---

*The goal was not a bigger vault. Clarity Creates Momentum.*
