# Pantheon+ Environment Labels — Void + Filament Cross-Match Methodology

**Status:** documented derived-label pipeline / preliminary

## Purpose

This document defines the conservative method for generating `data/pantheon/environment_labels.csv` from Pantheon+ supernova sky positions and redshifts using external public SDSS large-scale-structure catalogs.

The labels are **not** official Pantheon+ labels. They are a derived cross-match artifact for the P5 environment-dependent H0 test.

## Inputs

Required runtime inputs, kept outside normal git commits unless storage and redistribution policy is cleared:

```text
data/pantheon/raw/Pantheon+SH0ES.dat
data/pantheon/external/void_catalog_2014.06.18_just_sdss/
data/pantheon/external/J_MNRAS_438_3465/
```

The Pantheon+ table supplies row order, `CID`, `IDSURVEY`, `RA`, `DEC`, `zHD`, and `zCMB`. The SDSS void catalog supplies void-center sky positions, redshifts, radii, and sample redshift coverage. The Tempel/Bisous SDSS filament catalog (`J/MNRAS/438/3465`) supplies filament spine-point comoving coordinates from `table2.dat(.gz)`.

## Scripts

Two scripts are available:

```text
notebooks/pantheon/generate_environment_labels_from_void_catalog.py
notebooks/pantheon/generate_environment_labels_from_void_filament_catalogs.py
```

The void-only script is retained for conservative smoke tests. The preferred route, when the Tempel/Bisous catalog is staged, is the void+filament script.

## Output

```text
data/pantheon/environment_labels.csv
```

Required output columns for the combined pipeline include:

```text
row_index,CID,IDSURVEY,RA,DEC,zHD,zCMB,environment_label,void_label,filament_label,environment_method,catalog_source,nearest_void_id,nearest_void_sample,nearest_void_distance_mpc_h,nearest_void_radius_mpc_h,void_distance_over_radius,nearest_filament_id,nearest_filament_point_id,nearest_filament_distance_mpc_h,coverage_flag,notes
```

`row_index` must preserve the original Pantheon+SH0ES row order so labels can be joined back to the covariance-aligned SN table without reordering.

## Conservative label set

| Label | Meaning |
|---|---|
| `void` | SN falls inside the nearest catalog void effective radius. |
| `near_void_edge` | SN is outside the void radius but within a conservative edge buffer. |
| `filament` | SN is within the Tempel/Bisous filament radius threshold of a filament spine point. |
| `near_filament` | SN is near, but not inside, the conservative filament threshold. |
| `field_or_wall` | SN is covered by the filament catalog but not near a filament spine point. |
| `sdss_nonvoid` | SN is covered by the void catalog but no usable filament label is available. |
| `outside_catalog_coverage` | SN is outside usable catalog redshift/sky coverage or has invalid coordinates. |

## Priority rules

1. `void` and `near_void_edge` take priority over filament labels.
2. If not void-like and the filament catalog covers the redshift range, use `filament`, `near_filament`, or `field_or_wall`.
3. If void coverage exists but filament coverage is unavailable, use `sdss_nonvoid`.
4. If neither catalog covers the row, use `outside_catalog_coverage`.

## Claim boundary

These labels are acceptable for a preliminary pipeline and smoke test of the Pantheon+ environment-H0 workflow. They remain derived cross-match labels and should not be presented as official Pantheon+ metadata or as an established H0/environment result until the full pipeline is reproduced and independently audited.
