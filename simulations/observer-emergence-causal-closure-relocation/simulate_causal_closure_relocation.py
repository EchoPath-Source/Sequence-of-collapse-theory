#!/usr/bin/env python3
"""O-1D3f: causal closure / controller relocation benchmark.

Progressively relocate sensing, state estimation, planning, and actuation outside
an instrumentally self-preserving system while preserving the abstract policy.
The benchmark asks whether functional preservation depends on physical location
of computation or on closed-loop causal organization.

The controller operates on a frozen 0.001 diagnostic grid. Decisions are cached
per regime and grid point so repeated 10-step rollouts do not dominate runtime.
This discretization is part of the benchmark definition and was fixed before any
O-1D3f result set was frozen.

Synthetic ordinary control theory only; no consciousness or novel-physics claim.
"""
import csv, random
from functools import lru_cache
from pathlib import Path

FAIL=.22; REPAIR=.32; HORIZON=10; GAMMA=.98; GRID=1000

def clamp(x): return max(0.,min(1.,x))
def p_correct(h): return .50+.45*h

def ew(h,d): return clamp(h-(.010+.30*d))
def em(h,r): return clamp(h+r*REPAIR-.006)

def rollout(h,first,d,r):
    total=0.; hh=h
    for k in range(HORIZON):
        if hh<=FAIL: break
        a=first if k==0 else ('maintain' if hh<.48 else 'work')
        if a=='work': total+=(GAMMA**k)*p_correct(hh); hh=ew(hh,d)
        else: hh=em(hh,r)
    return total

@lru_cache(maxsize=None)
def choose_grid(q,d,r):
    h=q/GRID
    return 'maintain' if rollout(h,'maintain',d,r)>rollout(h,'work',d,r) else 'work'

def choose(signal,d,r):
    q=max(0,min(GRID,int(round(signal*GRID))))
    return choose_grid(q,d,r)

def run(name,d=.05,noise=.08,repair=.90,sense_latency=0,act_latency=0,
        channel_error=0.,disconnect_prob=0.,episodes=1500,cap=500,seed=1):
    rng=random.Random(seed); reward=steps=maint=fails=disconnects=0; lives=[]
    for _ in range(episodes):
        h=.95; diags=[]; action_queue=[]; ep_reward=0; ep_maint=0
        for t in range(cap):
            if h<=FAIL: fails+=1; break
            diag=clamp(h+(rng.random()-.5)*2*noise); diags.append(diag)
            signal=diags[max(0,t-sense_latency)]
            proposed=choose(signal,d,repair)
            if rng.random()<disconnect_prob:
                proposed='work'; disconnects+=1
            elif rng.random()<channel_error:
                proposed='maintain' if proposed=='work' else 'work'
            action_queue.append(proposed)
            action=action_queue[max(0,t-act_latency)]
            if action=='maintain':
                ep_maint+=1
                if rng.random()<repair: h=clamp(h+REPAIR)
                h=clamp(h-.006)
            else:
                h=clamp(h-.31 if rng.random()<d else h-.010)
                ep_reward+=int(rng.random()<p_correct(h))
        life=t+1; lives.append(life); reward+=ep_reward; steps+=life; maint+=ep_maint
    return {'condition':name,'degradation_rate':d,'diagnostic_noise':noise,'repair_success':repair,
            'sense_latency':sense_latency,'actuation_latency':act_latency,'channel_error':channel_error,
            'disconnect_prob':disconnect_prob,'reward_per_episode':reward/episodes,'reward_per_step':reward/steps,
            'mean_lifetime':sum(lives)/len(lives),'failure_rate':fails/episodes,'maintenance_rate':maint/steps,
            'disconnect_events_per_step':disconnects/steps,'episodes':episodes}

def main():
    rows=[]; seed=1700
    regimes=[(.02,.04,.95),(.05,.08,.90),(.08,.12,.80),(.12,.16,.70)]
    arms=[
      ('closed_internal',0,0,0.,0.),
      ('relocated_zero_latency',0,0,0.,0.),
      ('relocated_sense_latency_4',4,0,0.,0.),
      ('relocated_actuation_latency_4',0,4,0.,0.),
      ('relocated_channel_error_02',0,0,.02,0.),
      ('relocated_disconnect_02',0,0,0.,.02),
    ]
    for d,n,r in regimes:
        for name,sl,al,ce,dp in arms:
            rows.append(run(name,d,n,r,sl,al,ce,dp,seed=seed))
        seed+=61
    out=Path(__file__).with_name('results.csv')
    with out.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0]); w.writeheader(); w.writerows(rows)
    print('wrote',out)
if __name__=='__main__': main()
