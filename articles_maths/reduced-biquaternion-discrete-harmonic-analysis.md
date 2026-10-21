# __Reduced Biquaternion Discrete Harmonic Analysis__

## Introduction

This article studies the discrete Fourier transform of a reduced biquaternion-valued signal. The transform is defined by an algebra-valued kernel built from an algebra element whose square is $-1$; because the idempotents commute with every element and the multiplication is commutative, the transform splits into the pair of the ordinary complex discrete transforms of the two idempotent coordinates. The article records the kernel, the transform pair, the factorization, the convolution theorem, the vanishing-norm issue, and the two-dimensional and higher-dimensional transforms. The treatment is purely mathematical.

Throughout the element is $\breve Q=Q_++jQ_-$ with $Q_+=q_++iq'_+$, $Q_-=q_-+iq'_-$, the idempotent coordinates are $Q_{++}=Q_++Q_-$, $Q_{--}=Q_+-Q_-$, and $\breve Q=Q_{++}\Pi_++Q_{--}\Pi_-$ with $\Pi_{\pm}=\tfrac12(1\pm j)$. The basis is $1,i,j,ij$ with $i^{2}=-1$, $j^{2}=+1$ and $ji=ij$. A signal of length $N$ is a map $f:\{0,1,\dots,N-1\}\to\mathbb{B}_{\mathrm{r}}$.

## The Fourier Kernel

**Definition.** A **root of minus one** of the algebra is an element $\rho$ with $\rho^{2}=-1$. The **Fourier kernel** of length $N$ is
$$
W_{N}(n,m)=\exp\Bigl(-2\pi \rho\,\frac{nm}{N}\Bigr),
$$
with $\rho$ a root of minus one and the exponential that of *Reduced Biquaternion Elementary Functions*.

**Theorem (the roots of minus one and the kernel).** The roots of minus one are exactly
$$
\pm i,\qquad \pm ij,
$$
that is the elements with coordinates $Q_{++},Q_{--}\in\{i,-i\}$; the kernel with the choice $\rho=i$ is the complex kernel $W_{N}(n,m)=e^{-2\pi i nm/N}$ read in the algebra, and with $\rho=ij$ it is the same with $ij$ in place of $i$. In either case $W_{N}(n,m)=w_{1}^{nm}\Pi_++w_{2}^{nm}\Pi_-$ with $w_{1},w_{2}$ the two $N$-th roots of unity determined by the chosen root; for the choice $\rho=i$ the two idempotent coordinates of the kernel are equal, while for $\rho=ij$ they are conjugate.

*Proof.* An element $\rho=Q_{++}\Pi_++Q_{--}\Pi_-$ has $\rho^{2}=Q_{++}^{2}\Pi_++Q_{--}^{2}\Pi_-$, so $\rho^{2}=-1$ exactly when $Q_{++}^{2}=Q_{--}^{2}=-1$, that is $Q_{++},Q_{--}=\pm i$, four elements; the exponential $\exp(-2\pi\rho nm/N)$ acts coefficientwise, $e^{-2\pi Q_{++} nm/N}\Pi_++e^{-2\pi Q_{--} nm/N}\Pi_-$, which is the displayed pair, and the choice $\rho=i$ has $Q_{++}=Q_{--}=i$ while $\rho=ij$ has $Q_{++}=i$, $Q_{--}=-i$.

## The Discrete Transform Pair

**Definition.** For a signal $f$ of length $N$ the **discrete Fourier transform** is the signal $\mathcal F f$,
$$
(\mathcal F f)(m)=\sum_{n=0}^{N-1}f(n)\,W_{N}(n,m),\qquad m=0,1,\dots,N-1,
$$
the products being in the algebra, which is why the order of the factors is immaterial.

**Theorem (the transform pair).** The transform is linear and satisfies the inversion
$$
f(n)=\frac{1}{N}\sum_{m=0}^{N-1}(\mathcal F f)(m)\,W_{N}(n,-m),
$$
valid for **every** signal. The two formulas are the ordinary discrete transform pair in each idempotent coordinate.

*Proof.* The kernel satisfies the orthogonality $\sum_{m}W_{N}(n,m)W_{N}(r,-m)=N\,\delta_{n,r}$ in each coordinate, because $w_{1}$ and $w_{2}$ are $N$-th roots of unity; the algebra being commutative and the kernel scalar in each coordinate, the sums reassemble in the algebra, and the standard orthogonality gives the inversion. No divisibility condition is needed, the transform matrix being invertible over the algebra as over the complex numbers.

**Corollary (the ambiguity of the root).** The choice of the root $\pm i$ or $\pm ij$ is a choice of sign and of definite direction; choosing the opposite root conjugates the transform, and the property that matters, invertibility, is independent of the choice.

