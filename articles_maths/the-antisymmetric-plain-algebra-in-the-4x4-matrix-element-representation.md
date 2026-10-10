# __The Antisymmetric Plain Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$__

## Introduction

The antisymmetric plain algebra, $\tilde P\wedge\tilde Q=\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)=\mathbf{P}\times\mathbf{Q}$, is read here in the $4\times4$ regular model of the chapter of the general plain algebra: the four-dimensional regular model, in which the bracket is the halved commutator of the left multiplication operators and, through the adjoint representation, a six-dimensional real matrix model. This article is the second of the two representation articles of the block, and its companion *The Antisymmetric Plain Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* reads the same bracket in the two-dimensional model.

The model gives the operator identity $\mathsf{M}_4(\tilde P\wedge\tilde Q)=\tfrac12[\mathsf{M}_4(\tilde P),\mathsf{M}_4(\tilde Q)]$ and, for the adjoint representation, the six-dimensional real matrices of the adjoints, with their invariants: vanishing trace, vanishing determinant, rank four and the characteristic polynomial $\lambda^2(\lambda^2+4)^2$ at the real units. The model is identified with the Lie algebra of the derived algebra.

The model is *The General Plain Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$*, and its construction is *Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions*. The bracket, its structure and its adjoints are used from *Introduction to the Antisymmetric Plain Algebra of Biquaternions*, *The Lie Algebra of the Antisymmetric Plain Algebra*, *The Killing Form of the Antisymmetric Plain Algebra* and *The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra*; the left and the right multiplication operators of the plain product are *One-Sided Operators on the General Plain Algebra of Biquaternions* and *Two-Sided Operators on the General Plain Algebra of Biquaternions*; and the identification of the trace-free matrices with $\mathfrak{sl}(2,\mathbb{C})$ is *Structure of Lie Algebras*. The model is an algebra morphism, and no analytic notion is read on it.

## The Regular Operator and the Bracket

**Theorem (the bracket as the halved commutator of the operators).** Let $L:\mathbb{B}\to\operatorname{End}(\mathbb{B})$ be the left regular representation, $L_{\tilde P}(\tilde X)=\tilde P\tilde X$. Then

$$
\mathsf{M}_4(\tilde P\wedge\tilde Q)=\tfrac12\bigl[\mathsf{M}_4(\tilde P),\mathsf{M}_4(\tilde Q)\bigr],
$$

and the image of $\mathsf{M}_4$ is a commutative algebra of operators isomorphic to $\mathbb{B}$.

*Proof.* The left multiplication is multiplicative, $\mathsf{M}_4(\tilde P\tilde Q)=\mathsf{M}_4(\tilde P)\mathsf{M}_4(\tilde Q)$, because the product is associative; the commutator of the two operators is therefore $\mathsf{M}_4(\tilde P\tilde Q-\tilde Q\tilde P)$, and half of it is $\mathsf{M}_4$ applied to the half-difference, the bracket. The image is an algebra because $\mathsf{M}_4$ is an algebra morphism with kernel zero. This is the four-dimensional model of *The General Plain Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$*. Verified on the basis. $\square$

**Remark (the model of the two-sided operators).** The regular model realises the bracket as the commutator of the multiplication operators, and it is the model in which the adjoint of the block is seen as a commutator: by the same computation $\operatorname{ad}_{\tilde P}=\mathsf{M}_4(\tilde P)-\mathsf{M}_4^{R}(\tilde P)$, the difference of the left and the right multiplication, which is *Two-Sided Operators on the General Plain Algebra of Biquaternions*. **The four-dimensional model is thus the model of the two-sided operators, and the antisymmetric plain algebra is the half of their commutator.**

## The Adjoint Representation as a Six-Dimensional Real Model

**Theorem (the adjoint representation).** The adjoint representation of the derived algebra restricts to the vector subspace and is a morphism of real Lie algebras for the commutator, $\operatorname{ad}_{[\tilde P,\tilde Q]}=[\operatorname{ad}_{\tilde P},\operatorname{ad}_{\tilde Q}]$,

$$
\operatorname{ad}:\mathrm{Vect}(\mathbb{B})\to M_6(\mathbb{R}),\qquad
\operatorname{ad}_{\tilde P}\longmapsto \bigl(\text{the matrix of }\tilde X\mapsto[\tilde P,\tilde X]=2\,(\mathbf{P}\times\mathbf{X})\bigr)
$$

