---
type: system
engine: [Logistics]
season: [Survival, Stability]
laws: [Build In Order]
status: Canonical
sources: [2025-03-11 Weekly Coaching Call, Get Phone Number + A2P Approval]
updated: 2026-08-07
---

# A2P Verification

> [!abstract] In one line
> The compliance step that lets the business text clients from the CRM instead of your personal phone.

## Definition

Application-to-Person messaging registration. Carriers require it before a business can
send SMS through a platform like [[Harvest CRM]]. You register a campaign describing what
you'll send and how people consented; carriers approve or deny it.

Two things have to happen, in order: **buy a local number**, then **get the campaign
approved**. The number is bought inside Harvest CRM under **Settings → Phone System**.
On done-for-you setup, both are handled on the first onboarding call.

## Why It Matters

Until it's done, client texting happens from the owner's personal phone — which means it
isn't logged, isn't visible to a VA, can't be automated, and leaves with the owner.

> "Now you have a real system."

It's a precondition for [[Reactivating Past Clients]] and for handing client communication
to anyone else. It also gates [[Scheduling Cleans]] confirmations and on-the-way notices —
the texts clients actually judge you on.

## Symptoms

- Client conversations living in your personal messages
- A VA who can't see or answer client texts
- Follow-up automations that don't send
- Repeated A2P denials with no clear reason given

## Common Mistakes

- Deferring it as paperwork — it blocks the whole Logistics Engine
- Not budgeting time for approval
- Writing vague campaign language instead of describing the real cleaning-business use case
- Omitting HELP and STOP language from the sample messages
- Submitting a lead form where the SMS checkbox isn't **required**
- Using shortened or hyperlinked policy URLs instead of full naked URLs
- A screenshot that doesn't clearly show the consent checkbox
- Submitting with `YOUR BUSINESS NAME`, `YOUR WEBSITE`, or the policy placeholders still in the text

## Models

**Why denials happen.** Carriers are checking one thing: can you prove these people agreed
to be texted, and does what you say you'll send match what you'll actually send? Every rule
below is downstream of that. Vague language reads as a spam campaign hiding its purpose.

**The order that works:**

```
Buy local number (Settings → Phone System)
        ↓
Build the Facebook Lead Form with a REQUIRED opt-in checkbox   → [[SMS Opt-In Consent]]
        ↓
Screenshot the checkbox as a user sees it
        ↓
Submit A2P campaign — Low Volume Mixed — with matching language
```

The screenshot comes from the live lead form, not a mockup. This sequence is described in
the source as **the best way found to reliably get verified.**

## Checklist

- [ ] Harvest CRM → **Settings → Phone System** → buy a local number
- [ ] Build the Facebook Lead Form with a required SMS opt-in checkbox — see [[SMS Opt-In Consent]]
- [ ] Screenshot the consent checkbox as it appears to users
- [ ] Start the A2P campaign approval process
- [ ] Campaign use case: **Low Volume Mixed**
- [ ] Paste the use case description below, replacing the business name
- [ ] Additional message details: Embedded Links **Yes**, Embedded Phone **Yes**, Age Gated **No**, Financial Services **No**
- [ ] Paste the sample messages, replacing business name and website
- [ ] Confirm every placeholder is replaced before submitting
- [ ] Submit

## Templates

**Campaign use case:** Low Volume Mixed

**Use case description:**

> Sending booking confirmations, on-the-way arrival notices, service reminders, and
> occasional promotional offers to residential house-cleaning customers of YOUR BUSINESS
> NAME who opt-in through a Facebook Lead Form with a required SMS opt-in checkbox.

**Sample messages** — submit all five; they cover confirmation, operations, lead follow-up,
booking, and promotion, which is what "Mixed" means:

> BUSINESS NAME: Your house cleaning is confirmed for the scheduled date & time. Reply HELP for help or STOP to opt out.
>
> BUSINESS NAME: Your cleaner is on the way and should arrive within 30 minutes. Reply HELP for help or STOP to opt out.
>
> BUSINESS NAME: We received your inquiry from Facebook, how can we assist with your cleaning needs?
>
> BUSINESS NAME: View our availability and book a cleaning at YOUR WEBSITE. Reply STOP to opt out.
>
> BUSINESS NAME: Get $40 off of a first-time home cleaning when you book this week. Max 4 msgs/month. Reply HELP for help, or STOP to opt out.

**Opt-in confirmation message:**

> You have successfully opted-in to received notification and promotional SMS from YOUR
> BUSINESS. Reply STOP if you need to opt out in the future.

Checkbox copy lives on [[SMS Opt-In Consent]].

> [!warning] Two things to fix before this is taught
> 1. The opt-in confirmation message reads *"opted-in to received notification"* — a typo
>    carried from the source. It goes out to every client who opts in. Should be *"to
>    receive notifications and promotional SMS."*
> 2. The source's checkbox copy has a real business name, **My Personal Cleaners**, left in
>    where a placeholder belongs. A student copying it verbatim submits another company's
>    name to the carrier. Corrected on [[SMS Opt-In Consent]].
>
> Both are source defects, not vault errors — the source stays as it is per Rule 3.

## Videos

- [[2025-03-11 Weekly Coaching Call]]
- [[Get Phone Number + A2P Approval]] — the course lesson. DIY path, exact submission language.

## Student Examples

**Rick and Jack** — both verified around 2025-03-11. Both moved client texting off personal
phones onto laptops via the CRM. Rick's approval took time and required chasing; Jack
completed it in Canada.

## AI Prompts

> A student is getting denied on A2P. Ask which of these is true before suggesting
> anything: (1) is the SMS checkbox on their lead form *required*, or optional? (2) does
> their screenshot show the checkbox as a user sees it? (3) are the ToS and Privacy Policy
> links full naked URLs in the checkbox text? (4) do the sample messages include HELP and
> STOP? Most denials are one of these four, not the campaign description.

## FAQ

**Q:** Do I need this if I only text a handful of clients?
**A:** Yes. A2P governs business-to-person messaging through a platform, not volume. Low
Volume Mixed is the campaign type *for* small senders.

**Q:** Can I skip it and just text from my phone?
**A:** You can, and it costs you the whole point — see Why It Matters. Nothing is logged,
nothing automates, and the relationships stay yours instead of the business's.

**Q:** What if my leads don't come from Facebook?
**A:** The consent requirement is the same; the form changes. Describe the actual opt-in
path in the use case description and screenshot that form instead. Carriers care that
consent is provable, not where it happened.

## Conflict History

*None.*

## Presented In

- Course: *What is Harvest CRM* → module *Get Phone Number + A2P Approval*

## Related Concepts

- [[SMS Opt-In Consent]]
- [[Harvest CRM]]
- [[Logistics Engine]]
- [[Reactivating Past Clients]]
- [[IVR Setup]]
- [[Managing A VA]]
- [[Scheduling Cleans]]
- [[Importing Contacts Into Harvest CRM]]
