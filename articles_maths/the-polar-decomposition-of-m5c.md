# __The Polar Decomposition__

## Introduction

Every matrix $A\in M_5(\mathbb{C})$ has a **polar decomposition**

$$
A=U|A|,\qquad |A|=(A^*A)^{1/2},
$$

where $|A|$ is positive semidefinite and $U$ is a partial isometry; if $A$ is invertible, $U$ is $*$-unitary and $|A|$ is positive definite. The decomposition is the matrix analogue of the polar form $z=re^{i\theta}$ of a complex number: the positive part $|A|$ is the modulus, the $*$-unitary part $U$ is the phase.

The **singular value decomposition** is the diagonalization of the positive part:

$$
A=V\Sigma W^*,\qquad \Sigma=\operatorname{diag}(\sigma_1,\dots,\sigma_5),
\qquad \sigma_1\ge\cdots\ge\sigma_5\ge0,
$$

with $V,W$ $*$-unitary. The numbers $\sigma_k$ are the **singular values**, the eigenvalues of $|A|$. They give the operator norm $\|A\|_{\mathrm{op}}=\sigma_1$, the Frobenius norm $\|A\|_F=\sqrt{\sum_k\sigma_k^2}$, the determinant $|\det A|=\prod_k\sigma_k$, and the condition number $\sigma_1/\sigma_5$ for an invertible $A$.

The polar decomposition is also the **geometry of $GL_5$**: the map

$$
U(5)\times\mathcal{P}\longrightarrow GL_5,\qquad (U,P)\longmapsto UP,
$$

is a diffeomorphism, where $\mathcal{P}$ is the open convex cone of positive definite Hermitian matrices. The quotient $GL_5/U(5)\cong\mathcal{P}$ is a symmetric space of noncompact type; the geodesics and the distance are given by the logarithm and the Frobenius norm. The $*$-unitary group is the compact direction, the positive cone the noncompact direction.

The article proves the polar decomposition, the uniqueness, the SVD, the norm and determinant formulas, and the geometry of $GL_5$. It assumes the Hermitian spectral theorem, the positive semidefinite order, the square root and the functional calculus of *Spectral Theory and the Spectral Projectors*. It uses no topology beyond the homotopy type of $GL_5$.

## The Polar Decomposition

### The Positive Part

**Definition.** For $A\in M_5(\mathbb{C})$, the **positive part** is

$$
|A|=(A^*A)^{1/2},
$$

the positive semidefinite square root of $A^*A$.

**Proposition.** $A^*A$ is positive semidefinite; $|A|$ is positive semidefinite; and

$$
\||A|x\|=\|Ax\|\qquad\text{for all }x\in\mathbb{C}^5 .
$$

In particular $\ker|A|=\ker A$.

**Proof.** $\langle x,A^*Ax\rangle=\|Ax\|^2\ge0$, so $A^*A$ is positive semidefinite; its square root is positive semidefinite by the spectral theorem. Then $\||A|x\|^2=\langle x,|A|^2x\rangle=\langle x,A^*Ax\rangle=\|Ax\|^2$. The kernels agree because the norms agree.

**Corollary.** $|A|$ is the unique positive semidefinite matrix whose square is $A^*A$; it is diagonalizable with nonnegative eigenvalues, the singular values.

**Proof.** The uniqueness of the positive semidefinite square root is the spectral theorem; the eigenvalues of $|A|$ are the square roots of the eigenvalues of $A^*A$, which are nonnegative.

**Corollary.** $|A|$ is invertible iff $A$ is invertible; in that case $|A|^{-1}$ is positive definite.

**Proof.** $\ker|A|=\ker A$; invertibility is the triviality of the kernel; the inverse of a positive definite matrix is positive definite.

### The $*$-Unitary Part

**Theorem (polar decomposition).** Every $A\in M_5(\mathbb{C})$ can be written as

$$
A=U|A|,
$$

where $U$ is a partial isometry with initial space $\overline{\operatorname{ran}}|A|$ and final space $\overline{\operatorname{ran}}A$. If $A$ is invertible, $U$ is $*$-unitary.

