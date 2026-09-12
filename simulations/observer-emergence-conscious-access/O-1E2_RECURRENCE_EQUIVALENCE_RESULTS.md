# O-1E2 — Recurrent Processing Equivalence Test

## Purpose
Test whether recurrence itself provides a unique functional advantage once evidence and final decision rule are held fixed. This targets recurrent-processing-style hypotheses at the functional level only.

## Design
A latent binary state generates seven noisy observations. The recurrent condition accumulates observations sequentially. The batch feedforward condition receives the exact same seven observations and sums them once at the end. A last-observation-only control is included for reference.

N = 100,000 held-out episodes. Noise SD = 1.5.

## Frozen results
- last-observation-only accuracy: 0.74558
- recurrent accumulator accuracy: 0.96178
- batch feedforward integrator accuracy: 0.96178
- recurrent minus batch: 0.00000
- maximum prediction disagreement: 0

## Interpretation
Temporal evidence integration is highly useful, but recurrence is not uniquely privileged when a non-recurrent architecture receives exactly the same evidence and implements the same sufficient statistic.

Therefore O-1 should distinguish:

`temporal integration / persistence`

from

`recurrence as a specific implementation mechanism`.

This is a negative discriminator against treating recurrence alone as an observerhood or consciousness marker.