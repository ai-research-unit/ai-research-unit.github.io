
# __Quaternion Algebra__

## Introduction

This article introduces the quaternion algebra as an algebraic structure. The goal is to define the algebra precisely, establish its basic properties, and describe the distinguished real vector subspaces that arise from the natural conjugations.

The quadratic form the algebra carries — its polarisation, the Hermitian form and the inner product — is a form and a distance, and a norm is a distance: these belong to the topology group, in *Quaternion Norm and Invertibility*, and the present article only names them. The geometric reading of the algebra is likewise deferred to the geometry group, in *Quaternion Rotations and Reflections*.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. No examples are given.

## Quaternions

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
\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3, \qquad q_\mu \in \mathbb{R},
$$

or, more compactly, as

$$
\tilde q = \sum_{\mu=0}^{3} q_\mu e_\mu, \qquad q_\mu \in \mathbb{R}.
$$

The real number $q_0$ is the **scalar part**, and the triple $(q_1, q_2, q_3)$ is the **vector part**. We also write

$$
\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3, \qquad \mathbf{q} = \sum_{k=1}^{3} q_k e_k.
$$

### A Note on the Notation

The notation $e_1, e_2, e_3$ is chosen deliberately, and it replaces the classical notation $i, j, k$ used in the older literature. The reason is that the symbols $i, j, k$ collide with other standard notations:

- The symbol $i$ is universally used for the scalar imaginary unit of the complex numbers, with $i^2 = -1$. In the quaternion algebra, the unit $e_1$ also satisfies $e_1^2 = -e_0$, so writing it as $i$ makes it visually indistinguishable from the scalar imaginary. This collision becomes acute when the quaternion algebra is complexified: the biquaternion algebra $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ contains both the scalar imaginary $i$ and the quaternion unit $e_1$, and they are different elements. Writing both as $i$ makes the algebra unreadable.
- The symbol $j$ is universally used as an index, as in $a_j$, $e_j$, $x_j$, and so on. Writing the quaternion unit as $j$ makes every expression with an index ambiguous.
- The symbol $k$ is also used as an index, particularly in sums over three variables.

The notation $e_0, e_1, e_2, e_3$ avoids all three collisions. It also has the advantage of being uniform: the scalar unit $e_0$ is treated on the same footing as the vector units $e_1, e_2, e_3$, which makes the algebra look like a graded algebra with a single family of generators. This is the notation used throughout the corpus.

### Basic Properties

**Non-commutative.** Quaternion multiplication is not commutative: $e_1 e_2 = e_3$ but $e_2 e_1 = -e_3$.

**Associative.** Quaternion multiplication is associative: $(pq)r = p(qr)$.

**Conjugation.** The **quaternion conjugate** of $\tilde q$ is

$$
\tilde{q}^{\natural} = q_0 e_0 - q_1 e_1 - q_2 e_2 - q_3 e_3,
$$

an involution of the algebra that reverses the order of a product, $(pq)^{\natural} = \tilde{q}^{\natural}\,\bar p$.

**Division algebra.** Every non-zero quaternion has a two-sided multiplicative inverse, so $\mathbb{H}$ is a division algebra; it is the largest-dimensional associative real division algebra. The inverse is expressed through the quaternion norm, and the quaternion norm, its multiplicativity and the invertibility criterion it supplies are a form and a distance, developed in *Quaternion Norm and Invertibility* and not here.

**Frobenius theorem.** The quaternion algebra is one of only three finite-dimensional associative real division algebras, the others being $\mathbb{R}$ and $\mathbb{C}$.

### The Vector Part and $\mathbb{R}^3$

The vector part $\mathbf{q}$ of a quaternion is identified with a vector in $\mathbb{R}^3$. Under this identification, the product of two quaternions is

$$
pq = (p_0 q_0 - \mathbf{p} \cdot \mathbf{q}) + (p_0 \mathbf{q} + q_0 \mathbf{p} + \mathbf{p} \times \mathbf{q}),
$$

