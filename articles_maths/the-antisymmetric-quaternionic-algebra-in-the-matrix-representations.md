# __The Antisymmetric Quaternionic Algebra in the Matrix Representations__

## Introduction

The antisymmetric quaternionic multiplication $\tilde P\diamond\tilde Q=P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q$ is the halved difference of the quaternionic product and the product with the arguments exchanged (*Introduction to the Antisymmetric Quaternionic Algebra of Biquaternions*). The chapter carries two matrix models of the algebra: the isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$ with the matrix of ${}^{\natural}$ the adjugate, of *Introduction to the 2×2 Matrix Representation of Biquaternions* and *The General Quaternionic Algebra in the $2\times2$ Matrix Representation*, and the regular representation on $\mathbb{B}$ as a four-dimensional space, of *Introduction to the 4×4 Matrix Representation $M_4(\mathbb{C})_L$ of Biquaternions* and *The General Quaternionic Algebra in the $4\times4$ Matrix Representation*. This article reads the operation of the block in the two models: the difference of the two twisted products, the image and the kernel on the matrices, the trace, the determinant and the rank of the operator, and the matrix form of the invariant form and of the failure of the Jacobi identity. Nothing of the parent product's own models is redone; the models are cited and used.

## The Operation in the Two Models

**Theorem (the operation in the $2\times2$ model).** Let $\Phi:\mathbb{B}\to M_2(\mathbb{C})$ be the isomorphism of the algebra and let $\operatorname{adj}$ be the adjugate. The matrix of the operation is half the difference of the two twisted products,

$$
\Phi(\tilde P\diamond\tilde Q) = \tfrac12\Bigl(\operatorname{adj}\Phi(\tilde P)\,\Phi(\tilde Q)-\operatorname{adj}\Phi(\tilde Q)\,\Phi(\tilde P)\Bigr),
$$

and $\operatorname{adj}\Phi(\tilde P)=\Phi(\tilde P^{\natural})$ is the matrix of the quaternion conjugation.

*Proof.* The isomorphism satisfies $\Phi(\tilde P\tilde Q)=\Phi(\tilde P)\Phi(\tilde Q)$ for the plain product and $\Phi(\tilde P^{\natural})=\operatorname{adj}\Phi(\tilde P)$, which is *The General Quaternionic Algebra in the $2\times2$ Matrix Representation*; the $\natural$-product of the parent row is $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q$, of matrix $\Phi(\tilde P\star\tilde Q)=\operatorname{adj}\Phi(\tilde P)\Phi(\tilde Q)$, and the operation is half the difference of that product with its arguments exchanged. $\square$

**Theorem (the operation in the $4\times4$ model).** Let $\rho_L$ be the left regular representation, the matrix of the plain multiplication by the element. Then

$$
\rho_L(\tilde P\diamond\tilde Q) = \tfrac12\Bigl(\rho_L(\tilde P)^{\mathsf T}\rho_L(\tilde Q)-\rho_L(\tilde Q)^{\mathsf T}\rho_L(\tilde P)\Bigr),
$$

and $\rho_L(\tilde P^{\natural})=\rho_L(\tilde P)^{\mathsf T}$ is the matrix of the quaternion conjugation.

*Proof.* The regular representation is the multiplication action, faithful and multiplicative, and it carries ${}^{\natural}$ to the transpose, which is *The General Quaternionic Algebra in the $4\times4$ Matrix Representation*; the $\natural$-product $\tilde P\star\tilde Q$ has the matrix $\rho_L(\tilde P)^{\mathsf T}\rho_L(\tilde Q)$, and the operation is half the difference of it with its arguments exchanged. $\square$

The two theorems are the two readings of one fact: in each model the operation is half the difference of the $\natural$-product with its arguments exchanged, and the matrix of the $\natural$-product is a twisted product in which the first factor is read through the matrix of ${}^{\natural}$, the adjugate in the two-dimensional model and the transpose in the four-dimensional one.

**Computation (the witness in the $2\times2$ model).** At the witness of the failure the matrices are

