#!/usr/bin/env python3
"""RM-01C: dynamic local-propagation record geometry benchmark.

Toy-model methodology only. This is not evidence for SoCT or emergent spacetime.

Unlike RM-01/RM-01B, record-generation probability never uses a global distance
kernel. Records arise from repeated local random-walk propagation on graph edges.

The benchmark asks whether persistent record-support overlap recovers useful
geometry from local dynamics alone.
"""

from __future__ import annotations

import argparse
import csv
import math
from dataclasses import asdict, dataclass
from pathlib import Path

import networkx as nx
import numpy as np

from rm01b_heldout_geometries import (
    FAMILIES,
    MODES,
    all_pairs_distance,
    knn_recovery,
    make_family,
    record_distances,
    safe_spearman,
)


@dataclass
class DynamicSummary:
    family: str
    mode: str
    seeds: int
    record_density_mean: float
    record_density_sd: float
    jaccard_effective_rho_mean: float
    jaccard_effective_rho_sd: float
    jaccard_background_rho_mean: float
    jaccard_background_rho_sd: float
    jaccard_dynamic_rho_mean: float
    jaccard_dynamic_rho_sd: float
    jaccard_knn_mean: float
    jaccard_knn_sd: float
    hamming_effective_rho_mean: float
    hamming_effective_rho_sd: float
    vi_effective_rho_mean: float
    vi_effective_rho_sd: float


def transition_matrix(
    graph: nx.Graph,
    *,
    lazy: float,
) -> np.ndarray:
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


def cumulative_exposure(
    transition: np.ndarray,
    source: int,
    *,
    steps: int,
    decay: float,
) -> np.ndarray:
    state = np.zeros(len(transition), dtype=float)
    state[source] = 1.0
    exposure = np.zeros_like(state)

    for step in range(steps + 1):
        exposure += (decay ** step) * state
        state = state @ transition

    return exposure


def dynamic_path_distance(transition: np.ndarray) -> np.ndarray:
    """Most-probable-path geometry from local transition probabilities.

    Edge cost is -log(P_uv). The result is symmetrized because row-normalized
    transitions can be direction-dependent even on an undirected substrate.
    """
    n = len(transition)
    graph = nx.DiGraph()
    graph.add_nodes_from(range(n))

    for u in range(n):
        for v in np.where(transition[u] > 0.0)[0]:
            if u == v:
                continue
            graph.add_edge(
                u,
                int(v),
                weight=-math.log(float(transition[u, v])),
            )

    directed = np.full((n, n), np.inf, dtype=float)
    np.fill_diagonal(directed, 0.0)

    for source, distances in nx.all_pairs_dijkstra_path_length(
        graph,
        weight="weight",
    ):
        for target, value in distances.items():
            directed[source, target] = float(value)

    return 0.5 * (directed + directed.T)


def one_trial(
    family: str,
    mode: str,
    seed: int,
    *,
    replicas: int,
    steps: int,
    decay: float,
    lazy: float,
    gain: float,
    persistence: float,
) -> dict[str, float]:
    graph, _ = make_family(family, seed)
    effective = all_pairs_distance(graph, "effective")
    background = all_pairs_distance(graph, "background")

    transition = transition_matrix(graph, lazy=lazy)
    dynamic_distance = dynamic_path_distance(transition)

    exposures = np.asarray(
        [
            cumulative_exposure(
                transition,
                source,
                steps=steps,
                decay=decay,
            )
            for source in range(graph.number_of_nodes())
        ],
        dtype=float,
    )

    # No global distance appears here. Record probability depends only on the
    # cumulative result of local transition dynamics.
    probability = 1.0 - np.exp(-gain * exposures)
    probability = np.repeat(probability, replicas, axis=1)

    rng = np.random.default_rng(seed + 30_000)
    records = np.zeros_like(probability, dtype=np.int8)

    for source in range(len(records)):
        local = probability[source]
        if mode == "local":
            p = local
        elif mode == "scrambled":
            p = rng.permutation(local)
        elif mode == "global":
            p = np.full(len(local), float(np.mean(local)))
        else:
            raise ValueError(f"unknown mode: {mode}")

        encoded = rng.random(len(local)) < p
        retained = rng.random(len(local)) < persistence
        records[source] = encoded & retained

    candidates = record_distances(records)
    upper = np.triu_indices(len(records), 1)
    jaccard = candidates["jaccard"]

    return {
        "record_density": float(np.mean(records)),
        "jaccard_effective_rho": safe_spearman(
            jaccard[upper],
            effective[upper],
        ),
        "jaccard_background_rho": safe_spearman(
            jaccard[upper],
            background[upper],
        ),
        "jaccard_dynamic_rho": safe_spearman(
            jaccard[upper],
            dynamic_distance[upper],
        ),
        "jaccard_knn": knn_recovery(
            jaccard,
            effective,
            k=4,
        ),
        "hamming_effective_rho": safe_spearman(
            candidates["hamming"][upper],
            effective[upper],
        ),
        "vi_effective_rho": safe_spearman(
            candidates["vi"][upper],
            effective[upper],
        ),
    }


