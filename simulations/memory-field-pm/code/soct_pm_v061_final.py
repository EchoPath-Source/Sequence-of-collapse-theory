"""
SoCT-PM v0.6.1 FINAL (reference snapshot)
-------------------------------------------------
Repository role:
- validated reference-line snapshot for the memory-field PM program
- preserved from the working thread after conformal-time / EOM / FFT-centering fixes

IMPORTANT:
This file is archived here as a reference implementation snapshot.
If a later production version diverges, keep version lineage explicit rather than overwriting history.
"""

import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass


@dataclass
class Params:
    N_part: int = 12_000
    N: int = 32
    L: float = 50.0
    dt_conf: float = 0.002
    n_steps: int = 1000
    a_init: float = 0.1
    seed: int = 42
    H0: float = 0.07
    Omega_m: float = 0.3
    Omega_L: float = 0.7
    G: float = 1.0
    N_clumps: int = 30
    clump_size: int = 120
    clump_sigma_pos: float = 0.3
    clump_sigma_vel: float = 0.01
    delta_c: float = 1.8
    eta: float = 1.0
    tau_memory: float = 8.0
    beta_mbar: float = 0.01
    kernel_sigma: float = 0.08 * 32
    alpha_core: float = -1.5
    M_sat: float = 0.10
    q_lo: float = 30.0
    q_hi: float = 70.0
    softening: float = 0.05
    bind_every: int = 100
    snap_every: int = 100
    out_prefix: str = "soct_pm_v061"


P = Params()


def hubble(a, H0, Om, OL):
    return H0 * np.sqrt(Om / a**3 + OL)


def conformal_hubble(a, H0, Om, OL):
    return a * hubble(a, H0, Om, OL)


