---
type: canon
title: Constitution
status: Canonical
updated: 2026-08-05
---

# CONSTITUTION

The governing document of CleaningOS. Every agent — Claude, ChatGPT, or anything built
later — reads this first and obeys it without exception.

> [!abstract] What this is
> CleaningOS is not documentation of a business. It is the business, in a form both
> humans and machines can operate. The course, the VSL, the YouTube channel, the CRM,
> the emails — all of them are *outputs* rendered from this vault. The vault is the
> asset. Everything else is a presentation of it.

---

## I. Mission

To help ordinary people build a real business that gives them ownership of their time.

A cleaning business can be more than a way to replace a paycheck. Built correctly, it can
let someone leave a job they hate, be present with their family, travel, make art, serve
their church or community, and choose what their days are for. It can also create
dependable work and dignity for the people on the team.

Money matters because it creates options, but the final product is not money. **The final
product is a person who no longer feels trapped.**

Full version — the enemy, the promise, what we believe — in [[Philosophy]].

---

## II. The Canon

Four documents hold the intellectual property. They are the constitution's body, and
no page anywhere in the vault may contradict them.

- [[Five Laws]] — Stop Guessing · Clarity Creates Momentum · Build In Order · The Roadmap Already Exists · One Step Wins
- [[Four Engines]] — Leads · Labor · Logistics · Leadership
- [[Four Seasons]] — Survival · Stability · Scale · Harvest. Each Engine has its own.
- [[Philosophy]] — what we believe, what we reject, how we teach
- [[Language]] — naming rules. "Harvest CRM" is always both words
- [[Glossary]] — every defined term

**Canon is edited by Alex only.** Agents may propose changes to Canon in
`00 Inbox/canon-proposals.md`, but must never edit `02 Canon/` directly. Everything
else in the vault flows downhill from these files; changing them silently changes
everything. **There are no exceptions to this rule** — see the note below on why
[[Alex Voice]] was moved out rather than exempted.

> [!info] Voice used to live here — amended 2026-08-06 by Alex
> [[Alex Voice]] now lives in `Voice/`, outside the numbered folders, and agents may write
> to it under the policy stated at the top of that page.
>
> Two reasons. It is **descriptive, not governing** — it records how Alex already sounds,
> so appending to it cannot change what the vault teaches. And it is **portable**: voice
> belongs to the person, not the business, so it should survive into any other vault Alex
> builds, which a file governed by this constitution cannot.
>
> The alternative was a carve-out keeping Voice in Canon with write access. Rejected:
> an exception inside the lock teaches every future agent that the lock is negotiable,
> which is the exact silent erosion this section exists to prevent.

---

## III. The Four Rules

### Rule 1 — Organize by concept, never by artifact

The unit of knowledge is an idea, not a file. A video is not knowledge; it's a
container that knowledge arrived in.

```
WRONG                          RIGHT
Videos/                        03 Concepts/
  Lesson 1.mp4                   Hiring First Cleaner.md
  Lesson 2.mp4                   Pricing.md
```

The video becomes a source. The idea inside it becomes a page. One video may feed
fifteen pages; one page may draw on thirty videos. That many-to-many relationship is
the entire point.

### Rule 2 — Nothing exists twice

There is exactly **one** page per concept. It is canonical. Everything else links to
it.

```
WRONG                          RIGHT
Hiring Notes.md                Hiring First Cleaner.md
Hiring Overview.md             ← everything links here
Hiring Script.md
```

Before creating any page, search the vault. If a page covers this idea under any name,
**update it**. Creating a near-duplicate is the single most destructive thing an agent
can do here, because it splits the graph invisibly and the damage compounds silently.

When genuinely unsure whether two ideas are one concept or two: **they are two.** Split
now, merge later — `/lint-vault` surfaces merge candidates. An unnecessary split is
visible and cheap to fix. A wrong merge destroys distinctions you can't recover.

### Rule 3 — Sources are immutable

Everything in `01 Sources/` is read-only, permanently. No edits, no reformatting, no
"cleaning up," no deletions. Ever.

If a transcript is garbled or a source is wrong, note that on the concept page that
cites it. The source stays as it is. It is the evidentiary record.

The only permitted write to `01 Sources/` is **adding a new source file**.

