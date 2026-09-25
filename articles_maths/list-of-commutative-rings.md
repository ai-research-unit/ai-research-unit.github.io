
# __List of Commutative Rings__

## Introduction

This article lists the commutative rings that the corpus meets, with the dimension, the units and the zero divisors of each. Every entry points to the article that introduces the object.

The list gathers the number systems and their quotients, the quadratic and cyclotomic integer rings, the polynomial, power series and localisation rings, the two-dimensional real algebras of the split-complex and dual numbers, and the product rings. The non-commutative rings are the subject of *List of Non-Commutative Rings*; a ring that a reader may expect in a list of commutative rings and that is not commutative is named in the warnings.

The article introduces nothing and proves nothing. It records examples and non-examples side by side.

## The Convention on Dimension

Dimension means the Krull dimension for the rings of this list, and the vector-space dimension over the ground field for the finite-dimensional real algebras $\mathbb{D}$ and $\mathbb{D}'$; where both readings are available they are written together. Thus a field has dimension $0$, a principal ideal domain that is not a field has dimension $1$, the ring $\mathbb{Z}/n\mathbb{Z}$ has dimension $0$, the polynomial ring in $n$ variables has dimension $n$, and the split-complex and dual numbers have vector-space dimension $2$ over $\mathbb{R}$ and Krull dimension $0$. The Krull dimension is introduced in *Integral Extensions and Krull Dimension* and the polynomial case in *Polynomial Rings and Rational Functions*.

## The Number Systems and Their Quotients

| Ring | Dimension | Units | Zero divisors | Introduced in |
|---|---|---|---|---|
| $\mathbb{Z}$ | $1$ | $\pm 1$ | none | *The Integers* |
| $\mathbb{Q}$ | $0$ | all nonzero | none | *The Rational Numbers* |
| $\mathbb{R}$ | $0$ | all nonzero | none | *The Real Numbers* |
| $\mathbb{C}$ | $0$ | all nonzero | none | *The Complex Numbers* |
| $\mathbb{Z}/n\mathbb{Z}$ | $0$ | the classes coprime to $n$, of order $\varphi(n)$ | every nonunit when $n$ is composite | *Modular Arithmetic and the Ring of Residues* |
| $\mathbb{F}_p$ | $0$ | cyclic of order $p-1$ | none | *Finite Fields* |
| $\mathbb{F}_q$, $q = p^n$ | $0$ | cyclic of order $q-1$ | none | *Finite Fields* |
| $\mathbb{Z}/4\mathbb{Z}$ | $0$ | $\{1, 3\}$ | $2$ is nilpotent | *Reduced Rings and the Nilradical* |
| $\mathbb{Z}/6\mathbb{Z}$ | $0$ | $\{1, 5\}$ | $2 \cdot 3 = 0$; reduced, the product $\mathbb{F}_2 \times \mathbb{F}_3$ | *Modular Arithmetic and the Ring of Residues* |

The non-example that fixes this section is $\mathbb{Z}/6\mathbb{Z}$, a commutative reduced ring that is not an integral domain.

## Quadratic and Cyclotomic Integer Rings

| Ring | Dimension | Units | Zero divisors | Introduced in |
|---|---|---|---|---|
| $\mathbb{Z}[i]$ | $1$ | $\pm 1, \pm i$, the elements of norm $1$ | none | *Examples of Rings and Fields* |
| $\mathbb{Z}[\sqrt{2}]$ | $1$ | $\pm(1+\sqrt{2})^m$, $m \in \mathbb{Z}$ | none | *Examples of Rings and Fields* |
| $\mathbb{Z}[\sqrt{-2}]$ | $1$ | $\pm 1$ | none | *Examples of Rings and Fields* |
| $\mathbb{Z}[\sqrt{-5}]$ | $1$ | $\pm 1$ | none | *Examples of Rings and Fields* |
| $\mathbb{Z}[\zeta_n]$ | $1$ | finite rank, by Dirichlet's unit theorem | none | *Cyclotomic Fields* |
| $\mathcal{O}_K$ | $1$ | finite rank, by Dirichlet's unit theorem | none | *Algebraic Number Theory* |
| $\overline{\mathbb{Z}}$ | $1$ | the roots of unity it contains | none | *Bézout Domains* |

