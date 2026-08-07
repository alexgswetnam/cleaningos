---
type: company
title: Canon Proposals
status: Developing
updated: 2026-08-06
---

# Canon Proposals

Agents may not edit `02 Canon/` directly. Proposed changes go here for Alex to accept
or reject.

Format:

```
## YYYY-MM-DD — `[[Page]]` — proposed by <agent>
**Current:** what it says now
**Proposed:** what it should say
**Why:** the evidence, with source
```

---

## ⏳ AWAITING ALEX 2026-08-07 — [[Four Seasons]] and [[Four Roles]] — CleaningOS v2 refactor

> [!important] This is the Canon edit for Commit 2 on `refactor/cleaningos-v2`
> Alex directed these changes in writing and authorised execution under §XII, with the
> tool-layer lock in `.claude/settings.json` left in place. This entry is the amendment
> record. **Nothing has been applied yet** — approve and it goes in.

### 2a — [[Four Seasons]]: remove global Season revenue bands

**Current:** Survival opens *"Usually **$0–5,000/month**, though revenue alone doesn't
define the Season."* The "Still Needed" list asks for *"Revenue bands for Stability,
Scale, and Harvest"* and *"Headcount and recurring-client ranges per Season."* The four
Season definitions are written as descriptions of a whole business.

**Proposed:** Four Seasons describes the maturity of **each Engine independently**. There
is no universal business-level Season. The four definitions become questions you ask of
one Engine:

> **SURVIVAL** — Can this Engine reliably produce its required result at all?
>
> **STABILITY** — Can this Engine produce the result consistently and predictably?
>
> **SCALE** — Can this Engine increase output without proportional increases in
> complexity, errors, cost, or owner involvement?
>
> **HARVEST** — Can this Engine continue producing, monitoring, and improving its result
> without depending on the owner as its primary fuel?

Deletions:

- `$0–5,000/month` from Survival
- "Revenue bands for Stability, Scale, and Harvest" from Still Needed
- "Headcount and recurring-client ranges per Season" from Still Needed
- any phrasing implying the whole company sits in one Season

The existing descriptive prose for each Season is **kept**, re-scoped from "the business"
to "this Engine." The two superseded blocks (Sustain and Sell → Harvest) are untouched.

Specific thresholds move to the Engine × Season implementation map
([[CleaningOS Curriculum Map]], Commit 11), not the universal definition.

**No numerical graduation criteria will be invented.** Every cell is marked
`NEEDS ALEX` until Alex or a source supplies one.

**Why:** the bands are a category error, not a gap. If Leads can be in Scale while Labor
is in Survival — which [[Four Seasons]] already states under "The Structural Idea" — then
a single revenue figure cannot indicate a Season, because the four Engines producing that
revenue are in four different ones. The Still Needed list was asking for numbers that
cannot exist. Removing the request is the fix; answering it would have hard-coded the
error.

**Blast radius:** `VERIFY.md` §3 (the open ask), [[Business GPS]] (already corrected in
Commit 1), [[Philosophy]] line 168.

### 2b — [[Four Roles]] leaves Canon

**Current:** `02 Canon/Four Roles.md`, listed in `CONSTITUTION.md` §II as one of six
Canon documents. It maps one Role to each Season — Survival→Self-Employed,
Stability→Supervisor, Scale→General Manager, Harvest→Owner.

**Proposed:** move to `03 Concepts/Owner Role Evolution.md`, tagged
`engine: [Leadership]`. The progression stays: **Self-Employed → Supervisor → General
Manager → Owner.** The mechanism stays — you pull the business to the next stage by
acting like the next role up. The `$30K/month owner still acting self-employed` failure
mode stays; it is the best thing on the page.

**What is removed:** the one-Role-per-Season table, and every sentence stating that a
Role *defines* a Season.

**What is added:** an explicit note that this describes how the **owner's leadership role**
evolves, and that a Survival-stage Engine does **not** mean the owner personally cleans
houses. An owner with Leads in Harvest and Labor in Survival is not a self-employed
cleaner; they have a hiring problem.

**Why:** applied as universal Canon, Four Roles reintroduces exactly what 2a removes. One
Role per Season implies one Season per business — an owner cannot simultaneously be a
Self-Employed cleaner and a General Manager, so the model silently forces the four Engines
back into a single reading. Useful as a Leadership concept, contradictory as Canon.

