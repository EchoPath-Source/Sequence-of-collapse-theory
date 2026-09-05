# Simulation 4f — Sham Histories and Sensitivity Analysis

**Status:** Adversarial synthetic control model  
**Purpose:** Define when a history-associated residual must be withheld from SoCT interpretation.

## Design

The model includes three crossed channels:

- a randomized target history dose `h`;
- a randomized **sham history** that reproduces preparation burden without carrying the target record history;
- an unrelated negative-control label.

Measured carryover covariates are included, but both measurement error and an omitted ordinary history-correlated variable are allowed.

The true SoCT coupling is fixed to

```math
lambda_M = 0
```

throughout the baseline study.

## Why sham histories matter

A residual that follows the target history label can still be caused by ordinary preparation effects. A sham history asks whether a similarly burdensome but theoretically inactive protocol produces comparable residual structure.

If the sham channel lights up, the experiment has evidence for preparation sensitivity rather than uniquely for history-dependent memory.

The unrelated negative-control channel checks whether the analysis itself is generating generic significance unrelated to either history procedure.

## Representative Monte Carlo behavior

Using 200 synthetic experiments per condition and a nominal flag threshold `|z| >= 3`:

```text
hidden ordinary strength = 0.000
history false-positive rate ~ 0.00
sham flag rate            ~ 0.00
negative-control rate     ~ 0.01

hidden ordinary strength = 0.003
history false-positive rate ~ 0.02
sham flag rate              ~ 0.02
negative-control rate       ~ 0.01

hidden ordinary strength = 0.006
history false-positive rate ~ 0.09
sham flag rate              ~ 0.10
negative-control rate       ~ 0.01

hidden ordinary strength = 0.012
history false-positive rate ~ 0.35
sham flag rate              ~ 0.40
negative-control rate       ~ 0.01
```

The central lesson is not that the sham perfectly diagnoses every hidden variable. It is that a theoretically inactive but preparation-matched channel becomes increasingly informative as ordinary hidden carryover grows.

## Preregistration-style interpretation gate

A target history residual is **not eligible for SoCT interpretation** if any of the following holds:

1. the sham-history coefficient is significant or comparable in magnitude to the target-history coefficient;
2. negative controls show systematic excess significance;
3. the target result is unstable to plausible covariate-measurement error;
4. sensitivity analysis shows that a modest omitted ordinary variable could account for the observed effect;
5. present-state diagnostics differ materially between history conditions;
6. the effect fails to scale reproducibly with preregistered history dose;
7. the effect depends on a particular physical arm rather than following randomized history assignment.

The correct conclusion in those cases is:

> **ordinary explanation not sufficiently excluded.**

That is a valid scientific outcome and must not be relabeled as support for SoCT.

## Interpretation

Simulation 4f does not validate a memory field. It establishes a stronger falsification standard for a future laboratory study.

The observation branch has now progressed from defining records to asking what evidence would be required before a history-dependent residual could be scientifically interesting.

## Next gate

The next step should be a **preregisterable laboratory protocol scaffold**, not another unconstrained toy signal demonstration. It should specify:

- target platform and observable;
- state-matching diagnostics;
- target and sham history-preparation procedures;
- randomized/crossed assignment;
- negative controls;
- history-dose levels;
- carryover covariates and their calibration error;
- primary statistical model;
- sensitivity analysis;
- explicit rejection/withholding criteria;
- power and detectable-coupling analysis.

Conscious-access experiments remain downstream and separate.
