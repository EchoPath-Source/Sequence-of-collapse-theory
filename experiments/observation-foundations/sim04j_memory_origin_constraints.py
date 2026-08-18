#!/usr/bin/env python3
"""SIM-04J: memory-origin constraint / causal-completion benchmark.

Toy-model methodology test only. Not empirical evidence for SoCT.

The current reaction-diffusion law is treated as the overdamped limit of

    M_ddot + gamma M_dot - c_M^2 Laplacian M + omega_M^2 M = g C.

with
    beta = omega_M^2/gamma
    D_M  = c_M^2/gamma.

The benchmark fits only late-time, low-k data and then predicts early-time,
high-k behavior without adding high-k parameters. A pure diffusion null is
fit on exactly the same training data.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass

import numpy as np

TRUE_GAMMA = 5.0
TRUE_BETA = 0.08
TRUE_D = 0.18
NOISE_SIGMA = 0.006
LOW_K = np.asarray([0.0, 0.4, 0.8, 1.2])
HIGH_K = np.asarray([3.0, 4.0, 5.0])
TIMES = np.arange(0.0, 12.0001, 0.02)
TRAIN_MASK = (TIMES >= 4.0) & (TIMES <= 12.0)
TEST_MASK = (TIMES >= 0.0) & (TIMES <= 3.0)
BETA_GRID = np.arange(0.05, 0.111, 0.005)
D_GRID = np.arange(0.12, 0.241, 0.005)


@dataclass
class Summary:
    generator: str
    seeds: int
    causal_beta_mean: float
    causal_D_mean: float
    causal_train_rmse: float
    causal_test_rmse: float
    diffusion_beta_mean: float
    diffusion_D_mean: float
    diffusion_train_rmse: float
    diffusion_test_rmse: float


def causal_response(k: float, times: np.ndarray, beta: float, diffusion: float) -> np.ndarray:
    q = beta + diffusion * k * k
    disc = TRUE_GAMMA**2 - 4.0 * TRUE_GAMMA * q
    t = np.asarray(times)
    if disc > 1e-12:
        root = np.sqrt(disc)
        r_slow = (TRUE_GAMMA - root) / 2.0
        r_fast = (TRUE_GAMMA + root) / 2.0
        a = r_fast / (r_fast - r_slow)
        b = -r_slow / (r_fast - r_slow)
        return a * np.exp(-r_slow * t) + b * np.exp(-r_fast * t)
    if disc < -1e-12:
        omega = np.sqrt(TRUE_GAMMA * q - TRUE_GAMMA**2 / 4.0)
        return np.exp(-TRUE_GAMMA * t / 2.0) * (
            np.cos(omega * t) + TRUE_GAMMA * np.sin(omega * t) / (2.0 * omega)
        )
    r = TRUE_GAMMA / 2.0
    return np.exp(-r * t) * (1.0 + r * t)


def diffusion_response(k: float, times: np.ndarray, beta: float, diffusion: float) -> np.ndarray:
    return np.exp(-(beta + diffusion * k * k) * np.asarray(times))


def vector(ks, mask, model, beta, diffusion):
    return np.concatenate([model(float(k), TIMES[mask], beta, diffusion) for k in ks])


PARAMS = [(float(b), float(d)) for b in BETA_GRID for d in D_GRID]
TRAIN_CAUSAL = np.asarray([vector(LOW_K, TRAIN_MASK, causal_response, b, d) for b, d in PARAMS])
TEST_CAUSAL = np.asarray([vector(HIGH_K, TEST_MASK, causal_response, b, d) for b, d in PARAMS])
TRAIN_DIFF = np.asarray([vector(LOW_K, TRAIN_MASK, diffusion_response, b, d) for b, d in PARAMS])
TEST_DIFF = np.asarray([vector(HIGH_K, TEST_MASK, diffusion_response, b, d) for b, d in PARAMS])

TRUE = {
    "causal": (
        vector(LOW_K, TRAIN_MASK, causal_response, TRUE_BETA, TRUE_D),
        vector(HIGH_K, TEST_MASK, causal_response, TRUE_BETA, TRUE_D),
    ),
    "diffusion": (
        vector(LOW_K, TRAIN_MASK, diffusion_response, TRUE_BETA, TRUE_D),
        vector(HIGH_K, TEST_MASK, diffusion_response, TRUE_BETA, TRUE_D),
    ),
}


def fit_one(observed_train, observed_test, train_library, test_library):
    error = np.sqrt(np.mean((train_library - observed_train[None, :]) ** 2, axis=1))
    idx = int(np.argmin(error))
    return PARAMS[idx], float(error[idx]), float(
        np.sqrt(np.mean((test_library[idx] - observed_test) ** 2))
    )


def run(generator: str, seeds: int) -> Summary:
    train_true, test_true = TRUE[generator]
    rows = []
    for seed in range(seeds):
        rng = np.random.default_rng(5000 + seed)
        train = train_true + rng.normal(0.0, NOISE_SIGMA, train_true.shape)
        test = test_true + rng.normal(0.0, NOISE_SIGMA, test_true.shape)
        cp, ctr, cte = fit_one(train, test, TRAIN_CAUSAL, TEST_CAUSAL)
        dp, dtr, dte = fit_one(train, test, TRAIN_DIFF, TEST_DIFF)
        rows.append((cp[0], cp[1], ctr, cte, dp[0], dp[1], dtr, dte))
    arr = np.asarray(rows)
    means = arr.mean(axis=0)
    return Summary(generator, seeds, *map(float, means))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seeds", type=int, default=50)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    summaries = [run("causal", args.seeds), run("diffusion", args.seeds)]
    payload = {
        "gamma": TRUE_GAMMA,
        "beta_true": TRUE_BETA,
        "D_true": TRUE_D,
        "c_M_predicted": float(np.sqrt(TRUE_GAMMA * TRUE_D)),
        "k_c_predicted": float(np.sqrt((TRUE_GAMMA / 4.0 - TRUE_BETA) / TRUE_D)),
        "summaries": [asdict(s) for s in summaries],
    }
    if args.json:
        print(json.dumps(payload, indent=2))
        return
    print("SIM-04J memory-origin constraint benchmark")
    print(f"predicted c_M={payload['c_M_predicted']:.6f}  k_c={payload['k_c_predicted']:.6f}")
    for s in summaries:
        print(
            f"{s.generator:10s} causal test={s.causal_test_rmse:.6f} "
            f"diffusion test={s.diffusion_test_rmse:.6f}"
        )


if __name__ == "__main__":
    main()
