# __The Six Subspaces under the Antisymmetric Quaternionic Sesqualgebra of Biquaternions__

## Introduction

The block $\tilde P\diamond\tilde Q=\mathbf{P}\times\overline{\mathbf{Q}}$ of *Introduction to the Antisymmetric Quaternionic Sesqualgebra of Biquaternions* depends on its two arguments through their vector parts alone, with the vector part of the second argument conjugated. This article reads the block on the six distinguished real subspaces of *Introduction to the Six Subspaces* — the centre $\mathbb{C}_{\mathbb{B}}$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$, the Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$ — and answers three questions for each: whether the block is stable on it, that is whether the value of two of its elements stays in it; what the diagonal of the block does on it; and which of its elements give the value zero. The block kills the centre in both slots, so the centre is the one subspace on which the product vanishes identically, and the values of the block always lie in the vector subspace, so closure of any other subspace requires its intersection with the vector subspace to receive those values; that requirement separates the six into the four on which the block is stable and the two on which it is not.

The six subspaces and their bases are *Introduction to the Six Subspaces*; the same six are read by the other pairings in *The Six Subspaces under the General Quaternionic Sesqualgebra of Biquaternions* and its companions; the form that the block pairs with is *The Sesquilinear Pairing of the Antisymmetric Quaternionic Sesqualgebra*; and the product the block splits is *Introduction to the General Quaternionic Sesqualgebra of Biquaternions*. This article owns the reading of the block on the six themselves.

**Conventions.** As in the block: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_1e_2=e_3$, and a generic element $\tilde Q=Q_0e_0+\mathbf{Q}$, with $Q_k=q_k+iq'_k$ real and imaginary parts. The six subspaces are real subspaces of the complex space; the word *stable* means that the value of two elements of the subspace lies in it, in the real sense, and not that the subspace is a complex subspace. The centre and the vector subspace are the only two of the six that are complex subspaces.

## The Vanishing on the Centre and the Image

**Proposition.** The block annihilates the centre in both slots: for every central element $\tilde A=Ae_0$,

$$
\tilde A\diamond\tilde Q=0,\qquad \tilde Q\diamond\tilde A=0 .
$$

*Proof.* A central element has $\mathbf{A}=0$, so the value is the cross product of a zero vector; the value is zero from either slot. Verified on the centre.

**Proposition.** The image of the block on every subspace is contained in the vector subspace, and on the vector subspace the block is stable with image the whole vector subspace.

*Proof.* Every value of the block is pure vector, so the image of any subspace lies in $\mathrm{Vect}(\mathbb{B})$. On $\mathrm{Vect}(\mathbb{B})$ the vector parts are the elements themselves, so the value $\mathbf{Q}\times\overline{\mathbf{Q}'}$ of two complex vectors is again a complex vector, and the values fill the three complex dimensions. Verified on the six subspaces.

## The Six Subspaces

### The Centre $\mathbb{C}_{\mathbb{B}}$

The centre is the complex line of the multiples of $e_0$. The block vanishes on it identically, so the centre is **stable** and is in fact contained in the annihilator of the block; its diagonal is zero, and every element of the centre gives the value zero with every element of the space on either side. The centre is the only subspace of the six on which the block vanishes identically in both arguments.

### The Vector Subspace $\mathrm{Vect}(\mathbb{B})$

The vector subspace is the complex span of $e_1,e_2,e_3$, with real basis $e_k,ie_k$. The block is **stable** on it and its image is the whole subspace: for two complex vectors $\mathbf{Q},\mathbf{Q}'$ the value $\mathbf{Q}\times\overline{\mathbf{Q}'}$ is a complex vector, and the cross product with a fixed real direction already fills a complex plane. The diagonal is the conjugate cross product $\mathbf{Q}\times\overline{\mathbf{Q}}$, which is **not identically zero** on the subspace: it vanishes exactly when $\mathbf{Q}$ is a complex multiple of a real vector, that is on the union of the complex lines through the real directions, a quadric cone of real dimension $4$ and a proper subset; the witness $e_1+ie_2$ lies in the vector subspace and has diagonal $-2ie_3$. The vector subspace is the one stable subspace on which the diagonal does not vanish identically.

### The Quaternion Subspace $\mathbb{H}_{\mathbb{B}}$

