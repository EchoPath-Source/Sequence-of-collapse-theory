#!/usr/bin/env python3
"""O-1D2: self-regulation versus externally informed regulation.

Ordinary stochastic control benchmark. A sensing system degrades and can be
maintained. Compare: (1) internal self-state controller, (2) external controller
with the same diagnostic information and zero latency, (3) external controller
with latency, and (4) shuffled diagnostic control. Maintenance budgets are
matched by threshold calibration. No consciousness or novel-physics claim.
"""
import csv, random
from pathlib import Path


def generate_noise(n, seed):
    r=random.Random(seed)
    return [(r.random(),r.random(),r.random(),r.random()) for _ in range(n)]


def run(condition, degradation=.03, n=100000, seed=1, latency=0,
        diagnostic_noise=.08, repair_success=.90, threshold=.72):
    noise=generate_noise(n,seed); health=.95; history=[health];
    correct=maint=low=0; util=0.0; diagnostics=[]
    for t,(u_deg,u_diag,u_rep,u_obs) in enumerate(noise):
        health=max(.05,health-(.025 if u_deg<degradation else .002))
        diag=max(0,min(1,health+(u_diag-.5)*2*diagnostic_noise))
        diagnostics.append(diag)
        if condition=='internal': signal=diag
        elif condition.startswith('external'):
            idx=max(0,t-latency); signal=diagnostics[idx]
        elif condition=='shuffled':
            # deterministic placebo signal independent of current health
            signal=((t*1103515245+seed)%10000)/10000
        else: raise ValueError(condition)
        do_maint=signal<threshold
        if do_maint:
            maint+=1
            if u_rep<repair_success: health=min(1.0,health+.35)
            util-=.04
        acc=.50+.45*health
        hit=u_obs<acc; correct+=int(hit); util+=1.0 if hit else 0.0
        low+=int(health<.55); history.append(health)
    return {'condition':condition,'degradation_rate':degradation,'latency':latency,
            'diagnostic_noise':diagnostic_noise,'repair_success':repair_success,
            'accuracy':correct/n,'utility_per_step':util/n,'mean_health':sum(history)/len(history),
            'low_health_fraction':low/n,'maintenance_rate':maint/n,'n_steps':n}


def main():
    rows=[]; seed=700
    # Fixed policy across held-out degradation/noise/repair regimes.
    regimes=[(.01,.04,.95),(.03,.08,.90),(.06,.12,.80),(.10,.16,.70)]
    for deg,dn,rs in regimes:
        for cond,lat in [('internal',0),('external_zero_latency',0),('external_latency_2',2),('external_latency_8',8),('shuffled',0)]:
            rows.append(run('external' if cond.startswith('external') else cond,
                            degradation=deg,diagnostic_noise=dn,repair_success=rs,
                            latency=lat,seed=seed) | {'condition':cond})
        seed+=31
    out=Path(__file__).with_name('results.csv')
    with out.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    print('wrote',out)
if __name__=='__main__': main()
