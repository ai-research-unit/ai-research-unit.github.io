# __The Symmetric Plain Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$__

## Introduction

The symmetric plain algebra of $\mathbb{B}$ carries the product $\tilde P\bullet\tilde Q=\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ of *Introduction to the Symmetric Plain Algebra of Biquaternions*. This article reads the block in the $4\times4$ left regular representation $\mathsf{M}_4$ of *The General Plain Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$*; it is the second of the two representation articles of the block, and its companion *The Symmetric Plain Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* repeats the reading on the realization $\mathsf{M}_2$.

The transport is short because the symmetrisation of the plain product becomes the symmetrisation of the regular matrix product: the plain product is the matrix product, so the block's product is the half-sum of a regular matrix and its exchanged product. What the regular model adds is the matrix reading of every notion at once — the square as an ordinary matrix square, the quadratic identity as a degree-two factor of the squared characteristic polynomial, the idempotents as regular projectors, the isotropic cone as the singular matrices, the elements of square zero as the nilpotent matrices, the trace form as a quarter of the matrix trace — and the squared characteristic polynomial in which the regular matrix sees the quadratic identity twice.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$ and central scalar imaginary $i$; an element is $\tilde Q=\sum_\mu Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$; the generic norm is $N(\tilde Q)=\sum_\mu Q_\mu^2$ and the trace form is $\tau(\tilde P,\tilde Q)=P_0Q_0-(\mathbf{P},\mathbf{Q})$. The regular representation is $L_{\tilde Q}(\tilde R)=\tilde Q\tilde R$, with $\operatorname{Tr}\mathsf{M}_4(\tilde Q)=4Q_0$, $\det\mathsf{M}_4(\tilde Q)=N(\tilde Q)^2$, $\mathsf{M}_4^{R}(\tilde Q)=E\mathsf{M}_4(\tilde Q)^{\mathsf T}E$ and $\mathsf{M}_4(\tilde Q^{\natural})=\mathsf{M}_4(\tilde Q)^{\mathsf T}$. The matrices $\mathsf{M}_4(\tilde Q)$ and $\mathsf{M}_4^{R}(\tilde Q)$ are the plain and right regular matrices of *The General Plain Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$*.

## The Symmetrisation of the Regular Matrix Product

**Theorem.** The block's product becomes the symmetrisation of the regular matrix product:

$$
\mathsf{M}_4\bigl(\tilde P\bullet\tilde Q\bigr)=\tfrac12\bigl(\mathsf{M}_4(\tilde P)\mathsf{M}_4(\tilde Q)+\mathsf{M}_4(\tilde Q)\mathsf{M}_4(\tilde P)\bigr),\qquad
\mathsf{M}_4^{R}\bigl(\tilde P\bullet\tilde Q\bigr)=\tfrac12\bigl(\mathsf{M}_4^{R}(\tilde P)\mathsf{M}_4^{R}(\tilde Q)+\mathsf{M}_4^{R}(\tilde Q)\mathsf{M}_4^{R}(\tilde P)\bigr).
$$

*Proof.* $\mathsf{M}_4$ is an algebra homomorphism, $\mathsf{M}_4(\tilde P\bullet\tilde Q)=\tfrac12(\mathsf{M}_4(\tilde P\tilde Q)+\mathsf{M}_4(\tilde Q\tilde P))=\tfrac12(\mathsf{M}_4(\tilde P)\mathsf{M}_4(\tilde Q)+\mathsf{M}_4(\tilde Q)\mathsf{M}_4(\tilde P))$, and the same computation holds for $\mathsf{M}_4^{R}$. Verified on the model. $\square$

**Remark (the regular model and its invariants).** The $4\times4$ model is the direct sum of two copies of the $2\times2$ realization, carried by the coefficient space. **The model turns the block into the symmetrisation of the regular matrix algebra**, and its invariants are the dimension multiples of the ones of the realization: the trace is $4Q_0$ against $2Q_0$ and the determinant is $N^2$ against $N$. The relation of the two transports is read in *Biquaternion Objects and Their Matrix Correspondences*.

