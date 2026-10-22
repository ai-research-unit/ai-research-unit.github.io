# __Reduced Biquaternion Continuous Harmonic Analysis__

## Introduction

This article studies the continuous Fourier transform of a reduced biquaternion-valued function. The transform is defined by an algebra-valued kernel built from a root of minus one; because the idempotents commute with every element and the multiplication is commutative, the transform splits into the pair of the ordinary complex Fourier transforms of the two idempotent coordinates. The article records the kernel, the transform pair, the factorization, the convolution theorem, the relation to the differential operators, the vanishing-norm issue and the relation to the discrete transform. The treatment is purely mathematical.

Throughout the element is $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ with $Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle}$, $Q_{\blacktriangledown}=q_{\blacktriangledown}+iq'_{\blacktriangledown}$, the idempotent coordinates are $Q_{+}=Q_{\blacktriangle}+Q_{\blacktriangledown}$, $Q_{-}=Q_{\blacktriangle}-Q_{\blacktriangledown}$, and $\breve Q=Q_{+}\Pi_++Q_{-}\Pi_-$ with $\Pi_{\pm}=\tfrac12(1\pm j)$. The basis is $1,i,j,ij$ with $i^{2}=-1$, $j^{2}=+1$ and $ji=ij$. A signal is a function $f:\mathbb{R}\to\mathbb{B}_{\mathrm{r}}$, and the exponential is that of *Reduced Biquaternion Elementary Functions*.

## The Fourier Kernel

**Definition.** Fix a **root of minus one** $\rho$ of the algebra, an element with $\rho^{2}=-1$. The **continuous Fourier kernel** is
$$
W(t,\omega)=\exp\bigl(-2\pi \rho\,\omega t\bigr),\qquad t,\omega\in\mathbb{R}.
$$

**Theorem (the roots and the closed form).** The roots of minus one are exactly $\pm i$ and $\pm ij$, the elements with both coordinates in $\{i,-i\}$. For such a $\rho$,
$$
W(t,\omega)=\cos(2\pi\omega t)-\rho\,\sin(2\pi\omega t),
$$
and $W(t,\omega)$ is a **unit**, with $\langle W\rangle_{\mathrm{ts}*}=W\bar W=1$ and inverse $W^{-1}=\bar W=\cos(2\pi\omega t)+\rho\sin(2\pi\omega t)$; its multiplicative norm is $\langle W\rangle_{\mathrm{ts}}=1$ when $\rho=\pm ij$ and $\langle W\rangle_{\mathrm{ts}}=e^{-4\pi i\omega t}$ when $\rho=i$.

*Proof.* An element $\rho=Q_{+}\Pi_++Q_{-}\Pi_-$ has $\rho^{2}=Q_{+}^{2}\Pi_++Q_{-}^{2}\Pi_-$, so $\rho^{2}=-1$ exactly when $Q_{+}^{2}=Q_{-}^{2}=-1$; the kernel has the closed form because $\rho^{2}=-1$ makes the exponential series the two trigonometric series; and $W\bar W=K(W)=\cos^{2}+\sin^{2}=1$, because $\rho\bar\rho=1$ and $\rho+\bar\rho=0$ for the two roots, so the inverse is $\bar W$; the multiplicative norm is $\langle W\rangle_{\mathrm{ts}}=W W_{\mathrm{ts}}$, which is $1$ for $\rho=\pm ij$ and $e^{-4\pi i\omega t}$ for $\rho=i$, the tessarine sign fixing $i$.

**Corollary (the kernel in the two coordinates).** With $\rho$ having coordinates $(w_{1},w_{2})$, both in $\{i,-i\}$, the kernel is
$$
W(t,\omega)=e^{-2\pi w_{1}\omega t}\Pi_++e^{-2\pi w_{2}\omega t}\Pi_-,
$$
so it is the same complex kernel in the two coordinates when $\rho=\pm i$ and the mutually conjugate kernels when $\rho=\pm ij$; it is a unit in either case.

*Proof.* The exponential acts coefficientwise and the coordinates of $\rho$ are $w_{1},w_{2}$; for $\rho=i$ both are $i$, and for $\rho=ij$ they are $i$ and $-i$.

## The Continuous Transform Pair

**Definition.** For $f\in L^{1}(\mathbb{R},\mathbb{B}_{\mathrm{r}})$ the **Fourier transform** is
$$
\hat f(\omega)=\int_{\mathbb{R}}f(t)\,W(t,\omega)\,\mathrm{d}t .
$$
The **inverse transform** is
$$
f(t)=\int_{\mathbb{R}}\hat f(\omega)\,\overline{W(t,\omega)}\,\mathrm{d}\omega,
$$
the conjugate kernel $\overline{W(t,\omega)}=W(t,-\omega)$ inverting $W(t,\omega)$, so that no constant factor enters with the frequency convention $e^{-2\pi\rho\omega t}$.

