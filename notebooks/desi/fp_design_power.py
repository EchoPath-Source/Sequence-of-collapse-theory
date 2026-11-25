"""Outcome-blind FP density design sensitivity; no distance outcomes or physical fit."""
import argparse
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.linalg import cho_factor, cho_solve
from scipy.spatial.distance import cdist
from density_convergence import build, aperture_gate, summarize
from coverage_overlap import load_mask, covered, positions, C

SCENARIOS=((0.,0.,0.),(300.,0.,0.),(150.,300.,20.),(150.,300.,50.))

def design(rho,z,ra):
    if not np.all(np.isfinite(rho)&(rho>0)):raise ValueError('positive finite density required')
    x=np.log(rho);q=np.quantile(x,[.25,.75]);span=q[1]-q[0]
    if span<=0:raise ValueError('no density contrast')
    t=(z-z.mean())/.02; cap=((ra<80)|(ra>300)).astype(float)
    X=np.column_stack([np.ones(len(x)),(x-x.mean())/span,t,t*t]);
    if np.ptp(cap):X=np.column_stack([X,cap])
    return X,span

def contrast_se(X,cov):
    if X.shape[0]<=X.shape[1] or np.linalg.matrix_rank(X)<X.shape[1]:raise ValueError('rank deficient design')
    info=X.T@cho_solve(cho_factor(cov,lower=True),X)
    return float(np.sqrt(np.linalg.inv(info)[1,1]))

def bound(rho,z,ra,p,error,radius):
    X,span=design(rho,z,ra);dist=cdist(p,p);out=[]
    for independent,correlated,length in SCENARIOS:
        v=(5/np.log(10))/(C*z);cov=np.diag(error**2+(v*independent)**2)
        if correlated:cov+=(v*correlated)[:,None]*(v*correlated)[None,:]*np.exp(-dist/length)
        se=contrast_se(X,cov);out.append(70*np.expm1(np.log(10)/5*2.8016*se))
    overlap=(dist<2*radius)&(dist>0)
    return dict(n=len(z),median_error=round(float(np.median(error)),3),iqr_log_density=round(float(span),3),median_overlap_neighbors=round(float(np.median(overlap.sum(1))),1),mde=[round(float(v),3) for v in out])

def run(root,raw,mask_paths):
    mask=load_mask(mask_paths);data,random=build(root,raw,mask)
    other=['o_DMcal','o_DMtf','o_DMsnIa','o_DMsbfo','o_DMsbfi'];cols=['1PGC','RAJ2000','DEJ2000','Vcmb','o_DMfp','e_DMfp','e_DMsnII']+other
    d=pd.read_csv(root/'cosmicflows4/cf4_groups.tsv',sep='\t',comment='#',usecols=cols,dtype=str).iloc[2:].apply(pd.to_numeric,errors='coerce');z=d.Vcmb/C;sel=z.between(.01,.15)&covered(mask,d.RAJ2000,d.DEJ2000);d=d.loc[sel].copy();z=z[sel].to_numpy();ra=d.RAJ2000.to_numpy();p=positions(ra,d.DEJ2000,z);e=d.e_DMfp.to_numpy();fp=((d.o_DMfp>0)&np.isfinite(e)&(e>0)&(d[other].fillna(0)<=0).all(axis=1)&~(d.e_DMsnII>0)).to_numpy()
    for radius in (20,30):
        g=aperture_gate(p,radius,mask);a=summarize(p,radius,data,random[1]);b=summarize(p,radius,data,random[5]);v=g&fp&(b[:,1]>=25)&np.isfinite(b[:,0])&(b[:,0]>0);common=v&(a[:,1]>=25)&np.isfinite(a[:,0])&(a[:,0]>0)
        for label,keep,rho in [('5% supported',v,b[:,0]),('5% block10',v&(b[:,2]>=10),b[:,0]),('common 5%',common,b[:,0]),('common 1%',common,a[:,0])]:
            print(radius,label,bound(rho[keep],z[keep],ra[keep],p[keep],e[keep],radius),flush=True)
    print('DESIGN ONLY: no distance or H0 outcomes read')

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('root',type=Path);p.add_argument('raw',type=Path);p.add_argument('mask_parts',type=Path,nargs=3);a=p.parse_args();run(a.root,a.raw,a.mask_parts)
