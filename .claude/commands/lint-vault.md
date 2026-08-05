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

- Every `[[Target]]` resolving to nothing
- Pages with zero inbound links — invisible to browsing
- Pages with fewer than five outbound links, per the linking rule

## 4. Template compliance

- Missing sections (they should be present-and-empty, not deleted)
- Sections empty across many pages — this is a **content gap report**, the most useful
  output here. If 30 concepts have empty `Student Examples`, that's not a formatting
  problem, it's a business problem.
- Missing or malformed frontmatter
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

## 7. Stale stubs

`status: Stub` untouched 30+ days. Either the idea wasn't real or it's overdue.

## Output

Counts per section, then detail. Lead with the three findings that would most improve
the vault.

End with **What To Build Next**: 3–5 specific items ranked, each with one line on which
gap it fills. Prefer gaps that block content production — an empty `Templates` section
on a concept you're about to make a video about matters more than a tidy graph.

Fix frontmatter violations silently and note them. Everything else, ask first.
