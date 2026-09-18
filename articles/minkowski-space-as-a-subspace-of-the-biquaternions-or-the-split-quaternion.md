

# Minkowski Space as a Subspace of the Biquaternions or the Split Quaternions

## Introduction

This article studies the embedding of Minkowski space $\mathbb{R}^{1,3}$ as a real subspace of two eight-dimensional real algebras: the biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ and the split quaternion algebra $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$. The goal is to describe the embeddings precisely, to compare them, and to identify the structural features that distinguish them.

The treatment is purely mathematical. The identification with physical spacetime is left for a later article; here, Minkowski space is simply the four-dimensional real vector space equipped with an indefinite quadratic form of signature $(1, 3)$ or $(3, 1)$.

Every claim is either proved or stated as a definition. No examples are given. The quaternion algebra $\mathbb{H}$ is assumed from the article on quaternion algebra. The biquaternion algebra $\mathbb{B}$ is assumed from the basic algebra article, together with its four conjugations and its four fixed-point subspaces. The split quaternion algebra $\mathbb{H}_{\mathbb{D}}$ is assumed from the basic algebra article, together with its four conjugations and its four fixed-point subspaces.

Throughout, the quaternion basis is written $e_0 = 1, e_1, e_2, e_3$. In the biquaternion algebra, the scalar imaginary is $i$, with $i^2 = -1$, commuting with the quaternion units. In the split quaternion algebra, the split complex unit is $j$, with $j^2 = +1$, commuting with the quaternion units.

## Minkowski Space

### Definition

**Minkowski space** $\mathbb{R}^{1,3}$ is the four-dimensional real vector space $\mathbb{R}^4$ equipped with the indefinite quadratic form

$$
\eta(x, x) = x_0^2 - x_1^2 - x_2^2 - x_3^2.
$$

The form has signature $(1, 3)$ in the convention where one direction is timelike and three are spacelike. With the opposite sign convention, the form is

$$
\eta(x, x) = -x_0^2 + x_1^2 + x_2^2 + x_3^2,
$$

which has signature $(3, 1)$. Both conventions are used in the literature, and the choice is a matter of sign.

### The Light Cone

The **light cone** of Minkowski space is the set of vectors $x$ with $\eta(x, x) = 0$:

$$
x_0^2 = x_1^2 + x_2^2 + x_3^2.
$$

The light cone is a three-dimensional double cone in $\mathbb{R}^4$. Its nonzero elements are **null vectors**.

### The Lorentz Group

The **Lorentz group** is the group of linear transformations of $\mathbb{R}^{1,3}$ that preserve the quadratic form $\eta$:

$$
O(1, 3) = \{ \Lambda \in \mathrm{GL}(4, \mathbb{R}) : \eta(\Lambda x, \Lambda x) = \eta(x, x) \text{ for all } x \}.
$$

The **proper orthochronous Lorentz group** $SO^+(1, 3)$ is the connected component of the identity.

## Minkowski Space in the Biquaternion Algebra

### The Anti-Hermitian Subspace $\mathbb{M}_-$

In the biquaternion algebra $\mathbb{B}$, the **anti-Hermitian subspace** $\mathbb{M}_-$ is the fixed-point set of the anti-Hermitian conjugation $\flat = -\bar{\cdot}^*$. An element of $\mathbb{M}_-$ has the form

$$
\tilde{Q} = i q'_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3, \qquad q'_0, q_1, q_2, q_3 \in \mathbb{R}.
$$

This is a four-dimensional real subspace of $\mathbb{B}$. The norm form restricts to

