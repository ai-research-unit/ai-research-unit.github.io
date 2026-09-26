
# __List of Commutative Fields__

## Introduction

This article lists every field that the corpus introduces — $\mathbb{Q}$, $\mathbb{R}$ and $\mathbb{C}$, the finite fields, the $p$-adic fields, the rational function fields $k(x)$ and the Laurent series fields $k((t))$, the real algebraic numbers and the number fields — with the characteristic of each and the extensions of each. Every entry points to the article that introduces the object.

The list separates the fields of characteristic $0$, which contain a copy of $\mathbb{Q}$, from those of characteristic $p$, which contain a copy of $\mathbb{F}_p$; it separates the fields that are algebraically closed, such as $\mathbb{C}$, $\overline{\mathbb{Q}}$, $\overline{\mathbb{F}_p}$ and $\mathbb{C}_p$, from those that are only real closed, such as $\mathbb{R}$ and the real algebraic numbers; and it records the extensions and completions that the corpus builds from a given field.

The article introduces nothing and proves nothing. It records examples and non-examples side by side.

## The Prime Fields and the Number Systems

| Field | Characteristic | The prime field it contains | Extensions and closures | Introduced in |
|---|---|---|---|---|
| $\mathbb{Q}$ | $0$ | itself | the number fields; the completions $\mathbb{R}$ and $\mathbb{Q}_p$; the algebraic closure $\overline{\mathbb{Q}}$ | *The Rational Numbers* |
| $\mathbb{R}$ | $0$ | $\mathbb{Q}$ | $\mathbb{C} = \mathbb{R}(i)$, its algebraic closure; the real algebraic numbers as a proper subfield | *The Real Numbers* |
| $\mathbb{C}$ | $0$ | $\mathbb{Q}$ | algebraically closed; already its own algebraic closure | *The Complex Numbers* |
| $\overline{\mathbb{Q}}$, the algebraic numbers | $0$ | $\mathbb{Q}$ | algebraically closed; the algebraic closure of $\mathbb{Q}$ | *Algebraically Closed Fields* |
| $\overline{\mathbb{Q}} \cap \mathbb{R}$, the real algebraic numbers | $0$ | $\mathbb{Q}$ | the real closure of $\mathbb{Q}$; algebraic closure $\overline{\mathbb{Q}}$; countable and not order-complete | *Real-Closed and Complete Ordered Fields* |
| a number field $K$ | $0$ | $\mathbb{Q}$ | finite over $\mathbb{Q}$; completions at its primes | *Algebraic Number Theory* |
| $\mathbb{Q}(\zeta_n)$, a cyclotomic field | $0$ | $\mathbb{Q}$ | degree $\varphi(n)$ over $\mathbb{Q}$; the cyclotomic subfields | *Cyclotomic Fields* |
| $\mathbb{Q}(\sqrt{d})$, a quadratic field | $0$ | $\mathbb{Q}$ | degree $2$ over $\mathbb{Q}$; imaginary for $d < 0$, real for $d > 0$ | *Algebraic Number Theory* |

A field of characteristic $0$ contains a copy of $\mathbb{Q}$, and the prime field is the intersection of all its subfields. The real algebraic numbers are the real closure of $\mathbb{Q}$ and are countable; the algebraic numbers $\overline{\mathbb{Q}}$ are its algebraic closure, so the algebraic closure of the real algebraic numbers is $\overline{\mathbb{Q}}$ rather than $\mathbb{C}$.

## The Finite Fields and Characteristic $p$

| Field | Characteristic | The prime field it contains | Extensions and subfields | Introduced in |
|---|---|---|---|---|
| $\mathbb{F}_p$ | $p$ | itself | $\mathbb{F}_q$ is a vector space over it; the prime subfield of every characteristic-$p$ field | *Finite Fields* |
| $\mathbb{F}_q$, $q = p^n$ | $p$ | $\mathbb{F}_p$ | unique of order $q$; $\mathbb{F}_{p^m} \subseteq \mathbb{F}_{p^n}$ exactly when $m \mid n$ | *Finite Fields* |
| $\overline{\mathbb{F}_p}$ | $p$ | $\mathbb{F}_p$ | algebraically closed; the union of the $\mathbb{F}_{p^n}$; the residue field of $\mathbb{C}_p$ | *Finite Fields* |
| any field of characteristic $p$ | $p$ | $\mathbb{F}_p$ | contains $\mathbb{F}_p$ as its prime field; the Frobenius is injective | *Fields* |

The finite fields are exhausted by this list, and for each prime power $q$ there is exactly one field of order $q$ up to isomorphism; the Frobenius map and the cyclic multiplicative group of order $q - 1$ are recorded in *Finite Fields*. The finite fields are fields of this list and not of the non-commutative list, by Wedderburn's little theorem.

