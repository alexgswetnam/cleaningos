---
type: system
engine: [Labor, Logistics]
season: [Survival, Stability, Scale]
laws: [Stop Guessing]
status: Canonical
sources: [2026-02-24 Weekly Coaching Call, Every SOP We Use]
updated: 2026-08-07
---

# Cleaner Availability System

> [!abstract] In one line
> Ask every cleaner for next week's availability every Friday — don't discover the gap on Tuesday for Thursday.

## Definition

A weekly routine for confirming which cleaners are available when, so that scheduling
gaps surface a week ahead instead of the day before a clean. Distinct from [[Backup Cleaner]] (having enough total staff) and [[Scheduling Cleans]] (how a single day is
structured) — this is about knowing, continuously, who's actually available.

## Why It Matters

Cleaners who work for multiple companies ("squirrely") are the norm at small scale. Without
a standing check, you find out someone can't cover Thursday's clean on Tuesday, when
there's no time left to fix it.

## Symptoms

- Last-minute scrambles to cover a clean
- Booking a cleaner only to have them cancel days later
- No visibility into who's actually free next week until you need someone

## Common Mistakes

- Only checking availability when a specific job needs covering
- Not confirming a booking immediately after scheduling it
- Building automation to route around an unreliable cleaner instead of replacing them —
  see [[Scheduling Cleans]]

## Models

**The Friday text.** Every Friday, message every cleaner: update your availability for
next week. At small scale, when cleaners are less reliable, call instead of text:

> "What's your availability, seriously? I need to know."

**Confirm immediately.** The moment you book a cleaner, message them right away:

> "Your calendar is available, you're booked for this — that's good."

This closes the gap where you book someone Tuesday for Thursday and only find out
Wednesday night that they can't make it.

**At scale — first to respond gets it.** When multiple cleaners are open for the same
slot, message all of them the job details at once. Whoever accepts first gets the clean.
This treats them like the contractors they are and creates a healthy competitive dynamic
rather than you manually assigning each job.

**If someone is still unreliable despite this,** that's not an availability-system
problem — see [[Scheduling Cleans]] → Common Mistakes.

**The cleaner-side mechanics, in BookingKoala.** Two layers: a **default availability**
(baseline days/times, set once via Manage Availability → Change Availability → Default
Availability) and a **weekly update** for that specific upcoming week (Manage
Availability → Change Availability → Specific Date), where a cleaner adds extra open days
or marks days they can't work. Best practice is to update by Friday for the coming week,
at least a week out where possible — and **don't change availability within 72 hours of a
scheduled cleaning** except for a genuine emergency, in which case notify the team
immediately.

**The admin-side half of the same Friday routine.** [[SOPs]]'s weekly close-out process
runs this from the other direction: confirm every cleaner's availability for next week
(manually or via an automated reminder) and update the payment tracking sheet with
completed jobs, durations, and any adjustments — see [[Business Finances]] for the pay
side. The point of running both halves the same day: no surprises going into the next
week, on either the schedule or the payroll.

## Checklist

- [ ] Send the Friday availability text to every cleaner
- [ ] At small scale, call rather than text
- [ ] Confirm every booking immediately, in writing
- [ ] At scale, offer open slots to all available cleaners — first response wins
- [ ] If unreliability persists despite this system, replace the cleaner rather than
      building more automation
- [ ] Cleaners set a default (baseline) availability once, and update it for the specific
      upcoming week by Friday
- [ ] No availability changes within 72 hours of a scheduled clean except genuine
      emergencies, reported immediately
- [ ] Admin side: same Friday, confirm every cleaner's availability and update the
      payment tracking sheet together

## Templates

- "Update your availability in BookingKoala for the upcoming week. We need to know."
- "Your calendar is available. You're booked for this. That's good."
- "Here's the job — would you like to take it?" (sent to all available cleaners at once)

## Videos

[[2026-02-24 Weekly Coaching Call]]
[[Every SOP We Use]] — "FOR CLEANERS: Cleaner Schedule SOP" and "EOW/Friday SOP" lessons.

## Student Examples

*None yet — this call describes the system, not a specific member's rollout of it.*

## AI Prompts

*None yet.*

## FAQ

*None yet.*

## Conflict History

*None.*

## Presented In

*None yet.*

## Related Concepts

- [[Backup Cleaner]]
- [[Scheduling Cleans]]
- [[BookingKoala]]
- [[Testing A New Cleaner]]
- [[Labor Engine]]
