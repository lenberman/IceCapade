# DayOne.1 — The IMS, and how a sound in the Southern Ocean reaches an American desk

Reference note. Everything here is real and current unless flagged.

---

## 1. What the IMS is

The **International Monitoring System** is a global sensor network built to verify the Comprehensive Nuclear-Test-Ban Treaty. It is run by the **CTBTO** — the Preparatory Commission for the Comprehensive Nuclear-Test-Ban Treaty Organization — headquartered in Vienna. When complete it comprises 337 facilities.

Four technologies, each matched to a place a bomb could be hidden:

| Technology | Stations | Listens for |
|---|---|---|
| Seismic | 50 primary + 120 auxiliary | Underground |
| **Hydroacoustic** | **11** | **Underwater** |
| Infrasound | 60 | Atmosphere |
| Radionuclide | 80 + 16 labs | The debris afterwards |

The first three find and locate an event. The fourth is the one that proves it was nuclear.

**The relevant asymmetry for your book:** the IMS is the only continuously-operating sensor network on Earth with global coverage and a *single* data centre. Everything else is national or regional. That is the entire reason one analyst can put four pins in a map on Day 0 when nobody else can.

---

## 2. Why only eleven hydroacoustic stations

Because the ocean is an almost perfect sound pipe, and the pipe has a name.

**The SOFAR channel** (SOund Fixing And Ranging), also called the deep sound channel. Sound speed in seawater rises with temperature and rises with pressure. Near the surface, temperature dominates — warm water, fast sound. Going down, temperature falls and so does sound speed. Below the thermocline temperature levels off and pressure takes over, so sound speed climbs again. Between the two regimes sits a **minimum**, typically around 750–1,000 m, shallower toward the poles.

Sound entering that minimum is trapped. Rays that stray upward bend back down; rays that stray downward bend back up. The energy never touches the seabed and never touches the surface, so it never scatters. A signal in the SOFAR channel crosses an ocean basin with almost no loss.

Eleven stations therefore cover every ocean on Earth. Two kinds:

**Six hydrophone stations.** Actual underwater microphones, suspended from subsurface floats at 600–1,200 m, anchored to the seafloor, cabled to shore — cables that can exceed 100 km and cross water 5,000 m deep. Band 1–100 Hz. Sensitive, directional, expensive, and hard to maintain. Most sites use *two* triplets on opposite sides of the island, because a single set would sit in the island's own acoustic shadow for sources on the far side.

> HA01 Cape Leeuwin (Australia) · HA03 Juan Fernández (Chile) · HA04 Crozet (France) · HA08 Diego Garcia (UK) · HA10 Ascension (UK) · HA11 Wake Island (US)

**Five T-phase stations.** Seismometers on steep-sided oceanic islands. A "T-phase" is acoustic energy in the water that converts to seismic energy when it strikes a shoreline or the seabed. Cheaper, simpler, less sensitive.

> Including HA06 Socorro (Mexico) and HA07 Tristan da Cunha (UK)

**Useful for plot:** since 2014, data from stations on Australian, UK and US territory — four of the six hydrophone arrays — has been **openly available**. A university scientist can pull HA01 Cape Leeuwin himself with a few lines of code. Your analyst has no monopoly.

---

## 3. Reading the bulletin line in Fragment #1

> *0412Z. Broadband arrival, 11→4 Hz over 340 s. Back-azimuth 189°. Origin Prydz Bay, ~0320Z.*

**0412Z** — Z is Zulu, i.e. UTC. Everything in this world is UTC and nobody converts.

**Broadband arrival** — energy across many frequencies at once, rather than a tone. Distinguishes a physical event from machinery or biology.

**11→4 Hz over 340 s** — the signal starts near 11 hertz and descends to 4 over about six minutes. Both are below human hearing. Six minutes is a *very* long signal; an explosion is a fraction of a second.

**Back-azimuth 189°** — the compass bearing the sound came *from*. A hydrophone triplet gets bearing from the tiny arrival-time differences between its three elements. One station gives you a line, not a point. Two stations crossed give a location.

**~0320Z** — computed backwards. Distance divided by sound speed in the channel, about 1,485 m/s. Cape Leeuwin to Prydz Bay is roughly 4,660 km, so 52 minutes.

