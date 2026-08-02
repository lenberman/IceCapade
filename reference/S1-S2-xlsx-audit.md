# S1 / S2 against circumpolar-arrivals.xlsx

Audit of `lyx/ice.lyx` sections *Waiākea* (S1) and *Silver Spring* (S2) against all six sheets of `reference/circumpolar-arrivals.xlsx`. S3 excluded by instruction. Nothing here has been applied to the manuscript or to the workbook.

## Defects in the manuscript

**1. `HA13` should be `HA03`.** S2, *Expand 2*: "Juan Fernández (HA13) posted at 2031-05-15T13:00Z". No HA13 exists — the network is HA01 through HA11, and the workbook's Transit matrix lists Juan Fernández as HA03. The priority line three lines earlier and the later Ross-location block both say HA03 correctly.

**2. HA03 carries Wake's timestamp.** S2, Ross location block: "Juan Fernández (HA03) posted at 2031-05-15T13:37Z, back-azimuth 201.0". Workbook has HA03/Ross at 13:00:19Z; 13:37:49Z is HA11 Wake, listed on the immediately preceding line. HA03's 13:00Z arrival is what raised the priority item in the first place, so it cannot also be 13:37Z. Bearing 201.0 is correct.

**3. HA09 carries the same 13:37Z, in two places.** S2, both Weddell *Expand* blocks: "Tristan da Cunha (HA09) posted at 2031-05-15T13:37Z". Contradicts the priority header one line above ("IMS HA09 Tristan da Cunha:: 14:01Z T-phase") and the workbook (14:01:58Z). This one propagates: the Weddell fix is HA09's arrival time crossed with Ascension's back-azimuth, and ΔT(HA09→HA10) is 35 minutes at 14:01Z but 60 minutes at 13:37Z, which would not resolve to the Weddell.

**4. "two events, six hours apart" is stale.** S2, Daniel's reaction to the second priority item. Six hours belongs to the superseded ordering, where the Weddell collapsed second at 10:05Z. As the scene now stands he is comparing postings at 03:51Z and 13:00Z — nine hours and nine minutes — which resolve to origins at 03:20Z and 11:35Z, eight hours and fifteen minutes. S3 already says "eight hours," which suggests this line simply did not get migrated.

## Required workbook modification

**Crozet is dead from 03:51Z and the sheets do not know it.** S1 establishes the HA04 hydrophone as destroyed by the Prydz arrival ("the waveform of a damaged hydrophone"), and S2 confirms it ("query to Crozet: Is your 0351 event ongoing? No response"). S2 therefore locates the Weddell via Ascension (HA10) at 14:36Z. The *Arrivals* sheet still gives the Weddell a first location of HA04 at 14:19:39Z, and *Detect vs Locate* still shows HA04 as the LOCATED row for the Weddell with back-azimuth 210.2. The Conflicts sheet anticipates this as a parenthetical under #3 but the calculation sheets never apply it. The manuscript is internally consistent; the workbook needs the HA04 row suppressed for every event after Prydz, with the Weddell's blind interval recomputed from 14:01Z to 14:36Z (35 minutes, not 17.7).

## Stale entries on the Conflicts sheet

- **#1 (order of collapse)** — resolved in the workbook's favour. S2 now runs Prydz, then Ross at 11:35Z, then the Weddell at 13:09Z.
- **#2 (Weddell at 10:05Z)** — gone. The manuscript now says 13:09Z, matching the deep-water leg exactly.
- **#3 (Crozet posts the Weddell at 10:51Z)** — gone. The manuscript no longer routes the Weddell through Crozet at all.
- **#7 (HA01 back-azimuth 189°)** — fixed. S1 says 205°, S2 says 205.7.
- **#4, #5, #6** concern the Amundsen and the PTWC statement, neither of which appears in S1 or S2. Not assessed.

## Confirmed correct

Prydz: HA04 03:51Z / 157.5, HA01 04:12Z / 205.7, origin Prydz Bay 03:20Z, ΔT 21 minutes, Leeuwin transit 52 minutes against the workbook's 52.6. Ross: HA03 13:00Z / 201.0 detecting, HA11 13:37Z / 183.6 locating, origin 11:35Z. Weddell: HA09 14:01Z as a T-phase detection with no bearing (matching the workbook's "DETECTED — one arrival time, nothing"), HA10 14:36Z / 189.8, origin 13:09Z. Waveform 11 Hz to 4 Hz over 340 s throughout, consistent with the 340 s noise window on *Paths & Amplitude*. Daniel's local clock holds: beepers "just after ten" for 14:01Z, "nine forty" for a 13:37Z arrival Edgar took three minutes to expand.

## Cosmetic, optional

- S1 gives Cape Leeuwin as `205°`; 205.7 rounds to 206. Truncation is defensible for a display value.
- S1's `T03:51:07Z` and `T04:12:07Z` run about 29 seconds ahead of the workbook's 03:51:35.7 and 04:12:36.3. ΔT stays at exactly 21 minutes either way, so nothing downstream moves, and the workbook's sub-minute precision is spurious anyway — it inherits from a T0 of 03:20:00.096.

## Question, not a finding

S1 has Oscar report "Davis stopped at three nineteen" against T0 = 03:20Z — the station drops one minute before the collapse. Deliberate precursor, or should it join the others at three twenty? Not a spreadsheet conflict either way.
