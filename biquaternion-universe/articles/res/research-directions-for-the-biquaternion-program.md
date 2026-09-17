
# __Research Directions for the Biquaternion Program__

## What This Article Is

This article is a strategic map of the biquaternion program. Its purpose is to list the directions of research that the program opens, to classify them by what is established, what is conjectural, and what is frontier, and to propose a natural order of attack. It is intended to be consulted repeatedly, whenever a moment is available to develop one of the directions.

The article assumes the four anchor pieces of the program: the presentation page (*Complexified Spacetime with a Local Complex Structure*), the motivation article (*Why Complexify Spacetime?*), and the two companion articles on the two natural subspaces (*$\mathbb{M}_-$ as the Material Space* and *$\mathbb{M}_+$ as the Informational Space*), together with the identification of $\mathbb{M}_+$ with the operator algebra of a spin-1/2 system (*Spin-1/2 Quantum Mechanics in Biquaternionic Form*).

The goal of the program is **progressive incorporation**: to embed existing physical theories — quantum mechanics, thermodynamics, fluid dynamics, magnetohydrodynamics — into the biquaternion framework, and, if the informational hypothesis is correct, to develop new physics from the structure of $\mathbb{M}_+$.

The article is organized as follows. First the assets of the program are summarized. Then the research directions are organized into nine axes, each with a description, the relevant open questions, and candidate articles. Then a recommended order of attack is given. The article closes with a condensed table of directions and their status.

## The Assets of the Program

Before listing directions, it is worth being precise about what the program already has.

**Algebraic structure.** The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with four conjugations, four fixed-point subspaces ($\mathbb{C}_\mathbb{B}$, $\mathbb{H}_\mathbb{B}$, $\mathbb{M}_+$, $\mathbb{M}_-$), two natural decompositions (the Hermitian decomposition $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$ and the quaternion decomposition $\mathbb{B} = \mathbb{H}_\mathbb{B} \oplus i\mathbb{H}_\mathbb{B}$), and the isomorphism $\mathbb{B} \cong M_2(\mathbb{C})$.

**Analysis.** The biquaternionic gradient $\tilde{\nabla}$, its quaternion conjugate $\bar{\tilde{\nabla}}$, the d'Alembertian $\Box = \tilde{\nabla}\bar{\tilde{\nabla}}$, the factorization $\Box = \tilde{\nabla}\bar{\tilde{\nabla}}$, and the Cauchy integral formula for the four-dimensional subspace.

**Physics.** The four-vectors of relativistic mechanics (position, velocity, momentum, force, potential, current), Maxwell's equations in the form $\tilde{\nabla}\tilde{F} = -\tilde{R}$, the Lorentz transformation as a rotor conjugation, and the Dirac equation $\tilde{\nabla}\tilde{\Psi} = m\tilde{\Psi}^\flat$.

**The informational hypothesis.** The identification of $\mathbb{M}_+$ with the operator algebra of a spin-1/2 system: idempotents are pure-state projectors, Hermitian elements are observables, unitary elements are gates, the trace formula is the Born rule. The action of $\mathbb{M}_+$ on $\mathbb{M}_-$ by conjugation: unitary elements give reversible evolution, idempotent elements give irreversible measurement.

**The local complex structure.** The hypothesis that the complex structure is local, with $c(x) = 1/\sqrt{\epsilon(x)\mu(x)}$ as the local scale factor.

These assets are the starting point for the nine axes below.

## Axis A — Consolidating the Mathematical Foundations

Before extending the program, several loose ends in the mathematical structure need attention. These are not optional refinements; they are the load-bearing joints of the framework.

### A.1 The remaining internal tensions

Four internal tensions were identified in the current articles.

**Tension A: The polar form.** The Hamilton polar form in the polar representations article and the Hamilton polar form in the elementary functions article are not identical. The two must be reconciled, or the difference must be explained.

