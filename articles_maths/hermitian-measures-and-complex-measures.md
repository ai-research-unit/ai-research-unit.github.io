
# __Hermitian Measures and Complex Measures__

## Introduction

A complex measure is a countable additive set function with complex values, and the theory of the integral
associates with it its total variation $|\mu|$, a positive measure, and the **polar decomposition**
$\mu=h\,|\mu|$ with $\lvert h\rvert=1$ almost everywhere, which is the measure-theoretic counterpart of the
polar form $z=\lvert z\rvert e^{i\theta}$ of a complex number. The operation of complex conjugation acts on
the measures by conjugating their values,
$$
\bar\mu(A)=\overline{\mu(A)},
$$
and this **involution** is the subject of the present article: the measures fixed by it are the Hermitian
ones, exactly the real signed measures; an arbitrary complex measure splits into a Hermitian part and an
anti-Hermitian part; and the polar decomposition is compatible with the involution by the conjugation of the
density. The involution is the same involution as that of the previous articles of this group — complex
conjugation of functions — now on the space of measures, and the measures that are both Hermitian and
positive are exactly the ones that Bochner's theorem produces from the positive definite functions.

This article is the third of the `*` group of *Foundations of Analysis*. Its prerequisites are *Measure
Theory and Integration* for the signed and complex measures, the Hahn–Jordan decomposition, the total
variation, the Radon–Nikodym theorem and the convergence theorems, and *Positive Definite Functions and
Hermitian Kernels*, the previous article of this group, for Bochner's theorem and the positive definite
functions. The Fourier–Stieltjes transform of a measure and its compatibility with the involution use the
Fourier transform of *Fourier Analysis on Euclidean Spaces*; the general measure algebra of a locally
compact group and the convolution of measures are *Convolution on a Group* and *Harmonic Analysis on
Groups*, in the neighbouring category *Analysis on Groups* of this Part, and are named as forward references
only. The Riesz representation theorem that produces a measure from a positive functional is quoted from
*Measure Theory and Integration*, as in the previous article. The positive definite distributions of the
next article are the dual form of the present material; the Hermitian kernels of integral operators are the
`* Operator` article later in this group. No geometry is invoked.

## The Space of Complex Measures

### Definition and the Total Variation

**Definition.** Let $(X,\mathcal A)$ be a measurable space. A **complex measure** is a function
$\mu:\mathcal A\to\mathbb C$ with $\mu(\varnothing)=0$ that is countably additive; a **signed measure** is
the real-valued analogue. The **total variation** of a complex measure is the nonnegative set function
$$
\lvert\mu\rvert(A)=\sup\Bigl\{\sum_{j=1}^n\lvert\mu(A_j)\rvert : A=\bigsqcup_{j=1}^nA_j,\ A_j\in\mathcal A\Bigr\} ,
$$
the supremum over the finite measurable partitions of $A$; the **variation norm** is $\lVert\mu\rVert=\lvert\mu\rvert(X)$.

**Theorem (the variation is a measure and the norm is complete).** For every complex measure $\mu$ the set
function $\lvert\mu\rvert$ is a finite positive measure; every complex measure is a finite linear combination
of positive finite measures,
$$
\mu=\mu_1-\mu_2+i(\mu_3-\mu_4),
$$
and the space $M(X)$ of complex measures is a complex vector space in which the variation norm is complete,
so $M(X)$ is a Banach space.

**Proof.** The Hahn–Jordan decomposition of *Measure Theory and Integration* writes a real signed measure as
$\nu=\nu^+-\nu^-$ with $\lvert\nu\rvert=\nu^++\nu^-$, and applying it to the real and imaginary parts of
$\mu$ gives the four-measure representation; the variation of the combination is at most the sum of the
variations, so $M(X)$ embeds in the product of four copies of the space of finite measures, closed under the
norm; completeness follows from the completeness of the space of finite measures in the variation norm,
which is the countable additivity under limits. $\blacksquare$

### The Involution

**Definition.** The **involution** on $M(X)$ is
$$
\bar\mu(A)=\overline{\mu(A)},\qquad A\in\mathcal A .
$$
It is additive, conjugate-linear over $\mathbb C$, involutive, and it is an isometry for the variation norm,
$\lvert\bar\mu\rvert=\lvert\mu\rvert$ and $\lVert\bar\mu\rVert=\lVert\mu\rVert$; with this involution
$M(X)$ is a Banach space carrying an involutive conjugate-linear isometry.

**Proof.** Additivity and conjugation are immediate; $\lvert\bar\mu\rvert(A)=\lvert\mu\rvert(A)$ because a
partition has the same variation for $\bar\mu$ and $\mu$; the involution is conjugate-linear by the
conjugation of the scalars. $\blacksquare$

