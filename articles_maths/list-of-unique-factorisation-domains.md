
# __List of Unique Factorisation Domains__

## Introduction

This article lists the unique factorisation domains of the corpus, with the irreducibles of each example, and it records the failure of unique factorisation for each non-example with the two factorisations that witness it. Every entry points to the article that introduces the object.

A unique factorisation domain is an integral domain in which every nonzero nonunit is a product of irreducibles and the factorisation is unique up to order and associates; equivalently, by the criterion of *Unique Factorisation Domains*, every irreducible element is prime. The list gathers the Euclidean domains and their rings of integers, the polynomial rings over a field or a unique factorisation domain, and the power series rings, and it records $\mathbb{Z}[\sqrt{-5}]$ and the imaginary quadratic rings of class number greater than one on the other side.

The article introduces nothing and proves nothing. It records examples and non-examples side by side.

## The Criterion and the Transfer

The equivalence of unique factorisation with "every irreducible is prime" is the working criterion of *Unique Factorisation Domains*, and Euclid's lemma is its first consequence. The transfer to a polynomial ring is Gauss's lemma: if $R$ is a unique factorisation domain then $R[x]$ is one, with the content $c(f)$ and the primitive polynomials carrying the arithmetic. Eisenstein's criterion is the standard test for an irreducible polynomial. All of this is the subject of *Unique Factorisation Domains*; a catalogue records only which rings the corpus meets.

| Statement | Content | Introduced in |
|---|---|---|
| a domain is a UFD iff every irreducible is prime | irreducibles and primes | *Unique Factorisation Domains* |
| $R$ a UFD implies $R[x]$ a UFD | content and Gauss's lemma | *Unique Factorisation Domains* |
| Eisenstein's criterion | irreducibility of a polynomial over a UFD | *Unique Factorisation Domains* |

## The Unique Factorisation Domains and Their Irreducibles

| Unique factorisation domain | The irreducibles, up to associates | Introduced in |
|---|---|---|
| $\mathbb{Z}$ | the rational primes $\pm p$ | *The Integers* |
| $\mathbb{Z}[i]$ | $1+i$, the rational primes $p \equiv 3 \bmod 4$, and the elements $\pi$ with $N(\pi) = p$ for $p \equiv 1 \bmod 4$ | *Examples of Rings and Fields* |
| $\mathbb{Z}[\sqrt{-2}]$ | $\sqrt{-2}$, and the elements of norm $p$ for a rational prime $p$ with $-2$ a square modulo $p$ | *Examples of Rings and Fields* |
| $\mathbb{Z}[\sqrt{2}]$ | $\sqrt{2}$, and the elements of norm $\pm p$ | *Examples of Rings and Fields* |
| $\mathbb{Z}[\tfrac{1+\sqrt{-3}}{2}]$, the Eisenstein integers | $\sqrt{-3}$, and the elements of norm $p \equiv 1 \bmod 3$ | *Examples of Rings and Fields* |
| $k[x]$ | the monic irreducible polynomials; the linear ones when $k$ is algebraically closed | *Polynomial Rings and Rational Functions* |
| $\mathbb{F}_q[x]$ | the monic irreducible polynomials over the finite field | *Finite Fields* |
| $\mathbb{Z}[x]$ | the rational primes $p$, and the primitive irreducible polynomials | *Polynomial Rings and Rational Functions* |
| $k[x_1, \dots, x_n]$ | the irreducible polynomials in $n$ variables | *Polynomial Rings and Rational Functions* |
| $k[x_1, x_2, \ldots]$ in infinitely many variables | the irreducible polynomials in finitely many variables | *Examples of Rings and Fields* |
| $k[[x]]$ | $x$ alone, up to units | *Examples of Rings and Fields* |
| every field, for instance $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$, $\mathbb{F}_p$, $\mathbb{Q}_p$ | none: every nonzero element is a unit | *Fields* |
| $\mathcal{O}_{K,\mathfrak{p}}$, a discrete valuation ring | the uniformiser, a generator of the maximal ideal | *Dedekind Domains and Ideal Class Groups* |
| $\mathbb{Q}[x]$, $\mathbb{R}[x]$, $\mathbb{C}[x]$ | the monic irreducibles; the linear ones over $\mathbb{C}$ | *Polynomial Rings and Rational Functions* |

The Gaussian integers give the standard worked example: $2 = -i(1+i)^2$ ramifies, an odd prime $p \equiv 3 \bmod 4$ remains irreducible, and a prime $p \equiv 1 \bmod 4$ splits as $\pi\bar\pi$ with $N(\pi) = p$, the case $5 = (2+i)(2-i)$. In the power series ring the only irreducible is $x$, and the localisation $\mathbb{Z}_{(p)}$ has the single irreducible $p$; a discrete valuation ring has one irreducible up to associates, and this is recorded in *List of Local Rings and Valuations*.

