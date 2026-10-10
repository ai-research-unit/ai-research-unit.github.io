
# __The Isotropic Structure of the General Quaternionic Algebra__

## Introduction

The general quaternionic bilinear form

$$
\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde P\tilde Q^{\natural})=\sum_\mu P_\mu Q_\mu
$$

has for its null set the zero-divisor cone of the algebra. This article develops the cone: its two families of maximal totally isotropic planes, the minimal ideals it carries, and its identification with the zero-divisor set of the algebra. The topology of the cone and the realified invariants are not developed here; the pointers are in the last paragraph of this introduction.

The form itself, its polarisation and its quadratic space are *Biquaternion Norm and Invertibility*; the remarkable subspaces and their restriction matrices are *Remarkable Subspaces under the General Quaternionic Algebra of Biquaternions*; the classification of the isotropic elements is *Zero Divisors of the General Plain Algebra*; the projective picture of the cone, the quadric surface, the Klein quadric and the Plücker embedding are *The Null Quadric and Its Projective Geometry*; and the invertibility criterion that makes the cone the boundary of the group of units is *Biquaternion Norm and Invertibility*. The topology of the cone, its dimension, its apex and its link are *The Topology of the Zero-Divisor Cone*; the index, the defect and the signature of the realified form are *The Realification of the Four Forms*, and their values on the remarkable subspaces are *Remarkable Subspaces under the General Quaternionic Algebra of Biquaternions*.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$ and central scalar imaginary $i$; a general element is $\tilde{Q}=\sum_\mu Q_\mu e_\mu$ with $Q_\mu=q_\mu+iq'_\mu$, $q_\mu,q'_\mu\in\mathbb{R}$, so that $\tilde{Q}=\sum_\mu q_\mu e_\mu+\sum_\mu q'_\mu\,ie_\mu$ on the eight real basis elements. The norm is $N(\tilde Q)=\sum_\mu Q_\mu^2=\langle\tilde Q,\tilde Q\rangle_{\natural}$, and $\|\tilde Q\|_E=(\sum_\mu|Q_\mu|^2)^{1/2}$ is the definite norm of the coefficient space.

## The Null Cone

**Definition.** The **null cone** of the general quaternionic bilinear form is

$$
\mathcal N_{\natural}=\{\tilde Q:\langle\tilde Q,\tilde Q\rangle_{\natural}=0\}=\Bigl\{\tilde Q:\sum_\mu Q_\mu^2=0\Bigr\}.
$$

The cone is the zero set of the polynomial $f=\sum_\mu Q_\mu^2$, homogeneous of degree two and invariant under $\tilde Q\mapsto\lambda\tilde Q$ for every $\lambda\in\mathbb{C}$; its dimension and its singular point are *The Topology of the Zero-Divisor Cone*. Nothing of the cone's form beyond its equation is used below.

**Proposition (the cone is the zero-divisor set).** The cone is exactly the zero-divisor set: an element is a unit precisely when its norm is nonzero, so a nonzero null element is a zero divisor, and the algebra is a division algebra off the cone.

*Proof.* The criterion for invertibility is $N(\tilde Q)\neq0$, which is the statement that the diagonal of the form does not vanish. Hence the nonzero null elements are exactly the nonzero non-units, and the classification of the two families of zero divisors is by their purity. Verified: $N(e_1+ie_2)=1+i^{2}=0$ and $N(e_0+ie_1)=1+i^{2}=0$, both zero divisors, while $N(e_0+e_1)=2$.

The projective geometry of the cone is *The Null Quadric and Its Projective Geometry*.

## The Maximal Totally Isotropic Planes

**Definition.** A subspace $W\subset\mathbb{B}$ is **totally isotropic** when the form vanishes on it identically, $\langle\tilde P,\tilde Q\rangle_{\natural}=0$ for all $\tilde P,\tilde Q\in W$; equivalently when $W$ is isotropic and orthogonal to itself.

**Proposition (the maximal totally isotropic planes).** Over $\mathbb{C}$ the maximal totally isotropic dimension is $2$, and the maximal totally isotropic subspaces are the planes of two families. The two planes

$$
W_{+}=\mathbb{C}\{e_0+ie_1,\;e_2+ie_3\},\qquad
W_{-}=\mathbb{C}\{e_0+ie_1,\;e_2-ie_3\}
$$

are totally isotropic, one from each family; through each non-singular point of the cone passes one plane of each family, and two planes of the same family meet only at the origin, while two planes of the two families meet along a line.

