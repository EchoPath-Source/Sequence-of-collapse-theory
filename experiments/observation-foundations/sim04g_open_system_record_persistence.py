#!/usr/bin/env python3
"""SIM-04G: explicit qubit + detector + environment record-persistence benchmark.

Toy-model methodology test only. This is not evidence for SoCT, objective
collapse, or consciousness-induced physics.

The benchmark asks whether peak decoherence, pointer correlation, persistent
records, erasure, and environmental redundancy are operationally distinct.

Five qubits are used:

    S, D, E1, E2, E3

S starts in |+>. D and all E fragments start in |0>.

A partial measurement interaction is

    U_SD(theta) = |0><0|_S tensor I_D
                + |1><1|_S tensor R_y(2 theta)_D.

Environment records are created by CNOT-like copies from D to selected E
fragments. Local unmeasurement applies U_SD(theta)^dagger. Optional record
erasure reverses the D-E copy operations first.

Requires:
    numpy
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass

import numpy as np


N_QUBITS = 5
S = 0
D = 1
ENV = (2, 3, 4)

I2 = np.eye(2, dtype=complex)
X = np.asarray([[0, 1], [1, 0]], dtype=complex)
H = np.asarray([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2.0)
P0 = np.asarray([[1, 0], [0, 0]], dtype=complex)
P1 = np.asarray([[0, 0], [0, 1]], dtype=complex)


@dataclass
class ScenarioResult:
    theta: float
    scenario: str
    peak_decoherence_loss: float
    peak_system_detector_qmi: float
    environment_qmi_after_copy_sum: float
    final_recovered_coherence: float
    final_recovery_deficit: float
    final_environment_qmi_sum: float


def ry(angle: float) -> np.ndarray:
    return np.asarray(
        [
            [np.cos(angle / 2.0), -np.sin(angle / 2.0)],
            [np.sin(angle / 2.0), np.cos(angle / 2.0)],
        ],
        dtype=complex,
    )


def kron_all(operators) -> np.ndarray:
    result = operators[0]
    for operator in operators[1:]:
        result = np.kron(result, operator)
    return result


def apply_single(state: np.ndarray, unitary: np.ndarray, qubit: int) -> np.ndarray:
    operators = [I2 for _ in range(N_QUBITS)]
    operators[qubit] = unitary
    return kron_all(operators) @ state


def apply_controlled(
    state: np.ndarray,
    unitary: np.ndarray,
    control: int,
    target: int,
) -> np.ndarray:
    branch_zero = []
    branch_one = []

    for qubit in range(N_QUBITS):
        if qubit == control:
            branch_zero.append(P0)
            branch_one.append(P1)
        elif qubit == target:
            branch_zero.append(I2)
            branch_one.append(unitary)
        else:
            branch_zero.append(I2)
            branch_one.append(I2)

    return (kron_all(branch_zero) + kron_all(branch_one)) @ state


def initial_state() -> np.ndarray:
    state = np.zeros(2**N_QUBITS, dtype=complex)
    state[0] = 1.0
    return apply_single(state, H, S)


def reduced_density(state: np.ndarray, keep) -> np.ndarray:
    keep = list(keep)
    traced = [q for q in range(N_QUBITS) if q not in keep]
    tensor = state.reshape([2] * N_QUBITS)
    tensor = np.transpose(tensor, keep + traced)
    matrix = tensor.reshape(2 ** len(keep), 2 ** len(traced))
    return matrix @ matrix.conj().T


def entropy(rho: np.ndarray) -> float:
    eigenvalues = np.linalg.eigvalsh(rho).real
    eigenvalues = eigenvalues[eigenvalues > 1e-12]
    return float(-np.sum(eigenvalues * np.log2(eigenvalues)))


def quantum_mutual_information(state: np.ndarray, a, b) -> float:
    rho_a = reduced_density(state, a)
    rho_b = reduced_density(state, b)
    rho_ab = reduced_density(state, list(a) + list(b))
    return entropy(rho_a) + entropy(rho_b) - entropy(rho_ab)


def system_coherence(state: np.ndarray) -> float:
    rho_s = reduced_density(state, [S])
    # Normalized so |+> has coherence 1.
    return float(2.0 * abs(rho_s[0, 1]))


def measurement(state: np.ndarray, theta: float) -> np.ndarray:
    return apply_controlled(state, ry(2.0 * theta), S, D)


def unmeasurement(state: np.ndarray, theta: float) -> np.ndarray:
    return apply_controlled(state, ry(-2.0 * theta), S, D)


def copy_detector_to_environment(state: np.ndarray, fragment: int) -> np.ndarray:
    return apply_controlled(state, X, D, fragment)


def run_scenario(theta: float, scenario: str) -> ScenarioResult:
    state = initial_state()
    state = measurement(state, theta)

    peak_coherence = system_coherence(state)
    peak_sd_qmi = quantum_mutual_information(state, [S], [D])

    if scenario == "reversible":
        fragments = ()
        erase_before_unmeasure = False
    elif scenario == "persistent_1":
        fragments = ENV[:1]
        erase_before_unmeasure = False
    elif scenario == "redundant_3":
        fragments = ENV
        erase_before_unmeasure = False
    elif scenario == "erased_3":
        fragments = ENV
        erase_before_unmeasure = True
    else:
        raise ValueError(f"unknown scenario: {scenario}")

    for fragment in fragments:
        state = copy_detector_to_environment(state, fragment)

    environment_qmi_after_copy = float(
        sum(
            quantum_mutual_information(state, [S], [fragment])
            for fragment in fragments
        )
    )

    if erase_before_unmeasure:
        for fragment in reversed(fragments):
            state = copy_detector_to_environment(state, fragment)

    state = unmeasurement(state, theta)

    final_coherence = system_coherence(state)
    final_environment_qmi = float(
        sum(
            quantum_mutual_information(state, [S], [fragment])
            for fragment in fragments
        )
    )

    return ScenarioResult(
        theta=float(theta),
        scenario=scenario,
        peak_decoherence_loss=float(1.0 - peak_coherence),
        peak_system_detector_qmi=float(peak_sd_qmi),
        environment_qmi_after_copy_sum=environment_qmi_after_copy,
        final_recovered_coherence=float(final_coherence),
        final_recovery_deficit=float(1.0 - final_coherence),
        final_environment_qmi_sum=final_environment_qmi,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    thetas = (0.4, 0.8, 1.0, 1.2)
    scenarios = ("reversible", "persistent_1", "redundant_3", "erased_3")
    results = [
        run_scenario(theta, scenario)
        for theta in thetas
        for scenario in scenarios
    ]

    if args.json:
        print(json.dumps([asdict(result) for result in results], indent=2))
        return

    print("SIM-04G open-system record-persistence benchmark")
    for result in results:
        print(
            f"theta={result.theta:.1f} "
            f"{result.scenario:12s} "
            f"peak_loss={result.peak_decoherence_loss:.3f} "
            f"env_copy_qmi={result.environment_qmi_after_copy_sum:.3f} "
            f"final_coherence={result.final_recovered_coherence:.3f} "
            f"final_env_qmi={result.final_environment_qmi_sum:.3f}"
        )


if __name__ == "__main__":
    main()
