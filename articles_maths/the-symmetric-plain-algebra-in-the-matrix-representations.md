# __The Symmetric Plain Algebra in the Matrix Representations__

## Introduction

The symmetric plain algebra of $\mathbb{B}$ carries the product $\tilde P\bullet\tilde Q=\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ of *Introduction to the Symmetric Plain Algebra of Biquaternions*, and the algebra carries two matrix models: the $2\times2$ realization $\Phi:\mathbb{B}\to M_2(\mathbb{C})$ of *The General Plain Algebra in the $2\times2$ Matrix Representation* and the $4\times4$ left regular representation $\rho_L$ of *The General Plain Algebra in the $4\times4$ Regular Matrix Representation*. This article reads the block through the two models: the square and the polarisation, the idempotents, the isotropic cone and the elements of square zero, and the trace form and its operators, all transported to the matrices.

The transport is short because the symmetrisation of the plain product becomes the symmetrisation of the matrix product in either model: the plain product is the matrix product, so the block's product is the half-sum of a matrix and its exchanged product. What the models add is the matrix reading of every notion at once — the square as an ordinary matrix square, the quadratic identity as the Cayley–Hamilton identity, the idempotents as ordinary projectors, the isotropic cone as the singular matrices, the elements of square zero as the nilpotent matrices, the trace form as a scaled matrix trace — and the matrix list of the idempotents and of the non-isotropic elements.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$ and central scalar imaginary $i$; an element is $\tilde Q=\sum_\mu Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$; the generic norm is $N(\tilde Q)=\sum_\mu Q_\mu^2$ and the trace form is $\tau(\tilde P,\tilde Q)=P_0Q_0-(\mathbf{P},\mathbf{Q})$. The $2\times2$ realization is $\Phi(e_0)=I$ and $\Phi(e_k)=-i\sigma_k$ with the Pauli matrices $\sigma_k$, an isomorphism of algebras with $\operatorname{Tr}\Phi(\tilde Q)=2Q_0$, $\det\Phi(\tilde Q)=N(\tilde Q)$ and $\Phi(\tilde Q^{\natural})=\operatorname{adj}\Phi(\tilde Q)$; the regular representation is $\rho_L(\tilde Q)(\tilde R)=\tilde Q\tilde R$, with $\operatorname{Tr}\rho_L(\tilde Q)=4Q_0$, $\det\rho_L(\tilde Q)=N(\tilde Q)^2$, $\rho_R(\tilde Q)=E\rho_L(\tilde Q)^{\mathsf T}E$ and $\rho_L(\tilde Q^{\natural})=\rho_L(\tilde Q)^{\mathsf T}$. The matrices $\rho_L(\tilde Q)$ and $\rho_R(\tilde Q)$ are the plain and right regular matrices of *The General Plain Algebra in the $4\times4$ Regular Matrix Representation*.

## The Two Models

### The Two by Two Model

**Theorem.** The block's product becomes the symmetrisation of the matrix product:

$$
\Phi\bigl(\tilde P\bullet\tilde Q\bigr)=\tfrac12\bigl(\Phi(\tilde P)\Phi(\tilde Q)+\Phi(\tilde Q)\Phi(\tilde P)\bigr).
$$

*Proof.* $\Phi$ is an algebra isomorphism, so $\Phi(\tilde P\bullet\tilde Q)=\tfrac12\bigl(\Phi(\tilde P\tilde Q)+\Phi(\tilde Q\tilde P)\bigr)=\tfrac12\bigl(\Phi(\tilde P)\Phi(\tilde Q)+\Phi(\tilde Q)\Phi(\tilde P)\bigr)$. Verified on the model.

So the block is the image under $\Phi$ of the symmetrized matrix algebra, and the isomorphism of *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra* with the symmetrised matrices is this transport.

### The Four by Four Regular Model

**Theorem.** The block's product becomes the symmetrisation of the regular matrix product:

$$
\rho_L\bigl(\tilde P\bullet\tilde Q\bigr)=\tfrac12\bigl(\rho_L(\tilde P)\rho_L(\tilde Q)+\rho_L(\tilde Q)\rho_L(\tilde P)\bigr),\qquad
\rho_R\bigl(\tilde P\bullet\tilde Q\bigr)=\tfrac12\bigl(\rho_R(\tilde P)\rho_R(\tilde Q)+\rho_R(\tilde Q)\rho_R(\tilde P)\bigr).
$$

*Proof.* $\rho_L$ is an algebra homomorphism, $\rho_L(\tilde P\bullet\tilde Q)=\tfrac12(\rho_L(\tilde P\tilde Q)+\rho_L(\tilde Q\tilde P))=\tfrac12(\rho_L(\tilde P)\rho_L(\tilde Q)+\rho_L(\tilde Q)\rho_L(\tilde P))$, and the same computation holds for $\rho_R$. Verified on the model.

**Remark (the two models and the two carriers).** The $2\times2$ model is faithful and minimal, and the $4\times4$ model is the direct sum of two copies of it, carried by the coefficient space. **Both models turn the block into the symmetrisation of a matrix algebra**, and the invariants of the two transports differ by the dimension factor: the trace is $2Q_0$ against $4Q_0$ and the determinant is $N$ against $N^2$. The relation of the two transports is read in *Biquaternion Objects and Their Matrix Correspondences*.

## The Square and the Polarisation in the Models

### The Square

**Theorem.** The square of the block is the matrix square:

$$
\Phi\bigl(\tilde Q\bullet\tilde Q\bigr)=\Phi(\tilde Q)^2,\qquad
\rho_L\bigl(\tilde Q\bullet\tilde Q\bigr)=\rho_L(\tilde Q)^2 .
$$

*Proof.* The square of the block is the plain square $\tilde Q^2$ by *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*, and the models are multiplicative on the plain product. Verified on the models.

### The Cayley–Hamilton Identity

**Theorem.** In the $2\times2$ model the block's quadratic identity is the **Cayley–Hamilton identity**:

$$
\Phi(\tilde Q)^2-2Q_0\Phi(\tilde Q)+N(\tilde Q)I=0,\qquad
\lambda^2-2Q_0\lambda+N(\tilde Q)=0,
$$

the second display being the characteristic polynomial of $\Phi(\tilde Q)$.

*Proof.* Apply $\Phi$ to the quadratic identity $\tilde Q\bullet\tilde Q-T(\tilde Q)\tilde Q+N(\tilde Q)e_0=0$ and use $\Phi(e_0)=I$, $\Phi(\tilde Q\bullet\tilde Q)=\Phi(\tilde Q)^2$, $T(\tilde Q)=2Q_0$ and $\Phi(\tilde Q)^2-2Q_0\Phi(\tilde Q)+N(\tilde Q)I=0$, whose left side is the characteristic polynomial of the $2\times2$ matrix $\Phi(\tilde Q)$ by Cayley–Hamilton. Verified on the model.

**Remark (the regular matrix and the squared polynomial).** In the $4\times4$ model the characteristic polynomial of the regular matrix is the **square** of the quadratic:

$$
\det\bigl(\lambda I-\rho_L(\tilde Q)\bigr)=\bigl(\lambda^2-2Q_0\lambda+N(\tilde Q)\bigr)^2,
$$

because the regular module is the direct sum of the two copies of the simple module, so each eigenvalue of $\Phi(\tilde Q)$ occurs twice. The trace $4Q_0$ and the determinant $N^2$ of $\rho_L(\tilde Q)$ are the two coefficients of the squared polynomial that the dimension allows to be read; **the quadratic identity is a degree-two statement in both models, and the regular matrix sees it twice.** Verified on the model.

### The Quadratic Form and the Trace Form

**Theorem.** The quadratic trace and the trace form become scaled matrix traces:

$$
\mathrm{Sc}\bigl(\tilde Q\bullet\tilde Q\bigr)=\tfrac12\operatorname{Tr}\bigl(\Phi(\tilde Q)^2\bigr),\qquad
\tau(\tilde P,\tilde Q)=\tfrac12\operatorname{Tr}\bigl(\Phi(\tilde P)\Phi(\tilde Q)\bigr)=\tfrac14\operatorname{Tr}\bigl(\rho_L(\tilde P)\rho_L(\tilde Q)\bigr).
$$

*Proof.* $\mathrm{Sc}(\tilde Q^2)=\tfrac12\operatorname{Tr}(\Phi(\tilde Q)^2)$ is the trace pairing of the $2\times2$ model evaluated on $\tilde Q=\tilde P$; for the general form, $\tau(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\bullet\tilde Q)=\tfrac12\bigl(\mathrm{Sc}(\tilde P\tilde Q)+\mathrm{Sc}(\tilde Q\tilde P)\bigr)=\mathrm{Sc}(\tilde P\tilde Q)=\tfrac12\operatorname{Tr}(\Phi(\tilde P)\Phi(\tilde Q))$. In the regular model $\tfrac12\operatorname{Tr}(\rho_L(\tilde P)\rho_L(\tilde Q))=2\,\mathrm{Sc}(\tilde P\tilde Q)$, so the trace of the regular matrices is four times the form. Verified on the models.

**Remark (the polarisation on the matrices).** The quadratic form $\tilde Q\mapsto\tfrac12\operatorname{Tr}(\Phi(\tilde Q)^2)$ polarises to the bilinear form $\tfrac12\operatorname{Tr}(\Phi(\tilde P)\Phi(\tilde Q))$, and the product is recovered from the square by polarisation: $\Phi(\tilde P\bullet\tilde Q)=\tfrac12\bigl(\Phi(\tilde P)\Phi(\tilde Q)+\Phi(\tilde Q)\Phi(\tilde P)\bigr)$, equivalently $\tfrac12$ times the polarisation of the matrix square. **The whole degree-two structure of the block is the Cayley–Hamilton structure of the $2\times2$ matrices**; the polarisation that recovers the product from the form is *The Trace Form and the Invariance of the Symmetric Plain Algebra*. Verified on the model.

## The Idempotents in the Models

### The Projectors

**Theorem.** In the $2\times2$ model the non-trivial idempotents of the block are the **projectors** of rank one, and for a root $\xi$ of $-1$,

$$
\Phi\bigl(\tfrac12(e_0+\xi i)\bigr)=\tfrac12\bigl(I+J\bigr),\qquad J=i\Phi(\xi),\qquad J^2=I .
$$

*Proof.* $\Phi(\xi)^2=\Phi(\xi^2)=\Phi(-e_0)=-I$, so $J^2=i^2\Phi(\xi)^2=(-1)(-I)=I$; hence $\Phi(\tilde\Pi)^2=\tfrac14(I+J)^2=\tfrac14(2I+2J)=\tfrac12(I+J)=\Phi(\tilde\Pi)$, so the image is idempotent with eigenvalues $1,0$, that is a projector of rank one, of trace $\operatorname{Tr}\Phi(\tilde\Pi)=2\Pi_0=1$. Verified on the model.

**Theorem.** The Hermitian idempotents are the **Hermitian projectors**: for a unit real vector $\hat\mu$ in $\mathbb{R}^3$,

$$
\Phi\bigl(\tfrac12(e_0+i\hat\mu)\bigr)=\tfrac12\bigl(I+i\Phi(\hat\mu)\bigr)
$$

is a self-adjoint projector of the model, of kernel the complementary minimal left ideal.

*Proof.* The Hermitian conjugation satisfies $\Phi(\tilde Q^{*})=\Phi(\tilde Q)^{\dagger}$ in the model, so a Hermitian element has a Hermitian matrix; a Hermitian idempotent therefore has a Hermitian projector with $\Phi(\tilde\Pi)^2=\Phi(\tilde\Pi)$ and $\Phi(\tilde\Pi)^{\dagger}=\Phi(\tilde\Pi)$. The kernel and the image are the two minimal left ideals of the Peirce decomposition of *Biquaternion Ideals and Peirce Decomposition*. Verified on the model.

