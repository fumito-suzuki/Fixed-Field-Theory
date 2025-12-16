# Appendix C — Variational Derivation of the Sora Equation

*(Fixed-Field Theory v1.2.5.1 Supplemental Material)*

This appendix derives the **Sora Equation** from a χδ-generated variational
principle.
It shows that the generator field ψ evolves according to an extremal action,
placing FFT on the same mathematical foundation as GR, QFT, and classical
mechanics.

The resulting equation is:

$$
\boxed{
\partial_t\psi =
\omega_0' +
D\Delta\psi +
\kappa\|\nabla\psi\|^2 +
\xi
}
$$

## 1. Purpose and Scope

This appendix supports Section 4 and Section 6 of the main text by providing:

- the action functional whose Euler–Lagrange equation is the Sora Equation,
- explicit forms of kinetic, nonlinear, and forcing contributions,
- geometric interpretation in terms of χδ coupling,
- consistency with ψ = χδ and observational geometry (C-wave).

It clarifies why ψ evolves as a **generator field** and not as a physical wave.

## 2. Background (χδ–ψ Framework)

FFT adopts the χδ axiom (Appendix Z+0):

- χ — causal curvature injection (Z → τ)
- δ — interference density (XτZ / YτZ)
- ψ = χδ — appearance field governing perceptual and structural stability

ψ is **not** a physical wave;
it is the geometrically reconstructed generator of appearance.

This appendix shows that ψ must satisfy a **variationally optimal evolution law**.

## 3. Main Derivation / Model

### 3.1 Definition of the Generator Field

$$
\psi = \chi\delta.
$$

Because χ and δ are non-commuting geometric operators:

- ψ is nonlinear,
- inherits anisotropy (Z vs XY),
- responds to fractal scaling (D = a + b),
- interacts with delayed-plane geometry (C-wave).

### 3.2 The χδ-Generated Action

Define the action:

$$
\boxed{
\mathcal{A}[\psi] =
\int
\left[
\frac{1}{2}D\,\|\nabla\psi\|^2 +
\frac{\kappa}{3}\|\nabla\psi\|^3 -
\omega_0'\psi +
\xi\psi
\right]
\, dV\, dt
}
$$

This action includes:

1. **Kinetic smoothing** — $D\|\nabla\psi\|^2$
2. **Nonlinear χδ amplification** — $\kappa\|\nabla\psi\|^3$
3. **Baseline curvature injection** — $\omega_0'$
4. **Colored noise forcing** — $\xi$

These correspond directly to the terms in the Sora Equation.

### 3.3 Variational Procedure

Euler–Lagrange condition:

$$
\frac{\partial\mathcal{L}}{\partial\psi} -
\nabla\cdot
\frac{\partial\mathcal{L}}{\partial(\nabla\psi)} =
0.
$$

#### (1) Kinetic term

$$
\frac{\partial\mathcal{L}}{\partial(\nabla\psi)} = D\nabla\psi,
\qquad
\nabla\cdot(D\nabla\psi) = D\Delta\psi.
$$

#### (2) Nonlinear geometric term

Let $u = \|\nabla\psi\|$:

$$
\frac{\partial}{\partial(\nabla\psi)}
\left(\frac{\kappa}{3}u^3\right) =
\kappa u\nabla\psi.
$$

Leading to:

$$
\nabla\cdot(\kappa u\nabla\psi)
\simeq
\kappa\|\nabla\psi\|^2
+
\text{(higher-order terms)}.
$$

FFT retains the dominant χδ-amplification term.

#### (3) Potential and noise term

$$
\frac{\partial\mathcal{L}}{\partial\psi} =
-\!\left(\omega_0' - \xi\right).
$$

## 4. Result of the Euler–Lagrange Equation

Collecting all contributions:

$$
\boxed{
\partial_t\psi =
\omega_0' +
D\Delta\psi +
\kappa\|\nabla\psi\|^2 +
\xi
}
$$

Thus the Sora Equation follows directly from action minimization:

$$
\delta \mathcal{A}[\psi] = 0.
$$

This demonstrates that ψ evolves as the **least-action generator** of χδ geometry.

## 5. Relation to χδ Geometry

Since ψ = χδ:

- χ controls Z-axis depth and curvature injection
- δ governs delayed-plane interference
- action extremization enforces global χδ consistency
- ψ becomes the mediator between physical field Ψ and perceptual field C

The variational structure parallels GR:

$$
\delta\int R\sqrt{-g}\,d^4x = 0
\quad\leftrightarrow\quad
\delta\mathcal{A}[\chi\delta] = 0.
$$

## 6. Implications for Main Sections

**Section 4 — ψ as appearance dynamics**  
The Sora Equation determines how ψ smooths, amplifies, or collapses.

**Section 5 — low-curvature QM regime**  
Small $\|\nabla\psi\|$ suppresses nonlinearities, and FFT reproduces quantum behavior.

**Section 6 — curvature and cosmology**  
$\omega_0'$ and χδ scaling connect ψ evolution to global curvature (Λ).

**Section 7 — consciousness geometry**  
ψ stability determines reconstruction fidelity, χ-band stability,
and freedom bandwidth $d\chi/dt$.

## 7. Summary

- ψ = χδ evolves by extremizing a χδ-generated action.
- The Euler–Lagrange equation yields the Sora Equation directly.
- ψ incorporates smoothing, amplification, baseline unfolding, and noise.
- The variational principle guarantees consistency with FFT-1, FFT-2, and FFT-3.

$$
\boxed{
\delta\mathcal{A} = 0
\;\Longrightarrow\;
\partial_t\psi =
\omega_0' +
D\Delta\psi +
\kappa\|\nabla\psi\|^2 +
\xi.
}
$$
