---
type: concept
engine: [Leads, Labor]
season: [Stability, Scale]
laws: []
status: Developing
sources: [2026-03-04 Weekly Coaching Call, 2026-04-08 Weekly Coaching Call, 2026-04-20 Weekly Coaching Call, Cleaning Biz 101 — Convert]
updated: 2026-08-06
---

# Harvest CRM

> [!abstract] In one line
> The CRM (lead follow-up, hiring pipeline, workflow automation) — not [[BookingKoala]], which is the booking calendar.

## Definition

The CRM used for lead follow-up, automated win-back workflows, and the hiring pipeline.
Distinct from [[BookingKoala]], the booking and scheduling software: Harvest CRM is where
leads and applicants move through stages and get automated follow-up; BookingKoala is
where cleans actually get scheduled onto a calendar. Always both words — bare "Harvest"
means the Season, never this tool.

## Why It Matters

Answers the question [[BookingKoala]]'s own FAQ leaves open: why pay for two tools?
Because they solve different problems. BookingKoala solves "when is this cleaner
available and when is this clean happening." Harvest CRM solves "who is this lead/
applicant, what stage are they at, and did anyone follow up." A business can run
BookingKoala without Harvest CRM at low volume, but once leads or applicants arrive
faster than they can be tracked by memory, follow-up starts silently failing —
that's the trigger to adopt it.

## Symptoms

- Losing track of who reached out, who was followed up with, who never got a response
- Leads or applicants going cold because no one remembered to follow up
- Running lead tracking off memory or a spreadsheet once marketing is turned on

## Common Mistakes

- Buying a $500–$1,000/month CRM before there's lead volume to justify it
- Treating [[BookingKoala]] and Harvest CRM as redundant rather than complementary
- Trying to run the CRM primarily from the mobile app — it's built for messaging and
  notifications only, not day-to-day workflow management
- Building a new form (e.g. for hiring) without connecting it to the pipeline automation —
  the automation silently doesn't fire for that form's submissions
- Sending from Harvest's native email address instead of your actual business email —
  Harvest's native sender is more likely to land in spam
- Leaving the business email's DNS records unconfigured inside Harvest CRM — same
  underlying spam-deliverability problem, fixed once during setup rather than per-email

## Models

**When to get a CRM.** Not at the very beginning. The trigger is lead volume outpacing
manual tracking: *"Once you turn on marketing and you're losing money by not properly
following up with all these people — that's when."* Before that stage, a lighter tool
(e.g. ZenMaid's automated reminder texts) solves the immediate pain without the cost.

**The hiring pipeline lives inside it.** [[Automated Hiring Pipeline]] — originally
Rashawn's custom build — is now templatized into every member's Harvest CRM account:
application → schedule interview → interviewed → good candidate (collect ID, W-9,
insurance, background check, subcontractor agreement) → onboarded (cleaner handbook), or
automated rejection for a bad candidate.

**Follow-up workflows are customizable — and the default ones have gaps.** Rick found
that the default 60-day win-back email only triggered for one-time cleans, not recurring
clients who stopped booking. He built a separate VIP follow-up workflow specifically for
lapsed recurring clients — see [[Reactivating Past Clients]] for the full mechanism.

**What "the CRM does the heavy lifting" actually means, itemized.** `Cleaning Biz 101 —
Convert` names the specific list: auto-texting new leads instantly, a missed-call text,
follow-up sequences, reminders for the calls that still need a human, moving pipeline
stages automatically when a booking happens, and tagging lead sources automatically. Its
line on why this matters: *"If you don't have a follow-up machine, you don't really have
a sales system!! You have a 'respond when I remember' system."* See [[Sales Pipeline
Stages]] for the full stage-by-stage breakdown this list maps onto.

**Desktop-first, not mobile-first.** The mobile app is for messaging and notifications
only. Booking, scheduling, and CRM workflow management should happen on a laptop — several
members run a VA setup with the CRM open alongside a [[BookingKoala]] tab, a Thumbtack
tab, Notion for task boards, and Discord for cleaner communication.

## Checklist

- [ ] Don't adopt a CRM until lead/applicant volume outpaces manual tracking
- [ ] When adding a new form, confirm it's actually wired to the pipeline automation
- [ ] Send applicant/client emails from your real business email, not Harvest's native
      sender, to avoid spam filtering
- [ ] Use the templatized hiring pipeline rather than rebuilding it from scratch
- [ ] Check default win-back workflows cover recurring clients, not just one-time —
      customize if they don't (see [[Reactivating Past Clients]])
- [ ] Run day-to-day CRM work from a laptop; treat mobile as messaging/notifications only

## Templates

*None yet — specific workflow-builder steps aren't documented.*

## Videos

[[2026-03-04 Weekly Coaching Call]] — hiring pipeline templatization, Rick's VIP
customization, when-to-get-a-CRM guidance

## Student Examples

**Rashawn** — original builder of the hiring pipeline now templatized for everyone.

**Rick** — built a VIP lapsed-recurring follow-up workflow on top of the CRM's default
one-time win-back sequence, tracking last booking date via a Zapier webhook.

**Nicole** — at a stage where ZenMaid's automated reminders solve the immediate
follow-up pain, not yet at CRM-adoption volume.

## AI Prompts

*None yet.*

## FAQ

**Q:** Why both BookingKoala and Harvest CRM?
**A:** They're not redundant. BookingKoala schedules cleans against cleaner availability.
Harvest CRM tracks leads and applicants through stages and automates follow-up so nothing
goes cold. A cleaner also gets a BookingKoala provider account during onboarding, which
is a downstream step of the Harvest CRM hiring pipeline, not a substitute for it.

## Conflict History

*None.*

## Presented In

*None yet.*

## Related Concepts

- [[BookingKoala]]
- [[Automated Hiring Pipeline]]
- [[Reactivating Past Clients]]
- [[Cleaner Availability System]]
- [[Zapier]]
- [[Leads Engine]]
