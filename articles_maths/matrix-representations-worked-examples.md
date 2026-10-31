# __Matrix Representations : Worked Examples__

## Introduction

This article computes eight matrices through the same checklist: coordinates, trace and determinant, characteristic and minimal polynomials, spectrum, rank, diagonalising matrix or Jordan chain, commutant, spectral projectors, polar factors and normality flags. Each matrix exhibits one structure. The eight are a scalar, a Jordan block, a matrix with distinct eigenvalues, a singular matrix, a rank-one matrix, a $*$-unitary matrix, a Hermitian matrix and a normal matrix that is neither Hermitian nor $*$-unitary.

The article is the worked counterpart of the whole series. Each computation is done once in the entry model and once in the regular model, and the two columns show the doubling rule.

**Conventions.** The algebra and the displays are those of *Matrix Representations : The Models and the Change of Frame*. An element is $\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$, its entry-model matrix is
$$
A=\mathsf M_2(\tilde Q)=
\begin{pmatrix}
Q_t-iQ_z&-iQ_x-Q_y\\
-iQ_x+Q_y&Q_t+iQ_z
\end{pmatrix},
$$
and the inverse map for $A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$ is
$$
Q_t=\tfrac{a+d}{2},\qquad
Q_x=\tfrac{i(b+c)}{2},\qquad
Q_y=\tfrac{c-b}{2},\qquad
Q_z=\tfrac{i(a-d)}{2}.
$$
The regular matrix is $X=L(\tilde Q)=\operatorname{diag}(A,A)$ in the Peirce frame. The variable of the characteristic polynomial is $t$, and the eigenvalues of $A$ are $\lambda_\pm$.

**Boundaries.** The construction is *Matrix Representations : The Models and the Change of Frame*; the spectral theory is *Matrix Representations : The Eigenbasis and the Diagonalising Matrix* and *Matrix Representations : The Jordan Basis and the Jordanising Matrix*; the polar factors are *Matrix Representations : The Polar Decomposition of a Matrix*; the rank-one theory is *Matrix Representations : Rank-One Matrices and the Determinantal Variety*; the group theory is *Matrix Representations : GL2, SL2 and the Determinant*.

## The Method

**The invariants.** Put $\tau=\operatorname{Tr}A$ and $\delta=\det A$. Then
$$
p_A(t)=t^2-\tau t+\delta=(t-\lambda_+)(t-\lambda_-),
\qquad
\lambda_\pm=\frac{\tau\pm\sqrt{\tau^2-4\delta}}{2}.
$$
The discriminant is $(\lambda_+-\lambda_-)^2$; the eigenvalues are distinct exactly when it is nonzero.

**The minimal polynomial.**

| Type | $m_A(t)$ | Diagonalisable |
|---|---|---|
| scalar, $A=\lambda\mathrm I_2$ | $t-\lambda$ | yes |
| non-scalar, distinct eigenvalues | $(t-\lambda_+)(t-\lambda_-)$ | yes |
| non-scalar, repeated eigenvalue | $(t-\lambda)^2$ | no |

A non-scalar matrix with a repeated eigenvalue is a Jordan block: $A=C(\lambda\mathrm I_2+N)C^{-1}$ with $N\neq0$ and $N^2=0$.

**The rank.** The rank is $2$ when $\delta\neq0$, $1$ when $\delta=0$ and $A\neq0$, and $0$ only for $A=0$. Every nonzero singular $2\times2$ matrix has rank one; the singular example below is diagonal and reads the determinant, the kernel and the pseudo-inverse, while the rank-one example is non-diagonal and reads the outer-product factorisation.

**The spectral projectors.** For distinct eigenvalues,
$$
\Pi_+=\frac{A-\lambda_-\mathrm I_2}{\lambda_+-\lambda_-},
\qquad
\Pi_-=\mathrm I_2-\Pi_+,
\qquad
A=\lambda_+\Pi_++\lambda_-\Pi_- .
$$
The two are idempotent and satisfy $\Pi_+\Pi_-=0$. They are Hermitian exactly when $A$ is normal; for a non-normal matrix the eigenspaces are not orthogonal.

