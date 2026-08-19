#!/usr/bin/env python3
"""RM-01: persistent-record geometry reconstruction benchmark.

Exploratory toy-model methodology only. This is not evidence for SoCT,
emergent spacetime, or a historical/metaphysical source claim.

Question
--------
Can an effective latent geometry be reconstructed using only the pattern of
persistent, redundantly accessible records left by localized events?

The hidden substrate is an L x L periodic square lattice (2-torus). Each event
can leave records in many environmental fragments. The benchmark compares:

1. local: record probability decays with hidden torus distance;
2. scrambled: each event keeps the same probability multiset but fragment
   assignments are independently permuted, destroying locality;
3. global: each event has the same mean record density but no local structure.

Candidate record distances
--------------------------
- Jaccard support distance
- binary Hamming distance
- binary variation of information (VI)

Evaluation
----------
- Spearman correlation with hidden torus distance
- k-nearest-neighbor recovery

A useful method must outperform the scrambled/global nulls. High redundancy
alone is not sufficient: locality/structured overlap must matter.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path

import numpy as np
from scipy.stats import spearmanr


BROADCAST_VALUES = (0.2, 0.4, 0.6, 0.8, 1.0)
PERSISTENCE_VALUES = (0.40, 0.60, 0.80, 0.95)
MODES = ("local", "scrambled", "global")


@dataclass
class SweepRow:
    mode: str
    broadcast: float
    persistence: float
    record_density_mean: float
    record_density_sd: float
    jaccard_rho_mean: float
    jaccard_rho_sd: float
    jaccard_knn_mean: float
    jaccard_knn_sd: float
    hamming_rho_mean: float
    hamming_rho_sd: float
    vi_rho_mean: float
    vi_rho_sd: float
    seeds: int


def safe_spearman(a: np.ndarray, b: np.ndarray) -> float:
    value = spearmanr(a, b).statistic
    return float(value) if np.isfinite(value) else 0.0


def torus_distance(a: np.ndarray, b: np.ndarray, side: int) -> np.ndarray:
    delta = np.abs(a[:, None, :] - b[None, :, :])
    delta = np.minimum(delta, side - delta)
    return np.sqrt(np.sum(delta * delta, axis=2))


def entropy_from_counts(counts: np.ndarray, total: int) -> np.ndarray:
    probabilities = counts / float(total)
    with np.errstate(divide="ignore", invalid="ignore"):
        terms = np.where(
            probabilities > 0.0,
            -probabilities * np.log2(probabilities),
            0.0,
        )
    return np.sum(terms, axis=-1)


def record_distance_matrices(records: np.ndarray) -> dict[str, np.ndarray]:
    r = records.astype(np.int16, copy=False)
    n_events, n_fragments = r.shape
    ones = np.sum(r, axis=1, dtype=float)
    intersection = (r @ r.T).astype(float)

    union = ones[:, None] + ones[None, :] - intersection
    with np.errstate(divide="ignore", invalid="ignore"):
        jaccard = np.where(
            union > 0.0,
            1.0 - intersection / union,
            1.0,
        )
    np.fill_diagonal(jaccard, 0.0)

    hamming = (
        ones[:, None] + ones[None, :] - 2.0 * intersection
    ) / float(n_fragments)
    np.fill_diagonal(hamming, 0.0)

    c11 = intersection
    c10 = ones[:, None] - intersection
    c01 = ones[None, :] - intersection
    c00 = n_fragments - c11 - c10 - c01
    h_xy = entropy_from_counts(
        np.stack([c00, c01, c10, c11], axis=-1),
        n_fragments,
    )
    h_x = entropy_from_counts(
        np.stack([n_fragments - ones, ones], axis=-1),
        n_fragments,
    )
    vi = 2.0 * h_xy - h_x[:, None] - h_x[None, :]
    vi = np.maximum(vi, 0.0)
    np.fill_diagonal(vi, 0.0)

    return {
        "jaccard": jaccard,
        "hamming": hamming,
        "vi": vi,
    }


def generate_records(
    *,
    side: int,
    replicas: int,
    lengthscale: float,
    broadcast: float,
    persistence: float,
    mode: str,
    seed: int,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)
    event_coords = np.asarray(
        [(x, y) for x in range(side) for y in range(side)],
        dtype=float,
    )
    fragment_coords = np.repeat(event_coords, replicas, axis=0)

    event_fragment_distance = torus_distance(
        event_coords,
        fragment_coords,
        side,
    )
    local_probability = broadcast * np.exp(
        -event_fragment_distance / lengthscale
    )

    records = np.zeros(
        (len(event_coords), len(fragment_coords)),
        dtype=np.int8,
    )

    for event in range(len(event_coords)):
        if mode == "local":
            probability = local_probability[event]
        elif mode == "scrambled":
            probability = rng.permutation(local_probability[event])
        elif mode == "global":
            probability = np.full(
                len(fragment_coords),
                float(np.mean(local_probability[event])),
            )
        else:
            raise ValueError(f"unknown mode: {mode}")

        encoded = rng.random(len(fragment_coords)) < probability
        retained = rng.random(len(fragment_coords)) < persistence
        records[event] = encoded & retained

    hidden_distance = torus_distance(
        event_coords,
        event_coords,
        side,
    )
    return records, hidden_distance, event_coords


def knn_recovery(
    candidate_distance: np.ndarray,
    hidden_distance: np.ndarray,
    k: int,
) -> float:
    n = len(candidate_distance)
    scores: list[float] = []

    for i in range(n):
        mask_self = np.arange(n) == i
        true_order = np.argsort(
            np.where(mask_self, np.inf, hidden_distance[i])
        )
        candidate_order = np.argsort(
            np.where(mask_self, np.inf, candidate_distance[i])
        )
        overlap = len(
            set(true_order[:k]) & set(candidate_order[:k])
        )
        scores.append(overlap / float(k))

    return float(np.mean(scores))


def one_trial(
    *,
    side: int,
    replicas: int,
    lengthscale: float,
    broadcast: float,
    persistence: float,
    mode: str,
    seed: int,
    k: int,
) -> dict[str, float]:
    records, hidden_distance, _ = generate_records(
        side=side,
        replicas=replicas,
        lengthscale=lengthscale,
        broadcast=broadcast,
        persistence=persistence,
        mode=mode,
        seed=seed,
    )
    candidates = record_distance_matrices(records)
    upper = np.triu_indices(len(records), 1)
    hidden_vector = hidden_distance[upper]

    result = {
        "record_density": float(np.mean(records)),
    }
    for name, matrix in candidates.items():
        result[f"{name}_rho"] = safe_spearman(
            matrix[upper],
            hidden_vector,
        )
        if name == "jaccard":
            result["jaccard_knn"] = knn_recovery(
                matrix,
                hidden_distance,
                k,
            )
    return result


def summarize(
    *,
    side: int,
    replicas: int,
    lengthscale: float,
    seeds: int,
    k: int,
) -> list[SweepRow]:
    rows: list[SweepRow] = []

    for mode in MODES:
        for broadcast in BROADCAST_VALUES:
            for persistence in PERSISTENCE_VALUES:
                trials = [
                    one_trial(
                        side=side,
                        replicas=replicas,
                        lengthscale=lengthscale,
                        broadcast=broadcast,
                        persistence=persistence,
                        mode=mode,
                        seed=seed,
                        k=k,
                    )
                    for seed in range(seeds)
                ]

                def stats(key: str) -> tuple[float, float]:
                    values = np.asarray(
                        [trial[key] for trial in trials],
                        dtype=float,
                    )
                    return (
                        float(np.mean(values)),
                        float(np.std(values)),
                    )

                density_mean, density_sd = stats("record_density")
                jac_rho_mean, jac_rho_sd = stats("jaccard_rho")
                jac_knn_mean, jac_knn_sd = stats("jaccard_knn")
                ham_rho_mean, ham_rho_sd = stats("hamming_rho")
                vi_rho_mean, vi_rho_sd = stats("vi_rho")

                rows.append(
                    SweepRow(
                        mode=mode,
                        broadcast=broadcast,
                        persistence=persistence,
                        record_density_mean=density_mean,
                        record_density_sd=density_sd,
                        jaccard_rho_mean=jac_rho_mean,
                        jaccard_rho_sd=jac_rho_sd,
                        jaccard_knn_mean=jac_knn_mean,
                        jaccard_knn_sd=jac_knn_sd,
                        hamming_rho_mean=ham_rho_mean,
                        hamming_rho_sd=ham_rho_sd,
                        vi_rho_mean=vi_rho_mean,
                        vi_rho_sd=vi_rho_sd,
                        seeds=seeds,
                    )
                )

    return rows


def write_csv(rows: list[SweepRow], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(asdict(rows[0]).keys())
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))


def select_row(
    rows: list[SweepRow],
    *,
    mode: str,
    broadcast: float,
    persistence: float,
) -> SweepRow:
    for row in rows:
        if (
            row.mode == mode
            and row.broadcast == broadcast
            and row.persistence == persistence
        ):
            return row
    raise RuntimeError("requested summary row not found")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--side", type=int, default=8)
    parser.add_argument("--replicas", type=int, default=8)
    parser.add_argument("--lengthscale", type=float, default=1.4)
    parser.add_argument("--seeds", type=int, default=30)
    parser.add_argument("--knn-k", type=int, default=4)
    parser.add_argument(
        "--out-csv",
        type=Path,
        default=Path("rm01_record_geometry_sweep.csv"),
    )
    parser.add_argument(
        "--out-json",
        type=Path,
        default=Path("rm01_record_geometry_summary.json"),
    )
    args = parser.parse_args()

    rows = summarize(
        side=args.side,
        replicas=args.replicas,
        lengthscale=args.lengthscale,
        seeds=args.seeds,
        k=args.knn_k,
    )
    write_csv(rows, args.out_csv)

    strong = {
        mode: asdict(
            select_row(
                rows,
                mode=mode,
                broadcast=1.0,
                persistence=0.95,
            )
        )
        for mode in MODES
    }
    payload = {
        "claim_level": (
            "toy-model methodology only; not evidence for SoCT or "
            "emergent spacetime"
        ),
        "hidden_geometry": f"{args.side}x{args.side} periodic square lattice",
        "replicas_per_site": args.replicas,
        "lengthscale": args.lengthscale,
        "seeds": args.seeds,
        "knn_k": args.knn_k,
        "strong_regime": strong,
    }
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(
        json.dumps(payload, indent=2) + "\n",
        encoding="utf-8",
    )

    for mode in MODES:
        row = strong[mode]
        print(
            f"{mode:10s} "
            f"Jaccard rho={row['jaccard_rho_mean']:.3f} +/- "
            f"{row['jaccard_rho_sd']:.3f}; "
            f"kNN={row['jaccard_knn_mean']:.3f}; "
            f"Hamming rho={row['hamming_rho_mean']:.3f}; "
            f"VI rho={row['vi_rho_mean']:.3f}; "
            f"density={row['record_density_mean']:.3f}"
        )


if __name__ == "__main__":
    main()
