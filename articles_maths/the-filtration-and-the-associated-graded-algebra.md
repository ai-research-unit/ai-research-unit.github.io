
# __The Filtration and the Associated Graded Algebra__

## Introduction

The Clifford algebra is not graded by the number of its generators, but it is filtered by it: the products of at most $k$ vectors form an increasing chain of subspaces $F_0\subseteq F_1\subseteq F_2\subseteq\cdots$, closed under multiplication in the sense that $F_jF_l\subseteq F_{j+l}$. Passing to the successive quotients of that chain produces a graded algebra, and the content of the theorem of Poincaré–Birkhoff–Witt for Clifford algebras is that this graded algebra is the exterior algebra of $V$. The theorem is the reason the exterior algebra and the Clifford algebra have the same dimension, and it is what makes the antisymmetrisation map of *The Geometric Product and the Grade Decomposition* an isomorphism rather than merely an injection.

This article develops the filtration, proves the theorem, and separates two statements that are often run together: the filtration of the Clifford algebra exists for every quadratic form, degenerate ones included, and its associated graded algebra is always the exterior algebra; whereas its identification with the cumulative sum of the graded pieces of *The Geometric Product and the Grade Decomposition* requires the form to be non-degenerate. The parallel with the universal enveloping algebra, where the symmetric algebra plays the role that the exterior algebra plays here, closes the article.

The Clifford algebra, its universal property and the defining relation $v^2=q(v)$ are from *The Clifford Algebra*; the basis of products of distinct generators, the $k$-vectors, the multivectors and the volume element are from *Clifford Algebras in Finite Dimensions*; the reduction of a degenerate form to its non-degenerate part and its radical is from *Degenerate Clifford Algebras and the Radical*; the wedge product, the graded-commutativity and the exterior powers are from *The Exterior Algebra* and *Exterior Powers*; the grade decomposition, the grade projection and the symbol map are from *The Geometric Product and the Grade Decomposition*. Nothing owned by those entries is re-derived. The base is a field $F$, the space $V$ is finite-dimensional of dimension $n$, and $q$ is a quadratic form on $V$ with polar form $B$, not assumed non-degenerate until it is stated.

## The Length Filtration

### The Filtration Subspaces

**Definition.** For $k\ge0$ let $F_k$ be the subspace of $\mathrm{Cl}(V,q)$ spanned by the products $v_1v_2\cdots v_j$ with $j\le k$ and $v_1,\ldots,v_j\in V$. The chain

$$
F_0\subseteq F_1\subseteq F_2\subseteq\cdots, \qquad \bigcup_{k\ge0}F_k=\mathrm{Cl}(V,q),
$$

is the **length filtration**. It is **increasing** because the generating products of $F_k$ are among those of $F_{k+1}$, and it is **exhaustive** by the universal property; the scalars lie in every $F_k$, so $\bigcap_kF_k=F_0=F\cdot1$ for every $q$, degenerate ones included.

**Proposition.** $F_0=F\cdot1$ and $F_1=F\oplus V$.

**Proof.** The products of no vectors are the scalars of the algebra, and those of at most one vector span the scalars together with $V$. $\square$

**Theorem.** The filtration is compatible with the product: $F_jF_l\subseteq F_{j+l}$ for all $j,l$.

**Proof.** It suffices to multiply a product of $j$ vectors by a product of $l$ vectors, which is a product of $j+l$ vectors. $\square$

A filtered algebra is one carrying such a chain, and the theorem is the only compatibility the definition requires.

### Why the Filtration Is Not a Grading

The product of an element of $F_j$ with one of $F_l$ lies in $F_{j+l}$, but its component of exact length $j+l$ need not exhaust it: the relation $uv+vu=2B(u,v)$ converts a product of two vectors into a scalar plus a bivector, hence a product of two vectors into a sum of an element of $F_0$ and an element of $F_2$. So the spaces spanned by the products of a fixed length do not form a grading of the algebra, and the filtration is strictly finer information than any single grade. The algebra is a **deformation** of the exterior algebra in the sense made precise below.

## The Associated Graded Algebra

### Definition

**Definition.** For $k\ge0$ let $\operatorname{gr}_k\mathrm{Cl}(V,q)=F_k/F_{k-1}$, with $F_{-1}=0$, and let

$$
\operatorname{gr}\mathrm{Cl}(V,q)=\bigoplus_{k\ge0}\operatorname{gr}_k\mathrm{Cl}(V,q).
$$

The direct sum is a graded algebra under the product induced by that of $\mathrm{Cl}(V,q)$: for $x\in F_j$ and $y\in F_l$ the class of $xy$ in $\operatorname{gr}_{j+l}$ depends only on the classes of $x$ and of $y$, because a change of either representative by an element of $F_{j-1}$ or $F_{l-1}$ changes $xy$ by an element of $F_{j+l-1}$.

