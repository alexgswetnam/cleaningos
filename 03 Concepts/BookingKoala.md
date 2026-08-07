---
type: concept
engine: [Logistics]
season: []
laws: []
status: Developing
sources: [Premium Workshop — 4 Seasons, 4 Bottlenecks, Zapier The Software Glue, 2026-02-24 Weekly Coaching Call, 2026-03-04 Weekly Coaching Call, 2026-04-01 Weekly Coaching Call, Cleaning Biz 101 — Fulfill, Every SOP We Use, Logistics Fundamental Course]
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

**The teams-vs-individuals fix, independently corroborated.** A second source confirms
the same root cause and fix from a different angle: someone using "teams" was having
scheduling messed up by it; switching to individual providers, paired as needed, and
checking availability by pressing into each provider directly, resolved it. The same
source adds a smaller, easily-missed lever: **which calendar view you're in.** Week view
and timeline view are named as the easiest to work from; one owner used a harder view for
four months before switching, making scheduling feel more difficult than the software
actually was. If BookingKoala feels hard to use, check the view before assuming the
software itself is the problem.

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
members were still doing by hand. `Cleaning Biz 101 — Fulfill` names a slightly different
cadence for the same purpose — confirmation on booking, a 5-days-out reminder, a
24-hours-out reminder, and an on-the-way text — plus a payment-charged confirmation as a
distinct final touch. Treat both as the same underlying pattern (confirm → remind twice →
arrival notice) with member-specific timing rather than a contradiction; no source states
one cadence is superior to the other.

**BookingKoala as the fulfillment "source of truth."** If a job is quoted or booked,
BookingKoala is where scheduling and pricing details are trusted to live — not a head, a
text thread, or a personal calendar. Its job, stated as a checklist: pricing and package
consistency, calendar availability and scheduling rules, booking confirmations, reminder
texts/emails, payment-charged notifications, recurring scheduling structure, and cleaners
knowing their pay and schedule through the app. The single-sentence case for all of it:
*"it prevents your business from being run by memory."*

**Only book what a cleaner has actually marked available.** Booking against unconfirmed
availability creates exactly the back-and-forth (with both the cleaner and the client)
that a scheduling system exists to eliminate — treat marked availability as the hard
constraint on what gets booked, not a soft preference.

**When BookingKoala itself goes down: a manual backup, not a freeze.** The rule stated
plainly: *"Your software supports your business — it doesn't run it."* If the system
goes offline, the business shouldn't stop. A 3-step emergency process: (1) **Admin** —
pull every booking from email confirmations ("Cleaning Scheduled" / "New Booking" /
"Cleaning Assigned"), rebuild a temporary schedule in a spreadsheet or the team
communication channel (cleaner, client, time, address, notes — see
[[Internal Communication Via Discord]]), and notify cleaners and clients that the system
is temporarily down but their cleaning is still on. (2) **Cleaners** — work off the
emailed details directly, and report anything missing or unclear to admin immediately
rather than guessing. (3) **Restore** — once BookingKoala is back, enter every manual
note, confirm schedule accuracy, and tell the team normal operations have resumed. The
common failure mode this prevents: freezing when the system fails instead of switching
to the manual process immediately.

## Checklist

- [ ] Check the cleaner's week view before offering times to a client
- [ ] Offer 2 specific slots, not an open "when works for you?"
- [ ] Set recurring clients to weekly/bi-weekly/monthly so it doesn't need rebuilding
- [ ] Set automated reminders (25 hr and 24/48 hr) instead of manually texting
- [ ] Use individual providers with pairing — delete teams
- [ ] Set calendar colors to "Provider based" (Settings → General → Store Options)
- [ ] If scheduling feels harder than it should, try week view or timeline view before
      assuming it's a software problem
- [ ] VA checks this week and next week daily for overlapping colors
- [ ] Run booking/scheduling from a laptop with a split-screen two-tab setup
- [ ] Standardize recurring intervals to two or four weeks, never three
- [ ] Review the full calendar for double bookings at the start of every month
- [ ] Look at least two weeks ahead for holidays and preemptively move affected cleans
- [ ] Watch for recurring clients silently disappearing after ~1 year — known bug, no fix
- [ ] If BookingKoala goes down: admin pulls bookings from email, builds a temporary
      schedule, notifies cleaners and clients — don't freeze
- [ ] On restore: log all manual notes back into the system and confirm accuracy before
      declaring normal operations resumed

## Templates

- "When are you looking for the clean? I have [slot A] or [slot B] — those are your
  options."

## Videos

- [[Premium Workshop — 4 Seasons, 4 Bottlenecks]] — provider account in the hiring SOP
- [[Zapier The Software Glue]] — booking as a zap trigger
- [[2026-02-24 Weekly Coaching Call]] — live scheduling walkthrough
- [[2026-03-04 Weekly Coaching Call]] — double-booking fix, provider colors, split-screen
- [[2026-04-01 Weekly Coaching Call]] — monthly + daily double-booking checks, holiday quirk, disappearing-client bug
- [[Every SOP We Use]] — "BK Down SOP" lesson

## Student Examples

**Rick** — split-screen two-tab workflow to avoid double-booking.

**Rick and Melissa** — struggled specifically with teams vs. individual providers; moving
to individuals was, in Alex's words, "a big change for them."

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
