# __$M_2(\mathbb{C})$ Representation : Worked Examples__

## Introduction

This article computes eight matrices, one after another, through the same checklist: the biquaternion coordinates, the trace and the determinant, the characteristic and minimal polynomials, the spectrum, the rank, the diagonalising matrix or the Jordan chain, the commutant, the spectral projectors, the polar factors and the normality flags. The eight are chosen so that each exhibits one structure: a scalar, a Jordan block, a matrix with distinct eigenvalues, a singular matrix, a rank-one matrix, a $*$-unitary matrix, a Hermitian matrix and a normal matrix that is neither Hermitian nor $*$-unitary.

The article is the matrix counterpart of *Worked Examples of Eigenbasis of a Biquaternion* and *Worked Examples of Exponential Polar Decomposition of Biquaternions*: the same kind of computation, read in the model $\mathsf{M}_2$ rather than in the algebra.

**Conventions.** The algebra and the model are those of *$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant*. An element is $\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$, its matrix is

$$
X=\mathsf{M}_2(\tilde Q)=
\begin{pmatrix}
Q_t-iQ_z&-iQ_x-Q_y\\
-iQ_x+Q_y&Q_t+iQ_z
\end{pmatrix},
$$

and the inverse map is

$$
Q_t=\tfrac{a+d}{2},\qquad
Q_x=\tfrac{i(b+c)}{2},\qquad
Q_y=\tfrac{c-b}{2},\qquad
Q_z=\tfrac{i(a-d)}{2},
$$

for $X=\begin{pmatrix}a&b\\c&d\end{pmatrix}$. The trace is $\operatorname{Tr}X=2Q_t$ and the determinant is $\det X=Q_t^2+Q_x^2+Q_y^2+Q_z^2=\langle\tilde Q\rangle_{\natural}$. The variable of the characteristic polynomial is written $t$, and the two eigenvalues are $\lambda_\pm$.

**Boundaries.** The construction of the model is *$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant*; the eigenbasis is *$M_2(\mathbb{C})$ Model : The Eigenbasis and the Diagonalising Matrix*; the spectral projectors and the nilpotents are *$M_2(\mathbb{C})$ Model : The Spectral Projectors*; the polar decomposition is *$M_2(\mathbb{C})$ Representation : The Polar Decomposition of a Matrix*; the rank-one matrices are *$M_2(\mathbb{C})$ Representation : Rank-One Matrices and the Determinantal Variety*; the group cases are *$M_2(\mathbb{C})$ Representation : $GL_2(\mathbb{C})$, $SL_2(\mathbb{C})$ and the Determinant*.

## The Method

**The invariants.** For a $2\times2$ matrix $X$ put $\tau=\operatorname{Tr}X$ and $\delta=\det X$. The characteristic polynomial is

$$
p_X(t)=t^2-\tau t+\delta=(t-\lambda_+)(t-\lambda_-),
\qquad
\lambda_\pm=\frac{\tau\pm\sqrt{\tau^2-4\delta}}{2}.
$$

The discriminant is $\tau^2-4\delta=(\lambda_+-\lambda_-)^2$. The eigenvalues are distinct exactly when it is nonzero.

**The minimal polynomial.** The three spectral types are read from $p_X$ and from the size of the eigenspace:

| Type | $m_X(t)$ | Diagonalisable |
|---|---|---|
| scalar, $X=\lambda\mathrm I_2$ | $t-\lambda$ | yes |
| non-scalar, distinct eigenvalues | $(t-\lambda_+)(t-\lambda_-)$ | yes |
| non-scalar, repeated eigenvalue | $(t-\lambda)^2$ | no |

A non-scalar matrix with a repeated eigenvalue is a Jordan block in some basis, $X=C(\lambda\mathrm I_2+N)C^{-1}$ with $N\neq0$ and $N^2=0$.

**The rank.** The rank is $2$ when $\delta\neq0$, $1$ when $\delta=0$ and $X\neq0$, and $0$ only for $X=0$. In $2\times2$ every nonzero singular matrix has rank one, so the singular case and the rank-one case necessarily overlap; the singular example below is diagonal and reads the determinant, the kernel and the pseudo-inverse, while the rank-one example is non-diagonal and reads the outer-product factorisation and the non-normal projectors.

