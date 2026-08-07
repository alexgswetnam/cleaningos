---
type: log
date: 2026-08-06
status: Complete
---

# 2026-08-06 — Session memory, concept index, and the first unattended ingest run

## What I Did

- Built `03 Concepts/INDEX.md` and its generator — every concept in one line, ~5,600 tokens
  replacing a 92,000-word search space. Wired into `CLAUDE.md`, `/ingest`, and `/lint-vault`.
- Added `/resume` and `/save`, and `08 Logs/`. The vault had no session continuity before this.
- Added `/ingest-all`, a manifest-driven loop that works `00 Inbox/to-ingest/` to empty using
  one fresh-context subagent per source, serialized, with the index regenerated between each.
- Added `.claude/settings.json`. Beyond pre-approving tools so an unattended run doesn't stall,
  it denies `Edit` on `01 Sources/**` while allowing `Write` — Rule 3 enforced at the tool layer
  rather than by trusting an agent to have read it. Canon is denied outright.
- Ran the loop: **8 courses, 135 lessons.**

## Files Touched

**Created — machinery**

- `.claude/scripts/build_index.py`, `.claude/scripts/build_manifest.py`
- `.claude/commands/resume.md`, `save.md`, `ingest-all.md`
- `.claude/settings.json`
- `00 Inbox/review-queue.md`, `00 Inbox/ingest-run.md`, `00 Inbox/to-ingest/`
- `03 Concepts/INDEX.md`, `08 Logs/`

**Created — knowledge.** 16 concept pages, 2 stubs filled, 8 course source records, ~230 raw
lesson files archived. Concepts went 101 → 117.

