# Representational Novelty Mining

**Status:** exploratory hypothesis-generation method  
**Claim level:** research heuristic only  
**Epistemic rule:** source analogy is never treated as physical evidence.

## Purpose

This track tests whether deliberately distant representational domains — including mythology, ancient cosmology, metaphysics, philosophy, mathematics, biology, computation, and modern physics — can generate scientifically useful structural questions that survive independent mathematical and empirical scrutiny.

The method does **not** assume that ancient or esoteric sources encode modern physics.

The workflow is:

```text
source structure
-> abstract relation
-> candidate scientific question
-> remove the source
-> mathematical model
-> nulls / adversaries
-> simulation or derivation
-> prior-art search
-> empirical test
```

A candidate is retained only if it remains scientifically meaningful after the originating source is deleted.

## Primary safeguards

1. **Structural, not lexical, matching.** Shared vocabulary is weak evidence.
2. **Reverse mapping.** Ask whether ordinary human experience would naturally generate the same metaphor even without hidden scientific knowledge.
3. **Negative controls.** Test whether unrelated texts can be made to fit equally well.
4. **Mathematical compression.** Remove narrative language and express the surviving relation using state variables, operations, constraints, or geometry.
5. **Falsification before interpretation.** Predeclare what would make the candidate fail.
6. **Prior art after derivation.** First record the independently generated structure, then search literature to classify it as known, rediscovered, adjacent, or potentially novel.
7. **No source privilege.** A successful scientific hypothesis does not validate the metaphysical or historical source that inspired it.

## First candidate: RM-01

The first full run started from creation/order/observation motifs and progressively stripped away the source language.

The surviving abstraction was:

```text
indistinction
-> distinction
-> persistent record
-> structured record relations
-> causal/event structure
-> candidate geometry
```

The scientifically useful target became:

> Can classical/effective geometry be reconstructed from relationships among persistent, redundantly accessible physical records?

The original source is not required by the hypothesis and is not used as evidence.

## RM-01 simulation ladder

The benchmark series is stored at:

```text
experiments/observation-foundations/rm01-record-geometry/
```

### RM-01 — first metric gate

```text
structured local persistent record overlap -> recoverable hidden geometry
matched redundant scrambled records        -> no geometry recovery
matched homogeneous global records         -> no geometry recovery
binary variation-of-information candidate  -> fails first metric gate
```

The first important negative result was that binary variation-of-information did not recover the hidden geometry. Jaccard support distance did.

### RM-01B — held-out geometry families

A fixed Jaccard reconstruction generalized across cycle, torus, irregular, bottleneck, shortcut, and variable-speed families.

The shortcut benchmark showed that record relations follow **effective propagation geometry** more strongly than a supplied background embedding when genuine low-cost nonlocal routes are introduced.

### RM-01C — remove global distance from record generation

RM-01C removed the explicit distance-decay generator.

Records instead arise from repeated local transition dynamics:

```text
local edge rules
-> propagated influence
-> persistent records
-> relational support geometry
```

No all-pairs distance or coordinate is used to generate record probability.

Across six families, local record geometry remained strongly correlated with effective propagation geometry while scrambled/global controls collapsed toward zero.

### RM-01D — higher-structure reconstruction

RM-01D asks whether the record representation contains more than pairwise distance.

Using a family-agnostic reconstruction supplied only with persistent record supports, the first 30-seed benchmark finds:

```text
mean local direct-edge ROC AUC  = 0.978
scrambled/global edge ROC AUC   = ~0.505

bottleneck partition ARI        = 1.000
shortcut closeness percentile   = 0.996
```

An equal-size, fixed-record-density dimension suite separately compares a 64-node cycle, 64-node 2-D torus, and 64-node 3-D torus.

The record-only local growth estimator preserves

```text
cycle < 2-D < 3-D
```

in all `30 / 30` local seeds, versus `6 / 30` scrambled and `0 / 30` global controls.

The numerical growth exponents are not treated as unbiased continuum dimensions; finite-size and fixed-k reconstruction effects remain explicit limitations.

The current surviving toy chain is:

```text
local relational interaction
-> propagation
-> persistent record supports
-> overlap relations
-> effective distance
-> local adjacency
-> bottleneck / shortcut structure
-> relative growth-dimensional organization
```

This remains a toy-model methodology result only.

## Relationship to SoCT

Representational Novelty Mining is upstream of SoCT interpretation.

It may propose candidate mathematical questions relevant to the existing observation-foundations program, but those candidates must pass ordinary scientific gates before being connected to a SoCT-specific memory field, collapse mechanism, consciousness term, or spacetime response.

For RM-01, the relevant existing SoCT chain is:

```text
quantum interaction
-> distinguishable record
-> persistent accessible record
-> observation functional / record-production rate
-> candidate SoCT memory source
-> memory dynamics
-> open spacetime bridge
```

RM-01 currently probes only whether the relational structure of persistent records can carry recoverable effective geometry. It does not establish the SoCT-specific memory or gravity steps.

## Next gate — RM-01E

The strongest remaining assumption is that RM-01A-D begin from a substrate graph whose relational structure already exists.

RM-01E should instead generate an evolving **pre-geometric relational network** from local update rules and then ask which compressed description best explains the resulting persistent record relations:

```text
relation-update rules
-> evolving interaction network
-> propagation
-> persistent records
-> record-only reconstruction
-> competing model classes
```

Candidate explanatory classes should include:

```text
1-D / 2-D / 3-D geometric embedding
hyperbolic geometry
tree / ultrametric
community/block model
small-world network
generic higher-dimensional latent model
```

The key question is no longer whether a known geometry can be reconstructed.

It is:

> Does a low-dimensional geometric description become the best compressed explanation of persistent record relations in any nontrivial regime without hard-coding that geometry into the generator?

A negative result is an acceptable and informative outcome.
