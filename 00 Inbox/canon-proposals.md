---
type: company
title: Canon Proposals
status: Developing
updated: 2026-08-05
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

**Why:** I'd lean B. The reason Canon is locked is that changing it silently changes
everything downstream — true of [[Five Laws]], [[Philosophy]], [[Four Seasons]], not really
true of an index whose entries all point at concept pages. But this is a Canon question and
§XII says you decide.

**Blocking:** No. Both A2P terms are defined on their concept pages; only the Glossary
index is behind.
