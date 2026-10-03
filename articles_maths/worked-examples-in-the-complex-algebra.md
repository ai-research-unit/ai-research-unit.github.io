
# __Worked Examples in the Complex Algebra__

## Introduction

This article is the computed companion to the structural articles of the complex algebra. Where *Complex Algebra* states the definitions and proves the general properties, and *Complex Subspaces*, *Complex Norm and Invertibility*, *Complex Polar Element Representation*, *Complex Regular Element Representation* and *Complex Automorphisms and Derivations* develop them, the present article exhibits every one of those structures on explicit elements, so that the general statements can be read against a concrete computation.

The elements used throughout are

$$
A = 3 + 4i, \qquad B = 1 - 2i,
$$

chosen because their arithmetic is exact and their norms are small squares and small integers: $N(A) = 25$ and $N(B) = 5$, so that the inverse and the Galois action both display rational data. Where a statement needs a degenerate example, the element $0$ and the real and imaginary points of the previous articles are used. The conventions are those of *Complex Algebra*: basis $1$, $i$, $i^2 = -1$, involution $\bar{A} = a - i a'$, norm $N(A) = A\bar{A} = a^2+a'^2$.

Every numerical value below is recomputed exactly; where a trigonometric value is not rational it is given to the stated number of decimals and the exact replacement is indicated.

## The Algebra on Concrete Elements

**Sum, difference and product.** With $A = 3+4i$ and $B = 1-2i$,

$$
A + B = 4 + 2i, \qquad A - B = 2 + 6i,
$$

and, applying $(a+ia')(b+ib') = (ab-a'b') + (ab'+a'b)i$,

$$
A B = (3+4i)(1-2i) = (3\cdot 1 - 4\cdot(-2)) + (3\cdot(-2) + 4\cdot 1)i = 11 - 2i .
$$

The reversed product is

$$
B A = (1-2i)(3+4i) = (1\cdot 3 - (-2)\cdot 4) + (1\cdot 4 + (-2)\cdot 3)i = 11 - 2i,
$$

equal to $AB$, the concrete form of commutativity.

**Powers and the norm under multiplication.** The square of $A$ is

$$
A^2 = (3+4i)^2 = 9 + 24i + 16 i^2 = -7 + 24i,
$$

with

$$
N(A^2) = (-7)^2 + 24^2 = 49 + 576 = 625 = 25^2 = N(A)^2,
$$

the multiplicativity of the norm on a single element. In the same way $N(AB) = N(11-2i) = 121+4 = 125 = 25 \cdot 5 = N(A) N(B)$.

**Associativity and distributivity** are illustrated by the two products above agreeing and by $(A+B)^2 = A^2 + 2AB + B^2$, which is a computation of the same rules and needs no separate display.

## The Two Involutions on Concrete Elements

The complex algebra carries the identity and complex conjugation.

**The identity.** $\operatorname{id}(A) = 3+4i = A$ and $\operatorname{id}(B) = B$. The identity fixes every element.

**Complex conjugation.** $\bar{A} = 3-4i$ and $\bar{B} = 1+2i$. Conjugation is an involution:

$$
\overline{\bar{A}} = \overline{3-4i} = 3+4i = A,
$$

and it is an automorphism of the algebra:

$$
\overline{A B} = \overline{11-2i} = 11+2i, \qquad \bar{A}\,\bar{B} = (3-4i)(1+2i) = 3 + 6i - 4i - 8i^2 = 11 + 2i,
$$

the two values agreeing. In particular the norm is invariant: $N(\bar{A}) = 3^2 + (-4)^2 = 25 = N(A)$.

| element | $\operatorname{id}$ | $\bar{\cdot}$ | $\bar{\cdot}$ applied twice |
|---|---|---|---|
| $A = 3+4i$ | $3+4i$ | $3-4i$ | $3+4i$ |
| $B = 1-2i$ | $1-2i$ | $1+2i$ | $1-2i$ |
| $AB = 11-2i$ | $11-2i$ | $11+2i$ | $11-2i$ |

## The Two Subspaces on Concrete Elements

The fixed-point subspace of conjugation is the real axis $\mathbb{R}_{\mathbb{C}}$, and its anti-fixed subspace is the imaginary axis $i\mathbb{R}_{\mathbb{C}}$.

