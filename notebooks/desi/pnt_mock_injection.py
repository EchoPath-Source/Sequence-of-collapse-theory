"""Synthetic conditional-template injection; no astronomical inputs or physical light cone."""
import argparse
import numpy as np
from scipy.linalg import cholesky, solve_triangular
from scipy.spatial.distance import cdist
from scipy.special import expit
from pnt_density_prediction import toy_mu


def make_mock(n=1483, seed=20261125):
    rng=np.random.default_rng(seed)
    # Synthetic spatially clustered population; not a fit to CF4 geometry.
    k=64; cap=rng.integers(0,2,k); ra=rng.uniform(110,260,k);ra[cap==1]=rng.uniform(300,355,(cap==1).sum()); dec=rng.uniform(0,45,k);z=rng.uniform(.035,.12,k)
    a,b=np.deg2rad(ra),np.deg2rad(dec);u=np.column_stack((np.cos(a)*np.cos(b),np.sin(a)*np.cos(b),np.sin(b)))
    centers=2997.92458*z[:,None]*u
    count=3*n;ix=rng.integers(k,size=count);p=centers[ix]+rng.normal(0,8,(count,3));r=np.linalg.norm(p,axis=1);u=p/r[:,None];z=r/2997.92458
    latent=rng.normal(0,.85,k)[ix]+rng.normal(0,.45,count)
    delta=-.2+.69*np.tanh(latent)
    # Fixed covariate selection, not magnitude truncation / Malmquist model.
    eligible=np.flatnonzero((z>=.023)&(z<=.15)&(rng.random(count)<expit(2.0-15*(z-.06)+.5*delta)))
    if len(eligible)<n:raise ValueError('insufficient mock rows')
    i=rng.choice(eligible,n,replace=False);p,u,z,delta,ix,latent=[v[i] for v in (p,u,z,delta,ix,latent)]
    proxy=-.2+.69*np.tanh(latent+rng.normal(0,.22,k)[ix]+rng.normal(0,.18,n))
    sigma=np.clip(rng.normal(.52,.07,n),.28,.75)
    v=5/np.log(10)/(299792.458*z)
    # Illustrative projected coherent vector-field covariance, not calibrated GR.
    cov=np.diag(sigma**2+(150*v)**2)+300**2*(v[:,None]*v[None,:])*(u@u.T)*np.exp(-cdist(p,p)/50)
    bulk=-v*(u@np.array([150.,-100.,80.]))
    t=(z-z.mean())/.02; X=np.column_stack((np.ones(n),t,t*t,cap[ix]))
    mean=X@np.array([.03,.02,-.006,.04])+bulk
    systematic=.15*delta+.10*delta**2
    return delta,proxy,X,cov,mean,bulk,systematic


def residual_template(X,g,L):
    w=solve_triangular(L,g,lower=True);D=solve_triangular(L,X,lower=True)
    q,r=np.linalg.qr(D,mode='reduced')
    if np.linalg.matrix_rank(r)<D.shape[1]:raise ValueError('rank deficient nuisance design')
    h=w-q@(q.T@w);info=h@h
    if info<=1e-12*(w@w):raise ValueError('template unidentifiable')
    return h,info


def run(n=1483,reps=2000,seed=20261125):
    d,proxy,X,cov,mean,bulk,sys=make_mock(n,seed);L=cholesky(cov,lower=True)
    g=np.array([toy_mu(x) for x in d]);rng=np.random.default_rng(seed+1)
    # Reuse common noise across scenarios; exact unit Gaussian whitened covariance.
    noise=rng.normal(size=(n,reps));base_info=None
    print('n,reps,seed,delta_iqr,proxy_rmse',n,reps,seed,np.quantile(d,[.25,.75]),np.sqrt(np.mean((d-proxy)**2)))
    for kind,pred in [('truth',d),('noisy',proxy)]:
        gp=np.array([toy_mu(x) for x in pred])
        for name,extra in [('fixed',[]),('linear',[pred]),('quadratic',[pred,pred**2])]:
            D=np.column_stack([X,*extra]);h,I=residual_template(D,gp,L)
            if kind=='truth' and name=='fixed':base_info=I
            se=1/np.sqrt(I);noise_a=h@noise/I
            print('DESIGN',kind,name,'info',round(I,7),'fraction',round(I/base_info,7),'se',round(se,5),'MDA80',round(2.8016*se,5))
            # Mean bulk flow is treated as exactly known; all other baseline terms in X.
            for scenario,amp,conf in [('null',0,0),('injected',1,0),('confounded_null',0,1),('confounded_injected',1,1)]:
                signal=mean-bulk+amp*g+conf*sys
                expected=h@solve_triangular(L,signal,lower=True)/I
                a=expected+noise_a; reject=np.mean(abs(a)>1.959964*se);coverage=np.mean(abs(a-amp)<=1.959964*se)
                print('RESULT',kind,name,scenario,'mean',round(a.mean(),5),'reject0',round(reject,4),'coverage',round(coverage,4))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--n',type=int,default=1483);p.add_argument('--reps',type=int,default=2000);p.add_argument('--seed',type=int,default=20261125);a=p.parse_args();run(a.n,a.reps,a.seed)
