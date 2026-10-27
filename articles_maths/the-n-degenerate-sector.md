# __The N-Degenerate Sector__

## Introduction

The quaternionic norm $\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2$ is the one multiplicative norm of the biquaternion algebra. Its zero set is the **$\natural$-degenerate sector**,

$$
\mathcal{N}=\{\tilde Q\in\mathbb{B}:\langle\tilde Q\rangle_{\natural}=0\},
$$

the **null cone**. It contains the origin at its apex and the zero divisors at its punctured points. This article studies the sector as a set: its characterisation, its three strata, its geometry and link, its matrix picture, its multiplicative structure, the degeneration of the polar decomposition on it, and the way the spectral condition sits inside it. Its partner is *The N-Regular Sector*, the group of units.

The cone is split by the scalar part into two strata, the **pure** stratum of nilpotents and the **non-pure** stratum of complex multiples of idempotents. On the cone this split coincides exactly with the spectral split: the pure stratum, with the origin adjoined, is the doubly degenerate cell $\Sigma_{00}$, and the non-pure stratum is the norm-degenerate, spectrally regular cell $\Sigma_{01}$. That coincidence is special to the cone and is the main structural link between the norm partition and the spectral partition.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ on the basis $e_t,\vec e_x,\vec e_y,\vec e_z$, of complex dimension four and real dimension eight, with $\vec e_x\vec e_y=\vec e_z$ and $\vec e_k^2=-e_t$. An element is $\tilde Q=Q_te_t+\vec Q$ with $Q_\mu\in\mathbb{C}$ and $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$. The natural conjugation is $\tilde Q^{\natural}=Q_t-\vec Q$ and the Hermitian conjugation is $\tilde Q^{*}=\overline{Q_t}-\overline{\vec Q}$. The **quaternionic norm** is

$$
\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2,\qquad B^2=Q_x^2+Q_y^2+Q_z^2,
$$

a complex scalar; it is multiplicative. The **spectral-degenerate cone** is $\mathcal{S}=\{B^2=0\}$. The product is the plain product, with unit $e_t$. A **sector** is one of the two halves selected by the norm; a **cell** is one of the four intersections $\Sigma_{ij}$ selected by the norm and the spectrum together. The **pure stratum** is written $\mathcal{N}_{\mathrm{p}}$ and the **non-pure stratum** $\mathcal{N}_{\mathrm{np}}$.

## Definition and Characterisation

**Definition.** The **$\natural$-degenerate sector** is the null cone

$$
\mathcal{N}=\{\tilde Q:\langle\tilde Q\rangle_{\natural}=0\},
$$

and the **zero-divisor set** is its punctured part $\mathcal{Z}=\mathcal{N}\setminus\{0\}$.

**Theorem (the criterion).** For $\tilde Q\in\mathbb{B}$ the following are equivalent:

(i) $\langle\tilde Q\rangle_{\natural}=0$;

(ii) $\det\mathsf{M}_2(\tilde Q)=0$;

(iii) $\tilde Q$ is not invertible;

(iv) $\tilde Q\tilde Q^{\natural}=0$;

(v) the left translation $L_{\tilde Q}$ is not bijective;

(vi) the right translation $R_{\tilde Q}$ is not bijective.

For $\tilde Q\neq0$ they are also equivalent to:

(vii) $\tilde Q$ is a zero divisor;

(viii) $L_{\tilde Q}$ has complex rank $2$;

(ix) $\mathsf{M}_2(\tilde Q)$ has rank $1$.

*Proof.* (i)$\iff$(iv) is the identity $\tilde Q\tilde Q^{\natural}=\langle\tilde Q\rangle_{\natural}e_t$. (i)$\iff$(ii) is the matrix picture, where the determinant is the norm. (ii)$\iff$(iii) is the determinant criterion for invertibility. (iii)$\iff$(v),(vi): an element is invertible exactly when its left and right translations are bijective. (vii) is the zero-divisor criterion of *N-Regularity and N-Degeneracy in the Biquaternion Algebra*, §*The $\natural$-degenerate case: the origin together with the zero divisors*. For (viii) and (ix), a non-zero singular $2\times2$ matrix has rank one, and the left translation has complex rank twice the rank of the matrix.

**Theorem (the cone is a complex hypersurface).** The cone is a complex algebraic cone of complex dimension three and real dimension six, defined by one complex equation, hence by two real equations. It is closed, of empty interior, irreducible, and of real codimension two.

