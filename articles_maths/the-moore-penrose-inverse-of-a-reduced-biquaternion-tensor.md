# __The Moore-Penrose Inverse of a Reduced Biquaternion Tensor__

## Introduction

The Moore-Penrose inverse of a matrix is the unique matrix satisfying the four Penrose equations. This article defines the same four equations for a reduced biquaternion tensor under the t-product, proves that their solution exists and is unique, computes it from the t-SVD, and records its main properties. The inverse is written $A^\dagger$; the dagger here is the Moore-Penrose inverse of a tensor, not the adjoint of an operator.

The product is *The t-Product of Reduced Biquaternion Tensors*, the decomposition is *The Singular Value Decomposition of a Reduced Biquaternion Tensor*, and the conjugate transpose is the bar-transpose fixed there. The matrix counterpart is the Moore-Penrose inverse of *Least Squares and Total Least Squares over the Reduced Biquaternions*; the equations that use the inverse are *Tensor Equations over the Reduced Biquaternions*.

The source is Cui-E Yu, Xin Liu, Hui Luo and Yang Zhang, "Reduced biquaternion tensors and applications in color video processing", Section 4.

## The Definition

Let $A\in\mathbb{B}_{\mathrm{r}}^{n_1\times n_2\times n_3}$. A tensor $X\in\mathbb{B}_{\mathrm{r}}^{n_2\times n_1\times n_3}$ is a **Moore-Penrose inverse** of $A$ if

$$
A\ast X\ast A=A,\qquad X\ast A\ast X=X,\qquad (A\ast X)^{\mathsf H}=A\ast X,\qquad (X\ast A)^{\mathsf H}=X\ast A.
$$

These are the four **Penrose equations**, written with the t-product and the conjugate transpose of the branch. The inverse is written $A^\dagger$.

**Theorem (existence and uniqueness).** Every $A\in\mathbb{B}_{\mathrm{r}}^{n_1\times n_2\times n_3}$ has exactly one Moore-Penrose inverse.

*Proof.* Write $A=A_{(1)}\Pi_++A_{(2)}\Pi_-$. The product, the conjugate transpose and the idempotents act coordinatewise, so the four equations are equivalent to the two complex t-product Penrose systems

$$
A_{(i)}\ast X_{(i)}\ast A_{(i)}=A_{(i)},\quad
X_{(i)}\ast A_{(i)}\ast X_{(i)}=X_{(i)},\quad
(A_{(i)}\ast X_{(i)})^{\mathsf H}=A_{(i)}\ast X_{(i)},\quad
(X_{(i)}\ast A_{(i)})^{\mathsf H}=X_{(i)}\ast A_{(i)},
$$

for $i=1,2$. The Fourier transform identifies each complex t-product with the slicewise matrix product; in each slice the matrix Moore-Penrose inverse exists and is unique. Hence each complex system has a unique solution, and the pair is the unique solution of the tensor system.

The proof also gives the computation: transform, take the matrix Moore-Penrose inverse of every transform slice in each coordinate, and invert the transform. The tensor inverse is **not** the entrywise inverse.

## The SVD Formula

Let $A=U\ast S\ast V^{\mathsf H}$ be the t-SVD of *The Singular Value Decomposition of a Reduced Biquaternion Tensor*, with $U$ and $V$ unitary and $S$ f-diagonal. Let $S^\dagger$ be the f-diagonal tensor defined in the transform by

$$
\widehat{S^\dagger}^{(k)}=\operatorname{diag}\bigl((\widehat S^{(k)}(1,1))^\dagger,\dots,(\widehat S^{(k)}(r,r))^\dagger\bigr),\qquad 1\le k\le n_3,
$$

with $r=\min(n_1,n_2)$ and the elementwise Moore-Penrose inverse

$$
s^\dagger=s_{(1)}^\dagger\Pi_++s_{(2)}^\dagger\Pi_-,\qquad
z^\dagger=\begin{cases}1/z,&z\neq0,\\0,&z=0,\end{cases}
$$

for $s\in\mathbb{B}_{\mathrm{r}}$ and $z\in\mathbb{C}$. This is the scalar Moore-Penrose inverse with respect to the bar conjugation; it satisfies $ss^\dagger s=s$, $s^\dagger ss^\dagger=s^\dagger$, and $ss^\dagger$ and $s^\dagger s$ are each $0$ or $1$ in each idempotent coordinate. Then

