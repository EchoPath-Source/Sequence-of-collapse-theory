# O-1D3y — Regret-Balanced Randomized Hidden Dynamics

## Question
Does autobiographical self-dynamics identification improve held-out value when fixed strategies can no longer exploit asymmetric regret?

O-1D3x showed that a controller could perform well by always choosing the high-degradation policy because the two kinds of mistakes had unequal costs. O-1D3y first estimates the paired burst-1 minus burst-2 value difference across degradation levels, then freezes a more balanced pair of hidden regimes before the provenance test.

## Environment-identification step
Using 3,000 paired episodes per degradation value, burst-1 minus burst-2 value differences were:

- d=.02: +5.12, 95% CI [2.40, 7.84]
- d=.03: +4.27, 95% CI [0.92, 7.61]
- d=.04: +3.18, 95% CI [-0.91, 7.27]
- d=.06: +0.31, 95% CI [-4.27, 4.89]
- d=.07: -7.63, 95% CI [-12.29, -2.97]
- d=.09: -13.23, 95% CI [-17.88, -8.58]

The pair d=.02 and d=.07 was frozen because burst 1 and burst 2 are respectively favored with material, oppositely signed penalties of comparable order.

## Randomized held-out test
Each of 8,000 episodes samples d from `{.02,.07}` with equal probability. The controller is not told d. Own, matched external, shuffled, fixed-low, fixed-high, donor, and oracle controls use the same 140-step history and paired future streams. The classification boundary is fixed at d_hat=.045.

## Frozen result
Own autobiographical history:
- value 300.29;
- policy accuracy 93.0%;
- d_hat MAE 0.0143.

Controls:
- shuffled/fixed-high value 298.56, policy accuracy 50.8%;
- fixed-low value 297.93, policy accuracy 49.2%;
- donor value 295.63, policy accuracy 0%;
- oracle value 300.86, policy accuracy 100%.

Paired differences:
- own vs shuffled/fixed-high: +1.73, 95% CI [0.55, 2.92];
- own vs fixed-low: +2.36, 95% CI [0.35, 4.37];
- own vs donor: +4.66, 95% CI [2.41, 6.91];
- own vs oracle: -0.57, 95% CI [-1.19, 0.05].

Matched internal and zero-latency external own-history controllers are exactly equal.

## Interpretation
This gate supports a stronger ordinary-control result:

`when hidden self-dynamics are randomized and the costs of the two wrong policies are both material, autobiographical action–outcome history reduces held-out policy regret relative to fixed, shuffled, and mismatched-history controls.`

The internal implementation still has no functional privilege over an information- and timing-matched external controller.

The next loophole is base-rate dependence: a strongly skewed prior over hidden self-types can make one fixed policy rational again. The next gate therefore varies the prior probability of low versus high degradation and asks whether self-history remains valuable.
