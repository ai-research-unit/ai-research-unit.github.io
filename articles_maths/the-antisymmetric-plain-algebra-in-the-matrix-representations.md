# __The Antisymmetric Plain Algebra in the Matrix Representations__

## Introduction

The antisymmetric plain algebra, $\tilde P\wedge\tilde Q=\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)=\mathbf{P}\times\mathbf{Q}$, is read here in the two matrix models of the chapter of the general plain algebra: the two-dimensional model $\mathbb{B}\cong M_2(\mathbb{C})$, in which it is the halved commutator of the matrix product, and the four-dimensional regular model, in which it is the halved commutator of the left multiplication operators and, through the adjoint representation, a six-dimensional real matrix model.

The first model turns the bracket into the halved commutator $\tfrac12(XY-YX)$ of two by two complex matrices, and the whole block is read off the two standard facts about the matrix commutator: **its image is the trace-free matrices, of complex dimension three, and its kernel is the scalar matrices, of complex dimension one.** The image is the derived algebra $\mathrm{Vect}(\mathbb{B})$, identified with $\mathfrak{sl}(2,\mathbb{C})$; the kernel is the centre $\mathbb{C}_{\mathbb{B}}$; and the trace form of the model is the Killing form of the block, $\kappa(\tilde P,\tilde Q)=\operatorname{Tr}(\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q))$ on the derived algebra. The second model gives the operator identity $\mathsf{M}_4(\tilde P\wedge\tilde Q)=\tfrac12[\mathsf{M}_4(\tilde P),\mathsf{M}_4(\tilde Q)]$ and, for the adjoint representation, the six-dimensional real matrices of the adjoints, with their invariants: vanishing trace, vanishing determinant, rank four and the characteristic polynomial $\lambda^2(\lambda^2+4)^2$ at the real units. Both models are then identified with the Lie algebra of the derived algebra.

The two models are *The General Plain Algebra in the $2\times2$ Matrix Representation* and *The General Plain Algebra in the $4\times4$ Matrix Representation*, and their construction is *Introduction to the 2×2 Matrix Representation of Biquaternions* and *Introduction to the 4×4 Matrix Representation $M_4(\mathbb{C})_L$ of Biquaternions*. The bracket, its structure and its adjoints are used from *Introduction to the Antisymmetric Plain Algebra of Biquaternions*, *The Lie Algebra of the Antisymmetric Plain Algebra*, *The Killing Form of the Antisymmetric Plain Algebra* and *The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra*; the left and the right multiplication operators of the plain product are *One-Sided Operators on the General Plain Algebra of Biquaternions* and *Two-Sided Operators on the General Plain Algebra of Biquaternions*; and the identification of the trace-free matrices with $\mathfrak{sl}(2,\mathbb{C})$ is *Structure of Lie Algebras*. The two models are algebra isomorphisms, and no analytic notion is read on them.

## The Two-Dimensional Model

### The Model

**Theorem (the defining representation).** There is a $\mathbb{C}$-algebra isomorphism $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ with

$$
\mathsf{M}_2(e_0)=\mathrm{I}_2,\qquad \mathsf{M}_2(e_1)=-i\sigma_1,\qquad \mathsf{M}_2(e_2)=-i\sigma_2,\qquad \mathsf{M}_2(e_3)=-i\sigma_3,
$$

where $\sigma_1,\sigma_2,\sigma_3$ are the Pauli matrices, and with $\mathsf{M}_2(i\tilde P)=i\mathsf{M}_2(\tilde P)$; explicitly

$$
\mathsf{M}_2(\tilde Q)=
\begin{pmatrix}
Q_0-iQ_3 & -iQ_1-Q_2\\
-iQ_1+Q_2 & Q_0+iQ_3
\end{pmatrix},
\qquad \operatorname{Tr}\mathsf{M}_2(\tilde Q)=2Q_0.
$$

*Proof.* The assignments are $\mathbb{C}$-linear and send $e_0$ to the identity; the products of the images reproduce the quaternion relations, $(-i\sigma_1)(-i\sigma_2)=-\sigma_1\sigma_2=-i\sigma_3$, since $\sigma_1\sigma_2=i\sigma_3$. The displayed matrix is the expansion, and its trace is $2Q_0$ because the Pauli matrices are trace-free. This is the model of *Introduction to the 2×2 Matrix Representation of Biquaternions*. Verified on the sixteen products of the basis. $\square$

