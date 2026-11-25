"""P6 geometry-only CF4 feasibility. Do not load measured distances or H0."""
import argparse
from collections import Counter
from pathlib import Path
import numpy as np
import pandas as pd
from desivast_catalog_loader import load_catalog, VoidGeometry, radec_to_xyz

C = 299792.458
WINDOWS = ((.01,.15),(.023,.15),(.01,.05),(.05,.15))


def read_cf4(path, grouped):
    cols = ['1PGC','RAJ2000','DEJ2000','Vcmb'] + (['Ngal','Vh'] if grouped else ['PGC'])
    d = pd.read_csv(path, sep='\t', comment='#', skip_blank_lines=True, usecols=cols, dtype=str)
    # VizieR TSV has units and ruler rows after the header.
    if d.iloc[0].Vcmb.strip() != 'km/s' or set(d.iloc[1].Vcmb.strip()) != {'-'}:
        raise ValueError('Unexpected VizieR header layout')
    d = d.iloc[2:].apply(pd.to_numeric, errors='coerce').reset_index(drop=True)
    key = '1PGC' if grouped else 'PGC'
    if d[key].isna().any() or not d[key].is_unique or (d[key] <= 0).any():
        raise ValueError('Missing or duplicate object IDs')
    return d


def classify(d, geom, velocity, offset=0):
    p=radec_to_xyz(d.RAJ2000,d.DEJ2000,(d[velocity]+offset)/C)
    result=[geom.classify(x) for x in p]
    labels=np.array([a for a,b in result]); hits=[b for a,b in result]
    return labels,hits


def summarize(d,labels,hits,mask,grouped):
    keep=mask & (labels=='interior_candidate')
    return dict(rows=int(mask.sum()), labels=dict(sorted(Counter(labels[mask]).items())),
                interior_groups=int(d.loc[keep,'1PGC'].nunique()),
                interior_voids=len({hits[i][0][:2] for i in np.flatnonzero(keep)}),
                singleton_rows=int((d.loc[keep,'Ngal']==1).sum()) if grouped else None)


def audit(root):
    geom=VoidGeometry([(cap,*load_catalog(root/f'DESIVAST_BGS_VOLLIM_VoidFinder_{cap}.fits')) for cap in ('NGC','SGC')])
    data={k:read_cf4(root/'cosmicflows4'/f'cf4_{k}.tsv',k=='groups') for k in ('groups','galaxies')}
    for k,d in data.items():
        print(k,'rows',len(d),'parent IDs',d['1PGC'].nunique(),'missing parent',int(d['1PGC'].isna().sum()),'max CMB z',d.Vcmb.max()/C)
        z=d.Vcmb/C
        labels,hits=classify(d,geom,'Vcmb')
        for lo,hi in WINDOWS:
            mask=z.between(lo,hi).to_numpy();print(k,'CMB',lo,hi,summarize(d,labels,hits,mask,k=='groups'))
        mask=z.between(.01,.15).to_numpy()
        # A radial-position sensitivity, not a correction or a probabilistic error model.
        stable=labels=='interior_candidate'
        for dv in (-300,300):
            l,h=classify(d,geom,'Vcmb',dv)
            same=np.array([a==b for a,b in zip(hits,h)])
            stable &= (l=='interior_candidate') & same
            print(k,'CMB offset',dv,summarize(d,l,h,mask,k=='groups'))
        print(k,'same void at nominal and both offsets',summarize(d,np.where(stable,'interior_candidate','other'),hits,mask,k=='groups'))
        if k=='groups':
            l,h=classify(d,geom,'Vh');print(k,'heliocentric sensitivity, fixed CMB window',summarize(d,l,h,mask,True))
            print('same interior void CMB and heliocentric',int((mask&(labels=='interior_candidate')&(l=='interior_candidate')&np.array([a==b for a,b in zip(hits,h)])).sum()))
    groups,gal=data['groups'],data['galaxies']
    print('galaxy parent IDs absent from group table',len(set(gal['1PGC'].dropna())-set(groups['1PGC'])))
    print('GEOMETRY_ONLY: no measured distance, velocity residual, footprint, filament classification or H0 fit')

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('root',type=Path);audit(p.parse_args().root)
