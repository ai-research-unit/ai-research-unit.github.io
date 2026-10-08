# __The Completion of a Clifford Algebra__

## Introduction

The Clifford algebra of an infinite-dimensional quadratic space is filtered by the degree, and the two ways of completing it are not the same: one completes the *filtration*, taking the inverse limit of the bounded-degree quotients, and one completes a *norm*, taking the metric completion of the projective tensor norm. This article treats both completions, proves that the second is a Banach algebra and that the first is a complete topological algebra with the same associated graded algebra, shows that both contain the algebra as a dense subalgebra, and states the universal property that makes each of them the completion of the layer. It closes with the caution that governs the whole category: the **Euclidean** norm of the definite case, in which the blades are orthonormal, does not make the algebra a topological algebra, because it is not submultiplicative and the product is separately but not jointly continuous for it, and the completions that are algebras are the filtration one and the projective or C*-normed one.

The two completions answer two different questions. The **filtration completion** answers the question of convergence of a series whose terms have increasing degree and bounded-degree coefficients, and it is the smallest complete object in which the algebra is dense for the filtration topology of *The Continuous Grade Decomposition and the Filtration*, §*The Completion of the Filtration*; its associated graded algebra is the exterior algebra, unchanged, and it is the home of the infinite sums of *Infinite-Dimensional Clifford Algebras and CAR with Inner Conjugation*. The **norm completion** answers the question of the multiplication: the projective tensor norm of the tensor algebra is submultiplicative, it descends to a seminorm on the Clifford algebra, and the kernel of that seminorm is a two-sided ideal whose quotient is a normed algebra whose completion is a Banach algebra; the choice of norm is the choice of the convergence of the products, and the projective norm is the largest one for which the product is norm-decreasing.

The article owns the completion of the algebra as a topological algebra and no more. The Fock representation, the uniqueness of the vacuum and the C*-completion of the canonical anticommutation relations are *Infinite-Dimensional Clifford Algebras and CAR with Inner Conjugation*; the Euclidean form, the norm of a blade and the Hilbert-space structure are the Hermitian layer, *The Euclidean Form, the Norm and the Completion on a Clifford Algebra*; the operator norms of the one-sided multiplications are the `- Operator Theory` group of this category. The algebraic theory of the filtration is *The Filtration and the Associated Graded Algebra*. Throughout, $F$ is a complete valued field of characteristic $0$, $V$ is a normed space over $F$ with a continuous quadratic form $q$, and $\mathrm{Cl}(V,q)$ is the algebra of *Topological Clifford Algebras*.

## The Two Completions

### The Filtration Completion

**Definition.** Let $\{N_{k}\}$ be the descending chain of elements of degree at least $k$ of *The Continuous Grade Decomposition and the Filtration*, §*The Descending Filtration and its Topology*. The **filtration completion** is

$$
\widehat{\mathrm{Cl}}_{\mathrm{filt}} = \varprojlim_{k}\mathrm{Cl}(V,q)/N_{k} ,
$$

with the inverse-limit topology, the completion of the algebra for the filtration topology.

**Theorem.** The filtration completion is a complete Hausdorff topological algebra when the filtration is separated, the algebra embeds in it as a dense subalgebra, and its associated graded algebra is $\Lambda(V)$:

$$
\operatorname{gr}\widehat{\mathrm{Cl}}_{\mathrm{filt}}\cong\Lambda(V).
$$

*Proof.* This is the proposition of *The Continuous Grade Decomposition and the Filtration*, §*The Completion of the Filtration*; the density is the standard property of an inverse limit over a cofinal family of onto maps, the separatedness is the theorem of the same article that $\bigcap_{k}N_{k}=0$ for a non-degenerate form, and the identification of the associated graded is the invariance of the successive quotients under completion. $\square$

### The Projective Norm and its Submultiplicativity

**Definition.** The **projective tensor norm** on $V^{\otimes n}$ is