*Proof.* On the generators of $W_+$ the form vanishes, $\langle e_0+ie_1,e_0+ie_1\rangle=1+i^{2}=0$, $\langle e_2+ie_3,e_2+ie_3\rangle=1+i^{2}=0$ and $\langle e_0+ie_1,e_2+ie_3\rangle=0$, and the same computation holds for $W_-$; a $\mathbb{C}$-bilinear form vanishing on a generating set vanishes on the span, so both planes are totally isotropic. The two differ in the sign carried by the $e_3$ direction, and that is what puts them in different families: $W_+\cap W_-=\mathbb{C}(e_0+ie_1)$, a line, so the two planes meet rather than being skew, while the planes of a single family, such as $\mathbb{C}\{e_0+ie_1,e_2+ie_3\}$ and its sign-mirror $\mathbb{C}\{e_0-ie_1,e_2-ie_3\}$, intersect only at the origin. The upper bound is the Witt index of the form, which is $2$ over $\mathbb{C}$: the two-dimensional plane $\mathbb{C}\{e_0+ie_2,\;e_1+ie_3\}$ is totally isotropic and of dimension $2$, and no three-dimensional subspace can be isotropic because the form is non-degenerate of rank $4$. Verified: the form vanishes identically on both planes and on the two sign-mirrors, and the intersections are a line across the families and the origin within one family. The two families are those attached to the quadric in *The Null Quadric and Its Projective Geometry*.

**Corollary (the maximal totally isotropic dimension of the realified form).** The realified form of signature $(4,4)$ has maximal totally isotropic real dimension $4$.

*Proof.* The bound is the smaller of the two inertia indices of the signature $(4,4)$, which is $4$, and the realification of one of the complex planes above is a real totally isotropic $4$-space attaining it. The index, the defect and the full signature of the realified form, and their values on the remarkable subspaces, are *The Realification of the Four Forms* and *Remarkable Subspaces under the General Quaternionic Algebra of Biquaternions*.

## The Minimal Ideals and the Hyperbolic Peirce Basis

The null cone of the form is the zero-divisor set of the algebra, and the one-sided ideals it carries are the maximal totally isotropic subspaces.

**Theorem (the minimal ideals are the maximal isotropic one-sided ideals).** Every minimal left ideal and every minimal right ideal of $\mathbb{B}$ is a maximal totally isotropic subspace of the general quaternionic bilinear form. Conversely, a maximal totally isotropic subspace that is a left ideal is a minimal left ideal, and likewise on the right.

*Proof.* Let $\tilde Q\ne0$ be null for the form and let $\tilde X,\tilde Y\in\mathbb{B}$. Then

$$
\langle\tilde X\tilde Q,\tilde Y\tilde Q\rangle_{\natural}=\mathrm{Sc}\!\left(\tilde X\tilde Q\tilde Q^{\natural}\tilde Y^{\natural}\right)=\mathrm{Sc}\!\left(\tilde X\,\langle\tilde Q,\tilde Q\rangle_{\natural}\tilde Y^{\natural}\right)=\langle\tilde Q,\tilde Q\rangle_{\natural}\,\mathrm{Sc}\!\left(\tilde X\tilde Y^{\natural}\right)=0,
$$

so the left ideal $\mathbb{B}\tilde Q$ is totally isotropic; it has complex dimension $2$, and a totally isotropic subspace of the four-dimensional complex algebra has complex dimension at most $2$, since the form is non-degenerate of Witt index $2$. So $\mathbb{B}\tilde Q$ is maximal, and conversely a maximal totally isotropic left ideal is generated by a null element and is minimal. The right-handed statements are the mirror. $\square$

The theorem is not an equality of families: the maximal totally isotropic subspaces form a larger family than the one-sided ideals, and the two families meet in the minimal ideals. In the Peirce basis $\tilde\Pi,\tilde\Upsilon_1,f,\tilde\Upsilon_2$ of *Biquaternion Ideals and Peirce Decomposition*, where $\tilde\Pi=\tfrac12(e_0+ie_1)$, $f=e_0-\tilde\Pi$, $\tilde\Upsilon_1=e_3+ie_2$ and $\tilde\Upsilon_2=e_3-ie_2$, the Gram matrix of the form is

$$
\begin{pmatrix}
0 & 0 & \tfrac{1}{2} & 0 \\
0 & 0 & 0 & 2 \\
\tfrac{1}{2} & 0 & 0 & 0 \\
0 & 2 & 0 & 0
\end{pmatrix},
$$