**Consequences:** `CONSTITUTION.md` §II goes from six Canon documents to five, and the
"files that have left Canon on this test" table gains a third row. Governing-vs-descriptive
still applies — Four Roles is governing in form but wrong in substance, so this is the
first removal on grounds of *correctness* rather than *type*. Worth Alex noticing.

**Links repointed** (8 files): [[Business GPS]] · [[Owner-Dependent Revenue]] · [[SOPs]] ·
[[Sales Happen On The Phone]] · [[What The Money Makes Possible]] · [[When To Hire A VA]] ·
[[Philosophy]] · `CONSTITUTION.md`. No `aliases: [Four Roles]` will be added — the old name
should stop circulating. Say if you'd rather keep the alias.

---

## ✅ RULED 2026-08-06 — [[Four Engines]] — proposed by Claude

> [!success] Alex ruled, 2026-08-06
> *"The 5 parts are really meant to be an easy understanding of the model of businesses
> as a whole. I almost never ever speak of it. I use the 4 engines."*
>
> **Not a competing model.** The Five Pillars is generic business framing, not CleaningOS
> IP, and it is rarely taught. [[Four Engines]] is the diagnostic. There is no mapping to
> document and no contradiction to resolve — the apparent conflict came from an agent
> treating a generic framing device as a rival taxonomy.
>
> **Still open, but not a Canon question:** whether the Five Pillars should stay as the
> organizing spine of Cleaning Biz 101's 27 lessons. Alex is undecided. Tracked in
> `00 Inbox/review-queue.md`, not here.
>
> **Remaining Canon edit, if Alex wants it:** one line in [[Four Engines]] under Related
> Concepts — *"[[Five Business Pillars]] — generic business framing used occasionally with
> beginners. Not a CleaningOS model and not a rival to the Engines."* Optional.

**Current:** No mention of the "Acquire, Convert, Fulfill, Finances, Operate" framework
Alex uses with brand-new owners.

**Proposed:** Add `[[Five Business Pillars]]` to the Related Concepts list, and optionally
a one-line note under "Still Needed": *"How the beginner's Five Pillars framework
(Acquire/Convert/Fulfill/Finances/Operate) relates to this model — currently taught to
different audiences with no documented mapping."*

**Why:** [[2026-04-20 Weekly Coaching Call]] shows Alex onboarding a brand-new,
overwhelmed owner (Keeley) with a five-part generic-business framework instead of the
Four Engines diagnostic used with established members. It's plausibly a deliberate
simplification for beginners, not a competing model — but nothing in any ingested source
says so explicitly, and Finances gets its own pillar there while this page states finance
is *"not a separate production Engine."* Filed as a proposal rather than resolved
silently, per the Contradiction Protocol; the new page [[Five Business Pillars]] carries
the full writeup and an unresolved-relationship callout.

**Update 2026-08-06:** This is not just something said once on a beginner call — it's the
spine of an entire separate course, **Cleaning Biz 101** (27 lessons, uploaded and
ingested the same day, organized in five folders literally named Acquire/Convert/Fulfill/
Finances/Operate). The course's own opening lesson for each pillar defines it in terms
that map loosely onto [[Four Engines]] but aren't identical, same as before. This raises
rather than lowers the stakes of reconciling the two — a whole course is teaching a
five-part model alongside a Canon page teaching a four-part one, and no source says which
is meant to be primary or how a student should reconcile being taught both.

**Blocking:** No. Both frameworks stand independently; nothing downstream depends on the
mapping being resolved.

---

## ✅ ACCEPTED 2026-08-06 — [[Glossary]] — proposed by Claude

**Current:** No section for terms introduced by course lessons. Four terms now used on
`03 Concepts/` pages are undefined in the Glossary.

**Proposed:** Add a `## Terms From Course Lessons` section:

