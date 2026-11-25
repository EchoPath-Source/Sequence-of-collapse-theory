"""Conditional finite-exhaust relaxation: effective toy, not physical cosmology."""
import math
from scipy.integrate import quad, solve_ivp

S=.15
N=1.5
OM=.315
ODE=.685
H0=67.4
H_GYR=H0*1.022712165e-3
QPRIME=-S*N/(1-S)


def q(delta):
    if not math.isfinite(delta) or not -.9<=delta<=.5:
        raise ValueError('outside existing toy domain')
    return (1-S*(1+delta)**N)/(1-S)


def rate(tau,ell,k,a=1.):
    if tau<=0 or ell<0 or k<0 or a<=0:
        raise ValueError('invalid response parameters')
    return (1+(ell*k/a)**2)/tau


def step(u,source,duration,tau,ell=0.,k=0.,a=1.):
    """For a perturbation mode u=E-1 and source=q-1, fixed a."""
    if duration<0:raise ValueError('negative duration')
    lam=rate(tau,ell,k,a)
    return u*math.exp(-lam*duration)-source/(tau*lam)*math.expm1(-lam*duration)


def paired(tau,T=2.,probe=1.,ell=0.,k=0.):
    """Early dense then underdense vs reverse; identical mean-density probe."""
    h,l=q(.2)-1,q(-.2)-1
    early_dense=step(step(step(0,h,T,tau,ell,k),l,T,tau,ell,k),0,probe,tau,ell,k)
    early_void=step(step(step(0,l,T,tau,ell,k),h,T,tau,ell,k),0,probe,tau,ell,k)
    lam=rate(tau,ell,k)
    formula=(l-h)/(tau*lam)*math.expm1(-lam*T)**2*math.exp(-lam*probe)
    return early_dense,early_void,formula


def toy_h(u):
    return H0*math.sqrt(1+ODE*u)


def growth(a):
    def e(x):return math.sqrt(OM/x**3+ODE)
    # growing solution for pressureless matter + Lambda, arbitrary normalization
    return e(a)*quad(lambda x:1/(x**3*e(x)**3),0,a,epsabs=1e-10)[0]


def growing_mode(tau,ell,k,a_end=1.,a_start=.25,initial='zero'):
    """Linear source q'=QPRIME*delta; normalize growing delta(a_end)=1.
    This is a transfer coefficient, not a nonlinear delta=1 evaluation.
    Constant physical diffusion D=ell^2/tau; fixed LCDM background.
    """
    if not 0<a_start<a_end:raise ValueError('invalid scale-factor interval')
    rate(tau,ell,k,a_start)
    norm=growth(a_end)
    def source(a):return growth(a)/norm
    if initial=='zero':y0=0.
    elif initial=='equilibrium':y0=source(a_start)/(1+(ell*k/a_start)**2)
    else:raise ValueError('unknown initial condition')
    def rhs(a,y):
        H=H_GYR*math.sqrt(OM/a**3+ODE)
        return [(source(a)/tau-rate(tau,ell,k,a)*y[0])/(a*H)]
    sol=solve_ivp(rhs,(a_start,a_end),[y0],method='Radau',rtol=1e-8,atol=1e-10)
    if not sol.success:raise RuntimeError(sol.message)
    return float(sol.y[0,-1])


if __name__=='__main__':
    print('tau_Gyr,history_exhaust_difference,conditional_H_difference')
    for tau in (.1,1,2,5,10,20):
        a,b,d=paired(tau);print(tau,round(d,8),round(toy_h(a)-toy_h(b),6))
    print('tau,ell,k,history_difference,linear_growth_transfer_z0,transfer_z0.5')
    for tau in (1.,5.,10.):
        for ell in (0.,10.,30.):
            for k in (.02,.05,.1):
                print(tau,ell,k,round(paired(tau,ell=ell,k=k)[2],7),round(growing_mode(tau,ell,k),6),round(growing_mode(tau,ell,k,a_end=2/3),6))
    print('initial_condition_sensitivity_tau10_ell0',growing_mode(10,0,0,initial='zero'),growing_mode(10,0,0,initial='equilibrium'))
