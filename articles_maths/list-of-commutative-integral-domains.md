
# __List of Commutative Integral Domains__

## Introduction

This article lists the integral domains of the corpus and the ladder that descends from them toward the fields: GCD domain, Bézout domain, unique factorisation domain, principal ideal domain, Euclidean domain, field. Every entry points to the article that introduces the object.

The defining property is the absence of zero divisors, equivalently cancellation for nonzero elements. The ladder records the divisibility properties that a domain may or may not have: $\mathbb{Z}[\sqrt{-5}]$ is a domain that is not a unique factorisation domain, $\mathbb{Z}[x]$ is a unique factorisation domain that is not a principal ideal domain, and $\mathbb{Z}$ is a Euclidean domain that is not a field.

The article introduces nothing and proves nothing. It records examples and non-examples side by side.

## What a Domain Adds

An integral domain is a commutative ring with $1 \neq 0$ and no zero divisors: $ab = 0$ forces $a = 0$ or $b = 0$. Equivalently, every nonzero element is cancellable. The definition and its consequences are in *Rings*, §12, and the first examples are $\mathbb{Z}$ and every field; a field is a domain because a nonzero element is a unit, so it can never be a zero divisor.

| Object | Why it is a domain | Introduced in |
|---|---|---|
| $\mathbb{Z}$ | the cancellation law of the integers | *The Integers* |
| every field, for instance $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$, $\mathbb{F}_p$, $\mathbb{Q}_p$ | a nonzero element is a unit, hence not a zero divisor | *Fields* |
| $\mathbb{Z}[x]$, $k[x_1, \dots, x_n]$ | a product of nonzero polynomials is nonzero over a domain | *Polynomial Rings and Rational Functions* |
| $k[[x]]$ | a product of series with nonzero leading term has nonzero leading term | *Examples of Rings and Fields* |
| any subring of a domain | inherited from the larger ring | *Rings*, §3 |
| $\operatorname{Frac}(R)$ of a domain $R$ | a field, and every domain embeds in it | *Localization and the Fraction Field* |

Every domain has a field of fractions, and the passage to it is recorded in *Localization and the Fraction Field*. The domains of this article are the commutative ones; the non-commutative domains, in which cancellation holds on both sides but the ring need not be commutative, are the subject of *List of Domains*.

## The Ladder Down from a Domain

The ladder strengthens the divisibility theory step by step. Each row names the property added and the objects that reach it.

| Rung | The property added | Objects at this rung | Introduced in |
|---|---|---|---|
| integral domain | no zero divisors | $\mathbb{Z}[\sqrt{-5}]$, $\mathbb{Z}[x]$, $k[x_1, \dots, x_n]$ | *Integral Domains* |
| GCD domain | every pair has a greatest common divisor | $\mathbb{Z}[x]$ and every unique factorisation domain, $\overline{\mathbb{Z}}$ | *GCD Domains* |
| Bézout domain | every finitely generated ideal is principal | $\overline{\mathbb{Z}}$ | *Bézout Domains* |
| unique factorisation domain | unique factorisation into irreducibles | $\mathbb{Z}$, $\mathbb{Z}[i]$, $k[x_1, \dots, x_n]$, $k[[x]]$ | *Unique Factorisation Domains* |
| principal ideal domain | every ideal is principal | $\mathbb{Z}$, $\mathbb{Z}[i]$, $k[x]$, $\mathbb{Z}_p$ | *Principal Ideal Domains* |
| Euclidean domain | a Euclidean degree with division with remainder | $\mathbb{Z}$, $\mathbb{Z}[i]$, $\mathbb{Z}[\sqrt{2}]$, $k[x]$ | *Euclidean Domains* |
| field | every nonzero element is a unit | $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$, $\mathbb{F}_p$, $\mathbb{Q}_p$, $k(x)$, $k((t))$ | *Fields* |

The step from a domain to a unique factorisation domain branches: the unique factorisation domains and the Bézout domains are incomparable strengthenings of the GCD domains, and their intersection is the principal ideal domains. The witnesses at the strict steps are collected next.

## Where Each Object Stops on the Ladder

