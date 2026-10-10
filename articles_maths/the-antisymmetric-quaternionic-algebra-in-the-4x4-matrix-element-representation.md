# __The Antisymmetric Quaternionic Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$__

## Introduction

The antisymmetric quaternionic multiplication $\tilde P\diamond\tilde Q=P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q$ is the halved difference of the quaternionic product and the product with the arguments exchanged (*Introduction to the Antisymmetric Quaternionic Algebra of Biquaternions*). This article reads the operation of the block in the $4\times4$ left regular model, the regular representation on $\mathbb{B}$ as a four-dimensional space, of *Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions* and *The General Quaternionic Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$*; it is the second of the two representation articles of the block, and its companion *The Antisymmetric Quaternionic Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* repeats the reading on the isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$. The article treats the difference of the two twisted products, the image and the kernel on the matrices, the trace, the determinant and the rank of the operator, and the matrix form of the invariant form. Nothing of the parent product's own models is redone; the models are cited and used.

## The Operation in the Model

**Theorem (the operation in the $4\times4$ model).** Let $\mathsf{M}_4$ be the left regular representation, the matrix of the plain multiplication by the element. Then

$$
\mathsf{M}_4(\tilde P\diamond\tilde Q) = \tfrac12\Bigl(\mathsf{M}_4(\tilde P)^{\mathsf T}\mathsf{M}_4(\tilde Q)-\mathsf{M}_4(\tilde Q)^{\mathsf T}\mathsf{M}_4(\tilde P)\Bigr),
$$

and $\mathsf{M}_4(\tilde P^{\natural})=\mathsf{M}_4(\tilde P)^{\mathsf T}$ is the matrix of the quaternion conjugation.

*Proof.* The regular representation is the multiplication action, faithful and multiplicative, and it carries ${}^{\natural}$ to the transpose, which is *The General Quaternionic Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$*; the $\natural$-product $\tilde P\star\tilde Q$ has the matrix $\mathsf{M}_4(\tilde P)^{\mathsf T}\mathsf{M}_4(\tilde Q)$, and the operation is half the difference of it with its arguments exchanged. Verified on random pairs. $\square$

**Remark (the twisted product).** In the model the operation is half the difference of the $\natural$-product with its arguments exchanged, and the matrix of the $\natural$-product is a twisted product in which the first factor is read through the matrix of ${}^{\natural}$, the transpose.

## The Image and the Kernel on the Matrices

**Proposition (the image).** In the $4\times4$ model the image of the operation is the space of matrices of the regular representation of the vector subspace, which is the traceless part of the image of $\mathsf{M}_4$, of complex dimension three.

*Proof.* $\operatorname{Tr}\mathsf{M}_4(\tilde Q)=4Q_0$ and the value of the operation has zero scalar part, so $\operatorname{Tr}\mathsf{M}_4(\tilde P\diamond\tilde Q)=0$; conversely a traceless regular matrix of the vector subspace is the image of a pure vector, and the pure vectors are exactly the traceless matrices, since the trace reads the scalar part. Verified on the model. $\square$

**Proposition (the kernel).** The kernel of the left multiplication operator $L_{\tilde A}$ is the image under the model of the kernel in the coefficient space, which for a regular element $N(\tilde A)\neq0$ is the line $\mathbb{C}\tilde A$: the matrices that the operator annihilates are the multiples of $\mathsf{M}_4(\tilde A)$.

*Proof.* The model is an isomorphism of vector spaces that intertwines the operator with its image, so kernels correspond; the kernel in the coefficient space is computed in *The Adjoint Operators of the Antisymmetric Quaternionic Algebra*. $\square$

**Remark (the traceless matrices).** The image of the block on the matrices is therefore the traceless part of the image of the regular representation, and the kernel is the line of the element. The traceless matrices carry the three-dimensional Lie algebra $\mathfrak{sl}(2,\mathbb{C})$, which is the model of the vector subspace under the operation (*Remarkable Subspaces and the Four General Products*).

## The Operator of the Block on the Matrices

