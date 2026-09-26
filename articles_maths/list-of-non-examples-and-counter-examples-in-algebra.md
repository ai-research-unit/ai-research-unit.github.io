# __List of Non-Examples and Counter-Examples in Algebra__

## Introduction

This article lists the objects of the corpus that fail exactly one axiom, or exactly one rung of one of the algebra ladders, and it names the axiom each one fails. The five failures the corpus uses most often are the ones the scope of this list opens with: $\mathbb{Z}[\sqrt{-5}]$, which is a domain but not a unique factorisation domain; $\mathbb{Z}[x]$, which is a unique factorisation domain but not a principal ideal domain; the split-complex numbers and the dual numbers, which are not domains; $M_2(\mathbb{R})$, which is not a division ring; and the octonions, whose multiplication is not associative.

Every entry points to the article that records the object and the failure. This article is a list: it introduces no definition, states no theorem, gives no proof, and carries no display mathematics. The article is made of examples and non-examples side by side; here, indeed, the non-examples are the substance of the list, and each is paired with the example above it on the ladder, so that the reader sees the property that fails and the object that has it.

## Not Domains: Zero Divisors

A **domain** is a commutative ring with $1 \neq 0$ and no zero divisors; the objects listed here fail that condition, each with an explicit pair of nonzero elements whose product is zero or a nonzero nilpotent element.

| Object | The property above it, and the failure | Introduced in |
|---|---|---|
| Split-complex numbers $\mathbb{D}$ | not a domain: $e_+ e_- = 0$ for $e_\pm = \tfrac12(1\pm t)$, both nonzero | *Split-Complex Algebra* |
| Dual numbers $\mathbb{D}'$ | not a domain: $\varepsilon^2 = 0$ with $\varepsilon \neq 0$ | *Dual Numbers Algebra* |
| $\mathbb{Z}/n\mathbb{Z}$ for composite $n$ | not a domain: the residue classes of the proper factors of $n$ multiply to $0$ | *Examples of Rings and Fields* |
| $\mathbb{Z}/4\mathbb{Z}$ | not reduced: the class of $2$ is a nonzero nilpotent | *Reduced Rings and the Nilradical* |
| The exterior algebra $\Lambda(V)$, $\dim V \geq 1$ | not a domain: $v \wedge v = 0$ for $v \in V$ | *The Exterior Algebra* |
| Split biquaternions $\mathbb{H}_{\mathbb{D}}$ | not a domain: they are $\mathbb{H}\oplus\mathbb{H}$, and have zero divisors | *Split-Biquaternion Algebra* |
| Biquaternions $\mathbb{B}$ | not a domain: $\mathbb{B} \cong M_2(\mathbb{C})$ has zero divisors | *Biquaternion Algebra* |
| Sedenions $\mathbb{S}$ | not a domain: the norm is not multiplicative and there are zero divisors | *Octonion Algebra* |
| The ring $\mathbb{Z}[\sqrt{-5}]$ as a counter-example | it is nevertheless a domain: it is the failure of unique factorisation, not of the domain axiom | *Unique Factorisation Domains* |

## Not Reduced: Nilpotents

A ring is **reduced** when its only nilpotent element is $0$; the objects here carry a nonzero nilpotent element, or a nonzero nilpotent ideal, and each row names the nilpotent that fails the condition.

| Object | The property above it, and the failure | Introduced in |
|---|---|---|
| $\mathbb{Z}/4\mathbb{Z}$ | not reduced: $2^2 = 0$ | *Reduced Rings and the Nilradical* |
| $\mathbb{Z}/p^n\mathbb{Z}$, $n \geq 2$ | not reduced: the class of $p$ is nilpotent | *Reduced Rings and the Nilradical* |
| $\mathbb{D}' = \mathbb{R}[\varepsilon]/(\varepsilon^2)$ | not reduced: $\varepsilon^2 = 0$ | *Dual Numbers Algebra* |
| $\mathbb{D}'_F = F[\varepsilon]/(\varepsilon^n)$ | not reduced: $\varepsilon$ is nilpotent of index $n$ | *Noetherian and Artinian Rings* |
| A degenerate Clifford algebra | not semisimple: the radical is a nonzero nilpotent ideal | *Degenerate Clifford Algebras and the Radical* |
| Non-example: $\mathbb{Z}/6\mathbb{Z}$ as non-reduced | it is not: $\mathbb{Z}/6\mathbb{Z} \cong \mathbb{Z}/2\mathbb{Z}\times\mathbb{Z}/3\mathbb{Z}$ is reduced, a product of fields | *Reduced Rings and the Nilradical* |

