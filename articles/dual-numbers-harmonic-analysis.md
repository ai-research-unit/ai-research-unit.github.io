
# Dual Numbers Harmonic Analysis

## Introduction

This article introduces harmonic analysis on the dual plane as the study of the Fourier transform, convolution, and the function spaces on which they act, with the nilpotent structure playing an essential role. The goal is to define the core objects precisely, establish their basic properties, and describe the theorems that give the subject its shape.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. No examples are given. The dual number algebra is assumed from the article on dual numbers algebra, and the maximal ideal is used throughout. The article is stated for an arbitrary commutative ring $R$ in which $2$ is invertible, and no finiteness assumption is made unless stated.

Throughout this article, the dual number algebra is denoted $\mathbb{D}'$, and the split complex algebra is denoted $\mathbb{D}$. The unit of $\mathbb{D}'$ is denoted $\varepsilon$, and it satisfies $\varepsilon^2 = 0$.

## The Dual Plane as a Locally Compact Abelian Group

### Additive Structure

The dual plane $\mathbb{D}'$ is a locally compact abelian group under addition, isomorphic to $R^2$ when $R = \mathbb{R}$. Its **characters** are the continuous homomorphisms into the circle group. Since the additive group of $\mathbb{D}'$ is just $\mathbb{R}^2$, the characters are the ordinary two-dimensional Fourier characters:

$$
\chi_\xi(z) = e^{2\pi i \langle \xi, z \rangle}, \qquad \xi \in \mathbb{D}',
$$

where the exponential is the ordinary complex exponential, and the pairing is

$$
\langle \xi, z \rangle = u x + v y, \qquad \xi = u + v\varepsilon, \quad z = x + y\varepsilon.
$$

The pairing is the ordinary Euclidean pairing on $\mathbb{R}^2$: it pairs the real coordinate $u$ with $x$ and the infinitesimal coefficient $v$ with $y$. It is **not** $\operatorname{Re}(\bar{\xi} z)$: for dual numbers $\operatorname{Re}(\bar{\xi} z) = u x$, because the term $-vy\,\varepsilon^2$ vanishes since $\varepsilon^2 = 0$. The dual conjugation acts as the identity on the real part and negates the infinitesimal part, and it cannot supply the pairing of the two real coordinates that the additive characters require.

So at the level of the additive group, dual harmonic analysis is the same as Fourier analysis on $\mathbb{R}^2$, with a degenerate pairing.

### The Dual Characters

The **dual characters** are the homomorphisms into the multiplicative monoid of $\mathbb{D}'$:

$$
\chi_\xi(z) = e^{\langle \xi, z \rangle \varepsilon}, \qquad \xi \in \mathbb{D}',
$$

where the exponential is the dual exponential. Because $\varepsilon^2 = 0$, this is

$$
\chi_\xi(z) = 1 + \langle \xi, z \rangle \varepsilon.
$$

These characters take values in the affine line $1 + \mathbb{D}' \varepsilon$, and their Euclidean norm $\sqrt{1 + \langle \xi, z \rangle^2}$ grows only linearly in the coordinates. This is the fundamental difference from the split complex case, where the characters grow exponentially.

So the dual case is intermediate between the complex case, where the characters take values in the compact circle, and the split complex case, where the characters take values in the non-compact hyperbola. In the dual case, the characters take values in the affine line $1 + \mathfrak{m}$, so their deviation from the identity lies in the nilpotent maximal ideal.

## The Dual Fourier Transform

### Definition

The **dual Fourier transform** of a function $f : \mathbb{D}' \to \mathbb{D}'$ is

