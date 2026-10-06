
# __The Isotropic Structure of the Quaternion Bilinear Form__

## Introduction

The quaternion bilinear form

$$
\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde P\tilde Q^{\natural})=\sum_\mu P_\mu Q_\mu
$$

has for its null set the zero-divisor cone of the algebra. This article develops the cone: its dimension and its smoothness off the apex, its rulings and the maximal totally isotropic planes, its index and its defect, the link of the cone, its real dimension on each of the six distinguished subspaces, and the comparison with the null cone of the complex bilinear form.

The form itself, its polarisation and its quadratic space are *The Quaternion Bilinear Form on the Biquaternion Algebra*; the six subspaces and their restriction matrices are *The Six Subspaces under the Quaternion Bilinear Form*; the classification of the isotropic elements is *Biquaternion Zero Divisors*; the projective picture of the cone, the quadric surface, the Klein quadric and the Plücker embedding are *Biquaternion Topology*; and the invertibility criterion that makes the cone the boundary of the group of units is *Biquaternion Norm and Invertibility*.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$ and central scalar imaginary $i$; a general element is $\tilde{Q}=\sum_\mu Q_\mu e_\mu$ with $Q_\mu=q_\mu+iq'_\mu$, $q_\mu,q'_\mu\in\mathbb{R}$, so that $\tilde{Q}=\sum_\mu q_\mu e_\mu+\sum_\mu q'_\mu\,ie_\mu$ on the eight real basis elements. The norm is $N(\tilde Q)=\sum_\mu Q_\mu^2$.

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

*Proof.* On the generators of $W_+$ the form vanishes, $\langle e_0+ie_1,e_0+ie_1\rangle=1+i^{2}=0$, $\langle e_2+ie_3,e_2+ie_3\rangle=1+i^{2}=0$ and $\langle e_0+ie_1,e_2+ie_3\rangle=0$, and the same computation holds for $W_-$; a $\mathbb{C}$-bilinear form vanishing on a generating set vanishes on the span, so both planes are totally isotropic. The two differ in the sign carried by the $e_3$ direction, and that is what puts them in different families: $W_+\cap W_-=\mathbb{C}(e_0+ie_1)$, a line, so the two planes meet rather than being skew, while the planes of a single family, such as $\mathbb{C}\{e_0+ie_1,e_2+ie_3\}$ and its sign-mirror $\mathbb{C}\{e_0-ie_1,e_2-ie_3\}$, intersect only at the origin. The upper bound is the Witt index of the form, which is $2$ over $\mathbb{C}$: the two-dimensional plane $\mathbb{C}\{e_0+ie_2,\;e_1+ie_3\}$ is totally isotropic and of dimension $2$, and no three-dimensional subspace can be isotropic because the form is non-degenerate of rank $4$. Verified: the form vanishes identically on both planes and on the two sign-mirrors, and the intersections are a line across the families and the origin within one family. The families are the two rulings of the quadric surface $Q^2$ of *Biquaternion Topology*; over $\mathbb{R}$ the realified form of signature $(4,4)$ has maximal totally isotropic real dimension $4$, the realification of any of these planes.

**Corollary (the maximal totally isotropic dimension on the real forms).** On the Hermitian and anti-Hermitian subspaces, where the restriction is a real form of the interval of signature $(1,3)$ and $(3,1)$, the maximal totally isotropic dimension is $1$, a null line; on the vector subspace, where the restriction is the complex quadratic $\sum_kQ_k^2$, it is $1$ over $\mathbb{C}$ and $3$ over $\mathbb{R}$; on the two definite quaternion subspaces it is $0$.

*Proof.* Each value is the smaller of the two inertia indices of the restricted form. On the vector subspace the restriction is a complex quadratic form of complex dimension $3$, of complex Witt index $1$, so the complex value is $1$; its realification has signature $(3,3)$, so the real value is $3$, attained by the real $3$-space $\mathbb{R}\{e_1+ie_1,\;e_2+ie_2,\;e_3+ie_3\}$, which is totally isotropic and larger than the realification of a single complex isotropic line. Verified against the six restriction matrices and on that explicit $3$-space.

## The Index and the Defect

