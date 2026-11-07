"""SIM-04N invariants and held-out evaluation smoke tests.

Run: python -m unittest discover -s experiments/observation-foundations -p 'test_sim04n*.py'
"""
import importlib.util
from pathlib import Path
import unittest

import numpy as np

SPEC = importlib.util.spec_from_file_location(
    "sim04n", Path(__file__).with_name("sim04n_shared_spectrum_bath.py")
)
sim = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(sim)


class SharedBathTests(unittest.TestCase):
    def test_shared_spectrum_positive(self):
        w, c = sim.bath_spectrum(16)
        self.assertTrue(np.all(np.diff(w) > 0))
        self.assertTrue(np.all(c > 0))

    def test_energy_closure_and_holdout(self):
        result = sim.evaluate(n=16, dt=0.008)
        self.assertTrue(np.isfinite(result["heldout_rmse"]))
        self.assertTrue(np.isfinite(result["training_rmse"]))
        self.assertEqual(result["training_modes"], [0, 1])
        self.assertEqual(result["heldout_modes"], [2, 3])
        self.assertLess(result["energy_closure_max_error"], 2e-4)

    def test_timestep_refinement(self):
        coarse = sim.integrate(n=8, dt=0.008)
        fine = sim.integrate(n=8, dt=0.004)
        ec = np.max(np.abs(coarse["total"] - coarse["total"][0] - coarse["work"]))
        ef = np.max(np.abs(fine["total"] - fine["total"][0] - fine["work"]))
        self.assertLess(ef, ec + 1e-9)


if __name__ == "__main__":
    unittest.main()