### Rule 4 — The wiki is the product

Not notes about the product. The product.

Judge every page by this test: *could someone build this part of the business from this
page alone?* If not, the page isn't finished — it's a summary pretending to be
knowledge.

---

## IV. Knowledge vs. Presentation

The most important distinction in this system.

| Knowledge | Presentation |
|---|---|
| `Hiring First Cleaner.md` | Course Lesson 17 |
| Lives in `03 Concepts/` | Lives in `05 Products/`, `06 Marketing/` |
| One canonical page | Unlimited renderings |
| Changes when you learn something | Changes when the channel changes |

A YouTube video, a VSL, a lesson, an email, and a sales call answering an objection are
five presentations of the same underlying knowledge. They are not five pieces of
knowledge.

**Consequence for agents:** when asked to write a YouTube script, an email, or a
lesson, you do **not** search transcripts. You read the canonical concept page — which
already contains the philosophy, the student stories, the objections, the mistakes, the
analogies — and render it into the requested format. Presentation pages record *what
was shipped and where*; they never become the source of truth.

If you find yourself pulling a fact from a transcript that isn't on the concept page,
that's a signal the concept page is incomplete. Update the concept page first, then
write the script.

---

## V. Canonical Location Rule

The folders are a filing system, not a set of competing homes. Without a tiebreak,
"Referrals" plausibly belongs in Concepts, Systems, and Marketing at once — and Rule 2
dies. So:

| Folder | Holds | Never holds |
|---|---|---|
| `02 Canon/` | The IP. Laws, engines, seasons, philosophy, language | Anything operational |
| `03 Concepts/` | **Every idea.** The default home. One page per idea | Workflows, deliverables |
| `04 Systems/` | Engine hubs, SOPs, workflows — *sequences of concepts* | New idea definitions |
| `05 Products/` | Things sold or shipped | Knowledge |
| `06 Marketing/` | Assets that promote | Knowledge |
| `07 Company/` | Internal ops, vision, meetings | Anything customer-facing |
| `99 Scratchpad/` | Junk. Never linked to | Anything you'd miss |

**The tiebreak, stated once:** if an item is an *idea*, it goes in `03 Concepts/`. If
it is a *sequence, deliverable, or asset*, it lives in its own folder and **links to**
the concepts it uses. A page in `04–07` that defines an idea instead of linking to one
is a bug.

So: `Hiring Flow` (a workflow) lives in `04 Systems/` and links to
`[[Hiring First Cleaner]]`, `[[Interview Process]]`, `[[Cleaner Retention]]` — each of
which lives in `03 Concepts/` and is defined exactly once.

---

## VI. Naming Conventions

- **Title Case With Spaces.** `Hiring First Cleaner.md`, not `hiring-first-cleaner.md`.
  Wikilinks are read by humans; make them readable.
- **Singular, not plural.** `Referral.md` → actually no: use the form you'd say aloud.
  `Referrals.md` is right if that's how you talk. Consistency beats grammar.
- **Name the idea, not the container.** `Pricing.md`, never `Pricing Notes.md`,
  `Pricing Overview.md`, or `Pricing v2.md`. Qualifier suffixes are how Rule 2 dies.
- **No dates or versions in filenames.** Git holds history.
- **Sources keep their original names** plus a source ID prefix where one exists
  (`Video 41 — Hiring Your First Cleaner.md`).

---

## VII. Required Frontmatter

Every page in `02–07` carries this. Agents write it without being asked.

```yaml
---
type: concept | system | product | marketing | company | canon
engine: [Leads | Labor | Leadership | Logistics]
season: [Survival | Stability | Scale | Harvest]      # see Four Seasons
laws: [Stop Guessing]                                  # which laws bear on this
status: Canonical | Draft — Unverified | Developing | Stub
sources:
  - Video 41
  - Coaching Call #17
updated: YYYY-MM-DD
superseded: YYYY-MM-DD    # last time a claim here was replaced. Omit if never.
contested: true           # omit unless an unresolved dispute lives on this page
---
```

- `status: Stub` means the page exists to be linked to but isn't written yet. Stubs are
  how the vault tells you what to build next — create them eagerly.