## Unique Factorisation in the Local and Power Series Rings

The discrete valuation rings are the unique factorisation domains with the smallest possible supply of irreducibles: one, up to associates, because the nonzero ideals form a single chain.

| Unique factorisation domain | The single irreducible | The maximal ideal it generates | Introduced in |
|---|---|---|---|
| $\mathbb{Z}_{(p)}$ | $p$ | $p\mathbb{Z}_{(p)}$ | *Localization and the Fraction Field* |
| $\mathbb{Z}_p$ | $p$ | $p\mathbb{Z}_p$ | *Absolute Values, Valuations and Completions* |
| $k[t]_{(t)}$ | $t$ | $tk[t]_{(t)}$ | *Absolute Values, Valuations and Completions* |
| $\mathbb{F}_p[x]_{(x)}$ | $x$ | $x\mathbb{F}_p[x]_{(x)}$ | *Examples of Rings and Fields* |
| $k[[x]]$ | $x$ | $(x)$ | *Examples of Rings and Fields* |
| $\mathcal{O}_{K,\mathfrak{p}}$ | a generator of $\mathfrak{p}$ | $\mathfrak{p}$ | *Dedekind Domains and Ideal Class Groups* |

Each of these rings is a principal ideal domain and hence a unique factorisation domain, and in each the factorisation of an element is the statement that its value is a nonnegative integer. The power series ring is not a field, and its single irreducible is a nonunit that is not a zero divisor.

## Domains That Are Not Unique Factorisation Domains

| Domain | The failure | Class number | Introduced in |
|---|---|---|---|
| $\mathbb{Z}[\sqrt{-5}]$ | $6 = 2 \cdot 3 = (1+\sqrt{-5})(1-\sqrt{-5})$, four pairwise nonassociate irreducibles | $2$ | *Examples of Rings and Fields* |
| $\mathbb{Z}[\sqrt{-6}]$ | the class group is nontrivial, so some element has two factorisations | $2$ | *Dedekind Domains and Ideal Class Groups* |
| $\mathbb{Z}[\sqrt{-10}]$ | the class group is nontrivial | $2$ | *Dedekind Domains and Ideal Class Groups* |
| $\mathbb{Z}[\sqrt{-14}]$ | the class group is cyclic of order $4$ | $4$ | *Dedekind Domains and Ideal Class Groups* |
| $\mathcal{O}_K$ with nontrivial class group | unique factorisation of elements fails; ideals still factor uniquely | varies | *Dedekind Domains and Ideal Class Groups* |
| $\overline{\mathbb{Z}}$ | Bézout and not Noetherian, hence not a UFD | — | *Bézout Domains* |

For $\mathbb{Z}[\sqrt{-5}]$ the element $2$ is irreducible but not prime, since $\mathbb{Z}[\sqrt{-5}]/(2)$ is not a domain; the ideal class group has order $2$, generated by the class of the non-principal prime $P = (2, 1+\sqrt{-5})$, and the failure of unique factorisation of elements is repaired by the unique factorisation of ideals. The four factors $2$, $3$, $1+\sqrt{-5}$ and $1-\sqrt{-5}$ all have norm $4$, $9$, $6$, $6$, and no element of norm $2$ or $3$ exists in the ring, which is why they are irreducible; the units are $\pm 1$, which is why they are pairwise nonassociate. This computation is recorded in *Dedekind Domains and Ideal Class Groups* and in *Examples of Rings and Fields*, and it is the failure that *Unique Factorisation Domains* treats in detail.

## Unique Factorisation That Survives Without Principal Ideals

A unique factorisation domain need not be a principal ideal domain, and the standard witnesses are polynomial rings.

| Ring | Why it is a UFD | Why it is not principal | Introduced in |
|---|---|---|---|
| $\mathbb{Z}[x]$ | Gauss's lemma applied to $\mathbb{Z}$ | the ideal $(2, x)$ is not principal | *Polynomial Rings and Rational Functions* |
| $k[x_1, \dots, x_n]$, $n \geq 2$ | the iterated Gauss's lemma | the ideal $(x_1, x_2)$ is not principal | *Polynomial Rings and Rational Functions* |
| $k[x_1, x_2, \ldots]$ | the iterated Gauss's lemma on finitely many variables | not Noetherian | *Examples of Rings and Fields* |
| $R[x]$ for $R$ a UFD | Gauss's lemma | not principal in general | *Polynomial Rings and Rational Functions* |
| $\mathbb{F}_q[x, y]$ | the iterated Gauss's lemma over $\mathbb{F}_q$ | the ideal $(x, y)$ is not principal | *Polynomial Rings and Rational Functions* |
| $\mathbb{Z}[x_1, \dots, x_n]$ | Gauss's lemma applied to $\mathbb{Z}$, iterated | the ideal $(2, x_1)$ is not principal | *Polynomial Rings and Rational Functions* |

