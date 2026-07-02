# P4 Protocol Index — SOC-MZI / CGDS / Observer-Dependent Decoherence

**Status:** preregistration-support index.  
**Purpose:** map the split P4 protocol, OSF, simulation, and support materials without expanding claims.

This index exists because the P4 materials are intentionally distributed across paper, experiment, OSF, and support folders. Use this file as the routing map before editing or citing P4 materials.

## Claim boundary

Use:

> P4 is a preregistered / protocol-development track for testing whether conscious-access conditions modulate decoherence-like observables in controlled interferometry or related quantum settings. Current simulations are expected-signature / power-planning artifacts, not experimental evidence.

Avoid:

> P4 proves consciousness collapses the wavefunction, proves observer-dependent quantum mechanics, or proves an SOC-MZI effect.

## Canonical P4 locations

| Role | Path | Status | Notes |
|---|---|---|---|
| Canonical paper/protocol hub | `papers/p4-soc-mzi-awareness-modulated-decoherence/` | canonical | Primary P4 paper folder from the March 2026 roadmap. |
| P4 README | `papers/p4-soc-mzi-awareness-modulated-decoherence/README.md` | canonical | Paper-level overview and roadmap status. |
| Preregistration excerpt | `papers/p4-soc-mzi-awareness-modulated-decoherence/preregistration/OSF_Preregistration_Excerpt_v1.1_clean.md` | source/prereg excerpt | Clean imported preregistration excerpt. |
| Simulation script | `papers/p4-soc-mzi-awareness-modulated-decoherence/simulations/soc_mzi_visibility_decay_simulation.py` | simulation | Canonical paper-local simulation copy. |
| Simulation results | `papers/p4-soc-mzi-awareness-modulated-decoherence/simulations/results/` | simulation outputs | Contains committed CSV outputs and README. |

## Support / legacy locations

| Role | Path | Status | Notes |
|---|---|---|---|
| CGDS support paper folder | `papers/p4-observer-dependent-decoherence-cgds/` | support | Earlier CGDS / observer-dependent decoherence hub. Preserve as support, not replacement for canonical P4. |
| Quantum experiments folder | `experiments/quantum/` | experiment support | Experiment-specific plans and notes. |
| OSF experiment folder | `experiments/osf/` | OSF/prereg support | OSF-related protocol assets. |
| Docs experiment imports | `docs/experiments/` | imported source | Imported or extracted experiment/preregistration materials. |
| Exact uploaded simulation filename | `simulations/mzi-visibility-decay/SOC MZI Visibility Decay Simulation.py` | source script copy | Preserves original uploaded filename and source context. |

## Simulation outputs currently tracked

Expected files under:

```text
papers/p4-soc-mzi-awareness-modulated-decoherence/simulations/results/
```

| File | Meaning | Claim status |
|---|---|---|
| `main_effect.csv` | Simulated visibility outcome by condition. | Expected-signature simulation only. |
| `timing_asymmetry.csv` | Simulated timing/asymmetry scenario. | Expected-signature simulation only. |
| `dose_response.csv` | Simulated dose-response / awareness-scaling table. | Expected-signature simulation only. |
| `README.md` | Results provenance and claim boundary. | Governance / provenance. |

## Protocol components to reconcile

The full P4 protocol should eventually expose one canonical table covering:

1. Experiment name and variant: SOC-MZI, CGDS, delayed-choice, AI observer arm, or support simulation.
2. Primary endpoint.
3. Conscious-access manipulation.
4. Blinding/deletion rule.
5. Data-retention rule.
6. Confirmatory tests.
7. Exclusion criteria.
8. Underpowered/failed-run criteria.
9. Claim boundary.
10. OSF/preregistration source reference.

## AI observer control arm

The roadmap refers to an AI observer control arm. Treat it as **missing / partial** unless a complete protocol section is present with:

- AI system or model class;
- access condition;
- logging/deletion rule;
- whether AI receives trial-level outcome data;
- primary comparison against human conscious-access arms;
- interpretation table for AI-null, AI-positive, human-null, and human-positive cases.

## Recommended next files

```text
papers/p4-soc-mzi-awareness-modulated-decoherence/preregistration/full-protocol-status.md
papers/p4-soc-mzi-awareness-modulated-decoherence/preregistration/ai-observer-control-arm.md
papers/p4-soc-mzi-awareness-modulated-decoherence/preregistration/confirmatory-test-table.md
```

## Editing rule

Do not merge CGDS, SOC-MZI, delayed-choice, and AI-observer language into a single claim unless the protocol explicitly defines them as arms of the same registered experiment. Keep each variant separately labeled until the full preregistration package is assembled.
