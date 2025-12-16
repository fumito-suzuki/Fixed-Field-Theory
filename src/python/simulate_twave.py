from __future__ import annotations
import numpy as np

from fft_config import FFTConfig
from fields import init_state
from operators import (
    chi_operator, delta_operator, psi_from_chidelta,
    laplacian3, grad_norm2
)

def step_sora(psi: np.ndarray, cfg: FFTConfig, rng: np.random.Generator) -> np.ndarray:
    """
    ∂t ψ = ω0' + D Δψ + κ ||∇ψ||^2 + ξ
    Explicit Euler (toy)
    """
    lap = laplacian3(psi, cfg.dx, cfg.dy, cfg.dz)
    g2 = grad_norm2(psi, cfg.dx, cfg.dy, cfg.dz)
    xi = rng.normal(0.0, cfg.xi_sigma, size=psi.shape)
    dpsi = cfg.omega0p + cfg.D * lap + cfg.kappa * g2 + xi
    return psi + cfg.dt * dpsi

def run(cfg: FFTConfig):
    rng = np.random.default_rng(cfg.seed)
    state = init_state((cfg.nx, cfg.ny, cfg.nz), seed=cfg.seed)

    history = {
        "psi_mean": [],
        "grad2_mean": [],
    }

    for t in range(cfg.steps):
        # χ, δ from Ψ (toy closure: derived quantities, not independent N/J)
        state.chi = chi_operator(state.Psi, cfg.dz, alpha_z=1.0, alpha_0=0.0)
        state.delta = delta_operator(state.Psi, cfg.dx, cfg.dy, beta_xy=1.0, beta_0=0.0)

        # ψ = χδ
        state.psi = psi_from_chidelta(state.chi, state.delta)

        # evolve ψ by Sora (toy: treat ψ-dynamics as primary appearance evolution)
        state.psi = step_sora(state.psi, cfg, rng)

        # (optional) feed back to Ψ (toy) so Ψ is not static:
        # Ψ ← Ψ + ε ψ  (this is *not* a claim; just a placeholder for future FFT-1 coupling)
        state.Psi = state.Psi + 0.01 * cfg.dt * state.psi

        history["psi_mean"].append(float(state.psi.mean()))
        history["grad2_mean"].append(float(grad_norm2(state.psi, cfg.dx, cfg.dy, cfg.dz).mean()))

        if (t + 1) % 50 == 0:
            print(f"[{t+1:04d}/{cfg.steps}] mean(psi)={history['psi_mean'][-1]:.6f}")

    return state, history

if __name__ == "__main__":
    cfg = FFTConfig()
    run(cfg)