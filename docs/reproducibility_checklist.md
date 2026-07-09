# SoCT Reproducibility Checklist

## Purpose

This checklist defines the minimum reproducibility packet required before a SoCT empirical or simulation result is treated as research-ready, publication-ready, or safe to translate into product-facing architecture language.

## Status labels

Use these labels consistently:

```text
MISSING       required source/input is not present
STAGED        source/input is present but not validated
PARTIAL       some inputs/results are present, but the packet is incomplete
BLOCKED       a required input or method is unavailable
PRELIMINARY   result exists but is not publication-grade
REPRODUCIBLE  another run can regenerate the result from tracked inputs/methods
PUBLICATION   ready for manuscript/supplement review
```

## Minimum packet for empirical tracks

A reproducible empirical track should identify:

- research question,
- canonical paper track,
- source dataset(s),
- exact input files,
- checksums or source URLs where practical,
- preprocessing steps,
- scripts or notebooks,
- software/runtime requirements,
- random seeds if used,
- derived outputs,
- figures,
- statistical method,
- confidence intervals or uncertainty estimates,
- null model or baseline,
- limitations,
- claim boundary.

## Minimum packet for simulation tracks

A reproducible simulation track should identify:

- model purpose,
- governing equations or algorithm,
- parameter ledger,
- initial conditions,
- random seeds,
- step counts / runtime settings,
- output schema,
- expected smoke-test behavior,
- known limitations,
- claim boundary.

## Required claim boundary fields

Every reproducibility note should include:

```text
What this supports:
What this does not support:
Empirical status:
Product-claim status:
Next required validation:
```

## Product handoff requirement

A result may inform product architecture only after:

1. Inputs are traceable.
2. Methods are documented.
3. Outputs can be regenerated or manually verified.
4. Limitations are explicit.
5. Product-safe translation avoids unproven physics claims.

## Canonical import/status docs

Use dedicated import/status docs for large tracks:

```text
data/SPARC_IMPORT_STATUS.md
data/PANTHEON_IMPORT_STATUS.md
papers/p1-age-dependent-rotation-curves-sparc/REPRODUCIBILITY.md
papers/p4-soc-mzi-awareness-modulated-decoherence/EXPERIMENT_STATUS.md
```

## Final rule

No empirical claim should graduate from exploratory to publication-facing until the relevant reproducibility packet is present and internally consistent.
