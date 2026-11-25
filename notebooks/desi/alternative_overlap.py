"""Outcome-blind P6 feasibility audit; no final environment labels."""
import argparse
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.integrate import cumulative_trapezoid
from scipy.spatial import cKDTree
from desivast_catalog_loader import header, read_table, xyz, load_catalog, VoidGeometry, radec_to_xyz


def avism_xyz(d, frame):
    z=d[frame].to_numpy(); a,b=np.deg2rad(d.RA),np.deg2rad(d.DEC)
    grid=np.linspace(0,.8,80001)
    r=np.interp(z,grid,299792.458/67.8*np.r_[0,cumulative_trapezoid(1/np.sqrt(.31*(1+grid)**3+.69),grid)])
    return np.column_stack([r*np.cos(b)*np.cos(a),r*np.cos(b)*np.sin(a),r*np.sin(b)])


def spheres(points,centers,radii):
    return np.any(np.linalg.norm(points[:,None,:]-centers[None,:,:],axis=2)<=radii,axis=1)


def audit(root):
    d=pd.read_csv(root/'pantheonplus/Pantheon+SH0ES.dat',sep=r'\s+',usecols=['CID','RA','DEC','zHEL','zCMB','zHD'])
    windows={'base':d.zHD.between(.01,.15),'extended':d.zHD.between(.01,.24),'avism_bgs':d.zHD.between(.1,.3,inclusive='neither'),'avism_lrg':d.zHD.between(.4,.8,inclusive='neither')}
    def count(mask):
        return {k:(int((mask&w).sum()),int(d.loc[mask&w,'CID'].nunique())) for k,w in windows.items()}
    print('window totals',count(np.ones(len(d),bool)))
    catalogs=[]; gparts=[]; vid=[]; zparts=[]
    for cap in ('NGC','SGC'):
        m,s=load_catalog(root/f'DESIVAST_BGS_VOLLIM_VoidFinder_{cap}.fits');catalogs.append((cap,m,s))
        with (root/f'DESIVAST_BGS_VOLLIM_V2_ZOBOV_{cap}.fits').open('rb') as f:
            h=header(f);v,z,g=[read_table(f,k) for k in ('VOIDS','ZONEVOID','GALZONE')]
            assert not f.read(1) and float(h['OMEGAM'])==.315 and float(h['HP'])==1
        good=(v['EDGE_AREA']==0)&(v['TOT_AREA']>0)&(v['RADIUS']>0)&np.isfinite(xyz(v)).all(axis=1)
        print(cap,'ZOBOV valid centers',int(good.sum()),'redshift in range',int(((v['REDSHIFT']>=0)&(v['REDSHIFT']<=.24)).sum()),'total',len(v),'largest void unique',len(np.unique(z['VOID1'])))
        mapping=dict(zip(z['ZONE'],z['VOID0'])); ids=set(v['VOID'][good]); finite=np.isfinite(xyz(g)).all(axis=1)
        # Nearest of all finite listed sites, THEN apply flags; never skip an edge site to force a match.
        g=g[finite];gparts.append(xyz(g));vid.append(np.array([mapping.get(x,-1) in ids for x in g['ZONE']])&(g['EDGE']==0)&(g['OUT']==0));zparts.append((xyz(v[good]),v['RADIUS'][good]))
    geom=VoidGeometry(catalogs);tree=cKDTree(np.concatenate(gparts));ok=np.concatenate(vid)
    for frame in ('zHEL','zCMB','zHD'):
        p=radec_to_xyz(d.RA,d.DEC,d[frame]);valid=np.isfinite(p).all(axis=1);dist=np.full(len(d),np.inf);site=np.zeros(len(d),bool)
        dd,ii=tree.query(p[valid]);dist[valid]=dd;site[valid]=ok[ii]
        print(frame,'VF interior',count(np.array([geom.classify(x)[0]=='interior_candidate' for x in p])))
        for limit in (5,10): print(frame,'ZOBOV nearest site proxy',limit,count(site&(dist<=limit)))
        zhit=np.zeros(len(d),bool)
        for c,r in zparts: zhit[valid]|=spheres(p[valid],c,r)
        print(frame,'ZOBOV effective sphere proxy',count(zhit))
        p=avism_xyz(d,frame)
        for sample,lo,hi in [('BGS',.1,.3),('LRG',.4,.8)]:
            path=root/'avism'/f'{sample}_catalogue_clean.txt';a=np.loadtxt(path,skiprows=2);assert len(a)==int(path.open().readline()) and np.isfinite(a).all() and np.all(a[:,8]>0)
            valid=(d[frame]>lo)&(d[frame]<hi)&np.isfinite(p).all(axis=1)
            for start in (1,4): print(frame,'AVISM',sample,'divergence' if start==1 else 'geometric',count(valid&spheres(p,a[:,start:start+3],a[:,8])))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('root',type=Path);audit(parser.parse_args().root)
