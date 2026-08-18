#!/usr/bin/env python3
"""SIM-04M: microscopic oscillator-bath completion of the effective damping term.

Toy-model methodology test only. This is not empirical evidence for SoCT or for
an additional physical memory field.

The benchmark replaces the phenomenological damping term gamma*dM/dt with an
explicit finite Hamiltonian bath of harmonic oscillators. The full system is
reversible and conserves energy after the source is switched off.

The central test is whether a local Markovian equation

    M_ddot + gamma_eff M_dot + Omega_M^2 M = C_obs(t)

emerges as a useful reduced description only when the bath spectral sampling is
sufficiently broad/dense.

Sparse baths should retain a structured memory kernel and show recurrences,
while dense baths should suppress large returns over the tested time window.

Requires: numpy
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass

import numpy as np


DT = 0.001
T_FINAL = 20.0
OMEGA_M = 1.0

ETA = 0.50
CUTOFF = 12.0
OMEGA_MIN = 0.10
OMEGA_MAX = 30.0

TRAIN_WINDOW = (1.5, 7.0)
TEST_WINDOW = (7.0, 18.0)
ENERGY_WINDOW = (1.5, 18.0)
RECURRENCE_EARLY = (2.0, 7.0)
RECURRENCE_LATE = (10.0, 18.0)

BATH_SIZES = (8, 32, 128, 256)
GAMMA_GRID = np.round(np.arange(0.10, 0.901, 0.01), 2)


@dataclass
class BathResult:
    bath_modes: int
    gamma_eff: float
    train_rmse: float
    heldout_rmse: float
    effective_heat_rmse: float
    recurrence_ratio: float
    energy_closure_max_error: float
    final_effective_heat: float
    final_bath_coupling_energy_gain: float


def source_force(t: float) -> float:
    """Smooth record-derived source surrogate used only for this bath gate."""
    if 0.5 <= t < 1.5:
        u = t - 0.5
        return float(np.sin(np.pi * u) ** 2)
    return 0.0


def bath_parameters(n_modes: int):
    """Discretize an Ohmic-like finite-cutoff spectral envelope."""
    omega = np.linspace(OMEGA_MIN, OMEGA_MAX, n_modes)
    delta = (OMEGA_MAX - OMEGA_MIN) / (n_modes - 1)

    spectral_density = ETA * omega * np.exp(-omega / CUTOFF)

    # J(w) = pi/2 sum_j c_j^2/w_j delta(w-w_j)
    coupling = np.sqrt(
        (2.0 / np.pi) * spectral_density * omega * delta
    )
    return omega, coupling


def simulate_microscopic(n_modes: int):
    """Velocity-Verlet evolution of M plus explicit bath oscillators."""
    omega, coupling = bath_parameters(n_modes)
    steps = int(T_FINAL / DT)
    times = np.arange(steps) * DT

    field = 0.0
    velocity = 0.0
    bath_q = np.zeros(n_modes, dtype=float)
    bath_p = np.zeros(n_modes, dtype=float)

    fields = np.empty(steps, dtype=float)
    velocities = np.empty(steps, dtype=float)
    bath_coupling_energy = np.empty(steps, dtype=float)
    total_energy = np.empty(steps, dtype=float)
    source_work = np.empty(steps, dtype=float)

    work = 0.0

    def acceleration(m_value, q_value, source):
        shifted = q_value - (coupling / (omega * omega)) * m_value
        m_accel = (
            -OMEGA_M * OMEGA_M * m_value
            + np.dot(coupling, shifted)
            + source
        )
        q_accel = -(omega * omega) * q_value + coupling * m_value
        return m_accel, q_accel

    for index, time in enumerate(times):
        force_0 = source_force(float(time))
        accel_m_0, accel_q_0 = acceleration(field, bath_q, force_0)

        field_new = field + velocity * DT + 0.5 * accel_m_0 * DT * DT
        bath_q_new = bath_q + bath_p * DT + 0.5 * accel_q_0 * DT * DT

        force_1 = source_force(float(time + DT))
        accel_m_1, accel_q_1 = acceleration(
            field_new,
            bath_q_new,
            force_1,
        )

        velocity_new = velocity + 0.5 * (accel_m_0 + accel_m_1) * DT
        bath_p_new = bath_p + 0.5 * (accel_q_0 + accel_q_1) * DT

        # External work integral int C_obs dM.
        work += 0.5 * (force_0 + force_1) * (field_new - field)

        field = field_new
        velocity = velocity_new
        bath_q = bath_q_new
        bath_p = bath_p_new

        shifted = bath_q - (coupling / (omega * omega)) * field
        reservoir_energy = 0.5 * np.sum(
            bath_p * bath_p + (omega * shifted) ** 2
        )
        system_energy = 0.5 * (
            velocity * velocity + OMEGA_M * OMEGA_M * field * field
        )

        fields[index] = field
        velocities[index] = velocity
        bath_coupling_energy[index] = reservoir_energy
        total_energy[index] = system_energy + reservoir_energy
        source_work[index] = work

    return {
        "time": times,
        "field": fields,
        "velocity": velocities,
        "bath_energy": bath_coupling_energy,
        "total_energy": total_energy,
        "source_work": source_work,
    }


def simulate_markovian(gamma: float):
    """Reduced local-friction comparison model."""
    steps = int(T_FINAL / DT)
    times = np.arange(steps) * DT

    field = 0.0
    velocity = 0.0
    fields = np.empty(steps, dtype=float)
    velocities = np.empty(steps, dtype=float)

    # Explicit midpoint/RK2 is sufficient for this reduced comparison.
    for index, time in enumerate(times):
        force = source_force(float(time))
        accel = -gamma * velocity - OMEGA_M * OMEGA_M * field + force

        field_mid = field + 0.5 * DT * velocity
        velocity_mid = velocity + 0.5 * DT * accel
        force_mid = source_force(float(time + 0.5 * DT))
        accel_mid = (
            -gamma * velocity_mid
            - OMEGA_M * OMEGA_M * field_mid
            + force_mid
        )

        field += DT * velocity_mid
        velocity += DT * accel_mid

        fields[index] = field
        velocities[index] = velocity

    return {
        "time": times,
        "field": fields,
        "velocity": velocities,
    }


def rmse(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.sqrt(np.mean((a - b) ** 2)))


def mask_for(times: np.ndarray, window):
    return (times >= window[0]) & (times < window[1])


def build_markov_library():
    return {
        float(gamma): simulate_markovian(float(gamma))
        for gamma in GAMMA_GRID
    }


def evaluate_bath(n_modes: int, library) -> BathResult:
    microscopic = simulate_microscopic(n_modes)
    times = microscopic["time"]
    train_mask = mask_for(times, TRAIN_WINDOW)
    test_mask = mask_for(times, TEST_WINDOW)

    best = None
    for gamma, reduced in library.items():
        train_error = rmse(
            reduced["field"][train_mask],
            microscopic["field"][train_mask],
        )
        if best is None or train_error < best["train_rmse"]:
            best = {
                "gamma": gamma,
                "train_rmse": train_error,
                "heldout_rmse": rmse(
                    reduced["field"][test_mask],
                    microscopic["field"][test_mask],
                ),
                "reduced": reduced,
            }

    gamma = best["gamma"]
    reduced = best["reduced"]

    first = int(ENERGY_WINDOW[0] / DT)
    last = int(ENERGY_WINDOW[1] / DT)

    effective_heat = np.zeros_like(times)
    effective_heat[first:last] = np.cumsum(
        gamma * reduced["velocity"][first:last] ** 2
    ) * DT
    effective_heat[last:] = effective_heat[last - 1]

    bath_gain = microscopic["bath_energy"] - microscopic["bath_energy"][first]
    heat_error = rmse(
        effective_heat[first:last],
        bath_gain[first:last],
    )

    early_mask = mask_for(times, RECURRENCE_EARLY)
    late_mask = mask_for(times, RECURRENCE_LATE)
    recurrence_ratio = float(
        np.max(np.abs(microscopic["field"][late_mask]))
        / (np.max(np.abs(microscopic["field"][early_mask])) + 1e-15)
    )

    # Exact microscopic identity: H0(t)-H0(0)=W_source(t).
    closure_error = float(
        np.max(
            np.abs(
                (microscopic["total_energy"] - microscopic["total_energy"][0])
                - microscopic["source_work"]
            )
        )
    )

    return BathResult(
        bath_modes=n_modes,
        gamma_eff=float(gamma),
        train_rmse=float(best["train_rmse"]),
        heldout_rmse=float(best["heldout_rmse"]),
        effective_heat_rmse=heat_error,
        recurrence_ratio=recurrence_ratio,
        energy_closure_max_error=closure_error,
        final_effective_heat=float(effective_heat[last - 1]),
        final_bath_coupling_energy_gain=float(bath_gain[last - 1]),
    )


def run():
    library = build_markov_library()
    rows = [evaluate_bath(n_modes, library) for n_modes in BATH_SIZES]

    return {
        "claim_level": "synthetic microscopic-bath methodology only",
        "spectral_envelope": {
            "eta": ETA,
            "cutoff": CUTOFF,
            "omega_min": OMEGA_MIN,
            "omega_max": OMEGA_MAX,
        },
        "train_window": TRAIN_WINDOW,
        "heldout_window": TEST_WINDOW,
        "results": [asdict(row) for row in rows],
        "interpretation": {
            "dense_limit": (
                "gamma_eff stabilizes and held-out Markovian prediction improves "
                "as spectral sampling becomes dense"
            ),
            "sparse_limit": (
                "structured finite bath retains non-Markovian recurrence; local "
                "friction fails even though microscopic total energy is conserved"
            ),
            "ontology": (
                "ordinary Hamiltonian bath degrees of freedom can generate reduced "
                "dissipation; this does not establish a novel SoCT damping sector"
            ),
        },
    }


def print_report(payload):
    print("SIM-04M — Microscopic Bath / Emergent Damping")
    print("=" * 55)
    print(
        "modes | gamma_eff | train RMSE | held-out RMSE | heat RMSE | "
        "recurrence | energy closure"
    )
    for row in payload["results"]:
        print(
            f"{row['bath_modes']:5d} | "
            f"{row['gamma_eff']:9.3f} | "
            f"{row['train_rmse']:10.5f} | "
            f"{row['heldout_rmse']:13.5f} | "
            f"{row['effective_heat_rmse']:9.5f} | "
            f"{row['recurrence_ratio']:10.3f} | "
            f"{row['energy_closure_max_error']:.3e}"
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    output = run()
    if args.json:
        print(json.dumps(output, indent=2))
    else:
        print_report(output)