| Term | Definition | Source |
|---|---|---|
| **A2P** | Application-to-Person messaging. The carrier registration that lets a business send SMS through a platform. [[A2P Verification]] | Lesson |
| **Low Volume Mixed** | The A2P campaign type to select for a cleaning business — covers confirmations, reminders, and occasional promotions at small volume. | Lesson |
| **Naked URL** | A link written out as visible text (`https://site.com/terms`) rather than anchor text. Required in opt-in copy because the evidence is a screenshot. [[SMS Opt-In Consent]] | Lesson |
| **DIY / DFY** | Do-it-yourself vs. done-for-you setup of [[Harvest CRM]]. DFY is handled on the first onboarding call. | Lesson |
| **Zap** | One automation rule: when this happens in tool A, do that in tool B. [[Zapier]] | Lesson |
| **[[BookingKoala]]** | Booking and provider-management software used alongside [[Harvest CRM]]. Cleaners get a provider account in it at onboarding. | Lesson |

And to `## Terms From Coaching Calls`:

| Term | Definition | Source |
|---|---|---|
| **Micro-Commitment** | One small yes collected before the price — day, time, gate code. [[Micro-Commitments]] | Call |
| **Downward Inflection** | Voice drops at the end of the price, making it a statement. [[Price Delivery]] | Call |
| **Late Night DJ Voice** | Chris Voss tonality — slow, steady, deep. Used for non-negotiables. [[Price Delivery]] | Call |
| **Mirroring** | Matching a prospect's tone, pace, and professionalism. [[Mirroring]] | Call |
| **Reciprocity** | Framing a price reduction as a personal favour so it earns something back. [[Reciprocity]] | Call |

And a `## Terms From Buying & Selling` section:

| Term | Definition | Source |
|---|---|---|
| **SDE** | Seller's Discretionary Earnings. Profit plus everything the seller argues a new owner wouldn't spend. The number a business is priced on. [[Add-Backs And SDE]] | Broker call |
| **Add-Back** | An individual item added to profit to reach SDE. Each one is a claim, not a fact. [[Add-Backs And SDE]] | Broker call |
| **CIM** | Confidential Information Memorandum. The deal packet a broker sends after the NDA. | Broker call |
| **LOI** | Letter of Intent. Opens the due diligence window; not the purchase. [[Due Diligence]] | Broker call |
| **Balloon** | You make payments through the term, then pay the remaining balance at the end. **Not** a delayed start to payments — the source corrects this confusion explicitly. [[Deal Structure]] | Broker call |
| **Mailbox Money** | Passive income to a seller who retains equity. [[Deal Structure]] | Broker call |

**Why:** Ingested from `01 Sources/Course Videos/Get Phone Number + A2P Approval.md` and
`Zapier The Software Glue.md` (2026-08-06). All six terms appear on the concept pages
written from them. A student or
agent hitting "Low Volume Mixed" with no definition has to go back to the source, which is
what the Glossary exists to prevent.

---

## ✅ RESOLVED 2026-08-06 — [[CONSTITUTION]] §II vs. `/ingest` Step 6 — proposed by Claude

**Current:** The two documents give opposite instructions.

- `CONSTITUTION.md` §II: *"Agents may propose changes to Canon in `00 Inbox/canon-proposals.md`, but must never edit `02 Canon/` directly."*
- `.claude/commands/ingest.md` Step 6: *"Add new terms to [[Glossary]]."* — and `Glossary` lives in `02 Canon/`.

An agent following `/ingest` literally violates the Constitution on every single ingestion
that introduces a term. I followed the Constitution and filed the proposal above instead.

**Proposed:** Pick one, so the next agent doesn't have to guess.

- **Option A** — amend `/ingest` Step 6 to *"Propose new terms for [[Glossary]] in `00 Inbox/canon-proposals.md`."* Keeps the Canon lock absolute. Cost: every ingestion leaves a pending proposal for you to accept, and the Glossary lags the vault.
- **Option B** — amend Constitution §II to carve out the Glossary: *"Agents may append to [[Glossary]]. All other Canon pages are Alex-only."* The Glossary is an index of terms defined elsewhere, not a source of belief — appending to it can't change what the vault teaches. Cost: a small hole in an otherwise clean rule.

**Update 2026-08-06:** with [[Alex Voice]] moved out of Canon, **Option A is now the clean choice** and the Canon lock keeps zero exceptions. Superseding my earlier lean toward B.

