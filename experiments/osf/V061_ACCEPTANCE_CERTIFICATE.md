# v0.6.1 Acceptance Certificate

**Document Type:** Internal validation and acceptance note  
**Version:** v0.6.1 final  
**Evidence label:** `validated-simulation`

---

## Summary

This document records the acceptance of **SoCT-PM v0.6.1 final** as the current validated implementation line for the memory-field particle–mesh simulation program.

It supersedes earlier v0.6 and v0.6-corrected builds for production-facing analysis.

---

## Critical Fixes Preserved

### A. Conformal-Time Consistency
The implementation was corrected so the scale factor update is treated consistently within the conformal-time scheme used by the model.

### B. Equation-of-Motion Consistency
The kick-drift-kick update was revised so the force and Hubble-friction conventions are internally consistent with the chosen Poisson and velocity definitions.

### C. Kernel FFT Centering
The spatial kernel was centered correctly before the FFT step to avoid wraparound or mis-centering artifacts.

---

## Smoke-Test Outcomes Preserved

### Control Test
A control run with no active memory contribution was used to confirm that no spurious environment-dependent expansion split appears by construction.

### Memory Test
A memory-active run showed the expected sign pattern:
- void-like regions display a more expansion-dominated signature
- filament-like regions display a more collapse-dominated signature

The acceptance logic treated this as consistent with the intended phenomenology while remaining subdominant to the background expansion.

---

## Acceptance Decision

**Accepted for current use** as:
- the production reference implementation for internal parameter sweeps
- the code line associated with the current methods narrative
- the simulation branch safe to archive under validated materials

**Not implied by acceptance:**
- no claim of final theory proof
- no claim that all cosmological sectors are complete
- no automatic elevation of exploratory parent/child-universe work

---

## Version Hierarchy

- `v0.6 initial` — archived historical step
- `v0.6-corrected` — archived historical step
- `v0.6.1 final` — active validated reference line

---

## Recommended Repo Role

This file should be kept with OSF and validation materials so that later paper drafts and prereg outputs can point to a stable implementation checkpoint.