**Is the ice signal realistic?** Entirely. Antarctic ice is a known and well-studied source in IMS hydroacoustic data. Icebergs grinding, colliding, scraping the seabed and calving generate long-duration low-frequency signals — the literature calls the sustained kind **harmonic tremor** — and they are routinely recorded thousands of kilometres away at Cape Leeuwin and Crozet. There is a small community of scientists whose work is exactly this. Your event is that signal with the amplitude turned up past anything on record.

---

## 4. The routing, step by step

**T+0** — Event. Acoustic energy enters the SOFAR channel.

**T+52 min** — Arrival at HA01. Digitized, GPS-timestamped, authenticated.

**T+53 min** — Transmitted over the **GCI** (Global Communications Infrastructure), a dedicated satellite/VSAT network linking 300-plus IMS facilities and 100-plus national centres to Vienna. Real time, 24/7. Notably, several of the links are Antarctic.

**T+55 min** — At the **IDC** in Vienna. Automatic detection algorithms run continuously — a short-term-average / long-term-average trigger flags the arrival and extracts its features: azimuth, frequency content, duration, amplitude.

**Then two paths diverge, and the difference is your plot.**

### Path A — the treaty path (slow, thorough, wrong mission)

Vienna produces a sequence of bulletins: automatic **Standard Event Lists** (SEL1 at about an hour, SEL2 and SEL3 over the following hours), then a human-reviewed **Reviewed Event Bulletin** roughly two days later.

These flow to **National Data Centres**. Every state signatory may operate one.

**The US National Data Centre is the Air Force Technical Applications Center (AFTAC), at Patrick Space Force Base, Florida.** AFTAC is the Defense Department's sole nuclear treaty monitoring centre. It also runs the US Atomic Energy Detection System, a national network of 3,600-plus sensors that is separate from and additional to the IMS. AFTAC reports findings to national command authorities.

So: an American *does* see this, within the hour, and sees all four events because the IMS is global. But AFTAC's mission is nuclear discrimination. Its entire professional competence is the rapid separation of natural phenomena from detonations — and this signal is unambiguously, correctly, natural. **The system works exactly as designed and files it.**

### Path B — the hazard path (fast, but seismically gated)

After the 2004 Indian Ocean tsunami, the CTBTO and UNESCO's Intergovernmental Oceanographic Commission agreed to share IMS data for tsunami warning. This is now formalized as **Tsunami Warning Agreements**; as of late 2025, 23 warning centres in 22 countries hold one, receiving data from around 110 IMS stations. The data is forwarded from Vienna automatically, within about a minute of arrival, and has delivered up to three minutes of lead time over other sources.

The two US recipients:

- **Pacific Tsunami Warning Center (PTWC)**, Ewa Beach, Hawaii — Pacific, Caribbean, and provider of service to the Indian Ocean
- **National Tsunami Warning Center (NTWC)**, Palmer, Alaska — US and Canadian continental coasts

**Here is the gap.** Both centres are built around a seismic trigger. The workflow starts with an earthquake location — normally from the **USGS National Earthquake Information Center** in Golden, Colorado — then evaluates magnitude, depth and mechanism for tsunamigenic potential, then models. Confirmation comes from **DART buoys** (Deep-ocean Assessment and Reporting of Tsunamis): a bottom pressure recorder on the seafloor that detects a few centimetres of sea level change through 4,000 m of water, paired with a surface buoy.

Your event produces **no earthquake**. There is no origin to evaluate, no magnitude, no focal mechanism. The DART buoys will eventually see something, but the first pulse genuinely disperses, so what they see supports the cancellation. Every automated gate fails open.

### Path C — the polar path

The **NSF Office of Polar Programs**, which runs the US Antarctic Program, loses communications with its stations. That is an operational emergency about people and infrastructure, handled by a different building on a different timescale, and initially framed as a comms failure rather than a geophysical event.

---

## 5. So where does Sandoval sit?

Four options, with what each buys and costs.

**AFTAC / US NDC, Patrick SFB.** She is the one person in the US government who sees all four detections on Day 0, because only the IMS is global. Her institutional mandate tells her it isn't hers. *Buys:* the map with four pins, justified. Maximum dramatic irony — right data, wrong desk. *Costs:* a military intelligence setting, and she needs a plausible reason to care about ice.

