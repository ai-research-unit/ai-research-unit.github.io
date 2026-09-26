
# __List of Zero Divisors and Prime Ideals__

## Introduction

This article lists the rings of the corpus together with their zero divisors, the annihilator $\operatorname{Ann}(a)$ of an element, and the associated primes in which those zero divisors lie. Every entry points to the article that introduces the object, and the theorem $Z(R) = \bigcup_{\mathfrak{p} \in \operatorname{Ass}(R)} \mathfrak{p}$ is the statement the list is built to illustrate.

The zero divisors of a Noetherian ring are a finite union of prime ideals, so they carry an ideal-theoretic description even though they are not themselves an ideal; the annihilator of an element is an ideal, and the associated primes are exactly the maximal elements among the ideals of the form $\operatorname{Ann}(a)$. The list records each ring with its zero divisor set, its associated primes, and the idempotents that generate direct summands.

The article introduces nothing and proves nothing. It records examples and non-examples side by side.

## The Annihilator of an Element

| Ring | The element | $\operatorname{Ann}(a)$ | Introduced in |
|---|---|---|---|
| $\mathbb{Z}$ | $n \neq 0$ | $(0)$ | *The Integers* |
| $\mathbb{Z}/4\mathbb{Z}$ | $2$ | $(2)$ | *Reduced Rings and the Nilradical* |
| $\mathbb{Z}/6\mathbb{Z}$ | $2$ | $(3)$ | *Modular Arithmetic and the Ring of Residues* |
| $\mathbb{Z}/6\mathbb{Z}$ | $3$ | $(2)$ | *Modular Arithmetic and the Ring of Residues* |
| $\mathbb{Z}/6\mathbb{Z}$ | $4$ | $(3)$ | *Modular Arithmetic and the Ring of Residues* |
| $k[x,y]/(x^2,y)$ | the class of $x$ | $(x,y)$ | *Primary Decomposition* |
| $R \times S$ | $(1, 0)$ | $(0) \times S$ | *Examples of Rings and Fields* |
| a domain $R$ | $a \neq 0$ | $(0)$ | *Integral Domains* |
| $\mathbb{Z}[\sqrt{-5}]$ | $2$ | $(0)$ | *Examples of Rings and Fields* |

The annihilator $\operatorname{Ann}(a) = \{r : ra = 0\}$ is an ideal, and it consists of zero divisors together with $0$: every nonzero element of $\operatorname{Ann}(a)$ kills the nonzero element $a$. The colon form $(I : x) = \{r : rx \in I\}$ of the same construction, used for the zero divisors of a quotient $R/I$, is the notation of *Primary Decomposition*, and $\operatorname{Ann}(a) = ((0) : a)$ is the special case $I = (0)$.

## The Associated Primes and the Theorem

| Ring | The zero divisor set $Z(R)$ | The associated primes $\operatorname{Ass}(R)$ | Introduced in |
|---|---|---|---|
| a domain $R$ | $\{0\}$ | the single prime $(0)$ | *Integral Domains* |
| $\mathbb{Z}/4\mathbb{Z}$ | $(2)$ | $(2)$ | *Reduced Rings and the Nilradical* |
| $\mathbb{Z}/6\mathbb{Z}$ | $(2) \cup (3)$ | $(2)$ and $(3)$ | *Modular Arithmetic and the Ring of Residues* |
| $\mathbb{Z}/12\mathbb{Z}$ | $(2) \cup (3)$ | $(2)$ and $(3)$ | *Modular Arithmetic and the Ring of Residues* |
| $k[x,y]/(x^2,xy)$ | $(x,y)$ | $(x)$ and $(x,y)$ | *Primary Decomposition* |
| an Artinian local ring with maximal ideal $\mathfrak{m}$ | $\mathfrak{m}$, the maximal ideal | $\mathfrak{m}$ | *Noetherian and Artinian Rings* |
| a Dedekind domain | $\{0\}$ | the single prime $(0)$, although every nonunit lies in some maximal ideal | *Dedekind Domains and Ideal Class Groups* |
| a product $R \times S$ | $(Z(R) \times S) \cup (R \times Z(S))$ | $\operatorname{Ass}(R) \cup \operatorname{Ass}(S)$ | *Examples of Rings and Fields* |
| a Boolean ring | every element except $0$ and $1$ | the maximal ideals | *Von Neumann Regular Rings* |

The theorem is that the two middle columns agree: for a Noetherian ring, the zero divisors are the union of the associated primes, $\bigcup_{x \neq 0} \operatorname{Ann}(x) = \bigcup_{\mathfrak{p} \in \operatorname{Ass}(R)} \mathfrak{p}$, and this is stated and proved in *Primary Decomposition*. The theorem gives the zero divisors a finite description even when they are not an ideal, and it is the reason the row for an Artinian local ring is a single prime: its maximal ideal is nilpotent, hence consists of zero divisors, and it is the one associated prime.

