---
type: concept
engine: [Leads, Logistics]
season: [Stability, Scale]
laws: [Build In Order]
status: Developing
sources: [Upload Leads & Contacts to Harvest CRM]
updated: 2026-08-06
---

# Importing Contacts Into Harvest CRM

> [!abstract] In one line
> Sort contacts by booking history before you import — dumping everyone into one workflow blasts recurring clients with promos and buries leads worth following up.

## Definition

The setup step for an already-established business moving into [[Harvest CRM]]: exporting
existing leads and clients from whatever platform they're currently on (BookingKoala,
Housecall Pro, Jobber, ScheduleDrop, ZenMaid, or similar), sorting them by booking history
into three groups — never booked, one-time, recurring — and importing each group into the
matching workflow or pipeline stage rather than one undifferentiated bulk upload.

This is a one-time migration decision, distinct from [[Reactivating Past Clients]], which
is the ongoing decision of what to *do* with a quiet database that's already living
correctly inside the CRM.

## Why It Matters

A single bulk import with no sorting puts recurring clients into the same automations as
cold leads — meaning a client who's been paying you monthly for a year gets a promotional
"come back!" text. It also buries the leads and one-time clients actually worth automated
follow-up inside a pile that gets treated uniformly. The lesson's framing: *"We've made it
so simple and they'll also go to automations to already start following up for you"* — but
only if the import is sorted first. An unsorted import produces the opposite of that
promise.

## Symptoms

- Recurring, paying clients receiving reactivation or promotional texts meant for cold leads
- Old leads and one-time clients sitting unworked because everything landed in one
  undifferentiated bucket
- A phone number at risk of being flagged as spam after a bulk import fires too many texts
  at once

## Common Mistakes

- Uploading all contacts together without sorting by booking history first
- Putting recurring clients into old-lead follow-up automations
- Forgetting to import one-time clients into a sequence that can win them back
- Not matching fields properly during import (email, phone, date booked)
- Waiting to complete [[A2P Verification]] until after the import instead of before —
  automated texts depend on it and denial delays can run about a week
- Assuming old leads are dead instead of routing them into long-term follow-up

## Models

**The three-way split, and where each group lands:**

| Group | Definition | Destination workflow | Gets texted? |
|---|---|---|---|
| Never booked | Old leads who never converted | Did-not-book workflow → long-term follow-up, tagged "database upload" | Yes, but delayed and dripped (see below) |
| One-time | Booked once or twice, not recurring | One-time-clean workflow → a 12-month follow-up sequence | Yes, tagged as booked for automation purposes |
| Recurring | Currently on a recurring schedule | Booked Recurring stage — see [[Sales Pipeline Stages]] | No — organized only, never texted or placed in a reactivation sequence |

**The import mechanics.** Export from the current platform into a sheet, sort by number of
bookings, split into the three groups above, save one file per group, then import each
separately: Harvest CRM → **Contacts tab → Import Contacts** → upload → match fields
(email, phone, date booked at minimum) → assign the correct workflow for that group → bulk
import → review the pipeline afterward to confirm contacts landed in the stage they should
have.

**Why texts don't fire immediately.** [[A2P Verification]] governs whether the account can
text at all, but even once approved, imported contacts aren't texted right away: Harvest
CRM holds for 14 days, then drips messages out slowly instead of all at once. This protects
the phone number from being flagged as spam and protects the team from a flood of replies
arriving simultaneously. Sequencing consequence: get A2P approval done *before* or
immediately alongside the import, not after — the lesson's own emphasis is "ASAP," since
approval itself can take about a week and the automations the import is supposed to trigger
are stalled until it clears.

## Checklist

- [ ] Export contacts from the current platform (BookingKoala, Housecall Pro, Jobber,
      ScheduleDrop, ZenMaid, etc.) into a sheet
- [ ] Sort by number of bookings
- [ ] Split into three groups: never booked / one-time / recurring
- [ ] Save one file per group
- [ ] Harvest CRM → Contacts → Import Contacts, one group at a time
- [ ] Match fields: email, phone, date booked (skip fields that don't matter)
- [ ] Assign the correct workflow per group — did-not-book / one-time-clean / booked
      recurring
- [ ] Confirm [[A2P Verification]] is complete or in progress before importing — don't
      wait until after
- [ ] After import, review the pipeline to confirm contacts landed in the right stage
- [ ] Expect texts to imported never-booked/one-time contacts to start after a 14-day
      delay, dripped — not immediately

## Templates

*None yet — no specific field-mapping screenshot or import-sheet template is documented.*

## Videos

- [[Upload Leads & Contacts to Harvest CRM]]

## Student Examples

*None yet.*

## AI Prompts

> When a student asks how to bring an existing customer list into Harvest CRM, the first
> question is whether they've sorted contacts by booking history yet — never booked,
> one-time, recurring. Don't let them import in one batch. Recurring clients getting a
> promotional win-back text is the most common and most damaging mistake this page exists
> to prevent.

## FAQ

**Q:** Will imported contacts get texted right away?
**A:** No. Even with A2P approved, Harvest CRM holds imported never-booked and one-time
contacts for 14 days, then drips the texts out slowly rather than blasting everyone at
once.

**Q:** Do recurring clients need to be imported at all if they're not going to be texted?
**A:** Yes — they still go into the Booked Recurring stage so the CRM has an accurate
picture of the business. They're organized, not automated.

## Conflict History

*None.*

## Presented In

*None yet.*

## Related Concepts

- [[Harvest CRM]]
- [[A2P Verification]]
- [[Reactivating Past Clients]]
- [[Sales Pipeline Stages]]
- [[BookingKoala]]
- [[Zapier]]