**Remark (the two involutions).** The involution $\bar\mu$ is the **value-conjugation**, the one induced by
the complex conjugation of functions through the pairing $\langle\mu,f\rangle=\int f\,d\mu$ of the last
section. It is not the **adjoint involution** $\mu^{*}(A)=\overline{\mu(A^{-1})}$ of the group measure
algebra, which appears when $X$ is a group and $M(X)$ is given the convolution product; the adjoint
involution is anti-multiplicative and is treated in *Convolution on a Group*, in the neighbouring category
*Analysis on Groups* of this Part. Value-conjugation, by contrast, commutes with convolution,
$\overline{\mu*\nu}=\bar\mu*\bar\nu$. The distinction is recorded so that the mark $\bar\mu$ is never read
as the algebra involution.

**Definition.** A complex measure is **Hermitian** if $\bar\mu=\mu$, and **anti-Hermitian** if
$\bar\mu=-\mu$; the **Hermitian part** and the **anti-Hermitian part** of $\mu$ are
$$
\mu_{\mathrm h}=\frac12(\mu+\bar\mu),\qquad \mu_{\mathrm a}=\frac12(\mu-\bar\mu),\qquad
\mu=\mu_{\mathrm h}+\mu_{\mathrm a} .
$$
Equivalently $\mu_{\mathrm h}=\operatorname{Re}\mu$ and $\mu_{\mathrm a}=i\operatorname{Im}\mu$, where
$\operatorname{Re}\mu$ and $\operatorname{Im}\mu$ are the real signed measures defined by
$(\operatorname{Re}\mu)(A)=\operatorname{Re}(\mu(A))$ and $(\operatorname{Im}\mu)(A)=\operatorname{Im}(\mu(A))$.

**Theorem (the Hermitian measures are the real signed measures).** A complex measure $\mu$ is Hermitian if
and only if $\mu(A)\in\mathbb R$ for every $A$, if and only if $\mu$ is a real signed measure; the
Hermitian measures form a real vector space, and every complex measure decomposes uniquely as a Hermitian
plus an anti-Hermitian measure.

**Proof.** $\bar\mu=\mu$ is the statement $\overline{\mu(A)}=\mu(A)$ for all $A$, that is
$\mu(A)\in\mathbb R$; the converse is immediate. The decomposition is the one displayed, and its uniqueness
is the uniqueness of the real and imaginary parts. $\blacksquare$

## Polar Decomposition

### The Polar Form of a Measure

**Definition.** A **polar decomposition** of a complex measure $\mu$ is a representation
$$
\mu=h\,\lvert\mu\rvert,\qquad d\mu=h\,d\lvert\mu\rvert ,
$$
with $h$ a measurable function of modulus one $\lvert\mu\rvert$-almost everywhere.

**Theorem (existence and uniqueness of the polar decomposition).** Every complex measure $\mu$ has a polar
decomposition, and it is unique in the sense that its density $h$ is unique $\lvert\mu\rvert$-almost
everywhere.

**Proof.** The total variation is a positive measure and $\mu\ll\lvert\mu\rvert$: if $\lvert\mu\rvert(A)=0$
then every measurable subset of $A$ has $\mu$-measure zero, so $\mu(A)=0$. The Radon–Nikodym theorem of
*Measure Theory and Integration* therefore gives a density $h=d\mu/d\lvert\mu\rvert\in L^1(\lvert\mu\rvert)$
with $d\mu=h\,d\lvert\mu\rvert$; the identity $\lvert\mu\rvert=\lvert h\rvert\,\lvert\mu\rvert$, proved by
applying the Radon–Nikodym derivative to the definition of the variation, forces $\lvert h\rvert=1$
$\lvert\mu\rvert$-almost everywhere. Uniqueness is the uniqueness of the Radon–Nikodym derivative.
$\blacksquare$

### Compatibility with the Involution

**Theorem.** For a complex measure $\mu=h\,\lvert\mu\rvert$,
$$
\bar\mu=\bar h\,\lvert\mu\rvert,\qquad \lvert\bar\mu\rvert=\lvert\mu\rvert ,
$$
and if $\nu$ is a measure with $\mu\ll\nu$, then $\bar\mu\ll\nu$ and
$$
\frac{d\bar\mu}{d\nu}=\overline{\frac{d\mu}{d\nu}} .
$$
The polar decomposition of $\bar\mu$ is obtained from that of $\mu$ by conjugating the density.

**Proof.** $\bar\mu(A)=\overline{\int_Ah\,d\lvert\mu\rvert}=\int_A\bar h\,d\lvert\mu\rvert$ by the
conjugation of the integral, and $\lvert\bar h\rvert=1$; the Radon–Nikodym statement follows from the same
computation with $\nu$ in place of $\lvert\mu\rvert$. $\blacksquare$