## Why the Zero Divisors Are Not an Ideal

| Ring | The zero divisors | Their sum | The failure | Introduced in |
|---|---|---|---|---|
| $\mathbb{Z}/6\mathbb{Z}$ | $2, 3, 4$ | $2 + 3 = 5$, a unit | $Z(R)$ is not closed under addition | *Modular Arithmetic and the Ring of Residues* |
| $\mathbb{Z}$ | $0$ alone | $0 + 0 = 0$ | $Z(R) = (0)$ happens to be an ideal | *The Integers* |
| $\mathbb{Z}/4\mathbb{Z}$ | $0, 2$ | $2 + 2 = 0$ | $Z(R) = (2)$, an ideal by accident of the nilpotent | *Reduced Rings and the Nilradical* |
| $k[x,y]/(x^2,xy)$ | $\mathfrak{m} = (x,y)$, the union of $(x)$ and $(x,y)$ | $x + y$, again a zero divisor | $Z(R)$ is the maximal ideal, so the failure is absent | *Primary Decomposition* |
| $\mathbb{R} \times \mathbb{R}$ | $(a,0)$ and $(0,b)$ | $(1,0) + (0,1) = (1,1)$, a unit | $Z(R)$ is not closed under addition | *Examples of Rings and Fields* |
| $M_2(\mathbb{R})$ | the singular matrices | $E_{11} + (I - E_{11})$ is a unit | $Z(R)$ is not an ideal | *Matrix Algebras* |

The zero divisors form a union of primes and not an ideal, and the table records the two ways the failure shows: in $\mathbb{Z}/6\mathbb{Z}$ and in $\mathbb{R}\times\mathbb{R}$ the sum of two zero divisors is a unit, while in $k[x,y]/(x^2,xy)$ the sum stays a zero divisor because the whole set is the maximal ideal $(x,y)$, the union of the prime $(x)$ with the embedded prime $(x,y)$. The one case where the set is an ideal is the case where it is a single prime, the nilpotent maximal ideal of a local ring such as $\mathbb{Z}/4\mathbb{Z}$ or the dual numbers, and this is recorded in *List of Reduced, Local and Product Rings*.

## The Idempotent-Generated Ideals and the Direct Summands

| Ring | The idempotent $e$ | The ideal $Re$ | The complementary summand | Introduced in |
|---|---|---|---|---|
| $\mathbb{Z}/6\mathbb{Z}$ | $3$ | $(3) = \{0, 3\}$ | $(2) = \{0, 2, 4\}$ | *Modular Arithmetic and the Ring of Residues* |
| $\mathbb{Z}/6\mathbb{Z}$ | $4$ | $(2) = \{0, 2, 4\}$ | $(3) = \{0, 3\}$ | *Modular Arithmetic and the Ring of Residues* |
| $\mathbb{D} = \mathbb{R}[j]/(j^2-1)$ | $e_+ = \tfrac{1}{2}(1+j)$ | $\mathbb{R}e_+$ | $\mathbb{R}e_-$ | *Split-Complex Algebra* |
| $\mathbb{H}_{\mathbb{D}}$ | $e_+$, $e_-$ | $\mathbb{H}e_+$, $\mathbb{H}e_-$ | the other ideal | *Split-Biquaternion Algebra* |
| $R \times S$ | $(1, 0)$ | $R \times 0$ | $0 \times S$ | *Examples of Rings and Fields* |
| a Boolean ring | every element other than $0$ and $1$ | the principal ideal it generates | the ideal generated by $1 - e$ | *Von Neumann Regular Rings* |
| $M_2(\mathbb{R})$ | $E_{11}$, $E_{22}$ | the $(1,1)$ entries | the $(2,2)$ entries | *Matrix Algebras* |

An idempotent $e$ satisfies $e(1-e) = 0$ and induces the direct sum decomposition $R = Re \oplus R(1-e)$, so the principal ideal $Re$ is a direct summand and is generated by an idempotent. The rings in which every ideal is idempotent-generated are the von Neumann regular rings, in which every principal ideal is generated by an idempotent; the commutative von Neumann regular rings are exactly the reduced rings of Krull dimension zero, and the Boolean rings are the characteristic-two examples. The domains and the local rings are the opposite case, in which the idempotents are $0$ and $1$ alone: this is recorded in *Von Neumann Regular Rings* and in *List of Rings by Their Idempotents*.

## The Classes of Ring by Their Zero Divisors