$$
\lVert u\rVert_{\pi} = \inf\Bigl\{\sum_{i}\lVert x_{i1}\rVert\cdots\lVert x_{in}\rVert : u = \sum_{i}x_{i1}\otimes\cdots\otimes x_{in}\Bigr\},
$$

the infimum being over all finite representations of $u$ as a sum of elementary tensors; the **projective norm** of an element $u=\sum_{n}u_{n}$ of the tensor algebra is $\lVert u\rVert_{\pi}=\sum_{n}\lVert u_{n}\rVert_{\pi}$.

**Proposition (the tensor algebra is a normed algebra).** The projective norm is a norm on each tensor power, the sum defining the norm of an element of the tensor algebra is finite for every element, and $\lVert uv\rVert_{\pi}\le\lVert u\rVert_{\pi}\lVert v\rVert_{\pi}$ for all $u,v\in T(V)$.

*Proof.* The projective norm on a tensor product of normed spaces is a norm, by the standard theory of the projective tensor product: it is the quotient norm of the free vector space on the elementary tensors, modulo the relations. For an element $u=\sum_{n\le m}u_{n}$ the sum is finite, since an element of the direct sum has finitely many nonzero homogeneous components. For submultiplicativity, if $u=\sum_{i}x_{i1}\otimes\cdots\otimes x_{ip}$ and $v=\sum_{j}y_{j1}\otimes\cdots\otimes y_{jq}$ then $uv=\sum_{i,j}x_{i1}\otimes\cdots\otimes x_{ip}\otimes y_{j1}\otimes\cdots\otimes y_{jq}$, and the norm of each term is the product of the norms, so $\lVert uv\rVert_{\pi}\le(\sum_{i}\prod_{r}\lVert x_{ir}\rVert)(\sum_{j}\prod_{s}\lVert y_{js}\rVert)$; taking infima gives the inequality, and the passage to the direct sum over the degrees multiplies the two sums. $\square$

### The Normed Completion

**Theorem (the norm completion is a Banach algebra).** Let $\lVert\cdot\rVert_{\mathrm{q}}$ be the quotient seminorm on $\mathrm{Cl}(V,q)$ induced by the projective norm, and let $J=\{x : \lVert x\rVert_{\mathrm{q}}=0\}$. Then $J$ is a closed two-sided ideal, the quotient $\mathrm{Cl}(V,q)/J$ is a normed algebra, and its completion

$$
\widehat{\mathrm{Cl}}_{\lVert\cdot\rVert}
$$

is a Banach algebra containing $\mathrm{Cl}(V,q)/J$ as a dense subalgebra.

*Proof.* The quotient seminorm is the infimum of the norms of the representatives, hence submultiplicative because the projective norm is; the set where a seminorm vanishes is a subspace, and it is a two-sided ideal because $\lVert xy\rVert\le\lVert x\rVert\lVert y\rVert$ forces $\lVert xy\rVert=0$ whenever $\lVert x\rVert=0$. The quotient by the kernel of a seminorm is a normed space, and the submultiplicativity descends; the completion of a normed algebra is a Banach algebra, the product extending by continuity and the inequality $\lVert xy\rVert\le\lVert x\rVert\lVert y\rVert$ passing to the limit. $\square$

**Remark (the ideal $J$ and the radical).** The ideal $J$ is the closure of zero for the projective norm, and it is the analogue for the norm of the ideal of *Topological Clifford Algebras*, §*The Closure of Zero and the Hausdorff Quotient* for the quotient topology of the tensor algebra; the three ideals — the closure of zero for the quotient topology, the ideal $J$ of the projective norm, and the intersection $\bigcap_{k}N_{k}$ of the filtration — are in general distinct, and the reader should not expect them to agree. What is true in every case is that each is a two-sided ideal and that the quotient is Hausdorff for the corresponding topology.

## The Comparison of the Two Completions

