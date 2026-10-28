# __The Tensor Formalism of the Gauge Sector: Where It Is, and the Nine Non-Hermitian Adjoints__

## Introduction

The gauge articles of the physics corpus use two descriptions at once. One is the biquaternion algebra: a product, an involution, a trace. The other is a component description: an index $\mu$, a derivative $\partial_\mu$, a one-form $A_\mu$, a two-form $F_{\mu\nu}$. The second description is not contained in the first. It is a foreign layer, and this article records where it sits.

Two counts organise the record. **Thirty-seven articles** use the component description, in eight of the twelve categories of `physics.md`. The count uses at least three occurrences of the core tokens $A_\mu$, $F_{\mu\nu}$ or $[D_\mu,D_\nu]$. **Nine occurrences in seven articles** write the field strength as $F\mapsto UFU^{-1}$, with an inverse where the algebra supplies an adjoint.

The second count is the sharp one. On the unitary slice $U^{-1}=U^{*}$, so the nine formulas are numerically Hermitian. Off the slice they are not. The problem is therefore not an error of value; it is an error of provenance: a law of the Hermitian algebra written with an operation the Hermitian algebra does not own.

This article is an inventory. It does not propose a replacement, and it does not claim that one is available.

## What the Formalism Is

The component description consists of four objects and two operations.

| object | form | components |
|---|---|---|
| connection | $A_\mu$ | four algebra elements |
| curvature | $F_{\mu\nu}=-F_{\nu\mu}$ | six independent algebra elements |
| covariant derivative | $D_\mu=\partial_\mu+i\kappa A_\mu$ | four operators |
| current | $J_\mu$ | four algebra elements |

$$
F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu+i\kappa[A_\mu,A_\nu],
\qquad
D_\mu F^{\mu\nu}=J^\nu,
\qquad
D_\lambda F_{\mu\nu}+D_\mu F_{\nu\lambda}+D_\nu F_{\lambda\mu}=0.
$$

The two operations are the index shift $\mu\mapsto\nu$ and the derivative $\partial_\mu$. Neither is an operation of $\mathbb{B}$. The algebra is closed under product, adjoint and trace; it has no coordinate, no index and no derivative. The component description therefore carries the algebra along as a coefficient space and does its real work outside it.

This is why the description is not an extension of the algebra in any technical sense. An extension adds an ideal; this adds a commutative algebra of functions and a set of labels. The labels are what the gauge group does not act on, and the derivative is what the gauge transformation must correct. Both are external, and both are what the corpus would have to replace to write the gauge sector as algebra alone.

## Why It Is a Problem

Three properties make the layer foreign.

**The index is external.** Four components for $A_\mu$ and six for $F_{\mu\nu}$ are copies of the algebra, tied by antisymmetry and by the commutator. No element of $\mathbb{B}$ supplies the copies. Contracting them with a basis,
$$
\mathcal F=\tfrac12 F_{\mu\nu}\,\bar e_\mu e_\nu,
$$
stores the numbers in one biquaternion, but the storage is not equivariant: under $F_{\mu\nu}\mapsto UF_{\mu\nu}U^{-1}$ the contracted object does not go to $U\mathcal F U^{-1}$ unless $U$ is central. The Yang–Mills article verifies this failure numerically. The contraction is a summary, not a reduction.

**The derivative is external.** $\partial_\mu$ acts on functions of the base, not on the algebra. A gauge transformation is a function $U(Q)$, and the inhomogeneous term $(\partial_\mu U)U^{-1}$ exists precisely because $U$ varies over the base. An algebra-only formulation has no place for that term.

**The adjoint law is written with an inverse.** This is the subject of the next section, and it is the only one of the three that can be repaired without changing the layer.

## The Non-Hermitian Adjoint

The algebra has one two-sided action that uses only its own structure, the Hermitian sandwich,
$$
\Theta_U(X)=U\,X\,U^{*}.
$$
The gauge articles use a different one,
$$
\mathrm{Ad}_U(X)=U\,X\,U^{-1}.
$$
The second is not the Hermitian adjoint of the first. It is the inner automorphism, and it requires an inverse. The two maps agree exactly when $U^{-1}=U^{*}$, that is, on the unitary group. Off that group they differ: for $U=\rho V$ with $V$ unitary and $\rho>0$ real,
$$
U X U^{-1}=\rho^{-2}\,U X U^{*}.
$$

Three consequences follow.

