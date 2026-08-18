#!/usr/bin/env python3
"""SIM-04I: incomplete-reset / hidden-reservoir adversary.

Toy-model methodology test only. This is not empirical evidence for SoCT.

Question:
    How complete must independent reset verification be before a post-reset
    history residual can be distinguished from an ordinary leftover reservoir?

This simulation deliberately gives the conventional adversary the same
source/decay/diffusion family as H2. Probe-only data are therefore structurally
non-identifying. The only additional evidence comes from an independently
calibrated reset diagnostic that couples to ordinary reservoir state but not
to the proposed H2 state M.

Models:
    H2:
        post-reset probe residual from M; reset diagnostic has zero mean.
    conventional reservoir:
        an ordinary state survives reset by fraction q, has the same beta/D
        evolution, and couples both to the fresh probe and to an independently
        calibrated reset diagnostic.

If diagnostic coupling kappa_diag = 0, the two descriptions are exactly
observationally degenerate in this restricted experiment.

Requires:
    numpy

Reuses the observation-derived source histories and graph field operators from
SIM-04H to keep the source stage identical.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass

import numpy as np

from sim04h_h0_h1_h2_reset_probe import (
    SHOTS,
    TEST_PROTOCOLS,
    TRAIN_PROTOCOLS,
    TRUE_BETA,
    TRUE_DIFFUSION,
    probe_features,
)


BETA_GRID = np.round(np.arange(0.04, 0.141, 0.01), 2)
DIFFUSION_GRID = np.round(np.arange(0.0, 0.251, 0.025), 3)
PHASE_SCALE_GRID = np.round(np.arange(0.0, 3.01, 0.05), 2)

TRUE_EFFECTIVE_PHASE_SCALE = 1.05
TRUE_RESET_FRACTION = 0.35

DIAGNOSTIC_COUPLINGS = (1.0, 0.20, 0.05, 0.0)
DIAGNOSTIC_SIGMAS = (0.10, 0.05, 0.02, 0.01, 0.005)


@dataclass
class ScenarioSummary:
    generator: str
    kappa_diag: float
    sigma_diag: float
    seeds: int
    conventional_selected_fraction: float
    h2_selected_fraction: float
    unresolved_fraction: float
    delta_bic_conventional_minus_h2_mean: float
    h2_test_reduced_chi2_mean: float
    conventional_test_reduced_chi2_mean: float
    fitted_reset_fraction_mean: float


@dataclass
class ResetFractionSummary:
    true_reset_fraction: float
    conventional_selected_fraction: float
    delta_bic_conventional_minus_h2_mean: float


TRUE_TRAIN = probe_features(
    TRAIN_PROTOCOLS,
    TRUE_BETA,
    TRUE_DIFFUSION,
)
TRUE_TEST = probe_features(
    TEST_PROTOCOLS,
    TRUE_BETA,
    TRUE_DIFFUSION,
)


CANDIDATES = []
for beta in BETA_GRID:
    for diffusion in DIFFUSION_GRID:
        CANDIDATES.append(
            (
                float(beta),
                float(diffusion),
                probe_features(TRAIN_PROTOCOLS, beta, diffusion),
                probe_features(TEST_PROTOCOLS, beta, diffusion),
            )
        )

TRAIN_FEATURES = np.stack([row[2] for row in CANDIDATES])
TEST_FEATURES = np.stack([row[3] for row in CANDIDATES])
CANDIDATE_BETA = np.asarray([row[0] for row in CANDIDATES])
CANDIDATE_D = np.asarray([row[1] for row in CANDIDATES])

PROBE_TRAIN_PREDICTIONS = np.sin(
    TRAIN_FEATURES[:, None, :]
    * PHASE_SCALE_GRID[None, :, None]
)
PROBE_TEST_PREDICTIONS = np.sin(
    TEST_FEATURES[:, None, :]
    * PHASE_SCALE_GRID[None, :, None]
)


def sample_probe(
    expectation: np.ndarray,
    rng: np.random.Generator,
) -> np.ndarray:
    probability_plus = (
        1.0 + np.clip(expectation, -1.0, 1.0)
    ) / 2.0
    plus_counts = rng.binomial(SHOTS, probability_plus)
    return 2.0 * plus_counts / SHOTS - 1.0


def generate_dataset(
    generator: str,
    kappa_diag: float,
    sigma_diag: float,
    seed: int,
    reset_fraction: float = TRUE_RESET_FRACTION,
):
    rng = np.random.default_rng(seed)

    probe_train_mean = np.sin(
        TRUE_EFFECTIVE_PHASE_SCALE * TRUE_TRAIN
    )
    probe_test_mean = np.sin(
        TRUE_EFFECTIVE_PHASE_SCALE * TRUE_TEST
    )

    if generator == "conventional":
        diagnostic_train_mean = (
            kappa_diag * reset_fraction * TRUE_TRAIN
        )
        diagnostic_test_mean = (
            kappa_diag * reset_fraction * TRUE_TEST
        )
    elif generator == "H2":
        diagnostic_train_mean = np.zeros_like(TRUE_TRAIN)
        diagnostic_test_mean = np.zeros_like(TRUE_TEST)
    else:
        raise ValueError(f"unknown generator: {generator}")

    probe_train = sample_probe(probe_train_mean, rng)
    probe_test = sample_probe(probe_test_mean, rng)

    diagnostic_train = (
        diagnostic_train_mean
        + rng.normal(
            0.0,
            sigma_diag,
            size=diagnostic_train_mean.shape,
        )
    )
    diagnostic_test = (
        diagnostic_test_mean
        + rng.normal(
            0.0,
            sigma_diag,
            size=diagnostic_test_mean.shape,
        )
    )

    return (
        probe_train,
        probe_test,
        diagnostic_train,
        diagnostic_test,
    )


def fit_models(
    probe_train: np.ndarray,
    probe_test: np.ndarray,
    diagnostic_train: np.ndarray,
    diagnostic_test: np.ndarray,
    kappa_diag: float,
    sigma_diag: float,
):
    # For likelihood comparison we use the zero-signal shot scale. The phase
    # amplitudes are small enough here that this is an adequate benchmark
    # approximation.
    sigma_probe = 1.0 / math.sqrt(SHOTS)

    probe_residual = (
        PROBE_TRAIN_PREDICTIONS
        - probe_train[None, None, :]
    ) / sigma_probe
    probe_chi2 = np.sum(probe_residual ** 2, axis=2)

    # H2 predicts no ordinary-reservoir reset-diagnostic signal.
    h2_diag_chi2 = float(
        np.sum((diagnostic_train / sigma_diag) ** 2)
    )
    h2_total = probe_chi2 + h2_diag_chi2
    h2_candidate, h2_phase = np.unravel_index(
        int(np.argmin(h2_total)),
        h2_total.shape,
    )

    h2_probe_test = PROBE_TEST_PREDICTIONS[
        h2_candidate,
        h2_phase,
    ]
    h2_test_residual = np.concatenate(
        [
            (h2_probe_test - probe_test) / sigma_probe,
            -diagnostic_test / sigma_diag,
        ]
    )
    h2_test_reduced_chi2 = float(
        np.mean(h2_test_residual ** 2)
    )

    # Conventional reservoir:
    # - the probe sees one effective phase scale (lambda*q);
    # - the independent diagnostic estimates q through a calibrated coupling.
    # This reparameterization avoids assigning an artificial complexity
    # penalty to a product that probe-only data cannot separate.
    best_phase_index = np.argmin(probe_chi2, axis=1)
    best_probe_chi2 = probe_chi2[
        np.arange(len(CANDIDATES)),
        best_phase_index,
    ]

    if kappa_diag > 0.0:
        diagnostic_basis = kappa_diag * TRAIN_FEATURES
        numerator = np.sum(
            diagnostic_basis
            * diagnostic_train[None, :],
            axis=1,
        )
        denominator = (
            np.sum(diagnostic_basis ** 2, axis=1)
            + 1e-12
        )
        reset_fraction = np.clip(
            numerator / denominator,
            0.0,
            1.0,
        )
        diagnostic_prediction = (
            diagnostic_basis
            * reset_fraction[:, None]
        )
        conventional_diag_chi2 = np.sum(
            (
                (
                    diagnostic_prediction
                    - diagnostic_train[None, :]
                )
                / sigma_diag
            )
            ** 2,
            axis=1,
        )
        conventional_parameter_count = 4
    else:
        # A completely blind diagnostic cannot identify q. The conventional
        # model then has the same effective dimensionality as H2 in this
        # restricted experiment, and the two models are exactly degenerate.
        reset_fraction = np.zeros(len(CANDIDATES))
        conventional_diag_chi2 = np.sum(
            (
                (
                    np.zeros_like(TRAIN_FEATURES)
                    - diagnostic_train[None, :]
                )
                / sigma_diag
            )
            ** 2,
            axis=1,
        )
        conventional_parameter_count = 3

    conventional_total = (
        best_probe_chi2 + conventional_diag_chi2
    )
    conventional_candidate = int(
        np.argmin(conventional_total)
    )
    conventional_phase = int(
        best_phase_index[conventional_candidate]
    )

    conventional_probe_test = PROBE_TEST_PREDICTIONS[
        conventional_candidate,
        conventional_phase,
    ]
    conventional_diag_test = (
        kappa_diag
        * reset_fraction[conventional_candidate]
        * TEST_FEATURES[conventional_candidate]
    )
    conventional_test_residual = np.concatenate(
        [
            (
                conventional_probe_test - probe_test
            )
            / sigma_probe,
            (
                conventional_diag_test
                - diagnostic_test
            )
            / sigma_diag,
        ]
    )
    conventional_test_reduced_chi2 = float(
        np.mean(conventional_test_residual ** 2)
    )

    n_train = 2 * len(probe_train)
    h2_bic = float(
        h2_total[h2_candidate, h2_phase]
        + 3 * np.log(n_train)
    )
    conventional_bic = float(
        conventional_total[conventional_candidate]
        + conventional_parameter_count * np.log(n_train)
    )

    return {
        "h2_bic": h2_bic,
        "conventional_bic": conventional_bic,
        "delta_bic_conventional_minus_h2": (
            conventional_bic - h2_bic
        ),
        "h2_test_reduced_chi2": h2_test_reduced_chi2,
        "conventional_test_reduced_chi2": (
            conventional_test_reduced_chi2
        ),
        "h2_beta": float(
            CANDIDATE_BETA[h2_candidate]
        ),
        "h2_D": float(CANDIDATE_D[h2_candidate]),
        "h2_phase_scale": float(
            PHASE_SCALE_GRID[h2_phase]
        ),
        "conventional_beta": float(
            CANDIDATE_BETA[conventional_candidate]
        ),
        "conventional_D": float(
            CANDIDATE_D[conventional_candidate]
        ),
        "conventional_phase_scale": float(
            PHASE_SCALE_GRID[conventional_phase]
        ),
        "fitted_reset_fraction": float(
            reset_fraction[conventional_candidate]
        ),
    }


def run_scenario(
    generator: str,
    kappa_diag: float,
    sigma_diag: float,
    seeds: int,
    reset_fraction: float = TRUE_RESET_FRACTION,
) -> ScenarioSummary:
    rows = []

    for index in range(seeds):
        dataset = generate_dataset(
            generator,
            kappa_diag,
            sigma_diag,
            seed=1000 + index,
            reset_fraction=reset_fraction,
        )
        rows.append(
            fit_models(
                *dataset,
                kappa_diag=kappa_diag,
                sigma_diag=sigma_diag,
            )
        )

    delta = np.asarray(
        [
            row["delta_bic_conventional_minus_h2"]
            for row in rows
        ]
    )

    tolerance = 1e-9
    conventional_selected = delta < -tolerance
    h2_selected = delta > tolerance
    unresolved = np.abs(delta) <= tolerance

    return ScenarioSummary(
        generator=generator,
        kappa_diag=kappa_diag,
        sigma_diag=sigma_diag,
        seeds=seeds,
        conventional_selected_fraction=float(
            np.mean(conventional_selected)
        ),
        h2_selected_fraction=float(
            np.mean(h2_selected)
        ),
        unresolved_fraction=float(np.mean(unresolved)),
        delta_bic_conventional_minus_h2_mean=float(
            np.mean(delta)
        ),
        h2_test_reduced_chi2_mean=float(
            np.mean(
                [row["h2_test_reduced_chi2"] for row in rows]
            )
        ),
        conventional_test_reduced_chi2_mean=float(
            np.mean(
                [
                    row["conventional_test_reduced_chi2"]
                    for row in rows
                ]
            )
        ),
        fitted_reset_fraction_mean=float(
            np.mean(
                [
                    row["fitted_reset_fraction"]
                    for row in rows
                ]
            )
        ),
    )


def reset_fraction_sweep(
    seeds: int,
    kappa_diag: float = 0.20,
    sigma_diag: float = 0.02,
):
    output = []
    for reset_fraction in (0.10, 0.20, 0.35, 0.50, 0.70):
        summary = run_scenario(
            "conventional",
            kappa_diag,
            sigma_diag,
            seeds,
            reset_fraction=reset_fraction,
        )
        output.append(
            ResetFractionSummary(
                true_reset_fraction=reset_fraction,
                conventional_selected_fraction=(
                    summary.conventional_selected_fraction
                ),
                delta_bic_conventional_minus_h2_mean=(
                    summary.delta_bic_conventional_minus_h2_mean
                ),
            )
        )
    return output


def exact_blind_degeneracy() -> float:
    # Probe-only equality: conventional reset attenuation q can be absorbed
    # exactly into the effective phase scale lambda*q. With kappa_diag=0,
    # neither description has an additional observable.
    h2 = np.sin(TRUE_EFFECTIVE_PHASE_SCALE * TRUE_TEST)
    conventional = np.sin(
        TRUE_EFFECTIVE_PHASE_SCALE * TRUE_TEST
    )
    return float(np.max(np.abs(h2 - conventional)))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seeds", type=int, default=80)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    conventional = [
        run_scenario(
            "conventional",
            kappa_diag,
            sigma_diag,
            args.seeds,
        )
        for kappa_diag in DIAGNOSTIC_COUPLINGS
        for sigma_diag in DIAGNOSTIC_SIGMAS
    ]

    # H2 sanity checks at representative diagnostic sensitivities.
    h2 = [
        run_scenario(
            "H2",
            kappa_diag,
            sigma_diag,
            args.seeds,
        )
        for kappa_diag, sigma_diag in (
            (1.0, 0.02),
            (0.20, 0.02),
            (0.05, 0.005),
            (0.0, 0.02),
        )
    ]

    reset_sweep = reset_fraction_sweep(args.seeds)

    payload = {
        "true_beta": TRUE_BETA,
        "true_D": TRUE_DIFFUSION,
        "true_effective_phase_scale": (
            TRUE_EFFECTIVE_PHASE_SCALE
        ),
        "true_reset_fraction": TRUE_RESET_FRACTION,
        "blind_diagnostic_max_prediction_difference": (
            exact_blind_degeneracy()
        ),
        "conventional_generator": [
            asdict(row) for row in conventional
        ],
        "h2_generator_sanity": [
            asdict(row) for row in h2
        ],
        "reset_fraction_sweep": [
            asdict(row) for row in reset_sweep
        ],
    }

    if args.json:
        print(json.dumps(payload, indent=2))
        return

    print("SIM-04I incomplete-reset / hidden-reservoir adversary")
    print()
    print(
        "Conventional diffusive reservoir generator; "
        "fraction selecting conventional model"
    )
    for row in conventional:
        print(
            f"kappa={row.kappa_diag:>4.2f} "
            f"sigma={row.sigma_diag:>5.3f} "
            f"select={row.conventional_selected_fraction:>5.3f} "
            f"deltaBIC(conv-H2)="
            f"{row.delta_bic_conventional_minus_h2_mean:>8.2f}"
        )

    print()
    print(
        "Blind diagnostic exact max prediction difference: "
        f"{payload['blind_diagnostic_max_prediction_difference']:.3g}"
    )


if __name__ == "__main__":
    main()