*Proof.* The norm is a non-degenerate quadratic form in four complex variables, hence irreducible over $\mathbb{C}$ and not the zero polynomial. Its zero set is a hypersurface of complex dimension three; one complex equation is two real equations, so the real codimension is two. A proper algebraic subset has empty interior.

**Theorem (the cone is a semigroup ideal).** For all $\tilde P,\tilde Q$,

$$
\langle\tilde P\tilde Q\rangle_{\natural}=\langle\tilde P\rangle_{\natural}\langle\tilde Q\rangle_{\natural}.
$$

Hence if either factor lies in $\mathcal{N}$, so does the product. The cone is closed under multiplication on the left and on the right by any element of the algebra:

$$
\mathbb{B}\mathcal{N}\subseteq\mathcal{N},\qquad
\mathcal{N}\mathbb{B}\subseteq\mathcal{N}.
$$

*Proof.* Multiplicativity is the multiplicativity of the norm; if one factor has norm zero, the product has norm zero.

**Remark (not a subspace).** The cone is not closed under addition. The elements $\vec e_x+i\vec e_y$ and $\vec e_x-i\vec e_y$ are null, and their sum $2\vec e_x$ has norm $4$. The cone is a cone over a nonlinear base, not a linear subspace.

**Remark (not an additive ideal).** The cone is a two-sided ideal of the multiplicative semigroup, not of the ring: an ideal of the ring must be an additive subgroup, and the cone is not one. The algebra is simple, so it has no non-trivial additive two-sided ideals; the cone is the multiplicative shadow of the determinant.

## The Three Strata

**Definition.** The **pure stratum**, the **non-pure stratum**, and the **apex** are

$$
\mathcal{N}_{\mathrm{p}}=\{\tilde Q\in\mathcal{N}:Q_t=0,\ \tilde Q\neq0\},\qquad
\mathcal{N}_{\mathrm{np}}=\{\tilde Q\in\mathcal{N}:Q_t\neq0\},\qquad
\{0\}.
$$

**Theorem (the trichotomy).** The cone is the disjoint union

$$
\mathcal{N}=\{0\}\uplus\mathcal{N}_{\mathrm{p}}\uplus\mathcal{N}_{\mathrm{np}}.
$$

For $\tilde Q\neq0$ on the cone, the following are equivalent:

(i) $Q_t=0$;

(ii) $\tilde Q^2=0$;

(iii) $\tilde Q$ lies in the pure stratum.

They are also equivalent to $B^2=0$. The negations are equivalent: $Q_t\neq0$, $\tilde Q^2\neq0$, $B^2\neq0$, and $\tilde Q$ lies in the non-pure stratum. On the cone one always has $\tilde Q^2=2Q_t\tilde Q$, and the two sides are non-zero exactly in this case.

*Proof.* On the cone, $Q_t^2+B^2=0$, so $Q_t^2-B^2=2Q_t^2$ and

$$
\tilde Q^2=(Q_t^2-B^2)e_t+2Q_t\vec Q=2Q_t\tilde Q.
$$

If $Q_t=0$ then $\tilde Q^2=0$ and $B^2=0$. If $\tilde Q^2=0$ and $\tilde Q\neq0$, then $2Q_t\tilde Q=0$, so $Q_t=0$. If $B^2=0$ then $Q_t^2=0$, so $Q_t=0$. The equivalences follow.

**Theorem (the pure stratum).** On the pure stratum every element is a nilpotent of index two: $\tilde Q=\vec Q$, $\vec Q^2=0$, $\tilde Q^2=0$, and $\tilde Q\neq0$. The stratum is a complex cone of complex dimension two and real dimension four, smooth off the origin. In the matrix model it is the set of non-zero nilpotent matrices of rank one.

*Proof.* The description is the definition together with the equivalence above. The equation $\vec Q^2=0$ is one non-degenerate quadratic equation in the three vector coefficients, with gradient $2\vec Q\neq0$ off the origin, so the punctured set is a smooth complex surface. A non-zero matrix with square zero and rank one is nilpotent of index two.

**Theorem (the non-pure stratum).** Every element of the non-pure stratum is uniquely

$$
\tilde Q=c\,\tilde\Pi,\qquad c=2Q_t\neq0,
$$

where $\tilde\Pi$ is a non-trivial idempotent, $\tilde\Pi^2=\tilde\Pi$, $\tilde\Pi\neq0,e_t$. The idempotent is $\tilde\Pi=\tilde Q/(2Q_t)$ and has scalar part $1/2$. The stratum is open and dense in the punctured cone, of complex dimension three and real dimension six.