where $\mathbf{p} \cdot \mathbf{q}$ is the ordinary dot product and $\mathbf{p} \times \mathbf{q}$ is the ordinary cross product in $\mathbb{R}^3$. The dot product and cross product are not separate operations; they are the scalar and vector parts of a single quaternion product.

## The Algebra Structure

### Definition

The **quaternion algebra** is the algebra $\mathbb{H}$ considered as a four-dimensional real vector space equipped with its multiplication. As a real vector space, $\mathbb{H}$ has dimension $4$. As a ring, it is a division algebra. A general element is written in developed form as

$$
\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3, \qquad q_\mu \in \mathbb{R},
$$

or, more compactly, as

$$
\tilde q = \sum_{\mu=0}^{3} q_\mu e_\mu, \qquad q_\mu \in \mathbb{R}.
$$

We write

$$
\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3,
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

**Quaternion conjugation** $\tilde{q}^{\natural}$:

$$
\tilde{q}^{\natural} = q_0 e_0 - q_1 e_1 - q_2 e_2 - q_3 e_3.
$$

**Vector conjugation** $-\tilde{q}^{\natural}$:

$$
-\tilde{q}^{\natural} = -q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3.
$$

**Total conjugation** $-\tilde q$:

$$
-\tilde q = -q_0 e_0 - q_1 e_1 - q_2 e_2 - q_3 e_3.
$$

Each conjugation is an involution: applying it twice returns the original quaternion. Each has a fixed-point set, which is a real vector subspace of $\mathbb{H}$. The three subspaces are described in the following sections.

## The Three Subspaces

Each of the three conjugations has a fixed-point set, i.e., a set of quaternions left invariant by the conjugation. Each fixed-point set is a real vector subspace of $\mathbb{H}$. The three subspaces are described below.

### The Real Subspace

The fixed points of **quaternion conjugation** are the quaternions satisfying $\tilde{q}^{\natural} = \tilde q$. In developed form,

$$
q_0 e_0 - q_1 e_1 - q_2 e_2 - q_3 e_3 = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3.
$$

Comparing the scalar and vector parts:

- Scalar part: $q_0 = q_0$, always satisfied.
- Vector part: $-\mathbf{q} = \mathbf{q}$, so $\mathbf{q} = 0$.

The fixed points are quaternions with vanishing vector part:

$$
\tilde q = q_0, \qquad q_0 \in \mathbb{R}.
$$

This is the **real subspace** $\mathbb{R}_{\mathbb{H}}$, a copy of the real number line embedded in $\mathbb{H}$ as the scalar axis. It is a real vector space of dimension $1$. It is a subalgebra of $\mathbb{H}$ (isomorphic to $\mathbb{R}$), and it is the only one of the three fixed-point sets that is an ordered field.

### The Vector Subspace

The fixed points of **vector conjugation** are the quaternions satisfying $-\tilde{q}^{\natural} = \tilde q$. In developed form,

$$
-q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3 = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3.
$$

Comparing the scalar and vector parts:

- Scalar part: $-q_0 = q_0$, so $q_0 = 0$.
- Vector part: $\mathbf{q} = \mathbf{q}$, always satisfied.

The fixed points are quaternions with vanishing scalar part:

$$
\tilde q = \mathbf{q}, \qquad \mathbf{q} \in \mathbb{R}^3.
$$

This is the **vector subspace** $\operatorname{Im}\mathbb{H}$, a copy of three-dimensional space embedded in $\mathbb{H}$ as the pure imaginary quaternions. It is a real vector space of dimension $3$. It is not a subalgebra of $\mathbb{H}$: the product of two pure quaternions is not pure, because it has a scalar part $-\mathbf{p} \cdot \mathbf{q}$.

### The Total Subspace

The fixed points of **total conjugation** are the quaternions satisfying $-\tilde q = \tilde q$. In developed form,

$$
-q_0 e_0 - q_1 e_1 - q_2 e_2 - q_3 e_3 = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3.
$$