## The Square and the Polarisation

**Theorem (the square).** The square of the block is the matrix square:

$$
\mathsf{M}_4\bigl(\tilde Q\bullet\tilde Q\bigr)=\mathsf{M}_4(\tilde Q)^2 .
$$

*Proof.* The square of the block is the plain square $\tilde Q^2$ by *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*, and the model is multiplicative on the plain product. Verified on the model. $\square$

**Remark (the regular matrix and the squared polynomial).** The characteristic polynomial of the regular matrix is the **square** of the quadratic:

$$
\det\bigl(\lambda I-\mathsf{M}_4(\tilde Q)\bigr)=\bigl(\lambda^2-2Q_0\lambda+N(\tilde Q)\bigr)^2,
$$

because the regular module is the direct sum of the two copies of the simple module, so each eigenvalue of $\mathsf{M}_2(\tilde Q)$ occurs twice. The trace $4Q_0$ and the determinant $N^2$ of $\mathsf{M}_4(\tilde Q)$ are the two coefficients of the squared polynomial that the dimension allows to be read; **the quadratic identity is a degree-two statement in the model, and the regular matrix sees it twice.** The quadratic identity itself is carried by the transport of the square, $\mathsf{M}_4(\tilde Q)^2-2Q_0\mathsf{M}_4(\tilde Q)+N(\tilde Q)I=0$. Verified on the model.

**Theorem (the quadratic form and the trace form).** The quadratic trace and the trace form become scaled matrix traces:

$$
\mathrm{Sc}\bigl(\tilde Q\bullet\tilde Q\bigr)=\tfrac14\operatorname{Tr}\bigl(\mathsf{M}_4(\tilde Q)^2\bigr),\qquad
\tau(\tilde P,\tilde Q)=\tfrac14\operatorname{Tr}\bigl(\mathsf{M}_4(\tilde P)\mathsf{M}_4(\tilde Q)\bigr).
$$

*Proof.* $\mathrm{Sc}(\tilde Q^2)=\tfrac14\operatorname{Tr}(\mathsf{M}_4(\tilde Q)^2)$ is the trace pairing of the regular model evaluated on $\tilde Q=\tilde P$, because $\operatorname{Tr}\mathsf{M}_4(\tilde Q^2)=4\operatorname{Sc}(\tilde Q^2)$; for the general form, $\tau(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\bullet\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q)$ and $\tfrac14\operatorname{Tr}(\mathsf{M}_4(\tilde P)\mathsf{M}_4(\tilde Q))=\mathrm{Sc}(\tilde P\tilde Q)$. The trace of the regular matrices is four times the form. Verified on the model. $\square$

**Remark (the polarisation on the matrices).** The quadratic form $\tilde Q\mapsto\tfrac14\operatorname{Tr}(\mathsf{M}_4(\tilde Q)^2)$ polarises to the bilinear form $\tfrac14\operatorname{Tr}(\mathsf{M}_4(\tilde P)\mathsf{M}_4(\tilde Q))$, and the product is recovered from the square by polarisation: $\mathsf{M}_4(\tilde P\bullet\tilde Q)=\tfrac12\bigl(\mathsf{M}_4(\tilde P)\mathsf{M}_4(\tilde Q)+\mathsf{M}_4(\tilde Q)\mathsf{M}_4(\tilde P)\bigr)$, equivalently $\tfrac12$ times the polarisation of the regular matrix square. **The degree-two structure of the block is the Cayley–Hamilton structure of the regular matrices**, and the polarisation that recovers the product from the form is *The Trace Form and the Invariance of the Symmetric Plain Algebra*. Verified on the model.

## The Idempotents in the Regular Model

