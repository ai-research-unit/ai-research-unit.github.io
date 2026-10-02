
# __The Projection Operator on a Locally Convex Space__

## Introduction

A projection of a linear space is an endomorphism equal to its own square, and it is the algebraic form of a direct-sum decomposition: the space is the direct sum of the kernel and the image, and conversely a decomposition produces a projection. When the space is a locally convex space and the projection is continuous, the decomposition is a **topological direct sum**: the two summands are closed, the sum map is a topological isomorphism, and the projection is open onto its image. The question whether a given closed subspace is a summand of such a decomposition is the question whether it is **complemented**, and this is not automatic: $c_{0}$ is not complemented in $\ell^{\infty}$, and the complemented subspaces of $\ell^{1}$ are rigid, by the theorem of Lindenstrauss and Tzafriri. In the presence of a compatible inner product the orthogonal projection solves the problem for every closed subspace, but that construction is geometric and belongs to the Hilbert-space theory of Part III.

This article develops the algebraic and the topological theory of projections on a locally convex space. The topological vector spaces, the direct sums and the quotient topologies are *Topological Modules and Vector Spaces*; the locally convex spaces, the finite-dimensional subspaces and the sum topology are *Locally Convex Spaces*; the continuity criterion and the induced map are *Bounded Operators on a Topological Vector Space*; the bounded operators and the operator norm are *Bounded Operators and the Operator Norm*; the orthogonal projection of a Hilbert space, the closed-graph theorem of a complemented subspace and the geometric splitting are *Banach and Hilbert Spaces* in Part III, named and not used. Nothing analytic and nothing geometric is used here.

Throughout, $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$, $E, F$ are Hausdorff locally convex spaces over $\mathbb{K}$, and $\mathcal{L}(E)$ is the algebra of continuous operators. An **idempotent** is $P \in \mathcal{L}(E)$ with $P^{2} = P$; its kernel and its image are written $\ker P$ and $\mathrm{im}\,P$, and $\mathrm{id} - P$ is the complementary idempotent. A subspace $M \subseteq E$ is **complemented** when there is a closed subspace $N$ with $E = M \oplus N$ and the sum map $M \times N \to E$ is a topological isomorphism.

## Projections and Direct Decompositions

**Proposition (idempotents and decompositions).** Let $P \in \mathcal{L}(E)$ satisfy $P^{2} = P$. Then every $x \in E$ decomposes uniquely as $x = (x - Px) + Px$ with $x - Px \in \ker P$ and $Px \in \mathrm{im}\,P$, so

$$
E = \ker P \oplus \mathrm{im}\,P ,
$$

$\mathrm{im}\,P = \ker(\mathrm{id} - P)$, and $\ker P = \mathrm{im}(\mathrm{id} - P)$. Conversely, if $E = M \oplus N$ is an algebraic direct sum, the map $P$ that is the identity on $M$ and zero on $N$ is idempotent with $\mathrm{im}\,P = M$ and $\ker P = N$, and it is the unique idempotent with those kernel and image.

**Proof.** $P(x - Px) = Px - P^{2}x = 0$, and $Px \in \mathrm{im}\,P$; the decomposition is unique because an element of $\ker P \cap \mathrm{im}\,P$ is killed by $P$ and is in its image, hence is $0$. The statements about $\mathrm{id} - P$ are symmetric. For the converse, $P$ as defined is linear, satisfies $P^{2} = P$, and has the stated kernel and image; uniqueness is the decomposition.

**Proposition (continuity of the summand projection).** Let $P \in \mathcal{L}(E)$ be idempotent. Then $\ker P$ and $\mathrm{im}\,P$ are closed, the map

$$
\Phi : \ker P \times \mathrm{im}\,P \longrightarrow E, \qquad \Phi(u, v) = u + v ,
$$

is a topological isomorphism, and $P$ is an open map onto its image. Conversely, if $E = M \oplus N$ is a topological direct sum, the projection onto $M$ along $N$ is continuous.

