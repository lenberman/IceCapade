# The in-embayment speed — what an intermediate value buys

Working note on setting F13/F14 in `circumpolar-arrivals.xlsx` to something between the two extremes. Nothing applied to the workbook or the manuscript.

## The one number that matters

The collapse order Prydz, Ross, Weddell, Amundsen holds for any in-embayment speed **above 98.48 m/s**. Below that the Weddell front crosses 15:00:00Z and the Amundsen goes third, Weddell fourth.

Derivation: the wave reaches the Weddell mouth at 11:19:59.8Z and the front is 1,300 km further in. The Amundsen front is fixed at 15:00:00Z because its in-embayment leg is zero, so it does not move with F13/F14 at all. Setting the two equal needs 1,300,000 m / 13,200.2 s = 98.48 m/s.

At 110 m/s the Weddell front lands at 14:36:57Z, 23 minutes clear of the Amundsen. That is the whole margin.

**Ross is second at every speed from 70 to 198.1.** The load-bearing item on the Conflicts sheet is robust across the entire range and does not depend on this choice.

## What 110 m/s means physically

The honest construction is a two-segment path — deep water out to the shelf break, then shelf — with the legs summed as times, not speeds averaged. For an effective 110 m/s the split is 56% at 198.1 m/s and 44% at 70 m/s. On the Ross leg that is 506 km deep and 394 km shelf; on the Weddell leg, 731 km and 569 km.

| Effective v | Deep / shelf split | Equivalent mean depth |
|---|---|---|
| 70.0 | 0% / 100% | 499 m |
| 98.5 (flip) | 45% / 55% | 989 m |
| 110.0 | 56% / 44% | 1,233 m |
| 116.0 | 61% / 39% | 1,372 m |
| 130.0 | 71% / 29% | 1,723 m |
| 198.1 | 100% / 0% | 4,000 m |

The caveat to keep in view: the Ross and Ronne shelves are both genuinely wide, several hundred kilometres each, so a shelf fraction above 44% is arguable on the geography. At 55% shelf the order flips. This is a defensible choice, not a forced one, and the Assumptions sheet already says as much — but it should be recorded as a choice.

## Timetable at 110 m/s

Collapse at the front: Prydz 03:20:00Z, Ross 12:36:22Z, Weddell 14:36:57Z, Amundsen 15:00:00Z with the second branch at 15:15Z.

| Event | Detect | Locate | Confirm |
|---|---|---|---|
| Prydz | HA04 03:51:36Z | HA01 04:12:36Z | HA10 05:05:48Z |
| Ross | HA03 14:00:58Z | HA11 14:38:28Z | HA06 14:50:28Z, HA02 15:25:34Z |
| Weddell | HA09 15:29:33Z | HA10 16:04:33Z | HA08 16:40:15Z |
| Amundsen | HA03 15:55:18Z | HA06 16:57:00Z | HA11 17:08:00Z, HA02 17:41:36Z |
| Amundsen, 2nd branch | HA03 16:10:18Z | | |

HA04 is dead from 03:51Z, so the Weddell locates on HA10, not HA04. Blind intervals are unchanged by the speed choice — they depend only on transit differences: Ross 37.5 min, Weddell 35 min, Amundsen 62 min.

## Nālani's morning, Hilo local

| | |
|---|---|
| 04:00:58 | HA03 — Ross, bearing only |
| 04:38:28 | HA11 — Ross located |
| 04:50:28 | HA06 confirms Ross |
| 05:00 | she wakes |
| 05:25:34 | HA02 confirms Ross, as she sits down |
| 05:29:33 | HA09 — a new one, T-phase, no bearing, unplaceable |
| 05:44:54 | sunrise |
| 05:55:18 | HA03 — a bearing into the Amundsen |
| 06:04:33 | HA10 — the 05:29 event resolves: the Weddell |
| 06:10:18 | HA03 again — same signature, fifteen minutes after the first |
| 06:40:15 | HA08 confirms the Weddell |

She wakes to Prydz and Ross both located and the other two still in her future. Everything after 05:25 happens live at the desk. The Weddell arrives as a mystery and stays one for 35 minutes. The double ring at the Amundsen lands last, six minutes after the Weddell resolves — so she picks up the phone holding the strongest single piece of evidence on Day 0, and it is the freshest thing she has.

## Daniel's morning, EDT

| | |
|---|---|
| ~09:00 | arrives; one overnight event on the desk, Prydz |
| 10:00:58 | HA03 — Ross, bearing only |
| 10:38:28 | HA11 — Ross located |
| 11:25:34 | HA02 confirms Ross |
| 11:29:33 | HA09 — a third, unplaceable |
| 11:55:18 | HA03 — a bearing |
| 12:04:33 | HA10 — the Weddell |
| 12:10:18 | HA03 again |
| ~12:15 | lunch; the call |

This fixes the lunch problem on its own. At 198.1 m/s his last morning event is 10:37 EDT and "Let's have lunch" reads as an absurdly early lunch that then has to stretch to a 13:20 desk return. At 110 the morning fills and lunch falls where lunch falls.

It also changes the shape of S2's opening. He no longer arrives to two events; he arrives to one, and the second lands an hour after he sits down. He watches the day escalate instead of being handed it already escalated.

## Cost: S2 gets re-numbered

Every Edgar timestamp in S2 moves except the Prydz block and the Amundsen bearing.

| S2 currently | At 110 m/s |
|---|---|
| HA03 Juan Fernández 13:00Z | 14:01Z |
| Wake HA11 13:37Z | 14:38Z |
| Origin Ross 11:35Z | 12:36Z |
| HA09 Tristan da Cunha 14:01Z | 15:30Z |
| HA10 Ascension 14:36Z | 16:05Z |
| Origin Weddell 13:09Z | 14:37Z |

Prose consequences in S2: "just after ten, beepers started going off" now fits the Ross detection at 10:01 rather than the Weddell; "nine forty, not bad Edgar took three minutes" becomes ten forty; "two events, six hours apart" needs restructuring anyway and now becomes a single event waiting for him with the second arriving live; "Let's have lunch" moves to roughly 12:15.

S3's targets also shift from those in `S3-xlsx-conflicts.md`. The defects listed there are all still defects — they were keyed to the superseded 09:40Z Weddell — but the replacement numbers become the ones in this note.

## Where 116 m/s goes wrong

Pushing the speed up to get the Weddell located before 06:00 Hilo is a false economy. At 116 the Weddell locates at 15:54:22Z and the Amundsen bearing arrives at 15:55:18Z — 56 seconds apart. Two unrelated notices landing in the same minute reads as contrivance. At 110 they sit 9 minutes apart in the more useful order, bearing first and resolution second.
