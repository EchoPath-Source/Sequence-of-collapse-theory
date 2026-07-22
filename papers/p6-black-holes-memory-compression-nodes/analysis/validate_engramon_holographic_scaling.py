#!/usr/bin/env python3
"""
Validate the candidate Engramon / neutrino holographic-scaling reconciliation.

Status
------
CANDIDATE / DIMENSIONAL-AUDIT SUPPORT ONLY.

This script checks whether a target carrier energy near the neutrino scale can be
mapped to the same effective boundary wavelength from two candidate parent-mass
regimes using the generalized scaling relation

    L_E = l_Pl * (M_parent / M_Pl) ** alpha

It is intentionally conservative. Passing this script does not prove SoCT,
Engramons, memory gravity, neutrino coupling, or a parent-universe mechanism.
It only verifies arithmetic consistency for the stated assumptions.

Default assumptions
-------------------
- Target carrier energy: E_E = 0.034 eV
- Reduced Compton relation: L_E = hbar*c / E_E
- Seed parent scale: 10^5 solar masses
- Cluster parent scale: 10^14 solar masses

The script also prints the exact 10^9 mass-ratio gap between these two scales.
That numerical match to the GeV/eV conversion factor is treated as an audit clue,
not proof of a unit-conversion error.
"""

from __future__ import annotations

import argparse
import csv
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


# CODATA-like constants, sufficient for repo-level dimensional validation.
PLANCK_LENGTH_M = 1.616255e-35
PLANCK_MASS_KG = 2.176434e-8
SOLAR_MASS_KG = 1.98847e30
HBAR_C_EV_M = 1.973269804e-7  # hbar*c in eV*m
GEV_TO_EV = 1.0e9


@dataclass(frozen=True)
class ParentScale:
    """A named parent-mass scale in solar masses."""

    name: str
    mass_solar: float

    @property
    def mass_kg(self) -> float:
        return self.mass_solar * SOLAR_MASS_KG

    @property
    def mass_planck_units(self) -> float:
        return self.mass_kg / PLANCK_MASS_KG


def target_length_from_energy_ev(energy_ev: float) -> float:
    """Return reduced Compton wavelength L = hbar*c/E in meters."""

    if energy_ev <= 0:
        raise ValueError("energy_ev must be positive")
    return HBAR_C_EV_M / energy_ev


def alpha_for_target_length(parent: ParentScale, target_length_m: float) -> float:
    """Solve alpha = ln(L/l_Pl) / ln(M/M_Pl)."""

    if target_length_m <= 0:
        raise ValueError("target_length_m must be positive")
    base = parent.mass_planck_units
    if base <= 1:
        raise ValueError("parent mass must be larger than Planck mass")
    return math.log(target_length_m / PLANCK_LENGTH_M) / math.log(base)


def length_from_alpha(parent: ParentScale, alpha: float) -> float:
    """Evaluate L = l_Pl * (M/M_Pl)^alpha."""

    return PLANCK_LENGTH_M * (parent.mass_planck_units**alpha)


def energy_from_length_m(length_m: float) -> float:
    """Return E = hbar*c/L in eV."""

    if length_m <= 0:
        raise ValueError("length_m must be positive")
    return HBAR_C_EV_M / length_m


def rows_for_scales(scales: Iterable[ParentScale], energy_ev: float) -> list[dict[str, float | str]]:
    target_length_m = target_length_from_energy_ev(energy_ev)
    rows: list[dict[str, float | str]] = []
    for scale in scales:
        alpha = alpha_for_target_length(scale, target_length_m)
        reconstructed_length_m = length_from_alpha(scale, alpha)
        reconstructed_energy_ev = energy_from_length_m(reconstructed_length_m)
        rows.append(
            {
                "scale": scale.name,
                "mass_solar": scale.mass_solar,
                "mass_kg": scale.mass_kg,
                "mass_planck_units": scale.mass_planck_units,
                "target_energy_ev": energy_ev,
                "target_length_m": target_length_m,
                "alpha": alpha,
                "reconstructed_length_m": reconstructed_length_m,
                "reconstructed_energy_ev": reconstructed_energy_ev,
                "relative_length_error": abs(reconstructed_length_m - target_length_m)
                / target_length_m,
            }
        )
    return rows


def write_csv(path: Path, rows: list[dict[str, float | str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys())
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def format_float(value: float) -> str:
    """Compact scientific formatter for terminal output."""

    return f"{value:.12g}"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate candidate Engramon/neutrino holographic scaling arithmetic."
    )
    parser.add_argument(
        "--energy-ev",
        type=float,
        default=0.034,
        help="Target carrier energy in eV. Default: 0.034",
    )
    parser.add_argument(
        "--seed-mass-solar",
        type=float,
        default=1.0e5,
        help="Seed-scale parent mass in solar masses. Default: 1e5",
    )
    parser.add_argument(
        "--cluster-mass-solar",
        type=float,
        default=1.0e14,
        help="Cluster-scale parent mass in solar masses. Default: 1e14",
    )
    parser.add_argument(
        "--csv-out",
        type=Path,
        default=None,
        help="Optional CSV output path for reproducibility records.",
    )
    args = parser.parse_args()

    scales = [
        ParentScale("seed_scale", args.seed_mass_solar),
        ParentScale("cluster_scale", args.cluster_mass_solar),
    ]

    rows = rows_for_scales(scales, args.energy_ev)
    mass_ratio = args.cluster_mass_solar / args.seed_mass_solar

    print("Engramon / neutrino holographic scaling validation")
    print("Status: CANDIDATE arithmetic check, not physical proof")
    print()
    print(f"target_energy_ev: {format_float(args.energy_ev)}")
    print(f"target_length_m:  {format_float(rows[0]['target_length_m'])}")
    print()
    for row in rows:
        print(row["scale"])
        print(f"  mass_solar:               {format_float(float(row['mass_solar']))}")
        print(f"  mass_planck_units:        {format_float(float(row['mass_planck_units']))}")
        print(f"  alpha:                    {format_float(float(row['alpha']))}")
        print(f"  reconstructed_length_m:   {format_float(float(row['reconstructed_length_m']))}")
        print(f"  reconstructed_energy_ev:  {format_float(float(row['reconstructed_energy_ev']))}")
        print(f"  relative_length_error:    {format_float(float(row['relative_length_error']))}")
        print()

    print(f"cluster/seed mass ratio: {format_float(mass_ratio)}")
    print(f"GeV/eV conversion factor: {format_float(GEV_TO_EV)}")
    if math.isclose(mass_ratio, GEV_TO_EV, rel_tol=1e-12):
        print("audit_note: mass-ratio gap matches GeV/eV numerically; treat as clue, not proof.")
    else:
        print("audit_note: mass-ratio gap does not exactly match GeV/eV for these inputs.")

    if args.csv_out is not None:
        write_csv(args.csv_out, rows)
        print(f"csv_written: {args.csv_out}")


if __name__ == "__main__":
    main()
