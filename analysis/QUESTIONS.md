# QUESTIONS.md — registry of answerable question types

> The yardstick for the substrate. One entry per question type: what a good answer needs, which facets it consumes, current readiness. Add entries (and any facet they require) as new question types come up. See `ICECAPADE_SUBSTRATE_SPEC.md` §5.

Readiness values: **READY** · **PARTIAL** (consumable but a facet is thin or plan-based) · **GAPS** (a consumed facet is missing or empty).

Manuscript state these calls are made against: **none — bootstrap, no chapters yet.** Every entry below is GAPS for lack of text; that is expected, not ill health (spec §11).

---

### Q-CONT — Continuity audit  ← new relative to Critique
- needs: the plan (arc, promises); the facts of the written text; the timeline once live
- consumes: `PLAN` (primary), `BOOK_FACTS`, timeline
- renders: `renders/Continuity_<date>.md`; also runs implicitly on every prompt-B ingest (spec §7.1)
- readiness: **GAPS** — PLAN unseeded, no text. Becomes READY as soon as PLAN and any chapter exist.

### Q-NEG — Negative review (adversarial stress-test)
- needs: honest weakness model; facts to ground each charge; current text for quotes
- consumes: `WEAKNESSES` (primary), `BOOK_FACTS`, `THEMES`
- renders: `renders/Review_Negative_<date>.md`
- readiness: **GAPS** — no text. Audience/register parameterization (Critique spec §6.1) deferred until WEAKNESSES carries a matrix.

### Q-COMP — Comparable titles / shelf placement
- consumes: `POSITIONING` (primary), `THEMES`, `BOOK_FACTS`
- readiness: **GAPS** — can reach PARTIAL from a seeded PLAN-based POSITIONING (`basis: plan` entries).

### Q-STRESS — Unprepared-reader stress test
- consumes: `READER_EXPERIENCE` (primary), `BOOK_FACTS`
- readiness: **GAPS** — meaningful from roughly the second chapter on.

### Q-DEFEND — Positive case / defense
- consumes: `ARCHITECTURE`, `THEMES`, `BOOK_FACTS`
- readiness: **GAPS** — no text.

### Q-BLURB — Jacket copy / blurb
- consumes: `POSITIONING`, `READER_EXPERIENCE`, `BOOK_FACTS`
- readiness: **GAPS** — no text.

### Q-PITCH — Agent/editor pitch
- consumes: `POSITIONING`, `THEMES`, `BOOK_FACTS`
- readiness: **GAPS** — reaches PARTIAL once PLAN seeds POSITIONING (a pitch can render from intent, clearly labeled).

### Q-CHAR — Character study
- consumes: `BOOK_FACTS`, `evidence/Arc_<character>.md`, timeline
- readiness: **GAPS** — no text.

### Q-THEME — Thematic essay
- consumes: `THEMES` (primary), `ARCHITECTURE`, `BOOK_FACTS`, timeline
- readiness: **GAPS** — no text.

---

**Coverage at bootstrap:** 0 READY · 0 PARTIAL · 9 GAPS (all for lack of text). First flips: Q-CONT on PLAN + first chapter; Q-PITCH/Q-COMP to PARTIAL on PLAN-seeded POSITIONING.