**Tension B: The d'Alembertian sign.** The d'Alembertian is written $\Box = \partial_0^2 + \Delta$ in the analysis articles (with $x_0$ real) but acts as a wave operator (with $ict$ as a coordinate) in the harmonic analysis articles. The convention needs to be made uniform. The cleanest fix is to treat the analysis articles as operating in a "Euclidean" continuation and the harmonic analysis articles in the physical Lorentzian slice, with an explicit Wick-rotation relation between them.

**Tension C: The field-strength subspace.** The field-strength biquaternion $\tilde{F} = \sqrt{\epsilon}\mathbf{E} + i\sqrt{\mu}\mathbf{H}$ does not lie in any of the four named subspaces. It is a mixed biquaternion with real electric and imaginary magnetic vector parts. This is the **rank-2 antisymmetric tensor** representation of the Lorentz group, and it deserves its own subspace designation — perhaps $\mathbb{T}_-$, the "tensor subspace."

**Tension D: The Lorentz transformation formula.** The one-sided multiplication formula $\tilde{A}' = (\gamma/c)\tilde{U}\tilde{A}$ used in the earlier Maxwell article does not reproduce the standard component formulas in general. It has been replaced by the rotor conjugation $\tilde{A}' = \tilde{\Lambda}\tilde{A}\tilde{\Lambda}^\dagger$ in the Lorentz transformation article, which is correct. The older formula should be removed or flagged as a special-case convention.

### A.2 The five-subspace structure

The five natural subspaces $\mathbb{C}_\mathbb{B}$, $\mathbb{H}_\mathbb{B}$, $\mathbb{M}_+$, $\mathbb{M}_-$, $i\mathbb{H}_\mathbb{B}$ correspond to distinct physical objects, and the correspondence should be made explicit.

| Subspace | Dimension | Physical interpretation |
|---|---|---|
| $\mathbb{C}_\mathbb{B}$ | 2 | Center — the complex scalars (charge, mass as complex numbers?) |
| $\mathbb{H}_\mathbb{B}$ | 4 | Real quaternions — energy–momentum (real density + Poynting vector) |
| $i\mathbb{H}_\mathbb{B}$ | 4 | Purely imaginary — dual of $\mathbb{H}_\mathbb{B}$ |
| $\mathbb{M}_-$ | 4 | Material sector — four-vectors |
| $\mathbb{M}_+$ | 4 | Informational sector — operators (Hermitian, observables) |

The physical content of each subspace, and the transitions between them, is a natural organizing article.

### A.3 The automorphism group

The group of automorphisms of $\mathbb{B}$ preserving the Hermitian structure is $SO(4,\mathbb{C})$ (with the biquaternion version being $SL(2,\mathbb{C}) \times SL(2,\mathbb{C})$, up to finite quotients). The real subgroups — $SO(4)$, $SO(3,1)$, $SO(2,2)$ — correspond to distinct physical settings. A dedicated article on the automorphism group would clarify the symmetry content of the framework.

### A.4 Tensor representations

The rank-2 tensor representations of the Lorentz group need to be classified in the biquaternion framework. The antisymmetric tensor $F^{\mu\nu}$ (field strength) and the symmetric traceless tensor (energy–momentum, gravitational potential) have distinct biquaternion representations. This is essential for Axis D (fluids and MHD).

### A.5 The complex bilinear form and the signature

The relation between the complex bilinear form $\sum_\mu (dQ_\mu)^2$ and the Lorentzian signature of the physical slice is subtler than the presentation article suggests. On the real slice $q'_\mu = 0$ with real $q_\mu$, the form is Euclidean. The Lorentzian signature arises only when the time coordinate is assigned to be imaginary, i.e., when $q_0$ itself is treated as $ict$. A dedicated article clarifying this subtlety is important both for internal consistency and for the reader's understanding.

## Axis B — Quantum Mechanics

This is the axis with the sharpest anchor, because the identification of $\mathbb{M}_+$ with the spin-1/2 operator algebra is exact. The program should develop quantum mechanics fully before moving to more speculative directions.

### B.1 Density matrices and the Bloch ball

