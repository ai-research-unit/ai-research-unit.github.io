
# __The Isotropic Structure of the General Quaternionic Algebra__

## Introduction

The general quaternionic bilinear form

$$
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{\natural})=\sum_\mu Q_{1,\mu} Q_{2,\mu}
$$

has for its null set the zero-divisor cone of the algebra. This article develops the cone: its two families of maximal totally isotropic planes, the minimal ideals it carries, and its identification with the zero-divisor set of the algebra. The topology of the cone and the realified invariants are not developed here; the pointers are in the last paragraph of this introduction.

The form itself, its polarisation and its quadratic space are *Norm and Invertibility in the General Quaternionic Algebra*; the remarkable subspaces and their restriction matrices are *Remarkable Subspaces under the General Quaternionic Algebra*; the classification of the isotropic elements is *Zero Divisors of the Biquaternion Algebra*; the projective picture of the cone, the quadric surface, the Klein quadric and the Plücker embedding are *The Null Quadric and Its Projective Geometry*; and the invertibility criterion that makes the cone the boundary of the group of units is *Norm and Invertibility in the General Quaternionic Algebra*. The topology of the cone, its dimension, its apex and its link are *The Topology of the Zero-Divisor Cone*; the index, the defect and the signature of the realified form are *The Realification of the Four Forms*, and their values on the remarkable subspaces are *Remarkable Subspaces under the General Quaternionic Algebra*.

## The Null Cone

**Definition.** The **null cone** of the general quaternionic bilinear form is

$$
\mathcal N_{\natural}=\{\tilde Q:\langle\tilde Q,\tilde Q\rangle_{\natural}=0\}=\Bigl\{\tilde Q:\sum_\mu Q_\mu^2=0\Bigr\}.
$$

The cone is the zero set of the polynomial $f=\sum_\mu Q_\mu^2$, homogeneous of degree two and invariant under $\tilde Q\mapsto\lambda\tilde Q$ for every $\lambda\in\mathbb{C}$; its dimension and its singular point are *The Topology of the Zero-Divisor Cone*. Nothing of the cone's form beyond its equation is used below.

**Proposition (the cone is the zero-divisor set).** The cone is exactly the zero-divisor set: an element is a unit precisely when its norm is nonzero, so a nonzero null element is a zero divisor, and the algebra is a division algebra off the cone.

*Proof.* The criterion for invertibility is $\langle\tilde Q\rangle_{\natural}\neq0$, which is the statement that the form does not vanish at the two equal arguments. Hence the nonzero null elements are exactly the nonzero non-units, and the classification of the two families of zero divisors is by their purity.

The projective geometry of the cone is *The Null Quadric and Its Projective Geometry*.

## The Maximal Totally Isotropic Planes

**Definition.** A subspace $W\subset\mathbb{B}$ is **totally isotropic** when the form vanishes on it identically, $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=0$ for all $\tilde Q_1,\tilde Q_2\in W$; equivalently when $W$ is isotropic and orthogonal to itself.

**Proposition (the maximal totally isotropic planes).** Over $\mathbb{C}$ the maximal totally isotropic dimension is $2$, and the maximal totally isotropic subspaces are the planes of two families. The two planes

$$
\boxed{\; W_{+}=\mathbb{C}\{e_t+i\vec e_x,\;\vec e_y+i\vec e_z\},\qquad
W_{-}=\mathbb{C}\{e_t+i\vec e_x,\;\vec e_y-i\vec e_z\} \;}
$$

are totally isotropic, one from each family; through each non-singular point of the cone passes one plane of each family, and two planes of the same family meet only at the origin, while two planes of the two families meet along a line.

*Proof.* On the generators of $W_+$ the form vanishes, $\langle e_t+i\vec e_x,e_t+i\vec e_x\rangle=1+i^{2}=0$, $\langle \vec e_y+i\vec e_z,\vec e_y+i\vec e_z\rangle=1+i^{2}=0$ and $\langle e_t+i\vec e_x,\vec e_y+i\vec e_z\rangle=0$, and the same computation holds for $W_-$; a $\mathbb{C}$-bilinear form vanishing on a generating set vanishes on the span, so both planes are totally isotropic. The two differ in the sign carried by the $\vec e_z$ direction, and that is what puts them in different families: $W_+\cap W_-=\mathbb{C}(e_t+i\vec e_x)$, a line, so the two planes meet rather than being skew, while the planes of a single family, such as $\mathbb{C}\{e_t+i\vec e_x,\vec e_y+i\vec e_z\}$ and its sign-mirror $\mathbb{C}\{e_t-i\vec e_x,\vec e_y-i\vec e_z\}$, intersect only at the origin. The upper bound is the Witt index of the form, which is $2$ over $\mathbb{C}$: the two-dimensional plane $\mathbb{C}\{e_t+i\vec e_y,\;\vec e_x+i\vec e_z\}$ is totally isotropic and of dimension $2$, and no three-dimensional subspace can be isotropic because the form is non-degenerate of rank $4$. The two families are those attached to the quadric in *The Null Quadric and Its Projective Geometry*.

