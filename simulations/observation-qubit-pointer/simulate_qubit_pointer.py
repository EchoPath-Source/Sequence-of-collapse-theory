#!/usr/bin/env python3
"""Simulation 1 for the SoCT operational observation project.

Purpose
-------
Benchmark candidate observation metrics in the simplest measurement-like system:
a qubit S coupled to a two-state pointer O.

This script uses only ordinary unitary quantum mechanics plus a simple pointer-memory
depolarizing channel. It intentionally contains no SoCT memory feedback and no
consciousness term. Its role is to test whether distinguishability, accessible
record information, persistence, and the provisional observation proxy behave
sensibly before introducing new physics.

Model
-----
System input: |+> = (|0> + |1>)/sqrt(2)
Pointer input: |0>

Measurement interaction:
    |0>|0> -> |0>|0>
    |1>|0> -> |1>|phi(theta)>

where
    |phi(theta)> = cos(theta)|0> + sin(theta)|1>.

Thus theta=0 gives no record and theta=pi/2 gives orthogonal, perfectly
distinguishable pointer records.

After record formation, pointer persistence is modeled by a depolarizing memory
channel with retention r(t)=exp(-gamma*t). This is a benchmark memory channel,
not an SoCT memory field.
"""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path

import numpy as np


ZERO = np.array([1.0, 0.0], dtype=complex)
ONE = np.array([0.0, 1.0], dtype=complex)
RHO_ZERO = np.outer(ZERO, ZERO.conj())
I2 = np.eye(2, dtype=complex)


def von_neumann_entropy(rho: np.ndarray) -> float:
    """Entropy in bits."""
    rho = 0.5 * (rho + rho.conj().T)
    vals = np.linalg.eigvalsh(rho).real
    vals = vals[vals > 1e-12]
    return float(-np.sum(vals * np.log2(vals)))


def trace_distance(rho: np.ndarray, sigma: np.ndarray) -> float:
    """D_tr(rho,sigma)=1/2 ||rho-sigma||_1."""
    singular_values = np.linalg.svd(rho - sigma, compute_uv=False)
    return float(0.5 * np.sum(singular_values).real)


def pointer_record_state(theta: float) -> np.ndarray:
    phi = math.cos(theta) * ZERO + math.sin(theta) * ONE
    return np.outer(phi, phi.conj())


def depolarize(rho: np.ndarray, retention: float) -> np.ndarray:
    """Simple record-retention channel: rho -> r rho + (1-r) I/2."""
    return retention * rho + (1.0 - retention) * I2 / 2.0


def holevo_information(rho0: np.ndarray, rho1: np.ndarray) -> float:
    """Holevo information for equal-prior binary pointer record states, in bits."""
    avg = 0.5 * (rho0 + rho1)
    return (
        von_neumann_entropy(avg)
        - 0.5 * von_neumann_entropy(rho0)
        - 0.5 * von_neumann_entropy(rho1)
    )


def quantum_mutual_information_initial(theta: float) -> float:
    """I(S:O) immediately after the measurement interaction, in bits."""
    phi = math.cos(theta) * ZERO + math.sin(theta) * ONE
    psi = (np.kron(ZERO, ZERO) + np.kron(ONE, phi)) / math.sqrt(2.0)
    rho = np.outer(psi, psi.conj()).reshape(2, 2, 2, 2)
    rho_s = np.einsum("abcb->ac", rho)
    rho_o = np.einsum("abad->bd", rho)
    # The joint state is pure, so S(rho_SO)=0.
    return von_neumann_entropy(rho_s) + von_neumann_entropy(rho_o)