**The spectral projectors.** When the eigenvalues are distinct,

$$
\Pi_+=\frac{X-\lambda_-\mathrm I_2}{\lambda_+-\lambda_-},
\qquad
\Pi_-=\mathrm I_2-\Pi_+,
$$

and $X=\lambda_+\Pi_++\lambda_-\Pi_-$. The two matrices are idempotent and satisfy $\Pi_+\Pi_-=0$. They are Hermitian exactly when $X$ is normal; for a non-normal matrix they are idempotent but not orthogonal projectors, and the two eigenspaces are not orthogonal.

**The commutant.** For a non-scalar $X$ the commutant is $\mathbb{C}[X]=\operatorname{span}\{\mathrm I_2,X\}$, of complex dimension two; for a scalar it is the whole algebra $M_2(\mathbb{C})$. The double commutant returns $\mathbb{C}[X]$ in both cases.

**The polar factors.** The positive factor is $P=(XX^{\dagger})^{1/2}$ and the $*$-unitary or partial-isometry factor is $V$ with $X=PV$. When $X$ is invertible, $V=P^{-1}X$ is $*$-unitary. When $X$ is singular, $V=P^{+}X$ is a partial isometry, with $P^{+}$ the Moore–Penrose inverse.

**The flags.** A matrix is Hermitian when $X=X^{\dagger}$, $*$-unitary when $X^{\dagger}X=\mathrm I_2$, and normal when $XX^{\dagger}=X^{\dagger}X$. Hermitian and $*$-unitary matrices are normal; the converse fails in both directions, and the last example exhibits a normal matrix that is neither.

## The Eight Matrices

The eight matrices, their coordinates and their basic invariants are collected here; the sections that follow compute each one.

| Case | $X$ | $(Q_t,Q_x,Q_y,Q_z)$ | $\operatorname{Tr}X$ | $\det X$ | Spectrum |
|---|---|---|---|---|---|
| Scalar | $2\mathrm I_2$ | $(2,0,0,0)$ | $4$ | $4$ | $2,2$ |
| Jordan | $\begin{pmatrix}1&1\\0&1\end{pmatrix}$ | $(1,\tfrac{i}{2},-\tfrac12,0)$ | $2$ | $1$ | $1,1$ |
| Distinct | $\begin{pmatrix}1&2\\3&4\end{pmatrix}$ | $(\tfrac52,\tfrac{5i}{2},\tfrac12,-\tfrac{3i}{2})$ | $5$ | $-2$ | $\tfrac{5\pm\sqrt{33}}{2}$ |
| Singular | $\begin{pmatrix}2&0\\0&0\end{pmatrix}$ | $(1,0,0,i)$ | $2$ | $0$ | $2,0$ |
| Rank one | $\begin{pmatrix}1&2\\3&6\end{pmatrix}$ | $(\tfrac72,\tfrac{5i}{2},\tfrac12,-\tfrac{5i}{2})$ | $7$ | $0$ | $7,0$ |
| $*$-Unitary | $\tfrac{1}{\sqrt2}\begin{pmatrix}1&i\\i&1\end{pmatrix}$ | $(\tfrac{1}{\sqrt2},-\tfrac{1}{\sqrt2},0,0)$ | $\sqrt2$ | $1$ | $e^{\pm i\pi/4}$ |
| Hermitian | $\begin{pmatrix}2&1-i\\1+i&-1\end{pmatrix}$ | $(\tfrac12,i,i,\tfrac{3i}{2})$ | $1$ | $-4$ | $\tfrac{1\pm\sqrt{17}}{2}$ |
| Normal | $\begin{pmatrix}1&1\\-1&1\end{pmatrix}$ | $(1,0,-1,0)$ | $2$ | $2$ | $1\pm i$ |

The table is read with the inverse map of the introduction; the coordinates are the four complex numbers $Q_t,Q_x,Q_y,Q_z$, not the four entries.

## The Scalar Matrix

