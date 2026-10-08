
# __The Dirac Operator__

## Introduction

This article treats the operator of Clifford analysis as an operator. The setting is a Clifford
module $\mathcal{S}$ over the Clifford algebra $A=\mathrm{Cl}_{0,m}$ of a negative-definite
quadratic space of dimension $m$, the variable ranges over the vector subspace
$\mathbb{R}^{m+1}=\operatorname{span}(1,e_1,\dots,e_m)$ of $A$, and the operator is

$$
D = \partial_0+\sum_{i=1}^{m}e_i\,\partial_i = \sum_{\mu=0}^{m}e_\mu\,\partial_\mu , \qquad e_0=1 ,
$$

acting on the smooth $\mathcal{S}$-valued functions of the variable by the one-sided Clifford action
on the values. The corpus names this operator the **Cauchy–Riemann operator** — it is the operator
of *Clifford Analysis*, of *Regularity and the Cauchy–Riemann Operator* and of *Hypercomplex
Analysis* — and the classical name *Dirac operator* belongs in the corpus to the self-adjoint family
of *Dirac Differential Operators*. The entry is titled *The Dirac Operator* because the menu fixes
the title; this article reads the Clifford-analytic operator $D$ at its own layer, and the
reconciliation of the two names is stated once in the Remark below.

What the article establishes is the operator layer of the theory and nothing else: the definition of
$D$ on a Clifford module, its symbol, its ellipticity, its divergence form, the factorisation of the
Laplacian by its square, the failure of symmetry that a single scalar coefficient causes, the
description of its kernel — the monogenic functions — through the fundamental solution, and the way
$D$ organises the polynomials of the theory. The function-theoretic theorems themselves are
*Clifford Analysis*'s: the Cauchy–Pompeiu and Cauchy formulae, the harmonicity, the mean value
property and the Fischer decomposition are cited there and are not reproduced. The twisted operator
on a Clifford module over a manifold and the elliptic complex it defines are *Clifford Modules and
the Twisted Cauchy–Riemann Operator*; the integral operator built from the Cauchy kernel is *The
Cauchy Integral Operator*, next in this category; the projection that the Fischer decomposition
realises is *The Fischer Operator*; and the operators on a Clifford module as such — the Clifford
multiplication and its intertwiners — are *Operators on a Clifford Module*. The operator as an
algebraic and topological object, with the adjoint that the module form supplies, is Part II's
*Dirac Operators with Hermitian Adjoint*, and the analytic theory of the self-adjoint family is
*Dirac Differential Operators*; both are cited and neither is repeated.

## The Operator

### Definition

**Definition.** Let $A=\mathrm{Cl}_{0,m}$ be the Clifford algebra of a real vector space with basis
$e_1,\dots,e_m$ and quadratic form $q(\sum_ix_ie_i)=-\sum_ix_i^2$, so that

$$
e_ie_j+e_je_i=-2\delta_{ij} ,
$$

and let $\mathcal{S}$ be a left Clifford module over $A$ — the algebra itself in the classical
scalar case, an irreducible spinor module in the module case of *Spin Representations and Clifford
Modules with Inner Conjugation*. The **operator** of this article acts on a $C^1$ function
$f:\Omega\to\mathcal{S}$ on an open set $\Omega\subseteq\mathbb{R}^{m+1}$ by

$$
(Df)(x) = \sum_{\mu=0}^{m}e_\mu\,\partial_\mu f(x) ,
$$

the coefficient $e_\mu$ acting on the value by the module action and the derivative acting on the
component functions. The tuple $(e_0,e_1,\dots,e_m)$ with $e_0=1$ is the **frame** of the operator
in the sense of *Regularity and the Cauchy–Riemann Operator*.

**Definition.** The **conjugate operator** is

$$
\bar D = \partial_0-\sum_{i=1}^{m}e_i\,\partial_i ,
$$

and the two are related by the Clifford conjugation $x^{\natural}=x_0-\sum_{i\ge1}x_ie_i$ extended
to $A$ as the anti-automorphism with $(uv)^{\natural}=v^{\natural}u^{\natural}$.

