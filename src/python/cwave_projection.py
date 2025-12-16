from __future__ import annotations
import numpy as np
from fft_config import FFTConfig

def make_Kz(cfg: FFTConfig) -> np.ndarray:
    """
    K(z) = exp(-alpha z^2), normalized over discrete z
    """
    z = (np.arange(cfg.nz) - cfg.nz/2) * cfg.dz
    K = np.exp(-cfg.alpha_z * (z**2))
    K = K / (K.sum() + 1e-12)
    return K.astype(np.float64)

def project_f(Psi: np.ndarray, cfg: FFTConfig) -> np.ndarray:
    """
    C(x,y) = ∫ K(z) Ψ(x,y,z) dz  (discrete sum)
    """
    Kz = make_Kz(cfg)  # (nz,)
    # tensordot over z axis
    C = np.tensordot(Psi, Kz, axes=([2], [0]))  # (nx, ny)
    return C

def intensity(C: np.ndarray) -> np.ndarray:
    return C * C.conj()

if __name__ == "__main__":
    # quick smoke test
    cfg = FFTConfig()
    Psi = np.random.default_rng(cfg.seed).normal(0, 1, size=(cfg.nx, cfg.ny, cfg.nz))
    C = project_f(Psi, cfg)
    print("C shape:", C.shape, "mean:", float(C.mean()))