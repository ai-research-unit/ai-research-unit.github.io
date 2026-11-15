# __Rotors Acting on the Bivector Space: the Adjoint Action at $n=4$__

## Introduction

**A rotation of four-space acts on the six-dimensional space $\Lambda^{2}\mathbb{C}^{4}$, which splits into the self-dual and anti-self-dual three-spaces, and the two factors of $\mathrm{Spin}(4)=SU(2)\times SU(2)$ act on the two three-spaces separately; on the self-dual space the eigenvalues are $1$ and $e^{\pm2i\theta_+}$ and on the anti-self-dual space $1$ and $e^{\pm2i\theta_-}$, so each three-space carries one angle doubled.**

The article computes the second exterior power of a rotation, proves that the Hodge star splits the bivector space and that a rotation preserves the two halves, identifies the action on each half with the adjoint action of one summand of $\mathfrak{so}(4)$, computes the eigenvalues and the Casimir, and writes the six generators as the three left and the three right matrices of the axis-free frame.

It assumes *The Spectral Theorem: the Skew-Hermitian Case and the Reality of the Spectrum at $n=4$* and *The Rotor as a Square Root of a Rotation: the Two Signs and the Double Cover at $n=4$*. The model at order two is *Rotors Acting on the Bivector Space at $n=2$: the Adjoint Action*; the operator version is *The Two-Sided Operators and the Segre Cone at $n=4$*.

## The Second Exterior Power

**Definition.** For $Q\in SO(4,\mathbb{C})$ the second exterior power $\Lambda^{2}Q$ acts on $\Lambda^{2}\mathbb{C}^{4}$ by $u\wedge v\mapsto Qu\wedge Qv$.

