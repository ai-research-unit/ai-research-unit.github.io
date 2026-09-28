
# __Complex Two-Component Element Representation__

## Introduction

This article presents the **two-component realization** of the complex algebra: a complex number read off as its pair of real coordinates. It is the smallest realization in the tensor family, and it is the two-dimensional analogue of the four-vector realization of the biquaternion algebra $\mathbb{B}$. The word *representation* is used here in the sense of a concrete realization of the algebra by computable objects and not in the technical sense of an algebra acting on a vector space: the two-component reading supplies the coordinate space, the column and the row, the component form of the product with its rotation matrix on the unit circle, the conjugation in coordinates, the two distinguished subspaces and the norm; the operator so obtained is developed in *Complex Regular Element Representation*.

The conventions are those of *Complex Algebra*: basis $1$, $i$ with $i^2 = -1$, a general element $Z = a + i b$ with $a,b \in \mathbb{R}$, involution $\bar{Z} = a - i b$, norm $N(Z) = a^2+b^2$. Where the biquaternion article has four complex coordinates $Q^\mu$ and eight real coordinates, this article has two real coordinates and no complex coefficient field; the economy is the whole content of the two-dimensional case.

## The Coefficient Space

**Definition.** The **two-component vector** of a complex number $Z = a + i b$ is the ordered pair

$$
Z^\mu = (Z^0, Z^1) = (a, b) \in \mathbb{R}^2,
$$

with $Z^0 = a$ the **real component** and $Z^1 = b$ the **imaginary component**. The two components are **real** numbers: the realization carries two real coordinates, equivalently one complex coordinate, and it is the direct reading of the developed form of $Z$.

**Proposition.** The map $Z \mapsto (Z^0, Z^1)$ is an $\mathbb{R}$-linear isomorphism $\mathbb{C} \to \mathbb{R}^2$. Consequently the coefficient space has real dimension $2$ and complex dimension $1$.

**Proof.** The map sends the basis $1, i$ to the standard basis $(1,0)$, $(0,1)$ of $\mathbb{R}^2$ and is extended by linearity; it is bijective on bases.

The coefficient space $\mathbb{R}^2$ is **not** a complex vector space in a canonical way until the complex structure $J$ is imposed, and it is not the module $V$ of the representation theory, which is one-dimensional over $\mathbb{C}$; the two-component space is the algebra itself, read in real coordinates. This is the first difference from the biquaternion four-vector, whose coefficient space is $\mathbb{C}^4$: there each of the four components is itself a complex number, while here the single complex coordinate has been split into its two real parts.

### The Two Components and Their Real Parts

The two components are $Z^0 = a$ and $Z^1 = b$, both real; there is no further split into real and imaginary parts, because the split has already been performed. The two distinguished subspaces are read directly from the components:

- the real subspace $\mathbb{R}_{\mathbb{C}}$ is the set of pairs with $Z^1 = 0$;
- the imaginary subspace $i\mathbb{R}_{\mathbb{C}}$ is the set of pairs with $Z^0 = 0$.

The norm does not decompose further: it is the positive-definite expression $(Z^0)^2 + (Z^1)^2$ in the two real coordinates, in contrast with the biquaternion form, whose real and imaginary parts are $\sum_\mu ((a^\mu)^2 - (b^\mu)^2)$ and $2\sum_\mu a^\mu b^\mu$ in eight real coordinates.

## The Column and the Row

**Definition.** The **column** of $Z$ is the $2 \times 1$ matrix

$$
Z = \begin{pmatrix} Z^0 \\ Z^1 \end{pmatrix} = \begin{pmatrix} a \\ b \end{pmatrix},
$$

and the **row** of $Z$ is its transpose

$$
Z^{\mathsf{T}} = \begin{pmatrix} Z^0 & Z^1 \end{pmatrix} = \begin{pmatrix} a & b \end{pmatrix}.
$$

The column is the transcribed form of the pair, convenient because the product is bilinear. For a fixed $Z$, the map $W \mapsto ZW$ sends coefficients linearly to coefficients, so it is an $\mathbb{R}$-linear endomorphism of the coefficient space, and in the column convention it is written as a $2 \times 2$ matrix,

