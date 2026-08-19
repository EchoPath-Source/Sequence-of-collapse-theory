#!/usr/bin/env python3
"""RM-01G: local-action memory/geometry benchmark.

Toy-model methodology only. This is not evidence for SoCT, spacetime emergence,
or physical gravity.

This module reuses the matched-present history construction and geometry
statistics from RM-01F, but replaces its hand-designed memory-weighted closure
score with a single scalar action

    S[G,K] = -alpha*N_triangle(G) - beta*sum_{(i,j) in E} Khat_ij

under fixed-degree, fixed-edge-count, connected graph constraints.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
from pathlib import Path

import networkx as nx
import numpy as np
import pandas as pd
from scipy.stats import spearmanr, ttest_1samp, ttest_rel

from rm01f_matched_present_history_geometry import (
    build_reversed_histories,
    edge_jaccard_divergence,
    geometry_divergence,
    history_pair_geometry_effect,
    instantaneous_kernel,
    permute_kernel,
    zscore_offdiag,
)

NODES = 64
DEGREE = 4
ALPHA = 1.0
BETA = 0.10
EPOCHS = 10
SWAPS_PER_EPOCH = 4


def common_neighbors(graph: nx.Graph, u: int, v: int) -> int:
    return len(set(graph[u]) & set(graph[v]))


def action_value(
    graph: nx.Graph,
    kernel_z: np.ndarray,
    *,
    alpha: float = ALPHA,
    beta: float = BETA,
) -> float:
    triangles = sum(nx.triangles(graph).values()) / 3.0
    memory_alignment = sum(
        float(kernel_z[u, v]) for u, v in graph.edges()
    )
    return -alpha * triangles - beta * memory_alignment


def proposed_gain(
    graph: nx.Graph,
    kernel_z: np.ndarray,
    removed_1: tuple[int, int],
    removed_2: tuple[int, int],
    added_1: tuple[int, int],
    added_2: tuple[int, int],
    *,
    alpha: float,
    beta: float,
) -> float:
    """Return -Delta S; positive means the proposal lowers the action."""
    u, v = removed_1
    x, y = removed_2
    a, b = added_1
    c, d = added_2

    old_tri = common_neighbors(graph, u, v) + common_neighbors(graph, x, y)
    old_mem = float(kernel_z[u, v] + kernel_z[x, y])

    graph.remove_edge(u, v)
    graph.remove_edge(x, y)
    if a == b or c == d or graph.has_edge(a, b) or graph.has_edge(c, d):
        graph.add_edge(u, v)
        graph.add_edge(x, y)
        return -np.inf

    graph.add_edge(a, b)
    graph.add_edge(c, d)
    if not nx.is_connected(graph):
        graph.remove_edge(a, b)
        graph.remove_edge(c, d)
        graph.add_edge(u, v)
        graph.add_edge(x, y)
        return -np.inf

    new_tri = common_neighbors(graph, a, b) + common_neighbors(graph, c, d)
    new_mem = float(kernel_z[a, b] + kernel_z[c, d])

    graph.remove_edge(a, b)
    graph.remove_edge(c, d)
    graph.add_edge(u, v)
    graph.add_edge(x, y)

    return alpha * (new_tri - old_tri) + beta * (new_mem - old_mem)


def action_lowering_swap(
    graph: nx.Graph,
    kernel_z: np.ndarray,
    rng: np.random.Generator,
    *,
    alpha: float,
    beta: float,
    attempts: int = 80,
) -> float:
    edges = list(graph.edges())
    for _ in range(attempts):
        i, j = rng.choice(len(edges), 2, replace=False)
        u, v = edges[int(i)]
        x, y = edges[int(j)]
        if len({u, v, x, y}) < 4:
            continue

        candidates = [((u, x), (v, y)), ((u, y), (v, x))]
        if rng.random() < 0.5:
            candidates.reverse()

        best = None
        best_gain = 1e-12
        for edge_1, edge_2 in candidates:
            gain = proposed_gain(
                graph,
                kernel_z,
                (u, v),
                (x, y),
                edge_1,
                edge_2,
                alpha=alpha,
                beta=beta,
            )
            if gain > best_gain:
                best = (edge_1, edge_2)
                best_gain = gain

        if best is not None:
            graph.remove_edge(u, v)
            graph.remove_edge(x, y)
            graph.add_edge(*best[0])
            graph.add_edge(*best[1])
            return float(best_gain)

    return 0.0


def evolve_action(
    present: nx.Graph,
    memory: np.ndarray,
    seed: int,
    *,
    mode: str,
    alpha: float = ALPHA,
    beta: float = BETA,
) -> tuple[nx.Graph, float]:
    graph = present.copy()
    rng = np.random.default_rng(seed + 7000)
    accepted_gain = 0.0

    if mode == "memory":
        fixed_kernel = zscore_offdiag(memory)
    elif mode == "scalar":
        fixed_kernel = np.ones_like(memory)
        np.fill_diagonal(fixed_kernel, 0.0)
    else:
        fixed_kernel = np.zeros_like(memory)

    for _ in range(EPOCHS):
        if mode == "memory":
            kernel_z, local_beta = fixed_kernel, beta
        elif mode == "triadic":
            kernel_z, local_beta = fixed_kernel, 0.0
        elif mode == "scalar":
            kernel_z, local_beta = fixed_kernel, beta
        elif mode == "instantaneous":
            kernel_z = zscore_offdiag(instantaneous_kernel(graph))
            local_beta = beta
        elif mode == "random":
            raw = rng.normal(size=memory.shape)
            kernel_z = 0.5 * (raw + raw.T)
            np.fill_diagonal(kernel_z, 0.0)
            local_beta = beta
        else:
            raise ValueError(mode)

        for _ in range(SWAPS_PER_EPOCH):
            accepted_gain += action_lowering_swap(
                graph,
                kernel_z,
                rng,
                alpha=alpha,
                beta=local_beta,
            )

    return graph, accepted_gain


def forman_style_node_curvature(graph: nx.Graph) -> np.ndarray:
    values = [[] for _ in range(graph.number_of_nodes())]
    for u, v in graph.edges():
        shared = common_neighbors(graph, u, v)
        value = 4.0 - graph.degree(u) - graph.degree(v) + 3.0 * shared
        values[u].append(value)
        values[v].append(value)
    return np.asarray(
        [float(np.mean(row)) if row else 0.0 for row in values],
        dtype=float,
    )


def curvature_alignment(
    future_a: nx.Graph,
    future_b: nx.Graph,
    memory_a: np.ndarray,
    memory_b: np.ndarray,
) -> float:
    curvature_a = forman_style_node_curvature(future_a)
    curvature_b = forman_style_node_curvature(future_b)
    memory_contrast = (memory_a - memory_b).sum(axis=1)
    curvature_contrast = curvature_a - curvature_b
    rho = spearmanr(memory_contrast, curvature_contrast).statistic
    return float(rho) if np.isfinite(rho) else 0.0


@dataclass
class Trial:
    seed: int
    triadic_edge_div: float
    instantaneous_edge_div: float
    scalar_memory_edge_div: float
    random_edge_div: float
    memory_edge_div: float
    memory_metric_div: float
    memory_metric_mad: float
    memory_history_effect: float
    memory_curvature_alignment: float
    memory_action_gain_a: float
    memory_action_gain_b: float
    permuted_edge_div: float
    permuted_metric_div: float
    permuted_metric_mad: float
    permuted_history_effect: float
    permuted_curvature_alignment: float


def run_trial(seed: int) -> Trial:
    present = nx.random_regular_graph(DEGREE, NODES, seed=seed)
    memory_a, memory_b = build_reversed_histories(present, seed)

    control = {}
    for mode in ("triadic", "instantaneous", "scalar", "random"):
        future_a, _ = evolve_action(present, memory_a, seed, mode=mode)
        future_b, _ = evolve_action(present, memory_b, seed, mode=mode)
        control[mode] = edge_jaccard_divergence(future_a, future_b)

    future_a, gain_a = evolve_action(present, memory_a, seed, mode="memory")
    future_b, gain_b = evolve_action(present, memory_b, seed, mode="memory")
    edge_div = edge_jaccard_divergence(future_a, future_b)
    metric_div, metric_mad = geometry_divergence(future_a, future_b)
    history_effect = history_pair_geometry_effect(
        future_a, future_b, memory_a, memory_b
    )
    curvature = curvature_alignment(future_a, future_b, memory_a, memory_b)

    permuted_a = permute_kernel(memory_a, seed + 91001)
    permuted_b = permute_kernel(memory_b, seed + 91002)
    null_a, _ = evolve_action(present, permuted_a, seed, mode="memory")
    null_b, _ = evolve_action(present, permuted_b, seed, mode="memory")
    null_edge = edge_jaccard_divergence(null_a, null_b)
    null_metric, null_mad = geometry_divergence(null_a, null_b)
    null_history = history_pair_geometry_effect(
        null_a, null_b, memory_a, memory_b
    )
    null_curvature = curvature_alignment(
        null_a, null_b, memory_a, memory_b
    )

    return Trial(
        seed,
        control["triadic"],
        control["instantaneous"],
        control["scalar"],
        control["random"],
        edge_div,
        metric_div,
        metric_mad,
        history_effect,
        curvature,
        gain_a,
        gain_b,
        null_edge,
        null_metric,
        null_mad,
        null_history,
        null_curvature,
    )


def summarize(frame: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for column in frame.columns:
        if column == "seed":
            continue
        values = frame[column].to_numpy(dtype=float)
        sd = float(values.std(ddof=1))
        rows.append(
            {
                "metric": column,
                "mean": float(values.mean()),
                "sd": sd,
                "sem": sd / np.sqrt(len(values)),
            }
        )
    return pd.DataFrame(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed-start", type=int, default=2000)
    parser.add_argument("--seeds", type=int, default=300)
    parser.add_argument("--out-trials", type=Path, default=Path("rm01g_trials.csv"))
    parser.add_argument("--out-summary", type=Path, default=Path("rm01g_summary.csv"))
    args = parser.parse_args()

    frame = pd.DataFrame(
        [
            asdict(run_trial(seed))
            for seed in range(args.seed_start, args.seed_start + args.seeds)
        ]
    )
    summary = summarize(frame)
    frame.to_csv(args.out_trials, index=False)
    summary.to_csv(args.out_summary, index=False)

    history = frame["memory_history_effect"].to_numpy(dtype=float)
    null_history = frame["permuted_history_effect"].to_numpy(dtype=float)
    curvature = frame["memory_curvature_alignment"].to_numpy(dtype=float)
    null_curvature = frame["permuted_curvature_alignment"].to_numpy(dtype=float)

    print(summary.to_string(index=False))
    print("H_geo vs zero:", ttest_1samp(history, 0.0))
    print("H_geo vs permuted:", ttest_rel(history, null_history))
    print("curvature vs zero:", ttest_1samp(curvature, 0.0))
    print("curvature vs permuted:", ttest_rel(curvature, null_curvature))


if __name__ == "__main__":
    main()
