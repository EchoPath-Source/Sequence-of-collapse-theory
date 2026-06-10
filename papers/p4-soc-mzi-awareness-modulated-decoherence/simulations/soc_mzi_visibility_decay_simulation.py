"""
Sequence of Collapse (SOC) - MZI Visibility Decay Simulation
============================================================

Phenomenological simulation scaffold for the SOC-MZI program.

This script models visibility decay in a Mach-Zehnder interferometer under a
rate-law extension of the form:

    lambda_eff = lambda_env + lambda_c * A(t)
    V(tau, A) = V0 * exp[-lambda_eff * tau]

Important boundary:
- This script is not experimental evidence.
- It is a design and falsification scaffold for expected signatures.
- Outputs should be interpreted as simulation-informed planning assumptions.

Implemented qualitative signatures:
1. Main effect: higher A -> lower residual visibility at fixed delay
2. Timing asymmetry: early windows suppress more strongly than late windows
3. Dose response: visibility decreases monotonically with A
4. Shot-noise-limited measurement emulation

Repository context:
- P4 preregistration protocol
- MZI model summary
- materials and measures appendix
- statistical analysis plan

License: CC-BY-4.0
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import csv
import math
from typing import Dict, Tuple

import numpy as np
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
# Configuration
# -----------------------------------------------------------------------------

SEED = 42
RNG = np.random.default_rng(SEED)


@dataclass(frozen=True)
class SimConfig:
    lambda_env: float = 0.02          # 1 / microsecond
    lambda_c: float = 0.015           # free coupling coefficient
    v0: float = 0.90                  # baseline visibility
    n_photons: int = 5000             # photons per visibility estimate
    early_factor: float = 1.15        # longer effective exposure
    late_factor: float = 0.85         # shorter effective exposure
    a_low: float = 0.20
    a_high: float = 0.80
    delays_us: Tuple[float, ...] = (10.0, 20.0, 40.0, 80.0)
    a_grid_points: int = 11
    output_dir: str = "results"


CONFIG = SimConfig()


# -----------------------------------------------------------------------------
# Core model
# -----------------------------------------------------------------------------


def effective_rate(a_value: np.ndarray | float, config: SimConfig = CONFIG) -> np.ndarray | float:
    """Return the effective decoherence rate for a given awareness value."""
    return config.lambda_env + config.lambda_c * a_value



def visibility_decay(
    tau_us: np.ndarray | float,
    a_value: np.ndarray | float,
    config: SimConfig = CONFIG,
) -> np.ndarray | float:
    """
    Phenomenological visibility model.

    V(tau, A) = V0 * exp[-lambda_eff * tau]
    """
    lam_eff = effective_rate(a_value, config)
    return config.v0 * np.exp(-lam_eff * tau_us)



def timing_modulation(tau_us: np.ndarray | float, timing: str, config: SimConfig = CONFIG) -> np.ndarray | float:
    """Apply a simple early/late effective exposure modifier."""
    if timing == "early":
        return tau_us * config.early_factor
    if timing == "late":
        return tau_us * config.late_factor
    return tau_us



def add_shot_noise(true_visibility: np.ndarray, n_photons: int, rng: np.random.Generator = RNG) -> np.ndarray:
    """
    Add approximate shot-noise-limited measurement error.

    sigma_V ≈ sqrt(2 * V / N)
    """
    sigma_v = np.sqrt(np.clip(2.0 * true_visibility / n_photons, 0.0, None))
    measured = true_visibility + rng.normal(0.0, sigma_v, size=true_visibility.shape)
    return np.clip(measured, 0.0, 1.0)


# -----------------------------------------------------------------------------
# Simulation blocks
# -----------------------------------------------------------------------------


def simulate_main_effect(config: SimConfig = CONFIG) -> Dict[str, np.ndarray]:
    """Simulate visibility under low-A and high-A conditions."""
    delays = np.array(config.delays_us, dtype=float)
    v_low_true = visibility_decay(delays, config.a_low, config)
    v_high_true = visibility_decay(delays, config.a_high, config)
    v_low_meas = add_shot_noise(v_low_true, config.n_photons)
    v_high_meas = add_shot_noise(v_high_true, config.n_photons)
    delta_v = v_low_meas - v_high_meas
    return {
        "delay_us": delays,
        "v_low_true": v_low_true,
        "v_high_true": v_high_true,
        "v_low_meas": v_low_meas,
        "v_high_meas": v_high_meas,
        "delta_v": delta_v,
    }



def simulate_timing_asymmetry(config: SimConfig = CONFIG) -> Dict[str, np.ndarray]:
    """Simulate early/late timing asymmetry under high awareness."""
    delays = np.array(config.delays_us, dtype=float)
    tau_early = timing_modulation(delays, "early", config)
    tau_late = timing_modulation(delays, "late", config)
    v_early_true = visibility_decay(tau_early, config.a_high, config)
    v_late_true = visibility_decay(tau_late, config.a_high, config)
    v_early_meas = add_shot_noise(v_early_true, config.n_photons)
    v_late_meas = add_shot_noise(v_late_true, config.n_photons)
    delta_timing = v_late_meas - v_early_meas
    return {
        "delay_us": delays,
        "tau_early": tau_early,
        "tau_late": tau_late,
        "v_early_true": v_early_true,
        "v_late_true": v_late_true,
        "v_early_meas": v_early_meas,
        "v_late_meas": v_late_meas,
        "delta_timing": delta_timing,
    }



def simulate_dose_response(config: SimConfig = CONFIG) -> Dict[str, np.ndarray | float]:
    """Simulate visibility across a continuous A grid at a fixed representative delay."""
    a_values = np.linspace(0.0, 1.0, config.a_grid_points)
    representative_delay = 40.0
    v_true = visibility_decay(representative_delay, a_values, config)
    v_meas = add_shot_noise(v_true, config.n_photons)

    # Spearman rank correlation without scipy.
    a_ranks = np.argsort(np.argsort(a_values)).astype(float)
    v_ranks = np.argsort(np.argsort(v_meas)).astype(float)
    rho = np.corrcoef(a_ranks, v_ranks)[0, 1]

    # Linear least-squares slope.
    slope, intercept = np.polyfit(a_values, v_meas, 1)
    fitted = slope * a_values + intercept

    return {
        "a_values": a_values,
        "delay_us": representative_delay,
        "v_true": v_true,
        "v_meas": v_meas,
        "slope": slope,
        "intercept": intercept,
        "rho_spearman": rho,
        "fitted": fitted,
    }


# -----------------------------------------------------------------------------
# Reporting helpers
# -----------------------------------------------------------------------------


def print_main_effect(results: Dict[str, np.ndarray], config: SimConfig = CONFIG) -> None:
    print("\n=== H1a: Main Effect Test ===")
    print(f"lambda_env={config.lambda_env:.4f}, lambda_c={config.lambda_c:.4f}")
    print(f"A_low={config.a_low:.2f}, A_high={config.a_high:.2f}")
    print("delay_us | V_low(meas) | V_high(meas) | DeltaV")
    for tau, v_low, v_high, dv in zip(
        results["delay_us"],
        results["v_low_meas"],
        results["v_high_meas"],
        results["delta_v"],
    ):
        print(f"{tau:7.1f} | {v_low:11.4f} | {v_high:12.4f} | {dv:6.4f}")



def print_timing_asymmetry(results: Dict[str, np.ndarray]) -> None:
    print("\n=== H1b: Timing Asymmetry Test ===")
    print("delay_us | V_early(meas) | V_late(meas) | Late-Early")
    for tau, v_e, v_l, dt in zip(
        results["delay_us"],
        results["v_early_meas"],
        results["v_late_meas"],
        results["delta_timing"],
    ):
        print(f"{tau:7.1f} | {v_e:13.4f} | {v_l:12.4f} | {dt:10.4f}")



def print_dose_response(results: Dict[str, np.ndarray | float]) -> None:
    print("\n=== H1c: Dose Response Test ===")
    print(f"Representative delay: {results['delay_us']:.1f} us")
    print(f"Linear slope dV/dA: {results['slope']:.6f}")
    print(f"Spearman rho(A, V): {results['rho_spearman']:.6f}")


# -----------------------------------------------------------------------------
# Persistence
# -----------------------------------------------------------------------------


def ensure_output_dir(path_str: str) -> Path:
    path = Path(path_str)
    path.mkdir(parents=True, exist_ok=True)
    return path



def save_main_effect_csv(results: Dict[str, np.ndarray], output_dir: Path) -> Path:
    path = output_dir / "main_effect.csv"
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["delay_us", "v_low_true", "v_high_true", "v_low_meas", "v_high_meas", "delta_v"])
        for row in zip(
            results["delay_us"],
            results["v_low_true"],
            results["v_high_true"],
            results["v_low_meas"],
            results["v_high_meas"],
            results["delta_v"],
        ):
            writer.writerow(row)
    return path



def save_timing_csv(results: Dict[str, np.ndarray], output_dir: Path) -> Path:
    path = output_dir / "timing_asymmetry.csv"
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["delay_us", "tau_early", "tau_late", "v_early_true", "v_late_true", "v_early_meas", "v_late_meas", "late_minus_early"])
        for row in zip(
            results["delay_us"],
            results["tau_early"],
            results["tau_late"],
            results["v_early_true"],
            results["v_late_true"],
            results["v_early_meas"],
            results["v_late_meas"],
            results["delta_timing"],
        ):
            writer.writerow(row)
    return path



def save_dose_response_csv(results: Dict[str, np.ndarray | float], output_dir: Path) -> Path:
    path = output_dir / "dose_response.csv"
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["a_value", "v_true", "v_meas", "fitted"])
        for row in zip(results["a_values"], results["v_true"], results["v_meas"], results["fitted"]):
            writer.writerow(row)
    return path


# -----------------------------------------------------------------------------
# Plotting
# -----------------------------------------------------------------------------


def make_main_effect_plot(results: Dict[str, np.ndarray], output_dir: Path) -> Path:
    path = output_dir / "main_effect.png"
    plt.figure(figsize=(8, 5))
    plt.plot(results["delay_us"], results["v_low_meas"], marker="o", label="Low A")
    plt.plot(results["delay_us"], results["v_high_meas"], marker="s", label="High A")
    plt.xlabel("Delay (microseconds)")
    plt.ylabel("Measured visibility")
    plt.title("SOC-MZI Main Effect Simulation")
    plt.legend()
    plt.tight_layout()
    plt.savefig(path, dpi=180)
    plt.close()
    return path



def make_timing_plot(results: Dict[str, np.ndarray], output_dir: Path) -> Path:
    path = output_dir / "timing_asymmetry.png"
    plt.figure(figsize=(8, 5))
    plt.plot(results["delay_us"], results["v_early_meas"], marker="o", label="Early")
    plt.plot(results["delay_us"], results["v_late_meas"], marker="s", label="Late")
    plt.xlabel("Nominal delay (microseconds)")
    plt.ylabel("Measured visibility")
    plt.title("SOC-MZI Timing Asymmetry Simulation")
    plt.legend()
    plt.tight_layout()
    plt.savefig(path, dpi=180)
    plt.close()
    return path



def make_dose_response_plot(results: Dict[str, np.ndarray | float], output_dir: Path) -> Path:
    path = output_dir / "dose_response.png"
    plt.figure(figsize=(8, 5))
    plt.scatter(results["a_values"], results["v_meas"], label="Measured")
    plt.plot(results["a_values"], results["fitted"], label="Linear fit")
    plt.xlabel("A(t)")
    plt.ylabel("Measured visibility")
    plt.title("SOC-MZI Dose Response Simulation")
    plt.legend()
    plt.tight_layout()
    plt.savefig(path, dpi=180)
    plt.close()
    return path


# -----------------------------------------------------------------------------
# Main entrypoint
# -----------------------------------------------------------------------------


def main() -> None:
    output_dir = ensure_output_dir(CONFIG.output_dir)

    main_effect = simulate_main_effect(CONFIG)
    timing = simulate_timing_asymmetry(CONFIG)
    dose = simulate_dose_response(CONFIG)

    print_main_effect(main_effect, CONFIG)
    print_timing_asymmetry(timing)
    print_dose_response(dose)

    files_written = [
        save_main_effect_csv(main_effect, output_dir),
        save_timing_csv(timing, output_dir),
        save_dose_response_csv(dose, output_dir),
        make_main_effect_plot(main_effect, output_dir),
        make_timing_plot(timing, output_dir),
        make_dose_response_plot(dose, output_dir),
    ]

    print("\nWrote outputs:")
    for path in files_written:
        print(f"- {path}")

    print("\nInterpretation boundary:")
    print("These results are simulation-informed expected signatures, not empirical evidence.")


if __name__ == "__main__":
    main()