- `sources:` is not decoration. An empty `sources:` on a `Canonical` page means the page
  asserts things nothing backs up. `/lint-vault` flags these.
- `updated:` gets bumped on every touch.
- `superseded:` and `contested:` make conflict state queryable across the whole vault.
  Before writing any customer-facing copy, an agent checks `contested:` on every concept
  it draws from — see §X.

Presentation pages in `05`/`06` additionally carry:

```yaml
renders: [Hiring First Cleaner, Pricing]   # concepts this asset teaches
shipped: YYYY-MM-DD
channel: youtube | email | course | vsl | social
live: true | false                          # is it still being served to people?
```

`renders:` is what makes the blast-radius audit possible. Without it, a superseded
claim can't be traced to the assets teaching it, and §X's audit degrades to guesswork.
Any agent creating a presentation page must fill it.

---

## VIII. How Agents Think

Before writing anything, in this order:

1. **Read the Canon.** [[Philosophy]] and [[Language]] at minimum. Every output must
   sound like it came from the same mind.
2. **Search for an existing page.** By title, by tag, by full text. Assume it exists.
3. **Decide: update or create.**

```
New content arrives
        │
        ├── Does a page for this idea already exist?
        │       │
        │      YES ──→ UPDATE that page. Add the new evidence,
        │               new nuance, or flag the contradiction.
        │               Bump `updated:`. Add to `sources:`.
        │
        └──    NO  ──→ Is it genuinely a new idea, or a
                        different presentation of an existing one?
                        │
                        ├── New idea ──→ CREATE in 03 Concepts/
                        │                 using the standard template.
                        │
                        └── New presentation ──→ Record it in
                                          05/06 and LINK to the
                                          existing concept.
```

4. **Propagate.** A single ingestion should touch 5–15 pages: the concept pages it
   updates, the stubs it spawns, the engine hub, the glossary.
5. **Link.** Every page ends with Related Concepts. Minimum five links. A page with
   fewer hasn't been thought about hard enough.

---

## IX. How Agents Update

- **Never delete a source.** Ever. See Rule 3.
- **Never delete a concept page** without fixing every wikilink pointing at it.
- **Never edit `02 Canon/`.** Propose changes in `00 Inbox/canon-proposals.md`.
- **Never invent** a quotation, statistic, student name, or result. If it isn't in a
  source, it doesn't go in the vault. A fabricated student win in a concept page will
  eventually be read aloud on a sales call.
- **Never smooth over a contradiction.** If two sources disagree, both go on the page
  under `> [!warning] Contested`. Contradictions are information.
- **Always report** every file touched, grouped by created / updated, one line each on
  why.

---

## X. Contradiction Protocol

When new material conflicts with what the vault already says, agents must first
**classify the conflict**. "Contradiction" covers five different situations and they
are handled differently. Getting this wrong either buries a real change or freezes the
vault in warnings nobody reads.

### The five types

| Type | Looks like | Handling |
|---|---|---|
| **1. Supersession** | Same claim, different answer, newer source | **Newest wins.** Demote the old claim to a `Superseded` block. Run the blast-radius audit. |
| **2. Season-scoped** | "Do X" vs. "don't do X" | **Not a contradiction.** Split the claim by season on the page. |
| **3. Genuine dispute** | Outside source vs. our experience, unresolved | **Contested.** Both stay. Neither wins until Alex rules. |
| **4. Bad data** | A source misremembers a number or event | **Note and discard.** Record on the page that the source is unreliable here. Never edit the source. |
| **5. Canon conflict** | New material violates a Law, Season, or Philosophy | **STOP.** Do not write. Escalate to Alex. |

### Classification rules

Work through these in order:

1. **Does it contradict `02 Canon/`?** → Type 5. Halt immediately. Write the conflict to
   `00 Inbox/canon-proposals.md`, report it, and **do not ingest the rest of the source**
   until Alex rules. Either he misspoke, or his thinking moved and a Law needs amending.
   Both outcomes need a human.

2. **Do the two claims apply to different seasons or engines?** → Type 2. Not a
   conflict. Restructure the page so the claim is scoped:
   *"In Survival, do X. By [later season], do Y instead."* Most apparent contradictions
   in this vault will be this. Check for it before anything else.