**Proposition.** The induced product on $\operatorname{gr}\mathrm{Cl}(V,q)$ is associative and graded-commutative, with

$$
\bar x\,\bar y=(-1)^{jl}\,\bar y\,\bar x \qquad (\bar x\in\operatorname{gr}_j,\ \bar y\in\operatorname{gr}_l).
$$

**Proof.** Associativity is inherited from the associativity of the product of $\mathrm{Cl}(V,q)$. For the sign, $xy$ and $yx$ differ by $(xy-yx)$, which for $x$ a product of $j$ vectors and $y$ a product of $l$ vectors lies in $F_{j+l-2}$ by repeated application of $uv=-vu+2B(u,v)$; hence $xy-yx$ is of filtration at most $j+l-2$, and only its class in $\operatorname{gr}$ matters, so $\bar x\bar y=(-1)^{jl}\bar y\bar x$. $\square$

### The Theorem of Poincaré–Birkhoff–Witt

**Theorem.** For every quadratic form $q$ the linear map

$$
\Lambda^kV\longrightarrow\operatorname{gr}_k\mathrm{Cl}(V,q), \qquad v_1\wedge v_2\wedge\cdots\wedge v_k\longmapsto\overline{v_1v_2\cdots v_k},
$$

is an isomorphism, and it is an isomorphism of graded algebras from the exterior algebra $\Lambda(V)$ with its wedge product onto $\operatorname{gr}\mathrm{Cl}(V,q)$.

**Proof of well-definedness.** The multilinear map $V^k\to\operatorname{gr}_k$ sending $(v_1,\ldots,v_k)$ to the class of $v_1\cdots v_k$ is alternating: exchanging two adjacent factors changes the product by $2B(v_i,v_{i+1})v_1\cdots\hat v_i\hat v_{i+1}\cdots v_k$, an element of $F_{k-2}\subseteq F_{k-1}$, so the two classes in $\operatorname{gr}_k$ agree up to the sign of the transposition. An alternating multilinear map factors through $\Lambda^kV$. Surjectivity holds because the classes of the products of exactly $k$ vectors span $\operatorname{gr}_k$ by the definition of $F_k$.

**Proof of injectivity for non-degenerate $q$.** Let $e_1,\ldots,e_n$ be an orthogonal basis of $V$. Every product of at most $k$ vectors is a linear combination of the monomials $e_{i_1}\cdots e_{i_j}$ with $j\le k$, since the products of the basis elements span the algebra and reducing a product of vectors to monomials never increases the number of factors. Conversely every such monomial of length $j\le k$ lies in $F_k$, and by the basis theorem of *Clifford Algebras in Finite Dimensions* those monomials are linearly independent in $\mathrm{Cl}(V,q)$; together with $\dim\mathrm{Cl}(V,q)=2^n$ this gives

$$
\dim F_k=\sum_{j=0}^{k}\binom nj, \qquad \dim\operatorname{gr}_k\mathrm{Cl}(V,q)=\binom nk=\dim\Lambda^kV .
$$

A surjective linear map between spaces of equal finite dimension is an isomorphism, so the map is bijective for every $k$. For the multiplication, the top filtration term of a product of a $j$-vector and an $l$-vector is their wedge by the grade theorem of *The Geometric Product and the Grade Decomposition*, so the induced product on $\operatorname{gr}$ is the wedge. $\square$

**Remark (degenerate forms).** Injectivity above uses the basis theorem, which needs the form to be non-degenerate; for a degenerate form the reduction of *Degenerate Clifford Algebras and the Radical* writes $V=\operatorname{Rad}(V,q)\oplus W$ with $q|_W$ non-degenerate and $\mathrm{Cl}(V,q)$ as the Clifford algebra of $W$ contracted with the exterior algebra of the radical, and the same count gives $\dim F_k=\sum_{j\le k}\binom nj$ again. The theorem therefore holds for every quadratic form, which is the reason the filtration, unlike the grade decomposition, is the natural tool in the degenerate case.

## The Relation to the Grade Decomposition

### The Cumulative Filtration

If $q$ is non-degenerate the grade decomposition of *The Geometric Product and the Grade Decomposition* gives a second description of the filtration.

**Proposition.** For $q$ non-degenerate and $k\ge0$,

$$
F_k=\mathrm{Cl}_0(V,q)\oplus\mathrm{Cl}_1(V,q)\oplus\cdots\oplus\mathrm{Cl}_k(V,q),
$$

