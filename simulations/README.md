# Simulations Hub

This folder is reserved for computational, modeling, and validation materials.

## What belongs here

- symbolic derivations translated into code
- parameter sweeps
- simulation screenshots
- validation summaries
- numerical experiments for memory kernels
- SPARC fitting outputs
- CMB / GW / BH modeling notes
- notebooks converted to stable markdown summaries
- effective-G / memory-kernel toy models
- PM void-filament H-split notes and parameter logs

## Current status

The repo now contains runnable simulation material alongside imported and exploratory scaffolds.

### Operational observation program

```text
simulations/observation-qubit-pointer/
```

Simulation 1 is a standard-quantum qubit + two-state pointer benchmark. It sweeps measurement interaction strength and computes pointer trace distance, quantum mutual information, Holevo record information, persistence, and provisional observation-strength diagnostics.

It intentionally includes:

```text
no SoCT memory feedback
no consciousness term
```

so it functions as the null/baseline layer for the observation project.

Related derivation files:

```text
papers/math/soc-operational-observation-model.md
papers/math/soc-observation-to-spacetime-derivation-ladder.md
papers/math/soc-localization-memory-hamiltonian.md
```

The current empirical exploration summary is preserved at:

```text
docs/empirical-exploration-thread-summary-v0-1.md
```

This summary frames the strongest near-term gravitational simulation route as a low-energy effective-G / memory-kernel model rather than a Planck-scale rewrite.

Working phenomenological form:

```math
G_eff(x,t) = G_0 [1 + alpha M(x,t)]
```

Minimal exponential memory form:

```math
M(t) = 1 - exp(-t/tau)
```

## Active simulation directions

1. Operational observation: qubit -> pointer -> environment -> record erasure -> history-matched memory feedback.
2. SPARC memory-fit output tables and parameter logs.
3. PM void-filament H-split parameter logs.
4. Effective-G / memory-kernel toy-model scripts.
5. CMB / gravitational-wave / black-hole comparison models.
6. Parent-child directional-memory toy simulations.

## Observation simulation ladder

```text
Simulation 1: qubit + pointer                 COMPLETE baseline
Simulation 2: qubit + pointer + environment   NEXT
Simulation 3: record erasure                  planned
Simulation 4: SoCT memory feedback             planned
Simulation 5: conscious-access layer           planned only after lower layers stabilize
```

## Suggested structure

```text
simulations/
├─ README.md
├─ observation-qubit-pointer/
│  ├─ README.md
│  ├─ simulate_qubit_pointer.py
│  └─ results.csv
├─ sparc/
├─ memory-kernel/
├─ cosmology/
├─ parent-child-transfer/
└─ imported-assets/
```

## Import rule

For every simulation asset added later, include:

- filename
- date
- source thread or source file
- parameter summary
- whether it is exploratory, illustrative, or validation-grade
- whether it is real-data, synthetic, or toy-model output

## Claim boundary

Simulation outputs should be treated as mechanism checks unless directly tied to observed data and reproducible scripts.

Synthetic signal-injection demonstrations must not be presented as real observational detections.
