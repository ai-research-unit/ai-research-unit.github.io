
# __Dimension Theory__

## Introduction

The dimension of a space is the numerical invariant that measures how many independent directions the space has, and it is a topological invariant: homeomorphic spaces have the same dimension. There are three classical definitions. The **covering dimension** $\dim X$ is defined by refinements of open covers and the order of a cover, and it is the definition that generalises to arbitrary topological spaces and that makes the dimension of the cube $I^n$ equal to $n$ by an argument with the Lebesgue covering lemma. The **small inductive dimension** $\operatorname{ind} X$ and the **large inductive dimension** $\operatorname{Ind} X$ are defined inductively by the boundaries of neighbourhoods of points and of closed sets respectively. For separable metrisable spaces the three agree, by the theorem of Menger, Urysohn and Brouwer, and this is the theorem that fixes the dimension of Euclidean space, of the cube and of a manifold. For general spaces the three can differ, and the differences are themselves a source of examples.

This article develops the three definitions, the inducing theorems of dimension zero, the sum, product and subspace theorems for the covering dimension of metrisable spaces, and the invariance of dimension. The Lebesgue covering lemma is the compactness statement that makes the covering dimension of the cube computable, and the nerve of a cover, introduced in *Paracompactness and Partitions of Unity*, is the combinatorial object whose dimension is one less than the order of the cover. The facts about manifolds used here — that a manifold is locally Euclidean, second countable and Hausdorff, and that it is topologically homogeneous near a point — lie outside this article; the dimension theory of the manifold is the covering dimension of its underlying topological space, and the manifold structure enters only through the local Euclidean model. No measure, integral or analytic limit is used, and no physics is invoked. The homological proofs of the invariance of dimension belong to the algebraic topology category that follows in this Part, and the arguments here are the point-set ones.

## The Covering Dimension

### The Order of a Cover and the Definition

**Definition.** Let $\mathcal{U}$ be a family of subsets of a set $X$. The **order** of $\mathcal{U}$ at a point $x \in X$ is the number of members of $\mathcal{U}$ containing $x$, and the **order** of $\mathcal{U}$ is the supremum of these numbers over $X$. A family is **point-finite** if its order is finite at every point. A cover $\mathcal{V}$ **refines** $\mathcal{U}$ if every member of $\mathcal{V}$ is contained in a member of $\mathcal{U}$.

**Definition.** Let $X$ be a topological space and $n \geq -1$ an integer, with the convention that the empty family has order $0$. Then $\dim X \leq n$ if every finite open cover of $X$ has a finite open refinement of order at most $n+1$. The **covering dimension**, or **Lebesgue dimension**, is
$$
\dim X = \min \{ n : \dim X \leq n \},
$$
and $\dim X = \infty$ when the set of such $n$ is empty. The convention gives $\dim \emptyset = -1$, and a nonempty space with $\dim X \leq 0$ is called **zero-dimensional**.

The offset by one between the dimension and the order is the reason the dimension of the cube will come out as $n$ rather than $n+1$: a point of the cube lies in at most $n+1$ members of a suitable grid cover, and this is the least such number.

**Example (zero-dimensional spaces).** A space has $\dim X \leq 0$ exactly when every finite open cover has a refinement by pairwise disjoint open sets, and for a $T_1$ space this is equivalent to having a base of clopen sets, that is, of open sets with empty boundary. Every discrete space is zero-dimensional, the Cantor set is zero-dimensional, and the rationals are zero-dimensional because the intervals with irrational endpoints form a base of clopen sets. The compact metrisable zero-dimensional spaces are exactly the closed subspaces of the Cantor set, by Brouwer's theorem on the Cantor set, and the countably infinite metric zero-dimensional spaces without isolated points are exactly the rationals, by the theorem of Sierpiński quoted in *Baire Spaces and Category*.

**Example (the interval).** The unit interval $I = [0,1]$ has $\dim I = 1$. It is not zero-dimensional, since it is connected and a connected space with more than one point has no clopen separation, and it has a finite open refinement of order $2$ of every finite open cover: take a Lebesgue number $\delta$ of the cover, subdivide $I$ into intervals of length less than $\delta$, and use the two open sets obtained by joining consecutive intervals at overlapping endpoints.

