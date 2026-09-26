# __Biquaternion Algebra__

## Introduction

This article introduces the biquaternion algebra as an algebraic structure, without yet discussing its representations. The goal is to define the algebra precisely, establish its basic properties, and describe the **six** distinguished real subspaces that arise from the natural conjugations: four of dimension four, together with the two-dimensional center and the six-dimensional vector subspace.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. The anti-Hermitian subspace is defined algebraically.

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

The two views are related by a change of base ring: passing from the quaternion algebra $\mathbb{H}$ to the $\mathbb{C}$-algebra is the operation of **extension of scalars** from $\mathbb{R}$ to $\mathbb{C}$, and passing back is the operation of **restriction of scalars**. The dimension changes as follows:

$$
\dim_{\mathbb{R}} \mathbb{B} = 2 \cdot \dim_{\mathbb{C}} \mathbb{B},
$$

because each complex dimension contributes two real dimensions (the real and imaginary parts of each complex coefficient).

**Which view to use.** The two views are complementary, and both are used in the literature.

- The **$\mathbb{C}$-algebra view** is the natural one when the biquaternions are studied as a complex algebra, for instance in the context of complex representations, complex Lie algebras, or the algebra $M_2(\mathbb{C})$ of $2 \times 2$ complex matrices. In this view, the algebra is four-dimensional and its structure is relatively simple: it is isomorphic to $M_2(\mathbb{C})$.

- The **$\mathbb{R}$-algebra view** is the natural one when the biquaternions are studied as a real algebra, for instance in the context of real representations or real Clifford algebras. In this view, the algebra is eight-dimensional, and the six real subspaces $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$, $\mathbb{M}_-$ that we describe below are all real vector subspaces of this eight-dimensional real algebra.

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

There are **four** natural conjugations on $\mathbb{B}$. The first three are obtained from the quaternion conjugation $\bar{\cdot}$ and the complex conjugation ${}^*$; the fourth is defined as the negative of Hermitian conjugation:

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

Each conjugation is an involution: applying it twice returns the original biquaternion. Each therefore splits $\mathbb{B}$ into a fixed space and an anti-fixed space, and each of the two is a real vector subspace of $\mathbb{B}$.

### The Group of Conjugations

The quaternion conjugation $\bar{\cdot}$ and the complex conjugation ${}^*$ are commuting involutions. They generate the Klein four-group

$$
\{\mathrm{id},\bar{\cdot},{}^{*},{}^{\dagger}\}\cong \mathbb{Z}/2\times \mathbb{Z}/2,
$$

where

$$
\tilde{Q}^\dagger=\bar{\tilde{Q}}^*=\tilde{Q}^{*\bar{}}.
$$

Thus Hermitian conjugation is the composition of the two commuting generators.

The anti-Hermitian conjugation is defined by

$$
\tilde{Q}^\flat=-\tilde{Q}^\dagger=-\bar{\tilde{Q}}^*.
$$

It is an involution, since $(\tilde{Q}^\flat)^\flat=\tilde{Q}$, but it is not an algebra anti-automorphism and it is not a member of the Klein four-group above. Composing it with $\dagger$ gives

$$
(\tilde{Q}^\dagger)^\flat=-\tilde{Q},\qquad
(\tilde{Q}^\flat)^\dagger=-\tilde{Q}.
$$

So $\flat$ is determined by $\dagger$ together with the central sign $-1$. The four natural conjugations are $\bar{\cdot},{}^{*},{}^{\dagger},{}^{\flat}$, but only $\{\mathrm{id},\bar{\cdot},{}^{*},{}^{\dagger}\}$ forms a group under composition.

## The Six Subspaces

The three commuting involutions $\bar{\cdot}$, ${}^{*}$ and ${}^{\dagger}$ (with $\dagger = \bar{\cdot}\circ{}^{*}$) each split $\mathbb{B}$ into a fixed space and an anti-fixed space. The **six** subspaces so obtained are the distinguished real subspaces of $\mathbb{B}$. Four of them are four-dimensional; the remaining two are the two-dimensional **center** and the six-dimensional **vector subspace**. The fourth conjugation $\flat = -\dagger$ is not independent: it has the same two eigenspaces as $\dagger$, with the signs exchanged, so it produces no further subspace.

