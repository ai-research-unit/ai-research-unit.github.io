
# __Split-Complex Two-Component Element Representation__

## Introduction

The split-complex algebra $\mathbb{D}$ is two-dimensional over $\mathbb{R}$, so a split-complex number is read off as its list of **two real coefficients**, $A = a + j a' \leftrightarrow (a, a')$. This article presents that **two-component realization** in full: the coefficient space, the column and the dual row, the component form of the product, the conjugation in coordinates, the two fixed-point subspaces as coordinate conditions, and the norm with its two signs. It is the two-dimensional counterpart of *Biquaternion Four-Vector Element Representation*, and it is the last of the three Representation articles, after *Split-Complex Element Representations* and *Split-Complex Regular Element Representation*.

The word *representation* is used here in the sense of a concrete realization of the algebra as computable objects, not in the technical sense of a vector space carrying an algebra homomorphism into its endomorphisms. The technical sense is the subject of *Split-Complex Element Representations*, and the matrix of the action on this coefficient space is the subject of *Split-Complex Regular Element Representation*; this article supplies the coordinate space on which that operator is written.

The article owns the coefficient space $\mathbb{R}^2$, the column and the row, the component form of the product, the conjugation in coordinates, the two fixed-point subspaces and the norm with its two real restrictions. It does not treat the matrix of multiplication on this space, which belongs to *Split-Complex Regular Element Representation*; it does not treat the polar forms, which belong to *Split-Complex Polar Element Representation*; and it introduces no physical vocabulary. The comparison throughout is with the complex field, whose two-component realization is the **definite** one and whose product rule differs from the present one in a single sign.

**Conventions.** The algebra is $\mathbb{D} = \mathbb{R}[x]/(x^2-1)$, basis $1$, $j$, $j^2 = +1$; general element $A = a+j a'$ with $a = \operatorname{Re}A$, $a' = \operatorname{Im}A$; conjugate $\bar A = a-j a'$; idempotents $\Pi_\pm = \tfrac12(1\pm j)$; idempotent coordinates $A_\pm = a\pm a'$; norm $N(A) = a^2-a'^2$.

## The Coefficient Space

**Definition.** The **two-component vector** of a split-complex number $A = a+j a'$ is the ordered pair

$$
A^\mu = (A^0, A^1), \qquad A^0 = a, \quad A^1 = a'.
$$

The coefficient of the unit is written $A^0$ and the coefficient of $j$ is written $A^1$; the component $A^0$ is the **real component** and $A^1$ the **imaginary component**. These are the honest names, because they are the coefficients of the real and imaginary parts of $A$ and nothing else.

**Proposition.** The map $A \mapsto A^\mu$ is an $\mathbb{R}$-linear isomorphism from $\mathbb{D}$ onto $\mathbb{R}^2$. Consequently the coefficient space has real dimension $2$ and no other dimension: unlike a biquaternion, whose components are complex, a split-complex number is entirely real, so its coefficient space is $\mathbb{R}^2$ and there is no splitting of each coordinate into real and imaginary parts.

**Proof.** The map sends the basis $1, j$ to the standard basis of $\mathbb{R}^2$ and is extended by linearity; it is bijective on bases. The algebra is a real vector space of dimension $2$, matched by the dimension of $\mathbb{R}^2$.

The coefficient space $\mathbb{R}^2$ **is** the algebra itself, seen as a coordinate space, and it is also the simple module of $\mathbb{D}$: the algebra is two-dimensional, its two idempotent components are one-dimensional, and the regular module is the direct sum of the two one-dimensional simple modules. So the numbers $2$, $2$, $2$ appearing as the dimension of the algebra, the size of the regular matrix of *Split-Complex Regular Element Representation*, and the dimension of the coefficient space are the same number for the same reason, in contrast with the biquaternion case where the algebra dimension $4$ and the simple-module dimension $2$ are different objects.

### Coordinates in the Idempotent Basis

