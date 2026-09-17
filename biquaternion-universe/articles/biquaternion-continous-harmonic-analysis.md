
# Biquaternion Continuous Harmonic Analysis

## Introduction

This article introduces harmonic analysis for biquaternion-valued functions of a real variable. It follows the article on biquaternion discrete harmonic analysis, which defined the discrete biquaternion Fourier transform, and it uses the analysis article, which defined the biquaternion gradient, the d'Alembertian, and the convective derivative on the four-dimensional subspaces of $\mathbb{B}$.

The treatment is purely mathematical. The goal is to define the continuous biquaternion Fourier transform, establish its basic properties, show how it decomposes into ordinary complex Fourier transforms, and identify the points where the biquaternion structure creates genuinely new phenomena. The relation to the differential operators of the analysis article is the main structural content of this article.

The key structural fact is the same as in the discrete case: the Fourier kernel is a biquaternion exponential, and the exponential is defined by a **root of $-1$**. The choice of root determines the nature of the transform, and the transform decomposes into a finite number of ordinary complex Fourier transforms. The genuinely biquaternionic content is the choice of root, the decomposition, and the vanishing-norm issue.

Throughout, a biquaternion is written

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3, \qquad Q_\mu \in \mathbb{C},
$$

or, more compactly, as

$$
\tilde{Q} = Q_0 e_0 + \mathbf{Q}, \qquad \mathbf{Q} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3.
$$

The scalar imaginary is $i$, which commutes with the quaternion units. The quaternion conjugate is $\bar{\tilde{Q}} = Q_0 e_0 - \mathbf{Q}$, and the norm form is $N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}}$.

**Notation.** To avoid collision with the standard basis $\{e_0, e_1, e_2, e_3\}$ and with the scalar imaginary $i$, the root of $-1$ used in the Fourier kernel is denoted $\rho$ throughout. This is a local convention; the roots themselves are the objects classified in the division theory article.

## The Fourier Kernel

### Definition

Fix a root $\rho$ of $-1$, i.e., an element $\rho \in \mathbb{B}$ with

$$
\rho^2 = -e_0.
$$

The **biquaternion Fourier kernel** is the function

$$
W(t, \omega) = \exp(-2\pi \rho \omega t), \qquad t, \omega \in \mathbb{R}.
$$

Because $\rho^2 = -e_0$, the kernel takes the closed form

$$
W(t, \omega) = \cos(2\pi \omega t) \, e_0 - \sin(2\pi \omega t) \, \rho,
$$

where the cosine and sine are the ordinary real trigonometric functions applied to the real argument $2\pi \omega t$. The kernel is therefore a unit biquaternion:

$$
N(W(t, \omega)) = \cos^2(2\pi \omega t) + \sin^2(2\pi \omega t) = 1, \qquad N(W(t, \omega)) = e_0.
$$

In particular, the kernel is always invertible, and its inverse is its quaternion conjugate:

$$
W(t, \omega)^{-1} = \overline{W(t, \omega)} = \cos(2\pi \omega t) \, e_0 + \sin(2\pi \omega t) \, \rho.
$$

### The Condition on the Root

A biquaternion $\rho$ satisfies $\rho^2 = -e_0$ if and only if it is a pure biquaternion (i.e., its scalar part vanishes) and

$$
\Re(\rho) \perp \Im(\rho), \qquad \|\Re(\rho)\| - \|\Im(\rho)\| = 1,
$$

where $\Re(\rho)$ and $\Im(\rho)$ are the real and imaginary quaternion parts of $\rho$. This is the content of the classification of the biquaternion roots of $-1$ given in the division theory article. The classification yields three families: the scalar imaginary $\rho = \pm i$, the unit pure real quaternions $\rho = \pm \mu_{\mathbb{R}}$, and the non-trivial roots $\rho = b\mu + d\nu i$ with $\mu \perp \nu$ and $b^2 - d^2 = 1$.

