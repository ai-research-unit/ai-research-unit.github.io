
# __Involutions of the Projection Operators__

## Introduction

Every projection $P$ (an idempotent, the one-sided operator of *The Projection Operator*) determines an **involution** $\sigma_P = 2P - \mathrm{id}$, the reflection about the projection: it fixes the image of $P$ pointwise and negates the kernel, and the correspondence is a bijection between the projections and the involutions of the space. The article develops the projections of this Part together with the involution and the adjoint in the **operator built from the involution** layer: the projection is the one-sided operator, the involution it determines is the order-two operator, the adjoint is the one of the Hermitian structure, and the projective instances are the **perspectivities**, the central projections and the harmonic homologies of the projective space. The article proves the bijection and the compatibility of the involution with the adjoint.

The article develops the involution associated to a projection with the bijection between the projections and the involutions, the involution of the set of the projections given by the complement, the compatibility of the involution with the adjoint and the resulting characterisation of the orthogonal projections, the central projections and the perspectivities of the projective space with the harmonic homology, and the projective involutions with their fixed loci and the theorem of Baer. The article owns the involutions built from the projections.

The article assumes *The Projection Operator* for the idempotents, the centre of projection and the perspectivity; *Hermitian Structures and the Projection Operator* and *The Adjoint under a Hermitian Pairing* for the orthogonal projections and the adjoint; *Operators on a Projective Space* and *Projective Geometry* for the projectivities, the correlations and the frames; and *Involutive Bilinear Algebras* of Part I for the involutions and the decomposition of an algebra with an involution. No distance and no physics is invoked.

## The Involution Associated to a Projection

### The Construction

**Definition.** Let $P \in \operatorname{End}_K(V)$ be a projection, $P^2 = P$, and let $\mathrm{id}$ be the identity; the **involution associated to $P$** is

$$
\sigma_P = 2P - \mathrm{id} .
$$

**Theorem.** The map $\sigma_P$ is an involution of the vector space,

$$
\sigma_P^2 = \mathrm{id} ,
$$

and the correspondence $P \mapsto \sigma_P$ is a bijection between the projections of $V$ and the involutions of $V$ when $2$ is invertible in $K$; the inverse sends an involution $\sigma$ to the projection

$$
P_\sigma = \tfrac12(\sigma + \mathrm{id}) ,
$$

and the image of $\sigma_P$ is the $+1$-eigenspace of $\sigma_P$ and the kernel is the $-1$-eigenspace, so

$$
V = \operatorname{im} P \oplus \ker P , \qquad \sigma_P|_{\operatorname{im} P} = \mathrm{id}, \qquad \sigma_P|_{\ker P} = -\mathrm{id} .
$$

**Proof.** The square is $(2P - \mathrm{id})^2 = 4P^2 - 4P + \mathrm{id} = \mathrm{id}$ using $P^2 = P$; the map $\sigma \mapsto \tfrac12(\sigma+\mathrm{id})$ is inverse to $P \mapsto 2P - \mathrm{id}$ because $P \mapsto 2P-\mathrm{id} \mapsto \tfrac12(2P-\mathrm{id}+\mathrm{id}) = P$ and conversely; the eigenspace statement is the definition of the two eigenspaces of an involution and the decomposition of the space. The statement is in *Involutive Bilinear Algebras* and *The Projection Operator*.

**Corollary (the reflection).** A projection with a kernel of dimension one determines the reflection in the hyperplane of its image, and the reflections of the geometry are the involutions $\sigma_P$ of the projections with a one-dimensional kernel; the orthogonal reflection with respect to a form is the involution of the orthogonal projection $P_W$ of *Hermitian Structures and the Projection Operator*. The Cartan–Dieudonné theorem for the orthogonal group, in *Geodesic Reflection as an Operator*, is the statement that the orthogonal projections with the one-dimensional kernels generate the group.

**Proof.** The kernel of dimension one is a line, and the involution $\sigma_P$ fixes the hyperplane of the image pointwise and negates the line; the reflection of a form is the involution of the orthogonal projection onto the hyperplane, by the definition of the orthogonal projection. The statement is in *Hermitian Structures and the Projection Operator* and *Geodesic Reflection as an Operator*.

### The Eigenspaces and the Trace

**Proposition.** The trace of the involution $\sigma_P$ is $\operatorname{tr}\sigma_P = 2\operatorname{tr}P - \dim V$, the determinant is $(-1)^{\dim\ker P}$, and the two eigenspaces have the dimensions $\dim\operatorname{im}P$ and $\dim\ker P$; for the orthogonal projection of a Hermitian structure the involution is self-adjoint, $\sigma_P^{\dagger} = \sigma_P$, and its eigenvalues are $\pm1$.

