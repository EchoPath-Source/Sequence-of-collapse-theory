#!/usr/bin/env python3
"""SIM-04F: derive the SoCT memory source from an operational observation model.

Toy-model methodology test only. This is not empirical evidence for an SoCT
memory field or for observer-induced collapse.

The pipeline is:

    interaction parameter theta
        -> conditional pointer-state distinguishability
        -> accessible binary information
        -> ordinary detector record acquisition / persistence
        -> competing source functionals
        -> source-decay-diffusion memory equation
        -> propagation-delay residual

Competing source mappings receive the same downstream memory equation and the
same fitting privileges. The principal held-out adversary uses strong
interaction with fragile records, so a source that ignores persistence should
overpredict the downstream memory signal.

Requires:
    numpy
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass

import numpy as np


SIDE = 8
TRAIN_PROTOCOLS = ("A", "B")
TEST_PROTOCOLS = ("C", "D")
SOURCE_ORDER = (
    "interaction",
    "info",
    "omega",
    "gamma_acq",
    "gamma_rec",
)


@dataclass
class SourceSummary:
    source_model: str
    seeds: int
    test_rmse_mean: float
    protocol_c_rmse_mean: float
    protocol_d_rmse_mean: float
    fitted_beta_mean: float
    fitted_D_mean: float


@dataclass
class GeneratorCheck:
    generator: str
    best_source: str
    best_test_rmse: float
    runner_up_test_rmse: float


def grid_operators(side: int = SIDE):
    n = side * side
    adjacency = np.zeros((n, n), dtype=float)
    edges = []

    def index(i: int, j: int) -> int:
        return i * side + j

    for i in range(side):
        for j in range(side):
            u = index(i, j)
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < side and 0 <= nj < side:
                    adjacency[u, index(ni, nj)] = 1.0

            if i + 1 < side:
                edges.append((u, index(i + 1, j)))
            if j + 1 < side:
                edges.append((u, index(i, j + 1)))

    degree = adjacency.sum(axis=1)
    transition = adjacency / degree[:, None]
    normalized_laplacian = transition - np.eye(n)
    return normalized_laplacian, np.asarray(edges, dtype=int)


LAPLACIAN, EDGES = grid_operators()


def binary_entropy(p: np.ndarray) -> np.ndarray:
    p = np.clip(p, 1e-12, 1.0 - 1e-12)
    return -(p * np.log2(p) + (1.0 - p) * np.log2(1.0 - p))


def pointer_metrics(theta: np.ndarray):
    """Metrics for |o0>=|0>, |o1>=cos(theta)|0>+sin(theta)|1>."""
    distinguishability = np.sin(theta)
    helstrom_error = (1.0 - distinguishability) / 2.0
    accessible_information = 1.0 - binary_entropy(helstrom_error)
    interaction = np.clip(theta / (np.pi / 2.0), 0.0, 1.0)
    return interaction, distinguishability, accessible_information


def add_region(
    protocol: dict[str, np.ndarray],
    start: int,
    stop: int,
    row: int,
    col: int,
    theta: float,
    erase: float,
    access: float = 1.0,
) -> None:
    node = row * SIDE + col
    protocol["theta"][start:stop, node] = np.maximum(
        protocol["theta"][start:stop, node], theta
    )
    protocol["erase"][start:stop, node] = erase
    protocol["access"][start:stop, node] = access


def make_protocol(name: str, steps: int = 80) -> dict[str, np.ndarray]:
    protocol = {
        "theta": np.zeros((steps, SIDE * SIDE), dtype=float),
        "erase": np.full((steps, SIDE * SIDE), 0.08, dtype=float),
        "access": np.ones((steps, SIDE * SIDE), dtype=float),
    }

    if name == "A":
        add_region(protocol, 8, 24, 3, 3, 1.15, erase=0.05)
        add_region(protocol, 38, 47, 3, 3, 0.80, erase=0.05)
    elif name == "B":
        add_region(protocol, 5, 18, 1, 1, 1.00, erase=0.04)
        add_region(protocol, 28, 43, 6, 6, 1.10, erase=0.06)
    elif name == "C":
        add_region(protocol, 7, 17, 1, 6, 0.95, erase=0.05)
        add_region(protocol, 23, 34, 6, 1, 1.20, erase=0.04)
        add_region(protocol, 48, 56, 4, 4, 0.75, erase=0.05)
    elif name == "D":
        # Held-out adversary: strong interaction but fragile / short-lived records.
        add_region(protocol, 8, 25, 2, 5, 1.20, erase=0.65)
        add_region(protocol, 35, 50, 5, 2, 1.05, erase=0.55)
    else:
        raise ValueError(f"unknown protocol: {name}")

    return protocol


PROTOCOLS = {name: make_protocol(name) for name in ("A", "B", "C", "D")}


def derive_sources(
    protocol: dict[str, np.ndarray],
    acquisition_rate: float = 0.55,
    persistence_horizon: int = 4,
) -> dict[str, np.ndarray]:
    interaction, distinguishability, information = pointer_metrics(protocol["theta"])

    record = np.zeros_like(information)
    acquisition = np.zeros_like(information)
    robust_acquisition = np.zeros_like(information)
    previous = np.zeros(information.shape[1], dtype=float)

    for step in range(information.shape[0]):
        gain = acquisition_rate * information[step] * (1.0 - previous)
        retained = (1.0 - protocol["erase"][step]) * previous
        current = np.clip(retained + gain, 0.0, 1.0)

        persistence = (1.0 - protocol["erase"][step]) ** persistence_horizon
        acquisition[step] = gain * protocol["access"][step]
        robust_acquisition[step] = (
            gain * persistence * protocol["access"][step]
        )
        record[step] = current
        previous = current

    omega = (
        interaction
        * distinguishability
        * record
        * protocol["access"]
    )

    return {
        "interaction": interaction * protocol["access"],
        "info": information * protocol["access"],
        "omega": omega,
        "gamma_acq": acquisition,
        "gamma_rec": robust_acquisition,
    }


SOURCES = {name: derive_sources(protocol) for name, protocol in PROTOCOLS.items()}


def simulate_memory(
    source: np.ndarray,
    beta: float,
    diffusion: float,
    alpha: float = 1.0,
) -> np.ndarray:
    steps, nodes = source.shape
    field = np.zeros((steps, nodes), dtype=float)
    state = np.zeros(nodes, dtype=float)

    for step in range(steps):
        state = (
            state
            + alpha * source[step]
            - beta * state
            + diffusion * (LAPLACIAN @ state)
        )
        field[step] = state

    return field


def edge_field(node_field: np.ndarray) -> np.ndarray:
    return 0.5 * (
        node_field[:, EDGES[:, 0]] + node_field[:, EDGES[:, 1]]
    )


def flatten_candidate(
    source_name: str,
    protocols,
    beta: float,
    diffusion: float,
) -> np.ndarray:
    return np.concatenate(
        [
            edge_field(
                simulate_memory(
                    SOURCES[name][source_name],
                    beta=beta,
                    diffusion=diffusion,
                )
            ).ravel()
            for name in protocols
        ]
    )


def build_libraries():
    libraries = {}

    for source_name in SOURCE_ORDER:
        train_rows = []
        test_rows = []
        params = []

        for beta in np.arange(0.04, 0.181, 0.01):
            for diffusion in np.arange(0.0, 0.301, 0.02):
                train_rows.append(
                    flatten_candidate(
                        source_name,
                        TRAIN_PROTOCOLS,
                        beta,
                        diffusion,
                    )
                )
                test_rows.append(
                    flatten_candidate(
                        source_name,
                        TEST_PROTOCOLS,
                        beta,
                        diffusion,
                    )
                )
                params.append((float(beta), float(diffusion)))

        libraries[source_name] = {
            "train": np.asarray(train_rows),
            "test": np.asarray(test_rows),
            "params": params,
        }

    return libraries


def generate_observations(
    source_generator: str,
    seed: int,
    beta: float = 0.08,
    diffusion: float = 0.18,
    scale: float = 0.05,
    noise_sigma: float = 0.0015,
):
    rng = np.random.default_rng(seed)
    observed = {}

    for name in ("A", "B", "C", "D"):
        field = simulate_memory(
            SOURCES[name][source_generator],
            beta=beta,
            diffusion=diffusion,
        )
        edge_signal = scale * edge_field(field)
        observed[name] = edge_signal + rng.normal(
            0.0,
            noise_sigma,
            size=edge_signal.shape,
        )

    train = np.concatenate([observed[name].ravel() for name in TRAIN_PROTOCOLS])
    test = np.concatenate([observed[name].ravel() for name in TEST_PROTOCOLS])
    return train, test, observed


def rmse(prediction: np.ndarray, observed: np.ndarray) -> float:
    return float(np.sqrt(np.mean((prediction - observed) ** 2)))


def fit_candidate(
    observed_train: np.ndarray,
    observed_test: np.ndarray,
    observed_by_protocol: dict[str, np.ndarray],
    source_name: str,
    library,
):
    train_matrix = np.asarray(library["train"])
    test_matrix = np.asarray(library["test"])

    numerator = train_matrix @ observed_train
    denominator = np.sum(train_matrix * train_matrix, axis=1) + 1e-12
    scales = numerator / denominator

    train_error = np.sqrt(
        np.mean(
            (train_matrix * scales[:, None] - observed_train[None, :]) ** 2,
            axis=1,
        )
    )
    best = int(np.argmin(train_error))
    beta, diffusion = library["params"][best]

    per_protocol = {}
    for name in TEST_PROTOCOLS:
        candidate = edge_field(
            simulate_memory(
                SOURCES[name][source_name],
                beta=beta,
                diffusion=diffusion,
            )
        )
        per_protocol[name] = rmse(
            scales[best] * candidate,
            observed_by_protocol[name],
        )

    return {
        "test_rmse": rmse(test_matrix[best] * scales[best], observed_test),
        "protocol_c_rmse": per_protocol["C"],
        "protocol_d_rmse": per_protocol["D"],
        "beta": float(beta),
        "D": float(diffusion),
        "scale": float(scales[best]),
    }


def summarize_primary(seeds: int, libraries):
    rows = {source: [] for source in SOURCE_ORDER}

    for seed in range(seeds):
        observed_train, observed_test, observed = generate_observations(
            "gamma_rec",
            seed=1000 + seed,
        )

        for source in SOURCE_ORDER:
            rows[source].append(
                fit_candidate(
                    observed_train,
                    observed_test,
                    observed,
                    source,
                    libraries[source],
                )
            )

    summaries = []
    for source in SOURCE_ORDER:
        values = rows[source]
        summaries.append(
            SourceSummary(
                source_model=source,
                seeds=seeds,
                test_rmse_mean=float(np.mean([x["test_rmse"] for x in values])),
                protocol_c_rmse_mean=float(
                    np.mean([x["protocol_c_rmse"] for x in values])
                ),
                protocol_d_rmse_mean=float(
                    np.mean([x["protocol_d_rmse"] for x in values])
                ),
                fitted_beta_mean=float(np.mean([x["beta"] for x in values])),
                fitted_D_mean=float(np.mean([x["D"] for x in values])),
            )
        )

    return summaries


def generator_checks(seeds: int, libraries):
    checks = []

    # These checks make sure the fitting pipeline does not mechanically prefer
    # Gamma_rec when a different source law actually generated the data.
    for generator in ("gamma_rec", "gamma_acq", "omega", "info"):
        scores = {source: [] for source in SOURCE_ORDER}

        for seed in range(seeds):
            observed_train, observed_test, observed = generate_observations(
                generator,
                seed=3000 + seed,
            )
            for source in SOURCE_ORDER:
                fit = fit_candidate(
                    observed_train,
                    observed_test,
                    observed,
                    source,
                    libraries[source],
                )
                scores[source].append(fit["test_rmse"])

        mean_scores = {
            source: float(np.mean(values))
            for source, values in scores.items()
        }
        ranked = sorted(mean_scores.items(), key=lambda item: item[1])
        checks.append(
            GeneratorCheck(
                generator=generator,
                best_source=ranked[0][0],
                best_test_rmse=ranked[0][1],
                runner_up_test_rmse=ranked[1][1],
            )
        )

    return checks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seeds", type=int, default=12)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    libraries = build_libraries()
    summaries = summarize_primary(args.seeds, libraries)
    checks = generator_checks(args.seeds, libraries)

    if args.json:
        print(
            json.dumps(
                {
                    "primary_gamma_rec_generator": [
                        asdict(summary) for summary in summaries
                    ],
                    "generator_checks": [asdict(check) for check in checks],
                },
                indent=2,
            )
        )
        return

    print("SIM-04F observation-derived source benchmark")
    print("primary generator: Gamma_rec")
    print()
    for summary in summaries:
        print(
            f"{summary.source_model:12s} "
            f"test={summary.test_rmse_mean:.6f} "
            f"C={summary.protocol_c_rmse_mean:.6f} "
            f"D={summary.protocol_d_rmse_mean:.6f} "
            f"beta={summary.fitted_beta_mean:.3f} "
            f"D_M={summary.fitted_D_mean:.3f}"
        )

    print()
    print("generator sanity checks")
    for check in checks:
        print(
            f"{check.generator:12s} -> {check.best_source:12s} "
            f"best={check.best_test_rmse:.6f} "
            f"runner_up={check.runner_up_test_rmse:.6f}"
        )


if __name__ == "__main__":
    main()