**Remark (the model separates the families).** The trivial idempotents are the scalar projectors $0$ and $I$; the Hermitian idempotents are the rank-one projectors $\tfrac12(I+J)$ with $J$ a Hermitian involution of trace $0$; and the non-Hermitian idempotents are the rank-one projectors $\tfrac12(I+J)$ with $J=i\Phi(\xi)$ for a non-real root $\xi$, whose involution is not Hermitian. **The three families of idempotents are the three families of rank-one projectors of $M_2(\mathbb{C})$ cut by the involution.** Verified on the model.

### The Idempotents in the Regular Model

**Theorem.** In the $4\times4$ model an idempotent $\tilde\Pi$ gives the regular projector $\rho_L(\tilde\Pi)$ of trace $4\Pi_0=2$ and rank two, with the eigenvalues $1,1,0,0$; the two copies of the simple module carry one projector each.

*Proof.* $\rho_L(\tilde\Pi)^2=\rho_L(\tilde\Pi)$ by the transport of the square, so the regular matrix is a projector, of trace $\operatorname{Tr}\rho_L(\tilde\Pi)=4\Pi_0=2$ for a non-trivial idempotent; the regular module is the direct sum of the two copies of the simple module, and on each copy the projector has rank one, so the rank is two and the eigenvalues are $1,1,0,0$. Verified on the model.

## The Isotropic Cone in the Models

### The Determinant and the Norm

**Theorem.** In both models the generic norm is a determinant:

$$
\det\Phi(\tilde Q)=N(\tilde Q),\qquad \det\rho_L(\tilde Q)=N(\tilde Q)^2 .
$$

*Proof.* The determinant of the $2\times2$ model is $N$ by *The General Plain Algebra in the $2\times2$ Matrix Representation*; the determinant of the regular matrix is the square of it because the regular module is the direct sum of the two copies of the simple module. Verified on the models.

### The Isotropic Elements

**Theorem.** The isotropic cone of the block is the set of **singular matrices** in either model:

$$
N(\tilde Q)=0\iff \Phi(\tilde Q)\ \text{singular}\iff\rho_L(\tilde Q)\ \text{singular}.
$$

*Proof.* $\det\Phi(\tilde Q)=N(\tilde Q)$ and $\det\rho_L(\tilde Q)=N(\tilde Q)^2$; a matrix is singular exactly when its determinant vanishes, and the vanishing of $N$ and of $N^2$ are the same condition. Verified on the models.

**Remark (the rank of the isotropic matrices).** A non-zero isotropic element has a non-zero singular matrix; in the $2\times2$ model it is of **rank one**, hence of the form $uv^{\mathsf T}$, and in the regular model it is of rank two. **The isotropic cone of the block is the cone of the rank-one matrices in the $2\times2$ model**, and the zero divisors are the rank-one matrices; the two descriptions of *Biquaternion Zero Divisors* and *The General Plain Algebra in the $2\times2$ Matrix Representation* are the same list. Verified on the model.

### The Elements of Square Zero

**Theorem.** The elements of square zero are exactly the **nilpotent** matrices:

$$
\tilde Q\bullet\tilde Q=0\iff\Phi(\tilde Q)^2=0\iff\Phi(\tilde Q)\ \text{nilpotent},\qquad
\rho_L(\tilde Q)^2=0 .
$$

*Proof.* $\Phi(\tilde Q\bullet\tilde Q)=\Phi(\tilde Q)^2$ by the transport of the square, so the square of the block vanishes exactly when the matrix square vanishes, and a $2\times2$ matrix with vanishing square is nilpotent; a nilpotent $2\times2$ matrix is either zero or of rank one with vanishing trace. The regular matrix has vanishing square exactly when its two simple blocks do, so the two conditions agree. Verified on the models.

