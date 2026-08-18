#!/usr/bin/env python3
"""SIM-02: Hidden State vs Genuine Memory.

Demonstrates that conditional history dependence can reveal an incomplete
observed state but cannot, by itself, determine whether the missing predictive
state should be called an ordinary hidden variable or a physical memory degree
of freedom.

All models are intentionally simple binary stochastic processes. The statistic
is empirical conditional mutual information I(H;F|X), followed by state
augmentation I(H;F|X,A) where A is the model's known latent/memory state.
"""

from __future__ import annotations

import argparse
import math
import random
from collections import Counter
from typing import Iterable, List, Sequence, Tuple


Row = Tuple[int, int, int, int]  # H, X, F, A


def conditional_mutual_information(
    rows: Sequence[Row], h_index: int, f_index: int, condition_indices: Sequence[int]
) -> float:
    """Empirical conditional mutual information in bits."""
    n = len(rows)
    joint = Counter()
    h_cond = Counter()
    f_cond = Counter()
    cond = Counter()

    for row in rows:
        h = row[h_index]
        f = row[f_index]
        c = tuple(row[i] for i in condition_indices)
        joint[(h, f, c)] += 1
        h_cond[(h, c)] += 1
        f_cond[(f, c)] += 1
        cond[c] += 1

    value = 0.0
    for (h, f, c), count in joint.items():
        ratio = (count * cond[c]) / (h_cond[(h, c)] * f_cond[(f, c)])
        value += (count / n) * math.log(ratio, 2)
    return value


def markov_model(n: int, seed: int) -> List[Row]:
    rng = random.Random(seed)
    x = rng.randrange(2)
    sequence = [x]
    for _ in range(n + 1):
        p_one = 0.8 if x else 0.2
        x = 1 if rng.random() < p_one else 0
        sequence.append(x)
    return [
        (sequence[t - 1], sequence[t], sequence[t + 1], 0)
        for t in range(1, n + 1)
    ]


def hidden_markov_model(n: int, seed: int) -> List[Row]:
    rng = random.Random(seed)
    z = rng.randrange(2)
    hidden: List[int] = []
    observed: List[int] = []

    for t in range(n + 2):
        if t > 0 and rng.random() > 0.95:
            z = 1 - z
        x = z if rng.random() < 0.80 else 1 - z
        hidden.append(z)
        observed.append(x)

    return [
        (observed[t - 1], observed[t], observed[t + 1], hidden[t])
        for t in range(1, n + 1)
    ]


def second_order_memory_model(n: int, seed: int) -> List[Row]:
    rng = random.Random(seed)
    x = [rng.randrange(2), rng.randrange(2)]

    for t in range(1, n + 1):
        previous = x[t - 1]
        current = x[t]
        target = 1 if previous == current else 0
        future = target if rng.random() < 0.85 else 1 - target
        x.append(future)

    # A is the exact finite memory state needed by this toy process.
    return [(x[t - 1], x[t], x[t + 1], x[t - 1]) for t in range(1, n + 1)]


def dynamic_memory_model(n: int, seed: int) -> List[Row]:
    rng = random.Random(seed)
    x = rng.randrange(2)
    memory = rng.randrange(2)
    observed = [x]
    memories = [memory]

    for _ in range(n + 1):
        target = x ^ memory
        future = target if rng.random() < 0.85 else 1 - target
        memory_next = x if rng.random() < 0.25 else memory
        x, memory = future, memory_next
        observed.append(x)
        memories.append(memory)

    return [
        (observed[t - 1], observed[t], observed[t + 1], memories[t])
        for t in range(1, n + 1)
    ]


def analyze(name: str, rows: Sequence[Row]):
    incomplete = conditional_mutual_information(rows, 0, 2, [1])
    augmented = conditional_mutual_information(rows, 0, 2, [1, 3])
    return name, incomplete, augmented, incomplete - augmented


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=int, default=200000)
    parser.add_argument("--seed", type=int, default=20260817)
    args = parser.parse_args()

    models = [
        ("fully_observed_markov", markov_model(args.samples, args.seed)),
        ("hidden_markov_state", hidden_markov_model(args.samples, args.seed + 1)),
        ("finite_second_order_memory", second_order_memory_model(args.samples, args.seed + 2)),
        ("dynamic_memory_state", dynamic_memory_model(args.samples, args.seed + 3)),
    ]

    print("model,I(H;F|X)_bits,I(H;F|X,A)_bits,reduction_bits")
    for name, rows in models:
        result = analyze(name, rows)
        print(f"{result[0]},{result[1]:.12e},{result[2]:.12e},{result[3]:.12e}")

    print("\nInterpretation:")
    print("- I(H;F|X) > 0 flags an incomplete observed state description.")
    print("- If adding A drives the residual toward zero, A completes the predictive state.")
    print("- This criterion alone does not decide whether A is 'hidden state' or 'memory'.")
    print("- A SoCT-specific M therefore needs a specified update law, coupling, and intervention test.")


if __name__ == "__main__":
    main()
