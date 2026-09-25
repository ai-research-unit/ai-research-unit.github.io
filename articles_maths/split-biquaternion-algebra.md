# __Split-Biquaternion Algebra__

## Introduction

This article introduces the split biquaternion algebra as an algebraic structure. The goal is to define the algebra precisely, establish its basic properties, and describe the distinguished real vector subspaces that arise from the natural conjugations.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. No examples are given. The quaternion algebra $\mathbb{H}$ is assumed from the article on quaternion algebra. The split complex algebra $\mathbb{D}$ is assumed from the article on split complex algebra, together with its idempotents $e_+ = \tfrac{1}{2}(1 + j)$ and $e_- = \tfrac{1}{2}(1 - j)$ and the isomorphism $\mathbb{D} \cong \mathbb{R} \oplus \mathbb{R}$.

Throughout this article, the quaternion basis is written $e_0 = 1, e_1, e_2, e_3$, and the split complex unit is written $j$, with $j^2 = +1$. The unit $j$ commutes with the quaternion units: $j e_k = e_k j$ for $k = 0, 1, 2, 3$.

## The Split Biquaternions

### Definition

The **split biquaternion algebra** is the tensor product

$$
\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H},
$$

where $\mathbb{D}$ is the split complex algebra and $\mathbb{H}$ is the quaternion algebra.

As a real vector space, $\mathbb{H}_{\mathbb{D}}$ has dimension $8$. As a split complex vector space, it has dimension $4$. A general split biquaternion is written in developed form as

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3, \qquad Q_\mu \in \mathbb{D},
$$

or, more compactly, as

$$
\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu, \qquad Q_\mu \in \mathbb{D}.
$$

We write

$$
\tilde{Q} = Q_0 e_0 + \mathbf{Q}, \qquad \mathbf{Q} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3,
$$

where $Q_0$ is the **split scalar part** and $\mathbf{Q}$ is the **split vector part**. The tilde signals that $\tilde{Q}$ is an element of the algebra $\mathbb{H}_{\mathbb{D}}$, not a quaternion.

Each split complex coefficient is written in terms of its real and split parts:

$$
Q_\mu = q_\mu + j q'_\mu, \qquad q_\mu, q'_\mu \in \mathbb{R}.
$$

The split complex unit $j$ satisfies $j^2 = +1$ and commutes with all quaternion units: $j e_k = e_k j$. It is the only extra unit in the algebra; the quaternion units $e_k$ satisfy $e_k^2 = -e_0$.

### Basic Properties

**Non-commutative.** Split biquaternion multiplication is not commutative: $e_1 e_2 = e_3$ but $e_2 e_1 = -e_3$.

**Associative.** Split biquaternion multiplication is associative: $(\tilde{P} \tilde{Q}) \tilde{R} = \tilde{P} (\tilde{Q} \tilde{R})$.

**Not a division algebra.** The split biquaternion algebra has zero divisors. This is the fundamental difference from the quaternion algebra, and it is the source of everything that distinguishes the two theories. The zero divisors are studied in the article on split biquaternion zero divisors.

**Not simple.** The split biquaternion algebra is not simple: it has nontrivial two-sided ideals, and it is isomorphic to the direct sum of two copies of the quaternion algebra.

**Semisimple.** The split biquaternion algebra is semisimple: it is isomorphic to a direct sum of simple algebras. The isomorphism is established below.

### The Algebra Structure

The split biquaternion algebra is semisimple and isomorphic to the direct sum of two copies of the quaternion algebra:

$$
\mathbb{H}_{\mathbb{D}} \cong \mathbb{H} \oplus \mathbb{H}.
$$

The isomorphism is given by the **idempotent decomposition**, which is the most important structural fact about the algebra.

Define the idempotents

$$
e_+ = \tfrac{1}{2}(1 + j), \qquad e_- = \tfrac{1}{2}(1 - j).
$$

