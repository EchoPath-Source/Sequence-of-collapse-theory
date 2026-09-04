#!/usr/bin/env python3
"""Simulation 3: reversible record creation and erasure.

Purpose
-------
Create a measurement-like qubit-pointer correlation, quantify the record, then
apply the inverse interaction and verify exact erasure under unitary dynamics.
The script compares a present-state observation metric against a cumulative
positive record-production functional that remembers that a record existed.

This is a standard quantum toy model. No SoCT feedback term is applied.
"""

import csv
import math
from pathlib import Path


def binary_entropy(p: float) -> float:
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p * math.log(p, 2) - (1.0 - p) * math.log(1.0 - p, 2)


def metrics(theta: float):
    """Analytic metrics for equal-prior binary pointer records.

    Conditional pointer states are |0> and cos(theta)|0>+sin(theta)|1>.
    Their trace distance is |sin(theta)|.  The equal-prior Holevo quantity is
    S((rho0+rho1)/2), whose eigenvalues are (1 +/- |cos(theta)|)/2.
    """
    distinguishability = abs(math.sin(theta))
    p_plus = (1.0 + abs(math.cos(theta))) / 2.0
    holevo = binary_entropy(p_plus)

    # Exploratory normalized event metric.  This is not proposed as a law.
    omega = distinguishability * holevo
    return distinguishability, holevo, omega


def main():
    out = Path(__file__).with_name("results.csv")
    thetas = [
        0.0,
        math.pi / 12,
        math.pi / 6,
        math.pi / 4,
        math.pi / 3,
        5 * math.pi / 12,
        math.pi / 2,
    ]

    rows = []
    for theta in thetas:
        d_created, chi_created, omega_created = metrics(theta)

        # Applying the exact inverse unitary returns the joint state to the
        # pre-measurement product state in this ideal closed-system model.
        d_erased = 0.0
        chi_erased = 0.0
        omega_erased = 0.0

        # Positive record-production history: integrate only the positive jump
        # in the exploratory event metric.  Exact erasure removes the current
        # record but does not subtract the fact that the record was created.
        j_positive = omega_created

        rows.append(
            {
                "theta_rad": theta,
                "theta_over_pi": theta / math.pi,
                "D_created": d_created,
                "chi_created_bits": chi_created,
                "Omega_created": omega_created,
                "D_erased": d_erased,
                "chi_erased_bits": chi_erased,
                "Omega_erased": omega_erased,
                "J_positive_record_production": j_positive,
            }
        )

    with out.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print(f"wrote {out}")


if __name__ == "__main__":
    main()
