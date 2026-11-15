# __Simple and Non-Simple Rotations at $n=4$: the Two Angles and the Isoclinic Families__

## Introduction

**At order four a rotation has two invariant planes and two angles, the normal form $\operatorname{diag}(R_{\theta_1},R_{\theta_2})$, and the generic rotation is not simple; the isoclinic cases $\theta_1=\pm\theta_2$ are the two families, each a three-sphere of rotations, and the circle of one family is the Hopf action of $S^{1}$ on $S^{3}$.**

The article defines simplicity, proves that a simple rotation of four-space fixes a plane and has one angle, classifies the rotations into the three cases of distinct angles, equal angles and opposite angles, gives the count $\lfloor n/2\rfloor$, identifies the two angles with the two summands of $\mathfrak{so}(4)$, and relates the isoclinic families to the Hopf fibration.

It assumes *The Spectral Theorem: the Anti-Hermitian Case and the Reality of the Spectrum at $n=4$*, *The Lie Algebra $\operatorname{Skew}_4\cong\mathfrak{so}(4)$* and *The Rotor as a Square Root of a Rotation: the Two Signs and the Double Cover at $n=4$*. The general order is *Simple and Non-Simple Rotations: One Angle at $n\le3$, Two Angles at $n\ge4$*.

## Simple Rotations and the Fixed Subspace

**Definition.** A rotation is **simple** when it turns a single plane and fixes its orthogonal complement pointwise.

**Proposition.** A simple rotation of four-space has the eigenvalue $1$ with multiplicity at least two, and its fixed subspace is a plane.

**Proof.** The fixed complement of the rotating plane is two-dimensional and consists of eigenvectors with eigenvalue one; the rotating plane contributes the eigenvalues $e^{\pm i\theta}$.

**Corollary.** A simple rotation is $\operatorname{diag}(R_\theta,\mathrm I_2)$ in a suitable orthonormal frame, and the rank of $Q-\mathrm I_4$ is two.

**Proof.** The normal form of the two blocks, and the kernel of $Q-\mathrm I_4$ is the fixed plane.

**Proposition.** A rotation of four-space is simple exactly when the eigenvalue one has multiplicity at least two, that is when the geometric multiplicity of one exceeds one.

**Proof.** The multiplicity of the eigenvalue one is the dimension of the fixed space, which for a simple rotation is two; conversely two independent fixed vectors span a fixed plane whose complement is turned by a single angle.

**Corollary.** The simple rotations form a family of dimension five, of codimension one in the six-dimensional group: the choice of the plane costs four parameters and the angle one.

**Proof.** The normal form and the dimension count: a plane in four-space is a point of the Grassmannian of dimension four, and the angle adds one.

**The axis at order three.** At order three a rotation always has a fixed line, so every rotation is simple; at order four the fixed space can be a line or a point, and the generic rotation fixes only the origin.

**Proof.** An odd-dimensional real operator has a real eigenvalue, which for an orthogonal one is $\pm1$ and hence a fixed line after possibly reversing the sign.

## The Two Angles at Order Four

**Theorem.** Every rotation of four-space is orthogonally conjugate to $\operatorname{diag}(R_{\theta_1},R_{\theta_2})$ with $\theta_1\ge\theta_2\ge0$, up to signs and ordering.

**Proof.** The real normal form of the skew generator, exponentiated: the pair of invariant planes of the skew part is invariant under the rotation it generates.

**Corollary.** The spectrum is $\{e^{i\theta_1},e^{-i\theta_1},e^{i\theta_2},e^{-i\theta_2}\}$, and the two angles are read from it up to sign.

**Proof.** The eigenvalues of the two blocks.

**Corollary.** $\operatorname{tr}Q=2\cos\theta_1+2\cos\theta_2$ and $\det Q=1$, so the trace is the sum of the two cosines and the determinant carries no information.

**Proof.** Sum and product of the eigenvalues.

**The angle formula.** For a simple rotation $\operatorname{tr}Q=2+2\cos\theta$, which recovers the angle from the trace; at order four the single trace determines the sum of the two cosines and not the two angles separately.

**Proof.** The two formulas.