*Proof.* Put $\tilde\Pi=\tilde Q/(2Q_t)$. On the cone $\tilde Q^2=2Q_t\tilde Q$, hence

$$
\tilde\Pi^2=\frac{\tilde Q^2}{4Q_t^2}=\frac{2Q_t\tilde Q}{4Q_t^2}=\frac{\tilde Q}{2Q_t}=\tilde\Pi.
$$

The idempotent is neither $0$ nor $e_t$: $\tilde\Pi=0$ gives $\tilde Q=0$, and $\tilde\Pi=e_t$ gives $\tilde Q=2Q_te_t$, of norm $4Q_t^2\neq0$. The scalar part is $Q_t/(2Q_t)=1/2$. The map $\tilde Q\mapsto\tilde\Pi$ is continuous with fibre $\mathbb{C}^{\times}\tilde\Pi$, and the condition $Q_t\neq0$ is open in the cone and its complement is the pure stratum of lower dimension, so the stratum is open and dense.

**Corollary (the two dimensions).** The pure stratum has real dimension four and the non-pure stratum real dimension six; the pure stratum is of real codimension two in the punctured cone.

**Remark (the idempotent surface).** The non-trivial idempotents form a complex surface of complex dimension two and real dimension four; they are exactly the rank-one idempotents. The map $\mathcal{N}_{\mathrm{np}}\to\{\tilde\Pi\}$ is a principal $\mathbb{C}^{\times}$-bundle, the fibre over $\tilde\Pi$ being the punctured complex line $\mathbb{C}^{\times}\tilde\Pi$. A non-trivial idempotent is determined by its image line and its kernel line, two distinct complex lines; the surface is therefore $\mathbb{P}^1\times\mathbb{P}^1$ minus the diagonal. Its structure is *The Peirce Decomposition*, §*Idempotents and Orthogonal Idempotents*.

**Remark (the standard idempotents).** The elements

$$
\tilde\Pi_+=\frac{1}{2}(e_t+i\vec e_z),\qquad
\tilde\Pi_-=\frac{1}{2}(e_t-i\vec e_z)
$$

are orthogonal idempotents, $\tilde\Pi_+^2=\tilde\Pi_+$, $\tilde\Pi_-^2=\tilde\Pi_-$, $\tilde\Pi_+\tilde\Pi_-=\tilde\Pi_-\tilde\Pi_+=0$, and $\tilde\Pi_++\tilde\Pi_-=e_t$. They map to $\mathrm{diag}(1,0)$ and $\mathrm{diag}(0,1)$ respectively in the matrix model.

**Theorem (the similarity classes).** Under conjugation by $\mathbb{B}^{\times}$, the punctured cone has exactly the following orbits: the pure stratum is one orbit, and for each $c\in\mathbb{C}^{\times}$ the set $c\{\tilde\Pi\}$ of non-trivial idempotent multiples is one orbit. The invariant that separates them is the scalar part $Q_t$.

*Proof.* Two elements are conjugate exactly when they have the same Jordan form. A non-zero nilpotent of index two in dimension two has the single Jordan form $\begin{pmatrix}0&1\\0&0\end{pmatrix}$. A non-trivial idempotent has eigenvalues $1,0$ and is diagonalisable, so all non-trivial idempotents are conjugate; multiplying by $c$ scales the eigenvalues to $c,0$, and the scalar $c$ is preserved by conjugation. The scalar part is $c/2$.

## Geometry

**Theorem (the cone and its apex).** The cone is a complex cone of real dimension six, invariant under every complex scalar. It is smooth off the origin, and the origin is its only singular point. It is contractible.

*Proof.* The norm is homogeneous, $\langle\lambda\tilde Q\rangle_{\natural}=\lambda^2\langle\tilde Q\rangle_{\natural}$, so the zero set is a cone. Its gradient is $2(Q_t,Q_x,Q_y,Q_z)$, which vanishes only at the origin; off the apex the cone is a smooth complex three-fold. The straight-line homotopy $\tilde Q\mapsto(1-s)\tilde Q$ contracts it to the apex.

**Theorem (the link).** The link

$$
L=\mathcal{N}\cap S^7_E
$$

is a closed connected real five-manifold, and

$$
L\cong S^2\times S^3\cong V_2(\mathbb{R}^4).
$$

Its homotopy groups are $\pi_1(L)=0$, $\pi_2(L)\cong\mathbb{Z}$ and $\pi_3(L)\cong\mathbb{Z}\oplus\mathbb{Z}$. In particular $L$ is not a five-sphere, so the apex is a genuine topological singularity.