**Proof.** Define $U$ on $\operatorname{ran}|A|$ by $U(|A|x)=Ax$. This is well defined: if $|A|x=|A|y$, then $|A|(x-y)=0$, so $A(x-y)=0$ by the kernel identity. It is isometric: $\||A|x\|=\|Ax\|$. Extend $U$ by zero on $\ker|A|$; then $U$ is a partial isometry and $U|A|x=Ax$ for all $x$. If $A$ is invertible, $|A|$ is invertible, $\operatorname{ran}|A|=\mathbb{C}^5$, and $U=A|A|^{-1}$ is $*$-unitary: $U^*U=|A|^{-1}A^*A|A|^{-1}=I$ and $UU^*=A|A|^{-2}A^*=A(A^*A)^{-1}A^*=I$.

**Corollary.** For invertible $A$, the polar decomposition is $A=U|A|$ with $U=A|A|^{-1}$; equivalently $A=|A^*|U$ with $|A^*|=(AA^*)^{1/2}$.

**Proof.** The first formula is the theorem; the second follows by applying the first to $A^*$ and taking adjoints, or by $AA^*=U|A|^2U^*=U A^*AU^*$ and the uniqueness of the square root.

### Uniqueness

**Theorem.** If $A=UP=U'P'$ with $U,U'$ $*$-unitary and $P,P'$ positive definite, then $U=U'$ and $P=P'$. For a general $A$, the positive part is unique, and the partial isometry with initial space $\operatorname{ran}|A|$ is unique; it is zero on $\ker A$. A unitary extension is determined by an isometry from $\ker A$ onto $(\operatorname{ran}A)^\perp$.

**Proof.** $A^*A=P^2=P'^2$; the positive definite square root is unique, so $P=P'$. Then $UP=U'P$ and $P$ is invertible, so $U=U'$. For a general $A$, $A^*A$ determines $|A|$ uniquely; the canonical $U$ is determined on $\operatorname{ran}|A|$ by $U(|A|x)=Ax$ and is zero on $\ker|A|=\ker A$. A unitary extension is determined on $\ker A$ by an isometry onto $(\operatorname{ran}A)^\perp$.

**Corollary.** The polar decomposition gives a bijection between $GL_5$ and $U(5)\times\mathcal{P}$, where $\mathcal{P}$ is the cone of positive definite Hermitian matrices.

**Proof.** The map $(U,P)\mapsto UP$ is surjective by the theorem and injective by uniqueness; the inverse is $A\mapsto(A|A|^{-1},|A|)$.

## The Singular Value Decomposition

### The Singular Values

**Definition.** The **singular values** of $A$ are the eigenvalues $\sigma_1\ge\cdots\ge\sigma_5\ge0$ of $|A|$, counted with multiplicity.

**Proposition.** The singular values are the square roots of the eigenvalues of $A^*A$ (equivalently of $AA^*$); the number of nonzero singular values is the rank of $A$.

**Proof.** $|A|^2=A^*A$; the eigenvalues of $|A|$ are the square roots of those of $A^*A$. The rank is the number of nonzero eigenvalues of $A^*A$, which is the number of nonzero singular values.

**Corollary.** The singular values are invariant under left and right multiplication by $*$-unitary matrices: $\sigma_k(UAV)=\sigma_k(A)$.

**Proof.** $(UAV)^*(UAV)=V^*A^*AV$, which has the same eigenvalues as $A^*A$; the singular values are unchanged.

### The SVD

**Theorem (singular value decomposition).** Every $A\in M_5(\mathbb{C})$ can be written as

$$
A=V\Sigma W^*,
$$

with $V,W$ $*$-unitary and $\Sigma=\operatorname{diag}(\sigma_1,\dots,\sigma_5)$ the diagonal matrix of the singular values.

**Proof.** Diagonalize $|A|$ by a $*$-unitary $W$: $|A|=W\Sigma W^*$ with $\Sigma$ the diagonal of singular values. Then $A=U|A|=UW\Sigma W^*$; put $V=UW$, which is $*$-unitary when $A$ is invertible. In the general case, $U$ is a partial isometry; extend it to a $*$-unitary $V$ on the orthogonal complement of $\operatorname{ran}|A|$; the formula still holds because $\Sigma$ kills the kernel.

