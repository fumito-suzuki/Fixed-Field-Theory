from __future__ import annotations
import numpy as np

Array = np.ndarray

def grad3(f: Array, dx: float, dy: float, dz: float):
    # periodic finite differences (toy)
    dfx = (np.roll(f, -1, axis=0) - np.roll(f, 1, axis=0)) / (2*dx)
    dfy = (np.roll(f, -1, axis=1) - np.roll(f, 1, axis=1)) / (2*dy)
    dfz = (np.roll(f, -1, axis=2) - np.roll(f, 1, axis=2)) / (2*dz)
    return dfx, dfy, dfz

def laplacian3(f: Array, dx: float, dy: float, dz: float) -> Array:
    return (
        (np.roll(f, -1, axis=0) - 2*f + np.roll(f, 1, axis=0)) / (dx*dx) +
        (np.roll(f, -1, axis=1) - 2*f + np.roll(f, 1, axis=1)) / (dy*dy) +
        (np.roll(f, -1, axis=2) - 2*f + np.roll(f, 1, axis=2)) / (dz*dz)
    )

def chi_operator(Psi: Array, dz: float, alpha_z: float = 1.0, alpha_0: float = 0.0) -> Array:
    """
    χ operator (toy):
      χΨ = alpha_z * ∂zΨ + alpha_0 * Ψ
    """
    dPsi_dz = (np.roll(Psi, -1, axis=2) - np.roll(Psi, 1, axis=2)) / (2*dz)
    return alpha_z * dPsi_dz + alpha_0 * Psi

def delta_operator(Psi: Array, dx: float, dy: float,
                   beta_xy: float = 1.0, beta_0: float = 0.0) -> Array:
    """
    δ operator (toy minimal):
      δΨ = beta_xy * ||∇xy Ψ|| + beta_0 * Ψ
    ※本来は回転/スケール混合も入るが、まずは“干渉密度”の最小表現として。
    """
    dPsi_dx = (np.roll(Psi, -1, axis=0) - np.roll(Psi, 1, axis=0)) / (2*dx)
    dPsi_dy = (np.roll(Psi, -1, axis=1) - np.roll(Psi, 1, axis=1)) / (2*dy)
    return beta_xy * np.sqrt(dPsi_dx*dPsi_dx + dPsi_dy*dPsi_dy + 1e-12) + beta_0 * Psi

def psi_from_chidelta(chi: Array, delta: Array) -> Array:
    return chi * delta

def grad_norm2(f: Array, dx: float, dy: float, dz: float) -> Array:
    dfx, dfy, dfz = grad3(f, dx, dy, dz)
    return dfx*dfx + dfy*dfy + dfz*dfz