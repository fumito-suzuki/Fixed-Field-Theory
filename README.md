README

# 🌌 Fixed-Field Theory (FFT)
*A unified geometric field theory connecting quantum mechanics, cosmology, and perception.*



## Overview

**Fixed-Field Theory (FFT)** proposes that physical, cognitive, and cosmological
phenomena all emerge from a single geometric substrate:  
the **T-fiber**, a continuous fractal causal field, together with two interacting modes:

- **T-wave** — continuous, propagating causal flow  
- **C-wave** — discrete, receptor-dependent conceptual interference  

FFT introduces a unifying interaction:

$$
\chi \delta \quad (\text{entangle–expand})
$$

This reflects the classical Buddhist identity:

> **色即是空・空即是色** (“Form is emptiness; emptiness is form.”)

From this geometric mechanism, FFT derives:

- Planck constant  
- Newtonian gravitational constant  
- Cosmological constant λ  
- Quantum entanglement, collapse, and decoherence  
- Perception geometry (2.5D projection)  
- Dark matter / dark energy  
- Temporal emergence (τ-time)  

All **without introducing new particles**.



## ⚠️ Interpretation Notes (Important)

FFT introduces several unconventional concepts that should not be interpreted literally.
The following clarifications prevent common misunderstandings and define the intended
mathematical meaning.

### 1. “Zero-dimensional origin”
FFT does **not** claim the universe is physically 0D.  
This refers to an *unexpanded informational basepoint*—a mathematical origin from which
the T-fiber fractal geometry unfolds.  
It is a **topological basepoint**, not a spatial location.

### 2. “The world is 2D”
Physical space is **not** two-dimensional.  
FFT states:

- Physical reality evolves in 3D within the T-fiber field  
- Perception arises as a **2.5D projection**  
  - XY-plane: instantaneous visual surface  
  - Z-axis: causal delay (past-depth)  

This explains spherical appearance, depth perception, and perspective geometry.

### 3. “Everything is wave”
This is not metaphysics.  
FFT expresses all observable structures as **solutions of PDEs** involving:

- T-wave = continuous causal field  
- C-wave = measurement/conceptual field  

No mystical “energy waves” or new particles are introduced.

### 4. “Time is solid”
“Solid” refers to **phase alignment stability** along τ (emergent time).  
It does **not** imply crystallization.

- T-fiber is **not a lattice**  
- It is a **continuous, fractal causal field**  
- Local phase fixation gives the *appearance* of temporal solidity

This describes stability of causal stacking, not physical solidity.

### 5. “Matter is fluid”
Matter is described as **information-density flow** arising from ψ-gradients
and TC-wave interference.  
It is not a literal fluid; it behaves as a **continuity solution** in FFT.

### 6. “Reality emerges from TC-wave”
This means observable structure is encoded via interacting continuous (T) and
discrete (C) modes.  
It does not imply simulation hypotheses or idealist metaphysics.

Readers should understand these clarifications before interpreting FFT concepts.



## 📁 Repository Structure

The FFT repository is organized into clear layers separating
theory, documentation, equations, numerical experiments, and tools.

``` Repositry Structure
Fixed-Field-Theory/
│
├── docs/
│   └── v1.2.4/
│       ├── FFT-v1.2.4.md          # Main document
│       ├── equations/             # FFT-1/2/3 and derived equations
│       ├── appendices/            # Z-series (Z1–Z37B)
│       ├── figures/               # Diagrams and geometry illustrations
│       └── notes/                 # Research notes and drafts
│
├── src/
│   ├── python/
│   │   ├── simulate_twave.py      # T-wave simulation
│   │   ├── cwave_projection.py    # Observer-side C-wave simulation
│   │   ├── z_fourier_transform.py # Z-axis depth decomposition
│   │   ├── lambda_estimator.py    # Λ-estimation scripts
│   │   └── common/                # Shared utilities
│   │
│   └── latex/
│       └── fft-paper.tex          # Academic paper (arXiv-ready)
│
├── tools/
│   ├── build_pdf.sh               # Build script for LaTeX documents
│   └── validate_equations.py      # Consistency checker
│
├── README.md
├── CONTRIBUTING.md
├── LICENSE
└── .gitignore
```


## Key Contributions (v1.2.4)

### **1. Minimal Equation Set (FFT-1〜3)**

- **FFT-1:** Nonlinear fractal fixed-field equation  
- **FFT-2:** Information-flow equation with fractal currents  
- **FFT-3:** C-wave projected dynamics (XY-plane observer equation)  

These three equations constitute the mathematical backbone of FFT.

### **2. Geometric Origin of Quantum Mechanics**

FFT demonstrates:

- Density operator:

$$
\rho_{\mathrm{QM}} = \mathcal{G}[C] = f^\dagger f
$$

- Entanglement = Z-axis misalignment  
- Teleportation = Z-axis realignment  
- Collapse = minimization of Z-variance  

Low-energy limit reduces to:

$$
\Delta x \, \Delta p \ge \frac{\hbar}{2}
$$

### **3. Cosmology Without New Particles**

FFT provides geometric explanations for:

- Dark matter → suppressed T-fiber tension  
- Dark energy → global relaxation of T-fiber curvature  
- Cosmological constant λ → χδ-driven drift term  
- Expansion → “wire-bundle divergence”（針金実験の幾何対応）

### **4. Perception, Consciousness, Free Will**

Perception is constructed from:

- XZ-plane wave  
- YZ-plane wave  
- Z = causal delay (past-depth layer)

Thus human observation is **2.5-dimensional**.

Consciousness:

$$
\textbf{Consciousness} = \mathcal{G} \circ \Pi_{XY}
$$

Free will:

$$
\rho_{\text{reflected}}
= \arg\min_{\rho \in \mathcal{G}[C]} \mathrm{Var}_Z(\rho)
$$

Representing the ability to **shrink Z-axis causal variance**.



## Documentation (v1.2.4)

- **Main document:** [docs/v1.2.4/FFT-v1.2.4.md](docs/v1.2.4/FFT-v1.2.4.md)
- **Appendices:** [docs/v1.2.4/appendices/](docs/v1.2.4/appendices/)
- **Equations:** [docs/v1.2.4/equations/](docs/v1.2.4/equations/)
- **Figures:** [docs/v1.2.4/figures/](docs/v1.2.4/figures/) 



## Numerical Experiments

Located under `src/python/`:

- `simulate_twave.py` — T-wave simulation  
- `cwave_projection.py` — observer-side C-wave dynamics  
- `z_fourier_transform.py` — Z-axis depth decomposition  
- `lambda_estimator.py` — cosmological constant estimator  

Each script includes detailed headers.



## Citation

If you use FFT in academic work, please cite:

```bibtex
@misc{fft2025,
  title        = {Fixed-Field Theory (FFT): A unified geometric field theory},
  author       = {Suzuki, Fumito},
  year         = {2025},
  url          = {https://github.com/<username>/Fixed-Field-Theory}
}
```



## License

MIT License.



## Contributing

Pull requests are welcome.
Please review CONTRIBUTING.md before contributing.


