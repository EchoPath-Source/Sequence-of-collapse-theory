# SOC-MZI Visibility Decay Simulation Outputs

## Status

PRELIMINARY / simulation outputs.

These files are simulation-informed expected signatures for SOC-MZI planning and falsification scaffolding. They are not empirical evidence, and they do not establish an awareness-modulated decoherence effect.

## Script path used

Generated with:

```bash
python papers/p4-soc-mzi-awareness-modulated-decoherence/simulations/soc_mzi_visibility_decay_simulation.py
```

Script:

```text
papers/p4-soc-mzi-awareness-modulated-decoherence/simulations/soc_mzi_visibility_decay_simulation.py
```

## Seed

The simulation script states:

```text
SEED = 42
```

## Committed output files

- `main_effect.csv`
- `timing_asymmetry.csv`
- `dose_response.csv`

The script also generates PNG figures (`main_effect.png`, `timing_asymmetry.png`, and `dose_response.png`), but those binary artifacts are intentionally not included in this commit.

## Output descriptions

- `main_effect.csv`: Tabular simulated low-awareness and high-awareness visibility values across configured interferometer delays, including true values, noisy measured values, and visibility differences.
- `timing_asymmetry.csv`: Tabular simulated early-window and late-window high-awareness visibility values, including effective exposure times, true values, noisy measured values, and late-minus-early differences.
- `dose_response.csv`: Tabular simulated visibility values across an awareness-value grid at the representative delay, including true values, noisy measured values, and a fitted linear trend.

## Claim boundary

These are simulation-informed expected signatures, not empirical evidence. They do not establish an awareness-modulated decoherence effect.
