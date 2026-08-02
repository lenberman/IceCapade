# S3 against circumpolar-arrivals.xlsx

Every conflict between `lyx/ice.lyx` section S3 and `reference/circumpolar-arrivals.xlsx`. Built against the workbook's deep-water case (F13/F14 = 198.1), which is what the cells currently hold. Items that flip under the shelf-speed variant are marked **[soft]**. Nothing has been applied to the manuscript or the workbook.

## 0. Decide the in-embayment speed first

The Assumptions sheet calls the mouth-to-front leg "the soft number, and it is the one to argue about," and it changes which shelf is last.

| | Deep water, 198.1 m/s | Shelf, 70 m/s |
|---|---|---|
| Prydz | 03:20:00Z | 03:20:00Z |
| Ross | 11:35:43Z | 13:54:17Z |
| Weddell | 13:09:23Z | 16:29:31Z |
| Amundsen | 15:00:00Z | 15:00:00Z |

The Amundsen has a zero-length in-embayment leg, so it does not move. Under deep water it is fourth; under shelf speed the Weddell is fourth and the Amundsen third. A realistic mix — deep water to the shelf break, then shelf — lands between the two, and the workbook says so.

The consequence for S3 is large. At the 15:00Z open, deep water gives Nālani three shelves down and all three located. Shelf speed gives her Prydz located, Ross collapsed but not yet audible (HA03 hears it at 15:18Z), the Amundsen going at that instant, and the Weddell ninety minutes ahead of her. The second is closer to the scene as written.

## 1. State of the world at 15:00:00Z — deep-water case

| Event | Collapse | First detection | First location | Later confirmations |
|---|---|---|---|---|
| Prydz | 03:20:00Z | HA04 03:51:36Z | HA01 04:12:36Z | HA10 05:05:48Z |
| Ross | 11:35:43Z | HA03 13:00:19Z | HA11 13:37:49Z | HA06 13:49:49Z, HA02 14:24:55Z |
| Weddell | 13:09:23Z | HA09 14:01:58Z | HA10 14:36:58Z | HA08 15:12:40Z |
| Amundsen | 15:00:00Z | HA03 15:55:18Z | HA06 16:57:00Z | HA11 17:08:00Z, HA02 17:41:36Z |

Weddell first location is HA10, not the workbook's HA04, because S1 destroys the Crozet hydrophone. Blind interval 35:00, not the 17.7 minutes on the Arrivals sheet.

In Hilo local, the overnight buzz sequence Nālani slept through is 03:00:19, 03:37:49, 03:49:49, 04:01:58, 04:24:55, 04:36:58, and one at 05:12:40 while she is making coffee.

## 2. Conflicts in the live prose

**2.1 "Oscar buzzed me at ten past one" — 11:10Z.** Nothing is at 11:10Z. The line was computed off the superseded Weddell origin of 09:40Z plus HA10's 87.6-minute transit, which gives 11:07.6Z. On the corrected origin the same notice lands at 14:36:58Z, or 04:37 Hilo. The first thing that buzzes overnight is HA03 at 13:00:19Z, or 03:00 Hilo. **[soft]**

**2.2 "HA09, Tristan da Cunha, T-phase, 2031-05-15T10:33Z" should be 14:01:58Z.** Off by 3h29m. This also contradicts S2, which already carries 14:01Z in the priority header. Same event, same chapter, two times. **[soft]**

**2.3 "origin: Weddell 2031-05-15T09:40Z" should be 13:09:23Z.** Off by 3h29m, and contradicts S2's 13:09Z. **[soft]**

**2.4 "Located via Ascension (HA10) back-azimuth 190°" is correct.** Workbook gives 189.8. Do not touch it. The HA09-time-crossed-with-HA10-bearing method is also correct: the Detect vs Locate sheet's rule line says one hydrophone plus one T-station locates.

**2.5 The "Amplitude:" bullet cannot come from HA09.** Tristan da Cunha is a T-phase station — a seismometer on an island. The workbook is explicit: "T-phase stations are seismometers and report ground velocity, not pressure. No source level may be derived from one," and it leaves the peak-pressure column blank for every T-phase row. Ascension is a hydrophone and is already in her solution, so attributing the amplitude to HA10 fixes it at no cost.

