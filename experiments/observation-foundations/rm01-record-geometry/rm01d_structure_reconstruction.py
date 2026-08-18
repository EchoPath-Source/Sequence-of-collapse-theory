#!/usr/bin/env python3
"""RM-01D: record-only higher-structure reconstruction benchmark.

Toy-model methodology only. This is not evidence for SoCT, emergent spacetime,
or any mythic/metaphysical source claim.

The reconstruction stage receives only persistent binary record supports. It is
not given the substrate family, coordinates, edge list, bottleneck labels,
shortcut labels, or target dimension.

Two gates are tested:

1. Structure suite on six heterogeneous graph families:
   - nearest-neighbor recovery
   - direct-edge ranking
   - bottleneck community recovery
   - shortcut detection

2. Equal-size dimension suite:
   - 64-node cycle, 2-D torus, and 3-D torus
   - fixed-cardinality record supports remove node-count and record-density
     confounds
   - a record-only kNN graph is scored by local ball-volume growth
"""

from __future__ import annotations

import argparse
import csv
import math
from dataclasses import asdict, dataclass
from pathlib import Path

import networkx as nx
import numpy as np
from scipy.stats import spearmanr
from sklearn.metrics import adjusted_rand_score, average_precision_score, roc_auc_score


MODES = ("local", "scrambled", "global")
STRUCTURE_FAMILIES = (
    "cycle",
    "torus",
    "irregular",
    "bottleneck",
    "shortcut",
    "variable_speed",
)
DIMENSION_FAMILIES = ("dim_cycle", "dim_torus2d", "dim_torus3d")


@dataclass
class StructureSummary:
    family: str
    mode: str
    seeds: int
    density_mean: float
    density_sd: float
    knn_recovery_mean: float
    knn_recovery_sd: float
    edge_ap_mean: float
    edge_ap_sd: float
    edge_auc_mean: float
    edge_auc_sd: float
    bottleneck_ari_mean: float
    bottleneck_ari_sd: float
    shortcut_closeness_percentile_mean: float
    shortcut_closeness_percentile_sd: float


@dataclass
class DimensionSummary:
    family: str
    mode: str
    seeds: int
    density_mean: float
    density_sd: float
    true_growth_exponent_mean: float
    inferred_growth_exponent_mean: float
    inferred_growth_exponent_sd: float
    abs_error_mean: float
    abs_error_sd: float
    knn_recovery_mean: float
    edge_auc_mean: float


def ensure_connected_knn(
    coords: np.ndarray,
    rng: np.random.Generator,
    *,
    variable_speed: bool,
    k: int = 4,
) -> nx.Graph:
    n = len(coords)
    euclidean = np.linalg.norm(
        coords[:, None, :] - coords[None, :, :],
        axis=2,
    )
    graph = nx.Graph()
    graph.add_nodes_from(range(n))

    def add_edge(u: int, v: int) -> None:
        if graph.has_edge(u, v):
            return
        geometric = float(euclidean[u, v])
        speed = (
            float(np.exp(rng.normal(0.0, 0.50)))
            if variable_speed
            else 1.0
        )
        graph.add_edge(
            u,
            v,
            effective=geometric / speed,
            background=geometric,
        )

    for i in range(n):
        for j in np.argsort(euclidean[i])[1 : k + 1]:
            add_edge(i, int(j))

    while not nx.is_connected(graph):
        components = [list(c) for c in nx.connected_components(graph)]
        first = components[0]
        rest = [node for component in components[1:] for node in component]
        _, u, v = min(
            (euclidean[i, j], i, j)
            for i in first
            for j in rest
        )
        add_edge(int(u), int(v))

    return graph


