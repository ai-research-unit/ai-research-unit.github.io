# __List of Division Algebras__

## Introduction

This article lists the division algebras and division rings the corpus meets, grouped by the theorem that classifies them: Frobenius' theorem for the finite-dimensional real associative division algebras, Wedderburn's little theorem for the finite division rings, Hurwitz' theorem for the normed division algebras, and the structure theory of the central division algebras over a general field. Beside each family the list records the article that proves the classification and the objects that fail to be division algebras.

Every entry points to the article that introduces the object. This article is a list: it introduces no definition, states no theorem, gives no proof, and carries no display mathematics. It records examples and non-examples side by side, a non-example being an algebra that has zero divisors or fails associativity, or a division algebra that is not a ring, with the failure named and the article that records it.

## Division Algebras and Division Rings

A **division algebra** over a field $k$ is a $k$-algebra with identity in which every nonzero element is invertible; a **division ring**, or skew field, is a ring with the same property, without a chosen ground field, and the centre of a division ring is a field over which it is a division algebra. The two notions differ in scope: every division ring is a division algebra over its centre, but the centre may be small and the algebra may be infinite-dimensional there.

| Object | The property it has | Introduced in |
|---|---|---|
| Division algebra over $k$ | every nonzero element invertible; no zero divisors | *Division Algebras* |
| Unit group $D^\times = D\setminus\{0\}$ | the nonzero elements, a group under multiplication | *Division Algebras* |
| Centre $Z(D)$ | a field; $D$ is an algebra over it | *Division Algebras* |
| Matrix algebra $M_n(D)$ over a division algebra | simple; the building block of the Wedderburn–Artin decomposition | *Simple and Semisimple Modules* |
| Warning: the octonions $\mathbb{O}$ | a division algebra but not a ring: the multiplication is not associative | *Octonion Algebra* |
| Warning: the algebra of a division ring | the centre is a field, so a division ring is a division algebra over its centre, possibly of infinite dimension there | *Division Algebras* |

## The Real Division Algebras: Frobenius' Theorem

**Frobenius' theorem** states that the finite-dimensional associative real division algebras are exactly $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$; in particular $\mathbb{R}$ is the only one-dimensional and the only ordered one, $\mathbb{C}$ is the only commutative two-dimensional one, and $\mathbb{H}$ is the only non-commutative one. A finite-dimensional real algebra without zero divisors is a division algebra, so the theorem is also a statement about the absence of zero divisors in those dimensions.

| Algebra | The property it has | Introduced in |
|---|---|---|
| $\mathbb{R}$ | dimension $1$; the only one-dimensional and the only ordered real division algebra | *Division Algebras* |
| $\mathbb{C}$ | dimension $2$; the only two-dimensional real division algebra; commutative and algebraically closed | *The Complex Numbers* |
| $\mathbb{H}$ | dimension $4$; the only non-commutative real division algebra; a division ring but not a field | *Quaternion Algebra* |
| Frobenius' theorem | the complete list $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$ of real division algebras | *Division Algebras* |
| Non-example: the split biquaternions $\mathbb{H}_{\mathbb{D}}$ | have zero divisors: they are $\mathbb{H}\oplus\mathbb{H}$, so not a division algebra, and they have no nonzero nilpotents | *Split-Biquaternion Algebra* |
| Non-example: the biquaternions $\mathbb{B}$ | have zero divisors: $\mathbb{B} \cong M_2(\mathbb{C})$ is not a division algebra | *Biquaternion Algebra* |

## The Finite Division Rings: Wedderburn's Little Theorem

**Wedderburn's little theorem** states that every finite division ring is a field, so the finite division algebras are exactly the finite fields $\mathbb{F}_q$. One consequence is that a skew field is never finite: every division ring that is not a field is infinite, and the infinite examples are the quaternions, the division ring of fractions of the Weyl algebra and the central division algebras over infinite fields.

| Object | The property it has | Introduced in |
|---|---|---|
| Wedderburn's little theorem | every finite division ring is a field | *Division Algebras* |
| $\mathbb{F}_q$, $q = p^f$ | the finite field of order $q$; a finite division algebra | *Finite Fields* |
| $\mathbb{F}_p$ | the prime field of characteristic $p$; a finite division ring and a field | *Finite Fields* |
| Frobenius automorphism of $\mathbb{F}_q$ | the field automorphism $x \mapsto x^p$, of order $f$ | *Finite Fields* |
| Non-example: a finite division ring that is not a field | does not exist, by Wedderburn's little theorem | *Division Algebras* |

