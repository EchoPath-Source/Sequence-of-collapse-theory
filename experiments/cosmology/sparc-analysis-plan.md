# SPARC Collapse-Memory Analysis Plan

**Status:** Analysis scaffold / P1 empirical anchor target  
**Primary source anchors:** SoCT memory-field framing, PNT memory-kernel discussion, SPARC disk-galaxy rotation-curve dataset.

---

## Core Question

Do galaxy rotation-curve residuals or inferred dark-fraction behavior correlate with collapse-history proxies such as stellar population age, interaction history, morphology, environment, or baryonic concentration?

---

## SoCT/PNT Motivation

SoCT proposes that collapse events leave accumulated spacetime memory traces. PNT proposes a possible physical substrate for that memory field as long-lived entanglement residue from successful and failed Planck-scale nucleation events.

In the PNT working model, the memory field can be written schematically as:

```text
M(x,t) = integral over nucleation/collapse events of w_i * K(|x-x_i|, t-t_i) dt
```

with a gigayear-scale memory kernel discussed in prior SoCT/PNT work.

---

## Primary Hypothesis

Older or more interaction-rich galactic systems should show stronger apparent missing-mass behavior than younger or less collapse-history-rich systems after controlling for baryonic mass distribution.

---

## Key Tests

### 1. Age vs Dark Fraction

Estimate whether inferred dark fraction correlates with stellar population age proxies.

Candidate dependent variables:

- total inferred dark fraction;
- outer dark fraction;
- mass discrepancy at fixed radius;
- residual from baryonic Tully-Fisher relation;
- residual from standard mass-model prediction.

### 2. Radial Decomposition

Test whether the proposed memory-field contribution is stronger in outer rotation-curve regions than inner baryon-dominated regions.

Working expectation:

```text
memory signal should be more visible in outer halo / low-baryon-acceleration regimes
```

### 3. Environment / Interaction History

Compare field galaxies, cluster/filament environments, and interaction-rich systems where data permit.

### 4. Null Comparison Against Standard Predictors

Compare SoCT memory proxies against standard predictors:

- baryonic mass;
- stellar disk scale length;
- gas fraction;
- morphology;
- surface brightness;
- halo model parameters;
- MOND-style acceleration scaling.

---

## Required Controls

- distance uncertainties;
- inclination uncertainties;
- stellar mass-to-light ratio assumptions;
- gas contribution;
- morphology and surface brightness;
- environment;
- sample-selection effects;
- covariance between age and mass.

---

## Falsification / Weakening Criteria

The collapse-memory interpretation is weakened if:

1. age/collapse-history proxies do not improve predictions beyond baryonic predictors;
2. apparent signal disappears after controlling for morphology, mass, and environment;
3. radial decomposition shows no outer-region preference;
4. standard halo or MOND-style models explain the same residuals with fewer assumptions;
5. inferred memory timescale is unstable across subsamples.

---

## Output Targets

```text
data/sparc/
  source-notes.md
  derived-table-schema.md

notebooks/
  sparc_memory_field_analysis.ipynb

figures/sparc/
  age_vs_dark_fraction.png
  radial_decomposition.png
  residuals_by_environment.png

papers/cosmology/sparc/
  sparc-collapse-memory-paper-draft.md
```

---

## Publication Role

This is the recommended P1 empirical anchor paper before the broader SoCT synthesis.

Working title:

> Collapse-Memory Signatures in SPARC Rotation Curves: A Pre-Registered Reanalysis of Age, Radius, and Apparent Dark Fraction
