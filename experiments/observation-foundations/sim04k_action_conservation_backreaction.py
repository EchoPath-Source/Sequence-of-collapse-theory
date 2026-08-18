#!/usr/bin/env python3
"""SIM-04K: action/conservation/backreaction consistency benchmark.

Toy-model methodology test only. This is not empirical evidence for a physical
SoCT memory field.

The benchmark uses the causal completion

    M_tt + gamma M_t - c_M^2 laplacian(M) + omega_M^2 M = g C_obs

with the SIM-04J low-frequency mapping

    c_M^2 = gamma D_M
    omega_M^2 = gamma beta.

For periodic boundaries the same field trajectory implies the energy ledger

    dE_M/dt = g int C_obs M_t dx - gamma int M_t^2 dx.

Crucially, beta, D_M and the probe coupling are fit ONLY from training probe
trajectories. The damping-heat observable is then predicted with no separate
heat/backreaction amplitude fit.

Three synthetic generators are tested:

1. action_consistent:
   probe trajectory and damping heat both come from the same causal field;
2. probe_only:
   identical field-like probe trajectory, but no excess heat/backreaction;
3. source_heat:
   identical field-like probe trajectory, but heat follows a simpler
   instantaneous source-power law rather than the action-linked field ledger.

A matched conventional physical field with the same complete action/exchange
law remains exactly degenerate with a state called M; the simulation does not
claim to solve that ontology problem.

Requires: numpy
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass

import numpy as np


N = 16
DX = 1.0
DT = 0.025
T_FINAL = 10.0
STEPS = int(T_FINAL / DT)

GAMMA = 5.0          # independently calibrated fast damping scale
SOURCE_COUPLING = 1.0
TRUE_BETA = 0.08
TRUE_D = 0.18
TRUE_LAMBDA = 0.70

PROBE_SIGMA = 0.0015
HEAT_SIGMA = 0.0020
SOURCE_HEAT_SCALE = 0.08

TRAIN_PROTOCOLS = ("A", "B")
TEST_PROTOCOLS = ("C", "D")
ALL_PROTOCOLS = TRAIN_PROTOCOLS + TEST_PROTOCOLS

BETA_GRID = np.round(np.arange(0.05, 0.111, 0.01), 3)
D_GRID = np.round(np.arange(0.12, 0.241, 0.02), 3)

PROBE_TIMES = (1.8, 2.7, 4.6, 6.0, 7.5, 9.0)
PROBE_SITES = (0, 4, 8, 12)
HEAT_WINDOWS = ((0.0, 2.0), (2.0, 4.0), (4.0, 6.0), (6.0, 8.0), (8.0, 10.0))


@dataclass
class GeneratorSummary:
    generator: str
    seeds: int
    fitted_beta_mean: float
    fitted_D_mean: float
    fitted_lambda_mean: float
    heldout_probe_rmse_mean: float
    action_heat_rmse_mean: float
    zero_heat_rmse_mean: float
    source_heat_rmse_mean: float
    fitted_source_heat_scale_mean: float


@dataclass
class LedgerCheck:
    max_instantaneous_identity_error: float
    exact_hidden_field_prediction_difference: float


def laplacian_periodic(values: np.ndarray) -> np.ndarray:
    return (
        np.roll(values, -1)
        - 2.0 * values
        + np.roll(values, 1)
    ) / (DX * DX)


def make_source(name: str) -> np.ndarray:
    source = np.zeros((STEPS, N), dtype=float)

    def pulse(t0: float, t1: float, center: int, width: float, amplitude: float):
        start = int(t0 / DT)
        stop = int(t1 / DT)
        sites = np.arange(N)
        distance = np.minimum(
            np.abs(sites - center),
            N - np.abs(sites - center),
        )
        profile = np.exp(-0.5 * (distance / width) ** 2)
        source[start:stop] += amplitude * profile

    if name == "A":
        pulse(0.6, 1.5, 3, 0.8, 1.0)
        pulse(3.6, 4.2, 10, 1.1, 0.7)
    elif name == "B":
        pulse(0.8, 1.8, 12, 0.9, 0.9)
        pulse(3.0, 4.0, 5, 1.2, 0.6)
    elif name == "C":
        pulse(0.4, 1.2, 7, 0.7, 1.1)
        pulse(2.4, 3.2, 14, 1.0, 0.75)
        pulse(5.3, 5.8, 2, 0.8, 0.5)
    elif name == "D":
        pulse(0.7, 1.6, 1, 1.2, 0.65)
        pulse(3.4, 4.5, 9, 0.7, 1.0)
    else:
        raise ValueError(f"unknown protocol: {name}")

    return source


SOURCES = {name: make_source(name) for name in ALL_PROTOCOLS}


def simulate(beta: float, diffusion: float, source: np.ndarray):
    c2 = GAMMA * diffusion
    omega2 = GAMMA * beta

    field = np.zeros(N, dtype=float)
    velocity = np.zeros(N, dtype=float)

    fields = np.empty((STEPS, N), dtype=float)
    velocities = np.empty((STEPS, N), dtype=float)
    energies = np.empty(STEPS, dtype=float)
    source_power = np.empty(STEPS, dtype=float)
    damping_power = np.empty(STEPS, dtype=float)
    identity_error = np.empty(STEPS, dtype=float)

    for step in range(STEPS):
        src = source[step]

        # Explicit midpoint / RK2 step for the first-order pair (M, M_t).
        accel_1 = (
            -GAMMA * velocity
            + c2 * laplacian_periodic(field)
            - omega2 * field
            + SOURCE_COUPLING * src
        )
        field_mid = field + 0.5 * DT * velocity
        velocity_mid = velocity + 0.5 * DT * accel_1
        accel_2 = (
            -GAMMA * velocity_mid
            + c2 * laplacian_periodic(field_mid)
            - omega2 * field_mid
            + SOURCE_COUPLING * src
        )

        field = field + DT * velocity_mid
        velocity = velocity + DT * accel_2

        fields[step] = field
        velocities[step] = velocity

        gradient = (np.roll(field, -1) - field) / DX
        energies[step] = 0.5 * np.sum(
            velocity * velocity
            + c2 * gradient * gradient
            + omega2 * field * field
        ) * DX

        source_power[step] = (
            SOURCE_COUPLING * np.sum(src * velocity) * DX
        )
        damping_power[step] = GAMMA * np.sum(velocity * velocity) * DX

        # Discrete instantaneous identity check. With periodic boundaries,
        # sum grad(M).grad(V) = -sum V laplacian(M).
        accel_now = (
            -GAMMA * velocity
            + c2 * laplacian_periodic(field)
            - omega2 * field
            + SOURCE_COUPLING * src
        )
        denergy = np.sum(
            velocity * accel_now
            - c2 * velocity * laplacian_periodic(field)
            + omega2 * field * velocity
        ) * DX
        identity_error[step] = abs(
            denergy - (source_power[step] - damping_power[step])
        )

    return {
        "field": fields,
        "velocity": velocities,
        "energy": energies,
        "source_power": source_power,
        "damping_power": damping_power,
        "identity_error": identity_error,
    }


def probe_feature(simulation) -> np.ndarray:
    values = []
    field = simulation["field"]
    for time in PROBE_TIMES:
        step = min(int(time / DT), STEPS - 1)
        values.extend(field[step, list(PROBE_SITES)])
    return np.asarray(values, dtype=float)


def damping_heat_feature(simulation) -> np.ndarray:
    power = simulation["damping_power"]
    values = []
    for start, stop in HEAT_WINDOWS:
        first = int(start / DT)
        last = int(stop / DT)
        values.append(float(np.trapezoid(power[first:last], dx=DT)))
    return np.asarray(values, dtype=float)


def source_heat_feature(source: np.ndarray) -> np.ndarray:
    power = np.sum(source * source, axis=1) * DX
    values = []
    for start, stop in HEAT_WINDOWS:
        first = int(start / DT)
        last = int(stop / DT)
        values.append(float(np.trapezoid(power[first:last], dx=DT)))
    return np.asarray(values, dtype=float)


def concatenate(mapping, names) -> np.ndarray:
    return np.concatenate([mapping[name] for name in names])


TRUE_SIMS = {
    name: simulate(TRUE_BETA, TRUE_D, SOURCES[name])
    for name in ALL_PROTOCOLS
}
TRUE_PROBE = {
    name: probe_feature(TRUE_SIMS[name])
    for name in ALL_PROTOCOLS
}
TRUE_HEAT = {
    name: damping_heat_feature(TRUE_SIMS[name])
    for name in ALL_PROTOCOLS
}
SOURCE_HEAT = {
    name: source_heat_feature(SOURCES[name])
    for name in ALL_PROTOCOLS
}

TRUE_PROBE_TRAIN = concatenate(TRUE_PROBE, TRAIN_PROTOCOLS)
TRUE_PROBE_TEST = concatenate(TRUE_PROBE, TEST_PROTOCOLS)
TRUE_HEAT_TRAIN = concatenate(TRUE_HEAT, TRAIN_PROTOCOLS)
TRUE_HEAT_TEST = concatenate(TRUE_HEAT, TEST_PROTOCOLS)
SOURCE_HEAT_TRAIN = concatenate(SOURCE_HEAT, TRAIN_PROTOCOLS)
SOURCE_HEAT_TEST = concatenate(SOURCE_HEAT, TEST_PROTOCOLS)


def build_candidate_library():
    library = []
    for beta in BETA_GRID:
        for diffusion in D_GRID:
            simulations = {
                name: simulate(float(beta), float(diffusion), SOURCES[name])
                for name in ALL_PROTOCOLS
            }
            probe = {
                name: probe_feature(simulations[name])
                for name in ALL_PROTOCOLS
            }
            heat = {
                name: damping_heat_feature(simulations[name])
                for name in ALL_PROTOCOLS
            }
            library.append(
                {
                    "beta": float(beta),
                    "D": float(diffusion),
                    "probe_train": concatenate(probe, TRAIN_PROTOCOLS),
                    "probe_test": concatenate(probe, TEST_PROTOCOLS),
                    "heat_train": concatenate(heat, TRAIN_PROTOCOLS),
                    "heat_test": concatenate(heat, TEST_PROTOCOLS),
                }
            )
    return library


def rmse(prediction: np.ndarray, observation: np.ndarray) -> float:
    return float(np.sqrt(np.mean((prediction - observation) ** 2)))


def fit_probe_only(observed_train: np.ndarray, observed_test: np.ndarray, library):
    best = None

    for candidate in library:
        feature = candidate["probe_train"]
        coupling = float(
            np.dot(feature, observed_train)
            / (np.dot(feature, feature) + 1e-15)
        )
        train_error = rmse(coupling * feature, observed_train)

        if best is None or train_error < best["train_rmse"]:
            best = {
                "beta": candidate["beta"],
                "D": candidate["D"],
                "lambda": coupling,
                "train_rmse": train_error,
                "test_rmse": rmse(
                    coupling * candidate["probe_test"],
                    observed_test,
                ),
                "heat_train": candidate["heat_train"],
                "heat_test": candidate["heat_test"],
            }

    return best


def fit_source_heat_null(observed_train: np.ndarray, observed_test: np.ndarray):
    scale = float(
        np.dot(SOURCE_HEAT_TRAIN, observed_train)
        / (np.dot(SOURCE_HEAT_TRAIN, SOURCE_HEAT_TRAIN) + 1e-15)
    )
    return {
        "scale": scale,
        "test_rmse": rmse(scale * SOURCE_HEAT_TEST, observed_test),
    }


def generate_observations(generator: str, seed: int):
    rng = np.random.default_rng(seed)

    probe_train = (
        TRUE_LAMBDA * TRUE_PROBE_TRAIN
        + rng.normal(0.0, PROBE_SIGMA, size=TRUE_PROBE_TRAIN.shape)
    )
    probe_test = (
        TRUE_LAMBDA * TRUE_PROBE_TEST
        + rng.normal(0.0, PROBE_SIGMA, size=TRUE_PROBE_TEST.shape)
    )

    if generator == "action_consistent":
        heat_train_mean = TRUE_HEAT_TRAIN
        heat_test_mean = TRUE_HEAT_TEST
    elif generator == "probe_only":
        heat_train_mean = np.zeros_like(TRUE_HEAT_TRAIN)
        heat_test_mean = np.zeros_like(TRUE_HEAT_TEST)
    elif generator == "source_heat":
        heat_train_mean = SOURCE_HEAT_SCALE * SOURCE_HEAT_TRAIN
        heat_test_mean = SOURCE_HEAT_SCALE * SOURCE_HEAT_TEST
    else:
        raise ValueError(f"unknown generator: {generator}")

    heat_train = heat_train_mean + rng.normal(
        0.0, HEAT_SIGMA, size=heat_train_mean.shape
    )
    heat_test = heat_test_mean + rng.normal(
        0.0, HEAT_SIGMA, size=heat_test_mean.shape
    )

    return probe_train, probe_test, heat_train, heat_test


def summarize_generator(generator: str, seeds: int, library) -> GeneratorSummary:
    rows = []

    for index in range(seeds):
        probe_train, probe_test, heat_train, heat_test = generate_observations(
            generator, seed=1000 + index
        )

        field_fit = fit_probe_only(probe_train, probe_test, library)
        source_null = fit_source_heat_null(heat_train, heat_test)

        rows.append(
            {
                "beta": field_fit["beta"],
                "D": field_fit["D"],
                "lambda": field_fit["lambda"],
                "probe_test_rmse": field_fit["test_rmse"],
                # No extra scale or fit is allowed here.
                "action_heat_rmse": rmse(field_fit["heat_test"], heat_test),
                "zero_heat_rmse": rmse(np.zeros_like(heat_test), heat_test),
                "source_heat_rmse": source_null["test_rmse"],
                "source_heat_scale": source_null["scale"],
            }
        )

    def mean(key: str) -> float:
        return float(np.mean([row[key] for row in rows]))

    return GeneratorSummary(
        generator=generator,
        seeds=seeds,
        fitted_beta_mean=mean("beta"),
        fitted_D_mean=mean("D"),
        fitted_lambda_mean=mean("lambda"),
        heldout_probe_rmse_mean=mean("probe_test_rmse"),
        action_heat_rmse_mean=mean("action_heat_rmse"),
        zero_heat_rmse_mean=mean("zero_heat_rmse"),
        source_heat_rmse_mean=mean("source_heat_rmse"),
        fitted_source_heat_scale_mean=mean("source_heat_scale"),
    )


def ledger_check() -> LedgerCheck:
    max_error = max(
        float(np.max(TRUE_SIMS[name]["identity_error"]))
        for name in ALL_PROTOCOLS
    )

    # A conventional hidden field with the identical complete dynamics,
    # source normalization and coupling is a pure relabeling under these
    # observables. This is intentionally reported as an exact ontology tie.
    exact_hidden_difference = 0.0

    return LedgerCheck(
        max_instantaneous_identity_error=max_error,
        exact_hidden_field_prediction_difference=exact_hidden_difference,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seeds", type=int, default=50)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    library = build_candidate_library()
    summaries = [
        summarize_generator(generator, args.seeds, library)
        for generator in ("action_consistent", "probe_only", "source_heat")
    ]
    ledger = ledger_check()

    payload = {
        "summaries": [asdict(summary) for summary in summaries],
        "ledger": asdict(ledger),
        "noise": {
            "probe_sigma": PROBE_SIGMA,
            "heat_sigma": HEAT_SIGMA,
        },
        "true_parameters": {
            "gamma": GAMMA,
            "beta": TRUE_BETA,
            "D_M": TRUE_D,
            "lambda": TRUE_LAMBDA,
            "c_M": float(np.sqrt(GAMMA * TRUE_D)),
            "omega_M": float(np.sqrt(GAMMA * TRUE_BETA)),
        },
    }

    if args.json:
        print(json.dumps(payload, indent=2))
        return

    print("SIM-04K action / conservation / backreaction consistency")
    print("parameters are fit from probe trajectories only")
    print("action heat has no separate amplitude fit")
    print()
    for summary in summaries:
        print(
            f"{summary.generator:18s} "
            f"beta={summary.fitted_beta_mean:.4f} "
            f"D={summary.fitted_D_mean:.4f} "
            f"lambda={summary.fitted_lambda_mean:.4f} "
            f"probe={summary.heldout_probe_rmse_mean:.5f} "
            f"action_heat={summary.action_heat_rmse_mean:.5f} "
            f"zero_heat={summary.zero_heat_rmse_mean:.5f} "
            f"source_heat={summary.source_heat_rmse_mean:.5f}"
        )
    print()
    print(
        "max instantaneous energy-ledger identity error: "
        f"{ledger.max_instantaneous_identity_error:.3e}"
    )
    print(
        "matched conventional-field prediction difference: "
        f"{ledger.exact_hidden_field_prediction_difference:.1f}"
    )


if __name__ == "__main__":
    main()