the sum of the graded pieces of grade at most $k$. Hence $\operatorname{gr}_k\mathrm{Cl}(V,q)\cong\mathrm{Cl}_k(V,q)$ canonically, and the filtration is the **cumulative** filtration of the grading.

**Proof.** Every monomial $e_{i_1}\cdots e_{i_j}$ with $j\le k$ lies in $\mathrm{Cl}_j$, and every $j$-vector with $j\le k$ is a combination of such monomials, so the two sides have the same spanning set; conversely an element of $\mathrm{Cl}_j$ with $j>k$ is not a combination of monomials of length at most $k$, by the independence of the monomials. $\square$

So for a non-degenerate form the filtration adds nothing to the grading: the graded pieces are the grades, and the associated graded algebra is the exterior algebra read through the antisymmetrisation map.

### The Symbol Map Revisited

**Theorem.** Let $\sigma:\Lambda(V)\to\mathrm{Cl}(V,q)$ be the linear isomorphism of *The Geometric Product and the Grade Decomposition* sending a wedge of vectors to their antisymmetrised product. Then the composition of $\sigma$ with the quotient map $F_k\to\operatorname{gr}_k$ is the Poincaré–Birkhoff–Witt isomorphism, and the two isomorphisms $\Lambda(V)\to\operatorname{gr}\mathrm{Cl}(V,q)$ agree.

**Proof.** For a wedge of vectors $v_1\wedge\cdots\wedge v_k$ the antisymmetrisation $\sigma$ is $\frac1{k!}\sum_{\pi}\operatorname{sgn}(\pi)v_{\pi(1)}\cdots v_{\pi(k)}$, each term of which is $v_1\cdots v_k$ plus an element of $F_{k-1}$; so $\sigma$ and the monomial map have the same class in $\operatorname{gr}_k$. $\square$

**Corollary.** The Clifford algebra and the exterior algebra of the same space have the same dimension, $\sum_{k}\binom nk=2^n$, and the symbol map is a linear isomorphism realising the equality.

**Proof.** The associated graded algebra of a filtered vector space has the same dimension as the space, and it is $\Lambda(V)$ by the theorem. $\square$

## The Parallel with the Universal Enveloping Algebra

The construction is the quadratic analogue of a classical one for Lie algebras.

**Theorem.** Let $\mathfrak g$ be a Lie algebra and $U(\mathfrak g)$ its universal enveloping algebra, filtered by the length of the products of elements of $\mathfrak g$. Then the associated graded algebra is the symmetric algebra, $\operatorname{gr}U(\mathfrak g)\cong S(\mathfrak g)$.

**Proof.** This is the Poincaré–Birkhoff–Witt theorem for Lie algebras, as recorded in *Representations of Lie Algebras*. $\square$

The two theorems are read side by side as a dictionary:

| Lie algebra | Clifford algebra |
|---|---|
| Generators $x\in\mathfrak g$ | Generators $v\in V$ |
| Relation $xy-yx=[x,y]$ | Relation $uv+vu=2B(u,v)$ |
| Symmetric normal form | Alternating normal form |
| $\operatorname{gr}U(\mathfrak g)\cong S(\mathfrak g)$ | $\operatorname{gr}\mathrm{Cl}(V,q)\cong\Lambda(V)$ |
| Symmetric algebra | Exterior algebra |
| Commutators lower the length by one | Anticommutators lower the length by two |

The last row is the substantive difference. The commutator of two generators has length one, so the filtration of $U(\mathfrak g)$ is not separated by parity; the anticommutator of two generators is a scalar, of length zero and even, so every filtration step of $\mathrm{Cl}(V,q)$ splits into an even and an odd part, and the parity grading survives the passage to the associated graded algebra. The exterior algebra, not the symmetric one, appears because the Clifford relation is symmetric in the generators and the deformation it performs is a deformation by a quadratic form rather than by a Lie bracket.

## Worked Cases

### One and Two Dimensions

Let $q$ be non-degenerate on $V$ of dimension $1$, with $q(e_1)=a\neq0$. Then $F_0=F$, $F_1=\mathrm{Cl}(V,q)$ and $F_k=\mathrm{Cl}(V,q)$ for $k\ge1$, with $\operatorname{gr}_0\cong F$ and $\operatorname{gr}_1\cong V$, of dimensions $1$ and $1$; the associated graded algebra is $\Lambda(V)=\Lambda^0\oplus\Lambda^1$.

For $\dim V=2$ with orthogonal $e_1,e_2$, the filtration steps are $F_0=F$, $F_1=F\oplus V$ of dimension $3$, and $F_2=\mathrm{Cl}(V,q)$ of dimension $4$; the quotients have dimensions $1,2,1$, the dimensions of $\Lambda^0,\Lambda^1,\Lambda^2$, and the product of the classes of $e_1$ and $e_2$ in $\operatorname{gr}_1$ is the class of $e_1e_2$ in $\operatorname{gr}_2$, which is the exterior product $e_1\wedge e_2$ because $e_1e_2$ and $-e_2e_1$ differ by $2B(e_1,e_2)=0$.

