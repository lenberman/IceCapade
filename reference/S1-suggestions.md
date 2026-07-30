# S1 — suggested text, orthography, and reference state

Staging file for `lyx/ice.lyx`, scene S1. Nothing in §5 has been applied to the manuscript. The `.lyx` file is not edited by any chat; paste from here if you want a line.

Everything in `reference/` was written by chats. It is suggestive, not prescriptive. Where the manuscript disagrees with it, the manuscript is right and the reference gets updated.

Conventions: Nālani first person, past tense, **except S1's opening two paragraphs, which run present and are deliberate**. Times relative to T=0, local consistency only. Accents written out here; unaccented drafting in the manuscript is not a defect.

Audited against `ice.lyx` in full — header and body — ending at *"I closed Oscar, the screen and laptop. I needed to share."*

---

## 1. Applied to the reference files

Done, not pending.

**`Scenes.2.md`** — S1 sketch replaced wholesale; Cast entry for Nālani now carries Oscar instead of the cron job, plus the return-motive note; Lehua's Cast entry gains the directed-silence paragraph; a Cast entry for Oscar added; Narrative mode records the deliberate present-tense opening; Ledger #1 closed and #16–#27 added.

**`Scenes.1.md`** — status note updated at Cast level per its own sync rule; S1 sketch reduced to a pointer; ledger item 1 closed.

Both files' new paragraphs are written one line per paragraph. The older paragraphs in `Scenes.2.md` are still hard-wrapped at ~95 columns from whoever wrote them. Say the word and I'll rewrap the whole file; I left it alone so the diff would show content changes rather than reflow.

---

## 2. Cleared in the manuscript

Re-verified. Do not raise again.

- HA01 detection is **04:12:07Z**, matching `FourteenDays.md` §2. No reference change needed.
- Crozet is **HA04**.
- `pdf_title` is "Ice Capades"; the *Karmageddon Diaries* title is gone.
- The spellchecker ignore list is empty — all ~370 inherited entries removed.
- The unclosed quote on *"Tales of the families. Stories I've told you."* now closes.
- The duplicated verb in *"She walked with her father walked down"* is fixed.
- `secnumdepth -2` prints the heading unnumbered.
- The ʻokina characters already in the file are **U+02BB**, which is correct. See §3.

---

## 3. Hawaiian orthography — first occurrences

### How to type the two marks

**ʻOkina** is **U+02BB**, MODIFIER LETTER TURNED COMMA: `ʻ`. It is a consonant, not punctuation. It is *not* an apostrophe (`'` U+0027), *not* a left single quote (`'` U+2018), and *not* a right single quote (`'` U+2019). Your file already uses U+02BB throughout, so whatever you are doing to enter it, keep doing it.

**One trap in your current setup.** `dynamic_quotes` is now on. If you type a bare `'` intending an ʻokina, LyX will convert it to a typographic quote — which looks close enough to an ʻokina to survive proofreading and is the wrong character. Paste U+02BB or bind a key; do not type an apostrophe and hope.

**Kahakō** is the macron. Use the precomposed letters, not a combining accent: **ā ē ī ō ū** (U+0101, 0113, 012B, 014D, 016B) and **Ā Ē Ī Ō Ū** (U+0100, 0112, 012A, 014C, 016A).

### Already in the manuscript, in order of first appearance

| # | Correct form | First occurrence | Marks | Note |
|---|---|---|---|---|
| 1 | **Tūtū** | ¶1, *"Tūtū sitting in her straight-back chair"* | two kahakō | grandmother; a title, not a name |
| 2 | **Kuʻu hiwahiwa** | ¶1, Tūtū's first line | ʻokina in *kuʻu* | my precious one; *hiwahiwa* takes no marks |
| 3 | **Lehua** | ¶1 | none | the ʻōhiʻa blossom |
| 4 | *musubi* | ¶1 | none | Japanese, not Hawaiian |
| 5 | **Kuʻu lei** | ¶2 | ʻokina in *kuʻu* | *lei* takes no marks |
| 6 | **Ikaika** | *"Ikaika at school"* | none | strong |
| 7 | *Tomás* | same ¶ | Spanish acute | not Hawaiian |
| 8 | **Kuʻu mau hiwahiwa** | the call to the table | ʻokina in *kuʻu* | *mau* is the plural marker, no marks |
| 9 | **E ʻai kākou!** | same ¶ | ʻokina before *ai*; kahakō on the first *a* of *kākou* | let's eat |
| 10 | **Waiākea** | *"What happens to Waiākea?"* | kahakō on the second *a* | the district |

All ten are correct in the current file.

### Coming, per `Scenes.2.md` — and several are wrong in the reference

These have not reached the manuscript yet, so the first occurrence is still ahead of you. The middle column is how the reference files currently spell them, which is how the error would propagate if you drafted from them.

| Correct form | In the reference as | Where it first lands |
|---|---|---|
| **Hawaiʻi** | "Hawaii" | your section title; S23 |
| **Oʻahu** | "Oahu" | S23, S24, Dial 6 — the flank material |
| **Nuʻuanu** | "Nuuanu" | S23, S24 — the northeast scar |
| **Molokaʻi** | "Molokai" | Dial 6 |
| **Lānaʻi** | "Lanai" | S23 — the Lānaʻi deposits |
| **Mānoa** | correct | Cast, S3 |
| **Nālani** | correct | her own name, still not on the page |
| **Kamehameha** | correct | the store's street |
| **Kīlauea** | absent | if the volcanism material gets a scene |
| **Laupāhoehoe** | absent | the 1946 schoolhouse, if Tūtū's tale ever extends |
| Hilo, koa, Kawika, Keala, Hilina | correct | — |

