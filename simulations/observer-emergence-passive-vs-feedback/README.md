# O-1A — Passive Memory vs Feedback

**Status:** Exploratory observer-emergence baseline  
**Purpose:** Test whether stored records become functionally different when they causally alter later information acquisition.

## Design

Both agents have the same one-bit memory capacity and receive noisy observations of the same kind of latent binary world.

The world is a binary Markov process with persistence `p`.

Two specialized sensors are available:

```text
sensor matched to current world state: 0.90 accuracy
nonmatched sensor:                      0.55 accuracy
```

### Passive-memory control

The agent stores the previous observation but does not use it. Its next sensor is chosen randomly.

### Feedback agent

The agent stores the previous observation and uses that record to choose the next specialized sensor.

Thus memory capacity is held fixed while causal reuse is ablated.

## Metrics

- observation accuracy;
- mutual information `I(World:Observation)`;
- gain produced by feedback relative to passive storage.

## Representative results

```text
world persistence   passive acc   feedback acc   acc gain   passive MI   feedback MI   MI gain
0.50                0.7263        0.7263         ~0.0000    0.1532       0.1532        ~0.0000
0.70                0.7264        0.7635          0.0371    0.1534       0.2109         0.0574
0.90                0.7259        0.8137          0.0878    0.1527       0.3063         0.1536
0.97                0.7270        0.8365          0.1095    0.1542       0.3574         0.2032
```

## Interpretation

When the environment has no temporal structure (`p=0.5`), causal reuse of memory gives essentially no advantage.

As environmental persistence rises, stored records become predictive of the near future. The feedback agent can then use memory to choose a better sensor, increasing both accuracy and acquired information.

This demonstrates a clean functional distinction:

```text
passive record persistence
!=
causally reused record persistence
```

The result is expected from ordinary information/control theory. It is not new physics.

## Relevance to Track 1

O-1A suggests defining a separate quantity such as

```math
Gamma_use
```

for the causal reuse of stored records. It should remain distinct from the current Track-1 record-production source

```math
Gamma_rec.
```

A later question is whether two histories with equal `Gamma_rec` but different `Gamma_use` ever produce a physical difference after ordinary present-state matching. That would require a separate preregistered experiment and must not be assumed from this simulation.

## Next O-1 gate

O-1B should add an internal-state estimate and compare:

```text
external-world-only prediction/control
vs
external-world + self-state model
```

followed by self-model ablation in O-1C.

## Claim boundary

This simulation shows that memory can have greater functional value when embedded in a closed causal loop. It does not show consciousness, observer-dependent collapse, or a SoCT memory field.
