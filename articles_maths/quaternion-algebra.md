
# __Quaternion Algebra__

## Introduction

This article introduces the quaternion algebra as an algebraic structure. The goal is to define the algebra precisely, establish its basic properties, and describe the distinguished real vector subspaces that arise from the natural conjugations.

The quadratic form the algebra carries — its polarisation, the Hermitian form and the inner product — is a form and a distance, and a norm is a distance: these belong to the topology group, in *Quaternion Norm and Invertibility*, and the present article only names them. The geometric reading of the algebra is likewise deferred to the geometry group, in *Quaternion Rotations and Reflections*.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. No examples are given.

## Quaternions

### Definition

The **quaternion algebra** $\mathbb{H}$ is the four-dimensional real algebra with basis

$$
e_t = 1, \qquad \vec e_x, \qquad \vec e_y, \qquad \vec e_z,
$$

and multiplication rules

$$
e_t \vec e_\mu = \vec e_\mu e_t = \vec e_\mu, \qquad e_t^2 = e_t,
$$

$$
\vec e_x^2 = \vec e_y^2 = \vec e_z^2 = -e_t,
$$

$$
\vec e_x \vec e_y = \vec e_z, \qquad \vec e_y \vec e_z = \vec e_x, \qquad \vec e_z \vec e_x = \vec e_y,
$$

$$
\vec e_y \vec e_x = -\vec e_z, \qquad \vec e_z \vec e_y = -\vec e_x, \qquad \vec e_x \vec e_z = -\vec e_y.
$$

A general quaternion is written in developed form as

$$
\tilde q = q_t e_t + q_x \vec e_x + q_y \vec e_y + q_z \vec e_z, \qquad q_\mu \in \mathbb{R},
$$

or, more compactly, as

$$
\tilde q = \sum_{\mu\in\{t,x,y,z\}} q_\mu e_\mu, \qquad q_\mu \in \mathbb{R}.
$$

The real number $q_t$ is the **scalar part**, and the triple $(q_x, q_y, q_z)$ is the **vector part**. We also write

$$
\tilde q = q_t e_t + q_x \vec e_x + q_y \vec e_y + q_z \vec e_z, \qquad \vec q = \sum_{\mu=1}^{3} q_\mu \vec e_\mu.
$$

### A Note on the Notation

The notation $\vec e_x, \vec e_y, \vec e_z$ is chosen deliberately, and it replaces the classical notation $i, j, k$ used in the older literature. The reason is that the symbols $i, j, k$ collide with other standard notations:

- The symbol $j$ is universally used as an index, as in $a_j$, $e_j$, $q_j$, and so on. Writing the quaternion unit as $j$ makes every expression with an index ambiguous.
- The symbol $k$ is also used as an index, particularly in sums over three variables.

The notation $e_t, \vec e_x, \vec e_y, \vec e_z$ avoids all three collisions. It also has the advantage of being uniform: the scalar unit $e_t$ is treated on the same footing as the vector units $\vec e_x, \vec e_y, \vec e_z$, which makes the algebra look like a graded algebra with a single family of generators. This is the notation used throughout the corpus.

### Basic Properties

**Non-commutative.** Quaternion multiplication is not commutative: $\vec e_x \vec e_y = \vec e_z$ but $\vec e_y \vec e_x = -\vec e_z$.

**Associative.** Quaternion multiplication is associative: $(\tilde q_1\tilde q_2)\tilde q_3 = \tilde q_1(\tilde q_2\tilde q_3)$.

**Conjugation.** The **quaternion conjugate** of $\tilde q$ is

$$
\tilde{q}^{\natural} = q_t e_t - q_x \vec e_x - q_y \vec e_y - q_z \vec e_z,
$$

an involution of the algebra that reverses the order of a product, $(\tilde q_1\tilde q_2)^{\natural} = \tilde q_2^{\natural}\,\bar{\tilde q}_1$.

**Division algebra.** Every non-zero quaternion has a two-sided multiplicative inverse, so $\mathbb{H}$ is a division algebra; it is the largest-dimensional associative real division algebra. The inverse is expressed through the quaternion norm, and the quaternion norm, its multiplicativity and the invertibility criterion it supplies are a form and a distance, developed in *Quaternion Norm and Invertibility* and not here.

**Frobenius theorem.** The quaternion algebra is one of only three finite-dimensional associative real division algebras, the others being $\mathbb{R}$ and $\mathbb{C}$.

### The Vector Part and $\mathbb{R}^3$

The vector part $\vec q$ of a quaternion is identified with a vector in $\mathbb{R}^3$. Under this identification, the product of two quaternions is

