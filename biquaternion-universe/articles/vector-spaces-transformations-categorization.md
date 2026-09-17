
# __Vector Space Transformations categorization__

## Introduction

This article describes the groups of linear transformations of the simplest vector spaces and modules, organized by the **field or ring of scalars**.

We consider four scalar structures:

- The rational numbers $\mathbb{Q}$.
- The real numbers $\mathbb{R}$.
- The complex numbers $\mathbb{C}$.
- The split complex numbers $\mathbb{D}$.

For each scalar structure, we give the simplest modules over that structure, and describe their groups of linear transformations. We treat the rational line, the real line, the complex plane, the split complex plane, and the quaternions.

We do not use matrices as the primary tool. Instead, we describe each transformation by what it does geometrically: dilatation, rotation, reflection, hyperbolic transformation.

We assume familiarity with modules and linear transformations. No prior knowledge of groups, quadratic forms, or Lie algebras is required.

A word on terminology. We consider only **linear** transformations, that is, transformations that fix the origin. Translations, which move the origin, are not linear and are not part of the groups we discuss.

A word on the scalar structures. The rational numbers $\mathbb{Q}$, the real numbers $\mathbb{R}$, and the complex numbers $\mathbb{C}$ are fields. The split complex numbers $\mathbb{D}$ are a commutative ring with zero divisors, not a field. When we work over $\mathbb{D}$, the theory is similar to the theory over a field, with the caveat that the "general linear group" consists of the transformations whose determinant is a **unit** of $\mathbb{D}$. We indicate where this difference matters.

---

# Part I: The Field $\mathbb{Q}$

In this part, the field of scalars is $\mathbb{Q}$. The modules are rational vector spaces. The linear transformations are $\mathbb{Q}$-linear, and the groups of invertible ones are the general linear groups $GL(n, \mathbb{Q})$.

## 1. The Rational Line $\mathbb{Q}$ over $\mathbb{Q}$

### The space

Let $V = \mathbb{Q}$ be the rational line. It is a one-dimensional rational vector space. A point is a rational number $x$.

### The transformations

A $\mathbb{Q}$-linear transformation $T : \mathbb{Q} \to \mathbb{Q}$ is determined by its value on $1$:

$$
T(x) = \lambda x
$$

for some rational number $\lambda$.

### The geometric interpretation

- If $\lambda > 1$, the transformation **stretches** the line away from the origin.
- If $0 < \lambda < 1$, the transformation **shrinks** the line toward the origin.
- If $\lambda = 1$, the transformation is the **identity**.
- If $\lambda = -1$, the transformation is the **reflection** through the origin.
- If $\lambda < 0$ with $\lambda \neq -1$, the transformation is a reflection followed by a stretch or shrink.

So the linear transformations of the rational line are the **dilatations** and the **reflections** through the origin. In one dimension, there are no rotations. The same geometric description applies as over $\mathbb{R}$, but the allowed scalars are only rational numbers.

### The groups

The group of invertible linear transformations is

$$
GL(1, \mathbb{Q}) = \mathbb{Q}^\times,
$$

the group of nonzero rational numbers under multiplication. It has two connected components: the positive rationals (dilatations) and the negative rationals (reflections composed with dilatations).

The determinant is $\lambda$. The special linear group is

$$
SL(1, \mathbb{Q}) = \{1\},
$$

the trivial group.

## 2. The Rational Plane $\mathbb{Q}^2$ over $\mathbb{Q}$

### The space

Let $V = \mathbb{Q}^2$ be the rational plane. It is a two-dimensional rational vector space. A point is a pair $(x, y)$ of rational numbers.

### The transformations

A $\mathbb{Q}$-linear transformation $T : \mathbb{Q}^2 \to \mathbb{Q}^2$ is determined by its values on the standard basis. In coordinates, it is given by a $2 \times 2$ matrix with rational entries.

### The groups

The group of invertible $\mathbb{Q}$-linear transformations is $GL(2, \mathbb{Q})$, the group of $2 \times 2$ matrices with rational entries whose determinant is nonzero.

