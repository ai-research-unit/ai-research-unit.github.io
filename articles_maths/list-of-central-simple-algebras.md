
# __List of Central Simple Algebras__

## Introduction

This article lists the central simple algebras over a field that the corpus meets, together with the algebras that fail to be central or fail to be simple. A central simple algebra is a finite-dimensional algebra with $1 \neq 0$ whose centre is exactly the scalar copy of the field and whose only two-sided ideals are $0$ and the algebra itself; its dimension is a perfect square, its degree, and it is a matrix algebra over a central division algebra by Wedderburn's structure theorem. Every entry points to the article that introduces the object.

The list is a proper subclass of *List of Algebras*: that article carries the algebras over a field of the corpus with their dimension, their centre and their ideals, and this one carries the central simple algebras, with the degree of each and the division algebra it is a matrix algebra over, and beside them the algebras that fail centrality or simplicity.

This article introduces nothing and proves nothing. It records examples and non-examples side by side, a non-example being an algebra whose centre is larger than the field, or an algebra with a proper nonzero two-sided ideal, with the failure named and the article that records it.

## The Definition, the Degree and the Dimension

A central simple $F$-algebra is central when its centre is the scalar copy $F \cdot 1_A$ of the field, and simple when its only two-sided ideals are $0$ and $A$; the two conditions are independent, and each fails in examples of the corpus. The degree is the square root of the dimension, so centrality and simplicity together force the dimension to be a square.

| Object | The property it has | Introduced in |
|---|---|---|
| Central $F$-algebra $A$ | $1 \neq 0$ and $Z(A) = F \cdot 1_A$ | *Central Simple Algebras and the Brauer Group* |
| Simple algebra $A$ | the only two-sided ideals are $0$ and $A$ | *Central Simple Algebras and the Brauer Group* |
| Central simple algebra | central and simple; finite-dimensional over $F$ | *Central Simple Algebras and the Brauer Group* |
| The degree $\deg(A) = \sqrt{\dim_F A}$ | the square root of the dimension; the dimension of a central simple algebra is always a perfect square | *Central Simple Algebras and the Brauer Group* |
| The tensor product $A \otimes_F B$ | central simple of degree $\deg(A)\deg(B)$ and dimension $(\dim_F A)(\dim_F B)$ | *Central Simple Algebras and the Brauer Group* |
| The opposite algebra $A^{\mathrm{op}}$ | central simple; $A \otimes_F A^{\mathrm{op}} \cong M_{d^2}(F)$ | *Central Simple Algebras and the Brauer Group* |
| Skolem–Noether | every $F$-algebra automorphism of $A$ is inner, and $\operatorname{Aut}_F(A) \cong A^\times/F^\times$ | *Central Simple Algebras and the Brauer Group* |
| The centralizer $C_A(B)$ and the double centralizer | $C_A(B)$ has dimension $\dim_F A / \dim_F B$ for a simple subalgebra $B$ | *Central Simple Algebras and the Brauer Group* |
| The reduced trace and norm $\operatorname{Trd}, \operatorname{Nrd}$ | the degree-$d$ analogues of the trace and determinant, becoming them over a splitting field $L$ with $A \otimes_F L \cong M_d(L)$ | *Central Simple Algebras and the Brauer Group* |

Simplicity is detected after base change, since a central simple algebra becomes a full matrix algebra after a suitable extension of scalars, and centrality and simplicity are both preserved by base change; the phrase *central over $F$* names the ground field, which is not a matter of indifference: the biquaternions have centre $\mathbb{C}$, so they are central simple over $\mathbb{C}$ and not central over $\mathbb{R}$.

## The Central Simple Algebras of the Corpus

The examples fall into three families: the matrix algebras, which are the split case; the division algebras, which are the non-split case; and the four-dimensional quaternion algebras, which are the first case where both occur.

| Algebra | Its degree and simplicity | Introduced in |
|---|---|---|
| $M_n(F)$, the matrix algebra | central simple of degree $n$ and dimension $n^2$; centre $F I_n$ | *Central Simple Algebras and the Brauer Group* |
| A finite-dimensional central division algebra $D$ over $F$ | central simple exactly when its centre is $F$; degree $\deg(D)$ | *Central Simple Algebras and the Brauer Group* |
| The quaternion algebra $(a,b)_F$ | central simple of degree $2$ and dimension $4$; either a division algebra or $M_2(F)$ | *Central Simple Algebras and the Brauer Group* |
| $\mathbb{H} = (-1,-1)_{\mathbb{R}}$ | the real quaternion algebra; a central division algebra over $\mathbb{R}$ | *Quaternion Algebra* |
| The biquaternions $\mathbb{B} = \mathbb{C} \otimes_\mathbb{R} \mathbb{H}$ | central simple over $\mathbb{C}$, where it is $M_2(\mathbb{C})$; simple but not central over $\mathbb{R}$ | *Biquaternion Algebra* |
| The field $F$ itself | central simple of degree $1$; the identity of the Brauer group | *Central Simple Algebras and the Brauer Group* |

