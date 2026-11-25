# P6 coverage products — intake audit

2026-11-25 UTC. All eight Drive sharing notices received; three mask FITS parts and two random FITS files downloaded, and both Python scripts and the methodology note read in full. This is a transfer and structural audit, not a validated final survey mask or P6 result. No distance or H0 outcomes inspected. Raw products remain external.

## Reconstructed mask: direct local byte and table checks

| Part | Bytes | Pixel IDs inclusive | SHA-256 |
|---|---:|---|---|
| iron_mask_smoothed_reconstructed_part1of3.fits | 151001280 | 0–4194303 | 371d3a6f05dcb1bcb33f63a2b0e2acddab4ba9eb569d9d8fe7c92ffc30522d7a |
| iron_mask_smoothed_reconstructed_part2of3.fits | 151001280 | 4194304–8388607 | 02cd7926397051c5bbd4020d58e85aece363e69fccab946a82ebc44564017f57 |
| iron_mask_smoothed_reconstructed_part3of3.fits | 151001280 | 8388608–12582911 | 26b08788e981513ac7d654321b2e6b72cec6a3ad829ebb263fa68a9cfad73875 |

Each part is a standalone FITS binary table (not a byte chunk to concatenate), 4194304 rows of 36 bytes each, HPXNSIDE=1024, HPXNEST=T. Verified all pixel IDs in sequence, disjoint and collectively exhaustive (12582912 rows). Verified DESI/DONE FITS logical values, DESI equals GOAL>0, GOAL range 0–4, FRAC finite inside DESI and NaN outside, all DONE rows within DESI, FRAC=1 and RA>=40. 4508464 DESI pixels; 825472 DONE pixels. Using cap convention RA<80 or RA>300 = SGC, independently calculated:

| Cap | DONE pixels | Reconstructed deg² | Published area reported by Muse (deg²) |
|---|---:|---:|---:|
| NGC | 707787 | 2320.473169 | 2320.45 |
| SGC | 117685 | 385.829190 | 385.83 |
| Total | 825472 | 2706.302359 | 2706.28 |

The reconstructed counts and areas match Muse's report. Area agreement does not prove pixel-by-pixel agreement: a six-pixel difference in total count does not bound the symmetric difference of two masks. Original author mask not available. No independent HEALPix coordinate/index check or reconstruction rerun yet (Astropy/healpy unavailable in intake runtime). Do not compare hash of concatenated FITS parts to unsplit original. Member hashes identify received bytes.

## BGS_ANY sampled randoms

| Cap | Bytes | Source rows (header) | Sample rows | 0.01<=z<=0.24 | SHA-256 |
|---|---:|---:|---:|---:|---|
| NGC | 11802240 | 13248857 | 132489 | 71661 | c0a1b7846c298d2118584b25a0d89ad3f138bf4bd17d8c8e31a476a570cc9a60 |
| SGC | 4844160 | 5432939 | 54330 | 29582 | edd432a3db71c1294c2ea1325c891191f04734dd1a381263449696f8698499d2 |

Hashes independently match Muse's report. FITS scalar row layout 89 bytes with RA, DEC, Z, NTILE, PHOTSYS, FRAC_TLOBS_TILES, WEIGHT, WEIGHT_SYS, WEIGHT_COMP, WEIGHT_ZFAIL, NX, WEIGHT_FKP. All numeric fields finite; coordinates within physical range, Z positive, listed weights and NX positive. Completeness range NGC .6667–1, SGC .7895–1. Stride=100, offset=0 in headers; counts match ceil(source_rows/100). Original source identity and row sampling not independently re-fetched; lack of source-row IDs limits direct verification. Fixed-stride sampling is deterministic but not guaranteed unbiased; check angular/radial/completeness distributions and aperture support before adopting for density estimation. These are BGS_ANY LSS v1.5 products, not exact DESIVAST volume-limited randoms.

## Source methodology (as delivered, not independently reproduced)

Read P6_Mask_and_Randoms_2026-11-25.md, reconstruct_desivast_mask.py, sample_bgs_randoms_1pct.py via Drive. Public upstream mask script https://github.com/hbrincon/DESIVAST/blob/main/galaxy_catalog/mask/mask_smoothed.py ; tile inputs https://data.desi.lbl.gov/public/dr1/survey/ops/surveyops/tags/1.0/ops/tiles-main.ecsv and https://data.desi.lbl.gov/public/dr1/survey/ops/surveyops/tags/1.0/ops/tiles-specstatus.ecsv . Reported recipe uses BRIGHT IN_DESI planned passes 0–3, mainbright QA good LASTNIGHT<=20220613, per-pass pixel unions, base DONE=FRAC==1, Gaussian smoothing sigma=2.8 deg, retain original DONE pixels with smoothed weight>=.338, RA>=40. Port substitutes per-pass union for TILEIDS and lmax=1024 for default 3071. Equivalence claims require independent checks, especially overlaps in tile selection, dependency/data versions and smoothing threshold sensitivity. Exact tile inputs, run logs, validation JSON, sampling JSON and model-data snapshots were not part of eight shared files. Request compact provenance artifacts if needed, not more full randoms. No full BAO analysis.

## Next gate

1. Validate HEALPix lookup and mask boundary handling; compare outcome-blind survey-covered candidate counts for Pantheon+ and CF4; do not label uncovered/unmatched as filament.
2. Validate VIDE/REVOLVER memberships and geometry independently; repeat blind overlap with mask.
3. Assess sampled random support and estimator convergence at predetermined apertures; compare with source selection metadata. If support inadequate, request a more suitable compact projection or additional seeded/offset random sample, not multi-GB transfers by default.
4. Establish positive filament classification, radial coverage/selection, distance-indicator and covariance feasibility, conventional null, and preregistration before H0 fitting.

Status: coverage inputs received and structurally checked; exact coverage equivalence and classifier integration remain pending. Raw files and Drive links not committed.
