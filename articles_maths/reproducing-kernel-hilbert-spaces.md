
# __Reproducing Kernel Hilbert Spaces__

## Introduction

A Hilbert space whose elements are functions may or may not allow the value of a function at a point to be
recovered from the function by an inner product. When it does — when evaluation at every point is a
continuous linear functional — the space is called a **reproducing kernel Hilbert space**, and the Riesz
representation of the evaluation functionals gives a function $K$ of two variables, the **reproducing
kernel**, from which the space may be reconstructed: $K(x,y)$ is the value at $x$ of the vector representing
the evaluation at $y$, and the reproducing property $f(x)=\langle f,k_x\rangle$ holds for every element.
The theorem of Aronszajn is that this correspondence is a bijection: a kernel is a reproducing kernel for
one and only one space of this kind exactly when it is positive definite in the sense of the previous
article. The space is thus the Hilbert space that a positive definite kernel carries, and the kernel is the
concrete carrier of the involution and the positivity of the previous article: the same object read as an
inner product.

This article is the second of the `*` group of *Foundations of Analysis*. Its prerequisites are *Measure
Theory and Integration* for the $L^2$ spaces and the integral, and *Positive Definite Functions and
Hermitian Kernels*, the previous article of this group, for the Hermitian and positive definite conditions
and the Kolmogorov decomposition. The Hilbert-space vocabulary — inner product, completion, closed subspace,
Riesz representation, orthonormal basis — is quoted as it is used from *Banach and Hilbert Spaces*, later in
this Part, where it is developed; the construction of the space from the kernel is carried out concretely,
so that the article depends on the Riesz theorem only for the converse direction, and the reader may read
the construction as the positive definite case of the Kolmogorov decomposition of the previous article. The
kernel and the integral operator it defines are *Hermitian Kernels and the Integral Operator*, later in this
group. The connection with the classical spaces of complex analysis — the Hardy, Bergman and Fock spaces —
is named only, and belongs to the complex analysis of the later Parts. No geometry is invoked.

## Hilbert Spaces of Functions with Continuous Evaluation

### The Definition

**Definition.** Let $X$ be a set. A **Hilbert space of functions on $X$** is a Hilbert space $H$ whose
elements are functions on $X$ and in which the vector operations are the pointwise operations. The space
$H$ has **continuous evaluation** at $x\in X$ if the evaluation functional
$$
\operatorname{ev}_x:H\to\mathbb C,\qquad \operatorname{ev}_x(f)=f(x),
$$
is bounded; that is, if there is $C_x$ with $\lvert f(x)\rvert\leq C_x\lVert f\rVert$ for all $f\in H$.
The space is a **reproducing kernel Hilbert space** if it has continuous evaluation at every point of $X$.

**Example.** The space $L^2(\mathbb R)$ is not a reproducing kernel Hilbert space: its elements are classes
of functions, and the value at a point is not defined for a general element; even after a choice of
representative, evaluation is not continuous, as the translates of a fixed bump function show. The finite
dimensional space $\mathbb C^n$ with the Euclidean inner product, considered as functions on
$X=\{1,\dots,n\}$, is a reproducing kernel Hilbert space, and so is $\ell^2(\mathbb N)$ with $X=\mathbb N$
countably infinite.

### The Reproducing Kernel

**Theorem (the kernel from the space).** Let $H$ be a reproducing kernel Hilbert space on $X$. For each
$x$ let $k_x\in H$ be the Riesz representer of the evaluation at $x$, so that
$$
f(x)=\langle f,k_x\rangle\qquad\text{for all }f\in H ,
$$
and define $K(x,y)=k_y(x)$. Then $K$ is a Hermitian positive definite kernel, it is the **reproducing
kernel** of $H$, and
$$
K(x,y)=\langle k_y,k_x\rangle ,
$$
so that the kernel is the Gram matrix of the representers. The span of the $k_x$ is dense in $H$.

**Proof.** The existence and uniqueness of $k_x$ are the Riesz representation theorem, applicable because
evaluation is bounded, in *Banach and Hilbert Spaces*, later in this Part. The reproducing property gives
$k_y(x)=\langle k_y,k_x\rangle$ and hence $K(x,y)=\langle k_y,k_x\rangle$; the kernel is Hermitian because
$\overline{K(y,x)}=\overline{\langle k_x,k_y\rangle}=\langle k_y,k_x\rangle=K(x,y)$, and positive definite
because $\sum_{i,j}\overline{c_i}c_jK(x_i,x_j)=\lVert\sum_ic_ik_{x_i}\rVert^2\geq0$. If $g$ is orthogonal
to every $k_x$ then $g(x)=\langle g,k_x\rangle=0$ for every $x$, so $g=0$ and the span is dense.
$\blacksquare$

