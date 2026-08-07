# CleaningOS — Agent Entry Point

The vault **is** the business, in a form humans and machines can operate. Courses, VSLs,
emails and the CRM are outputs rendered from it.

## The model

**Four Engines × Four Seasons, governed by the Five Laws.**

| | |
|---|---|
| **Engines** | Leads · Labor · Logistics · Leadership |
| **Seasons** | Survival · Stability · Scale · Harvest — **the maturity of one Engine.** There is no business-level Season |
| **Laws** | Clarity Creates Momentum · Stop Guessing · Build In Order · The Roadmap Already Exists · One Step Wins |

One model. A second customer-facing map needs Alex's explicit approval before it exists.

## The four rules

1. Organize by **concept**, never by artifact.
2. **Nothing exists twice.** Default to update — read `03 Concepts/INDEX.md` before creating.
3. `01 Sources/` is **immutable**.
4. The wiki **is** the product.

## Never

- Edit `01 Sources/` or `02 Canon/` — propose to `00 Inbox/canon-proposals.md`
- Invent a quotation, statistic, student name, result, price, or guarantee
- Cite an AI summary as proof — raw source or nothing (`09 Derived/README.md`)
- Publish a claim marked `DO NOT USE` in `07 Company/Claim Register.md`
- Shorten "Harvest CRM" to "Harvest" — bare Harvest means the Season
- Teach a contested claim as settled, or silently pick a winner between sources
- Cite a session log as a source

## Where things go

| | |
|---|---|
| `03 Concepts/` | **Knowledge to understand.** One page per idea |
| `04 Systems/` | **Steps someone executes.** Plus the four Engine hubs |
| `05 Products/` | Things sold |
| `06 Marketing/` | Assets that promote |
| `07 Company/` | Internal — including the Claim Register |
| `09 Derived/` | AI interpretation of sources. **Never evidence** |

**Concept or System?** If the main value is understanding a principle → Concepts. If it's
following steps to produce an outcome → Systems. The title is not evidence.

Folder-specific rules load automatically from `.claude/rules/`. Read `CONSTITUTION.md` when
you need governance, evidence rules, or the contradiction protocol — not for every task.

## Voice — two separate layers

**Advising Alex, brainstorming, reviewing strategy, helping decide** → read
`Voice/AI Working Style.md`. Direct, opinionated, stress-tests ideas.

**Creating or substantially editing customer-facing content** → read
`Voice/Brand Voice.md`, plus `Voice/Alex Voice.md` for the sound. Use approved files in
`Voice/Examples/` as extra calibration — **never copy them verbatim.**

**Do not mix them.** The private layer may say "this is solving the wrong problem." A
CleaningOS email does not talk that way.

Technical work — moving files, linting, ingestion, dedupe, metadata, source processing —
needs neither, unless it includes writing customer-facing content.

## Skills

`ingest` · `draft` · `reconcile` · `process-inbox` · `lint-vault` · `save`

In `.claude/skills/`. The matching slash commands still work and point at these.

## Subagents

`dedupe-scout` — does a page already cover this idea?
`vault-auditor` — one audit dimension across the vault
`evidence-auditor` — what actually backs this claim? Read-only, **never creates proof**

## Scripts

Run from the vault root. All idempotent.

| | |
|---|---|
| `python3 .claude/scripts/build_index.py .` | Rebuild `03 Concepts/INDEX.md`. **After any change to `03 Concepts/` or `04 Systems/`** |
| `python3 .claude/scripts/lint_structure.py .` | Broken links, duplicate titles, invalid Engine/Season, type-vs-folder, unregistered claims |
| `python3 .claude/scripts/fix_wrapped_links.py .` | Wikilinks broken across a line break. `--write` to repair |
| `python3 .claude/scripts/build_manifest.py .` | Rebuild `00 Inbox/ingest-run.md` from what's staged |

## The four queues

- `00 Inbox/ingest-run.md` — what's staged, done, pending
- `00 Inbox/review-queue.md` — decisions an unattended run declined to make
- `00 Inbox/knowledge-gaps.md` — candidate pages that didn't clearly earn existence
- `00 Inbox/canon-proposals.md` — Canon changes waiting on Alex

## Two things that will bite you

- **A wikilink wrapped across a line break does not resolve** — and the page still *reads*
  as linked, so the failure is invisible.
- **`aliases:` in frontmatter are real links.** `Voice/Alex Voice.md` declares
  `aliases: [Voice]`, so `[[Voice]]` is valid. Any broken-link check must parse them.

## Parallel variants — not yet

`/ingest-fast` and `/lint-fast` only pay off above roughly 200 concept pages. See
`.claude/SCALING.md`. **`/ingest-all` must stay serialized regardless** — isolated agents
share only `INDEX.md`, so two at once produce duplicate concepts.