**Remark (the two names, reconciled).** The operator $D$ is the Cauchy–Riemann operator of the
corpus; the name *Dirac operator* is the classical name of the operator $\sum_\mu e_\mu\partial_\mu$
in the literature, and the corpus reserves it for the self-adjoint family $\sum_jc(e_j)\nabla_{e_j}$
of *Dirac Differential Operators*. The two are not the same operator: the family of that article has
all its coefficients skew for the fibre metric, while $D$ carries the single Hermitian coefficient
$e_0=1$, which is the origin of the failure of symmetry recorded below. The present article uses the
symbol $D$ throughout and the name *Dirac operator* only in its title and in this remark. That $D$
and the self-adjoint vector operator $\sum_{i\ge1}e_i\partial_i$ are the two faces of one
factorisation of the Laplacian is stated in *Dirac Differential Operators*.

### The Symbol and Ellipticity

**Definition.** The **principal symbol** of $D$ is the map $\sigma:\mathbb{R}^{m+1}\to A$,

$$
\sigma(\xi) = \sum_{\mu=0}^{m}e_\mu\,\xi_\mu ,
$$

and the **reflected symbol** is
$\bar\sigma(\xi)=\sum_\mu \bar e_\mu\xi_\mu=\xi_0-\sum_{i\ge1}e_i\xi_i$.

**Proposition (invertibility of the symbol).** For every $\xi\neq0$,

$$
\sigma(\xi)\,\bar\sigma(\xi) = \bar\sigma(\xi)\,\sigma(\xi) = |\xi|^2 = \xi_0^2+\sum_{i=1}^{m}\xi_i^2 > 0 ,
$$

so $\sigma(\xi)$ is a unit of $A$, with $\sigma(\xi)^{-1}=\bar\sigma(\xi)/|\xi|^2$, and $D$ is
**elliptic**.

*Proof.* Expanding the product, the diagonal terms contribute $\sum_\mu e_\mu\bar e_\mu\xi_\mu^2$.
For $\mu=0$, $e_0\bar e_0=1$; for $\mu=i\ge1$, $e_i\bar e_i=-e_i^2=1$. Hence every diagonal term is
$\xi_\mu^2$. The off-diagonal terms cancel pairwise, because $\xi_\mu\xi_\nu$ is a real scalar and
$e_\mu\bar e_\nu+\bar e_\nu e_\mu=0$ for $\mu\neq\nu$, this being the Clifford relation
$e_\mu e_\nu+e_\nu e_\mu=-2\delta_{\mu\nu}$ after the sign $\bar e_\nu=\epsilon_\nu e_\nu$ with
$\epsilon_0=1$, $\epsilon_i=-1$. The value $|\xi|^2$ is a positive real number, hence a unit of $A$,
and the displayed inverse is immediate. The computation is identical in the other order because
$\xi_0$ is central and the two factors commute. $\square$

**Corollary.** The equality $D\bar D=\bar DD=\Delta$ holds, $\Delta=\sum_{\mu=0}^{m}\partial_\mu^2$
being the Laplacian of the ambient space, and $D$ is a first-order elliptic operator with constant
coefficients.

*Proof.* Applying the symbol computation to the covector $i\xi$ and separating orders gives the
operator identity; equivalently, expand $D\bar D$ directly as in *Regularity and the Cauchy–Riemann
Operator*. $\square$

### Divergence Form

**Proposition (divergence form).** Because the coefficients are constant,

$$
Df = \sum_{\mu=0}^{m}\partial_\mu\bigl(e_\mu f\bigr) ,
$$

so $D$ is the divergence of the $A$-valued field with components $e_\mu f$, and the divergence
theorem applies to it directly. For a domain $\Omega$ with smooth boundary and outward unit normal
$\nu$, the **conormal element** is

$$
\nu_B = \sum_{\mu=0}^{m}\nu_\mu\,e_\mu \in A .
$$

*Proof.* The derivative of a constant times a function is the constant times the derivative, and
$\partial_\mu(e_\mu f)=e_\mu\partial_\mu f$. $\square$

