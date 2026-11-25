"""Compare 1% and 5% random support; raw weights, not full density rerun."""
import argparse
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.spatial import cKDTree
from coverage_overlap import tables, load_mask, covered, positions, C
from lss_density_support import fractions

def effective(w):
    s=w.sum()
    return s*s/(w@w) if s else 0.

def randoms(root,mask,pct):
    pp=[];ww=[];bb=[]
    for i,cap in enumerate(('NGC','SGC')):
        path=root/f'BGS_ANY_{cap}_0_clustering_ran_{pct}pct.fits.bin'
        h,t=list(tables(path))[1]
        if pct==5:
            if (h.get('SAMPSEED'),h.get('SAMPBLCK'),h.get('SAMPFRAC'))!=('20261125','1000','0.05') or len(t)%1000 or len(np.unique(t['TARGETID']))!=len(t):raise ValueError('unexpected 5% sample')
            a,b=np.deg2rad(t['RA']),np.deg2rad(t['DEC'])
            u=np.column_stack([np.cos(a)*np.cos(b),np.sin(a)*np.cos(b),np.sin(b)]).reshape(-1,1000,3)
            cen=u.mean(axis=1);cen/=np.linalg.norm(cen,axis=1)[:,None]
            ang=np.rad2deg(np.arccos(np.clip(np.einsum('ijk,ik->ij',u,cen),-1,1))).max(axis=1)
            print(cap,'block max deviation p50/p90/max deg',np.quantile(ang,[.5,.9,1]))
        elif (h.get('SAMPSTRD'),h.get('SAMPOFF'))!=('100','0'):raise ValueError('unexpected 1% sample')
        w=t['WEIGHT']; z=t['Z'];ra=t['RA'];dec=t['DEC']
        if not np.all(np.isfinite(w)&(w>0)&np.isfinite(z)&(z>0)&np.isfinite(ra)&(ra>=0)&(ra<360)&np.isfinite(dec)&(abs(dec)<=90)):raise ValueError('invalid randoms')
        sel=(z>=.01)&(z<=.24)
        j=np.flatnonzero(sel);j=j[covered(mask,ra[j],dec[j])]
        print(cap,pct,'total/radial/masked',len(t),sel.sum(),len(j))
        pp.append(positions(ra[j],dec[j],z[j]));ww.append(w[j]);bb.append(j//1000+i*100000)
    return cKDTree(np.concatenate(pp)),np.concatenate(ww),np.concatenate(bb)

def audit(root,random_dir,mask_paths):
    mask=load_mask(mask_paths)
    d=pd.read_csv(root/'cosmicflows4/cf4_groups.tsv',sep='\t',comment='#',usecols=['1PGC','RAJ2000','DEJ2000','Vcmb'],dtype=str).iloc[2:].apply(pd.to_numeric,errors='coerce')
    z=d.Vcmb/C;keep=z.between(.01,.15)&covered(mask,d.RAJ2000,d.DEJ2000)
    p=positions(d.RAJ2000[keep],d.DEJ2000[keep],z[keep])
    samples={pct:randoms(random_dir,mask,pct) for pct in (1,5)}
    for radius in (10,20,30):
        g=(fractions(p,radius,mask,10)>=.8)&(fractions(p,radius,mask,11)>=.8)
        print('radius',radius,'geometric gate',g.sum())
        for pct,(tree,w,b) in samples.items():
            stats=[]
            for j in range(0,len(p),128):
                for idx in tree.query_ball_point(p[j:j+128],radius):
                    ii=np.asarray(idx,int);ww=w[ii];_,inv=np.unique(b[ii],return_inverse=True);bw=np.bincount(inv,weights=ww)
                    stats.append((len(ii),effective(ww),len(bw),effective(bw)))
            raw,eff,blocks,be=np.asarray(stats).T;ok=g&(eff>=25)
            print(pct,'median raw',np.median(raw),'point gate 25/50',ok.sum(),(g&(eff>=50)).sum())
            if pct==5 and ok.any():
                print('median blocks',np.median(blocks[ok]),'effective block p10/p50/p90',np.quantile(be[ok],[.1,.5,.9]),'block eff >=10/25',np.sum(ok&(be>=10)),np.sum(ok&(be>=25)))
    print('SUPPORT_ONLY; block concentration is descriptive, not independent effective N or full density estimate')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('root',type=Path);p.add_argument('random_dir',type=Path);p.add_argument('mask_parts',type=Path,nargs=3);a=p.parse_args();audit(a.root,a.random_dir,a.mask_parts)
