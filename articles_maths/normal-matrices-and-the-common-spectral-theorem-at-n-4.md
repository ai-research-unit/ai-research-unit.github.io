# __Normal Matrices and the Common Spectral Theorem at $n=4$__

## Introduction

**A matrix is normal when $A^{\ast}A=AA^{\ast}$, and exactly then is it unitarily diagonalisable; for a normal $A=U\Lambda U^{\ast}$ one has $A^{\ast}=U\bar\Lambda U^{\ast}$, $A^{\mathsf T}=\bar U\Lambda\bar U^{\ast}$ and $\bar A=\bar U\bar\Lambda\bar U^{\ast}$, so the pair of conjugate unitaries diagonalises all four matrices at once, and a single unitary suffices when $A$ is real or symmetric.**

The article proves the equivalence of normality with unitary diagonalisability, writes the four diagonal forms, identifies the four spectral families and their constraints on the eigenvalues, exhibits a Jordan block of size four as the failure, and reads the result in the axis-free frame, where the left matrix of a real element is a scalar multiple of an orthogonal matrix.

It assumes *The Spectral Theorem: the Hermitian Case at $n=4$* and *The Spectral Theorem: the Anti-Hermitian Case at $n=4$*. The model at order two is *Normal $2\times2$ Matrices and the Common Spectral Theorem*; the fine structure of the spectrum is in *The Minimal Polynomial and the Jordan Form of a $4\times4$ Matrix*.

## Normal Matrices

**Definition.** $A$ is **normal** when $A^{\ast}A=AA^{\ast}$.

**Proposition.** Hermitian, anti-Hermitian and unitary matrices are normal; a scalar multiple of a unitary matrix is normal; sums and products of normal matrices need not be normal.

**Proof.** For $A^{\ast}=\pm A$ the two products $A^{\ast}A$ and $AA^{\ast}$ are equal because $A$ commutes with itself; for $A^{\ast}=A^{-1}$ both products are the identity. For the failure of additivity, the diagonal $D=\operatorname{diag}(1,i,1,i)$ and the symmetric $S=E_{12}+E_{21}$ are both normal, while $D+S$ has the upper-left block $\begin{pmatrix}1&1\\1&i\end{pmatrix}$, for which $X^{\ast}X$ and $XX^{\ast}$ differ in the off-diagonal entries.

**Corollary.** Normality is not a linear condition, since the normal matrices do not form a subspace; it is a quadratic condition on the entries.

**Proof.** The display of the failure.

**Proposition.** $A$ is normal exactly when $\operatorname{tr}(A^{\ast}A)=\sum_k|\lambda_k|^{2}$ and the Frobenius norm of $A$ is the Euclidean norm of the spectrum.

**Proof.** The Schur triangular form gives $\operatorname{tr}(A^{\ast}A)=\sum_k|\lambda_k|^{2}+\sum_{i<j}|t_{ij}|^{2}$, so equality holds exactly when the strictly upper part vanishes.

**Corollary.** Normality is the statement that the triangular form is diagonal, hence that the eigenbasis is orthonormal.

**Proof.** The Schur form is triangular in an orthonormal basis, and it is diagonal exactly when the basis consists of eigenvectors.

## The Common Spectral Theorem

**Theorem.** $A$ is normal if and only if there is a unitary $U$ and a diagonal $\Lambda$ with $A=U\Lambda U^{\ast}$.

**Proof.** If $A=U\Lambda U^{\ast}$ then $A^{\ast}=U\bar\Lambda U^{\ast}$ and the two products are $U|\Lambda|^{2}U^{\ast}$. Conversely, the Schur form is triangular with the eigenvalues on the diagonal, and the hypothesis of normality forces the strictly upper part to vanish.

**Corollary.** For such $A$,
$$
A^{\ast}=U\bar\Lambda U^{\ast},\qquad A^{\mathsf T}=\bar U\Lambda\bar U^{\ast},\qquad \bar A=\bar U\bar\Lambda\bar U^{\ast},
$$
so the unitary $U$ diagonalises $A$ and $A^{\ast}$, and the conjugate unitary $\bar U$ diagonalises $A^{\mathsf T}$ and $\bar A$.

**Proof.** Transpose $U\Lambda U^{\ast}$ and use $\overline{U^{\ast}}=\bar U^{\mathsf T}=(\bar U)^{\ast}$; conjugate the same identity.