The determinant is a rational number. The special linear group $SL(2, \mathbb{Q})$ is the set of transformations with determinant $1$. It is the group of **area-preserving** rational transformations.

The geometric interpretation is analogous to the real case: rotations, dilatations, reflections, and shears are all available, but only with rational parameters.

### Summary over $\mathbb{Q}$

| Notion | Description |
|---|---|
| Scalar structure | Field |
| Modules | Rational vector spaces |
| Invertibility | Nonzero determinant |
| General linear group | $GL(n, \mathbb{Q})$ |
| Special linear group | $SL(n, \mathbb{Q})$ |

---

# Part II: The Field $\mathbb{R}$

In this part, the field of scalars is $\mathbb{R}$. The modules are real vector spaces. The linear transformations are $\mathbb{R}$-linear, and the groups of invertible ones are the general linear groups $GL(n, \mathbb{R})$.

## 3. The Real Line $\mathbb{R}$ over $\mathbb{R}$

### The space

Let $V = \mathbb{R}$ be the real line. It is a one-dimensional real vector space. A point is a real number $x$.

### The transformations

An $\mathbb{R}$-linear transformation $T : \mathbb{R} \to \mathbb{R}$ is determined by its value on $1$:

$$
T(x) = \lambda x
$$

for some real number $\lambda$.

### The geometric interpretation

- If $\lambda > 1$, the transformation **stretches** the line away from the origin.
- If $0 < \lambda < 1$, the transformation **shrinks** the line toward the origin.
- If $\lambda = 1$, the transformation is the **identity**.
- If $\lambda = -1$, the transformation is the **reflection** through the origin.
- If $\lambda < 0$ with $\lambda \neq -1$, the transformation is a reflection followed by a stretch or shrink.

So the linear transformations of the real line are the **dilatations** and the **reflections** through the origin. In one dimension, there are no rotations.

### The groups

The group of invertible linear transformations is

$$
GL(1, \mathbb{R}) = \mathbb{R}^\times,
$$

the group of nonzero real numbers under multiplication. It has two connected components: the positive reals (dilatations) and the negative reals (reflections composed with dilatations).

The determinant is $\lambda$. The special linear group is

$$
SL(1, \mathbb{R}) = \{1\},
$$

the trivial group.

## 4. The Complex Plane $\mathbb{C}$ over $\mathbb{R}$

### The space

Let $V = \mathbb{C}$ be the complex plane, viewed as a **two-dimensional real vector space**. A point is $z = x + iy$, with $x, y \in \mathbb{R}$.

### The transformations

An $\mathbb{R}$-linear transformation $T : \mathbb{C} \to \mathbb{C}$ is determined by its values on the basis $\{1, i\}$. The most general such transformation can be written as

$$
T(z) = \lambda z + \mu \bar{z}
$$

for some complex numbers $\lambda, \mu$.

### The geometric interpretation

The transformation $T(z) = \lambda z$ with $\lambda = re^{i\theta}$ is a **rotation combined with a dilatation**: it rotates the plane by angle $\theta$ and dilates it by a factor of $r$. These are the **complex-linear** transformations, viewed as real-linear transformations.

The transformation $T(z) = \bar{z}$ is the **reflection** across the real axis. This is real-linear but not complex-linear. More generally, if $\mu \neq 0$, the transformation includes a reflection component.

So the $\mathbb{R}$-linear transformations of $\mathbb{C}$ include rotations, dilatations, reflections, and shears, and their compositions.

### The groups

The group of invertible $\mathbb{R}$-linear transformations is $GL(2, \mathbb{R})$. It is four-dimensional.

The determinant is a real number. It measures the factor by which the transformation scales areas, with sign indicating orientation.

The special linear group $SL(2, \mathbb{R})$ is the set of transformations with determinant $1$. These are the **area-preserving** transformations: rotations, shears, and hyperbolic transformations. It is three-dimensional.

Inside $GL(2, \mathbb{R})$, the complex-linear transformations form a subgroup isomorphic to $\mathbb{C}^\times$. Geometrically, this is the group of **rotations-dilatations**: transformations of the form $z \mapsto \lambda z$ with $\lambda \neq 0$.

