from __future__ import annotations
import numpy as np
from dataclasses import dataclass
from typing import Tuple

Array = np.ndarray

@dataclass
class FFTState:
    # Core fields
    Psi: Array   # T-fiber field Ψ(x,y,z)
    chi: Array   # χ(x,y,z)
    delta: Array # δ(x,y,z)
    psi: Array   # ψ(x,y,z) = χδ (appearance generator)

def init_state(shape: Tuple[int,int,int], seed: int = 42) -> FFTState:
    rng = np.random.default_rng(seed)
    nx, ny, nz = shape

    # Start Ψ as smooth + small noise (toy)
    Psi = rng.normal(0.0, 0.05, size=shape).astype(np.float64)
    # Add a gentle blob
    x = np.linspace(-1, 1, nx)[:, None, None]
    y = np.linspace(-1, 1, ny)[None, :, None]
    z = np.linspace(-1, 1, nz)[None, None, :]
    Psi += 0.7 * np.exp(-(x**2 + y**2 + 0.5*z**2) / 0.15)

    # χ, δ initial (toy): derived from Ψ via simple operators later
    chi = np.zeros_like(Psi)
    delta = np.zeros_like(Psi)
    psi = np.zeros_like(Psi)

    return FFTState(Psi=Psi, chi=chi, delta=delta, psi=psi)