*Proof.* The identification and the homotopy groups are *The Topology of the Zero-Divisor Cone*, §*The Link Is $S^{2}\times S^{3}$*. If the cone were a topological manifold at the apex, its link would be $S^5$; the link has $\pi_2\cong\mathbb{Z}$, while $\pi_2(S^5)=0$.

**Theorem (the projectivised cone).** The quotient of the punctured cone by the complex scalars is the smooth quadric surface

$$
\mathbb{P}(\mathcal{N})\cong\mathbb{P}^1\times\mathbb{P}^1,
$$

whose underlying real manifold is $S^2\times S^2$, and the punctured cone is a $\mathbb{C}^{\times}$-bundle over it. The link is a circle bundle over the quadric.

*Proof.* The projective quadric of a non-degenerate quadratic form in four variables is smooth of dimension two, and over $\mathbb{C}$ it is $\mathbb{P}^1\times\mathbb{P}^1$; the real picture is $S^2\times S^2$. The bundle statements are the definitions of the projectivisation and of the link.

**Theorem (homogeneity under isometries).** The special orthogonal group $\mathrm{SO}(4,\mathbb{C})$ of the norm acts transitively on $\mathcal{N}\setminus\{0\}$. The punctured cone is a single orbit; every invariant of the isometry group is constant on it.

*Proof.* Two non-zero isotropic vectors of a non-degenerate quadratic form are carried one to the other by an isometry, by Witt's theorem; the isometry may be taken of determinant one because a reflection in a non-isotropic vector orthogonal to the target has determinant minus one and fixes the target. The norm is invariant and equal to zero.

**Remark (the two readings of homogeneity).** Under the isometry group the cone is one orbit. Under conjugation by the units it is not: the similarity classes are the pure stratum and the idempotent multiples $c\tilde\Pi$, separated by $Q_t$. The isometry group is much larger than the similarity group, and the two statements are compatible. The first says that the metric structure of the cone carries no invariant beyond the value zero; the second says that the algebraic structure carries the scalar part.

**Remark (not convex, not pointed).** The null elements $\vec e_x+i\vec e_y$ and $\vec e_x-i\vec e_y$ have the midpoint $\vec e_x$, of norm $1$, so the cone is not convex. It contains the whole complex line through each of its points, so it is not pointed.

## The Matrix Picture

**Theorem (rank one).** For $\tilde Q\neq0$ on the cone the matrix model is a rank-one matrix

$$
\mathsf{M}_2(\tilde Q)=uv^{\mathsf{T}},
$$

with $u,v\in\mathbb{C}^2\setminus\{0\}$, unique up to $(u,v)\mapsto(\lambda u,\lambda^{-1}v)$ for $\lambda\in\mathbb{C}^{\times}$. The scalar part is the contraction

$$
Q_t=\frac{1}{2}v^{\mathsf{T}}u,
$$

and the two strata are

$$
\mathcal{N}_{\mathrm{p}}=\{v^{\mathsf{T}}u=0\},\qquad
\mathcal{N}_{\mathrm{np}}=\{v^{\mathsf{T}}u\neq0\}.
$$

On the non-pure stratum the idempotent is

$$
\tilde\Pi=\frac{uv^{\mathsf{T}}}{v^{\mathsf{T}}u}.
$$

*Proof.* A non-zero singular $2\times2$ matrix has rank one, hence is $uv^{\mathsf{T}}$; the pair is determined up to the scaling that leaves the product unchanged. The trace of $uv^{\mathsf{T}}$ is $v^{\mathsf{T}}u$, and the trace of $\mathsf{M}_2(\tilde Q)$ is $2Q_t$. The square is $(uv^{\mathsf{T}})^2=(v^{\mathsf{T}}u)uv^{\mathsf{T}}$, so it vanishes exactly when $v^{\mathsf{T}}u=0$, and the idempotent formula follows by dividing by the contraction.

**Theorem (the annihilators).** For $\tilde Q\neq0$ on the cone, in the matrix model the left and right annihilators are complex planes:

$$
\{X:\tilde QX=0\}=\{X:v^{\mathsf{T}}X=0\},\qquad
\{X:X\tilde Q=0\}=\{X:Xu=0\}.
$$

The left translation has complex rank two, kernel the left annihilator and image $\{uw^{\mathsf{T}}:w\in\mathbb{C}^2\}$. The right translation has complex rank two, kernel the right annihilator and image $\{wv^{\mathsf{T}}:w\in\mathbb{C}^2\}$.