**Remark (the isotropic matrices split into the nilpotent and the non-nilpotent).** The isotropic cone is the union of the origin, the **nilpotent** matrices, which are the images of the elements of square zero, and the **singular non-nilpotent** matrices, which are the images of the isotropic elements that are not of square zero. The element $e_1+ie_2$ is of square zero, and $\Phi(e_1+ie_2)=\begin{pmatrix}0&-2i\\0&0\end{pmatrix}$ is nilpotent of trace $0$; the element $e_0+ie_1$ is isotropic without being of square zero, and $\Phi(e_0+ie_1)=\begin{pmatrix}1&1\\1&1\end{pmatrix}$ is singular of rank one and of trace $2$, not nilpotent. **The two model descriptions of the isotropic cone are the nilpotent matrices together with the singular matrices of non-zero trace.** Verified on the witnesses.

## The Trace Form and the Operators in the Models

**Theorem.** The multiplication operator of the block becomes the **symmetrised multiplication** of the matrix:

$$
\Phi\bigl(L^{\bullet}_{\tilde A}\tilde Q\bigr)=\tfrac12\bigl(\Phi(\tilde A)\Phi(\tilde Q)+\Phi(\tilde Q)\Phi(\tilde A)\bigr),
$$

so the operator $L^{\bullet}_{\tilde A}$ is carried to the map $M\mapsto\tfrac12(\Phi(\tilde A)M+M\Phi(\tilde A))$ on $M_2(\mathbb{C})$, and likewise for $\rho_L$ on $M_4(\mathbb{C})$.

*Proof.* Apply $\Phi$ to $L^{\bullet}_{\tilde A}\tilde Q=\tfrac12(\tilde A\tilde Q+\tilde Q\tilde A)$ and use the multiplicativity of $\Phi$. Verified on the model.

**Theorem.** The trace and the determinant of the operator are the matrix invariants

$$
\operatorname{Tr}\bigl(L^{\bullet}_{\tilde A}\bigr)=2\operatorname{Tr}\Phi(\tilde A)=4A_0,\qquad
\det\bigl(L^{\bullet}_{\tilde A}\bigr)=A_0^2N(\tilde A),
$$

in the $2\times2$ model, and the operator trace is $\operatorname{Tr}(L^{\bullet}_{\tilde P}L^{\bullet}_{\tilde Q})=4P_0Q_0-2(\mathbf{P},\mathbf{Q})$ in the coefficient basis.

*Proof.* The operator is the sum of the two maps $M\mapsto\tfrac12\Phi(\tilde A)M$ and $M\mapsto\tfrac12 M\Phi(\tilde A)$. On $M_2(\mathbb{C})$ the map $M\mapsto AM$ has trace $2\operatorname{Tr}A$, so each half has trace $\operatorname{Tr}\Phi(\tilde A)=2A_0$ and the sum has trace $4A_0$; the determinant $A_0^2N(\tilde A)$ is that of *The Multiplication Operators of the Symmetric Plain Algebra* and the operator trace $\operatorname{Tr}(L^{\bullet}_{\tilde P}L^{\bullet}_{\tilde Q})=4P_0Q_0-2(\mathbf{P},\mathbf{Q})$ that of *The Trace Form and the Invariance of the Symmetric Plain Algebra*, both recomputed in the model. Verified on the model.

**Remark (the two operators and the two traces).** The multiplication operator of the block is the **average of the two one-sided matrix multiplications**, and the trace of that average is the trace of the matrix and not twice it; the operator trace is

$$
\operatorname{Tr}\bigl(L^{\bullet}_{\tilde P}L^{\bullet}_{\tilde Q}\bigr)=4P_0Q_0-2(\mathbf{P},\mathbf{Q})=2\tau(\tilde P,\tilde Q)+\tfrac12T(\tilde P)T(\tilde Q),
$$

