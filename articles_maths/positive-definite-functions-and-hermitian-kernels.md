
# __Positive Definite Functions and Hermitian Kernels__

## Introduction

The involution of the algebra of functions is complex conjugation, and the structures that respect it are
the Hermitian and positive definite ones. A kernel $K$ on a set $X$ is **Hermitian** if it is unchanged by
the conjugate transpose, $K(x,y)=\overline{K(y,x)}$, and **positive definite** if every finite matrix
$(K(x_i,x_j))$ it produces is positive semidefinite,
$$
\sum_{i,j=1}^n\overline{c_i}c_jK(x_i,x_j)\geq0
$$
for all choices of points and coefficients. A function $\varphi$ on a group is positive definite when the
kernel $K(x,y)=\varphi(x-y)$ is, and the two notions are the two faces of one object: a positive definite
function is exactly a Hermitian positive definite kernel that is translation invariant. The central theorem
of the subject is **Bochner's theorem**: a continuous positive definite function on $\mathbb R^n$ is the
Fourier transform of a unique finite positive measure, so that positive definiteness is the same condition
as being the Fourier–Stieltjes transform of a measure, and the positive definite functions are the
characters of the group mixed by a positive weight.

This article is the first of the `*` group of *Foundations of Analysis*, and it fixes the notions for the
five that follow: the corresponding Hilbert space of a kernel (the next article), the Hermitian part of a
measure, the conjugate symmetry of the transform, the positive definite distributions, and the Hermitian
kernels of integral operators. Its prerequisites are *Measure Theory and Integration* for positive measures,
the Radon–Nikodym theorem, the decomposition of a complex measure and the properties of the integral, and
*Fourier Analysis on Euclidean Spaces* for the transform and the multiplication formula. The Riesz
representation theorem for positive linear functionals, which produces the measure of Bochner's theorem, is
that of *Measure Theory and Integration*; the inner product of a Hilbert space is the one fixed by
*Banach and Hilbert Spaces*, later in this Part, $\langle f,g\rangle=\int f\bar g$, linear in the first
argument. The general locally compact abelian group version of Bochner's theorem, the Gelfand–Raikov theorem
and the decomposition of the positive definite cone are the subject of *Harmonic Analysis on Groups*, in the
neighbouring category *Analysis on Groups* of this Part, and of *Positive Definite Functions and the
Gelfand–Raikov Theorem*; the present Article states the Euclidean theorem with proof sketch and the
group-theoretic version as a forward reference. The reproducing kernel Hilbert space of a positive definite
kernel is *Reproducing Kernel Hilbert Spaces*, the next article of this group. No geometry is invoked.

## Hermitian Kernels

### The Involution on Functions and Kernels

**Definition.** On the $\mathbb C$-vector space of functions on a set $X$ the **involution** is complex
conjugation, $f^{*}=\bar f$. It is conjugate-linear, involutive, $(f^{*})^{*}=f$, and multiplicative,
$(fg)^{*}=f^{*}g^{*}$. On the space of kernels $K:X\times X\to\mathbb C$ the induced involution is
$$
K^{*}(x,y)=\overline{K(y,x)} ,
$$
which is again conjugate-linear and involutive, $(K^{*})^{*}=K$; the star on the elements is the same star,
in the sense of *Conventions in Mathematics*: the involution of the function $\bar f$ and of the kernel on
the diagonal coincide, $K^{*}(x,x)=\overline{K(x,x)}$, and this is why the same mark is used. Both marks
coincide with the **notational convention** that the dagger is reserved for the adjoint of an operator,
$T^\dagger$, and the star for the involution on elements.

**Definition.** A kernel $K$ is **Hermitian** if $K^{*}=K$, that is,
$$
K(x,y)=\overline{K(y,x)}\quad\text{for all }x,y\in X .
$$
The **real part** of a kernel is $K_{\mathrm h}=\frac12(K+K^{*})$; it is Hermitian, and $K$ is Hermitian
exactly when $K=K_{\mathrm h}$, so that the Hermitian kernels are the fixed points of the involution, the
kernel analogue of the real functions.

### Positive Definite Kernels

