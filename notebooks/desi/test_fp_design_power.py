import unittest
import numpy as np
from fp_design_power import design, contrast_se, bound

class DesignTests(unittest.TestCase):
    def test_interquartile_scaling(self):
        x=np.exp(np.arange(8.)/8);z=np.linspace(.02,.08,8);ra=np.full(8,180.)
        X,span=design(x,z,ra)
        self.assertAlmostEqual(np.diff(np.quantile(X[:,1],[.25,.75]))[0],1)
        self.assertGreater(span,0)
        with self.assertRaises(ValueError):design(np.ones(8),z,ra)
    def test_diagonal_information(self):
        X=np.column_stack([np.ones(4),[-1.,-1.,1.,1.]])
        self.assertAlmostEqual(contrast_se(X,np.eye(4)),.5)
        with self.assertRaises(ValueError):contrast_se(np.ones((4,2)),np.eye(4))
    def test_correlated_information(self):
        X=np.column_stack([np.ones(4),[-1.,-1.,1.,1.]])
        cov=np.array([[1,.5,0,0],[.5,1,0,0],[0,0,1,.5],[0,0,.5,1]])
        self.assertAlmostEqual(contrast_se(X,cov),np.sqrt(.375))
    def test_bound(self):
        z=np.array([.03,.05,.04,.08,.09,.06,.07,.11]);rho=np.exp(np.array([0,1,2,0,2,1,3,2.]));ra=np.full(8,180.);p=np.column_stack([z*3000,np.zeros(8),np.zeros(8)]);v=bound(rho,z,ra,p,np.full(8,.5),20)
        self.assertEqual(v['n'],8);self.assertEqual(len(v['mde']),4);self.assertTrue(all(x>0 for x in v['mde']))

if __name__=='__main__':unittest.main()
