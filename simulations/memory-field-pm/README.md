# Memory-Field PM Simulation Hub

**Evidence label:** `validated-simulation` for the active reference line, with archived historical steps preserved separately.

This folder is the home for the particle–mesh memory-field simulation program associated with the current Sequence of Collapse Theory cosmology testbed.

## Intended structure

```text
simulations/memory-field-pm/
├─ README.md
├─ code/
├─ outputs/
├─ figures/
└─ validation/
```

## What belongs here
- validated code snapshots for the PM simulation line
- archived intermediate versions kept for provenance
- CSV outputs and parameter-sweep summaries
- figure assets from production or validation runs
- acceptance notes and correction logs

## Current version policy
- **active reference line:** v0.6.1 final
- **archived provenance:** v0.6 initial, v0.6-corrected

## Important usage rule
Any future writeup that references results from this folder should specify:
1. exact code version
2. whether the run was baseline or memory-active
3. whether the artifact is a validation result, exploratory run, or publication figure
