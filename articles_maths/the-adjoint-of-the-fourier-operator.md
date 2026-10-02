
# __The Adjoint of the Fourier Operator__

## Introduction

The Fourier operator is unitary, and for a unitary operator the adjoint is the inverse; this single
observation is the operator form of the Fourier inversion formula. On $L^2(\mathbb R^n)$, with the transform
$$
(\mathcal Ff)(\xi)=\int_{\mathbb R^n}f(x)e^{-2\pi ix\cdot\xi}\,dx ,
$$
the adjoint is the conjugate transform,
$$
\mathcal F^\dagger=\overline{\mathcal F}=\mathcal F^{-1} ,
$$
so that $\mathcal F^\dagger\mathcal F=\mathcal F\mathcal F^\dagger=\mathrm{id}$ is exactly the pair of
inversion identities, and applied to the transform the statement $\mathcal F^\dagger=\mathcal F^{-1}$ reads
$f(x)=\int\hat f(\xi)e^{2\pi ix\cdot\xi}d\xi$. The kernel of the operator is $K(x,\xi)=e^{-2\pi ix\cdot\xi}$
and the conjugate transpose kernel is $K^*(x,\xi)=\overline{K(\xi,x)}=e^{2\pi ix\cdot\xi}$, the kernel of the
inverse; the operator is also symmetric, $\mathcal F^{\mathrm t}=\mathcal F$, because its kernel is symmetric
in $x$ and $\xi$, so that the adjoint and the transpose differ only by the conjugation, as for every integral
operator. The phrase **unitary up to a constant** records the dependence on the normalisation: in the
angular-frequency convention the transform is not an isometry but has adjoint $(2\pi)^n$ times its inverse,
and it becomes unitary after the multiplication by $(2\pi)^{-n/2}$.

The article is the fourth and last of the `* Operator Theory` group of *Foundations of Analysis*. Its
prerequisites are *The Fourier Operator*, the third article of the first group of this category, for the
transform, the Plancherel theorem and the unitarity, and for the explicit deferral to this article;
*Fourier Analysis on Euclidean Spaces* for the transform on $L^1$ and the Schwartz class, the inversion
theorem and the convolution theorem; *The Fourier Transform and Conjugate Symmetry* for the conjugate
symmetry $\widehat{\bar f}(\xi)=\overline{\hat f(-\xi)}$; *The Adjoint of an Integral Operator* and
*Involutions of the Convolution Operators*, the earlier articles of this group, for the adjoint and the
multiplier forms; and *Banach and Hilbert Spaces*, later in this Part, for the adjoint and the unitary
operators, quoted as established. The transform on a general locally compact abelian group, the Pontryagin
dual and the Plancherel theorem there are *Harmonic Analysis on Groups* and *Pontryagin Duality*, in the
neighbouring category *Analysis on Groups* of this Part, and are named here as forward references only; the
distributional transform is *Distributions and Fundamental Solutions*, later in this Part. No geometry is
invoked.

## The Fourier Operator and Its Pairing

### The Transform

**Definition.** On the Schwartz class the **Fourier operator** is
$$
(\mathcal Ff)(\xi)=\int_{\mathbb R^n}f(x)e^{-2\pi ix\cdot\xi}\,dx ,
$$
and it extends to a unique bounded operator on $L^2(\mathbb R^n)$ with
$$
\lVert\mathcal Ff\rVert_2=\lVert f\rVert_2,\qquad
\langle\mathcal Ff,\mathcal Fg\rangle=\langle f,g\rangle ,
$$
for the Hilbert pairing $\langle f,g\rangle=\int f\bar g$; it is onto, hence unitary, and its inverse is the
conjugate transform, $\mathcal F^{-1}=\overline{\mathcal F}$, where
$(\overline{\mathcal F}f)(\xi)=\int f(x)e^{2\pi ix\cdot\xi}dx$. The transform has order four,
$$
\mathcal F^2=R,\qquad \mathcal F^4=\mathrm{id},\qquad Rf(x)=f(-x) ,
$$
$R$ being the reflection.

### The Pairing and the Kernel

**Definition.** The **kernel** of $\mathcal F$ is $K(x,\xi)=e^{-2\pi ix\cdot\xi}$, so that
$$
(\mathcal Ff)(\xi)=\int_{\mathbb R^n}K(x,\xi)f(x)\,dx ,
$$
and the **conjugate transpose kernel** is
$$
K^*(x,\xi)=\overline{K(\xi,x)}=e^{2\pi ix\cdot\xi} ,
$$
the kernel of the conjugate transform. The transform is **symmetric**, $K(\xi,x)=K(x,\xi)$, equivalently
$\mathcal F^{\mathrm t}=\mathcal F$ with respect to the bilinear pairing $\{f,g\}=\int fg$.

