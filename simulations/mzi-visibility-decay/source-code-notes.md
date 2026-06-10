# SOC MZI Visibility Decay Simulation — Source Code Notes

**Canonical path:** `simulations/mzi-visibility-decay/SOC MZI Visibility Decay Simulation.py`  
**Status:** Imported source artifact requiring cleanup  
**Claim level:** Simulation scaffold; not experimental evidence

---

## Purpose

This note documents the current state of the imported SOC-MZI simulation script and explains how it should be treated in the repository.

The script is intended to model a minimal awareness-modulated dephasing scenario for Mach-Zehnder visibility decay using the phenomenological form:

```text
lambda_eff = lambda_env + lambda_c * A(t)
V(tau, A) = V0 * exp[-lambda_eff * tau]
```

This makes it a useful **source artifact** for the P4 experiment track and for the simulation summary already stored in this folder.

---

## Current repository state

The script has been imported into the canonical simulation folder, but the currently uploaded version appears to be **truncated/incomplete**.

That means it should presently be treated as:

- a provenance-preserving source import,
- a placeholder for later repair,
- and not yet a fully runnable reproducibility artifact.

---

## What the script is for

The script is intended to support three core qualitative predictions:

1. **Main effect** — higher `A` produces faster visibility suppression
2. **Timing asymmetry** — early pulses suppress more strongly than late pulses
3. **Dose response** — suppression scales monotonically with `A`

Those predictions align with the P4 preregistration draft and the `model-summary.md` already present in this folder.

---

## Repo-safe interpretation

Use:

> The imported script preserves the original simulation logic used to motivate the SOC-MZI experimental design, but the current copy requires cleanup before it can serve as a reproducibility-grade code artifact.

Avoid:

> The simulation script proves the P4 hypothesis.

---

## Recommended next work

1. Replace or repair the truncated script with a complete runnable version.
2. Add a notebook or clean Python module version with documented dependencies.
3. Add expected output descriptions and parameter notes.
4. Cross-link the cleaned script to:
   - `simulations/mzi-visibility-decay/model-summary.md`
   - `experiments/quantum/mach-zehnder-consciousness-test.md`
   - `papers/p4-soc-mzi-awareness-modulated-decoherence/SOC-MZI-01-preregistration.md`
5. Keep the script labeled as a simulation scaffold unless and until it passes a reproducibility review.

---

## Bottom line

The current script is worth keeping because it preserves provenance and modeling intent, but it should not yet be treated as the final canonical implementation for the SOC-MZI simulation track.