# Pantheon+ Raw Input Staging Guide

**Status:** external/raw-data staging guide.  
**Purpose:** document the exact ignored raw inputs needed to run the covariance-aware Pantheon+ environment-H0 diagnostic without committing raw public-data files by accident.

This guide does not create a Pantheon H0 result. It explains how to stage the missing raw inputs locally so the existing runner can validate row order, covariance shape, environment labels, redshift cuts, group counts, and fit outputs.

## Claim boundary

Use:

> The Pantheon+ environment-H0 pipeline is a preliminary diagnostic scaffold. Environment labels are imported, and a full covariance candidate has been identified locally, but no H0/environment result is established until the Pantheon+ SN table is staged, row-order validation passes, and the covariance-aware runner emits fit outputs.

Avoid:

> The repo proves an environment-dependent H0 result or resolves the Hubble tension.

## Required local raw inputs

Raw Pantheon+ source files should be staged under ignored paths:

```text
data/pantheon/raw/Pantheon+SH0ES.dat
data/pantheon/raw/Pantheon+SH0ES_STAT+SYS.cov
```

The runner also supports these covariance candidate paths:

```text
data/pantheon/Pantheon_SH0ES_cov.txt.gz
data/pantheon/raw/Pantheon+SH0ES_STAT+SYS.cov
data/pantheon/pantheon_covariance.txt
data/pantheon/Pantheon_cov_subset.txt
```

Current diagnostic status from the latest Pantheon pass:

- `data/pantheon/environment_labels.csv` is present and row-aligned with 1701 labels.
- `Pantheon_SH0ES_STAT_SYS_cov.zip` was inspected locally and its member was classified as a usable flattened 1701 x 1701 covariance candidate.
- `Pantheon_cov_subset-5(1).txt` and `Pantheon_cov_subset-6.txt` are incomplete subset-like excerpts with only 99 entries after the leading `N=1701`; do not use them for the full 1701-row fit.
- `data/pantheon/raw/Pantheon+SH0ES.dat` remains the main blocker.

## Source files expected

The public PantheonPlusSH0ES/DataRelease directory `Pantheon+_Data/4_DISTANCES_AND_COVAR/` documents:

```text
Pantheon+SH0ES.dat
Pantheon+SH0ES_STAT+SYS.cov
```

The SN table must include row-alignment columns expected by the runner, including:

```text
CID
zHD
zCMB
RA
DEC
MU_SH0ES
```

The covariance file format expected by the runner is:

```text
1701
<1701 * 1701 flattened covariance entries>
```

## Checksum / provenance record

After staging raw files locally, record byte sizes and checksums before running diagnostics:

```bash
python - <<'PY'
from pathlib import Path
import hashlib

for path in [
    Path('data/pantheon/raw/Pantheon+SH0ES.dat'),
    Path('data/pantheon/raw/Pantheon+SH0ES_STAT+SYS.cov'),
]:
    if not path.exists():
        print(f'MISSING {path}')
        continue
    h = hashlib.sha256(path.read_bytes()).hexdigest()
    print(f'{path}\tbytes={path.stat().st_size}\tsha256={h}')
PY
```

Do not commit the raw files unless repository policy explicitly changes. Prefer committing a small provenance note with file name, byte size, SHA-256 checksum, source URL/reference, and staging date.

## Run command after staging

Run from the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 python notebooks/pantheon/run_pantheon_environment_h0_analysis.py
```

The runner should validate:

1. Pantheon row count equals 1701.
2. Environment label row count equals 1701.
3. Covariance shape equals `(1701, 1701)`.
4. Row-order safety using `row_index` plus `CID`, `RA`, `DEC`, `zHD`, and `zCMB` checks.
5. Locked redshift cut, expected grouping modes, and underpowered-contrast skip rules.

## Expected derived outputs if successful

Commit only derived outputs and summaries if the run completes:

```text
observations/pantheon-environment-h0/results/pantheon_environment_h0_group_counts.csv
observations/pantheon-environment-h0/results/pantheon_environment_h0_fit_by_group.csv
observations/pantheon-environment-h0/results/pantheon_environment_h0_contrast_results.csv
observations/pantheon-environment-h0/results/pantheon_environment_h0_run_summary.md
```

If the run blocks, commit only the updated run summary if it adds new diagnostic information. Do not fabricate empty fit CSVs.

## Filament-count caution

The imported label table has a very small strict filament sample. Strict filament-only H0 contrasts should be skipped or labeled underpowered unless the grouping mode broadens the comparison and the runner confirms both sides meet the predeclared minimum sample threshold.

## Storage policy

Raw data policy remains:

- Raw Pantheon+ SN tables and covariance matrices are external/ignored by default.
- Derived labels, summaries, checksums, validation notes, and fit CSVs may be committed.
- Large raw covariance files require an explicit redistribution/storage decision before being added to the repository.