**Corollary.** A single unitary diagonalises all four exactly when $\bar U=U$ up to relabelling, which holds when $A$ is real and symmetric, and more generally when the eigenbasis can be chosen closed under conjugation.

**Proof.** $A^{\mathsf T}=A$ forces $\bar U\Lambda\bar U^{\ast}=U\Lambda U^{\ast}$; for a real symmetric $A$ the eigenvectors can be taken real.

**The spectral projectors.** $A=\sum_k\lambda_kP_k$ with $P_k$ the orthogonal projections onto the eigenspaces, $P_jP_k=\delta_{jk}P_k$, $\sum_kP_k=\mathrm I_4$, and each $P_k$ a polynomial in $A$.

**Proof.** The projections are $U\operatorname{diag}(0,\dots,1,\dots,0)U^{\ast}$, and the Lagrange interpolation polynomials in $A$ produce them.

**Corollary.** $A^{\ast}=\sum_k\bar\lambda_kP_k$ and $A$ is determined by its spectrum together with its spectral projectors, so normality makes the matrix a function of the spectrum and the basis.

**Proof.** The spectral resolution and the orthogonality of the projectors.

## The Four Families and Their Constraints

**Theorem.** Each of the following is normal with a constraint on the spectrum, and conversely:

| family | condition | spectral constraint |
|---|---|---|
| Hermitian | $A^{\ast}=A$ | $\lambda_k\in\mathbb{R}$ |
| anti-Hermitian | $A^{\ast}=-A$ | $\lambda_k\in i\mathbb{R}$ |
| unitary | $A^{\ast}=A^{-1}$ | $|\lambda_k|=1$ |
| positive definite | $A^{\ast}=A$, $\langle v,Av\rangle>0$ | $\lambda_k>0$ |

**Proof.** From $A=U\Lambda U^{\ast}$ each condition becomes the corresponding condition on the diagonal entries, and conversely.

**Corollary.** The Hermitian and anti-Hermitian families are the fixed sets of the involutions $A\mapsto A^{\ast}$ and $A\mapsto-A^{\ast}$, the unitary family is the fixed set of $A\mapsto(A^{\ast})^{-1}$ on the invertible matrices, and each of the four is a real algebraic subset of the normal set.

**Proof.** The table, read as equations in the spectral data.

**Corollary.** The intersection of the Hermitian and unitary families is the set of involutions $A^{2}=\mathrm I$, of which the Hermitian idempotents are the positive members.

**Proof.** Real spectrum with unit modulus gives $\lambda\in\{\pm1\}$.

**The four eigenvalues.** At order four the spectrum is a multiset of four complex numbers, and the constraint sets are the real line, the imaginary line, the unit circle and the positive half-line, each counted with multiplicity.

**Proof.** The diagonal form and the table.

## The Failure for Non-Normal Matrices

**Theorem.** A matrix with a Jordan block of size two or more is not normal.

**Proof.** Let $A=\lambda\mathrm I+N$ with $N^{2}=0$, $N\neq0$. Then $A^{\ast}A-AA^{\ast}=N^{\ast}N-NN^{\ast}$, and for $N=E_{12}$ this is $E_{22}-E_{11}\neq0$.

**Corollary.** The nilpotent $J_4=E_{12}+E_{23}+E_{34}$, with $J_4^{4}=0$ and $J_4^{3}=E_{14}\neq0$, is not normal, and no unitary diagonalises it although its only eigenvalue is zero.

**Proof.** $J_4^{\ast}J_4=E_{22}+E_{33}+E_{44}$ and $J_4J_4^{\ast}=E_{11}+E_{22}+E_{33}$, so the defect is $E_{44}-E_{11}$; and a diagonal form would force $J_4=0$, since its only eigenvalue is zero.

**Corollary.** The size-four Jordan block is the extreme failure: its invariant flag has length four, the longest possible at order four.

**Proof.** The flag of $J_4$ is $0\subset\ker J_4\subset\ker J_4^{2}\subset\ker J_4^{3}\subset\mathbb{C}^{4}$, of length four.

**The deficit.** The defect $J_4^{\ast}J_4-J_4J_4^{\ast}=E_{44}-E_{11}$ has operator norm one, and that nonzero value is the measure of the failure: a normal matrix has zero defect, whatever its spectrum.

**Proof.** The two products computed above, and $\lVert E_{44}-E_{11}\rVert=1$ acting on $e_4$.

