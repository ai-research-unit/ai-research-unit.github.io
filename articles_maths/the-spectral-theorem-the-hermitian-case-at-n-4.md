# __The Spectral Theorem: the Hermitian Case at $n=4$__

## Introduction

**A Hermitian matrix of order four has four real eigenvalues and an orthonormal eigenbasis, so it is a real linear combination of four orthogonal projections that are polynomials in it; the eigenvalues are given by the min-max principle, they interlace on every principal submatrix of order three, and the set of matrices with nonnegative spectrum is the closed convex cone that carries the order.**

The article proves the spectral theorem in the Hermitian case, writes the spectral resolution with its projectors, proves the Courant–Fischer formula and the interlacing inequality, describes the cone and the order it defines, compares the spectral decomposition with the Peirce decomposition at a Hermitian idempotent, and reads the trace, the determinant and the elementary symmetric functions as sums of powers and products of the eigenvalues.

It assumes *Normal Matrices and the Common Spectral Theorem at $n=4$* for the diagonal form and *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric* for the dimensions. The model at order two is *The Spectral Theorem: the Hermitian Case and the Sphere of Idempotents*; the cone is *The Positive Cone and Its Boundary at $n=4$*.

## The Theorem and the Projectors

**Theorem.** For Hermitian $A$ there are real numbers $\lambda_1\ge\lambda_2\ge\lambda_3\ge\lambda_4$ and an orthonormal basis $u_1,\dots,u_4$ with $Au_k=\lambda_ku_k$; the eigenvalues are real and the eigenvectors of distinct eigenvalues are orthogonal.

**Proof.** The characteristic polynomial has real coefficients and the matrix is normal, so it is unitarily diagonalisable; for an eigenvector $u$ with eigenvalue $\lambda$, $\lambda\lVert u\rVert^{2}=\langle u,Au\rangle=\overline{\langle Au,u\rangle}=\bar\lambda\lVert u\rVert^{2}$, so $\lambda$ is real; for distinct eigenvalues $\lambda\neq\mu$ the identity $\lambda\langle u,v\rangle=\langle Au,v\rangle=\langle u,Av\rangle=\mu\langle u,v\rangle$ forces orthogonality.

**Corollary.** $A=\sum_{k=1}^{4}\lambda_ku_ku_k^{\ast}$, and each $u_ku_k^{\ast}$ is an orthogonal projection of rank one.

**Proof.** The spectral resolution of the diagonal form.

**Definition.** Grouping equal eigenvalues gives the **spectral projectors** $P_1,\dots,P_r$, with $P_jP_k=\delta_{jk}P_k$, $P_k^{\ast}=P_k$, $\sum_kP_k=\mathrm I_4$, and $A=\sum_k\lambda_kP_k$ with the $\lambda_k$ distinct.

**Proposition.** Each spectral projector is a polynomial in $A$ with real coefficients, and the polynomial depends only on the spectrum.

**Proof.** The Lagrange polynomials $L_k$ with $L_k(\lambda_j)=\delta_{jk}$ give $P_k=L_k(A)$ by the diagonal form, and they have real coefficients because the eigenvalues are real.

**Corollary.** Every matrix commuting with $A$ commutes with each $P_k$, and the commutant of $A$ is the set of matrices that preserve every eigenspace.

**Proof.** $P_k$ is a polynomial in $A$; conversely a matrix preserving the eigenspaces commutes with $A$.

## The Variational Characterisation

**Theorem (Courant–Fischer).** For Hermitian $A$ with eigenvalues $\lambda_1\ge\dots\ge\lambda_4$,
$$
\lambda_k=\max_{\dim V=k}\ \min_{v\in V,\ \lVert v\rVert=1}\langle v,Av\rangle=\min_{\dim W=5-k}\ \max_{v\in W,\ \lVert v\rVert=1}\langle v,Av\rangle.
$$

**Proof.** In the eigenbasis the quadratic form is $\sum\lambda_k|v_k|^{2}$. The min over the $k$-dimensional $V$ of the max is attained at the span of $u_1,\dots,u_k$: any $k$-dimensional $V$ meets the span of $u_{k+1},\dots,u_4$ in a nonzero vector, on which the form is at most $\lambda_k$, and on the first $k$ eigenvectors the form is at least $\lambda_k$. The second formula is the first applied to $-A$.

