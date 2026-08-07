---
type: concept
engine: [Leads]
season: [Stability, Scale]
laws: [Stop Guessing]
status: Developing
sources: [2026-03-18 Weekly Coaching Call, 2026-04-27 Weekly Coaching Call, Free Resources and Mini Courses]
updated: 2026-08-06
---

# Website Technical SEO Basics

> [!abstract] In one line
> One H1 per page, local business schema everywhere, GBP embedded on service pages — most paid SEO companies still skip these.

## Definition

The minimum technical SEO checklist for a cleaning company website: schema markup,
heading structure, and per-page uniqueness on service area pages. Distinct from
[[Google Business Profile Naming]] (naming convention) and [[GBP Verification]]
(getting the profile approved) — this covers the website itself.

## Why It Matters

Even paid SEO retainers ($2K/month observed) routinely miss these basics. The fix is
usually cheaper and faster than the retainer itself, and doesn't require technical
expertise to verify — an owner can audit their own site with a browser extension in
minutes.

> "Every single SEO company except one I recommend — I haven't seen a single one do it
> right."

## Symptoms

- Paying an SEO company monthly with no clear before/after on rankings
- Service area (city/neighborhood) pages that all read identically
- No local business schema on the site despite promises it was added

## Common Mistakes

- Trusting that paid SEO work was done without auditing it yourself
- Duplicating FAQ or page content across service area pages — Google penalizes this as
  gateway/doorway pages
- Missing an H1 heading on service area pages, or using more than one
- Letting footer or navigation links pull visitors off a PPC squeeze page before they convert
- Broken form/button wiring that goes unnoticed because nobody tested the page as a visitor would

## Models

**The basic checklist, in Alex's words:** *"One H1, the rest H2s or H3s, local business
schema, correct description and title, GBP on the page — that's just very basic."**

**Local business schema, everywhere.** Structured markup connecting each page to the
Google Business Profile. An offer-catalog schema (what services are offered) should
accompany it. This is foundational and frequently just missing, even after a paid vendor
says it's been added.

**Service area (city) pages need their own identity.** Each should have its own H1, its
own meta description, its own title tag — not a template with the city name swapped in.
FAQs on these pages should be H3s, and content should be customized per city rather than
duplicated across pages; Google penalizes near-identical gateway pages.

**PPC squeeze pages need functional testing, not just copy review.** Check that
call-to-action buttons are actually wired to their forms (a broken CSS ID connection can
silently disable a "request a quote" button for weeks). Duplicate the footer with
navigation links removed, so a visitor can't wander off the page before converting — the
whole point of a squeeze page is a single path forward.

**Confirm GBP is embedded on service area pages** — a smaller, easy-to-verify win, but
worth checking since it's part of tying the site back to the profile.

**Embed Google Maps to connect the site to the GBP (2026-04-27 call).** GBP → Share →
Embed a map → copy the HTML → paste it into the site. This is a distinct step from local
business schema — schema tells Google what the business is, the Maps embed physically
links the website to the profile — and both matter for map pack ranking. A second member's
site had schema present but not connected to GBP with hours and contact info, which is its
own gap even when schema exists.

**Use a browser extension to check your own work, not just trust a vendor.** The Detailed
SEO Extension surfaces H1 count, schema presence, and other basics in seconds — the same
free-tool philosophy as auditing a paid SEO vendor's claims.

**Business listing syndication is a secondary, unproven lever.** Syndicating a business
listing across roughly 80 directories (Yelp, WhitePages, Yext/BrightSpark, etc.) gives
Google more references to the business, theoretically building trust. Costs ~$40–50/month
as a CRM add-on. Presented as something Alex was testing on his own business first, not
yet a recommendation — the payoff logic (one extra sale over 12 months covers the cost) is
the same threshold used for the AI CRM auditing tool, but the syndication claim itself is
unverified in any source so far.

**Audit yourself before paying more.** Use ChatGPT to generate the task list from a
checklist like this one, then implement it yourself or hire cheaply (Fiverr) for
mechanical fixes like per-city page content. Don't assume a paid vendor has done the
basics — verify with a browser extension or a manual pass.

**Where the map-pack ranking actually comes from, quantified.** A live audit (using a
WhiteSpark-style ranking-factor report) breaks map-pack ranking down as roughly **32%
Google Business Profile signals, 19% on-page website signals, 16% review signals** —
GBP alone is close to a third of the weight, and GBP + on-page together are nearly half.
This is why fixing the website and the GBP together outperforms either alone.

