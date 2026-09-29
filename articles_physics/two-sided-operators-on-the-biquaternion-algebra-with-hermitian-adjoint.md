# __Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint__

## Introduction

The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries the Hermitian conjugation ${}^{\dagger}$ whose fixed space is the informational sector $\mathbb{M}_+$ and whose anti-fixed space is the material sector $\mathbb{M}_-$ (*Biquaternion Algebra*, *The Hermitian Subspace M+ as the Informational Sector*, *The Anti-Hermitian Subspace M− as the Material Sector*). The corpus uses one two-sided operator throughout, the **dagger sandwich**

$$
\Theta_{\tilde{Q}}(\tilde T) = \tilde{Q}\,\tilde T\,\tilde{Q}^{\dagger} ,
$$

the transformation of the algebra by an element and its adjoint: it is the transformation of the material sector in *Biquaternion Rotations and Lorentz Transformations*, the congruence $\tilde{Q}\mapsto M\tilde{Q} M^{\dagger}$ of *The 2×2 Matrix Element Representation of Biquaternions*, and the operator of *The Sandwich Action in Subspaces*.

This article is the physics companion of *Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint* of the mathematical series. The operator, its adjoint, its composition law and its type theorems are proved there and are cited here; what this article adds is the physical reading, the physical examples, and the two traps that a reader coming from the physics meets first.

## The Dagger, the Form and the Two Sectors

The scalar form of the dagger is the Euclidean form of the coefficient space,

$$
(\tilde R,\tilde T) = \mathrm{Sc}(\tilde R^{\dagger}\tilde T) = \sum_{\mu}R_{\mu}^{*}T_{\mu} ,
$$

positive definite, with Gram matrix the identity in the basis $e_{0},e_{1},e_{2},e_{3}$. **This is not the metric of spacetime**, and the first trap is to confuse the two forms. They have different carriers: the form $(\cdot,\cdot)$ is positive definite on the whole eight-dimensional real algebra and belongs to the internal structure; the **quaternion norm** $N(\tilde{Q})=\sum_{\mu}Q_{\mu}^{2}$, complex and indefinite, is the one whose restriction to the material sector carries the Minkowski interval (*Biquaternion Norm and Invertibility*, *The Clifford Structure of the Biquaternion Algebra*). Positivity lives on the internal space; the signature $(1,3)$ lives on the material space, and no statement of one form transfers to the other.

The second trap is the action of the dagger on the coefficients. For $\tilde{Q}=\sum_{\mu}Q_{\mu}e_{\mu}$,

$$
\tilde{Q}^{\dagger}=Q_{0}^{*}e_{0}-Q_{1}^{*}e_{1}-Q_{2}^{*}e_{2}-Q_{3}^{*}e_{3} ,
$$

so the scalar coefficient is conjugated and the vector coefficients are conjugated **and negated**. The reading of the sectors follows: the informational sector is the set of $ae_{0}+i(b_{1}e_{1}+b_{2}e_{2}+b_{3}e_{3})$ with real coefficients, a real scalar part and an imaginary vector part; the material sector is the set of $ib_{0}e_{0}+(c_{1}e_{1}+c_{2}e_{2}+c_{3}e_{3})$ with real coefficients, an imaginary scalar part and a real vector part. In particular $ie_{3}$ is **Hermitian** and $e_{3}$ is **anti-Hermitian**, which is the opposite of what the notation suggests and the source of most mistakes with this operator.

## The Parameter Rules and the Two Invisibilities

The assignment $\tilde{Q}\mapsto \Theta_{\tilde{Q}}$ is multiplicative and quadratic: $\Theta_{\tilde{Q}\tilde{S}}=\Theta_{\tilde{Q}}\circ \Theta_{\tilde{S}}$, and for a central scalar $\lambda e_{0}$,

$$
\Theta_{\lambda\tilde{Q}}=\lvert\lambda\rvert^{2}\Theta_{\tilde{Q}} .
$$

Three readings follow.

