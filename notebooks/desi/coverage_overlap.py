"""Outcome-blind coverage and VoidFinder candidate counts. No distance outcomes."""
import argparse
from pathlib import Path
from collections import Counter
import numpy as np
import pandas as pd
from scipy.integrate import cumulative_trapezoid
from scipy.spatial import cKDTree

NSIDE=1024
NPIX=12*NSIDE**2
C=299792.458


def nested_pixel(ra, dec, nside=NSIDE):
    """HEALPix face coordinates and Morton ordering, RA/Dec in degrees."""
    if nside<1 or nside&(nside-1): raise ValueError('nside must be power of two')
    a,b=np.broadcast_arrays(np.asarray(ra,float),np.asarray(dec,float))
    shape=a.shape; a,b=a.ravel(),b.ravel()
    valid=np.isfinite(a)&np.isfinite(b)&(a>=0)&(a<360)&(abs(b)<=90)
    out=np.full(len(a),-1,dtype=np.int64)
    z=np.sin(np.deg2rad(b[valid])); t=a[valid]/90; az=abs(z)
    equ=az<=2/3; face=np.empty(len(z),dtype=np.int64); x=face.copy(); y=face.copy()
    j=np.floor(nside*(.5+t[equ]-.75*z[equ])).astype(np.int64)
    k=np.floor(nside*(.5+t[equ]+.75*z[equ])).astype(np.int64)
    f,g=j//nside,k//nside
    face[equ]=np.where(f==g,(f%4)+4,np.where(f<g,f%4,(g%4)+8))
    x[equ]=k%nside; y[equ]=nside-1-j%nside
    q=t[~equ]; sector=np.minimum(3,q.astype(np.int64)); frac=q-sector
    r=nside*np.sqrt(3*(1-az[~equ])); j=np.minimum(nside-1,(frac*r).astype(np.int64)); k=np.minimum(nside-1,((1-frac)*r).astype(np.int64))
    north=z[~equ]>=0
    face[~equ]=sector+np.where(north,0,8)
    x[~equ]=np.where(north,nside-1-k,j); y[~equ]=np.where(north,nside-1-j,k)
    morton=np.zeros(len(x),dtype=np.int64)
    for bit in range(nside.bit_length()-1):
        morton|=((x>>bit)&1)<<(2*bit); morton|=((y>>bit)&1)<<(2*bit+1)
    out[valid]=face*nside*nside+morton
    return out.reshape(shape)


def header(f):
    h={}
    while True:
        b=f.read(2880)
        if len(b)!=2880: raise ValueError('truncated header')
        for i in range(0,2880,80):
            c=b[i:i+80].decode('ascii'); k=c[:8].strip()
            if k=='END':return h
            if c[8:10]=='= ':h[k]=c[10:].split('/')[0].strip().strip("'").strip()


