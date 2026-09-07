# O-1D3k — Action–Outcome Autobiography Under Hidden Degradation Dynamics

## Question
Can the system's own action–outcome history identify a hidden self-dynamics parameter that matters during a later observation gap, and does that improved self-knowledge improve behavior?

## Design
Before a 60-step diagnostic gap, the controller records recent `(action, pre-diagnostic, post-diagnostic)` tuples. For WORK actions it estimates degradation probability from abrupt state drops. The paired-history arm is compared with a matched external controller, shuffled action–outcome pairing, compressed-state/zero-memory controls, donor history, and oracle knowledge of the true degradation rate. Potential-outcome streams are paired across arms.

## Frozen result
The autobiographical estimator is substantially better at identifying the hidden degradation rate than shuffled or donor-history controls, especially in the harder regimes.

At true degradation 0.12:

- own paired-history estimate error: 0.0321;
- shuffled-pairing error: 0.1035;
- compressed/zero prior error: 0.0700;
- donor-history error: 0.1000;
- oracle: 0.

However improved self-dynamics knowledge does **not** translate monotonically into reward or survival under the frozen policy.

At true degradation 0.12:

- own paired history: reward 284.41, lifetime 431.83, failure 0.253;
- shuffled pairing: reward 303.05, lifetime 454.14, failure 0.163;
- oracle: reward 308.27, lifetime 444.94, failure 0.193.

The shuffled control performs better behaviorally despite a far worse degradation estimate because its biased estimate induces a more conservative maintenance policy. Similar inversions occur at lower degradation.

Internal and matched zero-latency external paired-history controllers are identical.

## Interpretation
Supported:

`temporally paired autobiographical action–outcome records can improve identification of hidden self-dynamics`.

Not supported:

`better autobiographical self-knowledge automatically improves policy value`.

This repeats, in a more demanding memory setting, the model-versus-policy separation found in O-1D3b/O-1D3c: self-knowledge, prediction, policy, and realized value must be tested separately.

## Next gate
The next experiment should hold the self-dynamics estimate fixed and explicitly calibrate the maintenance policy to realized continuation value on a training set, then evaluate on held-out paired episodes. That would test whether autobiographical information becomes behaviorally useful once the model-to-policy mapping is correctly calibrated, without rewarding self-preservation directly.

This is synthetic ordinary control theory only; no consciousness or novel-physics claim.
