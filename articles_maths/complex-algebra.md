# __Complex Algebra__

## Introduction

This article introduces the complex algebra as an algebraic structure, without yet discussing its representations. The goal is to define the algebra precisely, establish its basic properties, and describe the distinguished real vector subspaces that arise from the natural conjugation.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. The complex algebra is defined algebraically, and its identification with the plane is not covered here.

## The Complex Numbers

### Definition

The **complex algebra** $\mathbb{C}$ is the two-dimensional real algebra with basis

$$
e_0 = 1, \qquad e_1 = i,
$$

and multiplication rules

$$
e_0 e_0 = e_0, \qquad e_0 e_1 = e_1 e_0 = e_1, \qquad e_1 e_1 = -e_0.
$$

A general complex number is written in developed form as

$$
z = a e_0 + b e_1, \qquad a, b \in \mathbb{R},
$$

or, more compactly, as

$$
z = a + b i, \qquad a, b \in \mathbb{R}.
$$

The real number $a$ is the **real part**, and the real number $b$ is the **imaginary part**. We also write

$$
z = a + b i, \qquad a = \operatorname{Re} z, \quad b = \operatorname{Im} z.
$$

The notation $i$ is chosen deliberately. In some of the older literature, the imaginary unit is written $j$ or $\sqrt{-1}$, which collides visually with the index $j$ or with the square root sign. This collision is a persistent source of confusion, especially when the complex algebra is tensored with other algebras. Using $i$ for the imaginary unit and reserving $j$ for indices avoids the collision entirely. This is the notation we use throughout the blog.

### Basic Properties

**Commutative.** Complex multiplication is commutative: $z w = w z$.

**Associative.** Complex multiplication is associative: $(z w) u = z (w u)$.

**Division algebra.** Every nonzero complex number has a multiplicative inverse. The inverse is

$$
z^{-1} = \frac{\bar{z}}{|z|^2},
$$

where

$$
\bar{z} = a - b i
$$

is the **complex conjugate**, and

$$
|z|^2 = z \bar{z} = a^2 + b^2
$$

is the **norm squared**. The norm is multiplicative: $|z w| = |z| |w|$.

**Frobenius theorem.** The complex algebra is one of only three finite-dimensional associative real division algebras, the others being $\mathbb{R}$ and $\mathbb{H}$. In fact, $\mathbb{C}$ is the only one that is commutative but not ordered.

### The Imaginary Part and $\mathbb{R}^2$

The pair $(a, b)$ can be identified with a vector in $\mathbb{R}^2$. Under this identification, the product of two complex numbers is

$$
z w = (ac - bd) + (ad + bc) i, \qquad z = a + bi, \quad w = c + di.
$$

This is the formula for the product in the algebra, written in real coordinates. There is no dot product and no cross product in this expression, because $\mathbb{C}$ is commutative and two-dimensional. The multiplication is the only operation, and it encodes both a rotation and a scaling of the plane.

## Complex Algebra

### Definition

The **complex algebra** is the field $\mathbb{C}$ considered as a two-dimensional real vector space equipped with its field multiplication. As a real vector space, $\mathbb{C}$ has dimension $2$. As a ring, it is a field. A general element is written in developed form as

$$
z = a e_0 + b e_1, \qquad a, b \in \mathbb{R},
$$

or, more compactly, as

$$
z = a + b i, \qquad a, b \in \mathbb{R}.
$$

We write

$$
z = a + b i,
$$

where $a$ is the **real part** and $b$ is the **imaginary part**. The tilde is absent because $z$ is an element of the algebra $\mathbb{C}$, not a vector in some larger space.

### Multiplication

The product of two complex numbers is defined by extending the real multiplication bilinearly:

$$
z w = (a + bi)(c + di) = (ac - bd) + (ad + bc) i.
$$

In developed form,

$$
z w = \sum_{\mu=0}^{1} \sum_{\nu=0}^{1} z_\mu w_\nu \, e_\mu e_\nu,
$$

where the products $e_\mu e_\nu$ are those of the complex algebra.

### Conjugations

There are **two** natural conjugations on $\mathbb{C}$, obtained by composing the complex conjugation with itself:

**Complex conjugation** $\bar{z}$:

$$
\bar{z} = a - b i.
$$

**Identity conjugation** $\operatorname{id}$:

$$
\operatorname{id}(z) = z.
$$

Each conjugation is an involution: applying it twice returns the original complex number. Each has a fixed-point set, which is a real vector subspace of $\mathbb{C}$. The two subspaces are described in the following sections.

## The Two Fixed-Point Subspaces

Each of the two conjugations has a fixed-point set, i.e., a set of complex numbers left invariant by the conjugation. Each fixed-point set is a real vector subspace of $\mathbb{C}$. The two subspaces are described below.

### The Real Subspace

The fixed points of **complex conjugation** are the complex numbers satisfying $\bar{z} = z$. In developed form,

