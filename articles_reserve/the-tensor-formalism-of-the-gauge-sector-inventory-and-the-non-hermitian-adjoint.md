# __The Tensor Formalism of the Gauge Sector: Where It Is, and the Non-Hermitian Adjoint__

## Introduction

The gauge articles of the physics corpus use two descriptions at once. One is the biquaternion algebra: a product, an involution, a trace. The other is a component description: an index $\mu$, a derivative $\partial_\mu$, a one-form $A_\mu$, a two-form $F_{\mu\nu}$. The second description is not contained in the first. It is a foreign layer, and this article records where it sits.

One count organises the record, and it replaces the count of an earlier version of this article. **Fifteen articles that use the component description write at least one conjugation with an inverse**, $X\mapsto GXG^{-1}$, where the algebra supplies an involution that could stand in its place. The field-strength law alone, $F\mapsto UFU^{-1}$, is written on **thirty-three lines in ten of those articles**.

The earlier version reported nine occurrences in seven articles. That number was a count of distinct statement sites, not of written occurrences, and it was wrong in three ways. It included *Confinement and the Loss of Partonic Information*, which writes no field strength at all. It listed *Electroweak Theory* and *Instantons and Solitons* only as adjacent, although both write the field-strength law. And it omitted *The Stueckelberg Mechanism*, which writes it once. The corrected lists are below, with a line number for every entry.

The defect is not an error of value. On the compact slice $U^{-1}=U^{*}$, so every formula listed here is numerically equal to its Hermitian form. The defect is one of provenance: a law of the algebra written with an operation the algebra does not own.

This article is an inventory. It does not propose a replacement for the component layer, and it does not claim that one is available.

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

The last point is where a blanket repair fails. The algebra has two involutions that reverse an element, and they coincide with the inverse on different slices.

| conjugating element | class | $G^{-1}$ equals | is $G^{*}=G^{-1}$? |
|---|---|---|---|
| $SU(2)$ element, unit real quaternion | compact | $G^{*}$ and $G^{\natural}$ | yes |
| unit-norm Lorentz rotor, including a boost | non-compact | $G^{\natural}$ only | no |
| odd Clifford element $\Pi$ | pseudoautomorphism | $\Pi$ itself, $\Pi^{2}=\pm1$ | yes, up to sign |

So the replacement of $U^{-1}$ by $U^{*}$ is silent in the compact articles, and it is wrong on the Lorentz slice. There the correct rewrite is $U^{-1}\to U^{\natural}$. The example is the boost rotor of *Exercise: Duality Rotation and the Riemann–Silberstein Vector*,
$$
\tilde U_{\mathrm b}=\cosh\tfrac{\psi}{2}\,e_t+i\sinh\tfrac{\psi}{2}\,\vec u_{\mathrm b},
\qquad
\tilde U_{\mathrm b}^{*}=\tilde U_{\mathrm b},
\qquad
\tilde U_{\mathrm b}^{\natural}=\tilde U_{\mathrm b}^{-1}.
$$
A blind substitution of ${}^{*}$ for ${}^{-1}$ therefore doubles the rapidity instead of reversing it. That article records the failure explicitly: the rotation is reproduced by $\tilde U\tilde F\tilde U^{*}$, the boost only by $\tilde U^{-1}\tilde F\tilde U$.

One gauge article sits on the non-compact slice. *Curved Spacetime and the Biquaternion Framework* writes the connection on the spinor module as
$$
\vec\Gamma_\mu \longmapsto \tilde U\vec\Gamma_\mu\tilde U^{-1}
-\left(\partial/\partial Q_\mu\,\tilde U\right)\tilde U^{-1},
$$
with $\tilde U$ a Lorentz rotor, an element of $SL(2,\mathbb{C})$ rather than $SU(2)$. There the inverse is load-bearing and the star is not its equal. The earlier version's statement that every gauge parameter in the corpus is unitary is false for this article.

## The Field-Strength Law: Ten Articles, Thirty-Three Lines

The law $F\mapsto UFU^{-1}$ is written on the following lines. The count is of distinct lines; a line that states the law twice is counted once.

