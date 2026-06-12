#!/usr/bin/env python3
"""
PNT void-filament H0 toy calculation.

Status: PRELIMINARY / toy-model calculation
Claim level: Simulation / phenomenological calculation only; not an empirical detection.

Purpose
-------
This script implements the explicit equations currently documented in:

    simulations/pnt_hubble_void/README.md
    simulations/pnt_hubble_void/pnt_hubble_void.jsx

It converts the existing JSX visualization into a reproducible Python calculation that
exports machine-readable CSV and JSON summaries.

Core equations
--------------
Failed-nucleation fraction:

    f_fail(delta) = 1 - f_succ_mean * max(0, 1 + delta)^n

with physical clipping:

    0 <= f_fail <= 1

Dark-energy ratio:

    rho_DE(delta) / rho_DE(mean) = f_fail(delta) / f_fail(0)

Local H0 estimate:

    H0(delta) = H0_CMB * sqrt[(Omega_m + Omega_DE * rho_DE_ratio(delta))
                              / (Omega_m + Omega_DE)]

Fiducial values are chosen to match the repo visualization:

    H0_CMB = 67.4 km/s/Mpc
    H0_local_obs = 73.0 km/s/Mpc
    Omega_m = 0.315
    Omega_DE = 0.685
    f_succ_mean = 0.15
    n = 1.5
    representative local delta = -0.35

Expected fiducial result:

    H0(delta=-0.35, n=1.5) ~= 69.312 km/s/Mpc
    Delta_H0 ~= +1.912 km/s/Mpc
    fraction of 5.6 km/s/Mpc Hubble tension ~= 34.1%

Run from repository root:

    python simulations/pnt_hubble_void/pnt_hubble_void_calculation.py

Outputs:

    simulations/pnt_hubble_void/outputs/pnt_void_h0_grid.csv
    simulations/pnt_hubble_void/outputs/pnt_void_h0_sensitivity.csv
    simulations/pnt_hubble_void/outputs/pnt_void_h0_summary.json

Notes
-----
This is a controlled reproduction of the current PNT toy model, not a claim that
void dark energy has been measured. A real empirical test still requires Pantheon+
environment labels, covariance-aware fitting, and preregistered controls.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class PNTParameters:
    """Parameter set for the PNT void-filament toy calculation."""

    H0_CMB: float = 67.4
    H0_local_obs: float = 73.0
    Omega_m: float = 0.315
    Omega_DE: float = 0.685
    f_succ_mean: float = 0.15
    n_fiducial: float = 1.5
    representative_delta: float = -0.35
    delta_min: float = -0.90
    delta_max: float = 0.50
    delta_step: float = 0.05

    def validate(self) -> None:
        if not (0.0 < self.H0_CMB):
            raise ValueError("H0_CMB must be positive")
        if not (0.0 < self.H0_local_obs):
            raise ValueError("H0_local_obs must be positive")
        if not (0.0 <= self.Omega_m <= 2.0):
            raise ValueError("Omega_m is outside a reasonable toy-model range")
        if not (0.0 <= self.Omega_DE <= 2.0):
            raise ValueError("Omega_DE is outside a reasonable toy-model range")
        if math.isclose(self.Omega_m + self.Omega_DE, 0.0):
            raise ValueError("Omega_m + Omega_DE must be nonzero")
        if not (0.0 <= self.f_succ_mean <= 1.0):
            raise ValueError("f_succ_mean must be in [0, 1]")
        if self.n_fiducial <= 0.0:
            raise ValueError("n_fiducial must be positive")
        if self.delta_step <= 0.0:
            raise ValueError("delta_step must be positive")
        if self.delta_min >= self.delta_max:
            raise ValueError("delta_min must be smaller than delta_max")


def clamp(value: float, lower: float = 0.0, upper: float = 1.0) -> float:
    """Clamp a value to a closed interval."""

    return max(lower, min(upper, value))


def f_fail(delta: float, params: PNTParameters, n: float | None = None) -> float:
    """Failed-nucleation fraction in the current power-law toy model."""

    exponent = params.n_fiducial if n is None else n
    raw = 1.0 - params.f_succ_mean * max(0.0, 1.0 + delta) ** exponent
    return clamp(raw, 0.0, 1.0)


def f_succ(delta: float, params: PNTParameters, n: float | None = None) -> float:
    """Successful-nucleation fraction implied by f_fail."""

    return 1.0 - f_fail(delta, params, n=n)


def rho_de_ratio(delta: float, params: PNTParameters, n: float | None = None) -> float:
    """Local dark-energy ratio relative to the cosmic-mean environment."""

    baseline = f_fail(0.0, params, n=n)
    if math.isclose(baseline, 0.0):
        # Degenerate edge case. Returning 1 keeps H0 finite and neutral.
        return 1.0
    return f_fail(delta, params, n=n) / baseline


def h0_pnt(delta: float, params: PNTParameters, n: float | None = None) -> float:
    """PNT local H0 estimate for an environment overdensity delta."""

    numerator = params.Omega_m + params.Omega_DE * rho_de_ratio(delta, params, n=n)
    denominator = params.Omega_m + params.Omega_DE
    if numerator < 0.0 or denominator <= 0.0:
        raise ValueError("Invalid density combination for square-root H0 calculation")
    return params.H0_CMB * math.sqrt(numerator / denominator)


def h0_matter_only_diagnostic(delta: float, params: PNTParameters) -> float:
    """Diagnostic matter-density-only curve with no PNT dark-energy differential.

    This is not a replacement for peculiar-velocity modeling or a real void cosmology.
    It is included only to provide a transparent comparison curve for the toy model.
    """

    local_matter_factor = max(0.0, 1.0 + delta)
    numerator = params.Omega_m * local_matter_factor + params.Omega_DE
    denominator = params.Omega_m + params.Omega_DE
    return params.H0_CMB * math.sqrt(numerator / denominator)


def tension_fraction(delta_h0: float, params: PNTParameters) -> float:
    """Fraction of observed local-CMB H0 difference explained by delta_h0."""

    observed_tension = params.H0_local_obs - params.H0_CMB
    if math.isclose(observed_tension, 0.0):
        return math.nan
    return 100.0 * delta_h0 / observed_tension


def delta_values(params: PNTParameters) -> list[float]:
    """Return rounded delta grid values inclusive of endpoints within tolerance."""

    values: list[float] = []
    i = 0
    current = params.delta_min
    while current <= params.delta_max + 1e-12:
        values.append(round(current, 10))
        i += 1
        current = params.delta_min + i * params.delta_step
    return values


def grid_rows(params: PNTParameters, n_values: Iterable[float]) -> list[dict[str, float]]:
    """Build main delta-grid rows for CSV export."""

    rows: list[dict[str, float]] = []
    for delta in delta_values(params):
        row: dict[str, float] = {
            "delta": delta,
            "f_fail_fiducial": f_fail(delta, params),
            "f_succ_fiducial": f_succ(delta, params),
            "rho_de_ratio_fiducial": rho_de_ratio(delta, params),
            "H0_pnt_fiducial": h0_pnt(delta, params),
            "delta_H0_fiducial": h0_pnt(delta, params) - params.H0_CMB,
            "tension_fraction_pct_fiducial": tension_fraction(h0_pnt(delta, params) - params.H0_CMB, params),
            "H0_matter_only_diagnostic": h0_matter_only_diagnostic(delta, params),
        }
        for n in n_values:
            key = str(n).replace(".", "p")
            h0 = h0_pnt(delta, params, n=n)
            row[f"rho_de_ratio_n_{key}"] = rho_de_ratio(delta, params, n=n)
            row[f"H0_pnt_n_{key}"] = h0
            row[f"tension_fraction_pct_n_{key}"] = tension_fraction(h0 - params.H0_CMB, params)
        rows.append(row)
    return rows


def sensitivity_rows(params: PNTParameters, deltas: Iterable[float], n_values: Iterable[float]) -> list[dict[str, float]]:
    """Build compact sensitivity rows matching the visualization intent."""

    rows: list[dict[str, float]] = []
    for delta in deltas:
        row: dict[str, float] = {"delta": float(delta)}
        for n in n_values:
            key = str(n).replace(".", "p")
            h0 = h0_pnt(delta, params, n=n)
            row[f"H0_n_{key}"] = h0
            row[f"delta_H0_n_{key}"] = h0 - params.H0_CMB
            row[f"tension_fraction_pct_n_{key}"] = tension_fraction(h0 - params.H0_CMB, params)
        rows.append(row)
    return rows


def fiducial_summary(params: PNTParameters) -> dict[str, object]:
    """Build a JSON-safe summary for the fiducial local-density case."""

    delta = params.representative_delta
    h0 = h0_pnt(delta, params)
    delta_h0 = h0 - params.H0_CMB
    observed_tension = params.H0_local_obs - params.H0_CMB
    return {
        "status": "PRELIMINARY / toy-model calculation",
        "claim_boundary": "This is a phenomenological PNT calculation, not an empirical detection.",
        "parameters": asdict(params),
        "fiducial_case": {
            "delta": delta,
            "n": params.n_fiducial,
            "f_fail": f_fail(delta, params),
            "f_succ": f_succ(delta, params),
            "rho_de_ratio": rho_de_ratio(delta, params),
            "H0_pnt": h0,
            "H0_CMB": params.H0_CMB,
            "H0_local_obs": params.H0_local_obs,
            "delta_H0": delta_h0,
            "observed_tension": observed_tension,
            "tension_fraction_pct": tension_fraction(delta_h0, params),
            "H0_matter_only_diagnostic": h0_matter_only_diagnostic(delta, params),
        },
        "required_before_empirical_claim": [
            "Pantheon+ environment_labels.csv with locked provenance",
            "covariance-aware void/filament H0 fitting",
            "redshift-matched bootstrap",
            "environment-label permutation test",
            "sky jackknife",
            "peculiar-velocity and survey-selection controls",
        ],
    }


def write_csv(path: Path, rows: list[dict[str, float]]) -> None:
    """Write CSV rows with stable column order."""

    if not rows:
        raise ValueError(f"No rows to write for {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys())
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, data: dict[str, object]) -> None:
    """Write JSON summary with deterministic formatting."""

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the PNT void-filament H0 toy calculation.")
    parser.add_argument("--H0-CMB", type=float, default=67.4)
    parser.add_argument("--H0-local-obs", type=float, default=73.0)
    parser.add_argument("--Omega-m", type=float, default=0.315)
    parser.add_argument("--Omega-DE", type=float, default=0.685)
    parser.add_argument("--f-succ-mean", type=float, default=0.15)
    parser.add_argument("--n", type=float, default=1.5, help="Fiducial environmental scaling exponent")
    parser.add_argument("--representative-delta", type=float, default=-0.35)
    parser.add_argument("--delta-min", type=float, default=-0.90)
    parser.add_argument("--delta-max", type=float, default=0.50)
    parser.add_argument("--delta-step", type=float, default=0.05)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parent / "outputs",
        help="Directory where CSV/JSON outputs will be written",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    params = PNTParameters(
        H0_CMB=args.H0_CMB,
        H0_local_obs=args.H0_local_obs,
        Omega_m=args.Omega_m,
        Omega_DE=args.Omega_DE,
        f_succ_mean=args.f_succ_mean,
        n_fiducial=args.n,
        representative_delta=args.representative_delta,
        delta_min=args.delta_min,
        delta_max=args.delta_max,
        delta_step=args.delta_step,
    )
    params.validate()

    output_dir: Path = args.output_dir
    n_values = [1.0, params.n_fiducial, 2.0]
    sensitivity_deltas = [-0.20, -0.30, -0.35, -0.40, -0.50]

    grid = grid_rows(params, n_values=n_values)
    sensitivity = sensitivity_rows(params, sensitivity_deltas, n_values=n_values)
    summary = fiducial_summary(params)

    write_csv(output_dir / "pnt_void_h0_grid.csv", grid)
    write_csv(output_dir / "pnt_void_h0_sensitivity.csv", sensitivity)
    write_json(output_dir / "pnt_void_h0_summary.json", summary)

    fid = summary["fiducial_case"]
    assert isinstance(fid, dict)
    print("PNT void-filament H0 toy calculation complete")
    print(f"Output directory: {output_dir}")
    print(f"Fiducial delta: {fid['delta']}")
    print(f"Fiducial H0_PNT: {fid['H0_pnt']:.3f} km/s/Mpc")
    print(f"Delta H0: {fid['delta_H0']:.3f} km/s/Mpc")
    print(f"Fraction of observed tension: {fid['tension_fraction_pct']:.1f}%")


if __name__ == "__main__":
    main()
