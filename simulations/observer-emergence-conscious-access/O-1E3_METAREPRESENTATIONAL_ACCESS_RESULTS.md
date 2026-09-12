# O-1E3 — Metarepresentational Access Comparison

## Purpose
Test whether making a representation of first-order reliability explicitly available improves downstream reportability without changing first-order task performance. This is a functional metacognition/access test, not a consciousness test.

## Design
A latent binary state generates three noisy cues. A first-order classifier pools the cues to choose the latent state. An explicit metarepresentational channel exposes absolute decision evidence |score| to a downstream correctness-report head. The no-meta control receives only the categorical first-order decision and therefore reports the majority correctness class. A threshold for the explicit meta channel is fitted on an independent calibration half and frozen before held-out evaluation.

N = 120,000 total episodes; 60,000 calibration and 60,000 held-out. Noise SD = 1.4.

## Frozen results
- first-order held-out accuracy: 0.89137
- fitted confidence threshold: 2.08317
- no-meta balanced accuracy for predicting own correctness: 0.50000
- explicit-meta balanced accuracy: 0.77916

## Interpretation
Explicit access to a representation of first-order reliability substantially improves the ability to report whether the first-order decision is likely correct, while leaving the first-order decision itself unchanged.

This supports a clean distinction:

`task performance != access to a representation of task reliability`.

The result operationalizes an R5-like metarepresentational-access function. It does not establish subjective confidence, awareness, sentience, or consciousness.