**Why:** I'd lean B. The reason Canon is locked is that changing it silently changes
everything downstream — true of [[Five Laws]], [[Philosophy]], [[Four Seasons]], not really
true of an index whose entries all point at concept pages. But this is a Canon question and
§XII says you decide.

**Blocking:** No. Both A2P terms are defined on their concept pages; only the Glossary
index is behind.

---

## ✅ ACCEPTED 2026-08-06 — [[Alex Voice]] relocation — proposed by Claude

> [!success] Accepted and executed by Alex's instruction, 2026-08-06
> `02 Canon/Voice.md` → `Voice/Alex Voice.md`. Write policy added at the top of the file.
> CONSTITUTION §II and §XI amended; `CLAUDE.md` step 3 updated. An `aliases: [Voice]`
> entry keeps every existing `[[Voice]]` link resolving, including the two inside Canon
> that agents may not edit. Hard paths in `/voice`, `/draft` and `/lint-fast` repointed.
>
> Side effect worth noting: `/voice` instructed agents to write the Voice Log into a Canon
> file, so like the Glossary item below it was a command that could not be run without
> breaking §II. That is now fixed rather than merely documented.

**Current:** `Voice` lives in `02 Canon/`, so §II makes it Alex-only. Voice rules can
therefore only ever accumulate at the speed Alex hand-edits them, which is the opposite of
what the page's own learning loop describes: *"Voice is learned from corrections, not
descriptions… Run `/voice` after any edit."* The loop is specified and structurally
unrunnable.

**Proposed:** Move it out of Canon rather than carving an exception inside Canon.

1. Relocate `02 Canon/Voice.md` → `Voice/Alex Voice.md` — a new unnumbered top-level
   folder. Unnumbered on purpose: `00`–`07` encode the CleaningOS pipeline, and this file
   isn't CleaningOS-specific.
2. Give it a stated write policy at the top of the file:
   - **Anchors** — append-only. An agent may add a verbatim sample **only** when the
     speaker is unambiguous, and must record source and date. Evidence, not interpretation.
   - **Modes** — an agent may propose; promotion of a pattern into a Mode rule still needs
     the three occurrences the page already requires.
   - **Voice Log** — freely agent-writable. This is the part that has to move fast.
3. Amend §II to drop `[[Voice]]` from the Canon list, and §XI to point at the new location.
4. Update `CLAUDE.md` step 3 in the order of operations.

**Why:** Two reasons, and the second is Alex's.

**It isn't governing.** The stated reason Canon is locked is that *"everything else in the
vault flows downhill from these files; changing them silently changes everything."* True of
[[Five Laws]], [[Philosophy]], [[Four Seasons]] — those are beliefs and taxonomy. `Voice`
is descriptive. It records how Alex already sounds. An agent appending "he says X, not Y"
is not changing what CleaningOS believes. It was filed in Canon because it's important, and
importance is not the same thing as governance.

**It's portable and Canon isn't.** Alex, 2026-08-06: the file should be usable *"across
different vaults."* Voice is a property of the person, not of this business. If a second
vault starts, [[Philosophy]] does not travel and `Voice` does. A file that belongs to two
vaults cannot be governed by one vault's constitution.

Alex offered the alternative of letting agents write to `Voice` while it stays in Canon.
Recommending against it: an undocumented exception teaches every future agent that the
Canon lock is negotiable, which is the exact silent erosion §II exists to prevent. Note the
open [[Glossary]] question above is the same shape — if `Voice` moves out, Option A there
becomes clean and the Canon rule stays absolute with zero exceptions.

**Blocking:** No, but it blocks the item below.

---

## ✅ RESOLVED 2026-08-06 — [[Alex Voice]] anchors — proposed by Claude

> [!success] Alex ruled, 2026-08-06
> *"should not pull from the 1-1 document to sound like me. that is a legal contract."*
>
> Handled as a **Type 1 supersession** on [[Alex Voice]], not a confidence-table tweak.
> All nine previous anchors came from the 1:1 Coaching Agreement, and the entire derived
> pattern with them. Both are now in a collapsed `Superseded` block with the reason.
> Replaced with eight spoken anchors from [[2026-04-15 Weekly Coaching Call]], restricted
> to passages where attribution is unambiguous.
>
> **Blast radius: nil.** `06 Marketing/` is empty and every `renders:` field in
> `05 Products/` is empty, so nothing was ever drafted from the retired anchors.
>
> The agreement remains a valid source for *what it says* — [[Philosophy]] and
> [[1-1 Coaching]] cite it for content and are unaffected.
>
> Note the gap this opens: **informal written voice is now the vault's biggest hole.** The
> only voice evidence is one spoken session in which Alex was being coached rather than
> teaching. A real email or a post that performed would be worth more than another call.

