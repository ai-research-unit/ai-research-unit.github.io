
# __List of Matrix Rings__

## Introduction

This article lists the matrix rings $M_n(R)$ over the commutative rings and the matrix algebras over the fields, together with the rings and the algebras that are not of that form. The matrix ring is the model object of the subject: it is the algebra by which the associative theory is tested, it carries a basis — the matrix units — whose multiplication table is the clearest display of a non-commutative structure, and over a field it is simple, central and finite-dimensional. Every entry points to the article that introduces the object.

The list is a proper subclass of *List of Algebras*: that article carries the algebras over a field of the corpus with their dimension, their centre and their ideals; the matrix rings over a commutative ring and over a division ring lie beyond that scope, and this one carries them together with the matrix algebras, with the matrix units, the centre, the units and the ideals of each, and beside them the rings and algebras that are not a matrix ring.

A ring-theoretic point governs the naming throughout. The object is a **matrix ring** when the row reads $M_n(R)$ over a commutative ring or $M_n(D)$ over a division ring, and a **matrix algebra** when the row reads it over a field and the algebra structure is what matters; the article that introduces the object is *Matrix Algebras*, and the rows for $M_n(R)$ and its structure point there whatever name the row uses.

This article introduces nothing and proves nothing. It records examples and non-examples side by side, a non-example being a ring that is not a matrix ring in the sense of the list, with the failure named and the article that records it.

## The Matrix Ring and Its Matrix Units

For a commutative ring $R$ and $n \geq 1$, the matrix ring $M_n(R)$ is the ring of $n \times n$ matrices with the usual addition and multiplication. Its additive basis is the set of matrix units, and the multiplication table of the units is the source of every structural fact below.

| Object | The property it has | Introduced in |
|---|---|---|
| $M_n(R)$, the matrix ring | the $n \times n$ matrices over a commutative ring $R$; associative with unit $I_n$ | *Matrix Algebras* |
| The matrix units $E_{ij}$ | an $R$-basis, with $E_{ij}E_{kl} = \delta_{jk}E_{il}$; $\dim_R M_n(R) = n^2$ | *Matrix Algebras* |
| $\operatorname{End}_R(R^n)$ | the endomorphism ring of the free module $R^n$, isomorphic to $M_n(R)$ | *Matrix Algebras* |
| The case $n = 1$ | $M_1(R) = R$: the ring itself | *Matrix Algebras* |
| The case $n = 2$ | four-dimensional, with $E_{12}$ and $E_{21}$ nilpotent and $E_{11}E_{22} = 0$ | *Matrix Algebras* |

The units satisfy $E_{ij} = E_{ik}E_{kj}$ for every $k$, which is the identity that makes the ideal theory of the matrix ring trivial over a field, and the products $E_{ij}E_{kl}$ with $j \neq k$ vanish, which is why the matrix ring is never a domain for $n \geq 2$.

## The Matrix Algebras over a Field

Over a field the matrix ring is simple, its left ideals are the sets of matrices whose columns lie in a subspace, and its regular module is a direct sum of copies of the unique simple module.

| Algebra | The property it has | Introduced in |
|---|---|---|
| $M_n(k)$, the matrix algebra over a field | simple: the only two-sided ideals are $0$ and $M_n(k)$ | *Matrix Algebras* |
| A left ideal $I_V$ | the matrices whose columns lie in a subspace $V \subseteq k^n$; the left ideals are in bijection with the subspaces | *Matrix Algebras* |
| The regular module | a direct sum of $n$ copies of the simple module $k^n$ | *Matrix Algebras* |
| The simple module $k^n$ | the unique simple left $M_n(k)$-module up to isomorphism | *Matrix Algebras* |

Over a field the two-sided ideal structure is trivial, so a proper nonzero two-sided ideal is the one thing a matrix algebra does not have; the left ideals are not trivial, and they are classified by the subspaces of the column space.

## The Centre, the Units and the Ideals

