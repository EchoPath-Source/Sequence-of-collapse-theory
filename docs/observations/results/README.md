# Observational results

This folder stores summary result tables generated from public-data tests of Sequence of Collapse predictions.

## Current files

### `sparc_inner_outer_correlation_summary.csv`
Summary statistics for the SPARC radial decomposition follow-up.

The analysis splits each SPARC rotation curve into inner and outer regions and checks whether the WISE color proxy `g-W1` correlates more strongly with apparent dark residuals in the outer region.

Main split definitions:
- Half-radius split: inner `r < Rmax/2`, outer `r >= Rmax/2`
- Effective-radius split: inner `r < Reff`, outer `r >= Reff`

Main residual definition:

`fDM(r) = 1 - (Vgas^2 + Vdisk^2 + Vbulge^2) / Vobs^2`

Key clean-subset result:
- Disk-dominated + SPARC `Q=1`
- Half-radius split: outer Spearman rho `-0.657`, inner Spearman rho `-0.553`
- Effective-radius split: outer Spearman rho `-0.637`, inner Spearman rho `-0.409`

Interpretation should remain conservative: this is evidence of structured radial dependence in the residual / color relationship, not proof of a specific physical mechanism.
