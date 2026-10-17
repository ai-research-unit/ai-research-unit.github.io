
# __Split-Biquaternion Algebra__

## Introduction

This article introduces the split biquaternion algebra as an algebraic structure. The goal is to define the algebra precisely, establish its basic properties, and describe the distinguished real vector subspaces that arise from the natural conjugations.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. No examples are given. The quaternion algebra $\mathbb{H}$ is assumed from the article on quaternion algebra. The split complex algebra $\mathbb{D}$ is assumed from the article on split complex algebra, together with its idempotents $\tilde\Pi_1 = \tfrac{1}{2}(1 + j)$ and $\tilde\Pi_2 = \tfrac{1}{2}(1 - j)$ and the isomorphism $\mathbb{D} \cong \mathbb{R} \oplus \mathbb{R}$.

Throughout this article, the quaternion basis is written $e_t = 1, \vec e_x, \vec e_y, \vec e_z$, and the split complex unit is written $j$, with $j^2 = +1$. The unit $j$ commutes with the quaternion units: $j e_\mu = e_\mu j$ for $\mu = 0, 1, 2, 3$.

## The Split Biquaternions

### Definition

The **split biquaternion algebra** is the tensor product

$$
\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H},
$$

where $\mathbb{D}$ is the split complex algebra and $\mathbb{H}$ is the quaternion algebra. It is also met, in the form $\mathbb{H} \oplus \mathbb{H}$, as the algebra of the two quaternion halves.

As a real vector space, $\mathbb{H}_{\mathbb{D}}$ has dimension $8$. As a split complex vector space, it has dimension $4$. A general split biquaternion is written in developed form as

$$
\tilde{Q} = Q_t e_t + Q_x \vec e_x + Q_y \vec e_y + Q_z \vec e_z, \qquad Q_\mu \in \mathbb{D},
$$

or, more compactly, as

$$
\tilde{Q} = \sum_{\mu\in\{t,x,y,z\}} Q_\mu e_\mu, \qquad Q_\mu \in \mathbb{D}.
$$

We write

$$
\tilde{Q} = Q_t e_t + \vec Q, \qquad \vec Q = Q_x \vec e_x + Q_y \vec e_y + Q_z \vec e_z,
$$

where $Q_t$ is the **split scalar part** and $\vec Q$ is the **split vector part**. The tilde signals that $\tilde{Q}$ is an element of the algebra $\mathbb{H}_{\mathbb{D}}$, not a quaternion.

Each split complex coefficient is written in terms of its real and split parts:

$$
Q_\mu = q_\mu + j q'_\mu, \qquad q_\mu, q'_\mu \in \mathbb{R}.
$$

The split complex unit $j$ satisfies $j^2 = +1$ and commutes with all quaternion units: $j e_\mu = e_\mu j$. It is the only extra unit in the algebra; the quaternion units $\vec e_\mu$ satisfy $\vec e_\mu^2 = -e_t$.

### Basic Properties

**Non-commutative.** Split biquaternion multiplication is not commutative: $\vec e_x \vec e_y = \vec e_z$ but $\vec e_y \vec e_x = -\vec e_z$.

**Associative.** Split biquaternion multiplication is associative: $(\tilde{Q}_1 \tilde{Q}_2) \tilde{Q}_3 = \tilde{Q}_1 (\tilde{Q}_2 \tilde{Q}_3)$.

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
\tilde\Pi_1 = \tfrac{1}{2}(1 + j), \qquad \tilde\Pi_2 = \tfrac{1}{2}(1 - j).
$$

They satisfy

$$
\tilde\Pi_1^2 = \tilde\Pi_1, \qquad \tilde\Pi_2^2 = \tilde\Pi_2, \qquad \tilde\Pi_1 \tilde\Pi_2 = \tilde\Pi_2 \tilde\Pi_1 = 0, \qquad \tilde\Pi_1 + \tilde\Pi_2 = 1.
$$

Every split biquaternion is written uniquely in the idempotent basis as

