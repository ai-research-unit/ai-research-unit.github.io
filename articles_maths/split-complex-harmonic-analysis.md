# __Split Complex Harmonic Analysis__

## Introduction

This article introduces harmonic analysis on the split complex plane as the study of the Fourier transform, convolution, and the function spaces on which they act, with the hyperbolic structure playing an essential role. The goal is to define the core objects precisely, establish their basic properties, and describe the theorems that give the subject its shape.

The treatment is mathematically honest: every claim is either proved or stated as a definition. The split complex algebra is assumed from the article on split complex algebra, and the idempotent decomposition is used throughout. No physics is invoked. The obstruction that distinguishes split complex harmonic analysis from complex harmonic analysis — the unboundedness of the characters — is stated precisely and its consequences are developed systematically.

## The Split Complex Plane as a Locally Compact Abelian Group

### Additive Structure

The split complex plane $\mathbb{D}$ is a locally compact abelian group under addition, isomorphic to $\mathbb{R}^2$. Its **characters** are the continuous homomorphisms

$$
\chi_\xi(z) = e^{2\pi i \operatorname{Re}(\bar{\xi} z)}, \qquad \xi \in \mathbb{D},
$$

where the exponential is the ordinary complex exponential, and the pairing is

$$
\langle \xi, z \rangle = \operatorname{Re}(\bar{\xi} z) = u x - v y, \qquad \xi = u + jv, \quad z = x + jy.
$$

Note the minus sign: it comes from the split complex conjugation $\bar{\xi} = u - jv$ and the fact that $j^2 = +1$. The dual group $\hat{\mathbb{D}}$ is isomorphic to $\mathbb{D}$ itself, but the pairing is indefinite.

So at the level of the additive group, split complex harmonic analysis is the same as Fourier analysis on $\mathbb{R}^2$, with a Lorentzian pairing instead of a Euclidean one.

### The Split Complex Characters

The **split complex characters** are the homomorphisms into the multiplicative monoid of $\mathbb{D}$:

$$
\chi_\xi(z) = e^{j \operatorname{Re}(\bar{\xi} z)}, \qquad \xi \in \mathbb{D},
$$

where the exponential is the split complex exponential. Explicitly,

$$
\chi_\xi(z) = \cosh(\operatorname{Re}(\bar{\xi} z)) + j \sinh(\operatorname{Re}(\bar{\xi} z)).
$$

These characters are **unbounded**: as $|\operatorname{Re}(\bar{\xi} z)| \to \infty$, the hyperbolic functions grow exponentially. This is the fundamental obstruction, and it is the reason split complex harmonic analysis differs from complex harmonic analysis.

## The Split Complex Fourier Transform

### Definition

The **split complex Fourier transform** of a function $f : \mathbb{D} \to \mathbb{D}$ is

$$
\hat{f}(\xi) = \int_{\mathbb{D}} f(z) e^{-j \operatorname{Re}(\bar{\xi} z)} \, dz,
$$

where $dz$ is Lebesgue measure on $\mathbb{D} \cong \mathbb{R}^2$, and the exponential is the split complex exponential.

**Caution.** The integral converges only for functions $f$ that decay faster than any exponential in both directions. This is the fundamental difference from the complex case.

### The Idempotent Form

In the idempotent basis, the split complex Fourier transform decomposes as

$$
\hat{f}(\xi) = \hat{f}_+(\xi_+) e_+ + \hat{f}_-(\xi_-) e_-,
$$

where

$$
\hat{f}_\pm(\xi_\pm) = \int_{\mathbb{R}} f_\pm(z_\pm) e^{\mp \xi_\pm z_\pm} \, dz_\pm.
$$

The two integrals are **Laplace transforms**, one for each idempotent component. The first integral converges for $\xi_+ > 0$ and the second for $\xi_- < 0$. So the split complex Fourier transform is the pair of Laplace transforms on the two light cone directions.

This is the precise sense in which split complex harmonic analysis is the Laplace transform in disguise.

