
# __The Isotropic Structure of the Quaternion Bilinear Form__

## Introduction

The quaternion bilinear form

$$
\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde P\tilde Q^{\natural})=\sum_\mu P_\mu Q_\mu
$$

has for its null set the zero-divisor cone of the algebra. This article develops the cone: its dimension and its smoothness off the apex, its rulings and the maximal totally isotropic planes, the index and the defect of the realified form, the link of the cone, and its identification with the zero-divisor set of the algebra.

The form itself, its polarisation and its quadratic space are *The Quaternion Bilinear Form on the Biquaternion Algebra*; the six subspaces and their restriction matrices are *The Six Subspaces under the Quaternion Bilinear Form*; the classification of the isotropic elements is *Biquaternion Zero Divisors*; the projective picture of the cone, the quadric surface, the Klein quadric and the Plücker embedding are *Biquaternion Topology*; and the invertibility criterion that makes the cone the boundary of the group of units is *Biquaternion Norm and Invertibility*.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$ and central scalar imaginary $i$; a general element is $\tilde{Q}=\sum_\mu Q_\mu e_\mu$ with $Q_\mu=q_\mu+iq'_\mu$, $q_\mu,q'_\mu\in\mathbb{R}$, so that $\tilde{Q}=\sum_\mu q_\mu e_\mu+\sum_\mu q'_\mu\,ie_\mu$ on the eight real basis elements. The norm is $N(\tilde Q)=\sum_\mu Q_\mu^2=\langle\tilde Q,\tilde Q\rangle_{\natural}$, and $\|\tilde Q\|_E=(\sum_\mu|Q_\mu|^2)^{1/2}$ is the Euclidean norm of the coefficient space.

## The Null Cone

**Definition.** The **null cone** of the quaternion bilinear form is

$$
\mathcal N_{\natural}=\{\tilde Q:\langle\tilde Q,\tilde Q\rangle_{\natural}=0\}=\Bigl\{\tilde Q:\sum_\mu Q_\mu^2=0\Bigr\}.
$$

**Proposition (dimension and smoothness).** On $\mathbb{C}^4\cong\mathbb{B}$ the cone is the complex quadric $\sum_\mu Q_\mu^2=0$, a complex hypersurface through the origin: of complex dimension $3$ and **real dimension $6$**. It is a cone, invariant under $\tilde Q\mapsto\lambda\tilde Q$ for every $\lambda\in\mathbb{C}$, and it is smooth off the apex, which is its only singular point.

*Proof.* The defining polynomial is $f(Q_0,\dots,Q_3)=\sum_\mu Q_\mu^2$, whose complex gradient is $2(Q_0,\dots,Q_3)$; the gradient vanishes only at the apex, so the complex hypersurface is smooth of complex dimension $3$, hence real dimension $6$, off it; at the apex all four complex partial derivatives vanish and the apex is the only singular point. Equivalently, $f$ gives the two real equations $\mathrm{Re}\,f=0$, $\mathrm{Im}\,f=0$, whose real Jacobian has rank $2$ off the apex. Verification: at the explicit cone points $e_0+ie_1$, $e_0+ie_2$ and $ie_0+e_1$ the rank is $2$, so the real dimension is $8-2=6$, and at the apex the rank is $0$.

**Proposition (the cone is the zero-divisor set).** The cone is exactly the zero-divisor set: an element is a unit precisely when its norm is nonzero, so a nonzero null element is a zero divisor, and the algebra is a division algebra off the cone.

*Proof.* The criterion for invertibility is $N(\tilde Q)\neq0$, which is the statement that the diagonal of the form does not vanish. Hence the nonzero null elements are exactly the nonzero non-units, and the classification of the two families of zero divisors is by their purity. Verified: $N(e_1+ie_2)=1+i^{2}=0$ and $N(e_0+ie_1)=1+i^{2}=0$, both zero divisors, while $N(e_0+e_1)=2$.

The projective picture of the cone – the Segre embedding, the quadric surface, the two rulings of null planes, the tangency and the polarity – is *Biquaternion Topology*.

## The Rulings and the Maximal Totally Isotropic Planes

**Definition.** A subspace $W\subset\mathbb{B}$ is **totally isotropic** when the form vanishes on it identically, $\langle\tilde P,\tilde Q\rangle_{\natural}=0$ for all $\tilde P,\tilde Q\in W$; equivalently when $W$ is isotropic and orthogonal to itself.

