#!/usr/bin/env python3
"""RM-01H: transferability gate for the RM-01G memory/geometry action.

Toy-model methodology only. This is not evidence for SoCT, spacetime emergence,
or physical gravity.

RM-01H asks whether the finite-network action used in RM-01G supports a
transferable coarse-grained response law when system size, degree, memory
persistence, and present-network topology are changed without retuning.

The primary action remains

    S[G,K] = -alpha*N_triangle(G) - beta*sum_(i,j in E) Khat_ij

The transfer study adds two intensive/extensive normalizations after a first
naive size-transfer failure:

1. history event count scales with source-group size;
2. attempted accepted-improvement updates scale with edge count.

It also defines a dimensionless proposal-level coupling

    lambda_eff = beta * sigma(Delta K) / (alpha * sigma(Delta N_triangle))

and fits one threshold response law on training systems only:

    R_geo = H_geo / <d> = A * max(0, lambda_eff - lambda_c).

The fitted A and lambda_c are then frozen before unseen-size and topology
holdouts.

Requires: numpy, pandas, networkx, scipy, scikit-learn.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
from pathlib import Path

import networkx as nx
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from scipy.stats import ttest_1samp
from sklearn.metrics import mean_absolute_error, r2_score, roc_auc_score

from rm01f_matched_present_history_geometry import (
    build_reversed_histories,
    history_pair_geometry_effect,
    zscore_offdiag,
)
from rm01g_local_action_memory_geometry import (
    action_lowering_swap,
    proposed_gain,
)

ALPHA = 1.0
EPOCHS = 10
BASELINE_EDGES = 128.0      # n=64, degree=4
BASELINE_SWAPS_PER_EPOCH = 4.0
BASELINE_GROUP_SIZE = 8.0
BASELINE_CYCLES = 20.0

TRAIN_SIZES = (48, 64)
TRAIN_DEGREES = (4, 6)
TRAIN_MEMORY_DECAYS = (0.85, 0.90)
BETAS = (0.05, 0.10, 0.15)
SIZE_HOLDOUT_SIZES = (80, 96)
SIZE_HOLDOUT_MEMORY_DECAY = 0.95
TOPOLOGY_HOLDOUTS = ("regular", "smallworld", "ring")


@dataclass
class Trial:
    stage: str
    family: str
    n: int
    degree: int
    memory_decay: float
    beta: float
    seed: int
    history_effect: float
    mean_present_distance: float
    normalized_response: float
    lambda_eff: float
    sigma_triangle: float
    sigma_memory: float
    swaps_per_epoch: int
    edge_contrast: float
    edge_auc: float


def make_present(family: str, n: int, degree: int, seed: int) -> nx.Graph:
    if family == "regular":
        return nx.random_regular_graph(degree, n, seed=seed)

    k = degree if degree % 2 == 0 else degree + 1
    if family == "smallworld":
        return nx.watts_strogatz_graph(n, k, 0.15, seed=seed)
    if family == "ring":
        return nx.watts_strogatz_graph(n, k, 0.0, seed=seed)
    raise ValueError(f"unknown family: {family}")


def scaled_histories(
    graph: nx.Graph,
    seed: int,
    *,
    memory_decay: float,
) -> tuple[np.ndarray, np.ndarray]:
    """Keep source-history exposure per group member approximately intensive."""
    group_size = max(4, graph.number_of_nodes() // 8)
    cycles = max(
        4,
        int(round(BASELINE_CYCLES * group_size / BASELINE_GROUP_SIZE)),
    )
    return build_reversed_histories(
        graph,
        seed,
        group_size=group_size,
        cycles=cycles,
        memory_decay=memory_decay,
    )


def swaps_per_epoch(graph: nx.Graph) -> int:
    """Keep update attempts per edge near the RM-01G baseline."""
    return max(
        1,
        int(
            round(
                BASELINE_SWAPS_PER_EPOCH
                * graph.number_of_edges()
                / BASELINE_EDGES
            )
        ),
    )


def evolve_scaled_action(
    present: nx.Graph,
    memory: np.ndarray,
    seed: int,
    *,
    beta: float,
) -> nx.Graph:
    graph = present.copy()
    kernel_z = zscore_offdiag(memory)
    rng = np.random.default_rng(seed + 7000)
    local_swaps = swaps_per_epoch(graph)

    for _ in range(EPOCHS):
        for _ in range(local_swaps):
            action_lowering_swap(
                graph,
                kernel_z,
                rng,
                alpha=ALPHA,
                beta=beta,
            )
    return graph


def distance_matrix(graph: nx.Graph) -> np.ndarray:
    n = graph.number_of_nodes()
    out = np.zeros((n, n), dtype=float)
    for source, distances in nx.all_pairs_shortest_path_length(graph):
        for target, value in distances.items():
            out[source, target] = float(value)
    return out


def mean_present_distance(graph: nx.Graph) -> float:
    d = distance_matrix(graph)
    upper = np.triu_indices(len(d), 1)
    return float(np.mean(d[upper]))


def proposal_scales(
    graph: nx.Graph,
    memory: np.ndarray,
    seed: int,
    *,
    samples: int,
) -> tuple[float, float]:
    """Estimate proposal-level leverage of closure and memory action terms."""
    kernel_z = zscore_offdiag(memory)
    rng = np.random.default_rng(seed + 88_000)
    edges = list(graph.edges())
    triangle_delta: list[float] = []
    memory_delta: list[float] = []
    attempts = 0

    while len(triangle_delta) < samples and attempts < 20 * samples:
        attempts += 1
        i, j = rng.choice(len(edges), 2, replace=False)
        u, v = edges[int(i)]
        x, y = edges[int(j)]
        if len({u, v, x, y}) < 4:
            continue

        candidates = [((u, x), (v, y)), ((u, y), (v, x))]
        edge_1, edge_2 = candidates[int(rng.integers(2))]

        delta_t = proposed_gain(
            graph,
            kernel_z,
            (u, v),
            (x, y),
            edge_1,
            edge_2,
            alpha=1.0,
            beta=0.0,
        )
        if not np.isfinite(delta_t):
            continue

        delta_m = proposed_gain(
            graph,
            kernel_z,
            (u, v),
            (x, y),
            edge_1,
            edge_2,
            alpha=0.0,
            beta=1.0,
        )
        if not np.isfinite(delta_m):
            continue

        triangle_delta.append(float(delta_t))
        memory_delta.append(float(delta_m))

    if len(triangle_delta) < 2:
        return 0.0, 0.0
    return (
        float(np.std(triangle_delta)),
        float(np.std(memory_delta)),
    )


def local_extreme_response(
    future_a: nx.Graph,
    future_b: nx.Graph,
    memory_a: np.ndarray,
    memory_b: np.ndarray,
    *,
    fraction: float = 0.10,
) -> tuple[float, float]:
    """Local edge-response diagnostic used only as a topology-transfer check."""
    n = future_a.number_of_nodes()
    delta_memory = zscore_offdiag(memory_a) - zscore_offdiag(memory_b)
    adjacency_a = nx.to_numpy_array(future_a, nodelist=range(n), dtype=float)
    adjacency_b = nx.to_numpy_array(future_b, nodelist=range(n), dtype=float)

    upper = np.triu_indices(n, 1)
    x = delta_memory[upper]
    y = (adjacency_a - adjacency_b)[upper]
    count = max(1, int(fraction * len(x)))
    order = np.argsort(x)
    chosen = np.concatenate([order[:count], order[-count:]])
    y_extreme = y[chosen]
    x_extreme = x[chosen]

    contrast = 0.5 * (
        float(np.mean(y_extreme[count:]))
        - float(np.mean(y_extreme[:count]))
    )

    mask = y_extreme != 0.0
    auc = float("nan")
    if np.sum(mask) > 2 and len(np.unique(y_extreme[mask])) == 2:
        auc = float(
            roc_auc_score(
                (y_extreme[mask] > 0.0).astype(int),
                x_extreme[mask],
            )
        )
    return contrast, auc


def run_trial(
    *,
    stage: str,
    family: str,
    n: int,
    degree: int,
    memory_decay: float,
    beta: float,
    seed: int,
    proposal_samples: int,
) -> Trial:
    present = make_present(family, n, degree, seed)
    memory_a, memory_b = scaled_histories(
        present,
        seed,
        memory_decay=memory_decay,
    )

    tri_a, mem_a = proposal_scales(
        present,
        memory_a,
        seed,
        samples=proposal_samples,
    )
    tri_b, mem_b = proposal_scales(
        present,
        memory_b,
        seed + 1,
        samples=proposal_samples,
    )
    sigma_triangle = float(np.mean([tri_a, tri_b]))
    sigma_memory = float(np.mean([mem_a, mem_b]))
    lambda_eff = (
        beta * sigma_memory / max(ALPHA * sigma_triangle, 1e-12)
    )

    future_a = evolve_scaled_action(present, memory_a, seed, beta=beta)
    future_b = evolve_scaled_action(present, memory_b, seed, beta=beta)
    history_effect = history_pair_geometry_effect(
        future_a,
        future_b,
        memory_a,
        memory_b,
    )
    mean_distance = mean_present_distance(present)
    normalized = history_effect / max(mean_distance, 1e-12)
    edge_contrast, edge_auc = local_extreme_response(
        future_a,
        future_b,
        memory_a,
        memory_b,
    )

    return Trial(
        stage=stage,
        family=family,
        n=n,
        degree=degree,
        memory_decay=memory_decay,
        beta=beta,
        seed=seed,
        history_effect=float(history_effect),
        mean_present_distance=mean_distance,
        normalized_response=float(normalized),
        lambda_eff=float(lambda_eff),
        sigma_triangle=sigma_triangle,
        sigma_memory=sigma_memory,
        swaps_per_epoch=swaps_per_epoch(present),
        edge_contrast=float(edge_contrast),
        edge_auc=float(edge_auc),
    )


def threshold_response(
    x: np.ndarray,
    amplitude: float,
    threshold: float,
) -> np.ndarray:
    return amplitude * np.maximum(0.0, x - threshold)


def aggregate_configs(frame: pd.DataFrame) -> pd.DataFrame:
    keys = ["stage", "family", "n", "degree", "memory_decay", "beta"]
    return (
        frame.groupby(keys, as_index=False)
        .agg(
            history_effect=("history_effect", "mean"),
            normalized_response=("normalized_response", "mean"),
            lambda_eff=("lambda_eff", "mean"),
            mean_present_distance=("mean_present_distance", "mean"),
            edge_contrast=("edge_contrast", "mean"),
            edge_auc=("edge_auc", "mean"),
        )
    )


def run_training(seeds: int, proposal_samples: int) -> pd.DataFrame:
    rows: list[dict] = []
    config = 0
    for n in TRAIN_SIZES:
        for degree in TRAIN_DEGREES:
            for memory_decay in TRAIN_MEMORY_DECAYS:
                for beta in BETAS:
                    for offset in range(seeds):
                        seed = 90_000 + 20 * config + offset
                        rows.append(
                            asdict(
                                run_trial(
                                    stage="train",
                                    family="regular",
                                    n=n,
                                    degree=degree,
                                    memory_decay=memory_decay,
                                    beta=beta,
                                    seed=seed,
                                    proposal_samples=proposal_samples,
                                )
                            )
                        )
                    config += 1
    return pd.DataFrame(rows)


def run_size_holdout(seeds: int, proposal_samples: int) -> pd.DataFrame:
    rows: list[dict] = []
    config = 0
    for n in SIZE_HOLDOUT_SIZES:
        for degree in TRAIN_DEGREES:
            for beta in BETAS:
                for offset in range(seeds):
                    seed = 100_000 + 30 * config + offset
                    rows.append(
                        asdict(
                            run_trial(
                                stage="size_holdout",
                                family="regular",
                                n=n,
                                degree=degree,
                                memory_decay=SIZE_HOLDOUT_MEMORY_DECAY,
                                beta=beta,
                                seed=seed,
                                proposal_samples=proposal_samples,
                            )
                        )
                    )
                config += 1
    return pd.DataFrame(rows)


def run_topology_holdout(seeds: int, proposal_samples: int) -> pd.DataFrame:
    rows: list[dict] = []
    for family_index, family in enumerate(TOPOLOGY_HOLDOUTS):
        for offset in range(seeds):
            seed = 160_000 + 100 * family_index + offset
            rows.append(
                asdict(
                    run_trial(
                        stage="topology_holdout",
                        family=family,
                        n=64,
                        degree=4,
                        memory_decay=0.90,
                        beta=0.10,
                        seed=seed,
                        proposal_samples=proposal_samples,
                    )
                )
            )
    return pd.DataFrame(rows)


def fit_training_law(training: pd.DataFrame) -> tuple[float, float, float, float]:
    config = aggregate_configs(training)
    x = config["lambda_eff"].to_numpy(dtype=float)
    y = config["normalized_response"].to_numpy(dtype=float)
    params, _ = curve_fit(
        threshold_response,
        x,
        y,
        p0=(0.15, 0.20),
        bounds=((0.0, 0.0), (5.0, 2.0)),
        maxfev=20_000,
    )
    prediction = threshold_response(x, *params)
    return (
        float(params[0]),
        float(params[1]),
        float(r2_score(y, prediction)),
        float(mean_absolute_error(y, prediction)),
    )


def evaluate_size_holdout(
    holdout: pd.DataFrame,
    *,
    amplitude: float,
    threshold: float,
) -> tuple[float, float]:
    config = aggregate_configs(holdout)
    x = config["lambda_eff"].to_numpy(dtype=float)
    y = config["normalized_response"].to_numpy(dtype=float)
    prediction = threshold_response(x, amplitude, threshold)
    return (
        float(r2_score(y, prediction)),
        float(mean_absolute_error(y, prediction)),
    )


def topology_summary(frame: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for family, group in frame.groupby("family"):
        h = group["history_effect"].to_numpy(dtype=float)
        c = group["edge_contrast"].to_numpy(dtype=float)
        auc = group["edge_auc"].dropna().to_numpy(dtype=float)
        h_test = ttest_1samp(h, 0.0) if np.std(h) > 0.0 else None
        c_test = ttest_1samp(c, 0.0) if np.std(c) > 0.0 else None
        rows.append(
            {
                "family": family,
                "seeds": len(group),
                "history_effect_mean": float(np.mean(h)),
                "history_effect_sd": float(np.std(h, ddof=1)),
                "history_effect_p": (
                    float(h_test.pvalue) if h_test is not None else float("nan")
                ),
                "edge_contrast_mean": float(np.mean(c)),
                "edge_contrast_sd": float(np.std(c, ddof=1)),
                "edge_contrast_p": (
                    float(c_test.pvalue) if c_test is not None else float("nan")
                ),
                "edge_auc_mean": (
                    float(np.mean(auc)) if len(auc) else float("nan")
                ),
            }
        )
    return pd.DataFrame(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--train-seeds", type=int, default=8)
    parser.add_argument("--size-seeds", type=int, default=10)
    parser.add_argument("--topology-seeds", type=int, default=15)
    parser.add_argument("--proposal-samples", type=int, default=40)
    parser.add_argument("--out-dir", type=Path, default=Path("."))
    args = parser.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    training = run_training(args.train_seeds, args.proposal_samples)
    size_holdout = run_size_holdout(args.size_seeds, args.proposal_samples)
    topology = run_topology_holdout(args.topology_seeds, args.proposal_samples)

    amplitude, threshold, train_r2, train_mae = fit_training_law(training)
    size_r2, size_mae = evaluate_size_holdout(
        size_holdout,
        amplitude=amplitude,
        threshold=threshold,
    )
    topo = topology_summary(topology)

    training.to_csv(args.out_dir / "rm01h_training_trials.csv", index=False)
    size_holdout.to_csv(args.out_dir / "rm01h_size_holdout_trials.csv", index=False)
    topology.to_csv(args.out_dir / "rm01h_topology_holdout_trials.csv", index=False)
    topo.to_csv(args.out_dir / "rm01h_topology_summary.csv", index=False)

    summary = pd.DataFrame(
        [
            {
                "stage": "training_threshold_law",
                "amplitude": amplitude,
                "threshold": threshold,
                "r2": train_r2,
                "mae": train_mae,
            },
            {
                "stage": "unseen_size_holdout",
                "amplitude": amplitude,
                "threshold": threshold,
                "r2": size_r2,
                "mae": size_mae,
            },
        ]
    )
    summary.to_csv(args.out_dir / "rm01h_transfer_summary.csv", index=False)

    print(summary.to_string(index=False))
    print()
    print(topo.to_string(index=False))


if __name__ == "__main__":
    main()