**Corollary (the maximal totally isotropic dimension of the realified form).** The realified form of signature $(4,4)$ has maximal totally isotropic real dimension $4$.

*Proof.* The bound is the smaller of the two inertia indices of the signature $(4,4)$, which is $4$, and the realification of one of the complex planes above is a real totally isotropic $4$-space attaining it. The index, the defect and the full signature of the realified form, and their values on the remarkable subspaces, are *The Realification of the Four Forms* and *Remarkable Subspaces under the General Quaternionic Algebra*.

## The Minimal Ideals and the Hyperbolic Peirce Basis

The null cone of the form is the zero-divisor set of the algebra, and the one-sided ideals it carries are the maximal totally isotropic subspaces.

**Theorem (the minimal ideals are the maximal isotropic one-sided ideals).** Every minimal left ideal and every minimal right ideal of $\mathbb{B}$ is a maximal totally isotropic subspace of the general quaternionic bilinear form. Conversely, a maximal totally isotropic subspace that is a left ideal is a minimal left ideal, and likewise on the right.

*Proof.* Let $\tilde Q\ne0$ be null for the form and let $\tilde Q_1,\tilde Q_2\in\mathbb{B}$. Then

$$
\langle\tilde Q_1\tilde Q,\tilde Q_2\tilde Q\rangle_{\natural}=\mathrm{Sc}\!\left(\tilde Q_1\tilde Q\tilde Q^{\natural}\tilde Q_2^{\natural}\right)=\mathrm{Sc}\!\left(\tilde Q_1\,\langle\tilde Q,\tilde Q\rangle_{\natural}\tilde Q_2^{\natural}\right)=\langle\tilde Q,\tilde Q\rangle_{\natural}\,\mathrm{Sc}\!\left(\tilde Q_1\tilde Q_2^{\natural}\right)=0,
$$

so the left ideal $\mathbb{B}\tilde Q$ is totally isotropic; it has complex dimension $2$, and a totally isotropic subspace of the four-dimensional complex algebra has complex dimension at most $2$, since the form is non-degenerate of Witt index $2$. So $\mathbb{B}\tilde Q$ is maximal, and conversely a maximal totally isotropic left ideal is generated by a null element and is minimal. The right-handed statements are the mirror.

The theorem is not an equality of families: the maximal totally isotropic subspaces form a larger family than the one-sided ideals, and the two families meet in the minimal ideals. In the Peirce basis $\tilde\Pi,\vec\Upsilon_x,f,\vec\Upsilon_y$ of *Ideals and Peirce Decomposition of the Biquaternion Algebra*, where $\tilde\Pi=\tfrac12(e_t+i\vec e_x)$, $f=e_t-\tilde\Pi$, $\vec\Upsilon_x=\vec e_z+i\vec e_y$ and $\vec\Upsilon_y=\vec e_z-i\vec e_y$, the Gram matrix of the form is

$$
\boxed{\; \begin{pmatrix}
0 & 0 & \tfrac{1}{2} & 0 \\
0 & 0 & 0 & 2 \\
\tfrac{1}{2} & 0 & 0 & 0 \\
0 & 2 & 0 & 0
\end{pmatrix} \;},
$$

an antidiagonal matrix: **the form is hyperbolic in the Peirce basis, and the four Peirce lines are paired by it**, the idempotent line $\mathbb{C}\tilde\Pi$ with the idempotent line $\mathbb{C}f$ and the nilpotent line $\mathbb{C}\vec\Upsilon_x$ with the nilpotent line $\mathbb{C}\vec\Upsilon_y$. The two minimal left ideals $\mathbb{B}\tilde\Pi=\mathbb{C}\tilde\Pi\oplus\mathbb{C}\vec\Upsilon_x$ and $\mathbb{B}f=\mathbb{C}f\oplus\mathbb{C}\vec\Upsilon_y$ are maximal totally isotropic by the theorem, and the span of $\tilde\Pi$ and $\vec\Upsilon_y$, one line from each, is a maximal totally isotropic subspace that is **not** a left ideal, since it mixes the two.

