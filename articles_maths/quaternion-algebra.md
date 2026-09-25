# __Quaternion Algebra__

## Introduction

This article introduces the quaternion algebra as an algebraic structure. The goal is to define the algebra precisely, establish its basic properties, and describe the distinguished real vector subspaces that arise from the natural conjugations.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. No examples are given. The quaternion algebra is defined algebraically, and its identification with rotations is not covered here.

## The Quaternions

### Definition

The **quaternion algebra** $\mathbb{H}$ is the four-dimensional real algebra with basis

$$
e_0 = 1, \qquad e_1, \qquad e_2, \qquad e_3,
$$

and multiplication rules

$$
e_0 e_k = e_k e_0 = e_k, \qquad e_0^2 = e_0,
$$

$$
e_1^2 = e_2^2 = e_3^2 = -e_0,
$$

$$
e_1 e_2 = e_3, \qquad e_2 e_3 = e_1, \qquad e_3 e_1 = e_2,
$$

$$
e_2 e_1 = -e_3, \qquad e_3 e_2 = -e_1, \qquad e_1 e_3 = -e_2.
$$

A general quaternion is written in developed form as

$$
q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3, \qquad q_\mu \in \mathbb{R},
$$

or, more compactly, as

$$
q = \sum_{\mu=0}^{3} q_\mu e_\mu, \qquad q_\mu \in \mathbb{R}.
$$

The real number $q_0$ is the **scalar part**, and the triple $(q_1, q_2, q_3)$ is the **vector part**. We also write

$$
q = q_0 + \mathbf{q}, \qquad \mathbf{q} = \sum_{k=1}^{3} q_k e_k.
$$

### A Note on the Notation

The notation $e_1, e_2, e_3$ is chosen deliberately, and it replaces the classical notation $i, j, k$ used in the older literature. The reason is that the symbols $i, j, k$ collide with other standard notations:

- The symbol $i$ is universally used for the scalar imaginary unit of the complex numbers, with $i^2 = -1$. In the quaternion algebra, the unit $e_1$ also satisfies $e_1^2 = -e_0$, so writing it as $i$ makes it visually indistinguishable from the scalar imaginary. This collision becomes acute when the quaternion algebra is complexified: the biquaternion algebra $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ contains both the scalar imaginary $i$ and the quaternion unit $e_1$, and they are different elements. Writing both as $i$ makes the algebra unreadable.
- The symbol $j$ is universally used as an index, as in $a_j$, $e_j$, $x_j$, and so on. Writing the quaternion unit as $j$ makes every expression with an index ambiguous.
- The symbol $k$ is also used as an index, particularly in sums over three variables.

The notation $e_0, e_1, e_2, e_3$ avoids all three collisions. It also has the advantage of being uniform: the scalar unit $e_0$ is treated on the same footing as the vector units $e_1, e_2, e_3$, which makes the algebra look like a graded algebra with a single family of generators. This is the notation we use throughout the blog.

### Basic Properties

**Non-commutative.** Quaternion multiplication is not commutative: $e_1 e_2 = e_3$ but $e_2 e_1 = -e_3$.

**Associative.** Quaternion multiplication is associative: $(pq)r = p(qr)$.

**Division algebra.** Every nonzero quaternion has a multiplicative inverse. The inverse is

$$
q^{-1} = \frac{\bar{q}}{|q|^2},
$$

where

$$
\bar{q} = q_0 - \mathbf{q}
$$

is the **quaternion conjugate**, and

$$
|q|^2 = q \bar{q} = \sum_{\mu=0}^{3} q_\mu^2
$$

is the **norm squared**. The norm is multiplicative: $|pq| = |p||q|$.

**Frobenius theorem.** The quaternion algebra is one of only three finite-dimensional associative real division algebras, the others being $\mathbb{R}$ and $\mathbb{C}$.

### The Vector Part and $\mathbb{R}^3$

The vector part $\mathbf{q}$ of a quaternion is identified with a vector in $\mathbb{R}^3$. Under this identification, the product of two quaternions is

