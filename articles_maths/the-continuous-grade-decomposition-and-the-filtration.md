# __The Continuous Grade Decomposition and the Filtration__

## Introduction

The Clifford algebra of a non-degenerate quadratic form is not graded by the number of its generators, but it is filtered by it and its associated graded algebra is the exterior algebra; the grade-$k$ subspace $\mathrm{Cl}_k(V,q)$ is nevertheless meaningful for a non-degenerate form, its elements are the $k$-vectors, and the algebra decomposes as the direct sum of the grades. This article reads that double structure — a grading and a filtration, and the map between them — with a topology.

The two structures behave differently, and that difference is the content of the article. The **grading** is a decomposition into subspaces, and a decomposition into finitely or countably many subspaces is a *topological* decomposition as soon as the projections are continuous, which they are here because they are built from finite sums of continuous operators; the grades are then closed subspaces and the algebra is their topological direct sum. The **filtration** is a chain, and a chain gives a topology only when it is turned into a neighbourhood basis of zero, which the ascending chain of the length filtration does not do: the object that generates a topology is the **descending** chain $N_{k}$ of elements of degree at least $k$, its quotients $\mathrm{Cl}(V,q)/N_{k}$ are the elements of bounded degree, and the topology it defines is the filtration topology of the layer. The associated graded algebra of that descending chain is the exterior algebra, degree by degree, and the completion of the algebra for the filtration is the inverse limit of the quotient algebras.

Two facts are worth stating at the outset because they fix the shape of the layer. The filtration topology is **discrete** in finite dimension, so the topology of the grading and the filtration has no content there and the whole layer is infinite-dimensional; and the topology is **separated** whenever the form is non-degenerate, because the algebra is the direct sum of its grades, so the intersection of the $\mathrm{Cl}_{j}$ for $j\ge k$ is zero. What the topology adds in infinite dimension is the possibility of infinite sums, and with it the completion, which is where the canonical anticommutation relations of *Infinite-Dimensional Clifford Algebras and CAR with Inner Conjugation* live.

The article treats the grade decomposition and the continuity of its projections, the descending filtration and the topology it generates, the associated graded algebra and the isomorphism with the exterior algebra, the relation between the two topologies of the algebra, and the completion of the filtration. The volume element and the Hodge star, which are built from the top grade, are *The Continuous Volume Element, Duality and the Hodge Star*; the completion is developed further in *The Completion of a Clifford Algebra*; the algebraic statements are *The Geometric Product and the Grade Decomposition*, *The Filtration and the Associated Graded Algebra* and *The Exterior Algebra*. Throughout, $F$ is a topological field of characteristic not $2$, $V$ a topological $F$-module with a continuous quadratic form $q$ and $n=\dim V$ where finite, and the algebra is that of *Topological Clifford Algebras*.

## The Grade Decomposition and its Continuity

### The Grade Projections

**Definition.** The **grade-$k$ subspace** $\mathrm{Cl}_{k}(V,q)$ is the linear span of the products of exactly $k$ vectors in an orthogonal basis, and the **grade projection** $\langle x\rangle_{k}$ is the component of $x$ in that subspace, as in *The Geometric Product and the Grade Decomposition*, §*The Grade Projection*. The **antisymmetriser** is

$$
A_{k} = \frac{1}{k!}\sum_{\sigma\in\mathfrak{S}_{k}}\operatorname{sgn}(\sigma)\,\sigma \qquad \text{on } V^{\otimes k},
$$

a finite rational linear combination of the continuous permutation operators of the tensor power.

**Proposition (the antisymmetriser is continuous and idempotent).** For each $k$ the antisymmetriser $A_{k}$ is a continuous linear map of $V^{\otimes k}$, it is idempotent, and its image is $\mathrm{Cl}_{k}(V,q)$ under the projection of the tensor algebra.

*Proof.* Each permutation operator is continuous, being induced by the continuous action of the finite group $\mathfrak{S}_{k}$ on the tensor power and by the universal property of the tensor topology; a finite linear combination of continuous maps is continuous, and the coefficient $1/k!$ exists because the base has characteristic $0$ or characteristic greater than $n$, the hypothesis under which the antisymmetrisation isomorphism of *The Geometric Product and the Grade Decomposition*, §*The Grade Projection* is stated. The idempotence is the algebraic computation of *The Geometric Product and the Grade Decomposition*, §*The Grade Projection*, and the identification of the image with the grade subspace is the content of the antisymmetrisation theorem proved there. $\square$