$$
\tilde{Q} = \tilde{Q}_+ \tilde\Pi_1 + \tilde{Q}_- \tilde\Pi_2,
$$

where $\tilde{Q}_\pm \in \mathbb{H}$ are ordinary quaternions, given by

$$
\tilde{Q}_+ = \tilde{Q} \tilde\Pi_1 = Q_t' + Q_x' \vec e_x + Q_y' \vec e_y + Q_z' \vec e_z,
$$

$$
\tilde{Q}_- = \tilde{Q} \tilde\Pi_2 = Q_t'' + Q_x'' \vec e_x + Q_y'' \vec e_y + Q_z'' \vec e_z,
$$

with real coefficients $Q_\mu', Q_\mu'' \in \mathbb{R}$.

The map

$$
\varphi : \mathbb{H}_{\mathbb{D}} \to \mathbb{H} \oplus \mathbb{H}, \qquad \varphi(\tilde{Q}) = (\tilde{Q}_+, \tilde{Q}_-),
$$

is an algebra isomorphism, where the multiplication on $\mathbb{H} \oplus \mathbb{H}$ is componentwise. This is the **idempotent decomposition** of the split biquaternion algebra.

The isomorphism is the reason the algebra is semisimple. It is not simple, because the two summands $\mathbb{H} \tilde\Pi_1$ and $\mathbb{H} \tilde\Pi_2$ are nontrivial two-sided ideals.

### The Clifford Structure

The algebra is also a Clifford algebra, of three generators of square $-1$ — the sign opposite to the generators of the biquaternion algebra's Clifford reading, where the three generators square to $+1$.

**Proposition (the generators).** The three elements

$$
E_1 = j\vec e_x, \qquad E_2 = j\vec e_y, \qquad E_3 = j\vec e_z
$$

satisfy

$$
E_\mu^2 = -1, \qquad E_\mu E_\nu = -E_\nu E_\mu \quad (\mu \neq \nu),
$$

so that $\{E_\mu, E_\nu\} = -2\delta_{\mu\nu}$. They therefore generate a copy of the real Clifford algebra $\mathrm{Cl}(0,3)$.

*Proof.* Because $j$ is central with $j^2=+1$ and the quaternion units satisfy $\vec e_\mu^2=-1$ and $\vec e_\mu \vec e_\nu=-\vec e_\nu \vec e_\mu$ for $\mu\neq \nu$,
$$
E_\mu^2 = j^2\vec e_\mu^2 = -1, \qquad E_\mu E_\nu = j^2\vec e_\mu \vec e_\nu = -\vec e_\nu \vec e_\mu = -E_\nu E_\mu .
$$

**Proposition (identification and volume element).** The eight monomials in $E_1,E_2,E_3$ are linearly independent and span $\mathbb{H}_{\mathbb{D}}$, so

$$
\mathbb{H}_{\mathbb{D}} \cong \mathrm{Cl}(0,3) \cong \mathrm{Cl}_{0,3},
$$

the Clifford algebra of a three-dimensional negative definite space. The volume element is

$$
E_1E_2E_3 = j^3(\vec e_x \vec e_y)\vec e_z = j\,\vec e_z \vec e_z = -j,
$$

which is central with square $+1$; the Clifford idempotents $\tfrac12(1 \pm E_1E_2E_3) = \tfrac12(1 \mp j)$ are the idempotents $\tilde\Pi_{1,2}$ of the idempotent decomposition, with the index reversed.

*Proof.* The monomials are the eight elements $\tilde\Pi_{1,2}$ times the quaternion basis and are independent; the product is immediate from $j^2=1$, $\vec e_x \vec e_y=\vec e_z$ and $\vec e_z^2=-1$.

**Proposition (the complexification).** The complexification $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}_{\mathbb{D}}$ is the complex Clifford algebra

$$
\mathrm{Cl}(3) \cong \mathrm{Cl}_3(\mathbb{C}) \cong M_2(\mathbb{C}) \oplus M_2(\mathbb{C}) \cong \mathbb{B} \oplus \mathbb{B},
$$