**The matrix.** $X=2\mathrm I_2$, with $\tilde Q=2e_t$. It is central: it commutes with every matrix.

**The invariants.** $\operatorname{Tr}X=4$, $\det X=4$, $p_X(t)=(t-2)^2$ and $m_X(t)=t-2$. The spectrum is $\{2\}$, the rank is $2$, and the eigenspace is the whole of $\mathbb{C}^2$.

**The commutant.** $C(X)=M_2(\mathbb{C})$, of complex dimension four, and $C(C(X))=\mathbb{C}\mathrm I_2=\mathbb{C}[X]$. The scalar is the only matrix whose commutant is the whole algebra.

**The flags.** The matrix is normal and Hermitian, because $2$ is real. It is not $*$-unitary, because $|2|\neq1$; the scalar $\tfrac12X=\mathrm I_2$ is $*$-unitary.

**The polar factors.** $P=2\mathrm I_2$ and $V=\mathrm I_2$, so $X=PV$ with $P$ positive and $V$ $*$-unitary.

**The reading.** The scalar is the degenerate spectral case: one eigenvalue, one spectral projector $\mathrm I_2$, and no eigenbasis to choose. In the algebra it is the central line $\mathbb{C}e_t$.

## The Jordan Block

**The matrix.** $X=J=\begin{pmatrix}1&1\\0&1\end{pmatrix}$, with $\tilde Q=e_t+\tfrac{i}{2}\vec e_x-\tfrac12\vec e_y$. The vector part is $\vec Q=\tfrac{i}{2}(\vec e_x+i\vec e_y)$, a null vector; the element is spectrally degenerate with $B=0$ and $Q_t=1$.

**The invariants.** $\operatorname{Tr}X=2$, $\det X=1$, $p_X(t)=(t-1)^2$ and $m_X(t)=(t-1)^2$. The spectrum is $\{1\}$, the rank is $2$, and the eigenspace is $\mathbb{C}(1,0)$, of dimension one. The matrix is invertible and not diagonalisable.

**The Jordan chain.** With $N=J-\mathrm I_2=\begin{pmatrix}0&1\\0&0\end{pmatrix}$, $N^2=0$ and $J=\mathrm I_2+N$. The first standard vector is the eigenvector, and the second is a generalized eigenvector: $N(0,1)^{\mathsf T}=(1,0)^{\mathsf T}$.

**The commutant.** $C(J)=\{a\mathrm I_2+bN\}=\left\{\begin{pmatrix}a&b\\0&a\end{pmatrix}\right\}$, of complex dimension two, the dual numbers $\mathbb{C}[\varepsilon]/(\varepsilon^2)$ with $\varepsilon=N$. Equivalently, $C(J)=\{c\mathrm I_2+dJ\}$, with $c=a-b$ and $d=b$. The double commutant is the same algebra.

**The flags.** The matrix is not normal:

$$
JJ^{\dagger}=\begin{pmatrix}2&1\\1&1\end{pmatrix},
\qquad
J^{\dagger}J=\begin{pmatrix}1&1\\1&2\end{pmatrix}.
$$

It is neither Hermitian nor $*$-unitary.

**The polar factors.** $JJ^{\dagger}=\begin{pmatrix}2&1\\1&1\end{pmatrix}$ has determinant $1$ and trace $3$, so

$$
P=(JJ^{\dagger})^{1/2}=\frac{1}{\sqrt5}\begin{pmatrix}3&1\\1&2\end{pmatrix},
\qquad
V=P^{-1}J=\frac{1}{\sqrt5}\begin{pmatrix}2&1\\-1&2\end{pmatrix}.
$$

The factor $P$ is positive definite and $V$ is $*$-unitary; the product is $J$.

**The reading.** The Jordan block is the matrix form of a spectrally degenerate, N-regular element: $B=0$, $Q_t=1$, norm $1$. The missing eigenvector is the missing spectral idempotent; the commutant keeps the nilpotent direction. The exponential is $\exp J=e(\mathrm I_2+N)=eJ$.

## The Matrix with Distinct Eigenvalues

