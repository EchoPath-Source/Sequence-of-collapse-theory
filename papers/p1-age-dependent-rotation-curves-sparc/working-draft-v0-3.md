# Age-Dependent Rotation-Curve Discrepancy in SPARC Galaxies

**Subtitle:** A PRELIMINARY, hypothesis-generating SPARC test for age-associated outer rotation-curve discrepancy  
**Author:** Antoine L. Shephard (Echo Mirrowen)  
**Affiliation:** Echo Labs Field Harmonics Institute  
**Correspondence:** contact@echopathxr.com  
**Status:** PRELIMINARY submission-candidate working draft v0.3  
**Canonical script:** `papers/p1-age-dependent-rotation-curves-sparc/analysis/sparc_age_fdm_analysis.py`  
**Canonical derived data:** `data/sparc/sparc_age_fdm_data.csv`  
**Claim boundary:** This draft is hypothesis-generating. It does not prove Sequence of Collapse Theory (SoCT), memory gravity, dark-matter replacement, or any nonstandard gravitational mechanism.

---

## Abstract

We test whether the derived SPARC quantity `fdm_outer_mean`, an outer rotation-curve discrepancy / dark-matter-fraction proxy, is associated with the stellar-population age proxy `age_best`. In the current derived table (`N = 175`), the marginal age--fDM association is modest and positive: Pearson `r = 0.200943`, `p = 0.007666`, and Spearman `rho = 0.211441`, `p = 0.004971`. However, the key submission-candidate result is the attenuation under structural controls. In the full OLS structural-control model,

```text
fdm_outer_mean ~ age_best + logVmax + logRmax + logSB0
```

the age coefficient is `beta_age = 0.018406`, `SE = 0.013111`, `t = 1.403873`, and `p_age = 0.162181`. The corresponding full structural-control partial correlation controlling `logVmax + logRmax + logSB0` is `partial_r = 0.107053`, `p = 0.158513`. We therefore treat the result as a preliminary empirical pattern that motivates follow-up, not as a confirmed physical detection.

---

## 1. Research Question

Do older SPARC galaxies, as represented by the repository's `age_best` proxy, show larger inferred outer rotation-curve discrepancy (`fdm_outer_mean`) than younger SPARC galaxies?

The question is intentionally empirical. The SoCT/memory-gravity motivation is treated as a source of hypotheses, not as an inference licensed by the present data alone.

---

## 2. Data and Variables

The analysis uses:

```text
data/sparc/sparc_age_fdm_data.csv
```

Required columns in the current script are:

- `galaxy`;
- `fdm_outer_mean`;
- `age_best`;
- `SB0_disk_Lpc2`;
- `Vmax_kms`;
- `Rmax_kpc`.

The script constructs structural controls:

```text
logVmax = log10(Vmax_kms)
logRmax = log10(Rmax_kpc)
logSB0  = log10(SB0_disk_Lpc2)
```

The current analysis should not be interpreted without a dedicated age-proxy provenance audit, outlier analysis, and selection-function review.

---

## 3. Methods

Run from the repository root:

```bash
python papers/p1-age-dependent-rotation-curves-sparc/analysis/sparc_age_fdm_analysis.py
```

The script regenerates these committed CSV outputs:

```text
papers/p1-age-dependent-rotation-curves-sparc/results/SPARC_age_fdm_correlations.csv
papers/p1-age-dependent-rotation-curves-sparc/results/SPARC_age_fdm_partial_correlations.csv
papers/p1-age-dependent-rotation-curves-sparc/results/SPARC_age_fdm_regression_models.csv
papers/p1-age-dependent-rotation-curves-sparc/results/SPARC_age_fdm_binned_bootstrap.csv
```

The script also generates `SPARC_age_vs_fdm_scatter.png`. That plot is intentionally not committed in this pass because binary artifacts are handled separately.

---

## 4. Results

### 4.1 Marginal age--fDM association

