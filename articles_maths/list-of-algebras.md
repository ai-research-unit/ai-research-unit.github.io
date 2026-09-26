# __List of Algebras__

## Introduction

This article lists the algebras over a field the corpus meets, with the axioms each satisfies, its dimension, its centre and its ideals. An algebra over a field is a vector space with a bilinear product, and the list separates the associative from the non-associative, the commutative from the non-commutative, and the division, simple, semisimple and central simple algebras from the general case.

Every entry points to the article that introduces the algebra and states its invariants. This article is a list: it introduces no definition, states no theorem, gives no proof, and carries no display mathematics. It records examples and non-examples side by side, a non-example being an algebra that fails associativity, or a division algebra that has zero divisors, or an algebra that is simple but not a division algebra, with the failure named and the article that records it.

## The Axioms of a Linear Algebra

An **algebra over a field** $F$ is an $F$-module with a bilinear product; it is **associative** if the product is, **unital** if it has an identity, **commutative** if the product is, and a **division algebra** if every nonzero element is invertible. A **Lie algebra** has an anticommutative product satisfying the Jacobi identity, and a **Jordan algebra** has a commutative product satisfying the Jordan identity; neither is associative in general.

| Axiom or class | The property it has | Introduced in |
|---|---|---|
| Algebra over a field $F$ | an $F$-module with a bilinear product | *Algebras* |
| Associative algebra | the product is associative | *Algebras* |
| Unital algebra | the product has an identity $1$ | *Algebras* |
| Commutative algebra | the product is commutative | *Algebras* |
| Division algebra | every nonzero element is a unit, so the algebra has no zero divisors | *Division Algebras* |
| Ideal of an algebra | a subspace closed under multiplication by the algebra; the kernel of a homomorphism | *Algebras* |
| Centre $Z(A)$ | the elements commuting with every element; a commutative subalgebra | *Algebras* |
| Lie algebra | an anticommutative product satisfying the Jacobi identity; not associative | *Lie Algebras* |
| Jordan algebra | a commutative product satisfying the Jordan identity; not associative | *Jordan Algebras* |
| Non-example: a non-associative algebra | fails associativity: the octonions and the Lie algebras are the examples | *Octonion Algebra* |
| Non-example: a non-unital algebra | fails to have an identity: the even part of a Clifford algebra with a nontrivial radical | *The Clifford Algebra* |

## Associative Algebras and Their Invariants

The associative algebras of the corpus are the field itself, the matrix algebras, the polynomial and group algebras, the number systems and their quotients. The dimension, the centre and the ideals distinguish them: a division algebra has no nontrivial ideals, a matrix algebra $M_n(k)$ has centre $k$ and no nontrivial two-sided ideals, and a group algebra has a centre spanned by the conjugacy-class sums.

| Algebra | Dimension, centre, ideals | Introduced in |
|---|---|---|
| Field $F$ | dimension $1$; centre $F$; only the ideals $0$ and $F$ | *Fields* |
| $F[x]$ | infinite-dimensional; centre $F[x]$; every ideal principal | *Polynomial Rings and Rational Functions* |
| Matrix algebra $M_n(k)$ | dimension $n^2$; centre $k$; two-sided ideals only $0$ and $M_n(k)$; simple | *Examples of Algebras* |
| Group algebra $k[G]$ | dimension $|G|$; centre spanned by the conjugacy-class sums; the augmentation ideal is nontrivial | *Group Algebras* |
| Quaternions $\mathbb{H}$ | dimension $4$ over $\mathbb{R}$; centre $\mathbb{R}$; no nontrivial ideals; division algebra | *Quaternion Algebra* |
| Split-complex numbers $\mathbb{D}$ | dimension $2$; centre the whole algebra; the ideals $(1 \pm t)$; not a field | *Split-Complex Algebra* |
| Dual numbers $\mathbb{D}'$ | dimension $2$; centre the whole algebra; the nilpotent ideal $(\varepsilon)$; local | *Dual Numbers Algebra* |
| Biquaternions $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | dimension $4$ over $\mathbb{C}$; centre $\mathbb{C}$; isomorphic to $M_2(\mathbb{C})$; simple | *Biquaternion Algebra* |
| Central simple algebra | finite-dimensional, centre the field, no nontrivial two-sided ideals | *Central Simple Algebras and the Brauer Group* |
| Non-example: $\mathbb{D}$ as a field | fails: it has zero divisors $(1-t)(1+t)=0$ | *Split-Complex Algebra* |
| Non-example: $\mathbb{H}$ as a field | fails: it is a division ring but not commutative | *Quaternion Algebra* |

## Simple, Semisimple and Central Simple Algebras

