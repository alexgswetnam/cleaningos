---
type: concept
engine: [Leads, Logistics]
season: [Scale]
laws: [Stop Guessing]
status: Developing
sources: [2026-04-27 Weekly Coaching Call]
updated: 2026-08-06
---

# AI CRM Auditing

> [!abstract] In one line
> Connect Claude to Harvest CRM and ask it what's been missed — it catches the lead nobody followed up on.

## Definition

Connecting an AI assistant (Claude, in the source) directly to [[Harvest CRM]] and using
plain-language prompts to audit the pipeline: flagging untouched leads, calculating
speed-to-lead, and generating daily reports for a VA — work that would otherwise require
manually scanning every contact record.

## Why It Matters

A pipeline can look fine in aggregate while individual leads quietly go cold — a task
assigned and never closed out, a note never left, a follow-up nobody circled back to. This
is exactly the failure mode [[SOPs|the daily checklist]] exists to prevent, but a
checklist depends on a human remembering to run it thoroughly every day. An AI audit does
the same check mechanically, at whatever frequency it's asked, and catches individual
misses a busy owner or VA would miss by inattention rather than laziness.

## Symptoms

- A lead status shows "in progress" with no recent activity
- Uncertainty about actual speed-to-lead versus the assumed number
- Following up inconsistently because nobody's watching for gaps

## Common Mistakes

- Assuming the pipeline is healthy because most leads are handled — a few slipping through
  is enough to lose real bookings
- Running the free AI plan without budgeting for the upgrade once it's exhausted
- Treating this as a replacement for follow-up discipline rather than a check on it

## Models

**The core prompts.** Two do most of the work:

- *"What leads are untouched that should have a task or status note?"* — surfaces leads
  with no recent activity despite an open status. In the source, this caught a lead
  (inquired days earlier, called once, said he'd talk to his spouse, then silently
  dropped) that should have been followed up on and wasn't.
- *"What's our speed-to-lead Monday through Friday, 9–5?"* — a per-lead breakdown of
  response time. See [[Conversion Tracking]] for the industry-standard five-minute
  benchmark this is measured against.

**Beyond auditing, the same connection can generate content.** Writing or improving email
sequences, drafting mass texts to cold or canceled leads with a promotion, and producing a
daily summary report for the VA — flagged leads, overdue tasks, notes-missing contacts.

**Cost is real but the payoff bar is low.** The free plan burns through quickly on a task
like this. The justification for upgrading: if even one additional booking results over
12 months, the lifetime value of that client covers the subscription many times over — the
same threshold logic used elsewhere for marginal tooling spend (see [[Website Technical
SEO Basics]]'s business listing syndication).

**A paid extension exists but isn't yet adopted.** A $300 add-on, seen working in another
business, transcribes every sales call, grades lead quality, and gives the VA specific
feedback on where a call could have closed better. Noted as something to watch, not yet
something this vault documents as proven for this group.

## Checklist

- [ ] Connect Claude (or a comparable AI) to Harvest CRM
- [ ] Run the untouched-leads prompt on a regular cadence, not just once
- [ ] Run the speed-to-lead prompt and compare against the 5-minute industry benchmark
- [ ] Route flagged leads and overdue tasks into a daily VA report
- [ ] Budget for the paid tier once the free plan's usage limit is hit

## Templates

- "What leads are untouched that should have a task or status note?"
- "What's our speed-to-lead Monday through Friday, 9–5?"

## Videos

[[2026-04-27 Weekly Coaching Call]]

## Student Examples

**Alex** — caught a missed lead (Steve Chisholm — inquired April 25th, called once, no
follow-up since) via the untouched-leads prompt; also surfaced a 3-day response outlier
caused by a duplicate-contact bug via the speed-to-lead prompt.

## AI Prompts

> When auditing a CRM pipeline for a cleaning business, ask specifically for leads with no
> recent activity despite an open status, and for a per-lead speed-to-lead breakdown
> against a 5-minute benchmark — these two questions surfaced real misses in the source
> and are the reusable core of the audit, not general "how's my pipeline doing" prompts.

## FAQ

**Q:** Is the free Claude plan enough?
**A:** For a single audit, maybe — it burns through fast with real usage. The source
recommends upgrading once it's exhausted rather than working around the limit.

## Conflict History

*None.*

## Presented In

*None yet.*

## Related Concepts

- [[Harvest CRM]]
- [[Conversion Tracking]]
- [[SOPs]]
- [[Managing A VA]]
- [[Leads Engine]]