## Not Unique Factorisation Domains

A **unique factorisation domain** is a domain in which every nonzero nonunit is a product of irreducibles, uniquely up to order and associates, equivalently a domain in which every irreducible is prime. The standard failure is $\mathbb{Z}[\sqrt{-5}]$, where $6 = 2 \cdot 3 = (1+\sqrt{-5})(1-\sqrt{-5})$ exhibits two factorisations.

| Object | The property above it, and the failure | Introduced in |
|---|---|---|
| $\mathbb{Z}[\sqrt{-5}]$ | a domain and a Dedekind domain, but not a unique factorisation domain: two factorisations of $6$ | *Unique Factorisation Domains* |
| The class number as witness | the failure of unique factorisation is the nontriviality of the class group | *Dedekind Domains and Ideal Class Groups* |
| The ideal $(2, 1+\sqrt{-5})$ | a nonprincipal ideal whose square is principal; the obstruction made explicit | *Dedekind Domains and Ideal Class Groups* |
| $\overline{\mathbb{Z}}$, the ring of algebraic integers | not a unique factorisation domain, and not Noetherian | *Bézout Domains* |
| Non-example: $\mathbb{Z}[\sqrt{-5}]$ as a non-domain | it is a domain: the failure is the factorisation, not the zero-divisor axiom | *Integral Domains* |
| Non-example: $\mathbb{Z}[\sqrt{-5}]$ as non-Noetherian | it is Noetherian: it is a Dedekind domain | *Dedekind Domains and Ideal Class Groups* |

## Not Principal Ideal Domains

A **principal ideal domain** is a domain in which every ideal is generated by one element; it is a unique factorisation domain, so a failure of unique factorisation is also a failure of principality, but the corpus's sharp examples keep the two failures apart.

| Object | The property above it, and the failure | Introduced in |
|---|---|---|
| $\mathbb{Z}[x]$ | a unique factorisation domain but not principal: the ideal $(2,x)$ is not generated by one element | *Principal Ideal Domains* |
| $k[x_1,\dots,x_n]$, $n \geq 2$ | a unique factorisation domain but not principal: the ideal $(x_1,x_2)$ | *Principal Ideal Domains* |
| $\overline{\mathbb{Z}}$ | a Bézout domain but not Noetherian, hence not a principal ideal domain | *Bézout Domains* |
| $\mathbb{Z}[\sqrt{-5}]$ | not principal, because not a unique factorisation domain | *Unique Factorisation Domains* |
| $\mathbb{Z}\left[\tfrac{1+\sqrt{-19}}{2}\right]$ | a principal ideal domain that is **not** a Euclidean domain | *Euclidean Domains* |
| Non-example: $\mathbb{Z}$ as a non-principal domain | it is principal: every ideal is $(n)$ | *Principal Ideal Domains* |
| Non-example: $k[x,y]$ as a Bézout domain | it is not: its finitely generated ideal $(x,y)$ is not principal | *Bézout Domains* |

## Not Euclidean Domains

A **Euclidean domain** is a domain with a degree function and division with remainder; every Euclidean domain is a principal ideal domain, and the failure here is the converse: a principal ideal domain that admits no Euclidean degree.

| Object | The property above it, and the failure | Introduced in |
|---|---|---|
| $\mathbb{Z}\left[\tfrac{1+\sqrt{-19}}{2}\right]$ | a principal ideal domain but not Euclidean; the standard counter-example | *Euclidean Domains* |
| Non-example: $\mathbb{Z}[i]$ as non-Euclidean | it is Euclidean, with the norm as degree function | *Examples of Rings and Fields* |
| Non-example: $\mathbb{Z}$ as a non-Euclidean domain | it is Euclidean: it is norm-Euclidean with the absolute value as norm | *Euclidean Domains* |

## Not Division Rings or Division Algebras

A **division ring** is a ring in which every nonzero element is a unit; a **division algebra** is the corresponding algebra over a field. The failures are of two kinds: the objects with zero divisors, and the objects that are division algebras but not rings because associativity fails.

