#!/usr/bin/env python3
"""
SOC-HYS-01 simulation and analysis scaffold.

Status: SIMULATION / ANALYSIS PIPELINE ONLY.

This script does not test SoCT physically. It generates synthetic trial streams for
collapse-memory hysteresis protocol development so the analysis can be checked
against null data, injected hysteresis, sensor settling, and slow drift before any
physical measurement stream is used.

Core protocol:
- H -> L block transition
- L -> H block transition
- compare early post-switch residuals

Claim boundary:
Passing this simulation does not prove collapse memory, physical hysteresis, or
any nonstandard physics. It only verifies that the analysis pipeline can recover
or reject a known injected order-dependent residual under stated assumptions.
"""

from __future__ import annotations

import argparse
import csv
import math
import random
import statistics
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class SimulationConfig:
    trials_per_condition: int = 1000
    post_window: int = 100
    repeats: int = 20
    noise_sigma: float = 1.0
    hysteresis_amplitude: float = 0.0
    settling_amplitude: float = 0.0
    drift_per_trial: float = 0.0
    decay_tau: float = 25.0
    seed: int = 12345


def exp_decay(index: int, tau: float) -> float:
    if tau <= 0:
        raise ValueError("decay_tau must be positive")
    return math.exp(-index / tau)


def generate_transition(
    rng: random.Random,
    transition: str,
    config: SimulationConfig,
    repeat_index: int,
) -> list[dict[str, float | int | str]]:
    """Generate one two-block transition sequence."""

    if transition not in {"H_to_L", "L_to_H"}:
        raise ValueError("transition must be H_to_L or L_to_H")

    first_condition, second_condition = transition.split("_to_")
    total_trials = config.trials_per_condition * 2
    switch_trial = config.trials_per_condition
    rows: list[dict[str, float | int | str]] = []

    # Sign convention: positive injected hysteresis means H->L early post-switch
    # residual is larger than L->H early post-switch residual.
    hysteresis_sign = 1.0 if transition == "H_to_L" else -1.0

    for trial in range(total_trials):
        condition = first_condition if trial < switch_trial else second_condition
        post_index = trial - switch_trial
        is_post_switch = post_index >= 0

        base = 0.0 if condition == "L" else 0.2
        drift = config.drift_per_trial * (trial + repeat_index * total_trials)
        settling = 0.0
        hysteresis = 0.0

        if is_post_switch:
            settling = config.settling_amplitude * exp_decay(post_index, config.decay_tau)
            hysteresis = (
                hysteresis_sign
                * config.hysteresis_amplitude
                * exp_decay(post_index, config.decay_tau)
            )

        value = base + drift + settling + hysteresis + rng.gauss(0.0, config.noise_sigma)
        rows.append(
            {
                "repeat": repeat_index,
                "trial": trial,
                "transition": transition,
                "condition": condition,
                "is_post_switch": int(is_post_switch),
                "post_index": post_index if is_post_switch else -1,
                "value": value,
            }
        )
    return rows


def generate_dataset(config: SimulationConfig) -> list[dict[str, float | int | str]]:
    rng = random.Random(config.seed)
    rows: list[dict[str, float | int | str]] = []
    transitions = ["H_to_L", "L_to_H"]
    for repeat in range(config.repeats):
        order = transitions[:]
        rng.shuffle(order)
        for transition in order:
            rows.extend(generate_transition(rng, transition, config, repeat))
    return rows


def post_switch_values(
    rows: list[dict[str, float | int | str]],
    transition: str,
    post_window: int,
) -> list[float]:
    values: list[float] = []
    for row in rows:
        if row["transition"] != transition:
            continue
        post_index = int(row["post_index"])
        if 0 <= post_index < post_window:
            values.append(float(row["value"]))
    return values


def mean(values: list[float]) -> float:
    if not values:
        raise ValueError("cannot compute mean of empty list")
    return statistics.fmean(values)


