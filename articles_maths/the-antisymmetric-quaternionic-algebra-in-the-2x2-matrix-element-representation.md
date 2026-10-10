# __The Antisymmetric Quaternionic Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$__

## Introduction

The antisymmetric quaternionic multiplication $\tilde P\diamond\tilde Q=P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q$ is the halved difference of the quaternionic product and the product with the arguments exchanged (*Introduction to the Antisymmetric Quaternionic Algebra of Biquaternions*). This article reads the operation of the block in the $2\times2$ model, the isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$ with the matrix of ${}^{\natural}$ the adjugate, of *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* and *The General Quaternionic Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*; it is the first of the two representation articles of the block, and its companion *The Antisymmetric Quaternionic Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$* repeats the reading on the regular representation. The article treats the difference of the two twisted products, the image and the kernel on the matrices, the trace, the determinant and the rank of the operator, and the matrix form of the invariant form and of the failure of the Jacobi identity. Nothing of the parent product's own models is redone; the models are cited and used.

## The Operation in the Model

**Theorem (the operation in the $2\times2$ model).** Let $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ be the isomorphism of the algebra and let $\operatorname{adj}$ be the adjugate. The matrix of the operation is half the difference of the two twisted products,

$$
\mathsf{M}_2(\tilde P\diamond\tilde Q) = \tfrac12\Bigl(\operatorname{adj}\mathsf{M}_2(\tilde P)\,\mathsf{M}_2(\tilde Q)-\operatorname{adj}\mathsf{M}_2(\tilde Q)\,\mathsf{M}_2(\tilde P)\Bigr),
$$

and $\operatorname{adj}\mathsf{M}_2(\tilde P)=\mathsf{M}_2(\tilde P^{\natural})$ is the matrix of the quaternion conjugation.

*Proof.* The isomorphism satisfies $\mathsf{M}_2(\tilde P\tilde Q)=\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)$ for the plain product and $\mathsf{M}_2(\tilde P^{\natural})=\operatorname{adj}\mathsf{M}_2(\tilde P)$, which is *The General Quaternionic Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*; the $\natural$-product of the parent row is $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q$, of matrix $\mathsf{M}_2(\tilde P\star\tilde Q)=\operatorname{adj}\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)$, and the operation is half the difference of that product with its arguments exchanged. Verified on random pairs. $\square$

**Remark (the twisted product).** In the model the operation is half the difference of the $\natural$-product with its arguments exchanged, and the matrix of the $\natural$-product is a twisted product in which the first factor is read through the matrix of ${}^{\natural}$, the adjugate.

## The Image and the Kernel on the Matrices

**Proposition (the image).** In the $2\times2$ model the image of the operation is the space of traceless matrices, of complex dimension three, since the trace of the image matrix is twice the scalar part of the value.

*Proof.* $\operatorname{Tr}\mathsf{M}_2(\tilde Q)=2Q_0$ and the value of the operation has zero scalar part, so $\operatorname{Tr}\mathsf{M}_2(\tilde P\diamond\tilde Q)=0$; conversely a traceless matrix is the image of a pure vector, and the pure vectors are exactly the traceless matrices, since the trace reads the scalar part. Verified on the model. $\square$

**Proposition (the kernel).** The kernel of the left multiplication operator $L_{\tilde A}$ is the image under the model of the kernel in the coefficient space, which for a regular element $N(\tilde A)\neq0$ is the line $\mathbb{C}\tilde A$: the matrices that the operator annihilates are the multiples of $\mathsf{M}_2(\tilde A)$.

*Proof.* The model is an isomorphism of vector spaces that intertwines the operator with its image, so kernels correspond; the kernel in the coefficient space is computed in *The Adjoint Operators of the Antisymmetric Quaternionic Algebra*. $\square$

**Remark (the traceless matrices).** The image of the block on the matrices is therefore the traceless part, and the kernel is the line of the element. The traceless matrices carry the three-dimensional Lie algebra $\mathfrak{sl}(2,\mathbb{C})$, which is the model of the vector subspace under the operation (*Remarkable Subspaces and the Four General Products*).

## The Operator of the Block on the Matrices

**Proposition (the invariants of the operator).** The left multiplication operator of the block, read in the model, has

$$
\operatorname{Tr}L_{\tilde A} = 3A_0 = \tfrac32\operatorname{Tr}\mathsf{M}_2(\tilde A), \qquad
\det L_{\tilde A} = 0, \qquad
\operatorname{rank}L_{\tilde A} = 3 \iff N(\tilde A)\neq0 ,
$$

with the rank dropping to $2$ on the isotropic cone and to $0$ only at $\tilde A=0$.

*Proof.* The trace of the model is $\operatorname{Tr}\mathsf{M}_2(\tilde A)=2A_0$, which converts the coefficient-space value $3A_0$ computed in *The Adjoint Operators of the Antisymmetric Quaternionic Algebra* into the model formula; the determinant and the rank are basis-independent properties of the operator and are carried over by the intertwining isomorphism. Verified on the model. $\square$

