---
type: canon
title: Constitution
status: Canonical
updated: 2026-08-06
---

# CONSTITUTION

The governing document of CleaningOS. Every agent — Claude, ChatGPT, or anything built later — reads this first and obeys it without exception.

> [!abstract] What this is CleaningOS is not documentation of a business. It is the business, in a form both humans and machines can operate. The course, the VSL, the YouTube channel, the CRM, the emails — all of them are _outputs_ rendered from this vault. The vault is the asset. Everything else is a presentation of it.

> [!info] Amended 2026-08-06 by Alex, executed by Claude on instruction Rewritten after the first large unattended ingest (8 courses, 135 lessons) exposed gaps. Changes: §II corrected and given the governing/descriptive test · §V gained rows for `08 Logs/` and the unnumbered files · §VI gained the filename-collision rule · §VII gained citation granularity · §VIII now routes through `03 Concepts/INDEX.md` · §IX gained the unsourced-claim rule. Nothing in §I, §III, §IV, §X or §XI changed in substance.

> [!info] Amended 2026-08-07 by Alex, executed by Claude on instruction — CleaningOS v2 refactor §II: the Canon drops from six documents to five. **Four Roles removed** and demoted to [[Owner Role Evolution]] in `03 Concepts/` — it assigned one Role per Season, which implies one Season per business and contradicts [[Four Seasons]]. First removal on grounds of correctness rather than filing. §II also now states the model in one line and requires Alex's approval before any second customer-facing business map exists. [[Four Seasons]] rewritten to describe **per-Engine maturity**; universal revenue, headcount and recurring-client bands removed as a category error. [[Business GPS]] corrected separately — the constraint is selected by the owner's goal, not by the lowest-Season Engine. Proposal and reasoning recorded in `00 Inbox/canon-proposals.md`. Further amendments land as the refactor proceeds.

---

## I. Mission

To help ordinary people build a real business that gives them ownership of their time.

A cleaning business can be more than a way to replace a paycheck. Built correctly, it can let someone leave a job they hate, be present with their family, travel, make art, serve their church or community, and choose what their days are for. It can also create dependable work and dignity for the people on the team.

Money matters because it creates options, but the final product is not money. **The final product is a person who no longer feels trapped.**

Full version — the enemy, the promise, what we believe — in [[Philosophy]].

---

## II. The Canon

**Five documents** hold the intellectual property. They are the constitution's body, and no page anywhere in the vault may contradict them.

- [[Five Laws]] — Stop Guessing · Clarity Creates Momentum · Build In Order · The Roadmap Already Exists · One Step Wins
- [[Four Engines]] — Leads · Labor · Logistics · Leadership
- [[Four Seasons]] — Survival · Stability · Scale · Harvest. **The maturity of one Engine.** Each Engine has its own; there is no business-level Season.
- [[Philosophy]] — what we believe, what we reject, how we teach
- [[Language]] — naming rules. "Harvest CRM" is always both words

**The model, in one line: Four Engines × Four Seasons, governed by the Five Laws.** Any second customer-facing map of the business is a competing model and needs Alex's explicit approval before it exists.

**Canon is edited by Alex only.** Agents may propose changes in `00 Inbox/canon-proposals.md`, but must never edit `02 Canon/` directly. Everything else in the vault flows downhill from these files; changing them silently changes everything. **There are no exceptions to this rule.**

### The test for what belongs in Canon

Applied twice, so it is written down rather than re-derived each time:

> **Is the file governing, or is it descriptive?**
> 
> **Governing** — it states what CleaningOS _believes_ or how it _classifies_. Changing it changes every page downstream. It belongs in `02 Canon/`, locked.
> 
> **Descriptive** — it _records_ something defined elsewhere. Appending to it cannot change what the vault teaches. It belongs outside Canon, with a write policy at the top of the file.

Two files have left Canon on this test:

|File|Now at|Why it isn't governing|
|---|---|---|
|[[Alex Voice]]|`Voice/`|Records how Alex already sounds. Also **portable** — voice belongs to the person, not the business, and should survive into any other vault Alex builds.|
|[[Glossary]]|vault root|An _index_. Every real definition lives on a concept page; a row is a pointer to one. Also had to move at the speed of ingestion, which the lock made impossible.|
|[[Owner Role Evolution]] — was *Four Roles*|`03 Concepts/`|**Removed for being wrong, not for being descriptive** — the first on those grounds. It assigned one Role per Season, which implies one Season per business, which contradicts [[Four Seasons]]. The progression survives as a Leadership concept about the _owner's_ job. Alex, 2026-08-07.|