The coefficient pair $(a, a')$ in the basis $\{1, j\}$ and the idempotent pair $(A_+, A_-)$ in the basis $\{\Pi_1, \Pi_2\}$ are related by

$$
A_+ = a+a', \qquad A_- = a-a', \qquad a = \tfrac12(A_+ + A_-), \qquad a' = \tfrac12(A_+ - A_-),
$$

the change of coordinates of the plane. The pair $(A_+, A_-)$ is the pair of **eigen-coordinates** of the conjugation, since the regular representation is diagonal in that basis, and it is also the pair that makes the multiplication componentwise.

## The Column and the Row

**Definition.** The **column** of $A$ is the $2\times 1$ matrix

$$
A = \begin{pmatrix} a \\ a' \end{pmatrix},
$$

the transpose of the two-component vector. The **row** of $A$ is the $1\times 2$ matrix

$$
A^{\mathsf{T}} = \begin{pmatrix} a & a' \end{pmatrix}.
$$

The column is the transcribed form of the same object, and it is convenient because the product of split-complex numbers is bilinear. For a fixed $A$, the map $B \mapsto AB$ sends coordinates linearly to coordinates, so it is an $\mathbb{R}$-linear endomorphism of the coefficient space, and with the column convention it is written as a $2\times2$ matrix acting on the column of $B$:

$$
AB \longleftrightarrow \operatorname{mat}_4(A)\, B, \qquad \operatorname{mat}_4(A) = \begin{pmatrix} a & a' \\ a' & a \end{pmatrix}.
$$

The matrix $\operatorname{mat}_4(A)$ is constructed and verified in *Split-Complex Regular Element Representation*; the present article records only that the product rule admits this reading. The **component form** is the same statement written out:

$$
AB = (a b + a' b') + (a b' + a' b) j, \qquad B = b+j b',
$$

so the two components of the product are the two entries of the matrix product $\operatorname{mat}_4(A)B$.

**Remark (the row is the dual).** The row $A^{\mathsf{T}}$ is the element of the dual space $\operatorname{Hom}_{\mathbb{R}}(\mathbb{D}, \mathbb{R})$ associated with $A$ by the standard pairing $\langle A^{\mathsf{T}}, B\rangle = a b + a' b'$, and it is **not** a further realization of the algebra. The dual of a left module is a right module, carrying the *right* action $(\varphi\cdot A)(B) = \varphi(AB)$. Because $\mathbb{D}$ is commutative, the right action is the action of the same element, and the row picture and the column picture are interchanged by transposition without a conjugate: the transpose of $\operatorname{mat}_4(A)$ is $\operatorname{mat}_4(A)$ itself, since the regular matrix is symmetric. This is the degeneration of the biquaternion transposition identity, where the transpose of the left matrix is the left matrix of the conjugate.

## Multiplication in Two-Component Form

**Proposition (the product in components).** Let $A, B$ have two-component vectors $(a, a')$ and $(b, b')$. Then the two-component vector of the product has components

$$
(AB)^0 = a b + a' b', \qquad (AB)^1 = a b' + a' b.
$$

**Proof.** Expand $AB = (a+j a')(b+j b') = a b + a b' j + a' b j + a' b' j^2$ and use $j^2 = +1$ to collect the terms:

$$
AB = (a b + a' b') 1 + (a b' + a' b) j,
$$

which is the displayed pair.

**Comparison with the complex case.** For the complex number $A = a+i a'$ with the complex unit $i^2 = -1$, the product with $B = b+i b'$ has components

$$
(AB)^0 = a b - a' b', \qquad (AB)^1 = a b' + a' b.
$$

The two product rules differ **only** in the sign of the $a' b'$ term in the first component: the split-complex product adds $a' b'$, the complex product subtracts it. This single sign is the whole difference between the two algebras at the level of components, and it is the reason the split-complex norm is indefinite while the complex one is definite.

| product rule | first component | second component |
|---|---|---|
| complex ($i^2 = -1$) | $a b - a' b'$ | $a b' + a' b$ |
| split-complex ($j^2 = +1$) | $a b + a' b'$ | $a b' + a' b$ |

### The Multiplication Table of the Basis

The component rule is the developed form of the two products

$$
1 = 1, \qquad j = j, \qquad j = j, \qquad j j = +1,
$$

which may be tabulated:

| $\cdot$ | $1$ | $j$ |
|---|---|---|
| $1$ | $1$ | $j$ |
| $j$ | $j$ | $+1$ |

The table is the group table of $\mathbb{Z}/2$ with $j$ playing the non-identity element, and the algebra is the group ring $\mathbb{R}[\mathbb{Z}/2]$.

## The Conjugation in Coordinates

For $A = a+j a'$ the conjugation is $\bar A = a-j a'$, so in coordinates

$$
\overline{(a, a')} = (a, -a'),
$$

and in the idempotent coordinates

$$
\overline{(A_+, A_-)} = (A_-, A_+),
$$

because $\bar A = a-j a' = A_- \Pi_1 + A_+ \Pi_2$. So the conjugation reflects the coefficient plane across the real axis and swaps the two idempotent coordinates. It is $\mathbb{R}$-linear, of order two, and its matrix in the basis $\{1, j\}$ is

$$
C = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix},
$$

a diagonal reflection; in the idempotent basis $\{\Pi_1, \Pi_2\}$ its matrix is $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, the swap. In the complex case the matrix is the same $C$; the difference is not in the conjugation but in the product, and it is the product that makes the conjugation a **ring** involution here as there.

## The Two Fixed-Point Subspaces

The conjugation splits the coefficient space into its fixed and anti-fixed subspaces.

**Fixed subspace.** The condition $(a,-a') = (a,a')$ gives $a' = 0$, so

$$
\mathbb{R}_{\mathbb{D}} = \{(a, 0)\},
$$

the real axis, of real dimension $1$. It is the set of real components.

**Anti-fixed subspace.** The condition $(a,-a') = (-a,-a')$ gives $a = 0$, so

$$
j\mathbb{R}_{\mathbb{D}} = \{(0, a')\},
$$

the split imaginary axis, of real dimension $1$. Its elements are the pure imaginary components.

So $\mathbb{D} = \mathbb{R}_{\mathbb{D}}\oplus j\mathbb{R}_{\mathbb{D}}$ as a direct sum of coordinate axes, and each coordinate $a, a'$ is the projection onto the corresponding axis:

$$
a = \tfrac12(A + \bar A), \qquad a' = \tfrac12 j^{-1}(A - \bar A).
$$

In the idempotent basis the same two lines appear as the diagonals $(t,t)$ and $(t,-t)$, and it is those two lines, rather than the coordinate axes, that carry the multiplicative structure: the coordinate axes carry the definite norm, the diagonals the isotropic one.

## The Norm with Its Two Signs

The norm of $A = a+j a'$ in coordinates is

$$
N(A) = A\bar A = a^2 - a'^2,
$$

the difference of the two squares of the coordinates. Its polarisation is the symmetric bilinear form

$$
g(A, B) = a b - a' b', \qquad A = (a,a'), \; B = (b,b'),
$$

with matrix $\operatorname{diag}(1, -1)$ and signature $(1,1)$. So the coefficient space is a **Lorentzian plane**: the form is indefinite, of the two signs, and its isotropic set is the pair of diagonal lines $a = \pm a'$.

| region | coordinate condition | sign of $N$ |
|---|---|---|
| spacelike | $\lvert a\rvert > \lvert a'\rvert$ | $+$ |
| null | $\lvert a\rvert = \lvert a'\rvert$ | $0$ |
| timelike | $\lvert a\rvert < \lvert a'\rvert$ | $-$ |

### The Two Real Restrictions

Restricted to the two fixed-point subspaces the norm is definite:

$$
N\big|_{\mathbb{R}_{\mathbb{D}}}(a) = a^2 \quad (\text{positive definite}), \qquad N\big|_{j\mathbb{R}_{\mathbb{D}}}(a') = -a'^2 \quad (\text{negative definite}),
$$

so the real axis is positive definite and the split imaginary axis negative definite. This is the coordinate statement, made in *Split-Complex Norm and Invertibility*, that the null cone meets each eigenspace only at the origin. In the idempotent coordinates the same form is the product $N = A_+A_-$, which vanishes exactly when one coordinate vanishes.

**Comparison with the complex case.** For $\mathbb{C}$ the norm is

$$
N_{\mathbb{C}}(A) = A\bar A = a^2 + a'^2,
$$

the **sum** of the two squares: positive definite, so the complex coefficient plane carries a Euclidean, not a Lorentzian, structure. It is again the single sign of the product rule that produces the difference: the square $i^2 = -1$ turns the $a'^2$ term of $a^2+a'^2$ into $-a'^2$ in the split case, and the definite form becomes the indefinite one.

## The Two-Component Opposite of the Complex Two-Component Element Representation

The complex field and the split-complex algebra are the two two-dimensional real algebras generated by an element of square $-1$ and $+1$ respectively, and their two-component realizations are parallel in every respect except the sign of the generator's square. The following table is the comparison in full.

| feature | $\mathbb{C}$ ($i^2 = -1$) | $\mathbb{D}$ ($j^2 = +1$) |
|---|---|---|
| coefficient space | $\mathbb{R}^2$, components $(a,a')$ | $\mathbb{R}^2$, components $(a,a')$ |
| product rule | $(a b-a' b', \, a b'+a' b)$ | $(a b+a' b', \, a b'+a' b)$ |
| conjugation in coordinates | $(a,-a')$ | $(a,-a')$ |
| fixed / anti-fixed subspaces | $\mathbb{R}$ and $i\mathbb{R}$ | $\mathbb{R}_{\mathbb{D}}$ and $j\mathbb{R}_{\mathbb{D}}$ |
| norm | $a^2+a'^2$, positive definite | $a^2-a'^2$, signature $(1,1)$ |
| isotropic set | $\{0\}$ | the two lines $a = \pm a'$ |
| zero divisors | none | the two idempotent lines |
| idempotents beyond $0,1$ | none | $\Pi_\pm$ |
| isomorphism | field $\mathbb{C}$ | ring $\mathbb{R}\oplus\mathbb{R}$ |

The two realizations share their coefficient space, their column and row, their product's second component, and their conjugation; they differ in the sign of the first component's $a' b'$ term, and that single difference turns a field into a ring with zero divisors and a Euclidean plane into a Lorentzian one. The split-complex algebra is thus the **indefinite two-component** algebra, the systematic opposite of the complex field, and the comparison table is the complete statement of the difference at the level of coordinates.

## Summary

A split-complex number $A = a+j a'$ is realized as its two-component vector $(a, a')$ in $\mathbb{R}^2$, with column $\begin{pmatrix} a \\ a' \end{pmatrix}$ and dual row $(a, a')$; the map to $\mathbb{R}^2$ is an isomorphism of real vector spaces, and the component space is the algebra itself as a coordinate space. The product in components is $(AB)^0 = a b+a' b'$, $(AB)^1 = a b'+a' b$, differing from the complex product rule in the single sign of the $a' b'$ term; the left multiplication operator is the regular matrix $\begin{pmatrix} a & a' \\ a' & a \end{pmatrix}$ of *Split-Complex Regular Element Representation*.

The conjugation is the reflection $(a,a') \mapsto (a,-a')$, with fixed subspace the real axis and anti-fixed subspace the split imaginary axis. The norm is $a^2-a'^2$, indefinite of signature $(1,1)$ with isotropic set the two lines $a = \pm a'$; restricted to the real axis it is positive definite and to the split imaginary axis negative definite. In the idempotent coordinates the same form is $A_+A_-$ and the conjugation swaps the two coordinates. The complex field shares the coefficient space, the conjugation, the column and row picture and the second component of the product, and differs only in the sign of the $a' b'$ term of the first component; that sign is the whole difference between the definite two-component algebra and the indefinite one, between a field and a ring with zero divisors.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | Split complex algebra |
| $A = a + j a'$ | General split complex number |
| $A^\mu = (A^0, A^1) = (a, a')$ | Two-component vector |
| $A^0 = a$, $A^1 = a'$ | Real and imaginary components |
| $A = \begin{pmatrix} a \\ a' \end{pmatrix}$, $A^{\mathsf{T}} = (a\ \ a')$ | Column and row |
| $\operatorname{mat}_4(A) = \begin{pmatrix} a & a' \\ a' & a \end{pmatrix}$ | Left multiplication matrix |
| $(AB)^0 = a b+a' b'$, $(AB)^1 = a b'+a' b$ | Component product rule |
| $\overline{(a,a')} = (a,-a')$ | Conjugation in coordinates |
| $C = \operatorname{diag}(1,-1)$ | Matrix of the conjugation |
| $\mathbb{R}_{\mathbb{D}} = \{(a,0)\}$ | Fixed subspace, real axis |
| $j\mathbb{R}_{\mathbb{D}} = \{(0,a')\}$ | Anti-fixed subspace, split imaginary axis |
| $N(A) = a^2-a'^2$ | Norm, signature $(1,1)$ |
| $g(A,B) = a b-a' b'$ | Polarised form |
| $(A_+, A_-) = (a+a', a-a')$ | Idempotent coordinates |

## Further Reading

- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the two-component and matrix readings of the split complex plane.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the parallel treatment of the two-dimensional real algebras.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the split complex numbers as $\mathrm{Cl}_{1,0}$ and their coordinate realization.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for signatures, isotropic vectors and the Lorentzian plane.
- Harvey Cohn, *A Classical Invitation to Algebraic Numbers and Class Fields* (Springer, Universitext, 1978), for the comparison of the two quadratic real algebras of dimension two.
