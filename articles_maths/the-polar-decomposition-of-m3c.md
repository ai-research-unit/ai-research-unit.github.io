# __The Polar Decomposition of $M_3(\mathbb{C})$__

## Introduction

**Every matrix $A\in M_3(\mathbb{C})$ factors as $A=UP$, with $U$ $*$-unitary and $P$ positive semidefinite Hermitian; the factor $P$ is unique, and $U$ is unique when $A$ is invertible.** The factor is

$$
P=(A^{*}A)^{1/2}=|A|,\qquad U=AP^{-1}\ \text{on }(\ker A)^{\perp},
$$

and $U$ is a partial isometry in general, $*$-unitary exactly when $\ker A=0$. On the invertible matrices the polar decomposition is a diffeomorphism

$$
U(3)\times\operatorname{Herm}_{>0}(3)\longrightarrow GL_3(\mathbb{C}),
\qquad (U,P)\longmapsto UP,
$$

and the real dimensions match: $9+9=18$. The positive definite factor is the exponential of a Hermitian matrix, $P=e^{H}$, and the $*$-unitary factor is the exponential of a skew-Hermitian matrix, $U=e^{iK}$, so the polar decomposition is the real splitting

$$
\mathfrak{gl}_3=\mathfrak{u}(3)\oplus\operatorname{Herm}(3),
\qquad
X=\tfrac12(X-X^{*})+\tfrac12(X+X^{*}).
$$

The article proves the existence and uniqueness, identifies the factors with the singular value decomposition, works an explicit example with exact numbers, treats the singular and the idempotent cases, and explains the manifold structure. The singular values are the eigenvalues of $P$; the singular set is $\det A=0$, of real codimension $2$, and there is no null cone. The Hermitian structure is *The Involution and the Hermitian Structure of $M_3(\mathbb{C})$*; the exponential is *The Exponential and the Lie Group of $M_3(\mathbb{C})$*; the combined exponential polar form is *The Exponential Polar Decomposition of $M_3(\mathbb{C})$*; the topology is *The Topology of $M_3(\mathbb{C})$*.

## The Statement

**Theorem (polar decomposition).** For every $A\in M_3(\mathbb{C})$ there are a $*$-unitary $U$ and a positive semidefinite Hermitian $P$ with

$$
A=UP.
$$

The factor $P$ is unique, $P=|A|=(A^{*}A)^{1/2}$. If $A$ is invertible then $U$ is unique and $*$-unitary. If $A$ is singular, $U$ is determined on $(\ker A)^{\perp}$ and arbitrary $*$-unitary on $\ker A$.

**Proof of existence.** The matrix $A^{*}A$ is Hermitian and positive semidefinite, because $\langle v,A^{*}Av\rangle=\|Av\|^{2}\ge0$. A positive semidefinite Hermitian matrix has a unique positive semidefinite square root: diagonalise $A^{*}A=V\Lambda V^{*}$ with $\Lambda=\operatorname{diag}(\sigma_1^{2},\sigma_2^{2},\sigma_3^{2})$, $\sigma_i\ge0$, and set

$$
P=V\operatorname{diag}(\sigma_1,\sigma_2,\sigma_3)V^{*}.
$$

Then $P^{2}=A^{*}A$. On the range of $P$, which is the orthogonal complement of $\ker A$, define $U(Pa)=Aa$; this is well defined because $\|Pa\|^{2}=\langle Pa,Pa\rangle=\langle a,A^{*}Aa\rangle=\|Aa\|^{2}$, so $Pa=0$ implies $Aa=0$. The map $U$ is an isometry from $\operatorname{im}P$ onto $\operatorname{im}A$, and it extends to a $*$-unitary of $\mathbb{C}^{3}$ by choosing an isometry from $\ker P=\ker A$ onto $(\operatorname{im}A)^{\perp}$. Then $UP=A$.

