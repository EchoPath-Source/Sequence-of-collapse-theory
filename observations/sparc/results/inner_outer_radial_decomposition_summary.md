# SPARC Inner/Outer Radial Decomposition Summary

**Status:** candidate empirical result / radial-discriminator support  
**Dataset:** derived SPARC + WISE inner/outer apparent dark-fraction split  
**Primary derived dataset:** `observations/sparc/data/sparc_wise_inner_outer_fdm_split.csv`  
**Correlation table:** `observations/sparc/results/inner_outer_correlation_summary.csv`  
**Claim level:** preliminary; requires notebook reproduction and independent review

## Research question

Does the formation-history / stellar-population proxy correlate more strongly with the apparent dark residual in the outer rotation curve than in the inner, baryon-dominated region?

This is a key discriminator for the SoCT gravitational-memory track. If the signal is stronger in the outer region than the inner disk, it is less likely to be only an inner baryonic modeling artifact.

## Definition of apparent dark fraction

For each radius:

```text
f_DM(r) = 1 - (V_gas^2 + V_disk^2 + V_bulge^2) / V_obs^2
```

Derived metrics were computed by splitting each curve into inner and outer radial zones.

Two split definitions were used:

1. **Half-radius split:** inner and outer regions separated by half of the measured rotation-curve extent.
2. **Effective-radius split:** inner and outer regions separated using the effective-radius scale, which is often more physically meaningful for baryon-dominated disks.

## Formation-history proxy

The current proxy is:

```text
g - W1
```

This should be described carefully as a WISE/color stellar-population or formation-history proxy, not a direct cosmic age measurement.

## Key result: clean Disk + Q=1 subset

The cleanest subset removes low-quality curves and bulge contamination.

```text
Subset: Disk + Q=1
N = 56
```

### Half-radius split

| Metric | N | Spearman rho vs g-W1 | p-value |
|---|---:|---:|---:|
| Inner fDM | 56 | -0.553 | 9.79e-06 |
| Outer fDM | 56 | -0.657 | 3.71e-08 |

Result:

```text
|rho_outer| > |rho_inner|
```

The outer apparent dark residual has the stronger association with the formation-history proxy.

### Effective-radius split

| Metric | N | Spearman rho vs g-W1 | p-value |
|---|---:|---:|---:|
| Inner fDM | 56 | -0.409 | 1.77e-03 |
| Outer fDM | 56 | -0.637 | 1.31e-07 |

Result:

```text
|rho_outer| >> |rho_inner|
```

The effective-radius split gives the cleaner radial discriminator: the outer correlation is substantially stronger than the inner correlation.

## Headline interpretation

> In the clean disk-dominated, high-quality SPARC subset, the WISE color / formation-history proxy correlates more strongly with outer apparent dark residuals than inner residuals.

Conservative version:

> This strengthens the SPARC/P1 track from an age-DM candidate signal to a candidate signal with radial-discriminator support, pending committed notebook reproduction and external review.

## Why this matters for SoCT

The SoCT memory-field interpretation expects accumulated history/environment effects to become cleaner in the outer rotation curve, where central baryonic feedback and inner disk modeling are less dominant.

The result is therefore directionally consistent with the SoCT expectation:

```text
formation-history proxy association: outer > inner
```

This does not prove a memory field. It does show that the candidate signal is not confined to the inner baryonic disk.

## Conventional alternatives

The main standard explanations remain viable and must be tested:

- assembly bias,
- halo concentration,
- stellar-mass coupling,
- feedback history,
- gas fraction,
- morphology,
- local density / satellite environment,
- selection effects in the clean subset.

A publication-ready version must compare the SoCT interpretation against these conventional alternatives.

## Required next steps

1. Add a runnable notebook that regenerates the derived dataset and correlation table from documented inputs.
2. Add source links and citations for SPARC and WISE/color inputs.
3. Run controlled regressions with stellar mass, gas fraction, morphology, surface brightness, curve quality, and environment.
4. Cross-match with cosmic-web / local-density catalogs.
5. Test whether the outer association survives bootstrap, jackknife, and outlier removal.
6. Keep this result labeled as candidate empirical support until reproduced.

## Current bottom line

The inner/outer radial decomposition gives the SPARC track its strongest current discriminator:

> For the clean Disk + Q=1 subset, the formation-history proxy is more strongly associated with the outer apparent dark residual than with the inner residual, especially under the effective-radius split.