**Definition.** A kernel $K:X\times X\to\mathbb C$ is **positive definite** (in the sense of the
kernel) if for every $n\geq1$, every $x_1,\dots,x_n\in X$ and every $c_1,\dots,c_n\in\mathbb C$,
$$
\sum_{i,j=1}^n\overline{c_i}c_jK(x_i,x_j)\geq0 ,
$$
equivalently if every finite matrix $(K(x_i,x_j))_{i,j=1}^n$ is Hermitian positive semidefinite; a
**positive definite function** on a group is a function $\varphi$ for which the kernel
$K(x,y)=\varphi(x-y)$ is positive definite.

**Theorem (positivity implies Hermitian).** Every positive definite kernel is Hermitian.

**Proof.** Take $n=2$, with points $x,y$ and coefficients $1,t$ for $t\in\mathbb C$; the condition is
$$
K(x,x)+\lvert t\rvert^2K(y,y)+\bar tK(x,y)+tK(y,x)\geq0
$$
for all $t$. The left side is a quadratic polynomial in $t,\bar t$ that is nonnegative for all $t$; varying
the argument of $t$ forces the two linear terms to be conjugates in the sense $K(y,x)=\overline{K(x,y)}$.
$\blacksquare$

**Theorem (Cauchy–Schwarz for a positive definite kernel).** For a positive definite kernel $K$,
$$
\lvert K(x,y)\rvert^2\leq K(x,x)\,K(y,y),\qquad K(x,x)\geq0 .
$$

**Proof.** The $1\times1$ matrix is $K(x,x)\geq0$. Applying the $2\times2$ condition to
$K$ with coefficients $\lambda,1$ and points $x,y$ gives
$\lvert\lambda\rvert^2K(x,x)+\bar\lambda K(x,y)+\lambda K(y,x)+K(y,y)\geq0$ for all $\lambda$; the
discriminant of this quadratic in $\lambda$ is $\lvert K(x,y)\rvert^2-K(x,x)K(y,y)$, and the
nonnegativity forces it to be at most zero. $\blacksquare$

**Remark.** The Hermitian and positive definite conditions are the kernel form of the operator conditions of
*Hermitian Kernels and the Integral Operator*, later in this group: a kernel is the Hermitian and positive
definite object on the elements, and the integral operator with that kernel is the self-adjoint and positive
operator. The dictionary is proved there.

## Positive Definite Functions

### Definition and Elementary Properties

**Definition.** Let $G$ be an abelian group written additively. A function $\varphi:G\to\mathbb C$ is
**positive definite** if
$$
\sum_{i,j=1}^n\overline{c_i}c_j\varphi(x_i-x_j)\geq0
$$
for all $n$, all $x_i\in G$ and all $c_i\in\mathbb C$; it is **Hermitian** if
$\varphi(-x)=\overline{\varphi(x)}$.

**Theorem (elementary properties).** For a positive definite function $\varphi$:
$$
\varphi(0)\geq0,\qquad \varphi(-x)=\overline{\varphi(x)},\qquad \lvert\varphi(x)\rvert\leq\varphi(0),
\qquad \varphi(x-x)=\overline{\varphi(x-x)} .
$$
If $\varphi(0)=0$ then $\varphi=0$; if $\varphi$ is not identically zero then $\varphi(0)>0$.

**Proof.** The first is the $1\times1$ case; the second is the Hermitian property of the kernel
$K(x,y)=\varphi(x-y)$ established above, which gives
$\varphi(x-y)=\overline{\varphi(y-x)}$ and hence $\varphi(-x)=\overline{\varphi(x)}$ at $y=0$; the third is
the Cauchy–Schwarz inequality applied to $K(x,0)=\varphi(x)$, $K(x,x)=\varphi(0)$ and $K(0,0)=\varphi(0)$.
$\blacksquare$

**Theorem (the correspondence).** A Hermitian function $\varphi$ on $G$ is positive definite if and only if
the kernel $K(x,y)=\varphi(x-y)$ is positive definite; the matching is a bijection between the positive
definite functions and the translation-invariant positive definite kernels on $G$.

**Proof.** The kernel $K(x,y)=\varphi(x-y)$ is translation invariant by construction, and its positive
definiteness is the displayed condition for $\varphi$; conversely a translation-invariant kernel is
determined by $\varphi(z)=K(z,0)$, and the Hermitian property of $K$ is the Hermitian property of $\varphi$.
$\blacksquare$

### Examples

