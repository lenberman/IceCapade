#!/usr/bin/env python3
"""
anchors.py — validate the substrate's quote-canonical anchors against the manuscript.

Anchors in analysis/facets/*.md look like:   "verbatim phrase" (Chapter)
where Chapter is an html/ basename (Logic, Rescuing, FrontMatter, ...).

For each anchor this tool finds the quoted phrase in the current chapter HTML and reports:
  OK        phrase present verbatim (after smart-quote normalization)  -> prints current line
  REWORDED  phrase mostly present (word-overlap >= 0.6) but changed     -> re-read the claim
  STALE     phrase not found (passage cut/rewritten, or anchor wrong)   -> re-derive / fix anchor

Exit code: 0 if no STALE anchors; 1 if any STALE (so it can gate a commit / CI).

Also runs spec-§10 lint: every chapter covered by BOOK_FACTS; every QUESTIONS `consumes` facet exists.

It also validates the TIMELINE layer (analysis/timeline/*.csv, the diff-able mirror of
IceCapade_timeline.xlsx produced by tools/timeline_export.py): every chronology row resolves
to a real html/ chapter, the mirror is not stale relative to the workbook, and (with
--timeline-quotes) verbatim quotes in the rows are checked against the manuscript. Timeline
row dependencies are folded into --changed-since so a chapter edit lists the H##/S## rows that
may need re-checking. Timeline findings are reported but do NOT gate the exit code (only facet
STALE anchors do); the timeline carries known content gaps that shouldn't block a commit.

Usage:
  python3 tools/anchors.py                 # validate all facet anchors + lint + timeline
  python3 tools/anchors.py --quiet         # summary table only
  python3 tools/anchors.py --facet WEAKNESSES
  python3 tools/anchors.py --timeline-quotes   # also spot-check verbatim quotes in timeline rows
  python3 tools/anchors.py --changed-since v1-architectural-critique   # changed chapters + affected facet/timeline rows
"""
import os, re, sys, html, glob, csv, argparse, subprocess
from collections import defaultdict

ROOT   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTMLD  = os.path.join(ROOT, "html")
FACETD = os.path.join(ROOT, "analysis", "facets")
QFILE  = os.path.join(ROOT, "analysis", "QUESTIONS.md")
BOOKFACTS = os.path.join(FACETD, "BOOK_FACTS.md")
TLDIR  = os.path.join(ROOT, "analysis", "timeline")            # CSV mirror of the timeline workbook
TLXLSX = os.path.join(ROOT, "analysis", "IceCapade_timeline.xlsx")

# ---------- normalization ----------
_TRANS = {0x2018:"'",0x2019:"'",0x201c:'"',0x201d:'"',0x2013:"-",0x2014:"-",0x2026:"...",0x00a0:" "}
def norm(s):
    s = html.unescape(s).translate(_TRANS).lower()
    return re.sub(r"\s+", " ", s).strip()

def strip_tags(line):
    line = re.sub(r"<!--.*?-->", "", line)
    return re.sub(r"<[^>]+>", " ", line)

# ---------- chapter index ----------
def chapters():
    return {os.path.splitext(os.path.basename(p))[0]: p
            for p in glob.glob(os.path.join(HTMLD, "*.html"))}

def build_index(path):
    """return (flat_normalized_text, [(char_offset,line)...], [(word,line)...])"""
    flat=[]; off=0; mp=[]; words=[]
    with open(path, encoding="utf-8", errors="replace") as f:
        for i, line in enumerate(f, 1):
            t = norm(strip_tags(line))
            if t:
                mp.append((off, i)); flat.append(t+" "); off += len(t)+1
                for w in t.split():
                    words.append((w, i))
    return "".join(flat), mp, words

def line_at(mp, pos):
    best = mp[0][1] if mp else 0
    for o, ln in mp:
        if o <= pos: best = ln
        else: break
    return best

def fuzzy(words, phrase):
    pw = [w for w in norm(phrase).split() if len(w) >= 4]
    T = set(pw)
    if not T: return (0.0, None)
    L = max(len(pw), 4); n = len(words); best = 0.0; bestln = None
    for i in range(max(0, n-1)):
        win = words[i:i+L]
        r = len({w for w,_ in win} & T) / len(T)
        if r > best:
            best, bestln = r, win[0][1]
            if best == 1.0: break
    return (best, bestln)