The first two are the reason the ladder of *List of Structures from Rings to Fields* has a strict step between a unique factorisation domain and a principal ideal domain, and the third is the reason a unique factorisation domain need not be Noetherian.

## Warnings

| Object | Why it is not a unique factorisation domain of this list | Introduced in |
|---|---|---|
| $M_2(\mathbb{R})$, $\mathbb{H}$, $\mathbb{B}$, $\mathbb{H}_{\mathbb{D}}$ | not commutative, and the matrix, biquaternion and split-biquaternion rings have zero divisors | *Matrix Algebras*, *Quaternion Algebra*, *Biquaternion Algebra*, *Split-Biquaternion Algebra* |
| $\mathbb{D}$, $\mathbb{D}'$ | not domains: the split-complex numbers have $e_+e_- = 0$ and the dual numbers a nilpotent | *Split-Complex Algebra*, *Dual-Numbers Algebra* |
| $\mathbb{Z}/6\mathbb{Z}$ | not a domain: $2 \cdot 3 = 0$ | *Modular Arithmetic and the Ring of Residues* |
| $\mathbb{O}$ | not a ring | *Octonion Algebra* |
| a general Dedekind domain $\mathcal{O}_K$ | a UFD exactly when its class number is $1$ | *Dedekind Domains and Ideal Class Groups* |

## Summary

This article has listed the unique factorisation domains of the corpus with the irreducibles of each: the rational primes in $\mathbb{Z}$, the Gaussian, quadratic and Eisenstein primes in the rings of integers of class number one, the monic irreducible polynomials in $k[x]$ and $\mathbb{F}_q[x]$, the primitive irreducibles and the rational primes in $\mathbb{Z}[x]$, the irreducible polynomials in several and in infinitely many variables, the single irreducible $x$ in $k[[x]]$, and no irreducible at all in a field. It has recorded the failures: the two factorisations of $6$ in $\mathbb{Z}[\sqrt{-5}]$, the nontrivial class groups of $\mathbb{Z}[\sqrt{-6}]$, $\mathbb{Z}[\sqrt{-10}]$, $\mathbb{Z}[\sqrt{-14}]$ and a general $\mathcal{O}_K$, and the non-Noetherian Bézout domain $\overline{\mathbb{Z}}$.

## Summary of Notation

A catalogue denotes its objects by name rather than by symbol. The symbols that appear in the tables are the following.

| Symbol | Meaning |
|---|---|
| $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$, $\mathbb{F}_q$ | The number systems and the finite fields |
| $\mathbb{Z}[i]$, $\mathbb{Z}[\sqrt{-2}]$, $\mathbb{Z}[\sqrt{2}]$, $\mathbb{Z}[\sqrt{-5}]$ | Quadratic integer rings |
| $\mathbb{Z}[\tfrac{1+\sqrt{-3}}{2}]$ | The Eisenstein integers |
| $\mathbb{Z}[\sqrt{-6}]$, $\mathbb{Z}[\sqrt{-10}]$, $\mathbb{Z}[\sqrt{-14}]$ | Imaginary quadratic rings of class number $> 1$ |
| $\overline{\mathbb{Z}}$, $\mathcal{O}_K$ | All algebraic integers, ring of integers of $K$ |
| $N(\cdot)$, $c(f)$ | Norm, content of a polynomial |
| $k[x]$, $k[x_1,\dots,x_n]$, $\mathbb{Z}[x]$, $k[[x]]$ | Polynomial and power series rings |
| $\mathbb{Q}_p$, $\mathbb{Z}_{(p)}$ | $p$-adic numbers, localisation at $p$ |
| $\mathbb{H}$, $\mathbb{B}$, $\mathbb{H}_{\mathbb{D}}$, $M_2(\mathbb{R})$ | Non-commutative rings, named in the warnings |

## Further Reading

- Paulo Ribenboim, *Classical Theory of Algebraic Numbers* (Springer, 2001), for the quadratic rings, their class numbers and the explicit factorisations.
- Oscar Zariski and Pierre Samuel, *Commutative Algebra*, Volume I (Van Nostrand, 1958), for unique factorisation, Gauss's lemma and content.
- Irving Kaplansky, *Commutative Rings* (University of Chicago Press, revised ed. 1974), for unique factorisation domains and their failure in Dedekind domains.
