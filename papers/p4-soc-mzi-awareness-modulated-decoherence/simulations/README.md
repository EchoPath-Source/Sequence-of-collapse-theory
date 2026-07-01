# P4 SOC-MZI Simulation Package

## Status

PRELIMINARY / simulation support.

This folder contains the canonical paper-local SOC-MZI visibility-decay simulation used for expected-signature planning and falsification scaffolding. It is not empirical evidence and does not establish an awareness-modulated decoherence effect.

## Canonical script

Run from the repository root:

```bash
python papers/p4-soc-mzi-awareness-modulated-decoherence/simulations/soc_mzi_visibility_decay_simulation.py
```

The script writes default outputs to:

```text
papers/p4-soc-mzi-awareness-modulated-decoherence/simulations/results/
```

## Committed outputs

Committed CSV outputs:

```text
papers/p4-soc-mzi-awareness-modulated-decoherence/simulations/results/main_effect.csv
papers/p4-soc-mzi-awareness-modulated-decoherence/simulations/results/timing_asymmetry.csv
papers/p4-soc-mzi-awareness-modulated-decoherence/simulations/results/dose_response.csv
```

Output metadata and claim boundaries are documented in:

```text
papers/p4-soc-mzi-awareness-modulated-decoherence/simulations/results/README.md
```

## Generated but intentionally uncommitted

The script can also generate these PNG files:

```text
main_effect.png
timing_asymmetry.png
dose_response.png
```

These binary figures are intentionally treated as generated local artifacts rather than committed source artifacts. Regenerate them from the script when preparing a figure packet or review appendix.

## Relationship to legacy/import path

Earlier imported/support material remains under:

```text
simulations/mzi-visibility-decay/
```

The canonical P4 paper package should point here first. Legacy files should be treated as source-support history unless explicitly reconciled into this folder.

## Claim boundary

Use this package for planning, expected-signature visualization, simulation regression checks, and preregistration support. Do not describe these CSV outputs or generated figures as experimental findings.
