# __The Exponential and the Lie Group of $M_6(\mathbb{C})$__

## Introduction

The exponential of a matrix is the power series

$$
e^X=\sum_{n=0}^{\infty}\frac{X^n}{n!},
$$

which converges for every $X\in M_6(\mathbb{C})$ and defines a holomorphic map

$$
\exp:M_6(\mathbb{C})\longrightarrow GL_6(\mathbb{C}).
$$

The map is surjective: every invertible matrix has a logarithm. The one-parameter subgroups are the curves $t\mapsto e^{tX}$, and the Lie algebra $\mathfrak{gl}_6=M_6(\mathbb{C})$ has real dimension $72$; the compact real form $\mathfrak{su}(6)$ has dimension $35$. The closed form of the exponential is the Jordan form

$$
e^{PJP^{-1}}=Pe^JP^{-1},
\qquad
e^{\lambda I+N}=e^\lambda\sum_{k=0}^{m-1}\frac{N^k}{k!},
$$

and the eigenvalues of $e^X$ are $e^{\lambda_1},\dots,e^{\lambda_6}$.

The article assumes the Jordan form of *The Element, the Coordinates and the Trace of $M_6(\mathbb{C})$* and the $*$-unitary group of *The Involution and the Hermitian Structure of $M_6(\mathbb{C})$*. It uses the holomorphic functional calculus of *Spectral Theory and the Spectral Projectors of $M_6(\mathbb{C})$*. The polar decomposition is *The Polar Decomposition of $M_6(\mathbb{C})$*; the topology of the group is *The Topology of $M_6(\mathbb{C})$*.

## The Exponential

### Definition

**Definition.** For $X\in M_6(\mathbb{C})$,

$$
e^X=\sum_{n=0}^{\infty}\frac{X^n}{n!}.
$$

**Theorem.** The series converges absolutely and uniformly on compact subsets of $M_6(\mathbb{C})$; the map $\exp$ is holomorphic; and

$$
e^0=I_6,\qquad
e^{X+Y}=e^Xe^Y\ \text{if }XY=YX,\qquad
(e^X)^{-1}=e^{-X}.
$$

**Proof.** $\lVert X^n\rVert\le\lVert X\rVert^n$, so the series is dominated by $e^{\lVert X\rVert}$; the product formula follows from the binomial theorem when $X$ and $Y$ commute; the inverse is $e^{-X}$.

**Theorem (the determinant and the eigenvalues).** For every $X$,

$$
\det e^X=e^{\operatorname{tr}X},
\qquad
\sigma(e^X)=e^{\sigma(X)}=\{e^{\lambda_1},\dots,e^{\lambda_6}\}.
$$

**Proof.** In the Jordan form, $X=PJP^{-1}$ and $e^X=Pe^JP^{-1}$; the eigenvalues of $e^J$ are $e^{\lambda_i}$ with the same multiplicities; the determinant is the product, $e^{\sum\lambda_i}=e^{\operatorname{tr}X}$.

**Corollary (the image).** The image of $\exp$ is contained in $GL_6(\mathbb{C})$, and it is contained in the open set of matrices with nonzero determinant.

**Proof.** $e^X$ has inverse $e^{-X}$; the determinant is $e^{\operatorname{tr}X}\neq0$.

### The Derivative

**Theorem.** The derivative of $\exp$ at $X$ is

$$
d(\exp)_X(Y)=\int_0^1e^{sX}Ye^{(1-s)X}\,ds
=\sum_{n=0}^{\infty}\frac{1}{(n+1)!}\sum_{j=0}^{n}X^jYX^{n-j}.
$$

**Proof.** Differentiate the power series term by term:

$$
\frac{d}{dt}e^{X+tY}\Big|_{t=0}
=\sum_{n=1}^{\infty}\frac{1}{n!}\sum_{j=0}^{n-1}X^jYX^{n-1-j}
=\int_0^1e^{sX}Ye^{(1-s)X}ds .
$$

**Corollary (the local diffeomorphism).** $d(\exp)_0=I_6$, so $\exp$ is a local diffeomorphism from a neighborhood of $0$ onto a neighborhood of $I_6$.

**Proof.** The derivative at $0$ is $Y\mapsto\int_0^1Yds=Y$; the inverse function theorem.

