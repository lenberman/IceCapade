#!/usr/bin/env python3
"""
timeline_sync.py — one-command currency helper for the timeline workbook.

Runs three steps, in order:

  1. DETECT   — git-diff html/ since a manuscript tag and list the chapters that
                changed (and any brand-new chapter files), then the timeline rows
                (H##/S##) that depend on each changed chapter — printed as a
                ready-to-work checklist with each row's current content.
  2. REFRESH  — rebuild the pre-rendered Reader sheet (tools/build_reader.py) and
                regenerate the CSV mirror (tools/timeline_export.py).
  3. VALIDATE — run tools/anchors.py (chapter resolution, unresolved labels,
                mirror freshness, facet anchors).

What it does NOT do: write or edit event rows. Turning a changed chapter into
corrected dates/summaries/anchors is the human/LLM step — this tool tells you
*which* rows to touch and keeps the Reader + mirror + validation in sync around
that edit. Typical loop:

    python3 tools/timeline_sync.py --since ms-2026-05-24   # see the worklist
    # ...edit the listed rows in analysis/IceCapade_timeline.xlsx...
    python3 tools/timeline_sync.py --since ms-2026-05-24   # refresh + confirm clean

Usage:
  python3 tools/timeline_sync.py --since <gitref>   # e.g. ms-2026-05-24 or a SHA
  python3 tools/timeline_sync.py                    # uses newest ms-* tag if any
  python3 tools/timeline_sync.py --no-refresh       # checklist + validate only
  python3 tools/timeline_sync.py --refresh-only     # skip detection; just rebuild+validate
"""
import os, sys, csv, glob, argparse, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
TLDIR = os.path.join(ROOT, "analysis", "timeline")
sys.path.insert(0, HERE)


def git(*args):
    return subprocess.run(["git", "-C", ROOT, *args],
                          capture_output=True, text=True).stdout.strip()


def basenames(lines):
    return [os.path.splitext(os.path.basename(l))[0]
            for l in lines.splitlines() if l.strip().endswith(".html")]


def newest_ms_tag():
    out = git("tag", "--list", "ms-*", "--sort=-creatordate")
    return out.splitlines()[0].strip() if out else None


def read_chron_rows():
    """All chronology rows from the CSV mirror, with resolved ChapterFile(s)."""
    rows = []
    for fp in sorted(glob.glob(os.path.join(TLDIR, "*.csv"))):
        with open(fp, encoding="utf-8", newline="") as f:
            rd = csv.reader(f); header = next(rd, None)
            if not header or "ChapterFile" not in header:
                continue
            ci = {n: i for i, n in enumerate(header)}
            for r in rd:
                if not any(c.strip() for c in r):
                    continue
                cell = lambda n: r[ci[n]] if n in ci and ci[n] < len(r) else ""
                chs = [t for t in cell("ChapterFile").split(";")
                       if t and not t.startswith("UNRESOLVED")]
                rows.append(dict(id=cell("#"), chapter=cell("Chapter"),
                                 date=cell("Date/Range"), event=cell("Event Summary"),
                                 evidence=cell("Evidence"), chapterfiles=chs))
    return rows


def detect(since):
    if not since:
        print("DETECT: no --since ref and no ms-* tag found.")
        print("        Pass --since <gitref> (e.g. a SHA or tag) to get a change checklist.\n")
        return
    changed = basenames(git("diff", "--name-only", since, "--", "html/"))
    new = basenames(git("ls-files", "--others", "--exclude-standard", "--", "html/"))
    print(f"DETECT (since {since})")
    print(f"  changed chapters: {', '.join(changed) if changed else '(none)'}")
    print(f"  new chapters:     {', '.join(new) if new else '(none)'}")

    if changed:
        rows = read_chron_rows()
        print("\n  Timeline rows to re-verify (edit these in the workbook):")
        any_hit = False
        for ch in changed:
            hits = [r for r in rows if ch in r["chapterfiles"]]
            if not hits:
                continue
            any_hit = True
            print(f"\n  ▼ {ch}")
            for r in hits:
                ev = (r["event"][:96] + "…") if len(r["event"]) > 96 else r["event"]
                print(f"    [ ] {r['id']:5} {r['date']:<22} {ev}")
                if r["evidence"]:
                    print(f"          anchor: {r['evidence'][:90]}")
        if not any_hit:
            print("    (no existing rows depend on the changed chapters)")
    if new:
        print("\n  NEW chapters need rows ADDED to the workbook (then rerun this tool):")
        for ch in new:
            print(f"    [ ] add events for: {ch}")
    print()


def run(label, *cmd):
    print(label); sys.stdout.flush()
    res = subprocess.run([sys.executable, *cmd], cwd=ROOT)
    return res.returncode


def main():
    ap = argparse.ArgumentParser(description="Timeline currency helper (detect + refresh + validate).")
    ap.add_argument("--since", help="git ref/tag to diff html/ against (default: newest ms-* tag)")
    ap.add_argument("--no-refresh", action="store_true", help="skip rebuilding the Reader + mirror")
    ap.add_argument("--refresh-only", action="store_true", help="skip the change checklist")
    args = ap.parse_args()

    # keep our prints in step with subprocess (anchors/export) output
    try:
        sys.stdout.reconfigure(line_buffering=True)
    except Exception:
        pass

    since = args.since or newest_ms_tag()

    if not args.refresh_only:
        detect(since)

    rc = 0
    if not args.no_refresh:
        print("REFRESH")
        try:
            import timeline_style
            n = timeline_style.normalize()
            print(f"  styles normalized: {n} cell(s) restyled to the row-2 template."
                  if n else "  styles uniform (row-2 template).")
        except Exception as e:
            print(f"  style normalization FAILED: {e}"); rc = 1
        try:
            import build_reader
            n = build_reader.build_reader()
            print(f"  Reader rebuilt: {n} cards.")
        except Exception as e:
            print(f"  Reader rebuild FAILED: {e}"); rc = 1
        run("  regenerating CSV mirror…", os.path.join(HERE, "timeline_export.py"))

    print("VALIDATE")
    vc = run("  anchors.py…", os.path.join(HERE, "anchors.py"))

    print("\nDONE." + ("" if (rc == 0 and vc == 0)
                        else "  (check the messages above — a step reported a problem.)"))
    sys.exit(rc or vc)


if __name__ == "__main__":
    main()