**The phase is invisible.** $\Theta_{i\tilde{Q}}=\Theta_{\tilde{Q}}$, and more generally $\Theta_{\omega\tilde{Q}}=\Theta_{\tilde{Q}}$ for $\lvert\omega\rvert=1$. The operator depends on the whole element only through the combination $\tilde{Q}\tilde{Q}^{\dagger}$, so it is blind to the central phase: this is the phase freedom of a state, and the operator can never detect it.

**The sign is invisible.** $\Theta_{-\tilde{Q}}=\Theta_{\tilde{Q}}$. The elements $\tilde{Q}$ and $-\tilde{Q}$ lie in opposite sectors when $\tilde{Q}$ is a sector element, and yet define the same transformation. The physical content is the double cover: the operator sees the pair $\{\pm \tilde R\}$, and the sector label of the parameter is not an observable of the transformation.

**The amplitude is quadratic.** A scale enters as $\lvert\lambda\rvert^{2}$. The operator is quadratic in the amplitude, exactly as a state is quadratic in a state vector: the analogy is not superficial, and the image of the identity below makes it exact.

## The Adjoint and the Observable Operators

The adjoint of $\Theta_{\tilde{Q}}$ for the form $(\cdot,\cdot)$ is a two-sided operator, of the adjoint element:

$$
(\Theta_{\tilde{Q}})^{*}=\Theta_{\tilde{Q}^{\dagger}} .
$$

**Theorem (the observables).** For $\tilde{Q}\neq0$ the operator $\Theta_{\tilde{Q}}$ is self-adjoint if and only if $\tilde{Q}^{\dagger}=\omega\tilde{Q}$ with $\lvert\omega\rvert=1$. In particular every element of the informational sector and every element of the material sector gives a self-adjoint operator, and the two sectors give the **same** family of operators.

*The statement is the mathematical theorem of the companion article; its verification over the two sectors and over the singular Hermitian elements is reported there.*

**Physical reading.** A two-sided operator is a candidate observable as soon as its parameter is a sector element, and the assignment **cannot tell information from matter**: the informational operators and the material operators coincide. Whatever distinguishes the two sectors is not visible to a sandwich; it is visible only in the norm $N$ and in the equations of motion, which is why the corpus keeps the two sectors separate in the norm and in the dynamics and not in the operators.

**No two-sided operator is skew.** If $\Theta_{\tilde{Q}}$ were skew-adjoint, evaluating on the identity would give $\tilde{Q}^{\dagger}\tilde{Q}=-\tilde{Q}\tilde{Q}^{\dagger}$ and the scalar part would give $\sum_{\mu}\lvert Q_{\mu}\rvert^{2}=0$, so $\tilde{Q}=0$. Physically, the infinitesimal generators of the internal group are therefore **not** two-sided: a two-sided antisymmetric object would be the anticommutator $\tilde R\tilde T+\tilde T\tilde{Q}^{\dagger}$, and the generators of the internal group are one-sided instead, as the companion article *One-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint* shows.

## The Slice, the Automorphisms and the Lorentz Action

The unitary slice is $U=\{\tilde R:\tilde{Q}^{\dagger}\tilde{Q}=e_{0}\}=U(2)$, of real dimension four, with determinant-one part $\mathrm{SU}(2)\cong\mathrm{Spin}(3)$ (*The Hermitian Sandwich in the Biquaternion Algebra with Hermitian Adjoint*, *The Biquaternion Unit Group as a Topological Group*).

**Theorem (the automorphisms are the slice).** $\Theta_{\tilde{Q}}$ is an algebra automorphism of $\mathbb{B}$ if and only if $\tilde{Q}\in U$, and then $\tilde{Q}^{\dagger}=\tilde{Q}^{-1}$ and $\Theta_{\tilde{Q}}(\tilde T)=\tilde R\tilde T\tilde{Q}^{-1}$.