**Remark (the derivative formula).** The derivative can be written

$$
d(\exp)_X=\frac{1-e^{-\operatorname{ad}_X}}{\operatorname{ad}_X}e^X
=e^X\frac{1-e^{-\operatorname{ad}_X}}{\operatorname{ad}_X},
$$

where the fraction is the power series $\sum_{k\ge0}(-\operatorname{ad}_X)^k/(k+1)!$. The formula is the closed form of the derivative; it is singular exactly when $\operatorname{ad}_X$ has an eigenvalue in $2\pi\mathrm i\mathbb{Z}\setminus\{0\}$.

**Proof.** Expand the integral and use $\operatorname{ad}_X^k(Y)$; the series is the standard formula for the derivative of the exponential.

### The Logarithm

**Theorem (the logarithm near the identity).** For $\lVert N\rVert<1$,

$$
\log(I_6+N)=\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}N^n,
$$

and

$$
e^{\log(I_6+N)}=I_6+N .
$$

**Proof.** The series converges for $\lVert N\rVert<1$; the identity $e^{\log(1+z)}=1+z$ for $|z|<1$ extends to commuting matrices, and $N$ commutes with its powers.

**Theorem (the principal logarithm).** If $A\in GL_6(\mathbb{C})$ has no eigenvalue on the negative real axis, then there is a unique logarithm $X$ with spectrum in the strip $\lvert\operatorname{Im}z\rvert<\pi$; it is

$$
X=\log A,
$$

defined by the Dunford calculus with the principal branch of the logarithm.

**Proof.** The principal logarithm is holomorphic on $\mathbb{C}\setminus(-\infty,0]$; the Dunford calculus applies; the spectral mapping gives $e^{\log A}=A$; the spectrum condition fixes the branch.

**Corollary (the branch ambiguity).** The logarithm is not unique. For a diagonalizable $A$ with distinct eigenvalues $\lambda_i$, the logarithms are

$$
X_0+2\pi\mathrm i\,\operatorname{diag}(k_1,\dots,k_6)
$$

in an eigenbasis, with $k_i\in\mathbb{Z}$. For a general $A$, the choices of the branches of $\log\lambda_i$ in the Jordan construction give different logarithms.

**Proof.** In an eigenbasis, $e^X=A$ forces $X$ to preserve each eigenspace and to have eigenvalues $\log\lambda_i+2\pi\mathrm i k_i$. The Jordan construction gives one logarithm for each choice of branch.

## The Surjectivity

**Theorem.** The exponential map

$$
\exp:M_6(\mathbb{C})\longrightarrow GL_6(\mathbb{C})
$$

is surjective.

**Proof.** Let $A\in GL_6(\mathbb{C})$ and let $A=PJP^{-1}$ be its Jordan form, with blocks $J_m(\lambda)=\lambda I+N$, $\lambda\neq0$. For each block,

$$
J_m(\lambda)=\lambda\left(I+\frac{N}{\lambda}\right),
\qquad
\log J_m(\lambda)=(\log\lambda)I+\log\left(I+\frac{N}{\lambda}\right),
$$

where the logarithm of $I+N/\lambda$ is the finite polynomial $\sum_{k=1}^{m-1}(-1)^{k+1}(N/\lambda)^k/k$ because $N$ is nilpotent. Then

$$
X=P\left(\bigoplus\log J_m(\lambda)\right)P^{-1}
$$

satisfies $e^X=A$. The choice of $\log\lambda$ is arbitrary; different choices give different logarithms.

**Corollary (the real case).** The real exponential $\exp:M_6(\mathbb{R})\to GL_6(\mathbb{R})$ is not surjective: every image has positive determinant, so a real matrix with negative determinant is not in the image.

**Proof.** $\det e^X=e^{\operatorname{tr}X}>0$ for real $X$.

**Corollary (the fibres).** The fibre of $\exp$ over $A$ is the set of logarithms of $A$; it is nonempty, and it is a union of components indexed by the choices of the logarithms of the eigenvalues.

**Proof.** The Jordan-form construction gives one logarithm for each choice of $\log\lambda_i$; the branch ambiguity gives the rest.

## The One-Parameter Subgroups