They satisfy

$$
e_+^2 = e_+, \qquad e_-^2 = e_-, \qquad e_+ e_- = e_- e_+ = 0, \qquad e_+ + e_- = 1.
$$

Every split biquaternion is written uniquely in the idempotent basis as

$$
\tilde{Q} = \tilde{Q}_+ e_+ + \tilde{Q}_- e_-,
$$

where $\tilde{Q}_\pm \in \mathbb{H}$ are ordinary quaternions, given by

$$
\tilde{Q}_+ = \tilde{Q} e_+ = Q_0' + Q_1' e_1 + Q_2' e_2 + Q_3' e_3,
$$

$$
\tilde{Q}_- = \tilde{Q} e_- = Q_0'' + Q_1'' e_1 + Q_2'' e_2 + Q_3'' e_3,
$$

with real coefficients $Q_\mu', Q_\mu'' \in \mathbb{R}$.

The map

$$
\varphi : \mathbb{H}_{\mathbb{D}} \to \mathbb{H} \oplus \mathbb{H}, \qquad \varphi(\tilde{Q}) = (\tilde{Q}_+, \tilde{Q}_-),
$$

is an algebra isomorphism, where the multiplication on $\mathbb{H} \oplus \mathbb{H}$ is componentwise. This is the **idempotent decomposition** of the split biquaternion algebra.

The isomorphism is the reason the algebra is semisimple. It is not simple, because the two summands $\mathbb{H} e_+$ and $\mathbb{H} e_-$ are nontrivial two-sided ideals.

### Multiplication

The product of two split biquaternions is defined by extending the quaternion product split-complex-linearly. In developed form,

$$
\tilde{Q} \circ \tilde{R} = \sum_{\mu=0}^{3} \sum_{\nu=0}^{3} Q_\mu R_\nu \, e_\mu e_\nu,
$$

where the products $e_\mu e_\nu$ are those of the quaternion algebra, extended split-complex-linearly. In scalar-vector notation, this becomes

$$
\tilde{Q} \circ \tilde{R} = Q_0 R_0 - (\mathbf{Q}, \mathbf{R}) + Q_0 \mathbf{R} + R_0 \mathbf{Q} + [\mathbf{Q}, \mathbf{R}],
$$

where

$$
(\mathbf{Q}, \mathbf{R}) = \sum_{k=1}^{3} Q_k R_k, \qquad [\mathbf{Q}, \mathbf{R}] = \sum_{j,k,l=1}^{3} \epsilon_{jkl} Q_j R_k e_l.
$$

This formula has the same structure as the quaternion product: scalar part, vector part, dot product, cross product. The only difference is that the coefficients are now split complex.

### Conjugations

There are **four** natural conjugations on $\mathbb{H}_{\mathbb{D}}$, obtained by composing the quaternion conjugation $\bar{\cdot}$ and the split complex conjugation ${}^*$:

**Quaternion conjugation** $\bar{\tilde{Q}}$:

$$
\bar{\tilde{Q}} = Q_0 e_0 - Q_1 e_1 - Q_2 e_2 - Q_3 e_3.
$$

**Split complex conjugation** $\tilde{Q}^*$:

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

Each conjugation is an involution: applying it twice returns the original split biquaternion. Each has a fixed-point set, which is a real vector subspace of $\mathbb{H}_{\mathbb{D}}$. The four subspaces are described in the following sections.

### The Group of Conjugations

The two conjugations $\bar{\cdot}$ and ${}^*$ commute and generate the group $\{\mathrm{id}, \bar{\cdot}, {}^*, {}^\dagger\} \cong \mathbb{Z}/2 \times \mathbb{Z}/2$; the anti-Hermitian conjugation $\flat = -\dagger$ is an involution outside this group:

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

Each of the four conjugations has a fixed-point set, i.e., a set of split biquaternions left invariant by the conjugation. Each fixed-point set is a real vector subspace of $\mathbb{H}_{\mathbb{D}}$. The four subspaces are described below.