**Proof.** The kernel of a continuous map is closed, and $\ker(\mathrm{id} - P) = \mathrm{im}\,P$ is closed for the same reason. The inverse of $\Phi$ is $x \mapsto (x - Px, Px)$, which is continuous, so $\Phi$ is a continuous bijection with continuous inverse. The restriction of $P$ to $E$ is the composite of $\Phi^{-1}$ and the projection onto the second factor, hence open onto its image. Conversely, the projection onto $M$ along $N$ is the composite of the inverse of the sum isomorphism and the projection of a product, hence continuous.

## Complemented Subspaces

**Theorem (complemented exactly when there is a continuous projection).** A closed subspace $M \subseteq E$ is complemented if and only if there is $P \in \mathcal{L}(E)$ with $P^{2} = P$ and $\mathrm{im}\,P = M$; then $N = \ker P$ is a complement. A subspace that is the kernel of a continuous idempotent is complemented by its image.

**Proof.** Given a continuous $P$ with image $M$, the previous proposition gives $E = M \oplus \ker P$ as a topological direct sum, so $M$ is complemented. Conversely, if $E = M \oplus N$ is a topological direct sum, the projection onto $M$ along $N$ is continuous by the previous proposition and is idempotent with image $M$. The kernel statement is the symmetric argument applied to $\mathrm{id} - P$.

**Proposition (the elementary cases).** Every finite-dimensional subspace of a locally convex space is complemented; every closed subspace $M$ such that $\dim E/M < \infty$ is complemented; and if $M$ is complemented, then $M$ is closed. In a normed space a finite-dimensional subspace is complemented by any algebraic complement, which is closed because it is the kernel of the bounded projection onto the finite-dimensional summand.

**Proof.** If $\dim M < \infty$, choose a basis $e_{1}, \dots, e_{n}$ of $M$ and functionals $\varphi_{i} \in E'$ with $\varphi_{i}(e_{j}) = \delta_{ij}$, by the separation of points of a locally convex space; then $Px = \sum_{i}\varphi_{i}(x)e_{i}$ is a continuous idempotent with image $M$. The finite-codimensional case is the same construction on the quotient lifted by Hahn–Banach. The last statement is that a complemented subspace is one of the summands of a topological direct sum, hence closed.

**Theorem (the orthogonal case, deferred).** In a Hilbert space every closed subspace is complemented, by the orthogonal projection along the orthogonal complement; this is the projection theorem of *Banach and Hilbert Spaces* in Part III, and it uses the inner product and the geometry of a Hilbert space, which the present Part does not.

**Proof.** The statement is recorded here as a forward reference and is neither proved nor used; the orthogonal projection is constructed there from the nearest-point property of a closed convex set in a complete inner-product space.

## The Failure of Complementation

**Theorem (Phillips).** The closed subspace $c_{0}$ of the Banach space $\ell^{\infty}$ is not complemented.

**Proof.** The theorem of Phillips states that there is no bounded projection of $\ell^{\infty}$ onto $c_{0}$; it is quoted from the literature, and its proof uses the structure of the finitely additive measures on $\mathbb{N}$ and the fact that $c_{0}^{\perp}$ contains no $\ell^{1}$-summable structure. It shows in particular that the closed subspaces of a Banach space are not automatically complemented, and hence that the continuous projection of the theorem above cannot always be found.

**Theorem (Lindenstrauss and Tzafriri).** Every infinite-dimensional complemented subspace of $\ell^{1}$ is isomorphic to $\ell^{1}$.

**Proof.** This is the theorem of Lindenstrauss and Tzafriri; it is quoted, and it shows that an infinite-dimensional closed subspace of $\ell^{1}$ that is not isomorphic to $\ell^{1}$ is not complemented. The two theorems together make the class of complemented subspaces a proper subclass of the closed subspaces, in both the separable and the non-separable setting.

**Remark (the general Banach-space problem).** The complementation problem — which closed subspaces of a Banach space are complemented — is the subject of the theory of injective and projective spaces and of the approximation property; the results above are the first two answers, and the counterexamples depend on the space. A space in which every closed subspace is complemented is isomorphic to a Hilbert space, by a theorem of Lindenstrauss and Tzafriri, so complementation is the exception rather than the rule.

## The Sum of Two Closed Subspaces

