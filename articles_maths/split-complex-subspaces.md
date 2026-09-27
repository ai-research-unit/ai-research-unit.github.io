
# __Split-Complex Subspaces__

## Introduction

The distinguished subspaces of $\mathbb{D}$ are the fixed and anti-fixed spaces of the unique non-trivial involution, the real line $\mathbb{R}_{\mathbb{D}}$ and the split imaginary line $j\mathbb{R}_{\mathbb{D}}$, together with the two idempotent lines $\mathbb{R}\Pi_1$ and $\mathbb{R}\Pi_2$, which are the finest one-dimensional pieces of the algebra. This article collects their relations in one place: their bases, their dimensions, their intersections, their sums, the action of the involution on each, the restricted norm form, and the failure of the six-subspace lattice that the biquaternion category supports. It is the two-dimensional counterpart of *Biquaternion Relations Between Subspaces*, and the systematic difference is that the involution lattice degenerates to a single edge, so the number of distinguished one-dimensional subspaces is two rather than six.

The single non-trivial involution is the conjugation $\bar{\cdot}$: it is the only involution distinct from the identity, and the idempotent conjugation coincides with it. Each involution splits the algebra into a fixed space and an anti-fixed space, so there is one decomposition into two lines, namely the scalar–split-vector decomposition, and there is a second, finer decomposition, the idempotent one, not induced by an involution. Every number below is recomputed from the definitions by comparison of coefficients.

**Conventions.** The algebra is $\mathbb{D} = \mathbb{R}[x]/(x^2-1)$, with basis $1$, $j$, $j^2 = +1$; general element $Z = a+j b$; conjugate $\bar Z = a-j b$; idempotents $\Pi_\pm = \tfrac12(1\pm j)$; idempotent coordinates $Z_\pm = a\pm b$; norm form $N(Z) = Z\bar Z = a^2-b^2$. The algebra is commutative, so there is no quaternion conjugation and no Hermitian decomposition; those slots of the four-dimensional case are empty here.

## The Two Involutions

The algebra carries two natural involutions: the split-complex conjugation $\bar{Z} = a-j b$ and the idempotent conjugation (the swap) $\tilde{Z} = (a-b)\Pi_1 + (a+b)\Pi_2$. Each is an $\mathbb{R}$-linear map of order two, and on $\mathbb{D}$ they coincide:

$$
\tilde Z = (a-b)\Pi_1 + (a+b)\Pi_2 = (a-b)\tfrac{1+j}{2} + (a+b)\tfrac{1-j}{2} = a - j b = \bar Z.
$$

So there is one involution worth naming, the conjugation $\bar{\cdot}$, and the map sending an element to its "conjugate with respect to the idempotent basis" produces no second structure. In the four-dimensional algebra the corresponding statements are different: $\mathbb{B}$ carries the four involutions $\bar{\cdot}, {}^{*}, {}^{\dagger}, \flat$, they are pairwise distinct, and they generate six subspaces. Here the whole involution content is a single non-trivial map.

## The Distinguished Subspaces at a Glance

The involution $\bar{\cdot}$ splits $\mathbb{D}$ into its fixed line and its anti-fixed line, and the idempotent basis adds the two finer lines.

| subspace | defining condition | real basis | $\dim_{\mathbb{R}}$ | subalgebra? | restricted $N$ |
|---|---|---|---|---|---|
| $\mathbb{R}_{\mathbb{D}}$ | $\bar Z = Z$ | $1$ | $1$ | yes, $\cong\mathbb{R}$ | $a^2$, positive definite |
| $j\mathbb{R}_{\mathbb{D}}$ | $\bar Z = -Z$ | $j$ | $1$ | no | $-b^2$, negative definite |
| $\mathbb{R}\Pi_1$ | $Z_- = 0$ | $\Pi_1$ | $1$ | ideal, $\cong\mathbb{R}$ | $0$ |
| $\mathbb{R}\Pi_2$ | $Z_+ = 0$ | $\Pi_2$ | $1$ | ideal, $\cong\mathbb{R}$ | $0$ |