## The Square and the Failure of Symmetry

### The Factorisation of the Laplacian

**Theorem.** $D\bar D=\bar DD=\Delta$; every solution of $Df=0$ or of $fD=0$ is harmonic
componentwise, hence real-analytic.

*Proof.* The first statement is the Corollary above. For the second, if $Df=0$ then
$\Delta f=\bar DDf=0$, and the components of a harmonic function are real-analytic by the classical
theory; the Weyl lemma and the identity theorem are stated in *Regularity and the Cauchy–Riemann
Operator*. $\square$

### The Adjoint and the Split into Hermitian Parts

The operator is read with the module form of Part II, so let $(\cdot,\cdot)$ be a Hermitian form on
$\mathcal{S}$ for which the Clifford coefficients are skew, $(e_iv,w)=-(v,e_iw)$ for $i\ge1$; the
form exists on a Hermitian Clifford module and is the one of *Hermitian Modules over a Hermitian
Algebra with Hermitian Adjoint*. The adjoint of an operator is taken with respect to it, as in *The
Adjoint of the One-Sided Action with Hermitian Adjoint*.

**Proposition (the adjoint of $D$).** On compactly supported smooth functions,

$$
D^{*} = -\partial_0+\sum_{i=1}^{m}e_i\partial_i = -\bar D .
$$

*Proof.* The Clifford coefficients $e_i$ for $i\ge1$ are skew for the module form, so $e_i^{*}=-e_i$
under the adjoint of the one-sided action, while the scalar coefficient $e_0=1$ is Hermitian,
$e_0^{*}=e_0$; the coordinate derivative satisfies $\partial_\mu^{*}=-\partial_\mu$ on compactly
supported functions. Reversing the factors in the adjoint of a product,
$(e_\mu\partial_\mu)^{*}=\partial_\mu^{*}e_\mu^{*}=(-\partial_\mu)e_\mu^{*}$, which is $-\partial_0$
for $\mu=0$ and $+e_i\partial_i$ for $\mu=i\ge1$. Summing over $\mu$ gives
$D^{*}=-\partial_0+\sum_{i\ge1}e_i\partial_i=-\bar D$. $\square$

**Corollary (the operator is not symmetric).** $D$ satisfies $D^{*}=-\bar D$, so $D$ is symmetric
only if $D=-\bar D$, that is only if $\partial_0=0$; on the full space of functions $D$ is neither
symmetric nor normal. Its **self-adjoint part** is the vector operator
$D_{\mathrm{sa}}=\tfrac12(D-D^{*})=\sum_{i\ge1}e_i\partial_i$, and its **skew-adjoint part** is
$\partial_0$. The factorisation of the Laplacian can be read through the split: $D\bar D=\Delta$ is
the product of two distinct operators, while $D_{\mathrm{sa}}^2=-\Delta$ is the square of one
self-adjoint operator.

*Proof.* The split is immediate from the Proposition. For the square, $D_{\mathrm{sa}}$ has all
coefficients skew, so expanding $D_{\mathrm{sa}}^2$ gives
$\sum_{i,j}e_ie_j\partial_i\partial_j =-\sum_i\partial_i^2=-\Delta$. $\square$

**Remark (the two factorisations, and which article owns which).** The operator $D_{\mathrm{sa}}$
and its spectral theory belong to *Dirac Differential Operators*; the present article records the
split and the factorisations, and does not develop the spectrum. In the complex case $m=1$, where
$A\cong\mathbb{C}$, the split degenerates: $D_{\mathrm{sa}}=e_1\partial_1$ and $\partial_0$ are the
two halves of the classical Cauchy–Riemann operator, and their sum is the holomorphic operator on
the one hand and its conjugate on the other.

### The Kernel and the Fundamental Solution

**Definition.** A $C^1$ function $f$ is **left monogenic** (left regular) if $Df=0$, and **right
monogenic** if $fD=0$; for $m=1$ the two notions coincide. The left monogenic functions form a real
vector space closed under right multiplication by constants; the class is not closed under products,
which is the non-commutative obstruction of *Hypercomplex Analysis*.