The quaternion subspace is the real span of $e_0,e_1,e_2,e_3$, of real coefficients. The block is **stable** on it: two real vector parts have a real cross product, which lies in $\mathbb{H}_{\mathbb{B}}\cap\mathrm{Vect}(\mathbb{B})$, the real vector directions. On this subspace the block is the ordinary cross product of the real vector parts,

$$
\tilde P\diamond\tilde Q=\mathbf{P}\times\mathbf{Q}=\mathrm{APA}(\tilde P,\tilde Q)\qquad(\tilde P,\tilde Q\in\mathbb{H}_{\mathbb{B}}),
$$

the real coincidence of the block, and its image is the three real dimensions of the real vector directions. The diagonal is **identically zero**, a real vector being its own conjugate.

### The Anti-Quaternion Subspace $i\mathbb{H}_{\mathbb{B}}$

The anti-quaternion subspace is the real span of $ie_0,ie_1,ie_2,ie_3$, of imaginary coefficients. The block is **not stable** on it: for two imaginary elements $\tilde P=i\mathbf{a}$, $\tilde Q=i\mathbf{b}$ with $\mathbf{a},\mathbf{b}$ real, the value is

$$
(i\mathbf{a})\diamond(i\mathbf{b})=i\mathbf{a}\times\overline{i\mathbf{b}}=i\mathbf{a}\times(-i\mathbf{b})=\mathbf{a}\times\mathbf{b},
$$

a **real** vector, which lies in $\mathbb{H}_{\mathbb{B}}\cap\mathrm{Vect}(\mathbb{B})$ and not in $i\mathbb{H}_{\mathbb{B}}$. The value of two elements of the subspace therefore leaves the subspace, and the intersection of the subspace with the vector subspace is the imaginary vector directions, which the block never reaches from the subspace. The diagonal is **identically zero**.

### The Hermitian Subspace $\mathbb{M}_+$

The Hermitian subspace is the real span of $e_0,ie_1,ie_2,ie_3$, with real scalar coordinate and imaginary vector coordinates. The block is **not stable** on it: for two elements $i\mathbf{a},i\mathbf{b}$ with real vector parts, the same computation as for the anti-quaternion subspace gives the real vector $\mathbf{a}\times\mathbf{b}$, which is not Hermitian, the vector part of a Hermitian element being imaginary. Its intersection with the vector subspace is the imaginary vector directions, which the block does not reach. The diagonal is **identically zero**, an imaginary vector being a complex multiple of a real vector.

### The Anti-Hermitian Subspace $\mathbb{M}_-$

The anti-Hermitian subspace is the real span of $ie_0,e_1,e_2,e_3$, with imaginary scalar coordinate and real vector coordinates. The block is **stable** on it: for two elements with real vector parts the value is the real vector $\mathbf{a}\times\mathbf{b}$, which is anti-Hermitian. On this subspace the block is again the ordinary cross product of the real vector parts, with the scalar coordinates ignored, and its image is the three real dimensions of the real vector directions. The diagonal is **identically zero**, a real vector being its own conjugate.

**Remark (the four stable subspaces and the two failing ones).** Closure holds on the centre, on the vector subspace, on the quaternion subspace and on the anti-Hermitian subspace, and it fails on the anti-quaternion subspace and on the Hermitian subspace. The reason is uniform: the block always lands in the vector subspace, so a subspace is stable exactly when the values that reach it lie in its intersection with the vector subspace. The quaternion and the anti-Hermitian subspaces contain the real vector directions and stay stable; the anti-quaternion and the Hermitian subspaces contain only the imaginary vector directions, and the value of two of their elements is a real vector, so they fail. The centre is stable because its value is zero. The menu entry of the block records the vanishing on the centre and the pure-vector image; the failure of closure is not shared by the quaternion and the anti-Hermitian subspaces, and the reading here corrects the impression that the block fails closure on every subspace other than the centre and the vector subspace.

## The Table of the Six

| Subspace | Natural real basis | Value of the block on two of its elements | Stable | Diagonal |
|---|---|---|---|---|
| Centre $\mathbb{C}_{\mathbb{B}}$ | $e_0,\,ie_0$ | $0$ | yes | $0$ |
| Vector $\mathrm{Vect}(\mathbb{B})$ | $e_1,e_2,e_3,\,ie_1,ie_2,ie_3$ | a complex vector | yes | not identically zero |
| Quaternion $\mathbb{H}_{\mathbb{B}}$ | $e_0,e_1,e_2,e_3$ | a real vector | yes | $0$ |
| Anti-quaternion $i\mathbb{H}_{\mathbb{B}}$ | $ie_0,ie_1,ie_2,ie_3$ | a real vector | no | $0$ |
| Hermitian $\mathbb{M}_+$ | $e_0,ie_1,ie_2,ie_3$ | a real vector | no | $0$ |
| Anti-Hermitian $\mathbb{M}_-$ | $ie_0,e_1,e_2,e_3$ | a real vector | yes | $0$ |

