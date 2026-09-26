
# __List of Rings by Their Idempotents__

## Introduction

This article lists the rings of the corpus by their idempotents — the elements $e$ with $e^2 = e$ — the direct sum decompositions those idempotents induce, the Peirce decomposition of a module or an algebra relative to an orthogonal family of them, and the two extreme cases: the von Neumann regular rings, in which every ideal is idempotent-generated, and the domains and local rings, in which the only idempotents are $0$ and $1$. Every entry points to the article that introduces the object.

The idempotents of a ring are indifferent to its additive and ideal structure and sensitive to its decomposition: a nontrivial idempotent $e$ with $e \neq 0, 1$ splits the ring as $R = Re \oplus R(1-e)$ and its module as $M = eM \oplus (1-e)M$, while a ring with no nontrivial idempotent is indecomposable and is called connected. The list records each ring with its idempotents, with the decomposition they give, and with the corner algebra $eRe$ that the Peirce decomposition isolates.

The article introduces nothing and proves nothing. It records examples and non-examples side by side.

## The Idempotents of Each Ring

| Ring | The idempotents | Their number | Introduced in |
|---|---|---|---|
| a field $k$ | $0, 1$ | $2$ | *Fields* |
| a domain $R$ | $0, 1$ | $2$ | *Integral Domains* |
| a local ring | $0, 1$ | $2$ | *Localization and the Fraction Field* |
| $\mathbb{H}$, a division ring | $0, 1$ | $2$ | *Quaternion Algebra* |
| $\mathbb{Z}/4\mathbb{Z}$ | $0, 1$ | $2$ | *Reduced Rings and the Nilradical* |
| $\mathbb{Z}/p^n\mathbb{Z}$ | $0, 1$ | $2$ | *Reduced Rings and the Nilradical* |
| $\mathbb{D}' = \mathbb{R}[\varepsilon]/(\varepsilon^2)$ | $0, 1$ | $2$ | *Dual-Numbers Algebra* |
| $\mathbb{F}_2[C_2] \cong \mathbb{F}_2[x]/(x+1)^2$ | $0, 1$ | $2$ | *Examples of Rings and Fields* |
| $\mathbb{Z}/6\mathbb{Z}$ | $0, 1, 3, 4$ | $4$ | *Modular Arithmetic and the Ring of Residues* |
| $\mathbb{Z}/12\mathbb{Z}$ | $0, 1, 4, 9$ | $4$ | *Modular Arithmetic and the Ring of Residues* |
| $\mathbb{Z}/n\mathbb{Z}$ | one for each factorisation into coprime parts | $2^{\omega(n)}$ | *Modular Arithmetic and the Ring of Residues* |
| $\mathbb{D} = \mathbb{R}[j]/(j^2-1)$ | $0, 1, e_+, e_-$ | $4$ | *Split-Complex Algebra* |
| $\mathbb{R}[x]/(x^2-1)$ | $0, 1$, the two class idempotents | $4$ | *Examples of Rings and Fields* |
| $\mathbb{H}_{\mathbb{D}}$, the split-biquaternions | $0, e_+, e_-, e_0$ | $4$ | *Split-Biquaternion Algebra* |
| $\mathbb{Q}[C_3]$ | $0, 1$ and the two minimal ones | $4$ | *Examples of Rings and Fields* |
| $M_2(\mathbb{R})$ | the projections | infinitely many | *Matrix Algebras* |
| $\mathbb{B}$, the biquaternions | the complex multiples of the idempotents | infinitely many | *Biquaternion Ideals and Peirce Decomposition* |
| a Boolean ring $B$ | every element | $\lvert B \rvert$ | *Von Neumann Regular Rings* |

The dichotomy the table records is between the rings that are connected, with $0$ and $1$ as their only idempotents, and the rings that split. The domains, the fields, the division rings and the local rings are connected; $\mathbb{Z}/n\mathbb{Z}$ has $2^{\omega(n)}$ idempotents, where $\omega(n)$ counts the distinct primes dividing $n$, so $\mathbb{Z}/6\mathbb{Z}$ and $\mathbb{Z}/12\mathbb{Z}$ have four; and the Boolean rings have an idempotent for every element. The split-biquaternions and the split-complex numbers have exactly four idempotents each, and $\mathbb{H}$ has two, which is the sharpest contrast between the quaternion family and its split relatives.

## The Direct Sum Decompositions

