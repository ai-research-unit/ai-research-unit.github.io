
# Biquaternion Algebra

## Introduction

This article introduces the biquaternion algebra as an algebraic structure, without yet discussing its representations. The goal is to define the algebra precisely, establish its basic properties, and describe the four distinguished real vector subspaces that arise from the natural conjugations.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. The anti-Hermitian subspace is defined algebraically, and its identification with spacetime is left for a later article.

The quaternion algebra $\mathbb{H}$ is assumed from the article on quaternion algebra, together with its basis, its multiplication, its conjugation, and its norm. No facts about $\mathbb{H}$ are restated here.

## Biquaternions

### Definition

The **biquaternion algebra** is the complexification of the quaternion algebra:

$$
\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}.
$$

### Two Views: Over $\mathbb{C}$ and Over $\mathbb{R}$

The biquaternion algebra can be viewed in two equivalent ways, depending on which scalars we allow.

**As a $\mathbb{C}$-algebra.** The tensor product $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ is naturally a module over $\mathbb{C}$, with the complex scalars acting on the first factor. In this view, $\mathbb{B}$ is a **four-dimensional algebra over $\mathbb{C}$**: its complex basis is $\{e_0, e_1, e_2, e_3\}$, and every element is a $\mathbb{C}$-linear combination of these four basis elements. The multiplication is $\mathbb{C}$-bilinear, and the algebra is associative and unital, with unit $e_0$. The center of this $\mathbb{C}$-algebra is $\mathbb{C}$.

**As an $\mathbb{R}$-algebra.** Forgetting the $\mathbb{C}$-module structure, the same set $\mathbb{B}$ is also naturally a **real vector space of dimension $8$**, with real basis $\{e_0, e_1, e_2, e_3, i e_0, i e_1, i e_2, i e_3\}$. In this view, $\mathbb{B}$ is an **eight-dimensional algebra over $\mathbb{R}$**. The multiplication is $\mathbb{R}$-bilinear, and the algebra is associative and unital, with unit $e_0$. The scalar imaginary $i$ is now an element of the algebra itself, not a scalar, and it lies in the center.

The two views are related by a change of base ring: passing from the $\mathbb{R}$-algebra to the $\mathbb{C}$-algebra is the operation of **extension of scalars** from $\mathbb{R}$ to $\mathbb{C}$, and passing back is the operation of **restriction of scalars**. The dimension changes as follows:

$$
\dim_{\mathbb{R}} \mathbb{B} = 2 \cdot \dim_{\mathbb{C}} \mathbb{B},
$$

because each complex dimension contributes two real dimensions (the real and imaginary parts of each complex coefficient).

**Which view to use.** The two views are complementary, and both are used in the literature.

- The **$\mathbb{C}$-algebra view** is the natural one when the biquaternions are studied as a complex algebra, for instance in the context of complex representations, complex Lie algebras, or the algebra $M_2(\mathbb{C})$ of $2 \times 2$ complex matrices. In this view, the algebra is four-dimensional and its structure is relatively simple: it is isomorphic to $M_2(\mathbb{C})$.

- The **$\mathbb{R}$-algebra view** is the natural one when the biquaternions are studied as a real algebra, for instance in the context of real representations, real Clifford algebras, or applications to physics. In this view, the algebra is eight-dimensional, and the four real subspaces $\mathbb{C}_{\mathbb{B}}$, $\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$, $\mathbb{M}_-$ that we describe below are all real vector subspaces of this eight-dimensional real algebra.

In this article we use both views, and we indicate which one is in force whenever it matters. When we say "$\mathbb{B}$ is four-dimensional," we mean over $\mathbb{C}$. When we say "$\mathbb{B}$ is eight-dimensional," we mean over $\mathbb{R}$. The context will make the field clear.

### Developed Form

A general biquaternion is written in developed form as

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3, \qquad Q_\mu \in \mathbb{C},
$$

or, more compactly, as

$$
\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu, \qquad Q_\mu \in \mathbb{C}.
$$

We write

$$
\tilde{Q} = Q_0 + \mathbf{Q}, \qquad \mathbf{Q} = \sum_{k=1}^{3} Q_k e_k,
$$