**Corollary (Hermitian and anti-Hermitian densities).** A measure $\mu=h\,\lvert\mu\rvert$ is Hermitian if
and only if its density is real $\lvert\mu\rvert$-almost everywhere, and anti-Hermitian if and only if its
density is purely imaginary; the Hermitian and anti-Hermitian parts have densities
$\operatorname{Re}h$ and $i\operatorname{Im}h$.

**Proof.** The involution conjugates $h$, so the fixed points and the skew points of the involution are the
real and imaginary densities. $\blacksquare$

## Hermitian Measures and the Fourier–Stieltjes Transform

### The Transform and Its Involution Property

**Definition.** For a finite complex measure $\mu$ on $\mathbb R^n$ the **Fourier–Stieltjes transform** is
$$
\hat\mu(\xi)=\int_{\mathbb R^n}e^{-2\pi ix\cdot\xi}\,d\mu(x),
$$
with the normalisation of *Fourier Analysis on Euclidean Spaces*; it is a bounded uniformly continuous
function of $\xi$, with $\lVert\hat\mu\rVert_\infty\leq\lVert\mu\rVert$, and it determines $\mu$ uniquely.

**Theorem.** The involution commutes with the transform through the reflection of the argument,
$$
\widehat{\bar\mu}(\xi)=\overline{\hat\mu(-\xi)} .
$$
Consequently $\mu$ is Hermitian if and only if its transform is a Hermitian function,
$\hat\mu(-\xi)=\overline{\hat\mu(\xi)}$, and $\mu$ is anti-Hermitian if and only if $\hat\mu$ is odd, with
$\hat\mu(-\xi)=-\overline{\hat\mu(\xi)}$.

**Proof.** $\widehat{\bar\mu}(\xi)=\int e^{-2\pi ix\cdot\xi}d\bar\mu(x)
=\overline{\int e^{2\pi ix\cdot\xi}d\mu(x)}=\overline{\hat\mu(-\xi)}$ by the conjugation of the integral and
the sign change $x\mapsto-x$. The Hermitian condition $\hat\mu=\widehat{\bar\mu}$ is then the stated
symmetry. $\blacksquare$

### Positive Definite Functions and the Cone of Positive Measures

**Theorem (Bochner, recast).** A continuous function $\varphi$ on $\mathbb R^n$ is positive definite if and
only if $\varphi(x)=\hat\mu(-x)$ for a unique finite **positive** measure $\mu$, equivalently
$\varphi(x)=\int e^{2\pi ix\cdot\xi}d\mu(\xi)$; the Hermitian measures are exactly the measures whose
transforms satisfy the Hermitian symmetry, and the positive measures among them are exactly the transforms
of the positive definite functions.

**Proof.** This is Bochner's theorem of *Positive Definite Functions and Hermitian Kernels*, the previous
article of this group, with the transform of the present Article; the statement that a positive measure
gives a positive definite function is the computation
$$
\sum_{i,j}\overline{c_i}c_j\hat\mu(x_j-x_i)=\int\Bigl\lvert\sum_ic_ie^{-2\pi ix_i\cdot\xi}\Bigr\rvert^2d\mu(\xi)\geq0 ,
$$
and the converse is the theorem quoted. $\blacksquare$

Thus the positive definite functions are the transforms of the positive cone in the Hermitian measures, and
the Hermitian measures are the real subspace on which the involution acts trivially; the whole of Bochner's
theorem is the statement that the transform identifies the positive cone of $M(\mathbb R^n)$ with the cone
of positive definite functions.

### The Pairing of a Measure with a Function

**Theorem.** Write $\langle\mu,f\rangle=\int f\,d\mu$ for $f\in L^1(\lvert\mu\rvert)$. The involution is the
adjoint of the complex conjugation of the function,
$$
\langle\bar\mu,f\rangle=\overline{\langle\mu,\bar f\rangle},\qquad
\langle\mu,\bar f\rangle=\overline{\langle\bar\mu,f\rangle} .
$$

**Proof.** $\langle\bar\mu,f\rangle=\int f\,d\bar\mu=\overline{\int\bar f\,d\mu}$ by the conjugation of the
integral, which is the first identity; the second is its conjugate. $\blacksquare$

## Order and the Positive Cone

**Definition.** For Hermitian (real, signed) measures define $\mu\leq\nu$ if $\nu-\mu$ is a positive measure,
that is, if $(\nu-\mu)(A)\geq0$ for every $A$. A Hermitian measure is **positive** if $\mu\geq0$, and the
**positive cone** is the set of positive measures.