**Proof of uniqueness.** If $A=UP$ with $U$ $*$-unitary and $P\ge0$, then $A^{*}A=P U^{*}UP=P^{2}$, so $P$ is the positive semidefinite square root of $A^{*}A$, which is unique. If $A$ is invertible, $P$ is invertible, and $U=AP^{-1}$ is determined. If $A$ is singular, $U$ is determined on $\operatorname{im}P=(\ker A)^{\perp}$ and arbitrary on $\ker A$.

**The right polar form.** Since $A=UP$ and $U$ is $*$-unitary, also

$$
A=(UPU^{*})U,
$$

with $UPU^{*}$ positive semidefinite. So every matrix has a right polar decomposition $A=P'U$ with $P'=UPU^{*}$; the two forms carry the same information.

**The singular value decomposition.** Diagonalise $A$ by two unitaries:

$$
A=W\Sigma V^{*},\qquad
\Sigma=\operatorname{diag}(\sigma_1,\sigma_2,\sigma_3),\quad \sigma_1\ge\sigma_2\ge\sigma_3\ge0 .
$$

Then

$$
P=V\Sigma V^{*},\qquad U=WV^{*}.
$$

**Proof.** $A^{*}A=V\Sigma^{2}V^{*}$, so $P=V\Sigma V^{*}$; then $UP=WV^{*}V\Sigma V^{*}=W\Sigma V^{*}=A$. The columns of $V$ are the right singular vectors, the columns of $W$ the left singular vectors, and the $\sigma_i$ the singular values.

**The $*$-unitary group.** The group $U(3)$ consists of the matrices with $U^{*}U=I$; it is a real Lie group of dimension $9$. The Hermitian matrices form a real vector space of dimension $9$, and the positive definite ones form an open convex cone in it. The polar decomposition says that the multiplication map

$$
U(3)\times\operatorname{Herm}_{>0}(3)\to GL_3(\mathbb{C})
$$

is a bijection; it is a diffeomorphism because the inverse $A\mapsto(A(A^{*}A)^{-1/2},(A^{*}A)^{1/2})$ is smooth.

## The Real Geometry

**The dimensions.** Over $\mathbb{R}$,

$$
\dim_\mathbb{R}GL_3(\mathbb{C})=18,\qquad
\dim_\mathbb{R}U(3)=9,\qquad
\dim_\mathbb{R}\operatorname{Herm}(3)=9 .
$$

The polar decomposition is the real diffeomorphism $GL_3\cong U(3)\times\mathbb{R}^{9}$, because $\operatorname{Herm}_{>0}(3)\cong\mathbb{R}^{9}$ via the matrix logarithm. It is not a complex diffeomorphism: $U(3)$ is not a complex subgroup of $GL_3(\mathbb{C})$, and the splitting $\mathfrak{gl}_3=\mathfrak{u}(3)\oplus\operatorname{Herm}(3)$ is a real splitting, not a complex one.

**Proof of the dimension count.** A $*$-unitary matrix has $9$ real parameters: three diagonal phases and three independent complex off-diagonal entries, $3+3\cdot2=9$. A Hermitian matrix has three real diagonal entries and three independent complex off-diagonal entries, $3+3\cdot2=9$. The product is $18$, the real dimension of $GL_3(\mathbb{C})$.

**The exponential form.** Every positive definite $P$ is $e^{H}$ for a unique Hermitian $H=\log P$, and every $*$-unitary $U$ is $e^{iK}$ for a Hermitian $K$ defined modulo the spectral lattice. Hence every invertible $A$ has

$$
A=e^{iK}e^{H},\qquad K=K^{*},\quad H=H^{*},
$$

the **polar exponential form**. The real tangent space at the identity splits as the skew-Hermitian part and the Hermitian part:

$$
\mathfrak{gl}_3=\mathfrak{u}(3)\oplus\operatorname{Herm}(3),\qquad
X=\tfrac12(X-X^{*})+\tfrac12(X+X^{*}).
$$

The first summand is the Lie algebra of $U(3)$, the second is the tangent space of the positive definite cone.

**The metric.** With the real part of the trace form, $\operatorname{Re}\operatorname{tr}(X^{*}Y)$, the two summands are orthogonal. For skew-Hermitian $S$ and Hermitian $H$,