**Proposition (the invariants of the operator).** The left multiplication operator of the block, read in the model, has

$$
\operatorname{Tr}L_{\tilde A} = 3A_0 = \tfrac34\operatorname{Tr}\mathsf{M}_4(\tilde A), \qquad
\det L_{\tilde A} = 0, \qquad
\operatorname{rank}L_{\tilde A} = 3 \iff N(\tilde A)\neq0 ,
$$

with the rank dropping to $2$ on the isotropic cone and to $0$ only at $\tilde A=0$.

*Proof.* The trace of the model is $\operatorname{Tr}\mathsf{M}_4(\tilde A)=4A_0$, which converts the coefficient-space value $3A_0$ computed in *The Adjoint Operators of the Antisymmetric Quaternionic Algebra* into the model formula; the determinant and the rank are basis-independent properties of the operator and are carried over by the intertwining isomorphism. Verified on the model. $\square$

**Proposition (the operator on the matrices).** In the $4\times4$ model the operator acts on a matrix by

$$
L_{\tilde A}\mathsf{M}_4(\tilde R) = \tfrac12\Bigl(\mathsf{M}_4(\tilde A)^{\mathsf T}\mathsf{M}_4(\tilde R)-\mathsf{M}_4(\tilde R)^{\mathsf T}\mathsf{M}_4(\tilde A)\Bigr),
$$

which is antisymmetric in the two matrix arguments. The operator is the sum of the two terms, the first of which is the multiplication by the fixed matrix in the twisted product and the second the reverse.

*Proof.* This is the model form of $L_{\tilde A}\tilde R=\tilde A\diamond\tilde R$ under the theorem above. Verified on the model. $\square$

## The Matrix Form of the Invariant Form

**Proposition (the invariant form on the matrices).** The unique invariant form of the block, $\varphi(\tilde P,\tilde Q)=P_0Q_0$, reads in the model as

$$
\varphi(\tilde P,\tilde Q) = \tfrac1{16}\operatorname{Tr}\mathsf{M}_4(\tilde P)\,\operatorname{Tr}\mathsf{M}_4(\tilde Q),
$$

its Gram matrix in the coefficient basis is $\operatorname{diag}(1,0,0,0)$, and its radical is the traceless part, that is the image of the block.

*Proof.* $\operatorname{Tr}\mathsf{M}_4(\tilde P)=4P_0$ gives the coefficient; the Gram matrix and the radical are those of *The Invariant Bilinear Forms of the Antisymmetric Quaternionic Algebra*, and the radical is the traceless part by the trace formula. Verified on the model. $\square$

**Remark (the form is not the matrix pairing).** The invariant form reads the two traces and nothing else: it is degenerate on every value, its radical being the whole traceless part, which is the image of the block. In the model this is the statement that the form is blind to the traceless regular matrices and sees only the scalar direction.

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

and the involution is the transposition, the trace-complement $X^{\mathsf T}=\tfrac12(\operatorname{Tr}X)I_4-X$ of the regular matrix.

**The reduction to the commutator, entry by entry.** Because the transposition is the trace-complement, the two scalar terms of the half-difference cancel exactly as in the realization, and the operation collapses to the same scalar pairing and commutator,

$$
\mathsf{M}_4(\tilde P\diamond\tilde Q)=\tfrac12\Bigl(\mathsf{M}_4(\tilde P)^{\mathsf{T}}\mathsf{M}_4(\tilde Q)-\mathsf{M}_4(\tilde Q)^{\mathsf{T}}\mathsf{M}_4(\tilde P)\Bigr)
=P_0Y-Q_0X-\tfrac12\bigl[X,Y\bigr],
$$

the scalar coefficient $\tfrac12$ of the trace-complement being absorbed by the commutator, which is blind to the scalar matrix. **The two models therefore carry the same reduction**, $P_0Y-Q_0X-\tfrac12[X,Y]$, although the involution is the adjugate in one and the transposition in the other.