The five in the top block are the ones worth fixing in `Scenes.2.md` before they reach the manuscript. Say the word.

---

## 4. Chapter **Ice**, section **Hawaiʻi**

### The names

**Ice works, and it works better because S1 contains none.** The chapter is called Ice and the reader spends it in a kitchen in Hilo listening to a sixteen-year-old recite a catechism. The title says what the sound was; the scene refuses to show it. That is the book's method in miniature, on the first page, for free.

It also sets up a system. Your parts are already THE DAY / THE MUD / THE WEEK / THE LOAD, and *Ice* against *Mud* is the book's real argument — two substances, and the reader learns in Part Two that the second one is the killer. If chapters are substances the scheme extends without strain.

**Chapters named for a substance, sections named for a place** is a clean division: chapter is *what*, section is *where*. It scales — Ice / Hawaiʻi, Ice / Silver Spring, Ice / Prydz Bay. One thing to decide early: what a found document is titled, since `FourteenDays.md`'s pieces have no place or several. Options are to give them the place of their origin (Cape Leeuwin, Malé, Keamari), or to leave them untitled and let the typography mark them.

**Use the ʻokina: Hawaiʻi.** In a book whose household turns on *tūtū* and *kuʻu hiwahiwa*, a section head spelled "Hawaii" is the one place the orthography would visibly lapse, and it is set in large type at the top of a page. Same reasoning will apply to Oʻahu when Part Four gets there.

### The LyX problem

**`extarticle` has no `Chapter` layout.** You currently have `\textclass extarticle` and S1's container marked up as `Section`. To get a real chapter you need a book class — `extbook` is the direct swap and is what the file used to be.

Two ways:

- **Switch to `extbook`.** Chapter = *Ice*, Section = *Hawaiʻi*. Natural, and `papersides 2` is already set for it. This is what I would do.
- **Stay in `extarticle`.** Use `Part` = *Ice* and `Section` = *Hawaiʻi*. Works, but Part and Chapter set differently and you will fight it later when there are four parts *and* chapters.

Either way `secnumdepth -2` keeps the numbers off, which is what you want for named chapters.

---

## 5. Continuation — the return

The room is drafted; this is the last movement, from *"I needed to share."* Lehua was sent to clean up, so the table is clear and there is no fork to put down. Tūtū's chair by the window closes the scene where it opened.

The table was cleared and Lehua had her book back. Tūtū was in her chair, and the light had gone out of the sky while I was in my room.

She watched me come down the hall. She did not ask what had happened. She has never in her life asked what had happened.

"How long," she said.

"It isn't that kind, Tūtū. It's ice. Ice floats — all of it, all the time, it's already floating. It doesn't make a wave."

She looked at me a while longer. Then she turned back to the window, where there was nothing left to see.

### Notes

*"How long"* is the only question she has ever needed. It presumes a wave, because in this house a wave is what the ocean does, and it hands Nālani the chance to be reassuring and wrong in one breath — with the exact reasoning Daniel signs in S4, hours before he sees it.

*"where there was nothing left to see"* returns to the opening image and closes on darkness, and on a ninety-one-year-old deferring to her granddaughter's expertise.

Colder: cut *"She looked at me a while longer"* and let her turn to the window immediately. Warmer: she says nothing and takes Nālani's burned hand.

Open: whether the return gets its own break. Not another **Bzzzz** — twice in one scene it stops being a marker and becomes punctuation (Ledger #23).

---

## 6. Live items in the manuscript

### Hard

**Unmatched quote inset in Tūtū's 1960 speech.** The paragraph opens with a `qld` inset and closes with a literal `"` after *"the family store was destroyed,"* before the narration break. The opening inset never gets its `qrd`. LyX will not complain and the PDF may look fine; the source is malformed.

**`Display possible source locii`** — *loci*. Defensible as her typing fast at a machine that doesn't care, but a reader is likelier to read it as yours than as hers.

### Open decisions

**Dinner is still *"takeout from L&L."*** Your earlier note was that this becomes something she cooks.

**Hawaiian glosses are inconsistent.** *Kuʻu mau hiwahiwa. E ʻai kākou!* gets a footnote; *Kuʻu hiwahiwa* and *Kuʻu lei* don't. Three defensible policies — gloss the first occurrence of each, gloss only full sentences as now, or gloss nothing and let context carry it. Worth settling once so the rest of the book follows. My preference is the third for single words in dialogue between family, and the second for anything a reader could not infer.

### Cosmetic

**Three quote encodings coexist** — `qld/qrd` insets early, `xld/xrd` on *"Lehua, no reading until you've cleaned up,"* and literal ASCII quotes through the catechism and the Oscar section. With `quotes_style plain` the output is probably uniform; source hygiene rather than a visible defect.

**`pdf_keywords` is still "AI, peace, family, greed."** Leftover.

**Textclass `extarticle`** — see §4.

---

## 7. Open

1. Fix the five misspelled place names in `Scenes.2.md` — Hawaiʻi, Oʻahu, Nuʻuanu, Molokaʻi, Lānaʻi?
2. Rewrap `Scenes.2.md` to one line per paragraph throughout?
3. Gloss policy for Hawaiian — §6.
4. Does the bedroom-to-table return get its own break?
5. *loci* or *locii*?
