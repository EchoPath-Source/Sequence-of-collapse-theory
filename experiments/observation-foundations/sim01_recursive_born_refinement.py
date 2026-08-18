#!/usr/bin/env python3
"""SIM-01: Recursive Born Refinement.

Tests the restricted family P_i ∝ |alpha_i|^p for invariance when one
orthogonal record branch is refined into m equal subbranches with amplitude
alpha/sqrt(m), then coarse-grained back to the original branch.

This is a consistency test inside Hilbert-space quantum mechanics. It does not
derive Hilbert space, unitarity, orthogonality, probability additivity, or
single-outcome selection.
"""

from __future__ import annotations

import argparse
import math
import random
import statistics
from dataclasses import dataclass
from typing import Iterable, List, Sequence, Tuple


ComplexVector = List[complex]
Operation = Tuple[int, int]


@dataclass(frozen=True)
class Case:
    amplitudes: Tuple[complex, ...]
    refinements: Tuple[Operation, ...]


def normalize(values: Sequence[complex]) -> ComplexVector:
    norm = math.sqrt(sum(abs(z) ** 2 for z in values))
    if norm == 0.0:
        raise ValueError("zero vector cannot be normalized")
    return [z / norm for z in values]


def probabilities(amplitudes: Sequence[complex], exponent: float) -> List[float]:
    weights = [abs(a) ** exponent for a in amplitudes]
    total = sum(weights)
    return [w / total for w in weights]


def refine(
    amplitudes: Sequence[complex],
    labels: Sequence[int],
    index: int,
    multiplicity: int,
) -> Tuple[ComplexVector, List[int]]:
    if multiplicity < 2:
        raise ValueError("refinement multiplicity must be >= 2")
    child_amplitude = amplitudes[index] / math.sqrt(multiplicity)
    label = labels[index]
    new_amplitudes = (
        list(amplitudes[:index])
        + [child_amplitude] * multiplicity
        + list(amplitudes[index + 1 :])
    )
    new_labels = (
        list(labels[:index])
        + [label] * multiplicity
        + list(labels[index + 1 :])
    )
    return new_amplitudes, new_labels


def generate_cases(seed: int, trials: int, recursive_steps: int) -> List[Case]:
    rng = random.Random(seed)
    cases: List[Case] = []
    for _ in range(trials):
        n = rng.randint(2, 8)
        amplitudes = normalize(
            [complex(rng.gauss(0.0, 1.0), rng.gauss(0.0, 1.0)) for _ in range(n)]
        )
        operations: List[Operation] = []
        current_length = n
        for _ in range(recursive_steps):
            index = rng.randrange(current_length)
            multiplicity = rng.randint(2, 8)
            operations.append((index, multiplicity))
            current_length += multiplicity - 1
        cases.append(Case(tuple(amplitudes), tuple(operations)))
    return cases


def case_error(case: Case, exponent: float) -> Tuple[float, float]:
    amplitudes = list(case.amplitudes)
    original_count = len(amplitudes)
    labels = list(range(original_count))
    original_probabilities = probabilities(amplitudes, exponent)

    for index, multiplicity in case.refinements:
        amplitudes, labels = refine(amplitudes, labels, index, multiplicity)

    refined_probabilities = probabilities(amplitudes, exponent)
    coarse_probabilities = [0.0] * original_count
    for probability, label in zip(refined_probabilities, labels):
        coarse_probabilities[label] += probability

    errors = [
        abs(before - after)
        for before, after in zip(original_probabilities, coarse_probabilities)
    ]
    return statistics.fmean(errors), max(errors)


def evaluate(cases: Sequence[Case], exponents: Iterable[float]):
    rows = []
    for exponent in exponents:
        errors = [case_error(case, exponent) for case in cases]
        rows.append(
            {
                "p": exponent,
                "mean_abs_coarse_error": statistics.fmean(e[0] for e in errors),
                "mean_max_branch_error": statistics.fmean(e[1] for e in errors),
                "worst_max_branch_error": max(e[1] for e in errors),
            }
        )
    return rows


def print_rows(title: str, rows, limit: int | None = None) -> None:
    print(f"\n{title}")
    print("p,mean_abs_coarse_error,mean_max_branch_error,worst_max_branch_error")
    chosen = rows if limit is None else rows[:limit]
    for row in chosen:
        print(
            f"{row['p']:.6f},"
            f"{row['mean_abs_coarse_error']:.12e},"
            f"{row['mean_max_branch_error']:.12e},"
            f"{row['worst_max_branch_error']:.12e}"
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--single-trials", type=int, default=5000)
    parser.add_argument("--recursive-trials", type=int, default=2000)
    parser.add_argument("--recursive-steps", type=int, default=12)
    parser.add_argument("--seed", type=int, default=20260817)
    args = parser.parse_args()

    scan = [0.5 + 0.025 * i for i in range(int((4.0 - 0.5) / 0.025) + 1)]
    single_cases = generate_cases(args.seed, args.single_trials, 1)
    single_rows = evaluate(single_cases, scan)
    ranked = sorted(single_rows, key=lambda row: row["mean_abs_coarse_error"])
    print_rows("Single-refinement exponent scan: best 10", ranked, limit=10)

    checkpoints = [1.0, 1.5, 1.9, 1.99, 2.0, 2.01, 2.1, 2.5, 3.0]
    recursive_cases = generate_cases(
        args.seed + 1, args.recursive_trials, args.recursive_steps
    )
    recursive_rows = evaluate(recursive_cases, checkpoints)
    print_rows(
        f"Recursive refinement checkpoints ({args.recursive_steps} nested refinements)",
        recursive_rows,
    )

    best = ranked[0]
    print("\nBest exponent on scan:")
    print(f"p={best['p']:.6f}")
    print(f"mean_abs_coarse_error={best['mean_abs_coarse_error']:.12e}")


if __name__ == "__main__":
    main()
