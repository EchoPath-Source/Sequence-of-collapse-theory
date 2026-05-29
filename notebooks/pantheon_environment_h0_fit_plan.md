# Pantheon+ Environment-H0 Fit Notebook Plan

**Status:** scaffold / pending runnable notebook  
**Target notebook:** `notebooks/pantheon_environment_h0_test.ipynb`  
**Claim level:** exploratory until Pantheon+ table, covariance validation, and environment labels are committed

## Purpose

This note defines the reproducibility contract for the Pantheon+ environment-dependent H0 test.

The locked primary prediction is:

```text
H0_void > H0_filament
```

Primary statistic:

```math
\Delta H_0 = H_{0,void} - H_{0,filament}
```

## Required Inputs

```text
data/pantheon/source-notes.md
data/pantheon/environment_labels.csv
```

Large raw covariance files may be stored outside the repo if redistribution or file-size constraints apply. If so, the notebook must document the local path, checksum, and source URL in `data/pantheon/covariance-notes.md`.

## Required Covariance Validation

The notebook must validate the covariance matrix before any H0 fit:

1. read first value as `N`;
2. confirm remaining value count equals `N * N`;
3. reshape into `N x N`;
4. verify symmetry;
5. verify positive diagonal values;
6. report condition number or numerical stability notes;
7. confirm covariance row order matches the Pantheon+ SN table.

## Primary Fit

For each environment subset:

```math
\chi^2 = (\mu_{obs}-\mu_{model})^T C^{-1}_{subset}(\mu_{obs}-\mu_{model})
```

with:

```math
C_{subset} = C[indices, indices]
```

Fixed background cosmology unless otherwise documented:

```text
Omega_m = 0.315
Flat Lambda-CDM background
H0 fit separately for void and filament subsets
```

## Primary Output Files

```text
data/pantheon/results/h0_environment_fit_summary.csv
data/pantheon/results/permutation_test_summary.csv
data/pantheon/results/jackknife_summary.csv
data/pantheon/results/redshift_match_summary.csv
data/pantheon/results/covariance_validation.json
```

## Required Robustness Checks

1. redshift-matched bootstrap;
2. random environment permutation test;
3. sky-region jackknife;
4. diagonal-only covariance diagnostic, clearly labeled non-primary;
5. alternate void/environment catalog if available;
6. redshift-cut sensitivity check.

## Claim Boundary

No environment threshold, redshift cut, or binarization rule should be tuned after inspecting `Delta_H0`.

A positive `Delta_H0` is only a sign-consistency result unless it survives the covariance-aware fit and required robustness checks.
