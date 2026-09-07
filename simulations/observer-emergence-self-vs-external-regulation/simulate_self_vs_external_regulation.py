#!/usr/bin/env python3
"""O-1D2: self-regulation versus externally informed regulation.

Ordinary stochastic control benchmark. A sensing system degrades and can be
maintained. Compare: (1) internal self-state controller, (2) external controller
with the same diagnostic information and zero latency, (3) delayed external
controllers, and (4) a placebo/shuffled diagnostic control.

Maintenance rates are explicitly budget-matched within each regime. No
consciousness or novel-physics claim is made.
"""
import csv, random
from pathlib import Path


def generate_noise(n, seed):
    r=random.Random(seed)
    return [(r.random(),r.random(),r.random(),r.random(),r.random()) for _ in range(n)]


def run(condition, degradation=.03, n=100000, seed=1, latency=0,
        diagnostic_noise=.08, repair_success=.90, threshold=.72):
    noise=generate_noise(n,seed); health=.95; history=[health]
    correct=maint=low=0; util=0.0; diagnostics=[]
    for t,(u_deg,u_diag,u_rep,u_obs,u_placebo) in enumerate(noise):
        health=max(.05,health-(.025 if u_deg<degradation else .002))
        diag=max(0,min(1,health+(u_diag-.5)*2*diagnostic_noise))
        diagnostics.append(diag)
        if condition=='internal':
            signal=diag
        elif condition=='external':
            idx=max(0,t-latency); signal=diagnostics[idx]
        elif condition=='shuffled':
            signal=u_placebo
        else:
            raise ValueError(condition)
        do_maint=signal<threshold
        if do_maint:
            maint+=1
            if u_rep<repair_success:
                health=min(1.0,health+.35)
            util-=.04
        acc=.50+.45*health
        hit=u_obs<acc; correct+=int(hit); util+=1.0 if hit else 0.0
        low+=int(health<.55); history.append(health)
    return {'accuracy':correct/n,'utility_per_step':util/n,
            'mean_health':sum(history)/len(history),
            'low_health_fraction':low/n,'maintenance_rate':maint/n}


def calibrate_threshold(condition,target_rate,degradation,diagnostic_noise,
                        repair_success,seed,latency=0):
    lo,hi=0.0,1.0; best=(0.5,1.0)
    for _ in range(24):
        mid=(lo+hi)/2
        rr=run(condition,degradation=degradation,diagnostic_noise=diagnostic_noise,
               repair_success=repair_success,seed=seed,latency=latency,threshold=mid)
        diff=rr['maintenance_rate']-target_rate
        if abs(diff)<best[1]: best=(mid,abs(diff))
        if diff<0: lo=mid
        else: hi=mid
    return best[0]


def main():
    rows=[]; seed=700
    regimes=[(.01,.04,.95),(.03,.08,.90),(.06,.12,.80),(.10,.16,.70)]
    for deg,dn,rs in regimes:
        internal=run('internal',degradation=deg,diagnostic_noise=dn,
                     repair_success=rs,seed=seed,threshold=.72)
        target=internal['maintenance_rate']
        conditions=[('internal','internal',0),
                    ('external_zero_latency','external',0),
                    ('external_latency_2','external',2),
                    ('external_latency_8','external',8),
                    ('shuffled','shuffled',0)]
        for name,kind,lat in conditions:
            if name in ('internal','external_zero_latency'):
                threshold=.72
            else:
                threshold=calibrate_threshold(kind,target,deg,dn,rs,seed,lat)
            rr=run(kind,degradation=deg,diagnostic_noise=dn,
                   repair_success=rs,seed=seed,latency=lat,threshold=threshold)
            rows.append({'condition':name,'degradation_rate':deg,'latency':lat,
                         'diagnostic_noise':dn,'repair_success':rs,
                         'threshold_used':threshold,**rr})
        seed+=31
    out=Path(__file__).with_name('results.csv')
    with out.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    print('wrote',out)

if __name__=='__main__': main()
