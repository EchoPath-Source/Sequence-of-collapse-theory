#!/usr/bin/env python3
"""SIM-04L: local source/field/bath exchange continuity benchmark.

Toy-model methodology test only. This is not empirical evidence for SoCT.

The candidate causal memory equation is

    M_tt + gamma M_t - c_M^2 Laplacian(M) + omega_M^2 M = g C_obs

with

    c_M^2 = gamma D_M
    omega_M^2 = gamma beta.

The local flat-background energy ledger is

    d_t rho_M + div S_M = g C_obs M_t - gamma M_t^2.

Field parameters are fit ONLY from probe trajectories. The same fitted field
then predicts held-out, spatially resolved source-work and bath-gain maps with
no extra exchange amplitude.

Generators:
  action_local    : correct local source/bath exchange;
  global_scramble : same global exchange totals, wrong spatial deposition;
  no_exchange     : field-like probe signal, no excess exchange channels.

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

GAMMA = 5.0
SOURCE_COUPLING = 1.0
TRUE_BETA = 0.08
TRUE_D = 0.18
TRUE_LAMBDA = 0.70
PROBE_SIGMA = 0.0015
EXCHANGE_SIGMA = 0.0015

TRAIN_PROTOCOLS = ("A", "B")
TEST_PROTOCOLS = ("C", "D")
ALL_PROTOCOLS = TRAIN_PROTOCOLS + TEST_PROTOCOLS

BETA_GRID = np.round(np.arange(0.05, 0.111, 0.01), 3)
D_GRID = np.round(np.arange(0.12, 0.241, 0.02), 3)

PROBE_TIMES = (1.8, 2.7, 4.6, 6.0, 7.5, 9.0)
PROBE_SITES = (0, 4, 8, 12)
EXCHANGE_WINDOWS = ((0.0, 2.0), (2.0, 4.0), (4.0, 6.0), (6.0, 8.0), (8.0, 10.0))


@dataclass
class GeneratorSummary:
    generator: str
    seeds: int
    fitted_beta_mean: float
    fitted_D_mean: float
    fitted_lambda_mean: float
    probe_test_rmse_mean: float
    action_source_local_rmse_mean: float
    action_bath_local_rmse_mean: float
    zero_source_local_rmse_mean: float
    zero_bath_local_rmse_mean: float
    action_source_global_rmse_mean: float
    action_bath_global_rmse_mean: float


@dataclass
class IdentitySummary:
    max_local_continuity_error: float
    exact_matched_hidden_sector_prediction_difference: float


def laplacian_periodic(values: np.ndarray) -> np.ndarray:
    return (
        np.roll(values, -1)
        - 2.0 * values
        + np.roll(values, 1)
    ) / (DX * DX)


def make_source(name: str) -> np.ndarray:
    source = np.zeros((STEPS, N), dtype=float)
    sites = np.arange(N)

    def pulse(t0: float, t1: float, center: int, width: float, amplitude: float):
        distance = np.minimum(np.abs(sites - center), N - np.abs(sites - center))
        profile = np.exp(-0.5 * (distance / width) ** 2)
        source[int(t0 / DT):int(t1 / DT)] += amplitude * profile

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
        raise ValueError(name)
    return source


SOURCES = {name: make_source(name) for name in ALL_PROTOCOLS}


def simulate(beta: float, diffusion: float, source: np.ndarray):
    c2 = GAMMA * diffusion
    omega2 = GAMMA * beta
    field = np.zeros(N)
    velocity = np.zeros(N)

    fields = np.empty((STEPS, N))
    source_power = np.empty((STEPS, N))
    bath_power = np.empty((STEPS, N))
    local_residual = np.empty((STEPS, N))

    for step in range(STEPS):
        src = source[step]
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

        accel_now = (
            -GAMMA * velocity
            + c2 * laplacian_periodic(field)
            - omega2 * field
            + SOURCE_COUPLING * src
        )

        dm_plus = np.roll(field, -1) - field
        dm_minus = field - np.roll(field, 1)
        gradient_energy_rate = c2 / (2.0 * DX * DX) * (
            dm_plus * (np.roll(velocity, -1) - velocity)
            + dm_minus * (velocity - np.roll(velocity, 1))
        )
        d_rho_dt = (
            velocity * accel_now
            + omega2 * field * velocity
            + gradient_energy_rate
        )

        flux_plus = -c2 / (2.0 * DX) * dm_plus * (
            velocity + np.roll(velocity, -1)
        )
        div_flux = (flux_plus - np.roll(flux_plus, 1)) / DX

        src_power = SOURCE_COUPLING * src * velocity
        damp_power = GAMMA * velocity * velocity

        fields[step] = field
        source_power[step] = src_power
        bath_power[step] = damp_power
        local_residual[step] = d_rho_dt + div_flux - (src_power - damp_power)

    return {
        "field": fields,
        "source_power": source_power,
        "bath_power": bath_power,
        "local_residual": local_residual,
    }


def probe_feature(simulation) -> np.ndarray:
    values = []
    for time in PROBE_TIMES:
        step = min(int(time / DT), STEPS - 1)
        values.extend(simulation["field"][step, list(PROBE_SITES)])
    return np.asarray(values)


def exchange_feature(power: np.ndarray) -> np.ndarray:
    values = []
    for start, stop in EXCHANGE_WINDOWS:
        first = int(start / DT)
        last = int(stop / DT)
        values.extend(np.trapezoid(power[first:last], dx=DT, axis=0).tolist())
    return np.asarray(values)


def concatenate(mapping, names) -> np.ndarray:
    return np.concatenate([mapping[name] for name in names])


def global_totals(local_feature: np.ndarray) -> np.ndarray:
    return local_feature.reshape(-1, N).sum(axis=1)


def scramble_sites(local_feature: np.ndarray, shift: int = 3) -> np.ndarray:
    return np.roll(local_feature.reshape(-1, N), shift, axis=1).reshape(-1)


def rmse(prediction: np.ndarray, observation: np.ndarray) -> float:
    return float(np.sqrt(np.mean((prediction - observation) ** 2)))


TRUE_SIMS = {name: simulate(TRUE_BETA, TRUE_D, SOURCES[name]) for name in ALL_PROTOCOLS}
TRUE_PROBE = {name: probe_feature(TRUE_SIMS[name]) for name in ALL_PROTOCOLS}
TRUE_SOURCE = {name: exchange_feature(TRUE_SIMS[name]["source_power"]) for name in ALL_PROTOCOLS}
TRUE_BATH = {name: exchange_feature(TRUE_SIMS[name]["bath_power"]) for name in ALL_PROTOCOLS}

TRUE_PROBE_TRAIN = concatenate(TRUE_PROBE, TRAIN_PROTOCOLS)
TRUE_PROBE_TEST = concatenate(TRUE_PROBE, TEST_PROTOCOLS)
TRUE_SOURCE_TRAIN = concatenate(TRUE_SOURCE, TRAIN_PROTOCOLS)
TRUE_SOURCE_TEST = concatenate(TRUE_SOURCE, TEST_PROTOCOLS)
TRUE_BATH_TRAIN = concatenate(TRUE_BATH, TRAIN_PROTOCOLS)
TRUE_BATH_TEST = concatenate(TRUE_BATH, TEST_PROTOCOLS)


def build_library():
    library = []
    for beta in BETA_GRID:
        for diffusion in D_GRID:
            sims = {name: simulate(float(beta), float(diffusion), SOURCES[name]) for name in ALL_PROTOCOLS}
            probe = {name: probe_feature(sims[name]) for name in ALL_PROTOCOLS}
            source = {name: exchange_feature(sims[name]["source_power"]) for name in ALL_PROTOCOLS}
            bath = {name: exchange_feature(sims[name]["bath_power"]) for name in ALL_PROTOCOLS}
            library.append({
                "beta": float(beta),
                "D": float(diffusion),
                "probe_train": concatenate(probe, TRAIN_PROTOCOLS),
                "probe_test": concatenate(probe, TEST_PROTOCOLS),
                "source_test": concatenate(source, TEST_PROTOCOLS),
                "bath_test": concatenate(bath, TEST_PROTOCOLS),
            })
    return library


def fit_probe(observed_train: np.ndarray, observed_test: np.ndarray, library):
    best = None
    for candidate in library:
        feature = candidate["probe_train"]
        coupling = float(np.dot(feature, observed_train) / (np.dot(feature, feature) + 1e-15))
        error = rmse(coupling * feature, observed_train)
        if best is None or error < best["train_rmse"]:
            best = dict(candidate)
            best.update({
                "lambda": coupling,
                "train_rmse": error,
                "test_rmse": rmse(coupling * candidate["probe_test"], observed_test),
            })
    return best


def generate_observations(generator: str, seed: int):
    rng = np.random.default_rng(seed)
    probe_train = TRUE_LAMBDA * TRUE_PROBE_TRAIN + rng.normal(0, PROBE_SIGMA, TRUE_PROBE_TRAIN.shape)
    probe_test = TRUE_LAMBDA * TRUE_PROBE_TEST + rng.normal(0, PROBE_SIGMA, TRUE_PROBE_TEST.shape)

    if generator == "action_local":
        source_train, source_test = TRUE_SOURCE_TRAIN, TRUE_SOURCE_TEST
        bath_train, bath_test = TRUE_BATH_TRAIN, TRUE_BATH_TEST
    elif generator == "global_scramble":
        source_train, source_test = scramble_sites(TRUE_SOURCE_TRAIN), scramble_sites(TRUE_SOURCE_TEST)
        bath_train, bath_test = scramble_sites(TRUE_BATH_TRAIN), scramble_sites(TRUE_BATH_TEST)
    elif generator == "no_exchange":
        source_train, source_test = np.zeros_like(TRUE_SOURCE_TRAIN), np.zeros_like(TRUE_SOURCE_TEST)
        bath_train, bath_test = np.zeros_like(TRUE_BATH_TRAIN), np.zeros_like(TRUE_BATH_TEST)
    else:
        raise ValueError(generator)

    source_train = source_train + rng.normal(0, EXCHANGE_SIGMA, source_train.shape)
    source_test = source_test + rng.normal(0, EXCHANGE_SIGMA, source_test.shape)
    bath_train = bath_train + rng.normal(0, EXCHANGE_SIGMA, bath_train.shape)
    bath_test = bath_test + rng.normal(0, EXCHANGE_SIGMA, bath_test.shape)
    return probe_train, probe_test, source_train, source_test, bath_train, bath_test


def summarize_generator(generator: str, seeds: int, library) -> GeneratorSummary:
    rows = []
    for index in range(seeds):
        probe_train, probe_test, _, source_test, _, bath_test = generate_observations(generator, 1000 + index)
        fit = fit_probe(probe_train, probe_test, library)
        rows.append({
            "beta": fit["beta"],
            "D": fit["D"],
            "lambda": fit["lambda"],
            "probe": fit["test_rmse"],
            "source_action": rmse(fit["source_test"], source_test),
            "bath_action": rmse(fit["bath_test"], bath_test),
            "source_zero": rmse(np.zeros_like(source_test), source_test),
            "bath_zero": rmse(np.zeros_like(bath_test), bath_test),
            "source_global": rmse(global_totals(fit["source_test"]), global_totals(source_test)),
            "bath_global": rmse(global_totals(fit["bath_test"]), global_totals(bath_test)),
        })

    def mean(key):
        return float(np.mean([row[key] for row in rows]))

    return GeneratorSummary(
        generator=generator,
        seeds=seeds,
        fitted_beta_mean=mean("beta"),
        fitted_D_mean=mean("D"),
        fitted_lambda_mean=mean("lambda"),
        probe_test_rmse_mean=mean("probe"),
        action_source_local_rmse_mean=mean("source_action"),
        action_bath_local_rmse_mean=mean("bath_action"),
        zero_source_local_rmse_mean=mean("source_zero"),
        zero_bath_local_rmse_mean=mean("bath_zero"),
        action_source_global_rmse_mean=mean("source_global"),
        action_bath_global_rmse_mean=mean("bath_global"),
    )


def identity_summary() -> IdentitySummary:
    max_error = max(float(np.max(np.abs(TRUE_SIMS[name]["local_residual"]))) for name in ALL_PROTOCOLS)
    return IdentitySummary(
        max_local_continuity_error=max_error,
        exact_matched_hidden_sector_prediction_difference=0.0,
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seeds", type=int, default=50)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    library = build_library()
    summaries = [summarize_generator(name, args.seeds, library) for name in ("action_local", "global_scramble", "no_exchange")]
    identity = identity_summary()

    payload = {
        "generator_summaries": [asdict(row) for row in summaries],
        "identity": asdict(identity),
        "noise": {"probe_sigma": PROBE_SIGMA, "exchange_sigma_per_local_measurement": EXCHANGE_SIGMA},
    }

    if args.json:
        print(json.dumps(payload, indent=2))
        return

    print("SIM-04L local exchange continuity")
    for row in summaries:
        print(
            f"{row.generator:16s} beta={row.fitted_beta_mean:.4f} D={row.fitted_D_mean:.4f} "
            f"probe={row.probe_test_rmse_mean:.5f} source_local={row.action_source_local_rmse_mean:.5f} "
            f"bath_local={row.action_bath_local_rmse_mean:.5f} source_global={row.action_source_global_rmse_mean:.5f} "
            f"bath_global={row.action_bath_global_rmse_mean:.5f}"
        )
    print(f"max local continuity identity error={identity.max_local_continuity_error:.3e}")


if __name__ == "__main__":
    main()
