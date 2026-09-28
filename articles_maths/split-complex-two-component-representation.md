
# __Split-Complex Two-Component Representation__

## Introduction

The split-complex algebra $\mathbb{D}$ is two-dimensional over $\mathbb{R}$, so a split-complex number is read off as its list of **two real coefficients**, $Z = a + j b \leftrightarrow (a, b)$. This article presents that **two-component realization** in full: the coefficient space, the column and the dual row, the component form of the product, the conjugation in coordinates, the two fixed-point subspaces as coordinate conditions, and the norm with its two signs. It is the two-dimensional counterpart of *Biquaternion Four-Vector Representation*, and it is the last of the three Representation articles, after *Split-Complex Representations* and *Split-Complex Regular Representation*.

The word *representation* is used here in the sense of a concrete realization of the algebra as computable objects, not in the technical sense of a vector space carrying an algebra homomorphism into its endomorphisms. The technical sense is the subject of *Split-Complex Representations*, and the matrix of the action on this coefficient space is the subject of *Split-Complex Regular Representation*; this article supplies the coordinate space on which that operator is written.

The article owns the coefficient space $\mathbb{R}^2$, the column and the row, the component form of the product, the conjugation in coordinates, the two fixed-point subspaces and the norm with its two real restrictions. It does not treat the matrix of multiplication on this space, which belongs to *Split-Complex Regular Representation*; it does not treat the polar forms, which belong to *Split-Complex Polar Representation*; and it introduces no physical vocabulary. The comparison throughout is with the complex field, whose two-component realization is the **definite** one and whose product rule differs from the present one in a single sign.

**Conventions.** The algebra is $\mathbb{D} = \mathbb{R}[x]/(x^2-1)$, basis $1$, $j$, $j^2 = +1$; general element $Z = a+j b$ with $a = \operatorname{Re}Z$, $b = \operatorname{Im}Z$; conjugate $\bar Z = a-j b$; idempotents $\Pi_\pm = \tfrac12(1\pm j)$; idempotent coordinates $Z_\pm = a\pm b$; norm $N(Z) = a^2-b^2$.

## The Coefficient Space

**Definition.** The **two-component vector** of a split-complex number $Z = a+j b$ is the ordered pair

$$
Z^\mu = (Z^0, Z^1), \qquad Z^0 = a, \quad Z^1 = b.
$$

The coefficient of the unit is written $Z^0$ and the coefficient of $j$ is written $Z^1$; the component $Z^0$ is the **real component** and $Z^1$ the **imaginary component**. These are the honest names, because they are the coefficients of the real and imaginary parts of $Z$ and nothing else.

**Proposition.** The map $Z \mapsto Z^\mu$ is an $\mathbb{R}$-linear isomorphism from $\mathbb{D}$ onto $\mathbb{R}^2$. Consequently the coefficient space has real dimension $2$ and no other dimension: unlike a biquaternion, whose components are complex, a split-complex number is entirely real, so its coefficient space is $\mathbb{R}^2$ and there is no splitting of each coordinate into real and imaginary parts.

**Proof.** The map sends the basis $1, j$ to the standard basis of $\mathbb{R}^2$ and is extended by linearity; it is bijective on bases. The algebra is a real vector space of dimension $2$, matched by the dimension of $\mathbb{R}^2$.

The coefficient space $\mathbb{R}^2$ **is** the algebra itself, seen as a coordinate space, and it is also the simple module of $\mathbb{D}$: the algebra is two-dimensional, its two idempotent components are one-dimensional, and the regular module is the direct sum of the two one-dimensional simple modules. So the numbers $2$, $2$, $2$ appearing as the dimension of the algebra, the size of the regular matrix of *Split-Complex Regular Representation*, and the dimension of the coefficient space are the same number for the same reason, in contrast with the biquaternion case where the algebra dimension $4$ and the simple-module dimension $2$ are different objects.

### Coordinates in the Idempotent Basis

The coefficient pair $(a, b)$ in the basis $\{1, j\}$ and the idempotent pair $(Z_+, Z_-)$ in the basis $\{\Pi_1, \Pi_2\}$ are related by

$$
Z_+ = a+b, \qquad Z_- = a-b, \qquad a = \tfrac12(Z_+ + Z_-), \qquad b = \tfrac12(Z_+ - Z_-),
$$

