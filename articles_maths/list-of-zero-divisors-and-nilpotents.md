
# __List of Zero Divisors and Nilpotents__

## Introduction

This article lists the rings of the corpus that carry zero divisors and those that carry nilpotents — the dual numbers, $\mathbb{Z}/4\mathbb{Z}$, $\mathbb{Z}/6\mathbb{Z}$, $M_2(\mathbb{R})$, the product rings and the biquaternions — and it separates the three reasons a zero divisor can occur: a nonzero nilpotent, a nontrivial idempotent, and torsion in a finite ring. Every entry points to the article that introduces the object.

The nilpotents are the elements with some power zero, and they form the nilradical when the nilradical is defined; the idempotent zero divisors are the nontrivial idempotents $e$ with $e(1-e) = 0$, and they decompose the ring; and the torsion case is the finite ring $\mathbb{Z}/n\mathbb{Z}$ whose zero divisors come from the factors of $n$ and need not be nilpotent. The three cases are independent, and each ring of the list is placed in exactly one of them where possible.

The article introduces nothing and proves nothing. It records examples and non-examples side by side.

## The Three Kinds of Zero Divisor

| Kind | The defining relation | A nilpotent? | An idempotent? | Introduced in |
|---|---|---|---|---|
| nilpotent | $a^n = 0$ for some $n \geq 1$ | yes | not in general | *Reduced Rings and the Nilradical* |
| idempotent zero divisor | $e^2 = e$ with $e \neq 0, 1$ | no | yes | *Rings*, §§8–9 |
| torsion zero divisor | $n \cdot a = 0$ for some $n \neq 0$ | only when $n$ is not squarefree | in general no | *Modular Arithmetic and the Ring of Residues* |

Every nonzero nilpotent is a zero divisor, since $a \cdot a^{n-1} = 0$ with $a^{n-1} \neq 0$ when $n \geq 2$ is the first exponent with $a^n = 0$; a nilpotent is never a nonzero idempotent, because $e^2 = e$ forces $e^n = e$ for all $n$. The reverse implications fail, and the failures are the content of the sections below: $\mathbb{Z}/6\mathbb{Z}$ has zero divisors that are neither nilpotent nor idempotent, and the split-biquaternions have idempotent zero divisors and no nonzero nilpotents.

## The Nilpotents

| Ring | The nilpotent | Its index | Introduced in |
|---|---|---|---|
| $\mathbb{D}'$, the dual numbers | $\varepsilon$, with $\varepsilon^2 = 0$ | $2$ | *Dual-Numbers Algebra* |
| $\mathbb{Z}/4\mathbb{Z}$ | $2$, with $2^2 = 0$ | $2$ | *Reduced Rings and the Nilradical* |
| $\mathbb{Z}/8\mathbb{Z}$ | $2$, with $2^3 = 0$ | $3$ | *Modular Arithmetic and the Ring of Residues* |
| $\mathbb{Z}/p^n\mathbb{Z}$ | $p$, with $p^n = 0$ | $n$ | *Modular Arithmetic and the Ring of Residues* |
| $k[x]/(x^n)$ | $x$, with $x^n = 0$ | $n$ | *Examples of Rings and Fields* |
| $\mathbb{F}_2[C_2]$ | $x + 1$, with $(x+1)^2 = 0$ | $2$ | *Examples of Rings and Fields* |
| $M_2(\mathbb{R})$ | the strictly upper triangular $N = E_{12}$ | $2$ | *Matrix Algebras* |
| $\mathbb{B}$, the biquaternions | the pure zero divisors satisfying $\tilde{Q}^2 = 0$ | $2$ | *Biquaternion Zero Divisors* |
| $\mathbb{Z}/12\mathbb{Z}$ | $6$, with $6^2 = 0$ | $2$ | *Modular Arithmetic and the Ring of Residues* |

The nilpotents of a commutative ring form an ideal, the nilradical, which is the intersection of the prime ideals; this is developed in *Reduced Rings and the Nilradical* and *Rings*, §§6–7. In $\mathbb{B}$ the nilpotents are exactly the pure zero divisors, the elements with vanishing scalar part and $\tilde{Q}^2 = 0$, and they form the nilpotent cone of real dimension $4$ described in *Biquaternion Zero Divisors*.

## The Idempotent Zero Divisors

