---
type: system
engine: [Leads, Logistics]
season: [Survival, Stability]
laws: [Build In Order]
status: Canonical
sources: [Get Phone Number + A2P Approval]
updated: 2026-08-07
---

# SMS Opt-In Consent

> [!abstract] In one line
> The lead form is where you earn the right to text — build it wrong and the carrier
> denies you months later, after the leads are already in.

## Definition

The consent a lead gives, at the moment they submit their information, to receive text
messages from the business. In practice it's a **required checkbox** on the lead form with
specific legal language, plus a screenshot of that checkbox used as evidence during
[[A2P Verification]].

## Why It Matters

This is a [[Five Laws|Build In Order]] problem wearing a compliance costume.

The lead form is built during the Leads Engine work. A2P approval happens later, in
Logistics. If the checkbox wasn't required — or the wording was thin, or the policy links
were hyperlinked instead of naked URLs — you don't find out until the carrier denies the
campaign. By then you have leads you legally cannot text, and fixing the form doesn't
retroactively fix consent for the people already in the list.

Get it right once at form-build time and A2P is a formality. Get it wrong and you rebuild
the form, re-collect consent, and resubmit.

## Symptoms

- A2P campaign denied with no specific reason given
- The SMS checkbox on your form is optional, or pre-checked
- Your consent text links to "Terms of Service" as anchor text rather than showing the URL
- You have leads in the CRM you're not sure you're allowed to text
- The screenshot you submitted was a mockup, or a form editor view, not the live form

## Common Mistakes

- Making the checkbox optional. Carriers read optional as no consent.
- Pre-checking the box. Same problem — consent has to be an action.
- Anchor-text links (`Terms of Service`) instead of full naked URLs
- Omitting "consent is not a condition of purchase"
- Omitting "Msg & data rates may apply"
- No STOP instruction in the checkbox text
- Screenshotting the form builder instead of the form as a user sees it
- Copying the template with someone else's business name still in it

## Models

**Four things the checkbox text must contain.** Each one exists because a carrier looks
for it:

| Element | Why it's there |
|---|---|
| "I agree to receive SMS updates and promotional messages from [BUSINESS]" | Names who is texting and that it includes promotional content |
| "Msg & data rates may apply" | Required disclosure |
| "Consent is not a condition of purchase" | Proves the consent is freely given, not coerced |
| "Reply STOP to opt out" | Proves an exit exists |
| Full naked URLs to Terms of Service and Privacy Policy | Must be readable in a screenshot |

The naked-URL rule is the one people trip over. The screenshot is the evidence, and a
reviewer can't click a hyperlink in an image — so the URL has to be visible as text.

**Where the screenshot comes from.** Build the form in Facebook Lead Forms, add the
required checkbox, then capture it *as it appears to a user*. Not the editor. Not a
comp. The point is to show a reviewer exactly what the lead saw.

## Checklist

- [ ] Checkbox is **required**, not optional
- [ ] Checkbox is **not** pre-checked
- [ ] Business name is your business name — no placeholder, no one else's
- [ ] "Msg & data rates may apply" present
- [ ] "Consent is not a condition of purchase" present
- [ ] "Reply STOP to opt out" present
- [ ] Terms of Service link is a full naked URL
- [ ] Privacy Policy link is a full naked URL
- [ ] Both policy pages actually exist and load
- [ ] Screenshot taken of the live form, user's view
- [ ] Opt-in confirmation message configured in [[Harvest CRM]]

## Templates

**Checkbox copy** — replace the bracketed values:

> I agree to receive SMS updates and promotional messages from **[YOUR BUSINESS NAME]**.
> Msg & data rates may apply. Consent is not a condition of purchase. Link to our Terms of
> Service **[https://yoursite.com/terms]** and Privacy Policy
> **[https://yoursite.com/privacy]**. Reply STOP to opt out.

> [!warning] The source template has a real business name in it
> The lesson's version reads *"...promotional messages from My Personal Cleaners."* That is
> a placeholder leak, not an instruction. A student who pastes it submits another company's
> name to the carrier. The version above is corrected. The source file stays as it is —
> Rule 3.

**Opt-in confirmation message** — sent automatically once someone opts in:

> You have successfully opted in to receive notifications and promotional SMS from [YOUR
> BUSINESS]. Reply STOP if you need to opt out in the future.

*(The source reads "opted-in to received notification" — a typo. Corrected here, since this
message goes to every client who opts in.)*

## Videos

- [[Get Phone Number + A2P Approval]]

## Student Examples

*None yet.* Worth capturing the next student who gets denied and what fixed it — the denial
reasons are the most useful data this concept could have.

## AI Prompts

> Before writing or reviewing any lead form for a cleaning business, check the SMS consent
> checkbox against the five required elements on this page. Do not treat a missing element
> as a style note — each one is a denial reason at A2P submission.

## FAQ

**Q:** Can I add the checkbox later, after I've already collected leads?
**A:** You can add it going forward, but it doesn't cover people who already submitted.
Those contacts need consent collected again before you text them.

**Q:** Does this apply if leads come from Google or my website instead of Facebook?
**A:** Yes. The channel changes, the requirement doesn't — every form that feeds the CRM
needs the checkbox, and you screenshot whichever form you're citing for approval.

**Q:** What about someone who calls me directly — did they opt in?
**A:** Not by calling. Verbal consent is harder to evidence; the reliable path is getting
them onto a form or sending a documented opt-in confirmation. Worth an explicit ruling.

## Conflict History

*None.*

## Presented In

- Course: *What is Harvest CRM* → module *Get Phone Number + A2P Approval*

## Related Concepts

- [[A2P Verification]]
- [[Harvest CRM]]
- [[Conversion Tracking]]
- [[Leads Engine]]
- [[Logistics Engine]]
- [[Five Laws|Build In Order]]
- [[Reactivating Past Clients]]
