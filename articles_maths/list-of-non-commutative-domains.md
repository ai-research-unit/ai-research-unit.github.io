
# __List of Non-Commutative Domains__

## Introduction

This article lists the non-commutative domains of the corpus: the rings with $1 \neq 0$ and no zero divisors in which commutativity is not assumed. Every entry points to the article that introduces the object.

The list gathers $\mathbb{H}$, the free algebra, the Weyl algebra and the group ring of a torsion-free group, as the scope names, together with the division rings of the corpus, which are domains for the trivial reason that every nonzero element is invertible. The intersection of this ladder with the commutative one is exactly the integral domains; the commutative domains are listed in *List of Integral Domains*.

The article introduces nothing and proves nothing. It records examples and non-examples side by side.

## What a Non-Commutative Domain Adds

A non-commutative domain is a ring with $1 \neq 0$ and no zero divisors: $ab = 0$ forces $a = 0$ or $b = 0$. Cancellation holds on both sides, but the left ideals and the right ideals need not match, and a domain need not have a division ring of fractions. The definition is in *Non-Commutative Domains*, and the consequences for the ideal structure are developed there.

| Feature | The commutative case | The non-commutative case | Introduced in |
|---|---|---|---|
| no zero divisors | the definition of an integral domain | the definition of a domain | *Non-Commutative Domains* |
| cancellation | on both sides, by commutativity | on both sides, directly from no zero divisors | *Non-Commutative Domains* |
| fraction object | the field of fractions always exists | a division ring of fractions exists only under the Ore condition | *Ore Domains and Division Rings of Fractions* |
| ideals | left and right ideals coincide | left and right ideals may differ | *Non-Commutative Domains* |

The last two rows are the whole difference between the two ladders. A commutative domain always embeds in a field; a non-commutative domain embeds in a division ring exactly when it is an Ore domain, and the free algebra is the standard domain for which this fails.

## The Domains of the Corpus

| Domain | Ground ring or centre | What makes it a domain | Introduced in |
|---|---|---|---|
| $\mathbb{H}$ | $\mathbb{R}$ | every nonzero element is invertible | *Quaternion Algebra* |
| a division ring, for instance the division ring of fractions of $A_1(k)$ | its centre, a field | every nonzero element is invertible | *Division Rings* |
| $R\langle x_1, \dots, x_n\rangle$ | $R$ | the leading terms of a product do not cancel | *Tensor Powers and the Free Algebra* |
| $A_1(k) = k\langle x, y\rangle/(yx - xy - 1)$ | $k$ | the leading term in $x$ and $y$ does not cancel | *Quotients of the Tensor Algebra* |
| $k[G]$, $G$ torsion-free | $k$ | the theorem of Malcev and B. H. Neumann | *Non-Commutative Domains* |
| $k[F_n]$, the group ring of a free group | $k$ | $F_n$ is torsion-free | *Ore Domains and Division Rings of Fractions* |
| $k[G]$ for $G$ an ordered group | $k$ | the Malcev–Neumann embedding of $k[G]$ in a division ring | *Ore Domains and Division Rings of Fractions* |
| an integral domain | its own centre, the ring itself | commutativity is the special case | *Integral Domains* |

The commutative domains are included in the last row so that the intersection of the two chains is visible: $\mathbb{Z}$, $\mathbb{Z}[i]$, $k[x]$ and every field are domains in the non-commutative sense as well, but they are listed with the commutative ladder in *List of Integral Domains*. The group ring of a free group is the concrete case of the torsion-free hypothesis that the scope names; the free algebra is the monoid algebra of the free monoid, the case in which the indeterminates do not commute.

## The Group Ring and the Torsion-Free Hypothesis

| Group ring | The hypothesis on $G$ | Domain? | Introduced in |
|---|---|---|---|
| $k[G]$ | $G$ torsion-free | yes, provided $k$ is a domain | *Non-Commutative Domains* |
| $k[F_n]$ | $F_n$ free | yes | *Ore Domains and Division Rings of Fractions* |
| $k[\mathbb{Z}] \cong k[x, x^{-1}]$ | $\mathbb{Z}$ torsion-free | yes; commutative | *Group Algebras* |
| $k[C_2]$, $k$ of characteristic $\neq 2$ | $C_2$ has torsion | no: $k[C_2] \cong k \times k$ has zero divisors | *Examples of Rings and Fields* |
| $\mathbb{F}_2[C_2]$ | $C_2$ has torsion | no: $\mathbb{F}_2[C_2] \cong \mathbb{F}_2[x]/(x+1)^2$ is local with a nilpotent | *Examples of Rings and Fields* |
| $k[C_p]$, with $\zeta_p \in k$ and $\operatorname{char} k \nmid p$ | $C_p$ has torsion | no: $k[C_p] \cong k^p$, a product of fields | *Group Algebras* |

The torsion-free hypothesis is necessary and the two counterexamples in characteristic zero and characteristic two show it. The group ring of a torsion-free group need not be Ore, however: the torsion-free hypothesis gives the absence of zero divisors and not the existence of a division ring of fractions, which is the subject of *Ore Domains and Division Rings of Fractions*.

## Two Domains With and Without a Division Ring of Fractions

The Ore condition is what makes the division ring of fractions of a domain exist; the free algebra and the Weyl algebra are the two sides of the boundary.

