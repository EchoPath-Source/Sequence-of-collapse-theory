import unittest
import numpy as np
from scipy.spatial import cKDTree
from lss_density_support import normalize, shell, counts, fractions, offsets
from coverage_overlap import NPIX

class DensitySupportTests(unittest.TestCase):
    def test_shell_edges(self):
        np.testing.assert_array_equal(shell(np.array([.01,.029,.031,.24])),[0,0,1,11])
    def test_shell_normalization(self):
        d={'Z':np.array([.02,.02,.04]),'PHOTSYS':np.array([b'N',b'N',b'S']),'WEIGHT':np.array([1.,3.,6.])}
        r={'Z':np.array([.02,.02,.04]),'PHOTSYS':np.array([b'N',b'N',b'S']),'WEIGHT':np.array([1.,1.,2.])}
        np.testing.assert_allclose(normalize(d,r),[2,2,6])
        with self.assertRaises(ValueError):normalize(d,{k:v[:2] for k,v in r.items()})
    def test_counts(self):
        dt=cKDTree([[0,0,0],[1,0,0],[9,0,0]]);rt=cKDTree([[0,0,0],[1,0,0]])
        out=counts(np.array([[0,0,0],[20,0,0]]),2,dt,np.array([1.,3.,9.]),rt,np.array([2.,2.]),np.array([0,1]))
        np.testing.assert_allclose(out[0],[2,2,2,1,1,1]);self.assertEqual(out[1,2],0);self.assertTrue(np.isnan(out[1,3:]).all())
    def test_coverage(self):
        m=np.ones(NPIX,bool);p=np.array([[200.,0,0]])
        self.assertEqual(fractions(p,10,m)[0],1);self.assertEqual(fractions(p,10,~m)[0],0)
        self.assertTrue(np.all(np.linalg.norm(offsets(10),axis=1)<=1))

if __name__=='__main__':unittest.main()