## 5. The Split Complex Plane $\mathbb{D}$ over $\mathbb{R}$

### The space

Let $V = \mathbb{D}$ be the split complex plane, viewed as a **two-dimensional real vector space** with basis $\{1, e\}$. A general element is

$$
z = a + be, \qquad a, b \in \mathbb{R}.
$$

### The product

The split complex numbers carry a product, defined by the single relation

$$
e^2 = +1.
$$

Combined with bilinearity, this gives

$$
(a + be)(c + de) = (ac + bd) + (ad + bc)e.
$$

The product is associative, commutative, and unital. It is not a division algebra: it has zero divisors.

### The transformations

An $\mathbb{R}$-linear transformation $T : \mathbb{D} \to \mathbb{D}$ is determined by its values on the basis $\{1, e\}$. The most general such transformation is an arbitrary element of $GL(2, \mathbb{R})$ when invertible.

A distinguished family of transformations is the set of maps of the form

$$
T(z) = \lambda z
$$

for $\lambda$ a split complex number. If $\lambda = p + qe$, the matrix in the basis $\{1, e\}$ is

$$
\begin{pmatrix} p & q \\ q & p \end{pmatrix}.
$$

The determinant is $p^2 - q^2$. So the transformation is invertible if and only if $p^2 - q^2 \neq 0$.

### The geometric interpretation

The condition $p^2 - q^2 \neq 0$ means that $(p, q)$ does not lie on the two **isotropic lines** $p = q$ or $p = -q$. These lines divide the plane into four regions, and the group of units has four connected components.

Inside $SL(2, \mathbb{R})$, the family of **hyperbolic transformations**

$$
H_t = \begin{pmatrix} \cosh t & \sinh t \\ \sinh t & \cosh t \end{pmatrix}, \qquad t \in \mathbb{R},
$$

stretches the plane along the line $a = b$ by a factor of $e^t$, and shrinks it along the line $a = -b$ by a factor of $e^{-t}$. The determinant is $\cosh^2 t - \sinh^2 t = 1$, so the area is preserved.

The hyperbolic transformations are the analogues, for the split complex plane, of the rotations for the complex plane. They preserve the **split form** $a^2 - b^2$, not the Euclidean form $a^2 + b^2$.

The set of units with $p^2 - q^2 = 1$ is a **hyperbola** in the $(p, q)$-plane, with two connected components.

### The automorphisms

The automorphisms of the split complex algebra are the linear maps that respect the product. There are exactly two:

- The **identity:** $T(a + be) = a + be$.
- The **conjugation:** $T(a + be) = a - be$.

So the automorphism group is $\{\mathrm{id}, \mathrm{conj}\} \cong \mathbb{Z}/2\mathbb{Z}$.

## 6. The Quaternions $\mathbb{H}$ over $\mathbb{R}$

### The space

Let $V = \mathbb{H}$ be the quaternions, viewed as a **four-dimensional real vector space** with basis $\{1, i, j, k\}$. A general element is

$$
q = a + bi + cj + dk, \qquad a, b, c, d \in \mathbb{R}.
$$

### The product

The quaternions carry a product, defined by the relations

$$
i^2 = j^2 = k^2 = ijk = -1.
$$

The product is associative and unital. It is not commutative. It is a division algebra: every nonzero element has an inverse.

### The transformations

An $\mathbb{R}$-linear transformation $T : \mathbb{H} \to \mathbb{H}$ is determined by its values on the basis $\{1, i, j, k\}$. The most general such transformation is an arbitrary element of $GL(4, \mathbb{R})$ when invertible.

A distinguished family of transformations is the set of maps of the form

$$
T(q) = \lambda q
$$

for $\lambda$ a quaternion. These are the **quaternion-linear** transformations, viewed as real-linear transformations. They form a subgroup of $GL(4, \mathbb{R})$ isomorphic to $\mathbb{H}^\times$, the group of nonzero quaternions under multiplication.