- **The formula imports an operation.** $U^{*}$ is defined for every element of $\mathbb{B}$; $U^{-1}$ only for the invertible ones. A law written with $U^{-1}$ silently restricts the domain.
- **The formula hides its hypothesis.** It is correct for the gauge groups the corpus uses — $SU(2)$, unit quaternions — but the correctness comes from unitarity, and the formula does not say so.
- **The formula invites a false identification.** Because $UFU^{-1}$ and $UFU^{*}$ coincide on the slice, the first is often read as a sandwich with the right factor inverted. It is not: it is an automorphism, and the sandwich is a congruence. They coincide on the slice and part company off it.

The nine occurrences are all on the slice. That is why the problem has stayed invisible: every gauge parameter in the corpus is unitary, so no computation can expose the difference.

### The Nine Occurrences in Seven Articles

| article | occurrences | what the inverse does |
|---|---:|---|
| [Non-Abelian Gauge Fields in Biquaternionic Form](../articles_physics/non-abelian-gauge-fields-in-biquaternionic-form.html) | 3 | states the law, derives it from covariance, restates it in the summary |
| [The Yang–Mills Equation in Biquaternionic Form](../articles_physics/the-yang-mills-equation-in-biquaternionic-form.html) | 1 | componentwise law; proves the packaged curvature is not $U\mathcal F U^{-1}$ |
| [Gauge Curvature and the Bianchi Identity in Biquaternionic Form](../articles_physics/gauge-curvature-and-the-bianchi-identity-in-biquaternionic-form.html) | 1 | covariance of $D_\lambda F_{\mu\nu}$ and the Jacobi identity |
| [Quantum Chromodynamics under the Biquaternion Framework — A Research Agenda](../articles_physics/quantum-chromodynamics-under-the-biquaternion-framework-a-research-agenda.html) | 1 | inventory item: the adjoint action a gauge theory requires |
| [The Standard Model under the Biquaternion Framework — A Research Agenda](../articles_physics/the-standard-model-under-the-biquaternion-framework-a-research-agenda.html) | 1 | the same inventory, in the reality-class paragraph |
| [Wilson Loops in Biquaternionic Form](../articles_physics/wilson-loops-in-biquaternionic-form.html) | 1 | gauge invariance of the traced holonomy |
| [Confinement and the Loss of Partonic Information in Biquaternionic Form](../articles_physics/confinement-and-the-loss-of-partonic-information-in-biquaternionic-form.html) | 1 | Haar average of automorphisms onto the commutant |

**Non-Abelian Gauge Fields.** The article introduces $F_{\mathrm g,\mu\nu}=\tilde U F_{\mu\nu}\tilde U^{-1}$ at the definition, derives it from the covariance of $D_\mu$, and repeats it in the summary. The derivation uses $U(ab)U^{-1}=(UaU^{-1})(UbU^{-1})$ at every step.

**The Yang–Mills Equation.** The componentwise law is $\tilde U F_{\mu\nu}\tilde U^{-1}$. The article then proves that the packaged curvature $\mathcal F$ does **not** inherit the single-conjugation law, because $\tilde U^{-1}$ does not pass through the basis products $\bar e_\mu e_\nu$. The negative result is a statement about the adjoint action and would read the same with $U^{*}$.

**Gauge Curvature and the Bianchi Identity.** The same law is used to prove that $D_\lambda F_{\mu\nu}$ is covariant and that the Bianchi identity is the Jacobi identity of the covariant derivatives. Both proofs are properties of the automorphism.

**The QCD Agenda.** The adjoint law appears once, as one item in the list of what a gauge theory must supply. The article's point is that the available factor is $SU(2)$, not colour.

**The Standard Model Agenda.** The same law, in the paragraph on the reality class of the connection. The question there is whether the connection can be placed in a fixed Hermitian eigenspace.

**Wilson Loops.** The field strength transforms by conjugation, $\tilde F\mapsto Q\tilde F Q^{-1}$. The gauge invariance of the loop is the invariance of the trace under that action.

**Confinement.** The colour-singlet conditional expectation $E(\tilde Q)=\int_G dU\,U\tilde Q U^{-1}$ averages automorphisms. Its fixed-point algebra is the commutant of the group.

### Adjacent Occurrences, Outside the Nine

The same inverse appears in laws that are not the field-strength law. They are listed so that the nine are not mistaken for the whole of the problem.