| Ring | The nontrivial idempotents | The decomposition they induce | Introduced in |
|---|---|---|---|
| $\mathbb{D}$, the split-complex numbers | $e_{\pm} = \tfrac{1}{2}(1 \pm j)$ | $\mathbb{D} \cong \mathbb{R} \times \mathbb{R}$ | *Split-Complex Algebra* |
| $\mathbb{Z}/6\mathbb{Z}$ | the images of $(1,0)$ and $(0,1)$ | $\mathbb{Z}/6\mathbb{Z} \cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/3\mathbb{Z}$ | *Modular Arithmetic and the Ring of Residues* |
| $R \times S$ | $(1,0)$ and $(0,1)$ | the ring is the product by construction | *Examples of Rings and Fields* |
| $\mathbb{H}_{\mathbb{D}}$, the split-biquaternions | $e_+$, $e_-$ | $\mathbb{H}_{\mathbb{D}} \cong \mathbb{H} \oplus \mathbb{H}$ | *Split-Biquaternion Zero Divisors* |
| $M_2(\mathbb{R})$ | $E_{11}$, $E_{22}$ | the column decomposition $\mathbb{R}^2 = \mathbb{R}e_1 \oplus \mathbb{R}e_2$ | *Matrix Algebras* |
| a Boolean ring $B$ | every element | $B$ is a product of copies of $\mathbb{F}_2$ | *Von Neumann Regular Rings* |
| $\mathbb{Q}[C_3]$ | the orbit sums of the components | $\mathbb{Q}[C_3] \cong \mathbb{Q} \times \mathbb{Q}(\zeta_3)$ | *Examples of Rings and Fields* |
| $\mathbb{R}[x]/(x^2 - 1)$ | the images of the factors | $\mathbb{R}[x]/(x^2-1) \cong \mathbb{R} \times \mathbb{R}$ | *Examples of Rings and Fields* |

A nontrivial idempotent $e$ satisfies $e(1-e) = 0$ with $e \neq 0$ and $1 - e \neq 0$, so it is a zero divisor, and it induces the direct sum decomposition $R = Re \oplus R(1-e)$ with the two-sided ideals $Re$ and $R(1-e)$. The decomposition of a ring into a product of two rings is the same thing as a pair of complementary idempotents, and this is the sense in which the idempotents of a commutative Artinian ring give its splitting into local rings, as recorded in *List of Reduced, Local and Product Rings*.

## The Torsion Case

| Ring | The zero divisors | Nilpotents? | Idempotents? | Introduced in |
|---|---|---|---|---|
| $\mathbb{Z}/n\mathbb{Z}$, $n$ squarefree | the nonzero nonunits, all from the factors | none | $2^{\omega(n)}$ of them, one for each factor | *Modular Arithmetic and the Ring of Residues* |
| $\mathbb{Z}/6\mathbb{Z}$ | $2, 3, 4$ | none | the images of $(1,0)$, $(0,1)$ | *Modular Arithmetic and the Ring of Residues* |
| $\mathbb{Z}/12\mathbb{Z}$ | the nonzero nonunits | $6$ | from the factors of $12$ | *Modular Arithmetic and the Ring of Residues* |
| $\mathbb{Z}/p^2\mathbb{Z}$ | the multiples of $p$ | $p$ | none: the ring is local | *Modular Arithmetic and the Ring of Residues* |
| $\mathbb{Z}/p^n\mathbb{Z}$ | the multiples of $p$ | $p$ | none: the ring is local | *Modular Arithmetic and the Ring of Residues* |

The torsion case is where the three kinds of zero divisor separate most cleanly: $\mathbb{Z}/6\mathbb{Z}$ has zero divisors and no nilpotents, so it is reduced; $\mathbb{Z}/4\mathbb{Z}$ and $\mathbb{Z}/p^n\mathbb{Z}$ have nilpotents and no nontrivial idempotents, so they are local and not reduced; and $\mathbb{Z}/12\mathbb{Z}$ has both, since $12$ is neither squarefree nor a prime power. The Chinese remainder theorem records the decomposition, and it is stated in *Modular Arithmetic and the Ring of Residues*.

## The Non-Commutative Cases

| Ring | Nilpotents | Idempotent zero divisors | Introduced in |
|---|---|---|---|
| $M_2(\mathbb{R})$ | yes: the nilpotent matrices with $N^2 = 0$ | yes: $E_{11}$, $E_{22}$ | *Matrix Algebras* |
| $\mathbb{B}$, the biquaternions | yes: the pure zero divisors | yes: the complex multiples of the idempotents | *Biquaternion Zero Divisors* |
| $\mathbb{H}_{\mathbb{D}}$, the split-biquaternions | no nonzero nilpotents | yes: $e_+$, $e_-$ | *Split-Biquaternion Zero Divisors* |
| $\mathbb{H}$ | none | none | *Quaternion Algebra* |
| the upper triangular matrices | yes: the strictly upper triangular matrices | yes: the diagonal idempotents | *Matrix Algebras* |
| $k[G]$ for $G$ with torsion | when the characteristic divides the order | from the idempotents of the group algebra | *Group Algebras* |

The two eight-dimensional cases are the contrast the corpus records: $\mathbb{B}$ has both kinds, since the vanishing of its norm form produces nilpotents as well as idempotents, while $\mathbb{H}_{\mathbb{D}}$ has only the idempotents, since it is isomorphic to the product $\mathbb{H} \oplus \mathbb{H}$ of two division rings and a product of division rings has no nonzero nilpotents. The matrix ring $M_2(\mathbb{R})$ is semisimple and has no nonzero nilpotent ideal, yet it has nilpotent elements: semisimplicity forbids a nilpotent ideal and not a nilpotent element.

## The Reduced Rings

