# __Remarkable Subspaces under the Antisymmetric Plain Algebra of Biquaternions__

## Introduction

The bracket of the antisymmetric plain algebra, $\tilde P\wedge\tilde Q=\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)=\mathbf{P}\times\mathbf{Q}$, meets the remarkable real subspaces of *Introduction to the Remarkable Subspaces* — the centre $\mathbb{C}_{\mathbb{B}}$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$, the Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$ — and this article reads the bracket on each of the remarkable subspaces, one to a section.

Because the bracket is the cross product of the vector parts and nothing else, the readings are read off a single fact: the sector, real or purely imaginary, that the vector part of an element of the subspace occupies. The result is a table of four stabilities and two failures. The centre, the vector subspace, the quaternion subspace and the anti-Hermitian subspace are **stable** under the bracket, hence Lie subalgebras; the anti-quaternion subspace and the Hermitian subspace are **not**, and the bracket of two of their elements is always a real vector. The identifications of the Lie subalgebras are $\mathrm{Vect}(\mathbb{B})\cong\mathfrak{sl}(2,\mathbb{C})$, $\mathbb{H}_{\mathbb{B}}\cong\mathbb{R}e_0\oplus\mathfrak{su}(2)$ and $\mathbb{M}_-\cong\mathfrak{u}(2)$; the two failures have image the real vector triple $\mathbf{B}_1=\mathbb{R}e_1\oplus\mathbb{R}e_2\oplus\mathbb{R}e_3$, identified with $\mathfrak{su}(2)$. The centre is where the bracket vanishes and the vector subspace is where it takes its values; the two together are the whole algebra.

The bracket is introduced in *Introduction to the Antisymmetric Plain Algebra of Biquaternions* and its Lie structure on the whole algebra is *The Lie Algebra of the Antisymmetric Plain Algebra*, where the centre and the identifications of the vector, quaternion and anti-Hermitian subspaces are established; this article owns the reading of the bracket on each of the remarkable subspaces and the two failures, and it defers the whole-algebra structure to that article and the invariant form to *The Killing Form of the Antisymmetric Plain Algebra*. The remarkable subspaces themselves are *Introduction to the Remarkable Subspaces* and their relations *Comparison of the Remarkable Subspaces*; their reading under the four general products is *Remarkable Subspaces and the Four General Products*; the pattern of the reading is *Remarkable Subspaces under the General Plain Algebra of Biquaternions*; and the operators of the block are *The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra*.

## The Bracket on the remarkable subspaces: the Rule

**Lemma (the sector rule).** Let $\tilde P,\tilde Q$ have vector parts in the real vector triple $\mathbf{B}_1=\mathbb{R}e_1\oplus\mathbb{R}e_2\oplus\mathbb{R}e_3$ or in the imaginary triple $i\mathbf{B}_1=\mathbb{R}(ie_1)\oplus\mathbb{R}(ie_2)\oplus\mathbb{R}(ie_3)$. Then

$$
\mathbf{P}\times\mathbf{Q}\in
\begin{cases}
\mathbf{B}_1, & \mathbf{P},\mathbf{Q}\in\mathbf{B}_1\text{ or }\mathbf{P},\mathbf{Q}\in i\mathbf{B}_1,\\[2pt]
i\mathbf{B}_1, & \text{one in }\mathbf{B}_1\text{ and one in }i\mathbf{B}_1.
\end{cases}
$$

*Proof.* Write $\mathbf{P}=i^{\varepsilon}\mathbf{p}$, $\mathbf{Q}=i^{\eta}\mathbf{q}$ with $\mathbf{p},\mathbf{q}$ in the real vector triple and $\varepsilon,\eta\in\{0,1\}$. Then $\mathbf{P}\times\mathbf{Q}=i^{\varepsilon+\eta}(\mathbf{p}\times\mathbf{q})$, and $\mathbf{p}\times\mathbf{q}\in\mathbf{B}_1$; the sector is $\varepsilon+\eta$ modulo two, which is the statement. $\square$

