# USAGE — how to run the IceCapade project

A practical how-to. Design rationale: `ICECAPADE_SUBSTRATE_SPEC.md`. Ready-to-paste prompts: `../prompt.txt`. This mirrors Critique's USAGE, adapted for a book being **written**, not one already finished.

## What this project is

A living substrate for the *IceCapade* novel-in-progress. Two jobs:

1. **Continuity keeper.** As you add chapters, it ingests them, keeps the fact/timeline layer current, and flags anything that contradicts the plan or the text so far — immediately, not months later.
2. **Critic on demand.** The Critique question machinery (negative review, stress test, comps, pitch, character study) works on the partial draft at any stage.

## Layout

- `lyx/` — where you write. `html/` — the LyX HTML export, **ground truth**, one file per chapter.
- `reference/` — research/source material the novel draws on. Input only, never anchored.
- `analysis/facets/` — the knowledge layer. `PLAN.md` (intent: arc, planned chapters, open promises) plus the six Critique facets (`BOOK_FACTS`, `THEMES`, `WEAKNESSES`, `POSITIONING`, `READER_EXPERIENCE`, `ARCHITECTURE`) covering the written text.
- `analysis/QUESTIONS.md` — question menu + readiness. `analysis/DASHBOARD.md` — status board; read first in any chat.
- `analysis/evidence/`, `analysis/renders/` — deep reports and dated deliverables, as they accumulate.
- `tools/` — ported from Critique: `anchors.py` (lint), timeline machinery (dormant until the timeline is scaffolded).
- `prompt.txt` — copy-paste prompts (A modify · B new chapter · C ask · D autonomous · P plan · K continuity · T/U timeline).

## Everyday tasks

### Seed or revise the plan
Paste **prompt P**. Bring whatever you have — a synopsis, chapter list, loose notes (drop files in `reference/` if you like). The chat turns it into `PLAN.md` atomic claims and promise entries. This is the natural first session in the project.

### Add a NEW chapter  ← the primary flow
1. Write in `lyx/`, export HTML into `html/` (any new filename).
2. Paste **prompt B**. It detects the untracked file (`git status`, not `git diff`), ingests it (`BOOK_FACTS` first, then interpretive facets), **reconciles it against `PLAN.md`** — paid promises marked with anchors, divergences queued for your decision — runs the lint, commits manuscript and analysis separately, and tags `ms-YYYY-MM-DD`.
3. The lint is the safety net: an un-ingested chapter shows as **MISSING** in BOOK_FACTS coverage.

### Change an existing chapter
Overwrite the file in `html/` (same filename) and paste **prompt A** — diff, targeted re-verification of dependent claims, re-baseline, separate commits, tag. Same as Critique.

### Ask a question / get a deliverable
Paste **prompt C**, naming the question (IDs in `QUESTIONS.md`). Early in the draft most will be GAPS — the entry tells you what's missing. `Q-CONT` (continuity sweep) works as soon as `PLAN` and any text exist.

### Continuity sweep
Paste **prompt K** for a full plan-vs-text-vs-timeline audit with a written report in `renders/`.

## The timeline

Dormant until the book has enough chronology to matter. When it does, a chat scaffolds `analysis/IceCapade_timeline.xlsx` (sheets and calendar conventions defined for this book; the ported tools get their sheet-prefix constants updated in the same pass), and from then on the Critique mechanics apply unchanged: workbook canonical, CSV mirror committed alongside, rows validated by `anchors.py`, prompts T/U for upkeep and approval-gated event extraction.

## Keeping it healthy

- `python3 tools/anchors.py` any time — anchor staleness, BOOK_FACTS coverage, QUESTIONS integrity, timeline (once live). Exit code gates only on stale facet anchors.
- Healthy = staleness queue empty, divergence queue empty or explicitly parked, lint green, every question READY or waiting-on-text (spec §11).

## Cautions

- Same git/Dropbox caution as Critique if this folder ever syncs: one machine at a time, or keep `.git` out of sync and use the remote (`REMOTE_SETUP.md`).
- Run `./commit.sh` from your own terminal, not the sandbox (same reason as Critique: sandbox mounts can't delete git lock files).
