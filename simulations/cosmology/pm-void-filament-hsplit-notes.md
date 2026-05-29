# PM Void-Filament H-Split Simulation Notes

**Status:** scaffold / pending reproducible parameter logs  
**Claim level:** simulation-support only until code, seeds, and outputs are committed  
**Related experiment:** `experiments/cosmology/pantheon-environment-h0-test.md`

## Purpose

This note defines the simulation-output contract for particle-mesh or PM-style tests of the SoCT memory-field prediction:

```text
void environments should show higher effective expansion than filament environments
```

Primary qualitative prediction:

```text
H_void > H_filament
```

Primary measured statistic:

```math
\Delta_H = H_{void} - H_{filament}
```

or normalized form:

```math
\Delta_H/H_{bg}
```

## Model Boundary

The preferred conservative implementation is:

```text
Memory affects the gravity/source side only.
The background expansion remains Lambda-CDM unless explicitly testing an alternate model.
```

This keeps the simulation aligned with the Pantheon+ environment-H0 test and avoids mixing background-cosmology modifications with local/environmental memory effects.

## Required Parameter Log

Every PM run should export a machine-readable parameter log containing:

```text
run_id
random_seed
box_size
N_particles
mesh_resolution
initial_redshift
final_redshift
Omega_m
Omega_Lambda
H0_background
memory_alpha
memory_tau
memory_kernel_type
memory_source_field
smoothing_length
void_definition
filament_definition
classification_thresholds
```

## Required Output Files

Recommended output paths:

```text
simulations/cosmology/results/pm_hsplit_summary.csv
simulations/cosmology/results/pm_parameter_log.csv
simulations/cosmology/results/pm_environment_counts.csv
simulations/cosmology/figures/pm_void_filament_hsplit.png
```

## Required Diagnostics

1. baseline Lambda-CDM control run with memory disabled;
2. memory-enabled run with identical seed;
3. comparison of void and filament classification counts;
4. distribution of local expansion estimates by environment;
5. sensitivity to memory parameters `alpha` and `tau`;
6. sensitivity to smoothing scale and environment threshold;
7. check that the background expansion history is unchanged unless intentionally varied.

## Interpretation Boundary

A PM H-split is not by itself an observational detection. It is a mechanistic bridge between the effective-G memory model and the Pantheon+ environment-H0 test.

A useful simulation result is one that predicts the expected sign and approximate scale of `Delta_H` before the real Pantheon+ environment split is interpreted.
