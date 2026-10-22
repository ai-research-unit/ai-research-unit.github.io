
# __Complex Two-Component Element Representation__

## Introduction

This article presents the **two-component realization** of the complex algebra: a complex number read off as its pair of real coordinates. It is the smallest realization in the family. The word *representation* is used here in the sense of a concrete realization of the algebra by computable objects and not in the technical sense of an algebra acting on a vector space: the two-component reading supplies the coordinate space, the column and the row, the component form of the product with its rotation matrix on the unit circle, the conjugation in coordinates, the two distinguished subspaces and the norm; the operator so obtained is developed in *Complex Regular Element Representation*.

The conventions are those of *Complex Algebra*: basis $1$, $i$ with $i^2 = -1$, a general element $Q = q + i q'$ with $q,q' \in \mathbb{R}$, involution $\bar Q = q - i q'$, norm $\langle Q\rangle_{*} = q^2+q'^2$. This article has two real coordinates and no complex coefficient field; the economy is the whole content of the two-dimensional case.

## The Coefficient Space

**Definition.** The **two-component vector** of a complex number $Q = q + i q'$ is the ordered pair

$$
Q^\mu = (Q^0, Q^1) = (q, q') \in \mathbb{R}^2,
$$

with $Q^0 = q$ the **real component** and $Q^1 = q'$ the **imaginary component**. The two components are **real** numbers: the realization carries two real coordinates, equivalently one complex coordinate, and it is the direct reading of the developed form of $Q$.

**Proposition.** The map $Q \mapsto (Q^0, Q^1)$ is an $\mathbb{R}$-linear isomorphism $\mathbb{C} \to \mathbb{R}^2$. Consequently the coefficient space has real dimension $2$ and complex dimension $1$.

**Proof.** The map sends the basis $1, i$ to the standard basis $(1,0)$, $(0,1)$ of $\mathbb{R}^2$ and is extended by linearity; it is bijective on bases.

The coefficient space $\mathbb{R}^2$ is **not** a complex vector space in a canonical way until the complex structure $J$ is imposed, and it is not the module $V$ of the representation theory, which is one-dimensional over $\mathbb{C}$; the two-component space is the algebra itself, read in real coordinates. Here the single complex coordinate has been split into its two real parts.

### The Two Components and Their Real Parts

The two components are $Q^0 = q$ and $Q^1 = q'$, both real; there is no further split into real and imaginary parts, because the split has already been performed. The two distinguished subspaces are read directly from the components:

- the real subspace $\mathbb{R}_{\mathbb{C}}$ is the set of pairs with $Q^1 = 0$;
- the imaginary subspace $i\mathbb{R}_{\mathbb{C}}$ is the set of pairs with $Q^0 = 0$.

The norm does not decompose further: it is the positive-definite expression $(Q^0)^2 + (Q^1)^2$ in the two real coordinates.

## The Column and the Row

**Definition.** The **column** of $Q$ is the $2 \times 1$ matrix

$$
Q = \begin{pmatrix} Q^0 \\ Q^1 \end{pmatrix} = \begin{pmatrix} q \\ q' \end{pmatrix},
$$

and the **row** of $Q$ is its transpose

$$
Q^{\mathsf{T}} = \begin{pmatrix} Q^0 & Q^1 \end{pmatrix} = \begin{pmatrix} q & q' \end{pmatrix}.
$$

The column is the transcribed form of the pair, convenient because the product is bilinear. For a fixed $Q$, the map $Q_1 \mapsto QQ_1$ sends coefficients linearly to coefficients, so it is an $\mathbb{R}$-linear endomorphism of the coefficient space, and in the column convention it is written as a $2 \times 2$ matrix,

$$
Q Q_1 \longleftrightarrow \mathsf{M}_2(Q)\, Q_1,
$$

where $\mathsf{M}_2(Q) = \begin{pmatrix} q & -q' \\ q' & q \end{pmatrix}$ is the Cayley matrix of *Complex Regular Element Representation*, each entry of which is a single component of $Q$ carrying a sign. The present article records only that the product rule admits this reading; the operator is developed there.

**Remark (the row is the dual).** The row $Q^{\mathsf{T}}$ is the element of the dual space associated with $Q$ under the standard pairing, and it is not a further realization of the algebra. Because the algebra is commutative and the ground field is $\mathbb{R}$, the left and right actions coincide and the distinction between the column picture and the row picture carries no information: the row is the transpose and nothing more. The involution acts on the two real components without a coefficient field to conjugate.

## Multiplication in Two-Component Form

**Proposition (the product in components).** Let $Q = (q,q')$ and $Q_1 = (q_1,q'_1)$. Then the product has components

$$
(QQ_1)^0 = q q_1 - q' q'_1, \qquad (QQ_1)^1 = q q'_1 + q' q_1 .
$$

**Proof.** Expand $QQ_1 = (q+i q')(q_1+i q'_1) = q q_1 + i q q'_1 + i q' q_1 + i^2 q' q'_1 = (q q_1-q' q'_1) + (q q'_1+q' q_1)i$.

The product is the sum of a scalar part $q q_1$ and a rotation part, and it is **symmetric** in the two factors:

$$
QQ_1 = Q_1Q, \qquad (q q_1-q' q'_1, q q'_1+q' q_1) = (q_1 q-q'_1 q', q_1 q'+q'_1 q),
$$

so there is no antisymmetric term and no commutator. The two-component product has no such term, and its absence is the commutativity of the field.

**Example.** For $Q = (3,4)$ and $Q_1 = (1,-2)$ the product is $(3\cdot 1 - 4\cdot(-2),\, 3\cdot(-2)+4\cdot 1) = (11,-2)$, the element $11-2i$; the reversed order gives the same pair.

### The Multiplication Table of the Basis

The product formula is the row-by-row reading of the multiplication table of the basis. The entry in row $\mu$ and column $\nu$ is the product $e_\mu e_\nu$.

| $e_\mu \backslash e_\nu$ | $1$ | $i$ |
|---|---|---|
| $1$ | $1$ | $i$ |
| $i$ | $i$ | $-1$ |

The first row and the first column reproduce the basis, since $1$ is the identity. The corner $\mu = \nu = 1$ carries $-1$, which is why the scalar component of a product is $q q_1-q' q'_1$, and the off-diagonal entries carry $i$, which is why the imaginary component is $q q'_1+q' q_1$. The table is symmetric about the diagonal, $e_\mu e_\nu = e_\nu e_\mu$. The same table read as a map on the column space is the regular matrix of *Complex Regular Element Representation*.

### The Rotation Matrix

On the unit circle the component product becomes a rotation. A unit has the polar form $u = \cos\theta + i\sin\theta$, so its two components are $(u^0,u^1) = (\cos\theta,\sin\theta)$ and its matrix is

$$
\mathsf{M}_2(u) = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix} = R_\theta,
$$

