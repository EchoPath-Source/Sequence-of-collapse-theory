"""P6 outcome-blind CF4 reported-error audit; no DM or velocity-residual fields."""
import argparse
from pathlib import Path
import numpy as np
import pandas as pd
from coverage_overlap import load_mask, covered, geometry, classify, positions, C

METHODS={'groups':['av','fp','tf','snIa','sbfo','sbfi','snII','zp'],
         'galaxies':['','fp','tf','snIa','sbf','snII','trgb','ceph','mas']}

def optimistic_mde(errors):
    e=np.asarray(errors,float)
    if not len(e) or not np.all(np.isfinite(e)&(e>0)):raise ValueError('positive finite errors required')
    se=1/np.sqrt(np.sum(e**-2))
    return se,70*np.expm1(np.log(10)/5*2.8016*se)

def audit(root,mask_paths):
    mask=load_mask(mask_paths);parts=geometry(root);parent={}
    for name,methods in METHODS.items():
        group=name=='groups';key='1PGC' if group else 'PGC'
        errs=['e_DM'+x for x in methods]
        counts=['o_DM'+x for x in ['cal','fp','tf','snIa','sbfo','sbfi']] if group else []
        cols=list(dict.fromkeys([key,'1PGC','RAJ2000','DEJ2000','Vcmb']+errs+counts+(['Ngal'] if group else [])))
        d=pd.read_csv(root/'cosmicflows4'/f'cf4_{name}.tsv',sep='\t',comment='#',usecols=cols,dtype=str).iloc[2:].apply(pd.to_numeric,errors='coerce')
        if d[key].isna().any() or not d[key].is_unique:raise ValueError('invalid IDs')
        parent[name]=set(d['1PGC'].dropna())
        z=d.Vcmb/C
        sub=d[z.between(.01,.15)&d.RAJ2000.between(0,360,inclusive='left')&d.DEJ2000.between(-90,90)].copy()
        sub['z']=sub.Vcmb/C
        s=sub[covered(mask,sub.RAJ2000,sub.DEJ2000)].copy()
        def match(dv):
            return [classify(parts,p) for p in positions(s.RAJ2000,s.DEJ2000,s.z+dv/C)]
        h=match(0);interior=np.array([label=='interior' for label,_ in h])
        stable=interior.copy()
        for dv in (-300,300):stable &= np.array([a==b for a,b in zip(h,match(dv))])
        print(name,'total/window/covered/interior/stable',len(d),len(sub),len(s),interior.sum(),stable.sum())
        for label,t in [('window',sub),('covered',s),('interior',s[interior]),('stable',s[stable])]:
            print(label,'rows',len(t),'parent IDs',t['1PGC'].nunique())
            for col in errs:
                x=t[col];v=x[np.isfinite(x)&(x>0)]
                print(col,len(v),v.quantile([.1,.5,.9]).round(3).tolist())
            if group:
                print('positive count fields',{c:int((t[c]>0).sum()) for c in counts})
                if label in ('interior','stable'):
                    print('optimistic FP MDE',optimistic_mde(t.e_DMfp))
    print('missing group parents',sorted(parent['galaxies']-parent['groups']))
    print('NO distance outcome analysis')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('root',type=Path);p.add_argument('mask_parts',type=Path,nargs=3);a=p.parse_args();audit(a.root,a.mask_parts)
