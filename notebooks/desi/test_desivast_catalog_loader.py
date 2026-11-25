import unittest
import numpy as np
from scipy.integrate import quad
from desivast_catalog_loader import VoidGeometry, radec_to_xyz

class GeometryTests(unittest.TestCase):
    def setUp(self):
        dt=[(k,'f8') for k in ('X','Y','Z','RADIUS')]+[('VOID','i8'),('EDGE','i8')]
        m=np.array([(0,0,0,1,7,0),(5,0,0,1,8,2)],dtype=dt)
        s=np.array([(0,0,0,1,7,0),(1.5,0,0,1,7,0),(5,0,0,1,8,2)],dtype=dt)
        self.g=VoidGeometry([('N',m,s)])
        self.overlap=VoidGeometry([('N',m,s),('S',m,s)])
    def test_union(self):
        self.assertEqual(self.g.classify([2,0,0])[0],'interior_candidate')
    def test_edge(self):
        self.assertEqual(self.g.classify([5,0,0])[0],'edge_candidate')
    def test_unmatched(self):
        self.assertEqual(self.g.classify([10,0,0])[0],'unmatched_unclassified')
    def test_boundary(self):
        self.assertEqual(self.g.classify([-1,0,0])[0],'interior_candidate')
    def test_overlap(self):
        self.assertEqual(self.overlap.classify([0,0,0])[0],'ambiguous_overlap')
    def test_invalid(self):
        self.assertEqual(self.g.classify([np.nan,0,0])[0],'invalid_or_outside_z')
        self.assertTrue(np.isnan(radec_to_xyz(0,91,.1)).all())
    def test_distance(self):
        r=2997.92458*quad(lambda z:1/np.sqrt(.315*(1+z)**3+.685),0,.1)[0]
        np.testing.assert_allclose(radec_to_xyz(90,0,.1),[0,r,0],atol=1e-6)

if __name__=='__main__': unittest.main()
