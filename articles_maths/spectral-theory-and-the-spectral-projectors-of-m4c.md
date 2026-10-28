# __Spectral Theory and the Spectral Projectors__

## Introduction

**The characteristic polynomial of $A\in M_4(\mathbb{C})$ has degree four and four roots, the Jordan form classifies the element up to conjugacy, and the spectral projectors are the Riesz projectors of the resolvent.** At a simple spectrum the spectral projectors are the Lagrange projectors, polynomials in $A$ of degree at most three. At a repeated root the Lagrange formula is not defined; the Riesz projectors are still defined by the contour integral, and they are the limits of sums of Lagrange projectors, with a nilpotent part appearing in the limit.

The article states the characteristic and minimal polynomials, the Jordan form, the Dunford calculus and the Riesz projectors, the resolvent and the spectral radius, the simple-spectrum Lagrange formula and its degeneration at a repeated root.

The element and the trace are *The Element, the Coordinates and the Trace*; the Jordan decomposition is there as well; the polar decomposition is *The Polar Decomposition*; the geometry of the spectral strata is *The Geometry of the Idempotents*.

## The Characteristic Polynomial

**Definition.** The **characteristic polynomial** of $A$ is

$$
\chi_A(t)=\det(tI-A).
$$

It is a monic polynomial of degree four:

$$
\chi_A(t)=t^4-(\operatorname{tr}A)t^3+c_2t^2-c_1t+\det A,
$$

with

$$
c_2=\frac12\bigl((\operatorname{tr}A)^2-\operatorname{tr}(A^2)\bigr),
$$

$$
c_1=\frac16\bigl((\operatorname{tr}A)^3-3\operatorname{tr}A\operatorname{tr}(A^2)+2\operatorname{tr}(A^3)\bigr).
$$

**The roots.** The **eigenvalues** are the roots

$$
\lambda_1,\lambda_2,\lambda_3,\lambda_4
$$

of $\chi_A$, counted with algebraic multiplicity. By the fundamental theorem of algebra there are four roots, and

$$
\operatorname{tr}A=\sum_{k=1}^{4}\lambda_k,\qquad
\det A=\prod_{k=1}^{4}\lambda_k .
$$

The **spectrum** is the set of eigenvalues, denoted $\sigma(A)$.

**The discriminant.** The **discriminant** is

$$
\Delta(A)=\prod_{i<j}(\lambda_i-\lambda_j)^2.
$$

It is a polynomial in the coefficients, hence in the entries of $A$. The spectrum is **simple** exactly when $\Delta(A)\ne0$; the four eigenvalues are then distinct.

**Invariance.** The characteristic polynomial is invariant under conjugation:

$$
\chi_{SAS^{-1}}(t)=\det(tI-SAS^{-1})=\det(S(tI-A)S^{-1})=\chi_A(t).
$$

The trace, the determinant and the coefficients $c_1,c_2$ are therefore conjugacy invariants.

**Cayley–Hamilton.** The matrix satisfies its own characteristic polynomial:

$$
\chi_A(A)=0.
$$

**Proof.** The characteristic polynomial is the determinant of $tI-A$; the Cayley–Hamilton theorem is the standard identity for matrices over a commutative ring. The proof uses the adjugate identity $\operatorname{adj}(tI-A)(tI-A)=\chi_A(t)I$ and the fact that the entries of the adjugate are polynomials in $t$; substituting $A$ for $t$ gives $\chi_A(A)=0$.

## The Minimal Polynomial and the Jordan Form

**The minimal polynomial.** The **minimal polynomial** $m_A(t)$ is the monic polynomial of least degree with $m_A(A)=0$. It divides the characteristic polynomial, and it has the same roots:

$$
m_A(t)=\prod_{k=1}^{r}(t-\lambda_k)^{m_k},
$$

where $\lambda_1,\dots,\lambda_r$ are the distinct eigenvalues and $m_k$ is the size of the largest Jordan block for $\lambda_k$.

**Diagonalisability.** The matrix $A$ is diagonalisable if and only if its minimal polynomial has distinct roots, equivalently if and only if all $m_k=1$. In that case