**The matrix.** $X=D=\begin{pmatrix}1&2\\3&4\end{pmatrix}$, with $\tilde Q=\tfrac52e_t+\tfrac{5i}{2}\vec e_x+\tfrac12\vec e_y-\tfrac{3i}{2}\vec e_z$. The vector part has square $B^2=-\tfrac{33}{4}$, so the element is spectrally regular.

**The invariants.** $\operatorname{Tr}X=5$, $\det X=-2$, and

$$
p_X(t)=t^2-5t-2=(t-\lambda_+)(t-\lambda_-),
\qquad
\lambda_\pm=\frac{5\pm\sqrt{33}}{2}.
$$

The eigenvalues are distinct, so $m_X=p_X$ and the matrix is diagonalisable. The rank is $2$.

**The eigenbasis.** An eigenvector for $\lambda$ is $v(\lambda)=(2,\lambda-1)^{\mathsf T}$, because the first row gives $(1-\lambda)x+2y=0$. Hence

$$
C=\begin{pmatrix}2&2\\\lambda_+-1&\lambda_--1\end{pmatrix},
\qquad
\det C=2(\lambda_--\lambda_+)=-2\sqrt{33},
$$

and $C^{-1}DC=\operatorname{diag}(\lambda_+,\lambda_-)$.

**The spectral projectors.** The Lagrange formula gives

$$
\Pi_+=\frac{D-\lambda_-\mathrm I_2}{\lambda_+-\lambda_-}
=\frac{1}{\sqrt{33}}
\begin{pmatrix}
\tfrac{\sqrt{33}-3}{2}&2\\[2pt]
3&\tfrac{\sqrt{33}+3}{2}
\end{pmatrix},
\qquad
\Pi_-=\mathrm I_2-\Pi_+.
$$

Both are idempotent and $\Pi_+\Pi_-=0$. They are not Hermitian: the $(1,2)$ entry is $2/\sqrt{33}$ and the $(2,1)$ entry is $3/\sqrt{33}$, which are different real numbers. The eigenvectors are not orthogonal.

**The commutant.** $C(D)=\mathbb{C}[D]=\operatorname{span}\{\mathrm I_2,D\}$, of complex dimension two; the double commutant is the same plane.

**The flags.** The matrix is diagonalisable but not normal, not Hermitian and not $*$-unitary. It is the standard example that diagonalisability does not imply normality.

**The reading.** The element is spectrally regular with real eigenvalues, because $B$ is imaginary. The two spectral projectors are idempotent but not Hermitian; the eigenbasis is a pair of non-orthogonal lines. In the algebra, the spectrum is the two roots of the characteristic polynomial, and the coordinates of $D$ in its eigenbasis are the diagonal entries.

## The Singular Matrix

**The matrix.** $X=S=\begin{pmatrix}2&0\\0&0\end{pmatrix}$, with $\tilde Q=e_t+i\vec e_z$. The element has norm $Q_t^2+B^2=1-1=0$, so it is a zero divisor.

**The invariants.** $\operatorname{Tr}X=2$, $\det X=0$, $p_X(t)=t(t-2)$ and $m_X(t)=t(t-2)$. The spectrum is $\{2,0\}$, the rank is $1$, and the matrix is diagonalisable.

**The kernel and the image.** The kernel is $\mathbb{C}(0,1)^{\mathsf T}$ and the image is $\mathbb{C}(1,0)^{\mathsf T}$. The two coordinate lines are orthogonal.

**The spectral projectors.** $\Pi_+=\begin{pmatrix}1&0\\0&0\end{pmatrix}$ projects onto the image, and $\Pi_-=\begin{pmatrix}0&0\\0&1\end{pmatrix}$ projects onto the kernel. Both are Hermitian and orthogonal, because $S$ is normal.

**The polar factors.** $S$ is positive semidefinite, so $P=S$ and $V=\Pi_+=\begin{pmatrix}1&0\\0&0\end{pmatrix}$. The factor $V$ is a partial isometry, not a $*$-unitary matrix; $S=PV$.

**The pseudo-inverse.** $S^{+}=\begin{pmatrix}\tfrac12&0\\0&0\end{pmatrix}$, and $SS^{+}=S^{+}S=\Pi_+$.

