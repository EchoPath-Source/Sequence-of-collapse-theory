#!/usr/bin/env python3
"""CTI-00B SPARC specification-curve audit.

Purpose
-------
Quantify how the age -> outer-fDM association changes across defensible,
pre-existing analysis choices before SPARC is used as a cross-track anchor.

This is a robustness audit, not a search for the most significant model.
No specification is promoted to canonical based on this script's output.
"""
from pathlib import Path
import json
import numpy as np
import pandas as pd
from scipy import stats

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data/sparc/sparc_age_fdm_data.csv"
OUT = ROOT / "observations/sparc/results/cti00b"
SEED = 20260922
N_BOOT = 5000

def residual_effect(df, predictor, outcome, controls):
    cols=[predictor,outcome]+controls
    d=df.dropna(subset=cols).copy()
    x=d[predictor].to_numpy(float); y=d[outcome].to_numpy(float)
    if controls:
        Z=np.column_stack([np.ones(len(d))]+[d[c].to_numpy(float) for c in controls])
        bx=np.linalg.lstsq(Z,x,rcond=None)[0]; by=np.linalg.lstsq(Z,y,rcond=None)[0]
        x=x-Z@bx; y=y-Z@by
    r,p=stats.pearsonr(x,y)
    sx=np.std(x,ddof=1); sy=np.std(y,ddof=1)
    beta_std=r
    return len(d),r,p,beta_std

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    df=pd.read_csv(DATA)
    for c in ["fdm_outer_mean","age_best","age_combined_proxy","age_literature","Vmax_kms","Rmax_kpc","SB0_disk_Lpc2"]:
        df[c]=pd.to_numeric(df[c],errors="coerce")
    df["logVmax"]=np.log10(df["Vmax_kms"])
    df["logRmax"]=np.log10(df["Rmax_kpc"])
    df["logSB0"]=np.log10(df["SB0_disk_Lpc2"])
    df["logKinMass"]=np.log10(df["Vmax_kms"]**2*df["Rmax_kpc"])
    df["logPhotMass"]=np.log10(df["SB0_disk_Lpc2"]*df["Rmax_kpc"]**2)
    df["logCombinedMass"]=0.5*(df["logKinMass"]+df["logPhotMass"])

    # All entries are motivated by analysis choices already represented in the repo.
    specs=[
      ("S01","age_best","none",[],"current primary unadjusted"),
      ("S02","age_best","Vmax",["logVmax"],"existing Vmax control"),
      ("S03","age_best","Rmax",["logRmax"],"existing Rmax control"),
      ("S04","age_best","SB0",["logSB0"],"existing surface-brightness control"),
      ("S05","age_best","Vmax+Rmax",["logVmax","logRmax"],"existing two-control model"),
      ("S06","age_best","Vmax+Rmax+SB0",["logVmax","logRmax","logSB0"],"existing maximal committed control set"),
      ("S07","age_best","kinematic mass proxy",["logKinMass"],"existing mass-proxy family"),
      ("S08","age_best","photometric mass proxy",["logPhotMass"],"existing mass-proxy family"),
      ("S09","age_best","combined mass proxy",["logCombinedMass"],"existing mass-proxy family"),
      ("S10","age_combined_proxy","none",[],"documented alternative age proxy; sensitivity only"),
      ("S11","age_combined_proxy","combined mass proxy",["logCombinedMass"],"alternative age proxy + mass control"),
      ("S12","age_literature","none",[],"literature-age subset; small-N sensitivity"),
      ("S13","age_literature","combined mass proxy",["logCombinedMass"],"literature-age subset + mass control"),
    ]

    rows=[]
    for sid,pred,label,controls,rationale in specs:
        n,r,p,b=residual_effect(df,pred,"fdm_outer_mean",controls)
        rows.append(dict(spec_id=sid,predictor=pred,control_family=label,controls="+".join(controls) or "none",
                         n=n,effect_r=r,standardized_effect=b,p_value=p,sign=np.sign(r),
                         rationale=rationale,status="candidate_defensible"))

    out=pd.DataFrame(rows)
    canonical_sign=np.sign(out.loc[out.spec_id=="S01","effect_r"].iloc[0])
    out["same_sign_as_S01"]=out["sign"]==canonical_sign

    def xorshift32(seed):
        s = seed & 0xffffffff
        while True:
            s ^= (s << 13) & 0xffffffff
            s ^= (s >> 17)
            s ^= (s << 5) & 0xffffffff
            yield (s & 0xffffffff) / 4294967296.0

    boot=[]
    for _,s in out.iterrows():
        sid=s.spec_id
        spec=next(x for x in specs if x[0]==sid)
        _,pred,_,controls,_=spec
        d=df.dropna(subset=[pred,"fdm_outer_mean"]+controls).copy().reset_index(drop=True)
        vals=[]
        rng=xorshift32(SEED + int(sid[1:]))
        for _ in range(N_BOOT):
            idx=[int(next(rng)*len(d)) for _ in range(len(d))]
            sample=d.iloc[idx]
            try:
                _,r,_,_=residual_effect(sample,pred,"fdm_outer_mean",controls); vals.append(r)
            except Exception:
                pass
        boot.append(dict(spec_id=sid,n_boot=len(vals),ci_low=np.quantile(vals,.025),ci_high=np.quantile(vals,.975),
                         boot_median=np.median(vals),fraction_positive=np.mean(np.array(vals)>0)))
    boot=pd.DataFrame(boot)
    out=out.merge(boot,on="spec_id")
    out.to_csv(OUT/"specification_curve.csv",index=False)

    comparable=out[out.predictor=="age_best"]
    summary={
      "seed":SEED,"n_boot":N_BOOT,"n_specifications":int(len(out)),
      "n_primary_age_best_specs":int(len(comparable)),
      "median_effect_primary_age_best":float(comparable.effect_r.median()),
      "min_effect_primary_age_best":float(comparable.effect_r.min()),
      "max_effect_primary_age_best":float(comparable.effect_r.max()),
      "fraction_same_sign_primary_age_best":float(comparable.same_sign_as_S01.mean()),
      "q05_effect_primary_age_best":float(comparable.effect_r.quantile(.05)),
      "q95_effect_primary_age_best":float(comparable.effect_r.quantile(.95)),
      "decision":"NOT_AUTOMATICALLY_CLASSIFIED",
      "reason":"CTI-00B forbids inventing a numerical stability threshold before the common estimand/error model and decision rule are frozen."
    }
    (OUT/"summary.json").write_text(json.dumps(summary,indent=2)+"\n")
    print(out.to_string(index=False))
    print(json.dumps(summary,indent=2))

if __name__=="__main__":
    main()
