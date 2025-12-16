# src/python — Minimal Computability Layer (Toy)

This folder provides **example realizations** of FFT dynamics for
**computability and falsifiability entrypoints**.

IMPORTANT NOTES

- FFT does **not** introduce `N` or `J` as fundamental quantities.
- Multiplicity and flux are derived geometric consequences of χδ interaction.
- χ and δ are computed as derived operators acting on Ψ.
- ψ = χδ is evolved via the Sora Equation (toy discretization).
- Observation is implemented explicitly as a projection operator
  `f : Ψ → C` with a kernel `K(z)`.

This code is intentionally **minimal and falsifiable**,
not a claim of final physical accuracy.

---

## Quick Start

Run each component independently:

    python simulate_twave.py
    python cwave_projection.py
    python lambda_estimator.py

All scripts are self-contained and use toy parameter values defined in
`fft_config.py`.

---

## File Overview

### fft_config.py

Centralized configuration:

- grid size and spacing
- time step and iteration count
- Sora equation parameters
- projection kernel parameters

---

### simulate_twave.py

Minimal **ψ-dynamics loop**.

Implements:

- χ-operator (causal depth derivative along Z)
- δ-operator (interference density in XY)
- ψ = χδ (appearance generator)
- Sora equation

Notes:

- `N` and `J` are **not introduced**
- ψ evolves directly as the appearance field
- feedback into Ψ is a placeholder for future FFT-1 closure

---

### cwave_projection.py

Explicit implementation of the **projection operator**:

    C(x,y) = ∫ K(z) Ψ(x,y,z) dz

Where:

- K(z) = exp(-α z²) (normalized)
- C corresponds to C-wave observable
- |C|² is the observable intensity

---

### lambda_estimator.py

Toy estimator for the cosmological constant:

    Λ ∝ ⟨ ||∇ψ||² ⟩

Implements:

- gradient norm calculation
- volume averaging
- explicit numerical output

This file exists to demonstrate **computability and falsifiability**,
not numerical agreement with ΛCDM.