**Proposition.** $\Lambda^{2}Q$ is linear, invertible with inverse $\Lambda^{2}(Q^{-1})$, and the assignment is a homomorphism: $\Lambda^{2}(QQ')=\Lambda^{2}Q\,\Lambda^{2}Q'$.

**Proof.** Bilinearity and the alternating property give the induced map, and the functoriality is the identity $Q Q'u\wedge QQ'v$.

**Corollary.** The six-dimensional space $\Lambda^{2}\mathbb{C}^{4}$ carries a representation of $SO(4,\mathbb{C})$, and through the covering also a representation of $\mathrm{Spin}(4)$.

**Proof.** The homomorphism property, and the covering map composes with it.

**The trace.** $\operatorname{tr}\Lambda^{2}Q=(\operatorname{tr}Q)^{2}-\operatorname{tr}(Q^{2})$, divided by two for the alternating convention.

**Proof.** On the basis $e_i\wedge e_j$ with $i<j$ the diagonal entry is $\det$ of the $2\times2$ minor, and the sum of the principal $2\times2$ minors is the second elementary symmetric function of the eigenvalues.

**Corollary.** For a rotation the eigenvalues of $\Lambda^{2}Q$ are the pairwise products of the eigenvalues of $Q$.

**Proof.** Triangularise $Q$ and read the diagonal in the corresponding bivector basis.

## The Two Three-Spaces

**Definition.** The **Hodge star** is the map $\ast:\Lambda^{2}\mathbb{C}^{4}\to\Lambda^{2}\mathbb{C}^{4}$ sending $e_i\wedge e_j$ to $\pm e_k\wedge e_l$ with the complement in cyclic order; it satisfies $\ast^{2}=\mathrm I$.

**Proof.** The complement of a pair in four indices is a pair, and complementing twice returns the original sign.

**Definition.** $\Lambda^{2}_{+}$ and $\Lambda^{2}_{-}$ are the eigenspaces of $\ast$ for the eigenvalues $+1$ and $-1$, the **self-dual** and **anti-self-dual** spaces, each of dimension $3$.

**Proof.** The eigenvalues are $\pm1$ and the two eigenspaces have equal dimension, the sum being six.

**Theorem.** For $Q\in SO(4,\mathbb{C})$ the operator $\Lambda^{2}Q$ commutes with the Hodge star, so it preserves both three-spaces.

**Proof.** The Hodge star is natural under an orientation-preserving isometry: $\ast(\Lambda^{2}Q\,\omega)=\Lambda^{2}Q(\ast\omega)$ for $\det Q=1$.

**Corollary.** The representation of $SO(4,\mathbb{C})$ on $\Lambda^{2}$ is the direct sum of two three-dimensional representations, and the covering group acts through the same two.

**Proof.** Invariance of the two summands, and the sum is the whole.

**The concrete basis.** With $J_1=e_1\wedge e_2+e_3\wedge e_4$, $J_2=e_1\wedge e_3+e_4\wedge e_2$, $J_3=e_1\wedge e_4+e_2\wedge e_3$ the three are self-dual, and the three with the signs changed on the second term are anti-self-dual.

**Proof.** $\ast(e_1\wedge e_2)=e_3\wedge e_4$, $\ast(e_1\wedge e_3)=e_4\wedge e_2$, $\ast(e_1\wedge e_4)=e_2\wedge e_3$.

## The Action of the Two Factors

**Theorem.** The self-dual three-space carries the adjoint representation of the first summand of $\mathfrak{so}(4)$ and the trivial action of the second, and the anti-self-dual three-space the reverse.

**Proof.** The summands act on $\Lambda^{2}$ by the commutator, which is the derivative of the conjugation action; the self-dual part of $\mathfrak{so}(4)$ fixes $\Lambda^{2}_{+}$ pointwise as a bivector identity and acts on it by its own adjoint action, and it annihilates $\Lambda^{2}_{-}$; the anti-self-dual part does the reverse.

**Corollary.** A rotor which is a single left quaternion acts on $\Lambda^{2}_{+}$ as an element of $SO(3)$ and on $\Lambda^{2}_{-}$ as the identity; a single right quaternion does the reverse.

**Proof.** The left quaternion generates the self-dual summand, and the exponential of a self-dual element acts trivially on the anti-self-dual space.

**Corollary.** The two actions commute, and the representation of $\mathrm{Spin}(4)$ on $\Lambda^{2}$ is the sum of the two adjoint representations.

**Proof.** The two summands commute and each acts trivially on the other's space.

**The isoclinic reading.** A rotation acts trivially on one of the two three-spaces exactly when it is isoclinic in the corresponding family.

**Proof.** Triviality on $\Lambda^{2}_{-}$ means $\theta_-=0$, that is $\theta_1=\theta_2$, and the other case likewise.

## The Eigenvalues and the Two Angles

**Theorem.** For $Q$ with angles $\theta_1,\theta_2$ the eigenvalues of $\Lambda^{2}Q$ are
$$
1,\ 1,\ e^{\pm2i\theta_+},\ e^{\pm2i\theta_-},
\qquad \theta_\pm=\tfrac{\theta_1\pm\theta_2}{2},
$$
and on $\Lambda^{2}_{+}$ they are $1,e^{\pm2i\theta_+}$ while on $\Lambda^{2}_{-}$ they are $1,e^{\pm2i\theta_-}$.

**Proof.** The eigenvalues of $Q$ are $e^{\pm i\theta_1},e^{\pm i\theta_2}$; the pairwise products are $1=e^{i\theta_1}e^{-i\theta_1}$, $1=e^{i\theta_2}e^{-i\theta_2}$, $e^{i(\theta_1+\theta_2)}=e^{2i\theta_+}$ and $e^{i(\theta_1-\theta_2)}=e^{2i\theta_-}$ with their inverses. The self-dual and the anti-self-dual space separate the two nontrivial pairs: on $\Lambda^{2}_{+}$ the operator is a rotation of the three-space with angle $2\theta_+$, and on $\Lambda^{2}_{-}$ one with angle $2\theta_-$.

**Corollary.** The angle on each three-space is twice the angle of the corresponding one-sided quaternion, and the isoclinic rotations are those with two eigenvalues equal to one on one of the spaces.

**Proof.** The factor two is the factor of the pairwise product, and the rest is the previous corollary.

**Corollary.** $\operatorname{tr}\Lambda^{2}Q=2+2\cos2\theta_++2\cos2\theta_-=2+4\cos\theta_1\cos\theta_2$, which at $\theta_1=\theta_2=\theta$ is $4+2\cos2\theta$.

**Proof.** Sum the eigenvalues and use $2\cos2\theta_++2\cos2\theta_-=4\cos\theta_1\cos\theta_2$.

**The determinant.** $\det\Lambda^{2}Q=1$, so the second exterior power map lands in $SL(\Lambda^{2})$.

**Proof.** The eigenvalues multiply to $1$ in each three-space, since $e^{2i\theta}e^{-2i\theta}=1$.

## The Casimir and the Killing Form

**Proposition.** On each three-space the Casimir of the corresponding summand is a scalar, and with the trace form as the invariant pairing the scalar is one on the adjoint three-space and $3/8$ on the defining two-space.

**Proof.** The Casimir is invariant, so it acts as a scalar on an irreducible representation; the adjoint computation is $\operatorname{ad}(J_1)^{2}+\operatorname{ad}(J_2)^{2}+\operatorname{ad}(J_3)^{2}=-2\mathrm I$ with the normalisation of the trace form, giving $-\tfrac12(-2\mathrm I)=\mathrm I$; the defining computation is $\sum_k(i\sigma_k/2)^{2}=-\tfrac34\mathrm I$, giving $3\mathrm I/8$.

**Corollary.** The two Casimirs of the two summands commute and are diagonal in the bivector basis, so the bivector space carries two commuting angular momenta.

**Proof.** The scalar Casimirs of the two summands, each acting trivially on the other's space.

**Corollary.** The Killing form of $\mathfrak{so}(4)$ is the sum of the two Killing forms, and on each three-space it is negative definite.

**Proof.** The two summands are orthogonal ideals, and each is a copy of $\mathfrak{sl}_2$ with negative definite Killing form.

## The Axis-Free Matrices

**Theorem.** In the axis-free frame the three left matrices $L_x,L_y,L_z$ span $\Lambda^{2}_{+}$ and the three right matrices $R_x,R_y,R_z$ span $\Lambda^{2}_{-}$, and each triple obeys the quaternion brackets.

**Proof.** The left multiplications by the three imaginary units rotate two planes in the same sense, hence are self-dual; the right ones rotate them in opposite senses, hence are anti-self-dual; and $[L_x,L_y]=2L_z$ in the normalisation of the frame.

**Corollary.** The six-dimensional bivector space is spanned by the six signed permutations, and the Hodge star is the identity on the left triple and minus the identity on the right triple.

**Proof.** The two triples and the definition of the star.

**Corollary.** An element $\theta_1L_i+\theta_2R_i$ acts on $\Lambda^{2}_{+}$ with angle $2\theta_1$ and on $\Lambda^{2}_{-}$ with angle $2\theta_2$, so the two angles of the rotation are read directly from the two triples.

**Proof.** The two triples are the two summands, and the theorem above.

**The finite shadow.** The group of the sixteen $T_{\mu\nu}$ acts on $\Lambda^{2}$ through the two copies of $Q_8$, and the two actions are the two finite shadows of the two factors.

**Proof.** $T_{\mu\nu}=L_\mu R_\nu$ acts as the product of the two one-sided actions, each of which is a signed permutation of the corresponding triple.

## Summary

A rotation acts on the six-dimensional bivector space by its second exterior power, which commutes with the Hodge star and therefore preserves the self-dual and the anti-self-dual three-spaces. Each three-space carries the adjoint action of one summand of $\mathfrak{so}(4)=\mathfrak{sl}_2\oplus\mathfrak{sl}_2$ and the trivial action of the other.

The eigenvalues are $1$ and $e^{\pm2i\theta_+}$ on the self-dual space and $1$ and $e^{\pm2i\theta_-}$ on the anti-self-dual one, with $\theta_\pm=(\theta_1\pm\theta_2)/2$; the angles are doubled by passing to bivectors, and a rotation acts trivially on one three-space exactly when it is isoclinic in the corresponding family.

The Casimir of each summand is a scalar on its three-space, one in the adjoint normalization; the Killing form restricts to a negative definite form on each. In the axis-free frame the left triple spans the self-dual space and the right triple the anti-self-dual one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Lambda^{2}\mathbb{C}^{4}$ | the six-dimensional bivector space |
| $\Lambda^{2}_{\pm}$ | the self-dual and anti-self-dual three-spaces |
| $\ast$ | the Hodge star |
| $\theta_\pm=(\theta_1\pm\theta_2)/2$ | the two half-angles |
| $L_k,R_k$ | the two triples in the axis-free frame |
| $J_1,J_2,J_3$ | the self-dual bivector basis |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for bivectors, the Hodge star and the self-dual split.
- [The Rotor as a Square Root of a Rotation: the Two Signs and the Double Cover at $n=4$](the-rotor-as-a-square-root-of-a-rotation-the-two-signs-and-the-double-cover-at-n-4.html), for the covering and the rotor.
- [Simple and Non-Simple Rotations: One Angle at $n\le3$, Two Angles at $n\ge4$](simple-and-non-simple-rotations-one-angle-at-n-le-3-two-angles-at-n-ge-4.html), for the two angles and the isoclinic families.
- [The Lie Algebra $\operatorname{Skew}_4\cong\mathfrak{so}(4)$](the-lie-algebra-skew-4-and-so-4.html), for the identification with the bivectors.
- [Rotors Acting on the Bivector Space at $n=2$: the Adjoint Action](rotors-acting-on-the-bivector-space-at-n-2-the-adjoint-action.html), for the case at order two.