**Theorem.** The positive cone is a closed convex cone in the real space of Hermitian measures, and it is
generated by the measures of the form $\mathbf 1_A\,\lvert\mu\rvert$; a complex measure is positive if and
only if it is Hermitian and its density in the polar decomposition is $+1$. The Hermitian measures are the
span of the positive cone, and $\lvert\mu\rvert$ is the least positive measure dominating $\mu$ in the
absolute-value sense.

**Proof.** The cone properties are immediate from positivity; the generation and the density statement
follow from the polar decomposition, since $\lvert\mu\rvert=h^{-1}\mu$ with $h$ of modulus one and, when
$\mu$ is positive, the density of its polar decomposition is the constant $1$. The domination property is
the definition of the total variation. $\blacksquare$

**Remark (the involution and the order).** The involution is order preserving on the Hermitian measures: if
$\mu\leq\nu$ with both Hermitian, then, $\mu$ and $\nu$ being real, $\bar\mu=\mu\leq\nu=\bar\nu$. The
positive definite functions are exactly the positive cone, under the transform, and this is the content of
Bochner's theorem in its sharpest form.

## Summary

A complex measure is a countably additive $\mathbb C$-valued set function, and the space $M(X)$ of them is a
Banach space with total variation norm carrying the involutive conjugate-linear isometry
$\bar\mu(A)=\overline{\mu(A)}$; a measure is Hermitian, $\bar\mu=\mu$, exactly when it is a real signed
measure, and every complex measure splits uniquely as $\mu=\mu_{\mathrm h}+\mu_{\mathrm a}$ with
$\mu_{\mathrm h}=\operatorname{Re}\mu$ and $\mu_{\mathrm a}=i\operatorname{Im}\mu$. Every complex measure
has a polar decomposition $\mu=h\lvert\mu\rvert$ with $\lvert h\rvert=1$ almost everywhere, unique in $h$,
which is the Radon–Nikodym derivative of $\mu$ with respect to its variation, and the involution conjugates
$h$ and commutes with the Radon–Nikodym derivative. The Fourier–Stieltjes transform satisfies
$\widehat{\bar\mu}(\xi)=\overline{\hat\mu(-\xi)}$, so the Hermitian measures are exactly the measures whose
transforms are Hermitian functions; Bochner's theorem identifies the positive measures with the positive
definite functions, so that the positive definite functions are the transform of the positive cone, and the
involution is the adjoint of complex conjugation of functions. The Hermitian measures form a real ordered
space whose positive cone is closed, convex and spanned by the positive measures.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M(X)$ | Complex measures with the variation norm, a Banach space with value-conjugation |
| $\lvert\mu\rvert$, $\lVert\mu\rVert$ | Total variation and variation norm |
| $\bar\mu(A)=\overline{\mu(A)}$ | The involution on measures |
| $\mu_{\mathrm h}=\frac12(\mu+\bar\mu)$ | Hermitian part, a real signed measure |
| $\mu_{\mathrm a}=\frac12(\mu-\bar\mu)$ | Anti-Hermitian part, $i$ times a signed measure |
| $\mu=h\lvert\mu\rvert$ | Polar decomposition, $\lvert h\rvert=1$ a.e. |
| $\hat\mu(\xi)=\int e^{-2\pi ix\cdot\xi}d\mu(x)$ | Fourier–Stieltjes transform |
| $\widehat{\bar\mu}(\xi)=\overline{\hat\mu(-\xi)}$ | Involution property of the transform |
| $\langle\mu,f\rangle=\int f\,d\mu$ | Pairing of a measure with a function |

## Further Reading

- Walter Rudin, *Real and Complex Analysis* (3rd ed., McGraw-Hill, 1987), for complex measures, the polar
  decomposition and the Radon–Nikodym theorem.
- Paul R. Halmos, *Measure Theory* (Van Nostrand, 1950; reprinted Springer, 1974), for the total variation
  and the Banach space of measures.
- Nelson Dunford and Jacob T. Schwartz, *Linear Operators, Part I* (Interscience, 1958), for the space of
  measures as a Banach space and its duality.
- Walter Rudin, *Fourier Analysis on Groups* (Interscience, 1962), for the measure algebra, the
  Fourier–Stieltjes transform and the positive definite functions.
- Elias M. Stein and Guido Weiss, *Introduction to Fourier Analysis on Euclidean Spaces* (Princeton
  University Press, 1971), for the Fourier–Stieltjes transform on $\mathbb R^n$.
- Gerald B. Folland, *Real Analysis: Modern Techniques and Their Applications* (2nd ed., Wiley, 1999), for
  the signed and complex measures and the Radon–Nikodym theorem.