**2.6 "The event had been large, but not like Prydz" is backwards.** Back out source level from the workbook's own model — spherical spreading to 1 km, then cylindrical, plus 5e-4 dB/km absorption and 8 dB shelf-coupling excess — and all four stations agree to within 0.07 dB per event:

| Event | Source SEL (dB re 1 uPa^2 s) |
|---|---|
| Ross | 267.0 |
| Weddell | 266.0 |
| Prydz | 263.0 |
| Amundsen | 256.0 |

The Weddell is 3 dB above Prydz at source — twice the radiated energy — and Ross is 4 dB above it. Prydz is third of four. The comparison needs no model at all if you use Ascension, which heard both: Prydz arrived at 150.6 dB, the Weddell at 155.2 dB, same instrument, same site, 4.6 dB louder.

What made Prydz feel enormous was range, not size. Crozet sat 2,806 km away and clipped. The honest line is that the Weddell was bigger and further off, and the only reason it did not pin the needle is that nothing was close to it. That reads better than what is there now and it costs one sentence.

**2.7 "two so close in time and nothing to link them" should be three.** Ross was detected at 03:00 Hilo and located at 03:38 Hilo, both while she slept. She wakes to three located events, not two, and the three of them are already in circumpolar order. **[soft — under shelf speed she genuinely has two, but the second is Ross, not the Weddell]**

**2.8 "It was 05:45:00" — nothing arrives at 15:45Z.** The next notice is HA03/Amundsen at 15:55:18Z, ten minutes later. See 4.3 for what this costs.

## 3. Conflicts in the `Draft` branch

**3.1 "I ran the Crozet solution again by hand."** Crozet is dead from 03:51Z and the Weddell solution is HA09 crossed with HA10. There is no Crozet solution to re-run. Should be Tristan, or Ascension.

**3.2 "Two shelves, six hours and forty-five minutes apart" should be three shelves, and Prydz to Weddell is 9h49m.** The 6h45m figure is the superseded 10:05Z Weddell. **[soft]**

**3.3 "At a quarter to six the sun came up over the water and Oscar buzzed and they were the same minute."** Sunrise at Hilo on 15 May 2031 is 05:44:54 HST, so the sun is right. The buzz is not: HA03 posts the Amundsen at 15:55:18Z, or 05:55 Hilo.

**3.4 "Back-azimuth 196" should be 193.7.**

**3.5 "origin in the Amundsen embayment at ten to three Greenwich" — 14:50Z against the workbook's 15:00Z.** Ten minutes, and it is inside the workbook's own error band: the Amundsen path is stated as "~8,400-8,600 km," a 200 km spread that is 17 minutes at 198.1 m/s. 14:50Z back-solves to 8,201 km, about 120 km under the stated low end. This is the one conflict where moving the workbook is as defensible as moving the manuscript. Your call, but pick one and write it down.

**3.6 One hydrophone cannot produce an origin time.** This is the real problem with the Juan Fernández beat, and the Conflicts sheet does not record it. The Detect vs Locate sheet has HA03/Amundsen as "DETECTED — bearing only, a ray." Location waits for HA06 at 16:57:00Z, two hours later. At 15:55Z she has a direction and nothing else. See 4.2.

**3.7 "Three shelves. Three oceans." should be four shelves.** Three oceans still holds — the Amundsen and Ross are both Pacific.

**3.8 "The fourth came in at twenty past six and it was not a sound at all... Nobody had heard the Ross shelf go, because there was no instrument in the right place to hear it."** Ross is the loudest event of the four at source and the best-heard of the four in the water: two CLEAR paths, HA03 at 41 dB over noise and HA11 at 38 dB, plus HA06 and HA02 marginal. It is detected at 13:00:19Z and located at 13:37:49Z, and under the deep-water case it is second, not fourth. The beat as written has no support anywhere in the workbook. See 4.1.

