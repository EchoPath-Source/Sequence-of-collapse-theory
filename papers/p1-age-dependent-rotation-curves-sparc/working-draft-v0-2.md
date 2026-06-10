# Age-Dependent Rotation Curves in SPARC Galaxies

**Subtitle:** A PRELIMINARY Test for Temporally Accumulated Gravitational-Memory Signatures in the SPARC Dataset  
**Author:** Antoine L. Shephard (Echo Mirrowen)  
**Affiliation:** Echo Labs Field Harmonics Institute  
**Correspondence:** contact@echopathxr.com  
**OSF Pre-registration:** [OSF DOI PLACEHOLDER]  
**Status:** PRELIMINARY / working manuscript draft  
**Source note:** Markdown working draft converted from the available SPARC paper scaffold that records lineage from `sparc_paper-1.docx`; `sparc_paper.docx` was not present in this checkout.  
**Important boundary:** Numerical values marked `TODO_FROM_SCRIPT_OUTPUT` must be updated only from committed analysis code and data. Do not convert this draft into a claim stronger than PRELIMINARY without independent audit and reproduction.

---

## Abstract Draft

We test whether inferred outer dark-matter fraction in SPARC galaxies is associated with stellar-population age. The working hypothesis, motivated by the Sequence of Collapse Theory (SoCT), is that any history-dependent gravitational-memory contribution would appear as a modest age-associated trend in outer rotation-curve discrepancy, after appropriate structural and mass controls. The current analysis is PRELIMINARY: it may report an empirical correlation in the derived repository table, but it does not establish a physical mechanism, does not rule out conventional assembly-history or age-proxy explanations, and must be independently reproduced before publication-grade claims.

Primary numerical results must be inserted from the committed reproducibility script outputs:

```text
TODO_FROM_SCRIPT_OUTPUT: observations/sparc/results/sparc_age_fdm_summary.csv
TODO_FROM_SCRIPT_OUTPUT: observations/sparc/results/sparc_mass_bin_summary.csv
TODO_FROM_SCRIPT_OUTPUT: observations/sparc/results/sparc_bootstrap_summary.csv
TODO_FROM_SCRIPT_OUTPUT: observations/sparc/results/sparc_memory_fit_parameters.csv
```

---

## 1. Introduction

Galaxy rotation curves remain a central motivation for dark matter and for tests of alternative or complementary gravitational phenomenology. Standard rotation-curve analyses compare observed circular velocities with the contributions expected from baryonic components. This draft asks a narrower empirical question:

> Do older stellar populations in SPARC galaxies show a reproducible, statistically modest association with inferred outer dark-matter fraction?

Within SoCT, such an association would be treated as a possible consistency check for a memory-field hypothesis: if apparent gravitational excess partly reflects accumulated collapse or dynamical history, older systems may show stronger apparent outer-region discrepancy than younger systems, all else equal.

This manuscript is deliberately conservative. The present draft is a correlation test and reproducibility scaffold, not evidence sufficient to establish a new gravitational theory.

---

## 2. Theoretical Prediction

### 2.1 SoCT Age--Dark-Matter Relation

A minimal working form from the imported scaffold is:

```text
f_DM(r > r_half) = f_0 + alpha * log(t_age / t_0) + epsilon(M_*)
```

where:

- `f_0` is a baseline dark-matter-fraction term;
- `alpha > 0` is the predicted memory-accumulation coefficient in this toy parameterization;
- `t_0` is a reference age;
- `epsilon(M_*)` is a mass-dependent residual or structural term.

Null hypothesis:

```text
alpha = 0
```

The committed reproducibility script uses an additional exploratory nonlinear memory form:

```math
f_{DM}(t) = f_0 + A_{mem}\left(1 - e^{-t/\tau}\right)
```

`TODO_FROM_SCRIPT_OUTPUT`: fill `f_0`, `A_mem`, `tau`, `rmse`, and fit method from `observations/sparc/results/sparc_memory_fit_parameters.csv` after running `notebooks/sparc/sparc_age_dm_analysis.py`.

This model is exploratory. Its fitted parameters should not be presented as validated physical constants unless the model is preregistered, audited, and replicated.

---

## 3. Data and Sample

### 3.1 SPARC Dataset

SPARC provides high-quality rotation curves and photometric data for late-type galaxies. The repository's canonical derived table for this draft is:

```text
data/sparc/sparc_age_fdm_data.csv
```

`TODO_FROM_SCRIPT_OUTPUT`: fill final row count `N` from the `N` row in `observations/sparc/results/sparc_age_fdm_summary.csv`, not from hand-entered draft text.

### 3.2 Sample Selection

Current draft placeholders:

- Quality flag: Q <= 2.
- Inclination: i > 30 degrees.
- Rotation curve points beyond half-light radius.
- Available age proxy.

Final sample-selection values must be verified against the committed derived table and analysis script before submission.

### 3.3 Age Proxy

Placeholder:

```text
Age proxy source and construction method must be specified before submission.
```

Known limitation: the current repository notes that age values may mix literature ages and proxy-derived ages. This is a dominant source of interpretive uncertainty and must remain explicit in any PRELIMINARY claim.

### 3.4 Outer Dark-Matter Fraction

Working definition from the imported scaffold:

```text
f_DM = (M_total(r_out) - M_baryon(r_out)) / M_total(r_out)
```

Equivalent velocity-space estimate used in repository materials:

```text
f_DM = 1 - (V_bary / V_obs)^2
```

Final manuscript must specify whether this is evaluated at the last measured radius, beyond `r_half`, or over a radial window.

---

## 4. Analysis and Results

All numerical results in this section are placeholders until regenerated from:

```bash
python notebooks/sparc/sparc_age_dm_analysis.py
```

The script declares the following output files as canonical for this draft:

```text
observations/sparc/results/sparc_age_fdm_summary.csv
observations/sparc/results/sparc_mass_bin_summary.csv
observations/sparc/results/sparc_bootstrap_summary.csv
observations/sparc/results/sparc_memory_fit_parameters.csv
figures/sparc/sparc_age_fdm_scatter.png
figures/sparc/sparc_memory_fit.png
figures/sparc/sparc_mass_bins.png
```

### 4.1 Primary Correlation

`TODO_FROM_SCRIPT_OUTPUT`: insert from `observations/sparc/results/sparc_age_fdm_summary.csv`:

```text
N = TODO_FROM_SCRIPT_OUTPUT
Pearson(age_best, fdm_outer_mean): r = TODO_FROM_SCRIPT_OUTPUT, p = TODO_FROM_SCRIPT_OUTPUT
Spearman(age_best, fdm_outer_mean): rho = TODO_FROM_SCRIPT_OUTPUT, p = TODO_FROM_SCRIPT_OUTPUT
```

Interpretation boundary:

> If positive after audited rerun, this result should be described only as a preliminary empirical association between age proxy and inferred outer dark-matter fraction in the derived SPARC table.

### 4.2 Mass and Structural Controls

`TODO_FROM_SCRIPT_OUTPUT`: insert from `observations/sparc/results/sparc_age_fdm_summary.csv`:

```text
Pearson(mass_proxy, fdm_outer_mean): r = TODO_FROM_SCRIPT_OUTPUT, p = TODO_FROM_SCRIPT_OUTPUT
Spearman(mass_proxy, fdm_outer_mean): rho = TODO_FROM_SCRIPT_OUTPUT, p = TODO_FROM_SCRIPT_OUTPUT
Partial Spearman(age, fdm | mass_proxy): rho_partial = TODO_FROM_SCRIPT_OUTPUT, p = TODO_FROM_SCRIPT_OUTPUT
```

The manuscript must explicitly distinguish:

- independent age effect;
- structural mediation;
- structural confounding.

Do not claim that mass or structural controls eliminate conventional explanations unless a dedicated sensitivity analysis supports that claim.

### 4.3 Bootstrap Validation

Placeholder:

```text
Insert bootstrap distribution, number of seeds, 95% confidence interval, and seed list after code is committed.
```

`TODO_FROM_SCRIPT_OUTPUT`: insert from `observations/sparc/results/sparc_bootstrap_summary.csv`:

```text
n_bootstrap = TODO_FROM_SCRIPT_OUTPUT
pearson_r_mean = TODO_FROM_SCRIPT_OUTPUT
pearson_r_95_percent_interval = [TODO_FROM_SCRIPT_OUTPUT, TODO_FROM_SCRIPT_OUTPUT]
spearman_r_mean = TODO_FROM_SCRIPT_OUTPUT
spearman_r_95_percent_interval = [TODO_FROM_SCRIPT_OUTPUT, TODO_FROM_SCRIPT_OUTPUT]
fraction_pearson_positive = TODO_FROM_SCRIPT_OUTPUT
fraction_spearman_positive = TODO_FROM_SCRIPT_OUTPUT
```

### 4.4 Out-of-Sample Validation

Placeholder:

```text
Insert 70/30 train-test split result after locked random seed is chosen and committed.
```

This validation is not produced by `notebooks/sparc/sparc_age_dm_analysis.py` as currently described. If used, it requires a separate committed script or extension to the reproducibility workflow.

### 4.5 Subgroup / Mass-Bin Analysis

`TODO_FROM_SCRIPT_OUTPUT`: replace the table below from `observations/sparc/results/sparc_mass_bin_summary.csv`.

