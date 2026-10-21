# __Remarkable Subspaces under the Antisymmetric Quaternionic Sesqualgebra__

## Introduction

The block $\tilde Q_1\diamond\tilde Q_2=\vec Q_1\times\overline{\vec Q_2}$ of *Introduction to the Antisymmetric Quaternionic Sesqualgebra* depends on its two arguments through their vector parts alone, with the vector part of the second argument conjugated. This article reads the block on the remarkable real subspaces of *Introduction to the Remarkable Subspaces* — the centre $\mathbb{C}_{\mathbb{B}}$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$, the Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$ — and answers three questions for each: whether the block is stable on it, that is whether the value of two of its elements stays in it; what the diagonal of the block does on it; and which of its elements give the value zero. The block kills the centre in both slots, so the centre is the one subspace on which the product vanishes identically, and the values of the block always lie in the vector subspace, so closure of any other subspace requires its intersection with the vector subspace to receive those values; that requirement separates the remarkable subspaces into the four on which the block is stable and the two on which it is not.

The remarkable subspaces and their bases are *Introduction to the Remarkable Subspaces*; the same six are read by the other pairings in *Remarkable Subspaces under the General Quaternionic Sesqualgebra* and its companions; the form that the block pairs with is *The Sesquilinear Pairing of the Antisymmetric Quaternionic Sesqualgebra*; and the product the block splits is *Introduction to the General Quaternionic Sesqualgebra*. This article owns the reading of the block on the remarkable subspaces themselves.

**Conventions.** As in the block: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$, $\vec e_x\vec e_y=\vec e_z$, and a generic element $\tilde Q_2=Q_{2t}e_t+\vec Q_2$, with $Q_{2,\mu}=q_\mu+iq'_\mu$ real and imaginary parts. The remarkable subspaces are real subspaces of the complex space; the word *stable* means that the value of two elements of the subspace lies in it, in the real sense, and not that the subspace is a complex subspace. The centre and the vector subspace are the only two of the remarkable subspaces that are complex subspaces.

## The Vanishing on the Centre and the Image

**Proposition.** The block annihilates the centre in both slots: for every central element $\tilde Q_3=Q_{3t}e_t$,

$$
\tilde Q_3\diamond\tilde Q_2=0,\qquad \tilde Q_2\diamond\tilde Q_3=0 .
$$

*Proof.* A central element has $\vec Q_3=0$, so the value is the cross product of a zero vector; the value is zero from either slot.

**Proposition.** The image of the block on every subspace is contained in the vector subspace, and on the vector subspace the block is stable with image the whole vector subspace.

*Proof.* Every value of the block is pure vector, so the image of any subspace lies in $\mathrm{Vect}(\mathbb{B})$. On $\mathrm{Vect}(\mathbb{B})$ the vector parts are the elements themselves, so the value $\vec Q_1\times\overline{\vec Q_2}$ of two complex vectors is again a complex vector, and the values fill the three complex dimensions.

## Remarkable Subspaces

### The Centre $\mathbb{C}_{\mathbb{B}}$

The centre is the complex line of the multiples of $e_t$. The block vanishes on it identically, so the centre is **stable** and is in fact contained in the annihilator of the block; its diagonal is zero, and every element of the centre gives the value zero with every element of the space on either side. The centre is the only subspace of the remarkable subspaces on which the block vanishes identically in both arguments.

### The Vector Subspace $\mathrm{Vect}(\mathbb{B})$

The vector subspace is the complex span of $\vec e_x,\vec e_y,\vec e_z$, with real basis $\vec e_x,\vec e_y,\vec e_z,i\vec e_x,i\vec e_y,i\vec e_z$. The block is **stable** on it and its image is the whole subspace: for two complex vectors $\vec Q_1,\vec Q_2$ the value $\vec Q_1\times\overline{\vec Q_2}$ is a complex vector, and the cross product with a fixed real direction already fills a complex plane. The diagonal is the conjugate cross product $\vec Q\times\overline{\vec Q}$, which is **not identically zero** on the subspace: it vanishes exactly when $\vec Q$ is a complex multiple of a real vector, that is on the union of the complex lines through the real directions, a quadric cone of real dimension $4$ and a proper subset; the witness $\vec e_x+i\vec e_y$ lies in the vector subspace and has diagonal $-2i\vec e_z$. The vector subspace is the one stable subspace on which the diagonal does not vanish identically.

### The Quaternion Subspace $\mathbb{H}_{\mathbb{B}}$

The quaternion subspace is the real span of $e_t,\vec e_x,\vec e_y,\vec e_z$, of real coefficients. The block is **stable** on it: two real vector parts have a real cross product, which lies in $\mathbb{H}_{\mathbb{B}}\cap\mathrm{Vect}(\mathbb{B})$, the real vector directions. On this subspace the block is the ordinary cross product of the real vector parts,