### The Bracket as the Halved Commutator

**Theorem.** For all $\tilde P,\tilde Q\in\mathbb{B}$,

$$
\mathsf{M}_2(\tilde P\wedge\tilde Q)=\tfrac12\bigl[\mathsf{M}_2(\tilde P),\mathsf{M}_2(\tilde Q)\bigr],
$$

and the image of the block is the subspace of the trace-free matrices, while its kernel is the subspace of the scalar matrices:

$$
\mathsf{M}_2\bigl(\mathrm{Vect}(\mathbb{B})\bigr)=\{X\in M_2(\mathbb{C}):\operatorname{Tr}X=0\},\qquad
\ker\wedge=\mathsf{M}_2^{-1}(\mathbb{C}\,\mathrm{I}_2)=\mathbb{C}_{\mathbb{B}}.
$$

*Proof.* The model is an algebra isomorphism, so $\mathsf{M}_2(\tilde P\tilde Q-\tilde Q\tilde P)=[\mathsf{M}_2(\tilde P),\mathsf{M}_2(\tilde Q)]$ and half of it is the image of the bracket. An element of the vector subspace has $Q_0=0$ and image of trace zero, and conversely a trace-free matrix has the second coefficient $Q_0$ zero, so it is the image of a vector element; the kernel of the bracket is the centre by *The Lie Algebra of the Antisymmetric Plain Algebra*, and its image under $\mathsf{M}_2$ is the scalar matrices, because $\operatorname{Tr}\mathsf{M}_2(\tilde Q)=2Q_0$ vanishes exactly on the vector subspace. Computed exactly on general elements. $\square$

**Remark (the block is the matrix commutator).** **The antisymmetric plain algebra is, in this model, the halved commutator of the two by two complex matrices, its image is $\mathfrak{sl}(2,\mathbb{C})$ and its kernel is the centre.** The scalar part of the biquaternion is the trace of the matrix, split in two, and the bracket annihilates it; the vector part is the trace-free part, of complex dimension three, and the bracket is the commutator there. The trace-free matrices with the commutator are the Lie algebra $\mathfrak{sl}(2,\mathbb{C})$ of *Structure of Lie Algebras*, and the block's halved bracket is the same Lie algebra under the rescaling $\tilde P\mapsto2\tilde P$.

### The Lie Algebra and the Trace Form

**Theorem.** The bracket on the trace-free matrices is a Lie bracket, of which the model satisfies the identity

$$
\bigl[\mathsf{M}_2(\tilde P\wedge\tilde Q),\mathsf{M}_2(\tilde R)\bigr]=\tfrac12\bigl[\bigl[\mathsf{M}_2(\tilde P),\mathsf{M}_2(\tilde Q)\bigr],\mathsf{M}_2(\tilde R)\bigr],
$$

and the Lie algebra it makes of the trace-free matrices is $\mathfrak{sl}(2,\mathbb{C})$, of complex dimension three.

*Proof.* The bracket is the commutator of the associative matrix product, which satisfies the Jacobi identity as the expansion of the associativity, *Associative Algebras*; the halving carries the identity unchanged on each side. $\square$

**Theorem (the trace form is the Killing form).** On the derived algebra,

$$
\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)\bigr)=\kappa(\tilde P,\tilde Q)=-2\,\mathbf{P}\cdot\mathbf{Q}\qquad(\tilde P,\tilde Q\in\mathrm{Vect}(\mathbb{B})),
$$

so the trace form of the two-dimensional model is the Killing form of the block.

*Proof.* With $\mathsf{M}_2(\tilde P)=-i\,\mathbf{P}\cdot\sigma$ and $\mathsf{M}_2(\tilde Q)=-i\,\mathbf{Q}\cdot\sigma$ one has $\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)=-(\mathbf{P}\cdot\sigma)(\mathbf{Q}\cdot\sigma)=-(\mathbf{P}\cdot\mathbf{Q})\mathrm{I}_2-i(\mathbf{P}\times\mathbf{Q})\cdot\sigma$, whose trace is $-2\,\mathbf{P}\cdot\mathbf{Q}$ because the Pauli matrices are trace-free; this is the formula of *The Killing Form of the Antisymmetric Plain Algebra*. Computed exactly on general elements. $\square$