*Proof.* Left multiplication by $uv^{\mathsf{T}}$ is $X\mapsto u(v^{\mathsf{T}}X)$; its kernel is the two linear conditions $v^{\mathsf{T}}X=0$ and its image is $\{uw^{\mathsf{T}}:w\in\mathbb{C}^{2}\}$. The right-hand statement is the transpose, with the kernel $Xu=0$ and the image $\{wv^{\mathsf{T}}:w\in\mathbb{C}^{2}\}$.

**Remark (the Peirce corners).** For a non-pure element, the idempotent $\tilde\Pi$ gives the Peirce decomposition

$$
\mathbb{B}=\mathbb{B}_{11}\oplus\mathbb{B}_{10}\oplus\mathbb{B}_{01}\oplus\mathbb{B}_{00},
\qquad
\mathbb{B}_{ij}=\tilde\Pi_i\mathbb{B}\tilde\Pi_j,
$$

with $\tilde\Pi_1=\tilde\Pi$ and $\tilde\Pi_0=e_t-\tilde\Pi$. For a rank-one idempotent each corner is a complex line. The kernel of $L_{\tilde Q}$ is $\mathbb{B}_{01}\oplus\mathbb{B}_{00}$ and its image is $\mathbb{B}_{11}\oplus\mathbb{B}_{10}$; the kernel of $R_{\tilde Q}$ is $\mathbb{B}_{10}\oplus\mathbb{B}_{00}$ and its image is $\mathbb{B}_{11}\oplus\mathbb{B}_{01}$. The general Peirce theory is *The Peirce Decomposition*, §*The Peirce Decompositions*.

**Remark (the determinantal variety).** The cone is the determinantal variety of rank at most one,

$$
\mathcal{N}=\{\tilde Q:\operatorname{rank}\mathsf{M}_2(\tilde Q)\le1\},
$$

and the apex is its rank-zero locus. The two strata are the rank-one locus split by the contraction $v^{\mathsf{T}}u$, which is the trace: the pure stratum is the nilpotent part and the non-pure stratum the idempotent part.

## Multiplication and Inversion

**Theorem (the semigroup).** The cone is a subsemigroup without identity of the multiplicative semigroup of the algebra, and it is a two-sided ideal of that semigroup. The product of two non-zero null elements can be zero and can be non-zero.

*Proof.* Closure is the multiplicativity of the norm. The identity $e_t$ is not null, so there is no identity. For the two behaviours, $\tilde\Pi_+\tilde\Pi_-=0$ and $\tilde\Pi_+\tilde\Pi_+=\tilde\Pi_+\neq0$.

**Remark (the pure product).** For a pure element $\nu$, $\nu^{\natural}=-\nu$ and $\nu\nu^{\natural}=-\nu^2=0$. The conjugate of a pure null element is a pure null element, and their product is zero. The pure stratum therefore contains many pairs of orthogonal elements.

**Theorem (no inverses).** No element of the cone is invertible. The equations $\tilde Q\tilde X=e_t$ and $\tilde X\tilde Q=e_t$ have no solution in $\mathbb{B}$.

*Proof.* An invertible element has non-zero norm, and the norm is multiplicative with $\langle e_t\rangle_{\natural}=1$. The one-sided equations would make $\tilde Q$ invertible.

**Remark (the cone is stable under similarity).** For $\tilde P\in\mathbb{B}^{\times}$ and $\tilde Q\in\mathcal{N}$,

$$
\langle\tilde P\tilde Q\tilde P^{-1}\rangle_{\natural}=\langle\tilde Q\rangle_{\natural}=0,
$$

so the cone is invariant under conjugation by the units. The similarity classes inside it are the pure stratum and the idempotent multiples, as in §*The Three Strata*.

**Remark (the product with a unit).** A product of a null element and a unit is null by multiplicativity, and it can be zero or non-zero. In the matrix picture, multiplying a rank-one matrix by an invertible matrix on either side keeps the rank one; the result is zero exactly when the images and kernels align.

## The Polar Decomposition on the Cone

**Theorem (the two factors).** Every element of the cone has a unique polar decomposition

$$
\tilde Q=\tilde Q_H\tilde Q_0,
\qquad
\tilde Q_H=(\tilde Q\tilde Q^{*})^{1/2},\qquad
\tilde Q_0=\tilde Q_H^{+}\tilde Q,
$$

with $\tilde Q_H$ Hermitian positive semidefinite and $\tilde Q_0$ a partial isometry. For $\tilde Q\neq0$, $\tilde Q_H$ has rank one, $\tilde Q_0$ is not unitary, and its final projection is a rank-one projection. At the origin both factors vanish.

