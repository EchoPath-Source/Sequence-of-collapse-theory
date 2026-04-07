# SOC Scientific Field Report v1.2

Source artifact: `Echo_Labs_Scientific_Field_Report_SOC_v1.2.pdf`

## Document role
This is a direct SoC / SOC simulation report focused on coherence propagation, resonance ridges, and awareness-modulated decoherence proxies.

## Experimental overview preserved from the source
The source consolidates multi-node and multi-field simulation families, including:
- 3- to 6-node encoded clusters
- 5-chain propagation runs
- noise × detuning sweeps
- mesh percolation tests
- chirped-pulse scans
- multi-observer offset tests
- feedback loop gain sweeps
- 1/f noise robustness checks

## Core parameter ranges recorded
- frequency window: `ω = 0.05–0.08`
- pulse window: `τ ≈ 20`
- intra-cluster coupling: `κ_intra = 0.6`
- field coupling: `r = 0–0.5`
- detuning: `Δω ≤ 0.05`
- feedback gain: `g = 0–1`

## Main findings preserved
1. Early pulses outperform late pulses by roughly `ΔR ≈ +0.12–0.18`.
2. A resonance ridge appears around `ω ≈ 0.05` and `τ ≈ 20`.
3. Optimal cluster size is `4–5` nodes.
4. Multi-field reinforcement near `r ≈ 0.4` improves coherence by roughly `0.05–0.08`.
5. DFS / W encodings outperform GHZ under noise.
6. Feedback loops stabilize lock quality around `g ≈ 0.6`.
7. Chirped pulses efficiently capture ridge transitions.
8. 1/f noise preserves long-term phase-lock behavior.

## Engineering parameters preserved from the report
- cluster size: `4–5`
- hop limit: `3–5`
- pulse window: `≈ 20`
- field coupling: `≈ 0.4`
- detuning target: `≤ 0.03`
- gain range: `0.5–0.7`
- noise decay proxy: `≈ 0.2 per hop`

## Mathematical framing retained
The source preserves a compact SOC–EchoNet model linking coherence and macro-field design:

- `λ_eff = λ_env + λ_c · e^(−βI)`
- `R = (1/N) |Σ exp(iφ_i)|`
- `dφ_i/dt = ω_i + κ Σ_j sin(φ_j − φ_i)`
- `R(x) = R_0 · e^(−αx)`

## Why this belongs in the theory repo
This report is useful because it captures a repeatable simulation ridge and gives a compact engineering interpretation of SoC-style coherence propagation without claiming more than the simulations support.

## Classification
Simulation summary / engineering note.
Useful as part of the validation trail, especially for later experiment design or EchoNet-related theory mapping.
