#!/usr/bin/env python3
"""O-1B: explicit self-state model versus feedback-only observer.

Synthetic control/information-theory simulation. Two adaptive agents have the
same memory and action repertoire. One estimates only the external world; the
other also estimates its own sensor reliability state and uses that estimate
to select sensing mode. No consciousness claim is made.
"""

import csv
import math
import random
from pathlib import Path


def entropy2(p):
    if p <= 0 or p >= 1:
        return 0.0
    return -p*math.log2(p)-(1-p)*math.log2(1-p)


def mutual_information_binary(xs, ys):
    n=len(xs)
    counts={(x,y):0 for x in (0,1) for y in (0,1)}
    cx={0:0,1:0}; cy={0:0,1:0}
    for x,y in zip(xs,ys):
        counts[(x,y)]+=1; cx[x]+=1; cy[y]+=1
    mi=0.0
    for x in (0,1):
        for y in (0,1):
            c=counts[(x,y)]
            if c:
                pxy=c/n; px=cx[x]/n; py=cy[y]/n
                mi += pxy*math.log2(pxy/(px*py))
    return mi


def step_markov(state, persistence, rng):
    return state if rng.random() < persistence else 1-state


def run_agent(kind, persistence=0.9, sensor_switch=0.05, n=200000, seed=1):
    rng=random.Random(seed)
    world=rng.choice([0,1])
    sensor_good=True
    prev_obs=rng.choice([0,1])
    est_good=0.5
    ys=[]; guesses=[]; sensor_truth=[]; sensor_est=[]
    correct=0

    for _ in range(n):
        world=step_markov(world,persistence,rng)
        if rng.random() < sensor_switch:
            sensor_good=not sensor_good

        # Agent chooses between direct sensing and memory-weighted sensing.
        # Direct observation is reliable in good state, poor in degraded state.
        # The self-state agent adapts mode using its own estimated reliability.
        if kind == "self_state":
            use_direct = est_good >= 0.5
        else:
            use_direct = True

        direct_acc = 0.90 if sensor_good else 0.55
        direct = world if rng.random() < direct_acc else 1-world
        memory_pred = prev_obs

        if use_direct:
            obs=direct
        else:
            # fallback blends persistent-world prediction with a weak fresh sample
            if rng.random() < 0.75:
                obs=memory_pred
            else:
                obs=direct

        guess=obs
        correct += int(guess==world)
        ys.append(world); guesses.append(guess)
        sensor_truth.append(1 if sensor_good else 0)

        # Only the self-state model estimates sensor reliability from whether
        # direct evidence agrees with the memory prediction in a persistent world.
        if kind == "self_state":
            agree = 1.0 if direct == memory_pred else 0.0
            target = agree
            est_good = 0.96*est_good + 0.04*target
        sensor_est.append(est_good)
        prev_obs=obs

    # self-state discrimination: threshold estimated reliability against truth
    if kind == "self_state":
        est_bits=[1 if e>=0.5 else 0 for e in sensor_est]
        self_mi=mutual_information_binary(sensor_truth,est_bits)
    else:
        self_mi=0.0
    return {
        "agent":kind,
        "world_persistence":persistence,
        "sensor_switch_prob":sensor_switch,
        "accuracy":correct/n,
        "world_mutual_information_bits":mutual_information_binary(ys,guesses),
        "self_state_mutual_information_bits":self_mi,
        "n_steps":n,
    }


def main():
    rows=[]
    seed=10
    for persistence in [0.50,0.70,0.90,0.97]:
        for switch in [0.01,0.05,0.15]:
            for kind in ["feedback_only","self_state"]:
                rows.append(run_agent(kind,persistence,switch,seed=seed))
                seed+=1
    out=Path(__file__).with_name("results.csv")
    with out.open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    print(f"wrote {out}")

if __name__ == "__main__":
    main()
