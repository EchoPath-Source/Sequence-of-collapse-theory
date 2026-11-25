# P6 CosmicFlows-4 geometry-only overlap audit

Status: EXECUTED / PROMISING LARGER CANDIDATE SAMPLE / CONFIRMATORY FIT BLOCKED. P6 prediction, P5 paper. PR32 merged at 1c97e5c1c780db51748530128f4c0f1b867558ed. No distance moduli, measured distances, peculiar velocity residuals, or H0 values loaded in analysis.

## Inputs and reproducibility

Use staged CF4 TSVs and DESIVAST VoidFinder NGC/SGC per DESIVAST_INPUT_MANIFEST.md. CF4 hashes rechecked:
- cf4_groups.tsv b6d9fba37fe35cc45e548296b5ef899f05c290bb524cbd8b9c5d595e8a591bab
- cf4_galaxies.tsv eac1bfdc2ab65a159fab1bb8824f08823339b5eb12a12abd8eacafd1bd4ddc41

Sources: Tully et al. 2023, ApJ 944, 94, https://cdsarc.cds.unistra.fr/viz-bin/cat/J/ApJ/944/94 ; EDD https://edd.ifa.hawaii.edu/catalog/kallcf4 ; DESIVAST https://data.desi.lbl.gov/doc/releases/dr1/vac/desivast/ . CF4 metadata verifies Vcmb is systemic CMB-frame velocity, not peculiar velocity; use z=Vcmb/c as redshift-space proxy. Group Vh is solar-frame velocity, used only as sensitivity. Coordinate conversion reuses the PR31 fiducial Om=.315 and Mpc/h convention. The actual catalog construction frame remains to be confirmed. No distance-derived supergalactic positions used.

Run from repository root:
    python -m unittest discover -s notebooks/desi -p 'test_*overlap.py' -v
    python -m unittest discover -s notebooks/desi -p test_desivast_catalog_loader.py -v
    python notebooks/desi/cosmicflows_overlap.py /path/to/p6_staging

Local execution passed 10/10 tests (7 existing geometry + 3 new tests for geometry-only read and duplicate IDs, distinct group/void counts, and radial perturbation). Both CF4 files loaded with unique primary identifiers, no missing parent IDs. VizieR groups table contains 38053 unique IDs (12 fewer than published 38065); galaxy file 55877 unique PGC, 38035 distinct parent IDs, 12 parent IDs absent from staged group table. Reconcile these before combining/grouping sources. Do not add galaxy and group samples.

## Observed geometry-only counts

Fixed nominal CMB window z=.01–.15 inclusive; maximum catalog z=.108659. EDGE=0 union of holes, no overlap with another void, qualified by hemisphere ID. Unmatched is unclassified, not filament; no angular mask verified.

| Table | Window rows | Interior | Edge | Ambiguous | Unmatched | Interior parent groups | Interior void IDs |
|---|---:|---:|---:|---:|---:|---:|---:|
| Groups | 35978 | 61 | 785 | 85 | 35047 | 61 | 17 |
| Galaxies | 52816 | 78 | 1006 | 74 | 51658 | 72 | 23 |

55 of 61 interior group rows are singleton groups. Group and galaxy geometry differ and cannot be treated as independent samples. No final label export.

| CMB redshift window | Group rows / interior | Galaxy rows / interior |
|---|---:|---:|
| .023–.15 | 30553 / 61 | 45540 / 78 |
| .01–.05 | 16414 / 0 | 24648 / 0 |
| .05–.15 | 19564 / 61 | 28168 / 78 |

No interior hits at z<=.05 in this staged crossmatch. Check angular/radial completeness and source fidelity before interpreting this distribution; this is not a physical absence of low-z void galaxies.

## Sensitivity (fixed nominal .01–.15 sample)

| Coordinate case | Group interior | Galaxy interior |
|---|---:|---:|
| Nominal CMB | 61 | 78 |
| CMB minus 300 km/s | 66 | 66 |
| CMB plus 300 km/s | 63 | 137 |
| Same interior void at nominal and both offsets | 22 (8 void IDs) | 20 (19 parent groups, 12 void IDs) |
| Group heliocentric Vh | 66 | not evaluated |

51 groups retain the same interior void between nominal CMB and heliocentric coordinates. The +/-300 check is illustrative radial perturbation, not a correction, selection threshold, probabilistic model, or bound on real velocities. Do not select a frame or perturbation based on count or eventual H0 results.

## Prospective power sanity check

For an optimistic independent Gaussian mean contrast with infinitely precise comparison group, assumed scatter sigma_mu, and two-sided alpha=.05, 80% power, detectable modulus contrast approx 2.8016*sigma_mu/sqrt(N_void). Convert with 70*(10^(delta_mu/5)-1) for magnitude of a positive H0 offset. These are illustrative assumed scatters, not measured CF4 residuals; finite controls, calibration, shared void/velocity covariance, indicator selection and label uncertainty worsen power in general.

| N candidate groups | sigma=.15 mag | sigma=.30 mag | sigma=.40 mag |
|---|---:|---:|---:|
| 61 nominal | 1.76 | 3.56 | 4.78 |
| 22 stable | 2.95 | 6.02 | 8.14 |

Units km/s/Mpc. This is not covariance-aware power or a statement of detected effect. CF4 is not automatically more statistically powerful than a smaller SN sample; distance-indicator scatter matters. Target 1–3 km/s/Mpc remains challenging, especially when within-void correlations reduce effective N.

## Next gate

1. Verify DESIVAST source bytes, footprint, redshift convention, independent parser and redshift-space membership; resolve previous ZOBOV schema anomaly.
2. Acquire documented footprint support and actual filament classifier; obtain VIDE/REVOLVER and validate their selection/topology. Avoid forcing nonvoid/edge/unmatched into filament. Existing SDSS comparison remains historical.
3. Audit CF4 distance-indicator availability and reported error fields without exposing measured modulus/velocity residual values; reconcile missing group IDs, selection/calibration differences and independence of velocity controls. Select a homogeneous distance-indicator sample where feasible. Use group clustering and cross-void covariance, independent mocks or velocity model; CF4 velocities derived from distances are not independent controls on those distances.
4. Compute prospective joint power from frozen selection and covariance assumptions; if insufficient, investigate larger independent distance samples or alternate survey overlap. Document new CF4 protocol separate from original Pantheon+ preregistration.
5. Freeze conventional outflow/selection null, predicted additional SoCT effect and failure criteria before outcome analysis.

No final labels, no new physics claim, no H0 fit. This is a feasibility result, not evidence for or against P6. Raw inputs stay external.
