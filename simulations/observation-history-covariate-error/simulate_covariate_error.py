#!/usr/bin/env python3
"""Simulation 4e: unmeasured carryover and covariate-measurement error.

Tests how imperfect measurement of ordinary preparation carryover can leave a
false history-associated residual after adjustment. Synthetic design study
only; no empirical or SoCT detection claim is made.
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
    sigma2 = sum(r*r for r in residuals) / dof
    se = [math.sqrt(max(0.0, sigma2 * inv[i][i])) for i in range(p)]
    return coef, se


def memory_basis(beta=0.25, t=4.0):
    return (1.0 - math.exp(-beta*t))/beta


def run(measurement_sigma, hidden_strength, seed, n_trials=3000):
    rng = random.Random(seed)
    fm = memory_basis()
    x = []
    y = []
    for i in range(n_trials):
        dose = rng.choice([0.0, 0.5, 1.0])
        sign = rng.choice([-1, 1]) if dose else 0
        h = sign*dose
        order = (i-(n_trials-1)/2)/n_trials

        heat = 0.80*h + rng.gauss(0, 0.18)
        coh = 0.45*h + rng.gauss(0, 0.12)
        pulse = 1.20*h + rng.gauss(0, 0.25)
        hidden = 0.70*h + rng.gauss(0, 0.20)

        # Experimenter observes noisy proxies, not the latent true values.
        heat_m = heat + rng.gauss(0, measurement_sigma)
        coh_m = coh + rng.gauss(0, measurement_sigma)
        pulse_m = pulse + rng.gauss(0, measurement_sigma)

        ordinary = 0.025*heat - 0.018*coh + 0.008*pulse + hidden_strength*hidden
        outcome = 0.010 + 0.012*order + ordinary + rng.gauss(0, 0.02)
        x.append([1.0, order, h*fm, heat_m, coh_m, pulse_m])
        y.append(outcome)

    coef, se = least_squares(x, y)
    return {
        "measurement_sigma": measurement_sigma,
        "hidden_strength": hidden_strength,
        "lambda_true": 0.0,
        "lambda_fit": coef[2],
        "lambda_se": se[2],
        "z": coef[2]/se[2],
        "n_trials": n_trials,
    }


def main():
    out = Path(__file__).with_name("results.csv")
    rows=[]
    seed=100
    for hidden in [0.0, 0.003, 0.006, 0.012]:
        for ms in [0.0, 0.02, 0.05, 0.10, 0.20]:
            rows.append(run(ms, hidden, seed))
            seed += 1
    with out.open("w", newline="") as f:
        w=csv.DictWriter(f, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
