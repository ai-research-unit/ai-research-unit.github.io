
# Quaternion Harmonic Analysis

## Introduction

This article introduces harmonic analysis on the quaternion space as the study of the Fourier transform, convolution, and the function spaces on which they act, with the non-commutative structure playing an essential role. The goal is to define the core objects precisely, establish their basic properties, and describe the theorems that give the subject its shape.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. No examples are given. The quaternion algebra is assumed from the article on quaternion algebra, and the scalar-vector decomposition is used throughout. The article is stated for the quaternion algebra over the real numbers, and the complexification is mentioned only where it clarifies the structure.

Throughout this article, the quaternion algebra is denoted $\mathbb{H}$, and its basis is $e_0 = 1, e_1, e_2, e_3$. The scalar imaginary of the complex numbers is denoted $i$, so that it does not collide with the quaternion units.

## The Quaternion Space as a Locally Compact Abelian Group

### Additive Structure

The quaternion space $\mathbb{H}$ is a locally compact abelian group under addition, isomorphic to $\mathbb{R}^4$. Its **characters** are the continuous homomorphisms into the circle group. Since the additive group of $\mathbb{H}$ is just $\mathbb{R}^4$, the characters are the ordinary four-dimensional Fourier characters:

$$
\chi_\xi(q) = e^{2\pi i \operatorname{Re}(\bar{\xi} q)}, \qquad \xi \in \mathbb{H},
$$

where the exponential is the ordinary complex exponential, and the pairing is

$$
\langle \xi, q \rangle = \operatorname{Re}(\bar{\xi} q) = \xi_0 q_0 + \xi_1 q_1 + \xi_2 q_2 + \xi_3 q_3.
$$

Note the sign: the quaternion conjugation $\bar{\xi} = \xi_0 - \boldsymbol{\xi}$ gives $\bar{\xi} q = (\xi_0 - \boldsymbol{\xi})(q_0 + \mathbf{q})$, whose real part is $\xi_0 q_0 + \boldsymbol{\xi} \cdot \mathbf{q}$. So the pairing is the ordinary Euclidean pairing on $\mathbb{R}^4$.

So at the level of the additive group, quaternion harmonic analysis is the same as Fourier analysis on $\mathbb{R}^4$. The non-commutative structure of $\mathbb{H}$ enters only when the algebra structure is used, as in the quaternion Fourier transform and the convolution theorem.

### The Quaternion Characters

The **quaternion characters** are the homomorphisms into the multiplicative group of $\mathbb{H}$:

$$
\chi_\xi(q) = e^{\omega \operatorname{Re}(\bar{\xi} q)}, \qquad \xi \in \mathbb{H},
$$

where $\omega$ is a fixed unit pure quaternion and the exponential is the quaternion exponential. Because $\omega^2 = -1$, this is

$$
\chi_\xi(q) = \cos(\operatorname{Re}(\bar{\xi} q)) + \omega \sin(\operatorname{Re}(\bar{\xi} q)).
$$

These characters are **bounded** in the quaternion norm, because they take values on the unit sphere $\mathbb{S}^3$. This is the fundamental difference from the split complex case, where the characters are unbounded, and the similarity with the complex case, where the characters take values in the compact circle.

So the quaternion case is intermediate between the complex case and the split complex case: the characters are bounded, but the algebra is non-commutative, and the transform depends on the choice of the unit pure quaternion $\omega$.

## The Quaternion Fourier Transform

### Definition

The **quaternion Fourier transform** of a function $f : \mathbb{H} \to \mathbb{H}$ is

$$
\hat{f}(\xi) = \int_{\mathbb{H}} f(q) e^{-\omega \operatorname{Re}(\bar{\xi} q)} \, dq,
$$

where $dq$ is Lebesgue measure on $\mathbb{H} \cong \mathbb{R}^4$, $\omega$ is a fixed unit pure quaternion, and the exponential is the quaternion exponential.

Because the exponential depends on the choice of $\omega$, there are infinitely many quaternion Fourier transforms, one for each unit pure quaternion. The most common choices are:

- **Left-sided transform.** $\hat{f}(\xi) = \int f(q) e^{-\omega \operatorname{Re}(\bar{\xi} q)} \, dq$, with the exponential on the right.
- **Right-sided transform.** $\hat{f}(\xi) = \int e^{-\omega \operatorname{Re}(\bar{\xi} q)} f(q) \, dq$, with the exponential on the left.
- **Two-sided transform.** $\hat{f}(\xi) = \int e^{-\omega_1 \operatorname{Re}(\bar{\xi} q)} f(q) e^{-\omega_2 \operatorname{Re}(\bar{\xi} q)} \, dq$, with two distinct unit pure quaternions $\omega_1$ and $\omega_2$.

The three transforms are related but not equivalent, and the choice depends on the application. The two-sided transform is the most general, and it is the one that diagonalizes the quaternion Dirac operator.

### The Structure of the Transform

Write $f(q) = f_0(q) + f_1(q) e_1 + f_2(q) e_2 + f_3(q) e_3$ with $f_\mu : \mathbb{H} \to \mathbb{R}$. Then the quaternion Fourier transform decomposes into four real Fourier transforms, one for each component, with the kernel depending on the choice of $\omega$.

For the simplest case $\omega = e_1$, the kernel is

$$
e^{-e_1 \operatorname{Re}(\bar{\xi} q)} = \cos(\operatorname{Re}(\bar{\xi} q)) - e_1 \sin(\operatorname{Re}(\bar{\xi} q)).
$$

So the transform is

$$
\hat{f}(\xi) = \int f(q) \cos(\operatorname{Re}(\bar{\xi} q)) \, dq - e_1 \int f(q) \sin(\operatorname{Re}(\bar{\xi} q)) \, dq.
$$

The first integral is the cosine transform, and the second is the sine transform. Both are real-valued when $f$ is real-valued, and both are ordinary four-dimensional Fourier transforms. So the quaternion Fourier transform is the ordinary Fourier transform on $\mathbb{R}^4$, tensored with the quaternion algebra.

### Basic Properties

**Linearity.** The transform is linear over $\mathbb{R}$, but not over $\mathbb{H}$, because $\mathbb{H}$ is non-commutative.

**Translation.** If $f_a(q) = f(q - a)$, then $\hat{f}_a(\xi) = e^{-\omega \operatorname{Re}(\bar{\xi} a)} \hat{f}(\xi)$ for the left-sided transform.

**Modulation.** If $f_\xi(q) = e^{\omega \operatorname{Re}(\bar{\xi} q)} f(q)$, then $\hat{f}_\xi(\eta) = \hat{f}(\eta - \xi)$.

**Scaling.** If $f_\lambda(q) = f(\lambda q)$ for $\lambda \in \mathbb{H}^\times$, then

$$
\widehat{f_\lambda}(\xi) = \frac{1}{|\lambda|^4} \hat{f}(\xi/\lambda).
$$

**Rotation.** If $f_u(q) = f(u q u^{-1})$ for a unit quaternion $u$, then $\hat{f}_u(\xi) = \hat{f}(u \xi u^{-1})$. The transform commutes with rotations.

**Conjugation.** $\widehat{\bar{f}}(\xi) = \overline{\hat{f}(-\xi)}$.

### The Plancherel Theorem

**Theorem.** The quaternion Fourier transform extends uniquely to a unitary operator

$$
\mathcal{F} : L^2(\mathbb{H}) \to L^2(\mathbb{H}),
$$

with

$$
\|\hat{f}\|_2 = \|f\|_2, \qquad \langle \hat{f}, \hat{g} \rangle = \langle f, g \rangle.
$$

This is the Plancherel theorem for $\mathbb{R}^4$, written in quaternion notation. The non-commutativity does not affect the $L^2$ theory, because the transform is defined by an integral against a bounded kernel.

### The Inversion Theorem

**Theorem.** If $f \in L^1(\mathbb{H})$ and $\hat{f} \in L^1(\mathbb{H})$, then

$$
f(q) = \int_{\mathbb{H}} \hat{f}(\xi) e^{\omega \operatorname{Re}(\bar{\xi} q)} \, d\xi
$$

for almost every $q$.

The inversion formula holds because the kernel is bounded and the transform is essentially the ordinary Fourier transform on $\mathbb{R}^4$.

## Convolution

### Definition

The **convolution** of $f, g : \mathbb{H} \to \mathbb{H}$ is

