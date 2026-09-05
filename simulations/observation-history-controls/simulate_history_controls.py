#!/usr/bin/env python3
"""Simulation 4b: adversarial controls for history-dependent SoCT phase residuals.

This script asks whether the phase signature proposed in Simulation 4 can be
separated from ordinary nuisance effects over a finite observation window.

The candidate SoCT phase basis is

    f_M(t) = [1 - exp(-beta t)] / beta,

while ordinary nuisance terms include a constant offset, linear frequency
mismatch, and quadratic drift. The script quantifies how well the memory basis
can be absorbed by those nuisance terms and runs representative noisy fits.

Important: this is a falsification/control toy model. It is designed to expose
non-identifiability, not to demonstrate new physics.
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


def memory_basis(beta, t):
    if beta == 0.0:
        return t
    return (1.0 - math.exp(-beta * t)) / beta


def memory_basis_absorbability(times, beta):
    target = [memory_basis(beta, t) for t in times]
    nuisance = [[1.0, t, t * t] for t in times]
    _, residuals, _ = least_squares(nuisance, target)
    mean = sum(target) / len(target)
    sst = sum((v - mean) ** 2 for v in target)
    sse = sum(r * r for r in residuals)
    r2 = 1.0 - sse / sst if sst > 0 else 1.0
    rms = math.sqrt(sse / len(times))
    return r2, rms


def fit_memory_with_nuisance(times, y, beta):
    design = [[1.0, t, t * t, memory_basis(beta, t)] for t in times]
    coef, residuals, inv = least_squares(design, y)
    dof = max(1, len(y) - len(design[0]))
    sigma2 = sum(r * r for r in residuals) / dof
    se_lambda = math.sqrt(max(0.0, sigma2 * inv[3][3]))
    return coef, se_lambda


def representative_fit(label, lam, beta, noise_sigma, seed):
    rng = random.Random(seed)
    times = [0.2 * i for i in range(41)]

    # Ordinary arm-to-arm nuisance terms.
    offset = 0.002
    linear = 0.002
    quadratic = 0.00035

    y = []
    for t in times:
        signal = lam * memory_basis(beta, t)
        nuisance = offset + linear * t + quadratic * t * t
        y.append(signal + nuisance + rng.gauss(0.0, noise_sigma))

    coef, se = fit_memory_with_nuisance(times, y, beta)
    estimate = coef[3]
    z = estimate / se if se > 0 else float("inf")
    return {
        "scenario": label,
        "lambda_true": lam,
        "beta": beta,
        "noise_sigma": noise_sigma,
        "lambda_fit": estimate,
        "lambda_se": se,
        "z_score": z,
    }


def main():
    out = Path(__file__).with_name("results.csv")
    times = [0.2 * i for i in range(41)]

    rows = []
    for beta in [0.02, 0.05, 0.10, 0.25, 0.50, 1.00]:
        r2, rms = memory_basis_absorbability(times, beta)
        rows.append({
            "row_type": "basis_absorbability",
            "scenario": "",
            "lambda_true": "",
            "beta": beta,
            "noise_sigma": "",
            "lambda_fit": "",
            "lambda_se": "",
            "z_score": "",
            "memory_basis_R2_from_const_linear_quadratic": r2,
            "memory_basis_residual_rms": rms,
        })

    fits = [
        representative_fit("null_low_noise", 0.0, 0.25, 0.01, 11),
        representative_fit("signal_low_noise", 0.03, 0.25, 0.01, 12),
        representative_fit("signal_high_noise", 0.03, 0.25, 0.05, 13),
        representative_fit("signal_slow_memory", 0.03, 0.02, 0.01, 14),
    ]
    for fit in fits:
        rows.append({
            "row_type": "representative_fit",
            **fit,
            "memory_basis_R2_from_const_linear_quadratic": "",
            "memory_basis_residual_rms": "",
        })

    fields = [
        "row_type",
        "scenario",
        "lambda_true",
        "beta",
        "noise_sigma",
        "lambda_fit",
        "lambda_se",
        "z_score",
        "memory_basis_R2_from_const_linear_quadratic",
        "memory_basis_residual_rms",
    ]
    with out.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    print(f"wrote {out}")


if __name__ == "__main__":
    main()