| article | lines | count |
|---|---|---:|
| [Non-Abelian Gauge Fields in Biquaternionic Form](../articles_physics/non-abelian-gauge-fields-in-biquaternionic-form.html) | 10, 131, 136, 198, 202, 292, 334, 366 | 8 |
| [The Yang–Mills Equation in Biquaternionic Form](../articles_physics/the-yang-mills-equation-in-biquaternionic-form.html) | 43, 82, 105, 111, 229, 232, 235, 383 | 8 |
| [Instantons and Solitons in Biquaternionic Form](../articles_physics/instantons-and-solitons-in-biquaternionic-form.html) | 232, 235, 236, 351 | 4 |
| [Gauge Curvature and the Bianchi Identity in Biquaternionic Form](../articles_physics/gauge-curvature-and-the-bianchi-identity-in-biquaternionic-form.html) | 84, 285, 319 | 3 |
| [Electroweak Theory under the Biquaternion Framework — A Research Agenda](../articles_physics/electroweak-theory-under-the-biquaternion-framework-a-research-agenda.html) | 72, 230 | 2 |
| [Quantum Chromodynamics under the Biquaternion Framework — A Research Agenda](../articles_physics/quantum-chromodynamics-under-the-biquaternion-framework-a-research-agenda.html) | 52, 236 | 2 |
| [The Standard Model under the Biquaternion Framework — A Research Agenda](../articles_physics/the-standard-model-under-the-biquaternion-framework-a-research-agenda.html) | 84, 315 | 2 |
| [The Yang–Mills Path Integral and the Faddeev–Popov Procedure in Biquaternionic Form](../articles_physics/the-yang-mills-path-integral-and-the-faddeev-popov-procedure-in-biquaternionic-form.html) | 31, 52 | 2 |
| [The Stueckelberg Mechanism in Biquaternionic Form](../articles_physics/the-stueckelberg-mechanism-in-biquaternionic-form.html) | 226 | 1 |
| [Wilson Loops in Biquaternionic Form](../articles_physics/wilson-loops-in-biquaternionic-form.html) | 5 | 1 |

The three additions to the earlier list are *Electroweak*, *Instantons* and *Stueckelberg*. The removal is *Confinement*, which writes $E(\tilde Q)=\int_G dU\,U\tilde Q U^{-1}$ — a Haar average of automorphisms, not a field strength.

## The Gauge Articles: Fifteen

Every article below uses the component layer and writes at least one sandwich with an inverse. The representative formula is the first occurrence in the article that is not a repetition in a summary.

