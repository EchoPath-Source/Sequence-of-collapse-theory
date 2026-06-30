import argparse, re, gzip, hashlib, json
from pathlib import Path
import numpy as np, pandas as pd
from scipy.spatial import cKDTree

C_KM_S=299792.458; H0=70.0; OMEGA_M=0.3; METHOD_VERSION='sdss_void_filament_crossmatch_v0.1_local_generated_2026-06-30'

def sha256(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for chunk in iter(lambda:f.read(1024*1024), b''):
            h.update(chunk)
    return h.hexdigest()

def comoving_distance_mpc_h(z_values):
    omega_l=1-OMEGA_M; out=[]
    for z in np.asarray(z_values,dtype=float):
        if not np.isfinite(z) or z<=0: out.append(np.nan); continue
        grid=np.linspace(0,z,256); ez=np.sqrt(OMEGA_M*(1+grid)**3+omega_l)
        dc=(C_KM_S/H0)*np.trapz(1/ez, grid)
        out.append(dc*(H0/100.0))
    return np.asarray(out)

def radec_to_xyz(ra,dec,z):
    r=comoving_distance_mpc_h(z); ra=np.deg2rad(np.asarray(ra,float)); dec=np.deg2rad(np.asarray(dec,float))
    return np.column_stack([r*np.cos(dec)*np.cos(ra), r*np.cos(dec)*np.sin(ra), r*np.sin(dec)])

def read_pantheon(path):
    df=pd.read_csv(path, sep=r'\s+', comment='#')
    req=['CID','IDSURVEY','RA','DEC','zHD','zCMB']
    miss=[c for c in req if c not in df.columns]
    if miss: raise ValueError(miss)
    return df.reset_index().rename(columns={'index':'row_index'})

def parse_zrange(path):
    txt=Path(path).read_text(errors='replace')
    m=re.search(r'Redshift range:\s*([0-9.eE+-]+)\s*-\s*([0-9.eE+-]+)', txt)
    return None if not m else (float(m.group(1)), float(m.group(2)))

def sample_nickname(path):
    txt=Path(path).read_text(errors='replace')
    m=re.search(r'Sample nickname:\s*(.+)', txt)
    return m.group(1).strip() if m else Path(path).parent.name

def load_voids(root):
    root=Path(root); rows=[]
    for si in root.glob('*/comoving/*/sample_info.txt'):
        zr=parse_zrange(si)
        if zr is None: continue
        sdir=si.parent; nickname=sample_nickname(si)
        for sky in sdir.glob('sky_positions_central*.out'):
            data=pd.read_csv(sky, sep=r'\s+', comment='#', header=None)
            if data.shape[1] < 4: continue
            rows.append(pd.DataFrame({
                'void_ra':pd.to_numeric(data.iloc[:,0],errors='coerce'),
                'void_dec':pd.to_numeric(data.iloc[:,1],errors='coerce'),
                'void_z':pd.to_numeric(data.iloc[:,2],errors='coerce'),
                'void_radius_mpc_h':pd.to_numeric(data.iloc[:,3],errors='coerce'),
                'void_id': data.iloc[:,4].astype(str) if data.shape[1]>4 else data.index.astype(str),
                'void_sample': nickname,
                'void_sample_path': str(sdir.relative_to(root)),
                'void_z_min': zr[0],
                'void_z_max': zr[1]
            }))
    if not rows: raise RuntimeError('no void rows')
    voids=pd.concat(rows, ignore_index=True).dropna(subset=['void_ra','void_dec','void_z','void_radius_mpc_h'])
    xyz=radec_to_xyz(voids['void_ra'].values, voids['void_dec'].values, voids['void_z'].values)
    voids[['void_x_mpc_h','void_y_mpc_h','void_z_mpc_h']]=xyz
    return voids.reset_index(drop=True)

def open_text(path): return gzip.open(path,'rt') if str(path).endswith('.gz') else open(path,'rt')

def load_filaments(root):
    root=Path(root); path=root/'table2.dat.gz'
    if not path.exists(): path=root/'table2.dat'
    rows=[]
    with open_text(path) as f:
        for line in f:
            if not line.strip() or line.lstrip().startswith('#'): continue
            p=line.split()
            if len(p)<14: continue
            rows.append((int(p[0]), int(p[1]), int(p[2]), float(p[3]), float(p[4]), float(p[5]), float(p[6]), float(p[11]), float(p[12]), float(p[13])))
    df=pd.DataFrame(rows, columns=['filament_id','filament_point_id','filament_npts','filament_len_mpc_h','filament_x_mpc_h','filament_y_mpc_h','filament_z_mpc_h','filament_vmap','filament_density','filament_orientation_strength'])
    return df

def classify(sn, voids, fil):
    sn_xyz=radec_to_xyz(sn['RA'].values, sn['DEC'].values, sn['zHD'].values)
    # Build void trees per sample path for z coverage; avoid mixing overlapping samples? Use all covered, query subset using KDTree per sample.
    void_groups=[]
    for sample, g in voids.groupby('void_sample_path'):
        xyz=g[['void_x_mpc_h','void_y_mpc_h','void_z_mpc_h']].to_numpy()
        mask=np.isfinite(xyz).all(axis=1) & np.isfinite(g['void_radius_mpc_h'].to_numpy())
        gg=g.loc[mask].reset_index(drop=True)
        if len(gg):
            void_groups.append((gg['void_z_min'].iloc[0], gg['void_z_max'].iloc[0], sample, gg, cKDTree(gg[['void_x_mpc_h','void_y_mpc_h','void_z_mpc_h']].to_numpy())))
    fxyz=fil[['filament_x_mpc_h','filament_y_mpc_h','filament_z_mpc_h']].to_numpy()
    fmask=np.isfinite(fxyz).all(axis=1)
    fil=fil.loc[fmask].reset_index(drop=True); fxyz=fxyz[fmask]
    ftree=cKDTree(fxyz)
    rows=[]
    for i, rec in sn.iterrows():
        z=float(rec['zHD']); base=dict(row_index=int(rec['row_index']), CID=str(rec['CID']), IDSURVEY=int(rec['IDSURVEY']), RA=float(rec['RA']), DEC=float(rec['DEC']), zHD=z, zCMB=float(rec['zCMB']), environment_method=METHOD_VERSION, catalog_source='SDSS void catalog 2014.06.18 plus Tempel/Bisous SDSS filament catalog J/MNRAS/438/3465')
        x=sn_xyz[i]
        void_label='outside_catalog_coverage'; nearest_void_id=''; nearest_void_sample=''; void_distance=np.nan; void_radius=np.nan; void_ratio=np.nan
        # choose nearest ratio among all samples with redshift coverage, not simply nearest distance
        candidates=[]
        if np.isfinite(x).all():
            for zmin,zmax,sample,gg,tree in void_groups:
                if zmin <= z <= zmax:
                    d, idx = tree.query(x, k=1)
                    radius=float(gg.iloc[int(idx)]['void_radius_mpc_h'])
                    ratio=float(d/radius) if radius>0 else np.nan
                    candidates.append((ratio, float(d), radius, gg.iloc[int(idx)]))
        if candidates:
            candidates=[c for c in candidates if np.isfinite(c[0])]
            if candidates:
                ratio,d,radius,nv=min(candidates, key=lambda t:t[0])
                void_distance=d; void_radius=radius; void_ratio=ratio; nearest_void_id=nv['void_id']; nearest_void_sample=nv['void_sample']
                if ratio <= 1.0: void_label='void'
                elif ratio <= 1.25: void_label='near_void_edge'
                else: void_label='not_void'
        filament_label='outside_filament_catalog_redshift'; fdist=np.nan; fid=''; fpid=''
        if np.isfinite(x).all() and 0.009 <= z <= 0.2:
            fdist, fi = ftree.query(x, k=1)
            nf=fil.iloc[int(fi)]; fid=int(nf['filament_id']); fpid=int(nf['filament_point_id'])
            if fdist <= 0.5: filament_label='filament'
            elif fdist <= 1.0: filament_label='near_filament'
            else: filament_label='field_or_wall'
        if void_label in ('void','near_void_edge'): final=void_label
        elif filament_label in ('filament','near_filament','field_or_wall'): final=filament_label
        elif void_label == 'not_void': final='sdss_nonvoid'
        else: final='outside_catalog_coverage'
        rows.append({**base, 'environment_label':final, 'void_label':void_label, 'filament_label':filament_label, 'nearest_void_id':nearest_void_id, 'nearest_void_sample':nearest_void_sample, 'nearest_void_distance_mpc_h':void_distance, 'nearest_void_radius_mpc_h':void_radius, 'void_distance_over_radius':void_ratio, 'nearest_filament_id':fid, 'nearest_filament_point_id':fpid, 'nearest_filament_distance_mpc_h':fdist, 'coverage_flag':'derived_crossmatch' if final!='outside_catalog_coverage' else 'outside_catalog_coverage', 'notes':'Derived void+filament cross-match; preliminary, not official Pantheon+ metadata.'})
    return pd.DataFrame(rows)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--pantheon', required=True); ap.add_argument('--void-catalog-dir', required=True); ap.add_argument('--filament-catalog-dir', required=True); ap.add_argument('--output', required=True); args=ap.parse_args()
    sn=read_pantheon(Path(args.pantheon)); print('SN rows', len(sn))
    voids=load_voids(Path(args.void_catalog_dir)); print('void centers', len(voids))
    fil=load_filaments(Path(args.filament_catalog_dir)); print('filament points', len(fil))
    labels=classify(sn, voids, fil)
    if len(labels)!=len(sn): raise RuntimeError('row mismatch')
    if not labels['row_index'].equals(pd.Series(range(len(labels)))): raise RuntimeError('index mismatch')
    Path(args.output).parent.mkdir(parents=True,exist_ok=True); labels.to_csv(args.output,index=False)
    print(labels['environment_label'].value_counts(dropna=False).to_string())
    print(labels['coverage_flag'].value_counts(dropna=False).to_string())
if __name__=='__main__': main()