The three families give three essentially different Fourier transforms, as in the discrete case.

## The Continuous Transform Pair

### Definition

Let $f : \mathbb{R} \to \mathbb{B}$ be a biquaternion-valued function. The **continuous biquaternion Fourier transform** of $f$ is

$$
F(\omega) = \int_{-\infty}^{\infty} W(t, \omega) f(t) \, dt = \int_{-\infty}^{\infty} \exp(-2\pi \rho \omega t) f(t) \, dt, \qquad \omega \in \mathbb{R},
$$

provided the integral converges. The **inverse transform** is

$$
f(t) = \int_{-\infty}^{\infty} \overline{W(t, \omega)} F(\omega) \, d\omega = \int_{-\infty}^{\infty} \exp(2\pi \rho \omega t) F(\omega) \, d\omega,
$$

provided the integral converges.

The placement of the kernel on the **left** of $f(t)$ is a choice. An alternative transform has the kernel on the right:

$$
F(\omega) = \int_{-\infty}^{\infty} f(t) \, W(t, \omega) \, dt.
$$

The two transforms are related as in the discrete case: the left-kernel transform of $f$ equals the right-kernel transform of the conjugate of $f$, with a sign change in the kernel.

### Convergence

The integral defining the transform converges absolutely if $f$ is integrable, i.e., if

$$
\int_{-\infty}^{\infty} \|f(t)\|_E \, dt < \infty.
$$

Under this condition, the transform $F$ is bounded and uniformly continuous:

$$
\|F(\omega)\|_E \leq \int_{-\infty}^{\infty} \|f(t)\|_E \, dt, \qquad \omega \in \mathbb{R}.
$$

The convergence of the inverse transform requires additional conditions, as in the ordinary complex case. The standard conditions are:

- $f$ is integrable and continuous at the point $t$.
- $F$ is integrable.
- The kernel is chosen so that the inversion formula holds pointwise.

Under these conditions, the inverse formula holds at every point of continuity of $f$.

### The Riemann–Lebesgue Lemma

**Theorem (Riemann–Lebesgue).** If $f : \mathbb{R} \to \mathbb{B}$ is integrable, then

$$
\lim_{|\omega| \to \infty} \|F(\omega)\|_E = 0.
$$

**Proof.** The kernel is bounded and the integrand is integrable. The standard proof for the complex Fourier transform applies component-wise, and the result follows from the component-wise statement. $\square$

### The Inversion Theorem

**Theorem (inversion).** Let $f : \mathbb{R} \to \mathbb{B}$ be integrable and continuous at a point $t \in \mathbb{R}$, and let $F$ be integrable. Then

$$
f(t) = \int_{-\infty}^{\infty} \overline{W(t, \omega)} F(\omega) \, d\omega.
$$

**Proof.** The proof follows the standard proof of the inversion theorem for the complex Fourier transform, applied component-wise in the basis $\{e_0, \rho, \nu, \xi\}$ introduced below. The key step is the approximation of the identity by a sequence of Gaussian kernels, and the result follows from the corresponding statement for the complex transform. $\square$

### The Plancherel Theorem

**Theorem (Plancherel).** The transform extends uniquely to a unitary operator on the space $L^2(\mathbb{R}, \mathbb{B})$ of square-integrable biquaternion-valued functions, with

$$
\int_{-\infty}^{\infty} \|f(t)\|_E^2 \, dt = \int_{-\infty}^{\infty} \|F(\omega)\|_E^2 \, d\omega.
$$

**Proof.** The proof follows the standard proof of the Plancherel theorem, using the factorization into complex transforms established below. Since the factorization is an isometry on each complex component, the total norm is preserved. $\square$

**Corollary (Parseval).** For $f, g \in L^2(\mathbb{R}, \mathbb{B})$,

$$
\int_{-\infty}^{\infty} \overline{f(t)} g(t) \, dt = \int_{-\infty}^{\infty} \overline{F(\omega)} G(\omega) \, d\omega.
$$

