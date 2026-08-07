---
type: system
engine: [Logistics]
season: [Stability, Scale]
laws: [Stop Guessing, Clarity Creates Momentum]
status: Canonical
sources: [Every SOP We Use, Leads 101 Part 2]
updated: 2026-08-07
---

# Payment Verification & Collection

> [!abstract] In one line
> Verify the card 48 hours before the job, confirm payment before you close the ticket —
> "we'll figure it out later" is how cleaners show up to jobs that don't pay.

## Definition

Two linked procedures around the same failure mode — a cleaner dispatched to a job that
never gets paid for. Pre-job: a payment authorization hold run 48 hours before the
appointment, with a 24-hour window for the client to fix a failed card before the job is
canceled. Post-job: confirming and logging the actual payment (card, cash, check, or
approved digital method) before the job is considered closed. Distinct from
[[Business Finances]], which covers *paying cleaners* fast and simply — this is about
collecting *from the client* in the first place.

## Why It Matters

Most cleaning businesses lose money from two related but separate failures: clients
canceling last-minute because a card failed with no advance warning, and payments that
were supposedly collected but never got logged anywhere — which, functionally, means
they didn't happen. Both are prevented by treating payment as a checklist item, not an
assumption.

## Symptoms

- Cleaners arrive to jobs where the card was going to fail anyway
- "I thought the cleaner collected it" / "I thought it was already charged" disputes
- No single record of which jobs are paid and which aren't
- Cleaners paid out of pocket, unpaid, over an ambiguous job

## Common Mistakes

- Never verifying payment until the day of the job
- Making exceptions to the 24-hour cure window "just this once"
- Assuming payment was handled instead of confirming with the cleaner or the system
- Not logging a payment the moment it's collected, so it disappears from tracking

## Models

**48-Hour Payment Rule (pre-job):**

1. 48 hours before the appointment, attempt a payment authorization hold.
2. If it fails, notify the client immediately and follow up (30 minutes, then a call
   at 2 hours if no response).
3. 24 hours before the appointment: if fixed, confirm the booking. If not fixed, cancel.
4. **Cleaner protection:** pay the cleaner $25 if they've already started traveling or
   arrived, even if the job gets canceled for non-payment — this is what keeps good
   cleaners trusting the schedule.
5. Never send a cleaner to a job without a verified payment method. No exceptions.

**Post-clean collection (3-step):**

1. Check the payment method on file before doing anything (card, cash, check, approved
   digital like Zelle).
2. Follow the flow for that method — charge card on file once the cleaner confirms
   completion; for cash/check, confirm with the cleaner whether it was collected.
3. **Log it everywhere** — CRM, job notes, and the payment tracking system. If it's not
   logged, it didn't happen.

**Escalate** when the payment method is unclear, wasn't received, the client is
unresponsive, or someone's asking for a policy exception.

**The mechanism behind the 48-hour hold, and why a hold isn't a charge.** A second source
corroborates the 48-hour window and adds the client-facing distinction that makes it work
without creating confusion: the hold is run through [[BookingKoala]], and it exists to
surface a bad card *before* a cleaner is dispatched, not after. If the hold fails, contact
the client immediately: *"Hey, the hold didn't go through, so we need to fix that before
the clean."* A legitimate client with a real card problem will usually fix it — a
different card, or a funds transfer.

The distinction to hold onto on the phone: **a hold is not a charge.** Clients sometimes
say "I got charged" when they see the hold. The correction is explicit and immediate:
*"We put a hold, but we will not charge you until after the cleaning and everything goes
perfectly well and you're satisfied."* Explaining this clearly up front is what prevents
the alternative — cleaning a home first, then discovering there's nothing to collect and a
cleaner who still needs to be paid, with a client who may simply disappear.

**Payment methods policy — card as the default, not just card-on-file for the hold.**
Beyond the hold mechanism itself, the underlying policy is that card should be the only
payment method accepted going forward. Cash, Zelle, Venmo, Cash App, and checks all remove
the "recourse" the card-on-file model depends on — if a client refuses to pay after a
completed clean, or isn't home for a lockout, there's no card to charge a cancellation or
lockout fee against. **Out-of-state certified check requests are a specific, named scam
pattern** — treat with real suspicion, not just caution. The business has made exceptions
before for trusted long-term clients (a next-door neighbor paying cash, an elderly client
who has always paid by check), but the policy going forward, especially while scaling, is
not to make new ones: *"We're a real business... you go to the doctor's office, you pay
card."* Mixed payment methods also make bookkeeping meaningfully harder to track.

## Checklist

- [ ] 48 hours out: run authorization hold
- [ ] If failed: notify client, follow up at 30 min and 2 hrs
- [ ] 24 hours out: confirm or cancel — no exceptions to the deadline
- [ ] Cleaner paid $25 if en route or arrived, regardless of outcome
- [ ] Post-job: payment method confirmed before closing the ticket
- [ ] Payment logged in CRM, job notes, and tracking system
- [ ] Unclear or missing payment escalated to a manager same day
- [ ] If a client says "I was charged," correct it immediately: it's a hold, not a charge,
      until after the clean
- [ ] Card is the default and effectively only accepted method going forward — no new
      cash/Zelle/Venmo/Cash App/check exceptions
- [ ] Treat any out-of-state certified-check request as a likely scam

## Templates

**Failed card notice:**
> "Hi [Client Name], we attempted to verify your payment method for your upcoming
> cleaning, but the card on file was declined. Please update your payment method within
> 24 hours to keep your booking active. Thank you!"

**Confirmed after fix:**
> "Thank you, [Client Name]! Your payment method has been updated and your cleaning is
> confirmed. We look forward to serving you!"

**Canceled for non-payment:**
> "Hi [Client Name], we were unable to verify your payment method for your upcoming
> cleaning, so the appointment has been canceled. You're welcome to reschedule anytime
> once your payment method is updated."

**Hold-not-a-charge correction:**
> "We put a hold, but we will not charge you until after the cleaning and everything goes
> perfectly well and you're satisfied."

**Failed-hold outreach:**
> "Hey, the hold didn't go through, so we need to fix that before the clean."

## Videos

- [[Every SOP We Use]] — "Card Declined SOP" and "How to Collect Payment from Clients"
  lessons.
- [[Leads 101 Part 2]] — "Why we put a 48 hour card hold..." and "What payment methods to
  accept..." lessons.

## Student Examples

*None yet.*

## AI Prompts

*None yet.*

## FAQ

**Q:** What about first-time clients or repeat payment failures?
**A:** The source lesson suggests a deposit (e.g. 25%) as optional for first-time
clients, and tagging repeat-failure clients "high risk" and requiring prepayment going
forward.

## Conflict History

*None.*

## Presented In

*None yet.*

## Related Concepts

- [[Business Finances]]
- [[Reschedule Not Cancel]]
- [[Quality Complaints]]
- [[BookingKoala]]
- [[SOPs]]