which is the **rotation matrix** of the plane through the angle $\theta$. It is orthogonal, $R_\theta^{\mathsf{T}}R_\theta = I$, and of determinant $1$, and the unit criterion $\langle u\rangle_{*} = 1$ is exactly the statement $\det R_\theta = 1$. For a general element $Q = q+i q' = r u$ with $r = \sqrt{\langle Q\rangle_{*}}$ and $u = Q/\sqrt{\langle Q\rangle_{*}}$, the component product is the matrix

$$
\mathsf{M}_2(Q) = rR_\theta,
$$

the product of the positive scale $r$ and the rotation $R_\theta$; the matrix is thus the conformal matrix of scaling by $r$ and rotating by $\theta$, and the polar decomposition $Q = ru$ is the factorisation of the matrix into its scale and its rotation. The operator is developed in *Complex Regular Element Representation*; here it is recorded as the matrix form of the component product on the two coordinates.

## The Conjugation in Coordinates

The complex algebra carries one nontrivial involution, complex conjugation. In coordinates it fixes the real component and negates the imaginary one.

**Proposition (conjugation in coordinates).** For $Q = (q,q')$,

$$
(\bar Q)^\mu = (Q^0, -Q^1) = (q, -q').
$$

**Proof.** $\bar Q = \overline{q+i q'} = q-i q'$, whose components are $(q,-q')$.

The map $(q,q') \mapsto (q,-q')$ is the reflection of the plane in the real axis, and it is an involution, since applying it twice returns $(q,q')$. Its matrix is $\operatorname{diag}(1,-1)$, the coordinate form of the transpose relation $\mathsf{M}_2(Q)^{\mathsf{T}} = \mathsf{M}_2(\bar Q)$ of *Complex Regular Element Representation*.

## The Two Distinguished Subspaces

Each subspace of the involution is a coordinate condition, and the two conditions are the simplest possible.

**Definition.** The two **distinguished subspaces** are

$$
\mathbb{R}_{\mathbb{C}} = \{ Q : \bar Q = Q \}, \qquad i\mathbb{R}_{\mathbb{C}} = \{ Q : \bar Q = -Q \}.
$$

**Proposition (coordinate conditions).** In terms of the two-component vector,

| subspace | coordinate condition | real basis | $\dim_{\mathbb{R}}$ |
|---|---|---|---|
| $\mathbb{R}_{\mathbb{C}}$ | $Q^1 = 0$ | $1$ | $1$ |
| $i\mathbb{R}_{\mathbb{C}}$ | $Q^0 = 0$ | $i$ | $1$ |

**Proof.** The condition $\bar Q = Q$ is $q' = 0$, and $\bar Q = -Q$ is $q = 0$; the two sets are the coordinate axes, of dimension one each.

The two conditions partition the two real coordinates, so the decomposition $\mathbb{C} = \mathbb{R}_{\mathbb{C}} \oplus i\mathbb{R}_{\mathbb{C}}$ is the splitting of the pair $(q,q')$ into its two components. The two subspaces are the two coordinate blocks $\langle 1 \rangle$ and $\langle i \rangle$ of *Complexoid Subspaces*. In the four-vector realization the remarkable subspaces are the coordinate conditions on four complex components, some of them mixing the real and imaginary parts; here there are two conditions on two real components, and no mixing is possible.

## The Norm

**Definition.** The **norm** of a complex number is

$$
\langle Q\rangle_{*} = Q\bar Q = (Q^0)^2 + (Q^1)^2 = q^2 + q'^2 \in \mathbb{R}.
$$

In two-component form the norm has **both signs positive**.

**Proposition.** For every $Q$, $Q\bar Q = (Q^0)^2 + (Q^1)^2$.

**Proof.** $(q+i q')(q-i q') = q^2 - (i q')^2 = q^2 + q'^2$.

The norm is a positive-definite quadratic form on the coefficient space $\mathbb{R}^2$, of signature $(2,0)$. There is no indefinite form on the coefficient space here, and no restriction can produce one, because there is no central scalar imaginary separate from the algebra.

### The Two Signs

The phrase "the two signs" refers to the two restrictions of the norm to the two distinguished subspaces. On the real subspace, $Q = (q,0)$, the norm restricts to

$$
\langle Q\rangle_{*} = q^2,
$$

and on the imaginary subspace, $Q = (0,q')$, it restricts to

$$
\langle Q\rangle_{*} = q'^2.
$$

Both restrictions are **positive definite**, of signature $(1,0)$, and the form is $(+,+)$ on the coordinate space. The two signs coincide and the two signatures agree: the opposite-sign pattern of an indefinite algebra does not occur, and the definiteness of the form is why the complex algebra has no zero divisors and no null cone.

### The Unit Criterion in Coordinates

**Theorem.** A complex number $Q = (q,q')$ is invertible if and only if $(q,q') \neq (0,0)$, equivalently if and only if $\langle Q\rangle_{*} \neq 0$, and then

$$
Q^{-1} = \frac{\bar Q}{\langle Q\rangle_{*}}, \qquad (Q^{-1})^\mu = \left( \frac{Q^0}{\langle Q\rangle_{*}}, \, -\frac{Q^1}{\langle Q\rangle_{*}} \right), \qquad \langle Q\rangle_{*} = q^2+q'^2 .
$$

**Proof.** The criterion and the formula are those of *Complex Norm and Invertibility*; in coordinates the inverse of the pair $(q,q')$ is $(q,-q')/(q^2+q'^2)$.

**Example.** For $Q = (3,4)$ the norm is $\langle Q\rangle_{*} = 9+16 = 25$, so $Q$ is a unit and $Q^{-1} = (3,-4)/25 = (0.12, -0.16)$. The product check $(3,4)(0.12,-0.16) = (0.36+0.64, -0.48+0.48) = (1,0) = 1$ is exact.

## Summary

The two-component realization reads a complex number $Q = q+i q'$ as its pair of real coordinates $(Q^0,Q^1) = (q,q')$, an $\mathbb{R}$-linear isomorphism onto $\mathbb{R}^2$. The column is the pair written vertically, the row is its dual by transposition, and because the algebra is commutative the left and right actions coincide and the row carries no separate right action.

The product in components is $(q q_1-q' q'_1, q q'_1+q' q_1)$, the multiplication table of the basis being symmetric about the diagonal, and there is no antisymmetric term: its absence is the commutativity of the field. On the unit circle the component product is the rotation matrix $R_\theta = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$, and a general element has $\mathsf{M}_2(Q) = rR_\theta$, the scale times the rotation. The conjugation acts by $(q,q') \mapsto (q,-q')$, a reflection of the plane; its fixed subspace is the real axis $Q^1 = 0$ and its anti-fixed subspace the imaginary axis $Q^0 = 0$, each of real dimension one.

The norm is $\langle Q\rangle_{*} = (Q^0)^2 + (Q^1)^2$, with both signs positive. Its restrictions to the two subspaces are $q^2$ and $q'^2$, both positive definite, so the form is definite. The invertibility criterion is $(q,q') \neq (0,0)$, and the inverse in coordinates is $(q,-q')/(q^2+q'^2)$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{C}$ | the complex algebra, basis $1$, $i$, $i^2 = -1$ |
| $Q = q+i q'$ | a complex number |
| $Q^\mu = (Q^0, Q^1) = (q,q')$ | the two-component vector, both components real |
| $Q^0 = q$, $Q^1 = q'$ | real and imaginary components |
| $Q = \begin{pmatrix} Q^0 \\ Q^1 \end{pmatrix}$, $Q^{\mathsf{T}}$ | the column and the row |
| $(QQ_1)^\mu = (q q_1-q' q'_1, q q'_1+q' q_1)$ | the product in components |
| $\mathsf{M}_2(Q) = qI + q'J$ | the regular matrix acting on the column |
| $R_\theta = \mathsf{M}_2(u)$ | the rotation matrix of a unit $u = \cos\theta + i\sin\theta$ |
| $\bar Q \leftrightarrow (q,-q')$ | conjugation in coordinates |
| $\mathbb{R}_{\mathbb{C}}, i\mathbb{R}_{\mathbb{C}}$ | real axis $Q^1=0$ and imaginary axis $Q^0=0$ |
| $\langle Q\rangle_{*} = (Q^0)^2+(Q^1)^2 = q^2+q'^2$ | the norm, signature $(2,0)$ |
| $Q^{-1} = (q,-q')/\langle Q\rangle_{*}$ | the inverse in coordinates |

## Further Reading

- Carl Friedrich Gauss, *Theoria residuorum biquadraticorum, Commentatio secunda* (Göttingen, 1831), for the representation of a complex number by two real coordinates.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd edition (Cambridge University Press, 2001), for the quadratic forms and signatures attached to a real algebra in coordinates.
- Tristan Needham, *Visual Complex Analysis* (Oxford University Press, 1997), for the rotation-and-scaling reading of the component product.