where $Q_0$ is the **complex scalar part** and $\mathbf{Q}$ is the **complex vector part**. The tilde signals that $\tilde{Q}$ is an element of the algebra $\mathbb{B}$, not a four-vector.

Each complex coefficient is written in terms of its real and imaginary parts:

$$
Q_0 = q_0 + i q'_0, \qquad Q_k = q_k + i q'_k, \qquad q_\mu, q'_\mu \in \mathbb{R}.
$$

The scalar imaginary $i$ satisfies $i^2 = -1$ and commutes with all quaternion units: $i e_k = e_k i$.

When $\mathbb{B}$ is viewed as a real vector space of dimension 8, the eight real coordinates of $\tilde{Q}$ are $(q_0, q_1, q_2, q_3, q'_0, q'_1, q'_2, q'_3)$. When $\mathbb{B}$ is viewed as a complex vector space of dimension 4, the four complex coordinates are $(Q_0, Q_1, Q_2, Q_3)$.

### The Algebra Structure

The algebra $\mathbb{B}$ is a four-dimensional algebra over $\mathbb{C}$, and simultaneously an eight-dimensional algebra over $\mathbb{R}$. In both views it is non-commutative and associative. It is not a division algebra: it has zero divisors, and the study of these is the subject of the divisibility article.

The **center** of $\mathbb{B}$ is $\mathbb{C}$ in both views, but with a subtlety. As a $\mathbb{C}$-algebra, the center is the scalar copy of $\mathbb{C}$ spanned by $e_0$: an element $\tilde{Q}$ is central iff it commutes with every quaternion unit, and the only such elements are the complex scalars $\tilde{Q} = Q_0 e_0$ with $Q_0 \in \mathbb{C}$. As an $\mathbb{R}$-algebra, the same center $\mathbb{C}$ is a real vector space of dimension 2, spanned by $e_0$ and $i e_0$.

### Multiplication

The product of two biquaternions is defined by extending the quaternion product complex-linearly. In developed form,

$$
\tilde{Q} \circ \tilde{R} = \sum_{\mu=0}^{3} \sum_{\nu=0}^{3} Q_\mu R_\nu \, e_\mu e_\nu,
$$

where the products $e_\mu e_\nu$ are those of the quaternion algebra, extended complex-linearly. In scalar-vector notation, this becomes

$$
\tilde{Q} \circ \tilde{R} = Q_0 R_0 - (\mathbf{Q}, \mathbf{R}) + Q_0 \mathbf{R} + R_0 \mathbf{Q} + [\mathbf{Q}, \mathbf{R}],
$$

where

$$
(\mathbf{Q}, \mathbf{R}) = \sum_{k=1}^{3} Q_k R_k, \qquad [\mathbf{Q}, \mathbf{R}] = \sum_{j,k,l=1}^{3} \epsilon_{jkl} Q_j R_k e_l.
$$

The symbols $(\mathbf{Q}, \mathbf{R})$ and $[\mathbf{Q}, \mathbf{R}]$ denote the **complex bilinear dot product** and the **complex bilinear cross product**. They reduce to the ordinary dot product and cross product when the coefficients are real.

This formula has the same structure as the quaternion product: scalar part, vector part, dot product, cross product. The only difference is that the coefficients are now complex.

### Conjugations

There are **four** natural conjugations on $\mathbb{B}$, obtained by composing the quaternion conjugation $\bar{\cdot}$ and the complex conjugation ${}^*$:

**Quaternion conjugation** $\bar{\tilde{Q}}$:

$$
\bar{\tilde{Q}} = Q_0 e_0 - Q_1 e_1 - Q_2 e_2 - Q_3 e_3.
$$

**Complex conjugation** $\tilde{Q}^*$:

$$
\tilde{Q}^* = Q_0^* e_0 + Q_1^* e_1 + Q_2^* e_2 + Q_3^* e_3.
$$

**Hermitian conjugation** $\tilde{Q}^\dagger = \bar{\tilde{Q}}^*$:

$$
\tilde{Q}^\dagger = Q_0^* e_0 - Q_1^* e_1 - Q_2^* e_2 - Q_3^* e_3.
$$

**Anti-Hermitian conjugation** $\tilde{Q}^\flat = -\tilde{Q}^\dagger$:

