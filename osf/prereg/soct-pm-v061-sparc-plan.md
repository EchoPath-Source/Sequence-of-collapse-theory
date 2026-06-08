<!--
Source import note:
- Source files: OSF_Prereg_SoCT_PM_v061_and_SPARC_Plan.pdf and OSF_Prereg_Combined_v061.pdf
- Imported as Markdown extraction/summary for OSF and P1/P5 tracking.
- Status: preregistration / methods source.
- Claim boundary: methods and acceptance plan; not an empirical result by itself.
-->

# SoCT-PM v0.6.1 Code Freeze + SPARC Age-fDM Analysis Plan

**Date:** 2026-02-16  
**Project:** Sequence of Collapse Theory (SoCT) - Time-Dependent Gravity / Memory Field Tests

## 1. What this document is

This OSF upload document is intended as a primary preregistration / methods artifact for two linked items:

1. the SoCT-PM particle-mesh simulator code freeze at version v0.6.1; and
2. the observational test on SPARC galaxies relating stellar population age or formation-history proxy to outer dark-matter fraction / apparent missing-mass fraction.

The document should be treated as a preregistration and methods source, not as a final paper.

## 2. SoCT-PM v0.6.1 Code Freeze

**Code label:** SoCT-PM v0.6.1 FINAL - Proper Conformal Time + Emergent H-split

**Core design rule:** Memory affects gravity only through an effective density channel, while the background expansion remains Lambda-CDM.

Key fixes tracked in the source document include:

| Fix | What changed | Why it matters |
|---|---|---|
| Conformal time | scale-factor evolution corrected under conformal time | prevents time-evolution convention errors |
| EOM convention | keeps Poisson and kick convention consistent | removes mixed dynamics conventions |
| Kernel FFT centering | ifftshift before rfftn | prevents spatial wraparound artifacts |

## 3. Validation Smoke Tests

Two smoke tests are required for acceptance:

1. a control run with memory disabled must show no emergent H-split;
2. a memory-enabled run must reproduce the H-split without modifying background expansion directly.

## 4. SPARC Age-fDM Analysis Plan

The SPARC component tests whether stellar population age or formation-history proxies correlate with outer dark-matter fraction / apparent residual structure.

Core empirical question:

> Do older or more evolved systems show stronger apparent missing-mass fractions, especially in outer regions where baryonic closure is weakest?

## 5. Repository Destinations

This Markdown extraction supports:

```text
osf/prereg/
observations/sparc/
papers/p1-age-dependent-rotation-curves-sparc/
simulations/memory-field-pm/
```

## 6. Required Follow-up Artifacts

The repo still needs:

- runnable SPARC script or notebook;
- derived correlation tables;
- partial correlation tables;
- bootstrap tables;
- mass-proxy comparison table;
- generated figures;
- provenance for all SPARC-derived CSVs;
- clear licensing/source notes for any public-data inputs.

## 7. Claim Boundary

Use:

> This preregistration file defines acceptance criteria and analysis intentions for SoCT-PM v0.6.1 and the SPARC age-fDM test.

Avoid:

> This preregistration proves the SPARC result or validates SoCT-PM.