in the real basis $(e_1,e_2,e_3,ie_1,ie_2,ie_3)$, with kernel zero, so that the image is $\mathfrak{sl}(2,\mathbb{C})$ read as a six-dimensional real Lie algebra. The matrix of $\operatorname{ad}_{e_1}$ is

$$
\operatorname{ad}_{e_1}=
\begin{pmatrix}
0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & -2 & 0 & 0 & 0\\
0 & 2 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & -2\\
0 & 0 & 0 & 0 & 2 & 0
\end{pmatrix},
$$

and the matrix of $\operatorname{ad}_{ie_1}$ is the realification of the complex-linear operator $2iC_{e_1}$: its two diagonal $3\times3$ blocks are zero and its two off-diagonal blocks are the block of $\operatorname{ad}_{e_1}$ with opposite signs.

*Proof.* The adjoint is twice the cross product by the vector part, and it preserves the vector subspace and kills the centre, so in the real basis it has the displayed block form; the images of the basis vectors give the columns, as recomputed in *The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra*. The kernel on the derived algebra is zero because the centre is the whole kernel of the adjoint and the centre meets the derived algebra only at zero. The image is the adjoint algebra, identified with the derived algebra and hence with $\mathfrak{sl}(2,\mathbb{C})$. Verified on the real basis. $\square$

**Theorem (the invariants).** Every nonzero matrix of the six-dimensional real model has vanishing trace, rank $4$ and vanishing determinant, and its characteristic polynomial is

$$
\lambda^2\bigl(\lambda^2+4\,\mathbf{P}\cdot\mathbf{P}\bigr)\bigl(\lambda^2+4\,\overline{\mathbf{P}\cdot\mathbf{P}}\bigr).
$$

On the real vector directions, where $\mathbf{P}\cdot\mathbf{P}$ is real, this is $\lambda^2(\lambda^2+4\,\mathbf{P}\cdot\mathbf{P})^2$; at the real units, and in particular for the displayed matrix of $\operatorname{ad}_{e_1}$, it is $\lambda^2(\lambda^2+4)^2$, with the eigenvalues $0$, of multiplicity two, and $\pm2i$, of multiplicity two each, and the minimal polynomial $\lambda(\lambda^2+4)$; at $\operatorname{ad}_{ie_1}$, where $\mathbf{P}\cdot\mathbf{P}=-1$, it is $\lambda^2(\lambda^2-4)^2$.

The trace form of the model is read on the real six-dimensional space, where the trace is real, so that it is eight times the realification of the form of the block,

$$
\operatorname{Tr}\bigl(\operatorname{ad}_{\tilde P}\operatorname{ad}_{\tilde Q}\bigr)=8\,\operatorname{Re}\kappa(\tilde P,\tilde Q)=-16\,\operatorname{Re}(\mathbf{P}\cdot\mathbf{Q}),
$$

with Gram matrix $\operatorname{diag}(-16,-16,-16,16,16,16)$ in the real basis $(e_1,e_2,e_3,ie_1,ie_2,ie_3)$, negative on the real vector directions and positive on the imaginary ones. The factor eight is the square of the factor two that relates the adjoint $[\tilde P,\cdot]$ of the block to its halved adjoint $\tilde P\wedge\cdot$, times the factor two by which the real trace doubles the real part of the complex trace; the complex trace of the same adjoints, read before realification, is the $4\kappa$ of *The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra*.

*Proof.* The complex three-dimensional operator of the adjoint is $2C_{\mathbf{P}}$; the cross-product matrix satisfies $C_{\mathbf{P}}^2=\mathbf{P}\mathbf{P}^{\mathsf T}-(\mathbf{P}\cdot\mathbf{P})\mathrm{I}_3$, so its characteristic polynomial is $\lambda(\lambda^2+\mathbf{P}\cdot\mathbf{P})$ and that of $2C_{\mathbf{P}}$ is $\lambda(\lambda^2+4\,\mathbf{P}\cdot\mathbf{P})$; the realification replaces each complex eigenvalue by the pair formed with its conjugate, so the characteristic polynomial of the real $6\times6$ matrix is $\lambda^2(\lambda^2+4\,\mathbf{P}\cdot\mathbf{P})(\lambda^2+4\,\overline{\mathbf{P}\cdot\mathbf{P}})$, which at the real units is $\lambda^2(\lambda^2+4)^2$. The trace is the sum of the eigenvalues, which is zero, and the determinant the product, which is zero because of the eigenvalue $0$; the rank is four because the kernel of the adjoint on the derived algebra is the complex line $\mathbb{C}\mathbf{P}$, of real dimension two. For the trace form, the complex trace of the square of the adjoint is four times the complex trace of the square of the halved adjoint, that is $4\kappa=-8\,\mathbf{P}\cdot\mathbf{Q}$, and the realification of a complex-linear endomorphism doubles the real part of its trace, so the real trace of the square is $2\operatorname{Re}(-8\,\mathbf{P}\cdot\mathbf{Q})=-16\operatorname{Re}(\mathbf{P}\cdot\mathbf{Q})=8\operatorname{Re}\kappa(\tilde P,\tilde Q)$. Verified on the real basis. $\square$

