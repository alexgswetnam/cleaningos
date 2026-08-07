---
type: concept
engine: [Logistics]
season: [Stability, Scale]
laws: [Build In Order, One Step Wins]
status: Developing
sources: [Zapier The Software Glue, 2026-03-18 Weekly Coaching Call, 2026-04-01 Weekly Coaching Call, Cleaning Biz 101 — Operate, Use Zapier to Connect BookingKoala & Website, Weekly Sales Training Call — Harvest CRM, BookingKoala & Zapier Integration]
updated: 2026-08-06
---

# Zapier

> [!abstract] In one line
> Not a system — the glue between systems. Automate the handoffs that keep breaking, and nothing else.

## Definition

A tool that connects software that doesn't talk to each other. A "zap" is one rule: when
*this* happens in tool A, do *that* in tool B.

> "Zapier is not a 'system.' It's the glue between systems."

> "Every business without a developer (or even with a developer) uses Zapier as their glue
> when multiple softwares have to communicate."

## Why It Matters

A cleaning business ends up running several tools that were never designed to know about
each other — [[Harvest CRM]] for pipeline and messaging, BookingKoala for booking and
provider accounts, Discord for team notification, a lead form somewhere else. The gaps
between them are where work gets dropped: a booking that never reaches the pipeline, a
lead that sits unworked, a Friday schedule text nobody remembers to send.

Every one of those gaps currently has a human standing in it, remembering. That human is
usually the owner, and remembering is the least reliable thing they do.

## The Restraint Rule

The most important line in the lesson is the limit, not the capability:

> "The goal is not to build a thousand zaps!! You just remove the few manual steps that
> create the most errors or that you often forget, and let the glue make everything run
> smooth."

Two qualifying tests, and a step has to pass one:

1. **It creates the most errors** — the handoff that goes wrong repeatedly
2. **You often forget it** — the recurring task that depends on memory

A manual step that's reliable and remembered does not need a zap. Automating it adds a
thing that can silently break, and a thing you now have to maintain.

This is [[SOPs|the SOP timing rule]] applied to automation: document — or automate — after
the problem shows itself, not in advance.

## Symptoms

- A booking exists in one tool and not the other
- Someone finds out about a new lead by accident
- The Friday schedule text gets sent late, or not at all
- You are the integration between two pieces of software

## Common Mistakes

- **Building zaps before you have the failures that justify them.** The wrong-Engine
  mistake in miniature — see [[Business GPS]].
- Automating a step that already works reliably
- Chaining so many zaps that a failure is untraceable
- Treating Zapier as the system rather than the connective tissue. The system is the
  Engine; Zapier just stops it leaking at the seams.
- Building a frequency-based path filter (e.g. "one time" vs. recurring) that doesn't
  exactly match the booking software's actual wording and capitalization — the booking
  silently lands in the wrong pipeline stage instead of erroring
- Trying to build the New Booking zap's paths without the paid Zapier plan they require

## Models

**The three zaps named in the lesson.** Note what they have in common: each one closes a
gap *between* tools, and each one covers a step a human would otherwise have to remember.

