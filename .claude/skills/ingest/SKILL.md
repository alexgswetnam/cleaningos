---
name: ingest
description: Ingest raw material into 01 Sources and compile it into canonical concepts and systems. Use when a transcript, call recording, course lesson, document or URL needs to become vault knowledge.
---

# Ingest

Turn one source into knowledge. `01 Sources/` gets the original; `03 Concepts/` and
`04 Systems/` get what it taught.

## 1. Preserve the original

Place the raw material in the right `01 Sources/` subfolder, verbatim. **It is now
permanently immutable.**

If a fetch returns a paywall, a JavaScript shell, or a fragment: **stop and say so.** A
partial ingestion corrupts the vault silently.

## 2. Identify what it actually contains

List the **claims, ideas and workflows** in it — not sections, not chapter headings. Name
each as it would be named as a page.

Show this list before writing anything.

## 3. Search existing knowledge

For each item:

- **Read `03 Concepts/INDEX.md` first.** Every concept and system, one line each. It
  resolves most of this step without opening a page, and it catches near-synonyms a title
  match misses
- Full-text search `02–07` only for what the index didn't settle
- Check `Glossary.md`

## 4. Prefer updating

| Finding | Action |
|---|---|
| A page covers this | **UPDATE it.** Add evidence, nuance, or the contradiction |
| Genuinely new, meets all four creation criteria | **CREATE** from the right template |
| A presentation of an existing idea | Record in `05`/`06` and **link** |
| Unsure | **Neither.** Update the closest page, log the candidate in `00 Inbox/knowledge-gaps.md` |

**The four criteria, all required:** meaningfully distinct · independently reusable ·
enough substance to be useful now · likely to be referenced by curriculum, coaching,
systems or marketing.

**Do not create stubs automatically.**

## 5. Classify every piece of new material

- **concept** — knowledge to understand → `03 Concepts/`
- **system** — steps someone executes → `04 Systems/`
- **evidence / example** — a result, a story, a number → the relevant page, and a row in
  `07 Company/Claim Register.md` if it could ever be customer-facing
- **customer language** — how owners actually talk → `Voice/` or the concept's FAQ
- **product fact** — price, inclusion, term, eligibility → `05 Products/` **and** the claim
  register
- **marketing idea** — an angle or hook → `06 Marketing/`
- **unresolved** → `00 Inbox/review-queue.md` or `knowledge-gaps.md`

## 6. Update only what the source materially improved

**There is no page quota.** A forty-minute source may legitimately update one page. It may
legitimately update twenty. Touching pages to hit a number produces edits nobody asked for.

Cite at the granularity of the claim — the lesson, not the course, for anything
challengeable.

## 7. Conflict check

Classify per Constitution §X **before** writing:

1. **Contradicts `02 Canon/`?** → **STOP.** Log to `00 Inbox/canon-proposals.md`. Do not
   ingest the rest of the source
2. **Different Season or Engine?** → not a conflict. Scope the claim
3. **Source is simply wrong?** → note its unreliability on the page. Source untouched
4. **Alex, newer, changed his mind?** → supersede. Write the `> [!failure]-` block with
   what / which source / replaced by / why. Set `superseded:`. Run the blast-radius audit
5. **Genuinely unresolved?** → `> [!warning] Contested`, both claims kept, `contested: true`,
   and state what would settle it

Can't classify confidently? Default to Contested and say so. Undated material can never
supersede.

## 8. Propagate and report

Add to the Engine hub if it belongs there. Add new terms to `Glossary.md` as pointers.
Regenerate: `python3 .claude/scripts/build_index.py .`

Report every file created or updated, one line each on why. Then conflicts found and how
handled, claims superseded plus the blast-radius table, unresolved items parked, and
anything you were unsure about.
