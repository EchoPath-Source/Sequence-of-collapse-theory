# Pantheon+ Environment Labels — Void-Catalog Cross-Match Methodology

**Status:** documented derived-label pipeline / preliminary

## Purpose

This document defines the conservative first-pass method for generating `data/pantheon/environment_labels.csv` from Pantheon+ supernova sky positions and redshifts using an external public SDSS void catalog.

The labels are **not** official Pantheon+ labels. They are a derived cross-match artifact for the P5 environment-dependent H0 test.

## Inputs

Required runtime inputs, kept outside normal git commits unless storage and redistribution policy is cleared:

```text
data/pantheon/raw/Pantheon+SH0ES.dat
data/pantheon/external/void_catalog_2014.06.18_just_sdss.tar.gz
```

The Pantheon+ table supplies row order, `CID`, `IDSURVEY`, `RA`, `DEC`, `zHD`, and `zCMB`. The SDSS void catalog supplies void-center sky positions, redshifts, radii, and sample redshift coverage.

## Output

```text
data/pantheon/environment_labels.csv
```

Required output columns:

```text
row_index,CID,IDSURVEY,RA,DEC,zHD,zCMB,environment_label,environment_method,catalog_source,nearest_void_id,nearest_void_sample,nearest_void_distance_mpc_h,nearest_void_radius_mpc_h,void_distance_over_radius,coverage_flag,notes
```

`row_index` must preserve the original Pantheon+SH0ES row order so labels can be joined back to the covariance-aligned SN table without reordering.

## Conservative label set

| Label | Meaning |
|---|---|
| `void` | SN falls inside the nearest catalog void effective radius. |
| `near_void_edge` | SN is outside the void radius but within a conservative edge buffer. |
| `sdss_nonvoid` | SN is inside SDSS redshift coverage but not near a catalog void center. |
| `outside_catalog_coverage` | SN is outside the usable SDSS void-catalog redshift/sky coverage or has invalid coordinates. |

Do not relabel `sdss_nonvoid` as `filament` unless a true filament/cosmic-web catalog is added. A void catalog supports void/not-void classification, not full void/sheet/filament/node classification.

## Claim boundary

These labels are acceptable for a preliminary pipeline and smoke test of the Pantheon+ environment-H0 workflow. They are not publication-grade cosmic-web classifications until validated against a documented external filament/cosmic-web catalog and an independent reproducibility run.