The identity $\|k_x\|^2=\langle k_x,k_x\rangle=K(x,x)$ gives the bound the continuous evaluation requires,
$$
\lvert f(x)\rvert=\lvert\langle f,k_x\rangle\rvert\leq\lVert f\rVert\sqrt{K(x,x)} .
$$
The function $k_x$ is the **kernel vector** at $x$, and when the kernel is written as a function of two
variables, $k_x(\cdot)=K(\cdot,x)$; this is the same convention as in the previous article,
$K(x,y)=\langle k_y,k_x\rangle$, and the same vectors, ordered with the second index first inside the inner
product.

## The Aronszajn Construction

### From a Positive Definite Kernel to a Space

**Theorem (construction).** Let $K$ be a positive definite kernel on $X$. Define $H_0$ to be the vector
space of finite linear combinations $f=\sum_ic_ik_{x_i}$ of symbols $k_x$, one for each $x\in X$, with the
pairing
$$
\Bigl\langle\sum_ic_ik_{x_i},\sum_jd_jk_{x_j}\Bigr\rangle
=\sum_{i,j}c_i\overline{d_j}\,K(x_j,x_i).
$$
Then the pairing is a positive semidefinite Hermitian form; its null space $N=\{f\in H_0:\langle f,f\rangle=0\}$
is a subspace; the quotient $H_0/N$ completed in the induced norm is a Hilbert space $H_K$ in which the
class of $k_x$ is a function on $X$ by $k_x(y)=K(y,x)$; and the reproducing property
$$
f(x)=\langle f,k_x\rangle
$$
holds for every $f\in H_K$.

**Proof.** The form is Hermitian conjugate-symmetric by the change of index, and positive semidefinite
because for $d_j=c_j$ it equals $\sum_{i,j}c_i\overline{c_j}K(x_j,x_i)$, which relabels to
$\sum_{i,j}\overline{c_i}c_jK(x_i,x_j)\geq0$. The Cauchy–Schwarz inequality $\lvert\langle f,g\rangle\rvert^2\leq\langle f,f\rangle\langle g,g\rangle$
for a semidefinite form shows that the null vectors form a subspace and that the form descends to the
quotient; the quotient is an inner product space whose completion is $H_K$. In the quotient the assignment
$k_x\mapsto K(\cdot,x)$ is well defined: if $k_x-k_y\in N$ then
$\langle k_x-k_y,k_z\rangle=K(z,x)-K(z,y)=0$ for every $z$, and $K(\cdot,x)=K(\cdot,y)$ as functions
because $K$ is positive definite and hence Hermitian. The reproducing property holds on $H_0$ by the
definition of the form and extends to the completion by continuity, the map $f\mapsto f(x)=\langle f,k_x\rangle$
being continuous in $f$. $\blacksquare$

**Theorem (uniqueness).** If $H$ and $H'$ are two reproducing kernel Hilbert spaces on $X$ with the same
kernel $K$, then the map $k_x\mapsto k_x'$ extends to a unique isometric isomorphism $H\to H'$ carrying each
$k_x$ to $k_x'$; in particular the space $H_K$ of the construction is the unique reproducing kernel Hilbert
space with kernel $K$.

**Proof.** The linear map defined on $H_0$ by $\sum c_ik_{x_i}\mapsto\sum c_ik_{x_i}'$ preserves the inner
product, since both are given by the same kernel values $K(x_j,x_i)$; it therefore extends by continuity and
density to an isometry, and the isometry is onto because the image contains the dense span of the $k_x'$.
$\blacksquare$

### Aronszajn's Theorem

**Theorem (Aronszajn).** The map $K\mapsto H_K$ is a bijection between the positive definite kernels on a
set $X$ and the reproducing kernel Hilbert spaces on $X$, up to isometry fixing each kernel vector; the
inverse map is $H\mapsto\langle k_y,k_x\rangle$ of the preceding section.

**Proof.** Given $H$, the kernel $K(x,y)=\langle k_y,k_x\rangle$ is positive definite and $H$ reproduces it.
Given $K$, the construction produces $H_K$, whose kernel is $K$ again: the kernel of $H_K$ is
$\langle k_y,k_x\rangle=K(x,y)$. The uniqueness is the theorem above. $\blacksquare$