| Domain | Strongest rung reached | The failure it records | Introduced in |
|---|---|---|---|
| $\mathbb{Z}$ | Euclidean domain | not a field: $2$ is not a unit | *The Integers* |
| $\mathbb{Z}[i]$ | Euclidean domain | not a field: $2 = (1+i)(1-i)$ | *Examples of Rings and Fields* |
| $\mathbb{Z}[\sqrt{2}]$ | Euclidean domain | not a field | *Examples of Rings and Fields* |
| $\mathbb{Z}[\sqrt{-2}]$ | Euclidean domain | not a field | *Examples of Rings and Fields* |
| $k[x]$ | Euclidean domain | not a field: $x$ is not a unit | *Polynomial Rings and Rational Functions* |
| $\mathbb{Z}[(1+\sqrt{-19})/2]$ | principal ideal domain | not Euclidean | *Euclidean Domains* |
| $\mathbb{Z}_p$ | principal ideal domain | not a field | *Absolute Values, Valuations and Completions* |
| $\mathbb{Z}_{(p)}$ | principal ideal domain | not a field | *Localization and the Fraction Field* |
| $k[t]_{(t)}$, $\mathbb{F}_p[x]_{(x)}$ | principal ideal domain | not a field; a discrete valuation ring | *Absolute Values, Valuations and Completions*, *Examples of Rings and Fields* |
| $k[x_1, \dots, x_n]$, $n \geq 2$ | unique factorisation domain | not principal: $(x_1, x_2)$ | *Polynomial Rings and Rational Functions* |
| $\mathbb{Z}[x]$ | unique factorisation domain | not principal: $(2, x)$ | *Polynomial Rings and Rational Functions* |
| $k[[x]]$ | unique factorisation domain | not a field; the only irreducible is $x$ | *Examples of Rings and Fields* |
| $\overline{\mathbb{Z}}$ | Bézout domain | not Noetherian, hence not a PID, and not a UFD | *Bézout Domains* |
| $\mathbb{Z}[\sqrt{-5}]$ | integral domain | not a unique factorisation domain | *Examples of Rings and Fields* |
| $\mathcal{O}_K$ | integral domain | not a unique factorisation domain in general; Dedekind | *Algebraic Number Theory* |
| $k[x_1, x_2, \ldots]$ in infinitely many variables | integral domain | not Noetherian | *Examples of Rings and Fields* |
| $\mathbb{R}[x]$, $\mathbb{Q}[x]$, $\mathbb{F}_p[x]$ | Euclidean domain | not a field: $x$ is not a unit | *Polynomial Rings and Rational Functions* |
| $\mathbb{Z}[\zeta_n]$ | integral domain | Dedekind, not principal in general | *Cyclotomic Fields* |

## The Failure of Unique Factorisation

The classical failure is $\mathbb{Z}[\sqrt{-5}]$, where $6 = 2 \cdot 3 = (1 + \sqrt{-5})(1 - \sqrt{-5})$ are two factorisations into irreducibles, so the domain is not a unique factorisation domain. The element $2$ is irreducible but not prime: the quotient $\mathbb{Z}[\sqrt{-5}]/(2)$ is not a domain. The failure is measured by the ideal class group, which has order $2$ for this ring, as recorded in *Dedekind Domains and Ideal Class Groups*, and it is recorded for this and further rings in *Unique Factorisation Domains*.

| Ring | The failure | Introduced in |
|---|---|---|
| $\mathbb{Z}[\sqrt{-5}]$ | $6 = 2 \cdot 3 = (1+\sqrt{-5})(1-\sqrt{-5})$ | *Unique Factorisation Domains* |
| $\mathcal{O}_K$ | the class group need not be trivial | *Dedekind Domains and Ideal Class Groups* |
| $\overline{\mathbb{Z}}$ | Bézout, not Noetherian, not a unique factorisation domain | *Bézout Domains* |
| $\mathbb{Z}[x]$ | none: it is a unique factorisation domain, recorded here for its non-principal ideal | *Polynomial Rings and Rational Functions* |

## Quotients of a Domain That Are Not Domains

A quotient of a domain by an ideal is a domain exactly when the ideal is prime, so the quotients are a further source of non-examples.

| Quotient | The zero divisor that appears | Introduced in |
|---|---|---|
| $\mathbb{Z}[\sqrt{-5}]/(2)$ | the class of $1+\sqrt{-5}$ is a nonzero nilpotent, so $(2)$ is not prime | *Dedekind Domains and Ideal Class Groups* |
| $\mathbb{Z}[x]/(x^2 - 1)$ | $(x-1)(x+1) = x^2 - 1 = 0$ | *Polynomial Rings and Rational Functions* |
| $k[x]/(f)$, $f$ reducible | the factors of $f$ give zero divisors | *Polynomial Rings and Rational Functions* |
| $R[x]/(x^2)$ | the image of $x$ is a nonzero nilpotent | *Polynomial Rings and Rational Functions* |

The quotient $\mathbb{Z}[\sqrt{-5}]/(2)$ records that $2$ is irreducible but not prime in $\mathbb{Z}[\sqrt{-5}]$, which is what the failure of unique factorisation consists in: in a unique factorisation domain every irreducible element is prime. The ideal theory records the same failure by the non-principal prime $P = (2, 1+\sqrt{-5})$ of *Dedekind Domains and Ideal Class Groups*.