The quaternion-linear transformations preserve the norm $|q|^2 = a^2 + b^2 + c^2 + d^2$, up to a scale factor. The subgroup of norm-preserving quaternion-linear transformations is the group of unit quaternions, isomorphic to $SU(2)$.

### The groups

The group of invertible $\mathbb{R}$-linear transformations is $GL(4, \mathbb{R})$. It is sixteen-dimensional.

The determinant is a real number. The special linear group $SL(4, \mathbb{R})$ is the set of transformations with determinant $1$.

The quaternion-linear transformations form a subgroup isomorphic to $\mathbb{H}^\times$, which is four-dimensional. The norm-preserving ones form $SU(2)$, which is three-dimensional.

---

# Part III: The Field $\mathbb{C}$

In this part, the field of scalars is $\mathbb{C}$. The modules are complex vector spaces. The linear transformations are $\mathbb{C}$-linear, and the groups of invertible ones are the general linear groups $GL(n, \mathbb{C})$.

## 7. The Complex Line $\mathbb{C}$ over $\mathbb{C}$

### The space

Let $V = \mathbb{C}$ be the complex line, viewed as a **one-dimensional complex vector space**. A point is a complex number $z$.

### The transformations

A $\mathbb{C}$-linear transformation $T : \mathbb{C} \to \mathbb{C}$ is determined by its value on $1$:

$$
T(z) = \lambda z
$$

for some complex number $\lambda$.

### The geometric interpretation

Geometrically, the transformation $T(z) = \lambda z$ with $\lambda = re^{i\theta}$ is a **rotation-dilatation**: it rotates the plane by angle $\theta$ and dilates it by a factor of $r$.

The complex-linear transformations of $\mathbb{C}$ are exactly the rotations-dilatations. They preserve angles and orientation.

### The groups

The group of invertible $\mathbb{C}$-linear transformations is

$$
GL(1, \mathbb{C}) = \mathbb{C}^\times,
$$

the group of nonzero complex numbers under multiplication.

The determinant is $\lambda$. Its modulus $|\lambda|$ measures the dilatation factor, and its argument $\arg \lambda$ measures the rotation angle.

The special linear group is

$$
SL(1, \mathbb{C}) = \{1\},
$$

the trivial group.

## 8. The Complex Plane $\mathbb{C}^2$ over $\mathbb{C}$

### The space

Let $V = \mathbb{C}^2$ be the complex plane, viewed as a **two-dimensional complex vector space**. A point is a pair $(z_1, z_2)$ of complex numbers.

As a real vector space, this is four-dimensional. But we view it here as a complex vector space, so its complex dimension is two.

### The transformations

A $\mathbb{C}$-linear transformation $T : \mathbb{C}^2 \to \mathbb{C}^2$ is determined by its values on the standard basis. In coordinates, it is given by a complex $2 \times 2$ matrix.

Geometrically, a $\mathbb{C}$-linear transformation of $\mathbb{C}^2$ is a combination of complex rotations and complex dilatations, applied independently in two complex directions. It is more general than a single rotation-dilatation of the complex line.

### The groups

The group of invertible $\mathbb{C}$-linear transformations is $GL(2, \mathbb{C})$. It is eight-dimensional over $\mathbb{R}$ (four-dimensional over $\mathbb{C}$).

The determinant is a complex number. The special linear group $SL(2, \mathbb{C})$ is the set of transformations with determinant $1$. It is six-dimensional over $\mathbb{R}$ (three-dimensional over $\mathbb{C}$).

The group $GL(2, \mathbb{C})$ contains as subgroups:

- $GL(2, \mathbb{R})$, the transformations with real matrix entries, four-dimensional over $\mathbb{R}$.
- $U(2)$, the unitary transformations, four-dimensional over $\mathbb{R}$.
- $SU(2)$, the unitary transformations with determinant $1$, three-dimensional over $\mathbb{R}$.
- $\mathbb{C}^\times$, the scalar transformations $z \mapsto \lambda z$ with $\lambda \neq 0$, two-dimensional over $\mathbb{R}$.

### Summary for $\mathbb{C}^2$ over $\mathbb{C}$