$$
\Phi(e_0)=I, \qquad
\Phi(e_1)=\begin{pmatrix}0&-i\\-i&0\end{pmatrix}, \qquad
\Phi(e_2)=\begin{pmatrix}0&-1\\1&0\end{pmatrix}, \qquad
\Phi(e_3)=\begin{pmatrix}-i&0\\0&i\end{pmatrix},
$$

and the cyclic sum of the block at $(e_0,e_1,e_2)$, which is $-e_3$, has the matrix $-\Phi(e_3)=\operatorname{diag}(i,-i)$.

*Proof.* The matrices are the standard ones of the isomorphism (*Introduction to the 2×2 Matrix Representation of Biquaternions*), and the cyclic sum is the one computed in *Introduction to the Antisymmetric Quaternionic Algebra of Biquaternions*. $\square$

## The Image and the Kernel on the Matrices

**Proposition (the image).** In the $2\times2$ model the image of the operation is the space of traceless matrices, of complex dimension three, since the trace of the image matrix is twice the scalar part of the value; in the $4\times4$ model the image is the space of matrices of the regular representation of the vector subspace, which is the traceless part of the image of $\rho_L$. In the coefficient model the image is the vector subspace, as before.

*Proof.* $\operatorname{Tr}\Phi(\tilde Q)=2Q_0$ and the value of the operation has zero scalar part, so $\operatorname{Tr}\Phi(\tilde P\diamond\tilde Q)=0$; conversely a traceless matrix is the image of a pure vector, and the pure vectors are exactly the traceless matrices, since the trace reads the scalar part. In the regular model $\operatorname{Tr}\rho_L(\tilde Q)=4Q_0$, so the same argument applies. $\square$

**Proposition (the kernel).** In either model the kernel of the left multiplication operator $L_{\tilde A}$ is the image under the model of the kernel in the coefficient space, which for a regular element $N(\tilde A)\neq0$ is the line $\mathbb{C}\tilde A$: the matrices that the operator annihilates are the multiples of $\Phi(\tilde A)$, respectively of $\rho_L(\tilde A)$.

*Proof.* The models are isomorphisms of vector spaces that intertwine the operator with its image, so kernels correspond; the kernel in the coefficient space is computed in *The Adjoint Operators of the Antisymmetric Quaternionic Algebra*. $\square$

The image of the block on the matrices is therefore the traceless part, and the kernel is the line of the element. The traceless matrices carry the three-dimensional Lie algebra $\mathfrak{sl}(2,\mathbb{C})$, which is the model of the vector subspace under the operation (*The Six Subspaces and the Four General Products*).

## The Operator of the Block on the Matrices

**Proposition (the invariants of the operator).** The left multiplication operator of the block, read in either model, has

$$
\operatorname{Tr}L_{\tilde A} = 3A_0 = \tfrac32\operatorname{Tr}\Phi(\tilde A) = \tfrac34\operatorname{Tr}\rho_L(\tilde A), \qquad
\det L_{\tilde A} = 0, \qquad
\operatorname{rank}L_{\tilde A} = 3 \iff N(\tilde A)\neq0 ,
$$

with the rank dropping to $2$ on the isotropic cone and to $0$ only at $\tilde A=0$.

*Proof.* The traces of the two models are $\operatorname{Tr}\Phi(\tilde A)=2A_0$ and $\operatorname{Tr}\rho_L(\tilde A)=4A_0$, which convert the coefficient-space value $3A_0$ computed in *The Adjoint Operators of the Antisymmetric Quaternionic Algebra* into the two model formulae; the determinant and the rank are basis-independent properties of the operator and are carried over by the intertwining isomorphism. $\square$

**Proposition (the operator on the matrices).** In the $2\times2$ model the operator acts on a matrix by

$$
L_{\tilde A}\Phi(\tilde R) = \tfrac12\Bigl(\operatorname{adj}\Phi(\tilde A)\,\Phi(\tilde R)-\operatorname{adj}\Phi(\tilde R)\,\Phi(\tilde A)\Bigr),
$$

