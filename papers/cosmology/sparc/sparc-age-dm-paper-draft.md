# Galaxy Age Predicts Outer Dark Matter Fraction

**Subtitle:** Evidence for Temporally Accumulated Gravitational Memory in the SPARC Dataset  
**Author:** Antoine L. Shephard (Echo Mirrowen)  
**Affiliation:** Echo Labs Field Harmonics Institute  
**Correspondence:** [EMAIL PLACEHOLDER]  
**OSF Pre-registration:** [OSF DOI PLACEHOLDER]  
**Status:** Working manuscript draft scaffold based on `sparc_paper-1.docx`  
**Important boundary:** Numerical placeholders must be updated only from committed analysis code and data.

---

## Abstract Draft

We report a positive correlation between galaxy stellar age and inferred outer dark matter fraction in the SPARC galaxy dataset. Across galaxies with reliable age proxies and spatially resolved rotation curves, preliminary analysis finds a Pearson correlation of approximately `r ≈ +0.20` between mean stellar age and outer dark matter fraction. This correlation is in the direction predicted by the Sequence of Collapse Theory (SoCT): that dark matter phenomenology may reflect temporally accumulated gravitational memory, and that older galaxies, having experienced more collapse events, should exhibit stronger apparent dark matter signatures in their outer regions. We discuss alternative explanations, systematic uncertainties, and proposed follow-up tests.

---

## 1. Introduction

The nature of dark matter remains one of the central open problems in astrophysics. Galaxy rotation curves systematically exceed the predictions of Newtonian dynamics applied to observed baryonic mass, and this excess is typically attributed to extended halos of non-luminous matter.

Despite decades of direct-detection efforts, no dark matter particle has yet been identified. This motivates continued testing of alternative explanations, including modified gravity, emergent gravity, primordial black holes, and history-dependent gravitational frameworks.

SoCT proposes that apparent dark matter may arise partly from temporally accumulated gravitational memory: a field encoding the cumulative history of collapse events in a galaxy's past. Under this framework, older galaxies should exhibit stronger apparent dark matter signatures, especially in outer regions where baryonic self-gravity is weaker.

---

## 2. Theoretical Prediction

### 2.1 SoCT Age-Dark Matter Relation

Working form:

```text
f_DM(r > r_half) = f_0 + alpha * log(t_age / t_0) + epsilon(M_*)
```

Where:

- `f_0` is a baseline dark matter fraction;
- `alpha > 0` is the predicted memory-accumulation rate;
- `t_0` is a reference age;
- `epsilon(M_*)` is a mass-dependent residual.

Null hypothesis:

```text
alpha = 0
```

---

## 3. Data and Sample

### 3.1 SPARC Dataset

SPARC provides high-quality rotation curves and photometric data for 175 late-type galaxies.

### 3.2 Sample Selection

Current draft placeholders:

- Quality flag: Q <= 2.
- Inclination: i > 30 degrees.
- Rotation curve points beyond half-light radius.
- Available age proxy.

Final values must be filled from the committed analysis table.

### 3.3 Age Proxy

Placeholder:

```text
Age proxy source and construction method must be specified before submission.
```

### 3.4 Outer Dark Matter Fraction

Working definition:

```text
f_DM = (M_total(r_out) - M_baryon(r_out)) / M_total(r_out)
```

Equivalent velocity-space estimate used in summary:

```text
f_DM = 1 - (V_bary / V_obs)^2
```

Final manuscript must specify whether this is evaluated at the last measured radius, beyond `r_half`, or over a radial window.

---

## 4. Analysis and Results

### 4.1 Primary Correlation

Placeholder values from current summary:

```text
Pearson r ≈ +0.201
p ≈ 0.0077
N = 175
```

These values must be regenerated from committed arrays before final release.

### 4.2 Mass Control

Current report indicates partial correlations remain positive after controlling for structural parameters, with some weakening under the full structural model.

The manuscript must explicitly distinguish:

- independent age effect;
- structural mediation;
- structural confounding.

### 4.3 Bootstrap Validation

Placeholder:

```text
Insert bootstrap distribution, number of seeds, 95% confidence interval, and seed list after code is committed.
```

### 4.4 Out-of-Sample Validation

Placeholder:

```text
Insert 70/30 train-test split result after locked random seed is chosen and committed.
```

### 4.5 Subgroup Analysis

Mass-bin results from current summary:

| Mass Bin | n | r | p-value |
|---|---:|---:|---:|
| Low | 59 | +0.115 | 0.384 |
| Mid | 58 | +0.456 | 3.2e-4 |
| High | 58 | +0.277 | 0.036 |

Interpretation:

> The mid-mass bin appears to carry the strongest signal, but this must be checked for selection, outliers, and mass-bin boundary sensitivity.

---

## 5. Systematic Uncertainties

### 5.1 Rotation Curve Systematics

Required checks:

- Q=1 only;
- inclination >45 degrees;
- alternate `r_out` definitions;
- last-point sensitivity;
- baryonic mass-to-light ratio assumptions.

### 5.2 Age Proxy Systematics

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

### 6.1 Consistency With SoCT

The preliminary positive age-f_DM correlation is consistent with the SoCT prediction that memory-field effects should accumulate over time and become most visible in outer galactic regions.

### 6.2 Alternative Explanations

The current result does not rule out conventional explanations.

Alternatives to address:

1. baryonic feedback;
2. adiabatic contraction;
3. environment and tidal stripping;
4. halo assembly bias;
5. stellar population age proxy bias;
6. SPARC selection effects.

### 6.3 Relation to Other Dark Matter Anomalies

Potential future links:

- Radial Acceleration Relation;
- core-cusp problem;
- high-redshift declining rotation curves;
- CMB directional memory / CIH.

---

## 7. Conclusion

Current internal analysis reports a positive correlation between stellar age and outer dark matter fraction in the SPARC dataset. The result is in the preregistered direction predicted by SoCT, but it remains provisional until the derived dataset, analysis code, and sensitivity checks are committed and independently reproduced.

---

## Required Before Submission

- [ ] OSF DOI inserted.
- [ ] Email/correspondence inserted.
- [ ] Derived CSV committed.
- [ ] Analysis code committed.
- [ ] Figures generated from code.
- [ ] p-values independently checked.
- [ ] Age proxy source documented.
- [ ] Environmental confounds addressed or explicitly deferred.
- [ ] Direct quotes and references verified.

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