$$
\tilde Q_1\diamond\tilde Q_2=\vec Q_1\times\vec Q_2=\mathrm{APA}(\tilde Q_1,\tilde Q_2)\qquad(\tilde Q_1,\tilde Q_2\in\mathbb{H}_{\mathbb{B}}),
$$

the real coincidence of the block, and its image is the three real dimensions of the real vector directions. The diagonal is **identically zero**, a real vector being its own conjugate.

### The Anti-Quaternion Subspace $i\mathbb{H}_{\mathbb{B}}$

The anti-quaternion subspace is the real span of $ie_t,i\vec e_x,i\vec e_y,i\vec e_z$, of imaginary coefficients. The block is **not stable** on it: for two imaginary elements $\tilde Q_1=i\vec a$, $\tilde Q_2=i\vec b$ with $\vec a,\vec b$ real, the value is

$$
(i\vec a)\diamond(i\vec b)=i\vec a\times\overline{i\vec b}=i\vec a\times(-i\vec b)=\vec a\times\vec b,
$$

a **real** vector, which lies in $\mathbb{H}_{\mathbb{B}}\cap\mathrm{Vect}(\mathbb{B})$ and not in $i\mathbb{H}_{\mathbb{B}}$. The value of two elements of the subspace therefore leaves the subspace, and the intersection of the subspace with the vector subspace is the imaginary vector directions, which the block never reaches from the subspace. The diagonal is **identically zero**.

### The Hermitian Subspace $\mathbb{M}_+$

The Hermitian subspace is the real span of $e_t,i\vec e_x,i\vec e_y,i\vec e_z$, with real scalar coordinate and imaginary vector coordinates. The block is **not stable** on it: for two elements $i\vec a,i\vec b$ with real vector parts, the same computation as for the anti-quaternion subspace gives the real vector $\vec a\times\vec b$, which is not Hermitian, the vector part of a Hermitian element being imaginary. Its intersection with the vector subspace is the imaginary vector directions, which the block does not reach. The diagonal is **identically zero**, an imaginary vector being a complex multiple of a real vector.

### The Anti-Hermitian Subspace $\mathbb{M}_-$

The anti-Hermitian subspace is the real span of $ie_t,\vec e_x,\vec e_y,\vec e_z$, with imaginary scalar coordinate and real vector coordinates. The block is **stable** on it: for two elements with real vector parts the value is the real vector $\vec a\times\vec b$, which is anti-Hermitian. On this subspace the block is again the ordinary cross product of the real vector parts, with the scalar coordinates ignored, and its image is the three real dimensions of the real vector directions. The diagonal is **identically zero**, a real vector being its own conjugate.

**Remark (the four stable subspaces and the two failing ones).** Closure holds on the centre, on the vector subspace, on the quaternion subspace and on the anti-Hermitian subspace, and it fails on the anti-quaternion subspace and on the Hermitian subspace. The reason is uniform: the block always lands in the vector subspace, so a subspace is stable exactly when the values that reach it lie in its intersection with the vector subspace. The quaternion and the anti-Hermitian subspaces contain the real vector directions and stay stable; the anti-quaternion and the Hermitian subspaces contain only the imaginary vector directions, and the value of two of their elements is a real vector, so they fail. The centre is stable because its value is zero. The menu entry of the block records the vanishing on the centre and the pure-vector image; the failure of closure is not shared by the quaternion and the anti-Hermitian subspaces, and the reading here corrects the impression that the block fails closure on every subspace other than the centre and the vector subspace.

## The Table of the Remarkable Subspaces

| Subspace | Natural real basis | Value of the block on two of its elements | Stable | Diagonal |
|---|---|---|---|---|
| Centre $\mathbb{C}_{\mathbb{B}}$ | $e_t,\,ie_t$ | $0$ | yes | $0$ |
| Vector $\mathrm{Vect}(\mathbb{B})$ | $\vec e_x,\vec e_y,\vec e_z,\,i\vec e_x,i\vec e_y,i\vec e_z$ | a complex vector | yes | not identically zero |
| Quaternion $\mathbb{H}_{\mathbb{B}}$ | $e_t,\vec e_x,\vec e_y,\vec e_z$ | a real vector | yes | $0$ |
| Anti-quaternion $i\mathbb{H}_{\mathbb{B}}$ | $ie_t,i\vec e_x,i\vec e_y,i\vec e_z$ | a real vector | no | $0$ |
| Hermitian $\mathbb{M}_+$ | $e_t,i\vec e_x,i\vec e_y,i\vec e_z$ | a real vector | no | $0$ |
| Anti-Hermitian $\mathbb{M}_-$ | $ie_t,\vec e_x,\vec e_y,\vec e_z$ | a real vector | yes | $0$ |

