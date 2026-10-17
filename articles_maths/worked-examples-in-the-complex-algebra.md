
# __Worked Examples in the Complex Algebra__

## Introduction

This article is the computed companion to the structural articles of the complex algebra. Where *Complex Algebra* states the definitions and proves the general properties, and *Complexoid Subspaces*, *Complex Norm and Invertibility*, *Complex Polar Element Representation*, *Complex Regular Element Representation* and *Complex Automorphisms and Derivations* develop them, the present article exhibits every one of those structures on explicit elements, so that the general statements can be read against a concrete computation.

The elements used throughout are

$$
Q_1 = 3 + 4i, \qquad Q_2 = 1 - 2i,
$$

chosen because their arithmetic is exact and their norms are small squares and small integers: $N(Q_1) = 25$ and $N(Q_2) = 5$, so that the inverse and the Galois action both display rational data. Where a statement needs a degenerate example, the element $0$ and the real and imaginary points of the previous articles are used. The conventions are those of *Complex Algebra*: basis $1$, $i$, $i^2 = -1$, involution $\bar{Q} = q - i q'$, norm $N(Q) = Q\bar{Q} = q^2+q'^2$.

Every numerical value below is recomputed exactly; where a trigonometric value is not rational it is given to the stated number of decimals and the exact replacement is indicated.

## The Algebra on Concrete Elements

**Sum, difference and product.** With $Q_1 = 3+4i$ and $Q_2 = 1-2i$,

$$
Q_1 + Q_2 = 4 + 2i, \qquad Q_1 - Q_2 = 2 + 6i,
$$

and, applying $(q_1+iq'_1)(q_2+iq'_2) = (q_1q_2-q'_1q'_2) + (q_1q'_2+q'_1q_2)i$,

$$
Q_1 Q_2 = (3+4i)(1-2i) = (3\cdot 1 - 4\cdot(-2)) + (3\cdot(-2) + 4\cdot 1)i = 11 - 2i .
$$

The reversed product is

$$
Q_2 Q_1 = (1-2i)(3+4i) = (1\cdot 3 - (-2)\cdot 4) + (1\cdot 4 + (-2)\cdot 3)i = 11 - 2i,
$$

equal to $Q_1Q_2$, the concrete form of commutativity.

**Powers and the norm under multiplication.** The square of $Q_1$ is

$$
Q_1^2 = (3+4i)^2 = 9 + 24i + 16 i^2 = -7 + 24i,
$$

with

$$
N(Q_1^2) = (-7)^2 + 24^2 = 49 + 576 = 625 = 25^2 = N(Q_1)^2,
$$

the multiplicativity of the norm on a single element. In the same way $N(Q_1Q_2) = N(11-2i) = 121+4 = 125 = 25 \cdot 5 = N(Q_1) N(Q_2)$.

**Associativity and distributivity** are illustrated by the two products above agreeing and by $(Q_1+Q_2)^2 = Q_1^2 + 2Q_1Q_2 + Q_2^2$, which is a computation of the same rules and needs no separate display.

## The Two Involutions on Concrete Elements

The complex algebra carries the identity and complex conjugation.

**The identity.** $\operatorname{id}(Q_1) = 3+4i = Q_1$ and $\operatorname{id}(Q_2) = Q_2$. The identity fixes every element.

**Complex conjugation.** $\bar{Q}_1 = 3-4i$ and $\bar{Q}_2 = 1+2i$. Conjugation is an involution:

$$
\overline{\bar{Q}_1} = \overline{3-4i} = 3+4i = Q_1,
$$

and it is an automorphism of the algebra:

$$
\overline{Q_1 Q_2} = \overline{11-2i} = 11+2i, \qquad \bar{Q}_1\,\bar{Q}_2 = (3-4i)(1+2i) = 3 + 6i - 4i - 8i^2 = 11 + 2i,
$$

the two values agreeing. In particular the norm is invariant: $N(\bar{Q}_1) = 3^2 + (-4)^2 = 25 = N(Q_1)$.

| element | $\operatorname{id}$ | $\bar{\cdot}$ | $\bar{\cdot}$ applied twice |
|---|---|---|---|
| $Q_1 = 3+4i$ | $3+4i$ | $3-4i$ | $3+4i$ |
| $Q_2 = 1-2i$ | $1-2i$ | $1+2i$ | $1-2i$ |
| $Q_1Q_2 = 11-2i$ | $11-2i$ | $11+2i$ | $11-2i$ |

## The Two Subspaces on Concrete Elements

The fixed-point subspace of conjugation is the real axis $\mathbb{R}_{\mathbb{C}}$, and its anti-fixed subspace is the imaginary axis $i\mathbb{R}_{\mathbb{C}}$.

