# O-1D3x — Randomized Hidden Self-Dynamics

## Question
Can one fixed autobiographical estimator infer which hidden self-dynamics regime an agent occupies when the regime is randomized before each episode, rather than evaluated one regime at a time?

This directly attacks the O-1D3w loophole where a fixed prior or systematically biased estimator could win by always choosing one side of the burst-policy boundary.

## Design
Each episode independently samples hidden degradation `d` from `{0.04, 0.08}` with equal probability. The controller is not told which regime was sampled.

Each episode then:
1. generates a 140-step action–outcome history under a fixed exploratory controller;
2. estimates hidden degradation from WORK-action pre/post state changes;
3. selects maintenance burst 1 if `d_hat < 0.06`, otherwise burst 2;
4. resets current state and evaluates the selected burst on a paired future stream.

Controls:
- own autobiographical history;
- matched zero-latency external copy;
- shuffled action–outcome pairing;
- fixed-low prior;
- fixed-mid/high prior;
- donor/mismatched regime;
- oracle.

Evaluation uses 6,000 randomized episodes with paired future streams across arms.

## Frozen result
Own history classified the correct burst on 83.3% of episodes and estimated degradation with MAE 0.0166. However, held-out value was 262.13 versus 261.70 for shuffled/fixed-high and 259.58 for fixed-low.

Paired differences:
- own vs shuffled/fixed-high: +0.43, 95% CI [-1.59, 2.45];
- own vs fixed-low: +2.55, 95% CI [0.20, 4.89];
- own vs donor: +3.82, 95% CI [0.99, 6.65];
- own vs oracle: -0.85, 95% CI [-2.09, 0.40].

The estimator clearly identifies self-dynamics better than shuffled or fixed controls, but it does not significantly beat the always-high/shuffled strategy on value.

## Interpretation
The failure is not due to classification accuracy. It is due to **asymmetric policy regret**: choosing burst 2 in the low-degradation regime is less costly than choosing burst 1 in the high-degradation regime. A biased strategy can therefore score well without knowing the hidden self-state.

The next gate must identify a pair of regimes where the penalties for the two wrong choices are comparably large before testing autobiographical provenance again.

This remains ordinary adaptive control; it is not evidence of consciousness or novel physics.
