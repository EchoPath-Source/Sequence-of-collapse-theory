# Pantheon+ environment-H0 covariance-aware run summary

**Status:** BLOCKED_MISSING_SN_TABLE

## Root Pantheon files found

Command run from the repository root:

```text
ls -lh Pantheon* pantheon* 2>/dev/null || true
```

Found root files:

- `Pantheon_SH0ES_STAT_SYS_cov.zip` — 11M root zip containing `Pantheon_SH0ES_STAT_SYS_cov.txt`.
- `Pantheon_cov_subset-5(1).txt` — 1.2K text covariance-looking excerpt.
- `Pantheon_cov_subset-6.txt` — 1.2K text covariance-looking excerpt.

No root Pantheon+SH0ES SN table was found. In particular, no root file inspected in this pass had the expected SN-table columns such as `CID`, `zHD`, `zCMB`, `RA`, `DEC`, and `MU_SH0ES`.

## Staged raw inputs

- SN table staged: none; `data/pantheon/raw/Pantheon+SH0ES.dat` is still missing.
- Full covariance staged: `Pantheon_SH0ES_STAT_SYS_cov.zip` was extracted to ignored local path `data/pantheon/raw/Pantheon+SH0ES_STAT+SYS.cov`.

Raw Pantheon inputs remain ignored by repository policy and were not staged for git.

## Covariance candidate inspection

| Root file | Size | First values | Inferred shape/status | Can form 1701 x 1701? |
| --- | ---: | --- | --- | --- |
| `Pantheon_SH0ES_STAT_SYS_cov.zip` / `Pantheon_SH0ES_STAT_SYS_cov.txt` | 33,284,960 bytes inside zip | `1701, 0.03177108, 0.00575443, 0.00031006, 0.00118666, 0.00008342, -0.00009594, 0.00131823` | leading `N=1701` followed by `2,893,401 = 1701*1701` entries | yes |
| `Pantheon_cov_subset-5(1).txt` | 1,134 bytes | `1701, 0.03177108, 0.00575443, 0.00031006, 0.00118666, 0.00008342, -0.00009594, 0.00131823` | leading `N=1701` but only 99 entries after `N`; file has 100 numeric tokens total, so it is an incomplete/subset-like excerpt and is not row-compatible with a full 1701-row analysis | no |
| `Pantheon_cov_subset-6.txt` | 1,134 bytes | `1701, 0.03177108, 0.00575443, 0.00031006, 0.00118666, 0.00008342, -0.00009594, 0.00131823` | leading `N=1701` but only 99 entries after `N`; file has 100 numeric tokens total, so it is an incomplete/subset-like excerpt and is not row-compatible with a full 1701-row analysis | no |

## Analysis run status

The covariance-aware runner was executed after staging the full covariance locally:

```text
PYTHONDONTWRITEBYTECODE=1 python notebooks/pantheon/run_pantheon_environment_h0_analysis.py
```

It exited cleanly with `BLOCKED_MISSING_INPUTS` because the required SN table is still missing:

- `data/pantheon/raw/Pantheon+SH0ES.dat`

Because the SN table is absent, this pass could not validate:

- Pantheon row count = 1701;
- environment label row count = 1701 against the live SN table;
- covariance shape against the live SN row count, although the staged covariance itself is a valid flattened 1701 x 1701 covariance candidate;
- row-order safety for `CID`, `RA`, `DEC`, `zHD`, and `zCMB`;
- redshift-cut group counts;
- underpowered contrast skip behavior on live Pantheon rows;
- fit result CSV generation.

## Generated result files

- `observations/pantheon-environment-h0/results/pantheon_environment_h0_run_summary.md`

No fit CSV tables were generated in this pass because the run was blocked before data loading and fitting.

## Claim boundary

This is a preliminary covariance-aware pipeline execution using derived SDSS void + Tempel/Bisous filament cross-match labels. It does not establish a Pantheon H0/environment detection. Results are candidate diagnostics only until the raw input provenance, covariance handling, grouping choices, and independent reproducibility audit are complete.
