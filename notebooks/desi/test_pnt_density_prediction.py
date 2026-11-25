import math
import unittest
from pnt_density_prediction import *


class ToyTests(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(exhaust_ratio(0), 1)
        self.assertAlmostEqual(toy_h(0), H_REF)
        self.assertAlmostEqual(toy_mu(0), 0)

    def test_original_fiducial(self):
        self.assertAlmostEqual(toy_h(-.35), 69.31179362943229)
        self.assertAlmostEqual(toy_mu(-.35), -.0607358, places=6)

    def test_domain_and_monotonicity(self):
        for d in (-1, .6, float('nan')):
            with self.assertRaises(ValueError): toy_h(d)
        grid = [-.9 + 1.4 * i / 14 for i in range(14)] + [.5]
        values = [toy_h(d) for d in grid]
        self.assertTrue(all(a > b for a, b in zip(values, values[1:])))
        self.assertTrue(all(0 <= exhaust_ratio(d) * (1-SUCCESS) <= 1 for d in grid))

    def test_derivative(self):
        eps = 1e-5
        self.assertAlmostEqual((toy_h(eps)-toy_h(-eps))/(2*eps), toy_slope_at_mean(), places=7)

    def test_contrast(self):
        h, mu = toy_contrast(-.2,.2)
        self.assertAlmostEqual(h, 2.442760, places=5)
        self.assertAlmostEqual(mu, 5*math.log10(toy_h(-.2)/toy_h(.2)))
        self.assertGreater(gr_local_divergence(-.2),0)
        with self.assertRaises(ValueError): toy_contrast(.2,-.2)


if __name__ == '__main__': unittest.main()