**Finding the actual keyword to optimize for, not a guess.** Use Google Ads' Keyword
Planner ("Discover new keywords," filtered to your city) to see real local search volume
— e.g., for a window-cleaning business in McKinney, "window cleaning near me" and
"window washers near me" outranked the business's own assumed best keyword. Use whatever
that top keyword is consistently: in the GBP name/category, in the website's H1 and meta
description, and worked naturally into review responses (see [[Review Response
Scripts]]) — Google factors keyword usage in review replies into ranking too. SEMrush and
Ahrefs are named as alternative tools for the same lookup.

**Read a ranking-scan report as binary, not gradient.** A map-pack ranking scan colors
results on a gradient from green to red, but the only distinction that matters is
**position 1–3 (found) vs. position 4+ (invisible)** — a rank of 4 and a rank of 25 are
functionally the same to a searcher who never scrolls the map. Don't over-read shades of
yellow as partial progress.

**Reviews alone don't beat a missing address.** A live comparison: a competitor with far
more reviews (385) than a newly-optimized profile still ranked 7th because they were
running a service-area-only listing with no physical address (see [[Google Business
Profile Naming]] for why address placement outranks review count). Address and pin
placement can out-rank pure review volume.

## Checklist

- [ ] Exactly one H1 per page; everything else H2/H3
- [ ] Local business schema on every page, tied to GBP
- [ ] Offer catalog schema listing services
- [ ] Unique title, meta description, and H1 per service area page — no templated duplicates
- [ ] FAQs on service pages as H3s, content customized per city
- [ ] GBP embedded on service area pages
- [ ] PPC squeeze page CTA buttons functionally tested, not just visually reviewed
- [ ] Footer/nav links removed or duplicated-without-links on squeeze pages
- [ ] Audit any paid SEO vendor's claimed work yourself before trusting it
- [ ] Embed Google Maps from the GBP listing directly on the site
- [ ] Confirm schema is actually connected to GBP (hours, contact info), not just present
- [ ] Run a browser SEO extension yourself rather than relying on a vendor's word
- [ ] Run a ranking-factor report (WhiteSpark or similar) to see the GBP/on-page/review
      signal split
- [ ] Confirm your top keyword with Keyword Planner rather than assuming it
- [ ] Read a rank-scan result as 1–3 (visible) vs. 4+ (invisible), not a gradient

## Templates

*None yet — Alex recorded a separate screen-capture walkthrough of the fixes for Jack's
SEO team; not archived in the vault.*

## Videos

[[2026-03-18 Weekly Coaching Call]] — live audit of Jack's site (Take Care of Cleaners, Toronto).
[[2026-04-27 Weekly Coaching Call]] — live audit of William's site: H1s, schema-to-GBP connection, Maps embed.
[[Free Resources and Mini Courses]] — "How to Get FREE Leads from Google!" lesson.

## Student Examples

**Jack — Take Care of Cleaners (Toronto).** Missing local business schema (SEO company
had said they'd add it weeks earlier — hadn't). Service area pages had no H1, no
description, no title optimization. PPC squeeze page had broken "request a quote" buttons
(CSS ID not connected to the form) and a footer that let visitors navigate away. GBP was
correctly embedded on service pages. With 250 Google reviews already, Alex's read was
that fixing schema and headings alone would meaningfully lift rankings.

**William, 2026-04-27.** Four H1 headings on a single page (should be one). Local
business schema present but not connected to GBP with hours/contact info. No Google Maps
embed on the site at all. No service-area/location pages. Each issue individually fixable
and none requiring a developer.

**Double Eagle Window Cleaning — a live audit outside the cleaning niche, same
mechanics.** Not showing in the map pack at all when the scan was last run months prior;
after adding an address and "window cleaning" to the GBP name, ranked in the top 3 for
"glass cleaner near me" and "window cleaner near me" in the immediate area. GMB
interactions climbed steadily month over month once the changes landed (June 30 → July
36 → August 40+, accelerating into the current month). Remaining gaps identified live:
missing local business schema, four-level heading hierarchy collapsed into H1/H4 with no
H2/H3, no Google Maps embed, thin services/products list on the GBP.

## AI Prompts

*None yet.*

## FAQ

*None yet.*

## Conflict History

*None.*

## Presented In

*None yet.*

## Related Concepts

- [[Google Business Profile Naming]]
- [[GBP Verification]]
- [[PPC Landing Page Strategy]]
- [[Conversion Tracking]]
- [[Leads Engine]]
- [[Review Response Scripts]]
