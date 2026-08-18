#!/usr/bin/env python3
"""SIM-03A: emergent object benchmark.

This is a toy-model methodology test, not evidence for SoCT.

Question:
    Can hidden dynamical modules be recovered without coordinates or supplied
    object labels, and how do intervention-based estimators compare with
    ordinary correlation under a latent common-cause confound?

Requires:
    numpy
    scikit-learn
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, asdict

import numpy as np
from sklearn.cluster import KMeans, SpectralClustering
from sklearn.metrics import adjusted_rand_score, normalized_mutual_info_score


@dataclass
class CaseResult:
    case: str
    seeds: int
    ari_intervention_mean: float
    ari_intervention_std: float
    ari_correlation_mean: float
    ari_correlation_std: float
    ari_response_profile_mean: float
    ari_response_profile_std: float
    nmi_intervention_mean: float
    nmi_correlation_mean: float
    nmi_response_profile_mean: float


def make_block_system(
    n: int = 12,
    groups: int = 3,
    within: float = 0.55,
    between: float = 0.03,
    seed: int = 0,
) -> tuple[np.ndarray, np.ndarray]:
    """Construct a stable linear-nonlinear modular dynamical system.

    Node ordering is randomly permuted so no geometric/index prior reveals the
    withheld module labels.
    """
    rng = np.random.default_rng(seed)
    group_size = n // groups
    labels = np.repeat(np.arange(groups), group_size)
    if labels.size < n:
        labels = np.concatenate([labels, np.arange(n - labels.size)])

    w = rng.normal(0.0, 0.01, size=(n, n))
    for target in range(n):
        for source in range(n):
            if target == source:
                w[target, source] = 0.15
            elif labels[target] == labels[source]:
                w[target, source] += within / group_size
            else:
                w[target, source] += between / n

    spectral_radius = float(np.max(np.abs(np.linalg.eigvals(w))))
    w *= 0.88 / spectral_radius

    permutation = rng.permutation(n)
    w = w[np.ix_(permutation, permutation)]
    labels = labels[permutation]
    return w, labels


def simulate_natural_dynamics(
    w: np.ndarray,
    steps: int = 12_000,
    noise: float = 0.12,
    seed: int = 0,
) -> np.ndarray:
    rng = np.random.default_rng(seed)
    n = w.shape[0]
    x = np.zeros((steps + 1, n), dtype=float)
    x[0] = rng.normal(0.0, 0.2, size=n)
    for t in range(steps):
        x[t + 1] = np.tanh(w @ x[t] + rng.normal(0.0, noise, size=n))
    return x


def estimate_intervention_matrix(
    w: np.ndarray,
    amplitude: float = 0.5,
    trials: int = 4_000,
    noise: float = 0.08,
    seed: int = 0,
) -> np.ndarray:
    """Estimate one-step causal response by symmetric +/- interventions.

    K[target, source] approximates the mean signed next-step response of target
    to source after cancellation of matched additive noise.
    """
    rng = np.random.default_rng(seed)
    n = w.shape[0]
    k = np.zeros((n, n), dtype=float)

    for source in range(n):
        epsilon = rng.normal(0.0, noise, size=(trials, n))
        plus = np.tanh(amplitude * w[:, source][None, :] + epsilon)
        minus = np.tanh(-amplitude * w[:, source][None, :] + epsilon)
        k[:, source] = np.mean(plus - minus, axis=0) / (2.0 * amplitude)
    return k


def spectral_partition(affinity: np.ndarray, groups: int, seed: int) -> np.ndarray:
    a = np.maximum((affinity + affinity.T) / 2.0, 0.0)
    np.fill_diagonal(a, max(float(np.max(a)), 1e-6))
    return SpectralClustering(
        n_clusters=groups,
        affinity="precomputed",
        assign_labels="kmeans",
        random_state=seed,
    ).fit_predict(a)


def add_latent_common_cause(x: np.ndarray, seed: int) -> np.ndarray:
    """Add two strong unrelated latent drivers partitioned by observed index.

    This creates a correlation structure unrelated to the true dynamical
    modules while leaving the intervention matrix unchanged.
    """
    rng = np.random.default_rng(seed)
    t = x.shape[0]
    driver_a = rng.normal(0.0, 0.8, size=t)
    driver_b = rng.normal(0.0, 0.8, size=t)
    wrong_partition = np.arange(x.shape[1]) % 2
    confound = np.where(wrong_partition[None, :] == 0, driver_a[:, None], driver_b[:, None])
    return 0.25 * x + confound


def run_seed(seed: int, case: str) -> tuple[np.ndarray, np.ndarray]:
    if case == "clean_modular":
        within, between = 0.55, 0.03
    elif case == "weak_separation":
        within, between = 0.34, 0.18
    elif case == "latent_common_cause":
        within, between = 0.55, 0.03
    else:
        raise ValueError(f"unknown case: {case}")

    w, truth = make_block_system(within=within, between=between, seed=seed)
    x = simulate_natural_dynamics(w, seed=seed + 10)
    if case == "latent_common_cause":
        x = add_latent_common_cause(x, seed=seed + 99)

    k = estimate_intervention_matrix(w, seed=seed + 20)
    groups = len(np.unique(truth))

    intervention_affinity = np.abs(k) + np.abs(k.T)
    pred_intervention = spectral_partition(intervention_affinity, groups, seed)

    correlation_affinity = np.abs(np.corrcoef(x[1_000:].T))
    pred_correlation = spectral_partition(correlation_affinity, groups, seed)

    response_features = np.concatenate([k, k.T], axis=1)
    pred_response = KMeans(n_clusters=groups, n_init=50, random_state=seed).fit_predict(
        response_features
    )

    predictions = (pred_intervention, pred_correlation, pred_response)
    ari = np.asarray([adjusted_rand_score(truth, pred) for pred in predictions])
    nmi = np.asarray([normalized_mutual_info_score(truth, pred) for pred in predictions])
    return ari, nmi


def run_case(case: str, seeds: int) -> CaseResult:
    ari_rows = []
    nmi_rows = []
    for seed in range(seeds):
        ari, nmi = run_seed(seed, case)
        ari_rows.append(ari)
        nmi_rows.append(nmi)

    ari_arr = np.asarray(ari_rows)
    nmi_arr = np.asarray(nmi_rows)
    return CaseResult(
        case=case,
        seeds=seeds,
        ari_intervention_mean=float(ari_arr[:, 0].mean()),
        ari_intervention_std=float(ari_arr[:, 0].std()),
        ari_correlation_mean=float(ari_arr[:, 1].mean()),
        ari_correlation_std=float(ari_arr[:, 1].std()),
        ari_response_profile_mean=float(ari_arr[:, 2].mean()),
        ari_response_profile_std=float(ari_arr[:, 2].std()),
        nmi_intervention_mean=float(nmi_arr[:, 0].mean()),
        nmi_correlation_mean=float(nmi_arr[:, 1].mean()),
        nmi_response_profile_mean=float(nmi_arr[:, 2].mean()),
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seeds", type=int, default=20)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    cases = ["clean_modular", "weak_separation", "latent_common_cause"]
    results = [run_case(case, args.seeds) for case in cases]

    if args.json:
        print(json.dumps([asdict(result) for result in results], indent=2))
        return

    print("SIM-03A emergent object benchmark")
    print("method order: intervention | correlation | response-profile")
    for result in results:
        print(
            f"{result.case:20s} ARI "
            f"{result.ari_intervention_mean:.3f} | "
            f"{result.ari_correlation_mean:.3f} | "
            f"{result.ari_response_profile_mean:.3f}"
        )


if __name__ == "__main__":
    main()
