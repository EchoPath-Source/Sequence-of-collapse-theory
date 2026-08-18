#!/usr/bin/env python3
"""SIM-04A: causal-order and earliest-response reconstruction.

Toy-model methodology benchmark only; not evidence for emergent spacetime or SoCT.

The estimator receives noisy intervention responses but no coordinates, edge
list, or hidden topological order. It attempts to recover:

1. direct one-step causal edges;
2. causal reachability within a finite observation horizon;
3. earliest detectable causal lag.

Raw response magnitude is deliberately not interpreted as distance.

Requires:
    numpy
    scikit-learn
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, asdict

import numpy as np
from sklearn.metrics import precision_score, recall_score


@dataclass
class Result:
    gain_mode: str
    trials: int
    seeds: int
    reachability_precision_mean: float
    reachability_recall_mean: float
    direct_edge_precision_mean: float
    direct_edge_recall_mean: float
    earliest_lag_mae_mean: float


def make_hidden_dag(
    n: int = 20,
    shortcut_probability: float = 0.12,
    seed: int = 0,
) -> tuple[np.ndarray, np.ndarray, np.random.Generator]:
    """Construct a positive weighted DAG with concealed topological order."""
    rng = np.random.default_rng(seed)
    order = rng.permutation(n)
    a = np.zeros((n, n), dtype=float)

    # A hidden backbone guarantees broad reachability.
    for k in range(n - 1):
        source = order[k]
        target = order[k + 1]
        a[target, source] = rng.uniform(0.55, 0.80)

    # Forward shortcuts create multiple causal paths without cycles.
    for i in range(n):
        for j in range(i + 2, n):
            if rng.random() < shortcut_probability:
                source = order[i]
                target = order[j]
                a[target, source] = rng.uniform(0.30, 0.75)

    return a, order, rng


def ground_truth(
    a: np.ndarray,
    max_lag: int,
    epsilon: float = 1e-12,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return direct edges, finite-horizon reachability, and earliest true lag."""
    n = a.shape[0]
    direct = np.abs(a) > epsilon
    reachability = np.zeros((n, n), dtype=bool)
    earliest = np.full((n, n), np.nan, dtype=float)

    power = np.eye(n)
    for lag in range(1, max_lag + 1):
        power = a @ power
        active = np.abs(power) > epsilon
        new = active & ~reachability
        earliest[new] = lag
        reachability |= active

    np.fill_diagonal(direct, False)
    np.fill_diagonal(reachability, False)
    return direct, reachability, earliest


def run_seed(
    seed: int,
    trials: int,
    gain_mode: str,
    noise_sigma: float = 0.10,
    z_threshold: float = 4.0,
    max_lag: int = 8,
) -> dict[str, float]:
    a, _, rng = make_hidden_dag(seed=seed)
    n = a.shape[0]

    if gain_mode == "uniform":
        gain = np.ones(n)
    elif gain_mode == "heterogeneous":
        gain = np.clip(np.exp(rng.normal(0.0, 1.0, size=n)), 0.20, 5.0)
    else:
        raise ValueError(f"unknown gain mode: {gain_mode}")

    # Noise of the estimated mean response after repeated randomized trials.
    standard_error = noise_sigma / np.sqrt(trials)

    inferred_reach = np.zeros((n, n), dtype=bool)
    inferred_earliest = np.full((n, n), np.nan, dtype=float)
    inferred_direct = np.zeros((n, n), dtype=bool)

    power = np.eye(n)
    for lag in range(1, max_lag + 1):
        power = a @ power

        # Receiver susceptibility affects amplitude, but the estimator uses
        # significance / earliest appearance rather than amplitude as distance.
        observed = gain[:, None] * power + rng.normal(
            0.0,
            standard_error,
            size=(n, n),
        )
        significant = np.abs(observed) / standard_error > z_threshold
        np.fill_diagonal(significant, False)

        new = significant & ~inferred_reach
        inferred_earliest[new] = lag
        inferred_reach |= significant

        if lag == 1:
            inferred_direct = significant.copy()

    true_direct, true_reach, true_earliest = ground_truth(a, max_lag=max_lag)
    mask = ~np.eye(n, dtype=bool)

    reach_precision = precision_score(
        true_reach[mask], inferred_reach[mask], zero_division=0
    )
    reach_recall = recall_score(
        true_reach[mask], inferred_reach[mask], zero_division=0
    )
    direct_precision = precision_score(
        true_direct[mask], inferred_direct[mask], zero_division=0
    )
    direct_recall = recall_score(
        true_direct[mask], inferred_direct[mask], zero_division=0
    )

    jointly_detected = true_reach & inferred_reach
    lag_mae = float(
        np.nanmean(
            np.abs(
                inferred_earliest[jointly_detected]
                - true_earliest[jointly_detected]
            )
        )
    )

    return {
        "reach_precision": float(reach_precision),
        "reach_recall": float(reach_recall),
        "direct_precision": float(direct_precision),
        "direct_recall": float(direct_recall),
        "lag_mae": lag_mae,
    }


def run_case(gain_mode: str, trials: int, seeds: int) -> Result:
    rows = [run_seed(seed, trials, gain_mode) for seed in range(seeds)]
    return Result(
        gain_mode=gain_mode,
        trials=trials,
        seeds=seeds,
        reachability_precision_mean=float(np.mean([r["reach_precision"] for r in rows])),
        reachability_recall_mean=float(np.mean([r["reach_recall"] for r in rows])),
        direct_edge_precision_mean=float(np.mean([r["direct_precision"] for r in rows])),
        direct_edge_recall_mean=float(np.mean([r["direct_recall"] for r in rows])),
        earliest_lag_mae_mean=float(np.mean([r["lag_mae"] for r in rows])),
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seeds", type=int, default=100)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    results = [
        run_case(gain_mode, trials, args.seeds)
        for gain_mode in ("uniform", "heterogeneous")
        for trials in (25, 50, 100, 200, 500)
    ]

    if args.json:
        print(json.dumps([asdict(result) for result in results], indent=2))
        return

    print("SIM-04A causal-order / earliest-response reconstruction")
    print("gain mode       trials   reach P/R       direct P/R      lag MAE")
    for r in results:
        print(
            f"{r.gain_mode:14s} {r.trials:6d}   "
            f"{r.reachability_precision_mean:.4f}/{r.reachability_recall_mean:.4f}   "
            f"{r.direct_edge_precision_mean:.4f}/{r.direct_edge_recall_mean:.4f}   "
            f"{r.earliest_lag_mae_mean:.4f}"
        )


if __name__ == "__main__":
    main()