**Proposition (the operator on the matrices).** In the $2\times2$ model the operator acts on a matrix by

$$
L_{\tilde A}\mathsf{M}_2(\tilde R) = \tfrac12\Bigl(\operatorname{adj}\mathsf{M}_2(\tilde A)\,\mathsf{M}_2(\tilde R)-\operatorname{adj}\mathsf{M}_2(\tilde R)\,\mathsf{M}_2(\tilde A)\Bigr),
$$

which is antisymmetric in the two matrix arguments. The operator is the sum of the two terms, the first of which is the multiplication by the fixed matrix in the twisted product and the second the reverse.

*Proof.* This is the model form of $L_{\tilde A}\tilde R=\tilde A\diamond\tilde R$ under the theorem above. Verified on the model. $\square$

## The Invariant Form and the Failure

**Proposition (the invariant form on the matrices).** The unique invariant form of the block, $\varphi(\tilde P,\tilde Q)=P_0Q_0$, reads in the model as

$$
\varphi(\tilde P,\tilde Q) = \tfrac14\operatorname{Tr}\mathsf{M}_2(\tilde P)\,\operatorname{Tr}\mathsf{M}_2(\tilde Q),
$$

its Gram matrix in the coefficient basis is $\operatorname{diag}(1,0,0,0)$, and its radical is the traceless part, that is the image of the block.

*Proof.* $\operatorname{Tr}\mathsf{M}_2(\tilde P)=2P_0$ gives the coefficient; the Gram matrix and the radical are those of *The Invariant Bilinear Forms of the Antisymmetric Quaternionic Algebra*, and the radical is the traceless part by the trace formula. Verified on the model. $\square$

**Proposition (the failure on the matrices).** The failure of the Jacobi identity is the failure of the twisted matrix product to be associative, and the cyclic sum of the block corresponds to the matrix

$$
\mathsf{M}_2\bigl(J(\tilde P,\tilde Q,\tilde R)\bigr)
= \tfrac14\sum_{\sigma\in S_3}\operatorname{sgn}(\sigma)\;
\mathsf{M}_2\bigl([\tilde P_{\sigma(1)},\tilde P_{\sigma(2)},\tilde P_{\sigma(3)}]\bigr) ,
$$

the associator of the quaternionic product being computable on the matrices as the associator of the twisted product $\operatorname{adj}\mathsf{M}_2(\cdot)\mathsf{M}_2(\cdot)$.

*Proof.* The associator criterion expresses the cyclic sum as a quarter of the signed sum of the six associators, and the model carries the associator of the quaternionic product to the associator of the twisted matrix product, being an algebra isomorphism for the plain product and carrying ${}^{\natural}$ to the adjugate. Verified on the model. $\square$

**Computation (the witness in the model).** At the witness of the failure the matrices are

$$
\mathsf{M}_2(e_0)=I, \qquad
\mathsf{M}_2(e_1)=\begin{pmatrix}0&-i\\-i&0\end{pmatrix}, \qquad
\mathsf{M}_2(e_2)=\begin{pmatrix}0&-1\\1&0\end{pmatrix}, \qquad
\mathsf{M}_2(e_3)=\begin{pmatrix}-i&0\\0&i\end{pmatrix},
$$

and the cyclic sum of the block at $(e_0,e_1,e_2)$, which is $-e_3$, has the matrix $-\mathsf{M}_2(e_3)=\operatorname{diag}(i,-i)$.

*Proof.* The matrices are the standard ones of the isomorphism (*Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*), and the cyclic sum is the one computed in *Introduction to the Antisymmetric Quaternionic Algebra of Biquaternions*. $\square$

**Remark (the failure is not an accident of the basis).** The matrix form of the failure is therefore not a numerical accident: the twisted product $\operatorname{adj}\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)$ is the matrix of the parent product, and it is not associative for the same reason that the parent product is not, the adjugate insertion in the first slot being exactly what associativity cannot absorb. The block's matrix model is the antisymmetrisation of that twisted product, and it fails the Jacobi identity because the twisted product fails associativity.

## The Matrices

**The generators.** The realization is fixed on the basis by four matrices:

$$
\mathsf{M}_2(e_0)=\begin{pmatrix}1&0\\0&1\end{pmatrix},\qquad
\mathsf{M}_2(e_1)=\begin{pmatrix}0&-i\\-i&0\end{pmatrix},\qquad
\mathsf{M}_2(e_2)=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
\mathsf{M}_2(e_3)=\begin{pmatrix}-i&0\\0&i\end{pmatrix}.
$$

with the involution carried to the adjugate, $\operatorname{adj}X=(\operatorname{Tr}X)I-X$, and the general element of trace $2Q_0$ and determinant $N(\tilde Q)$.

**The reduction to the commutator, entry by entry.** The adjugate is the trace-complement of the matrix, so the two scalar parts of the half-difference cancel and the operation collapses to a scalar pairing and a commutator,