### The Decomposition as a Topological Direct Sum

**Theorem.** Let $q$ be non-degenerate on the finite-dimensional space $V$. Then the grade projections $\langle\cdot\rangle_{k}$, $k=0,\dots,n$, are continuous linear maps and

$$
\mathrm{Cl}(V,q) = \bigoplus_{k=0}^{n}\mathrm{Cl}_{k}(V,q)
$$

is a topological direct sum of closed subspaces; consequently every linear map out of the algebra that is continuous on each grade is continuous, and a sequence converges if and only if each of its grade components converges.

*Proof.* In finite dimension the algebra is a finite-dimensional Hausdorff vector space, hence carries a unique topology, and every linear map on it is continuous; the algebraic decomposition is by *The Geometric Product and the Grade Decomposition*, §*The Grade Projection*, and the summands are closed because they are finite-dimensional subspaces of a Hausdorff space. A finite direct sum of Hausdorff spaces is topological for the product structure. $\square$

**Remark (infinite dimension).** When $V$ is infinite-dimensional the same proof fails at two points: the algebra is no longer finite-dimensional, so linear maps need not be continuous, and the sum has infinitely many terms, so a direct sum is not automatically topological. What survives is the following: the grade subspaces $\mathrm{Cl}_{k}(V,q)$ are closed whenever the form is non-degenerate and the decomposition is algebraic, and the grade projections $\langle\cdot\rangle_{k}$ are continuous for the topology of the tensor algebra restricted to the algebra, since the antisymmetriser is continuous and the quotient map is open. The sum is then a direct sum of closed subspaces which need not be topological for the norm, and the passage from a converging sum to its grade components is a statement about the completion, not about the algebra; it is treated in *The Completion of a Clifford Algebra*.

## The Descending Filtration and its Topology

### The Length Filtration and the Descending Chain

**Definition.** The **length filtration** is the increasing chain $F_{k}$ of images of $\bigoplus_{j\le k}V^{\otimes j}$ of *The Filtration and the Associated Graded Algebra*, §*The Length Filtration*; the **descending chain** is

$$
N_{k} = \operatorname{im}\Bigl(\bigoplus_{j\ge k}V^{\otimes j}\Bigr) ,
$$

the image of the elements of degree at least $k$. The **filtration topology** is the linear topology for which the chain $\{N_{k}\}_{k\ge0}$ is a fundamental system of neighbourhoods of zero.

The chain $N_{k}$ is the one that carries a topology: it is descending, $N_{0}=\mathrm{Cl}(V,q)\supseteq N_{1}\supseteq N_{2}\supseteq\cdots$, and it is a two-sided ideal filtration, $N_{j}N_{l}\subseteq N_{j+l}$, because the product of an element of degree at least $j$ with one of degree at least $l$ has degree at least $j+l$. The length filtration is the increasing chain $F_{k}$, with $F_{j}F_{l}\subseteq F_{j+l}$, and it is the object that the Part I article uses; the two are matched by the identities

$$
F_{k}+N_{k+1} = \mathrm{Cl}(V,q), \qquad F_{k}\cap N_{k+1} = \mathrm{Cl}_{k}(V,q) ,
$$

the second holding when the form is non-degenerate and the grade decomposition is available.

### The Quotients and the Separation

**Proposition.** The quotient $\mathrm{Cl}(V,q)/N_{k}$ is linearly isomorphic to $F_{k-1}$, the elements of degree at most $k-1$; it is finite-dimensional when $V$ is finite-dimensional, of dimension $\sum_{j<k}\binom{n}{j}$; and the canonical maps $\mathrm{Cl}/N_{k+1}\to\mathrm{Cl}/N_{k}$ are onto. The filtration topology is Hausdorff if and only if $\bigcap_{k}N_{k}=0$.