| subspace | defining condition | real basis | $\dim_{\mathbb{R}}$ |
|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ (complex, the center) | $\bar{\tilde{Q}} = \tilde{Q}$ | $e_0,\ ie_0$ | $2$ |
| $\mathrm{Vect}(\mathbb{B})$ (vector) | $\bar{\tilde{Q}} = -\tilde{Q}$ | $e_1,\ e_2,\ e_3,\ ie_1,\ ie_2,\ ie_3$ | $6$ |
| $\mathbb{H}_{\mathbb{B}}$ (quaternion) | $\tilde{Q}^{*} = \tilde{Q}$ | $e_0,\ e_1,\ e_2,\ e_3$ | $4$ |
| $i\mathbb{H}_{\mathbb{B}}$ (anti-quaternion) | $\tilde{Q}^{*} = -\tilde{Q}$ | $ie_0,\ ie_1,\ ie_2,\ ie_3$ | $4$ |
| $\mathbb{M}_+$ (Hermitian) | $\tilde{Q}^{\dagger} = \tilde{Q}$ | $e_0,\ ie_1,\ ie_2,\ ie_3$ | $4$ |
| $\mathbb{M}_-$ (anti-Hermitian) | $\tilde{Q}^{\flat} = \tilde{Q}$ | $ie_0,\ e_1,\ e_2,\ e_3$ | $4$ |

Each of the six has its own article in the **Subspaces** group of the series, where its basis and dimension, its algebra and module structure, its norm form, its matrix image, its behaviour under the four conjugations and its intersections with the other five are worked out in full:

| subspace | article |
|---|---|
| $\mathbb{C}_{\mathbb{B}}$, the centre | *Biquaternion Centre Subspace* |
| $\mathrm{Vect}(\mathbb{B})$, the vector subspace | *Biquaternion Vector Subspace* |
| $\mathbb{H}_{\mathbb{B}}$, the quaternion subspace | *Biquaternion Quaternion Subspace* |
| $i\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace | *Biquaternion Anti-Quaternion Subspace* |
| $\mathbb{M}_+$, the Hermitian subspace | *Biquaternion Hermitian Subspace* |
| $\mathbb{M}_-$, the anti-Hermitian subspace | *Biquaternion Anti-Hermitian Subspace* |

The relations between them are collected in *Biquaternion Relations Between Subspaces*, and the four conjugations themselves in *Biquaternion Involution Lattice*. What the present article uses of the six, again and again, is the following:

- $\mathbb{C}_{\mathbb{B}}$ is the set of central elements, a copy of $\mathbb{C}$ embedded as the scalar part, $\{\lambda e_0 : \lambda \in \mathbb{C}\}$;
- $\mathrm{Vect}(\mathbb{B})$ is the kernel of the scalar-part functional, equivalently the derived subspace $[\mathbb{B},\mathbb{B}]$, equivalently the set of traceless elements under $\Phi$, and it is neither a subalgebra nor a module over $\mathbb{H}_{\mathbb{B}}$;
- $\mathbb{H}_{\mathbb{B}}$ is the set of elements with real coefficients, a copy of the real quaternion algebra, and the only non-commutative one of the six;
- $i\mathbb{H}_{\mathbb{B}}$ is the set of products $i\tilde{P}$ with $\tilde{P} \in \mathbb{H}_{\mathbb{B}}$, a two-sided module over $\mathbb{H}_{\mathbb{B}}$ but not a subalgebra;
- $\mathbb{M}_+$ is the set of elements with real scalar part and purely imaginary vector part;
- $\mathbb{M}_-$ is the set of elements with purely imaginary scalar part and real vector part.

### The Six Together