3. **Is one claim demonstrably an error** — a misremembered number, a garbled
   transcript, a student misstating what they were told? → Type 4. Add a line to the
   page's Examples section noting the source is unreliable on this point. The source
   file stays untouched forever.

4. **Are both claims Alex's, at different times?** → Type 1. Supersession. Newest wins.

5. **Is it Alex vs. an outside source, or two of Alex's claims where the newer one
   looks like a mistake rather than a change of mind?** → Type 3. Contested.

If you cannot confidently classify, default to **Type 3 (Contested)** and say so.
Contested is recoverable; a wrong supersession quietly deletes a belief.

### Type 1 — Supersession, in detail

Newest wins by default. But *never* delete, and never silently overwrite:

```markdown
## Hiring Threshold

Hire your first cleaner once you've turned away work three weeks running.

> [!failure]- Superseded — 2024-03-11
> Previously: "hire at $10k/mo revenue."
> Source: [[Video 41]]
> Replaced by: [[Coaching Call 88]], 2026-07-02
> Reason: revenue proved a bad trigger — it lags the actual constraint.
```

Rules for the block:

- Use a **collapsed** callout (`>[!failure]-`) so the page reads clean but the history
  is one click away.
- Always record **what it said, which source, what replaced it, and why.** A supersession
  without a reason is indistinguishable from a mistake six months later.
- Add `superseded:` to the page's frontmatter with the date.
- **Never edit the old source file.** The old video still exists and still says the old
  thing. That's fine — that's what supersession is for.

### The blast-radius audit — required on every Type 1

A superseded claim is usually already published. When you demote a claim, you must
report what's now teaching the old version.

Trace forward from the concept page:

1. Every page in `05 Products/` and `06 Marketing/` that links to this concept
2. Every entry in the concept's own "where this has been presented" list
3. Every SOP in `04 Systems/` referencing the old number or rule

Output a table:

| Asset | Where | Says | Severity |
|---|---|---|---|
| Course Lesson 17 | `05 Products/` | old threshold | **High — students act on it** |
| YouTube "First Hire" | `06 Marketing/` | old threshold | Medium — public, hard to edit |
| Welcome email 3 | `06 Marketing/` | old threshold | **High — still sending** |

Rank by whether someone is *currently acting on the wrong information*. A live email
sequence outranks an old video nobody watches.

Do not fix these automatically. Report, and offer `/draft` to regenerate each.

### Type 3 — Contested, in detail

```markdown
> [!warning] Contested
> **Claim A:** hire at three weeks of turned-away work — [[Coaching Call 88]]
> **Claim B:** hire only after documenting the job — [[Book: Traction]]
> **Unresolved since:** 2026-08-05
> **What would settle it:** track the next 10 students who hired each way.
```

Always include **what would settle it.** A contested callout without a resolution path
is just an argument you're storing forever. `/lint-vault` reports contested items older
than 60 days.

While a claim is contested, agents writing customer-facing copy must **use neither
side** without asking. Teaching a disputed claim as settled is how the vault damages
the business rather than helping it.

### What agents may never do

- Silently pick a winner and delete the loser
- Average two conflicting claims into a vague middle that neither source said
- Edit a source file to match the new claim
- Ingest past a Type 5 Canon conflict
- Supersede based on a source whose date you couldn't establish — undated material is
  Type 3 by default

---

## XI. Voice

Write like Alex talks. Short sentences. Concrete over abstract. Second person when
teaching. No corporate register, no hedging, no throat-clearing.

[[Alex Voice]] — in `Voice/`, **not** in `02 Canon/` — holds the anchors: real Alex
sentences. **Imitate those, not a description of them.** Check the Voice Log there for
rules extracted from past corrections.

The anchors are **spoken** samples. The 1:1 Coaching Agreement was retired as a voice
source on 2026-08-06: it is a legal contract, and drafting from it produces something far
more composed than Alex sounds. It remains a valid source for what it *says*.

[[Language]] holds naming rules. There is no forbidden-word list; Alex removed it. The
one hard rule: **"Harvest CRM" is always both words** — bare *Harvest* means the Season.

---

## XII. Amendment

This document is amended by Alex only. Any agent that believes a rule here is wrong
should say so in its response — not edit the file.