**Remark (the two gradings).** The rule is a $\mathbb{Z}/2$-grading of the real algebra in two ways. With the two real subspaces $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$ the brackets are $[\mathbb{H}_{\mathbb{B}},\mathbb{H}_{\mathbb{B}}]\subseteq\mathbb{H}_{\mathbb{B}}$, $[\mathbb{H}_{\mathbb{B}},i\mathbb{H}_{\mathbb{B}}]\subseteq i\mathbb{H}_{\mathbb{B}}$ and $[i\mathbb{H}_{\mathbb{B}},i\mathbb{H}_{\mathbb{B}}]\subseteq\mathbb{H}_{\mathbb{B}}$; with the two subspaces $\mathbb{M}_-$ and $\mathbb{M}_+$ they are $[\mathbb{M}_-,\mathbb{M}_-]\subseteq\mathbb{M}_-$, $[\mathbb{M}_-,\mathbb{M}_+]\subseteq\mathbb{M}_+$ and $[\mathbb{M}_+,\mathbb{M}_+]\subseteq\mathbb{M}_-$. **Both decompositions of the real algebra, $\mathbb{B}=\mathbb{H}_{\mathbb{B}}\oplus i\mathbb{H}_{\mathbb{B}}$ and $\mathbb{B}=\mathbb{M}_-\oplus\mathbb{M}_+$, are gradings of the bracket**, the first with subalgebra $\mathbb{H}_{\mathbb{B}}$ and the second with subalgebra $\mathbb{M}_-$.

## The Centre

**Theorem.** The bracket vanishes identically on the centre:

$$
\tilde P\wedge\tilde Q=0\qquad(\tilde P,\tilde Q\in\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0).
$$

The centre is a Lie subalgebra of $\mathfrak{g}$, abelian of complex dimension one and real dimension two; it is the kernel of the adjoint of every element and the radical of the bracket, and it is the radical of the Killing form of *The Killing Form of the Antisymmetric Plain Algebra*.

*Proof.* An element of the centre has vector part zero, so every bracket with it vanishes by the vector-part formula; an abelian subalgebra is a Lie subalgebra. The centre is the annihilator of the bracket by *The Lie Algebra of the Antisymmetric Plain Algebra*, §*The Centre and the Quotient*, and its identification with the radical of the invariant form is *The Killing Form of the Antisymmetric Plain Algebra*, §*The Radical and the Rank*. Computed on the two real coordinates $e_0$ and $ie_0$. $\square$

**Remark.** **The centre is the subspace of the remarkable subspaces on which the bracket is the zero operation**, and it is the only one on which every bracket vanishes. It is not the whole of the kernel of the block, since the bracket of an element with itself vanishes by alternation; it is the common kernel of all the adjoints, which is the stronger statement.

## The Vector Subspace

**Theorem.** The vector subspace $\mathrm{Vect}(\mathbb{B})$ is stable under the bracket:

$$
\mathbf{P}\times\mathbf{Q}\in\mathrm{Vect}(\mathbb{B})\qquad(\mathbf{P},\mathbf{Q}\in\mathrm{Vect}(\mathbb{B})),
$$

and it is a Lie subalgebra of complex dimension three and real dimension six, an ideal, and the derived algebra of the whole block. It is identified with the cross-product algebra of $\mathbb{C}^3$ and with $\mathfrak{sl}(2,\mathbb{C})$,

$$
\bigl(\mathrm{Vect}(\mathbb{B}),\wedge\bigr)\cong\bigl(\mathbb{C}^3,\times\bigr)\cong\mathfrak{sl}(2,\mathbb{C}),
$$

and it is simple: it has no nonzero proper ideal.

*Proof.* The vector subspace is the image of the bracket, so it is stable and it is the derived algebra; the identification and the simplicity are *The Lie Algebra of the Antisymmetric Plain Algebra*, §*The Derived Algebra and the Identifications*. Computed on the complex basis $e_1,e_2,e_3$ and on the real basis $e_1,e_2,e_3,ie_1,ie_2,ie_3$. $\square$

**Remark.** **The vector subspace is the smallest of the remarkable subspaces that contains the values of the bracket and the largest simple piece of the block.** Its real and imaginary halves obey the sector rule: the bracket of two real vectors is a real vector, of two imaginary vectors a real vector, and of one of each an imaginary vector; the composition table of the cross product of $\mathbb{C}^3$ is thus the real and imaginary reading of the three complex brackets $e_1\wedge e_2=e_3$ and its cyclic analogues.

## The Quaternion Subspace

**Theorem.** The quaternion subspace

$$
\mathbb{H}_{\mathbb{B}}=\mathbb{R}e_0\oplus\mathbf{B}_1=\{Q_0e_0+\mathbf{Q}:Q_0\in\mathbb{R},\ \mathbf{Q}\in\mathbb{R}^3\}
$$