| Object | The property above it, and the failure | Introduced in |
|---|---|---|
| $M_2(\mathbb{R})$ | a simple algebra but not a division ring: the matrix with one nonzero entry is a nonzero zero divisor | *Examples of Algebras* |
| Split biquaternions $\mathbb{H}_{\mathbb{D}}$ | not a division algebra: $\cong \mathbb{H}\oplus\mathbb{H}$, with zero divisors and no nonzero nilpotents | *Split-Biquaternion Algebra* |
| Biquaternions $\mathbb{B}$ | not a division ring: $\cong M_2(\mathbb{C})$ | *Biquaternion Algebra* |
| $\mathbb{Z}$ | a domain but not a division ring: only $\pm 1$ are units | *The Integers* |
| The free algebra $k\langle x_1,\dots,x_n\rangle$ | a domain but not a division ring, and not commutative | *Tensor Powers and the Free Algebra* |
| The Weyl algebra $A_1$ | a domain but not a division ring; it embeds in a division ring of fractions | *Quotients of the Tensor Algebra* |
| The octonions $\mathbb{O}$ | a division algebra but **not a ring**: the multiplication is not associative | *Octonion Algebra* |
| The sedenions $\mathbb{S}$ | not even a division algebra: zero divisors | *Octonion Algebra* |
| Non-example: $\mathbb{H}$ as a division ring that is not a field | it is a division ring: the failure is commutativity, not inverses | *Quaternion Algebra* |
| Non-example: a finite division ring that is not a field | does not exist, by Wedderburn's little theorem | *Division Algebras* |

## Not Fields

A **field** is a commutative division ring; the objects here are domains or division rings that fail one of the two clauses, either commutativity or the existence of inverses for every nonzero element.

| Object | The property above it, and the failure | Introduced in |
|---|---|---|
| $\mathbb{H}$ | a division ring but not a field: not commutative | *Quaternion Algebra* |
| $\mathbb{O}$ | neither commutative nor associative, so neither a ring nor a field | *Octonion Algebra* |
| $\mathbb{Z}$ | an integral domain but not a field: $2$ is not a unit | *The Integers* |
| $\mathbb{Z}_p$, the $p$-adic integers | a principal ideal domain but not a field: $p$ is not a unit | *Absolute Values, Valuations and Completions* |
| $k[x]$, $k[[x]]$ | principal ideal domains but not fields: $x$ is not a unit | *Polynomial Rings and Rational Functions* |
| $\mathbb{Z}[\sqrt{-5}]$ | a domain but not a field, and not a unique factorisation domain | *Unique Factorisation Domains* |
| The zero ring | not a field: $1 = 0$ | *Rings* |
| Non-example: $\mathbb{D}$ and $\mathbb{D}'$ as fields | fail already the domain axiom: a field is a domain | *Split-Complex Algebra* |
| Non-example: $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$, $\mathbb{F}_p$ as non-fields | they are fields: the failures above are not generic | *Fields* |

## Not Associative and Not Commutative

**Associativity** and **commutativity** are the two axioms that survive the doubling chain and fail one at a time; the objects here each fail exactly one of them.

| Object | The property above it, and the failure | Introduced in |
|---|---|---|
| The octonions $\mathbb{O}$ | not associative: $(e_1e_2)e_4 = e_7$ but $e_1(e_2e_4) = -e_7$; alternative and power-associative | *Octonion Algebra* |
| The sedenions $\mathbb{S}$ | neither associative nor alternative, and not a division algebra | *Octonion Algebra* |
| A Lie algebra $\mathfrak{g}$ | not associative and not commutative: $[x,y] = -[y,x]$ | *Lie Algebras* |
| A Jordan algebra | not associative: the Jordan identity replaces associativity | *Jordan Algebras* |
| The free algebra $k\langle x_1,\dots,x_n\rangle$ | associative but not commutative for $n \geq 2$ | *Tensor Powers and the Free Algebra* |
| The exterior algebra $\Lambda(V)$ | associative but graded-commutative, not commutative for $\dim V \geq 2$ | *The Exterior Algebra* |
| $M_2(\mathbb{R})$ | associative but not commutative | *Examples of Algebras* |
| $\mathbb{H}$ | associative but not commutative | *Quaternion Algebra* |
| Non-example: $\mathbb{C}$ as non-commutative | it is commutative: commutativity is lost only at $\mathbb{H}$ | *The Complex Numbers* |

## Not Semisimple