def simulate(theta_values, time_values, gamma: float):
    rows = []

    for theta in theta_values:
        rho0 = RHO_ZERO
        rho1 = pointer_record_state(theta)

        measurement_strength = math.sin(theta) ** 2
        d0 = trace_distance(rho0, rho1)
        chi0 = holevo_information(rho0, rho1)
        qmi0 = quantum_mutual_information_initial(theta)

        # Provisional event-level observation proxy. Accessibility is fixed to 1
        # in Simulation 1. Persistence is applied separately below.
        omega_event = measurement_strength * d0

        for time in time_values:
            retention = math.exp(-gamma * time)
            rho0_t = depolarize(rho0, retention)
            rho1_t = depolarize(rho1, retention)

            d_t = trace_distance(rho0_t, rho1_t)
            chi_t = holevo_information(rho0_t, rho1_t)

            if chi0 <= 1e-12:
                persistence_ratio = 0.0
            else:
                persistence_ratio = chi_t / chi0

            omega_persistent = omega_event * persistence_ratio

            rows.append(
                {
                    "theta_rad": theta,
                    "time": time,
                    "measurement_strength": measurement_strength,
                    "pointer_trace_distance_t0": d0,
                    "quantum_mutual_info_bits_t0": qmi0,
                    "holevo_bits_t0": chi0,
                    "retention_factor": retention,
                    "pointer_trace_distance_t": d_t,
                    "holevo_bits_t": chi_t,
                    "persistence_ratio": persistence_ratio,
                    "omega_event": omega_event,
                    "omega_persistent": omega_persistent,
                }
            )

    return rows


def validate(rows) -> None:
    """Sanity checks expected of the benchmark observation metric."""
    by_theta_time = {(r["theta_rad"], r["time"]): r for r in rows}
    theta_values = sorted({r["theta_rad"] for r in rows})
    time_values = sorted({r["time"] for r in rows})

    weak = by_theta_time[(theta_values[0], time_values[0])]
    strong = by_theta_time[(theta_values[-1], time_values[0])]

    assert abs(weak["pointer_trace_distance_t0"]) < 1e-10
    assert abs(weak["holevo_bits_t0"]) < 1e-10
    assert abs(weak["omega_event"]) < 1e-10

    assert abs(strong["pointer_trace_distance_t0"] - 1.0) < 1e-10
    assert abs(strong["holevo_bits_t0"] - 1.0) < 1e-9
    assert abs(strong["omega_event"] - 1.0) < 1e-10

    initial_rows = [r for r in rows if abs(r["time"] - time_values[0]) < 1e-12]
    for key in ("pointer_trace_distance_t0", "holevo_bits_t0", "omega_event"):
        values = [r[key] for r in initial_rows]
        assert all(b + 1e-12 >= a for a, b in zip(values, values[1:])), key

    for theta in theta_values[1:]:
        series = [by_theta_time[(theta, t)]["omega_persistent"] for t in time_values]
        assert all(b <= a + 1e-12 for a, b in zip(series, series[1:])), theta


def write_csv(rows, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys())
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("results.csv"),
    )
    parser.add_argument("--gamma", type=float, default=0.5)
    parser.add_argument("--theta-count", type=int, default=9)
    args = parser.parse_args()

    theta_values = np.linspace(0.0, math.pi / 2.0, args.theta_count)
    time_values = [0.0, 0.5, 1.0, 2.0, 4.0]

    rows = simulate(theta_values, time_values, args.gamma)
    validate(rows)
    write_csv(rows, args.output)

    perfect = [
        r for r in rows
        if abs(r["theta_rad"] - math.pi / 2.0) < 1e-10 and abs(r["time"]) < 1e-12
    ][0]

    print(f"wrote {len(rows)} rows to {args.output}")
    print(
        "perfect-record limit: "
        f"D={perfect['pointer_trace_distance_t0']:.6f}, "
        f"chi={perfect['holevo_bits_t0']:.6f} bit, "
        f"QMI={perfect['quantum_mutual_info_bits_t0']:.6f} bits, "
        f"Omega_event={perfect['omega_event']:.6f}"
    )
    print("sanity checks: PASS")


if __name__ == "__main__":
    main()
