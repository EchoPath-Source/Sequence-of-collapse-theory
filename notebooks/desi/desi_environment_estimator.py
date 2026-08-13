#!/usr/bin/env python3
"""Deterministic DESI environment-estimator prototype.

This module implements the analysis stages that do not require a live DESI
connection: redshift shelling, k-nearest-neighbor density on precomputed
Cartesian coordinates, within-shell percentile normalization, candidate
percentile-based environment labels, and basic quality flags.

Important: coordinate conversion is intentionally out of scope here. Production
DESI inputs must first be converted to x/y/z under a separately documented and
frozen coordinate/cosmology contract. This module must not be used to infer an
H0 environment effect directly.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import random
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Sequence

METHOD_VERSION = "desi-knn-shell-v0.1"


@dataclass(frozen=True)
class EnvironmentConfig:
    shell_width: float = 0.02
    min_shell_size: int = 20
    k_neighbors: int = 5
    void_max_pct: float = 10.0
    low_max_pct: float = 30.0
    sheet_max_pct: float = 70.0
    filament_max_pct: float = 90.0


@dataclass
class Point:
    targetid: str
    z: float
    x: float
    y: float
    z_cart: float
    healpix: str = ""
    redshift_shell: str = ""
    local_density: float = math.nan
    density_percentile: float = math.nan
    environment_bin: str = "unclassified"
    quality_flags: str = ""


def shell_index(z: float, shell_width: float) -> int:
    if not math.isfinite(z) or z < 0:
        raise ValueError(f"invalid redshift: {z}")
    if shell_width <= 0:
        raise ValueError("shell_width must be > 0")
    return int(math.floor(z / shell_width))


def assign_shells(points: Sequence[Point], config: EnvironmentConfig) -> None:
    for p in points:
        idx = shell_index(p.z, config.shell_width)
        lo = idx * config.shell_width
        hi = (idx + 1) * config.shell_width
        p.redshift_shell = f"{lo:.3f}-{hi:.3f}"


def euclidean_distance(a: Point, b: Point) -> float:
    return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2 + (a.z_cart - b.z_cart) ** 2)


def knn_density(points: Sequence[Point], k: int) -> List[float]:
    """Return kNN number density using a sphere enclosing the kth neighbor.

    Density = k / (4/3*pi*r_k^3). Coordinates therefore define the physical
    units. Production use requires documented comoving/proper coordinate units.
    """
    if k < 1:
        raise ValueError("k must be >= 1")
    if len(points) <= k:
        return [math.nan] * len(points)

    result: List[float] = []
    for i, p in enumerate(points):
        distances = [euclidean_distance(p, q) for j, q in enumerate(points) if j != i]
        distances.sort()
        rk = distances[k - 1]
        if rk <= 0 or not math.isfinite(rk):
            result.append(math.nan)
            continue
        volume = (4.0 / 3.0) * math.pi * rk ** 3
        result.append(k / volume)
    return result


def percentile_ranks(values: Sequence[float]) -> List[float]:
    """Deterministic midrank percentiles for finite values, 0..100."""
    finite = [(i, v) for i, v in enumerate(values) if math.isfinite(v)]
    out = [math.nan] * len(values)
    n = len(finite)
    if n == 0:
        return out
    if n == 1:
        out[finite[0][0]] = 50.0
        return out

    sorted_pairs = sorted(finite, key=lambda iv: (iv[1], iv[0]))
    pos = 0
    while pos < n:
        end = pos + 1
        value = sorted_pairs[pos][1]
        while end < n and sorted_pairs[end][1] == value:
            end += 1
        mean_rank = ((pos + 1) + end) / 2.0
        pct = 100.0 * (mean_rank - 1.0) / (n - 1.0)
        for j in range(pos, end):
            out[sorted_pairs[j][0]] = pct
        pos = end
    return out


def classify_percentile(pct: float, config: EnvironmentConfig) -> str:
    if not math.isfinite(pct):
        return "unclassified"
    if pct <= config.void_max_pct:
        return "void_like"
    if pct <= config.low_max_pct:
        return "low_density"
    if pct <= config.sheet_max_pct:
        return "sheet_like"
    if pct <= config.filament_max_pct:
        return "filament_like"
    return "cluster_like"


def estimate_environment(points: Sequence[Point], config: EnvironmentConfig) -> None:
    """Estimate density and labels independently within redshift shells."""
    assign_shells(points, config)
    by_shell: dict[str, List[Point]] = {}
    for p in points:
        by_shell.setdefault(p.redshift_shell, []).append(p)

    for shell, shell_points in sorted(by_shell.items()):
        flags = []
        if len(shell_points) < config.min_shell_size:
            flags.append("SMALL_SHELL")
        densities = knn_density(shell_points, config.k_neighbors)
        percentiles = percentile_ranks(densities)
        for p, density, pct in zip(shell_points, densities, percentiles):
            p.local_density = density
            p.density_percentile = pct
            p.environment_bin = classify_percentile(pct, config)
            p.quality_flags = ";".join(flags)
            if not math.isfinite(density):
                p.quality_flags = ";".join(filter(None, [p.quality_flags, "DENSITY_UNDEFINED"]))


def read_points(path: Path) -> List[Point]:
    required = {"targetid", "z", "x", "y", "z_cart"}
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        missing = required - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"missing required columns: {sorted(missing)}")
        rows = []
        for r in reader:
            rows.append(
                Point(
                    targetid=str(r["targetid"]),
                    z=float(r["z"]),
                    x=float(r["x"]),
                    y=float(r["y"]),
                    z_cart=float(r["z_cart"]),
                    healpix=str(r.get("healpix", "")),
                )
            )
    return rows


def write_points(path: Path, points: Sequence[Point]) -> None:
    fields = [
        "targetid", "z", "x", "y", "z_cart", "healpix", "redshift_shell",
        "local_density", "density_percentile", "environment_bin",
        "environment_method", "quality_flags",
    ]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for p in points:
            writer.writerow(
                {
                    "targetid": p.targetid,
                    "z": p.z,
                    "x": p.x,
                    "y": p.y,
                    "z_cart": p.z_cart,
                    "healpix": p.healpix,
                    "redshift_shell": p.redshift_shell,
                    "local_density": p.local_density,
                    "density_percentile": p.density_percentile,
                    "environment_bin": p.environment_bin,
                    "environment_method": METHOD_VERSION,
                    "quality_flags": p.quality_flags,
                }
            )


def synthetic_points(seed: int = 7) -> List[Point]:
    """Create deterministic dense + sparse synthetic regions for smoke testing."""
    rng = random.Random(seed)
    pts: List[Point] = []
    for i in range(60):
        pts.append(Point(str(i), 0.101 + rng.uniform(-0.004, 0.004), rng.gauss(0, 0.25), rng.gauss(0, 0.25), rng.gauss(0, 0.25)))
    for i in range(60, 100):
        pts.append(Point(str(i), 0.105 + rng.uniform(-0.004, 0.004), rng.uniform(3, 10), rng.uniform(3, 10), rng.uniform(3, 10)))
    return pts


def self_test() -> dict:
    config = EnvironmentConfig(shell_width=0.02, min_shell_size=20, k_neighbors=5)
    pts = synthetic_points()
    estimate_environment(pts, config)
    finite = [p for p in pts if math.isfinite(p.local_density)]
    if len(finite) != len(pts):
        raise AssertionError("synthetic test produced undefined density")
    dense_median = sorted(p.local_density for p in pts[:60])[30]
    sparse_median = sorted(p.local_density for p in pts[60:])[20]
    if not dense_median > sparse_median:
        raise AssertionError("dense synthetic cloud did not receive higher kNN density")
    bins: dict[str, int] = {}
    for p in pts:
        bins[p.environment_bin] = bins.get(p.environment_bin, 0) + 1
    return {
        "status": "PASS",
        "method": METHOD_VERSION,
        "n": len(pts),
        "dense_median_density": dense_median,
        "sparse_median_density": sparse_median,
        "environment_bin_counts": bins,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, help="CSV with targetid,z,x,y,z_cart[,healpix]")
    parser.add_argument("--output", type=Path, help="Output CSV")
    parser.add_argument("--k", type=int, default=5)
    parser.add_argument("--shell-width", type=float, default=0.02)
    parser.add_argument("--min-shell-size", type=int, default=20)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test or args.input is None:
        print(json.dumps(self_test(), indent=2, sort_keys=True))
        return 0

    if args.output is None:
        parser.error("--output is required with --input")

    config = EnvironmentConfig(
        shell_width=args.shell_width,
        min_shell_size=args.min_shell_size,
        k_neighbors=args.k,
    )
    points = read_points(args.input)
    estimate_environment(points, config)
    write_points(args.output, points)
    print(json.dumps({"status": "PASS", "rows": len(points), "method": METHOD_VERSION}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