**Current:** | Spoken voice | **Unknown** — no transcripts ingested |

**Proposed:** Raise to **Developing**, and add a note that written and spoken voice diverge
enough to matter.

**Why:** [[2026-04-15 Weekly Coaching Call]] is roughly 15,400 words with Alex speaking
throughout, much of it unrehearsed and personal. It's the first real sample of him talking.

The finding worth acting on: **the spoken voice does not sound like the anchors.** The
written anchors are precise, dry, and controlled — the 1:1 agreement register. Spoken Alex
self-interrupts, restarts sentences, leans on "like" and "honestly" and "I would say,"
circles a point before landing it, is openly warm with people, and gets concrete only when
pushed. Both are him. Drafting a YouTube script from the written anchors alone would
produce something too composed to sound like the person in this transcript.

Not filing sample anchors yet — that's an edit to a Canon page, and the relocation above
should be settled first. Once it is, the anchors are sitting in the raw file ready to pull.

**Caveat that constrains this:** the transcript has **no speaker labels**. Attribution is
by context only. Some passages are unambiguously Alex — addressed by name, answering a
direct question — and others cannot be safely attributed. Any harvesting must take only the
unambiguous ones. This is also the practical limit on Alex's "when we are confident it is
me speaking": with unlabelled transcripts, confidence is a judgement per passage, not a
property of the file.

**Blocking:** No.

---

## ✅ RESOLVED 2026-08-06 — [[Philosophy]] vs. Troy's framing — raised by Claude

> [!success] Alex ruled, 2026-08-06
> *"troy's framework is a helpful thing we used once."*
>
> Not something CleaningOS teaches, so there is nothing for [[Philosophy]] to reconcile and
> **no Canon change is needed.** The Contested block on
> [[2026-04-15 Weekly Coaching Call]] has been closed with the ruling recorded.

**The tension:** Troy's workshop teaches deliberate operation "between reality and riding
dragons" — believing past the evidence as the thing that expands what a person attempts.
[[Philosophy]] refuses to sell fantasy, insists on evidence before infrastructure, and lists
"work on your mindset" among the phrases Alex finds hollow when the industry uses them.

Logged as **Type 3 Contested** on [[2026-04-15 Weekly Coaching Call]], not Type 5. It's a
guest's framework rather than Alex revising a Law, so ingestion was not halted. §X directs
an agent who cannot classify confidently to default to Contested and say so.

**What's needed from Alex:** whether Troy's framing is something CleaningOS teaches, or
something Alex personally found useful once. Those are different answers with different
consequences, and only he can give them. If it's the former, [[Philosophy]] needs a
paragraph reconciling the two. If the latter, no change — and the contested block on the
source page can close.

**Blocking:** No. Nothing has been written that depends on the answer.

---

## ❌ WITHDRAWN 2026-08-06 — [[Language]] and [[Philosophy]] — proposed by Claude

> [!failure] Withdrawn — the proposal was wrong, twice
> `[[Voice]]` **is not broken.** `Voice/Alex Voice.md` carries `aliases: [Voice]` in its
> frontmatter, which Obsidian resolves. The Alex Voice relocation note two entries down
> says so explicitly — *"an `aliases: [Voice]` entry keeps every existing `[[Voice]]` link
> resolving, including the two inside Canon"* — and I filed this anyway, then re-confirmed
> it during the post-ingest audit and reported it to Alex as a live defect.
>
> **Root cause:** my link checker matched wikilinks against filenames only and never
> parsed `aliases:`. Two false positives, reported twice, plus a duplicate of this same
> proposal filed later the same day. Checker corrected; the vault has **2** genuinely
> broken links, both untouchable — an illustrative `[[Pricing]]` in `SETUP.md` and a
> wrapped link inside an immutable source.
>
> Nothing to do. Left in place rather than deleted so the mistake is on the record.

