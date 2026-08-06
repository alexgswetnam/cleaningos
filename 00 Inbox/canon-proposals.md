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
## YYYY-MM-DD — [[Page]] — proposed by <agent>
**Current:** what it says now
**Proposed:** what it should say
**Why:** the evidence, with source
```

---

## 2026-08-06 — [[Four Engines]] — proposed by Claude

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

## 2026-08-06 — [[Glossary]] — proposed by Claude

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

## 2026-08-06 — [[CONSTITUTION]] §II vs. `/ingest` Step 6 — proposed by Claude

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