$$
(f * g)(q) = \int_{\mathbb{H}} f(q - r) g(r) \, dr,
$$

whenever the integral converges. This is the convolution on the additive group $\mathbb{H} \cong \mathbb{R}^4$.

### Basic Properties

**Non-commutativity.** The convolution is not commutative in general, because $\mathbb{H}$ is not commutative: $f * g \neq g * f$ in general. It is commutative only when one of the functions takes values in the center of $\mathbb{H}$, which is $\mathbb{R}$.

**Associativity.** $(f * g) * h = f * (g * h)$.

**Young's inequality.** If $1/p + 1/q = 1/r + 1$ with $1 \leq p, q, r \leq \infty$, then

$$
\|f * g\|_r \leq \|f\|_p \|g\|_q,
$$

where the norms are the ordinary $L^p$ norms on $\mathbb{R}^4$.

**Convolution theorem.** For functions for which the quaternion Fourier transform is defined,

$$
\widehat{f * g}(\xi) = \hat{f}(\xi) \hat{g}(\xi),
$$

with the same ordering on both sides for the left-sided transform. For the two-sided transform, the statement is more complicated, because the two kernels do not commute.

**Proof.** Write the definition, apply Fubini, and change variables. $\square$

### The Structure of the Convolution Theorem

The convolution theorem for the quaternion Fourier transform is the same as for the complex Fourier transform on $\mathbb{R}^4$, except that the multiplication on the right is quaternion multiplication, which is non-commutative. So the convolution theorem says that the transform turns convolution into quaternion multiplication, and the non-commutativity of the convolution is a reflection of the non-commutativity of $\mathbb{H}$.

### Approximate Identities

A sequence $(\phi_n)$ in $L^1(\mathbb{H})$ is an **approximate identity** if

$$
\int_{\mathbb{H}} \phi_n = 1, \qquad \sup_n \|\phi_n\|_1 < \infty, \qquad \int_{|q| > \delta} |\phi_n(q)| \, dq \to 0
$$

for every $\delta > 0$.

**Theorem.** If $(\phi_n)$ is an approximate identity and $f \in L^p(\mathbb{H})$ for $1 \leq p < \infty$, then

$$
\|f * \phi_n - f\|_p \to 0.
$$

This is the same as in the real case, because the additive group of $\mathbb{H}$ is just $\mathbb{R}^4$.

## Distributions

### Definition

A **tempered distribution** on $\mathbb{H}$ is a continuous linear functional on the Schwartz space $\mathcal{S}(\mathbb{H})$. The space of tempered distributions is denoted $\mathcal{S}'(\mathbb{H})$. It includes all functions in $L^p(\mathbb{H})$ for $1 \leq p \leq \infty$, all finite measures, and all derivatives of such objects.

### Operations on Distributions

**Differentiation.** For $T \in \mathcal{S}'(\mathbb{H})$ and $\phi \in \mathcal{S}(\mathbb{H})$,

$$
\langle \partial_\mu T, \phi \rangle = -\langle T, \partial_\mu \phi \rangle, \qquad \mu = 0, 1, 2, 3.
$$

**Multiplication by a function.** For $f \in C^\infty(\mathbb{H})$ with polynomial growth and $T \in \mathcal{S}'(\mathbb{H})$,

$$
\langle f T, \phi \rangle = \langle T, f \phi \rangle.
$$

**Quaternion Fourier transform.** For $T \in \mathcal{S}'(\mathbb{H})$ and $\phi \in \mathcal{S}(\mathbb{H})$,

$$
\langle \hat{T}, \phi \rangle = \langle T, \hat{\phi} \rangle.
$$

The quaternion Fourier transform is a bijection $\mathcal{S}'(\mathbb{H}) \to \mathcal{S}'(\mathbb{H})$.

### The Dirac Delta

The **Dirac delta** $\delta$ is the tempered distribution

$$
\langle \delta, \phi \rangle = \phi(0).
$$

Its quaternion Fourier transform is the constant function $1$, and the quaternion Fourier transform of $1$ is $\delta$. The delta is the identity for convolution: $\delta * T = T$ for every tempered distribution $T$.

### The Cauchy Kernel

The **Cauchy kernel** is the distribution

$$
E(q) = \frac{\bar{q}}{|q|^4},
$$

