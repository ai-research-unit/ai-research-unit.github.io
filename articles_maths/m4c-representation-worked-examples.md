# __$M_4(\mathbb{C})_{\mathbb{B}}$ Representation : Worked Examples__

## Introduction

This article computes eight regular matrices through the same checklist used in the $2\times2$ series: the biquaternion coordinates, the trace and the determinant, the characteristic and minimal polynomials, the spectrum, the rank, the spectral projectors, the polar factors and the normality flags. The eight exhibit the scalar, the Jordan block, the distinct case, the singular case, the rank-one case, the $*$-unitary element, the Hermitian element and the normal element. A closing roster lists the twenty articles of the series with their key formulas.

The article is the $4\times4$ counterpart of *$M_2(\mathbb{C})$ Model : Worked Examples* and the capstone of the series.

**Conventions.** The algebra and the model are those of *$M_4(\mathbb{C})_{\mathbb{B}}$ Model : The Product, the Trace and the Determinant*. In the canonical frame,
$$
\mathsf{M}_4^{L}(\tilde Q)=\mathrm I_2\otimes\mathsf{M}_2(\tilde Q)=\operatorname{diag}(A,A),
\qquad
A=\mathsf{M}_2(\tilde Q),
$$
with
$$
A=\begin{pmatrix}Q_t-iQ_z&-iQ_x-Q_y\\-iQ_x+Q_y&Q_t+iQ_z\end{pmatrix}.
$$
The inverse map is
$$
Q_t=\tfrac{a+d}{2},\quad
Q_x=\tfrac{i(b+c)}{2},\quad
Q_y=\tfrac{c-b}{2},\quad
Q_z=\tfrac{i(a-d)}{2},
$$
for $A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$. The trace is $\operatorname{Tr}\mathsf{M}_4^{L}(\tilde Q)=4Q_t$, the determinant is $\langle\tilde Q\rangle_{\natural}^2$, and the eigenvalues are $\lambda_\pm=Q_t\pm iB$ with $B^2=Q_x^2+Q_y^2+Q_z^2$, each twice.

**Boundaries.** The construction is *$M_4(\mathbb{C})_{\mathbb{B}}$ Model : The Product, the Trace and the Determinant*; the eigenbasis is *$M_4(\mathbb{C})_{\mathbb{B}}$ Model : The Eigenbasis and the Diagonalising Matrix*; the projectors are *$M_4(\mathbb{C})_{\mathbb{B}}$ Model : The Spectral Projectors*; the polar factors are *$M_4(\mathbb{C})_{\mathbb{B}}$ Representation : The Polar Decomposition of a Matrix*; the rank is *$M_4(\mathbb{C})_{\mathbb{B}}$ Representation : Rank-One Matrices and the Determinantal Variety*; the groups are *$M_4(\mathbb{C})_{\mathbb{B}}$ Representation : $GL_2(\mathbb{C})$, $SL_2(\mathbb{C})$ and the Determinant*.

**Frame.** Unless a basis is named, matrices are written in the canonical frame of *Conventions of the Matrix Models*, §*The Matrix Models*, where $\mathsf{M}_4^{L}(\tilde Q)=I_2\otimes\mathsf{M}_2(\tilde Q)$. The coefficient basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$ is the conjugate display: $\mathsf M_{4,\mathrm{coef}}^{L}=S\,(I_2\otimes\mathsf M_2)\,S^{-1}$, with $S$ the change of *The Product, the Trace and the Determinant*.

## The Method

**The invariants.** Put $\tau=\operatorname{Tr}A=2Q_t$ and $\delta=\det A=N$. The characteristic polynomial of $A$ is
$$
p_A(t)=t^2-\tau t+\delta=(t-\lambda_+)(t-\lambda_-),
\qquad
\lambda_\pm=\frac{\tau\pm\sqrt{\tau^2-4\delta}}{2}.
$$
The regular matrix has each eigenvalue twice, so
$$
p_X(t)=p_A(t)^2,\qquad
\operatorname{Tr}X=2\tau=4Q_t,\qquad
\det X=\delta^2=N^2.
$$

