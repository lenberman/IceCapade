# Typography — machine registers

How machine output is set on the page, and where the definitions have to live.

---

## 1. The question is not one convention, it is two

Nālani's Oscar is already set: **monospace bold** for her typed commands (`Explain alert`, `Amplitude`, `Again.`), with replies in ordinary quoted text. That works and should not change.

The instinct to give Daniel's LLM the *same* treatment is worth resisting. The book's whole method is two households, two clocks, two registers, and this is a free chance to extend it.

**Hers is a terminal she drives.** She set it up herself six years ago when her grants stopped. She types verbs at it. It answers in short sentences and never interprets. Monospace is right because it is a command line and because it is *hers* — a personal tool, unbranded, terse.

**His is an institutional product that reports at him.** Procured, named by a program office, running on somebody else's infrastructure, and arriving in his queue whether he asked or not. It should not look like a command line, because he is not commanding it.

So: **different faces, and the difference carries the characterisation.** Her machine answers. His machine files.

---

## 2. Recommendation

| | Nālani / Oscar | Daniel's |
|---|---|---|
| Face | typewriter | **sans-serif**, small |
| Weight | bold for her input | regular |
| Layout | inline with the prose | indented block, thin rule above and below |
| Label | none | small-caps source line, optional |
| Register | terse, imperative | complete sentences, hedged, institutional |

Sans against a Latin Modern body is an immediate, quiet signal. It prints cleanly at any size, survives print-on-demand, works on E Ink, and never looks like design. A thin rule top and bottom sets the block off without a box.

