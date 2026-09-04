"""Simulation 2: qubit + pointer + environment benchmark.

This script tests whether the operational observation metrics distinguish
pointer-record formation from ordinary environmental decoherence.

No SoCT memory feedback or consciousness term is included.
"""

from __future__ import annotations

import csv
import math
from pathlib import Path

import numpy as np

N_ENV = 4
GRID = [0.0, 0.25, 0.50, 0.75, 1.0]


def entropy(rho: np.ndarray) -> float:
    vals = np.linalg.eigvalsh((rho + rho.conj().T) / 2.0)
    vals = vals[vals > 1e-12]
    return float(-(vals * np.log2(vals)).sum())


def partial_trace(rho: np.ndarray, dims: list[int], keep: list[int]) -> np.ndarray:
    arr = rho.reshape(*(dims + dims))
    current_dims = list(dims)
    for idx in sorted([i for i in range(len(dims)) if i not in keep], reverse=True):
        arr = np.trace(arr, axis1=idx, axis2=idx + len(current_dims))
        current_dims.pop(idx)
    size = int(np.prod(current_dims))
    return arr.reshape(size, size)


def h2(x: float) -> float:
    if x <= 1e-15 or x >= 1 - 1e-15:
        return 0.0
    return -(x * math.log2(x) + (1 - x) * math.log2(1 - x))


def binary_pure_holevo(overlap: float) -> float:
    return h2((1.0 + abs(overlap)) / 2.0)


def simulate(theta: float, phi: float, n_env: int = N_ENV) -> dict[str, float]:
    zero = np.array([1.0, 0.0], dtype=complex)
    one = np.array([0.0, 1.0], dtype=complex)

    pointer_record = math.cos(theta) * zero + math.sin(theta) * one
    env_record = math.cos(phi) * zero + math.sin(phi) * one

    branch0 = zero
    for state in [zero] + [zero] * n_env:
        branch0 = np.kron(branch0, state)

    branch1 = one
    for state in [pointer_record] + [env_record] * n_env:
        branch1 = np.kron(branch1, state)

    psi = (branch0 + branch1) / math.sqrt(2.0)
    rho = np.outer(psi, psi.conj())
    dims = [2] * (n_env + 2)

    rho_s = partial_trace(rho, dims, [0])
    rho_p = partial_trace(rho, dims, [1])
    rho_sp = partial_trace(rho, dims, [0, 1])
    rho_e1 = partial_trace(rho, dims, [2])
    rho_se1 = partial_trace(rho, dims, [0, 2])

    i_sp = entropy(rho_s) + entropy(rho_p) - entropy(rho_sp)
    i_se1 = entropy(rho_s) + entropy(rho_e1) - entropy(rho_se1)

    d_pointer = abs(math.sin(theta))
    d_env = abs(math.sin(phi))
    chi_pointer = binary_pure_holevo(math.cos(theta))
    chi_env = binary_pure_holevo(math.cos(phi))
    system_coherence = 2.0 * abs(rho_s[0, 1])

    # Exploratory strong-record proxy: accessible pointer record only.
    omega_pointer = d_pointer * chi_pointer

    return {
        "theta_frac_pi_over_2": theta / (math.pi / 2.0),
        "phi_frac_pi_over_2": phi / (math.pi / 2.0),
        "system_coherence": system_coherence,
        "pointer_trace_distance": d_pointer,
        "pointer_holevo_bits": chi_pointer,
        "pointer_mutual_information_bits": i_sp,
        "omega_pointer": omega_pointer,
        "env_fragment_trace_distance": d_env,
        "env_fragment_holevo_bits": chi_env,
        "env_fragment_mutual_information_bits": i_se1,
        "redundant_env_fragments_ge_0_5_bits": n_env if chi_env >= 0.5 else 0,
    }


def main() -> None:
    rows = []
    for theta_fraction in GRID:
        for phi_fraction in GRID:
            rows.append(
                simulate(
                    theta_fraction * math.pi / 2.0,
                    phi_fraction * math.pi / 2.0,
                )
            )

    out = Path(__file__).with_name("results.csv")
    with out.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    print(f"wrote {len(rows)} rows to {out}")


if __name__ == "__main__":
    main()
