# Canonical Parameter Ledger

**Status:** Ledger scaffold / anti-drift document  
**Purpose:** Track key SoCT/PNT/CIH parameters, their source, current value, uncertainty, and claim status.

---

## Purpose

This ledger prevents parameter drift across papers, simulations, and metaphysical/theoretical notes.

Any quantity used in multiple repo branches should eventually appear here with:

```text
symbol
meaning
current value
units
source file
derivation status
uncertainty
claim level
last updated
```

---

## Claim-Level Legend

| Label | Meaning |
|---|---|
| `placeholder` | Mentioned but not derived. |
| `toy-model` | Used in a simplified model. |
| `candidate` | Derived internally but not independently checked. |
| `constrained` | Bounded by data or consistency condition. |
| `canonical` | Stable repo convention for current work, still revisable. |
| `deprecated` | Superseded or found inconsistent. |

---

## Core SOC Parameters

| Symbol | Meaning | Current value | Units | Status | Source / notes |
|---|---|---:|---|---|---|
| `lambda_M` | memory-field coupling strength | TBD | model-dependent | placeholder | Appears in SOC Hamiltonian. |
| `lambda_c` | observer/conscious-access coupling strength | TBD | model-dependent | placeholder | Appears in SOC Hamiltonian and MZI branch. |
| `alpha` | collapse-to-memory conversion rate | TBD | TBD | placeholder | Memory evolution equation. |
| `beta` | memory decay / relaxation rate | TBD | inverse time | placeholder | Memory evolution equation. |
| `D_M` | memory diffusion coefficient | TBD | length^2/time | placeholder | Memory evolution equation. |
| `tau_memory` | long-memory timescale | ~Gyr scale | Gyr | candidate | Needs SPARC/PNT consistency derivation. |

---

## SPARC / Galaxy Dynamics Parameters

| Symbol / quantity | Meaning | Current value | Units | Status | Source / notes |
|---|---|---:|---|---|---|
| `N_SPARC_age_fDM` | candidate age/fDM sample size | 175 | galaxies | candidate | Needs notebook reproduction. |
| `r_age_fDM_outer` | full-sample Pearson correlation | +0.201 | dimensionless | candidate | Reported internal analysis. |
| `p_age_fDM_outer` | p-value for full-sample correlation | 0.0077 | dimensionless | candidate | Reported internal analysis. |
| `rho_outer_disk_Q1_half` | Spearman rho, Disk+Q=1 outer half split | -0.657 | dimensionless | candidate | `observations/sparc/results/inner_outer_correlation_summary.csv` |
| `rho_inner_disk_Q1_half` | Spearman rho, Disk+Q=1 inner half split | -0.553 | dimensionless | candidate | Same source. |
| `rho_outer_disk_Q1_Reff` | Spearman rho, Disk+Q=1 outer Reff split | -0.637 | dimensionless | candidate | Same source. |
| `rho_inner_disk_Q1_Reff` | Spearman rho, Disk+Q=1 inner Reff split | -0.409 | dimensionless | candidate | Same source. |

Note:

> Negative sign follows the chosen `g-W1` proxy direction and must be interpreted through the color/formation-history convention used in the analysis.

---

## PNT Dark-Energy / Hubble Parameters

| Symbol / quantity | Meaning | Current value | Units | Status | Source / notes |
|---|---|---:|---|---|---|
| `Omega_m` | matter density parameter | 0.315 | dimensionless | toy-model | Used in PNT void-H0 dashboard. |
| `Omega_DE` | dark-energy density parameter | 0.685 | dimensionless | toy-model | Used in PNT void-H0 dashboard. |
| `H0_CMB` | CMB-inferred H0 | 67.4 | km/s/Mpc | toy-model | Fiducial comparison value. |
| `H0_local_target` | local-distance-ladder H0 target | 73.0 | km/s/Mpc | toy-model | Fiducial comparison value. |
| `delta_local` | local underdensity proxy | ~-0.35 | dimensionless | toy-model | Used in void-filament H0 mechanism. |
| `f_succ_mean` | mean successful nucleation fraction | 0.15 | dimensionless | toy-model | Phenomenological; needs derivation. |
| `n_SK` | density scaling exponent | 1.5 | dimensionless | toy-model | Schmidt-Kennicutt-style scaling. |
| `H0_PNT_void_fiducial` | fiducial PNT local H0 in local underdensity | ~69.3 | km/s/Mpc | toy-model | Explains ~34% of tension in toy model. |
| `tau_ex` | prompt exhaust timescale requirement | 0.001-0.03 | Myr | constrained/toy | Needs plasma-physics derivation. |

