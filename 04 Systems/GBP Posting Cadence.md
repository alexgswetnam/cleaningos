---
type: system
engine: [Leads]
season: [Stability, Scale]
laws: [Clarity Creates Momentum]
status: Canonical
sources: [Every SOP We Use, 2026-04-01 Weekly Coaching Call, 2026-04-20 Weekly Coaching Call, Google Biz Profile Setup and Growth, Weekly Sales Training Call — April 6]
updated: 2026-08-07
---

# GBP Posting Cadence

> [!abstract] In one line
> Three real-job photos a week, Monday/Wednesday/Friday, 80% updates and 20% offers —
> consistency is the ranking signal, not any single post.

## Definition

A weekly posting routine for Google Business Profile: three posts per week on a fixed
schedule, mostly real-job updates with occasional capped offers. Distinct from
[[Google Business Profile Naming]], which covers the profile's name and physical-address
pin — the two moves that get you *found*. This is what keeps the profile active once
it's found, which GBP's algorithm also weighs.

## Why It Matters

Consistent posting boosts local SEO, gives prospects real before/after proof instead of
stock photography, and gives every post a direct "Call now" path to booking. It's a
low-cost, compounding lever on top of the naming/address work that gets the profile
ranking in the first place.

## Symptoms

- GBP has no posts, or posts are sporadic
- Posts use stock imagery instead of real job photos
- No consistent call-to-action across posts
- Offers with no expiration or a discount deep enough to train clients to wait for one

## Common Mistakes

- Posting stock images instead of real before/after job photos
- Including faces, personal items, or documents in photos
- Discounting more than ~15%, or running an offer with no end date
- Putting a price or phone number directly in the post text
- Reusing the same photos across multiple posts without tracking usage

## Models

**Cadence:** 3 posts/week, Monday/Wednesday/Friday. 80% updates (services, tips,
testimonials), 20% offers.

> [!info] A looser floor stated elsewhere — not treated as contradicting this
> Two coaching calls give looser cadence language: "2x/week minimum" (2026-04-01) and
> "every other day at minimum, daily is better" (2026-04-20) — see
> [[Google Business Profile Naming]]. Read as a floor rather than a competing target: this
> page's Mon/Wed/Fri/3-per-week routine satisfies both stated minimums and is the more
> specific instruction (a dedicated SOP vs. conversational coaching guidance). Noted here
> rather than silently merged, since the two sources were never reconciled by Alex
> directly.

**Photos:** always real job photos, before/after, focused on the cleaned room. Avoid
faces, family items, documents, anything sensitive. Consistent filename convention:
`city_service_cleaningbiz_001.jpg`.

**Copy:** include city + neighborhood/landmark for local SEO. One service per post.
Friendly, professional tone. CTA: "Tap Call now to book." Max 1 emoji, 650–900
characters.

**Offer posts specifically:** discount capped at 15%, short validity window, one
condition stated (e.g. "new clients only"), never a price or phone number in the text.

**Post structure:** hook/title → body (benefit/service/solution) → CTA → optional
hashtags → 1–3 real photos.

**Where to actually schedule the posts.** [[Harvest CRM]]'s Social Planner (Marketing →
Social Planner) connects directly to the Google Business Profile and lets you write and
schedule posts from inside the CRM rather than GBP's own interface — same rules apply
(no phone numbers, no stock images, no text baked into graphics, "Call Now" over a number).

**Photo volume, beyond the 3 posts/week themselves.** Upload 3–5 new images to the
rotation weekly, so the photo pool doesn't run dry between posting days. Source: the
fuller, versioned internal SOP (v2.0, effective Nov. 2025, prepared by Elle, approved by
Alex/Elijah) in [[Google Biz Profile Setup and Growth]] — same routine as the shorter
SOP already archived under [[Every SOP We Use]], with more mechanical detail attached.

**Sourcing real job photos from BookingKoala, step by step.** Open BookingKoala → Jobs
→ filter by the city/zip of the target GBP location → select 3–5 jobs with strong
visuals → download 4–6 images total → rename to the filename convention → store in
`Google Drive > Marketing > GBP > <Location> > YYYY > MM > raw/selected`.

