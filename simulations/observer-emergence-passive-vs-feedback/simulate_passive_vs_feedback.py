#!/usr/bin/env python3
"""O-1A: passive memory versus causal feedback.

Two agents have the same memory capacity and receive the same kind of noisy
observations. The passive agent stores the previous observation but does not use
it to select its next sensor. The feedback agent uses the stored record to
choose a specialized sensor. The latent world is a persistent binary Markov
process.

Purpose: quantify the causal contribution of record reuse to later information
acquisition. This is a control/information-theory toy model, not evidence for
consciousness, objective collapse, or SoCT-specific physics.
"""

import csv
import math
import random
from collections import Counter
from pathlib import Path


def mutual_information(pairs):
    n = len(pairs)
    joint = Counter(pairs)
    cw = Counter(w for w, y in pairs)
    cy = Counter(y for w, y in pairs)
    mi = 0.0
    for (w, y), count in joint.items():
        pxy = count / n
        pw = cw[w] / n
        py = cy[y] / n
        mi += pxy * math.log(pxy / (pw * py), 2)
    return mi


def run_agent(persistence, feedback, seed=42, steps=200000):
    rng = random.Random(seed)
    world = rng.choice([0, 1])
    memory = rng.choice([0, 1])
    pairs = []
    correct = 0

    for _ in range(steps):
        if rng.random() > persistence:
            world = 1 - world

        # Two specialized sensors. A sensor matched to the current world state
        # has 0.90 accuracy; the other has 0.55 accuracy. The feedback agent
        # selects using its stored previous observation. The passive-control
        # agent stores the same one-bit memory but sensor choice is randomized.
        sensor = memory if feedback else rng.choice([0, 1])
        accuracy = 0.90 if sensor == world else 0.55
        observation = world if rng.random() < accuracy else 1 - world

        pairs.append((world, observation))
        correct += int(observation == world)
        memory = observation

    return correct / steps, mutual_information(pairs)


def main():
    out = Path(__file__).with_name("results.csv")
    rows = []
    for persistence in [0.50, 0.70, 0.90, 0.97]:
        passive_acc, passive_mi = run_agent(persistence, False)
        feedback_acc, feedback_mi = run_agent(persistence, True)
        rows.append({
            "world_persistence": persistence,
            "passive_accuracy": passive_acc,
            "feedback_accuracy": feedback_acc,
            "accuracy_gain": feedback_acc - passive_acc,
            "passive_MI_bits": passive_mi,
            "feedback_MI_bits": feedback_mi,
            "MI_gain_bits": feedback_mi - passive_mi,
        })

    with out.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print(f"wrote {out}")


if __name__ == "__main__":
    main()