$$
\operatorname{tr}(S^{*}H)=-\operatorname{tr}(SH),
\qquad
\operatorname{tr}(SH)=\operatorname{tr}((SH)^{\mathsf T})
=\operatorname{tr}(H^{\mathsf T}S^{\mathsf T})
=-\operatorname{tr}(\bar H\bar S)
=-\overline{\operatorname{tr}(HS)}
=-\overline{\operatorname{tr}(SH)} .
$$

The fourth equality uses that the transpose does not change the trace and that $H$ and $S$ are Hermitian and skew-Hermitian, so $H^{\mathsf T}=\bar H$ and $S^{\mathsf T}=-\bar S$. Hence $\operatorname{tr}(SH)$ is purely imaginary, $\operatorname{tr}(S^{*}H)$ is purely imaginary, and the real part of the trace form vanishes on the pair. The real part is the Riemannian metric and the imaginary part is the symplectic form.

**The singular set.** The map $A\mapsto P=|A|$ is continuous everywhere and smooth away from $\det A=0$. On the singular set the rank drops and the $*$-unitary factor is not unique: the fibre over a matrix of rank $r$ is the $*$-unitary group of the kernel, of real dimension $(3-r)^{2}$. For $r=2$ the fibre is $U(1)$, of dimension $1$; for $r=1$ it is $U(2)$, of dimension $4$; for $r=0$ it is $U(3)$, of dimension $9$.

**Proof.** If $A=UP$ and $A$ has rank $r$, then $P$ has rank $r$ and $\ker P=\ker A$ has dimension $3-r$. The equation $A=U'P$ holds exactly when $U'=U$ on $\operatorname{im}P$ and $U'$ is any $*$-unitary on $\ker P$; the freedom is $U(3-r)$, of real dimension $(3-r)^{2}$.

## Worked Example

Take

$$
A=\begin{pmatrix}1&2&0\\0&1&0\\0&0&3\end{pmatrix}.
$$

Then

$$
A^{*}A=\begin{pmatrix}1&2&0\\2&5&0\\0&0&9\end{pmatrix}
=\begin{pmatrix}1&2\\2&5\end{pmatrix}\oplus(9).
$$

The $2\times2$ block has trace $6$ and determinant $1$, so its eigenvalues are $3\pm2\sqrt{2}=(\sqrt{2}\pm1)^{2}$. Its positive square root is

$$
P_{2}=\frac{A^{*}A_{2}+I}{2\sqrt{2}}
=\frac{1}{\sqrt2}\begin{pmatrix}1&1\\1&3\end{pmatrix},
$$

because $\big(\frac{1}{\sqrt2}\begin{pmatrix}1&1\\1&3\end{pmatrix}\big)^{2}=\begin{pmatrix}1&2\\2&5\end{pmatrix}$. Hence

$$
P=|A|=\begin{pmatrix}\tfrac{1}{\sqrt2}&\tfrac{1}{\sqrt2}&0\\ \tfrac{1}{\sqrt2}&\tfrac{3}{\sqrt2}&0\\ 0&0&3\end{pmatrix},
\qquad
P^{-1}=\begin{pmatrix}\tfrac{3}{\sqrt2}&-\tfrac{1}{\sqrt2}&0\\ -\tfrac{1}{\sqrt2}&\tfrac{1}{\sqrt2}&0\\ 0&0&\tfrac13\end{pmatrix}.
$$

Then

$$
U=AP^{-1}
=\begin{pmatrix}\tfrac{1}{\sqrt2}&\tfrac{1}{\sqrt2}&0\\ -\tfrac{1}{\sqrt2}&\tfrac{1}{\sqrt2}&0\\ 0&0&1\end{pmatrix}.
$$

**Checks.** The matrix $U$ is $*$-unitary: its first two columns are orthonormal and the third is orthogonal to them, and $U^{*}U=I$. The product is

$$
UP=\begin{pmatrix}1&2&0\\0&1&0\\0&0&3\end{pmatrix}=A .
$$

The singular values are the eigenvalues of $P$, namely