Comparing the scalar and vector parts:

- Scalar part: $-q_0 = q_0$, so $q_0 = 0$.
- Vector part: $-\mathbf{q} = \mathbf{q}$, so $\mathbf{q} = 0$.

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

**Remark.** The biquaternion algebra carries three decompositions — the quaternion, the Hermitian and the centre–vector decomposition — because it has a central imaginary unit and a complex conjugation beside the quaternion conjugation. Here the centre of $\mathbb{H}$ is the real line and the only involution is quaternion conjugation, so the conjugate decomposition above is the only one, and the scalar–vector decomposition within it is the single decomposition from which the quaternion norm is read. The quaternion norm, its polarisation, the Hermitian form and the inner product are a form and a distance: they are developed in *Quaternion Norm and Invertibility*, in the topology group, and are only named here.

## The Lie Algebra Structure

The quaternion algebra carries a Lie bracket, defined by the commutator

$$
[p, \tilde q] = pq - qp.
$$

For pure quaternions $\mathbf{p}, \mathbf{q} \in \operatorname{Im}\mathbb{H}$, the commutator is

$$
[\mathbf{p}, \mathbf{q}] = 2 \mathbf{p} \times \mathbf{q}.
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

The quaternion algebra $\mathbb{H}$ is the four-dimensional real algebra with basis $e_0 = 1, e_1, e_2, e_3$, in which $e_0$ is the unit, the three imaginary units square to $-e_0$, and distinct imaginary units anticommute. It is associative with unit, non-commutative, and a division algebra: every non-zero element is invertible, the inverse being expressed through the quaternion norm of *Quaternion Norm and Invertibility*. A general element is written in developed form as $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$.

The algebra carries three conjugations, and each has its fixed-point subspace; the fundamental one is quaternion conjugation, whose fixed points form the real subspace $\mathbb{R}_{\mathbb{H}}$ and whose anti-fixed points form the vector subspace $\operatorname{Im}\mathbb{H}$. These are the eigenspaces for the eigenvalues $+1$ and $-1$, and every quaternion decomposes uniquely both as a scalar part plus a vector part and as the sum of the two eigencomponents.

The commutator $[p,\tilde q] = pq - qp$ gives $\mathbb{H}$ a Lie algebra structure, in which the commutator of two pure quaternions is expressed by the vector product on $\mathbb{R}^3$; the vector subspace is thereby the orthogonal Lie algebra $\mathrm{SO}(3)$. The article closes with the tensor product decomposition, in which the Clifford algebra of a direct sum is the graded tensor product of the Clifford algebras of the summands, giving $\mathbb{H}\otimes_{\mathbb{R}}\mathbb{H}\cong M_4(\mathbb{R})$. The quaternion norm, its polarisation, the Hermitian form and the inner product are a form and a distance and belong to the topology group, in *Quaternion Norm and Invertibility*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | Quaternion algebra |
| $e_0 = 1$ | Identity |
| $e_1, e_2, e_3$ | Quaternion units, $e_k^2 = -e_0$ |
| $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ | General quaternion |
| $q_0$ | Scalar part |
| $\mathbf{q}$ | Vector part |
| $\tilde{q}^{\natural} = q_0 e_0 - q_1 e_1 - q_2 e_2 - q_3 e_3$ | Quaternion conjugate |
| $-\tilde{q}^{\natural} = -q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ | Vector conjugate |
| $-\tilde q = -q_0 e_0 - q_1 e_1 - q_2 e_2 - q_3 e_3$ | Total conjugate |
| $\mathbb{R}_{\mathbb{H}}$ | Real subspace, fixed-point set of ${}^{\natural}$ |
| $\operatorname{Im}\mathbb{H}$ | Vector subspace, fixed-point set of $\tilde{\cdot}$ |
| $\mathrm{SO}(3)$ | Lie algebra of rotations |



## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original formulation.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the classification of real algebras.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton, 1989), for the role of quaternions in geometry.