These rings are all integral domains, so none has a zero divisor; they separate on the units. The Z-rank of the unit group of $\mathcal{O}_K$ is finite by Dirichlet's unit theorem, recorded in *Algebraic Number Theory*; for $\mathbb{Z}[\sqrt{-5}]$ and $\mathbb{Z}[\sqrt{-2}]$ the only units are $\pm 1$, while $\mathbb{Z}[i]$ has four and $\mathbb{Z}[\sqrt{2}]$ has infinitely many. The failure of unique factorisation in $\mathbb{Z}[\sqrt{-5}]$ is not visible in the units or the zero divisors; it is recorded in *Unique Factorisation Domains*.

## Polynomial, Power Series and Localisation Rings

| Ring | Dimension | Units | Zero divisors | Introduced in |
|---|---|---|---|---|
| $R[x]$ | $\dim R + 1$ | the units of $R$ | none when $R$ is a domain | *Polynomial Rings and Rational Functions* |
| $R[x_1, \dots, x_n]$ | $\dim R + n$ | the units of $R$ | none when $R$ is a domain | *Polynomial Rings and Rational Functions* |
| $k[x]$ | $1$ | $k^{\times}$ | none | *Polynomial Rings and Rational Functions* |
| $k[x_1, \dots, x_n]$ | $n$ | $k^{\times}$ | none | *Polynomial Rings and Rational Functions* |
| $R[[x]]$ | $1$ when $R$ is a field | the series with unit constant term | none when $R$ is a domain | *Formal Power Series and Completion* |
| $k[[x]]$ | $1$ | the series with nonzero constant term | none | *Examples of Rings and Fields* |
| $k(x)$ | $0$ | all nonzero | none | *Fields*, §19 |
| $k((t))$ | $0$ | all nonzero | none | *Absolute Values, Valuations and Completions* |
| $\mathbb{Z}_{(p)}$ | $1$ | the fractions with numerator prime to $p$ | none | *Localization and the Fraction Field* |
| $\mathbb{Z}[x]$ | $2$ | $\pm 1$ | none | *Polynomial Rings and Rational Functions* |
| $\mathbb{Z}_p$ | $1$ | the elements with $\lvert x \rvert_p = 1$ | none | *Absolute Values, Valuations and Completions* |

The ring $\mathbb{Z}[x]$, with dimension $2$ and units $\pm 1$, is the standard unique factorisation domain that is not a principal ideal domain; the failure is recorded in *Principal Ideal Domains*.

## The Two-Dimensional Real Algebras

| Ring | Dimension | Units | Zero divisors | Introduced in |
|---|---|---|---|---|
| $\mathbb{D}$ | $2$ over $\mathbb{R}$; Krull $0$ | $N(u) \neq 0$ | the null cone $\{N = 0\}$ | *Split-Complex Algebra* |
| $\mathbb{D}'$ | $2$ over $\mathbb{R}$; Krull $0$ | $x \neq 0$ | the maximal ideal $\mathfrak{m} = (\varepsilon)$ | *Dual-Numbers Algebra* |

The two algebras are not isomorphic. The split-complex numbers are a product of two copies of $\mathbb{R}$ and are reduced; the dual numbers are local and not reduced. Their zero divisors are correspondingly different: the null cone of $\mathbb{D}$ consists of the elements with $N(u) = 0$, while the zero divisors of $\mathbb{D}'$ are exactly the elements of the maximal ideal, and $\varepsilon$ is nilpotent rather than idempotent.

## Product Rings

| Ring | Dimension | Units | Zero divisors | Introduced in |
|---|---|---|---|---|
| $\mathbb{F}_2^n$ | $0$ | the single element $(1, \dots, 1)$ | yes for $n \geq 2$ | *Examples of Rings and Fields* |
| $R \times S$ | $\max(\dim R, \dim S)$ | the pairs $(u, v)$ with $u, v$ units | $(1,0)(0,1) = 0$; every complementary pair of idempotents gives one | *Examples of Rings and Fields* |
| $\mathbb{Z} \times \mathbb{Z}$ | $1$ | the pairs $(\pm1, \pm1)$ | $(1,0)(0,1) = 0$ | *Examples of Rings and Fields* |
| $\mathbb{C} \times \mathbb{C}$ | $0$ | the pairs of nonzero elements | $(1,0)(0,1) = 0$ | *Examples of Rings and Fields* |
| $\mathbb{F}_p \times \mathbb{F}_p$ | $0$ | the pairs of nonzero elements | $(1,0)(0,1) = 0$ | *Examples of Rings and Fields* |