Of the six subspaces, exactly two are subalgebras: the center $\mathbb{C}_{\mathbb{B}} \cong \mathbb{C}$ and the quaternion subspace $\mathbb{H}_{\mathbb{B}} \cong \mathbb{H}$. Both are division algebras. The vector subspace is closed under neither multiplication nor left multiplication by $\mathbb{H}_{\mathbb{B}}$; the anti-quaternion subspace is an $\mathbb{H}_{\mathbb{B}}$-module but not a subalgebra; and the two sectors $\mathbb{M}_\pm$ are neither. The six are pairwise distinct as sets, and no two of them are equal; their dimensions $2, 6, 4, 4, 4, 4$ sum to more than $8$, so they necessarily overlap, and how they do so is the subject of *Biquaternion Relations Between Subspaces*.

## The Quaternion Decomposition

The complex conjugation ${}^{*}$ is an involution, and the two subspaces just defined are its eigenspaces: $\mathbb{H}_{\mathbb{B}}$ is the eigenspace of eigenvalue $+1$ and $i\mathbb{H}_{\mathbb{B}}$ the eigenspace of eigenvalue $-1$. Both have real dimension 4, and they are independent, so $\mathbb{B}$ splits as a direct sum of the two.

Every biquaternion can be written uniquely as

$$
\tilde{Q} = \tilde{Q}_r + i \tilde{Q}_i,
$$

where $\tilde{Q}_r$ and $\tilde{Q}_i$ are **ordinary quaternions** (elements of $\mathbb{H}$ embedded in $\mathbb{B}$), with real coefficients. The two components are

$$
\tilde{Q}_r = \frac{1}{2}(\tilde{Q} + \tilde{Q}^*), \qquad \tilde{Q}_i = \frac{1}{2i}(\tilde{Q} - \tilde{Q}^*).
$$

Indeed, $\tilde{Q}_r$ is fixed by complex conjugation, so it lies in the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, and $\tilde{Q}_i$ is also fixed by complex conjugation. To see the latter, compute

$$
\tilde{Q}_i^* = \left(\frac{1}{2i}(\tilde{Q} - \tilde{Q}^*)\right)^* = \frac{-1}{2i}\left(\tilde{Q}^* - \tilde{Q}\right) = \frac{1}{2i}\left(\tilde{Q} - \tilde{Q}^*\right) = \tilde{Q}_i,
$$

so $\tilde{Q}_i$ lies in $\mathbb{H}_{\mathbb{B}}$ as well. The sum is $\tilde{Q}_r + i \tilde{Q}_i = \tilde{Q}$.

This gives the direct sum decomposition

$$
\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i \mathbb{H}_{\mathbb{B}},
$$

where $i\mathbb{H}_{\mathbb{B}}$ is the set of biquaternions of the form $i \tilde{Q}$ with $\tilde{Q} \in \mathbb{H}_{\mathbb{B}}$. Both are real vector spaces of dimension 4, and their direct sum is the full algebra $\mathbb{B}$ of real dimension 8.

This is the **quaternion decomposition** of a biquaternion. It expresses $\tilde{Q}$ as a quaternion plus the scalar imaginary times another quaternion. It is the natural decomposition when we think of $\mathbb{B}$ as the complexification of $\mathbb{H}$: the first summand is the "real part" and the second is the "imaginary part" of the complexification.

## The Hermitian Decomposition

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

## The Center and Vector Decomposition

The quaternion conjugation $\bar{\cdot}$ is the third commuting involution. Its eigenspaces are the center $\mathbb{C}_{\mathbb{B}}$ (eigenvalue $+1$) and the vector subspace $\mathrm{Vect}(\mathbb{B})$ (eigenvalue $-1$), of real dimensions 2 and 6. Every biquaternion therefore decomposes uniquely as a scalar plus a pure vector part:

$$
\tilde{Q} = \tilde{Q}_{\mathrm{c}} + \tilde{Q}_{\mathrm{v}}, \qquad \tilde{Q}_{\mathrm{c}} = Q_0 e_0 \in \mathbb{C}_{\mathbb{B}}, \quad \tilde{Q}_{\mathrm{v}} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3 \in \mathrm{Vect}(\mathbb{B}),
$$

with

