# __The Polar Decomposition__

## Introduction

**Every $A\in M_4(\mathbb{C})$ factors as $A=UP$ with $U\in U(4)$ unitary and $P$ positive semidefinite; the factor $P$ is unique, and $U$ is unique when $A$ is invertible.** The decomposition is the matrix form of the Cartan decomposition $GL_4=U(4)\cdot\exp(\operatorname{Herm}_4)$, and the positive factor is $P=\sqrt{A^*A}$. The singular value decomposition refines it, and the singular case has a freedom on the kernel.

The article proves the polar decomposition, identifies the singular value decomposition, describes the singular case and the manifold $GL_4/U(4)$, states the exponential form and the Cartan decomposition, and identifies the unitary factor as the closest unitary to $A$.

The positive definite form is *The Involution and the Hermitian Structure*; the singular values and the norms are *The Forms, the Norms and the Singular Set*; the exponential form is *The Exponential Polar Decomposition*; the mass-block version is *The Mass Block and the Chiral Polar Decomposition*.

## The Polar Decomposition

**Theorem (polar decomposition).** Every $A\in M_4(\mathbb{C})$ can be written as

$$
A=UP,
$$

with $U\in U(4)$ and $P$ positive semidefinite. The factor $P$ is unique:

$$
P=(A^*A)^{1/2}=\lvert A\rvert .
$$

If $A$ is invertible, $U$ is unique and

$$
U=A(A^*A)^{-1/2}.
$$

If $A$ is singular, $U$ is unique on the range of $P$ and arbitrary on its kernel.

**Proof.** The matrix $A^*A$ is positive semidefinite, so it has a unique positive semidefinite square root $P$. On the range of $P$, define $U(Pv)=Av$. This is well defined: if $Pv=0$, then $A^*Av=P^2v=0$, so $Av=0$. It is isometric:

$$
\lVert Av\rVert^2=\langle v,A^*Av\rangle=\langle v,P^2v\rangle=\lVert Pv\rVert^2.
$$

Extend $U$ isometrically from the range of $P$ to its orthogonal complement, the kernel of $P$, with values in the kernel of $A^*$; the dimensions agree because $\operatorname{rank}P=\operatorname{rank}A$. Then $U$ is unitary and $A=UP$. If $A$ is invertible, $P$ is invertible and $U=AP^{-1}=A(A^*A)^{-1/2}$ is forced.

**The two factors.** The factor $P$ is the **positive factor** or **modulus**; the factor $U$ is the **unitary factor** or **phase**. The decomposition is also written

$$
A=U\lvert A\rvert,\qquad
\lvert A\rvert=\sqrt{A^*A}.
$$

**The polar of the adjoint.** Applying the theorem to $A^*$,

$$
A^*=VP,
$$

with the same $P$ and $V=U^*$ when $A$ is invertible. The two decompositions are related by

$$
A=UP,\qquad A^*=PU^*.
$$

**The unitary invariance.** If $A=UP$ and $Q,R\in U(4)$, then

$$
QAR=(QU R)(R^*PR)
$$

is the polar decomposition of $QAR$: the unitary factor is $QUR$ and the positive factor is $R^*PR$. The singular values are unchanged.

## The Singular Value Decomposition

**Theorem (SVD).** Every $A\in M_4(\mathbb{C})$ has a decomposition

$$
A=U\Sigma V^*,
$$

with $U,V\in U(4)$ and

$$
\Sigma=\operatorname{diag}(\sigma_1,\sigma_2,\sigma_3,\sigma_4),\qquad
\sigma_1\ge\sigma_2\ge\sigma_3\ge\sigma_4\ge0.
$$

The numbers $\sigma_k$ are the singular values, the square roots of the eigenvalues of $A^*A$.

**The relation to the polar decomposition.** The SVD gives the polar decomposition by

$$
A=U\Sigma V^*=(UV^*)(V\Sigma V^*),
$$

so the unitary factor is $W=UV^*$ and the positive factor is $P=V\Sigma V^*$. Conversely, diagonalising $P$ by $V$ and setting $U=WV$ recovers the SVD.