**Proposition (the maximal totally isotropic planes).** Over $\mathbb{C}$ the maximal totally isotropic dimension is $2$, and the maximal totally isotropic subspaces are the planes of two families, the **two rulings** of the quadric. The two planes

$$
W_{+}=\mathbb{C}\{e_0+ie_1,\;e_2+ie_3\},\qquad
W_{-}=\mathbb{C}\{e_0+ie_1,\;e_2-ie_3\}
$$

are totally isotropic, one from each family; through each smooth point of the cone passes one plane of each family, and two planes of the same family meet only at the origin, while two planes of the two families meet along a line.

*Proof.* On the generators of $W_+$ the form vanishes, $\langle e_0+ie_1,e_0+ie_1\rangle=1+i^{2}=0$, $\langle e_2+ie_3,e_2+ie_3\rangle=1+i^{2}=0$ and $\langle e_0+ie_1,e_2+ie_3\rangle=0$, and the same computation holds for $W_-$; a $\mathbb{C}$-bilinear form vanishing on a generating set vanishes on the span, so both planes are totally isotropic. The two differ in the sign carried by the $e_3$ direction, and that is what puts them in different families: $W_+\cap W_-=\mathbb{C}(e_0+ie_1)$, a line, so the two planes meet rather than being skew, while the planes of a single family, such as $\mathbb{C}\{e_0+ie_1,e_2+ie_3\}$ and its sign-mirror $\mathbb{C}\{e_0-ie_1,e_2-ie_3\}$, intersect only at the origin. The upper bound is the Witt index of the form, which is $2$ over $\mathbb{C}$: the two-dimensional plane $\mathbb{C}\{e_0+ie_2,\;e_1+ie_3\}$ is totally isotropic and of dimension $2$, and no three-dimensional subspace can be isotropic because the form is non-degenerate of rank $4$. Verified: the form vanishes identically on both planes and on the two sign-mirrors, and the intersections are a line across the families and the origin within one family. The families are the two rulings of the quadric surface $Q^2$ of *Biquaternion Topology*.

**Corollary (the maximal totally isotropic dimension of the realified form).** The realified form of signature $(4,4)$ has maximal totally isotropic real dimension $4$.

*Proof.* The bound is the smaller of the two inertia indices of the signature $(4,4)$, which is $4$, and the realification of one of the complex planes above is a real totally isotropic $4$-space attaining it.

## The Minimal Ideals and the Hyperbolic Peirce Basis

The null cone of the form is the zero-divisor set of the algebra, and the one-sided ideals it carries are the maximal totally isotropic subspaces.

**Theorem (the minimal ideals are the maximal isotropic one-sided ideals).** Every minimal left ideal and every minimal right ideal of $\mathbb{B}$ is a maximal totally isotropic subspace of the quaternion bilinear form. Conversely, a maximal totally isotropic subspace that is a left ideal is a minimal left ideal, and likewise on the right.

*Proof.* Let $\tilde Q\ne0$ be null for the form and let $\tilde X,\tilde Y\in\mathbb{B}$. Then

$$
\langle\tilde X\tilde Q,\tilde Y\tilde Q\rangle_{\natural}=\mathrm{Sc}\!\left(\tilde X\tilde Q\tilde Q^{\natural}\tilde Y^{\natural}\right)=\mathrm{Sc}\!\left(\tilde X\,\langle\tilde Q,\tilde Q\rangle_{\natural}\tilde Y^{\natural}\right)=\langle\tilde Q,\tilde Q\rangle_{\natural}\,\mathrm{Sc}\!\left(\tilde X\tilde Y^{\natural}\right)=0,
$$

so the left ideal $\mathbb{B}\tilde Q$ is totally isotropic; it has complex dimension $2$, and a totally isotropic subspace of the four-dimensional complex algebra has complex dimension at most $2$, since the form is non-degenerate of Witt index $2$. So $\mathbb{B}\tilde Q$ is maximal, and conversely a maximal totally isotropic left ideal is generated by a null element and is minimal. The right-handed statements are the mirror. $\square$