| Ring | The idempotent $e$ | The decomposition | Introduced in |
|---|---|---|---|
| any ring | $e$ | $R = Re \oplus R(1-e)$ | *Rings*, §§8–9 |
| $\mathbb{Z}/6\mathbb{Z}$ | $3$ | $\mathbb{Z}/6\mathbb{Z} \cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/3\mathbb{Z}$ | *Modular Arithmetic and the Ring of Residues* |
| $\mathbb{D}$ | $e_+$ | $\mathbb{D} \cong \mathbb{R} e_+ \oplus \mathbb{R} e_- \cong \mathbb{R} \times \mathbb{R}$ | *Split-Complex Algebra* |
| $\mathbb{H}_{\mathbb{D}}$ | $e_+$ | $\mathbb{H}_{\mathbb{D}} \cong \mathbb{H}e_+ \oplus \mathbb{H}e_-$ | *Split-Biquaternion Zero Divisors* |
| $R \times S$ | $(1,0)$ | the product by construction | *Examples of Rings and Fields* |
| $\mathbb{Q}[C_3]$ | the minimal idempotents | $\mathbb{Q}[C_3] \cong \mathbb{Q} \times \mathbb{Q}(\zeta_3)$ | *Examples of Rings and Fields* |
| $\mathbb{R}[x]/(x^2-1)$ | $e_{\pm}$ | $\mathbb{R}[x]/(x^2-1) \cong \mathbb{R} \times \mathbb{R}$ | *Examples of Rings and Fields* |
| a Boolean ring $B$ | every idempotent $e$ | $B = Be \oplus B(1-e)$ for every $e$, every element being idempotent | *Von Neumann Regular Rings* |
| a commutative Artinian ring | the primitive idempotents | the product of the local rings $R e_i$ | *Noetherian and Artinian Rings* |

A nontrivial idempotent $e$ satisfies $e(1-e) = 0$, so $R = Re \oplus R(1-e)$ is a direct sum of the two-sided ideals $Re$ and $R(1-e)$, and the two ideals are rings in their own right with identities $e$ and $1-e$. A family of idempotents that are orthogonal, $e_i e_j = 0$ for $i \neq j$, and complete, $\sum e_i = 1$, gives the decomposition $R = \bigoplus_i R e_i$; the primitive idempotents are those that cannot be split further, and for a commutative Artinian ring the primitive decomposition is the product of its localisations, as recorded in *Noetherian and Artinian Rings* and in *List of Reduced, Local and Product Rings*.

## The Peirce Decomposition

| Object | The orthogonal family | The decomposition | Introduced in |
|---|---|---|---|
| a module $M$ over $R$ | a single idempotent $e$ | $M = eM \oplus (1-e)M$ | *Modules* |
| an algebra $A$ | a single idempotent $e$ | $A = eAe \oplus eA(1-e) \oplus (1-e)Ae \oplus (1-e)A(1-e)$ | *Biquaternion Ideals and Peirce Decomposition* |
| $\mathbb{B} \cong M_2(\mathbb{C})$ | $p = E_{11}$, $q = E_{22}$ | the four one-dimensional corners | *Biquaternion Ideals and Peirce Decomposition* |
| $M_2(\mathbb{R})$ | $E_{11}, E_{22}$ | the column decomposition of $\mathbb{R}^2$ | *Matrix Algebras* |
| $R \times S$ | $(1,0)$, $(0,1)$ | the two components | *Examples of Rings and Fields* |
| a group algebra $k[G]$ | the idempotents of the group | $k[G] = \bigoplus e_i k[G] e_i \oplus \text{off-diagonal}$ | *Group Algebras* |

The Peirce decomposition relative to a complete orthogonal family of idempotents $e_1 + \cdots + e_n = 1$ writes a module as $M = \bigoplus_i e_i M$ and an algebra as the direct sum of the corner algebras $e_i A e_j$. The biquaternion case is the corpus's worked example: with $p = E_{11}$ and $q = E_{22}$ the four corners are one-dimensional over $\mathbb{C}$, and the off-diagonal ones are spanned by the nilpotents $x$ and $y$, as recorded in *Biquaternion Ideals and Peirce Decomposition*.

## The von Neumann Regular Rings

| Ring | Why every ideal is idempotent-generated | Introduced in |
|---|---|---|
| a Boolean ring | every element is idempotent, so every ideal is generated by idempotents | *Von Neumann Regular Rings* |
| a product of fields | the primitive idempotents generate the principal ideals | *Examples of Rings and Fields* |
| $\prod_i k_i$ over a family of fields | the idempotents of the product generate the ideals | *Examples of Rings and Fields* |
| a commutative von Neumann regular ring | each localisation at a maximal ideal is a field, and every principal ideal is generated by an idempotent | *Von Neumann Regular Rings* |
| a reduced ring of Krull dimension zero | equivalently von Neumann regular | *Von Neumann Regular Rings* |
| $\mathbb{Z}$, $k[x]$, $\mathbb{Z}[\sqrt{-5}]$ | not von Neumann regular: the ideal $(2)$ is not generated by an idempotent | *Integral Domains* |
| $\mathbb{Z}/4\mathbb{Z}$ | not von Neumann regular: $2 \cdot 2 = 0$, and the maximal ideal is not idempotent-generated | *Reduced Rings and the Nilradical* |

A ring is von Neumann regular when every principal left ideal is generated by an idempotent, equivalently when every finitely generated left ideal is idempotent-generated. The commutative von Neumann regular rings are exactly the reduced rings of Krull dimension zero, equivalently those whose localisation at every maximal ideal is a field; the Boolean rings are the characteristic-two examples. The domains and the local rings are the non-examples: in a domain the principal ideal $(a)$ for $a$ neither zero nor a unit is not generated by an idempotent, since the only idempotents are $0$ and $1$, and $\mathbb{Z}/4\mathbb{Z}$ fails because $2 \cdot 2 = 0$. The class is the subject of *Von Neumann Regular Rings*.

