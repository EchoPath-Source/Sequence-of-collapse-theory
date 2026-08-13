#!/usr/bin/env python3
"""Deterministic RA/Dec/redshift -> comoving Cartesian conversion for DESI.

Primary geometry follows data/desi/DESI_DR1_COORDINATE_NEIGHBORHOOD_CONTRACT.md.
This module is a coordinate transform only. It does not classify environment or
make any SoCT/PNT inference.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Sequence

C_KMS = 299792.458
METHOD_VERSION = "desi-comoving-planck18-v0.1"


@dataclass(frozen=True)
class FlatLambdaCDM:
    h0: float = 67.4
    omega_m: float = 0.315

    @property
    def omega_lambda(self) -> float:
        return 1.0 - self.omega_m

    def validate(self) -> None:
        if not math.isfinite(self.h0) or self.h0 <= 0:
            raise ValueError("h0 must be finite and > 0")
        if not math.isfinite(self.omega_m) or not (0.0 < self.omega_m < 1.0):
            raise ValueError("omega_m must lie in (0,1) for this flat-LambdaCDM helper")


def e_z(z: float, cosmology: FlatLambdaCDM) -> float:
    cosmology.validate()
    if not math.isfinite(z) or z < 0:
        raise ValueError(f"invalid redshift: {z}")
    return math.sqrt(cosmology.omega_m * (1.0 + z) ** 3 + cosmology.omega_lambda)


def comoving_distance_mpc(z: float, cosmology: FlatLambdaCDM = FlatLambdaCDM(), n_steps: int = 2048) -> float:
    """Line-of-sight comoving distance in Mpc using composite Simpson integration."""
    cosmology.validate()
    if not math.isfinite(z) or z < 0:
        raise ValueError(f"invalid redshift: {z}")
    if z == 0:
        return 0.0
    if n_steps < 2:
        raise ValueError("n_steps must be >= 2")
    if n_steps % 2:
        n_steps += 1

    h = z / n_steps
    total = 1.0 / e_z(0.0, cosmology) + 1.0 / e_z(z, cosmology)
    for i in range(1, n_steps):
        zz = i * h
        total += (4.0 if i % 2 else 2.0) / e_z(zz, cosmology)
    integral = (h / 3.0) * total
    return (C_KMS / cosmology.h0) * integral


def validate_sky_position(ra_deg: float, dec_deg: float) -> None:
    if not math.isfinite(ra_deg) or not (0.0 <= ra_deg < 360.0):
        raise ValueError(f"invalid RA degrees: {ra_deg}")
    if not math.isfinite(dec_deg) or not (-90.0 <= dec_deg <= 90.0):
        raise ValueError(f"invalid Dec degrees: {dec_deg}")


def radec_z_to_cartesian(
    ra_deg: float,
    dec_deg: float,
    redshift: float,
    cosmology: FlatLambdaCDM = FlatLambdaCDM(),
    n_steps: int = 2048,
) -> tuple[float, float, float, float]:
    """Return (chi_mpc, x_mpc, y_mpc, z_cart_mpc)."""
    validate_sky_position(ra_deg, dec_deg)
    chi = comoving_distance_mpc(redshift, cosmology, n_steps=n_steps)
    ra = math.radians(ra_deg)
    dec = math.radians(dec_deg)
    cos_dec = math.cos(dec)
    x = chi * cos_dec * math.cos(ra)
    y = chi * cos_dec * math.sin(ra)
    z_cart = chi * math.sin(dec)
    return chi, x, y, z_cart


def convert_csv(
    input_path: Path,
    output_path: Path,
    cosmology: FlatLambdaCDM,
    ra_field: str = "mean_fiber_ra",
    dec_field: str = "mean_fiber_dec",
    z_field: str = "z",
    n_steps: int = 2048,
) -> int:
    with input_path.open(newline="", encoding="utf-8") as src:
        reader = csv.DictReader(src)
        fields = list(reader.fieldnames or [])
        required = {ra_field, dec_field, z_field}
        missing = required - set(fields)
        if missing:
            raise ValueError(f"missing required fields: {sorted(missing)}")
        extra = ["chi_mpc", "x", "y", "z_cart", "coordinate_method", "fiducial_h0", "fiducial_omega_m"]
        out_fields = fields + [name for name in extra if name not in fields]
        rows = []
        for row in reader:
            ra = float(row[ra_field])
            dec = float(row[dec_field])
            redshift = float(row[z_field])
            chi, x, y, z_cart = radec_z_to_cartesian(ra, dec, redshift, cosmology, n_steps=n_steps)
            row.update(
                {
                    "chi_mpc": repr(chi),
                    "x": repr(x),
                    "y": repr(y),
                    "z_cart": repr(z_cart),
                    "coordinate_method": METHOD_VERSION,
                    "fiducial_h0": repr(cosmology.h0),
                    "fiducial_omega_m": repr(cosmology.omega_m),
                }
            )
            rows.append(row)

    with output_path.open("w", newline="", encoding="utf-8") as dst:
        writer = csv.DictWriter(dst, fieldnames=out_fields)
        writer.writeheader()
        writer.writerows(rows)
    return len(rows)


def self_test() -> dict:
    cosmology = FlatLambdaCDM()
    d0 = comoving_distance_mpc(0.0, cosmology)
    d01 = comoving_distance_mpc(0.1, cosmology)
    d02 = comoving_distance_mpc(0.2, cosmology)
    if d0 != 0.0 or not (0.0 < d01 < d02):
        raise AssertionError("comoving distance monotonicity failed")

    chi, x, y, zc = radec_z_to_cartesian(0.0, 0.0, 0.1, cosmology)
    if not math.isclose(x, chi, rel_tol=0.0, abs_tol=1e-9):
        raise AssertionError("RA=0, Dec=0 x-axis transform failed")
    if abs(y) > 1e-9 or abs(zc) > 1e-9:
        raise AssertionError("RA=0, Dec=0 transverse coordinates failed")

    chi2, x2, y2, z2 = radec_z_to_cartesian(90.0, 0.0, 0.1, cosmology)
    if abs(x2) > 1e-9 or not math.isclose(y2, chi2, rel_tol=0.0, abs_tol=1e-9) or abs(z2) > 1e-9:
        raise AssertionError("RA=90, Dec=0 transform failed")

    return {
        "status": "PASS",
        "method": METHOD_VERSION,
        "h0": cosmology.h0,
        "omega_m": cosmology.omega_m,
        "chi_z_0_1_mpc": d01,
        "chi_z_0_2_mpc": d02,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--h0", type=float, default=67.4)
    parser.add_argument("--omega-m", type=float, default=0.315)
    parser.add_argument("--ra-field", default="mean_fiber_ra")
    parser.add_argument("--dec-field", default="mean_fiber_dec")
    parser.add_argument("--z-field", default="z")
    parser.add_argument("--steps", type=int, default=2048)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test or args.input is None:
        print(json.dumps(self_test(), indent=2, sort_keys=True))
        return 0
    if args.output is None:
        parser.error("--output is required with --input")

    cosmology = FlatLambdaCDM(h0=args.h0, omega_m=args.omega_m)
    rows = convert_csv(
        args.input,
        args.output,
        cosmology,
        ra_field=args.ra_field,
        dec_field=args.dec_field,
        z_field=args.z_field,
        n_steps=args.steps,
    )
    print(json.dumps({"status": "PASS", "rows": rows, "method": METHOD_VERSION}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
