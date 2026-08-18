#!/usr/bin/env python3
"""RM-01B: cross-family persistent-record geometry stress test.

Toy-model methodology only. This is not evidence for SoCT or emergent spacetime.

RM-01 showed that Jaccard distance between persistent record supports can recover
a hidden periodic lattice geometry when record formation is local. RM-01B asks
whether the same reconstruction rule generalizes across qualitatively different
substrates without tuning the reconstruction metric.

Families:
    cycle
    torus
    irregular
    bottleneck
    shortcut
    variable_speed

For every family, records are generated from the effective propagation metric.
Scrambled and global controls preserve record abundance while destroying
structured locality. Shortcut and variable-speed families separately track a
background geometry to test whether record overlap follows effective causal/path
geometry rather than background embedding geometry.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import asdict, dataclass
from pathlib import Path

import networkx as nx
import numpy as np
from scipy.stats import spearmanr


FAMILIES = (
    "cycle",
    "torus",
    "irregular",
    "bottleneck",
    "shortcut",
    "variable_speed",
)
MODES = ("local", "scrambled", "global")


@dataclass
class FamilySummary:
    family: str
    mode: str
    seeds: int
    record_density_mean: float
    record_density_sd: float
    jaccard_effective_rho_mean: float
    jaccard_effective_rho_sd: float
    jaccard_background_rho_mean: float
    jaccard_background_rho_sd: float
    jaccard_knn_mean: float
    jaccard_knn_sd: float
    hamming_effective_rho_mean: float
    hamming_effective_rho_sd: float
    vi_effective_rho_mean: float
    vi_effective_rho_sd: float


def safe_spearman(a: np.ndarray, b: np.ndarray) -> float:
    value = spearmanr(a, b).statistic
    return float(value) if np.isfinite(value) else 0.0


def all_pairs_distance(graph: nx.Graph, weight: str) -> np.ndarray:
    n = graph.number_of_nodes()
    out = np.full((n, n), np.inf, dtype=float)
    np.fill_diagonal(out, 0.0)
    for source, distances in nx.all_pairs_dijkstra_path_length(
        graph, weight=weight
    ):
        for target, value in distances.items():
            out[source, target] = float(value)
    return out


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


def make_family(
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
        graph_2d = nx.grid_2d_graph(side, side, periodic=True)
        mapping = {node: idx for idx, node in enumerate(graph_2d.nodes())}
        graph = nx.relabel_nodes(graph_2d, mapping)
        coords = np.asarray(list(graph_2d.nodes()), dtype=float)
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

        graph.add_edge(24, 25, effective=3.0, background=3.0)

    elif family == "shortcut":
        side = 8
        graph_2d = nx.grid_2d_graph(side, side, periodic=True)
        mapping = {node: idx for idx, node in enumerate(graph_2d.nodes())}
        graph = nx.relabel_nodes(graph_2d, mapping)
        coords = np.asarray(list(graph_2d.nodes()), dtype=float)
        for u, v in graph.edges():
            graph.edges[u, v]["effective"] = 1.0
            graph.edges[u, v]["background"] = 1.0

        for u, v in ((0, 36), (7, 56), (18, 45), (27, 52)):
            graph.add_edge(
                u,
                v,
                effective=0.5,
                background=50.0,
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
        raise ValueError(f"unknown family: {family}")

    return graph, coords


def entropy_from_counts(counts: np.ndarray, total: int) -> np.ndarray:
    probabilities = counts / float(total)
    with np.errstate(divide="ignore", invalid="ignore"):
        terms = np.where(
            probabilities > 0.0,
            -probabilities * np.log2(probabilities),
            0.0,
        )
    return np.sum(terms, axis=-1)


def record_distances(records: np.ndarray) -> dict[str, np.ndarray]:
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
    vi = np.maximum(
        2.0 * h_xy - h_x[:, None] - h_x[None, :],
        0.0,
    )
    np.fill_diagonal(vi, 0.0)

    return {
        "jaccard": jaccard,
        "hamming": hamming,
        "vi": vi,
    }


def knn_recovery(
    candidate: np.ndarray,
    target: np.ndarray,
    *,
    k: int = 4,
) -> float:
    scores: list[float] = []
    n = len(candidate)
    for i in range(n):
        self_mask = np.arange(n) == i
        truth = np.argsort(
            np.where(self_mask, np.inf, target[i])
        )[:k]
        estimate = np.argsort(
            np.where(self_mask, np.inf, candidate[i])
        )[:k]
        scores.append(
            len(set(truth) & set(estimate)) / float(k)
        )
    return float(np.mean(scores))


def one_trial(
    family: str,
    mode: str,
    seed: int,
    *,
    replicas: int,
    broadcast: float,
    persistence: float,
    scale_factor: float,
) -> dict[str, float]:
    graph, _ = make_family(family, seed)
    effective = all_pairs_distance(graph, "effective")
    background = all_pairs_distance(graph, "background")
    n = len(effective)

    nearest = np.asarray(
        [np.min(row[row > 0.0]) for row in effective],
        dtype=float,
    )
    lengthscale = scale_factor * float(np.median(nearest))

    local_probability = broadcast * np.exp(
        -effective / lengthscale
    )
    local_probability = np.repeat(
        local_probability,
        replicas,
        axis=1,
    )

    rng = np.random.default_rng(seed + 10_000)
    records = np.zeros(
        (n, n * replicas),
        dtype=np.int8,
    )

    for event in range(n):
        local = local_probability[event]
        if mode == "local":
            probability = local
        elif mode == "scrambled":
            probability = rng.permutation(local)
        elif mode == "global":
            probability = np.full(
                len(local),
                float(np.mean(local)),
            )
        else:
            raise ValueError(f"unknown mode: {mode}")

        encoded = rng.random(len(local)) < probability
        retained = rng.random(len(local)) < persistence
        records[event] = encoded & retained

    candidates = record_distances(records)
    upper = np.triu_indices(n, 1)
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
    broadcast: float,
    persistence: float,
    scale_factor: float,
) -> list[FamilySummary]:
    rows: list[FamilySummary] = []

    for family in FAMILIES:
        for mode in MODES:
            trials = [
                one_trial(
                    family,
                    mode,
                    seed,
                    replicas=replicas,
                    broadcast=broadcast,
                    persistence=persistence,
                    scale_factor=scale_factor,
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
            je_mean, je_sd = stats("jaccard_effective_rho")
            jb_mean, jb_sd = stats("jaccard_background_rho")
            knn_mean, knn_sd = stats("jaccard_knn")
            h_mean, h_sd = stats("hamming_effective_rho")
            vi_mean, vi_sd = stats("vi_effective_rho")

            rows.append(
                FamilySummary(
                    family=family,
                    mode=mode,
                    seeds=seeds,
                    record_density_mean=density_mean,
                    record_density_sd=density_sd,
                    jaccard_effective_rho_mean=je_mean,
                    jaccard_effective_rho_sd=je_sd,
                    jaccard_background_rho_mean=jb_mean,
                    jaccard_background_rho_sd=jb_sd,
                    jaccard_knn_mean=knn_mean,
                    jaccard_knn_sd=knn_sd,
                    hamming_effective_rho_mean=h_mean,
                    hamming_effective_rho_sd=h_sd,
                    vi_effective_rho_mean=vi_mean,
                    vi_effective_rho_sd=vi_sd,
                )
            )

    return rows


def write_csv(rows: list[FamilySummary], path: Path) -> None:
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
    parser.add_argument("--broadcast", type=float, default=1.0)
    parser.add_argument("--persistence", type=float, default=0.95)
    parser.add_argument("--scale-factor", type=float, default=1.6)
    parser.add_argument(
        "--out-csv",
        type=Path,
        default=Path("rm01b_family_summary.csv"),
    )
    args = parser.parse_args()

    rows = summarize(
        seeds=args.seeds,
        replicas=args.replicas,
        broadcast=args.broadcast,
        persistence=args.persistence,
        scale_factor=args.scale_factor,
    )
    write_csv(rows, args.out_csv)

    for row in rows:
        print(
            f"{row.family:14s} {row.mode:10s} "
            f"J_eff={row.jaccard_effective_rho_mean:.3f} +/- "
            f"{row.jaccard_effective_rho_sd:.3f}; "
            f"J_bg={row.jaccard_background_rho_mean:.3f}; "
            f"kNN={row.jaccard_knn_mean:.3f}; "
            f"H={row.hamming_effective_rho_mean:.3f}; "
            f"VI={row.vi_effective_rho_mean:.3f}; "
            f"density={row.record_density_mean:.3f}"
        )


if __name__ == "__main__":
    main()