$$
\sigma_1=1+\sqrt2,\qquad \sigma_2=\sqrt2-1,\qquad \sigma_3=3,
$$

and $\det P=(1+\sqrt2)(\sqrt2-1)\cdot3=3=\det A$. The $*$-unitary factor has $\det U=1$; the rotation is by $-\pi/4$ in the first two coordinates, followed by the identity on the third.

**The right polar form.** The factor $P'=UPU^{*}$ is positive definite with the same eigenvalues as $P$. In this example the rotation does not commute with $P$, and

$$
P'=UPU^{*}=\frac{1}{\sqrt2}\begin{pmatrix}3&1&0\\1&1&0\\0&0&3\sqrt2\end{pmatrix},
$$

so that $A=P'U$. The two polar forms carry the same positive spectrum and differ by the $*$-unitary conjugation.

## The Singular Case

**Example.** Take

$$
A=\operatorname{diag}(1,2,0).
$$

Then $A^{*}A=A^{2}=\operatorname{diag}(1,4,0)$, so

$$
P=\operatorname{diag}(1,2,0),\qquad
U=\begin{pmatrix}1&0&0\\0&1&0\\0&0&u\end{pmatrix},
$$

with $|u|=1$. Every $u$ on the unit circle gives a polar decomposition, because the third coordinate of $P$ is zero and the third column of $U$ never appears in $UP$. The fibre is $U(1)$, of real dimension $1=(3-2)^{2}$.

**The general fibre.** For $A$ of rank $r$, the positive factor has rank $r$ and kernel of dimension $3-r$. The $*$-unitary factor is fixed on $(\ker A)^{\perp}$ and arbitrary on the kernel, so the fibre is $U(3-r)$, of real dimension $(3-r)^{2}$. The factor $P$ is always unique, even when $U$ is not.

**The partial isometry.** When $A$ is singular, the operator $U$ defined by $U(Pa)=Aa$ is an isometry from $\operatorname{im}P$ onto $\operatorname{im}A$ and zero on $\ker A$; it is a **partial isometry**, with $U^{*}U$ the orthogonal projector onto $(\ker A)^{\perp}$ and $UU^{*}$ the orthogonal projector onto $\operatorname{im}A$. It is $*$-unitary exactly when both projections are the identity, that is, when $A$ is invertible.

## The Idempotent Case

**The polar of an idempotent.** Let $E\in M_3$ satisfy $E^{2}=E$, $E\neq0$. Then

$$
E=UP,\qquad
P=(E^{*}E)^{1/2},\qquad
U=EP^{-1}\ \text{on }\operatorname{im}E .
$$

For a rank-one idempotent $E=u\varphi$ with $\varphi(u)=1$,

$$
E^{*}E=\|u\|^{2}\,\varphi^{*}\varphi,
\qquad
P=\|u\|\,\frac{\varphi^{*}\varphi}{\|\varphi\|},
\qquad
U=\frac{u\varphi}{\|u\|\,\|\varphi\|}.
$$

**Proof.** The computation $E^{*}E=\varphi^{*}u^{*}u\varphi=\|u\|^{2}\varphi^{*}\varphi$ uses that $u^{*}u=\|u\|^{2}$ is a scalar. The matrix $\varphi^{*}\varphi$ is rank one with trace $\|\varphi\|^{2}$, so its positive square root is $\varphi^{*}\varphi/\|\varphi\|$. The $*$-unitary factor follows by multiplying $u\varphi$ by the inverse of $P$ on the range: $P^{-1}=\varphi^{*}\varphi/(\|u\|\,\|\varphi\|^{3})$ there, and $u\varphi\,\varphi^{*}\varphi=u\|\varphi\|^{2}\varphi$.

**The meaning.** The positive factor of an idempotent measures the angle between the line and the functional. Since $\varphi(u)=1$, the product of the norms is $\|u\|\,\|\varphi\|=1/\cos\theta$, and

$$
P=\|u\|\,\|\varphi\|\,\frac{\varphi^{*}\varphi}{\|\varphi\|^{2}}
$$

