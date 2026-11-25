"""DESIVAST DR1 v1.0 VoidFinder geometry; no H0 outcome analysis.
Narrow FITS reader for the released scalar D/K binary tables only.
"""
from pathlib import Path
import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.spatial import cKDTree


def header(f):
    h = {}
    while True:
        b = f.read(2880)
        if len(b) != 2880:
            raise ValueError('Incomplete FITS header')
        for i in range(0, 2880, 80):
            c = b[i:i+80].decode('ascii')
            k = c[:8].strip()
            if k == 'END':
                return h
            if c[8:10] == '= ':
                h[k] = c[10:].split('/')[0].strip().strip("'").strip()


def read_table(f, expected):
    h = header(f)
    if (h.get('XTENSION'), h.get('EXTNAME'), h.get('BITPIX'), h.get('NAXIS'), h.get('PCOUNT'), h.get('GCOUNT')) != ('BINTABLE', expected, '8', '2', '0', '1'):
        raise ValueError('Unsupported FITS extension')
    types = {'D': '>f8', 'K': '>i8'}
    fields = []
    for i in range(1, int(h['TFIELDS'])+1):
        if any(k+str(i) in h for k in ('TSCAL','TZERO','TNULL','TDIM')):
            raise ValueError('Unsupported FITS column transform')
        fields.append((h['TTYPE'+str(i)], types[h['TFORM'+str(i)]]))
    dt = np.dtype(fields)
    n = int(h['NAXIS2'])
    if n <= 0 or dt.itemsize != int(h['NAXIS1']):
        raise ValueError('Invalid FITS row layout')
    size = n*dt.itemsize
    b = f.read((size+2879)//2880*2880)
    if len(b) != (size+2879)//2880*2880:
        raise ValueError('Truncated FITS data')
    for i in range(1, len(fields)+1):
        if fields[i-1][0] in ('X','Y','Z','RADIUS','R','R_EFF') and h.get('TUNIT'+str(i)) != 'Mpc h-1':
            raise ValueError('Unexpected spatial units')
    return np.frombuffer(b, dtype=dt, count=n)


def xyz(tab):
    return np.column_stack([tab[k] for k in 'XYZ'])


def load_catalog(path):
    with Path(path).open('rb') as f:
        h = header(f)
        if (h.get('SIMPLE'),h.get('NAXIS'),h.get('METRIC'),float(h['OMEGAM']),float(h['HP']),float(h['ZLIMU'])) != ('T','0','comoving',0.315,1.0,0.24):
            raise ValueError('Unexpected catalog geometry')
        m, s = read_table(f,'MAXIMALS'), read_table(f,'HOLES')
        if f.read(1):
            raise ValueError('Unexpected additional FITS data')
    for t in (m,s):
        if not np.isfinite(xyz(t)).all() or not np.isfinite(t['RADIUS']).all() or np.any(t['RADIUS']<=0):
            raise ValueError('Invalid sphere geometry')
    if len(set(m['VOID'])) != len(m) or set(s['VOID']) != set(m['VOID']) or not set(m['EDGE']).issubset({0,1,2}):
        raise ValueError('Invalid void identifiers or edge flags')
    if not np.allclose(np.linalg.norm(xyz(m),axis=1),m['R'],rtol=0,atol=1e-6):
        raise ValueError('Radial coordinates inconsistent')
    return m,s


def radec_to_xyz(ra,dec,z):
    """Comoving Mpc/h, flat LCDM Om=.315; invalid rows become NaN."""
    ra,dec,z = np.broadcast_arrays(np.asarray(ra,float),np.asarray(dec,float),np.asarray(z,float))
    valid = np.isfinite(ra)&np.isfinite(dec)&np.isfinite(z)&(ra>=0)&(ra<360)&(abs(dec)<=90)&(z>0)&(z<=.24)
    grid=np.linspace(0,.24,24001)
    dist=2997.92458*np.r_[0,cumulative_trapezoid(1/np.sqrt(.315*(1+grid)**3+.685),grid)]
    r=np.interp(z,grid,dist); a,d=np.deg2rad(ra),np.deg2rad(dec)
    out=np.stack([r*np.cos(d)*np.cos(a),r*np.cos(d)*np.sin(a),r*np.sin(d)],axis=-1)
    return np.where(valid[...,None],out,np.nan)


class VoidGeometry:
    def __init__(self, catalogs):
        self.parts=[]
        for cap,m,s in catalogs:
            centers=xyz(s); radii=np.asarray(s['RADIUS'],float)
            edges=dict(zip(m['VOID'],m['EDGE']))
            self.parts.append((cap,cKDTree(centers),centers,radii,s['VOID'],edges))

    def classify(self, point):
        """Geometric candidates only. No footprint => no final labels."""
        point=np.asarray(point,float)
        if point.shape!=(3,) or not np.isfinite(point).all():
            return 'invalid_or_outside_z',()
        hits=set()
        for cap,tree,centers,radii,ids,edges in self.parts:
            ix=np.asarray(tree.query_ball_point(point,float(radii.max())),dtype=int)
            inside=ix[np.linalg.norm(centers[ix]-point,axis=1)<=radii[ix]]
            hits.update((cap,int(ids[i]),int(edges[ids[i]])) for i in inside)
        hits=tuple(sorted(hits))
        if not hits: return 'unmatched_unclassified',hits
        if len(hits)>1: return 'ambiguous_overlap',hits
        return ('interior_candidate' if hits[0][2]==0 else 'edge_candidate'),hits
