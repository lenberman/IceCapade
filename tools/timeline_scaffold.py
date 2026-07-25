#!/usr/bin/env python3
"""
timeline_scaffold.py — scaffold candidate timeline rows from a chapter's text.

This does the MECHANICAL part of adding timeline events for a changed/new chapter:
it splits the chapter into its scenes (the `______` rules and `### date/heading`
markers the manuscript already uses), and for each scene reports a verbatim
opening-line anchor, any date heading, the known characters it mentions, and a
rough word count. It also shows the timeline rows already on file for the chapter
and the next free row id.

Implicit-break hint: not every scene boundary is marked. Paragraphs that OPEN
inside a scene with a time/location cue ("Later that night…", "Three weeks later…",
"The next morning…", "After dinner…", "In late 2045…") are also reported as
"implicit?" candidates so the drafter can decide whether to split the scene.
A long-scene flag (≥1500 words) makes the candidates extra worth a look. This is
high-recall heuristic — a false positive just adds a line to the output.

It does NOT write rows or invent summaries — that judgment step is the LLM/human's
job (see the "Update Timeline" prompt, prompt.txt block U). Default working
granularity is ONE candidate row per scene; if `implicit?` cues fire, consider
splitting that scene into multiple rows.

Usage:
  python3 tools/timeline_scaffold.py Progress
  python3 tools/timeline_scaffold.py Rescuing.html
  python3 tools/timeline_scaffold.py            # list chapters
"""
import os, re, sys, html, glob, csv

ROOT  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTMLD = os.path.join(ROOT, "html")
TLDIR = os.path.join(ROOT, "analysis", "timeline")

# known character / entity names (heuristic, high-recall; the LLM verifies).
ROSTER = ["Lia", "Kaelen", "Ethan", "Dad", "Granny", "Mother", "Tara", "Renee",
          "Eddie", "Zum", "Aum", "Sam", "Poon", "Eli", "Maya", "Chloe", "George",
          "Raghavan", "Thorne", "Petrova", "Naomi", "Xina", "Mira", "Ms. Aris",
          "Gaia", "Armitage"]
DATE_RE = re.compile(r"\b\d{2,3}-\d{2}(?:-\d{2})?\b")

# heuristic openings that suggest an IMPLICIT scene break (time/location shift
# mid-section, no `____` rule above). Matched case-insensitively at the start
# of a paragraph. High-recall on purpose — the LLM judges; a false positive
# just adds one line to the scaffold output.
TIME_CUE = re.compile(
    r"^("
    r"(later|earlier)( that (night|day|morning|evening|afternoon|week|month|year))?"
    r"|the next (morning|day|night|week|month|year|afternoon|evening)"
    r"|that (night|morning|day|evening|afternoon)"
    r"|(a|the) (next|following) (morning|day|night|evening|afternoon|week|month)"
    r"|(an? )?(few|several|many|two|three|four|five|six|seven|eight|nine|ten)\s+"
    r"(minutes?|hours?|days?|weeks?|months?|years?|decades?)\s+(later|after|earlier|passed)"
    r"|hours? later|days? later|weeks? later|months? later|years? later|decades? later"
    r"|by (the time|then|morning|evening|nightfall|dawn|dusk)"
    r"|when (i|we|they|she|he) (woke|arrived|returned|got back|reached)"
    r"|after (dinner|breakfast|lunch|the meeting|the call|the funeral|that)"
    r"|(eventually|meanwhile|afterwards?|afterward|presently|soon enough)"
    r"|sometime (later|after)"
    r"|that (was|had been) ([a-z]+ ){1,3}ago"
    r"|((early|mid|late) )?(spring|summer|autumn|fall|winter)( of \d{4})?"
    r"|in (january|february|march|april|may|june|july|august|september|october|november|december)"
    r")\b",
    re.IGNORECASE,
)


def flatten_blocks(path):
    """Yield ('head'|'rule'|'p', text) blocks from a chapter's HTML."""
    t = open(path, encoding="utf-8", errors="replace").read()
    t = re.sub(r"<head.*?</head>", "", t, flags=re.S | re.I)
    t = re.sub(r"<h[1-6][^>]*>", "\n\x01HEAD\x01", t, flags=re.I)
    t = re.sub(r"</h[1-6]>", "\n", t, flags=re.I)
    t = re.sub(r"<p[^>]*>", "\n", t, flags=re.I)
    t = re.sub(r"<br[^>]*>", "\n", t, flags=re.I)
    t = re.sub(r"<[^>]+>", "", t)
    t = html.unescape(t)
    for raw in t.split("\n"):
        s = re.sub(r"[ \t]+", " ", raw).strip()
        if not s:
            continue
        if s.startswith("\x01HEAD\x01"):
            yield ("head", s.replace("\x01HEAD\x01", "").strip())
        elif re.fullmatch(r"[_—\-\s]{6,}", s):
            yield ("rule",)
        else:
            yield ("p", s)


def scenes_of(path):
    scenes, cur = [], None
    def newscene(heading=""):
        nonlocal cur
        cur = {"heading": heading, "paras": []}
        scenes.append(cur)
    newscene()
    for blk in flatten_blocks(path):
        if blk[0] == "head":
            newscene(blk[1])
        elif blk[0] == "rule":
            newscene()
        else:
            cur["paras"].append(blk[1])
    return [s for s in scenes if s["paras"] or s["heading"]]


