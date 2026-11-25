# P6 mask and watershed geometry audit

2026-11-25 UTC. Outcome-blind execution completed. PR33 merged at 706c3a107f4bd87eb91dbad641e7974d39d7f9af. No distance moduli, measured distances or H0 outcomes loaded. Original Pantheon+ and CF4 windows unchanged. No final environment labels.

## Reproduction

Extract the core, CF4, VIDE and REVOLVER archives into one staging directory. Keep mask parts as three standalone FITS files. From repository root:
    python -m unittest discover -s notebooks/desi -p test_coverage_watershed.py -v
    python notebooks/desi/coverage_overlap.py STAGED MASK1 MASK2 MASK3
    OPENBLAS_NUM_THREADS=1 python notebooks/desi/watershed_overlap.py STAGED MASK1 MASK2 MASK3
    python notebooks/desi/mesh_audit.py STAGED

Six new synthetic tests passed locally. Both overlap CLIs executed. Full mesh audit finished for REVOLVER NGC and SGC; timed out during VIDE. Separate zero-edge VIDE mesh check completed and restricted overlap CLI executed on all four catalogs. The standalone narrow FITS reader and NumPy HEALPix indexer are diagnostic implementations. Astropy/healpy unavailable; attempted dependency installation failed. Reference: https://healpix.sourceforge.io/html/Healpix_cxx/healpix__base_8cc_source.html ; VAST documentation https://vast.readthedocs.io/en/latest/Vsquared_examples.html . Independent library comparison, boundary-distance validation and source authentication remain outstanding.

## Mask lookup

All 12582912 stored coordinate centers mapped to the exact supplied nested pixel IDs at NSIDE=1024; checked for duplicates and gaps; 825472 DONE pixels. Angular point inclusion is a reconstructed-mask gate, not radial completeness or validated neighborhood support. The original unpublished mask is not available. The catalog primary headers also report different coverage areas: VoidFinder NGC 2446.47, SGC 406.31 deg2; V2 NGC 2450.44, SGC 414.27 deg2. These differ from reconstructed 2320.47/385.83 deg2; likely definitions/resolutions differ, but explanation not verified. Do not claim equivalent algorithm-specific masks.

## VoidFinder covered counts

Position frame CMB for comparison; Pantheon window uses nominal zHD. CF4 uses Vcmb/c. All original strict interior candidates survive. Distinct literal IDs equal interior rows; no final selection. Unmatched means unclassified, not filament.

| Dataset | Window | Total | Mask covered | Interior | Edge | Ambiguous | Unmatched within mask |
|---|---|---:|---:|---:|---:|---:|---:|
| Pantheon+ | .01–.15 | 715 | 82 | 3 | 6 | 1 | 72 |
| Pantheon+ | .01–.24 | 944 | 111 | 12 | 10 | 2 | 87 |
| CF4 groups | .01–.15 | 35978 | 5008 | 61 | 671 | 82 | 4194 |
| CF4 galaxies | .01–.15 | 52816 | 7054 | 78 | 854 | 73 | 6049 |

CF4 extended window identical because the maximum nominal redshift is below .15. Pantheon zHEL sensitivity: 1 and 9 interiors in the two windows; zHD 3 and 12. No claim of independent tests. CF4 groups and galaxies overlap and cannot be pooled.

## V2 visualization mesh checks

Per VAST, each V2 void is a union of Voronoi cells and TRIANGLE describes visualization boundary triangles. For source catalog objects, GALZONE/ZONEVOID define membership. Arbitrary external point containment requires verified geometry/complete generating sites. Use conservative EDGE_AREA==0 and TOT_AREA>0 for this smoke audit, NOT the paper's interior criterion. Closed edge incidence requires exactly two incident triangles per exact-coordinate-welded undirected edge, no degenerate triangles; consistent winding requires opposing directions. No repair or tolerance-based weld. Closed incidence is necessary, not proof of manifold embedded geometry, complete physical boundary or absence of self-intersections.

| Method/cap | Void rows | Mesh missing (all) | Zero-edge rows | Zero-edge missing | Zero-edge closed | Zero-edge closed + consistent winding |
|---|---:|---:|---:|---:|---:|---:|
| VIDE NGC | 1258 | 199 | 105 | 11 | 93 | 0 |
| VIDE SGC | 220 | 22 | 6 | 1 | 5 | 0 |
| REVOLVER NGC | 1692 | 0 | 131 | 0 | 131 | 0 |
| REVOLVER SGC | 300 | 0 | 8 | 0 | 8 | 0 |

One zero-edge VIDE NGC mesh had a nonmanifold edge. All REVOLVER meshes passed closed edge incidence, none had consistently oriented winding. All VOIDS REDSHIFT values in the four pruned files were within 0–.24, unlike previously observed ZOBOV anomaly; independent parser/source verification still needed.

## Restricted point containment

Use axis-aligned bounding box then three fixed non-axis-aligned ray-parity evaluations, not signed winding. Intersection on face edge, vertex, origin within numerical tolerance or disagreement => ambiguous; multiple eligible mesh hits => ambiguous. Near-boundary physical uncertainty, self-intersection, overlaps with excluded meshes and comparison to GALZONE/ZONEVOID on source tracers remain untested. Do not use no-hit as a negative environment label. Candidate hits only within reconstructed mask and z window.

| Method | Eligible meshes | Pantheon .01–.15 | Pantheon .01–.24 | CF4 groups | CF4 galaxies |
|---|---:|---:|---:|---:|---:|
| VIDE | 98 | 0 | 1 | 0 | 0 |
| REVOLVER | 139 | 0 | 1 | 0 | 0 |

No ambiguity from tested rays in these samples. Extended candidates may overlap between algorithms; no independent detections. This restricted selection does not reproduce published nonedge counts (297 VIDE, 389 REVOLVER; Rincon et al. 2025); cannot infer full-catalog overlap or physical absence from these zeros. No H0 fit.

## Next gate

1. Independent source/library check and reconciliation of mask area conventions. Quantify boundary sensitivity using angular erosion or distance-to-mask-boundary at predefined scales; verify actual published edge-area policy and compare triangle membership to source galaxy Voronoi-zone assignments (and official completeness). Investigate missing VIDE surfaces; no silent mesh repairs.
2. Coverage-controlled LSS density proxy using staged BGS data and sampled randoms: define selection, local aperture support and weight policy, assess sparse random counts, radial n(z) and convergence. Never call density rank a filament classifier. Positive filament classification remains separate.
3. CF4 indicator/error audit, correlated group/void power, conventional flow null, freeze protocol. Original P6 void-versus-filament test remains blocked. No new physics result or falsification.

Raw data remain external. The geometry-only diagnostic is a partial implementation, not production membership or final mask validation.
