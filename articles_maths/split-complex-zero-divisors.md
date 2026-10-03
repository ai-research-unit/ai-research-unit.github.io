
# __Split-Complex Zero Divisors__

## Introduction

A **zero divisor** in a commutative ring is a nonzero element $A$ for which there is a nonzero element $B$ with $AB = 0$. The split-complex algebra has a zero-divisor set of real dimension $1$, the pair of null lines, and this article determines it, describes its two families, relates it to the idempotents, and gives the criterion in the idempotent coordinates; the metrical reading of the set is in *Split-Complex Norm and Invertibility*. It is the two-dimensional counterpart of *Biquaternion Zero Divisors*, where the null cone is a six-real-dimensional variety inside the eight-real-dimensional algebra.

**Placement.** The article is fourth in the Algebra group, after *Split-Complex Algebra*, *Split-Complex Idempotents and Projections* and *Split-Complex Ideals and Peirce Decomposition*, and before *Worked Examples in the Split-Complex Algebra*. It owns the classification of the null cone, in the algebraic form $a^2 = a'^2$; the metrical reading of that cone — the norm, its isotropy and the criterion by its vanishing — belongs to *Split-Complex Norm and Invertibility* in the Topology group. The idempotents $\Pi_\pm$ and the decomposition $\mathbb{D}\cong\mathbb{R}\oplus\mathbb{R}$ belong to *Split-Complex Idempotents and Projections*, and the minimal ideals to *Split-Complex Ideals and Peirce Decomposition*. This article is the boundary case: it classifies the null cone itself.

**Conventions.** The algebra is $\mathbb{D} = \mathbb{R}[x]/(x^2-1)$, basis $1$, $j$, $j^2 = +1$, general element $A = a+ja'$, conjugate $\bar A = a-ja'$, idempotents $\Pi_\pm = \tfrac12(1\pm j)$, idempotent coordinates $A = A_+\Pi_1 + A_-\Pi_2$ with $A_\pm = a\pm a'$. In this article $\mathcal{N} = \{A : a^2 = a'^2\}$ is the **null cone** and $\mathcal{Z} = \mathcal{N}\setminus\{0\}$ its set of non-zero points. The norm and the quadratic form it polarises are introduced and owned by *Split-Complex Norm and Invertibility*; the present article cites them and does not develop them.

## The Zero Divisors of $\mathbb{D}$

**Definition.** An element $A \in \mathbb{D}$ is a **zero divisor** if $A \neq 0$ and there exists $B \in \mathbb{D}$ with $B \neq 0$ and $AB = 0$. The **annihilator** of $A$ is

$$
\operatorname{ann}(A) = \{B \in \mathbb{D} : AB = 0\},
$$

an ideal of $\mathbb{D}$.

**Theorem.** A non-zero element $A \in \mathbb{D}$ is a zero divisor if and only if one of its idempotent coordinates vanishes, equivalently if and only if $a^2 = a'^2$.

**Proof.** If $A$ is a zero divisor, choose $B \neq 0$ with $AB = 0$. In idempotent coordinates $AB = A_+B_+\Pi_1 + A_-B_-\Pi_2$, so $AB = 0$ iff $A_+B_+ = 0$ and $A_-B_- = 0$. Since $B \neq 0$, at least one of $B_+, B_-$ is nonzero; if $B_+ \neq 0$ then $A_+B_+ = 0$ forces $A_+ = 0$, and if $B_- \neq 0$ then $A_-B_- = 0$ forces $A_- = 0$; in either case $A_+A_- = 0$. Conversely, if $A_+A_- = 0$ with $A \neq 0$, then one coordinate vanishes and the other does not; if $A_+ = 0$ then $A = A_-\Pi_2 \neq 0$ and $A \Pi_1 = A_-\Pi_2\Pi_1 = 0$ with $\Pi_1 \neq 0$, so $A$ is a zero divisor, and the case $A_- = 0$ is symmetric.

So the zero-divisor set is exactly the non-zero part of the null cone:

