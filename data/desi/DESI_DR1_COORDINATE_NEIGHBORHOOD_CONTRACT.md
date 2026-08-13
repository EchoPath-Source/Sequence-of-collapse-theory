# DESI DR1 Coordinate and Neighborhood Contract

**Status:** Production-method contract v0.1  
**Method family:** `desi-comoving-knn-shell-v0.1`  
**Purpose:** Freeze the coordinate geometry, fiducial cosmology, shelling assumptions, edge policy, and sensitivity grid used before DESI DR1 local-density/environment labels are generated.

## Scope

This contract governs the transformation

```text
DESI RA / Dec / redshift
  -> comoving radial distance
  -> comoving Cartesian x,y,z
  -> redshift-controlled kNN density
  -> within-shell density percentile
  -> candidate environment label
```

It does not establish that the resulting labels are physically unique void/filament classifications, and it contains no Pantheon+ or H0 result.

## Source coordinates

For the current DR1 `zpix` path, the source sky coordinates remain:

```text
mean_fiber_ra
mean_fiber_dec
z
```

The coordinate-semantics boundary in `data/desi/DESI_DR1_COLUMN_SEMANTICS.md` remains authoritative. `mean_fiber_ra` and `mean_fiber_dec` are not to be silently described as target coordinates.

Normalized downstream names may be introduced only with explicit provenance, for example:

```text
source_ra_field = desi_dr1.zpix.mean_fiber_ra
source_dec_field = desi_dr1.zpix.mean_fiber_dec
```

## Fiducial cosmology

Primary production geometry uses a flat Lambda-CDM fiducial cosmology consistent with the Planck 2018 baseline used in DESI DR1 distance-conversion analyses:

```text
H0 = 67.4 km s^-1 Mpc^-1
Omega_m = 0.315
Omega_Lambda = 0.685
Omega_k = 0
```

For the current `0.01 <= z <= 0.5` environment track, radiation is neglected in the distance integral.

This fiducial cosmology is a coordinate convention for constructing neighborhoods. It is not a claim that Planck 2018 cosmology is the final physical model and is not evidence against or for SoCT/PNT.

Primary source notes:

- Planck Collaboration VI (2020), DOI `10.1051/0004-6361/201833910`, reports base-Lambda-CDM `H0 = 67.4 +/- 0.5 km s^-1 Mpc^-1` and `Omega_m = 0.315 +/- 0.007`.
- DESI DR1 fiducial-cosmology studies explicitly describe DESI's baseline distance-conversion cosmology as Planck 2018 and test sensitivity to alternative cosmologies; see arXiv:`2406.06085` and subsequent DR1 full-shape fiducial-cosmology work.

## Comoving-distance definition

Use line-of-sight comoving distance

```math
chi(z) = (c / H0) * integral_0^z dz' / E(z')
```

with

```math
E(z) = sqrt(Omega_m (1+z)^3 + Omega_Lambda)
```

and

```text
c = 299792.458 km/s
```

Distances are stored in physical comoving `Mpc`, not `Mpc/h`.

The numerical integration method and tolerance must be deterministic and versioned. The repository implementation uses composite Simpson integration with a fixed even subdivision count unless explicitly revised.

## Cartesian transformation

Convert degrees to radians:

```text
alpha = RA * pi / 180
delta = Dec * pi / 180
```

then

```math
x = chi cos(delta) cos(alpha)
y = chi cos(delta) sin(alpha)
z_cart = chi sin(delta)
```

Output units:

```text
x, y, z_cart: comoving Mpc
```

The `z_cart` field must never be confused with spectroscopic redshift `z`.

## Primary neighborhood estimator

The current estimator family remains k-nearest-neighbor number density:

```math
rho_k = k / [(4/3) pi r_k^3]
```

where `r_k` is the comoving Cartesian distance to the kth neighbor **within the same redshift-control shell**.

Primary exploratory configuration:

```text
k = 5
redshift shell width = 0.02
minimum shell size = 20
```

These values are not publication-frozen until the live sample and sensitivity tests are available.

## Why shell normalization remains required

DESI sampling density changes with redshift and tracer population. Raw kNN density across the full redshift interval would therefore mix cosmic environment with the survey selection function.

The current v0.1 approach controls this by:

1. assigning each galaxy to a redshift shell;
2. estimating kNN density within that shell;
3. converting density to a percentile within the same shell.

The percentile is the primary environment-ranking quantity. Absolute `local_density` remains diagnostic and depends on the coordinate-scale convention.

## Candidate environment bins

Until validated against real DESI data, the percentile bins remain explicitly candidate labels:

```text
0-10%   -> void_like
10-30%  -> low_density
30-70%  -> sheet_like
70-90%  -> filament_like
90-100% -> cluster_like
```