New pages: [[Importing Contacts Into Harvest CRM]], [[Building Connection]],
[[AI Chatbots For Sales]], [[Payment Processor Selection]], [[Systems Cost-Benefit Analysis]],
[[Picking The Right VA]], [[When To Fire A VA]], [[Website Strategy]],
[[Ideal Customer Profile]], [[Sell The Result Not The Service]], [[Owner Learns Marketing First]],
[[Hire Slow Fire Fast]], [[Three-Strike System]], [[Cleaner Job Notes]],
[[Should Clients Have A Cleaner's Number]], [[Cleaner-Caused Damage]], [[When To Fire A Client]].
Stubs filled: [[Backup Cleaner]], [[Testing A New Cleaner]].

**Updated.** ~60 concept and hub pages. The four courses `00 Inbox/ingestion-queue.md` flagged as
"still genuinely unconfirmed" — Logistics Fundamental, Leads 101 parts 1 and 2, Labor 101 — are
all now ingested.

## Post-Run Repairs

Ran after the ingest, once the audit showed what the run had actually done to the graph.

- **41 hard-wrapped wikilinks repaired across 25 pages.** `[[Sales Pipeline\nStages]]`
  does not resolve in Obsidian, and the page still *reads* as linked, so the failure is
  invisible. This was 41 of the 49 broken links in the vault. Concept/system orphans went
  from a handful to **zero** (only `INDEX` and `_TEMPLATE` remain, both intentional).
  New script: `.claude/scripts/fix_wrapped_links.py`, which refuses to touch `01 Sources/`
  or `02 Canon/`. Now idempotent — a second run finds nothing.
- **`/lint-vault` §3 rescoped.** Orphan checking now covers `03 Concepts/` and
  `04 Systems/` only, and the section runs the wrapped-link script first.
- **`/ingest-all` now writes a `running` marker before spawning**, not after returning.
  This is the Logistics bug fixed at the source.
- **`/ingest` Step 4 gained a citation-granularity rule.** Cite the course for background,
  the lesson for anything disputable. The test: could you find the evidence in under a
  minute if Alex challenged the line?
- **Fixed my own dead links** in `review-queue.md`, `ingest-run.md`, and the staging
  README — I'd written `[[ingestion-queue|Ingestion Queue]]` where Obsidian resolves on the *filename*,
  `ingestion-queue`. Aliased form now used throughout.

Broken links: **49 distinct → 2.**

> [!failure] Correction — my link checker was wrong
> I reported the two `[[Voice]]` links in `02 Canon/` as broken, twice, and filed a Canon
> proposal about them. They are not broken. `Voice/Alex Voice.md` declares
> `aliases: [Voice]` and Obsidian resolves aliases; the Alex Voice relocation note says so
> in as many words. My checker compared wikilinks against filenames only and never parsed
> frontmatter. Proposal withdrawn, checker corrected, `/lint-vault` §3 now requires alias
> handling.
>
> The two genuinely broken links are an illustrative `[[Pricing]]` in `SETUP.md` and one
> wrapped link inside an immutable source. Neither is fixable and neither matters.

## Post-Run Audit

Everything above rested on eight subagents' self-reports. This checked their work
independently.

**Held:**

- **Rule 3.** No pre-existing source file was modified by any agent. The one `M` in git is
  a CRLF→LF conversion timestamped 20:00:34, before the first subagent ran — Alex's file
  sync, not an agent. Content byte-identical.
- **Canon lock.** `02 Canon/` and `CONSTITUTION.md` untouched.
- **§VII frontmatter.** 117/117 compliant. No `Canonical` page with empty `sources:`.
- **Template structure.** 113/117 complete; the 4 deviations are pre-existing pages
  missing `## Models`, not from this run.
- **Rule 2.** An independent auditor with no stake in the work read all 19 new pages plus
  every flagged comparison and found **zero** violations. Each new page carries an explicit
  `Distinct from [[X]]` line, and in every case traced, the distinction was real rather
  than merely asserted.
- **Figures.** 189 of 194 dollar amounts and percentages on concept pages trace to an
  archived source. Four of the five misses are arithmetic shown in-line ($300 × 35% =
  $105); one was a format variant ($1M vs 1,000,000).
- **The pay-floor conflict.** All four quotes verified verbatim in the archive. It is
  *worse* than reported: the interview script's promise ends *"This is outlined further in
  the subcontractor agreement"* — pointing candidates at the document that says the
  opposite.

**Found and fixed:**

- **5 of 19 new concepts never reached their engine hub** (§Step 6). Mostly from the
  interrupted Logistics run. Added to Logistics, Leadership, and Leads hubs.
- **One unsourced statistic.** [[When To Hire A VA]] asserts *"the workshop cites an owner
  at $45K/month with no VA — working 12 hours a day."* A full-corpus scan of all 224
  source files found no `45K`, no `45,000`, and no such owner. The workshop's only `$45`
  is *"~$45/hour"* cleaner pay. **The line predates this session** — it is in the last
  commit — so the ingest didn't cause it; the audit surfaced it. Flagged on the page and
  parked; not deleted, since it may come from unignested material or from Alex directly.

**False alarm:** the auditor flagged `laws: []` on one new page as an oversight. It's on 14
of 117 pages — a normal state, not a defect.

**Still unresolved and now biting:** the `/ingest` Step 6 instruction to add new terms to
[[Glossary]] is unfollowable, because the Glossary is in `02 Canon/` and agents may never
edit it. 19 new concepts, 0 glossary entries. Already filed as a Canon proposal earlier
today; this run is the evidence it matters.

## Decisions Alex Made

- Rejected Graphify. It parses code; this vault has none. The Obsidian half of both guides is a
  weaker version of what CleaningOS already does.
- Sources come from Google Drive, staged by hand into `00 Inbox/to-ingest/`.
- Autonomy level: auto-proceed, park the close calls. Agent decides the mechanical work; anything
  ambiguous goes to `review-queue.md` and the run continues.
- Canary first (3 lessons) before committing to 135.

## Open Threads

1. **Work `00 Inbox/review-queue.md`.** Six items. The cleaner pay-floor contest is the one that
   matters — see Escalations.
2. **Three Canon proposals are waiting** in `00 Inbox/canon-proposals.md` — the dead `[[Voice]]`
   links, the `Hiring SOP` filename collision, and a §V row for `08 Logs/`. All three are §XII
   territory: Alex amends, agents propose.
3. **12 `-SUMMARY` files in `01 Sources/Coaching Calls/` are dead weight.** Each pairs with a raw
   transcript that is cited 9× while the summary is cited 0×. Decide whether they earn their place.
4. **The 79MB mp3 is `blocked`, not failed** — needs a transcript before it can be ingested.
5. **Back-cite the pay-floor pages at lesson level.** The new `/ingest` rule applies going
   forward, but the pages already written still cite three course names for the vault's most
   consequential dispute.

## Escalations Left Standing

**The cleaner pay floor — four company artifacts, four positions, none dated.** This is not a
tidiness problem. A guaranteed hourly minimum is an employee-like signal, so these documents point
at different worker classifications:

| Artifact | Says |
|---|---|
| Cleaner Handbook | **$28.00/hr** MEA, framed as a real floor |
| Subcontractor Agreement, Exhibit A | **$25.00/hr** reference rate, discretionary, explicitly *"not a weekly floor"* |
| Labor 101 interview script | **$25/hr** — *"we'll pay the difference to make sure you got at least that much"* |
| Labor 101 coaching lesson | same $25 figure — *"I'm not guaranteeing anything"* |

The interview script is the sharp end: if it's still spoken verbatim to candidates, there is a de
facto floor regardless of what the Agreement says. No agent should resolve this. Recorded on
[[Cleaner Pay Structure]] and [[Subcontractor Vs W-2]].

**Also contested, all awaiting Alex:** [[GBP Verification]] (pre-recorded video first vs. request
live from the start), [[Close Rate By Channel]] (Meta 3–5% vs ~10%), and the two pre-existing
items [[Reciprocity]] and [[Drop Scope Not Price]] — both were checked against the newly-dated
April 2 and April 6 sales training calls this session and **neither was settled.** That negative
result is itself worth knowing: those two have now survived a targeted attempt to date them.

**No Canon conflicts.** Nothing was written to `00 Inbox/canon-proposals.md` this run.

## Related Concepts

- [[CONSTITUTION]]
- [[ingest-run|Ingest Run]]
- [[review-queue]]
- [[ingestion-queue|Ingestion Queue]]