The data that distinguish $M_n(R)$ from a general ring are the scalar centre, the determinant criterion for a unit, and the trace; all three are computed from the matrix units.

| Object | The property it has | Introduced in |
|---|---|---|
| The centre $Z(M_n(R)) = R I_n$ | the scalar matrices; $M_n(R)$ is a central $R$-algebra | *Matrix Algebras* |
| The unit criterion | $A$ is a unit if and only if $\det A \in R^\times$, with $A^{-1} = (\det A)^{-1}\operatorname{adj}(A)$ | *Matrix Algebras* |
| $\mathrm{GL}_n(k)$, the units over a field | the matrices with $\det A \neq 0$ | *Matrix Algebras* |
| The trace $\operatorname{Tr} A$ | $R$-linear, with $\operatorname{Tr}(AB) = \operatorname{Tr}(BA)$ and invariance under cyclic permutation | *Matrix Algebras* |
| The determinant $\det A$ | multiplicative, $\det(AB) = \det A \cdot \det B$ and $\det I_n = 1$ | *Matrix Algebras* |
| The characteristic polynomial $\chi_A(t) = \det(tI_n - A)$ | constant term $(-1)^n \det A$ and coefficient of $t^{n-1}$ equal to $-\operatorname{Tr} A$ | *Matrix Algebras* |
| The trace form $\langle A,B\rangle = \operatorname{Tr}(AB)$ | symmetric, associative and non-degenerate; $M_n(k)$ is a symmetric Frobenius algebra | *Matrix Algebras* |
| Skolem–Noether | every $k$-automorphism of $M_n(k)$ is inner, and $\operatorname{Aut}_k(M_n(k)) \cong \mathrm{PGL}_n(k)$ | *Matrix Algebras* |
| Derivations of $M_n(k)$ | every $k$-derivation is inner, $\delta(A) = [H,A]$ | *Matrix Algebras* |

The determinant criterion is the reason the units of a matrix ring are computable: over a field they are the invertible matrices, and over a general commutative ring the determinant may be a nonzero nonunit, as for $\operatorname{diag}(2,1) \in M_2(\mathbb{Z})$.

## Tensor Products and Products of Matrix Rings

Matrix rings are closed under the tensor product, and they are the factors of the Wedderburn–Artin decomposition of a semisimple ring; a product of two or more of them is again a ring but not again a single matrix ring.

| Object | The property it has | Introduced in |
|---|---|---|
| The tensor product formula | $M_m(k) \otimes_k M_n(k) \cong M_{mn}(k)$: the tensor product of two matrix algebras is again a matrix algebra, of the product size | *Matrix Algebras* |
| The tensor product of algebras | the general construction, of which the matrix formula is the worked case | *Tensor Products of Algebras* |
| The Wedderburn–Artin decomposition | a semisimple ring is $\prod_i M_{n_i}(D_i)$, a product of matrix rings over division rings, the factors determined up to permutation | *Simple and Semisimple Modules* |
| Non-example: a product $\prod_{i=1}^{r} M_{n_i}(D_i)$ with $r \geq 2$ | semisimple but not simple: each factor is a proper nonzero two-sided ideal, so it is not a matrix ring over a division ring | *Simple and Semisimple Modules* |

The tensor product formula is the algebraic statement that the tensor product of two matrix algebras over a field is again a matrix algebra over that field, of size the product.

## Matrix Rings over Division Rings

A matrix ring over a division ring is the general simple finite-dimensional algebra, and the theorem that identifies the rings of this form is Wedderburn–Artin.

