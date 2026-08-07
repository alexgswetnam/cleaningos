---
type: concept
engine: [Logistics]
season: [Survival, Stability, Scale]
laws: [Stop Guessing]
status: Developing
sources: [Leads 101 Part 2]
updated: 2026-08-06
---

# Payment Processor Selection

> [!abstract] In one line
> Pick whatever processor connects cleanly to your scheduling platform — don't turn it into a decision, and only negotiate the fee once real volume is moving through it.

## Definition

Which payment gateway (Stripe, Square, or another) actually runs the charge behind your
booking system. Distinct from [[Payment Verification & Collection]], which is the
*process* of verifying and collecting a payment once a processor is already in place —
this page is the earlier, one-time decision of which processor to use at all.

## Why It Matters

Early on this is not a decision worth much time. Most processors carry similar fees at
low volume, and the only question that actually matters is compatibility with the
scheduling platform. Owners who treat it as a major strategic choice are spending
attention on the wrong Engine question — see [[Systems Cost-Benefit Analysis]].

At higher volume it does matter: a 1% fee difference on $100,000 processed is $1,000
kept or lost. That's the point where it's worth negotiating, not before.

## Symptoms

- Overthinking Stripe vs. Square before the business has real volume
- A processor that doesn't integrate with the scheduling platform, creating manual
  reconciliation work
- Never having checked whether the current rate is negotiable at current volume

## Common Mistakes

- Letting the processor choice become a bottleneck to launching
- Picking a processor that doesn't support card-on-file, which breaks
  [[Payment Verification & Collection]]'s hold-and-charge model entirely
- Ignoring fees once volume is high enough that a percentage point is real money

## Models

**The compatibility test.** The only early question: does the processor work with the
scheduling platform? In this business, [[BookingKoala]] keeps the card on file and Stripe
handles the actual charge — the two are integrated, so a booking charged in BookingKoala
is processed through Stripe without extra steps.

**The negotiation trigger.** Not a date or revenue number — a volume threshold. Once
enough money is moving through the processor, ask about a lower rate. The math: 1% on
$100K processed is $1,000. Below that kind of volume, the conversation isn't worth having.

## Checklist

- [ ] Confirm the processor integrates with your scheduling/booking platform
- [ ] Confirm it supports card-on-file (required for [[Payment Verification & Collection]])
- [ ] Don't let this decision block launch — normal fees at low volume are close enough
      across processors that it doesn't matter which you pick
- [ ] Once processing meaningful volume, ask the processor about a reduced rate

## Templates

*None yet.*

## Videos

[[Leads 101 Part 2]] — "What payment processor to use..." lesson.

## Student Examples

*None yet.*

## AI Prompts

*None yet.*

## FAQ

**Q:** Should I use Stripe or Square?
**A:** Not established as a general answer — Stripe is what this business uses, chosen
for its BookingKoala integration. The source is explicit this isn't a decision to spend
much time on; pick whichever connects to your platform.

## Conflict History

*None.*

## Presented In

*None yet.*

## Related Concepts

- [[Payment Verification & Collection]]
- [[BookingKoala]]
- [[Systems Cost-Benefit Analysis]]
- [[Logistics Engine]]
- [[SOPs]]