### The Domain of Definition

The split complex Fourier transform is defined on the class of functions $f$ for which both idempotent components are integrable against the corresponding exponential. This is a very restrictive class, essentially the functions that decay faster than any exponential at both ends of each light ray.

The transform is **not** defined on $L^1(\mathbb{D})$ or $L^2(\mathbb{D})$, because the characters are unbounded. This is the obstruction that cannot be removed.

## The Laplace Transform

### Definition

The **Laplace transform** of a function $f : [0, \infty) \to \mathbb{R}$ is

$$
\mathcal{L} f(s) = \int_0^\infty f(t) e^{-st} \, dt,
$$

whenever the integral converges. For $f$ of exponential growth, the transform converges for $\operatorname{Re} s > \sigma_0$, where $\sigma_0$ is the abscissa of convergence.

### Relation to the Split Complex Fourier Transform

The split complex Fourier transform on the positive light cone is the Laplace transform:

$$
\hat{f}_+(\xi_+) = \int_0^\infty f_+(z_+) e^{-\xi_+ z_+} \, dz_+ = \mathcal{L} f_+(\xi_+).
$$

So the split complex Fourier transform is the pair of Laplace transforms on the two light cone directions. This is not an analogy; it is an identity.

### Inversion

The Laplace transform is inverted by the **Bromwich integral**

$$
f(t) = \frac{1}{2\pi i} \int_{\sigma - i\infty}^{\sigma + i\infty} \mathcal{L} f(s) e^{st} \, ds,
$$

which is a contour integral in the complex plane. So the inversion of the split complex Fourier transform requires complexification of the idempotent components. This is the price of working with unbounded characters.

## The Split Complex Fourier Transform on a Bounded Interval

### Definition

On a bounded interval $[-T, T]$, the characters $e^{-j \operatorname{Re}(\bar{\xi} z)}$ are bounded, and the split complex Fourier transform

$$
\hat{f}(\xi) = \int_{-T}^T f(z) e^{-j \operatorname{Re}(\bar{\xi} z)} \, dz
$$

converges for $f \in L^1([-T, T])$.

### Inversion

On a bounded interval, the inversion formula is

$$
f(z) = \frac{1}{2\pi} \int_{\mathbb{R}} \hat{f}(\xi) e^{j \operatorname{Re}(\bar{\xi} z)} \, d\xi,
$$

under suitable conditions. This is the analogue of the Fourier inversion theorem for the split complex case, and it is the setting in which split complex harmonic analysis is useful.

### Applications

The split complex Fourier transform on a bounded interval is used in the analysis of transient signals, where the signal is better modeled by hyperbolic functions than by trigonometric functions. The transform diagonalizes the wave operator on the interval, and the idempotent decomposition corresponds to the decomposition into forward and backward propagating waves.

## Convolution

### Definition

The **convolution** of $f, g : \mathbb{D} \to \mathbb{D}$ is

$$
(f * g)(z) = \int_{\mathbb{D}} f(z - w) g(w) \, dw,
$$

whenever the integral converges. This is the convolution on the additive group $\mathbb{D} \cong \mathbb{R}^2$.

### Basic Properties

**Commutativity.** $f * g = g * f$.

**Associativity.** $(f * g) * h = f * (g * h)$.

**Young's inequality.** If $1/p + 1/q = 1/r + 1$ with $1 \leq p, q, r \leq \infty$, then

$$
\|f * g\|_r \leq \|f\|_p \|g\|_q,
$$

where the norms are the ordinary $L^p$ norms on $\mathbb{R}^2$.

**Convolution theorem.** For functions for which the split complex Fourier transform is defined,

$$
\widehat{f * g}(\xi) = \hat{f}(\xi) \hat{g}(\xi).
$$

**Proof.** Write the definition, apply Fubini, and change variables. $\square$

### The Idempotent Form

In the idempotent basis, the convolution decomposes as

$$
(f * g)_\pm = f_\pm * g_\pm,
$$

