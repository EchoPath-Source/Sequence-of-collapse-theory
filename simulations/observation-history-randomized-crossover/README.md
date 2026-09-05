# Simulation 4c — Randomized History-Dose Crossover

**Status:** Exploratory identifiability/design toy model  
**Purpose:** Test whether a candidate history-dependent residual follows randomized prior record history rather than fixed apparatus identity or smooth drift.

## Motivation

Simulation 4b showed that the original single-trajectory phase signature is highly confounded: over a finite window, the candidate memory basis

```math
f_M(t)=[1-exp(-beta t)]/beta
```

can be approximated extremely well by ordinary offset, frequency mismatch, and smooth drift terms.

The remedy is not a more complicated fit to the same trajectory. The experimental design must change.

Simulation 4c randomizes the history assignment itself.

## Trial structure

Each trial contains two physical arms, `A` and `B`, with a measured differential phase.

A prior durable-record history dose is assigned as

```text
dose = 0.0, 0.5, or 1.0
```

and, for nonzero dose, the sign is randomized:

```text
+ dose -> B receives the larger prior-history assignment
- dose -> A receives the larger prior-history assignment
```

Thus the history contrast is

```math
h_i in {0, +/-0.5, +/-1}.
```

The injected SoCT term is

```math
y_M = lambda_M h_i f_M(t_probe).
```

Ordinary nuisance effects remain tied to apparatus/run order:

```text
fixed hardware offset
linear slow drift
periodic drift
Gaussian measurement noise
```

Because the history label is randomized and crossed between physical arms, those fixed nuisance terms should not systematically track `h_i`.

## Analysis model

The synthetic analysis fits

```math
y_i = a_0 + a_1 r_i + lambda_M h_i f_M + epsilon_i,
```

where `r_i` is centered run order.

The target coefficient is `lambda_M`.

## Representative setup

```text
N trials = 600
beta = 0.25
probe time = 4
noise sigma = 0.03 rad
history dose = 0, 0.5, 1.0
```

For these settings,

```math
f_M(4) = 2.52848.
```

## Representative seeded results

```text
null:
  true lambda_M = 0
  fit = -0.00038 +/- 0.00075
  z = -0.51

weak signal:
  true lambda_M = 0.005
  fit = 0.00529 +/- 0.00076
  z = 6.92

moderate signal:
  true lambda_M = 0.010
  fit = 0.00978 +/- 0.00075
  z = 13.09

strong signal:
  true lambda_M = 0.020
  fit = 0.01981 +/- 0.00075
  z = 26.27
```

These are synthetic injected-signal recoveries, not empirical detections.

## Why this is stronger than Simulation 4

Simulation 4 asked whether two different memory histories could generate different trajectories if a memory coupling were inserted.

Simulation 4b showed that a smooth trajectory alone is not unique because ordinary drift can mimic it.

Simulation 4c changes the causal design:

```text
history assignment is randomized
hardware identity is fixed/crossed
history dose is varied
sham dose = 0 trials are interleaved
```

A genuine history-linked residual should therefore follow the assigned history contrast rather than the physical arm or run order.

This is much closer to the structure needed for a real falsifiable experiment.

## What this simulation establishes

It establishes only a design principle:

> If an SoCT-like residual exists and follows randomized history labels, a crossover/dose design can make it statistically identifiable even when smooth apparatus drift exists.

It does **not** establish that such a residual exists in nature.

## Remaining confounds

A realistic design still has to test:

- imperfect present-state matching after different history preparations;
- history-dependent heating, decoherence, charge accumulation, trap shifts, or calibration changes;
- preparation pulses that differ physically between history-dose conditions;
- leakage of the randomized history label into control electronics or timing;
- non-Gaussian and correlated noise;
- multiple-comparison and stopping-rule bias;
- uncertainty in the mapping from record production to `M_0`.

## Next gate — Simulation 4d

The next simulation should model **preparation-induced physical carryover**.

Instead of assuming the two history protocols leave identical ordinary quantum and hardware states, introduce measurable residual covariates such as

```text
temperature/heating proxy
coherence loss
frequency shift
pulse count / control-energy exposure
environmental occupation
```

Then ask whether randomized history dose retains an independent coefficient after those ordinary carryover variables are included.

This is necessary because a real experiment cannot simply assert that two differently prepared systems have the same present physical state.

## Pass/fail logic

```text
PASS DESIGN GATE:
  injected history coefficient follows randomized label/dose,
  fixed-arm offsets do not mimic it,
  sham trials remain null,
  and known carryover covariates can be included without destroying identifiability.

FAIL DESIGN GATE:
  apparent signal follows hardware or preparation energy,
  disappears after ordinary carryover controls,
  or sham procedures reproduce the same effect.
```

## Claim boundary

This is a synthetic design study. It demonstrates identifiability under specified assumptions and injected effects. It is not evidence for a physical memory field or history-dependent quantum dynamics.