$$
\tilde{Q}_{\mathrm{c}} = \frac{1}{2}(\tilde{Q} + \bar{\tilde{Q}}), \qquad \tilde{Q}_{\mathrm{v}} = \frac{1}{2}(\tilde{Q} - \bar{\tilde{Q}}).
$$

This gives the direct sum decomposition

$$
\mathbb{B} = \mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B}),
$$

the two summands being of real dimensions 2 and 6. It is the decomposition into center and derived subspace, and it is the one with summands of unequal dimension: the other two decompositions split $\mathbb{B}$ into two halves of dimension 4.

## Relation Between the Three Decompositions

The three decompositions

$$
\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i \mathbb{H}_{\mathbb{B}}, \qquad \mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-, \qquad \mathbb{B} = \mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B})
$$

are the eigenspace decompositions of the three pairwise commuting involutions ${}^{*}$, $\dagger$ and $\bar{\cdot}$. They are the only decompositions of this kind: each is determined by one of the three, and $\flat = -\dagger$ reproduces the eigenspaces of $\dagger$ with the signs exchanged and so gives nothing new. That is why there are six subspaces rather than four or eight.

**The four coordinate blocks.** Because the involutions commute, the four-dimensional subspaces are built from four common pieces. Write

$$
A_1 = \mathbb{R} e_0, \qquad A_2 = \mathbb{R}(ie_0), \qquad B_1 = \operatorname{span}_{\mathbb{R}}\{e_1, e_2, e_3\}, \qquad B_2 = \operatorname{span}_{\mathbb{R}}\{ie_1, ie_2, ie_3\}.
$$

These are the two **scalar blocks** $A_1, A_2$ of dimension 1 and the two **vector blocks** $B_1, B_2$ of dimension 3. The two involutions ${}^{*}$ and $\bar{\cdot}$ are diagonal on them, and every one of the six subspaces is a sum of blocks:

| subspace | blocks | $\dim_{\mathbb{R}}$ |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $A_1 \oplus A_2$ | $2$ |
| $\mathrm{Vect}(\mathbb{B})$ | $B_1 \oplus B_2$ | $6$ |
| $\mathbb{H}_{\mathbb{B}}$ | $A_1 \oplus B_1$ | $4$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $A_2 \oplus B_2$ | $4$ |
| $\mathbb{M}_+$ | $A_1 \oplus B_2$ | $4$ |
| $\mathbb{M}_-$ | $A_2 \oplus B_1$ | $4$ |

The pattern is that each of the four four-dimensional subspaces takes one scalar block and one vector block — the four ways of choosing one from each column — while the center takes both scalar blocks and the vector subspace both vector blocks.

**The three pairings.** The three decompositions are exactly the three ways of splitting the four blocks into two complementary pairs: $\{A_1, B_1\}$ against $\{A_2, B_2\}$ gives $\mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}}$; $\{A_1, B_2\}$ against $\{A_2, B_1\}$ gives $\mathbb{M}_+ \oplus \mathbb{M}_-$; and $\{A_1, A_2\}$ against $\{B_1, B_2\}$ gives $\mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B})$. There are exactly three such pairings of a four-element set into two pairs, so there are exactly three decompositions, and no fourth.

**Intersections.** Two distinct subspaces meet in the blocks they share, so their intersection has dimension $0$, $1$ or $3$, and never $2$ or $4$:

$$
\mathbb{H}_{\mathbb{B}}\cap \mathbb{M}_+=A_1,\qquad
\mathbb{H}_{\mathbb{B}}\cap \mathbb{M}_-=B_1,\qquad
i\mathbb{H}_{\mathbb{B}}\cap \mathbb{M}_+=B_2,\qquad
i\mathbb{H}_{\mathbb{B}}\cap \mathbb{M}_-=A_2,
$$

and, in the same way,

$$
\mathbb{C}_{\mathbb{B}}\cap \mathbb{H}_{\mathbb{B}}=A_1,\qquad
\mathbb{C}_{\mathbb{B}}\cap i\mathbb{H}_{\mathbb{B}}=A_2,\qquad
\mathrm{Vect}(\mathbb{B})\cap \mathbb{H}_{\mathbb{B}}=B_1,\qquad
\mathrm{Vect}(\mathbb{B})\cap i\mathbb{H}_{\mathbb{B}}=B_2,
$$