*Proof.* The existence and uniqueness are *The Polar Decomposition of a Biquaternion*, §*Uniqueness*; the rank and partial-isometry statements are *The Polar Decomposition of a N-Degenerate Biquaternion*, §*The Two-Factor Decomposition*.

**Theorem (the Hermitian factor).** For $\tilde Q\neq0$ on the cone, write $\tilde Q\tilde Q^{*}=\langle\tilde Q\rangle_{*}e_t+i\vec W$ with $\vec W$ real and put

$$
a=\sqrt{\frac{\langle\tilde Q\rangle_{*}}{2}},
\qquad
\tilde Q_H=a\,e_t+\frac{i}{2a}\,\vec W .
$$

Then $\tilde Q_H^2=\tilde Q\tilde Q^{*}$, $\tilde Q_H$ is positive semidefinite of rank one, and its spectrum is $\{0,2a\}$. The scalar part of $\tilde Q_H$ is $a$ and its vector part has length $a$.

*Proof.* This is *The Polar Decomposition of a N-Degenerate Biquaternion*, §*The Hermitian Factor*, where the identities $\lvert\vec W\rvert=\langle\tilde Q\rangle_{*}$ and $\lvert\vec W\rvert=2a^2$ are proved; the spectrum follows from $\tilde Q_H^2=2a^2e_t+i\vec W$.

**Remark (what degenerates).** On the sector the Hermitian factor is positive definite and the isometry factor is unitary. On the cone the Hermitian factor drops to rank one and the isometry factor to a partial isometry; the two projections are rank-one and no longer the identity. The Hermitian factor is the continuous limit of the regular one; the isometry factor is not continuous at the cone.

**Remark (the matrix reading).** Under $\mathsf{M}_2$ the factor $\tilde Q_H$ is the positive semidefinite square root of $MM^{\dagger}$ and $\tilde Q_0$ is the isometry factor of the matrix polar decomposition, a partial isometry with rank-one initial and final projections. The matrix decomposition exists for every matrix and is unique; on the cone it is the degenerate case.

## Relation to the Spectral Partition

**Theorem (the cone meets two cells).** The cone is the disjoint union of the two cells

$$
\mathcal{N}=\Sigma_{01}\uplus\Sigma_{00},
\qquad
\Sigma_{01}=\{N=0,\ B^2\neq0\},\qquad
\Sigma_{00}=\{N=0,\ B^2=0\}.
$$

The other two cells are disjoint from the cone: $\Sigma_{11}\cap\mathcal{N}=\Sigma_{10}\cap\mathcal{N}=\varnothing$. Moreover

$$
\Sigma_{01}=\mathcal{N}_{\mathrm{np}},\qquad
\Sigma_{00}=\mathcal{N}_{\mathrm{p}}\cup\{0\}.
$$

*Proof.* On the cone $Q_t^2=-B^2$. Hence $Q_t=0$ exactly when $B^2=0$, and $Q_t\neq0$ exactly when $B^2\neq0$. The identification with the strata is the trichotomy of §*The Three Strata*.

**Corollary (the algebraic and spectral splits coincide).** On the cone the split by the scalar part and the split by the square of the vector part are the same split. The two conditions cut the same partition there, although neither implies the other off the cone.

*Proof.* The two equivalences above. Off the cone the two conditions are independent: $e_t$ has $Q_t=1$ and $B^2=0$, while $\vec e_x$ has $Q_t=0$ and $B^2=1$.

**Theorem (the spectrum on the cone).** On $\Sigma_{01}$ the eigenvalues are $2Q_t\neq0$ and $0$, and the element is the idempotent multiple $2Q_t\tilde\Pi$. On $\Sigma_{00}$ the only eigenvalue is $0$, and the element is the origin or a non-zero nilpotent. In both cases $0$ is an eigenvalue.

*Proof.* The eigenvalues are $\lambda_\pm=Q_t\pm iB$. On the cone $\lambda_+\lambda_-=N=0$, so one of them is zero; if $B^2\neq0$ then $Q_t\neq0$ and the other is $2Q_t$; if $B^2=0$ then $Q_t=0$ and both vanish.

**Corollary (the norm is the product of the eigenvalues).** For every biquaternion $\langle\tilde Q\rangle_{\natural}=\lambda_+\lambda_-$. The cone is exactly the set on which at least one eigenvalue vanishes.

