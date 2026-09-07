#!/usr/bin/env python3
"""O-1D-prep: self-model-guided preservation of future sensing capability.

Synthetic information/control simulation. A sensor-bearing agent accumulates
stochastic internal degradation. Maintenance restores sensing capability but
has a fixed cost. The calibrated agent uses an estimate of its own current
health to time maintenance. Two controls receive the same maintenance budget:
(1) a shuffled self-state channel with the calibrated channel's marginal
distribution but destroyed temporal alignment, and (2) a budget-matched random
ablation schedule.

This is ordinary control theory. It is not a consciousness model and does not
establish SoCT physics.
"""
import csv, random
from pathlib import Path


def make_stream(n, seed, degrade_prob, obs_noise=0.08):
    r=random.Random(seed)
    shocks=[r.random()<degrade_prob for _ in range(n)]
    sensing_uniform=[r.random() for _ in range(n)]
    noise=[r.gauss(0,obs_noise) for _ in range(n)]
    return shocks, sensing_uniform, noise


def evaluate(condition, shocks, sensing_uniform, noise, channel=None,
             maintenance_mask=None, threshold=0.72, damage=0.18, repair=0.55,
             maintenance_cost=0.08):
    n=len(shocks); health=1.0; estimate=1.0
    utility=0.0; correct=0; maintenance=0; low_health=0; health_sum=0.0
    estimate_trace=[]; action_trace=[]

    for t in range(n):
        if shocks[t]:
            health=max(0.0,health-damage)

        z=min(1.0,max(0.0,health+noise[t]))
        estimate=0.85*estimate+0.15*z

        if condition=='calibrated':
            do_maintenance=estimate<threshold
        elif condition=='shuffled_placebo':
            do_maintenance=channel[t]<threshold
        elif condition=='budget_matched_ablation':
            do_maintenance=maintenance_mask[t]
        else:
            raise ValueError(condition)

        if do_maintenance:
            maintenance += 1
            health=min(1.0,health+repair)
            utility -= maintenance_cost

        sensing_accuracy=0.50+0.45*health
        is_correct=sensing_uniform[t] < sensing_accuracy
        correct += int(is_correct)
        utility += int(is_correct)
        health_sum += health
        low_health += int(health<0.5)
        estimate_trace.append(estimate)
        action_trace.append(int(do_maintenance))

    return {
        'utility_per_step':utility/n,
        'accuracy':correct/n,
        'maintenance_rate':maintenance/n,
        'mean_health':health_sum/n,
        'low_health_rate':low_health/n,
    }, estimate_trace, action_trace


def run_triplet(degrade_prob, n=100000, seed=100):
    shocks, sensing_uniform, noise=make_stream(n,seed,degrade_prob)
    calibrated, trace, actions=evaluate('calibrated',shocks,sensing_uniform,noise)

    r=random.Random(seed+999)
    shuffled=trace[:]
    r.shuffle(shuffled)
    placebo,_,_=evaluate('shuffled_placebo',shocks,sensing_uniform,noise,channel=shuffled)

    k=sum(actions)
    indices=list(range(n)); r.shuffle(indices)
    mask=[False]*n
    for i in indices[:k]: mask[i]=True
    ablated,_,_=evaluate('budget_matched_ablation',shocks,sensing_uniform,noise,
                         maintenance_mask=mask)

    rows=[]
    for name,result in [('calibrated',calibrated),('shuffled_placebo',placebo),
                        ('budget_matched_ablation',ablated)]:
        rows.append({'degrade_prob':degrade_prob,'condition':name,**result})
    return rows


def main():
    rows=[]
    for j,p in enumerate([0.01,0.03,0.06,0.10]):
        rows += run_triplet(p,seed=100+j)
    out=Path(__file__).with_name('results.csv')
    with out.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    print('wrote',out)

if __name__=='__main__': main()
