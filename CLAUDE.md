# IceCapade — working rules for any chat in this folder

Novel in progress. Manuscript lives in `lyx/`. Research, outlines and staged suggestions live in `reference/`. Read this before touching anything.

## Manuscript structure

- `lyx/IceCapades.lyx` is the **master**: `extbook`, title, and nothing else but `\include`s of the chapter files.
- `lyx/ice.lyx` is the first **chapter child** — Chapter *Ice*, sections *Waiākea* and *Silver Spring*. One file per chapter; more will appear.
- **Chapters are named for a substance** (Ice, Mud …), **sections for a place**, at district or town granularity (*Waiākea*, *Silver Spring*). Place names carry correct Hawaiian orthography — *Waiākea*, *Hawaiʻi*, *Oʻahu*.
- **Scene IDs live in a collapsed LyX Note attached to the section head** (`S1` inside the *Waiākea* heading). That is the link back to `reference/Scenes.2.md`. Do not expect scene numbers in printed text.
- **Each scene opens with a Subsection holding a plain ISO 8601 local timestamp** — `2031-05-14T17:20:00-10:00`. Offsets west of Greenwich are negative. The running list is in `reference/Calendar.md` §2a.
- **Drafting uses LyX Branches declared in the master**, all permanently deactivated: `Plan` (the Scenes sketch, deleted when written), `Draft` (candidate prose, retyped not moved), `Scenes.2`, and the dial branches.
- When compiled through the master, only the **master's** preamble applies. Any preamble edit made in a child is silently ignored.

## Files

- **Never edit `lyx/*.lyx` directly.** Len edits the manuscript. Any suggested prose — new passages, line fixes, cuts — goes into `reference/<scene>-suggestions.md` as plain text he can paste. No exceptions, and no "I'll just fix the typo."
- **Never write to `reference/Scenes.*.md` without asking.** Draft the change, show it, wait.
- New staging files are fine. Name them for the scene: `S1-suggestions.md`.
- **Write every `.md` file with one line per paragraph.** No hard wrapping at any column. Long lines are correct — they paste into LyX as single paragraphs.

## Authority

- **The manuscript is ground truth.** `Scenes.1.md` and `Scenes.2.md` were written by other chats and are suggestions Len may or may not follow.
- **A conflict between the `.lyx` and the outline is not an error.** It means the outline is out of date. Flag it as a required modification to Scenes, report it, and ask before recording it.
- Do not silently reconcile in either direction.
- Before characterizing what the manuscript does, re-read the manuscript. Do not infer a scene's behaviour from the outline's description of it.
- **Every file in `reference/` was written by a chat, including the ledgers.** When two of them disagree about a physical quantity, *compute it*. Do not adjudicate by which file the number lives in, and never describe an inherited number as "the physical number" without having checked it. Show the arithmetic and state the error band.

## Time

**Day 0 is Thursday 15 May 2031, UTC.** D+8 is Friday 23 May 2031 — the Friday before Memorial Day, and USNA commissioning day. The full calendar, the zone table and the conflicts the anchor exposes are in `reference/Calendar.md`; read it before dating anything.

Offsets that matter: Hilo is UTC−10 and **never** observes DST; the DC area is UTC−4 in May. **Silver Spring is 6 hours ahead of Hilo** through the fortnight, 5 in winter.

**Notation — two registers, never mixed.** Machines speak UTC only (`04:12:07Z`): Oscar's screen, IMS notices, bulletins, gauges, logs. People speak local with no offset. Subsection heads carry both plus the day marker and both dates, because the **date rollover** is the trap, not the offset. Never write `Z+dd` — in ISO 8601 the `Z` *is* the offset.

Beyond the anchored calendar, times are relative to T=0. **Audit local consistency within a scene only.** Do not raise global clock reconciliation against `Timeline.1.md` or the clock tables in Scenes — the component sums are not expected to add up and the disagreement is not a defect.

## Prose

- Nālani's sections: first person, past tense. Daniel's: close third. (The tense of the S1 opening is an open question — see `reference/S1-suggestions.md`.)
- Direct subject–verb–object. No cleft constructions ("What she did was…", "It was Tūtū who…"). No passive voice without a specific reason.
- **Do not restructure sentences that already work.** If a change is only about rhythm, flag it as optional rather than folding it into a rewrite.
- Len's book, Len's voice. Suggest sparely and say what a suggestion costs.

## Hawaiian and diacritics

Macrons and ʻokina belong in the finished text: Tūtū, Nālani, Kuʻu hiwahiwa, Lehua, Kamehameha, Kuʻu lei.

**Len types without accents on purpose** — they are awkward to enter — and corrects them in a single cleanup pass at the end. So: write accents correctly in anything you compose, and **do not report Len's unaccented spellings as errors or defects.** They are not typos and they are not continuity problems. Keep a running cleanup list only if asked. Real misspellings (a wrong letter, not a missing diacritic) are still worth flagging.

*Tūtū* is Hawaiian for grandmother, not a name — inside the house she is **Tūtū**; narration and outsiders say **Tūtū Ruth**. A cultural read is planned at manuscript stage.

## Git

- **History is linear on `main`.** One author, sequential work, nothing to merge. Do not propose a git branch per scene or per chapter.
- **Tags are the memory.** Every tag name is used exactly once — `S1-draft1`, `S1-draft2`, never a bare `S1`. `commit.sh` tags with `git tag -f`, which silently *moves* an existing tag; unique names make that harmless. Retrieve any past state with `git show <tag>:lyx/ice.lyx`.
- **`commit.sh` gotcha:** passing paths *replaces* `git add -u` rather than adding to it. To pick up a new file, `git add` it once by hand, then run `commit.sh` normally.
- Run `commit.sh` from Len's own terminal, never from the sandbox — the mount can create files but not delete git's lock files.
- **A git branch is only for a speculative variant that might be discarded** — `try/present-tense-opening`. Name it for the question, not the scene.
- **For alternative text inside the manuscript, use LyX Branches, not git.** Both versions live in the same `.lyx` file, travel with it, and toggle from a checkbox. This is the tool for the Dials in `Scenes.2.md`. Branch names are declared in the master, `IceCapades.lyx`.

## Continuity

`reference/Scenes.2.md` carries the consistency ledger. Check it before proposing anything that touches dates, ages, the cottage, the one sheet, or Nālani's chronology. The Cast and the ledger are the parts of Scenes worth trusting; the scene sketches are provisional.