**The minimal polynomial.** The spectral type is read from $p_A$ and from the size of the eigenspace:

| Type | $m_A(t)$ | $m_X(t)$ | Diagonalisable |
|---|---|---|---|
| scalar, $A=\lambda\mathrm I_2$ | $t-\lambda$ | $t-\lambda$ | yes |
| non-scalar, distinct eigenvalues | $(t-\lambda_+)(t-\lambda_-)$ | $(t-\lambda_+)(t-\lambda_-)$ | yes |
| non-scalar, repeated eigenvalue | $(t-\lambda)^2$ | $(t-\lambda)^2$ | no |

**The rank.** The rank of $X$ is twice the rank of $A$: it is $4$ when $N\neq0$, $2$ when $N=0$ and $\tilde Q\neq0$, and $0$ when $\tilde Q=0$. The regular model therefore has only the ranks $0,2,4$.

**The spectral projectors.** When the eigenvalues are distinct,
$$
\Pi_+=\frac{A-\lambda_-\mathrm I_2}{\lambda_+-\lambda_-},
\qquad
\Pi_-=\mathrm I_2-\Pi_+,
$$
and the regular projectors are $\rho_\pm=\operatorname{diag}(\Pi_\pm,\Pi_\pm)$, of rank two. They satisfy $\rho_+\rho_-=0$ and $\rho_++\rho_-=\mathrm I_4$.

**The polar factors.** The positive factor is $P=(XX^{\dagger})^{1/2}$ and the $*$-unitary factor is $V$ with $X=PV$. When $X$ is invertible, $V=P^{-1}X$ is $*$-unitary; when $X$ is singular, $V=P^{+}X$ is a partial isometry.

**The flags.** A matrix is Hermitian when $X=X^{\dagger}$, $*$-unitary when $X^{\dagger}X=\mathrm I_4$, and normal when $XX^{\dagger}=X^{\dagger}X$. Hermitian and $*$-unitary matrices are normal.

## The Eight Matrices

The eight matrices, their blocks $A$ and their basic invariants are collected here; the sections that follow compute each one.

| Case | $A$ | $(Q_t,Q_x,Q_y,Q_z)$ | $\operatorname{Tr}X$ | $\det X$ | Spectrum |
|---|---|---|---|---|---|
| Scalar | $2\mathrm I_2$ | $(2,0,0,0)$ | $8$ | $16$ | $2,2,2,2$ |
| Jordan | $\begin{pmatrix}1&1\\0&1\end{pmatrix}$ | $(1,\tfrac{i}{2},-\tfrac12,0)$ | $4$ | $1$ | $1,1,1,1$ |
| Distinct | $\begin{pmatrix}1&2\\3&4\end{pmatrix}$ | $(\tfrac52,\tfrac{5i}{2},\tfrac12,-\tfrac{3i}{2})$ | $10$ | $4$ | $\tfrac{5\pm\sqrt{33}}{2}$ twice |
| Singular | $\begin{pmatrix}2&0\\0&0\end{pmatrix}$ | $(1,0,0,i)$ | $4$ | $0$ | $2,0$ twice |
| Rank one | $\begin{pmatrix}1&2\\3&6\end{pmatrix}$ | $(\tfrac72,\tfrac{5i}{2},\tfrac12,-\tfrac{5i}{2})$ | $14$ | $0$ | $7,0$ twice |
| $*$-Unitary | $\tfrac{1}{\sqrt2}\begin{pmatrix}1&i\\i&1\end{pmatrix}$ | $(\tfrac{1}{\sqrt2},-\tfrac{1}{\sqrt2},0,0)$ | $2\sqrt2$ | $1$ | $e^{\pm i\pi/4}$ twice |
| Hermitian | $\begin{pmatrix}2&1-i\\1+i&-1\end{pmatrix}$ | $(\tfrac12,i,i,\tfrac{3i}{2})$ | $2$ | $16$ | $\tfrac{1\pm\sqrt{17}}{2}$ twice |
| Normal | $\begin{pmatrix}1&1\\-1&1\end{pmatrix}$ | $(1,0,-1,0)$ | $4$ | $4$ | $1\pm i$ twice |

