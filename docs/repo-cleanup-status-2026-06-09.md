# Repo Cleanup Status — 2026-06-09

**Repository:** `EchoPath-Source/Sequence-of-collapse-theory`  
**Purpose:** Current status snapshot after cross-thread cleanup and import review.

---

## Executive Summary

The repository has moved from a documentation scaffold into a structured research archive with a publication roadmap, prediction tracker, empirical tracks, and separated exploratory branches.

The main remaining gap is no longer folder structure. The main remaining gap is **reproducibility artifacts**:

- runnable notebooks/scripts,
- final executable code snapshots,
- generated CSV outputs,
- figure source-data links,
- provenance indexes for uploaded source documents.

---

## What Is Now In Place

### 1. Publication roadmap

The README now defines a seven-paper roadmap:

1. P1 — Age-Dependent Galactic Rotation Curves / SPARC
2. P2 — High-Redshift Disk Galaxies / Time-Dependent Gravity
3. P3 — SOC from Concept to Equation
4. P4 — SOC-MZI / Awareness-Modulated Decoherence
5. P5 — Hubble Tension as Memory Field Gradient
6. P6 — Black Holes as Memory Compression Nodes
7. P7 — Unified SoCT Framework

### 2. Prediction tracker

`PREDICTIONS.md` now separates:

- proposed predictions,
- in-progress analyses,
- preregistered tests,
- preliminary calculations,
- replication-needed results,
- constrained/falsified branches,
- speculative/philosophical extensions.

### 3. SPARC observational package

The SPARC track now contains:

```text
observations/sparc/README.md
observations/sparc/analyses/current-status-note.md
observations/sparc/results/outer_mass_discrepancy_analysis.md
observations/sparc/results/inner_outer_radial_decomposition_summary.md
observations/sparc/results/inner_outer_correlation_summary.csv
observations/sparc/data/sparc_wise_inner_outer_fdm_split.csv
observations/sparc/scripts/README.md
observations/sparc/tables/README.md
```

Status:

- derived result summaries are present,
- derived split CSV is present,
- reproducibility script/notebook is still missing.

### 4. Pantheon+ / H0 environment scaffold

The Pantheon+ track contains:

```text
experiments/cosmology/pantheon-environment-h0-test.md
data/pantheon/README.md
data/pantheon/covariance-notes.md
data/pantheon/environment-labels-schema.md
```

Status:

- prereg-style test scaffold is present,
- covariance ingestion requirements are documented,
- environment-label schema is documented,
- real covariance-aware output is not yet committed.

### 5. Memory-field PM simulation hub

The PM simulation line contains:

```text
simulations/memory-field-pm/README.md
simulations/memory-field-pm/validation/v061_acceptance_summary.md
simulations/memory-field-pm/outputs/README.md
simulations/memory-field-pm/figures/README.md
```

Status:

- v0.6.1 is marked as the active reference line,
- validation summary is present,
- output and figure landing zones are now present,
- final code and generated outputs still need to be added or verified.

### 6. Parent-child / recursive-universe exploratory separation

Exploratory structure now includes:

```text
exploratory/recursive-universe/README.md
exploratory/recursive-universe/notes/recursive-universe-status-note.md
exploratory/recursive-universe/code/README.md
exploratory/recursive-universe/figures/README.md
simulations/parent-child-transfer/real-space-bounce-transfer-v4-1.md
simulations/parent-child-transfer/kernel-robustness-summary.md
```

Status:

- exploratory status is correctly separated from validated evidence,
- parent-child transfer summaries are present,
- multi-seed / expanded-null follow-up tests are still missing.

---

## What Is Still Missing

### Critical Missing Artifacts

#### SPARC reproducibility

Still needed:

```text
observations/sparc/scripts/reproduce_inner_outer_radial_decomposition.py
observations/sparc/scripts/reproduce_outer_mass_discrepancy.py
observations/sparc/notebooks/sparc_age_dm_analysis.ipynb
```

Minimum requirement:

- one runnable script that regenerates the committed CSV and summary tables from documented inputs.

#### Pantheon+ environment-H0 real-data run

Still needed:

```text
notebooks/pantheon_environment_h0_test.ipynb
data/pantheon/environment_labels.csv
data/pantheon/results/h0-environment-fit-summary.md
data/pantheon/results/permutation-test-summary.md
data/pantheon/results/jackknife-summary.md
```

Minimum requirement:

- covariance-aware fit using locked void/filament labels,
- no threshold tuning after seeing `Delta_H0`,
- redshift-matched bootstrap,
- environment-label permutation test,
- sky jackknife.

#### Memory-field PM source and outputs

Still needed:

```text
simulations/memory-field-pm/code/soct_pm_v061_final.py
simulations/memory-field-pm/outputs/v061_parameter_sweep_summary.csv
simulations/memory-field-pm/outputs/v061_dwarf_survival_by_environment.csv
simulations/memory-field-pm/outputs/v061_environment_hsplit_summary.csv
simulations/memory-field-pm/figures/*.png
```

Minimum requirement:

- executable v0.6.1 code snapshot,
- one baseline run,
- one memory-active run,
- output CSVs linked to figure captions.

#### Parent-child transfer follow-up

Still needed:

```text
simulations/parent-child-transfer/code/
simulations/parent-child-transfer/results/kernel_scan_v4_1.csv
simulations/parent-child-transfer/results/multiseed_kernel_scan_summary.csv
```

Minimum requirement:

- multi-seed version of the 20-kernel robustness scan,
- kernel-only artifact control,
- isotropic-parent null,
- axis-shuffle null.

#### Source corpus / uploaded artifact index

Still needed:

```text
docs/source-corpus/echo-labs-uploaded-artifacts-index.md
```

Purpose:

- index uploaded Echo Labs / Q-RRG / SOC files,
- classify whether each belongs in SoCT, EchoPath, EchoGenesis, or external/private archive,
- avoid bloating the SoCT repo with product/confidential documents.

---

## Current Cleanup Priorities

### Priority 1 — Reproducibility before more theory

Focus on executable artifacts:

1. SPARC reproduction script/notebook.
2. PM v0.6.1 code and output tables.
3. Pantheon+ covariance-aware notebook.

### Priority 2 — Update stale scaffolds

Files that should be updated soon:

```text
observations/sparc/README.md
docs/repo-map.md
README.md
osf/OSF_PROJECT_MAP.md
```

Reason:

- several files now say outputs are pending even though derived outputs have been partially committed.

### Priority 3 — Keep exploratory branches separated

Do not merge recursive-universe / parent-child-transfer results into core evidence claims until:

- multi-seed tests are complete,
- expanded nulls pass,
- a preregistered observable statistic exists.

---

## Claim Boundary Reminder

Safe language:

> The repo now preserves a structured SoCT research program with candidate empirical signals, preregistered tests, exploratory simulations, and a clear path toward reproducibility.

Avoid:

> The repo proves SoCT, rules out dark matter, proves observer collapse, or confirms parent-universe inheritance.

---

## Next Best Action

The next best technical action is to add a runnable SPARC reproduction script, because the SPARC package is the most mature empirical track and already has committed derived results.
