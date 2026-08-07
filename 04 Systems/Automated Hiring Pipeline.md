---
type: system
engine: [Labor, Logistics]
season: [Stability, Scale]
laws: [One Step Wins, Build In Order]
status: Canonical
sources: [2026-02-20 Weekly Coaching Call, 2026-03-04 Weekly Coaching Call, 2026-04-01 Weekly Coaching Call, 2026-04-08 Weekly Coaching Call, Weekly Sales Training Call — April 6]
updated: 2026-08-07
---

# Automated Hiring Pipeline

> [!abstract] In one line
> Every stage of hiring except the interview itself can fire on its own — move a card, the right email goes out. Now templatized into every member's Harvest CRM.

## Definition

A CRM pipeline (built in Go High Level / Harvest CRM) where moving an applicant from one
stage to the next automatically triggers the email, calendar link, or document request
that stage needs — application, interview scheduling, onboarding, and document
collection all happen without the owner writing another message.

## Why It Matters

Hiring is already the slower half of [[Labor Before Leads]] — the reason owners avoid it.
Most of that slowness is administrative, not the actual judgment calls (is this person
good, do they fit). Automating the administrative half doesn't just save time, it lowers
the activation energy for owners who are avoiding hiring out of dread. See Courtney's
example on [[Labor Before Leads]] — the pipeline is what made facing her hiring backlog
feel doable.

## Symptoms

- You're manually writing the same rejection, interview-invite, or onboarding email every
  time someone applies
- Applicants go quiet between stages because nobody followed up
- Onboarding documents (ID, W-9, background check, agreement) live scattered across email
  instead of one record
- You're the bottleneck on every single hire because every step needs you to remember to
  do it

## Common Mistakes

- Running the entire hiring process manually when each stage can be automated
- Not filtering obviously unqualified applicants before they reach a human (e.g. no
  vehicle, when the role requires one)
- Storing onboarding documents outside the CRM contact record instead of in it
- Automating everything except realizing the interview itself still has to be human
- Describing subcontractor cleaners as "full-time employees" on your website — a
  misclassification signal that can draw attention from state workforce commissions and
  the IRS

## Models

**The pipeline, stage by stage — each move triggers its own automation:**