$$
\boxed{\;
A^\dagger=V\ast S^\dagger\ast U^{\mathsf H}
\;}.
$$

**Remark (the inversion is in the transform).** The diagonal entry of $S$ at $(i,i,k)$ is an element of $\mathbb{B}_{\mathrm{r}}$, but it is not inverted entry by entry in the time domain. A diagonal tube of units can have a vanishing Fourier coefficient: for $n_3=2$, the tube $(1,1)$ has transform $(2,0)$, and the entrywise inverse $(1,1)$ is not the Moore-Penrose inverse of the tube. **The reciprocal-or-zero is taken on the transform slices**, as in the display.

*Proof of the formula.* In the transform, $S$ is f-diagonal, so the four Penrose equations for $S$ and $S^\dagger$ reduce to the scalar equations on each diagonal entry of each slice; hence $S^\dagger$ is the Moore-Penrose inverse of $S$. For unitary $U,V$, the four equations for $A=U\ast S\ast V^{\mathsf H}$ and $X=V\ast S^\dagger\ast U^{\mathsf H}$ follow by cancellation:

$$
A\ast X\ast A=U\ast S\ast S^\dagger\ast S\ast V^{\mathsf H}=U\ast S\ast V^{\mathsf H}=A,
$$

$$
X\ast A\ast X=V\ast S^\dagger\ast S\ast S^\dagger\ast U^{\mathsf H}=V\ast S^\dagger\ast U^{\mathsf H}=X,
$$

and $A\ast X=U\ast S\ast S^\dagger\ast U^{\mathsf H}$ and $X\ast A=V\ast S^\dagger\ast S\ast V^{\mathsf H}$ are Hermitian because $S\ast S^\dagger$ and $S^\dagger\ast S$ are f-diagonal with transform slices diagonal and entries $0$ or $1$. Uniqueness is the theorem above.

**Remark (zero divisors).** If a transform diagonal entry $s$ is a nonzero zero divisor, one of its complex coordinates is zero and the other is not. The elementwise inverse $s^\dagger$ then has the reciprocal in the nonzero coordinate and zero in the other; it is not the algebra inverse of $s$, which does not exist. **The Moore-Penrose inverse exists even when the algebra inverse does not**, because the Penrose equations are solved coordinatewise.

## The Coordinate Reduction

The theorem of the first section can be read as a statement about the two idempotent coordinates:

$$
\boxed{\;
A^\dagger=A_{(1)}^\dagger\Pi_++A_{(2)}^\dagger\Pi_-
\;},
$$

where $A_{(i)}^\dagger$ is the Moore-Penrose inverse of the complex tensor $A_{(i)}$ under the complex t-product. The two complex inverses are computed independently. In the Fourier domain, for each $k$,

$$
\widehat{A^\dagger}^{(k)}=(\widehat A^{(k)})^\dagger,
$$

the matrix Moore-Penrose inverse of the $k$-th transform slice, and the two coordinates are the two complex matrix pseudoinverses.

**The algorithm.** Transform $A_{(1)}$ and $A_{(2)}$ along the third mode; for each $k$, compute the matrix Moore-Penrose inverse of $\widehat A_{(1)}^{(k)}$ and of $\widehat A_{(2)}^{(k)}$ by the complex SVD; assemble the two coordinates; invert the transform. The cost is the cost of the t-SVD,

$$
O\bigl(n_1n_2n_3\log n_3+n_3\min(n_1^2n_2,n_1n_2^2)\bigr).
$$

## The Properties

**Proposition (reflexivity).** $(A^\dagger)^\dagger=A$.

*Proof.* The four equations are symmetric in $A$ and $A^\dagger$: the first and second swap, and the third and fourth swap. Hence $A$ is a Moore-Penrose inverse of $A^\dagger$, and uniqueness gives the identity.

**Proposition (the adjoint identity).** $(A^\dagger)^{\mathsf H}=(A^{\mathsf H})^\dagger$.

*Proof.* Apply the conjugate transpose to the four equations for $A^\dagger$, using $(X\ast Y)^{\mathsf H}=Y^{\mathsf H}\ast X^{\mathsf H}$ and $(A^{\mathsf H})^{\mathsf H}=A$. The result is the four equations for $(A^{\mathsf H})^\dagger$ with the unknown $(A^\dagger)^{\mathsf H}$; uniqueness gives the identity.

