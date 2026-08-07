---
description: Health check — duplicates, orphans, broken links, gaps, Canon drift
argument-hint: "[folder]"
allowed-tools: Read, Glob, Grep, Bash, Edit
---

Audit CleaningOS. **Report first. Fix only what I approve.**

Scope: `$ARGUMENTS` if given, else the whole vault.

## 1. Duplicate concepts — highest priority

The rule this vault lives or dies by. Find:

- Pages with near-identical titles
- Pages with heavy tag and content overlap
- A page in `04–07` that *defines* an idea instead of linking to a concept — this is
  the most common way duplication sneaks in
- Two pages citing the same source for the same claim

Read candidates before flagging; near-synonyms are often genuinely distinct. For each,
propose which name survives and what merges.

## 2. Canonical location violations

Per Constitution §V: ideas belong in `03 Concepts/`. Flag any page in `04–07` that
defines rather than links.

## 3. Broken links and orphans

**Run `python3 .claude/scripts/fix_wrapped_links.py .` first** (dry run), then report.
A wikilink hard-wrapped across two lines — `[[Sales Pipeline\nStages]]` — does not
resolve, and the page still *reads* as linked, so this failure is invisible without
the script. It was the cause of 41 of 49 broken links the first time anyone checked.

- Every `[[Target]]` resolving to nothing, after wrapped links are excluded. **Honour
  `aliases:` in frontmatter** — Obsidian resolves them and a filename-only check does not.
  `Voice/Alex Voice.md` declares `aliases: [Voice]`, so `[[Voice]]` is valid. A checker
  that missed this reported two false positives twice and generated a bogus Canon
  proposal on 2026-08-06.
- **Orphans — check `03 Concepts/` and `04 Systems/` ONLY.** Do not report orphans in
  `01 Sources/`. Roughly 170 files there are individual course lessons living inside a
  course folder, and concepts cite the *course record*, not each lesson. They are archive
  by design and will never have inbound links. Reporting them buries the handful of real
  orphans under ~170 false positives and teaches the reader to skip this section.

## 4. Frontmatter and classification

**Do not report missing optional sections.** They are optional, and the old rule that
they be present-and-empty is retired — see Constitution Rule 2.

- Missing or malformed frontmatter
- **Invalid `engine:` values** — anything not Leads, Labor, Logistics, Leadership
- **Invalid `season:` values** — anything not Survival, Stability, Scale, Harvest
- **`type:` contradicting the folder** — `type: concept` in `04 Systems/`, and the reverse
- **Pages in `03 Concepts/` whose main value is a procedure**, and Systems pages that
  define an idea instead of linking to one
- `status: Canonical` with an empty `sources:` — a page asserting things nothing backs

## 5. Canon drift

Pages that contradict `02 Canon/`. Also: every bare **"Harvest"** that means the product
rather than the Season (must read "Harvest CRM"). Owner/Client/Cleaner used incorrectly.
Any guarantee or revenue number stated without naming its product. Drafts violating a
rule in the [[Voice]] Log. List each with file and line.

## 6. Conflict state

Per `CONSTITUTION.md` §X:

- **Contested claims older than 60 days.** List with age, oldest first. A stale dispute
  is blocking content production somewhere.
- **Contested callouts missing "what would settle it."** An argument with no resolution
  path is stored forever.
- **Supersessions with no reason recorded.** Six months on, these are indistinguishable
  from mistakes.
- **Supersessions with no blast-radius audit run.** Flag loudly — this means published
  assets may still teach a claim you've retired.
- **Presentation pages missing `renders:`.** Without it the blast-radius audit can't
  trace them, so these are invisible to correction.
- **Undetected contradictions:** two pages asserting incompatible claims with no callout
  on either. Propose a classification for each; don't resolve them yourself.

Send anything needing a decision to `/reconcile` rather than resolving it here.

## 7. Index freshness

`03 Concepts/INDEX.md` is what every other agent reads instead of searching. If it's
stale, Rule 2 is being enforced against an out-of-date map.

- Any page in `03 Concepts/` or `04 Systems/` with an `updated:` later than the index's
- Any page missing an `In one line` block — these are invisible to search-before-create
  and show up in the index's own **Needs A One-Liner** section
- Regenerate at the end of the audit: `python3 .claude/scripts/build_index.py .`

## 8. Stale stubs

`status: Stub` untouched 30+ days. Either the idea wasn't real or it's overdue.

## Output

Counts per section, then detail. Lead with the three findings that would most improve
the vault.

End with **What To Build Next**: 3–5 specific items ranked, each with one line on which
gap it fills. Prefer gaps that block content production — an empty `Templates` section
on a concept you're about to make a video about matters more than a tidy graph.

Fix frontmatter violations silently and note them. Everything else, ask first.