**Corollary.** The columns of $V$ are the left singular vectors, the columns of $W$ the right singular vectors, and $Av_k=\sigma_kw_k$? With the convention $A=V\Sigma W^*$, $Aw_k=\sigma_kv_k$ and $A^*v_k=\sigma_kw_k$.

**Proof.** $A=V\Sigma W^*$ gives $AW=V\Sigma$, so $Aw_k=\sigma_kv_k$; taking adjoints gives $A^*v_k=\sigma_kw_k$.

**Corollary.** The rank of $A$ is the number of nonzero singular values; the kernel is spanned by the right singular vectors with $\sigma_k=0$; the range is spanned by the left singular vectors with $\sigma_k>0$.

**Proof.** The SVD is the diagonal form; the kernel and range are read on the zero and nonzero singular values.

### The Norms and the Determinant

**Theorem.** For $A$ with singular values $\sigma_1\ge\cdots\ge\sigma_5$,

$$
\|A\|_{\mathrm{op}}=\sigma_1,\qquad
\|A\|_F=\sqrt{\sigma_1^2+\cdots+\sigma_5^2},\qquad
|\det A|=\sigma_1\cdots\sigma_5 .
$$

**Proof.** The operator norm is the square root of the largest eigenvalue of $A^*A$, which is $\sigma_1$; the Frobenius norm is the square root of the trace of $A^*A$, which is the sum of the squares; the determinant is the product of the eigenvalues of $A$, whose moduli are the singular values (the eigenvalues of $|A|$).

**Corollary.** The condition number of an invertible $A$ is $\kappa(A)=\sigma_1/\sigma_5\ge1$, with equality iff $A$ is a scalar multiple of a $*$-unitary matrix.

**Proof.** The ratio of the largest to the smallest singular value is at least $1$; equality means all singular values are equal, so $|A|$ is scalar and $A$ is a scalar multiple of a $*$-unitary.

**Corollary.** The determinant of $A$ is nonzero iff all singular values are nonzero; the singular set $\det=0$ is the set of matrices with at least one zero singular value.

**Proof.** The product of the singular values is $|\det A|$; it vanishes iff one factor vanishes.

## The Geometry of $GL_5$

### The Diffeomorphism

**Theorem.** The polar map

$$
\Phi:U(5)\times\mathcal{P}\longrightarrow GL_5,\qquad (U,P)\longmapsto UP,
$$

is a diffeomorphism, where $\mathcal{P}=\{P:P^*=P,\ P>0\}$ is the open cone of positive definite Hermitian matrices.

**Proof.** The map is bijective by the polar decomposition and uniqueness. It is smooth because the product and the inverse are smooth; the inverse $A\mapsto(A|A|^{-1},|A|)$ is smooth because $|A|$ is a smooth function of $A$ on the invertible locus (the square root of the positive definite $A^*A$ is smooth). The derivative is invertible, so the map is a diffeomorphism.

**Corollary.** $GL_5$ is diffeomorphic to $U(5)\times\mathbb{R}^{25}$; the positive cone $\mathcal{P}$ is diffeomorphic to the real vector space of Hermitian matrices via the exponential.

**Proof.** $\mathcal{P}$ is open in the $25$-real-dimensional space of Hermitian matrices; the exponential of a Hermitian matrix is positive definite, and the logarithm is its smooth inverse.

### The Symmetric Space

**Theorem.** The quotient $GL_5(\mathbb{C})/U(5)$ is diffeomorphic to $\mathcal{P}$, and it is a symmetric space of noncompact type for the metric

$$
\langle X,Y\rangle=\operatorname{Re}\operatorname{tr}(X^*Y)
$$

on the tangent space. The Cartan decomposition is

$$
\mathfrak{gl}_5=\mathfrak{u}(5)\oplus i\mathfrak{u}(5),
$$

the skew-Hermitian and Hermitian parts.

