# O-1D3e — Instrumental Self-Preservation Under a Continuation Constraint

## Question
Can preservation behavior emerge without assigning direct reward to internal health?

The agent earns reward only from successful `WORK` actions. `MAINTAIN` produces no direct reward and consumes a time step. If internal health falls below a failure boundary, the episode terminates and all future reward opportunities disappear.

Thus maintenance can become useful only because preserving the system preserves future access to reward-producing sensing/action.

## Conditions
1. **Myopic** — always work; no continuation model.
2. **Threshold** — hand-coded maintenance below a present-state threshold.
3. **Continuation internal** — compares short-horizon expected future reward under `WORK` versus `MAINTAIN` using current internal-state information.
4. **Continuation external, zero latency** — identical state information, predictive model, and action rule implemented externally.
5. **Continuation external, latency 4** — same external controller with stale state information.

No condition receives reward for health itself.

## Frozen result
Across all four stress regimes, the continuation controller chose nonzero maintenance and prevented failure in every simulated episode despite receiving no direct health reward.

Representative medium regime:

```text
p_degrade = 0.05
myopic:
  reward/episode = 25.3587
  mean lifetime  = 33.614
  failure rate   = 1.000
  maintenance    = 0

threshold:
  reward/episode = 190.1013
  mean lifetime  = 258.5013
  failure rate   = 0.7807
  maintenance    = 0.0725

continuation internal:
  reward/episode = 403.2907
  mean lifetime  = 500.0
  failure rate   = 0
  maintenance    = 0.1039

continuation external, zero latency:
  reward/episode = 403.2907
  mean lifetime  = 500.0
  failure rate   = 0
  maintenance    = 0.1039

continuation external, latency 4:
  reward/episode = 242.88
  mean lifetime  = 351.5167
  failure rate   = 0.5233
  maintenance    = 0.2107
```

At the harshest regime (`p_degrade = 0.12`), the continuation controller still eliminated simulated failures across the 500-step episode cap, but required a maintenance rate of 0.3538 and produced lower reward per step. This illustrates the expected preservation/performance tradeoff.

## Interpretation
The central result is:

`no direct health reward + continuation constraint -> maintenance can emerge instrumentally`

The system preserves its own capability because losing that capability eliminates future opportunities to perform the reward-producing task.

This is a stronger operational notion than directly rewarding self-preservation. The preservation behavior is derived from continuation value rather than inserted as an explicit terminal preference.

However:

`J_continuation_internal = J_continuation_external_zero_latency`

for every frozen regime. Therefore the result does **not** establish a unique functional privilege for internally represented self-state. An external controller with the same information and causal access reproduces the behavior exactly.

The latency-4 deficit is interpreted as stale-information/locality cost, not intrinsic agency.

## Observer-emergence implication
O-1D3e supports the following functional step:

```text
continued task opportunity
-> future-value representation
-> present internal-state relevance
-> maintenance action
-> preserved future sensing/action capability
```

This justifies calling the behavior **instrumental self-preservation** in the limited control-theoretic sense.

It does not establish:
- subjective desire to survive,
- intrinsic goals,
- consciousness,
- phenomenology,
- objective collapse,
- SoCT memory feedback,
- new physics.

## Revised next gate
The next discriminator should test **causal closure and controller relocation** rather than merely stronger prediction.

Question:

> If the estimator, continuation-value model, and action-selection loop are progressively moved outside the regulated system while information, computation, latency, and actuation are matched, is there any functional boundary at which the organization ceases to qualify as self-regulation?

The null expectation is that location alone should not matter. A defensible observer-like boundary must therefore be defined by causal organization, not by arbitrary physical placement of a controller.
