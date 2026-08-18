#!/usr/bin/env python3
"""SIM-04D: identifiability gate for causal-geometry changes.

Toy-model methodology benchmark only. This is not evidence for SoCT or for
emergent spacetime.

The benchmark has two purposes:

1. test whether a multi-protocol diagnostic panel can separate several common
   mechanisms that can all distort inferred causal geometry;
2. construct explicit non-identifiability counterexamples showing where no
   estimator can identify the underlying mechanism from the restricted
   observations alone.

Easy mechanism families:
    speed            propagation-delay changes at fixed topology/gain
    susceptibility   receiver-gain changes at fixed topology/delay
    topology         edge additions/removals
    memory           ordinary local dynamical memory / response tails

Hard equivalence classes:
    geometry length vs propagation speed       (delay = length / speed)
    hidden mediator vs delayed direct edge     (same observed transfer)
    named memory state vs hidden latent state  (same state-space realization)

Requires:
    numpy
    scikit-learn
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


MECHANISMS = ("speed", "susceptibility", "topology", "memory")
FEATURE_NAMES = (
    "relative_response_change",
    "earliest_lag_mae",
    "reachability_support_change",
    "direct_support_change",
    "peak_amplitude_log_change",
    "local_gain_calibration_change",
    "tail_energy_change",
    "post_reset_persistence",
)


@dataclass
class AccuracySummary:
    repeats: int
    naive_mean: float
    naive_std: float
    response_panel_mean: float
    response_panel_std: float
    full_panel_mean: float
    full_panel_std: float


@dataclass
class EquivalenceSummary:
    geometry_speed_delay_max_abs_error: float
    hidden_mediator_direct_edge_max_abs_error: float
    memory_latent_state_max_abs_error: float


def make_layered_system(seed: int, layers: int = 4, width: int = 4):
    """Create a hidden feed-forward transmission network with integer delays."""
    rng = np.random.default_rng(seed)
    n = layers * width
    edges: list[list[float | int]] = []

    for layer in range(layers - 1):
        sources = np.arange(layer * width, (layer + 1) * width)
        targets = np.arange((layer + 1) * width, (layer + 2) * width)

        for source in sources:
            chosen = rng.choice(targets, size=int(rng.integers(2, 4)), replace=False)
            for target in chosen:
                edges.append(
                    [
                        int(source),
                        int(target),
                        float(rng.uniform(0.18, 0.45)),
                        int(rng.choice([1, 1, 1, 2])),
                    ]
                )

        for target in targets:
            if not any(int(edge[1]) == int(target) for edge in edges if int(edge[0]) // width == layer):
                source = int(rng.choice(sources))
                edges.append(
                    [source, int(target), float(rng.uniform(0.18, 0.45)), 1]
                )

    # A few weak skip-layer paths make reachability less trivial.
    for layer in range(layers - 2):
        for _ in range(2):
            source = int(rng.integers(layer * width, (layer + 1) * width))
            target_layer = layer + 2
            target = int(rng.integers(target_layer * width, (target_layer + 1) * width))
            edges.append([source, target, float(rng.uniform(0.08, 0.20)), 2])

    return n, edges


def response_from_edges(
    n: int,
    edges,
    gains: np.ndarray | None = None,
    max_lag: int = 10,
) -> np.ndarray:
    """Return impulse-response matrices H[k][target, source]."""
    if gains is None:
        gains = np.ones(n, dtype=float)

    max_edge_delay = max(int(edge[3]) for edge in edges)
    matrices = {
        delay: np.zeros((n, n), dtype=float)
        for delay in range(1, max(max_edge_delay, max_lag) + 1)
    }

    for source, target, weight, delay in edges:
        matrices[int(delay)][int(target), int(source)] += (
            float(weight) * float(gains[int(target)])
        )

    response = [np.eye(n, dtype=float)]
    for lag in range(1, max_lag + 1):
        current = np.zeros((n, n), dtype=float)
        for delay, matrix in matrices.items():
            if delay <= lag:
                current += matrix @ response[lag - delay]
        response.append(current)

    return np.asarray(response)


def apply_output_memory(
    response: np.ndarray,
    selected: np.ndarray,
    beta: float,
    rho: float,
) -> np.ndarray:
    """Add an ordinary exponential response-memory kernel to selected outputs."""
    out = response.copy()
    max_lag = response.shape[0] - 1

    for lag in range(1, max_lag + 1):
        for offset in range(1, lag + 1):
            out[lag, selected, :] += (
                beta * (rho ** (offset - 1)) * response[lag - offset, selected, :]
            )
    return out


def support_change(a: np.ndarray, b: np.ndarray) -> float:
    union = np.logical_or(a, b).sum()
    if union == 0:
        return 0.0
    return float(np.logical_xor(a, b).sum() / union)


def response_fingerprint(
    baseline: np.ndarray,
    perturbed: np.ndarray,
    gain_calibration_change: float,
    post_reset_persistence: float,
    threshold: float = 1e-4,
) -> np.ndarray:
    """Build a mechanism-oriented diagnostic fingerprint."""
    max_lag = baseline.shape[0] - 1

    reachable_0 = np.max(np.abs(baseline[1:]), axis=0) > threshold
    reachable_1 = np.max(np.abs(perturbed[1:]), axis=0) > threshold
    direct_0 = np.abs(baseline[1]) > threshold
    direct_1 = np.abs(perturbed[1]) > threshold

    earliest_0 = np.full(reachable_0.shape, np.nan)
    earliest_1 = np.full(reachable_1.shape, np.nan)
    peak_0 = np.zeros(reachable_0.shape, dtype=float)
    peak_1 = np.zeros(reachable_1.shape, dtype=float)

    for lag in range(1, max_lag + 1):
        mask_0 = np.isnan(earliest_0) & (np.abs(baseline[lag]) > threshold)
        mask_1 = np.isnan(earliest_1) & (np.abs(perturbed[lag]) > threshold)
        earliest_0[mask_0] = lag
        earliest_1[mask_1] = lag
        peak_0 = np.maximum(peak_0, np.abs(baseline[lag]))
        peak_1 = np.maximum(peak_1, np.abs(perturbed[lag]))

    common = reachable_0 & reachable_1
    if common.any():
        lag_mae = float(
            np.nanmean(np.abs(earliest_1[common] - earliest_0[common]))
        )
        amplitude_change = float(
            np.median(
                np.abs(
                    np.log(
                        (peak_1[common] + 1e-8)
                        / (peak_0[common] + 1e-8)
                    )
                )
            )
        )
    else:
        lag_mae = 0.0
        amplitude_change = 0.0

    relative_change = float(
        np.linalg.norm(perturbed[1:] - baseline[1:])
        / (np.linalg.norm(baseline[1:]) + 1e-12)
    )

    def tail_fraction(response: np.ndarray) -> float:
        return float(
            np.linalg.norm(response[5:])
            / (np.linalg.norm(response[1:]) + 1e-12)
        )

    return np.asarray(
        [
            relative_change,
            lag_mae,
            support_change(reachable_0, reachable_1),
            support_change(direct_0, direct_1),
            amplitude_change,
            gain_calibration_change,
            abs(tail_fraction(perturbed) - tail_fraction(baseline)),
            post_reset_persistence,
        ],
        dtype=float,
    )


def sample_mechanism(
    seed: int,
    mechanism: str,
    strength_range: tuple[float, float],
) -> np.ndarray:
    rng = np.random.default_rng(seed)
    n, edges = make_layered_system(seed)
    baseline = response_from_edges(n, edges)
    strength = float(rng.uniform(*strength_range))

    gain_change = 0.0
    post_reset = 0.0

    if mechanism == "speed":
        changed = [edge.copy() for edge in edges]
        count = max(1, int((0.15 + 0.35 * strength) * len(changed)))
        indices = rng.choice(len(changed), size=count, replace=False)
        for index in indices:
            extra = 1 if strength < 0.7 else int(rng.integers(1, 3))
            changed[index][3] = min(4, int(changed[index][3]) + extra)
        perturbed = response_from_edges(n, changed)

    elif mechanism == "susceptibility":
        gains = np.ones(n, dtype=float)
        count = max(2, int((0.15 + 0.25 * strength) * n))
        selected = rng.choice(np.arange(4, n), size=count, replace=False)
        multipliers = np.exp(
            rng.normal(0.0, 0.25 + 0.45 * strength, size=count)
        )
        gains[selected] = multipliers
        gain_change = float(np.median(np.abs(np.log(multipliers))))
        perturbed = response_from_edges(n, edges, gains=gains)

    elif mechanism == "topology":
        changed = [edge.copy() for edge in edges]
        count = max(1, int((0.05 + 0.12 * strength) * len(changed)))
        removal = sorted(
            rng.choice(len(changed), size=count, replace=False), reverse=True
        )
        for index in removal:
            changed.pop(int(index))

        for _ in range(count):
            source_layer = int(rng.integers(0, 3))
            source = int(rng.integers(source_layer * 4, (source_layer + 1) * 4))
            target_layer = int(rng.integers(source_layer + 1, 4))
            target = int(rng.integers(target_layer * 4, (target_layer + 1) * 4))
            changed.append(
                [
                    source,
                    target,
                    float(rng.uniform(0.10, 0.40)),
                    int(rng.integers(1, 3)),
                ]
            )
        perturbed = response_from_edges(n, changed)

    elif mechanism == "memory":
        count = max(2, int((0.15 + 0.25 * strength) * n))
        selected = rng.choice(np.arange(4, n), size=count, replace=False)
        beta = 0.08 + 0.25 * strength
        rho = 0.45 + 0.45 * strength
        perturbed = apply_output_memory(baseline, selected, beta, rho)
        post_reset = float(beta * (rho ** 4))

    else:
        raise ValueError(f"unknown mechanism: {mechanism}")

    features = response_fingerprint(
        baseline,
        perturbed,
        gain_calibration_change=gain_change,
        post_reset_persistence=post_reset,
    )

    # Modest measurement noise prevents the diagnostics from being exact labels.
    feature_noise = np.asarray(
        [0.01, 0.02, 0.005, 0.005, 0.01, 0.01, 0.005, 0.003]
    )
    return features + feature_noise * rng.normal(size=len(features))


def make_dataset(
    offset: int,
    per_class: int,
    strength_range: tuple[float, float] | None,
    split_extremes: bool,
):
    rows = []
    labels = []

    for class_index, mechanism in enumerate(MECHANISMS):
        for index in range(per_class):
            if split_extremes:
                if index < per_class // 2:
                    current_range = (0.12, 0.35)
                else:
                    current_range = (0.75, 0.98)
            else:
                assert strength_range is not None
                current_range = strength_range

            seed = offset + class_index * 10_000 + index
            rows.append(sample_mechanism(seed, mechanism, current_range))
            labels.append(mechanism)

    return np.asarray(rows), np.asarray(labels)


def score_panel(
    x_train: np.ndarray,
    y_train: np.ndarray,
    x_test: np.ndarray,
    y_test: np.ndarray,
    feature_indices: list[int],
):
    model = make_pipeline(
        StandardScaler(),
        LogisticRegression(max_iter=2500, random_state=0),
    )
    model.fit(x_train[:, feature_indices], y_train)
    prediction = model.predict(x_test[:, feature_indices])
    return (
        float(accuracy_score(y_test, prediction)),
        confusion_matrix(y_test, prediction, labels=MECHANISMS),
    )


def run_classification(
    repeats: int,
    train_per_class: int,
    test_per_class: int,
):
    naive_scores = []
    response_scores = []
    full_scores = []
    last_confusion = None

    naive_features = [0, 1, 2]
    response_panel = [0, 1, 2, 3, 4, 6]
    full_panel = list(range(len(FEATURE_NAMES)))

    for repeat in range(repeats):
        offset = repeat * 100_000
        x_train, y_train = make_dataset(
            offset,
            train_per_class,
            strength_range=(0.30, 0.75),
            split_extremes=False,
        )
        x_test, y_test = make_dataset(
            offset + 50_000,
            test_per_class,
            strength_range=None,
            split_extremes=True,
        )

        naive, _ = score_panel(
            x_train, y_train, x_test, y_test, naive_features
        )
        response, _ = score_panel(
            x_train, y_train, x_test, y_test, response_panel
        )
        full, confusion = score_panel(
            x_train, y_train, x_test, y_test, full_panel
        )

        naive_scores.append(naive)
        response_scores.append(response)
        full_scores.append(full)
        last_confusion = confusion

    summary = AccuracySummary(
        repeats=repeats,
        naive_mean=float(np.mean(naive_scores)),
        naive_std=float(np.std(naive_scores)),
        response_panel_mean=float(np.mean(response_scores)),
        response_panel_std=float(np.std(response_scores)),
        full_panel_mean=float(np.mean(full_scores)),
        full_panel_std=float(np.std(full_scores)),
    )
    return summary, last_confusion


def equivalence_geometry_vs_speed() -> float:
    rng = np.random.default_rng(7)
    length = rng.uniform(0.2, 5.0, size=1000)
    speed = rng.uniform(0.5, 3.0, size=1000)
    scale = rng.uniform(1.1, 2.5, size=1000)

    geometry_stretch_delay = (scale * length) / speed
    medium_slowdown_delay = length / (speed / scale)
    return float(np.max(np.abs(geometry_stretch_delay - medium_slowdown_delay)))


def equivalence_hidden_mediator_vs_delayed_edge() -> float:
    rng = np.random.default_rng(8)
    first = rng.uniform(0.1, 0.9, size=1000)
    second = rng.uniform(0.1, 0.9, size=1000)

    hidden_mediator_lag2 = first * second
    direct_delayed_edge_lag2 = first * second
    return float(np.max(np.abs(hidden_mediator_lag2 - direct_delayed_edge_lag2)))


def equivalence_memory_vs_latent_state() -> float:
    rng = np.random.default_rng(9)
    signal = rng.normal(size=2000)
    rho = 0.83
    beta = 0.27

    # Description A calls the internal variable a memory state.
    memory_state = 0.0
    output_memory = np.zeros_like(signal)
    for index, value in enumerate(signal):
        output_memory[index] = value + memory_state
        memory_state = rho * memory_state + beta * value

    # Description B calls the mathematically identical variable an unobserved
    # latent state. Restricted input/output observations cannot choose ontology.
    latent_state = 0.0
    output_latent = np.zeros_like(signal)
    for index, value in enumerate(signal):
        output_latent[index] = value + latent_state
        latent_state = rho * latent_state + beta * value

    return float(np.max(np.abs(output_memory - output_latent)))


def run_equivalence_tests() -> EquivalenceSummary:
    return EquivalenceSummary(
        geometry_speed_delay_max_abs_error=equivalence_geometry_vs_speed(),
        hidden_mediator_direct_edge_max_abs_error=(
            equivalence_hidden_mediator_vs_delayed_edge()
        ),
        memory_latent_state_max_abs_error=equivalence_memory_vs_latent_state(),
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repeats", type=int, default=8)
    parser.add_argument("--train-per-class", type=int, default=150)
    parser.add_argument("--test-per-class", type=int, default=100)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    accuracy, confusion = run_classification(
        repeats=args.repeats,
        train_per_class=args.train_per_class,
        test_per_class=args.test_per_class,
    )
    equivalence = run_equivalence_tests()

    if args.json:
        print(
            json.dumps(
                {
                    "accuracy": asdict(accuracy),
                    "equivalence": asdict(equivalence),
                    "feature_names": FEATURE_NAMES,
                    "last_full_panel_confusion": confusion.tolist(),
                    "mechanism_order": MECHANISMS,
                },
                indent=2,
            )
        )
        return

    print("SIM-04D identifiability gate")
    print()
    print(
        f"naive panel:    {accuracy.naive_mean:.4f} +/- {accuracy.naive_std:.4f}"
    )
    print(
        "response panel: "
        f"{accuracy.response_panel_mean:.4f} +/- {accuracy.response_panel_std:.4f}"
    )
    print(
        f"full panel:     {accuracy.full_panel_mean:.4f} +/- {accuracy.full_panel_std:.4f}"
    )
    print()
    print("exact non-identifiability counterexamples (max absolute difference)")
    print(
        "geometry vs speed:        "
        f"{equivalence.geometry_speed_delay_max_abs_error:.3e}"
    )
    print(
        "hidden mediator vs edge:  "
        f"{equivalence.hidden_mediator_direct_edge_max_abs_error:.3e}"
    )
    print(
        "memory vs latent state:   "
        f"{equivalence.memory_latent_state_max_abs_error:.3e}"
    )


if __name__ == "__main__":
    main()
