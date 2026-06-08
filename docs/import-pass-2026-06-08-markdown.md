# Markdown Import Pass — 2026-06-08

**Purpose:** record the Markdown import pass performed after the current-state audit identified several files as `RECEIVED / NOT IMPORTED`.

## Imported files

| Source artifact | Imported repo path | Track | Status |
|---|---|---|---|
| `PNT_Working_Paper.docx` | `papers/pnt-dark-energy-hubble-window/pnt-working-paper-v0-1.md` | P5 / PNT | Markdown source imported; claim-boundary note added. |
| `causal_inversion.docx` | `papers/p6-black-holes-memory-compression-nodes/source/causal-inversion-hypothesis.md` | P6 / CIH | Markdown source imported; claim-boundary note added. |
| `kerr_to_cosmos.docx` | `papers/p6-black-holes-memory-compression-nodes/source/kerr-to-cosmos.md` | P6 / Kerr-to-Cosmos | Markdown source imported; claim-boundary note added. |
| `engramon_scale.docx` | `papers/p6-black-holes-memory-compression-nodes/source/engramon-scale.md` | P6 / Engramon | Markdown source imported; claim-boundary note added. |
| `OSF_Preregistration_Excerpt_v1.1_clean.docx` | `papers/p4-soc-mzi-awareness-modulated-decoherence/preregistration/OSF_Preregistration_Excerpt_v1.1_clean.md` | P4 / SOC-MZI | Preregistration excerpt imported; duplicate DOCX hash matched. |
| `Gravity as Accumulated Collapse History.PDF` | `papers/p1-age-dependent-rotation-curves-sparc/source/gravity-as-accumulated-collapse-history.md` | P1 / SPARC | Public-facing source article imported with empirical claim boundary. |
| `OSF_Home_Page_Book_of_Sacred_Science.md` | `osf/book-of-sacred-science-home-page.md` | OSF / Context | OSF source-context page imported; marked philosophical/theological context. |
| `OSF_Prereg_SoCT_PM_v061_and_SPARC_Plan.pdf` and `OSF_Prereg_Combined_v061.pdf` | `osf/prereg/soct-pm-v061-sparc-plan.md` | P1 / OSF / SoCT-PM | Markdown extraction/summary imported; full binary import not performed. |

## Duplicate handling

The two uploaded preregistration excerpt DOCX files were byte-identical:

```text
OSF_Preregistration_Excerpt_v1.1_clean.docx
OSF_Preregistration_Excerpt_v1.1_clean-1.docx
```

Only one Markdown import was created.

## Import boundaries

This pass intentionally avoids claiming empirical validation. These imports move received source material into repo-tracked Markdown form. They do not replace reproducible notebooks, scripts, tables, figures, or peer review.

## Still pending from audit

Highest-priority missing or not-yet-imported items remain:

- `sparc_age_fdm_analysis.py`
- `SPARC_age_fdm_correlations.csv`
- `SPARC_age_fdm_partial_correlations.csv`
- `SPARC_age_fdm_binned_bootstrap.csv`
- `mass_proxy_comparison.csv`
- `paper_grade_analysis.png`
- `sparc_fdm_vs_age_full_analysis.png`
- `sparc_mass_controlled_analysis.png`
- `repo_bundle_sparc_pnt_void.zip`
- `SOC MZI Visibility Decay Simulation.py`
- `environment_H0_analysis.png`
- Pantheon+ covariance matrix / SN table / environment labels

## Recommended next pass

1. Import any available SPARC analysis scripts and CSV outputs.
2. Import figure PNGs if available and internally generated.
3. Add P6 `open-issues.md` to track known tensions.
4. Reconcile imported source files with canonical P1-P7 manuscript folders.
5. Update `docs/repo-audit-current-state.md` after all received artifacts are imported.