**The real subspace.** An element is fixed by conjugation exactly when its imaginary part vanishes. For $Q_1$ and $Q_2$,

$$
\bar{Q}_1 = Q_1 \iff 3-4i = 3+4i \iff 4 = 0, \quad \text{false},
$$

so $Q_1 \notin \mathbb{R}_{\mathbb{C}}$; the real element $3$ and the real scalar part of $Q_2$, namely $1$, do lie in $\mathbb{R}_{\mathbb{C}}$, with $\overline{3} = 3$.

**The imaginary subspace.** An element is anti-fixed exactly when its real part vanishes. For $Q_1$ and $Q_2$,

$$
\bar{Q}_1 = -Q_1 \iff 3-4i = -3-4i \iff 3 = 0, \quad \text{false},
$$

so $Q_1 \notin i\mathbb{R}_{\mathbb{C}}$; the imaginary multiples $4i$ and $-2i$ do lie in $i\mathbb{R}_{\mathbb{C}}$, with $\overline{4i} = -4i$.

**A product leaving the subspace.** The product of the two anti-fixed elements $4i$ and $-2i$ is

$$
(4i)(-2i) = -8 i^2 = 8 \in \mathbb{R}_{\mathbb{C}},
$$

which is fixed and not anti-fixed, exhibiting the failure of $i\mathbb{R}_{\mathbb{C}}$ to be closed under multiplication.

## The Decompositions, Worked

**The real and imaginary parts.** The eigencomponents of conjugation are

$$
Q_{1,+} = \tfrac{1}{2}(Q_1 + \bar{Q}_1) = \tfrac{1}{2}\bigl((3+4i)+(3-4i)\bigr) = 3 \in \mathbb{R}_{\mathbb{C}},
$$

$$
Q_{1,-} = \tfrac{1}{2}(Q_1 - \bar{Q}_1) = \tfrac{1}{2}\bigl((3+4i)-(3-4i)\bigr) = 4i \in i\mathbb{R}_{\mathbb{C}},
$$

with $Q_{1,+} + Q_{1,-} = 3+4i = Q_1$. For $Q_2$ the same computation gives $Q_{2,+} = 1$ and $Q_{2,-} = -2i$, again summing to $Q_2$. The two subspaces meet only in $0$: the element $Q_{1,+} = 3$ is not a multiple of $i$ unless $3 = 0$.

**The norm on the pieces.** $N(Q_{1,+}) = 3^2 = 9$ and $N(Q_{1,-}) = 4^2 = 16$, and

$$
N(Q_{1,+}) + N(Q_{1,-}) = 9 + 16 = 25 = N(Q_1),
$$

the Pythagorean instance of the definite decomposition; for $Q_2$, $N(Q_{2,+}) + N(Q_{2,-}) = 1 + 4 = 5 = N(Q_2)$.

## The Matrix Model, Worked

Multiplication by an element is an $\mathbb{R}$-linear endomorphism of $\mathbb{C}$, and in the basis $1$, $i$ it is the Cayley matrix of *Complex Regular Element Representation*. The matrices of the two worked elements are

$$
\mathsf{M}_2(Q_1) = \begin{pmatrix} 3 & -4 \\ 4 & 3 \end{pmatrix}, \qquad \mathsf{M}_2(Q_2) = \begin{pmatrix} 1 & 2 \\ -2 & 1 \end{pmatrix}.
$$

**Multiplicativity.** The product of the two matrices reproduces the product computed in components,

$$
\mathsf{M}_2(Q_1)\mathsf{M}_2(Q_2) = \begin{pmatrix} 3 & -4 \\ 4 & 3 \end{pmatrix}\begin{pmatrix} 1 & 2 \\ -2 & 1 \end{pmatrix} = \begin{pmatrix} 11 & 2 \\ -2 & 11 \end{pmatrix} = \mathsf{M}_2(Q_1Q_2),
$$

the matrix of $Q_1Q_2 = 11-2i$.

**The determinant is the norm.** Each matrix has determinant equal to the norm of its element,

$$
\det \mathsf{M}_2(Q_1) = 3\cdot 3 - (-4)\cdot 4 = 25 = N(Q_1), \qquad \det \mathsf{M}_2(Q_2) = 1\cdot 1 - 2\cdot(-2) = 5 = N(Q_2),
$$

so multiplicativity of the determinant is the multiplicativity $N(Q_1Q_2) = N(Q_1)N(Q_2)$ on the worked pair.

**Transposition is conjugation.** The transpose of the matrix of $Q_1$ is the matrix of $\bar{Q}_1$:

$$
\mathsf{M}_2(Q_1)^{\mathsf{T}} = \begin{pmatrix} 3 & 4 \\ -4 & 3 \end{pmatrix} = \mathsf{M}_2(3-4i) = \mathsf{M}_2(\bar{Q}_1),
$$