**Proof.** The trace is linear, so $\operatorname{tr}\sigma_P = 2\operatorname{tr}P - \operatorname{tr}\mathrm{id}$, and $\operatorname{tr}P = \dim\operatorname{im}P$; the determinant is the product of the eigenvalues, which are $+1$ on the image and $-1$ on the kernel; the self-adjointness follows from $P^\dagger = P$ for the orthogonal projection. The statement is in *Hermitian Structures and the Projection Operator*.

## The Involution of the Set of the Projections

**Definition.** The **complementary projection** of $P$ is $\mathrm{id} - P$, the projection onto the kernel along the image; the map

$$
c : P \longmapsto \mathrm{id} - P
$$

is the **involution of the set of the projections**, and it satisfies $c^2 = \mathrm{id}$.

**Theorem.** The complementary map is an involution of the set of the projections exchanging the image and the kernel, $\operatorname{im}(\mathrm{id} - P) = \ker P$ and $\ker(\mathrm{id} - P) = \operatorname{im}P$; it reverses the order by the kernels, $P \leq P' \iff c(P') \leq c(P)$; it has no fixed point in characteristic not two, and it commutes with the involution of the previous section in the sense that $\sigma_{c(P)} = -\sigma_P$.

**Proof.** The complement of a projection is the projection along the image, which is immediate from the definitions; the image and the kernel are exchanged by inspection, and the order reversal is the exchange of the kernel and the image; a fixed point would need $P = \mathrm{id} - P$, that is, $2P = \mathrm{id}$, which is impossible because $\mathrm{id}/2$ is not idempotent unless $2 = 1$; the composite identity $\sigma_{c(P)} = 2(\mathrm{id}-P) - \mathrm{id} = \mathrm{id} - 2P = -\sigma_P$ is the definition. The statement is in *The Projection Operator*.

**Corollary (the two involutions and the transposition).** The involution $\sigma_P$ and the map $c$ generate the Klein four-group acting on the projections $\{P, \mathrm{id}-P, \sigma_P, \sigma_{c(P)}\}$; the passage from a projection to its adjoint, $P \mapsto P^\dagger$, is the third involution of the same elementary action, and the three are related by the identities above.

## The Adjoint and the Involutions

**Theorem.** The involution associated to a projection is compatible with the adjoint of the Hermitian structure: for the adjoint $P^{\dagger}$ of the projection $P$ with respect to $h$, the associated involution is the adjoint of the associated involution,

$$
\sigma_{P^{\dagger}} = (\sigma_P)^{\dagger} ,
$$

so the map $P \mapsto \sigma_P$ intertwines the adjoint on the projections with the adjoint on the involutions; consequently $\sigma_P$ is self-adjoint exactly when $P$ is an orthogonal projection, and the involutions coming from the orthogonal projections are the self-adjoint involutions of the Hermitian structure.

**Proof.** The adjoint is conjugate-linear and additive and it reverses the products, so $(2P - \mathrm{id})^\dagger = 2P^\dagger - \mathrm{id} = \sigma_{P^\dagger}$; the self-adjointness is the equivalence $P^\dagger = P \iff \sigma_P^\dagger = \sigma_P$, which is the characterisation of the orthogonal projection of *Hermitian Structures and the Projection Operator*. The statement is in *The Adjoint under a Hermitian Pairing* and *Hermitian Structures and the Projection Operator*.

**Remark (the involutions of the adjoint layer).** The article is the intersection of three structures: the projections of *The Projection Operator*, the adjoint of *The Adjoint under a Hermitian Pairing* and the involutions of *Involutive Bilinear Algebras*; the associated involution $\sigma_P$ is the one-sided operator built from the projection, the adjoint is the structure built from the involution on the elements, and their compatibility is the theorem above, proved and not assumed.

## The Central Projection and the Perspectivity

### The Central Projection

**Definition.** Let $U, W \subseteq V$ be complementary subspaces and let $\mathbb{P}(V)$ be the projective space of *The Projection Operator*; the **central projection** with centre $\mathbb{P}(U)$ onto $\mathbb{P}(W)$ is the map $\pi_U$, the projectivisation of the projection $P$ onto $W$ along $U$.

**Proposition.** The central projection is not an involution and not a collineation of the whole space: it is defined off the centre and it collapses each line through the centre to a point, so $\pi_U^2$ is defined only on the target and equals the identity there; the projection is one-sided, and the associated involution $\sigma_U$ of the previous section is the reflection that negates the centre and fixes the target. The involution associated to the central projection is defined on the whole space and is a linear involution, while the central projection itself is the rational map.

**Proof.** The square of the central projection is $\pi_U|_{\mathbb{P}(W)}$ extended by the collapse, which is the identity on the target and undefined on the centre; the associated involution $\sigma_U$ fixes $W$ and negates $U$ by the previous section. The statement is in *The Projection Operator*.

### The Perspectivity and the Harmonic Homology

