# __Biquaternion Algebra__

## Introduction

This article introduces the biquaternion algebra as an algebraic structure and works with it as an **algebra over $\mathbb{C}$**. The goal is to define the algebra precisely, establish its basic properties, and describe the **six** distinguished real subspaces that arise from the natural conjugations: four of dimension four, together with the two-dimensional center and the six-dimensional vector subspace.

$\mathbb{B}$ can also be considered in other ways — as an algebra over $\mathbb{R}$, as a bimodule over $\mathbb{H}$, and in the corresponding coordinate systems. Those views are the subject of *Different Ways to Consider Biquaternions*. Here $\mathbb{B}$ is read as an algebra over $\mathbb{C}$; the underlying real space is used only for the six subspaces.

The treatment is elementary and self-contained: every claim is either proved or stated as a definition, and no physics is invoked. The anti-Hermitian subspace is defined algebraically. No form appears in this article; the Hermitian form, the inner product and everything measured with them belong to the Topology group. The product of the algebra — its definition, its two scalar–vector parts, and the dot and cross products they are built from — is *Biquaternion Multiplication*, and it is used here as given.

The quaternion algebra $\mathbb{H}$ is assumed from the article on quaternion algebra, together with its basis, its multiplication and its conjugation. No facts about $\mathbb{H}$ are restated here.

## Biquaternions

### Definition

The **biquaternion algebra** is the complexification of the quaternion algebra:

$$
\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}.
$$

As a $\mathbb{C}$-algebra it is **four-dimensional**, with complex basis $\{e_0, e_1, e_2, e_3\}$. Its multiplication is the one defined and studied in *Biquaternion Multiplication*; with it the algebra is associative and unital, with unit $e_0$. Its center is the scalar line $\mathbb{C}e_0$. The underlying real space, in which the six subspaces of this article are cut out, is **eight-dimensional**, with real basis $\{e_0, e_1, e_2, e_3, ie_0, ie_1, ie_2, ie_3\}$.

The complex dimension four and the real dimension eight are related by

$$
\dim_{\mathbb{R}} \mathbb{B} = 2 \dim_{\mathbb{C}} \mathbb{B},
$$

because each complex coefficient contributes its real and imaginary parts.

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

As a $\mathbb{C}$-algebra the coordinates of $\tilde{Q}$ are the four complex numbers $(Q_0, Q_1, Q_2, Q_3)$.

### The Algebra Structure

As a $\mathbb{C}$-algebra $\mathbb{B}$ is four-dimensional, associative and non-commutative. It is not a division algebra: it has zero divisors, and the study of these is the subject of the divisibility article.

The **center** of $\mathbb{B}$ is the scalar line $\mathbb{C}e_0 = \{Q_0 e_0 : Q_0 \in \mathbb{C}\}$. As a real space it is spanned by $e_0$ and $ie_0$, and it is the first of the six subspaces below.

### Conjugations

There are **four** natural conjugations on $\mathbb{B}$. The first three are obtained from the quaternion conjugation ${}^{\natural}$ and the complex conjugation $\bar{\cdot}$; the fourth is defined as the negative of Hermitian conjugation:

**Quaternion conjugation** $\tilde{Q}^{\natural}$:

$$
\tilde{Q}^{\natural} = Q_0 e_0 - Q_1 e_1 - Q_2 e_2 - Q_3 e_3.
$$

**Complex conjugation** $\bar{\tilde{Q}}$:

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

Each conjugation is an involution: applying it twice returns the original biquaternion. Each therefore splits $\mathbb{B}$ into a fixed space and an anti-fixed space, and each of the two is a real vector subspace of $\mathbb{B}$.

### The Group of Conjugations

The quaternion conjugation ${}^{\natural}$ and the complex conjugation $\bar{\cdot}$ are commuting involutions. They generate the Klein four-group

$$
\{\mathrm{id},{}^{\natural},\bar{\cdot},{}^{*}\}\cong \mathbb{Z}/2\times \mathbb{Z}/2,
$$

where

$$
\tilde{Q}^{*}=\overline{\tilde{Q}^{\natural}}=\bar{\tilde{Q}}^{\natural}.
$$

Thus Hermitian conjugation is the composition of the two commuting generators.

