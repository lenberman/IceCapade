# Hydroacoustics — what the IMS can and cannot know, and when

Computed, not inherited. Everything below comes from `tools/ims_paths.py` and `tools/ims_locate.py`, which are in the repo and re-runnable. Bathymetry is Natural Earth 10 m depth-contour polygons. Method, modelling choices and limits are documented in the scripts' docstrings; the short version is in §6.

This file answers three questions: which stations can hear which collapse, when each event becomes **detectable**, and when it becomes **locatable**. Those last two are not the same instant and the gap between them is where most of Part One lives.

---

## 1. The network is two different instruments, and the difference is the whole answer

The IMS hydroacoustic network is eleven stations. It is not eleven of the same thing.

**Six hydrophone stations** — HA01 Cape Leeuwin, HA03 Juan Fernández, HA04 Crozet, HA08 Diego Garcia, HA10 Ascension, HA11 Wake. Each is a **triad** of hydrophones moored in deep water at the sound-channel axis, elements kilometres apart. Cross-correlating across the three gives a **back-azimuth** good to a degree or two. One of these gives you a *direction and no range.*

**Five T-phase stations** — HA02 Queen Charlotte, HA05 Guadeloupe, HA06 Socorro, HA07 Flores, HA09 Tristan da Cunha. These are **seismometers on islands**. The acoustic wave converts to a seismic wave on the island flank, so the apparent arrival direction is set by where the conversion happened, not by where the source is. Treat these as **arrival time only, no usable bearing.**

From which the locatability rules follow, and they are not negotiable:

| what you have | what you know |
|---|---|
| 1 hydrophone | a **ray**. A direction. Nothing else. |
| 2 hydrophones | two bearings crossing, plus a ΔT hyperbola → **located** |
| 1 hydrophone + 1 T-station | ray × hyperbola → **located** |
| any 3 stations | multilateration on times alone → **located, and the origin time falls out** |
| 2 T-stations, no hydrophone | one hyperbola. **Not located.** |

**One station can never locate anything.** That is the fact behind the question, and it holds however good the instrument is.

---

## 2. Which stations can hear which collapse

Great-circle path screened against bathymetry shallower than 1,000 m. **CLEAR** = nothing. **MARGINAL** = the longest obstruction is under 150 km — a ridge crest or a seamount, so expect transmission loss and some delay, not extinction. **BLOCKED** = a real barrier, and for those the range and transit below are a lower bound, because the actual path goes round and this screen does not route it.

Sources are modelled in two legs — the shelf front radiates into its own embayment, the energy crosses the continental shelf, and it couples into the deep sound channel at the shelf break. Using the front itself as a far-field point source is what makes great circles run three thousand kilometres along the Antarctic coast and score as blocked. Shelf leg at 1,450 m/s, deep leg at 1,485 m/s.

**Only 3 to 4 of the 11 stations hear any given collapse.** The network is sparse and Antarctica is in the way of most of it.

### Prydz Bay / Amery — front 68.5°S 72.0°E, radiator 65.5°S 73.0°E, shelf leg 336 km

| station | kind | range | t+ | back-az | screen |
|---|---|---|---|---|---|
| **HA04 Crozet** | hydrophone | 2,806 km | **31.6 min** | 157.5° | CLEAR |
| **HA01 Cape Leeuwin** | hydrophone | 4,675 km | **52.6 min** | 205.7° | CLEAR |
| **HA10 Ascension** | hydrophone | 9,415 km | 105.8 min | 155.2° | marginal |
| HA09 Tristan da Cunha | T-phase | 6,433 km | — | — | blocked, 410 km |
| **HA08 Diego Garcia** | hydrophone | 6,808 km | — | — | **blocked by the Kerguelen Plateau** |
| the other six | | | | | blocked |

### Weddell / Ronne-Filchner — front 75.0°S 50.0°W, radiator 68.0°S 38.0°W, shelf leg 882 km

| station | kind | range | t+ | back-az | screen |
|---|---|---|---|---|---|
| **HA09 Tristan da Cunha** | T-phase | 4,669 km | **52.6 min** | *none* | CLEAR |
| **HA04 Crozet** | hydrophone | 6,242 km | **70.3 min** | 210.2° | marginal |
| **HA10 Ascension** | hydrophone | 7,780 km | 87.6 min | 189.8° | marginal |
| HA08 Diego Garcia | hydrophone | 10,964 km | 123.3 min | 200.6° | marginal |
| HA01 Cape Leeuwin | hydrophone | — | — | — | blocked, 4,139 km |

