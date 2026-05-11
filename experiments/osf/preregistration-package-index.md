# OSF Preregistration Package Index

**Status:** Import scaffold / provenance tracker  
**Purpose:** Track OSF-facing SoCT preregistration materials and split them into reproducible experiment files.

---

## Source Files

| Source | Import status | Intended repo use |
|---|---|---|
| `OSF_Home_Page_Book_of_Sacred_Science.md` | direct import target | OSF landing page / project overview |
| `OSF_Preregistration_Excerpt_v1.1_clean.docx` | direct import target | clean preregistration excerpt |
| `OSF_Prereg_SoCT_PM_v061_and_SPARC_Plan.pdf` | split import target | SoCT-PM prereg + SPARC analysis plan |
| `OSF_Prereg_Combined_v061.pdf` | archive/direct import target | combined preregistration snapshot |

---

## Package Goal

The OSF package should convert broad SoCT claims into preregistered, adversarially testable study plans.

Priority lanes:

1. Conscious-access / MZI visibility protocol.
2. Modified double-slit storage/deletion/access protocol.
3. SPARC collapse-memory gravity analysis plan.
4. Preregistered exclusion criteria, SESOI, and statistical analysis plan.

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
- blinding plan;
- randomization plan;
- deletion/storage/access protocol where relevant;
- SESOI or minimum effect size of interest;
- sample size or power rationale;
- analysis script version/hash;
- null interpretation;
- falsification/weakening criteria.

---

## Current Status

This index is a scaffold. The raw OSF materials are not yet fully converted into Markdown.

Immediate next step:

> Convert the clean preregistration excerpt and combined v061 materials into versioned Markdown files, preserving original wording where experimental commitments matter.
