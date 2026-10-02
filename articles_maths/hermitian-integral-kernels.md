
# __Hermitian Integral Kernels__

## Introduction

A Hermitian kernel is a kernel equal to its conjugate transpose, $K(y,x)=\overline{K(x,y)}$, and the integral
operator of a Hermitian kernel is self-adjoint. The self-adjointness is only the beginning: such an operator
has a real spectrum, its eigenfunctions are orthogonal, and the kernel is the expansion
$$
K(x,y)=\sum_n\lambda_n\varphi_n(x)\overline{\varphi_n(y)}
$$
in the eigenfunctions with the eigenvalues as coefficients. Positivity of the operator — the case of a
positive definite kernel — is exactly the nonnegativity of the eigenvalues, and then the expansion converges
absolutely and uniformly for a continuous kernel on a compact space (Mercer's theorem), the reproducing
kernel Hilbert space of the kernel is the range of the square root with the square roots of the eigenvalues
as its basis, and the trace and the Hilbert–Schmidt norm are read from the kernel. This article is the
spectral theory of the Hermitian kernel, built from the involution of the previous articles.

It is the second article of the `* Operator Theory` group of *Foundations of Analysis*. Its prerequisites
are *Hermitian Kernels and the Integral Operator*, the last article of the `* Theory` group, for the Hermitian
and positive definite kernels and their dictionary with self-adjointness and positivity; *The Adjoint of an
Integral Operator*, the previous article, for $T_K^\dagger=T_{K^*}$; *Reproducing Kernel Hilbert Spaces* and
*Positive Definite Functions and Hermitian Kernels*, the first two articles of the `* Theory` group, for the
reproducing space and Bochner's theorem; *Banach and Hilbert Spaces* and *Compact Operators*, later in this
Part, for the spectral theorem for compact self-adjoint operators, the Fredholm theory and the positivity
criterion, quoted as established; and *Measure Theory and Integration* for the product measure, Fubini and
the monotone convergence theorem. The abstract spectral theorem in its projection-valued form, the square
root of a positive operator, and the general theory of Hilbert–Schmidt and trace-class operators are
*Analysis on Linear Spaces*, later in this Part; Mercer's uniform convergence is quoted from the classical
theory and deferred in its detail to *Compact Operators*. The distributional generalisation is *The Schwartz
Kernel Theorem*, later in this Part. No geometry is invoked.

## The Hermitian Kernel and the Self-Adjoint Operator

### The Hermitian Kernel

**Definition.** A kernel $K\in L^2(X\times X)$ is **Hermitian** if $K^*=K$, that is
$K(y,x)=\overline{K(x,y)}$ for almost every $(x,y)$; it is **symmetric** if in addition it is real; and it is
**positive definite** if $\sum_{i,j}\overline{c_i}c_jK(x_i,x_j)\geq0$ for every finite family of points and
coefficients. A **Hermitian integral kernel** is the operator $T_K$ of a Hermitian kernel,
$$
(T_Kf)(x)=\int_XK(x,y)f(y)\,d\mu(y) .
$$

### Self-Adjointness

**Theorem.** Let $K\in L^2(X\times X)$ and let $T_K$ be bounded on $L^2(X,\mu)$. Then $T_K$ is self-adjoint,
$T_K^\dagger=T_K$, if and only if the kernel is Hermitian; equivalently
$$
\langle T_Kf,g\rangle=\overline{\langle T_Kg,f\rangle}\qquad\text{for all }f,g\in L^2 ,
$$
the sesquilinear form of the operator being Hermitian, and $\langle T_Kf,f\rangle$ is real for every $f$.

**Proof.** The adjoint of $T_K$ is $T_{K^*}$ by *The Adjoint of an Integral Operator*, the previous article,
so $T_K^\dagger=T_K$ is $K^*=K$ by the uniqueness of the kernel of a Hilbert–Schmidt operator; the form
identity is the polarisation of that self-adjointness, and it holds for every square-integrable kernel
because the finite data of the definition of positive definiteness are dense in the form's domain.
$\blacksquare$

### Positivity

**Theorem (the positivity criterion).** For a Hermitian kernel $K$, the following are equivalent: the kernel
is positive definite; the operator is positive, $\langle T_Kf,f\rangle\geq0$ for every $f\in L^2$; and every
eigenvalue of $T_K$ is nonnegative. If in addition the kernel is continuous and $X$ is compact with a finite
measure, positivity is also equivalent to $K(x,x)\geq0$ together with the nonnegativity of the eigenvalues,
by Mercer's theorem below.

**Proof.** The equivalence of the first two is the dictionary of *Hermitian Kernels and the Integral
Operator*, the previous group; the equivalence with the third is the spectral theorem below, since the
eigenvalues are the values of the quadratic form on the eigenfunctions, and a self-adjoint operator is
positive exactly when its spectrum is contained in $[0,\infty)$ by *Banach and Hilbert Spaces*, later in this
Part. The last statement is Mercer's theorem. $\blacksquare$

## The Spectral Theory of the Kernel

### Compactness and the Real Spectrum

**Theorem (the spectral theorem for the Hermitian Hilbert–Schmidt kernel).** Let $K\in L^2(X\times X)$ be
Hermitian and let $T_K$ be its integral operator. Then $T_K$ is self-adjoint and compact, its eigenvalues
$\lambda_n$ are real and tend to $0$, the eigenvectors $\varphi_n$ may be taken orthonormal,
$$
T_K\varphi_n=\lambda_n\varphi_n,\qquad
T_Kf=\sum_n\lambda_n\langle f,\varphi_n\rangle\varphi_n ,
$$
and the eigenvalue list is the only spectral data of the operator,
$\lVert T_K\rVert=\max_n\lvert\lambda_n\rvert$.

**Proof.** An integral operator with an $L^2$ kernel is Hilbert–Schmidt and hence compact, being the norm
limit of its finite-rank truncations in the kernel expansion; a compact self-adjoint operator has a countable
real spectrum with an orthonormal eigenbasis and $\lVert T_K\rVert=\max\lvert\lambda_n\rvert$, by the
spectral theory of *Compact Operators* and *Banach and Hilbert Spaces*, later in this Part.
$\blacksquare$

### The Eigenfunction Expansion of the Kernel

**Theorem (the kernel expansion).** Under the hypotheses of the spectral theorem,
$$
K(x,y)=\sum_n\lambda_n\varphi_n(x)\overline{\varphi_n(y)} ,
$$
the series converging in $L^2(X\times X)$; and $\lVert K\rVert_{L^2}^2=\sum_n\lambda_n^2$.

**Proof.** The kernel of $T_K$ is recovered from the operator by
$K(x,y)=\sum_n(T_K\varphi_n)(x)\overline{\varphi_n(y)}$ in the $L^2$ sense, as in the isometry of the
`* Theory` article, and the eigenrelation gives the stated expansion; the norm identity is Parseval's
identity applied to the expansion. $\blacksquare$

**Example (the Green function of the Dirichlet problem).** On $X=[0,1]$ with the Lebesgue measure the kernel
$$
G(x,y)=\min(x,y)-xy
$$
is real, symmetric and continuous, hence Hermitian and self-adjoint; the operator $T_G$ is the inverse of
$-\frac{d^2}{dx^2}$ with the vanishing boundary conditions, so its eigenfunctions are
$\varphi_n(x)=\sqrt2\sin(n\pi x)$ and its eigenvalues are $\lambda_n=1/(n^2\pi^2)>0$. The kernel is positive
definite, the expansion $\min(x,y)-xy=\sum_{n\geq1}\frac2{n^2\pi^2}\sin(n\pi x)\sin(n\pi y)$ converges
absolutely and uniformly, and $\sum_n\lambda_n=1/6=\int_0^1G(x,x)\,dx$.

**Example (the covariance kernel).** The kernel $K(x,y)=\min(x,y)$ on $[0,1]$ is continuous, symmetric and
positive definite, so its operator is compact, self-adjoint and positive, with a nonnegative eigenvalue list
and the uniform Mercer expansion; it is the sum of the Green kernel above and the kernel $xy$ of the rank-one
projection on the constant function, and this is the two-term decomposition of the covariance into its part
vanishing at $0$ and its mean.

## Positive Definite Kernels and Nonnegative Spectrum

### The Equivalence

**Theorem.** A Hermitian kernel is positive definite if and only if its eigenvalues are nonnegative; then
$T_K$ is a positive operator, its square root $T_K^{1/2}$ is the operator with eigenvalues
$\sqrt{\lambda_n}$,
$$
T_K^{1/2}f=\sum_n\sqrt{\lambda_n}\langle f,\varphi_n\rangle\varphi_n ,
$$
and the pair $(T_K,T_K^{1/2})$ is the spectral square root of the positive kernel.

**Proof.** The equivalence is the positivity criterion above; the square root is the operator with the
square-root eigenvalues, and its square is $T_K$ by the eigenrelation, so it is the unique positive square
root once uniqueness is known, by the positivity of the eigenvalues. The functional calculus that defines
$T_K^{1/2}$ in general is *Analysis on Linear Spaces*, later in this Part. $\blacksquare$

### Mercer's Theorem

**Theorem (Mercer).** Let $X$ be a compact space with a finite measure $\mu$ and let $K$ be a continuous
positive definite kernel on $X\times X$. Then the eigenvalues $\lambda_n$ are nonnegative, the eigenfunctions
$\varphi_n$ may be taken continuous and orthonormal, and
$$
K(x,y)=\sum_n\lambda_n\varphi_n(x)\overline{\varphi_n(y)} ,
$$
the series converging absolutely and uniformly on $X\times X$. In particular $K(x,x)\geq0$ for every $x$, and
the convergence of the diagonal is the convergence of $\sum_n\lambda_n\lvert\varphi_n(x)\rvert^2$.

**Proof.** A continuous kernel on a compact space with a finite measure defines a compact self-adjoint
operator with continuous eigenfunctions by the classical argument, and the nonnegative eigenvalues give the
absolute and uniform convergence of the expansion; the positivity of the eigenvalues is the positivity of
the kernel. The uniform convergence is quoted from *Compact Operators*, later in this Part, where the
Riesz–Schauder theory is developed. $\blacksquare$

## The Reproducing Space and the Trace

### The Reproducing Space as the Range of the Square Root

**Theorem.** For a continuous positive definite kernel $K$ on a compact space with a finite measure, the
reproducing kernel Hilbert space $H_K$ of *Reproducing Kernel Hilbert Spaces* is the range of the square
root,
$$
H_K=T_K^{1/2}(L^2),\qquad
\lVert T_K^{1/2}g\rVert_{H_K}=\lVert g\rVert_{L^2}\quad(g\perp\ker T_K) ,
$$
and, on the eigenfunctions, $H_K$ consists of the functions $f=\sum_na_n\varphi_n$ with
$\sum_n\lvert a_n\rvert^2/\lambda_n<\infty$, the sum over the nonzero eigenvalues,
$$
\lVert f\rVert_{H_K}^2=\sum_n\frac{\lvert a_n\rvert^2}{\lambda_n},
\qquad
\langle f,K(\cdot,x)\rangle=f(x) .
$$

**Proof.** The functions $\sqrt{\lambda_n}\varphi_n$ for the nonzero eigenvalues form an orthonormal basis of
$H_K$, so $H_K$ is the range of the map $g\mapsto\sum_n\sqrt{\lambda_n}\langle g,\varphi_n\rangle\varphi_n$
on the orthogonal complement of $\ker T_K$; the reproducing property is the expansion of the kernel, by the
eigenfunction expansion of the previous section. $\blacksquare$

### The Trace

**Corollary (the trace identities).** If $K$ is continuous positive definite and the eigenvalues are
summable, then
$$
\operatorname{tr}T_K=\sum_n\lambda_n=\int_XK(x,x)\,d\mu(x),
\qquad
\lVert K\rVert_{L^2}^2=\lVert T_K\rVert_{\mathrm{HS}}^2=\sum_n\lambda_n^2 .
$$

**Proof.** The first identity is the integral of the diagonal of the Mercer expansion, legitimate by the
monotone convergence theorem applied to the nonnegative expansion of $K(x,x)$; the second is Parseval's
identity for the eigenfunction expansion, equivalently the isometry of the Hilbert–Schmidt correspondence of
the `* Theory` article. $\blacksquare$

**Example (the Green function, continued).** For $G(x,y)=\min(x,y)-xy$ the diagonal integral is
$\int_0^1(x-x^2)dx=1/6$ and the eigenvalue sum is $\sum_{n\geq1}1/(n^2\pi^2)=\frac1{\pi^2}\cdot\frac{\pi^2}6=1/6$,
so the trace identity holds; the Hilbert–Schmidt norm is
$\lVert G\rVert_{L^2}^2=\sum_{n\geq1}\pi^{-4}n^{-4}=\pi^{-4}\cdot\frac{\pi^4}{90}=1/90$.

## Summary

A Hermitian kernel $K(y,x)=\overline{K(x,y)}$ has the self-adjoint integral operator $T_K$, characterised by
the reality of the sesquilinear form and equivalent to the Hermitian condition by the adjoint kernel
$K^*(x,y)=\overline{K(y,x)}$; positivity of the operator is the positive definiteness of the kernel, and both
are equivalent to the nonnegativity of the eigenvalues. A Hermitian Hilbert–Schmidt kernel has a real
eigenvalue list tending to $0$ with an orthonormal eigenbasis, and the kernel is the expansion
$K(x,y)=\sum_n\lambda_n\varphi_n(x)\overline{\varphi_n(y)}$ converging in $L^2$, with
$\lVert K\rVert_{L^2}^2=\sum_n\lambda_n^2$. For a continuous positive definite kernel on a compact space the
eigenvalues are nonnegative, the expansion converges absolutely and uniformly (Mercer's theorem) and the
diagonal is nonnegative; the reproducing kernel Hilbert space is the range of the square root,
$H_K=T_K^{1/2}(L^2)$, with the orthonormal basis $\sqrt{\lambda_n}\varphi_n$ and the norm
$\sum_n\lvert a_n\rvert^2/\lambda_n$, and the trace identities
$\operatorname{tr}T_K=\sum_n\lambda_n=\int K(x,x)d\mu$ and $\lVert K\rVert_{L^2}^2=\sum_n\lambda_n^2$ hold.
The Green kernel $\min(x,y)-xy$ of the Dirichlet problem, with eigenvalues $1/(n^2\pi^2)$ and trace $1/6$,
is the standard illustration. The abstract projection-valued spectral theorem and the general square root are
owned by later articles.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K^*$, Hermitian | $K^*(x,y)=\overline{K(y,x)}$, $K^*=K$ |
| $T_K^\dagger=T_K$ | Self-adjointness of a Hermitian kernel |
| positive definite kernel | $\sum_{i,j}\overline{c_i}c_jK(x_i,x_j)\geq0$ |
| $\lambda_n$, $\varphi_n$ | Eigenvalues and orthonormal eigenfunctions, $T_K\varphi_n=\lambda_n\varphi_n$ |
| $K(x,y)=\sum_n\lambda_n\varphi_n(x)\overline{\varphi_n(y)}$ | Eigenfunction expansion of the kernel |
| $T_K^{1/2}$ | Positive square root, eigenvalues $\sqrt{\lambda_n}$ |
| $H_K=T_K^{1/2}(L^2)$ | Reproducing space as the range of the square root |
| $\lVert f\rVert_{H_K}^2=\sum_n\lvert a_n\rvert^2/\lambda_n$ | Reproducing norm |
| $\operatorname{tr}T_K=\int K(x,x)d\mu=\sum_n\lambda_n$ | Trace identity |

## Further Reading

- Frigyes Riesz and Béla Szőkefalvi-Nagy, *Functional Analysis* (Ungar, 1955; reprinted Dover, 1990), for the
  spectral theory of compact self-adjoint operators and the integral operators.
- Franco Smithies, *Integral Equations* (Cambridge University Press, 1958), for Mercer's theorem and the
  eigenfunction expansion of a kernel.
- James Mercer, *Functions of Positive and Negative Type, and their Connection with the Theory of Integral
  Equations* (Philosophical Transactions of the Royal Society A 209, 1909), for the original uniform
  convergence theorem.
- Nachman Aronszajn, *Theory of Reproducing Kernels* (Transactions of the American Mathematical Society 68,
  1950), for the reproducing space and its spectral basis.
- Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics I: Functional Analysis* (Academic
  Press, 1980), for the compact self-adjoint spectral theorem and the trace class.
- Richard Courant and David Hilbert, *Methods of Mathematical Physics, Vol. I* (Interscience, 1953), for the
  integral equations, the eigenvalue problem of a kernel and the Green function examples.