$$
A=S\operatorname{diag}(\lambda_1,\dots,\lambda_4)S^{-1}.
$$

**The Jordan form.** In general,

$$
A=SJS^{-1},\qquad
J=\operatorname{diag}\bigl(J_{n_1}(\lambda_1),\dots,J_{n_r}(\lambda_r)\bigr),
$$

with Jordan blocks

$$
J_n(\lambda)=\begin{pmatrix}
\lambda&1&0&\cdots&0\\
0&\lambda&1&\cdots&0\\
\vdots&&\ddots&\ddots&\vdots\\
0&&&\lambda&1\\
0&&\cdots&0&\lambda
\end{pmatrix}.
$$

The **semisimple part** is the diagonal of $J$, and the **nilpotent part** is the off-diagonal shift; the two commute. This is the Jordan decomposition of *The Element, the Coordinates and the Trace*.

**The spectral strata.** The eigenvalue multiplicity pattern stratifies the algebra:

| Multiplicity pattern | Semisimple orbit dimension | Jordan refinement |
|---|---|---|
| $1+1+1+1$ | $12$ | simple spectrum, diagonalisable |
| $2+1+1$ | $10$ | the double eigenvalue has a $2$-block or two $1$-blocks |
| $2+2$ | $8$ | each double eigenvalue has a $2$-block or two $1$-blocks |
| $3+1$ | $6$ | the triple eigenvalue has a $3$-block, a $2+1$, or three $1$-blocks |
| $4$ | $0$ | the scalar; the nilpotent refinements are all partitions of $4$ |

The dimensions are the semisimple orbit dimensions $16-\sum m_k^2$; the Jordan refinements within each pattern are the nilpotent orbits of the centraliser.

## The Resolvent

**Definition.** The **resolvent** of $A$ is

$$
R(z)=(zI-A)^{-1},
$$

defined for $z\notin\sigma(A)$.

**Proposition.** The resolvent is a holomorphic matrix-valued function on the complement of the spectrum, and

$$
R(z)=\frac{1}{z}\Bigl(I+\frac{A}{z}+\frac{A^2}{z^2}+\cdots\Bigr)
$$

for $\lvert z\rvert>\rho(A)$, where

$$
\rho(A)=\max_{k}\lvert\lambda_k\rvert
$$

is the **spectral radius**. The series converges absolutely and uniformly on compact subsets of $\lvert z\rvert>\rho(A)$.

**Proof.** The identity $(zI-A)^{-1}=z^{-1}(I-A/z)^{-1}$ and the geometric series for $\lVert A/z\rVert<1$ give the expansion. The radius of convergence is the spectral radius by the root test and the Gelfand formula.

**The poles.** The resolvent has poles at the eigenvalues. If $\lambda$ is an eigenvalue with Jordan blocks of sizes $n_1,\dots,n_s$, the Laurent expansion at $\lambda$ has the form

$$
R(z)=\sum_{k=1}^{N}\frac{N_k}{(z-\lambda)^k}+\text{holomorphic},
$$

where $N_k$ are nilpotent matrices supported on the generalized eigenspace. The residue at $\lambda$ is the spectral projector:

$$
P_\lambda=\frac{1}{2\pi i}\oint_{\gamma_\lambda}R(z)\,dz,
$$

with $\gamma_\lambda$ a small positively oriented circle around $\lambda$ separating it from the other eigenvalues.

**The Riesz projectors.** The **spectral projector** of $\lambda$ is

$$
P_\lambda=\frac{1}{2\pi i}\oint_{\gamma_\lambda}(zI-A)^{-1}\,dz.
$$

**Theorem.** The projectors satisfy

$$
P_\lambda^2=P_\lambda,\qquad
P_\lambda P_\mu=0\quad(\lambda\ne\mu),\qquad
\sum_{\lambda\in\sigma(A)}P_\lambda=I.
$$

The image of $P_\lambda$ is the generalized eigenspace

$$
\ker(A-\lambda I)^{m_\lambda},
$$

