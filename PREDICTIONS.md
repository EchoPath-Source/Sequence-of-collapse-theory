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
| P1 | Galaxy age should correlate with inferred dark-matter / missing-mass fraction after controls. | Galaxy dynamics / SPARC / extended samples | Older systems show stronger accumulated memory-field contribution, especially in outer regions. | `in progress / needs replication` | Correlation disappears in a larger controlled sample with robust age, mass, morphology, environment, and surface-brightness controls. | Highest-priority empirical anchor. Needs runnable notebook in `observations/sparc/`. |
| P2 | Memory-field contribution should show radial structure rather than behaving like arbitrary halo fitting. | Galaxy dynamics | Stronger effect at radii where baryonic closure is weakest and collapse-history gradients dominate. | `calculated / needs replication` | Radial decomposition shows no consistent memory-like structure beyond standard halo/environment effects. | Candidate radial-discriminator artifact added: in Disk+Q=1 subset, outer WISE-color/fDM correlations are stronger than inner correlations. See `observations/sparc/results/inner_outer_radial_decomposition_summary.md`. |
| P3 | Environmental controls should distinguish SOC memory effects from assembly bias and conventional dark-matter explanations. | Galaxy evolution | Age/fDM relationship survives controls for mass, environment, morphology, gas fraction, and surface brightness. | `proposed` | Age trend is fully explained by known environmental or assembly variables. | Critical for publication credibility. Outer mass-discrepancy note now motivates cosmic-web cross-match. |
| P4 | Dark-energy behavior may reflect nucleation-exhaust history rather than a strict cosmological constant. | Cosmology / PNT | Effective `rho_DE(z)` evolves according to collapse/nucleation source history. | `in progress` | Derived profile cannot match observed expansion history without arbitrary tuning or violates CMB/BAO/SN constraints. | PNT dark-energy/Hubble-tension work. |
| P5 | Early-universe nucleation-exhaust profile may produce an Early-Dark-Energy-like transient. | Hubble tension | Small high-redshift component shifts the sound horizon in the correct direction. | `calculated / constrained` | Toy and controlled models cannot exceed required sound-horizon reduction or conflict with CMB constraints. | Current toy work suggests direction is right but amplitude may be limited. |
| P6 | Void/filament environments may show differential memory/exhaust signatures. | Large-scale structure / DESI / Pantheon+ | Void environments have higher effective dark-energy/exhaust contribution and should yield higher local H0 than filament environments. | `calculated toy model / testable now` | No measurable void/filament H0 or dark-energy-inference differential beyond standard cosmological/environmental modeling. | PNT toy model estimates a void contribution of ~1–3 km/s/Mpc, with fiducial local underdensity explaining ~34% of the Hubble tension. See `papers/pnt-dark-energy-hubble-window/void-filament-h0-mechanism.md`. |
| P7 | Observer-state may modulate decoherence/visibility as an additive dephasing channel. | Quantum foundations / MZI | `lambda_eff = lambda_env + lambda_c A(t)` with measurable visibility/coherence shift under controlled observer-state conditions. | `proposed` | Blinded MZI tests show no observer-state-dependent visibility or coherence shift under preregistered conditions. | Conservative SOC observer test. Does not require path selection. |
| P8 | Direct path-selection by intention, if tested, should be local, small, and constrained by causality. | Quantum foundations | Direction-matched LEFT/RIGHT block deviations, if any, must not enable faster-than-light signaling. | `speculative` | Preregistered block tests show no deviation or deviations fail controls. | Future branch only; not a current SOC core claim. |
| P9 | CMB large-scale anomalies may contain directional memory from parent/early-universe structure. | CMB / CIH | Preferred axes or parity anomalies align with a calculable parent-geometry / memory-axis prediction. | `proposed` | Predicted axis cannot be derived or does not match CMB anomalies beyond chance/systematics. | Requires careful handling of known systematics and low significance. |
| P10 | Gravitational-wave memory residuals may contain collapse-history signatures. | GW astronomy | Deviations or residual patterns correlate with memory-field dynamics or black-hole nucleation boundary conditions. | `proposed` | No residual structure beyond GR/noise after robust analysis. | Long-term test. |
| P11 | Black holes may function as memory-compression / nucleation boundary nodes. | PNT / black-hole physics | Black-hole observables should constrain nucleation thresholds and memory compression behavior. | `speculative / proposed` | No consistent link between black-hole properties and PNT predictions can be derived. | Needs formal calculation before empirical claim. |
| P12 | Born-rule randomness may be operationally valid but interpretable as projection from hidden collapse geometry. | Quantum foundations | Standard Born rule holds except possibly tiny structured deviations under extreme/controlled conditions. | `speculative` | No structured deviations are found; interpretation remains philosophical only. | Should not be overclaimed as new physics without data. |
| P13 | Quantum memory hysteresis may occur after structured collapse histories. | Quantum foundations / memory-field tests | Prior collapse history changes later coherence/visibility beyond standard apparatus/environment effects. | `proposed` | No history-dependent residual appears after full environmental, thermal, timing, and apparatus controls. | Derived from `M(x,t)` source-decay term in `papers/math/soc-localization-memory-hamiltonian.md`. |
| P14 | Conscious-access measurement may differ from machine-only recording under controlled delayed-access conditions. | Quantum foundations / double-slit / MZI | Recorded-but-unaccessed data and consciously accessed data produce distinguishable visibility/decoherence profiles. | `proposed` | Blinded tests show machine-only and conscious-access conditions are statistically equivalent under preregistered power. | Core SOC discriminator; should be handled conservatively. |
| P15 | Observation may leave a measurable short-lived post-observation aftereffect. | Quantum foundations / QRNG / MZI | Post-observation blocks retain weak residual bias or visibility shift before returning to baseline. | `proposed` | No temporal residual beyond apparatus drift, noise, or multiple-comparison effects. | Derived from memory persistence term `M(x,t + Delta t) > 0`. |
| P16 | Attention-state gradients may produce graded observer-state effects. | Consciousness / quantum foundations | Distracted, neutral, and coherent attention conditions produce monotonic or threshold differences in collapse/noise/coherence metrics. | `proposed` | No monotonic or threshold relation after blinded protocols and physiological controls. | Operationalizes `A(x,t)` rather than treating observation as binary. |