**Definition.** A **one-parameter subgroup** of $GL_6(\mathbb{C})$ is a continuous homomorphism

$$
\gamma:\mathbb{R}\longrightarrow GL_6(\mathbb{C}),
\qquad
\gamma(s+t)=\gamma(s)\gamma(t).
$$

**Theorem.** Every one-parameter subgroup is of the form

$$
\gamma(t)=e^{tX}
$$

for a unique $X\in M_6(\mathbb{C})$.

**Proof.** The standard theorem for Lie groups: a continuous one-parameter subgroup is smooth, and its derivative at $0$ is $X=\gamma'(0)$; the function $t\mapsto\gamma(t)$ and $t\mapsto e^{tX}$ satisfy the same differential equation $\gamma'=\gamma X$ with the same initial condition, hence they agree. Uniqueness: $X=\gamma'(0)$.

**Corollary (the Lie algebra).** The tangent space at the identity is $M_6(\mathbb{C})$, with the bracket

$$
[X,Y]=XY-YX,
$$

and the exponential is the Lie group exponential.

**Proof.** The tangent space of $GL_6$ at $I_6$ is $M_6(\mathbb{C})$; the bracket is the derivative of the commutator of the conjugation; the one-parameter subgroups are the exponentials.

**Corollary (the functoriality).** For a homomorphism $\Phi:GL_6\to GL_6$, the derivative at the identity is a Lie algebra homomorphism, and

$$
\Phi(e^X)=e^{d\Phi(X)}.
$$

**Proof.** $\Phi$ sends one-parameter subgroups to one-parameter subgroups; differentiate.

## The Lie Algebras

### The General Linear Algebra

**Theorem.** $\mathfrak{gl}_6(\mathbb{C})=M_6(\mathbb{C})$ is a Lie algebra of complex dimension $36$ and real dimension $72$, with center $\mathbb{C}I_6$ and derived algebra $\mathfrak{sl}_6$.

**Proof.** The bracket is bilinear, antisymmetric and satisfies the Jacobi identity; the center is the scalars; the derived algebra is the traceless matrices because $[E_{ij},E_{ji}]=E_{ii}-E_{jj}$ and the commutators span the traceless part.

**Corollary (the real form).** The real Lie algebra $\mathfrak{gl}_6(\mathbb{R})$ has dimension $36$; the complex algebra, viewed as a real algebra, has dimension $72$.

**Proof.** A complex $n\times n$ matrix has $2n^2$ real parameters; a real one has $n^2$.

### The Special $*$-Unitary Algebra

**Definition.** The **special $*$-unitary algebra** is

$$
\mathfrak{su}(6)=\{X\in M_6(\mathbb{C}):X^*=-X,\ \operatorname{tr}X=0\}.
$$

**Theorem.** $\mathfrak{su}(6)$ is a real Lie algebra of dimension

$$
36-1=35,
$$

a compact real form of $\mathfrak{sl}_6(\mathbb{C})$, and the Lie algebra of $SU(6)$.

**Proof.** The skew-Hermitian matrices have real dimension $36$ (the diagonal is purely imaginary, the upper triangle is free complex, the lower is determined); the traceless condition removes one real dimension. The complexification is $\mathfrak{sl}_6(\mathbb{C})$; the Killing form is negative definite on $\mathfrak{su}(6)$, so the form is compact.

**Theorem (the exponential).** The exponential maps $\mathfrak{su}(6)$ onto $SU(6)$, and the eigenvalues of $e^X$ for $X\in\mathfrak{su}(6)$ lie on the unit circle.

**Proof.** $SU(6)$ is compact and connected, so the exponential of its Lie algebra is surjective. If $X$ is skew-Hermitian, it is unitarily diagonalizable with purely imaginary eigenvalues $\mathrm i\theta_j$; then $e^X$ has eigenvalues $e^{\mathrm i\theta_j}$ on the unit circle, and $\det e^X=e^{\operatorname{tr}X}=1$.

**Corollary (the dimensions).**

$$
\dim_{\mathbb{R}}U(6)=36,\qquad
\dim_{\mathbb{R}}SU(6)=35,\qquad
\dim_{\mathbb{R}}\mathfrak{gl}_6=72 .
$$

