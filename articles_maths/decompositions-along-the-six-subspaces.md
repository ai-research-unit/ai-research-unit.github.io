# __Decompositions Along the Six Subspaces__

## Introduction

Each conjugation of $\mathbb{B}$ is an involution, so each divides the real space into the elements it fixes and the elements it reverses, and each division is a direct-sum decomposition of that space. Three of the four conjugations give decompositions distinct in the sense that no one reproduces another, and each of the three pairs two of the six distinguished real subspaces of $\mathbb{B}$: the halves have real dimensions $2+6$, $4+4$ and $4+4$. The article takes them in that order, from the one with halves of unequal dimension to the two symmetric halves.

This article establishes the three decompositions, gives the two projection formulas for each — the halved sum and the halved difference against the conjugation — and closes with the reason there are exactly three and not four. The decompositions are vector-space decompositions: they are read off the conjugations, and no product is needed.

The six subspaces, one to a section, are *Introduction to the Six Subspaces*; the four conjugations as formulas, the group they form and the lattice of their fixed spaces are *The Group of Involutions* and *Biquaternion Involution Lattice*. The elements, the basis, the coordinate systems and the fact that the conjugations are linear and antilinear are assumed from *Biquaternions as a Vector Space over $\mathbb{C}$*. The coordinate blocks, the fifteen pairwise intersections, the sums and the sign patterns of the conjugations on the six subspaces are *Comparison of the Six Subspaces*.

## The Center and Vector Decomposition

The quaternion conjugation ${}^{\natural}$ is one of the three commuting involutions. Its eigenspaces are the center $\mathbb{C}_{\mathbb{B}}$ (eigenvalue $+1$) and the vector subspace $\mathrm{Vect}(\mathbb{B})$ (eigenvalue $-1$), of real dimensions 2 and 6. Every biquaternion therefore decomposes uniquely as a scalar plus a pure vector part:

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

## The Quaternion Decomposition

The complex conjugation $\bar{\cdot}$ is an involution, and the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ and the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$ are its eigenspaces: $\mathbb{H}_{\mathbb{B}}$ is the eigenspace of eigenvalue $+1$ and $i\mathbb{H}_{\mathbb{B}}$ the eigenspace of eigenvalue $-1$. Both have real dimension 4, and they are independent, so $\mathbb{B}$ splits as a direct sum of the two.

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
\bar{\tilde{Q}_i} = \overline{\left(\frac{1}{2i}(\tilde{Q} - \bar{\tilde{Q}})\right)} = \frac{-1}{2i}\left(\bar{\tilde{Q}} - \tilde{Q}\right) = \frac{1}{2i}\left(\tilde{Q} - \bar{\tilde{Q}}\right) = \tilde{Q}_i,
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

Indeed, $\tilde{Q}_+$ is fixed by Hermitian conjugation, so it lies in $\mathbb{M}_+$, and $\tilde{Q}_-$ satisfies $\tilde{Q}_-^{*} = -\tilde{Q}_-$, so it lies in $\mathbb{M}_-$. The sum is $\tilde{Q}_+ + \tilde{Q}_- = \tilde{Q}$.

This gives the direct sum decomposition

$$
\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-,
$$

where $\mathbb{M}_+$ is the Hermitian subspace and $\mathbb{M}_-$ is the anti-Hermitian subspace. Both are real vector spaces of dimension 4, and their direct sum is the full algebra $\mathbb{B}$ of real dimension 8.

The decomposition is the algebraic analogue of writing a complex number as the sum of its real and imaginary parts. Here, however, both components are biquaternions, and the two subspaces $\mathbb{M}_+$ and $\mathbb{M}_-$ are not subalgebras of $\mathbb{B}$; the decomposition is a vector-space decomposition, not an algebra decomposition.

## Relation Between the Three Decompositions

The three decompositions

$$
\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i \mathbb{H}_{\mathbb{B}}, \qquad \mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-, \qquad \mathbb{B} = \mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B})
$$

are the eigenspace decompositions of the three pairwise commuting involutions $\bar{\cdot}$, ${}^{*}$ and ${}^{\natural}$, and they are the only decompositions of this kind: $\flat = -{}^{*}$ reproduces the eigenspaces of ${}^{*}$ with the signs exchanged and gives nothing new, so there are exactly three decompositions and six subspaces.