| Mass Bin | n | Mass Proxy Range | Age Range | Pearson r | Pearson p | Spearman rho | Spearman p |
|---|---:|---|---|---:|---:|---:|---:|
| TODO_FROM_SCRIPT_OUTPUT | TODO_FROM_SCRIPT_OUTPUT | TODO_FROM_SCRIPT_OUTPUT | TODO_FROM_SCRIPT_OUTPUT | TODO_FROM_SCRIPT_OUTPUT | TODO_FROM_SCRIPT_OUTPUT | TODO_FROM_SCRIPT_OUTPUT | TODO_FROM_SCRIPT_OUTPUT |
| TODO_FROM_SCRIPT_OUTPUT | TODO_FROM_SCRIPT_OUTPUT | TODO_FROM_SCRIPT_OUTPUT | TODO_FROM_SCRIPT_OUTPUT | TODO_FROM_SCRIPT_OUTPUT | TODO_FROM_SCRIPT_OUTPUT | TODO_FROM_SCRIPT_OUTPUT | TODO_FROM_SCRIPT_OUTPUT |
| TODO_FROM_SCRIPT_OUTPUT | TODO_FROM_SCRIPT_OUTPUT | TODO_FROM_SCRIPT_OUTPUT | TODO_FROM_SCRIPT_OUTPUT | TODO_FROM_SCRIPT_OUTPUT | TODO_FROM_SCRIPT_OUTPUT | TODO_FROM_SCRIPT_OUTPUT | TODO_FROM_SCRIPT_OUTPUT |

Interpretation boundary:

> Any mass-bin trend should be described as preliminary until bin boundaries, outlier sensitivity, and selection effects are audited.

### 4.6 Figures

`TODO_FROM_SCRIPT_OUTPUT`: generate and reference the following after rerunning the script:

```text
figures/sparc/sparc_age_fdm_scatter.png
figures/sparc/sparc_memory_fit.png
figures/sparc/sparc_mass_bins.png
```

---

## 5. Systematic Uncertainties

### 5.1 Rotation-Curve Systematics

Required checks:

- Q=1 only;
- inclination >45 degrees;
- alternate `r_out` definitions;
- last-point sensitivity;
- baryonic mass-to-light ratio assumptions.

### 5.2 Age-Proxy Systematics

Required checks:

- uncertainty perturbation;
- alternate age proxy;
- color-based vs literature-derived ages;
- metallicity and star-formation-history dependence.

### 5.3 Selection Effects

Required checks:

- mass-range completeness;
- low-surface-brightness representation;
- environmental membership;
- distance/inclination correlation with age proxy.

---

## 6. Discussion

### 6.1 Conservative Interpretation

The maximum allowed current claim is:

> In the derived SPARC age--outer-fDM table, there may be a modest positive association between best-estimate stellar age and inferred outer dark-matter fraction, pending audited rerun and independent validation.

### 6.2 Consistency With SoCT

If the script output confirms a positive age--fDM association after audit, the result may be described as consistent with the SoCT prediction that memory-field effects could accumulate over time and become more visible in outer galactic regions. This phrasing is intentionally limited: consistency is not confirmation.

### 6.3 Alternative Explanations

The current result does not rule out conventional explanations.

Alternatives to address:

1. baryonic feedback;
2. adiabatic contraction;
3. environment and tidal stripping;
4. halo assembly bias;
5. stellar population age-proxy bias;
6. SPARC selection effects.

### 6.4 Relation to Other Dark-Matter Anomalies

Potential future links:

- Radial Acceleration Relation;
- core-cusp problem;
- high-redshift declining rotation curves;
- CMB directional memory / CIH.

These links should remain speculative unless separately quantified.

---

## 7. Conclusion

This PRELIMINARY working draft records a theory-motivated correlation test between stellar-population age proxies and inferred outer dark-matter fraction in the SPARC dataset. Numerical claims remain `TODO_FROM_SCRIPT_OUTPUT` placeholders until regenerated from the committed script and archived outputs. The draft does not establish memory gravity, does not replace dark matter, and does not eliminate standard astrophysical explanations.

---

## Required Before Submission

- [ ] OSF DOI inserted.
- [ ] Derived CSV committed and provenance documented.
- [ ] Analysis code committed and rerun.
- [ ] `TODO_FROM_SCRIPT_OUTPUT` values replaced only from script-generated output tables.
- [ ] Figures generated from code.
- [ ] p-values independently checked.
- [ ] Age proxy source documented.
- [ ] Environmental confounds addressed or explicitly deferred.
- [ ] Sensitivity checks completed for rotation-curve quality, inclination, and age-proxy uncertainties.
- [ ] Direct quotes and references verified.

---

## Claim Boundary

Status label:

```text
PRELIMINARY
```

Allowed language:

- "consistent with gravitational-memory predictions";
- "preliminary empirical correlation";
- "requires independent validation";
- "does not establish mechanism".

Avoid:

- "confirmed memory gravity";
- "proof of SoCT";
- "dark matter replacement demonstrated";
- "publication-ready detection".

---

## References Placeholder

- Bosma 1981.
- Lelli, McGaugh & Schombert 2016.
- McGaugh, Lelli & Schombert 2016.
- Milgrom 1983.
- Rubin & Ford 1970.
- Verlinde 2016.
- Shephard OSF preregistration.
- Additional sources for age proxies and high-redshift rotation curves.
