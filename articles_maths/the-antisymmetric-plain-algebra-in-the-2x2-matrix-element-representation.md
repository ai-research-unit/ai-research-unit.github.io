# __The Antisymmetric Plain Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$__

## Introduction

The antisymmetric plain algebra, $\tilde P\wedge\tilde Q=\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)=\mathbf{P}\times\mathbf{Q}$, is read here in the $2\times2$ matrix model of the chapter of the general plain algebra: the two-dimensional model $\mathbb{B}\cong M_2(\mathbb{C})$, in which the bracket is the halved commutator of the matrix product. This article is the first of the two representation articles of the block, and its companion *The Antisymmetric Plain Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$* reads the same bracket in the regular model and through the adjoint representation.

The model turns the bracket into the halved commutator $\tfrac12(XY-YX)$ of two by two complex matrices, and the whole block is read off the two standard facts about the matrix commutator: **its image is the trace-free matrices, of complex dimension three, and its kernel is the scalar matrices, of complex dimension one.** The image is the derived algebra $\mathrm{Vect}(\mathbb{B})$, identified with $\mathfrak{sl}(2,\mathbb{C})$; the kernel is the centre $\mathbb{C}_{\mathbb{B}}$; and the trace form of the model is the Killing form of the block, $\kappa(\tilde P,\tilde Q)=\operatorname{Tr}(\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q))$ on the derived algebra.

The model is *The General Plain Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*, and its construction is *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*. The bracket, its structure and its forms are used from *Introduction to the Antisymmetric Plain Algebra of Biquaternions*, *The Lie Algebra of the Antisymmetric Plain Algebra*, *The Killing Form of the Antisymmetric Plain Algebra* and *The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra*; the left and the right multiplication operators of the plain product are *One-Sided Operators on the General Plain Algebra of Biquaternions* and *Two-Sided Operators on the General Plain Algebra of Biquaternions*; and the identification of the trace-free matrices with $\mathfrak{sl}(2,\mathbb{C})$ is *Structure of Lie Algebras*. The model is an algebra isomorphism, and no analytic notion is read on it.

## The Bracket as the Halved Commutator

**Recall (the model).** The $2\times2$ realization is the $\mathbb{C}$-algebra isomorphism $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ fixed by its values on the basis, the rest following by $\mathbb{C}$-linearity:

$$
\mathsf{M}_2(e_0)=\mathrm{I}_2,\qquad \mathsf{M}_2(e_1)=-i\sigma_1,\qquad \mathsf{M}_2(e_2)=-i\sigma_2,\qquad \mathsf{M}_2(e_3)=-i\sigma_3,
$$

where $\sigma_1,\sigma_2,\sigma_3$ are the Pauli matrices, with $\mathsf{M}_2(i\tilde P)=i\mathsf{M}_2(\tilde P)$ and $\operatorname{Tr}\mathsf{M}_2(\tilde Q)=2Q_0$ (*Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*).

**Theorem (the bracket as the halved commutator).** For all $\tilde P,\tilde Q\in\mathbb{B}$,

$$
\mathsf{M}_2(\tilde P\wedge\tilde Q)=\tfrac12\bigl[\mathsf{M}_2(\tilde P),\mathsf{M}_2(\tilde Q)\bigr],
$$

and the image of the block is the subspace of the trace-free matrices, while its kernel is the subspace of the scalar matrices:

$$
\mathsf{M}_2\bigl(\mathrm{Vect}(\mathbb{B})\bigr)=\{X\in M_2(\mathbb{C}):\operatorname{Tr}X=0\},\qquad
\ker\wedge=\mathsf{M}_2^{-1}(\mathbb{C}\,\mathrm{I}_2)=\mathbb{C}_{\mathbb{B}}.
$$

*Proof.* The model is an algebra isomorphism, so $\mathsf{M}_2(\tilde P\tilde Q-\tilde Q\tilde P)=[\mathsf{M}_2(\tilde P),\mathsf{M}_2(\tilde Q)]$ and half of it is the image of the bracket. An element of the vector subspace has $Q_0=0$ and image of trace zero, and conversely a trace-free matrix has the second coefficient $Q_0$ zero, so it is the image of a vector element; the kernel of the bracket is the centre by *The Lie Algebra of the Antisymmetric Plain Algebra*, and its image under $\mathsf{M}_2$ is the scalar matrices, because $\operatorname{Tr}\mathsf{M}_2(\tilde Q)=2Q_0$ vanishes exactly on the vector subspace. Verified on general elements. $\square$

