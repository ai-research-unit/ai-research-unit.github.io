
# __List of Non-Commutative Division Rings__

## Introduction

This article lists the division rings of the corpus, finite-dimensional and infinite-dimensional, with the centre over which each is an algebra, and it records Wedderburn's little theorem and the consequence that every skew field is infinite. Every entry points to the article that introduces the object.

A division ring, or skew field, is a ring with $1 \neq 0$ in which every nonzero element is invertible, without the commutative hypothesis; the finite-dimensional division rings are the division algebras over a field, the infinite-dimensional ones are the division ring of fractions of the Weyl algebra and the free field, and the commutative ones are exactly the fields. The centre of a division ring is a field, and the division ring is an algebra over that centre, possibly of infinite dimension there.

The article introduces nothing and proves nothing. It records examples and non-examples side by side.

## What a Division Ring Is

A field is a commutative division ring, so every field of the corpus is an entry of this list, and the entries that are not fields are the proper skew fields. The division ring is an algebra over its centre, and the centre is a field by the argument of *Division Algebras*.

| Object | Degree over its centre | Commutative? | Introduced in |
|---|---|---|---|
| $\mathbb{R}$, $\mathbb{Q}$, $\mathbb{C}$ and every field | $1$ | yes | *The Real Numbers*, *The Rational Numbers*, *The Complex Numbers*, *Fields* |
| $\mathbb{H}$ | $4$ | no | *Quaternion Algebra* |
| the rational quaternions $(-1,-1)_{\mathbb{Q}}$ | $4$ | no | *Quaternion Algebra* |
| a central simple algebra that is a division ring | finite, a square | no in general | *Division Algebras* |
| the division ring of fractions of $A_1(k)$ | infinite | no | *Ore Domains and Division Rings of Fractions* |
| the free field on $n \geq 2$ generators | infinite | no | *Ore Domains and Division Rings of Fractions* |

The commutative entries are the fields and are listed for completeness; the proper skew fields are the quaternions and the two infinite-dimensional rings. The matrix ring $M_n(\mathbb{R})$ for $n \geq 2$ is an algebra over the same centre $\mathbb{R}$ as $\mathbb{H}$, but it is not a division ring, since the matrix units are zero divisors.

## The Finite-Dimensional Division Rings

| Division ring | Centre | Dimension over the centre | Introduced in |
|---|---|---|---|
| $\mathbb{R}$ | $\mathbb{R}$ | $1$ | *The Real Numbers* |
| $\mathbb{C}$ | $\mathbb{C}$ | $1$ | *The Complex Numbers* |
| $\mathbb{H}$ | $\mathbb{R}$ | $4$ | *Quaternion Algebra* |
| $(-1,-1)_{\mathbb{Q}} = \mathbb{Q} + \mathbb{Q}i + \mathbb{Q}j + \mathbb{Q}k$ | $\mathbb{Q}$ | $4$ | *Quaternion Algebra* |
| a quaternion algebra $(a,b)_k$ that is not split | $k$ | $4$ | *Division Algebras* |
| a cyclic division algebra over $k$ | $k$ | $\deg^2$ | *Division Algebras* |

Over $\mathbb{R}$ the finite-dimensional associative division algebras are exactly $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$, by the theorem of Frobenius recorded in *Division Algebras*; this is why the first three rows are the whole real case. Over $\mathbb{Q}$ there is more than one quaternion division algebra: a quaternion algebra $(a,b)_{\mathbb{Q}}$ is a division ring exactly when its norm form is anisotropic, and the classes of the quaternion algebras over $\mathbb{Q}$ are the elements of order dividing two in the Brauer group of $\mathbb{Q}$, as recorded in *Division Algebras*.

## The Infinite-Dimensional Division Rings

| Division ring | Centre | Why it is infinite-dimensional over its centre | Introduced in |
|---|---|---|---|
| the division ring of fractions of $A_1(k)$ | $k$ | it contains $k[x]$ and $k[y]$ as polynomial subrings | *Ore Domains and Division Rings of Fractions* |
| the free field on $n \geq 2$ generators | $k$ | it contains the free algebra on $n$ generators, which is infinite-dimensional | *Ore Domains and Division Rings of Fractions* |
| the Malcev–Neumann division ring of series over an ordered group | a field containing $k$ | it contains the group ring $k[G]$ of an infinite orderable group | *Ore Domains and Division Rings of Fractions* |

The Weyl algebra $A_1(k)$ is an Ore domain, so it has a division ring of fractions; the free algebra is not Ore, so it has no division ring of fractions, but it embeds in the free field that it generates. This is the separation of the two infinite-dimensional cases.

## The Centre and the Algebra Structure

| Division ring | Centre | The centre is a field because | Introduced in |
|---|---|---|---|
| $\mathbb{H}$ | $\mathbb{R}$ | the centre consists of the real multiples of $1$ | *Quaternion Algebra* |
| the division ring of fractions of $A_1(k)$ | $k$ | an element commuting with $x$ and $y$ is in $k$ | *Ore Domains and Division Rings of Fractions* |
| the free field | $k$ | the centre of the free algebra is $k$ | *Tensor Powers and the Free Algebra* |
| a general division ring $D$ | $Z(D)$ | if $a \in Z(D)$ is nonzero then $a^{-1} \in Z(D)$ | *Division Algebras* |

The division ring is an algebra over its centre; for $\mathbb{H}$ the dimension is $4$, and for the infinite-dimensional cases the dimension over the centre is infinite. The centre is the maximal commutative subfield in the sense that it is the field of scalars, and the division ring is central when the centre is the whole scalar field.

