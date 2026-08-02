# Calendar — the anchored dates

**D+8 = Friday, 23 May 2031**, the Friday before Memorial Day (Monday 26 May 2031). Everything else follows.

**D0 = Thursday, 15 May 2031**, UTC — the date of the Amery failure at 03:20Z.

2031 shares its calendar with 2025 exactly. The US Naval Academy held its graduation and commissioning ceremony on Friday 23 May 2025 at 10 a.m. at Navy–Marine Corps Memorial Stadium, so the 2031 ceremony falls on **D+8 itself**.

---

## 1. Time zones

| Place | Zone | Offset | DST |
|---|---|---|---|
| Hilo | HST | UTC−10 | **never** — Hawaiʻi does not observe DST |
| Silver Spring / Annapolis / Currituck | EDT in May | UTC−4 | yes, EST = UTC−5 Nov–Mar |
| Davis station, Antarctica | — | UTC+7 | — |
| Perth (Marcus Yee, HA01 side) | AWST | UTC+8 | no |

**Silver Spring is 6 hours ahead of Hilo** through the fortnight, because May is EDT. In Part Four winter scenes it is **5**. This is the one offset that changes across the book.

---

## 2. Notation

Two registers, never mixed in one string.

**Machines speak UTC only.** Oscar's screen, IMS notices, IERS bulletins, tide gauges, seismic bulletins, ship's logs: `04:12:07Z`, or with the date `2031-05-15T04:12:07Z`. This is what those systems actually publish and the manuscript already does it correctly.

**People speak local, with no offset.** Narration and dialogue: *ten past six*, *nine at night*. Nobody thinks in offsets.

**The subsection head carries both, and the day.** Proposed form:

> **D−1 · Wed 14 May 2031 · Hilo · 18:12 HST (15 May, 04:12Z)**

A note on `Thh:mm:ssZ+dd`: it will not do what you want, because in ISO 8601 the `Z` **is** the offset — it means +00:00. Writing `Z+10` is malformed, and this book's reader is exactly the reader who will notice. Valid ISO gives you local-plus-offset in one string — `2031-05-14T18:12:07-10:00` — from which UTC is one subtraction, but it never displays the UTC.

More importantly, the offset is not the thing that confuses people. **The date rollover is.** Hilo at six in the evening on Wednesday is already Thursday in Greenwich, and that is the trap in every scene of Part One. Any format that shows the offset but hides the day flip solves the easy half of the problem. Hence the day marker and both dates above.

If you want something terser, use an arrow rather than a second offset sign: `04:12:07Z −10 → 14 May 18:12 HST`.

---

## 3. The fortnight

Local columns are the same instant, not the same clock reading.

| | UTC date | Day | Hilo | US East |
|---|---|---|---|---|
| **D−1** | 14 May | Wed | S1 evening, 18:12 HST | — |
| **D0** | 15 May | **Thu** | 03:20Z = Wed 17:20 HST | 03:20Z = Wed 23:20 EDT |
| D+1 | 16 May | Fri | Hilo harbor, 02:40 HST | Crary wave ~13:00 EDT |
| D+2 | 17 May | Sat | | Bengal Fan |
| D+3 | 18 May | Sun | | Norway |
| D+4 | 19 May | Mon | | Sandoval's forward |
| D+5 | 20 May | Tue | | Makran, Mw 8.2 |
| D+6 | 21 May | Wed | | Currituck argument |
| D+7 | 22 May | Thu | | evacuation order; Ellen drives down |
| **D+8** | **23 May** | **Fri** | | **Currituck slide · USNA graduation** |
| D+9 | 24 May | Sat | | |
| D+10 | 25 May | Sun | | IERS bulletin |
| D+11 | 26 May | **Mon** | | **Memorial Day** |
| D+12 | 27 May | Tue | | the hinge |

Two free gifts in that table. **The hinge falls the day after Memorial Day** — the country goes back to work and the gauges have not come down. And **D+11 is Memorial Day itself**, three days after a wave took the Virginia–Carolina coast, which is either unusable or the best chapter in Part Three.

## 2a. Subsection strings — the running list

Scene heads use plain ISO 8601 local-with-offset. **Offsets west of Greenwich are negative.**

