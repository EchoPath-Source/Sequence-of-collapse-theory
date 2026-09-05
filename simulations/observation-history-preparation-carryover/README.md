# Simulation 4d — Preparation Carryover Controls

**Status:** Adversarial synthetic control model  
**Purpose:** Test whether ordinary preparation-induced physical differences can mimic a randomized history-dependent SoCT residual.

## Why this matters

Simulation 4c improved identifiability by randomizing and crossing the assigned history dose between physical arms. That protects against fixed hardware offsets and smooth run-order drift.

But a deeper confound remains:

> Different history-preparation protocols may leave different ordinary physical states behind.

Examples include:

```text
heating / temperature shift
coherence loss
frequency shift
pulse-count or control-energy exposure
environmental occupation
charge accumulation
trap or cavity shifts
```

If those variables follow the randomized history label, they can imitate a history-dependent effect even in a crossover design.

## Synthetic model

Each trial receives a randomized signed history contrast `h` as in Simulation 4c.

Three measured carryover covariates are generated so that they are intentionally correlated with the history assignment:

```text
heat
coherence_loss
pulse_exposure
```

The synthetic outcome contains:

```math
y = apparatus + drift + ordinary_carryover + lambda_M h f_M + noise.
```

Two analysis models are compared.

### Naive model

```math
y = a_0 + a_1 r + lambda_M h f_M + epsilon.
```

### Carryover-adjusted model

```math
y = a_0 + a_1 r + lambda_M h f_M
    + gamma_H H
    + gamma_C C
    + gamma_P P
    + epsilon.
```

## Representative result: a false positive appears easily

In the `carryover_only_null_memory` scenario, the true memory coupling is

```text
lambda_M = 0.
```

The naive model nevertheless returns approximately

```text
lambda_fit = 0.00864 +/- 0.00038
z ~ 23.0
```

because the history label is correlated with ordinary preparation carryover.

After explicitly adjusting for the measured carryover variables:

```text
lambda_fit = 0.00223 +/- 0.00175
z ~ 1.28
```

which is consistent with no injected memory term in this seeded toy realization.

This is an important negative-control result:

> Randomization of history labels is necessary, but not sufficient, if the history protocol itself changes the ordinary present physical state.

## Injected-signal cases

For a weak injected memory term

```text
true lambda_M = 0.005
```

the naive estimate is badly inflated by carryover:

```text
naive ~ 0.01418
```

while the adjusted estimate is much closer:

```text
adjusted ~ 0.00416 +/- 0.00173.
```

For a moderate injected term

```text
true lambda_M = 0.010
```

the naive estimate is again inflated:

```text
naive ~ 0.01811
```

while the adjusted model recovers

```text
adjusted ~ 0.01075 +/- 0.00177.
```

These are synthetic injected-signal recoveries only.

## Core lesson

A credible SoCT history experiment must satisfy a much stricter statement than

```text
same intended quantum state
```

or

```text
same nominal hardware configuration.
```

It must demonstrate that all measured ordinary present-state consequences of the preparation history are either:

```text
matched,
randomized independently,
measured and adjusted,
or bounded below the target effect size.
```

Otherwise an ordinary preparation artifact can masquerade as `M`.

## Revised discriminator

The stronger target becomes:

```text
randomized prior durable-record history
+ matched target quantum state
+ measured preparation carryover
+ crossover hardware assignment
+ sham history controls
-> residual follows history dose after ordinary present-state covariates are removed.
```

Only such a residual would be worth taking to a more serious SoCT-specific interpretation.

## Next gate — Simulation 4e / protocol design

Before moving to consciousness, the lower observation-memory track should now translate this into a candidate experimental protocol architecture with:

1. history-dose preparation and sham preparation;
2. randomized/crossover arm assignment;
3. independent present-state tomography or calibration;
4. measured carryover channels;
5. preregistered nuisance model;
6. fixed stopping rules and effect-size thresholds;
7. blinded history labels during primary analysis;
8. explicit standard-QM null simulations.

A useful Simulation 4e could test **unmeasured carryover** and measurement error in the covariates to determine how accurately ordinary state variables must be characterized before a history residual becomes interpretable.

## Claim boundary

This simulation deliberately demonstrates how a false positive can arise. It does not provide evidence for a physical memory field. Its value is methodological: it identifies a confound that any future SoCT history experiment must control.