| Group | Dimension over $\mathbb{R}$ | Description |
|---|---|---|
| $GL(2, \mathbb{C})$ | $8$ | all invertible complex-linear transformations |
| $SL(2, \mathbb{C})$ | $6$ | determinant $1$ |
| $GL(2, \mathbb{R})$ | $4$ | real matrix entries |
| $U(2)$ | $4$ | unitary transformations |
| $SU(2)$ | $3$ | unitary, determinant $1$ |
| $\mathbb{C}^\times$ | $2$ | scalar transformations |

## 9. The Quaternions $\mathbb{H}$ over $\mathbb{C}$

### The space

Let $V = \mathbb{H} \otimes_\mathbb{R} \mathbb{C}$ be the quaternions complexified, also called the **biquaternions**. It is a **four-dimensional complex vector space** with basis $\{1, i, j, k\}$. A general element is

$$
q = a + bi + cj + dk, \qquad a, b, c, d \in \mathbb{C}.
$$

Equivalently, it is the algebra of quaternions with complex coefficients, or the tensor product $\mathbb{H} \otimes \mathbb{C}$.

### The product

The product is defined by the same relations as for the quaternions,

$$
i^2 = j^2 = k^2 = ijk = -1,
$$

with coefficients in $\mathbb{C}$. The product is associative and unital. It is not commutative. It is not a division algebra: it has zero divisors.

As a complex algebra, the biquaternions are isomorphic to the algebra $M_2(\mathbb{C})$ of $2 \times 2$ complex matrices.

### The transformations

A $\mathbb{C}$-linear transformation $T : \mathbb{H} \otimes \mathbb{C} \to \mathbb{H} \otimes \mathbb{C}$ is determined by its values on the basis $\{1, i, j, k\}$. The most general such transformation is an arbitrary element of $GL(4, \mathbb{C})$ when invertible.

A distinguished family of transformations is the set of maps of the form

$$
T(q) = \lambda q
$$

for $\lambda$ a biquaternion. These are the **biquaternion-linear** transformations, viewed as complex-linear transformations.

### The groups

The group of invertible $\mathbb{C}$-linear transformations is $GL(4, \mathbb{C})$. It is sixteen-dimensional over $\mathbb{R}$ (eight-dimensional over $\mathbb{C}$).

The determinant is a complex number. The special linear group $SL(4, \mathbb{C})$ is the set of transformations with determinant $1$.

The biquaternion-linear transformations form a subgroup isomorphic to $(\mathbb{H} \otimes \mathbb{C})^\times$, the group of units of the biquaternions. This subgroup is not the same as the group of invertible complex-linear transformations, because the biquaternions have zero divisors.

---

# Part IV: The Commutative Ring $\mathbb{D}$

In this part, the scalar structure is $\mathbb{D}$, the split complex numbers. The modules are split complex modules. The linear transformations are $\mathbb{D}$-linear, and the groups of invertible ones are the general linear groups $GL(n, \mathbb{D})$.

A word of caution. The split complex numbers are not a field in the strict sense: they are a commutative ring with zero divisors. They do not form a field, because not every nonzero element has an inverse. But they behave like a field in many respects, and the theory of modules over $\mathbb{D}$ is similar to the theory over a field, with the caveat that the "general linear group" consists of the transformations whose determinant is a **unit** of $\mathbb{D}$.

## 10. The Split Complex Line $\mathbb{D}$ over $\mathbb{D}$

### The space

Let $V = \mathbb{D}$ be the split complex line, viewed as a **one-dimensional module over $\mathbb{D}$**. A point is a split complex number $z = a + be$.

### The transformations

A $\mathbb{D}$-linear transformation $T : \mathbb{D} \to \mathbb{D}$ is determined by its value on $1$:

$$
T(z) = \lambda z
$$

for some split complex number $\lambda$.

### The geometric interpretation

If $\lambda = p + qe$, the transformation is multiplication by $\lambda$. In the basis $\{1, e\}$, the matrix is

$$
\begin{pmatrix} p & q \\ q & p \end{pmatrix}.
$$