**Corollary (the Lorentz action is not an automorphism).** A Lorentz transformation is produced by an element of unit norm, $\lvert N(\tilde{Q})\rvert=1$, which lies in $SL(2,\mathbb{C})$ up to phase and not in $U(2)$ in general. The boosts are Hermitian elements of unit norm, and a Hermitian element is unitary for the dagger only when it is central. So the Lorentz action is **not** an automorphism of the algebra: it is the similarity of the quaternion norm, it preserves the interval and not the dagger form. The corpus states the same contrast from the group side — $U(2)$ acts by automorphisms and fixes the dagger form, while $SL(2,\mathbb{C})$ acts by the similarities of $N$ and gives the Lorentz action on the material sector (*Biquaternion Versors and the Orthogonal Group*, *Biquaternion Rotations and Lorentz Transformations*) — and the operator theorem gives the reason in one line: an automorphism needs $\tilde{Q}^{\dagger}\tilde{Q}=e_{0}$, and a boost has $\tilde{Q}^{\dagger}\tilde{Q}=\tilde{Q}^{2}$, a Hermitian square and not the identity.

**The two families are disjoint, and they are the two physical classes.** The theorem and the adjoint theorem separate the two-sided operators into two families that a physicist uses daily:

| parameter $\tilde{Q}$ | $\Theta_{\tilde{Q}}$ | physical object |
|---|---|---|
| a rotor, $\tilde{Q}\in\mathrm{SU}(2)\subset U$ | unitary, automorphism, **not** self-adjoint | a symmetry of the internal space |
| a boost, $\tilde{Q}\in\mathbb{M}_+$ Hermitian of unit norm | self-adjoint, **not** unitary, **not** automorphism | a change of inertial frame, an observable |
| a phase, $\tilde{Q}=\omega e_{0}$ | the identity | unobservable |

A rotation is a symmetry and not an observable; a boost is an observable and not a symmetry; a phase is neither. The two-sided operator article explains why: the automorphism property requires $\tilde{Q}^{\dagger}\tilde{Q}=e_{0}$ and the self-adjointness requires $\tilde{Q}^{\dagger}=\omega\tilde{Q}$, and a rotor satisfies the first and a boost the second, and no non-central element satisfies both.

## The Image of the Identity: the Cone, the States and the Channels

**Proposition.** $\Theta_{\tilde{Q}}(e_{0})=\tilde{Q}\tilde{Q}^{\dagger}$, and it is the identity exactly on the slice. In the matrix model $\Phi(\tilde{Q}\tilde{Q}^{\dagger})=MM^{\dagger}$ is the Gram matrix of the columns of $M=\Phi(\tilde{Q})$ (*The 2×2 Matrix Element Representation of Biquaternions*).

Three physical readings of the same display:

1. **The state reading.** The set $\{\tilde{Q}\tilde{Q}^{\dagger}\}$ is the cone of the positive semidefinite Hermitian elements, and on its trace-one slice it is the set of the states of the internal space: this is exactly the corpus's Bloch ball, the trace-one slice of the future light cone (*The Bloch Ball as the Trace-One Slice of the Future Light Cone*, and for the spin-one case *The Generalized Bloch Ball for Spin 1 in the Biquaternion Framework*). The map from the amplitude to the state is quadratic in the amplitude, as the parameter rule requires.
2. **The pure-state reading.** For an idempotent $\tilde\Pi=\tfrac12(e_{0}+i\hat{\mathbf{u}})$ of the informational sector, $\Theta_{\tilde\Pi}(e_{0})=\tilde\Pi^{2}=\tilde\Pi$: a rank-one projection, a pure state, the projector onto a Weyl spinor. The corpus's idempotents and their orthogonal pairs are exactly the orthogonal pairs of pure states (*Biquaternion Idempotents and Projections*).
3. **The channel reading.** The two-sided operators are congruences, hence positive maps; the trace-preserving ones among them are the quantum channels of the framework, and the phase blindness $\Theta_{\omega\tilde{Q}}=\Theta_{\tilde{Q}}$ is the statement that a channel acts on states and not on amplitudes (*Quantum Channels and the Reversible–Irreversible Dichotomy*, *Exercise: Quantum Channels and Dephasing in M−*, and in the mathematical series *Completely Positive Maps of a Clifford Algebra with Hermitian Adjoint*).