These are density-rank bins, not a topological cosmic-web classifier such as tidal-tensor, velocity-shear, DisPerSE, watershed/ZOBOV, or Voronoi-web classification.

Consequently, manuscripts must say `density-percentile environment bin` unless/until a stronger topology method is implemented.

## Survey footprint and edge policy

A raw kNN estimator can falsely classify footprint edges, holes, fiber-assignment incompleteness, or masked regions as low-density environments.

DESI's own DR1 documentation provides clustering-ready LSS catalogs and associated random catalogs specifically to represent the usable survey selection/footprint. Production environment labels must therefore include an angular-footprint/completeness control rather than interpreting absent DESI targets as physical emptiness.

### Production requirement

Before full environment-label export, use DESI DR1 LSS random catalogs or an equivalently documented survey mask to estimate neighborhood coverage.

For each object, define a coverage diagnostic such as:

```text
coverage_fraction = observed random support / expected random support
```

for an angular/comoving aperture tied to the estimator scale.

Until this is implemented:

```text
EDGE_CORRECTION_STATUS = PENDING
```

and no full-sample `void_like` claim is permitted.

### Candidate edge threshold sensitivity

The first production implementation should test, not silently assume:

```text
coverage_fraction >= 0.70
coverage_fraction >= 0.80
coverage_fraction >= 0.90
```

The preferred threshold should be chosen from stability/retention diagnostics before Pantheon+ crossmatching.

Objects failing the selected coverage threshold should receive an explicit quality flag and should default to `unclassified` for the primary analysis rather than being forced into a low-density bin.

## Duplicate and coordinate-quality policy

Before density estimation:

- require finite RA, Dec, and redshift;
- require the frozen quality-selection predicates;
- resolve repeated astronomical objects using documented `targetid` / `zcat_primary` semantics;
- reject impossible RA/Dec/redshift values;
- do not impute missing sky positions or redshifts;
- preserve the original source coordinates in the provenance layer.

## Sensitivity grid

The environment method must be tested across a small preregistered-style grid before a production setting is promoted.

### Neighbor count

```text
k = 3, 5, 10
```

### Shell width

```text
Delta z = 0.01, 0.02, 0.04
```

### Fiducial geometry

Primary:

```text
Planck18: H0=67.4, Omega_m=0.315
```

Geometry sensitivity cases:

```text
LCDM-70: H0=70.0, Omega_m=0.300
LCDM-73: H0=73.0, Omega_m=0.300
```

Important interpretation: changing only `H0` approximately rescales all comoving distances and absolute densities but should leave neighbor ordering and within-shell percentiles nearly invariant. `Omega_m` changes the radial mapping non-uniformly with redshift and is therefore a more meaningful geometry sensitivity. Any substantial environment-label instability under these modest geometry changes must be reported.

### Candidate percentile thresholds

Primary exploratory bins:

```text
10 / 30 / 70 / 90 percent
```

Sensitivity should also test modest threshold shifts, for example:

```text
5 / 25 / 75 / 95
15 / 35 / 65 / 85
```

The purpose is to measure label stability, not to choose thresholds that maximize the later H0 contrast.

## Required stability metrics

For each sensitivity run record at minimum:

```text
row_count
classified_fraction
unclassified_fraction
median local_density by shell
environment-bin counts by shell
fraction of labels unchanged from baseline
Spearman correlation of density percentiles with baseline
edge-flag fraction
```

For Pantheon+ use, additionally record the fraction of matched supernovae whose environment label changes across reasonable estimator settings.

## Promotion gate

The candidate method may be promoted from exploratory to production only after:

```text
1. live DESI smoke query passes;
2. source coordinates/redshifts are validated;
3. production sample cuts are frozen;
4. DESI random/mask footprint control is implemented;
5. k/shell/cosmology sensitivity grid is run;
6. label stability is quantified;
7. edge-biased objects are flagged or excluded;
8. a small real-data environment export passes review.
```

## Repo implementation mapping

Coordinate conversion:

```text
notebooks/desi/desi_comoving_coordinates.py
```

Density/environment estimator:

```text
notebooks/desi/desi_environment_estimator.py
```

Estimator tests:

```text
notebooks/desi/test_desi_environment_estimator.py
```

Notebook plan:

```text
notebooks/desi/DESI_ENVIRONMENT_NOTEBOOK_PLAN.md
```

## Claim boundary

This coordinate contract makes the DESI environment test reproducible. It does not show that:

- the candidate percentile bins are unique physical void/filament classifications;
- DESI supports SoCT/PNT;
- gravity or dark matter is memory;
- voids have a higher H0;
- `H0_void > H0_filament` has been measured;
- the Hubble tension has been solved.

A null, unstable, footprint-dominated, or convention-sensitive environment result must be reported as such rather than rescued by changing the geometry or thresholds after seeing the Pantheon+ outcome.