**Theorem (the fundamental solution).** Let $\Phi$ be a fundamental solution of the Laplacian,
$\Delta\Phi=\delta_0$ in the sense of distributions, and put

$$
E = \bar D\Phi .
$$

Then $DE=\delta_0$; explicitly

$$
E(x) = \frac{1}{\omega_m}\frac{x^{\natural}}{|x|^{m+1}} , \qquad
\omega_m = |S^m| = \frac{2\pi^{(m+1)/2}}{\Gamma\bigl(\frac{m+1}{2}\bigr)} ,
$$

and $E(x-y)$ is the **Cauchy kernel** of the theory.

*Proof.* $DE=D\bar D\Phi=\Delta\Phi=\delta_0$. The explicit computation of $\bar D\Phi$ for the
radially symmetric fundamental solution of the Laplacian produces the displayed homogeneity and the
constant $\omega_m$, as in *Clifford Analysis*. $\square$

**Remark (normalisation and the operator).** The normalisation in the theorem is fixed by the flux
of $E$ through a small sphere, and it is the reason the operator $D$ and the kernel $E$ are
reciprocal: $E$ is what the conjugate operator does to the Laplacian kernel, and the pair $(D,E)$ is
the pair (operator, fundamental solution) of the divergence theorem. The Cauchy–Pompeiu and Cauchy
formulae built on this kernel are *Clifford Analysis*'s, and the operator-theoretic reading of them
is *The Cauchy Integral Operator*.

## The Organisation of the Polynomials

The homogeneous polynomials of the theory are organised by the operator through the Fischer
decomposition, which the next article reads as an operator statement; here the part that belongs to
$D$ is recorded.

**Definition.** A **solid spherical monogenic** of degree $k$ is a left monogenic polynomial
$P:\mathbb{R}^{m+1}\to\mathcal{S}$ homogeneous of degree $k$; the space of these is $\mathcal{M}_k$,
and $\mathcal{P}_k$ denotes the space of all $\mathcal{S}$-valued homogeneous polynomials of degree
$k$.

**Lemma (Fischer, monogenic form; standard).** For every $k\ge1$ the operator
$D:\mathcal{P}_k\to \mathcal{P}_{k-1}$ is surjective, and left multiplication by $x^{\natural}$ maps
$\mathcal{P}_{k-1}$ injectively with image meeting $\mathcal{M}_k$ only at $0$.

**Theorem (Fischer decomposition).** For every $k\ge0$,

$$
\mathcal{P}_k = \bigoplus_{j=0}^{k}\,(x^{\natural})^{\,j}\,\mathcal{M}_{k-j} ,
$$

the multiplier being left multiplication by the $j$-th power of the conjugate variable.

*Proof.* By the Lemma, $\dim\mathcal{M}_k=\dim\mathcal{P}_k-\dim\mathcal{P}_{k-1}$ and the sum
$\mathcal{M}_k+(x^{\natural})\mathcal{P}_{k-1}$ is direct of dimension
$\dim\mathcal{M}_k+\dim\mathcal{P}_{k-1}=\dim\mathcal{P}_k$, hence equal to $\mathcal{P}_k$;
iterating gives the displayed decomposition. The argument is the standard triangular induction of
*Clifford Analysis*, quoted there and not reproduced. $\square$

**Corollary (the counting).** With $\dim\mathcal{P}_k=\dim\mathcal{S}\binom{m+k}{k}$,

$$
\dim\mathcal{M}_k = \dim\mathcal{S}\left[\binom{m+k}{k}-\binom{m+k-1}{k-1}\right] .
$$

**Remark (why the kernel is the interesting object).** The operator $D$ determines the whole theory
through its kernel: the monogenic functions are the null solutions, the spaces $\mathcal{M}_k$ are
the polynomial part of the kernel, the fundamental solution is the distributional inverse read
through the conjugate operator, and the Cauchy kernel is the kernel of the inverse operator. In one
line, $D$ is a first-order elliptic operator whose symbol is invertible and whose kernel is large;
the two facts together are what make a Cauchy theory available, and both are the content of the
symbol computation and of the Fischer decomposition above.