**The algebra reading.** The two idempotents are the images of $\tfrac12(e_t+i\vec e_z)$ and $\tfrac12(e_t-i\vec e_z)$. The element is a non-pure zero divisor: it is $2$ times the Hermitian idempotent $\tfrac12(e_t+i\vec e_z)$. The right annihilator is the minimal right ideal $E_{22}M_2$, of complex dimension two, and the left annihilator is the minimal left ideal $M_2E_{22}$; the element $\tfrac12(e_t-i\vec e_z)$ is a nonzero annihilator on both sides, and the product is zero in both orders.

**The flags.** The matrix is Hermitian and normal, not $*$-unitary. It is the normal singular case: the spectral projectors are orthogonal.

## The Rank-One Matrix

**The matrix.** $X=R=\begin{pmatrix}1&2\\3&6\end{pmatrix}$, with $\tilde Q=\tfrac72e_t+\tfrac{5i}{2}\vec e_x+\tfrac12\vec e_y-\tfrac{5i}{2}\vec e_z$. The vector part has square $B^2=-\tfrac{49}{4}$, so the element is spectrally regular with eigenvalues $7$ and $0$.

**The outer product.** With $u=(1,3)^{\mathsf T}$ and $v=(1,2)^{\mathsf T}$,

$$
R=uv^{\mathsf T},
\qquad
v^{\mathsf T}u=7,
\qquad
R^2=7R.
$$

Hence $E=R/7$ is an idempotent, and $R=7E$ is a complex multiple of an idempotent. The rank is $1$ and the determinant is $0$.

**The kernel and the image.** The kernel is $\mathbb{C}(-2,1)^{\mathsf T}$ and the image is $\mathbb{C}(1,3)^{\mathsf T}$. The row space is $\mathbb{C}(1,2)$ and the left kernel is $\mathbb{C}(-3,1)$; the left kernel is orthogonal to the image, and the right kernel is orthogonal to the row space.

**The spectral projectors.** $E=R/7=\begin{pmatrix}\tfrac17&\tfrac27\\[2pt]\tfrac37&\tfrac67\end{pmatrix}$ projects onto the image along the kernel, and $\mathrm I_2-E$ projects onto the kernel along the image. They are idempotent and $\Pi_+\Pi_-=0$, but they are not Hermitian: $E^{\dagger}=\begin{pmatrix}\tfrac17&\tfrac37\\[2pt]\tfrac27&\tfrac67\end{pmatrix}\neq E$. The two eigenspaces are not orthogonal.

**The polar factors.** $RR^{\dagger}=5\begin{pmatrix}1&3\\3&9\end{pmatrix}$, of rank one and trace $50$, so

$$
P=(RR^{\dagger})^{1/2}=\frac{1}{\sqrt2}\begin{pmatrix}1&3\\3&9\end{pmatrix},
\qquad
V=\frac{1}{\sqrt{50}}R=\frac{1}{\sqrt{50}}\begin{pmatrix}1&2\\3&6\end{pmatrix}.
$$

The factor $P$ is positive semidefinite of rank one and $V$ is a partial isometry; $PV=R$.

**The flags.** The matrix is singular and rank one, but not normal, not Hermitian and not $*$-unitary. It is the rank-one case that is not a Hermitian projector.

**The reading.** The rank-one matrices are the nonzero points of the null cone; the determinantal variety is their closure, with the origin as apex. The element is a non-pure zero divisor, $7$ times the idempotent $E$. The contrast with the singular example is the contrast between a Hermitian rank-one projector and a non-Hermitian one.

## The $*$-Unitary Matrix

**The matrix.** $X=U=\tfrac{1}{\sqrt2}\begin{pmatrix}1&i\\i&1\end{pmatrix}$, with $\tilde Q=\tfrac{1}{\sqrt2}(e_t-\vec e_x)$. The element has norm $Q_t^2+B^2=\tfrac12+\tfrac12=1$, so it lies in the norm-one group.

**The invariants.** $\operatorname{Tr}X=\sqrt2$, $\det X=1$, and

