import unittest
import numpy as np
from scipy.spatial import cKDTree
from density_convergence import normalize, effective, summarize, compare

class ConvergenceTests(unittest.TestCase):
    def test_normalization(self):
        d={'Z':np.array([.02,.02,.04]),'PHOTSYS':np.array([b'N',b'N',b'S']),'WEIGHT':np.array([1.,3.,6.])}
        r={'Z':np.array([.02,.02,.04]),'PHOTSYS':np.array([b'N',b'N',b'S']),'WEIGHT':np.array([1.,1.,2.])}
        np.testing.assert_allclose(normalize(d,r),[2,2,6])
        with self.assertRaises(ValueError):normalize(d,{k:v[:2] for k,v in r.items()})
    def test_effective_block_concentration(self):
        self.assertEqual(effective(np.array([1.,1.,1.,1.])),4)
        self.assertEqual(effective(np.array([4.])),1)
        self.assertEqual(effective(np.array([])),0)
    def test_density_and_block_share(self):
        data=(cKDTree([[0,0,0],[1,0,0]]),np.array([1.,3.]))
        random=(cKDTree([[0,0,0],[1,0,0]]),np.array([2.,2.]),np.array([0,0]))
        a=summarize(np.array([[0,0,0],[20,0,0]]),2,data,random)
        np.testing.assert_allclose(a[0],[1,2,1,1]);self.assertTrue(np.isnan(a[1,0]));self.assertEqual(a[1,1],0)
    def test_paired_metrics(self):
        a=np.array([[1.,25,10,.1],[2.,25,10,.1],[4.,25,10,.1]])
        b=a.copy();b[:,0]*=2
        v=compare(a,b,np.ones(3,bool));self.assertEqual(v['pairs'],3);self.assertEqual(v['rho'],1);self.assertAlmostEqual(v['median_symdiff'],2/3,places=4)
        self.assertEqual(compare(a,b,np.zeros(3,bool)),{'pairs':0})

if __name__=='__main__':unittest.main()
