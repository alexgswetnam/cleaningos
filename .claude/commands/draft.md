---
description: Render a presentation asset from canonical knowledge
argument-hint: "<format> <concept>  e.g. youtube script for Hiring First Cleaner"
allowed-tools: Read, Write, Edit, Glob, Grep
---

Produce: `$ARGUMENTS`

If a mode is named (`teach`, `walk`, `straight`, `sell`), follow that mode's rules in
[[Voice]]. If none is named, infer from the format and **say which you chose** so Alex
can correct it — that correction is itself signal for `/voice`.

This command exists to enforce Constitution §IV — knowledge and presentation are
different things. You are rendering existing knowledge into a format, not researching
a topic.

## Step 1 — Load the voice

Read, in this order, before writing a word:

1. `02 Canon/Philosophy.md` — what we believe, how we teach
2. `Voice/Alex Voice.md` — **the anchors are the target.** Read the verbatim Alex samples
   before writing a word, and check the Voice Log for rules from past corrections.
3. `02 Canon/Language.md` — naming rules. "Harvest CRM" never shortens.
3. `02 Canon/Five Laws.md` and `Four Seasons.md` — the frames

If a section you need says *Not yet written*, **stop and tell me.** Do not improvise
philosophy. An invented belief in a YouTube script becomes a belief I have to defend on
a sales call.

## Step 2 — Read the concept, not the transcripts

Open the canonical concept page. It should already contain the definition, the
mistakes, the student examples, the objections, the analogies, the FAQ.

**Do not search `01 Sources/` for material.** If the concept page is missing something
you need, that is a gap in the concept page. Say so, offer to fill it via `/ingest`,
and stop. Pulling from transcripts is how the vault gets bypassed and slowly becomes
irrelevant.

Also read the concept's Related Concepts — the best content usually comes from the
connection, not the concept alone.

## Step 3 — Render

Match the format requested. Some defaults:

- **YouTube script** — hook, the mistake, the reframe, the one step, CTA
- **Email** — one idea, one story, one action
- **VSL / sales page** — enemy, promise, mechanism, proof, offer, objections
- **Course lesson** — where this sits on the roadmap, concept, checklist, template
- **Social post** — one claim, one proof, no CTA

Ask if the format is unclear rather than guessing.

## Step 3.5 — Conflict gate

Before writing, check every concept you're drawing from:

- `contested: true` in frontmatter, or a `> [!warning] Contested` callout covering the
  claim you're about to teach → **stop and ask me.** Do not pick a side, and do not
  write around it with vague phrasing. Teaching a disputed claim as settled is how this
  vault damages the business instead of helping it.
- A `> [!failure]- Superseded` block → make sure you're using the **current** claim, not
  the one in the collapsed history. This is an easy mistake to make when skimming.

If a concept is contested but the conflict doesn't touch what you're writing, proceed
and say which claim you avoided.

## Step 4 — Self-check before returning

- Does every claim trace to something on the concept page?
- Does it sound like the anchors in [[Voice]]? Read one, then read your draft. Same person?
- Any rule in the Voice Log violated?
- Every "Harvest" that means the product written as "Harvest CRM"?
- Does it contradict [[Philosophy]]?
- Owner vs. Client used correctly throughout?
- Would this sound like Alex read aloud, or like an AI?
- Did you teach any claim that sits under a Contested or Superseded block?

## Step 5 — File it

Save to `05 Products/` or `06 Marketing/` with full frontmatter:

```yaml
renders: [Hiring First Cleaner, Pricing]
shipped: YYYY-MM-DD
channel: youtube | email | course | vsl | social
live: true
```

**`renders:` is not optional.** It's what lets `/reconcile` find this asset later when
one of these concepts changes. An asset without it becomes invisible to correction and
will still be teaching a retired claim a year from now.

Presentation pages record what was shipped; they never become the source of truth.

Then add a line to the concept's own page noting where it's been presented, so the
graph stays two-way.