**Example (characters and positive measures).** Let $\mu$ be a finite positive measure on the character
group $\widehat G$ of a group $G$ (on a finite abelian group, a positive measure on the finite set of
characters). Then
$$
\varphi(x)=\int_{\widehat G}\chi(x)\,d\mu(\chi)
$$
is positive definite, because for every finite collection
$$
\sum_{i,j}\overline{c_i}c_j\varphi(x_i-x_j)
=\int_{\widehat G}\Bigl\lvert\sum_ic_i\chi(x_i)\Bigr\rvert^2d\mu(\chi)\geq0 ,
$$
using $\chi(x_i-x_j)=\chi(x_i)\overline{\chi(x_j)}$. Every positive definite function of a finite abelian
group is of this form, with $\mu$ a finite measure on the finite set of characters; this is the finite
instance of Bochner's theorem.

**Example (the Gaussian and the characteristic functions).** On $\mathbb R$ the functions $e^{-\pi tx^2}$
for $t>0$ are positive definite, with the measure $\mu$ of density $\sqrt t\,e^{-\pi t\xi^2}$ in Bochner's
theorem below; more generally the characteristic function of any probability measure,
$\varphi(x)=\int e^{2\pi ix\xi}d\mu(\xi)$ with $\mu\geq0$ and $\mu(\mathbb R)=1$, is positive definite. A
function that is not Hermitian is not positive definite: the real cosine
$\cos(2\pi\xi_0x)=\frac12(e^{2\pi i\xi_0x}+e^{-2\pi i\xi_0x})$ is positive definite, with
$\mu=\frac12(\delta_{\xi_0}+\delta_{-\xi_0})$, while $\varphi(x)=e^{2\pi i\xi_0x}$ is Hermitian and positive
definite because it is a character, and a function such as $\mathrm i\sin(2\pi\xi_0x)$ fails the Hermitian
condition.

**Example (the point mass).** On a discrete group the function $\varphi=\mathbf 1_{\{0\}}$, equal to $1$ at
the identity and $0$ elsewhere, is positive definite, with the measure $\mu$ the normalised Haar measure of
the compact character group; on $\mathbb Z$ this is the constant measure $d\mu=d\theta$ on the circle, and
$\varphi(n)=\int_0^1e^{2\pi in\theta}d\theta=\delta_{n0}$. This is the positive definite function of the
regular representation, and its kernel is the identity kernel $K(x,y)=\mathbf 1_{\{x=y\}}$.

## Bochner's Theorem

### Statement

**Theorem (Bochner, Euclidean form).** A continuous function $\varphi:\mathbb R^n\to\mathbb C$ is positive
definite if and only if there is a unique finite positive measure $\mu$ on $\mathbb R^n$, with
$\mu(\mathbb R^n)=\varphi(0)$, such that
$$
\varphi(x)=\int_{\mathbb R^n}e^{2\pi ix\cdot\xi}\,d\mu(\xi)\qquad\text{for all }x\in\mathbb R^n .
$$
The measure $\mu$ is a probability measure exactly when $\varphi(0)=1$, and it is the
**Fourier–Stieltjes transform** (or spectral measure) of $\varphi$; the transform is written with the
positive exponent $e^{+2\pi ix\cdot\xi}$, so that it is the conjugate of the transform at $x$.

### Proof Sketch

**Proof sketch.** The easy direction is the computation of the example above: if
$\varphi(x)=\int e^{2\pi ix\cdot\xi}d\mu(\xi)$ with $\mu\geq0$, then
$\sum\bar c_ic_j\varphi(x_i-x_j)=\int\lvert\sum_ic_ie^{2\pi ix_i\cdot\xi}\rvert^2d\mu(\xi)\geq0$, and the
continuity is dominated convergence. For the converse, let $\varphi$ be continuous and positive definite,
with $\varphi(0)\geq0$, and consider the linear functional defined on the compactly supported continuous
functions by
$$
L(\psi)=\iint\varphi(x-y)\psi(x)\overline{\psi(y)}\,dx\,dy ;
$$
positive definiteness of $\varphi$ makes $L$ nonnegative on every $\psi=\sum c_ik_{\xi_i}$ and hence on all
of $C_c(\mathbb R^n)$, by density, and a standard polarisation recovers $L$ from the diagonal values
$L(\psi*\psi^{*})$. Since $\varphi$ is continuous and dominated by $\varphi(0)$, the functional $L$ is
bounded by $\varphi(0)\lVert\psi\rVert_1^2$ and extends to a finite positive measure by the Riesz
representation theorem of *Measure Theory and Integration* (the duality of $C_c$ and positive functionals).
The Fourier transform of this measure is then computed from $L$ by inserting $e^{2\pi ix\cdot\cdot}$, which
shows
$$
\varphi(x)=\int e^{2\pi ix\cdot\xi}\,d\mu(\xi) ;
$$
the uniqueness of $\mu$ is the injectivity of the Fourier–Stieltjes transform on finite measures, from the
multiplication formula. The details of the duality argument belong to *Measure Theory and Integration* and
to *Harmonic Analysis on Groups*, where the theorem is proved for a general locally compact abelian group.
$\blacksquare$