**Corollary.** $\lambda_1=\max_{\lVert v\rVert=1}\langle v,Av\rangle$ and $\lambda_4=\min_{\lVert v\rVert=1}\langle v,Av\rangle$, so the extreme eigenvalues are the extreme values of the Rayleigh quotient.

**Proof.** The case $k=1$ and $k=4$.

**Corollary.** $A$ is positive semidefinite exactly when $\langle v,Av\rangle\ge0$ for every $v$, and then $\lambda_1=\lVert A\rVert_2$.

**Proof.** The minimum is $\lambda_4$, and the maximum of the modulus of the form is the largest eigenvalue.

## Interlacing

**Theorem (Cauchy interlacing).** Let $B$ be the principal submatrix of $A$ obtained by deleting one row and the corresponding column, with eigenvalues $\mu_1\ge\mu_2\ge\mu_3$. Then
$$
\lambda_1\ge\mu_1\ge\lambda_2\ge\mu_2\ge\lambda_3\ge\mu_3\ge\lambda_4.
$$

**Proof.** Apply the two variational formulas to $A$ on $\mathbb{C}^{4}$ and to the compression $B$ on the three-dimensional coordinate subspace $W$. Every $k$-dimensional subspace of $W$ is a $k$-dimensional subspace of $\mathbb{C}^{4}$, and the set over which the max-min formula maximises is therefore smaller for $B$, which gives $\mu_k\le\lambda_k$. Every $(4-k)$-dimensional subspace of $W$ is one of $\mathbb{C}^{4}$, and the set over which the min-max formula minimises is smaller for $B$, which gives $\mu_k\ge\lambda_{k+1}$. For $k=1,2,3$ this is the chain.

**Corollary.** The interlacing is strict unless an eigenvector of $B$ is an eigenvector of $A$ supported in the submatrix.

**Proof.** Equality in the variational formula forces the extremal subspace to be spanned by eigenvectors of $A$.

**Corollary.** A Hermitian matrix of order four with a positive semidefinite principal submatrix of order three has at least two nonnegative eigenvalues.

**Proof.** $\mu_3\ge0$ gives $\lambda_3\ge\mu_3\ge0$.

**The count.** The interlacing gives three eigenvalues of the submatrix trapped between four of the matrix, so the spectrum of the compression is a "sub-spectrum" in the strong sense.

**Proof.** The chain of seven inequalities.

## The Cone and the Order

**Definition.** $\operatorname{Herm}_4^{+}=\{A:A^{\ast}=A,\ \lambda_k(A)\ge0\ \text{for all}\ k\}$.

**Theorem.** $\operatorname{Herm}_4^{+}$ is a closed convex cone of real dimension $16$ with nonempty interior $\operatorname{Herm}_4^{++}$, and it is pointed: $A\in\operatorname{Herm}_4^{+}$ and $-A\in\operatorname{Herm}_4^{+}$ force $A=0$.

**Proof.** Convexity: if $A$ and $B$ are positive semidefinite then $\langle v,(tA+(1-t)B)v\rangle=t\langle v,Av\rangle+(1-t)\langle v,Bv\rangle\ge0$. Closedness: the eigenvalues are continuous functions of the entries. Pointedness: a matrix with $\lambda_k\ge0$ and $-\lambda_k\ge0$ has all eigenvalues zero, and being Hermitian it is zero.

**Corollary.** The cone defines a partial order $A\succeq B$ by $A-B\in\operatorname{Herm}_4^{+}$, which is compatible with addition and with multiplication by nonnegative scalars.

**Proof.** The cone is convex and pointed, and it is closed under addition.

**Corollary.** Every Hermitian matrix is the difference of two positive semidefinite ones, $A=A^{+}-A^{-}$ with $A^{\pm}$ the sums of the spectral projectors of the positive and negative eigenvalues.

**Proof.** The spectral resolution grouped by the sign of the eigenvalue.

**The order and the trace.** If $A\succeq B$ then $\operatorname{tr}A\ge\operatorname{tr}B$, and the trace is a strictly positive linear functional on the cone away from zero.

**Proof.** The trace is the sum of the eigenvalues, and a nonzero element of the cone has a positive eigenvalue.

## The Spectral Decomposition and the Peirce Decomposition

**Proposition.** For a Hermitian idempotent $E$ of rank two the spectral projectors are $P_1=E$ and $P_0=\mathrm I_4-E$, and the Peirce spaces are
$$
V_{11}=P_1MP_1,\quad V_{00}=P_0MP_0,\quad V_{10}\oplus V_{01}=P_1MP_0\oplus P_0MP_1.
$$