**Proof.** $U(6)$ is the skew-Hermitian matrices (dimension $36$); $SU(6)$ is the traceless part (dimension $35$); $\mathfrak{gl}_6$ is all matrices (complex dimension $36$, real dimension $72$).

**Remark (the center and the quotient).** The center of $SU(6)$ is $\mathbb{Z}/6$, and the adjoint group is $PSU(6)=SU(6)/(\mathbb{Z}/6)$, of dimension $35$, with Lie algebra $\mathfrak{su}(6)$.

## The Closed Form

### The Jordan Form

**Theorem (the closed form).** Let $X=PJP^{-1}$ with $J=\bigoplus J_{m_{ij}}(\lambda_i)$. Then

$$
e^X=P\left(\bigoplus e^{J_{m_{ij}}(\lambda_i)}\right)P^{-1},
\qquad
e^{J_m(\lambda)}=e^\lambda\sum_{k=0}^{m-1}\frac{N^k}{k!},
$$

where $N=J_m(\lambda)-\lambda I$ is the nilpotent shift.

**Proof.** $e^{PJP^{-1}}=Pe^JP^{-1}$; for a Jordan block, $e^{\lambda I+N}=e^\lambda e^N$ because $\lambda I$ commutes with $N$; the series $e^N$ terminates at $k=m-1$.

**Corollary (the trace and the determinant).**

$$
\operatorname{tr}e^X=\sum_{i=1}^{6}e^{\lambda_i},
\qquad
\det e^X=\prod_{i=1}^{6}e^{\lambda_i}=e^{\operatorname{tr}X}.
$$

**Proof.** The eigenvalues of $e^X$ are $e^{\lambda_i}$ with the algebraic multiplicities; the trace is the sum and the determinant the product.

**Corollary (the real eigenvalues).** If $X$ is Hermitian, $e^X$ is Hermitian positive definite; if $X$ is skew-Hermitian, $e^X$ is $*$-unitary.

**Proof.** The spectral theorem; the exponential acts on the eigenvalues by $e^{\lambda}$.

### The Exponential of a Sum

**Theorem (the Baker–Campbell–Hausdorff formula).** For $X,Y$ near $0$,

$$
e^Xe^Y=e^{X+Y+\frac12[X,Y]+\frac{1}{12}[X,[X,Y]]-\frac{1}{12}[Y,[X,Y]]+\cdots}.
$$

**Proof.** The standard BCH formula; the series converges in a neighborhood of $0$.

**Corollary (the Lie correspondence).** The Lie algebra bracket is the deviation from commutativity of the exponential:

$$
e^{tX}e^{tY}e^{-tX}e^{-tY}=e^{t^2[X,Y]+O(t^3)}.
$$

**Proof.** Expand the BCH formula to second order.

**Remark (the exponential is not a homomorphism).** In general $e^{X+Y}\neq e^Xe^Y$; the defect is measured by the BCH series. The exponential is a local diffeomorphism, not a group homomorphism.

## The Lie Group

### The Group Structure

**Theorem.** $GL_6(\mathbb{C})$ is a complex Lie group of complex dimension $36$ and real dimension $72$; its Lie algebra is $\mathfrak{gl}_6(\mathbb{C})$; its exponential is the matrix exponential.

**Proof.** $GL_6$ is the open subset $\det\neq0$ of $M_6(\mathbb{C})$; the group operations are rational and smooth; the tangent space at the identity is $M_6$; the exponential is the matrix exponential.

