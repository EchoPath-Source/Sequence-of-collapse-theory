"""Paired outcome-blind 1%/5% BGS density diagnostic on CF4 groups."""
import argparse
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.spatial import cKDTree
from scipy.stats import qmc, spearmanr
from coverage_overlap import tables, load_mask, covered, positions, C

EDGES=np.r_[np.arange(.01,.24,.02),.24]
FIELDS=('RA','DEC','Z','WEIGHT','PHOTSYS')


def read(path,pct=0):
    h,t=list(tables(path))[1]
    if pct==1 and (h.get('SAMPSTRD'),h.get('SAMPOFF'))!=('100','0'):raise ValueError('unexpected 1% sample')
    if pct==5 and ((h.get('SAMPSEED'),h.get('SAMPBLCK'),h.get('SAMPFRAC'))!=('20261125','1000','0.05') or len(t)%1000):raise ValueError('unexpected 5% sample')
    if not pct and h.get('DESIDR')!='dr1':raise ValueError('unexpected release')
    i=np.flatnonzero((t['Z']>=.01)&(t['Z']<=.24));a={k:np.asarray(t[k][i]) for k in FIELDS}
    a['id']=i if pct else t['TARGETID'][i]
    if not np.all(np.isfinite(a['WEIGHT'])&(a['WEIGHT']>0)) or not np.isin(a['PHOTSYS'],[b'N',b'S']).all():raise ValueError('invalid weights or PHOTSYS')
    if not np.isfinite(positions(a['RA'],a['DEC'],a['Z'])).all():raise ValueError('invalid coordinates')
    return a


def normalize(d,r):
    w=np.full(len(r['Z']),np.nan)
    for phot in (b'N',b'S'):
        for k,(lo,hi) in enumerate(zip(EDGES[:-1],EDGES[1:])):
            di=(d['PHOTSYS']==phot)&(d['Z']>=lo)&((d['Z']<hi) if k<len(EDGES)-2 else (d['Z']<=hi))
            ri=(r['PHOTSYS']==phot)&(r['Z']>=lo)&((r['Z']<hi) if k<len(EDGES)-2 else (r['Z']<=hi))
            if not di.any() and not ri.any():continue
            if not di.any() or not ri.any():raise ValueError('missing normalization stratum')
            w[ri]=r['WEIGHT'][ri]*d['WEIGHT'][di].sum()/r['WEIGHT'][ri].sum()
    if not np.all(np.isfinite(w)&(w>0)):raise ValueError('invalid normalization')
    return w


