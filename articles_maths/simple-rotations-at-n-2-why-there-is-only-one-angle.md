# __Simple Rotations at $n=2$: Why There Is Only One Angle__

## Introduction

**At order two the antisymmetric matrices form a single line, so a rotation has one plane and one angle, every rotation is simple, and the rotation group is a circle parametrised by that angle modulo $2\pi$.**

The article explains what a simple rotation is, shows that the antisymmetric line is the only plane available at order two, proves that a rotation is determined by a single angle, computes the angle from the trace, compares the situation with the two angles of a rotation in four dimensions, and reads the single angle inside the complex and Hermitian pictures. It assumes *The Exponential of $\operatorname{Skew}_2$: the Single Rotation Plane*, *The Lie Algebra $\operatorname{Skew}_2$: One Dimension, Hence Abelian* and *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric at $n=2$*.

It follows the biquaternion account of *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra* for the norm that the single angle leaves fixed.

## Simple Rotations

**Definition.** A **simple rotation** of a real vector space with an inner product is a rotation that fixes pointwise the orthogonal complement of a single plane.

**Proposition.** Every rotation at order two is simple, with the whole plane as its plane of rotation.

**Proof.** The space has dimension two, so the orthogonal complement of the whole plane is zero and the condition is vacuous.

**Corollary.** At order two there is no room for a rotation to mix two independent planes.

**Proof.** A second independent plane would need two more dimensions, and the space has only two.

**Corollary.** In four dimensions the general rotation is not simple: it is the composition of two rotations in two orthogonal planes with two independent angles.

**Proof.** The Lie algebra $\mathfrak{so}(4)$ has dimension six and splits as the sum of two three-dimensional ideals, each contributing one angle, so a general element has two angles; such an element is simple only when one of the two angles vanishes.

## The Single Plane

**Theorem.** The antisymmetric matrices at order two form the line $\mathbb{R}J$, and the exponential of that line is the whole rotation group.

**Proof.** A real antisymmetric matrix is $tJ$ with $t$ real, by *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric at $n=2$*; and its exponential runs over all the rotations by *The Exponential of $\operatorname{Skew}_2$: the Single Rotation Plane*.

**Corollary.** The rotation group at order two has dimension one, and its Lie algebra is the antisymmetric line.

**Proof.** The exponential of a line is at most one-dimensional, and it is onto the rotation group, which is therefore one-dimensional.

**Corollary.** A rotation at order two is determined by a single real parameter, which is its angle.

**Proof.** The group is a circle and every point of it is reached by one angle modulo $2\pi$.

## Why There Is Only One Angle

**The absence of a second angle is a dimension count, and it can be seen in three ways.**

**Proposition.** The tangent space of the rotation group at the identity is one-dimensional, so the group has one infinitesimal generator and one angle.

**Proof.** The tangent space is the antisymmetric line, which is one-dimensional.

**Corollary.** The trace of a rotation determines the cosine of the angle, and the off-diagonal entry determines its sine, so the two together fix the angle modulo $2\pi$.

**Proof.** The rotation is $(\cos t)I+(\sin t)J$, so the trace is $2\cos t$ and the upper right entry is $\sin t$.

**Corollary.** A rotation at order two commutes with every other rotation, so the group is abelian and every element lies in a one-parameter subgroup.

**Proof.** All the rotations are polynomials in the single matrix $J$, and polynomials in one matrix commute.

## The Angle from the Trace

**Proposition.** For a rotation $R$ the angle satisfies $\operatorname{tr}R=2\cos t$ and $\det R=1$, so the angle is determined up to sign by the trace alone.

**Proof.** The Euler formula gives the trace as twice the cosine and the determinant as one.

**Corollary.** The map from rotations to traces is two-to-one except at the two rotations $\pm I$, where the angle is $0$ or $\pi$.

**Proof.** The cosine takes the same value at $t$ and $-t$, and at the two endpoints of the interval the two angles coincide.

**Corollary.** The trace is a function of the angle alone, and it is injective on the rotations whose angle lies in the interval $[0,\pi)$.

**Proof.** The trace is $2\cos t$, which is strictly decreasing on that interval.

## The Complex Reading

**Proposition.** Over $\mathbb{C}$ the antisymmetric line is a complex line, and a rotation is $e^{tJ}$ with $t$ complex, so the single angle becomes a single complex parameter.

**Proof.** The complex antisymmetric matrices are $tJ$ with $t\in\mathbb{C}$, and the exponential is computed by the same Euler formula.

**Corollary.** The complex rotation group is the quadric $X^{\mathsf T}X=I$ with determinant one, which is a cylinder parametrised by one complex number modulo $2\pi$.

**Proof.** The parametrisation by $t$ has the period lattice $2\pi\mathbb{Z}$, so the group is the quotient of the complex line by that lattice.

**Corollary.** There is still only one complex angle, because the complex antisymmetric space has complex dimension one and real dimension two.

**Proof.** The real dimension of the complex line is two, and it is the whole Lie algebra of the complex rotation group.

## The Hidden Second Parameter

**The single angle does not mean that the rotation group is trivial: the group has a second real direction coming from the scalar phase.**

**Proposition.** The rotation circle sits inside the unitary group as the subgroup generated by $J$, and the unitary group has real dimension four, so three further real directions surround it.

**Proof.** The unitary group at order two has real dimension four; the circle generated by $J$ is one-dimensional; the scalar phases form a second circle commuting with it; and the two remaining directions are the other two traceless skew-Hermitian directions, which complete the three-dimensional space $\mathfrak{su}(2)$ together with $J$.

**Corollary.** The single rotation plane of the real picture is one circle inside the four-dimensional unitary group.

**Proof.** The rotations sit inside the unitaries as the matrices of the form $e^{tJ}$, and these form a circle.

**Corollary.** At order two the count of angles is one for the rotations of the plane and one for the phase, and the two circles commute.

**Proof.** The scalar phases commute with the rotations, so the two circles generate a torus inside the unitary group.

## Summary

A simple rotation fixes the orthogonal complement of one plane, and at order two every rotation is simple because the whole plane is the only plane. The antisymmetric matrices form the single line $\mathbb{R}J$, its exponential is the whole rotation group, and the group is a circle parametrised by one angle modulo $2\pi$.

The angle is read from the trace as $2\cos t$ and from the off-diagonal entry as $\sin t$, and the absence of a second angle is the one-dimensionality of the antisymmetric line. Over $\mathbb{C}$ the single real angle becomes a single complex parameter, and the four-dimensional unitary group contains the rotation circle as one factor of a torus.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $J$ | the generator of the antisymmetric line |
| $t$ | the single angle |
| $\mathrm{SO}(2)$ | the rotation group at order two |
| $\mathfrak{so}(2)$ | the antisymmetric line as a Lie algebra |
| $\mathrm{SO}(4)$ | the comparison case with two angles |

## Further Reading

- Morton L. Curtis, *Matrix Groups* (Springer, 1984), for rotation groups and their angles in low dimensions.
- Jean Dieudonné, *La géométrie des groupes classiques* (Springer, 1971), for simple rotations and their planes.
- [The Exponential of $\operatorname{Skew}_2$: the Single Rotation Plane](the-exponential-of-skew-2-the-single-rotation-plane.html), for the Euler formula and the group of rotations.
- [The Lie Algebra $\operatorname{Skew}_2$: One Dimension, Hence Abelian](the-lie-algebra-skew-2-one-dimension-hence-abelian.html), for the one-dimensional Lie algebra.
- [The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric at $n=2$](the-two-halves-over-r-symmetric-and-antisymmetric-at-n-2.html), for the antisymmetric line as a half.