def make_structure_family(
    family: str,
    seed: int,
) -> tuple[nx.Graph, np.ndarray]:
    rng = np.random.default_rng(seed)

    if family == "cycle":
        n = 48
        graph = nx.cycle_graph(n)
        theta = np.linspace(0.0, 2.0 * np.pi, n, endpoint=False)
        coords = np.column_stack([np.cos(theta), np.sin(theta)])
        for u, v in graph.edges():
            graph.edges[u, v]["effective"] = 1.0
            graph.edges[u, v]["background"] = 1.0

    elif family == "torus":
        side = 8
        raw = nx.grid_2d_graph(side, side, periodic=True)
        nodes = list(raw.nodes())
        mapping = {node: idx for idx, node in enumerate(nodes)}
        graph = nx.relabel_nodes(raw, mapping)
        coords = np.asarray(nodes, dtype=float)
        for u, v in graph.edges():
            graph.edges[u, v]["effective"] = 1.0
            graph.edges[u, v]["background"] = 1.0

    elif family == "irregular":
        coords = rng.uniform(0.0, 8.0, size=(48, 2))
        graph = ensure_connected_knn(
            coords,
            rng,
            variable_speed=False,
            k=4,
        )

    elif family == "bottleneck":
        side = 5
        left = np.asarray(
            [(i, j) for i in range(side) for j in range(side)],
            dtype=float,
        )
        right = np.asarray(
            [(i + 7, j) for i in range(side) for j in range(side)],
            dtype=float,
        )
        coords = np.vstack([left, right])
        graph = nx.Graph()
        graph.add_nodes_from(range(len(coords)))

        for offset in (0, side * side):
            for i in range(side):
                for j in range(side):
                    u = offset + i * side + j
                    if i + 1 < side:
                        graph.add_edge(
                            u,
                            offset + (i + 1) * side + j,
                            effective=1.0,
                            background=1.0,
                        )
                    if j + 1 < side:
                        graph.add_edge(
                            u,
                            offset + i * side + j + 1,
                            effective=1.0,
                            background=1.0,
                        )

        graph.add_edge(
            24,
            25,
            effective=3.0,
            background=3.0,
            bridge=True,
        )

    elif family == "shortcut":
        side = 8
        raw = nx.grid_2d_graph(side, side, periodic=True)
        nodes = list(raw.nodes())
        mapping = {node: idx for idx, node in enumerate(nodes)}
        graph = nx.relabel_nodes(raw, mapping)
        coords = np.asarray(nodes, dtype=float)
        for u, v in graph.edges():
            graph.edges[u, v]["effective"] = 1.0
            graph.edges[u, v]["background"] = 1.0

        for u, v in ((0, 36), (7, 56), (18, 45), (27, 52)):
            graph.add_edge(
                u,
                v,
                effective=0.5,
                background=50.0,
                shortcut=True,
            )

    elif family == "variable_speed":
        coords = rng.uniform(0.0, 8.0, size=(48, 2))
        graph = ensure_connected_knn(
            coords,
            rng,
            variable_speed=True,
            k=4,
        )

    else:
        raise ValueError(f"unknown structure family: {family}")

    return graph, coords


def make_dimension_family(family: str) -> nx.Graph:
    """Equal-size regular families: every graph has exactly 64 nodes."""
    if family == "dim_cycle":
        graph = nx.cycle_graph(64)

    elif family == "dim_torus2d":
        raw = nx.grid_2d_graph(8, 8, periodic=True)
        mapping = {node: idx for idx, node in enumerate(raw.nodes())}
        graph = nx.relabel_nodes(raw, mapping)

    elif family == "dim_torus3d":
        raw = nx.grid_graph(dim=[4, 4, 4], periodic=True)
        mapping = {node: idx for idx, node in enumerate(raw.nodes())}
        graph = nx.relabel_nodes(raw, mapping)

    else:
        raise ValueError(f"unknown dimension family: {family}")

    for u, v in graph.edges():
        graph.edges[u, v]["effective"] = 1.0
        graph.edges[u, v]["background"] = 1.0

    return graph


def transition_matrix(
    graph: nx.Graph,
    *,
    lazy: float,
) -> np.ndarray:
    """Local transition operator; no all-pairs distance enters."""
    n = graph.number_of_nodes()
    weights = np.zeros((n, n), dtype=float)

    for u, v, data in graph.edges(data=True):
        cost = max(float(data["effective"]), 1e-9)
        conductance = 1.0 / cost
        weights[u, v] = conductance
        weights[v, u] = conductance

    row_sum = np.sum(weights, axis=1)
    transition = np.divide(
        weights,
        row_sum[:, None],
        out=np.zeros_like(weights),
        where=row_sum[:, None] > 0.0,
    )

    return (1.0 - lazy) * transition + lazy * np.eye(n)


def exposure_matrix(
    transition: np.ndarray,
    *,
    steps: int,
    decay: float,
) -> np.ndarray:
    """Discounted cumulative local propagation from every source."""
    n = len(transition)
    state = np.eye(n)
    exposure = np.zeros_like(state)

    for step in range(steps + 1):
        exposure += (decay ** step) * state
        state = state @ transition

    return exposure