def opening_anchor(body, min_words=7, max_chars=120):
    """First distinctive verbatim span of a scene body (for the Evidence cell)."""
    m = re.match(r"(.+?[.!?])(\s|$)", body)
    sent = m.group(1) if m else body
    if len(sent.split()) < min_words:
        sent = body[:max_chars]
    return sent[:max_chars].strip()


def find_chars(text):
    out = []
    for name in ROSTER:
        pat = re.escape(name) if " " in name or "." in name else r"\b" + re.escape(name) + r"\b"
        if re.search(pat, text):
            out.append(name)
    return out


def chron_index():
    """Return {chapterfile: [(id, sheetfile, date, event)]}, and {sheetfile:set(ids)}."""
    bychap, ids = {}, {}
    for fp in sorted(glob.glob(os.path.join(TLDIR, "*.csv"))):
        with open(fp, encoding="utf-8", newline="") as f:
            rd = csv.reader(f); header = next(rd, None)
            if not header or "ChapterFile" not in header:
                continue
            ci = {n: i for i, n in enumerate(header)}
            sheet = os.path.basename(fp)
            ids.setdefault(sheet, set())
            for r in rd:
                if not any(c.strip() for c in r):
                    continue
                cell = lambda n: r[ci[n]] if n in ci and ci[n] < len(r) else ""
                rid = cell("#"); ids[sheet].add(rid)
                for cf in cell("ChapterFile").split(";"):
                    cf = cf.strip()
                    if cf and not cf.startswith("UNRESOLVED"):
                        bychap.setdefault(cf, []).append(
                            (rid, sheet, cell("Date/Range"), cell("Event Summary")))
    return bychap, ids


def next_free(ids_set, prefix):
    nums = [int(m.group(1)) for i in ids_set
            for m in [re.match(prefix + r"(\d+)", i)] if m]
    return f"{prefix}{(max(nums) + 1) if nums else 1}"


def main():
    if len(sys.argv) < 2:
        chs = sorted(os.path.splitext(os.path.basename(p))[0] for p in glob.glob(os.path.join(HTMLD, "*.html")))
        print("usage: python3 tools/timeline_scaffold.py <Chapter>\nchapters: " + ", ".join(chs))
        sys.exit(0)
    ch = os.path.splitext(os.path.basename(sys.argv[1]))[0]
    path = os.path.join(HTMLD, ch + ".html")
    if not os.path.exists(path):
        print(f"no such chapter file: {path}"); sys.exit(2)

    bychap, ids = chron_index()
    existing = bychap.get(ch, [])
    sheets = sorted({s for _, s, _, _ in existing})
    print(f"=== SCAFFOLD: {ch} ===")
    if existing:
        print(f"already on the timeline in: {', '.join(sheets)}")
        for rid, sh, date, ev in existing:
            print(f"   {rid:5} {date:<26} {ev[:70]}")
    else:
        print("not yet on the timeline (new chapter).")
    # suggest next ids for both id-spaces
    allids = set().union(*ids.values()) if ids else set()
    print(f"next free ids — Slow Mend: {next_free(allids,'S')} · Historical: {next_free(allids,'H')}")
    print("   (Book-2/2154 events -> S ids on 'Slow Mend'; historical -> H ids on 'Historical')")

    scenes = scenes_of(path)
    print(f"\n{len(scenes)} scene(s) split on explicit ____/### markers. "
          f"Default: one candidate row per scene\n"
          f"(merge trivial ones; SPLIT scenes whose `implicit?` line lists time-cues — "
          f"those usually mark a hidden scene break that the manuscript didn't punctuate). "
          f"Confirm before writing:\n")
    LONG = 1500
    for i, s in enumerate(scenes, 1):
        body = " ".join(s["paras"])
        if not body.strip() and not s["heading"]:
            continue
        wc = len(body.split())
        head = s["heading"]
        date = ", ".join(DATE_RE.findall(head)) or (", ".join(DATE_RE.findall(body[:120])) or "—")
        chars = find_chars(head + " " + body) or ["(none detected)"]
        # implicit-break detection: report up to a handful of paragraph indices
        # whose opening matches a time-cue pattern. Skip paragraph 1 (it IS the
        # scene opening).
        implicit = []
        for pi, para in enumerate(s["paras"][1:], start=2):
            m = TIME_CUE.match(para)
            if m:
                implicit.append((pi, m.group(0), opening_anchor(para, max_chars=80)))
            if len(implicit) >= 6:
                break
        long_flag = "  ⟵ long scene; check for implicit breaks" if wc >= LONG else ""
        print(f"SCENE {i}" + (f'  heading: "{head}"' if head else "") + f"   ~{wc} words{long_flag}")
        print(f"   date?      {date}")
        print(f"   characters {', '.join(chars)}")
        print(f"   anchor     \"{opening_anchor(body) if body else head}\"")
        if implicit:
            print(f"   implicit?  {len(implicit)} paragraph(s) open with a time/location cue "
                  f"— consider splitting:")
            for pi, cue, anchor in implicit:
                print(f"        ¶{pi:>3}  [{cue}]  \"{anchor}\"")
        print()


if __name__ == "__main__":
    main()
