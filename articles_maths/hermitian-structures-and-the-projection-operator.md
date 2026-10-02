
# __Hermitian Structures and the Projection Operator__

## Introduction

A **Hermitian structure** on a projective space is a nondegenerate Hermitian pairing, and among the projections of the space it singles out the **orthogonal projections** $P$: the projections with $P^2 = P = P^{\dagger}$, that is, the idempotents that are self-adjoint for the pairing. The article develops the projection operator together with the adjoint in the **operator built from the involution** layer of this Part: the projection is the idempotent of *The Projection Operator*, the pairing is the Hermitian structure of the `*` layer, and their intersection — the orthogonal projection — is the operator the pairing selects, with the kernel and the image orthogonal, the adjoint equal to the operator, and the spectral decomposition as the closure. The article proves which projections are orthogonal, and it proves the agreement of the adjoint with the orthogonal complement rather than assuming it.

The article develops the Hermitian structures on a vector space and on a projective space, the adjoint of a projection with its image and kernel, the orthogonal projection with the characterisation $P^2 = P = P^{\dagger}$ and the least-squares property, the algebra and the order of the orthogonal projections, and the spectral decomposition of a self-adjoint operator into orthogonal projections. The projection itself is *The Projection Operator*, the adjoint is *The Adjoint under a Hermitian Pairing*, and the spectral theory is *Self-Adjoint Operators and the Spectral Theorem*; the article owns their intersection.

The article assumes *The Projection Operator* for the idempotents, the centre of projection and the direct sum decomposition; *The Adjoint under a Hermitian Pairing* for the pairing, the adjoint and the self-adjoint elements; *Unitary Geometry over a Field with Involution* for the Hermitian forms and the unitary group; and *Vector Spaces* and *Linear Maps and Matrices* of Part I for the subspaces and the operators. The spectral theory of the self-adjoint operators and the orthogonal projections on a Hilbert space are *Self-Adjoint Operators and the Spectral Theorem*, named as a forward reference, and the article keeps the finite-dimensional case over a general field with an involution. No distance and no physics is invoked.

## Hermitian Structures on a Projective Space

### The Hermitian Structure

**Definition.** Let $V$ be a finite-dimensional vector space over a field $K$ with an involution $c$, and let $h$ be a nondegenerate Hermitian pairing with the matrix $H$ with $H^{*} = H$. The **Hermitian structure** on $\mathbb{P}(V)$ is the pairing together with the induced polarity $W \mapsto W^\perp$ of the lattice of the subspaces,

$$
W^\perp = \{y \in V : h(w,y) = 0 \ \text{for all } w \in W\} ,
$$

an inclusion-reversing involution with $W^{\perp\perp} = W$ and $\dim W + \dim W^\perp = \dim V$.

**Proposition.** The Hermitian structure determines the orthogonal complement of every subspace, hence a **complementary subspace** for each $W$, the space $W^\perp$; the direct sum $V = W \oplus W^\perp$ holds exactly when the restriction of the pairing to $W$ is nondegenerate, and a subspace with a nondegenerate restriction has the pairing of the direct sum of the two restrictions. Every subspace has at least one complement, but the pairing selects the orthogonal one, and this is the structure that the projections of the next sections will use.

**Proof.** The orthogonal complement is an involution of the lattice by the nondegeneracy of the pairing, and the dimension formula is the standard one; the direct sum decomposition holds exactly when $W \cap W^\perp = 0$, which is the nondegeneracy of the restriction; the statement is the elementary linear algebra of a Hermitian pairing, in *Unitary Geometry over a Field with Involution* and *The Adjoint under a Hermitian Pairing*.

**Definition.** A subspace $W$ is **isotropic** when $h$ vanishes on it, **nondegenerate** when the restriction of $h$ to $W$ is nondegenerate, and **totally isotropic** when all its vectors are isotropic; the pairing is **definite** when every nonzero vector has $h(x,x) \neq 0$ and **indefinite** otherwise. Over the real and the complex fields the definite pairings are the positive-definite ones after the multiplication by a sign, and they are the pairings for which every subspace is nondegenerate.

