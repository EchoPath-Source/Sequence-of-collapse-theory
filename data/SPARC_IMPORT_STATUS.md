# SPARC Import Status

## Purpose

Track the import and reproducibility status for the P1 SPARC age-dependent rotation-curve analysis.

Canonical paper track:

```text
papers/p1-age-dependent-rotation-curves-sparc/
```

Support folder:

```text
papers/p1-memory-field-gravity-sparc/
```

## Current status

```text
Status: PARTIAL / PRELIMINARY
```

The repository roadmap identifies P1 as data-in-hand / write-now, but publication-grade use requires a complete reproducibility packet with canonical inputs, derived tables, figures, scripts/notebooks, and uncertainty estimates.

## Required inputs

Track whether each artifact is present and validated:

| Artifact | Status | Notes |
|---|---|---|
| SPARC source catalog reference | PARTIAL | Record exact citation/source and version. |
| SPARC photometry / rotation-curve table inputs | PARTIAL | Confirm canonical local paths. |
| Age or stellar-population proxy table | PARTIAL | Confirm source, units, joins, and missing values. |
| Derived inner/outer radial decomposition table | PARTIAL | Confirm reproducible generation path. |
| Derived f_DM / memory-field proxy table | PARTIAL | Confirm column definitions and uncertainty handling. |
| Bootstrap or confidence interval outputs | PARTIAL | Required before strong paper claims. |
| Figures for manuscript | PARTIAL | Mark preliminary until scripts regenerate them. |
| Notebook/script that regenerates outputs | PARTIAL | Must be canonicalized before publication use. |

## Required reproducibility packet

P1 should eventually include:

```text
papers/p1-age-dependent-rotation-curves-sparc/REPRODUCIBILITY.md
notebooks or scripts used for the analysis
tracked derived CSV outputs
figure generation notes or scripts
confidence interval / bootstrap outputs
claim boundary for SPARC-specific findings
```

## Claim boundary

Current safe language:

> The SPARC track explores whether age-dependent rotation-curve structure or inferred outer mass discrepancy can be modeled with a memory-field-inspired effective-gravity scaffold.

Avoid until fully reproduced:

- claiming dark matter is replaced,
- claiming SPARC proves SoCT,
- claiming memory fields are physically confirmed,
- claiming publication-grade confidence before scripts, inputs, and intervals are complete.

## Next actions

1. Identify canonical raw/source input paths.
2. Identify canonical derived output paths.
3. Add checksums where practical.
4. Confirm scripts/notebooks that regenerate each derived table.
5. Add confidence intervals and figure regeneration path.
6. Update P1 `REPRODUCIBILITY.md` when packet is complete.