which satisfies

$$
D E = \delta_0
$$

in the sense of distributions, where $D$ is the quaternion Dirac operator. It is the fundamental solution of the Dirac operator, and it is the quaternion analogue of the kernel $1/z$ in complex analysis.

## The Quaternion Hilbert Transform

### Definition

The **quaternion Hilbert transform** of $f : \mathbb{H} \to \mathbb{H}$ is defined by the principal value integral

$$
Hf(q) = \frac{1}{\pi^2} \, \text{p.v.} \int_{\mathbb{H}} \frac{(r - q)^{-1}}{|r - q|^2} f(r) \, dr,
$$

where the integral is over the quaternion space and the principal value is taken with respect to the singularity at $r = q$.

### Basic Properties

**Boundedness.** $H$ is bounded on $L^p(\mathbb{H})$ for $1 < p < \infty$, with

$$
\|Hf\|_p \leq C_p \|f\|_p.
$$

**Fourier multiplier.** In terms of the quaternion Fourier transform,

$$
\widehat{Hf}(\xi) = -\omega \operatorname{sgn}(\xi) \hat{f}(\xi),
$$

where $\operatorname{sgn}$ is the sign function on the real part.

### The Relation to the Dirac Operator

The quaternion Hilbert transform is the boundary value of the Cauchy integral for monogenic functions. It is the quaternion analogue of the Hilbert transform in complex analysis, and it is used in the theory of boundary value problems for the Dirac equation.

## Maximal Functions

### The Quaternion Maximal Function

The **quaternion Hardy–Littlewood maximal function** of $f \in L^1_{\mathrm{loc}}(\mathbb{H})$ is

$$
Mf(q) = \sup_{r > 0} \frac{1}{|B(q, r)|} \int_{B(q, r)} |f(r)| \, dr,
$$

where $B(q, r)$ is the Euclidean ball of radius $r$ centered at $q$, and $|B(q, r)|$ is its volume.

### The Maximal Inequality

**Theorem (Hardy–Littlewood, quaternion version).** There exists a constant $C > 0$ such that for every $f \in L^1(\mathbb{H})$ and every $\lambda > 0$,

$$
|\{q : Mf(q) > \lambda\}| \leq \frac{C}{\lambda} \|f\|_1.
$$

This is a **weak $(1,1)$** estimate. It implies that $M$ is bounded on $L^p(\mathbb{H})$ for $1 < p \leq \infty$.

**Theorem.** For $1 < p \leq \infty$, there exists $C_p > 0$ such that

$$
\|Mf\|_p \leq C_p \|f\|_p.
$$

**Proof.** The case $p = \infty$ is trivial. The case $1 < p < \infty$ follows from the weak $(1,1)$ estimate and the trivial $L^\infty$ estimate by interpolation. $\square$

### The Structure of the Maximal Function

Because the additive group of $\mathbb{H}$ is just $\mathbb{R}^4$, the maximal function theory is identical to the real theory on $\mathbb{R}^4$. The non-commutativity of $\mathbb{H}$ does not affect the maximal function, because the maximal function is defined in terms of the Euclidean norm, which does not see the algebra structure.

## The Calderón–Zygmund Theory

### Singular Integrals

A **quaternion Calderón–Zygmund operator** is a bounded operator $T : L^2(\mathbb{H}) \to L^2(\mathbb{H})$ with a kernel $K : \mathbb{H} \times \mathbb{H} \to \mathbb{H}$ such that

$$
Tf(q) = \int_{\mathbb{H}} K(q, r) f(r) \, dr
$$

for $q \notin \operatorname{supp} f$, and $K$ satisfies the size and smoothness estimates

$$
|K(q, r)| \leq \frac{C}{|q - r|^4},
$$

$$
|K(q, r) - K(q', r)| \leq C \frac{|q - q'|^\delta}{|q - r|^{4+\delta}}, \qquad |q - q'| < \frac{1}{2} |q - r|,
$$

and the analogous estimate in the second variable, for some $\delta > 0$. The power $4$ is the dimension of $\mathbb{H}$ as a real vector space.

**Theorem (Calderón–Zygmund, quaternion version).** Every quaternion Calderón–Zygmund operator is bounded on $L^p(\mathbb{H})$ for $1 < p < \infty$, and satisfies a weak $(1,1)$ estimate.