the change of coordinates of the plane. The pair $(Z_+, Z_-)$ is the pair of **eigen-coordinates** of the conjugation, since the regular representation is diagonal in that basis, and it is also the pair that makes the multiplication componentwise.

## The Column and the Row

**Definition.** The **column** of $Z$ is the $2\times 1$ matrix

$$
Z = \begin{pmatrix} a \\ b \end{pmatrix},
$$

the transpose of the two-component vector. The **row** of $Z$ is the $1\times 2$ matrix

$$
Z^{\mathsf{T}} = \begin{pmatrix} a & b \end{pmatrix}.
$$

The column is the transcribed form of the same object, and it is convenient because the product of split-complex numbers is bilinear. For a fixed $Z$, the map $W \mapsto ZW$ sends coordinates linearly to coordinates, so it is an $\mathbb{R}$-linear endomorphism of the coefficient space, and with the column convention it is written as a $2\times2$ matrix acting on the column of $W$:

$$
ZW \longleftrightarrow \rho_L(Z)\, W, \qquad \rho_L(Z) = \begin{pmatrix} a & b \\ b & a \end{pmatrix}.
$$

The matrix $\rho_L(Z)$ is constructed and verified in *Split-Complex Regular Representation*; the present article records only that the product rule admits this reading. The **component form** is the same statement written out:

$$
ZW = (a c + b d) + (a d + b c) j, \qquad W = c+j d,
$$

so the two components of the product are the two entries of the matrix product $\rho_L(Z)W$.

**Remark (the row is the dual).** The row $Z^{\mathsf{T}}$ is the element of the dual space $\operatorname{Hom}_{\mathbb{R}}(\mathbb{D}, \mathbb{R})$ associated with $Z$ by the standard pairing $\langle Z^{\mathsf{T}}, W\rangle = a c + b d$, and it is **not** a further realization of the algebra. The dual of a left module is a right module, carrying the *right* action $(\varphi\cdot Z)(W) = \varphi(ZW)$. Because $\mathbb{D}$ is commutative, the right action is the action of the same element, and the row picture and the column picture are interchanged by transposition without a conjugate: the transpose of $\rho_L(Z)$ is $\rho_L(Z)$ itself, since the regular matrix is symmetric. This is the degeneration of the biquaternion transposition identity, where the transpose of the left matrix is the left matrix of the conjugate.

## Multiplication in Two-Component Form

**Proposition (the product in components).** Let $Z, W$ have two-component vectors $(a, b)$ and $(c, d)$. Then the two-component vector of the product has components

$$
(ZW)^0 = a c + b d, \qquad (ZW)^1 = a d + b c.
$$

**Proof.** Expand $ZW = (a+j b)(c+j d) = a c + adj + bcj + b j d^2$ and use $j^2 = +1$ to collect the terms:

$$
ZW = (a c + b d) 1 + (a d + b c) j,
$$

which is the displayed pair.

**Comparison with the complex case.** For the complex number $Z = a+i b$ with the complex unit $i^2 = -1$, the product with $W = c+i d$ has components

$$
(ZW)^0 = a c - b d, \qquad (ZW)^1 = a d + b c.
$$

The two product rules differ **only** in the sign of the $b d$ term in the first component: the split-complex product adds $b d$, the complex product subtracts it. This single sign is the whole difference between the two algebras at the level of components, and it is the reason the split-complex norm is indefinite while the complex one is definite.

| product rule | first component | second component |
|---|---|---|
| complex ($i^2 = -1$) | $a c - b d$ | $a d + b c$ |
| split-complex ($j^2 = +1$) | $a c + b d$ | $a d + b c$ |

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

For $Z = a+j b$ the conjugation is $\bar Z = a-j b$, so in coordinates

$$
\overline{(a, b)} = (a, -b),
$$

and in the idempotent coordinates

$$
\overline{(Z_+, Z_-)} = (Z_-, Z_+),
$$

because $\bar Z = a-j b = Z_- \Pi_1 + Z_+ \Pi_2$. So the conjugation reflects the coefficient plane across the real axis and swaps the two idempotent coordinates. It is $\mathbb{R}$-linear, of order two, and its matrix in the basis $\{1, j\}$ is

$$
C = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix},
$$