$$
Z W \longleftrightarrow \rho_L(Z)\, W,
$$

where $\rho_L(Z) = \begin{pmatrix} a & -b \\ b & a \end{pmatrix}$ is the Cayley matrix of *Complex Regular Element Representation*, each entry of which is a single component of $Z$ carrying a sign. The present article records only that the product rule admits this reading; the operator is developed there.

**Remark (the row is the dual).** The row $Z^{\mathsf{T}}$ is the element of the dual space associated with $Z$ under the standard pairing, and it is not a further realization of the algebra. Because the algebra is commutative and the ground field is $\mathbb{R}$, the left and right actions coincide and the distinction between the column picture and the row picture carries no information: the row is the transpose and nothing more. This is the placement, in two dimensions, of the biquaternion remark that the row carries the right action and is related to the column by transposition dressed with quaternion conjugation; the dressing is absent here because the involution acts on the two real components without a coefficient field to conjugate.

## Multiplication in Two-Component Form

**Proposition (the product in components).** Let $Z = (a,b)$ and $W = (c,d)$. Then the product has components

$$
(ZW)^0 = a c - b d, \qquad (ZW)^1 = a d + b c .
$$

**Proof.** Expand $ZW = (a+i b)(c+i d) = a c + i a d + i b c + i^2 b c = (a c-b d) + (a d+b c)i$.

The product is the sum of a scalar part $a c$ and a rotation part, and it is **symmetric** in the two factors:

$$
ZW = WZ, \qquad (a c-b d, a d+b c) = (c a-d b, c b+d a),
$$

so there is no antisymmetric term and no commutator. In the four-vector form of the biquaternions the scalar component is $Q^0R^0 - \sum_k Q^kR^k$ and each vector component carries a Levi-Civita term $2\sum_{j,k}\epsilon^{ijk}Q^jR^k$, which is the only trace of non-commutativity; here the two-component product has no such term, and its absence is the commutativity of the field.

**Example.** For $Z = (3,4)$ and $W = (1,-2)$ the product is $(3\cdot 1 - 4\cdot(-2),\, 3\cdot(-2)+4\cdot 1) = (11,-2)$, the element $11-2i$; the reversed order gives the same pair.

### The Multiplication Table of the Basis

The product formula is the row-by-row reading of the multiplication table of the basis. The entry in row $\mu$ and column $\nu$ is the product $e_\mu e_\nu$.

| $e_\mu \backslash e_\nu$ | $1$ | $i$ |
|---|---|---|
| $1$ | $1$ | $i$ |
| $i$ | $i$ | $-1$ |

The first row and the first column reproduce the basis, since $1$ is the identity. The corner $\mu = \nu = 1$ carries $-1$, which is why the scalar component of a product is $a c-b d$, and the off-diagonal entries carry $i$, which is why the imaginary component is $a d+b c$. The table is symmetric about the diagonal, $e_\mu e_\nu = e_\nu e_\mu$, whereas the quaternion table of the four-vector article is skew off the diagonal. The same table read as a map on the column space is the regular matrix of *Complex Regular Element Representation*.

### The Rotation Matrix

On the unit circle the component product becomes a rotation. A unit has the polar form $u = \cos\theta + i\sin\theta$, so its two components are $(u^0,u^1) = (\cos\theta,\sin\theta)$ and its matrix is

$$
\rho_L(u) = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix} = R_\theta,
$$

which is the **rotation matrix** of the plane through the angle $\theta$. It is orthogonal, $R_\theta^{\mathsf{T}}R_\theta = I$, and of determinant $1$, and the unit criterion $N(u) = 1$ is exactly the statement $\det R_\theta = 1$. For a general element $Z = a+i b = r u$ with $r = |Z|$ and $u = Z/|Z|$, the component product is the matrix

$$
\rho_L(Z) = rR_\theta,
$$

the product of the positive scale $r$ and the rotation $R_\theta$; the matrix is thus the conformal matrix of scaling by $r$ and rotating by $\theta$, and the polar decomposition $Z = ru$ is the factorisation of the matrix into its scale and its rotation. The operator is developed in *Complex Regular Element Representation*; here it is recorded as the matrix form of the component product on the two coordinates.