def locate(idx, phrase):
    flat, mp, words = idx
    p = norm(phrase)
    if len(p) < 4: return ("skip", None, None)
    if p in flat:
        return ("ok", line_at(mp, flat.find(p)), 1.0)
    r, ln = fuzzy(words, phrase)
    if r >= 0.85: return ("ok", ln, r)
    if r >= 0.60: return ("reworded", ln, r)
    return ("stale", None, r)

# ---------- anchor extraction ----------
# "phrase" (Chapter[, extra])   -- chapter must be a known html basename
ANCHOR_RE = re.compile(r'"([^"]{4,}?)"\s*\(([^)]*)\)')
HEAD_RE   = re.compile(r'^#{2,4}\s+([A-Z]+-\d+|\S.*)')

def extract_anchors(md_path, chapset):
    out = []  # (claim_id, chapter, phrase)
    claim = "(file)"
    for raw in open(md_path, encoding="utf-8", errors="replace"):
        h = re.match(r'^###\s+([A-Za-z]+-\d+)', raw)
        if h: claim = h.group(1)
        for m in ANCHOR_RE.finditer(raw):
            phrase, paren = m.group(1), m.group(2)
            # find a known chapter token in the parenthetical
            ch = None
            for tok in re.findall(r'[A-Za-z_]+', paren):
                if tok in chapset:
                    ch = tok; break
            if ch:
                out.append((claim, ch, phrase))
    return out

# ---------- timeline (CSV mirror of the workbook) ----------
def read_timeline():
    """Read the chronology CSVs. Returns (rows, mirror_files).
    rows = [ {sheet, id, chapter_label, chapterfiles:[...], unresolved:[...],
              summary, evidence, raw_row} ]  -- only for sheets that carry ChapterFile."""
    rows = []; files = sorted(glob.glob(os.path.join(TLDIR, "*.csv")))
    for fp in files:
        with open(fp, encoding="utf-8", errors="replace", newline="") as f:
            rd = csv.reader(f); header = next(rd, None)
            if not header or "ChapterFile" not in header:
                continue                      # Cross-References / Flagged Entries: no chapter anchor
            ci = {name: i for i, name in enumerate(header)}
            cf = ci["ChapterFile"]
            for r in rd:
                if not any(c.strip() for c in r): continue
                cell = lambda n: r[ci[n]] if n in ci and ci[n] < len(r) else ""
                resolved, unresolved = [], []
                for tok in (r[cf] if cf < len(r) else "").split(";"):
                    tok = tok.strip()
                    if not tok: continue
                    if tok.startswith("UNRESOLVED:"): unresolved.append(tok[len("UNRESOLVED:"):])
                    else: resolved.append(tok)
                rows.append(dict(sheet=os.path.basename(fp), id=cell("#"),
                                 chapter_label=cell("Chapter"), chapterfiles=resolved,
                                 unresolved=unresolved, summary=cell("Event Summary"),
                                 evidence=cell("Evidence")))
    return rows, files

# pull out verbatim-looking quoted spans (>=5 words of real prose) from a cell
_QUOTE_RE = re.compile(r'["“”]([^"“”]{12,}?)["“”]')
def quoted_spans(text):
    out = []
    for m in _QUOTE_RE.finditer(text or ""):
        ph = m.group(1).strip()
        words = [w for w in re.findall(r"[A-Za-z']+", ph) if len(w) >= 3]
        if len(words) >= 5 and "..." not in ph and "…" not in ph:
            out.append(ph)
    return out