a diagonal reflection; in the idempotent basis $\{\Pi_1, \Pi_2\}$ its matrix is $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, the swap. In the complex case the matrix is the same $C$; the difference is not in the conjugation but in the product, and it is the product that makes the conjugation a **ring** involution here as there.

## The Two Fixed-Point Subspaces

The conjugation splits the coefficient space into its fixed and anti-fixed subspaces.

**Fixed subspace.** The condition $(a,-b) = (a,b)$ gives $b = 0$, so

$$
\mathbb{R}_{\mathbb{D}} = \{(a, 0)\},
$$

the real axis, of real dimension $1$. It is the set of real components.

**Anti-fixed subspace.** The condition $(a,-b) = (-a,-b)$ gives $a = 0$, so

$$
j\mathbb{R}_{\mathbb{D}} = \{(0, b)\},
$$

the split imaginary axis, of real dimension $1$. Its elements are the pure imaginary components.

So $\mathbb{D} = \mathbb{R}_{\mathbb{D}}\oplus j\mathbb{R}_{\mathbb{D}}$ as a direct sum of coordinate axes, and each coordinate $a, b$ is the projection onto the corresponding axis:

$$
a = \tfrac12(Z + \bar Z), \qquad b = \tfrac12 j^{-1}(Z - \bar Z).
$$

In the idempotent basis the same two lines appear as the diagonals $(t,t)$ and $(t,-t)$, and it is those two lines, rather than the coordinate axes, that carry the multiplicative structure: the coordinate axes carry the definite norm, the diagonals the isotropic one.

## The Norm with Its Two Signs

The norm of $Z = a+j b$ in coordinates is

$$
N(Z) = Z\bar Z = a^2 - b^2,
$$

the difference of the two squares of the coordinates. Its polarisation is the symmetric bilinear form

$$
g(Z, W) = a c - b d, \qquad Z = (a,b), \; W = (c,d),
$$

with matrix $\operatorname{diag}(1, -1)$ and signature $(1,1)$. So the coefficient space is a **Lorentzian plane**: the form is indefinite, of the two signs, and its isotropic set is the pair of diagonal lines $a = \pm b$.

| region | coordinate condition | sign of $N$ |
|---|---|---|
| spacelike | $\lvert a\rvert > \lvert b\rvert$ | $+$ |
| null | $\lvert a\rvert = \lvert b\rvert$ | $0$ |
| timelike | $\lvert a\rvert < \lvert b\rvert$ | $-$ |

### The Two Real Restrictions

Restricted to the two fixed-point subspaces the norm is definite:

$$
N\big|_{\mathbb{R}_{\mathbb{D}}}(a) = a^2 \quad (\text{positive definite}), \qquad N\big|_{j\mathbb{R}_{\mathbb{D}}}(b) = -b^2 \quad (\text{negative definite}),
$$

so the real axis is positive definite and the split imaginary axis negative definite. This is the coordinate statement, made in *Split-Complex Norm and Invertibility*, that the null cone meets each eigenspace only at the origin. In the idempotent coordinates the same form is the product $N = Z_+Z_-$, which vanishes exactly when one coordinate vanishes.

**Comparison with the complex case.** For $\mathbb{C}$ the norm is

$$
N_{\mathbb{C}}(Z) = Z\bar Z = a^2 + b^2,
$$

the **sum** of the two squares: positive definite, so the complex coefficient plane carries a Euclidean, not a Lorentzian, structure. It is again the single sign of the product rule that produces the difference: the square $i^2 = -1$ turns the $b^2$ term of $a^2+b^2$ into $-b^2$ in the split case, and the definite form becomes the indefinite one.

## The Two-Component Opposite of the Complex Two-Component Representation

The complex field and the split-complex algebra are the two two-dimensional real algebras generated by an element of square $-1$ and $+1$ respectively, and their two-component realizations are parallel in every respect except the sign of the generator's square. The following table is the comparison in full.

