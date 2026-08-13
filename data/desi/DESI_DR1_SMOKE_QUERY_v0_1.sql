-- DESI DR1 tiny smoke query v0.1
-- Purpose: validate column access, quality cuts, coordinates, redshift,
-- HEALPix, and row retrieval before any environment analysis.
--
-- Status: READY / NOT YET RUN
-- Source release: DESI DR1
-- Source table: desi_dr1.zpix
-- Query version: desi-dr1-smoke-v0.1
-- Planned retrieval mode: NSF NOIRLab Astro Data Lab Query Client / SQL
--
-- This query is deliberately tiny and is not an environment estimator,
-- Pantheon+ crossmatch, H0 test, or evidence for SoCT/PNT.

SELECT
  targetid,
  mean_fiber_ra,
  mean_fiber_dec,
  z,
  zwarn,
  zcat_primary,
  objtype,
  survey,
  program,
  spectype,
  healpix
FROM desi_dr1.zpix
WHERE zcat_primary = true
  AND objtype = 'TGT'
  AND zwarn = 0
  AND spectype = 'GALAXY'
  AND survey = 'main'
  AND program <> 'other'
  AND z BETWEEN 0.01 AND 0.5
  AND mean_fiber_ra BETWEEN 55.5 AND 56.5
  AND mean_fiber_dec BETWEEN -9.5 AND -8.5
LIMIT 25;
