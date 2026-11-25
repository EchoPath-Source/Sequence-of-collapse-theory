# P6 BGS_ANY coverage-controlled density support audit

2026-11-25 UTC. PR34 merged at 84ff7da9d0df4bb47e6f16b1d52d8b434a51d38a. Executed exploratory density proxy on real staged catalogs. No measured distance moduli, peculiar-velocity residuals, or H0 outcomes read. No ranks or filament labels exported. Original strict P6 contrast remains unchanged. Separate method family from DESI_DR1_COORDINATE_NEIGHBORHOOD_CONTRACT.md (zpix kNN); does not replace it.

## Method and reproducibility

Extract P6_Core.zip, P6_CosmicFlows.zip and the three BGS_ANY data ZIPs to STAGED; retain both random files and three mask parts in RAW. From repository root:

    python -m unittest discover -s notebooks/desi -p test_lss_density_support.py -v
    OPENBLAS_NUM_THREADS=1 python notebooks/desi/lss_density_support.py STAGED RAW MASK1 MASK2 MASK3

The random filenames in RAW have the staged .fits.bin suffix. Four new synthetic tests passed locally and the diagnostic ran to completion. Local copy of prior mask helper used same lookup/table/position algorithms; independent FITS/HEALPix library verification remains outstanding.

Use BGS_ANY data and index-0 randoms of the same stated LSS DR1 iron v1.5 tracer. Apply identical redshift cuts [.01,.24], require positive finite WEIGHT and valid coordinates, no FKP weight. No duplicate TARGETID across selected data files. Normalize random weights by alpha=sum(data WEIGHT)/sum(random WEIGHT) separately by cap, PHOTSYS and redshift shells width .02 starting .01 (last shell ends .24), before restricting both to reconstructed DONE mask. Relative density D/sum(alpha_i*w_r), not matter density; the comparison is to the selected survey-wide mean within strata, and tracer bias, redshift-space distortion and cosmic variance remain. Zero random support => undefined, not void. Use comoving h^-1 Mpc geometry with Om=.315 from PR34. SN selection on zHD .01–.15; matching zCMB; CF4 Vcmb/c .01–.15. Point mask coverage first. Galaxy and group samples overlap, no pooling.

Use 10/20/30 h^-1 Mpc spherical apertures, not kNN. For each center estimate geometric volume fraction inside reconstructed angular mask and [.01,.24] radial limits using 1024 and 2048 nested scrambled Sobol sphere points (seed 20261125). Require both estimates above .70/.80/.90 in sensitivity grid, plus weighted effective random count N_eff=(sum w)^2/sum(w^2)>=25; >=50 reported separately. This geometric fraction is not an independently established LSS selection-completeness fraction. No final thresholds selected. Weight normalization, redshift frame, mask equivalence, unblinded catalog provenance, and potential target self-count contamination (e.g. CF4 group member also BGS tracer) need review before production. A self-count exclusion needs independent object matching, not arbitrary removal of nearest galaxies. Sobol agreement is numerical convergence only. Interleaved even/odd sampled-row halves with doubled normalized weights are a stress diagnostic, not independent random realizations or a formal uncertainty estimate.

Sources: DESI LSS data model https://desidatamodel.readthedocs.io/en/stable/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSION/data_clustering.html ; catalog construction https://arxiv.org/abs/2405.16593 ; intake manifests P6_REMAINING_BUNDLES_INTAKE.md and P6_COVERAGE_PRODUCTS_INTAKE.md.

## Real data support

| Cap | Data in z range | Randoms in z range | Data inside mask | Randoms inside mask | Alpha min/median/max |
|---|---:|---:|---:|---:|---|
| NGC | 2214456 | 71661 | 1012443 | 26771 | 26.770/28.336/32.013 |
| SGC | 779358 | 29582 | 144080 | 4056 | 24.686/28.135/30.696 |

Different retained data/random fractions require selection and radial/angular distribution checks. Not evidence of physical overdensity by themselves.

| Dataset | Covered centers | Radius | Median raw random count | N_eff>=25 before aperture coverage | N_eff>=50 before aperture coverage | Both f>=.80 and N_eff>=25 | Same with N_eff>=50 |
|---|---:|---:|---:|---:|---:|---:|---:|
| SN | 82 | 10 | 3 | 0 | 0 | 0 | 0 |
| SN | 82 | 20 | 22 | 7 | 0 | 0 | 0 |
| SN | 82 | 30 | 54 | 49 | 24 | 7 | 1 |
| CF4 groups | 5008 | 10 | 4 | 0 | 0 | 0 | 0 |
| CF4 groups | 5008 | 20 | 24 | 514 | 0 | 200 | 0 |
| CF4 groups | 5008 | 30 | 72 | 4305 | 1838 | 821 | 442 |
| CF4 galaxies | 7054 | 10 | 4 | 0 | 0 | 0 | 0 |
| CF4 galaxies | 7054 | 20 | 25 | 788 | 0 | 313 | 0 |
| CF4 galaxies | 7054 | 30 | 73 | 6090 | 2741 | 1209 | 626 |

All retained counts equal distinct literal object IDs for each sample separately, not independent statistical observations. Across all centers/radii maximum difference between 1024/2048 estimated volume fractions .0161133. No claim of exact volume or selection completeness.

| Dataset and radius | Retained at f>=.70 / .80 / .90, N_eff>=25 | Split Spearman at .80 | Median abs half difference / full ratio at .80 |
|---|---|---:|---:|
| SN 20 | 1 / 0 / 0 | undefined | undefined |
| SN 30 | 7 / 7 / 6 | .643 | .311 |
| Groups 20 | 272 / 200 / 109 | .720 | .262 |
| Groups 30 | 1372 / 821 / 253 | .782 | .195 |
| Galaxies 20 | 409 / 313 / 150 | .707 | .272 |
| Galaxies 30 | 1993 / 1209 / 424 | .797 | .204 |

10 h^-1 Mpc: zero retained all datasets and thresholds. At .80, retained CF4 group density proxy is promising for exploratory work at 30 h^-1 Mpc, but half-sample discrepancies ~20% and rank correlation <.8 make final rank assignments premature. These are not void/filament membership; even 821 groups may have much smaller effective independent sample size due to overlapping apertures and correlated velocities. Larger aperture changes the physical environment scale.

## Minimum next acquisition and gates

The current 1% randoms are too sparse for the tested 10 h^-1 Mpc scale and limited for 20. Request a bounded 5% independent/seeded representative BGS_ANY random projection for each cap (or an equivalent compact selection integration product). Keep original sample for comparison, retain TARGETID or source-row index, source file index/version, seed, sampling fraction, RA DEC Z PHOTSYS WEIGHT and completeness fields. Approximately 83 MB combined at existing projected row width, before added IDs; not a full random download. This is a proposed first increment, not a guaranteed sufficient density. 10 Mpc/h could require larger or differently targeted support; do not tune aperture or acquire full randoms just to achieve desired sample count. Verify angular/radial/weight distributions with source metadata, compare across independent realizations, and quantify precision at each fixed aperture. A compact exact or sufficiently dense selection integrator may be preferable. Resolve reconstructed mask versus catalog area and full LSS footprint separately. Obtain exact source/recipe provenance, test true filament assignment separately, and audit CF4 indicator uncertainties and overlap/selection/correlated errors before power calculations. No final labels, H0 estimates or scientific support/falsification claim.
