# Parameter Log — Parent-Child Directional Transfer

**Status:** Parameter scaffold / v0.1  
**Related files:**

```text
simulations/parent-child-transfer/real-space-bounce-transfer-v4-1.md
simulations/parent-child-transfer/kernel-robustness-summary.md
simulations/parent-child-transfer/null-models.md
```

**Claim level:** Reproducibility scaffold. No physical claim.

---

## Purpose

This file defines the parameter-recording structure for the parent-child directional-transfer simulation branch.

The purpose is to prevent informal result drift and make future simulation runs reproducible.

Every result should eventually have:

```text
run_id
script/notebook version
random seed
parent-field parameters
transfer-kernel parameters
metric definitions
null model used
alignment outputs
verdict
artifact links
```

---

## Current v4.0 / v4.1 Summary Values

### v4.0 Real-Space Split Result

| Quantity | Value | Notes |
|---|---:|---|
| anisotropy ratio, signal | 0.648 | Diagnostic only; kernel-contaminated. |
| anisotropy ratio, null | 1.225 | Null exceeded signal on ratio metric. |
| anisotropy ratio delta | -0.577 | Ratio metric failed. |
| quadrupole alignment, signal | 0.968 | Strong alignment with parent axis. |
| quadrupole alignment, null | 0.073 | Near-random alignment. |
| quadrupole alignment delta | +0.894 | Strong positive signal. |

### v4.1 Kernel Robustness Scan

| Quantity | Value | Notes |
|---|---:|---|
| kernel configurations tested | 20 | Reported robustness grid. |
| strong positive deltas | 19 | Threshold: delta > 0.1. |
| weak positive deltas | 1 | Positive but below strong threshold. |
| negative deltas | 0 | No null-beating-signal cases. |
| mean alignment delta | ~+0.583 | Approximate reported mean. |

---

## Required Run Log Schema

Future runs should be recorded using this table structure.

| run_id | seed | model_version | parent_type | A_aniso | sigma_parallel | sigma_perp | kernel_type | null_type | alignment_signal | alignment_null | delta | verdict | artifact |
|---|---:|---|---|---:|---:|---:|---|---|---:|---:|---:|---|---|
| TBD | TBD | v4.1 | anisotropic | TBD | TBD | TBD | real-space | isotropic-parent | TBD | TBD | TBD | pending | TBD |

---

## Parameter Definitions

| Parameter | Meaning | Required? | Notes |
|---|---|---|---|
| `run_id` | Unique identifier for run. | yes | Use date/version prefix when possible. |
| `seed` | Random seed. | yes | Required for reproducibility. |
| `model_version` | Simulation architecture version. | yes | Example: `v4.0`, `v4.1`, `v4.2`. |
| `parent_type` | Parent-field type. | yes | anisotropic, isotropic, phase-randomized, rotated, etc. |
| `A_aniso` | Parent anisotropy amplitude. | yes | Needed for sweep tests. |
| `sigma_parallel` | Kernel width parallel to parent axis. | yes | If applicable. |
| `sigma_perp` | Kernel width perpendicular to parent axis. | yes | If applicable. |
| `kernel_type` | Transfer-kernel family. | yes | real-space Gaussian, anisotropic, near-isotropic, etc. |
| `null_type` | Null/control used. | yes | axis-shuffle, isotropic-parent, phase-randomized, etc. |
| `alignment_signal` | Signal-child alignment score. | yes | Use frozen metric definition. |
| `alignment_null` | Null alignment score. | yes | Matched null comparison. |
| `delta` | `alignment_signal - alignment_null`. | yes | Primary statistic. |
| `verdict` | Pass/fail/diagnostic. | yes | Avoid overclaiming. |
| `artifact` | Link to CSV, notebook, chart, or screenshot. | yes | Must point to repo artifact when available. |

---

## Metric Definitions

### Primary Metric

```text
delta_alignment = alignment_signal - alignment_null
```

Primary verdict thresholds for exploratory work:

| Delta range | Exploratory verdict |
|---:|---|
| `delta <= 0` | negative / fail |
| `0 < delta <= 0.1` | weak positive |
| `delta > 0.1` | strong positive |

These thresholds are provisional and should be replaced by statistical thresholds after multi-seed ensembles.

### Diagnostic Metrics

Record but do not use as primary:

```text
anisotropy_ratio
along_axis_power
perpendicular_power
raw_quadrupole_strength
axis_recovery_error
low_ell_power_proxy
non_gaussianity_proxy
```

The v4.0 result showed that anisotropy ratio can be contaminated by transfer-kernel smoothing geometry.

---

## Required Artifact Locations

Future committed outputs should use:

```text
data/parent-child-transfer/kernel_scan_v4_1.csv
notebooks/parent_child_directional_transfer.ipynb
figures/parent-child-transfer/
simulations/parent-child-transfer/src/
```

---

## Minimum Reproducibility Requirements

Before any observational comparison, each result must include:

1. source code or notebook;
2. random seed;
3. parameter table;
4. full null model description;
5. metric definition;
6. raw output CSV;
7. summary plot or table;
8. statement of whether the run was exploratory or pre-registered.

---

## Next Planned Runs

| Priority | Run type | Purpose | Status |
|---:|---|---|---|
| 1 | multi-seed kernel grid | Test whether v4.1 survives seed variation. | pending |
| 2 | isotropic-parent null | Test kernel/metric artifact risk. | pending |
| 3 | axis-shuffle null | Test true-axis specificity. | pending |
| 4 | phase-randomized parent | Preserve spectrum but destroy coherent orientation. | pending |
| 5 | rotated-parent control | Test whether child axis follows parent rotation. | pending |
| 6 | anisotropy sweep | Find detection threshold in `A_aniso`. | pending |
| 7 | CMB-facing statistic freeze | Define statistic before observed CMB comparison. | pending |

---

## Claim Boundary

Use:

> The parameter log records exploratory and future reproducible runs for the parent-child directional-transfer branch.

Avoid:

> Parameter logging upgrades an exploratory result into physical evidence.