**Definition.** A **perspectivity** is a projectivity between two figures of the same dimension with a common centre, the restriction of a central projection; a **homology** is a projectivity of the projective space fixing a hyperplane $\mathbb{P}(W)$ pointwise (the **axis**) and a point $\mathbb{P}(U)$ (the **centre**) not on it, and it is determined by the multiplier $\lambda$ on the pencil through the centre; an **elation** is the case in which the centre lies on the axis.

**Theorem.** The involutorial projectivities are the **harmonic homologies** (with the multiplier $\lambda = -1$) and the **harmonic elations**; the involution of a homology is the associated involution of the central projection with the centre and the axis, its fixed locus is the union of the axis and the centre, and the **harmonic homology** is the projective involution whose two fixed figures are complementary. The theorem of **Baer** states that the fixed locus of an involutorial projectivity in characteristic not two is the union of a subspace and a complementary subspace, and the harmonic homologies and the elations are exactly the projective involutions.

**Proof.** A homology fixes the axis pointwise and the centre, and it acts on each line through the centre by the multiplier; the square acts by $\lambda^2$, so the involution is the case $\lambda^2 = 1$, that is, $\lambda = \pm1$, and the case $\lambda = -1$ is the harmonic one; the fixed locus is the axis together with the centre, and the two are complementary. Baer's theorem computes the fixed locus of an involutorial projectivity in the general case. The statement is in *Projective Geometry* and *Operators on a Projective Space*.

**Corollary (the harmonic involution).** The harmonic involution of the projective line of *The Projection Operator* is the involution associated with the projection of the complete quadrangle: it is the perspectivity of the line with the two fixed points, and it is the boundary case of the harmonic homology in which the axis is a point and the centre is the complementary point. The involution of the projections and the harmonic conjugation are two readings of the same order-two operator, the linear and the projective one.

**Proof.** The harmonic involution fixes the two points and exchanges the two conjugates, and it is the case of Baer with the fixed locus a pair of points in the projective line; the construction by the complete quadrangle is the classical one, in *The Projection Operator* and *Projective Geometry*.

## Summary

A projection $P$ determines the **involution** $\sigma_P = 2P - \mathrm{id}$, fixing the image pointwise and negating the kernel, and the correspondence $P \leftrightarrow \sigma_P$ is a bijection between the projections and the involutions when $2$ is invertible; the reflections of a geometry are the involutions of the projections with a one-dimensional kernel, and the orthogonal reflections are those of the orthogonal projections. The map $c(P) = \mathrm{id} - P$ is an involution of the set of the projections exchanging the image and the kernel and reversing the order, and it satisfies $\sigma_{c(P)} = -\sigma_P$; the adjoint acts compatibly, $\sigma_{P^\dagger} = (\sigma_P)^\dagger$, so the associated involution is self-adjoint exactly when the projection is orthogonal. The central projection is not an involution, but it determines the linear involution $\sigma_U$ and the projective **perspectivity**, and the projective involutions are the harmonic homologies and the harmonic elations with the multiplier $\lambda = -1$; their fixed loci are the union of the axis and the centre, complementary figures in the sense of Baer, and the harmonic involution of the projective line is the boundary case. The involutions of the projections, the involutions of the projective geometry and the harmonic conjugation are three readings of the same order-two operator.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P^2 = P$ | Projection (idempotent) |
| $\sigma_P = 2P - \mathrm{id}$ | Involution associated to the projection |
| $P_\sigma = \tfrac12(\sigma + \mathrm{id})$ | Projection associated to an involution |
| $\operatorname{im} P$, $\ker P$ | Image and kernel, the $\pm1$-eigenspaces of $\sigma_P$ |
| $\operatorname{tr}\sigma_P = 2\operatorname{tr}P - \dim V$ | Trace of the involution |
| $c(P) = \mathrm{id} - P$ | Complementary projection, an involution of the set |
| $\sigma_{P^\dagger} = (\sigma_P)^\dagger$ | Compatibility of the involution with the adjoint |
| $\pi_U$ | Central projection with centre $\mathbb{P}(U)$ |
| perspectivity | Projectivity between two figures from a common centre |
| homology | Projectivity fixing a hyperplane and a point off it |
| $\lambda = -1$ | Harmonic homology, the involutorial case |
| elation | Homology with the centre on the axis |
| Baer's theorem | Fixed locus of an involutorial projectivity |

## Further Reading

- Paul R. Halmos, *Finite-Dimensional Vector Spaces*, 2nd ed. (Van Nostrand, 1958), for the projections, the involutions and the reflections.
- H. S. M. Coxeter, *Projective Geometry*, 2nd ed. (Springer, 2003), for the perspectivities, the homologies and the harmonic conjugation.
- Reinhold Baer, *Linear Algebra and Projective Geometry* (Academic Press, 1952), for the involutorial collineations and the fixed loci.
- Pierre Samuel, *Projective Geometry* (Springer, 1988), for the projective transformations and the central projections.
- Bertram Huppert, *Endliche Gruppen I* (Springer, 1967), for the involutions and the products of the involutions in the classical groups.