The proof of the converse is the only place where the Riesz representation of a positive functional on
$C_c$ is used, and it is quoted from *Measure Theory and Integration*. The reader should note that the
measure is produced from the functional, not observed directly; the theorem is therefore the statement that
the positive definite cone is the image of the positive cone of measures under the transform.

### Consequences

The theorem identifies four conditions on a continuous $\varphi$: positive definiteness, being a
Fourier–Stieltjes transform with a positive measure, being a positive linear functional on the convolution
algebra, and being the matrix of a positive operator on the characters. The consequences used later are the
following.

**Corollary (normalisation and products).** For a positive definite $\varphi$ the value $\varphi(0)$ is the
total mass $\mu(\mathbb R^n)$, and $\varphi$ is bounded with $\lvert\varphi\rvert\leq\varphi(0)$; the
product of two positive definite functions is positive definite, with the measure the convolution of the two
spectral measures; the conjugate $\bar\varphi$ and the reflection $x\mapsto\varphi(-x)$ are positive
definite, with the reflected measure.

**Proof.** The mass statement is the value at $0$; the bound is above; the product is
$\varphi\psi(x)=\iint e^{2\pi ix\cdot(\xi+\eta)}d\mu(\xi)d\nu(\eta)$, which is the transform of the
push-forward of $\mu\otimes\nu$ under addition, a positive measure; the conjugation and reflection are the
adjoint and the inverse of the transform on measures. $\blacksquare$

**Corollary (Bochner on a group, forward reference).** The same equivalence holds on a locally compact
abelian group, with the character group in place of $\mathbb R^n$ and the Haar measure in place of Lebesgue
measure, and it is the **Bochner theorem on groups**; the discrete group $\mathbb Z$, the circle, and the
finite abelian groups are the instances with the known transforms. The statement and proof are in
*Harmonic Analysis on Groups*, in *Analysis on Groups*, the neighbouring category of this Part; the
Gelfand–Raikov theorem, the refinement in which a positive definite function separates the points of the
group, is *Positive Definite Functions and the Gelfand–Raikov Theorem*.

## The GNS Construction and the Bridge to Hilbert Space

### The Kolmogorov Decomposition

**Theorem (the GNS decomposition of a positive definite kernel).** Let $K$ be a positive definite kernel on
a set $X$. Then there are a Hilbert space $H$ and a map $x\mapsto k_x$ of $X$ into $H$ with
$$
K(x,y)=\langle k_y,k_x\rangle
$$
for all $x,y$, and the $k_x$ span a dense subspace; the pair $(H,k_\bullet)$ is unique up to unitary
equivalence fixing every $k_x$. Conversely, for every map $k_\bullet:X\to H$ the kernel
$K(x,y)=\langle k_y,k_x\rangle$ is positive definite.

**Proof.** On the vector space of finite sums $\sum_ic_ik_{x_i}$ define
$$
\Bigl\langle\sum_ic_ik_{x_i},\sum_jd_jk_{x_j}\Bigr\rangle
=\sum_{i,j}c_i\overline{d_j}K(x_j,x_i) ;
$$
the positive definiteness of $K$ makes this a positive semidefinite Hermitian form, the Schwarz inequality
makes the null vectors a subspace, and the quotient completed in the induced norm is a Hilbert space $H$ in
which the classes of the $k_x$ satisfy $\langle k_y,k_x\rangle=K(x,y)$. The span is dense by construction,
and the uniqueness is that of a dense span in its completion. The converse is the computation of the
previous section. $\blacksquare$