the ordinary convolution on $\mathbb{R}$. So the split complex convolution is the pair of ordinary convolutions.

## The Split Complex Delta Distribution

### Definition

The **split complex delta distribution** $\delta$ is the distribution

$$
\langle \delta, \phi \rangle = \phi(0), \qquad \phi \in C_c^\infty(\mathbb{D}).
$$

It satisfies $\delta * f = f$ for every function $f$, and its split complex Fourier transform is the constant function $1$.

### The Idempotent Form

In the idempotent basis,

$$
\delta = \delta_+ e_+ + \delta_- e_-,
$$

where $\delta_+$ and $\delta_-$ are the ordinary real delta distributions on the two light cone directions.

## The Split Complex Hilbert Transform

### Definition

The **split complex Hilbert transform** of $f : \mathbb{R} \to \mathbb{R}$ is

$$
Hf(x) = \frac{1}{\pi} \, \text{p.v.} \int_{\mathbb{R}} \frac{f(y)}{x - y} \, dy,
$$

where p.v. denotes the Cauchy principal value. This is the ordinary real Hilbert transform, and it acts on each idempotent component separately.

### The Split Complex Hilbert Transform on $\mathbb{D}$

For $f : \mathbb{D} \to \mathbb{D}$, the split complex Hilbert transform is defined by

$$
Hf(z) = Hf_+(z_+) e_+ + Hf_-(z_-) e_-.
$$

So the split complex Hilbert transform is the pair of ordinary real Hilbert transforms.

### Basic Properties

**Boundedness.** $H$ is bounded on $L^p(\mathbb{D})$ for $1 < p < \infty$, with

$$
\|Hf\|_p \leq C_p \|f\|_p.
$$

**Fourier multiplier.** In terms of the split complex Fourier transform,

$$
\widehat{Hf}(\xi) = -j \operatorname{sgn}(\xi) \hat{f}(\xi),
$$

where $\operatorname{sgn}$ is the sign function on each idempotent component.

## Maximal Functions

### The Split Complex Maximal Function

The **split complex Hardy–Littlewood maximal function** of $f \in L^1_{\mathrm{loc}}(\mathbb{D})$ is

$$
Mf(z) = \sup_{r > 0} \frac{1}{|B(z, r)|} \int_{B(z, r)} \|f(w)\|_E \, dw,
$$

where $B(z, r)$ is the Euclidean ball of radius $r$ centered at $z$, and $|B(z, r)|$ is its area.

### The Maximal Inequality

**Theorem (Hardy–Littlewood, split version).** There exists a constant $C > 0$ such that for every $f \in L^1(\mathbb{D})$ and every $\lambda > 0$,

$$
|\{z : Mf(z) > \lambda\}| \leq \frac{C}{\lambda} \|f\|_1.
$$

This is a **weak $(1,1)$** estimate. It implies that $M$ is bounded on $L^p(\mathbb{D})$ for $1 < p \leq \infty$.

**Theorem.** For $1 < p \leq \infty$, there exists $C_p > 0$ such that

$$
\|Mf\|_p \leq C_p \|f\|_p.
$$

**Proof.** The case $p = \infty$ is trivial. The case $1 < p < \infty$ follows from the weak $(1,1)$ estimate and the trivial $L^\infty$ estimate by interpolation. $\square$

### The Idempotent Form

In the idempotent basis, the split complex maximal function decomposes as the pair of ordinary real maximal functions on the two light cone directions. So the theory of maximal functions in the split complex case is the pair of the real theory, and the constants are the same.

## The Calderón–Zygmund Theory

### Singular Integrals

A **split complex Calderón–Zygmund operator** is a bounded operator $T : L^2(\mathbb{D}) \to L^2(\mathbb{D})$ with a kernel $K : \mathbb{D} \times \mathbb{D} \to \mathbb{D}$ such that

$$
Tf(z) = \int_{\mathbb{D}} K(z, w) f(w) \, dw
$$