## The Conjugation in Coordinates

The complex algebra carries one nontrivial involution, complex conjugation. In coordinates it fixes the real component and negates the imaginary one.

**Proposition (conjugation in coordinates).** For $Z = (a,b)$,

$$
(\bar{Z})^\mu = (Z^0, -Z^1) = (a, -b).
$$

**Proof.** $\bar{Z} = \overline{a+i b} = a-i b$, whose components are $(a,-b)$.

The map $(a,b) \mapsto (a,-b)$ is the reflection of the plane in the real axis, and it is an involution, since applying it twice returns $(a,b)$. Its matrix is $\operatorname{diag}(1,-1)$, the coordinate form of the transpose relation $\rho_L(Z)^{\mathsf{T}} = \rho_L(\bar{Z})$ of *Complex Regular Element Representation*.

## The Two Distinguished Subspaces

Each subspace of the involution is a coordinate condition, and the two conditions are the simplest possible.

**Definition.** The two **distinguished subspaces** are

$$
\mathbb{R}_{\mathbb{C}} = \{ Z : \bar{Z} = Z \}, \qquad i\mathbb{R}_{\mathbb{C}} = \{ Z : \bar{Z} = -Z \}.
$$

**Proposition (coordinate conditions).** In terms of the two-component vector,

| subspace | coordinate condition | real basis | $\dim_{\mathbb{R}}$ |
|---|---|---|---|
| $\mathbb{R}_{\mathbb{C}}$ | $Z^1 = 0$ | $1$ | $1$ |
| $i\mathbb{R}_{\mathbb{C}}$ | $Z^0 = 0$ | $i$ | $1$ |

**Proof.** The condition $\bar{Z} = Z$ is $b = 0$, and $\bar{Z} = -Z$ is $a = 0$; the two sets are the coordinate axes, of dimension one each.

The two conditions partition the two real coordinates, so the decomposition $\mathbb{C} = \mathbb{R}_{\mathbb{C}} \oplus i\mathbb{R}_{\mathbb{C}}$ is the splitting of the pair $(a,b)$ into its two components. The two subspaces are the two coordinate blocks $\langle 1 \rangle$ and $\langle i \rangle$ of *Complex Subspaces*. In the four-vector realization the six subspaces are the coordinate conditions on four complex components, some of them mixing the real and imaginary parts; here there are two conditions on two real components, and no mixing is possible.

## The Norm

**Definition.** The **norm** of a complex number is

$$
N(Z) = Z\bar{Z} = (Z^0)^2 + (Z^1)^2 = a^2 + b^2 \in \mathbb{R}.
$$

In two-component form the norm has **both signs positive**.

**Proposition.** For every $Z$, $Z\bar{Z} = (Z^0)^2 + (Z^1)^2$.

**Proof.** $(a+i b)(a-i b) = a^2 - (i b)^2 = a^2 + b^2$.

The norm is a positive-definite quadratic form on the coefficient space $\mathbb{R}^2$, of signature $(2,0)$. This is a genuine difference from the biquaternion norm, which is a complex quadratic form on $\mathbb{C}^4$ with all four signs positive but which restricts to real forms of opposite signatures on the two sectors. There is no indefinite form on the coefficient space here, and no restriction can produce one, because there is no central scalar imaginary separate from the algebra.

### The Two Signs

The phrase "the two signs" refers to the two restrictions of the norm to the two distinguished subspaces. On the real subspace, $Z = (a,0)$, the norm restricts to

$$
N(Z) = a^2,
$$

and on the imaginary subspace, $Z = (0,b)$, it restricts to

$$
N(Z) = b^2.
$$

Both restrictions are **positive definite**, of signature $(1,0)$, and the form is $(+,+)$ on the coordinate space. In the biquaternion algebra the two corresponding restrictions have opposite signatures, $(1,3)$ and $(3,1)$, because the sectors there are exchanged by multiplication by the central imaginary, which reverses the sign of the norm. Here the two signs coincide and the two signatures agree: the opposite-sign pattern of the indefinite algebra does not occur, and the definiteness of the form is why the complex algebra has no zero divisors and no null cone.

### The Unit Criterion in Coordinates