**Remark.** The model is the smallest faithful representation of the derived algebra, of complex dimension two, and its trace form is the invariant form itself: **the two objects of the block, the bracket and the form, are in this model the commutator and the trace. The identification is the reason the block is called the Lie block.** The scalar matrices, the kernel, are the centre; the trace-free matrices, the image, are the derived algebra; and the two are the two-dimensional model of the decomposition $\mathbb{B}=\mathbb{C}_{\mathbb{B}}\oplus\mathrm{Vect}(\mathbb{B})$.

## The Four-Dimensional Regular Model

### The Regular Operator and the Bracket

**Theorem.** Let $L:\mathbb{B}\to\operatorname{End}(\mathbb{B})$ be the left regular representation, $L_{\tilde P}(\tilde X)=\tilde P\tilde X$. Then

$$
\mathsf{M}_4(\tilde P\wedge\tilde Q)=\tfrac12\bigl[\mathsf{M}_4(\tilde P),\mathsf{M}_4(\tilde Q)\bigr],
$$

and the image of $\mathsf{M}_4$ is a commutative algebra of operators isomorphic to $\mathbb{B}$.

*Proof.* The left multiplication is multiplicative, $\mathsf{M}_4(\tilde P\tilde Q)=\mathsf{M}_4(\tilde P)\mathsf{M}_4(\tilde Q)$, because the product is associative; the commutator of the two operators is therefore $\mathsf{M}_4(\tilde P\tilde Q-\tilde Q\tilde P)$, and half of it is $\mathsf{M}_4$ applied to the half-difference, the bracket. The image is an algebra because $\mathsf{M}_4$ is an algebra morphism with kernel zero. This is the four-dimensional model of *The General Plain Algebra in the $4\times4$ Matrix Representation*. Computed on the basis. $\square$

**Remark.** The regular model realises the bracket as the commutator of the multiplication operators, and it is the model in which the adjoint of the block is seen as a commutator: by the same computation $\operatorname{ad}_{\tilde P}=\mathsf{M}_4(\tilde P)-\mathsf{M}_4^{R}(\tilde P)$, the difference of the left and the right multiplication, which is *Two-Sided Operators on the General Plain Algebra of Biquaternions*. **The four-dimensional model is thus the model of the two-sided operators, and the antisymmetric plain algebra is the half of their commutator.**

### The Adjoint Representation as a Six-Dimensional Real Model

**Theorem.** The adjoint representation of the derived algebra restricts to the vector subspace and is a morphism of real Lie algebras for the commutator, $\operatorname{ad}_{[\tilde P,\tilde Q]}=[\operatorname{ad}_{\tilde P},\operatorname{ad}_{\tilde Q}]$,

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

*Proof.* The adjoint is twice the cross product by the vector part, and it preserves the vector subspace and kills the centre, so in the real basis it has the displayed block form; the images of the basis vectors give the columns, as recomputed in *The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra*. The kernel on the derived algebra is zero because the centre is the whole kernel of the adjoint and the centre meets the derived algebra only at zero. The image is the adjoint algebra, identified with the derived algebra and hence with $\mathfrak{sl}(2,\mathbb{C})$. Computed exactly on the real basis. $\square$

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

