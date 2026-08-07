#!/usr/bin/env python3
"""
Repair wikilinks that got hard-wrapped across a line break.

Agents writing prose at a ~90-character margin will happily wrap mid-link:

    ...one of the four numbers in [[Marketing
    Math]], which drags your average ticket down.

Obsidian does not resolve that. The link is dead, the target loses an inbound
link, and nothing announces it — the page still *looks* linked when you read it.
This is the most invisible failure mode in the vault, which is why it earns a
script instead of a lint note.

Joins the link back onto one line, preserving any blockquote prefix. Refuses to
touch `01 Sources/` (Rule 3) and `02 Canon/` (Canon lock).

Note for anything that also *checks* links: Obsidian resolves `aliases:` declared in
frontmatter, so a filename-only comparison produces false positives. `Voice/Alex
Voice.md` declares `aliases: [Voice]`, which makes every `[[Voice]]` valid.

Usage:
  python3 .claude/scripts/fix_wrapped_links.py [vault_root]           # dry run
  python3 .claude/scripts/fix_wrapped_links.py [vault_root] --write   # apply
"""

import re
import sys
from pathlib import Path

PROTECTED = ("01 Sources", "02 Canon")
SKIP_DIRS = {".git", ".obsidian", ".ts", "99 Scratchpad", "chatgpt", "08 Logs"}
SKIP_FILES = {"_TEMPLATE.md", "CONSTITUTION.md"}  # Constitution's links are illustrative

# [[ ... newline ... ]] with no closing bracket before the break.
WRAPPED = re.compile(r"\[\[([^\]\[\n]*)\n\s*(?:>\s*)?([^\]\[\n]*)\]\]")


def fix(text: str) -> tuple[str, int]:
    n = 0
    while True:
        new, k = WRAPPED.subn(
            lambda m: "[[" + re.sub(r"\s+", " ", f"{m.group(1)} {m.group(2)}").strip() + "]]",
            text)
        if not k:
            return text, n
        text, n = new, n + k


def main() -> None:
    args = sys.argv[1:]
    write = "--write" in args
    root = Path(next((a for a in args if not a.startswith("-")), ".")).resolve()

    total, touched = 0, []
    for p in sorted(root.rglob("*.md")):
        rel = p.relative_to(root)
        if any(d in rel.parts for d in SKIP_DIRS) or p.name in SKIP_FILES:
            continue
        if rel.parts and rel.parts[0] in PROTECTED:
            continue

        text = p.read_text(encoding="utf-8")
        new, n = fix(text)
        if n:
            total += n
            touched.append((rel, n))
            if write:
                p.write_text(new, encoding="utf-8")

    for rel, n in touched:
        print(f"  {n:2d}  {rel}")
    verb = "Repaired" if write else "Would repair"
    print(f"\n{verb} {total} wrapped wikilink(s) across {len(touched)} file(s).")
    if not write and total:
        print("Dry run. Re-run with --write to apply.")


if __name__ == "__main__":
    main()
