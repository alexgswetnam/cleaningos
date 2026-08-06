---
description: Parallel vault audit — five auditors at once. For large vaults.
argument-hint: "[folder]"
allowed-tools: Task, Read, Glob, Grep, Bash, Edit
---

Audit the vault using parallel auditors. Scope: `$ARGUMENTS` if given, else everything.

Same checks as `/lint-vault`, same output. The dimensions are independent, so they run
concurrently.

> [!warning] Use `/lint-vault` unless the vault is large
> Below roughly 200 pages a single pass is faster and cheaper. This exists for when a
> full audit has become a coffee-break job.

## Step 1 — Spawn five auditors in parallel

All in **one message**. Each gets exactly one dimension:

**Auditor 1 — Duplication & placement**
> Find duplicate concepts and canonical-location violations. Near-identical titles,
> heavy tag/content overlap, pages in `04`–`07` that *define* an idea instead of linking
> to one (Constitution §V), two pages citing the same source for the same claim. Read
> candidates before flagging — near-synonyms are often genuinely distinct. Propose which
> name survives.

**Auditor 2 — Graph integrity**
> Every `[[Target]]` resolving to nothing. Orphan pages with zero inbound links. Pages
> with fewer than five outbound links. For each orphan, propose where it should be
> linked from.

**Auditor 3 — Template & frontmatter**
> Missing or malformed frontmatter. `status: Canonical` with empty `sources:`.
> Presentation pages missing `renders:`. Deleted template sections (they should be
> present-and-empty). Count which sections are empty *across* pages — that aggregate is
> a content-gap report, not a formatting one.

**Auditor 4 — Canon drift**
> Pages contradicting `02 Canon/`. Every bare "Harvest" that means the product instead of
> the Season — must read "Harvest CRM". Owner/Client/Cleaner used incorrectly. Any
> guarantee or revenue number stated without naming its product. Drafts violating a rule
> in the Voice Log. Read `02 Canon/Language.md` and `Voice/Alex Voice.md` first.

**Auditor 5 — Conflict state**
> Contested claims older than 60 days, oldest first. Contested callouts missing "what
> would settle it." Supersessions with no reason recorded, or no blast-radius audit run.
> Undetected contradictions — two pages asserting incompatible claims with no callout on
> either. Propose classifications per §X; resolve nothing.

## Step 2 — Merge

Auditors don't see each other's findings, so the same root cause surfaces under several
dimensions. A page that's a duplicate is often also an orphan with bad frontmatter —
that's **one** problem, not three.

Merge before reporting:

1. Group findings by file
2. Identify the root cause where several findings share one
3. Rank by consequence, not count

## Step 3 — Report

Match `/lint-vault`'s format exactly: counts per section, then detail, leading with the
three findings that would most improve the vault.

End with **What To Build Next** — 3–5 ranked items, each with one line on the gap it
fills. Prefer gaps blocking content production over cosmetic graph tidiness.

Fix frontmatter violations silently and note them. Everything else, ask first. Send
anything needing a judgment call to `/reconcile`.

## Step 4 — Note the cost

State how many auditors ran and roughly what it cost versus a single pass. If the vault
has shrunk or the audit came back nearly clean, say plainly that `/lint-vault` would
have been the better choice. Don't let this command justify itself out of habit.
