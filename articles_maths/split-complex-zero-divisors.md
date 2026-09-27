
# __Split-Complex Zero Divisors__

## Introduction

A **zero divisor** in a commutative ring is a nonzero element $Z$ for which there is a nonzero element $W$ with $ZW = 0$. The split-complex algebra has a zero-divisor set of real dimension $1$, the pair of null lines, and this article determines it, describes its two families, relates it to the idempotents and to the isotropic cone of the norm form, and locates it as the boundary between the two regions of the norm form. It is the two-dimensional counterpart of *Biquaternion Zero Divisors*, where the null cone is a six-real-dimensional variety inside the eight-real-dimensional algebra.

**Placement.** The article is fifth in the Algebra group, after *Split-Complex Algebra*, *Split-Complex Norm and Invertibility*, *Split-Complex Idempotents and Projections* and *Split-Complex Ideals and Peirce Decomposition*, and before *Worked Examples in the Split-Complex Algebra*. It owns the classification of the null cone; the norm form and the invertibility criterion belong to the second article, the idempotents $\Pi_\pm$ and the decomposition $\mathbb{D}\cong\mathbb{R}\oplus\mathbb{R}$ to the third, and the minimal ideals to the fourth. This article is the boundary case: it classifies the null cone itself.

**Conventions.** The algebra is $\mathbb{D} = \mathbb{R}[x]/(x^2-1)$, basis $1$, $j$, $j^2 = +1$, general element $Z = a+j b$, conjugate $\bar Z = a-j b$, norm form $N(Z) = Z\bar Z = a^2-b^2$, idempotents $\Pi_\pm = \tfrac12(1\pm j)$, idempotent coordinates $Z = Z_+\Pi_1 + Z_-\Pi_2$ with $Z_\pm = a\pm b$. In this article $\mathcal{N} = \{Z : N(Z) = 0\}$ is the null cone and $\mathcal{Z} = \mathcal{N}\setminus\{0\}$ its set of nonzero points.

## The Zero Divisors of $\mathbb{D}$

**Definition.** An element $Z \in \mathbb{D}$ is a **zero divisor** if $Z \neq 0$ and there exists $W \in \mathbb{D}$ with $W \neq 0$ and $ZW = 0$. The **annihilator** of $Z$ is

$$
\operatorname{ann}(Z) = \{W \in \mathbb{D} : ZW = 0\},
$$

an ideal of $\mathbb{D}$.

**Theorem.** A nonzero element $Z \in \mathbb{D}$ is a zero divisor if and only if $N(Z) = 0$.

**Proof.** If $Z$ is a zero divisor, choose $W \neq 0$ with $ZW = 0$. In idempotent coordinates $ZW = Z_+W_+\Pi_1 + Z_-W_-\Pi_2$, so $ZW = 0$ iff $Z_+W_+ = 0$ and $Z_-W_- = 0$. Since $W \neq 0$, at least one of $W_+, W_-$ is nonzero; if $W_+ \neq 0$ then $Z_+W_+ = 0$ forces $Z_+ = 0$, and if $W_- \neq 0$ then $Z_-W_- = 0$ forces $Z_- = 0$; in either case $N(Z) = Z_+Z_- = 0$. Conversely, if $N(Z) = Z_+Z_- = 0$ with $Z \neq 0$, then one coordinate vanishes and the other does not; if $Z_+ = 0$ then $Z = Z_-\Pi_2 \neq 0$ and $Z \Pi_1 = Z_-\Pi_2\Pi_1 = 0$ with $\Pi_1 \neq 0$, so $Z$ is a zero divisor, and the case $Z_- = 0$ is symmetric. $\square$

So the zero-divisor set is exactly the nonzero part of the null cone:

$$
\mathcal{Z} = \{Z \neq 0 : N(Z) = 0\} = \{Z \neq 0 : a^2 = b^2\}.
$$

The criterion makes no reference to a choice of annihilator; it also shows that for $Z \neq 0$, being a zero divisor is equivalent to being a non-unit, since the units are exactly the elements with $N \neq 0$. Thus every nonzero non-unit of $\mathbb{D}$ is a zero divisor, a state of affairs impossible in a field. The non-units do not form an ideal: $\mathcal{N}$ is not closed under addition, since $\Pi_1 + \Pi_2 = 1$ is a unit, so $\mathbb{D}$ is not a local ring and has no unique maximal ideal of non-units.