**The proof.** The spectral theorem for the positive semidefinite matrix $A^*A$ gives an orthonormal eigenbasis $v_1,\dots,v_4$ with eigenvalues $\sigma_1^2,\dots,\sigma_4^2$. For $\sigma_k>0$, set $u_k=Av_k/\sigma_k$; the $u_k$ are orthonormal. Extend them to a unitary $U$; then $A=U\Sigma V^*$.

**The non-uniqueness.** The singular values are unique. The unitaries $U,V$ are not unique when some singular values coincide, and they are not unique on the kernel when $A$ is singular. The polar factor $W=UV^*$ is unique on the range of $P$ and arbitrary on the kernel; the positive factor $P$ is always unique.

**Example.** For

$$
A=\begin{pmatrix}3&0&0&0\\0&2&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix},
$$

the singular values are $3,2,0,0$, the positive factor is $P=A$, and the unitary factor is $U=I$. For

$$
A=\begin{pmatrix}0&3&0&0\\2&0&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix},
$$

the singular values are $3,2,0,0$, and

$$
A=
\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix}
\begin{pmatrix}3&0&0&0\\0&2&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix}
\begin{pmatrix}0&1&0&0\\1&0&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix}.
$$

## The Singular Case

**The freedom on the kernel.** If $A$ has rank $k<4$, then $P$ has rank $k$ and kernel of dimension $4-k$. The unitary factor $U$ is determined on the range of $P$ and arbitrary on the kernel of $P$. The freedom is a unitary $U(4-k)$ acting on the kernel, with values in the kernel of $A^*$.

**The partial isometry.** The factor $U$ is a **partial isometry**:

$$
U^*U=P_{\operatorname{ran}P},\qquad
UU^*=P_{\operatorname{ran}A},
$$

the orthogonal projections onto the range of $P$ and the range of $A$. It is unitary exactly when $A$ is invertible.

**Example.** For

$$
A=\begin{pmatrix}3&0&0&0\\0&0&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix},
$$

the positive factor is $P=A$, and the unitary factor can be any unitary whose first column is $e_1$; the freedom is $U(3)$ on the kernel. The polar decomposition is not unique, but the positive factor is.

**The polar of a projection.** A projection $P$ (self-adjoint idempotent) is positive semidefinite, so its polar decomposition is $P=P\cdot I$; the unitary factor is $I$ on the range and arbitrary on the kernel. A partial isometry $U$ has polar decomposition $U=U P$ with $P=U^*U$ the projection onto its initial space; the positive factor is that projection.

## The Manifold $GL_4/U(4)$

**The diffeomorphism.** The polar decomposition gives a diffeomorphism

$$
GL_4(\mathbb{C})\longrightarrow U(4)\times P_+,\qquad
A\longmapsto(U,P),
$$

where $P_+$ is the open cone of positive definite Hermitian matrices. The inverse is $(U,P)\mapsto UP$. Hence

$$
GL_4(\mathbb{C})/U(4)\cong P_+,
$$

the **symmetric space** of positive definite Hermitian matrices.

**The dimension.** The real dimensions are

$$
\dim_\mathbb{R}GL_4=32,\qquad
\dim_\mathbb{R}U(4)=16,\qquad
\dim_\mathbb{R}P_+=16,
$$

and $32=16+16$.

**The contractibility.** The exponential map

$$
\operatorname{Herm}_4\longrightarrow P_+,\qquad
H\longmapsto e^H,
$$

is a diffeomorphism, with inverse the Hermitian logarithm. The space $\operatorname{Herm}_4$ is a real vector space of dimension $16$, so $P_+$ is contractible and $GL_4/U(4)$ is contractible. The unitary group $U(4)$ is a maximal compact subgroup of $GL_4(\mathbb{C})$.

**The Cartan decomposition.** The polar decomposition is the global form of the Cartan decomposition of the Lie algebra

