import tempfile,unittest
from pathlib import Path
import numpy as np
from scipy import fft
from quijote_history_extract import overdensity,window,tidal_s2,extract

class ExtractTests(unittest.TestCase):
    def test_normalization(self):
        a=np.arange(8.).reshape(2,2,2)+1
        d=overdensity(a,'counts'); self.assertAlmostEqual(float(d.mean()),0,places=6)
        np.testing.assert_array_equal(overdensity(d,'overdensity'),d)
        with self.assertRaises(ValueError):overdensity(d,'counts')
        with self.assertRaises(ValueError):overdensity(a,'overdensity')
    def test_periodic_window(self):
        n=32;w=window(n,1000,40);a=np.zeros((n,)*3);a[0,0,0]=1
        b=fft.irfftn(fft.rfftn(a)*w,s=a.shape,axes=(0,1,2))
        self.assertAlmostEqual(float(b.sum()),1,places=6)
        self.assertAlmostEqual(float(b[1,0,0]),float(b[-1,0,0]),places=6)
        self.assertGreater(b[-1,0,0],0)
    def test_plane_wave_tidal(self):
        n=16; a=np.broadcast_to(np.cos(2*np.pi*np.arange(n)/n)[:,None,None],(n,)*3)
        i=np.unravel_index(np.arange(n**3),(n,)*3)
        np.testing.assert_allclose(tidal_s2(fft.rfftn(a),n,i),2/3*a[i]**2,atol=1e-6)
    def test_extract(self):
        n=32; d=np.broadcast_to(.1*np.cos(2*np.pi*np.arange(n)/n)[:,None,None],(n,)*3).astype('f4')
        with tempfile.TemporaryDirectory() as tmp:
            p=[]
            for i in range(5):
                path=Path(tmp)/f'{i}.npy';np.save(path,d*(i+1));p.append(path)
            a,records=extract(p,'overdensity',n=n,count=128)
            b,_=extract(p,'overdensity',n=n,count=128)
            self.assertEqual(a['delta'].shape,(128,2,5));self.assertEqual(len(records),5)
            np.testing.assert_array_equal(a['indices'],b['indices'])
            np.testing.assert_allclose(a['delta'][:,:,4],5*a['delta'][:,:,0],atol=1e-6)
            self.assertTrue(np.all(a['tidal_s2']>=0))

if __name__=='__main__':unittest.main()
