"""Frozen PNT toy equations and linear-GR local-divergence comparator.
Neither provides a line-of-sight distance likelihood. No observations loaded.
"""
import math

H_REF = 67.4
OMEGA_M = .315
OMEGA_DE = .685
SUCCESS = .15
EXPONENT = 1.5
A = OMEGA_DE * SUCCESS / (1 - SUCCESS)


def check_delta(delta):
    if not math.isfinite(delta) or not -.9 <= delta <= .5:
        raise ValueError('outside existing toy-model domain [-.9,.5]')


def exhaust_ratio(delta):
    check_delta(delta)
    return (1 - SUCCESS * (1 + delta)**EXPONENT) / (1 - SUCCESS)


def toy_h(delta):
    return H_REF * math.sqrt(OMEGA_M + OMEGA_DE * exhaust_ratio(delta))


def toy_mu(delta):
    """Conditional fixed-redshift distance rescaling only, not a light-cone prediction."""
    return -5 * math.log10(toy_h(delta) / H_REF)


def toy_slope_at_mean():
    return -H_REF * A * EXPONENT / 2


def gr_local_divergence(delta):
    """Linear z=0 local expansion perturbation, not observed H0 residual."""
    check_delta(delta)
    return -H_REF * OMEGA_M**.55 * delta / 3


def toy_contrast(low, high):
    """H(low)-H(high), mu(high)-mu(low), both at fixed fiducial background."""
    if not low < high:
        raise ValueError('ordered density endpoints required')
    return toy_h(low) - toy_h(high), toy_mu(high) - toy_mu(low)


if __name__ == '__main__':
    print('delta,rho_exhaust_ratio,H_toy,delta_H_toy,delta_mu_conditional,delta_H_GR_linear')
    for d in (-.9, -.8, -.5, -.35, -.2, 0., .2, .3, .5):
        print(f'{d:.2f},{exhaust_ratio(d):.6f},{toy_h(d):.6f},{toy_h(d)-H_REF:.6f},{toy_mu(d):.6f},{gr_local_divergence(d):.6f}')
    print('toy derivative at mean', toy_slope_at_mean())
    print('conditional example contrast [-.2,.2]', toy_contrast(-.2,.2))