### The Split Complex Subspace

The fixed points of **quaternion conjugation** are the split biquaternions satisfying $\bar{\tilde{Q}} = \tilde{Q}$. In developed form,

$$
Q_0 e_0 - Q_1 e_1 - Q_2 e_2 - Q_3 e_3 = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3.
$$

Comparing the coefficients of $e_0, e_1, e_2, e_3$:

- Coefficient of $e_0$: $Q_0 = Q_0$, always satisfied.
- Coefficient of $e_1$: $-Q_1 = Q_1$, so $Q_1 = 0$.
- Coefficient of $e_2$: $-Q_2 = Q_2$, so $Q_2 = 0$.
- Coefficient of $e_3$: $-Q_3 = Q_3$, so $Q_3 = 0$.

The fixed points are split biquaternions with vanishing vector part:

$$
\tilde{Q} = Q_0 e_0, \qquad Q_0 \in \mathbb{D}.
$$

This is the **split complex subspace** $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$, a copy of the split complex number line embedded in $\mathbb{H}_{\mathbb{D}}$ as the scalar part. It is a real vector space of dimension 2. It is a subalgebra of $\mathbb{H}_{\mathbb{D}}$ (isomorphic to $\mathbb{D}$), it is commutative, and it coincides with the center of $\mathbb{H}_{\mathbb{D}}$.

### The Quaternion Subspace

The fixed points of **split complex conjugation** are the split biquaternions satisfying $\tilde{Q}^* = \tilde{Q}$. In developed form,

$$
Q_0^* e_0 + Q_1^* e_1 + Q_2^* e_2 + Q_3^* e_3 = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3.
$$

Comparing the coefficients:

- $Q_0^* = Q_0$, so $Q_0$ is real.
- $Q_1^* = Q_1$, so $Q_1$ is real.
- $Q_2^* = Q_2$, so $Q_2$ is real.
- $Q_3^* = Q_3$, so $Q_3$ is real.

The fixed points are split biquaternions with real coefficients:

$$
\tilde{Q} = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3, \qquad q_\mu \in \mathbb{R}.
$$

This is the **quaternion subspace** $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$, a copy of the real quaternion algebra embedded in $\mathbb{H}_{\mathbb{D}}$. It is a real vector space of dimension 4. It is a subalgebra of $\mathbb{H}_{\mathbb{D}}$, isomorphic to $\mathbb{H}$.

### The Hermitian Subspace

The fixed points of **Hermitian conjugation** are the split biquaternions satisfying $\tilde{Q}^\dagger = \tilde{Q}$. In developed form,

$$
Q_0^* e_0 - Q_1^* e_1 - Q_2^* e_2 - Q_3^* e_3 = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3.
$$

Comparing the coefficients:

- $Q_0^* = Q_0$, so $Q_0$ is real.
- $-Q_1^* = Q_1$, so $Q_1^* = -Q_1$, which means $Q_1$ is purely split-imaginary, i.e., $Q_1 = j r_1$ with $r_1 \in \mathbb{R}$.
- Similarly, $Q_2$ and $Q_3$ are purely split-imaginary.

The fixed points are split biquaternions of the form

$$
\tilde{Q} = q_0 e_0 + j q'_1 e_1 + j q'_2 e_2 + j q'_3 e_3, \qquad q_0, q'_1, q'_2, q'_3 \in \mathbb{R}.
$$

This is the **Hermitian subspace** $\mathbb{M}_+$, a real vector space of dimension 4. It consists of split biquaternions with real scalar part and purely split-imaginary vector part. It is not a subalgebra of $\mathbb{H}_{\mathbb{D}}$.

### The Anti-Hermitian Subspace

