#!/usr/bin/env python3
"""Simulation 4f: sham histories, negative controls, and sensitivity analysis.

Purpose: formalize rejection rules for a history-dependent residual. Synthetic
study only. No empirical or SoCT detection claim is made.
"""

import csv, math, random
from pathlib import Path


def inv(a):
    n=len(a); aug=[r[:] + [1.0 if i==j else 0.0 for j in range(n)] for i,r in enumerate(a)]
    for c in range(n):
        p=max(range(c,n), key=lambda r: abs(aug[r][c])); aug[c],aug[p]=aug[p],aug[c]
        v=aug[c][c]
        if abs(v)<1e-14: raise ValueError('singular')
        aug[c]=[x/v for x in aug[c]]
        for r in range(n):
            if r==c: continue
            f=aug[r][c]; aug[r]=[aug[r][j]-f*aug[c][j] for j in range(2*n)]
    return [r[n:] for r in aug]


def fit(x,y):
    p=len(x[0]); xtx=[[sum(r[i]*r[j] for r in x) for j in range(p)] for i in range(p)]
    xty=[sum(r[i]*yy for r,yy in zip(x,y)) for i in range(p)]
    ii=inv(xtx); b=[sum(ii[i][j]*xty[j] for j in range(p)) for i in range(p)]
    e=[yy-sum(r[i]*b[i] for i in range(p)) for r,yy in zip(x,y)]
    s2=sum(v*v for v in e)/max(1,len(y)-p)
    se=[math.sqrt(max(0,s2*ii[i][i])) for i in range(p)]
    return b,se


def basis(beta=.25,t=4.0): return (1-math.exp(-beta*t))/beta


def trial(seed, hidden_strength=0.0, measurement_sigma=0.05, n=1500):
    rng=random.Random(seed); fm=basis(); x=[]; y=[]
    for i in range(n):
        d=rng.choice([0,0.5,1.0]); h=(rng.choice([-1,1])*d) if d else 0.0
        sd=rng.choice([0,0.5,1.0]); sham=(rng.choice([-1,1])*sd) if sd else 0.0
        neg=rng.choice([-1,1]); order=(i-(n-1)/2)/n
        heat=.7*h+.6*sham+rng.gauss(0,.2)
        coh=.4*h+.3*sham+rng.gauss(0,.15)
        pulse=1.1*h+1.0*sham+rng.gauss(0,.25)
        hidden=.65*h+.60*sham+rng.gauss(0,.22)
        hm=heat+rng.gauss(0,measurement_sigma); cm=coh+rng.gauss(0,measurement_sigma); pm=pulse+rng.gauss(0,measurement_sigma)
        out=.01+.012*order+.025*heat-.018*coh+.008*pulse+hidden_strength*hidden+rng.gauss(0,.02)
        x.append([1,order,h*fm,sham*fm,neg,hm,cm,pm]); y.append(out)
    b,se=fit(x,y)
    return b[2],se[2],b[2]/se[2],b[3]/se[3],b[4]/se[4]


def main():
    out=Path(__file__).with_name('results.csv')
    rows=[]
    for hidden in [0.0,0.003,0.006,0.012]:
        vals=[trial(5000+i,hidden) for i in range(200)]
        fp=sum(abs(v[2])>=3 for v in vals)/len(vals)
        sham=sum(abs(v[3])>=3 for v in vals)/len(vals)
        neg=sum(abs(v[4])>=3 for v in vals)/len(vals)
        lam_sorted=sorted(v[0] for v in vals); med=lam_sorted[len(lam_sorted)//2]
        rows.append({'hidden_strength':hidden,'history_false_positive_rate_abs_z_ge_3':fp,'sham_flag_rate_abs_z_ge_3':sham,'negative_control_flag_rate_abs_z_ge_3':neg,'median_history_lambda_fit':med,'replicates':len(vals)})
    with out.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    print(f'wrote {out}')

if __name__=='__main__': main()
