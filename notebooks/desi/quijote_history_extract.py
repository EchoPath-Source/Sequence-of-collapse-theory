"""Compact outcome-blind Quijote Eulerian history extraction; no distances."""
import argparse, hashlib, json
from pathlib import Path
import numpy as np
from scipy import fft

REDSHIFTS = (3, 2, 1, .5, 0)
RADII = (20., 30.)
SEED = 20261126


def sha256(path):
    with Path(path).open('rb') as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()


def overdensity(a, convention):
    a = np.asarray(a, dtype=np.float32)
    if a.ndim != 3 or len(set(a.shape)) != 1 or not np.isfinite(a).all():
        raise ValueError('expected finite cubic field')
    m = a.mean(dtype=np.float64)
    if convention == 'overdensity':
        if abs(m) > 1e-4 or a.min() < -1.0001:
            raise ValueError('invalid overdensity convention')
        return a
    if convention == 'counts' and m > 0 and a.min() >= 0:
        return (a / m - 1).astype(np.float32)
    raise ValueError('invalid counts or density convention')


def window(n, box, radius):
    """Discrete periodic real-space spherical mean, including boundary cells."""
    if not 0 < radius < box/2:
        raise ValueError('invalid radius')
    x = np.fft.fftfreq(n)*box
    w = (x[:,None,None]**2+x[None,:,None]**2+x[None,None,:]**2 <= radius**2).astype(np.float32)
    w /= w.sum(dtype=np.float64)
    return fft.rfftn(w)


def tidal_s2(fk, n, indices):
    """Trace-free tidal tensor invariant of smoothed present density."""
    x=fft.fftfreq(n); y=fft.rfftfreq(n)
    k=(x[:,None,None],x[None,:,None],y[None,None,:])
    k2=k[0]**2+k[1]**2+k[2]**2
    inv=np.divide(1.,k2,out=np.zeros_like(k2),where=k2>0)
    out=np.zeros(len(indices[0]))
    for i in range(3):
        for j in range(i,3):
            mult=k[i]*k[j]*inv-(1/3 if i==j else 0)
            if i!=j: mult=np.where((abs(k[i])==.5)|(abs(k[j])==.5),0,mult)
            mult[0,0,0]=0
            s=fft.irfftn(fk*mult.astype(np.float32),s=(n,)*3,axes=(0,1,2))[indices]
            out+=(1 if i==j else 2)*s.astype(float)**2
    return out


def extract(paths, convention, box=1000., n=256, count=4096, seed=SEED):
    if len(paths)!=len(REDSHIFTS) or not 0<count<=n**3:
        raise ValueError('five snapshots and valid sample size required')
    ids=np.sort(np.random.default_rng(seed).choice(n**3,count,replace=False))
    ix=np.unravel_index(ids,(n,)*3); xyz=np.column_stack(ix)*box/n
    w=[window(n,box,r) for r in RADII]
    hist=np.empty((count,len(RADII),len(paths))); tidal=np.empty((count,len(RADII)))
    records=[]
    for j,path in enumerate(paths):
        path=Path(path); a=np.load(path,mmap_mode='r',allow_pickle=False)
        if a.shape!=(n,)*3:raise ValueError(f'unexpected grid shape: {path}')
        records.append(dict(name=path.name,sha256=sha256(path),bytes=path.stat().st_size,mean=float(a.mean(dtype=np.float64)),dtype=str(a.dtype)))
        f=fft.rfftn(overdensity(a,convention)); f[0,0,0]=0
        for i,win in enumerate(w):
            sf=f*win
            hist[:,i,j]=fft.irfftn(sf,s=(n,)*3,axes=(0,1,2))[ix]
            if j==len(paths)-1: tidal[:,i]=tidal_s2(sf,n,ix)
    return dict(indices=ids,xyz_mpc_h=xyz,delta=hist,tidal_s2=tidal,redshifts=np.array(REDSHIFTS),radii=np.array(RADII)),records


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('root',type=Path,help='3D_cubes/fiducial directory')
    p.add_argument('output',type=Path)
    p.add_argument('--convention',required=True,choices=['overdensity','counts'])
    a=p.parse_args();a.output.mkdir(parents=True,exist_ok=True)
    manifest={'schema':'quijote-history-v1','suite':'Quijote standard fiducial','box_mpc_h':1000.,'grid':256,'assignment':'CIC','space':'real','coordinate_frame':'fixed Eulerian grid indices; origin convention unverified','convention':a.convention,'seed':SEED,'count_per_realization':4096,'omega_m':.3175,'h':.6711,'redshifts':list(REDSHIFTS),'radii_mpc_h':list(RADII),'realizations':[]}
    # Fail before processing if any required input is missing.
    paths=[[a.root/str(i)/f'df_m_256_CIC_z={z}.npy' for z in REDSHIFTS] for i in range(3)]
    missing=[str(p) for row in paths for p in row if not p.is_file()]
    if missing:raise FileNotFoundError('\n'.join(missing))
    for i,row in enumerate(paths):
        product,records=extract(row,a.convention,seed=SEED+i)
        out=a.output/f'fiducial_{i}_histories.npz';np.savez_compressed(out,**product)
        manifest['realizations'].append({'id':i,'source_files':records,'product':out.name,'sha256':sha256(out),'seed':SEED+i})
    (a.output/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')

if __name__=='__main__':main()
