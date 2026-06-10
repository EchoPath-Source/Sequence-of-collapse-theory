# SPARC Age / Missing-Mass Reproducibility Package

**Evidence label:** `real-data-analysis` for controlled files, with clear separation from exploratory or synthetic material.  
**Status:** Preliminary reproducibility package. Derived CSVs, result tables, figures, and a runnable Python script are present; a full notebook and final provenance review are still pending.  
**Purpose:** Provide a reproducible empirical test of the SoCT gravitational memory-field hypothesis using galaxy rotation-curve and stellar-population data.

This folder is the executable home for SPARC-related observational work tied to the Sequence of Collapse research program.

---

## Research Question

Does galaxy age or formation-history proxy correlate with inferred dark-matter / missing-mass fraction after controlling for standard confounds?

---

## SoCT Motivation

If collapse history leaves a cumulative memory-field imprint, older systems should show a measurable relationship between stellar age / assembly history and inferred missing-mass fraction, especially in outer regions where baryonic closure is weakest.

This does not by itself prove the SoCT memory field. A positive signal must survive standard astrophysical controls and be compared against conventional explanations such as assembly bias, environment, morphology, gas fraction, and surface brightness.

---

## Current Target Claim to Reproduce

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

## Current Artifact Status

```text
observations/sparc/
├─ README.md
├─ analyses/
│  └─ current-status-note.md
├─ data/
│  ├─ sparc_age_fdm_data.csv
│  └─ sparc_wise_inner_outer_fdm_split.csv
├─ results/
│  ├─ outer_mass_discrepancy_analysis.md
│  ├─ inner_outer_radial_decomposition_summary.md
│  └─ inner_outer_correlation_summary.csv
├─ scripts/
│  └─ README.md
└─ tables/
   └─ README.md
```

Repo-level mirrors and supporting artifacts also exist at:

```text
data/sparc/
notebooks/sparc/sparc_age_dm_analysis.py
notebooks/sparc/sparc_age_fdm_analysis.py
figures/sparc/
papers/p1-age-dependent-rotation-curves-sparc/results/
```

Notes:

- `notebooks/sparc/sparc_age_dm_analysis.py` is the canonical runnable Python script.
- `notebooks/sparc/sparc_age_fdm_analysis.py` is a compatibility wrapper for older manifests that expected the exact `age_fdm` filename.
- `observations/sparc/data/` is the canonical runnable data location for this observations package.
- `data/sparc/` remains a repo-level mirror until data provenance is fully settled.

---

## Current Reproduction Command

From repository root:

```bash
python notebooks/sparc/sparc_age_dm_analysis.py
```

or, using the compatibility filename:

```bash
python notebooks/sparc/sparc_age_fdm_analysis.py
```

The script writes summary tables to:

```text
observations/sparc/results/
```

and figures to:

```text
figures/sparc/
```

---

## Current Analysis Flow

1. Load committed SPARC derived age/fDM data.
2. Compute the mass proxy used in the preliminary controls.
3. Run baseline Pearson and Spearman correlation tests.
4. Run mass-bin summaries.
5. Run partial Spearman control against mass proxy.
6. Bootstrap uncertainty and sign stability.
7. Fit the exploratory memory-saturation curve.
8. Produce reproducible tables and figures.
9. State limitations and conventional interpretations.

---

## Inner / Outer Radial Decomposition

The radial-decomposition subtrack is now represented by:

```text
observations/sparc/results/inner_outer_radial_decomposition_summary.md
observations/sparc/results/inner_outer_correlation_summary.csv
observations/sparc/data/sparc_wise_inner_outer_fdm_split.csv
```

Claim-safe summary:

> In the clean disk-dominated, high-quality SPARC subset, the formation-history proxy association appears stronger in outer apparent dark residuals than inner residuals, especially under the effective-radius split. This is candidate evidence only and requires full reproduction and conventional controls.

---

## Minimal Reproducibility Standard

A reviewer should be able to:

```text
clone repo
install requirements
run the script or notebook
reproduce reported tables and plots
inspect source data and controls
```

The current Python script is a reproducibility-support artifact. A publication-ready notebook is still recommended.

---

## Controls to Prioritize

- Stellar mass / baryonic mass.
- Total luminosity.
- Vmax and Rmax.
- Disk surface brightness.
- Gas fraction.
- Morphology / bulge fraction.
- Environment / cosmic-web classification.
- Age-proxy source and measurement uncertainty.

---

## Remaining Missing / Needed Items

```text
observations/sparc/sparc_age_dark_matter_analysis.ipynb
observations/sparc/scripts/reproduce_inner_outer_radial_decomposition.py
observations/sparc/scripts/reproduce_outer_mass_discrepancy.py
figures/sparc/figure-provenance.md updates for all current SPARC figures
```

Also needed for stronger P1 paper support:

```text
SPARC_age_fdm_regression_models.csv review / regeneration path
mass_proxy_comparison.csv review / regeneration path
SPARC_age_vs_fdm_scatter.png or canonical equivalent
```

---

## Claim Boundary

Use:

> The SPARC package contains preliminary reproducibility artifacts and candidate empirical signals that motivate further controlled testing of a memory-field gravity hypothesis.

Avoid:

> The SPARC package proves SoCT, disproves dark matter, or confirms memory-based gravity.