| Object | The property it has | Introduced in |
|---|---|---|
| $M_n(D)$ over a division ring $D$ | simple and Artinian; $\dim_D M_n(D) = n^2$, and its simple module is $D^n$ | *Simple and Semisimple Modules* |
| The simple module $D^n$ | the unique simple left $M_n(D)$-module, of endomorphism ring $D^{\mathrm{op}}$ | *Simple and Semisimple Modules* |
| Wedderburn–Artin, the simple case | a ring is a matrix ring over a division ring exactly when it is simple Artinian; this is a theorem, not a definition | *Simple and Semisimple Modules* |
| The division rings as the boundary case | the case $r = n_1 = 1$ of Wedderburn–Artin: a ring is a division ring exactly when it is semisimple with one factor, of size one | *Simple and Semisimple Modules* |
| $\mathbb{H}$ as a matrix ring | a division ring, so the case of a single factor of size one; a matrix ring over a division ring | *Quaternion Algebra*; *Simple and Semisimple Modules* |
| The biquaternions $\mathbb{B} \cong M_2(\mathbb{C})$ | an eight-dimensional real algebra that is a matrix ring over the division ring $\mathbb{C}$ | *Biquaternion Algebra* |
| $M_2(\mathbb{R})$ | the four-dimensional real matrix algebra, simple Artinian | *Matrix Algebras* |

The phrase "a matrix ring over a division ring" names the conclusion of Wedderburn–Artin rather than a definition, and by the theorem the class is exactly the simple Artinian rings; the division rings themselves are the case of a single factor of size one, which is the boundary the list records.

## Rings and Algebras That Are Not of That Form

The objects below are the ones a reader might expect among the matrix rings and will not find, and each row names the property that puts it outside the class.

| Object | Why it is not a matrix ring of the list | Introduced in |
|---|---|---|
| The split-complex numbers $\mathbb{D} = \mathbb{R}[j]/(j^2-1)$ | not simple: it is $\mathbb{R} \times \mathbb{R}$, with the proper ideals generated by the idempotents $\tfrac{1}{2}(1 \pm j)$ | *Split-Complex Algebra* |
| The dual numbers $\mathbb{D}' = \mathbb{R}[\varepsilon]/(\varepsilon^2)$ | not simple: the maximal ideal $(\varepsilon)$ is a proper nonzero two-sided ideal; local | *Dual Numbers Algebra* |
| The upper triangular matrix ring | a subring of $M_n(R)$ and not a full matrix ring; it is not simple, having the nilpotent ideal of strictly upper triangular matrices | *Examples of Rings and Fields*; *Semiprime Rings* |
| $\mathbb{Z}$, the integers | Noetherian but not Artinian, since $(2) \supsetneq (4) \supsetneq (8) \supsetneq \cdots$ never stabilises; hence not simple Artinian, and so not $M_n(D)$ | *Noetherian and Artinian Rings* |
| $k[x]$ and $k[x_1,\dots,x_n]$ | not Artinian: $k[x]$ is infinite-dimensional over $k$, and the chain $(x) \supsetneq (x^2) \supsetneq \cdots$ does not stabilise | *Noetherian and Artinian Rings* |
| The group algebra $\mathbb{C}[G]$ for a nontrivial finite group $G$ | semisimple but a product of two or more matrix algebras, not a single matrix ring | *Group Algebras* |
| $\mathbb{O}$, the octonions | not a ring at all: the multiplication is not associative | *Octonion Algebra* |

The upper triangular matrices, the split-complex numbers and the dual numbers are the sharp cases: each is a ring of matrices or of a matrix-like shape, and each fails simplicity, so none is a matrix ring over a division ring. The distinction between "a subring of a matrix ring" and "a matrix ring" is exactly the distinction between an arbitrary subalgebra and the full endomorphism algebra of a free module.

## Warnings

| Object | Why it is absent from the list | Introduced in |
|---|---|---|
| A commutative matrix ring $M_n(R)$ with $n \geq 2$ | does not exist: $E_{12}E_{21} \neq E_{21}E_{12}$ | *Matrix Algebras* |
| A matrix ring $M_n(R)$ with $n \geq 2$ that is a domain | does not exist: $E_{11}E_{22} = 0$ | *Matrix Algebras* |
| A matrix ring $M_n(R)$ with $n \geq 2$ that is a division ring | does not exist: a division ring has no zero divisors | *Matrix Algebras* |
| A simple Artinian ring that is not a matrix ring over a division ring | does not exist, by Wedderburn–Artin | *Simple and Semisimple Modules* |
| A finite-dimensional central division algebra over $\mathbb{C}$ other than $\mathbb{C}$ | does not exist, so $M_n(\mathbb{C})$ is the only central simple $\mathbb{C}$-algebra of each degree | *Central Simple Algebras and the Brauer Group* |

