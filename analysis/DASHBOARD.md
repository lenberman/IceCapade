# DASHBOARD.md — orchestration

> Registers only — **no findings live here** (findings live in `facets/`, depth in `evidence/`, the log is `git log`). Readable in a few minutes or it has failed. See `ICECAPADE_SUBSTRATE_SPEC.md`.

**Manuscript state:** none — no chapters yet. **Substrate mode:** bootstrap (spec §8). Baseline tag: `v0-scaffold`.

## 1. Coverage map (from `QUESTIONS.md`)

| Question | Consumes | Readiness |
|---|---|---|
| Q-CONT continuity audit | PLAN, BOOK_FACTS, timeline | GAPS — PLAN unseeded, no text |
| Q-NEG negative review | WEAKNESSES, BOOK_FACTS, THEMES | GAPS — no text |
| Q-DEFEND defense | ARCHITECTURE, THEMES, BOOK_FACTS | GAPS — no text |
| Q-CHAR character study | BOOK_FACTS, evidence/Arc_* | GAPS — no text |
| Q-THEME thematic essay | THEMES, ARCHITECTURE, BOOK_FACTS | GAPS — no text |
| Q-COMP comps / placement | POSITIONING, THEMES, BOOK_FACTS | GAPS — POSITIONING may seed from PLAN |
| Q-STRESS reader stress test | READER_EXPERIENCE, BOOK_FACTS | GAPS — no text |
| Q-BLURB jacket copy | POSITIONING, READER_EXPERIENCE, BOOK_FACTS | GAPS — no text |
| Q-PITCH agent/editor pitch | POSITIONING, THEMES, BOOK_FACTS | GAPS — can go PARTIAL once PLAN is seeded |

Facets present (all 7, seeded empty): `PLAN` · `BOOK_FACTS` · `THEMES` · `WEAKNESSES` · `POSITIONING` · `READER_EXPERIENCE` · `ARCHITECTURE`. **Coverage: 0/9 READY — expected at bootstrap; GAPS-for-lack-of-text is not ill health (spec §11).**

**Timeline layer:** dormant. `analysis/IceCapade_timeline.xlsx` does not exist yet; scaffold when the draft has real chronology (USAGE "The timeline").

## 2. Staleness queue

Empty (nothing to go stale).

## 3. Divergence queue (plan vs text — author decisions pending)

Empty.

## 4. Work queue (ranked)

1. **Seed `PLAN.md`** (prompt P) — premise, arc, planned chapter list, opening promises. Everything else keys off this.
2. **Seed `POSITIONING` from PLAN** (marked `basis: plan`) once PLAN exists — flips Q-PITCH/Q-COMP toward PARTIAL.
3. **Ingest chapters as written** (prompt B) — BOOK_FACTS first; READER_EXPERIENCE from the second chapter on.
4. **Scaffold the timeline** when chronology warrants; update tools' sheet-prefix constants in the same pass.

## Tooling
- `python3 tools/anchors.py` — facet anchors + lint (+ timeline once live). Exit 1 only on STALE facet anchors.
- `python3 tools/anchors.py --changed-since <gitref>` — changed chapters + dependent claims/rows.
- Timeline tools (`timeline_export.py`, `timeline_sync.py`, `timeline_scaffold.py`, `build_reader.py`, `timeline_style.py`) — ported from Critique; dormant until the workbook exists.

## 5. Pointers

- Spec: `analysis/ICECAPADE_SUBSTRATE_SPEC.md` · Registry: `analysis/QUESTIONS.md` · How-to: `analysis/USAGE.md`
- Facets: `analysis/facets/` · Evidence: `analysis/evidence/` · Renders: `analysis/renders/` · Reference material: `reference/`
- Manuscript: `html/` (ground truth; exported from `lyx/`) · Change detection: `git diff <ms-tag> -- html/`
- Scaffold tag: `v0-scaffold` · Template project: `~/Critique`