which is not a multiple of the trace form $\tau(\tilde P,\tilde Q)=P_0Q_0-(\mathbf{P},\mathbf{Q})$, since the two coefficient pairs $(4,-2)$ and $(1,-1)$ are not proportional. **The operator trace is not the trace form**, and it agrees with the trace of the product of the two plain operators, $\operatorname{Tr}(L_{\tilde P}L_{\tilde Q})=4\tau(\tilde P,\tilde Q)$, exactly when $(\mathbf{P},\mathbf{Q})=0$; the two differ at $\tilde P=\tilde Q=e_1$, where the operator trace is $-2$ against $4\tau=-4$. **The models carry the operators to the symmetrised matrix multiplications and the trace form to the half trace of the matrix square**, and the two transports agree with the coordinate computation. Verified on the model with random pairs and on the witnesses.

## The Derivations and the Automorphisms in the Models

**Theorem.** In the models the inner derivations are the **matrix commutators**:

$$
\Phi\bigl(\tfrac14\operatorname{ad}_{\tilde C}\tilde X\bigr)=\tfrac14\bigl[\Phi(\tilde C),\Phi(\tilde X)\bigr],
$$

so the derivation algebra of the block is carried to the commutator algebra of the trace-zero matrices, $\mathfrak{sl}(2,\mathbb{C})$.

*Proof.* $\operatorname{ad}_{\tilde C}=L_{\tilde C}-R_{\tilde C}$ and $\Phi(L_{\tilde C}\tilde X-R_{\tilde C}\tilde X)=\Phi(\tilde C\tilde X-\tilde X\tilde C)=\Phi(\tilde C)\Phi(\tilde X)-\Phi(\tilde X)\Phi(\tilde C)=[\Phi(\tilde C),\Phi(\tilde X)]$; the trace-zero matrices are the commutators, and the factor $\tfrac14$ is the one of *The Multiplication Operators of the Symmetric Plain Algebra*. Verified on the model.

**Theorem.** In the models the automorphisms are the **conjugations** and the **transposition-like maps**:

$$
\Phi\bigl(\operatorname{Ad}_{\tilde A}\tilde X\bigr)=\Phi(\tilde A)\Phi(\tilde X)\Phi(\tilde A)^{-1},\qquad
\operatorname{adj}\Phi(\tilde X)=J_0\,\Phi(\tilde X)^{\mathsf T}J_0^{-1},\qquad
J_0=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
$$

for a unit $\tilde A$, and with the natural conjugation read on the matrix as $\Phi(\tilde X^{\natural})=\operatorname{adj}\Phi(\tilde X)$.

*Proof.* The inner automorphism is the conjugation by the unit by *The Multiplication Operators of the Symmetric Plain Algebra*, and $\Phi$ is multiplicative. The natural conjugation satisfies $\Phi(\tilde X^{\natural})=\operatorname{adj}\Phi(\tilde X)$ with $\operatorname{adj}M=(\operatorname{Tr}M)I-M$; for a $2\times2$ matrix $\operatorname{adj}M=J_0M^{\mathsf T}J_0^{-1}$, so the natural conjugation is the transpose composed with the conjugation by the alternating matrix, an anti-automorphism of the matrix product and an automorphism of the symmetrised product. Verified on the model.

**Remark (the models and the two groups).** The automorphism group of the block is the inner conjugations together with the natural conjugation, of dimension three, with the commutator algebra of the trace-zero matrices as Lie algebra; the structure group of *The Multiplication Operators of the Symmetric Plain Algebra*, the norm similarities, is the larger group carried to the **similarities of the determinant** of the matrix model,

$$
\Gamma=\bigl\{g:\det\Phi(g\tilde X)=\nu(g)\det\Phi(\tilde X)\bigr\},
$$

of dimension seven. **In the model the automorphisms are the conjugations and the adjugate-conjugates, and the structure group is the group of determinant similarities**; the derivations are the commutators with the trace-zero matrices. Verified on the model.

## Summary