$$
\tilde{Q}^\flat = -Q_0^* e_0 + Q_1^* e_1 + Q_2^* e_2 + Q_3^* e_3.
$$

Each conjugation is an involution: applying it twice returns the original biquaternion. Each has a fixed-point set, which is a real vector subspace of $\mathbb{B}$.

### The Group of Conjugations

The four conjugations form a group under composition, isomorphic to $\mathbb{Z}/2 \times \mathbb{Z}/2$. The group is generated by the quaternion conjugation $\bar{\cdot}$ and the complex conjugation ${}^*$, which commute:

$$
\bar{\tilde{Q}}^* = \tilde{Q}^{*\bar{}}.
$$

The Hermitian conjugation is the composition of the two:

$$
\tilde{Q}^\dagger = \bar{\tilde{Q}}^* = \tilde{Q}^{*\bar{}}.
$$

The anti-Hermitian conjugation is the negative of the Hermitian conjugation:

$$
\tilde{Q}^\flat = -\tilde{Q}^\dagger.
$$

So the four conjugations are not independent: they are determined by the two commuting involutions $\bar{\cdot}$ and ${}^*$, together with the sign choice in the definition of $\flat$.

## The Four Fixed-Point Subspaces

Each of the four conjugations has a fixed-point set, i.e., a set of biquaternions left invariant by the conjugation. Each fixed-point set is a real vector subspace of $\mathbb{B}$. The four subspaces are described below.

### The Complex Subspace

The fixed points of **quaternion conjugation** are the biquaternions satisfying $\bar{\tilde{Q}} = \tilde{Q}$. In developed form,

$$
Q_0 e_0 - Q_1 e_1 - Q_2 e_2 - Q_3 e_3 = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3.
$$

Comparing the coefficients of $e_0, e_1, e_2, e_3$:

- Coefficient of $e_0$: $Q_0 = Q_0$, always satisfied.
- Coefficient of $e_1$: $-Q_1 = Q_1$, so $Q_1 = 0$.
- Coefficient of $e_2$: $-Q_2 = Q_2$, so $Q_2 = 0$.
- Coefficient of $e_3$: $-Q_3 = Q_3$, so $Q_3 = 0$.

The fixed points are biquaternions with vanishing vector part:

$$
\tilde{Q} = Q_0 e_0, \qquad Q_0 \in \mathbb{C}.
$$

This is the **complex subspace** $\mathbb{C}_{\mathbb{B}}$, a copy of the complex number line embedded in $\mathbb{B}$ as the scalar part. It is a real vector space of dimension 2. It is a subalgebra of $\mathbb{B}$ (isomorphic to $\mathbb{C}$), it is commutative, and it coincides with the center of $\mathbb{B}$.

### The Quaternion Subspace

The fixed points of **complex conjugation** are the biquaternions satisfying $\tilde{Q}^* = \tilde{Q}$. In developed form,

$$
Q_0^* e_0 + Q_1^* e_1 + Q_2^* e_2 + Q_3^* e_3 = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3.
$$

Comparing the coefficients:

- $Q_0^* = Q_0$, so $Q_0$ is real.
- $Q_1^* = Q_1$, so $Q_1$ is real.
- $Q_2^* = Q_2$, so $Q_2$ is real.
- $Q_3^* = Q_3$, so $Q_3$ is real.

The fixed points are biquaternions with real coefficients:

$$
\tilde{Q} = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3, \qquad q_\mu \in \mathbb{R}.
$$

This is the **quaternion subspace** $\mathbb{H}_{\mathbb{B}}$, a copy of the real quaternion algebra embedded in $\mathbb{B}$. It is a real vector space of dimension 4. It is a subalgebra of $\mathbb{B}$, isomorphic to $\mathbb{H}$.

### The Hermitian Subspace

The fixed points of **Hermitian conjugation** are the biquaternions satisfying $\tilde{Q}^\dagger = \tilde{Q}$. In developed form,

$$
Q_0^* e_0 - Q_1^* e_1 - Q_2^* e_2 - Q_3^* e_3 = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3.
$$

Comparing the coefficients:

- $Q_0^* = Q_0$, so $Q_0$ is real.
- $-Q_1^* = Q_1$, so $Q_1^* = -Q_1$, which means $Q_1$ is purely imaginary.
- Similarly, $Q_2$ and $Q_3$ are purely imaginary.