## Factorization into Complex Fourier Transforms

### The Change of Basis

Let $\rho$ be the root of $-1$ used in the kernel. Choose two other unit pure biquaternions $\nu$ and $\xi$ such that

$$
\rho \perp \nu, \qquad \nu \perp \xi, \qquad \xi \perp \rho, \qquad \rho \nu = \xi.
$$

The four elements $\{e_0, \rho, \nu, \xi\}$ form a **complex orthonormal basis** of $\mathbb{B}$. Any biquaternion can be written in this basis as

$$
\tilde{Q} = Q_0 e_0 + Q_\rho \rho + Q_\nu \nu + Q_\xi \xi,
$$

with $Q_0, Q_\rho, Q_\nu, Q_\xi \in \mathbb{C}$.

### The Factorization

Writing the function $f$ in the new basis,

$$
f(t) = w(t) e_0 + x(t) \rho + y(t) \nu + z(t) \xi,
$$

and substituting into the transform with the closed form of the kernel, we obtain

$$
F(\omega) = \int_{-\infty}^{\infty} \left(\cos(2\pi \omega t) \, e_0 - \sin(2\pi \omega t) \, \rho\right) \left(w(t) e_0 + x(t) \rho + y(t) \nu + z(t) \xi\right) dt.
$$

Expanding the product and collecting terms by basis element gives four sums:

$$
F(\omega) = F_0(\omega) e_0 + F_\rho(\omega) \rho + F_\nu(\omega) \nu + F_\xi(\omega) \xi,
$$

where

$$
F_0(\omega) = \int_{-\infty}^{\infty} \left(\cos(2\pi \omega t) \, w(t) + \sin(2\pi \omega t) \, x(t)\right) dt,
$$

$$
F_\rho(\omega) = \int_{-\infty}^{\infty} \left(\cos(2\pi \omega t) \, x(t) - \sin(2\pi \omega t) \, w(t)\right) dt,
$$

$$
F_\nu(\omega) = \int_{-\infty}^{\infty} \left(\cos(2\pi \omega t) \, y(t) + \sin(2\pi \omega t) \, z(t)\right) dt,
$$

$$
F_\xi(\omega) = \int_{-\infty}^{\infty} \left(\cos(2\pi \omega t) \, z(t) - \sin(2\pi \omega t) \, y(t)\right) dt.
$$

### The Complex Fourier Transforms

Each of the four sums is a complex linear combination of the cosine and sine transforms of the real and imaginary parts of the complex coefficients. Using the complex exponential, we can write each sum as a combination of two ordinary complex Fourier transforms:

$$
F_\bullet(\omega) = \frac{1}{2}\left(\hat{G}_\bullet^{(+)}(\omega) + \hat{G}_\bullet^{(-)}(\omega)\right) + \frac{1}{2i}\left(\hat{G}_\bullet^{(+)}(\omega) - \hat{G}_\bullet^{(-)}(\omega)\right),
$$

where $\hat{G}_\bullet^{(\pm)}(\omega)$ are the ordinary complex Fourier transforms of the complex functions $G_\bullet^{(\pm)}(t)$ defined by

$$
G_\bullet^{(\pm)}(t) = G_\bullet(t) \exp(\pm 2\pi i t),
$$

and $G_\bullet(t)$ are the complex coefficients of $f(t)$ in the new basis.

Concretely, the factorization is the following procedure:

1. **Change of basis.** For each $t$, write the function value $f(t)$ in the basis $\{e_0, \rho, \nu, \xi\}$, obtaining four complex functions $w(t), x(t), y(t), z(t)$.
2. **Complex Fourier transforms.** Apply the ordinary complex Fourier transform to the four complex functions obtained by combining the coefficients as above. The result is four complex spectra.
3. **Reassemble.** Combine the four complex spectra into the biquaternion spectrum $F(\omega)$.