In the $2\times2$ model the block's product becomes the symmetrisation of the matrix product, $\Phi(\tilde P\bullet\tilde Q)=\tfrac12(\Phi(\tilde P)\Phi(\tilde Q)+\Phi(\tilde Q)\Phi(\tilde P))$, the square becomes the matrix square, and the quadratic identity becomes the Cayley–Hamilton identity $\Phi(\tilde Q)^2-2Q_0\Phi(\tilde Q)+N(\tilde Q)I=0$; in the $4\times4$ regular model the same holds for $\rho_L$, whose characteristic polynomial is the square of the quadratic. The idempotents are the rank-one projectors $\tfrac12(I+i\Phi(\xi))$ over the roots of $-1$, Hermitian for the real roots and not Hermitian otherwise, and the regular projector has trace two and rank two. The generic norm is the determinant, $\det\Phi(\tilde Q)=N(\tilde Q)$ and $\det\rho_L(\tilde Q)=N(\tilde Q)^2$, so the isotropic cone is the set of singular matrices and the elements of square zero are the nilpotent matrices; the isotropic cone is the nilpotent matrices together with the singular matrices of non-zero trace, the witnesses being $e_1+ie_2$ and $e_0+ie_1$. The trace form is the half trace of the matrix product, $\tau(\tilde P,\tilde Q)=\tfrac12\operatorname{Tr}(\Phi(\tilde P)\Phi(\tilde Q))=\tfrac14\operatorname{Tr}(\rho_L(\tilde P)\rho_L(\tilde Q))$, the multiplication operator is the averaged one-sided matrix multiplication of trace $2\operatorname{Tr}\Phi(\tilde A)=4A_0$ and determinant $A_0^2N(\tilde A)$, the derivations are the commutators with the trace-zero matrices, and the automorphisms are the conjugations together with the adjugate-conjugate of the natural conjugation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Phi(e_0)=I$, $\Phi(e_k)=-i\sigma_k$ | the $2\times2$ realization, an algebra isomorphism |
| $\rho_L(\tilde Q)(\tilde R)=\tilde Q\tilde R$ | the $4\times4$ left regular representation |
| $\Phi(\tilde P\bullet\tilde Q)=\tfrac12(\Phi(\tilde P)\Phi(\tilde Q)+\Phi(\tilde Q)\Phi(\tilde P))$ | the block's product in the model |
| $\Phi(\tilde Q)^2-2Q_0\Phi(\tilde Q)+N(\tilde Q)I=0$ | the Cayley–Hamilton identity |
| $\Phi(\tfrac12(e_0+\xi i))=\tfrac12(I+i\Phi(\xi))$ | the idempotents as projectors |
| $\det\Phi(\tilde Q)=N(\tilde Q)$, $\det\rho_L(\tilde Q)=N(\tilde Q)^2$ | the generic norm as a determinant |
| $\tau(\tilde P,\tilde Q)=\tfrac12\operatorname{Tr}(\Phi(\tilde P)\Phi(\tilde Q))$ | the trace form as a matrix trace |
| $\tfrac14\operatorname{ad}_{\tilde C}\leftrightarrow\tfrac14[\Phi(\tilde C),\cdot]$ | the inner derivations as commutators |
| $\Phi(\tilde X^{\natural})=\operatorname{adj}\Phi(\tilde X)$ | the natural conjugation as the adjugate |

## Further Reading

- *The General Plain Algebra in the $2\times2$ Matrix Representation* and *The General Plain Algebra in the $4\times4$ Regular Matrix Representation*, for the two models.
- *Biquaternion 2×2 Matrix Element Representation* and *Biquaternion 4×4 Regular Matrix Element Representation*, for the element tables of the models.
- *Biquaternion Objects and Their Matrix Correspondences*, for the correspondence between the objects and the matrices.
- *Biquaternion Idempotents and Projections* and *Biquaternion Ideals and Peirce Decomposition*, for the idempotents, the projectors and the minimal left ideals.
- *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*, *The Trace Form and the Invariance of the Symmetric Plain Algebra* and *The Multiplication Operators of the Symmetric Plain Algebra*, for the coordinate statements transported here.