The fixed points are biquaternions of the form

$$
\tilde{Q} = q_0 e_0 + i q'_1 e_1 + i q'_2 e_2 + i q'_3 e_3, \qquad q_0, q'_1, q'_2, q'_3 \in \mathbb{R}.
$$

This is the **Hermitian subspace** $\mathbb{M}_+$, a real vector space of dimension 4. It consists of biquaternions with real scalar part and purely imaginary vector part. It is not a subalgebra of $\mathbb{B}$.

### The Anti-Hermitian Subspace

The fixed points of **anti-Hermitian conjugation** are the biquaternions satisfying $\tilde{Q}^\flat = \tilde{Q}$, or equivalently $\tilde{Q} = -\tilde{Q}^\dagger$. In developed form,

$$
-Q_0^* e_0 + Q_1^* e_1 + Q_2^* e_2 + Q_3^* e_3 = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3.
$$

Comparing the coefficients:

- $-Q_0^* = Q_0$, so $Q_0^* = -Q_0$, which means $Q_0$ is purely imaginary.
- $Q_1^* = Q_1$, so $Q_1$ is real.
- Similarly, $Q_2$ and $Q_3$ are real.

The fixed points are biquaternions of the form

$$
\tilde{Q} = i q'_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3, \qquad q'_0, q_1, q_2, q_3 \in \mathbb{R}.
$$

This is the **anti-Hermitian subspace** $\mathbb{M}_-$, a real vector space of dimension 4. It consists of biquaternions with purely imaginary scalar part and real vector part. It is not a subalgebra of $\mathbb{B}$.

## Quaternion Decomposition

The complex subspace $\mathbb{C}_{\mathbb{B}}$ and the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ are **not** the two eigenspaces of a single involution; they are different fixed-point sets. However, there is a natural decomposition of $\mathbb{B}$ associated with the complex conjugation ${}^*$.

Every biquaternion can be written uniquely as

$$
\tilde{Q} = \tilde{Q}_r + i \tilde{Q}_i,
$$

where $\tilde{Q}_r$ and $\tilde{Q}_i$ are **ordinary quaternions** (elements of $\mathbb{H}$ embedded in $\mathbb{B}$), with real coefficients. The two components are

$$
\tilde{Q}_r = \frac{1}{2}(\tilde{Q} + \tilde{Q}^*), \qquad \tilde{Q}_i = \frac{1}{2i}(\tilde{Q} - \tilde{Q}^*).
$$

Indeed, $\tilde{Q}_r$ is fixed by complex conjugation, so it lies in the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, and $\tilde{Q}_i$ satisfies $\tilde{Q}_i^* = -\tilde{Q}_i$, so $i\tilde{Q}_i$ is fixed by complex conjugation, meaning $\tilde{Q}_i$ also lies in $\mathbb{H}_{\mathbb{B}}$. The sum is $\tilde{Q}_r + i \tilde{Q}_i = \tilde{Q}$.

This gives the direct sum decomposition

$$
\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i \mathbb{H}_{\mathbb{B}},
$$

where $i\mathbb{H}_{\mathbb{B}}$ is the set of biquaternions of the form $i \tilde{Q}$ with $\tilde{Q} \in \mathbb{H}_{\mathbb{B}}$. Both are real vector spaces of dimension 4, and their direct sum is the full algebra $\mathbb{B}$ of real dimension 8.

This is the **quaternion decomposition** of a biquaternion. It expresses $\tilde{Q}$ as a quaternion plus the scalar imaginary times another quaternion. It is the natural decomposition when we think of $\mathbb{B}$ as the complexification of $\mathbb{H}$: the first summand is the "real part" and the second is the "imaginary part" of the complexification.

## Hermitian Decomposition

The Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$ are the two eigenspaces of the Hermitian conjugation $\dagger$. Every biquaternion decomposes uniquely as the sum of a Hermitian part and an anti-Hermitian part:

$$
\tilde{Q} = \tilde{Q}_+ + \tilde{Q}_-, \qquad \tilde{Q}_+ \in \mathbb{M}_+, \quad \tilde{Q}_- \in \mathbb{M}_-.
$$

The two components are obtained from the Hermitian conjugation:

$$
\tilde{Q}_+ = \frac{1}{2}(\tilde{Q} + \tilde{Q}^\dagger), \qquad \tilde{Q}_- = \frac{1}{2}(\tilde{Q} - \tilde{Q}^\dagger).
$$

Indeed, $\tilde{Q}_+$ is fixed by Hermitian conjugation, so it lies in $\mathbb{M}_+$, and $\tilde{Q}_-$ satisfies $\tilde{Q}_-^\dagger = -\tilde{Q}_-$, so it lies in $\mathbb{M}_-$. The sum is $\tilde{Q}_+ + \tilde{Q}_- = \tilde{Q}$.

This gives the direct sum decomposition

$$
\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-,
$$

where $\mathbb{M}_+$ is the Hermitian subspace and $\mathbb{M}_-$ is the anti-Hermitian subspace. Both are real vector spaces of dimension 4, and their direct sum is the full algebra $\mathbb{B}$ of real dimension 8.

The decomposition is the algebraic analogue of writing a complex number as the sum of its real and imaginary parts. Here, however, both components are biquaternions, and the two subspaces $\mathbb{M}_+$ and $\mathbb{M}_-$ are not subalgebras of $\mathbb{B}$; the decomposition is a vector-space decomposition, not an algebra decomposition.

## Relation Between the Two Decompositions

The quaternion decomposition $\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i \mathbb{H}_{\mathbb{B}}$ and the Hermitian decomposition $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$ are two different decompositions of the same eight-dimensional real vector space. They are associated with two different involutions: the quaternion decomposition is associated with the complex conjugation ${}^*$, and the Hermitian decomposition is associated with the Hermitian conjugation $\dagger$.

The two decompositions are related by the quaternion conjugation. Indeed, the quaternion conjugation maps $\mathbb{M}_+$ to $\mathbb{M}_-$ and vice versa:

$$
\overline{\mathbb{M}_+} = \mathbb{M}_-, \qquad \overline{\mathbb{M}_-} = \mathbb{M}_+.
$$

So the quaternion conjugation swaps the two summands of the Hermitian decomposition, and the Hermitian conjugation swaps the two summands of the quaternion decomposition. The two decompositions are complementary, and they together generate the full structure of the algebra as a real vector space with four distinguished subspaces.

## Quadratic Forms and Inner Product

### The Norm Form

The **norm form** of a biquaternion $\tilde{Q}$ is

$$
N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}} = \sum_{\mu=0}^{3} Q_\mu^2,
$$

where $\bar{\tilde{Q}}$ is the quaternion conjugate. It is a complex number in general. It is not positive-definite, and it can vanish for a nonzero biquaternion. The vanishing of the norm form and the structure of the elements on which it vanishes are the subject of the divisibility article.

The norm form is **multiplicative**:

$$
N(\tilde{Q} \circ \tilde{R}) = N(\tilde{Q}) \, N(\tilde{R}).
$$

### The Hermitian Form

The **Hermitian form** of a biquaternion $\tilde{Q}$ is