## The Axis-Free Reading

**Proposition.** In the axis-free frame the left matrix of a real element is a real signed permutation combination and satisfies $L^{\mathsf T}L=N\mathrm I_4$ with $N=Q_t^{2}+B^{2}$, so $L$ is a scalar multiple of an orthogonal matrix and is normal.

**Proof.** $L(\tilde Q)^{\mathsf T}=L(\tilde Q^{\natural})$ and $\tilde Q^{\natural}\tilde Q=\tilde Q\tilde Q^{\natural}=Ne_t$, so both products of $L$ with its transpose are $N\mathrm I_4$.

**Corollary.** The left matrices of the real algebra are normal with spectrum on the circle of radius $\sqrt N$, so the whole real algebra sits inside the normal matrices.

**Proof.** An orthogonal matrix has eigenvalues of modulus one, and multiplying by the scalar $\sqrt N$ scales the moduli.

**The complex case.** For a general complex element the left matrix need not be normal, and it is normal exactly when $\tilde Q^{\natural\ast}\tilde Q=\tilde Q\tilde Q^{\natural\ast}$, that is when the element commutes with its conjugate transpose in the biquaternion algebra.

**Proof.** $L(\tilde Q)^{\ast}=L(\tilde Q^{\natural\ast})$, so $L^{\ast}L=L(\tilde Q^{\natural\ast}\tilde Q)$ and $LL^{\ast}=L(\tilde Q\tilde Q^{\natural\ast})$; the representation is faithful, so the two are equal exactly when the elements are.

**Corollary.** Normality in the algebra is the normality of the left matrix, and the axis-free frame turns the abstract condition into a condition on the four coefficients.

**Proof.** The faithfulness of $L$ and the identity above.

**The warning.** The phrase "the left matrices are normal because they are orthogonal up to a scalar" is true for the real algebra and false for the complex one: over $\mathbb{C}$ a signed permutation with complex coefficients is not a scalar multiple of a unitary matrix.

**Proof.** A complex combination of orthogonal matrices is unitary only if its singular values coincide, which a general combination does not satisfy.

## Summary

Normality $A^{\ast}A=AA^{\ast}$ is equivalent to unitary diagonalisability, which is equivalent to the vanishing of the strictly upper part of the Schur form. For a normal $A=U\Lambda U^{\ast}$ the four matrices $A$, $A^{\ast}$, $A^{\mathsf T}$ and $\bar A$ are diagonalised by the pair $U$, $\bar U$, with $A^{\mathsf T}=\bar U\Lambda\bar U^{\ast}$ and $\bar A=\bar U\bar\Lambda\bar U^{\ast}$; one unitary suffices when the eigenbasis is closed under conjugation, as for a real symmetric matrix.

The four spectral families — Hermitian, anti-Hermitian, unitary, positive definite — are the normal matrices whose spectrum lies on the real line, the imaginary line, the unit circle and the positive half-line. The Jordan block of size four is the extreme failure, with a flag of length four.

In the axis-free frame the left matrix of a real element satisfies $L^{\mathsf T}L=N\mathrm I_4$ and is normal; for a complex element normality holds exactly when the element commutes with its conjugate transpose.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A^{\ast}A=AA^{\ast}$ | normality |
| $A=U\Lambda U^{\ast}$ | the unitary diagonal form |
| $\bar U\Lambda\bar U^{\ast}$ | the diagonal form of the transpose |
| $J_4$ | the nilpotent Jordan block of size four |
| $N=Q_t^{2}+B^{2}$ | the scalar of orthogonality in the axis-free frame |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for normality, the Schur form and the spectral theorem.
- [The Spectral Theorem: the Hermitian Case at $n=4$](the-spectral-theorem-the-hermitian-case-at-n-4.html), for the real spectrum and the projectors.
- [The Spectral Theorem: the Anti-Hermitian Case at $n=4$](the-spectral-theorem-the-anti-hermitian-case-at-n-4.html), for the imaginary spectrum.
- [The Minimal Polynomial and the Jordan Form of a $4\times4$ Matrix](the-minimal-polynomial-and-the-jordan-form-of-a-4x4-matrix.html), for the Jordan block that fails normality.
- [Normal $2\times2$ Matrices and the Common Spectral Theorem](normal-2x2-matrices-and-the-common-spectral-theorem.html), for the case at order two.