The matrix algebra is central simple because its centre is the scalars and its matrix units generate it from any nonzero element, and the quaternion algebras are the four-dimensional case: $(a,b)_F$ is a division algebra for suitable $a$ and $b$, and otherwise it splits to $M_2(F)$.

## The Division Algebra Part, the Index and the Exponent

Wedderburn's structure theorem writes every central simple algebra as a matrix algebra over a central division algebra, and the size of that division algebra is the index of the class.

| Object | The property it has | Introduced in |
|---|---|---|
| Wedderburn's structure theorem | $A \cong M_n(D)$ with $D$ a central division $F$-algebra, determined up to isomorphism | *Central Simple Algebras and the Brauer Group* |
| The index $\operatorname{ind}(A) = \sqrt{\dim_F D} = \deg(D)$ | the degree of the division algebra part; it divides the degree $\deg(A)$ | *Central Simple Algebras and the Brauer Group* |
| A splitting field $L/F$ | a field extension with $A \otimes_F L \cong M_d(L)$, $d = \deg(A)$ | *Central Simple Algebras and the Brauer Group* |
| Splitting by a maximal subfield | a maximal subfield of $D$ has degree $\operatorname{ind}(A)$ and splits $A$ | *Central Simple Algebras and the Brauer Group* |
| The exponent $\exp(A)$ | the order of $[A]$ in $\operatorname{Br}(F)$; it divides the index | *Central Simple Algebras and the Brauer Group* |
| The division algebra of index $n$ | $\dim_F D = n^2$, and every maximal subfield of $D$ has degree $n$ and splits it | *Central Simple Algebras and the Brauer Group* |

The index and the degree are the two numerical invariants of a central simple algebra, and the theorem that the exponent divides the index is the arithmetic relation between the two; the index is always realised, because a maximal subfield of the division algebra has degree equal to it.

## The Central Division Algebras

A central division algebra is a central simple algebra that is itself a division algebra, and it is the canonical representative of its class under similarity. The list records them here because the scope of the article asks for the division algebra a central simple algebra is a matrix algebra over.

| Algebra | The property it has | Introduced in |
|---|---|---|
| A central division algebra over $F$ | finite-dimensional, centre exactly $F$, no zero divisors; central simple of degree its index | *Central Simple Algebras and the Brauer Group* |
| The quaternion algebra $(a,b)_F$ as a division algebra | a division algebra exactly when it does not split to $M_2(F)$, that is, when the norm condition fails | *Central Simple Algebras and the Brauer Group* |
| A cyclic algebra $(\chi,a)$ | a division algebra when $a$ is not a norm from the cyclic extension | *Central Simple Algebras and the Brauer Group* |
| The Hasse invariant $\operatorname{inv}_v(D)$ | the local invariant that determines a central division algebra over a number field | *Central Simple Algebras and the Brauer Group* |

The division algebras themselves, with the classification theorems of Frobenius, Wedderburn and Hurwitz, are carried by *List of Division Algebras*; the division rings without a chosen ground field, including the division ring of fractions of the Weyl algebra and the free field, are carried by *List of Non-Commutative Division Rings*. This list carries the same objects only as the division-algebra representatives of the classes in the Brauer group, and the pointer for each is the article that introduces it, *Central Simple Algebras and the Brauer Group*.

## The Brauer Group of Similarity Classes

The similarity classes of central simple algebras form an abelian group under the tensor product, and the group is the invariant that the classification produces.

| Object | The property it has | Introduced in |
|---|---|---|
| Similarity $A \sim B$ | $A \otimes_F M_m(F) \cong B \otimes_F M_n(F)$ for some $m, n$; equivalent to $D_A \cong D_B$ | *Central Simple Algebras and the Brauer Group* |
| The division algebra representative of $[A]$ | the unique representative of the class that is a division algebra, up to isomorphism | *Central Simple Algebras and the Brauer Group* |
| The Brauer group $\operatorname{Br}(F)$ | similarity classes under $\otimes_F$, identity $[F]$, inverse $[A^{\mathrm{op}}]$; abelian | *Central Simple Algebras and the Brauer Group* |
| The relative Brauer group $\operatorname{Br}(L/F)$ | the classes split by $L$, isomorphic to $H^2(G, L^\times)$ for $G = \operatorname{Gal}(L/F)$ | *Central Simple Algebras and the Brauer Group* |
| A crossed product | the central simple algebra attached to a factor set of a finite Galois extension | *Central Simple Algebras and the Brauer Group* |
| The cyclic algebra $(\chi,a) = (L/F,\sigma,a)$ | $z^n = a$, $z\ell = \sigma(\ell)z$; the explicit crossed product over a cyclic extension | *Central Simple Algebras and the Brauer Group* |

