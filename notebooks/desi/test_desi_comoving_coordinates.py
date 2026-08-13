#!/usr/bin/env python3
"""Regression tests for deterministic DESI comoving coordinate conversion."""

import math
import unittest

from desi_comoving_coordinates import FlatLambdaCDM, comoving_distance_mpc, radec_z_to_cartesian


class TestComovingCoordinates(unittest.TestCase):
    def test_zero_and_monotonic_distance(self):
        cosmo = FlatLambdaCDM()
        self.assertEqual(comoving_distance_mpc(0.0, cosmo), 0.0)
        d1 = comoving_distance_mpc(0.05, cosmo)
        d2 = comoving_distance_mpc(0.10, cosmo)
        d3 = comoving_distance_mpc(0.50, cosmo)
        self.assertGreater(d1, 0.0)
        self.assertLess(d1, d2)
        self.assertLess(d2, d3)

    def test_axis_transform_ra0_dec0(self):
        chi, x, y, zc = radec_z_to_cartesian(0.0, 0.0, 0.1)
        self.assertTrue(math.isclose(x, chi, rel_tol=0.0, abs_tol=1e-9))
        self.assertLess(abs(y), 1e-9)
        self.assertLess(abs(zc), 1e-9)

    def test_axis_transform_ra90_dec0(self):
        chi, x, y, zc = radec_z_to_cartesian(90.0, 0.0, 0.1)
        self.assertLess(abs(x), 1e-9)
        self.assertTrue(math.isclose(y, chi, rel_tol=0.0, abs_tol=1e-9))
        self.assertLess(abs(zc), 1e-9)

    def test_north_pole_transform(self):
        chi, x, y, zc = radec_z_to_cartesian(123.0, 90.0, 0.1)
        self.assertLess(abs(x), 1e-9)
        self.assertLess(abs(y), 1e-9)
        self.assertTrue(math.isclose(zc, chi, rel_tol=0.0, abs_tol=1e-9))

    def test_h0_rescales_distance(self):
        z = 0.2
        d_low_h0 = comoving_distance_mpc(z, FlatLambdaCDM(h0=67.4, omega_m=0.315))
        d_high_h0 = comoving_distance_mpc(z, FlatLambdaCDM(h0=73.0, omega_m=0.315))
        ratio = d_low_h0 / d_high_h0
        self.assertTrue(math.isclose(ratio, 73.0 / 67.4, rel_tol=1e-10))

    def test_invalid_coordinates(self):
        with self.assertRaises(ValueError):
            radec_z_to_cartesian(-1.0, 0.0, 0.1)
        with self.assertRaises(ValueError):
            radec_z_to_cartesian(0.0, 91.0, 0.1)
        with self.assertRaises(ValueError):
            radec_z_to_cartesian(0.0, 0.0, -0.1)


if __name__ == "__main__":
    unittest.main()
