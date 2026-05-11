# OSF Preregistration Package Index

**Status:** Import scaffold / provenance tracker  
**Purpose:** Track OSF-facing SoCT preregistration materials and split them into reproducible experiment files.

---

## Source Files

| Source | Import status | Intended repo use |
|---|---|---|
| `OSF_Home_Page_Book_of_Sacred_Science.md` | direct import target | OSF landing page / project overview |
| `OSF_Preregistration_Excerpt_v1.1_clean.docx` | direct import target | clean consciousness-collapse preregistration excerpt |
| `OSF_Preregistration_Excerpt_v1.1_clean-1.docx` | duplicate/direct import check | duplicate or revised copy of v1.1 excerpt; verify before conversion |
| `OSF_Prereg_SoCT_PM_v061_and_SPARC_Plan.pdf` | split import target | SoCT-PM prereg + SPARC analysis plan |
| `OSF_Prereg_Combined_v061.pdf` | archive/direct import target | combined preregistration snapshot |
| `SOC_PreReg_Draft-3.docx` | direct import target | SPARC memory-field prereg draft |
| `SOC_Paper1_OSF_PreReg.md` | imported | formal Paper 1 SPARC preregistration Markdown |

---

## Imported Prereg Artifacts

```text
experiments/cosmology/sparc-memory-field-preregistration-v0-1.md
```

This file is now the strongest current prereg artifact for Paper 1. It contains:

- age-dependent rotation-curve hypothesis;
- memory-field Hamiltonian and kernel;
- SPARC data plan;
- inclusion/exclusion criteria;
- primary and secondary predictions;
- null/falsification criteria;
- statistical analysis plan;
- expected outcomes;
- figure and code plan.

---

## Package Goal

The OSF package should convert broad SoCT claims into preregistered, adversarially testable study plans.

Priority lanes:

1. SPARC age-dependent rotation-curve / memory-field preregistration.
2. Conscious-access / MZI visibility protocol.
3. Modified double-slit storage/deletion/access protocol.
4. Pantheon+ environment-dependent H0 protocol.
5. Preregistered exclusion criteria, SESOI, and statistical analysis plans.

---

## Repo Destination Plan

```text
experiments/osf/
  preregistration-package-index.md
  osf-home-page.md
  preregistration-excerpt-v1-1.md
  combined-prereg-v061.md
  soct-pm-prereg-v061.md

experiments/cosmology/
  sparc-analysis-plan.md
  sparc-memory-field-preregistration-v0-1.md
  pantheon-environment-h0-test.md

experiments/quantum/
  mach-zehnder-consciousness-test.md
  modified-double-slit-conscious-access.md
```

---

## Required Preregistration Fields

Each prereg protocol should eventually define:

- core hypothesis;
- primary endpoint;
- secondary endpoints;
- independent variables;
- covariates;
- exclusion criteria;
- blinding plan where applicable;
- randomization plan where applicable;
- deletion/storage/access protocol where relevant;
- SESOI or minimum effect size of interest;
- sample size or power rationale;
- analysis script version/hash;
- null interpretation;
- falsification/weakening criteria.

---

## Current Status

The SPARC Paper 1 preregistration has been converted into a repo artifact.

Still needed:

1. Convert the clean v1.1 consciousness-collapse preregistration excerpt.
2. Convert the combined v061 OSF preregistration snapshot.
3. Convert the OSF homepage text.
4. Reconcile duplicate `OSF_Preregistration_Excerpt_v1.1_clean` files.
5. Add notebook/code scaffolds for SPARC and Pantheon+ before analysis.