**PTWC, Ewa Beach.** A duty scientist whose system is designed for precisely this and cannot trigger on it. *Buys:* she is the correct person, professionally, and watches her own tooling refuse. *Costs:* she sees the Pacific well and the Indian Ocean by agreement; the four-basin picture arrives later.

**A research hydroacoustician — university, or one of the labs doing CTBT verification work.** Open data since 2014, and there are real scientists who spend careers listening to Antarctic ice on these instruments. She recognises the signal in minutes and has no authority whatsoever. *Buys:* fastest correct understanding, zero power, and a natural arc into government as the crisis pulls expertise in. *Costs:* she has to be brought inside for the later fragments.

**OSTP or an NSC directorate.** The integrator. *Buys:* the testimony fragment, effortlessly. *Costs:* no reason to be awake at 04:12Z on Day 0.

**My recommendation: three, then one.** Start her outside as the person who understands it first and is listened to least, then have the government reach for her in week two. That gives you the Day 0 fragments from someone technically fluent and institutionally powerless, the middle fragments from someone newly inside and appalled by the latency, and the testimony from someone senior enough to be in the chair. It also lets you keep the AFTAC beat as a *separate* document she reads later and finds unbearable, because it is correct.

---

## 6. Fragment #1, made legible

A version that carries its own explanation for a reader who has never heard of any of this.

> **CTBTO INTERNATIONAL DATA CENTRE — VIENNA**
> **Automatic detection notice — Hydroacoustic**
>
> **Station HA01, Cape Leeuwin, Western Australia.** Hydrophone triplet, 1,050 m depth, SOFAR channel.
>
> Arrival 0412:07Z. Broadband, 11 Hz descending to 4 Hz across 340 seconds. Amplitude exceeds every entry in this station's catalogue since installation. Back-azimuth 189°.
>
> Assuming channel sound speed 1,485 m/s, origin lies 4,660 km along that bearing, in Prydz Bay, at approximately 0320Z.
>
> Signal character is cryogenic — consistent with ice fracture and iceberg tremor, inconsistent with explosion. **Screened. No treaty relevance.**
>
> *Auto-forwarded: National Data Centres (all); tsunami warning centres holding a current TWA.*
>
> ---
>
> *[Handwritten across the printout, undated:*
> *"Screened means we looked at it. It doesn't mean anything else. — ES"]*

The phrase **"no treaty relevance"** is your whole first act in three words. The system was asked one question, answered it correctly, and had no mechanism for the question nobody asked.

---

## 7. Glossary

**CTBTO** — Vienna body running the IMS. Preparatory Commission, technically; the treaty is not yet in force.
**IMS** — International Monitoring System. 337 facilities, four technologies.
**IDC** — International Data Centre, Vienna. Where everything lands.
**GCI** — Global Communications Infrastructure. The satellite network carrying it there.
**NDC** — National Data Centre. One per participating state. **The US one is AFTAC.**
**AFTAC** — Air Force Technical Applications Center, Patrick SFB, Florida. DoD's nuclear treaty monitoring centre.
**USAEDS** — US Atomic Energy Detection System. AFTAC's own 3,600-sensor network, separate from the IMS.
**SOFAR channel** — the ocean's sound-speed minimum, ~750–1,000 m. Traps sound and carries it across basins.
**Hydrophone / T-phase station** — the two kinds of hydroacoustic station. Six and five.
**Back-azimuth** — bearing to the source.
**H phase / T phase** — CTBTO shorthand. H is in-water. T is converted seismic.
**SEL / REB** — automatic Standard Event Lists; human Reviewed Event Bulletin, ~2 days.
**TWA** — Tsunami Warning Agreement. The formal channel from Vienna to a warning centre.
**PTWC / NTWC** — Pacific Tsunami Warning Center, Hawaii; National Tsunami Warning Center, Alaska.
**NEIC** — USGS National Earthquake Information Center, Golden, Colorado.
**DART** — seafloor pressure recorder plus surface buoy. Detects the wave itself in deep water.
**Zulu / Z** — UTC.