$$
\mathsf{M}_2(\tilde P\diamond\tilde Q)=\tfrac12\Bigl(\operatorname{adj}X\,Y-\operatorname{adj}Y\,X\Bigr)
=P_0Y-Q_0X-\tfrac12\bigl[X,Y\bigr],
$$

which is the model form of $P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q$: the two scalar multiples carry the $P_0$ and $Q_0$ terms, and the halved commutator carries the cross product, since on two vector parts the commutator of the matrices is twice the matrix of the cross product.

**The witness, entry by entry.** At the pair $e_0,e_1$ the scalar terms collapse and the commutator vanishes, $\mathsf{M}_2(e_0\diamond e_1)=\tfrac12\bigl(\mathsf{M}_2(e_1)-(-\mathsf{M}_2(e_1))\bigr)=\mathsf{M}_2(e_1)$; at the pair $e_1,e_2$ the commutator carries the whole value,
$$
\tfrac12\bigl[\mathsf{M}_2(e_1),\mathsf{M}_2(e_2)\bigr]=\mathsf{M}_2(e_3)=\mathsf{M}_2(e_1\diamond e_2),
$$
on the two pure vectors. Every value is traceless, since the operation is pure vector and the trace of the model is twice the scalar part.

## Summary

In the $2\times2$ model the operation of the block is half the difference of the two twisted products, $\mathsf{M}_2(\tilde P\diamond\tilde Q)=\tfrac12(\operatorname{adj}\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)-\operatorname{adj}\mathsf{M}_2(\tilde Q)\mathsf{M}_2(\tilde P))$, with the adjugate the matrix of ${}^{\natural}$. The image is the traceless part, of complex dimension three, and the kernel is the line of the element, the multiples of the matrix of $\tilde A$ for a regular element. The left multiplication operator has trace $3A_0$, equal to $\tfrac32\operatorname{Tr}\mathsf{M}_2(\tilde A)$, determinant zero, and rank three exactly when $N(\tilde A)\neq0$, dropping to two on the isotropic cone and to zero only at the origin. The unique invariant form is $\varphi(\tilde P,\tilde Q)=\tfrac14\operatorname{Tr}\mathsf{M}_2(\tilde P)\operatorname{Tr}\mathsf{M}_2(\tilde Q)$, with Gram matrix $\operatorname{diag}(1,0,0,0)$ and radical the traceless part. The failure of the Jacobi identity is the failure of the twisted matrix product to be associative, and its matrix at the witness $(e_0,e_1,e_2)$ is $\operatorname{diag}(i,-i)$, the negative of the matrix of $e_3$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\diamond\tilde Q=P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q$ | the antisymmetric quaternionic multiplication, the operation $\mathrm{AQA}$ |
| $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ | the isomorphism of the algebra with the $2\times2$ matrices |
| $\operatorname{adj}\mathsf{M}_2(\tilde P)=\mathsf{M}_2(\tilde P^{\natural})$ | the matrix of the quaternion conjugation in the model |
| $\operatorname{adj}\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)$ | the twisted product, the matrix of the parent product |
| traceless matrices | the image of the block in the model |
| $\operatorname{Tr}L_{\tilde A}=3A_0=\tfrac32\operatorname{Tr}\mathsf{M}_2(\tilde A)$ | the trace of the operator in the model |
| $\varphi=\tfrac14\operatorname{Tr}\mathsf{M}_2(\tilde P)\operatorname{Tr}\mathsf{M}_2(\tilde Q)$ | the invariant form in the model |
| $\operatorname{diag}(i,-i)$ | the matrix of the failure at the witness $(e_0,e_1,e_2)$ |

## Further Reading

- *Introduction to the Antisymmetric Quaternionic Algebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-quaternionic-algebra-of-biquaternions.md`), for the operation, its table and the witness of the failure
- *The Adjoint Operators of the Antisymmetric Quaternionic Algebra* (`articles_maths/the-adjoint-operators-of-the-antisymmetric-quaternionic-algebra.md`), for the trace, the determinant, the rank and the kernel of the operator in the coefficient space
- *The Invariant Bilinear Forms of the Antisymmetric Quaternionic Algebra* (`articles_maths/the-invariant-bilinear-forms-of-the-antisymmetric-quaternionic-algebra.md`), for the invariant form, its Gram matrix and its radical
- *The Jacobi Failure and the Associator Defect of the Antisymmetric Quaternionic Algebra* (`articles_maths/the-jacobi-failure-and-the-associator-defect-of-the-antisymmetric-quaternionic-algebra.md`), for the associator criterion that gives the matrix form of the failure
- *The General Quaternionic Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/the-general-quaternionic-algebra-in-the-2x2-matrix-element-representation.md`), for the model, the matrix of ${}^{\natural}$ and the twisted product
- *The Antisymmetric Quaternionic Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$* (`articles_maths/the-antisymmetric-quaternionic-algebra-in-the-4x4-matrix-element-representation.md`), for the reading on the regular representation
- *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* (`articles_maths/introduction-to-the-2x2-matrix-element-representation-of-biquaternions.md`), for the model itself