**Remark.** The kernel is not in $L^2(\mathbb R^n\times\mathbb R^n)$, so the transform is not Hilbert–Schmidt;
it is unitary, and the kernel is a tempered distribution, the pairing of which against a test function
reproduces the transform. The distributional kernel is *Distributions and Fundamental Solutions*, later in
this Part; the kernel notation used here is the same as for an integral operator, and the identities are
proved by the same change of variable wherever the integrals converge.

## The Adjoint Is the Inverse

### The Computation

**Theorem.** The adjoint of the Fourier operator is the conjugate transform, and the conjugate transform is
the inverse:
$$
\mathcal F^\dagger=\overline{\mathcal F}=\mathcal F^{-1} .
$$
Equivalently, $\langle\mathcal Ff,g\rangle=\langle f,\overline{\mathcal F}g\rangle$ for all $f,g\in L^2$.

**Proof.** On the Schwartz class, where the integrals converge absolutely,
$$
\langle\mathcal Ff,g\rangle=\int_{\mathbb R^n}\hat f(\xi)\overline{g(\xi)}\,d\xi
=\int_{\mathbb R^n}\!\!\int_{\mathbb R^n}f(x)e^{-2\pi ix\cdot\xi}\overline{g(\xi)}\,dx\,d\xi
=\int_{\mathbb R^n}f(x)\overline{\Bigl(\int_{\mathbb R^n}g(\xi)e^{2\pi ix\cdot\xi}\,d\xi\Bigr)}\,dx
=\langle f,\overline{\mathcal F}g\rangle ,
$$
by Fubini, and the identity extends to $L^2$ by the density of the Schwartz class and the boundedness of the
two operators. The inverse transform is the conjugate transform by the inversion theorem,
$\overline{\mathcal F}\mathcal F=\mathcal F\overline{\mathcal F}=\mathrm{id}$ on the Schwartz class, extended
by continuity; hence $\mathcal F^\dagger=\overline{\mathcal F}=\mathcal F^{-1}$. $\blacksquare$

### The Inversion Formula as Unitarity

**Theorem.** The Fourier operator is unitary,
$$
\mathcal F^\dagger\mathcal F=\mathcal F\mathcal F^\dagger=\mathrm{id},\qquad
\mathcal F^\dagger=\mathcal F^{-1}=\mathcal F^3 ,
$$
and the two identities are the two Fourier inversion formulas: the first, applied at a point, reads
$$
f(x)=\int_{\mathbb R^n}\hat f(\xi)e^{2\pi ix\cdot\xi}\,d\xi ,
$$
and the second is the conjugate statement. In the kernel language the first identity is
$$
K^*(x,\xi)=\overline{K(\xi,x)}=e^{2\pi ix\cdot\xi} ,
$$
with the left side the kernel of the adjoint and the right side the kernel of the inverse.

**Proof.** Unitarity is Plancherel's theorem of *The Fourier Operator*, the previous group; the adjoint is
the inverse by the theorem above; the order-four relation gives $\mathcal F^{-1}=\mathcal F^3$; the pointwise
form of $\mathcal F^\dagger\mathcal F=\mathrm{id}$ is the inversion theorem, and the kernel computation is
the definition of the conjugate transpose kernel of the previous articles. $\blacksquare$

**Corollary (the Plancherel identity as adjointness).** For $f,g\in L^2$,
$$
\langle\mathcal Ff,g\rangle=\langle f,\mathcal F^{-1}g\rangle ,
$$
and the transform preserves the inner product,
$$
\langle\mathcal Ff,\mathcal Fg\rangle=\langle f,g\rangle .
$$

**Proof.** The first identity is $\mathcal F^\dagger=\mathcal F^{-1}$ written as a pairing identity; replacing
$g$ by $\mathcal Fg$ in it and using $\mathcal F^{-1}\mathcal F=\mathrm{id}$ gives the second. $\blacksquare$

## Unitarity up to a Constant

### The Three Conventions

**Theorem (the constant of the normalisation).** Let
$$
(\mathcal F_1f)(\xi)=\int_{\mathbb R^n}f(x)e^{-ix\cdot\xi}\,dx
$$
be the transform in the **angular-frequency** convention. Then its adjoint is $(2\pi)^n$ times its inverse,
$$
\mathcal F_1^\dagger=(2\pi)^n\mathcal F_1^{-1},\qquad
\mathcal F_1^\dagger\mathcal F_1=(2\pi)^n\,\mathrm{id} ,
$$
so $\mathcal F_1$ is **unitary up to the constant** $(2\pi)^{-n/2}$:
$$
\lVert\mathcal F_1f\rVert_2^2=(2\pi)^n\lVert f\rVert_2^2,\qquad
(2\pi)^{-n/2}\mathcal F_1\ \text{is unitary}.
$$
In the **ordinary-frequency** convention $\mathcal Ff(\xi)=\int f(x)e^{-2\pi ix\cdot\xi}dx$ the constant is
$1$, $\mathcal F^\dagger\mathcal F=\mathcal F\mathcal F^\dagger=\mathrm{id}$, and the transform is exactly
unitary.

