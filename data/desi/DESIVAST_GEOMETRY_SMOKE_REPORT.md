# DESIVAST geometry smoke report

Status: GEOMETRY IMPLEMENTED / STRICT P6 FIT BLOCKED. No distance moduli read and no H0 fit. P6 prediction / P5 paper track.

Sources: DESIVAST release https://data.desi.lbl.gov/doc/releases/dr1/vac/desivast/ ; VAST membership methodology https://vast.readthedocs.io/en/latest/VoidFinder_examples.html#using-the-output ; Rincon et al. https://arxiv.org/abs/2411.00148 . Raw files staged per DESIVAST_INPUT_MANIFEST.md.

Local execution used Python, NumPy, SciPy, pandas. Astropy unavailable; loader intentionally supports only the released scalar D/K FITS tables, not arbitrary FITS files. Independent Astropy readback and broader malformed-file tests remain desirable.

## Geometry and tests

Both catalog primary headers declare METRIC=comoving, OMEGAM=.315, HP=1, ZLIML=0, ZLIMU=.24. Compute comoving distances in Mpc/h using c/100 and flat Lambda-CDM. HP=1 is the unit convention, not a physical H0 measurement. MAXIMALS radial coordinates equal norm(X,Y,Z); hole-to-void ID joins complete. EDGE=0 retained as candidate interior; both 1 and 2 excluded from strict interior, exact flag 2 semantics not needed for this conservative exclusion.

| Cap | Maximals | Holes | EDGE 0 | EDGE 1 | EDGE 2 |
|---|---:|---:|---:|---:|---:|
| NGC | 3241 | 89003 | 1333 | 1872 | 36 |
| SGC | 524 | 12860 | 156 | 360 | 8 |
| Total | 3765 | 101863 | 1489 | 2232 | 44 |

The interior total agrees with published counts. Membership uses union of HOLES spheres, qualified by hemisphere and void ID. Multiple distinct void hits are ambiguous. No hit is unmatched/unclassified, never a positive filament or wall assignment. Even an interior hit is a candidate pending footprint/redshift policy verification. Closed sphere boundaries are an exploratory convention.

Seven synthetic geometry tests passed locally (union, edge, unmatched, boundary, overlap, invalid input, coordinate integration vs quadrature). Both real catalogs loaded. The smoke diagnostic was executed via equivalent inline commands; CLI wrapper added for reproducibility, not independently executed in this turn.

## Outcome-blind counts

Only CID, RA, DEC, HOST_RA, HOST_DEC, zHEL, zCMB and zHD loaded from Pantheon+. All 1701 host RA/DEC pairs fail physical coordinate validity; observed sentinel values -999 and -9. Supernova RA/DEC used for diagnostic only. No final frame choice or matching policy locked. The existing exploratory fit-window cut is zHD in [.01,.15], 715 rows (598 distinct literal CID strings before classification). Full counts include rows beyond this cut.

| Position redshift | Full interior | Full edge | Full overlap | Full unmatched | Full invalid/outside z | Cut interior | Cut edge | Cut overlap | Cut unmatched |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| zHEL | 9 | 7 | 2 | 1038 | 645 | 1 | 5 | 1 | 708 |
| zCMB | 12 | 12 | 2 | 1029 | 646 | 3 | 7 | 1 | 704 |
| zHD | 12 | 12 | 2 | 1029 | 646 | 3 | 7 | 1 | 704 |

No invalid/outside-z rows in the exploratory cut for these three geometry choices. Distinct literal CID counts in cut interior equal the respective row counts. These are NOT final survey-covered samples; no distance-modulus analysis performed. Do not select zCMB or zHD merely to increase matches. Resolve frame against DESIVAST construction before locking any endpoint.

## Reproduction

From repo root, with raw inputs outside Git:

    python -m unittest discover -s notebooks/desi -p test_desivast_catalog_loader.py -v
    python notebooks/pantheon/generate_environment_labels_from_desivast.py --catalog-dir /path/to/staged --pantheon /path/to/staged/pantheonplus/Pantheon+SH0ES.dat

## Next gates

1. Confirm source bytes against publisher, validate coordinate convention/footprint, and independently read FITS with Astropy/VAST. Review whether supplied catalog geometry and source coordinates match official release and expected overlap.
2. Check coordinate-only overlap with ZOBOV/VIDE/REVOLVER and independent SDSS labels; no outcome-informed method selection. Obtain survey mask and positive filament labels; use density rank only as explicitly separate exploratory proxy.
3. Estimate prospective power from unique objects and joint covariance; present detectable effect and sample requirements. The tiny interior count in the current window is insufficient for a credible target 1–3 km/s/Mpc claim; no confirmatory fit until feasibility and preregistration gates.
4. If needed, expand sample through a justified independently selected SN catalog or different void survey; keep any higher-redshift extension separate. Standard outflow and selection modeling remain required. Preserve historical SDSS labels.

No scientific outcome, no SoCT evidence, no claim of falsification.