**Example (the complex case, $m=1$).** Here $A\cong\mathbb{C}$ with $e_1=i$, the operator is
$D=\partial_0+i\partial_1$, the monogenic functions are the holomorphic ones, and the Fischer
decomposition $\mathcal{P}_k=\bigoplus_{j=0}^{k}\bar z^{\,j}\mathbb{C}z^{k-j}$ is the monomial basis
of the homogeneous polynomials of degree $k$. The dimension formula reads
$\dim_{\mathbb{C}}\mathcal{M}_k=\binom{k+1}{k}-\binom{k}{k-1}=1$; the monogenic part is the single
line spanned by $z^k$, as it must be.

**Example (the quaternionic case, $m=2$).** Here $A\cong\mathbb{H}$, the variable ranges over
$\mathbb{R}^3$, and $\dim\mathcal{M}_k=4[\binom{k+2}{k}-\binom{k+1}{k-1}]$, giving $4,8,12,\dots$
The linear monogenic functions are spanned by the constants and the Fueter variables
$z_i=x_0e_i-x_i$ of *Fueter Theory*, which is the same count read there.

## The Operator on a Module and the Twisting

**Remark (values in a module).** The definition of $D$ uses only that $\mathcal{S}$ is a left
Clifford module, so the whole construction — symbol, ellipticity, square, kernel — is independent of
the choice of $\mathcal{S}$, and the count $\dim\mathcal{M}_k$ alone depends on it. The passage to a
vector bundle and to a connection, which produces the twisted operator and the elliptic complex of
*Clifford Modules and the Twisted Cauchy–Riemann Operator*, replaces the constant coefficients
$e_\mu$ by the Clifford multiplication $c(e_j)$ and the derivative $\partial_j$ by a covariant
derivative $\nabla_{e_j}$; the flat operator of this article is the local model of that
construction, and the relation between the two — the Weitzenböck formula as the curved form of
$D\bar D=\Delta$ — is stated there.

**Remark (the symmetry group).** A constant unit $u\in A$ leaves the kernel unchanged, because
$D(uf)=u(Df)$; more generally the group of orthogonal transformations of the generating space and
the automorphisms of the algebra act on the admissible operators and their kernel, and the
stabiliser is the symmetry group of the system, as in *Hypercomplex Analysis*. The conformal action
on monogenic functions by the Vahlen matrices is *Clifford Analysis*'s, and the conformal geometry
is Part IV's.

## Summary

The operator of Clifford analysis is $D=\partial_0+\sum_{i=1}^{m}e_i\partial_i$, acting on
$\mathcal{S}$-valued functions of a vector variable by the one-sided Clifford action; the corpus
names it the Cauchy–Riemann operator, and the classical name *Dirac operator* is carried by the
self-adjoint family of *Dirac Differential Operators*. Its principal symbol is left multiplication
by $\sigma(\xi)=\sum_\mu e_\mu\xi_\mu$, which satisfies $\sigma(\xi)\bar\sigma(\xi)=|\xi|^2$; hence
$\sigma(\xi)$ is a unit for $\xi\neq0$, $D$ is elliptic, and $D\bar D=\bar DD=\Delta$. Because the
coefficients are constant, $D$ is the divergence of the field with components $e_\mu f$, and the
divergence theorem applies to it with the conormal element $\nu_B=\sum_\mu\nu_\mu e_\mu$.

