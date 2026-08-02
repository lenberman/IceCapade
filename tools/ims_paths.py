#!/usr/bin/env python3
"""
ims_paths.py — IMS hydroacoustic path screen for the four Antarctic sources.

WHAT IT COMPUTES
For every IMS hydroacoustic station and every ice-shelf-front source:
range, SOFAR transit time, back-azimuth, and whether the deep-water part of
the path is obstructed by bathymetry shallower than a threshold.

SOURCE GEOMETRY — the part that matters
An ice-shelf front is not a far-field acoustic point source. It radiates into
its own embayment; the energy crosses the continental shelf and couples into
the deep sound channel at the shelf break. So each source is modelled in two
legs:

    front  --(shelf leg, slow, lossy)-->  radiator  --(SOFAR)-->  station

The radiator is a deep-water point just seaward of the shelf break, in the
embayment's natural exit corridor. Using the front itself as the far-field
source is what makes great circles run along the Antarctic coast for
thousands of kilometres and score as blocked when the real path simply
leaves the embayment first.

BATHYMETRY
Natural Earth 10m depth-contour polygons (ne_10m_bathymetry_*). A sample is
"deeper than D" if it falls inside the polygon set for D. Barriers are graded
against the 200 m and 2000 m contours so a sill is distinguished from an island.

GRADING
    CLEAR     nothing shallower than the threshold on the deep leg
    MARGINAL  longest barrier < --marginal km. A ridge crest or seamount:
              expect transmission loss and some delay, not extinction.
    BLOCKED   anything longer. Range and transit are then a LOWER BOUND —
              the real path goes round, and this screen does not route it.

WHAT THIS IS NOT
A geometric screen, not a propagation model. It finds hard barriers. It does
not model refraction over a sill, diffraction round a ridge end, upslope
conversion at a receiving island, sea-ice scattering loss, or the poleward
shoaling of the sound-channel axis. Read MARGINAL as "ask an acoustician".

Usage:
    python3 ims_paths.py
    python3 ims_paths.py --threshold 2000 --csv sens2000.csv
"""

import argparse
import csv
import math
import os
import sys

import shapefile
from shapely.geometry import Point, shape
from shapely.ops import unary_union
from shapely.prepared import prep

NE_DIR = os.environ.get("NE_BATHY_DIR", "/tmp/ne/10m_physical/ne_10m_bathymetry_all")
LEVELS = {200: "K_200", 1000: "J_1000", 2000: "I_2000", 3000: "H_3000",
          4000: "G_4000", 5000: "F_5000"}

# CTBT IMS hydroacoustic network: 6 hydrophone (H), 5 T-phase (T).
STATIONS = [
    ("HA01", "Cape Leeuwin, Australia",     -34.9,  114.1, "H"),
    ("HA02", "Queen Charlotte Is., Canada",  53.3, -132.5, "T"),
    ("HA03", "Juan Fernandez, Chile",       -33.7,  -78.8, "H"),
    ("HA04", "Crozet, France",              -46.2,   52.6, "H"),
    ("HA05", "Guadeloupe, France",           16.3,  -61.1, "T"),
    ("HA06", "Socorro Is., Mexico",          18.7, -110.9, "T"),
    ("HA07", "Flores, Azores, Portugal",     39.4,  -31.2, "T"),
    ("HA08", "Diego Garcia, BIOT (UK)",      -7.3,   72.4, "H"),
    ("HA09", "Tristan da Cunha, UK",        -37.1,  -12.3, "T"),
    ("HA10", "Ascension Is., UK",            -8.0,  -14.4, "H"),
    ("HA11", "Wake Is., USA",                19.3, -166.6, "H"),
]

# code, label, front lat/lon, radiator lat/lon (deep water seaward of the
# shelf break, in the embayment's exit corridor)
SOURCES = [
    ("Prydz",    "Amery front / Prydz Bay",     -68.5,   72.0, -65.5,   73.0),
    ("Weddell",  "Ronne-Filchner front",        -75.0,  -50.0, -68.0,  -38.0),
    ("Amundsen", "Thwaites / Pine I. front",    -74.8, -105.0, -71.5, -108.0),
    ("Ross",     "Ross Ice Shelf front",        -78.0, -175.0, -71.5, -178.0),
]

R_EARTH_KM = 6371.0


def to_vec(lat, lon):
    la, lo = math.radians(lat), math.radians(lon)
    return (math.cos(la) * math.cos(lo), math.cos(la) * math.sin(lo), math.sin(la))


def to_ll(v):
    x, y, z = v
    return (math.degrees(math.asin(max(-1.0, min(1.0, z)))),
            math.degrees(math.atan2(y, x)))


def gc_km(lat1, lon1, lat2, lon2):
    p1, l1, p2, l2 = map(math.radians, (lat1, lon1, lat2, lon2))
    d = math.acos(max(-1.0, min(1.0,
        math.sin(p1) * math.sin(p2) + math.cos(p1) * math.cos(p2) * math.cos(l2 - l1))))
    return d * R_EARTH_KM


def azimuth(lat1, lon1, lat2, lon2):
    p1, l1, p2, l2 = map(math.radians, (lat1, lon1, lat2, lon2))
    y = math.sin(l2 - l1) * math.cos(p2)
    x = math.cos(p1) * math.sin(p2) - math.sin(p1) * math.cos(p2) * math.cos(l2 - l1)
    return (math.degrees(math.atan2(y, x)) + 360.0) % 360.0


