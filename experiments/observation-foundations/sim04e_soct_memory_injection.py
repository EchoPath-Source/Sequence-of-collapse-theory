#!/usr/bin/env python3
"""SIM-04E: first SoCT-specific memory-field injection benchmark.

Toy-model methodology test only. This is not empirical evidence for the SoCT
memory field or for modified spacetime.

The data-generating SoCT-like branch uses the repository's canonical
phenomenological equation in discrete graph form:

    dM/dt = alpha C - beta M + D_M Laplacian(M)

Only one feedback channel is allowed in this simulation: M produces a small
fractional propagation-delay residual on each edge through the average memory
at its two endpoints.

The test asks whether beta, D_M, and one overall coupling scale learned on two
source-history protocols transfer to unseen protocols better than simpler
nulls:

    instantaneous source / medium response
    instantaneous spatially smoothed source
    ordinary local memory with D_M = 0
    source-decay-diffusion memory

The script also generates null datasets to check that the diffusive model does
not automatically win when diffusion is absent.

Requires:
    numpy
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass

import numpy as np


TRAIN_PROTOCOLS = ("A", "B")
TEST_PROTOCOLS = ("C", "D")
MODEL_ORDER = ("instant", "spatial_instant", "local_memory", "diffusive_memory")


@dataclass
class GeneratorSummary:
    generator: str
    seeds: int
    instant_test_rmse: float
    spatial_instant_test_rmse: float
    local_memory_test_rmse: float
    diffusive_memory_test_rmse: float
    fitted_diffusive_beta_mean: float
    fitted_diffusive_D_mean: float


@dataclass
class MatchedPresentSummary:
    edge_rms_history_residual_t40: float
    per_edge_noise_sigma: float
    rms_to_noise_ratio_t40: float
    instantaneous_prediction_rms_t40: float
    local_memory_shape_correlation_t40: float


def grid_operators(side: int = 8):
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
    return normalized_laplacian, transition, np.asarray(edges, dtype=int)


LAPLACIAN, NEIGHBOR_AVERAGE, EDGES = grid_operators(side=8)


def add_pulse(
    source: np.ndarray,
    start: int,
    stop: int,
    row: int,
    col: int,
    amplitude: float,
) -> None:
    side = int(np.sqrt(source.shape[1]))
    source[start:stop, row * side + col] = amplitude


def make_protocol(name: str, steps: int = 70, side: int = 8) -> np.ndarray:
    source = np.zeros((steps, side * side), dtype=float)

    if name == "A":
        add_pulse(source, 8, 24, 3, 3, 1.0)
        add_pulse(source, 34, 42, 3, 3, 0.6)
    elif name == "B":
        add_pulse(source, 5, 18, 1, 1, 1.0)
        add_pulse(source, 25, 39, 6, 6, 0.9)
    elif name == "C":
        add_pulse(source, 6, 15, 1, 6, 0.8)
        add_pulse(source, 20, 28, 6, 1, 1.0)
        add_pulse(source, 42, 48, 4, 4, 0.7)
    elif name == "D":
        add_pulse(source, 8, 20, 2, 5, 1.0)
        add_pulse(source, 30, 44, 5, 2, 0.8)
    else:
        raise ValueError(f"unknown protocol: {name}")

    return source


PROTOCOLS = {name: make_protocol(name) for name in ("A", "B", "C", "D")}


def simulate_memory(
    source: np.ndarray,
    beta: float,
    diffusion: float,
    alpha: float = 1.0,
) -> np.ndarray:
    """Discrete graph version of alpha*C - beta*M + D*Laplacian(M)."""
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


def spatial_instantaneous(
    source: np.ndarray,
    gamma: float,
    smoothing_steps: int,
) -> np.ndarray:
    """Spatial spread without temporal memory."""
    field = source.copy()
    for _ in range(smoothing_steps):
        field = (
            (1.0 - gamma) * field
            + gamma * (field @ NEIGHBOR_AVERAGE.T)
        )
    return field


def edge_field(node_field: np.ndarray) -> np.ndarray:
    return 0.5 * (
        node_field[:, EDGES[:, 0]] + node_field[:, EDGES[:, 1]]
    )


def flatten_fields(fields: dict[str, np.ndarray], names) -> np.ndarray:
    return np.concatenate([edge_field(fields[name]).ravel() for name in names])


def fit_scale(candidate: np.ndarray, observed: np.ndarray) -> float:
    return float(
        np.dot(candidate, observed)
        / (np.dot(candidate, candidate) + 1e-12)
    )


def rmse(prediction: np.ndarray, observed: np.ndarray) -> float:
    return float(np.sqrt(np.mean((prediction - observed) ** 2)))


def build_candidate_library():
    library: dict[str, dict[str, object]] = {}

    instant_fields = {name: source for name, source in PROTOCOLS.items()}
    library["instant"] = {
        "train": flatten_fields(instant_fields, TRAIN_PROTOCOLS)[None, :],
        "test": flatten_fields(instant_fields, TEST_PROTOCOLS)[None, :],
        "params": [{}],
    }

    local_train = []
    local_test = []
    local_params = []
    for beta in np.arange(0.02, 0.251, 0.01):
        fields = {
            name: simulate_memory(source, beta=beta, diffusion=0.0)
            for name, source in PROTOCOLS.items()
        }
        local_train.append(flatten_fields(fields, TRAIN_PROTOCOLS))
        local_test.append(flatten_fields(fields, TEST_PROTOCOLS))
        local_params.append({"beta": float(beta)})

    library["local_memory"] = {
        "train": np.asarray(local_train),
        "test": np.asarray(local_test),
        "params": local_params,
    }

    diffusion_train = []
    diffusion_test = []
    diffusion_params = []
    for beta in np.arange(0.04, 0.181, 0.01):
        for diffusion in np.arange(0.0, 0.301, 0.02):
            fields = {
                name: simulate_memory(
                    source,
                    beta=beta,
                    diffusion=diffusion,
                )
                for name, source in PROTOCOLS.items()
            }
            diffusion_train.append(flatten_fields(fields, TRAIN_PROTOCOLS))
            diffusion_test.append(flatten_fields(fields, TEST_PROTOCOLS))
            diffusion_params.append(
                {"beta": float(beta), "D": float(diffusion)}
            )

    library["diffusive_memory"] = {
        "train": np.asarray(diffusion_train),
        "test": np.asarray(diffusion_test),
        "params": diffusion_params,
    }

    spatial_train = []
    spatial_test = []
    spatial_params = []
    for smoothing_steps in (1, 2, 3, 4):
        for gamma in np.arange(0.10, 0.901, 0.05):
            fields = {
                name: spatial_instantaneous(
                    source,
                    gamma=gamma,
                    smoothing_steps=smoothing_steps,
                )
                for name, source in PROTOCOLS.items()
            }
            spatial_train.append(flatten_fields(fields, TRAIN_PROTOCOLS))
            spatial_test.append(flatten_fields(fields, TEST_PROTOCOLS))
            spatial_params.append(
                {"steps": smoothing_steps, "gamma": float(gamma)}
            )

    library["spatial_instant"] = {
        "train": np.asarray(spatial_train),
        "test": np.asarray(spatial_test),
        "params": spatial_params,
    }

    return library


def generate_observations(
    generator: str,
    seed: int,
    noise_sigma: float = 0.002,
    scale: float = 0.05,
):
    rng = np.random.default_rng(seed)
    observed = {}

    for name, source in PROTOCOLS.items():
        if generator == "diffusive":
            field = simulate_memory(source, beta=0.08, diffusion=0.18)
        elif generator == "local":
            field = simulate_memory(source, beta=0.10, diffusion=0.0)
        elif generator == "spatial_instant":
            field = spatial_instantaneous(
                source,
                gamma=0.45,
                smoothing_steps=3,
            )
        elif generator == "instant":
            field = source
        else:
            raise ValueError(f"unknown generator: {generator}")

        observed[name] = (
            scale * edge_field(field)
            + rng.normal(
                0.0,
                noise_sigma,
                size=(source.shape[0], len(EDGES)),
            )
        )

    train = np.concatenate([observed[name].ravel() for name in TRAIN_PROTOCOLS])
    test = np.concatenate([observed[name].ravel() for name in TEST_PROTOCOLS])
    return train, test


def fit_candidate(
    observed_train: np.ndarray,
    observed_test: np.ndarray,
    candidate: dict[str, object],
):
    train_matrix = np.asarray(candidate["train"])
    test_matrix = np.asarray(candidate["test"])

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

    return {
        "train_rmse": float(train_error[best]),
        "test_rmse": rmse(
            test_matrix[best] * scales[best],
            observed_test,
        ),
        "scale": float(scales[best]),
        "params": candidate["params"][best],
    }


def run_generator(
    generator: str,
    seeds: int,
    library,
) -> GeneratorSummary:
    rows = []

    for index in range(seeds):
        observed_train, observed_test = generate_observations(
            generator,
            seed=1000 + index,
        )
        fits = {
            name: fit_candidate(
                observed_train,
                observed_test,
                library[name],
            )
            for name in MODEL_ORDER
        }
        rows.append(fits)

    def mean_rmse(model: str) -> float:
        return float(np.mean([row[model]["test_rmse"] for row in rows]))

    beta = np.mean(
        [row["diffusive_memory"]["params"].get("beta", 0.0) for row in rows]
    )
    diffusion = np.mean(
        [row["diffusive_memory"]["params"].get("D", 0.0) for row in rows]
    )

    return GeneratorSummary(
        generator=generator,
        seeds=seeds,
        instant_test_rmse=mean_rmse("instant"),
        spatial_instant_test_rmse=mean_rmse("spatial_instant"),
        local_memory_test_rmse=mean_rmse("local_memory"),
        diffusive_memory_test_rmse=mean_rmse("diffusive_memory"),
        fitted_diffusive_beta_mean=float(beta),
        fitted_diffusive_D_mean=float(diffusion),
    )


def make_matched_present(prior_history: bool, steps: int = 60) -> np.ndarray:
    source = np.zeros((steps, 64), dtype=float)
    if prior_history:
        add_pulse(source, 5, 20, 1, 1, 1.0)

    # Both histories have identical present source conditions from t=40 onward.
    add_pulse(source, 40, 50, 4, 4, 0.7)
    return source


def matched_present_test(
    scale: float = 0.05,
    noise_sigma: float = 0.002,
) -> MatchedPresentSummary:
    history = make_matched_present(True)
    control = make_matched_present(False)

    true_delta = scale * (
        edge_field(simulate_memory(history, beta=0.08, diffusion=0.18))
        - edge_field(simulate_memory(control, beta=0.08, diffusion=0.18))
    )

    # Representative no-diffusion fit from the cross-protocol benchmark.
    local_delta = 0.0443 * (
        edge_field(simulate_memory(history, beta=0.16, diffusion=0.0))
        - edge_field(simulate_memory(control, beta=0.16, diffusion=0.0))
    )

    step = 40
    signal_rms = float(np.sqrt(np.mean(true_delta[step] ** 2)))

    if np.std(local_delta[step]) > 0.0:
        correlation = float(np.corrcoef(true_delta[step], local_delta[step])[0, 1])
    else:
        correlation = 0.0

    return MatchedPresentSummary(
        edge_rms_history_residual_t40=signal_rms,
        per_edge_noise_sigma=noise_sigma,
        rms_to_noise_ratio_t40=float(signal_rms / noise_sigma),
        instantaneous_prediction_rms_t40=0.0,
        local_memory_shape_correlation_t40=correlation,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seeds", type=int, default=12)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    library = build_candidate_library()
    generators = ("diffusive", "local", "spatial_instant", "instant")
    summaries = [
        run_generator(generator, args.seeds, library)
        for generator in generators
    ]
    matched = matched_present_test()

    if args.json:
        print(
            json.dumps(
                {
                    "generator_summaries": [asdict(summary) for summary in summaries],
                    "matched_present": asdict(matched),
                },
                indent=2,
            )
        )
        return

    print("SIM-04E SoCT memory injection / cross-protocol gate")
    print()
    print("test RMSE by data-generating mechanism")
    for summary in summaries:
        print(
            f"{summary.generator:16s} "
            f"instant={summary.instant_test_rmse:.5f} "
            f"spatial={summary.spatial_instant_test_rmse:.5f} "
            f"local={summary.local_memory_test_rmse:.5f} "
            f"diffusive={summary.diffusive_memory_test_rmse:.5f} "
            f"fit(beta,D)=({summary.fitted_diffusive_beta_mean:.3f},"
            f"{summary.fitted_diffusive_D_mean:.3f})"
        )

    print()
    print("matched-present / different-history test")
    print(
        f"edge RMS residual at t=40: {matched.edge_rms_history_residual_t40:.6f}"
    )
    print(
        f"per-edge noise sigma:       {matched.per_edge_noise_sigma:.6f}"
    )
    print(
        f"RMS/noise ratio:            {matched.rms_to_noise_ratio_t40:.3f}"
    )
    print(
        "local-memory shape corr:  "
        f"{matched.local_memory_shape_correlation_t40:.3f}"
    )


if __name__ == "__main__":
    main()
