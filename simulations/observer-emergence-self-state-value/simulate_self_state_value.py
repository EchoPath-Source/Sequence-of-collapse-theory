#!/usr/bin/env python3
"""O-1C2: decision-theoretic value of calibrated self-state information.

All agents face the same binary world and the same changing internal sensor state.
They can use either a cheap sensor whose reliability depends on internal state or
an expensive/reliable sensor with fixed cost. The calibrated, shuffled-placebo,
and ablated agents are constrained to the SAME expensive-sensor usage rate.

The only intended advantage of the calibrated agent is temporal alignment between
its self-state estimate and its true internal reliability state.

Ordinary information/control-theory simulation. No consciousness or novel-physics
claim is made.
"""
import csv, math, random
from pathlib import Path


def mi_binary(xs, ys):
    n=len(xs); joint={(x,y):0 for x in (0,1) for y in (0,1)}; cx=[0,0]; cy=[0,0]
    for x,y in zip(xs,ys):
        joint[(x,y)]+=1; cx[x]+=1; cy[y]+=1
    out=0.0
    for x in (0,1):
        for y in (0,1):
            c=joint[(x,y)]
            if c:
                p=c/n
                out += p*math.log2(p/((cx[x]/n)*(cy[y]/n)))
    return out


def generate_stream(n, persistence, switch_prob, seed):
    r=random.Random(seed); world=r.randrange(2); good=True; rows=[]
    for _ in range(n):
        if r.random() >= persistence:
            world=1-world
        if r.random() < switch_prob:
            good=not good
        cheap_acc=.90 if good else .55
        cheap=world if r.random()<cheap_acc else 1-world
        reliable=world if r.random()<.96 else 1-world
        rows.append((world,1 if good else 0,cheap,reliable))
    return rows


def estimate_self_state(stream, alpha=.05):
    est=.5; prev=stream[0][2]; values=[]
    for _,_,cheap,_ in stream:
        # In a temporally persistent world, agreement with recent sensory history
        # provides a noisy cue to current sensor reliability.
        agree=1.0 if cheap==prev else 0.0
        est=(1-alpha)*est+alpha*agree
        values.append(est)
        prev=cheap
    return values


def evaluate_actions(stream, actions, cost):
    rewards=[]; guesses=[]; worlds=[]; truths=[]; action_bits=[]
    correct=0
    for (world,truth,cheap,reliable),use_reliable in zip(stream,actions):
        obs=reliable if use_reliable else cheap
        correct += int(obs==world)
        rewards.append((1 if obs==world else 0) - (cost if use_reliable else 0))
        guesses.append(obs); worlds.append(world); truths.append(truth)
        action_bits.append(1 if use_reliable else 0)
    n=len(stream)
    return {
        'utility_per_step':sum(rewards)/n,
        'accuracy':correct/n,
        'reliable_sensor_rate':sum(action_bits)/n,
        'world_mutual_information_bits':mi_binary(worlds,guesses),
        'sensor_state_action_mutual_information_bits':mi_binary(truths,action_bits),
    }


def run_case(persistence,switch_prob,n=100000,seed=100,cost=.12,threshold=.52):
    stream=generate_stream(n,persistence,switch_prob,seed)
    calibrated=estimate_self_state(stream)

    calibrated_actions=[z<threshold for z in calibrated]
    budget=sum(calibrated_actions)/n

    shuffled=calibrated[:]
    random.Random(seed+1).shuffle(shuffled)
    shuffled_actions=[z<threshold for z in shuffled]

    # Ablated control receives no self-state information but is forced to spend
    # exactly the same expensive-sensor budget as the calibrated policy.
    order=list(range(n)); random.Random(seed+2).shuffle(order)
    k=round(budget*n); selected=set(order[:k])
    ablated_actions=[i in selected for i in range(n)]

    rows=[]
    for name,actions in [
        ('calibrated',calibrated_actions),
        ('shuffled_placebo',shuffled_actions),
        ('ablated_budget_matched',ablated_actions),
    ]:
        metrics=evaluate_actions(stream,actions,cost)
        rows.append({
            'condition':name,
            'world_persistence':persistence,
            'sensor_switch_prob':switch_prob,
            'expensive_sensor_cost':cost,
            **metrics,
            'n_steps':n,
        })
    return rows


def main():
    rows=[]; seed=100
    for persistence in [0.70,0.90,0.97]:
        for switch_prob in [0.01,0.05,0.15]:
            rows += run_case(persistence,switch_prob,seed=seed)
            seed += 20
    out=Path(__file__).with_name('results.csv')
    with out.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    print('wrote',out)

if __name__=='__main__':
    main()