**Proof.** The angular transform is the composition of the ordinary transform with the dilation
$\xi\mapsto2\pi\xi$, so its adjoint carries the scaling factor $(2\pi)^n$; the isometry constant is computed
from $\lVert\mathcal F_1f\rVert_2^2=\int\lvert f(x)e^{-ix\xi}\rvert^2$-type Plancherel identity for the
angular convention, and the normalisation by $(2\pi)^{-n/2}$ cancels it. The ordinary-frequency statement is
the previous section. $\blacksquare$

### The Constant Fixed

**Theorem.** The multiplication constant is the unique normalisation making the transform unitary, up to a
unimodular scalar: the operators $c\mathcal F_1$ that are unitary are those with
$\lvert c\rvert=(2\pi)^{-n/2}$.

**Proof.** $(c\mathcal F_1)^\dagger(c\mathcal F_1)=\lvert c\rvert^2\,\mathcal F_1^\dagger\mathcal F_1
=\lvert c\rvert^2(2\pi)^n\mathrm{id}$, so unitarity is $\lvert c\rvert^2=(2\pi)^{-n}$; the phase is free. The
ordinary-frequency convention is the case $c=(2\pi)^{-n/2}$ of the angular one. $\blacksquare$

**Remark (the classical normalisation).** The two classical normalisations are the one of the present corpus,
$c=1$ with the $2\pi$-frequency, and the symmetric one
$$
\hat f(\xi)=(2\pi)^{-n/2}\int f(x)e^{-ix\cdot\xi}dx ,
$$
which is unitary because the constant has been absorbed. The inversion formulas differ by the constant:
$\check{\hat f}=f$ in the corpus, and
$f(x)=(2\pi)^{-n/2}\int\hat f(\xi)e^{ix\cdot\xi}d\xi$ in the symmetric one.

## The Transpose and the Reflection

### Reflection and Order Four

**Theorem.** The square of the transform is the reflection, $\mathcal F^2=R$ with $Rf(x)=f(-x)$, and the
symmetries of the transform are
$$
\mathcal F^3=\mathcal F^{-1}=\overline{\mathcal F},\qquad
\mathcal F^4=\mathrm{id},\qquad
\overline{\mathcal F}=\mathcal F R=R\mathcal F .
$$
The adjoint is the transform followed by the reflection, $\mathcal F^\dagger=\mathcal F R=\mathcal F^{-1}$,
and the reflection is self-adjoint and unitary, $R^\dagger=R=R^{-1}$.

**Proof.** The order-four relation is the Fourier article's; the identity $\overline{\mathcal F}=\mathcal F R$
is the conjugate symmetry in operator form, $\overline{\mathcal F}f=\overline{\mathcal F\bar f}$ computed from
the kernel $e^{2\pi ix\xi}=e^{-2\pi ix(-\xi)}$, that is the transform of the reflection; the reflection is its
own inverse and preserves the pairing. Combining with $\mathcal F^{-1}=\overline{\mathcal F}$ gives
$\mathcal F^\dagger=\mathcal F R$. $\blacksquare$

### The Transpose Coincides with the Transform

**Theorem.** The transform is symmetric for the bilinear pairing, $\mathcal F^{\mathrm t}=\mathcal F$; hence
the adjoint and the transpose are related by
$$
\mathcal F^\dagger=\overline{\mathcal F^{\mathrm t}}=\overline{\mathcal F} ,
$$
and the transform is complex-symmetric rather than self-adjoint; the deviation from self-adjointness is
exactly the conjugation.

**Proof.** The kernel $K(x,\xi)=e^{-2\pi ix\cdot\xi}$ is symmetric in $x$ and $\xi$, so the transposed kernel
is $K(\xi,x)=K(x,\xi)$ and the transpose of $\mathcal F$ is $\mathcal F$; the relation between the adjoint and
the transpose is that of *The Adjoint of an Integral Operator*, $K^*=\overline{K^{\mathrm t}}$, and it gives
$\mathcal F^\dagger=\overline{\mathcal F}$. A distributional argument extends the identity beyond the
convergent integrals. $\blacksquare$

**Example (the multiplication and convolution sides).** The transform conjugates convolution to
multiplication, $\mathcal F(f*g)=\mathcal Ff\cdot\mathcal Fg$, and the involution $f^*(x)=\overline{f(-x)}$ to
the conjugation, $\widehat{f^*}=\overline{\hat f}$; under these two correspondences the transform is a
$\ast$-isomorphism of the convolution algebra onto the algebra of multipliers, with the involution on the
first side carried to the conjugation on the second. The constant of the normalisation does not enter the
algebraic identities, only the metric ones, and the Hilbert transform, with the multiplier
$-i\operatorname{sgn}\xi$, is the skew-adjoint instance computed in *The Fourier Transform and Conjugate
Symmetry*.

