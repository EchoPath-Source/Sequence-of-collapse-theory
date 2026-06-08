# SPARC Outer Mass Discrepancy Analysis

**Status:** preliminary observational result / candidate empirical artifact  
**Dataset:** SPARC / Rotmod LTG sample  
**Sample size:** N = 175 galaxies  
**Metric:** `fdm_outer` = apparent dark-matter fraction proxy, computed as the mean of the last three rotation-curve radii  
**Claim level:** exploratory; not proof of SoCT

## Summary

This note preserves the outer mass-discrepancy result used in the Sequence of Collapse Theory (SoCT) / gravitational-memory track. The result is useful because it asks whether central baryonic brightness alone explains the apparent dark residual in the outer rotation curve.

The conservative conclusion is:

> Central baryonic brightness alone does not strongly predict the outer apparent dark residual. This leaves environment, formation history, halo assembly, and memory-field interpretations as open competing explanations.

## Distribution of outer apparent dark fraction

```text
Mean fdm_outer:    0.700 ± 0.189
Median fdm_outer:  0.754
Range:             [0.043, 0.927]
Q1:                0.658
Q2:                0.754
Q3:                0.828
Skewness:         -1.709
Kurtosis:          2.800
```

## Bimodality / population structure

```text
DM-dominated outer regions (fdm_outer > 0.7):       111 / 175 = 63.4%
Baryon-dominated outer regions (fdm_outer < 0.3):    10 / 175 = 5.7%
Intermediate (0.3 <= fdm_outer <= 0.7):              54 / 175 = 30.9%
```

Interpretation:

- The sample is strongly skewed toward dark-residual-dominated outer regions.
- A small but non-negligible baryon-dominated outer population exists.
- This supports a two-channel interpretation: most systems retain strong outer residuals, while a minority appear baryon-dominated or strongly feedback/structure-modified.

## Correlations with baryonic / curve properties

```text
fdm_outer vs SB0_disk:   r = -0.093, p = 0.223   not significant
fdm_outer vs Vmax:       r = +0.034, p = 0.657   not significant
fdm_outer vs Rmax:       r = +0.168, p = 0.026   weak but significant
```

Interpretation:

- The relationship with central disk surface brightness is weak and non-significant.
- The relationship with maximum velocity is essentially absent.
- The relationship with curve extent is weak but significant.
- Outer residuals are not simply predicted by central disk brightness.

## Brightness-stratified comparison

```text
SB0 Quartile 1 (faintest):   0.723  (n = 44)
SB0 Quartile 2:              0.721  (n = 44)
SB0 Quartile 3:              0.687  (n = 43)
SB0 Quartile 4 (brightest):  0.667  (n = 44)

Delta(Q1 - Q4):              +0.056
```

Faint galaxies show slightly higher outer apparent dark fractions, but the effect is weak.

## Extreme cases

```text
Top 10 fdm_outer galaxies:
  Mean fdm_outer:      0.904
  Mean SB0_disk:       354.7 L_sun/pc^2
  Mean Vmax:            86.5 km/s

Bottom 10 fdm_outer galaxies:
  Mean fdm_outer:      0.145
  Mean SB0_disk:       214.7 L_sun/pc^2
  Mean Vmax:            63.7 km/s
```

The low-residual population is rare. It may reflect systems where central baryonic content, feedback history, or local formation conditions strongly suppress the outer residual.

## SoCT interpretation

This result is consistent with, but does not prove, the SoCT expectation that outer regions are less dominated by central baryonic modeling and may better preserve environment/history-dependent structure.

Conservative interpretation:

> The weak relationship between central surface brightness and outer apparent dark fraction suggests that central baryonic brightness alone is insufficient to explain the outer mass discrepancy. The next test is whether outer residuals correlate with formation-history proxies, local density, or cosmic-web environment more strongly than inner residuals.

## Next validation steps

1. Compute inner and outer apparent dark fractions using half-radius and effective-radius splits.
2. Compare formation-history proxy correlations in inner vs outer regions.
3. Cross-match with cosmic-web classifications such as void, sheet, filament, and cluster.
4. Test local density within 1–5 Mpc.
5. Cross-match with HI deficiency and group environment proxies.
6. Preserve null or confounded results explicitly.

## Status boundary

This artifact is not proof of SoCT. It is a preliminary empirical support note showing that the outer mass discrepancy is not strongly explained by central disk surface brightness alone.