| Scene | Section | Subsection string | = UTC | |
|---|---|---|---|---|
| S1 | Waiākea | `2031-05-14T17:20:00-10:00` | 15 May 03:20Z | in `ice.lyx` |
| S2 | Silver Spring | `2031-05-15T07:00:00-04:00` | 15 May 11:00Z | in `ice.lyx` |
| S2 | Silver Spring | `08:30:00-04:00` | 15 May 12:30Z | in `ice.lyx`, short form |
| S3a | *(open — Waiākea?)* | `2031-05-15T05:00:00-10:00` | 15 May 15:00Z | proposed |
| S3b | same section | `2031-05-15T13:20:00-04:00` | 15 May 17:20Z | proposed |

**S2's second head uses a short form** — `08:30:00-04:00`, time-only, no date. That is a reasonable house rule for a second subsection inside one scene on one day, and it dodges the cost noted below by never re-stating a date the reader might misread. If you want it as the rule, S3b becomes `13:20:00-04:00` — but note that S3 changes *hemisphere* between its subsections and not merely hour, so the full date-and-offset string is doing more work there than it does in S2.

**S3's two heads are 6 h 20 m apart on the page and 2 h 20 m apart in the world**, in opposite directions — hers reads 05:00 and his reads 13:20, and his is the later. That is the sharpest instance in Part One of the thing §2 says the heads exist for.

**S1 currently reads `+10` and needs to be `-10:00`.** Hilo is UTC−10; `+10` is Vladivostok. Use the two-digit minute field — `-10:00` rather than `-10` — because RFC 3339 requires it and every parser accepts it.

S1's 17:20 is the instant the Amery front lets go, which is also roughly when she is at the stove. Good choice: the head timestamps the thing the reader does not yet know about.

### The one cost of local-with-offset

S1 reads 05-14 and S2 reads 05-15, so the date advances — but only **7 hours 40 minutes** of story passes between them. A reader may infer a day where there is a third of one. This bites hardest at exactly these two heads, because they are the reader's first two.