is stable under the bracket: the bracket of two of its elements is the cross product of their real vector parts, a real vector. It is a real Lie subalgebra of dimension four,

$$
\mathbb{H}_{\mathbb{B}}\cong\mathbb{R}e_0\oplus\mathfrak{su}(2),
$$

with the scalar direction $\mathbb{R}e_0$ central and the vector triple $\mathbf{B}_1$ identified with $\mathfrak{su}(2)$, and its derived algebra is $\mathbf{B}_1$.

*Proof.* An element of $\mathbb{H}_{\mathbb{B}}$ has real scalar and real vector parts; the bracket sees only the vector parts and is the cross product of two real vectors, which is a real vector, so the subspace is stable. Its derived algebra is $\mathbf{B}_1$, since $e_1\wedge e_2=e_3$ and cyclically; the real vector triple with the cross product is the real form $\mathfrak{so}(3,\mathbb{R})\cong\mathfrak{su}(2)$ of $\mathfrak{sl}(2,\mathbb{C})$, and the scalar direction is central. This is *The Lie Algebra of the Antisymmetric Plain Algebra*, §*The Real Forms*. Computed on the real basis. $\square$

**Remark.** The quaternion subspace is one of the two real forms of the block that carry the real vector triple as their derived algebra; the other is the anti-Hermitian subspace below. **The scalar direction is central and the vector triple is simple, so the quaternion subspace is the direct sum of an abelian line and $\mathfrak{su}(2)$.** In the grading $\mathbb{B}=\mathbb{H}_{\mathbb{B}}\oplus i\mathbb{H}_{\mathbb{B}}$ it is the subalgebra, and $i\mathbb{H}_{\mathbb{B}}$ is the complement, read next.

## The Anti-Quaternion Subspace

**Theorem.** The anti-quaternion subspace

$$
i\mathbb{H}_{\mathbb{B}}=\mathbb{R}(ie_0)\oplus i\mathbf{B}_1=\{Q_0e_0+\mathbf{Q}:Q_0\in i\mathbb{R},\ \mathbf{Q}\in i\mathbb{R}^3\}
$$

is **not** stable under the bracket. The bracket of two of its elements is a real vector, and

$$
[i\mathbb{H}_{\mathbb{B}},i\mathbb{H}_{\mathbb{B}}]=\mathbf{B}_1\cong\mathfrak{su}(2).
$$

A witness of the failure is the pair $ie_1,ie_2$: both lie in $i\mathbb{H}_{\mathbb{B}}$ and

$$
(ie_1)\wedge(ie_2)=(i)(i)\,(e_1\wedge e_2)=-e_3,
$$

which is a real vector and does not lie in $i\mathbb{H}_{\mathbb{B}}$.

*Proof.* Write the vector parts of two elements of $i\mathbb{H}_{\mathbb{B}}$ as $i\mathbf{p}$ and $i\mathbf{q}$ with $\mathbf{p},\mathbf{q}\in\mathbf{B}_1$; then $(i\mathbf{p})\times(i\mathbf{q})=-(\mathbf{p}\times\mathbf{q})\in\mathbf{B}_1$, by the sector rule. The bracket therefore leaves the subspace and its image is spanned by the cross products of real vectors, which is the whole of $\mathbf{B}_1$; the witness is the explicit computation. Verified on the real basis. $\square$

**Remark.** The anti-quaternion subspace is one of the two failures, and the failure is total: **its bracket is not merely outside it, it is in the other grading half.** With the quaternion subspace it forms the grading $\mathbb{B}=\mathbb{H}_{\mathbb{B}}\oplus i\mathbb{H}_{\mathbb{B}}$ in which $\mathbb{H}_{\mathbb{B}}$ is the subalgebra, $i\mathbb{H}_{\mathbb{B}}$ the module, and the module is large enough that its own bracket fills the vector triple of the subalgebra.

## The Hermitian and the Anti-Hermitian Subspaces

**Theorem (the Hermitian subspace is not stable).** The Hermitian subspace

$$
\mathbb{M}_+=\mathbb{R}e_0\oplus i\mathbf{B}_1=\{Q_0e_0+\mathbf{Q}:Q_0\in\mathbb{R},\ \mathbf{Q}\in i\mathbb{R}^3\}
$$

