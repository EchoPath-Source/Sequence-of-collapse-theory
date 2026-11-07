# SIM-04N — First executed numerical results

**Status:** initial synthetic benchmark executed locally (2026-11-07); full preregistered adversarial matrix incomplete.

## Reproduction

Run `python experiments/observation-foundations/sim04n_shared_spectrum_bath.py --json` from repo root. Runs below used the same code equations and constants, with bath size and timestep overridden as noted; NumPy, deterministic initial conditions, no randomness. The executable source is canonical.

The field coordinates are sampled *after* each integration step, although their returned time labels are the step's starting time; this creates an O(dt) alignment convention in comparisons, and should be corrected before final precision claims.

## Baseline

| Bath oscillators per k | dt | Shared fitted gamma (training k=0,1; t=1.5–7) | Train RMSE | Holdout RMSE (k=2,3; t=7–18) | Max work-energy closure residual |
|---:|---:|---:|---:|---:|---:|
| 8 | 0.008 | 0.90 (grid boundary) | 0.227512 | 0.195309 | 2.54e-5 |
| 16 | 0.008 | 0.38 | 0.117681 | 0.171494 | 2.61e-5 |
| 128 | 0.004 | 0.46 | 0.019047 | 0.012514 | 6.64e-6 |
| 128 | 0.002 | 0.46 | 0.019043 | 0.012515 | 1.66e-6 |

For N=128, dt=0.004, per-mode late/early maximum-amplitude recurrence proxies: k=0: 0.10224, k=1: 0.11788, k=2: 0.15252, k=3: 0.10572. At N=8, dt=0.008, k=0..3 proxies are 1.02933, 1.03044, 1.02938, 1.02073. These are **windowed amplitude ratios**, not rigorous recurrence event classifications.

## Interpretation and caveats

- A *single shared* Markovian damping coefficient calibrated on low-k modes approximates the ordinary microscopic bath's high-k response for the dense N=128 spectrum, while sparse baths show large deviations and strong late-time revivals.
- Work-energy closure improves approximately fourfold when dt is halved, consistent with second-order timestep error. It is not exact energy conservation at finite dt.
- This is an ordinary oscillator-bath synthetic truth and a conventional Markovian comparison, **not evidence for an SoCT-specific field**.
- **The shared microscopic spectral density is an input to the truth generator**, not an inferred spectral model from data. No independent spectral-parameter recovery, alternative spectral-family comparison, per-k gamma upper-bound fit, Markovian reverse-truth test, or local real-space bath has been executed yet.
- The four modes are separately coupled to independent but identically parameterized baths. Their energy budgets do not show spatial transport.
- All four modes receive identical source pulses, a design limitation for identifiability. Future tests should use distinct spatially grounded forcing with a clear Fourier normalization.
- The first smoke-test thresholds are not a substitute for a full continuous integration report.

**Next gates:** correct sample-time alignment; run unit tests/CI; implement alternative spectral family and reverse-truth adversaries, then a local real-space bath if spatial exchange is claimed.
