"""Audit V2 visualization surfaces; fail closed for unclosed geometry."""
import argparse
from pathlib import Path
import numpy as np
from coverage_overlap import tables


def mesh_stats(t):
    pts=np.stack([np.column_stack([t[f'P{i}_{k}'] for k in 'XYZ']) for i in (1,2,3)],axis=1)
    if not np.isfinite(pts).all():return False,False,0,0,0
    # Exact coordinate welding only. No tolerance-based repair.
    _,ix=np.unique(pts.reshape(-1,3),axis=0,return_inverse=True);f=ix.reshape(-1,3)
    e=np.concatenate([f[:,[0,1]],f[:,[1,2]],f[:,[2,0]]]); direction=e[:,0]<e[:,1];e.sort(axis=1)
    _,j,n=np.unique(e,axis=0,return_inverse=True,return_counts=True)
    s=np.bincount(j,weights=np.where(direction,1.,-1.))
    cross=np.cross(pts[:,1]-pts[:,0],pts[:,2]-pts[:,0]); deg=int((np.linalg.norm(cross,axis=1)==0).sum())
    return bool(np.all(n==2)&(deg==0)),bool(np.all(s==0)),int((n==1).sum()),int((n>2).sum()),deg


def audit(path):
    hdus=list(tables(path)); h=hdus[0][0]; v,t=hdus[1][1],hdus[4][1]; ids=t['VOID'];
    if np.any(np.diff(ids)<0) or len(set(v['VOID']))!=len(v) or not set(np.unique(ids))<=set(v['VOID']):raise ValueError('unexpected IDs')
    valid=(v['TOT_AREA']>0)&(v['EDGE_AREA']==0)
    counts={'voids':len(v),'triangles':len(t),'missing_mesh':len(set(v['VOID'])-set(ids)),'edge_zero':int(valid.sum()),'edge_zero_missing_mesh':0,'closed':0,'closed_oriented':0,'edge_zero_closed':0,'edge_zero_closed_oriented':0,'open_edge_meshes':0,'nonmanifold_meshes':0,'degenerate_meshes':0,'valid_redshifts':int(((v['REDSHIFT']>=0)&(v['REDSHIFT']<=.24)).sum())}
    starts=np.searchsorted(ids,v['VOID'],'left');ends=np.searchsorted(ids,v['VOID'],'right')
    for i,(a,b) in enumerate(zip(starts,ends)):
        if a==b:
            counts['edge_zero_missing_mesh']+=int(valid[i]);continue
        closed,orient,open_e,nonman,deg=mesh_stats(t[a:b]);counts['closed']+=closed;counts['closed_oriented']+=closed and orient;counts['edge_zero_closed']+=valid[i] and closed;counts['edge_zero_closed_oriented']+=valid[i] and closed and orient;counts['open_edge_meshes']+=open_e>0;counts['nonmanifold_meshes']+=nonman>0;counts['degenerate_meshes']+=deg>0
    print(path.name,counts,flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('root',type=Path);a=p.parse_args()
    for path in sorted(a.root.glob('*V2*fits')):audit(path)
