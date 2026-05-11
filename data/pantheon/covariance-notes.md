# Pantheon+ Covariance Data Notes

**Status:** Data-ingestion note / not yet parsed into analysis code  
**Uploaded sources:** `Pantheon_cov_subset-5.txt`, `Pantheon_SH0ES_cov.txt.gz`  
**Related test:** `experiments/cosmology/pantheon-environment-h0-test.md`

---

## Purpose

These covariance files support the Pantheon+ environment-dependent H0 test.

The test requires covariance-aware fitting of void and filament supernova subsets:

```text
chi2 = (mu_obs - mu_model)^T C_subset^-1 (mu_obs - mu_model)
```

with:

```text
C_subset = C[indices, indices]
```

---

## Observed File Structure

`Pantheon_cov_subset-5.txt` begins with:

```text
1701
0.03177108
0.00575443
0.00031006
...
```

Interpretation:

> The leading `1701` is consistent with a Pantheon-style flattened covariance matrix for a 1701-entry sample.

This must be verified before use.

---

## Required Ingestion Steps

1. Read first value as `N`.
2. Confirm remaining value count equals `N * N`.
3. Reshape flattened array into an `N x N` covariance matrix.
4. Verify matrix symmetry.
5. Check diagonal values are positive.
6. Check numerical conditioning.
7. Match covariance row/column order to the Pantheon+ supernova table.
8. Only then extract void/filament submatrices.

---

## Required Data Pairings

The covariance matrix alone is insufficient.

The Pantheon+ environment-H0 test also requires:

- SN ID;
- redshift `z`;
- distance modulus `mu_obs`;
- RA / Dec;
- host redshift if available;
- environment label: void / filament / unclassified;
- catalog source for environment classification.

---

## Analysis Boundary

Do not fit H0 using diagonal-only uncertainties except as a diagnostic robustness check.

Primary analysis must use full covariance submatrices.

---

## Next Work

Create:

```text
notebooks/pantheon_environment_h0_test.ipynb
```

with functions:

```python
load_flat_covariance(path) -> np.ndarray
validate_covariance(C) -> dict
extract_subset_covariance(C, indices) -> np.ndarray
fit_h0_for_subset(sn_table, C_subset, omega_m=0.315) -> result
```

---

## Repo Boundary

Raw covariance files may be large. If committed, place them under:

```text
data/pantheon/raw/
```

If not committed, document their source URL, checksum, and local filename here.