*Proof.* The characteristic polynomial is $X^2-2Q_tX+N$, whose roots are $\lambda_\pm$; their product is $\langle\tilde Q\rangle_{\natural}$.

**Remark (what the cone is not).** The cone is neither of the two simpler sets. It is not the spectral-degenerate cone $\mathcal{S}=\{B^2=0\}$, which contains the unit $e_t$; and it is not the hyperplane $\{Q_t=0\}$, which contains the unit $\vec e_x$. It is the single complex equation that ties the two coefficients together, $Q_t^2+B^2=0$.

## Comparison with the N-Regular Sector

The two sectors are complementary, and the comparison is the content of the norm partition.

| | $\mathcal{N}$, the $\natural$-degenerate sector | $\mathbb{B}^{\times}$, the $\natural$-regular sector |
|---|---|---|
| condition | $\langle\tilde Q\rangle_{\natural}=0$ | $\langle\tilde Q\rangle_{\natural}\neq0$ |
| real dimension | $6$ | $8$ |
| topology | closed cone, contractible, singular at the apex | open and dense, connected, $\simeq S^1\times S^3$ |
| multiplication | semigroup with absorbing $0$, no identity | group |
| inverse | none | two-sided |
| matrix model | rank at most $1$ | invertible, rank $2$ |
| polar factors | $\tilde Q_H$ of rank one, $\tilde Q_0$ a partial isometry | $\tilde Q_H$ positive definite, $\tilde Q_0$ unitary |
| spectrum | $0$ is an eigenvalue | $\lambda_\pm\neq0$ |
| boundary | the boundary of the sector | $\partial\mathbb{B}^{\times}=\mathcal{N}$ |

**Theorem (the boundary).** The cone is the boundary of the group of units, and it has empty interior:

$$
\partial\mathbb{B}^{\times}=\mathcal{N},\qquad
\operatorname{int}\mathcal{N}=\varnothing.
$$

*Proof.* The group is open and dense, and its complement is the cone.

**Remark (the two halves of the algebra).** The partition is by the value of one multiplicative invariant. The cone is the closed half; the group is the open half. The cone is not a group, but it is a semigroup ideal, and the product of any element with a null element stays null.

## Consequences

The cone is a complex algebraic hypersurface, of complex dimension three and real dimension six, smooth off its apex, with link $S^2\times S^3$ and projectivisation $S^2\times S^2$. It is contractible, and its apex is its only singular point.

It is the determinantal variety of rank at most one. Its non-zero elements are the rank-one matrices; the pure stratum is the nilpotent part and the non-pure stratum the idempotent part. The three strata have real dimensions zero, four and six, and the non-pure stratum is open and dense in the punctured cone.

The cone is a semigroup ideal, not a group. It contains no inverse, and the polar decomposition degenerates on it to a rank-one Hermitian factor and a partial isometry.

The spectral condition does not refine the cone into four cells: it meets only two of them, and on the cone the algebraic split and the spectral split coincide. The pure stratum, with the origin adjoined, is the doubly degenerate cell $\Sigma_{00}$, and the non-pure stratum is the norm-degenerate, spectrally regular cell $\Sigma_{01}$. The detailed study of those cells is *The N-Degenerate, Spectrally Degenerate Sector* and *The N-Degenerate, Spectrally Regular Sector*.

The cone is the boundary of the group of units. The two articles together carry the norm partition: this one the zero half, *The N-Regular Sector* the invertible half.

## Summary

The $\natural$-degenerate sector is the null cone $\mathcal{N}=\{N=0\}$, the zero set of the quaternionic norm. It is a complex algebraic cone of complex dimension three and real dimension six, closed, of empty interior, contractible, smooth off its apex, with link $S^2\times S^3$ and projectivisation $S^2\times S^2$.

It is the determinantal variety of rank at most one. The origin is the apex and the only singular point; the punctured cone is the zero-divisor set. The cone is a two-sided ideal of the multiplicative semigroup and contains no invertible element.

The cone splits into the origin, the pure stratum of nilpotents of index two, and the non-pure stratum of complex multiples of non-trivial idempotents. The three have real dimensions zero, four and six; the non-pure stratum is open and dense in the punctured cone. Under similarity the pure stratum is one orbit and each idempotent multiple family $c\tilde\Pi$ is one orbit, separated by the scalar part $Q_t$.