## The Collapse by a Null Element

Let $\tilde{Q}=e_{0}+ie_{3}$, of norm $N(\tilde{Q})=1+i^{2}=0$: a zero divisor, the algebraic form of a lightlike direction. The element is Hermitian, so $\Theta_{\tilde{Q}}$ is self-adjoint, and

$$
\Theta_{\tilde{Q}}(e_{0})=\tilde{Q}^{2}=2(e_{0}+ie_{3})=2\tilde{Q} ,
$$

a Hermitian element of rank one, since $\Phi(\tilde{Q})=\mathrm{diag}(2,0)$ in the matrix model. The operator maps the algebra onto a rank-one corner and is neither unitary nor an automorphism.

**Physical reading.** A two-sided operator built from a **null** element loses one internal direction: it is the degenerate limit of the transformation, and its rank collapses exactly when the norm vanishes. The corpus meets the same cone in the polar representation, which fails on the null cone, and in the null quadric (*Biquaternion Polar Element Representation*, *Biquaternion Null Quadric and Projective Geometry*): the interior of the cone $\{\tilde{Q}\tilde{Q}^{\dagger}\}$ is the image of the invertible elements, and the boundary is the image of the zero divisors. The two statements are one.

## Congruence, Unitary Equivalence and the Two Frame Changes

Two equivalence relations act on the operators, and the physics uses both without naming them.

**Congruence** is the change of the internal basis by an invertible element: $\Theta_{\tilde{Q}}\mapsto \Theta_{a}^{-1}\Theta_{\tilde{Q}}\Theta_{a}=\Theta_{a^{-1}\tilde{Q}a}$ for $a\in\mathbb{B}^{\times}$, of invariant the **inertia** of the form the operator carries. A change of representative, a gauge, or any invertible relabelling acts this way.

**Unitary equivalence** is the change of the internal basis by an element of the slice: $\Theta_{\tilde{Q}}\mapsto \Theta_{u}^{-1}\Theta_{\tilde{Q}}\Theta_{u}=\Theta_{u^{-1}\tilde{Q}u}$ for $u\in U$, of invariant the **spectrum**. An internal symmetry acts this way.

The two relations agree on the slice and unitary equivalence is strictly finer off it: two operators can have the same inertia and different spectra, and then they are congruent and not unitarily equivalent. The physical content is the difference between a **basis change** and a **symmetry**: only the second preserves the observable content of the operator, and only the second is implemented by an element of the internal group. The general theory, with the Sylvester invariants and the operator form of the Sylvester equation, is *Unitary Equivalence and Congruence of Operators with Hermitian Adjoint* and *The Hermitian Sylvester Equation with Hermitian Adjoint* in the mathematical series.

## Worked Examples in Physical Terms

**The phase.** For $\tilde{Q}=\omega e_{0}$ with $\lvert\omega\rvert=1$ the operator is the identity, so an overall phase of a spinor or of a state produces no transformation. This is the operator form of the phase freedom, and it is the reason the corpus's physical statements are always phase-blind.

**A rotation.** Let $\tilde{Q}$ be a unit real quaternion, $\tilde{Q}=\cos(\theta/2)+\sin(\theta/2)\hat{\mathbf{u}}$, of real coefficients. Then $\tilde{Q}^{\dagger}=\tilde{Q}^{*}=\tilde{Q}^{-1}$ and $\tilde{Q}^{\dagger}\tilde{Q}=e_{0}$, so $\tilde{Q}\in U$ and $\Theta_{\tilde{Q}}$ is a unitary operator and an algebra automorphism; and $\tilde{Q}$ has a real vector part, so it is not Hermitian and $\Theta_{\tilde{Q}}$ is not self-adjoint. On the vector subspace $\Theta_{\tilde{Q}}$ is the rotation by $\theta$, which is the corpus's sandwich reading of a rotor, with the doubling of the angle coming from the two factors of the sandwich (*Biquaternion Rotations and Lorentz Transformations*). **A rotation is a symmetry, not an observable.**

