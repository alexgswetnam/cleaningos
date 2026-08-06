---
type: concept
engine: [Logistics]
season: [Stability, Scale]
laws: [Build In Order, One Step Wins]
status: Developing
sources: [Zapier The Software Glue, 2026-03-18 Weekly Coaching Call, 2026-04-01 Weekly Coaching Call, Cleaning Biz 101 — Operate]
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

**The lead-capture zap, in the mechanism actually running (2026-03-18 call).** Website
form submission → email → Zapier scans for that email every two minutes → a JavaScript
step parses the email body → creates the contact in [[Harvest CRM]] + fires a Discord
notification. It's an email-parsing workaround, not a native form integration — the
simpler alternative (embed a Harvest CRM form directly on the site and skip the email
step) is known but not yet adopted. See [[Conversion Tracking]] for how UTM data rides
along through the same pipeline.

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

## Templates

*None yet.* The three zaps above are described, not built — no screenshots, field mappings,
or trigger configuration in the source.

## Videos

- [[Zapier The Software Glue]]
- [[2026-03-18 Weekly Coaching Call]] — the live lead-capture email-parsing mechanism.
- [[2026-04-01 Weekly Coaching Call]] — Rick's tag-triggered webhook optimization.

## Student Examples

**Rick, 2026-04-01** — narrowed a lead-sheet automation to an "update contact" tag
trigger, cutting monthly zap volume from ~1,500 to ~200.

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

## Related Concepts

- [[Harvest CRM]]
- [[BookingKoala]]
- [[SOPs]]
- [[Logistics Engine]]
- [[Business GPS]]
- [[Scheduling Cleans]]
- [[Managing A VA]]