**Definition.** The **index** of the realified form on a subspace is the number of negative eigenvalues of its restriction Gram matrix; the **defect** or radical is the subspace of vectors orthogonal to the whole subspace.

**Proposition (the index table).** The realified form on $\mathbb{R}^8$ has index $4$, of signature $(4,4)$; on the six subspaces the index is $1,3,0,4,3,1$; and the defect is trivial on the algebra and on each of the six subspaces, every restriction being non-degenerate.

*Proof.* The index is read from the signatures: $(1,1)$ gives $1$, $(3,3)$ gives $3$, $(4,0)$ gives $0$, $(0,4)$ gives $4$, $(1,3)$ gives $3$ and $(3,1)$ gives $1$; on the whole algebra the realified Gram matrix $\operatorname{diag}(I_4,-I_4)$ has four negative eigenvalues. A restriction Gram matrix of nonzero determinant has no radical, and each of the six determinants is $\pm1$. Verified on the six restriction matrices and on the realified matrix of the whole form.

**Remark (the defect vanishes and the index does not).** The two invariants measure different things: a non-degenerate restriction may still have a nonzero index, and a restriction of index zero is the definite case. The vanishing of the defect is what makes the restriction a quadratic space in its own right, and it is why each row of the table defines an orthogonal group; the index is what decides whether that form has an isotropic cone.

## The Link of the Cone

**Proposition (the link).** The link of the cone, that is its intersection with the Euclidean unit sphere $S^7=\{\|\tilde Q\|_E=1\}$, is a compact real $5$-manifold, and it is an $S^1$-bundle over the quadric surface $Q^2\cong\mathbb{P}^1\times\mathbb{P}^1\cong S^2\times S^2$.

*Proof.* The cone has real dimension $6$ and the sphere has real dimension $7$, and the cone is a real cone with apex at the origin, so its link is of real dimension $5$; the intersection is a transverse intersection away from the apex, since the real gradient of the two real equations defining the cone has rank $2$ there and the sphere contributes the radial direction. The projection $\mathbb{C}^4\setminus\{0\}\to\mathbb{P}^3$ carries the cone minus the apex onto the quadric surface $Q^2$ with fibres the complex lines, and the unit sphere selects in each fibre the circle of radius one, so the link is the circle bundle of the tautological line bundle over $Q^2$. The quadric surface is smooth, hence $\mathbb{P}^1\times\mathbb{P}^1$, and $\mathbb{P}^1\cong S^2$. Verified: the dimension count $3+2=5$ matches, the cone contributes a complex dimension $3$ and the projective quadric a real dimension $4$.

The link, the rulings and the projective reading are *Biquaternion Topology*; the Euclidean sphere and its relation to the cone are *The Euclidean Topology of the Biquaternion Algebra*.

## The Dimension on the Six Subspaces

Intersected with the six distinguished real subspaces, the cone has the following real dimensions, read from the signatures of the restriction:

| Subspace | Restricted norm | Null set | Real dimension |
|---|---|---|---|
| Centre $\mathbb C_{\mathbb B}$ | $Q_0^2$ | $Q_0=0$ | $0$ |
| Vector $\mathrm{Vect}(\mathbb B)$ | $Q_1^2+Q_2^2+Q_3^2$ | the complex cone $\sum_kQ_k^2=0$ | $4$ |
| Quaternion $\mathbb H_{\mathbb B}$ | $\sum_\mu q_\mu^2$, signature $(4,0)$ | $\{0\}$ | $0$ |
| Anti-quaternion $i\mathbb H_{\mathbb B}$ | $-\sum_\mu(q'_\mu)^2$, signature $(0,4)$ | $\{0\}$ | $0$ |
| Hermitian $\mathbb M_+$ | $q_0^2-\sum_k(q'_k)^2$, signature $(1,3)$ | the real light cone | $3$ |
| Anti-Hermitian $\mathbb M_-$ | $\sum_kq_k^2-(q'_0)^2$, signature $(3,1)$ | the real light cone | $3$ |

Two features stand out. The restriction to the **quaternion subspace** is positive definite and to the **anti-quaternion subspace** negative definite, so neither contains a non-zero null element: these are the two subspaces on which the norm has a definite sign, and they are the reason the classical quaternion algebra is a division algebra. On the **vector subspace** the restricted form is the complex quadratic $\sum_kQ_k^2$, whose null set carries the *pure* zero divisors; on the two **real forms** it is the real light cone, whose null set carries the non-pure zero divisors. The centre carries none, being a field.

**The isotropic lines.** The isotropic elements of each subspace form the projective set of isotropic lines, and the three kinds differ:

| Subspace | Isotropic lines | Max totally isotropic |
|---|---|---|
| Centre $\mathbb C_{\mathbb B}$ | none for $N$; the two real lines $\mathbb{R}(e_0\pm ie_0)$ for the realified restriction | $0$ |
| Vector $\mathrm{Vect}(\mathbb B)$ | the conic $\{[Q]:\sum_kQ_k^2=0\}\subset\mathbb{P}^2$, a rational curve | $1$ over $\mathbb{C}$, $3$ over $\mathbb{R}$ |
| Quaternion $\mathbb H_{\mathbb B}$ | none | $0$ |
| Anti-quaternion $i\mathbb H_{\mathbb B}$ | none | $0$ |
| Hermitian $\mathbb M_+$ | the $S^2$ of null directions of the light cone | $1$ |
| Anti-Hermitian $\mathbb M_-$ | the $S^2$ of null directions of the light cone | $1$ |

**Remark (the centre is indefinite and anisotropic).** The two readings of the centre must not be confused. The realified restriction to $\mathbb{C}_{\mathbb B}$ is the hyperbolic plane $q_0^2-(q'_0)^2$, which vanishes on the two real lines $\mathbb{R}(e_0\pm ie_0)$; the complex bilinear form $N$ itself reads $Q_0R_0$ on the complex line $\mathbb{C}e_0$ and is anisotropic there, so the null set of $N$ on the centre is $\{0\}$. The dimension table records the second reading, which is the one the algebra produces.

## Comparison with the Complex Bilinear Form

The complex bilinear form has null set

$$
\Bigl\{\tilde Q:\sum_\mu\varepsilon_\mu Q_\mu^2=0\Bigr\}=\{Q_0^2=Q_1^2+Q_2^2+Q_3^2\},
$$

also a smooth complex cone, of complex dimension $3$ and real dimension $6$. As complex quadrics the two are equivalent, each being a non-degenerate quadric of $\mathbb{P}^3$, hence each isomorphic to $\mathbb{P}^1\times\mathbb{P}^1$ with the same two rulings; they differ as real forms, and their restrictions to the six subspaces differ accordingly.

**Proposition (the intersection of the two cones).** The two complex cones meet in the **pure cone**

$$
\mathcal N_{\natural}\cap\Bigl\{\sum_\mu\varepsilon_\mu Q_\mu^2=0\Bigr\}=\Bigl\{Q_0=0,\;\sum_{k=1}^{3}Q_k^2=0\Bigr\},
$$

the cone of the pure zero divisors of the vector subspace, of complex dimension $2$ and real dimension $4$; they do not meet only at the origin.

*Proof.* An element lies on both cones exactly when $\sum_\mu Q_\mu^2=0$ and $\sum_\mu\varepsilon_\mu Q_\mu^2=0$. Adding the two equations gives $2Q_0^2=0$, so $Q_0=0$; subtracting them gives $2\sum_{k=1}^3Q_k^2=0$, so $\sum_kQ_k^2=0$. Conversely these two conditions give both equations. The intersection is therefore the null cone of the restriction to the vector subspace, of real dimension $4$ by the dimension table. Verified on the corpus's representatives: $e_1+ie_2$ lies on both cones, since $1+i^{2}=0$ and $-1-(-1)=0$; $e_0+ie_1$ lies on the $\natural$-cone alone, since $1+i^{2}=0$ while $1-i^{2}=2$; and $e_0+e_1$ lies on the complex bilinear cone alone.

The $\natural$-cone meets the Krein null set in the doubly null lines $\mathbb C(e_0\pm ie_1)$ recorded in *The Isotropic Structure of the Krein Form*, and the comparison of the four null cones is the tabulated *The Real Isotropic Structure*.

## Worked Examples

**A null vector of the vector subspace.** For $\tilde Q=e_1+ie_2$ the norm is $1+i^{2}=0$, so the element lies on the cone and is a zero divisor; it is one of the isotropic directions of the vector subspace, a point of the conic $\sum_kQ_k^{2}=0$.

**A null element outside the vector subspace.** For $\tilde Q=e_0+ie_1$ the norm is again $1+i^{2}=0$, but the element is not pure; it lies on the null cone of the Hermitian subspace $\mathbb{M}_+$, and it shows that the cone has non-pure points, which the dimension table records by giving the Hermitian and anti-Hermitian rows the real dimension $3$.

**A null element of the realified centre that is not on the cone.** For $\tilde Q=e_0+ie_0$ the complex norm is $(1+i)^{2}=2i\neq0$, so the element is a unit and not on the cone, while the realified restriction of the centre vanishes on it: the two readings of the centre, the complex and the realified, must not be conflated.

**An element of the complex bilinear cone alone.** For $\tilde Q=e_0+e_1$ the norm is $2$ and the $\varepsilon$-twisted value is $1-1=0$: the element is a unit of positive norm and lies on the null cone of the sibling form only, which is the example behind the intersection statement of the comparison section.

## Summary

The null cone of the quaternion bilinear form is $\sum_\mu Q_\mu^2=0$, the zero-divisor cone of the algebra, of complex dimension $3$ and real dimension $6$, smooth off the apex, which is its only singular point. It is ruled by two families of maximal totally isotropic planes, of complex dimension $2$, and the maximal totally isotropic dimension is $2$ over $\mathbb{C}$ and $4$ over the realified form of signature $(4,4)$. The realified form has index $4$ and the six restrictions have index $1$, $3$, $0$, $4$, $3$, $1$, with trivial defect throughout. The link of the cone is a compact real $5$-manifold, an $S^1$-bundle over the quadric surface $Q^2\cong S^2\times S^2$. On the six subspaces the cone has real dimension $0$, $4$, $0$, $0$, $3$, $3$; it is empty off the origin on the two definite subspaces, it is exactly the pure zero-divisor cone on the vector subspace, and it consists of non-pure zero divisors on the two real forms; the centre is anisotropic for $N$ although its realified restriction is indefinite. As a complex quadric the cone is equivalent to the null cone of the complex bilinear form, which is also a smooth complex cone of real dimension $6$; the two differ as real forms, and they meet exactly in the pure cone $\{Q_0=0,\sum_kQ_k^2=0\}$ of real dimension $4$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal N_{\natural}=\{\tilde Q:\sum_\mu Q_\mu^2=0\}$ | The null cone of the quaternion bilinear form |
| real dimension $6$ | Its dimension in $\mathbb B$; complex dimension $3$ |
| $\mathcal N_{\natural}\setminus\{0\}$ | The zero-divisor set of the algebra |
| $W_+=\mathbb{C}\{e_0+ie_1,e_2+ie_3\}$, $W_-=\mathbb{C}\{e_0+ie_1,e_2-ie_3\}$ | The two maximal totally isotropic planes, one from each ruling |
| index $4$ | The number of negative directions of the realified form on $\mathbb{R}^8$ |
| $0,4,0,0,3,3$ | The real dimension of the cone on the six subspaces |
| $\{Q_0=0,\sum_kQ_k^2=0\}$ | The intersection of the two complex cones; the pure cone |

## Further Reading

- *The Quaternion Bilinear Form on the Biquaternion Algebra* (`articles_maths/the-quaternion-bilinear-form-on-the-biquaternion-algebra.md`), for the form
- *Biquaternion Zero Divisors* (`articles_maths/biquaternion-zero-divisors.md`), for the classification of the isotropic elements
- *The Complex Bilinear Form on the Biquaternion Algebra* (`articles_maths/the-complex-bilinear-form-on-the-biquaternion-algebra.md`), for the companion cone of the sibling form, into which the isotropic-structure placeholder of that group was absorbed
- *The Six Subspaces under the Quaternion Bilinear Form* (`articles_maths/the-six-subspaces-under-the-quaternion-bilinear-form.md`), for the restriction matrices behind the dimension table
- *Biquaternion Topology* (`articles_maths/biquaternion-topology.md`), for the quadric surface and the rulings