def generate_bernoulli_records(
    graph: nx.Graph,
    seed: int,
    mode: str,
    *,
    replicas: int,
    steps: int,
    decay: float,
    lazy: float,
    gain: float,
    persistence: float,
) -> np.ndarray:
    """RM-01C-compatible persistent records."""
    transition = transition_matrix(graph, lazy=lazy)
    exposure = exposure_matrix(
        transition,
        steps=steps,
        decay=decay,
    )
    probability = 1.0 - np.exp(-gain * exposure)
    probability = np.repeat(probability, replicas, axis=1)

    mode_offset = MODES.index(mode) * 100_000
    rng = np.random.default_rng(seed + 30_000 + mode_offset)
    records = np.zeros_like(probability, dtype=np.int8)

    for source in range(len(records)):
        p = probability[source]
        if mode == "scrambled":
            p = rng.permutation(p)
        elif mode == "global":
            p = np.full(len(p), float(np.mean(p)))
        elif mode != "local":
            raise ValueError(mode)

        encoded = rng.random(len(p)) < p
        retained = rng.random(len(p)) < persistence
        records[source] = encoded & retained

    return records


def generate_fixed_cardinality_records(
    graph: nx.Graph,
    seed: int,
    mode: str,
    *,
    replicas: int,
    steps: int,
    decay: float,
    lazy: float,
    cardinality_fraction: float,
) -> np.ndarray:
    """Density-matched record generator for the equal-size dimension suite.

    Each event gets exactly the same number of active record fragments.
    Scrambled mode preserves the exposure-weight multiset but permutes fragment
    identity. Global mode chooses uniformly. This removes record-density as an
    explanation for dimension ordering.
    """
    transition = transition_matrix(graph, lazy=lazy)
    exposure = exposure_matrix(
        transition,
        steps=steps,
        decay=decay,
    )
    weights = np.repeat(exposure, replicas, axis=1)
    active = max(
        2,
        int(round(cardinality_fraction * weights.shape[1])),
    )

    mode_offset = MODES.index(mode) * 100_000
    rng = np.random.default_rng(seed + 50_000 + mode_offset)
    records = np.zeros_like(weights, dtype=np.int8)

    for source in range(len(weights)):
        w = weights[source].copy()
        if mode == "scrambled":
            w = rng.permutation(w)
        elif mode == "global":
            w = np.ones_like(w)
        elif mode != "local":
            raise ValueError(mode)

        w = np.maximum(w, 0.0)
        p = w / np.sum(w)
        selected = rng.choice(
            len(w),
            size=active,
            replace=False,
            p=p,
        )
        records[source, selected] = 1

    return records


def jaccard_distance(records: np.ndarray) -> np.ndarray:
    r = records.astype(np.int16, copy=False)
    ones = np.sum(r, axis=1, dtype=float)
    intersection = (r @ r.T).astype(float)
    union = ones[:, None] + ones[None, :] - intersection

    with np.errstate(divide="ignore", invalid="ignore"):
        distance = np.where(
            union > 0.0,
            1.0 - intersection / union,
            1.0,
        )
    np.fill_diagonal(distance, 0.0)
    return distance


def all_pairs_distance(
    graph: nx.Graph,
    weight: str,
) -> np.ndarray:
    n = graph.number_of_nodes()
    out = np.full((n, n), np.inf, dtype=float)
    np.fill_diagonal(out, 0.0)

    for source, distances in nx.all_pairs_dijkstra_path_length(
        graph,
        weight=weight,
    ):
        for target, value in distances.items():
            out[source, target] = float(value)

    return out


def inferred_knn_graph(
    record_distance: np.ndarray,
    *,
    k: int,
) -> nx.Graph:
    """Family-agnostic reconstruction using record distance only."""
    n = len(record_distance)
    graph = nx.Graph()
    graph.add_nodes_from(range(n))

    for i in range(n):
        self_mask = np.arange(n) == i
        nearest = np.argsort(
            np.where(self_mask, np.inf, record_distance[i])
        )[:k]
        for j in nearest:
            graph.add_edge(
                i,
                int(j),
                weight=float(record_distance[i, j]),
            )

    while not nx.is_connected(graph):
        components = [list(c) for c in nx.connected_components(graph)]
        first = components[0]
        rest = [node for component in components[1:] for node in component]
        _, u, v = min(
            (record_distance[i, j], i, j)
            for i in first
            for j in rest
        )
        graph.add_edge(
            int(u),
            int(v),
            weight=float(record_distance[u, v]),
        )

    return graph