*Proof.* Replacing $\rho$ by $-\rho$ replaces the kernel by its reciprocal, and replacing $i$ by $ij$ exchanges the two idempotent roles in the kernel pair, both invertible operations.

## Factorization into Two Complex Fourier Transforms

**Theorem (the factorization).** Writing the signal as $f(n)=g_{1}(n)\Pi_++g_{2}(n)\Pi_-$, the transform is
$$
(\mathcal F f)(m)=(\mathcal F g_{1})(m)\,\Pi_++(\mathcal F g_{2})(m)\,\Pi_-,
$$
where $\mathcal F g_{1}$ and $\mathcal F g_{2}$ are the ordinary complex discrete Fourier transforms of the two coordinate signals. Thus the reduced biquaternion transform is the pair of the two complex transforms, and it factorizes into exactly two complex transforms, one per idempotent.

*Proof.* The kernel is constant in the two coordinates of the algebra and equal to $w_{1}^{nm}$ in the first and $w_{2}^{nm}$ in the second, so the sum over $n$ splits into the two independent complex sums.

**Corollary (the count of complex transforms).** A general reduced biquaternion signal is a quadruple of real signals, and its transform is the pair of complex transforms of the two complex signals $g_{1}=\text{first pair}$ and $g_{2}=\text{second pair}$; expressed in real signals this is four real discrete transforms grouped into two complex pairs. There is no coupling between the two pairs.

*Proof.* Each of $g_{1}$ and $g_{2}$ is a complex signal, hence a pair of real signals, and the complex transform of a complex signal is computed as two real transforms; the two coordinates are independent by the factorization.

## The Convolution Theorem

**Definition.** The **convolution** of two length-$N$ signals is $(f*h)(n)=\sum_{r}f(r)h(n-r)$, the index taken modulo $N$.

**Theorem (the convolution theorem).** The transform of the convolution is the pointwise product of the transforms,
$$
(\mathcal F(f*h))(m)=(\mathcal F f)(m)\,(\mathcal F h)(m),
$$
and the convolution splits in the idempotent coordinates into the two ordinary complex convolutions.

*Proof.* The index-shift computation is the standard one and uses only the commutativity of the algebra and the identity $W_{N}(n,m)=W_{N}(n-r,m)W_{N}(r,m)$, which holds because the kernel factors through the addition in the exponent; the coordinate statement follows from the factorization of the transform.

**Corollary (the cyclic convolution and the two coordinates).** The cyclic convolution is the componentwise cyclic convolution, $(f*h)= (g_{1}*h_{1})\Pi_++(g_{2}*h_{2})\Pi_-$; the convolution of two signals is again a signal, and no zero-divisor obstruction appears in the convolution theorem itself.

*Proof.* In each coordinate the classical cyclic convolution theorem holds, and the two coordinates are carried by the idempotents.

## The Vanishing-Norm Issue

**The obstruction is deconvolution, not convolution.** The convolution theorem holds for all signals, but the **inverse filter** $h=f*g$ solved for $g$ requires the division by $(\mathcal F f)(m)$ at each frequency, and $(\mathcal F f)(m)$ may be a zero divisor; the division then fails and the deconvolution is not determined. This is the point where the commutative algebra with zero divisors differs from the field.

**The norm is not multiplicative along the transform.** The Euclidean norm $\langle\cdot\rangle_{\natural*}$ of the product is not the product of the norms, $\langle fh\rangle_{\natural*}\neq K(f)K(h)$, so the energy identity does not hold with the Euclidean norm; what holds is the pair of the classical Parseval identities in the two coordinates, each with the norm of the corresponding complex coordinate.

**The transform of a unit need not be a unit.** Because the transform is a sum with complex scalar coefficients, the transformed samples may be zero divisors even when the original samples are units, so the pointwise invertibility of the transform is not preserved by the transform; the invertibility that is preserved is that of the transform as a linear operator, not of its values.

*Proof.* Division by a zero divisor fails by definition; $\langle fh\rangle_{\natural*}-K(f)K(h)$ is the cross term computed in the discussion of the norm in *Topology and Metric for Each of the Operations*; and a sum of units is generally not a unit, the zero divisors being a union of two lines, so the sum can land on one of them.

## The Two-Dimensional Transform

**Definition.** For a signal $f$ of size $N\times N$ the **two-dimensional transform** is
$$
(\mathcal F f)(m_{1},m_{2})=\sum_{n_{1},n_{2}}f(n_{1},n_{2})W_{N}(n_{1},m_{1})W_{N}(n_{2},m_{2}),
$$
one kernel factor for each index.