def tables(path):
    """Memory-map scalar tables in the staged releases; reject transforms."""
    types={'D':'>f8','K':'>i8','I':'>i2','L':'S1','1A':'S1','E':'>f4'}
    with Path(path).open('rb') as f:
        h=header(f)
        if h.get('SIMPLE')!='T' or h.get('NAXIS')!='0':raise ValueError('unexpected primary HDU')
        yield h,None
        while f.tell()<Path(path).stat().st_size:
            h=header(f)
            if (h.get('XTENSION'),h.get('BITPIX'),h.get('NAXIS'),h.get('PCOUNT'),h.get('GCOUNT'))!=('BINTABLE','8','2','0','1'):raise ValueError('unsupported table')
            fields=[]
            for i in range(1,int(h['TFIELDS'])+1):
                if any(k+str(i) in h for k in ('TSCAL','TZERO','TNULL','TDIM')):raise ValueError('unsupported column transform')
                fields.append((h['TTYPE'+str(i)],types[h['TFORM'+str(i)]]))
            dt=np.dtype(fields); n=int(h['NAXIS2']); length=n*dt.itemsize; offset=f.tell()
            if dt.itemsize!=int(h['NAXIS1']) or offset+(length+2879)//2880*2880>Path(path).stat().st_size:raise ValueError('invalid row layout')
            yield h,np.memmap(path,dtype=dt,mode='r',offset=offset,shape=(n,))
            f.seek(offset+(length+2879)//2880*2880)


def load_mask(paths):
    seen=np.zeros(NPIX,bool); done=seen.copy()
    for path in paths:
        hdus=list(tables(path)); h,t=hdus[1]
        if len(hdus)!=2 or h['HPXNSIDE']!='1024' or h['HPXNEST']!='T':raise ValueError('unexpected mask convention')
        for i in range(0,len(t),200000):
            a=t[i:i+200000]; p=a['HPXPIXEL']; expected=nested_pixel(a['RA'],a['DEC'])
            if not np.array_equal(p,expected):raise ValueError(f'mask coordinate/index mismatch: {np.count_nonzero(p!=expected)} of {len(p)}')
            if np.any(p<0) or np.any(p>=NPIX) or np.any(seen[p]) or len(np.unique(p))!=len(p):raise ValueError('invalid or duplicate pixels')
            if not np.isin(a['DONE'],[b'T',b'F']).all():raise ValueError('invalid DONE')
            seen[p]=True;done[p]=a['DONE']==b'T'
    if not seen.all():raise ValueError('missing pixels')
    return done


def covered(mask,ra,dec):
    ids=nested_pixel(ra,dec); out=np.zeros(ids.shape,bool); good=ids>=0;out[good]=mask[ids[good]];return out


def xyz(t):return np.column_stack([t[k] for k in 'XYZ'])


def positions(ra,dec,z):
    ra,dec,z=np.broadcast_arrays(np.asarray(ra,float),np.asarray(dec,float),np.asarray(z,float)); valid=(nested_pixel(ra,dec)>=0)&np.isfinite(z)&(z>0)&(z<=.24)
    g=np.linspace(0,.24,24001); r=np.interp(z,g,2997.92458*np.r_[0,cumulative_trapezoid(1/np.sqrt(.315*(1+g)**3+.685),g)])
    a,b=np.deg2rad(ra),np.deg2rad(dec); p=np.stack([r*np.cos(b)*np.cos(a),r*np.cos(b)*np.sin(a),r*np.sin(b)],axis=-1)
    return np.where(valid[...,None],p,np.nan)


def geometry(root):
    parts=[]
    for cap in ('NGC','SGC'):
        hdus=list(tables(root/f'DESIVAST_BGS_VOLLIM_VoidFinder_{cap}.fits')); h=hdus[0][0]; m,s=hdus[1][1],hdus[2][1]
        if (float(h['OMEGAM']),float(h['HP']),h['METRIC'])!=(.315,1.,'comoving'):raise ValueError('wrong geometry')
        centers=xyz(s); radii=s['RADIUS']; edges=dict(zip(m['VOID'],m['EDGE']))
        parts.append((cap,cKDTree(centers),centers,radii,s['VOID'],edges))
        print('catalog header area',cap,h.get('COVDEG'))
    return parts


def classify(parts,p):
    if not np.isfinite(p).all():return 'invalid',()
    hits=set()
    for cap,tree,c,r,ids,e in parts:
        ix=np.asarray(tree.query_ball_point(p,float(r.max())),int); ix=ix[np.linalg.norm(c[ix]-p,axis=1)<=r[ix]]
        hits.update((cap,int(ids[i]),int(e[ids[i]])) for i in ix)
    hits=tuple(sorted(hits))
    if not hits:return 'unmatched',hits
    if len(hits)>1:return 'ambiguous',hits
    return ('interior' if hits[0][2]==0 else 'edge'),hits


def run(root,mask_paths):
    mask=load_mask(mask_paths); print('verified full-grid center-to-index roundtrip; DONE',mask.sum())
    parts=geometry(root)
    sn=pd.read_csv(root/'pantheonplus/Pantheon+SH0ES.dat',sep=r'\s+',usecols=['CID','RA','DEC','zHD','zCMB','zHEL'])
    datasets=[('SN',sn,'RA','DEC','CID','zHD',[(f,sn[f]) for f in ('zHEL','zCMB','zHD')])]
    for name,key in [('groups','1PGC'),('galaxies','PGC')]:
        d=pd.read_csv(root/'cosmicflows4'/f'cf4_{name}.tsv',sep='\t',comment='#',usecols=[key,'RAJ2000','DEJ2000','Vcmb'],dtype=str).iloc[2:].apply(pd.to_numeric,errors='coerce');d['z']=d.Vcmb/C
        datasets.append((name,d,'RAJ2000','DEJ2000',key,'z',[('CMB',d.z)]))
    for name,d,ra,dec,key,cutz,frames in datasets:
        inmask=covered(mask,d[ra],d[dec]);
        for frame,z in frames:
            p=positions(d[ra],d[dec],z); res=[classify(parts,x) for x in p]; labels=np.array([x[0] for x in res]);
            for hi in (.15,.24):
                sel=d[cutz].between(.01,hi).to_numpy(); inside=sel&inmask; keep=inside&(labels=='interior');print(name,frame,hi,'total',sel.sum(),'covered',inside.sum(),'covered labels',dict(Counter(labels[inside])),'interior outside mask',int((sel&~inmask&(labels=='interior')).sum()),'covered interior distinct IDs',d.loc[keep,key].nunique(),'voids',len({res[i][1][0][:2] for i in np.flatnonzero(keep)}))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('root',type=Path);p.add_argument('mask_parts',type=Path,nargs=3);a=p.parse_args();run(a.root,a.mask_parts)
