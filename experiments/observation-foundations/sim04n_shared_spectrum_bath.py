#!/usr/bin/env python3
"""SIM-04N: shared-spectrum Fourier-mode oscillator bath; synthetic methodology."""
import argparse
import json
import numpy as np

DT = 0.004
T_END = 18.0
MODES = (0, 1, 2, 3)
TRAIN = (0, 1)
TEST = (2, 3)
OMEGA0 = 1.0
C = 0.45
ETA = 0.5
CUTOFF = 12.0
WMIN, WMAX = 0.1, 30.0
N_BATH = 128
GAMMAS = np.arange(0.1, 0.901, 0.02)


def bath_spectrum(n=N_BATH, eta=ETA, cutoff=CUTOFF):
    w = np.linspace(WMIN, WMAX, n)
    dw = w[1] - w[0]
    J = eta * w * np.exp(-w / cutoff)
    coupling = np.sqrt(2 * J * w * dw / np.pi)
    return w, coupling


def source(t):
    if 0.5 <= t < 1.5:
        return np.sin(np.pi * (t - 0.5)) ** 2
    return 0.0


def omega2():
    # Periodic 8-site lattice; real normalized Fourier-mode surrogates.
    return np.array([OMEGA0 ** 2 + C ** 2 * 4 * np.sin(np.pi * k / 8) ** 2
                     for k in MODES])


def integrate(n=N_BATH, eta=ETA, cutoff=CUTOFF, dt=DT):
    w, coupling = bath_spectrum(n, eta, cutoff)
    steps = int(round(T_END / dt))
    times = np.arange(steps) * dt
    M = np.zeros(len(MODES))
    P = np.zeros(len(MODES))
    q = np.zeros((len(MODES), n))
    p = np.zeros_like(q)
    fields = np.empty((steps, len(MODES)))
    baths = np.empty_like(fields)
    totals = np.empty(steps)
    works = np.empty(steps)
    work = 0.
    w2 = w * w
    c_over_w2 = coupling / w2
    o2 = omega2()

    def acceleration(m, bq, force):
        shift = bq - m[:, None] * c_over_w2[None, :]
        return -o2 * m + shift @ coupling + force, -w2[None, :] * bq + m[:, None] * coupling[None, :]

    for i, t in enumerate(times):
        f0 = source(t)
        am, aq = acceleration(M, q, f0)
        mn = M + dt * P + 0.5 * dt * dt * am
        qn = q + dt * p + 0.5 * dt * dt * aq
        f1 = source(t + dt)
        am1, aq1 = acceleration(mn, qn, f1)
        pn = P + 0.5 * dt * (am + am1)
        bp = p + 0.5 * dt * (aq + aq1)
        work += 0.5 * (f0 + f1) * np.sum(mn - M)
        M, P, q, p = mn, pn, qn, bp
        shift = q - M[:, None] * c_over_w2[None, :]
        e_bath = 0.5 * np.sum(p * p + w2[None, :] * shift * shift, axis=1)
        e_field = 0.5 * (P * P + o2 * M * M)
        fields[i] = M
        baths[i] = e_bath
        totals[i] = np.sum(e_field + e_bath)
        works[i] = work
    return dict(t=times, field=fields, bath=baths, total=totals, work=works)


def reduced(gamma, dt=DT):
    steps = int(round(T_END / dt))
    t = np.arange(steps) * dt
    m = np.zeros(len(MODES))
    p = np.zeros_like(m)
    fields = np.empty((steps, len(MODES)))
    o2 = omega2()
    for i, ti in enumerate(t):
        a = -o2 * m - gamma * p + source(ti)
        mm = m + 0.5 * dt * p
        pp = p + 0.5 * dt * a
        a_mid = -o2 * mm - gamma * pp + source(ti + 0.5 * dt)
        m += dt * pp
        p += dt * a_mid
        fields[i] = m
    return fields


def rmse(x, y):
    return float(np.sqrt(np.mean((x - y) ** 2)))


def evaluate(n=N_BATH, dt=DT):
    micro = integrate(n=n, dt=dt)
    t = micro["t"]
    fit = (t >= 1.5) & (t < 7)
    hold = (t >= 7) & (t < 18)
    library = {round(float(g), 3): reduced(float(g), dt=dt) for g in GAMMAS}
    scores = {g: rmse(pred[fit][:, TRAIN], micro["field"][fit][:, TRAIN])
              for g, pred in library.items()}
    gamma = min(scores, key=scores.get)
    pred = library[gamma]
    per_mode = {}
    for k in MODES:
        early = (t >= 2) & (t < 7)
        late = (t >= 10) & (t < 18)
        per_mode[str(k)] = {
            "heldout_rmse": rmse(pred[hold, k], micro["field"][hold, k]),
            "recurrence_ratio": float(np.max(np.abs(micro["field"][late, k])) /
                                      (np.max(np.abs(micro["field"][early, k])) + 1e-15)),
            "final_bath_energy": float(micro["bath"][-1, k]),
        }
    closure = float(np.max(np.abs(micro["total"] - micro["total"][0] - micro["work"])))
    return {
        "status": "synthetic benchmark; no evidence for a novel memory field",
        "dt": dt, "bath_modes": n, "shared_eta": ETA, "shared_cutoff": CUTOFF,
        "training_modes": list(TRAIN), "heldout_modes": list(TEST),
        "training_window": [1.5, 7], "heldout_window": [7, 18],
        "fitted_shared_gamma": gamma,
        "training_rmse": scores[gamma],
        "heldout_rmse": rmse(pred[hold][:, TEST], micro["field"][hold][:, TEST]),
        "energy_closure_max_error": closure,
        "per_mode": per_mode,
        "limitation": "Fourier-diagonal independent baths do not establish spatial bath energy transport",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--bath-modes", type=int, default=N_BATH)
    parser.add_argument("--dt", type=float, default=DT)
    args = parser.parse_args()
    result = evaluate(n=args.bath_modes, dt=args.dt)
    print(json.dumps(result, indent=2))