**The commutant.** For a non-scalar $A$ the commutant is $\mathbb{C}[A]=\operatorname{span}\{\mathrm I_2,A\}$, of complex dimension two; for a scalar it is the whole algebra. The double commutant returns $\mathbb{C}[A]$ in both cases.

**The polar factors.** $P=(AA^{\dagger})^{1/2}$ and $A=PV$. When $A$ is invertible, $V=P^{-1}A$ is $*$-unitary; when $A$ is singular, $V=P^{+}A$ is a partial isometry.

**The flags.** Hermitian means $A=A^{\dagger}$, $*$-unitary means $A^{\dagger}A=\mathrm I_2$, normal means $AA^{\dagger}=A^{\dagger}A$. Hermitian and $*$-unitary each imply normal; the converses fail.

**The doubling rule.** For the regular matrix $X=\operatorname{diag}(A,A)$,
$$
\operatorname{Tr}X=2\operatorname{Tr}A,\qquad
\det X=(\det A)^2,\qquad
\operatorname{rank}X=2\operatorname{rank}A,
$$
and every eigenvalue and every Jordan block is doubled. The minimal polynomial is unchanged, and the flags are read blockwise.

## The Eight Matrices

| Case | $A$ | $(Q_t,Q_x,Q_y,Q_z)$ | $\operatorname{Tr}$ of $A$ / $X$ | $\det$ of $A$ / $X$ | Spectrum of $A$ / $X$ |
|---|---|---|---|---|---|
| Scalar | $2\mathrm I_2$ | $(2,0,0,0)$ | $4$ / $8$ | $4$ / $16$ | $2,2$ / $2,2,2,2$ |
| Jordan | $\begin{pmatrix}1&1\\0&1\end{pmatrix}$ | $(1,\tfrac{i}{2},-\tfrac12,0)$ | $2$ / $4$ | $1$ / $1$ | $1,1$ / $1,1,1,1$ |
| Distinct | $\begin{pmatrix}1&2\\3&4\end{pmatrix}$ | $(\tfrac52,\tfrac{5i}{2},\tfrac12,-\tfrac{3i}{2})$ | $5$ / $10$ | $-2$ / $4$ | $\tfrac{5\pm\sqrt{33}}{2}$, twice |
| Singular | $\begin{pmatrix}2&0\\0&0\end{pmatrix}$ | $(1,0,0,i)$ | $2$ / $4$ | $0$ / $0$ | $2,0$, twice |
| Rank one | $\begin{pmatrix}1&2\\3&6\end{pmatrix}$ | $(\tfrac72,\tfrac{5i}{2},\tfrac12,-\tfrac{5i}{2})$ | $7$ / $14$ | $0$ / $0$ | $7,0$, twice |
| $*$-Unitary | $\tfrac1{\sqrt2}\begin{pmatrix}1&i\\i&1\end{pmatrix}$ | $(\tfrac1{\sqrt2},-\tfrac1{\sqrt2},0,0)$ | $\sqrt2$ / $2\sqrt2$ | $1$ / $1$ | $e^{\pm i\pi/4}$, twice |
| Hermitian | $\begin{pmatrix}2&1-i\\1+i&-1\end{pmatrix}$ | $(\tfrac12,i,i,\tfrac{3i}{2})$ | $1$ / $2$ | $-4$ / $16$ | $\tfrac{1\pm\sqrt{17}}{2}$, twice |
| Normal | $\begin{pmatrix}1&1\\-1&1\end{pmatrix}$ | $(1,0,-1,0)$ | $2$ / $4$ | $2$ / $4$ | $1\pm i$, twice |

