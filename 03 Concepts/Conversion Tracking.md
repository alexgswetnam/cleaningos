---
type: concept
engine: [Leads]
season: [Stability, Scale]
laws: [Stop Guessing]
status: Developing
sources: [2025-02-03 Weekly Coaching Call, 2025-03-11 Weekly Coaching Call, 2026-03-18 Weekly Coaching Call, 2026-04-27 Weekly Coaching Call, Cleaning Biz 101 — Acquire]
updated: 2026-08-06
---

# Conversion Tracking

> [!abstract] In one line
> If you can't attribute a lead to its source, none of your other numbers are real.

## Definition

The plumbing that ties each lead back to the channel that produced it — UTM tags, cookies, and call tracking.

## Why It Matters

[[Marketing Math]] is only as good as attribution. Guessing that a lead was "organic" when it came from PPC corrupts every downstream number.

## Symptoms

*None yet.*

## Common Mistakes

- Guessing at lead source
- Tracking form fills but not phone clicks
- Assuming a lead is organic because you don't know otherwise

## Models

**The setup:**

1. **UTM campaign builder** tags PPC links — e.g. `thefaithfulcleaners.com?campaign=PPC1`
2. A **cookie plugin** captures the UTM data and submits it along with the lead form, so the source arrives attached to the lead
3. **Google Ads conversion tracking** handles phone-click conversions separately from web form submissions
4. The **Google click ID** lets Alex trace an individual lead back to the click

> "I know that this person came from our Prosper Google Business Profile. I know that this person came in from our PPC and I can track it back with the Google click ID."

**Attribution has a hidden second dimension: time-to-convert, not just source.**
`Cleaning Biz 101 — Acquire` makes this explicit: a lead source isn't just "where did this
come from," it's also "how long did it take to convert." Some leads book same-day, others
two weeks later, others six months later off an automated follow-up text. Without tagging
and tracking this inside the CRM, a campaign can look like it's not working and get cut
before its slow-converting leads have had time to close — killing bookings that were
already in motion. This is the same trap [[Marketing Seasonality]] warns about at the
month level, applied to individual leads.

**When you can't attribute, you can't decide.** Rick ran PPC and LSA simultaneously with
everything reporting through the LSA dashboard — leaving him unable to answer which one to
cut. Without the plumbing below, the only remaining tool is the crude
[[Channel Prioritization|pause test]].

**Microsoft Clarity** records real user sessions on the site — mouse movement, scroll depth, time on page. It's how Alex knows organic visitors spend 10–30 minutes before calling. See [[Close Rate By Channel]]. It's free, and Alex calls it *"freaking spyware"* in the same breath as recommending it — a real session recording (a visitor arriving from GBP, browsing service options, reading the checklist, scrolling reviews, then hitting the contact form) shows exactly where a site helps or loses a visitor, which no aggregate analytics number does on its own.

**Speed-to-lead is a trackable, comparable number, not a vibe.** Industry standard is
responding within five minutes of a form submission. Auditing actual response times
(2026-04-27 call) showed most leads called within minutes, but a few took days — one took
three days purely because of a duplicate-contact bug creating two records for the same
lead. See [[AI CRM Auditing]] for the tool that surfaces this automatically rather than
requiring a manual pull.

**The full attribution pipeline, end to end (2026-03-18 call).** Tag every link pointing
at the site with a UTM campaign parameter (Google's UTM Campaign Builder) — one tag per
source, e.g. "GBP McKinney" or "PPC1." When a visitor lands and fills out the website
form, the UTM data is captured and submitted along with the lead. From there, one of two
paths gets it into [[Harvest CRM]]:

1. **Email-parsing path (the one running live):** form submission → email → [[Zapier]]
   scans for that email every two minutes → a JavaScript step parses the email body →
   creates a contact in Harvest CRM and sends a Discord notification ("new lead"). The UTM
   campaign tag on the parsed data is what shows the source.
2. **Direct-embed path (simpler, not yet adopted):** embed a Harvest CRM form directly on
   the website, skipping the email-parsing step and sending leads straight into the CRM.

**A pop-up form can quietly corrupt attribution.** Jack's site pop-up generated 33 form
submissions in the rest of the month vs. 2 from the original PPC-only form — a real
increase, but it raised the question of whether those submissions were actually coming
from PPC visitors or organic ones, since the pop-up could fire on either. Fix: make sure
lead-capture pop-ups do **not** appear on the [[PPC Landing Page Strategy|PPC squeeze
page]], so PPC leads and organic leads stay cleanly separable.

## Checklist

- [ ] UTM campaign tag on every link pointing at the site, one tag per source
- [ ] Website form captures and submits UTM data with the lead
- [ ] Lead reaches [[Harvest CRM]] automatically — via email-parsing Zap or a direct-embed
      CRM form
- [ ] Team gets notified on new lead (e.g. Discord)
- [ ] Lead-capture pop-ups excluded from the PPC squeeze page so PPC and organic stay
      separable

## Templates

*None yet.*

## Videos

[[2026-03-18 Weekly Coaching Call]] — full UTM + Zapier + Harvest CRM attribution walkthrough.

## Student Examples

**Rick** — ran PPC and LSA at the same time with everything reporting through the LSA
dashboard, and so could not tell which channel to cut. The attribution gap, not the
spend, was the problem.

**Jack** — a new pop-up form drove 33 submissions vs. 2 from the old PPC-only form, which
looked like a win but muddied attribution until the pop-up was excluded from the PPC
squeeze page.

## AI Prompts

*None yet.*

## FAQ

*None yet.*

## Conflict History

*None.*

## Presented In

*None yet.*

## Related Concepts

- [[Marketing Math]]
- [[PPC Landing Page Strategy]]
- [[Close Rate By Channel]]
- [[KPI Tracking Sheet]]
- [[Channel Prioritization]]
- [[Quality Complaints]]
- [[SMS Opt-In Consent]]