An algebra is **simple** when it has no nontrivial two-sided ideals, **semisimple** when it is a product of matrix algebras over division rings, and **central simple** over $F$ when it is simple with centre exactly $F$. The **Wedderburn–Artin theorem** describes the semisimple algebras, and the central simple algebras over $F$ form the **Brauer group** under the tensor product over $F$.

| Algebra | Dimension, centre, ideals | Introduced in |
|---|---|---|
| Semisimple algebra | a product $\prod_i M_{n_i}(D_i)$ of matrix algebras over division rings | *Simple and Semisimple Modules* |
| Wedderburn–Artin decomposition | the factors are determined up to permutation; the centre is the product of the centres | *Simple and Semisimple Modules* |
| Simple algebra | exactly two two-sided ideals, $0$ and the algebra; a matrix algebra over a division ring | *Simple and Semisimple Modules* |
| Central simple algebra over $F$ | simple, finite-dimensional, centre $F$; becomes a matrix algebra over a splitting field | *Central Simple Algebras and the Brauer Group* |
| Brauer group $\operatorname{Br}(F)$ | the central simple algebras modulo matrix algebras, under $\otimes_F$ | *Central Simple Algebras and the Brauer Group* |
| Division algebra | a simple algebra whose only nonzero elements are units | *Division Algebras* |
| Non-example: a simple algebra that is not a division algebra | $M_2(\mathbb{R})$ is simple but has zero divisors | *Examples of Algebras* |
| Non-example: the biquaternions over $\mathbb{R}$ | fail to be central simple over $\mathbb{R}$: their centre is $\mathbb{C}$, and $\mathbb{B}$ is split | *Biquaternion Algebra* |

## Algebras Defined by Generators and Relations

The tensor algebra $T(V)$ is the free associative algebra on a vector space, and the symmetric, exterior and Clifford algebras are its quotients by relations of low degree; the universal enveloping algebra is the quotient by the relations of a Lie bracket. The non-homogeneous relations give the Weyl algebra, which carries a filtration rather than a grading, and the path algebra of a quiver is the tensor algebra of its arrow space modulo the relations of the quiver.

| Algebra | Dimension, centre, ideals | Introduced in |
|---|---|---|
| Tensor algebra $T(V)$ | infinite-dimensional; the free associative algebra on $V$ | *Tensor Powers and the Free Algebra* |
| Free algebra | infinite-dimensional for $\dim V \geq 1$; the non-commutative polynomial algebra | *Tensor Powers and the Free Algebra* |
| Symmetric algebra $\operatorname{Sym}(V)$ | the polynomial algebra on $\dim V$ generators; centre the whole algebra | *The Symmetric Algebra* |
| Exterior algebra $\Lambda(V)$ | dimension $2^{\dim V}$; graded-commutative; not commutative for $\dim V \geq 2$ | *The Exterior Algebra* |
| Clifford algebra $\mathrm{Cl}(V,q)$ | dimension $2^{\dim V}$; centre computed from the volume element; a $\mathbb{Z}/2$-grading | *The Clifford Algebra* |
| Universal enveloping algebra $U(\mathfrak{g})$ | infinite-dimensional; centre the Casimir-type elements; by PBW a filtered deformation of $\operatorname{Sym}(\mathfrak{g})$ | *Representations of Lie Algebras* |
| Weyl algebra $A_1$ | infinite-dimensional; centre $k$; the algebra of polynomial differential operators, with $yx - xy = 1$ | *Quotients of the Tensor Algebra* |
| Quotients giving the number systems | $\mathbb{R}$, $\mathbb{C}$, $\mathbb{D}$ and $\mathbb{H}$ as quotients of $T(V)$ | *Quotients of the Tensor Algebra* |
| Clifford algebras in finite dimensions | the real Clifford algebras of dimension $2^n$, with their centre and periodicity | *Clifford Algebras in Finite Dimensions* |
| Path algebra $kQ$ of a quiver | the algebra with the paths as a basis; finite-dimensional exactly when $Q$ has no oriented cycle | *Quiver Representations and Representation Type* |
| Non-example: the free algebra as a commutative algebra | fails commutativity: $xy \neq yx$ for the generators | *Tensor Powers and the Free Algebra* |
| Non-example: $\mathrm{Cl}(V,q)$ for a degenerate form | fails semisimplicity: the radical is a nontrivial nilpotent ideal | *Degenerate Clifford Algebras and the Radical* |

## Non-Associative Algebras and the Number Systems

The number systems give the corpus its chain of non-associative algebras: $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$ are associative division algebras, the octonions are a non-associative division algebra, and the split-complex, split-biquaternion, dual and biquaternion algebras are associative but have zero divisors. The **Cayley–Dickson construction** produces the chain and the **Hurwitz theorem** fixes the four normed division algebras.