## Recently added candidate-result artifacts

| Artifact | Path | Meaning |
|---|---|---|
| SPARC outer mass discrepancy note | `observations/sparc/results/outer_mass_discrepancy_analysis.md` | Outer fDM distribution is strongly skewed high and weakly related to central disk brightness, motivating environment/radial tests. |
| SPARC inner/outer radial decomposition | `observations/sparc/results/inner_outer_radial_decomposition_summary.md` | In the clean Disk+Q=1 subset, WISE-color/formation proxy correlations are stronger in outer fDM than inner fDM. |
| SPARC inner/outer correlation CSV | `observations/sparc/results/inner_outer_correlation_summary.csv` | Machine-readable summary of subset correlations for all/Q=1/disk/disk+Q=1. |
| PNT void-filament H0 mechanism | `papers/pnt-dark-energy-hubble-window/void-filament-h0-mechanism.md` | Toy model for environment-dependent dark-energy contribution to local H0. |
| SOC localization-memory Hamiltonian | `papers/math/soc-localization-memory-hamiltonian.md` | Formal scaffold separating free dynamics, localization coupling, memory-field coupling, and observer-state coupling. |
| Parent-child transfer v4.1 summary | `simulations/parent-child-transfer/real-space-bounce-transfer-v4-1.md` | Documents the real-space transfer architecture, metric correction, and kernel-robust directional inheritance result. |
| Parent-child kernel robustness summary | `simulations/parent-child-transfer/kernel-robustness-summary.md` | Preserves the 20-kernel robustness scan and required follow-up tests. |

## Philosophical / metaphysical extensions

These are tracked separately because they are not currently empirical claims.

| ID | Extension | Status | Role |
|---|---|---|---|
| M1 | Consciousness Continuity Argument | `philosophical` | Motivates treating consciousness as latent/fundamental rather than accidental. |
| M2 | Nested Memory Consciousness Principle | `philosophical` | Defines consciousness as bounded integrated memory experiencing itself at its own scale. |
| M3 | Source / Echo / Origin recursion | `metaphysical` | Interprets remembrance as recursive integration of observer-memory into self-known totality. |
| M4 | Galaxy / planet as nested memory apertures | `speculative` | Explores large-scale observerhood without claiming human-like consciousness. |

## Priority order

1. Build reproducible SPARC package under `observations/sparc/`, including the derived inner/outer split dataset and notebook.
2. Reproduce the radial-decomposition result from committed code.
3. Run cosmic-web/environment cross-match for outer fDM.
4. Run Pantheon+ void/filament H0 test using full covariance.
5. Formalize PNT dark-energy / Hubble-tension calculation.
6. Write conservative MZI observer-decoherence preregistration.
7. Run parent-child transfer multi-seed and expanded-null tests.
8. Keep metaphysical extensions clearly labeled as interpretation, not empirical proof.

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