**What to develop.** The general mixed state of a qubit is a Hermitian positive operator of trace one, which in the biquaternion framework has the form $\rho = \tfrac{1}{2}(e_0 + i\boldsymbol{\mu}\cdot\mathbf{e})$ with $|\boldsymbol{\mu}| \le 1$. The Bloch ball is embedded in $\mathbb{M}_+$.

**Why it matters.** This extends the pure-state identification to mixed states and prepares the framework for thermodynamics and for measurement theory.

**Candidate article.** *"Mixed States and the Bloch Ball in Biquaternionic Form"* — short, clean, direct extension of the spin-1/2 article.

### B.2 Schrödinger and Heisenberg evolution

**What to develop.** The dynamics of a quantum system is generated by a Hermitian element $\tilde{H} \in \mathbb{M}_+$: the unitary family $\tilde{\Lambda}(t) = \exp(-i\tilde{H}t/2)$ acts by rotor conjugation $\tilde{X}(t) = \tilde{\Lambda}(t)\tilde{X}\tilde{\Lambda}^\dagger(t)$. The infinitesimal form is the Heisenberg equation $d\tilde{X}/dt = i[\tilde{H},\tilde{X}]$. The corresponding Schrödinger equation is obtained by passing to the spinor representation.

**Why it matters.** This gives the framework a **dynamics**. Without it, the informational hypothesis has no content. With it, the framework contains quantum mechanics as a specific kinematic-and-dynamic structure.

**Candidate article.** *"Schrödinger and Heisenberg Evolution from Rotor Conjugation"* — short, foundational.

### B.3 Entropy

**What to develop.** The von Neumann entropy $S(\rho) = -\mathrm{Tr}(\rho\log\rho)$ is well-defined on the Bloch ball: the eigenvalues of $\rho$ are $(1 \pm |\boldsymbol{\mu}|)/2$, and $S$ is a function of $|\boldsymbol{\mu}|$. The biquaternion logarithm from the elementary functions article is multivalued; the multivaluedness is closely related to the periodicity of thermal states in imaginary time.

**Why it matters.** Entropy is the bridge to thermodynamics (Axis C) and to the informational reading of $\mathbb{M}_+$.

**Candidate article.** *"Entropy and the Arrow of Time in the Biquaternion Framework"* — medium.

### B.4 Measurement theory

**What to develop.** The idempotent projection $\tilde{X} \mapsto \tilde{P}\tilde{X}\tilde{P}$ is a formal operation. What is not yet there is the **probability assignment** (the Born rule, which is available via the trace formula) and the **state update** in a full measurement theory. The measurement problem itself — the emergence of definite outcomes from a unitary evolution — is outside the current framework, but the **structure** of projective measurement is contained.

**Why it matters.** This is the sharpest point of contact with foundational questions in quantum mechanics.

**Candidate article.** *"Measurement Theory in the Biquaternion Framework"* — medium-to-long.

### B.5 Tensor products and entanglement

**What to develop.** The tensor product $\mathbb{B} \otimes \mathbb{B} \cong M_4(\mathbb{C})$ gives a two-qubit system. Entanglement is the existence of states in $M_4(\mathbb{C})$ that are not product states. The biquaternion framework does not yet contain this extension, but it is straightforward algebraically.

**Why it matters.** This is the natural route to many-body quantum mechanics and to the quantum-information content of the informational sector.

**Candidate article.** *"Tensor Products and Entanglement in the Biquaternion Framework"* — medium.

### B.6 Summary

Axis B is the **safest and most productive** direction. Everything in it follows from established quantum mechanics and the exact identification already made. By the end of Axis B, the framework will contain non-relativistic quantum mechanics in full.

## Axis C — Thermodynamics and the Wick Bridge

This axis uses imaginary time as the bridge between Lorentzian dynamics and thermodynamic structure.

### C.1 Imaginary time as thermodynamic time

**What to develop.** The Wick rotation $t \to -i\tau$ connects Lorentzian QFT to Euclidean statistical mechanics. The same imaginary time direction already lives in $\mathbb{M}_-$ as the $ict$ coordinate. The framework should make this explicit and recover the KMS condition as the equilibrium condition for a thermal state.