def summarize(
    *,
    seeds: int,
    replicas: int,
    steps: int,
    decay: float,
    lazy: float,
    gain: float,
    persistence: float,
) -> list[DynamicSummary]:
    rows: list[DynamicSummary] = []

    for family in FAMILIES:
        for mode in MODES:
            trials = [
                one_trial(
                    family,
                    mode,
                    seed,
                    replicas=replicas,
                    steps=steps,
                    decay=decay,
                    lazy=lazy,
                    gain=gain,
                    persistence=persistence,
                )
                for seed in range(seeds)
            ]

            def stats(key: str) -> tuple[float, float]:
                values = np.asarray(
                    [trial[key] for trial in trials],
                    dtype=float,
                )
                return float(np.mean(values)), float(np.std(values))

            density_mean, density_sd = stats("record_density")
            je_mean, je_sd = stats("jaccard_effective_rho")
            jb_mean, jb_sd = stats("jaccard_background_rho")
            jd_mean, jd_sd = stats("jaccard_dynamic_rho")
            knn_mean, knn_sd = stats("jaccard_knn")
            h_mean, h_sd = stats("hamming_effective_rho")
            vi_mean, vi_sd = stats("vi_effective_rho")

            rows.append(
                DynamicSummary(
                    family=family,
                    mode=mode,
                    seeds=seeds,
                    record_density_mean=density_mean,
                    record_density_sd=density_sd,
                    jaccard_effective_rho_mean=je_mean,
                    jaccard_effective_rho_sd=je_sd,
                    jaccard_background_rho_mean=jb_mean,
                    jaccard_background_rho_sd=jb_sd,
                    jaccard_dynamic_rho_mean=jd_mean,
                    jaccard_dynamic_rho_sd=jd_sd,
                    jaccard_knn_mean=knn_mean,
                    jaccard_knn_sd=knn_sd,
                    hamming_effective_rho_mean=h_mean,
                    hamming_effective_rho_sd=h_sd,
                    vi_effective_rho_mean=vi_mean,
                    vi_effective_rho_sd=vi_sd,
                )
            )

    return rows


def write_csv(rows: list[DynamicSummary], path: Path) -> None:
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
    parser.add_argument("--replicas", type=int, default=8)
    parser.add_argument("--steps", type=int, default=10)
    parser.add_argument("--decay", type=float, default=0.90)
    parser.add_argument("--lazy", type=float, default=0.25)
    parser.add_argument("--gain", type=float, default=1.50)
    parser.add_argument("--persistence", type=float, default=0.95)
    parser.add_argument(
        "--out-csv",
        type=Path,
        default=Path("rm01c_dynamic_summary.csv"),
    )
    args = parser.parse_args()

    rows = summarize(
        seeds=args.seeds,
        replicas=args.replicas,
        steps=args.steps,
        decay=args.decay,
        lazy=args.lazy,
        gain=args.gain,
        persistence=args.persistence,
    )
    write_csv(rows, args.out_csv)

    for row in rows:
        print(
            f"{row.family:14s} {row.mode:10s} "
            f"J_eff={row.jaccard_effective_rho_mean:.3f}; "
            f"J_dyn={row.jaccard_dynamic_rho_mean:.3f}; "
            f"J_bg={row.jaccard_background_rho_mean:.3f}; "
            f"kNN={row.jaccard_knn_mean:.3f}; "
            f"density={row.record_density_mean:.3f}"
        )


if __name__ == "__main__":
    main()