---

## CIH / Kerr / Engramon Parameters

| Symbol / quantity | Meaning | Current value | Units | Status | Source / notes |
|---|---|---:|---|---|---|
| `M_parent` | parent black-hole/universe mass estimate | TBD | solar masses | unresolved | Multiple source values may exist; needs canonical derivation. |
| `a_star_parent` | parent Kerr spin parameter | TBD | dimensionless | placeholder | Needed for directional-memory axis model. |
| `l_E` | Engramon / inversion length scale | TBD | length | unresolved | Derived from Kerr/ring quantization branch. |
| `E_E` | Engramon energy scale | TBD | energy | unresolved | Derived from `l_E`; neutrino check pending. |
| `axis_parent` | predicted parent/Kerr direction | TBD | sky coordinates | placeholder | Must be derived before comparing to CMB anomalies. |
| `f_NL_limit` | non-Gaussianity bound | Planck-dependent | dimensionless | constrained | Use published constraints when formalized. |

---

## Parent-Child Transfer Simulation Metrics

| Symbol / quantity | Meaning | Current value | Units | Status | Source / notes |
|---|---|---:|---|---|---|
| `alignment_signal_v4_0` | v4.0 quadrupole alignment for signal child field | 0.968 | dimensionless | toy-model | `simulations/parent-child-transfer/real-space-bounce-transfer-v4-1.md` |
| `alignment_null_v4_0` | v4.0 quadrupole alignment for null field | 0.073 | dimensionless | toy-model | Same source. |
| `delta_alignment_v4_0` | signal-null quadrupole alignment delta | +0.894 | dimensionless | toy-model | Strong positive exploratory result. |
| `ratio_signal_v4_0` | v4.0 anisotropy ratio for signal | 0.648 | dimensionless | diagnostic | Ratio metric considered kernel-contaminated. |
| `ratio_null_v4_0` | v4.0 anisotropy ratio for null | 1.225 | dimensionless | diagnostic | Null exceeded signal on ratio metric. |
| `delta_ratio_v4_0` | signal-null anisotropy-ratio delta | -0.577 | dimensionless | diagnostic/fail | Preserved as failed diagnostic metric. |
| `N_kernel_v4_1` | kernel configurations tested | 20 | configurations | toy-model | `simulations/parent-child-transfer/kernel-robustness-summary.md` |
| `N_strong_positive_v4_1` | configurations with delta > 0.1 | 19 | configurations | toy-model | Strong-positive threshold is provisional. |
| `N_weak_positive_v4_1` | positive but weak configurations | 1 | configuration | toy-model | Positive but below strong threshold. |
| `N_negative_v4_1` | negative deltas | 0 | configurations | toy-model | No null-beating-signal cases reported. |
| `mean_delta_alignment_v4_1` | mean alignment advantage across kernel scan | ~+0.583 | dimensionless | toy-model | Approximate reported mean. Needs CSV reproduction. |

Claim boundary:

> These values document an exploratory toy-model signal. They should not be used as empirical evidence until code, random seeds, null models, CSV outputs, and multi-seed tests are committed.

---

## Memory Kernel Parameters

| Symbol | Meaning | Current value | Units | Status | Notes |
|---|---|---:|---|---|---|
| `K(r,t)` | memory kernel | TBD | model-dependent | placeholder | Candidate forms need comparison. |
| `r_memory` | spatial range of memory coupling | TBD | kpc/Mpc or other | placeholder | May differ by galaxy/cosmology branch. |
| `tau_short` | prompt/short memory timescale | ~10^3-10^4 yr candidate | time | toy/constrained | Related to PNT prompt EDE branch. |
| `tau_long` | long memory residue timescale | Gyr scale | time | candidate | Related to SPARC/PNT late DE. |

---

## Rules for Updating This Ledger

1. Do not replace a parameter silently.
2. Add date/source when changing a value.
3. Mark conflicting values as unresolved until recalculated.
4. Link to notebooks/scripts once available.
5. Separate toy-model constants from data-constrained values.
6. Never use metaphysical language as a parameter source.

---

## Immediate Ledger Tasks

1. Resolve `M_parent` discrepancy.
2. Add Kerr ring quantization derivation outputs.
3. Add `f0` from `rho_DE` cross-constraint.
4. Add SPARC radial-decomposition exact provenance.
5. Add Pantheon environment-H0 fitted values once available.
6. Add thermalization `tau_ex` calculation results.
7. Replace parent-child transfer summary values with CSV-linked reproducible outputs once available.
8. Add multi-seed parent-child transfer statistics when run.