## The $p$-adic and Complete Valued Fields

| Field | Characteristic | Valuation ring and residue field | Extensions and closures | Introduced in |
|---|---|---|---|---|
| $\mathbb{Q}_p$ | $0$ | $\mathbb{Z}_p$, maximal ideal $p\mathbb{Z}_p$, residue field $\mathbb{F}_p$, value group $\mathbb{Z}$ | finite extensions; the algebraic closure $\overline{\mathbb{Q}_p}$; the completion $\mathbb{C}_p$ | *Absolute Values, Valuations and Completions* |
| $\mathbb{C}_p$ | $0$ | $\overline{\mathbb{Z}_p}$, residue field $\overline{\mathbb{F}_p}$, value group $\mathbb{Q}$ | algebraically closed and complete | *Absolute Values, Valuations and Completions* |
| $\overline{\mathbb{Q}_p}$ | $0$ | $\overline{\mathbb{Z}_p}$ | not complete; its completion is $\mathbb{C}_p$ | *Absolute Values, Valuations and Completions* |
| $\mathbb{R}$ | $0$ | the Archimedean completion of $\mathbb{Q}$ | as in the first table | *The Real Numbers* |

The two completions of $\mathbb{Q}$ at the Archimedean and the non-Archimedean places are $\mathbb{R}$ and $\mathbb{Q}_p$, by Ostrowski's theorem recorded in *Absolute Values, Valuations and Completions*. The completion preserves the value group and the residue field in the non-Archimedean case, which is why $\mathbb{Q}_p$ has value group $\mathbb{Z}$ and residue field $\mathbb{F}_p$.

## Rational Function Fields and Laurent Series Fields

| Field | Characteristic | Residue field and value group | Extensions and closures | Introduced in |
|---|---|---|---|---|
| $k(x)$, $k(x_1, \dots, x_n)$ | $\operatorname{char} k$ | — | the fraction field of $k[x]$; a purely transcendental extension | *Fields*, §19 |
| $k((t))$ | $\operatorname{char} k$ | $k$, value group $\mathbb{Z}$ | the completion of $k(t)$ at the $t$-adic valuation | *Absolute Values, Valuations and Completions* |
| $\mathbb{F}_p((t))$ | $p$ | $\mathbb{F}_p$, value group $\mathbb{Z}$ | the completion of $\mathbb{F}_p(t)$ | *Absolute Values, Valuations and Completions* |
| the Puiseux series field | $0$ | — | the real closure of $\mathbb{R}(t)$ with $t$ infinite | *Real-Closed and Complete Ordered Fields* |
| $\operatorname{Frac}(R)$ of a domain $R$ | $\operatorname{char} R$ | — | the smallest field containing $R$ | *Localization and the Fraction Field* |

The rational function field $k(x)$ is the fraction field of the polynomial ring $k[x]$, and the Laurent series field $k((t))$ is its completion at the $t$-adic valuation. The two constructions differ by completion, and the residue field and the value group are the invariants that record the difference.

## The Algebraic Closures of the Fields

Every field has an algebraic closure, unique up to isomorphism, and for the fields of this list the closure is known by name.

| Field | Its algebraic closure | Introduced in |
|---|---|---|
| $\mathbb{Q}$ | $\overline{\mathbb{Q}}$, the algebraic numbers | *Algebraically Closed Fields* |
| $\mathbb{R}$ | $\mathbb{C} = \mathbb{R}(i)$ | *Galois Theory of ℂ/ℝ* |
| the real algebraic numbers $\overline{\mathbb{Q}} \cap \mathbb{R}$ | $\overline{\mathbb{Q}}$, not $\mathbb{C}$, since $\mathbb{C}$ is transcendental over $\mathbb{Q}$ | *Real-Closed and Complete Ordered Fields* |
| $\mathbb{F}_p$, $\mathbb{F}_q$ | $\overline{\mathbb{F}_p}$, the union of the $\mathbb{F}_{p^n}$ | *Finite Fields* |
| $\mathbb{Q}_p$ | $\overline{\mathbb{Q}_p}$, whose completion is $\mathbb{C}_p$ | *Absolute Values, Valuations and Completions* |
| a number field $K$ | $\overline{\mathbb{Q}}$ | *Algebraic Number Theory* |

The case of $\mathbb{R}$ is the Galois theory of $\mathbb{C}$ over $\mathbb{R}$: the extension has degree $2$, generated by a root of $x^2 + 1$, and $\mathbb{C}$ is algebraically closed by the fundamental theorem of algebra. The case of $\mathbb{F}_p$ is the union of the finite extensions $\mathbb{F}_{p^n}$, one for each $n$ inside the closure. For the real algebraic numbers the closure is not $\mathbb{C}$, because $\mathbb{C}$ contains transcendental elements over $\mathbb{Q}$.

