#!/usr/bin/env python3
"""SIM-04B: geometry from causal order + interval count + delay.

Toy-model methodology benchmark only. This is not evidence for SoCT or for
emergent spacetime.

The benchmark uses uniformly sprinkled events in finite flat Minkowski boxes
(1+1 and 2+1 dimensions) and asks how much metric information can be recovered
when coordinates are hidden from the estimator.

Core estimator:
    causal order -> Alexandrov-interval count N_ij
    N_ij + global event density -> estimated proper time tau_hat
    tau_hat + measured coordinate/propagation delay -> estimated spatial
    separation for causally related pairs

Adversaries:
    random event thinning
    nonuniform sampling density
    nonlocal/shortcut causal relations
    heterogeneous delay/clock calibration

Requires:
    numpy
    scipy
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass

import numpy as np
from scipy.stats import spearmanr


SCENARIOS = (
    "uniform",
    "random_thinning",
    "density_gradient",
    "shortcuts",
    "variable_delay",
)


@dataclass
class Summary:
    spacetime_dimension: int
    scenario: str
    seeds: int
    observed_events_mean: float
    evaluated_pairs_mean: float
    proper_time_count_rho_mean: float
    proper_time_count_rho_std: float
    proper_time_delay_rho_mean: float
    proper_time_delay_rho_std: float
    proper_time_count_rmse_mean: float
    spatial_rho_raw_delay_mean: float
    spatial_rho_raw_delay_std: float
    spatial_rho_calibrated_delay_mean: float
    spatial_rho_calibrated_delay_std: float
    false_causal_fraction_mean: float
    false_causal_fraction_std: float


def causal_interval_coefficient(d: int) -> float:
    """Coefficient zeta_d for a flat d-dimensional Alexandrov interval.

    V_d(tau) = zeta_d * tau**d

    Here d is spacetime dimension: d=2 means 1+1 and d=3 means 2+1.
    """
    spatial_dimension = d - 1
    unit_ball_volume = (
        math.pi ** (spatial_dimension / 2)
        / math.gamma(spatial_dimension / 2 + 1)
    )
    return unit_ball_volume / (2 ** (d - 1) * d)


def sample_events(
    d: int,
    n: int,
    time_extent: float,
    space_extent: float,
    seed: int,
    scenario: str,
) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)
    t = rng.uniform(0.0, time_extent, n)

    if scenario == "density_gradient":
        # Deliberately violate the homogeneous sprinkling assumption.
        u = rng.beta(1.3, 3.0, size=(n, d - 1))
        x = (u - 0.5) * space_extent
    else:
        x = rng.uniform(
            -space_extent / 2,
            space_extent / 2,
            size=(n, d - 1),
        )

    if scenario == "random_thinning":
        keep = rng.random(n) < 0.55
        t = t[keep]
        x = x[keep]

    return t, x


def minkowski_relations(
    t: np.ndarray,
    x: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Return causal order, coordinate-time gap, spatial gap, and proper time."""
    dt = t[None, :] - t[:, None]
    dx = x[None, :, :] - x[:, None, :]
    r = np.linalg.norm(dx, axis=2)
    order = (dt > 0.0) & (dt >= r)
    tau = np.sqrt(np.maximum(dt**2 - r**2, 0.0))
    return order, dt, r, tau


def add_shortcuts_and_close(
    order: np.ndarray,
    t: np.ndarray,
    rng: np.random.Generator,
    fraction: float = 0.0015,
) -> tuple[np.ndarray, int]:
    """Inject forward-in-time nonlocal relations, then restore transitivity."""
    forward = (t[None, :] - t[:, None]) > 0.0
    candidates = np.argwhere(forward & ~order)
    if len(candidates) == 0:
        return order.copy(), 0

    shortcut_count = max(1, int(fraction * len(candidates)))
    chosen = candidates[
        rng.choice(len(candidates), shortcut_count, replace=False)
    ]

    reach = order.copy()
    reach[chosen[:, 0], chosen[:, 1]] = True

    # All relations point toward increasing coordinate time, so time order is a
    # valid topological ordering for a simple transitive-closure pass.
    for k in np.argsort(t):
        ancestors = np.flatnonzero(reach[:, k])
        descendants = np.flatnonzero(reach[k, :])
        if ancestors.size and descendants.size:
            reach[np.ix_(ancestors, descendants)] = True

    return reach, shortcut_count