which is antisymmetric in the two matrix arguments, and in the $4\times4$ model by the same formula with $\rho_L$ and the transpose. In either model the operator is the sum of the two terms, the first of which is the multiplication by the fixed matrix in the twisted product and the second the reverse.

*Proof.* This is the model form of $L_{\tilde A}\tilde R=\tilde A\diamond\tilde R$ under the two theorems above. $\square$

## The Matrix Form of the Invariant Form and of the Failure

**Proposition (the invariant form on the matrices).** The unique invariant form of the block, $\varphi(\tilde P,\tilde Q)=P_0Q_0$, reads in the two models as

$$
\varphi(\tilde P,\tilde Q) = \tfrac14\operatorname{Tr}\Phi(\tilde P)\,\operatorname{Tr}\Phi(\tilde Q) = \tfrac1{16}\operatorname{Tr}\rho_L(\tilde P)\,\operatorname{Tr}\rho_L(\tilde Q),
$$

its Gram matrix in the coefficient basis is $\operatorname{diag}(1,0,0,0)$, and its radical is the traceless part, that is the image of the block.

*Proof.* $\operatorname{Tr}\Phi(\tilde P)=2P_0$ and $\operatorname{Tr}\rho_L(\tilde P)=4P_0$, giving the two coefficients; the Gram matrix and the radical are those of *The Invariant Bilinear Forms of the Antisymmetric Quaternionic Algebra*, and the radical is the traceless part by the trace formula. $\square$

**Proposition (the failure on the matrices).** The failure of the Jacobi identity is the failure of the twisted matrix product to be associative, and in the $2\times2$ model the cyclic sum of the block corresponds to the matrix

$$
\Phi\bigl(J(\tilde P,\tilde Q,\tilde R)\bigr)
= \tfrac14\sum_{\sigma\in S_3}\operatorname{sgn}(\sigma)\;
\Phi\bigl([\tilde P_{\sigma(1)},\tilde P_{\sigma(2)},\tilde P_{\sigma(3)}]\bigr) ,
$$

the associator of the quaternionic product being computable on the matrices as the associator of the twisted product $\operatorname{adj}\Phi(\cdot)\Phi(\cdot)$. In particular the matrix of the failure at the witness is $\operatorname{diag}(i,-i)$.

*Proof.* The associator criterion expresses the cyclic sum as a quarter of the signed sum of the six associators, and the model carries the associator of the quaternionic product to the associator of the twisted matrix product, being an algebra isomorphism for the plain product and carrying ${}^{\natural}$ to the adjugate; the value at the witness is the computation above. $\square$

**Remark.** The matrix form of the failure is therefore not a numerical accident of the basis: the twisted product $\operatorname{adj}\Phi(\tilde P)\Phi(\tilde Q)$ is the matrix of the parent product, and it is not associative for the same reason that the parent product is not, the adjugate insertion in the first slot being exactly what associativity cannot absorb. The block's matrix model is the antisymmetrisation of that twisted product, and it fails the Jacobi identity because the twisted product fails associativity.

## Summary

