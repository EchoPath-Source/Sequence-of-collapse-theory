# P1 Working Draft v0.1

# Age-Dependent Rotation Curves in SPARC Galaxies: A Preliminary Test of Gravitational Memory

**Author:** Antoine L. Shephard  
**Status:** PRELIMINARY / working draft  
**Claim level:** empirical correlation reported; physical mechanism unproven  
**Repository package:** P1 — Age-Dependent Rotation Curves (SPARC)  
**Target:** preprint / journal manuscript after independent audit and reproducibility rerun

---

## Abstract draft

We investigate whether inferred outer dark-matter fraction in SPARC galaxies correlates with stellar-population age, as predicted by gravitational-memory interpretations in which accumulated dynamical history contributes to apparent large-scale gravitational excess. Using a derived table of 175 SPARC galaxies, the preliminary analysis reports a modest positive association between best-estimate stellar age and outer dark-matter fraction. The current repository package includes the derived data table and a runnable analysis script to regenerate correlation summaries, mass-bin checks, bootstrap summaries, nonlinear memory-fit parameters, and figures. The current result should be interpreted as a preliminary empirical correlation only. It does not establish a modified-gravity mechanism, does not rule out assembly-history or age-proxy systematics, and requires independent age validation and external reproduction before publication-grade claims.

---

## 1. Introduction

Galaxy rotation curves remain one of the central empirical motivations for dark matter and/or modified gravitational dynamics. Standard analyses typically compare observed circular velocities with the contribution expected from baryonic components. In this paper-track package, we test a narrower question:

> Do older stellar populations in SPARC galaxies show systematically higher inferred outer dark-matter fractions?

Within the Sequence of Collapse Theory (SoCT) research program, this is treated as a first empirical probe of a memory-field hypothesis: if gravitational excess partly reflects accumulated collapse or dynamical history, older systems should show stronger apparent memory signatures than younger systems, all else equal.

The present draft is deliberately conservative. The analysis is framed as a correlation test, not as evidence sufficient to establish a new gravitational theory.

---

## 2. Data

### 2.1 Source table

Canonical derived dataset:

```text
data/sparc/sparc_age_fdm_data.csv
```

Primary fields:

- `galaxy`: SPARC galaxy identifier.
- `fdm_outer_mean`: inferred outer dark-matter fraction.
- `age_best`: best-estimate stellar age in Gyr.
- `age_source`: whether the age is literature-derived or proxy-derived.
- `SB0_disk_Lpc2`: disk central surface-brightness proxy.
- `Vmax_kms`: maximum circular velocity.
- `Rmax_kpc`: maximum measured radius.

### 2.2 Derived outer dark-matter fraction

The working observable is:

```math
f_{DM} = 1 - \left(\frac{V_{bar}}{V_{obs}}\right)^2
```

computed at the outer measured rotation-curve region in the derived table.

### 2.3 Caveats

The age column is mixed. Some entries use literature values; others use proxy estimates. This is the dominant interpretive limitation and must be addressed before submission.

---

## 3. Methods

Canonical reproducibility script:

```text
notebooks/sparc/sparc_age_dm_analysis.py
```

Run from repository root:

```bash
python notebooks/sparc/sparc_age_dm_analysis.py
```

The script generates:

```text
observations/sparc/results/sparc_age_fdm_summary.csv
observations/sparc/results/sparc_mass_bin_summary.csv
observations/sparc/results/sparc_bootstrap_summary.csv
observations/sparc/results/sparc_memory_fit_parameters.csv
figures/sparc/sparc_age_fdm_scatter.png
figures/sparc/sparc_memory_fit.png
figures/sparc/sparc_mass_bins.png
```

### 3.1 Correlation tests

The primary reported test is the association between `age_best` and `fdm_outer_mean`.

The script reports:

- Pearson correlation.
- Spearman correlation.
- Mass-proxy correlation.
- Partial Spearman age--fDM relation controlling for mass proxy.

### 3.2 Bootstrap validation

The script performs bootstrap resampling with a fixed seed to estimate stability of Pearson and Spearman correlations.

### 3.3 Mass-bin validation

The sample is split into mass-proxy tertiles and the age--fDM relation is measured within each bin.

### 3.4 Nonlinear memory fit

The working memory model is:

```math
f_{DM}(t) = f_0 + A_{mem}\left(1 - e^{-t/\tau}\right)
```

where:

- `f0` is the baseline outer discrepancy.
- `A_mem` is the fitted memory-amplitude term.
- `tau` is the characteristic accumulation timescale in Gyr.

This fit is exploratory and should not be interpreted as a validated physical parameter until replicated.

---

## 4. Preliminary Results

The imported publication-summary artifact reports:

- Pearson age vs outer fDM: `r = +0.201`, `p = 0.0077`, `n = 175`.
- Spearman age vs outer fDM: `rho = +0.211`, `p = 0.0050`.
- Strongest reported mass-bin signal: mid-mass bin, `r = +0.456`, `p = 0.0003`.

These are preliminary reported values. The canonical values for future citation should be the values regenerated from the committed script and stored in `observations/sparc/results/` after an audited run.

---

## 5. Interpretation

### 5.1 Conservative interpretation

The current package supports this limited claim:

> In the derived SPARC age--fDM table, older galaxies show a modest positive association with inferred outer dark-matter fraction.

### 5.2 SoCT interpretation

Within SoCT, this trend is consistent with the hypothesis that apparent gravitational excess may include a history-dependent memory component. In effective-G language, the minimal model can be written:

```math
G_{eff}(x,t) = G_0[1 + \alpha M(x,t)]
```

with a coarse age-dependent accumulation term:

```math
M(t) \sim 1 - e^{-t/\tau}
```

This provides an interpretable bridge between the empirical fit and the broader memory-field framework, but it remains a hypothesis rather than an established mechanism.

---

## 6. Alternative Explanations and Confounds

The following alternatives must be treated seriously:

1. Age-proxy systematics.
2. Stellar population modeling bias.
3. Assembly-history effects.
4. Surface-brightness / structural covariates.
5. Environmental effects and interaction history.
6. Selection effects in the derived table.

The mass-control and mass-bin tests are useful but not sufficient to eliminate these explanations.

---

## 7. Required Next Work Before Submission

Minimum needed before a submission-ready P1 manuscript:

1. Rerun the committed analysis script and archive generated results.
2. Confirm that generated results match the reported summary values.
3. Add a results README describing each generated table and figure.
4. Add independent age-proxy validation where possible.
5. Add clear provenance for all age estimates.
6. Freeze selection cuts.
7. Add a limitations section with explicit claim boundaries.
8. Decide whether the paper is framed as:
   - observational correlation note, or
   - theory-motivated empirical test.

---

## 8. Current Claim Boundary

Status label:

```text
PRELIMINARY
```

Allowed language:

- "consistent with gravitational-memory predictions"
- "preliminary empirical correlation"
- "requires independent validation"
- "does not establish mechanism"

Avoid:

- "confirmed memory gravity"
- "proof of SoCT"
- "dark matter replacement demonstrated"
- "publication-ready detection"

---

## 9. Repository References

Data:

```text
data/sparc/sparc_age_fdm_data.csv
```

Script:

```text
notebooks/sparc/sparc_age_dm_analysis.py
```

Publication summary artifact:

```text
papers/sparc-age-dm/SPARC_Age_DM_Publication_Summary.md
```

Expected outputs:

```text
observations/sparc/results/
figures/sparc/
```

---

## 10. Draft Status

This is a manuscript scaffold. It is not yet submission-ready. Its purpose is to convert the P1 package from imported data/code into a structured paper track with explicit claim boundaries.