**Decided: local-with-offset, uniformly, for every scene and both POVs.** Daniel and Edgar work in UTC (Scenes ledger #37), but that habit lives inside his narration and Edgar's output — it does not reach the scene heads. The apparatus stays one thing.

The three options, kept for the record:

- **Local + offset (current).** The reader gets each character's own clock and has to do the subtraction. The book is *about* a planet whose local clocks disagree — Part One's engine is four sectors failing on one UTC day that is four different local days — so making the reader feel that in the heads is the right kind of work. Oscar's screen supplies Z whenever precision actually matters.
- **UTC throughout.** `2031-05-15T03:20:00Z`, `2031-05-15T11:00:00Z`. Elapsed time becomes trivial; the local evening goes cold.
- **Both.** `2031-05-14T17:20:00-10:00 (03:20Z)`. Unambiguous, and it clutters the top of every scene.

## 3a. S1 — the evening in Hilo, minute by minute

Wednesday 14 May 2031. Hilo sun: **sunset 18:48 HST**, civil twilight ends **19:12**. Solar noon 12:16.

| Hilo | UTC | What |
|---|---|---|
| ~17:00 | 03:00Z | Nālani at the stove. Tūtū watching the clouds, sun descending. |
| **17:20** | **03:20Z** | **The Amery front lets go.** Nobody in the house knows, and nobody anywhere knows for another fifty-two minutes. |
| ~17:30 | 03:30Z | The glaze, the burn, *get me ice*, the table set for three. |
| ~17:45–18:25 | | Dinner. The catechism. Waiākea, 1946, 1960. |
| **18:12** | **04:12:07Z** | HA01 Cape Leeuwin posts the detection notice. Still nobody in the house knows. |
| **18:30–18:55** | 04:30–04:55Z | **Bzzzz.** Free parameter — see below. |
| | | The room. Oscar, the railed trace, Crozet, the hyperbola. Fifteen to twenty-five minutes. |
| 18:48 | 04:48Z | Sunset, whether she is in the room or not. |
| ~19:00–19:20 | | She comes back out. |

**The crack begins while she is cooking.** 17:20 HST is roughly when the Spam goes in the pan. The book never has to say so; a reader who reconstructs it from the subsection heads gets it for nothing.

At Davis station (UTC+7) the same instant is **10:20 in the morning**, in daylight, in the open.

### The one free parameter

Origin → Leeuwin is **fixed physics**: 4,660 km at ~1,485 m/s = 52 minutes. Not adjustable.

Leeuwin → Oscar's buzz is **engineering**: station processing, the data reaching the open feed, her watcher's polling interval. Anything from ten minutes to an hour is defensible and nothing in the book forces a number. So the buzz is placed wherever the scene wants it.

| Lag | Buzz (HST) | Light at the buzz | She returns | Light on return |
|---|---|---|---|---|
| 18 min | 18:30 | sun low, still up | ~18:50 | just after sunset, sky bright |
| 23 min | 18:35 | sun low, still up | ~18:55 | afterglow |
| 33 min | 18:45 | minutes from sunset | ~19:05 | dusk, colour going |
| 43 min | **18:55** | **just after sunset** | ~19:15 | **civil twilight over; dark** |

**Your 18:30–18:45 window needs nothing changed** — 03:20Z origin and 04:12:07Z detection already deliver it on a 18–33 minute lag.

But if the scene wants her to come back out into the dark, push the buzz to ~18:55 on a 43-minute lag, which is if anything the more realistic figure for data reaching a public feed. Note that the suggested closing line in `S2-suggestions`' sibling — *"the light had gone out of the sky while I was in my room"* — is only true on that longer lag. On an 18:35 buzz she returns to afterglow, and the line should be *the light was going* instead.

## 4. Part Four

| Scene | Marker | Date | Notes |
|---|---|---|---|
| S18 | M4 | Sept 2031 | GRACE-FO first solution |
| S19 | Y2 | 2033 | Hilo rebuild hearings |
| S20 | Y6 | 2037 | first stall; Eve 22 |
| S21 | Y9 | 2040 | the surge; Exhibit 14 |
| S22 | Y14 | 2045 | Norfolk; Eve 30 |
| S23 | Y15 | 2046 | the Oʻahu chart; Nālani 59 |
| S24 | ~Y20 | 2051 | the gun; Nālani 64 |
| S25 | Y30 | 2061 | retreat authority; Eve 46 |
| S26 | Y60+ | 2091 | coda; **Lehua 76** ✓ |

Lehua at 76 in 2091 checks out against her being 16 in 2031.

---

## 5. What the anchor breaks

Four conflicts the date exposes. None is drafted into `Scenes.2.md`; all four need your ruling.

### 5a. RESOLVED — Tūtū Ruth is 91

The manuscript now reads *"when Tūtū was six."* Six at the April 1946 wave puts her birth between April 1939 and April 1940, which makes her **91 at Day 0** and **93 in the spring of Y2**. Ledger #10 stands unchanged and no edit is needed anywhere.

Six is also the better age for what the scene does. At eleven she would have understood something; at six she has only the image — the reef, the fish standing on their sides — which is exactly what she hands to Lehua eighty-five years later. And Scenes' beat about her having seen that face before, in 1946, on her own mother, needs a small child looking up at an adult.

*The paragraph below is superseded and kept only so the reasoning is on the record.*

### ~~5a-old. Tūtū Ruth is 96, not 91~~

The manuscript says *"when Tūtū was eleven"* in 1946, which puts her birth in 1934–35 and makes her **96 at Day 0**, not the 91 in Ledger #10. Manuscript wins. Consequences: she dies at 98 rather than 93 in S19 (Y2, 2033), and a 96-year-old is a materially different woman from a 91-year-old — frailer, and more remarkable for directing the packing and getting up to follow her granddaughter down a hall.

Alternative is to change *eleven* on the page. I would not: eleven is the age at which a child remembers the reef and the fish, and six is not.

### 5b. Nobody's Sunday survives

`Scenes.1` calls S1 "Sunday dinner" and `Scenes.2` S7 puts Keala in the lab "at 9 pm on a Sunday." With this anchor, S1 is **Wednesday evening** and S7 is Wednesday night.

I think this is a gain. Lehua reading at the table on a school night is better than Sunday dinner, and an undergraduate in a lab at nine on a Wednesday is more ordinary than on a Sunday. The book's closing argument is that none of this ever presented itself as news — an ordinary Wednesday serves that better than a Sunday does.

### 5c. D+8's hour is free — not a conflict

`FourteenDays.md` §12 puts the failure at 0341Z; `Scenes.2` S15 says mid-afternoon. This is **not** two sources contradicting each other about a fact. It is two chats independently guessing an unfixed parameter, and the parameter is genuinely unfixed.

The Currituck failure is pore-pressure re-equilibration on a fan loaded by the D+1 Crary wave. That clock has no tight constraint — the delay from loading to failure is hours to days and nothing in the physics picks an hour out of it. **So the hour is yours, and graduation day picks it.**

**One thing is fixed: failure → shore.** I previously wrote that Ledger #2's ~40 minutes was "the physical number" and that §12's 89–159 was too long. **That was wrong, and the reasoning behind it was worse than the answer.** I preferred 40 because it sits in the consistency ledger, which `CLAUDE.md` calls the part of Scenes worth trusting — an argument from where a number lives in the file tree, presented as if it were an argument from physics. Both numbers came from chats. Neither had been computed.

Computed now. Source 36.4°N 74.7°W to the Currituck Banks shore near 75.80°W is **99 km**. Transit is ∫dx/√(gh) — roughly 30 km of slope shoaling 1000→100 m, then ~70 km of shelf shoaling 100 m→shore:

| shelf carried to | transit |
|---|---|
| 20 m | 59 min |
| 10 m | 64 min |
| 5 m | 69 min |
| 2 m | 73 min |

So **60 to 75 minutes**, and what each candidate would require as a mean depth over that path:

| | mean speed | implied mean depth |
|---|---|---|
| 40 min | 41.7 m/s | **177 m** — far too deep for a path that is mostly shelf |
| 60 min | 27.8 m/s | 79 m — plausible |
| 89 min | 18.7 m/s | 36 m — slow but defensible |
| 159 min | 10.5 m/s | 11 m — too shallow for the whole path |

**§12 is closer to right and is internally coherent.** Its 89–159 is not a transit range to one place; it is first arrival at the nearest coast (89 min) through the last of the places it lists — Delaware Bay approaches, several hundred kilometres farther. Ledger #2's 40 minutes is the outlier, and it reads like a number chosen for tension rather than computed.

**Recommendation reversed: keep §12 and amend Ledger #2 to ~65 minutes** at the Currituck Banks, with later arrivals northward into the Chesapeake and Delaware approaches.

It costs the book nothing. S15's tension does not come from the forty minutes — Ellen and Eve are already on the causeway because of the D+7 order, and an hour is still nowhere near enough to clear a barrier island cold. If anything an hour is better: long enough that people try to leave, which is why there is traffic to be caught in.

For graduation day: arrival about **15:10 EDT** with ~65 minutes of transit means failure about **14:05 EDT = 18:05Z**. The ceremony is over, the families are still in town, the roads are full.

**Caveats on my own number.** The shallow tail dominates the integral and is sensitive to where you stop; real bathymetry off the Outer Banks is not a linear ramp; and "arrival" is ambiguous between first detectable rise and damaging run-up, which can differ by ten minutes or more. Treat these as estimates with a ±15 minute band, not computed constants.

### 5c-i. The fixed progression

Set the failure hour anywhere you like. Once it goes, the wave walks the coast on this schedule and nothing about the calendar changes it. **T+0 is the failure.**

| | distance | T+ | 14:00 EDT failure |
|---|---|---|---|
| Nags Head | 96 km | 62 min | 15:02 |
| **Currituck Banks / Corolla** | 98 km | **64 min** | **15:04** |
| Virginia Beach oceanfront | 124 km | 86 min | 15:26 |
| Chesapeake mouth, Cape Henry | 131 km | 91 min | 15:31 |
| Cape Hatteras | 148 km | 106 min | 15:46 |
| **Naval Station Norfolk** | +29 km up-bay | **136 min** | **16:16** |
| Hampton Roads / Newport News | +38 km up-bay | 149 min | 16:29 |
| Delaware Bay mouth | 269 km | 206 min | 17:26 |
| **Annapolis / USNA** | +232 km up-bay | **447 min (7.5 h)** | **21:27** |

Open-coast rows use the slope-plus-shelf integration. In-bay rows add propagation from the bay mouth at an effective channel depth of ~12 m, giving about 10.8 m/s — the Chesapeake is shallow and it is slow.

**This vindicates §12 rather than Ledger #2.** §12's advisory names Virginia Beach, the Outer Banks, Hampton Roads and the Delaware Bay approaches, and quotes arrival 0510Z–0620Z — 89 to 159 minutes. Against the table: Virginia Beach 86, Hampton Roads 149. That window maps onto the places §12 itself lists, almost exactly. Whoever wrote §12 computed it. Forty minutes is not the arrival anywhere.

### 5c-ii. Norfolk is the naval base, and Annapolis is not

**Naval Station Norfolk takes the water — around T+136 minutes.** It is the largest naval base in the world; much of the station lies **less than ten feet above sea level**; regional sea level has risen roughly 18 inches since 1930; and it already floods on sunny days from tides alone. The Navy has been raising piers at about $60 million each. So the wave arrives at an installation that has spent thirty years quietly documenting its own drowning, and it arrives for the **second time in eight days** — Scenes S11 already floods Norfolk with the D+1 Crary wave. Two inundations in a week is what makes S22's Y14 dry abandonment inevitable rather than editorial.

**The Academy is a different matter, and the arithmetic is against inundating it.** Annapolis sits 232 km up a shallow bay; the wave needs about seven and a half hours to get there and is stripped and dispersed the whole way. This confirms `EastCoast.md`'s claim about the bent shallow Chesapeake and puts a number on it. On a 14:00 failure the Academy sees something around **half past nine at night**, modest.

Which gives a better D+8 than flooding the Yard would. Graduation ends around noon. The margin fails at two. At quarter past four, while the families of the class commissioned that morning are still in Annapolis, the largest naval base in the world takes water — on their phones, from thirty miles away, and some of those new ensigns have orders to Norfolk. Ledger #3 holds; nobody in the Grier family gets wet, and the horror is entirely watched.

**General rule now that dates are being tracked.** Fixed: acoustic transit (sound speed × distance), tsunami transit (√gh × distance), sunset, tides, anything astronomical. Free: every hour at which a loaded slope decides to let go. Do not audit the free ones.

### 5d. Daniel's PTWC posting lands after the move

Ledger #9 gives him Ewa Beach at 34–40; with D0 in 2031 that is **2014–2020**, and Ledger #12 records PTWC leaving Ewa Beach for Ford Island in **2014**. So virtually his entire posting is at Ford Island, not Ewa Beach.

Three ways out: make him a Ford Island duty scientist and keep one line about having helped carry the operation across (which is better — he watched a warning centre relocate for sea level, and then spent Day 0 arguing there was no wave); age him up so the posting predates 2014; or move Day 0 later, which this anchor forbids.

I would take the first. Eve is still born on Oʻahu either way.

---

## 6. Annapolis on D+8

Graduation day gives you a third thread that is not the cottage and not the ops floor. Worth knowing before you place a family member in it:

Navy–Marine Corps Memorial Stadium sits roughly a mile and a half inland and well above the water, so the ceremony itself is not the peril. **The Yard is** — the Naval Academy campus sits at the mouth of the Severn on the Chesapeake at very low elevation, and it is one of the most frequently cited US federal installations for routine tidal flooding. Verify the specifics before writing, but the pairing is almost too apt: the institution that has been quietly measuring its own drowning for thirty years, commissioning a class on the afternoon the margin fails.

Ledger #3 holds — Daniel never gets wet. Ellen and Eve are on the Currituck causeway (Ledger #4), so the Annapolis relative is a third party: a niece or nephew commissioning, with Daniel's side of the family in the stands. Undecided and yours.

---

## 7. Proposed ledger additions — NOT applied

**#28** *Day 0 is Thursday 15 May 2031, UTC. D+8 is Friday 23 May 2031, the Friday before Memorial Day and the date of the USNA commissioning ceremony. See `Calendar.md`.*

**#29** *Machines speak UTC (`04:12:07Z`). People speak local with no offset. Subsection heads carry both plus the day marker and both dates, because the date rollover is the trap, not the offset. Never `Z+dd` — in ISO 8601 the Z is the offset.*

**#30** *Silver Spring is 6 hours ahead of Hilo in May (EDT), 5 in winter. Hawaiʻi never observes DST.*

**#31** *Tūtū Ruth is **96** at Day 0, born 1934–35, eleven at the 1946 wave per the manuscript. Amends #10. She dies at 98 in S19.*

**#32** *S1 and S7 are a **Wednesday**. Remove "Sunday dinner" from `Scenes.1` and "9 pm on a Sunday" from S7.*

**#33** *D+8 mid-afternoon EDT, per S15. `FourteenDays.md` §12's 0341Z is superseded; failure ~1830Z, arrival ~1910Z, restoring the forty-minute figure in #2.*

**#34** *Daniel's PTWC posting is Ford Island, not Ewa Beach — the relocation happened in 2014, inside his tour. Amends #9 and #12.*