**Proposition.** A subspace is nondegenerate exactly when it has the orthogonal complement with the direct sum, and the pairing is definite exactly when every subspace is nondegenerate; for the definite pairings the map $W \mapsto W^\perp$ is a complementation of the lattice, while for the indefinite pairings some subspaces meet their orthogonal complements.

**Proof.** The first statement is the previous proposition; a subspace with an isotropic vector fails to be nondegenerate because the span of the isotropic vector meets its orthogonal complement, and conversely a degenerate subspace has an isotropic vector in its radical. The statement is in *Unitary Geometry over a Field with Involution*.

## The Adjoint of a Projection

### The Projection and Its Adjoint

**Definition.** Let $P \in \operatorname{End}_K(V)$ be a projection, $P^2 = P$ (of *The Projection Operator*), and let $P^{\dagger}$ be its adjoint with respect to $h$, $h(Px,y) = h(x,P^{\dagger}y)$ (of *The Adjoint under a Hermitian Pairing*).

**Theorem.** The adjoint $P^{\dagger}$ of a projection is again a projection,

$$
(P^{\dagger})^2 = P^{\dagger} ,
$$

and its image and kernel are the orthogonal complements

$$
\operatorname{im} P^{\dagger} = (\ker P)^\perp , \qquad \ker P^{\dagger} = (\operatorname{im} P)^\perp ;
$$

consequently the adjoint of the projection onto $W$ along $U$ is the projection onto $U^\perp$ along $W^\perp$, and the two projections have the same rank.

**Proof.** The idempotence is $(P^\dagger)^2 = (P^2)^\dagger = P^\dagger$ by the anti-multiplicativity of the adjoint; for the image, $x \in \ker P^\dagger$ exactly when $h(x, Py) = h(P^\dagger x, y) = 0$ for all $y$, that is, exactly when $x$ is orthogonal to the image of $P$; the kernel statement follows, and the image is the orthogonal complement of the kernel by the involution of the lattice. The rank is preserved because the orthogonal complementation preserves the dimension. The statement is in *The Adjoint under a Hermitian Pairing* and *The Projection Operator*.

**Corollary.** The adjoint of a projection has the same trace as the projection, $\operatorname{tr} P^\dagger = \overline{\operatorname{tr} P}$, and for a self-adjoint projection the trace lies in the fixed field; the projection and its adjoint are conjugate when the two subspaces have the same dimension relations, and they coincide exactly in the orthogonal case of the next section.

### The Orthogonal Projection

**Definition.** A projection $P$ is **orthogonal** for $h$ when $P = P^{\dagger}$, equivalently when $\ker P = (\operatorname{im} P)^\perp$; it is then the **orthogonal projection** onto $W = \operatorname{im} P$ along $W^\perp = \ker P$, and it is written $P_W$.

**Theorem (the characterisation).** For a projection $P$ the following are equivalent: (i) $P$ is orthogonal; (ii) $P$ is self-adjoint, $P^\dagger = P$; (iii) $h(x - Px, Px) = 0$ for every $x$, that is, the residual is orthogonal to the image; (iv) the kernel and the image of $P$ are orthogonal complements. For a definite pairing there is exactly one orthogonal projection onto each subspace $W$, namely the projection along $W^\perp$; for an indefinite pairing a subspace may have more than one orthogonal projection or none, according to its degeneration.

**Proof.** The equivalence of (i), (ii) and (iv) is the identity $\ker P^\dagger = (\operatorname{im}P)^\perp$ of the previous theorem applied to the projection $P$: $P = P^\dagger$ holds exactly when the kernel of $P$ equals $(\operatorname{im}P)^\perp$. The equality $h(x - Px, Px) = h(x,Px) - h(Px,Px)$ is the statement (iii), and it vanishes exactly when $Px$ realises the orthogonal decomposition; for a definite pairing every subspace is nondegenerate, so the orthogonal projection exists and is unique, while for an indefinite pairing the existence fails for the isotropic subspaces. The statement is the standard orthogonal projection, in *Unitary Geometry over a Field with Involution*.

