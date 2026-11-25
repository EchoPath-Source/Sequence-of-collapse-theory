"""Outcome-blind BGS_ANY counts-in-spheres feasibility, not filament labels."""
import argparse
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.spatial import cKDTree
from scipy.stats import qmc, spearmanr
from coverage_overlap import tables, load_mask, covered, positions, C

EDGES=np.r_[np.arange(.01,.24,.02),.24]
RADII=(10.,20.,30.)


def shell(z):
    return np.clip(np.searchsorted(EDGES,z,side='right')-1,0,len(EDGES)-2)


def read(path, random=False):
    h,t=list(tables(path))[1]
    if random and (h.get('SAMPSTRD'),h.get('SAMPOFF'))!=('100','0'):
        raise ValueError('unexpected random sample')
    if not random and h.get('DESIDR')!='dr1':raise ValueError('wrong data release')
    z=t['Z']; good=(z>=.01)&(z<=.24)
    a={k:np.asarray(t[k][good]) for k in ('RA','DEC','Z','WEIGHT','PHOTSYS')}
    a['index']=np.flatnonzero(good) if random else np.asarray(t['TARGETID'][good])
    if not np.isfinite(positions(a['RA'],a['DEC'],a['Z'])).all() or not np.all(np.isfinite(a['WEIGHT'])&(a['WEIGHT']>0)) or not np.isin(a['PHOTSYS'],[b'N',b'S']).all():raise ValueError('invalid inputs')
    return a


def join(parts):return {k:np.concatenate([a[k] for a in parts]) for k in parts[0]}


def normalize(d,r):
    """Per-cap, photometric system and redshift-shell normalization before mask cut."""
    w=np.full(len(r['Z']),np.nan); ds,rs=shell(d['Z']),shell(r['Z'])
    for phot in (b'N',b'S'):
        a=d['PHOTSYS']==phot;b=r['PHOTSYS']==phot
        for k in range(len(EDGES)-1):
            di=a&(ds==k);ri=b&(rs==k)
            if not np.any(di) and not np.any(ri):continue
            if not np.any(di) or not np.any(ri):raise ValueError('missing data/random shell support')
            w[ri]=r['WEIGHT'][ri]*d['WEIGHT'][di].sum()/r['WEIGHT'][ri].sum()
    if not np.all(np.isfinite(w)&(w>0)):raise ValueError('bad normalization')
    return w


def build(root, random_dir, mask):
    dp=[];dw=[];rp=[];rw=[];par=[];ids=[]
    for cap,files in [('NGC',['BGS_ANY_NGC_part1.fits','BGS_ANY_NGC_part2.fits']),('SGC',['lss/BGS_ANY_SGC_clustering.dat.fits'])]:
        d=join([read(root/p) for p in files]);r=read(random_dir/f'BGS_ANY_{cap}_0_clustering_ran_1pct.fits.bin',True)
        ids.append(d['index']); w=normalize(d,r); dm=covered(mask,d['RA'],d['DEC']);rm=covered(mask,r['RA'],r['DEC'])
        print(cap,'radial data/random',len(dm),len(rm),'masked',int(dm.sum()),int(rm.sum()),'alpha quantiles',np.quantile(w/r['WEIGHT'],[0,.5,1]).round(3),flush=True)
        dp.append(positions(d['RA'][dm],d['DEC'][dm],d['Z'][dm]));dw.append(d['WEIGHT'][dm]);rp.append(positions(r['RA'][rm],r['DEC'][rm],r['Z'][rm]));rw.append(w[rm]);par.append(r['index'][rm]%2)
    allids=np.concatenate(ids)
    if len(np.unique(allids))!=len(allids):raise ValueError('duplicate selected target ID across files')
    return cKDTree(np.concatenate(dp)),np.concatenate(dw),cKDTree(np.concatenate(rp)),np.concatenate(rw),np.concatenate(par)


def offsets(power):
    a=qmc.Sobol(d=3,scramble=True,seed=20261125).random_base2(power)
    r=a[:,0]**(1/3); z=2*a[:,1]-1; phi=2*np.pi*a[:,2]
    return r[:,None]*np.column_stack([np.sqrt(1-z*z)*np.cos(phi),np.sqrt(1-z*z)*np.sin(phi),z])