### The Lebesgue Covering Lemma

**Lemma (Lebesgue number).** Let $(X,d)$ be a compact metric space and let $\mathcal{U}$ be an open cover of $X$. Then there is a number $\delta > 0$, a **Lebesgue number** of the cover, such that every subset of $X$ of diameter less than $\delta$ is contained in some member of $\mathcal{U}$.

**Proof.** If no such $\delta$ existed, then for each $n$ there would be a set $A_n$ of diameter less than $1/n$ meeting the complement of every member of $\mathcal{U}$; choose $x_n \in A_n$ and pass to a convergent subsequence with limit $x$, using compactness. The point $x$ lies in some $U \in \mathcal{U}$, and a ball $B(x, \varepsilon) \subseteq U$ captures all but finitely many of the $x_n$; for $n$ large, $A_n \subseteq B(x,\varepsilon)$ because its diameter is small and it contains a point close to $x$, contradicting that $A_n$ meets the complement of $U$. $\square$

**Theorem (Lebesgue covering theorem).** Let $n \geq 1$ and let the cube $I^n$ be covered by finitely many closed sets each of diameter less than $1$. Then some point of $I^n$ lies in at least $n+1$ of the sets.

The proof is by induction on $n$, the case $n=1$ being the statement that a closed cover of an interval by small closed sets must overlap, and the inductive step being the classical argument of Lebesgue with a subdivision of the cube into $2^n$ subcubes and the pigeonhole principle. The theorem is standard, and the proof is in the literature on dimension theory; the present article uses it as the lower bound for $\dim I^n$.

**Theorem.** $\dim I^n = n$ for every $n \geq 0$.

**Proof.** For $\dim I^n \leq n$, let $\mathcal{U}$ be a finite open cover of $I^n$ and let $\delta$ be a Lebesgue number of it. The cube is a polyhedron, so it can be triangulated with mesh less than $\delta/2$; let $\mathcal{V}$ be the cover by the *open stars* of the vertices of the triangulation, an open star of a vertex $v$ being the union of the open simplices that meet $v$. A set of diameter less than $\delta$ lies in a member of $\mathcal{U}$ by the choice of $\delta$, and each open star has diameter at most twice the mesh, hence less than $\delta$; so $\mathcal{V}$ refines $\mathcal{U}$. A point in the interior of a simplex lies in the open star of exactly the vertices of that simplex, and a simplex of the $n$-dimensional triangulation has at most $n+1$ vertices, so the order of $\mathcal{V}$ is at most $n+1$. Hence $\dim I^n \leq n$. For $\dim I^n \geq n$, cover $I^n$ by finitely many open sets of diameter less than $1$, and suppose a finite open refinement $\mathcal{W}$ of order at most $n$ existed. Shrink $\mathcal{W}$, keeping the index set, to a closed cover $\mathcal{F} = (F_W)_{W \in \mathcal{W}}$ with $F_W \subseteq W$, which is possible by the shrinking lemma of *Paracompactness and Partitions of Unity* since $I^n$ is compact Hausdorff; each $F_W$ refines $\mathcal{U}$ and so has diameter less than $1$, and since $F_W \subseteq W$ the order of $\mathcal{F}$ is at most the order of $\mathcal{W}$, hence at most $n$, so no point lies in $n+1$ of the sets of $\mathcal{F}$, contradicting the Lebesgue covering theorem. Hence $\dim I^n \geq n$. $\square$

**Remark.** The two halves of the proof use the two halves of the theory. The upper bound is the refinement by the open stars of a sufficiently fine triangulation, and the lower bound converts a combinatorial statement about closed covers into a statement about open refinements, the conversion being the shrinking lemma of the paracompactness article. The Lebesgue covering lemma enters the upper bound through the Lebesgue number, and it is the point at which the compactness of the cube and the metric on it are used; for a general compact space without a metric the argument is replaced by the inductive definitions.