The fixed points of **anti-Hermitian conjugation** are the split biquaternions satisfying $\tilde{Q}^\flat = \tilde{Q}$, or equivalently $\tilde{Q} = -\tilde{Q}^\dagger$. In developed form,

$$
-Q_0^* e_0 + Q_1^* e_1 + Q_2^* e_2 + Q_3^* e_3 = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3.
$$

Comparing the coefficients:

- $-Q_0^* = Q_0$, so $Q_0^* = -Q_0$, which means $Q_0$ is purely split-imaginary, i.e., $Q_0 = j r_0$ with $r_0 \in \mathbb{R}$.
- $Q_1^* = Q_1$, so $Q_1$ is real.
- Similarly, $Q_2$ and $Q_3$ are real.

The fixed points are split biquaternions of the form

$$
\tilde{Q} = j r_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3, \qquad r_0, q_1, q_2, q_3 \in \mathbb{R}.
$$

This is the **anti-Hermitian subspace** $\mathbb{M}_-$, a real vector space of dimension 4. It consists of split biquaternions with purely split-imaginary scalar part and real vector part. It is not a subalgebra of $\mathbb{H}_{\mathbb{D}}$.

## Quaternion Decomposition

The split complex subspace $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ and the quaternion subspace $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ are not the two eigenspaces of a single involution; they are different fixed-point sets. However, there is a natural decomposition of $\mathbb{H}_{\mathbb{D}}$ associated with the split complex conjugation ${}^*$.

Every split biquaternion can be written uniquely as

$$
\tilde{Q} = \tilde{Q}_r + j \tilde{Q}_i,
$$

where $\tilde{Q}_r$ and $\tilde{Q}_i$ are **ordinary quaternions** (elements of $\mathbb{H}$ embedded in $\mathbb{H}_{\mathbb{D}}$), with real coefficients. The two components are

$$
\tilde{Q}_r = \frac{1}{2}(\tilde{Q} + \tilde{Q}^*), \qquad \tilde{Q}_i = \frac{1}{2j}(\tilde{Q} - \tilde{Q}^*).
$$

Indeed, $\tilde{Q}_r$ is fixed by split complex conjugation and so is $\tilde{Q}_i$ (compute $\tilde{Q}_i^* = \tilde{Q}_i$), so both lie in the quaternion subspace $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$; equivalently, $(j\tilde{Q}_i)^* = -j\tilde{Q}_i$ exhibits $j\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ as the $-1$ eigenspace of ${}^*$.

This gives the direct sum decomposition

$$
\mathbb{H}_{\mathbb{D}} = \mathbb{H}_{\mathbb{H}_{\mathbb{D}}} \oplus j \mathbb{H}_{\mathbb{H}_{\mathbb{D}}},
$$

where $j\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ is the set of split biquaternions of the form $j \tilde{Q}$ with $\tilde{Q} \in \mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$. Both are real vector spaces of dimension 4, and their direct sum is the full algebra $\mathbb{H}_{\mathbb{D}}$ of real dimension 8.

This is the **quaternion decomposition** of a split biquaternion. It expresses $\tilde{Q}$ as a quaternion plus the split complex unit times another quaternion.

## Idempotent Decomposition

The idempotent decomposition is the second natural decomposition of $\mathbb{H}_{\mathbb{D}}$, and it is the key to the structure of the algebra.

Every split biquaternion is written uniquely as

$$
\tilde{Q} = \tilde{Q}_+ e_+ + \tilde{Q}_- e_-,
$$

where $e_\pm = \tfrac{1}{2}(1 \pm j)$ are the idempotents, and $\tilde{Q}_\pm = \tilde{Q} e_\pm \in \mathbb{H}$.

This gives the direct sum decomposition

$$
\mathbb{H}_{\mathbb{D}} = \mathbb{H} e_+ \oplus \mathbb{H} e_-,
$$

