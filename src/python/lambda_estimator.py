from __future__ import annotations
import numpy as np
from fft_config import FFTConfig
from operators import grad_norm2

def estimate_lambda_from_psi(psi: np.ndarray, cfg: FFTConfig, alpha_DE: float = 1.0) -> float:
    """
    Λ = 8πG α_DE < ||∇ψ||^2 >_cosmic
    ここでは 8πG を 1 に吸収した toy estimator.
    """
    g2 = grad_norm2(psi, cfg.dx, cfg.dy, cfg.dz)
    return float(alpha_DE * g2.mean())

def estimate_dark_energy_density(psi: np.ndarray, cfg: FFTConfig, alpha_DE: float = 1.0) -> float:
    """
    ρ_DE = α_DE <||∇ψ||^2>
    """
    g2 = grad_norm2(psi, cfg.dx, cfg.dy, cfg.dz)
    return float(alpha_DE * g2.mean())

if __name__ == "__main__":
    cfg = FFTConfig()
    psi = np.random.default_rng(cfg.seed).normal(0, 1, size=(cfg.nx, cfg.ny, cfg.nz))
    lam = estimate_lambda_from_psi(psi, cfg, alpha_DE=1.0)
    print("Lambda_est:", lam)