"""Conservative V2 mesh parity diagnostic, not authoritative membership."""
import argparse
from pathlib import Path
from collections import Counter
import numpy as np
import pandas as pd
from coverage_overlap import tables, load_mask, covered, positions, C
from mesh_audit import mesh_stats

RAYS=np.array([[1.,.371,.619],[-.417,1.,.283],[.217,-.529,1.]])
RAYS/=np.linalg.norm(RAYS,axis=1)[:,None]


def triangles(t):
    return np.stack([np.column_stack([t[f'P{i}_{k}'] for k in 'XYZ']) for i in (1,2,3)],axis=1)


def parity(p,t):
    """Three independent ray directions; any boundary or disagreement => None."""
    a=t[:,0];e1=t[:,1]-a;e2=t[:,2]-a;s=p-a
    q=np.cross(s,e1); hits=[]
    for d in RAYS:
        h=np.cross(d,e2); det=np.einsum('ij,ij->i',e1,h); ok=np.abs(det)>1e-12
        inv=np.zeros(len(det)); inv[ok]=1/det[ok]
        u=np.einsum('ij,ij->i',s,h)*inv;v=(q@d)*inv;dist=np.einsum('ij,ij->i',e2,q)*inv
        eps=1e-9
        incl=ok&(u>=-eps)&(v>=-eps)&(u+v<=1+eps)&(dist>=-eps)
        if np.any(incl&((abs(dist)<=eps)|(abs(u)<=eps)|(abs(v)<=eps)|(abs(1-u-v)<=eps))):return None
        hits.append(int(incl.sum())%2)
    return bool(hits[0]) if len(set(hits))==1 else None


def audit(root,mask_paths):
    mask=load_mask(mask_paths)
    sn=pd.read_csv(root/'pantheonplus/Pantheon+SH0ES.dat',sep=r'\s+',usecols=['CID','RA','DEC','zHD','zCMB']);
    datasets=[('SN',sn,'RA','DEC','zHD','zCMB','CID')]
    for name,key in [('groups','1PGC'),('galaxies','PGC')]:
        d=pd.read_csv(root/'cosmicflows4'/f'cf4_{name}.tsv',sep='\t',comment='#',usecols=[key,'RAJ2000','DEJ2000','Vcmb'],dtype=str).iloc[2:].apply(pd.to_numeric,errors='coerce');d['z']=d.Vcmb/C;datasets.append((name,d,'RAJ2000','DEJ2000','z','z',key))
    inputs=[]
    for name,d,ra,dec,cut,frame,key in datasets:
        sel=d[cut].between(.01,.24)&covered(mask,d[ra],d[dec]);sub=d.loc[sel].reset_index(drop=True); p=positions(sub[ra],sub[dec],sub[frame]);inputs.append((name,sub,p,cut,key))
    for method in ('VIDE','REVOLVER'):
        matches=[[[] for _ in range(len(p))] for _,_,p,_,_ in inputs];amb=[np.zeros(len(p),bool) for _,_,p,_,_ in inputs]
        for cap in ('NGC','SGC'):
            hdus=list(tables(root/f'DESIVAST_BGS_VOLLIM_V2_{method}_{cap}.fits'));v,t=hdus[1][1],hdus[4][1]; ids=t['VOID']; good=(v['EDGE_AREA']==0)&(v['TOT_AREA']>0); vv=v[good]; a=np.searchsorted(ids,vv['VOID'],'left');b=np.searchsorted(ids,vv['VOID'],'right'); eligible=0
            for row,i,j in zip(vv,a,b):
                if i==j or not mesh_stats(t[i:j])[0]:continue
                eligible+=1;tri=triangles(t[i:j]);lo=tri.min(axis=(0,1));hi=tri.max(axis=(0,1))
                for k,(_,_,p,_,_) in enumerate(inputs):
                    cand=np.flatnonzero(np.all((p>=lo)&(p<=hi),axis=1))
                    for ix in cand:
                        hit=parity(p[ix],tri)
                        if hit is None:amb[k][ix]=True
                        elif hit:matches[k][ix].append((cap,int(row['VOID'])))
            print(method,cap,'eligible closed zero-edge meshes',eligible,flush=True)
        for k,(name,d,p,cut,key) in enumerate(inputs):
            labels=np.array(['ambiguous' if amb[k][i] or len(m)>1 else 'candidate' if len(m)==1 else 'unclassified' for i,m in enumerate(matches[k])]);
            for hi in (.15,.24):
                w=d[cut].between(.01,hi).to_numpy();keep=w&(labels=='candidate');print(method,name,hi,dict(Counter(labels[w])), 'distinct IDs',d.loc[keep,key].nunique(),'voids',len({matches[k][i][0] for i in np.flatnonzero(keep)}),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('root',type=Path);p.add_argument('mask_parts',type=Path,nargs=3);a=p.parse_args();audit(a.root,a.mask_parts)