The warnings state the two directions in which the class is rigid: the full matrix ring of size at least two is never commutative, never a domain and never a division ring, and the simple Artinian rings are exactly the matrix rings over division rings.

## Summary

This article has listed the matrix rings and matrix algebras of the corpus, and the rings that are not of that form. The matrix ring $M_n(R)$ has $R$-basis the matrix units $E_{ij}$ with $E_{ij}E_{kl} = \delta_{jk}E_{il}$ and dimension $n^2$, it is isomorphic to $\operatorname{End}_R(R^n)$, it is associative with unit $I_n$, and it is non-commutative with zero divisors as soon as $n \geq 2$. Over a field it is simple, its left ideals are the sets of matrices with columns in a subspace, its regular module is a direct sum of $n$ copies of the simple module $k^n$, and its centre is $kI_n$; its units are the matrices of nonzero determinant, its trace form $\langle A,B\rangle = \operatorname{Tr}(AB)$ is symmetric, associative and non-degenerate, and by Skolem–Noether every automorphism is inner and every derivation is inner. The tensor product of two matrix algebras is a matrix algebra of the product size, and the factors of the Wedderburn–Artin decomposition of a semisimple ring are matrix rings over division rings. A ring is a matrix ring over a division ring exactly when it is simple Artinian, by Wedderburn–Artin; the division rings themselves are the boundary case of a single factor of size one. The non-examples — the split-complex numbers, the dual numbers, the upper triangular matrix ring, the integers, the polynomial algebra, the group algebra of a nontrivial finite group and the octonions — each name the failure of simplicity, of the Artinian condition or of associativity.

## Summary of Notation

A catalogue denotes its objects by name rather than by symbol. The symbols that appear in the tables are the following.

| Symbol | Meaning |
|---|---|
| $M_n(R)$, $M_n(k)$, $M_n(D)$ | matrix ring over a commutative ring, a field, a division ring |
| $n$, $I_n$ | the size and the identity matrix |
| $E_{ij}$ | the matrix units, $E_{ij}E_{kl} = \delta_{jk}E_{il}$ |
| $A_{ij}$ | the entries of a matrix $A$ |
| $\operatorname{Tr} A$, $\det A$, $\operatorname{adj}(A)$ | trace, determinant and adjugate |
| $\chi_A(t) = \det(tI_n - A)$ | the characteristic polynomial |
| $\langle A,B\rangle = \operatorname{Tr}(AB)$ | the trace form |
| $\mathrm{GL}_n(k)$, $\mathrm{PGL}_n(k)$ | the units and the projective general linear group |
| $\operatorname{End}_R(R^n)$ | the endomorphism ring, isomorphic to $M_n(R)$ |
| $I_V$ | the left ideal of matrices whose columns lie in the subspace $V$ |
| $D$, $D^n$ | a division ring and its $n$-fold direct sum, the simple module |
| $\prod_i M_{n_i}(D_i)$ | the Wedderburn–Artin decomposition of a semisimple ring |
| $\mathbb{H}$, $\mathbb{B}$, $\mathbb{D}$, $\mathbb{D}'$, $\mathbb{O}$ | quaternions, biquaternions, split-complex numbers, dual numbers, octonions |
| $M_2(\mathbb{R})$ | the four-dimensional real matrix algebra |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the matrix rings, their ideals, the Wedderburn–Artin structure theory and the division rings they are built from.
- Frank W. Anderson and Kent R. Fuller, *Rings and Categories of Modules* (Springer, 2nd ed. 1992), for the matrix ring as an endomorphism ring and the simple Artinian case.
- Tsit-Yuen Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for the matrix units, the simplicity of $M_n(D)$ and the Wedderburn–Artin theorem.