def knn_recovery(
    record_distance: np.ndarray,
    graph: nx.Graph,
    *,
    k: int,
) -> float:
    target = all_pairs_distance(graph, "effective")
    scores: list[float] = []
    n = len(record_distance)

    for i in range(n):
        self_mask = np.arange(n) == i
        truth = np.argsort(
            np.where(self_mask, np.inf, target[i])
        )[:k]
        estimate = np.argsort(
            np.where(self_mask, np.inf, record_distance[i])
        )[:k]
        scores.append(
            len(set(truth) & set(estimate)) / float(k)
        )

    return float(np.mean(scores))


def edge_ranking_metrics(
    record_distance: np.ndarray,
    graph: nx.Graph,
) -> tuple[float, float]:
    n = len(record_distance)
    true_edges = {tuple(sorted(edge)) for edge in graph.edges()}
    labels: list[int] = []
    scores: list[float] = []

    for i in range(n):
        for j in range(i + 1, n):
            labels.append(1 if (i, j) in true_edges else 0)
            scores.append(-float(record_distance[i, j]))

    return (
        float(average_precision_score(labels, scores)),
        float(roc_auc_score(labels, scores)),
    )


def fiedler_partition(graph: nx.Graph) -> np.ndarray:
    adjacency = nx.to_numpy_array(graph, weight=None)
    degree = np.sum(adjacency, axis=1)
    laplacian = np.diag(degree) - adjacency
    values, vectors = np.linalg.eigh(laplacian)
    if len(values) < 2:
        return np.zeros(len(values), dtype=int)

    fiedler = vectors[:, 1]
    return (fiedler > np.median(fiedler)).astype(int)


def bottleneck_ari(
    inferred: nx.Graph,
) -> float:
    truth = np.asarray([0] * 25 + [1] * 25, dtype=int)
    estimate = fiedler_partition(inferred)
    return float(adjusted_rand_score(truth, estimate))


def shortcut_closeness_percentile(
    record_distance: np.ndarray,
    graph: nx.Graph,
) -> float:
    shortcuts = [
        (u, v)
        for u, v, data in graph.edges(data=True)
        if data.get("shortcut", False)
    ]
    if not shortcuts:
        return float("nan")

    background = all_pairs_distance(graph, "background")
    upper = np.triu_indices(len(record_distance), 1)
    background_values = background[upper]
    far_cutoff = float(np.quantile(background_values, 0.80))

    far_record_distances = np.asarray(
        [
            record_distance[i, j]
            for i, j in zip(*upper)
            if background[i, j] >= far_cutoff
        ],
        dtype=float,
    )

    ranks = [
        float(np.mean(far_record_distances >= record_distance[u, v]))
        for u, v in shortcuts
    ]
    return float(np.mean(ranks))


def ball_growth_exponent(
    graph: nx.Graph,
    *,
    max_radius: int = 2,
) -> float:
    """Fit log mean ball volume vs log radius.

    The equal-size dimension suite uses radii 1-2 deliberately, because the
    4x4x4 periodic lattice saturates quickly at larger radii.
    """
    lengths = dict(
        nx.all_pairs_shortest_path_length(
            graph,
            cutoff=max_radius,
        )
    )
    radii: list[float] = []
    volumes: list[float] = []

    for radius in range(1, max_radius + 1):
        per_node = [
            sum(
                1
                for target, distance in lengths[node].items()
                if 0 < distance <= radius
            )
            for node in graph.nodes()
        ]
        mean_volume = float(np.mean(per_node))
        if mean_volume > 0.0:
            radii.append(float(radius))
            volumes.append(mean_volume)

    if len(radii) < 2:
        return float("nan")

    slope = np.polyfit(
        np.log(np.asarray(radii)),
        np.log(np.asarray(volumes)),
        1,
    )[0]
    return float(slope)


