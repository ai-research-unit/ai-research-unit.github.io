
# __Split-Complex Two-Component Element Representation__

## Introduction

The split-complex algebra $\mathbb{D}$ is two-dimensional over $\mathbb{R}$, so a split-complex number is read off as its list of **two real coefficients**, $Q = q + j q' \leftrightarrow (q, q')$. This article presents that **two-component realization** in full: the coefficient space, the column and the dual row, the component form of the product, the conjugation in coordinates, the two fixed-point subspaces as coordinate conditions, and the norm with its two signs. It is the last of the three Representation articles, after *Split-Complex Element Representations* and *Split-Complex Regular Element Representation*.

The word *representation* is used here in the sense of a concrete realization of the algebra as computable objects, not in the technical sense of a vector space carrying an algebra homomorphism into its endomorphisms. The technical sense is the subject of *Split-Complex Element Representations*, and the matrix of the action on this coefficient space is the subject of *Split-Complex Regular Element Representation*; this article supplies the coordinate space on which that operator is written.

The article owns the coefficient space $\mathbb{R}^2$, the column and the row, the component form of the product, the conjugation in coordinates, the two fixed-point subspaces and the norm with its two real restrictions. It does not treat the matrix of multiplication on this space, which belongs to *Split-Complex Regular Element Representation*; it does not treat the polar forms, which belong to *Modulus–Unit Polar Decomposition of Split-Complex Numbers* and its two companion articles; and it introduces no physical vocabulary. The comparison throughout is with the complex field, whose two-component realization is the **definite** one and whose product rule differs from the present one in a single sign.

## The Coefficient Space

**Definition.** The **two-component vector** of a split-complex number $Q = q+j q'$ is the ordered pair

$$
Q^\mu = (Q^0, Q^1), \qquad Q^0 = q, \quad Q^1 = q'.
$$

The coefficient of the unit is written $Q^0$ and the coefficient of $j$ is written $Q^1$; the component $Q^0$ is the **real component** and $Q^1$ the **imaginary component**. These are the honest names, because they are the coefficients of the real and imaginary parts of $Q$ and nothing else.

**Proposition.** The map $Q \mapsto Q^\mu$ is an $\mathbb{R}$-linear isomorphism from $\mathbb{D}$ onto $\mathbb{R}^2$. Consequently the coefficient space has real dimension $2$ and no other dimension: a split-complex number is entirely real, so its coefficient space is $\mathbb{R}^2$ and there is no splitting of each coordinate into real and imaginary parts.

**Proof.** The map sends the basis $1, j$ to the standard basis of $\mathbb{R}^2$ and is extended by linearity; it is bijective on bases. The algebra is a real vector space of dimension $2$, matched by the dimension of $\mathbb{R}^2$.

The coefficient space $\mathbb{R}^2$ **is** the algebra itself, seen as a coordinate space, and it is also the simple module of $\mathbb{D}$: the algebra is two-dimensional, its two idempotent components are one-dimensional, and the regular module is the direct sum of the two one-dimensional simple modules. So the numbers $2$, $2$, $2$ appearing as the dimension of the algebra, the size of the regular matrix of *Split-Complex Regular Element Representation*, and the dimension of the coefficient space are the same number for the same reason.

### Coordinates in the Idempotent Basis