**A boost.** Let $\tilde{Q}=\cosh(\chi/2)e_{0}+i\sinh(\chi/2)e_{1}$, which is Hermitian because it has a real scalar part and an imaginary vector part, and of norm $N(\tilde{Q})=\cosh^{2}(\chi/2)-\sinh^{2}(\chi/2)=1$. Then

$$
\tilde{Q}^{\dagger}\tilde{Q}=\tilde{Q}^{2}=\cosh\chi\,e_{0}+i\sinh\chi\,e_{1}\neq e_{0} ,
$$

so $\Theta_{\tilde{Q}}$ is self-adjoint and neither unitary nor an automorphism. On the material sector it is the Lorentz boost of rapidity $\chi$, and the doubling of the rapidity has the same origin as the doubling of the angle. **A boost is an observable and a change of frame, not a symmetry of the algebra.**

**A null element.** For $\tilde{Q}=e_{0}+ie_{3}$ the operator is self-adjoint of rank one, as computed above: the lightlike direction is lost.

**A Hermitian sector element in general.** For $\tilde{Q}$ in the informational sector, $\tilde{Q}^{\dagger}=\tilde{Q}$ and $\Theta_{\tilde{Q}}$ is self-adjoint with $\Theta_{\tilde{Q}}(e_{0})=\tilde{Q}^{2}$, so the whole informational sector acts by self-adjoint operators whose image of the identity is the square of the element; for the material sector the same family is obtained through $\Theta_{i\tilde{Q}}=\Theta_{\tilde{Q}}$, which is the statement that the informational and the material sector elements are the same observable operators with the sector label erased.

## Summary

The two-sided operator of the biquaternion algebra is the dagger sandwich $\Theta_{\tilde{Q}}(\tilde T)=\tilde{Q}\tilde T\tilde{Q}^{\dagger}$, and its physics is fixed by three rules. The **form** is the positive definite Euclidean form of the coefficients, not the Minkowski metric, and the dagger conjugates the scalar coefficient and conjugates-and-negates the vector ones, so $ie_{3}$ is Hermitian and $e_{3}$ anti-Hermitian. The **parameter rules** make the operator blind to the central phase and to the sign, $\Theta_{\omega\tilde{Q}}=\Theta_{-\tilde{Q}}=\Theta_{\tilde{Q}}$, and quadratic in the amplitude, $\Theta_{\lambda\tilde{Q}}=\lvert\lambda\rvert^{2}\Theta_{\tilde{Q}}$, which is the density-matrix structure of the image of the identity. The **adjoint** is $(\Theta_{\tilde{Q}})^{*}=\Theta_{\tilde{Q}^{\dagger}}$, so the self-adjoint operators are exactly those whose parameters are sector elements, which makes the informational and the material sectors carry **one and the same family of observables**; and no nonzero two-sided operator is skew, which is why the generators of the internal group are one-sided. The **automorphisms** are exactly the slice $U=U(2)$, so the rotations are symmetries and the boosts are observables, the two families disjoint: the Lorentz action is not an automorphism of the algebra but the similarity of the norm. The **image of the identity** is the cone $\{\tilde{Q}\tilde{Q}^{\dagger}\}$ of the positive semidefinite Hermitian elements, which is the state space of the internal theory — the Bloch ball on the trace-one slice — and which collapses to a rank-one corner exactly for a null parameter, that is on the cone where the polar representation also fails. Finally **congruence** and **unitary equivalence** are the change of internal basis and the change of internal frame by a symmetry, of invariants the inertia and the spectrum.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | The biquaternion algebra; basis $e_{0},e_{1},e_{2},e_{3}$ |
| ${}^{\dagger}$ | Hermitian conjugation; $Q_{0}^{*}e_{0}-Q_{1}^{*}e_{1}-Q_{2}^{*}e_{2}-Q_{3}^{*}e_{3}$ |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | Informational sector (real scalar, imaginary vector) and material sector (imaginary scalar, real vector) |
| $(\tilde R,\tilde T)=\mathrm{Sc}(\tilde R^{\dagger}\tilde T)$ | The positive definite internal form; not the spacetime metric |
| $N(\tilde{Q})=\sum_{\mu}Q_{\mu}^{2}$ | The quaternion norm; carries the interval on $\mathbb{M}_-$ |
| $\Theta_{\tilde{Q}}(\tilde T)=\tilde{Q}\tilde T\tilde{Q}^{\dagger}$ | The dagger sandwich; the two-sided operator |
| $\Theta_{\lambda\tilde{Q}}=\lvert\lambda\rvert^{2}\Theta_{\tilde{Q}}$, $\Theta_{i\tilde{Q}}=\Theta_{-\tilde{Q}}=\Theta_{\tilde{Q}}$ | Phase and sign invisibility; quadratic amplitude |
| $(\Theta_{\tilde{Q}})^{*}=\Theta_{\tilde{Q}^{\dagger}}$ | The adjoint; $\Theta_{\tilde{Q}}$ self-adjoint iff $\tilde{Q}\in\mathbb{M}_+\cup\mathbb{M}_-$ up to phase |
| $U=U(2)$ | The unitary slice; $\Theta_{\tilde{Q}}$ automorphism iff $\tilde{Q}\in U$ |
| $\lvert N(\tilde{Q})\rvert=1$ | The unit-norm slice $SL(2,\mathbb{C})$ up to phase; the Lorentz action, not an automorphism |
| $\{\tilde{Q}\tilde{Q}^{\dagger}\}$ | The cone of positive semidefinite Hermitian elements; the states |
| $\Theta_{\tilde{Q}}(e_{0})=\tilde{Q}\tilde{Q}^{\dagger}=MM^{\dagger}$ | The image of the identity; the Gram matrix |