**Corollary (the closed subgroups).** Every closed subgroup of $GL_6(\mathbb{C})$ is a Lie subgroup (Cartan's theorem), and its Lie algebra is a subalgebra of $\mathfrak{gl}_6$.

**Proof.** Cartan's theorem on closed subgroups of Lie groups.

### The Compact Real Form

**Theorem.** $SU(6)$ is a compact connected Lie group of dimension $35$, with Lie algebra $\mathfrak{su}(6)$; its exponential is surjective.

**Proof.** $SU(6)$ is closed and bounded in $M_6(\mathbb{C})$, hence compact; it is connected; the dimension is the dimension of the Lie algebra; the exponential is surjective on a compact connected Lie group.

**Corollary (the eigenvalues and the determinant).** For $X\in\mathfrak{su}(6)$, the eigenvalues of $X$ are purely imaginary and sum to zero; the eigenvalues of $e^X$ are on the unit circle and their product is $1$.

**Proof.** Skew-Hermitian trace-zero; the exponential maps $\mathrm i\theta_j$ to $e^{\mathrm i\theta_j}$; the sum is zero, so the product is $1$.

**Remark (the topology).** $\pi_1(SU(6))=\mathbb{Z}/6$ and the center is $\mathbb{Z}/6$; the adjoint group $PSU(6)$ is $SU(6)/(\mathbb{Z}/6)$. The details are *The Topology of $M_6(\mathbb{C})$*.

## Summary

The exponential is

$$
e^X=\sum_{n=0}^{\infty}\frac{X^n}{n!},
$$

entire on $M_6(\mathbb{C})$, with

$$
e^{X+Y}=e^Xe^Y\ (XY=YX),\qquad
\det e^X=e^{\operatorname{tr}X},\qquad
\sigma(e^X)=e^{\sigma(X)} .
$$

It is surjective onto $GL_6(\mathbb{C})$; every invertible matrix has a logarithm, constructed from the Jordan form. The one-parameter subgroups are $e^{tX}$, and the Lie algebra is $\mathfrak{gl}_6$ with the commutator.

$$
\boxed{\ \exp:M_6(\mathbb{C})\twoheadrightarrow GL_6(\mathbb{C}),\qquad \dim_{\mathbb{R}}\mathfrak{gl}_6=72,\qquad \dim_{\mathbb{R}}\mathfrak{su}(6)=35 .\ }
$$

The closed form is the Jordan formula

$$
e^{PJP^{-1}}=Pe^JP^{-1},
\qquad
e^{J_m(\lambda)}=e^\lambda\sum_{k=0}^{m-1}\frac{N^k}{k!},
$$

and the eigenvalues of $e^X$ are $e^{\lambda_i}$.

| Object | Data |
|---|---|
| Exponential | entire, surjective onto $GL_6(\mathbb{C})$ |
| Logarithm | exists for every invertible matrix |
| One-parameter subgroups | $e^{tX}$, $X\in\mathfrak{gl}_6$ |
| $\dim_{\mathbb{R}}\mathfrak{gl}_6$ | $72$ |
| $\dim_{\mathbb{R}}\mathfrak{u}(6)$ | $36$ |
| $\dim_{\mathbb{R}}\mathfrak{su}(6)$ | $35$ |
| Determinant | $\det e^X=e^{\operatorname{tr}X}$ |
| Eigenvalues | $e^{\lambda_1},\dots,e^{\lambda_6}$ |
| Closed form | Jordan blocks, finite exponential series |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $e^X=\exp X$ | the matrix exponential |
| $\log A$ | a logarithm of $A$ |
| $\mathfrak{gl}_6$ | the Lie algebra $M_6(\mathbb{C})$ |
| $\mathfrak{su}(6)$ | the skew-Hermitian traceless algebra |
| $\operatorname{ad}_X$ | the commutator map $Y\mapsto[X,Y]$ |
| $J_m(\lambda)$ | the Jordan block |

## Further Reading

- [The Element, the Coordinates and the Trace of $M_6(\mathbb{C})$](the-element-the-coordinates-and-the-trace-of-m6c.html), for the Jordan form.
- [The Involution and the Hermitian Structure of $M_6(\mathbb{C})$](the-involution-and-the-hermitian-structure-of-m6c.html), for the $*$-unitary and special $*$-unitary groups.
- [Spectral Theory and the Spectral Projectors of $M_6(\mathbb{C})$](spectral-theory-and-the-spectral-projectors-of-m6c.html), for the Dunford calculus and the principal logarithm.
- [The Polar Decomposition of $M_6(\mathbb{C})$](the-polar-decomposition-of-m6c.html), for the exponential form $A=Ue^H$.
- [The Matrix Algebra $M_6(\mathbb{C})$](the-matrix-algebra-m6c.html), for the Lie algebra and its derivations.
- [The Topology of $M_6(\mathbb{C})$](the-topology-of-m6c.html), for the fundamental group and the center.
- [Analysis on $M_6(\mathbb{C})$](analysis-on-m6c.html), for the exponential as a holomorphic map and its differential.