The theorem is not an equality of families: the maximal totally isotropic subspaces form a larger family than the one-sided ideals, and the two families meet in the minimal ideals. In the Peirce basis $\tilde\Pi,\tilde R,f,\tilde T$ of *Biquaternion Ideals and Peirce Decomposition*, where $\tilde\Pi=\tfrac12(e_0+ie_1)$, $f=e_0-\tilde\Pi$, $\tilde R=e_3+ie_2$ and $\tilde T=e_3-ie_2$, the Gram matrix of the form is

$$
\begin{pmatrix}
0 & 0 & \tfrac{1}{2} & 0 \\
0 & 0 & 0 & 2 \\
\tfrac{1}{2} & 0 & 0 & 0 \\
0 & 2 & 0 & 0
\end{pmatrix},
$$

an antidiagonal matrix: **the form is hyperbolic in the Peirce basis, and the four Peirce lines are paired by it**, the idempotent line $\mathbb{C}\tilde\Pi$ with the idempotent line $\mathbb{C}f$ and the nilpotent line $\mathbb{C}\tilde R$ with the nilpotent line $\mathbb{C}\tilde T$. The two minimal left ideals $\mathbb{B}\tilde\Pi=\mathbb{C}\tilde\Pi\oplus\mathbb{C}\tilde R$ and $\mathbb{B}f=\mathbb{C}f\oplus\mathbb{C}\tilde T$ are maximal totally isotropic by the theorem, and the span of $\tilde\Pi$ and $\tilde T$, one line from each, is a maximal totally isotropic subspace that is **not** a left ideal, since it mixes the two.

**Corollary (the isotropic lines of the six).** Since the null elements of the form are exactly the zero divisors, its isotropic lines inside the six subspaces are their zero-divisor lines: none in the centre, the quaternion subspace and the anti-quaternion subspace, which have no nonzero null element; the complex lines of the nilpotents in the vector subspace; and the lines of the real multiples of the Hermitian idempotents in the two Hermitian subspaces. No isotropic subspace beyond a line lies inside a single one of the six, since each restriction is non-degenerate, and the six subspaces are *The Six Subspaces under the Quaternion Bilinear Form* and *Introduction to the Six Subspaces*.

## The Index and the Defect

**Definition.** The **index** of the realified form is the number of negative eigenvalues of its Gram matrix, and the **defect** or radical is the subspace of vectors orthogonal to the whole space.

**Proposition (the index and the defect of the realified form).** The realified form on $\mathbb{R}^8$ has index $4$, of signature $(4,4)$, and trivial defect.

*Proof.* In the grouped real basis $e_0,\dots,e_3,ie_0,\dots,ie_3$ the Gram matrix is $\operatorname{diag}(I_4,-I_4)$, with four $+1$ and four $-1$ diagonal entries: the signature is $(4,4)$, the index is the number of negative entries, and the determinant is $1$, so the matrix is invertible and the radical is trivial. Verified on the diagonal matrix.

**Remark (the defect vanishes and the index does not).** The two invariants measure different things: a non-degenerate form may still have a nonzero index, and an index zero is the definite case. The vanishing of the defect is what makes the realified form a quadratic space in its own right, and it is why it defines an orthogonal group; the index is what decides whether that form has an isotropic cone. The index and the defect of the restriction to each of the six distinguished subspaces are recorded with the restriction matrices in *The Six Subspaces under the Quaternion Bilinear Form*.

## The Link of the Cone

**Proposition (the link).** The link of the cone, that is its intersection with the Euclidean unit sphere $S^7=\{\|\tilde Q\|_E=1\}$, is a compact real $5$-manifold, and it is an $S^1$-bundle over the quadric surface $Q^2\cong\mathbb{P}^1\times\mathbb{P}^1\cong S^2\times S^2$.

*Proof.* The cone has real dimension $6$ and the sphere has real dimension $7$, and the cone is a real cone with apex at the origin, so its link is of real dimension $5$; the intersection is a transverse intersection away from the apex, since the real gradient of the two real equations defining the cone has rank $2$ there and the sphere contributes the radial direction. The projection $\mathbb{C}^4\setminus\{0\}\to\mathbb{P}^3$ carries the cone minus the apex onto the quadric surface $Q^2$ with fibres the complex lines, and the unit sphere selects in each fibre the circle of radius one, so the link is the circle bundle of the tautological line bundle over $Q^2$. The quadric surface is smooth, hence $\mathbb{P}^1\times\mathbb{P}^1$, and $\mathbb{P}^1\cong S^2$. Verified: the dimension count $3+2=5$ matches, the cone contributes a complex dimension $3$ and the projective quadric a real dimension $4$.

