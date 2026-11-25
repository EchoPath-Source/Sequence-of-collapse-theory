# P6 remaining nine packages — intake and coverage gate

2026-11-25 UTC. All nine shared ZIPs downloaded into temporary analysis runtime; all member bytes streamed to EOF (CRC validation) and hashed. No H0 outcomes loaded. Raw data remain external. Original intake: DESIVAST_INPUT_MANIFEST.md.

| Archive | Compressed bytes | Member | SHA-256 of member |
|---|---:|---|---|
| P6_VIDE_NGC.zip | 128668968 | DESIVAST_BGS_VOLLIM_V2_VIDE_NGC.fits | 41b9073805b6ee11ab3855d0c21c255b7ba309186755e7d6e17c06eb1fac8ce3 |
| P6_VIDE_SGC.zip | 17277009 | DESIVAST_BGS_VOLLIM_V2_VIDE_SGC.fits | 9ae33edfe0c13ed6b0c189d2258edef4ec48171d27153b6b3ef8cd30c2ecb45c |
| P6_REVOLVER_NGC.zip | 170388339 | DESIVAST_BGS_VOLLIM_V2_REVOLVER_NGC.fits | 08d94b3e1740e154bde865b470c1f1a8d05d6e30ea4800fae2df2f5adec317b8 |
| P6_REVOLVER_SGC.zip | 24318992 | DESIVAST_BGS_VOLLIM_V2_REVOLVER_SGC.fits | 297e51d92b7955d81d68c674af78f43f2bc6c04247f7510c0224d1f81a984ad2 |
| P6_LSS_BGS_ANY_NGC_part1.zip | 122657657 | BGS_ANY_NGC_part1.fits | eed8995293a07ac0334c7628c071cea2c7becbad21e5d1eb8151db31584f3c88 |
| P6_LSS_BGS_ANY_NGC_part2.zip | 120527408 | BGS_ANY_NGC_part2.fits | baaf3ccfe335006bfff9ffe43f52066becb9f404d35576b453b5b13b946487ba |
| P6_LSS_BGS_ANY_SGC.zip | 85291928 | lss/BGS_ANY_SGC_clustering.dat.fits | eb42e382148a5880edcf5c70fd21747a13a1c850b0037176bdea9350a0428ba4 |
| P6_LSS_BGS_BRIGHT.zip | 19558842 | lss/BGS_BRIGHT-21.5_NGC_clustering.dat.fits | b67e8e3ee579d9673089f2c9c6930b793a2bf1895f85198472fb7fc5aa392825 |
| same | — | lss/BGS_BRIGHT-21.5_SGC_clustering.dat.fits | 4daf878cc5bfce71c3ee67f91882bd70179643033741af1f1324bdf655c5d98f |
| P6_LSS_LRG.zip | 101427789 | lss/LRG_NGC_clustering.dat.fits | 84548c4ea5208232f1c2f04416ddf272c72fa31313e3bbb60e67d134f186a027 |
| same | — | lss/LRG_SGC_clustering.dat.fits | ae478557d9ef70257cc689197052515f5ebbc0b23359c81159a8ad3289332e69 |

All four new DESIVAST hashes match the supplied checksum manifest; no independent publisher checksum retrieval in this pass. LSS hashes are local member hashes, not authenticated upstream hashes. Split parts are derived files, not byte-identical to original full FITS.

## LSS row audit

Streamed all scalar table rows with a narrow FITS reader and checked TARGETID uniqueness within each file, finite/in-range RA, DEC and positive finite Z, and finite positive WEIGHT, WEIGHT_COMP, WEIGHT_SYS, WEIGHT_FKP. All pass. No TARGETID intersection between the two NGC halves. Cross-cap and cross-tracer uniqueness not assumed. Counts:

| Member | Rows | 0<z<=.24 |
|---|---:|---:|
| BGS_ANY NGC part 1 | 2040613 | 1105640 |
| BGS_ANY NGC part 2 | 2040614 | 1108816 |
| BGS_ANY SGC | 1441126 | 779358 |
| BGS_BRIGHT-21.5 NGC | 217614 | 48644 |
| BGS_BRIGHT-21.5 SGC | 82429 | 18565 |
| LRG NGC | 1476135 | 0 |
| LRG SGC | 662492 | 0 |

NGC ANY logical concatenation gives 4081227 rows with disjoint IDs. Not physically stacked and not verified against source TARGETID sequence yet. All seven tables include TARGETID, Z, RA, DEC, NTILE, FRAC_TLOBS_TILES, WEIGHT_ZFAIL, WEIGHT, WEIGHT_COMP, WEIGHT_SYS, NX, WEIGHT_FKP, PHOTSYS. BGS tables additionally have dereddened fluxes g/r/z/W1/W2. No absolute magnitude or full targeting selection column present; do not equate the BGS_ANY z cut to the DESIVAST BGS Bright M_r<-20 volume-limited sample. Reconstruct exact selection with documented K/evolution corrections and targeting, or acquire authoritative selected tracers. Keep LSS density proxy separate. Confirm unblinded redshifts, official source identity and reader independently before science use.

## New DESIVAST FITS headers

| Catalog | VOIDS | ZONEVOID | GALZONE | TRIANGLE | GALVIZ |
|---|---:|---:|---:|---:|---:|
| VIDE NGC | 1258 | 2950 | 604032 | 3854410 | 604032 |
| VIDE SGC | 220 | 569 | 90610 | 511574 | 90610 |
| REVOLVER NGC | 1692 | 2950 | 604032 | 5321800 | 604032 |
| REVOLVER SGC | 300 | 569 | 90610 | 756302 | 90610 |

Header inspection only for these extensions; triangle boundaries and membership not yet validated. Verify IDs, tessellation/mesh, EDGE_AREA/TOT_AREA policy, frame and ZOBOV redshift anomaly before classification. No new overlap results.

## Minimum coverage request

Not BAO. Need an independent footprint and selection model, not just weights on observed targets. First seek the exact DESIVAST angular mask used to construct BGS Bright voids (both caps), with coordinate frame, pixelization, ordering/resolution and veto provenance; or a validated equivalent with explicit differences. Angular mask alone is a geometric first gate, not full radial/completeness correction.

For LSS density estimation, if needed, use a compact representative projection of version/tracer/cap-matched BGS randoms with RA, DEC, Z, WEIGHT (plus completeness and provenance fields where available), generated from official selection or by uniform seeded thinning of existing randoms, preserving weights and selection. Document original source, seed, sampling fraction, n(z), region and convergence at intended apertures. Choose density by coverage precision, not an arbitrary file size; start with geometry and assess support. A separate compact HEALPix completeness/selection map plus radial selection can be evaluated. No 6.7 GB random transfers, no LRG randoms for low-z branch, no new large acquisition until needed. FKP is not automatically a local density weight; define estimator and weights before outcome inspection.

References: https://data.desi.lbl.gov/doc/releases/dr1/vac/desivast/ ; https://desidatamodel.readthedocs.io/en/latest/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSION/index.html ; https://data.desi.lbl.gov/doc/releases/dr1/ .

Next: implement VIDE/REVOLVER geometry-only audit; independent source/mask and parser verification; density classifier with coverage; repeat candidate counts before power/preregistration. No H0 fit.