A product of two nonzero rings is never an integral domain, never local and never reduced as soon as one of the factors is not reduced. The idempotents of a product and the direct sum decompositions they generate are listed in *List of Rings by Their Idempotents*.

## Warnings: Commutative Expectation, Absent

| Object | Why it is not a commutative ring | Introduced in |
|---|---|---|
| $\mathbb{H}$ | a division ring, but not commutative | *Quaternion Algebra* |
| $\mathbb{B}$ | the biquaternions, not commutative and with zero divisors | *Biquaternion Algebra* |
| $\mathbb{H}_{\mathbb{D}}$ | the split-biquaternions, not commutative and with zero divisors | *Split-Biquaternion Algebra* |
| $M_n(R)$, $n \geq 2$ | the matrix ring, not commutative | *Matrix Algebras* |
| $M_n(D)$ over a division ring $D$ | not commutative in general | *Matrix Algebras* |
| $R\langle x_1, \dots, x_n\rangle$ | the free algebra, not commutative for $n \geq 2$ | *Tensor Powers and the Free Algebra* |
| $A_1(k)$ | the Weyl algebra, not commutative | *Quotients of the Tensor Algebra* |
| $\mathbb{O}$ | the octonions, not a ring | *Octonion Algebra* |

## Summary

This article has listed the commutative rings of the corpus with their dimension, their units and their zero divisors. The number systems and the residue rings begin the list; the quadratic and cyclotomic integer rings follow, all of them domains and distinguished by their units; the polynomial, power series and localisation rings carry the dimension $\dim R + n$ and the units of the base; the split-complex and dual numbers are the two two-dimensional real algebras, reduced and non-reduced respectively; and the product rings close it with their idempotent zero divisors. Beside the examples stand the non-examples $\mathbb{Z}/6\mathbb{Z}$, $\mathbb{Z}/4\mathbb{Z}$ and the two-dimensional algebra $\mathbb{D}'$.

## Summary of Notation

A catalogue denotes its objects by name rather than by symbol. The symbols that appear in the tables are the following.

| Symbol | Meaning |
|---|---|
| $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$ | The number systems |
| $\mathbb{Z}/n\mathbb{Z}$, $\mathbb{F}_p$, $\mathbb{F}_q$ | Residue ring, prime field, finite field |
| $\mathbb{D}$, $\mathbb{D}'$ | Split-complex numbers and dual numbers |
| $\mathbb{Z}[i]$, $\mathbb{Z}[\sqrt{2}]$, $\mathbb{Z}[\sqrt{-2}]$, $\mathbb{Z}[\sqrt{-5}]$ | Quadratic integer rings |
| $\mathbb{Z}[\zeta_n]$, $\mathcal{O}_K$, $\overline{\mathbb{Z}}$ | Cyclotomic integers, ring of integers, all algebraic integers |
| $R[x]$, $R[x_1,\dots,x_n]$, $R[[x]]$, $k[[x]]$ | Polynomial and power series rings |
| $k(x)$, $k((t))$ | Rational function field, Laurent series field |
| $\mathbb{Z}_{(p)}$, $\mathbb{Z}_p$ | Localisation at $p$, $p$-adic integers |
| $R \times S$ | Product ring |
| $\varphi(n)$ | Euler totient, the order of $(\mathbb{Z}/n\mathbb{Z})^{\times}$ |
| $\mathbb{H}$, $\mathbb{B}$, $\mathbb{H}_{\mathbb{D}}$, $\mathbb{O}$ | Quaternions, biquaternions, split-biquaternions, octonions; not commutative |
| $M_n(R)$, $R\langle x_1,\dots,x_n\rangle$, $A_1(k)$ | Matrix ring, free algebra, Weyl algebra; not commutative |

## Further Reading

- Irving Kaplansky, *Commutative Rings* (University of Chicago Press, revised ed. 1974), for the commutative rings of the list and their units and zero divisors.
- Paulo Ribenboim, *Classical Theory of Algebraic Numbers* (Springer, 2001), for the quadratic and cyclotomic integer rings and the structure of their units.
- Tsit-Yuen Lam, *Exercises in Classical Ring Theory* (Springer, 2nd ed. 2003), for the counterexamples $\mathbb{Z}/6\mathbb{Z}$, $\mathbb{Z}/4\mathbb{Z}$ and the two-dimensional algebras.