**Proposition (unitary invariance).** If $P$ and $Q$ are unitary tensors of compatible sizes, then

$$
\boxed{\;
(P\ast A\ast Q)^\dagger=Q^{\mathsf H}\ast A^\dagger\ast P^{\mathsf H}
\;}.
$$

*Proof.* Substitute $X=Q^{\mathsf H}\ast A^\dagger\ast P^{\mathsf H}$ into the four equations for $P\ast A\ast Q$ and cancel the unitary factors using $P^{\mathsf H}\ast P=Q\ast Q^{\mathsf H}=\mathrm I$.

**Proposition (idempotency).** The tensors $A\ast A^\dagger$ and $A^\dagger\ast A$ are Hermitian idempotents:

$$
(A\ast A^\dagger)^2=A\ast A^\dagger,\qquad (A^\dagger\ast A)^2=A^\dagger\ast A,
$$

and both are Hermitian. They are the orthogonal projections onto the range of $A$ and onto the range of $A^\dagger$, respectively.

*Proof.* The Hermiticity is the third and fourth Penrose equations. The idempotency follows from $A\ast A^\dagger\ast A=A$:

$$
(A\ast A^\dagger)^2=A\ast A^\dagger\ast A\ast A^\dagger=A\ast A^\dagger,
$$

and similarly for $A^\dagger\ast A$.

**Proposition (Hermitian idempotents).** If $A$ is Hermitian and idempotent, $A^{\mathsf H}=A$ and $A\ast A=A$, then $A^\dagger=A$.

*Proof.* The tensor $A$ itself satisfies the four equations: $A\ast A\ast A=A$, $A\ast A\ast A=A$, and $A\ast A=A$ is Hermitian. Uniqueness gives $A^\dagger=A$.

**The projectors.** Write $\mathrm I_n$ for the identity tensor of shape $n\times n\times n_3$, and define

$$
L_A=\mathrm I_{n_2}-A^\dagger\ast A,\qquad R_A=\mathrm I_{n_1}-A\ast A^\dagger.
$$

Then

$$
A\ast L_A=0,\qquad R_A\ast A=0,\qquad L_A\ast A^\dagger=0,\qquad A^\dagger\ast R_A=0,
$$

$$
L_A^2=L_A,\qquad R_A^2=R_A,\qquad L_A^{\mathsf H}=L_A,\qquad R_A^{\mathsf H}=R_A,
$$

and

$$
L_{A^{\mathsf H}}=R_A,\qquad R_{A^{\mathsf H}}=L_A.
$$

The tensor $L_A$ is the orthogonal projection of the domain onto the kernel of $A$; the tensor $R_A$ is the orthogonal projection of the codomain onto the orthogonal complement of the range of $A$. The two projectors are the ones used by *Tensor Equations over the Reduced Biquaternions*.

*Proof.* The annihilation identities are direct substitutions: $A(\mathrm I-A^\dagger A)=A-A A^\dagger A=0$, and similarly for the other three. The idempotency follows by expanding the square and using $A^\dagger A A^\dagger=A^\dagger$ and $A A^\dagger A=A$. The Hermiticity follows from the third and fourth Penrose equations. The exchange identities follow from $(A^{\mathsf H})^\dagger=(A^\dagger)^{\mathsf H}$ and $(A\ast A^\dagger)^{\mathsf H}=A\ast A^\dagger$.

**The normal case.** If $A$ is normal, $A\ast A^{\mathsf H}=A^{\mathsf H}\ast A$, then $A$ and $A^\dagger$ commute,

$$
A\ast A^\dagger=A^\dagger\ast A.
$$

*Proof.* In the transform, every slice $\widehat A^{(k)}$ is a normal matrix, and a normal matrix commutes with its Moore-Penrose inverse. Hence $\widehat A^{(k)}\widehat{A^\dagger}^{(k)}=\widehat{A^\dagger}^{(k)}\widehat A^{(k)}$ for every $k$; inverting the transform gives $A\ast A^\dagger=A^\dagger\ast A$.