where $\mathbb{H} e_+$ and $\mathbb{H} e_-$ are the two ideals of $\mathbb{H}_{\mathbb{D}}$, each isomorphic to $\mathbb{H}$. Both are real vector spaces of dimension 4, and their direct sum is the full algebra $\mathbb{H}_{\mathbb{D}}$ of real dimension 8.

The isomorphism

$$
\varphi : \mathbb{H}_{\mathbb{D}} \to \mathbb{H} \oplus \mathbb{H}, \qquad \varphi(\tilde{Q}) = (\tilde{Q}_+, \tilde{Q}_-)
$$

is an algebra isomorphism, and it is the reason the algebra is semisimple.

## Hermitian Decomposition

The Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$ are the two eigenspaces of the Hermitian conjugation $\dagger$. Every split biquaternion decomposes uniquely as the sum of a Hermitian part and an anti-Hermitian part:

$$
\tilde{Q} = \tilde{Q}_+ + \tilde{Q}_-, \qquad \tilde{Q}_+ \in \mathbb{M}_+, \quad \tilde{Q}_- \in \mathbb{M}_-.
$$

The two components are obtained from the Hermitian conjugation:

$$
\tilde{Q}_+ = \frac{1}{2}(\tilde{Q} + \tilde{Q}^\dagger), \qquad \tilde{Q}_- = \frac{1}{2}(\tilde{Q} - \tilde{Q}^\dagger).
$$

This gives the direct sum decomposition

$$
\mathbb{H}_{\mathbb{D}} = \mathbb{M}_+ \oplus \mathbb{M}_-,
$$

where $\mathbb{M}_+$ is the Hermitian subspace and $\mathbb{M}_-$ is the anti-Hermitian subspace. Both are real vector spaces of dimension 4.

## Relation Between the Two Decompositions

The quaternion decomposition $\mathbb{H}_{\mathbb{D}} = \mathbb{H}_{\mathbb{H}_{\mathbb{D}}} \oplus j \mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ and the Hermitian decomposition $\mathbb{H}_{\mathbb{D}} = \mathbb{M}_+ \oplus \mathbb{M}_-$ are two different decompositions of the same eight-dimensional real vector space. They are associated with two different involutions: the quaternion decomposition is associated with the split complex conjugation ${}^*$, and the Hermitian decomposition is associated with the Hermitian conjugation $\dagger$.

The two decompositions are related by multiplication by the split complex unit $j$, which maps $\mathbb{M}_+$ to $\mathbb{M}_-$ and vice versa. The idempotent decomposition is a third decomposition, associated with the idempotents $e_\pm$, and it is the one that reveals the semisimple structure of the algebra.

## Quadratic Forms and Inner Product

### The Norm Form

The **norm form** of a split biquaternion $\tilde{Q}$ is

$$
N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}} = \sum_{\mu=0}^{3} Q_\mu^2,
$$

where $\bar{\tilde{Q}}$ is the quaternion conjugate. It is a split complex number in general:

$$
N(\tilde{Q}) = \sum_{\mu=0}^{3} (q_\mu^2 + q'^2_\mu) + 2j \sum_{\mu=0}^{3} q_\mu q'_\mu.
$$

Its real part is positive-definite, $\sum_\mu(q_\mu^2+q'^2_\mu)$, so $N(\tilde Q)=0$ forces $\tilde Q=0$: the norm form does **not** single out the zero divisors. Those are characterized instead by the vanishing of an idempotent component, $\tilde Q_+=0$ or $\tilde Q_-=0$, as the article on split biquaternion zero divisors shows.

The norm form is **multiplicative**:

$$
N(\tilde{Q} \circ \tilde{R}) = N(\tilde{Q}) \, N(\tilde{R}).
$$

### The Hermitian Form

The **Hermitian form** of a split biquaternion $\tilde{Q}$ is

$$
\tilde{Q} \tilde{Q}^\dagger,
$$

where $\tilde{Q}^\dagger$ is the Hermitian conjugate and $Q_\mu^* = q_\mu - j q'_\mu$ is the split complex conjugate. Its **scalar part** is $\sum_{\mu=0}^{3} Q_\mu Q_\mu^* = \sum_{\mu=0}^{3} (q_\mu^2 - q'^2_\mu)$, while its vector part need not vanish. That scalar part is a **real** form which is **not positive-definite**: it can be positive, negative, or zero. Its signature is $(4, 4)$ on the eight-dimensional real space $\mathbb{H}_{\mathbb{D}}$.

So the Hermitian form does not define a Euclidean norm on $\mathbb{H}_{\mathbb{D}}$. It is an indefinite quadratic form of signature $(4, 4)$.

### The Euclidean Norm

The **Euclidean norm** on $\mathbb{H}_{\mathbb{D}} \cong \mathbb{R}^8$ is defined separately by

$$
\|\tilde{Q}\|_E = \sqrt{\sum_{\mu=0}^{3} (q_\mu^2 + q'^2_\mu)}.
$$

It is a genuine norm on the real vector space $\mathbb{H}_{\mathbb{D}}$: positive-definite, subadditive, and homogeneous of degree one. It is **not** the square root of the Hermitian form, because the Hermitian form is indefinite. It is the ordinary Euclidean norm on the underlying real vector space.

### The Inner Product

The **inner product** of two split biquaternions $\tilde{P}$ and $\tilde{Q}$ is

$$
\langle \tilde{P}, \tilde{Q} \rangle = \sum_{\mu=0}^{3} P_\mu^* Q_\mu,
$$

which is a split complex number in general:

$$
\langle \tilde{P}, \tilde{Q} \rangle = \sum_{\mu=0}^{3} (p_\mu q_\mu - p'_\mu q'_\mu) + j \sum_{\mu=0}^{3} (p_\mu q'_\mu - p'_\mu q_\mu).
$$

The real part is the indefinite form of signature $(4, 4)$, and the split part is the cross-term. The inner product is linear in the second argument and split-antilinear in the first, and it is Hermitian in the sense that $\langle \tilde{P}, \tilde{Q} \rangle^* = \langle \tilde{Q}, \tilde{P} \rangle$.

### Relation Between the Three Forms

The three quadratic objects are related as follows:

- **Norm form:** $N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}} = \sum_\mu Q_\mu^2$. Split complex-valued, vanishes only at $\tilde{Q}=0$, multiplicative.
- **Hermitian form:** $\tilde{Q} \tilde{Q}^\dagger$, whose scalar part is $\sum_\mu (q_\mu^2 - q'^2_\mu)$. That scalar part is real, indefinite of signature $(4, 4)$, and vanishes on a quadric hypersurface of dimension $7$; the full product is not multiplicative.
- **Inner product:** $\langle \tilde{P}, \tilde{Q} \rangle = \sum_\mu P_\mu^* Q_\mu$. Split complex-valued in general, Hermitian, linear in the second argument.

The three are distinct, and each is useful in a different context. The norm form controls invertibility (through $\Delta$, its split complex invertibility). The zero divisors are not a norm-form condition; they are the vanishing of an idempotent component. The Hermitian form is indefinite and does not control the topological structure. The Euclidean norm, which is defined separately, provides the topological structure.

## The Lie Algebra Structure

The split biquaternion algebra carries a Lie bracket, defined by the commutator

$$
[\tilde{P}, \tilde{Q}] = \tilde{P} \tilde{Q} - \tilde{Q} \tilde{P}.
$$

The Lie algebra structure of $\mathbb{H}_{\mathbb{D}}$ is the direct sum of two copies of the Lie algebra of $\mathbb{H}$, because the algebra is isomorphic to $\mathbb{H} \oplus \mathbb{H}$. In particular, the pure split biquaternions (with respect to the quaternion conjugation) form a Lie subalgebra isomorphic to $\mathfrak{so}(3) \oplus \mathfrak{so}(3)$, which is the Lie algebra of the group $SO(3) \times SO(3)$.

## Summary

The split biquaternion algebra is the tensor product $\mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ of the split complex algebra and the quaternion algebra. It is an eight-dimensional real algebra, non-commutative and associative, with zero divisors. It is not a division algebra, and it is not simple, but it is semisimple.

The algebra is isomorphic to the direct sum $\mathbb{H} \oplus \mathbb{H}$ via the idempotent decomposition $\tilde{Q} = \tilde{Q}_+ e_+ + \tilde{Q}_- e_-$, where $e_\pm = \tfrac{1}{2}(1 \pm j)$ are the idempotents of the split complex algebra. This is the most important structural fact about the algebra.

There are four natural conjugations: quaternion conjugation, split complex conjugation, Hermitian conjugation, and anti-Hermitian conjugation. Each has a fixed-point set, which is a four-dimensional real subspace (or two-dimensional in the case of the split complex subspace). The four subspaces are the split complex subspace, the quaternion subspace, the Hermitian subspace, and the anti-Hermitian subspace.

There are three natural decompositions of the algebra: the quaternion decomposition $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}} \oplus j \mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$, the idempotent decomposition $\mathbb{H} e_+ \oplus \mathbb{H} e_-$, and the Hermitian decomposition $\mathbb{M}_+ \oplus \mathbb{M}_-$.