Thus positive definite kernels and reproducing kernel spaces are the same data, and the previous article's
Kolmogorov decomposition is exactly this construction: the Kolmogorov vectors are the kernel vectors
$k_x$, and the abstract Hilbert space they span is realised here as a space of functions by the reading
$k_x=K(\cdot,x)$.

## Examples

**Example (finite and countable sets).** For $X=\{1,\dots,n\}$ every positive semidefinite matrix
$K=(K_{ij})$ is a reproducing kernel, and $H_K\subseteq\mathbb C^n$; when $K$ is invertible the inner
product is $\langle u,v\rangle_K=\sum_{ij}(K^{-1})_{ij}u_i\overline{v_j}$, and when $K$ is the identity the
space is $\mathbb C^n$ with its Euclidean inner product and $k_i=e_i$. For $X=\mathbb N$ and the identity
kernel the space is $\ell^2$, with $k_n=e_n$.

**Example (the Sobolev space with one boundary condition).** On $X=[0,1]$ let
$\langle f,g\rangle=\int_0^1f'(t)\overline{g'(t)}\,dt$ on the functions with $f(0)=0$ and square-integrable
derivative. The kernel is
$$
K(x,y)=\min(x,y),
$$
and the reproducing property is exact: $\partial_y\min(x,y)=\mathbf 1_{\{y<x\}}$ away from $y=x$, so
$$
\langle f,K(\cdot,x)\rangle=\int_0^1f'(y)\mathbf 1_{\{y<x\}}\,dy=f(x)-f(0)=f(x) .
$$
The space $H_K$ is the completion, consisting of absolutely continuous functions vanishing at $0$ with
square-integrable derivative. The kernel $\min(x,y)$ is positive definite on $[0,1]$, its finite matrices
$(\min(x_i,x_j))$ being positive semidefinite, and it is the Green's function of $-\frac{d^2}{dt^2}$ on
$[0,1]$ with the Dirichlet condition at the left endpoint.

**Example (the trigonometric polynomials and the Dirichlet kernel).** Let $H_N$ be the space of
trigonometric polynomials of degree at most $N$ under the $L^2(\mathbb T)$ inner product. Every element is
continuous, so evaluation is bounded, and the reproducing kernel is the **Dirichlet kernel**
$$
K(x,y)=D_N(x-y)=\sum_{m=-N}^Ne^{2\pi im(x-y)},
$$
with the reproducing property $f(x)=\int_{\mathbb T}f(y)\overline{D_N(x-y)}\,dy$. This is the kernel of the
orthogonal projection onto $H_N$ in $L^2(\mathbb T)$, and it exhibits the general fact that the reproducing
kernel of a closed subspace of $L^2$ with continuous evaluation is the integral kernel of the orthogonal
projection onto it.

**Example (the Hardy, Bergman and Fock spaces).** On the unit disc the Hardy space $H^2(\mathbb D)$ of
square-summable power series has reproducing kernel $K(z,w)=(1-z\bar w)^{-1}$, the Bergman space
$A^2(\mathbb D)$ has $K(z,w)=(1-z\bar w)^{-2}$, and the Fock space of entire functions with Gaussian weight
has $K(z,w)=e^{z\bar w}$; on $\mathbb R$ the space of entire functions with the Gaussian kernel
$e^{-\pi(x-y)^2}$ is the Segal–Bargmann space. These spaces and their kernels belong to the complex analysis
and the operator theory of the later Parts, and are recorded here as instances of the correspondence.

## Properties of the Space

**Theorem (pointwise bounds and convergence).** In a reproducing kernel Hilbert space with kernel $K$,
$$
\lvert f(x)\rvert\leq\lVert f\rVert\sqrt{K(x,x)} ,
$$
and if $f_n\to f$ in norm then $f_n\to f$ pointwise, uniformly on every set on which $K(x,x)$ is bounded. The
convergence of a norm-bounded sequence in a dense subset to a pointwise limit is pointwise convergence to the
limit in $H$.

**Proof.** The bound is the identity $f(x)=\langle f,k_x\rangle$ and Cauchy–Schwarz with
$\lVert k_x\rVert^2=K(x,x)$; the convergence is the bound applied to $f_n-f$. $\blacksquare$

**Theorem (the kernel of a subspace).** If $H_1\subseteq H_2$ are reproducing kernel Hilbert spaces on $X$
with the same inner product, with kernels $K_1,K_2$, then $K_2-K_1$ is a positive definite kernel, and it is
the reproducing kernel of the orthogonal complement $H_2\ominus H_1$ whenever that complement has continuous
evaluation.