### The Nerve and the Combinatorial Form

**Definition.** Let $\mathcal{U} = (U_s)_{s \in S}$ be a finite cover. The **nerve** $N(\mathcal{U})$ is the abstract simplicial complex with vertex set $S$ whose simplices are the finite subsets $\sigma \subseteq S$ with $\bigcap_{s \in \sigma} U_s \neq \emptyset$. The **dimension** of an abstract simplicial complex is one less than the maximum number of vertices of its simplices.

**Proposition.** The order of a finite cover $\mathcal{U}$ equals $\dim N(\mathcal{U}) + 1$. Hence $\dim X \leq n$ if and only if every finite open cover of $X$ has a finite open refinement whose nerve has dimension at most $n$.

**Proof.** A point of order $k$ lies in $k$ members, and the corresponding set of $k$ vertices is a simplex of $N(\mathcal{U})$ of dimension $k-1$; conversely a simplex of dimension $k-1$ has $k$ vertices with a common point. The second statement is the first applied to every refinement. $\square$

**Remark.** The nerve turns the covering dimension into a combinatorial dimension, and the nerve theorem of algebraic topology — that the nerve of a suitable cover is homotopy equivalent to the space — converts the covering statements into statements about simplicial complexes. The nerve theorem belongs to the algebraic topology category of this Part, where the homotopy and the homology it needs are available; the present article uses only the correspondence between the order of a cover and the dimension of its nerve.

## The Inductive Dimensions

### The Definitions

**Definition.** The **small inductive dimension** $\operatorname{ind} X$ is defined by the following recursion. First $\operatorname{ind} \emptyset = -1$; then $\operatorname{ind} X \leq n$ if every point $x \in X$ has a neighbourhood base of open sets $U$ with $\operatorname{ind} \partial U \leq n-1$, where $\partial U = \overline{U} \setminus U$ is the boundary; and $\operatorname{ind} X = \min\{n : \operatorname{ind} X \leq n\}$.

**Definition.** The **large inductive dimension** $\operatorname{Ind} X$ is defined by the following recursion. First $\operatorname{Ind} \emptyset = -1$; then $\operatorname{Ind} X \leq n$ if for every closed set $A \subseteq X$ and every open set $V \supseteq A$ there is an open set $U$ with
$$
A \subseteq U \subseteq \overline{U} \subseteq V, \qquad \operatorname{Ind} \partial U \leq n-1 ,
$$
and $\operatorname{Ind} X = \min\{n : \operatorname{Ind} X \leq n\}$.

**Proposition.** For every space $X$, $\operatorname{ind} X \leq \operatorname{Ind} X$.

**Theorem.** Let $X$ be a normal space. Then $\dim X \leq \operatorname{Ind} X$; if $X$ is metrisable then $\operatorname{Ind} X = \dim X$; and if $X$ is compact Hausdorff then $\dim X \leq \operatorname{ind} X \leq \operatorname{Ind} X$.

**Proof sketch.** The inequality $\dim X \leq \operatorname{Ind} X$ for normal $X$ is due to P. S. Aleksandrov and is proved by induction on $n$ using the characterisation of $\dim X \leq n$ by the extension of maps into the $n$-sphere: a map from a closed subspace into $S^n$ extends over $X$ when $\dim X \leq n$, and the large inductive dimension $\operatorname{Ind} X \leq n$ is equivalent to the same extension property for a normal space. The equality $\operatorname{Ind} X = \dim X$ for metrisable $X$ is the theorem of Katětov, and the chain for compact Hausdorff spaces is Aleksandrov's; both are proved in the standard references by the same induction, using the compactness to pass between covers and neighbourhoods. $\square$

**Theorem (Menger–Urysohn; Urysohn).** For every separable metrisable space $X$,
$$
\operatorname{ind} X = \operatorname{Ind} X = \dim X .
$$
The theorem is due to Menger and Urysohn, and it is stated in the classical form for normal spaces with a countable base, which are exactly the separable metrisable spaces by Urysohn's metrisation theorem. Its proof is by simultaneous induction on the three definitions, and it is the central theorem of the classical dimension theory. The proof is in the standard references.