| Test | N | Statistic | p-value |
|---|---:|---:|---:|
| Pearson(`age_best`, `fdm_outer_mean`) | 175 | 0.200943 | 0.007666 |
| Spearman(`age_best`, `fdm_outer_mean`) | 175 | 0.211441 | 0.004971 |

These marginal associations are positive but modest.

### 4.2 Partial correlations with structural controls

| Control set | N | partial r | p-value |
|---|---:|---:|---:|
| `logVmax` | 175 | 0.289127 | 0.000104 |
| `logRmax` | 175 | 0.222749 | 0.003048 |
| `logSB0` | 175 | 0.155467 | 0.039937 |
| `logVmax + logRmax` | 175 | 0.264475 | 0.000405 |
| `logVmax + logRmax + logSB0` | 175 | 0.107053 | 0.158513 |

The full structural-control partial-correlation model is not conventionally significant at `p < 0.05`.

### 4.3 OLS age coefficient across control models

| Model | N | beta_age | SE | t | p_age |
|---|---:|---:|---:|---:|---:|
| `fdm ~ age_best` | 175 | 0.023842 | 0.008837 | 2.698028 | 0.007666 |
| `fdm ~ age_best + logVmax` | 175 | 0.037977 | 0.009588 | 3.961045 | 0.000109 |
| `fdm ~ age_best + logRmax` | 175 | 0.026149 | 0.008726 | 2.996607 | 0.003134 |
| `fdm ~ age_best + logVmax + logRmax` | 175 | 0.041343 | 0.011529 | 3.586148 | 0.000438 |
| `fdm ~ age_best + logVmax + logRmax + logSB0` | 175 | 0.018406 | 0.013111 | 1.403873 | 0.162181 |

The key interpretive point is attenuation in the full structural-control model: adding `logVmax`, `logRmax`, and `logSB0` attenuates the age coefficient to `p ≈ 0.162`.

### 4.4 Binned bootstrap by `logVmax`

| mass_bin | N | Pearson r | p-value | old-minus-young mean | 95% bootstrap CI |
|---|---:|---:|---:|---:|---:|
| lowV | 59 | 0.115486 | 0.383753 | 0.036491 | [-0.115511, 0.160084] |
| midV | 58 | 0.456372 | 0.000317 | 0.090419 | [0.015351, 0.176680] |
| highV | 58 | 0.276598 | 0.035567 | 0.093290 | [0.013190, 0.170739] |

These bins are exploratory and should be rerun with outlier checks and preregistered binning rules before publication.

---

## 5. Interpretation

The current results support only this limited statement:

> In the repository's derived SPARC table, `age_best` shows a modest positive marginal association with `fdm_outer_mean`, but the association weakens after controlling simultaneously for `logVmax`, `logRmax`, and `logSB0`. This is a hypothesis-generating pattern requiring independent reproduction and astrophysical confound analysis.

The current results do **not** support any of the following stronger statements:

- SoCT is proven;
- memory gravity is proven;
- a nonstandard gravitational mechanism has been detected;
- dark matter has been replaced or falsified;
- SPARC confirms a collapse-memory field.

---

## 6. Required Follow-up Before Submission

- Audit age-proxy provenance and uncertainties.
- Define the primary control model before looking at inferential outcomes in future reruns.
- Test sensitivity to inclination, rotation-curve quality, baryonic mass-to-light assumptions, and outliers.
- Compare against conventional galaxy-formation expectations and assembly-history explanations.
- Document all binary figures through the repository's separate artifact process.
- Independently reproduce all p-values and confidence intervals.

---

## 7. Conclusion

This v0.3 working draft finalizes a conservative, text/CSV-only submission-candidate state for P1. The main empirical pattern is a modest marginal age--outer-fDM association in the derived SPARC table, paired with attenuation under the full structural-control model to `p ≈ 0.162`. The result is preliminary and hypothesis-generating; it does not prove SoCT, memory gravity, or any nonstandard gravitational mechanism.