The factorization shows that the biquaternion Fourier transform is not a fundamentally new operation: it is the ordinary complex Fourier transform applied to the entries of the matrix representation, dressed in biquaternion language. The non-trivial content is the choice of root and the basis change that it induces.

### The Number of Complex Transforms

The number of complex Fourier transforms required depends on the choice of root and on the values of the function.

**Scalar imaginary, $\rho = i$.** The kernel reduces to the ordinary complex exponential, and the transform requires **four** complex Fourier transforms, one for each complex coefficient of $f$ in the standard basis.

**Unit pure real quaternion, $\rho = \mu_{\mathbb{R}}$.** The kernel is a real quaternion exponential. If $f$ takes values in $\mathbb{H}_{\mathbb{B}}$ or in $i \mathbb{H}_{\mathbb{B}}$, the transform requires **two** complex Fourier transforms. If $f$ takes values in the full algebra, the transform requires **four** complex Fourier transforms.

**Non-trivial root, signal in a subspace.** If $\rho$ is a non-trivial root and $f$ takes values in $\mathbb{H}_{\mathbb{B}}$ or in $i \mathbb{H}_{\mathbb{B}}$, the transform requires **two** complex Fourier transforms.

**Non-trivial root, fully biquaternion signal.** If $\rho$ is a non-trivial root and $f$ takes values in the full algebra, the transform requires **four** complex Fourier transforms.

So the generic case is four complex transforms, and the degenerate cases reduce to two or one.

## The Convolution Theorem

### Definition of Convolution

Let $f, g : \mathbb{R} \to \mathbb{B}$ be two biquaternion-valued functions. The **convolution** of $f$ and $g$ is

$$
(f * g)(t) = \int_{-\infty}^{\infty} f(\tau) g(t - \tau) \, d\tau,
$$

provided the integral converges. The convolution is **not commutative** in general, because the biquaternion product is not commutative.

### The Convolution Theorem

**Theorem (convolution theorem).** Let $f, g : \mathbb{R} \to \mathbb{B}$ be integrable, and let $\mathcal{F}$ denote the continuous biquaternion Fourier transform with the kernel on the left:

$$
\mathcal{F}[f](\omega) = \int_{-\infty}^{\infty} W(t, \omega) f(t) \, dt.
$$

Then

$$
\mathcal{F}[f * g](\omega) = \mathcal{F}[f](\omega) \cdot \mathcal{F}[g](\omega),
$$

where the product on the right is the biquaternion product.

**Proof.** Compute

$$
\mathcal{F}[f * g](\omega) = \int_{-\infty}^{\infty} W(t, \omega) \int_{-\infty}^{\infty} f(\tau) g(t - \tau) \, d\tau \, dt.
$$

Apply Fubini's theorem and change variables $t = \tau + s$:

$$
\mathcal{F}[f * g](\omega) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} W(\tau + s, \omega) f(\tau) g(s) \, ds \, d\tau.
$$

The kernel is multiplicative in the time argument: $W(\tau + s, \omega) = W(\tau, \omega) W(s, \omega)$. So

$$
\mathcal{F}[f * g](\omega) = \int_{-\infty}^{\infty} W(\tau, \omega) f(\tau) \, d\tau \cdot \int_{-\infty}^{\infty} W(s, \omega) g(s) \, ds = \mathcal{F}[f](\omega) \cdot \mathcal{F}[g](\omega).
$$

$\square$

**Corollary (right-kernel case).** For the transform with the kernel on the right,

$$
\mathcal{F}_{\text{right}}[f * g](\omega) = \mathcal{F}_{\text{right}}[g](\omega) \cdot \mathcal{F}_{\text{right}}[f](\omega).
$$

### Consequences

The convolution theorem implies that convolution in the time domain becomes **biquaternion multiplication** in the frequency domain. The convolution is associative, distributive over addition, and not commutative.