*Proof.* The complex three-dimensional operator of the adjoint is $2C_{\mathbf{P}}$; the cross-product matrix satisfies $C_{\mathbf{P}}^2=\mathbf{P}\mathbf{P}^{\mathsf T}-(\mathbf{P}\cdot\mathbf{P})\mathrm{I}_3$, so its characteristic polynomial is $\lambda(\lambda^2+\mathbf{P}\cdot\mathbf{P})$ and that of $2C_{\mathbf{P}}$ is $\lambda(\lambda^2+4\,\mathbf{P}\cdot\mathbf{P})$; the realification replaces each complex eigenvalue by the pair formed with its conjugate, so the characteristic polynomial of the real $6\times6$ matrix is $\lambda^2(\lambda^2+4\,\mathbf{P}\cdot\mathbf{P})(\lambda^2+4\,\overline{\mathbf{P}\cdot\mathbf{P}})$, which at the real units is $\lambda^2(\lambda^2+4)^2$. The trace is the sum of the eigenvalues, which is zero, and the determinant the product, which is zero because of the eigenvalue $0$; the rank is four because the kernel of the adjoint on the derived algebra is the complex line $\mathbb{C}\mathbf{P}$, of real dimension two. For the trace form, the complex trace of the square of the adjoint is four times the complex trace of the square of the halved adjoint, that is $4\kappa=-8\,\mathbf{P}\cdot\mathbf{Q}$, and the realification of a complex-linear endomorphism doubles the real part of its trace, so the real trace of the square is $2\operatorname{Re}(-8\,\mathbf{P}\cdot\mathbf{Q})=-16\operatorname{Re}(\mathbf{P}\cdot\mathbf{Q})=8\operatorname{Re}\kappa(\tilde P,\tilde Q)$. Computed exactly in the real basis. $\square$

**Remark.** **The six-dimensional real model is the realification of the three-dimensional complex adjoint, and its three invariants — trace, determinant and rank — are the three invariants of a model of $\mathfrak{sl}(2,\mathbb{C})$ in real form.** The vanishing trace is the vanishing of the trace of every adjoint; the vanishing determinant and the rank four are the statement that the kernel is a complex line; and the eigenvalues are those of the complex cross-product operator, doubled by the realification. The same matrices with the centre restored are the matrices of the adjoints of the whole block, read in *The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra*.

## The Identification of the Two Models

**Theorem.** Both models identify the derived algebra with $\mathfrak{sl}(2,\mathbb{C})$:

$$
\mathsf{M}_2\bigl(\mathrm{Vect}(\mathbb{B})\bigr)=\mathfrak{sl}(2,\mathbb{C}),\qquad
\operatorname{ad}\bigl(\mathrm{Vect}(\mathbb{B})\bigr)\cong\mathfrak{sl}(2,\mathbb{C}),
$$

the first as the trace-free matrices of the two-dimensional model, with the halved commutator, and the second as the image of the six-dimensional real model; and the two identifications agree with the abstract identification $\mathrm{Vect}(\mathbb{B})\cong\mathfrak{sl}(2,\mathbb{C})$ of *The Lie Algebra of the Antisymmetric Plain Algebra*.

*Proof.* The first is the image computation of the two-dimensional model; the second is the kernel-zero image of the adjoint; and the abstract identification is the cross-product identification of the derived algebra. The three agree because all three are morphisms of the bracket and all three are injective on the derived algebra. Computed on the basis. $\square$

**Remark (the two halves of the block in the two models).** The two-dimensional model is the defining representation of the derived algebra, of complex dimension two; the six-dimensional model is its adjoint representation, of complex dimension three, realified. **The derived algebra of the block acts on the two-dimensional model and on itself, and the two actions are the two irreducible actions of $\mathfrak{sl}(2,\mathbb{C})$ that the block carries.** The kernel of the first action is zero on the derived algebra and the kernel of the second is zero on the derived algebra; on the whole algebra the first has kernel the centre in the domain and the second has the centre in the domain as well, so both models exhibit the decomposition $\mathbb{B}=\mathbb{C}_{\mathbb{B}}\oplus\mathrm{Vect}(\mathbb{B})$ as a kernel and an image.

## Worked Examples

**A bracket of two units, in matrices.** $\mathsf{M}_2(e_1)=\begin{pmatrix}0&-i\\-i&0\end{pmatrix}$, $\mathsf{M}_2(e_2)=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ and $\tfrac12[\mathsf{M}_2(e_1),\mathsf{M}_2(e_2)]=\mathsf{M}_2(e_3)=\begin{pmatrix}-i&0\\0&i\end{pmatrix}$: the halved commutator in the two-dimensional model.

**The trace.** $\operatorname{Tr}\mathsf{M}_2(e_1)=0$ and $\operatorname{Tr}\mathsf{M}_2(e_0)=2$: the vector part is trace-free, the centre is the trace direction, split in two.

**A scalar matrix.** $\mathsf{M}_2(ie_0)=i\mathrm{I}_2$, and $\mathsf{M}_2(ie_0\wedge e_1)=0$: the central element is the scalar matrix, and it is in the kernel of the bracket.