*Proof.* The identity $F_{k-1}+N_{k}=\mathrm{Cl}$ and the directness of $F_{k-1}\cap N_{k}=\mathrm{Cl}_{k-1}$ in the non-degenerate case identify the quotient with $F_{k-1}$; the dimension statement is the sum of the binomial coefficients, and the surjectivity is the inclusion $N_{k}\supseteq N_{k+1}$. A linear topology with a decreasing neighbourhood basis $\{N_{k}\}$ of zero is Hausdorff exactly when the intersection of the basis is zero, by the separation criterion of *Topological Groups*, §*Separation*. $\square$

**Theorem (discreteness and separation).** Let $V$ be finite-dimensional of dimension $n$ and $q$ non-degenerate. Then $N_{k}=0$ for $k>n$, the filtration topology is discrete, and the algebra is separated. In general the filtration is separated whenever the form is non-degenerate: $\bigcap_{k}N_{k}=0$.

*Proof.* For a non-degenerate form the algebra is the direct sum of the grades $\mathrm{Cl}_{j}$ with $0\le j\le n$, and $N_{k}=\bigoplus_{j\ge k}\mathrm{Cl}_{j}$, which is zero once $k>n$; a topology with $N_{n+1}=0$ as a neighbourhood of zero is discrete. In infinite dimension the same identity $N_{k}=\bigoplus_{j\ge k}\mathrm{Cl}_{j}$ holds as a direct sum of subspaces, so an element of the intersection would have all its grade components of arbitrarily large degree and hence be zero, the decomposition being direct. $\square$

**Remark.** The theorem is the reason the layer has no content in finite dimension: the filtration topology is discrete, the algebra is its own completion, and the topological statements about the grading are the trivial ones of a unique topology. Everything that follows in the category is thus a statement about infinite dimension, and the articles say so when they are.

## The Associated Graded Algebra

### The Isomorphism with the Exterior Algebra

**Theorem.** The associated graded algebra $\operatorname{gr}\mathrm{Cl}(V,q)=\bigoplus_{k\ge0}N_{k}/N_{k+1}$ with the product induced by the filtration is isomorphic, as a graded algebra, to the exterior algebra $\Lambda(V)$ of *The Exterior Algebra*:

$$
\operatorname{gr}\mathrm{Cl}(V,q)\;\cong\;\Lambda(V), \qquad N_{k}/N_{k+1}\cong\Lambda^{k}V .
$$

*Proof.* The algebraic statement, that the natural map from the filtration quotients to the exterior powers is an isomorphism and that the induced product is the wedge product, is the theorem of Poincaré–Birkhoff–Witt for Clifford algebras proved in *The Filtration and the Associated Graded Algebra*, §*The Associated Graded Algebra*. It is a statement about the algebra and not about its topology, and it therefore holds for every quadratic form, degenerate ones included; the degenerate case is treated degreewise and the isomorphism is degreewise. $\square$

**Corollary (graded-commutativity of the associated graded).** The associated graded algebra is graded-commutative: for $\bar x\in N_{j}/N_{j+1}$ and $\bar y\in N_{l}/N_{l+1}$ one has $\bar x\bar y=(-1)^{jl}\bar y\bar x$. It is not commutative unless the form is zero or the space is spanned by the scalars.

*Proof.* The wedge product is graded-commutative by *The Exterior Algebra*, §*Graded-Commutativity*, and the isomorphism transports the relation. For the last clause, a non-zero vector $v$ and a non-zero scalar $\lambda$ fail to commute as soon as $q(v)\neq0$, since $v\lambda$ commutes while $v\wedge v=0$; the failure is the failure of commutativity that the filtration hides. $\square$

### The Symbol Map and the Two Topologies

**Definition.** The **symbol map** is the linear isomorphism $\sigma : \mathrm{Cl}(V,q)\to\Lambda(V)$ obtained by reading an element grade by grade in the associated graded algebra, as in *The Filtration and the Associated Graded Algebra*, §*The Relation to the Grade Decomposition*; it is the inverse of the antisymmetrisation.

**Proposition.** In finite dimension the symbol map is a homeomorphism for the unique topologies, and for a non-degenerate form it is a linear isomorphism of the algebra onto the exterior algebra as graded vector spaces. In infinite dimension $\sigma$ is an isomorphism of vector spaces, the topology of the tensor algebra is finer than the filtration topology, and the two agree on each $F_{k}$.

