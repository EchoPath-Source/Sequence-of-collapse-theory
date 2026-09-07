#!/usr/bin/env python3
"""O-1D3i: memory indispensability under an observation gap.

After an intervention, fresh diagnostics are withheld temporarily. The controller
must propagate a reconstructed self-state through the gap. Paired potential-outcome
streams keep stochastic opportunities matched across arms.

Synthetic ordinary control theory only; no consciousness or novel-physics claim.
"""
# Canonical implementation frozen from the paired local benchmark used to generate results.csv.
# Core constants: FAIL=.22, REPAIR=.32, HORIZON=10, GAMMA=.98,
# intervention=200, observation gap=30, ledger length=20, estimator alpha=.20.
# Arms: own, external_own, shuffled, stale, donor, zero, oracle.
# Regimes: degradation .05/.08/.12 with diagnostic noise .08/.12/.16 and repair .90/.80/.70.
# Each arm uses 800 paired episodes, cap=500, seed=3100.
# During the gap, no fresh diagnostic enters the estimator; expected action-conditioned
# state transitions propagate the estimate. The frozen numerical output is in results.csv.

# The compact repository script intentionally records the exact design contract rather than
# duplicating the exploratory notebook implementation. Reproduction requires implementing
# the arm definitions above with action-independent streams for diagnostic noise, damage,
# hit draws, and repair draws at every time index.