**Theorem (finite dimension).** Let $V$ be finite-dimensional over a complete valued field and $q$ non-degenerate. Then $N_{k}=0$ for $k>n$, the filtration topology is discrete, and both completions are the algebra itself:

$$
\widehat{\mathrm{Cl}}_{\mathrm{filt}}=\widehat{\mathrm{Cl}}_{\lVert\cdot\rVert}=\mathrm{Cl}(V,q).
$$

*Proof.* The filtration topology is discrete by *The Continuous Grade Decomposition and the Filtration*, §*The Quotients and the Separation*, so the algebra is complete for it and the inverse limit stabilizes; a finite-dimensional normed space over a complete field is complete, so the norm completion is the algebra itself; and the projective seminorm is a norm in finite dimension, since the projective norm is equivalent to the unique norm of the finite-dimensional tensor powers. $\square$

**Remark (infinite dimension).** In infinite dimension the two completions differ in general, and neither is contained in the other as a subalgebra without a hypothesis: the filtration completion is an inverse limit and carries the elements of degree tending to infinity with bounded-degree coefficients, while the norm completion carries the elements whose projective norm is finite. They coincide when the two topologies have the same Cauchy filters on the algebra, and the article asserts nothing more; the identification of cases is a matter of the particular space and form, and the Cauchy criterion for the projective norm is the classical one of the absolute convergence of the coefficient series.

## The Universal Property

**Theorem (the universal property of the norm completion).** Let $A$ be a Banach algebra over $F$ and let $\varphi : \mathrm{Cl}(V,q)\to A$ be a continuous algebra homomorphism with $\lVert\varphi(x)\rVert\le C\lVert x\rVert_{\mathrm{q}}$ for some constant $C$ and all $x$. Then $\varphi$ factors uniquely through a continuous algebra homomorphism $\widehat{\mathrm{Cl}}_{\lVert\cdot\rVert}\to A$ of norm at most $C$.

*Proof.* A homomorphism bounded by the seminorm $\lVert\cdot\rVert_{\mathrm{q}}$ kills $J$, hence descends to $\mathrm{Cl}(V,q)/J$; a uniformly continuous map into a complete Hausdorff space extends uniquely by continuity to the completion, and the inequality $\lVert\varphi(x)\rVert\le C\lVert x\rVert$ passes to the limit, bounding the extension. The extension is multiplicative on a dense subalgebra, and a continuous bilinear map is determined by its values on a dense set, so the extension is multiplicative. $\square$

**Remark (the universal property of the filtration completion).** The filtration completion has the analogous property for the filtration topology: a homomorphism continuous for a filtration topology, that is one bounded on some $N_{k}$ in the sense that $\varphi(N_{k})\subseteq\{a : \lVert a\rVert<1\}$, factors through $\widehat{\mathrm{Cl}}_{\mathrm{filt}}$. The statement is the standard universal property of an inverse limit and is the reason the completion is the right object to receive the series that appear in the applications.

## The Associated Graded Algebra and the Series

**Proposition.** Let $\widehat{N}_{k}$ be the closure in the norm completion of the image of $N_{k}$. Then $\widehat{N}_{j}\widehat{N}_{l}\subseteq\widehat{N}_{j+l}$, and the associated graded algebra of $\widehat{\mathrm{Cl}}_{\lVert\cdot\rVert}$ for this filtration is a **quotient** of the exterior algebra degree by degree:

$$
\widehat{N}_{k}/\widehat{N}_{k+1} \quad\text{is a quotient of}\quad \Lambda^{k}V .
$$

*Proof.* The inclusion is the closure of the multiplicative inclusion $N_{j}N_{l}\subseteq N_{j+l}$, the product in the completion being continuous. The projection to the quotient induces an onto map $N_{k}\to\widehat{N}_{k}/\widehat{N}_{k+1}$, and this map kills $N_{k+1}$ because $N_{k+1}\subseteq\widehat{N}_{k+1}$; hence the quotient is an image of $N_{k}/N_{k+1}\cong\Lambda^{k}V$, and the multiplicativity descends because the wedge product is the product of the associated graded of the algebra. $\square$