## The Relation to the Differential Operators

The continuous Fourier transform is the natural tool for analysing the differential operators of the analysis article. This is the main structural content of the continuous theory.

### The Gradient

Let $\tilde{\nabla}$ be the biquaternion gradient on a four-dimensional subspace $V \subset \mathbb{B}$, with coordinates $x_0, x_1, x_2, x_3$. For a function $\tilde{F} : V \to \mathbb{B}$, the Fourier transform in the variable $x_0$ (with the other coordinates treated as parameters, or with a full four-dimensional transform) diagonalizes the partial derivative $\partial_0$:

$$
\mathcal{F}[\partial_0 \tilde{F}](\omega) = 2\pi \rho \omega \, \mathcal{F}[\tilde{F}](\omega),
$$

where the sign depends on the convention for the kernel (the sign is positive for the kernel $\exp(+2\pi \rho \omega t)$ and negative for $\exp(-2\pi \rho \omega t)$).

If the transform is taken in all four variables, the gradient becomes multiplication by the biquaternion

$$
2\pi \rho (\omega_0 e_0 + \omega_1 e_1 + \omega_2 e_2 + \omega_3 e_3),
$$

where $\omega_0, \omega_1, \omega_2, \omega_3$ are the frequency variables conjugate to $x_0, x_1, x_2, x_3$. The precise form depends on the placement of the root $\rho$ and on the choice of basis, but the structural fact is that the gradient becomes a biquaternion-valued multiplier.

### The d'Alembertian

The d'Alembertian $\Box = \partial_0^2 + \Delta$ is a scalar operator, and it commutes with the Fourier transform. Under the transform,

$$
\mathcal{F}[\Box \tilde{F}](\omega) = \left((2\pi \omega_0)^2 - (2\pi)^2 (\omega_1^2 + \omega_2^2 + \omega_3^2)\right) \mathcal{F}[\tilde{F}](\omega) = -4\pi^2 (\omega_0^2 - \omega_1^2 - \omega_2^2 - \omega_3^2) \mathcal{F}[\tilde{F}](\omega).
$$

The multiplier is a scalar (times $e_0$), and it vanishes on the **light cone**

$$
\omega_0^2 = \omega_1^2 + \omega_2^2 + \omega_3^2.
$$

So the Fourier transform of a solution of $\Box \tilde{F} = 0$ is supported on the light cone. This is the biquaternion analogue of the statement that the Fourier transform of a harmonic function is supported on the zero set of the symbol.

### The Square of the Gradient

The square of the gradient $\tilde{\nabla}^2 = (\partial_0^2 - \Delta) + 2\sum_k e_k \partial_0 \partial_k$ is a biquaternion-valued operator. Under the transform, it becomes multiplication by

$$
\left((2\pi \omega_0)^2 + (2\pi)^2 (\omega_1^2 + \omega_2^2 + \omega_3^2)\right) e_0 + 2 \sum_k e_k (2\pi \omega_0)(2\pi \omega_k),
$$

which is a biquaternion-valued multiplier. The precise form depends on the sign convention and on the placement of the root.

### The Convective Derivative

The convective derivative $\tilde{D} = \bar{\tilde{U}} \tilde{\nabla}$ becomes multiplication by the biquaternion

$$
\bar{\tilde{U}} \cdot 2\pi \rho (\omega_0 e_0 + \omega_1 e_1 + \omega_2 e_2 + \omega_3 e_3),
$$

which depends on the velocity biquaternion $\tilde{U}$ and on the frequency variables. The multiplier is a biquaternion, and its vanishing determines the dispersion relation of the operator.

### The General Principle

The general principle is that the continuous Fourier transform **diagonalizes the constant-coefficient differential operators** on the four-dimensional subspaces. The symbol of the operator is a biquaternion-valued function of the frequency variables, and the solutions of the operator equation are determined by the support of the transform on the zero set of the symbol.