Both were considered for a carve-out — keeping them in Canon with write access — and both times that was rejected: **an exception inside the lock teaches every future agent that the lock is negotiable**, which is the exact silent erosion this section exists to prevent. Moving the file out is honest; a hole in the rule is not.

A new candidate is decided by the same test, by Alex, and recorded in the table above.

---

## III. The Four Rules

### Rule 1 — Organize by concept, never by artifact

The unit of knowledge is an idea, not a file. A video is not knowledge; it's a container that knowledge arrived in. `Videos/Lesson 1.mp4` is wrong; `03 Concepts/Pricing.md` is right.

The video becomes a source. The idea inside it becomes a page. One video may feed fifteen pages; one page may draw on thirty videos. That many-to-many relationship is the entire point.

### Rule 2 — Nothing exists twice

There is exactly **one** page per concept. It is canonical. Everything else links to it.

Before creating any page, **read `03 Concepts/INDEX.md`** — every concept in one line each. That file exists so this rule can be obeyed cheaply; see §VIII. Creating a near-duplicate is the single most destructive thing an agent can do here, because it splits the graph invisibly and the damage compounds silently.

When genuinely unsure whether two ideas are one concept or two: **they are two.** Split now, merge later — `/lint-vault` surfaces merge candidates. An unnecessary split is visible and cheap to fix. A wrong merge destroys distinctions you can't recover.

### Rule 3 — Sources are immutable

Everything in `01 Sources/` is read-only, permanently. No edits, no reformatting, no "cleaning up," no deletions. Ever.

If a transcript is garbled or a source is wrong, note that on the concept page that cites it. The source stays as it is. It is the evidentiary record.

**The only permitted write to `01 Sources/` is adding a new file.** This is enforced at the tool layer in `.claude/settings.json`, which denies `Edit` while allowing `Write`.

### Rule 4 — The wiki is the product

Not notes about the product. The product.

Judge every page by this test: _could someone build this part of the business from this page alone?_ If not, the page isn't finished — it's a summary pretending to be knowledge.

---

## IV. Knowledge vs. Presentation

The most important distinction in this system.

|Knowledge|Presentation|
|---|---|
|`Hiring First Cleaner.md`|Course Lesson 17|
|Lives in `03 Concepts/`|Lives in `05 Products/`, `06 Marketing/`|
|One canonical page|Unlimited renderings|
|Changes when you learn something|Changes when the channel changes|

A YouTube video, a VSL, a lesson, an email, and a sales call answering an objection are five presentations of the same underlying knowledge. They are not five pieces of knowledge.

**Consequence for agents:** when asked to write a YouTube script, an email, or a lesson, you do **not** search transcripts. You read the canonical concept page — which already contains the philosophy, the student stories, the objections, the mistakes, the analogies — and render it into the requested format. Presentation pages record _what was shipped and where_; they never become the source of truth.

If you find yourself pulling a fact from a transcript that isn't on the concept page, that's a signal the concept page is incomplete. Update the concept page first, then write the script.

---

## V. Canonical Location Rule

The folders are a filing system, not a set of competing homes. Without a tiebreak, "Referrals" plausibly belongs in Concepts, Systems, and Marketing at once — and Rule 2 dies. So:

|Folder|Holds|Never holds|
|---|---|---|
|`00 Inbox/`|Unfiled arrivals, queues, proposals|Anything permanent|
|`01 Sources/`|The evidentiary record. Immutable|Anything written by an agent|
|`02 Canon/`|The IP. Laws, engines, seasons, roles, philosophy, language|Anything operational|
|`03 Concepts/`|**Every idea.** The default home. One page per idea|Workflows, deliverables|
|`04 Systems/`|Engine hubs, SOPs, workflows — _sequences of concepts_|New idea definitions|
|`05 Products/`|Things sold or shipped|Knowledge|
|`06 Marketing/`|Assets that promote|Knowledge|
|`07 Company/`|Internal ops, vision, meetings|Anything customer-facing|
|`08 Logs/`|Session records written by `/save`|Knowledge. **Never linked to from a concept**|
|`99 Scratchpad/`|Junk. Never linked to|Anything you'd miss|

**Unnumbered files sit outside this pipeline on purpose** — the numbers encode the CleaningOS flow and these aren't part of it:

