# SIM-04N — Shared-spectrum spatial microscopic bath: preregistered protocol

**Status:** protocol frozen; first implementation and smoke tests committed; numerical execution and results pending.
**Claim level:** synthetic methodology only. No evidence of a new physical SoCT memory field.

## Question and motivation

SIM-04M showed that a conventional finite oscillator bath can mimic reduced damping, with recurrences for sparse spectra. SIM-04J independently imposed a low-k/high-k cross-regime prediction on a causal field. SIM-04N asks whether **one microscopic bath spectral density and coupling law**, rather than independently tuned damping for each wavelength, reproduces mode-dependent decay, recurrence, and spatial exchange.

The main adversary is an ordinary microscopic reservoir with the same allowed couplings. A good fit is **not** evidence for a novel ontology.

## Hamiltonian and fixed shared parameters

For real orthonormal spatial Fourier modes (M_k) on a periodic lattice, use

```math
H_0=\sum_k\left[\frac{P_k^2}{2}+\frac{\Omega_k^2 M_k^2}{2}
+\sum_j\left(\frac{p_{kj}^2}{2}+\frac{\omega_j^2}{2}
\left(q_{kj}-\frac{c_j M_k}{\omega_j^2}\right)^2\right)\right],
\quad \Omega_k^2=\omega_0^2+c_M^2\widehat{k}^2.
```

A source adds `-sum_k F_k(t) M_k`. The same `omega_j`, `c_j`, bath size, cutoff, and envelope are used for **every** k. For an Ohmic-like candidate, `J(omega)=eta * omega * exp(-omega/cutoff)`; sample its discretization once, not per mode. Integrate all field and bath coordinates symplectically. Verify the external-work identity `H0(t)-H0(0)=sum_k integral F_k dM_k`.

**Important limitation:** independent baths for each Fourier mode do not, by themselves, define a spatially local bath or demonstrate physical bath-energy transport between sites. The Fourier-diagonal bath is the first baseline only. A subsequent real-space local-bath variant is required to test spatial energy flux, continuity and finite-speed exchange. Do not label Fourier-mode energy redistribution as measured spatial transport.

## Frozen comparison and evaluation

1. Train on `k=0,1` only, using post-drive `t=1.5..7`; hold out `k=2,3` and `t=7..18`. The lattice size, normalization, drive waveform, initial bath preparation, integration timestep, spectral discretization and random seeds must be fixed before examining held-out data.
2. Fit one shared spectral parameter vector on training modes only; do not refit a separate `gamma(k)`. Report whether a single constant effective `gamma` is adequate and the empirical per-k effective rates as **diagnostics only**, never as extra prediction parameters.
3. Predict held-out trajectories, mode-resolved recurrence ratios, field-sector energies, bath-sector energies and microscopic work/energy closure. Compare against (a) constant-`gamma` Markovian reduction, (b) independently tuned per-mode `gamma(k)` as a non-predictive upper-bound diagnostic, (c) a different fixed bath spectral family with equal parameter budget, and (d) sparse-bath recurrence adversary.
4. Compare the low/high-k response to SIM-04J **only after** accounting for the different effective `gamma` conventions and any renormalized frequency. Do not import SIM-04J's `gamma=5` into SIM-04M's `eta=0.5` model without calibration.
5. Include reverse-truth tests: data from a standard bath and from a Markovian model. The preferred model should switch when the data-generating mechanism switches.

## Acceptance / failure criteria

- Reproducible seed/config and machine-readable metrics; no test-window retuning.
- Microscopic work-energy closure checked at multiple timesteps; energy error must converge under timestep refinement.
- Held-out predictive error compared against the noise floor and against equal-complexity ordinary bath nulls.
- Explicitly report when local damping fails because of recurrences or colored memory.
- Do not infer a unique physical field from a model that is observationally equivalent to an ordinary reservoir.

## Interpretation boundary

A successful shared-spectrum transfer would show **internal cross-wavelength consistency of a synthetic microscopic completion**, not necessity of (M). A failure would rule out the tested spectral family/discretization under its assumptions, not all conventional baths. A genuinely discriminating future test requires independently calibrated bath degrees of freedom or a SoCT-specific constraint that conventional open-system models cannot simply replicate.

## Relationship to earlier gates

- SIM-04J: causal low-k/high-k spectral constraint, phenomenological damping independently calibrated.
- SIM-04K/L: global/local exchange ledgers, without microscopic bath recipient.
- SIM-04M: explicit single-mode oscillator bath and finite-size recurrence.
- SIM-04N: shared microscopic spectrum across spatial modes, then a separate locality/transport extension.

## First implementation\n\n- `sim04n_shared_spectrum_bath.py`: deterministic four-mode Hamiltonian oscillator bath, shared spectral envelope, one early-time damping fit, held-out mode/time metrics and work-energy ledger.\n- `test_sim04n_shared_spectrum.py`: spectral positivity, energy-closure and timestep-refinement smoke tests.\n\nRun from repository root:\n\n```bash\npython experiments/observation-foundations/sim04n_shared_spectrum_bath.py --json\npython -m unittest discover -s experiments/observation-foundations -p 'test_sim04n*.py'\n```\n\n**Execution status:** code and tests have been committed but have not been run or verified in this session. No numerical result is claimed.\n\n**Remaining protocol work:** alternative bath families, reverse-truth comparisons, independently fitted per-mode diagnostic and a real-space local-bath transport variant are not yet implemented.