### Amundsen / Thwaites–Pine Island — front 74.8°S 105.0°W, radiator 71.5°S 108.0°W, shelf leg 379 km

| station | kind | range | t+ | back-az | screen |
|---|---|---|---|---|---|
| **HA03 Juan Fernández** | hydrophone | 4,920 km | **55.3 min** | 193.7° | marginal |
| HA06 Socorro | T-phase | 10,412 km | 117.0 min | *none* | marginal |
| HA11 Wake | hydrophone | 11,394 km | 128.0 min | 164.1° | marginal |
| HA02 Queen Charlotte | T-phase | 14,390 km | 161.6 min | *none* | marginal |

### Ross — front 78.0°S 175.0°W, radiator 71.5°S 178.0°W, shelf leg 728 km

| station | kind | range | t+ | back-az | screen |
|---|---|---|---|---|---|
| **HA03 Juan Fernández** | hydrophone | 7,517 km | **84.6 min** | 201.0° | CLEAR |
| **HA11 Wake** | hydrophone | 10,862 km | **122.1 min** | 183.6° | CLEAR |
| HA06 Socorro | T-phase | 11,934 km | 134.1 min | *none* | marginal |
| HA02 Queen Charlotte | T-phase | 15,057 km | 169.2 min | *none* | marginal |
| HA01 Cape Leeuwin | hydrophone | — | — | — | blocked (Balleny Is. / Macquarie) |

**The result is robust.** Re-run at a 2,000 m threshold and not one station changes side: the CLEAR ones become MARGINAL over ridge crests in the 1,000–2,000 m band, and nothing blocked becomes audible. `python3 tools/ims_paths.py --threshold 2000`.

**Three things worth having from that table.**

**Diego Garcia cannot hear Prydz Bay.** The path runs almost due north up the 72°E meridian and goes straight into the **Kerguelen Plateau** — 410 km of it in the 200–1,000 m band, around 53°S. The one IMS hydrophone station actually *in* the Indian Ocean is deaf to the event whose wave will empty the Indian Ocean rim, because a submarine plateau the size of Western Australia is standing in front of it.

**Cape Leeuwin cannot hear the Weddell, the Amundsen, or the Ross.** Antarctica is in the way of all three. HA01 hears exactly one of the four collapses.

**The Southern Ocean is not a well-covered ocean.** Four collapses, eleven stations, and the modal number of stations that hear any one of them is four.

---

## 3. Detectable, and then locatable

Detection is the first arrival. Location needs the second. The interval between is the **blind interval** — the time during which somebody knows a very large thing happened and cannot say where.

| event | origin | detectable | by | locatable | by | blind |
|---|---|---|---|---|---|---|
| **Prydz** | 03:20Z | **03:52Z** | HA04 Crozet | **04:13Z** | HA01 Leeuwin | 21 min |
| **Weddell** | 10:05Z | **10:58Z** | HA09 Tristan *(time only)* | **11:15Z** | HA04 Crozet | 18 min |
| **Amundsen** | 14:50Z | **15:45Z** | HA03 Juan Fernández | **16:47Z** | HA06 Socorro | **62 min** |
| **Ross** | *free* | +84.6 min | HA03 Juan Fernández | +122.1 min | HA11 Wake | 37 min |

Ross has no origin time fixed anywhere in the manuscript or the reference files. On an assumed 15:50Z failure it is detected 17:15Z and located 17:52Z.

**Location quality at the moment of locating**, from two crossed bearings at ±1.5°, before ranges are folded in:

| event | crossing angle | error ellipse |
|---|---|---|
| Prydz | 99° (Crozet × Leeuwin) | 115 × 65 km |
| Weddell | 85° (Crozet × Ascension) | 181 × 141 km |
| Amundsen | 93° (Juan Fernández × Wake) | 289 × 119 km |
| Ross | 99° (Juan Fernández × Wake) | 269 × 180 km |

All four geometries are well conditioned — the crossing angles are near 90°, which is as good as it gets. The ellipses are large anyway, because the ranges are enormous and a degree and a half at 4,700 km is 123 km. **Adding the ΔT hyperbola is what collapses these to something like a bay rather than a province**, which is precisely the operation S1 already performs on the page.

---

## 4. Against the manuscript — three checks pass, two fail

`ice.lyx` fixes six numbers. Computed against the geometry above:

| | manuscript | computed | |
|---|---|---|---|
| HA01, Prydz, transit | 52 min | **52.6 min** | ✓ |
| HA01, Prydz, back-azimuth | 189° | **205.7°** | ✗ 17° |
| HA04, Weddell, back-azimuth | 209° | **210.2°** | ✓ |
| HA04, Weddell, transit | 46 min | **70.3 min** | ✗ 24 min |
| HA03, Amundsen, transit | 54 min | **55.3 min** | ✓ |
| HA03, Amundsen, back-azimuth | 196° | **193.7°** | ✓ |

Four of six are right, and one of the four — Crozet's 209° to the Weddell — is right to a degree, which is better than the instrument. Whoever set those numbers was computing something.

**The two that fail are both one edit.**

**HA01's back-azimuth should be about 206°, not 189°.** 189° points nearly due south of Cape Leeuwin, which puts the source off Wilkes Land near 99°E, not in Prydz Bay. The bearing to Prydz Bay is 206°.

**Crozet cannot reach the Weddell in 46 minutes.** The path out of the Weddell is 6,242 km and takes 70 minutes. Either Crozet posts at **11:15Z** on a 10:05Z origin, or the Weddell origin moves back to **09:41Z**. Taking the first also changes Daniel's *two events, six hours apart* to **seven** — 04:12 to 11:15 is 7 h 03 m.

**And a third thing that is not an error but is now wrong:** Crozet hears Prydz Bay **twenty-one minutes before Cape Leeuwin does**, because Crozet is 2,806 km from Prydz and Leeuwin is 4,675 km. S1's *appropriately late* is backwards. §5 has the fix, and it is an improvement rather than a repair.

---

## 5. Proposed text — paste-ready, nothing applied

### 5a. S1 · the Crozet paragraph

The manuscript currently reads:

> Crozet is a French rock, significantly west of Leeuwin with three hydrophones.
>
> Oscar repainted the window. Crozet had it. The same waveform as HA01, appropriately late and not maxed out, just unimaginable. We knew the detector locations and we knew ΔT. I turned to Oscar.

Replacement, changing as little as possible:

> Crozet is a French rock, significantly west of Leeuwin and a great deal closer to the ice, with three hydrophones.
>
> Oscar repainted the window. Crozet had it. The same waveform as HA01, not maxed out, just unimaginable — and twenty minutes early. Twenty minutes *early*. Whatever this was, it was not out in the ocean between them. It was south, and it was much closer to Crozet than to Leeuwin. We knew the detector locations and we knew ΔT. I turned to Oscar.

**What the change buys.** The sign of ΔT is information and the old version threw it away. A later arrival at Crozet would have meant the source was somewhere east of both, and it is not; the earlier arrival is her first hard constraint on the geometry, arrived at before she asks Oscar for anything. She reasons from the sign of a number, in one line, and everything after it — the hyperboloid, the surface intersection, Prydz Bay — is unchanged and now correctly motivated.

**Everything else in S1 survives untouched, including the line that matters.** *If that was the source, it put the event at twenty past three, fifty-two minutes before it reached Leeuwin* — computed 52.6 minutes. It was right when it was a guess.

**And the epistemics were already right.** She has one station and claims nothing; she calls a second and gets a hyperbola, which is a *curve*; she picks a point off the curve by geography and flags it with *if that was the source*. Two stations give a curve, three give a point, and the prose knows it. Nothing about the two-measurement problem needs fixing in S1. It needed fixing in S2.

**Optional, and it is free.** Oscar alerted on HA01 because HA01 is *her* station — the one her thesis was about — so she gets the alert at 04:12 and the Crozet trace has been sitting on a public feed since ten to four. Half a line if you want it: *Crozet had had it for twenty minutes and nobody had asked Crozet.*

### 5b. S2 · Edgar's first block — one digit

> Back-azimuth 189°, origin Prydz Bay at 2031-05-15T03:20:07Z

becomes

> Back-azimuth 206°, origin Prydz Bay at 2031-05-15T03:20:07Z

The origin claim itself is **sound** and needs no change, because by 04:12:07Z the event is locatable — Crozet heard it at 03:52 and Leeuwin's arrival is the second measurement, not the first. If you want the notice to show its working, add one Analyst line: *Solution: HA04 0352:00Z, HA01 0412:07Z.* That also puts the two-station requirement on the page in Daniel's half of the book, where the reader can see the same rule operating in an institution that will still get the day wrong.

### 5c. S2 · Edgar's second block — the Crozet transit

