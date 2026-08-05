---
description: Parallel ingest — spawns scouts for the duplication check. For large vaults.
argument-hint: "<file path or URL> [category]"
allowed-tools: Task, WebFetch, Read, Write, Edit, Glob, Grep, Bash
---

Ingest `$ARGUMENTS` using parallel duplication scouts.

Identical to `/ingest` in every rule and output. The only difference is that Step 3 runs
concurrently. Read `CONSTITUTION.md` and apply it.

> [!warning] Use `/ingest` unless the vault is large
> Below roughly 200 concept pages, sequential is faster — a scout spends more time
> reading the Canon than it saves searching. Use this only when the duplication check
> has become the slow part.

## Step 1 — Archive to Sources

As `/ingest`. Raw material into the right `01 Sources/` subfolder, immutable from that
moment. Stop and report if the fetch returned a paywall or fragment.

## Step 2 — Extract ideas

List the distinct ideas in the source, each as a page name plus a one-line description.
Show me the list. **Do not spawn anything until I've seen it** — a bad extraction
multiplied across parallel agents is just a faster mistake.

## Step 3 — Spawn scouts in parallel

Launch one `dedupe-scout` per idea, **all in a single message** so they run
concurrently. Give each exactly one idea:

```
Idea: Cleaner Retention
Description: why cleaners leave in the first 90 days and what prevents it
Search the vault and return your verdict block.
```

Scouts are read-only. They cannot write, and that is deliberate — it is what stops two
of them racing to create the same page.

Cap at **8 scouts per batch.** More than that and you're paying more in spawn overhead
than you save. If a source yields more than eight ideas, run two batches.

## Step 4 — Cross-check the scouts against each other

**This step does not exist in `/ingest` and skipping it defeats the whole command.**

Each scout searched in isolation. Two of them can independently return NEW for what is
actually one concept under two names — `Cleaner Retention` and `Why Cleaners Quit` —
and if you act on both verdicts you create exactly the duplicate you were trying to
prevent. Parallelism introduced this risk; you have to close it.

So before writing anything:

1. Collect every verdict, including each scout's `NEAREST` field.
2. Compare the **NEW** verdicts against one another. Any two whose ideas or `NEAREST`
   values overlap are a collision candidate.
3. Read both candidates yourself. Decide: one concept or two?
4. Per the Constitution, when genuinely unsure — **two**. Split, and note it for
   `/lint-vault` to propose a merge later.

Report the cross-check explicitly, even when it finds nothing:

```
CROSS-CHECK
  Cleaner Retention (NEW) vs Why Cleaners Quit (NEW)
    → same concept. Merging into "Cleaner Retention".
  Pricing Anchors (NEW) vs Pricing (EXISTS)
    → distinct. Anchoring is a tactic within Pricing; creating as separate page.
  No other collisions among 6 verdicts.
```

Resolve every **UNCLEAR** yourself here too. Read the adjacent page and rule. If you
still can't, ask me — do not default to creating.

## Step 5 — Write, sequentially

You do all writing. Never delegate it. Sequential writes avoid git conflicts and let you
keep the whole picture in view as pages start referencing each other.

Follow `/ingest` Steps 4 through 7 exactly: write updates and new pages, run the §X
conflict classification (including the Canon halt and the blast-radius audit), propagate
to engine hubs and glossary, then report.

## Step 6 — Report

The standard `/ingest` report, plus:

- Scouts spawned, and their verdict spread
- The cross-check result
- Any UNCLEAR you resolved, and how

If the cross-check found no collisions across several runs, say so — that's evidence the
vault's naming is disciplined enough that you could raise the batch size.