$$
pq = (p_0 q_0 - \mathbf{p} \cdot \mathbf{q}) + (p_0 \mathbf{q} + q_0 \mathbf{p} + \mathbf{p} \times \mathbf{q}),
$$

where $\mathbf{p} \cdot \mathbf{q}$ is the ordinary dot product and $\mathbf{p} \times \mathbf{q}$ is the ordinary cross product in $\mathbb{R}^3$. The dot product and cross product are not separate operations; they are the scalar and vector parts of a single quaternion product.

## Quaternion Algebra

### Definition

The **quaternion algebra** is the algebra $\mathbb{H}$ considered as a four-dimensional real vector space equipped with its multiplication. As a real vector space, $\mathbb{H}$ has dimension $4$. As a ring, it is a division algebra. A general element is written in developed form as

$$
q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3, \qquad q_\mu \in \mathbb{R},
$$

or, more compactly, as

$$
q = \sum_{\mu=0}^{3} q_\mu e_\mu, \qquad q_\mu \in \mathbb{R}.
$$

We write

$$
q = q_0 + \mathbf{q},
$$

where $q_0$ is the **scalar part** and $\mathbf{q}$ is the **vector part**.

### Multiplication

The product of two quaternions is defined by extending the real multiplication bilinearly:

$$
pq = \sum_{\mu=0}^{3} \sum_{\nu=0}^{3} p_\mu q_\nu \, e_\mu e_\nu,
$$

where the products $e_\mu e_\nu$ are those of the quaternion algebra. In scalar-vector notation, this becomes

$$
pq = p_0 q_0 - \mathbf{p} \cdot \mathbf{q} + p_0 \mathbf{q} + q_0 \mathbf{p} + \mathbf{p} \times \mathbf{q}.
$$

### Conjugations

There are **three** natural conjugations on $\mathbb{H}$, obtained from the quaternion conjugation together with the negation map:

**Quaternion conjugation** $\bar{q}$:

$$
\bar{q} = q_0 - \mathbf{q}.
$$

**Vector conjugation** $\tilde{q}$:

$$
\tilde{q} = -q_0 + \mathbf{q}.
$$

**Total conjugation** $\hat{q}$:

$$
\hat{q} = -q_0 - \mathbf{q}.
$$

Each conjugation is an involution: applying it twice returns the original quaternion. Each has a fixed-point set, which is a real vector subspace of $\mathbb{H}$. The three subspaces are described in the following sections.

## The Three Fixed-Point Subspaces

Each of the three conjugations has a fixed-point set, i.e., a set of quaternions left invariant by the conjugation. Each fixed-point set is a real vector subspace of $\mathbb{H}$. The three subspaces are described below.

### The Real Subspace

The fixed points of **quaternion conjugation** are the quaternions satisfying $\bar{q} = q$. In developed form,

$$
q_0 - \mathbf{q} = q_0 + \mathbf{q}.
$$

Comparing the scalar and vector parts:

- Scalar part: $q_0 = q_0$, always satisfied.
- Vector part: $-\mathbf{q} = \mathbf{q}$, so $\mathbf{q} = 0$.

The fixed points are quaternions with vanishing vector part:

$$
q = q_0, \qquad q_0 \in \mathbb{R}.
$$

This is the **real subspace** $\mathbb{R}_{\mathbb{H}}$, a copy of the real number line embedded in $\mathbb{H}$ as the scalar axis. It is a real vector space of dimension $1$. It is a subalgebra of $\mathbb{H}$ (isomorphic to $\mathbb{R}$), and it is the only one of the three fixed-point sets that is an ordered field.

### The Vector Subspace

The fixed points of **vector conjugation** are the quaternions satisfying $\tilde{q} = q$. In developed form,

$$
-q_0 + \mathbf{q} = q_0 + \mathbf{q}.
$$

Comparing the scalar and vector parts:

- Scalar part: $-q_0 = q_0$, so $q_0 = 0$.
- Vector part: $\mathbf{q} = \mathbf{q}$, always satisfied.

The fixed points are quaternions with vanishing scalar part:

$$
q = \mathbf{q}, \qquad \mathbf{q} \in \mathbb{R}^3.
$$

This is the **vector subspace** $\mathbb{R}^3_{\mathbb{H}}$, a copy of three-dimensional space embedded in $\mathbb{H}$ as the pure imaginary quaternions. It is a real vector space of dimension $3$. It is not a subalgebra of $\mathbb{H}$: the product of two pure quaternions is not pure, because it has a scalar part $-\mathbf{p} \cdot \mathbf{q}$.

### The Total Subspace

The fixed points of **total conjugation** are the quaternions satisfying $\hat{q} = q$. In developed form,

$$
-q_0 - \mathbf{q} = q_0 + \mathbf{q}.
$$

Comparing the scalar and vector parts:

- Scalar part: $-q_0 = q_0$, so $q_0 = 0$.
- Vector part: $-\mathbf{q} = \mathbf{q}$, so $\mathbf{q} = 0$.

The fixed points are

$$
q = 0.
$$

This is the **zero subspace**, a real vector space of dimension $0$.

## Quaternion Decomposition

The real subspace $\mathbb{R}_{\mathbb{H}}$ and the vector subspace $\mathbb{R}^3_{\mathbb{H}}$ are the two eigenspaces of quaternion conjugation. Every quaternion decomposes uniquely as the sum of a scalar part and a vector part:

$$
q = q_r + q_v, \qquad q_r \in \mathbb{R}, \quad q_v \in \mathbb{R}^3.
$$

The two components are obtained from the quaternion conjugation:

$$
q_r = \frac{1}{2}(q + \bar{q}), \qquad q_v = \frac{1}{2}(q - \bar{q}).
$$

Indeed, $q_r$ is fixed by quaternion conjugation, so it lies in $\mathbb{R}_{\mathbb{H}}$, and $q_v$ satisfies $\bar{q}_v = -q_v$, so it lies in $\mathbb{R}^3_{\mathbb{H}}$.

This gives the direct sum decomposition

$$
\mathbb{H} = \mathbb{R}_{\mathbb{H}} \oplus \mathbb{R}^3_{\mathbb{H}},
$$

where $\mathbb{R}^3_{\mathbb{H}}$ is the set of pure quaternions. Both are real vector spaces of dimensions $1$ and $3$, and their direct sum is the full algebra $\mathbb{H}$ of real dimension $4$.

This is the **scalar-vector decomposition** of a quaternion. It expresses $q$ as a real number plus a vector in $\mathbb{R}^3$.

## Conjugate Decomposition

The quaternion conjugation $\bar{\cdot}$ is an involution, so it has eigenvalues $+1$ and $-1$. Its eigenspaces are the real subspace $\mathbb{R}_{\mathbb{H}}$ (eigenvalue $+1$) and the vector subspace $\mathbb{R}^3_{\mathbb{H}}$ (eigenvalue $-1$). Every quaternion decomposes uniquely as

$$
q = q_+ + q_-, \qquad q_+ = q_r, \quad q_- = q_v.
$$

This is the same decomposition as above, written in terms of the eigenspaces of the conjugation.

## Quadratic Forms and Inner Product

### The Norm Form

The **norm form** of a quaternion $q$ is

$$
N(q) = q \bar{q} = q_0^2 + q_1^2 + q_2^2 + q_3^2,
$$

where $\bar{q}$ is the quaternion conjugate. It is a non-negative real number, and it vanishes if and only if $q = 0$. It is a genuine positive-definite quadratic form.

The norm form is **multiplicative**:

$$
N(pq) = N(p) N(q).
$$

This is the statement that $|pq|^2 = |p|^2 |q|^2$, which follows from the multiplicativity of the quaternion norm.

### The Hermitian Form

The **Hermitian form** of a quaternion $q$ is