## The Rings with Few Idempotents

| Ring | The idempotents | Why | Introduced in |
|---|---|---|---|
| a domain | $0, 1$ | $e(1-e) = 0$ forces $e = 0$ or $1$ | *Integral Domains* |
| a local ring | $0, 1$ | the nonunits form the maximal ideal, and a nontrivial idempotent is a nonunit with a nonunit complement | *Localization and the Fraction Field* |
| a division ring | $0, 1$ | a nonzero idempotent is a unit, and the only unit idempotent is $1$ | *Division Rings* |
| $\mathbb{Z}/p^n\mathbb{Z}$ | $0, 1$ | a local ring | *Reduced Rings and the Nilradical* |
| $\mathbb{D}'$ | $0, 1$ | a local ring | *Dual-Numbers Algebra* |
| $\mathbb{F}_2[C_2]$ | $0, 1$ | isomorphic to $\mathbb{F}_2[x]/(x+1)^2$, a local ring | *Examples of Rings and Fields* |
| a connected ring | $0, 1$ | the definition of connected | *Rings*, §§8–9 |

A ring with $0$ and $1$ as its only idempotents is connected, equivalently indecomposable: it is not the product of two nonzero rings. Every domain, every local ring and every division ring is connected, and a nontrivial idempotent is exactly what a product fails to exclude. The scarcity of idempotents is therefore not a defect but the obstruction that makes the ideal theory of a domain a divisibility theory rather than a decomposition theory.

## Warnings

| Object | Why it is not in the list of rings with idempotents to compare | Introduced in |
|---|---|---|
| $\mathbb{O}$, the octonions | not a ring: the multiplication is not associative, so $e^2 = e$ is not defined in the ring sense | *Octonion Algebra* |
| the zero ring $\{0\}$ | $0 = 1$, and the single element is an idempotent, excluded by the convention $1 \neq 0$ | *Rings*, §2 |
| $M_2(\mathbb{R})$ as a "split" ring | it is simple, so it has no nontrivial two-sided idempotent splitting, although it has many one-sided idempotents | *Matrix Algebras* |
| $\mathbb{B}$ as a "split" ring | simple, like $M_2(\mathbb{C})$; its idempotents give the Peirce corners and not a product decomposition | *Biquaternion Ideals and Peirce Decomposition* |

The third and fourth rows record the distinction the list rests on: an idempotent gives a product decomposition only when it is central, and the idempotents of a matrix algebra are not. The split-biquaternions and the split-complex numbers are products because their idempotents are central, while the matrix ring and the biquaternions are simple and their idempotents are not.

## Summary

This article has listed the rings of the corpus by their idempotents. The connected rings — the fields, the domains, the local rings, the division rings, $\mathbb{Z}/4\mathbb{Z}$, $\mathbb{Z}/p^n\mathbb{Z}$, the dual numbers and $\mathbb{F}_2[C_2]$ — have $0$ and $1$ alone; the split rings — $\mathbb{Z}/6\mathbb{Z}$, $\mathbb{Z}/12\mathbb{Z}$, the split-complex numbers, the split-biquaternions, $\mathbb{R}[x]/(x^2-1)$ and $\mathbb{Q}[C_3]$ — have four; the matrix ring and the biquaternions have infinitely many one-sided idempotents without a product decomposition, since they are simple; and the Boolean rings have one for every element. The article has recorded the direct sum decomposition $R = Re \oplus R(1-e)$ and the product decompositions it gives, the Peirce decomposition $A = \bigoplus_{i,j} e_i A e_j$ relative to a complete orthogonal family with the biquaternion corners as the worked case, and the separation of the von Neumann regular rings, in which every ideal is idempotent-generated, from the domains and local rings, in which the idempotents are scarce.

## Summary of Notation

A catalogue denotes its objects by name rather than by symbol. The symbols that appear in the tables are the following.

| Symbol | Meaning |
|---|---|
| $e$ | An idempotent, $e^2 = e$ |
| $e_{\pm} = \tfrac{1}{2}(1 \pm j)$ | The idempotents of the split-complex numbers and the split-biquaternions |
| $e_0 = 1$ | The identity, the trivial idempotent |
| $p = E_{11}$, $q = E_{22}$ | Orthogonal matrix-unit idempotents, $p + q = 1$ |
| $x, y$ | The nilpotent off-diagonal elements of the Peirce corners |
| $e_i A e_j$ | A Peirce corner of the algebra $A$ |
| $\omega(n)$ | The number of distinct primes dividing $n$ |
| $eM$, $(1-e)M$ | The two summands of the Peirce decomposition of a module |

## Further Reading

- Tsit-Yuen Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for the idempotents, the Peirce decomposition and the corner algebras.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Peirce decomposition treated systematically.
- Irving Kaplansky, *Commutative Rings* (University of Chicago Press, revised ed. 1974), for the von Neumann regular rings, the reduced rings of Krull dimension zero and the idempotents of a Noetherian ring.
