# SPARC Reproducibility Runsheet

**Track:** P1 — Memory-Field Gravity / SPARC / SoCT-PM  
**Status:** required before public empirical claim escalation  
**Goal:** make the SPARC candidate result reproducible from committed inputs.

---

## Target standard

A visiting physicist or technically skilled reviewer should be able to:

```text
clone repo
install requirements
run notebook or script
regenerate tables
regenerate figures
compare output to committed result summaries
inspect controls and limitations
```

---

## Current candidate result to reproduce

The current radial-decomposition claim is intentionally conservative:

> In the clean disk-dominated, high-quality SPARC subset, the correlation between WISE color / formation-history proxy and apparent dark residual is stronger in the outer rotation curve than in the inner region, especially when using an effective-radius split.

Current candidate headline from the existing summary:

```text
Disk-dominated + Q=1 subset
N = 56

Half-radius split:
inner fDM Spearman rho = -0.553, p = 9.79e-6
outer fDM Spearman rho = -0.657, p = 3.71e-8

Effective-radius split:
inner fDM Spearman rho = -0.409, p = 0.00177
outer fDM Spearman rho = -0.637, p = 1.31e-7
```

---

## Files that should exist

```text
observations/sparc/
├─ README.md
├─ SPARC_REPRODUCIBILITY_RUNSHEET.md
├─ sparc_age_dark_matter_analysis.ipynb
├─ scripts/
│  └─ regenerate_inner_outer_summary.py
├─ data/
│  ├─ sparc_age_fdm_data.csv
│  └─ sparc_wise_inner_outer_fdm_split.csv
├─ results/
│  ├─ summary.json
│  ├─ correlation_table.csv
│  ├─ inner_outer_correlation_summary.csv
│  └─ bootstrap_results.csv
└─ figures/
   ├─ age_dm_full_sample.png
   ├─ age_dm_mass_bins.png
   └─ inner_outer_radial_decomposition.png
```

---

## Minimum notebook/script sections

### 1. Data provenance

- identify original SPARC files used;
- identify derived WISE/color/age proxy source;
- explain all joins and exclusions;
- document whether rows are galaxy-level or radial-point-level.

### 2. Derived quantities

At minimum, regenerate:

```text
f_DM(r) = 1 - [V_gas^2 + V_disk^2 + V_bulge^2] / V_obs^2
```

and galaxy-level summaries:

```text
fDM_inner_half_mean
fDM_outer_half_mean
fDM_inner_Reff_mean
fDM_outer_Reff_mean
fDM_outer_minus_inner_half
fDM_outer_minus_inner_Reff
```

### 3. Sample filters

Regenerate correlations for:

- all galaxies;
- Q=1 high-quality curves;
- disk-dominated galaxies;
- disk-dominated + Q=1 galaxies.

### 4. Correlation table

For every subset and split, output:

```text
subset
N
metric
Spearman rho
p-value
Pearson r
p-value
notes
```

### 5. Bootstrap confidence intervals

Run bootstrap on the core Disk + Q=1 subset.

Suggested output columns:

```text
subset
metric
n_bootstrap
rho_median
rho_ci_2p5
rho_ci_97p5
p_median
```

### 6. Controls and confounds

At minimum, test sensitivity to:

- stellar mass / logM;
- luminosity / logL;
- surface brightness / SBeff;
- gas fraction if available;
- morphology / bulge fraction;
- outliers / leverage points;
- alternate split definitions.

### 7. Figures

Generate publication-safe figures:

- outer fDM vs g-W1;
- inner vs outer correlation comparison;
- effective-radius split comparison;
- residual/control plots if available.

---

## Claim-language rule

Use:

> Candidate evidence suggests that formation-history proxies are more strongly associated with outer apparent dark residuals than inner residuals in a clean SPARC subset.

Avoid:

> The SPARC analysis proves dark matter is collapse memory.

---

## Completion checklist

- [ ] Notebook/script committed.
- [ ] Dependencies documented.
- [ ] Derived CSV committed or source regeneration documented.
- [ ] `inner_outer_correlation_summary.csv` regenerated from code.
- [ ] Bootstrap table committed.
- [ ] Figures committed.
- [ ] Controls/confounds note committed.
- [ ] P1 paper draft links to this runsheet.
- [ ] README and STATUS updated after reproduction works.
