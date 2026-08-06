---
type: concept
engine: [Leads]
season: [Stability, Scale]
laws: [Stop Guessing]
status: Developing
sources: [2026-03-18 Weekly Coaching Call, 2026-04-27 Weekly Coaching Call]
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

## Templates

*None yet — Alex recorded a separate screen-capture walkthrough of the fixes for Jack's
SEO team; not archived in the vault.*

## Videos

[[2026-03-18 Weekly Coaching Call]] — live audit of Jack's site (Take Care of Cleaners, Toronto).
[[2026-04-27 Weekly Coaching Call]] — live audit of William's site: H1s, schema-to-GBP connection, Maps embed.

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
