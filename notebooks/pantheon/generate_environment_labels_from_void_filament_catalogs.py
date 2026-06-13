#!/usr/bin/env python3
"""
Generate preliminary Pantheon+ environment labels from SDSS void + filament catalogs.

This script is a second-stage environment-label generator for the Pantheon+
environment-H0 track. It combines:

1. Pantheon+SH0ES row-order supernova table.
2. An extracted public SDSS void catalog directory.
3. An extracted Tempel et al. / Bisous SDSS filament catalog directory
   from VizieR J/MNRAS/438/3465.

The output is a row-aligned `environment_labels.csv` table. Labels are derived
cross-match labels, not official Pantheon+ labels and not a final publication-
grade cosmic-web classification without independent validation.
"""
from __future__ import annotations

import argparse
import gzip
import re
from pathlib import Path

import numpy as np
import pandas as pd

C_KM_S = 299792.458
H0 = 70.0
OMEGA_M = 0.3
METHOD_VERSION = "sdss_void_filament_crossmatch_v0.1"


def comoving_distance_mpc_h(z_values: np.ndarray) -> np.ndarray:
    """Approximate flat-LCDM comoving distance in Mpc/h."""
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
        for sky_path in sample_dir.glob("sky_positions_central*.out"):
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
                "void_sample": sample_dir.name,
                "void_z_min": z_range[0],
                "void_z_max": z_range[1],
            })
            rows.append(frame)
    if not rows:
        raise ValueError("No supported sky_positions_central*.out files found in void catalog directory")
    voids = pd.concat(rows, ignore_index=True).dropna(
        subset=["void_ra", "void_dec", "void_z", "void_radius_mpc_h"]
    )
    xyz = radec_to_xyz(voids["void_ra"].to_numpy(), voids["void_dec"].to_numpy(), voids["void_z"].to_numpy())
    voids[["void_x_mpc_h", "void_y_mpc_h", "void_z_mpc_h"]] = xyz
    return voids.reset_index(drop=True)


def open_text(path: Path):
    if path.suffix == ".gz":
        return gzip.open(path, "rt")
    return path.open("rt")


def load_filament_points(catalog_dir: Path) -> pd.DataFrame:
    """Load Tempel/Bisous filament point table2 as comoving Mpc/h coordinates."""
    if not catalog_dir.exists() or not catalog_dir.is_dir():
        raise FileNotFoundError(f"Missing extracted filament catalog directory: {catalog_dir}")
    candidates = [catalog_dir / "table2.dat.gz", catalog_dir / "table2.dat"]
    table_path = next((p for p in candidates if p.exists()), None)
    if table_path is None:
        raise FileNotFoundError("Missing table2.dat.gz or table2.dat in filament catalog directory")
    rows = []
    with open_text(table_path) as handle:
        for line in handle:
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            parts = line.split()
            if len(parts) < 14:
                continue
            rows.append({
                "filament_id": int(parts[0]),
                "filament_point_id": int(parts[1]),
                "filament_npts": int(parts[2]),
                "filament_len_mpc_h": float(parts[3]),
                "filament_x_mpc_h": float(parts[4]),
                "filament_y_mpc_h": float(parts[5]),
                "filament_z_mpc_h": float(parts[6]),
                "filament_point_density": float(parts[11]),
                "filament_orientation_strength": float(parts[13]),
            })
    if not rows:
        raise ValueError("No filament points parsed from table2")
    return pd.DataFrame(rows)