def fractions(points,radius,mask,power=10):
    off=offsets(power)*radius; result=[]; limits=np.linalg.norm(positions([0,0],[0,0],[.01,.24]),axis=1)
    for chunk in np.array_split(points,max(1,(len(points)+63)//64)):
        x=chunk[:,None,:]+off; norm=np.linalg.norm(x,axis=-1)
        ra=np.rad2deg(np.arctan2(x[...,1],x[...,0]))%360;dec=np.rad2deg(np.arctan2(x[...,2],np.hypot(x[...,0],x[...,1])))
        result.extend((covered(mask,ra,dec)&(norm>=limits[0])&(norm<=limits[1])).mean(axis=1))
    return np.array(result)


def counts(points,radius,dt,dw,rt,rw,par):
    out=[]
    for start in range(0,len(points),64):
        p=points[start:start+64]; di=dt.query_ball_point(p,radius);ri=rt.query_ball_point(p,radius)
        for a,b in zip(di,ri):
            a=np.asarray(a,int);b=np.asarray(b,int);ww=rw[b];s=ww.sum(); eff=s*s/(ww@ww) if s else 0.
            # Interleaved half samples: stress test only; same parent random catalog.
            s0=2*ww[par[b]==0].sum();s1=2*ww[par[b]==1].sum();dd=dw[a].sum()
            out.append((len(a),len(b),eff,dd/s if s else np.nan,dd/s0 if s0 else np.nan,dd/s1 if s1 else np.nan))
    return np.asarray(out).reshape(-1,6)


def run(root,random_dir,mask_paths):
    mask=load_mask(mask_paths);trees=build(root,random_dir,mask)
    sn=pd.read_csv(root/'pantheonplus/Pantheon+SH0ES.dat',sep=r'\s+',usecols=['CID','RA','DEC','zHD','zCMB'])
    datasets=[('SN',sn,'RA','DEC','zHD','zCMB','CID')]
    for name,key in [('groups','1PGC'),('galaxies','PGC')]:
        d=pd.read_csv(root/'cosmicflows4'/f'cf4_{name}.tsv',sep='\t',comment='#',usecols=[key,'RAJ2000','DEJ2000','Vcmb'],dtype=str).iloc[2:].apply(pd.to_numeric,errors='coerce');d['z']=d.Vcmb/C;datasets.append((name,d,'RAJ2000','DEJ2000','z','z',key))
    for name,d,ra,dec,cut,frame,key in datasets:
        sel=d[cut].between(.01,.15)&covered(mask,d[ra],d[dec]);sub=d.loc[sel].reset_index(drop=True);p=positions(sub[ra],sub[dec],sub[frame]);valid=np.isfinite(p).all(axis=1);p=p[valid];sub=sub.loc[valid].reset_index(drop=True)
        print(name,'covered centers',len(p),flush=True)
        for radius in RADII:
            f=fractions(p,radius,mask); f2=fractions(p,radius,mask,11); m=counts(p,radius,*trees)
            print(name,radius,'random count quantiles',np.quantile(m[:,1],[0,.1,.5,.9,1]),'eff >=25/50',int((m[:,2]>=25).sum()),int((m[:,2]>=50).sum()),'fraction max change',float(np.max(abs(f-f2))),flush=True)
            for thresh in (.7,.8,.9):
                keep=(f>=thresh)&(f2>=thresh)&(m[:,2]>=25); both=keep&np.isfinite(m[:,4:6]).all(axis=1);rho=spearmanr(m[both,4],m[both,5]).statistic if both.sum()>2 else np.nan
                positive=both&(m[:,3]>0);rel=np.abs(m[positive,4]-m[positive,5])/m[positive,3]
                print('gate',thresh,'rows',int(keep.sum()),'IDs',sub.loc[keep,key].nunique(),'eff>=50',int((keep&(m[:,2]>=50)).sum()),'split rho',round(float(rho),3),'split median fractional difference',round(float(np.median(rel)),3) if len(rel) else None,flush=True)
    print('GEOMETRY_ONLY; ratio is exploratory weighted tracer density, no ranks or filament labels, no H0 fit')

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('root',type=Path);p.add_argument('random_dir',type=Path);p.add_argument('mask_parts',type=Path,nargs=3);a=p.parse_args();run(a.root,a.random_dir,a.mask_parts)