def structure_trial(
    family: str,
    mode: str,
    seed: int,
    *,
    k: int,
    replicas: int,
    steps: int,
    decay: float,
    lazy: float,
    gain: float,
    persistence: float,
) -> dict[str, float]:
    graph, _ = make_structure_family(family, seed)
    records = generate_bernoulli_records(
        graph,
        seed,
        mode,
        replicas=replicas,
        steps=steps,
        decay=decay,
        lazy=lazy,
        gain=gain,
        persistence=persistence,
    )
    distance = jaccard_distance(records)
    inferred = inferred_knn_graph(distance, k=k)
    edge_ap, edge_auc = edge_ranking_metrics(distance, graph)

    return {
        "density": float(np.mean(records)),
        "knn_recovery": knn_recovery(distance, graph, k=k),
        "edge_ap": edge_ap,
        "edge_auc": edge_auc,
        "bottleneck_ari": (
            bottleneck_ari(inferred)
            if family == "bottleneck"
            else float("nan")
        ),
        "shortcut_closeness_percentile": (
            shortcut_closeness_percentile(distance, graph)
            if family == "shortcut"
            else float("nan")
        ),
    }


def dimension_trial(
    family: str,
    mode: str,
    seed: int,
    *,
    k: int,
    replicas: int,
    steps: int,
    decay: float,
    lazy: float,
    cardinality_fraction: float,
) -> dict[str, float]:
    graph = make_dimension_family(family)
    records = generate_fixed_cardinality_records(
        graph,
        seed,
        mode,
        replicas=replicas,
        steps=steps,
        decay=decay,
        lazy=lazy,
        cardinality_fraction=cardinality_fraction,
    )
    distance = jaccard_distance(records)
    inferred = inferred_knn_graph(distance, k=k)
    true_exponent = ball_growth_exponent(graph, max_radius=2)
    inferred_exponent = ball_growth_exponent(
        inferred,
        max_radius=2,
    )
    _, edge_auc = edge_ranking_metrics(distance, graph)

    return {
        "density": float(np.mean(records)),
        "true_growth_exponent": true_exponent,
        "inferred_growth_exponent": inferred_exponent,
        "abs_error": abs(inferred_exponent - true_exponent),
        "knn_recovery": knn_recovery(distance, graph, k=k),
        "edge_auc": edge_auc,
    }


def finite_stats(values: list[float]) -> tuple[float, float]:
    array = np.asarray(values, dtype=float)
    array = array[np.isfinite(array)]
    if len(array) == 0:
        return float("nan"), float("nan")
    return float(np.mean(array)), float(np.std(array))


def summarize_structure(
    *,
    seeds: int,
    k: int,
    replicas: int,
    steps: int,
    decay: float,
    lazy: float,
    gain: float,
    persistence: float,
) -> list[StructureSummary]:
    rows: list[StructureSummary] = []

    for family in STRUCTURE_FAMILIES:
        for mode in MODES:
            trials = [
                structure_trial(
                    family,
                    mode,
                    seed,
                    k=k,
                    replicas=replicas,
                    steps=steps,
                    decay=decay,
                    lazy=lazy,
                    gain=gain,
                    persistence=persistence,
                )
                for seed in range(seeds)
            ]

            def stat(key: str) -> tuple[float, float]:
                return finite_stats([trial[key] for trial in trials])

            density_mean, density_sd = stat("density")
            knn_mean, knn_sd = stat("knn_recovery")
            ap_mean, ap_sd = stat("edge_ap")
            auc_mean, auc_sd = stat("edge_auc")
            ari_mean, ari_sd = stat("bottleneck_ari")
            shortcut_mean, shortcut_sd = stat(
                "shortcut_closeness_percentile"
            )

            rows.append(
                StructureSummary(
                    family=family,
                    mode=mode,
                    seeds=seeds,
                    density_mean=density_mean,
                    density_sd=density_sd,
                    knn_recovery_mean=knn_mean,
                    knn_recovery_sd=knn_sd,
                    edge_ap_mean=ap_mean,
                    edge_ap_sd=ap_sd,
                    edge_auc_mean=auc_mean,
                    edge_auc_sd=auc_sd,
                    bottleneck_ari_mean=ari_mean,
                    bottleneck_ari_sd=ari_sd,
                    shortcut_closeness_percentile_mean=shortcut_mean,
                    shortcut_closeness_percentile_sd=shortcut_sd,
                )
            )

    return rows