> Crozet (HA04) posted at 2031-05-15T10:51Z.
> …
> Back-azimuth 209°, origin Weddell at 2031-05-15T10:05:00Z

becomes

> Crozet (HA04) posted at 2031-05-15T11:15Z.
> …
> Back-azimuth 209°, origin Weddell at 2031-05-15T10:05:00Z

and then, six lines later:

> Odd, he thought, two events, six hours apart.

becomes

> Odd, he thought, two events, seven hours apart.

**Keep 209°.** It is right to a degree and it is the one number in the manuscript that could not have been guessed.

### 5d. S2 · the third block — the hour the room has a direction and nothing else

This is the only change that is not arithmetic, and it is the one worth having.

The manuscript currently gives Juan Fernández a located origin in the same notice as the detection:

> Juan Fernández posted at 2031-05-15T15:44Z.
> Broadband arrival, 11Hz to 4Hz, 350 seconds
> Back-azimuth 196°, origin Amundsen Sea Embayment, 2031-05-15T14:50Z.

At 15:44Z that origin does not exist. HA03 is the only station that has heard it and one station is a bearing. **The Amundsen event cannot be located until Socorro picks it up at 16:47Z — sixty-two minutes later.** Proposed:

> Juan Fernández posted at 2031-05-15T15:44Z.
>
> Broadband arrival, 11Hz to 4Hz, 350 seconds
>
> Back-azimuth 194°. Single-station detection. **No origin.**
>
> Nearest supporting stations: HA06 Socorro, HA11 Wake. No arrival posted.

And then, later — after the PTWC statement, after lunch, in Daniel's afternoon or in S4 — the origin arrives:

> HA06 Socorro posted at 2031-05-15T16:47Z.
>
> Associated with HA03::15:44Z. Two-station solution: Amundsen Sea embayment, origin 2031-05-15T14:50Z.

**Why this is better than what it replaces.** The beepers go off just after eleven forty-five and the room has a *direction and no place*. Somebody asks where it is and the honest answer is *four thousand miles that way*. That is an hour of a deputy director's day spent holding an arrow — and it ends at ten to one, which is after they have gone to lunch. The consensus that survives four events now forms while the third one has no address. Nothing in the room is stupider than before; it has simply been given less, correctly, by an instrument doing exactly what instruments do.

It also makes PTWC's 16:22Z statement land properly. *Sea level disturbance recorded at Scott Base and at three DART buoys in the Ross sector. No seismic origin. Under evaluation.* Correct, and now legible: the Ross event is not acoustically detected until about 17:15Z and not located until about 17:52Z, so at twenty past four the Pacific centre has water moving and genuinely no source. They are not being cautious. They are being accurate.

### 5e. Available and unused — the Weddell's first witness is a seismometer

`HA09 Tristan da Cunha` hears the Weddell collapse at **10:58Z**, seventeen minutes before Crozet, and it is a T-phase station: an island seismometer, arrival time only, no bearing at all. If you want one more Analyst block in Daniel's morning, this is the one to have — the first thing anyone learns about the second collapse is that *something happened somewhere*, fifty-three minutes ago, reported by a rock in the South Atlantic.

---

## 6. Method, and where it would break

**Bathymetry.** Natural Earth 10 m depth-contour polygons. A path sample is "deep" if it falls inside the polygon set for the threshold. Barriers are graded against the 200 m and 2,000 m contours so a sill is distinguished from an island. Sampled every 10 km.

**Sound speed.** Deep leg 1,485 m/s, shelf leg 1,450 m/s. Southern Ocean water is cold and the channel-axis speed is genuinely nearer 1,450–1,465 m/s over the polar part of a path; running the deep leg at 1,465 moves Cape Leeuwin from 52.6 to 53.3 minutes and at 1,500 to 52.0. **Call it 52 ± 1 minute** and nothing in the book is sensitive to it.

**Bearings.** Great-circle initial bearing, station to source, clockwise from north. Real IMS azimuths carry a degree or two of scatter and some bias from horizontal refraction; ±1.5° is the figure used for the ellipses in §3.

**What the screen does not do.** It is geometry, not acoustics. It does not model refraction over a sill, diffraction round the end of a ridge, upslope conversion at a receiving island, or the poleward shoaling of the sound-channel axis — south of the Polar Front the sound channel is surface-bounded, which makes near-Antarctic segments more sensitive to shallow bathymetry than a 1,000 m threshold implies, and more sensitive still to **sea ice**, which in mid-May is advancing hard and scatters surface-ducted energy. None of that is in here. Read MARGINAL as *ask an acoustician*, and treat every BLOCKED range as a lower bound rather than a prediction of silence.