| article | representative | line | element | $G^{*}=G^{-1}$? |
|---|---|---|---:|---|
| [Non-Abelian Gauge Fields](../articles_physics/non-abelian-gauge-fields-in-biquaternionic-form.html) | $F_{\mathrm g,\mu\nu}=\tilde QF_{\mu\nu}\tilde Q^{-1}$ | 10 | $SU(2)$ | yes |
| [The Yang–Mills Equation](../articles_physics/the-yang-mills-equation-in-biquaternionic-form.html) | $F_{2,\mu\nu}=\tilde UF_{\mu\nu}\tilde U^{-1}$ | 43 | $SU(2)$ | yes |
| [The Yang–Mills Path Integral and the Faddeev–Popov Procedure](../articles_physics/the-yang-mills-path-integral-and-the-faddeev-popov-procedure-in-biquaternionic-form.html) | $\mathcal A_{2,\mu}=\tilde U\mathcal A_\mu\tilde U^{-1}+\tfrac{i}{\kappa}(\partial_\mu\tilde U)\tilde U^{-1}$ | 54 | $SU(2)$ | yes |
| [Gauge Curvature and the Bianchi Identity](../articles_physics/gauge-curvature-and-the-bianchi-identity-in-biquaternionic-form.html) | $F_{\mathrm g,\mu\nu}=\tilde UF_{\mu\nu}\tilde U^{-1}$ | 84 | $SU(2)$ | yes |
| [Quantum Chromodynamics — A Research Agenda](../articles_physics/quantum-chromodynamics-under-the-biquaternion-framework-a-research-agenda.html) | $F_{2,\mu\nu}=\tilde UF_{\mu\nu}\tilde U^{-1}$ | 52 | $SU(2)$ | yes |
| [The Standard Model — A Research Agenda](../articles_physics/the-standard-model-under-the-biquaternion-framework-a-research-agenda.html) | $F_{2,\mu\nu}=\tilde UF_{\mu\nu}\tilde U^{-1}$ | 84 | $SU(2)$ | yes |
| [Electroweak Theory — A Research Agenda](../articles_physics/electroweak-theory-under-the-biquaternion-framework-a-research-agenda.html) | $F_{2,\mu\nu}=\tilde UF_{\mu\nu}\tilde U^{-1}$ | 72 | $SU(2)$ | yes |
| [Wilson Loops](../articles_physics/wilson-loops-in-biquaternionic-form.html) | $\tilde F\mapsto Q\tilde FQ^{-1}$ | 5 | $SU(2)$ | yes |
| [Confinement and the Loss of Partonic Information](../articles_physics/confinement-and-the-loss-of-partonic-information-in-biquaternionic-form.html) | $E(\tilde Q)=\int_G dU\,U\tilde QU^{-1}$ | 183 | $SU(2)$ | yes |
| [Gauge Redundancy and the Information in the Gauge Orbit](../articles_physics/gauge-redundancy-and-the-information-in-the-gauge-orbit-in-biquaternionic-form.html) | $A_\mu\mapsto\tilde QA_\mu\tilde Q^{-1}+\tfrac{i}{\kappa}(\partial_\mu\tilde Q)\tilde Q^{-1}$ | 280 | $SU(2)$ | yes |
| [Curved Spacetime and the Biquaternion Framework](../articles_physics/curved-spacetime-and-the-biquaternion-framework.html) | $\vec\Gamma_\mu\mapsto\tilde U\vec\Gamma_\mu\tilde U^{-1}-(\partial_\mu\tilde U)\tilde U^{-1}$ | 255 | $SL(2,\mathbb{C})$ | **no** |
| [Instantons and Solitons](../articles_physics/instantons-and-solitons-in-biquaternionic-form.html) | $\mathcal F_2=\tfrac12\sum(\tilde UF_{\mu\nu}\tilde U^{-1})\bar e_\mu e_\nu$ | 235 | $SU(2)$ | yes |
| [The Hopf Fibration and the Biquaternion Gauge Bundle](../articles_physics/the-hopf-fibration-and-the-biquaternion-gauge-bundle.html) | $\vec u\mapsto\tilde U\vec u\tilde U^{-1}$ | 70 | $SU(2)$ | yes |
| [The Higgs Mechanism](../articles_physics/the-higgs-mechanism-in-biquaternionic-form.html) | $\tilde\Phi\mapsto U\tilde\Phi U^{-1}$ | 201 | $SU(2)$ | yes |
| [The Stueckelberg Mechanism](../articles_physics/the-stueckelberg-mechanism-in-biquaternionic-form.html) | $F_{2,\mu\nu}=UF_{\mu\nu}U^{-1}$ | 226 | $SU(2)$ | yes |

Fourteen of the fifteen are on the compact slice, where the inverse and the star agree and no number changes. One is not. The distinction is not a detail of bookkeeping: it decides which repair is correct.

## What the Counts Do Not Say

- **They do not report an arithmetic error.** On the compact slice all parameters are unitary, so every formula there is numerically equal to its Hermitian form. No result in the corpus changes if $U^{-1}$ is replaced by $U^{*}$ in those articles.
- **They do not licence one global replacement.** The Lorentz articles — the curved-spacetime connection, and two articles outside the gauge sector — need $U^{-1}\to U^{\natural}$, not $U^{-1}\to U^{*}$. A corpus-wide search and replace with the star would break them.
- **They do not single out the fifteen as bad articles.** The fifteen are the places where the component layer and the inverse meet. The same inverse appears in articles that do not use the component layer at all; the companion article *The Non-Hermitian Adjoint Outside the Gauge Sector* counts them, and records the four that are now written with the Hermitian sandwich.
- **They do not prescribe a replacement for the component layer.** The index and the derivative remain external. What the count establishes is the size of the layer and the exact places where its algebra is written with an operation it does not own.

## Conclusion

The gauge sector of the corpus is written on two layers. The algebra supplies the product, the involution and the trace; the tensor layer supplies the index, the derivative and the fourfold and sixfold copies. The two are not the same object, and the second is not an extension of the first.

The non-Hermitian adjoint is the sharpest trace of the split. It is an automorphism written where the algebra offers a congruence, an inverse written where the algebra offers an adjoint. On the compact slice the two coincide, which is why the corpus has not had to notice. Off that slice they part company, and the articles that live off it are the ones that fix the repair.

Fifteen gauge articles, thirty-three lines for the field-strength law alone, one non-compact case.
