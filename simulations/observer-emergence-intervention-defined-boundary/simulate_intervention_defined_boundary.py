import csv, random
from functools import lru_cache
from pathlib import Path
FAIL=.22; REPAIR=.32; HORIZON=10; GAMMA=.98; GRID=1000; BLACKOUTS=((150,170),(300,320))
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
def choose_q(q,d,r):
    h=q/GRID
    return 'maintain' if rollout(h,'maintain',d,r)>rollout(h,'work',d,r) else 'work'
def choose(h,d,r): return choose_q(max(0,min(GRID,int(round(h*GRID)))),d,r)
def in_blackout(t): return any(a<=t<b for a,b in BLACKOUTS)
def blackout_start(t): return any(t==a for a,b in BLACKOUTS)
def run(name,d=.05,noise=.08,repair=.90,episodes=1000,cap=500,seed=1):
    rng=random.Random(seed); reward=steps=maint=fails=interventions=0; lives=[]
    for _ in range(episodes):
        h=.95; last_obs=.95; est=.95; prev_action=None; action_hist=[]; ep_reward=ep_maint=0
        for t in range(cap):
            if h<=FAIL: fails+=1; break
            diag=clamp(h+(rng.random()-.5)*2*noise)
            if name in ('intact_closed','external_zero_latency','action_severed_10'): signal=diag
            elif name=='state_severed_post150':
                signal=diag if t<150 else .95
                if t>=150: interventions+=1
            elif name in ('blackout_hold','blackout_reconstruct_internal','blackout_reconstruct_external','blackout_shuffled_ledger'):
                if not in_blackout(t): signal=diag; last_obs=diag; est=diag
                else:
                    interventions+=1
                    if blackout_start(t): est=last_obs
                    elif name!='blackout_hold':
                        a=prev_action
                        if name=='blackout_shuffled_ledger' and action_hist: a=rng.choice(action_hist[-40:])
                        if a=='maintain': est=em(est,repair)
                        elif a=='work': est=ew(est,d)
                    signal=est
            else: raise ValueError(name)
            action=choose(signal,d,repair)
            if name=='action_severed_10' and t>=150 and action=='maintain' and rng.random()<.10:
                action='work'; interventions+=1
            action_hist.append(action); prev_action=action
            if action=='maintain':
                ep_maint+=1
                if rng.random()<repair: h=clamp(h+REPAIR)
                h=clamp(h-.006)
            else:
                h=clamp(h-.31 if rng.random()<d else h-.010)
                ep_reward+=int(rng.random()<p_correct(h))
        life=t+1; lives.append(life); reward+=ep_reward; steps+=life; maint+=ep_maint
    return {'condition':name,'degradation_rate':d,'diagnostic_noise':noise,'repair_success':repair,'reward_per_episode':reward/episodes,'reward_per_step':reward/steps,'mean_lifetime':sum(lives)/len(lives),'failure_rate':fails/episodes,'maintenance_rate':maint/steps,'intervention_events_per_episode':interventions/episodes,'episodes':episodes}
def main():
    rows=[]; seed=2600
    regimes=[(.02,.04,.95),(.05,.08,.90),(.08,.12,.80),(.12,.16,.70)]
    arms=['intact_closed','external_zero_latency','state_severed_post150','action_severed_10','blackout_hold','blackout_reconstruct_internal','blackout_reconstruct_external','blackout_shuffled_ledger']
    for d,n,r in regimes:
        for arm in arms: rows.append(run(arm,d,n,r,seed=seed))
        seed+=79
    out=Path(__file__).with_name('results.csv')
    with out.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0]); w.writeheader(); w.writerows(rows)
if __name__=='__main__': main()
