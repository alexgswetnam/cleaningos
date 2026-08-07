#!/usr/bin/env python3
"""
Build or refresh 00 Inbox/ingest-run.md — the state file /ingest-all works through.

Idempotent by design. Re-running never resets a file that has already been handled,
so a run that dies halfway (context exhaustion, crash, closed laptop) resumes by
re-scanning and picking up the first `pending` line. That resumability is the whole
reason this is a file on disk and not a list held in an agent's head.

Statuses:
  pending  — not yet attempted
  done     — ingested, result recorded
  parked   — ingested but left a decision for Alex (see review-queue.md)
  skipped  — deliberately not ingested, reason recorded
  failed   — attempted and errored

Usage:  python3 .claude/scripts/build_manifest.py [vault_root]
"""

import re
import sys
import zipfile
from datetime import date
from pathlib import Path

STAGING = "00 Inbox/to-ingest"
MANIFEST = "00 Inbox/ingest-run.md"
TEXTLIKE = {".md", ".txt", ".vtt", ".srt", ".rtf", ".docx", ".pdf", ".csv", ".html"}
MEDIA = {".mp3", ".mp4", ".m4a", ".wav", ".mov", ".aac", ".flac", ".avi", ".mkv"}
IGNORE = {".DS_Store", ".gitkeep", "README.md"}

LINE = re.compile(r"^- \[(?P<mark>.)\] `(?P<name>[^`]+)` — (?P<status>[\w-]+)(?P<rest>.*)$")

# Drive's bulk download stamps every export: "<Name>-20260807T005746Z-1-001.zip".
# Exporting one folder twice (once as .md, once as .txt) yields two zips of the same
# course, which is one source in two formats — not two sources.
EXPORT_STAMP = re.compile(r"-\d{8}T\d{6}Z(?:-\d+)*$")


def course_key(stem: str) -> str:
    return EXPORT_STAMP.sub("", stem).rstrip("_ ").lower().replace("_", " ").strip()


def zip_info(p: Path) -> tuple[int, set]:
    try:
        with zipfile.ZipFile(p) as z:
            names = [m for m in z.namelist() if not m.endswith("/")]
        return len(names), {("." + n.rsplit(".", 1)[-1]).lower()
                            for n in names if "." in n.rsplit("/", 1)[-1]}
    except zipfile.BadZipFile:
        return -1, set()


def scan(staging: Path) -> list[dict]:
    loose, zips = [], {}

    for p in sorted(staging.rglob("*")):
        if not p.is_file() or p.name in IGNORE or p.name.startswith("."):
            continue
        rel = p.relative_to(staging).as_posix()
        ext = p.suffix.lower()

        if ext == ".zip":
            zips.setdefault(course_key(p.stem), []).append(p)
        elif ext in MEDIA:
            mb = p.stat().st_size // (1024 * 1024)
            loose.append({"name": rel, "status": "blocked",
                          "note": f"{ext[1:]} audio/video, {mb}MB — needs a transcript first"})
        elif ext in TEXTLIKE:
            loose.append({"name": rel, "status": "pending",
                          "note": f"{p.stat().st_size // 1024}KB"})
        else:
            loose.append({"name": rel, "status": "pending",
                          "note": f"{ext or 'no ext'}, {p.stat().st_size // 1024}KB"
                                  " — check it's ingestible"})

    found = []
    for key, members in sorted(zips.items()):
        members.sort()
        counts, exts = zip(*(zip_info(m) for m in members)) if members else ((), ())
        allext = sorted({e for s in exts for e in s})
        if len(members) == 1:
            found.append({"name": members[0].relative_to(staging).as_posix(),
                          "status": "pending",
                          "note": f"zip, {counts[0]} files ({','.join(allext)})"})
        else:
            # One entry, all formats listed. The subagent picks the richest format and
            # archives the rest alongside it, the way Every SOP We Use was handled.
            names = " + ".join(m.relative_to(staging).as_posix() for m in members)
            found.append({"name": names, "status": "pending",
                          "note": f"{len(members)} format exports of one course,"
                                  f" {max(counts)} lessons ({','.join(allext)})"})

    return sorted(loose, key=lambda x: x["name"]) + found


def read_existing(manifest: Path) -> dict:
    if not manifest.exists():
        return {}
    out = {}
    for line in manifest.read_text(encoding="utf-8").splitlines():
        m = LINE.match(line.strip())
        if m:
            out[m.group("name")] = line.strip()
    return out


def main() -> None:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    staging = root / STAGING
    manifest = root / MANIFEST

    if not staging.is_dir():
        staging.mkdir(parents=True)
        print(f"Created {STAGING}/ — it's empty. Put source files there.")

    existing = read_existing(manifest)
    found = scan(staging)
    found_names = {f["name"] for f in found}

    lines, counts = [], {"pending": 0, "done": 0, "parked": 0,
                         "skipped": 0, "failed": 0, "blocked": 0}
    for f in found:
        if f["name"] in existing:
            prior = existing[f["name"]]
            lines.append(prior)
            st = LINE.match(prior).group("status")
            counts[st] = counts.get(st, 0) + 1
        else:
            mark = "-" if f["status"] == "blocked" else " "
            lines.append(f"- [{mark}] `{f['name']}` — {f['status']}  ({f['note']})")
            counts[f["status"]] += 1

    # A file handled in a past run but since removed from staging stays on the record.
    gone = [v for k, v in existing.items() if k not in found_names]

    body = [
        "---",
        "type: company",
        "title: Ingest Run",
        "status: Developing",
        f"updated: {date.today().isoformat()}",
        "---",
        "",
        "# Ingest Run",
        "",
        "> [!warning] State file — `/ingest-all` reads and writes this",
        "> Regenerate with `python3 .claude/scripts/build_manifest.py .`. Re-running never"
        " resets a handled file, so an interrupted run resumes from the first `pending`.",
        "",
        f"**{counts['pending']} pending** · {counts['done']} done ·"
        f" {counts['parked']} parked · {counts['skipped']} skipped ·"
        f" {counts['failed']} failed · {counts['blocked']} blocked",
        "",
        f"Staging folder: `{STAGING}/`",
        "",
        "## Queue",
        "",
    ]
    body += lines or ["*Nothing staged.*"]

    if gone:
        body += ["", "## No longer in staging", "",
                 "Handled in a past run, file since removed. Kept as record.", ""]
        body += gone

    body += [
        "",
        "## Status key",
        "",
        "`pending` not yet attempted · `done` ingested · `parked` ingested but a decision"
        " is waiting in [[review-queue|Review Queue]] · `skipped` deliberately not ingested ·"
        " `failed` errored · `blocked` can't be ingested as-is, needs work first",
        "",
        "## Related Concepts",
        "",
        "- [[CONSTITUTION]]",
        "- [[ingestion-queue|Ingestion Queue]]",
        "- [[review-queue|Review Queue]]",
        "",
    ]

    manifest.write_text("\n".join(body), encoding="utf-8")
    print(f"Wrote {MANIFEST}")
    print(f"  {len(found)} staged · {counts['pending']} pending · "
          f"{counts['done']} done · {counts['parked']} parked · {counts['failed']} failed")
    if gone:
        print(f"  {len(gone)} recorded but no longer in staging")


if __name__ == "__main__":
    main()
