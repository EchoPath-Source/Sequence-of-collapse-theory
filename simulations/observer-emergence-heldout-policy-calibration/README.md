# O-1D3l — Held-Out Policy Calibration from Autobiographical Self-Dynamics

## Question
O-1D3k showed that own action–outcome history estimates hidden self-degradation substantially better than shuffled, donor, or zero-memory controls, but better self-knowledge did not reliably improve behavior because the policy mapping was miscalibrated.

O-1D3l therefore asks a stricter question: **if the mapping from estimated self-dynamics to maintenance policy is calibrated on separate training episodes and then frozen, does autobiographical self-knowledge improve held-out continuation and task reward?**

## Design
The benchmark preserves the O-1D3k hidden degradation regimes (`d = .04/.08/.12`) and action–outcome estimator, but separates training from evaluation.

Training phase:
1. generate independent autobiographical histories;
2. estimate `d_hat` from each history;
3. evaluate a preregistered threshold grid for the continuation policy;
4. choose the threshold maximizing mean training reward within each `d_hat` bin;
5. freeze the mapping before held-out evaluation.

Held-out paired phase compares:
- `own_calibrated` — own paired action–outcome estimate + frozen calibrated policy;
- `external_own_calibrated` — exact zero-latency external replica;
- `shuffled_calibrated` — shuffled action–outcome pairing through the same frozen mapping;
- `compressed_calibrated` — compressed state/no self-dynamics estimate;
- `donor_calibrated` — mismatched donor dynamics estimate;
- `oracle_calibrated` — true degradation through the same frozen policy family;
- `own_uncalibrated` — O-1D3k-style self estimate with the old fixed mapping.

All evaluation arms use paired potential-outcome streams.

## Claim boundary
A positive result requires improvement on held-out episodes, not merely lower model error. The internal arm must also beat appropriate memory controls; equality with the matched external replica remains evidence against internal-location privilege.

This is ordinary adaptive control/system identification. It is not a consciousness or novel-physics test.
