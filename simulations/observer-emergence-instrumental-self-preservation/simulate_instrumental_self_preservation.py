#!/usr/bin/env python3
"""O-1D3e: instrumental self-preservation under a continuation constraint.

No direct reward is assigned to health. The agent earns reward only by successful
WORK actions. If internal health crosses a failure boundary, the episode ends and
all future reward opportunities are lost. MAINTAIN has an immediate opportunity
cost but can restore health. This tests whether preservation emerges instrumentally
from continuation value rather than from an explicit self-preservation objective.

Synthetic ordinary control theory only. No consciousness or novel-physics claim.
"""
import csv, random
from pathlib import Path

FAIL=0.22
REPAIR=0.32
MAINT_COST=0.0  # opportunity cost already arises from giving up a work step
HORIZON=10
GAMMA=.98


def clamp(x): return max(.0,min(1.0,x))

def p_correct(h): return .50+.45*h

def expected_health_after_work(h, degradation):
    return clamp(h - (.010 + .30*degradation))

def expected_health_after_maint(h, repair_success):
    return clamp(h + repair_success*REPAIR - .006)

def rollout_value(h, first_action, degradation, repair_success):
    """Deterministic continuation-value approximation with no direct health reward."""
    hh=h; total=0.0
    for k in range(HORIZON):
        if hh<=FAIL: break
        action=first_action if k==0 else ('maintain' if hh<.48 else 'work')
        if action=='work':
            total += (GAMMA**k)*p_correct(hh)
            hh=expected_health_after_work(hh,degradation)
        else:
            hh=expected_health_after_maint(hh,repair_success)
    return total

def policy(condition, signal, degradation, repair_success):
    if condition=='myopic':
        return 'work'
    if condition=='threshold':
        return 'maintain' if signal<.48 else 'work'
    if condition in ('continuation_internal','continuation_external'):
        vw=rollout_value(signal,'work',degradation,repair_success)
        vm=rollout_value(signal,'maintain',degradation,repair_success)
        return 'maintain' if vm>vw else 'work'
    raise ValueError(condition)

def run(condition,degradation=.05,diagnostic_noise=.08,repair_success=.90,
        latency=0,n_episodes=1500,episode_cap=500,seed=1):
    r=random.Random(seed)
    total_reward=total_steps=total_maint=failures=0
    lifetimes=[]
    for ep in range(n_episodes):
        h=.95; diagnostics=[]; ep_reward=0; ep_maint=0
        for t in range(episode_cap):
            if h<=FAIL:
                failures+=1; break
            diag=clamp(h+(r.random()-.5)*2*diagnostic_noise); diagnostics.append(diag)
            if condition=='continuation_external':
                signal=diagnostics[max(0,t-latency)]
            else:
                signal=diag
            action=policy(condition,signal,degradation,repair_success)
            if action=='maintain':
                ep_maint+=1
                if r.random()<repair_success: h=clamp(h+REPAIR)
                h=clamp(h-.006)
            else:
                # Work can produce abrupt stochastic damage plus baseline wear.
                if r.random()<degradation: h=clamp(h-.31)
                else: h=clamp(h-.010)
                ep_reward += 1 if r.random()<p_correct(h) else 0
        life=t+1
        lifetimes.append(life); total_reward+=ep_reward; total_steps+=life; total_maint+=ep_maint
    return {
        'condition':condition,'degradation_rate':degradation,'diagnostic_noise':diagnostic_noise,
        'repair_success':repair_success,'latency':latency,'reward_per_episode':total_reward/n_episodes,
        'reward_per_step':total_reward/total_steps,'mean_lifetime':sum(lifetimes)/len(lifetimes),
        'failure_rate':failures/n_episodes,'maintenance_rate':total_maint/total_steps,
        'n_episodes':n_episodes,'episode_cap':episode_cap
    }

def main():
    rows=[]; seed=1300
    regimes=[(.02,.04,.95),(.05,.08,.90),(.08,.12,.80),(.12,.16,.70)]
    arms=[('myopic',0),('threshold',0),('continuation_internal',0),
          ('continuation_external_zero_latency',0),('continuation_external_latency_4',4)]
    for deg,dn,rs in regimes:
        for name,lat in arms:
            cond='continuation_external' if name.startswith('continuation_external') else name
            rows.append(run(cond,deg,dn,rs,latency=lat,seed=seed)|{'condition':name})
        seed+=53
    out=Path(__file__).with_name('results.csv')
    with out.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    print('wrote',out)
if __name__=='__main__': main()
