from dataclasses import dataclass

@dataclass(frozen=True)
class FFTConfig:
    # Grid
    nx: int = 128
    ny: int = 128
    nz: int = 96
    dx: float = 1.0
    dy: float = 1.0
    dz: float = 1.0

    # Time stepping
    dt: float = 0.01
    steps: int = 200

    # Sora parameters (toy defaults)
    omega0p: float = 0.02   # ω0'
    D: float = 0.15         # diffusion
    kappa: float = 0.08     # nonlinear steepening
    xi_sigma: float = 0.01  # noise strength

    # Projection kernel K(z) = exp(-alpha z^2) (toy)
    alpha_z: float = 0.002

    # Effective propagation speed for tau delay (toy)
    c_eff: float = 20.0

    # Random seed
    seed: int = 42