**Theorem (separability and factorization).** The two-dimensional transform is separable, it is the composition of the one-dimensional transforms in the two indices in either order, and it factorizes into the pair of the two-dimensional complex transforms of the two idempotent coordinates; the convolution theorem holds for the two-dimensional cyclic convolution.

*Proof.* The kernel is the product of the two one-index kernels, and the double sum factors; the coordinate splitting is the same as in one dimension; the convolution theorem is the standard two-index computation, valid because the algebra is commutative.

## Higher-Dimensional Transforms

**Theorem (the $d$-dimensional transform).** For a signal on the grid $\{0,\dots,N-1\}^{d}$ the transform with one kernel factor per index is separable, invertible for every signal, and factorizes into the pair of the $d$-dimensional complex transforms of the two coordinates. Its convolution theorem holds for the $d$-dimensional cyclic convolution.

*Proof.* The kernel is the product of the $d$ one-index kernels, and the sum separates; the same orthogonality and the same coordinate splitting as in the lower-dimensional cases give the result.

**Corollary (the cost and the count).** A $d$-dimensional reduced biquaternion transform of size $N$ in each index is the pair of the two complex $d$-dimensional transforms, hence a fixed multiple of the cost of one complex $d$-dimensional transform; there is no reduced biquaternion transform that is not a pair of complex ones.

*Proof.* The factorization exhibits the transform as the direct sum of the two complex transforms, and the direct sum has the cost of the two.

## Summary

The discrete Fourier transform of a reduced biquaternion signal is defined by the kernel $W_{N}(n,m)=\exp(-2\pi\rho nm/N)$ with $\rho$ a root of minus one, and the roots of minus one are exactly $\pm i$ and $\pm ij$, the definite directions of the algebra. The kernel is constant in the two idempotent coordinates, so the transform splits into the pair of the ordinary complex discrete transforms of the two coordinates, and it factorizes into exactly two complex transforms, four real transforms for a general signal. The transform pair is invertible for every signal, independently of the choice of the root, and the convolution maps to the pointwise product. The vanishing-norm issue is the failure of deconvolution at the frequencies where the transformed sample is a zero divisor; the Euclidean norm is not multiplicative along the transform, and the Parseval identity holds only in the two coordinates. The two-dimensional and the higher-dimensional transforms are separable, invertible and reduce to the pair of the complex ones with the same number of dimensions. Against the split biquaternion case, where the transform is the pair of the quaternion transforms and the non-commutativity survives in the convolution, the reduced biquaternion transform is the purely commutative pair of the complex transforms.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\rho$ | Root of minus one, one of $\pm i,\pm ij$ |
| $W_{N}(n,m)=\exp(-2\pi\rho nm/N)$ | Fourier kernel |
| $(\mathcal F f)(m)=\sum_{n}f(n)W_{N}(n,m)$ | Discrete Fourier transform |
| $f(n)=\frac{1}{N}\sum_{m}(\mathcal F f)(m)W_{N}(n,-m)$ | Inversion |
| $f*h$ | Cyclic convolution |
| $\mathcal F(f*h)=\mathcal F f\,\mathcal F h$ | Convolution theorem |
| $g_{1},g_{2}$ | The two coordinate signals |
| $\Pi_{\pm}=\tfrac12(1\pm j)$ | Idempotents |

## Further Reading

- Elias M. Stein and Rami Shakarchi, *Fourier Analysis: An Introduction* (Princeton University Press, 2003), for the discrete and continuous Fourier transforms and their basic theorems.
- J. J. Benedetto and M. W. Frazier, eds., *Wavelets: Mathematics and Applications* (CRC Press, 1994), for discrete transforms and sampling in a commutative setting.
- G. Baley Price, *An Introduction to Multicomplex Spaces and Functions* (Marcel Dekker, 1991), for the exponential kernel and the transforms of the multicomplex algebra.
- M. Elena Luna-Elizarrarás, Michael Shapiro, Daniele C. Struppa and Adrian Vajiac, *Bicomplex Holomorphic Functions* (Birkhäuser, 2015), for the idempotent factorization of the integral transforms of the commutative algebra.
- [Harmonic Analysis over Hypercomplex Systems](harmonic-analysis-over-hypercomplex-systems.html), §*The Discrete Case and the Reduction to the Factor Algebra*, in this corpus, for the commutative reduction of the hypercomplex transform to a pair of complex transforms.
- [Biquaternion Discrete Harmonic Analysis](biquaternion-discrete-harmonic-analysis.html), §*The Commutative Alternative: The Reduced Biquaternion Transform*, in this corpus, for the discrete transform of the commutative algebra and its cost in complex transforms.
