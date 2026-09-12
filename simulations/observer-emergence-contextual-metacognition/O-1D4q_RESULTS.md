# O-1D4q — Latent Environment Inference

## Question
Can the controller infer environment base-rate context from experience, rather than receiving a context label, and use that inferred context for self-information regulation?

## Design
True p_low is randomized over {0.25, 0.50, 0.75}. Before the focal decision, the controller observes 30 independent population histories and estimates the context from classified low/high dynamics with beta smoothing, snapping to the three preregistered context classes. It then combines inferred context with its autobiographical self-estimate and the O-1D4p source maps. Evaluation uses 5,000 new episodes.

## Frozen results
Context inference accuracy: 0.7376.

| arm | mean value |
|---|---:|
| inferred-context | 303.3605 |
| balanced | 303.5888 |
| shuffled inference | 303.0352 |
| none | 303.4324 |
| cheap | 303.4286 |

Inferred-context minus controls, paired 95% CI:
- balanced: -0.2283 [-0.9520, 0.4954]
- shuffled inference: +0.3253 [-0.5353, 1.1859]
- none: -0.0719 [-0.9145, 0.7708]
- cheap: -0.0680 [-0.8798, 0.7438]

## Interpretation
The system can infer coarse environment context substantially above chance, but that inferred world-model does not yet yield reliable downstream information-policy value. Environment identification and useful contextual control are therefore separate gates, paralleling the earlier distinction between self-model accuracy and policy value.

No active contextual-metacognition claim is promoted from this experiment.