**Theorem (the transform pair and the basic theorems).** For $f$ in the Schwartz class the transform pair holds, $\hat f$ is continuous and vanishes at infinity, the inversion is valid pointwise, and the Plancherel identity holds:
$$
\int_{\mathbb{R}}\lvert\hat f(\omega)\rvert^{2}_{K}\,\mathrm{d}\omega=\int_{\mathbb{R}}\lvert f(t)\rvert^{2}_{K}\,\mathrm{d}t ,
$$
where $\lvert\cdot\rvert_{K}=\sqrt{K(\cdot)}$ is the Euclidean norm of the algebra.

*Proof.* In each idempotent coordinate the transform is the ordinary complex Fourier transform of the complex signal $g_{j}$, since the kernel is the complex kernel in that coordinate; the classical theory gives continuity, decay, inversion and the Plancherel identity in each coordinate, and the two identities add because the Euclidean norm is the sum of the two coordinate moduli, $\lvert X\rvert_{K}^{2}=\lvert x_{1}\rvert^{2}+\lvert x_{2}\rvert^{2}$ for $X=x_{1}\Pi_++x_{2}\Pi_-$.

## Factorization into Two Complex Fourier Transforms

**Theorem (the factorization).** Writing $f(t)=g_{1}(t)\Pi_++g_{2}(t)\Pi_-$, the transform is
$$
\hat f(\omega)=\hat g_{1}(\omega)\,\Pi_++\hat g_{2}(\omega)\,\Pi_-,
$$
where $\hat g_{1}$ and $\hat g_{2}$ are the ordinary complex Fourier transforms of the two coordinate signals. The transform therefore factorizes into exactly two complex transforms, one per idempotent, with no coupling between them.

*Proof.* The kernel is constant in the algebra and equal to the complex kernel in each coordinate, so the integral splits into the two independent complex integrals.

**Corollary (the counting in real signals).** A general reduced biquaternion signal is a quadruple of real signals; its transform is the pair of the complex transforms of the two complex signals, hence four real transforms grouped into two complex pairs.

*Proof.* Each complex signal is a pair of real signals and its transform is computed as two real transforms; the two complex pairs are independent.

## The Convolution Theorem

**Definition.** The **convolution** of two signals is $(f*h)(t)=\int_{\mathbb{R}}f(s)h(t-s)\,\mathrm{d}s$.

**Theorem (the convolution theorem).** For $f,h\in L^{1}$, the convolution is in $L^{1}$ and
$$
\widehat{f*h}(\omega)=\hat f(\omega)\,\hat h(\omega),
$$
and the convolution splits in the idempotent coordinates into the two ordinary complex convolutions.

*Proof.* Interchanging the order of integration and using the kernel identity $W(t,\omega)=W(s,\omega)W(t-s,\omega)$, valid because the kernel is multiplicative in the exponent, gives the display; the interchange is justified by the integrability, and the commutativity of the algebra makes the order of the factors immaterial.

**Corollary (the transform of a product).** The transform of a product is the convolution of the transforms, $\widehat{fh}=\hat f*\hat h$ with the appropriate normalisation, again coordinatewise.

*Proof.* The product is commutative and the one-variable duality between the product and the convolution holds in each coordinate.

## The Relation to the Differential Operators

**Theorem (the derivative and the Laplacian).** If $f$ is differentiable with integrable derivative, then
$$
\widehat{\partial/\partial t\,f}(\omega)=2\pi\rho\,\omega\,\hat f(\omega),
$$
so the derivative becomes multiplication by the algebra element $2\pi\rho\omega$, and the transform in the four real coordinates of the algebra replaces the Euclidean Laplacian by the multiplier
$$
\Delta\longmapsto-4\pi^{2}\bigl(\omega_{a}^{2}+\omega_{a'}^{2}+\omega_{b}^{2}+\omega_{b'}^{2}\bigr).
$$

*Proof.* Integrating by parts in each coordinate and using $\partial/\partial t\,W=2\pi\rho\omega W$ for the real variable case; in four variables the second derivative contributes the square of the frequency, and the sum of the four squares is the multiplier, with the global minus sign from the two integrations by parts.