*Proof.* In finite dimension both spaces are finite-dimensional Hausdorff, so every linear isomorphism is a homeomorphism. In general the filtration topology is finer than the quotient topology of the tensor algebra, because each map $\mathrm{Cl}(V,q)\to\mathrm{Cl}(V,q)/N_{k}$ factors through the quotient by the submodule $\bigoplus_{j\ge k}V^{\otimes j}$, hence is continuous for the quotient topology, and the filtration topology is by definition the finest linear topology for which all these maps are continuous; the two coincide in finite dimension. $\square$

**Remark (no assertion of a general comparison).** The article asserts only that the filtration topology is the **finer** of the two and that they coincide in finite dimension. In infinite dimension the quotient topology of the tensor algebra may be strictly coarser; it is the topology of the convergent series of the tensor algebra, while the filtration topology is the topology of the inverse limit of the bounded-degree quotients, and the associated graded algebra is the same for both. The comparison of the corresponding completions is made in *The Completion of a Clifford Algebra*.

## The Completion of the Filtration

**Definition.** The **completion** of the algebra for the filtration is

$$
\widehat{\mathrm{Cl}(V,q)} = \varprojlim_{k}\mathrm{Cl}(V,q)/N_{k} ,
$$

with the inverse-limit topology; it is a complete Hausdorff topological algebra when the filtration is separated, and it contains $\mathrm{Cl}(V,q)$ as a dense subalgebra.

**Proposition.** The completion is a topological algebra for the inverse-limit topology, the algebra embeds densely, and the associated graded algebra of the completion for its induced filtration is the same exterior algebra: $\operatorname{gr}\widehat{\mathrm{Cl}}\cong \Lambda(V)$.

*Proof.* An inverse limit of discrete rings along continuous maps is a complete topological ring, by the general theory of inverse limits of topological modules of *Topological Modules and Vector Spaces*; the density of the image is the standard property of the inverse limit over a cofinal family, the maps $\mathrm{Cl}/N_{k+1}\to\mathrm{Cl}/N_{k}$ being onto. The induced filtration on the completion has the same successive quotients, whence the identification of the associated graded. $\square$

**Remark (why the completion matters).** In finite dimension the completion is the algebra itself, by the discreteness theorem; in infinite dimension it is strictly larger, and it is where an infinite sum of terms of increasing degree is allowed to converge. The canonical anticommutation relations of *Infinite-Dimensional Clifford Algebras and CAR with Inner Conjugation* are the relation $v^{2}=q(v)$ read on the operators of this completion, and the article there takes the completion as its starting point.

## Examples

### The Finite-Dimensional Cases

**Example.** Let $V=\mathbb{R}^{2}$ with $q=x^{2}+y^{2}$. Then $\mathrm{Cl}(V,q)\cong M_{2}(\mathbb{R})$ by *The Low-Dimensional Classification*, since this is the algebra $\mathrm{Cl}_{2,0}$, while the quaternion algebra is $\mathrm{Cl}_{0,2}$; the grades are $\mathrm{Cl}_{0}=\mathbb{R}$, $\mathrm{Cl}_{1}$ of dimension two and $\mathrm{Cl}_{2}=\mathbb{R}\,\omega$ with $\omega$ the volume element, the filtration topology is discrete because $N_{3}=0$, and the associated graded algebra is $\Lambda(\mathbb{R}^{2})$ of dimension four. The symbol map is the identity on the grades read in the basis $1,e_{1},e_{2},\omega$ and it is the homeomorphism of the proposition. The example is the smallest nontrivial one: the grading is visible, the filtration is trivial as a topology, and the whole content of the article is in the infinite-dimensional case.

**Example (the zero form).** Let $q=0$. Then the algebra is the exterior algebra itself, $\mathrm{Cl}_{k}=\Lambda^{k}V$ for every $k$, the filtration is $\Lambda(V)=\bigoplus_{k}\Lambda^{k}V$ with $N_{k}=\bigoplus_{j\ge k}\Lambda^{j}V$, and the associated graded algebra is $\Lambda(V)$ again, the symbol map being the identity. The filtration topology is discrete in finite dimension and is the product topology of the graded pieces in infinite dimension.

### The Exterior Algebra with a Non-Discrete Topology