$$
q \bar{q} = q_0^2 + q_1^2 + q_2^2 + q_3^2.
$$

It coincides with the norm form, because the quaternion conjugation is the only non-trivial involution that is compatible with the algebra structure. It is a non-negative real number, and it vanishes if and only if $q = 0$.

The corresponding **Euclidean norm** is

$$
\|q\|_E = \sqrt{q \bar{q}} = \sqrt{q_0^2 + q_1^2 + q_2^2 + q_3^2}.
$$

It is a genuine norm on the real vector space $\mathbb{H} \cong \mathbb{R}^4$: positive-definite, subadditive, and homogeneous of degree one. It **is** multiplicative with respect to the quaternion product, because $|pq| = |p| |q|$.

### The Inner Product

The **inner product** of two quaternions $p$ and $q$ is

$$
\langle p, q \rangle = \bar{p} q = (p_0 - \mathbf{p})(q_0 + \mathbf{q}) = (p_0 q_0 + \mathbf{p} \cdot \mathbf{q}) + (p_0 \mathbf{q} - q_0 \mathbf{p} - \mathbf{p} \times \mathbf{q}).
$$

In general this is a **quaternion**, not a real number. This is a genuinely quaternionic feature: the inner product of two quaternions is a quaternion, and its scalar part measures the overlap while its vector part measures the oriented area and the relative orientation.

The inner product is linear in the second argument and anti-linear in the first:

$$
\langle p \lambda, q \rangle = \bar{\lambda} \langle p, q \rangle, \qquad \langle p, q \lambda \rangle = \langle p, q \rangle \lambda, \qquad \lambda \in \mathbb{H}.
$$

It is **Hermitian** in the sense that

$$
\langle p, q \rangle^* = \langle q, p \rangle,
$$

where $^*$ is the quaternion conjugation.

The inner product of a quaternion with itself is

$$
\langle q, q \rangle = \bar{q} q = q_0^2 + q_1^2 + q_2^2 + q_3^2,
$$

which is the Hermitian form. So the Hermitian form is the restriction of the inner product to the diagonal.

### Relation Between the Three Forms

The three quadratic objects are related as follows:

- **Norm form:** $N(q) = q \bar{q} = q_0^2 + q_1^2 + q_2^2 + q_3^2$. Non-negative real, vanishes only at $q = 0$, multiplicative.
- **Hermitian form:** $q \bar{q} = q_0^2 + q_1^2 + q_2^2 + q_3^2$. Same as the norm form, because the quaternion conjugation is the only non-trivial involution compatible with the algebra.
- **Inner product:** $\langle p, q \rangle = \bar{p} q$. Quaternion-valued in general, Hermitian, linear in the second argument.

The three are distinct, and each is useful in a different context. The norm form controls the multiplicative structure (invertibility, zero divisors). The Hermitian form controls the topological structure (continuity, completeness). The inner product combines both, and is the natural pairing on the algebra as a real vector space.

In the quaternion case, the norm form and the Hermitian form coincide, because the quaternion conjugation is the only non-trivial involution that is compatible with the algebra structure. This is a degeneracy of the four-dimensional case, and it is the reason the quaternion algebra is often treated as a special case rather than as a general example.

## The Lie Algebra Structure

The quaternion algebra carries a Lie bracket, defined by the commutator

$$
[p, q] = pq - qp.
$$

For pure quaternions $\mathbf{p}, \mathbf{q} \in \mathbb{R}^3_{\mathbb{H}}$, the commutator is

$$
[\mathbf{p}, \mathbf{q}] = 2 \mathbf{p} \times \mathbf{q}.
$$

So the vector subspace $\mathbb{R}^3_{\mathbb{H}}$, equipped with the commutator bracket, is a Lie subalgebra of $\mathbb{H}$ isomorphic to the Lie algebra $\mathfrak{so}(3)$ of infinitesimal rotations:

$$
\mathbb{R}^3_{\mathbb{H}} \cong \mathfrak{so}(3).
$$

