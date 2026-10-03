
# __Split-Biquaternion Algebra__

## Introduction

This article introduces the split biquaternion algebra as an algebraic structure. The goal is to define the algebra precisely, establish its basic properties, and describe the distinguished real vector subspaces that arise from the natural conjugations.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. No examples are given. The quaternion algebra $\mathbb{H}$ is assumed from the article on quaternion algebra. The split complex algebra $\mathbb{D}$ is assumed from the article on split complex algebra, together with its idempotents $\tilde\Pi_+ = \tfrac{1}{2}(1 + j)$ and $\tilde\Pi_- = \tfrac{1}{2}(1 - j)$ and the isomorphism $\mathbb{D} \cong \mathbb{R} \oplus \mathbb{R}$.

Throughout this article, the quaternion basis is written $e_0 = 1, e_1, e_2, e_3$, and the split complex unit is written $j$, with $j^2 = +1$. The unit $j$ commutes with the quaternion units: $j e_k = e_k j$ for $k = 0, 1, 2, 3$.

## The Split Biquaternions

### Definition

The **split biquaternion algebra** is the tensor product

$$
\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H},
$$

where $\mathbb{D}$ is the split complex algebra and $\mathbb{H}$ is the quaternion algebra. It is also met, in the form $\mathbb{H} \oplus \mathbb{H}$, as the algebra of the two quaternion halves.

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

**Associative.** Split biquaternion multiplication is associative: $(\tilde P \tilde{Q}) \tilde{R} = \tilde P (\tilde{Q} \tilde{R})$.

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
\tilde\Pi_+ = \tfrac{1}{2}(1 + j), \qquad \tilde\Pi_- = \tfrac{1}{2}(1 - j).
$$

They satisfy

$$
\tilde\Pi_+^2 = \tilde\Pi_+, \qquad \tilde\Pi_-^2 = \tilde\Pi_-, \qquad \tilde\Pi_+ \tilde\Pi_- = \tilde\Pi_- \tilde\Pi_+ = 0, \qquad \tilde\Pi_+ + \tilde\Pi_- = 1.
$$

Every split biquaternion is written uniquely in the idempotent basis as

$$
\tilde{Q} = \tilde{Q}_+ \tilde\Pi_+ + \tilde{Q}_- \tilde\Pi_-,
$$

where $\tilde{Q}_\pm \in \mathbb{H}$ are ordinary quaternions, given by

$$
\tilde{Q}_+ = \tilde{Q} \tilde\Pi_+ = Q_0' + Q_1' e_1 + Q_2' e_2 + Q_3' e_3,
$$

$$
\tilde{Q}_- = \tilde{Q} \tilde\Pi_- = Q_0'' + Q_1'' e_1 + Q_2'' e_2 + Q_3'' e_3,
$$

with real coefficients $Q_\mu', Q_\mu'' \in \mathbb{R}$.

The map

$$
\varphi : \mathbb{H}_{\mathbb{D}} \to \mathbb{H} \oplus \mathbb{H}, \qquad \varphi(\tilde{Q}) = (\tilde{Q}_+, \tilde{Q}_-),
$$

is an algebra isomorphism, where the multiplication on $\mathbb{H} \oplus \mathbb{H}$ is componentwise. This is the **idempotent decomposition** of the split biquaternion algebra.

The isomorphism is the reason the algebra is semisimple. It is not simple, because the two summands $\mathbb{H} \tilde\Pi_+$ and $\mathbb{H} \tilde\Pi_-$ are nontrivial two-sided ideals.

### The Clifford Structure

The algebra is also a Clifford algebra, of three generators of square $-1$ — the sign opposite to the generators of the biquaternion algebra's Clifford reading, where the three generators square to $+1$.

**Proposition (the generators).** The three elements

$$
E_1 = je_1, \qquad E_2 = je_2, \qquad E_3 = je_3
$$

satisfy

$$
E_k^2 = -1, \qquad E_iE_j = -E_jE_i \quad (i \neq j),
$$

so that $\{E_i, E_j\} = -2\delta_{ij}$. They therefore generate a copy of the real Clifford algebra $\mathrm{Cl}(0,3)$.

*Proof.* Because $j$ is central with $j^2=+1$ and the quaternion units satisfy $e_k^2=-1$ and $e_ie_j=-e_je_i$ for $i\neq j$,
$$
E_k^2 = j^2e_k^2 = -1, \qquad E_iE_j = j^2e_ie_j = -e_je_i = -E_jE_i .
$$
$\square$

**Proposition (identification and volume element).** The eight monomials in $E_1,E_2,E_3$ are linearly independent and span $\mathbb{H}_{\mathbb{D}}$, so