is **not** stable under the bracket. The bracket of two of its elements is a real vector, and

$$
[\mathbb{M}_+,\mathbb{M}_+]=\mathbf{B}_1\cong\mathfrak{su}(2).
$$

A witness is the pair $ie_1,ie_2$: both lie in $\mathbb{M}_+$ and $(ie_1)\wedge(ie_2)=-e_3$, which does not lie in $\mathbb{M}_+$.

*Proof.* Write the vector parts as $i\mathbf{p},i\mathbf{q}$ with $\mathbf{p},\mathbf{q}\in\mathbf{B}_1$; the sector rule gives $(i\mathbf{p})\times(i\mathbf{q})=-(\mathbf{p}\times\mathbf{q})\in\mathbf{B}_1$, outside $i\mathbf{B}_1$, and the image is the whole of $\mathbf{B}_1$. Verified on the real basis. $\square$

**Theorem (the anti-Hermitian subspace is stable).** The anti-Hermitian subspace

$$
\mathbb{M}_-=\mathbb{R}(ie_0)\oplus\mathbf{B}_1=\{Q_0e_0+\mathbf{Q}:Q_0\in i\mathbb{R},\ \mathbf{Q}\in\mathbb{R}^3\}
$$

is stable under the bracket: the bracket of two of its elements is the cross product of two real vectors. It is a real Lie subalgebra of dimension four,

$$
\mathbb{M}_-\cong\mathfrak{u}(2),\qquad[\mathbb{M}_-,\mathbb{M}_-]=\mathbf{B}_1\cong\mathfrak{su}(2).
$$

*Proof.* An element of $\mathbb{M}_-$ has purely imaginary scalar part and real vector part; the bracket sees only the vector parts, so it is a real vector in $\mathbf{B}_1$, which lies in $\mathbb{M}_-$. The derived algebra is $\mathbf{B}_1$, and the real Lie algebra with a central line and derived algebra $\mathfrak{su}(2)$ is $\mathfrak{u}(2)$, read on the skew-Hermitian elements in *The Unitary Lie Algebra*. This is *The Lie Algebra of the Antisymmetric Plain Algebra*, §*The Real Forms*. Computed on the real basis. $\square$

**Remark.** The two Hermitian halves are the second grading of the block: **$\mathbb{M}_-$ is the subalgebra and $\mathbb{M}_+$ the module, and $\mathbb{M}_+$ is the second of the two failures, of image again $\mathfrak{su}(2)$.** The quaternion grading and the Hermitian grading share the failure pattern — in each, one half is a subalgebra and the other half is not — and they differ in which central direction, real or imaginary, the subalgebra's scalar part occupies. The identification $\mathbb{M}_-\cong\mathfrak{u}(2)$ is the biquaternion case of the skew-Hermitian Lie algebra; the group of linear maps preserving the form of those elements, and the exponential that relates it to this algebra, are *The Unitary Lie Algebra* and are not read here.

## The Isotropic Elements

The invariant form of the block is computed in *The Killing Form of the Antisymmetric Plain Algebra*, where its restriction to each of the remarkable subspaces and its isotropic elements are found; the section is recorded here as the sixth row of the table, and one line of it belongs to the bracket. An element $\tilde Q$ is isotropic for the form when $\kappa(\tilde Q,\tilde Q)=-2\,\mathbf{Q}\cdot\mathbf{Q}=0$, that is when its vector part is isotropic for the complexified scalar product.

**Theorem.** The isotropic elements of the remarkable subspaces are: the whole centre, since the form vanishes there; the scalar directions $\mathbb{R}e_0$ and $\mathbb{R}(ie_0)$ on the four real subspaces, and no vector direction, because the vector part there is real or purely imaginary and a sum of three squares of real numbers vanishes only at zero; and the complex null cone $\{\mathbf{P}\cdot\mathbf{P}=0\}$ on the vector subspace, of real dimension four. On the centre and on the scalar directions the isotropy is the vanishing of the bracket as well, since those are the central directions; on the vector null cone the bracket is not identically zero, and the isotropic elements are the elements of the simple derived algebra that are isotropic for its invariant form.

*Proof.* The form is $-2\,\mathbf{Q}\cdot\mathbf{Q}$ on the vector part and zero on the scalar part, by *The Killing Form of the Antisymmetric Plain Algebra*; the four real subspaces have real or purely imaginary vector parts, and the two complex subspaces, the centre and the vector subspace, have the components as displayed. The vanishing of the bracket on the central directions is the previous sections. Verified on the basis and on general elements. $\square$

