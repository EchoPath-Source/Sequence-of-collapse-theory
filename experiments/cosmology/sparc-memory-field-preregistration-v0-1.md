# Pre-Registration: Age-Dependent Galactic Rotation Curves as Test of Memory Field Gravity

**Author:** Antoine L. Shephard (Echo Mirrowen)  
**Affiliation:** Echo Labs, New York  
**Date:** March 2026  
**Document Type:** Pre-Registered Study Protocol  
**Registration Date:** To be assigned by OSF  
**Status:** Pre-data analysis  
**Source files:** `SOC_Paper1_OSF_PreReg.md`, `SOC_PreReg_Draft-3.docx`

---

## Abstract

Recent high-redshift galaxy work suggests that some early massive galaxies are baryon-dominated and show declining rotation curves, while standard dark-matter simulations may fail to reproduce that behavior. The Sequence of Collapse Theory / memory-field framework interprets this as a possible sign that apparent dark-matter-like gravitational effects accumulate over cosmic time.

This preregistration defines a quantitative SPARC-based test:

> rotation curve shape should correlate with galaxy age in a specific functional form, with a characteristic memory decay timescale tau extractable from the data.

The aim is to establish falsifiable predictions before analysis and identify what observations would weaken or refute the framework.

---

## 1. Core Hypothesis

### 1.1 Memory Field Gravity Claim

Spacetime accumulates a memory field from collapse events, including particle interactions, stellar processes, supernovae, and other energy-concentrating events. This accumulated memory contributes to the effective gravitational potential.

### 1.2 Key Prediction

Older galaxies have accumulated more collapse history and therefore should show stronger memory-field contributions to gravity.

Young galaxies, especially high-redshift galaxies, have less collapse history and should appear more baryon-dominated.

---

## 2. Theoretical Framework

The standard Hamiltonian is extended with a memory coupling term:

```text
H_SOC = p^2 / 2m + V(x) + lambda * integral sum_i w_i K(|x - x_i|, t - t_i) d_tau
```

Where:

- `p^2 / 2m + V(x)` is the standard kinetic and potential energy term;
- `lambda` is the memory-field coupling constant;
- `w_i` is the weight of collapse event `i`;
- `K` is the memory kernel describing spatial and temporal decay;
- the integral is over past proper time.

Candidate memory kernel:

```text
K(r, tau) = A * exp(-r / lambda_s) * exp(-tau / tau_decay) * cos(omega * tau)
```

Where `tau_decay` is the key parameter to extract.

---

## 3. Application to Galactic Rotation Curves

Observed rotation velocity is decomposed as:

```text
v^2(r) = v_baryonic^2(r) + v_memory^2(r)
```

With a memory contribution of the form:

```text
v_memory^2(r) proportional to lambda_G * M_history(r) * tau_decay^-1 * f(r / r_core)
```

Critical prediction:

```text
M_history(r) scales with galaxy age.
```

Therefore:

1. rotation curve flatness increases with galaxy age;
2. the relationship has a characteristic timescale;
3. preliminary target timescale: `tau_decay ~ 3-5 Gyr`.

---

## 4. Primary Prediction

### Age-Dependent Rotation Curve Shape

The ratio of outer-to-inner rotation velocity should increase with galaxy age according to:

```text
v(r_out) / v(r_in) = R_0 + Delta_R * [1 - exp(-t_age / tau_decay)]
```

Where:

- `R_0 ~ 0.6-0.8` is the approximate baryon-only ratio;
- `Delta_R ~ 0.2-0.3` is the proposed memory contribution;
- `tau_decay ~ 3-5 Gyr` is the predicted memory timescale to be extracted from the data.

---

## 5. Secondary Predictions

### Prediction 2a

Galaxies with similar stellar mass but different ages should show different rotation curve shapes, with older galaxies showing flatter curves.

### Prediction 2b

The memory timescale `tau_decay` should be approximately universal across galaxy types to within about ±20%, if the same memory kernel governs all systems.

### Prediction 2c

Rotation curve residuals should correlate more strongly with age than with other galaxy properties after controlling for stellar mass, gas fraction, morphology, and surface brightness.

---

## 6. Null Hypothesis

```text
H0: Rotation curve shape shows no systematic correlation with galaxy age after controlling for stellar mass, gas fraction, and morphology.
```

If this null cannot be rejected at the preregistered threshold, the memory-field framework is weakened or falsified for galactic-scale phenomena in this formulation.

---

## 7. Data Source

### SPARC Database

Dataset:

```text
Spitzer Photometry and Accurate Rotation Curves (SPARC)
```

Primary contents:

- 175 disk galaxies;
- high-quality rotation curves;
- stellar mass surface density;
- gas surface density;
- distance;
- inclination;
- morphology.

Variables required but not contained directly in SPARC:

- stellar population age estimates;
- cross-match target catalogs such as SDSS, GAMA, or literature SED-fitting sources.

---

## 8. Sample Selection Criteria

### Inclusion Criteria

1. High-quality rotation curve.
2. Stellar population age estimate available from literature or cross-match.
3. Inclination greater than 30 degrees.
4. Distance less than 100 Mpc.

### Exclusion Criteria

1. Ongoing major merger or strong morphological disturbance.
2. AGN-dominated system that compromises stellar age estimates.
3. Significant non-circular motions such as extreme bars or warps.