| article | object |
|---|---|
| [Non-Abelian Gauge Fields](../articles_physics/non-abelian-gauge-fields-in-biquaternionic-form.html) | the connection law $A_\mu\mapsto UA_\mu U^{-1}+\tfrac{i}{\kappa}(\partial_\mu U)U^{-1}$ |
| [The Yang–Mills Path Integral and the Faddeev–Popov Procedure](../articles_physics/the-yang-mills-path-integral-and-the-faddeev-popov-procedure-in-biquaternionic-form.html) | the same connection law, and the current $J_\nu\mapsto UJ_\nu U^{-1}$ |
| [Electroweak Theory — A Research Agenda](../articles_physics/electroweak-theory-under-the-biquaternion-framework-a-research-agenda.html) | the connection law and its summary table |
| [Instantons and Solitons](../articles_physics/instantons-and-solitons-in-biquaternionic-form.html) | the packaged curvature $\mathcal F_2\neq \tilde U\mathcal F\tilde U^{-1}$ |
| [Wilson Loops](../articles_physics/wilson-loops-in-biquaternionic-form.html) | the connection law and the holonomy $U(C)\mapsto Q\,U(C)\,Q^{-1}$ |
| [The Hopf Fibration and the Biquaternion Gauge Bundle](../articles_physics/the-hopf-fibration-and-the-biquaternion-gauge-bundle.html) | the conjugation of a vector $\vec u\mapsto \tilde U\vec u\tilde U^{-1}$ |

These are the same defect in different places. A repair of the nine that leaves these untouched would be a repair of a count, not of a formalism.

## The Categories

The component description appears in eight of the twelve categories of `physics.md`. Four categories do not use it at all.

| category | physics.md | articles | subsections |
|---|---:|---:|---|
| Biquaternion Universe | 3 | 0 | — |
| Biquaternion Physical Interpretation of Mathematics | 42 | 0 | — |
| Biquaternion Non Relativistic Quantum Theory | 187 | 1 | Particles of spin 1/2 (1) |
| Biquaternion Non Relativistic Non Quantum Theory | 424 | 0 | — |
| Biquaternion Electromagnetism | 511 | 3 | no subsection (3) |
| Biquaternion Relativity | 588 | 1 | no subsection (1) |
| Biquaternion Relativistic Quantum Theory | 650 | 2 | Generalities (1); Particles of spin 1 and above (1) |
| Biquaternion Relativistic Non Quantum Theory | 812 | 1 | Generalities (1) |
| Biquaternion Quantum Fields | 871 | 4 | Generalities (1); Particles of spin 1 and above (3) |
| Biquaternion Particle Physics and Gauge Fields | 1087 | 24 | Generalities (11); Particles of spin 1/2 (4); Particles of spin 1 and above (7); Focus on informational aspects (2) |
| Biquaternion Gravity and Cosmology | 1256 | 1 | no subsection (1) |
| Biquaternion Thermodynamics and Statistical Mechanics | 1291 | 0 | — |

Subsection names follow `physics.md`. The dagger marks the seven articles of the non-Hermitian adjoint.

## The Articles by Category

### Biquaternion Non Relativistic Quantum Theory (1)

| article | subsection | tokens | `[A,A]` |
|---|---|---:|---|
| [The Berry Phase and Geometric Phases in Biquaternionic Form](../articles_physics/the-berry-phase-and-geometric-phases-in-biquaternionic-form.html) | Particles of spin 1/2 | 17 | — |

### Biquaternion Electromagnetism (3)