|Path|What|Who writes|
|---|---|---|
|`CONSTITUTION.md`|This document|Alex (§XII)|
|`CLAUDE.md`|Agent entry point — where to start, which commands exist|Agents|
|`Glossary.md`|Term index|Agents, per the policy at the top of the file|
|`Voice/Alex Voice.md`|How Alex sounds|Agents, per the policy at the top of the file|

**The tiebreak, stated once:** if an item is an _idea_, it goes in `03 Concepts/`. If it is a _sequence, deliverable, or asset_, it lives in its own folder and **links to** the concepts it uses. A page in `04–07` that defines an idea instead of linking to one is a bug.

So: `Hiring Flow` (a workflow) lives in `04 Systems/` and links to `[[Hiring First Cleaner]]`, `[[Interview Process]]`, `[[Cleaner Retention]]` — each of which lives in `03 Concepts/` and is defined exactly once.

**`08 Logs/` is outside the knowledge hierarchy** the way `99 Scratchpad/` is, for the opposite reason: scratchpad is junk you'd never miss, logs are an audit trail you would. A log records _that_ something was learned and filed. If a log contains a fact worth keeping, that fact belongs on a concept page. Never cite a log as a source.

---

## VI. Naming Conventions

- **Title Case With Spaces.** `Hiring First Cleaner.md`, not `hiring-first-cleaner.md`. Wikilinks are read by humans; make them readable.
- **Use the form you'd say aloud.** `Referrals.md` is right if that's how you talk. Consistency beats grammar.
- **Name the idea, not the container.** `Pricing.md`, never `Pricing Notes.md`, `Pricing Overview.md`, or `Pricing v2.md`. Qualifier suffixes are how Rule 2 dies.
- **No dates or versions in filenames.** Git holds history.
- **Sources keep their original names** plus a source ID prefix where one exists (`Video 41 — Hiring Your First Cleaner.md`).

### No filename may exist twice

**A page in `03–07` may not share a filename with any file in `01 Sources/`.** Sources keep their names under Rule 3, so the concept page is the one that gets renamed.

This is Rule 2's failure mode in disguise. If `03 Concepts/Hiring SOP.md` and `01 Sources/.../Hiring SOP.md` both exist, every `[[Hiring SOP]]` in the vault is ambiguous and Obsidian resolves it silently — half your links may point at a raw transcript. The idea still has one page, but the _name_ has two targets, and the graph splits invisibly. `/lint-vault` checks for this.

### Two link mechanics that bite

- **Never let a wikilink wrap across a line break.** `[[Sales Pipeline\nStages]]` does not resolve, and the page still _reads_ as linked, so the failure is invisible. Repair with `.claude/scripts/fix_wrapped_links.py`.
- **`aliases:` in frontmatter are real links.** Obsidian resolves them. Any tool checking for broken links must parse aliases or it will report false positives.

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

- `status: Stub` means the page exists to be linked to but isn't written yet. Stubs are how the vault tells you what to build next — create them eagerly.
- `updated:` gets bumped on every touch.
- `superseded:` and `contested:` make conflict state queryable across the whole vault. Before writing any customer-facing copy, an agent checks `contested:` on every concept it draws from — see §X.
- `laws: []` is a valid state. Not every concept sits under a Law.

### `sources:` is not decoration

An empty `sources:` on a `Canonical` page means the page asserts things nothing backs up. `/lint-vault` flags these.

**Cite at the granularity of the claim.** A multi-lesson course is one file name pointing at dozens of files, which is fine for background and useless for anything challengeable:

|The claim is…|Cite|
|---|---|
|Background, or restates what the page already said|the course — `Labor 101`|
|A number, a script, a policy, a date, or anything contested|the lesson — `Labor 101 → Determining Cleaners' Pay`|

The test: **if Alex challenged this line, could you find the evidence in under a minute?** If not, you cited too coarsely.

### Presentation pages

Pages in `05`/`06` additionally carry:

```yaml
renders: [Hiring First Cleaner, Pricing]   # concepts this asset teaches
shipped: YYYY-MM-DD
channel: youtube | email | course | vsl | social
live: true | false                          # is it still being served to people?
```

`renders:` is what makes the blast-radius audit possible. Without it, a superseded claim can't be traced to the assets teaching it, and §X's audit degrades to guesswork. Any agent creating a presentation page must fill it.

---