**Theorem.** A complex number $Z = (a,b)$ is invertible if and only if $(a,b) \neq (0,0)$, equivalently if and only if $N(Z) \neq 0$, and then

$$
Z^{-1} = \frac{\bar{Z}}{N(Z)}, \qquad (Z^{-1})^\mu = \left( \frac{Z^0}{N}, \, -\frac{Z^1}{N} \right), \qquad N = N(Z) = a^2+b^2 .
$$

**Proof.** The criterion and the formula are those of *Complex Norm and Invertibility*; in coordinates the inverse of the pair $(a,b)$ is $(a,-b)/(a^2+b^2)$.

**Example.** For $Z = (3,4)$ the norm is $N = 9+16 = 25$, so $Z$ is a unit and $Z^{-1} = (3,-4)/25 = (0.12, -0.16)$. The product check $(3,4)(0.12,-0.16) = (0.36+0.64, -0.48+0.48) = (1,0) = 1$ is exact.

## Summary

The two-component realization reads a complex number $Z = a+i b$ as its pair of real coordinates $(Z^0,Z^1) = (a,b)$, an $\mathbb{R}$-linear isomorphism onto $\mathbb{R}^2$; it is the two-dimensional analogue of the four-vector realization of the biquaternion algebra. The column is the pair written vertically, the row is its dual by transposition, and because the algebra is commutative the left and right actions coincide and the row carries no separate right action.

The product in components is $(a c-b d, a d+b c)$, the multiplication table of the basis being symmetric about the diagonal, and there is no Levi-Civita term: the antisymmetric part of the biquaternion product has no analogue, and its absence is the commutativity of the field. On the unit circle the component product is the rotation matrix $R_\theta = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$, and a general element has $\rho_L(Z) = rR_\theta$, the scale times the rotation. The conjugation acts by $(a,b) \mapsto (a,-b)$, a reflection of the plane; its fixed subspace is the real axis $Z^1 = 0$ and its anti-fixed subspace the imaginary axis $Z^0 = 0$, each of real dimension one.

The norm is $N(Z) = (Z^0)^2 + (Z^1)^2$, with both signs positive. Its restrictions to the two subspaces are $a^2$ and $b^2$, both positive definite, so the opposite signatures of the biquaternion sectors do not occur and the form is definite. The invertibility criterion is $(a,b) \neq (0,0)$, and the inverse in coordinates is $(a,-b)/(a^2+b^2)$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{C}$ | the complex algebra, basis $1$, $i$, $i^2 = -1$ |
| $Z = a+i b$ | a complex number |
| $Z^\mu = (Z^0, Z^1) = (a,b)$ | the two-component vector, both components real |
| $Z^0 = a$, $Z^1 = b$ | real and imaginary components |
| $Z = \begin{pmatrix} Z^0 \\ Z^1 \end{pmatrix}$, $Z^{\mathsf{T}}$ | the column and the row |
| $(ZW)^\mu = (a c-b d, a d+b c)$ | the product in components |
| $\rho_L(Z) = aI + bJ$ | the regular matrix acting on the column |
| $R_\theta = \rho_L(u)$ | the rotation matrix of a unit $u = \cos\theta + i\sin\theta$ |
| $\bar{Z} \leftrightarrow (a,-b)$ | conjugation in coordinates |
| $\mathbb{R}_{\mathbb{C}}, i\mathbb{R}_{\mathbb{C}}$ | real axis $Z^1=0$ and imaginary axis $Z^0=0$ |
| $N(Z) = (Z^0)^2+(Z^1)^2 = a^2+b^2$ | the norm, signature $(2,0)$ |
| $Z^{-1} = (a,-b)/N$ | the inverse in coordinates |

## Further Reading

- Carl Friedrich Gauss, *Theoria residuorum biquadraticorum, Commentatio secunda* (Göttingen, 1831), for the representation of a complex number by two real coordinates.
- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the coordinate treatment of multiplication.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the coordinate form of multiplication and its conjugations in the hypercomplex case.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd edition (Cambridge University Press, 2001), for the quadratic forms and signatures attached to a real algebra in coordinates.
- Tristan Needham, *Visual Complex Analysis* (Oxford University Press, 1997), for the rotation-and-scaling reading of the component product.