**Corollary (the Fourier support of a regular function).** The reduced Cauchy–Riemann operator $\bar\partial$ becomes, in the first idempotent coordinate, the multiplier $\tfrac14[(\omega_{a}+\omega_{b})+i(\omega_{a'}+\omega_{b'})]$, and in the second the multiplier $\tfrac14[(\omega_{a}-\omega_{b})+i(\omega_{a'}-\omega_{b'})]$. Consequently the Fourier transform of a **regular** function is supported in the union of the two two-planes
$$
\omega_{a}+\omega_{b}=0,\ \omega_{a'}+\omega_{b'}=0\qquad\text{and}\qquad \omega_{a}-\omega_{b}=0,\ \omega_{a'}-\omega_{b'}=0,
$$
the characteristic set of the operator; a regular function of compact support is therefore zero.

*Proof.* The multipliers are the symbols of the two Wirtinger derivatives, computed in *Reduced Biquaternion Regular Functions*, §*The Cauchy–Riemann Operator and Its Conjugate*; a distribution supported in a two-plane of measure zero in the frequency space is zero, and a compactly supported function has an entire transform, which must then vanish identically.

## The Vanishing-Norm Issue

**The obstruction is deconvolution, not convolution.** The convolution theorem holds for all integrable signals, but solving $h=f*g$ for $g$ requires dividing by $\hat f(\omega)$ at each frequency, and $\hat f(\omega)$ may be a zero divisor; the division then fails. This is the analytic place where the algebra differs from the field.

**The Euclidean norm is not multiplicative.** $\langle fh\rangle_{\mathrm{ts}*}\neq K(f)K(h)$ in general, so the energy identity does not hold for the Euclidean norm; the Plancherel identity holds because it is the sum of the two coordinate identities, not because the norm is multiplicative.

**The transformed values need not be units.** A sum of units is generally not a unit, the zero divisors being the union of two complex lines, so the transform of a signal of units can have zero-divisor values; only the transform as a linear operator is invertible, not its pointwise values.

*Proof.* The failure of the division is the definition of a zero divisor; the defect $\langle fh\rangle_{\mathrm{ts}*}-K(f)K(h)$ is the cross term described in *Topology and Metric for Each of the Operations*; and the possibility of a zero-divisor sum follows because the units are not closed under addition, though the unit set is open and dense.

## The Transform of a Measure and the Bochner Theorem

**Definition.** Let $\mu$ be a finite positive measure on $\mathbb{R}$. Its **transform** is $\hat\mu(\omega)=\int_{\mathbb{R}}W(t,\omega)\,\mathrm{d}\mu(t)$, an algebra-valued function of $\omega$. The **Hermitian pairing** of the algebra is
$$
\langle X,Y\rangle=x_{1}\bar y_{1}+x_{2}\bar y_{2},\qquad X=x_{1}\Pi_++x_{2}\Pi_-,
$$
whose real part is the Euclidean inner product of the two factors and whose diagonal is positive definite, $\langle X,X\rangle=\lvert x_{1}\rvert^{2}+\lvert x_{2}\rvert^{2}>0$ for $X\neq0$.

**Theorem (the Bochner theorem).** A continuous function $\Phi:\mathbb{R}\to\mathbb{B}_{\mathrm{r}}$ is the transform of a finite positive measure if and only if it is **positive definite**, that is
$$
\sum_{j,r=1}^{n}\bigl\langle c_{j},\,c_{r}\bigr\rangle\,\Phi(\omega_{j}-\omega_{r})\ \ge\ 0
$$
in the sense that the sum lies in the closed positive cone of the pairing, for every finite set of frequencies and every choice of algebra coefficients; equivalently, each of the two idempotent coordinate functions of $\Phi$ is positive definite in the classical sense.

*Proof.* The kernel has coordinates $e^{-2\pi w_{j}\omega t}$ with $w_{j}\in\{i,-i\}$ of modulus one, so each coordinate of $\hat\mu$ is the transform of $\mu$ against a complex kernel of modulus one; by the classical Bochner theorem in one complex variable, the transform of a finite positive measure is exactly a continuous positive-definite function, and conversely every such function comes from a measure; the two coordinates share the measure $\mu$, and the classical positivity of the two coordinates reassembles as the positivity of the pairing, which is positive definite because the Euclidean form of the algebra is definite.

**Corollary (the contrast with the non-commutative cases).** For the biquaternion algebra the transform of a measure is not positive definite, the quadratic form of the algebra norm being indefinite and negative on the central imaginary direction; for the reduced biquaternion algebra the definite Euclidean form $\langle\cdot\rangle_{\mathrm{ts}*}$ is available and the classical positivity survives, so the Bochner theorem holds coordinatewise. The indefinite form $\langle\cdot,\cdot\rangle_{*}$ of the geometry article plays no role here, and the vanishing of the multiplicative norm $\langle\cdot\rangle_{\mathrm{ts}}$ is irrelevant to the positivity, which is a statement about the definite form.