**Remark (the four subspaces with a vanishing diagonal).** The diagonal of the block is identically zero on the centre and on the four four-dimensional subspaces, and it is not identically zero on the vector subspace alone. The four four-dimensional subspaces have their vector part real or purely imaginary, and a real or purely imaginary vector is a complex multiple of a real vector, so the diagonal vanishes; on the vector subspace the vector part ranges over all complex vectors and the diagonal does not vanish identically.

## The Elements whose Value Vanishes

**Theorem.** For two biquaternions,

$$
\tilde P\diamond\tilde Q=0
\iff
\mathbf{P}\ \text{and}\ \overline{\mathbf{Q}}\ \text{are}\ \mathbb{C}\text{-linearly dependent},
$$

that is, exactly when the vector part of one is a complex multiple of the conjugate of the vector part of the other, or one of the two vector parts is zero.

*Proof.* The value is the cross product $\mathbf{P}\times\overline{\mathbf{Q}}$, and a cross product of two complex vectors vanishes exactly when the two are linearly dependent over $\mathbb{C}$ or one of them is zero. Verified on general elements and on the six subspaces.

**Remark (the annihilators).** For a fixed $\tilde Q$ the elements $\tilde P$ with $\tilde P\diamond\tilde Q=0$ are the central elements together with the complex line $\mathbb{C}\overline{\mathbf{Q}}$; for a fixed $\tilde P$ the elements $\tilde Q$ with $\tilde P\diamond\tilde Q=0$ are the central elements together with the complex line $\mathbb{C}\overline{\mathbf{P}}$. The left and the right annihilator of an element are therefore complex planes through the origin, the centre together with a complex line, of complex dimension two, except when the element is central, in which case the annihilator is the whole space. The annihilators are the reason the block has no unit: no element can be reproduced by a product whose values always have a line of annihilation.

## Summary

On the six distinguished subspaces the block vanishes identically on the centre, has its image in the vector subspace, and is stable on the centre, the vector subspace, the quaternion subspace and the anti-Hermitian subspace, failing closure on the anti-quaternion subspace and the Hermitian subspace; the reason is that the value of two imaginary vector parts is a real vector, which leaves the two subspaces whose vector directions are imaginary. On the quaternion and the anti-Hermitian subspaces the block is the ordinary cross product of the real vector parts, the real coincidence with $\mathrm{APA}$. The diagonal is identically zero on the centre and on the four four-dimensional subspaces, and is not identically zero on the vector subspace, where it vanishes exactly on the complex multiples of the real directions. The value of two elements vanishes exactly when their vector parts are conjugate-linearly dependent, so the annihilator of an element is a complex plane through the origin, the centre together with a complex line, unless the element is central, and the block has no unit.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$, $\mathbb{M}_-$ | the six distinguished real subspaces |
| $\tilde P\diamond\tilde Q=\mathbf{P}\times\overline{\mathbf{Q}}$ | the block on the six |
| stable | the value of two elements of the subspace stays in the subspace |
| the four stable subspaces | centre, vector, quaternion, anti-Hermitian |
| the two failing subspaces | anti-quaternion, Hermitian |
| $\tilde P\diamond\tilde Q=0\iff\mathbf{P}\parallel_{\mathbb{C}}\overline{\mathbf{Q}}$ | the vanishing of the value |

## Further Reading

- *Introduction to the Six Subspaces*, for the six distinguished real subspaces and their bases.
- *The Six Subspaces under the General Quaternionic Sesqualgebra of Biquaternions*, for the norm reading of the same six.
- *Introduction to the Antisymmetric Quaternionic Sesqualgebra of Biquaternions*, for the block.
- *The Conjugate Cross Product and the Jacobi Failure of the Antisymmetric Quaternionic Sesqualgebra*, for the diagonal and its cone.
- *The Sesquilinear Pairing of the Antisymmetric Quaternionic Sesqualgebra*, for the form of the block on the six.
- *The Adjoint Operators of the Antisymmetric Quaternionic Sesqualgebra*, for the multiplication operators of the block.