| Algebra | Dimension, centre, ideals | Introduced in |
|---|---|---|
| $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$ | dimensions $1$, $2$, $4$; centres $\mathbb{R}$, $\mathbb{C}$, $\mathbb{R}$; associative division algebras | *Division Algebras* |
| Octonions $\mathbb{O}$ | dimension $8$; centre $\mathbb{R}$; a non-associative division algebra | *Octonion Algebra* |
| Split biquaternions $\mathbb{H}_{\mathbb{D}} = \mathbb{D}\otimes_{\mathbb{R}}\mathbb{H}$ | dimension $8$; centre $\mathbb{D}$; associative with zero divisors, isomorphic to $\mathbb{H}\oplus\mathbb{H}$; not a division algebra | *Split-Biquaternion Algebra* |
| Lie algebra $\mathfrak{gl}_n(k)$ | dimension $n^2$; centre the scalar matrices; non-associative, with the bracket | *Lie Algebras* |
| Jordan algebra | commutative and non-associative, with the Jordan identity; the spin factors as examples | *Jordan Algebras* |
| The number systems as Clifford algebras | the realisation of $\mathbb{C}$, $\mathbb{H}$ and $\mathbb{O}$ inside Clifford algebras of a form | *The Number Systems as Clifford Algebras* |
| Non-example: the octonions as associative | fails associativity: the associator is nonzero | *Octonion Algebra* |
| Non-example: the split biquaternions as a division algebra | fail to be a division algebra: they have zero divisors, though they have no nonzero nilpotents | *Split-Biquaternion Algebra* |

## Summary

The list gathers the algebras over a field of the corpus. The axioms are associativity, a unit, commutativity and the division property, with the Lie and Jordan algebras as the non-associative classes. The associative algebras are the field, the polynomial algebra, the matrix algebra $M_n(k)$, the group algebra, the quaternions, the split biquaternions, the split-complex numbers, the dual numbers and the biquaternions, each with its dimension, centre and ideals; the simple, semisimple and central simple algebras are the matrix algebras over division rings, with the Wedderburn–Artin decomposition and the Brauer group. The algebras defined by generators and relations are the tensor and free algebras, the symmetric, exterior and Clifford algebras, the universal enveloping algebra, the Weyl algebra and the path algebra. The non-associative algebras are the Lie and Jordan algebras, and the number systems run from the associative division algebras $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$ to the non-associative division algebra $\mathbb{O}$ and the zero-divisor algebras. The non-examples — a non-associative algebra, a non-unital algebra, the split-complex numbers as a non-field, the quaternions as a non-field, a simple algebra that is not a division algebra, the biquaternions as non-central, the free algebra as non-commutative, a degenerate Clifford algebra and the octonions as non-associative — each name the failure.

## Summary of Notation

The article denotes its objects by name; the symbols appearing in the tables are those of the introducing articles.

| Symbol | Meaning |
|---|---|
| $T(V)$, $\operatorname{Sym}(V)$, $\Lambda(V)$ | tensor, symmetric and exterior algebras |
| $\mathrm{Cl}(V,q)$ | Clifford algebra of a quadratic form |
| $U(\mathfrak{g})$ | universal enveloping algebra of a Lie algebra |
| $A_1$ | the Weyl algebra, $yx - xy = 1$ |
| $M_n(k)$ | matrix algebra |
| $Z(A)$ | centre of an algebra |
| $\mathbb{Z}$ | the integers, as in the $\mathbb{Z}/2$-grading of a Clifford algebra |
| $\operatorname{Br}(F)$ | Brauer group |
| $k[G]$ | group algebra |
| $\mathbb{R}$, $\mathbb{C}$, $\mathbb{D}$, $\mathbb{D}'$, $\mathbb{H}$, $\mathbb{O}$, $\mathbb{B}$ | real, complex, split-complex, dual, quaternion, octonion and biquaternion algebras |
| $\mathbb{H}_{\mathbb{D}} = \mathbb{D}\otimes_{\mathbb{R}}\mathbb{H}$ | split biquaternions, of real dimension $8$ |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the structure theory of associative algebras, the Wedderburn–Artin theorem and the Brauer group.
- Frank Anderson and Kent Fuller, *Rings and Categories of Modules* (Springer, 2nd ed. 1992), for simple, semisimple and central simple algebras.
- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for the Lie algebras, their universal enveloping algebras and the PBW theorem.
- Richard Schafer, *An Introduction to Nonassociative Algebras* (Dover, 1995), for the Jordan algebras, the octonions and the Cayley–Dickson construction.