| feature | $\mathbb{C}$ ($i^2 = -1$) | $\mathbb{D}$ ($j^2 = +1$) |
|---|---|---|
| coefficient space | $\mathbb{R}^2$, components $(a,b)$ | $\mathbb{R}^2$, components $(a,b)$ |
| product rule | $(a c-b d, \, a d+b c)$ | $(a c+b d, \, a d+b c)$ |
| conjugation in coordinates | $(a,-b)$ | $(a,-b)$ |
| fixed / anti-fixed subspaces | $\mathbb{R}$ and $i\mathbb{R}$ | $\mathbb{R}_{\mathbb{D}}$ and $j\mathbb{R}_{\mathbb{D}}$ |
| norm | $a^2+b^2$, positive definite | $a^2-b^2$, signature $(1,1)$ |
| isotropic set | $\{0\}$ | the two lines $a = \pm b$ |
| zero divisors | none | the two idempotent lines |
| idempotents beyond $0,1$ | none | $\Pi_\pm$ |
| isomorphism | field $\mathbb{C}$ | ring $\mathbb{R}\oplus\mathbb{R}$ |

The two realizations share their coefficient space, their column and row, their product's second component, and their conjugation; they differ in the sign of the first component's $b d$ term, and that single difference turns a field into a ring with zero divisors and a Euclidean plane into a Lorentzian one. The split-complex algebra is thus the **indefinite two-component** algebra, the systematic opposite of the complex field, and the comparison table is the complete statement of the difference at the level of coordinates.

## Summary

A split-complex number $Z = a+j b$ is realized as its two-component vector $(a, b)$ in $\mathbb{R}^2$, with column $\begin{pmatrix} a \\ b \end{pmatrix}$ and dual row $(a, b)$; the map to $\mathbb{R}^2$ is an isomorphism of real vector spaces, and the component space is the algebra itself as a coordinate space. The product in components is $(ZW)^0 = a c+b d$, $(ZW)^1 = a d+b c$, differing from the complex product rule in the single sign of the $b d$ term; the left multiplication operator is the regular matrix $\begin{pmatrix} a & b \\ b & a \end{pmatrix}$ of *Split-Complex Regular Representation*.

The conjugation is the reflection $(a,b) \mapsto (a,-b)$, with fixed subspace the real axis and anti-fixed subspace the split imaginary axis. The norm is $a^2-b^2$, indefinite of signature $(1,1)$ with isotropic set the two lines $a = \pm b$; restricted to the real axis it is positive definite and to the split imaginary axis negative definite. In the idempotent coordinates the same form is $Z_+Z_-$ and the conjugation swaps the two coordinates. The complex field shares the coefficient space, the conjugation, the column and row picture and the second component of the product, and differs only in the sign of the $b d$ term of the first component; that sign is the whole difference between the definite two-component algebra and the indefinite one, between a field and a ring with zero divisors.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | Split complex algebra |
| $Z = a + j b$ | General split complex number |
| $Z^\mu = (Z^0, Z^1) = (a, b)$ | Two-component vector |
| $Z^0 = a$, $Z^1 = b$ | Real and imaginary components |
| $Z = \begin{pmatrix} a \\ b \end{pmatrix}$, $Z^{\mathsf{T}} = (a\ \ b)$ | Column and row |
| $\rho_L(Z) = \begin{pmatrix} a & b \\ b & a \end{pmatrix}$ | Left multiplication matrix |
| $(ZW)^0 = a c+b d$, $(ZW)^1 = a d+b c$ | Component product rule |
| $\overline{(a,b)} = (a,-b)$ | Conjugation in coordinates |
| $C = \operatorname{diag}(1,-1)$ | Matrix of the conjugation |
| $\mathbb{R}_{\mathbb{D}} = \{(a,0)\}$ | Fixed subspace, real axis |
| $j\mathbb{R}_{\mathbb{D}} = \{(0,b)\}$ | Anti-fixed subspace, split imaginary axis |
| $N(Z) = a^2-b^2$ | Norm, signature $(1,1)$ |
| $g(Z,W) = a c-b d$ | Polarised form |
| $(Z_+, Z_-) = (a+b, a-b)$ | Idempotent coordinates |

## Further Reading

- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the two-component and matrix readings of the split complex plane.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the parallel treatment of the two-dimensional real algebras.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the split complex numbers as $\mathrm{Cl}_{1,0}$ and their coordinate realization.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for signatures, isotropic vectors and the Lorentzian plane.
- Harvey Cohn, *A Classical Invitation to Algebraic Numbers and Class Fields* (Springer, Universitext, 1978), for the comparison of the two quadratic real algebras of dimension two.
