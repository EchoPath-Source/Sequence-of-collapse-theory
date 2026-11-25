import tempfile
import unittest
from pathlib import Path
import numpy as np
import pandas as pd
from cosmicflows_overlap import read_cf4, summarize, classify, C

class CF4Tests(unittest.TestCase):
    def test_read_only_geometry(self):
        text='1PGC\tRAJ2000\tDEJ2000\tVcmb\tNgal\tVh\tDMav\n \tdeg\tdeg\tkm/s\t \tkm/s\tmag\n---\t---\t---\t---\t---\t---\t---\n1\t10\t0\t4000\t1\t4100\tFORBIDDEN\n'
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'groups.tsv';p.write_text(text)
            d=read_cf4(p,True)
            self.assertEqual(len(d),1); self.assertNotIn('DMav',d)
            p.write_text(text+text.splitlines()[-1]+'\n')
            with self.assertRaises(ValueError):read_cf4(p,True)
    def test_group_and_void_counts(self):
        d=pd.DataFrame({'1PGC':[1,1,2]})
        labels=np.array(['interior_candidate']*3)
        hits=[(('N',7,0),),(('N',7,0),),(('S',7,0),)]
        out=summarize(d,labels,hits,np.ones(3,bool),False)
        self.assertEqual(out['interior_groups'],2);self.assertEqual(out['interior_voids'],2)
    def test_velocity_offset(self):
        class Geometry:
            def classify(self,p): return ('finite' if np.isfinite(p).all() else 'invalid',())
        d=pd.DataFrame({'RAJ2000':[0.,0.],'DEJ2000':[0.,0.],'Vcmb':[100.,C*.1]})
        labels,_=classify(d,Geometry(),'Vcmb',-300)
        self.assertEqual(labels.tolist(),['invalid','finite'])

if __name__=='__main__':unittest.main()