whose two simple summands are the complexified quaternion halves; its volume element is the element $-j$, central and an involution, and it is the algebra studied in *Complex Split Biquaternions and the Clifford Algebra Cl(3)*.

*Proof.* Complexification extends scalars, so the relations of the $E_\mu$ are unchanged and the complexified monomials are a basis; the classification of the odd complex Clifford algebras gives $\mathrm{Cl}_3(\mathbb{C})\cong M_2(\mathbb{C})\oplus M_2(\mathbb{C})$, and the complexified idempotent decomposition gives the two summands $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong\mathbb{B}$.

The Clifford reading is the reason the split biquaternion algebra is the natural lower rung of a doubling: its volume element is a central involution rather than a complex structure, so its complexification splits into two copies of the biquaternion algebra where the biquaternion algebra itself is simple.

### Multiplication

The product of two split biquaternions is defined by extending the quaternion product split-complex-linearly. In developed form,

$$
\tilde{Q}_1 \bullet \tilde{Q}_2 = \sum_{\mu\in\{t,x,y,z\}} \sum_{\nu\in\{t,x,y,z\}} Q_{1\mu} Q_{2\nu} \, e_\mu e_\nu,
$$

where the products $e_\mu e_\nu$ are those of the quaternion algebra, extended split-complex-linearly. In scalar-vector notation, this becomes

$$
\tilde{Q}_1 \bullet \tilde{Q}_2 = Q_{1t} Q_{2t} - (\vec Q_1, \vec Q_2) + Q_{1t} \vec Q_2 + Q_{2t} \vec Q_1 + [\vec Q_1, \vec Q_2],
$$

where

$$
(\vec Q_1, \vec Q_2) = \sum_{k=1}^{3} Q_{1k} Q_{2k}, \qquad [\vec Q_1, \vec Q_2] = \sum_{\mu,\nu,\lambda=1}^{3} \epsilon_{\mu\nu\lambda} Q_{1\mu} Q_{2\nu} \vec e_\lambda.
$$

This formula has the same structure as the quaternion product: scalar part, vector part, dot product, cross product. The only difference is that the coefficients are now split complex.

### Conjugations

There are **four** natural conjugations on $\mathbb{H}_{\mathbb{D}}$, obtained by composing the quaternion conjugation ${}^{\natural}$ and the split complex conjugation $\bar{\cdot}$:

**Quaternion conjugation** $\tilde{Q}^{\natural}$:

$$
\tilde{Q}^{\natural} = Q_t e_t - Q_x \vec e_x - Q_y \vec e_y - Q_z \vec e_z.
$$

**Split complex conjugation** $\bar{\tilde{Q}}$:

$$
\bar{\tilde{Q}} = \bar{Q_t} e_t + \bar{Q_x} \vec e_x + \bar{Q_y} \vec e_y + \bar{Q_z} \vec e_z.
$$

**Hermitian conjugation** $\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}}$:

$$
\tilde{Q}^{*} = \bar{Q_t} e_t - \bar{Q_x} \vec e_x - \bar{Q_y} \vec e_y - \bar{Q_z} \vec e_z.
$$

**Anti-Hermitian conjugation** $\tilde{Q}^\flat = -\tilde{Q}^{*}$:

$$
\tilde{Q}^\flat = -\bar{Q_t} e_t + \bar{Q_x} \vec e_x + \bar{Q_y} \vec e_y + \bar{Q_z} \vec e_z.
$$

Each conjugation is an involution: applying it twice returns the original split biquaternion. Each has a fixed-point set, which is a real vector subspace of $\mathbb{H}_{\mathbb{D}}$. The four subspaces are described in the following sections.

### The Group of Conjugations

The two conjugations ${}^{\natural}$ and $\bar{\cdot}$ commute, and the Hermitian conjugation is their composite; the three, together with the identity, form the group $\{\mathrm{id}, {}^{\natural}, \bar{\cdot}, {}^{*}\} \cong \mathbb{Z}/2 \times \mathbb{Z}/2$:

$$
\overline{\tilde{Q}^{\natural}} = \bar{\tilde{Q}}^{\natural} = \tilde{Q}^{*}.
$$

The anti-Hermitian conjugation $\flat = -{}^{*}$ is an involution outside this group:

$$
\tilde{Q}^{\flat} = -\tilde{Q}^{*}.
$$

So the four conjugations are not independent: they are determined by the two commuting involutions ${}^{\natural}$ and $\bar{\cdot}$, together with the sign choice in the definition of $\flat$.

## The Four Fixed-Point Subspaces

Each of the four conjugations has a fixed-point set, i.e., a set of split biquaternions left invariant by the conjugation. Each fixed-point set is a real vector subspace of $\mathbb{H}_{\mathbb{D}}$. The four subspaces are described below.

### The Split Complex Subspace

The fixed points of **quaternion conjugation** are the split biquaternions satisfying $\tilde{Q}^{\natural} = \tilde{Q}$. In developed form,

$$
Q_t e_t - Q_x \vec e_x - Q_y \vec e_y - Q_z \vec e_z = Q_t e_t + Q_x \vec e_x + Q_y \vec e_y + Q_z \vec e_z.
$$

Comparing the coefficients of $e_t, \vec e_x, \vec e_y, \vec e_z$:

- Coefficient of $e_t$: $Q_t = Q_t$, always satisfied.
- Coefficient of $\vec e_x$: $-Q_x = Q_x$, so $Q_x = 0$.
- Coefficient of $\vec e_y$: $-Q_y = Q_y$, so $Q_y = 0$.
- Coefficient of $\vec e_z$: $-Q_z = Q_z$, so $Q_z = 0$.

The fixed points are split biquaternions with vanishing vector part:

$$
\tilde{Q} = Q_t e_t, \qquad Q_t \in \mathbb{D}.
$$

This is the **split complex subspace** $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$, a copy of the split complex number line embedded in $\mathbb{H}_{\mathbb{D}}$ as the scalar part. It is a real vector space of dimension 2. It is a subalgebra of $\mathbb{H}_{\mathbb{D}}$ (isomorphic to $\mathbb{D}$), it is commutative, and it coincides with the centre of $\mathbb{H}_{\mathbb{D}}$.

### The Quaternion Subspace

The fixed points of **split complex conjugation** are the split biquaternions satisfying $\bar{\tilde{Q}} = \tilde{Q}$. In developed form,

$$
\bar{Q_t} e_t + \bar{Q_x} \vec e_x + \bar{Q_y} \vec e_y + \bar{Q_z} \vec e_z = Q_t e_t + Q_x \vec e_x + Q_y \vec e_y + Q_z \vec e_z.
$$

Comparing the coefficients:

- $\bar{Q_t} = Q_t$, so $Q_t$ is real.
- $\bar{Q_x} = Q_x$, so $Q_x$ is real.
- $\bar{Q_y} = Q_y$, so $Q_y$ is real.
- $\bar{Q_z} = Q_z$, so $Q_z$ is real.

The fixed points are split biquaternions with real coefficients:

$$
\tilde{Q} = q_t e_t + q_x \vec e_x + q_y \vec e_y + q_z \vec e_z, \qquad q_\mu \in \mathbb{R}.
$$

This is the **quaternion subspace** $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$, a copy of the real quaternion algebra embedded in $\mathbb{H}_{\mathbb{D}}$. It is a real vector space of dimension 4. It is a subalgebra of $\mathbb{H}_{\mathbb{D}}$, isomorphic to $\mathbb{H}$.

### The Hermitian Subspace

The fixed points of **Hermitian conjugation** are the split biquaternions satisfying $\tilde{Q}^{*} = \tilde{Q}$. In developed form,

$$
\bar{Q_t} e_t - \bar{Q_x} \vec e_x - \bar{Q_y} \vec e_y - \bar{Q_z} \vec e_z = Q_t e_t + Q_x \vec e_x + Q_y \vec e_y + Q_z \vec e_z.
$$