# ---------- main ----------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("--facet", help="limit to one facet (basename without .md)")
    ap.add_argument("--timeline-quotes", action="store_true", help="spot-check verbatim quotes in timeline rows against the manuscript")
    ap.add_argument("--changed-since", metavar="GITREF", help="also list html chapters changed since a git ref")
    args = ap.parse_args()

    chapset = chapters()
    idx_cache = {}
    def idx(ch):
        if ch not in idx_cache: idx_cache[ch] = build_index(chapset[ch])
        return idx_cache[ch]

    facet_files = sorted(glob.glob(os.path.join(FACETD, "*.md")))
    if args.facet:
        facet_files = [f for f in facet_files if os.path.splitext(os.path.basename(f))[0] == args.facet]

    totals = defaultdict(int)
    stale_rows = []; reworded_rows = []
    print("== ANCHOR VALIDATION ==")
    for fp in facet_files:
        fname = os.path.basename(fp)
        anchors = extract_anchors(fp, chapset)
        c = defaultdict(int); rows = []
        for claim, ch, phrase in anchors:
            status, ln, ratio = locate(idx(ch), phrase)
            c[status] += 1; totals[status] += 1
            short = (phrase[:60] + "...") if len(phrase) > 60 else phrase
            if status == "stale":
                stale_rows.append((fname, claim, ch, short, ratio))
            elif status == "reworded":
                reworded_rows.append((fname, claim, ch, ln, ratio, short))
            rows.append((claim, ch, status, ln, ratio, short))
        print(f"  {fname:24s} anchors={len(anchors):3d}  ok={c['ok']:3d}  reworded={c['reworded']:3d}  stale={c['stale']:3d}")
        if not args.quiet:
            for claim, ch, status, ln, ratio, short in rows:
                if status == "ok": continue
                tag = "STALE" if status=="stale" else "REWORDED"
                print(f"      [{tag} {ratio:.0%}] {claim} ({ch}) {'~L'+str(ln) if ln else ''}  \"{short}\"")

    print(f"\n  TOTAL  ok={totals['ok']}  reworded={totals['reworded']}  stale={totals['stale']}")

    if reworded_rows:
        print("\n-- REWORDED (re-read these claims) --")
        for fname, claim, ch, ln, ratio, short in reworded_rows:
            print(f"  {claim:8s} {fname:22s} ({ch} ~L{ln}, {ratio:.0%})  \"{short}\"")
    if stale_rows:
        print("\n-- STALE (re-derive or fix anchor) --")
        for fname, claim, ch, short, ratio in stale_rows:
            print(f"  {claim:8s} {fname:22s} ({ch})  \"{short}\"")

    # ---------- lint (spec §10) ----------
    print("\n== LINT ==")
    # every chapter covered by BOOK_FACTS?
    if os.path.exists(BOOKFACTS):
        bf = open(BOOKFACTS, encoding="utf-8", errors="replace").read()
        missing = [ch for ch in chapset if ch != "FrontMatter" and ch not in bf]
        print(f"  BOOK_FACTS chapter coverage: {'all '+str(max(0,len(chapset)-1))+' chapters referenced' if not missing else 'MISSING: '+', '.join(sorted(missing))}")
    # every QUESTIONS consumes-facet exists?
    if os.path.exists(QFILE):
        q = open(QFILE, encoding="utf-8", errors="replace").read()
        named = set(re.findall(r'`([A-Z_]+)`', q))
        facet_names = {os.path.splitext(os.path.basename(f))[0] for f in glob.glob(os.path.join(FACETD,'*.md'))}
        ghost = [n for n in named if n.isupper() and n.endswith(tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ")) and n in {
            'BOOK_FACTS','THEMES','WEAKNESSES','POSITIONING','READER_EXPERIENCE','ARCHITECTURE'} and n not in facet_names]
        print(f"  QUESTIONS consumes-facets present: {'yes' if not ghost else 'MISSING: '+', '.join(ghost)}")

    # ---------- timeline layer ----------
    tl_rows, tl_files = read_timeline()
    print("\n== TIMELINE ==")
    if not tl_files:
        print("  (no CSV mirror found — run `python3 tools/timeline_export.py`)")
    else:
        # mirror freshness: workbook newer than the newest CSV => regenerate
        if os.path.exists(TLXLSX) and tl_files:
            newest_csv = max(os.path.getmtime(f) for f in tl_files)
            if os.path.getmtime(TLXLSX) > newest_csv + 1:
                print("  MIRROR STALE: IceCapade_timeline.xlsx is newer than analysis/timeline/*.csv")
                print("                regenerate with `python3 tools/timeline_export.py`")
        # coverage: every chronology row resolves to a real chapter
        bad_chap = [(r["id"], cf) for r in tl_rows for cf in r["chapterfiles"] if cf not in chapset]
        unresolved = [(r["id"], r["chapter_label"]) for r in tl_rows if r["unresolved"]]
        print(f"  chronology rows: {len(tl_rows)} (in {sum(1 for f in tl_files if 'Cross' not in f and 'Flagged' not in f)} sheets)")
        if bad_chap:
            print("  CHAPTER RESOLVES TO MISSING FILE: " + ", ".join(f"{i}->{c}" for i, c in bad_chap))
        else:
            print("  chapter resolution: all resolved rows point at real html/ chapters")
        if unresolved:
            print(f"  UNRESOLVED chapter labels ({len(unresolved)} rows — content gap, non-gating):")
            for i, lab in unresolved:
                print(f"      {i}: \"{lab}\"")
        else:
            print("  unresolved labels: none")
        # optional verbatim-quote spot check
        if args.timeline_quotes:
            tq = defaultdict(int); flagged = []
            for r in tl_rows:
                if not r["chapterfiles"]: continue
                for span in quoted_spans(r["summary"]) + quoted_spans(r["evidence"]):
                    # try each chapter the row depends on; best status wins
                    best = ("stale", None, 0.0)
                    for ch in r["chapterfiles"]:
                        if ch not in chapset: continue
                        st, ln, ratio = locate(idx(ch), span)
                        if (ratio or 0) > (best[2] or 0): best = (st, ln, ratio or 0)
                    tq[best[0]] += 1
                    if best[0] != "ok":
                        flagged.append((r["id"], best[0], best[2], span[:55]))
            print(f"  quote spot-check: ok={tq['ok']}  reworded={tq['reworded']}  stale={tq['stale']}  (informational, non-gating)")
            for i, st, ratio, span in flagged[:40]:
                print(f"      [{st.upper()} {ratio:.0%}] {i}  \"{span}\"")

    if args.changed_since:
        try:
            # modified/deleted tracked chapters (working tree vs ref)
            out = subprocess.run(["git","-C",ROOT,"diff","--name-only",args.changed_since,"--","html/"],
                                 capture_output=True, text=True, check=True).stdout
            ch = [os.path.splitext(os.path.basename(l))[0] for l in out.splitlines() if l.strip()]
            # NEW chapters are untracked, so git diff won't show them — find separately
            unt = subprocess.run(["git","-C",ROOT,"ls-files","--others","--exclude-standard","--","html/"],
                                 capture_output=True, text=True).stdout
            new_ch = [os.path.splitext(os.path.basename(l))[0] for l in unt.splitlines() if l.strip().endswith(".html")]
            print(f"\n== CHANGED SINCE {args.changed_since} ==")
            print(f"  modified: {', '.join(ch) if ch else '(none)'}")
            print(f"  NEW (untracked — needs ingest, not just re-verify): {', '.join(new_ch) if new_ch else '(none)'}")
            if ch:
                hits = defaultdict(list)
                for fp in glob.glob(os.path.join(FACETD,"*.md")):
                    for claim, c, phrase in extract_anchors(fp, chapset):
                        if c in ch: hits[c].append(f"{os.path.basename(fp)}:{claim}")
                for c in ch:
                    if hits[c]: print(f"  {c}: anchors to re-verify -> {', '.join(sorted(set(hits[c])))}")
                # timeline rows that depend on a changed chapter
                tl_hits = defaultdict(list)
                for r in tl_rows:
                    for cf in r["chapterfiles"]:
                        if cf in ch: tl_hits[cf].append(r["id"])
                for c in ch:
                    if tl_hits[c]:
                        print(f"  {c}: timeline rows to re-check -> {', '.join(tl_hits[c])}")
            if new_ch:
                print(f"  -> for NEW chapters: read them and EXTEND the facets (BOOK_FACTS first); see prompt B.")
                print(f"  -> also add the new chapter's events to the timeline workbook, then re-run timeline_export.py.")
        except Exception as e:
            print(f"  (git step failed: {e})")

    sys.exit(1 if totals['stale'] else 0)

if __name__ == "__main__":
    main()