## The Distributional and Group Cases

**Remark (tempered distributions).** The transform extends to the tempered distributions by
$\langle\mathcal F T,\varphi\rangle=\langle T,\mathcal F\varphi\rangle$, and the adjoint identity is the
definition; on the tempered distributions the order-four relation $\mathcal F^4=\mathrm{id}$, the reflection
$\mathcal F^2=R$ and the statement that the adjoint is the inverse continue to hold. The distributional
transform is *Distributions and Fundamental Solutions*, later in this Part.

**Remark (the general group).** On a general locally compact abelian group the transform is the pairing
against the characters, valued in functions on the Pontryagin dual, and the inversion, unitarity and adjoint
statements are the Plancherel theory of that transform; the normalisation constant is the constant of the
Haar measure, and the dual group replaces $\mathbb R^n$. This is *Harmonic Analysis on Groups* and
*Pontryagin Duality*, in the neighbouring category *Analysis on Groups* of this Part, and it is the group form
of the present article.

## Summary

The Fourier operator $\mathcal F$ on $L^2(\mathbb R^n)$ has the adjoint $\mathcal F^\dagger=\overline{\mathcal F}$,
the conjugate transform, and since the transform is unitary the adjoint is the inverse,
$\mathcal F^\dagger=\mathcal F^{-1}=\mathcal F^3$; the identities $\mathcal F^\dagger\mathcal F=\mathcal F\mathcal F^\dagger=\mathrm{id}$
are the two inversion formulas, and the kernel form of $\mathcal F^\dagger=\mathcal F^{-1}$ is
$K^*(x,\xi)=\overline{K(\xi,x)}=e^{2\pi ix\cdot\xi}$. The transform is symmetric, $\mathcal F^{\mathrm t}=\mathcal F$,
so the adjoint and the transpose differ by the conjugation, and $\overline{\mathcal F}=\mathcal F R=R\mathcal F$
with $R$ the reflection; the order-four relation $\mathcal F^2=R$, $\mathcal F^4=\mathrm{id}$ organises the
symmetries. The unitarity is **up to a constant**: in the angular-frequency convention the adjoint is
$(2\pi)^n$ times the inverse and the constant $(2\pi)^{-n/2}$ makes the operator unitary, while in the
ordinary-frequency convention of the corpus the constant is $1$ and the transform is exactly unitary; the
constant is a normalisation of the measure behind the transform. The Plancherel identity is the adjointness
of the transform against the pairing, and the distributional and locally compact abelian generalisations are
owned by later articles.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(\mathcal Ff)(\xi)=\int f(x)e^{-2\pi ix\cdot\xi}dx$ | Fourier operator, ordinary-frequency convention |
| $(\overline{\mathcal F}f)(\xi)=\int f(x)e^{2\pi ix\cdot\xi}dx$ | Conjugate transform |
| $\mathcal F^\dagger=\overline{\mathcal F}=\mathcal F^{-1}$ | The adjoint is the conjugate transform |
| $K(x,\xi)=e^{-2\pi ix\cdot\xi}$ | Kernel of the transform |
| $K^*(x,\xi)=\overline{K(\xi,x)}=e^{2\pi ix\cdot\xi}$ | Conjugate transpose kernel |
| $\mathcal F^{\mathrm t}=\mathcal F$ | Symmetry of the transform |
| $R$, $\mathcal F^2=R$, $\mathcal F^4=\mathrm{id}$ | Reflection and order four |
| $\mathcal F_1$, $(2\pi)^{-n/2}\mathcal F_1$ | Angular-frequency transform and its normalisation |

## Further Reading

- Elias M. Stein and Guido Weiss, *Introduction to Fourier Analysis on Euclidean Spaces* (Princeton
  University Press, 1971), for the transform, Plancherel's theorem, the inversion formula and the
  normalisations.
- Elias M. Stein and Rami Shakarchi, *Fourier Analysis: An Introduction* (Princeton University Press, 2003),
  for the transform on the Schwartz class and the inversion theorem.
- Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics I: Functional Analysis* (Academic
  Press, 1980), for the unitary operator and its adjoint.
- Walter Rudin, *Fourier Analysis on Groups* (Interscience, 1962), for the transform on a locally compact
  abelian group, the Plancherel theorem and the constant of the Haar measure.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I* (2nd ed., Springer, 1990), for
  the distributional transform and the kernel.
- John B. Conway, *A Course in Functional Analysis* (2nd ed., Springer, 1990), for the adjoint of a unitary
  operator and the reflection.