| Domain | Ore? | Division ring of fractions | Introduced in |
|---|---|---|---|
| $R\langle x_1, \dots, x_n\rangle$, $n \geq 2$ | no | none | *Ore Domains and Division Rings of Fractions* |
| $A_1(k)$ | yes | the division ring of fractions of $A_1(k)$, infinite-dimensional over $k$ | *Ore Domains and Division Rings of Fractions* |
| $k[G]$, $G$ orderable | yes, by the Malcev–Neumann construction | the Malcev–Neumann division ring of series | *Ore Domains and Division Rings of Fractions* |
| $\mathbb{H}$ | trivially | itself, being already a division ring | *Quaternion Algebra* |

The free algebra is the standard non-Ore domain, and it is a domain all the same; the two properties, no zero divisors and the Ore condition, are independent, and this table is the reason the ladder of *List of Structures from Rings to Division Rings* has a rung between a domain and a division ring.

## Domains That Are Division Rings

A division ring is a domain in which every nonzero element is a unit; the class is listed in full in *List of Division Rings and Skew Fields*. The relation to the present list is that a division ring is the strongest domain, and it is the only case in which the left and right ideal structure is trivial.

| Division ring | Why it is a domain of this list | Introduced in |
|---|---|---|
| $\mathbb{H}$ | every nonzero element is invertible; the domain hypothesis is automatic | *Quaternion Algebra* |
| the division ring of fractions of $A_1(k)$ | it is the Ore division ring of the Weyl algebra | *Ore Domains and Division Rings of Fractions* |
| the free field | generated by a free algebra | *Ore Domains and Division Rings of Fractions* |
| a commutative division ring | a field, hence a commutative domain | *Fields* |

## Non-Examples: Rings That Fail Cancellation

| Ring | The zero divisor that excludes it | Introduced in |
|---|---|---|
| $M_n(\mathbb{R})$, $n \geq 2$ | the matrix units $E_{11}E_{22} = 0$ | *Matrix Algebras* |
| $\mathbb{B}$, the biquaternions | nilpotent elements; not a division ring | *Biquaternion Zero Divisors* |
| $\mathbb{H}_{\mathbb{D}}$, the split-biquaternions | the idempotents $e_{\pm}$ satisfy $e_+e_- = 0$ | *Split-Biquaternion Zero Divisors* |
| $k[C_2]$ over a field of characteristic $\neq 2$ | $k[C_2] \cong k \times k$ | *Examples of Rings and Fields* |
| $\mathbb{D}$, the split-complex numbers | $e_+ e_- = 0$; commutative, so an integral-domain failure | *Split-Complex Algebra* |
| $\mathbb{D}'$, the dual numbers | $\varepsilon$ is a nonzero nilpotent | *Dual-Numbers Algebra* |
| $\mathbb{Z}/6\mathbb{Z}$ | $2 \cdot 3 = 0$ | *Modular Arithmetic and the Ring of Residues* |

The matrix ring $M_2(\mathbb{R})$ is the standard non-commutative ring with zero divisors, and the biquaternions and split-biquaternions are the standard eight-dimensional ones. None of them is a domain, and none of them is an integral domain either.

## Warnings

| Object | Why it is not on this list | Introduced in |
|---|---|---|
| $\mathbb{O}$ | a division algebra whose multiplication is not associative, so not a ring | *Octonion Algebra* |
| $\mathbb{S}$ | the sedenions, non-associative and with zero divisors | *Division Algebras* |
| the commutative domains $\mathbb{Z}$, $\mathbb{Z}[i]$, $k[x]$ | domains, but listed on the commutative ladder in *List of Integral Domains* | *The Integers*, *Examples of Rings and Fields* |
| the ring of upper triangular matrices | not a domain: the strictly upper triangular matrices square to zero | *Matrix Algebras* |

## Summary

This article has listed the non-commutative domains of the corpus: $\mathbb{H}$ and the division rings, for which the domain property is automatic; the free algebra and the Weyl algebra, which are domains by their leading-term behaviour; and the group rings of torsion-free groups, which are domains by the torsion-free hypothesis. It has recorded the two features that distinguish this ladder from the commutative one, the asymmetry of the one-sided ideals and the conditional existence of a division ring of fractions, and it has named the matrix rings, the biquaternions, the split-biquaternions and the group rings of groups with torsion as the objects that fail the definition.

## Summary of Notation

A catalogue denotes its objects by name rather than by symbol. The symbols that appear in the tables are the following.

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | The real quaternions, a division ring |
| $\mathbb{H}_{\mathbb{D}}$, $\mathbb{B}$ | The split-biquaternions, the biquaternions; not domains |
| $\mathbb{O}$, $\mathbb{S}$ | The octonions and sedenions; not rings |
| $A_1(k)$ | The Weyl algebra $k\langle x,y\rangle/(yx - xy - 1)$ |
| $R\langle x_1,\dots,x_n\rangle$ | The free algebra |
| $k[G]$, $k[F_n]$, $k[C_2]$ | Group rings; $F_n$ free, $C_2$ of order two |
| $M_2(\mathbb{R})$ | The $2 \times 2$ real matrix ring; not a domain |
| $\mathbb{Z}$, $\mathbb{Z}[i]$, $k[x]$ | Commutative domains, on the ladder of *List of Integral Domains* |
| $\mathbb{D}$, $\mathbb{D}'$ | Split-complex numbers, dual numbers; not domains |

## Further Reading

- Tsit-Yuen Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for non-commutative domains, their one-sided ideals and their division rings of fractions.
- Paul M. Cohn, *Free Rings and Their Relations* (Academic Press, 2nd ed. 1985), for the free algebra, the free ideal theory and the embeddings of domains in division rings.
- Donald S. Passman, *The Algebraic Structure of Group Rings* (Wiley, 1977), for the group ring of a torsion-free group and the zero-divisor problem.
