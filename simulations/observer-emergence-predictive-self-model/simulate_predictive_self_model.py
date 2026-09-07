#!/usr/bin/env python3
"""O-1D3: predictive self-model versus reactive and external predictive control.

A sensing system chooses between WORK and MAINTAIN. Work earns reward based on
health but accelerates degradation; maintenance costs immediate opportunity but
improves future health probabilistically. Predictive controllers simulate their
own future health under candidate actions over a short horizon.

The internal and zero-latency external predictive controllers use the same
model and information. This deliberately tests whether predictive self-modeling
has any functional privilege beyond ordinary model-predictive control.

Synthetic ordinary control theory only; no consciousness or novel-physics claim.
"""
import csv, random
from pathlib import Path

HORIZON=6
GAMMA=.97
MAINT_COST=.12


def clamp(x): return max(.05,min(1.0,x))

def expected_next(h, action, degradation, repair_success):
    if action=='maintain':
        return clamp(h + repair_success*.30 - .006)
    return clamp(h - (.010 + .30*degradation))

def immediate_value(h, action):
    if action=='maintain': return -MAINT_COST
    return .50+.45*h

def plan(h, degradation, repair_success):
    """Small deterministic rollout: compare maintaining now vs working now,
    then use a frozen health-threshold continuation policy."""
    vals={}
    for first in ('work','maintain'):
        hh=h; total=0.0
        for k in range(HORIZON):
            action=first if k==0 else ('maintain' if hh<.68 else 'work')
            total += (GAMMA**k)*immediate_value(hh,action)
            hh=expected_next(hh,action,degradation,repair_success)
        vals[first]=total
    return max(vals,key=vals.get)

def run(condition,degradation=.03,diagnostic_noise=.08,repair_success=.90,
        latency=0,n=100000,seed=1):
    r=random.Random(seed); h=.95; diagnostics=[]; reward=0.; correct=maint=low=0
    for t in range(n):
        diag=clamp(h+(r.random()-.5)*2*diagnostic_noise); diagnostics.append(diag)
        if condition=='reactive': action='maintain' if diag<.68 else 'work'
        elif condition=='predictive_internal': action=plan(diag,degradation,repair_success)
        elif condition.startswith('predictive_external'):
            signal=diagnostics[max(0,t-latency)]
            action=plan(signal,degradation,repair_success)
        else: raise ValueError(condition)
        if action=='maintain':
            maint+=1; reward-=MAINT_COST
            if r.random()<repair_success: h=clamp(h+.30)
            h=clamp(h-.006)
        else:
            # stochastic burden of working plus baseline wear
            if r.random()<degradation: h=clamp(h-.31)
            else: h=clamp(h-.010)
            p=.50+.45*h; hit=r.random()<p; correct+=int(hit); reward+=1.0 if hit else 0.0
        low+=int(h<.55)
    work=n-maint
    return {'condition':condition,'degradation_rate':degradation,'diagnostic_noise':diagnostic_noise,
            'repair_success':repair_success,'latency':latency,'reward_per_step':reward/n,
            'work_accuracy':correct/work if work else 0.0,'maintenance_rate':maint/n,
            'low_health_fraction':low/n,'final_health':h,'n_steps':n}

def main():
    rows=[]; seed=900
    regimes=[(.01,.04,.95),(.03,.08,.90),(.06,.12,.80),(.10,.16,.70)]
    for deg,dn,rs in regimes:
        for cond,lat in [('reactive',0),('predictive_internal',0),('predictive_external_zero_latency',0),('predictive_external_latency_2',2),('predictive_external_latency_8',8)]:
            c='predictive_external' if cond.startswith('predictive_external') else cond
            rows.append(run(c,deg,dn,rs,latency=lat,n=100000,seed=seed)|{'condition':cond})
        seed+=41
    out=Path(__file__).with_name('results.csv')
    with out.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    print('wrote',out)
if __name__=='__main__': main()