The determinant is $p^2 - q^2$. The transformation is invertible if and only if $p^2 - q^2$ is a **unit** of $\mathbb{D}$, that is, if and only if $p^2 - q^2 \neq 0$.

Geometrically, the transformation is a **hyperbolic transformation**: it stretches the plane along the line $a = b$ and shrinks it along the line $a = -b$.

### The groups

The group of invertible $\mathbb{D}$-linear transformations is the group of units of $\mathbb{D}$:

$$
GL(1, \mathbb{D}) = \mathbb{D}^\times,
$$

the group of split complex numbers with $p^2 - q^2 \neq 0$.

The determinant is $\lambda = p + qe$. The special linear group is

$$
SL(1, \mathbb{D}) = \{\lambda \in \mathbb{D}^\times : p^2 - q^2 = 1\},
$$

the set of units of norm $1$. Geometrically, this is the **hyperbola** $p^2 - q^2 = 1$, which has two connected components.

## 11. The Split Complex Plane $\mathbb{D}^2$ over $\mathbb{D}$

### The space

Let $V = \mathbb{D}^2$ be the split complex plane, viewed as a **two-dimensional module over $\mathbb{D}$**. A point is a pair $(z_1, z_2)$ of split complex numbers.

### The transformations

A $\mathbb{D}$-linear transformation $T : \mathbb{D}^2 \to \mathbb{D}^2$ is determined by its values on the standard basis. In coordinates, it is given by a $2 \times 2$ matrix with entries in $\mathbb{D}$.

### The groups

The group of invertible $\mathbb{D}$-linear transformations is $GL(2, \mathbb{D})$, the group of $2 \times 2$ matrices with entries in $\mathbb{D}$ whose determinant is a unit of $\mathbb{D}$.

The determinant is a split complex number. The special linear group $SL(2, \mathbb{D})$ is the set of transformations with determinant $1$.

## 12. The Quaternions $\mathbb{H}$ over $\mathbb{D}$

### The space

Let $V = \mathbb{H} \otimes_\mathbb{R} \mathbb{D}$ be the quaternions tensored with the split complex numbers, also called the **split biquaternions**. It is a **four-dimensional $\mathbb{D}$-module** with basis $\{1, i, j, k\}$. A general element is

$$
q = a + bi + cj + dk, \qquad a, b, c, d \in \mathbb{D}.
$$

### The product

The product is defined by the same relations as for the quaternions,

$$
i^2 = j^2 = k^2 = ijk = -1,
$$

with coefficients in $\mathbb{D}$. The product is associative and unital. It is not commutative. It is not a division algebra: it has zero divisors.

As an algebra over $\mathbb{D}$, the split biquaternions are isomorphic to a subalgebra of $M_2(\mathbb{D})$. Equivalently, they are isomorphic to the algebra $M_2(\mathbb{D})$ of $2 \times 2$ matrices with entries in $\mathbb{D}$, when considered as an algebra over $\mathbb{R}$. But over $\mathbb{D}$, the structure is more subtle because $\mathbb{D}$ has zero divisors.

### The transformations

A $\mathbb{D}$-linear transformation $T : \mathbb{H} \otimes \mathbb{D} \to \mathbb{H} \otimes \mathbb{D}$ is determined by its values on the basis $\{1, i, j, k\}$. The most general such transformation is an arbitrary element of $GL(4, \mathbb{D})$ when invertible.

A distinguished family of transformations is the set of maps of the form

$$
T(q) = \lambda q
$$

for $\lambda$ a split biquaternion. These are the **split biquaternion-linear** transformations, viewed as $\mathbb{D}$-linear transformations.

### The groups

The group of invertible $\mathbb{D}$-linear transformations is $GL(4, \mathbb{D})$, the group of $4 \times 4$ matrices with entries in $\mathbb{D}$ whose determinant is a unit of $\mathbb{D}$.

The determinant is a split complex number. The special linear group $SL(4, \mathbb{D})$ is the set of transformations with determinant $1$.

The split biquaternion-linear transformations form a subgroup isomorphic to the group of units of the split biquaternions.