**Station coordinates** are nominal positions good to a few kilometres. Several stations are two triads rather than one (HA03, HA08, HA10, HA11); using the station centroid costs a few kilometres of range and nothing that matters here. **Source positions** are ice-front and shelf-break points chosen by hand; moving the Prydz radiator around inside Prydz Bay moves Cape Leeuwin's transit by a minute or two and does not change any CLEAR/BLOCKED verdict.

**Re-run it:**

```
python3 tools/ims_paths.py --csv out.csv          # the screen
python3 tools/ims_paths.py --threshold 2000       # sensitivity
python3 tools/ims_locate.py out.csv               # detect vs locate
```

Bathymetry is not in the repo. Fetch it once with:

```
git clone --depth 1 --filter=blob:none --sparse \
    https://github.com/nvkelso/natural-earth-vector.git /tmp/ne
cd /tmp/ne && git sparse-checkout set 10m_physical
```

---

## 7. Killing Crozet — what it costs and what it buys

Len's decision: the Prydz arrival takes out HA04. Computed consequences.

### 7a. The amplitude justifies it, and only just, which is right

Crozet sits 2,470 km from the Prydz radiator on the deep leg; Cape Leeuwin sits 4,339 km. Ratio 1.76. SOFAR propagation is cylindrical beyond the first convergence zones, so the transmission-loss difference is 10·log₁₀(1.76) = **2.45 dB**, and the pressure-amplitude ratio is √1.76 = **1.33**. Absorption at 4–11 Hz runs about 5×10⁻⁴ dB/km and contributes 0.93 dB over the extra 1,870 km — negligible, and in the same direction.

**So Crozet receives about a third more pressure than Cape Leeuwin.** That is exactly the right size of margin. Thirty-three per cent is enough to put one instrument over full scale while the other captures its peak on-scale, and not so much that it looks arranged. The manuscript already has Cape Leeuwin recording an amplitude and *then* railing; Crozet, a third louder, clips on the arrival itself.

Clipping and destruction are different, and the honest sequence is: **both stations clip, both then sit at full-scale drive for hours while the mélange keeps radiating, and the preamplifiers die in range order.** Crozet first.

### 7b. The onset has to survive, and it does

IMS hydrophone stations telemeter continuously to a shore facility. **The instrument dies; the data does not.** Whatever Crozet recorded before it went is already off the island, and that includes the onset, which precedes saturation.

This matters more than anything else here. If Crozet is gone before it reports, Prydz Bay is not locatable until Ascension arrives at **05:06Z**, and the 04:12:07Z alert — which is the whole opening of the book — dies with it. Keep the telemetry.

### 7c. Dead, or blinded? Blinded is better, and "three hydrophones" is why

Two versions, and they differ by more than flavour.

**Total loss.** Crozet contributes nothing after 03:52Z.

**Degraded — the arrival destroys two of the three elements.** Crozet keeps recording and keeps telemetering. What it loses is the *cross-correlation across the triad*, which is the only thing that produces a back-azimuth. **It survives as a timing station with no bearing — functionally a T-phase station.**

The manuscript already says *Crozet is a French rock, significantly west of Leeuwin with three hydrophones.* Under the degraded version that sentence becomes load-bearing: three is precisely what a bearing costs, and the reader who noticed the number gets paid for it forty pages later.

### 7d. What it does to the Weddell

Origin 10:05Z. All three scenarios below assume HA01 is already railed, which the manuscript establishes.

| | detected | located | origin time solved | blind |
|---|---|---|---|---|
| **A — Crozet intact** | 10:58Z HA09 Tristan *(no bearing)* | **11:15Z** HA04 Crozet | 11:33Z | 18 min |
| **B — Crozet blinded** | 10:58Z HA09 Tristan | **11:33Z** HA10 Ascension | **11:33Z** | **35 min** |
| **C — Crozet dead** | 10:58Z HA09 Tristan | **11:33Z** HA10 Ascension | 12:08Z HA08 | **35 min** |

**Both versions push the Weddell location from 11:15Z to 11:33Z and double the blind interval, 18 minutes to 35.** In Silver Spring that is 07:33 instead of 07:15 — Daniel is still on his bicycle either way, so nothing in S2 has to move.