$$
\mathfrak{gl}_4(\mathbb{C})=\mathfrak{u}(4)\oplus\operatorname{Herm}_4,
$$

with the Cartan involution

$$
\theta(X)=-X^*.
$$

The $+1$ eigenspace is $\mathfrak{u}(4)$, the $-1$ eigenspace is $\operatorname{Herm}_4$, and the brackets satisfy

$$
[\mathfrak{u},\mathfrak{u}]\subseteq\mathfrak{u},\qquad
[\mathfrak{u},\operatorname{Herm}]\subseteq\operatorname{Herm},\qquad
[\operatorname{Herm},\operatorname{Herm}]\subseteq\mathfrak{u}.
$$

The group decomposition is $GL_4=U(4)\exp(\operatorname{Herm}_4)$.

**The symmetric space.** The quotient $GL_4/U(4)\cong P_+$ is a symmetric space of noncompact type; the exponential map is a diffeomorphism, the geodesics are the curves $t\mapsto e^{H_0+tH}$, and the curvature is negative. The positive definite cone is the space of metrics on $\mathbb{C}^4$; the unitary group is the group of isometries of the standard metric.

## The Closest Unitary

**Theorem.** The unitary factor $U$ of $A=UP$ is the closest unitary to $A$ in the Frobenius norm:

$$
\lVert A-U\rVert_F=\min_{Q\in U(4)}\lVert A-Q\rVert_F .
$$

The minimum value is

$$
\lVert A-U\rVert_F^2=\lVert A\rVert_F^2+4-2\lVert A\rVert_*,
$$

where $\lVert A\rVert_*=\sum_k\sigma_k$ is the nuclear norm.

**Proof.** For $Q\in U(4)$,

$$
\lVert A-Q\rVert_F^2=\lVert A\rVert_F^2+4-2\operatorname{Re}\operatorname{tr}(Q^*A).
$$

The maximum of $\operatorname{Re}\operatorname{tr}(Q^*A)$ over unitary $Q$ is the nuclear norm $\lVert A\rVert_*$, attained at $Q=UV^*$ where $A=U\Sigma V^*$. This is the duality of the operator and nuclear norms. The polar factor is $W=UV^*$.

**The geometric meaning.** The polar decomposition is the orthogonal projection of $A$ onto the unitary group in the Frobenius metric: the unitary factor is the point of $U(4)$ closest to $A$. The positive factor is the radial part of $A$ relative to $U(4)$; its norm measures the distance from $A$ to the group.

## The Exponential Form

**The unitary factor.** Every unitary $U\in U(4)$ has a Hermitian logarithm:

$$
U=e^{iK},\qquad K=K^*,
$$

defined modulo the eigenvalues of $K$ shifted by $2\pi$. The principal logarithm chooses the eigenvalues of $K$ in $(-\pi,\pi]$.

**The positive factor.** Every positive definite $P$ has a unique Hermitian logarithm:

$$
P=e^H,\qquad H=H^*,
$$

with $H=\log P$.

**The exponential form of the polar decomposition.** For invertible $A$,

$$
A=UP=e^{iK}e^H,
$$

with $K,H$ Hermitian. The factor $e^{iK}$ is unitary and $e^H$ is positive definite. The decomposition is the polar decomposition, written in exponential form.

**The other order.** The **exponential polar decomposition** of *The Exponential Polar Decomposition* writes an invertible $A$ as

$$
A=e^{H'}e^{iK'},
$$

with $H',K'$ Hermitian. The two orderings are different; the factors are related by the polar decomposition and the conjugation. The existence of both is the statement that the exponential map from the Hermitian matrices is surjective onto the positive definite cone and onto the unitary group.

**The logarithm.** For invertible $A$, the principal logarithm is

$$
\log A=\log P+iK,
$$

with $P=|A|$ and $U=e^{iK}$; it is a holomorphic function of $A$ on the domain avoiding the negative real axis of the spectrum. The exponential and the logarithm are *The Exponential and the Lie Group*.

## The Biquaternion Case

**At $n=2$ the polar decomposition is the same theorem.** For $A\in M_2(\mathbb{C})$,

