#!/usr/bin/env python3
"""SIM-04C: compare candidate causal-distance constructions.

Toy-model methodology benchmark only. This is not evidence for SoCT or for
emergent spacetime.

The benchmark separates two targets:

1. background embedding geometry: Euclidean distance between hidden coordinates;
2. effective causal/path geometry: shortest path through the actual causal
   transmission network using hidden edge transit cost.

Candidate estimators:
    D1 = shortest path on inverse calibrated transmission/capacity
    D2 = shortest path on -log calibrated transmission
    D3 = shortest path on calibrated propagation delay
    D4 = unweighted hop-count path distance
    D5 = learned combination of D1-D4 trained only on chain + grid families
         and tested on withheld families.

Requires:
    numpy
    scipy
    networkx
    scikit-learn
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass

import networkx as nx
import numpy as np
from scipy.stats import spearmanr
from sklearn.linear_model import Ridge
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


TRAIN_FAMILIES = ("chain", "grid")
TEST_FAMILIES = (
    "chain",
    "grid",
    "irregular",
    "bottleneck",
    "shortcut",
    "variable_speed",
)


@dataclass
class FamilySummary:
    family: str
    seeds: int
    d1_effective_rho: float
    d2_effective_rho: float
    d3_effective_rho: float
    d4_effective_rho: float
    d5_effective_rho: float
    d1_background_rho: float
    d2_background_rho: float
    d3_background_rho: float
    d4_background_rho: float
    d5_background_rho: float


def safe_spearman(a: np.ndarray, b: np.ndarray) -> float:
    value = spearmanr(a, b).statistic
    return float(value) if np.isfinite(value) else 0.0


def ensure_connected_knn(coords: np.ndarray, k: int = 4) -> nx.Graph:
    n = len(coords)
    distance = np.linalg.norm(coords[:, None, :] - coords[None, :, :], axis=2)
    graph = nx.Graph()
    graph.add_nodes_from(range(n))

    for i in range(n):
        for j in np.argsort(distance[i])[1 : k + 1]:
            graph.add_edge(i, int(j))

    while not nx.is_connected(graph):
        components = [list(c) for c in nx.connected_components(graph)]
        first = components[0]
        rest = [node for comp in components[1:] for node in comp]
        _, u, v = min(
            (distance[i, j], i, j) for i in first for j in rest
        )
        graph.add_edge(u, v)

    return graph


def make_family(family: str, seed: int) -> tuple[nx.Graph, np.ndarray]:
    rng = np.random.default_rng(seed)

    if family == "chain":
        n = 30
        coords = np.column_stack([np.arange(n, dtype=float), np.zeros(n)])
        graph = nx.path_graph(n)

    elif family == "grid":
        side = 6
        coords = np.asarray(
            [(i, j) for i in range(side) for j in range(side)], dtype=float
        )
        graph_2d = nx.grid_2d_graph(side, side)
        mapping = {node: idx for idx, node in enumerate(graph_2d.nodes())}
        graph = nx.relabel_nodes(graph_2d, mapping)

    elif family == "irregular":
        n = 36
        coords = rng.uniform(0.0, 6.0, size=(n, 2))
        graph = ensure_connected_knn(coords, k=4)

    elif family == "bottleneck":
        side = 4
        left = np.asarray(
            [(i, j) for i in range(side) for j in range(side)], dtype=float
        )
        right = np.asarray(
            [(i + 6, j) for i in range(side) for j in range(side)], dtype=float
        )
        coords = np.vstack([left, right])
        graph = nx.Graph()

        for offset in (0, side * side):
            for i in range(side):
                for j in range(side):
                    u = offset + i * side + j
                    if i + 1 < side:
                        graph.add_edge(u, offset + (i + 1) * side + j)
                    if j + 1 < side:
                        graph.add_edge(u, offset + i * side + j + 1)

        graph.add_edge(15, 16)

    elif family == "shortcut":
        side = 6
        coords = np.asarray(
            [(i, j) for i in range(side) for j in range(side)], dtype=float
        )
        graph_2d = nx.grid_2d_graph(side, side)
        mapping = {node: idx for idx, node in enumerate(graph_2d.nodes())}
        graph = nx.relabel_nodes(graph_2d, mapping)
        for u, v in ((0, 35), (5, 30), (2, 33)):
            graph.add_edge(u, v, shortcut=True)

    elif family == "variable_speed":
        n = 36
        coords = rng.uniform(0.0, 6.0, size=(n, 2))
        graph = ensure_connected_knn(coords, k=4)

    else:
        raise ValueError(f"unknown family: {family}")

    for u, v in graph.edges():
        geometric_length = float(np.linalg.norm(coords[u] - coords[v]))
        speed = 1.0

        if family == "variable_speed":
            speed = float(np.exp(rng.normal(0.0, 0.45)))

        true_cost = geometric_length / speed

        if family == "shortcut" and graph.edges[u, v].get("shortcut", False):
            # The shortcut is physically nonlocal relative to the background
            # embedding, but has a much smaller causal transit cost.
            true_cost = max(0.5, 0.25 * geometric_length)

        graph.edges[u, v]["geometric_length"] = geometric_length
        graph.edges[u, v]["true_cost"] = true_cost

    return graph, coords


def observe_edges(graph: nx.Graph, seed: int) -> nx.Graph:
    rng = np.random.default_rng(seed + 1000)
    observed = graph.copy()
    alpha = 0.7

    for _, _, data in observed.edges(data=True):
        true_cost = float(data["true_cost"])

        transmission = (
            math.exp(-alpha * true_cost)
            * math.exp(float(rng.normal(0.0, 0.12)))
        )
        transmission = float(np.clip(transmission, 1e-4, 0.999))

        delay = true_cost * math.exp(float(rng.normal(0.0, 0.08)))

        data["d1"] = 1.0 / transmission
        data["d2"] = -math.log(transmission)
        data["d3"] = delay
        data["d4"] = 1.0

    return observed


def all_pairs_distance(graph: nx.Graph, weight: str) -> np.ndarray:
    n = graph.number_of_nodes()
    matrix = np.full((n, n), np.inf, dtype=float)
    np.fill_diagonal(matrix, 0.0)

    for source, distances in nx.all_pairs_dijkstra_path_length(graph, weight=weight):
        for target, value in distances.items():
            matrix[source, target] = float(value)

    return matrix


def family_dataset(
    family: str,
    seed: int,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, dict[str, float]]:
    graph, coords = make_family(family, seed)
    observed = observe_edges(graph, seed)
    n = len(coords)
    upper = np.triu_indices(n, 1)

    background = np.linalg.norm(
        coords[:, None, :] - coords[None, :, :], axis=2
    )[upper]
    effective = all_pairs_distance(graph, "true_cost")[upper]

    candidates = [
        all_pairs_distance(observed, key)[upper]
        for key in ("d1", "d2", "d3", "d4")
    ]
    features = np.column_stack(candidates)

    scores: dict[str, float] = {}
    for idx, candidate in enumerate(candidates, start=1):
        scores[f"d{idx}_effective"] = safe_spearman(candidate, effective)
        scores[f"d{idx}_background"] = safe_spearman(candidate, background)

    return features, effective, background, scores


def normalize_graph_dataset(
    features: np.ndarray,
    target: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    feature_scale = np.median(features, axis=0)
    feature_scale = np.where(feature_scale > 0.0, feature_scale, 1.0)
    target_scale = float(np.median(target))
    if target_scale <= 0.0:
        target_scale = 1.0
    return features / feature_scale, target / target_scale


def train_cross_family_model(seeds: int):
    x_rows = []
    y_rows = []

    for seed in range(seeds):
        for family in TRAIN_FAMILIES:
            features, effective, _, _ = family_dataset(family, seed)
            x_norm, y_norm = normalize_graph_dataset(features, effective)
            x_rows.append(x_norm)
            y_rows.append(y_norm)

    x_train = np.vstack(x_rows)
    y_train = np.concatenate(y_rows)

    model = make_pipeline(StandardScaler(), Ridge(alpha=1.0))
    model.fit(x_train, y_train)
    return model


def summarize_family(
    family: str,
    seeds: int,
    model,
) -> FamilySummary:
    rows = []

    for seed in range(seeds):
        features, effective, background, scores = family_dataset(family, seed)
        x_norm, y_norm = normalize_graph_dataset(features, effective)
        prediction = model.predict(x_norm)

        row = dict(scores)
        row["d5_effective"] = safe_spearman(prediction, y_norm)
        row["d5_background"] = safe_spearman(prediction, background)
        rows.append(row)

    def mean(key: str) -> float:
        return float(np.mean([row[key] for row in rows]))

    return FamilySummary(
        family=family,
        seeds=seeds,
        d1_effective_rho=mean("d1_effective"),
        d2_effective_rho=mean("d2_effective"),
        d3_effective_rho=mean("d3_effective"),
        d4_effective_rho=mean("d4_effective"),
        d5_effective_rho=mean("d5_effective"),
        d1_background_rho=mean("d1_background"),
        d2_background_rho=mean("d2_background"),
        d3_background_rho=mean("d3_background"),
        d4_background_rho=mean("d4_background"),
        d5_background_rho=mean("d5_background"),
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seeds", type=int, default=25)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    model = train_cross_family_model(args.seeds)
    summaries = [
        summarize_family(family, args.seeds, model)
        for family in TEST_FAMILIES
    ]

    if args.json:
        print(json.dumps([asdict(s) for s in summaries], indent=2))
        return

    print("SIM-04C: candidate causal-distance comparison")
    print("D5 is trained only on chain + grid families")
    print()
    print("effective causal/path geometry correlations")
    for s in summaries:
        print(
            f"{s.family:15s} "
            f"D1={s.d1_effective_rho:.3f} "
            f"D2={s.d2_effective_rho:.3f} "
            f"D3={s.d3_effective_rho:.3f} "
            f"D4={s.d4_effective_rho:.3f} "
            f"D5={s.d5_effective_rho:.3f}"
        )

    print()
    print("background embedding geometry correlations")
    for s in summaries:
        print(
            f"{s.family:15s} "
            f"D1={s.d1_background_rho:.3f} "
            f"D2={s.d2_background_rho:.3f} "
            f"D3={s.d3_background_rho:.3f} "
            f"D4={s.d4_background_rho:.3f} "
            f"D5={s.d5_background_rho:.3f}"
        )


if __name__ == "__main__":
    main()