$$
p_X(t)=t^2-\sqrt2\,t+1=(t-\lambda_+)(t-\lambda_-),
\qquad
\lambda_\pm=\frac{1\pm i}{\sqrt2}=e^{\pm i\pi/4}.
$$

The eigenvalues are distinct, so $m_X=p_X$; the rank is $2$.

**The $*$-unitary and normal flags.** $U^{\dagger}U=\mathrm I_2$, so $U$ is $*$-unitary; $*$-unitary matrices are normal. It is not Hermitian, because the $(1,2)$ entry $i/\sqrt2$ is not the conjugate of the $(2,1)$ entry $i/\sqrt2$.

**The eigenbasis.** The eigenvectors are $(1,1)^{\mathsf T}$ for $\lambda_+$ and $(1,-1)^{\mathsf T}$ for $\lambda_-$. With

$$
C=\begin{pmatrix}1&1\\1&-1\end{pmatrix},
\qquad
C^{-1}=\tfrac12C,
\qquad
C/\sqrt2 \text{ is }{}^{*}\text{-unitary},
$$

one has $U=C\operatorname{diag}(\lambda_+,\lambda_-)C^{-1}$.

**The spectral projectors.** $\Pi_+=\tfrac12\begin{pmatrix}1&1\\1&1\end{pmatrix}$ and $\Pi_-=\tfrac12\begin{pmatrix}1&-1\\-1&1\end{pmatrix}$. Both are Hermitian and orthogonal, and $U=\lambda_+\Pi_++\lambda_-\Pi_-$.

**The polar factors.** $P=\mathrm I_2$ and $V=U$: a $*$-unitary matrix is its own $*$-unitary polar factor.

**The reading.** The element is a unit of norm one, hence an element of $SL_2(\mathbb{C})$. Its eigenvalues lie on the unit circle, and the determinant is $1$. The matrix is a rotation rotor: $U^2=i\sigma_1$ and $U^4=-\mathrm I_2$, so its eigenvalues are those of a rotor of angle $\pi/2$; the sign of the rotation axis is the sign convention of the rotor.

## The Hermitian Matrix

**The matrix.** $X=H=\begin{pmatrix}2&1-i\\1+i&-1\end{pmatrix}$, with $\tilde Q=\tfrac12e_t+i(\vec e_x+\vec e_y+\tfrac32\vec e_z)$. The vector part is pure imaginary, so the element lies in the Hermitian subspace.

**The invariants.** $\operatorname{Tr}X=1$, $\det X=-2-|1-i|^2=-4$, and

$$
p_X(t)=t^2-t-4=(t-\lambda_+)(t-\lambda_-),
\qquad
\lambda_\pm=\frac{1\pm\sqrt{17}}{2}.
$$

The eigenvalues are real and distinct, so $m_X=p_X$; the rank is $2$. The signature is $(1,1)$, because the determinant is negative.

**The eigenbasis.** For the eigenvalue $\lambda$, the eigenvector is $v(\lambda)=(2,(\lambda-2)(1+i))^{\mathsf T}$, from the first row $(2-\lambda)x+(1-i)y=0$. The two eigenvectors are orthogonal:

$$
v(\lambda_+)^{\dagger}v(\lambda_-)=0.
$$

**The spectral projectors.** The Lagrange formula gives

$$
\Pi_+=\frac{1}{2\sqrt{17}}
\begin{pmatrix}
3+\sqrt{17}&2(1-i)\\
2(1+i)&\sqrt{17}-3
\end{pmatrix},
\qquad
\Pi_-=\mathrm I_2-\Pi_+.
$$

Both are Hermitian and orthogonal, as the spectral theorem requires.

**The polar factors.** Because $H$ is Hermitian, $|H|$ is the matrix of $|\lambda_\pm|$ in the eigenbasis and $\operatorname{sign}(H)$ is the $*$-unitary matrix of the signs of the eigenvalues; $H=|H|\operatorname{sign}(H)$ is the polar decomposition, with both factors Hermitian.

**The flags.** The matrix is Hermitian and normal, not $*$-unitary: the eigenvalues are real but not of modulus one.