**Corollary (the isotropic lines of the remarkable subspaces).** Since the null elements of the form are exactly the zero divisors, its isotropic lines inside the remarkable subspaces are their zero-divisor lines, tabulated in *Remarkable Subspaces under the General Quaternionic Algebra*, §*The Isotropic Lines of the Indefinite Restrictions*; no isotropic subspace beyond a line lies inside a single one of the remarkable subspaces, since each restriction is non-degenerate.

## Worked Examples

**A null vector of the vector subspace.** For $\tilde Q=\vec e_x+i\vec e_y$ the norm is $1+i^{2}=0$, so the element lies on the cone and is a zero divisor; it is one of the isotropic directions of the vector subspace, a point of the conic $\sum_kQ_k^{2}=0$.

**A non-pure null element.** For $\tilde Q=e_t+i\vec e_x$ the norm is again $1+i^{2}=0$, but the element is not pure: it is a non-pure zero divisor, so the cone has points outside the pure cone of the vector subspace, and the classification of the two families is *Zero Divisors of the Biquaternion Algebra*.

**A point of each family.** On the complex generators displayed, $\langle e_t+i\vec e_x,\vec e_y+i\vec e_z\rangle_{\natural}=0$ and $\langle e_t+i\vec e_x,\vec e_y-i\vec e_z\rangle_{\natural}=0$, so the line $\mathbb{C}(e_t+i\vec e_x)$ lies in one plane of each family; the two planes $W_+$ and $W_-$ meet along it, as the proposition records.

**A unit outside the cone.** For $\tilde Q=e_t+\vec e_x$ the norm is $1+1=2\neq0$, so the element is a unit and lies off the cone: the cone is exactly the zero-divisor set.

## Summary

The null cone of the general quaternionic bilinear form is $\sum_\mu Q_\mu^2=0$, the zero-divisor cone of the algebra, of complex dimension $3$ and real dimension $6$, non-singular off the apex, which is its only singular point. It is ruled by two families of maximal totally isotropic planes, of complex dimension $2$, and the maximal totally isotropic dimension is $2$ over $\mathbb{C}$ and $4$ over the realified form of signature $(4,4)$. The realified form has index $4$ and trivial defect (*The Realification of the Four Forms*). The cone is exactly the zero-divisor set: a nonzero null element is a zero divisor, and the algebra is a division algebra off the cone. The restrictions of the form to the remarkable subspaces, and the comparison of this cone with the null cones of the three sibling forms, belong to *Remarkable Subspaces under the General Quaternionic Algebra* and to the synthesis of the four forms.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal N_{\natural}=\{\tilde Q:\sum_\mu Q_\mu^2=0\}$ | The null cone of the general quaternionic bilinear form |
| real dimension $6$ | Its dimension in $\mathbb B$; complex dimension $3$ |
| $\mathcal N_{\natural}\setminus\{0\}$ | The zero-divisor set of the algebra |
| $W_+=\mathbb{C}\{e_t+i\vec e_x,\vec e_y+i\vec e_z\}$, $W_-=\mathbb{C}\{e_t+i\vec e_x,\vec e_y-i\vec e_z\}$ | The two maximal totally isotropic planes, one from each family |
| index $4$ | The number of negative directions of the realified form on $\mathbb{R}^8$ |

## Further Reading

- [The 4 Forms over the Biquaternion $\mathbb{C}$ Space](the-4-forms-over-the-biquaternion-c-space.html), for the form
- [Zero Divisors of the Biquaternion Algebra](zero-divisors-of-the-biquaternion-algebra.html), for the classification of the isotropic elements
- [Remarkable Subspaces under the General Quaternionic Algebra](remarkable-subspaces-under-the-general-quaternionic-algebra.html), for the restrictions of the form to the remarkable subspaces, the indexes and the maximal totally isotropic dimensions of the restrictions
- [The Realification of the Eight Derived Structures](the-realification-of-the-eight-derived-structures.html), for the realified null cones of the four forms and the comparison of the cones
- [The Null Quadric and Its Projective Geometry](the-null-quadric-and-its-projective-geometry.html), for the null quadric and the rulings
- [The Topology of the Zero-Divisor Cone](the-topology-of-the-zero-divisor-cone.html), for the link of the cone
