# Recursive Universe Figure Provenance Notes

**Status:** Static figure documentation / images not yet committed  
**Related files:**

```text
simulations/recursive-universe/README.md
simulations/recursive-universe/exploratory-analysis-v0-1.md
simulations/recursive-universe/testable-framework-v2-summary.md
```

---

## Figure 1 — Recursive Universe Summary

Uploaded image contents:

```text
3D Power Spectra
Transfer Function (1D slice)
Child "CMB" Map
Child "CMB" Angular Power
```

This figure corresponds to the v1 exploratory parent-to-child memory-transfer toy model.

Panels:

1. Parent density, parent memory, and child perturbation power spectra.
2. Transfer function magnitude as a function of k.
3. 2D projected child CMB-like map.
4. Toy angular power spectrum.

Intended future output path:

```text
simulations/recursive-universe/figures/recursive_universe_summary.png
```

---

## Figure 2 — Falsifiability / Non-Gaussianity Constraint

Uploaded image contents:

```text
Non-Gaussianity Constraint
Observability (green = falsifiable)
```

This figure corresponds to the v2 testable framework.

Panels:

1. Predicted `f_NL` versus coupling `eta`, with Planck-like threshold line.
2. Fractional `Delta C2 / C2` observability versus coupling.

Interpretation:

> Strong coupling becomes constrained by non-Gaussianity; weak coupling becomes difficult to observe.

Intended future output path:

```text
simulations/recursive-universe/figures/falsifiability_analysis.png
```

---

## Figure 3 — CMB Power Spectrum Comparison

Uploaded image contents:

```text
CMB Power Spectrum: Standard vs Memory-Modified
Inflation only
Inflation + Memory (eta=0.003)
```

This figure corresponds to the v2 toy CMB calculator.

Interpretation boundary:

> This is not a CLASS/CAMB result. It is a simplified pedagogical power-spectrum comparison and should not be treated as a real CMB likelihood analysis.

Intended future output path:

```text
simulations/recursive-universe/figures/cmb_power_spectrum_comparison.png
```

---

## Required Reproducibility Steps

Before using any of these figures in public scientific material:

1. Commit source scripts under `simulations/recursive-universe/src/`.
2. Record exact parameters and random seeds.
3. Regenerate all figures from committed code.
4. Document Python package versions.
5. Label all outputs as toy-model figures unless replaced by CLASS/CAMB.
6. Do not compare to Planck maps until statistics are pre-defined.

---

## Research Boundary

These figures are useful for internal model development and constraint thinking.

They are not evidence for:

- parent universes;
- Causal Inversion Hypothesis;
- SoCT;
- memory transfer into the real CMB.

The scientifically useful outcome is the constraint structure:

```text
observable memory transfer must evade non-Gaussianity limits while producing a measurable low-ell signature.
```