an antidiagonal matrix: **the form is hyperbolic in the Peirce basis, and the four Peirce lines are paired by it**, the idempotent line $\mathbb{C}\tilde\Pi$ with the idempotent line $\mathbb{C}f$ and the nilpotent line $\mathbb{C}\tilde\Upsilon_1$ with the nilpotent line $\mathbb{C}\tilde\Upsilon_2$. The two minimal left ideals $\mathbb{B}\tilde\Pi=\mathbb{C}\tilde\Pi\oplus\mathbb{C}\tilde\Upsilon_1$ and $\mathbb{B}f=\mathbb{C}f\oplus\mathbb{C}\tilde\Upsilon_2$ are maximal totally isotropic by the theorem, and the span of $\tilde\Pi$ and $\tilde\Upsilon_2$, one line from each, is a maximal totally isotropic subspace that is **not** a left ideal, since it mixes the two.

**Corollary (the isotropic lines of the remarkable subspaces).** Since the null elements of the form are exactly the zero divisors, its isotropic lines inside the remarkable subspaces are their zero-divisor lines, tabulated in *Remarkable Subspaces under the General Quaternionic Algebra of Biquaternions*, §*The Isotropic Lines of the Indefinite Restrictions*; no isotropic subspace beyond a line lies inside a single one of the remarkable subspaces, since each restriction is non-degenerate.

## Worked Examples

**A null vector of the vector subspace.** For $\tilde Q=e_1+ie_2$ the norm is $1+i^{2}=0$, so the element lies on the cone and is a zero divisor; it is one of the isotropic directions of the vector subspace, a point of the conic $\sum_kQ_k^{2}=0$.

**A non-pure null element.** For $\tilde Q=e_0+ie_1$ the norm is again $1+i^{2}=0$, but the element is not pure: it is a non-pure zero divisor, so the cone has points outside the pure cone of the vector subspace, and the classification of the two families is *Zero Divisors of the General Plain Algebra*.

**A point of each family.** On the complex generators displayed, $\langle e_0+ie_1,e_2+ie_3\rangle_{\natural}=0$ and $\langle e_0+ie_1,e_2-ie_3\rangle_{\natural}=0$, so the line $\mathbb{C}(e_0+ie_1)$ lies in one plane of each family; the two planes $W_+$ and $W_-$ meet along it, as the proposition records.

**A unit outside the cone.** For $\tilde Q=e_0+e_1$ the norm is $1+1=2\neq0$, so the element is a unit and lies off the cone: the cone is exactly the zero-divisor set.

## Summary

The null cone of the general quaternionic bilinear form is $\sum_\mu Q_\mu^2=0$, the zero-divisor cone of the algebra, of complex dimension $3$ and real dimension $6$, non-singular off the apex, which is its only singular point. It is ruled by two families of maximal totally isotropic planes, of complex dimension $2$, and the maximal totally isotropic dimension is $2$ over $\mathbb{C}$ and $4$ over the realified form of signature $(4,4)$. The realified form has index $4$ and trivial defect (*The Realification of the Four Forms*). The cone is exactly the zero-divisor set: a nonzero null element is a zero divisor, and the algebra is a division algebra off the cone. The restrictions of the form to the remarkable subspaces, and the comparison of this cone with the null cones of the three sibling forms, belong to *Remarkable Subspaces under the General Quaternionic Algebra of Biquaternions* and to the synthesis of the four forms.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal N_{\natural}=\{\tilde Q:\sum_\mu Q_\mu^2=0\}$ | The null cone of the general quaternionic bilinear form |
| real dimension $6$ | Its dimension in $\mathbb B$; complex dimension $3$ |
| $\mathcal N_{\natural}\setminus\{0\}$ | The zero-divisor set of the algebra |
| $W_+=\mathbb{C}\{e_0+ie_1,e_2+ie_3\}$, $W_-=\mathbb{C}\{e_0+ie_1,e_2-ie_3\}$ | The two maximal totally isotropic planes, one from each family |
| index $4$ | The number of negative directions of the realified form on $\mathbb{R}^8$ |

## Further Reading

- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the form
- *Zero Divisors of the General Plain Algebra* (`articles_maths/zero-divisors-of-the-general-plain-algebra.md`), for the classification of the isotropic elements
- *Remarkable Subspaces under the General Quaternionic Algebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-general-quaternionic-algebra-of-biquaternions.md`), for the restrictions of the form to the remarkable subspaces, the indexes and the maximal totally isotropic dimensions of the restrictions
- *The Realification of the Four Forms* (`articles_maths/the-realification-of-the-four-forms.md`), for the realified null cones of the four forms and the comparison of the cones
- *The Null Quadric and Its Projective Geometry* (`articles_maths/the-null-quadric-and-its-projective-geometry.md`), for the quadric surface and the rulings
- *The Topology of the Zero-Divisor Cone* (`articles_maths/the-topology-of-the-zero-divisor-cone.md`), for the link of the cone
