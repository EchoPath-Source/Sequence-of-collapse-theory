# Kernel Robustness Summary — Parent-Child Directional Transfer v4.1

**Status:** Exploratory robustness note  
**Related file:** `simulations/parent-child-transfer/real-space-bounce-transfer-v4-1.md`  
**Claim level:** Toy-model robustness result only; not empirical cosmology.

---

## Purpose

This note preserves the v4.1 kernel robustness result for the parent-child directional transfer branch.

The test asks whether the reported quadrupole-axis alignment survives changes in transfer-kernel shape.

If the effect disappears when the kernel changes, the signal is likely a kernel artifact. If the effect remains positive across kernel choices, the signal is more likely tied to orientation already present in the parent field.

---

## Primary Robustness Question

```text
Does child-field quadrupole alignment remain above null across different transfer kernels?
```

This is the correct robustness question because the hypothesis concerns **orientation inheritance**, not merely total anisotropic power.

---

## Reported Result

```text
20 kernel configurations tested
19/20 strong positive deltas (> 0.1)
1/20 weak positive delta
0/20 negative deltas
mean alignment delta approximately +0.583
```

Key interpretation:

> The alignment signal remains positive across the tested kernel grid, including near-isotropic kernels.

---

## Why This Matters

The most important result is not a single high alignment score. The important result is the absence of negative cases across the tested kernel set.

A kernel artifact would be expected to fail or reverse under some kernel choices, especially near-isotropic kernels where the transfer kernel barely distinguishes directions.

Instead, the reported scan showed:

```text
signal > null across all tested configurations
```

This suggests, within the toy model, that directional information resides in the parent field and is not purely imposed by the transfer operator.

---

## Metric Hierarchy

### Primary Metric

```text
quadrupole-axis alignment delta
```

Definition:

```text
delta = alignment_signal - alignment_null
```

This metric answers:

```text
Does the child field point along the parent collapse axis more than a null field does?
```

### Secondary / Diagnostic Metrics

- anisotropy power ratio;
- along-axis vs perpendicular variance;
- raw quadrupole strength;
- non-Gaussianity proxies;
- small-scale power leakage.

The anisotropy ratio is not a primary metric because it can be contaminated by smoothing geometry.

---

## Current Scientific Statement

Use:

> In the v4.1 real-space bounce-transfer toy model, parent-axis directional inheritance remained positive across all 20 tested kernel configurations, with 19/20 configurations exceeding the strong-positive threshold and mean alignment delta of approximately +0.583 above null.

Avoid:

> Kernel robustness proves the physical universe inherited structure from a parent universe.

---

## Interpretation Boundaries

This scan supports:

1. real-space transfer is a better architecture than the earlier k-space tests for this question;
2. quadrupole alignment is the correct primary metric for directional inheritance;
3. the tested toy model can preserve parent-field orientation across kernel variation;
4. the result justifies multi-seed and expanded-null follow-up.

This scan does not establish:

1. physical parent universes;
2. black-hole bounce cosmology;
3. dark matter as leaked gravity;
4. dark energy as post-bounce pressure;
5. a CMB anomaly match.

---

## Required Follow-Up Table

Future versions should include a table with:

| Seed | sigma_parallel | sigma_perp | kernel type | alignment_signal | alignment_null | delta | verdict |
|---|---:|---:|---|---:|---:|---:|---|
| TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

A CSV version should be added under:

```text
data/parent-child-transfer/kernel_scan_v4_1.csv
```

---

## Next Tests

### 1. Multi-Seed Robustness

Run the full kernel grid across many random seeds.

Minimum useful target:

```text
N_seeds >= 20
```

Better target:

```text
N_seeds >= 100
```

Report:

```text
fraction_positive
mean_delta
std_delta
worst_case_delta
seed_failure_cases
```

### 2. Parent Anisotropy Sweep

Vary parent anisotropy amplitude.

Goal:

```text
Find the minimum anisotropy needed for reliable axis recovery.
```

### 3. Kernel-Only Artifact Control

Run the anisotropic kernel on an isotropic parent field and test whether alignment appears without parent orientation.

### 4. Axis-Shuffle Null

Randomize the reference parent axis while keeping the child field fixed.

### 5. CMB-Facing Pre-Registration

Before any comparison to observed CMB axes, define:

- predicted axis rule;
- amplitude statistic;
- multipole range;
- look-elsewhere correction;
- foreground/systematics exclusion plan.

---

## Repo-Safe Summary

> The v4.1 kernel robustness scan provides exploratory toy-model support that directional memory transfer can survive real-space kernel variation. It motivates further multi-seed, null-model, and observable-facing tests but does not confirm physical parent-child universe transfer.