Two of these are the members of a decomposition induced by the involution, and two are the members of the idempotent decomposition. The first pair is a decomposition into complementary eigenspaces; the second pair is a decomposition into complementary ideals.

## The Decompositions

The involution gives the **scalar–split-vector decomposition**

$$
\mathbb{D} = \mathbb{R}_{\mathbb{D}} \oplus j\mathbb{R}_{\mathbb{D}}, \qquad Z = Z_r + j Z_i, \qquad Z_r = \tfrac12(Z+\bar Z), \quad Z_i = \tfrac12 j^{-1}(Z-\bar Z) = b,
$$

and the idempotent basis gives the **idempotent decomposition**

$$
\mathbb{D} = \mathbb{R}\Pi_1 \oplus \mathbb{R}\Pi_2, \qquad Z = Z_+\Pi_1 + Z_-\Pi_2, \qquad Z_\pm = Z\Pi_\pm = a\pm b.
$$

The two decompositions are related by the coefficient change-of-basis in the plane $\mathbb{D}\cong\mathbb{R}^2$:

$$
Z_+ = Z_r + Z_i, \qquad Z_- = Z_r - Z_i,
$$

so the change from the eigenbasis $\{1, j\}$ of the involution to the idempotent basis $\{\Pi_1, \Pi_2\}$ is the linear map

$$
\begin{pmatrix} Z_+ \\ Z_- \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} Z_r \\ Z_i \end{pmatrix}.
$$

In the four-dimensional algebra there are three such decompositions, the scalar–vector, the quaternion and the Hermitian; here there are two, and only the first is induced by an involution.

## The Four Coordinate Lines

The two real coordinates of $\mathbb{D}$ are $(a,b)$, in the basis $\{1,j\}$. They group into the two lines

$$
\langle\rangle = \{(a,0)\}, \qquad \langle j\rangle = \{(0,b)\},
$$

the real and split imaginary coordinate lines. In the idempotent basis the same plane is grouped into the two lines

$$
\langle \Pi_1\rangle = \{(t,t)\}, \qquad \langle \Pi_2\rangle = \{(t,-t)\},
$$

the two diagonal directions. The four lines are pairwise distinct: the coordinate lines have slopes $0$ and $\infty$, the idempotent lines have slopes $+1$ and $-1$, and no two of them coincide. Every one of the four is a real line through the origin, and each of the two decompositions selects one pair.

| line | basis | coordinates | slope |
|---|---|---|---|
| real line | $1$ | $b = 0$ | $0$ |
| split imaginary line | $j$ | $a = 0$ | $\infty$ |
| positive idempotent line | $\Pi_1$ | $a = b$ | $+1$ |
| negative idempotent line | $\Pi_2$ | $a = -b$ | $-1$ |

## The Intersections

With only four one-dimensional lines through the origin, the intersection table is immediate: distinct lines meet only at the origin, and each line meets itself in itself.

| | $\mathbb{R}_{\mathbb{D}}$ | $j\mathbb{R}_{\mathbb{D}}$ | $\mathbb{R}\Pi_1$ | $\mathbb{R}\Pi_2$ |
|---|---|---|---|---|
| $\mathbb{R}_{\mathbb{D}}$ | $1$ | $0$ | $0$ | $0$ |
| $j\mathbb{R}_{\mathbb{D}}$ | $0$ | $1$ | $0$ | $0$ |
| $\mathbb{R}\Pi_1$ | $0$ | $0$ | $1$ | $0$ |
| $\mathbb{R}\Pi_2$ | $0$ | $0$ | $0$ | $1$ |

So all four lines are pairwise independent: no two distinct lines of the list coincide, and no line is contained in another. This is a sharper statement than in the four-dimensional case, where different subspaces may meet in a nonzero block; here every off-diagonal entry is $0$, because there is no room for a proper subspace of a line.

Two features are worth isolating:

- the members of the scalar–split-vector decomposition meet only at $0$, the entries of the first $2\times2$ block;
- the members of the idempotent decomposition meet only at $0$, the entries of the last $2\times2$ block.

