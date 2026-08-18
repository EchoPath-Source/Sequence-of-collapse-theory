#!/usr/bin/env python3
"""RM-01F: matched-present / different-history memory-geometry benchmark.

Toy-model methodology only. This is not evidence for SoCT, emergent spacetime,
or a physical gravity-as-memory mechanism.

Design:
    1. Construct one present relation graph G0.
    2. Generate two past event histories containing the same multiset of source
       events in opposite temporal order.
    3. Compress those histories into persistent memory kernels M_A and M_B with
       exponential recency weighting; normalize both kernels to equal Frobenius
       norm.
    4. Reset both branches to the exact same present graph G0 with no active
       source.
    5. Evolve paired futures under:
           triadic closure,
           instantaneous-state closure,
           paired random rewiring,
           memory-weighted closure,
           node-permuted-memory null.
    6. Measure whether different hidden histories create different future
       relational geometry and whether that divergence aligns with the actual
       remembered history rather than an arbitrary hidden kernel.

Requires: numpy, networkx, scipy, pandas.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, asdict
from pathlib import Path

import networkx as nx
import numpy as np
import pandas as pd
from scipy.stats import spearmanr, ttest_1samp, ttest_rel


def transition_matrix(graph: nx.Graph, lazy: float = 0.25) -> np.ndarray:
    n = graph.number_of_nodes()
    w = nx.to_numpy_array(graph, nodelist=range(n), dtype=float)
    row_sum = w.sum(axis=1)
    p = np.divide(w, row_sum[:, None], out=np.zeros_like(w), where=row_sum[:, None] > 0.0)
    return (1.0 - lazy) * p + lazy * np.eye(n)


def source_exposure(transition: np.ndarray, source: int, *, steps: int = 2, decay: float = 0.80) -> np.ndarray:
    state = np.zeros(len(transition), dtype=float)
    state[source] = 1.0
    exposure = np.zeros_like(state)
    for t in range(steps + 1):
        exposure += (decay ** t) * state
        state = state @ transition
    return exposure


def common_neighbor_score(graph: nx.Graph) -> np.ndarray:
    n = graph.number_of_nodes()
    neighborhoods = [set(graph.neighbors(i)) for i in range(n)]
    score = np.zeros((n, n), dtype=float)
    for i in range(n):
        for j in range(i + 1, n):
            value = len(neighborhoods[i] & neighborhoods[j])
            score[i, j] = score[j, i] = float(value)
    return score


def instantaneous_kernel(graph: nx.Graph) -> np.ndarray:
    p = transition_matrix(graph)
    n = graph.number_of_nodes()
    kernel = np.zeros((n, n), dtype=float)
    for source in range(n):
        exposure = source_exposure(p, source, steps=3, decay=0.82)
        exposure /= max(float(exposure.max()), 1e-12)
        kernel += np.outer(exposure, exposure)
    kernel /= float(n)
    np.fill_diagonal(kernel, 0.0)
    return kernel


def zscore_offdiag(matrix: np.ndarray) -> np.ndarray:
    n = len(matrix)
    mask = ~np.eye(n, dtype=bool)
    values = matrix[mask]
    sd = float(values.std())
    if sd < 1e-12:
        return np.zeros_like(matrix, dtype=float)
    out = (matrix - float(values.mean())) / sd
    np.fill_diagonal(out, 0.0)
    return out


def guided_double_edge_swap(graph: nx.Graph, score: np.ndarray, rng: np.random.Generator, *, attempts: int = 80) -> bool:
    edges = list(graph.edges())
    for _ in range(attempts):
        if len(edges) < 2:
            return False
        i, j = rng.choice(len(edges), 2, replace=False)
        u, v = edges[int(i)]
        x, y = edges[int(j)]
        if len({u, v, x, y}) < 4:
            continue
        old_score = float(score[u, v] + score[x, y])
        candidates = [((u, x), (v, y)), ((u, y), (v, x))]
        if rng.random() < 0.5:
            candidates.reverse()
        best = None
        best_gain = 1e-12
        for edge1, edge2 in candidates:
            a, b = edge1
            c, d = edge2
            if a == b or c == d or graph.has_edge(a, b) or graph.has_edge(c, d):
                continue
            gain = float(score[a, b] + score[c, d] - old_score)
            if gain > best_gain:
                best = (edge1, edge2)
                best_gain = gain
        if best is None:
            continue
        graph.remove_edge(u, v)
        graph.remove_edge(x, y)
        graph.add_edge(*best[0])
        graph.add_edge(*best[1])
        if nx.is_connected(graph):
            return True
        graph.remove_edge(*best[0])
        graph.remove_edge(*best[1])
        graph.add_edge(u, v)
        graph.add_edge(x, y)
    return False


def build_reversed_histories(graph: nx.Graph, seed: int, *, group_size: int = 8, cycles: int = 20, memory_decay: float = 0.90, neutral_steps: int = 1) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed + 1000)
    n = graph.number_of_nodes()
    paths = dict(nx.all_pairs_shortest_path_length(graph))
    anchor_a = int(rng.integers(n))
    anchor_b = max(range(n), key=lambda node: paths[anchor_a][node])
    group_a = sorted(range(n), key=lambda node: paths[anchor_a][node])[:group_size]
    group_b = sorted(range(n), key=lambda node: paths[anchor_b][node])[:group_size]
    group_b = [node for node in group_b if node not in group_a]
    farthest = sorted(range(n), key=lambda node: paths[anchor_a][node], reverse=True)
    for node in farthest:
        if len(group_b) >= group_size:
            break
        if node not in group_a and node not in group_b:
            group_b.append(node)
    p = transition_matrix(graph)
    source_kernels = {}
    for source in set(group_a + group_b):
        exposure = source_exposure(p, source, steps=2, decay=0.80)
        exposure /= max(float(exposure.max()), 1e-12)
        kernel = np.outer(exposure, exposure)
        np.fill_diagonal(kernel, 0.0)
        source_kernels[source] = kernel
    seq_a = [group_a[i % len(group_a)] for i in range(cycles)] + [group_b[i % len(group_b)] for i in range(cycles)]
    seq_b = [group_b[i % len(group_b)] for i in range(cycles)] + [group_a[i % len(group_a)] for i in range(cycles)]
    def accumulate(sequence):
        memory = np.zeros((n, n), dtype=float)
        for source in sequence:
            memory = memory_decay * memory + (1.0 - memory_decay) * source_kernels[source]
        for _ in range(neutral_steps):
            memory *= memory_decay
        np.fill_diagonal(memory, 0.0)
        norm = float(np.linalg.norm(memory))
        if norm > 0.0:
            memory /= norm
        return memory
    return accumulate(seq_a), accumulate(seq_b)


def permute_kernel(memory: np.ndarray, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    permutation = rng.permutation(len(memory))
    return memory[np.ix_(permutation, permutation)]


def evolve_future(present_graph: nx.Graph, rule: str, memory: np.ndarray, seed: int, *, epochs: int = 10, swaps_per_epoch: int = 4, memory_beta: float = 2.0, memory_decay: float = 0.99) -> nx.Graph:
    graph = present_graph.copy()
    persistent = memory.copy()
    rng = np.random.default_rng(seed + 5000)
    for _ in range(epochs):
        triadic = common_neighbor_score(graph)
        instantaneous = instantaneous_kernel(graph)
        if rule == "triadic":
            score = zscore_offdiag(triadic)
        elif rule == "instantaneous":
            score = zscore_offdiag(triadic) + memory_beta * zscore_offdiag(instantaneous)
        elif rule == "memory_weighted":
            candidate_memory = persistent.copy()
            for u, v in graph.edges():
                candidate_memory[u, v] = candidate_memory[v, u] = 0.0
            score = zscore_offdiag(triadic) + memory_beta * zscore_offdiag(candidate_memory)
            persistent *= memory_decay
        elif rule == "random":
            raw = rng.random((len(graph), len(graph)))
            score = 0.5 * (raw + raw.T)
            np.fill_diagonal(score, 0.0)
        else:
            raise ValueError(rule)
        for _ in range(swaps_per_epoch):
            guided_double_edge_swap(graph, score, rng)
    return graph


def edge_jaccard_divergence(a: nx.Graph, b: nx.Graph) -> float:
    edge_a = {tuple(sorted(edge)) for edge in a.edges()}
    edge_b = {tuple(sorted(edge)) for edge in b.edges()}
    return 1.0 - len(edge_a & edge_b) / float(len(edge_a | edge_b))


def distance_matrix(graph: nx.Graph) -> np.ndarray:
    n = graph.number_of_nodes()
    out = np.zeros((n, n), dtype=float)
    for source, distances in nx.all_pairs_shortest_path_length(graph):
        for target, value in distances.items():
            out[source, target] = float(value)
    return out


def geometry_divergence(a: nx.Graph, b: nx.Graph) -> tuple[float, float]:
    da = distance_matrix(a)
    db = distance_matrix(b)
    upper = np.triu_indices(len(da), 1)
    rho = spearmanr(da[upper], db[upper]).statistic
    rho = float(rho) if np.isfinite(rho) else 1.0
    mad = float(np.mean(np.abs(da[upper] - db[upper])))
    return 1.0 - rho, mad


def history_pair_geometry_effect(future_a: nx.Graph, future_b: nx.Graph, memory_a: np.ndarray, memory_b: np.ndarray, *, quantile_fraction: float = 0.10) -> float:
    da = distance_matrix(future_a)
    db = distance_matrix(future_b)
    upper = np.triu_indices(len(da), 1)
    delta_memory = (memory_a - memory_b)[upper]
    delta_geometry = (db - da)[upper]
    count = max(1, int(quantile_fraction * len(delta_memory)))
    low = np.argsort(delta_memory)[:count]
    high = np.argsort(delta_memory)[-count:]
    return 0.5 * (float(np.mean(delta_geometry[high])) - float(np.mean(delta_geometry[low])))


@dataclass
class Trial:
    seed: int
    present_edge_match: float
    memory_norm_a: float
    memory_norm_b: float
    triadic_edge_div: float
    instantaneous_edge_div: float
    random_edge_div: float
    memory_edge_div: float
    memory_metric_div: float
    memory_metric_mad: float
    memory_history_effect: float
    shuffled_edge_div: float
    shuffled_metric_div: float
    shuffled_metric_mad: float
    shuffled_history_effect: float


def run_trial(seed: int) -> Trial:
    present = nx.random_regular_graph(4, 64, seed=seed)
    memory_a, memory_b = build_reversed_histories(present, seed)
    control = {}
    for rule in ("triadic", "instantaneous", "random"):
        future_a = evolve_future(present, rule, memory_a, seed)
        future_b = evolve_future(present, rule, memory_b, seed)
        control[rule] = edge_jaccard_divergence(future_a, future_b)
    future_a = evolve_future(present, "memory_weighted", memory_a, seed)
    future_b = evolve_future(present, "memory_weighted", memory_b, seed)
    edge_div = edge_jaccard_divergence(future_a, future_b)
    metric_div, metric_mad = geometry_divergence(future_a, future_b)
    history_effect = history_pair_geometry_effect(future_a, future_b, memory_a, memory_b)
    shuffled_a = permute_kernel(memory_a, seed + 90001)
    shuffled_b = permute_kernel(memory_b, seed + 90002)
    shuf_future_a = evolve_future(present, "memory_weighted", shuffled_a, seed)
    shuf_future_b = evolve_future(present, "memory_weighted", shuffled_b, seed)
    shuf_edge_div = edge_jaccard_divergence(shuf_future_a, shuf_future_b)
    shuf_metric_div, shuf_metric_mad = geometry_divergence(shuf_future_a, shuf_future_b)
    shuf_history_effect = history_pair_geometry_effect(shuf_future_a, shuf_future_b, memory_a, memory_b)
    return Trial(seed, 1.0, float(np.linalg.norm(memory_a)), float(np.linalg.norm(memory_b)), control["triadic"], control["instantaneous"], control["random"], edge_div, metric_div, metric_mad, history_effect, shuf_edge_div, shuf_metric_div, shuf_metric_mad, shuf_history_effect)


def summarize(frame: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for column in frame.columns:
        if column == "seed":
            continue
        values = frame[column].to_numpy(dtype=float)
        rows.append({"metric": column, "mean": float(values.mean()), "sd": float(values.std(ddof=1))})
    return pd.DataFrame(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed-start", type=int, default=300)
    parser.add_argument("--seeds", type=int, default=300)
    parser.add_argument("--out-trials", type=Path, default=Path("rm01f_trials.csv"))
    parser.add_argument("--out-summary", type=Path, default=Path("rm01f_summary.csv"))
    args = parser.parse_args()
    trials = [asdict(run_trial(seed)) for seed in range(args.seed_start, args.seed_start + args.seeds)]
    frame = pd.DataFrame(trials)
    summary = summarize(frame)
    frame.to_csv(args.out_trials, index=False)
    summary.to_csv(args.out_summary, index=False)
    history = frame["memory_history_effect"].to_numpy(dtype=float)
    shuffled = frame["shuffled_history_effect"].to_numpy(dtype=float)
    print(summary.to_string(index=False))
    print()
    print("history effect vs zero:", ttest_1samp(history, 0.0))
    print("history effect vs shuffled:", ttest_rel(history, shuffled))


if __name__ == "__main__":
    main()
