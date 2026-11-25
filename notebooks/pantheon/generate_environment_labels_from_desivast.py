"""Outcome-blind DESIVAST overlap smoke diagnostic. No distance moduli read."""
import argparse
from pathlib import Path
from collections import Counter
import sys
import numpy as np
import pandas as pd

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'desi'))
from desivast_catalog_loader import load_catalog, VoidGeometry, radec_to_xyz


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--catalog-dir',type=Path,required=True)
    p.add_argument('--pantheon',type=Path,required=True)
    a=p.parse_args()
    catalogs=[]
    for cap in ('NGC','SGC'):
        m,s=load_catalog(a.catalog_dir/f'DESIVAST_BGS_VOLLIM_VoidFinder_{cap}.fits')
        print(cap,len(m),len(s),dict(sorted(Counter(m['EDGE']).items())))
        catalogs.append((cap,m,s))
    g=VoidGeometry(catalogs)
    d=pd.read_csv(a.pantheon,sep=r'\s+',usecols=['CID','RA','DEC','HOST_RA','HOST_DEC','zHEL','zCMB','zHD'])
    cut=d.zHD.between(.01,.15)
    invalid=(~np.isfinite(d.HOST_RA)|~np.isfinite(d.HOST_DEC)|(d.HOST_RA<0)|(d.HOST_RA>=360)|(d.HOST_DEC.abs()>90))
    print('rows',len(d),'cut',int(cut.sum()),'invalid host coordinates',int(invalid.sum()))
    for z in ('zHEL','zCMB','zHD'):
        labels=[g.classify(x)[0] for x in radec_to_xyz(d.RA,d.DEC,d[z])]
        print(z,'full',dict(Counter(labels)),'cut',dict(Counter(np.array(labels)[cut])))
        print('distinct literal CID strings in cut by label',d.assign(label=labels)[cut].groupby('label').CID.nunique().to_dict())
    print('GEOMETRY_ONLY: no coverage mask, no filament labels, no H0 fit')

if __name__=='__main__': main()