## The Null Cone and the Two Null Lines

The equation $a^2 = b^2$ factors as

$$
(a-b)(a+b) = 0 \iff a = b \ \text{or}\ a = -b,
$$

so the null cone is the union of the two lines

$$
\mathbb{R}(1+j) = \mathbb{R}\Pi_1, \qquad \mathbb{R}(1-j) = \mathbb{R}\Pi_2,
$$

and $\mathcal{Z} = \mathcal{N}\setminus\{0\}$ is the same union with the origin deleted. Each line is one-dimensional, so the null cone has real dimension $1$; it is a cross of two lines through the origin, in contrast with the biquaternion null cone, which has real dimension $6$ inside dimension $8$.

**Proposition.** The null cone is **exactly** the zero-divisor set and is a union of two one-dimensional subspaces of the underlying real vector space.

**Proof.** The displayed factorisation gives $\mathcal{N} = \mathbb{R}\Pi_1\cup\mathbb{R}\Pi_2$; each line is one-dimensional over $\mathbb{R}$; and the two lines meet only at $0$, since $\Pi_1$ and $\Pi_2$ are linearly independent. The identification with the zero-divisor set is the theorem above. $\square$

Every point of $\mathcal{Z}$ lies on exactly one of the two lines, because the two lines meet only at the origin, which is not in $\mathcal{Z}$.

## The Two Families of Zero Divisors

The set $\mathcal{Z}$ decomposes into the two **families**

$$
\mathcal{Z}_+ = \mathbb{R}\Pi_1\setminus\{0\} = \{(t, t) : t \neq 0\}, \qquad \mathcal{Z}_- = \mathbb{R}\Pi_2\setminus\{0\} = \{(t, -t) : t \neq 0\},
$$

where a split-complex number is written as the pair $(a,b)$ of its coordinates in the basis $\{1, j\}$. These are the two open half-lines-with-sign, that is, the two lines with the origin removed; each has two connected components, a ray on each side of $0$.

**Proposition.** The annihilator of a nonzero multiple of $\Pi_1$ is the opposite line, and symmetrically:

$$
\operatorname{ann}(\lambda \Pi_1) = \mathbb{R}\Pi_2, \qquad \operatorname{ann}(\lambda \Pi_2) = \mathbb{R}\Pi_1, \qquad \lambda \neq 0.
$$

**Proof.** Write $Z = \lambda \Pi_1$ and $W = W_+\Pi_1 + W_-\Pi_2$. Then $ZW = \lambda W_+ \Pi_1$, which vanishes iff $W_+ = 0$, i.e. $W \in \mathbb{R}\Pi_2$. The other case is symmetric. $\square$

So the two families annihilate one another: each null line is the annihilator of the other. The two families are exchanged by the conjugation, $\overline{\Pi_1} = \Pi_2$, and they are the two minimal ideals of *Split-Complex Ideals and Peirce Decomposition* with the origin removed.

The zero divisors of the two families are, up to a real scale, the two **primitive** zero divisors $\Pi_1$ and $\Pi_2$:

$$
\mathcal{Z} = \mathbb{R}^\times \Pi_1 \;\cup\; \mathbb{R}^\times \Pi_2.
$$

There is no third family and no interior; the zero-divisor set consists of two lines only.

## The Distribution of the Zero Divisors

The norm form partitions the complement of the null cone into the two open regions

$$
\mathcal{S} = \{N(Z) > 0\} = \{|a| > |b|\}, \qquad \mathcal{T} = \{N(Z) < 0\} = \{|a| < |b|\},
$$

the spacelike and timelike regions. Each is a union of two connected sectors, so the complement of the null cone has four components in all. The two null lines are the common boundary:

| region | definition | sign of $N$ | number of components |
|---|---|---|---|
| spacelike | $\lvert a\rvert > \lvert b\rvert$ | $+$ | $2$ (sectors through $\pm1$) |
| null lines | $a = \pm b$ | $0$ | $2$ (the lines $\mathbb{R}\Pi_\pm$) |
| timelike | $\lvert a\rvert < \lvert b\rvert$ | $-$ | $2$ (sectors through $\pm j$) |