$$
\tilde q_1\tilde q_2 = (q_{1t} q_{2t} - \vec q_1 \cdot \vec q_2) + (q_{1t} \vec q_2 + q_{2t} \vec q_1 + \vec q_1 \times \vec q_2),
$$

where $\vec q_1 \cdot \vec q_2$ is the ordinary dot product and $\vec q_1 \times \vec q_2$ is the ordinary cross product in $\mathbb{R}^3$. The dot product and cross product are not separate operations; they are the scalar and vector parts of a single quaternion product.

## The Algebra Structure

### Definition

The **quaternion algebra** is the algebra $\mathbb{H}$ considered as a four-dimensional real vector space equipped with its multiplication. As a real vector space, $\mathbb{H}$ has dimension $4$. As a ring, it is a division algebra. A general element is written in developed form as

$$
\tilde q = q_t e_t + q_x \vec e_x + q_y \vec e_y + q_z \vec e_z, \qquad q_\mu \in \mathbb{R},
$$

or, more compactly, as

$$
\tilde q = \sum_{\mu\in\{t,x,y,z\}} q_\mu e_\mu, \qquad q_\mu \in \mathbb{R}.
$$

We write

$$
\tilde q = q_t e_t + q_x \vec e_x + q_y \vec e_y + q_z \vec e_z,
$$

where $q_t$ is the **scalar part** and $\vec q$ is the **vector part**.

### Multiplication

The product of two quaternions is defined by extending the real multiplication bilinearly:

$$
\tilde q_1\tilde q_2 = \sum_{\mu\in\{t,x,y,z\}} \sum_{\nu\in\{t,x,y,z\}} q_{1\mu} q_{2\nu} \, e_\mu e_\nu,
$$

where the products $e_\mu e_\nu$ are those of the quaternion algebra. In scalar-vector notation, this becomes

$$
\tilde q_1\tilde q_2 = q_{1t} q_{2t} - \vec q_1 \cdot \vec q_2 + q_{1t} \vec q_2 + q_{2t} \vec q_1 + \vec q_1 \times \vec q_2.
$$

### Conjugations

There are **three** natural conjugations on $\mathbb{H}$, obtained from the quaternion conjugation together with the negation map:

**Quaternion conjugation** $\tilde{q}^{\natural}$:

$$
\tilde{q}^{\natural} = q_t e_t - q_x \vec e_x - q_y \vec e_y - q_z \vec e_z.
$$

**Vector conjugation** $-\tilde{q}^{\natural}$:

$$
-\tilde{q}^{\natural} = -q_t e_t + q_x \vec e_x + q_y \vec e_y + q_z \vec e_z.
$$

**Total conjugation** $-\tilde q$:

$$
-\tilde q = -q_t e_t - q_x \vec e_x - q_y \vec e_y - q_z \vec e_z.
$$

Each conjugation is an involution: applying it twice returns the original quaternion. Each has a fixed-point set, which is a real vector subspace of $\mathbb{H}$. The three subspaces are described in the following sections.

## The Three Subspaces

Each of the three conjugations has a fixed-point set, i.e., a set of quaternions left invariant by the conjugation. Each fixed-point set is a real vector subspace of $\mathbb{H}$. The three subspaces are described below.

### The Real Subspace

The fixed points of **quaternion conjugation** are the quaternions satisfying $\tilde{q}^{\natural} = \tilde q$. In developed form,

$$
q_t e_t - q_x \vec e_x - q_y \vec e_y - q_z \vec e_z = q_t e_t + q_x \vec e_x + q_y \vec e_y + q_z \vec e_z.
$$

Comparing the scalar and vector parts:

- Scalar part: $q_t = q_t$, always satisfied.
- Vector part: $-\vec q = \vec q$, so $\vec q = 0$.

The fixed points are quaternions with vanishing vector part:

$$
\tilde q = q_t, \qquad q_t \in \mathbb{R}.
$$

This is the **real subspace** $\mathbb{R}_{\mathbb{H}}$, a copy of the real number line embedded in $\mathbb{H}$ as the scalar axis. It is a real vector space of dimension $1$. It is a subalgebra of $\mathbb{H}$ (isomorphic to $\mathbb{R}$), and it is the only one of the three fixed-point sets that is an ordered field.

### The Vector Subspace

The fixed points of **vector conjugation** are the quaternions satisfying $-\tilde{q}^{\natural} = \tilde q$. In developed form,

$$
-q_t e_t + q_x \vec e_x + q_y \vec e_y + q_z \vec e_z = q_t e_t + q_x \vec e_x + q_y \vec e_y + q_z \vec e_z.
$$