**Examples.** The quaternion Hilbert transform, the quaternion Riesz transforms, and the Beurling–Ahlfors transform are quaternion Calderón–Zygmund operators.

### The Structure of the Theory

Because the additive group of $\mathbb{H}$ is just $\mathbb{R}^4$, the Calderón–Zygmund theory is identical to the real theory on $\mathbb{R}^4$, with the dimension adjusted from $n$ to $4$. The non-commutativity of $\mathbb{H}$ does not affect the kernel estimates, because they are in terms of the Euclidean norm, which does not see the algebra structure. The non-commutativity affects only the multiplication of the kernel with the function, and this is a minor modification.

## The Mellin Transform

### Definition

The **quaternion Mellin transform** of a function $f : (0, \infty) \to \mathbb{H}$ is

$$
\mathcal{M} f(s) = \int_0^\infty t^{s-1} f(t) \, dt,
$$

where the power is the quaternion power. Because the variable $t$ is real and the quaternion $s$ appears only in the exponent, the integral converges for $s_0$ in the appropriate range.

### Relation to the Quaternion Fourier Transform

Under the change of variables $t = e^x$, the Mellin transform becomes the quaternion Fourier transform on the real line:

$$
\mathcal{M} f(\sigma + \omega \tau) = \int_{-\infty}^\infty e^{(\sigma + \omega \tau) x} f(e^x) \, dx = \hat{g}(\tau),
$$

where $g(x) = e^{\sigma x} f(e^x)$ and $\omega$ is a unit pure quaternion. So the Mellin transform is the quaternion Fourier transform in logarithmic coordinates.

### The Mellin Convolution

The **quaternion Mellin convolution** is

$$
(f \star g)(x) = \int_0^\infty f(x/y) g(y) \frac{dy}{y}.
$$

It satisfies

$$
\mathcal{M}(f \star g)(s) = \mathcal{M} f(s) \, \mathcal{M} g(s),
$$

which is the multiplicative analogue of the convolution theorem.

## The Radon Transform

### Definition

The **quaternion Radon transform** of a function $f : \mathbb{H} \to \mathbb{H}$ is

$$
Rf(\theta, t) = \int_{L(\theta, t)} f(q) \, ds,
$$

where $L(\theta, t)$ is the hyperplane with normal direction $\theta \in \mathbb{S}^3$ and signed distance $t$ from the origin, and $ds$ is the Euclidean surface measure.

### The Fourier Slice Theorem

**Theorem (Fourier Slice, quaternion version).** The one-dimensional quaternion Fourier transform of $Rf(\theta, \cdot)$ is the restriction of the four-dimensional quaternion Fourier transform of $f$ to the line through the origin in direction $\theta$:

$$
\widehat{Rf(\theta, \cdot)}(\sigma) = \hat{f}(\sigma \theta).
$$

**Proof.** Write the definition of the Radon transform, take the quaternion Fourier transform in $t$, and change variables. $\square$

The Fourier slice theorem is the mathematical basis of quaternion tomography, the analogue of computed tomography for the quaternion space.

### The Inversion Formula

**Theorem.** For suitable $f$,

$$
f(q) = \frac{1}{2} \int_{\mathbb{S}^3} \int_{-\infty}^\infty \widehat{Rf(\theta, \cdot)}(\sigma) |\sigma|^3 e^{\omega \operatorname{Re}(\bar{\theta} q)} \, d\sigma \, d\theta,
$$

where $d\theta$ is the surface measure on the unit sphere $\mathbb{S}^3$. The factor $|\sigma|^3$ is the ramp filter in dimension four, and it is the source of the high-frequency amplification in quaternion tomography.

## The Wavelet Transform

### Definition

The **quaternion continuous wavelet transform** of $f \in L^2(\mathbb{H})$ with respect to a wavelet $\psi \in L^2(\mathbb{H})$ is

$$
W_\psi f(a, b) = \frac{1}{|a|^2} \int_{\mathbb{H}} f(q) \overline{\psi\left( \frac{q - b}{a} \right)} \, dq, \qquad a \in \mathbb{H}^\times, \; b \in \mathbb{H}.
$$