Comparing the coefficients:

- $\bar{Q_t} = Q_t$, so $Q_t$ is real.
- $-\bar{Q_x} = Q_x$, so $\bar{Q_x} = -Q_x$, which means $Q_x$ is purely split-imaginary, i.e., $Q_x = j r_1$ with $r_1 \in \mathbb{R}$.
- Similarly, $Q_y$ and $Q_z$ are purely split-imaginary.

The fixed points are split biquaternions of the form

$$
\tilde{Q} = q_t e_t + j q'_x \vec e_x + j q'_y \vec e_y + j q'_z \vec e_z, \qquad q_t, q'_x, q'_y, q'_z \in \mathbb{R}.
$$

This is the **Hermitian subspace** $\mathbb{M}_+$, a real vector space of dimension 4. It consists of split biquaternions with real scalar part and purely split-imaginary vector part. It is not a subalgebra of $\mathbb{H}_{\mathbb{D}}$.

### The Anti-Hermitian Subspace

The fixed points of **anti-Hermitian conjugation** are the split biquaternions satisfying $\tilde{Q}^\flat = \tilde{Q}$, or equivalently $\tilde{Q} = -\tilde{Q}^{*}$. In developed form,

$$
-\bar{Q_t} e_t + \bar{Q_x} \vec e_x + \bar{Q_y} \vec e_y + \bar{Q_z} \vec e_z = Q_t e_t + Q_x \vec e_x + Q_y \vec e_y + Q_z \vec e_z.
$$

Comparing the coefficients:

- $-\bar{Q_t} = Q_t$, so $\bar{Q_t} = -Q_t$, which means $Q_t$ is purely split-imaginary, i.e., $Q_t = j r_0$ with $r_0 \in \mathbb{R}$.
- $\bar{Q_x} = Q_x$, so $Q_x$ is real.
- Similarly, $Q_y$ and $Q_z$ are real.

The fixed points are split biquaternions of the form

$$
\tilde{Q} = j r_0 e_t + q_x \vec e_x + q_y \vec e_y + q_z \vec e_z, \qquad r_0, q_x, q_y, q_z \in \mathbb{R}.
$$

This is the **anti-Hermitian subspace** $\mathbb{M}_-$, a real vector space of dimension 4. It consists of split biquaternions with purely split-imaginary scalar part and real vector part. It is not a subalgebra of $\mathbb{H}_{\mathbb{D}}$.

## Quaternion Decomposition

The split complex subspace $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ and the quaternion subspace $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ are not the two eigenspaces of a single involution; they are different fixed-point sets. However, there is a natural decomposition of $\mathbb{H}_{\mathbb{D}}$ associated with the split complex conjugation $\bar{\cdot}$.

Every split biquaternion can be written uniquely as

$$
\tilde{Q} = \tilde q + j \tilde q',
$$

where $\tilde q$ and $\tilde q'$ are **ordinary quaternions** (elements of $\mathbb{H}$ embedded in $\mathbb{H}_{\mathbb{D}}$), with real coefficients. The two components are

$$
\tilde q = \frac{1}{2}(\tilde{Q} + \bar{\tilde{Q}}), \qquad \tilde q' = \frac{1}{2j}(\tilde{Q} - \bar{\tilde{Q}}).
$$

Indeed, $\tilde q$ is fixed by split complex conjugation and so is $\tilde q'$ (compute $\bar{\tilde q'} = \tilde q'$), so both lie in the quaternion subspace $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$; equivalently, $(j\tilde q')^* = -j\tilde q'$ exhibits $j\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ as the $-1$ eigenspace of $\bar{\cdot}$.

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
\tilde{Q} = \tilde{Q}_+ \tilde\Pi_1 + \tilde{Q}_- \tilde\Pi_2,
$$

where $\tilde\Pi_{1,2} = \tfrac{1}{2}(1 \pm j)$ are the idempotents, and $\tilde{Q}_\pm = \tilde{Q} \tilde\Pi_{1,2} \in \mathbb{H}$.