On the cone the algebraic split by $Q_t$ and the spectral split by $B^2$ coincide: the pure stratum, with the origin adjoined, is the doubly degenerate cell $\Sigma_{00}$, and the non-pure stratum is the cell $\Sigma_{01}$. The cone meets neither $\Sigma_{11}$ nor $\Sigma_{10}$. The norm is the product of the eigenvalues, and the cone is exactly the set on which at least one eigenvalue vanishes.

The polar decomposition survives on the cone in degenerate form: the Hermitian factor has rank one and the isometry factor is a partial isometry. The cone is the boundary of the group of units, and the two articles together carry the norm partition.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra, complex dimension four, real dimension eight |
| $\tilde Q=Q_te_t+\vec Q$ | an element and its scalar–vector split |
| $\tilde Q^{\natural}=Q_t-\vec Q$ | the natural conjugation |
| $\tilde Q^{*}=\overline{Q_t}-\overline{\vec Q}$ | the Hermitian conjugation |
| $\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2$ | the quaternionic norm |
| $B^2=Q_x^2+Q_y^2+Q_z^2$ | the square of the vector part |
| $\mathcal{N}=\{N=0\}$ | the null cone, the $\natural$-degenerate sector |
| $\mathcal{Z}=\mathcal{N}\setminus\{0\}$ | the zero-divisor set |
| $\mathcal{N}_{\mathrm{p}}=\{Q_t=0,\ \vec Q^2=0,\ \tilde Q\neq0\}$ | the pure stratum, nilpotents of index two |
| $\mathcal{N}_{\mathrm{np}}=\{Q_t\neq0\}$ | the non-pure stratum, idempotent multiples |
| $\mathcal{S}=\{B^2=0\}$ | the spectral-degenerate cone |
| $\Sigma_{01}=\{N=0,\ B^2\neq0\}$ | the norm-degenerate, spectrally regular cell |
| $\Sigma_{00}=\{N=0,\ B^2=0\}$ | the doubly degenerate cell |
| $\tilde\Pi=\tilde Q/(2Q_t)$ | the idempotent of a non-pure element |
| $\tilde\Pi_\pm=\frac{1}{2}(e_t\pm i\vec e_z)$ | the standard orthogonal idempotents |
| $\mathsf{M}_2(\tilde Q)=uv^{\mathsf{T}}$ | the rank-one matrix model |
| $Q_t=\frac{1}{2}v^{\mathsf{T}}u$ | the scalar part as a contraction |
| $\tilde Q=\tilde Q_H\tilde Q_0$ | the polar decomposition; $\tilde Q_H$ of rank one, $\tilde Q_0$ a partial isometry |
| $L=\mathcal{N}\cap S^7_E$ | the link, $L\cong S^2\times S^3$ |

## Further Reading

- [N-Regularity and N-Degeneracy in the Biquaternion Algebra](n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the norm, the criterion, the zero divisors and the two strata
- [The N-Regular Sector](the-n-regular-sector.html), for the partner article and the group of units
- [The Polar Decomposition of a N-Degenerate Biquaternion](the-polar-decomposition-of-an-n-degenerate-biquaternion.html), for the two factors and the Hermitian factor on the cone
- [The N-Degenerate, Spectrally Regular Sector](the-n-degenerate-spectrally-regular-sector.html), for the non-pure stratum as a cell
- [The N-Degenerate, Spectrally Degenerate Sector](the-n-degenerate-spectrally-degenerate-sector.html), for the pure stratum as a cell
- [Relations between the N Norm and Spectral Regularity and Degeneracy](relations-between-quaternionic-norm-and-spectral-regularity-and-degeneracy.html), for the four cells and the chain of invariants
- [The Topology of the Zero-Divisor Cone](the-topology-of-the-zero-divisor-cone.html), for the link, the projectivisation and the singularity
- [The Peirce Decomposition](ideals-peirce-decompositions-and-spinors-in-the-biquaternion-algebra.html), for the idempotents and the Peirce corners
- [Square Roots of Zero and the Nilpotents of the Biquaternion Algebra](square-roots-of-zero-and-the-nilpotents-of-the-biquaternion-algebra.html), for the pure stratum
- [$M_2(\mathbb{C})$ Representation : Rank-One Matrices and the Determinantal Variety](m2c-representation-rank-one-matrices-and-the-determinantal-variety.html), for the rank-one matrices and the determinant
- [The Biquaternion Unit Group as a Topological Group](the-biquaternion-unit-group-as-a-topological-group.html), for the complement of the cone
- S. J. Sangwine and D. Alfsmann, "Determination of the biquaternion divisors of zero, including the idempotents and nilpotents", *Advances in Applied Clifford Algebras* **20** (2010) 401--416.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995).