$$
A=UP,\qquad U\in U(2),\quad P\ge0,
$$

and

$$
GL_2(\mathbb{C})/U(2)\cong P_+,
$$

the positive definite $2\times2$ Hermitian cone, of real dimension $4$. The exponential map $\operatorname{Herm}_2\to P_+$ is a diffeomorphism. The biquaternion polar decomposition of the regular model is the same decomposition applied to the $4\times4$ regular matrices; the full algebra's polar decomposition is the $U(4)$ version.

**The comparison.** The positive definite cone $P_+$ is the same object in both cases; the unitary group is $U(2)$ for the biquaternion algebra and $U(4)$ for the full matrix algebra. The full algebra's polar decomposition has a larger unitary factor and a larger positive factor, and its singular values are four rather than two.

## Summary

Every $A\in M_4(\mathbb{C})$ has a polar decomposition $A=UP$ with $U\in U(4)$ and $P$ positive semidefinite; $P=(A^*A)^{1/2}$ is unique, and $U$ is unique when $A$ is invertible. The singular value decomposition $A=U\Sigma V^*$ refines it, with $P=V\Sigma V^*$ and $W=UV^*$. When $A$ is singular, $U$ is a partial isometry, unique on the range of $P$ and arbitrary on the kernel, with freedom $U(4-k)$ for rank $k$. The polar decomposition is the diffeomorphism $GL_4\cong U(4)\times P_+$, hence $GL_4/U(4)\cong P_+$, the contractible symmetric space of positive definite Hermitian matrices; it is the global Cartan decomposition of $\mathfrak{gl}_4=\mathfrak{u}(4)\oplus\operatorname{Herm}_4$ with Cartan involution $\theta(X)=-X^*$. The unitary factor is the closest unitary to $A$ in the Frobenius norm, with distance squared $\lVert A\rVert_F^2+4-2\lVert A\rVert_*$. In exponential form $A=e^{iK}e^H$ with $K,H$ Hermitian; the other ordering $e^{H'}e^{iK'}$ is the exponential polar decomposition.

$$
\boxed{\ A=UP,\quad P=(A^*A)^{1/2},\quad U\in U(4),\quad P\ge0,\quad GL_4/U(4)\cong P_+,\quad \dim_\mathbb{R}P_+=16. }
$$

| Object | Dimension or property |
|---|---|
| $GL_4(\mathbb{C})$ | $32$ real |
| $U(4)$ | $16$ real, compact |
| $P_+$ | $16$ real, contractible |
| $GL_4/U(4)$ | $16$ real |
| Positive factor $P$ | unique |
| Unitary factor $U$ | unique if $A$ invertible |
| Singular values | four, non-negative |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A=UP$ | the polar decomposition |
| $P=\lvert A\rvert=\sqrt{A^*A}$ | the positive factor |
| $U$ | the unitary factor |
| $A=U\Sigma V^*$ | the singular value decomposition |
| $P_+$ | the positive definite Hermitian cone |
| $\theta(X)=-X^*$ | the Cartan involution |
| $\lVert A\rVert_*$ | the nuclear norm |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the polar decomposition, the singular value decomposition and the closest unitary problem.
- Rajendra Bhatia, *Matrix Analysis* (Springer, 1997), for the positive definite cone, the operator and nuclear norms, and the geometry of matrices.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (AMS, 2001), for the Cartan decomposition and the symmetric space $GL_4/U(4)$.
- [The Involution and the Hermitian Structure](the-involution-and-the-hermitian-structure-of-m4c.html), for the positive definite form and the unitary group.
- [The Forms, the Norms and the Singular Set](the-forms-the-norms-and-the-singular-set-of-m4c.html), for the singular values and the norms.
- [The Exponential Polar Decomposition](the-exponential-polar-decomposition-of-m4c.html), for the other ordering $e^He^{iK}$.
- [The Mass Block and the Chiral Polar Decomposition](the-mass-block-and-the-chiral-polar-decomposition-of-m4c.html), for the chiral version.
