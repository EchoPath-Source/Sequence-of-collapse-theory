# SPARC Age-DM Analysis Notebook Plan

**Status:** Notebook implementation scaffold  
**Target notebook:** `notebooks/sparc_age_dm_analysis.ipynb`  
**Related data schema:** `data/sparc/derived-data-schema.md`

---

## Purpose

This notebook should reproduce the reported SPARC age-dark-matter correlation from committed data and generate all figures/tables needed for the Paper 1 draft.

---

## Notebook Sections

### 1. Imports and Configuration

Required libraries:

```python
import numpy as np
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
```

Configuration:

```python
DATA_PATH = "data/sparc/sparc_age_fdm_data.csv"
RANDOM_SEED = 20260217
N_BOOTSTRAP = 10000
```

---

### 2. Load and Validate Data

Tasks:

1. Load derived table.
2. Validate required columns.
3. Check for missing values.
4. Confirm sample size.
5. Recompute `f_dm_outer` from velocity columns.
6. Confirm mass-bin assignments.

Expected checks:

```python
assert "age_gyr" in df.columns
assert "f_dm_outer" in df.columns
assert len(df) == 175  # or report actual N after filters
```

---

### 3. Primary Correlation

Compute:

```python
pearson_r, pearson_p = stats.pearsonr(df["age_gyr"], df["f_dm_outer"])
spearman_rho, spearman_p = stats.spearmanr(df["age_gyr"], df["f_dm_outer"])
```

Target reported values:

```text
Pearson r = +0.201, p = 0.0077
Spearman rho = +0.211, p = 0.0050
```

---

### 4. Full-Sample Plot

Generate:

```text
figures/sparc/age_dm_full_sample.png
```

Required features:

- x-axis: mean stellar age in Gyr;
- y-axis: outer dark matter fraction;
- color: `log10(Vmax)` or mass proxy;
- best-fit line;
- annotation box with r, p, sigma;
- legend/caption stating provisional status.

---

### 5. Mass-Binned Analysis

Use terciles by `vmax_kms` unless preregistration specifies otherwise.

Expected bins:

```text
Low:  n = 59, r = +0.115, p = 0.384
Mid:  n = 58, r = +0.456, p = 3.2e-4
High: n = 58, r = +0.277, p = 0.036
```

Generate:

```text
figures/sparc/age_dm_mass_bins.png
```

---

### 6. Partial Correlations

Implement residual-based partial correlation:

1. Regress `age_gyr` on controls.
2. Regress `f_dm_outer` on controls.
3. Correlate residuals.

Controls to test:

```text
Vmax only
Rmax only
SB0 only
Vmax + Rmax
Vmax + Rmax + SB0
```

---

### 7. Multivariate Regression

Models:

```text
f_dm_outer ~ age_gyr
f_dm_outer ~ age_gyr + logVmax + logRmax
f_dm_outer ~ age_gyr + logVmax + logRmax + logSB0
```

Report:

- beta_age;
- standard error;
- p-value;
- adjusted R^2;
- diagnostics.

---

### 8. Bootstrap Confidence Intervals

Bootstrap:

```python
for i in range(N_BOOTSTRAP):
    sample = df.sample(frac=1, replace=True, random_state=seed+i)
    r, p = stats.pearsonr(sample["age_gyr"], sample["f_dm_outer"])
```

Report:

- mean r;
- median r;
- 95% CI;
- fraction of seeds with r > 0;
- fraction with p < 0.05.

---

### 9. Out-of-Sample Validation

Use locked seed:

```python
RANDOM_SEED = 20260217
```

Split:

```text
70% training
30% test
```

Report r and p for:

- train;
- test;
- full sample.

---

### 10. Robustness Checks

Required:

1. Q=1 only.
2. Inclination > 45 degrees.
3. Remove outliers / high leverage points.
4. Alternate f_DM definition.
5. Alternate age proxy, if available.
6. Environment/group membership, if available.
7. Mass-bin threshold sensitivity.
8. Diagonal comparison with structural controls.

---

### 11. Export Tables

Export:

```text
data/sparc/results/primary_correlation.csv
data/sparc/results/partial_correlations.csv
data/sparc/results/mass_bin_results.csv
data/sparc/results/regression_models.csv
data/sparc/results/bootstrap_summary.csv
```

---

### 12. Figure Provenance

Every figure should include:

- script/notebook version;
- data file checksum;
- generation date;
- random seed;
- input columns.

---

## Research Boundary

The notebook should regenerate the results, not tune them.

No changes to filters, bins, or age proxy definitions should be made after inspecting whether they improve the age-f_DM correlation unless explicitly labeled exploratory.