The table is read with the inverse map of the introduction; the coordinates are the four complex numbers $Q_t,Q_x,Q_y,Q_z$ of the block, and the regular matrix is $X=\operatorname{diag}(A,A)$.

## The Scalar Matrix

**The matrix.** $A=2\mathrm I_2$, $X=2\mathrm I_4$, and $\tilde Q=2e_t$. It is central.

**The invariants.** $\operatorname{Tr}X=8$, $\det X=16$, $p_X(t)=(t-2)^4$ and $m_X(t)=t-2$. The spectrum is $\{2\}$, the rank is $4$, and the eigenspace is the whole of $\mathbb{C}^4$.

**The commutant.** $C(X)=M_4(\mathbb{C})$, and the relative commutant is the whole image. The double relative commutant is $C_L(C_L(X))=\mathbb{C}\mathrm I_4$, the centre, because the image is a central simple algebra and its centraliser in itself is the centre.

**The flags.** The matrix is normal and Hermitian, because $2$ is real. It is not $*$-unitary, because $|2|\neq1$; the scalar $\tfrac12X=\mathrm I_4$ is $*$-unitary.

**The polar factors.** $P=2\mathrm I_4$ and $V=\mathrm I_4$.

**The reading.** The scalar is the degenerate spectral case: one eigenvalue, one spectral projector $\mathrm I_4$, and no eigenbasis to choose. In the algebra it is the central line $\mathbb{C}e_t$.

## The Jordan Block

**The matrix.** $A=J=\begin{pmatrix}1&1\\0&1\end{pmatrix}$, $X=\operatorname{diag}(J,J)$, and $\tilde Q=e_t+\tfrac{i}{2}\vec e_x-\tfrac12\vec e_y$. The vector part is null, $B=0$, and $Q_t=1$.

**The invariants.** $\operatorname{Tr}X=4$, $\det X=1$, $p_X(t)=(t-1)^4$ and $m_X(t)=(t-1)^2$. The spectrum is $\{1\}$, the rank is $4$, and each block has a one-dimensional eigenspace, of dimension two in $\mathbb{C}^4$. The matrix is invertible and not diagonalisable.

**The Jordan chain.** With $N=J-\mathrm I_2=\begin{pmatrix}0&1\\0&0\end{pmatrix}$, $N^2=0$ and $J=\mathrm I_2+N$. The chain is repeated in the two blocks.

**The commutant.** The relative commutant is $\{a\mathrm I_4+b\operatorname{diag}(N,N)\}$, of complex dimension two. The full commutant in $M_4(\mathbb{C})$ is $M_2(\mathbb{C})\otimes\mathbb{C}[J]$, of dimension eight.

**The flags.** The matrix is not normal, because $JJ^{\dagger}\neq J^{\dagger}J$.

**The polar factors.** $P=\operatorname{diag}((JJ^{\dagger})^{1/2},(JJ^{\dagger})^{1/2})$ and $V=P^{-1}X$; both are block diagonal, and $V$ is $*$-unitary because $J$ is invertible.

## The Matrix with Distinct Eigenvalues

**The matrix.** $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$, $X=\operatorname{diag}(A,A)$, and $\tilde Q=\tfrac52e_t+\tfrac{5i}{2}\vec e_x+\tfrac12\vec e_y-\tfrac{3i}{2}\vec e_z$.

**The invariants.** $\operatorname{Tr}A=5$, $\det A=-2$, $\operatorname{Tr}X=10$, $\det X=4$. The eigenvalues of $A$ are $\tfrac{5\pm\sqrt{33}}{2}$, distinct and nonzero; the regular matrix has each twice. The rank is $4$.

**The spectral projectors.** The two rank-two projectors are
$$
\rho_\pm=\operatorname{diag}\left(\frac{A-\lambda_\mp\mathrm I_2}{\lambda_+-\lambda_-},\frac{A-\lambda_\mp\mathrm I_2}{\lambda_+-\lambda_-}\right),
$$
and $X=\lambda_+\rho_++\lambda_-\rho_-$. They are not Hermitian, because $A$ is not normal.

