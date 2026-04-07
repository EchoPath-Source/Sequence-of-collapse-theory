# Gravity Imprint & Dark-Matter Analog — Simulation Update (2026-01-30)

Source artifact: `EchoLabs_QRRG_GravityImprint_DMAnalog_SimUpdate_2026-01-30.docx`

## Scope
This note preserves the main conclusions from a Q-RRG / SoCT-style simulation family where a memory field `M(r,t)` with observer coupling `Φ` produces two internal attribution channels:

- `grav`: gravity-imprint score
- `dm`: dark-matter analog score

These are **model-internal curvature-attribution proxies**, not physical mass measurements.

## Metric glossary
- `grav`: portion of trajectory bending attributed to accumulated memory imprint.
- `dm`: residual curvature not captured by the explicit grav imprint.
- `share = grav / (grav + dm)`: higher means curvature is attributed more to the memory imprint.
- `ratio = dm / grav`: higher means a dark-matter-analog dominant regime.
- `Φ`: observer-coupling strength.
- `write`: memory write rate.
- `cap`: memory horizon / history cap.
- `steps`: simulation time horizon.

## Main patterns preserved from the source memo

### 1. Grav increases with observer coupling and write rate
Across multiple sweeps, `grav` rises as `Φ` and write rate increase.

### 2. DM-dominant behavior appears early, then decays
A repeated pattern in the source memo is that `dm / grav` starts high and then relaxes downward as the memory imprint accumulates.

### 3. Noise suppresses dm more than grav
High noise reduces the dm analog while the grav imprint remains comparatively robust.

### 4. Φ shifts attribution from dm toward grav
Higher observer coupling tends to reduce entropy and move the system toward a grav-dominant regime.

### 5. Density matters
Higher agent density lowers the dm analog, consistent with a sparsity / unresolved-curvature interpretation.

## Representative source results

### Noise ablation (100 agents)
- 10% noise: OFF = (0,0), ON = (grav 0.64, dm 0.47), ON+Φ = (grav 1.03, dm 0.67)
- 15% noise: OFF = (0,0), ON = (0.63, 0.36), ON+Φ = (0.65, 0.35)
- 20% noise: OFF = (0,0), ON = (0.77, 0.13), ON+Φ = (0.74, 0.36)

### Φ sweep (fixed medium write, 100 agents, 15% noise)
- Φ = 0.0 -> grav 0.12, dm 0.45
- Φ = 0.25 -> grav 0.38, dm 0.52
- Φ = 0.5 -> grav 0.61, dm 0.68
- Φ = 0.75 -> grav 0.79, dm 0.71
- Φ = 1.0 -> grav 0.92, dm 0.82

### Write-rate sweep (fixed Φ = 0.5)
- Low write: grav 0.42, dm 0.59
- Medium write: grav 0.61, dm 0.68
- High write: grav 0.85, dm 0.77

### Step / cap sweeps (100 agents, 15% noise, Φ = 0.5)
- Short steps / small cap -> share 0.33, ratio 2.0 (early dm-dominant regime)
- Medium steps / medium cap -> share 0.55, ratio 0.83
- Long steps / large cap -> share 0.74, ratio 0.36
- Long steps / no cap -> share 0.73, ratio 0.37

## Time-resolved decay law preserved from the memo
A key takeaway from the source is the time-resolved fit:

`ratio(t) ≈ a * exp(-b * t) + c`

Interpretation retained from the source:
- `dm / grav` decays exponentially as grav accumulates.
- larger history caps slow the decay rate `b`.
- the asymptotic regime remains grav-dominant.

## Why this matters for the SoCT repo
This memo is useful because it preserves a computational bridge between:
- early unresolved curvature / residual attribution
- late stabilized memory imprint
- observer coupling as a persistence amplifier

It does **not** establish a physical dark-matter theory. It does preserve a testable internal signature for later work:
- exponential ratio decay
- entropy correlation
- parameter dependence on `Φ`, write, noise, density, and cap

## Recommended next steps from the source memo
1. Export the full `Φ × write × noise` grid to CSV.
2. Add explicit time-series plots for `grav(t)`, `dm(t)`, `share(t)`, and `ratio(t)`.
3. Fit `ratio(t)` across multiple `Φ` values.
4. Run density controls that hold area or volume fixed while varying agent count.
5. Compare against a conventional non-memory potential-field baseline.

## Classification
Exploratory simulation memo. Useful for preserving hypothesis structure and internal model behavior, but not yet publication-ready evidence.
