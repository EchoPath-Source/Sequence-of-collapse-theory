# SPARC Age / Missing-Mass Reproducibility Package

**Evidence label:** `real-data-analysis` for controlled files, with clear separation from exploratory or synthetic material.  
**Status:** Reproducibility scaffold pending derived CSV and runnable notebook.  
**Purpose:** Provide a reproducible empirical test of the SoCT gravitational memory-field hypothesis using galaxy rotation-curve and stellar-population data.

This folder is the executable home for SPARC-related observational work tied to the Sequence of Collapse research program.

---

## Research Question

Does galaxy age correlate with inferred dark-matter / missing-mass fraction after controlling for standard confounds?

---

## SoCT Motivation

If collapse history leaves a cumulative memory-field imprint, older systems should show a measurable relationship between stellar age / assembly history and inferred missing-mass fraction, especially in outer regions where baryonic closure is weakest.

This does not by itself prove the SoCT memory field. A positive signal must survive standard astrophysical controls and be compared against conventional explanations such as assembly bias, environment, morphology, gas fraction, and surface brightness.

---

## Target Claim to Reproduce

Current internally reported candidate signal:

```text
Pearson r(age_gyr, f_dm_outer) = +0.201
p = 0.0077
n = 175

Spearman rho = +0.211
p = 0.0050
```

Mass-bin targets from the current internal summary:

```text
Low mass:  n = 59, r = +0.115, p = 0.384
Mid mass:  n = 58, r = +0.456, p = 3.2e-4
High mass: n = 58, r = +0.277, p = 0.036
```

Claim calibration:

> Candidate empirical signal consistent with the SoCT memory-accumulation prediction.

Do not claim yet:

> Confirmed proof of memory-based gravity.

---

## Folder Structure

```text
observations/sparc/
├─ README.md
├─ requirements.txt
├─ preregistration.md
├─ analysis-plan.md
├─ sparc_age_dark_matter_analysis.ipynb        # to be added
├─ data/
│  ├─ README.md
│  ├─ source-links.md
│  └─ sparc_age_fdm_data.csv                  # to be added or source-linked
├─ results/
│  ├─ README.md
│  ├─ summary.json                            # to be generated
│  ├─ correlation_table.csv                   # to be generated
│  ├─ partial_correlations.csv                # to be generated
│  ├─ mass_bin_results.csv                    # to be generated
│  ├─ regression_models.csv                   # to be generated
│  └─ bootstrap_results.csv                   # to be generated
└─ figures/
   ├─ README.md
   ├─ age_dm_full_sample.png                  # to be regenerated
   └─ age_dm_mass_bins.png                    # to be regenerated
```

---

## Existing Repo Artifacts Feeding This Package

Primary preregistration:

```text
experiments/cosmology/sparc-memory-field-preregistration-v0-1.md
```

Initial analysis plan:

```text
experiments/cosmology/sparc-analysis-plan.md
```

Derived data schema:

```text
data/sparc/derived-data-schema.md
```

Notebook plan:

```text
notebooks/sparc_age_dm_analysis_plan.md
```

Paper draft and result summary:

```text
papers/cosmology/sparc/sparc-age-dm-publication-summary-v1.md
papers/cosmology/sparc/sparc-age-dm-paper-draft.md
```

Figure provenance:

```text
figures/sparc/figure-provenance.md
```

---

## Planned Analysis Flow

1. Load SPARC rotation-curve data and derived galaxy properties.
2. Add or merge stellar-population age estimates from documented sources.
3. Compute missing-mass / inferred dark-matter fraction metrics.
4. Run baseline Pearson and Spearman correlation tests.
5. Run controlled regressions with mass, morphology, gas fraction, surface brightness, and environment where available.
6. Run partial correlations and residualized tests.
7. Bootstrap uncertainty and robustness.
8. Run out-of-sample validation.
9. Produce reproducible tables and figures.
10. State limitations and conventional interpretations.

---

## Minimal Reproducibility Standard

A reviewer should be able to:

```text
clone repo
install requirements
open notebook
run all cells
reproduce reported table and plots
inspect source data and controls
```

---

## Controls to Prioritize

- Stellar mass / baryonic mass.
- Total luminosity.
- Vmax and Rmax.
- Gas fraction.
- Morphology.
- Surface brightness.
- Rotation-curve quality flags.
- Inclination cuts.
- Environment / satellite status if available.
- Stellar-population age source quality.

---

## What Belongs Here

- controlled analysis summaries;
- reproducible scripts and notebooks;
- cleaned tables with named galaxies and defined variables;
- figure exports with provenance notes;
- null or inconclusive findings preserved honestly;
- preregistration text or links.

---

## What Does Not Belong Here

- synthetic demonstrations presented as observational evidence;
- unsourced AI-only summary claims without scripts or underlying tables;
- public-facing theory essays without dataset linkage;
- unlabelled exploratory results presented as final evidence.

---

## Working Rule

Every file added to this folder should state:

1. whether it uses real SPARC data;
2. the age proxy or mass-discrepancy definition used;
3. where the variables came from;
4. whether the result is exploratory, controlled, or publication-ready.

---

## Falsification Condition

The memory-field interpretation is weakened if:

- the age/missing-mass trend disappears in a larger controlled sample;
- the trend is fully explained by standard environmental or assembly variables;
- the radial structure does not match memory-field expectations;
- bootstrap or cross-validation shows the signal is unstable;
- an independent age proxy fails to reproduce the direction.

---

## Immediate Next Step

Add either:

```text
observations/sparc/data/sparc_age_fdm_data.csv
```

or, if the data is not ready to commit:

```text
observations/sparc/data/source-links.md
```

with a complete recipe for regenerating the derived table.
