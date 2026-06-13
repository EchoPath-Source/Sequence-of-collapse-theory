# P1 — PRELIMINARY Age-Dependent Galactic Rotation Curves in SPARC

## Subtitle

A PRELIMINARY quantitative, hypothesis-generating test using the SPARC database

## Roadmap status

**Submission-candidate text in progress — PRELIMINARY, not confirmed/proven.**

Roadmap target: **MNRAS or Physical Review Letters**.

## Purpose

This is the canonical P1 folder from the March 2026 SOC Publication Roadmap.

P1 is intended as a conservative entry point into peer-reviewed literature. It tests whether galaxies with different stellar-population age proxies show different inferred outer rotation-curve discrepancy in the derived SPARC table. The current result is an empirical, submission-candidate analysis scaffold; it is not a validated detection of a new force, not proof of Sequence of Collapse Theory (SoCT), and not proof of memory gravity.

## Core preliminary claim

> In the committed derived SPARC table, `age_best` has a modest positive marginal association with `fdm_outer_mean`, but the association is attenuated under the full structural-control model and should be treated as hypothesis-generating only.

The current script-generated CSV outputs report:

- marginal Pearson association: `r ≈ 0.201`, `p ≈ 0.0077`, `N = 175`;
- marginal Spearman association: `rho ≈ 0.211`, `p ≈ 0.0050`, `N = 175`;
- full structural-control OLS model `fdm_outer_mean ~ age_best + logVmax + logRmax + logSB0`: `beta_age ≈ 0.0184`, with the age-coefficient p-value attenuated to `p ≈ 0.162`;
- full structural-control partial correlation for `age_best` and `fdm_outer_mean` controlling `logVmax + logRmax + logSB0`: `partial_r ≈ 0.107`, `p ≈ 0.159`.

This attenuation is central to the claim boundary: the analysis may motivate follow-up work, but it does not prove SoCT, memory gravity, or any nonstandard gravitational mechanism.

## Key roadmap result — revised claim boundary

Earlier roadmap language described Prediction 3 as confirmed from SPARC. For this submission-candidate pass, that wording is replaced by the following conservative boundary:

> The current SPARC age/fDM analysis is PRELIMINARY and hypothesis-generating. It reports a candidate age-associated trend in derived outer dark-matter fraction, with substantial sensitivity to structural controls. It does not confirm or prove SoCT, memory gravity, dark-matter replacement, or any other nonstandard gravitational mechanism.

## Existing support noted in roadmap

- Nelson 2024: baryon-only models outperform ΛCDM at high redshift.
- Genzel 2017: declining rotation curves at z > 1.
- High-redshift companion paper exists on Medium and should cite / be cited by this paper.

These context items remain background motivation only. They are not treated here as proof of the SPARC P1 hypothesis.

## Reproducible outputs

Run the canonical analysis script from the repository root:

```bash
python papers/p1-age-dependent-rotation-curves-sparc/analysis/sparc_age_fdm_analysis.py
```

The text/CSV outputs committed for this pass are:

- `results/SPARC_age_fdm_correlations.csv`;
- `results/SPARC_age_fdm_partial_correlations.csv`;
- `results/SPARC_age_fdm_regression_models.csv`;
- `results/SPARC_age_fdm_binned_bootstrap.csv`.

The same script also generates `results/SPARC_age_vs_fdm_scatter.png`. That scatter plot is intentionally not committed in this pass because binary artifacts are handled separately.

## What to add before publication

1. Full independent reproduction and audit of the derived SPARC table.
2. Explicit provenance for the age proxy and uncertainty model.
3. Sensitivity checks for structural controls, stellar-population confounds, selection effects, and outliers.
4. Comparison to standard ΛCDM/galaxy-formation expectations for the same sample.
5. Preregistered criteria for which control model is considered primary.
6. Paper draft PDF or Markdown generated from committed text sources.
7. Figure artifacts handled through the repository's binary-artifact process rather than this text/CSV pass.

## Relationship to earlier scaffold

Earlier repo folder:

```text
papers/p1-memory-field-gravity-sparc/
```

That folder remains as a broader theory/protocol support package. This folder is the roadmap-canonical P1 paper folder.

## OSF action

Create or update OSF project:

```text
SOC-P1: Age-Dependent Rotation Curves
```

Upload, after audit and according to repository artifact policy:

- paper draft PDF;
- SPARC analysis data;
- analysis code;
- figures;
- confidence interval tables;
- preregistration notes if new analyses are run.