This gives the direct sum decomposition

$$
\mathbb{H}_{\mathbb{D}} = \mathbb{H} \tilde\Pi_1 \oplus \mathbb{H} \tilde\Pi_2,
$$

where $\mathbb{H} \tilde\Pi_1$ and $\mathbb{H} \tilde\Pi_2$ are the two ideals of $\mathbb{H}_{\mathbb{D}}$, each isomorphic to $\mathbb{H}$. Both are real vector spaces of dimension 4, and their direct sum is the full algebra $\mathbb{H}_{\mathbb{D}}$ of real dimension 8.

The isomorphism

$$
\varphi : \mathbb{H}_{\mathbb{D}} \to \mathbb{H} \oplus \mathbb{H}, \qquad \varphi(\tilde{Q}) = (\tilde{Q}_+, \tilde{Q}_-)
$$

is an algebra isomorphism, and it is the reason the algebra is semisimple.

## Hermitian Decomposition

The Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$ are the two eigenspaces of the Hermitian conjugation ${}^{*}$. Every split biquaternion decomposes uniquely as the sum of a Hermitian part and an anti-Hermitian part:

$$
\tilde{Q} = \tilde{Q}_{\mathrm{H}} + \tilde{Q}_{\mathrm{A}}, \qquad \tilde{Q}_{\mathrm{H}} \in \mathbb{M}_+, \quad \tilde{Q}_{\mathrm{A}} \in \mathbb{M}_-.
$$

The two components are obtained from the Hermitian conjugation:

$$
\tilde{Q}_{\mathrm{H}} = \frac{1}{2}(\tilde{Q} + \tilde{Q}^{*}), \qquad \tilde{Q}_{\mathrm{A}} = \frac{1}{2}(\tilde{Q} - \tilde{Q}^{*}).
$$

This gives the direct sum decomposition

$$
\mathbb{H}_{\mathbb{D}} = \mathbb{M}_+ \oplus \mathbb{M}_-,
$$

where $\mathbb{M}_+$ is the Hermitian subspace and $\mathbb{M}_-$ is the anti-Hermitian subspace. Both are real vector spaces of dimension 4.

## Relation Between the Three Decompositions

The quaternion decomposition $\mathbb{H}_{\mathbb{D}} = \mathbb{H}_{\mathbb{H}_{\mathbb{D}}} \oplus j \mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ and the Hermitian decomposition $\mathbb{H}_{\mathbb{D}} = \mathbb{M}_+ \oplus \mathbb{M}_-$ are two different decompositions of the same eight-dimensional real vector space. They are associated with two different involutions: the quaternion decomposition is associated with the split complex conjugation $\bar{\cdot}$, and the Hermitian decomposition is associated with the Hermitian conjugation ${}^{*}$.

The two decompositions are related by multiplication by the split complex unit $j$, which maps $\mathbb{M}_+$ to $\mathbb{M}_-$ and vice versa. The idempotent decomposition is a third decomposition, associated with the idempotents $\tilde\Pi_{1,2}$, and it is the one that reveals the semisimple structure of the algebra.

## The Lie Algebra Structure

The split biquaternion algebra carries a Lie bracket, defined by the commutator

$$
[\tilde{Q}_1, \tilde{Q}_2] = \tilde{Q}_1 \tilde{Q}_2 - \tilde{Q}_2 \tilde{Q}_1.
$$

The Lie algebra structure of $\mathbb{H}_{\mathbb{D}}$ is the direct sum of two copies of the Lie algebra of $\mathbb{H}$, because the algebra is isomorphic to $\mathbb{H} \oplus \mathbb{H}$. In particular, the pure split biquaternions (with respect to the quaternion conjugation) form a Lie subalgebra isomorphic to $\mathrm{SO}(3) \oplus \mathrm{SO}(3)$. The group this Lie algebra integrates to, and the motions it defines, are treated in Geometry, where the form is available.

