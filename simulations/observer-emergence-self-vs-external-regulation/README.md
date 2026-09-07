# O-1D2 — Self-Regulation vs Externally Informed Regulation

## Question
Does the O-1D-prep preservation advantage require information to be represented *inside* the regulated system, or is it simply ordinary feedback control available to any controller with the same state information?

## Conditions
- **internal** — current noisy health diagnostic drives maintenance.
- **external, zero latency** — an external controller receives the same diagnostic at the same time and uses the same policy.
- **external latency 2 / 8** — same controller with delayed diagnostic access.
- **shuffled** — placebo diagnostic unrelated to current health.

The policy is frozen across held-out degradation, diagnostic-noise, and repair-success regimes.

## Budget-matching correction
The first scaffold incorrectly inherited the health threshold into the shuffled control, causing a grossly unmatched maintenance rate (~72%). That run was not frozen or interpreted. The corrected benchmark explicitly calibrates each delayed/placebo control to the internal controller's maintenance rate within each regime. The zero-latency external controller uses the identical threshold because its state information is identical.

This correction is scientifically important: apparent preservation advantages are not interpretable if one controller simply receives more maintenance.

## Frozen result
Across all four tested regimes, the internal and zero-latency external controllers are numerically identical in accuracy, utility, mean health, low-health fraction, and maintenance rate.

Representative degradation = 0.03 regime:

| condition | accuracy | utility/step | mean health | low-health fraction | maintenance rate |
|---|---:|---:|---:|---:|---:|
| internal | 0.89890 | 0.898379 | 0.88972 | 0.00000 | 0.01303 |
| external, zero latency | 0.89890 | 0.898379 | 0.88972 | 0.00000 | 0.01303 |
| external latency 2 | 0.88173 | 0.881209 | 0.85105 | 0.00000 | 0.01303 |
| external latency 8 | 0.78596 | 0.785439 | 0.64054 | 0.37247 | 0.01302 |
| shuffled | 0.80929 | 0.808769 | 0.69134 | 0.25866 | 0.01303 |

The equality at zero latency is the decisive result:

\[
J_{\rm internal}=J_{\rm external}^{\tau=0}
\]

within the implemented model.

Delayed external regulation degrades performance despite matched maintenance budgets. This is consistent with a causal locality/latency advantage: state information is more useful when acted on promptly.

Destroying state alignment in the shuffled control also degrades preservation, confirming that timing maintenance from informative state diagnostics matters.

## Interpretation
O-1D-prep therefore demonstrates **state-informed feedback regulation and preservation of future capability**, but not a unique functional privilege for internal self-representation.

The strongest justified statement is:

> A system can use information about its own current condition to preserve future observational capacity, but an external controller with the same information and causal access can reproduce the effect exactly in this benchmark.

So:

\[
\boxed{\text{self-regulation} \neq \text{observerhood by itself}}
\]

and

\[
\boxed{\text{internal representation} \neq \text{functional privilege when causal access is matched}}
\]

## What the latency result does and does not mean
The delayed-controller penalty should be interpreted first as a control-theoretic consequence of stale information. It is not evidence of consciousness, intrinsic agency, or novel physics.

## Next discriminator
The next observer-emergence step should test whether a system gains any additional functional property when the self-model participates recursively in predicting and modifying its own future internal dynamics, rather than merely supplying a current-state feedback signal.

A suitable next design should compare:
1. ordinary state feedback,
2. predictive self-model control,
3. externally implemented predictive control with matched model access,
4. recursive self-model ablation,
5. model-mismatch and adversarial perturbation controls.

The key question becomes whether recursive self-modeling adds a causal capability not reducible to ordinary matched predictive control.

## Scope
This is ordinary stochastic control/information theory. It does not test consciousness or SoCT memory feedback.