def safe_spearman(a: np.ndarray, b: np.ndarray) -> float:
    result = spearmanr(a, b).statistic
    return float(result) if np.isfinite(result) else 0.0


def run_seed(
    d: int,
    n: int,
    time_extent: float,
    space_extent: float,
    seed: int,
    scenario: str,
    max_pairs: int,
) -> dict[str, float]:
    rng = np.random.default_rng(seed + 10_000)
    t, x = sample_events(
        d=d,
        n=n,
        time_extent=time_extent,
        space_extent=space_extent,
        seed=seed,
        scenario=scenario,
    )

    true_order, dt, spatial_gap, true_tau = minkowski_relations(t, x)
    observed_order = true_order.copy()
    shortcut_count = 0

    if scenario == "shortcuts":
        observed_order, shortcut_count = add_shortcuts_and_close(
            true_order, t, rng
        )

    # N_ij = number of observed events k with i < k < j.
    order_int = observed_order.astype(np.int16)
    interval_count = (order_int @ order_int).astype(np.int32)

    spacetime_volume = time_extent * space_extent ** (d - 1)
    observed_density = len(t) / spacetime_volume
    zeta = causal_interval_coefficient(d)

    tau_from_count = (
        np.maximum(interval_count, 0) / (observed_density * zeta)
    ) ** (1.0 / d)

    # Delay is an independently available operational quantity. In the
    # variable-delay adversary, node-specific clock/propagation factors distort
    # the raw value. A separate calibration can remove the imposed distortion.
    raw_delay = dt.copy()
    calibrated_delay = dt.copy()
    if scenario == "variable_delay":
        node_scale = np.exp(rng.normal(0.0, 0.35, size=len(t)))
        pair_scale = np.sqrt(node_scale[:, None] * node_scale[None, :])
        raw_delay = dt * pair_scale
        calibrated_delay = raw_delay / pair_scale

    # Restrict evaluation to true timelike pairs whose causal diamonds are
    # comfortably inside the finite spatial box, reducing simple boundary bias.
    midpoint = (x[:, None, :] + x[None, :, :]) / 2.0
    interior = np.all(
        np.abs(midpoint) + dt[:, :, None] / 2.0 < space_extent / 2.0,
        axis=2,
    )
    mask = true_order & interior & (interval_count >= 3)
    pairs = np.argwhere(mask)

    if len(pairs) > max_pairs:
        pairs = pairs[rng.choice(len(pairs), max_pairs, replace=False)]
    if len(pairs) < 20:
        raise RuntimeError(
            f"too few evaluable pairs for d={d}, scenario={scenario}, seed={seed}"
        )

    i = pairs[:, 0]
    j = pairs[:, 1]

    tau_true = true_tau[i, j]
    tau_count = tau_from_count[i, j]
    delay_raw = raw_delay[i, j]
    delay_cal = calibrated_delay[i, j]
    spatial_true = spatial_gap[i, j]

    # In c=1 flat spacetime, r^2 = dt^2 - tau^2. This step intentionally asks
    # whether count-derived timelike scale plus an operational delay can recover
    # spatial separation for causally related pairs.
    spatial_raw = np.sqrt(np.maximum(delay_raw**2 - tau_count**2, 0.0))
    spatial_cal = np.sqrt(np.maximum(delay_cal**2 - tau_count**2, 0.0))

    false_causal_fraction = float(
        np.sum(observed_order & ~true_order) / max(int(observed_order.sum()), 1)
    )

    return {
        "observed_events": float(len(t)),
        "evaluated_pairs": float(len(pairs)),
        "proper_time_count_rho": safe_spearman(tau_count, tau_true),
        "proper_time_delay_rho": safe_spearman(delay_raw, tau_true),
        "proper_time_count_rmse": float(
            np.sqrt(np.mean((tau_count - tau_true) ** 2))
        ),
        "spatial_rho_raw_delay": safe_spearman(spatial_raw, spatial_true),
        "spatial_rho_calibrated_delay": safe_spearman(
            spatial_cal, spatial_true
        ),
        "false_causal_fraction": false_causal_fraction,
        "shortcut_count": float(shortcut_count),
    }


