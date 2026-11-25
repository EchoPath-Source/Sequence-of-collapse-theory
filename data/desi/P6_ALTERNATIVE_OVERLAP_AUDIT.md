# P6 alternative-catalog overlap audit

Status: EXECUTED GEOMETRY-ONLY / STRICT P6 BLOCKED BY SAMPLE AND CLASSIFICATION. P6 prediction, P5 publication track. No SN distance modulus values read or H0 fits performed.

PR 31 merged as 99bca4d56f758454447f03833fcb57a7ab1e66c1. Existing seven local geometry tests rerun, all pass. New local script executed successfully against staged core, ZOBOV and AVISM archives. Reproduce from root:

    python notebooks/desi/alternative_overlap.py /path/to/p6_staging

## Sources and definitions

- DESIVAST release: https://data.desi.lbl.gov/doc/releases/dr1/vac/desivast/
- VAST V2 format: https://vast.readthedocs.io/en/latest/Vsquared_examples.html#output ; hierarchy: https://vast.readthedocs.io/en/latest/Vsquared_functions.html
- AVISM catalogue README and reader as supplied in archive, upstream https://github.com/oscarmonllor99/AVISM_BGS_LRG_voids ; paper https://arxiv.org/abs/2610.18348 .
- Historical SDSS: data/pantheon/environment_labels.csv and environment_labels_summary.md, read from main. Counts computed from row-aligned historical CSV, not independently reclassified in this pass.

Pantheon read only CID, RA, DEC, zHEL, zCMB, zHD. Base window zHD=.01–.15 inclusive: 715 rows, 598 distinct literal CIDs. Exploratory extension .01–.24: 944 rows, 827 CIDs. AVISM BGS .1<zHD<.3: 466 rows/CIDs; LRG .4<zHD<.8: 278. Matching frame alternatives zHEL/zCMB/zHD are sensitivity checks, not three independent experiments.

## Results

Entries below are candidate row counts in frame order zHEL/zCMB/zHD; all positive counts from newly evaluated catalogs have equal distinct literal CID counts. No survey footprint established. The two ZOBOV methods and AVISM are proxies, NOT authoritative membership.

| Method | Base .01–.15 | Extended .01–.24 | Native AVISM window |
|---|---|---|---|
| VoidFinder union, EDGE=0 | 1/3/3 | 9/12/12 | n/a |
| ZOBOV nearest listed site, 5 Mpc/h | 0/0/0 | 2/1/1 | n/a |
| ZOBOV nearest listed site, 10 Mpc/h | 0/0/0 | 2/1/1 | n/a |
| ZOBOV effective-radius spheres | 0/0/0 | 1/1/1 | n/a |
| AVISM BGS geometric center sphere | 0/0/0 | 3/2/2 | 3/2/2 |
| AVISM BGS maximum-divergence center sphere | 0/0/0 | 0/0/0 | 0/0/0 |
| AVISM LRG either center | 0/0/0 | 0/0/0 | 0/0/0 |

ZOBOV: nearest of all finite listed GALZONE sites across caps, then require EDGE=OUT=0, smallest containing void (VOID0) with finite XYZ, positive radius and total area, EDGE_AREA=0; thresholds 5 and 10 Mpc/h illustrative. This is a nearest-listed-site proxy; no proof of complete generating sites, exact tessellation or footprint. Spherical proxy uses those same qualified voids, not actual boundaries. Largest containing void is identical across all zones in each cap, consistent with a full hierarchy and not a useful independent strict classifier. 162 NGC and 13 SGC voids satisfy Cartesian/area selection. Zero of 3519 rows have REDSHIFT within [0,.24]; finite values ~8.17e27–1.014e28. Staged file hashes rechecked against the intake manifest. Quarantine redshift field; do not silently rescale. Verify independently using Astropy and publisher/maintainer; not a proven upstream bug. Official VAC documentation emphasizes VIDE and REVOLVER, not raw ZOBOV as final pruned catalogs. Obtain those catalogs and their geometry/selection support for the next comparison.

AVISM: use flat fiducial Om=.31, H0=67.8 and cMpc units; geometric vs maximum-divergence centers both tested; apply respective native redshift ranges. The released catalog is a spherical approximation of real-space voids; SN observed/redshift-corrected positions are not the same reconstruction. Full 3D masks not staged. Cube/mask and boundary checks not implemented; no claim of complete spatial classification. No negative inference from no hits.

Historical SDSS counts in base window: void 19 rows (14 CIDs), filament 2 (2), near_void_edge 5 (4), near_filament 1 (1), field_or_wall 688 (577). Full catalog totals void 34 and filament 2. Historical labels are preliminary, lack validated angular footprint, and are not a rescue of strict contrast. The raw catalog geometry was not re-run.

## Prospective feasibility

No strict sample has enough verified void and filament objects. As an illustrative independent Gaussian calculation ONLY, at assumed 0.15 mag scatter and H0_ref=70, target 1–3 km/s/Mpc corresponds to ~0.031–0.091 mag. Equal groups, two-sided alpha .05, 80% power require about 372 to 43 objects per group (before correlations, nuisance parameters and selection). This is not a measured scatter or covariance-aware power result. No definitive power estimate until labels, covariance pairing, design and unique object treatment are frozen. Larger redshift range is a separate exploratory sensitivity, not a change to the primary window.

## Next gate

1. Independently verify ZOBOV REDSHIFT anomaly and coordinate frame against publisher; verify original VoidFinder source bytes and loader through Astropy.
2. Obtain VIDE/REVOLVER (pruned catalogs), survey mask and positive filament classifier, or an independently selected nearby SN/distance sample. Do not tune labels to H0 outcomes. DESI LSS density percentiles can support a separate void-like versus dense-like diagnostic, not true filament membership.
3. Evaluate larger nearby distance datasets (e.g. staged CosmicFlows-4) for footprint and genuine independent distance tracers; do not mix distance indicators or treat existing Vpec estimates as independent when derived from the same data. Keep calibration, distance-indicator selection, velocity-field modeling, overlap and correlated errors explicit. This is a new candidate protocol, not a preregistered substitution.
4. Report counts, uncertainty and power before freezing a confirmatory model. If sample remains insufficient, record underpowered and defer, not falsified. No H0 analysis until preregistration and coverage gates.

Raw files not committed. Existing historical labels untouched. New script is exploratory and uses the narrow FITS reader from PR31; independent parser cross-check and dedicated alternative-method unit tests remain open.