<details><summary>Original proposal</summary>


**Current:** Both pages link to `[[Voice]]` — `Language.md`: *"For how sentences sound,
see `[[Voice]]`."*; `Philosophy.md`: *"Read this and `[[Voice]]` before any customer-facing
output."* Neither resolves to a real file.

**Proposed:** Change both links to `[[Alex Voice]]`, which is the actual file
(`Voice/Alex Voice.md`, per `CLAUDE.md`'s own Order of Operations). Mechanical rename,
no content change.

**Why:** Found during `/lint-vault`'s broken-link scan. `Voice/Alex Voice.md` exists and
is exactly what both sentences are pointing at — this reads as a naming slip (the folder
is `Voice/`, the page is `Alex Voice`) rather than a missing page. Filed here rather than
fixed directly since both source lines live in `02 Canon/`, which agents may not edit.

**Blocking:** No, but it means two Canon pages currently send a reader to a dead link on
a topic (`Voice`) they explicitly say to read before writing customer-facing copy.

**Confirmed still broken 2026-08-06, post-ingest audit.** Exact lines: `Language.md:11`
and `Philosophy.md:334`. — *This confirmation was itself wrong; see the withdrawal note
above.*

</details>

---

## 2026-08-06 — [[Four Engines]] and [[Four Seasons]] — blast-radius audit note — proposed by Claude

> [!note] Audit re-run 2026-08-06 after the 135-lesson ingest — conclusion holds, evidence corrected
> The original version of this proposal justified itself with *"`06 Marketing/` is empty."*
> That was incomplete even then: it never checked `05 Products/`, which is **not** empty.
> Re-verified properly after the ingest:
>
> - `06 Marketing/` — still empty
> - `05 Products/` — 3 pages (1-1 Coaching, Group Coaching, Harvest CRM). **None mention a
>   retired term**, and all 3 carry `renders:`, so future audits can trace them
> - `"Sustain and Sell"` appears on exactly 2 pages, both of which *flag it as retired and
>   translated to Harvest* rather than teaching it
> - `"Bottlenecks"` appears only inside the source filename
>   `Premium Workshop — 4 Seasons, 4 Bottlenecks`, which is immutable under Rule 3 and is a
>   citation, not a claim
>
> **Nothing live teaches either retired term.** Risk is zero, now with evidence that covers
> the whole presentation layer rather than one empty folder.

**Current:** Both pages carry a `superseded:` frontmatter date and a well-documented
`[!failure]` block (Bottlenecks→Engines; Sustain and Sell→Harvest) with a reason recorded,
but neither notes that a blast-radius audit ran — i.e. a check for whether any shipped
asset still teaches the retired term.

**Proposed:** Add a line to each supersession block once Alex confirms the audit: *"Blast-
radius audit run 2026-08-06: `06 Marketing/` is empty and no page's `Presented In` section
lists either of these as shipped, so no live asset currently teaches the retired term."*

**Why:** Found during `/lint-vault`'s conflict-state scan, per `CONSTITUTION.md` §X's
instruction to flag supersessions with no audit note loudly — "this means published
assets may still teach a claim you've retired." I ran the check (grepped `06 Marketing/`
and every page's `Presented In` section) and found nothing shipped yet, so risk is
currently zero, but the audit itself was never recorded on either page. Filed here rather
than added directly since both are in `02 Canon/`.

**Blocking:** No — nothing is shipped, so there's nothing currently mistaught. Relevant
again the moment anything ships to `06 Marketing/` or gets a `Presented In` entry.

---

## ✅ RULE EXECUTED 2026-08-06 — [[CONSTITUTION]] §VI — filename collisions — proposed by Claude

**Current:** §VI governs naming but says nothing about a source file and a concept page
sharing a filename. One collision exists today:

- `03 Concepts/Hiring SOP.md`
- `01 Sources/Course Videos/Every SOP We Use/Hiring SOP.md`

Every `[[Hiring SOP]]` in the vault is therefore ambiguous — on [[SOPs]],
[[Hire Slow Fire Fast]], [[Cleaner Handbook]], [[Picking The Right VA]], and
`04 Systems/Labor Engine.md`. Obsidian resolves it by proximity rules and picks one
silently. Half those links may be pointing at a raw transcript instead of the concept.

**Proposed:** Add to §VI: *"A page in `03–07` may not share a filename with any file in
`01 Sources/`. Sources keep their original names (Rule 3), so the concept page is the one
that gets renamed."*

Then rename `03 Concepts/Hiring SOP.md` — `Hiring Process` or `Hiring Workflow` — and
repoint its inbound links. The source file is untouched, as Rule 3 requires.

**Why:** This is Rule 2's failure mode wearing a disguise. The idea has one page, but the
*name* has two targets, so the graph splits invisibly — the exact damage §III says
compounds silently. It will recur every time a course lesson happens to share a title with
a concept, which gets likelier as `01 Sources/` grows; it's at 224 files after one
ingest run.

**Blocking:** Not urgent, but it corrupts link integrity quietly and the fix gets more
expensive with every new inbound link.

---

## ✅ EXECUTED 2026-08-06 — [[CONSTITUTION]] §V — `08 Logs/` has no row — proposed by Claude

**Current:** §V's table assigns every folder a purpose. `08 Logs/` was created this session
for `/save` session records and has no row, so its rules live only in `CLAUDE.md` and a
README — neither of which is governing.

**Proposed:** Add a row:

| `08 Logs/` | Session records written by `/save` | Knowledge. Never linked to from a concept |

**Why:** Logs sit outside the knowledge hierarchy the way `99 Scratchpad/` does, but for
the opposite reason — scratchpad is junk you'd never miss, logs are an audit trail you
would. Without a row, a future agent has no governing instruction preventing it from
citing a log as a source, which would let a session narrative harden into knowledge.

**Blocking:** No. Worth folding in whenever §V is next touched.

---

## ✅ EXECUTED 2026-08-06 — [[CONSTITUTION]] §II — the Canon list is wrong three ways — proposed by Claude

> [!note] Supersedes the narrower "remove Glossary" version below
> Checking §II against `02 Canon/` to write that proposal turned up two further errors,
> both older than today. All three are in the same six lines, so they should be fixed in
> one pass.

**Three defects in §II's list:**

1. **The count is wrong, and has been.** Line 39 says *"Four documents hold the
   intellectual property"* — then lists six bullets.
2. **[[Four Roles]] is missing.** `02 Canon/Four Roles.md` exists, carries
   `type: canon` and `status: Canonical`, and is linked by [[Philosophy]] itself plus
   seven concept pages ([[SOPs]], [[Owner-Dependent Revenue]], [[Business GPS]],
   [[When To Hire A VA]], [[Sales Happen On The Phone]], [[What The Money Makes Possible]]).
   **The Constitution does not mention it once, anywhere.** A governing document is
   silently absent from the list of governing documents.
3. **[[Glossary]] is listed but left** — moved to the vault root on 2026-08-06.

**Proposed replacement for lines 39–47:**

```markdown
Six documents hold the intellectual property. They are the constitution's body, and
no page anywhere in the vault may contradict them.

- [[Five Laws]] — Stop Guessing · Clarity Creates Momentum · Build In Order · The Roadmap Already Exists · One Step Wins
- [[Four Engines]] — Leads · Labor · Logistics · Leadership
- [[Four Seasons]] — Survival · Stability · Scale · Harvest. Each Engine has its own.
- [[Four Roles]] — Self-Employed · Supervisor · General Manager · Owner. One per Season; the role is how you move between them.
- [[Philosophy]] — what we believe, what we reject, how we teach
- [[Language]] — naming rules. "Harvest CRM" is always both words
```

*(Gloss verified against `02 Canon/Four Roles.md` — the roles are Self-Employed,
Supervisor, General Manager, Owner. Not "Technician"; that's the E-Myth term, and your
page doesn't use it.)*

**And extend the `> [!info] Voice used to live here` note**, or add a sibling:

> **Glossary moved out — 2026-08-06 by Alex.** Same reasoning as Voice, minus
> portability. The Glossary is an *index*: every real definition lives on a concept page
> and a row here is a pointer to one, so appending can't change what the vault teaches.
> It also has to move at the speed of ingestion, which the Canon lock made impossible —
> `/ingest` Step 6 ordered agents to do what §II forbade, so the Glossary simply fell
> behind. Write policy is at the top of the file.

**Why this matters more than a typo:** §II is the source of the Canon lock. Every other
rule about what agents may not touch resolves through this list. An agent reading it today
learns that a file which isn't locked is (Glossary), and never learns that a file which is
locked exists at all (Four Roles) — so it may edit `02 Canon/Four Roles.md` believing it's
an ordinary page. That is the one failure mode §II exists to prevent, and it's live now.

**Worth deciding while you're here:** two files have now left Canon on the same test —
*is it governing, or is it descriptive?* Voice records how you sound; the Glossary indexes
what words mean elsewhere. Neither changes what CleaningOS believes. If that test is going
to keep being applied, it belongs written into §II rather than re-derived from two
precedent notes each time.

**Blocking:** The Four Roles omission, mildly — an agent could edit a Canon file today
without knowing it's Canon.

---

## ✅ SUPERSEDED 2026-08-06 — [[CONSTITUTION]] §II — remove Glossary from the Canon list — proposed by Claude

**Current:** §II lists six documents as the Canon, including:

> - [[Glossary]] — every defined term

Alex moved `Glossary.md` out of `02 Canon/` to the vault root on 2026-08-06, resolving the
§II vs. `/ingest` Step 6 contradiction above. The file is gone from Canon but §II still
names it, so the governing document now describes a structure that doesn't exist.

**Proposed:** Two edits.

1. Delete the `[[Glossary]]` bullet from §II's list. The Canon is now five documents:
   [[Five Laws]], [[Four Engines]], [[Four Seasons]], [[Philosophy]], [[Language]].
2. Extend the existing `> [!info] Voice used to live here` note to cover this move, or add
   a sibling note:

   > **Glossary moved out — 2026-08-06 by Alex.** Same reasoning as Voice, minus
   > portability. The Glossary is an *index*: every real definition lives on a concept
   > page and a row here is a pointer to one, so appending can't change what the vault
   > teaches. It also has to move at the speed of ingestion, which the Canon lock made
   > impossible — Step 6 of `/ingest` ordered agents to do what §II forbade, and in
   > practice the Glossary simply fell behind. Write policy is stated at the top of the
   > file.

**Why:** §II is the source of the Canon lock. If it lists a file that isn't locked, the
next agent either edits Canon believing the Glossary is in it, or refuses to write to the
Glossary believing it still is. Both are wrong, and the document that exists to remove
that ambiguity is now the thing creating it.

Note this is the *second* file to leave Canon by this argument, which is worth Alex
noticing: the test that moved both was **"is it governing, or is it descriptive?"** Voice
records how Alex sounds; the Glossary indexes what words mean elsewhere. Neither changes
what CleaningOS believes. If a third candidate appears, that test is now precedent — and
it may be worth writing it into §II explicitly rather than re-deriving it each time.

**Blocking:** No, but it is a governing document describing the wrong structure, which is
the one kind of staleness §XII exists to prevent. Two-line fix.

---

## 2026-08-06 — Remaining action from §VI — rename `03 Concepts/Hiring SOP.md`

**Not a Canon proposal.** The §VI rule is written and in force; this is the one existing
violation it makes illegal, left for Alex because it needs a name.

`03 Concepts/Hiring SOP.md` collides with `01 Sources/Course Videos/Every SOP We Use/Hiring
SOP.md`. Under §VI the source keeps its name (Rule 3) and the concept gets renamed.

Inbound links to repoint after the rename: [[SOPs]], [[Hire Slow Fire Fast]],
[[Cleaner Handbook]], [[Picking The Right VA]], `04 Systems/Labor Engine.md`.

**Candidate names** — the page describes the sequence for hiring a cleaner, so §V says it
may belong in `04 Systems/` rather than `03 Concepts/` at all:

| Name | Note |
|---|---|
| `Hiring Process` | Closest to current meaning, no collision |
| `Hiring Workflow` | Signals it's a sequence — but then §V says move it to `04 Systems/` |
| `Hiring A Cleaner` | Names the decision rather than the artifact, most consistent with §VI's "name the idea, not the container" |

I lean **`Hiring A Cleaner`**, staying in `03 Concepts/`. Say the word and I'll rename and
repoint every link.