**The commutant.** The relative commutant is $\mathrm I_2\otimes\mathbb{C}[A]$, of complex dimension two; the full commutant is the eight-dimensional algebra of block matrices with each block in $\mathbb{C}[A]$.

**The flags.** The matrix is not normal, because $AA^{\dagger}\neq A^{\dagger}A$.

**The polar factors.** $P=\operatorname{diag}((AA^{\dagger})^{1/2},(AA^{\dagger})^{1/2})$ and $V=P^{-1}X$, $*$-unitary because $A$ is invertible.

## The Singular Matrix

**The matrix.** $A=S=\begin{pmatrix}2&0\\0&0\end{pmatrix}$, $X=\operatorname{diag}(S,S)$, and $\tilde Q=e_t+i\vec e_z$. The norm is $1-1=0$, so the element is a zero divisor.

**The invariants.** $\operatorname{Tr}X=4$, $\det X=0$, $p_X(t)=t^2(t-2)^2$ and $m_X(t)=t(t-2)$. The spectrum is $\{2,0\}$ with multiplicity two each, the rank is $2$, and the matrix is diagonalisable.

**The kernel and the image.** Each block has kernel $\mathbb{C}(0,1)^{\mathsf T}$ and image $\mathbb{C}(1,0)^{\mathsf T}$; in the regular model the kernel and the image are the direct sums of the two, and the two coordinate planes are orthogonal.

**The spectral projectors.** $\rho_+=\operatorname{diag}(E_{11},E_{11})$ projects onto the image plane, and $\rho_-=\operatorname{diag}(E_{22},E_{22})$ projects onto the kernel plane. Both are Hermitian and orthogonal, because $S$ is normal.

**The polar factors.** $S\ge0$, so $P=X$ and $V=\rho_+$; the factor $V$ is a partial isometry, not a $*$-unitary matrix.

**The pseudo-inverse.** $X^{+}=\operatorname{diag}(\tfrac12E_{11},\tfrac12E_{11})$, and $XX^{+}=X^{+}X=\rho_+$.

**The algebra reading.** The two idempotents are the images of $\tfrac12(e_t+i\vec e_z)$ and $\tfrac12(e_t-i\vec e_z)$, doubled. The element is a non-pure zero divisor: $2$ times the Hermitian idempotent. The right annihilator is the doubled minimal right ideal, of complex dimension two, and the left annihilator is the doubled minimal left ideal.

**The flags.** The matrix is Hermitian and normal, not $*$-unitary. It is the normal singular case.

## The Rank-One Matrix

**The matrix.** $A=R=\begin{pmatrix}1&2\\3&6\end{pmatrix}$, $X=\operatorname{diag}(R,R)$, and $\tilde Q=\tfrac72e_t+\tfrac{5i}{2}\vec e_x+\tfrac12\vec e_y-\tfrac{5i}{2}\vec e_z$. The block has eigenvalues $7$ and $0$.

**The outer product.** With $u=(1,3)^{\mathsf T}$ and $v=(1,2)^{\mathsf T}$,
$$
R=uv^{\mathsf T},\qquad v^{\mathsf T}u=7,\qquad R^2=7R.
$$
Hence $E=R/7$ is an idempotent, and $X=7\operatorname{diag}(E,E)$ is a complex multiple of a rank-two idempotent. The rank is $2$ and the determinant is $0$.

**The kernel and the image.** Each block has kernel $\mathbb{C}(-2,1)^{\mathsf T}$ and image $\mathbb{C}(1,3)^{\mathsf T}$; in the regular model these are doubled into planes.

**The spectral projectors.** $\rho_+=\operatorname{diag}(E,E)$ projects onto the image plane along the kernel plane, and $\mathrm I_4-\rho_+$ projects onto the kernel plane along the image plane. They are idempotent and orthogonal, but not Hermitian: $\rho_+^{\dagger}\neq\rho_+$.

**The polar factors.** $RR^{\dagger}=5\begin{pmatrix}1&3\\3&9\end{pmatrix}$ has rank one, so
$$
P=\frac{1}{\sqrt2}\operatorname{diag}\left(\begin{pmatrix}1&3\\3&9\end{pmatrix},\begin{pmatrix}1&3\\3&9\end{pmatrix}\right),
\qquad
V=\frac{1}{\sqrt{50}}X.
$$
The factor $P$ is positive semidefinite of rank two and $V$ is a partial isometry; $PV=X$.