$$
\mathbb{H}_{\mathbb{D}} \cong \mathrm{Cl}(0,3) \cong \mathrm{Cl}_{0,3},
$$

the Clifford algebra of a three-dimensional negative definite space. The volume element is

$$
E_1E_2E_3 = j^3(e_1e_2)e_3 = j\,e_3e_3 = -j,
$$

which is central with square $+1$; the Clifford idempotents $\tfrac12(1 \pm E_1E_2E_3) = \tfrac12(1 \mp j)$ are the idempotents $\tilde\Pi_\mp$ of the idempotent decomposition, with the index reversed.

*Proof.* The monomials are the eight elements $\tilde\Pi_\pm$ times the quaternion basis and are independent; the product is immediate from $j^2=1$, $e_1e_2=e_3$ and $e_3^2=-1$. $\square$

**Proposition (the complexification).** The complexification $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}_{\mathbb{D}}$ is the complex Clifford algebra

$$
\mathrm{Cl}(3) \cong \mathrm{Cl}_3(\mathbb{C}) \cong M_2(\mathbb{C}) \oplus M_2(\mathbb{C}) \cong \mathbb{B} \oplus \mathbb{B},
$$

whose two simple summands are the complexified quaternion halves; its volume element is the element $-j$, central and an involution, and it is the algebra studied in *Complex Split Biquaternions and the Clifford Algebra Cl(3)*.

*Proof.* Complexification extends scalars, so the relations of the $E_i$ are unchanged and the complexified monomials are a basis; the classification of the odd complex Clifford algebras gives $\mathrm{Cl}_3(\mathbb{C})\cong M_2(\mathbb{C})\oplus M_2(\mathbb{C})$, and the complexified idempotent decomposition gives the two summands $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong\mathbb{B}$. $\square$

The Clifford reading is the reason the split biquaternion algebra is the natural lower rung of a doubling: its volume element is a central involution rather than a complex structure, so its complexification splits into two copies of the biquaternion algebra where the biquaternion algebra itself is simple.

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

There are **four** natural conjugations on $\mathbb{H}_{\mathbb{D}}$, obtained by composing the quaternion conjugation ${}^{\natural}$ and the split complex conjugation $\bar{\cdot}$:

**Quaternion conjugation** $\tilde{Q}^{\natural}$:

$$
\tilde{Q}^{\natural} = Q_0 e_0 - Q_1 e_1 - Q_2 e_2 - Q_3 e_3.
$$

**Split complex conjugation** $\bar{\tilde{Q}}$:

$$
\bar{\tilde{Q}} = \bar{Q_0} e_0 + \bar{Q_1} e_1 + \bar{Q_2} e_2 + \bar{Q_3} e_3.
$$

**Hermitian conjugation** $\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}}$:

$$
\tilde{Q}^{*} = \bar{Q_0} e_0 - \bar{Q_1} e_1 - \bar{Q_2} e_2 - \bar{Q_3} e_3.
$$

**Anti-Hermitian conjugation** $\tilde{Q}^\flat = -\tilde{Q}^{*}$:

$$
\tilde{Q}^\flat = -\bar{Q_0} e_0 + \bar{Q_1} e_1 + \bar{Q_2} e_2 + \bar{Q_3} e_3.
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

The fixed points of **split complex conjugation** are the split biquaternions satisfying $\bar{\tilde{Q}} = \tilde{Q}$. In developed form,

$$
\bar{Q_0} e_0 + \bar{Q_1} e_1 + \bar{Q_2} e_2 + \bar{Q_3} e_3 = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3.
$$

Comparing the coefficients:

- $\bar{Q_0} = Q_0$, so $Q_0$ is real.
- $\bar{Q_1} = Q_1$, so $Q_1$ is real.
- $\bar{Q_2} = Q_2$, so $Q_2$ is real.
- $\bar{Q_3} = Q_3$, so $Q_3$ is real.

The fixed points are split biquaternions with real coefficients:

$$
\tilde{Q} = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3, \qquad q_\mu \in \mathbb{R}.
$$

This is the **quaternion subspace** $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$, a copy of the real quaternion algebra embedded in $\mathbb{H}_{\mathbb{D}}$. It is a real vector space of dimension 4. It is a subalgebra of $\mathbb{H}_{\mathbb{D}}$, isomorphic to $\mathbb{H}$.

### The Hermitian Subspace

The fixed points of **Hermitian conjugation** are the split biquaternions satisfying $\tilde{Q}^{*} = \tilde{Q}$. In developed form,

$$
\bar{Q_0} e_0 - \bar{Q_1} e_1 - \bar{Q_2} e_2 - \bar{Q_3} e_3 = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3.
$$

Comparing the coefficients:

- $\bar{Q_0} = Q_0$, so $Q_0$ is real.
- $-\bar{Q_1} = Q_1$, so $\bar{Q_1} = -Q_1$, which means $Q_1$ is purely split-imaginary, i.e., $Q_1 = j r_1$ with $r_1 \in \mathbb{R}$.
- Similarly, $Q_2$ and $Q_3$ are purely split-imaginary.

The fixed points are split biquaternions of the form

$$
\tilde{Q} = q_0 e_0 + j q'_1 e_1 + j q'_2 e_2 + j q'_3 e_3, \qquad q_0, q'_1, q'_2, q'_3 \in \mathbb{R}.
$$

This is the **Hermitian subspace** $\mathbb{M}_+$, a real vector space of dimension 4. It consists of split biquaternions with real scalar part and purely split-imaginary vector part. It is not a subalgebra of $\mathbb{H}_{\mathbb{D}}$.

### The Anti-Hermitian Subspace

The fixed points of **anti-Hermitian conjugation** are the split biquaternions satisfying $\tilde{Q}^\flat = \tilde{Q}$, or equivalently $\tilde{Q} = -\tilde{Q}^{*}$. In developed form,

$$
-\bar{Q_0} e_0 + \bar{Q_1} e_1 + \bar{Q_2} e_2 + \bar{Q_3} e_3 = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3.
$$

Comparing the coefficients:

- $-\bar{Q_0} = Q_0$, so $\bar{Q_0} = -Q_0$, which means $Q_0$ is purely split-imaginary, i.e., $Q_0 = j r_0$ with $r_0 \in \mathbb{R}$.
- $\bar{Q_1} = Q_1$, so $Q_1$ is real.
- Similarly, $Q_2$ and $Q_3$ are real.

The fixed points are split biquaternions of the form

$$
\tilde{Q} = j r_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3, \qquad r_0, q_1, q_2, q_3 \in \mathbb{R}.
$$

This is the **anti-Hermitian subspace** $\mathbb{M}_-$, a real vector space of dimension 4. It consists of split biquaternions with purely split-imaginary scalar part and real vector part. It is not a subalgebra of $\mathbb{H}_{\mathbb{D}}$.

## Quaternion Decomposition

The split complex subspace $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ and the quaternion subspace $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ are not the two eigenspaces of a single involution; they are different fixed-point sets. However, there is a natural decomposition of $\mathbb{H}_{\mathbb{D}}$ associated with the split complex conjugation $\bar{\cdot}$.

Every split biquaternion can be written uniquely as

$$
\tilde{Q} = \tilde{Q}_r + j \tilde{Q}_i,
$$

where $\tilde{Q}_r$ and $\tilde{Q}_i$ are **ordinary quaternions** (elements of $\mathbb{H}$ embedded in $\mathbb{H}_{\mathbb{D}}$), with real coefficients. The two components are

$$
\tilde{Q}_r = \frac{1}{2}(\tilde{Q} + \bar{\tilde{Q}}), \qquad \tilde{Q}_i = \frac{1}{2j}(\tilde{Q} - \bar{\tilde{Q}}).
$$

Indeed, $\tilde{Q}_r$ is fixed by split complex conjugation and so is $\tilde{Q}_i$ (compute $\bar{\tilde{Q}_i} = \tilde{Q}_i$), so both lie in the quaternion subspace $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$; equivalently, $(j\tilde{Q}_i)^* = -j\tilde{Q}_i$ exhibits $j\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ as the $-1$ eigenspace of $\bar{\cdot}$.

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
\tilde{Q} = \tilde{Q}_+ \tilde\Pi_+ + \tilde{Q}_- \tilde\Pi_-,
$$

where $\tilde\Pi_\pm = \tfrac{1}{2}(1 \pm j)$ are the idempotents, and $\tilde{Q}_\pm = \tilde{Q} \tilde\Pi_\pm \in \mathbb{H}$.

This gives the direct sum decomposition

$$
\mathbb{H}_{\mathbb{D}} = \mathbb{H} \tilde\Pi_+ \oplus \mathbb{H} \tilde\Pi_-,
$$

where $\mathbb{H} \tilde\Pi_+$ and $\mathbb{H} \tilde\Pi_-$ are the two ideals of $\mathbb{H}_{\mathbb{D}}$, each isomorphic to $\mathbb{H}$. Both are real vector spaces of dimension 4, and their direct sum is the full algebra $\mathbb{H}_{\mathbb{D}}$ of real dimension 8.

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

The two decompositions are related by multiplication by the split complex unit $j$, which maps $\mathbb{M}_+$ to $\mathbb{M}_-$ and vice versa. The idempotent decomposition is a third decomposition, associated with the idempotents $\tilde\Pi_\pm$, and it is the one that reveals the semisimple structure of the algebra.