**Example (the least-squares property).** Let the pairing be positive definite and let $W \subseteq V$ be a subspace; then for every $x$ the vector $P_W x$ is the unique element of $W$ minimising the square length $h(x - w, x - w)$ over $w \in W$, because $h(x - P_W x, w) = 0$ for all $w \in W$ makes the identity

$$
h(x - w, x - w) = h(x - P_W x, x - P_W x) + h(P_W x - w, P_W x - w)
$$

an orthogonal decomposition; the orthogonal projection is the minimising element, and the property is the arithmetic content of the self-adjointness.

**Proof.** The displayed identity is the expansion of $x - w = (x - P_W x) + (P_W x - w)$ and the vanishing of the cross term, which is the orthogonality of the residual to $W$; the two summands are nonnegative for a definite pairing, so the minimum is attained at $w = P_W x$. The statement is the classical property of the orthogonal projection, in *Unitary Geometry over a Field with Involution* and *Self-Adjoint Operators and the Spectral Theorem*.

## The Algebra of the Orthogonal Projections

### The Order and the Products

**Definition.** The orthogonal projections onto the subspaces are ordered by the inclusion of the images,

$$
P_W \leq P_W' \quad \Longleftrightarrow \quad W \subseteq W' ,
$$

and the meet and the join of two orthogonal projections are the orthogonal projections onto $W \cap W'$ and $W + W'$ when the two subspaces have the appropriate position.

**Theorem.** For two orthogonal projections $P$ and $Q$ the product $PQ$ is a projection exactly when $P$ and $Q$ commute, $PQ = QP$, in which case $PQ$ is the orthogonal projection onto $\operatorname{im} P \cap \operatorname{im} Q$; the order satisfies $P \leq Q$ exactly when $PQ = P$, and the orthogonal projections form a lattice under the order with the meet $P \wedge Q$ the projection onto the intersection when the two commute. The difference $P - Q$ of two orthogonal projections with $Q \leq P$ is again an orthogonal projection.

**Proof.** The product of two self-adjoint idempotents is a projection exactly when it is self-adjoint and idempotent, which forces the commutation; the image of $PQ$ under the commutation is the intersection of the images; the order relation is the idempotence of the product, and the statements are the standard algebra of the projections. The statement is in *Unitary Geometry over a Field with Involution* and *Self-Adjoint Operators and the Spectral Theorem*.

### The Spectral Decomposition

**Theorem (the spectral decomposition).** Let $T$ be a self-adjoint operator on a Hermitian space over a field in which the characteristic is not two, and suppose that $T$ is diagonalisable with the distinct eigenvalues $t_1, \dots, t_k$ in the fixed field; then $T$ decomposes as

$$
T = t_1 P_1 + \cdots + t_k P_k ,
$$

where $P_i$ is the orthogonal projection onto the eigenspace of $t_i$, the projections are pairwise orthogonal, $P_i P_j = 0$ for $i \neq j$, and they sum to the identity, $P_1 + \cdots + P_k = \mathrm{id}$; conversely every sum of this form with the $t_i$ in the fixed field is self-adjoint.

**Proof.** The eigenspaces of a self-adjoint operator are pairwise orthogonal: for $x$ in the eigenspace of $t_i$ and $y$ in the eigenspace of $t_j$, the identity $h(Tx,y) = t_i h(x,y)$ equals $h(x,Ty) = \bar{t}_j h(x,y) = t_j h(x,y)$ because the eigenvalues are fixed, so $(t_i - t_j)h(x,y) = 0$; the projections onto the eigenspaces are orthogonal and the sum of the operators is $T$ on the sum of the eigenspaces, which is the whole space by the diagonalisability. The statement is in *Self-Adjoint Operators and the Spectral Theorem*.