$$
\tilde{Q} \tilde{Q}^\dagger = \sum_{\mu=0}^{3} |Q_\mu|^2 = \sum_{\mu=0}^{3} (q_\mu^2 + q'^2_\mu),
$$

where $\tilde{Q}^\dagger$ is the Hermitian conjugate. It is a **non-negative real number**, and it vanishes if and only if $\tilde{Q} = 0$. It is a genuine positive-definite quadratic form, and it is the natural "length squared" of $\tilde{Q}$ in the underlying real vector space of dimension 8.

The corresponding **Euclidean norm** is

$$
\|\tilde{Q}\|_E = \sqrt{\tilde{Q} \tilde{Q}^\dagger} = \sqrt{\sum_{\mu=0}^{3} |Q_\mu|^2}.
$$

It is a genuine norm on the real vector space $\mathbb{B} \cong \mathbb{R}^8$: positive-definite, subadditive, and homogeneous of degree one. It is **not** multiplicative with respect to the biquaternion product.

### The Inner Product

The **inner product** of two biquaternions $\tilde{P}$ and $\tilde{Q}$ is

$$
\langle \tilde{P}, \tilde{Q} \rangle = \sum_{\mu=0}^{3} P_\mu^* Q_\mu = \sum_{\mu=0}^{3} (p_\mu q_\mu + p'_\mu q'_\mu) + i \sum_{\mu=0}^{3} (p'_\mu q_\mu - p_\mu q'_\mu).
$$

In general this is a **complex number**, not a real one. This is a genuinely biquaternionic feature: the inner product of two biquaternions is complex, and its imaginary part measures the "phase" between them.

The inner product is linear in the second argument and anti-linear in the first:

$$
\langle \lambda \tilde{P}, \tilde{Q} \rangle = \lambda^* \langle \tilde{P}, \tilde{Q} \rangle, \qquad \langle \tilde{P}, \lambda \tilde{Q} \rangle = \lambda \langle \tilde{P}, \tilde{Q} \rangle, \qquad \lambda \in \mathbb{C}.
$$

It is **Hermitian** in the sense that

$$
\langle \tilde{P}, \tilde{Q} \rangle^* = \langle \tilde{Q}, \tilde{P} \rangle,
$$

which follows from the definition.

The inner product of a biquaternion with itself is

$$
\langle \tilde{Q}, \tilde{Q} \rangle = \tilde{Q} \tilde{Q}^\dagger = \sum_{\mu=0}^{3} |Q_\mu|^2,
$$

which is the Hermitian form. So the Hermitian form is the restriction of the inner product to the diagonal.

### Relation Between the Three Forms

The three quadratic objects are related as follows:

- **Norm form:** $N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}} = \sum_\mu Q_\mu^2$. Complex-valued, can vanish for nonzero $\tilde{Q}$, multiplicative.
- **Hermitian form:** $\tilde{Q} \tilde{Q}^\dagger = \sum_\mu |Q_\mu|^2$. Non-negative real, vanishes only at $\tilde{Q} = 0$, not multiplicative.
- **Inner product:** $\langle \tilde{P}, \tilde{Q} \rangle = \sum_\mu P_\mu^* Q_\mu$. Complex-valued in general, Hermitian, linear in the second argument.

The three are distinct, and each is useful in a different context. The norm form controls the multiplicative structure. The Hermitian form controls the topological structure (continuity, completeness). The inner product combines both, and is the natural pairing on the algebra as a complex vector space.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | Quaternion algebra |
| $\mathbb{B}$ | Biquaternion algebra, $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ |
| $e_0 = 1$ | Identity |
| $e_1, e_2, e_3$ | Quaternion units, $e_k^2 = -e_0$ |
| $i$ | Scalar imaginary, $i^2 = -1$, commutes with $e_k$ |
| $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ | General biquaternion |
| $Q_\mu = q_\mu + i q'_\mu$ | Complex coefficient, with $q_\mu, q'_\mu \in \mathbb{R}$ |
| $Q_0$ | Complex scalar part |
| $\mathbf{Q}$ | Complex vector part |
| $\bar{\tilde{Q}} = Q_0 e_0 - \mathbf{Q}$ | Quaternion conjugate |
| $\tilde{Q}^* = Q_0^* e_0 + \mathbf{Q}^*$ | Complex conjugate |
| $\tilde{Q}^\dagger = Q_0^* e_0 - \mathbf{Q}^*$ | Hermitian conjugate |
| $\tilde{Q}^\flat = -\bar{\tilde{Q}}^* = -\tilde{Q}^\dagger$ | Anti-Hermitian conjugate |
| $N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}}$ | Norm form |
| $\tilde{Q} \tilde{Q}^\dagger$ | Hermitian form |
| $\langle \tilde{P}, \tilde{Q} \rangle = \sum_\mu P_\mu^* Q_\mu$ | Inner product |
| $\|\tilde{Q}\|_E = \sqrt{\tilde{Q} \tilde{Q}^\dagger}$ | Euclidean norm |
| $\mathbb{C}_{\mathbb{B}}$ | Complex subspace, fixed-point set of $\bar{\cdot}$ |
| $\mathbb{H}_{\mathbb{B}}$ | Quaternion subspace, fixed-point set of ${}^*$ |
| $\mathbb{M}_+$ | Hermitian subspace, fixed-point set of $\dagger$ |
| $\mathbb{M}_-$ | Anti-Hermitian subspace, fixed-point set of $\flat$ |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original formulation.
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the first systematic treatment of biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra perspective.

