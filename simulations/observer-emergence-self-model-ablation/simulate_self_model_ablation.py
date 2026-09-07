#!/usr/bin/env python3
"""O-1C: calibrated self-model versus shuffled/placebo and ablated controls.

Synthetic observer-emergence simulation. All agents receive the same world,
sensor-state sequence, raw observations, memory capacity, and nominal policy
complexity. The distinction is whether the internal reliability channel is
informative, shuffled across time, or fixed/ablated.

This is ordinary information/control theory and makes no consciousness or
novel-physics claim.
"""
import csv, math, random
from pathlib import Path


def mi_binary(xs, ys):
    n=len(xs); joint={(x,y):0 for x in (0,1) for y in (0,1)}; cx=[0,0]; cy=[0,0]
    for x,y in zip(xs,ys): joint[(x,y)]+=1; cx[x]+=1; cy[y]+=1
    out=0.0
    for x in (0,1):
        for y in (0,1):
            c=joint[(x,y)]
            if c:
                p=c/n; out += p*math.log2(p/((cx[x]/n)*(cy[y]/n)))
    return out


def generate_stream(n, persistence, switch_prob, seed):
    r=random.Random(seed); world=r.randrange(2); good=True; rows=[]
    for _ in range(n):
        if r.random() >= persistence: world=1-world
        if r.random() < switch_prob: good=not good
        acc=.90 if good else .55
        direct=world if r.random()<acc else 1-world
        rows.append((world,1 if good else 0,direct))
    return rows


def reliability_estimates(stream, alpha=.04):
    est=.5; prev=stream[0][2]; vals=[]
    for _,_,direct in stream:
        agree=1.0 if direct==prev else 0.0
        est=(1-alpha)*est+alpha*agree
        vals.append(est); prev=direct
    return vals


def evaluate(stream, channel, seed):
    r=random.Random(seed); prev_obs=stream[0][2]; worlds=[]; guesses=[]; truths=[]; estbits=[]; correct=0
    for i,(world,truth,direct) in enumerate(stream):
        z=channel[i]
        use_direct=z>=.5
        if use_direct: obs=direct
        else: obs=prev_obs if r.random()<.75 else direct
        worlds.append(world); guesses.append(obs); truths.append(truth); estbits.append(1 if z>=.5 else 0)
        correct += int(obs==world); prev_obs=obs
    return correct/len(stream), mi_binary(worlds,guesses), mi_binary(truths,estbits)


def run_case(persistence,switch_prob,n=200000,seed=101):
    stream=generate_stream(n,persistence,switch_prob,seed)
    calibrated=reliability_estimates(stream)
    # Shuffled placebo preserves the exact marginal distribution/computational
    # channel size but destroys temporal alignment with the agent's own state.
    shuffled=calibrated[:]; random.Random(seed+1).shuffle(shuffled)
    # Ablated channel retains the scalar input slot but contains no information.
    ablated=[.5]*n
    rows=[]
    for j,(name,ch) in enumerate([('calibrated',calibrated),('shuffled_placebo',shuffled),('ablated',ablated)]):
        acc,wmi,smi=evaluate(stream,ch,seed+10+j)
        rows.append({'condition':name,'world_persistence':persistence,'sensor_switch_prob':switch_prob,
                     'accuracy':acc,'world_mutual_information_bits':wmi,
                     'self_state_mutual_information_bits':smi,'n_steps':n})
    return rows


def main():
    rows=[]; seed=101
    for p in [0.50,0.70,0.90,0.97]:
        for sw in [0.01,0.05,0.15]:
            rows += run_case(p,sw,seed=seed); seed+=20
    out=Path(__file__).with_name('results.csv')
    with out.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    print('wrote',out)

if __name__=='__main__': main()
