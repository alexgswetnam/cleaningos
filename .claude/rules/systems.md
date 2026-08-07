---
paths: "04 Systems/**"
---

# Rules for `04 Systems/`

**Something someone executes.** Sequences, SOPs, workflows, setup procedures, scripts.

Hiring SOP · Automated Hiring Pipeline · Cleaner Availability System · A2P Verification ·
IVR Setup · scheduling · review-request processes — that shape.

Engine hub pages live here too: Leads, Labor, Logistics, Leadership.

## A System links to concepts. It never defines them

If you find yourself explaining *why* something is true on a System page, that explanation
belongs in `03 Concepts/` and this page should link to it. A page in `04–07` that defines an
idea instead of linking to one is a bug — Constitution §V.

## Structure

`04 Systems/_TEMPLATE.md`. Required: frontmatter, Outcome, Use This When, Prerequisites,
Steps, Checklist, Metrics / Done Criteria, Templates & Resources, Sources, Related Concepts.

**Outcome is stated as a result, not an activity.** "Every applicant reaches a decision
within 5 days," not "manage the hiring pipeline."

## Orphaned Systems are worse than orphaned Concepts

Nobody can follow a procedure they can't find. Every System should be reachable from its
Engine hub. Lint checks this.

## After any change

`python3 .claude/scripts/build_index.py .`