**The trace form.** $\operatorname{Tr}(\mathsf{M}_2(e_1)\mathsf{M}_2(e_2))=0$ and $\operatorname{Tr}(\mathsf{M}_2(e_1)\mathsf{M}_2(e_1))=-2$: the trace form on the trace-free matrices is the Gram matrix $\operatorname{diag}(-2,-2,-2)$, the Killing form of the block.

**A regular operator.** $\mathsf{M}_4(e_1\wedge e_2)=\mathsf{M}_4(e_3)$ and $\tfrac12[\mathsf{M}_4(e_1),\mathsf{M}_4(e_2)]=\mathsf{M}_4(e_3)$: the operator identity of the four-dimensional model, on the pair of the first two units.

**The six-dimensional matrix.** The matrix of $\operatorname{ad}_{e_1}$ displayed above has $\operatorname{Tr}=0$, $\det=0$ and rank $4$; the matrix of $\operatorname{ad}_{ie_1}$ is the realification of $2iC_{e_1}$, with zero diagonal $3\times3$ blocks and the block of $\operatorname{ad}_{e_1}$ in the two off-diagonal positions with opposite signs, and it has the same vanishing trace, vanishing determinant and rank.

**The characteristic polynomial.** $\lambda^2(\lambda^2+4)^2$ for the matrix of $\operatorname{ad}_{e_1}$: the eigenvalues $0$ twice and $\pm2i$ twice each, the imaginary eigenvalues of the cross product doubled by the realification. For $\operatorname{ad}_{ie_1}$, where $\mathbf{P}\cdot\mathbf{P}=-1$, the same count gives $\lambda^2(\lambda^2-4)^2$: the characteristic polynomial depends on $\mathbf{P}\cdot\mathbf{P}$.

**The trace form in the model.** $\operatorname{Tr}(\operatorname{ad}_{e_1}\operatorname{ad}_{e_1})=-16$ and $\operatorname{Tr}(\operatorname{ad}_{ie_1}\operatorname{ad}_{ie_1})=16$, while $\operatorname{Tr}(\operatorname{ad}_{e_1}\operatorname{ad}_{ie_1})=0$: the model's trace form is eight times the realification of the form of the block, of Gram matrix $\operatorname{diag}(-16,-16,-16,16,16,16)$, as the theorem states.

## Summary