## The Sums

Every pair of distinct lines spans a plane, and every pair with a repeated line has the dimension of that line.

| | $\mathbb{R}_{\mathbb{D}}$ | $j\mathbb{R}_{\mathbb{D}}$ | $\mathbb{R}\Pi_1$ | $\mathbb{R}\Pi_2$ |
|---|---|---|---|---|
| $\mathbb{R}_{\mathbb{D}}$ | $1$ | $2$ | $2$ | $2$ |
| $j\mathbb{R}_{\mathbb{D}}$ | $2$ | $1$ | $2$ | $2$ |
| $\mathbb{R}\Pi_1$ | $2$ | $2$ | $1$ | $2$ |
| $\mathbb{R}\Pi_2$ | $2$ | $2$ | $2$ | $1$ |

Every off-diagonal sum has dimension $2 = \dim\mathbb{D}$, so **every pair of distinct distinguished lines spans the whole algebra**. This is the statement that any two of the four lines are complementary direct summands, and it is the reason $\mathbb{D}$ carries two decompositions into pairs of the four lines:

$$
\mathbb{D} = \mathbb{R}_{\mathbb{D}} \oplus j\mathbb{R}_{\mathbb{D}} = \mathbb{R}\Pi_1 \oplus \mathbb{R}\Pi_2.
$$

In the four-dimensional case only the three decomposition pairs span the algebra; here all six pairs of distinct lines do, simply because there are only two dimensions to fill.

## The Failure of a Six-Subspace Lattice

The biquaternion category has six distinguished subspaces because it has three commuting involutions, each contributing a fixed and an anti-fixed space, and the four involutions $\{\mathrm{id}, \bar{\cdot}, {}^{*}, {}^{\dagger}\}$ form the Klein four-group. In $\mathbb{D}$ the conjugation group is

$$
\{\mathrm{id}, \bar{\cdot}\} \cong \mathbb{Z}/2,
$$

with a single non-trivial element, so the involution lattice is the single edge $\{0\}\subset\mathbb{Z}/2$ drawn on the two lines $\mathbb{R}_{\mathbb{D}}$ and $j\mathbb{R}_{\mathbb{D}}$. A six-subspace lattice of the biquaternion kind would require three independent involutions and their products; there is only one, and the idempotent conjugation does not add a second, since it equals the first.

There is, of course, a finer decomposition of the plane into the two idempotent lines, and in that sense one may say the plane carries four distinguished lines rather than two. But the four do not form a lattice under intersection and sum in the way the six biquaternion subspaces do: they form the two bases of the two decompositions, with all cross-intersections zero and all cross-sums equal to the whole plane. The honest statement is that the involution lattice of $\mathbb{D}$ is the two-element chain of the single involution, and the idempotent lines are a second, non-involution decomposition.

## The Action of the Involution

The conjugation $\bar{\cdot}$ preserves each of the four lines, acting on each by a scalar sign:

| line | $\bar{\cdot}$ action | eigenvalue |
|---|---|---|
| $\mathbb{R}_{\mathbb{D}}$ | $\bar Z = Z$ | $+1$ |
| $j\mathbb{R}_{\mathbb{D}}$ | $\bar Z = -Z$ | $-1$ |
| $\mathbb{R}\Pi_1$ | $\overline{\lambda \Pi_1} = \lambda \Pi_2$ | swaps with $\mathbb{R}\Pi_2$ |
| $\mathbb{R}\Pi_2$ | $\overline{\lambda \Pi_2} = \lambda \Pi_1$ | swaps with $\mathbb{R}\Pi_1$ |

The first two lines are the eigenspaces of the involution, and the last two are exchanged by it:

$$
\bar \Pi_1 = \tfrac12(1-j) = \Pi_2, \qquad \bar \Pi_2 = \tfrac12(1+j) = \Pi_1.
$$