**Why it matters.** This establishes the thermodynamic reading of imaginary time and prepares the ground for the informational interpretation of $\mathbb{M}_+$.

**Candidate article.** *"Imaginary Time and Thermodynamics in the Biquaternion Framework"* — medium.

### C.2 The two time directions

**What to develop.** $\mathbb{M}_-$ has an imaginary time direction (the direction of entropy increase); $\mathbb{M}_+$ has a real time direction. The conjectured mirror — dispersion in the first, organization in the second — should be developed into a quantitative statement. Candidate formalization: an entropy functional on $\mathbb{M}_-$ that increases along $ict$, paired with a "negative entropy" functional on $\mathbb{M}_+$ that increases along $ct'$.

**Why it matters.** This is the structural content of the informational hypothesis in the time domain.

**Candidate article.** *"Two Time Directions: The Thermodynamic Reading"* — medium.

### C.3 Modular theory and the KMS condition

**What to develop.** In the algebraic approach to QFT, every state on a von Neumann algebra has a modular group, and thermal states are characterized by the KMS condition. The biquaternion algebra $\mathbb{B} \cong M_2(\mathbb{C})$ is a von Neumann algebra; its modular structure gives a natural notion of temperature for the informational sector. This is a frontier direction but mathematically well-defined.

**Why it matters.** This is the natural **algebraic** entry point to the informational hypothesis.

**Candidate article.** *"Modular Theory and the KMS Condition in the Biquaternion Framework"* — long.

### C.4 Summary

Axis C is medium-difficulty. It uses established mathematics (Wick rotation, KMS theory) and connects the framework to the thermodynamic reading of imaginary time.

## Axis D — Relativistic Field Theory and Fluids

This axis extends the framework to fields and continua.

### D.1 Rank-2 tensors

**What to develop.** The field-strength tensor $F^{\mu\nu}$ (antisymmetric) and the energy–momentum tensor $T^{\mu\nu}$ (symmetric) have distinct biquaternion representations. The antisymmetric case is partially handled (the field-strength biquaternion $\tilde{F}$); the symmetric case is not. A dedicated article establishing the biquaternion representation of both is essential.

**Candidate article.** *"Rank-2 Tensors in the Biquaternion Framework"* — medium, foundational for the rest of Axis D.

### D.2 Energy–momentum and its conservation

**What to develop.** The energy–momentum tensor $T^{\mu\nu}$ satisfies $\partial_\mu T^{\mu\nu} = 0$. In the biquaternion framework, this should be expressible as a conservation law for the biquaternion representation of $T^{\mu\nu}$. The Poynting theorem is a special case.

**Candidate article.** *"Energy–Momentum and Conservation Laws in Biquaternionic Form"* — medium.

### D.3 Relativistic fluid dynamics

**What to develop.** A perfect fluid has four-velocity $\tilde{U} \in \mathbb{M}_-$, density $\rho$, pressure $p$, and energy–momentum tensor $T^{\mu\nu} = (\rho + p/c^2)U^\mu U^\nu + p\eta^{\mu\nu}$. The Euler equation $\partial_\mu T^{\mu\nu} = 0$ becomes a biquaternion equation once the tensor representation is in place.

**Candidate article.** *"Relativistic Fluid Dynamics in the Biquaternion Framework"* — medium-to-long.

### D.4 Magnetohydrodynamics

**What to develop.** The coupling of the electromagnetic field to a conducting fluid is via Ohm's law $\mathbf{J} = \sigma(\mathbf{E} + \mathbf{v}\times\mathbf{B})$ and the Lorentz force. Both are biquaternion objects. The nonlinearity leads to shocks, connecting to the shock-waves article.

**Why it matters.** This is the first direction that goes beyond what the framework has already covered, into new physical content.

**Candidate article.** *"Magnetohydrodynamics in Biquaternionic Form"* — long.

### D.5 Shock waves

**What to develop.** The shock-waves article already covers the linear skeleton. The next step is to incorporate the nonlinear physics of MHD shocks and plasma shocks within the same framework.

