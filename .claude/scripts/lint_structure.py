#!/usr/bin/env python3
"""
Structural lint for CleaningOS. Mechanical checks only — the judgment calls
live in .claude/skills/lint-vault/SKILL.md.

Usage:  python3 .claude/scripts/lint_structure.py .
Exit 1 if any ERROR-level finding is present.

Deliberately NOT checked (retired 2026-08-07, v2 refactor):
  - pages with fewer than five outbound links     -> there is no minimum
  - ingestions that didn't touch enough pages     -> there is no quota
  - missing optional template sections            -> they are optional
These measured volume, not health.
"""
import os, re, sys, subprocess
from collections import defaultdict

ENGINES = {"Leads", "Labor", "Logistics", "Leadership"}
SEASONS = {"Survival", "Stability", "Scale", "Harvest"}
KNOWLEDGE = ["02 Canon", "03 Concepts", "04 Systems", "05 Products", "06 Marketing",
             "07 Company", "09 Derived"]
FOLDER_TYPE = {"02 Canon": "canon", "03 Concepts": "concept", "04 Systems": "system",
               "05 Products": "product", "06 Marketing": "marketing", "07 Company": "company"}
# pages allowed to sit in a folder without matching its type
TYPE_EXEMPT = {"03 Concepts/INDEX.md"}
# structural filenames that legitimately repeat across the tree
NAME_EXEMPT = {"README", "SKILL", "_TEMPLATE", "index"}
SOURCES = "01 Sources"

errors, warns = [], []
def err(cat, msg): errors.append((cat, msg))
def warn(cat, msg): warns.append((cat, msg))

root = sys.argv[1] if len(sys.argv) > 1 else "."
os.chdir(root)

# ---------- collect ----------
pages, names, aliases = {}, set(), {}
for base, dirs, files in os.walk("."):
    if "/.git" in base or base.startswith("./.git"):
        continue
    for f in files:
        if not f.endswith(".md"):
            continue
        p = os.path.normpath(os.path.join(base, f))
        try:
            t = open(p, encoding="utf-8").read()
        except Exception:
            continue
        pages[p] = t
        names.add(f[:-3])
        m = re.search(r"^aliases:\s*\[(.*?)\]", t, re.M)
        if m:
            for a in m.group(1).split(","):
                a = a.strip().strip("\"'")
                if a:
                    aliases[a] = p
                    names.add(a)

def fm(t, key):
    m = re.search(r"^%s:\s*(.*)$" % key, t, re.M)
    return m.group(1).strip() if m else None

def in_knowledge(p):
    return any(p.startswith(k + "/") for k in KNOWLEDGE)

# ---------- 1. duplicate titles ----------
by_name = defaultdict(list)
for p in pages:
    by_name[os.path.basename(p)[:-3]].append(p)
for n, ps in sorted(by_name.items()):
    if len(ps) < 2 or n in NAME_EXEMPT:
        continue
    outside = [x for x in ps if not x.startswith(SOURCES) and not x.startswith(".claude")]
    if len(outside) > 1:
        err("duplicate-title", "%s -> %s" % (n, ", ".join(outside)))
    elif len(outside) == 1:
        warn("duplicate-title", "%s in %s collides with a source file (\u00a7VI) -> %s"
             % (n, outside[0], ", ".join(x for x in ps if x != outside[0])))

# ---------- 2. ambiguous Harvest CRM ----------
hc = [x for x in by_name.get("Harvest CRM", []) if not x.startswith(SOURCES)]
if len(hc) > 1:
    err("harvest-crm", "[[Harvest CRM]] has %d targets: %s" % (len(hc), ", ".join(hc)))

# ---------- 3. broken wikilinks ----------
for p, t in sorted(pages.items()):
    if not in_knowledge(p) or p.endswith("_TEMPLATE.md"):
        continue
    for l in set(re.findall(r"\[\[([^\]|#\n]+)", t)):
        l = l.strip()
        if l and l not in names:
            err("broken-link", "%s -> [[%s]]" % (p, l))

# ---------- 4. wrapped wikilinks ----------
for p, t in sorted(pages.items()):
    if not in_knowledge(p):
        continue
    if re.search(r"\[\[[^\]\n]*\n[^\]\n]*\]\]", t):
        err("wrapped-link", "%s has a wikilink broken across a line break" % p)

# ---------- 5. engine / season / type ----------
for p, t in sorted(pages.items()):
    if not in_knowledge(p) or p.endswith("_TEMPLATE.md"):
        continue
    rel = p
    for key, valid in (("engine", ENGINES), ("season", SEASONS)):
        raw = fm(t, key)
        if raw and raw.startswith("["):
            for v in [x.strip() for x in raw.strip("[]").split(",") if x.strip()]:
                if v not in valid:
                    err("invalid-%s" % key, "%s -> '%s'" % (rel, v))
    folder = rel.split("/")[0]
    want = FOLDER_TYPE.get(folder)
    got = fm(t, "type")
    if want and got and got != want and rel not in TYPE_EXEMPT:
        if not (folder == "07 Company" and got in ("company", "index")):
            err("type-folder", "%s is in %s but declares type: %s" % (rel, folder, got))