So the involution is diagonal on the eigenbasis and the swap on the idempotent basis. In the four-dimensional case the four involutions act on the six subspaces with mixed signs; here a single involution acts with the two signs on its own eigenspaces, and interchanges the two idempotent lines. The action table is the whole of the involution information, and it is consistent with the earlier statement $\tilde Z = \bar Z$: the idempotent swap is neither more nor less than the conjugation.

## The Norm Form on Each Line

The restricted norm form is definite on the two eigenlines and identically zero on the two idempotent lines:

| line | restricted $N$ | signature | zero divisors on the line |
|---|---|---|---|
| $\mathbb{R}_{\mathbb{D}}$ | $N(a) = a^2$ | positive definite | none |
| $j\mathbb{R}_{\mathbb{D}}$ | $N(j b) = -b^2$ | negative definite | none |
| $\mathbb{R}\Pi_1$ | $N(\lambda \Pi_1) = 0$ | zero | all nonzero elements |
| $\mathbb{R}\Pi_2$ | $N(\lambda \Pi_2) = 0$ | zero | all nonzero elements |

The two eigenlines are the definite lines of the form; the two idempotent lines are the isotropic lines. This is the plane-level version of the statement, made in *Split-Complex Zero Divisors*, that the null cone is exactly the union of the two idempotent lines, and of the statement, made in *Split-Complex Norm and Invertibility*, that the null cone meets each eigenspace only at the origin.

## Comparison with the Two Subspaces of $\mathbb{C}$

The complex field $\mathbb{C}$ is the definite two-dimensional algebra, and its subspace theory is the simplest of all: conjugation $Z \mapsto \bar Z$ is the unique non-trivial involution, with fixed space the real line and anti-fixed space the pure imaginary line, and there are

$$
\mathbb{C} = \mathbb{R}_{\mathbb{C}} \oplus i\mathbb{R}_{\mathbb{C}},
\qquad
\mathbb{R}_{\mathbb{C}} = \{a\}, \quad i\mathbb{R}_{\mathbb{C}} = \{ib\},
$$

exactly two distinguished subspaces, both of dimension $1$. The difference from $\mathbb{D}$ is that the norm form on $i\mathbb{R}_{\mathbb{C}}$ is $N(ib) = b^2$, **positive definite**, whereas on $j\mathbb{R}_{\mathbb{D}}$ it is $-b^2$; and that $\mathbb{C}$ has no idempotent decomposition, because $\mathbb{C}$ has no idempotents other than $0$ and $1$ (the equation $\zeta^2 = \zeta$ in a field forces $\zeta = 0$ or $1$). So the split-complex algebra has the same two involutive lines as $\mathbb{C}$ but with the sign of the imaginary line reversed, and it has in addition the two idempotent lines, which the field does not possess. This is the precise way in which the subspace theory of $\mathbb{D}$ is the indefinite enrichment of the subspace theory of $\mathbb{C}$.

| feature | $\mathbb{C}$ | $\mathbb{D}$ |
|---|---|---|
| non-trivial involutions | $1$ | $1$ |
| involutive lines | $\mathbb{R}_{\mathbb{C}}$, $i\mathbb{R}_{\mathbb{C}}$ | $\mathbb{R}_{\mathbb{D}}$, $j\mathbb{R}_{\mathbb{D}}$ |
| norm on the anti-fixed line | $+b^2$ (definite) | $-b^2$ (definite) |
| idempotents beyond $0,1$ | none | $\Pi_1, \Pi_2$ |
| idempotent lines | none | $\mathbb{R}\Pi_1$, $\mathbb{R}\Pi_2$ |
| isotropic lines | none | both idempotent lines |

## Worked Verifications

### An Element in All Four Lines

Take $Z = 4+3j$. Its eigenline coordinates are

$$
Z_r = \tfrac12(Z+\bar Z) = 4, \qquad Z_i = \tfrac12 j^{-1}(Z-\bar Z) = 3,
$$

so $Z$ lies in the plane spanned by the two eigenlines with both coordinates nonzero. Its idempotent coordinates are

$$
Z_+ = a+b = 7, \qquad Z_- = a-b = 1,
$$

