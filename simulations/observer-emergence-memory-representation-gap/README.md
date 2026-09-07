# O-1D3j — Memory Representation Under an Observation Gap

## Question
Does the ordered autobiographical sequence contain behaviorally useful information beyond compressed summaries of recent self-state?

## Design
At step 200 fresh self-observation is withheld for 40 steps. The same recent diagnostic history is reconstructed using an ordered exponential filter, a matched external ordered filter, arithmetic mean, last sample, median, shuffled exponential filter, zero memory, and oracle current state. Potential-outcome streams are paired across arms.

## Frozen result
Ordered history is useful in the moderate regime, but no representation dominates robustly across the full grid.

At degradation 0.08:

- ordered filter: reward 313.19, lifetime 421.84, failure 0.288;
- mean: 308.44, 415.41, 0.308;
- last sample: 308.72, 415.62, 0.314;
- shuffled filter: 306.76, 413.03, 0.322;
- zero memory: 299.58, 403.51, 0.354;
- oracle: 315.01, 424.52, 0.280.

This is compatible with ordered recent history carrying useful state information. However at degradation 0.12 the last-sample and median representations outperform the ordered filter, and zero memory is not consistently worst. Therefore temporal sequence itself has not earned a general privileged status.

Internal and matched external ordered-filter arms are identical.

## Interpretation
Supported:

`memory representation matters under information gaps`.

Not supported:

`ordered autobiographical sequence is universally superior to compressed state summaries`.

The next discriminator should make temporal action-outcome structure explicitly decision-relevant rather than merely using a history of noisy state samples. O-1D3k therefore tests whether records of the system's own actions and subsequent state changes help identify hidden degradation dynamics.
