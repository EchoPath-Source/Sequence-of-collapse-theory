#!/usr/bin/env python3
"""O-1D3j: ordered history versus compressed self-state summaries under an observation gap.

Frozen design contract for the paired benchmark that generated results.csv.
Synthetic ordinary control theory only; no consciousness or novel-physics claim.
"""
# Constants: FAIL=.22, REPAIR=.32, HORIZON=10, GAMMA=.98,
# intervention=200, gap=40, ledger length=20, estimator alpha=.20.
# Representations: ordered exponential filter, matched external ordered filter,
# arithmetic mean, last sample, median, shuffled exponential filter, zero memory,
# and oracle current state.
# Regimes: degradation .05/.08/.12; diagnostic noise .08/.12/.16;
# repair .90/.80/.70. 500 paired episodes per arm, cap=500, seed=4100.
# During the gap, expected action-conditioned transitions propagate the estimate.
# Policy decisions use the same continuation-value controller as O-1D3i.
# See results.csv for the frozen output and README.md for interpretation.
