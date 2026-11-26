"""Held-out density-history variance audit of compact extraction products."""
import argparse,json
from pathlib import Path
import numpy as np
from quijote_history_extract import sha256,REDSHIFTS,RADII
from history_discriminator import exhaust_history,conditional_mu


def ages(z,om,h):
    # Flat dust+Lambda, Gyr, no radiation.
    return 2/(3*100*h*1.022712165e-3*np.sqrt(1-om))*np.arcsinh(np.sqrt((1-om)/om)/(1+np.asarray(z))**1.5)


def response(d,t,tau,linear=False):
    if not linear:return conditional_mu(exhaust_history((d[:,:-1]+d[:,1:])/2,t,tau))
    # Linear interpolation of density, not q; resolve each interval at <= .025 Gyr.
    fine=np.concatenate([np.linspace(a,b,int(np.ceil((b-a)/.025))+1)[:-1] for a,b in zip(t[:-1],t[1:])]+[t[-1:]])
    mid=(fine[1:]+fine[:-1])/2
    values=np.stack([np.interp(mid,t,row) for row in d])
    return conditional_mu(exhaust_history(values,fine,tau))


def audit(products,om=.3175,h=.6711):
    t=ages(REDSHIFTS,om,h); print('snapshot ages Gyr',t.tolist(),'intervals',np.diff(t).tolist())
    # Holdout IDs 1 and 2 separately, fit only ID 0; no tuning on holdouts.
    for i,R in enumerate(RADII):
        rows=[]
        for a in products:
            d=a['delta'][:,i,:];valid=np.isfinite(d).all(1)&(d>=-.9).all(1)&(d<=.5).all(1)
            print('radius',R,'domain pass',int(valid.sum()),'total',len(d))
            d=d[valid];now=d[:,-1];recent=(now-d[:,-2])/(t[-1]-t[-2]);other=a['delta'][valid,1-i,-1];tidal=a['tidal_s2'][valid,i]
            X=np.column_stack([np.ones(len(d)),now,now**2,recent,other,tidal]);rows.append((d,X))
        for tau in (1.,2.,5.,10.,20.):
            targets=[response(d,t,tau,True) for d,X in rows]
            # This interpolation comparison is not a proof of true time convergence.
            for j in (1,2):
                d,X=rows[j]; y=targets[j]; midpoint=response(d,t,tau)
                for name,ncols in [('density',3),('environment',6)]:
                    coef=np.linalg.lstsq(rows[0][1][:,:ncols],targets[0],rcond=None)[0]
                    err=y-X[:,:ncols]@coef; variance=np.var(y)
                    print('R/tau/holdout',R,tau,j,name,'n',len(y),'rms',float(np.sqrt(np.mean(err**2))),'variance fraction',float(np.var(err)/variance) if variance else None,'interpolation rms',float(np.sqrt(np.mean((y-midpoint)**2))))


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('root',type=Path);a=p.parse_args();m=json.loads((a.root/'manifest.json').read_text())
    if (m['schema'],m['grid'],m['box_mpc_h'],m['assignment'],m['space'],m['omega_m'],m['h'])!=('quijote-history-v1',256,1000.,'CIC','real',.3175,.6711):raise ValueError('unexpected manifest')
    if [r['id'] for r in m['realizations']]!=[0,1,2]:raise ValueError('require fixed realization IDs 0,1,2')
    products=[]
    for r in m['realizations']:
        path=a.root/r['product']
        if sha256(path)!=r['sha256']:raise ValueError('product checksum mismatch')
        with np.load(path,allow_pickle=False) as f: d={k:f[k] for k in f.files}
        if d['delta'].shape!=(4096,2,5) or d['tidal_s2'].shape!=(4096,2) or not np.array_equal(d['redshifts'],REDSHIFTS) or not np.array_equal(d['radii'],RADII):raise ValueError('unexpected product schema')
        if not np.isfinite(d['delta']).all() or not np.isfinite(d['tidal_s2']).all() or np.any(d['tidal_s2']<0):raise ValueError('invalid field values')
        ids=d['indices'];expected=np.sort(np.random.default_rng(20261126+r['id']).choice(256**3,4096,replace=False))
        if not np.array_equal(ids,expected):raise ValueError('unexpected sampling IDs')
        if not np.array_equal(d['xyz_mpc_h'],np.column_stack(np.unravel_index(ids,(256,)*3))*1000/256):raise ValueError('coordinate mismatch')
        products.append(d)
    audit(products)

if __name__=='__main__':main()
