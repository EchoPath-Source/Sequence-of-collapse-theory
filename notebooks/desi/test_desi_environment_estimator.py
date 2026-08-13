#!/usr/bin/env python3
"""Synthetic regression tests for desi_environment_estimator.py."""

import math
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from desi_environment_estimator import (  # noqa: E402
    EnvironmentConfig,
    Point,
    assign_shells,
    classify_percentile,
    estimate_environment,
    percentile_ranks,
    self_test,
)


class TestDESIEnvironmentEstimator(unittest.TestCase):
    def test_percentile_midrank(self):
        got = percentile_ranks([1.0, 2.0, 2.0, 4.0])
        self.assertAlmostEqual(got[0], 0.0)
        self.assertAlmostEqual(got[1], 50.0)
        self.assertAlmostEqual(got[2], 50.0)
        self.assertAlmostEqual(got[3], 100.0)

    def test_candidate_bin_boundaries(self):
        cfg = EnvironmentConfig()
        self.assertEqual(classify_percentile(10.0, cfg), "void_like")
        self.assertEqual(classify_percentile(30.0, cfg), "low_density")
        self.assertEqual(classify_percentile(70.0, cfg), "sheet_like")
        self.assertEqual(classify_percentile(90.0, cfg), "filament_like")
        self.assertEqual(classify_percentile(90.1, cfg), "cluster_like")

    def test_shell_assignment(self):
        pts = [Point("a", 0.019, 0, 0, 0), Point("b", 0.021, 1, 0, 0)]
        assign_shells(pts, EnvironmentConfig(shell_width=0.02))
        self.assertEqual(pts[0].redshift_shell, "0.000-0.020")
        self.assertEqual(pts[1].redshift_shell, "0.020-0.040")

    def test_small_shell_flag_and_undefined_density(self):
        pts = [Point(str(i), 0.1, float(i), 0.0, 0.0) for i in range(4)]
        cfg = EnvironmentConfig(shell_width=0.02, min_shell_size=10, k_neighbors=5)
        estimate_environment(pts, cfg)
        for p in pts:
            self.assertIn("SMALL_SHELL", p.quality_flags)
            self.assertIn("DENSITY_UNDEFINED", p.quality_flags)
            self.assertFalse(math.isfinite(p.local_density))
            self.assertEqual(p.environment_bin, "unclassified")

    def test_synthetic_dense_vs_sparse(self):
        result = self_test()
        self.assertEqual(result["status"], "PASS")
        self.assertGreater(result["dense_median_density"], result["sparse_median_density"])


if __name__ == "__main__":
    unittest.main()
