#!/usr/bin/env python3
"""O-1D3b: adaptive self-model calibration under distribution shift.

The system experiences a mid-run increase in its own degradation probability.
Adaptive controllers estimate that degradation rate online from observed
state-transition shocks and use the estimate inside the same short-horizon
planner used in O-1D3. Internal and zero-latency external adaptive controllers
are deliberately matched.

Synthetic ordinary control/information theory only. No consciousness or novel
physics claim.
"""
import csv, random
from pathlib import Path

HORIZON = 6
GAMMA = 0.97
MAINT_COST = 0.12
PRE_DEGRADATION = 0.02
REPAIR_SUCCESS = 0.90
DIAGNOSTIC_NOISE = 0.05
WINDOW = 200
N_STEPS = 100000


def clamp(x):
    return max(0.05, min(1.0, x))


def expected_next(h, action, degradation, repair_success):
    if action == "maintain":
        return clamp(h + repair_success * 0.30 - 0.006)
    return clamp(h - (0.010 + 0.30 * degradation))


def immediate_value(h, action):
    return -MAINT_COST if action == "maintain" else 0.50 + 0.45 * h


def plan(h, degradation, repair_success):
    values = {}
    for first in ("work", "maintain"):
        hh = h
        total = 0.0
        for k in range(HORIZON):
            action = first if k == 0 else ("maintain" if hh < 0.68 else "work")
            total += (GAMMA ** k) * immediate_value(hh, action)
            hh = expected_next(hh, action, degradation, repair_success)
        values[first] = total
    return max(values, key=values.get)


def run(condition, post_degradation, seed):
    rng = random.Random(seed)
    health = 0.95
    reward = 0.0
    post_reward = 0.0
    maintenance = 0
    low_health = 0
    shock_events = []
    estimated_degradation = PRE_DEGRADATION

    for t in range(N_STEPS):
        true_degradation = PRE_DEGRADATION if t < N_STEPS // 2 else post_degradation
        pre_diag = clamp(health + (rng.random() - 0.5) * 2 * DIAGNOSTIC_NOISE)

        if condition == "reactive":
            action = "maintain" if pre_diag < 0.68 else "work"
        elif condition == "frozen_predictive":
            action = plan(pre_diag, PRE_DEGRADATION, REPAIR_SUCCESS)
        elif condition.startswith("adaptive"):
            action = plan(pre_diag, estimated_degradation, REPAIR_SUCCESS)
        else:
            raise ValueError(condition)

        step_reward = 0.0
        if action == "maintain":
            maintenance += 1
            step_reward -= MAINT_COST
            if rng.random() < REPAIR_SUCCESS:
                health = clamp(health + 0.30)
            health = clamp(health - 0.006)
        else:
            shock = rng.random() < true_degradation
            health = clamp(health - (0.31 if shock else 0.010))
            if rng.random() < 0.50 + 0.45 * health:
                step_reward += 1.0

        post_diag = clamp(health + (rng.random() - 0.5) * 2 * DIAGNOSTIC_NOISE)

        if condition.startswith("adaptive") and action == "work":
            shock_events.append(1 if (post_diag - pre_diag) < -0.15 else 0)
            shock_events = shock_events[-WINDOW:]
            estimated_degradation = (1 + sum(shock_events)) / (2 + len(shock_events))

        reward += step_reward
        if t >= N_STEPS // 2:
            post_reward += step_reward
        low_health += int(health < 0.55)

    return {
        "condition": condition,
        "pre_degradation": PRE_DEGRADATION,
        "post_degradation": post_degradation,
        "repair_success": REPAIR_SUCCESS,
        "diagnostic_noise": DIAGNOSTIC_NOISE,
        "window": WINDOW,
        "reward_per_step": reward / N_STEPS,
        "post_shift_reward": post_reward / (N_STEPS // 2),
        "maintenance_rate": maintenance / N_STEPS,
        "low_health_fraction": low_health / N_STEPS,
        "final_estimated_degradation": estimated_degradation,
        "n_steps": N_STEPS,
        "seed": seed,
    }


def main():
    rows = []
    for j, post in enumerate((0.04, 0.06, 0.08, 0.10, 0.15)):
        seed = 1200 + 37 * j
        for label in (
            "reactive",
            "frozen_predictive",
            "adaptive_internal",
            "adaptive_external_zero_latency",
        ):
            model_label = "adaptive_internal" if label == "adaptive_external_zero_latency" else label
            row = run(model_label, post, seed)
            row["condition"] = label
            rows.append(row)

    out = Path(__file__).with_name("results.csv")
    with out.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