The difference between B and C is the **origin time**. Blinded Crozet still supplies a third arrival time, so when Ascension's bearing lands at 11:33Z the whole solution closes at once — position and origin together. Dead Crozet leaves only two arrivals at 11:33Z, so the position comes then and the origin time waits for Diego Garcia at **12:08Z**. A thirty-five minute stretch in which an agency knows *where* the second collapse happened and cannot say *when* — which is a strange and specific kind of not-knowing, and free if you want it.

**And the geometry degrades.** With Crozet the Weddell bearings cross at 85° over a 181 × 141 km ellipse. Without it the cross is Ascension × Diego Garcia — still 85°, but at far greater range, giving **265 × 181 km**. The second collapse is located to within a large European country.

### 7e. The prize — the instrument that would have heard the mud

The Prydz Channel Fan lets go at 15:22Z at the shelf break, which is the same point the ice radiated from. **Crozet is the nearest hydroacoustic station on Earth to it — 2,470 km, twenty-eight minutes.** An intact Crozet posts a fifteen-to-twenty-minute non-impulsive arrival at about **15:50Z**.

It is dead, killed by the ice twelve hours earlier.

That is the cleanest statement of the book's whole mechanism in one instrument: *the ice destroyed the ear that would have heard the mud.* Nobody in the story ever has to say it. It is simply true, and a reader who reconstructs it gets it for nothing.

**And the sector goes dark.** From about four in the morning the Indian Ocean sector has no functioning hydrophone triad except HA08 Diego Garcia — which, per §2, is blocked from Prydz Bay by the Kerguelen Plateau. The ocean about to be destroyed is being monitored by one station that could not hear the event that started it.

### 7f. Two lines in S1 that have to move

**The alert.** Len's instinct — Oscar beeps on detection and labels location UNKNOWN — is right, and there is a version that keeps the manuscript exactly as it stands. Let the alert be **HA01 at 04:12:07Z**, her own station, the one her thesis was about, and let it say **LOCATION UNKNOWN**. That is what an automatic system would post, because association takes minutes and Crozet's 03:52 arrival is sitting unassociated on another feed.

Then `Examine Crozet hydrophones, HA04` **is the association.** She does by hand, in a bedroom, the thing the network has not done yet. Nothing in the scene changes and every keystroke in it acquires a reason.

**The query.** The manuscript has the query originating at Crozet:

> query to Cape Leeuwin: Is your 0412 event ongoing? No response.

Crozet cannot ask anything if Crozet is down. Reassign it to Vienna and let it go to both:

> Query to HA01, HA04: is your 0412 event ongoing?
>
> No response from either station.

Colder, and it puts the second dead instrument into Daniel's queue at nine in the morning without a word of comment.

**And a fact she can register in S1 without breaking Ledger #19.** Two of the world's six hydrophone triads died inside an hour. That is a larger signal than *three orders of magnitude too large* and no bulletin has stated it. It also rhymes hard against the four silent shore stations she looks at in the same scene and does not add up — **six dead instruments, and she registers two of them.** Ledger #21 survives intact, because the two she registers are not the four she doesn't.

---

## 8. Amplitude — units, and numbers for the four events

### 8a. The unit is dB re 1 µPa²·s, and the reason matters

Underwater acoustics measures everything in decibels referenced to **one micropascal**, and there are four quantities in that family. Only one of them is right here.

| quantity | unit | what it is |
|---|---|---|
| sound pressure level | dB re 1 µPa | the pressure at the sensor, peak or RMS over a window |
| **sound exposure level (SEL)** | **dB re 1 µPa²·s** | **pressure squared integrated over the whole event** |
| source level | dB re 1 µPa @ 1 m | back-propagated to a nominal metre from the source |
| spectral density | dB re 1 µPa²/Hz | for broadband noise |

**SEL is the one, because these events last 340 seconds.** A peak pressure describes an explosion. It badly undersells a source that radiates for nearly six minutes, and the whole point of an ice collapse is that it is not impulsive. `four-sectors-sequence.md` §13 already has Sandoval forwarding *the complete Day 0 SEL sequence*, so the book chose this unit before anyone asked the question.

**And it resolves the manuscript's best line.** *It could not be — three orders of magnitude too large.* Three orders of magnitude in **energy** is 30 dB, which is only 32× in pressure. In pressure it would be 60 dB and imply a source level above anything ever recorded. As an SEL statement it is exactly right, and it is what an analyst comparing a 340-second arrival to her own six years of them would actually say.

