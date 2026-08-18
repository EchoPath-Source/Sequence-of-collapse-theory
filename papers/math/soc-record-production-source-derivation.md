# SoCT Record-Production Source Derivation

**Status:** exploratory operational derivation / simulation-ready scaffold  
**Claim level:** proposed source construction, not established physics  
**Purpose:** replace hand-injected collapse/memory source pulses with a source derived from an explicit interaction -> distinguishability -> record-production chain.

Related files:

- `papers/math/soc-operational-observation-model.md`
- `papers/math/soc-localization-memory-hamiltonian.md`
- `experiments/observation-foundations/SIM04E_RESULTS.md`

---

## 1. Target bridge

The operational observation program requires a concrete version of

```text
H_int
  -> conditional record states
  -> distinguishability / accessible information
  -> physical record acquisition
  -> persistence / accessibility
  -> Gamma_rec
  -> C_obs
  -> M.
```

SIM-04E established only that the canonical memory equation

```math
\partial_t M = \alpha C - \beta M + D_M \nabla^2 M
```

can produce a transferable synthetic signature when `C` is supplied externally.

The present derivation targets the missing source step.

---

## 2. Minimal binary system + pointer model

Let the observed system have two orthogonal alternatives

```math
|s_0\rangle, |s_1\rangle.
```

Use a two-state record-bearing pointer whose conditional states after an interaction are

```math
|o_0\rangle = |0\rangle,
```

```math
|o_1\rangle = \cos\theta\,|0\rangle + \sin\theta\,|1\rangle.
```

The interaction parameter `theta` is supplied by the ordinary interaction sector. It is **not** itself identified with collapse strength.

The conditional pointer overlap is

```math
|\langle o_0|o_1\rangle| = |\cos\theta|.
```

For pure conditional pointer states, the trace distance is

```math
D_{tr}
= \frac12\|\rho_0-\rho_1\|_1
= \sqrt{1-|\langle o_0|o_1\rangle|^2}
= |\sin\theta|.
```

Thus

```text
theta = 0      -> indistinguishable pointer states
theta = pi/2   -> orthogonal / perfectly distinguishable pointer states.
```

---

## 3. Accessible information candidate

For an equiprobable binary ensemble, the minimum Helstrom discrimination error is

```math
P_e = \frac{1-D_{tr}}{2}.
```

A simple operational information quantity is then

```math
I_{acc}
= 1-H_2(P_e),
```

where

```math
H_2(p)=-p\log_2 p-(1-p)\log_2(1-p).
```

This quantity obeys the desired limits:

```text
D_tr = 0 -> I_acc = 0
D_tr = 1 -> I_acc = 1 bit.
```

This is a deliberately minimal binary measurement model. It does not claim that every observation process reduces to this form.

---

## 4. Ordinary physical record state

Distinguish information available in the immediate pointer state from information that has actually been retained in a record-bearing degree of freedom.

Let

```math
R_t \in [0,1]
```

be a normalized ordinary record state.

Use the exploratory update

```math
\Delta R_t^{+}
= a\,I_{acc}(t)\,[1-R_{t-1}],
```

followed by ordinary record loss

```math
R_t
= (1-e_t)R_{t-1}+\Delta R_t^{+},
```

clipped to `[0,1]` when needed.

Here

```text
a   = record-acquisition rate
e_t = ordinary detector-record erasure / instability rate.
```

The saturation factor

```math
1-R_{t-1}
```

prevents repeated interrogation of an already saturated record from being counted as unlimited new record production.

Crucially, `R_t` is **ordinary detector/environment memory**, not the proposed SoCT field `M`.

---

## 5. Persistence and downstream accessibility

For a chosen persistence horizon `H`, define the first exploratory survival factor

```math
P_H(t)=[1-e_t]^H.
```

Let

```math
A_d(t)\in[0,1]
```

represent downstream accessibility of the record.

The candidate robust record-production rate is

```math
\Gamma_{rec}(t)
= \Delta R_t^{+}\,P_H(t)\,A_d(t).
```

Equivalently,

```math
\Gamma_{rec}(t)
= a\,I_{acc}(t)\,[1-R_{t-1}]\,[1-e_t]^H\,A_d(t).
```

This realizes the qualitative structure proposed in the operational observation model:

```math
\Gamma_{rec}
= G(\partial_t I, R, A_d, \Xi_{irr}).
```

The present `P_H` term is only a simple operational proxy for record robustness / irreversibility. It is not asserted to be fundamental.

---

## 6. Candidate SoCT observation source

Define

```math
C_{obs}(x,t)
= \kappa_{rec}\,\Gamma_{rec}(x,t).
```

The memory equation becomes

```math
\partial_t M
= \alpha C_{obs}
- \beta M
+ D_M\nabla^2M.
```

The coupling constants `kappa_rec` and `alpha` are partly degenerate in this minimal model; only their product is identifiable unless another observable fixes one of them independently.

---

## 7. Competing source constructions

SIM-04F must not assume that `Gamma_rec` is correct merely because it was proposed here.

The same downstream memory model should be tested with at least:

```text
S_interaction = normalized interaction strength theta
S_info        = I_acc
S_Omega       = I_c * D_tr * R * A_d
S_acquisition = Delta R^+ * A_d
S_Gamma       = Delta R^+ * P_H * A_d.
```

All source candidates receive the same fitting privileges for `beta`, `D_M`, and one overall feedback scale.

A source mapping earns support only if parameters learned on one set of interaction/record protocols predict held-out protocols without retuning.

---

## 8. The source-memory confound

This derivation introduces an important conceptual boundary.

Because

```math
R_t
```

is itself history dependent, a source such as

```math
\Gamma_{rec}(t)
```

can inherit ordinary detector-history dependence **before** the SoCT field `M` is introduced.

Therefore

```text
history-dependent C_obs
```

is not evidence for

```text
an additional SoCT memory field.
```

The two layers must be separated experimentally:

```text
ordinary record state R
    -> derived source C_obs
    -> candidate SoCT memory M.
```

A strong later protocol should reset or independently measure `R` while testing whether a residual attributed to `M` remains.

---

## 9. Dimensional note

In the discrete simulation, `Gamma_rec` is measured in normalized record-information units per simulation step.

In a continuous-time physical model, if `Gamma_rec` is taken to have units

```text
bits / time / volume,
```

then `kappa_rec` converts record-production rate into the units chosen for `C_obs`, while `alpha` converts `C_obs` into memory-density production.

A future dimensional audit must choose the physical normalization of `M` and `C_obs` before either coupling is interpreted independently.

---

## 10. Falsification / interpretation discipline

This derivation is useful only if the following remain distinct:

1. ordinary interaction;
2. pointer distinguishability;
3. accessible information;
4. ordinary detector record state;
5. robust record-production rate;
6. candidate SoCT memory field;
7. feedback of `M` into later dynamics.

Failure to distinguish these layers would make the model circular.

A successful synthetic SIM-04F would establish only:

> the existing observation model can generate a concrete source functional whose downstream SoCT memory signature is recoverable across held-out protocols.

It would **not** establish that physical record production creates a new field in nature.