is the norm ratio times the orthogonal projection onto the row line $\mathbb{C}\varphi^{*}$. The $*$-unitary factor is the partial isometry that identifies the row line with the image line $\mathbb{C}u$; it is $*$-unitary only when the idempotent is an orthogonal projection, that is, when $\theta=0$.

**Example.** For $E=\begin{pmatrix}1&1&0\\0&0&0\\0&0&0\end{pmatrix}=e_{1}(e_{1}+e_{2})^{\mathsf T}$, one has $u=e_{1}$, $\varphi=e_{1}^{\mathsf T}+e_{2}^{\mathsf T}$, $\|u\|=1$, $\|\varphi\|=\sqrt2$, and

$$
P=\frac{1}{\sqrt2}\begin{pmatrix}1&1&0\\1&1&0\\0&0&0\end{pmatrix},
\qquad
U=\frac{1}{\sqrt2}\begin{pmatrix}1&1&0\\0&0&0\\0&0&0\end{pmatrix}.
$$

Then $UP=E$ and $U$ has singular values $1$ on the range and $0$ on the kernel.

## The Root and the Frame

**A root is $*$-unitary exactly when it is normal.** A root $H$ with $H^{3}=I$ and simple spectrum is diagonalisable, $H=\sum_k\zeta_kP_k$, with spectral projectors $P_k$. It satisfies $H^{*}H=I$ exactly when the projectors are Hermitian, equivalently when $H$ is normal. For the standard root $H_0=\operatorname{diag}(1,\omega,\omega^{2})$ and the cyclic permutation root, the projectors are Hermitian and

$$
H=H\cdot I,\qquad U=H,\quad P=I .
$$

For a non-normal root the positive factor $P=(H^{*}H)^{1/2}$ is not the identity.

**An oblique root.** The matrix

$$
H=\begin{pmatrix}1&1&0\\0&\omega&0\\0&0&\omega^{2}\end{pmatrix}
$$

satisfies $H^{3}=I$ and has simple spectrum. It is not normal: on the first two coordinates

$$
H^{*}H=\begin{pmatrix}1&1\\1&2\end{pmatrix},
\qquad
HH^{*}=\begin{pmatrix}2&\omega^{2}\\ \omega&1\end{pmatrix},
$$

so $H^{*}H\neq HH^{*}$. The polar factor is the positive square root of $\operatorname{diag}\big(\begin{pmatrix}1&1\\1&2\end{pmatrix},1\big)$, whose eigenvalues $\sqrt{(3\pm\sqrt5)/2}$ are not all $1$; the root is not $*$-unitary.

**The spectral projectors.** The projectors $P_k$ of a general root are oblique idempotents; their polar decompositions are computed by the formula of the previous section.

**The frame.** For a general frame $S\in GL_3$, the polar decomposition separates the $*$-unitary change of frame from the positive stretching:

$$
S=UP,\qquad U\in U(3),\quad P\in\operatorname{Herm}_{>0}(3).
$$

The gauge torus $T$ acts on the frame by $S\mapsto ST$, and the two factors of the polar decomposition do not transform separately: the polar decomposition of $ST$ is the polar decomposition of $PT$, which mixes the positive factor and the $*$-unitary factor unless $T$ is $*$-unitary. The gauge is not a polar factor.

**The Cartan decomposition.** The decomposition $GL_3(\mathbb{C})=U(3)\cdot\exp(\operatorname{Herm}(3))$ is the Cartan decomposition of the real group $GL_3(\mathbb{C})$ with respect to the involution $\theta(X)=-X^{*}$. The fixed subgroup is $U(3)$, the $-1$ eigenspace is $\operatorname{Herm}(3)$, and the symmetric space $GL_3/U(3)\cong\operatorname{Herm}_{>0}(3)$ is the space of positive definite Hermitian matrices, of real dimension $9$ and rank $3$.