**Corollary (Nöbeling–Pontryagin).** Every separable metrisable space of finite covering dimension embeds as a subspace of a Euclidean space; more precisely, by the Menger–Nöbeling theorem, every compact metrisable space of dimension $n$ embeds in $\mathbb{R}^{2n+1}$. The first statement is the topological characterisation of the separable metrisable finite-dimensional spaces, and the second is the quantitative embedding theorem; both are proved by an approximation argument that places the space in general position, and the proof is in the standard references.

**Remark.** Outside the separable metrisable class the three dimensions can differ, and the inequalities of the preceding theorem are the whole of the general comparison. Roy's space is a metrisable space with $\operatorname{ind} = 0$ and $\operatorname{Ind} = \dim = 1$, so the equality of the Menger–Urysohn theorem genuinely needs separability and not only metrisability; Filippov's examples are compact Hausdorff spaces in which the two inductive dimensions differ, so the chain $\dim \leq \operatorname{ind} \leq \operatorname{Ind}$ for compact spaces is not the equality; and there are normal spaces in which $\dim X < \operatorname{Ind} X$. At dimension zero there is no room for a discrepancy: $\dim X = 0$ is equivalent to $\operatorname{Ind} X = 0$ for every space. The phenomenon is that the inductive dimensions are sensitive to the local structure of boundaries while the covering dimension is sensitive to the global refinement of covers, and the three agree only under hypotheses strong enough to pass between the local and the global descriptions.

### Zero-Dimensional Spaces

**Theorem.** For a nonempty space $X$ the following are equivalent:

**(i)** $\dim X = 0$;

**(ii)** every finite open cover has a finite open refinement by pairwise disjoint open sets;

**(iii)** every finite open cover has a refinement by clopen sets.

Moreover, for every space $X$ the equality $\dim X = 0$ is equivalent to $\operatorname{Ind} X = 0$, and for a regular space it is equivalent to $\operatorname{ind} X = 0$.

**Proof.** (i) $\Leftrightarrow$ (ii): a refinement of order at most $1$ is a family of pairwise disjoint sets, since a point in two members would have order at least $2$; conversely a pairwise disjoint refinement has order $1$. (ii) $\Leftrightarrow$ (iii): a family of pairwise disjoint open sets covering $X$ is a family of clopen sets, since each member is the complement of the union of the others; conversely a cover by clopen sets is pairwise disjoint after removing redundancies. The comparison with the inductive dimensions is the statement that a base of clopen sets is exactly a base of sets with empty boundary, which is $\operatorname{ind} X = 0$ in a regular space, and the equivalence of $\dim X = 0$ with $\operatorname{Ind} X = 0$ is the standard zero-dimensionality theorem. $\square$

**Example.** The Cantor set is zero-dimensional, compact and metrisable, and is the unique such space that is perfect, that is, has no isolated points; it is the projectively universal zero-dimensional compact metrisable space, in the sense that every zero-dimensional compact metrisable space embeds in it. The Baire space of sequences $\mathbb{N}^{\mathbb{N}}$ of *Baire Spaces and Category* is zero-dimensional and completely metrisable, and every zero-dimensional separable metrisable space embeds in it. The two embeddings are the standard universal embedding theorems of the theory.

## The Sum, Subspace and Product Theorems

### Monotonicity and the Sum Theorem

**Theorem (subspace theorem).** If $A \subseteq X$ then $\dim A \leq \dim X$.

**Proof.** Let $\mathcal{U}$ be a finite open cover of $A$ and write each member as $U_i \cap A$ with $U_i$ open in $X$. Since $\dim X \leq n$, the open cover $\{U_i\} \cup \{X \setminus A\}$ of $X$ has a finite open refinement of order at most $n+1$; intersecting with $A$ gives a finite open refinement of $\mathcal{U}$ of order at most $n+1$. $\square$

**Theorem (countable sum theorem).** Let $X$ be a separable metrisable space that is the countable union of closed subspaces $X_k$ with $\dim X_k \leq n$ for all $k$. Then $\dim X \leq n$.

