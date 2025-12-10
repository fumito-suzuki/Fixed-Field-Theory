# FFT Equations — Master Reference  
This document collects the core equations of Fixed-Field Theory (FFT), including  
the three foundational field equations (FFT-1/2/3) and all essential derived  
relations used throughout the main manuscript and appendices.

---

# 1. FFT-1: The Fundamental Fixed-Field Equation

\[
\hat{\mathcal{S}}_{\mathrm{FFT}}\Psi = 0
\tag{FFT-1}
\]

with operator

\[
\hat{\mathcal{S}}_{\mathrm{FFT}}
=
i\hbar\partial_t
+ D\Delta
+ \ell_D^{\,2-D}\Delta^{D}
- \hat{\Sigma}[\Psi;\rho,C].
\tag{1.1}
\]

### Parameter Notes
- **D** — fractal dimension of diffusion  
- **\(\ell_D\)** — scale parameter for fractal Laplacian  
- **\(\hat{\Sigma}\)** — nonlinear backreaction term  
- **\(\Psi\)** — full T-fiber field (complex)

This is the master evolution law of FFT, reducing to the Schrödinger equation  
when \(D=2\) and \(\hat{\Sigma}=V\Psi\).

---

# 2. FFT-2: Information Density Equation

\[
\partial_t\rho
+ \nabla\cdot\mathbf{J}
+ \mathcal{S}_\rho[\Psi,\rho,C]
= 0
\tag{FFT-2}
\]

where the current is

\[
\mathbf{J}
=
\frac{\hbar}{2mi}
(\Psi^\*\nabla\Psi - \Psi\nabla\Psi^\*)
+
\ell_D^{\,2-D}
\frac{\hbar}{2mi}
(\Psi^\*\nabla^{D}\Psi - \Psi\nabla^{D}\Psi^\*)
+
\rho\,\mathbf{v}_{\mathrm{geo}}.
\tag{2.1}
\]

The source/sink term:

\[
\mathcal{S}_\rho
=
\frac{2}{\hbar}\,
\Im\big[\Psi^\*\hat{\Sigma}\Psi\big]
=
\frac{2}{\hbar}\,
\Im\big[\Psi^\*(\mathcal{N}+\mathcal{J})\Psi\big].
\tag{2.2}
\]

### Interpretation
- **\(\rho\)** is information density, not probability.  
- **J** contains three flows:
  - standard quantum flow  
  - fractal flow  
  - geometric drift  
- **\(\mathcal{S}_\rho\)** expresses creation/annihilation of information density by χδ interactions.

---

# 3. FFT-3: C-wave Projection Equation

\[
i\hbar \partial_t C
=
\Pi_{XY}
\left[
V\Psi
+ \mathcal{N}[\Psi;\rho,C]\Psi
+ \mathcal{J}[\rho,C]\Psi
\right]
\tag{FFT-3}
\]

### Notes
- **C** represents concept-wave / optical projection field.  
- **\(\Pi_{XY}\)** extracts the XY interference plane of Ψ.  
- C includes light, EM waves, IR, radio (all receptor-dependent waves).

---

# 4. Sora Equation (Derived Generator Evolution)

The generator field:

\[
\psi = \chi\delta
\tag{4.0}
\]

obeys the Sora evolution equation:

\[
\partial_t \psi
=
\omega_0'
+ D\Delta\psi
+ \kappa\|\nabla\psi\|^2
+ \xi .
\tag{4.1}
\]

### Parameters
- \(\omega_0'\)：基準巻込み速度（原子時計周波数）  
- \(D\)：情報的拡散  
- \(\kappa\)：非線形増幅  
- \(\xi\)：カラードノイズ  

This expresses how causal curvature χ and interference δ recursively reinforce each other.

---

# 5. T-wave Density Equation

\[
\partial_t \rho_T
=
\beta_1\|\nabla\psi\|^2
+
\beta_2\|\nabla C\|^2
-
\gamma\,\rho_T.
\tag{5.1}
\]

- ρ_T：T-fiber（Z-axis causal strands）の密度  
- β1：ψ-wave からの生成  
- β2：C-wave 干渉からの生成  
- γ：T-fiber 減衰（因果の散逸）

This governs structure formation in both perception and cosmology.

---

# 6. FFT Uncertainty Relations

## 6.1 Geometric Uncertainty

\[
\Delta_Z \cdot \Delta_{XY} \ge \Lambda_{\mathrm{geom}}.
\tag{6.1}
\]

- ΔZ = Z-axis accumulation width (τ-lag)  
- ΔXY = transverse interference width  

This arises from the projection \(\Pi_{XY}\circ\mathcal{G}\).

---

## 6.2 Low-Energy Reduction to Heisenberg

When ψ-gradients flatten:

\[
\Delta_Z \sim \frac{\Delta p}{m\omega_0'},
\qquad
\Delta_{XY} \sim \Delta x,
\]

we obtain:

\[
\Delta x \cdot \Delta p
\simeq
\frac{\hbar}{2}.
\tag{6.2}
\]

Thus FFT reproduces standard QM in the low-energy, small-curvature limit.

---

# 7. Fundamental Constants Derived from χδ Geometry

## 7.1 Planck Constant

\[
\hbar_{\mathrm{phys}}
=
\alpha_D\,M_F\,\frac{L_F^{2+D}}{T_F}
\,|\gamma|^{D}.
\tag{7.1}
\]

- γ：Z-axis propagation constant  
- \(M_F,L_F,T_F\)：FFT 基準スケール  
- α_D：無次元定数  

---

## 7.2 Gravitational Constant

\[
G_{\mathrm{phys}}
=
c^{5}\,
\frac{f(D,\gamma)}{K(D)\,|\gamma|^{D}\,\kappa^{2}}
\tag{7.2}
\]

where \(K(D)\) is a geometric factor from curvature accumulation.

---

## 7.3 Cosmological Constant

Λ arises from the average δ-drift:

\[
\Lambda
\;\propto\;
\partial_t\langle \delta \rangle.
\tag{7.3}
\]

This connects cosmic acceleration to concept-wave density drift.

---

# 8. Observation and Consciousness Geometry

## 8.1 Maximum-Entropy Z-extension

\[
\mathcal{G}[C]
=
\arg\max_\rho
S[\rho]
\quad
\text{subject to}
\quad
\int\rho\,dz=q(x,y),
\tag{8.1}
\]

where  
\[
q(x,y)=\frac{|C|^2}{\int|C|^2 dxdy}.
\]

---

## 8.2 Reflection (反省)

\[
\rho_{\text{reflected}}
=
\arg\min_{\rho\in\mathcal{G}[C]}
\operatorname{Var}_{z}(\rho).
\tag{8.2}
\]

This defines “freedom as Z-axis collapse”.

---

# 9. Summary Table of Primary Variables

| Symbol | Meaning |
|--------|---------|
| χ | causal curvature (Z-axis) |
| δ | interference density (XY-plane) |
| ψ | generator field ψ = χδ |
| Ψ | full T-fiber field |
| C | concept-wave (XY projection) |
| ρ | information density |
| ρ_T | T-wave density |
| τ | phase-time |
| ΔZ | Z-axis width (past-lag) |
| ΔXY | interference width |

---

# End of FFT Equation Catalogue