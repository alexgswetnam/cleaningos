---
name: lint-vault
description: Structural health check of the vault - broken links, duplicate titles, classification conflicts, invalid Engine or Season values, unproven claims, conflict state. Use when auditing vault integrity.
---

# Lint Vault

**Report first. Fix only what Alex approves.**

Mechanical checks: `python3 .claude/scripts/lint_structure.py .`
Wrapped links: `python3 .claude/scripts/fix_wrapped_links.py .` (add `--write` to repair)

## What is checked

### 1. Graph integrity
- Broken wikilinks, after excluding wrapped ones. **Honour `aliases:`** — `Voice/Alex Voice.md`
  declares `aliases: [Voice]`, so `[[Voice]]` is valid
- **Ambiguous `[[Harvest CRM]]` links** — exactly one target may exist
- **Exact duplicate titles** across folders — Constitution §VI
- **Orphans in `03 Concepts/` and `04 Systems/` only.** Never report orphans in
  `01 Sources/` — ~170 course lessons live there by design and will never have inbound
  links. Reporting them buries the real orphans
- **Orphaned Systems** specifically — a procedure nobody can find

### 2. Classification
- `type:` contradicting the folder
- Concept pages whose main value is a procedure, and System pages that define an idea
- **Invalid `engine:`** — anything not Leads, Labor, Logistics, Leadership
- **Invalid `season:`** — anything not Survival, Stability, Scale, Harvest

### 3. Evidence and claims
- `status: Canonical` with empty `sources:`
- **Customer-facing claims with no row in `07 Company/Claim Register.md`**
- Register rows stuck at NEEDS VERIFICATION
- **Named students without a cleared permission status**
- **Source files modified after ingestion** — compare mtime against git. `01 Sources/` is
  immutable and a modification is a defect, not a detail
- Pages citing a file in `09 Derived/` or a course-folder `.md` as proof

### 4. Canon drift
Pages contradicting `02 Canon/`. Every bare "Harvest" meaning the product. Owner / Client /
Cleaner misuse. Any guarantee or revenue number stated without naming its product. **Any
universal Season claim** — Seasons describe one Engine, never the business.

### 5. Conflict state
Contested claims older than 60 days · contested callouts missing "what would settle it" ·
supersessions with no reason · supersessions with no blast-radius audit · presentation pages
missing `renders:` · undetected contradictions.

Send anything needing a decision to the `reconcile` skill.

### 6. Index freshness
Any page in `03 Concepts/` or `04 Systems/` with `updated:` later than the index's. Any page
missing an `In one line` block. Regenerate at the end.

## Not checked — deliberately retired 2026-08-07

- ~~Pages with fewer than five outbound links~~ — there is no minimum
- ~~Ingestions that didn't touch enough pages~~ — there is no quota
- ~~Missing optional template sections~~ — they are optional

These measured volume, not health, and drove the proliferation the v2 refactor removed.

## Output

Counts per section, then detail. Lead with the three findings that would most improve the
vault. End with **What To Build Next** — 3–5 items ranked, each with one line on the gap it
fills. Prefer gaps that block content production.

Fix frontmatter violations silently and note them. Everything else, ask first.