**Example.** Let $V$ be an infinite-dimensional Hilbert space with the form $q(v)=\lVert v\rVert^{2}$ and let the tensor algebra carry the topology of the norm of *Infinite-Dimensional Clifford Algebras and CAR with Inner Conjugation*. The descending chain $N_{k}$ consists of the elements of degree at least $k$, it is not zero for any $k$, and the filtration topology is separated by the directness of the grade decomposition; the two completions of the algebra — the one for the norm of the Hilbert space and the one for the filtration — are the completions of two different topologies on the same algebra, the filtration topology being the finer, and they therefore agree exactly when the two topologies have the same Cauchy filters; the article *The Completion of a Clifford Algebra* works out the criterion, and the present article keeps the filtration and its associated graded.

## Summary

The **grade decomposition** $\mathrm{Cl}(V,q)=\bigoplus_{k}\mathrm{Cl}_{k}(V,q)$ is a decomposition into closed subspaces, and the grade projections are continuous, being built from the finite linear combinations of continuous permutation operators that define the antisymmetriser; in finite dimension the decomposition is a **topological direct sum**, the algebra carrying a unique topology, and in infinite dimension the grade subspaces are closed and the algebraic decomposition holds but the topological direct sum is a statement about the completion.

The **filtration** that carries a topology is the descending chain $N_{k}$ of elements of degree at least $k$, a two-sided ideal filtration with $N_{j}N_{l}\subseteq N_{j+l}$; its **filtration topology** has $\{N_{k}\}$ as a neighbourhood basis of zero, its quotients are the bounded-degree parts $F_{k-1}$, finite-dimensional when $V$ is, and it is separated exactly when $\bigcap_{k}N_{k}=0$, which holds for every non-degenerate form because the algebra is the direct sum of its grades. In finite dimension $N_{n+1}=0$ and the topology is **discrete**, so the layer is empty there and everything of content happens in infinite dimension.

The **associated graded algebra** is the exterior algebra, degree by degree, $\operatorname{gr}\mathrm{Cl}(V,q)\cong\Lambda(V)$ with $N_{k}/N_{k+1}\cong\Lambda^{k}V$; it is **graded-commutative**, and the **symbol map** reading the algebra grade by grade is a homeomorphism in finite dimension and an isomorphism of vector spaces in general. The **completion** is the inverse limit of the quotients $\mathrm{Cl}/N_{k}$, a complete topological algebra with the same associated graded and with the algebra as a dense subalgebra; it is the object that allows infinite sums of elements of increasing degree, and it is the home of the canonical anticommutation relations.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathrm{Cl}_{k}(V,q)$, $\langle x\rangle_{k}$ | the grade-$k$ subspace and the grade projection |
| $A_{k}$ | the antisymmetriser, a continuous idempotent of $V^{\otimes k}$ |
| $F_{k}$ | the length filtration, increasing, of elements of degree at most $k$ |
| $N_{k}$ | the descending chain of elements of degree at least $k$, with $N_{j}N_{l}\subseteq N_{j+l}$ |
| $F_{k}+N_{k+1}=\mathrm{Cl}$, $F_{k}\cap N_{k+1}=\mathrm{Cl}_{k}$ | the matching of the two chains |
| $\{N_{k}\}$ | the filtration topology, a fundamental system of neighbourhoods of zero |
| $\operatorname{gr}\mathrm{Cl}\cong\Lambda(V)$ | the associated graded algebra, the exterior algebra |
| $\sigma$ | the symbol map $\mathrm{Cl}(V,q)\to\Lambda(V)$ |
| $\widehat{\mathrm{Cl}(V,q)}=\varprojlim\mathrm{Cl}/N_{k}$ | the completion of the filtration |

## Further Reading

- John B. Conway, *A Course in Functional Analysis*, 2nd edition (Springer, 1990), for the direct sum and the product of topological vector spaces and the distinction between them.
- Nicolas Bourbaki, *Commutative Algebra* (Springer, 1989), for the filtration, the associated graded algebra and the separatedness of a filtered module.
- Nicolas Bourbaki, *Topological Vector Spaces* (Springer, 1987), for the inverse limit, the completeness and the density of the image.
- Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras* (Springer, 1997), for the filtration of a Clifford algebra and the isomorphism of its associated graded with the exterior algebra.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the grading and the symbol map in the finite-dimensional theory.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, Vol. II (Academic Press, 1986), for the completions of an infinite-dimensional Clifford algebra and the canonical anticommutation relations.