# ---------- 6. canonical pages with no sources ----------
for p, t in sorted(pages.items()):
    if not in_knowledge(p) or p.endswith("_TEMPLATE.md"):
        continue
    if fm(t, "status") == "Canonical" and not p.startswith("09 Derived"):
        s = fm(t, "sources")
        if s in (None, "[]", ""):
            warn("unsourced-canonical", "%s is Canonical with empty sources:" % p)

# ---------- 7. derived material cited as proof ----------
derived = set()
man = "09 Derived/Derived Source Manifest.md"
if os.path.exists(man):
    for m in re.findall(r"^\| `([^`]+\.md)` \|", open(man, encoding="utf-8").read(), re.M):
        derived.add(m[:-3])
for p, t in sorted(pages.items()):
    if not in_knowledge(p) or p.startswith("09 Derived"):
        continue
    for l in set(re.findall(r"\[\[([^\]|#\n]+)", t)):
        if l.strip() in derived:
            warn("derived-as-source", "%s links [[%s]], which is an AI summary" % (p, l.strip()))

# ---------- 8. orphaned systems ----------
inbound = defaultdict(int)
for p, t in pages.items():
    if p.startswith("08 Logs") or p.startswith("99"):
        continue
    for l in set(re.findall(r"\[\[([^\]|#\n]+)", t)):
        inbound[l.strip()] += 1
for p in sorted(pages):
    if p.startswith("04 Systems/") and not p.endswith("_TEMPLATE.md"):
        n = os.path.basename(p)[:-3]
        if inbound.get(n, 0) == 0:
            err("orphan-system", "%s has no inbound links — nobody can find this procedure" % p)

# ---------- 9. contested / superseded hygiene ----------
for p, t in sorted(pages.items()):
    if not in_knowledge(p):
        continue
    if "[!warning] Contested" in t and "What would settle it" not in t:
        err("contested-no-test", "%s has a Contested callout with no 'What would settle it'" % p)
    for blk in re.findall(r"\[!failure\]-?[^\n]*\n((?:>[^\n]*\n)+)", t):
        if "Reason:" not in blk and "**Reason:**" not in blk:
            warn("supersede-no-reason", "%s has a Superseded block with no Reason" % p)

# ---------- 10. sources modified after ingestion ----------
try:
    out = subprocess.run(["git", "diff", "--name-status", "HEAD", "--", "01 Sources"],
                         capture_output=True, text=True, timeout=30).stdout
    for line in out.strip().splitlines():
        if line.startswith("M"):
            err("source-modified", "%s modified — 01 Sources/ is immutable" % line.split("\t", 1)[-1])
except Exception:
    pass

# ---------- 11. customer-facing claims without a register status ----------
reg = "07 Company/Claim Register.md"
reg_text = open(reg, encoding="utf-8").read() if os.path.exists(reg) else ""
money = re.compile(r"\$\s?([\d,]+(?:\.\d+)?)\s*([kK])?")

def canon_amounts(text):
    """Every dollar figure in `text`, normalised to an integer number of dollars."""
    out = set()
    for num, k in money.findall(text):
        try:
            v = float(num.replace(",", ""))
        except ValueError:
            continue
        if k:
            v *= 1000
        if v >= 1:                       # $0 is never a claim
            out.add(int(v))
    return out

registered = canon_amounts(reg_text)
for p, t in sorted(pages.items()):
    if not (p.startswith("05 Products/") or p.startswith("06 Marketing/")):
        continue
    body = re.sub(r"^---.*?^---", "", t, flags=re.S | re.M)
    # inline code spans quote source titles and file names, not claims
    body = re.sub(r"`[^`\n]*`", " ", body)
    for amt in sorted(canon_amounts(body) - registered):
        warn("unregistered-claim",
             "%s states $%s with no matching row in the Claim Register" % (p, format(amt, ",")))

# ---------- report ----------
def group(items):
    d = defaultdict(list)
    for c, m in items:
        d[c].append(m)
    return d

print("CleaningOS structural lint\n" + "=" * 60)
for label, items in (("ERROR", errors), ("WARN", warns)):
    g = group(items)
    total = sum(len(v) for v in g.values())
    print("\n%s — %d" % (label, total))
    if not total:
        print("  none")
    for cat in sorted(g):
        print("  [%s] %d" % (cat, len(g[cat])))
        for m in sorted(g[cat])[:25]:
            print("     - %s" % m)
        if len(g[cat]) > 25:
            print("     ... and %d more" % (len(g[cat]) - 25))
print("\n" + "=" * 60)
print("%d pages checked. %d errors, %d warnings." % (len(pages), len(errors), len(warns)))
sys.exit(1 if errors else 0)