| article | subsection | tokens | `[A,A]` |
|---|---|---:|---|
| [Maxwell's Theory on Non-Commutative Spaces and Quaternions](../articles_physics/maxwells-theory-on-non-commutative-spaces-and-quaternions.html) | — | 19 | yes |
| [The Algebrodynamical Programme: Nonlinear Cauchy–Riemann Conditions, Self-Quantized Charge, and Induced Causal Geometry](../articles_physics/the-algebrodynamical-programme-nonlinear-cauchy-riemann-and-self-quantized-charge.html) | — | 8 | — |
| [Gauge Transformations of the First and Second Kind in Biquaternionic Form](../articles_physics/gauge-transformations-of-the-first-and-second-kind-in-biquaternionic-form.html) | — | 3 | — |

### Biquaternion Relativity (1)

| article | subsection | tokens | `[A,A]` |
|---|---|---:|---|
| [The Relativistic Particle in an External Field, in Biquaternionic Form](../articles_physics/the-relativistic-particle-in-an-external-field-in-biquaternionic-form.html) | — | 3 | — |

### Biquaternion Relativistic Quantum Theory (2)

| article | subsection | tokens | `[A,A]` |
|---|---|---:|---|
| [Dual Equivalence of the Dirac and Topologically Massive Gauge Fields](../articles_physics/dual-equivalence-of-the-dirac-and-topologically-massive-gauge-fields.html) | Particles of spin 1 and above | 6 | — |
| [The Relativistic Action and the Stationary-Action Principle in Biquaternionic Form](../articles_physics/the-relativistic-action-and-the-stationary-action-principle-in-biquaternionic-form.html) | Generalities | 3 | — |

### Biquaternion Relativistic Non Quantum Theory (1)

| article | subsection | tokens | `[A,A]` |
|---|---|---:|---|
| [Stress–Energy, Conservation Laws and the Field Action in Biquaternionic Form](../articles_physics/stress-energy-conservation-laws-and-the-field-action-in-biquaternionic-form.html) | Generalities | 9 | — |

### Biquaternion Quantum Fields (4)

| article | subsection | tokens | `[A,A]` |
|---|---|---:|---|
| [Wilson Loops in Biquaternionic Form](../articles_physics/wilson-loops-in-biquaternionic-form.html) † | Particles of spin 1 and above | 13 | — |
| [The Theta Vacuum in Biquaternionic Form](../articles_physics/the-theta-vacuum-in-biquaternionic-form.html) | Generalities | 10 | — |
| [Canonical Quantization of the Biquaternion Maxwell Field](../articles_physics/canonical-quantization-of-the-biquaternion-maxwell-field.html) | Particles of spin 1 and above | 7 | — |
| [Canonical Quantization of the Biquaternion Proca Field](../articles_physics/canonical-quantization-of-the-biquaternion-proca-field.html) | Particles of spin 1 and above | 6 | — |

### Biquaternion Particle Physics and Gauge Fields (24)

| article | subsection | tokens | `[A,A]` |
|---|---|---:|---|
| [Gauge Curvature and the Bianchi Identity in Biquaternionic Form](../articles_physics/gauge-curvature-and-the-bianchi-identity-in-biquaternionic-form.html) † | Generalities | 151 | yes |
| [Non-Abelian Gauge Fields in Biquaternionic Form](../articles_physics/non-abelian-gauge-fields-in-biquaternionic-form.html) † | Particles of spin 1 and above | 117 | yes |
| [The Yang–Mills Equation in Biquaternionic Form](../articles_physics/the-yang-mills-equation-in-biquaternionic-form.html) † | Particles of spin 1 and above | 97 | yes |
| [Instantons and Solitons in Biquaternionic Form](../articles_physics/instantons-and-solitons-in-biquaternionic-form.html) | Generalities | 53 | yes |
| [Lattice Gauge Theory and the Biquaternion Path Integral](../articles_physics/lattice-gauge-theory-and-the-biquaternion-path-integral.html) | Particles of spin 1 and above | 47 | yes |
| [The Yang–Mills Path Integral and the Faddeev–Popov Procedure in Biquaternionic Form](../articles_physics/the-yang-mills-path-integral-and-the-faddeev-popov-procedure-in-biquaternionic-form.html) | Particles of spin 1 and above | 30 | yes |
| [The Standard Model under the Biquaternion Framework — A Research Agenda](../articles_physics/the-standard-model-under-the-biquaternion-framework-a-research-agenda.html) † | Generalities | 25 | yes |
| [The Fujikawa Method and the Path-Integral Anomaly in Biquaternionic Form](../articles_physics/the-fujikawa-method-and-the-path-integral-anomaly-in-biquaternionic-form.html) | Particles of spin 1/2 | 24 | — |
| [Electroweak Theory under the Biquaternion Framework — A Research Agenda](../articles_physics/electroweak-theory-under-the-biquaternion-framework-a-research-agenda.html) | Generalities | 22 | yes |
| [The Gauge Principle in Biquaternionic Form](../articles_physics/the-gauge-principle-in-biquaternionic-form.html) | Generalities | 21 | yes |
| [The Covariant Derivative and Gauge Connection in Biquaternionic Form](../articles_physics/the-covariant-derivative-and-gauge-connection-in-biquaternionic-form.html) | Generalities | 20 | yes |
| [Quantum Chromodynamics under the Biquaternion Framework — A Research Agenda](../articles_physics/quantum-chromodynamics-under-the-biquaternion-framework-a-research-agenda.html) † | Generalities | 18 | yes |
| [Chiral Fermions in the Biquaternion Framework](../articles_physics/chiral-fermions-in-the-biquaternion-framework.html) | Particles of spin 1/2 | 12 | — |
| [The Theta Parameter and Strong CP in Biquaternionic Form](../articles_physics/the-theta-parameter-and-strong-cp-in-biquaternionic-form.html) | Generalities | 11 | — |
| [The Gluon: An Octet Outside the Biquaternion Algebra](../articles_physics/the-gluon-an-octet-outside-the-biquaternion-algebra.html) | Particles of spin 1 and above | 11 | yes |
| [Anomalies and Anomaly Cancellation in Biquaternionic Form](../articles_physics/anomalies-and-anomaly-cancellation-in-biquaternionic-form.html) | Particles of spin 1/2 | 9 | — |
| [The Stueckelberg Mechanism in Biquaternionic Form](../articles_physics/the-stueckelberg-mechanism-in-biquaternionic-form.html) | Particles of spin 1 and above | 8 | — |
| [The W and Z Bosons in Biquaternionic Form](../articles_physics/the-w-and-z-bosons-in-biquaternionic-form.html) | Particles of spin 1 and above | 7 | yes |
| [The Index Theorem and the Zero-Mode Count in Biquaternionic Form](../articles_physics/the-index-theorem-and-the-zero-mode-count-in-biquaternionic-form.html) | Generalities | 6 | — |
| [The Electric Dipole Moment and the Biquaternion Anti-Hermitian Structure](../articles_physics/the-electric-dipole-moment-and-the-biquaternion-anti-hermitian-structure.html) | Particles of spin 1/2 | 6 | — |
| [Electric–Magnetic Duality and the Modular Group in Biquaternionic Form](../articles_physics/electric-magnetic-duality-and-the-modular-group-in-biquaternionic-form.html) | Generalities | 4 | — |
| [Gauge Redundancy and the Information in the Gauge Orbit in Biquaternionic Form](../articles_physics/gauge-redundancy-and-the-information-in-the-gauge-orbit-in-biquaternionic-form.html) | Focus on informational aspects | 4 | — |
| [The Higgs Mechanism as an Erasure of Information in Biquaternionic Form](../articles_physics/the-higgs-mechanism-as-an-erasure-of-information-in-biquaternionic-form.html) | Focus on informational aspects | 4 | — |
| [The Semiclassical Expansion and the Instanton Gas in Biquaternionic Form](../articles_physics/the-semiclassical-expansion-and-the-instanton-gas-in-biquaternionic-form.html) | Generalities | 3 | — |

**Below the threshold.** [Confinement and the Loss of Partonic Information](../articles_physics/confinement-and-the-loss-of-partonic-information-in-biquaternionic-form.html) belongs to the informational aspects of this category and is the seventh article of the non-Hermitian list. It writes the holonomy $U(C)=\mathcal P\exp(i\oint A_\mu\,dx^\mu)$ and no field strength, so it falls below the three-token threshold used for these tables. It is counted in §*The Non-Hermitian Adjoint*.

### Biquaternion Gravity and Cosmology (1)

| article | subsection | tokens | `[A,A]` |
|---|---|---:|---|
| [Curved Spacetime and the Biquaternion Framework](../articles_physics/curved-spacetime-and-the-biquaternion-framework.html) | — | 3 | — |



## What the Counts Do Not Say

- **They do not report an arithmetic error.** All nine parameters are unitary, so all nine formulas are numerically equal to the Hermitian form. No result in the corpus changes if $U^{-1}$ is replaced by $U^{*}$.
- **They do not single out the seven as bad articles.** The seven are the places where the field-strength law is written. The same inverse appears in the connection laws of the articles listed above, and the index calculus appears in thirty-seven articles. The seven are the visible edge of a larger layer.
- **They do not prescribe a replacement.** The formalism is foreign to the algebra, and no article in the corpus removes it. What the count establishes is the size of the task and the places where it is exact.

## Conclusion

The gauge sector of the corpus is written on two layers. The algebra supplies the product, the involution and the trace; the tensor layer supplies the index, the derivative and the fourfold and sixfold copies. The two are not the same object, and the second is not an extension of the first.

The non-Hermitian adjoint is the sharpest trace of the split. It is an automorphism written where the algebra offers a congruence, an inverse written where the algebra offers an adjoint. On the unitary slice the two coincide, which is why the corpus has not had to notice. Off the slice they differ by the square of the modulus.

Nine occurrences in seven articles, nine unitary parameters, one defect.
