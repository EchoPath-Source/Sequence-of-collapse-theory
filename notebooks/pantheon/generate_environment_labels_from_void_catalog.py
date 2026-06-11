#!/usr/bin/env python3
"""
Generate preliminary Pantheon+ environment labels from an extracted SDSS void catalog.

This script creates a derived cross-match table for the Pantheon+ environment-H0
track. It expects the public Pantheon+SH0ES table and an already-extracted SDSS
void catalog directory. It does not download data and does not unpack archives.

Labels are conservative void-catalog labels, not official Pantheon+ labels and
not full void/sheet/filament/node cosmic-web classifications.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

import numpy as np
import pandas as pd

C_KM_S = 299792.458
H0 = 70.0
OMEGA_M = 0.3
METHOD_VERSION = "sdss_void_catalog_crossmatch_v0.1"


def comoving_distance_mpc_h(z_values: np.ndarray) -> np.ndarray:
    """Flat-LCDM comoving distance approximation in Mpc/h."""
    omega_l = 1.0 - OMEGA_M
    distances = []
    for z in np.asarray(z_values, dtype=float):
        if not np.isfinite(z) or z <= 0:
            distances.append(np.nan)
            continue
        grid = np.linspace(0.0, z, 256)
        ez = np.sqrt(OMEGA_M * (1.0 + grid) ** 3 + omega_l)
        dc_mpc = (C_KM_S / H0) * np.trapz(1.0 / ez, grid)
        distances.append(dc_mpc * (H0 / 100.0))
    return np.asarray(distances)


def radec_to_xyz(ra_deg: np.ndarray, dec_deg: np.ndarray, redshift: np.ndarray) -> np.ndarray:
    r = comoving_distance_mpc_h(redshift)
    ra = np.deg2rad(np.asarray(ra_deg, dtype=float))
    dec = np.deg2rad(np.asarray(dec_deg, dtype=float))
    return np.column_stack([
        r * np.cos(dec) * np.cos(ra),
        r * np.cos(dec) * np.sin(ra),
        r * np.sin(dec),
    ])


def read_pantheon(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Missing Pantheon+SH0ES table: {path}")
    table = pd.read_csv(path, sep=r"\s+", comment="#")
    required = ["CID", "IDSURVEY", "RA", "DEC", "zHD", "zCMB"]
    missing = [col for col in required if col not in table.columns]
    if missing:
        raise ValueError(f"Pantheon+ table missing required columns: {missing}")
    return table.reset_index().rename(columns={"index": "row_index"})


def parse_sample_redshift_range(sample_info: Path) -> tuple[float, float] | None:
    text = sample_info.read_text(errors="replace")
    match = re.search(r"Redshift range:\s*([0-9.eE+-]+)\s*-\s*([0-9.eE+-]+)", text)
    if not match:
        return None
    return float(match.group(1)), float(match.group(2))


def load_void_centers(catalog_dir: Path) -> pd.DataFrame:
    if not catalog_dir.exists() or not catalog_dir.is_dir():
        raise FileNotFoundError(f"Missing extracted void catalog directory: {catalog_dir}")

    rows = []
    for sample_info in catalog_dir.rglob("sample_info.txt"):
        z_range = parse_sample_redshift_range(sample_info)
        if z_range is None:
            continue
        sample_dir = sample_info.parent
        sky_files = list(sample_dir.glob("sky_positions_central*.out"))
        for sky_path in sky_files:
            try:
                data = pd.read_csv(sky_path, sep=r"\s+", comment="#", header=None)
            except Exception:
                continue
            if data.shape[1] < 4:
                continue
            frame = pd.DataFrame({
                "void_ra": pd.to_numeric(data.iloc[:, 0], errors="coerce"),
                "void_dec": pd.to_numeric(data.iloc[:, 1], errors="coerce"),
                "void_z": pd.to_numeric(data.iloc[:, 2], errors="coerce"),
                "void_radius_mpc_h": pd.to_numeric(data.iloc[:, 3], errors="coerce"),
                "void_id": data.iloc[:, 4].astype(str) if data.shape[1] > 4 else data.index.astype(str),
                "sample_name": sample_dir.name,
                "sample_z_min": z_range[0],
                "sample_z_max": z_range[1],
                "catalog_file": str(sky_path.relative_to(catalog_dir)),
            })
            rows.append(frame)

    if not rows:
        raise ValueError("No supported sky_positions_central*.out files found in catalog directory")

    voids = pd.concat(rows, ignore_index=True).dropna(
        subset=["void_ra", "void_dec", "void_z", "void_radius_mpc_h"]
    )
    xyz = radec_to_xyz(voids["void_ra"].to_numpy(), voids["void_dec"].to_numpy(), voids["void_z"].to_numpy())
    voids[["void_x_mpc_h", "void_y_mpc_h", "void_z_mpc_h"]] = xyz
    return voids.reset_index(drop=True)


def classify(pantheon: pd.DataFrame, voids: pd.DataFrame) -> pd.DataFrame:
    sn_xyz = radec_to_xyz(pantheon["RA"].to_numpy(), pantheon["DEC"].to_numpy(), pantheon["zHD"].to_numpy())
    out_rows = []

    for idx, sn in pantheon.iterrows():
        base = {
            "row_index": int(sn["row_index"]),
            "CID": sn["CID"],
            "IDSURVEY": int(sn["IDSURVEY"]),
            "RA": float(sn["RA"]),
            "DEC": float(sn["DEC"]),
            "zHD": float(sn["zHD"]),
            "zCMB": float(sn["zCMB"]),
            "environment_method": METHOD_VERSION,
            "catalog_source": "SDSS public void catalog; central sky-position void centers",
        }
        z = float(sn["zHD"])
        covered = voids[(voids["sample_z_min"] <= z) & (z <= voids["sample_z_max"])]
        if covered.empty or not np.isfinite(sn_xyz[idx]).all():
            out_rows.append({
                **base,
                "environment_label": "outside_catalog_coverage",
                "nearest_void_id": "",
                "nearest_void_sample": "",
                "nearest_void_distance_mpc_h": np.nan,
                "nearest_void_radius_mpc_h": np.nan,
                "void_distance_over_radius": np.nan,
                "coverage_flag": "outside_redshift_or_invalid_position",
                "notes": "No covered SDSS void sample for this row.",
            })
            continue

        centers = covered[["void_x_mpc_h", "void_y_mpc_h", "void_z_mpc_h"]].to_numpy()
        distances = np.linalg.norm(centers - sn_xyz[idx], axis=1)
        nearest_i = int(np.nanargmin(distances))
        nearest = covered.iloc[nearest_i]
        nearest_distance = float(distances[nearest_i])
        radius = float(nearest["void_radius_mpc_h"])
        ratio = nearest_distance / radius if radius > 0 else np.nan

        if ratio <= 1.0:
            label = "void"
            flag = "inside_void_radius"
        elif ratio <= 1.25:
            label = "near_void_edge"
            flag = "near_void_edge_buffer"
        else:
            label = "sdss_nonvoid"
            flag = "covered_not_near_void"

        out_rows.append({
            **base,
            "environment_label": label,
            "nearest_void_id": nearest["void_id"],
            "nearest_void_sample": nearest["sample_name"],
            "nearest_void_distance_mpc_h": nearest_distance,
            "nearest_void_radius_mpc_h": radius,
            "void_distance_over_radius": ratio,
            "coverage_flag": flag,
            "notes": "Derived void-catalog label; not a true filament classification.",
        })

    return pd.DataFrame(out_rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pantheon", type=Path, default=Path("data/pantheon/raw/Pantheon+SH0ES.dat"))
    parser.add_argument("--void-catalog-dir", type=Path, default=Path("data/pantheon/external/void_catalog_2014.06.18_just_sdss"))
    parser.add_argument("--output", type=Path, default=Path("data/pantheon/environment_labels.csv"))
    args = parser.parse_args()

    try:
        pantheon = read_pantheon(args.pantheon)
        voids = load_void_centers(args.void_catalog_dir)
        labels = classify(pantheon, voids)
    except Exception as exc:
        print(f"INPUT ERROR: {exc}")
        print("Provide raw Pantheon+SH0ES data and an extracted void catalog directory, or pass explicit paths.")
        return 2

    if len(labels) != len(pantheon):
        raise RuntimeError("environment_labels row count does not match Pantheon+ input")
    if not labels["row_index"].equals(pd.Series(range(len(labels)))):
        raise RuntimeError("row_index does not preserve Pantheon+ row order")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    labels.to_csv(args.output, index=False)
    print(f"Wrote {len(labels)} environment labels to {args.output}")
    print(labels["environment_label"].value_counts(dropna=False).to_string())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