and likewise $\mathsf{M}_2(Q_2)^{\mathsf{T}} = \mathsf{M}_2(\bar{Q}_2)$.

## The Galois Action, Worked

The unique nontrivial $\mathbb{R}$-automorphism of $\mathbb{C}$ is complex conjugation, written $\sigma = \bar{\cdot}$, and *Complex Automorphisms and Derivations* and *Galois Theory of ℂ/ℝ* treat its automorphism theory. On the worked elements,

$$
\sigma(Q_1) = \bar{Q}_1 = 3-4i, \qquad \sigma(Q_2) = \bar{Q}_2 = 1+2i, \qquad \sigma(Q_1Q_2) = \overline{11-2i} = 11+2i .
$$

The automorphism property is exhibited by

$$
\sigma(Q_1)\sigma(Q_2) = (3-4i)(1+2i) = 3+6i-4i-8i^2 = 11+2i = \sigma(Q_1Q_2),
$$

and the norm is preserved, $N(\sigma(Q_1)) = 25 = N(Q_1)$. The fixed points are exactly the real axis: $\sigma(Q_1) = Q_1$ would require $4 = 0$, so $Q_1$ is moved; $\sigma(3) = 3$ and $\sigma$ fixes every real number. The action is not $\mathbb{C}$-linear: $\sigma(i\cdot 1) = -i$ while $i\,\sigma(1) = i$, so $\sigma$ conjugates the scalar $i$, which is the concrete form of the conjugate-linearity of complex conjugation over $\mathbb{C}$.

## Summary

The article exhibits the structures of the complex algebra on the elements $Q_1 = 3+4i$ and $Q_2 = 1-2i$. Their product is $Q_1Q_2 = 11-2i$ and their square norms are $N(Q_1) = 25$, $N(Q_2) = 5$, $N(Q_1Q_2) = 125$, so the norm is multiplicative on the worked pair. The identity and complex conjugation are the two involutions; conjugation sends $Q_1$ to $3-4i$ and $Q_2$ to $1+2i$, is an involution and an algebra automorphism, and fixes exactly the real axis while negating the imaginary axis.

The eigencomponents of conjugation are $Q_{1,+} = 3 \in \mathbb{R}_{\mathbb{C}}$ and $Q_{1,-} = 4i \in i\mathbb{R}_{\mathbb{C}}$, with $N(Q_{1,+})+N(Q_{1,-}) = N(Q_1)$; the product $(4i)(-2i) = 8$ is real and shows that the imaginary subspace is not closed. The unit criterion and the inverse formula belong to the topology layer and are developed, with the worked instances, in the companion article *Complex Norm and Invertibility*. The matrix model carries the same data: $\mathsf{M}_2(Q_1) = \begin{pmatrix} 3 & -4 \\ 4 & 3 \end{pmatrix}$ and $\mathsf{M}_2(Q_2) = \begin{pmatrix} 1 & 2 \\ -2 & 1 \end{pmatrix}$ multiply to $\mathsf{M}_2(Q_1Q_2)$, their determinants $25$ and $5$ are the norms of the elements, and $\mathsf{M}_2(Q_1)^{\mathsf{T}} = \mathsf{M}_2(\bar{Q}_1)$ is the transpose relation. The Galois action $\sigma = \bar{\cdot}$ preserves the product and the norm on the worked elements and is conjugate-linear over $\mathbb{C}$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{C}$ | the complex algebra, basis $1$, $i$, $i^2 = -1$ |
| $Q_1 = 3+4i$, $Q_2 = 1-2i$ | the two worked elements |
| $\operatorname{id}, \bar{\cdot}$ | the identity and complex conjugation |
| $\sigma = \bar{\cdot}$ | the nontrivial $\mathbb{R}$-automorphism, the Galois action |
| $Q_{1,\pm} = \tfrac12(Q_1 \pm \bar{Q}_1)$ | the eigencomponents of conjugation |
| $\mathbb{R}_{\mathbb{C}}, i\mathbb{R}_{\mathbb{C}}$ | the real and imaginary subspaces |
| $N(Q) = Q\bar{Q} = q^2+q'^2$ | the norm |
| $\mathsf{M}_2(Q) = qI + q'J$ | the Cayley matrix of multiplication by $Q$, the $2\times2$ matrix model |

## Further Reading

- Carl Friedrich Gauss, *Theoria residuorum biquadraticorum, Commentatio secunda* (Göttingen, 1831), for the geometry of the plane and worked computational examples.
- Israel Nathan Herstein, *Topics in Algebra*, 2nd edition (Wiley, 1975), for elementary computational practice with complex numbers and field automorphisms.
- Walter Rudin, *Real and Complex Analysis*, 3rd edition (McGraw-Hill, 1987), for the norm and its multiplicativity.