**The witness, entry by entry.** At the pair $e_1,e_2$ the value is the halved commutator of the two regular matrices, $\tfrac12[\mathsf{M}_4(e_1),\mathsf{M}_4(e_2)]=\mathsf{M}_4(e_3)=\mathsf{M}_4(e_1\diamond e_2)$, since $\mathsf{M}_4(e_1)\mathsf{M}_4(e_2)=\mathsf{M}_4(e_3)$ and the reversed product is its negative. Every value is a traceless regular matrix of the vector subspace, and the image is the complex three-dimensional space of those matrices.

## Summary

In the $4\times4$ regular model the operation of the block is half the difference of the two twisted products, $\mathsf{M}_4(\tilde P\diamond\tilde Q)=\tfrac12(\mathsf{M}_4(\tilde P)^{\mathsf T}\mathsf{M}_4(\tilde Q)-\mathsf{M}_4(\tilde Q)^{\mathsf T}\mathsf{M}_4(\tilde P))$, with the transpose the matrix of ${}^{\natural}$, since $\mathsf{M}_4(\tilde P^{\natural})=\mathsf{M}_4(\tilde P)^{\mathsf T}$. The image is the traceless part of the image of the regular representation, of complex dimension three, and the kernel is the line of the element, the multiples of the matrix of $\tilde A$ for a regular element. The left multiplication operator has trace $3A_0$, equal to $\tfrac34\operatorname{Tr}\mathsf{M}_4(\tilde A)$, determinant zero, and rank three exactly when $N(\tilde A)\neq0$, dropping to two on the isotropic cone and to zero only at the origin. The unique invariant form is $\varphi(\tilde P,\tilde Q)=\tfrac1{16}\operatorname{Tr}\mathsf{M}_4(\tilde P)\operatorname{Tr}\mathsf{M}_4(\tilde Q)$, with Gram matrix $\operatorname{diag}(1,0,0,0)$ and radical the traceless part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\diamond\tilde Q=P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q$ | the antisymmetric quaternionic multiplication, the operation $\mathrm{AQA}$ |
| $\mathsf{M}_4$ | the left regular representation, the $4\times4$ model |
| $\mathsf{M}_4(\tilde P^{\natural})=\mathsf{M}_4(\tilde P)^{\mathsf T}$ | the matrix of the quaternion conjugation in the model |
| $\mathsf{M}_4(\tilde P)^{\mathsf T}\mathsf{M}_4(\tilde Q)$ | the twisted product, the matrix of the parent product |
| traceless matrices | the image of the block in the model |
| $\operatorname{Tr}L_{\tilde A}=3A_0=\tfrac34\operatorname{Tr}\mathsf{M}_4(\tilde A)$ | the trace of the operator in the model |
| $\varphi=\tfrac1{16}\operatorname{Tr}\mathsf{M}_4(\tilde P)\operatorname{Tr}\mathsf{M}_4(\tilde Q)$ | the invariant form in the model |

## Further Reading

- *Introduction to the Antisymmetric Quaternionic Algebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-quaternionic-algebra-of-biquaternions.md`), for the operation, its table and the witness of the failure
- *The Adjoint Operators of the Antisymmetric Quaternionic Algebra* (`articles_maths/the-adjoint-operators-of-the-antisymmetric-quaternionic-algebra.md`), for the trace, the determinant, the rank and the kernel of the operator in the coefficient space
- *The Invariant Bilinear Forms of the Antisymmetric Quaternionic Algebra* (`articles_maths/the-invariant-bilinear-forms-of-the-antisymmetric-quaternionic-algebra.md`), for the invariant form, its Gram matrix and its radical
- *The General Quaternionic Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$* (`articles_maths/the-general-quaternionic-algebra-in-the-4x4-matrix-element-representation.md`), for the regular representation and the transpose of the conjugation
- *The Antisymmetric Quaternionic Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/the-antisymmetric-quaternionic-algebra-in-the-2x2-matrix-element-representation.md`), for the reading on the isomorphism
- *Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions* (`articles_maths/introduction-to-the-4x4-matrix-element-representation-of-biquaternions.md`), for the model itself
