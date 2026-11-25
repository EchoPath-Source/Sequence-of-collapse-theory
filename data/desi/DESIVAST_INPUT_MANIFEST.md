# P6 environment-split H0 — input intake manifest

Status: CORE AND THREE SUPPORT BUNDLES STAGED / INPUT AUDIT ONLY. Intake 2026-11-25 UTC. P6 is the prediction identifier; P5 is the publication-roadmap track. No H0 outcomes fitted or inspected.

## Transport verification

Four ZIP files were retrieved into a temporary analysis runtime from the research team's shared Drive. All passed ZIP CRC checks and were safely extracted. Raw data are not committed. SHA-256 hashes below identify the received bytes, not independent publisher authentication.

| Archive | Bytes | SHA-256 |
|---|---:|---|
| P6_Core.zip | 14236025 | 30ae99a61a167c72eeafe240de2604760de5d6f614bb03e3b1936ccee4542994 |
| P6_CosmicFlows.zip | 5821879 | 74feb5d5cb01097436a5d739137ebc1b72ff650a524663480188cd6103602e59 |
| P6_AVISM.zip | 73936 | e0fe428fda4c0f47f5d07d929b6abb9d8050530d545426d8e01acdd627a326e1 |
| P6_ZOBOV.zip | 22937143 | 517466a639706c817273edf52bdb8b8b404716e280f66c4aaac0aa9fccf7a034 |

## Core and support file checksums

DESIVAST source: https://data.desi.lbl.gov/public/dr1/vac/dr1/desivast/v1.0/ . The four staged FITS hashes match the supplied official manifest (manifest SHA-256 7b8c33cb1c272cc69f028fbd696b344892da493e1bc43ab3f947fa5a1ebc9be1). Publisher-hosted manifest not independently re-fetched in this intake.

| File | SHA-256 |
|---|---|
| DESIVAST_BGS_VOLLIM_VoidFinder_NGC.fits | c69f2f7b2b1fed4554527475dd96584169b1ead5bbcd0c152164200e6a2f34c8 |
| DESIVAST_BGS_VOLLIM_VoidFinder_SGC.fits | 47c43b9b446f4bcb47cbc023115ac5297f9afb0045aea96d853649a80d7219c1 |
| DESIVAST_BGS_VOLLIM_V2_ZOBOV_NGC.fits | 70ddfe3fcc7183597435d62c75651c96271a0a7c364b4bb439ba1f9507f91c37 |
| DESIVAST_BGS_VOLLIM_V2_ZOBOV_SGC.fits | acbc1551ed64e38cfc489763939240844b18521095e9d667632ed1c7d5f8ed8a |
| pantheonplus/Pantheon+SH0ES.dat | 1cb0fc379ef066afdc2ffd1857681cc478024570d8a3eba284fb645775198cf8 |
| pantheonplus/Pantheon+SH0ES_STAT+SYS.cov | abf806d966485e64afdb359c87bffc0ecc00d05eff0a31ced66f247385df0fdc |
| cosmicflows4/cf4_groups.tsv | b6d9fba37fe35cc45e548296b5ef899f05c290bb524cbd8b9c5d595e8a591bab |
| cosmicflows4/cf4_galaxies.tsv | eac1bfdc2ab65a159fab1bb8824f08823339b5eb12a12abd8eacafd1bd4ddc41 |
| avism/BGS_catalogue_clean.txt | dc2ae9e7156b729ef342da5e6f503ba6e03a94a48dfd864f481c14632c7485b6 |
| avism/LRG_catalogue_clean.txt | 6d97385c201450f92006179bcb2b3b2005ae58552242115e4bc45b8197a23e03 |
| avism/read_void_cat.py | 3a2a4803c77c36aec83626233f312deac66cc0d001bd24af37eaf900d8b8c92c |

Pantheon+ source: https://github.com/PantheonPlusSH0ES/DataRelease . AVISM source: https://github.com/oscarmonllor99/AVISM_BGS_LRG_voids . CosmicFlows-4: VizieR J/ApJ/944/94 (NAOJ mirror per acquisition inventory). Other than supplied DESIVAST checksums, hashes are locally computed; Pantheon table hash agrees with acquisition inventory, covariance publisher identity/order remains to be established.

## FITS header audit (direct byte inspection)

| Catalog | HDU | NGC rows | SGC rows |
|---|---|---:|---:|
| VoidFinder | MAXIMALS | 3241 | 524 |
| VoidFinder | HOLES | 89003 | 12860 |
| ZOBOV | VOIDS | 2950 | 569 |
| ZOBOV | ZONEVOID | 2950 | 569 |
| ZOBOV | GALZONE | 604032 | 90610 |

MAXIMALS columns: X Y Z RADIUS VOID EDGE R RA DEC R_EFF R_EFF_UNCERT. Spatial distances Mpc/h, angles degrees. There is NO direct redshift column; Z is Cartesian. HOLES columns: X Y Z RADIUS VOID. True VoidFinder membership should use the union of holes for a void, not an effective-radius sphere. Verify EDGE semantics and fiducial cosmology against VAC documentation before classification.

ZOBOV VOIDS columns include VOID X Y Z REDSHIFT RA DEC RADIUS X1 Y1 Z1 X2 Y2 Z2 X3 Y3 Z3 TOT_AREA EDGE_AREA. GALZONE columns GAL TARGET X Y Z ZONE DEPTH EDGE OUT; ZONEVOID columns ZONE VOID0 VOID1. Do not infer topology from an effective radius or from raw ZOBOV zones alone. No Astropy installed in intake runtime; table semantics beyond headers and membership are not yet validated.

## Pantheon+ audit

1701 data rows, 1543 distinct literal CID strings (not a determination of the number of physical supernovae). 715 rows in existing exploratory zHD range 0.01–0.15 inclusive, before any coverage or sample selection; 277 rows USED_IN_SH0ES_HF=1 across full input. Required coordinate, redshift, calibrator and modulus fields exist. No distance-modulus values inspected. Covariance header N=1701; 2893401 matrix entries; finite, positive diagonal; maximum absolute asymmetry 3e-8 (mag squared); direct NumPy Cholesky succeeded. These checks establish structural plausibility, not source row-order identity or final numerical policy. Preserve original row index, resolve duplicate observations and verify released covariance pairing; quantify asymmetry and explicitly symmetrize within justified tolerance before fitting.

## Next gate

1. Confirm DESIVAST cosmology, EDGE flags, survey footprint/mask and redshift convention from official documentation. Use appropriate host coordinates and redshift for catalog matching, not automatically zHD.
2. Implement tested VoidFinder union-of-holes membership with distinct hemisphere IDs, edge exclusions and coverage-aware unclassified/nonvoid labels. Do not label nonvoid as filament. Existing DESI density classifier remains a separate branch.
3. Produce blinded geometry-only overlap, distinct-object counts and covariance-aware prospective power. Do not inspect outcomes or fit H0 before locking analysis. Existing SDSS labels remain historical; do not overwrite them.
4. Establish a positive filament classifier and survey-mask support for strict P6. Compare to conventional velocity/environment predictions; avoid double-correcting zHD with CosmicFlows.
5. Joint covariance fit with cross-group terms, calibrator policy, duplicate treatment and a locked selection, effect-size range and conventional null; independent validation.

VIDE, REVOLVER and LSS clustering catalogs not retrieved in this batch. Survey masks/randoms or an equivalent validated footprint are still needed. Raw bundles are temporarily staged, not guaranteed persistent in a later runtime; use original shared archives to restage. This is an input audit, not physical evidence for SoCT/PNT.