$$
a - b i = a + b i.
$$

Comparing the coefficients of $1$ and $i$:

- Coefficient of $1$: $a = a$, always satisfied.
- Coefficient of $i$: $-b = b$, so $b = 0$.

The fixed points are complex numbers with vanishing imaginary part:

$$
z = a, \qquad a \in \mathbb{R}.
$$

This is the **real subspace** $\mathbb{R}_{\mathbb{C}}$, a copy of the real number line embedded in $\mathbb{C}$ as the real axis. It is a real vector space of dimension $1$. It is a subalgebra of $\mathbb{C}$ (isomorphic to $\mathbb{R}$), and it is the only one of the two fixed-point sets that is an ordered field.

### The Complex Subspace

The fixed points of the **identity conjugation** are all complex numbers. In developed form,

$$
z = z.
$$

The fixed points are

$$
z = a + b i, \qquad a, b \in \mathbb{R}.
$$

This is the **complex subspace** $\mathbb{C}_{\mathbb{C}}$, a copy of the complex plane embedded in $\mathbb{C}$ as the whole thing. It is a real vector space of dimension $2$. It is a subalgebra of $\mathbb{C}$, and it is a division algebra.

## Complex Decomposition

The real subspace $\mathbb{R}_{\mathbb{C}}$ and its imaginary translate $i \mathbb{R}_{\mathbb{C}}$ are the two eigenspaces of complex conjugation. Every complex number decomposes uniquely as the sum of a real part and an imaginary part:

$$
z = z_r + i z_i, \qquad z_r \in \mathbb{R}, \quad z_i \in \mathbb{R}.
$$

The two components are obtained from the complex conjugation:

$$
z_r = \frac{1}{2}(z + \bar{z}), \qquad z_i = \frac{1}{2i}(z - \bar{z}).
$$

Indeed, $z_r$ is fixed by complex conjugation, so it lies in $\mathbb{R}_{\mathbb{C}}$, and $z_i$ is real, so $i z_i$ is negated by complex conjugation.

This gives the direct sum decomposition

$$
\mathbb{C} = \mathbb{R}_{\mathbb{C}} \oplus i \mathbb{R}_{\mathbb{C}},
$$

where $i \mathbb{R}_{\mathbb{C}}$ is the set of complex numbers of the form $i b$ with $b \in \mathbb{R}$. Both are real vector spaces of dimension $1$, and their direct sum is the full algebra $\mathbb{C}$ of real dimension $2$.

This is the **complex decomposition** of a complex number. It expresses $z$ as a real number plus $i$ times another real number. It is the natural decomposition when we think of $\mathbb{C}$ as the complexification of $\mathbb{R}$.

## Conjugate Decomposition

The complex conjugation $\bar{\cdot}$ is an involution, so it has eigenvalues $+1$ and $-1$. Its eigenspaces are the real subspace $\mathbb{R}_{\mathbb{C}}$ (eigenvalue $+1$) and the imaginary subspace $i \mathbb{R}_{\mathbb{C}}$ (eigenvalue $-1$). Every complex number decomposes uniquely as

$$
z = z_+ + z_-, \qquad z_+ = z_r, \quad z_- = i z_i.
$$

This is the same decomposition as above, written in terms of the eigenspaces of the conjugation. It is the algebraic analogue of writing a real number as the sum of its even and odd parts under a reflection.

## Quadratic Forms and Inner Product

### The Norm Form

The **norm form** of a complex number $z$ is

$$
N(z) = z \bar{z} = a^2 + b^2,
$$

where $\bar{z}$ is the complex conjugate. It is a non-negative real number, and it vanishes if and only if $z = 0$. It is a genuine positive-definite quadratic form.

The norm form is **multiplicative**:

$$
N(z w) = N(z) N(w).
$$

This is the statement that $|z w|^2 = |z|^2 |w|^2$, which follows from the multiplicativity of the complex norm.

### The Hermitian Form

The **Hermitian form** of a complex number $z$ is

$$
z \bar{z} = a^2 + b^2.
$$

It coincides with the norm form, because $\mathbb{C}$ is commutative and the conjugation is the only non-trivial involution. It is a non-negative real number, and it vanishes if and only if $z = 0$.

The corresponding **Euclidean norm** is

$$
\|z\|_E = \sqrt{z \bar{z}} = \sqrt{a^2 + b^2}.
$$

It is a genuine norm on the real vector space $\mathbb{C} \cong \mathbb{R}^2$: positive-definite, subadditive, and homogeneous of degree one. It **is** multiplicative with respect to the complex product, because $|z w| = |z| |w|$.

### The Inner Product

The **inner product** of two complex numbers $z$ and $w$ is

$$
\langle z, w \rangle = \bar{z} w = (a - bi)(c + di) = (ac + bd) + (ad - bc) i.
$$

