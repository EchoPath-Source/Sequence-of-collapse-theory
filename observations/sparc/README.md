# SPARC Age / Missing-Mass Observational Track

**Evidence label:** `real-data-analysis` for controlled files, with clear separation from exploratory or synthetic material.  
**Status:** scaffold pending runnable notebook.  
**Purpose:** provide a reproducible empirical test of the SoCT gravitational memory-field hypothesis using galaxy rotation-curve and stellar-population data.

This folder is the home for SPARC-related observational work tied to the Sequence of Collapse research program.

## Research question

Does galaxy age correlate with inferred dark-matter / missing-mass fraction after controlling for standard confounds?

## SOC motivation

If collapse history leaves a cumulative memory-field imprint, older systems should show a measurable relationship between stellar age / assembly history and inferred missing-mass fraction, especially in outer regions where baryonic closure is weakest.

This does not by itself prove the SoCT memory field. A positive signal must survive standard astrophysical controls and be compared against conventional explanations such as assembly bias, environment, morphology, gas fraction, and surface brightness.

## Target claim to reproduce

Working claim under review:

```text
A modest positive age / missing-mass correlation exists in disk-galaxy data and remains nonzero after basic controls.
```

This folder should eventually reproduce the result from documented inputs.

## Planned folder structure

```text
observations/sparc/
├─ README.md
├─ sparc_age_dark_matter_analysis.ipynb
├─ requirements.txt
├─ preregistration.md
├─ data/
│  ├─ README.md
│  └─ source-links.md
└─ results/
   ├─ summary.json
   ├─ correlation_table.csv
   └─ bootstrap_results.csv
```

## Planned analysis flow

1. Load SPARC rotation-curve data and derived galaxy properties.
2. Add or merge stellar-population age estimates from documented sources.
3. Compute missing-mass / inferred dark-matter fraction metrics.
4. Run baseline correlation tests.
5. Run controlled regressions with mass, morphology, gas fraction, surface brightness, and environment where available.
6. Bootstrap uncertainty and robustness.
7. Produce reproducible tables and figures.
8. State limitations and conventional interpretations.

## Minimal reproducibility standard

A reviewer should be able to:

```text
clone repo
install requirements
open notebook
run all cells
reproduce reported table and plots
inspect source data and controls
```

## Controls to prioritize

- Stellar mass / baryonic mass
- Total luminosity
- Gas fraction
- Morphology
- Surface brightness
- Rotation-curve quality flags
- Environment / satellite status if available
- Stellar-population age source quality

## What belongs here

- controlled analysis summaries
- reproducible scripts and notebooks
- cleaned tables with named galaxies and defined variables
- figure exports with provenance notes
- null or inconclusive findings preserved honestly
- preregistration text or links

## What does not belong here

- synthetic demonstrations presented as observational evidence
- unsourced AI-only summary claims without scripts or underlying tables
- public-facing theory essays without dataset linkage
- unlabelled exploratory results presented as final evidence

## Working rule

Every file added to this folder should state:

1. whether it uses real SPARC data,
2. the age proxy or mass-discrepancy definition used,
3. where the variables came from,
4. whether the result is exploratory, controlled, or publication-ready.

## Falsification condition

The memory-field interpretation is weakened if:

- the age/missing-mass trend disappears in a larger controlled sample,
- the trend is fully explained by standard environmental or assembly variables,
- the radial structure does not match memory-field expectations,
- bootstrap or cross-validation shows the signal is unstable.

## Current status

This is a scaffold. The runnable notebook, source links, and result tables still need to be added.