$$
\mathcal{Z} = \{A \neq 0 : a^2 = a'^2\} = \{A : A_+ = 0 \text{ or } A_- = 0, \; A \neq 0\}.
$$

The criterion makes no reference to a choice of annihilator; it also shows that for $A \neq 0$, being a zero divisor is equivalent to being a non-unit, since the units are exactly the elements whose two idempotent coordinates are nonzero (the criterion on the norm is in *Split-Complex Norm and Invertibility*). Thus every nonzero non-unit of $\mathbb{D}$ is a zero divisor, a state of affairs impossible in a field. The non-units do not form an ideal: $\mathcal{N}$ is not closed under addition, since $\Pi_1 + \Pi_2 = 1$ is a unit, so $\mathbb{D}$ is not a local ring and has no unique maximal ideal of non-units.

## The Null Cone and the Two Null Lines

The equation $a^2 = a'^2$ factors as

$$
(a-a')(a+a') = 0 \iff a = a' \ \text{or}\ a = -a',
$$

so the null cone is the union of the two lines

$$
\mathbb{R}(1+j) = \mathbb{R}\Pi_1, \qquad \mathbb{R}(1-j) = \mathbb{R}\Pi_2,
$$

and $\mathcal{Z} = \mathcal{N}\setminus\{0\}$ is the same union with the origin deleted. Each line is one-dimensional, so the null cone has real dimension $1$; it is a cross of two lines through the origin, in contrast with the biquaternion null cone, which has real dimension $6$ inside dimension $8$.

**Proposition.** The null cone is **exactly** the zero-divisor set and is a union of two one-dimensional subspaces of the underlying real vector space.

**Proof.** The displayed factorisation gives $\mathcal{N} = \mathbb{R}\Pi_1\cup\mathbb{R}\Pi_2$; each line is one-dimensional over $\mathbb{R}$; and the two lines meet only at $0$, since $\Pi_1$ and $\Pi_2$ are linearly independent. The identification with the zero-divisor set is the theorem above.

Every point of $\mathcal{Z}$ lies on exactly one of the two lines, because the two lines meet only at the origin, which is not in $\mathcal{Z}$.

## The Two Families of Zero Divisors

The set $\mathcal{Z}$ decomposes into the two **families**

$$
\mathcal{Z}_+ = \mathbb{R}\Pi_1\setminus\{0\} = \{(t, t) : t \neq 0\}, \qquad \mathcal{Z}_- = \mathbb{R}\Pi_2\setminus\{0\} = \{(t, -t) : t \neq 0\},
$$

where a split-complex number is written as the pair $(a,a')$ of its coordinates in the basis $\{1, j\}$. These are the two lines with the origin removed; the origin splits each of them into its two sign classes, the points of parameter $t>0$ and the points of parameter $t<0$.

**Proposition.** The annihilator of a nonzero multiple of $\Pi_1$ is the opposite line, and symmetrically:

$$
\operatorname{ann}(\lambda \Pi_1) = \mathbb{R}\Pi_2, \qquad \operatorname{ann}(\lambda \Pi_2) = \mathbb{R}\Pi_1, \qquad \lambda \neq 0.
$$

**Proof.** Write $A = \lambda \Pi_1$ and $B = B_+\Pi_1 + B_-\Pi_2$. Then $AB = \lambda B_+ \Pi_1$, which vanishes iff $B_+ = 0$, i.e. $B \in \mathbb{R}\Pi_2$. The other case is symmetric.

So the two families annihilate one another: each null line is the annihilator of the other. The two families are exchanged by the conjugation, $\overline{\Pi_1} = \Pi_2$, and they are the two minimal ideals of *Split-Complex Ideals and Peirce Decomposition* with the origin removed.

The zero divisors of the two families are, up to a real scale, the two **primitive** zero divisors $\Pi_1$ and $\Pi_2$:

$$
\mathcal{Z} = \mathbb{R}^\times \Pi_1 \;\cup\; \mathbb{R}^\times \Pi_2.
$$

There is no third family and no interior; the zero-divisor set consists of two lines only.

## The Distribution of the Zero Divisors

A zero divisor is an element on which the product $A_+A_-$ of the idempotent coordinates vanishes, so which subsets of $\mathbb{D}$ contain zero divisors is the algebraic question of where that product vanishes. The real subspace $\mathbb{R}_{\mathbb{D}}$ and the split imaginary line $j\mathbb{R}_{\mathbb{D}}$ contain no zero divisor other than $0$: on the first the product is $a^2$ and on the second it is $-a'^2$, and each vanishes only at the origin. The two null lines $\mathbb{R}\Pi_1$ and $\mathbb{R}\Pi_2$ consist of $0$ together with the zero divisors, and on each the product is identically zero.

Off the null cone both coordinates are non-zero, and the pair of signs $(\operatorname{sgn} A_+, \operatorname{sgn} A_-)$ separates the complement into four **sign classes**:

$$
\{A_+ > 0, A_- > 0\}, \quad \{A_+ > 0, A_- < 0\}, \quad \{A_+ < 0, A_- > 0\}, \quad \{A_+ < 0, A_- < 0\},
$$

on which $A_+A_-$ takes the constant values $+,-,-,+$. A zero divisor is reached from either of the two neighbouring sign classes by forcing one coordinate to vanish, and the sign of that coordinate changes as it passes through zero, so the null cone is exactly the set across which the sign of $A_+A_-$ changes, and it carries no interior in the classification by that sign.

The finer description — the sign of $A_+A_-$ read as the indefiniteness of a form, the two spacelike and the two timelike regions, and the components of the group of units — reads a form as a form and is in *Split-Complex Norm and Invertibility*, §*Distribution of the Invertible Elements*.

## The Relation to the Idempotents

The zero divisors are exactly the elements supported on a single idempotent. In the idempotent basis,

$$
A = A_+\Pi_1 + A_-\Pi_2,
$$

so $A_+A_-$ is the product of the two coordinates, and $A$ is a zero divisor iff one of $A_+, A_-$ is zero and the other is not. So

$$
\mathcal{Z} = \{A : A_+ = 0, A_- \neq 0\} \cup \{A : A_- = 0, A_+ \neq 0\},
$$

and the two families are the two coordinate lines $\mathbb{R}\Pi_\pm$, with the origin removed. The primitive zero divisors $\Pi_\pm$ are the idempotents themselves; every other zero divisor is a real multiple of one of them. Because the idempotents are central, there is no distinction between a left and a right annihilator and no phenomenon of one-sided invertibility: an element is a zero divisor iff it is a non-unit, iff it annihilates a whole line, namely the opposite one.

## Comparison with the Complex, Biquaternion and Split-Biquaternion Cases

| algebra | zero-divisor set | real dimension | reason |
|---|---|---|---|
| $\mathbb{C}$ | empty | $0$ | $\mathbb{C}$ is a field |
| $\mathbb{D}$ | $\mathbb{R}\Pi_1\cup\mathbb{R}\Pi_2$ | $1$ | $\mathbb{D}\cong\mathbb{R}\oplus\mathbb{R}$ is not a field |
| $\mathbb{B}$ | null cone $\{N=0\}$ | $6$ | $\mathbb{B}\cong M_2(\mathbb{C})$ is not a division algebra |
| $\mathbb{H}_{\mathbb{D}}$ | $(\mathbb{H}\times\{0\})\cup(\{0\}\times\mathbb{H})$ | $4$ | $\mathbb{H}$ is a division algebra |

The complex field has no zero divisors at all. The split-complex algebra has a one-dimensional zero-divisor set, the simplest nontrivial one. The biquaternion algebra has a six-real-dimensional null cone, the subject of *Biquaternion Zero Divisors*. The split-biquaternion algebra $\mathbb{H}_{\mathbb{D}}\cong\mathbb{H}\oplus\mathbb{H}$ has a four-real-dimensional set, the union of a plane and its complementary plane in the product of two quaternion algebras, since the quaternions themselves have no zero divisors. The split-complex case is thus the minimal instance of the phenomenon: the smallest algebra in the family that is not a division algebra, with the zero-divisor set a pair of lines.

## Summary

A non-zero split-complex number $A$ is a zero divisor exactly when $a^2 = a'^2$, equivalently when one of its idempotent coordinates vanishes. The zero-divisor set is the null cone with the origin removed, the union of the two null lines $\mathbb{R}\Pi_1$ and $\mathbb{R}\Pi_2$, a one-dimensional cross through the origin, with each line the annihilator of the other.

The null cone is the zero set of the quadratic form of *Split-Complex Norm and Invertibility*, its isotropic cone; the form theory that reads it as a form — its polarisation, its signature, its hyperbolic pair of lines and the spacelike and timelike regions — is developed there and is named only here. The two families of zero divisors are the two coordinate lines of the idempotent decomposition, and up to scale they consist of the two primitive zero divisors $\Pi_1$ and $\Pi_2$; the sign of the product $A_+A_-$ separates the complement of the null cone into four sign classes, and the zero divisors are the elements across which that sign changes. Compared with the complex field, which has no zero divisors, with the biquaternion algebra, whose null cone has real dimension $6$, and with the split-biquaternion algebra, whose zero divisors form two copies of $\mathbb{H}$, the split-complex case is the minimal example in the family that is not a division algebra: a pair of lines.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | Split complex algebra |
| $A = a + j a'$ | General split complex number |
| $A_\pm = a\pm a'$ | Idempotent coordinates, $A = A_+\Pi_1 + A_-\Pi_2$ |
| $\mathcal{N} = \{a^2 = a'^2\}$ | Null cone |
| $\mathcal{Z} = \mathcal{N}\setminus\{0\}$ | Zero-divisor set |
| $\mathcal{Z}_\pm = \mathbb{R}\Pi_\pm\setminus\{0\}$ | The two families of zero divisors |
| $\Pi_\pm = \tfrac12(1\pm j)$ | Idempotents, the primitive zero divisors |
| $\overline{A} = a - j a'$ | Conjugation, exchanging the two families |
| $\operatorname{ann}(A)$ | Annihilator; $\operatorname{ann}(\lambda \Pi_1) = \mathbb{R}\Pi_2$ |
| $\mathbb{R}\Pi_1$, $\mathbb{R}\Pi_2$ | The two null lines, which are the two minimal ideals |
| $A_+A_-$ | Product of the idempotent coordinates, vanishing on the zero divisors; its sign classes the complement |

## Further Reading

- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, Graduate Texts in Mathematics 131, 2nd ed. 2001), for zero divisors, annihilators and the theory of non-units.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for zero divisors across the real division and non-division algebras.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for isotropic cones and the split complex algebra in the Clifford setting.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for isotropic vectors and the isotropic cone of an indefinite quadratic form.
- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the geometric reading of the split complex plane and its null directions.