The quaternion algebras are the cyclic algebras for the quadratic extensions, and the crossed-product description makes the Brauer group the cohomological home of the factor-set classification: the class of a central simple algebra is a second cohomology class of the splitting extension.

## Computations of the Brauer Group

The Brauer group is computed for the standard fields, and each computation is a statement about which central division algebras the field admits.

| Field $F$ | The property it has | Introduced in |
|---|---|---|
| Algebraically closed $F$ | $\operatorname{Br}(F) = 0$: every central simple algebra is $M_n(F)$ | *Central Simple Algebras and the Brauer Group* |
| Finite $\mathbb{F}_q$ | $\operatorname{Br}(\mathbb{F}_q) = 0$, by Wedderburn's little theorem | *Central Simple Algebras and the Brauer Group* |
| $\mathbb{R}$ | $\operatorname{Br}(\mathbb{R}) \cong \mathbb{Z}/2\mathbb{Z}$, generated by $[\mathbb{H}]$, with $\mathbb{H} \otimes_\mathbb{R} \mathbb{H} \cong M_4(\mathbb{R})$ | *Central Simple Algebras and the Brauer Group* |
| $\mathbb{C}$ | $\operatorname{Br}(\mathbb{C}) = 0$; the relative group $\operatorname{Br}(\mathbb{C}/\mathbb{R}) \cong \mathbb{Z}/2\mathbb{Z}$ | *Central Simple Algebras and the Brauer Group* |
| A non-Archimedean local field | $\operatorname{Br}(F) \cong \mathbb{Q}/\mathbb{Z}$, with invariant $1/n$ for a degree-$n$ unramified cyclic algebra | *Central Simple Algebras and the Brauer Group* |
| A number field | Hasse–Brauer–Noether: the local invariants with the reciprocity relation, identifying $\operatorname{Br}(F)$ with a subgroup of $\bigoplus_v \mathbb{Q}/\mathbb{Z}$ | *Central Simple Algebras and the Brauer Group*; the reciprocity law belongs to *Class Field Theory* |

Over an algebraically closed field and over a finite field there is no central division algebra beyond the field itself, so every central simple algebra is split; over $\mathbb{R}$ there is exactly one nontrivial class, that of the quaternions; and over a number field the group is infinite and is computed by the local invariants.

## Algebras That Fail Centrality or Simplicity

The objects below are the ones a reader might expect among the central simple algebras and will not find, and each row names the condition that fails.

| Algebra | Why it is not central simple | Introduced in |
|---|---|---|
| The biquaternions $\mathbb{B}$ over $\mathbb{R}$ | the centre is $\mathbb{C}$ and not $\mathbb{R}$, so it is not central over $\mathbb{R}$; it is central simple over $\mathbb{C}$, where it is $M_2(\mathbb{C})$ | *Biquaternion Algebra* |
| $\mathbb{C}$ as an $\mathbb{R}$-algebra | the centre is all of $\mathbb{C}$, so it is simple but not central over $\mathbb{R}$ | *The Complex Numbers* |
| The split-complex algebra $\mathbb{D}$ over $\mathbb{R}$ | not simple: it is $\mathbb{R} \times \mathbb{R}$, with the proper ideals generated by the idempotents $\tfrac{1}{2}(1 \pm j)$ | *Split-Complex Algebra* |
| The dual numbers $\mathbb{D}'$ | not simple: the maximal ideal $(\varepsilon)$ is a proper nonzero two-sided ideal | *Dual Numbers Algebra* |
| The group algebra $\mathbb{C}[G]$ for a nontrivial finite group $G$ | not simple: the augmentation ideal $I(G)$ is a proper nonzero two-sided ideal; it is a product of two or more matrix algebras | *Group Algebras* |
| A product $\prod_i M_{n_i}(D_i)$ with two or more factors | semisimple but not simple: each factor is a proper nonzero two-sided ideal | *Simple and Semisimple Modules* |

Centrality and simplicity are independent conditions, and the rows show both failures: the biquaternions and $\mathbb{C}$ over $\mathbb{R}$ are simple and not central, while the split-complex numbers and the dual numbers are not simple, each with a proper nonzero two-sided ideal that the commutative case exhibits explicitly. The biquaternions are the sharpest case, because they become central simple after the scalar extension to $\mathbb{C}$ that exposes the ground field in the phrase.

## Warnings