This is the same principle as in the complex and quaternion cases, and it is the reason the continuous Fourier transform is the natural tool for the analysis of the biquaternion differential operators.

## The Vanishing-Norm Issue

### Functions of Vanishing Norm

A function $f : \mathbb{R} \to \mathbb{B}$ may take values of vanishing norm form on a set of positive measure. On such a set, the values are zero divisors, and the transform may not be invertible.

More precisely, if $f(t)$ is a zero divisor for some $t$, then there exists a nonzero biquaternion $\tilde{Z}(t)$ with $f(t) \circ \tilde{Z}(t) = 0$ or $\tilde{Z}(t) \circ f(t) = 0$. The kernel is invertible, so the product $W(t, \omega) f(t)$ is also a zero divisor, and the integral over $t$ may or may not preserve the information of $f(t)$.

### Consequences for the Transform

- **The transform is not necessarily invertible on functions that take zero-divisor values on a set of positive measure.**
- **The transform is invertible on functions of non-vanishing norm**, i.e., on functions whose values lie in the complement of the zero divisor set.

### Structural Interpretation

The vanishing-norm issue is a genuinely biquaternionic feature. It does not arise in the complex or quaternion Fourier transforms, because the complex and quaternion algebras are division algebras. The biquaternion algebra is not a division algebra, and this is reflected in the harmonic analysis.

The issue can be avoided by restricting to functions whose values lie in a subspace where the norm form is nonzero, such as the quaternion subspace $\mathbb{H}_{\mathbb{B}}$. On $\mathbb{H}_{\mathbb{B}}$, every nonzero value is invertible, and the transform is invertible on all functions. On the anti-Hermitian subspace $\mathbb{M}_-$, the functions with vanishing norm lie on a cone, and the transform is invertible only for functions whose values lie off the cone.

### The Open Question

The precise condition under which the transform is invertible on a function that takes zero-divisor values on a set of positive measure is not known. It depends on the cancellations in the integral $\int W(t, \omega) f(t) \, dt$, and it is not determined by the norms of the values alone. This is one of the open questions listed below.

## The Relation to the Discrete Transform

### Sampling

The continuous transform is the limit of the discrete transform as the number of samples $N$ tends to infinity and the sampling interval tends to zero. The precise relation is the standard one: if $f$ is a function of bounded variation and $F$ is its continuous transform, then the discrete transform of the samples $f(nT)$ for $n \in \mathbb{Z}$ approximates $F$ as the sampling interval $T$ tends to zero.

### Periodization

Conversely, the discrete transform is the periodization of the continuous transform. If $f$ is a function with continuous transform $F$, then the discrete transform of the samples $f(nT)$ is the periodization of $F$:

$$
F_{\text{disc}}[u] = \frac{1}{T} \sum_{k \in \mathbb{Z}} F\left(\frac{u}{NT} + \frac{k}{T}\right).
$$

This is the standard Poisson summation formula, and it holds in the biquaternion case with the same proof, because the kernel is the ordinary complex kernel in the direction $\rho$.

### The Sampling Theorem

The **sampling theorem** (or Shannon–Nyquist theorem) states that a function whose continuous transform is supported in a bounded interval $[-W, W]$ can be reconstructed from its samples at the rate $1/(2W)$. The biquaternion version of the sampling theorem holds under the same conditions, with the reconstruction formula

$$
f(t) = \sum_{n \in \mathbb{Z}} f(nT) \operatorname{sinc}\left(\frac{t - nT}{T}\right),
$$

where the sinc function is the ordinary real sinc, and the convergence is in the appropriate sense. The proof is the same as in the complex case, because the reconstruction is component-wise.

## Open Questions

1. **The precise invertibility condition.** Under what conditions on the zero-divisor values is the continuous transform invertible? The answer is not known.