The anti-Hermitian conjugation is defined by

$$
\tilde{Q}^\flat=-\tilde{Q}^{*}=-\overline{\tilde{Q}^{\natural}}.
$$

It is an involution, since $(\tilde{Q}^\flat)^\flat=\tilde{Q}$, but it is not an algebra anti-automorphism and it is not a member of the Klein four-group above. Composing it with ${}^{*}$ gives

$$
(\tilde{Q}^{*})^\flat=-\tilde{Q},\qquad
(\tilde{Q}^\flat)^\dagger=-\tilde{Q}.
$$

So $\flat$ is determined by ${}^{*}$ together with the central sign $-1$. The four natural conjugations are ${}^{\natural},\bar{\cdot},{}^{*},{}^{\flat}$, but only $\{\mathrm{id},{}^{\natural},\bar{\cdot},{}^{*}\}$ forms a group under composition.

## The Six Subspaces

The three commuting involutions ${}^{\natural}$, $\bar{\cdot}$ and ${}^{*}$ (with ${}^{*} = {}^{\natural}\circ\bar{\cdot}$) each split $\mathbb{B}$ into a fixed space and an anti-fixed space. The spaces so obtained are the **six distinguished subspaces** of $\mathbb{B}$: the **centre** $\mathbb{C}_{\mathbb{B}}$, of real dimension $2$, fixed by ${}^{\natural}$; the **vector subspace** $\mathrm{Vect}(\mathbb{B})$, of dimension $6$, the anti-fixed space of ${}^{\natural}$ and the kernel of the scalar-part functional; the **quaternion subspace** $\mathbb{H}_{\mathbb{B}}$, of dimension $4$, fixed by $\bar{\cdot}$; the **anti-quaternion subspace** $i\mathbb{H}_{\mathbb{B}}$, of dimension $4$, the anti-fixed space of $\bar{\cdot}$; the **Hermitian subspace** $\mathbb{M}_+$, of dimension $4$, fixed by ${}^{*}$; and the **anti-Hermitian subspace** $\mathbb{M}_-$, of dimension $4$, fixed by $\flat = -{}^{*}$. The fourth conjugation produces no space beyond these, its two eigenspaces being those of ${}^{*}$ with the signs exchanged, which is why there are six of them and not eight. Exactly two of the six are subalgebras, the centre $\mathbb{C}_{\mathbb{B}} \cong \mathbb{C}$ and the quaternion subspace $\mathbb{H}_{\mathbb{B}} \cong \mathbb{H}$, and both are division algebras.

Each of the six is defined and tabulated in *Introduction to the Six Subspaces*, one subspace to a section. Their bases, the four coordinate blocks out of which they are built, their pairwise intersections, their sums, the action of the four conjugations upon them and the action of the central imaginary unit are *Comparison of the Six Subspaces*, which carries the tables. The present article uses the three decompositions of the following sections and nothing else of the six.

## The Quaternion Decomposition

The complex conjugation $\bar{\cdot}$ is an involution, and the two subspaces just named are its eigenspaces: $\mathbb{H}_{\mathbb{B}}$ is the eigenspace of eigenvalue $+1$ and $i\mathbb{H}_{\mathbb{B}}$ the eigenspace of eigenvalue $-1$. Both have real dimension 4, and they are independent, so $\mathbb{B}$ splits as a direct sum of the two.

Every biquaternion can be written uniquely as

$$
\tilde{Q} = \tilde{Q}_r + i \tilde{Q}_i,
$$

where $\tilde{Q}_r$ and $\tilde{Q}_i$ are **ordinary quaternions** (elements of $\mathbb{H}$ embedded in $\mathbb{B}$), with real coefficients. The two components are

$$
\tilde{Q}_r = \frac{1}{2}(\tilde{Q} + \bar{\tilde{Q}}), \qquad \tilde{Q}_i = \frac{1}{2i}(\tilde{Q} - \bar{\tilde{Q}}).
$$

Indeed, $\tilde{Q}_r$ is fixed by complex conjugation, so it lies in the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, and $\tilde{Q}_i$ is also fixed by complex conjugation. To see the latter, compute