**Proof.** The group $GL_5$ acts transitively on $\mathcal{P}$ by $g\cdot P=gPg^*$; the stabilizer of $I$ is $U(5)$; the quotient is $\mathcal{P}$. The Cartan involution is $\theta(X)=-X^*$, with fixed space $\mathfrak{u}(5)$ and $-1$ eigenspace $i\mathfrak{u}(5)$; the metric is invariant and the space is symmetric. The noncompact type is the sign of the curvature; the sectional curvature is nonpositive.

**Corollary.** The polar decomposition is the global Cartan decomposition: every $g\in GL_5$ is $g=UP$ with $U\in U(5)$ and $P$ positive definite, the exponential of a Hermitian matrix.

**Proof.** The polar decomposition is the global form of the Lie algebra decomposition $\mathfrak{gl}_5=\mathfrak{u}(5)\oplus i\mathfrak{u}(5)$; the exponential of $i\mathfrak{u}(5)$ is $\mathcal{P}$.

### The Geodesics and the Distance

**Theorem.** The geodesic between $P_0,P_1\in\mathcal{P}$ is

$$
P(t)=P_0^{1/2}\left(P_0^{-1/2}P_1P_0^{-1/2}\right)^tP_0^{1/2},\qquad 0\le t\le1,
$$

and the distance is

$$
d(P_0,P_1)=\left\|\log\left(P_0^{-1/2}P_1P_0^{-1/2}\right)\right\|_F .
$$

**Proof.** The geodesics of the symmetric space $\mathcal{P}$ are the images of the one-parameter subgroups $t\mapsto P_0^{1/2}e^{tS}P_0^{1/2}$ with $S$ Hermitian; the endpoint condition at $t=1$ determines $S=\log(P_0^{-1/2}P_1P_0^{-1/2})$. The distance is the length of the geodesic, which is the Frobenius norm of $S$ because the metric is the trace metric.

**Corollary.** The distance is invariant under $g\mapsto gPg^*$ and under inversion; it is complete, and the exponential map at $I$ is a diffeomorphism.

**Proof.** The metric is invariant under the group action; the exponential of Hermitian matrices is a diffeomorphism onto $\mathcal{P}$; completeness is the Hopf–Rinow theorem for the complete metric.

**Remark.** **The geometry of $GL_5$ is the product of the compact $*$-unitary group and the noncompact positive cone.** The polar decomposition splits the group into a compact direction $U(5)$ and a noncompact direction $\mathcal{P}$; the positive cone is a symmetric space of nonpositive curvature, and the geodesics are the matrix analogues of the straight lines in the logarithm. The determinant is the volume of the image of the unit ball, and the singular values are the lengths of the semi-axes of the ellipsoid $A(S^5)$.

## The Degenerate Case

### Partial Isometries

**Definition.** A **partial isometry** is a matrix $U$ with $U^*U$ a projection; equivalently, $U$ is isometric on the orthogonal complement of its kernel.

**Proposition.** In the polar decomposition $A=U|A|$, the partial isometry $U$ satisfies $U^*U$ is the projection onto $\overline{\operatorname{ran}}|A|$ and $UU^*$ is the projection onto $\overline{\operatorname{ran}}A$.

**Proof.** $U$ is isometric on $\operatorname{ran}|A|$ and zero on its orthogonal complement; $U^*U$ is the projection onto $\operatorname{ran}|A|$; $UU^*$ is the projection onto the range of $U$, which is $\operatorname{ran}A$.

**Corollary.** $U$ is $*$-unitary iff $A$ is invertible; it is an isometry iff $A$ is injective; it is a coisometry iff $A$ is surjective.

**Proof.** $U$ is $*$-unitary iff both projections are the identity, i.e., $\ker A=0$ and $\operatorname{ran}A=\mathbb{C}^5$.

### The Non-Uniqueness

**Proposition.** For a singular $A$, the positive part $|A|$ is unique, and the canonical partial isometry with initial space $\operatorname{ran}|A|$ is unique. A unitary extension is not unique: on $\ker A$ it can be any isometry onto $(\operatorname{ran}A)^\perp$.

**Proof.** The canonical $U$ is determined on $\operatorname{ran}|A|$ and is zero on $\ker|A|=\ker A$. For a unitary extension, the condition $A=U|A|$ imposes nothing on $\ker A$ beyond $U(\ker A)\subseteq(\operatorname{ran}A)^\perp$ and isometry; any such choice gives $A=U|A|$.

