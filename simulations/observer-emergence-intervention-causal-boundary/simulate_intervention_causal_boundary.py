#!/usr/bin/env python3
"""O-1D3g: intervention-defined causal boundary.

Tests whether a persistent regulation loop is better characterized by intervention
sensitivity and recoverability than by the spatial location of computation.

Synthetic ordinary control theory only; no consciousness or novel-physics claim.
"""
import csv, random
from pathlib import Path

FAIL=.22
REPAIR=.32
HORIZON=10
GAMMA=.98
INTERVENTION_T=200
LEDGER_N=20
EST_ALPHA=.20


def clamp(x): return max(0., min(1., x))
def p_correct(h): return .50 + .45*h
def ew(h,d): return clamp(h-(.010+.30*d))
def em(h,r): return clamp(h+r*REPAIR-.006)

def rollout(h, first, d, r):
    total=0.; hh=h
    for k in range(HORIZON):
        if hh<=FAIL: break
        a=first if k==0 else ('maintain' if hh<.48 else 'work')
        if a=='work':
            total += (GAMMA**k)*p_correct(hh)
            hh=ew(hh,d)
        else:
            hh=em(hh,r)
    return total

def choose(hhat,d,r):
    return 'maintain' if rollout(hhat,'maintain',d,r)>rollout(hhat,'work',d,r) else 'work'

def run(name,d=.08,noise=.12,repair=.80,episodes=300,cap=500,seed=1):
    rng=random.Random(seed)
    total_reward=post_reward=steps=maint=failures=0
    recovery_times=[]
    for _ in range(episodes):
        h=.95; hhat=.95; ledger=[]; stale=[]; recovered=None
        ep_reward=ep_post=ep_maint=0
        for t in range(cap):
            if h<=FAIL:
                failures+=1
                break
            diag=clamp(h+(rng.random()-.5)*2*noise)
            ledger.append(diag)
            if len(ledger)>LEDGER_N: ledger.pop(0)
            if t<LEDGER_N: stale.append(diag)
            hhat=(1-EST_ALPHA)*hhat+EST_ALPHA*diag

            if t==INTERVENTION_T and name in (
                'estimator_reset','reset_with_reconstruction','reset_with_stale_reconstruction'):
                hhat=.95
                if name=='reset_with_reconstruction' and ledger:
                    hhat=sum(ledger)/len(ledger)
                elif name=='reset_with_stale_reconstruction' and stale:
                    hhat=sum(stale)/len(stale)

            action=choose(hhat,d,repair)

            if name=='action_channel_intervention' and INTERVENTION_T <= t < INTERVENTION_T+20:
                action='maintain' if action=='work' else 'work'

            if name=='state_estimator_replacement' and INTERVENTION_T <= t < INTERVENTION_T+20:
                # Replace the operative self-state with a fixed healthy-state surrogate.
                action=choose(.95,d,repair)

            if t>=INTERVENTION_T and recovered is None and abs(hhat-h)<.08:
                recovered=t-INTERVENTION_T

            if action=='maintain':
                ep_maint+=1
                if rng.random()<repair: h=clamp(h+REPAIR)
                h=clamp(h-.006)
            else:
                h=clamp(h-.31 if rng.random()<d else h-.010)
                hit=int(rng.random()<p_correct(h))
                ep_reward+=hit
                if t>=INTERVENTION_T: ep_post+=hit

        life=t+1
        total_reward+=ep_reward
        post_reward+=ep_post
        steps+=life
        maint+=ep_maint
        if recovered is not None: recovery_times.append(recovered)

    return {
        'condition':name,'degradation_rate':d,
        'reward_per_episode':total_reward/episodes,
        'post_reward_per_episode':post_reward/episodes,
        'mean_lifetime':steps/episodes,
        'failure_rate':failures/episodes,
        'maintenance_rate':maint/steps,
        'mean_recovery_steps':sum(recovery_times)/len(recovery_times) if recovery_times else -1,
        'recovery_fraction':len(recovery_times)/episodes,
        'episodes':episodes,
    }

def main():
    arms=[
        'intact_internal',
        'external_zero_latency',
        'estimator_reset',
        'reset_with_reconstruction',
        'reset_with_stale_reconstruction',
        'state_estimator_replacement',
        'action_channel_intervention',
    ]
    regimes=[(.05,.08,.90),(.08,.12,.80),(.12,.16,.70)]
    rows=[]; seed=2100
    for d,n,r in regimes:
        for arm in arms:
            rows.append(run(arm,d,n,r,seed=seed))
        seed+=73
    out=Path(__file__).with_name('results.csv')
    with out.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0]); w.writeheader(); w.writerows(rows)
    print('wrote',out)

if __name__=='__main__': main()