Comparing the scalar and vector parts:

- Scalar part: $-q_t = q_t$, so $q_t = 0$.
- Vector part: $\vec q = \vec q$, always satisfied.

The fixed points are quaternions with vanishing scalar part:

$$
\tilde q = \vec q, \qquad \vec q \in \mathbb{R}^3.
$$

This is the **vector subspace** $\operatorname{Im}\mathbb{H}$, a copy of three-dimensional space embedded in $\mathbb{H}$ as the pure imaginary quaternions. It is a real vector space of dimension $3$. It is not a subalgebra of $\mathbb{H}$: the product of two pure quaternions is not pure, because it has a scalar part $-\vec q_1 \cdot \vec q_2$.

### The Total Subspace

The fixed points of **total conjugation** are the quaternions satisfying $-\tilde q = \tilde q$. In developed form,

$$
-q_t e_t - q_x \vec e_x - q_y \vec e_y - q_z \vec e_z = q_t e_t + q_x \vec e_x + q_y \vec e_y + q_z \vec e_z.
$$

Comparing the scalar and vector parts:

- Scalar part: $-q_t = q_t$, so $q_t = 0$.
- Vector part: $-\vec q = \vec q$, so $\vec q = 0$.

The fixed points are

$$
\tilde q = 0.
$$

This is the **zero subspace**, a real vector space of dimension $0$.

## The Scalar–Vector Decomposition

The real subspace $\mathbb{R}_{\mathbb{H}}$ and the vector subspace $\operatorname{Im}\mathbb{H}$ are the two eigenspaces of quaternion conjugation. Every quaternion decomposes uniquely as the sum of a scalar part and a vector part:

$$
\tilde q = q_r + q_v, \qquad q_r \in \mathbb{R}, \quad q_v \in \mathbb{R}^3.
$$

The two components are obtained from the quaternion conjugation:

$$
q_r = \frac{1}{2}(\tilde q + \tilde{q}^{\natural}), \qquad q_v = \frac{1}{2}(\tilde q - \tilde{q}^{\natural}).
$$

Indeed, $q_r$ is fixed by quaternion conjugation, so it lies in $\mathbb{R}_{\mathbb{H}}$, and $q_v$ satisfies $\tilde{q}^{\natural}_v = -q_v$, so it lies in $\operatorname{Im}\mathbb{H}$.

This gives the direct sum decomposition

$$
\mathbb{H} = \mathbb{R}_{\mathbb{H}} \oplus \operatorname{Im}\mathbb{H},
$$

where $\operatorname{Im}\mathbb{H}$ is the set of pure quaternions. Both are real vector spaces of dimensions $1$ and $3$, and their direct sum is the full algebra $\mathbb{H}$ of real dimension $4$.

This is the **scalar-vector decomposition** of a quaternion. It expresses $\tilde q$ as a real number plus a vector in $\mathbb{R}^3$.

## The Conjugate Decomposition

The quaternion conjugation ${}^{\natural}$ is an involution, so it has eigenvalues $+1$ and $-1$. Its eigenspaces are the real subspace $\mathbb{R}_{\mathbb{H}}$ (eigenvalue $+1$) and the vector subspace $\operatorname{Im}\mathbb{H}$ (eigenvalue $-1$). Every quaternion decomposes uniquely as

$$
\tilde q = q_+ + q_-, \qquad q_+ = q_r, \quad q_- = q_v.
$$

This is the same decomposition as above, written in terms of the eigenspaces of the conjugation.

Here the centre of $\mathbb{H}$ is the real line and the only involution is quaternion conjugation, so the conjugate decomposition above is the only one, and the scalar–vector decomposition within it is the single decomposition from which the quaternion norm is read. The quaternion norm, its polarisation, the Hermitian form and the inner product are a form and a distance: they are developed in *Quaternion Norm and Invertibility*, in the topology group, and are only named here.

## The Lie Algebra Structure

The quaternion algebra carries a Lie bracket, defined by the commutator

$$
[\tilde q_1, \tilde q_2] = \tilde q_1\tilde q_2 - \tilde q_2\tilde q_1.
$$

For pure quaternions $\vec q_1, \vec q_2 \in \operatorname{Im}\mathbb{H}$, the commutator is

$$
[\vec q_1, \vec q_2] = 2 \vec q_1 \times \vec q_2.
$$

So the vector subspace $\operatorname{Im}\mathbb{H}$, equipped with the commutator bracket, is a Lie subalgebra of $\mathbb{H}$ isomorphic to the Lie algebra $\mathrm{SO}(3)$ of skew-symmetric $3\times 3$ real matrices:

$$
\operatorname{Im}\mathbb{H} \cong \mathrm{SO}(3).
$$

This is the algebraic origin of the Lie algebra structure that the pure quaternions carry, and of the relation of the algebra to the orthogonal Lie algebra. Its geometric reading — the motions the bracket generates on the vector subspace — belongs to the geometry group and is developed in *Quaternion Rotations and Reflections* and *Quaternion Automorphisms and Derivations*.

## The Tensor Product Decomposition

The Clifford algebra of an orthogonal direct sum of two quadratic spaces is the graded tensor product of the Clifford algebras of the summands, and the quaternion algebra is obtained as such a Clifford algebra. For the quaternion algebra itself the relevant decomposition is

$$
\mathbb{H} \otimes_{\mathbb{R}} \mathbb{H} \cong M_4(\mathbb{R}),
$$

the algebra of $4 \times 4$ real matrices. More generally, the tensor product of two quaternion algebras is a matrix algebra over $\mathbb{R}$, and the specific size depends on the quadratic forms.

The tensor product decomposition is the algebraic content of the classification of Clifford algebras, and the quaternion algebra is the case $n = 2$ of the classification. The general classification is the subject of the article *Clifford Algebras in Finite Dimensions*.

## Summary

The quaternion algebra $\mathbb{H}$ is the four-dimensional real algebra with basis $e_t = 1, \vec e_x, \vec e_y, \vec e_z$, in which $e_t$ is the unit, the three imaginary units square to $-e_t$, and distinct imaginary units anticommute. It is associative with unit, non-commutative, and a division algebra: every non-zero element is invertible, the inverse being expressed through the quaternion norm of *Quaternion Norm and Invertibility*. A general element is written in developed form as $\tilde q = q_t e_t + q_x \vec e_x + q_y \vec e_y + q_z \vec e_z$.

The algebra carries three conjugations, and each has its fixed-point subspace; the fundamental one is quaternion conjugation, whose fixed points form the real subspace $\mathbb{R}_{\mathbb{H}}$ and whose anti-fixed points form the vector subspace $\operatorname{Im}\mathbb{H}$. These are the eigenspaces for the eigenvalues $+1$ and $-1$, and every quaternion decomposes uniquely both as a scalar part plus a vector part and as the sum of the two eigencomponents.

The commutator $[\tilde q_1,\tilde q_2] = \tilde q_1\tilde q_2 - \tilde q_2\tilde q_1$ gives $\mathbb{H}$ a Lie algebra structure, in which the commutator of two pure quaternions is expressed by the vector product on $\mathbb{R}^3$; the vector subspace is thereby the orthogonal Lie algebra $\mathrm{SO}(3)$. The article closes with the tensor product decomposition, in which the Clifford algebra of a direct sum is the graded tensor product of the Clifford algebras of the summands, giving $\mathbb{H}\otimes_{\mathbb{R}}\mathbb{H}\cong M_4(\mathbb{R})$. The quaternion norm, its polarisation, the Hermitian form and the inner product are a form and a distance and belong to the topology group, in *Quaternion Norm and Invertibility*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | Quaternion algebra |
| $e_t = 1$ | Identity |
| $\vec e_x, \vec e_y, \vec e_z$ | Quaternion units, $\vec e_\mu^2 = -e_t$ |
| $\tilde q = q_t e_t + q_x \vec e_x + q_y \vec e_y + q_z \vec e_z$ | General quaternion |
| $q_t$ | Scalar part |
| $\vec q$ | Vector part |
| $\tilde{q}^{\natural} = q_t e_t - q_x \vec e_x - q_y \vec e_y - q_z \vec e_z$ | Quaternion conjugate |
| $-\tilde{q}^{\natural} = -q_t e_t + q_x \vec e_x + q_y \vec e_y + q_z \vec e_z$ | Vector conjugate |
| $-\tilde q = -q_t e_t - q_x \vec e_x - q_y \vec e_y - q_z \vec e_z$ | Total conjugate |
| $\mathbb{R}_{\mathbb{H}}$ | Real subspace, fixed-point set of ${}^{\natural}$ |
| $\operatorname{Im}\mathbb{H}$ | Vector subspace, fixed-point set of the vector conjugate, $q\mapsto-\tilde q^{\natural}$ |
| $\mathrm{SO}(3)$ | Lie algebra of rotations |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original formulation.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the classification of real algebras.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton, 1989), for the role of quaternions in geometry.