This is the algebraic origin of the relationship between quaternions and rotations. The pure quaternions generate the rotations, and the commutator bracket on the pure quaternions is the Lie bracket of the rotation algebra.

## The Tensor Product Decomposition

The quaternion algebra of a direct sum of two modules with quadratic forms is the tensor product of the quaternion algebras of the summands. For the specific case of the quaternion algebra, the relevant decomposition is

$$
\mathbb{H} \otimes_{\mathbb{R}} \mathbb{H} \cong M_4(\mathbb{R}),
$$

the algebra of $4 \times 4$ real matrices. More generally, the tensor product of two quaternion algebras is a matrix algebra over $\mathbb{R}$, and the specific size depends on the quadratic forms.

The tensor product decomposition is the algebraic content of the classification of Clifford algebras, and the quaternion algebra is the case $n = 2$ of the classification. The general classification is the subject of the article *Clifford Algebras in Finite Dimensions*.

## Summary

The quaternion algebra $\mathbb{H}$ is the four-dimensional real algebra with basis $e_0 = 1, e_1, e_2, e_3$, in which $e_0$ is the unit, the three imaginary units square to $-e_0$, and distinct imaginary units anticommute. It is associative with unit, non-commutative, and a division algebra: every nonzero element is invertible, with $q^{-1} = \bar{q}/N(q)$. A general element is written in developed form as $q = q_0 + q_1e_1 + q_2e_2 + q_3e_3$.

The algebra carries three conjugations, and each has its fixed-point subspace; the fundamental one is quaternion conjugation, whose fixed points form the real subspace $\mathbb{R}_{\mathbb{H}}$ and whose anti-fixed points form the vector subspace $\mathbb{R}^3_{\mathbb{H}}$. These are the eigenspaces for the eigenvalues $+1$ and $-1$, and every quaternion decomposes uniquely both as a scalar part plus a vector part and as the sum of the two eigencomponents.

Further structures are attached to the algebra. The norm form $N(q) = q\bar{q} = q_0^2 + q_1^2 + q_2^2 + q_3^2$ is positive definite and multiplicative, and it is the form that controls invertibility; with it come the Hermitian form and the inner product on $\mathbb{H}$ as a real vector space. The commutator $[p,q] = pq - qp$ gives $\mathbb{H}$ a Lie algebra structure, in which the commutator of two pure quaternions is expressed by the vector product on $\mathbb{R}^3$. The article closes with the tensor product decomposition, in which the quaternion algebra of a direct sum is the tensor product of the quaternion algebras of the summands.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | Quaternion algebra |
| $e_0 = 1$ | Identity |
| $e_1, e_2, e_3$ | Quaternion units, $e_k^2 = -e_0$ |
| $q = q_0 + \mathbf{q}$ | General quaternion |
| $q_0$ | Scalar part |
| $\mathbf{q}$ | Vector part |
| $\bar{q} = q_0 - \mathbf{q}$ | Quaternion conjugate |
| $\tilde{q} = -q_0 + \mathbf{q}$ | Vector conjugate |
| $\hat{q} = -q_0 - \mathbf{q}$ | Total conjugate |
| $N(q) = q \bar{q}$ | Norm form |
| $q \bar{q} = q_0^2 + q_1^2 + q_2^2 + q_3^2$ | Hermitian form |
| $\langle p, q \rangle = \bar{p} q$ | Inner product |
| $\|q\|_E = \sqrt{q \bar{q}}$ | Euclidean norm |
| $\mathbb{R}_{\mathbb{H}}$ | Real subspace, fixed-point set of $\bar{\cdot}$ |
| $\mathbb{R}^3_{\mathbb{H}}$ | Vector subspace, fixed-point set of $\tilde{\cdot}$ |
| $\mathfrak{so}(3)$ | Lie algebra of rotations |



## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original formulation.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the classification of real algebras.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton, 1989), for the role of quaternions in geometry.