## VIII. How Agents Think

Before writing anything, in this order:

1. **Read the Canon.** [[Philosophy]] and [[Language]] at minimum. Every output must sound like it came from the same mind.
2. **Read `03 Concepts/INDEX.md`.** Every concept and system, one line each, in one file. This is the duplication check — it catches near-synonyms a title search misses, and it is how Rule 2 gets obeyed without reading the whole vault. Open individual pages only once the index tells you which ones you need.
3. **Then search full text**, but only for ideas the index didn't settle.
4. **Decide: update or create.**

```
New content arrives
        │
        ├── Does a page for this idea already exist?
        │       │
        │      YES ──→ UPDATE it. Add the new evidence, new nuance,
        │               or flag the contradiction. Bump `updated:`.
        │               Add to `sources:`.
        │
        └──    NO  ──→ New idea, or a different presentation of one
                        that already exists?
                        │
                        ├── New idea ──→ CREATE in 03 Concepts/ from the template
                        │
                        └── New presentation ──→ Record in 05/06 and LINK
                                                  to the existing concept
```

### The confidence test

Before calling two things the same concept: **would this page's `In one line` and the new idea both be true about the same decision an Owner makes?**

- Same decision → same concept. Update.
- Different decisions → two concepts. Create.
- Can't tell → **create separately and flag a merge proposal** in `00 Inbox/review-queue.md`. Per Rule 2, an unnecessary split is cheap; a wrong merge destroys a distinction you can't recover.

5. **Propagate.** A single ingestion should touch 5–15 pages: the concept pages it updates, the stubs it spawns, the engine hub in `04 Systems/`, the [[Glossary]].
6. **Link.** Every page ends with Related Concepts. Minimum five links. A page with fewer hasn't been thought about hard enough.
7. **Regenerate the index.** `python3 .claude/scripts/build_index.py .` after any change to `03 Concepts/` or `04 Systems/`. A stale index means the next agent enforces Rule 2 against an out-of-date map.

> [!warning] When agents run in parallel Isolated agents cannot see each other's work. `INDEX.md` is the only memory they share, so ingestion is **serialized** — one source at a time, index regenerated between each. Two agents running concurrently will both read the same index, both find no page for an idea, and both create one. That is Rule 2's unrecoverable error, produced at machine speed.

---

## IX. How Agents Update

- **Never delete a source.** Ever. See Rule 3.
- **Never delete a concept page** without fixing every wikilink pointing at it.
- **Never edit `02 Canon/`.** Propose changes in `00 Inbox/canon-proposals.md`.
- **Never invent** a quotation, statistic, student name, or result. If it isn't in a source, it doesn't go in the vault. A fabricated student win in a concept page will eventually be read aloud on a sales call.
- **A claim you can't trace is a defect, not a detail.** If an existing page asserts a figure no source supports, flag it on the page and record it under _Unsourced claims_ in `00 Inbox/review-queue.md`. Don't delete it — it may come from material not yet ingested — and don't repeat it in customer-facing copy until it's sourced.
- **Never smooth over a contradiction.** If two sources disagree, both go on the page under `> [!warning] Contested`. Contradictions are information.
- **Always report** every file touched, grouped by created / updated, one line each on why.

---

## X. Contradiction Protocol

When new material conflicts with what the vault already says, agents must first **classify the conflict**. "Contradiction" covers five different situations and they are handled differently. Getting this wrong either buries a real change or freezes the vault in warnings nobody reads.

### The five types

|Type|Looks like|Handling|
|---|---|---|
|**1. Supersession**|Same claim, different answer, newer source|**Newest wins.** Demote the old claim to a `Superseded` block. Run the blast-radius audit.|
|**2. Season-scoped**|"Do X" vs. "don't do X"|**Not a contradiction.** Split the claim by season on the page.|
|**3. Genuine dispute**|Outside source vs. our experience, unresolved|**Contested.** Both stay. Neither wins until Alex rules.|
|**4. Bad data**|A source misremembers a number or event|**Note and discard.** Record on the page that the source is unreliable here. Never edit the source.|
|**5. Canon conflict**|New material violates a Law, Season, Role, or Philosophy|**STOP.** Do not write. Escalate to Alex.|

### Classification rules

Work through these in order:

1. **Does it contradict `02 Canon/`?** → Type 5. Halt immediately. Write the conflict to `00 Inbox/canon-proposals.md`, report it, and **do not ingest the rest of that source** until Alex rules. Either he misspoke, or his thinking moved and a Law needs amending. Both outcomes need a human. Other sources in the queue are unaffected.
    
2. **Do the two claims apply to different seasons or engines?** → Type 2. Not a conflict. Restructure the page so the claim is scoped: _"In Survival, do X. By [later season], do Y instead."_ Most apparent contradictions in this vault will be this. Check for it before anything else.
    
3. **Is one claim demonstrably an error** — a misremembered number, a garbled transcript, a student misstating what they were told? → Type 4. Add a line to the page's Examples section noting the source is unreliable on this point. The source file stays untouched forever.
    
4. **Are both claims Alex's, at different times?** → Type 1. Supersession. Newest wins.
    
5. **Is it Alex vs. an outside source, or two of Alex's claims where the newer one looks like a mistake rather than a change of mind?** → Type 3. Contested.
    

If you cannot confidently classify, default to **Type 3 (Contested)** and say so. Contested is recoverable; a wrong supersession quietly deletes a belief.

### Type 1 — Supersession, in detail

Newest wins by default. But _never_ delete, and never silently overwrite:

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

- Use a **collapsed** callout (`>[!failure]-`) so the page reads clean but the history is one click away.
- Always record **what it said, which source, what replaced it, and why.** A supersession without a reason is indistinguishable from a mistake six months later.
- Add `superseded:` to the page's frontmatter with the date.
- **Never edit the old source file.** The old video still exists and still says the old thing. That's fine — that's what supersession is for.

### The blast-radius audit — required on every Type 1

A superseded claim is usually already published. When you demote a claim, you must report what's now teaching the old version. Trace forward from the concept page:

1. Every page in `05 Products/` and `06 Marketing/` that links to this concept
2. Every entry in the concept's own "where this has been presented" list
3. Every SOP in `04 Systems/` referencing the old number or rule

Output a table ranked by whether someone is _currently acting on the wrong information_. A live email sequence outranks an old video nobody watches.

|Asset|Where|Says|Severity|
|---|---|---|---|
|Course Lesson 17|`05 Products/`|old threshold|**High — students act on it**|
|Welcome email 3|`06 Marketing/`|old threshold|**High — still sending**|
|YouTube "First Hire"|`06 Marketing/`|old threshold|Medium — public, hard to edit|

Do not fix these automatically. Report, and offer `/draft` to regenerate each.

### Type 3 — Contested, in detail

```markdown
> [!warning] Contested
> **Claim A:** hire at three weeks of turned-away work — [[Coaching Call 88]]
> **Claim B:** hire only after documenting the job — [[Book: Traction]]
> **Unresolved since:** 2026-08-05
> **What would settle it:** track the next 10 students who hired each way.
```

Always include **what would settle it.** A contested callout without a resolution path is just an argument you're storing forever. `/lint-vault` reports contested items older than 60 days.

While a claim is contested, agents writing customer-facing copy must **use neither side** without asking. Teaching a disputed claim as settled is how the vault damages the business rather than helping it.

### What agents may never do

- Silently pick a winner and delete the loser
- Average two conflicting claims into a vague middle that neither source said
- Edit a source file to match the new claim
- Ingest past a Type 5 Canon conflict
- Supersede based on a source whose date you couldn't establish — undated material is Type 3 by default

---

## XI. Voice

Write like Alex talks. Short sentences. Concrete over abstract. Second person when teaching. No corporate register, no hedging, no throat-clearing.

[[Alex Voice]] — in `Voice/`, **not** in `02 Canon/`, per §II — holds the anchors: real Alex sentences. **Imitate those, not a description of them.** Check the Voice Log there for rules extracted from past corrections.

The anchors are **spoken** samples. The 1:1 Coaching Agreement was retired as a voice source on 2026-08-06: it is a legal contract, and drafting from it produces something far more composed than Alex sounds. It remains a valid source for what it _says_. Apply the same treatment to any legal document — content, never voice.

[[Language]] holds naming rules. There is no forbidden-word list; Alex removed it. The one hard rule: **"Harvest CRM" is always both words** — bare _Harvest_ means the Season.

---

## XII. Amendment

This document is amended by Alex only. Any agent that believes a rule here is wrong should say so in its response — not edit the file.

When Alex directs a rewrite, the agent executes it and records the amendment in the note at the top, listing what changed. An amendment nobody can see is indistinguishable from drift.