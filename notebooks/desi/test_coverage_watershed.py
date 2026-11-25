import unittest
import numpy as np
from coverage_overlap import nested_pixel, covered
from watershed_overlap import parity
from mesh_audit import mesh_stats

class GeometryAuditTests(unittest.TestCase):
    def test_base_faces(self):
        np.testing.assert_array_equal(nested_pixel([45,135,225,315],[45]*4,1),[0,1,2,3])
        np.testing.assert_array_equal(nested_pixel([0,90,180,270],[0]*4,1),[4,5,6,7])
        np.testing.assert_array_equal(nested_pixel([45,135,225,315],[-45]*4,1),[8,9,10,11])
    def test_invalid(self):
        np.testing.assert_array_equal(nested_pixel([360,-1,1,np.nan],[0,0,91,0]),[-1]*4)
    def test_nesting(self):
        a=np.array([12.,180.,359.,71.,222.]);b=np.array([12.,-89.,89.,-45.,45.]);np.testing.assert_array_equal(nested_pixel(a,b,1024)//4,nested_pixel(a,b,512))
    def test_coverage(self):
        m=np.zeros(12*1024**2,bool);m[nested_pixel(180,0)]=True
        np.testing.assert_array_equal(covered(m,[180,0,360],[0,0,0]),[True,False,False])
    def test_parity(self):
        v=np.array([[0.,0.,0.],[1.,0.,0.],[0.,1.,0.],[0.,0.,1.]])
        t=v[[[0,2,1],[0,1,3],[0,3,2],[1,2,3]]]
        self.assertIs(parity(np.array([.1,.1,.1]),t),True)
        self.assertIs(parity(np.array([.8,.8,.8]),t),False)
        self.assertIsNone(parity(np.array([0.,.2,.2]),t))
        self.assertIs(parity(np.array([.1,.1,.1]),t[:,::-1]),True)
    def test_mesh_closure(self):
        v=np.array([[0.,0.,0.],[1.,0.,0.],[0.,1.,0.],[0.,0.,1.]])
        t=v[[[0,2,1],[0,1,3],[0,3,2],[1,2,3]]];a=np.zeros(4,dtype=[(f'P{i}_{k}','f8') for i in (1,2,3) for k in 'XYZ'])
        for i in range(3):
            for j,k in enumerate('XYZ'):a[f'P{i+1}_{k}']=t[:,i,j]
        self.assertEqual(mesh_stats(a)[:2],(True,True));self.assertFalse(mesh_stats(a[:-1])[0])

if __name__=='__main__':unittest.main()
