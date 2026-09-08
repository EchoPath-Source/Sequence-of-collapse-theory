# O-1D3z — Base-Rate Shift and Prior-Conditioned Self-Inference

## Question
Does autobiographical self-dynamics inference remain useful when the hidden self-type prior changes, or is its value an artifact of a 50/50 regime mixture?

This follows O-1D3y, where own history significantly reduced held-out policy regret for a regret-balanced randomized pair `d in {.02,.07}`.

## Phase A — base-rate shift with the fixed O-1D3y classifier
The hidden low-degradation probability is varied across `p_low = .25, .50, .75`. The same fixed threshold (`d_hat=.045`) is used without telling the controller the realized regime.

Results:

| p_low | own value | own policy accuracy | fixed-low value | fixed-high/shuffled value |
|---:|---:|---:|---:|---:|
| .25 | 268.98 | .923 | 266.04 | 267.65 |
| .50 | 305.49 | .921 | 304.55 | 301.68 |
| .75 | 335.68 | .920 | 336.44 | 330.10 |

Paired own-vs-best-static differences:
- p_low=.25: +1.33, 95% CI [0.23, 2.43];
- p_low=.50: +0.94, 95% CI [-1.12, 3.00];
- p_low=.75: -0.76, 95% CI [-2.31, 0.79].

Own history still beats the systematically high/shuffled policy at all three priors, but when the population is strongly low-degradation, the fixed-low strategy becomes competitive and slightly higher in the finite held-out sample.

### Interpretation
Accurate self-history is not automatically valuable when a strong population prior already makes one action nearly optimal. The correct next comparison is not 'history versus no prior'; it is **history plus prior versus prior alone**.

## Phase B — Bayesian prior + autobiographical likelihood
Independent training histories estimate the distribution of the autobiographical degradation estimate under the two hidden regimes:
- low d=.02: mean d_hat=.02679, SD=.01201;
- high d=.07: mean d_hat=.07641, SD=.02169.

Independent future evaluation estimates the policy payoff matrix:
- low d, burst1: 372.23;
- low d, burst2: 366.19;
- high d, burst1: 226.22;
- high d, burst2: 228.38.

A prior-conditioned controller combines the population prior with the autobiographical likelihood, computes a posterior over the two self-dynamics regimes, and chooses the burst with greater posterior expected value. Training and held-out future streams are separate.

Held-out results (8,000 episodes per prior):

| p_low | Bayesian-own value | policy accuracy | shuffled/prior-high value | fixed-low value | oracle value |
|---:|---:|---:|---:|---:|---:|
| .25 | 264.50 | .920 | 263.38 | 261.28 | 264.37 |
| .50 | 301.88 | .917 | 299.48 | 301.07 | 302.37 |
| .75 | 337.42 | .944 | 334.42 | 337.32 | 337.78 |

Paired Bayesian-own differences:
- p_low=.25 vs shuffled/fixed-high: +1.12, 95% CI [0.08, 2.16];
- p_low=.50 vs shuffled/fixed-high: +2.40, 95% CI [1.05, 3.75];
- p_low=.75 vs shuffled/fixed-high: +2.99, 95% CI [1.56, 4.43].

Against the best strong-prior static policy, the advantage becomes small and often unresolved, especially at p_low=.75 where fixed-low is already highly appropriate. Bayesian-own remains statistically indistinguishable from oracle at all three tested priors.

A coarse value-of-information sweep from p_low=.1 to .9 shows the same qualitative pattern: self-history is most valuable near decision boundaries where the prior alone does not settle the action, and has little incremental value when one static action is already strongly favored. Finite-sample estimates are noisy and are not promoted as a smooth law.

## Strongest supported result

`autobiographical self-history can reduce policy regret under randomized hidden self-dynamics, and its incremental value is conditional on prior uncertainty and on whether the hidden self-state changes the rational action.`

This is a stronger adaptive-control result than regime-by-regime evaluation, but it still does not establish intrinsic agency, consciousness, phenomenology, or privileged internal location. The zero-latency external implementation remains functionally equivalent when given identical information and authority.

## Next gate
The Bayesian phase uses a Gaussian approximation to the learned self-history estimator distribution. A stricter next test should replace that approximation with an independently calibrated empirical likelihood or reliability model, then evaluate **posterior calibration, regret, and out-of-distribution prior shift**. The goal is to test whether the system can know not only an estimate of itself, but how uncertain that self-estimate is.