A **semisimple** algebra is a product of matrix algebras over division rings; by Wedderburn–Artin it is exactly an algebra whose radical vanishes. The failures here have a nonzero radical, and the group algebra in the modular case is the classical one.

| Object | The property above it, and the failure | Introduced in |
|---|---|---|
| $k[G]$ with $\operatorname{char} k$ dividing $|G|$ | not semisimple: Maschke's theorem fails, and the radical is nonzero | *Group Algebras* |
| The modular group algebra | the failure of Maschke's theorem and the decomposition of the regular representation | *Modular Representation Theory* |
| $k[x]/(x^2)$ | not semisimple: the radical is $(x)$ | *Simple and Semisimple Modules* |
| A degenerate Clifford algebra | not semisimple: the radical is nonzero | *Degenerate Clifford Algebras and the Radical* |
| $\mathbb{Z}/4\mathbb{Z}$ | not semisimple as a ring over itself: the radical is $(2)$ | *Noetherian and Artinian Rings* |
| The dual numbers $\mathbb{D}'$ | not semisimple: local with a nilpotent maximal ideal | *Dual Numbers Algebra* |
| Non-example: a semisimple algebra over a field of characteristic $0$ | it is semisimple: Maschke's theorem holds when the characteristic does not divide the group order | *Group Algebras* |

## Summary

The list gathers the objects of the corpus that fail exactly one axiom. The failures of the multiplicative structure are the zero divisors of the split-complex numbers, the dual numbers, $\mathbb{Z}/n\mathbb{Z}$ for composite $n$, the exterior algebra and the split-biquaternions; the nilpotents of $\mathbb{Z}/4\mathbb{Z}$, the dual numbers and a degenerate Clifford algebra; the matrix algebra $M_2(\mathbb{R})$, the biquaternions and the sedenions as non-division rings; and $\mathbb{Z}$, $\mathbb{Z}_p$, $k[x]$ and $\mathbb{Z}[\sqrt{-5}]$ as non-fields. The failures of the divisibility ladders are $\mathbb{Z}[\sqrt{-5}]$, which is not a unique factorisation domain, $\mathbb{Z}[x]$ and $k[x_1,\dots,x_n]$, which are not principal ideal domains, and $\mathbb{Z}\left[\tfrac{1+\sqrt{-19}}{2}\right]$, which is a principal ideal domain that is not Euclidean. The failures of the structural axioms are the octonions and the sedenions, which are not associative, the free algebra and the exterior algebra, which are not commutative, and the modular group algebra, which is not semisimple. Each row names the example above the failure, so that the strictness of the ladder is visible in the list itself.

## Summary of Notation

The article denotes its objects by name; the symbols appearing in the tables are those of the introducing articles.

| Symbol | Meaning |
|---|---|
| $\mathbb{Z}[\sqrt{-5}]$, $\overline{\mathbb{Z}}$ | the standard non-unique-factorisation domain, the algebraic integers |
| $\mathbb{Z}[x]$, $k[x_1,\dots,x_n]$ | polynomial rings, unique factorisation domains that are not principal |
| $\mathbb{D}$, $\mathbb{D}'$ | split-complex numbers, dual numbers |
| $M_2(\mathbb{R})$, $\mathbb{B}$ | matrix algebra, biquaternions |
| $\mathbb{H}$, $\mathbb{O}$, $\mathbb{S}$ | quaternions, octonions, sedenions |
| $\Lambda(V)$, $k\langle x_1,\dots,x_n\rangle$ | exterior algebra, free algebra |
| $k[G]$ | group algebra |
| $\mathbb{Z}/n\mathbb{Z}$ | residue rings |
| $\mathbb{Q}$, $\mathbb{C}$, $\mathbb{F}_p$ | the rationals, the complex numbers and the prime fields |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Wedderburn–Artin theory and the standard counter-examples in the structure of algebras.
- Paulo Ribenboim, *Classical Theory of Algebraic Numbers* (Springer, 2001), for $\mathbb{Z}[\sqrt{-5}]$, the failure of unique factorisation and the ideal class group.
- Thomas Hungerford, *Algebra* (Springer, 1974), for the divisibility ladder and the counter-examples $\mathbb{Z}[x]$ and $\mathbb{Z}[\sqrt{-5}]$.
- Richard Schafer, *An Introduction to Nonassociative Algebras* (Dover, 1995), for the octonions, the sedenions and the failure of associativity.
