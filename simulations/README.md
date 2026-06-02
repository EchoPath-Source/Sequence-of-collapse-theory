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

The repo has been initialized with simulation structure and empirical scaffolding.

No raw simulation datasets or runnable notebooks have been imported yet.

The current empirical exploration summary is preserved at:

```text
docs/empirical-exploration-thread-summary-v0-1.md
```

This summary frames the strongest near-term simulation route as a low-energy effective-G / memory-kernel model rather than a Planck-scale rewrite.

Working phenomenological form:

```math
G_eff(x,t) = G_0 [1 + alpha M(x,t)]
```

Minimal exponential memory form:

```math
M(t) = 1 - exp(-t/tau)
```

## Recommended first imports

1. SPARC memory-fit output tables and parameter logs.
2. PM void-filament H-split parameter logs.
3. Effective-G / memory-kernel toy-model scripts.
4. Any plots or tables tied to the Unified Physics Framework.
5. Validation screenshots or summary tables from prior work.
6. Any code that explores:
   - memory kernels
   - age-dependent rotation curves
   - collapse weighting
   - void-filament expansion differentials
   - black-hole compression / bounce intuition
7. Any exported notebooks or scripts from local or thread work.

## Suggested structure

```text
simulations/
├─ README.md
├─ sparc/
│  ├─ notes.md
│  ├─ parameter-log.md
│  └─ outputs/
├─ memory-kernel/
│  ├─ effective-g-memory-model.md
│  ├─ notes.md
│  └─ outputs/
├─ cosmology/
│  ├─ pm-void-filament-hsplit-notes.md
│  ├─ cmb-correlation-notes.md
│  ├─ hubble-memory-drag-notes.md
│  └─ outputs/
├─ black-hole/
│  ├─ soc-bh-01-notes.md
│  └─ outputs/
└─ imported-assets/
   ├─ screenshots/
   ├─ tables/
   └─ charts/
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