The link, the rulings and the projective reading are *Biquaternion Topology*; the Euclidean sphere and its relation to the cone are *The Euclidean Topology of the Biquaternion Algebra*.

## Worked Examples

**A null vector of the vector subspace.** For $\tilde Q=e_1+ie_2$ the norm is $1+i^{2}=0$, so the element lies on the cone and is a zero divisor; it is one of the isotropic directions of the vector subspace, a point of the conic $\sum_kQ_k^{2}=0$.

**A non-pure null element.** For $\tilde Q=e_0+ie_1$ the norm is again $1+i^{2}=0$, but the element is not pure: it is a non-pure zero divisor, so the cone has points outside the pure cone of the vector subspace, and the classification of the two families is *Biquaternion Zero Divisors*.

**A point of each ruling.** On the complex generators displayed, $\langle e_0+ie_1,e_2+ie_3\rangle_{\natural}=0$ and $\langle e_0+ie_1,e_2-ie_3\rangle_{\natural}=0$, so the line $\mathbb{C}(e_0+ie_1)$ lies in one plane of each family; the two planes $W_+$ and $W_-$ meet along it, as the proposition records.

**A unit outside the cone.** For $\tilde Q=e_0+e_1$ the norm is $1+1=2\neq0$, so the element is a unit and lies off the cone: the cone is exactly the zero-divisor set.

## Summary

The null cone of the quaternion bilinear form is $\sum_\mu Q_\mu^2=0$, the zero-divisor cone of the algebra, of complex dimension $3$ and real dimension $6$, smooth off the apex, which is its only singular point. It is ruled by two families of maximal totally isotropic planes, of complex dimension $2$, and the maximal totally isotropic dimension is $2$ over $\mathbb{C}$ and $4$ over the realified form of signature $(4,4)$. The realified form has index $4$ and trivial defect. The link of the cone is a compact real $5$-manifold, an $S^1$-bundle over the quadric surface $Q^2\cong S^2\times S^2$. The cone is exactly the zero-divisor set: a nonzero null element is a zero divisor, and the algebra is a division algebra off the cone. The restrictions of the form to the six distinguished subspaces, and the comparison of this cone with the null cones of the three sibling forms, belong to *The Six Subspaces under the Quaternion Bilinear Form* and to the synthesis of the four forms.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal N_{\natural}=\{\tilde Q:\sum_\mu Q_\mu^2=0\}$ | The null cone of the quaternion bilinear form |
| real dimension $6$ | Its dimension in $\mathbb B$; complex dimension $3$ |
| $\mathcal N_{\natural}\setminus\{0\}$ | The zero-divisor set of the algebra |
| $W_+=\mathbb{C}\{e_0+ie_1,e_2+ie_3\}$, $W_-=\mathbb{C}\{e_0+ie_1,e_2-ie_3\}$ | The two maximal totally isotropic planes, one from each ruling |
| index $4$ | The number of negative directions of the realified form on $\mathbb{R}^8$ |
| $\mathrm{Link}=\{\|\tilde Q\|_E=1\}\cap\mathcal N_{\natural}$ | The link, an $S^1$-bundle over $Q^2$ |

## Further Reading

- *The Quaternion Bilinear Form on the Biquaternion Algebra* (`articles_maths/the-quaternion-bilinear-form-on-the-biquaternion-algebra.md`), for the form
- *Biquaternion Zero Divisors* (`articles_maths/biquaternion-zero-divisors.md`), for the classification of the isotropic elements
- *The Six Subspaces under the Quaternion Bilinear Form* (`articles_maths/the-six-subspaces-under-the-quaternion-bilinear-form.md`), for the restrictions of the form to the six subspaces, the indexes and the maximal totally isotropic dimensions of the restrictions
- *The Realification of the Four Forms* (`articles_maths/the-realification-of-the-four-forms.md`), for the realified null cones of the four forms and the comparison of the cones
- *Biquaternion Topology* (`articles_maths/biquaternion-topology.md`), for the quadric surface and the rulings