2. **The support of the transform of solutions of $\tilde{\nabla}\tilde{F} = 0$.** The Fourier transform of a solution of the gradient equation $\tilde{\nabla}\tilde{F} = 0$ is supported on a set determined by the symbol of the gradient. What is the structure of this set?

3. **The Plancherel theorem for general functions.** Under what conditions does the Plancherel theorem hold for functions that take zero-divisor values? The current statement requires square-integrability, which is a norm condition and does not detect the zero divisors.

4. **Wavelets and time-frequency analysis.** Can a biquaternion wavelet transform be defined, and what are its properties? Can a biquaternion time-frequency distribution be defined?

5. **The relation to the analysis article.** The connection between the continuous Fourier transform and the differential operators is established at the level of symbols. What are the deeper consequences for the structure of the solutions of the operator equations?

6. **The Clifford algebra framework.** How does the biquaternion continuous Fourier transform fit into the general theory of Clifford algebra Fourier transforms?

7. **Applications to physics.** The biquaternion Fourier transform may be relevant to the analysis of biquaternion-valued fields in the complexified-spacetime program. This is a forward reference to physics and is not developed in this article.

## Summary

The continuous biquaternion Fourier transform is defined by the kernel $W(t, \omega) = \exp(-2\pi \rho \omega t)$, where $\rho$ is a root of $-1$ in $\mathbb{B}$. The choice of root determines the nature of the transform: the scalar imaginary gives the ordinary complex transform, the unit pure real quaternions give the quaternion transform, and the non-trivial roots give genuinely biquaternionic transforms.

The transform is invertible on functions of non-vanishing norm, and it satisfies the Riemann–Lebesgue lemma, the inversion theorem, and the Plancherel theorem. It factorizes into four complex Fourier transforms, which is the computational and structural content of the theory.

The convolution theorem holds, with the non-commutativity requiring careful placement of the kernel. The transform diagonalizes the constant-coefficient differential operators of the analysis article: the gradient becomes a biquaternion-valued multiplier, the d'Alembertian becomes a scalar multiplier vanishing on the light cone, and the convective derivative becomes a biquaternion-valued multiplier depending on the velocity.

The vanishing-norm issue is a genuinely biquaternionic feature: functions that take zero-divisor values on a set of positive measure are not necessarily recoverable from their transform, and the precise invertibility condition is not known.

The continuous transform is the limit of the discrete transform as the sampling interval tends to zero, and it is related to the discrete transform by the Poisson summation formula and the sampling theorem.

## Further Reading

- S. Said, N. Le Bihan, S. J. Sangwine, "Fast complexified quaternion Fourier transform", *IEEE Transactions on Signal Processing* **56** (2008) 1522–1531, for the discrete biquaternion Fourier transform.
- S. J. Sangwine and T. A. Ell, "Complexification of the quaternion roots of $-1$", arXiv:math.RA/0506190 (2005), for the classification of the biquaternion roots of $-1$.
- S. J. Sangwine and D. Alfsmann, "Determination of the biquaternion divisors of zero, including the idempotents and nilpotents", arXiv:0812.1102 (2008), for the classification of the zero divisors.
- N. Le Bihan and J. Mars, "Singular value decomposition of quaternion matrices: a new tool for vector-sensor signal processing", *Signal Processing* **84** (2004) 1177–1199, for the quaternion signal processing background.
- T. A. Ell and S. J. Sangwine, "Hypercomplex Fourier transforms of color images", *IEEE Transactions on Image Processing* **16** (2007) 22–35, for the quaternion Fourier transform and its applications.
- R. Fueter, "Die Funktionentheorie der Differentialgleichungen $\Delta u = 0$ und $\Delta\Delta u = 0$ mit vier reellen Variablen", *Commentarii Mathematici Helvetici* **7** (1934–35) 307–330, for the analysis of quaternion-valued functions of four real variables.
- F. Brackx, R. Delanghe, and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the general Clifford analysis.
- W. R. Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original formulation of quaternions and biquaternions.