def build(root,raw,mask):
    data=[];weights=[];ids=[];random={1:[],5:[]}
    for cap,files in [('NGC',['BGS_ANY_NGC_part1.fits','BGS_ANY_NGC_part2.fits']),('SGC',['lss/BGS_ANY_SGC_clustering.dat.fits'])]:
        parts=[read(root/f) for f in files];d={k:np.concatenate([x[k] for x in parts]) for k in parts[0]};ids.append(d['id'])
        m=covered(mask,d['RA'],d['DEC']);data.append(positions(d['RA'][m],d['DEC'][m],d['Z'][m]));weights.append(d['WEIGHT'][m])
        for pct in (1,5):
            r=read(raw/f'BGS_ANY_{cap}_0_clustering_ran_{pct}pct.fits.bin',pct);w=normalize(d,r);m=covered(mask,r['RA'],r['DEC'])
            random[pct].append((positions(r['RA'][m],r['DEC'][m],r['Z'][m]),w[m],r['id'][m]//1000+(100000 if cap=='SGC' else 0)))
    ids=np.concatenate(ids)
    if len(np.unique(ids))!=len(ids):raise ValueError('duplicate data IDs')
    return (cKDTree(np.concatenate(data)),np.concatenate(weights)),{pct:(cKDTree(np.concatenate([a[0] for a in v])),np.concatenate([a[1] for a in v]),np.concatenate([a[2] for a in v])) for pct,v in random.items()}


def aperture_gate(p,radius,mask):
    a=qmc.Sobol(d=3,scramble=True,seed=20261125).random_base2(11);r=a[:,0]**(1/3);z=2*a[:,1]-1;phi=2*np.pi*a[:,2];off=r[:,None]*np.column_stack([np.sqrt(1-z*z)*np.cos(phi),np.sqrt(1-z*z)*np.sin(phi),z]);lo,hi=np.linalg.norm(positions([0,0],[0,0],[.01,.24]),axis=1)
    result=[]
    for i in range(0,len(p),64):
        x=p[i:i+64,None,:]+off*radius;norm=np.linalg.norm(x,axis=-1);ra=np.rad2deg(np.arctan2(x[...,1],x[...,0]))%360;dec=np.rad2deg(np.arctan2(x[...,2],np.hypot(x[...,0],x[...,1])));c=covered(mask,ra,dec)&(norm>=lo)&(norm<=hi)
        result.extend((c.mean(axis=1)>=.8)&(c[:,:1024].mean(axis=1)>=.8))
    return np.array(result,bool)


def effective(w):
    return w.sum()**2/(w@w) if len(w) and w.sum()>0 else 0.


def summarize(p,radius,data,random):
    dt,dw=data;rt,rw,block=random;out=[]
    for i in range(0,len(p),64):
        for a,b in zip(dt.query_ball_point(p[i:i+64],radius),rt.query_ball_point(p[i:i+64],radius)):
            a=np.asarray(a,int);b=np.asarray(b,int);w=rw[b];s=w.sum();_,inv=np.unique(block[b],return_inverse=True);bw=np.bincount(inv,weights=w);dd=dw[a].sum()
            out.append((dd/s if s else np.nan,effective(w),effective(bw),bw.max()/s if s else np.nan))
    return np.array(out).reshape(-1,4)


def compare(a,b,keep):
    x,y=a[keep,0],b[keep,0];good=np.isfinite(x)&np.isfinite(y)&(x+y>0);x,y=x[good],y[good]
    if not len(x):return {'pairs':0}
    diff=2*abs(x-y)/(x+y);pos=(x>0)&(y>0)
    return {'pairs':len(x),'rho':round(float(spearmanr(x,y).statistic),4) if len(x)>2 else None,'median_symdiff':round(float(np.median(diff)),4),'p90_symdiff':round(float(np.quantile(diff,.9)),4),'median_log5_over1':round(float(np.median(np.log(y[pos]/x[pos]))),4) if pos.any() else None,'median_max_block_share_5':round(float(np.median(b[keep,3][good])),4)}


def run(root,raw,mask_paths):
    mask=load_mask(mask_paths);data,random=build(root,raw,mask)
    errors=['e_DMfp','e_DMsnII'];other=['o_DMcal','o_DMtf','o_DMsnIa','o_DMsbfo','o_DMsbfi'];cols=['1PGC','RAJ2000','DEJ2000','Vcmb','o_DMfp']+errors+other
    d=pd.read_csv(root/'cosmicflows4/cf4_groups.tsv',sep='\t',comment='#',usecols=cols,dtype=str).iloc[2:].apply(pd.to_numeric,errors='coerce');z=d.Vcmb/C;sel=z.between(.01,.15)&covered(mask,d.RAJ2000,d.DEJ2000);d=d.loc[sel].copy();p=positions(d.RAJ2000,d.DEJ2000,z[sel]);fp=((d.o_DMfp>0)&np.isfinite(d.e_DMfp)&(d.e_DMfp>0)&(d[other].fillna(0)<=0).all(axis=1)&~(d.e_DMsnII>0)).to_numpy();print('centers',len(p),'FP only proxy',fp.sum(),flush=True)
    for radius in (10,20,30):
        g=aperture_gate(p,radius,mask);a=summarize(p,radius,data,random[1]);b=summarize(p,radius,data,random[5]);u=g&(a[:,1]>=25);v=g&(b[:,1]>=25);common=u&v
        print('radius',radius,'geometry',g.sum(),'1%',u.sum(),'5%',v.sum(),'common',common.sum(),'5% FP',int((v&fp).sum()),'5% block>=10',int((v&(b[:,2]>=10)).sum()),'5% FP block>=10',int((v&fp&(b[:,2]>=10)).sum()),flush=True)
        for label,keep in [('common',common),('common_FP',common&fp),('common_block10',common&(b[:,2]>=10)),('5%_support_1%_positive',v&np.isfinite(a[:,0]))]:print(label,compare(a,b,keep),flush=True)
    print('NO outcome analysis, no final labels or power inference')


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('root',type=Path);p.add_argument('random_dir',type=Path);p.add_argument('mask_parts',nargs=3,type=Path);a=p.parse_args();run(a.root,a.random_dir,a.mask_parts)