## The Normed Division Algebras: Hurwitz' Theorem

A **normed division algebra** is an algebra with a multiplicative anisotropic norm; the norm determines an involution $\bar x$, and $x^{-1} = \bar x/N(x)$. **Hurwitz' theorem** states that a finite-dimensional real normed division algebra has dimension $1$, $2$, $4$ or $8$, and is one of the reals, the complexes, the quaternions and the octonions. The Cayley–Dickson doubling produces the chain and the sedenions show that the norm stops being multiplicative in dimension $16$.

| Algebra | The property it has | Introduced in |
|---|---|---|
| $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$ | the associative normed division algebras, of dimensions $1$, $2$ and $4$ | *Normed Division Algebras and the Hurwitz Theorem* |
| $\mathbb{O}$ | dimension $8$; the only non-associative normed division algebra | *Octonion Algebra* |
| Hurwitz' theorem | the four normed division algebras and the exclusion of dimension $16$ | *Normed Division Algebras and the Hurwitz Theorem* |
| Cayley–Dickson double $\mathrm{CD}(A)$ | the doubling construction producing the chain and losing one property per step | *Normed Division Algebras and the Hurwitz Theorem* |
| Sums-of-squares identities | the existence of the identity exactly for $n = 1, 2, 4, 8$ | *Normed Division Algebras and the Hurwitz Theorem* |
| Non-example: the sedenions $\mathbb{S}$ | fail the multiplicative norm and have zero divisors; dimension $16$ | *Octonion Algebra* |
| Non-example: $\mathbb{O}$ as a division ring | fails to be a ring: the multiplication is not associative | *Octonion Algebra* |

## The Central Division Algebras over a General Field

Over a general field the finite-dimensional division algebras are the division-algebra parts of the central simple algebras: by Wedderburn's structure theorem every central simple $F$-algebra is a matrix algebra $M_n(D)$ over a central division $F$-algebra $D$, and the classes of central simple algebras under similarity form the **Brauer group** $\operatorname{Br}(F)$. The **quaternion algebras** $(a,b)_F$ and the **cyclic algebras** are the standard constructions, and the index and exponent of a class measure the size of its division algebra.

| Algebra | The property it has | Introduced in |
|---|---|---|
| Central division algebra over $F$ | finite-dimensional, centre exactly $F$, no zero divisors | *Central Simple Algebras and the Brauer Group* |
| Quaternion algebra $(a,b)_F$ | $u^2 = a$, $v^2 = b$, $uv = -vu$; a division algebra for suitable $a$, $b$ | *Central Simple Algebras and the Brauer Group* |
| $\mathbb{H} = (-1,-1)_{\mathbb{R}}$ | the real quaternion algebra, a division algebra | *Quaternion Algebra* |
| Cyclic algebra $(\chi,a)$ | built from a cyclic field extension and an element $a$; a division algebra when $a$ is not a norm | *Central Simple Algebras and the Brauer Group* |
| Brauer group $\operatorname{Br}(F)$ | the similarity classes of central simple algebras under $\otimes_F$; the division algebras as representatives | *Central Simple Algebras and the Brauer Group* |
| Index and exponent | $\operatorname{ind}(A) = \sqrt{\dim_F D}$ and $\exp(A)$, the order in the Brauer group | *Central Simple Algebras and the Brauer Group* |
| Hasse invariant $\operatorname{inv}_v(D)$ | the local invariant of a division algebra over a number field | *Class Field Theory* (Part I) |
| Division ring of fractions of an Ore domain | the non-commutative analogue of the fraction field, a division ring not finite-dimensional over its centre | *Ore Domains and Division Rings of Fractions* |
| Division algebra over $\mathbb{C}$ | there is none beyond $\mathbb{C}$: an algebraically closed field carries no proper finite-dimensional division algebra | *Algebraically Closed Fields* |
| Central division algebra over a local field | the unique one of each index, determined by its Hasse invariant | *Class Field Theory* (Part I) |
| Division algebra of index $n$ | $\dim_F D = n^2$; split by a field extension of degree $n$ | *Central Simple Algebras and the Brauer Group* |
| Non-example: a quaternion algebra with $a$ a norm | is isomorphic to $M_2(F)$, so it is not a division algebra | *Central Simple Algebras and the Brauer Group* |
| Non-example: $\mathbb{B}$ as a central division algebra over $\mathbb{R}$ | fails: its centre is $\mathbb{C}$ and it is not central over $\mathbb{R}$ | *Biquaternion Algebra* |

## The Four Theorems Compared