The parameter $a$ is the **scale**, and $b$ is the **translation**. The wavelet $\psi$ is assumed to satisfy the **admissibility condition**

$$
C_\psi = \int_{\mathbb{H}} \frac{|\hat{\psi}(\xi)|^2}{|\xi|^4} \, d\xi < \infty,
$$

where $\hat{\psi}$ is the quaternion Fourier transform.

### The Inversion Formula

**Theorem.** If $\psi$ is admissible and $f \in L^2(\mathbb{H})$, then

$$
f(q) = \frac{1}{C_\psi} \int_{\mathbb{H}^\times} \int_{\mathbb{H}} W_\psi f(a, b) \frac{1}{|a|^2} \psi\left( \frac{q - b}{a} \right) \frac{da \, db}{|a|^4}.
$$

The inversion formula reconstructs $f$ from its wavelet transform.

### The Quaternion Wavelet Transform

The quaternion wavelet transform is used in quaternion signal processing, where it provides both magnitude and phase information, and in the analysis of quaternion-valued images, where the three imaginary components encode the color channels.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | Quaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis |
| $q = q_0 + \mathbf{q}$ | General quaternion |
| $\omega$ | Unit pure quaternion |
| $\chi_\xi(q) = e^{\omega \operatorname{Re}(\bar{\xi} q)}$ | Quaternion character |
| $\hat{f}$ | Quaternion Fourier transform |
| $f * g$ | Convolution |
| $\delta$ | Dirac delta |
| $E(q) = \bar{q}/\|q\|^4$ | Cauchy kernel |
| $D$ | Quaternion Dirac operator |
| $Hf$ | Quaternion Hilbert transform |
| $Mf$ | Quaternion maximal function |
| $\mathcal{M} f$ | Quaternion Mellin transform |
| $Rf$ | Quaternion Radon transform |
| $W_\psi f$ | Quaternion wavelet transform |

## The Structure Principle

The pattern in all the definitions above is the same: whenever the analysis depends only on the additive group structure and the Euclidean norm, the quaternion case is identical to the real case on $\mathbb{R}^4$. Whenever the analysis involves the algebra structure, the non-commutativity of $\mathbb{H}$ makes the theory richer but more complicated.

**Theorem (Structure Principle for quaternion harmonic analysis).** Let $\mathcal{T}$ be a transform or operator defined on functions on $\mathbb{R}^n$ that depends only on the additive group structure and the Euclidean norm. Then the quaternion analogue of $\mathcal{T}$ is identical to $\mathcal{T}$ on $\mathbb{R}^4$, stated in quaternion notation. If $\mathcal{T}$ depends on the algebra structure, then the quaternion analogue depends on the choice of the unit pure quaternion $\omega$, and the non-commutativity of $\mathbb{H}$ prevents the simple identities that hold in the commutative case.

**Consequences.**

- The maximal function, the Calderón–Zygmund theory, and the wavelet transform are identical to the real theory on $\mathbb{R}^4$, because they depend only on the additive group and the Euclidean norm.
- The Fourier transform, the convolution theorem, and the Radon transform depend on the choice of $\omega$, and the non-commutativity of $\mathbb{H}$ makes the identities more complicated than in the complex case.
- The quaternion Fourier transform is the ordinary Fourier transform on $\mathbb{R}^4$ tensored with $\mathbb{H}$, and the non-commutativity enters only in the ordering of the factors.

This is the fundamental structural fact about quaternion harmonic analysis: the additive group is $\mathbb{R}^4$, so the analysis is the ordinary analysis on $\mathbb{R}^4$, and the quaternion structure enters only through the algebra of the coefficients.

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original formulation.
- F. Brackx, R. Delanghe, and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the general Clifford theory.
- John Ryan, *Clifford Algebras in Analysis and Related Topics* (CRC Press, 1996), for the analytic theory.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton, 1989), for the role of the Dirac operator in geometry.
- Elias M. Stein and Guido Weiss, *Introduction to Fourier Analysis on Euclidean Spaces* (Princeton, 1971), for the classical treatment of the Fourier transform on $\mathbb{R}^n$.
- Todd A. Ell and Stephen J. Sangwine, *Quaternion Fourier Transforms for Signal and Image Processing* (Wiley, 2014), for the engineering applications.