The coordinates are the four complex numbers $Q_\mu$ of the block, not the four entries. The regular matrix is $X=\operatorname{diag}(A,A)$.

## The Scalar

**Entry model.** $A=2\mathrm I_2$, $\tilde Q=2e_t$. Then $\operatorname{Tr}A=4$, $\det A=4$, $p_A(t)=(t-2)^2$, $m_A(t)=t-2$, and the rank is two.

**Regular model.** $X=2\mathrm I_4$. Then $\operatorname{Tr}X=8$, $\det X=16$, $p_X(t)=(t-2)^4$, $m_X(t)=t-2$, and the rank is four.

**Reading.** The scalar is the only matrix whose minimal polynomial has degree one. It is normal, Hermitian and central; it is $*$-unitary only when $\lvert\lambda\rvert=1$, which fails here.

## The Jordan Block

**Entry model.** $A=\begin{pmatrix}1&1\\0&1\end{pmatrix}$, with $Q_t=1$, $Q_x=\tfrac{i}{2}$, $Q_y=-\tfrac12$, $Q_z=0$. Then $\operatorname{Tr}A=2$, $\det A=1$, $p_A(t)=(t-1)^2$, $m_A(t)=(t-1)^2$, and the rank is two. The spectral projector is the whole matrix, and there is no eigenbasis.

**Regular model.** $X=J\oplus J$ has $\operatorname{Tr}X=4$, $\det X=1$, $p_X(t)=(t-1)^4$ and $m_X(t)=(t-1)^2$; the rank is four. The Jordan form has two blocks of size two, not one block of size four.

**Reading.** The block is neither diagonalisable nor normal. It lies in $SL_2(\mathbb{C})$ and its regular image in the image of $SL_2$.

## The Distinct Eigenvalues

**Entry model.** $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$ has $\tau=5$, $\delta=-2$, so
$$
\lambda_\pm=\frac{5\pm\sqrt{33}}{2},\qquad
p_A(t)=t^2-5t-2,\qquad m_A(t)=p_A(t).
$$
The spectral projectors are
$$
\Pi_\pm=\pm\frac{A-\lambda_\mp\mathrm I_2}{\sqrt{33}},
$$
they are idempotent and not Hermitian, because $A$ is not normal.

**Regular model.** $X=\operatorname{diag}(A,A)$ has $\operatorname{Tr}X=10$, $\det X=4$, the same minimal polynomial, and each eigenvalue twice. The projectors are $\operatorname{diag}(\Pi_\pm,\Pi_\pm)$, of rank two.

**Reading.** The matrix is diagonalisable and not normal. It lies in $GL_2(\mathbb{C})$ with determinant $-2$, so it is not in $SL_2$.

## The Singular Matrix

**Entry model.** $A=\begin{pmatrix}2&0\\0&0\end{pmatrix}$ has $\tau=2$, $\delta=0$, $p_A(t)=t(t-2)$, $m_A(t)=p_A(t)$, and rank one. The kernel is $\mathbb{C}e_2$ and the image is $\mathbb{C}e_1$. The Moore–Penrose inverse is $\operatorname{diag}(\tfrac12,0)$, and the polar factor is $V=\operatorname{diag}(1,0)$, a partial isometry.

**Regular model.** $X=\operatorname{diag}(A,A)$ has $\operatorname{Tr}X=4$, $\det X=0$, rank two, kernel $\mathbb{C}e_2\oplus\mathbb{C}e_4$ and image $\mathbb{C}e_1\oplus\mathbb{C}e_3$.

**Reading.** The matrix is Hermitian, normal and a scaled projector. It is singular, so its polar factor is only a partial isometry. It is not $*$-unitary.

## The Rank-One Matrix

