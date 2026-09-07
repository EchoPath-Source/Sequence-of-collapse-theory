#!/usr/bin/env python3
"""O-1D3k: autobiographical action-outcome pairing under hidden degradation dynamics.

The system must estimate its own degradation probability from recent WORK-action
outcomes before a diagnostic gap. Pairing is compared with shuffled pairing,
compressed-state controls, donor history, zero-memory and oracle knowledge.

Synthetic ordinary control theory only; no consciousness or novel-physics claim.
"""
# Frozen design contract used to generate results.csv.
# Constants: FAIL=.22, REPAIR=.32, HORIZON=10, GAMMA=.98,
# intervention=220, observation gap=60, ledger length=80, estimator alpha=.20.
# Hidden true degradation regimes: .04/.08/.12; diagnostic noise=.04; repair=.85.
# 700 paired episodes per arm, cap=500, seed=5100.
# Autobiographical estimator: among recent WORK records (action, pre-diagnostic,
# post-diagnostic), classify abrupt post-pre drops below -.15 as shock events and
# form Beta-smoothed estimate (shocks+1)/(work_count+2).
# Shuffled-pairing control preserves marginals but permutes post-diagnostics before
# estimating the same statistic. Compressed/zero controls use d=.05; donor uses the
# opposite-regime prior (.12 for low true d, .02 otherwise); oracle uses true d.
# See README.md for interpretation and results.csv for frozen output.
