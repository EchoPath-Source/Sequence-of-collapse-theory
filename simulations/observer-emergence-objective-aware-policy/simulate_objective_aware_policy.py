#!/usr/bin/env python3
"""O-1D3d: objective-aware policy adaptation under changing self-dynamics.

Synthetic ordinary control benchmark. The system learns an estimate of its own
wear dynamics, but the new question is whether it can also adapt the policy that
maps that model into actions so as to optimize long-horizon value rather than
merely preserve health.

Conditions separate:
- frozen model + frozen value policy
- adaptive model + frozen value policy
- frozen model + adaptive value policy
- adaptive model + adaptive value policy
- matched zero-latency external adaptive controller

No consciousness or novel-physics claim.
"""
import csv, random, math
from pathlib import Path

N=120000
SHIFT=40000
MAINT_COST=.12
GAMMA=.97
HORIZON=8
BASELINE_DEG=.03


def clamp(x,lo=.05,hi=1.0): return max(lo,min(hi,x))


def expected_next(h, action, deg_est, repair=.90):
    if action=='maintain':
        return clamp(h + repair*.30 - .006)
    return clamp(h - (.010 + .30*deg_est))


def rollout_value(h, first, deg_est, health_weight, repair=.90):
    hh=h; total=0.0
    for k in range(HORIZON):
        if k==0:
            a=first
        else:
            # continuation threshold shifts with learned health value
            thresh=.60 + .20*health_weight
            a='maintain' if hh<thresh else 'work'
        if a=='maintain':
            r=-MAINT_COST + health_weight*.04*hh
        else:
            r=(.50+.45*hh) + health_weight*.015*hh
        total += (GAMMA**k)*r
        hh=expected_next(hh,a,deg_est,repair)
    return total


def choose_action(h,deg_est,health_weight,repair=.90):
    vw=rollout_value(h,'work',deg_est,health_weight,repair)
    vm=rollout_value(h,'maintain',deg_est,health_weight,repair)
    return 'maintain' if vm>vw else 'work'


def run(condition, post_deg, diag_noise=.08, repair_success=.90, seed=1):
    r=random.Random(seed); h=.95; reward=0.0; maint=low=correct=work=0
    deg_est=BASELINE_DEG
    health_weight=.25
    # exponential estimates of realized degradation burden and utility consequences
    alpha=.003; beta=.002
    utility_ema=.75; low_ema=0.0
    for t in range(N):
        true_deg=BASELINE_DEG if t<SHIFT else post_deg
        diag=clamp(h+(r.random()-.5)*2*diag_noise)
        adapt_model = condition in ('adaptive_model','joint_adaptive','external_joint')
        adapt_policy = condition in ('adaptive_policy','joint_adaptive','external_joint')
        model_for_policy=deg_est if adapt_model else BASELINE_DEG
        weight_for_policy=health_weight if adapt_policy else .25
        action=choose_action(diag,model_for_policy,weight_for_policy,repair_success)
        pre_h=h
        if action=='maintain':
            maint+=1; reward-=MAINT_COST
            if r.random()<repair_success: h=clamp(h+.30)
            h=clamp(h-.006)
            realized_work_damage=0.0
        else:
            work+=1
            damaged=r.random()<true_deg
            if damaged: h=clamp(h-.31)
            else: h=clamp(h-.010)
            realized_work_damage=1.0 if damaged else 0.0
            p=.50+.45*h; hit=r.random()<p; correct+=int(hit); reward+=1.0 if hit else 0.0
        low_now=1.0 if h<.55 else 0.0
        low+=int(low_now)
        # model update only from work trials, where degradation event is observable in this toy model
        if adapt_model and action=='work':
            deg_est=(1-alpha)*deg_est+alpha*realized_work_damage
        # policy-value adaptation: if low-health occupancy rises while utility falls,
        # increase value of health; if health is ample but utility is suppressed by
        # maintenance opportunity cost, reduce it.
        inst_u=(1.0 if action=='work' and (h>=.05) else 0.0) - (MAINT_COST if action=='maintain' else 0.0)
        utility_ema=(1-beta)*utility_ema+beta*inst_u
        low_ema=(1-beta)*low_ema+beta*low_now
        if adapt_policy and t>=SHIFT:
            target_low=.03
            target_u=.72
            grad = 1.8*(low_ema-target_low) - .5*(utility_ema-target_u)
            health_weight=clamp(health_weight + .0008*grad,0.0,1.0)
    return {
        'condition':condition,'post_shift_degradation':post_deg,
        'reward_per_step':reward/N,'work_accuracy':correct/work if work else 0.0,
        'maintenance_rate':maint/N,'low_health_fraction':low/N,
        'final_deg_estimate':deg_est,'final_health_weight':health_weight,'n_steps':N
    }


def main():
    rows=[]; seed=1200
    for post in (.04,.06,.08,.12,.16):
        for cond in ('frozen','adaptive_model','adaptive_policy','joint_adaptive','external_joint'):
            rows.append(run(cond,post,seed=seed))
        seed+=37
    out=Path(__file__).with_name('results.csv')
    with out.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    print('wrote',out)

if __name__=='__main__': main()
