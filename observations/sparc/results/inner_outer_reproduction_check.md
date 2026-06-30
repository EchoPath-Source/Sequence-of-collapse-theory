# SPARC Inner/Outer Radial-Decomposition Reproduction Check

**Status:** PASS  
**Claim level:** candidate empirical result / reproducibility support  
**Input dataset:** `observations/sparc/data/sparc_wise_inner_outer_fdm_split.csv`  
**Expected table:** `observations/sparc/results/inner_outer_correlation_summary.csv`  
**Regenerated table:** `observations/sparc/results/inner_outer_correlation_summary_regenerated.csv`

## What this checks

This reproduction script recalculates Pearson and Spearman correlations between `gW1` and each inner/outer apparent dark-fraction metric across four subsets:

```text
All
Q=1
Disk
Disk+Q=1
```

It then compares the regenerated table against the committed reference table.

## Comparison result

| Field | Value |
|---|---:|
| matched | `True` |
| tolerance | `1e-12` |
| max_abs_diff | `9.4368957093138306e-16` |
| compared_numeric_cells | `120` |
| missing_rows | `0` |
| extra_rows | `0` |

## Interpretation

Use:

> The radial-decomposition correlation table can be regenerated from the committed derived radial-split dataset, subject to the comparison status above.

Avoid:

> This reproduction check proves SoCT, proves gravity is memory, or rules out conventional halo/assembly explanations.

## Remaining scientific controls

Even if this check passes, publication-grade use still requires:

1. source/provenance notes for the radial-split dataset;
2. controls for stellar mass, gas fraction, morphology, surface brightness, curve quality, and environment;
3. bootstrap, jackknife, and outlier/leverage diagnostics;
4. independent replication or adversarial review.