**The flags.** The matrix is singular and rank two, but not normal, not Hermitian and not $*$-unitary.

**The reading.** The rank-two elements are the nonzero points of the null cone; the determinantal variety is their closure, with the origin as apex. The element is a non-pure zero divisor, $7$ times the idempotent. The contrast with the singular example is the contrast between a Hermitian rank-two projector and a non-Hermitian one.

## The $*$-Unitary Matrix

**The matrix.** $A=\tfrac{1}{\sqrt2}\begin{pmatrix}1&i\\i&1\end{pmatrix}$, $X=\operatorname{diag}(A,A)$, and $\tilde Q=\tfrac{1}{\sqrt2}(e_t-\vec e_x)$.

**The invariants.** $\operatorname{Tr}A=\sqrt2$, $\det A=1$, $\operatorname{Tr}X=2\sqrt2$, $\det X=1$. The eigenvalues of $A$ are $e^{\pm i\pi/4}$, each twice. The rank is $4$.

**The $*$-unitary condition.** $A^{\dagger}A=\mathrm I_2$, because $\tilde Q^{*}\tilde Q=e_t$. The matrix $X$ is $*$-unitary, and its determinant has modulus one.

**The spectral projectors.** The two rank-two projectors are $\rho_\pm=\operatorname{diag}(\Pi_\pm,\Pi_\pm)$, with $\Pi_\pm$ the rank-one projectors of $A$. They are Hermitian and orthogonal.

**The commutant.** The relative commutant is $\mathrm I_2\otimes\mathbb{C}[A]$, of dimension two; the full commutant is $M_2(\mathbb{C})\otimes\mathbb{C}[A]$, of dimension eight.

**The polar factors.** $X$ is $*$-unitary, so $P=\mathrm I_4$ and $V=X$.

**The reading.** The element is a unit of norm one. Its eigenvalues lie on the unit circle, and the determinant is $1$; it is the double of a rotor of angle $\pi/2$.

## The Hermitian Matrix

**The matrix.** $A=H=\begin{pmatrix}2&1-i\\1+i&-1\end{pmatrix}$, $X=\operatorname{diag}(H,H)$, and $\tilde Q=\tfrac12e_t+i(\vec e_x+\vec e_y+\tfrac32\vec e_z)$.

**The invariants.** $\operatorname{Tr}X=2$, $\det X=16$, and
$$
p_X(t)=(t^2-t-4)^2,
\qquad
\lambda_\pm=\frac{1\pm\sqrt{17}}{2},
$$
each twice. The eigenvalues are real and distinct, so $m_X=t^2-t-4$; the rank is $4$.

**The eigenbasis.** The eigenvectors are those of $H$, repeated in the two blocks; they are orthogonal because $H$ is Hermitian.

**The spectral projectors.** The Lagrange projectors $\rho_\pm=\operatorname{diag}(\Pi_\pm,\Pi_\pm)$ are Hermitian and orthogonal, of rank two each.

**The polar factors.** Because $H$ is Hermitian, $|X|=\operatorname{diag}(|H|,|H|)$ and $\operatorname{sign}(X)=\operatorname{diag}(\operatorname{sign}H,\operatorname{sign}H)$; both factors are Hermitian.

**The flags.** The matrix is Hermitian and normal, not $*$-unitary: the eigenvalues are real but not of modulus one.

**The reading.** The element lies in $\mathbb{M}_+$, so its spectral projectors are Hermitian and its eigenbasis is orthonormal. The two eigenvalues have opposite signs, so the Hermitian form has signature $(1,1)$ on the two spectral planes.

## The Normal Matrix

**The matrix.** $A=N=\begin{pmatrix}1&1\\-1&1\end{pmatrix}$, $X=\operatorname{diag}(N,N)$, and $\tilde Q=e_t-\vec e_y$.

**The invariants.** $\operatorname{Tr}X=4$, $\det X=4$, and
$$
p_X(t)=(t^2-2t+2)^2,
\qquad
\lambda_\pm=1\pm i,
$$
each twice. The rank is $4$.