The null cone is precisely the boundary of each of the two open regions: every neighbourhood of a point of $\mathcal{Z}$ contains points of $\mathcal{S}$ and points of $\mathcal{T}$. The zero-divisor set therefore has empty interior and is a closed set of measure zero; the zero divisors are the "critical" elements across which the multiplicative geometry changes sign. This is the distribution statement for $\mathbb{D}$, against the biquaternion case in which the null cone has a rich stratification and non-pure zero divisors.

## The Relation to the Idempotents

The zero divisors are exactly the elements supported on a single idempotent. In the idempotent basis,

$$
Z = Z_+\Pi_1 + Z_-\Pi_2, \qquad N(Z) = Z_+Z_-,
$$

and $Z$ is a zero divisor iff one of $Z_+, Z_-$ is zero and the other is not. So

$$
\mathcal{Z} = \{Z : Z_+ = 0, Z_- \neq 0\} \cup \{Z : Z_- = 0, Z_+ \neq 0\},
$$

and the two families are the two coordinate lines $\mathbb{R}\Pi_\pm$, with the origin removed. The primitive zero divisors $\Pi_\pm$ are the idempotents themselves; every other zero divisor is a real multiple of one of them. Because the idempotents are central, there is no distinction between a left and a right annihilator and no phenomenon of one-sided invertibility: an element is a zero divisor iff it is a non-unit, iff it annihilates a whole line, namely the opposite one.

## The Relation to the Isotropic Cone of the Norm Form

The bilinear form polarising $N$ is

$$
g(Z, W) = \frac{1}{2}\big(N(Z+W)-N(Z)-N(W)\big) = a c - b d, \qquad Z = a+j b, \; W = c+j d,
$$

of signature $(1,1)$. The null cone is the **isotropic cone** of $g$: $N(Z) = g(Z,Z) = 0$. On each null line the form vanishes identically, since

$$
N(\lambda(1\pm j)) = \lambda^2(1-1) = 0,
$$

so each line is a **totally isotropic** subspace. The two isotropic lines are not orthogonal to one another under $g$:

$$
g(\Pi_1, \Pi_2) = \tfrac12\cdot\tfrac12 - \tfrac12\cdot\bigl(-\tfrac12\bigr) = \tfrac14 + \tfrac14 = \tfrac12 \neq 0.
$$

So the pair of isotropic lines is not an orthogonal pair; it is a hyperbolic (or Gauss) pair, and its existence is the geometric form of the signature $(1,1)$. A vector $W$ is $g$-orthogonal to $\Pi_1$ iff $W_- = 0$, i.e. iff $W \in \mathbb{R}\Pi_1$; each isotropic line is its own $g$-orthogonal companion, which is the definiteness failure in the language of bilinear forms.

## The Zero Divisor Set as the Boundary of the Two Norm Regions

On the open region $N > 0$ every element has the spacelike polar form

$$
Z = \rho(\cosh t + j\sinh t), \qquad \rho = \sqrt{N(Z)} > 0, \quad t \in \mathbb{R},
$$

and on the open region $N < 0$ the timelike polar form

$$
Z = \rho(\sinh t + j\cosh t), \qquad \rho = \sqrt{-N(Z)} > 0, \quad t \in \mathbb{R};
$$

the two are the two regimes of the polar decomposition. The zero-divisor set is the common boundary of the two regions:

- on the null lines the modulus $\rho = \sqrt{|N(Z)|}$ vanishes, so the polar factorisation degenerates: the "angle" parameter $t$ is not defined, and the element is not reachable by either polar form with a nonzero radius;
- the primitive zero divisors $\Pi_1$ and $\Pi_2$ are the limits of the spacelike unit hyperbola and of the timelike unit hyperbola; they are the asymptotic directions that both unit hyperbolas approach.

So the polar decomposition covers the complement of the two null lines, and the zero divisors are exactly its boundary. This is the two-dimensional analogue of the observation that the biquaternion polar decomposition is defined on the complement of the null cone, where the modulus is nonzero.

## Comparison with the Complex, Biquaternion and Split-Biquaternion Cases