$$
N(\tilde{Q}) = -(q'_0)^2 + q_1^2 + q_2^2 + q_3^2,
$$

which is the Minkowski quadratic form of signature $(3, 1)$. The identification is

$$
(x_0, x_1, x_2, x_3) \in \mathbb{R}^{1,3} \longleftrightarrow i x_0 e_0 + x_1 e_1 + x_2 e_2 + x_3 e_3 \in \mathbb{M}_- \subset \mathbb{B}.
$$

The timelike direction is the imaginary scalar part $i e_0$, and the spacelike directions are the real vector part $e_1, e_2, e_3$.

### The Hermitian Subspace $\mathbb{M}_+$

In the biquaternion algebra $\mathbb{B}$, the **Hermitian subspace** $\mathbb{M}_+$ is the fixed-point set of the Hermitian conjugation $\dagger = \bar{\cdot}^*$. An element of $\mathbb{M}_+$ has the form

$$
\tilde{Q} = q_0 e_0 + i q'_1 e_1 + i q'_2 e_2 + i q'_3 e_3, \qquad q_0, q'_1, q'_2, q'_3 \in \mathbb{R}.
$$

This is also a four-dimensional real subspace of $\mathbb{B}$. The norm form restricts to

$$
N(\tilde{Q}) = q_0^2 - (q'_1)^2 - (q'_2)^2 - (q'_3)^2,
$$

which is the Minkowski quadratic form of signature $(1, 3)$. The identification is

$$
(x_0, x_1, x_2, x_3) \in \mathbb{R}^{1,3} \longleftrightarrow x_0 e_0 + i x_1 e_1 + i x_2 e_2 + i x_3 e_3 \in \mathbb{M}_+ \subset \mathbb{B}.
$$

The timelike direction is the real scalar part $e_0$, and the spacelike directions are the imaginary vector parts $i e_1, i e_2, i e_3$.

### The Two Embeddings Are Mirror Images

The two subspaces $\mathbb{M}_+$ and $\mathbb{M}_-$ are related by the quaternion conjugation:

$$
\overline{\mathbb{M}_+} = \mathbb{M}_-, \qquad \overline{\mathbb{M}_-} = \mathbb{M}_+.
$$

So they are mirror images of each other. The two embeddings of Minkowski space in $\mathbb{B}$ are therefore equivalent up to the quaternion conjugation, and the choice between them is a convention.

### The Light Cone

In both cases, the light cone of Minkowski space is the intersection of the subspace with the zero divisor set of $\mathbb{B}$:

$$
\mathbb{M}_- \cap \mathcal{Z}_\mathbb{B} = \text{light cone of signature } (3, 1),
$$

$$
\mathbb{M}_+ \cap \mathcal{Z}_\mathbb{B} = \text{light cone of signature } (1, 3).
$$

The nonzero elements of the light cone are zero divisors of $\mathbb{B}$. This is a general feature: the light cone is the set of spacetime points that are zero divisors in the algebra.

## Minkowski Space in the Split Quaternion Algebra

### The Hermitian Subspace $\mathbb{M}_+$

In the split quaternion algebra $\mathbb{H}_{\mathbb{D}}$, the **Hermitian subspace** $\mathbb{M}_+$ is the fixed-point set of the Hermitian conjugation $\dagger = \bar{\cdot}^*$. An element of $\mathbb{M}_+$ has the form

$$
\tilde{Q} = q_0 e_0 + j q'_1 e_1 + j q'_2 e_2 + j q'_3 e_3, \qquad q_0, q'_1, q'_2, q'_3 \in \mathbb{R}.
$$

This is a four-dimensional real subspace of $\mathbb{H}_{\mathbb{D}}$. The norm form restricts to

$$
N(\tilde{Q}) = q_0^2 - (q'_1)^2 - (q'_2)^2 - (q'_3)^2,
$$

which is the Minkowski quadratic form of signature $(1, 3)$. The identification is

$$
(x_0, x_1, x_2, x_3) \in \mathbb{R}^{1,3} \longleftrightarrow x_0 e_0 + j x_1 e_1 + j x_2 e_2 + j x_3 e_3 \in \mathbb{M}_+ \subset \mathbb{H}_{\mathbb{D}}.
$$

The timelike direction is the real scalar part $e_0$, and the spacelike directions are the split-imaginary vector parts $j e_1, j e_2, j e_3$.

### The Anti-Hermitian Subspace $\mathbb{M}_-$

In the split quaternion algebra $\mathbb{H}_{\mathbb{D}}$, the **anti-Hermitian subspace** $\mathbb{M}_-$ is the fixed-point set of the anti-Hermitian conjugation $\flat = -\bar{\cdot}^*$. An element of $\mathbb{M}_-$ has the form

$$
\tilde{Q} = j q'_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3, \qquad q'_0, q_1, q_2, q_3 \in \mathbb{R}.
$$

This is also a four-dimensional real subspace. The norm form restricts to

$$
N(\tilde{Q}) = -(q'_0)^2 + q_1^2 + q_2^2 + q_3^2,
$$

which is the Minkowski quadratic form of signature $(3, 1)$. The identification is

$$
(x_0, x_1, x_2, x_3) \in \mathbb{R}^{1,3} \longleftrightarrow j x_0 e_0 + x_1 e_1 + x_2 e_2 + x_3 e_3 \in \mathbb{M}_- \subset \mathbb{H}_{\mathbb{D}}.
$$

The timelike direction is the split-imaginary scalar part $j e_0$, and the spacelike directions are the real vector part $e_1, e_2, e_3$.

### The Two Embeddings Are Mirror Images

The two subspaces $\mathbb{M}_+$ and $\mathbb{M}_-$ in $\mathbb{H}_{\mathbb{D}}$ are related by the quaternion conjugation:

$$
\overline{\mathbb{M}_+} = \mathbb{M}_-, \qquad \overline{\mathbb{M}_-} = \mathbb{M}_+.
$$

So they are mirror images of each other, exactly as in the biquaternion case. The two embeddings of Minkowski space in $\mathbb{H}_{\mathbb{D}}$ are equivalent up to the quaternion conjugation, and the choice between them is a convention.

### The Light Cone

In both cases, the light cone of Minkowski space is the intersection of the subspace with the zero divisor set of $\mathbb{H}_{\mathbb{D}}$:

$$
\mathbb{M}_+ \cap \mathcal{Z}_{\mathbb{H}_{\mathbb{D}}} = \text{light cone of signature } (1, 3),
$$

$$
\mathbb{M}_- \cap \mathcal{Z}_{\mathbb{H}_{\mathbb{D}}} = \text{light cone of signature } (3, 1).
$$

The nonzero elements of the light cone are zero divisors of $\mathbb{H}_{\mathbb{D}}$.

## Comparison of the Two Algebras

The two algebras $\mathbb{B}$ and $\mathbb{H}_{\mathbb{D}}$ are both eight-dimensional real algebras, and both contain copies of Minkowski space as four-dimensional real subspaces. But the embeddings are different in character, and the differences are structural.

### The Extra Unit

The fundamental difference is the sign of the square of the extra unit:

- In $\mathbb{B}$, the extra unit is $i$ with $i^2 = -1$.
- In $\mathbb{H}_{\mathbb{D}}$, the extra unit is $j$ with $j^2 = +1$.

This sign change has consequences for the structure of the algebra and for the embeddings of Minkowski space.

### The Timelike Direction

In $\mathbb{B}$, the timelike direction of $\mathbb{M}_-$ is the **imaginary** scalar part $i e_0$, and the timelike direction of $\mathbb{M}_+$ is the **real** scalar part $e_0$.

In $\mathbb{H}_{\mathbb{D}}$, the timelike direction of $\mathbb{M}_+$ is the **real** scalar part $e_0$, and the timelike direction of $\mathbb{M}_-$ is the **split-imaginary** scalar part $j e_0$.

So the timelike direction is imaginary in one embedding and real in the other. The choice between the embeddings is a choice of which direction is timelike.

### The Zero Divisor Structure

The zero divisor sets of the two algebras are different:

- In $\mathbb{B}$, the zero divisor set is a **seven-dimensional complex cone**.
- In $\mathbb{H}_{\mathbb{D}}$, the zero divisor set is the **union of two four-dimensional linear subspaces** $Z_+$ and $Z_-$.

The intersection of the zero divisor set with the embedded Minkowski space is the light cone in both cases, but the structure of the intersection is different. In $\mathbb{B}$, the intersection is a three-dimensional cone, and it is a subset of the seven-dimensional complex cone. In $\mathbb{H}_{\mathbb{D}}$, the intersection is a three-dimensional cone, and it is a subset of the union of the two four-dimensional linear subspaces.

### The Idempotent Decomposition

The split quaternion algebra has the **idempotent decomposition** $\mathbb{H}_{\mathbb{D}} = \mathbb{H} e_+ \oplus \mathbb{H} e_-$, where $e_\pm = \tfrac{1}{2}(1 \pm j)$. The biquaternion algebra does not have a comparable idempotent decomposition, because the scalar imaginary $i$ is not an idempotent.

The idempotent decomposition is what makes the split quaternion algebra semisimple, and it is what makes the embeddings of Minkowski space in $\mathbb{H}_{\mathbb{D}}$ decomposable into two quaternion components. Specifically, an element of $\mathbb{M}_+$ or $\mathbb{M}_-$ decomposes as a pair of quaternions satisfying a conjugation condition, as described in the article on split quaternion analysis on subspaces.

### The Quaternion Decomposition

The biquaternion algebra has the **quaternion decomposition** $\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i \mathbb{H}_{\mathbb{B}}$, where $\mathbb{H}_{\mathbb{B}}$ is the quaternion subspace. This is the decomposition into the real and imaginary parts with respect to the scalar imaginary $i$.

The quaternion decomposition is what makes the biquaternion algebra a complexification of the quaternion algebra. An element of $\mathbb{M}_-$ decomposes as a pure real quaternion plus an imaginary scalar, as described in the article on biquaternion analysis on subspaces.

### The Algebra Structure

The two algebras have different algebraic structures:

- $\mathbb{B}$ is **simple**: it is isomorphic to $M_2(\mathbb{C})$, and it has no nontrivial two-sided ideals.
- $\mathbb{H}_{\mathbb{D}}$ is **semisimple but not simple**: it is isomorphic to $\mathbb{H} \oplus \mathbb{H}$, and it has two nontrivial two-sided ideals $Z_+$ and $Z_-$.

This difference is reflected in the zero divisor structure and in the idempotent decomposition. In $\mathbb{B}$, the zero divisors form a single cone; in $\mathbb{H}_{\mathbb{D}}$, they form the union of two linear subspaces, corresponding to the two ideals.

## Which Embedding Is the Standard One?

Both embeddings are used in the literature, and the choice depends on the context.

**Biquaternion embedding.** The embedding of Minkowski space in the anti-Hermitian subspace $\mathbb{M}_-$ of the biquaternion algebra is the standard one in the **complexified-spacetime program**. In this program, the biquaternion algebra is the complexification of the quaternion algebra, and the anti-Hermitian subspace is the real spacetime. The timelike direction is the imaginary scalar part, and the spacelike directions are the real vector part. This embedding is used in the study of the Dirac equation, in the theory of twistors, and in the algebraic formulation of special relativity.

**Split quaternion embedding.** The embedding of Minkowski space in the Hermitian subspace $\mathbb{M}_+$ or the anti-Hermitian subspace $\mathbb{M}_-$ of the split quaternion algebra is used in the study of the **Lorentz group** and in **twistor theory**. The split quaternion algebra is the split form of the biquaternion algebra, and its indefinite subspaces are the natural home for the Lorentzian structure. The timelike direction is the real scalar part in $\mathbb{M}_+$ and the split-imaginary scalar part in $\mathbb{M}_-$.

## Comparison Table

The following table summarizes the embeddings of Minkowski space in the two algebras.

| Property | $\mathbb{B}$ | $\mathbb{H}_{\mathbb{D}}$ |
|---|---|---|
| Extra unit | $i$, $i^2 = -1$ | $j$, $j^2 = +1$ |
| Spacetime subspace | $\mathbb{M}_-$ or $\mathbb{M}_+$ | $\mathbb{M}_+$ or $\mathbb{M}_-$ |
| Timelike direction in $\mathbb{M}_-$ | $i e_0$ | $j e_0$ |
| Timelike direction in $\mathbb{M}_+$ | $e_0$ | $e_0$ |
| Spacelike directions in $\mathbb{M}_-$ | $e_1, e_2, e_3$ | $e_1, e_2, e_3$ |
| Spacelike directions in $\mathbb{M}_+$ | $i e_1, i e_2, i e_3$ | $j e_1, j e_2, j e_3$ |
| Norm form signature | $(3, 1)$ or $(1, 3)$ | $(1, 3)$ or $(3, 1)$ |
| Zero divisor set | Seven-dimensional cone | Union of two four-dimensional subspaces |
| Light cone | Three-dimensional cone | Three-dimensional cone |
| Algebra structure | Simple ($M_2(\mathbb{C})$) | Semisimple ($\mathbb{H} \oplus \mathbb{H}$) |
| Primary decomposition | Quaternion decomposition | Idempotent decomposition |

## The Role of the Light Cone

In both algebras, the light cone of Minkowski space is the intersection of the embedded spacetime with the zero divisor set. This is a general feature, and it is the reason the light cone plays a distinguished role in the algebraic structure.

**In $\mathbb{B}$.** The light cone is the set of nonzero elements $\tilde{Q} \in \mathbb{M}_-$ with $N(\tilde{Q}) = 0$. These are the zero divisors of $\mathbb{B}$ that lie in the spacetime subspace. The zero divisors of $\mathbb{B}$ outside the light cone are the non-pure zero divisors, which are complex multiples of idempotents.

**In $\mathbb{H}_{\mathbb{D}}$.** The light cone is the set of nonzero elements $\tilde{Q} \in \mathbb{M}_+$ or $\mathbb{M}_-$ with $N(\tilde{Q}) = 0$. These are the zero divisors of $\mathbb{H}_{\mathbb{D}}$ that lie in the spacetime subspace. The zero divisors of $\mathbb{H}_{\mathbb{D}}$ outside the light cone are the elements with a vanishing idempotent component, which form the union of the two linear subspaces $Z_+$ and $Z_-$.

So the light cone is the intersection of the spacetime subspace with the zero divisor set in both algebras, and the structure of the zero divisor set outside the light cone is different in the two cases.

## The Lorentz Group

The Lorentz group acts naturally on the spacetime subspace in both algebras. The action is by conjugation by the unit elements of the algebra.

**In $\mathbb{B}$.** The unit elements of $\mathbb{B}$ that preserve the spacetime subspace $\mathbb{M}_-$ form a group isomorphic to the double cover of the Lorentz group. The action is by conjugation:

$$
\tilde{Q} \mapsto \tilde{U} \tilde{Q} \tilde{U}^{-1}, \qquad \tilde{U} \in \mathbb{B}, \quad |\tilde{U}| = 1.
$$

The subgroup that preserves $\mathbb{M}_-$ is the group of unit biquaternions whose conjugate acts on $\mathbb{M}_-$ as a Lorentz transformation.

**In $\mathbb{H}_{\mathbb{D}}$.** The unit elements of $\mathbb{H}_{\mathbb{D}}$ that preserve the spacetime subspace $\mathbb{M}_+$ or $\mathbb{M}_-$ form a group isomorphic to the double cover of the Lorentz group. The action is by conjugation, as in the biquaternion case.

So the Lorentz group is realized as a group of unit elements acting by conjugation on the spacetime subspace in both algebras. The realization is the same in character, but the specific group elements are different because the algebras are different.

## Summary

Minkowski space $\mathbb{R}^{1,3}$ can be embedded as a four-dimensional real subspace of both the biquaternion algebra $\mathbb{B}$ and the split quaternion algebra $\mathbb{H}_{\mathbb{D}}$:

- **In $\mathbb{B}$:** Minkowski space is either the anti-Hermitian subspace $\mathbb{M}_-$ (timelike direction $i e_0$, spacelike directions $e_1, e_2, e_3$) or the Hermitian subspace $\mathbb{M}_+$ (timelike direction $e_0$, spacelike directions $i e_1, i e_2, i e_3$). The two are mirror images under quaternion conjugation. The standard choice for physics is $\mathbb{M}_-$.
- **In $\mathbb{H}_{\mathbb{D}}$:** Minkowski space is either the Hermitian subspace $\mathbb{M}_+$ (timelike direction $e_0$, spacelike directions $j e_1, j e_2, j e_3$) or the anti-Hermitian subspace $\mathbb{M}_-$ (timelike direction $j e_0$, spacelike directions $e_1, e_2, e_3$). The two are mirror images under quaternion conjugation.

In both algebras, the norm form restricts to the Minkowski quadratic form on the subspace, and the light cone is the intersection of the subspace with the zero divisor set. The Lorentz group is realized as the group of unit elements acting by conjugation.

The two algebras differ in their structure: $\mathbb{B}$ is simple, and its zero divisor set is a seven-dimensional cone; $\mathbb{H}_{\mathbb{D}}$ is semisimple, and its zero divisor set is the union of two four-dimensional linear subspaces. This difference is reflected in the embeddings and in the structure of the spacetime subspace.

The choice between the two algebras and between the two subspaces within each algebra is a matter of convention and of the algebraic structure that one wishes to emphasize. The biquaternion embedding is natural when the complexification of the quaternion algebra is the primary structure; the split quaternion embedding is natural when the indefinite form and the idempotent decomposition are the primary structure.

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original formulation.
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the first systematic treatment of biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra perspective.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the algebraic structure of biquaternions and split quaternions.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the classification of real algebras.
- F. Brackx, R. Delanghe, and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the general Clifford analysis with split signature.