*Proof.* The biquaternion obstruction is the negativity of the norm on the central imaginary element; here the pairing has a positive-definite diagonal, the two coordinates each satisfy the classical positivity, and the multiplicative norm does not enter the positivity condition.

## The Relation to the Discrete Transform

**Theorem (the discrete transform as a periodisation).** The discrete transform of *Reduced Biquaternion Discrete Harmonic Analysis* is the continuous transform of the periodised signal, and the periodisation is the Poisson summation in each of the two complex coordinates; the two transforms agree on signals of finite support after the usual sampling hypotheses.

*Proof.* The Poisson summation formula holds in each coordinate, and the two coordinates are independent; sampling and periodisation are the two sides of the same coordinatewise duality.

**Corollary (the sampling identity).** Sampling the signal at the integers multiplies the transform by the periodisation in each coordinate, so the discrete and the continuous transforms carry the same information under the classical band limitation hypotheses, coordinatewise.

*Proof.* The Poisson summation in one variable is the sampling identity, and the two coordinates each obey it.

## Summary

The continuous Fourier transform of a reduced biquaternion signal is defined by the kernel $W(t,\omega)=\exp(-2\pi\rho\omega t)$ with $\rho$ a root of minus one, the roots being exactly $\pm i$ and $\pm ij$; the kernel has the closed form $\cos(2\pi\omega t)-\rho\sin(2\pi\omega t)$, is a unit with $\langle W\rangle_{\mathrm{ts}*}=1$, and is the ordinary complex kernel in each idempotent coordinate. The transform pair, the continuity and decay, the inversion and the Plancherel identity hold, the last being the sum of the two coordinate identities, and the transform factorizes into exactly two complex transforms. The convolution theorem holds for integrable signals, and the transform of a product is the convolution of the transforms. The derivative becomes multiplication by $2\pi\rho\omega$; the Euclidean Laplacian becomes the negative of the sum of the squared frequency variables; and the Cauchy–Riemann operator becomes the pair of its two symbols, so the Fourier transform of a regular function is supported in the union of the two characteristic two-planes, a regular function of compact support being zero. The vanishing-norm issue is the failure of deconvolution at the zero-divisor frequencies, and the discrete transform is the periodisation of the continuous one under the Poisson summation in each coordinate. The transform of a finite positive measure is positive definite and the Bochner theorem holds coordinatewise, with the Hermitian pairing of the two factors, unlike the biquaternion case where the definiteness fails. Against the split biquaternion case, where the transform is the pair of the quaternion transforms and the non-commutativity survives in the kernel product, the reduced biquaternion transform is the purely commutative pair of the complex transforms.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\rho$ | Root of minus one, one of $\pm i,\pm ij$ |
| $W(t,\omega)=\exp(-2\pi\rho\omega t)$ | Continuous Fourier kernel |
| $\hat f(\omega)=\int_{\mathbb{R}}f(t)W(t,\omega)\mathrm{d}t$ | Fourier transform |
| $f(t)=\int_{\mathbb{R}}\hat f(\omega)\overline{W(t,\omega)}\mathrm{d}\omega$ | Inversion |
| $f*h$ | Convolution |
| $\lvert X\rvert_{K}=\sqrt{K(X)}$ | Euclidean norm of the value |
| $2\pi\rho\omega$ | Multiplier of the derivative |
| $-4\pi^{2}(\omega_{a}^{2}+\omega_{a'}^{2}+\omega_{b}^{2}+\omega_{b'}^{2})$ | Multiplier of the Laplacian |

## Further Reading

- Elias M. Stein and Rami Shakarchi, *Fourier Analysis: An Introduction* (Princeton University Press, 2003), for the transform pair, the Plancherel identity and the Poisson summation.
- Elias M. Stein and Guido Weiss, *Introduction to Fourier Analysis on Euclidean Spaces* (Princeton University Press, 1971), for the sampling identities and the higher-dimensional transforms.
- G. Baley Price, *An Introduction to Multicomplex Spaces and Functions* (Marcel Dekker, 1991), for the exponential kernel and the transforms of the commutative algebra.
- M. Elena Luna-Elizarrarás, Michael Shapiro, Daniele C. Struppa and Adrian Vajiac, *Bicomplex Holomorphic Functions* (Birkhäuser, 2015), for the idempotent factorization of the analytic transforms.
- Todd K. Moon and Wynn C. Stirling, *Mathematical Methods and Algorithms for Signal Processing* (Prentice-Hall, 2000), for the reduction of hypercomplex transforms to a pair of complex transforms.