## The Lie Algebra Structure

The split biquaternion algebra carries a Lie bracket, defined by the commutator

$$
[\tilde P, \tilde{Q}] = \tilde P \tilde{Q} - \tilde{Q} \tilde P.
$$

The Lie algebra structure of $\mathbb{H}_{\mathbb{D}}$ is the direct sum of two copies of the Lie algebra of $\mathbb{H}$, because the algebra is isomorphic to $\mathbb{H} \oplus \mathbb{H}$. In particular, the pure split biquaternions (with respect to the quaternion conjugation) form a Lie subalgebra isomorphic to $\mathrm{SO}(3) \oplus \mathrm{SO}(3)$. The group this Lie algebra integrates to, and the motions it defines, are treated in Geometry, where the form is available.

## Summary

The split biquaternion algebra is the tensor product $\mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ of the split complex algebra and the quaternion algebra. It is an eight-dimensional real algebra, non-commutative and associative, with zero divisors. It is not a division algebra, and it is not simple, but it is semisimple.

The algebra is isomorphic to the direct sum $\mathbb{H} \oplus \mathbb{H}$ via the idempotent decomposition $\tilde{Q} = \tilde{Q}_+ \tilde\Pi_+ + \tilde{Q}_- \tilde\Pi_-$, where $\tilde\Pi_\pm = \tfrac{1}{2}(1 \pm j)$ are the idempotents of the split complex algebra. This is the most important structural fact about the algebra.

There are four natural conjugations: quaternion conjugation, split complex conjugation, Hermitian conjugation, and anti-Hermitian conjugation. Each has a fixed-point set, which is a four-dimensional real subspace (or two-dimensional in the case of the split complex subspace). The four subspaces are the split complex subspace, the quaternion subspace, the Hermitian subspace, and the anti-Hermitian subspace.

There are three natural decompositions of the algebra: the quaternion decomposition $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}} \oplus j \mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$, the idempotent decomposition $\mathbb{H} \tilde\Pi_+ \oplus \mathbb{H} \tilde\Pi_-$, and the Hermitian decomposition $\mathbb{M}_+ \oplus \mathbb{M}_-$.

The quadratic form, the inner product, the norm and the Euclidean norm are a form and a distance; they are developed in *Split-Biquaternion Norm and Invertibility*, where the invertibility criterion and the group of units are also established.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | Split complex algebra |
| $\mathbb{H}$ | Quaternion algebra |
| $\mathbb{H}_{\mathbb{D}}$ | Split biquaternion algebra, $\mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ |
| $e_0 = 1$ | Identity |
| $e_1, e_2, e_3$ | Quaternion units, $e_k^2 = -e_0$ |
| $j$ | Split complex unit, $j^2 = +1$, commutes with $e_k$ |
| $\tilde\Pi_+ = \tfrac{1}{2}(1 + j)$ | Positive idempotent |
| $\tilde\Pi_- = \tfrac{1}{2}(1 - j)$ | Negative idempotent |
| $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ | General split biquaternion |
| $Q_\mu = q_\mu + j q'_\mu$ | Split complex coefficient |
| $Q_0$ | Split scalar part |
| $\mathbf{Q}$ | Split vector part |
| $\tilde{Q}^{\natural} = Q_0 e_0 - \mathbf{Q}$ | Quaternion conjugate |
| $\bar{\tilde{Q}} = \bar{Q_0} e_0 + \mathbf{Q}^*$ | Split complex conjugate |
| $\tilde{Q}^{*} = \bar{Q_0} e_0 - \mathbf{Q}^*$ | Hermitian conjugate |
| $\tilde{Q}^\flat = -\tilde{Q}^{*}$ | Anti-Hermitian conjugate |
| $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ | Split complex subspace |
| $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ | Quaternion subspace |
| $\mathbb{M}_+$ | Hermitian subspace |
| $\mathbb{M}_-$ | Anti-Hermitian subspace |
| $\tilde{Q}_{\mathrm{H}}, \tilde{Q}_{\mathrm{A}}$ | Hermitian and anti-Hermitian parts of $\tilde{Q}$ |
| $\tilde{Q}_\pm = \tilde{Q} \tilde\Pi_\pm$ | Idempotent components of $\tilde{Q}$, in $\mathbb{H}$ |
| $\mathbb{H} \tilde\Pi_+, \mathbb{H} \tilde\Pi_-$ | Idempotent ideals |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original formulation of quaternions and their complexification.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the algebraic structure of the split biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the classification of real algebras.
- F. Brackx, R. Delanghe, and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the general Clifford analysis.
- Companion article *Complex Split Biquaternions and the Clifford Algebra Cl(3)*, for the complexification of this algebra and its splitting into two biquaternion summands.
