---
paths:
  - "03 Concepts/**"
---

# Rules for `03 Concepts/`

**Knowledge to understand.** One page per idea, defined exactly once. Everything else links
here.

Speed To Lead · Client Lifetime Value · Labor Before Leads · Reciprocity · Pricing
Methodology · Owner-Dependent Revenue — that shape.

## DEFAULT TO UPDATE

Before creating anything, read `03 Concepts/INDEX.md`. Every concept in one line each.

**Create a new concept only when all four are true:**

1. Meaningfully distinct from existing knowledge
2. Independently reusable
3. Enough substance to be useful now
4. Likely to be referenced by curriculum, coaching, systems, or marketing

**Uncertain? Do not create pages.** Add the candidate to `00 Inbox/knowledge-gaps.md`,
naming the existing pages it might belong to. Do not create stubs automatically.

## Concept or System?

**If the page's main value is understanding a principle, it belongs here. If its main value
is following steps to produce an outcome, it belongs in `04 Systems/`.**

The title is not evidence. `Three-Strike System` is a policy and lives here.
`Cleaner Availability System` is a weekly routine and does not.

## Structure

`03 Concepts/_TEMPLATE.md`. Required: frontmatter, One Line, Definition, When This Matters,
Key Ideas / Decision Rules, Sources.

Everything else is optional and **added only when you have something to put in it.** Never
write `*None yet.*` under a heading. Delete empty filler sections when you find them.

## Links

Related Concepts records **meaningful relationships. No minimum count.** Five weak links are
worse than two strong ones.

Never let a wikilink wrap across a line break — it silently fails to resolve. Repair with
`.claude/scripts/fix_wrapped_links.py`.

## After any change

`python3 .claude/scripts/build_index.py .`