Expected final sample:

```text
N ~ 80-120 galaxies
```

---

## 9. Analysis Protocol

### Step 1: Rotation Curve Characterization

For each galaxy compute:

```text
v_in  = median rotation velocity at r < 0.5 R_eff
v_out = median rotation velocity at 2.0 < r/R_eff < 3.0
F     = v_out / v_in
```

Where `F` is the flatness ratio.

### Step 2: Baryonic Model Subtraction

Compute expected baryonic rotation curve:

```text
v_bary^2(r) = G [M_*(r) + M_gas(r)] / r
```

Extract residual:

```text
v_residual^2(r) = v_obs^2(r) - v_bary^2(r)
```

### Step 3: Age Correlation

Test:

- `F` vs `t_age`;
- `v_residual^2(r_out)` vs `t_age`.

### Step 4: Timescale Extraction

Fit:

```text
F(t_age) = F_0 + Delta_F * [1 - exp(-t_age / tau_decay)]
```

Extract `tau_decay` with confidence intervals.

---

## 10. Statistical Tests

### Primary Test

Spearman rank correlation between flatness ratio `F` and stellar population age `t_age`.

Preregistered threshold:

```text
p < 0.05, two-tailed
```

### Secondary Test

Linear or generalized regression:

```text
v_residual^2 ~ t_age
```

Threshold:

```text
slope significantly different from zero at p < 0.05
```

### Timescale Extraction

Use non-linear least squares with bootstrapped errors.

Bootstrap target:

```text
1000 iterations
```

---

## 11. Control Variables

Run multivariate regressions including:

- stellar mass `log M_*`;
- gas fraction `M_gas / M_*`;
- morphological type;
- central surface brightness or stellar surface density;
- distance and inclination diagnostics where relevant.

Critical test:

> Does age explain significant variance beyond these controls?

---

## 12. Predicted Outcomes

### If Memory-Field Framework Is Correct

Expected results:

```text
Spearman rho(F, t_age) > 0.4
p < 0.001
tau_decay = 3.5 +/- 1.0 Gyr
age explains >=30% of variance in rotation-curve residuals
relationship holds across galaxy types
```

Interpretation:

> Memory-field accumulation produces age-dependent gravity. Dark-matter phenomenology may emerge from spacetime memory rather than exotic particles.

### If Memory-Field Framework Is Incorrect

Expected null results:

```text
rho(F, t_age) < 0.2
p > 0.10
age contributes <5% of variance after controlling for mass
no universal timescale extractable
```

Interpretation:

> Rotation curves are determined by current mass distribution and standard predictors only. The proposed galactic-scale memory contribution is falsified or strongly weakened.

### Intermediate Outcomes

Weak correlation:

```text
0.2 < rho < 0.3
```

Interpretation: possible subdominant effect or need to reformulate coupling strength.

Wrong timescale:

```text
tau_decay >> 10 Gyr or tau_decay << 1 Gyr
```

Interpretation: basic mechanism may require revision of the memory kernel.

---

## 13. Timeline and Resources

### Phase 1: Data Compilation

Weeks 1-4:

- download SPARC database;
- cross-match with age catalogs;
- apply selection criteria;
- generate final sample table.

### Phase 2: Analysis

Weeks 5-8:

- compute rotation metrics;
- perform correlation analysis;
- fit timescale model;
- run control regressions.

### Phase 3: Manuscript Preparation

Weeks 9-12:

- write manuscript;
- create figures;
- perform robustness checks;
- prepare supplementary materials.

Estimated direct cost:

```text
$0 for public-data analysis, excluding time/collaboration costs.
```

---

## 14. Pre-Registration Commitment

Before analyzing SPARC data, this study commits to:

1. specific predictions;
2. statistical tests;
3. falsification criteria;
4. analysis protocol;
5. public analysis code;
6. publication of null results.

Prohibited actions:

- changing predictions after seeing data;
- p-hacking by trying multiple methods until a result appears;
- selective reporting;
- adding post-hoc explanations as confirmatory claims.

---

## 15. Expected Figure Gallery

Pre-specified figures:

1. rotation curves for young vs old galaxies;
2. flatness ratio vs galaxy age with exponential fit;
3. rotation-curve residuals vs age, color-coded by stellar mass;
4. memory-field contribution to velocity as a function of radius for different galaxy ages.

---

## 16. Planned Analysis Repository Structure

```text
/sparc-memory-analysis
  /data
  /scripts
    01_download_data.py
    02_compute_rotation_metrics.py
    03_age_correlation.py
    04_timescale_fit.py
    05_generate_figures.py
  /results
  README.md
```

---

## 17. Relationship to Broader SoCT Tests

This is the proposed P1 empirical anchor.

Complementary tracks:

- Pantheon+ environment-dependent H0 test;
- PNT two-timescale dark-energy / Hubble-window paper;
- SOC-MZI consciousness-coupled visibility test;
- CIH / CMB directional-memory analysis.

---

## 18. Current Boundary

This preregistration is a research draft. It should be checked against the final available SPARC data products, age cross-match feasibility, and citation details before OSF submission.

Any direct quote from Nelson et al. or Genzel et al. must be verified against the original paper before public release.