**Proof sketch.** The theorem is proved by the technique of the *dimension-preserving* refinement: for each finite open cover of $X$, construct by recursion on $k$ a refinement whose restriction to $X_k$ has order at most $n+1$, using the induction hypothesis on the closed set $X_k$ and the normality of $X$ to extend the refinement from the partial union. The separability enters in making the family of covers countable, so that the recursive construction can be run over a countable dense set of conditions. The result is due to Urysohn and Menger, and the proof is in the standard references. $\square$

**Corollary.** A separable metrisable space that is a countable union of zero-dimensional closed subspaces is zero-dimensional; the irrationals and the rationals are zero-dimensional; and a countable metrisable space is zero-dimensional.

### The Product Theorem

**Theorem (product theorem; Menger, Hurewicz).** Let $X$ and $Y$ be separable metrisable spaces with $\dim X \leq m$ and $\dim Y \leq n$. Then
$$
\dim (X \times Y) \leq m + n .
$$

**Proof sketch.** Let $\mathcal{U}$ be a finite open cover of $X \times Y$; refine it by a finite cover of the form $(U_i \times V_{i,j})_{i,j}$ with $U_i$ open in $X$ and $V_{i,j}$ open in $Y$. The family $(U_i)$ is a finite open cover of $X$; refine it to a finite open cover of order at most $m+1$, and for each $i$ apply the hypothesis $\dim Y \leq n$ to the finite cover of $Y$ by the sets $V_{i,j}$ to obtain a finite open cover of $Y$ of order at most $n+1$. The family of products of the refined members is then a finite open cover of $X \times Y$ refining $\mathcal{U}$, and its order is at most $m+n+1$. The naive order of the product of a cover of order $m+1$ with one of order $n+1$ is $(m+1)(n+1)$, and the reduction to $m+n+1$ is the substance of the theorem: it is obtained by the sum theorem applied to the fibres of the projection onto $X$, which lets the refinement in the $Y$-direction be chosen independently over the members of the refinement in the $X$-direction. Hence $\dim (X \times Y) \leq m+n$. $\square$

**Corollary.** $\dim (I^m \times I^n) = m+n$, so $\dim I^{m+n} = m+n$; the dimension of the product of the cubes is additive.

**Remark.** The product theorem is the reason the dimension is the exponent in the products of cubes, and the inequality $\dim(X \times Y) \leq \dim X + \dim Y$ is the dimension-theoretic form of the statement that independent directions add. The inequality is not an identity: there exist compact metric spaces with $\dim(X \times Y) < \dim X + \dim Y$, the classical examples being those of Pontryagin, so the equality in the theorem is not a general identity but a property of the cubes and of the spaces that contain them.

### Infinite Dimension

**Definition.** A space has **infinite dimension** if $\dim X \leq n$ fails for every $n$, and then one writes $\dim X = \infty$. A space is **strongly infinite-dimensional** if it contains closed subspaces of every finite dimension, and **weakly infinite-dimensional** if it is the countable union of finite-dimensional closed subspaces.

**Example.** The space $\mathbb{R}^\infty = \bigcup_n \mathbb{R}^n$ of finite-support sequences with the subspace topology from $\mathbb{R}^{\mathbb{N}}$ is separable metrisable, and it contains each $\mathbb{R}^n$ as a closed subspace; by the subspace theorem $\dim \mathbb{R}^\infty \geq n$ for every $n$, hence $\dim \mathbb{R}^\infty = \infty$. It is nevertheless weakly infinite-dimensional, being a countable union of its finite-dimensional closed subspaces, and this shows that the countable sum theorem needs its uniform bound: a countable union of finite-dimensional closed subspaces whose dimensions are unbounded need not be finite-dimensional, and no statement of the form $\dim X \leq \sup_k \dim X_k$ holds for such a union. The Hilbert cube $I^\infty$ of *Metric, Uniform and Complete Spaces* is compact, metrisable and infinite-dimensional, and it contains a copy of every separable metrisable space; the finer invariants of infinite-dimensional spaces, among them the cohomological dimension and the compactly finite dimension, belong to the algebraic topology of this Part, where the cohomology they use is available.

