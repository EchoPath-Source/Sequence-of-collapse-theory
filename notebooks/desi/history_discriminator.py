"""Synthetic matched-density history identifiability. No astronomical outcomes."""
import argparse
import numpy as np
from scipy.linalg import cholesky, solve_triangular
from scipy.special import ndtr


def exhaust_history(delta, times, tau):
    """Normalized relaxation with E(t0)=1, piecewise constant midpoint source."""
    delta=np.asarray(delta,float); times=np.asarray(times,float)
    if tau<=0 or times.ndim!=1 or len(times)<2 or np.any(np.diff(times)<=0) or delta.shape[-1]!=len(times)-1:
        raise ValueError('invalid trajectory grid or tau')
    if not np.all(np.isfinite(delta)&(delta>=-.9)&(delta<=.5)):
        raise ValueError('outside existing toy domain')
    q=(1-.15*(1+delta)**1.5)/.85
    # Exact integral for each midpoint-constant segment, initial E=1.
    w=np.exp(-(times[-1]-times[1:])/tau)*(-np.expm1(-np.diff(times)/tau))
    return 1+(q-1)@w


def conditional_mu(E):
    return -2.5*np.log10(.315+.685*E)


def trajectories(n=768, blocks=64, steps=320, seed=20261125):
    if n%blocks or steps<2:raise ValueError('equal-sized spatial blocks required')
    rng=np.random.default_rng(seed); t=np.linspace(0,8,steps+1); m=(t[1:]+t[:-1])/2
    group=np.repeat(np.arange(blocks),n//blocks)
    current=rng.uniform(-.3,.25,n); amplitude=rng.uniform(.05,.25,n)
    base=current[:,None]*np.exp((m-8)/8)
    bump=amplitude[:,None]*np.sin(np.pi*m/8)**2
    # Analytic underlying curves match both endpoint density and derivative.
    plus,minus=base+bump,base-bump
    proxy=2*amplitude+rng.normal(0,.08,n)+rng.normal(0,.04,blocks)[group]
    # Fixed paired FP-like error and illustrative shared block covariance.
    sigma=rng.uniform(.43,.60,(n,2)); C=np.diag(np.sum(sigma**2,axis=1))+.03**2*(group[:,None]==group[None,:])
    return t,plus,minus,current,2*amplitude,proxy,C


def evaluate(g,X,L,confound):
    """Known covariance, analytic normal power and omitted-variable stress."""
    w=solve_triangular(L,g,lower=True); W=solve_triangular(L,X,lower=True)
    U,s,_=np.linalg.svd(W,full_matrices=False); Q=U[:,s>s[0]*1e-12]
    h=w-Q@(Q.T@w); info=h@h
    if info<=1e-12*(w@w):return dict(info=0.,mda=float('inf'),power=float('nan'),false_positive=float('nan'),bias=float('nan'))
    se=1/np.sqrt(info); bias=h@solve_triangular(L,confound,lower=True)/info
    def reject(a):return float(ndtr(-1.959964-a/se)+ndtr(a/se-1.959964))
    return dict(info=info,mda=2.801585*se,power=reject(1),false_positive=reject(bias),bias=bias)


def run(n=768,seed=20261125):
    t,p,m,d,A,proxy,C=trajectories(n=n,seed=seed); L=cholesky(C,lower=True)
    # Pair-difference systematic, deliberately chosen for stress, not CF4 estimate.
    conf=.08*A+.04*A*d
    base=np.column_stack([np.ones(n),d,d*d])
    nuisances={'density':base,'assembly_exact':np.column_stack([base,A]),'assembly_interaction':np.column_stack([base,A,A*d]),'assembly_noisy':np.column_stack([base,proxy,proxy*d])}
    for tau in (.1,1,2,5,10,20):
        g=conditional_mu(exhaust_history(p,t,tau))-conditional_mu(exhaust_history(m,t,tau))
        print('tau',tau,'median mag',round(float(np.median(g)),7),'range',np.quantile(g,[.1,.9]).round(7).tolist())
        for name,X in nuisances.items():
            s=evaluate(g,X,L,conf)
            print(name,{k:round(v,6) for k,v in s.items()})


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--n',type=int,default=768);p.add_argument('--seed',type=int,default=20261125);a=p.parse_args();run(a.n,a.seed)