## Warnings: Objects Expected and Absent

| Object | Why it is not an integral domain | Introduced in |
|---|---|---|
| $\mathbb{Z}/6\mathbb{Z}$ | $2 \cdot 3 = 0$ with neither factor zero | *Modular Arithmetic and the Ring of Residues* |
| $\mathbb{Z}/4\mathbb{Z}$ | $2$ is a nonzero nilpotent, hence a zero divisor | *Reduced Rings and the Nilradical* |
| $\mathbb{D} = \mathbb{R}[j]/(j^2-1)$ | the idempotents $e_{\pm}$ satisfy $e_+e_- = 0$ | *Split-Complex Algebra* |
| $\mathbb{D}'$ | $\varepsilon$ is a nonzero nilpotent | *Dual-Numbers Algebra* |
| $R \times S$ for nonzero $R, S$ | $(1,0)(0,1) = 0$ | *Examples of Rings and Fields* |
| $M_2(\mathbb{R})$ | not commutative, and it has zero divisors | *Matrix Algebras* |
| $\mathbb{H}$ | a division ring, but not commutative, so not a commutative domain | *Quaternion Algebra* |
| the free algebra, $A_1(k)$, $k[G]$ of a torsion-free group | non-commutative domains; the subject of *List of Domains* | *Tensor Powers and the Free Algebra*, *Quotients of the Tensor Algebra*, *Non-Commutative Domains* |

A non-commutative domain is not a counterexample to the definition of an integral domain but a different object: the absence of zero divisors is shared, and commutativity is the extra hypothesis.

## Summary

This article has listed the integral domains of the corpus with the rung of the divisibility ladder each reaches. The Euclidean domains are $\mathbb{Z}$, $\mathbb{Z}[i]$, $\mathbb{Z}[\sqrt{2}]$, $\mathbb{Z}[\sqrt{-2}]$ and $k[x]$; the principal ideal domain that is not Euclidean is $\mathbb{Z}[(1+\sqrt{-19})/2]$; the unique factorisation domains that are not principal are $\mathbb{Z}[x]$ and $k[x_1, \dots, x_n]$ for $n \geq 2$; the Bézout domain that is neither Noetherian nor a unique factorisation domain is $\overline{\mathbb{Z}}$; and the classical failure of unique factorisation is $\mathbb{Z}[\sqrt{-5}]$, with $6 = 2 \cdot 3 = (1+\sqrt{-5})(1-\sqrt{-5})$. The rings that are not domains are recorded with the zero divisor that excludes them.

## Summary of Notation

A catalogue denotes its objects by name rather than by symbol. The symbols that appear in the tables are the following.

| Symbol | Meaning |
|---|---|
| $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$ | The number systems |
| $\mathbb{Z}/n\mathbb{Z}$, $\mathbb{F}_p$, $\mathbb{F}_q$ | Residue ring, prime field, finite field |
| $\mathbb{Z}[i]$, $\mathbb{Z}[\sqrt{2}]$, $\mathbb{Z}[\sqrt{-2}]$, $\mathbb{Z}[\sqrt{-5}]$ | Quadratic integer rings |
| $\mathbb{Z}[(1+\sqrt{-19})/2]$ | Principal ideal domain that is not Euclidean |
| $\overline{\mathbb{Z}}$, $\mathcal{O}_K$ | All algebraic integers, ring of integers of $K$ |
| $k[x]$, $k[x_1,\dots,x_n]$, $\mathbb{Z}[x]$, $k[[x]]$ | Polynomial and power series rings |
| $k(x)$, $k((t))$ | Rational function field, Laurent series field |
| $\mathbb{Z}_{(p)}$, $\mathbb{Z}_p$, $\mathbb{Q}_p$ | Localisation at $p$, $p$-adic integers, $p$-adic numbers |
| $\operatorname{Frac}(R)$ | Field of fractions |
| $\mathbb{D}$, $\mathbb{D}'$ | Split-complex numbers, dual numbers; not domains |
| $M_2(\mathbb{R})$, $\mathbb{H}$ | Matrix ring, quaternions; not commutative domains |

## Further Reading

- Paulo Ribenboim, *Classical Theory of Algebraic Numbers* (Springer, 2001), for the quadratic integer rings, the failure of unique factorisation and the class group.
- Oscar Zariski and Pierre Samuel, *Commutative Algebra*, Volume I (Van Nostrand, 1958), for the divisibility ladder from domains to fields and the Bézout case.
- Irving Kaplansky, *Commutative Rings* (University of Chicago Press, revised ed. 1974), for integral domains, their localisations and their fraction fields.