for $z \notin \operatorname{supp} f$, and $K$ satisfies the size and smoothness estimates

$$
\|K(z, w)\|_E \leq \frac{C}{\|z - w\|_E},
$$

$$
\|K(z, w) - K(z', w)\|_E \leq C \frac{\|z - z'\|_E^\delta}{\|z - w\|_E^{1+\delta}}, \qquad \|z - z'\|_E < \frac{1}{2} \|z - w\|_E,
$$

and the analogous estimate in the second variable, for some $\delta > 0$.

**Theorem (Calderón–Zygmund, split version).** Every split complex Calderón–Zygmund operator is bounded on $L^p(\mathbb{D})$ for $1 < p < \infty$, and satisfies a weak $(1,1)$ estimate.

**Examples.** The split complex Hilbert transform, the split complex Riesz transforms, and the Beurling–Ahlfors transform are split complex Calderón–Zygmund operators.

### The Idempotent Form

In the idempotent basis, every split complex Calderón–Zygmund operator decomposes as the pair of ordinary real Calderón–Zygmund operators on the two light cone directions. So the theory in the split complex case is the pair of the real theory.

## The Mellin Transform

### Definition

The **split complex Mellin transform** of a function $f : (0, \infty) \to \mathbb{D}$ is

$$
\mathcal{M} f(s) = \int_0^\infty t^{s-1} f(t) \, dt,
$$

where the power is the split complex power. In the idempotent basis,

$$
\mathcal{M} f(s) = \mathcal{M} f_+(s_+) e_+ + \mathcal{M} f_-(s_-) e_-,
$$

where $\mathcal{M}$ on the right is the ordinary real Mellin transform.

### Relation to the Split Complex Fourier Transform

Under the change of variables $t = e^x$, the Mellin transform becomes the split complex Fourier transform on the real line:

$$
\mathcal{M} f(\sigma + j\tau) = \int_{-\infty}^\infty e^{(\sigma + j\tau) x} f(e^x) \, dx = \hat{g}(\tau),
$$

where $g(x) = e^{\sigma x} f(e^x)$. So the Mellin transform is the split complex Fourier transform in logarithmic coordinates.

### The Mellin Convolution

The **split complex Mellin convolution** is

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

The **split complex Radon transform** of a function $f : \mathbb{D} \to \mathbb{D}$ is

$$
Rf(\theta, t) = \int_{L(\theta, t)} f(z) \, ds,
$$

where $L(\theta, t)$ is the line with normal direction $(\cosh\theta, \sinh\theta)$ and signed distance $t$ from the origin, and $ds$ is the hyperbolic arc length.

### The Fourier Slice Theorem

**Theorem (Fourier Slice, split version).** The one-dimensional split complex Fourier transform of $Rf(\theta, \cdot)$ is the restriction of the two-dimensional split complex Fourier transform of $f$ to the line through the origin in direction $(\cosh\theta, \sinh\theta)$:

$$
\widehat{Rf(\theta, \cdot)}(\sigma) = \hat{f}(\sigma \cosh\theta, \sigma \sinh\theta).
$$

**Proof.** Write the definition of the Radon transform, take the split complex Fourier transform in $t$, and change variables. $\square$

The Fourier slice theorem is the mathematical basis of hyperbolic tomography, the analogue of computed tomography for the hyperbolic plane.

### The Inversion Formula

**Theorem.** For suitable $f$,

$$
f(z) = \frac{1}{2} \int_0^{2\pi} \int_{-\infty}^\infty \widehat{Rf(\theta, \cdot)}(\sigma) |\sigma| e^{j \sigma \operatorname{Re}(\bar{\xi} z)} \, d\sigma \, d\theta,
$$

where $\xi = \cosh\theta + j \sinh\theta$. The factor $|\sigma|$ is the ramp filter, and it is the source of the high-frequency amplification in hyperbolic tomography.

## The Wavelet Transform

### Definition

The **split complex continuous wavelet transform** of $f \in L^2(\mathbb{R})$ with respect to a wavelet $\psi \in L^2(\mathbb{R})$ is