| Ring | Why it has no nonzero nilpotent | Introduced in |
|---|---|---|
| every domain, for instance $\mathbb{Z}$, $k[x]$, $\mathbb{Z}[i]$ | a nilpotent would be a zero divisor | *Integral Domains* |
| every field | every nonzero element is a unit | *Fields* |
| $\mathbb{Z}/6\mathbb{Z}$ | the modulus is squarefree, so no nonzero element has a zero power | *Reduced Rings and the Nilradical* |
| a product of reduced rings | the nilpotents of a product are the tuples of nilpotents | *Reduced Rings and the Nilradical* |
| a Boolean ring | every element is idempotent, so $a^n = a \neq 0$ for $a \neq 0$ | *Von Neumann Regular Rings* |
| $\mathbb{H}_{\mathbb{D}}$, the split-biquaternions | isomorphic to $\mathbb{H} \oplus \mathbb{H}$, a product of division rings | *Split-Biquaternion Zero Divisors* |

A ring is reduced when it has no nonzero nilpotent, equivalently when its nilradical is zero. The reduced rings may still have zero divisors, and $\mathbb{Z}/6\mathbb{Z}$ and $\mathbb{H}_{\mathbb{D}}$ are the two standard cases of that phenomenon in the corpus: the first by torsion and the second by idempotents.

## Warnings

| Object | Why it has no zero divisors and no nilpotents | Introduced in |
|---|---|---|
| $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$ | integral domains and fields | *The Integers*, *Fields* |
| $k[x]$, $\mathbb{Z}[x]$, $k[x_1, \dots, x_n]$ | polynomial rings over a domain | *Polynomial Rings and Rational Functions* |
| $\mathbb{Z}[i]$, $\mathbb{Z}[\sqrt{-5}]$ | quadratic integer rings, hence domains | *Examples of Rings and Fields* |
| $\mathbb{H}$ | a division ring: every nonzero element is a unit | *Quaternion Algebra* |
| $k[F_n]$, the group ring of a free group | torsion-free group, domain | *Group Algebras* |
| the zero ring $\{0\}$ | $0 = 1$, excluded by the convention $1 \neq 0$ | *Rings*, §2 |

## Summary

This article has listed the rings of the corpus with zero divisors and with nilpotents, separating the three kinds. The nilpotents are $\varepsilon$ in the dual numbers, $2$ in $\mathbb{Z}/4\mathbb{Z}$ and $\mathbb{Z}/8\mathbb{Z}$, $p$ in $\mathbb{Z}/p^n\mathbb{Z}$, $x$ in $K[x]/(x^n)$, $x+1$ in $\mathbb{F}_2[C_2]$, the nilpotent and strictly upper triangular matrices in $M_2(\mathbb{R})$, and the pure zero divisors of the biquaternions; the idempotent zero divisors are $e_{\pm}$ in the split-complex numbers and the split-biquaternions, the images of $(1,0)$ and $(0,1)$ in $\mathbb{Z}/6\mathbb{Z}$ and in every product ring, the matrix units in $M_2(\mathbb{R})$, the elements of a Boolean ring, and the idempotents of $\mathbb{Q}[C_3]$; and the torsion case separates $\mathbb{Z}/6\mathbb{Z}$, which is reduced, from $\mathbb{Z}/4\mathbb{Z}$, which is not. The reduced rings, the domains and the fields close the list as the objects with no nilpotent and, in the last two cases, no zero divisor at all.

## Summary of Notation

A catalogue denotes its objects by name rather than by symbol. The symbols that appear in the tables are the following.

| Symbol | Meaning |
|---|---|
| $\mathbb{Z}/n\mathbb{Z}$ | The residue ring; $\mathbb{Z}/6\mathbb{Z}$ reduced, $\mathbb{Z}/4\mathbb{Z}$ not |
| $\varepsilon$ | The nilpotent generator of the dual numbers, $\varepsilon^2 = 0$ |
| $e_{\pm} = \tfrac{1}{2}(1 \pm j)$ | The idempotents of the split-complex numbers and the split-biquaternions |
| $E_{11}$, $E_{22}$, $E_{12}$ | Matrix units; $E_{12}$ is nilpotent |
| $\mathbb{D}$, $\mathbb{D}'$ | Split-complex numbers, dual numbers |
| $\mathbb{B}$, $\mathbb{H}_{\mathbb{D}}$ | Biquaternions with nilpotents, split-biquaternions without |
| $\mathbb{H}$ | The quaternions, with neither |
| $\tilde{Q}$ | A biquaternion |
| $B$ | A Boolean ring |
| $[a]$ | The class of $a$ in a residue ring |

## Further Reading

- Irving Kaplansky, *Commutative Rings* (University of Chicago Press, revised ed. 1974), for the nilradical, the reduced rings and the separation of nilpotents from zero divisors.
- Tsit-Yuen Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for idempotents, the Peirce decomposition and the zero divisors of matrix rings.
- S. J. Sangwine and D. Alfsmann, "Determination of the biquaternion divisors of zero, including the idempotents and nilpotents", *Advances in Applied Clifford Algebras* 20 (2010) 401–416, for the classification in the biquaternions.