**Remark (the realification of the complex adjoint).** **The six-dimensional real model is the realification of the three-dimensional complex adjoint, and its three invariants — trace, determinant and rank — are the three invariants of a model of $\mathfrak{sl}(2,\mathbb{C})$ in real form.** The vanishing trace is the vanishing of the trace of every adjoint; the vanishing determinant and the rank four are the statement that the kernel is a complex line; and the eigenvalues are those of the complex cross-product operator, doubled by the realification. The same matrices with the centre restored are the matrices of the adjoints of the whole block, read in *The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra*.

## Worked Examples

**A regular operator.** $\mathsf{M}_4(e_1\wedge e_2)=\mathsf{M}_4(e_3)$ and $\tfrac12[\mathsf{M}_4(e_1),\mathsf{M}_4(e_2)]=\mathsf{M}_4(e_3)$: the operator identity of the four-dimensional model, on the pair of the first two units.

**The six-dimensional matrix.** The matrix of $\operatorname{ad}_{e_1}$ displayed above has $\operatorname{Tr}=0$, $\det=0$ and rank $4$; the matrix of $\operatorname{ad}_{ie_1}$ is the realification of $2iC_{e_1}$, with zero diagonal $3\times3$ blocks and the block of $\operatorname{ad}_{e_1}$ in the two off-diagonal positions with opposite signs, and it has the same vanishing trace, vanishing determinant and rank.

**The characteristic polynomial.** $\lambda^2(\lambda^2+4)^2$ for the matrix of $\operatorname{ad}_{e_1}$: the eigenvalues $0$ twice and $\pm2i$ twice each, the imaginary eigenvalues of the cross product doubled by the realification. For $\operatorname{ad}_{ie_1}$, where $\mathbf{P}\cdot\mathbf{P}=-1$, the same count gives $\lambda^2(\lambda^2-4)^2$: the characteristic polynomial depends on $\mathbf{P}\cdot\mathbf{P}$.

**The trace form in the model.** $\operatorname{Tr}(\operatorname{ad}_{e_1}\operatorname{ad}_{e_1})=-16$ and $\operatorname{Tr}(\operatorname{ad}_{ie_1}\operatorname{ad}_{ie_1})=16$, while $\operatorname{Tr}(\operatorname{ad}_{e_1}\operatorname{ad}_{ie_1})=0$: the model's trace form is eight times the realification of the form of the block, of Gram matrix $\operatorname{diag}(-16,-16,-16,16,16,16)$, as the theorem states.

## The Matrices

**The generators.** The regular model is fixed on the basis by four matrices:

$$
\mathsf{M}_4(e_0)=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},\qquad
\mathsf{M}_4(e_1)=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},
$$
$$
\mathsf{M}_4(e_2)=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix},\qquad
\mathsf{M}_4(e_3)=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&1&0&0\\1&0&0&0\end{pmatrix}.
$$

A general element is the block matrix

$$
\mathsf{M}_4(\tilde Q)=\begin{pmatrix}A&B\\-B&A\end{pmatrix},\qquad
A=\begin{pmatrix}Q_0&-Q_1\\Q_1&Q_0\end{pmatrix},\qquad
B=\begin{pmatrix}-Q_2&-Q_3\\-Q_3&Q_2\end{pmatrix},
$$

and the derived algebra is the image of the pure-vector subspace.

**The bracket, entry by entry.** The bracket is the halved commutator, and on the pair of units $e_1,e_2$ it is the matrix identity

$$
\tfrac12\bigl[\mathsf{M}_4(e_1),\mathsf{M}_4(e_2)\bigr]
=\tfrac12\bigl(\mathsf{M}_4(e_3)-\mathsf{M}_4(-e_3)\bigr)=\mathsf{M}_4(e_3),
$$

since $\mathsf{M}_4(e_1)\mathsf{M}_4(e_2)=\mathsf{M}_4(e_3)$ and $\mathsf{M}_4(e_2)\mathsf{M}_4(e_1)=-\mathsf{M}_4(e_3)$. On the generators that is the whole computation: the model is multiplicative, so the bracket of two regular matrices is the regular matrix of the bracket.