and $A$ preserves it. The restriction of $A$ to the image is $\lambda I+N_\lambda$ with $N_\lambda$ nilpotent. Hence

$$
A=\sum_{\lambda}\bigl(\lambda P_\lambda+N_\lambda\bigr),
\qquad
N_\lambda=(A-\lambda I)P_\lambda,
$$

and the $N_\lambda$ commute with the projectors.

**Proof.** The projector is the residue of the resolvent; the residue calculus gives $P_\lambda^2=P_\lambda$ and the orthogonality, because the contours are disjoint. The sum is $I$: at infinity $R(z)=z^{-1}I+O(z^{-2})$, so the residue at infinity is $-I$ and the sum of the finite residues is $I$. The image is the generalized eigenspace by the Riesz decomposition theorem; the nilpotent part is $A-\lambda I$ on that space. The details are in Kato, *Perturbation Theory for Linear Operators*, and in Horn and Johnson, *Matrix Analysis*.

## The Dunford Calculus

**The holomorphic functional calculus.** Let $f$ be holomorphic on an open set containing the spectrum of $A$. Define

$$
f(A)=\frac{1}{2\pi i}\oint_{\gamma}f(z)(zI-A)^{-1}\,dz,
$$

where $\gamma$ is a positively oriented contour enclosing the spectrum. The integral is independent of the contour by Cauchy's theorem.

**Theorem.** The map $f\mapsto f(A)$ is an algebra homomorphism:

$$
(f+g)(A)=f(A)+g(A),\qquad
(fg)(A)=f(A)g(A),\qquad
1(A)=I,
$$

and it satisfies the **spectral mapping theorem**:

$$
\sigma(f(A))=f(\sigma(A)).
$$

**Proof.** The homomorphism property follows from the resolvent identity

$$
(zI-A)^{-1}(wI-A)^{-1}=\frac{(zI-A)^{-1}-(wI-A)^{-1}}{w-z},
$$

and the Cauchy integral. The spectral mapping theorem is the standard consequence for the holomorphic functional calculus. The details are in Dunford and Schwartz, *Linear Operators*, Part I.

**The Dunford decomposition.** The spectral projectors give the **Dunford decomposition**

$$
A=\sum_{\lambda}(\lambda P_\lambda+N_\lambda)=A_s+A_n,
$$

with

$$
A_s=\sum_{\lambda}\lambda P_\lambda,\qquad
A_n=\sum_{\lambda}N_\lambda .
$$

The semisimple part $A_s$ is diagonalisable, the nilpotent part $A_n$ is nilpotent, and they commute. This is the Jordan–Chevalley decomposition of *The Element, the Coordinates and the Trace*, recovered from the resolvent.

**The spectral resolution.** For a function $f$ holomorphic on the spectrum,

$$
f(A)=\sum_{\lambda}\sum_{k=1}^{m_\lambda}\frac{f^{(k-1)}(\lambda)}{(k-1)!}N_\lambda^{k-1}P_\lambda .
$$

For a polynomial $f$, this is the Lagrange–Sylvester interpolation formula. For the exponential, it gives the closed form of *The Exponential and the Lie Group*.

## The Simple Spectrum and the Lagrange Projectors

**The Lagrange formula.** Suppose the spectrum is simple: $\lambda_1,\lambda_2,\lambda_3,\lambda_4$ are distinct. Then the spectral projectors are the **Lagrange projectors**

$$
P_k=\prod_{l\ne k}\frac{A-\lambda_lI}{\lambda_k-\lambda_l},
\qquad k=1,2,3,4.
$$

**Theorem.** The Lagrange projectors are idempotent, orthogonal and complete:

$$
P_k^2=P_k,\qquad
P_kP_l=0\quad(k\ne l),\qquad
\sum_{k=1}^{4}P_k=I,
$$

and

$$
A=\sum_{k=1}^{4}\lambda_kP_k .
$$

They are the Riesz projectors of the simple eigenvalues, and they are polynomials in $A$ of degree at most three.

