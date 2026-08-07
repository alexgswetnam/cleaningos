#!/usr/bin/env python3
"""
Build 03 Concepts/INDEX.md — the search-first map of the vault.

Constitution Rule 2 says "nothing exists twice," which means every agent must
search before creating. Full-text searching 101 concept pages costs thousands of
tokens per session. This generates one file an agent can read once instead.

Source of truth is each page's own `> [!abstract] In one line` block plus its
frontmatter. Nothing here is invented; if a page has no one-liner, it is listed
under Needs A One-Liner rather than summarized.

Usage:  python3 .claude/scripts/build_index.py [vault_root]
"""

import re
import sys
from datetime import date
from pathlib import Path

FOLDERS = ["03 Concepts", "04 Systems"]
ENGINE_ORDER = ["Leads", "Labor", "Logistics", "Leadership"]


def parse(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")

    fm = {}
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if m:
        for line in m.group(1).splitlines():
            if ":" not in line or line.startswith(" "):
                continue
            key, _, val = line.partition(":")
            fm[key.strip()] = val.strip()

    # The one-liner: first non-empty quoted line after the abstract callout.
    one_liner = ""
    m = re.search(r"\[!abstract\][^\n]*\n((?:>[^\n]*\n)+)", text)
    if m:
        body = [re.sub(r"^>\s?", "", l).strip() for l in m.group(1).splitlines()]
        one_liner = " ".join(l for l in body if l).strip()

    def listval(key):
        raw = fm.get(key, "")
        raw = raw.strip("[]")
        return [v.strip() for v in raw.split(",") if v.strip()]

    return {
        "title": path.stem,
        "folder": path.parent.name,
        "one_liner": one_liner,
        "status": fm.get("status", "—"),
        "engines": listval("engine"),
        "seasons": listval("season"),
        "contested": fm.get("contested", "").lower() == "true",
        "superseded": fm.get("superseded", ""),
        "updated": fm.get("updated", ""),
    }


def flags(p: dict) -> str:
    out = []
    if p["status"] not in ("Canonical", "—"):
        out.append(p["status"])
    if p["contested"]:
        out.append("**contested**")
    if p["superseded"]:
        out.append(f"superseded {p['superseded']}")
    return f"  ({', '.join(out)})" if out else ""


def main() -> None:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()

    pages, missing = [], []
    for folder in FOLDERS:
        d = root / folder
        if not d.is_dir():
            continue
        for f in sorted(d.glob("*.md")):
            if f.name == "INDEX.md" or f.name.startswith("_"):
                continue
            p = parse(f)
            (pages if p["one_liner"] else missing).append(p)

    lines = [
        "---",
        "type: index",
        "title: Concept Index",
        "status: Generated",
        f"updated: {date.today().isoformat()}",
        "---",
        "",
        "# Concept Index",
        "",
        "> [!warning] Generated file — do not edit by hand",
        "> Built by `.claude/scripts/build_index.py` from each page's own"
        " `In one line` block and frontmatter.",
        "> Edit the concept page; regenerate this.",
        "",
        "**Read this before creating any page.** Constitution Rule 2: if an idea below"
        " already covers what you're about to write, update that page instead.",
        "",
        f"{len(pages)} pages indexed across {', '.join(FOLDERS)}.",
        "",
        "---",
        "",
    ]

    # Grouped by engine, so an agent can load one engine's slice when that's all it needs.
    buckets = {e: [] for e in ENGINE_ORDER}
    buckets["Unassigned"] = []
    for p in pages:
        placed = False
        for e in p["engines"]:
            if e in buckets:
                buckets[e].append(p)
                placed = True
        if not placed:
            buckets["Unassigned"].append(p)

    for engine in ENGINE_ORDER + ["Unassigned"]:
        group = sorted(buckets[engine], key=lambda x: x["title"])
        if not group:
            continue
        lines.append(f"## {engine}" + (" Engine" if engine in ENGINE_ORDER else ""))
        lines.append("")
        for p in group:
            lines.append(f"- [[{p['title']}]] — {p['one_liner']}{flags(p)}")
        lines.append("")

    if missing:
        lines += ["---", "", "## Needs A One-Liner", "",
                  "These pages have no `In one line` block, so they are invisible to"
                  " search-before-create. Fix at the source.", ""]
        lines += [f"- [[{p['title']}]] ({p['folder']})" for p in sorted(
            missing, key=lambda x: x["title"])]
        lines.append("")

    out = root / "03 Concepts" / "INDEX.md"
    out.write_text("\n".join(lines), encoding="utf-8")

    words = len("\n".join(lines).split())
    print(f"Wrote {out.relative_to(root)}")
    print(f"  {len(pages)} indexed, {len(missing)} missing a one-liner")
    print(f"  ~{words} words (~{int(words * 1.35)} tokens)")


if __name__ == "__main__":
    main()