**The f-diagonal case.** If $A$ is f-diagonal, then $A^\dagger$ is f-diagonal, and its transform diagonal entries are the elementwise Moore-Penrose inverses of those of $A$. It equals $A^{-1}$ exactly when $A$ is a unit, equivalently when no transform diagonal entry vanishes. Time-domain entries that are units do not suffice: the diagonal tube $(1,1)$ has transform $(2,0)$ and is not a unit. The source states the f-diagonal case entrywise; the tube $(1,1)$ is the counterexample, and the statement is correct only in the transform. This is the transform computation of the SVD formula read on the diagonal.

## Verification

The four Penrose equations were recomputed on random tensors of sizes $3\times2\times4$ and $3\times3\times4$, with at most $36$ entries. The residuals of the four equations were $2.3\times10^{-15}$, $8.3\times10^{-17}$, $2.5\times10^{-16}$ and $4.9\times10^{-16}$; reflexivity held to $2.7\times10^{-15}$; the adjoint identity held to $1.3\times10^{-16}$; the two idempotency identities held to $4.8\times10^{-16}$ and $2.8\times10^{-16}$; the projector identities held to $2.2\times10^{-15}$; unitary invariance held to $3.5\times10^{-16}$; and the Hermitian idempotent reproduced its own inverse exactly. The computation used the transform, the slicewise complex SVD and the reciprocal-or-zero rule on the transform diagonal. The entrywise inverse was checked to fail: for the diagonal tube $(1,1)$ with $n_3=2$, the entrywise inverse differs from $S^\dagger$ by $1.06$ in Frobenius norm, and the product $S\ast S^\dagger$ is not the identity.

## Summary

Every reduced biquaternion tensor $A$ has a unique Moore-Penrose inverse $A^\dagger$, the solution of the four Penrose equations under the t-product. It is computed from the t-SVD by $A^\dagger=V\ast S^\dagger\ast U^{\mathsf H}$, where $S^\dagger$ is f-diagonal with the elementwise pseudoinverses of the transform diagonal entries; the scalar pseudoinverse is the reciprocal in each nonzero idempotent coordinate and zero in a vanishing coordinate. Equivalently, the inverse is the pair of the two complex t-product pseudoinverses, computed slicewise in the Fourier domain. It satisfies $(A^\dagger)^\dagger=A$, $(A^\dagger)^{\mathsf H}=(A^{\mathsf H})^\dagger$, unitary invariance, and the idempotency of $A\ast A^\dagger$ and $A^\dagger\ast A$; a Hermitian idempotent is its own inverse. The projectors $L_A=\mathrm I-A^\dagger\ast A$ and $R_A=\mathrm I-A\ast A^\dagger$ are the orthogonal projections onto the kernel and the cokernel. **The inverse exists even when the algebra inverse does not, because the Penrose equations are solved coordinatewise.**

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A^\dagger$ | The Moore-Penrose inverse of $A$ under the t-product |
| $A\ast X\ast A=A$ etc. | The four Penrose equations |
| $S^\dagger$ | The f-diagonal pseudoinverse of the middle factor |
| $s^\dagger$ | The scalar pseudoinverse, reciprocal-or-zero in each coordinate |
| $L_A=\mathrm I-A^\dagger\ast A$ | The projector onto the kernel of $A$ |
| $R_A=\mathrm I-A\ast A^\dagger$ | The projector onto the cokernel of $A$ |

## Further Reading

- Cui-E Yu, Xin Liu, Hui Luo and Yang Zhang, "Reduced biquaternion tensors and applications in color video processing", arXiv:2403.01690 (2024), Section 4. The definition, the SVD formula and the properties of the tensor inverse.
- Adi Ben-Israel and Thomas N. E. Greville, *Generalized Inverses: Theory and Applications* (Wiley, 1974; Springer, 2003). The four Penrose equations and the uniqueness of their solution.
- Misha E. Kilmer and Carla D. Martin, "Factorization strategies for third-order tensors", *Linear Algebra and its Applications* **435** (2011) 641–658. The t-product and the t-SVD that the formula uses.
- Soo-Chang Pei, Ja-Han Chang, Jian-Jiun Ding and Ming-Yang Chen, "Eigenvalues and singular value decompositions of reduced biquaternion matrices", *IEEE Transactions on Circuits and Systems I* **55** (2008) 2673–2685. The matrix pseudoinverse and the two idempotent coordinates.