The four classification statements differ in their hypotheses and in the class they pin down, and the table gathers them so that the scope of each is visible: Frobenius' theorem restricts the ground field to $\mathbb{R}$ and the algebra to be associative, Wedderburn's little theorem restricts the division ring to be finite, Hurwitz' theorem restricts the algebra to carry a multiplicative norm, and the theory over a general field keeps only the central simple algebras and their classes in the Brauer group.

| Theorem | The class it classifies | The hypothesis that makes the class small | Introduced in |
|---|---|---|---|
| Frobenius | the associative real division algebras: $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$ | finite dimension over $\mathbb{R}$, associative | *Division Algebras* |
| Wedderburn (little) | the finite division rings: the finite fields $\mathbb{F}_q$ | finite cardinality | *Division Algebras* |
| Hurwitz | the normed division algebras: $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$, $\mathbb{O}$ | a multiplicative anisotropic norm | *Normed Division Algebras and the Hurwitz Theorem* |
| Wedderburn's structure theorem | every central simple algebra is $M_n(D)$ over a central division algebra | central and finite-dimensional over $F$ | *Central Simple Algebras and the Brauer Group* |
| The Brauer group | the central division algebras up to similarity | the similarity relation and the tensor product | *Central Simple Algebras and the Brauer Group* |

The hypotheses are not redundant: dropping associativity from Frobenius' theorem admits $\mathbb{O}$, dropping finiteness from Wedderburn's little theorem admits $\mathbb{H}$, and dropping the norm from Hurwitz' theorem admits the division rings that are not finite-dimensional over their centre.

## Summary

The list gathers the division algebras and division rings of the corpus. The real division algebras are $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$, by Frobenius' theorem, with the split biquaternions $\mathbb{H}_{\mathbb{D}}$ and the biquaternions as the non-examples that have zero divisors. The finite division rings are the finite fields, by Wedderburn's little theorem, which forces every skew field that is not a field to be infinite. The normed division algebras are $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$ and $\mathbb{O}$, by Hurwitz' theorem, with the octonions recorded as a division algebra that is not a ring and the sedenions as the first system with zero divisors. The central division algebras over a general field are the division algebras $D$ with $M_n(D)$ central simple, the quaternion and cyclic algebras among them, classified up to similarity by the Brauer group with its index and exponent, and the division ring of fractions of an Ore domain is the non-commutative example that is not finite-dimensional over its centre. The non-examples — the split biquaternions $\mathbb{H}_{\mathbb{D}}$, the biquaternions, the sedenions, a quaternion algebra that splits to $M_2(F)$, the octonions as a non-ring, and the biquaternions as not central over $\mathbb{R}$ — each name the failure.

## Summary of Notation

The article denotes its objects by name; the symbols appearing in the tables are those of the introducing articles.

| Symbol | Meaning |
|---|---|
| $D$, $D^\times$, $Z(D)$ | division algebra or ring, its units, its centre |
| $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$, $\mathbb{O}$, $\mathbb{S}$ | real, complex, quaternion, octonion and sedenion algebras |
| $\mathbb{F}_q$, $\mathbb{F}_p$ | finite fields |
| $(a,b)_F$ | quaternion algebra over $F$ |
| $\operatorname{Br}(F)$, $\operatorname{ind}$, $\exp$ | Brauer group, index, exponent |
| $M_n(D)$ | matrix algebra over a division algebra |
| $N(x)$, $x^{-1} = \bar x/N(x)$ | norm and inverse in a normed division algebra |
| $\mathrm{CD}(A)$ | Cayley–Dickson double |
| $\mathbb{B}$, $\mathbb{H}_{\mathbb{D}}$ | biquaternions and split biquaternions |

## Further Reading

- Ferdinand Georg Frobenius, *Über lineare Substitutionen und bilineare Formen* (Journal für die reine und angewandte Mathematik, 1878), for the classification of the real associative division algebras.
- Joseph Wedderburn, *On Hypercomplex Numbers* (Proceedings of the London Mathematical Society, 1908), for the theorem that every finite division ring is a field and the structure theory of algebras.
- Adolf Hurwitz, *Über die Composition der quadratischen Formen von beliebig vielen Variabeln* (Nachrichten von der Königlichen Gesellschaft der Wissenschaften zu Göttingen, 1898), for the normed division algebras.
- Philippe Gille and Tamás Szamuely, *Central Simple Algebras and Galois Cohomology* (Cambridge University Press, 2006), for the central division algebras, the quaternion and cyclic algebras and the Brauer group.
