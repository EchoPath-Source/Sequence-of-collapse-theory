#!/usr/bin/env python3
"""O-1D3c: system identification versus policy adaptation.

Separates four questions under an abrupt degradation shift:
1. frozen model + frozen policy,
2. adaptive model + frozen policy,
3. frozen model + adaptive policy,
4. adaptive model + adaptive policy,
plus a matched external implementation and an oracle reference.

Synthetic ordinary control/model-predictive-control benchmark only.
"""
import csv, random
from pathlib import Path

HORIZON=6
GAMMA=.97
MAINT_COST=.12


def clamp(x): return max(.05,min(1.0,x))

def expected_next(h, action, degradation, repair_success):
    if action == 'maintain': return clamp(h + repair_success*.30 - .006)
    return clamp(h - (.010 + .30*degradation))

def immediate_value(h, action):
    return -MAINT_COST if action == 'maintain' else .50 + .45*h

def plan(h, degradation, repair_success, threshold=.68):
    vals={}
    for first in ('work','maintain'):
        hh=h; total=0.0
        for k in range(HORIZON):
            action=first if k == 0 else ('maintain' if hh < threshold else 'work')
            total += (GAMMA**k)*immediate_value(hh,action)
            hh=expected_next(hh,action,degradation,repair_success)
        vals[first]=total
    return max(vals,key=vals.get)

def run(condition, pre_deg=.03, post_deg=.08, shift_at=30000, n=80000,
        seed=1000, diag_noise=.08, repair_success=.90,
        adapt_alpha=.02, policy_alpha=.01):
    r=random.Random(seed); h=.95; model_deg=.03; threshold=.68
    pre_reward=post_reward=0.0; post_maint=post_low=0; model_errors=[]
    reward_ewma=.75
    for t in range(n):
        true_deg=pre_deg if t < shift_at else post_deg
        diag=clamp(h+(r.random()-.5)*2*diag_noise)
        if condition == 'frozen_model_frozen_policy':
            action=plan(diag,.03,repair_success,.68)
        elif condition == 'adaptive_model_frozen_policy':
            action=plan(diag,model_deg,repair_success,.68)
        elif condition == 'frozen_model_adaptive_policy':
            action=plan(diag,.03,repair_success,threshold)
        elif condition in ('adaptive_model_adaptive_policy_internal','adaptive_model_adaptive_policy_external'):
            action=plan(diag,model_deg,repair_success,threshold)
        elif condition == 'oracle':
            action=plan(diag,true_deg,repair_success,threshold)
        else: raise ValueError(condition)

        before=h; inst=0.0
        if action == 'maintain':
            inst=-MAINT_COST
            if r.random() < repair_success: h=clamp(h+.30)
            h=clamp(h-.006)
        else:
            if r.random() < true_deg: h=clamp(h-.31)
            else: h=clamp(h-.010)
            p=.50+.45*h; inst=1.0 if r.random() < p else 0.0
            if condition in ('adaptive_model_frozen_policy','adaptive_model_adaptive_policy_internal','adaptive_model_adaptive_policy_external'):
                observed_event=1.0 if before-h > .1 else 0.0
                model_deg=(1-adapt_alpha)*model_deg+adapt_alpha*observed_event

        if condition in ('frozen_model_adaptive_policy','adaptive_model_adaptive_policy_internal','adaptive_model_adaptive_policy_external','oracle'):
            reward_ewma=(1-policy_alpha)*reward_ewma+policy_alpha*inst
            threshold += .002*(reward_ewma-.75)
            threshold=min(.85,max(.45,threshold))

        if t < shift_at: pre_reward += inst
        else:
            post_reward += inst; post_maint += int(action == 'maintain'); post_low += int(h < .55)
            model_errors.append(abs(model_deg-true_deg))

    post_n=n-shift_at
    return {
        'condition':condition,'post_degradation':post_deg,
        'pre_reward_per_step':pre_reward/shift_at,'post_reward_per_step':post_reward/post_n,
        'post_maintenance_rate':post_maint/post_n,'post_low_health_fraction':post_low/post_n,
        'final_model_degradation':model_deg,
        'mean_post_model_abs_error':sum(model_errors)/len(model_errors),
        'final_policy_threshold':threshold,'n_steps':n
    }

def main():
    rows=[]
    conditions=['frozen_model_frozen_policy','adaptive_model_frozen_policy',
                'frozen_model_adaptive_policy','adaptive_model_adaptive_policy_internal',
                'adaptive_model_adaptive_policy_external','oracle']
    for j,post_deg in enumerate([.04,.06,.08,.12,.15]):
        for condition in conditions:
            rows.append(run(condition,post_deg=post_deg,seed=1100+37*j))
    out=Path(__file__).with_name('results.csv')
    with out.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    print('wrote',out)

if __name__ == '__main__': main()