**Entry model.** $A=\begin{pmatrix}1&2\\3&6\end{pmatrix}=uv^{\mathsf T}$ with $u=(1,3)^{\mathsf T}$ and $v=(1,2)^{\mathsf T}$. Then $\tau=7$, $\delta=0$, $v^{\mathsf T}u=7$, and
$$
P=\frac{A}{7}
$$
is the rank-one idempotent with image $\mathbb{C}u$ and kernel $\ker v^{\mathsf T}$. The two strata: the matrix is non-pure because $v^{\mathsf T}u\neq0$.

**Regular model.** $X=\operatorname{diag}(A,A)$ has $\operatorname{Tr}X=14$, rank two, and is the double of the idempotent up to scale. Its image is $\mathbb{C}u\oplus\mathbb{C}u$ and its kernel is the complementary plane.

**Reading.** The matrix is diagonalisable, not normal, and not Hermitian. It differs from the singular example exactly by the normality flag: the singular example is a scaled Hermitian projector, the rank-one example a scaled non-Hermitian idempotent.

## The $*$-Unitary Matrix

**Entry model.** $A=\tfrac1{\sqrt2}\begin{pmatrix}1&i\\i&1\end{pmatrix}$ has $A^{\dagger}A=\mathrm I_2$, $\tau=\sqrt2$, $\delta=1$, and
$$
p_A(t)=t^2-\sqrt2\,t+1,\qquad
\lambda_\pm=e^{\pm i\pi/4}.
$$
The eigenvalues have modulus one. The matrix lies in $SU(2)$.

**Regular model.** $X=\operatorname{diag}(A,A)$ has $\operatorname{Tr}X=2\sqrt2$, $\det X=1$, the same minimal polynomial, and each eigenvalue twice. It is $*$-unitary.

**Reading.** The matrix is normal and not Hermitian. Its polar decomposition is $P=\mathrm I_2$ and $V=A$.

## The Hermitian Matrix

**Entry model.** $A=\begin{pmatrix}2&1-i\\1+i&-1\end{pmatrix}$ has $A=A^{\dagger}$, $\tau=1$, $\delta=-4$, and
$$
p_A(t)=t^2-t-4,\qquad
\lambda_\pm=\frac{1\pm\sqrt{17}}{2}.
$$
The eigenvalues are real and distinct, the spectral projectors are Hermitian, and the eigenbasis is orthonormal.

**Regular model.** $X=\operatorname{diag}(A,A)$ has $\operatorname{Tr}X=2$, $\det X=16$, the same minimal polynomial, and each eigenvalue twice. It is Hermitian of rank four.

**Reading.** The matrix is Hermitian and normal. Its polar factor is $P=\lvert A\rvert$ and its unitary factor is the sign of $A$.

## The Normal Matrix

**Entry model.** $A=\begin{pmatrix}1&1\\-1&1\end{pmatrix}$ has $AA^{\dagger}=A^{\dagger}A$, $\tau=2$, $\delta=2$, and
$$
p_A(t)=t^2-2t+2,\qquad
\lambda_\pm=1\pm i .
$$
The spectral projectors are Hermitian, but the matrix is neither Hermitian nor $*$-unitary. It is $\sqrt2$ times a matrix in $SU(2)$.

**Regular model.** $X=\operatorname{diag}(A,A)$ has $\operatorname{Tr}X=4$, $\det X=4$, the same minimal polynomial, and each eigenvalue twice.

**Reading.** The matrix is the example that separates normality from the two stronger flags. Its polar decomposition is $P=\sqrt2\,\mathrm I_2$ and $V=A/\sqrt2\in SU(2)$.

## The Pattern

