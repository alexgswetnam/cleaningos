---
description: Capture a correction to Alex's voice and turn it into a rule
argument-hint: "[paste before/after, or point at a file I drafted]"
allowed-tools: Read, Edit, Write, Glob, Grep
---

Learn from a correction. Input: `$ARGUMENTS`

This is how [[Voice]] improves. Descriptions of style are weak; **the diff between what
I wrote and what Alex actually wanted is strong.** Extract it precisely.

## Step 1 — Get both versions

I need the before and the after. If Alex pasted only the corrected version, ask for what
I originally wrote, or find it in the file's git history.

If he gives a correction without a specific text — *"this is too long"*, *"stop using
that word"* — that's still valid. Treat the instruction as the rule and skip to Step 3.

Also accept **old material he wrote himself**. A post that performed well is a
correction waiting to be extracted; compare it against how I would have written the same
thing.

## Step 2 — Diff it properly

Go line by line. Categorize every change:

| Change | Example |
|---|---|
| **Word swap** | "utilize" → "use" |
| **Cut** | An entire hedge or setup sentence deleted |
| **Structure** | Conclusion moved to the front |
| **Register** | Formal → blunt, or explanation → command |
| **Concreteness** | Principle replaced with a consequence or number |
| **Length** | Compression ratio, roughly |

**Ignore changes of fact.** Those aren't voice — they belong in the concept page.

## Step 3 — Extract the rule

State it as something reusable, not a description of this one edit.

- ❌ "Alex changed 'ensure your onboarding is optimized' to 'train them day one or they
  quit in month two'"
- ✅ **"Never state a principle where a consequence will do."**

One rule per correction. If you find three, write three entries — don't fuse them into a
vague meta-rule.

Ask which mode it applies to (`teach`, `walk`, `straight`, `sell`) or whether it's
universal. Don't guess — a rule filed under the wrong mode gets applied everywhere or
nowhere.

## Step 4 — Log it

Prepend to the Voice Log in `Voice/Alex Voice.md`:

```markdown
### YYYY-MM-DD — <what I was writing>
**I wrote:** <verbatim>
**You changed to:** <verbatim>
**Rule:** <the reusable rule>
**Mode:** <teach | walk | straight | sell | universal>
```

Verbatim on both sides. A paraphrased log entry is worthless — the whole value is the
exact wording.

## Step 5 — Promote when a pattern repeats

**Scan the log before writing the new entry.** If this rule (or a near-twin) already
appears twice, it's now a pattern:

1. Write it into the relevant Modes section of `Voice/Alex Voice.md` as a standing rule
2. Mark the log entries `→ promoted`
3. Tell Alex what got promoted

This is what keeps the page useful. **A 200-entry log nobody reads is worse than 12 good
rules.** The log is raw material; the rules are the product.

## Step 6 — Check for conflict

Does this rule contradict something already in `Voice/Alex Voice.md`?

If so, **don't silently overwrite.** Alex's taste may have moved, or the two rules may
apply to different modes. Show both and ask. Same principle as the §X contradiction
protocol — a preference that changed is a supersession, and it should be recorded as one
so we know what changed and when.

## Step 7 — Report

- The rule extracted
- Which mode
- Whether anything got promoted
- Any conflict found

Keep it short. This command runs often and shouldn't feel like a ceremony.