**3.9 "Prydz at twenty past three. The Weddell at five past ten. The Amundsen at ten to three. The Ross sector somewhere in the last six hours with nobody's name on the time."** Prydz correct. Weddell 13:09, not 10:05. Amundsen 15:00, not 14:50, subject to 3.5. Ross 11:35:43, and HA11 put a name on it at 13:37:49Z.

**3.10 Daniel: "Eight hours and forty degrees apart."** Eight hours is right for Prydz to Ross — 8h15m. Forty degrees is not: the workbook puts Ross 107 degrees east of Prydz along the wave path, which at 47.0 km per degree at 65S is the 5,029 km on the Assumptions sheet. A hundred degrees, or a hundred and seven. **[soft]**

**3.11 The four notices she reads back to him.** Currently "Cape Leeuwin at twelve past four, Crozet at ten to eleven, Juan Fernández at a quarter to four, and the Pacific centre's statement at twenty past." Cape Leeuwin is correct. Crozet at 10:50Z does not exist in any ordering and Crozet is dead besides. The Pacific centre statement is 3.8. On the corrected timings the four first-locations are Cape Leeuwin 04:12Z, Wake 13:37Z, Ascension 14:37Z, and Juan Fernández 15:55Z — and the fourth is a bearing only, which is worth keeping rather than hiding, because it lets Daniel push on it.

**3.12 "about seven hundred kilometres an hour" is correct.** sqrt(9.81 x 4000) = 198.09 m/s = 713 km/h. Matches the Assumptions sheet exactly. Do not touch it.

## 4. Three that are not find-and-replace

**4.1 The unheard shelf does not exist.** Every one of the four is detected acoustically, and the quietest of them, the Amundsen, still clears the noise floor by 27 dB at Wake and 34 dB at Juan Fernández. If you want a shelf that is seen and not heard, the workbook cannot give you one, and the "no time on it" beat has to be rebuilt or cut. The nearest honest substitute is the Amundsen's two-hour gap between bearing at 15:55Z and location at 16:57Z: heard, unmistakably, and still unplaceable.

**4.2 "In order. Around a circle." is no longer the geometry.** Ross is 107 degrees east of Prydz, the Weddell is 123 degrees west, and the Amundsen is where the two branches converge at 178 to 182 degrees. Nothing sweeps. Two arms open in opposite directions from Prydz and close on the far side of the continent, and the collapse order is east, west, then both. The clock face can survive if the marks read as symmetric about the Prydz-Amundsen axis rather than as a sweep hand — and the symmetry is stronger evidence than the sequence was, because no random set of four does that.

**4.3 The Amundsen is rung twice, and S3 does not use it.** The Assumptions sheet: the eastward and westward branches arrive at the Amundsen roughly 15:00Z and 15:15Z, "the only place on Day 0 where one shelf is hit twice." Juan Fernández hears them at 15:55:18Z and 16:10:18Z — fifteen minutes apart, same signature, both inside S3's morning. The workbook's own note calls this "a signature no single collapse can produce, and the hardest evidence available to anyone on Day 0 that the four events are one mechanism." It is currently on the floor. It would also give the phone call something it does not have: a measurement Daniel cannot explain away, arriving while they are still on the line.

Against that, 2.8 and 3.3 cost you something real. Sunrise at 05:45 and Oscar buzzing in the same minute is a good image and the corrected arrival is at 05:55. Nothing lands at 05:45. Either lose the coincidence, or let the sun come up on her ten minutes of waiting for it.

## 5. Noticed while reading, not xlsx conflicts

The subsection head reads "Hilo Bay 2031-05-15T05:00:00-10:00" where S1 and S2 carry a bare local ISO stamp with no place name.

There is an unpaired closing quote inset in the Ascension bullet in the live prose.

The `Draft` branch still carries its markdown staging marks throughout — fenced backticks, `**bold**`, `>` quote levels, a `##` heading and a `---` rule — plus a stray backtick after the S3b timestamp.

Daniel goes to lunch at 14:40Z, takes Nālani's call around 16:30Z, and sits down at his desk at 17:20Z. That is a two-hour-forty lunch. It is not a workbook conflict, but the corrected arrival times stretched it and it may want a line.