| Class | The zero divisor set | Introduced in |
|---|---|---|
| a domain | $\{0\}$ | *Integral Domains* |
| a reduced ring | a union of primes, possibly $\{0\}$ | *Reduced Rings and the Nilradical* |
| an Artinian local ring | the maximal ideal | *Noetherian and Artinian Rings* |
| a principal ideal domain | $\{0\}$ | *Principal Ideal Domains* |
| a Dedekind domain | $\{0\}$; the nonunits are the union of the maximal ideals, the zero divisors are not | *Dedekind Domains and Ideal Class Groups* |
| a Noetherian ring | a finite union of primes | *Primary Decomposition* |
| a general commutative ring | a union of primes, not necessarily finite | *Commutative Rings* |
| a von Neumann regular ring | the union of the maximal ideals | *Von Neumann Regular Rings* |

The eighth row is the row that ties this list to the idempotents: in a von Neumann regular ring every element is a unit times an idempotent, the maximal ideals are the associated primes, and the zero divisors are their union, so the ring realises the theorem in its sharpest form. The non-Noetherian case loses only the finiteness of the union.

## Warnings

| Object | Why it has no zero divisors and no prime to record | Introduced in |
|---|---|---|
| a field $k$ | every nonzero element is a unit; the only prime is $(0)$ | *Fields* |
| $\mathbb{Z}/p\mathbb{Z}$ | a field; its associated prime is $(0)$ | *Modular Arithmetic and the Ring of Residues* |
| $\mathbb{H}$ | a division ring; every nonzero element is a unit | *Quaternion Algebra* |
| $\mathbb{Z}$, $k[x]$, $\mathbb{Z}[i]$ | domains, so $Z(R) = \{0\}$ | *Integral Domains* |
| the free algebra $R\langle x_1, \dots, x_n\rangle$ | a non-commutative domain; the annihilator is one-sided | *Tensor Powers and the Free Algebra* |
| $M_2(\mathbb{R})$ | non-commutative: an element may have a left annihilator and no right annihilator | *Matrix Algebras* |

The last two rows are the reason the theorem is stated for a commutative ring: in a non-commutative ring the annihilator of an element is a one-sided ideal, the associated primes are replaced by the prime ideals in the non-commutative sense, and the union statement is not available in the same form. The non-commutative substitute is developed in *Prime Rings* and *Semiprime Rings*.

## Summary

This article has listed the rings of the corpus with their zero divisors, their annihilators and their associated primes. The annihilator $\operatorname{Ann}(a)$ is computed for the residue rings, the quotient $k[x,y]/(x^2,y)$, the products and the domains; the associated primes are tabulated for the same objects, and the theorem $Z(R) = \bigcup \operatorname{Ass}(R)$ of *Primary Decomposition* is the statement they illustrate, holding for a finite union in the Noetherian case and for a possibly infinite one in general; the failure of the zero divisors to be an ideal is recorded at $\mathbb{Z}/6\mathbb{Z}$ and at $\mathbb{R}\times\mathbb{R}$, where the sum of two zero divisors is a unit; and the idempotent-generated ideals $Re$ are recorded as the direct summands $R = Re \oplus R(1-e)$, with the von Neumann regular rings as the case in which every ideal is generated by an idempotent and the domains and local rings as the case in which no nontrivial idempotent exists.

## Summary of Notation

A catalogue denotes its objects by name rather than by symbol. The symbols that appear in the tables are the following.

| Symbol | Meaning |
|---|---|
| $Z(R)$ | The set of zero divisors of $R$ |
| $\operatorname{Ann}(a) = ((0) : a)$ | The annihilator of $a$, $\{r : ra = 0\}$ |
| $(I : x)$ | The colon ideal $\{r : rx \in I\}$ |
| $\operatorname{Ass}(R)$ | The associated primes of $R$, that is $\operatorname{Ass}((0))$ |
| $\operatorname{Ass}(I)$ | The associated primes of the ideal $I$ |
| $\mathfrak{p}, \mathfrak{m}$ | Prime ideal, maximal ideal |
| $e$, $e_{\pm}$ | Idempotents; $e_+ = \tfrac{1}{2}(1+j)$, $e_- = \tfrac{1}{2}(1-j)$ |
| $k[x,y]/(x^2,xy)$ | The quotient with associated primes $(x)$ and $(x,y)$ |

## Further Reading

- Irving Kaplansky, *Commutative Rings* (University of Chicago Press, revised ed. 1974), for the associated primes and the union-of-primes description of the zero divisors.
- M. F. Atiyah and I. G. Macdonald, *Introduction to Commutative Algebra* (Addison–Wesley, 1969), for primary decomposition, the first uniqueness theorem and the Nullstellensatz.
- Tsit-Yuen Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for the non-commutative prime and semiprime rings that replace the prime ideals of the commutative theory.
