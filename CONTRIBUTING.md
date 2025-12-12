# Contributing to Fixed-Field Theory (FFT)

Thank you for your interest in contributing to Fixed-Field Theory (FFT),
a unified geometric framework connecting quantum mechanics, cosmology, and perception.

This project welcomes contributions from physics, mathematics, computer science,
and cognitive science communities. To maintain consistency and scientific rigor,
please follow the guidelines below.


## 1. Ways to Contribute

You can contribute in several forms.

### 1.1 Report Issues

Examples:
- Mathematical inconsistencies
- Numerical errors or simulation bugs
- Typos or unclear explanations
- Incorrect references

When opening an Issue, please include:
- A clear description of the problem
- Equation numbers or file locations (for example FFT-2 or Appendix Z+3)
- A minimal reproducible example if code is involved


### 1.2 Submit Improvements

Examples:
- Clearer explanations of geometric concepts (T-wave, C-wave, tau, chi-delta)
- New diagrams for tau geometry or projection structure
- Proofreading or LaTeX cleanup
- Performance or stability improvements in numerical scripts


### 1.3 Propose Theoretical Extensions

FFT evolves through formal appendices (Z+0, Z+1, … Z+37B).

For new theoretical proposals:
- Open an Issue first
- Attach derivations or proof sketches
- Specify whether the extension concerns chi-delta geometry, tau geometry,
  projection theory, cosmology, or consciousness
- Clearly state interactions with existing sections (quantum, cosmology, perception)


## 2. Repository Structure

Please follow this structure when adding or modifying files.

docs/v1.2.5/
docs/v1.2.5/equations/
docs/v1.2.5/appendices/
docs/v1.2.5/figures/
src/python/
src/latex/
tools/

Directory descriptions:
- docs/v1.2.5/            main theory documents
- docs/v1.2.5/equations/  FFT-1, FFT-2, FFT-3 and derived equations
- docs/v1.2.5/appendices/ Z+0 to Z+37B and new formal appendices
- docs/v1.2.5/figures/    diagrams and geometric illustrations
- src/python/             numerical experiments and simulations
- src/latex/              full academic paper (FFT-paper.tex)
- tools/                  build scripts and validation tools

Guidelines:
- New equations go to docs/v1.2.5/equations/
- New appendices go to docs/v1.2.5/appendices/
- New figures go to docs/v1.2.5/figures/
- New simulations go to src/python/


## 3. Mathematical Style Guidelines

### 3.1 Equations

- Use LaTeX notation in tex files or Markdown math blocks
- Prefer block math using double dollar notation
- Core equations are labeled FFT-1, FFT-2, FFT-3
- Appendix equations use local numbering unless extending FFT-1 to FFT-3


### 3.2 Core Symbols

The following symbols must be used consistently.

Symbol meanings:
- chi      causal depth and T-fiber stacking
- delta    interference density on projected planes
- psi      appearance field defined as chi times delta
- tau      phase-time
- rho      information density or density operator
- C        C-wave observable projection
- T        T-wave or T-fiber field
- Z        causal depth or delay axis

New symbols must be justified in the corresponding appendix.


## 4. Python Code Guidelines

All numerical experiments must:
- Run on Python 3.10 or later
- Include a short description at the top of each file
- Avoid unnecessary external dependencies
- Follow PEP8 when practical

Each script should begin with a documentation block describing:
- Purpose of the simulation
- Input parameters
- Output data or plots
- Related FFT equations or appendices

Simulation references:
- T-wave dynamics relate to FFT-1
- C-wave projection relates to FFT-3
- Tau geometry and perception relate to Z-appendices
- Cosmological constants relate to Z+5 and Z+10


## 5. Pull Request Process

Before submitting a pull request:

1. Create an Issue unless the change is trivial
2. Explain the motivation and benefit
3. For theory additions:
   - Provide derivations or a clear roadmap
   - Explain interaction with chi-delta, tau, or projection geometry
   - Explicitly note any tension with FFT-1 to FFT-3
4. For equations:
   - Confirm LaTeX builds successfully
5. For simulations:
   - Describe expected behavior and outputs

Checklist:
- Code builds without errors
- LaTeX compiles
- Documentation updated
- Notation matches FFT conventions
- No unused code remains


## 6. Academic Integrity

FFT is a scientific work.

Contributors must ensure:
- Rigorous mathematical reasoning
- Correct citation of prior work
- No unverifiable claims presented as established results
- No plagiarism

AI tools may assist drafting, but human verification is required.


## 7. Licensing

All contributions are accepted under the MIT License.

By submitting a contribution, you confirm:
- You have the right to submit the material
- The contribution is MIT-compatible
- No conflicting third-party licenses are introduced


## 8. Contact

For major theoretical proposals or collaboration:

Project Maintainer:
Fumito Suzuki
(Contact details to be added)

Thank you for contributing to Fixed-Field Theory.