def gc_samples(lat1, lon1, lat2, lon2, step_km):
    total = gc_km(lat1, lon1, lat2, lon2)
    n = max(2, int(total / step_km) + 1)
    v1, v2 = to_vec(lat1, lon1), to_vec(lat2, lon2)
    ang = math.acos(max(-1.0, min(1.0, sum(a * b for a, b in zip(v1, v2)))))
    out = []
    for i in range(n + 1):
        f = i / n
        if ang < 1e-12:
            v = v1
        else:
            s1 = math.sin((1 - f) * ang) / math.sin(ang)
            s2 = math.sin(f * ang) / math.sin(ang)
            v = tuple(s1 * a + s2 * b for a, b in zip(v1, v2))
        nrm = math.sqrt(sum(c * c for c in v))
        la, lo = to_ll(tuple(c / nrm for c in v))
        out.append((f * total, la, lo))
    return out, total


def load_level(depth):
    name = LEVELS.get(depth)
    if name is None:
        sys.exit(f"no Natural Earth level for {depth} m; have {sorted(LEVELS)}")
    path = os.path.join(NE_DIR, f"ne_10m_bathymetry_{name}.shp")
    if not os.path.exists(path):
        sys.exit(f"missing {path} — set NE_BATHY_DIR")
    sf = shapefile.Reader(path)
    return prep(unary_union([shape(s.__geo_interface__) for s in sf.shapes()]))


def band(lon, lat, d200, d1000, d2000):
    p = Point(lon, lat)
    if not d200.contains(p):
        return "<200m"
    if not d1000.contains(p):
        return "200-1000m"
    if not d2000.contains(p):
        return "1000-2000m"
    return ">2000m"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--threshold", type=int, default=1000)
    ap.add_argument("--c-deep", type=float, default=1485.0, help="SOFAR group speed m/s")
    ap.add_argument("--c-shelf", type=float, default=1450.0, help="shelf leg speed m/s")
    ap.add_argument("--step", type=float, default=10.0)
    ap.add_argument("--rx-exclude", type=float, default=100.0)
    ap.add_argument("--marginal", type=float, default=150.0)
    ap.add_argument("--csv", default=None)
    args = ap.parse_args()

    deep = load_level(args.threshold)
    d200, d1000, d2000 = load_level(200), load_level(1000), load_level(2000)

    rows = []
    for scode, slabel, flat, flon, rlat0, rlon0 in SOURCES:
        shelf_km = gc_km(flat, flon, rlat0, rlon0)
        shelf_min = shelf_km * 1000.0 / args.c_shelf / 60.0
        for code, name, rlat, rlon, typ in STATIONS:
            pts, deep_km = gc_samples(rlat0, rlon0, rlat, rlon, args.step)

            shallow = [(d, la, lo) for d, la, lo in pts
                       if d > args.step and d <= deep_km - args.rx_exclude
                       and not deep.contains(Point(lo, la))]

            barriers = []
            for d, la, lo in shallow:
                if barriers and d - barriers[-1]["end"] <= args.step * 1.5:
                    barriers[-1]["end"] = d
                else:
                    barriers.append({"start": d, "end": d, "lat": la, "lon": lo})
            for b in barriers:
                b["len"] = b["end"] - b["start"] + args.step
                b["band"] = band(b["lon"], b["lat"], d200, d1000, d2000)

            longest = max((b["len"] for b in barriers), default=0.0)
            grade = ("CLEAR" if not barriers
                     else "MARGINAL" if longest < args.marginal else "BLOCKED")

            deep_min = deep_km * 1000.0 / args.c_deep / 60.0
            rows.append({
                "source": scode, "station": code, "type": typ, "name": name,
                "shelf_km": round(shelf_km), "shelf_min": round(shelf_min, 1),
                "deep_km": round(deep_km), "deep_min": round(deep_min, 1),
                "total_km": round(shelf_km + deep_km),
                "total_min": round(shelf_min + deep_min, 1),
                "baz_deg": round(azimuth(rlat, rlon, rlat0, rlon0), 1),
                "grade": grade,
                "blocked_km": round(sum(b["len"] for b in barriers)),
                "longest_km": round(longest),
                "worst": "; ".join(
                    f"{round(b['start'])}-{round(b['end'])}km "
                    f"{b['lat']:.1f},{b['lon']:.1f} {b['band']}"
                    for b in sorted(barriers, key=lambda x: -x["len"])[:3]),
            })

    hdr = (f"IMS path screen — threshold {args.threshold} m, c_deep {args.c_deep:.0f}, "
           f"c_shelf {args.c_shelf:.0f} m/s, step {args.step:.0f} km, "
           f"marginal < {args.marginal:.0f} km")
    print(hdr + "\n" + "=" * len(hdr))
    for scode, slabel, flat, flon, rlat0, rlon0 in SOURCES:
        sh = next(r for r in rows if r["source"] == scode)
        print(f"\n## {scode} — {slabel}")
        print(f"   front {flat:.1f},{flon:.1f} -> radiator {rlat0:.1f},{rlon0:.1f}"
              f"  (shelf leg {sh['shelf_km']} km, {sh['shelf_min']:.1f} min)")
        print(f"{'stn':5s}{'ty':3s}{'deep':>8s}{'TOTAL':>8s}{'t_tot':>8s}{'baz':>7s}"
              f"  {'grade':9s}{'blk':>6s}  worst barriers")
        for r in sorted([x for x in rows if x["source"] == scode],
                        key=lambda x: x["total_min"]):
            print(f"{r['station']:5s}{r['type']:3s}{r['deep_km']:7d}k"
                  f"{r['total_km']:7d}k{r['total_min']:7.1f}m{r['baz_deg']:7.1f}"
                  f"  {r['grade']:9s}{r['blocked_km']:5d}k  {r['worst']}")

    if args.csv:
        with open(args.csv, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)
        print(f"\nwrote {args.csv}")


if __name__ == "__main__":
    main()