The vectors $k_x$ are the **Kolmogorov vectors** of the kernel, and the construction is the
**Kolmogorov decomposition**; when the kernel is the reproducing kernel of a space of functions it produces
that space, which is the subject of *Reproducing Kernel Hilbert Spaces*, the next article of this group.

### The Positive Definite Cone

**Theorem.** The positive definite kernels on a fixed set $X$ form a convex cone closed under pointwise
limits: sums with nonnegative coefficients, products, and pointwise limits of positive definite kernels are
positive definite.

**Proof.** Sums and nonnegative coefficients are immediate from the defining inequality; the product
corresponds to the tensor product of the Kolmogorov spaces and the Hadamard product of Gram matrices, which
is positive semidefinite by the Schur product theorem; the pointwise limit is the limit of nonnegative
numbers. $\blacksquare$

## Summary

The involution $\bar f$ on functions induces the involution $K^{*}(x,y)=\overline{K(y,x)}$ on kernels; a
kernel is Hermitian when $K^{*}=K$ and positive definite when every finite matrix $(K(x_i,x_j))$ is
positive semidefinite, a condition that forces Hermitian and gives
$\lvert K(x,y)\rvert^2\leq K(x,x)K(y,y)$. A function $\varphi$ on a group is positive definite when the
translation-invariant kernel $K(x,y)=\varphi(x-y)$ is, and then $\varphi(0)\geq0$,
$\varphi(-x)=\overline{\varphi(x)}$ and $\lvert\varphi(x)\rvert\leq\varphi(0)$. Bochner's theorem states
that a continuous positive definite function on $\mathbb R^n$ is exactly the Fourier–Stieltjes transform
$\varphi(x)=\int e^{2\pi ix\cdot\xi}d\mu(\xi)$ of a unique finite positive measure of total mass
$\varphi(0)$, and the general locally compact abelian case, together with the Gelfand–Raikov theorem, is
that of *Harmonic Analysis on Groups* and of *Positive Definite Functions and the Gelfand–Raikov Theorem*.
Every positive definite kernel is the Gram kernel of a family of vectors in a Hilbert space, the Kolmogorov
decomposition, $K(x,y)=\langle k_y,k_x\rangle$; and the positive definite kernels form a cone closed under
sums, products and limits. The Hilbert space so produced, when the kernel is a reproducing one, is the
subject of the next article of this group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $f^{*}$, $K^{*}$ | Involution, $\bar f$; $K^{*}(x,y)=\overline{K(y,x)}$ |
| Hermitian | $K(x,y)=\overline{K(y,x)}$, the fixed points of the involution |
| positive definite | $\sum_{i,j}\overline{c_i}c_jK(x_i,x_j)\geq0$ for all finite data |
| $\varphi$ | Positive definite function, kernel $\varphi(x-y)$ |
| $\mu$ | The spectral measure of Bochner's theorem, $\mu(\mathbb R^n)=\varphi(0)$ |
| $\chi$ | Character of the group |
| $k_x$, $\langle k_y,k_x\rangle=K(x,y)$ | Kolmogorov vectors and decomposition |
| $K_{\mathrm h}$ | Hermitian part $\frac12(K+K^{*})$ |

## Further Reading

- Salomon Bochner, *Lectures on Fourier Integrals* (Princeton University Press, 1959), for Bochner's
  theorem in its original setting.
- Walter Rudin, *Fourier Analysis on Groups* (Interscience, 1962), for the positive definite functions, the
  Fourier–Stieltjes transform and the group form of Bochner's theorem.
- Saburou Saitoh, *Theory of Reproducing Kernels and its Applications* (Longman, 1988), for the
  Kolmogorov decomposition and the correspondence with Hilbert spaces of functions.
- Zoltán Sasvári, *Positive Definite and Definitizable Functions* (Akademie Verlag, 1994), for the positive
  definite cone and its integral representations.
- Christian Berg, Jens Peter Reus Christensen and Paul Ressel, *Harmonic Analysis on Semigroups* (Springer,
  1984), for positive definite functions and kernels on semigroups and their applications.
- Nachman Aronszajn, *Theory of Reproducing Kernels* (Transactions of the American Mathematical Society 68,
  1950), for the correspondence between positive definite kernels and Hilbert spaces of functions.