| Trigger | Action | Gap it closes |
|---|---|---|
| New lead form submitted | Create lead in [[Harvest CRM]] | Lead capture → CRM |
| New booking in BookingKoala | Update [[Harvest CRM]] pipeline + send Discord notification | Booking → pipeline, and → team awareness |
| Every Friday | Text cleaners to update next week's schedule | Recurring task → memory |
| Daily | Pull BookingKoala + [[Harvest CRM]] numbers into [[Internal Communication Via Discord|the team's Discord]] | Owner/VA having to manually check two tools to see today's leads, cleans, and bookings |

The third is the odd one out and worth noticing: it isn't connecting two tools at all. It's
a scheduled action replacing a thing the owner kept forgetting. That's the "often forget"
test doing its job.

**The BookingKoala setup, built out at field level.** The onboarding lesson for connecting
BookingKoala (or Jobber, Housecall Pro, or another scheduling platform) to [[Harvest CRM]]
names the same first two zaps from the table above, but as an actual build, not just a
principle:

| Zap | Trigger | Action | Pipeline stage |
|---|---|---|---|
| New Quote | BookingKoala → New Quote | **LeadConnector** (Harvest CRM's Zapier connector) — map first name, last name, full name, phone, email, mark as lead, plus notes: booking date, service category, frequency, pricing parameters, square footage, extras, adjusted price, special notes | Quoted |
| New Booking | BookingKoala → New Booking | Split into **paths** by frequency: contains "one time" → one path; anything else → the other | Booked One-Time / Booked Recurring |
| Website Lead | Website form submission or its notification email (only needed if leads don't already arrive through BookingKoala's native form) | Extract contact info, create contact + opportunity in Harvest CRM | New Lead |

These three pipeline stages — Quoted, Booked One-Time / Booked Recurring, New Lead — are
the same stages defined on [[Sales Pipeline Stages]]; this lesson is the mechanical
how-to for getting BookingKoala data into them, not a second definition of the stages.

**Two build-level gotchas, worth carrying into any zap using paths:**

- **The frequency string has to match exactly.** The "contains 'one time'" filter is a
  literal text match against whatever the booking software actually outputs — wrong
  capitalization or wording silently sends bookings down the wrong path.
- **Paths require Zapier's paid plan (~$30/month).** Not optional if the New Booking zap
  needs to split one-time from recurring — budget for it rather than trying to route
  around it.

> "Zapier is the middle point that everyone can come to. Booking Koala can connect there,
> Harvest CRM can connect there, Google Sheets can connect there, Discord can connect
> there, Twilio, Gmail, everything can connect there."

> "Unfortunately, most softwares do not play nice and don't allow their API to be open."
> — the reason Zapier exists at all, stated plainly.

The website-lead zap for a WordPress site described in this lesson is the same
email-parsing pattern documented above from the 2026-03-18 call (form → email → Zapier
scans for it → JavaScript step extracts the fields) — not a second mechanism, the general
case of the same workaround, generalized beyond the one lead-form example already on this
page.

**The lead-capture zap, in the mechanism actually running (2026-03-18 call).** Website
form submission → email → Zapier scans for that email every two minutes → a JavaScript
step parses the email body → creates the contact in [[Harvest CRM]] + fires a Discord
notification. It's an email-parsing workaround, not a native form integration — the
simpler alternative (embed a Harvest CRM form directly on the site and skip the email
step) is known but not yet adopted. See [[Conversion Tracking]] for how UTM data rides
along through the same pipeline.

**A live build, from zero, corroborating the same three-zap shape.** A separate call walks
through Courtney building this from scratch — first Zapier account, Wix site, brand-new
BookingKoala and Harvest CRM. Worth noting because it confirms the pattern generalizes
past the one BookingKoala-specific lesson it was first documented from:

- **Each website form gets its own Zap**, not one shared trigger — Courtney's Wix site has
  a pop-up quote form and a separate contact form, wired as two Zaps, each tagging its own
  source label (*"Wix pop-up"* vs. *"Wix contact form"*) so the lead's origin survives
  into [[Sales Pipeline Stages]] and [[Conversion Tracking]].
- **The BookingKoala quote (not just the booking) has its own zap and its own pipeline
  destination.** Saving a lead as a *quote* in BookingKoala (rather than a booking) moves
  the contact to the "Quoted" stage automatically — this is the live version of the New
  Quote zap already documented in the field-level table above, now demonstrated end to end
  on a call rather than described as a setup step.
- **Test every zap by submitting the form yourself** before trusting it — done live on
  both Wix forms in this build.

**The BookingKoala quote feature, mechanically, is what makes the New Quote zap fire.**
On a call where the lead doesn't book, save their info as a **draft** (no email on file)
or a **quote** (email on file). Saving as a quote prompts BookingKoala to ask whether to
email it to the client — say yes, and the client gets a full quote they can open and pay
from later without calling back. That email-and-self-checkout mechanic is the reason the
"Quoted" pipeline stage exists as a *higher-priority* follow-up stage rather than a dead
end: Alex's team has had two to three people book days later off an emailed quote with no
follow-up call in between. See [[Handling I'm Shopping Around]] for the sales-side version
of the same move — getting the email to re-enter the conversation.

**A tag-triggered webhook beats a broad automation (2026-04-01 call).** Rick automated his
lead sheet updates — reflecting status changes like new lead, quote sent, booked, no
booking, canceled — with a webhook that only fires on an "update contact" tag, rather than
a broader automation reacting to every field change. That single change cut his monthly
zap volume from roughly 1,500 to 200, and cost with it. The lesson generalizes: a
narrowly-scoped trigger is worth checking for before assuming a workflow needs the volume
of zaps it's currently running.

## Checklist

- [ ] List the manual handoffs you actually perform each week
- [ ] Mark the ones that have gone wrong more than twice
- [ ] Mark the ones you've forgotten more than twice
- [ ] Build zaps only for what got marked
- [ ] Confirm each zap fired correctly for a full week before building the next
- [ ] Write down what breaks if the zap fails silently
- [ ] If a zap's volume looks high, check whether a narrower trigger (e.g. a specific tag)
      would fire it less often for the same result
- [ ] When wiring BookingKoala → Harvest CRM: build the New Quote zap (→ Quoted stage)
      and the New Booking zap with paths (→ Booked One-Time / Booked Recurring)
- [ ] Confirm the frequency path filter matches the booking software's exact wording and
      capitalization
- [ ] Sign up for Zapier's paid plan if paths are needed — there's no workaround
- [ ] Build a website-lead zap only if leads aren't already arriving through the booking
      platform's native lead form
- [ ] Test every zap after building it: a quote, a one-time booking, a recurring booking,
      and a website lead

## Templates

*None yet — no screenshots or exportable zap configuration.* The BookingKoala setup above
gives trigger/action/field-mapping detail for the New Quote, New Booking, and Website Lead
zaps; the other three zaps in the first table are still described only at the
trigger-and-action level.

## Videos

- [[Zapier The Software Glue]]
- [[2026-03-18 Weekly Coaching Call]] — the live lead-capture email-parsing mechanism.
- [[2026-04-01 Weekly Coaching Call]] — Rick's tag-triggered webhook optimization.
- [[Use Zapier to Connect BookingKoala & Website]] — the field-level build for the New
  Quote, New Booking (paths), and Website Lead zaps.
- [[Weekly Sales Training Call — Harvest CRM, BookingKoala & Zapier Integration]] — the
  same build, live and from zero, plus the BookingKoala draft/quote mechanic and why the
  "Quoted" stage matters.

## Student Examples

**Rick, 2026-04-01** — narrowed a lead-sheet automation to an "update contact" tag
trigger, cutting monthly zap volume from ~1,500 to ~200.

**Courtney** — built her Wix-to-Harvest CRM and BookingKoala-to-Harvest CRM integrations
live, from a brand-new Zapier account, with Alex walking through it in real time. Both
Wix forms tested and confirmed working the same call.

*None yet.*

## AI Prompts

> When a student asks what to automate, do not answer with a list of possible zaps. Ask
> which manual steps have actually broken or been forgotten, and build only from that list.
> The lesson's own instruction is that the goal is not a thousand zaps.

## FAQ

**Q:** Do I need Zapier in Survival?
**A:** Almost certainly not. In Survival you don't yet have enough tools or enough volume
for the gaps between them to be your constraint. See [[Business GPS]].

**Q:** Isn't this what [[Harvest CRM]] does?
**A:** Harvest CRM automates inside itself. Zapier is for when something outside Harvest CRM
has to reach in, or vice versa.

**Q:** What's LeadConnector?
**A:** The name of Harvest CRM's own connector inside Zapier — select it as the action app
whenever a zap needs to create or update something in Harvest CRM (a contact, an
opportunity, a pipeline stage).

## Conflict History

> [!warning] Source reliability — not a contradiction
> The lesson summary lists "Key Principles" (*speed-to-lead wins deals, systems beat memory
> and motivation, sales happens on the phone, tracking determines what to scale, CRM is the
> center of operations*) and a "Common Mistakes" list that do **not** appear in the lesson
> body. They are cleaning biz 101 course-level boilerplate inserted by the summariser.
>
> They are not wrong — most map to concepts already in the vault — but they must not be
> cited to this lesson. Nothing on this page is drawn from them.

## Presented In

- Course: *cleaning biz 101* → module *Zapier The Software Glue*
- Course: *What is Harvest CRM* → module *Use Zapier to Connect BookingKoala & Website*

## Related Concepts

- [[Harvest CRM]]
- [[BookingKoala]]
- [[SOPs]]
- [[Logistics Engine]]
- [[Business GPS]]
- [[Scheduling Cleans]]
- [[Managing A VA]]
- [[Sales Pipeline Stages]]
