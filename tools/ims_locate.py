#!/usr/bin/env python3
"""
ims_locate.py — when is each event DETECTABLE, and when is it LOCATABLE?

Reads the CSV written by ims_paths.py and builds, per event, the ordered list
of arrivals at stations whose path is CLEAR or MARGINAL, then marks the first
instant at which a location is obtainable at all.

THE DISTINCTION THAT DRIVES EVERYTHING
The IMS hydroacoustic network is two different instruments.

  * 6 HYDROPHONE stations (HA01/03/04/08/10/11) are triads of hydrophones
    moored at the sound-channel axis. Cross-correlating across the three
    elements yields a BACK-AZIMUTH, ~1-2 deg. One of these gives you a
    direction and no range.

  * 5 T-PHASE stations (HA02/05/06/07/09) are seismometers on islands. The
    acoustic wave converts to a seismic wave on the island flank, so the
    apparent arrival direction is set by where the conversion happened, not
    by where the source is. Treat these as ARRIVAL TIME ONLY.

So the rules are:
    1 hydrophone                  -> a ray. No location.
    1 hydrophone + 1 T-station    -> ray x hyperbola. Located.
    2 hydrophones                 -> two bearings crossing, plus a hyperbola.
                                     Located, quality set by crossing angle.
    3 stations of any kind        -> multilateration. Located, and the origin
                                     TIME falls out without assuming anything.
    2 T-stations, no hydrophone   -> one hyperbola. Not located.

Bearing-only error model: a station at range R with azimuth error sigma gives
a cross-range strip of width R*sigma. Two strips crossing at angle theta give
semi-axes ~ R*sigma/sin(theta). Timing adds a hyperbola that collapses the
along-strip direction, so the figures below are an upper bound on the error
once ranges are also used.

Usage:  python3 ims_locate.py /tmp/ims1000.csv
"""

import csv
import math
import sys

HYDROPHONE = {"HA01", "HA03", "HA04", "HA08", "HA10", "HA11"}

# duplicated from ims_paths.py so the crossing angle can be recomputed here
STN = {"HA01": (-34.9, 114.1), "HA02": (53.3, -132.5), "HA03": (-33.7, -78.8),
       "HA04": (-46.2, 52.6), "HA05": (16.3, -61.1), "HA06": (18.7, -110.9),
       "HA07": (39.4, -31.2), "HA08": (-7.3, 72.4), "HA09": (-37.1, -12.3),
       "HA10": (-8.0, -14.4), "HA11": (19.3, -166.6)}
RADIATOR = {"Prydz": (-65.5, 73.0), "Weddell": (-68.0, -38.0),
            "Amundsen": (-71.5, -108.0), "Ross": (-71.5, -178.0)}


def azimuth(lat1, lon1, lat2, lon2):
    p1, l1, p2, l2 = map(math.radians, (lat1, lon1, lat2, lon2))
    y = math.sin(l2 - l1) * math.cos(p2)
    x = math.cos(p1) * math.sin(p2) - math.sin(p1) * math.cos(p2) * math.cos(l2 - l1)
    return (math.degrees(math.atan2(y, x)) + 360.0) % 360.0


SIGMA_AZ_DEG = 1.5          # per-station back-azimuth uncertainty
ORIGINS = {                 # UTC minutes past midnight, Day 0
    "Prydz":    3 * 60 + 20,
    "Weddell":  10 * 60 + 5,
    "Amundsen": 14 * 60 + 50,
    "Ross":     None,       # free — the manuscript fixes no origin time
}
ROSS_ASSUMED = 15 * 60 + 50


def hhmm(minutes):
    m = int(round(minutes)) % (24 * 60)
    day = int(minutes) // (24 * 60)
    return f"{m//60:02d}:{m%60:02d}Z" + ("+1" if day else "")


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "/tmp/ims1000.csv"
    rows = list(csv.DictReader(open(path)))

    for src in ["Prydz", "Weddell", "Amundsen", "Ross"]:
        sel = [r for r in rows if r["source"] == src
               and r["grade"] in ("CLEAR", "MARGINAL")]
        sel.sort(key=lambda r: float(r["total_min"]))

        origin = ORIGINS[src]
        assumed = origin is None
        if assumed:
            origin = ROSS_ASSUMED

        print(f"\n## {src}   origin {hhmm(origin)}"
              + ("  (assumed — no origin time is fixed anywhere)" if assumed else ""))
        print(f"{'#':2s} {'stn':5s}{'kind':11s}{'range':>8s}{'t+':>8s}"
              f"{'arrives':>10s}{'baz':>7s}  {'grade':9s} what you have")

        n_h = n_any = 0
        located_at = None
        for i, r in enumerate(sel, 1):
            is_h = r["station"] in HYDROPHONE
            n_any += 1
            n_h += 1 if is_h else 0
            t = float(r["total_min"])

            if n_any == 1:
                have = "bearing only — a ray" if is_h else "one arrival time — nothing"
            elif located_at is None and (n_h >= 1 and n_any >= 2):
                have = ("two bearings + dT" if n_h >= 2
                        else "ray x hyperbola")
                located_at = origin + t
            elif located_at is None and n_any >= 3:
                have = "multilateration on times alone"
                located_at = origin + t
            elif located_at is None:
                have = f"{n_any} times, no bearing — one hyperbola, not located"
            else:
                have = "confirms; tightens" + (" ; origin time solved"
                                               if n_any == 3 else "")

            print(f"{i:2d} {r['station']:5s}"
                  f"{'hydrophone' if is_h else 'T-phase':11s}"
                  f"{int(r['total_km']):7d}k{t:7.1f}m"
                  f"{hhmm(origin + t):>10s}"
                  f"{(r['baz_deg'] if is_h else '—'):>7s}  "
                  f"{r['grade']:9s} {have}")

        if located_at is None:
            print("   NOT LOCATABLE from hydroacoustics on this geometry.")
        else:
            print(f"   DETECTABLE {hhmm(origin + float(sel[0]['total_min']))}"
                  f"   ·   LOCATABLE {hhmm(located_at)}"
                  f"   ·   blind interval "
                  f"{located_at - origin - float(sel[0]['total_min']):.0f} min")

        # crossing angle and error ellipse for the first two hydrophones
        hyd = [r for r in sel if r["station"] in HYDROPHONE][:2]
        if len(hyd) == 2:
            a, b = hyd
            rl, ro = RADIATOR[src]
            az_a = azimuth(rl, ro, *STN[a["station"]])
            az_b = azimuth(rl, ro, *STN[b["station"]])
            th = abs(az_a - az_b) % 360.0
            th = min(th, 360.0 - th)
            s = math.radians(SIGMA_AZ_DEG)
            st = max(math.sin(math.radians(th)), 1e-6)
            ea = float(a["deep_km"]) * s / st
            eb = float(b["deep_km"]) * s / st
            print(f"   bearings cross at {th:.0f}° "
                  f"({a['station']} x {b['station']}); at ±{SIGMA_AZ_DEG}° that is "
                  f"a {max(ea, eb):.0f} km × {min(ea, eb):.0f} km ellipse "
                  f"before ranges are used")


if __name__ == "__main__":
    main()