**Theorem (closedness of a sum).** Let $X$ be a Banach space and let $M, N \subseteq X$ be closed subspaces with $M \cap N = \{0\}$. Then the algebraic sum $M + N$ is closed in $X$ if and only if the projection $P : M + N \to M$ along $N$ is continuous for the norm inherited from $X$; in that case $M + N$ is a topological direct sum and $M, N$ are complemented in $M + N$.

**Proof.** Give $M \times N$ the sum norm, which is complete because $M$ and $N$ are, and consider the continuous bijection $\Phi : M \times N \to M + N$ onto the subspace $M + N$ with the norm of $X$. If $M + N$ is closed, it is a Banach space and the open mapping theorem makes $\Phi$ a topological isomorphism; then $P$ is the composite of $\Phi^{-1}$ with the projection of the product, hence continuous. Conversely, if $P$ is continuous, then $\mathrm{id} - P$ is the projection onto $N$ and $M + N$ is the image of the continuous idempotent $P$ read in the ambient space, hence closed; the topological direct-sum statement is the proposition above.

**Corollary (failure of closedness).** There exist closed subspaces $M, N$ of a Banach space with $M \cap N = \{0\}$ but $M + N$ not closed, so the sum map of a pair of closed subspaces need not be a topological isomorphism.

**Proof.** This is stated and proved in the literature on the three-space problem; it is quoted here. The dichotomy of the theorem is the reason the statement is not vacuous: closedness of $M + N$ is exactly the continuity of the sum projection, which fails for suitable pairs.

## Summary

An idempotent operator $P$ on a locally convex space produces the algebraic direct sum $E = \ker P \oplus \mathrm{im}\,P$, and conversely every decomposition produces an idempotent; the operator is a projection exactly when it is an idempotent endomorphism. When $P$ is continuous, the direct sum is a topological one, the summands are closed, the sum map $\ker P \times \mathrm{im}\,P \to E$ is a topological isomorphism and $P$ is open onto its image; a closed subspace is complemented exactly when it is the image of a continuous idempotent, and finite-dimensional and finite-codimensional closed subspaces are always complemented. Complementation fails in general: $c_{0}$ is not complemented in $\ell^{\infty}$ by Phillips' theorem, and every infinite-dimensional complemented subspace of $\ell^{1}$ is isomorphic to $\ell^{1}$ by the theorem of Lindenstrauss and Tzafriri, so the complemented subspaces are a proper class; only in a Hilbert space, where the orthogonal projection solves the problem, is every closed subspace complemented, and that is the geometry of Part III. The sum of two closed subspaces with zero intersection is closed exactly when the associated projection is continuous, which is the open mapping theorem in the form used for decompositions.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P$, $P^{2} = P$ | Idempotent, a projection |
| $\ker P$, $\mathrm{im}\,P$ | Kernel and image, the two summands |
| $E = \ker P \oplus \mathrm{im}\,P$ | Algebraic and, for continuous $P$, topological direct sum |
| $\mathrm{id} - P$ | Complementary projection |
| complemented | Closed subspace that is a summand of a topological direct sum |
| $c_{0} \subseteq \ell^{\infty}$ | Non-complemented pair of Phillips |
| Lindenstrauss–Tzafriri | Complemented subspaces of $\ell^{1}$ are isomorphic to $\ell^{1}$ |
| $M + N$ closed | Equivalent to continuity of the sum projection |
| orthogonal projection | Hilbert-space case, Part III |

## Further Reading

- Nicolas Bourbaki, *Topological Vector Spaces, Chapters 1–5* (Springer, 1987), for direct sums, projections and the topology of a sum.
- Helmut H. Schaefer and Manfred P. Wolff, *Topological Vector Spaces* (Springer, second edition, 1999), for the complementation of subspaces and the open mapping theorem.
- Joram Lindenstrauss and Lior Tzafriri, *Classical Banach Spaces I* (Springer, 1977), for the theorem that every infinite-dimensional complemented subspace of $\ell^{1}$ is isomorphic to $\ell^{1}$, and for the structure of the classical spaces.
- Robert E. Megginson, *An Introduction to Banach Space Theory* (Springer, 1998), for Phillip's theorem, the complementation problem and the characterisation of Hilbert spaces by complementation.
- Joseph Diestel, *Sequences and Series in Banach Spaces* (Springer, 1984), for the non-complemented subspaces and the finitely additive measures on $\mathbb{N}$.