**Remark.** **The isotropic elements of the block are not its zero divisors, and on the four real subspaces they are only the null directions of the bracket.** The comparison with the zero-divisor cone and with the null cones of the four pairings is *Remarkable Subspaces and the Four General Products* and *Biquaternion Zero Divisors*; the two cones agree on the vector subspace at the complex null cone of the scalar product and differ on the real subspaces, where the Killing isotropy is a line and the zero-divisor condition is a genuine cone.

## The Table of the Remarkable Subspaces

| Subspace | Vector part | Stable under $\wedge$ | Image of $\wedge$ | Identification |
|---|---|---|---|---|
| Centre $\mathbb{C}_{\mathbb{B}}$ | $0$ | yes, trivially | $0$ | abelian, the radical |
| Vector $\mathrm{Vect}(\mathbb{B})$ | complex | yes | itself | $\mathfrak{sl}(2,\mathbb{C})$, simple |
| Quaternion $\mathbb{H}_{\mathbb{B}}$ | real | yes | $\mathbf{B}_1$ | $\mathbb{R}e_0\oplus\mathfrak{su}(2)$ |
| Anti-quaternion $i\mathbb{H}_{\mathbb{B}}$ | imaginary | **no** | $\mathbf{B}_1$ | $\mathfrak{su}(2)$ image, not a subalgebra |
| Hermitian $\mathbb{M}_+$ | imaginary | **no** | $\mathbf{B}_1$ | $\mathfrak{su}(2)$ image, not a subalgebra |
| Anti-Hermitian $\mathbb{M}_-$ | real | yes | $\mathbf{B}_1$ | $\mathfrak{u}(2)$, derived $\mathfrak{su}(2)$ |

**Remark.** **Four of the remarkable subspaces are Lie subalgebras and two are not**, and the two failures are exactly the two subspaces whose vector part is the imaginary triple $i\mathbf{B}_1$, $i\mathbb{H}_{\mathbb{B}}$ and $\mathbb{M}_+$. The two are exchanged by the central scalar $i$, which reverses the sector of the vector part and the sector of the scalar part together and carries the quaternion subalgebra to the anti-quaternion failure and the anti-Hermitian subalgebra to the Hermitian failure; the table is therefore symmetric under $i$ with the stability column exchanged.

## Worked Examples

**The centre.** $\tilde P=e_0+ie_0$ and $\tilde Q=e_1$ give $\tilde P\wedge\tilde Q=0$: the central element is annihilated, and the centre is the zero row.

**A real vector bracket.** $e_1\wedge e_2=e_3$: the bracket of two real vectors is a real vector, the first line of the sector rule.

**An imaginary vector bracket.** $(ie_1)\wedge(ie_2)=-e_3$: the bracket of two imaginary vectors is a real vector, the witness of the two failures.

**A mixed bracket.** $e_1\wedge(ie_2)=ie_3$: one real and one imaginary vector give an imaginary vector, the second line of the sector rule.

**A quaternion bracket.** For $\tilde Q=e_0+e_1$ and $\tilde R=e_0+e_2$ in $\mathbb{H}_{\mathbb{B}}$ the bracket is $\tilde Q\wedge\tilde R=e_3$, inside the subspace: the quaternion subspace is stable.

**An anti-Hermitian bracket.** For $x=ie_0+e_1$ and $y=ie_0+e_2$ in $\mathbb{M}_-$ the bracket is $x\wedge y=e_3$, inside the subspace: the anti-Hermitian subspace is stable, and the imaginary scalar direction $ie_0$ is central in it.

**A failure.** For $x=ie_1$ and $y=ie_2$ in $i\mathbb{H}_{\mathbb{B}}$, and also in $\mathbb{M}_+$, the bracket is $x\wedge y=-e_3$, outside both; the image lies in $\mathbf{B}_1$, the derived algebra of both subalgebras $\mathbb{H}_{\mathbb{B}}$ and $\mathbb{M}_-$.

## Summary

