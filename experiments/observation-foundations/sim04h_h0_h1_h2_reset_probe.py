#!/usr/bin/env python3
"""SIM-04H: H0/H1/H2 complete-reset-and-probe benchmark.

Toy-model methodology test only. This is not empirical evidence for SoCT.

H0:
    Complete standard unitary quantum record model. After an exact reset of
    S, detector, and all modeled environment fragments, a fresh probe has no
    history-dependent residual.

H1:
    The same standard model summarized by an operational record-production
    quantity, but with no additional physical state. After an exact reset it
    has the same post-reset physical prediction as H0.

H2:
    H0/H1 plus an additional field M sourced by retained record production:
        dM/dt = alpha*C_obs - beta*M + D_M*Laplacian(M)
    M is not erased by the ordinary S/D/E reset and shifts a fresh probe phase.

The benchmark:
  1. derives retained-record source pulses from an explicit five-qubit unitary
     S-D-E model;
  2. globally resets all ordinary modeled quantum degrees of freedom;
  3. probes fresh qubits at multiple sites and wait times;
  4. fits beta, D_M, and one probe-coupling scale on protocols A/B;
  5. scores held-out protocols C/D;
  6. tests exact-reset H0 data and an ordinary local-reservoir null;
  7. records an exact ontology degeneracy: a conventional hidden field with
     the same source/decay/diffusion/coupling law is observationally identical
     to M under this restricted protocol.

Requires:
    numpy
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass

import numpy as np


# ---------------------------------------------------------------------------
# Explicit standard quantum record model: S, D, E1, E2, E3
# ---------------------------------------------------------------------------

NQ = 5
DIM = 2 ** NQ
I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)


def kron_all(ops):
    out = ops[0]
    for op in ops[1:]:
        out = np.kron(out, op)
    return out


def controlled_gate(control: int, target: int, unitary: np.ndarray) -> np.ndarray:
    matrix = np.zeros((DIM, DIM), dtype=complex)
    for idx in range(DIM):
        bits = [(idx >> (NQ - 1 - k)) & 1 for k in range(NQ)]
        if bits[control] == 0:
            matrix[idx, idx] = 1.0
            continue

        source_bit = bits[target]
        for target_bit in (0, 1):
            amplitude = unitary[target_bit, source_bit]
            if abs(amplitude) == 0.0:
                continue
            out_bits = bits.copy()
            out_bits[target] = target_bit
            out_idx = 0
            for bit in out_bits:
                out_idx = (out_idx << 1) | bit
            matrix[out_idx, idx] += amplitude
    return matrix


def ry(angle: float) -> np.ndarray:
    return np.array(
        [
            [math.cos(angle / 2.0), -math.sin(angle / 2.0)],
            [math.sin(angle / 2.0), math.cos(angle / 2.0)],
        ],
        dtype=complex,
    )


def initial_record_state() -> np.ndarray:
    """|+>_S |0000>_{D,E1,E2,E3}."""
    state = np.zeros(DIM, dtype=complex)
    state[0] = 1.0 / math.sqrt(2.0)
    state[16] = 1.0 / math.sqrt(2.0)
    return state


def partial_measurement(theta: float) -> np.ndarray:
    return controlled_gate(0, 1, ry(2.0 * theta))


CNOTS = [controlled_gate(1, 2 + index, X) for index in range(3)]


def reduced_density(state: np.ndarray, keep) -> np.ndarray:
    keep = list(keep)
    rest = [index for index in range(NQ) if index not in keep]
    tensor = state.reshape([2] * NQ)
    reordered = np.transpose(tensor, keep + rest)
    matrix = reordered.reshape(2 ** len(keep), 2 ** len(rest))
    return matrix @ matrix.conj().T


def entropy(rho: np.ndarray) -> float:
    values = np.linalg.eigvalsh((rho + rho.conj().T) / 2.0)
    values = values[values > 1e-12]
    return float(-np.sum(values * np.log2(values)))


def mutual_information(state: np.ndarray, a, b) -> float:
    rho_a = reduced_density(state, a)
    rho_b = reduced_density(state, b)
    rho_ab = reduced_density(state, list(a) + list(b))
    return entropy(rho_a) + entropy(rho_b) - entropy(rho_ab)


def retained_record_score(
    theta: float,
    fragments: int,
    erase: bool = False,
) -> float:
    """Retained environmental record after local unmeasurement.

    The score is the sum of I(S:E_k) after:
      U_SD -> copies D->E -> optional copy erasure -> U_SD^dagger.

    If records are fully erased before unmeasurement, the score returns to
    numerical zero. No SoCT term is present here.
    """
    state = initial_record_state()
    u_sd = partial_measurement(theta)
    state = u_sd @ state

    for index in range(fragments):
        state = CNOTS[index] @ state

    if erase:
        for index in reversed(range(fragments)):
            state = CNOTS[index] @ state

    state = u_sd.conj().T @ state

    return float(
        sum(mutual_information(state, [0], [2 + index]) for index in range(3))
    )


# ---------------------------------------------------------------------------
# Observation-derived source histories on a hidden seven-site chain
# ---------------------------------------------------------------------------

SITES = 7
HISTORY_STEPS = 30
WAITS = (0, 3, 7, 12)
TRAIN_PROTOCOLS = ("A", "B")
TEST_PROTOCOLS = ("C", "D")

ADJACENCY = np.zeros((SITES, SITES), dtype=float)
for index in range(SITES - 1):
    ADJACENCY[index, index + 1] = 1.0
    ADJACENCY[index + 1, index] = 1.0

DEGREE = ADJACENCY.sum(axis=1)
NEIGHBOR_AVERAGE = np.zeros_like(ADJACENCY)
for index in range(SITES):
    if DEGREE[index] > 0.0:
        NEIGHBOR_AVERAGE[index] = ADJACENCY[index] / DEGREE[index]
LAPLACIAN = NEIGHBOR_AVERAGE - np.eye(SITES)


# time, site, theta, environment fragments, erase records before unmeasurement
PROTOCOL_EVENTS = {
    "A": [
        (3, 1, 0.80, 1, False),
        (10, 1, 1.00, 3, False),
        (18, 4, 0.60, 1, False),
    ],
    "B": [
        (2, 5, 1.10, 1, False),
        (8, 2, 0.70, 3, False),
        (15, 5, 0.90, 1, False),
        (22, 0, 0.50, 1, False),
    ],
    "C": [
        (4, 0, 0.65, 1, False),
        (9, 3, 1.15, 3, False),
        (17, 6, 0.75, 1, False),
    ],
    # First strong interaction is deliberately erased and therefore should
    # not source retained-record memory.
    "D": [
        (3, 2, 1.10, 3, True),
        (11, 2, 1.00, 3, False),
        (19, 5, 0.55, 1, False),
    ],
}


def make_source_history(name: str) -> np.ndarray:
    source = np.zeros((HISTORY_STEPS, SITES), dtype=float)
    for step, site, theta, fragments, erase in PROTOCOL_EVENTS[name]:
        source[step, site] += retained_record_score(theta, fragments, erase)
    return source


SOURCES = {name: make_source_history(name) for name in PROTOCOL_EVENTS}


def simulate_field(
    source: np.ndarray,
    beta: float,
    diffusion: float,
) -> np.ndarray:
    state = np.zeros(SITES, dtype=float)
    for step in range(source.shape[0]):
        state = (
            state
            + source[step]
            - beta * state
            + diffusion * (LAPLACIAN @ state)
        )
    return state


def decay_field(
    state: np.ndarray,
    wait: int,
    beta: float,
    diffusion: float,
) -> np.ndarray:
    out = state.copy()
    for _ in range(wait):
        out = out - beta * out + diffusion * (LAPLACIAN @ out)
    return out


def probe_features(names, beta: float, diffusion: float) -> np.ndarray:
    values = []
    for name in names:
        terminal = simulate_field(SOURCES[name], beta, diffusion)
        for wait in WAITS:
            field = decay_field(terminal, wait, beta, diffusion)
            values.extend(field.tolist())
    return np.asarray(values, dtype=float)


# ---------------------------------------------------------------------------
# Fresh-probe measurement after exact reset
# ---------------------------------------------------------------------------

TRUE_BETA = 0.08
TRUE_DIFFUSION = 0.15
TRUE_LAMBDA = 3.00
SHOTS = 12_000

BETA_GRID = np.round(np.arange(0.04, 0.141, 0.01), 2)
DIFFUSION_GRID = np.round(np.arange(0.0, 0.251, 0.025), 3)
LAMBDA_GRID = np.arange(0.0, 5.01, 0.05)


def y_expectation(memory: np.ndarray, coupling: float) -> np.ndarray:
    """Fresh |+> probe with phase phi=lambda*M, measured in Y."""
    return np.sin(coupling * memory)


def sample_y(expectation: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    probability_plus = (1.0 + np.clip(expectation, -1.0, 1.0)) / 2.0
    plus_counts = rng.binomial(SHOTS, probability_plus)
    return 2.0 * plus_counts / SHOTS - 1.0


TRUE_TRAIN = probe_features(TRAIN_PROTOCOLS, TRUE_BETA, TRUE_DIFFUSION)
TRUE_TEST = probe_features(TEST_PROTOCOLS, TRUE_BETA, TRUE_DIFFUSION)


def generate_observations(generator: str, seed: int):
    rng = np.random.default_rng(seed)

    if generator == "H2_diffusive":
        train_mean = y_expectation(TRUE_TRAIN, TRUE_LAMBDA)
        test_mean = y_expectation(TRUE_TEST, TRUE_LAMBDA)

    elif generator == "H0_exact_reset":
        # H0 and H1 have identical post-reset physical predictions.
        train_mean = np.zeros_like(TRUE_TRAIN)
        test_mean = np.zeros_like(TRUE_TEST)

    elif generator == "ordinary_local_reservoir":
        # Conventional unreset local state: history dependent but D=0.
        train_local = probe_features(TRAIN_PROTOCOLS, TRUE_BETA, 0.0)
        test_local = probe_features(TEST_PROTOCOLS, TRUE_BETA, 0.0)
        train_mean = y_expectation(train_local, TRUE_LAMBDA)
        test_mean = y_expectation(test_local, TRUE_LAMBDA)

    else:
        raise ValueError(f"unknown generator: {generator}")

    return sample_y(train_mean, rng), sample_y(test_mean, rng)


def rmse(prediction: np.ndarray, observed: np.ndarray) -> float:
    return float(np.sqrt(np.mean((prediction - observed) ** 2)))


CANDIDATES = []
for beta in BETA_GRID:
    for diffusion in DIFFUSION_GRID:
        CANDIDATES.append(
            (
                float(beta),
                float(diffusion),
                probe_features(TRAIN_PROTOCOLS, beta, diffusion),
                probe_features(TEST_PROTOCOLS, beta, diffusion),
            )
        )

LOCAL_CANDIDATES = [
    (
        float(beta),
        probe_features(TRAIN_PROTOCOLS, beta, 0.0),
        probe_features(TEST_PROTOCOLS, beta, 0.0),
    )
    for beta in BETA_GRID
]


def fit_h2(observed_train: np.ndarray, observed_test: np.ndarray):
    best = None

    for beta, diffusion, train_feature, test_feature in CANDIDATES:
        predictions = np.sin(LAMBDA_GRID[:, None] * train_feature[None, :])
        errors = np.sqrt(
            np.mean((predictions - observed_train[None, :]) ** 2, axis=1)
        )
        index = int(np.argmin(errors))

        row = {
            "beta": beta,
            "D": diffusion,
            "lambda": float(LAMBDA_GRID[index]),
            "train_rmse": float(errors[index]),
            "test_rmse": rmse(
                np.sin(LAMBDA_GRID[index] * test_feature),
                observed_test,
            ),
        }
        if best is None or row["train_rmse"] < best["train_rmse"]:
            best = row

    return best


def fit_local_reservoir(
    observed_train: np.ndarray,
    observed_test: np.ndarray,
):
    best = None

    for beta, train_feature, test_feature in LOCAL_CANDIDATES:
        predictions = np.sin(LAMBDA_GRID[:, None] * train_feature[None, :])
        errors = np.sqrt(
            np.mean((predictions - observed_train[None, :]) ** 2, axis=1)
        )
        index = int(np.argmin(errors))
        row = {
            "beta": beta,
            "lambda": float(LAMBDA_GRID[index]),
            "train_rmse": float(errors[index]),
            "test_rmse": rmse(
                np.sin(LAMBDA_GRID[index] * test_feature),
                observed_test,
            ),
        }
        if best is None or row["train_rmse"] < best["train_rmse"]:
            best = row

    return best


def bic(rss: float, n: int, parameters: int) -> float:
    return float(n * np.log(rss / n + 1e-30) + parameters * np.log(n))


@dataclass
class GeneratorSummary:
    generator: str
    seeds: int
    h0_h1_test_rmse_mean: float
    h2_test_rmse_mean: float
    local_reservoir_test_rmse_mean: float
    fitted_h2_beta_mean: float
    fitted_h2_D_mean: float
    fitted_h2_lambda_mean: float
    delta_bic_h2_minus_h0_mean: float
    delta_bic_h2_minus_local_mean: float


def run_generator(generator: str, seeds: int) -> GeneratorSummary:
    rows = []

    for index in range(seeds):
        train, test = generate_observations(generator, 2000 + index)
        h2 = fit_h2(train, test)
        local = fit_local_reservoir(train, test)

        zero_test = rmse(np.zeros_like(test), test)

        h2_train_feature = probe_features(
            TRAIN_PROTOCOLS,
            h2["beta"],
            h2["D"],
        )
        h2_train_prediction = np.sin(h2["lambda"] * h2_train_feature)

        local_train_feature = probe_features(
            TRAIN_PROTOCOLS,
            local["beta"],
            0.0,
        )
        local_train_prediction = np.sin(
            local["lambda"] * local_train_feature
        )

        rss_h0 = float(np.sum(train ** 2))
        rss_h2 = float(np.sum((h2_train_prediction - train) ** 2))
        rss_local = float(np.sum((local_train_prediction - train) ** 2))

        rows.append(
            {
                "zero_test": zero_test,
                "h2_test": h2["test_rmse"],
                "local_test": local["test_rmse"],
                "beta": h2["beta"],
                "D": h2["D"],
                "lambda": h2["lambda"],
                "delta_bic_h2_h0": (
                    bic(rss_h2, len(train), 3)
                    - bic(rss_h0, len(train), 0)
                ),
                "delta_bic_h2_local": (
                    bic(rss_h2, len(train), 3)
                    - bic(rss_local, len(train), 2)
                ),
            }
        )

    def mean(key: str) -> float:
        return float(np.mean([row[key] for row in rows]))

    return GeneratorSummary(
        generator=generator,
        seeds=seeds,
        h0_h1_test_rmse_mean=mean("zero_test"),
        h2_test_rmse_mean=mean("h2_test"),
        local_reservoir_test_rmse_mean=mean("local_test"),
        fitted_h2_beta_mean=mean("beta"),
        fitted_h2_D_mean=mean("D"),
        fitted_h2_lambda_mean=mean("lambda"),
        delta_bic_h2_minus_h0_mean=mean("delta_bic_h2_h0"),
        delta_bic_h2_minus_local_mean=mean("delta_bic_h2_local"),
    )


def source_table():
    table = {}
    for name, events in PROTOCOL_EVENTS.items():
        rows = []
        for step, site, theta, fragments, erase in events:
            rows.append(
                {
                    "step": step,
                    "site": site,
                    "theta": theta,
                    "fragments": fragments,
                    "erase": erase,
                    "retained_record_score": retained_record_score(
                        theta,
                        fragments,
                        erase,
                    ),
                }
            )
        table[name] = rows
    return table


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seeds", type=int, default=24)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    generators = (
        "H2_diffusive",
        "H0_exact_reset",
        "ordinary_local_reservoir",
    )
    summaries = [run_generator(name, args.seeds) for name in generators]

    # H1 is a descriptive summary only and has no independent post-reset
    # physical state, so it is exactly prediction-equivalent to H0 here.
    h0_h1_prediction_difference = 0.0

    # Exact ontology degeneracy: if a conventional hidden field is assigned
    # the same source, beta, diffusion, and probe coupling as M, all restricted
    # predictions are identical by construction.
    conventional_diffusive_reservoir = y_expectation(
        TRUE_TEST,
        TRUE_LAMBDA,
    )
    soct_m_prediction = y_expectation(TRUE_TEST, TRUE_LAMBDA)
    hidden_field_equivalence_max_abs = float(
        np.max(np.abs(conventional_diffusive_reservoir - soct_m_prediction))
    )

    output = {
        "summaries": [asdict(summary) for summary in summaries],
        "h0_h1_post_reset_prediction_max_abs_difference": (
            h0_h1_prediction_difference
        ),
        "hidden_diffusive_field_equivalence_max_abs_difference": (
            hidden_field_equivalence_max_abs
        ),
        "true_parameters": {
            "beta": TRUE_BETA,
            "D_M": TRUE_DIFFUSION,
            "lambda": TRUE_LAMBDA,
            "shots_per_probe_point": SHOTS,
        },
        "protocol_sources": source_table(),
    }

    if args.json:
        print(json.dumps(output, indent=2))
        return

    print("SIM-04H H0/H1/H2 complete-reset-and-probe benchmark")
    print()
    for summary in summaries:
        print(
            f"{summary.generator:26s} "
            f"H0/H1={summary.h0_h1_test_rmse_mean:.5f} "
            f"local={summary.local_reservoir_test_rmse_mean:.5f} "
            f"H2={summary.h2_test_rmse_mean:.5f} "
            f"fit(beta,D,lambda)=("
            f"{summary.fitted_h2_beta_mean:.3f},"
            f"{summary.fitted_h2_D_mean:.3f},"
            f"{summary.fitted_h2_lambda_mean:.3f}) "
            f"dBIC(H2-H0)={summary.delta_bic_h2_minus_h0_mean:.1f}"
        )

    print()
    print(
        "H0 vs H1 post-reset max prediction difference:",
        h0_h1_prediction_difference,
    )
    print(
        "H2 vs identically parameterized conventional hidden field "
        "max prediction difference:",
        hidden_field_equivalence_max_abs,
    )


if __name__ == "__main__":
    main()