---

# Part V: The General Pattern

## Dilatations, rotations, reflections, hyperbolic transformations

In every dimension and over every scalar structure, the linear transformations of a module can be decomposed into elementary geometric operations:

- **Dilatations:** stretch or shrink uniformly. Present over every scalar structure.
- **Rotations:** rotate around the origin. Present over $\mathbb{Q}$ (in dimension at least 2), over $\mathbb{R}$ (in dimension at least 2), and over $\mathbb{C}$.
- **Hyperbolic transformations:** stretch in one direction and shrink in another. Present over $\mathbb{Q}$ (in dimension at least 2), over $\mathbb{R}$ (in dimension at least 2), and over $\mathbb{D}$.
- **Reflections:** reflect across a line or hyperplane through the origin. Present over every scalar structure.
- **Shears:** stretch in one direction while leaving another fixed. Present over $\mathbb{Q}$, $\mathbb{R}$, and $\mathbb{C}$.

## The scalar structure matters

The choice of scalar structure determines the structure of the transformation group.

- Over $\mathbb{Q}$, the linear transformations of $\mathbb{Q}^n$ form $GL(n, \mathbb{Q})$. The determinant is a rational number. Invertibility requires the determinant to be nonzero.
- Over $\mathbb{R}$, the linear transformations of $\mathbb{R}^n$ form $GL(n, \mathbb{R})$. The determinant is a real number. Invertibility requires the determinant to be nonzero.
- Over $\mathbb{C}$, the linear transformations of $\mathbb{C}^n$ form $GL(n, \mathbb{C})$. The determinant is a complex number. Invertibility requires the determinant to be nonzero.
- Over $\mathbb{D}$, the linear transformations of $\mathbb{D}^n$ form $GL(n, \mathbb{D})$. The determinant is a split complex number. Invertibility requires the determinant to be a **unit** of $\mathbb{D}$, not merely nonzero.

## The same set, different scalars

The same set can be viewed as a module over different scalar structures. For example:

- $\mathbb{C}$ is a two-dimensional vector space over $\mathbb{R}$ and a one-dimensional vector space over $\mathbb{C}$.
- $\mathbb{D}$ is a two-dimensional vector space over $\mathbb{R}$ and a one-dimensional module over $\mathbb{D}$.
- $\mathbb{H}$ is a four-dimensional vector space over $\mathbb{R}$, a two-dimensional vector space over $\mathbb{C}$ (after complexification), and a four-dimensional module over $\mathbb{D}$ (after tensoring with $\mathbb{D}$).

The transformation groups are different in each case. For example, the transformations of $\mathbb{C}$ over $\mathbb{R}$ form $GL(2, \mathbb{R})$, while the transformations of $\mathbb{C}$ over $\mathbb{C}$ form $GL(1, \mathbb{C}) = \mathbb{C}^\times$. These are different groups: $GL(2, \mathbb{R})$ is four-dimensional, while $\mathbb{C}^\times$ is two-dimensional.

This is the reason the article is organized by scalar structure: the choice of scalars is the primary determinant of the structure of the transformation group.

## The determinant and the special linear group

The determinant is the factor by which the transformation scales volume. Its sign (over $\mathbb{R}$ and $\mathbb{Q}$) or argument (over $\mathbb{C}$) records whether the transformation preserves orientation.

$SL(V)$ is the subgroup of volume-preserving transformations. It is the kernel of the determinant map. In one dimension, it is trivial over $\mathbb{Q}$, $\mathbb{R}$, and $\mathbb{C}$, and it is the hyperbola over $\mathbb{D}$.

**Key difference from the field case.** Over a field, every nonzero scalar is a unit, so invertibility is equivalent to nonzero determinant. Over a general commutative ring, the units may be a proper subset of the nonzero elements, so invertibility requires the determinant to be a unit. This is the main modification needed to extend the theory from fields to commutative rings.

---

# Summary

Let me summarize the geometric description of the transformation groups.

**The field $\mathbb{Q}$.**