**Corollary.** The map from the rotation to its trace is not injective at order four, and it cannot be, since the group has dimension six and the trace takes values in a two-dimensional real set.

**Proof.** The trace is a continuous function of two parameters into a bounded interval on a six-dimensional group.

## The Three Cases

**Theorem.** A rotation of four-space falls in exactly one of four cases:

| case | condition | fixed space | simple |
|---|---|---|---|
| simple | $\theta_1\neq0$, $\theta_2=0$ | a plane | yes |
| isoclinic, left | $\theta_1=\theta_2\neq0$ | a point | no |
| isoclinic, right | $\theta_1=-\theta_2\neq0$ | a point | no |
| general | $|\theta_1|\neq|\theta_2|$, both nonzero | a point | no |

**Proof.** A block $R_\theta$ of a nonzero angle contributes no fixed vector, so the fixed space is spanned by the blocks with $\theta=0$: it is a plane when exactly one angle vanishes and the origin otherwise. A rotation is simple exactly when it is a single block together with an untouched plane.

**Corollary.** The isoclinic rotations split into two families, $\theta_1=\theta_2$ and $\theta_1=-\theta_2$, and the two families are the left and the right one-sided quaternion actions; both families fix only the origin.

**Proof.** The left action turns both planes in the same sense and the right action in opposite senses; in either case both planes move.

**Corollary.** A non-isoclinic rotation has no fixed vector and no invariant vector at all, since an invariant vector would be an eigenvector with a real eigenvalue.

**Proof.** The eigenvalues are not real for a nonzero angle.

**The generic case.** The generic rotation is non-isoclinic with two distinct nonzero angles, so the generic rotation is not simple.

**Proof.** The conditions $\theta_1=\pm\theta_2$ and $\theta_k=0$ are of codimension one or more in the two parameters.

## The Count and the Normal Form

**Proposition.** The number of independent angles is $\lfloor n/2\rfloor$, which is $1$ at $n=2,3$ and $2$ at $n=4,5$.

**Proof.** The maximal torus of $SO(n)$ has dimension $\lfloor n/2\rfloor$, one circle per invariant plane.

**Corollary.** At order four the rotation group has dimension six and rank two, and the two angles are the coordinates on a maximal torus.

**Proof.** $\dim SO(4)=6$, the rank is two, and the remaining four dimensions are the choice of the two planes.

**Corollary.** The normal form is $\operatorname{diag}(R_{\theta_1},R_{\theta_2})$, and the two planes of the normal form are the eigenplanes of the skew generator.

**Proof.** The normal form of the skew matrix, exponentiated.

**The order five.** At order five a third angle exists but the extra dimension is a fixed line, so the count is still two; the first order with three angles is six.

**Proof.** $\lfloor5/2\rfloor=2$ and $\lfloor6/2\rfloor=3$.

## The Two Angles as the Two Parameters

**Proposition.** The two angles are the parameters of the two summands of $\mathfrak{so}(4)=\mathfrak{sl}_2\oplus\mathfrak{sl}_2$: the self-dual part has size $\theta_1$ and the anti-self-dual part size $\theta_2$.

**Proof.** $\tfrac12(A+\ast A)=\theta_1J_1$ and $\tfrac12(A-\ast A)=\theta_2J_2$ in the normal form, and the two summands are the two eigenspaces of the star.

**Corollary.** The simple rotations are those with one summand vanishing, and the isoclinic rotations are those whose two summands have equal size.

**Proof.** A vanishing self-dual part means $\theta_1=0$, which is a rotation in one plane only, and equal sizes means $|\theta_1|=|\theta_2|$.

**Corollary.** The two angles are independent coordinates, and the rotation group is the product of the two circle groups of the summands modulo the diagonal sign.

**Proof.** Each summand contributes one circle, and the pair of signs $(-1,-1)$ acts trivially.

**The biquaternion form.** A rotation is $L_pR_q$ with $p,q$ unit quaternions, and the two angles are the arguments of $p$ and of $q$.

**Proof.** $p=e^{\theta_1 i}$ turns both planes by $\theta_1$ and $q=e^{\theta_2 i}$ turns them by $\theta_2$ with opposite senses, so the product has the two angles.

## The Isoclinic Rotations and the Hopf Fibrations

