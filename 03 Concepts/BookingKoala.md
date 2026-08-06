---
type: concept
engine: [Logistics]
season: []
laws: []
status: Developing
sources: [Premium Workshop — 4 Seasons, 4 Bottlenecks, Zapier The Software Glue, 2026-02-24 Weekly Coaching Call, 2026-03-04 Weekly Coaching Call, 2026-04-01 Weekly Coaching Call]
updated: 2026-08-06
---

# BookingKoala

> [!abstract] In one line
> The booking calendar and provider-management software — pair individual providers, don't use teams.

## Definition

Booking and scheduling software used alongside [[Harvest CRM]]. Clients book through it;
cleaners get a **provider account** in it during onboarding. See [[Harvest CRM]]'s FAQ for
why both tools exist: BookingKoala schedules cleans against provider availability;
Harvest CRM tracks leads and applicants through stages.

## Why It Matters

*Not yet documented.* What's known:

- A cleaner's **provider account** is created during same-day onboarding, per the hiring
  SOP — see [[SOPs]]
- A **new booking** is the trigger for the pipeline-update zap — see [[Zapier]]

So it sits at the intersection of Labor and Logistics: it's where cleaners exist as
schedulable resources and where client bookings originate.

## Symptoms

- Cleaners showing as available in the calendar when they're actually double-booked
- Manually scanning the calendar and still missing overlaps
- Scheduling chaos on clients booked at odd intervals (e.g. every three weeks)

## Common Mistakes

- Using "teams" instead of individual providers with pairing — the root cause of most
  double-booking, since BookingKoala doesn't correctly account for individual availability
  inside a team
- Leaving calendar colors on the default instead of provider-based, making overlaps hard
  to spot visually
- Doing booking and scheduling from the mobile app instead of a laptop
- Booking recurring clients on three-week intervals, which don't align cleanly with any
  calendar system and compound into scheduling chaos over time

## Models

**Fixing double-booking: individual providers with pairing, not teams.** The root cause
of most BookingKoala double-booking is using "teams." When a team is created, BookingKoala
doesn't properly account for each member's individual availability — it still shows team
members as available even when they're on a team clean. Fix: delete all teams, add every
cleaner as an individual provider, and when a clean needs two people, assign one provider
then use the "pair provider" function to add the second. This way BookingKoala tracks each
person's real availability and pairing adjusts for both.

**Spotting double bookings visually: provider-based colors.** Settings → General → Store
Options → "How do you manage colors in your admin booking calendar?" → set to "Provider
based." Each cleaner becomes a distinct color; overlapping colors on the calendar mean
someone's double-booked. Checking this week and next week for overlaps should be part of
the VA's daily SOP.

**Split-screen scheduling workflow.** Use the week view with sidebar layout. Keep two
BookingKoala tabs open — one showing the calendar/availability, one for making the
booking — so you're checking availability and booking in parallel instead of tabbing back
and forth. Rick: *"We have a split screen with two BookingKoala browsers — one with the
schedule, one to make bookings. That's what helps me not double-book."* Do this on a
laptop; the mobile app is for messaging and notifications only.

**Known quirk: recurring cleans can still double-book, and holidays don't self-block.**
Even with individual providers and pairing set up correctly, recurring bookings
occasionally double-book the same cleaner, and marking a day as a holiday doesn't stop
BookingKoala from booking onto it. There's no fix in the software — only a monitoring
habit:

- At the start of every month, review the full calendar and fix any double bookings found.
- Fold it into the VA's end-of-day checklist — one of roughly eight daily items — checking
  this week and next week for overlaps, every single day, not just monthly.
- Look at least two weeks ahead for upcoming holidays and preemptively move affected cleans.
- If a client only needs to move by one day, just move them — no call needed. More than a
  day, call and explain: *"Your cleaner accidentally got double-booked. Is there another
  day that works?"*

**A second known bug: recurring clients can silently vanish from the calendar** after
roughly a year and have to be manually re-added. No fix identified — just something to
watch for.

**Drop three-week intervals.** Recurring clients booked every three weeks don't align
cleanly with any calendar system and eventually produce scheduling chaos. Standardize to
every two weeks or every four weeks (monthly). If a client won't move off three weeks,
it's reasonable to keep them short-term but plan to eventually let them go if they won't
shift to two or four weeks.

**Offering slots, not asking for availability.** Look at a specific cleaner's week view,
see what's actually open (e.g. Wednesday afternoon, Thursday late morning, Friday
afternoon), and give the client those exact options rather than an open question:

> "When are you looking for the clean? I have Wednesday afternoon or Friday afternoon —
> those are your options."

Book based on your schedule's availability, not the client's preference first. It's faster
and it keeps the calendar dense instead of scattered.

**Recurring bookings repeat on their own.** Set a booking as weekly, bi-weekly, or
monthly and it doesn't need to be manually recreated each time.

**Automated reminders replace manual texting.** Set to fire 25 hours before, and again at
24/48 hours before. This is what eliminates the nightly manual-text routine several
members were still doing by hand.

## Checklist

- [ ] Check the cleaner's week view before offering times to a client
- [ ] Offer 2 specific slots, not an open "when works for you?"
- [ ] Set recurring clients to weekly/bi-weekly/monthly so it doesn't need rebuilding
- [ ] Set automated reminders (25 hr and 24/48 hr) instead of manually texting
- [ ] Use individual providers with pairing — delete teams
- [ ] Set calendar colors to "Provider based" (Settings → General → Store Options)
- [ ] VA checks this week and next week daily for overlapping colors
- [ ] Run booking/scheduling from a laptop with a split-screen two-tab setup
- [ ] Standardize recurring intervals to two or four weeks, never three
- [ ] Review the full calendar for double bookings at the start of every month
- [ ] Look at least two weeks ahead for holidays and preemptively move affected cleans
- [ ] Watch for recurring clients silently disappearing after ~1 year — known bug, no fix

## Templates

- "When are you looking for the clean? I have [slot A] or [slot B] — those are your
  options."

## Videos

- [[Premium Workshop — 4 Seasons, 4 Bottlenecks]] — provider account in the hiring SOP
- [[Zapier The Software Glue]] — booking as a zap trigger
- [[2026-02-24 Weekly Coaching Call]] — live scheduling walkthrough
- [[2026-03-04 Weekly Coaching Call]] — double-booking fix, provider colors, split-screen
- [[2026-04-01 Weekly Coaching Call]] — monthly + daily double-booking checks, holiday quirk, disappearing-client bug

## Student Examples

**Rick** — split-screen two-tab workflow to avoid double-booking.

**Nicole** — discovered three-week clean intervals were the source of her scheduling
chaos; moved most clients to two- or four-week intervals.

**Courtney, 2026-04-01** — hit the recurring-client-disappears-after-a-year bug; no fix
found, just re-adds the client when it happens.

## AI Prompts

*None yet.*

## FAQ

**Q:** Why both BookingKoala and [[Harvest CRM]]?
**A:** They solve different problems. BookingKoala schedules cleans against provider
availability. Harvest CRM tracks leads and applicants through stages and automates
follow-up. A cleaner's BookingKoala provider account is created as a downstream step of
the Harvest CRM hiring pipeline, not a duplicate of it. See [[Harvest CRM]].

## Conflict History

*None.*

## Presented In

*None yet.*

## Related Concepts

- [[Harvest CRM]]
- [[Zapier]]
- [[SOPs]]
- [[Scheduling Cleans]]
- [[Logistics Engine]]
- [[Testing A New Cleaner]]