**The real subspace.** An element is fixed by conjugation exactly when its imaginary part vanishes. For $A$ and $B$,

$$
\bar{A} = A \iff 3-4i = 3+4i \iff 4 = 0, \quad \text{false},
$$

so $A \notin \mathbb{R}_{\mathbb{C}}$; the real element $3$ and the real scalar part of $B$, namely $1$, do lie in $\mathbb{R}_{\mathbb{C}}$, with $\overline{3} = 3$.

**The imaginary subspace.** An element is anti-fixed exactly when its real part vanishes. For $A$ and $B$,

$$
\bar{A} = -A \iff 3-4i = -3-4i \iff 3 = 0, \quad \text{false},
$$

so $A \notin i\mathbb{R}_{\mathbb{C}}$; the imaginary multiples $4i$ and $-2i$ do lie in $i\mathbb{R}_{\mathbb{C}}$, with $\overline{4i} = -4i$.

**A product leaving the subspace.** The product of the two anti-fixed elements $4i$ and $-2i$ is

$$
(4i)(-2i) = -8 i^2 = 8 \in \mathbb{R}_{\mathbb{C}},
$$

which is fixed and not anti-fixed, exhibiting the failure of $i\mathbb{R}_{\mathbb{C}}$ to be closed under multiplication.

## The Decompositions, Worked

**The real and imaginary parts.** The eigencomponents of conjugation are

$$
A_+ = \tfrac{1}{2}(A + \bar{A}) = \tfrac{1}{2}\bigl((3+4i)+(3-4i)\bigr) = 3 \in \mathbb{R}_{\mathbb{C}},
$$

$$
A_- = \tfrac{1}{2}(A - \bar{A}) = \tfrac{1}{2}\bigl((3+4i)-(3-4i)\bigr) = 4i \in i\mathbb{R}_{\mathbb{C}},
$$

with $A_+ + A_- = 3+4i = A$. For $B$ the same computation gives $B_+ = 1$ and $B_- = -2i$, again summing to $B$. The two subspaces meet only in $0$: the element $A_+ = 3$ is not a multiple of $i$ unless $3 = 0$.

**The norm on the pieces.** $N(A_+) = 3^2 = 9$ and $N(A_-) = 4^2 = 16$, and

$$
N(A_+) + N(A_-) = 9 + 16 = 25 = N(A),
$$

the Pythagorean instance of the definite decomposition; for $B$, $N(B_+) + N(B_-) = 1 + 4 = 5 = N(B)$.

## The Matrix Model, Worked

Multiplication by an element is an $\mathbb{R}$-linear endomorphism of $\mathbb{C}$, and in the basis $1$, $i$ it is the Cayley matrix of *Complex Regular Element Representation*. The matrices of the two worked elements are

$$
\rho_L(A) = \begin{pmatrix} 3 & -4 \\ 4 & 3 \end{pmatrix}, \qquad \rho_L(B) = \begin{pmatrix} 1 & 2 \\ -2 & 1 \end{pmatrix}.
$$

**Multiplicativity.** The product of the two matrices reproduces the product computed in components,

$$
\rho_L(A)\rho_L(B) = \begin{pmatrix} 3 & -4 \\ 4 & 3 \end{pmatrix}\begin{pmatrix} 1 & 2 \\ -2 & 1 \end{pmatrix} = \begin{pmatrix} 11 & 2 \\ -2 & 11 \end{pmatrix} = \rho_L(AB),
$$

the matrix of $AB = 11-2i$.

**The determinant is the norm.** Each matrix has determinant equal to the norm of its element,

$$
\det \rho_L(A) = 3\cdot 3 - (-4)\cdot 4 = 25 = N(A), \qquad \det \rho_L(B) = 1\cdot 1 - 2\cdot(-2) = 5 = N(B),
$$

so multiplicativity of the determinant is the multiplicativity $N(AB) = N(A)N(B)$ on the worked pair.

**Transposition is conjugation.** The transpose of the matrix of $A$ is the matrix of $\bar{A}$:

$$
\rho_L(A)^{\mathsf{T}} = \begin{pmatrix} 3 & 4 \\ -4 & 3 \end{pmatrix} = \rho_L(3-4i) = \rho_L(\bar{A}),
$$

and likewise $\rho_L(B)^{\mathsf{T}} = \rho_L(\bar{B})$.