**Proof.** The involution $\theta(X)=-X^{*}$ is an automorphism of the real Lie algebra $\mathfrak{gl}_3$: it preserves the bracket because $\theta([X,Y])=-[X,Y]^{*}=[-X^{*},-Y^{*}]=[\theta X,\theta Y]$. Its fixed set is $\{X:X=-X^{*}\}=\mathfrak{u}(3)$, and its $-1$ eigenspace is $\{X:X=X^{*}\}=\operatorname{Herm}(3)$. The Cartan decomposition theorem then gives the global decomposition for the connected group $GL_3(\mathbb{C})$.

## Summary

Every $A\in M_3(\mathbb{C})$ has a polar decomposition $A=UP$, with $P=|A|=(A^{*}A)^{1/2}$ positive semidefinite and unique, and $U$ $*$-unitary when $A$ is invertible, a partial isometry in general. The factors are read from the singular value decomposition $A=W\Sigma V^{*}$: $P=V\Sigma V^{*}$ and $U=WV^{*}$. On $GL_3(\mathbb{C})$ the map $(U,P)\mapsto UP$ is a diffeomorphism $U(3)\times\operatorname{Herm}_{>0}(3)\to GL_3(\mathbb{C})$, and the real dimensions match, $9+9=18$. The decomposition is the Cartan decomposition of $GL_3(\mathbb{C})$ as a real group for the involution $\theta(X)=-X^{*}$, and the symmetric space is the positive definite cone $\operatorname{Herm}_{>0}(3)\cong\mathbb{R}^{9}$, of rank $3$. On the singular set the factor $P$ stays unique and the $*$-unitary factor is free on the kernel: the fibre over a matrix of rank $r$ is $U(3-r)$, of real dimension $(3-r)^{2}$. For a rank-one idempotent $E=u\varphi$ the polar factors are $P=\|u\|\,\varphi^{*}\varphi/\|\varphi\|$ and $U=u\varphi/(\|u\|\,\|\varphi\|)$.

$$
\boxed{\ A=UP,\quad P=(A^{*}A)^{1/2},\quad U=AP^{-1};\qquad GL_3(\mathbb{C})\cong U(3)\times\operatorname{Herm}_{>0}(3),\quad 18=9+9.\ }
$$

| Object | Real dimension | Description |
|---|---|---|
| $GL_3(\mathbb{C})$ | $18$ | invertible matrices |
| $U(3)$ | $9$ | $*$-unitary group |
| $\operatorname{Herm}(3)$ | $9$ | Hermitian matrices |
| $\operatorname{Herm}_{>0}(3)$ | $9$ | positive definite cone |
| fibre over rank $r$ | $(3-r)^{2}$ | $U(3-r)$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A^{*}$ | conjugate transpose |
| $P=|A|$ | positive semidefinite factor $(A^{*}A)^{1/2}$ |
| $U$ | $*$-unitary or partial isometry factor |
| $\sigma_i$ | singular values, eigenvalues of $P$ |
| $\operatorname{Herm}(3)$ | real space of Hermitian matrices |
| $\operatorname{Herm}_{>0}(3)$ | positive definite Hermitian matrices |
| $\theta(X)=-X^{*}$ | Cartan involution |

## Further Reading

- Rajendra Bhatia, *Matrix Analysis* (Springer, 1997), for the polar decomposition, the singular value decomposition and the positive square root.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the $*$-unitary group and the singular value decomposition.
- Sigurdur Helgason, *Differential Geometry, Lie Groups and Symmetric Spaces* (AMS, 2001), for the Cartan decomposition and the symmetric space $GL_3/U(3)$.
- [The Involution and the Hermitian Structure of $M_3(\mathbb{C})$](the-involution-and-the-hermitian-structure-of-m3c.html), for the star and the positive cone.
- [The Exponential and the Lie Group of $M_3(\mathbb{C})$](the-exponential-and-the-lie-group-of-m3c.html), for $P=e^{H}$ and $U=e^{iK}$.
- [The Exponential Polar Decomposition of $M_3(\mathbb{C})$](the-exponential-polar-decomposition-of-m3c.html), for the combined form.
- [The Topology of $M_3(\mathbb{C})$](the-topology-of-m3c.html), for the homotopy type of $GL_3$ and $U(3)$.