## Characteristic and Extensions at a Glance

| Characteristic | The prime field | The fields of the corpus | Introduced in |
|---|---|---|---|
| $0$ | $\mathbb{Q}$ | $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$, $\overline{\mathbb{Q}}$, the real algebraic numbers, the number fields, $\mathbb{Q}_p$, $\mathbb{C}_p$, $k(x)$ and $k((t))$ for $k$ of characteristic $0$ | *The Rational Numbers*, *Finite Fields*, *Absolute Values, Valuations and Completions*, *Fields* |
| $p$ | $\mathbb{F}_p$ | $\mathbb{F}_p$, $\mathbb{F}_q$, $\overline{\mathbb{F}_p}$, $\mathbb{F}_p((t))$, and $k(x)$, $k((t))$ for $k$ of characteristic $p$ | *Finite Fields*, *Absolute Values, Valuations and Completions*, *Fields* |

## Warnings

| Object | Why it is not a field | Introduced in |
|---|---|---|
| $\mathbb{H}$ | a division ring, but not commutative; a skew field | *Quaternion Algebra* |
| the division ring of fractions of $A_1(k)$ | not commutative | *Ore Domains and Division Rings of Fractions* |
| $\mathbb{Z}$, $\mathbb{Z}[x]$, $\mathbb{Z}[i]$ | commutative domains that are not fields: not every nonzero element is a unit | *The Integers*, *Examples of Rings and Fields* |
| $\mathbb{O}$ | a division algebra whose multiplication is not associative; not a ring | *Octonion Algebra* |
| the zero ring $\{0\}$ | excluded by the convention $1 \neq 0$; a field has $1 \neq 0$ | *Rings*, §2 |

A commutative division ring is a field, so $\mathbb{H}$ is excluded by commutativity alone and not by the absence of inverses. By Wedderburn's little theorem a finite division ring is a field, so there is no finite skew field and *List of Division Rings and Skew Fields* is left with the infinite ones.

## Summary

This article has listed the fields of the corpus with their characteristic and their extensions. The characteristic-$0$ fields are the number systems and their closures and completions; the characteristic-$p$ fields are the finite fields, their algebraic closure and the Laurent series fields over a field of characteristic $p$; the function fields $k(x)$ and the Laurent series fields $k((t))$ carry the characteristic of their ground field; and the real algebraic numbers, the real closure of $\mathbb{Q}$, are the field that is real closed without being order-complete. The extensions of each are recorded beside it: the algebraic closures $\overline{\mathbb{Q}}$, $\overline{\mathbb{F}_p}$ and $\mathbb{C}_p$, the completion $\mathbb{C}_p$ of $\overline{\mathbb{Q}_p}$, and the algebraic closure $\mathbb{C} = \mathbb{R}(i)$ of $\mathbb{R}$.

## Summary of Notation

A catalogue denotes its objects by name rather than by symbol. The symbols that appear in the tables are the following.

| Symbol | Meaning |
|---|---|
| $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$ | The rational, real and complex fields |
| $\overline{\mathbb{Q}}$, $\overline{\mathbb{F}_p}$, $\overline{\mathbb{Q}_p}$ | Algebraic closures |
| $\mathbb{F}_p$, $\mathbb{F}_q$ | The finite fields of order $p$ and $q = p^n$ |
| $\mathbb{Q}_p$, $\mathbb{Z}_p$, $\mathbb{C}_p$ | $p$-adic numbers, $p$-adic integers, complete algebraic closure |
| $k(x)$, $k((t))$, $\mathbb{F}_p((t))$ | Rational function field, Laurent series fields |
| $\mathbb{Q}(\zeta_n)$, $\mathbb{Q}(\sqrt{d})$, $K$ | Cyclotomic, quadratic and number fields |
| $\overline{\mathbb{Q}} \cap \mathbb{R}$ | The real algebraic numbers |
| $\operatorname{Frac}(R)$ | Field of fractions |
| $\varphi(n)$ | Euler totient, the degree $[\mathbb{Q}(\zeta_n):\mathbb{Q}]$ |
| $\operatorname{char} k$ | The characteristic of a field |
| $\mathbb{H}$ | The quaternions; a division ring, not a field |

## Further Reading

- Serge Lang, *Algebra* (Springer, revised 3rd ed. 2002), for field extensions, algebraic closures and the classification of finite fields.
- Neal Koblitz, *p-adic Numbers, p-adic Analysis, and Zeta-Functions* (Springer, 2nd ed. 1984), for $\mathbb{Q}_p$ and $\mathbb{C}_p$ as fields with their valuations.
- John B. Fraleigh, *A First Course in Abstract Algebra* (Addison–Wesley, 7th ed. 2003), for a tabulation of the standard examples of fields and their characteristic.