**The normal flag.** With $K=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$, $A=\mathrm I_2+K$, $K^2=-\mathrm I_2$, and
$$
A^{\dagger}A=(\mathrm I_2-K)(\mathrm I_2+K)=2\mathrm I_2=AA^{\dagger},
$$
so $X$ is normal. It is not Hermitian and not $*$-unitary, because $X^{\dagger}X=2\mathrm I_4$.

**The eigenbasis.** The eigenvectors of $A$ are $(1,i)^{\mathsf T}$ and $(1,-i)^{\mathsf T}$, repeated in the two blocks; the eigenbasis is orthonormal.

**The spectral projectors.** $\rho_\pm=\operatorname{diag}(\Pi_\pm,\Pi_\pm)$ are Hermitian and orthogonal.

**The polar factors.** $|X|=\sqrt2\,\mathrm I_4$ and $V=X/\sqrt2$; the $*$-unitary factor has determinant $1$, so $X/\sqrt2$ lies in the image of $SU(2)$.

**The flags.** The matrix is normal, neither Hermitian nor $*$-unitary.

## The Pattern

The checks are collected in one table.

| Case | $m_X(t)$ | Rank | Diagonalisable | Normal | Hermitian | $*$-Unitary |
|---|---|---|---|---|---|---|
| Scalar | $t-2$ | $4$ | yes | yes | yes | no |
| Jordan | $(t-1)^2$ | $4$ | no | no | no | no |
| Distinct | $t^2-5t-2$ | $4$ | yes | no | no | no |
| Singular | $t(t-2)$ | $2$ | yes | yes | yes | no |
| Rank one | $t(t-7)$ | $2$ | yes | no | no | no |
| $*$-Unitary | $t^2-\sqrt2\,t+1$ | $4$ | yes | yes | no | yes |
| Hermitian | $t^2-t-4$ | $4$ | yes | yes | yes | no |
| Normal | $t^2-2t+2$ | $4$ | yes | yes | no | no |

**The implications.** Hermitian implies normal, and $*$-unitary implies normal; the converse fails in both directions. A normal matrix with a repeated eigenvalue is scalar: the only normal matrix among the three Jordan types is the scalar. A non-scalar Jordan block is never normal. In the regular model each block is doubled, so every rank and every eigenvalue multiplicity is doubled, and the implications are read blockwise.

**The spectral reading.** For a normal matrix the spectral projectors are Hermitian and the eigenbasis is orthonormal; for a non-normal matrix with distinct eigenvalues the same Lagrange formula gives idempotents that are not Hermitian. The distinct-spectrum example and the rank-one example are the two non-normal diagonalisable cases; the Jordan block is the non-diagonalisable case.

**The rank reading.** The singular example and the rank-one example both have rank two and determinant zero. The first is a Hermitian projector up to scale, the second is a non-Hermitian idempotent up to scale. The difference is exactly the normality flag: the first is normal, the second is not.

**The group reading.** The $*$-unitary example lies in the image of $SU(2)$; the normal example is $\sqrt2$ times such an element; the Jordan block and the distinct-spectrum matrix both lie in the image of $GL_2(\mathbb{C})$, with determinants $1$ and $4$, so the first is in the image of $SL_2(\mathbb{C})$ and the second is not. The scalar lies in the centre.