$$
\bar{\tilde{Q}_i} = \left(\frac{1}{2i}(\tilde{Q} - \bar{\tilde{Q}})\right)^* = \frac{-1}{2i}\left(\bar{\tilde{Q}} - \tilde{Q}\right) = \frac{1}{2i}\left(\tilde{Q} - \bar{\tilde{Q}}\right) = \tilde{Q}_i,
$$

so $\tilde{Q}_i$ lies in $\mathbb{H}_{\mathbb{B}}$ as well. The sum is $\tilde{Q}_r + i \tilde{Q}_i = \tilde{Q}$.

This gives the direct sum decomposition

$$
\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i \mathbb{H}_{\mathbb{B}},
$$

where $i\mathbb{H}_{\mathbb{B}}$ is the set of biquaternions of the form $i \tilde{Q}$ with $\tilde{Q} \in \mathbb{H}_{\mathbb{B}}$. Both are real vector spaces of dimension 4, and their direct sum is the full algebra $\mathbb{B}$ of real dimension 8.

This is the **quaternion decomposition** of a biquaternion. It expresses $\tilde{Q}$ as a quaternion plus the scalar imaginary times another quaternion. It is the natural decomposition when we think of $\mathbb{B}$ as the complexification of $\mathbb{H}$: the first summand is the "real part" and the second is the "imaginary part" of the complexification.

## The Hermitian Decomposition

The Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$ are the two eigenspaces of the Hermitian conjugation ${}^{*}$. Every biquaternion decomposes uniquely as the sum of a Hermitian part and an anti-Hermitian part:

$$
\tilde{Q} = \tilde{Q}_+ + \tilde{Q}_-, \qquad \tilde{Q}_+ \in \mathbb{M}_+, \quad \tilde{Q}_- \in \mathbb{M}_-.
$$

The two components are obtained from the Hermitian conjugation:

$$
\tilde{Q}_+ = \frac{1}{2}(\tilde{Q} + \tilde{Q}^{*}), \qquad \tilde{Q}_- = \frac{1}{2}(\tilde{Q} - \tilde{Q}^{*}).
$$

Indeed, $\tilde{Q}_+$ is fixed by Hermitian conjugation, so it lies in $\mathbb{M}_+$, and $\tilde{Q}_-$ satisfies $\tilde{Q}_-^\dagger = -\tilde{Q}_-$, so it lies in $\mathbb{M}_-$. The sum is $\tilde{Q}_+ + \tilde{Q}_- = \tilde{Q}$.

This gives the direct sum decomposition

$$
\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-,
$$

where $\mathbb{M}_+$ is the Hermitian subspace and $\mathbb{M}_-$ is the anti-Hermitian subspace. Both are real vector spaces of dimension 4, and their direct sum is the full algebra $\mathbb{B}$ of real dimension 8.

The decomposition is the algebraic analogue of writing a complex number as the sum of its real and imaginary parts. Here, however, both components are biquaternions, and the two subspaces $\mathbb{M}_+$ and $\mathbb{M}_-$ are not subalgebras of $\mathbb{B}$; the decomposition is a vector-space decomposition, not an algebra decomposition.

## The Center and Vector Decomposition

The quaternion conjugation ${}^{\natural}$ is the third commuting involution. Its eigenspaces are the center $\mathbb{C}_{\mathbb{B}}$ (eigenvalue $+1$) and the vector subspace $\mathrm{Vect}(\mathbb{B})$ (eigenvalue $-1$), of real dimensions 2 and 6. Every biquaternion therefore decomposes uniquely as a scalar plus a pure vector part:

$$
\tilde{Q} = \tilde{Q}_{\mathrm{c}} + \tilde{Q}_{\mathrm{v}}, \qquad \tilde{Q}_{\mathrm{c}} = Q_0 e_0 \in \mathbb{C}_{\mathbb{B}}, \quad \tilde{Q}_{\mathrm{v}} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3 \in \mathrm{Vect}(\mathbb{B}),
$$

with

$$
\tilde{Q}_{\mathrm{c}} = \frac{1}{2}(\tilde{Q} + \tilde{Q}^{\natural}), \qquad \tilde{Q}_{\mathrm{v}} = \frac{1}{2}(\tilde{Q} - \tilde{Q}^{\natural}).
$$

This gives the direct sum decomposition