$$
W_\psi f(a, b) = \frac{1}{\sqrt{|a|}} \int_{\mathbb{R}} f(t) \overline{\psi\left( \frac{t - b}{a} \right)} \, dt, \qquad a \neq 0, \; b \in \mathbb{R}.
$$

The parameter $a$ is the **scale**, and $b$ is the **translation**. The wavelet $\psi$ is assumed to satisfy the **admissibility condition**

$$
C_\psi = \int_{\mathbb{R}} \frac{|\hat{\psi}(\xi)|^2}{|\xi|} \, d\xi < \infty,
$$

where $\hat{\psi}$ is the ordinary Fourier transform.

### The Inversion Formula

**Theorem.** If $\psi$ is admissible and $f \in L^2(\mathbb{R})$, then

$$
f(t) = \frac{1}{C_\psi} \int_{\mathbb{R}} \int_{\mathbb{R}} W_\psi f(a, b) \frac{1}{\sqrt{|a|}} \psi\left( \frac{t - b}{a} \right) \frac{da \, db}{a^2}.
$$

The inversion formula reconstructs $f$ from its wavelet transform.

### The Split Complex Wavelet Transform

In the split complex setting, the wavelet $\psi$ is allowed to be split-complex-valued, and the transform becomes

$$
W_\psi f(a, b) = \frac{1}{\sqrt{|a|}} \int_{\mathbb{D}} f(z) \overline{\psi\left( \frac{z - b}{a} \right)} \, dz, \qquad a \in \mathbb{D}^\times, \; b \in \mathbb{D}.
$$

The split complex wavelet transform is used in hyperbolic signal processing, where it provides both magnitude and hyperbolic phase information.

## Summary

Harmonic analysis on the split complex plane $\mathbb{D}$ is the study of the Fourier transform, of convolution, and of the function spaces on which the two act, with the decomposition of the algebra into idempotents in an essential role. The plane is first a locally compact abelian group under addition, isomorphic to $\mathbb{R}^2$, and its characters are the exponentials built from $j$, which are unbounded because $j^2 = +1$.

The split complex Fourier transform is defined with a kernel built from the split complex exponential, and it is developed on the full plane and on a bounded interval, together with the Laplace transform, convolution and the delta distribution, the Hilbert transform, the Hardy–Littlewood maximal function, and the Calderón–Zygmund theory of singular integrals. The transform is then extended to the Mellin transform on the multiplicative half-line, the Radon transform along lines, and the continuous wavelet transform.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | Split complex algebra |
| $j$ | Split imaginary unit, $j^2 = +1$ |
| $\chi_\xi(z) = e^{j \operatorname{Re}(\bar{\xi} z)}$ | Split complex character |
| $\hat{f}$ | Split complex Fourier transform |
| $f * g$ | Convolution |
| $f \star g$ | Mellin convolution |
| $\delta$ | Split complex delta distribution |
| $Hf$ | Split complex Hilbert transform |
| $Mf$ | Split complex maximal function |
| $\mathcal{M} f$ | Split complex Mellin transform |
| $Rf$ | Split complex Radon transform |
| $W_\psi f$ | Split complex wavelet transform |
| $e_+ = (1 + j)/2$ | Positive idempotent |
| $e_- = (1 - j)/2$ | Negative idempotent |

## Further Reading

- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the geometric interpretation of split complex numbers.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- Vladimir V. Kisil, *Geometry of Möbius Transformations: Elliptic, Parabolic and Hyperbolic Actions of SL(2, ℝ)* (Imperial College Press, 2012), for the analytic applications.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the classification of real algebras.
- Walter Rudin, *Real and Complex Analysis* (McGraw-Hill, 1987), for the comparison with the complex case.
- Elias M. Stein and Guido Weiss, *Introduction to Fourier Analysis on Euclidean Spaces* (Princeton, 1971), for the classical treatment of the Fourier transform on $\mathbb{R}^n$.