| Article | Subject | Key formula |
|---|---|---|
| The Matrix Product and the Algebra Structure | the model | $\mathsf{M}_4^{L}(\tilde Q)$ injective, $\operatorname{diag}(A,A)$ in the Peirce basis |
| The Four Words and the Four Traces | the trace pairing | $\operatorname{Tr}(XY)=4\langle\tilde X,\tilde Y\rangle$ |
| Peirce Coordinates, Matrix Units and the Spinor Planes | the corners and the spinors | the four entries, each doubled; the two planes $\mathbb{B}\Pi_\pm$ |
| Trace, Determinant and the Biquaternion Norm | the invariants | $\operatorname{Tr}X=4Q_t$, $\det X=N^2$ |
| The Killing Form | the Lie form | $\kappa_{\mathbb{C}}=-8\vec X\cdot\vec Y$ |
| Rank-One Matrices and the Determinantal Variety | the strata | $\operatorname{rk}X=2\operatorname{rk}A\in\{0,2,4\}$ |
| Spin, Qubits and the Bloch Vector | the states | $\rho_4=\tfrac12\mathrm I_2\otimes\rho$ |
| The Polar Decomposition of a Matrix | the factors | $X=PV$, $P=(XX^{\dagger})^{1/2}$ |
| The Spectral Projectors and the Nilpotents | the spectrum | $\rho_\pm$ of rank two |
| The Eigenbasis and the Diagonalising Matrix | the basis | $X=\operatorname{diag}(A,A)$ |
| The Centraliser and the Double Centraliser | the commutants and the right matrix | $C_L(X)\cong\mathbb{C}[A]$, $C_L(C_L(X))\cong\mathbb{C}[A]$, $\mathsf{M}_4^{R}(\tilde Q)$ |
| The Conjugations and the Adjoints | the involutions | $X^{\dagger}=M_X^{\dagger}$; $X^{\mathsf T}=M_{X^{\natural}}$ in the coefficient basis |
| The Six Subspaces as Matrix Conditions | the real forms | Hermitian, anti-Hermitian, quaternion, anti-quaternion |
| Worked Examples | this article | the eight matrices and the roster |
| $GL_2(\mathbb{C})$, $SL_2(\mathbb{C})$ and the Determinant | the groups | $\det X=N^2$, $\ker\det=\{N=\pm1\}$ |
| The Functional Calculus | the exponential, the logarithm and the roots | $\exp X=\mathsf{M}_4^{L}(\exp\tilde Q)$, $\log X=\mathsf{M}_4^{L}(\log\tilde Q)$, $X^{1/2}=(X+\sqrt N\mathrm I_4)/\sqrt{\tfrac12\operatorname{Tr}X+2\sqrt N}$ |
| The Sandwich as a Matrix Congruence | the action | $X\mapsto MXM^{\dagger}$, $\det$ scales by $\lvert N\rvert^4$ |
| The Projective Line and the Möbius Action | the ideals | $J_L$, $z\mapsto(az+b)/(cz+d)$ |

## Summary

The eight examples exhibit the scalar, the Jordan block, the distinct case, the singular case, the rank-one case, the $*$-unitary element, the Hermitian element and the normal element. The regular matrix has the invariants $\operatorname{Tr}X=4Q_t$, $\det X=N^2$, the eigenvalues $\lambda_\pm$ each twice, and the rank $2\operatorname{rk}A\in\{0,2,4\}$. The spectral projectors have rank two, the polar factors are the images of the algebra factors, and the flags Hermitian, $*$-unitary and normal are read from $X$. The roster collects the twenty articles of the series and their key formulas.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $X=\mathsf{M}_4^{L}(\tilde Q)$ | the regular matrix |
| $A=\mathsf{M}_2(\tilde Q)$ | the $2\times2$ block |
| $\tau=2Q_t$, $\delta=N$ | the trace and determinant of $A$ |
| $\lambda_\pm=Q_t\pm iB$ | the eigenvalues, each twice |
| $\rho_\pm$ | the rank-two spectral projectors |
| $P,V$ | the polar factors |

## Further Reading

- [$M_4(\mathbb{C})_{\mathbb{B}}$ Model : The Product, the Trace and the Determinant](m4c-model-the-product-the-trace-and-the-determinant.html), for the model
- [$M_4(\mathbb{C})_{\mathbb{B}}$ Model : The Eigenbasis and the Diagonalising Matrix](m4c-model-the-eigenbasis-and-the-diagonalising-matrix.html), for the basis
- [$M_2(\mathbb{C})$ Representation : Worked Examples](m2c-representation-worked-examples.html), for the $2\times2$ version
- [Worked Examples of an Eigenbasis of a Biquaternion](worked-examples-of-an-eigenbasis-of-a-biquaternion.html), for the algebra
- *Worked Examples of Exponential Polar Decomposition of Biquaternions*, for the algebra
