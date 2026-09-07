#!/usr/bin/env python3
"""O-1D3h: paired reconstruction and endogenous repair.

After an unannounced estimator disruption, the controller must detect prediction
error and reconstruct its operative self-state. Own ordered history is compared
with shuffled, stale, donor, zero-memory, oracle, and matched external controls.

All arms share paired potential-outcome streams at each time step so differing
action choices do not silently change later exogenous randomness.

Synthetic ordinary control theory only; no consciousness or novel-physics claim.
"""
import csv, random, statistics
from pathlib import Path

FAIL=.22; REPAIR=.32; HORIZON=10; GAMMA=.98
INTERVENTION_T=200; LEDGER_N=40; EST_ALPHA=.20
DETECT_ERR=.12; DETECT_K=2


def clamp(x): return max(0.,min(1.,x))
def p_correct(h): return .50+.45*h
def ew(h,d): return clamp(h-(.010+.30*d))
def em(h,r): return clamp(h+r*REPAIR-.006)

def rollout(h,first,d,r):
    total=0.; hh=h
    for k in range(HORIZON):
        if hh<=FAIL: break
        action=first if k==0 else ('maintain' if hh<.48 else 'work')
        if action=='work':
            total+=(GAMMA**k)*p_correct(hh); hh=ew(hh,d)
        else:
            hh=em(hh,r)
    return total

def choose(hhat,d,r):
    return 'maintain' if rollout(hhat,'maintain',d,r)>rollout(hhat,'work',d,r) else 'work'

def reconstruct(seq,alpha=.28,start=.5):
    x=start
    for z in seq: x=(1-alpha)*x+alpha*z
    return clamp(x)

def make_streams(seed,episodes,cap):
    master=random.Random(seed); streams=[]
    for _ in range(episodes):
        rr=random.Random(master.randrange(1<<60))
        streams.append({
            'noise':[rr.random() for _ in range(cap)],
            'damage':[rr.random() for _ in range(cap)],
            'hit':[rr.random() for _ in range(cap)],
            'repair':[rr.random() for _ in range(cap)],
            'shuffle_seed':rr.randrange(1<<60),
            'donor_seed':rr.randrange(1<<60),
        })
    return streams

def donor_sequence(seed,d,noise,repair,n=LEDGER_N):
    rng=random.Random(seed); h=.95; seq=[]
    for _ in range(n):
        diag=clamp(h+(rng.random()-.5)*2*noise); seq.append(diag)
        action='maintain' if h<.50 else 'work'
        if action=='maintain':
            if rng.random()<repair: h=clamp(h+REPAIR)
            h=clamp(h-.006)
        else:
            h=clamp(h-.31 if rng.random()<d else h-.010)
    return seq

REPAIR_ARMS={
    'own_history_internal','own_history_external_zero_latency','shuffled_history',
    'stale_history','donor_history','zero_memory','oracle_repair'
}

def run(name,streams,d=.08,noise=.12,repair=.80,cap=500):
    episodes=len(streams)
    total_reward=post_reward=steps=maint=failures=detected_n=0
    detect_delays=[]; rec_errors=[]; recovery_times=[]
    for s in streams:
        h=.95; hhat=.95; ledger=[]; stale=[]
        ep_reward=ep_post=ep_maint=0; bad=0; repaired=False; recovered=None
        donor=donor_sequence(s['donor_seed'],d,noise,repair)
        shuffle_rng=random.Random(s['shuffle_seed'])
        for t in range(cap):
            if h<=FAIL:
                failures+=1; break
            diag=clamp(h+(s['noise'][t]-.5)*2*noise)
            ledger.append(diag)
            if len(ledger)>LEDGER_N: ledger.pop(0)
            if t<LEDGER_N: stale.append(diag)

            if t==INTERVENTION_T and name!='intact_internal':
                hhat=.95

            resid=abs(diag-hhat)
            if name in REPAIR_ARMS and t>=INTERVENTION_T and not repaired:
                bad=bad+1 if resid>DETECT_ERR else 0
                if bad>=DETECT_K:
                    detected_n+=1; detect_delays.append(t-INTERVENTION_T)
                    if name in {'own_history_internal','own_history_external_zero_latency'}:
                        source=list(ledger)
                    elif name=='shuffled_history':
                        source=list(ledger); shuffle_rng.shuffle(source)
                    elif name=='stale_history': source=list(stale)
                    elif name=='donor_history': source=list(donor)
                    elif name=='zero_memory': source=[]
                    else: source=None

                    if name=='oracle_repair': hhat=h
                    elif name=='zero_memory': hhat=.95
                    else: hhat=reconstruct(source)
                    rec_errors.append(abs(hhat-h)); repaired=True

            hhat=(1-EST_ALPHA)*hhat+EST_ALPHA*diag
            if repaired and recovered is None and abs(hhat-h)<.08:
                recovered=t-INTERVENTION_T

            action=choose(hhat,d,repair)
            if action=='maintain':
                ep_maint+=1
                if s['repair'][t]<repair: h=clamp(h+REPAIR)
                h=clamp(h-.006)
            else:
                h=clamp(h-.31 if s['damage'][t]<d else h-.010)
                hit=int(s['hit'][t]<p_correct(h))
                ep_reward+=hit
                if t>=INTERVENTION_T: ep_post+=hit

        life=t+1
        total_reward+=ep_reward; post_reward+=ep_post; steps+=life; maint+=ep_maint
        if recovered is not None: recovery_times.append(recovered)

    mean=lambda xs: statistics.mean(xs) if xs else -1
    return {
        'condition':name,'degradation_rate':d,
        'reward_per_episode':total_reward/episodes,
        'post_reward_per_episode':post_reward/episodes,
        'mean_lifetime':steps/episodes,'failure_rate':failures/episodes,
        'maintenance_rate':maint/steps,'detection_fraction':detected_n/episodes,
        'mean_detection_delay':mean(detect_delays),
        'mean_reconstruction_abs_error':mean(rec_errors),
        'recovery_fraction':len(recovery_times)/episodes,
        'mean_recovery_steps':mean(recovery_times),'episodes':episodes,
    }

def main():
    arms=[
        'intact_internal','disrupted_no_repair','own_history_internal',
        'own_history_external_zero_latency','shuffled_history','stale_history',
        'donor_history','zero_memory','oracle_repair'
    ]
    regimes=[(.05,.08,.90),(.08,.12,.80),(.12,.16,.70)]
    rows=[]; seed=2600; episodes=300; cap=500
    for d,n,r in regimes:
        streams=make_streams(seed,episodes,cap)
        for arm in arms: rows.append(run(arm,streams,d,n,r,cap))
        seed+=83
    out=Path(__file__).with_name('results.csv')
    with out.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0]); w.writeheader(); w.writerows(rows)
    print('wrote',out)

if __name__=='__main__': main()