**Proof.** On the eigenvector $v_l$, the product $\prod_{l\ne k}(A-\lambda_lI)/(\lambda_k-\lambda_l)$ acts by $\delta_{kl}$: all factors except the $k$-th vanish, and the $k$-th factor is $1$. Hence $P_k$ is the projector onto the $k$-th eigenline along the sum of the other three, and the identities follow. The spectral resolution follows by applying both sides to a basis of eigenvectors.

**The interpolation form.** The projectors are the images of the indicator polynomials

$$
p_k(t)=\prod_{l\ne k}\frac{t-\lambda_l}{\lambda_k-\lambda_l},
\qquad
p_k(\lambda_l)=\delta_{kl}.
$$

For every polynomial $f$ of degree at most three,

$$
f(A)=\sum_{k=1}^{4}f(\lambda_k)P_k .
$$

This is the Lagrange interpolation formula in the algebra $M_4$.

## The Limit at a Repeated Root

**The failure of the Lagrange formula.** If two eigenvalues coalesce, $\lambda_1\to\lambda_2$, the denominators $\lambda_1-\lambda_2$ tend to zero, and the individual Lagrange projectors need not have a limit. The sum $P_1+P_2$ does have a limit: it is the Riesz projector onto the generalized eigenspace of the double eigenvalue. The weighted sum $\lambda_1P_1+\lambda_2P_2$ tends to $\lambda(P_1+P_2)+N$, where $N$ is a nilpotent matrix; the nilpotent part is the limit of the difference.

**The theorem.** Let $A(t)$ be a holomorphic family of matrices, and suppose that two simple eigenvalues $\lambda_1(t),\lambda_2(t)$ coalesce at $t=0$ to $\lambda$. Then, for a fixed contour $\gamma$ around $\lambda$,

$$
P(t)=P_1(t)+P_2(t)=\frac{1}{2\pi i}\oint_\gamma(zI-A(t))^{-1}\,dz
\longrightarrow
P(0),
$$

the Riesz projector onto the generalized eigenspace of $\lambda$. The individual Lagrange projectors $P_1(t),P_2(t)$ may diverge like $1/t$; their sum remains bounded. The limit of $A(t)$ is

$$
A(0)=\lambda P(0)+N,
$$

with $N$ nilpotent and $N=P(0)N P(0)$.

**The path dependence.** The nilpotent $N$ is determined by the limit matrix $A(0)$: once $A(0)$ is fixed, its Jordan form and its nilpotent part are fixed. What depends on the path is the way the individual Lagrange projectors diverge and the way $N$ is approximated by the weighted differences. Different paths with different limit matrices give different nilpotent parts; for a fixed limit $A(0)$, the Riesz projector and $N$ are fixed. The individual Lagrange projectors do not have a canonical limit, while the Riesz projector is canonical and continuous.

**The simple-spectrum limit.** When the spectrum stays simple, the Riesz projectors and the Lagrange projectors coincide, and they depend holomorphically on $A$. At the discriminant locus $\Delta(A)=0$, the Lagrange formula degenerates and the Riesz projectors continue across the stratum.

## The Spectral Radius and the Norms

**The spectral radius.** The spectral radius is

$$
\rho(A)=\max_{\lambda\in\sigma(A)}\lvert\lambda\rvert .
$$

It satisfies the **Gelfand formula**

$$
\rho(A)=\lim_{n\to\infty}\lVert A^n\rVert^{1/n},
$$

for every matrix norm. It is not a norm: $\rho(A)=0$ for a nonzero nilpotent, and it does not satisfy the triangle inequality in general.

**The comparison with the operator norm.** For every matrix norm,

$$
\rho(A)\le\lVert A\rVert,
$$

and for the operator norm,

$$
\rho(A)\le\lVert A\rVert_{\mathrm{op}},
$$

with equality for normal matrices. For a normal matrix, the operator norm is the largest modulus of an eigenvalue; for a non-normal matrix, the operator norm can be strictly larger.

**The resolvent bound.** For $\lvert z\rvert>\rho(A)$, the resolvent series converges. The spectral radius is the radius of convergence of the Neumann series at infinity: the series converges for $\lvert z\rvert>\rho(A)$ and diverges for $\lvert z\rvert<\rho(A)$ in general. The resolvent itself is holomorphic on the whole complement of the spectrum, which is larger than the exterior disc when the spectrum has eigenvalues of smaller modulus.

