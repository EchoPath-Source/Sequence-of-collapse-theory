# SPARC Figure Provenance Notes

**Status:** Figure documentation / image artifacts not yet committed  
**Related result summary:** `papers/cosmology/sparc/sparc-age-dm-publication-summary-v1.md`  
**Related notebook plan:** `notebooks/sparc_age_dm_analysis_plan.md`

---

## Purpose

This file tracks the SPARC plots shared during the analysis thread so they can later be regenerated from committed code and data.

The images should be treated as provisional visual outputs until the derived CSV and notebook are committed.

---

## Figure 1 — Full Sample Age-DM Correlation

Description:

```text
SPARC Age-DM Correlation (n=175)
```

Visual contents:

- x-axis: Mean Stellar Age (Gyr);
- y-axis: Outer Dark Matter Fraction;
- colorbar: log10(Vmax) [km/s];
- red best-fit line;
- annotation box:

```text
r = +0.201
p = 7.67e-03
sigma = 2.67
```

Intended future path:

```text
figures/sparc/age_dm_full_sample.png
```

Required regeneration source:

```text
notebooks/sparc_age_dm_analysis.ipynb
```

---

## Figure 2 — Mass-Binned Age-DM Correlations

Description:

```text
Low Mass (n=59), Mid Mass (n=58), High Mass (n=58)
```

Visual contents:

- three panels by mass tercile;
- x-axis: Age (Gyr);
- y-axis: f_DM;
- red best-fit lines;
- pink scatter points;
- annotation boxes:

```text
Low Mass:  r = +0.115, p = 0.384
Mid Mass:  r = +0.456, p = 0.000
High Mass: r = +0.277, p = 0.036
```

Intended future path:

```text
figures/sparc/age_dm_mass_bins.png
```

---

## Reproducibility Requirements

Before these figures are used in a manuscript:

1. commit `data/sparc/sparc_age_fdm_data.csv` or equivalent;
2. commit `notebooks/sparc_age_dm_analysis.ipynb`;
3. regenerate both figures from the committed notebook;
4. record the exact random seed;
5. record any filtering applied;
6. record mass-bin thresholds;
7. verify that annotations match computed values;
8. include figure-generation date and data checksum.

---

## Manuscript Use

Recommended captions:

### Figure 1 Caption Draft

> Outer inferred dark matter fraction versus mean stellar age for the SPARC sample. Points are colored by log10(Vmax). The red line shows the linear best fit. The reported positive correlation is in the direction predicted by the SoCT memory-field model, but remains provisional pending release of derived data and analysis code.

### Figure 2 Caption Draft

> Age-DM correlation split by Vmax terciles. The strongest reported signal appears in the mid-mass bin, while the low-mass bin is non-significant and the high-mass bin is weakly significant. This bin structure should be tested for sensitivity to bin thresholds and outliers.

---

## Research Boundary

Do not treat static image files as reproducible evidence. They are visual summaries only.

The evidentiary artifact is the data + code that regenerates them.