**The rule that pays for itself:** anything set in a machine face is also in UTC (Ledger #29). Typography and clock make the same cut, so the reader learns one distinction instead of two.

---

## 3. On white-on-black

I would not, for body text, and the reasons are production rather than taste.

- Reversed type on uncoated novel stock fills in. Counters close, small type turns muddy, and the ink load shows through the leaf.
- It is the first thing in the book that would look like **a screen**. Your found-document tradition is a *paper* tradition — `FourteenDays.md` is telemetry buffers, tide-gauge columns, a master's log, a handwritten note on the back of a bulletin. Introduce reversed video and Oscar's exchange retroactively looks like it should have been one too.
- Print-on-demand and e-readers handle it unevenly; on E Ink a black slab flashes on every page turn.
- It reads as design-forward, which fights the documentary register everything else is working to hold.

**Where it would earn its keep:** once. A single reversed page or block at one moment where the shock is the point — the Bulletin 003 cancellation, or the D+12 hinge. If it appears exactly once in four hundred pages, it lands. If it appears every time a machine speaks, it is wallpaper.

If you want it, `tcolorbox` is the tool:

```latex
\usepackage[most]{tcolorbox}
\newtcolorbox{screen}{colback=black, colupper=white, boxrule=0pt,
                      arc=0pt, left=6pt, right=6pt, top=6pt, bottom=6pt}
```

---

## 4. Recipes

### Where these must go

**In the preamble of `IceCapades.lyx`, the master — not `ice.lyx`.** When the book compiles through the master, only the master's preamble applies and any definition in a child is silently discarded. This is exactly the trap `CLAUDE.md` warns about, and a new environment is precisely the kind of thing that gets defined in the file you happen to have open.

### Preamble

```latex
% --- machine output ---------------------------------------------------
\usepackage{xcolor}

% Daniel's institutional assistant: sans, small, ruled block
\newenvironment{analyst}%
  {\par\addvspace{\medskipamount}%
   \noindent\rule{\linewidth}{0.4pt}\par\nobreak\vspace{2pt}%
   \begingroup\sffamily\small\setlength{\parindent}{0pt}%
   \leftskip=1.5em \rightskip=1.5em}%
  {\par\endgroup\vspace{2pt}%
   \noindent\rule{\linewidth}{0.4pt}\par\addvspace{\medskipamount}}

% optional small-caps source label, used as \analystfrom{name}
\newcommand{\analystfrom}[1]{{\scshape\footnotesize #1}\par\vspace{2pt}}
```

### Use a module, not Local Layout — corrected

**Local Layout is per-document and does not inherit from the master.** Putting the style in `IceCapades.lyx` does nothing for `ice.lyx`, even with `\master` correctly set: the master relationship gives the child the textclass and lets it compile in context, but the child's style list comes from its own textclass, its own modules, and its own local layout. That is why **Analyst** does not appear in the dropdown while editing the chapter.

For a master plus chapter children, the right container is a **module**. One file, one definition, added per document with two clicks.

**Put the LaTeX in the module too**, so it no longer depends on the master preamble at all. If you do, delete `\newenvironment{analyst}` and `\newcommand{\analystfrom}` from `IceCapades.lyx`'s preamble or LaTeX will error on the duplicate definition.

**House convention: the file lives in `lyx/` and is symlinked from the user layouts directory.** Modules work under a symlink exactly as `.layout` files do — LyX's reconfigure scans the layouts path for entries named `*.module` and the OS resolves the link when the file is read, so it never learns the difference.

```
ln -s "$PWD/lyx/machineoutput.module" ~/.lyx/layouts/machineoutput.module
```

Two rules that follow. **The link name must keep the `.module` extension**, because the scan matches on the directory entry, not the target. And **use an absolute target** — a dangling link is the failure mode to fear here, because LyX drops an unreadable module silently, `Analyst` paragraphs fall back to Standard, and the environment vanishes from the export with no error.

Verify it took, after Tools → Reconfigure:

```
grep -i "machine output" ~/.lyx/lyxmodules.lst
```

The payoff is that the module is versioned with the manuscript, travels in the repo, and can be read and edited by a chat — none of which is true of a file buried in `~/.lyx`.

```
#\DeclareLyXModule{Machine Output}
#DescriptionBegin
#Paragraph styles for machine output. Analyst: institutional, sans, ruled.
#DescriptionEnd

Format 104

Preamble
	\newenvironment{analyst}%
	  {\par\addvspace{\medskipamount}%
	   \noindent\rule{\linewidth}{0.4pt}\par\nobreak\vspace{2pt}%
	   \begingroup\sffamily\small\setlength{\parindent}{0pt}%
	   \leftskip=1.5em \rightskip=1.5em}%
	  {\par\endgroup\vspace{2pt}%
	   \noindent\rule{\linewidth}{0.4pt}\par\addvspace{\medskipamount}}
	\newcommand{\analystfrom}[1]{{\scshape\footnotesize #1}\par\vspace{2pt}}
EndPreamble

Style Analyst
	Category      MainText
	Margin        Static
	LatexType     Environment
	LatexName     analyst
	NextNoIndent  1
	ParIndent     ""
	LeftMargin    MMM
	RightMargin   MMM
	TopSep        0.7
	BottomSep     0.7
	ParSep        0.4
	Align         Block
	LabelType     No_Label
	Font
	  Family      Sans
	  Size        Small
	EndFont
End
```

Then:

1. **Tools → Reconfigure**, and restart LyX.
2. Document → Settings → **Modules** → select *Machine Output* → **Add**. Do this in `IceCapades.lyx` **and** in `ice.lyx`, and in every future chapter child. Modules do not inherit from the master either, but adding one is two clicks and there is a single source of truth.
3. Remove the Local Layout block from `IceCapades.lyx` so it cannot drift against the module.

**Format 104** is right for your LyX — the master's Local Layout already validated at that number.

### The dropdown

It is the leftmost combo box on the toolbar, the one currently reading **Standard**. If it is not visible: View → Toolbars → **Standard**.

### Zero-configuration fallback

If you would rather not install anything yet, paste the `Style Analyst` block (without the module header and `Preamble`) into **`ice.lyx`**'s own Local Layout and keep the `\newenvironment` in the master preamble. That works immediately. The cost is a copy in every chapter file, drifting against each other — the same problem as two preambles.

---

## 5. Open

1. **What did the K2 manuscript environment do?** If it was a `\newenvironment`, it can be lifted into the master preamble as-is and I will match the drafting to it. Paste the definition and I will fold it in here.
2. Does Daniel's assistant have a name, and does he type to it or does it push to him? The answer decides whether it needs an input face at all — Oscar needs two (bold command, plain reply); a thing that only reports needs one.
3. Small-caps source label on each block, or unlabelled?
4. Reserve one reversed-video moment, or none at all?