def summarize_dimension(
    *,
    seeds: int,
    k: int,
    replicas: int,
    steps: int,
    decay: float,
    lazy: float,
    cardinality_fraction: float,
) -> tuple[list[DimensionSummary], dict[str, float]]:
    rows: list[DimensionSummary] = []
    raw: dict[tuple[str, str], list[dict[str, float]]] = {}

    for family in DIMENSION_FAMILIES:
        for mode in MODES:
            trials = [
                dimension_trial(
                    family,
                    mode,
                    seed,
                    k=k,
                    replicas=replicas,
                    steps=steps,
                    decay=decay,
                    lazy=lazy,
                    cardinality_fraction=cardinality_fraction,
                )
                for seed in range(seeds)
            ]
            raw[(family, mode)] = trials

            def stat(key: str) -> tuple[float, float]:
                return finite_stats([trial[key] for trial in trials])

            density_mean, density_sd = stat("density")
            true_mean, _ = stat("true_growth_exponent")
            inferred_mean, inferred_sd = stat("inferred_growth_exponent")
            error_mean, error_sd = stat("abs_error")
            knn_mean, _ = stat("knn_recovery")
            auc_mean, _ = stat("edge_auc")

            rows.append(
                DimensionSummary(
                    family=family,
                    mode=mode,
                    seeds=seeds,
                    density_mean=density_mean,
                    density_sd=density_sd,
                    true_growth_exponent_mean=true_mean,
                    inferred_growth_exponent_mean=inferred_mean,
                    inferred_growth_exponent_sd=inferred_sd,
                    abs_error_mean=error_mean,
                    abs_error_sd=error_sd,
                    knn_recovery_mean=knn_mean,
                    edge_auc_mean=auc_mean,
                )
            )

    order_fraction: dict[str, float] = {}
    for mode in MODES:
        successes = 0
        for seed in range(seeds):
            d1 = raw[("dim_cycle", mode)][seed][
                "inferred_growth_exponent"
            ]
            d2 = raw[("dim_torus2d", mode)][seed][
                "inferred_growth_exponent"
            ]
            d3 = raw[("dim_torus3d", mode)][seed][
                "inferred_growth_exponent"
            ]
            successes += int(d1 < d2 < d3)
        order_fraction[mode] = successes / float(seeds)

    return rows, order_fraction


def write_csv(rows: list[object], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = list(asdict(rows[0]).keys())

    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seeds", type=int, default=30)
    parser.add_argument("--k", type=int, default=4)
    parser.add_argument("--replicas", type=int, default=8)
    parser.add_argument("--steps", type=int, default=10)
    parser.add_argument("--decay", type=float, default=0.90)
    parser.add_argument("--lazy", type=float, default=0.25)
    parser.add_argument("--gain", type=float, default=1.50)
    parser.add_argument("--persistence", type=float, default=0.95)
    parser.add_argument(
        "--cardinality-fraction",
        type=float,
        default=0.10,
    )
    parser.add_argument(
        "--structure-csv",
        type=Path,
        default=Path("rm01d_structure_summary.csv"),
    )
    parser.add_argument(
        "--dimension-csv",
        type=Path,
        default=Path("rm01d_dimension_summary.csv"),
    )
    args = parser.parse_args()

    structure = summarize_structure(
        seeds=args.seeds,
        k=args.k,
        replicas=args.replicas,
        steps=args.steps,
        decay=args.decay,
        lazy=args.lazy,
        gain=args.gain,
        persistence=args.persistence,
    )
    dimension, order = summarize_dimension(
        seeds=args.seeds,
        k=args.k,
        replicas=args.replicas,
        steps=args.steps,
        decay=args.decay,
        lazy=args.lazy,
        cardinality_fraction=args.cardinality_fraction,
    )

    write_csv(structure, args.structure_csv)
    write_csv(dimension, args.dimension_csv)

    print("STRUCTURE SUITE")
    for row in structure:
        print(
            f"{row.family:14s} {row.mode:10s} "
            f"kNN={row.knn_recovery_mean:.3f}; "
            f"AP={row.edge_ap_mean:.3f}; "
            f"AUC={row.edge_auc_mean:.3f}; "
            f"ARI={row.bottleneck_ari_mean:.3f}; "
            f"shortcut={row.shortcut_closeness_percentile_mean:.3f}"
        )

    print("\nEQUAL-SIZE DIMENSION SUITE")
    for row in dimension:
        print(
            f"{row.family:14s} {row.mode:10s} "
            f"true={row.true_growth_exponent_mean:.3f}; "
            f"inferred={row.inferred_growth_exponent_mean:.3f}; "
            f"err={row.abs_error_mean:.3f}; "
            f"density={row.density_mean:.3f}"
        )

    print("\nDIMENSION ORDER FRACTION")
    for mode in MODES:
        print(
            f"{mode:10s}: "
            f"P(d_cycle < d_2d < d_3d)={order[mode]:.3f}"
        )


if __name__ == "__main__":
    main()