**The photo uniqueness log, with its actual columns.** A shared sheet titled "GBP Photo
Usage Log": `Date | GBP Location | File Name | BookingKoala Job ID | Room/Area | VA |
Notes`. Rule: search the sheet before scheduling a post — if a photo is already used on
another GBP location, pick a different image. This is the mechanical version of the
"don't reuse photos across locations" rule already on this page.

**Who does what.** Marketing Assistant / Admin / VA-Sales handles copywriting, post
creation, scheduling, and compliance. VA-Fulfillment / Team Lead sources the real job
photos from BookingKoala and runs quality checks. Manager/Owner handles approval (if
required) and the monthly performance review.

**Approval workflow.** Draft the post in Google Docs or a Canva content calendar →
attach the photos plus their filenames → manager reviews if approval is required → once
approved, upload to GBP, log the photo usage in the Photo Usage Log, and do a final
formatting check before it goes live.

**The exact ChatGPT prompt used to generate post copy, verbatim:**

```
You are writing a Google Business Profile post for a home cleaning company. Follow these rules STRICTLY:
- Return exactly 3 options labeled Option 1/2/3.
- Each option must be 650–900 characters.
- Do NOT include a phone number, email, or any URL.
- CTA must be a single, short line: "Tap **Call now** to book."
- Work in local SEO naturally using these variables: {City}, {Neighborhood_or_Landmark}.
- Emphasize exactly one service: {ServiceName} (e.g., Deep Clean, Move-Out Clean, Standard Maintenance, Short-Term Rental Turnover).
- Use friendly, professional tone; avoid hype.
- For Offer posts only (if `{IsOffer}=true`): discount must be ≤ 15%, include start `{OfferStartDate}` and end `{OfferEndDate}` dates, and a one-line condition like "new clients only." Do NOT embed prices.
- If `{IsOffer}=false`, do NOT mention any discount.
- Never ask to text/call a number; rely on the Call now button only.
- Avoid emojis except 0–1 optional tasteful emoji.
- Output in plain text.

Inputs:
- City: {City}
- Neighborhood_or_Landmark: {Neighborhood_or_Landmark}
- ServiceName: {ServiceName}
- IsOffer: {true|false}
- OfferDiscount: {0–15}% (ignored unless IsOffer=true)
- OfferStartDate: {YYYY-MM-DD}
- OfferEndDate: {YYYY-MM-DD}

Now produce 3 options that follow every rule above. Make the options distinct in angle (benefit, problem-solution, social proof), but consistent in tone.
```

**Monthly performance review, with the actual metrics.** Review GBP Insights monthly:
Views, Calls, Clicks, and Direction requests. Evaluate which post types perform best,
adjust the schedule or content mix accordingly, and archive top-performing posts as
templates — the same "review monthly, save top performers" rule already on this page,
now with the specific metrics named.

## Checklist

- [ ] Post Mon/Wed/Fri, 3x per week
- [ ] Upload 3–5 new photos to the rotation weekly
- [ ] 80/20 split: updates vs. offers
- [ ] Real photos only, correct filename convention, no repeats (tracked in the GBP
      Photo Usage Log — search it before scheduling)
- [ ] City + neighborhood in copy; one service per post
- [ ] CTA present: "Tap Call now to book"
- [ ] Offer posts: ≤15% discount, dated, one condition, no price/phone in text
- [ ] Character count 650–900, max 1 emoji
- [ ] Draft → attach photos/filenames → manager review (if required) → upload → log
      photo usage → final formatting check
- [ ] Review GBP Insights monthly (Views, Calls, Clicks, Direction requests); save top
      performers as templates

## Templates

Post structure and copy rules above serve as the template. The ChatGPT prompt for
generating post copy (verbatim, in Models above) is the one concrete template this
source provides — see also AI Prompts.

## Videos

- [[Every SOP We Use]] — "Google Business Profile - Posting 3x/Week SOP" lesson.
- [[Google Biz Profile Setup and Growth]] — "SOP for Making Google Biz Profile Posts"
  (the fuller, versioned internal SOP) and "We add $6k in new business every month with
  this."

## Student Examples

*None yet.*

## AI Prompts

**Generating GBP post copy.** The exact prompt in Models above, run with the four
variables (`City`, `Neighborhood_or_Landmark`, `ServiceName`, `IsOffer` plus offer
fields when relevant) filled in per post. Returns 3 distinct angles (benefit,
problem-solution, social proof) in one pass, each already compliant with the character
count, CTA, and no-phone-number rules.

## FAQ

*None yet.*

## Conflict History

*None.*

## Presented In

*None yet.*

## Related Concepts

- [[Google Business Profile Naming]]
- [[GBP Verification]]
- [[Review Response Scripts]]
- [[Leads Engine]]
- [[Social Media Strategy]]
- [[Harvest CRM]]