**Remark (the four subspaces with a vanishing diagonal).** The diagonal of the block is identically zero on the centre and on the four four-dimensional subspaces, and it is not identically zero on the vector subspace alone. The four four-dimensional subspaces have their vector part real or purely imaginary, and a real or purely imaginary vector is a complex multiple of a real vector, so the diagonal vanishes; on the vector subspace the vector part ranges over all complex vectors and the diagonal does not vanish identically.

## The Elements whose Value Vanishes

**Theorem.** For two biquaternions,

$$
\tilde Q_1\diamond\tilde Q_2=0
\iff
\vec Q_1\ \text{and}\ \overline{\vec Q_2}\ \text{are}\ \mathbb{C}\text{-linearly dependent},
$$

that is, exactly when the vector part of one is a complex multiple of the conjugate of the vector part of the other, or one of the two vector parts is zero.

*Proof.* The value is the cross product $\vec Q_1\times\overline{\vec Q_2}$, and a cross product of two complex vectors vanishes exactly when the two are linearly dependent over $\mathbb{C}$ or one of them is zero.

**Remark (the annihilators).** For a fixed $\tilde Q_2$ the elements $\tilde Q_1$ with $\tilde Q_1\diamond\tilde Q_2=0$ are the central elements together with the complex line $\mathbb{C}\overline{\vec Q_2}$; for a fixed $\tilde Q_1$ the elements $\tilde Q_2$ with $\tilde Q_1\diamond\tilde Q_2=0$ are the central elements together with the complex line $\mathbb{C}\overline{\vec Q_1}$. The left and the right annihilator of an element are therefore complex planes through the origin, the centre together with a complex line, of complex dimension two, except when the element is central, in which case the annihilator is the whole space. The annihilators are the reason the block has no unit: no element can be reproduced by a product whose values always have a line of annihilation.

## Summary

On the remarkable subspaces the block vanishes identically on the centre, has its image in the vector subspace, and is stable on the centre, the vector subspace, the quaternion subspace and the anti-Hermitian subspace, failing closure on the anti-quaternion subspace and the Hermitian subspace; the reason is that the value of two imaginary vector parts is a real vector, which leaves the two subspaces whose vector directions are imaginary. On the quaternion and the anti-Hermitian subspaces the block is the ordinary cross product of the real vector parts, the real coincidence with $\mathrm{APA}$. The diagonal is identically zero on the centre and on the four four-dimensional subspaces, and is not identically zero on the vector subspace, where it vanishes exactly on the complex multiples of the real directions. The value of two elements vanishes exactly when their vector parts are conjugate-linearly dependent, so the annihilator of an element is a complex plane through the origin, the centre together with a complex line, unless the element is central, and the block has no unit.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$, $\mathbb{M}_-$ | the remarkable real subspaces |
| $\tilde Q_1\diamond\tilde Q_2=\vec Q_1\times\overline{\vec Q_2}$ | the block on the remarkable subspaces |
| stable | the value of two elements of the subspace stays in the subspace |
| the four stable subspaces | centre, vector, quaternion, anti-Hermitian |
| the two failing subspaces | anti-quaternion, Hermitian |
| $\tilde Q_1\diamond\tilde Q_2=0\iff\vec Q_1\parallel_{\mathbb{C}}\overline{\vec Q_2}$ | the vanishing of the value |

## Further Reading

- [Introduction to the Remarkable Subspaces](introduction-to-the-remarkable-subspaces.html), for the remarkable real subspaces and their bases.
- [Remarkable Subspaces under the General Quaternionic Sesqualgebra](remarkable-subspaces-under-the-general-quaternionic-sesqualgebra.html), for the norm reading of the same six.
- [Introduction to the Antisymmetric Quaternionic Sesqualgebra](introduction-to-the-antisymmetric-quaternionic-sesqualgebra.html), for the block.
- [The Conjugate Cross Product and the Jacobi Failure of the Antisymmetric Quaternionic Sesqualgebra](the-conjugate-cross-product-and-the-jacobi-failure-of-the-antisymmetric-quaternionic-sesqualgebra.html), for the diagonal and its cone.
- [The Sesquilinear Pairing of the Antisymmetric Quaternionic Sesqualgebra](the-sesquilinear-pairing-of-the-antisymmetric-quaternionic-sesqualgebra.html), for the form of the block on the remarkable subspaces.
- [The Adjoint Operators of the Antisymmetric Quaternionic Sesqualgebra](the-adjoint-operators-of-the-antisymmetric-quaternionic-sesqualgebra.html), for the multiplication operators of the block.