**Corollary (the orthogonal projection as a spectral projection).** An operator $P$ is an orthogonal projection exactly when it is self-adjoint with the eigenvalues $0$ and $1$, and the orthogonal projections are exactly the spectral projections of the spectral decomposition; the lattice of the orthogonal projections is the lattice of the self-adjoint idempotents, and the spectral theorem expresses every diagonalisable self-adjoint operator as a combination of them.

**Remark (the pairing selects one projection among many).** A subspace $W$ carries many projections onto it along its various complements, and the projection $P_W$ is the unique one that is self-adjoint for the pairing; the Hermitian structure therefore does not add a new projection to the space but it fixes one among the existing ones, and this is the sense in which the article is the intersection of *The Projection Operator* and *The Adjoint under a Hermitian Pairing*.

## Summary

A Hermitian structure on $\mathbb{P}(V)$ is a nondegenerate Hermitian pairing $h$ with the polarity $W \mapsto W^\perp$; it selects the complements and the nondegenerate subspaces, and for a definite pairing every subspace is nondegenerate. The adjoint of a projection $P$ is again a projection, with $\operatorname{im} P^\dagger = (\ker P)^\perp$ and $\ker P^\dagger = (\operatorname{im} P)^\perp$, so the adjoint of the projection onto $W$ along $U$ is the projection onto $U^\perp$ along $W^\perp$. A projection is **orthogonal** exactly when $P = P^\dagger$, equivalently when the kernel and the image are orthogonal complements, equivalently when $h(x - Px, Px) = 0$; for a definite pairing the orthogonal projection $P_W$ onto each subspace exists and is unique and is the minimising element of the square length over $W$. The orthogonal projections are ordered by the images, the product of two is a projection exactly when they commute, and the spectral decomposition writes a diagonalisable self-adjoint operator as $T = t_1P_1 + \cdots + t_kP_k$ with pairwise orthogonal projections summing to the identity; the orthogonal projections are exactly the self-adjoint idempotents, and the pairing fixes one projection among the many onto each subspace.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $h(x,y) = \overline{h(y,x)}$ | Nondegenerate Hermitian pairing |
| $W^\perp = \{y : h(W,y) = 0\}$ | Orthogonal complement, the polarity |
| $P^2 = P$ | Projection (idempotent) |
| $P^{\dagger}$ | Adjoint of the projection |
| $\operatorname{im} P^\dagger = (\ker P)^\perp$ | Image of the adjoint |
| $\ker P^\dagger = (\operatorname{im} P)^\perp$ | Kernel of the adjoint |
| $P = P^{\dagger}$ | Orthogonal (self-adjoint) projection |
| $P_W$ | Orthogonal projection onto $W$ along $W^\perp$ |
| $h(x - Px, Px) = 0$ | Orthogonality of the residual, the characterisation |
| $P \leq Q \iff \operatorname{im} P \subseteq \operatorname{im} Q$ | Order of the orthogonal projections |
| $PQ = QP$ | Condition for the product to be a projection |
| $T = \sum_i t_i P_i$ | Spectral decomposition |

## Further Reading

- Paul R. Halmos, *Finite-Dimensional Vector Spaces*, 2nd ed. (Van Nostrand, 1958), for the projections, the adjoints and the orthogonal projections.
- Paul R. Halmos, *A Hilbert Space Problem Book*, 2nd ed. (Springer, 1982), for the algebra and the lattice of the orthogonal projections.
- Tsit Yuen Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for the Hermitian forms and the nondegenerate subspaces.
- Jean Dieudonné, *La géométrie des groupes classiques* (Springer, 1955), for the Hermitian structures and the unitary groups.
- Israel M. Gelfand and Mark A. Naimark, *Unitäre Darstellungen der klassischen Gruppen* (Akademie-Verlag, 1957), for the projection-valued measures and the spectral theory.
