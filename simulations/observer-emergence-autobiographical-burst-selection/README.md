# O-1D3w — Autobiographical Maintenance-Burst Selection

## Question
Given two independently reproduced policy basins — d=0.04 -> burst 1 and d=0.08 -> burst 2 — can the system's own action–outcome history identify its hidden degradation dynamics well enough to select the better maintenance duration on a held-out future?

## Design
Each episode first generates an independent 140-step autobiographical history using a fixed exploratory controller. The held-out evaluation then resets present state and applies a burst policy selected from the history estimate:

- estimate < 0.06 -> burst 1
- estimate >= 0.06 -> burst 2

Compare own paired action–outcome history, matched external own history, shuffled pairing, compressed/zero estimate, donor estimate, and oracle. Future evaluation streams are paired across arms. Main frozen table uses 2,200 episodes per arm; key contrasts are rechecked with 4,000 paired episodes and 95% confidence intervals.

## Frozen result
### d = 0.04
Own history estimates self-dynamics accurately (MAE 0.0143) and selects burst 1 on 80.8% of episodes. Mean value is 314.50, compared with 310.59 for shuffled/donor histories, which always select the wrong burst. However, a simple compressed/zero estimate of 0.05 happens to select the correct low-d policy perfectly and reaches 314.68.

The paired own-vs-shuffled difference is +2.84 value units, but its 95% CI [-0.17, 5.84] narrowly crosses zero. Own-vs-zero is +0.16 with 95% CI [-1.39, 1.71].

### d = 0.08
Own history selects burst 2 on 87.2% of episodes and yields value 210.11. Zero/compressed/donor controls select the wrong burst and yield 207.45. The 4,000-episode paired own-vs-zero difference is +5.72 with 95% CI [2.05, 9.40], a positive held-out advantage.

Shuffled history, despite very poor dynamics estimation (MAE 0.2013), always selects burst 2 in this regime and therefore matches the oracle policy. Own-vs-shuffled is -1.38 with 95% CI [-2.83, 0.06].

Matched internal and zero-latency external own-history controllers are exactly equal.

## Interpretation
O-1D3w establishes a narrower positive result:

`accurate autobiographical self-dynamics can improve held-out action selection relative to uninformative controls when the hidden dynamics change which discrete policy is better.`

But it still does not establish uniquely privileged autobiographical provenance. A biased shuffled estimator can accidentally land on the correct coarse action, and a fixed prior can be optimal in one regime.

The stronger future discriminator should therefore evaluate **regret across randomized hidden dynamics**, with neither fixed prior nor systematic estimator bias able to win by always choosing one side of the boundary. Hidden d should be randomized across both policy basins before history is generated, then the same estimator must generalize without knowing which basin it is in.

This remains ordinary adaptive control and does not establish agency, consciousness, or novel physics.