$$
\hat{f}(\xi) = \int_{\mathbb{D}'} f(z) e^{- \langle \xi, z \rangle \varepsilon} \, dz,
$$

where $dz$ is Lebesgue measure on $\mathbb{D}' \cong \mathbb{R}^2$, and the exponential is the dual exponential. Because $\varepsilon^2 = 0$, this is

$$
\hat{f}(\xi) = \int_{\mathbb{D}'} f(z) (1 - \langle \xi, z \rangle \varepsilon) \, dz.
$$

So the dual Fourier transform is the ordinary two-dimensional Fourier transform of the real part, plus an infinitesimal correction given by the first moment of the function.

### The Structure of the Transform

Write $f(z) = u(x, y) + v(x, y) \varepsilon$. Then

$$
\hat{f}(\xi) = \int_{\mathbb{R}^2} u(x, y) \, dx \, dy + \left( \int_{\mathbb{R}^2} v(x, y) \, dx \, dy - \int_{\mathbb{R}^2} u(x, y) \langle \xi, z \rangle \, dx \, dy \right) \varepsilon.
$$

So the dual Fourier transform has:

- A real part that is the total integral of the real part of $f$, independent of $\xi$.
- An infinitesimal part that is the total integral of the infinitesimal part of $f$, minus the first moment of the real part of $f$ against the character.

This is the fundamental structural fact about the dual Fourier transform: the real part is constant in $\xi$, and the infinitesimal part is affine in $\xi$. The transform does not oscillate, because the characters have nilpotent deviation from the identity and do not wrap around the circle.

### Comparison with the Complex and Split Cases

| Property | Complex | Split Complex | Dual |
|---|---|---|---|
| Characters | $e^{i\xi x}$, bounded | $e^{j\xi x}$, unbounded | $1 + \xi x \varepsilon$, linear growth |
| Transform converges | for $f \in L^1$ | only for rapid decay | for $f \in L^1$ |
| Real part of transform | oscillatory | exponential | constant |
| Infinitesimal part | — | — | affine in $\xi$ |
| Plancherel | yes | no | degenerate |

So the dual case is the only one of the three where the transform converges on $L^1$ and is bounded, but the transform is degenerate in the sense that the real part is constant and the infinitesimal part is affine. This is a consequence of the nilpotence of $\varepsilon$.

## The Dual Fourier Transform on a Bounded Interval

### Definition

On a bounded interval $[-T, T]^2$, the dual Fourier transform

$$
\hat{f}(\xi) = \int_{[-T, T]^2} f(z) e^{- \langle \xi, z \rangle \varepsilon} \, dz
$$

converges for $f \in L^1([-T, T]^2)$. The transform has the same structure as above: the real part is the total integral of the real part of $f$, and the infinitesimal part is the total integral of the infinitesimal part minus the first moment of the real part.

### Inversion

The inversion formula is

$$
f(z) = \frac{1}{(2\pi)^2} \int_{\mathbb{R}^2} \hat{f}(\xi) e^{\langle \xi, z \rangle \varepsilon} \, d\xi,
$$

under suitable conditions. Because $\varepsilon^2 = 0$, this reduces to

$$
f(z) = \frac{1}{(2\pi)^2} \int_{\mathbb{R}^2} \hat{f}(\xi) (1 + \langle \xi, z \rangle \varepsilon) \, d\xi.
$$

The real part of the inversion recovers the total integral, and the infinitesimal part recovers the first moment. So the inversion is not a true inversion: it recovers only the total integral and the first moment of the function, not the function itself. This is the degeneracy of the dual Fourier transform.

### Why the Inversion Is Not Complete

The dual Fourier transform loses information because the characters $1 + \xi x \varepsilon$ are linear in $\xi$ and do not oscillate. The transform is essentially the map

$$
f \mapsto \left( \int f, \int f \cdot z \right),
$$

which records only the zeroth and first moments. Higher moments are lost. So the dual Fourier transform is not invertible on $L^1$, and it does not have a Plancherel theorem in the usual sense.

This is the fundamental limitation of dual harmonic analysis: the nilpotence of $\varepsilon$ means that the characters are too simple to resolve the function, and the transform is a moment map rather than a true Fourier transform.

## Convolution

### Definition

The **convolution** of $f, g : \mathbb{D}' \to \mathbb{D}'$ is

$$
(f * g)(z) = \int_{\mathbb{D}'} f(z - w) g(w) \, dw,
$$

whenever the integral converges. This is the convolution on the additive group $\mathbb{D}' \cong \mathbb{R}^2$.

### Basic Properties

**Commutativity.** $f * g = g * f$.

**Associativity.** $(f * g) * h = f * (g * h)$.

**Young's inequality.** If $1/p + 1/q = 1/r + 1$ with $1 \leq p, q, r \leq \infty$, then

$$
\|f * g\|_r \leq \|f\|_p \|g\|_q,
$$

where the norms are the ordinary $L^p$ norms on $\mathbb{R}^2$.

**Convolution theorem.** For functions for which the dual Fourier transform is defined,

$$
\widehat{f * g}(\xi) = \hat{f}(\xi) \hat{g}(\xi).
$$

**Proof.** Write the definition, apply Fubini, and change variables. $\square$

### The Structure of the Convolution Theorem

Because the dual Fourier transform is a moment map, the convolution theorem says that the moments of the convolution are the products of the moments of the factors. Explicitly, if

$$
\hat{f} = F_0 + F_1 \varepsilon, \qquad \hat{g} = G_0 + G_1 \varepsilon,
$$

then

$$
\widehat{f * g} = F_0 G_0 + (F_0 G_1 + F_1 G_0) \varepsilon.
$$

So the zeroth moment of the convolution is the product of the zeroth moments, and the first moment is the sum of the cross terms. This is the algebraic content of the convolution theorem in the dual case.

### Approximate Identities

A sequence $(\phi_n)$ in $L^1(\mathbb{D}')$ is an **approximate identity** if

$$
\int_{\mathbb{D}'} \phi_n = 1, \qquad \sup_n \|\phi_n\|_1 < \infty, \qquad \int_{\|z\|_E > \delta} |\phi_n(z)| \, dz \to 0
$$

for every $\delta > 0$.

**Theorem.** If $(\phi_n)$ is an approximate identity and $f \in L^p(\mathbb{D}')$ for $1 \leq p < \infty$, then

$$
\|f * \phi_n - f\|_p \to 0.
$$

This is the same as in the real case, because the additive group of $\mathbb{D}'$ is just $\mathbb{R}^2$.

## Distributions

### Definition

A **tempered distribution** on $\mathbb{D}'$ is a continuous linear functional on the Schwartz space $\mathcal{S}(\mathbb{D}')$. The space of tempered distributions is denoted $\mathcal{S}'(\mathbb{D}')$. It includes all functions in $L^p(\mathbb{D}')$ for $1 \leq p \leq \infty$, all finite measures, and all derivatives of such objects.

### Operations on Distributions

**Differentiation.** For $T \in \mathcal{S}'(\mathbb{D}')$ and $\phi \in \mathcal{S}(\mathbb{D}')$,

$$
\langle \partial_x T, \phi \rangle = -\langle T, \partial_x \phi \rangle, \qquad \langle \partial_y T, \phi \rangle = -\langle T, \partial_y \phi \rangle.
$$

**Multiplication by a function.** For $f \in C^\infty(\mathbb{D}')$ with polynomial growth and $T \in \mathcal{S}'(\mathbb{D}')$,

$$
\langle f T, \phi \rangle = \langle T, f \phi \rangle.
$$

**Dual Fourier transform.** For $T \in \mathcal{S}'(\mathbb{D}')$ and $\phi \in \mathcal{S}(\mathbb{D}')$,

$$
\langle \hat{T}, \phi \rangle = \langle T, \hat{\phi} \rangle.
$$

The dual Fourier transform is a bijection $\mathcal{S}'(\mathbb{D}') \to \mathcal{S}'(\mathbb{D}')$.

### The Dirac Delta

The **Dirac delta** $\delta$ is the tempered distribution

$$
\langle \delta, \phi \rangle = \phi(0).
$$

Its dual Fourier transform is the constant function $1$, and the dual Fourier transform of $1$ is $\delta$. The delta is the identity for convolution: $\delta * T = T$ for every tempered distribution $T$.

### The Infinitesimal Delta

The **infinitesimal delta** is the distribution

$$
\langle \delta_\varepsilon, \phi \rangle = \partial_\varepsilon \phi(0),
$$

where $\partial_\varepsilon$ is the derivation that extracts the infinitesimal part. It is the distributional content of the maximal ideal, and it is the dual analogue of the derivative of the delta.

## The Dual Hilbert Transform

### Definition

The **dual Hilbert transform** of $f : \mathbb{R} \to \mathbb{R}$ is

$$
Hf(x) = \frac{1}{\pi} \, \text{p.v.} \int_{\mathbb{R}} \frac{f(y)}{x - y} \, dy,
$$

where p.v. denotes the Cauchy principal value. This is the ordinary real Hilbert transform, and it acts on the real part of the dual function.

### The Dual Hilbert Transform on $\mathbb{D}'$

For $f : \mathbb{D}' \to \mathbb{D}'$, the dual Hilbert transform is defined by

$$
Hf(z) = Hf_r(x) + Hf_i(x) \varepsilon,
$$

where $f_r$ and $f_i$ are the real and infinitesimal parts of $f$. So the dual Hilbert transform is the ordinary real Hilbert transform applied to each component separately.

### Basic Properties

**Boundedness.** $H$ is bounded on $L^p(\mathbb{D}')$ for $1 < p < \infty$, with

$$
\|Hf\|_p \leq C_p \|f\|_p.
$$

**Fourier multiplier.** In terms of the dual Fourier transform,

$$
\widehat{Hf}(\xi) = -i \operatorname{sgn}(\xi) \hat{f}(\xi),
$$

where $\operatorname{sgn}$ is the sign function on the real part.

## Maximal Functions

### The Dual Maximal Function

The **dual Hardy–Littlewood maximal function** of $f \in L^1_{\mathrm{loc}}(\mathbb{D}')$ is

$$
Mf(z) = \sup_{r > 0} \frac{1}{|B(z, r)|} \int_{B(z, r)} \|f(w)\|_E \, dw,
$$

where $B(z, r)$ is the Euclidean ball of radius $r$ centered at $z$, and $|B(z, r)|$ is its area.

### The Maximal Inequality

**Theorem (Hardy–Littlewood, dual version).** There exists a constant $C > 0$ such that for every $f \in L^1(\mathbb{D}')$ and every $\lambda > 0$,

$$
|\{z : Mf(z) > \lambda\}| \leq \frac{C}{\lambda} \|f\|_1.
$$

This is a **weak $(1,1)$** estimate. It implies that $M$ is bounded on $L^p(\mathbb{D}')$ for $1 < p \leq \infty$.

**Theorem.** For $1 < p \leq \infty$, there exists $C_p > 0$ such that

$$
\|Mf\|_p \leq C_p \|f\|_p.
$$

**Proof.** The case $p = \infty$ is trivial. The case $1 < p < \infty$ follows from the weak $(1,1)$ estimate and the trivial $L^\infty$ estimate by interpolation. $\square$

### The Structure of the Maximal Function

Because the additive group of $\mathbb{D}'$ is just $\mathbb{R}^2$, the maximal function theory is identical to the real theory on $\mathbb{R}^2$. The nilpotence of $\varepsilon$ does not affect the maximal function, because the maximal function is defined in terms of the Euclidean norm, which does not see the algebra structure.

## The Calderón–Zygmund Theory

### Singular Integrals

A **dual Calderón–Zygmund operator** is a bounded operator $T : L^2(\mathbb{D}') \to L^2(\mathbb{D}')$ with a kernel $K : \mathbb{D}' \times \mathbb{D}' \to \mathbb{D}'$ such that

$$
Tf(z) = \int_{\mathbb{D}'} K(z, w) f(w) \, dw
$$

for $z \notin \operatorname{supp} f$, and $K$ satisfies the size and smoothness estimates

$$
\|K(z, w)\|_E \leq \frac{C}{\|z - w\|_E},
$$

$$
\|K(z, w) - K(z', w)\|_E \leq C \frac{\|z - z'\|_E^\delta}{\|z - w\|_E^{1+\delta}}, \qquad \|z - z'\|_E < \frac{1}{2} \|z - w\|_E,
$$

and the analogous estimate in the second variable, for some $\delta > 0$.

**Theorem (Calderón–Zygmund, dual version).** Every dual Calderón–Zygmund operator is bounded on $L^p(\mathbb{D}')$ for $1 < p < \infty$, and satisfies a weak $(1,1)$ estimate.

**Examples.** The dual Hilbert transform, the dual Riesz transforms, and the Beurling–Ahlfors transform are dual Calderón–Zygmund operators.

### The Structure of the Theory

Because the additive group of $\mathbb{D}'$ is just $\mathbb{R}^2$, the Calderón–Zygmund theory is identical to the real theory on $\mathbb{R}^2$. The nilpotence of $\varepsilon$ does not affect the theory, because the kernel estimates are in terms of the Euclidean norm, which does not see the algebra structure.

So the dual Calderón–Zygmund theory is the real theory on $\mathbb{R}^2$, stated in dual notation. This is a general phenomenon: whenever the analysis depends only on the additive group structure and the Euclidean norm, the dual case is identical to the real case. The nilpotence of $\varepsilon$ only matters when the algebra structure enters, as in the Fourier transform and the convolution theorem.

## The Mellin Transform

### Definition

The **dual Mellin transform** of a function $f : (0, \infty) \to \mathbb{D}'$ is

$$
\mathcal{M} f(s) = \int_0^\infty t^{s-1} f(t) \, dt,
$$

where the power is the dual power. For $s = \sigma + \tau \varepsilon$ and $f = f_r + f_i \varepsilon$,

$$
\mathcal{M} f(s) = \int_0^\infty t^{\sigma-1} f_r(t) \, dt + \left( \int_0^\infty t^{\sigma-1} \left( f_i(t) + \tau \log t \, f_r(t) \right) dt \right) \varepsilon.
$$

So the dual Mellin transform has a real part that is the ordinary Mellin transform of the real part of $f$, and an infinitesimal part that involves the Mellin transform of the infinitesimal part plus the Mellin transform of the real part against $\log t$.

### Relation to the Dual Fourier Transform

Under the change of variables $t = e^x$, the Mellin transform becomes the dual Fourier transform on the real line:

$$
\mathcal{M} f(\sigma + \tau \varepsilon) = \int_{-\infty}^\infty e^{(\sigma + \tau \varepsilon) x} f(e^x) \, dx = \hat{g}(\tau),
$$

where $g(x) = e^{\sigma x} f(e^x)$. So the Mellin transform is the dual Fourier transform in logarithmic coordinates.

## The Radon Transform

### Definition

The **dual Radon transform** of a function $f : \mathbb{D}' \to \mathbb{D}'$ is

$$
Rf(\theta, t) = \int_{L(\theta, t)} f(z) \, ds,
$$

where $L(\theta, t)$ is the line with normal direction $(\cos\theta, \sin\theta)$ and signed distance $t$ from the origin, and $ds$ is the Euclidean arc length.

### The Fourier Slice Theorem

**Theorem (Fourier Slice, dual version).** The one-dimensional dual Fourier transform of $Rf(\theta, \cdot)$ is the restriction of the two-dimensional dual Fourier transform of $f$ to the line through the origin in direction $(\cos\theta, \sin\theta)$:

$$
\widehat{Rf(\theta, \cdot)}(\sigma) = \hat{f}(\sigma \cos\theta, \sigma \sin\theta).
$$

**Proof.** Write the definition of the Radon transform, take the dual Fourier transform in $t$, and change variables. $\square$

The Fourier slice theorem is the mathematical basis of dual tomography, the analogue of computed tomography for the dual plane.

### The Inversion Formula

**Theorem.** For suitable $f$,

$$
f(z) = \frac{1}{2} \int_0^{2\pi} \int_{-\infty}^\infty \widehat{Rf(\theta, \cdot)}(\sigma) |\sigma| e^{\langle \xi, z \rangle \varepsilon} \, d\sigma \, d\theta,
$$

where $\xi = \sigma \cos\theta + \sigma \sin\theta \varepsilon$. The factor $|\sigma|$ is the ramp filter, and it is the source of the high-frequency amplification in dual tomography.

## The Wavelet Transform

### Definition

The **dual continuous wavelet transform** of $f \in L^2(\mathbb{R})$ with respect to a wavelet $\psi \in L^2(\mathbb{R})$ is

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

### The Dual Wavelet Transform

In the dual setting, the wavelet $\psi$ is allowed to be dual-valued, and the transform becomes

$$
W_\psi f(a, b) = \frac{1}{\sqrt{|a|}} \int_{\mathbb{D}'} f(z) \overline{\psi\left( \frac{z - b}{a} \right)} \, dz, \qquad a \in (\mathbb{D}')^\times, \; b \in \mathbb{D}'.
$$

The dual wavelet transform is used in infinitesimal signal processing, where it provides both the value and the derivative information.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}'$ | Dual number algebra |
| $\varepsilon$ | Dual unit, $\varepsilon^2 = 0$ |
| $\chi_\xi(z) = 1 + \langle \xi, z \rangle \varepsilon$ | Dual character |
| $\hat{f}$ | Dual Fourier transform |
| $f * g$ | Convolution |
| $\delta$ | Dirac delta |
| $Hf$ | Dual Hilbert transform |
| $Mf$ | Dual maximal function |
| $\mathcal{M} f$ | Dual Mellin transform |
| $Rf$ | Dual Radon transform |
| $W_\psi f$ | Dual wavelet transform |
| $\mathfrak{m} = (\varepsilon)$ | Maximal ideal |

## The Structure Principle

The pattern in all the definitions above is the same: whenever the analysis depends only on the additive group structure and the Euclidean norm, the dual case is identical to the real case on $\mathbb{R}^2$. Whenever the analysis involves the algebra structure, the nilpotence of $\varepsilon$ makes the theory degenerate.

**Theorem (Structure Principle for harmonic analysis).** Let $\mathcal{T}$ be a transform or operator defined on functions on $\mathbb{R}^n$ that depends only on the additive group structure and the Euclidean norm. Then the dual analogue of $\mathcal{T}$ is identical to $\mathcal{T}$ on $\mathbb{R}^2$, stated in dual notation. If $\mathcal{T}$ depends on the algebra structure, then the dual analogue is degenerate, and the degeneracy is controlled by the nilpotence of $\varepsilon$.

**Consequences.**

- The maximal function, the Calderón–Zygmund theory, and the wavelet transform are identical to the real theory, because they depend only on the additive group and the Euclidean norm.
- The Fourier transform, the convolution theorem, and the Radon transform are degenerate, because they depend on the algebra structure through the characters.
- The degeneracy is always of the same form: the real part of the transform is constant or affine, and the infinitesimal part is linear in the dual variable.

This is the fundamental limitation of dual harmonic analysis: the nilpotence of $\varepsilon$ means that the characters are too simple to resolve the function, and the transform is a moment map rather than a true Fourier transform. The theory is useful in the cases where the additive group structure is all that matters, and degenerate in the cases where the algebra structure enters.

## Further Reading

- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the origin of the dual numbers in the biquaternion program.
- Eduard Study, *Geometrie der Dynamen* (1903), for the geometry of dual numbers.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the classification of real algebras.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings* (Springer, 1991), for the theory of algebras over commutative rings.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (AMS, 2005), for the general theory of quadratic forms.
- Elias M. Stein and Guido Weiss, *Introduction to Fourier Analysis on Euclidean Spaces* (Princeton, 1971), for the classical treatment of the Fourier transform on $\mathbb{R}^n$.
- Andreas Griewank and Andrea Walther, *Evaluating Derivatives* (SIAM, 2008), for automatic differentiation with dual numbers.