**Two things the units do for the plot.**

**She can say it without a location.** The received SEL is compared against her own population of ice signals *at that station*, and an instrument-local comparison needs no range. So the alert can post LOCATION UNKNOWN and she can still know the size in one keystroke. The amplitude beat and the location beat are independent, which is what lets `Amplitude` come before `Examine Crozet hydrophones`.

**The source level needs a location.** Converting received SEL to source SEL requires the range, which requires two stations. So the sentence *this is bigger than anything that has ever happened* is not available until Crozet is associated — and for the Amundsen event it is not available for sixty-two minutes.

### 8b. The four events

Source SELs assigned by shelf area, not linearly — radiated energy depends on the fracture process and the coupling as much as on how much ice there is. Transmission loss is spherical to 1 km then cylindrical, plus 5×10⁻⁴ dB/km absorption at 4–11 Hz, plus 8 dB excess for crossing the Antarctic shelf and coupling into the sound channel. Peak pressure assumes a crest factor of 4 for a swept broadband arrival.

Band ambient at 4–11 Hz is about 90 dB re 1 µPa, so **the noise floor over a 340 s window is 115 dB re 1 µPa²·s** and a station detects at roughly 125.

**Prydz Bay / Amery** — ~62,000 km². Source SEL **263 dB re 1 µPa²·s @ 1 m** (RMS source level 238 dB re 1 µPa @ 1 m), 340 s.

| station | range | received SEL | peak | over noise |
|---|---|---|---|---|
| HA04 Crozet | 2,806 km | **159.1** | 19.6 Pa | +44 dB |
| HA01 Cape Leeuwin | 4,675 km | **156.0** | 13.6 Pa | +41 dB |
| HA10 Ascension | 9,415 km | 150.6 | 7.3 Pa | +36 dB |

**Weddell / Filchner-Ronne** — ~430,000 km². Source SEL **266**, RMS SL 241, 340 s.

| station | range | received SEL | peak | over noise |
|---|---|---|---|---|
| HA09 Tristan da Cunha *(T)* | 4,669 km | 159.0 | — | +44 dB |
| HA04 Crozet | 6,242 km | 156.9 | 15.2 Pa | +42 dB |
| HA10 Ascension | 7,780 km | 155.2 | 12.5 Pa | +40 dB |
| HA08 Diego Garcia | 10,964 km | 152.1 | 8.8 Pa | +37 dB |

**Amundsen / Thwaites–Pine Island** — ~13,000 km². Source SEL **256**, RMS SL 231, 350 s.

| station | range | received SEL | peak | over noise |
|---|---|---|---|---|
| HA03 Juan Fernández | 4,920 km | 148.6 | 5.8 Pa | +34 dB |
| HA06 Socorro *(T)* | 10,412 km | 142.6 | — | +28 dB |
| HA11 Wake | 11,394 km | 141.7 | 2.6 Pa | +27 dB |
| HA02 Queen Charlotte *(T)* | 14,390 km | 139.2 | — | +24 dB |

**Ross** — ~500,000 km². Source SEL **267**, RMS SL 242, 340 s.

| station | range | received SEL | peak | over noise |
|---|---|---|---|---|
| HA03 Juan Fernández | 7,517 km | 156.5 | 14.5 Pa | +41 dB |
| HA11 Wake | 10,862 km | 153.2 | 9.9 Pa | +38 dB |
| HA06 Socorro *(T)* | 11,934 km | 152.3 | — | +37 dB |
| HA02 Queen Charlotte *(T)* | 15,057 km | 149.7 | — | +35 dB |

**T-phase stations do not report pressure.** They are seismometers, so their amplitude is **ground velocity in nm/s**, and the acoustic-to-seismic conversion efficiency at an island flank is site-specific and poorly constrained. These arrivals land in the order of a few hundred nm/s. If you want a number on the page use one, but **no character may back out a source level from a T-station**, because the conversion loss is not known to better than 10 dB.

### 8c. Her scale, at HA01

The whole force of the amplitude beat is the comparison, so it needs a fixed reference.

| | received SEL at HA01 | peak | implied source level |
|---|---|---|---|
| noise floor, 340 s window | 115 | 0.03 Pa | — |
| ordinary iceberg tremor | 118 | 0.17 Pa | 200 dB re 1 µPa @ 1 m |
| **her largest ice signal in six years** | **126** | **0.43 Pa** | 208 dB re 1 µPa @ 1 m |
| **this one** | **156** | **13.6 Pa** | **238 dB re 1 µPa @ 1 m** |

