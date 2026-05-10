# SPARC Data Notes

**Status:** scaffold pending source files / links  
**Purpose:** document the provenance of every dataset used in the SPARC age / missing-mass analysis.

## Rules

Do not add derived or cleaned tables without documenting:

1. source URL or citation,
2. access date,
3. license or usage constraints,
4. variables imported,
5. cleaning steps,
6. whether the table is raw, cleaned, merged, or derived.

## Expected inputs

| Dataset | Role | Status |
|---|---|---|
| SPARC rotation-curve data | Galaxy rotation curves and baryonic components | pending |
| SPARC galaxy properties table | Distances, luminosities, gas/stars, morphology where available | pending |
| Stellar-population age source | Age proxy or derived stellar ages | pending |
| Environment catalog | Group/satellite/field controls | pending |
| Surface-brightness / morphology variables | Confound controls | pending |

## Data handling policy

- Prefer source links and scripts over committing large raw datasets if licensing is uncertain.
- Commit small cleaned/derived tables only when license allows and provenance is explicit.
- Keep exploratory derived files separate from publication-ready files.
- Include a column dictionary for every derived table.

## Planned derived tables

```text
sparc_age_dm_merged.csv
correlation_table.csv
bootstrap_results.csv
regression_controls.csv
```

Each derived table should eventually have a matching metadata note.
