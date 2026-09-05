# SOC-HISTORY-01 — History-Dependent Quantum Memory Test

**Status:** Platform-specific protocol-design stage

SOC-HISTORY-01 is the first proposed laboratory-facing experiment arising from the operational-observation simulation ladder.

The experiment asks whether a later quantum observable can retain a reproducible dependence on **randomized prior durable-record history** after the prespecified ordinary present state, preparation carryover, hardware assignment, drift, sham histories, negative controls, covariate measurement error, and plausible omitted-variable strength have been bounded.

## Current artifacts

- `PREREGISTRATION_DRAFT.md` — general protocol skeleton and conservative interpretation gates.
- `PLATFORM_COMPARISON.md` — comparison of candidate quantum platforms against SOC-HISTORY-01 requirements.
- `TRAPPED_ION_PROTOCOL_DRAFT.md` — current preferred first implementation using a data ion, measured/reset record ancilla, and strongly preferred spectator nuisance monitor.

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

## Current preferred platform

Trapped ions are the current preferred first platform because selective mid-circuit measurement/reset, shelving/hiding of protected qubits, recooling, long-coherence Ramsey readout, and explicit measurement-crosstalk diagnostics map well onto the failure modes identified in Simulations 4b-4f.

The preferred conceptual register is:

```text
D = data / Ramsey probe ion
A = record-bearing ancilla measured and reset mid-circuit
S = spectator nuisance-monitor ion
```

The ion species, trap architecture, exact gates, history dose, probe time, equivalence margins, noise model, and sample size remain intentionally unfrozen pending laboratory-specific calibration.

## Current gate

The next Track-1 task is to convert the trapped-ion draft into a laboratory parameter sheet and power/sensitivity plan without inventing hardware values. That requires either a specific collaborating platform or a deliberately parameterized design covering realistic calibration ranges.

## Explicit scope boundary

This experiment does not test consciousness. It targets the lower physical question of history-dependent memory feedback only.