**Proof.** For each $x$ the projection $Pk^2_x$ of the kernel vector of $H_2$ at $x$ onto $H_1$ is the
representer in $H_1$ of the evaluation at $x$, hence equals $k^1_x$; therefore the vector
$k^2_x-k^1_x$ lies in the complement and
$\langle k^2_y-k^1_y,k^2_x-k^1_x\rangle=K_2(x,y)-K_1(x,y)$, which is positive definite as a Gram kernel.
$\blacksquare$

## The Kernel and the Integral Operator

**Theorem (finite and countable case).** Let $X$ be a finite or countable set with counting measure and let
$K$ be a Hermitian kernel on $X$. Then $K$ is positive definite if and only if the integral operator $T_K$
is positive,
$$
\langle T_Kf,f\rangle=\sum_{i,j}\overline{f_i}f_jK(i,j)\geq0
$$
for every finitely supported $f$. A positive definite kernel is therefore exactly a Hermitian kernel whose
operator is positive.

**Proof.** The displayed identity is the definition of $T_K$ in the countable case; the positivity of $K$
and of $T_K$ are the same condition. The general measure-theoretic statement — a kernel is positive definite
exactly when its integral operator is self-adjoint and positive — is *Hermitian Kernels and the Integral
Operator*, later in this group, where the operator and the kernel are matched. $\blacksquare$

## Summary

A reproducing kernel Hilbert space is a Hilbert space of functions in which evaluation at every point is a
bounded linear functional; the Riesz representers $k_x$ of the evaluations define the reproducing kernel
$K(x,y)=k_y(x)=\langle k_y,k_x\rangle$, a Hermitian positive definite kernel, and satisfy the reproducing
property $f(x)=\langle f,k_x\rangle$ with the bound $\lvert f(x)\rvert\leq\lVert f\rVert\sqrt{K(x,x)}$.
Aronszajn's theorem reverses the direction: every positive definite kernel is the reproducing kernel of one
and only one such space, constructed as the completion of the span of the kernel vectors $k_x=K(\cdot,x)$
under the pairing $\langle k_x,k_y\rangle=K(y,x)$, and the Kolmogorov decomposition of the previous article
is exactly this construction. The examples include the finite-dimensional spaces, the Sobolev space
$H^1_0$ with kernel $\min(x,y)$, the trigonometric polynomials with the Dirichlet kernel, and the Hardy,
Bergman, Fock and Segal–Bargmann spaces. In a reproducing kernel Hilbert space norm convergence implies
pointwise convergence, and inside $L^2$ the kernel is the integral kernel of the orthogonal projection onto
the space; that operator reading is completed in *Hermitian Kernels and the Integral Operator*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{ev}_x$ | Evaluation functional, $\operatorname{ev}_x(f)=f(x)$ |
| $k_x$ | Kernel vector, Riesz representer of $\operatorname{ev}_x$ |
| $K(x,y)=k_y(x)=\langle k_y,k_x\rangle$ | Reproducing kernel |
| $f(x)=\langle f,k_x\rangle$ | Reproducing property |
| $H_K$ | The reproducing kernel Hilbert space of $K$ |
| $\lvert f(x)\rvert\leq\lVert f\rVert\sqrt{K(x,x)}$ | Pointwise bound |
| $D_N$ | Dirichlet kernel $\sum_{\lvert m\rvert\leq N}e^{2\pi im(\cdot)}$ |

## Further Reading

- Nachman Aronszajn, *Theory of Reproducing Kernels* (Transactions of the American Mathematical Society 68,
  1950), for the fundamental theorem and the properties of the space.
- Saburou Saitoh, *Theory of Reproducing Kernels and its Applications* (Longman, 1988), for the applications
  and the integral-operator reading.
- N. Aronszajn and K. T. Smith, *Functional Spaces and Functional Completion* (Annales de l'Institut
  Fourier 6, 1956), for the completion and the kernel of a subspace.
- Alain Berlinet and Christine Thomas-Agnan, *Reproducing Kernel Hilbert Spaces in Probability and
  Statistics* (Kluwer, 2004), for the role of the reproducing kernel in the modern theory.
- Vladimir I. Paulsen and Mrinal Raghupathi, *An Introduction to the Theory of Reproducing Kernel Hilbert
  Spaces* (Springer, 2016), for a complete modern treatment.
- John B. Conway, *A Course in Functional Analysis* (2nd ed., Springer, 1990), for the Hilbert-space theory
  on which the Riesz representation step depends.