**The reading.** The element is Hermitian, so its spectral projectors are Hermitian and its eigenbasis is orthonormal. The two eigenvalues have opposite signs, so the Hermitian form has signature $(1,1)$ on the two spectral lines.

## The Normal Matrix

**The matrix.** $X=N=\begin{pmatrix}1&1\\-1&1\end{pmatrix}$, with $\tilde Q=e_t-\vec e_y$. The vector part is real, so the spectral direction is pure imaginary and the element is normal.

**The invariants.** $\operatorname{Tr}X=2$, $\det X=2$, and

$$
p_X(t)=t^2-2t+2=(t-\lambda_+)(t-\lambda_-),
\qquad
\lambda_\pm=1\pm i.
$$

The eigenvalues are distinct, so $m_X=p_X$; the rank is $2$.

**The normal flag.** Write $K=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$, so that $N=\mathrm I_2+K$, $K^2=-\mathrm I_2$ and $K^{\dagger}=-K$. Then

$$
N^{\dagger}N=(\mathrm I_2-K)(\mathrm I_2+K)=2\mathrm I_2=NN^{\dagger},
$$

so $N$ is normal. It is not Hermitian, because $K$ is not Hermitian, and it is not $*$-unitary, because $N^{\dagger}N=2\mathrm I_2$.

**The eigenbasis.** The eigenvectors are $(1,i)^{\mathsf T}$ for $1+i$ and $(1,-i)^{\mathsf T}$ for $1-i$. With

$$
C=\begin{pmatrix}1&1\\i&-i\end{pmatrix},
\qquad
C/\sqrt2 \text{ is }{}^{*}\text{-unitary},
$$

one has $N=C\operatorname{diag}(1+i,1-i)C^{-1}$.

**The spectral projectors.** $\Pi_+=\tfrac12\begin{pmatrix}1&-i\\i&1\end{pmatrix}$ and $\Pi_-=\tfrac12\begin{pmatrix}1&i\\-i&1\end{pmatrix}$. Both are Hermitian and orthogonal.

**The polar factors.** $|N|=\sqrt2\,\mathrm I_2$ and $V=N/\sqrt2$; the $*$-unitary factor has determinant $1$, so $N/\sqrt2\in SU(2)$.

**The algebra reading.** $\tilde Q=e_t-\vec e_y$, $\vec Q=-\vec e_y$, $B=1$ and $\vec\Xi=i\vec e_y$. The spectral idempotents are $\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_y)$, which are Hermitian. In a $*$-unitary eigenbasis the pair of nilpotents is exchanged by the star. This is the normal case of *$M_2(\mathbb{C})$ Model : The Eigenbasis and the Diagonalising Matrix*, §*The Normal Case*.

**The flags.** The matrix is normal, neither Hermitian nor $*$-unitary. It is the example that separates normality from the two special normal types.

## The Pattern

The checks are collected in one table.

| Case | $m_X(t)$ | Rank | Diagonalisable | Normal | Hermitian | $*$-Unitary |
|---|---|---|---|---|---|---|
| Scalar | $t-2$ | $2$ | yes | yes | yes | no |
| Jordan | $(t-1)^2$ | $2$ | no | no | no | no |
| Distinct | $t^2-5t-2$ | $2$ | yes | no | no | no |
| Singular | $t(t-2)$ | $1$ | yes | yes | yes | no |
| Rank one | $t(t-7)$ | $1$ | yes | no | no | no |
| $*$-Unitary | $t^2-\sqrt2\,t+1$ | $2$ | yes | yes | no | yes |
| Hermitian | $t^2-t-4$ | $2$ | yes | yes | yes | no |
| Normal | $t^2-2t+2$ | $2$ | yes | yes | no | no |

**The implications.** Hermitian implies normal, and $*$-unitary implies normal; the converse fails in both directions. A normal matrix with a repeated eigenvalue is scalar: the only normal matrix among the three Jordan types is the scalar. A non-scalar Jordan block is never normal.

