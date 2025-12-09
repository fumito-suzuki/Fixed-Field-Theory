# Contributing to Fixed-Field Theory (FFT)

Thank you for your interest in contributing to **Fixed-Field Theory (FFT)** —  
a unified geometric framework connecting quantum mechanics, cosmology, and perception.

This project welcomes contributions from physics, mathematics, computer science,  
and cognitive science communities. To maintain consistency and scientific rigor,  
please follow the guidelines below.

---

## 1. Ways to Contribute

You can contribute in several forms:

### 1.1 Report Issues

- Mathematical inconsistencies  
- Numerical errors or simulation bugs  
- Typos or unclear explanations in documentation  
- Incorrect references  

When opening an Issue, please include:

- A clear description of the problem  
- Equation numbers or file locations (e.g., FFT-2, Appendix Z3)  
- A minimal reproducible example (for code-related issues)

### 1.2 Submit Improvements

- Better explanations of geometric concepts (T-wave, C-wave, τ, χδ, etc.)  
- New diagrams for τ-geometry, T-wave / C-wave interference  
- Proofreading and clarifying LaTeX equations  
- Improved numerical stability or speed for Python scripts  

### 1.3 Propose Theoretical Extensions

FFT evolves through formal appendices (Z1, Z2, … Z37B …).  
For adding new theoretical insights:

- First discuss the idea in an Issue  
- Attach mathematical derivations or sketches of proofs  
- Specify whether it extends χδ, τ-geometry, or the FFT-1–3 equation set  
- Indicate which existing sections it interacts with (e.g., quantum, cosmology, mind)

---

## 2. Repository Structure

Please follow this structure when adding or modifying files:

    docs/v1.2.2/           — main theory documents
    docs/v1.2.2/equations/ — FFT-1, FFT-2, FFT-3, and derived equations
    docs/v1.2.2/appendices — Z1–Z37B and new formal appendices
    docs/v1.2.2/figures/   — diagrams and geometric illustrations
    src/python/            — numerical experiments and simulations
    src/latex/             — full academic paper (FFT-paper.tex)
    tools/                 — build scripts and validation tools

Guidelines:

- New equations → place in `docs/v1.2.2/equations/`  
- New appendices → place in `docs/v1.2.2/appendices/` and name as `Z##-title.md`  
- New figures → place in `docs/v1.2.2/figures/`  
- New simulations → place in `src/python/`  

---

## 3. Mathematical Style Guidelines

To ensure consistency across all documents:

### 3.1 Equations

- Use LaTeX notation in `.tex` files or Markdown math blocks.  
- Prefer block math with `$$ ... $$` in Markdown documents.  
- Main equations use the label `FFT-N` (e.g., FFT-1, FFT-2, FFT-3).  
- Appendices use local numbering unless they refine FFT-1–3 directly.

### 3.2 Core Symbols

These key symbols must be used consistently:

| Symbol | Meaning |
|--------|--------|
| χ      | Z-axis causal stacking (T-fiber accumulation) |
| δ      | XY-plane interference density |
| ψ      | information density gradient |
| τ      | phase-time (emergent time coordinate) |
| ρ      | information density / density operator |
| C      | conceptual-wave field (measurement-dependent mode) |
| T      | T-wave / T-fiber field |
| Z      | depth / delay axis (causal past extension) |

If you need new notation, please justify it in the corresponding appendix.

---

## 4. Python Code Guidelines

All numerical experiments should:

- Run with **Python 3.10+**  
- Include a short description at the top of each file  
- Avoid external dependencies unless clearly justified  
- Follow PEP8 when practical  
- Place shared utilities in `src/python/common/` if reuse grows

Each script should start with a header like:

    """
    Description:  Short summary of what this script simulates.
    Inputs:       List of key parameters or input files.
    Outputs:      What the script produces (plots, data, logs).
    Reference:    Related FFT equations (e.g., FFT-1, Appendix Z3).
    """

Simulation code should reference FFT equations whenever possible:

- T-wave dynamics → FFT-1  
- C-wave projection → FFT-3  
- Z-axis transform / perception model → relevant Z-appendices  
- Λ (cosmological constant) estimator → cosmology appendices  

---

## 5. Pull Request (PR) Process

Before submitting a PR:

1. **Create an Issue** describing your proposed change (unless it is trivial).  
2. **Explain the motivation** — why this change improves FFT.  
3. **If adding theory**:  
   - Include derivations or at least a clear roadmap.  
   - Explain how it connects to χδ, τ-geometry, or T-wave/C-wave dynamics.  
   - Check that it does not contradict FFT-1–3 without explicit discussion.  
4. **If adding equations**:  
   - Ensure all LaTeX compiles (use `tools/build_pdf.sh` if available).  
5. **If adding simulations**:  
   - Provide sample input/output or a brief description of expected behavior.  

PR Checklist (you can paste this into your PR description):

- [ ] Code builds without errors  
- [ ] LaTeX compiles successfully  
- [ ] Documentation updated where necessary  
- [ ] Mathematical notation matches FFT standards  
- [ ] No unused variables or dead code remain  

---

## 6. Academic Integrity

FFT is a scientific work. All contributors must follow:

- Rigorous mathematical argumentation  
- Correct citation of external sources and prior work  
- No unverifiable claims presented as proven facts  
- No plagiarism (including from AI-generated text)  

AI tools may be used for drafting or prototyping,  
but human verification and responsibility are required for all contributions.

---

## 7. Licensing and Copyright

Contributions are accepted under the **MIT License**.

By submitting a Pull Request, you agree that:

- Your contribution will be licensed under MIT as part of this project.  
- You hold the necessary rights to the content you submit.  
- You do not introduce code or text that conflicts with third-party licenses  
  incompatible with MIT.

---

## 8. Contact

For major theoretical proposals or collaboration requests, please contact:

**Project Maintainer:**  
Fumito Suzuki  
(GitHub profile or contact information to be added)

---

Thank you for helping advance **Fixed-Field Theory (FFT)**.
