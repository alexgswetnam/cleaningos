---
type: concept
engine: []                      # Leads | Labor | Logistics | Leadership
season: []                      # Survival | Stability | Scale | Harvest — of the Engine, not the business
laws: []                        # which of the Five Laws bear on this. Empty is valid.
status: Draft — Unverified      # Canonical | Developing | Draft — Unverified | Stub
sources: []
updated: YYYY-MM-DD
# superseded: YYYY-MM-DD        # uncomment when a claim here has been replaced
# contested: true               # uncomment while an unresolved dispute lives here
---

# {{Concept Name}}

> [!abstract] In one line
> The compressed claim. If you can't write this, you don't understand the concept yet.

## Definition

What it is. Two or three sentences, written so an owner in their first month understands
it. Say what it is *distinct from* if there's a page it gets confused with.

## When This Matters

What breaks without it, and when it becomes the owner's problem. Concrete — a number if a
source gives you one.

## Key Ideas / Decision Rules

The substance. What someone actually needs to know or decide. Structure it however the
idea wants — prose, a table, a short list of rules.

## Sources

Cite at the granularity of the claim. A number, script, policy or anything challengeable
gets the lesson (`Labor 101 → Determining Cleaners' Pay`), not the course.

-

---

## Optional sections — use only when you have something to put in them

**Do not add these empty.** A heading with `*None yet.*` under it is not information, it's
furniture. Delete empty sections when you find them.

- **Symptoms** — observable signals that this is the owner's problem right now
- **Common Mistakes** — what owners do instead, and why it fails
- **Examples** — real situations from sources, attributed
- **FAQ** — questions owners actually ask, pulled from calls
- **Proof** — verified results, with a row in `07 Company/Claim Register.md`
- **Related Concepts** — meaningful relationships only. **No minimum count.**
- **Conflict History** — superseded and contested claims
- **Presented In** — where this knowledge has shipped, so `/reconcile` can find it

Patterns for the conflict callouts:

```markdown
> [!failure]- Superseded — YYYY-MM-DD
> Previously: "the old claim, verbatim"
> Source: [[Old Source]]
> Replaced by: [[New Source]], YYYY-MM-DD
> Reason: why it changed

> [!warning] Contested
> **Claim A:** … — [[Source]]
> **Claim B:** … — [[Source]]
> **Unresolved since:** YYYY-MM-DD
> **What would settle it:** the specific test
```

> [!info] Why this template shrank — 2026-08-07
> It previously carried fourteen mandatory headings and a rule to keep every one of them,
> writing `*None yet.*` underneath rather than deleting. The theory was that an empty
> section is a visible gap. In practice it produced pages that were mostly headings, and
> readers learned to skip. **A gap belongs in `00 Inbox/knowledge-gaps.md`, where someone
> will act on it — not as an empty heading on a page nobody finishes reading.**