## Summary

The split biquaternion algebra is the tensor product $\mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ of the split complex algebra and the quaternion algebra. It is an eight-dimensional real algebra, non-commutative and associative, with zero divisors. It is not a division algebra, and it is not simple, but it is semisimple.

The algebra is isomorphic to the direct sum $\mathbb{H} \oplus \mathbb{H}$ via the idempotent decomposition $\tilde{Q} = \tilde{Q}_+ \tilde\Pi_1 + \tilde{Q}_- \tilde\Pi_2$, where $\tilde\Pi_{1,2} = \tfrac{1}{2}(1 \pm j)$ are the idempotents of the split complex algebra. This is the most important structural fact about the algebra.

There are four natural conjugations: quaternion conjugation, split complex conjugation, Hermitian conjugation, and anti-Hermitian conjugation. Each has a fixed-point set, which is a four-dimensional real subspace (or two-dimensional in the case of the split complex subspace). The four subspaces are the split complex subspace, the quaternion subspace, the Hermitian subspace, and the anti-Hermitian subspace.

There are three natural decompositions of the algebra: the quaternion decomposition $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}} \oplus j \mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$, the idempotent decomposition $\mathbb{H} \tilde\Pi_1 \oplus \mathbb{H} \tilde\Pi_2$, and the Hermitian decomposition $\mathbb{M}_+ \oplus \mathbb{M}_-$.

The quadratic form, the inner product, the norm and the Euclidean norm are a form and a distance; they are developed in *Split-Biquaternion Norm and Invertibility*, where the invertibility criterion and the group of units are also established.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | Split complex algebra |
| $\mathbb{H}$ | Quaternion algebra |
| $\mathbb{H}_{\mathbb{D}}$ | Split biquaternion algebra, $\mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ |
| $e_t = 1$ | Identity |
| $\vec e_x, \vec e_y, \vec e_z$ | Quaternion units, $\vec e_\mu^2 = -e_t$ |
| $j$ | Split complex unit, $j^2 = +1$, commutes with $e_\mu$ |
| $\tilde\Pi_1 = \tfrac{1}{2}(1 + j)$ | Positive idempotent |
| $\tilde\Pi_2 = \tfrac{1}{2}(1 - j)$ | Negative idempotent |
| $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ | General split biquaternion |
| $Q_\mu = q_\mu + j q'_\mu$ | Split complex coefficient |
| $Q_t$ | Split scalar part |
| $\vec Q$ | Split vector part |
| $\tilde{Q}^{\natural} = Q_t e_t - \vec Q$ | Quaternion conjugate |
| $\bar{\tilde{Q}} = \bar{Q_t} e_t + \bar{\vec Q}$ | Split complex conjugate |
| $\tilde{Q}^{*} = \bar{Q_t} e_t - \bar{\vec Q}$ | Hermitian conjugate |
| $\tilde{Q}^\flat = -\tilde{Q}^{*}$ | Anti-Hermitian conjugate |
| $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ | Split complex subspace |
| $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ | Quaternion subspace |
| $\mathbb{M}_+$ | Hermitian subspace |
| $\mathbb{M}_-$ | Anti-Hermitian subspace |
| $\tilde{Q}_{\mathrm{H}}, \tilde{Q}_{\mathrm{A}}$ | Hermitian and anti-Hermitian parts of $\tilde{Q}$ |
| $\tilde{Q}_\pm = \tilde{Q} \tilde\Pi_{1,2}$ | Idempotent components of $\tilde{Q}$, in $\mathbb{H}$ |
| $\mathbb{H} \tilde\Pi_1, \mathbb{H} \tilde\Pi_2$ | Idempotent ideals |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original formulation of quaternions and their complexification.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the algebraic structure of the split biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the classification of real algebras.
- F. Brackx, R. Delanghe, and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the general Clifford analysis.
- Companion article *Complex Split Biquaternions and the Clifford Algebra Cl(3)*, for the complexification of this algebra and its splitting into two biquaternion summands.