**Candidate article.** *"Nonlinear Shocks in the Biquaternion Framework"* — medium, extends the existing shock article.

### D.6 Summary

Axis D is the **most substantial** axis. It requires filling the rank-2 tensor gap first, and it opens the door to fluid dynamics and MHD. Each article in this axis builds on the previous.

## Axis E — The Local Complex Structure as a Field

This axis develops the locality hypothesis.

### E.1 The connection of the complex structure

**What to develop.** If $c(x) = 1/\sqrt{\epsilon(x)\mu(x)}$ is a field, the complex structure varies from point to point. The covariant derivative that respects the local complex structure is the analogue of the Christoffel connection in GR. A dedicated article should develop this.

**Candidate article.** *"The Connection of the Local Complex Structure"* — long, frontier.

### E.2 Emergent gravity from the local complex structure

**What to develop.** In some approaches to emergent gravity, the metric emerges from the properties of an underlying medium. The same idea applied here: the metric of the real slice might emerge from the local complex structure. This is highly speculative but structurally motivated.

**Candidate article.** *"Emergent Gravity from the Local Complex Structure"* — long, exploratory.

### E.3 Varying speed of light

**What to develop.** The literature on varying speed of light (Magueijo, Albrecht) is directly relevant. The local complex structure gives a specific realization of VSL.

**Candidate article.** *"The Local Complex Structure and Varying Speed of Light"* — medium.

### E.4 Summary

Axis E is **frontier** but well-motivated. It connects the program to emergent gravity and VSL, both of which have substantial literature.

## Axis F — Connections to Other Programs

This axis surveys the programs that overlap with the biquaternion program and extracts useful material.

### F.1 Twistor theory

**What to develop.** Penrose's twistor theory complexifies Minkowski space in a specific way (spinor space $\mathbb{C}^4$, Minkowski as a real slice via the incidence relation). The relation between the biquaternion complexification and the twistor complexification is a gap worth filling.

**Candidate article.** *"Biquaternions and Twistors: Parallels and Divergences"* — medium.

### F.2 Holography

**What to develop.** The AdS/CFT correspondence relates bulk geometry to boundary information. The informational reading of the imaginary directions in the biquaternion framework is structurally analogous.

**Candidate article.** *"Holography and the Informational Reading of the Biquaternion Framework"* — medium, exploratory.

### F.3 Kassandrov's algebrodynamics

**What to develop.** Vladimir Kassandrov's program uses biquaternions to reformulate physics, with an emphasis on the algebraic structure of spacetime. It is one of the closest existing programs to this one. A dedicated comparative article is warranted.

**Candidate article.** *"Kassandrov's Algebrodynamics and the Biquaternion Program: A Comparison"* — medium.

### F.4 Information geometry

**What to develop.** The Fisher metric and the Bures metric are information-theoretic metrics on spaces of probability distributions and quantum states. The Bloch ball has a natural Bures metric, and the biquaternion framework may give a specific realization of it.

**Candidate article.** *"Information Geometry in the Biquaternion Framework"* — medium.

### F.5 Thermodynamic geometry

**What to develop.** The Ruppeiner and Weinhold metrics are thermodynamic analogues of the Fisher metric. The connection between thermodynamic geometry and the biquaternion framework could be developed.

**Candidate article.** *"Thermodynamic Geometry and the Informational Sector"* — medium.

### F.6 Summary

Axis F is **comparative**. Each article in this axis situates the biquaternion program relative to an existing research program.

## Axis G — Critical Open Questions

This axis is dedicated to the open problems that test the program.

### G.1 Dimensionality

**Question.** Why are the imaginary spatial directions of $\mathbb{M}_+$ not observed? A compactification or hiding mechanism is required.

**Candidate article.** *"The Dimensionality Problem in Complexified Spacetime"* — medium.

### G.2 Causality

**Question.** How does causal structure in the material sector interact with the informational character of $\mathbb{M}_+$? Can signals propagate between sectors?

**Candidate article.** *"Causality in Complexified Spacetime"* — medium, foundational.

