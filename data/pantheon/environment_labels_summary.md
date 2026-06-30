# Pantheon+ Environment Labels — Local Generation Summary

**Generation date:** 2026-06-30
**Output:** `data/pantheon/environment_labels.csv`
**Rows:** 1701
**Method version:** `sdss_void_filament_crossmatch_v0.1`

## Source inputs used

| Input | Bytes | SHA-256 |
|---|---:|---|
| `Pantheon+SH0ES.dat` | 579283 | `1cb0fc379ef066afdc2ffd1857681cc478024570d8a3eba284fb645775198cf8` |
| `Pantheon+SH0ES_STAT+SYS.cov` | 33284960 | `abf806d966485e64afdb359c87bffc0ecc00d05eff0a31ced66f247385df0fdc` |
| `void_catalog_2014.06.18_just_sdss.tar.gz` | 327352211 | `104a892379b1ff36848d2fd15e27784835d68f80418af6f997fd5af117e1bc02` |
| `J_MNRAS_438_3465.tar.gz.tar` | 44933120 | `e4e548dd8580386824d9b9e59825f2684f9bcff568b59073ea1485615ff81a07` |

## Output checksum

| Output | Bytes | SHA-256 |
|---|---:|---|
| `environment_labels.csv` | 705628 | `ff3006e8cbf7316db29b3760f39d02e911b99a86e814e1a698014a8242695a9d` |

## Environment label counts

| Label | Count |
|---|---:|
| `field_or_wall` | 827 |
| `sdss_nonvoid` | 741 |
| `outside_catalog_coverage` | 75 |
| `void` | 34 |
| `near_void_edge` | 21 |
| `filament` | 2 |
| `near_filament` | 1 |

## Coverage counts

| Coverage flag | Count |
|---|---:|
| `derived_crossmatch` | 1626 |
| `outside_catalog_coverage` | 75 |

## Validation checks

- Confirmed `environment_labels.csv` exists.
- Confirmed row count matches the Pantheon+ table: 1701 rows.
- Confirmed `row_index` is sequential from 0 to 1700.
- Confirmed required output columns are present.
- Confirmed `environment_label` is nonempty for every row.
- Confirmed row-order safety by matching `CID`, `RA`, `DEC`, `zHD`, and `zCMB` row-by-row against the Pantheon+ source table.

## Claim boundary

These are derived SDSS void + Tempel/Bisous filament cross-match labels for preliminary Pantheon+ environment-H0 pipeline testing. They are not official Pantheon+ metadata and do not establish an H0/environment detection without the full covariance-aware fit and independent reproducibility audit.

## Notes

This file was generated locally from the uploaded source inputs because Codex did not have the raw/staged files in its workspace. The raw Pantheon+ and catalog archives should remain untracked unless redistribution/storage policy is explicitly settled.