**Theorem.** An idempotent $\tilde\Pi$ gives the regular projector $\mathsf{M}_4(\tilde\Pi)$ of trace $4\Pi_0=2$ and rank two, with the eigenvalues $1,1,0,0$; the two copies of the simple module carry one projector each.

*Proof.* $\mathsf{M}_4(\tilde\Pi)^2=\mathsf{M}_4(\tilde\Pi)$ by the transport of the square, so the regular matrix is a projector, of trace $\operatorname{Tr}\mathsf{M}_4(\tilde\Pi)=4\Pi_0=2$ for a non-trivial idempotent; the regular module is the direct sum of the two copies of the simple module, and on each copy the projector has rank one, so the rank is two and the eigenvalues are $1,1,0,0$. Verified on the model. $\square$

**Remark (the regular projector and the realization).** The regular projector is the direct sum of the two rank-one projectors $\mathsf{M}_2(\tilde\Pi)$ of the two copies of the simple module, and it is why the trace doubles and the rank doubles with respect to the $2\times2$ realization. The Hermitian idempotents give the Hermitian regular projectors, and the non-Hermitian ones the non-Hermitian regular projectors, by the transport of the two conjugations; the Peirce decomposition is that of *Biquaternion Ideals and Peirce Decomposition*. Verified on the model.

## The Isotropic Cone

**Theorem (the determinant and the norm).** The generic norm is a determinant:

$$
\det\mathsf{M}_4(\tilde Q)=N(\tilde Q)^2 .
$$

*Proof.* The determinant of the regular matrix is the square of the determinant of the realization, because the regular module is the direct sum of the two copies of the simple module. Verified on the model. $\square$

**Theorem (the isotropic elements).** The isotropic cone of the block is the set of **singular matrices**:

$$
N(\tilde Q)=0\iff\mathsf{M}_4(\tilde Q)\ \text{singular}.
$$

*Proof.* $\det\mathsf{M}_4(\tilde Q)=N(\tilde Q)^2$; a matrix is singular exactly when its determinant vanishes. Verified on the model. $\square$

**Remark (the rank of the isotropic matrices).** A non-zero isotropic element has a non-zero singular matrix of **rank two**, the two copies of the simple module carrying one vanishing direction each. **The isotropic cone of the block is the cone of the rank-two matrices of the regular model**, and the zero divisors are the rank-two matrices; the description of *Biquaternion Zero Divisors* is the same list. Verified on the model.

**Theorem (the elements of square zero).** The elements of square zero are exactly the **nilpotent** matrices:

$$
\tilde Q\bullet\tilde Q=0\iff\mathsf{M}_4(\tilde Q)^2=0 .
$$

*Proof.* $\mathsf{M}_4(\tilde Q\bullet\tilde Q)=\mathsf{M}_4(\tilde Q)^2$ by the transport of the square, so the square of the block vanishes exactly when the regular matrix square vanishes; the regular matrix has vanishing square exactly when its two simple blocks do, so the two conditions agree. Verified on the model. $\square$

**Remark (the isotropic matrices split into the nilpotent and the non-nilpotent).** The isotropic cone is the union of the origin, the **nilpotent** matrices, which are the images of the elements of square zero, and the **singular non-nilpotent** matrices, which are the images of the isotropic elements that are not of square zero. The element $e_1+ie_2$ is of square zero, and $\mathsf{M}_4(e_1+ie_2)$ is nilpotent of trace $0$ and of rank two; the element $e_0+ie_1$ is isotropic without being of square zero, and $\mathsf{M}_4(e_0+ie_1)$ is singular of rank two and of trace $4$, not nilpotent. **The model description of the isotropic cone is the nilpotent matrices together with the singular matrices of non-zero trace.** Verified on the witnesses.

## The Trace Form and the Operators

**Theorem (the multiplication operator).** The multiplication operator of the block becomes the **symmetrised multiplication** of the regular matrix:

$$
\mathsf{M}_4\bigl(L^{\bullet}_{\tilde A}\tilde Q\bigr)=\tfrac12\bigl(\mathsf{M}_4(\tilde A)\mathsf{M}_4(\tilde Q)+\mathsf{M}_4(\tilde Q)\mathsf{M}_4(\tilde A)\bigr),
$$

so the operator $L^{\bullet}_{\tilde A}$ is carried to the map $M\mapsto\tfrac12(\mathsf{M}_4(\tilde A)M+M\mathsf{M}_4(\tilde A))$ on the image of $\mathsf{M}_4$.

*Proof.* Apply $\mathsf{M}_4$ to $L^{\bullet}_{\tilde A}\tilde Q=\tfrac12(\tilde A\tilde Q+\tilde Q\tilde A)$ and use the multiplicativity of $\mathsf{M}_4$. Verified on the model. $\square$

**Theorem (the invariants of the operator).** The trace and the determinant of the operator are the matrix invariants

$$
\operatorname{Tr}\bigl(L^{\bullet}_{\tilde A}\bigr)=\operatorname{Tr}\mathsf{M}_4(\tilde A)=4A_0,\qquad
\det\bigl(L^{\bullet}_{\tilde A}\bigr)=A_0^2N(\tilde A).
$$

*Proof.* The operator is the sum of the two maps $M\mapsto\tfrac12\mathsf{M}_4(\tilde A)M$ and $M\mapsto\tfrac12 M\mathsf{M}_4(\tilde A)$. On the four-dimensional space each one-sided map has trace $\operatorname{Tr}\mathsf{M}_4(\tilde A)=4A_0$, so each half has trace $2A_0$ and the sum has trace $4A_0$; the determinant $A_0^2N(\tilde A)$ is that of *The Multiplication Operators of the Symmetric Plain Algebra*, recomputed in the model. Verified on the model. $\square$

**Remark (the operator and the trace form).** The multiplication operator of the block is the **average of the two one-sided regular matrix multiplications**, and its trace is the trace of the regular matrix and not twice it. The trace form is a quarter of the matrix trace of the product, $\tau(\tilde P,\tilde Q)=\tfrac14\operatorname{Tr}(\mathsf{M}_4(\tilde P)\mathsf{M}_4(\tilde Q))$, while the trace of the product of the two plain operators is $\operatorname{Tr}(L_{\tilde P}L_{\tilde Q})=4\tau(\tilde P,\tilde Q)$; the two agree in the model exactly when the operator trace coincides with the form. **The model carries the operators to the symmetrised regular matrix multiplications and the trace form to a quarter of the trace of the matrix product**, and the transport agrees with the coordinate computation. Verified on the model with random pairs.

## The Derivations and the Automorphisms

**Theorem (the derivations).** The inner derivations are the **matrix commutators**:

$$
\mathsf{M}_4\bigl(\tfrac14\operatorname{ad}_{\tilde C}\tilde X\bigr)=\tfrac14\bigl[\mathsf{M}_4(\tilde C),\mathsf{M}_4(\tilde X)\bigr],
$$

so the derivation algebra of the block is carried to the commutator algebra of the trace-zero regular matrices, of complex dimension three.

*Proof.* $\operatorname{ad}_{\tilde C}=L_{\tilde C}-R_{\tilde C}$ and $\mathsf{M}_4(L_{\tilde C}\tilde X-R_{\tilde C}\tilde X)=\mathsf{M}_4(\tilde C\tilde X-\tilde X\tilde C)=\mathsf{M}_4(\tilde C)\mathsf{M}_4(\tilde X)-\mathsf{M}_4(\tilde X)\mathsf{M}_4(\tilde C)=[\mathsf{M}_4(\tilde C),\mathsf{M}_4(\tilde X)]$; the factor $\tfrac14$ is the one of *The Multiplication Operators of the Symmetric Plain Algebra*. Verified on the model. $\square$

**Theorem (the automorphisms).** The automorphisms are the **conjugations** and the **transposition-like maps**:

$$
\mathsf{M}_4\bigl(\operatorname{Ad}_{\tilde A}\tilde X\bigr)=\mathsf{M}_4(\tilde A)\mathsf{M}_4(\tilde X)\mathsf{M}_4(\tilde A)^{-1},\qquad
\mathsf{M}_4(\tilde X^{\natural})=\mathsf{M}_4(\tilde X)^{\mathsf T},
$$

for a unit $\tilde A$, where the natural conjugation is read on the regular matrix as the transpose.

*Proof.* The inner automorphism is the conjugation by the unit by *The Multiplication Operators of the Symmetric Plain Algebra*, and $\mathsf{M}_4$ is multiplicative. The natural conjugation satisfies $\mathsf{M}_4(\tilde X^{\natural})=\mathsf{M}_4(\tilde X)^{\mathsf T}$ by the transpose identity of the regular model; the transpose is an anti-automorphism of the matrix product and an automorphism of the symmetrised regular product. Verified on the model. $\square$

**Remark (the regular model and the two groups).** The automorphism group of the block is the inner conjugations together with the natural conjugation, of dimension three, with the commutator algebra of the trace-zero regular matrices as Lie algebra; the structure group of *The Multiplication Operators of the Symmetric Plain Algebra*, the norm similarities, is the larger group carried to the **similarities of the determinant** of the regular model,

$$
\Gamma=\bigl\{g:\det\mathsf{M}_4(g\tilde X)=\nu(g)\det\mathsf{M}_4(\tilde X)\bigr\},
$$

of dimension seven. **In the model the automorphisms are the conjugations and the transposes, and the structure group is the group of determinant similarities**; the derivations are the commutators with the trace-zero regular matrices. Verified on the model.

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

The general element has trace $4Q_0$ and determinant $N(\tilde Q)^2$.

**The product, entry by entry.** The block's product is the **anticommutator** of the regular matrices,

$$
\mathsf{M}_4(\tilde P\bullet\tilde Q)=\tfrac12\bigl\{\mathsf{M}_4(\tilde P),\mathsf{M}_4(\tilde Q)\bigr\}
=\tfrac12\bigl(\mathsf{M}_4(\tilde P)\mathsf{M}_4(\tilde Q)+\mathsf{M}_4(\tilde Q)\mathsf{M}_4(\tilde P)\bigr),
$$

and on the unit $e_1$ the square is the negative identity of the regular model,

$$
\mathsf{M}_4(e_1)^2=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix}^2=-I_4=-\mathsf{M}_4(e_0).
$$

**The idempotents, entry by entry.** The idempotent $\tfrac12(e_0+ie_1)$ is the projector

$$
\mathsf{M}_4\bigl(\tfrac12(e_0+ie_1)\bigr)=\tfrac12\bigl(I_4+i\mathsf{M}_4(e_1)\bigr),
\qquad
i\mathsf{M}_4(e_1)=\begin{pmatrix}0&-i&0&0\\i&0&0&0\\0&0&0&-i\\0&0&i&0\end{pmatrix},
$$

whose involution squares to $I_4$, so that the value is a projector of rank two and trace two; **the rank and the trace of the projector are one in the realization and two in the regular model**, the two values of $\tfrac12\operatorname{Tr}\mathsf{M}(\tilde Q)$ on the same element.

**The isotropic cone, entry by entry.** The element $e_1+ie_2$ is of square zero and its regular matrix is $\mathsf{M}_4(e_1+ie_2)=\mathsf{M}_4(e_1)+i\mathsf{M}_4(e_2)$, of vanishing square; the element $e_0+ie_1$ is isotropic without being of square zero and its regular matrix is $I_4+i\mathsf{M}_4(e_1)$, of rank two and trace four, not nilpotent. As in the realization, the two kinds of isotropic element are the two kinds of singular regular matrix.

## Summary

