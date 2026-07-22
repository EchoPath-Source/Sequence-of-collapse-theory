# SOC-HYS-01 Protocol v0.1

**Title:** Collapse-Memory Hysteresis in Repeated Physical Measurement Systems  
**Status:** DRAFT PROTOCOL / PREREGISTRATION CANDIDATE  
**Primary claim boundary:** This protocol tests for an order-dependent residual. It does not claim that any residual, if observed, proves SoCT without independent replication and conventional-effect exclusion.

## 1. Research question

Does the order of prior physical measurement conditions leave a measurable post-switch residual in a later measurement stream?

## 2. Hypothesis

If collapse-memory hysteresis exists, then early post-switch measurements should differ depending on whether the system was previously exposed to a high-coherence condition or a low-coherence condition.

Primary directional hypothesis:

```text
R_post(H -> L) differs from R_post(L -> H)
```

The sign should be locked before a real preregistered run once the exact sensor and H/L definitions are chosen.

## 3. Conditions

### H condition

High-coherence or high-structure measurement condition.

Candidate optical implementation:

```text
stable laser or narrow-path illumination onto sensor
```

### L condition

Low-coherence, diffuse, or matched-control measurement condition.

Candidate optical implementation:

```text
same average power through diffuser or scattered illumination
```

## 4. Trial structure

A trial is a fixed-duration sensor-sampling window.

Candidate default:

```text
trial_duration_seconds = 1
samples_per_trial = hardware-dependent
```

Block A:

```text
1000 H trials followed by 1000 L trials
```

Block B:

```text
1000 L trials followed by 1000 H trials
```

The order of blocks should be randomized and blinded in the stored data labels where possible.

## 5. Primary endpoint

Primary endpoint:

```text
mean residual shift in the first N post-switch trials
```

Candidate N:

```text
N = 100
```

The endpoint must be finalized before the preregistered physical run.

## 6. Residual model

The measured signal should be converted into a residual after accounting for conventional covariates:

```text
residual = measured_signal - model(temperature, power, time, block_index, baseline, environmental_flags)
```

Suggested covariates:

- sensor temperature;
- source temperature;
- input optical/electrical power;
- time since start;
- block number;
- electronics baseline;
- dark-run baseline;
- vibration or environmental flags, if available.

## 7. Statistical test

Minimum recommended tests:

1. Difference in post-switch mean residual between H->L and L->H.
2. Bootstrap confidence interval for the difference.
3. Permutation test that shuffles block labels under the null.
4. Sensitivity check for multiple N values, reported as exploratory unless preregistered.

Primary statistic:

```text
Delta_HYS = mean(R_post(H -> L)) - mean(R_post(L -> H))
```

## 8. Controls

Minimum controls:

1. Dark/sham runs.
2. Same power or measured-power correction.
3. Temperature logging.
4. Randomized block order.
5. Blinded labels for analysis.
6. Dummy thermal load where feasible.
7. Same sensor/readout chain for H and L.
8. Repeat runs across multiple days.
9. Predefined exclusion criteria.
10. Full reporting of null results.

## 9. Exclusion criteria

Candidate exclusions, to be finalized before preregistration:

- sensor saturation;
- missing temperature or power logs;
- known equipment disturbance;
- large vibration event;
- source dropout;
- DAQ error;
- environmental condition outside preregistered bounds.

## 10. Interpretation ladder

Level 0: Simulation-only validation.

```text
No physical claim.
```

Level 1: Physical residual detected in one setup.

```text
Anomaly candidate only.
```

Level 2: Residual survives controls and repeat days.

```text
Strong anomaly candidate.
```

Level 3: Independent replication with blinded analysis.

```text
Credible empirical anomaly.
```

Level 4: Scaling law tied to a SoCT variable.

```text
Theory-relevant support.
```

## 11. Falsification / weakening condition

SOC-HYS-01 is weakened for a given setup if:

```text
Delta_HYS is statistically consistent with zero after controls
```

or if the effect is fully explained by temperature, power drift, sensor memory, electronics settling, vibration, or other conventional confounds.

## 12. Do-not-say list

Do not claim:

- proof of SoCT;
- proof that collapse leaves memory;
- proof of consciousness-driven collapse;
- proof of new physics;
- vacuum engineering;
- propulsion or gravity control;
- product readiness.

Acceptable wording:

```text
SOC-HYS-01 tests for order-dependent residuals in repeated physical measurement streams.
```