In the $2\times2$ model the operation of the block is half the difference of the two twisted products, $\Phi(\tilde P\diamond\tilde Q)=\tfrac12(\operatorname{adj}\Phi(\tilde P)\Phi(\tilde Q)-\operatorname{adj}\Phi(\tilde Q)\Phi(\tilde P))$, with the adjugate the matrix of ${}^{\natural}$; in the $4\times4$ regular model it is the same formula with $\rho_L$ and the transpose, since $\rho_L(\tilde P^{\natural})=\rho_L(\tilde P)^{\mathsf T}$. The image is the traceless part in either model, of complex dimension three, and the kernel is the line of the element, the multiples of the matrix of $\tilde A$ for a regular element. The left multiplication operator has trace $3A_0$, equal to $\tfrac32\operatorname{Tr}\Phi(\tilde A)$ and to $\tfrac34\operatorname{Tr}\rho_L(\tilde A)$, determinant zero, and rank three exactly when $N(\tilde A)\neq0$, dropping to two on the isotropic cone and to zero only at the origin. The unique invariant form is $\varphi(\tilde P,\tilde Q)=\tfrac14\operatorname{Tr}\Phi(\tilde P)\operatorname{Tr}\Phi(\tilde Q)=\tfrac1{16}\operatorname{Tr}\rho_L(\tilde P)\operatorname{Tr}\rho_L(\tilde Q)$, with Gram matrix $\operatorname{diag}(1,0,0,0)$ and radical the traceless part. The failure of the Jacobi identity is the failure of the twisted matrix product to be associative, and its matrix at the witness $(e_0,e_1,e_2)$ is $\operatorname{diag}(i,-i)$, the negative of the matrix of $e_3$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\diamond\tilde Q=P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q$ | the antisymmetric quaternionic multiplication, the operation $\mathrm{AQA}$ |
| $\Phi:\mathbb{B}\to M_2(\mathbb{C})$ | the isomorphism of the algebra with the $2\times2$ matrices |
| $\operatorname{adj}\Phi(\tilde P)=\Phi(\tilde P^{\natural})$ | the matrix of the quaternion conjugation in the $2\times2$ model |
| $\rho_L$ | the left regular representation, the $4\times4$ model |
| $\rho_L(\tilde P^{\natural})=\rho_L(\tilde P)^{\mathsf T}$ | the matrix of the quaternion conjugation in the regular model |
| $\operatorname{adj}\Phi(\tilde P)\Phi(\tilde Q)$ | the twisted product, the matrix of the parent product |
| traceless matrices | the image of the block in either model |
| $\operatorname{Tr}L_{\tilde A}=3A_0$ | the trace of the operator, in the models $\tfrac32\operatorname{Tr}\Phi(\tilde A)$ and $\tfrac34\operatorname{Tr}\rho_L(\tilde A)$ |
| $\varphi=\tfrac14\operatorname{Tr}\Phi(\tilde P)\operatorname{Tr}\Phi(\tilde Q)$ | the invariant form in the $2\times2$ model |
| $\operatorname{diag}(i,-i)$ | the matrix of the failure at the witness $(e_0,e_1,e_2)$ |

## Further Reading

- *Introduction to the Antisymmetric Quaternionic Algebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-quaternionic-algebra-of-biquaternions.md`), for the operation, its table and the witness of the failure
- *The Adjoint Operators of the Antisymmetric Quaternionic Algebra* (`articles_maths/the-adjoint-operators-of-the-antisymmetric-quaternionic-algebra.md`), for the trace, the determinant, the rank and the kernel of the operator in the coefficient space
- *The Invariant Bilinear Forms of the Antisymmetric Quaternionic Algebra* (`articles_maths/the-invariant-bilinear-forms-of-the-antisymmetric-quaternionic-algebra.md`), for the invariant form, its Gram matrix and its radical
- *The Jacobi Failure and the Associator Defect of the Antisymmetric Quaternionic Algebra* (`articles_maths/the-jacobi-failure-and-the-associator-defect-of-the-antisymmetric-quaternionic-algebra.md`), for the associator criterion that gives the matrix form of the failure
- *The General Quaternionic Algebra in the $2\times2$ Matrix Representation* (`articles_maths/the-general-quaternionic-algebra-in-the-2x2-matrix-representation.md`), for the model, the matrix of ${}^{\natural}$ and the twisted product
- *The General Quaternionic Algebra in the $4\times4$ Matrix Representation* (`articles_maths/the-general-quaternionic-algebra-in-the-4x4-matrix-representation.md`), for the regular representation and the transpose of the conjugation
- *Introduction to the 2×2 Matrix Representation of Biquaternions* (`articles_maths/introduction-to-the-2x2-matrix-representation-of-biquaternions.md`) and *Introduction to the 4×4 Matrix Representation $M_4(\mathbb{C})_L$ of Biquaternions* (`articles_maths/introduction-to-the-4x4-matrix-representation-of-biquaternions.md`), for the two models themselves
