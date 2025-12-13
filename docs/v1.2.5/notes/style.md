# FFT Style Guide — Mathematical Notation & Document Structure

This document defines the mandatory style rules for all Fixed-Field Theory (FFT)
documents, including Main Text, Appendices, and supplemental materials.

The goal is long-term consistency, mathematical clarity, and renderer safety.
These rules are structural constraints, not aesthetic preferences.

## 1. Mathematical Notation Rules

### 1.1 Inline Math

Inline mathematical expressions MUST use `$ ... $`.

Backticks MUST NOT be used for mathematics.

Correct:
  The generator field satisfies $ψ = χδ$.

Incorrect:
  The generator field satisfies `ψ = χδ`.

### 1.2 Block Math

All defining, structural, or operator-level equations MUST use block math
notation with `$$ ... $$`.

This includes definitions, integrals, projection operators, and variational
principles.

Examples (notation only):
  $$ ψ = χδ $$
  $$ ∫ dz A(z) B(z) $$
  $$ δ𝒜 = 0 $$

### 1.3 Inline vs Block Decision Rule

Inline `$...$` is used only for references, labels, and light relations inside
sentences.

Block `$$...$$` is used for structure, definitions, operators, and dynamics.

If an equation contains an integral, projection, or operator definition, it MUST
be a block equation.

### 1.4 Norm and Absolute Value

Vector magnitudes MUST use double bars `\|\nabla\psi\|`.

Single bars `| |` are reserved for scalar absolute values.

Correct:
  $\kappa\|\nabla\psi\|^2$

Incorrect:
  $\kappa|\nabla\psi|^2$

### 1.5 KaTeX Stability Rules

To avoid GitHub and KaTeX rendering issues:

- Do NOT start a line with operators such as `i\hbar`, `=`, or `+`.
- Operators must appear after an assignment or continuation.

## 2. Document Structure Rules

All appendices MUST follow this structure:

1. Purpose and Scope
2. Background (χδ–ψ Framework)
3. Main Derivation / Model
4. Relation to χδ Geometry
5. Implications for Main Sections
6. Link to Open Problems
7. Summary

## 3. Projection and Interference Operators

Definitions of projection or interference operators
(e.g. $f$, $\mathcal{I}$, $\Pi_{\mathrm{obs}}$)
MUST be written as block equations.

Inline usage is allowed only for symbolic reference.

## 4. Non-Negotiable Rule

If a choice exists between convenience and consistency,
consistency always wins.