**The spectral reading.** For a normal matrix the spectral projectors are Hermitian and the eigenbasis is orthonormal; for a non-normal matrix with distinct eigenvalues the same Lagrange formula gives idempotents that are not Hermitian. The distinct-spectrum example and the rank-one example are the two non-normal diagonalisable cases; the Jordan block is the non-diagonalisable case.

**The rank-one reading.** The singular example and the rank-one example both have rank one and determinant zero. The first is a Hermitian projector up to scale, the second is a non-Hermitian idempotent up to scale. The difference is exactly the normality flag: the first is normal, the second is not.

**The group reading.** The $*$-unitary example lies in $SU(2)$; the normal example is $\sqrt2$ times an element of $SU(2)$; the Jordan block and the distinct-spectrum matrix both lie in $GL_2(\mathbb{C})$, with determinants $1$ and $-2$ respectively, so the first is in $SL_2(\mathbb{C})$ and the second is not. The scalar lies in the centre.

## Summary

The eight matrices are read through one checklist: coordinates, trace and determinant, spectrum and minimal polynomial, rank, diagonalisability, commutant, spectral projectors and polar factors. The scalar is the degenerate normal case; the Jordan block is the non-diagonalisable case; the distinct-spectrum matrix is diagonalisable but not normal; the singular matrix is a Hermitian rank-one projector up to scale; the rank-one matrix is a non-Hermitian idempotent up to scale; the $*$-unitary and Hermitian matrices are the two special normal types; and the normal matrix is neither. The pattern table collects the flags, and the two non-normal diagonalisable examples show that diagonalisability does not imply normality.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $X=\mathsf{M}_2(\tilde Q)$ | the matrix of the element |
| $(Q_t,Q_x,Q_y,Q_z)$ | the biquaternion coordinates of $X$ |
| $\tau=\operatorname{Tr}X$, $\delta=\det X$ | the trace and the determinant |
| $\lambda_\pm$ | the two eigenvalues |
| $p_X$, $m_X$ | the characteristic and minimal polynomials |
| $\Pi_\pm$ | the spectral projectors |
| $C(X)$ | the commutant |
| $P=(XX^{\dagger})^{1/2}$ | the positive polar factor |
| $V$ | the $*$-unitary or partial-isometry polar factor |
| $P^{+}$ | the Moore–Penrose inverse of $P$ |
| $E=R/7$ | the idempotent carried by the rank-one example |

## Further Reading

- [$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant](m2c-model-the-product-the-trace-and-the-determinant.html), for the model and the coordinates
- [$M_2(\mathbb{C})$ Model : The Eigenbasis and the Diagonalising Matrix](m2c-model-the-eigenbasis-and-the-diagonalising-matrix.html), for the eigenbasis, the normal case and the diagonalising matrix
- [$M_2(\mathbb{C})$ Model : The Spectral Projectors](m2c-model-the-spectral-projectors.html), for the projectors and the Jordan types
- [$M_2(\mathbb{C})$ Model : The Centraliser and the Double Centraliser](m2c-model-the-centraliser-and-the-double-centraliser.html), for the commutant and the minimal polynomial
- [$M_2(\mathbb{C})$ Representation : The Polar Decomposition of a Matrix](m2c-representation-the-polar-decomposition-of-a-matrix.html), for the polar factors and the singular case
- [$M_2(\mathbb{C})$ Representation : Rank-One Matrices and the Determinantal Variety](m2c-representation-rank-one-matrices-and-the-determinantal-variety.html), for the rank-one and determinantal readings
- [$M_2(\mathbb{C})$ Representation : Trace, Determinant and the Biquaternion Norm](m2c-representation-trace-determinant-and-the-biquaternion-norm.html), for the trace and the determinant
- [$M_2(\mathbb{C})$ Representation : $GL_2(\mathbb{C})$, $SL_2(\mathbb{C})$ and the Determinant](m2c-representation-gl2-sl2-and-the-determinant.html), for the group reading
- [Worked Examples of Eigenbasis of a Biquaternion](worked-examples-of-eigenbasis-of-a-biquaternion.html), for the same computations in the algebra
- *Worked Examples of Exponential Polar Decomposition of Biquaternions*, for the polar computations in the algebra