**Remark (the block is the matrix commutator).** **The antisymmetric plain algebra is, in this model, the halved commutator of the two by two complex matrices, its image is $\mathfrak{sl}(2,\mathbb{C})$ and its kernel is the centre.** The scalar part of the biquaternion is the trace of the matrix, split in two, and the bracket annihilates it; the vector part is the trace-free part, of complex dimension three, and the bracket is the commutator there. The trace-free matrices with the commutator are the Lie algebra $\mathfrak{sl}(2,\mathbb{C})$ of *Structure of Lie Algebras*, and the block's halved bracket is the same Lie algebra under the rescaling $\tilde P\mapsto2\tilde P$.

**Theorem (the Lie algebra).** The bracket on the trace-free matrices is a Lie bracket, of which the model satisfies the identity

$$
\bigl[\mathsf{M}_2(\tilde P\wedge\tilde Q),\mathsf{M}_2(\tilde R)\bigr]=\tfrac12\bigl[\bigl[\mathsf{M}_2(\tilde P),\mathsf{M}_2(\tilde Q)\bigr],\mathsf{M}_2(\tilde R)\bigr],
$$

and the Lie algebra it makes of the trace-free matrices is $\mathfrak{sl}(2,\mathbb{C})$, of complex dimension three.

*Proof.* The bracket is the commutator of the associative matrix product, which satisfies the Jacobi identity as the expansion of the associativity, *Associative Algebras*; the halving carries the identity unchanged on each side. Verified on the model. $\square$

## The Trace Form and the Killing Form

**Theorem (the trace form is the Killing form).** On the derived algebra,

$$
\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)\bigr)=\kappa(\tilde P,\tilde Q)=-2\,\mathbf{P}\cdot\mathbf{Q}\qquad(\tilde P,\tilde Q\in\mathrm{Vect}(\mathbb{B})),
$$

so the trace form of the two-dimensional model is the Killing form of the block.

*Proof.* With $\mathsf{M}_2(\tilde P)=-i\,\mathbf{P}\cdot\sigma$ and $\mathsf{M}_2(\tilde Q)=-i\,\mathbf{Q}\cdot\sigma$ one has $\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)=-(\mathbf{P}\cdot\sigma)(\mathbf{Q}\cdot\sigma)=-(\mathbf{P}\cdot\mathbf{Q})\mathrm{I}_2-i(\mathbf{P}\times\mathbf{Q})\cdot\sigma$, whose trace is $-2\,\mathbf{P}\cdot\mathbf{Q}$ because the Pauli matrices are trace-free; this is the formula of *The Killing Form of the Antisymmetric Plain Algebra*. Verified on general elements. $\square$

**Remark (the two objects of the block).** The model is the smallest faithful representation of the derived algebra, of complex dimension two, and its trace form is the invariant form itself: **the two objects of the block, the bracket and the form, are in this model the commutator and the trace. The identification is the reason the block is called the Lie block.** The scalar matrices, the kernel, are the centre; the trace-free matrices, the image, are the derived algebra; and the two are the two-dimensional model of the decomposition $\mathbb{B}=\mathbb{C}_{\mathbb{B}}\oplus\mathrm{Vect}(\mathbb{B})$.

## Worked Examples

**A bracket of two units, in matrices.** $\mathsf{M}_2(e_1)=\begin{pmatrix}0&-i\\-i&0\end{pmatrix}$, $\mathsf{M}_2(e_2)=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ and $\tfrac12[\mathsf{M}_2(e_1),\mathsf{M}_2(e_2)]=\mathsf{M}_2(e_3)=\begin{pmatrix}-i&0\\0&i\end{pmatrix}$: the halved commutator in the two-dimensional model.

**The trace.** $\operatorname{Tr}\mathsf{M}_2(e_1)=0$ and $\operatorname{Tr}\mathsf{M}_2(e_0)=2$: the vector part is trace-free, the centre is the trace direction, split in two.

**A scalar matrix.** $\mathsf{M}_2(ie_0)=i\mathrm{I}_2$, and $\mathsf{M}_2(ie_0\wedge e_1)=0$: the central element is the scalar matrix, and it is in the kernel of the bracket.

**The trace form.** $\operatorname{Tr}(\mathsf{M}_2(e_1)\mathsf{M}_2(e_2))=0$ and $\operatorname{Tr}(\mathsf{M}_2(e_1)\mathsf{M}_2(e_1))=-2$: the trace form on the trace-free matrices is the Gram matrix $\operatorname{diag}(-2,-2,-2)$, the Killing form of the block.

## The Matrices

**The generators.** The realization is fixed on the basis by four matrices:

$$
\mathsf{M}_2(e_0)=\begin{pmatrix}1&0\\0&1\end{pmatrix},\qquad
\mathsf{M}_2(e_1)=\begin{pmatrix}0&-i\\-i&0\end{pmatrix},\qquad
\mathsf{M}_2(e_2)=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
\mathsf{M}_2(e_3)=\begin{pmatrix}-i&0\\0&i\end{pmatrix}.
$$