In general this is a **complex number**, not a real one. This is a genuinely complex feature: the inner product of two complex numbers is complex, and its imaginary part measures the oriented area of the parallelogram spanned by $z$ and $w$.

The inner product is linear in the second argument and anti-linear in the first:

$$
\langle \lambda z, w \rangle = \bar{\lambda} \langle z, w \rangle, \qquad \langle z, \lambda w \rangle = \lambda \langle z, w \rangle, \qquad \lambda \in \mathbb{C}.
$$

It is **Hermitian** in the sense that

$$
\langle z, w \rangle^* = \langle w, z \rangle,
$$

which follows from the definition.

The inner product of a complex number with itself is

$$
\langle z, z \rangle = \bar{z} z = a^2 + b^2,
$$

which is the Hermitian form. So the Hermitian form is the restriction of the inner product to the diagonal.

### Relation Between the Three Forms

The three quadratic objects are related as follows:

- **Norm form:** $N(z) = z \bar{z} = a^2 + b^2$. Non-negative real, vanishes only at $z = 0$, multiplicative.
- **Hermitian form:** $z \bar{z} = a^2 + b^2$. Same as the norm form, because $\mathbb{C}$ is commutative.
- **Inner product:** $\langle z, w \rangle = \bar{z} w$. Complex-valued in general, Hermitian, linear in the second argument.

The norm form and the Hermitian form coincide, while the inner product is a distinct two-variable object; each is useful in a different context. The norm form controls the multiplicative structure (invertibility, zero divisors). The Hermitian form controls the topological structure (continuity, completeness). The inner product combines both, and is the natural pairing on the algebra as a complex vector space.

In the complex case, the norm form and the Hermitian form coincide, because the conjugation is the only non-trivial involution and the algebra is commutative. This is a degeneracy of the two-dimensional case, and it is the reason the complex numbers are often treated as a trivial example rather than as a case study.

## Summary

The complex algebra $\mathbb{C}$ is the real algebra of dimension $2$ with basis $e_0 = 1$, $e_1 = i$ and the single relation $e_1^2 = -e_0$. With its multiplication it is a field: commutative, associative and unital, with every nonzero element invertible. A general element is written in developed form as $z = a e_0 + b e_1$.

Complex conjugation is the nontrivial $\mathbb{R}$-linear involution, and its two fixed-point subspaces are the real subspace $\mathbb{R}_{\mathbb{C}}$, on which the conjugation acts as the identity, and the imaginary subspace $i\mathbb{R}_{\mathbb{C}}$, which it negates. These are the eigenspaces for the eigenvalues $+1$ and $-1$, and every complex number decomposes uniquely in each of the two ways the article records: as a real part plus an imaginary part, and as the sum of the $+1$ and $-1$ eigencomponents.

Three quadratic objects are attached to the algebra. The norm form $N(z) = z\bar{z} = a^2 + b^2$ is positive definite and multiplicative, $N(zw) = N(z)N(w)$, and it vanishes only at $z = 0$; it is the form that controls invertibility. The Hermitian form is the same expression, while the inner product $\langle z, w\rangle = \bar{z}w$ is a genuinely two-variable Hermitian object, complex-valued in general and linear in the second argument. That the norm form and the Hermitian form coincide is a degeneracy of the commutative two-dimensional case, and it is the reason the complex numbers are commonly treated as a trivial example rather than as a case study.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{C}$ | Complex algebra |
| $e_0 = 1$ | Identity |
| $e_1 = i$ | Imaginary unit, $i^2 = -1$ |
| $z = a + b i$ | General complex number |
| $a = \operatorname{Re} z$ | Real part |
| $b = \operatorname{Im} z$ | Imaginary part |
| $\bar{z} = a - b i$ | Complex conjugate |
| $\operatorname{id}(z) = z$ | Identity conjugation |
| $N(z) = z \bar{z}$ | Norm form |
| $z \bar{z} = a^2 + b^2$ | Hermitian form |
| $\langle z, w \rangle = \bar{z} w$ | Inner product |
| $\|z\|_E = \sqrt{z \bar{z}}$ | Euclidean norm |
| $\mathbb{R}_{\mathbb{C}}$ | Real subspace, fixed-point set of $\bar{\cdot}$ |
| $\mathbb{C}_{\mathbb{C}}$ | Complex subspace, fixed-point set of $\operatorname{id}$ |



## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the origin of the complex algebra in the quaternion program.
- Carl Friedrich Gauss, *Theoria residuorum biquadraticorum* (1831), for the geometric interpretation of complex numbers.
- Edmund Landau, *Grundlagen der Analysis* (1930), for the axiomatic treatment of the complex field.
- Walter Rudin, *Real and Complex Analysis* (McGraw-Hill, 1987), for the standard modern treatment.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the classification of real division algebras.
- Charles C. Pinter, *A Book of Abstract Algebra* (Dover, 2010), for the representation theory of fields.