**Thirty decibels over the largest thing she has ever seen. A thousand times the energy, thirty-two times the pressure.** *Three orders of magnitude too large*, exactly as written, and now with a unit behind it.

The peak pressure is the y-axis she looks at: her scale has been a fraction of a pascal for six years and this trace is at fourteen. **Neither station clips** — an IMS hydrophone runs to roughly 160 dB re 1 µPa — which is why she can read a number at all, and why the destruction in §7 has to come from hours of sustained drive rather than from the peak. Those two facts have to stay consistent: she gets an amplitude, and then the instrument dies.

### 8d. The first one sounded biggest and was third

| event | first station | range | received SEL | source SEL |
|---|---|---|---|---|
| Prydz | HA04 | 2,806 km | **159.1** | 263 |
| Weddell | HA09 | 4,669 km | 159.0 | 266 |
| Ross | HA03 | 7,517 km | 156.5 | **267** |
| Amundsen | HA03 | 4,920 km | 148.6 | 256 |

**Apparent order, loudest first: Prydz, Weddell, Ross, Amundsen.**
**Actual order, largest first: Ross, Weddell, Prydz, Amundsen.**

The Prydz collapse posts the loudest arrival on Day 0 because it happened 2,806 km from a microphone. The Ross collapse is the largest of the four by a factor of two and a half in radiated energy and arrives third, because the nearest station that can hear it is 7,500 km away.

**And the ranking is not available to anybody on Day 0.** Ordering the four by size means back-propagating each to a source level, which means locating each, which means two stations each — so the Amundsen cannot be ranked until 16:47Z and the Ross not until about 17:52Z. By the time anyone could put the four in order, the Prydz Channel Fan has been running for two and a half hours.

This is the same error as the fan argument, one act early. A source a hundred kilometres wide has no meaningful level at one metre, and a source that runs eight hundred kilometres does not radiate like a point. **The book gets to make that mistake twice, correctly, and only name it the second time.**

### 8e. Paste-ready

Oscar, after `Amplitude` — she reads a y-axis, so pressure:

> Peak 13.6 Pa. Sound exposure level 156 dB re 1 µPa²·s over 340 seconds.

Edgar's blocks — an institution reports SEL and says where it stands:

> Sound exposure level 156.0 dB re 1 µPa²·s, 340 s. Largest on this instrument's record.

> Sound exposure level 156.9 dB re 1 µPa²·s, 340 s.

> Sound exposure level 148.6 dB re 1 µPa²·s, 350 s. Single-station detection. No origin, therefore no source level.

That last line is the one that earns its place. An institutional assistant reporting, correctly and without comment, that it cannot tell you how big the thing was because it cannot tell you where it was.

---

## 9. Open

1. **HA01's back-azimuth: 206°, or leave 189° alone?** No character ever computes a bearing on the page, so nothing in the book will contradict it. One digit either way.
2. **Crozet's Weddell arrival: move the posting to 11:15Z, or move the origin to 09:41Z?** The posting is cheaper — it costs *six hours* → *seven hours* in Daniel's line and nothing else.
3. **The Amundsen single-station block (§5d)** is the substantive change and the one I would take. Yes or no.
4. **Tristan da Cunha in Daniel's morning (§5e)** — one more Analyst block, or leave the Weddell to Crozet alone.
5. **Ross's origin hour is free.** Nothing anywhere fixes it. On a 15:50Z failure it is detected 17:15Z and located 17:52Z — that is 13:15 and 13:52 in Silver Spring, which puts both inside the hour after Nālani's call. Available, and unusually cheap.
6. **Crozet: blinded or dead?** §7c. Blinded is the better version and makes *three hydrophones* load-bearing; dead buys you a 35-minute window in which the Weddell has a place and no time.
7. **Does Nālani register the two dead triads in S1?** §7f. It is the largest single fact available to her that night and it does not take her anywhere near the fans.
8. **Source SELs are mine, assigned by shelf area** — 263 / 266 / 256 / 267 for Prydz, Weddell, Amundsen, Ross. The *relative* order is the thing to rule on, because it decides whether the first collapse is also the biggest. It currently is not, and §8d argues that is worth more than the alternative.
9. **Does anybody notice, on the page, that the four cannot be ranked until each is located?** It is Sandoval's kind of observation and it is free at the end of Day 0, when three of the four finally have source levels and the fourth still does not.
