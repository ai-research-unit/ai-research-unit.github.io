
# __Hermitian Kernels and the Integral Operator__

## Introduction

The integral operator with kernel $K$ on a measure space is
$$
(T_Kf)(x)=\int_XK(x,y)f(y)\,d\mu(y),
$$
and its adjoint is the integral operator with the conjugate-transposed kernel,
$T_K^\dagger=T_{K^*}$ where $K^*(x,y)=\overline{K(y,x)}$. The involution of the previous articles of this
group — the conjugate transpose of a kernel — is in this way exactly the adjoint of an operator, and the
Hermitian kernels are exactly the self-adjoint integral operators, while the positive definite kernels are
exactly the positive ones. The correspondence is not only a dictionary: for kernels in $L^2$ it is an
isometry onto the Hilbert–Schmidt operators, so that the Hilbert–Schmidt class is a space of kernels with the
operator norm replaced by the $L^2$ norm, and the spectral decomposition of a Hermitian kernel is the
spectral decomposition of a compact self-adjoint operator, with real eigenvalues and orthogonal
eigenfunctions (Mercer's theorem). This article is the bridge between the kernel theory of the `*` group and
the operator theory of the corpus, and it completes the first half of the `*` material.

It is the sixth and last article of the `*` group of *Foundations of Analysis*. Its prerequisites are
*The Integral Operator*, *Convolution Operators* and *The Fourier Operator*, the operator articles of the
first group of this category, for the integral operator, the kernel and its adjoint; *Positive Definite
Functions and Hermitian Kernels* and *Reproducing Kernel Hilbert Spaces*, the first two articles of this
group, for the Hermitian and positive definite kernels and the reproducing space; and *Measure Theory and
Integration* for the product measure and Fubini. The general theorem that every bounded operator has a
distribution kernel is *The Schwartz Kernel Theorem*, later in this Part; the spectral theory of self-adjoint
and compact operators is *Banach and Hilbert Spaces* and *Compact Operators*, later in this Part; and the
`* Operator` group that follows this article — *The Adjoint of an Integral Operator*, *Hermitian Integral
Kernels*, *Involutions of the Convolution Operators* and *The Adjoint of the Fourier Operator* — develops the
operator theory for which the present article supplies the kernel form. The classical Fredholm theory of
integral equations and the Hilbert–Schmidt expansion are quoted from *Compact Operators*; the reproducing
kernel Hilbert space inside the range of the square root is the previous article. No geometry is invoked.

## The Integral Operator of a Kernel

### Definition and the Adjoint

**Definition.** Let $(X,\mathcal A,\mu)$ be a measure space and $K:X\times X\to\mathbb C$ a measurable
kernel. The **integral operator** with kernel $K$ is
$$
(T_Kf)(x)=\int_XK(x,y)f(y)\,d\mu(y) ,
$$
whenever the integral converges, and $K$ is a **kernel** of $T_K$; the **conjugate transpose** of the kernel
is $K^*(x,y)=\overline{K(y,x)}$, and the kernel is **Hermitian** if $K^*=K$, **positive definite** if the
kernel of the first article of this group is, and **real** if $K$ takes real values.

**Theorem (the adjoint kernel).** When $T_K$ is bounded on $L^2(\mu)$, its adjoint is the integral operator
with the conjugate transpose kernel,
$$
T_K^\dagger=T_{K^*} .
$$
Consequently $T_K$ is self-adjoint, $T_K^\dagger=T_K$, if and only if the kernel is Hermitian.

**Proof.** By Fubini,
$$
\langle T_Kf,g\rangle=\iint K(x,y)f(y)\overline{g(x)}\,d\mu(y)d\mu(x)
=\iint f(y)\overline{\Bigl(\int\overline{K(x,y)}g(x)\,d\mu(x)\Bigr)}\,d\mu(y)
=\langle f,T_{K^*}g\rangle ,
$$
the inner integral being $(T_{K^*}g)(y)$ with $K^*(y,x)=\overline{K(x,y)}$. Hence
$T_K^\dagger=T_{K^*}$, and the fixed-point statement is immediate. $\blacksquare$

### Positive Definite Kernels and Positive Operators

**Theorem (the dictionary).** Let $K\in L^2(X\times X)$ and suppose $T_K$ is bounded. Then $K$ is positive
definite if and only if $T_K$ is a positive operator,
$$
K\ \text{positive definite}\ \Longleftrightarrow\ \langle T_Kf,f\rangle\geq0\ \text{for all }f\in L^2(\mu) ;
$$
more precisely, for $f$ a finite linear combination of indicator functions,
$$
\langle T_Kf,f\rangle=\sum_{i,j}\overline{c_i}c_jK(x_i,x_j) ,
$$
so the positivity of the quadratic form of the operator is the positivity of the kernel.

**Proof.** The identity is the expansion of the double integral on simple functions; the passage to all of
$L^2$ is the density of the simple functions and the boundedness of $T_K$; the positive definite condition on
the kernel is the positivity of the same form for all finite data, which is the density of the finite
combinations of indicators in the relevant sense. $\blacksquare$

**Corollary (the Hermitian and the positive).** The Hermitian kernels correspond to the self-adjoint integral
operators and the positive definite kernels to the positive operators; the value-conjugation is not involved,
the relevant involution being the conjugate transpose $K\mapsto K^*$, which is the adjoint
$T\mapsto T^\dagger$ under the correspondence.

## Hilbert–Schmidt Operators

### The Isometry

**Definition.** An operator $T$ on $L^2(X,\mu)$ is **Hilbert–Schmidt** if it is the integral operator of a
kernel $K\in L^2(X\times X,\mu\otimes\mu)$, and the **Hilbert–Schmidt norm** is
$$
\lVert T_K\rVert_{\mathrm{HS}}=\lVert K\rVert_{L^2(X\times X)} .
$$

**Theorem (the correspondence is an isometry onto the Hilbert–Schmidt class).** The map $K\mapsto T_K$ is a
linear isometry of $L^2(X\times X)$ onto the class of Hilbert–Schmidt operators on $L^2(X)$, and the class is
a Hilbert space with the inner product
$$
\langle T_K,T_L\rangle_{\mathrm{HS}}=\iint K(x,y)\overline{L(x,y)}\,d\mu(x)d\mu(y) ;
$$
the correspondence carries the kernel involution to the adjoint, $T_{K^*}=T_K^\dagger$, so that it is a
$\ast$-isometry.

**Proof.** That the operator of an $L^2$ kernel is bounded and Hilbert–Schmidt is the computation of
$\lVert T_K\rVert_{\mathrm{HS}}^2=\iint\lvert K\rvert^2$ for an orthonormal basis, and the kernel is
recovered from the operator by the formula $K(x,y)=\sum_n(T_Ke_n)(x)\overline{e_n(y)}$ in the $L^2$ sense;
the inner product identity is the polarisation of the norm. The involution statement is the theorem of the
previous section. $\blacksquare$

**Forward reference.** The spectral theory of a Hermitian kernel — the reality of the spectrum, the
orthogonal eigenfunctions, the expansion of the kernel and Mercer's theorem — is the subject of
*Hermitian Integral Kernels*, the article of the `* Operator Theory` group that follows this one; it is the
operator theory built from the involution, and the present article supplies only the kernel, the involution
and the two conditions that it tests.

## The Kernel as the Symbol of the Operator

### The General Theorem

**Theorem (Schwartz kernel theorem, quoted).** Every bounded operator $T$ from $C_c^\infty(Y)$ to
$\mathcal D'(X)$ has a distribution kernel $K\in\mathcal D'(X\times Y)$ with
$$
\langle Tu,v\rangle=\langle K,v\otimes\bar u\rangle ,
$$
so that the operator is the integral operator of a distribution kernel; $T$ is self-adjoint exactly when the
kernel is Hermitian as a distribution, $K(x,y)=\overline{K(y,x)}$, and $T$ is positive exactly when the
kernel is positive definite as a distribution.

**Proof.** The existence and uniqueness of the kernel is the Schwartz kernel theorem of *The Schwartz Kernel
Theorem*, later in this Part; the identification of the Hermitian and positive conditions is the
distributional form of the computations of the previous sections, with the pairing of *Positive Definite
Distributions*, the previous article of this group. $\blacksquare$

The general bounded operator therefore has a kernel in the sense of distributions, and the kernel dictionary
of this article — the involution $K\mapsto K^*$ with the adjoint, the positive definite with the positive —
holds in the distributional generality; when the kernel is a function and the operator is Hilbert–Schmidt,
the isometry of the previous section identifies the two spaces.

### The Dictionary

**Theorem (the correspondence of structures).** Under the kernel-to-operator correspondence:

| Kernel | Operator |
|---|---|
| $K^*(x,y)=\overline{K(y,x)}$ | $T_K^\dagger$, the adjoint |
| $K$ Hermitian | $T_K$ self-adjoint |
| $K$ positive definite | $T_K$ positive |
| $K\in L^2(X\times X)$ | $T_K$ Hilbert–Schmidt |

and the correspondence is involution-preserving in each row; the last row is an isometry whose inverse is
the recovery of the kernel from the operator. The row that carries the spectral expansion of a Hermitian
kernel belongs to *Hermitian Integral Kernels*, later in this group.

**Proof.** The rows are the theorems of the previous sections; the Hilbert–Schmidt case is the isometry, and
the general rows are the distributional form. $\blacksquare$

## The Spectral Theory of the Hermitian Kernel

The operator theory built from the kernel involution — the self-adjointness of $T_K$, its compactness in the
Hilbert–Schmidt case, the reality of the eigenvalues, the orthogonal eigenfunctions, the expansion
$K(x,y)=\sum_n\lambda_n\varphi_n(x)\overline{\varphi_n(y)}$ with $\lambda_n\geq0$ exactly for a positive
definite kernel, the uniform convergence of the expansion for a continuous kernel (Mercer's theorem) and the
trace identities $\sum_n\lambda_n=\int K(x,x)\,d\mu$ and $\lVert K\rVert_{L^2}^2=\sum_n\lambda_n^2$ — is
*Hermitian Integral Kernels*, the article of the `* Operator Theory` group that follows this one, together
with the reproducing space $H_K$ of *Reproducing Kernel Hilbert Spaces*, the second article of this group.
This article has established the two conditions the spectral theory tests, the kernel involution that makes
the operator self-adjoint and the positive definiteness that makes it positive, and nothing more.

## Summary

The integral operator $(T_Kf)(x)=\int K(x,y)f(y)d\mu(y)$ has adjoint $T_K^\dagger=T_{K^*}$ with the
conjugate transpose kernel $K^*(x,y)=\overline{K(y,x)}$, so that the Hermitian kernels are exactly the
self-adjoint integral operators and the positive definite kernels exactly the positive ones; this is the
operator form of the involution of the `*` group, and it is the pair of conditions that the later spectral
theory tests. For kernels in $L^2(X\times X)$ the correspondence is an isometry onto the Hilbert–Schmidt
operators, with the inner product $\iint K\bar L$ and the norm $\lVert K\rVert_{L^2}$, and it is a
$\ast$-isometry for the kernel involution. The general bounded operator has a distribution kernel by the
Schwartz kernel theorem, and the same dictionary holds in the distributional generality, with the
involution $K\mapsto K^*$ matched to the adjoint. The spectral theory that the two conditions support — the
reality of the spectrum, the eigenfunction expansion, Mercer's theorem and the trace identities — is
*Hermitian Integral Kernels*, later in this group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T_K$, $K$ | Integral operator and its kernel, $(T_Kf)(x)=\int K(x,y)f(y)d\mu(y)$ |
| $K^*(x,y)=\overline{K(y,x)}$ | Conjugate transpose kernel |
| $T_K^\dagger=T_{K^*}$ | The adjoint is the conjugate transpose kernel |
| Hermitian / positive definite | $K^*=K$ / $\sum\overline{c_i}c_jK(x_i,x_j)\geq0$ |
| $\lVert T_K\rVert_{\mathrm{HS}}=\lVert K\rVert_{L^2}$ | Hilbert–Schmidt norm and isometry |
| $\langle T_K,T_L\rangle_{\mathrm{HS}}=\iint K\bar L$ | Hilbert–Schmidt inner product |

## Further Reading

- Frigyes Riesz and Béla Szőkefalvi-Nagy, *Functional Analysis* (Ungar, 1955; reprinted Dover, 1990), for the
  integral operators and the Hilbert–Schmidt class.
- Franco Smithies, *Integral Equations* (Cambridge University Press, 1958), for the kernel/operator
  correspondence.
- Nelson Dunford and Jacob T. Schwartz, *Linear Operators, Part II* (Interscience, 1963), for the
  Hilbert–Schmidt class and the adjoint.
- John B. Conway, *A Course in Functional Analysis* (2nd ed., Springer, 1990), for the integral operators and
  the Hilbert-space adjoint.
- Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics I: Functional Analysis* (Academic
  Press, 1980), for the Hilbert–Schmidt class and the adjoint.
- Kôsaku Yosida, *Functional Analysis* (6th ed., Springer, 1980), for the integral operators and the
  distributional kernel.