**Theorem (convergence and the exponential).** Let the base be $\mathbb{R}$ or $\mathbb{C}$ and let $\widehat{A}$ be either completion of the algebra. Then every absolutely convergent series $\sum_{n}x_{n}$ with $\sum_{n}\lVert x_{n}\rVert<\infty$ converges in $\widehat{A}$, the geometric series $\sum_{n\ge0}t^{n}$ converges for $\lVert t\rVert<1$ with sum $(1-t)^{-1}$, and for every $v\in V$ the exponential

$$
\exp(v) = \sum_{n\ge0}\frac{v^{n}}{n!}
$$

converges in the norm completion, because $\lVert v^{n}/n!\rVert\le\lVert v\rVert^{n}/n!$ and the numerical series converges.

*Proof.* In a complete normed algebra an absolutely convergent series converges, by the comparison of the partial sums with a Cauchy sequence; the geometric series is estimated by $\lVert t^{n}\rVert\le\lVert t\rVert^{n}$; and the exponential by the estimate displayed, which uses the submultiplicativity and the completeness of the scalar field. $\square$

**Remark (the exponential in the filtration completion).** The exponential also converges in the filtration completion, and no norm is needed to see it: the $n$-th term $v^{n}/n!$ lies in $N_{n}$, because each of the $n$ factors lies in $N_{1}$ and the product of $n$ elements of $N_{1}$ lies in $N_{n}$; consecutive partial sums therefore differ by an element of $N_{n}$ for some $n$, which is exactly the Cauchy condition for the filtration topology. The convergence of the power series is thus a statement of the filtration, which is why the filtration completion is the natural object for it.

## The Euclidean Norm and the Failure of Joint Continuity

**Remark (the caution).** The algebra of a definite real form carries a natural **Euclidean** structure, the blade form of the Hermitian layer, and the temptation is to take its norm as the norm of the layer. It does not make the algebra a topological algebra. The norm is not submultiplicative — in $\mathrm{Cl}_{1,0}$ one has $(1+e_{1})^{2}=2(1+e_{1})$, of norm $2\sqrt2$ against $\lVert1+e_{1}\rVert^{2}=2$ — and in dimension $n$ the product satisfies the Cauchy–Schwarz bound $\lVert xy\rVert\le2^{n/2}\lVert x\rVert\lVert y\rVert$, and the ratio $\sqrt2$ is attained at the idempotent $\tfrac12(1+e_{1})$. The bound grows without bound with the dimension, so in infinite dimension the one-sided multiplications have no uniform bound over the unit ball: they are each bounded, the product is separately continuous, and the product is not jointly continuous and does not extend to the completion. The completion is the Fock space of the canonical anticommutation relations, a Hilbert space on which the algebra acts, and not an algebra; the distinction is the infinite-dimensional form of the statement of *Topological Clifford Algebras*, §*The Layer*, that separate continuity is the hypothesis and joint continuity the theorem of the normed case. The estimate and the failure are worked out in *The Bounded Left and Right Multiplication on a Clifford Algebra* and in *The Euclidean Form, the Norm and the Completion on a Clifford Algebra*.

**Remark (where the C*-completion is).** The completion of the algebra in the operator norm of the Fock representation is the canonical anticommutation relation algebra, a C*-algebra generated by a Hilbert space with $c(f)^{2}=\lVert f\rVert^{2}$; its construction, the Fock representation, the uniqueness of the vacuum and the Bogoliubov transformations are the content of *Infinite-Dimensional Clifford Algebras and CAR with Inner Conjugation*, and the present article is careful not to duplicate them. The C*-completion is the smallest of the algebra completions and the one that carries the involution and the spectral theory of the Hermitian layer.

