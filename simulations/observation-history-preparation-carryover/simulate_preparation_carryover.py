#!/usr/bin/env python3
"""Simulation 4d: preparation-induced ordinary carryover controls.

History-conditioning protocols may leave ordinary physical traces such as
heating, coherence loss, and control-pulse exposure. Those traces can follow
the randomized history label and therefore mimic a history-dependent SoCT
signal even in a crossover design.

This simulation compares a naive history-only model against an adjusted model
that includes measured carryover covariates.

Synthetic design study only. No empirical claim is made.
"""

import csv
import math
import random
from pathlib import Path


def invert_matrix(a):
    n = len(a)
    aug = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(a)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(aug[r][col]))
        if abs(aug[pivot][col]) < 1e-14:
            raise ValueError("singular matrix")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        pv = aug[col][col]
        aug[col] = [x / pv for x in aug[col]]
        for r in range(n):
            if r == col:
                continue
            fac = aug[r][col]
            aug[r] = [aug[r][c] - fac * aug[col][c] for c in range(2 * n)]
    return [row[n:] for row in aug]


def least_squares(x, y):
    p = len(x[0])
    xtx = [[sum(row[i] * row[j] for row in x) for j in range(p)] for i in range(p)]
    xty = [sum(row[i] * yy for row, yy in zip(x, y)) for i in range(p)]
    inv = invert_matrix(xtx)
    coef = [sum(inv[i][j] * xty[j] for j in range(p)) for i in range(p)]
    residuals = [yy - sum(row[i] * coef[i] for i in range(p)) for row, yy in zip(x, y)]
    dof = max(1, len(y) - p)
    sigma2 = sum(r * r for r in residuals) / dof
    se = [math.sqrt(max(0.0, sigma2 * inv[i][i])) for i in range(p)]
    return coef, se


def memory_basis(beta, probe_time):
    if beta == 0.0:
        return probe_time
    return (1.0 - math.exp(-beta * probe_time)) / beta


def run_scenario(label, lam, seed, n_trials=1200, noise_sigma=0.02, beta=0.25, probe_time=4.0):
    rng = random.Random(seed)
    f_m = memory_basis(beta, probe_time)

    x_naive = []
    x_adjusted = []
    y = []

    for i in range(n_trials):
        dose = rng.choice([0.0, 0.5, 1.0])
        sign = rng.choice([-1, 1]) if dose > 0 else 0
        h = sign * dose
        run_order = (i - (n_trials - 1) / 2.0) / n_trials

        # Measured ordinary carryover variables. They are intentionally
        # correlated with the history assignment and therefore can mimic it.
        heat = 0.80 * h + rng.gauss(0.0, 0.18)
        coherence_loss = 0.45 * h + rng.gauss(0.0, 0.12)
        pulse_exposure = 1.20 * h + rng.gauss(0.0, 0.25)

        hardware_offset = 0.010
        slow_drift = 0.012 * run_order

        ordinary_carryover = (
            0.025 * heat
            - 0.018 * coherence_loss
            + 0.008 * pulse_exposure
        )
        memory_signal = lam * h * f_m

        outcome = (
            hardware_offset
            + slow_drift
            + ordinary_carryover
            + memory_signal
            + rng.gauss(0.0, noise_sigma)
        )

        x_naive.append([1.0, run_order, h * f_m])
        x_adjusted.append([1.0, run_order, h * f_m, heat, coherence_loss, pulse_exposure])
        y.append(outcome)

    coef_n, se_n = least_squares(x_naive, y)
    coef_a, se_a = least_squares(x_adjusted, y)

    return {
        "scenario": label,
        "lambda_true": lam,
        "naive_lambda_fit": coef_n[2],
        "naive_lambda_se": se_n[2],
        "naive_z": coef_n[2] / se_n[2],
        "adjusted_lambda_fit": coef_a[2],
        "adjusted_lambda_se": se_a[2],
        "adjusted_z": coef_a[2] / se_a[2],
        "n_trials": n_trials,
        "noise_sigma": noise_sigma,
        "beta": beta,
        "probe_time": probe_time,
    }


def main():
    out = Path(__file__).with_name("results.csv")
    rows = [
        run_scenario("carryover_only_null_memory", 0.0, 31),
        run_scenario("weak_memory_plus_carryover", 0.005, 32),
        run_scenario("moderate_memory_plus_carryover", 0.010, 33),
    ]

    with out.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print(f"wrote {out}")


if __name__ == "__main__":
    main()