**Corollary.** The canonical polar decomposition is unique for every $A$; for singular $A$, the ambiguity of a unitary extension is the choice of the isometry on the kernel. The positive part and the singular values are always unique.

**Proof.** The positive part is determined by $A^*A$; the singular values are its eigenvalues; the ambiguity is exactly the kernel isometry.

**Remark.** **The polar decomposition is the matrix analogue of the polar form, with the partial isometry as the phase.** For an invertible matrix the phase is $*$-unitary; for a singular matrix the phase is only a partial isometry, and the kernel is the ambiguity. The singular values are the moduli; the positive part is the modulus matrix; the SVD diagonalizes the modulus.

## Summary

Every $A\in M_5(\mathbb{C})$ has the polar decomposition

$$
A=U|A|,\qquad |A|=(A^*A)^{1/2},
$$

with $|A|$ positive semidefinite and $U$ a partial isometry; for invertible $A$, $U$ is $*$-unitary and the decomposition is unique. The singular value decomposition is

$$
A=V\Sigma W^*,\qquad \Sigma=\operatorname{diag}(\sigma_1,\dots,\sigma_5),
$$

with $\sigma_1\ge\cdots\ge\sigma_5\ge0$ the singular values.

$$
\boxed{\ A=U|A|=V\Sigma W^*;\quad \|A\|_{\mathrm{op}}=\sigma_1;\quad |\det A|=\prod_k\sigma_k;\quad GL_5\cong U(5)\times\mathcal{P}.\ }
$$

The polar map $U(5)\times\mathcal{P}\to GL_5$ is a diffeomorphism; the quotient $GL_5/U(5)\cong\mathcal{P}$ is a symmetric space of noncompact type, with geodesics $P_0^{1/2}(P_0^{-1/2}P_1P_0^{-1/2})^tP_0^{1/2}$ and distance $\|\log(P_0^{-1/2}P_1P_0^{-1/2})\|_F$. For singular $A$, the positive part and the singular values are unique, and the partial isometry is unique only on the range.

| Object | Formula |
|---|---|
| Positive part | $|A|=(A^*A)^{1/2}$ |
| Polar decomposition | $A=U|A|$ |
| $*$-Unitary part | $U=A|A|^{-1}$ for invertible $A$ |
| Singular values | Eigenvalues of $|A|$ |
| SVD | $A=V\Sigma W^*$ |
| Operator norm | $\sigma_1$ |
| Frobenius norm | $\sqrt{\sum_k\sigma_k^2}$ |
| Determinant modulus | $\prod_k\sigma_k$ |
| Condition number | $\sigma_1/\sigma_5$ |
| Geometry | $GL_5\cong U(5)\times\mathcal{P}$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $|A|=(A^*A)^{1/2}$ | The positive part |
| $U$ | The partial isometry ($*$-unitary if $A$ is invertible) |
| $\sigma_k$ | The singular values |
| $V,\Sigma,W$ | The SVD factors |
| $\mathcal{P}$ | The positive definite cone |
| $\kappa(A)$ | The condition number |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, second edition, 2013), for the polar decomposition, the singular value decomposition and the condition number.
- Rajendra Bhatia, *Matrix Analysis* (Springer, 1997), for the positive definite cone, the trace metric and the matrix geometric means.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (American Mathematical Society, 2001), for the symmetric space $GL_n(\mathbb{C})/U(n)$, the Cartan decomposition and the geodesics.
- [Spectral Theory and the Spectral Projectors](spectral-theory-and-the-spectral-projectors-of-m5c.html), for the Hermitian spectral theorem, the square root and the functional calculus.
- [The Involution and the Hermitian Structure](the-involution-and-the-hermitian-structure-of-m5c.html), for the Hermitian form and the $*$-unitary group.
- [The Exponential and the Lie Group](the-exponential-and-the-lie-group-of-m5c.html), for the exponential map and the Lie group.
- [The Exponential-Polar Decomposition](the-exponential-polar-decomposition-of-m5c.html), for the combination of the exponential and the polar decomposition.
