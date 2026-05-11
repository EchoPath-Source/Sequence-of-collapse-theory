# Pantheon+ Environment-Dependent H0 Test

**Status:** Locked analysis scaffold / prereg-style cosmology test  
**Thread source:** Pantheon+ environment-dependent H0 pipeline lock from SoCT/PNT discussion  
**Claim level:** Independent observational test of the SoCT/PNT prediction that void environments should show higher effective expansion than filament-rich regions.

---

## Purpose

This test evaluates whether supernovae classified as void-environment objects yield a higher best-fit local H0 than supernovae classified as filament-environment objects under a fixed flat Lambda-CDM background.

This is independent of the SPARC rotation-curve track.

- SPARC tests whether galaxy collapse-history proxies correlate with apparent dark-fraction behavior.
- Pantheon+ tests whether large-scale environment affects local expansion.

If both effects hold with compatible timescales, the collapse-memory / PNT memory-residue model becomes substantially stronger.

---

## Required Inputs

### Pantheon+ Supernova Table

Required columns:

- SN ID;
- redshift `z`;
- observed distance modulus `mu_obs`;
- distance-modulus uncertainty;
- RA / Dec;
- host redshift, if available.

### Covariance Matrix

Required file:

```text
Pantheon_cov_subset.txt
```

Note from thread:

```text
The covariance file begins with 1701, consistent with a flattened covariance structure for a 1701-entry Pantheon-style sample.
```

### Environment Labels

Required environment table:

- SN ID;
- environment label: `void`, `filament`, or `unclassified`;
- distance to nearest void center or filament structure;
- catalog source;
- environment-labeling method.

---

## Fixed Hypothesis

Primary directional hypothesis:

```text
H0_void > H0_filament
```

Equivalently:

```text
Delta_H0 = H0_void - H0_filament > 0
```

This aligns with the SoCT/PNT prediction that cosmic voids should show higher effective expansion than filament-rich regions if failed-nucleation / memory-residue effects contribute to late-time dark energy.

---

## Data Cleaning Rules

Before fitting:

1. Keep only SNe with valid `z`, `mu_obs`, covariance entry, and environment label.
2. Remove `unclassified` SNe from the primary test.
3. Do not tune void/filament threshold after seeing `Delta_H0`.
4. Record final `N_void` and `N_filament`.
5. Keep the same redshift cuts for both samples.

Recommended primary redshift cut:

```text
0.01 < z < 0.15
```

This focuses the test on local H0 / environment effects.

---

## Cosmology Model

Use fixed flat Lambda-CDM background except for H0.

Distance modulus model:

```text
mu_model(z; H0) = 5 log10(D_L(z; H0, Omega_m) / 10 pc)
```

Fixed parameter:

```text
Omega_m = 0.315
```

Fit only:

```text
H0
```

for the void and filament subsets separately.

---

## Covariance-Aware Chi-Square

For each subset:

```text
chi2 = (mu_obs - mu_model)^T C_subset^{-1} (mu_obs - mu_model)
```

Use the matching submatrix:

```text
C_subset = C[indices, indices]
```

Do not use diagonal-only errors except as a diagnostic robustness check.

---

## Required Fit Outputs

For each environment report:

```text
N_void
N_filament
H0_void +/- sigma_void
H0_filament +/- sigma_filament
Delta_H0 = H0_void - H0_filament
sigma_Delta
significance = Delta_H0 / sigma_Delta
```

Primary statistic:

```text
Delta_H0
```

---

## Required Robustness Checks

Run these before claiming any signal:

1. Redshift-matched bootstrap.
2. Random environment permutation test.
3. Jackknife by sky region.
4. Repeat using diagonal-only covariance as diagnostic.
5. Repeat with alternate void catalog, if available.
6. Test sensitivity to redshift cuts.

---

## Interpretation Thresholds

| Result | Interpretation |
|---|---|
| correct sign, <1 sigma | Correct sign, not significant |
| correct sign, 1-2 sigma | Suggestive |
| correct sign, 2-3 sigma | Interesting, needs replication |
| correct sign, >3 sigma | Strong candidate signal |
| opposite sign | Tension with SoCT/PNT prediction |

---

## Locked Primary Statement

Use this exact prereg-style wording:

> The primary Pantheon+ test evaluates whether supernovae classified as void-environment objects yield a higher best-fit local H0 than filament-environment objects under a fixed flat Lambda-CDM background, using the full covariance submatrix for each environment subset. The primary statistic is Delta_H0 = H0_void - H0_filament. No environment threshold or redshift cut will be adjusted after inspecting Delta_H0.

---

## Relationship to Existing Repo Tracks

Related files:

```text
experiments/cosmology/sparc-analysis-plan.md
papers/cosmology/pnt/planck-nucleation-theory-master-note.md
papers/pnt-dark-energy-hubble-window/working-draft-v0-1.md
papers/pnt-dark-energy-hubble-window/toy-model-results-v0-1.md
```

---

## Next Implementation Work

1. Add Pantheon+ data source notes.
2. Add environment-catalog selection notes.
3. Add notebook skeleton:

```text
notebooks/pantheon_environment_h0_test.ipynb
```

4. Add data schema:

```text
data/pantheon/environment_labels_schema.md
data/pantheon/covariance_notes.md
```

5. Run dry-fit on mock or subset data before interpreting real output.

---

## Research Boundary

This test should be interpreted cautiously.

A positive result would not prove PNT or SoCT. It would show that the predicted sign of environment-dependent expansion appears in one independent supernova dataset under fixed analysis rules.

A null result would constrain or weaken the environment-expansion branch of the model, but would not directly falsify the SPARC collapse-memory track or SOC-MZI consciousness-collapse track.