## Further Reading

- *Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/two-sided-operators-on-the-biquaternion-algebra-with-hermitian-adjoint.md`), the mathematical companion, for the proofs of the composition law, the adjoint theorem and the type theorems.
- *One-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint* (`articles_physics/one-sided-operators-on-the-biquaternion-algebra-with-hermitian-adjoint.md`), the companion of this article on the other side.
- *Biquaternion Algebra* (`articles_physics/biquaternion-algebra.md`), for the algebra, the four conjugations, the sectors and the Hermitian form.
- *Biquaternion Norm and Invertibility* (`articles_physics/biquaternion-norm-and-invertibility.md`), for the norm, the interval and the group of units.
- *Biquaternion Rotations and Lorentz Transformations* (`articles_physics/biquaternion-rotations-and-lorentz-transformations.md`), for the sandwich as the Lorentz transformation and the reading of the rotor and of the boost.
- *The Sandwich Action in Subspaces* (`articles_physics/the-sandwich-action-in-subspaces.md`), for the same operator restricted to the six distinguished subspaces.
- *Biquaternion Versors and the Orthogonal Group* (`articles_physics/biquaternion-versors-and-the-orthogonal-group.md`), for the contrast between $U(2)$ and $SL(2,\mathbb{C})$, the automorphisms and the similarities.
- *The Bloch Ball as the Trace-One Slice of the Future Light Cone* (`articles_physics/the-bloch-ball-as-the-trace-one-slice-of-the-future-light-cone.md`), for the state space as the trace-one slice of the cone $\{\tilde{Q}\tilde{Q}^{\dagger}\}$.
- *Quantum Channels and the Reversible–Irreversible Dichotomy* (`articles_physics/quantum-channels-and-the-reversible-irreversible-dichotomy.md`), for the two-sided operators as the positive maps and the channels of the framework.
- *The 2×2 Matrix Element Representation of Biquaternions* (`articles_physics/the-2x2-matrix-element-representation-of-biquaternions.md`), for the congruence $\tilde{Q}\mapsto M\tilde{Q} M^{\dagger}$ and the Gram matrix.
- *Unitary Equivalence and Congruence of Operators with Hermitian Adjoint* (`articles_maths/unitary-equivalence-and-congruence-of-operators-with-hermitian-adjoint.md`), for the two equivalence relations of the last section.