The bracket of the antisymmetric plain algebra is the cross product of the vector parts, and its reading on the remarkable subspaces is the reading of the sector of the vector part. The centre is the zero subspace, on which the bracket vanishes; the vector subspace is stable, is the derived algebra of the whole block and is identified with $\mathfrak{sl}(2,\mathbb{C})$; the quaternion subspace is stable and identified with $\mathbb{R}e_0\oplus\mathfrak{su}(2)$; the anti-Hermitian subspace is stable and identified with $\mathfrak{u}(2)$, of derived algebra $\mathfrak{su}(2)$; and the anti-quaternion subspace and the Hermitian subspace are not stable, with brackets $(ie_1)\wedge(ie_2)=-e_3$ in each case and image the real vector triple $\mathbf{B}_1\cong\mathfrak{su}(2)$. Four of the remarkable subspaces are Lie subalgebras and two are not, the two failures being the subspaces with vector part the imaginary triple $i\mathbf{B}_1$; the two decompositions $\mathbb{B}=\mathbb{H}_{\mathbb{B}}\oplus i\mathbb{H}_{\mathbb{B}}$ and $\mathbb{B}=\mathbb{M}_-\oplus\mathbb{M}_+$ are $\mathbb{Z}/2$-gradings of the bracket. The isotropic elements are the whole centre, the two scalar directions on the four real subspaces, and the complex null cone on the vector subspace.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\wedge\tilde Q=\mathbf{P}\times\mathbf{Q}$ | the bracket of the block, the cross product of the vector parts |
| $\mathbf{B}_1=\mathbb{R}e_1\oplus\mathbb{R}e_2\oplus\mathbb{R}e_3$ | the real vector triple, the image of the two failures |
| $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ | the centre, the subspace on which the bracket vanishes |
| $\mathrm{Vect}(\mathbb{B})$ | the stable image of the bracket $\cong\mathfrak{sl}(2,\mathbb{C})$ |
| $\mathbb{H}_{\mathbb{B}}\cong\mathbb{R}e_0\oplus\mathfrak{su}(2)$ | the quaternion subalgebra |
| $i\mathbb{H}_{\mathbb{B}}$, $[\ ,\ ]=\mathbf{B}_1$ | the anti-quaternion subspace, not stable |
| $\mathbb{M}_+\cong$ image $\mathbf{B}_1$ | the Hermitian subspace, not stable |
| $\mathbb{M}_-\cong\mathfrak{u}(2)$, $[\mathbb{M}_-,\mathbb{M}_-]\cong\mathfrak{su}(2)$ | the anti-Hermitian subalgebra |
| $\mathbb{B}=\mathbb{H}_{\mathbb{B}}\oplus i\mathbb{H}_{\mathbb{B}}=\mathbb{M}_-\oplus\mathbb{M}_+$ | the two $\mathbb{Z}/2$-gradings of the bracket |
| $\kappa(\tilde Q,\tilde Q)=-2\,\mathbf{Q}\cdot\mathbf{Q}$ | the form whose isotropic elements are tabulated |

## Further Reading

- *Introduction to the Antisymmetric Plain Algebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-plain-algebra-of-biquaternions.md`), for the bracket and its sixteen values on the basis
- *The Lie Algebra of the Antisymmetric Plain Algebra* (`articles_maths/the-lie-algebra-of-the-antisymmetric-plain-algebra.md`), for the structural reading of the whole algebra, the centre and the real forms
- *The Killing Form of the Antisymmetric Plain Algebra* (`articles_maths/the-killing-form-of-the-antisymmetric-plain-algebra.md`), for the form restricted to the remarkable subspaces and its isotropic elements
- *The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra* (`articles_maths/the-adjoint-operators-and-the-derivations-of-the-antisymmetric-plain-algebra.md`), for the adjoints and the automorphisms of the bracket
- *Introduction to the Remarkable Subspaces* (`articles_maths/introduction-to-the-remarkable-subspaces.md`) and *Comparison of the Remarkable Subspaces* (`articles_maths/comparison-of-the-remarkable-subspaces.md`), for the remarkable subspaces and their relations
- *Remarkable Subspaces under the General Plain Algebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-general-plain-algebra-of-biquaternions.md`), for the pattern of the reading under the general plain product
- *Remarkable Subspaces and the Four General Products* (`articles_maths/remarkable-subspaces-and-the-four-general-products.md`), for the comparison of the readings of the remarkable subspaces under the four general products
- *The Unitary Lie Algebra* (`articles_maths/the-unitary-lie-algebra.md`), for the skew-Hermitian elements and their group