and on a general element by the matrix $\mathsf{M}_2(\tilde Q)$ of trace $2Q_0$ and determinant $N(\tilde Q)$.

**The bracket, entry by entry.** The cross-product relation $\tilde P\wedge\tilde Q$ is the halved commutator, and on the pair of units $e_1,e_2$ it is the matrix identity

$$
\tfrac12\bigl[\mathsf{M}_2(e_1),\mathsf{M}_2(e_2)\bigr]
=\tfrac12\left(
\begin{pmatrix}0&-i\\-i&0\end{pmatrix}\begin{pmatrix}0&-1\\1&0\end{pmatrix}
-\begin{pmatrix}0&-1\\1&0\end{pmatrix}\begin{pmatrix}0&-i\\-i&0\end{pmatrix}
\right)
=\tfrac12\begin{pmatrix}-2i&0\\0&2i\end{pmatrix}
=\begin{pmatrix}-i&0\\0&i\end{pmatrix}=\mathsf{M}_2(e_3),
$$

which is $e_1\wedge e_2=e_3$ read in the entries.

**The image, entry by entry.** The bracket is pure vector, so every value is traceless in the model: $\operatorname{Tr}\mathsf{M}_2(e_3)=(-i)+(i)=0$, and the image is the space of traceless matrices, of complex dimension three, that is $\mathfrak{sl}(2,\mathbb{C})$; the image is the two-dimensional module on which the Casimir acts by the scalar $\tfrac38$ of *The Killing Form of the Antisymmetric Plain Algebra*.

## Summary

In the two-dimensional model $\mathbb{B}\cong M_2(\mathbb{C})$ the antisymmetric plain algebra is the halved commutator $\mathsf{M}_2(\tilde P\wedge\tilde Q)=\tfrac12[\mathsf{M}_2(\tilde P),\mathsf{M}_2(\tilde Q)]$, with image the trace-free matrices, identified with $\mathfrak{sl}(2,\mathbb{C})$ and with the derived algebra, and kernel the scalar matrices, identified with the centre; the trace form of the model is the Killing form of the block, $\kappa(\tilde P,\tilde Q)=\operatorname{Tr}(\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q))=-2\,\mathbf{P}\cdot\mathbf{Q}$ on the derived algebra. The model identifies the derived algebra with $\mathfrak{sl}(2,\mathbb{C})$ as its defining representation, and it exhibits the decomposition $\mathbb{B}=\mathbb{C}_{\mathbb{B}}\oplus\mathrm{Vect}(\mathbb{B})$ as a kernel and an image.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ | the two-dimensional model, $\mathsf{M}_2(e_k)=-i\sigma_k$, $\mathsf{M}_2(ie_0)=i\mathrm{I}_2$ |
| $\mathsf{M}_2(\tilde P\wedge\tilde Q)=\tfrac12[\mathsf{M}_2(\tilde P),\mathsf{M}_2(\tilde Q)]$ | the bracket as the halved matrix commutator |
| $\mathsf{M}_2(\mathrm{Vect}(\mathbb{B}))=\{X:\operatorname{Tr}X=0\}\cong\mathfrak{sl}(2,\mathbb{C})$ | the image, the derived algebra |
| $\ker\wedge=\mathsf{M}_2^{-1}(\mathbb{C}\mathrm{I}_2)=\mathbb{C}_{\mathbb{B}}$ | the kernel, the centre |
| $\operatorname{Tr}(\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q))=\kappa(\tilde P,\tilde Q)$ | the trace form is the Killing form on the derived algebra |

## Further Reading

- *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* (`articles_maths/introduction-to-the-2x2-matrix-element-representation-of-biquaternions.md`), for the construction of the model
- *The General Plain Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/the-general-plain-algebra-in-the-2x2-matrix-element-representation.md`), for the plain product in the model
- *The Antisymmetric Plain Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$* (`articles_maths/the-antisymmetric-plain-algebra-in-the-4x4-matrix-element-representation.md`), for the reading on the regular model and its adjoint representation
- *Introduction to the Antisymmetric Plain Algebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-plain-algebra-of-biquaternions.md`), for the bracket and the cross-product formula
- *The Lie Algebra of the Antisymmetric Plain Algebra* (`articles_maths/the-lie-algebra-of-the-antisymmetric-plain-algebra.md`), for the centre, the derived algebra and the identification with $\mathfrak{sl}(2,\mathbb{C})$
- *The Killing Form of the Antisymmetric Plain Algebra* (`articles_maths/the-killing-form-of-the-antisymmetric-plain-algebra.md`), for the invariant form and its constant relation to the plain form