The norm form is split complex-valued and multiplicative. The scalar part of the Hermitian form is real and indefinite of signature $(4, 4)$. The Euclidean norm is defined separately and is positive-definite. The split biquaternion algebra is therefore not a normed algebra in the same sense as the quaternion algebra, where the norm form is positive-definite and multiplicative.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | Split complex algebra |
| $\mathbb{H}$ | Quaternion algebra |
| $\mathbb{H}_{\mathbb{D}}$ | Split biquaternion algebra, $\mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ |
| $e_0 = 1$ | Identity |
| $e_1, e_2, e_3$ | Quaternion units, $e_k^2 = -e_0$ |
| $j$ | Split complex unit, $j^2 = +1$, commutes with $e_k$ |
| $e_+ = \tfrac{1}{2}(1 + j)$ | Positive idempotent |
| $e_- = \tfrac{1}{2}(1 - j)$ | Negative idempotent |
| $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ | General split biquaternion |
| $Q_\mu = q_\mu + j q'_\mu$ | Split complex coefficient |
| $Q_0$ | Split scalar part |
| $\mathbf{Q}$ | Split vector part |
| $\bar{\tilde{Q}} = Q_0 e_0 - \mathbf{Q}$ | Quaternion conjugate |
| $\tilde{Q}^* = Q_0^* e_0 + \mathbf{Q}^*$ | Split complex conjugate |
| $\tilde{Q}^\dagger = Q_0^* e_0 - \mathbf{Q}^*$ | Hermitian conjugate |
| $\tilde{Q}^\flat = -\tilde{Q}^\dagger$ | Anti-Hermitian conjugate |
| $N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}}$ | Norm form |
| $\tilde{Q} \tilde{Q}^\dagger$, scalar part $\sum_\mu (q_\mu^2 - q'^2_\mu)$ | Hermitian form (indefinite) |
| $\|\tilde{Q}\|_E = \sqrt{\sum_\mu (q_\mu^2 + q'^2_\mu)}$ | Euclidean norm |
| $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ | Split complex subspace |
| $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ | Quaternion subspace |
| $\mathbb{M}_+$ | Hermitian subspace |
| $\mathbb{M}_-$ | Anti-Hermitian subspace |
| $\mathbb{H} e_+, \mathbb{H} e_-$ | Idempotent ideals |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original formulation of quaternions and their complexification.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the algebraic structure of the split biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the classification of real algebras.
- F. Brackx, R. Delanghe, and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the general Clifford analysis.