def classify(pantheon: pd.DataFrame, voids: pd.DataFrame, filaments: pd.DataFrame) -> pd.DataFrame:
    sn_xyz = radec_to_xyz(pantheon["RA"].to_numpy(), pantheon["DEC"].to_numpy(), pantheon["zHD"].to_numpy())
    filament_xyz = filaments[["filament_x_mpc_h", "filament_y_mpc_h", "filament_z_mpc_h"]].to_numpy()
    out_rows = []

    for idx, sn in pantheon.iterrows():
        z = float(sn["zHD"])
        base = {
            "row_index": int(sn["row_index"]),
            "CID": sn["CID"],
            "IDSURVEY": int(sn["IDSURVEY"]),
            "RA": float(sn["RA"]),
            "DEC": float(sn["DEC"]),
            "zHD": z,
            "zCMB": float(sn["zCMB"]),
            "environment_method": METHOD_VERSION,
            "catalog_source": "SDSS void catalog plus Tempel/Bisous SDSS filament catalog J/MNRAS/438/3465",
        }

        if not np.isfinite(sn_xyz[idx]).all():
            out_rows.append({**base, "environment_label": "outside_catalog_coverage", "coverage_flag": "invalid_position"})
            continue

        covered_voids = voids[(voids["void_z_min"] <= z) & (z <= voids["void_z_max"])]
        void_label = "outside_catalog_coverage"
        void_distance = np.nan
        void_radius = np.nan
        void_ratio = np.nan
        nearest_void_id = ""
        nearest_void_sample = ""
        if not covered_voids.empty:
            void_centers = covered_voids[["void_x_mpc_h", "void_y_mpc_h", "void_z_mpc_h"]].to_numpy()
            void_distances = np.linalg.norm(void_centers - sn_xyz[idx], axis=1)
            vi = int(np.nanargmin(void_distances))
            nearest_void = covered_voids.iloc[vi]
            void_distance = float(void_distances[vi])
            void_radius = float(nearest_void["void_radius_mpc_h"])
            void_ratio = void_distance / void_radius if void_radius > 0 else np.nan
            nearest_void_id = nearest_void["void_id"]
            nearest_void_sample = nearest_void["void_sample"]
            if void_ratio <= 1.0:
                void_label = "void"
            elif void_ratio <= 1.25:
                void_label = "near_void_edge"
            else:
                void_label = "not_void"

        # Filament catalog galaxy sample covers z about 0.009--0.2. Use only this local range.
        filament_label = "outside_filament_catalog_redshift"
        filament_distance = np.nan
        nearest_filament_id = ""
        nearest_filament_point_id = ""
        if 0.009 <= z <= 0.2:
            distances = np.linalg.norm(filament_xyz - sn_xyz[idx], axis=1)
            fi = int(np.nanargmin(distances))
            nearest_fil = filaments.iloc[fi]
            filament_distance = float(distances[fi])
            nearest_filament_id = int(nearest_fil["filament_id"])
            nearest_filament_point_id = int(nearest_fil["filament_point_id"])
            if filament_distance <= 0.5:
                filament_label = "filament"
            elif filament_distance <= 1.0:
                filament_label = "near_filament"
            else:
                filament_label = "field_or_wall"

        if void_label in {"void", "near_void_edge"}:
            final_label = void_label
        elif filament_label in {"filament", "near_filament", "field_or_wall"}:
            final_label = filament_label
        elif void_label == "not_void":
            final_label = "sdss_nonvoid"
        else:
            final_label = "outside_catalog_coverage"

        out_rows.append({
            **base,
            "environment_label": final_label,
            "void_label": void_label,
            "filament_label": filament_label,
            "nearest_void_id": nearest_void_id,
            "nearest_void_sample": nearest_void_sample,
            "nearest_void_distance_mpc_h": void_distance,
            "nearest_void_radius_mpc_h": void_radius,
            "void_distance_over_radius": void_ratio,
            "nearest_filament_id": nearest_filament_id,
            "nearest_filament_point_id": nearest_filament_point_id,
            "nearest_filament_distance_mpc_h": filament_distance,
            "coverage_flag": "derived_crossmatch" if final_label != "outside_catalog_coverage" else "outside_catalog_coverage",
            "notes": "Derived void+filament cross-match; preliminary, not official Pantheon+ metadata.",
        })

    return pd.DataFrame(out_rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pantheon", type=Path, default=Path("data/pantheon/raw/Pantheon+SH0ES.dat"))
    parser.add_argument("--void-catalog-dir", type=Path, default=Path("data/pantheon/external/void_catalog_2014.06.18_just_sdss"))
    parser.add_argument("--filament-catalog-dir", type=Path, default=Path("data/pantheon/external/J_MNRAS_438_3465"))
    parser.add_argument("--output", type=Path, default=Path("data/pantheon/environment_labels.csv"))
    args = parser.parse_args()

    try:
        pantheon = read_pantheon(args.pantheon)
        voids = load_void_centers(args.void_catalog_dir)
        filaments = load_filament_points(args.filament_catalog_dir)
        labels = classify(pantheon, voids, filaments)
    except Exception as exc:
        print(f"INPUT ERROR: {exc}")
        print("Provide raw Pantheon+ data plus extracted SDSS void and Tempel/Bisous filament catalog directories.")
        return 2

    if len(labels) != len(pantheon):
        raise RuntimeError("environment_labels row count does not match Pantheon+ input")
    if not labels["row_index"].equals(pd.Series(range(len(labels)))):
        raise RuntimeError("row_index does not preserve Pantheon+ row order")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    labels.to_csv(args.output, index=False)
    print(f"Wrote {len(labels)} labels to {args.output}")
    print(labels["environment_label"].value_counts(dropna=False).to_string())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