**The image, entry by entry.** The bracket is pure vector, so every value is a **traceless skew-symmetric** regular matrix: the vector part satisfies $\tilde Q^{\natural}=-\tilde Q$, hence $\mathsf{M}_4(\tilde Q)^{\mathsf T}=\mathsf{M}_4(\tilde Q^{\natural})=-\mathsf{M}_4(\tilde Q)$, and the trace, which is four times the scalar part, vanishes. For instance $\mathsf{M}_4(e_3)=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&1&0&0\\1&0&0&0\end{pmatrix}$ is skew-symmetric of trace zero. The image is therefore the space of traceless skew-symmetric regular matrices, of complex dimension three, identified with the derived algebra $\mathfrak{sl}(2,\mathbb{C})$.

## Summary

In the four-dimensional regular model the bracket is the halved commutator of the left multiplication operators, $\mathsf{M}_4(\tilde P\wedge\tilde Q)=\tfrac12[\mathsf{M}_4(\tilde P),\mathsf{M}_4(\tilde Q)]$, and the adjoint representation is a six-dimensional real matrix model with kernel zero on the derived algebra and image $\mathfrak{sl}(2,\mathbb{C})$, every nonzero matrix of which has vanishing trace, vanishing determinant and rank $4$, with characteristic polynomial $\lambda^2(\lambda^2+4\,\mathbf{P}\cdot\mathbf{P})(\lambda^2+4\,\overline{\mathbf{P}\cdot\mathbf{P}})$ — equal to $\lambda^2(\lambda^2+4)^2$, with minimal polynomial $\lambda(\lambda^2+4)$, at the real units; the trace form of the model is eight times the realification of the form of the block, of Gram matrix $\operatorname{diag}(-16,-16,-16,16,16,16)$. The model identifies the derived algebra with $\mathfrak{sl}(2,\mathbb{C})$ as its adjoint representation, and it exhibits the decomposition $\mathbb{B}=\mathbb{C}_{\mathbb{B}}\oplus\mathrm{Vect}(\mathbb{B})$ as a kernel and an image.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_4(\tilde P\wedge\tilde Q)=\tfrac12[\mathsf{M}_4(\tilde P),\mathsf{M}_4(\tilde Q)]$ | the bracket in the four-dimensional regular model |
| $\operatorname{ad}:\mathrm{Vect}(\mathbb{B})\to M_6(\mathbb{R})$ | the six-dimensional real model of the adjoint |
| $\operatorname{Tr}=0$, $\det=0$, rank $4$ | the invariants of every nonzero matrix of the model |
| $\lambda^2(\lambda^2+4\,\mathbf{P}\cdot\mathbf{P})(\lambda^2+4\,\overline{\mathbf{P}\cdot\mathbf{P}})$ | the characteristic polynomial of the matrix of $\operatorname{ad}_{\tilde P}$, equal to $\lambda^2(\lambda^2+4)^2$ at the real units |
| $\operatorname{Tr}(\operatorname{ad}_{\tilde P}\operatorname{ad}_{\tilde Q})=8\operatorname{Re}\kappa(\tilde P,\tilde Q)$ | the trace form of the model, eight times the realification of the form of the block |

## Further Reading

- *Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions* (`articles_maths/introduction-to-the-4x4-matrix-element-representation-of-biquaternions.md`), for the construction of the model
- *The General Plain Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$* (`articles_maths/the-general-plain-algebra-in-the-4x4-matrix-element-representation.md`), for the plain product in the model
- *One-Sided Operators on the General Plain Algebra of Biquaternions* (`articles_maths/one-sided-operators-on-the-general-plain-algebra-of-biquaternions.md`) and *Two-Sided Operators on the General Plain Algebra of Biquaternions* (`articles_maths/two-sided-operators-on-the-general-plain-algebra-of-biquaternions.md`), for the left and right multiplication operators
- *The Antisymmetric Plain Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/the-antisymmetric-plain-algebra-in-the-2x2-matrix-element-representation.md`), for the reading on the two-dimensional model
- *Introduction to the Antisymmetric Plain Algebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-plain-algebra-of-biquaternions.md`), for the bracket and the cross-product formula
- *The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra* (`articles_maths/the-adjoint-operators-and-the-derivations-of-the-antisymmetric-plain-algebra.md`), for the adjoints, their matrices in the real basis and the derivations
