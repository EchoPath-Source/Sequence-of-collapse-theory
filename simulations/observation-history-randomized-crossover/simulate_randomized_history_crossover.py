#!/usr/bin/env python3
"""Simulation 4c: randomized history-dose crossover.

Goal
----
Break the nuisance degeneracy found in Simulation 4b by randomizing which
physical arm receives more prior durable-record history and by varying the
history dose across repeated trials.

The measured quantity is a differential phase between physical arms B and A.
Ordinary hardware offset and slow run-order drift remain tied to the apparatus.
The speculative SoCT term follows the randomized history contrast instead.

This is a synthetic design/identifiability study. It is not evidence for a
physical memory field.
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


def matvec(a, v):
    return [sum(x * y for x, y in zip(row, v)) for row in a]


def least_squares(x, y):
    p = len(x[0])
    xtx = [[sum(row[i] * row[j] for row in x) for j in range(p)] for i in range(p)]
    xty = [sum(row[i] * yy for row, yy in zip(x, y)) for i in range(p)]
    inv = invert_matrix(xtx)
    coef = matvec(inv, xty)
    pred = [sum(row[i] * coef[i] for i in range(p)) for row in x]
    residuals = [yy - pp for yy, pp in zip(y, pred)]
    return coef, residuals, inv


def memory_basis(beta, probe_time):
    if beta == 0.0:
        return probe_time
    return (1.0 - math.exp(-beta * probe_time)) / beta


def run_scenario(label, lam, seed, n_trials=600, noise_sigma=0.03, beta=0.25, probe_time=4.0):
    rng = random.Random(seed)
    f_m = memory_basis(beta, probe_time)

    design = []
    outcomes = []
    sham_values = []

    for i in range(n_trials):
        dose = rng.choice([0.0, 0.5, 1.0])
        sign = rng.choice([-1, 1]) if dose > 0 else 0
        history_contrast = sign * dose

        # Centered run order for slow drift calibration.
        run_order = (i - (n_trials - 1) / 2.0) / n_trials

        # Apparatus-tied nuisance terms. These do not follow the randomized
        # history label.
        hardware_offset = 0.012
        linear_drift = 0.018 * run_order
        periodic_drift = 0.004 * math.sin(2.0 * math.pi * i / 73.0)

        # SoCT injection follows assigned history contrast, not arm identity.
        memory_signal = lam * history_contrast * f_m

        y = (
            hardware_offset
            + linear_drift
            + periodic_drift
            + memory_signal
            + rng.gauss(0.0, noise_sigma)
        )

        # Fit intercept + calibrated linear drift + randomized history term.
        design.append([1.0, run_order, history_contrast * f_m])
        outcomes.append(y)
        if dose == 0.0:
            sham_values.append(y)

    coef, residuals, inv = least_squares(design, outcomes)
    dof = max(1, n_trials - len(design[0]))
    sigma2 = sum(r * r for r in residuals) / dof
    se_lambda = math.sqrt(max(0.0, sigma2 * inv[2][2]))
    lambda_fit = coef[2]
    z = lambda_fit / se_lambda if se_lambda > 0 else float("inf")

    sham_mean = sum(sham_values) / len(sham_values)
    return {
        "scenario": label,
        "n_trials": n_trials,
        "lambda_true": lam,
        "lambda_fit": lambda_fit,
        "lambda_se": se_lambda,
        "z_score": z,
        "beta": beta,
        "probe_time": probe_time,
        "noise_sigma": noise_sigma,
        "f_M": f_m,
        "fitted_hardware_offset": coef[0],
        "fitted_linear_drift": coef[1],
        "sham_mean_phase": sham_mean,
    }


def main():
    out = Path(__file__).with_name("results.csv")
    scenarios = [
        run_scenario("null", 0.0, 21),
        run_scenario("weak_signal", 0.005, 22),
        run_scenario("moderate_signal", 0.010, 23),
        run_scenario("strong_signal", 0.020, 24),
    ]

    with out.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=scenarios[0].keys())
        writer.writeheader()
        writer.writerows(scenarios)

    print(f"wrote {out}")


if __name__ == "__main__":
    main()