## The Invariance of Dimension

### Euclidean Spaces

**Theorem (invariance of dimension).** If $\mathbb{R}^m$ and $\mathbb{R}^n$ are homeomorphic, then $m = n$. More generally, if a nonempty open subset of $\mathbb{R}^m$ is homeomorphic to an open subset of $\mathbb{R}^n$, then $m = n$.

**Proof.** Both spaces are separable metrisable, so by the Menger–Urysohn theorem their dimensions are intrinsic. The dimension of the Euclidean space is local and finite: $\dim \mathbb{R}^n = n$, because $\mathbb{R}^n$ is the countable union of the closed cubes $[-k,k]^n$ of dimension $n$ and the countable sum theorem gives $\dim \mathbb{R}^n \leq n$, while the subspace theorem applied to the embedded cube gives $\dim \mathbb{R}^n \geq n$. A homeomorphism preserves the dimension, so $m = n$. For the local statement, restrict the homeomorphism to a small ball and use the subspace and local character of the covering dimension. $\square$

**Theorem (invariance of domain).** Let $U \subseteq \mathbb{R}^n$ be open and let $f : U \to \mathbb{R}^n$ be injective and continuous. Then $f(U)$ is open in $\mathbb{R}^n$ and $f$ is an embedding.

The theorem is due to Brouwer and is the local form of the invariance of dimension; the standard proofs use the Brouwer fixed point theorem or the degree of a map of spheres, both of which belong to the algebraic topology of this Part. The present article records the statement and the fact that it is equivalent to the invariance of dimension for open subsets.

### Manifolds and the Local Character

**Definition.** A **topological $n$-manifold** is a second countable Hausdorff space in which every point has a neighbourhood homeomorphic to an open subset of $\mathbb{R}^n$.

**Theorem.** A topological $n$-manifold has $\dim M = n$.

**Proof.** The covering dimension is locally determined for a separable metrisable space: a finite open cover of $M$ can be refined by a locally finite cover by coordinate neighbourhoods, each homeomorphic to an open subset of $\mathbb{R}^n$ of dimension $n$, and the countable sum theorem applied to a locally finite shrinking gives $\dim M \leq n$. Conversely the subspace theorem applied to a coordinate neighbourhood, which has dimension $n$, gives $\dim M \geq n$. $\square$

**Corollary.** The dimension of a manifold is a topological invariant, so a connected topological manifold homeomorphic to both an $m$-manifold and an $n$-manifold has $m=n$. The result is the reason the dimension of a manifold can be read from the local Euclidean model, and it is the input to the classification of manifolds by dimension that the geometry articles use.

**Remark.** The manifold facts — the existence of the locally finite cover by coordinate neighbourhoods, the homeomorphism types of Euclidean open sets, and the topological homogeneity of a manifold — belong. The dimension-theoretic content is the invariance of dimension and the countable sum theorem, and the two combine into the statement that a manifold's dimension is intrinsic. The same input is used in the dimension theory of the topological groups of the next category, where the dimension of a locally compact group is computed from the dimension of a neighbourhood of the identity.

## Summary

The **covering dimension** $\dim X$ is the least $n$ such that every finite open cover of $X$ has a finite open refinement of order at most $n+1$, the order of a family being the largest number of members containing a common point. The **small inductive dimension** $\operatorname{ind}$ and the **large inductive dimension** $\operatorname{Ind}$ are defined by the boundaries of neighbourhoods of points and of closed sets. For a separable metrisable space the three agree, by the Menger–Urysohn theorem; outside that class they differ, the counterexamples being Roy's metrisable space, in which $\operatorname{ind}=0$ while $\operatorname{Ind}=\dim=1$, and the compact Hausdorff spaces of Filippov in which the two inductive dimensions differ. A space is zero-dimensional exactly when every finite open cover has a refinement by pairwise disjoint open sets, and for a $T_1$ space this is equivalent to having a base of clopen sets; the zero-dimensional compact metrisable spaces are the closed subspaces of the Cantor set.

