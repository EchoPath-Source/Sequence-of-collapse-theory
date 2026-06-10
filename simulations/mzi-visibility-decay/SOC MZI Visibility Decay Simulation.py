"""
Sequence of Collapse (SOC) - MZI Visibility Decay Simulation
=============================================================

Simulates interference visibility V(τ, A) in a Mach-Zehnder interferometer
with awareness-modulated decoherence rate λ_eff = λ_env + λ_c * A(t).

Key Predictions:
1. V decreases faster with higher A (main effect)
2. Early pulses show stronger suppression than late pulses (timing asymmetry)
3. Effect scales monotonically with A (dose-response)

Author: Echo Mirrowen / Claude
License: CC-BY-4.0
Date: January 2025
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
import seaborn as sns

# Set random seed for reproducibility
np.random.seed(42)
sns.set_style("whitegrid")

# === PARAMETERS ===
# Environmental decoherence rate (standard QM, measured in 1/μs)
LAMBDA_ENV = 0.02  

# Awareness coupling constant (free parameter, to be estimated)
LAMBDA_C = 0.015  

# Baseline visibility (perfect interferometer)
V0 = 0.90

# Delays to test (microseconds)
DELAYS = np.array([10, 20, 40, 80])

# Awareness levels (0 = no attention, 1 = full attention)
A_LOW = 0.2
A_HIGH = 0.8
A_CONTINUOUS = np.linspace(0, 1, 10)

# Number of photons per measurement (shot-noise limited)
N_PHOTONS = 5000

# Timing windows (fraction of trial duration)
EARLY_WINDOW = (0.0, 0.33)  # First third of trial
LATE_WINDOW = (0.67, 1.0)   # Last third of trial


# === CORE MODEL ===
def visibility_decay(tau, A, lambda_env=LAMBDA_ENV, lambda_c=LAMBDA_C, V0=V0):
    """
    Calculate interference visibility with SOC decoherence.
    
    V(τ, A) = V0 * exp(-λ_eff * τ)
    where λ_eff = λ_env + λ_c * A
    
    Parameters:
    -----------
    tau : float or array
        Delay time (μs)
    A : float or array
        Awareness index (0 to 1)
    lambda_env : float
        Environmental decoherence rate
    lambda_c : float
        Awareness coupling constant
    V0 : float
        Baseline visibility
        
    Returns:
    --------
    V : float or array
        Interference visibility
    """
    lambda_eff = lambda_env + lambda_c * A
    return V0 * np.exp(-lambda_eff * tau)


def add_shot_noise(V, N):
    """
    Add Poissonian shot noise to visibility measurements.
    
    σ_V ≈ sqrt(2*V/N)
    
    Parameters:
    -----------
    V : float or array
        True visibility
    N : int
        Number of photons
        
    Returns:
    --------
    V_measured : array
        Visibility with noise
    """
    sigma_V = np.sqrt(2 * V / N)
    return V + np.random.normal(0, sigma_V, size=V.shape)


def timing_modulation(tau, timing='early'):
    """
    Simulate timing asymmetry: early pulses have longer A(t) exposure.
    
    Parameters:
    -----------
    tau : float
        Delay time
    timing : str
        'early' or 'late'
        
    Returns:
    --------
    tau_eff : float
        Effective delay (accounts for A(t) accumulation)
    """
    if timing == 'early':
        # Early pulses: A(t) acts over longer duration
        return tau * 1.15  # 15% longer effective exposure
    elif timing == 'late':
        # Late pulses: A(t) acts over shorter duration
        return tau * 0.85  # 15% shorter effective exposure
    else:
        return tau


# === SIMULATION FUNCTIONS ===
def simulate_main_effect():
    """Test H1a: V(A_low) > V(A_high) at fixed τ"""
    print("\n=== H1a: Main Effect Test ===")
    
    V_low = visibility_decay(DELAYS, A_LOW)
    V_high = visibility_decay(DELAYS, A_HIGH)
    
    # Add shot noise
    V_low_meas = add_shot_noise(V_low, N_PHOTONS)
    V_high_meas = add_shot_noise(V_high, N_PHOTONS)
    
    # Calculate effect size
    delta_V = V_low_meas - V_high_meas
    
    print(f"Awareness: Low={A_LOW}, High={A_HIGH}")
    print(f"λ_env={LAMBDA_ENV}, λ_c={LAMBDA_C}")
    print("\nResults by delay:")
    for i, tau in enumerate(DELAYS):
        print(f"τ={tau}μs: V_low={V_low_meas[i]:.3f}, V_high={V_high_meas[i]")
