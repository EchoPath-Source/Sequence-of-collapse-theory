#!/usr/bin/env python3
"""SIM-03B: susceptibility and criticality adversary.

Toy-model methodology test only; not evidence for SoCT.

Purpose
-------
Test the confound

    large response != strong transmission != small distance != same object

by separating receiver susceptibility from direct transmission and then asking
what happens when long-time recurrent amplification is used instead of the
first/direct response.

Requires:
    numpy
    scipy
    scikit-learn
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, asdict

import numpy as np
from scipy.stats import spearmanr
from sklearn.cluster import SpectralClustering
from sklearn.metrics import adjusted_rand_score, roc_auc_score


@dataclass
class SusceptibilityResult:
    case: str
    seeds: int
    ari_raw_mean: float
    ari_normalized_mean: float
    module_auc_raw_mean: float
    module_auc_normalized_mean: float
    transmission_rho_raw_mean: float
    transmission_rho_normalized_mean: float
    gain_hub_rho_raw_mean: float | None
    gain_hub_rho_normalized_mean: float | None


@dataclass
class CriticalityResult:
    spectral_radius: float
    seeds: int
    direct_rho_raw_mean: float
    direct_rho_normalized_mean: float
    integrated_rho_raw_mean: float
    integrated_rho_normalized_mean: float
    integrated_ari_raw_mean: float
    integrated_ari_normalized_mean: float


def make_block_system(
    n: int = 18,
    groups: int = 3,
    within: float = 0.42,
    between: float = 0.11,
    seed: int = 0,
) -> tuple[np.ndarray, np.ndarray, np.random.Generator]:
    """Create a directed modular transmission matrix with hidden labels."""
    rng = np.random.default_rng(seed)
    group_size = n // groups
    labels = np.repeat(np.arange(groups), group_size)

    w = rng.normal(0.0, 0.006, size=(n, n))
    for target in range(n):
        for source in range(n):
            if target == source:
                w[target, source] = 0.0
            elif labels[target] == labels[source]:
                w[target, source] += within / group_size
            else:
                w[target, source] += between / n

    permutation = rng.permutation(n)
    w = w[np.ix_(permutation, permutation)]
    labels = labels[permutation]
    return w, labels, rng


def spectral_partition(affinity: np.ndarray, groups: int, seed: int) -> np.ndarray:
    a = np.maximum((affinity + affinity.T) / 2.0, 0.0)
    np.fill_diagonal(a, max(float(np.max(a)), 1e-6))
    return SpectralClustering(
        n_clusters=groups,
        affinity="precomputed",
        assign_labels="kmeans",
        random_state=seed,
    ).fit_predict(a)


def sym_strength(matrix: np.ndarray) -> np.ndarray:
    return (np.abs(matrix) + np.abs(matrix.T)) / 2.0


def safe_abs_spearman(x: np.ndarray, y: np.ndarray) -> float | None:
    if np.allclose(x, x[0]) or np.allclose(y, y[0]):
        return None
    value = float(spearmanr(x, y).statistic)
    if not np.isfinite(value):
        return None
    return abs(value)


def susceptibility_case_parameters(case: str) -> tuple[float, float, float, bool]:
    """Return gain sigma, calibration noise, measurement noise, uniform flag."""
    if case == "uniform":
        return 0.0, 0.02, 0.0015, True
    if case == "heterogeneous":
        return 1.25, 0.03, 0.0015, False
    if case == "extreme":
        return 2.0, 0.05, 0.0015, False
    if case == "noisy_calibration":
        return 1.5, 0.30, 0.0015, False
    raise ValueError(f"unknown case: {case}")


def run_susceptibility_seed(seed: int, case: str) -> dict[str, float | None]:
    sigma, calibration_noise, measurement_noise, uniform = susceptibility_case_parameters(case)
    w, truth, rng = make_block_system(seed=seed)
    n = w.shape[0]

    if uniform:
        gain = np.ones(n)
    else:
        gain = np.clip(np.exp(rng.normal(0.0, sigma, size=n)), 0.08, 10.0)

    # Small-signal observed one-step response. Receiver gain multiplies the
    # actual transmission into that receiver.
    observed = gain[:, None] * w + rng.normal(0.0, measurement_noise, size=w.shape)

    # Independent local calibration probe estimates receiver susceptibility.
    gain_hat = np.maximum(
        gain * (1.0 + rng.normal(0.0, calibration_noise, size=n)),
        0.03,
    )
    normalized = observed / gain_hat[:, None]

    true_affinity = sym_strength(w)
    raw_affinity = sym_strength(observed)
    norm_affinity = sym_strength(normalized)

    groups = len(np.unique(truth))
    pred_raw = spectral_partition(raw_affinity, groups, seed)
    pred_norm = spectral_partition(norm_affinity, groups, seed)

    upper = np.triu(np.ones((n, n), dtype=bool), 1)
    same_module = (truth[:, None] == truth[None, :])[upper].astype(int)

    true_edges = true_affinity[upper]
    raw_edges = raw_affinity[upper]
    norm_edges = norm_affinity[upper]

    return {
        "ari_raw": float(adjusted_rand_score(truth, pred_raw)),
        "ari_normalized": float(adjusted_rand_score(truth, pred_norm)),
        "module_auc_raw": float(roc_auc_score(same_module, raw_edges)),
        "module_auc_normalized": float(roc_auc_score(same_module, norm_edges)),
        "transmission_rho_raw": float(spearmanr(true_edges, raw_edges).statistic),
        "transmission_rho_normalized": float(spearmanr(true_edges, norm_edges).statistic),
        "gain_hub_rho_raw": safe_abs_spearman(gain, raw_affinity.sum(axis=1)),
        "gain_hub_rho_normalized": safe_abs_spearman(gain, norm_affinity.sum(axis=1)),
    }


def mean_optional(values: list[float | None]) -> float | None:
    finite = [float(v) for v in values if v is not None and np.isfinite(v)]
    return float(np.mean(finite)) if finite else None


def run_susceptibility_case(case: str, seeds: int) -> SusceptibilityResult:
    rows = [run_susceptibility_seed(seed, case) for seed in range(seeds)]
    return SusceptibilityResult(
        case=case,
        seeds=seeds,
        ari_raw_mean=float(np.mean([r["ari_raw"] for r in rows])),
        ari_normalized_mean=float(np.mean([r["ari_normalized"] for r in rows])),
        module_auc_raw_mean=float(np.mean([r["module_auc_raw"] for r in rows])),
        module_auc_normalized_mean=float(np.mean([r["module_auc_normalized"] for r in rows])),
        transmission_rho_raw_mean=float(np.mean([r["transmission_rho_raw"] for r in rows])),
        transmission_rho_normalized_mean=float(np.mean([r["transmission_rho_normalized"] for r in rows])),
        gain_hub_rho_raw_mean=mean_optional([r["gain_hub_rho_raw"] for r in rows]),
        gain_hub_rho_normalized_mean=mean_optional([r["gain_hub_rho_normalized"] for r in rows]),
    )


def run_criticality_seed(seed: int, target_radius: float) -> dict[str, float]:
    """Compare direct versus integrated response near a recurrent instability.

    A = c diag(gain) W is globally scaled to the requested spectral radius.
    The integrated response sums all recurrent paths:

        R = A + A^2 + ... = (I - A)^(-1) A.

    Dividing R by local gain cannot remove the higher-order path mixing.
    """
    w, truth, rng = make_block_system(seed=seed)
    n = w.shape[0]
    gain = np.clip(np.exp(rng.normal(0.0, 1.5, size=n)), 0.10, 8.0)

    a = gain[:, None] * w
    radius = float(np.max(np.abs(np.linalg.eigvals(a))))
    a *= target_radius / radius

    integrated = np.linalg.solve(np.eye(n) - a, a)

    direct_normalized = a / gain[:, None]
    integrated_normalized = integrated / gain[:, None]

    true_affinity = sym_strength(w)
    direct_raw_affinity = sym_strength(a)
    direct_norm_affinity = sym_strength(direct_normalized)
    integrated_raw_affinity = sym_strength(integrated)
    integrated_norm_affinity = sym_strength(integrated_normalized)

    upper = np.triu(np.ones((n, n), dtype=bool), 1)
    true_edges = true_affinity[upper]

    groups = len(np.unique(truth))
    pred_integrated_raw = spectral_partition(integrated_raw_affinity, groups, seed)
    pred_integrated_norm = spectral_partition(integrated_norm_affinity, groups, seed)

    return {
        "direct_rho_raw": float(spearmanr(true_edges, direct_raw_affinity[upper]).statistic),
        "direct_rho_normalized": float(spearmanr(true_edges, direct_norm_affinity[upper]).statistic),
        "integrated_rho_raw": float(spearmanr(true_edges, integrated_raw_affinity[upper]).statistic),
        "integrated_rho_normalized": float(spearmanr(true_edges, integrated_norm_affinity[upper]).statistic),
        "integrated_ari_raw": float(adjusted_rand_score(truth, pred_integrated_raw)),
        "integrated_ari_normalized": float(adjusted_rand_score(truth, pred_integrated_norm)),
    }


def run_criticality_case(target_radius: float, seeds: int) -> CriticalityResult:
    rows = [run_criticality_seed(seed, target_radius) for seed in range(seeds)]
    return CriticalityResult(
        spectral_radius=target_radius,
        seeds=seeds,
        direct_rho_raw_mean=float(np.mean([r["direct_rho_raw"] for r in rows])),
        direct_rho_normalized_mean=float(np.mean([r["direct_rho_normalized"] for r in rows])),
        integrated_rho_raw_mean=float(np.mean([r["integrated_rho_raw"] for r in rows])),
        integrated_rho_normalized_mean=float(np.mean([r["integrated_rho_normalized"] for r in rows])),
        integrated_ari_raw_mean=float(np.mean([r["integrated_ari_raw"] for r in rows])),
        integrated_ari_normalized_mean=float(np.mean([r["integrated_ari_normalized"] for r in rows])),
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seeds", type=int, default=50)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    susceptibility_cases = ["uniform", "heterogeneous", "extreme", "noisy_calibration"]
    susceptibility = [run_susceptibility_case(case, args.seeds) for case in susceptibility_cases]
    criticality = [
        run_criticality_case(radius, args.seeds)
        for radius in (0.70, 0.90, 0.97, 0.99)
    ]

    payload = {
        "susceptibility": [asdict(result) for result in susceptibility],
        "criticality": [asdict(result) for result in criticality],
    }

    if args.json:
        print(json.dumps(payload, indent=2))
        return

    print("SIM-03B susceptibility adversary")
    print("case                 ARI raw/norm   edge rho raw/norm   module AUC raw/norm")
    for r in susceptibility:
        print(
            f"{r.case:20s} "
            f"{r.ari_raw_mean:.3f}/{r.ari_normalized_mean:.3f}     "
            f"{r.transmission_rho_raw_mean:.3f}/{r.transmission_rho_normalized_mean:.3f}         "
            f"{r.module_auc_raw_mean:.3f}/{r.module_auc_normalized_mean:.3f}"
        )

    print("\nSIM-03B recurrent criticality adversary")
    print("radius   direct rho raw/norm   integrated rho raw/norm   integrated ARI raw/norm")
    for r in criticality:
        print(
            f"{r.spectral_radius:.2f}     "
            f"{r.direct_rho_raw_mean:.3f}/{r.direct_rho_normalized_mean:.3f}              "
            f"{r.integrated_rho_raw_mean:.3f}/{r.integrated_rho_normalized_mean:.3f}                 "
            f"{r.integrated_ari_raw_mean:.3f}/{r.integrated_ari_normalized_mean:.3f}"
        )


if __name__ == "__main__":
    main()
