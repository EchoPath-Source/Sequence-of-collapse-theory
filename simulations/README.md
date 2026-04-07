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

## Current status

The repo has been initialized with **simulation structure only**.
No raw simulation datasets or notebooks have been imported yet.

## Recommended first imports

1. Any plots or tables tied to the Unified Physics Framework
2. Any SPARC analysis files or fitting notes
3. Validation screenshots or summary tables from prior work
4. Any code that explores:
   - memory kernels
   - age-dependent rotation curves
   - collapse weighting
   - black-hole compression / bounce intuition
5. Any exported notebooks or scripts from local or thread work

## Suggested structure

```text
simulations/
├─ README.md
├─ sparc/
│  ├─ notes.md
│  ├─ parameter-log.md
│  └─ outputs/
├─ memory-kernel/
│  ├─ notes.md
│  └─ outputs/
├─ cosmology/
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