$$
\mathbb{B} = \mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B}),
$$

the two summands being of real dimensions 2 and 6. It is the decomposition into scalar and vector parts, and it is the one with summands of unequal dimension: the other two decompositions split $\mathbb{B}$ into two halves of dimension 4.

## Relation Between the Three Decompositions

The three decompositions

$$
\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i \mathbb{H}_{\mathbb{B}}, \qquad \mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-, \qquad \mathbb{B} = \mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B})
$$

are the eigenspace decompositions of the three pairwise commuting involutions $\bar{\cdot}$, ${}^{*}$ and ${}^{\natural}$, and they are the only decompositions of this kind: $\flat = -{}^{*}$ reproduces the eigenspaces of ${}^{*}$ with the signs exchanged and gives nothing new, so there are exactly three decompositions and six subspaces.

The three are the three ways of splitting the four coordinate blocks into two complementary pairs, they are the only pairs of distinct subspaces whose intersection is trivial, and they are the only pairs that sum to the whole algebra. The blocks, the pairings, the full table of the fifteen pairwise intersections, the sums and the action of the four conjugations on the six subspaces are in *Comparison of the Six Subspaces*.

## Summary

The biquaternion algebra is $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$, a four-dimensional algebra over $\mathbb{C}$ whose underlying real space has dimension eight, with basis $e_0 = 1, e_1, e_2, e_3$, $e_k^2 = -e_0$, and central scalar imaginary $i$. It is associative, non-commutative, and not a division algebra.

It carries four natural conjugations, ${}^{\natural}$, $\bar{\cdot}$, ${}^{*}$ and $\flat = -{}^{*}$, of which the first three are commuting involutions and form the Klein four-group together with the identity. They define the six distinguished real subspaces of $\mathbb{B}$: the centre $\mathbb{C}_{\mathbb{B}}$ and the vector subspace $\mathrm{Vect}(\mathbb{B})$, of dimensions $2$ and $6$, and the quaternion, anti-quaternion, Hermitian and anti-Hermitian subspaces $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ and $\mathbb{M}_-$, of dimension $4$. They give the three direct-sum decompositions $\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}}$, $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$ and $\mathbb{B} = \mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B})$. The six subspaces and their bases are *Introduction to the Six Subspaces*; the coordinate blocks, the intersections, the sums and the action of the conjugations upon them are *Comparison of the Six Subspaces*.

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
| $\tilde{Q}^{\natural} = Q_0 e_0 - \mathbf{Q}$ | Quaternion conjugate |
| $\bar{\tilde{Q}} = \bar{Q_0} e_0 + \mathbf{Q}^*$ | Complex conjugate |
| $\tilde{Q}^{*} = \bar{Q_0} e_0 - \mathbf{Q}^*$ | Hermitian conjugate |
| $\tilde{Q}^\flat = -\overline{\tilde{Q}^{\natural}} = -\tilde{Q}^{*}$ | Anti-Hermitian conjugate |
| $\mathbb{C}_{\mathbb{B}}$ | Center (complex subspace), fixed-point set of ${}^{\natural}$; basis $e_0, ie_0$ |
| $\mathrm{Vect}(\mathbb{B})$ | Vector subspace, anti-fixed-point set of ${}^{\natural}$; $\{\tilde{Q} : \mathrm{Sc}(\tilde{Q}) = 0\} = [\mathbb{B}, \mathbb{B}]$; basis $e_1, e_2, e_3, ie_1, ie_2, ie_3$ |
| $\mathbb{H}_{\mathbb{B}}$ | Quaternion subspace, fixed-point set of $\bar{\cdot}$; basis $e_0, e_1, e_2, e_3$ |
| $i\mathbb{H}_{\mathbb{B}}$ | Anti-quaternion subspace, anti-fixed-point set of $\bar{\cdot}$; basis $ie_0, ie_1, ie_2, ie_3$ |
| $\mathbb{M}_+$ | Hermitian subspace, fixed-point set of ${}^{*}$; basis $e_0, ie_1, ie_2, ie_3$ |
| $\mathbb{M}_-$ | Anti-Hermitian subspace, fixed-point set of $\flat$; basis $ie_0, e_1, e_2, e_3$ |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original formulation.
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the first systematic treatment of biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.