def summarize(
    d: int,
    scenario: str,
    seeds: int,
    n: int,
    time_extent: float,
    space_extent: float,
    max_pairs: int,
) -> Summary:
    rows = [
        run_seed(
            d=d,
            n=n,
            time_extent=time_extent,
            space_extent=space_extent,
            seed=seed,
            scenario=scenario,
            max_pairs=max_pairs,
        )
        for seed in range(seeds)
    ]

    def mean(key: str) -> float:
        return float(np.mean([row[key] for row in rows]))

    def std(key: str) -> float:
        return float(np.std([row[key] for row in rows]))

    return Summary(
        spacetime_dimension=d,
        scenario=scenario,
        seeds=seeds,
        observed_events_mean=mean("observed_events"),
        evaluated_pairs_mean=mean("evaluated_pairs"),
        proper_time_count_rho_mean=mean("proper_time_count_rho"),
        proper_time_count_rho_std=std("proper_time_count_rho"),
        proper_time_delay_rho_mean=mean("proper_time_delay_rho"),
        proper_time_delay_rho_std=std("proper_time_delay_rho"),
        proper_time_count_rmse_mean=mean("proper_time_count_rmse"),
        spatial_rho_raw_delay_mean=mean("spatial_rho_raw_delay"),
        spatial_rho_raw_delay_std=std("spatial_rho_raw_delay"),
        spatial_rho_calibrated_delay_mean=mean(
            "spatial_rho_calibrated_delay"
        ),
        spatial_rho_calibrated_delay_std=std(
            "spatial_rho_calibrated_delay"
        ),
        false_causal_fraction_mean=mean("false_causal_fraction"),
        false_causal_fraction_std=std("false_causal_fraction"),
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seeds", type=int, default=25)
    parser.add_argument("--max-pairs", type=int, default=8_000)
    parser.add_argument("--time-extent", type=float, default=12.0)
    parser.add_argument("--space-extent", type=float, default=12.0)
    parser.add_argument("--events-1p1", type=int, default=360)
    parser.add_argument("--events-2p1", type=int, default=500)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    summaries = []
    for d, n in ((2, args.events_1p1), (3, args.events_2p1)):
        for scenario in SCENARIOS:
            summaries.append(
                summarize(
                    d=d,
                    scenario=scenario,
                    seeds=args.seeds,
                    n=n,
                    time_extent=args.time_extent,
                    space_extent=args.space_extent,
                    max_pairs=args.max_pairs,
                )
            )

    if args.json:
        print(json.dumps([asdict(s) for s in summaries], indent=2))
        return

    print("SIM-04B: causal order + count + delay geometry benchmark")
    print("rho columns are Spearman rank correlations against hidden geometry")
    print()
    for s in summaries:
        label = "1+1" if s.spacetime_dimension == 2 else "2+1"
        print(
            f"{label:4s} {s.scenario:18s} "
            f"tau(count)={s.proper_time_count_rho_mean:.3f}  "
            f"tau(delay)={s.proper_time_delay_rho_mean:.3f}  "
            f"r(raw)={s.spatial_rho_raw_delay_mean:.3f}  "
            f"r(cal)={s.spatial_rho_calibrated_delay_mean:.3f}  "
            f"false-causal={s.false_causal_fraction_mean:.3f}"
        )


if __name__ == "__main__":
    main()