### G.3 Falsifiability

**Question.** What quantitative prediction distinguishes the framework from standard physics? This is the **most important** open question.

**Candidate article.** *"Toward Empirical Contact: What Would Falsify This Hypothesis?"* — medium-to-long.

### G.4 The coupling problem

**Question.** What is the precise dynamical coupling between the material and informational sectors? The Lorentz coupling via the boost biquaternion is established; a genuinely new coupling would be needed for new physics.

**Candidate article.** *"The Coupling Between Material and Informational Sectors"* — long, frontier.

### G.5 Summary

Axis G is **critical**. It addresses the questions that determine whether the program is a physical theory or a mathematical reformulation.

## Axis H — Philosophical and Conceptual

This axis addresses the conceptual questions raised by the program.

- *"What Is Time Made Of? Real, Imaginary, and Complex Readings"* — medium.
- *"The Observer and the Imaginary Sector: Does Information Require a Mind?"* — medium.
- *"Structural Realism and Complexified Spacetime"* — medium.
- *"The Arrow of Time and Its Imaginary Counterpart"* — medium.
- *"On the Physical Meaning of Imaginary Coordinates: A Historical Survey"* — medium.
- *"Why Physics Resists Complexification: A Sociological Reflection"* — short.

These articles situate the program in a broader intellectual context. They are useful for orienting readers and for clarifying what the program does and does not claim.

## Axis I — Speculative Extensions

This axis contains the most exploratory directions. They are offered as possibilities, not commitments.

- *"Complexified Spacetime and the Measurement Problem"* — long.
- *"Could the Imaginary Sector Explain Dark Energy?"* — long.
- *"Black Holes as Interfaces Between Real and Imaginary Sectors"* — long.
- *"Quantum Entanglement and the Geometry of the Informational Sector"* — long.
- *"A Toy Model: Free Fields on $\mathbb{C}^4$ and Their Real-Slice Reduction"* — medium, useful as a computational anchor.

Axis I articles are best written after Axes A–D are more developed.

## Recommended Order of Attack

The axes are not all equally urgent. The recommended order, from most to least urgent, is:

1. **Axis A (Mathematical Foundations).** Fix the four internal tensions. Write the five-subspace article. Establish the tensor representations.
2. **Axis B (Quantum Mechanics).** Develop density matrices, evolution, entropy, measurement, entanglement. This is the safest and most productive direction.
3. **Axis C (Thermodynamics).** Develop imaginary time, two-time structure, KMS.
4. **Axis D (Field Theory and Fluids).** Rank-2 tensors, energy–momentum, fluids, MHD.
5. **Axis F (Other Programs).** Situate the program relative to twistor, holography, Kassandrov, information geometry.
6. **Axis G (Critical Questions).** Address dimensionality, causality, falsifiability, coupling.
7. **Axis E (Local Complex Structure as a Field).** Frontier direction.
8. **Axis H (Philosophical).** Context and orientation.
9. **Axis I (Speculative).** Exploratory.

The natural order is: consolidate, then build on solid foundations, then extend to frontier. Writing the quantum-mechanics axis first will give the program a solid core from which the more speculative directions can be explored.

## Condensed Table of Directions