$$
\mathbb{C}_{\mathbb{B}}\cap \mathbb{M}_+=A_1,\qquad
\mathbb{C}_{\mathbb{B}}\cap \mathbb{M}_-=A_2,\qquad
\mathrm{Vect}(\mathbb{B})\cap \mathbb{M}_+=B_2,\qquad
\mathrm{Vect}(\mathbb{B})\cap \mathbb{M}_-=B_1.
$$

The only pairs of distinct subspaces that meet in $\{0\}$ are the three complementary pairs of the three decompositions:

$$
\mathbb{M}_+ \cap \mathbb{M}_- = 0, \qquad \mathbb{H}_{\mathbb{B}} \cap i\mathbb{H}_{\mathbb{B}} = 0, \qquad \mathbb{C}_{\mathbb{B}} \cap \mathrm{Vect}(\mathbb{B}) = 0.
$$

Every pair that is not one of these three shares blocks, hence meets in dimension 1 or 3. Equivalently, in the decomposition $\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}}$ the intersections with $\mathbb{M}_+$ and $\mathbb{M}_-$ are

$$
\mathbb{M}_+=A_1\oplus B_2, \qquad \mathbb{M}_-=A_2\oplus B_1,
$$

which recovers the two displayed factorizations $\mathbb{M}_+ = \mathbb{R} e_0 \oplus \operatorname{span}_{\mathbb{R}}\{ie_1,ie_2,ie_3\}$ and $\mathbb{M}_- = \mathbb{R}(ie_0)\oplus \operatorname{span}_{\mathbb{R}}\{e_1,e_2,e_3\}$.

**Action of the conjugations.** The quaternion conjugation $\bar{\cdot}$ commutes with both ${}^*$ and $\dagger$, so it preserves each of the six subspaces, and it acts as $+1$ on the scalar blocks and $-1$ on the vector blocks. Multiplication by the central scalar $i$ interchanges the two summands in every decomposition:

$$
i\,\mathbb{H}_{\mathbb{B}}=i\mathbb{H}_{\mathbb{B}},\qquad
i\,(i\mathbb{H}_{\mathbb{B}})=\mathbb{H}_{\mathbb{B}},
$$

and

$$
i\,\mathbb{M}_+=\mathbb{M}_-,\qquad
i\,\mathbb{M}_-=\mathbb{M}_+,
$$

and

$$
i\,\mathbb{C}_{\mathbb{B}}=\mathbb{C}_{\mathbb{B}},\qquad
i\,\mathrm{Vect}(\mathbb{B})=\mathrm{Vect}(\mathbb{B}).
$$

The complex conjugation ${}^*$ fixes $\mathbb{H}_{\mathbb{B}}$ and negates $i\mathbb{H}_{\mathbb{B}}$, while Hermitian conjugation $\dagger$ fixes $\mathbb{M}_+$ and negates $\mathbb{M}_-$. In particular, it is multiplication by $i$, not quaternion conjugation, that swaps $\mathbb{M}_+$ and $\mathbb{M}_-$; the center and the vector subspace are each stable under it.

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

The **Hermitian form** of a biquaternion $\tilde{Q}$ is the biquaternion

$$
\tilde{Q} \tilde{Q}^\dagger = \sum_{\mu=0}^{3} |Q_\mu|^2 + \text{(vector terms)},
$$

where $\tilde{Q}^\dagger$ is the Hermitian conjugate. This is generally a **biquaternion**, not a real scalar: its scalar part is $\sum_\mu |Q_\mu|^2$, but its vector part need not vanish. For example, for $\tilde{Q} = e_0 + ie_1$, one has $\tilde{Q}^\dagger = e_0 + ie_1$ and

$$
\tilde{Q}\tilde{Q}^\dagger = (e_0 + ie_1)^2 = 2e_0 + 2ie_1,
$$

which has a nonzero vector part. The scalar part of the Hermitian form is the quantity that is non-negative:

$$
\mathrm{Sc}\!\left(\tilde{Q} \tilde{Q}^\dagger\right) = \sum_{\mu=0}^{3} |Q_\mu|^2 = \sum_{\mu=0}^{3} (q_\mu^2 + q'^2_\mu).
$$

The scalar part is non-negative, and it vanishes if and only if $\tilde{Q} = 0$. It is the natural "length squared" of $\tilde{Q}$ in the underlying real vector space of dimension 8.

The corresponding **Euclidean norm** is

$$
\|\tilde{Q}\|_E = \sqrt{\mathrm{Sc}\!\left(\tilde{Q} \tilde{Q}^\dagger\right)} = \sqrt{\sum_{\mu=0}^{3} |Q_\mu|^2}.
$$

It is a genuine norm on the real vector space $\mathbb{B} \cong \mathbb{R}^8$: positive-definite, subadditive, and homogeneous of degree one. It is **not** multiplicative with respect to the biquaternion product.

### The Inner Product

The **inner product** of two biquaternions $\tilde{P}$ and $\tilde{Q}$ is the complex scalar

$$
\langle \tilde{P}, \tilde{Q} \rangle = \sum_{\mu=0}^{3} P_\mu^* Q_\mu = \sum_{\mu=0}^{3} (p_\mu q_\mu + p'_\mu q'_\mu) + i \sum_{\mu=0}^{3} (p_\mu q'_\mu - p'_\mu q_\mu).
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
\langle \tilde{Q}, \tilde{Q} \rangle = \sum_{\mu=0}^{3} |Q_\mu|^2,
$$

which is real and non-negative, and vanishes if and only if $\tilde{Q} = 0$. This is the scalar part of the Hermitian form:

$$
\langle \tilde{Q}, \tilde{Q} \rangle = \mathrm{Sc}\!\left(\tilde{Q} \tilde{Q}^\dagger\right).
$$

### Relation Between the Three Forms

The three quadratic objects are related as follows:

- **Norm form:** $N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}} = \sum_\mu Q_\mu^2$. Complex-valued in general, can vanish for nonzero $\tilde{Q}$, multiplicative.
- **Hermitian form:** $\tilde{Q} \tilde{Q}^\dagger$, a biquaternion whose scalar part is $\sum_\mu |Q_\mu|^2$ and whose vector part does not in general vanish. Not multiplicative.
- **Inner product:** $\langle \tilde{P}, \tilde{Q} \rangle = \sum_\mu P_\mu^* Q_\mu$, a complex scalar in general, Hermitian, linear in the second argument. Its diagonal value $\langle \tilde{Q}, \tilde{Q} \rangle = \sum_\mu |Q_\mu|^2$ equals the scalar part of the Hermitian form.

The three are distinct, and each is useful in a different context. The norm form controls the multiplicative structure. The scalar part of the Hermitian form (equivalently, the diagonal value of the inner product) controls the topological structure: continuity, completeness, the Euclidean topology. The full inner product combines the Hermitian pairing on the complex coefficient space with a phase.

## Summary

The biquaternion algebra is $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$, four-dimensional over $\mathbb{C}$ and eight-dimensional over $\mathbb{R}$, with basis $e_0 = 1, e_1, e_2, e_3$, $e_k^2 = -e_0$, and central scalar imaginary $i$. It is associative, non-commutative, and not a division algebra.

It carries four natural conjugations, $\bar{\cdot}$, ${}^{*}$, ${}^{\dagger}$ and $\flat = -\dagger$, of which the first three are commuting involutions and form the Klein four-group together with the identity. The **six** distinguished real subspaces are the eigenspaces of those three involutions:

- the **center** $\mathbb{C}_{\mathbb{B}} = \{Q_0 e_0\}$, of dimension 2, fixed by $\bar{\cdot}$, a subalgebra isomorphic to $\mathbb{C}$;
- the **vector subspace** $\mathrm{Vect}(\mathbb{B}) = \{\tilde{Q} : Q_0 = 0\}$, of dimension 6, the anti-fixed space of $\bar{\cdot}$, the kernel of $\mathrm{Sc}$, and the derived subspace $[\mathbb{B}, \mathbb{B}]$;
- the **quaternion subspace** $\mathbb{H}_{\mathbb{B}}$, of dimension 4, fixed by ${}^{*}$, the subalgebra isomorphic to $\mathbb{H}$;
- the **anti-quaternion subspace** $i\mathbb{H}_{\mathbb{B}}$, of dimension 4, the anti-fixed space of ${}^{*}$, an $\mathbb{H}_{\mathbb{B}}$-module but not a subalgebra;
- the **Hermitian subspace** $\mathbb{M}_+$, of dimension 4, fixed by $\dagger$;
- the **anti-Hermitian subspace** $\mathbb{M}_-$, of dimension 4, fixed by $\flat$.

The three involutions give three direct-sum decompositions, $\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}}$, $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$ and $\mathbb{B} = \mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B})$. They are the three pairings of the four coordinate blocks $\mathbb{R}e_0$, $\mathbb{R}(ie_0)$, $\operatorname{span}_\mathbb{R}\{e_1,e_2,e_3\}$, $\operatorname{span}_\mathbb{R}\{ie_1,ie_2,ie_3\}$, so there is no fourth. Each of the four four-dimensional subspaces is one scalar block plus one vector block; two distinct subspaces meet in dimension $0$, $1$ or $3$, the dimension $0$ occurring exactly for the three complementary pairs.

On the algebra sit three quadratic objects, kept apart throughout: the **norm form** $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$, multiplicative and capable of vanishing for nonzero $\tilde{Q}$; the **Hermitian form** $\tilde{Q}\tilde{Q}^\dagger$, a biquaternion whose scalar part is $\sum_\mu |Q_\mu|^2$; and the complex **inner product** $\langle \tilde{P}, \tilde{Q}\rangle = \sum_\mu P_\mu^* Q_\mu$, whose diagonal value equals that scalar part and which defines the Euclidean norm on $\mathbb{B} \cong \mathbb{R}^8$.

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
| $\mathrm{Sc}(\tilde{Q} \tilde{Q}^\dagger) = \sum_\mu |Q_\mu|^2$ | Scalar part of the Hermitian form |
| $\langle \tilde{P}, \tilde{Q} \rangle = \sum_\mu P_\mu^* Q_\mu$ | Inner product |
| $\|\tilde{Q}\|_E = \sqrt{\mathrm{Sc}(\tilde{Q}\tilde{Q}^\dagger)}$ | Euclidean norm |
| $\mathbb{C}_{\mathbb{B}}$ | Center (complex subspace), fixed-point set of $\bar{\cdot}$; basis $e_0, ie_0$ |
| $\mathrm{Vect}(\mathbb{B})$ | Vector subspace, anti-fixed-point set of $\bar{\cdot}$; $\{\tilde{Q} : \mathrm{Sc}(\tilde{Q}) = 0\} = [\mathbb{B}, \mathbb{B}]$; basis $e_1, e_2, e_3, ie_1, ie_2, ie_3$ |
| $\mathbb{H}_{\mathbb{B}}$ | Quaternion subspace, fixed-point set of ${}^{*}$; basis $e_0, e_1, e_2, e_3$ |
| $i\mathbb{H}_{\mathbb{B}}$ | Anti-quaternion subspace, anti-fixed-point set of ${}^{*}$; basis $ie_0, ie_1, ie_2, ie_3$ |
| $\mathbb{M}_+$ | Hermitian subspace, fixed-point set of $\dagger$; basis $e_0, ie_1, ie_2, ie_3$ |
| $\mathbb{M}_-$ | Anti-Hermitian subspace, fixed-point set of $\flat$; basis $ie_0, e_1, e_2, e_3$ |
| $A_1, A_2, B_1, B_2$ | The four coordinate blocks $\mathbb{R}e_0$, $\mathbb{R}(ie_0)$, $\operatorname{span}_\mathbb{R}\{e_1,e_2,e_3\}$, $\operatorname{span}_\mathbb{R}\{ie_1,ie_2,ie_3\}$ |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original formulation.
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the first systematic treatment of biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.