both nonzero, so $Z$ is a unit; and $Z = 4 + 3 j = 7\Pi_1 + 1\Pi_2$, an identity checked directly in the two bases.

### A Pair of Lines That Spans the Plane

The lines $\mathbb{R}_{\mathbb{D}}$ and $\mathbb{R}\Pi_1$ have intersection $0$ and dimensions $1+1=2$, so they span the plane; decomposing $Z = j b$ along them,

$$
j b = -b + 2b \Pi_1,
$$

since $2\Pi_1 = 1 + j$. The coefficients are unique because the intersection is the origin, which is the content of the sum table.

### The Involution on Both Bases

For $Z = 4+3j$ the involution gives $\bar Z = 4-3j$; in the eigenbasis this flips the sign of the second coordinate, and in the idempotent basis it swaps the coordinates $7 \leftrightarrow 1$, since $Z = 7\Pi_1 + 1\Pi_2$ and $\bar Z = 1\Pi_1 + 7\Pi_2$. Both readings agree, and the arithmetic is the statement $\bar Z = 7\Pi_2 + 1\Pi_1$.

## Summary

The split-complex algebra has one non-trivial involution, the conjugation $\bar Z = a-j b$, which coincides with the idempotent conjugation, against the four involutions of the biquaternion algebra. It defines the real line $\mathbb{R}_{\mathbb{D}}$ and the split imaginary line $j\mathbb{R}_{\mathbb{D}}$, its fixed and anti-fixed spaces, and the plane splits as their direct sum; the idempotent basis defines the two finer lines $\mathbb{R}\Pi_1$ and $\mathbb{R}\Pi_2$, and the plane splits as their direct sum as well. The four lines are pairwise independent, every pair of distinct lines spans the whole plane, and the restricted norm form is definite on the two eigenlines and identically zero on the two idempotent lines, which are exactly the isotropic lines.

There is no six-subspace lattice of the biquaternion kind, because there is only one non-trivial involution; the involution lattice is the single edge $\{0\}\subset\mathbb{Z}/2$ on the two eigenlines, and the idempotent lines form a second, non-involution decomposition. Compared with $\mathbb{C}$, the split-complex algebra has the same two involutive lines but with the imaginary line's norm form reversed in sign, and it has in addition the two idempotent lines, which the field lacks because it has no nontrivial idempotents.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | Split complex algebra |
| $Z = a + j b$ | General split complex number |
| $\bar{Z} = a - j b$ | The unique non-trivial involution |
| $\tilde{Z} = \bar{Z}$ | Idempotent conjugation; equal to $\bar{Z}$ |
| $\mathbb{R}_{\mathbb{D}}$ | Real subspace, $+1$ eigenspace of $\bar{\cdot}$ |
| $j\mathbb{R}_{\mathbb{D}}$ | Split imaginary subspace, $-1$ eigenspace of $\bar{\cdot}$ |
| $\Pi_\pm = \tfrac12(1\pm j)$ | Idempotents, basis of the finer decomposition |
| $\mathbb{R}\Pi_1, \mathbb{R}\Pi_2$ | The two isotropic lines |
| $Z_r = a, Z_i = b$ | Eigenline coordinates |
| $Z_\pm = a\pm b$ | Idempotent coordinates |
| $N(Z) = a^2-b^2$ | Norm form, zero on the idempotent lines |
| $\langle\,\cdot\,\rangle$ | Real span of the listed elements |

## Further Reading

- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the scalar–vector and idempotent decompositions of the split complex plane.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the split complex algebra as the even Clifford algebra $\mathrm{Cl}_{1,0}$, with its two isotropic lines.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for isotropic lines, totally isotropic subspaces and signature in dimension two.
- Israel Nathan Herstein, *Topics in Algebra* (Wiley, 2nd ed. 1975), for involutions, eigenspaces and the elementary theory of decompositions.
- Harvey Cohn, *A Classical Invitation to Algebraic Numbers and Class Fields* (Springer, Universitext, 1978), for the arithmetic reading of the two-dimensional split algebra.
