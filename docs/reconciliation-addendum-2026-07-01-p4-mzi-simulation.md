# Reconciliation Addendum — P4 SOC-MZI Simulation Outputs

**Date:** 2026-07-01  
**Scope:** P4 SOC-MZI visibility-decay simulation package and generated output policy.

## Summary

This addendum records a focused P4 cleanup after the 2026-06-10 repository reconciliation. It does not replace the main reconciliation document; it narrows one previously incomplete P4 simulation item.

## Updated status

The canonical P4 paper folder now includes a runnable visibility-decay simulation script and committed CSV outputs:

```text
papers/p4-soc-mzi-awareness-modulated-decoherence/simulations/soc_mzi_visibility_decay_simulation.py
papers/p4-soc-mzi-awareness-modulated-decoherence/simulations/README.md
papers/p4-soc-mzi-awareness-modulated-decoherence/simulations/results/README.md
papers/p4-soc-mzi-awareness-modulated-decoherence/simulations/results/main_effect.csv
papers/p4-soc-mzi-awareness-modulated-decoherence/simulations/results/timing_asymmetry.csv
papers/p4-soc-mzi-awareness-modulated-decoherence/simulations/results/dose_response.csv
```

The script is documented to run from the repository root:

```bash
python papers/p4-soc-mzi-awareness-modulated-decoherence/simulations/soc_mzi_visibility_decay_simulation.py
```

## Reconciled item

The P4 simulation gap is now partially resolved:

- The canonical paper-local simulation script is present.
- The default output directory resolves to the script-local `results/` directory.
- CSV outputs for main effect, timing asymmetry, and dose response are committed.
- Generated PNGs are intentionally excluded from source control and should be regenerated locally unless promoted later through a figure-provenance pass.

## Still incomplete

The broader P4 package still needs:

- full OSF export if available;
- dedicated materials/measures appendix;
- dedicated statistical analysis plan appendix;
- AI observer control-arm implementation details;
- notebook-grade reproducibility wrapper or review packet;
- lab collaboration packet.

## Claim boundary

These files are simulation-informed expected signatures for planning and falsification scaffolding. They are not empirical evidence and do not establish an awareness-modulated decoherence effect.