### The Situation When the Form Is Trivial

**Theorem.** If $q=0$ then the filtration is the grading of the exterior algebra in disguise: the canonical map $\Lambda(V)\to\mathrm{Cl}(V,q)$ of *The Clifford Algebra* is an isomorphism of graded algebras, and the filtration steps are $F_k=\bigoplus_{j\le k}\Lambda^jV$.

**Proof.** With $q=0$ the relation becomes $uv=-vu$, so $\mathrm{Cl}(V,0)=\Lambda(V)$ by the cited universal property, and a product of $k$ vectors is a $k$-vector. $\square$

So the theorem of Poincaré–Birkhoff–Witt degenerates to a tautology when the form vanishes, which is the sense in which the exterior algebra is the free or undeformed case of the Clifford algebra.

## Summary

The **length filtration** $F_k$ of $\mathrm{Cl}(V,q)$ is spanned by the products of at most $k$ vectors; it is increasing, exhaustive and compatible with the product, $F_jF_l\subseteq F_{j+l}$, and $F_0=F\cdot1$, $F_1=F\oplus V$. It is a filtration and not a grading, because the defining relation lowers the length of a product: $uv+vu=2B(u,v)$ turns a product of two vectors into a scalar plus a bivector.

The associated graded algebra $\operatorname{gr}\mathrm{Cl}(V,q)=\bigoplus_kF_k/F_{k-1}$ is graded-commutative, and by the theorem of Poincaré–Birkhoff–Witt it is the exterior algebra: the map sending a wedge of vectors to the class of their product is an isomorphism $\Lambda^kV\to\operatorname{gr}_k\mathrm{Cl}(V,q)$, for every quadratic form, degenerate ones included. For a non-degenerate form the dimension count $\dim\operatorname{gr}_k=\binom nk$ follows from the basis theorem, and in the degenerate case from the reduction to the radical. The Clifford algebra and the exterior algebra of the same space therefore have the same dimension $2^n$, and the symbol map of *The Geometric Product and the Grade Decomposition* is the linear isomorphism realising it: it is the Poincaré–Birkhoff–Witt isomorphism read on the antisymmetrised products.

When $q$ is non-degenerate the filtration is the cumulative filtration of the grade decomposition, $F_k=\mathrm{Cl}_0\oplus\cdots\oplus\mathrm{Cl}_k$, so that $\operatorname{gr}_k\cong\mathrm{Cl}_k$ and the filtration carries no information beyond the grading; when $q$ is degenerate the filtration still exists and still has the exterior algebra as its associated graded algebra, and it is then the appropriate substitute for the grading. The construction is the quadratic parallel of the universal enveloping algebra of a Lie algebra, whose associated graded algebra is the symmetric algebra: the commutator $xy-yx$ lowers the length by one, the anticommutator $uv+vu$ by two, and that difference of parity is why the alternating normal form replaces the symmetric one and why the parity grading survives.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F_k$ | Products of at most $k$ vectors |
| $F_jF_l\subseteq F_{j+l}$ | Compatibility of the filtration with the product |
| $\operatorname{gr}_k=F_k/F_{k-1}$ | Successive quotient, $F_{-1}=0$ |
| $\operatorname{gr}\mathrm{Cl}(V,q)$ | Associated graded algebra |
| $\Lambda^kV\to\operatorname{gr}_k$ | Poincaré–Birkhoff–Witt isomorphism |
| $F_k=\bigoplus_{j\le k}\mathrm{Cl}_j$ | Cumulative filtration, $q$ non-degenerate |
| $\sigma$ | Symbol map, the antisymmetrisation |
| $U(\mathfrak g)$, $S(\mathfrak g)$ | Enveloping algebra and symmetric algebra, the parallel case |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the filtration, the associated graded algebra and the proof of the Poincaré–Birkhoff–Witt theorem for Clifford algebras.
- Marcel Riesz, *Clifford Numbers and Spinors* (Kluwer, 1993), for the graded algebra associated with the Clifford algebra and the symbol of a Clifford number.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the filtration, the graded algebra and the exterior algebra.
- Nicolas Bourbaki, *Algebra I* (Springer, 1998), for the general theory of filtered and graded algebras and the Poincaré–Birkhoff–Witt theorem in both the Lie and the Clifford cases.
- Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras*, Collected Works vol. 2 (Springer, 1997), for the filtration and the exterior algebra as its associated graded piece.
