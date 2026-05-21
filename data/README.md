# Data Directory

**Status:** Scaffold / provenance landing zone

This directory is reserved for raw, semi-processed, and derived data artifacts used in Sequence of Collapse Theory empirical tests.

## Data Policy

Do not add third-party datasets unless provenance, citation requirements, redistribution rights, and file size are clear.

Preferred pattern:

1. Add a source/provenance note first.
2. Add a schema for expected columns.
3. Add scripts or notebooks that can reproduce derived tables.
4. Commit derived summaries only when they are small and clearly labeled.
5. Keep large raw files outside the repo when licensing or size makes GitHub inappropriate.

## Current Planned Subfolders

```text
data/
├─ sparc/
│  └─ README.md
└─ pantheon/
   ├─ README.md
   ├─ covariance-notes.md
   └─ environment-labels-schema.md
```

## Claim-Level Labels

Use these labels in data notes and result tables:

- `raw-source` — direct external dataset, unmodified.
- `processed` — transformed from external dataset by documented script.
- `derived` — calculated output such as fitted parameter table, correlation table, or residual summary.
- `exploratory` — not suitable for publication claims.
- `validation-grade` — reproducible and ready to support a manuscript claim.

## Missing High-Priority Data Artifacts

- SPARC derived age/f_DM table.
- SPARC radial-decomposition table.
- Pantheon+ supernova metadata table.
- Pantheon+ covariance notes and source pointer.
- Supernova environment-label cross-match output.
- PM simulation parameter logs and H-split summary outputs.
