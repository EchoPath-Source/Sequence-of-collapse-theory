# Pantheon Import Status

## Purpose

Track the import and reproducibility status for Pantheon+ / environment-dependent H0 analysis used by the P5 Hubble-tension memory-gradient track.

Canonical paper track:

```text
papers/p5-hubble-tension-memory-gradient/
```

Support package:

```text
papers/pnt-dark-energy-hubble-window/
```

## Current status

```text
Status: PARTIAL / BLOCKED UNTIL CANONICAL INPUTS ARE VERIFIED
```

The empirical exploration package identifies Pantheon+ as a primary observational track with the directional expectation:

```text
Pantheon+: H0_void > H0_filament
```

Publication-grade use requires verified SN-table input, covariance input, environment labels, row-order validation, scripts/notebooks, derived outputs, and claim boundaries.

## Required inputs

| Artifact | Status | Notes |
|---|---|---|
| Pantheon+ SN table | MISSING / VERIFY | Must contain required columns and canonical row ordering. |
| Full covariance matrix | PARTIAL / VERIFY | Must match SN-table ordering and expected dimensions. |
| Environment labels | MISSING / VERIFY | Void/filament/unclassified labels and method required. |
| DESI environment-label scaffold | PLANNED | See `papers/p5-hubble-tension-memory-gradient/DESI_ENVIRONMENT_QUERY_PLAN.md`. |
| DESI reproducibility/data contract | PRESENT | See `data/desi/README.md` and `notebooks/desi/DESI_ENVIRONMENT_NOTEBOOK_PLAN.md`. No DESI labels generated yet. |
| DESI column semantics | PRESENT / SMOKE-QUERY SEMANTICS LOCKED | See `data/desi/DESI_DR1_COLUMN_SEMANTICS.md`. Live data-type/null inspection and optional VAC field/cardinality checks remain pending. |
| DESI tiny smoke query | READY / NOT YET RUN | `data/desi/DESI_DR1_SMOKE_QUERY_v0_1.sql`; plumbing validation only. |
| Row-order validation | MISSING | Required before covariance-aware fit. |
| Diagnostic script/notebook | PARTIAL | Must document command, inputs, outputs, and blocked states. |
| Derived result CSVs | MISSING / CONDITIONAL | Commit only if diagnostic run completes cleanly. |
| Figure outputs | MISSING / CONDITIONAL | Regenerate from derived outputs only. |

## Required reproducibility packet

P5/Pantheon should eventually include:

- raw-input staging guide,
- input checksums where possible,
- covariance validation note,
- environment-label methodology,
- row-order validation result,
- covariance-aware diagnostic output,
- derived result CSVs,
- uncertainty estimates,
- figure regeneration path,
- claim boundary.

For the DESI branch specifically, schema/column verification and reproducible environment-label generation must be completed before Pantheon+ coordinate crossmatching begins.

## Claim boundary

Current safe language:

> The Pantheon+ track proposes a preregistered environment-dependent H0 test comparing void and filament supernova subsets under a memory-gradient interpretation.

Avoid until fully reproduced:

- claiming the Hubble tension is solved,
- claiming void expansion proves SoCT,
- claiming environment-dependent H0 without completed row-order/covariance validation,
- claiming publication-grade results from incomplete inputs.

## Next actions

1. Stage canonical Pantheon+ SN table.
2. Stage/verify full covariance matrix.
3. Preserve the locked DESI smoke-query column semantics in `data/desi/DESI_DR1_COLUMN_SEMANTICS.md`.
4. Run only the staged 25-row DESI sky-patch smoke query and inspect live data types, null behavior, provenance, and sample cuts.
5. Inspect optional VAC schemas/join cardinality before any `stellar_mass_emline` or `emfit` join is used.
6. Define and validate the DESI density/environment methodology.
7. Generate DESI-derived environment labels only after schema and quality checks are stable.
8. Crossmatch Pantheon+ coordinates only after the DESI environment-label catalog exists reproducibly and the coordinate source is explicitly frozen.
9. Stage environment-label table and methodology.
10. Run row-order validation.
11. Run covariance-aware diagnostic.
12. Commit derived outputs only after clean run completion.
13. Update P5 reproducibility notes when outputs exist.