**The stability.** The spectral radius governs the asymptotic behaviour of the powers:

$$
A^n\to0\quad\iff\quad\rho(A)<1.
$$

If $\rho(A)<1$, the Neumann series $\sum_{n\ge0}A^n$ converges to $(I-A)^{-1}$; if $\rho(A)\ge1$, the series diverges in general. The spectral radius is the stability margin of the discrete dynamical system $x_{n+1}=Ax_n$.

## Summary

The characteristic polynomial of $A$ is a monic quartic with roots the eigenvalues, trace the sum and determinant the product; the minimal polynomial records the largest Jordan block for each eigenvalue, and $A$ is diagonalisable exactly when the minimal polynomial has distinct roots. The Jordan form classifies the conjugacy class. The resolvent $(zI-A)^{-1}$ is holomorphic off the spectrum and has poles at the eigenvalues; the residue at $\lambda$ is the Riesz projector $P_\lambda$, and the projectors are idempotent, orthogonal and complete, with $A=\sum(\lambda P_\lambda+N_\lambda)$ and $N_\lambda$ nilpotent. The holomorphic functional calculus is the Dunford calculus, with the spectral mapping theorem. At a simple spectrum the Riesz projectors are the Lagrange projectors $P_k=\prod_{l\ne k}(A-\lambda_lI)/(\lambda_k-\lambda_l)$, polynomials in $A$ of degree at most three. At a repeated root the individual Lagrange projectors need not converge, but their sums converge to the Riesz projectors, and the nilpotent part appears as the limit of the weighted differences. For a fixed limit matrix the Riesz projector and the nilpotent part are fixed; only the way the individual projectors diverge depends on the path. The spectral radius is the largest eigenvalue modulus, the radius of convergence of the resolvent series and the stability margin.

$$
\boxed{\ \chi_A(t)=t^4-(\operatorname{tr}A)t^3+c_2t^2-c_1t+\det A,\quad A=\sum_\lambda(\lambda P_\lambda+N_\lambda),\quad P_\lambda=\frac{1}{2\pi i}\oint_{\gamma_\lambda}(zI-A)^{-1}dz. }
$$

| Object | Meaning |
|---|---|
| $\chi_A$ | characteristic polynomial, degree $4$ |
| $m_A$ | minimal polynomial |
| $\sigma(A)$ | spectrum, four eigenvalues with multiplicity |
| $P_\lambda$ | Riesz spectral projector |
| $N_\lambda$ | nilpotent part on the generalized eigenspace |
| $\rho(A)$ | spectral radius |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\lambda_k$ | the eigenvalues |
| $\Delta(A)$ | the discriminant |
| $R(z)=(zI-A)^{-1}$ | the resolvent |
| $P_\lambda$ | the spectral projector |
| $N_\lambda$ | the nilpotent part |
| $P_k$ | the Lagrange projector at a simple spectrum |
| $\rho(A)$ | the spectral radius |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the characteristic polynomial, the Jordan form, the minimal polynomial and the spectral projectors.
- Tosio Kato, *Perturbation Theory for Linear Operators* (Springer, 1995), for the Riesz projectors, the resolvent and the perturbation of eigenvalues.
- Nelson Dunford and Jacob T. Schwartz, *Linear Operators, Part I* (Interscience, 1958), for the holomorphic functional calculus and the spectral mapping theorem.
- [The Element, the Coordinates and the Trace](the-element-the-coordinates-and-the-trace-of-m4c.html), for the Jordan decomposition.
- [The Polar Decomposition](the-polar-decomposition-of-m4c.html), for the spectral theorem for normal matrices.
- [Roots of Unity and the Lagrange Idempotents](roots-of-unity-and-the-lagrange-idempotents-of-m4c.html), for the simple-spectrum Lagrange projectors.
- [The Geometry of the Idempotents](the-geometry-of-the-idempotents-of-m4c.html), for the spectral strata and their geometry.