1. **Application.** A form (built in the CRM's form builder) embedded on the website.
   Feeds directly into the CRM's hiring pipeline. Add a hard filter where it's worth
   one — the source example auto-declines anyone who doesn't select "car" for
   transportation.
2. **New Application** — review manually. Check experience and requirements against the
   form answers. If unqualified, tag as "lost" → automated rejection email fires and they
   drop out of the pipeline.
3. **Schedule Interview** — drag here to trigger an email with a calendar link (synced to
   Google Calendar) so the applicant books their own interview slot.
4. **Interviewed** — a holding stage. Move here after the conversation; the only step in
   the whole process that has to be a human.
5. **Schedule Onboarding** — drag here to trigger another calendar-link email for the
   onboarding call.
6. **Document Collection** — drag here to start a *sequence* of emails, each firing after
   the last is submitted: ID upload first (goes straight into the CRM contact), then W-9,
   then insurance, then background check consent, then the signed subcontractor
   agreement. Every document lands in the same contact record.
7. **Rejection**, available at any stage — tag as "lost" and the rejection email fires
   automatically.

**The only manual step in the entire pipeline is the interview conversation itself.**
Everything before and after it can run without the owner writing a message.

**Rick and Melissa's build — the same shape, with more stages named (2026-04-01).**

- **Active Cleaners** — a standing automation, not a hiring stage: every currently-active
  cleaner gets a text every Thursday at 5 PM — *"Check your schedule for the next week or
  two. Make sure it's up to date."*
- **New Application** — routed through the website form, not directly from Indeed.
  Applicants who apply on Indeed are pointed to the website form instead: *"If they don't
  want to take the time to fill out that application on the website, then they're not
  worth it."* The form itself screens on valid driver's license, own vehicle, background-
  check consent, years of experience, and insurance status.
- **Schedule Interview** → automated email/text asking for a good time to call.
- **Interviewed** — same as before, the one human step. Melissa runs ~30-minute
  interviews.
- **Good Candidate** → automated requests for a driver's license photo, then the
  contract/agreement. Once signed, the team gets an automated notification: "ready for
  background check."
- **Background Check** — has to be sent manually; Harvest CRM can't trigger the check
  itself. Once it clears, onboarding kicks off (BookingKoala setup, Discord, etc.).
- **Bad Candidate** → automated rejection email at any stage.
- **Deactivated Cleaners** → automated farewell email when a cleaner leaves.

Setup took about a week, done in small sessions. The one bug Rick hit — duplicating an
automation and forgetting to update its trigger, which fired every email at once — was
user error, not a system limitation.

**Hiring tip layered on top: incentivize referrals from current cleaners.** A $200 bonus
after the referred cleaner completes five cleans gets existing cleaners vouching for
people who already fit the team. One member noted caregivers and home healthcare workers
transition well into cleaning — patient, experienced with demanding situations, and
cleaning is comparatively easier work.

## Checklist

- [ ] Build an application form in your CRM, embed it on your website
- [ ] Set up pipeline stages: New Application → Schedule Interview → Interviewed →
      Schedule Onboarding → Document Collection → Rejection (available anywhere)
- [ ] Add an auto-decline filter for hard requirements (e.g. must have a car)
- [ ] Automate: moving to Schedule Interview sends a calendar-link email
- [ ] Automate: moving to Schedule Onboarding sends a second calendar-link email
- [ ] Automate: moving to Document Collection triggers a sequenced request — ID, W-9,
      background check, agreement, one at a time
- [ ] Automate: tagging "lost" at any stage sends the rejection email
- [ ] Confirm all documents land in the CRM contact record, not scattered in email
- [ ] Route Indeed applicants to the website form as a proving ground, not directly
- [ ] Automate a standing weekly text to active cleaners to keep their availability current
- [ ] Consider a $200 referral bonus (after five completed cleans) to source through
      existing cleaners

## Templates

*None yet — Rashawn's specific automation configuration wasn't captured beyond the stage
sequence above.*

## Videos

[[2026-02-20 Weekly Coaching Call]] — Rashawn's full walkthrough. Alex committed to
templating it for the wider group on this call.
[[2026-03-04 Weekly Coaching Call]] — confirms the pipeline is now templatized into every
member's [[Harvest CRM]] account, via an eight-minute setup video uploaded to the module.
[[2026-04-01 Weekly Coaching Call]] — Rick and Melissa's full walkthrough, referral bonus,
Indeed-to-website routing.

## Student Examples

**Rashawn** — built the pipeline described above in Go High Level (Harvest CRM). His
bottleneck isn't hiring mechanics anymore, it's a VA to answer the phone leads he's
already paying for — see [[When To Hire A VA]].

**Courtney** — wanted the pipeline for her own business on the same call; had been
avoiding hiring despite being at capacity. See [[Labor Before Leads]].

**Courtney, April 6 — the follow-through.** Fully built out in Harvest CRM: applications,
calendar scheduling, and the workflow all automated. Ready to start reaching out to
applicants and running interviews, with a plan to hire within two weeks — the gap between
"wanted the pipeline" (Feb 20) and "it's live and I'm interviewing" closed inside about
six weeks.

**Group-wide** — as of 2026-03-04, the pipeline is no longer just Rashawn's; it's
templatized into every member's [[Harvest CRM]] account.

**Rick and Melissa, 2026-04-01** — built their own instance in about a week, naming
concrete stages (Active Cleaners, Background Check, Deactivated Cleaners) that fill out
the general shape documented above.

## AI Prompts

*None yet.*

## FAQ

**Q:** Does this replace judgment on who to hire?
**A:** No — it only removes the administrative overhead. The interview, and the decision
after it, are still entirely human.

## Conflict History

*None.*

## Presented In

*None yet.*

## Related Concepts

- [[Labor Before Leads]]
- [[Hiring Channels]]
- [[When To Hire A VA]]
- [[Managing A VA]]
- [[Labor Engine]]