| Case | $m_A(t)$ | Rank $A$ / $X$ | Diagonalisable | Normal | Hermitian | $*$-Unitary |
|---|---|---|---|---|---|---|
| Scalar | $t-2$ | $2$ / $4$ | yes | yes | yes | no |
| Jordan | $(t-1)^2$ | $2$ / $4$ | no | no | no | no |
| Distinct | $t^2-5t-2$ | $2$ / $4$ | yes | no | no | no |
| Singular | $t(t-2)$ | $1$ / $2$ | yes | yes | yes | no |
| Rank one | $t(t-7)$ | $1$ / $2$ | yes | no | no | no |
| $*$-Unitary | $t^2-\sqrt2\,t+1$ | $2$ / $4$ | yes | yes | no | yes |
| Hermitian | $t^2-t-4$ | $2$ / $4$ | yes | yes | yes | no |
| Normal | $t^2-2t+2$ | $2$ / $4$ | yes | yes | no | no |

**The implications.** Hermitian implies normal, and $*$-unitary implies normal; the converses fail in both directions. A normal matrix with a repeated eigenvalue is scalar: the only normal matrix among the three Jordan types is the scalar. A non-scalar Jordan block is never normal.

**The spectral reading.** For a normal matrix the spectral projectors are Hermitian and the eigenbasis is orthonormal; for a non-normal matrix with distinct eigenvalues the Lagrange formula gives idempotents that are not Hermitian. The distinct-spectrum example and the rank-one example are the two non-normal diagonalisable cases; the Jordan block is the non-diagonalisable case.

**The rank reading.** The singular example and the rank-one example both have determinant zero. The first is a Hermitian projector up to scale, the second a non-Hermitian idempotent up to scale. The difference is the normality flag.

**The group reading.** The $*$-unitary example lies in $SU(2)$; the normal example is $\sqrt2$ times an element of $SU(2)$; the Jordan block lies in $SL_2(\mathbb{C})$; the distinct-spectrum matrix has determinant $-2$ and is not in $SL_2$. The scalar is central.

**The doubling in one line.** The regular column has the doubled trace, the squared determinant, the doubled rank and each eigenvalue twice; the minimal polynomial and the flags are unchanged.

## Summary

The eight matrices cover the three spectral types and the three normality flags. The scalar has minimal polynomial of degree one; the Jordan block is the only non-diagonalisable case and the only non-normal case with a repeated eigenvalue; the distinct-spectrum, singular, rank-one, $*$-unitary, Hermitian and normal matrices are diagonalisable, and among them the rank-one and distinct-spectrum examples are not normal. The singular example is a scaled Hermitian projector and the rank-one example a scaled non-Hermitian idempotent, so the two singular cases differ exactly by the normality flag. In the regular model every trace, determinant, rank and eigenvalue multiplicity is doubled, and the minimal polynomial and the flags are read blockwise.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$ | the entry-model matrix |
| $X=\operatorname{diag}(A,A)$ | the regular matrix |
| $\tau,\delta$ | trace and determinant of $A$ |
| $p_A,m_A$ | characteristic and minimal polynomials |
| $\Pi_\pm$ | the spectral projectors |
| $P,V$ | the polar factors |
| $p_A(t)=t^2-5t-2$ etc. | the eight characteristic polynomials |

## Further Reading

- [Matrix Representations : The Models and the Change of Frame](matrix-representations-the-models-and-the-change-of-frame.html), for the displays
- [Matrix Representations : The Eigenbasis and the Diagonalising Matrix](matrix-representations-the-eigenbasis-and-the-diagonalising-matrix.html), for the distinct case
- [Matrix Representations : The Jordan Basis and the Jordanising Matrix](matrix-representations-the-jordan-basis-and-the-jordanising-matrix.html), for the Jordan case
- [Matrix Representations : The Polar Decomposition of a Matrix](matrix-representations-the-polar-decomposition-of-a-matrix.html), for the polar factors
- [Matrix Representations : Rank-One Matrices and the Determinantal Variety](matrix-representations-rank-one-matrices-and-the-determinantal-variety.html), for the rank-one case
- [$M_2(\mathbb{C})$ Representation : Worked Examples](m2c-representation-worked-examples.html), for the full entry-model computations
- [$M_4(\mathbb{C})$ Representation : Worked Examples](m4c-representation-worked-examples.html), for the full regular computations
