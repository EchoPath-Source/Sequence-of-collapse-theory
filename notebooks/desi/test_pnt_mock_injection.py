import unittest
import numpy as np
from pnt_mock_injection import make_mock,residual_template

class MockTests(unittest.TestCase):
    def test_geometry_and_covariance(self):
        d,p,X,C,m,b,s=make_mock(100,7)
        self.assertEqual(len(d),100);self.assertTrue(np.all((d>=-.9)&(d<=.5)))
        self.assertTrue(np.all((p>=-.9)&(p<=.5)))
        np.linalg.cholesky(C)
    def test_projection(self):
        x=np.arange(6.);X=np.column_stack([np.ones(6),x]);g=x*x
        h,I=residual_template(X,g,np.eye(6))
        np.testing.assert_allclose(X.T@h,0,atol=1e-10)
        self.assertAlmostEqual(h@g/I,1)
    def test_degeneracy(self):
        X=np.column_stack([np.ones(6),np.arange(6.)])
        with self.assertRaises(ValueError):residual_template(X,X[:,1],np.eye(6))
    def test_nuisance_removes_information(self):
        x=np.linspace(-1,1,20);g=x+.1*x*x+.001*x**3;L=np.eye(20)
        i=[residual_template(np.column_stack([x**k for k in range(j)]),g,L)[1] for j in (1,2,3)]
        self.assertTrue(i[0]>i[1]>i[2]>0)

if __name__=='__main__':unittest.main()