def permutation_p_value(a: list[float], b: list[float], iterations: int, seed: int) -> float:
    """Two-sided permutation p-value for difference in means."""

    if not a or not b:
        raise ValueError("permutation inputs must be non-empty")
    rng = random.Random(seed)
    observed = abs(mean(a) - mean(b))
    pooled = a + b
    n_a = len(a)
    count = 0
    for _ in range(iterations):
        rng.shuffle(pooled)
        diff = abs(mean(pooled[:n_a]) - mean(pooled[n_a:]))
        if diff >= observed:
            count += 1
    return (count + 1) / (iterations + 1)


def summarize(rows: list[dict[str, float | int | str]], config: SimulationConfig, permutations: int) -> dict[str, float | int | str]:
    h_to_l = post_switch_values(rows, "H_to_L", config.post_window)
    l_to_h = post_switch_values(rows, "L_to_H", config.post_window)
    mean_hl = mean(h_to_l)
    mean_lh = mean(l_to_h)
    delta = mean_hl - mean_lh
    p_value = permutation_p_value(h_to_l, l_to_h, permutations, config.seed + 999)
    return {
        "status": "SIMULATION_ONLY_NO_PHYSICAL_CLAIM",
        "repeats": config.repeats,
        "trials_per_condition": config.trials_per_condition,
        "post_window": config.post_window,
        "noise_sigma": config.noise_sigma,
        "hysteresis_amplitude": config.hysteresis_amplitude,
        "settling_amplitude": config.settling_amplitude,
        "drift_per_trial": config.drift_per_trial,
        "decay_tau": config.decay_tau,
        "mean_post_H_to_L": mean_hl,
        "mean_post_L_to_H": mean_lh,
        "delta_HL_minus_LH": delta,
        "permutation_p_value": p_value,
        "n_post_H_to_L": len(h_to_l),
        "n_post_L_to_H": len(l_to_h),
    }


def write_rows(path: Path, rows: list[dict[str, float | int | str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_summary(path: Path, summary: dict[str, float | int | str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(summary.keys()))
        writer.writeheader()
        writer.writerow(summary)


def main() -> None:
    parser = argparse.ArgumentParser(description="Simulate the SOC-HYS-01 hysteresis protocol.")
    parser.add_argument("--trials-per-condition", type=int, default=1000)
    parser.add_argument("--post-window", type=int, default=100)
    parser.add_argument("--repeats", type=int, default=20)
    parser.add_argument("--noise-sigma", type=float, default=1.0)
    parser.add_argument("--hysteresis-amplitude", type=float, default=0.0)
    parser.add_argument("--settling-amplitude", type=float, default=0.0)
    parser.add_argument("--drift-per-trial", type=float, default=0.0)
    parser.add_argument("--decay-tau", type=float, default=25.0)
    parser.add_argument("--seed", type=int, default=12345)
    parser.add_argument("--permutations", type=int, default=2000)
    parser.add_argument("--rows-out", type=Path, default=None)
    parser.add_argument("--summary-out", type=Path, default=None)
    args = parser.parse_args()

    config = SimulationConfig(
        trials_per_condition=args.trials_per_condition,
        post_window=args.post_window,
        repeats=args.repeats,
        noise_sigma=args.noise_sigma,
        hysteresis_amplitude=args.hysteresis_amplitude,
        settling_amplitude=args.settling_amplitude,
        drift_per_trial=args.drift_per_trial,
        decay_tau=args.decay_tau,
        seed=args.seed,
    )

    rows = generate_dataset(config)
    summary = summarize(rows, config, args.permutations)

    print("SOC-HYS-01 collapse-memory hysteresis simulation")
    print("Status: SIMULATION ONLY / NO PHYSICAL CLAIM")
    for key, value in summary.items():
        print(f"{key}: {value}")

    if args.rows_out is not None:
        write_rows(args.rows_out, rows)
        print(f"rows_written: {args.rows_out}")
    if args.summary_out is not None:
        write_summary(args.summary_out, summary)
        print(f"summary_written: {args.summary_out}")


if __name__ == "__main__":
    main()