**Proof.** Substitute $E=P_1$ in the definitions of the Peirce spaces.

**Corollary.** The spectral decomposition of a Hermitian idempotent produces the Peirce decomposition of the algebra: the two spectral projectors cut the four Peirce spaces.

**Proof.** The four spaces are the four combinations of the two projectors, read on the two sides.

**The converse failure.** The spectral decomposition of a general Hermitian matrix does not produce a Peirce decomposition. The projectors cut the algebra into $r^{2}$ blocks $P_iMP_j$, and this is a Peirce decomposition of a single idempotent only when $r=2$.

**Proof.** An idempotent has two eigenvalues, $1$ and $0$; four distinct eigenvalues give four projectors of rank one and sixteen blocks, none of which is a Peirce space of one idempotent.

**Corollary.** The Peirce decomposition is the spectral decomposition of one idempotent read on both sides; the spectral decomposition is the finer instrument, and the Peirce one is the case of two eigenvalues $1$ and $0$.

**Proof.** The two statements above.

## Trace, Determinant and the Elementary Symmetric Functions

**Proposition.** $\operatorname{tr}A=\sum_k\lambda_k$ and $\det A=\prod_k\lambda_k$, and more generally $e_k(A)$ is the $k$-th elementary symmetric function of the eigenvalues.

**Proof.** The characteristic polynomial is $\prod_k(t-\lambda_k)$ and its coefficients are the elementary symmetric functions up to sign; the two lowest are the trace and the determinant.

**Corollary.** $\operatorname{tr}(A^{2})=\sum_k\lambda_k^{2}$, so the Hilbert–Schmidt norm is the Euclidean norm of the spectrum, and $A$ is normal exactly when this identity holds.

**Proof.** The eigenvalues of $A^{2}$ are the squares, and the identity for a general matrix has the extra strictly upper terms.

**Corollary.** The determinant is positive on the interior of the cone, zero on the boundary and of sign $(-1)^{m}$ on a matrix with $m$ negative eigenvalues.

**Proof.** The product of the eigenvalues.

**The order and the determinant.** On the cone the determinant is monotone: $A\succeq B\succeq0$ implies $\det A\ge\det B$, with equality only when $A=B$.

**Proof.** $\det$ is the product of eigenvalues, and the eigenvalues of $A$ dominate those of $B$ in the interlacing sense; the equality case follows from the variational formula.

## Summary

A Hermitian matrix of order four has a real spectrum and an orthonormal eigenbasis, and it is the sum of its spectral projectors weighted by the eigenvalues. Each projector is a polynomial in the matrix, so the spectral decomposition is canonical and commutes with everything that commutes with the matrix.

The eigenvalues are the extreme values of the Rayleigh quotient on subspaces, by the min-max principle, and they interlace the eigenvalues of every principal submatrix of order three. The matrices with nonnegative spectrum form a closed convex pointed cone of real dimension sixteen, which defines the order compatible with addition.

The spectral decomposition of a Hermitian idempotent produces the four Peirce spaces of the algebra, so the Peirce decomposition is the two-eigenvalue case of the spectral one. The trace is the sum of the eigenvalues, the determinant their product, and the elementary symmetric functions the coefficients of the characteristic polynomial.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\lambda_1\ge\dots\ge\lambda_4$ | the real eigenvalues |
| $P_k$ | the spectral projectors |
| $A=\sum_k\lambda_kP_k$ | the spectral resolution |
| $\operatorname{Herm}_4^{+}$ | the cone of nonnegative spectrum |
| $A\succeq B$ | $A-B$ positive semidefinite |
| $e_k$ | the elementary symmetric functions of the spectrum |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the spectral theorem, the min-max principle and interlacing.
- Rajendra Bhatia, *Matrix Analysis* (Springer, 1997), for the variational characterisation and the order on Hermitian matrices.
- [Normal Matrices and the Common Spectral Theorem at $n=4$](normal-matrices-and-the-common-spectral-theorem-at-n-4.html), for the diagonal form that the theorem refines.
- [The Positive Cone and Its Boundary at $n=4$](the-positive-cone-and-its-boundary-at-n-4.html), for the cone and its faces.
- [The Spectral Theorem: the Hermitian Case and the Sphere of Idempotents](the-spectral-theorem-the-hermitian-case-and-the-sphere-of-idempotents.html), for the case at order two.
