#!/usr/bin/env python3
"""Simulation 3b: redundant record formation and partial erasure.

This is a standard-quantum toy model. A system qubit imprints the same binary
record into N environment fragments. We then erase k fragments exactly and
measure how much record structure remains outside the erased sector.

No SoCT memory feedback is applied here.
"""

import csv
import math
from pathlib import Path


def binary_entropy(p: float) -> float:
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p * math.log(p, 2) - (1.0 - p) * math.log(1.0 - p, 2)


def single_fragment_metrics(phi: float):
    overlap = abs(math.cos(phi))
    d = abs(math.sin(phi))
    chi = binary_entropy((1.0 + overlap) / 2.0)
    return overlap, d, chi


def main():
    out = Path(__file__).with_name("results.csv")
    n_values = [1, 2, 4, 8]
    phis = [math.pi / 12, math.pi / 6, math.pi / 4, math.pi / 3, math.pi / 2]
    rows = []

    for n in n_values:
        for phi in phis:
            overlap, d_frag, chi_frag = single_fragment_metrics(phi)
            for erased in range(n + 1):
                remaining = n - erased
                branch_overlap = overlap ** remaining

                # Record structure outside the sector that has been reversed.
                xi_irr = 1.0 - branch_overlap

                # Threshold redundancy diagnostic only; not the main score.
                redundancy_09 = remaining if chi_frag >= 0.9 else 0

                # Continuous exploratory durable-record score. It rewards residual
                # branch separation, surviving multiplicity, and accessible info.
                surviving_fraction = remaining / n if n else 0.0
                durable_score = xi_irr * surviving_fraction * chi_frag

                rows.append({
                    "N_fragments": n,
                    "phi_rad": phi,
                    "phi_over_pi": phi / math.pi,
                    "erased_fragments": erased,
                    "remaining_fragments": remaining,
                    "single_fragment_D": d_frag,
                    "single_fragment_chi_bits": chi_frag,
                    "remaining_branch_overlap": branch_overlap,
                    "Xi_irr_proxy": xi_irr,
                    "redundancy_R09": redundancy_09,
                    "durable_record_score": durable_score,
                })

    with out.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print(f"wrote {out}")


if __name__ == "__main__":
    main()