## The Galois Action, Worked

The unique nontrivial $\mathbb{R}$-automorphism of $\mathbb{C}$ is complex conjugation, written $\sigma = \bar{\cdot}$, and *Complex Automorphisms and Derivations* and *Galois Theory of ℂ/ℝ* treat its automorphism theory. On the worked elements,

$$
\sigma(A) = \bar{A} = 3-4i, \qquad \sigma(B) = \bar{B} = 1+2i, \qquad \sigma(AB) = \overline{11-2i} = 11+2i .
$$

The automorphism property is exhibited by

$$
\sigma(A)\sigma(B) = (3-4i)(1+2i) = 3+6i-4i-8i^2 = 11+2i = \sigma(AB),
$$

and the norm is preserved, $N(\sigma(A)) = 25 = N(A)$. The fixed points are exactly the real axis: $\sigma(A) = A$ would require $4 = 0$, so $A$ is moved; $\sigma(3) = 3$ and $\sigma$ fixes every real number. The action is not $\mathbb{C}$-linear: $\sigma(i\cdot 1) = -i$ while $i\,\sigma(1) = i$, so $\sigma$ conjugates the scalar $i$, which is the concrete form of the conjugate-linearity of complex conjugation over $\mathbb{C}$.

## Summary

The article exhibits the structures of the complex algebra on the elements $A = 3+4i$ and $B = 1-2i$. Their product is $AB = 11-2i$ and their square norms are $N(A) = 25$, $N(B) = 5$, $N(AB) = 125$, so the norm is multiplicative on the worked pair. The identity and complex conjugation are the two involutions; conjugation sends $A$ to $3-4i$ and $B$ to $1+2i$, is an involution and an algebra automorphism, and fixes exactly the real axis while negating the imaginary axis.

The eigencomponents of conjugation are $A_+ = 3 \in \mathbb{R}_{\mathbb{C}}$ and $A_- = 4i \in i\mathbb{R}_{\mathbb{C}}$, with $N(A_+)+N(A_-) = N(A)$; the product $(4i)(-2i) = 8$ is real and shows that the imaginary subspace is not closed. The unit criterion and the inverse formula belong to the topology layer and are developed, with the worked instances, in the companion article *Complex Norm and Invertibility*. The matrix model carries the same data: $\rho_L(A) = \begin{pmatrix} 3 & -4 \\ 4 & 3 \end{pmatrix}$ and $\rho_L(B) = \begin{pmatrix} 1 & 2 \\ -2 & 1 \end{pmatrix}$ multiply to $\rho_L(AB)$, their determinants $25$ and $5$ are the norms of the elements, and $\rho_L(A)^{\mathsf{T}} = \rho_L(\bar{A})$ is the transpose relation. The Galois action $\sigma = \bar{\cdot}$ preserves the product and the norm on the worked elements and is conjugate-linear over $\mathbb{C}$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{C}$ | the complex algebra, basis $1$, $i$, $i^2 = -1$ |
| $A = 3+4i$, $B = 1-2i$ | the two worked elements |
| $\operatorname{id}, \bar{\cdot}$ | the identity and complex conjugation |
| $\sigma = \bar{\cdot}$ | the nontrivial $\mathbb{R}$-automorphism, the Galois action |
| $A_\pm = \tfrac12(A \pm \bar{A})$ | the eigencomponents of conjugation |
| $\mathbb{R}_{\mathbb{C}}, i\mathbb{R}_{\mathbb{C}}$ | the real and imaginary subspaces |
| $N(A) = A\bar{A} = a^2+a'^2$ | the norm |
| $\rho_L(A) = aI + a'J$ | the Cayley matrix of multiplication by $A$, the $2\times2$ matrix model |

## Further Reading

- Carl Friedrich Gauss, *Theoria residuorum biquadraticorum, Commentatio secunda* (Göttingen, 1831), for the geometry of the plane and worked computational examples.
- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the origin of the worked multiplication rules.
- Israel Nathan Herstein, *Topics in Algebra*, 2nd edition (Wiley, 1975), for elementary computational practice with complex numbers and field automorphisms.
- Walter Rudin, *Real and Complex Analysis*, 3rd edition (McGraw-Hill, 1987), for the norm and its multiplicativity.
