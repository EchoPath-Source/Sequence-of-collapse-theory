# Memory-Field PM Figures

**Evidence label:** depends on the generating code and source data.

This folder is reserved for figures generated from the memory-field particle-mesh simulation line.

## Current status
Figure landing structure is in place. Final production figure files still need to be added or verified.

## Required metadata for every figure
Each figure should be accompanied by either a caption file or source note containing:

1. code version,
2. source CSV / output file,
3. parameter set,
4. seed or sweep range,
5. whether it is validation, exploratory, or production-facing,
6. exact claim-safe caption.

## Recommended filenames

```text
v061_core_ratio_baseline_vs_memory.png
v061_environment_hsplit_timeseries.png
v061_dwarf_survival_by_environment.png
v061_fields_seed42_snapshot.png
```

## Rule
Figures are visual summaries, not independent evidence. Do not cite a figure unless the source data and generating script/notebook are also committed or documented.
