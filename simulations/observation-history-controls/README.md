# Simulation 4b — Adversarial History Controls

**Status:** Control/falsification toy model  
**Purpose:** Test whether the Simulation 4 history-dependent phase signature is identifiable once ordinary nuisance effects are admitted.

## Why this simulation exists

Simulation 4 showed that an explicit SoCT memory coupling

```math
H_M = lambda_M M(t) sigma_z
```

produces an additional phase

```math
Delta phi_M(t)
  = lambda_M Delta M_0 [1-exp(-beta t)]/beta.
```

That is a clean mathematical discriminator only if ordinary physical effects cannot generate the same time dependence.

Simulation 4b therefore attacks the discriminator with mundane nuisance terms:

```text
constant arm-to-arm offset
linear frequency mismatch
quadratic slow drift
Gaussian measurement noise
```

The candidate memory basis is

```math
f_M(t) = [1-exp(-beta t)]/beta.
```

The nuisance basis is

```text
1, t, t^2.
```

## Main result

Over the finite window `t in [0,8]`, the memory basis is highly approximable by smooth low-order nuisance terms.

Representative coefficient of determination when fitting `f_M(t)` using only `1,t,t^2`:

```text
beta=0.02 -> R^2 = 0.999999915
beta=0.05 -> R^2 = 0.999996681
beta=0.10 -> R^2 = 0.999947824
beta=0.25 -> R^2 = 0.998187332
beta=0.50 -> R^2 = 0.979778065
beta=1.00 -> R^2 = 0.876045638
```

This means the simple phase trajectory from Simulation 4 is **not by itself a robust experimental signature** for slowly decaying memory. Frequency mismatch and smooth drift can absorb nearly all of the candidate signal over realistic finite windows.

## Noisy-fit stress test

The script also fits the model

```math
y(t)=a_0+a_1 t+a_2 t^2+lambda_M f_M(t)+epsilon(t).
```

Representative runs show the identifiability problem directly:

```text
null, low noise:
  true lambda_M = 0
  fitted lambda_M ~ 0.037 +/- 0.040

signal, low noise:
  true lambda_M = 0.03
  fitted lambda_M ~ 0.039 +/- 0.034

signal, high noise:
  true lambda_M = 0.03
  fitted lambda_M ~ -0.004 +/- 0.194

slow-memory signal:
  true lambda_M = 0.03, beta=0.02
  fitted lambda_M ~ -0.047 +/- 2.395
```

These are illustrative seeded toy realizations, not parameter estimates from data.

## Scientific interpretation

Simulation 4b does **not** falsify SoCT memory feedback.

It falsifies a weaker methodological claim:

> A single smooth history-dependent phase trajectory is sufficient to identify a unique SoCT memory term.

It is not sufficient.

A credible experiment must break the nuisance degeneracy by changing the experimental design, not merely by collecting a prettier phase curve.

## Revised discriminator requirements

A stronger design should include at least one of:

1. **Randomized history assignment** — prepare matched present states, then randomly assign different prior record-production histories while interleaving readout order.
2. **History-dose response** — vary prior durable-record production while holding the present quantum state and hardware configuration fixed.
3. **History-label reversal / crossover** — swap which physical arm receives which history so fixed hardware offsets change sign relative to the treatment label.
4. **Multiple beta/time-scale signatures** — use preparation protocols predicted to generate distinct memory-decay scales rather than fitting one smooth curve.
5. **Blinded nuisance calibration** — estimate frequency mismatch and drift independently of history labels.
6. **Null-history sham protocol** — execute the same timing/control sequence without producing the record history.

## Pass/fail gate

Simulation 4 should not progress directly to a laboratory claim.

The next design gate is passed only if a history-conditioned effect can be recovered under randomized/crossover treatment while remaining non-identifiable from ordinary nuisance covariates alone.

Operationally:

```text
PASS:
  history label/dose predicts residuals after nuisance calibration,
  label reversal tracks history rather than hardware,
  sham histories do not reproduce the effect.

FAIL:
  residual disappears after nuisance modeling,
  follows a fixed arm/device rather than randomized history,
  or can be reproduced by sham timing/drift controls.
```

## Next simulation

### Simulation 4c — randomized history-dose crossover

Construct repeated trials with:

```text
same present quantum target state
randomized prior history dose
randomized/crossed physical arm assignment
independent drift and frequency nuisance
blinded analysis model
```

The target question becomes:

> Does a residual follow experimentally assigned **history** rather than elapsed time, hardware identity, or smooth environmental drift?

That is a substantially stronger SoCT discriminator than the original single-trajectory phase test.

## Claim boundary

This entire package is synthetic and exploratory. The result strengthens experimental design by identifying a major confound. It is not evidence for an SoCT memory field.