The **Lebesgue covering lemma** gives a Lebesgue number to every open cover of a compact metric space, and the **Lebesgue covering theorem** states that in every closed cover of the cube $I^n$ by finitely many sets of diameter less than $1$ some point lies in at least $n+1$ sets. Together they give $\dim I^n = n$: the upper bound by an explicit cubical refinement, the lower bound by the shrinking lemma and the covering theorem. The dimension is monotone in subspaces, is controlled by the countable sum theorem on countable unions of closed subspaces, and satisfies $\dim (X \times Y) \leq \dim X + \dim Y$ for separable metrisable spaces with equality for the cubes; the equality fails for general spaces: there are compact metric spaces with $\dim (X \times Y) < \dim X + \dim Y$, the classical examples being those of Pontryagin. The **invariance of dimension** states that homeomorphic open subsets of Euclidean spaces have the same dimension, and the **invariance of domain** states that an injective continuous map from an open subset of $\mathbb{R}^n$ into $\mathbb{R}^n$ is open; both belong to Brouwer's theorems of 1911, and the homological proofs belong to the algebraic topology of this Part. A topological $n$-manifold has covering dimension $n$, by the countable sum theorem over the coordinate neighbourhoods and the invariance of dimension, so the dimension of a manifold is intrinsic.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $I = [0,1]$ | Closed unit interval; $I^n$ the $n$-cube |
| $\mathcal{U}, \mathcal{V}, \mathcal{W}$ | Open covers; $\mathcal{V}$ refines $\mathcal{U}$ |
| order of $\mathcal{U}$ | Supremum over points of the number of members containing the point |
| $\dim X$ | Covering (Lebesgue) dimension |
| $\operatorname{ind} X$ | Small inductive dimension |
| $\operatorname{Ind} X$ | Large inductive dimension |
| $\dim X = \infty$ | $\dim X \leq n$ fails for every $n$ |
| zero-dimensional | $\dim X \leq 0$; every finite open cover refines to pairwise disjoint open sets, equivalently a base of clopen sets for $T_1$ spaces |
| $\partial U$ | Boundary $\overline{U} \setminus U$ of $U$ |
| $N(\mathcal{U})$ | Nerve of the cover $\mathcal{U}$; $\operatorname{order}\mathcal{U} = \dim N(\mathcal{U}) + 1$ |
| $X_k$, $I^\infty$, $\mathbb{R}^\infty$ | Summands of the countable sum theorem; Hilbert cube; direct limit of the Euclidean spaces |
| $M$ | Topological $n$-manifold, with $\dim M = n$ |





## Further Reading

- Ryszard Engelking, *Theory of Dimensions, Finite and Infinite* (Heldermann, 1995), for the covering and inductive dimensions, the sum and product theorems, and the infinite-dimensional theory.
- Ryszard Engelking, *General Topology* (Heldermann, revised ed. 1989), for the point-set background, the Lebesgue covering lemma and the nerve.
- Witold Hurewicz and Henry Wallman, *Dimension Theory* (Princeton, 1941), for the classical Menger–Urysohn theory and the invariance of dimension.
- Karl Menger, *Dimensionstheorie* (Teubner, 1928), for the original development of the covering and inductive dimensions.
- Paul S. Alexandrov and Boris A. Pasynkov, *Introduction to Dimension Theory* (Nauka, 1973), for the general theory and the counterexamples separating the three dimensions.
- L. E. J. Brouwer, "Über den natürlichen Dimensionsbegriff", *Journal für die reine und angewandte Mathematik* 142 (1913), 146–152, for the invariance of dimension.
- Prabir Roy, "Nonequality of Dimensions for Metric Spaces", *Transactions of the American Mathematical Society* 134 (1968), 117–132, for the metric space with $\operatorname{ind} = 0$ and $\dim = 1$.
- Kiyoshi Nagami, "Dimension Theory with Respect to Various Covers", *Fundamenta Mathematicae* 72 (1971), for the infinite-dimensional and cohomological refinements.