| Object | Why it is absent from the list | Introduced in |
|---|---|---|
| A central division algebra over $\mathbb{C}$ other than $\mathbb{C}$ | does not exist: an algebraically closed field carries no proper finite-dimensional division algebra | *Central Simple Algebras and the Brauer Group* |
| A finite central division algebra that is not a field | does not exist, by Wedderburn's little theorem | *Division Algebras* |
| A central simple algebra of non-square dimension | does not exist: the dimension of a central simple algebra is a perfect square | *Central Simple Algebras and the Brauer Group* |
| A commutative central simple $F$-algebra other than $F$ | does not exist: the split case $M_n(F)$ is central simple and non-commutative for $n \geq 2$, and the non-split case is a division algebra, of degree $1$ when it is commutative | *Central Simple Algebras and the Brauer Group*; *Matrix Algebras* |
| The division ring of fractions of an Ore domain | not central simple: it is a division ring, but it need not be finite-dimensional over its centre | *Ore Domains and Division Rings of Fractions* |

The warnings record that the class is small in the ways a reader might not expect: the base change to an algebraic closure always splits the algebra, the base field fixes the centre, and the square dimension is forced by the two axioms together.

## Summary

This article has listed the central simple algebras of the corpus, the algebras that fail centrality or simplicity, and the computations of the Brauer group. A central simple $F$-algebra is a finite-dimensional algebra with $1 \neq 0$, centre $F \cdot 1_A$ and no two-sided ideal but $0$ and $A$; its dimension is a perfect square $d^2$, its degree is $d$, and it is a matrix algebra $M_n(D)$ over a central division algebra $D$ by Wedderburn's structure theorem. The index $\operatorname{ind}(A) = \deg(D)$ divides the degree, the exponent $\exp(A)$, the order of the class in the Brauer group, divides the index, and a maximal subfield of $D$ has degree the index and splits the algebra. The examples are the matrix algebras $M_n(F)$, the central division algebras, the quaternion algebras $(a,b)_F$ and $\mathbb{H} = (-1,-1)_{\mathbb{R}}$, and the cyclic algebras and crossed products. The similarity classes of central simple algebras form the Brauer group $\operatorname{Br}(F)$, with $\operatorname{Br}(F) = 0$ for algebraically closed and for finite fields, $\operatorname{Br}(\mathbb{R}) \cong \mathbb{Z}/2\mathbb{Z}$ generated by $[\mathbb{H}]$, $\operatorname{Br}(F) \cong \mathbb{Q}/\mathbb{Z}$ for a non-Archimedean local field, and the Hasse–Brauer–Noether isomorphism for a number field. The non-examples — the biquaternions over $\mathbb{R}$, the complex numbers over $\mathbb{R}$, the split-complex numbers, the dual numbers, the group algebra of a nontrivial finite group and a product of two or more simple factors — each name the failure of centrality or of simplicity.

## Summary of Notation

A catalogue denotes its objects by name rather than by symbol. The symbols that appear in the tables are the following.

| Symbol | Meaning |
|---|---|
| $F$, $L$ | field and a field extension of $F$ |
| $A$, $B$ | central simple $F$-algebras |
| $D$ | central division algebra, the division algebra part of $A$ |
| $M_n(F)$, $M_n(D)$ | matrix algebras over a field and over a division algebra |
| $F \cdot 1_A$, $Z(A)$ | the scalar copy of the field and the centre of $A$ |
| $\deg(A)$, $\operatorname{ind}(A)$, $\exp(A)$ | degree, index and exponent |
| $\operatorname{Br}(F)$, $\operatorname{Br}(L/F)$, $\operatorname{inv}_v$ | Brauer group, relative Brauer group, Hasse invariant |
| $A \sim B$, $[A]$, $A^{\mathrm{op}}$ | similarity, a class in $\operatorname{Br}(F)$, the opposite algebra |
| $A \otimes_F B$ | tensor product, the group law of $\operatorname{Br}(F)$ |
| $(a,b)_F$, $(\chi,a)$, $(L/F,\sigma,a)$ | quaternion algebra, cyclic algebra and crossed product |
| $\operatorname{Trd}$, $\operatorname{Nrd}$, $C_A(B)$ | reduced trace, reduced norm, centralizer |
| $\mathbb{H}$, $\mathbb{B}$, $\mathbb{D}$, $\mathbb{D}'$ | quaternions, biquaternions, split-complex numbers, dual numbers |
| $H^2(G, L^\times)$ | second cohomology, isomorphic to $\operatorname{Br}(L/F)$ |

## Further Reading

- Philippe Gille and Tamás Szamuely, *Central Simple Algebras and Galois Cohomology* (Cambridge University Press, 2006), for the structure theory, the Brauer group and its cohomological description.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for centrality, simplicity, the division algebra part and the reduced trace and norm.
- I. N. Herstein, *Noncommutative Rings* (Mathematical Association of America, 1968), for the central simple algebras and the Brauer group in the classical formulation.