def make_gaussian_kernel(N, sigma_grid):
    x = np.arange(-N // 2, N // 2)
    X, Y, Z = np.meshgrid(x, x, x, indexing="ij")
    r2 = X**2 + Y**2 + Z**2
    kernel = np.exp(-r2 / (2 * sigma_grid**2))
    kernel /= kernel.sum()
    return kernel


def fft_convolve_3d(grid, kernel_fft):
    grid_k = np.fft.rfftn(grid)
    conv_k = grid_k * kernel_fft
    return np.fft.irfftn(conv_k, s=grid.shape)


def update_memory_kernel(M, rho, dt, tau, eta, kernel_fft, delta_c):
    decay = np.exp(-dt / tau) if tau > 0 else 1.0
    overd = rho / (rho.mean() + 1e-12)
    S_raw = np.maximum(overd - delta_c, 0.0) * np.exp(-((overd - delta_c) ** 2) / 0.5)
    S_conv = fft_convolve_3d(S_raw, kernel_fft)
    M_new = decay * M + eta * S_conv * dt
    return M_new, S_conv


def saturating_fM(M, M_sat):
    return M / (1.0 + (M / (M_sat + 1e-12)))


def cic_deposit_3d(pos, N, L):
    rho = np.zeros((N, N, N), dtype=np.float64)
    dx = L / N
    xp = pos / dx
    i0 = np.floor(xp).astype(np.int64) % N
    f = xp - np.floor(xp)
    wx0, wy0, wz0 = 1.0 - f[:, 0], 1.0 - f[:, 1], 1.0 - f[:, 2]
    wx1, wy1, wz1 = f[:, 0], f[:, 1], f[:, 2]
    ix0, iy0, iz0 = i0[:, 0], i0[:, 1], i0[:, 2]
    ix1, iy1, iz1 = (ix0 + 1) % N, (iy0 + 1) % N, (iz0 + 1) % N

    np.add.at(rho, (ix0, iy0, iz0), wx0 * wy0 * wz0)
    np.add.at(rho, (ix1, iy0, iz0), wx1 * wy0 * wz0)
    np.add.at(rho, (ix0, iy1, iz0), wx0 * wy1 * wz0)
    np.add.at(rho, (ix0, iy0, iz1), wx0 * wy0 * wz1)
    np.add.at(rho, (ix1, iy1, iz0), wx1 * wy1 * wz0)
    np.add.at(rho, (ix1, iy0, iz1), wx1 * wy0 * wz1)
    np.add.at(rho, (ix0, iy1, iz1), wx0 * wy1 * wz1)
    np.add.at(rho, (ix1, iy1, iz1), wx1 * wy1 * wz1)
    rho /= dx**3
    return rho


def cic_gather_3d(pos, grid, N, L):
    dx = L / N
    xp = pos / dx
    i0 = np.floor(xp).astype(np.int64) % N
    f = xp - np.floor(xp)
    wx0, wy0, wz0 = 1.0 - f[:, 0], 1.0 - f[:, 1], 1.0 - f[:, 2]
    wx1, wy1, wz1 = f[:, 0], f[:, 1], f[:, 2]
    ix0, iy0, iz0 = i0[:, 0], i0[:, 1], i0[:, 2]
    ix1, iy1, iz1 = (ix0 + 1) % N, (iy0 + 1) % N, (iz0 + 1) % N

    val = (
        grid[ix0, iy0, iz0] * (wx0 * wy0 * wz0)
        + grid[ix1, iy0, iz0] * (wx1 * wy0 * wz0)
        + grid[ix0, iy1, iz0] * (wx0 * wy1 * wz0)
        + grid[ix0, iy0, iz1] * (wx0 * wy0 * wz1)
        + grid[ix1, iy1, iz0] * (wx1 * wy1 * wz0)
        + grid[ix1, iy0, iz1] * (wx1 * wy0 * wz1)
        + grid[ix0, iy1, iz1] * (wx0 * wy1 * wz1)
        + grid[ix1, iy1, iz1] * (wx1 * wy1 * wz1)
    )
    return val


def solve_potential_comoving(rho, rho_bg, a, N, L, G):
    dx = L / N
    delta_rho = rho - rho_bg
    rho_k = np.fft.rfftn(delta_rho)
    kx = 2.0 * np.pi * np.fft.fftfreq(N, d=dx)
    ky = 2.0 * np.pi * np.fft.fftfreq(N, d=dx)
    kz = 2.0 * np.pi * np.fft.rfftfreq(N, d=dx)
    k2 = (kx[:, None, None] ** 2) + (ky[None, :, None] ** 2) + (kz[None, None, :] ** 2)
    k2[0, 0, 0] = 1.0
    phi_k = -4.0 * np.pi * G * a**2 * rho_k / k2
    phi_k[0, 0, 0] = 0.0
    return np.fft.irfftn(phi_k, s=(N, N, N))


def accel_from_phi(phi, N, L):
    dx = L / N
    dphix = (np.roll(phi, -1, axis=0) - np.roll(phi, 1, axis=0)) / (2.0 * dx)
    dphiy = (np.roll(phi, -1, axis=1) - np.roll(phi, 1, axis=1)) / (2.0 * dx)
    dphiz = (np.roll(phi, -1, axis=2) - np.roll(phi, 1, axis=2)) / (2.0 * dx)
    return -dphix, -dphiy, -dphiz


def compute_velocity_divergence(vel, pos, N, L):
    dx = L / N
    vx_grid = np.zeros((N, N, N))
    vy_grid = np.zeros((N, N, N))
    vz_grid = np.zeros((N, N, N))
    count_grid = np.zeros((N, N, N))

    xp = pos / dx
    i0 = np.floor(xp).astype(np.int64) % N
    f = xp - np.floor(xp)
    wx0, wy0, wz0 = 1.0 - f[:, 0], 1.0 - f[:, 1], 1.0 - f[:, 2]
    wx1, wy1, wz1 = f[:, 0], f[:, 1], f[:, 2]
    ix0, iy0, iz0 = i0[:, 0], i0[:, 1], i0[:, 2]
    ix1, iy1, iz1 = (ix0 + 1) % N, (iy0 + 1) % N, (iz0 + 1) % N

    for grid, comp in [(vx_grid, 0), (vy_grid, 1), (vz_grid, 2)]:
        np.add.at(grid, (ix0, iy0, iz0), vel[:, comp] * wx0 * wy0 * wz0)
        np.add.at(grid, (ix1, iy0, iz0), vel[:, comp] * wx1 * wy0 * wz0)
        np.add.at(grid, (ix0, iy1, iz0), vel[:, comp] * wx0 * wy1 * wz0)
        np.add.at(grid, (ix0, iy0, iz1), vel[:, comp] * wx0 * wy0 * wz1)
        np.add.at(grid, (ix1, iy1, iz0), vel[:, comp] * wx1 * wy1 * wz0)
        np.add.at(grid, (ix1, iy0, iz1), vel[:, comp] * wx1 * wy0 * wz1)
        np.add.at(grid, (ix0, iy1, iz1), vel[:, comp] * wx0 * wy1 * wz1)
        np.add.at(grid, (ix1, iy1, iz1), vel[:, comp] * wx1 * wy1 * wz1)

    np.add.at(count_grid, (ix0, iy0, iz0), wx0 * wy0 * wz0)
    np.add.at(count_grid, (ix1, iy0, iz0), wx1 * wy0 * wz0)
    np.add.at(count_grid, (ix0, iy1, iz0), wx0 * wy1 * wz0)
    np.add.at(count_grid, (ix0, iy0, iz1), wx0 * wy0 * wz1)
    np.add.at(count_grid, (ix1, iy1, iz0), wx1 * wy1 * wz0)
    np.add.at(count_grid, (ix1, iy0, iz1), wx1 * wy0 * wz1)
    np.add.at(count_grid, (ix0, iy1, iz1), wx0 * wy1 * wz1)
    np.add.at(count_grid, (ix1, iy1, iz1), wx1 * wy1 * wz1)

    mask = count_grid > 0
    vx_grid[mask] /= count_grid[mask]
    vy_grid[mask] /= count_grid[mask]
    vz_grid[mask] /= count_grid[mask]

    dvx_dx = (np.roll(vx_grid, -1, axis=0) - np.roll(vx_grid, 1, axis=0)) / (2.0 * dx)
    dvy_dy = (np.roll(vy_grid, -1, axis=1) - np.roll(vy_grid, 1, axis=1)) / (2.0 * dx)
    dvz_dz = (np.roll(vz_grid, -1, axis=2) - np.roll(vz_grid, 1, axis=2)) / (2.0 * dx)
    return dvx_dx + dvy_dy + dvz_dz


def quantile_masks(M_bar, q_lo, q_hi):
    lo = np.percentile(M_bar, q_lo)
    hi = np.percentile(M_bar, q_hi)
    return M_bar <= lo, M_bar >= hi, lo, hi


def periodic_delta(a, b, L):
    d = a - b
    return (d + 0.5 * L) % L - 0.5 * L


def bound_fraction_proxy(pos_c, vel_c, L, a, G=1.0, eps=0.05):
    n = pos_c.shape[0]
    com = pos_c.mean(axis=0)
    vcom = vel_c.mean(axis=0)
    r = periodic_delta(pos_c, com[None, :], L)
    vrel = vel_c - vcom[None, :]
    KE = 0.5 * np.sum(vrel**2, axis=1)
    phi = np.zeros(n, dtype=np.float64)
    for i in range(n):
        dr = r[i][None, :] - r
        dr2 = np.sum(dr**2, axis=1) + eps**2
        inv = 1.0 / np.sqrt(dr2)
        inv[i] = 0.0
        phi[i] = -G * a**2 * np.sum(inv)
    E = KE + phi
    bf = float((E < 0.0).mean())
    sigma_v = float(np.sqrt(np.mean(np.sum(vrel**2, axis=1))))
    r_rms = float(np.sqrt(np.mean(np.sum(r**2, axis=1))))
    return bf, r_rms, sigma_v


def save_slices(step, a, rho, M, M_bar, div_v, mask_void, mask_fil, out_prefix):
    mid = rho.shape[2] // 2
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    im = axes[0, 0].imshow(np.log10(rho[:, :, mid] + 1e-12), origin="lower", cmap="viridis")
    axes[0, 0].set_title(f"log10(rho) step={step} a={a:.3f}")
    plt.colorbar(im, ax=axes[0, 0])
    im = axes[0, 1].imshow(np.log10(M[:, :, mid] + 1e-12), origin="lower", cmap="viridis")
    axes[0, 1].set_title("log10(M)")
    plt.colorbar(im, ax=axes[0, 1])
    im = axes[0, 2].imshow(np.log10(M_bar[:, :, mid] + 1e-12), origin="lower", cmap="viridis")
    axes[0, 2].set_title("log10(M_bar)")
    plt.colorbar(im, ax=axes[0, 2])
    im = axes[1, 0].imshow(div_v[:, :, mid], origin="lower", cmap="RdBu_r", vmin=-np.abs(div_v).max(), vmax=np.abs(div_v).max())
    axes[1, 0].set_title("div(v)")
    plt.colorbar(im, ax=axes[1, 0])
    mask_img = np.zeros_like(M_bar[:, :, mid])
    mask_img[mask_void[:, :, mid]] = 0.2
    mask_img[mask_fil[:, :, mid]] = 0.9
    im = axes[1, 1].imshow(mask_img, origin="lower", cmap="coolwarm", vmin=0, vmax=1)
    axes[1, 1].set_title("environment masks")
    plt.colorbar(im, ax=axes[1, 1])
    delta = rho / (rho.mean() + 1e-12) - 1
    im = axes[1, 2].imshow(delta[:, :, mid], origin="lower", cmap="RdBu_r", vmin=-2, vmax=5)
    axes[1, 2].set_title("delta")
    plt.colorbar(im, ax=axes[1, 2])
    plt.tight_layout()
    plt.savefig(f"{out_prefix}_fields_step{step:05d}.png", dpi=150)
    plt.close()


def run():
    rng = np.random.default_rng(P.seed)
    pos = rng.uniform(0, P.L, size=(P.N_part, 3))
    vel = np.zeros_like(pos)
    slab = (pos[:, 0] > 0.45 * P.L) & (pos[:, 0] < 0.55 * P.L)
    vel[slab] += rng.normal(0, 0.01, size=(slab.sum(), 3))

    clump_ids = []
    pos_clumps = []
    vel_clumps = []
    centers = rng.uniform(0, P.L, size=(P.N_clumps, 3))
    for ci in range(P.N_clumps):
        c = centers[ci]
        pc = (c[None, :] + rng.normal(0, P.clump_sigma_pos, size=(P.clump_size, 3))) % P.L
        vc = rng.normal(0, P.clump_sigma_vel, size=(P.clump_size, 3))
        pos_clumps.append(pc)
        vel_clumps.append(vc)
        clump_ids.append(np.full(P.clump_size, ci, dtype=np.int64))

    pos_clumps = np.vstack(pos_clumps)
    vel_clumps = np.vstack(vel_clumps)
    clump_ids = np.concatenate(clump_ids)
    pos = np.vstack([pos, pos_clumps])
    vel = np.vstack([vel, vel_clumps])
    clump_indices = [np.where(clump_ids == ci)[0] + P.N_part for ci in range(P.N_clumps)]

    M = np.zeros((P.N, P.N, P.N), dtype=np.float64)
    M_bar = np.zeros_like(M)
    kernel = make_gaussian_kernel(P.N, P.kernel_sigma)
    kernel = np.fft.ifftshift(kernel)
    kernel_fft = np.fft.rfftn(kernel)
    a = P.a_init
    rho_bg = pos.shape[0] / P.L**3
    dwarf_rows = []
    snap_rows = []

    for step in range(P.n_steps):
        H_conf = conformal_hubble(a, P.H0, P.Omega_m, P.Omega_L)
        H_phys = hubble(a, P.H0, P.Omega_m, P.Omega_L)
        rho = cic_deposit_3d(pos, P.N, P.L)
        M, _ = update_memory_kernel(M, rho, P.dt_conf, P.tau_memory, P.eta, kernel_fft, P.delta_c)
        M_bar = (1.0 - P.beta_mbar) * M_bar + P.beta_mbar * M
        mask_void, mask_fil, lo_thr, hi_thr = quantile_masks(M_bar, P.q_lo, P.q_hi)
        rho_eff = rho + P.alpha_core * saturating_fM(M, P.M_sat)
        phi = solve_potential_comoving(rho_eff, rho_bg, a, P.N, P.L, P.G)
        axg, ayg, azg = accel_from_phi(phi, P.N, P.L)
        ax = cic_gather_3d(pos, axg, P.N, P.L)
        ay = cic_gather_3d(pos, ayg, P.N, P.L)
        az = cic_gather_3d(pos, azg, P.N, P.L)
        acc = np.stack([ax, ay, az], axis=1)

        vel += 0.5 * P.dt_conf * (acc - H_conf * vel)
        pos = (pos + P.dt_conf * vel) % P.L
        a += a * H_conf * P.dt_conf

        rho2 = cic_deposit_3d(pos, P.N, P.L)
        rho2_eff = rho2 + P.alpha_core * saturating_fM(M, P.M_sat)
        phi2 = solve_potential_comoving(rho2_eff, rho_bg, a, P.N, P.L, P.G)
        axg, ayg, azg = accel_from_phi(phi2, P.N, P.L)
        ax = cic_gather_3d(pos, axg, P.N, P.L)
        ay = cic_gather_3d(pos, ayg, P.N, P.L)
        az = cic_gather_3d(pos, azg, P.N, P.L)
        acc2 = np.stack([ax, ay, az], axis=1)
        H_conf2 = conformal_hubble(a, P.H0, P.Omega_m, P.Omega_L)
        vel += 0.5 * P.dt_conf * (acc2 - H_conf2 * vel)

        div_v = compute_velocity_divergence(vel, pos, P.N, P.L)
        div_void = float(div_v[mask_void].mean()) if mask_void.any() else 0.0
        div_fil = float(div_v[mask_fil].mean()) if mask_fil.any() else 0.0
        dH_void = div_void / (3.0 * a) if a > 0 else 0.0
        dH_fil = div_fil / (3.0 * a) if a > 0 else 0.0
        H_void_local = H_phys + dH_void
        H_fil_local = H_phys + dH_fil

        if step % P.snap_every == 0:
            coms = np.zeros((P.N_clumps, 3), dtype=np.float64)
            for ci in range(P.N_clumps):
                idx = clump_indices[ci]
                coms[ci] = pos[idx].mean(axis=0)
            local_M = cic_gather_3d(coms, M_bar, P.N, P.L)
            save_slices(step, a, rho2, M, M_bar, div_v, mask_void, mask_fil, P.out_prefix)
            snap_rows.append([step, float(a), float(M.max()), float(M.mean()), float(lo_thr), float(hi_thr), float(H_phys), float(dH_void), float(dH_fil), float(H_void_local), float(H_fil_local)])
            do_bind = step % P.bind_every == 0
            for ci in range(P.N_clumps):
                idx = clump_indices[ci]
                bf = np.nan
                r_rms = np.nan
                sigv = np.nan
                if do_bind:
                    bf, r_rms, sigv = bound_fraction_proxy(pos[idx], vel[idx], P.L, a, G=P.G, eps=P.softening)
                env = "void" if local_M[ci] <= lo_thr else ("fil" if local_M[ci] >= hi_thr else "mid")
                dwarf_rows.append([step, ci, float(coms[ci, 0]), float(coms[ci, 1]), float(coms[ci, 2]), float(local_M[ci]), env, float(bf), float(r_rms), float(sigv)])
            print(f"step {step:5d} | a={a:.3f} | Mmax={M.max():.3e} | H_bg={H_phys:.4f} | dH_v={dH_void:+.4f} dH_f={dH_fil:+.4f}")

    snap_rows = np.array(snap_rows, dtype=np.float64)
    np.savetxt(f"{P.out_prefix}_snapshots.csv", snap_rows, delimiter=",", header="step,a,M_max,M_mean,Mbar_qlo,Mbar_qhi,H_bg,dH_void,dH_fil,H_void_local,H_fil_local", comments="")
    with open(f"{P.out_prefix}_dwarfs.csv", "w", encoding="utf-8") as f:
        f.write("step,clump_id,com_x,com_y,com_z,local_Mbar,env,bound_frac,r_rms,sigma_v\n")
        for row in dwarf_rows:
            step, ci, cx, cy, cz, lm, env, bf, r_rms, sigv = row
            f.write(f"{int(step)},{int(ci)},{cx:.6f},{cy:.6f},{cz:.6f},{lm:.6e},{env},{bf},{r_rms},{sigv}\n")


if __name__ == "__main__":
    run()