| Axis | Direction | Status | Difficulty |
|---|---|---|---|
| A | Consolidate algebra | Established | Easy |
| A | Five-subspace structure | Established | Easy |
| A | Automorphism group | Established | Medium |
| A | Rank-2 tensors | Established | Medium |
| A | Complex bilinear form and signature | Established | Medium |
| B | Density matrices, Bloch ball | Established | Easy |
| B | Schrödinger/Heisenberg evolution | Established | Easy |
| B | Entropy | Established | Medium |
| B | Measurement theory | Established | Medium |
| B | Tensor products, entanglement | Established | Medium |
| C | Imaginary time, thermodynamics | Established | Medium |
| C | Two time directions | Conjectural | Medium |
| C | Modular theory, KMS | Established | Long |
| D | Rank-2 tensors in physics | Established | Medium |
| D | Energy–momentum, conservation | Established | Medium |
| D | Fluid dynamics | Established | Medium |
| D | MHD | Established | Long |
| D | Nonlinear shocks | Established | Medium |
| E | Connection of complex structure | Frontier | Long |
| E | Emergent gravity | Frontier | Long |
| E | Varying speed of light | Frontier | Medium |
| F | Twistor comparison | Comparative | Medium |
| F | Holography | Comparative | Medium |
| F | Kassandrov comparison | Comparative | Medium |
| F | Information geometry | Comparative | Medium |
| F | Thermodynamic geometry | Comparative | Medium |
| G | Dimensionality problem | Critical | Medium |
| G | Causality | Critical | Medium |
| G | Falsifiability | Critical | Long |
| G | Coupling problem | Critical | Long |
| H | Philosophical directions | Conceptual | Medium |
| I | Speculative extensions | Frontier | Long |

## The Two Axes That Matter Most

If the program is to grow, two axes are essential.

**Axis B (Quantum Mechanics)** is the **anchor**. It uses established quantum mechanics and the exact identification already made. Every article in Axis B is safe and gives the framework solid physical content. By the end of Axis B, the framework will contain non-relativistic quantum mechanics, and the informational hypothesis will have substantive content.

**Axis G (Critical Questions)** is the **test**. Without answers to the questions in Axis G, the program remains a mathematical reformulation. The dimensionality problem, the coupling problem, and the falsifiability question are the three that determine whether the informational hypothesis is a genuine physical hypothesis or a suggestive structural analogy.

The other axes — A, C, D — build the framework's coverage of existing physics. The other axes — E, F, H, I — situate it relative to frontier and existing programs.

## A Note on Method

The program is unusual in that it is simultaneously a **reformulation of established physics** and a **hypothesis about new physics**. The two aspects should be kept separate in the writing. The material sector $\mathbb{M}_-$ is established; every statement about it can be made with the confidence of standard relativistic physics. The informational sector $\mathbb{M}_+$ is a hypothesis; statements about it should be flagged as such, even when the mathematics is solid.

This separation is the strength of the program. It means that even if the informational hypothesis is wrong, the material sector is a useful reformulation of relativistic physics in the biquaternion algebra. And if the hypothesis is right, the framework is a genuine extension of physics.

The directions listed in this article should be pursued with this separation in mind. Axis A, Axis D, and most of Axis C are extensions of established physics. Axis B is established physics reformulated. Axis G is the critical test. Axis E and Axis I are frontier.

## Summary

The biquaternion program has two anchor assets — the material sector $\mathbb{M}_-$ and the informational sector $\mathbb{M}_+$ — and a clear structural relation between them. The program can grow by progressively absorbing existing physics (quantum mechanics, thermodynamics, fluid dynamics, MHD) into the framework, and by developing the informational hypothesis into a genuine physical theory.

The nine axes of research listed in this article provide a comprehensive map of the directions. The recommended order — consolidate the mathematics, then build quantum mechanics, then thermodynamics, then field theory, then connections to other programs, then the critical questions, then frontier directions — gives a natural path through the program.

The article is intended to be consulted repeatedly. Each axis is a set of articles to write. Each article is a step toward either a more complete reformulation of existing physics or a more substantive articulation of the informational hypothesis.

## Further Reading

- The articles of the biquaternion series (see the presentation page for the current list).
- P. A. M. Dirac, *The Principles of Quantum Mechanics* (Oxford, 1930), for the quantum-mechanical foundations.
- John von Neumann, *Mathematical Foundations of Quantum Mechanics* (Princeton, 1932), for the density matrix and measurement formalism.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the standard modern treatment of qubits and gates.
- Lev Landau and Evgeny Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the relativistic field theory and fluid dynamics.
- Roger Penrose, *The Road to Reality* (Knopf, 2004), for the complex structure of spacetime and twistor theory.
- Vladimir V. Kassandrov, "Relativistic Algebra of Space-Time and Algebrodynamics" (2006), for the closest existing biquaternion program.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric algebra approach to the same structures.