The three are the three ways of splitting the four coordinate blocks into two complementary pairs, they are the only pairs of distinct subspaces whose intersection is trivial, and they are the only pairs that sum to the whole algebra. The blocks, the pairings, the full table of the fifteen pairwise intersections, the sums and the action of the four conjugations on the six subspaces are in *Comparison of the Six Subspaces*.

## Summary

The six distinguished real subspaces of $\mathbb{B}$ come in three pairs, one pair to each of the three commuting conjugations, and each pair sums directly to the whole space:

$$
\mathbb{B} = \mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B}), \qquad \mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}}, \qquad \mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-,
$$

of real dimensions $2+6$, $4+4$ and $4+4$. In each case the two halves are the fixed and the anti-fixed space of the conjugation, and the components of an element are the halved sum and the halved difference against it.

The first is the centre–vector decomposition, $\tilde{Q} = \tilde{Q}_{\mathrm{c}} + \tilde{Q}_{\mathrm{v}}$, the splitting into scalar and pure vector parts, the only one whose halves have unequal dimension. The second is the quaternion decomposition, $\tilde{Q} = \tilde{Q}_r + i\tilde{Q}_i$ with both $\tilde{Q}_r$ and $\tilde{Q}_i$ real quaternions, the real and imaginary parts of the complexification. The third is the Hermitian decomposition, $\tilde{Q} = \tilde{Q}_+ + \tilde{Q}_-$, the algebraic analogue of real and imaginary parts of a complex number.

There are exactly three. The reversal $\flat = -{}^{*}$ reproduces the fixed and anti-fixed spaces of ${}^{*}$ with the signs exchanged, so it adds no fourth decomposition; the three conjugations are the three ways of pairing the four coordinate blocks, which is the argument of *Comparison of the Six Subspaces*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde{Q}$ | General biquaternion, $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ |
| $\bar{\cdot}$ | Complex conjugation; $\bar{\tilde{Q}} = \bar{Q_0} e_0 + \mathbf{Q}^*$ |
| ${}^{*}$ | Hermitian conjugation; $\tilde{Q}^{*} = \bar{Q_0} e_0 - \mathbf{Q}^*$ |
| ${}^{\natural}$ | Quaternion conjugation; $\tilde{Q}^{\natural} = Q_0 e_0 - \mathbf{Q}$ |
| $\flat$ | Reversal, $\flat = -{}^{*}$, the conjugation that gives no new decomposition |
| $\mathbb{C}_{\mathbb{B}}$ | Centre, fixed space of ${}^{\natural}$; basis $e_0, ie_0$, dimension $2$ |
| $\mathrm{Vect}(\mathbb{B})$ | Vector subspace, anti-fixed space of ${}^{\natural}$; basis $e_1, e_2, e_3, ie_1, ie_2, ie_3$, dimension $6$ |
| $\mathbb{H}_{\mathbb{B}}$ | Quaternion subspace, fixed space of $\bar{\cdot}$; basis $e_0, e_1, e_2, e_3$, dimension $4$ |
| $i\mathbb{H}_{\mathbb{B}}$ | Anti-quaternion subspace, anti-fixed space of $\bar{\cdot}$; basis $ie_0, ie_1, ie_2, ie_3$, dimension $4$ |
| $\mathbb{M}_+$ | Hermitian subspace, fixed space of ${}^{*}$; basis $e_0, ie_1, ie_2, ie_3$, dimension $4$ |
| $\mathbb{M}_-$ | Anti-Hermitian subspace, anti-fixed space of ${}^{*}$; basis $ie_0, e_1, e_2, e_3$, dimension $4$ |
| $\tilde{Q}_{\mathrm{c}}, \tilde{Q}_{\mathrm{v}}$ | Scalar and vector components, in $\mathbb{C}_{\mathbb{B}}$ and $\mathrm{Vect}(\mathbb{B})$ |
| $\tilde{Q}_r, \tilde{Q}_i$ | Quaternion and imaginary-quaternion components, both in $\mathbb{H}_{\mathbb{B}}$ |
| $\tilde{Q}_+, \tilde{Q}_-$ | Hermitian and anti-Hermitian components, in $\mathbb{M}_+$ and $\mathbb{M}_-$ |
| $\mathbb{B} = \mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B})$ | Centre–vector decomposition, from ${}^{\natural}$ |
| $\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}}$ | Quaternion decomposition, from $\bar{\cdot}$ |
| $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$ | Hermitian decomposition, from ${}^{*}$ |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original formulation.
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the first systematic treatment of biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- Nicolas Bourbaki, *Algebra I* (Springer, 1998), for the eigenspace decomposition of a vector space under an involution.