The operator is not symmetric: with respect to the module form in which the vectors are skew,
$D^{*}=-\bar D$, so $D$ is neither symmetric nor normal, and it splits into the self-adjoint vector
part $D_{\mathrm{sa}}=\sum_{i\ge1}e_i\partial_i$, with $D_{\mathrm{sa}}^2=-\Delta$, and the
skew-adjoint scalar part $\partial_0$; the two factorisations of the Laplacian by $D\bar D$ and by
$D_{\mathrm{sa}}^2$ are the two faces of the split, and the spectral theory of the second is *Dirac
Differential Operators*. The kernel of $D$ is the class of monogenic functions, organised in
polynomials by the Fischer decomposition
$\mathcal{P}_k=\bigoplus_{j=0}^{k}(x^{\natural})^j\mathcal{M}_{k-j}$, with
$\dim\mathcal{M}_k=\dim\mathcal{S}[\binom{m+k}{k}-\binom{m+k-1}{k-1}]$; the distributional inverse
is produced from a fundamental solution $\Phi$ of the Laplacian by $E=\bar D\Phi$, and equals
$\omega_m^{-1}x^{\natural}|x|^{-m-1}$ up to the normalisation, which is the Cauchy kernel of
*Clifford Analysis*. The integral operator built from $E$ is *The Cauchy Integral Operator*, the
operator of the Fischer decomposition is *The Fischer Operator*, the operators on a Clifford module
are *Operators on a Clifford Module*, and the twisted and curved forms are *Clifford Modules and the
Twisted Cauchy–Riemann Operator*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A=\mathrm{Cl}_{0,m}$ | Clifford algebra of the negative-definite form, $\dim_\mathbb{R}A=2^m$ |
| $e_0=1,e_1,\dots,e_m$ | Frame of the operator; $e_ie_j+e_je_i=-2\delta_{ij}$ |
| $x=x_0+\sum_{i\ge1}e_ix_i$ | Vector variable of $\mathbb{R}^{m+1}$ |
| $x^{\natural}$ | Clifford conjugation, $xx^{\natural}=|x|^2$ |
| $\mathcal{S}$ | Left Clifford module of values; the algebra in the scalar case |
| $D=\sum_{\mu=0}^{m}e_\mu\partial_\mu$ | The operator of the article (the corpus's Cauchy–Riemann operator) |
| $\bar D=\partial_0-\sum_{i\ge1}e_i\partial_i$ | Conjugate operator |
| $\Delta=\sum_\mu\partial_\mu^2$ | Laplacian; $D\bar D=\bar DD=\Delta$ |
| $\sigma(\xi)=\sum_\mu e_\mu\xi_\mu$ | Principal symbol; $\sigma\bar\sigma=|\xi|^2$ |
| $\nu_B=\sum_\mu\nu_\mu e_\mu$ | Conormal element of a boundary |
| $D^{*}=-\bar D$ | Adjoint for the module form with skew vectors |
| $D_{\mathrm{sa}}=\sum_{i\ge1}e_i\partial_i$ | Self-adjoint vector part; $D_{\mathrm{sa}}^2=-\Delta$ |
| $\mathcal{S}$-valued $\mathcal{P}_k$, $\mathcal M_k$ | Homogeneous polynomials of degree $k$; solid spherical monogenics |
| $E=\bar D\Phi=\omega_m^{-1}x^{\natural}|x|^{-m-1}$ | Fundamental solution of $D$, the Cauchy kernel |
| $\omega_m=|S^m|$ | Surface area of the unit sphere in $\mathbb{R}^{m+1}$ |
| $\mathcal P_k=\bigoplus_{j}(x^{\natural})^j\mathcal M_{k-j}$ | Fischer decomposition |

## Further Reading

- F. Brackx, R. Delanghe and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the Cauchy–Riemann operator of Clifford analysis, its symbol and the Fischer decomposition.
- R. Delanghe, F. Sommen and V. Souček, *Clifford Algebra and Spinor-Valued Functions* (Kluwer, 1992), for the operator over Clifford modules and the spherical monogenics.
- Klaus Gürlebeck and Wolfgang Sprößig, *Quaternionic and Clifford Calculus for Physicists and Engineers* (Wiley, 1997), for the divergence form and the conormal calculus.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the self-adjoint family of Dirac-type operators and the Weitzenböck formula.
- John E. Gilbert and Margaret A. M. Murray, *Clifford Algebras and Dirac Operators in Harmonic Analysis* (Cambridge University Press, 1991), for the operator as the generator of the Clifford-analytic function theory.
