# P6 CF4 uncertainty and 5% random block-support audit

2026-11-25. PR35 merged at c9444b79d8e9ef0dd7f49bdfedcd6042a074d8fe. Outcome-blind: only identifiers, positions, redshifts, indicator counts and reported uncertainty columns of CF4 were loaded; no measured distance moduli, H0 or peculiar-velocity residuals. No final classifications or fits.

## CF4 error availability

Sources: VizieR J/ApJ/944/94 https://cdsarc.cds.unistra.fr/viz-bin/ReadMe/J/ApJ/944/94 ; EDD table 3 https://edd.ifa.hawaii.edu/describe_columns.php?table=kcf4allgroup ; Tully et al. https://arxiv.org/abs/2209.11238 . Positive finite error is an availability proxy, not proof of a valid underlying measurement. Group indicator counts may differ from error availability (e.g. covered FP 4234 positive counts vs 4245 positive errors; reconcile before science use). Recompute mask-covered strict interior and same-ID ±300 km/s sensitivity using PR34 geometry.

| Sample | Window rows | Covered | Interior | Stable |
|---|---:|---:|---:|---:|
| Groups | 35978 | 5008 | 61 | 22 |
| Galaxies | 52816 | 7054 | 78 | 20 |

| Group field | Covered positive errors | Median mag | Interior positive errors | Interior median mag |
|---|---:|---:|---:|---:|
| e_DMav | 5008 | .510 | 61 | .530 |
| e_DMfp | 4245 | .510 | 61 | .530 |
| e_DMtf | 764 | .430 | 0 | — |
| e_DMsnIa | 95 | .150 | 0 | — |
| e_DMsbfo | 0 | — | 0 | — |
| e_DMsbfi | 8 | .083 | 0 | — |
| e_DMsnII | 5 | .360 | 0 | — |
| e_DMzp | 5008 | .510 | 61 | .530 |

All 61 interior group rows have positive FP count, no positive other indicator counts or SNII uncertainty. All 22 stable groups likewise. 4149 covered groups have FP count only under this proxy. Interior FP error p10/median/p90=.460/.530/.560 mag; stable=.355/.530/.559. All 78 interior galaxies have positive FP errors only, median .520; 72 parent groups. Stable 20 galaxies, 19 parents, median .515. Do not pool galaxies and groups. The 38053 group rows match VizieR merged-table row count, not the 38065 published total. Twelve parent IDs missing: 3085,12783,17223,36536,41471,56062,59529,1490117,2491454,3339448,5698034,6494152. Cause not established; resolve with EDD original table, not imputation.

Optimistic inverse-variance error-only bound: SE=1/sqrt(sum(1/sigma_i^2)), infinitely precise comparator, independent Gaussian errors, two-sided alpha=.05 and 80% power. MDE=70*(10^(2.8016*SE/5)-1) for positive H offset. 61 nominal: SE=.062472 mag, MDE=5.876 km/s/Mpc. 22 stable: SE=.100178 mag, MDE=9.658. Neither reaches 1–3. Not formal power: finite controls, calibration, selection, correlated flow and shared void covariance not modeled; group quoted errors do not supply full covariance. FP-only subset merits separate homogeneous-indicator feasibility, not outcome-based selection. Published CF4 calibration/systematic uncertainty and selection issues require explicit models; see https://doi.org/10.1093/mnras/stag1144 . No independent peculiar-velocity control using distance-derived CF4 residuals.

## 5% random intake and support

Both downloaded and independently SHA-256 checked against Muse email:
- NGC 63351360 bytes, 653000 rows (unique TARGETIDs within file), 81160e7b32aa8d67dd808df9452d3d8dbefae30e97df182361d35ccee6f36801
- SGC 28238400 bytes, 291000 rows (unique TARGETIDs within file), a48c117508694d224a3375b92c1f7d866dbc24bdaba248e1fce7c1ea92fb77b8

Positive finite weights, finite valid coordinates, positive z. Header SAMPSEED=20261125 SAMPBLCK=1000 SAMPFRAC=.05. Reported Bernoulli selection of contiguous 1000-row blocks from same source index 0 as 1%; not independent realizations; overlap unverified, original source row membership not supplied, no sampling JSON or 5% sampler received. Actual fractions 4.93% and 5.36%. Within [.01,.24]: NGC 353660, SGC 157786; mask retained 137370 and 20531 respectively. Total 511446 radial, 157901 masked.

Assuming delivered consecutive blocks correspond to intact source blocks as described, compute maximum angular distance from each block's unit-vector centroid. Median/p90/max degrees NGC 1.124/3.906/129.208, SGC 1.309/7.720/121.057. Thus uniform small angular-block extent is not established; extreme spans may reflect sorting transitions. For CF4 covered centers, rerun .80 aperture geometry gate with nested 1024/2048 Sobol offsets and **raw WEIGHT** effective count, no data/random alpha normalization. This is a support-only diagnostic, not a rerun of the full density estimator. Minor differences vs PR35 expected from raw weighting. 1% median raw counts 4/24/72; 5% 19/132/376.

| Radius h^-1 Mpc | Geometry eligible | 1% point N_eff>=25 | 5% point N_eff>=25 | 5% point N_eff>=50 | 5% median block concentration N_eff | 5% block N_eff>=10 | 5% block N_eff>=25 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 10 | 2782 | 0 | 488 | 3 | 5.492 | 77 | 0 |
| 20 | 1514 | 200 | 1508 | 1416 | 7.362 | 321 | 4 |
| 30 | 821 | 821 | 821 | 821 | 13.963 | 690 | 5 |

Block concentration N_eff=(sum block weights)^2/sum(block weights^2), descriptive only, not design-based uncertainty or independent N. Block columns conditional on point gate. Median distinct contributing blocks 7/10/18. This is not a final coverage criterion. Point support improves substantially, but cluster sampling can increase local variance and cannot be judged by row count alone. At 10 only 488/2782 geometrically eligible centers pass point gate, 3 pass >=50. No final density stability, labels or power inferred.

## Reproduction and next gate

Local equivalent scripts executed on staged files; committed CLI wrappers reuse existing repo helpers and have not been independently rerun or unit-tested in this turn. Commands:
    python notebooks/desi/cf4_uncertainty_audit.py STAGED MASK1 MASK2 MASK3
    OPENBLAS_NUM_THREADS=1 python notebooks/desi/random_block_support.py STAGED RAW MASK1 MASK2 MASK3

Request compact 5% sampler and selection manifest with source block/row IDs, verify inclusion design and angular/redshift distributions, then compare full alpha-normalized density ratios at identical centers and scales using block-aware resampling or independently seeded within-block/row selection. Do not request more raw files until convergence and support targets defined. A stratified sparse row projection rather than contiguous blocks may be more efficient. CF4 FP-only continuous density test is a separate exploratory route; require indicator/covariance/selection/flow model and preregister effect before outcomes. Strict void-vs-filament test remains sample-limited and positive filament classification unresolved. No data files committed, no H0 fit.