| algebra | zero-divisor set | real dimension | reason |
|---|---|---|---|
| $\mathbb{C}$ | empty | $0$ | $\mathbb{C}$ is a field |
| $\mathbb{D}$ | $\mathbb{R}\Pi_1\cup\mathbb{R}\Pi_2$ | $1$ | norm form indefinite, splits into two lines |
| $\mathbb{B}$ | null cone $N=0$ | $6$ | complex-valued norm form on $\mathbb{C}^4$ |
| $\mathbb{H}_{\mathbb{D}}$ | $(\mathbb{H}\times\{0\})\cup(\{0\}\times\mathbb{H})$ | $4$ | $\mathbb{H}$ is a division algebra |

The complex field has no zero divisors at all. The split-complex algebra has a one-dimensional zero-divisor set, the simplest nontrivial one. The biquaternion algebra has a six-real-dimensional null cone, the subject of *Biquaternion Zero Divisors*. The split-biquaternion algebra $\mathbb{H}_{\mathbb{D}}\cong\mathbb{H}\oplus\mathbb{H}$ has a four-real-dimensional set, the union of a plane and its complementary plane in the product of two quaternion algebras, since the quaternions themselves have no zero divisors. The split-complex case is thus the minimal instance of the phenomenon: the smallest algebra in the family whose norm form is indefinite, with the zero divisor set a pair of lines.

## Summary

A nonzero split-complex number $Z$ is a zero divisor exactly when $N(Z) = 0$, equivalently when $a^2 = b^2$, equivalently when one of its idempotent coordinates vanishes. The zero-divisor set is the null cone with the origin removed, the union of the two null lines $\mathbb{R}\Pi_1$ and $\mathbb{R}\Pi_2$, a one-dimensional cross through the origin, with each line the annihilator of the other.

The null cone is the isotropic cone of the polarised form $g(Z,W) = a c-b d$ of signature $(1,1)$; each null line is totally isotropic, and the two lines form a non-orthogonal hyperbolic pair. The null lines are the boundary between the open regions $N>0$ and $N<0$; they are the boundary between the two regions, where the modulus $\rho = \sqrt{|N|}$ vanishes and neither polar factorisation is defined. The two families of zero divisors are the two coordinate lines of the idempotent decomposition, and up to scale they consist of the two primitive zero divisors $\Pi_1$ and $\Pi_2$. Compared with the complex field, which has no zero divisors, with the biquaternion algebra, whose null cone has real dimension $6$, and with the split-biquaternion algebra, whose zero divisors form two copies of $\mathbb{H}$, the split-complex case is the minimal indefinite example: a pair of lines.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | Split complex algebra |
| $Z = a + j b$ | General split complex number |
| $N(Z) = a^2 - b^2$ | Norm form |
| $g(Z,W) = a c - b d$ | Polarisation of $N$, signature $(1,1)$ |
| $\mathcal{N} = \{N = 0\}$ | Null cone |
| $\mathcal{Z} = \mathcal{N}\setminus\{0\}$ | Zero-divisor set |
| $\mathcal{Z}_\pm = \mathbb{R}\Pi_\pm\setminus\{0\}$ | The two families of zero divisors |
| $\Pi_\pm = \tfrac12(1\pm j)$ | Idempotents, the primitive zero divisors |
| $\overline{Z} = a - j b$ | Conjugation, exchanging the two families |
| $\operatorname{ann}(Z)$ | Annihilator; $\operatorname{ann}(\lambda \Pi_1) = \mathbb{R}\Pi_2$ |
| $\mathcal{S} = \{N>0\}$, $\mathcal{T} = \{N<0\}$ | Spacelike and timelike regions |
| $\rho = \sqrt{\lvert N(Z)\rvert}$ | Modulus, vanishing on $\mathcal{N}$ |

## Further Reading

- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, Graduate Texts in Mathematics 131, 2nd ed. 2001), for zero divisors, annihilators and the theory of non-units.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for zero divisors across the real division and non-division algebras.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for isotropic cones and the split complex algebra in the Clifford setting.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for isotropic vectors, totally isotropic subspaces and signatures.
- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the geometric reading of the two null lines and their role as the boundary of the two regions.