In the two-dimensional model $\mathbb{B}\cong M_2(\mathbb{C})$ the antisymmetric plain algebra is the halved commutator $\mathsf{M}_2(\tilde P\wedge\tilde Q)=\tfrac12[\mathsf{M}_2(\tilde P),\mathsf{M}_2(\tilde Q)]$, with image the trace-free matrices, identified with $\mathfrak{sl}(2,\mathbb{C})$ and with the derived algebra, and kernel the scalar matrices, identified with the centre; the trace form of the model is the Killing form of the block, $\kappa(\tilde P,\tilde Q)=\operatorname{Tr}(\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q))=-2\,\mathbf{P}\cdot\mathbf{Q}$ on the derived algebra. In the four-dimensional regular model the bracket is the halved commutator of the left multiplication operators, $\mathsf{M}_4(\tilde P\wedge\tilde Q)=\tfrac12[\mathsf{M}_4(\tilde P),\mathsf{M}_4(\tilde Q)]$, and the adjoint representation is a six-dimensional real matrix model with kernel zero on the derived algebra and image $\mathfrak{sl}(2,\mathbb{C})$, every nonzero matrix of which has vanishing trace, vanishing determinant and rank $4$, with characteristic polynomial $\lambda^2(\lambda^2+4\,\mathbf{P}\cdot\mathbf{P})(\lambda^2+4\,\overline{\mathbf{P}\cdot\mathbf{P}})$ — equal to $\lambda^2(\lambda^2+4)^2$, with minimal polynomial $\lambda(\lambda^2+4)$, at the real units; the trace form of the model is eight times the realification of the form of the block, of Gram matrix $\operatorname{diag}(-16,-16,-16,16,16,16)$. Both models identify the derived algebra with $\mathfrak{sl}(2,\mathbb{C})$, the first as the defining representation and the second as the adjoint representation, and both exhibit the decomposition $\mathbb{B}=\mathbb{C}_{\mathbb{B}}\oplus\mathrm{Vect}(\mathbb{B})$ as a kernel and an image.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ | the two-dimensional model, $\mathsf{M}_2(e_k)=-i\sigma_k$, $\mathsf{M}_2(ie_0)=i\mathrm{I}_2$ |
| $\mathsf{M}_2(\tilde P\wedge\tilde Q)=\tfrac12[\mathsf{M}_2(\tilde P),\mathsf{M}_2(\tilde Q)]$ | the bracket as the halved matrix commutator |
| $\mathsf{M}_2(\mathrm{Vect}(\mathbb{B}))=\{X:\operatorname{Tr}X=0\}\cong\mathfrak{sl}(2,\mathbb{C})$ | the image, the derived algebra |
| $\ker\wedge=\mathsf{M}_2^{-1}(\mathbb{C}\mathrm{I}_2)=\mathbb{C}_{\mathbb{B}}$ | the kernel, the centre |
| $\operatorname{Tr}(\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q))=\kappa(\tilde P,\tilde Q)$ | the trace form is the Killing form on the derived algebra |
| $\mathsf{M}_4(\tilde P\wedge\tilde Q)=\tfrac12[\mathsf{M}_4(\tilde P),\mathsf{M}_4(\tilde Q)]$ | the bracket in the four-dimensional regular model |
| $\operatorname{ad}:\mathrm{Vect}(\mathbb{B})\to M_6(\mathbb{R})$ | the six-dimensional real model of the adjoint |
| $\operatorname{Tr}=0$, $\det=0$, rank $4$ | the invariants of every nonzero matrix of the model |
| $\lambda^2(\lambda^2+4\,\mathbf{P}\cdot\mathbf{P})(\lambda^2+4\,\overline{\mathbf{P}\cdot\mathbf{P}})$ | the characteristic polynomial of the matrix of $\operatorname{ad}_{\tilde P}$, equal to $\lambda^2(\lambda^2+4)^2$ at the real units |
| $\operatorname{Tr}(\operatorname{ad}_{\tilde P}\operatorname{ad}_{\tilde Q})=8\operatorname{Re}\kappa(\tilde P,\tilde Q)$ | the trace form of the model, eight times the realification of the form of the block |

## Further Reading

- *Introduction to the 2×2 Matrix Representation of Biquaternions* (`articles_maths/introduction-to-the-2x2-matrix-representation-of-biquaternions.md`) and *Introduction to the 4×4 Matrix Representation $M_4(\mathbb{C})_L$ of Biquaternions* (`articles_maths/introduction-to-the-4x4-matrix-representation-of-biquaternions.md`), for the construction of the two models
- *The General Plain Algebra in the $2\times2$ Matrix Representation* (`articles_maths/the-general-plain-algebra-in-the-2x2-matrix-representation.md`) and *The General Plain Algebra in the $4\times4$ Matrix Representation* (`articles_maths/the-general-plain-algebra-in-the-4x4-matrix-representation.md`), for the plain product in the two models
- *One-Sided Operators on the General Plain Algebra of Biquaternions* (`articles_maths/one-sided-operators-on-the-general-plain-algebra-of-biquaternions.md`) and *Two-Sided Operators on the General Plain Algebra of Biquaternions* (`articles_maths/two-sided-operators-on-the-general-plain-algebra-of-biquaternions.md`), for the left and right multiplication operators
- *Introduction to the Antisymmetric Plain Algebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-plain-algebra-of-biquaternions.md`), for the bracket and the cross-product formula
- *The Lie Algebra of the Antisymmetric Plain Algebra* (`articles_maths/the-lie-algebra-of-the-antisymmetric-plain-algebra.md`), for the centre, the derived algebra and the identification with $\mathfrak{sl}(2,\mathbb{C})$
- *The Killing Form of the Antisymmetric Plain Algebra* (`articles_maths/the-killing-form-of-the-antisymmetric-plain-algebra.md`), for the invariant form and its constant relation to the plain form
- *The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra* (`articles_maths/the-adjoint-operators-and-the-derivations-of-the-antisymmetric-plain-algebra.md`), for the adjoints, their matrices in the real basis and the derivations