## Wedderburn's Little Theorem and the Absence of Finite Skew Fields

| Statement | Content | Introduced in |
|---|---|---|
| Wedderburn's little theorem | every finite division ring is a field | *Division Rings* |
| Corollary | every skew field is infinite, since a finite skew field would be a finite division ring | *Division Rings* |
| Corollary | a finite ring with no zero divisors is a field | *Division Rings* |

The theorem is the reason the finite fields of *List of Finite Fields* are exhausted by the commutative case: a finite division ring is a field, so the search for a finite skew field has no solution. The proof uses the class equation of the multiplicative group of a finite division ring, and it is recorded in *Division Rings*.

## The Doubling Chain and Where the Properties Are Lost

| Algebra | Dimension over $\mathbb{R}$ | Commutative? | Associative? | Division algebra? | Introduced in |
|---|---|---|---|---|---|
| $\mathbb{R}$ | $1$ | yes | yes | yes, a field | *The Real Numbers* |
| $\mathbb{C}$ | $2$ | yes | yes | yes, a field | *The Complex Numbers* |
| $\mathbb{H}$ | $4$ | no | yes | yes, a division ring | *Quaternion Algebra* |
| $\mathbb{O}$ | $8$ | no | no | no: not associative, so not a division algebra in the sense of this corpus | *Octonion Algebra* |
| $\mathbb{S}$, the sedenions | $16$ | no | no | no: not associative, and with zero divisors | *Division Algebras* |

The Cayley–Dickson doubling chain loses commutativity at the quaternions and associativity at the octonions, and it loses the division property at the sedenions; this is the reason $\mathbb{H}$ is the last division ring in the chain and the octonions are a normed division algebra that is not a division algebra in the sense of this corpus, and not a ring. The Hurwitz theorem that the normed division algebras are exactly $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$ and $\mathbb{O}$ is recorded in *Division Algebras*.

## Warnings

| Object | Why it is not a division ring | Introduced in |
|---|---|---|
| $M_n(k)$, $n \geq 2$ | the matrix units $E_{11}E_{22} = 0$ are zero divisors | *Matrix Algebras* |
| $\mathbb{B}$, the biquaternions | zero divisors; not every nonzero element is invertible | *Biquaternion Zero Divisors* |
| $\mathbb{H}_{\mathbb{D}}$, the split-biquaternions | the idempotents $e_{\pm}$ satisfy $e_+e_- = 0$ | *Split-Biquaternion Zero Divisors* |
| $\mathbb{D}$, $\mathbb{D}'$, $\mathbb{Z}/6\mathbb{Z}$ | commutative, with zero divisors; not even domains | *Split-Complex Algebra*, *Dual-Numbers Algebra*, *Modular Arithmetic and the Ring of Residues* |
| $\mathbb{O}$, $\mathbb{S}$ | normed division algebras whose multiplication is not associative, so not rings | *Octonion Algebra*, *Division Algebras* |
| the group ring $k[G]$ | has zero divisors whenever $G$ has torsion | *Group Algebras* |
| $k[G]$ with $G$ torsion-free and nontrivial | a domain, but not every nonzero element is a unit: $g - 1$ has augmentation $0$ | *Non-Commutative Domains* |

The split-biquaternions and the biquaternions are the two eight-dimensional algebras closest to $\mathbb{H}$, and both fail the definition by a zero divisor that the quaternion algebra does not have. The octonions are excluded by non-associativity and not by zero divisors, and this is the exact sense in which they are a normed division algebra without being a division ring.

## Summary

This article has listed the division rings of the corpus with the centre over which each is an algebra. The commutative entries are the fields, with dimension $1$ over themselves; the finite-dimensional skew fields are $\mathbb{H}$ and the quaternion and cyclic division algebras, with centre a field and dimension a square; the infinite-dimensional ones are the division ring of fractions of the Weyl algebra, the free field and the Malcev–Neumann division rings of series, all of dimension infinite over their centres; and the centre of each is a field. The matrix ring $M_n(k)$ for $n \geq 2$, the biquaternions, the split-biquaternions and the octonions are recorded as the objects that fail to be division rings, with the failure named in each case. Wedderburn's little theorem closes the list by excluding the finite skew fields.

## Summary of Notation

A catalogue denotes its objects by name rather than by symbol. The symbols that appear in the tables are the following.

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | The real quaternions, a division ring |
| $(-1,-1)_{\mathbb{Q}}$, $(a,b)_k$ | Quaternion algebra over $\mathbb{Q}$, over $k$ |
| $Z(D)$, $Z(\mathbb{H}) = \mathbb{R}$ | The centre of a division ring |
| $A_1(k)$, $D_1(k)$ | The Weyl algebra and the first Weyl field $\operatorname{Frac}(A_1(k))$ |
| $M_n(k)$ | The matrix algebra; not a division ring for $n \geq 2$ |
| $\mathbb{B}$, $\mathbb{H}_{\mathbb{D}}$ | Biquaternions, split-biquaternions; not division rings |
| $\mathbb{O}$, $\mathbb{S}$ | Octonions, sedenions; not rings |
| $\mathbb{R}$, $\mathbb{C}$, $\mathbb{Q}$ | The commutative division rings |

## Further Reading

- Tsit-Yuen Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for division rings, their centres and Wedderburn's little theorem.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for central simple algebras, the Brauer group and finite-dimensional division algebras.
- Paul M. Cohn, *Skew Field Constructions* (Cambridge University Press, 1977), for infinite-dimensional division rings and the free field.
