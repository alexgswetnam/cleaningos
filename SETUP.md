---
title: Setup
---

# CleaningOS — Setup

## Part 1 — Vault and repo

1. Move this folder where it'll live. Not inside iCloud or Dropbox — they fight with
   git over `.git`.
2. Obsidian → Open folder as vault → select `CleaningOS`.
3. Create a **private** GitHub repo. Don't initialize it with anything.

```bash
cd /path/to/CleaningOS
git init && git add . && git commit -m "CleaningOS initial structure"
git branch -M main
git remote add origin https://github.com/YOU/YOUR-REPO.git
git push -u origin main
```

> [!warning] Private, permanently
> Sales call transcripts, student names, and revenue numbers will live here. If you
> ever consider making it public, audit the full history first — git remembers deleted
> files.

## Part 2 — Auto-sync

Obsidian → Settings → Community plugins → **Obsidian Git** → install and enable.

| Setting | Value |
|---|---|
| Vault backup interval | 10 min |
| Auto pull interval | 10 min |
| Pull on startup | on |

Auto-*pull* matters as much as push — it brings ChatGPT's inbox captures down to your
machine.

**Media files:** `.gitignore` excludes `.mp4`, `.mov`, `.wav`. Video belongs in Drive
or Dropbox; the vault holds transcripts and links. A repo full of video becomes
unusable for both AIs.

## Part 3 — Obsidian Skills

```bash
cd /path/to/CleaningOS
git clone https://github.com/kepano/obsidian-skills.git .claude/skills
```

Check that repo's README — layout may have changed. Skill folders should end up under
`.claude/skills/`.

## Part 4 — Fill the Canon *(do this before ingesting anything)*

This is the part that matters and the part it's tempting to skip.

Open these and fill the `<!-- ALEX -->` blocks:

1. `02 Canon/Philosophy.md` — the enemy, the promise, beliefs, teaching style
2. `02 Canon/Five Laws.md` — you have one; name the other four
3. `02 Canon/Four Seasons.md` — you have Survival; name the rest
4. `02 Canon/Four Engines.md` — one paragraph each
5. `02 Canon/Language.md` — resolve the three naming conflicts flagged at the bottom

**Why first:** every page an agent writes inherits its voice and framing from these
files. Ingest 50 sources against an empty Canon and you get 50 pages in generic AI
voice that all need rewriting. Fill the Canon first and the same 50 sources produce
pages that sound like you.

Fastest path: talk it out loud, dump the transcript in `00 Inbox/`, and have me shape
it into the Canon pages. Writing philosophy from a blank page is miserable; editing a
transcript of yourself talking is easy.

## Part 5 — First ingestion

```bash
cd /path/to/CleaningOS
claude
```

```
/ingest "01 Sources/Coaching Calls/your-first-transcript.md"
```

Watch Step 3 closely the first few times — the duplication check is the whole system.
If it's creating pages it should be updating, tighten the wording in `/ingest`.

Do 5–10 sources, then:

```
/lint-vault
```

Early on this mostly reports gaps, which is what you want — it's a content roadmap
derived from your own material.

## Part 6 — Custom GPT

1. **Fine-grained PAT:** GitHub → Settings → Developer settings → Personal access
   tokens → Fine-grained. **Only select repositories** → your vault. Permissions →
   **Contents: Read and write**. Nothing else. 90-day expiry.

2. **Action:** your GPT → Edit → Configure → Create new action. Paste
   `chatgpt/github-action-schema.yaml`. Auth: API Key → **Bearer** → your token.

3. **Instructions:** append the block from `chatgpt/gpt-instructions-block.md`. Don't
   replace what's there.

4. **Test in this order:**
   1. "List files in 03 Concepts/" → read
   2. "Read CONSTITUTION.md" → base64 decode
   3. "Save a note to 00 Inbox saying hello" → create (no sha)
   4. "Add a second line to that note" → **update (sha + base64)** ← the one that breaks

If step 4 throws repeated 409s, ask me for the Cloudflare Worker proxy version.

---

## Daily use

| When | Do | Where |
|---|---|---|
| Idea while driving | "Save to inbox: ..." | Custom GPT |
| Sales call ends | Drop transcript in `01 Sources/Sales Calls/` | Finder |
| Objection you keep hearing | "Add this FAQ to [[Pricing]]" | Custom GPT |
| New coaching call | `/ingest <path>` | Claude Code |
| Inbox piled up | `/process-inbox` | Claude Code |
| Making a video | `/draft youtube script for <concept>` | Claude Code |
| Weekly | `/lint-vault` | Claude Code |

## The failure mode to watch

Not technical. It's concept pages that are really just call summaries wearing a
template — every heading filled, nothing on it you couldn't get from the transcript.

The test: **open a concept page and ask whether someone could run that part of the
business from it alone.** If not, it's documentation, and Rule 4 says the wiki is the
product.

When that starts happening, tighten `_TEMPLATE.md` and the Step 4 instructions in
`/ingest`. Those two files are meant to be edited — they're the tuning knobs.