The coefficient pair $(q, q')$ in the basis $\{1, j\}$ and the idempotent pair $(Q_+, Q_-)$ in the basis $\{\Pi_+, \Pi_-\}$ are related by

$$
Q_+ = q+q', \qquad Q_- = q-q', \qquad q = \tfrac12(Q_+ + Q_-), \qquad q' = \tfrac12(Q_+ - Q_-),
$$

the change of coordinates of the plane. The pair $(Q_+, Q_-)$ is the pair of **eigen-coordinates** of the conjugation, since the regular representation is diagonal in that basis, and it is also the pair that makes the multiplication componentwise.

## The Column and the Row

**Definition.** The **column** of $Q$ is the $2\times 1$ matrix

$$
Q = \begin{pmatrix} q \\ q' \end{pmatrix},
$$

the transpose of the two-component vector. The **row** of $Q$ is the $1\times 2$ matrix

$$
Q^{\mathsf{T}} = \begin{pmatrix} q & q' \end{pmatrix}.
$$

The column is the transcribed form of the same object, and it is convenient because the product of split-complex numbers is bilinear. For a fixed $Q$, the map $B \mapsto QB$ sends coordinates linearly to coordinates, so it is an $\mathbb{R}$-linear endomorphism of the coefficient space, and with the column convention it is written as a $2\times2$ matrix acting on the column of $B$:

$$
QB \longleftrightarrow \mathsf{M}_2(Q)\, B, \qquad \mathsf{M}_2(Q) = \begin{pmatrix} q & q' \\ q' & q \end{pmatrix}.
$$

The matrix $\mathsf{M}_2(Q)$ is constructed and verified in *Split-Complex Regular Element Representation*; the present article records only that the product rule admits this reading. The **component form** is the same statement written out:

$$
QB = (q b + q' b') + (q b' + q' b) j, \qquad B = b+j b',
$$

so the two components of the product are the two entries of the matrix product $\mathsf{M}_2(Q)B$.

**Remark (the row is the dual).** The row $Q^{\mathsf{T}}$ is the element of the dual space $\operatorname{Hom}_{\mathbb{R}}(\mathbb{D}, \mathbb{R})$ associated with $Q$ by the standard pairing $\langle Q^{\mathsf{T}}, B\rangle = q b + q' b'$, and it is **not** a further realization of the algebra. The dual of a left module is a right module, carrying the *right* action $(\varphi\cdot Q)(B) = \varphi(QB)$. Because $\mathbb{D}$ is commutative, the right action is the action of the same element, and the row picture and the column picture are interchanged by transposition without a conjugate: the transpose of $\mathsf{M}_2(Q)$ is $\mathsf{M}_2(Q)$ itself, since the regular matrix is symmetric.

## Multiplication in Two-Component Form

**Proposition (the product in components).** Let $Q, B$ have two-component vectors $(q, q')$ and $(b, b')$. Then the two-component vector of the product has components

$$
(QB)^0 = q b + q' b', \qquad (QB)^1 = q b' + q' b.
$$

**Proof.** Expand $QB = (q+j q')(b+j b') = q b + q b' j + q' b j + q' b' j^2$ and use $j^2 = +1$ to collect the terms:

$$
QB = (q b + q' b') 1 + (q b' + q' b) j,
$$

which is the displayed pair.

**Comparison with the complex case.** For the complex number $Q = q+i q'$ with the complex unit $i^2 = -1$, the product with $B = b+i b'$ has components

$$
(QB)^0 = q b - q' b', \qquad (QB)^1 = q b' + q' b.
$$

The two product rules differ **only** in the sign of the $q' b'$ term in the first component: the split-complex product adds $q' b'$, the complex product subtracts it. This single sign is the whole difference between the two algebras at the level of components, and it is the reason the split-complex norm is indefinite while the complex one is definite.

| product rule | first component | second component |
|---|---|---|
| complex ($i^2 = -1$) | $q b - q' b'$ | $q b' + q' b$ |
| split-complex ($j^2 = +1$) | $q b + q' b'$ | $q b' + q' b$ |

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

For $Q = q+j q'$ the conjugation is $\bar Q = q-j q'$, so in coordinates

$$
\overline{(q, q')} = (q, -q'),
$$

and in the idempotent coordinates

$$
\overline{(Q_+, Q_-)} = (Q_-, Q_+),
$$

because $\bar Q = q-j q' = Q_- \Pi_+ + Q_+ \Pi_-$. So the conjugation reflects the coefficient plane across the real axis and swaps the two idempotent coordinates. It is $\mathbb{R}$-linear, of order two, and its matrix in the basis $\{1, j\}$ is

$$
C = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix},
$$

a diagonal reflection; in the idempotent basis $\{\Pi_+, \Pi_-\}$ its matrix is $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, the swap. In the complex case the matrix is the same $C$; the difference is not in the conjugation but in the product, and it is the product that makes the conjugation a **ring** involution here as there.

## The Two Fixed-Point Subspaces

The conjugation splits the coefficient space into its fixed and anti-fixed subspaces.

**Fixed subspace.** The condition $(q,-q') = (q,q')$ gives $q' = 0$, so

$$
\mathbb{R}_{\mathbb{D}} = \{(q, 0)\},
$$

the real axis, of real dimension $1$. It is the set of real components.

**Anti-fixed subspace.** The condition $(q,-q') = (-q,-q')$ gives $q = 0$, so

$$
j\mathbb{R}_{\mathbb{D}} = \{(0, q')\},
$$

the split imaginary axis, of real dimension $1$. Its elements are the pure imaginary components.

So $\mathbb{D} = \mathbb{R}_{\mathbb{D}}\oplus j\mathbb{R}_{\mathbb{D}}$ as a direct sum of coordinate axes, and each coordinate $q, q'$ is the projection onto the corresponding axis:

$$
q = \tfrac12(Q + \bar Q), \qquad q' = \tfrac12 j^{-1}(Q - \bar Q).
$$

In the idempotent basis the same two lines appear as the diagonals $(t,t)$ and $(t,-t)$, and it is those two lines, rather than the coordinate axes, that carry the multiplicative structure: the coordinate axes carry the definite norm, the diagonals the isotropic one.

## The Norm with Its Two Signs

The norm of $Q = q+j q'$ in coordinates is

$$
\langle Q\rangle_{*} = Q\bar Q = q^2 - q'^2,
$$

the difference of the two squares of the coordinates. Its polarisation is the symmetric bilinear form

$$
g(Q, B) = q b - q' b', \qquad Q = (q,q'), \; B = (b,b'),
$$

with matrix $\operatorname{diag}(1, -1)$ and signature $(1,1)$. So the coefficient space is a **Lorentzian plane**: the form is indefinite, of the two signs, and its isotropic set is the pair of diagonal lines $q = \pm q'$.

| region | coordinate condition | sign of $\langle Q\rangle_{*}$ |
|---|---|---|
| timelike | $\lvert q\rvert > \lvert q'\rvert$ | $+$ |
| null | $\lvert q\rvert = \lvert q'\rvert$ | $0$ |
| spacelike | $\lvert q\rvert < \lvert q'\rvert$ | $-$ |

### The Two Real Restrictions

Restricted to the two fixed-point subspaces the norm is definite:

$$
\langle\cdot\rangle_{*}\big|_{\mathbb{R}_{\mathbb{D}}}(q) = q^2 \quad (\text{positive definite}), \qquad \langle\cdot\rangle_{*}\big|_{j\mathbb{R}_{\mathbb{D}}}(q') = -q'^2 \quad (\text{negative definite}),
$$

so the real axis is positive definite and the split imaginary axis negative definite. This is the coordinate statement, made in *Norm and Invertibility in the General Split-Complex Algebra*, that the null cone meets each eigenspace only at the origin. In the idempotent coordinates the same form is the product $\langle Q\rangle_{*} = Q_+Q_-$, which vanishes exactly when one coordinate vanishes.

**Comparison with the complex case.** For $\mathbb{C}$ the norm is

$$
N_{\mathbb{C}}(Q) = Q\bar Q = q^2 + q'^2,
$$

the **sum** of the two squares: positive definite, so the complex coefficient plane carries a Euclidean, not a Lorentzian, structure. It is again the single sign of the product rule that produces the difference: the square $i^2 = -1$ turns the $q'^2$ term of $q^2+q'^2$ into $-q'^2$ in the split case, and the definite form becomes the indefinite one.

## The Two-Component Opposite of the Complex Two-Component Element Representation

The complex field and the split-complex algebra are the two two-dimensional real algebras generated by an element of square $-1$ and $+1$ respectively, and their two-component realizations are parallel in every respect except the sign of the generator's square. The following table is the comparison in full.

| feature | $\mathbb{C}$ ($i^2 = -1$) | $\mathbb{D}$ ($j^2 = +1$) |
|---|---|---|
| coefficient space | $\mathbb{R}^2$, components $(q,q')$ | $\mathbb{R}^2$, components $(q,q')$ |
| product rule | $(q b-q' b', \, q b'+q' b)$ | $(q b+q' b', \, q b'+q' b)$ |
| conjugation in coordinates | $(q,-q')$ | $(q,-q')$ |
| fixed / anti-fixed subspaces | $\mathbb{R}$ and $i\mathbb{R}$ | $\mathbb{R}_{\mathbb{D}}$ and $j\mathbb{R}_{\mathbb{D}}$ |
| norm | $q^2+q'^2$, positive definite | $q^2-q'^2$, signature $(1,1)$ |
| isotropic set | $\{0\}$ | the two lines $q = \pm q'$ |
| zero divisors | none | the two idempotent lines |
| idempotents beyond $0,1$ | none | $\Pi_\pm$ |
| isomorphism | field $\mathbb{C}$ | ring $\mathbb{R}\oplus\mathbb{R}$ |

The two realizations share their coefficient space, their column and row, their product's second component, and their conjugation; they differ in the sign of the first component's $q' b'$ term, and that single difference turns a field into a ring with zero divisors and a Euclidean plane into a Lorentzian one. The split-complex algebra is thus the **indefinite two-component** algebra, the systematic opposite of the complex field, and the comparison table is the complete statement of the difference at the level of coordinates.

## Summary

A split-complex number $Q = q+j q'$ is realized as its two-component vector $(q, q')$ in $\mathbb{R}^2$, with column $\begin{pmatrix} q \\ q' \end{pmatrix}$ and dual row $(q, q')$; the map to $\mathbb{R}^2$ is an isomorphism of real vector spaces, and the component space is the algebra itself as a coordinate space. The product in components is $(QB)^0 = q b+q' b'$, $(QB)^1 = q b'+q' b$, differing from the complex product rule in the single sign of the $q' b'$ term; the left multiplication operator is the regular matrix $\begin{pmatrix} q & q' \\ q' & q \end{pmatrix}$ of *Split-Complex Regular Element Representation*.

The conjugation is the reflection $(q,q') \mapsto (q,-q')$, with fixed subspace the real axis and anti-fixed subspace the split imaginary axis. The norm is $q^2-q'^2$, indefinite of signature $(1,1)$ with isotropic set the two lines $q = \pm q'$; restricted to the real axis it is positive definite and to the split imaginary axis negative definite. In the idempotent coordinates the same form is $Q_+Q_-$ and the conjugation swaps the two coordinates. The complex field shares the coefficient space, the conjugation, the column and row picture and the second component of the product, and differs only in the sign of the $q' b'$ term of the first component; that sign is the whole difference between the definite two-component algebra and the indefinite one, between a field and a ring with zero divisors.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | Split complex algebra |
| $Q = q + j q'$ | General split complex number |
| $Q^\mu = (Q^0, Q^1) = (q, q')$ | Two-component vector |
| $Q^0 = q$, $Q^1 = q'$ | Real and imaginary components |
| $Q = \begin{pmatrix} q \\ q' \end{pmatrix}$, $Q^{\mathsf{T}} = (q\ \ q')$ | Column and row |
| $\mathsf{M}_2(Q) = \begin{pmatrix} q & q' \\ q' & q \end{pmatrix}$ | Left multiplication matrix |
| $(QB)^0 = q b+q' b'$, $(QB)^1 = q b'+q' b$ | Component product rule |
| $\overline{(q,q')} = (q,-q')$ | Conjugation in coordinates |
| $C = \operatorname{diag}(1,-1)$ | Matrix of the conjugation |
| $\mathbb{R}_{\mathbb{D}} = \{(q,0)\}$ | Fixed subspace, real axis |
| $j\mathbb{R}_{\mathbb{D}} = \{(0,q')\}$ | Anti-fixed subspace, split imaginary axis |
| $\langle Q\rangle_{*} = q^2-q'^2$ | Norm, signature $(1,1)$ |
| $g(Q,B) = q b-q' b'$ | Polarised form |
| $(Q_+, Q_-) = (q+q', q-q')$ | Idempotent coordinates |

## Further Reading

- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the two-component and matrix readings of the split complex plane.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the split complex numbers as $\mathrm{Cl}_{1,0}$ and their coordinate realization.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for signatures, isotropic vectors and the Lorentzian plane.
- Harvey Cohn, *A Classical Invitation to Algebraic Numbers and Class Fields* (Springer, Universitext, 1978), for the comparison of the two quadratic real algebras of dimension two.