**Theorem.** The left-isoclinic rotations form a copy of $S^{3}$ inside $SO(4)$, and so do the right-isoclinic ones; their intersection is $\pm\mathrm I_4$.

**Proof.** The left unit quaternions form a three-sphere of rotations, the right ones another, and a rotation that is both is $\pm\mathrm I_4$ because its two angles satisfy $\theta_1=\theta_2$ and $\theta_1=-\theta_2$.

**Corollary.** The two three-spheres generate $SO(4)$ and intersect in two points, which is the double cover $\mathrm{Spin}(4)\to SO(4)$ read on the two factors.

**Proof.** Every rotation is a product of one from each, and the intersection is the kernel.

**The Hopf reading.** The circle $\{e^{i\theta}\}\subset S^{3}$ of left-isoclinic rotations through a plane acts on the unit sphere $S^{3}\subset\mathbb{C}^{2}$ as the Hopf action, whose orbits are the fibres of $S^{3}\to S^{2}$.

**Proof.** Writing $\mathbb{R}^{4}=\mathbb{C}^{2}$, the left multiplication by $e^{i\theta}$ is the scalar multiplication by the phase, and the orbit map of the unit sphere is the Hopf fibration.

**Corollary.** The isoclinic circle is the structure group of the Hopf bundle at order four, and the full three-sphere of left-isoclinic rotations is the total space of the same fibration.

**Proof.** The action of $S^{3}$ on its own unit sphere by left multiplication is free and transitive, and the circle inside it gives the fibres.

**The next level.** The same construction with $\mathbb{H}^{2}$ in place of $\mathbb{C}^{2}$, that is at order eight, gives the quaternionic Hopf fibration $S^{7}\to S^{4}$, whose structure group is the three-sphere of unit quaternions.

**Proof.** Left multiplication by unit quaternions on $\mathbb{H}^{2}=\mathbb{R}^{8}$ preserves the norm and acts freely on the unit sphere, with quotient the quaternionic projective line $S^{4}$.

**Corollary.** The isoclinic phenomenon is the geometric content of the Hopf fibrations, and at order four it is the complex one.

**Proof.** The two statements above.

## Summary

A rotation of four-space has two invariant planes and two angles, with the normal form $\operatorname{diag}(R_{\theta_1},R_{\theta_2})$; it is simple exactly when one angle is zero or the two are opposite, so the fixed space is a plane in those cases and a point otherwise. The generic rotation is non-isoclinic and not simple.

The number of angles is $\lfloor n/2\rfloor$, one at orders two and three and two from order four on. The two angles are the parameters of the two summands of $\mathfrak{so}(4)$, and the isoclinic families are the rotations with one summand vanishing.

The left-isoclinic and right-isoclinic rotations are two three-spheres meeting in two points, and their product is the whole group; the circle inside one of them is the Hopf action of $S^{1}$ on $S^{3}$, and the same construction at order eight gives the quaternionic Hopf fibration.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R_\theta$ | the rotation block of angle $\theta$ |
| $\theta_1,\theta_2$ | the two angles |
| $\lfloor n/2\rfloor$ | the number of angles |
| isoclinic | $\theta_1=\pm\theta_2$ |
| $S^{3}\to S^{2}$ | the Hopf fibration of the isoclinic circle |

## Further Reading

- Morton L. Curtis, *Matrix Groups* (Springer, 1984), for the normal form of a rotation and the two angles.
- [Simple and Non-Simple Rotations: One Angle at $n\le3$, Two Angles at $n\ge4$](simple-and-non-simple-rotations-one-angle-at-n-le-3-two-angles-at-n-ge-4.html), for the statement at general order.
- [The Spectral Theorem: the Anti-Hermitian Case and the Reality of the Spectrum at $n=4$](the-spectral-theorem-the-anti-hermitian-case-at-n-4.html), for the eigenvalues and the Pfaffian.
- [The Lie Algebra $\operatorname{Skew}_4\cong\mathfrak{so}(4)$](the-lie-algebra-skew-4-and-so-4.html), for the two summands.
- [Simple Rotations at $n=2$: Why There Is Only One Angle](simple-rotations-at-n-2-why-there-is-only-one-angle.html), for the case at order two.
