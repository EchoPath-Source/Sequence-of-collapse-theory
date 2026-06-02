# Null Models — Parent-Child Directional Transfer

**Status:** Required controls plan / v0.1  
**Related files:**

```text
simulations/parent-child-transfer/real-space-bounce-transfer-v4-1.md
simulations/parent-child-transfer/kernel-robustness-summary.md
```

**Claim level:** Methodology design only. No physical claim.

---

## Purpose

This document defines the null models required before the parent-child directional-transfer branch can move beyond exploratory toy modeling.

The v4.1 kernel scan reported robust positive quadrupole-alignment deltas across tested kernels. The next question is whether this signal survives stricter controls.

Primary risk:

```text
The transfer kernel, metric, or analysis pipeline may generate apparent alignment even when the parent field contains no meaningful directional memory.
```

This file defines the controls needed to test that risk.

---

## Primary Statistic

The primary statistic remains:

```text
delta_alignment = alignment_signal - alignment_null
```

Where alignment is the cosine-like agreement between the recovered child quadrupole axis and the predefined parent collapse axis.

The statistic must be defined before comparing to observed CMB axes.

---

## Null Model 1 — Isotropic Parent Field

### Purpose

Test whether the pipeline produces alignment even when the parent field has no preferred direction.

### Procedure

1. Generate an isotropic parent field.
2. Apply the same real-space transfer kernel grid.
3. Recover child quadrupole axes.
4. Compare recovered axes to the reference axis.

### Expected result if signal is real

```text
alignment_isotropic_parent approximately random
mean_delta near 0
```

### Failure mode

If the isotropic parent produces strong alignment, the kernel or metric may be imposing the signal.

---

## Null Model 2 — Axis-Shuffle Null

### Purpose

Test whether the result depends on the true parent axis or would appear for arbitrary axis choices.

### Procedure

1. Keep the signal child field fixed.
2. Randomize or shuffle the reference parent axis.
3. Compute alignment against each shuffled axis.
4. Build a shuffled-axis distribution.

### Expected result if signal is real

```text
alignment_true_axis > alignment_shuffled_axis_distribution
```

### Required output

```text
p_axis_shuffle
z_axis_shuffle
percentile_true_axis
```

---

## Null Model 3 — Phase-Randomized Parent

### Purpose

Preserve the parent power spectrum while destroying coherent spatial orientation.

### Procedure

1. Transform the parent field to spectral space.
2. Preserve amplitude spectrum.
3. Randomize phases.
4. Transform back to real space.
5. Apply the same transfer kernel.
6. Measure quadrupole alignment.

### Expected result if signal is real

```text
phase_randomized_delta << signal_delta
```

### Failure mode

If phase-randomized parents retain similar alignment, the signal may be caused by the power spectrum or kernel rather than coherent memory orientation.

---

## Null Model 4 — Rotated-Parent Control

### Purpose

Test whether child orientation rotates consistently with parent orientation.

### Procedure

1. Rotate the parent field by known angles.
2. Apply the same transfer kernel.
3. Recover child quadrupole axis.
4. Check whether recovered child axis follows the imposed parent rotation.

### Expected result if signal is real

```text
axis_child_rotated follows axis_parent_rotated
```

### Required output

```text
rotation_angle
recovered_axis_angle
axis_recovery_error
```

---

## Null Model 5 — Kernel-Only Artifact Control

### Purpose

Test whether the transfer kernel alone can create alignment from unstructured input.

### Procedure

1. Use white noise or isotropic Gaussian input.
2. Apply anisotropic and near-isotropic kernels.
3. Recover child quadrupole axis.
4. Compare to kernel axis and arbitrary parent-axis reference.

### Expected result if signal is real

Kernel-only fields should not reproduce the same signal strength as structured parent fields.

### Failure mode

If kernel-only runs strongly align with the reference axis, the signal may be a kernel artifact.

---

## Null Model 6 — Random Seed Ensemble

### Purpose

Test whether the v4.1 result was specific to one stochastic realization.

### Procedure

Run the full kernel grid across many seeds.

Minimum target:

```text
N_seeds >= 20
```

Better target:

```text
N_seeds >= 100
```

### Required outputs

```text
mean_delta
std_delta
median_delta
min_delta
max_delta
fraction_positive
fraction_strong_positive
failure_seed_list
```

---

## Null Model 7 — Parent Anisotropy Sweep

### Purpose

Find the minimum parent anisotropy needed for reliable detection.

### Procedure

Vary parent anisotropy amplitude:

```text
A_aniso = 0, low, medium, high
```

For each amplitude:

1. run all kernels;
2. run all nulls;
3. compute alignment recovery;
4. estimate threshold.

### Expected result if signal is real

```text
alignment_delta increases with A_aniso
```

A flat response would indicate possible metric or kernel bias.

---

## Acceptance Criteria for Next Stage

The branch may proceed toward observation-facing CMB tests only if:

1. true-axis alignment beats axis-shuffle nulls;
2. isotropic-parent and kernel-only controls do not reproduce the signal;
3. phase randomization weakens or destroys the signal;
4. rotated-parent controls recover the imposed axis;
5. multi-seed tests remain mostly positive;
6. the statistic is frozen before real CMB comparison.

---

## Required Results Table

Future output should include:

| Test | Expected if real | Current status | Pass/fail |
|---|---|---|---|
| Isotropic parent | near-random alignment | pending | TBD |
| Axis-shuffle null | true axis above shuffled distribution | pending | TBD |
| Phase-randomized parent | weakened alignment | pending | TBD |
| Rotated-parent control | recovered axis follows rotation | pending | TBD |
| Kernel-only artifact | no strong inherited-axis signal | pending | TBD |
| Multi-seed ensemble | mostly positive deltas | pending | TBD |
| Anisotropy sweep | monotonic response to parent anisotropy | pending | TBD |

---

## Repo-Safe Summary

> The parent-child transfer signal cannot be considered robust until it survives isotropic-parent, axis-shuffle, phase-randomized, rotated-parent, kernel-only, multi-seed, and anisotropy-sweep null tests.

---

## Claim Boundary

Use:

> Null models are being defined to determine whether the v4.1 directional-transfer signal reflects parent-field structure or analysis/kernel artifacts.

Avoid:

> The null tests are a formality because the v4.1 result is already confirmed.
