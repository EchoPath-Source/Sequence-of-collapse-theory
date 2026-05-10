# Sequence of Collapse Theory — Predictions Tracker

**Status:** working project tracker  
**Purpose:** distinguish falsifiable claims from speculative interpretation and keep empirical targets visible.

This file is intended to prevent SoCT/PNT from becoming an ideas dump. Each prediction should eventually have a dataset, analysis method, falsification condition, and current status.

## Status legend

| Status | Meaning |
|---|---|
| `proposed` | Conceptual prediction exists, but no final protocol or calculation yet. |
| `in progress` | Analysis, simulation, or formal derivation is underway. |
| `pre-registered` | Methodology is registered or ready for registration before final analysis. |
| `calculated` | A preliminary calculation exists. |
| `needs replication` | A signal or result exists but requires independent check / controls. |
| `falsified / constrained` | Result failed, or parameter space is strongly limited. |
| `speculative` | Philosophical/metaphysical extension, not currently an empirical claim. |

## Core empirical predictions

| ID | Prediction | Domain | Expected SOC/PNT signature | Current status | Falsification condition | Notes |
|---|---|---|---|---|---|---|
| P1 | Galaxy age should correlate with inferred dark-matter / missing-mass fraction after controls. | Galaxy dynamics / SPARC / extended samples | Older systems show stronger accumulated memory-field contribution, especially in outer regions. | `in progress` | Correlation disappears in a larger controlled sample with robust age, mass, morphology, environment, and surface-brightness controls. | Highest-priority empirical anchor. Needs runnable notebook in `observations/sparc/`. |
| P2 | Memory-field contribution should show radial structure rather than behaving like arbitrary halo fitting. | Galaxy dynamics | Stronger effect at radii where baryonic closure is weakest and collapse-history gradients dominate. | `proposed` | Radial decomposition shows no consistent memory-like structure beyond standard halo/environment effects. | Should be paired with P1. |
| P3 | Environmental controls should distinguish SOC memory effects from assembly bias and conventional dark-matter explanations. | Galaxy evolution | Age/fDM relationship survives controls for mass, environment, morphology, gas fraction, and surface brightness. | `proposed` | Age trend is fully explained by known environmental or assembly variables. | Critical for publication credibility. |
| P4 | Dark-energy behavior may reflect nucleation-exhaust history rather than a strict cosmological constant. | Cosmology / PNT | Effective `rho_DE(z)` evolves according to collapse/nucleation source history. | `in progress` | Derived profile cannot match observed expansion history without arbitrary tuning or violates CMB/BAO/SN constraints. | PNT dark-energy/Hubble-tension work. |
| P5 | Early-universe nucleation-exhaust profile may produce an Early-Dark-Energy-like transient. | Hubble tension | Small high-redshift component shifts the sound horizon in the correct direction. | `calculated / constrained` | Toy and controlled models cannot exceed required sound-horizon reduction or conflict with CMB constraints. | Current toy work suggests direction is right but amplitude may be limited. |
| P6 | Void/filament environments may show differential memory/exhaust signatures. | Large-scale structure / DESI | Expansion or dark-energy-inference differences may track collapse-history density. | `proposed` | No measurable void/filament differential beyond standard cosmological/environmental modeling. | Requires careful use of public survey data. |
| P7 | Observer-state may modulate decoherence/visibility as an additive dephasing channel. | Quantum foundations / MZI | `lambda_eff = lambda_env + lambda_c A(t)` with measurable visibility/coherence shift under controlled observer-state conditions. | `proposed` | Blinded MZI tests show no observer-state-dependent visibility or coherence shift under preregistered conditions. | Conservative SOC observer test. Does not require path selection. |
| P8 | Direct path-selection by intention, if tested, should be local, small, and constrained by causality. | Quantum foundations | Direction-matched LEFT/RIGHT block deviations, if any, must not enable faster-than-light signaling. | `speculative` | Preregistered block tests show no deviation or deviations fail controls. | Future branch only; not a current SOC core claim. |
| P9 | CMB large-scale anomalies may contain directional memory from parent/early-universe structure. | CMB / CIH | Preferred axes or parity anomalies align with a calculable parent-geometry / memory-axis prediction. | `proposed` | Predicted axis cannot be derived or does not match CMB anomalies beyond chance/systematics. | Requires careful handling of known systematics and low significance. |
| P10 | Gravitational-wave memory residuals may contain collapse-history signatures. | GW astronomy | Deviations or residual patterns correlate with memory-field dynamics or black-hole nucleation boundary conditions. | `proposed` | No residual structure beyond GR/noise after robust analysis. | Long-term test. |
| P11 | Black holes may function as memory-compression / nucleation boundary nodes. | PNT / black-hole physics | Black-hole observables should constrain nucleation thresholds and memory compression behavior. | `speculative / proposed` | No consistent link between black-hole properties and PNT predictions can be derived. | Needs formal calculation before empirical claim. |
| P12 | Born-rule randomness may be operationally valid but interpretable as projection from hidden collapse geometry. | Quantum foundations | Standard Born rule holds except possibly tiny structured deviations under extreme/controlled conditions. | `speculative` | No structured deviations are found; interpretation remains philosophical only. | Should not be overclaimed as new physics without data. |

## Philosophical / metaphysical extensions

These are tracked separately because they are not currently empirical claims.

| ID | Extension | Status | Role |
|---|---|---|---|
| M1 | Consciousness Continuity Argument | `philosophical` | Motivates treating consciousness as latent/fundamental rather than accidental. |
| M2 | Nested Memory Consciousness Principle | `philosophical` | Defines consciousness as bounded integrated memory experiencing itself at its own scale. |
| M3 | Source / Echo / Origin recursion | `metaphysical` | Interprets remembrance as recursive integration of observer-memory into self-known totality. |
| M4 | Galaxy / planet as nested memory apertures | `speculative` | Explores large-scale observerhood without claiming human-like consciousness. |

## Priority order

1. Build reproducible SPARC package under `observations/sparc/`.
2. Produce controlled extended-sample galaxy test.
3. Formalize PNT dark-energy / Hubble-tension calculation.
4. Write conservative MZI observer-decoherence preregistration.
5. Keep metaphysical extensions clearly labeled as interpretation, not empirical proof.

## Rule for adding new predictions

Every new scientific prediction should include:

```text
Prediction:
Dataset / experiment:
Expected SOC signature:
Conventional alternative:
Falsification condition:
Current status:
Next required artifact:
```