- $\mathbb{Q}$ over $\mathbb{Q}$: linear transformations are dilatations and reflections. The invertible ones form $GL(1, \mathbb{Q}) = \mathbb{Q}^\times$. The volume-preserving ones form the trivial group.
- $\mathbb{Q}^2$ over $\mathbb{Q}$: linear transformations form $GL(2, \mathbb{Q})$. The area-preserving ones form $SL(2, \mathbb{Q})$.

**The field $\mathbb{R}$.**

- $\mathbb{R}$ over $\mathbb{R}$: linear transformations are dilatations and reflections. The invertible ones form $GL(1, \mathbb{R}) = \mathbb{R}^\times$. The volume-preserving ones form the trivial group.
- $\mathbb{C}$ over $\mathbb{R}$: linear transformations are rotations, dilatations, reflections, and shears. The invertible ones form $GL(2, \mathbb{R})$. The area-preserving ones form $SL(2, \mathbb{R})$.
- $\mathbb{D}$ over $\mathbb{R}$: linear transformations include the hyperbolic transformations. The invertible ones form $GL(2, \mathbb{R})$. The area-preserving ones form $SL(2, \mathbb{R})$.
- $\mathbb{H}$ over $\mathbb{R}$: linear transformations form $GL(4, \mathbb{R})$. The quaternion-linear ones form $\mathbb{H}^\times$, and the norm-preserving ones form $SU(2)$.

**The field $\mathbb{C}$.**

- $\mathbb{C}$ over $\mathbb{C}$: linear transformations are rotations-dilatations. The invertible ones form $GL(1, \mathbb{C}) = \mathbb{C}^\times$. The volume-preserving ones form the trivial group.
- $\mathbb{C}^2$ over $\mathbb{C}$: linear transformations form $GL(2, \mathbb{C})$. The volume-preserving ones form $SL(2, \mathbb{C})$.
- $\mathbb{H} \otimes \mathbb{C}$ over $\mathbb{C}$: linear transformations form $GL(4, \mathbb{C})$. The biquaternion-linear ones form the group of units of the biquaternions.

**The commutative ring $\mathbb{D}$.**

- $\mathbb{D}$ over $\mathbb{D}$: linear transformations are hyperbolic transformations. The invertible ones form the group of units of $\mathbb{D}$. The norm-one ones form the hyperbola.
- $\mathbb{D}^2$ over $\mathbb{D}$: linear transformations form $GL(2, \mathbb{D})$.
- $\mathbb{H} \otimes \mathbb{D}$ over $\mathbb{D}$: linear transformations form $GL(4, \mathbb{D})$.

**The general pattern.** The linear transformations of a module decompose into elementary geometric operations: dilatations, rotations, hyperbolic transformations, reflections, and shears. The determinant records the volume scaling, and $SL(V)$ is the subgroup of volume-preserving transformations. The choice of scalar structure determines which operations are available and the structure of the transformation group.

**The key modification.** Over a field, invertibility is equivalent to nonzero determinant. Over a commutative ring, invertibility requires the determinant to be a unit. This is the main change needed to extend the theory from fields to commutative rings.

---

# Further Reading

- Michael Artin, *Algebra* (Prentice Hall, 1991), for an introduction to groups and transformations.
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002), for a more advanced treatment.
- I. N. Herstein, *Topics in Algebra* (Wiley, 2nd ed. 1975), for a classic introduction.
- Paul M. Cohn, *Basic Algebra: Groups, Rings and Fields* (Springer, 2003), for a modern introduction.
- Nathan Jacobson, *Basic Algebra I* (Dover, 2nd ed. 2009), for a thorough treatment.
- David S. Dummit and Richard M. Foote, *Abstract Algebra* (Wiley, 3rd ed. 2004), for a comprehensive treatment of groups, rings, and modules.
- I. M. Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for a geometric treatment of both the complex and split complex numbers.
- F. Catoni, R. Cannata, V. Catoni, E. Nichelatti, P. Zampetti, *The Mathematics of Minkowski Space-Time* (Birkhäuser, 2008), for the split complex numbers as the algebraic model of two-dimensional Minkowski space.


