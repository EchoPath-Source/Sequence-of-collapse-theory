# SOC-HISTORY-01 — History-Dependent Quantum Memory Test

**Status:** Protocol-design stage

SOC-HISTORY-01 is the first proposed laboratory-facing experiment arising from the operational-observation simulation ladder.

The experiment asks whether a later quantum observable can retain a reproducible dependence on **randomized prior durable-record history** after the prespecified ordinary present state, preparation carryover, hardware assignment, drift, sham histories, negative controls, covariate measurement error, and plausible omitted-variable strength have been bounded.

## Current artifact

- `PREREGISTRATION_DRAFT.md` — protocol skeleton and conservative interpretation gates.

## Core null

```math
lambda_H = 0
```

after ordinary present-state and nuisance controls.

## Core design principle

```text
different randomized record history
+ matched ordinary present state
+ crossed hardware
+ sham preparation
+ negative controls
+ calibrated carryover measurements
+ hidden-variable sensitivity
-> test for a remaining history-associated residual
```

A nominal residual is not automatically interpreted as SoCT memory.

## Current gate

The protocol is not ready for external preregistration until a physical platform and the platform-specific operations, observables, equivalence margins, noise estimates, effect-size target, sample size, and exact analysis are frozen.

## Explicit scope boundary

This experiment does not test consciousness. It targets the lower physical question of history-dependent memory feedback only.