In the $4\times4$ regular model the block's product becomes the symmetrisation of the regular matrix product, $\mathsf{M}_4(\tilde P\bullet\tilde Q)=\tfrac12(\mathsf{M}_4(\tilde P)\mathsf{M}_4(\tilde Q)+\mathsf{M}_4(\tilde Q)\mathsf{M}_4(\tilde P))$, the square becomes the matrix square, and the regular matrix's characteristic polynomial is the square of the quadratic, $\det(\lambda I-\mathsf{M}_4(\tilde Q))=(\lambda^2-2Q_0\lambda+N(\tilde Q))^2$. The idempotents give the regular projectors of trace two and rank two, the two copies of the simple module carrying one projector each. The generic norm is the determinant, $\det\mathsf{M}_4(\tilde Q)=N(\tilde Q)^2$, so the isotropic cone is the set of singular matrices of rank two and the elements of square zero are the nilpotent matrices; the isotropic cone is the nilpotent matrices together with the singular matrices of non-zero trace, the witnesses being $e_1+ie_2$ and $e_0+ie_1$. The trace form is a quarter of the trace of the matrix product, $\tau(\tilde P,\tilde Q)=\tfrac14\operatorname{Tr}(\mathsf{M}_4(\tilde P)\mathsf{M}_4(\tilde Q))$, the multiplication operator is the averaged one-sided regular matrix multiplication of trace $\operatorname{Tr}\mathsf{M}_4(\tilde A)=4A_0$ and determinant $A_0^2N(\tilde A)$, the derivations are the commutators with the trace-zero regular matrices, and the automorphisms are the conjugations together with the transpose of the natural conjugation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_{\tilde Q}(\tilde R)=\tilde Q\tilde R$ | the $4\times4$ left regular representation |
| $\mathsf{M}_4(\tilde P\bullet\tilde Q)=\tfrac12(\mathsf{M}_4(\tilde P)\mathsf{M}_4(\tilde Q)+\mathsf{M}_4(\tilde Q)\mathsf{M}_4(\tilde P))$ | the block's product in the model |
| $\det(\lambda I-\mathsf{M}_4(\tilde Q))=(\lambda^2-2Q_0\lambda+N(\tilde Q))^2$ | the squared characteristic polynomial |
| $\det\mathsf{M}_4(\tilde Q)=N(\tilde Q)^2$ | the generic norm as a determinant |
| $\tau(\tilde P,\tilde Q)=\tfrac14\operatorname{Tr}(\mathsf{M}_4(\tilde P)\mathsf{M}_4(\tilde Q))$ | the trace form as a matrix trace |
| $\tfrac14\operatorname{ad}_{\tilde C}\leftrightarrow\tfrac14[\mathsf{M}_4(\tilde C),\cdot]$ | the inner derivations as commutators |
| $\mathsf{M}_4(\tilde X^{\natural})=\mathsf{M}_4(\tilde X)^{\mathsf T}$ | the natural conjugation as the transpose |

## Further Reading

- *The General Plain Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$* (`articles_maths/the-general-plain-algebra-in-the-4x4-matrix-element-representation.md`), for the model.
- *The Symmetric Plain Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/the-symmetric-plain-algebra-in-the-2x2-matrix-element-representation.md`), for the reading on the realization.
- *The 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions* (`articles_maths/the-4x4-matrix-element-representation-of-biquaternions.md`), for the element tables of the model.
- *Biquaternion Objects and Their Matrix Correspondences* (`articles_maths/biquaternion-objects-and-their-matrix-correspondences.md`), for the correspondence between the objects and the matrices.
- *Biquaternion Idempotents and Projections* and *Biquaternion Ideals and Peirce Decomposition*, for the idempotents, the projectors and the minimal left ideals.
- *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*, *The Trace Form and the Invariance of the Symmetric Plain Algebra* and *The Multiplication Operators of the Symmetric Plain Algebra*, for the coordinate statements transported here.