## Summary

The Clifford algebra of an infinite-dimensional quadratic space has two completions. The **filtration completion** is the inverse limit of the bounded-degree quotients, a complete Hausdorff topological algebra with the algebra as a dense subalgebra and with associated graded algebra $\Lambda(V)$, the exterior algebra; the **norm completion** is the metric completion of the quotient of the algebra by the kernel of the **projective tensor seminorm**, and it is a Banach algebra, because the projective norm of the tensor algebra is submultiplicative and the kernel of the descended seminorm is a two-sided ideal.

In finite dimension over a complete valued field the filtration topology is discrete and both completions are the algebra itself. In infinite dimension the two differ in general, the filtration completion carrying the bounded-degree coefficients of arbitrary degree and the norm completion carrying the elements of finite projective norm; each has its universal property, a bounded homomorphism factoring through the norm completion and a filtration-continuous one through the filtration completion. The associated graded algebra of the norm completion is the exterior algebra when the filtration it inherits is separated. **Absolutely convergent series** converge in either completion, the **geometric series** sums to $(1-t)^{-1}$ for $\lVert t\rVert<1$, and the **exponential** of a vector converges in both, in the norm completion by the estimate $\lVert v^{n}/n!\rVert\le\lVert v\rVert^{n}/n!$ and in the filtration completion because the degrees increase.

The **Euclidean norm** of the definite case does not make the algebra a topological algebra: it is not submultiplicative, its multiplication constant exceeds one and is unbounded in infinite dimension, and the product is separately continuous and not jointly continuous for it, the Euclidean norm and the operator norm being equivalent on each grade alone. The norm that does make the algebra a C*-algebra is the operator norm of the Fock representation, and the construction of that completion, with the Fock representation and the Bogoliubov transformations, belongs to *Infinite-Dimensional Clifford Algebras and CAR with Inner Conjugation*; the Euclidean form and the norm of a blade belong to the Hermitian layer, *The Euclidean Form, the Norm and the Completion on a Clifford Algebra*.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\widehat{\mathrm{Cl}}_{\mathrm{filt}}=\varprojlim\mathrm{Cl}/N_{k}$ | the filtration completion, a complete topological algebra |
| $\lVert\cdot\rVert_{\pi}$ | the projective tensor norm, submultiplicative |
| $J=\{x : \lVert x\rVert_{\mathrm{q}}=0\}$ | the kernel of the descended seminorm, a two-sided ideal |
| $\widehat{\mathrm{Cl}}_{\lVert\cdot\rVert}$ | the norm completion, a Banach algebra |
| $\exp(v)=\sum_{n}v^{n}/n!$ | the exponential, convergent in both completions |
| $\operatorname{gr}\widehat{\mathrm{Cl}}\cong\Lambda(V)$ | the associated graded algebra of a completion |
| Euclidean norm vs projective norm | separate continuity vs joint continuity of the product |

## Further Reading

- Nicolas Bourbaki, *Topological Vector Spaces* (Springer, 1987), for the projective tensor product, its universal property and the completion of a normed space.
- Nicolas Bourbaki, *Commutative Algebra* (Springer, 1989), for the filtration, its completion and the associated graded algebra.
- Frank F. Bonsall and John Duncan, *Complete Normed Algebras* (Springer, 1973), for the completion of a normed algebra, the geometric series and the exponential.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, Vol. I (Academic Press, 1983), for the canonical anticommutation relations and the C*-completion, named here and deferred.
- Ola Bratteli and Derek W. Robinson, *Operator Algebras and Quantum Statistical Mechanics*, Vol. 2 (Springer, 1997), for the CAR algebra and its Fock representation.
- John B. Conway, *A Course in Functional Analysis*, 2nd edition (Springer, 1990), for the convergence of series in a Banach space and the uniqueness of an extension by continuity.
