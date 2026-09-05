# Simulation 4e — Unmeasured Carryover and Covariate Error

**Status:** Adversarial synthetic control model  
**Purpose:** Determine how imperfect characterization of the ordinary present state can generate a false history-associated residual.

## Question

Simulation 4d showed that measured preparation carryover can be adjusted away. That is not enough: real experiments never measure every ordinary state variable perfectly.

Simulation 4e therefore sets the true SoCT coupling to zero and varies two failure modes:

1. measurement error in observed carryover covariates;
2. an omitted history-correlated ordinary variable.

The fitted history coefficient is then tested for a false nonzero residual.

## Main result

The control fails gracefully only when ordinary carryover is characterized sufficiently well. As covariate measurement error increases, the fitted history term can reappear even with `lambda_M = 0`. An omitted history-correlated variable makes the problem worse.

Representative seeded outcomes from the baseline sweep include:

```text
hidden=0.000, measurement_sigma=0.00 -> lambda_fit=-0.00020, z=-0.18
hidden=0.000, measurement_sigma=0.20 -> lambda_fit= 0.00193, z= 2.35
hidden=0.003, measurement_sigma=0.20 -> lambda_fit= 0.00374, z= 4.62
hidden=0.006, measurement_sigma=0.20 -> lambda_fit= 0.00641, z= 7.76
hidden=0.012, measurement_sigma=0.20 -> lambda_fit= 0.00601, z= 7.50
```

Individual seeded cells fluctuate, so these numbers are design diagnostics rather than universal thresholds. The robust lesson is structural: **a residual associated with history is uninterpretable unless ordinary present-state matching and measurement fidelity are independently bounded.**

## Consequence for an experiment

A credible history-memory protocol must not merely regress on a few measured covariates. It should include:

- direct pre-probe equivalence tests on all known state variables;
- sham histories matched for energy, pulse count, timing, and environmental exposure;
- randomized/crossed assignment of history to hardware;
- negative-control observables expected to respond to ordinary carryover but not the proposed memory term;
- calibration of covariate measurement error;
- sensitivity analysis for omitted history-correlated variables;
- a preregistered exclusion rule if state matching fails.

## Stronger falsification criterion

The SoCT interpretation should be rejected or withheld if a candidate history residual:

1. disappears under improved state matching;
2. scales with a known carryover proxy;
3. appears in sham-history controls;
4. changes materially when plausible omitted-variable sensitivity is introduced; or
5. cannot be replicated across crossed physical arms.

Only a residual that follows the randomized record-history dose while surviving these ordinary-state controls should advance to a SoCT-specific interpretation.

## Next gate — Simulation 4f

Build a **sham-matched, negative-control, sensitivity-analysis design**. The target is no longer simply recovering an injected `lambda_M`; it is establishing an analysis protocol with explicit rejection regions for ordinary carryover explanations.

After 4f, the observation program should be mature enough to draft a laboratory-facing history-dependent memory protocol while keeping the SoCT term blinded and optional.
