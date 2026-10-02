# __Biquaternion Continuous Harmonic Analysis__

## Introduction

This article introduces harmonic analysis for biquaternion-valued functions of a real variable. It follows the article on biquaternion discrete harmonic analysis, which defined the discrete biquaternion Fourier transform, and it uses the analysis article, which defined the biquaternion gradient, the d'Alembertian, and the convective derivative on the four-dimensional subspaces of $\mathbb{B}$.

The treatment is purely mathematical. The goal is to define the continuous biquaternion Fourier transform, establish its basic properties, show how it decomposes into ordinary complex Fourier transforms, and identify the points where the biquaternion structure creates genuinely new phenomena. The relation to the differential operators of the analysis article is the main structural content of this article. Two kernels are treated: the one-unit kernel, and the two-unit kernel that assigns one unit to each of two variables. The transform of a finite measure is examined beside them, and the positivity it lacks is the same indefiniteness that governs the vanishing-norm issue.

The key structural fact is the same as in the discrete case: the Fourier kernel is a biquaternion exponential, and the exponential is defined by a **root of $-1$**. The choice of root determines the nature of the transform, and the transform decomposes into a finite number of ordinary complex Fourier transforms. The genuinely biquaternionic content is the choice of root, the decomposition, and the vanishing-norm issue.

Throughout, a biquaternion is written

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3, \qquad Q_\mu \in \mathbb{C},
$$

or, more compactly, as

$$
\tilde{Q} = Q_0 e_0 + \mathbf{Q}, \qquad \mathbf{Q} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3.
$$

The scalar imaginary is $i$, which commutes with the quaternion units. The quaternion conjugate is $\tilde{Q}^{\natural} = Q_0 e_0 - \mathbf{Q}$, and the biquaternion norm is $N(\tilde{Q}) = \tilde{Q} \tilde{Q}^{\natural}$.

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

where the cosine and sine are the ordinary real trigonometric functions applied to the real argument $2\pi \omega t$.

**The inverse.** The kernel is invertible at every point, with

$$
W(t, \omega)^{-1} = \cos(2\pi \omega t) \, e_0 + \sin(2\pi \omega t) \, \rho ,
$$

which follows from $\rho^2 = -e_0$ alone: the two factors multiply to $\cos^2 + \sin^2 = e_0$. This is a closed form that holds for **every** root, and it is the form the inverse transform uses.

**The conjugate and the norm, for a pure root.** When the root is pure, that is, when its scalar part vanishes, the quaternion conjugate of the kernel is this inverse and the norm is the identity:

$$
\overline{W(t, \omega)} = W(t, \omega)^{-1}, \qquad N(W(t, \omega)) = \cos^2(2\pi \omega t) + \sin^2(2\pi \omega t) = e_0 ,
$$

because $\bar\rho = -\rho$ for a pure element. The first family $\rho = \pm i$ is the exception: it is not pure, the quaternion conjugate leaves the kernel unchanged, and the inverse is the complex conjugate $\exp(2\pi\omega t\, i)$. In that family the kernel is a complex scalar and the transform is the ordinary complex Fourier transform of each component simultaneously. The distinction affects only that family, and the statements below that use the conjugate of the kernel are stated for a pure root.

### The Condition on the Root

A biquaternion $\rho$ satisfies $\rho^2 = -e_0$ if and only if either $\rho = \pm i$, or $\rho$ is a pure biquaternion (i.e., its scalar part $\rho_0$ vanishes) and

$$
\Re(\rho) \perp \Im(\rho), \qquad \|\Re(\rho)\|^2 - \|\Im(\rho)\|^2 = 1,
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

The two transforms are related as in the discrete case: the conjugate of the left-kernel transform of $f$ equals the right-kernel transform of the conjugate of $f$, with a sign change in the kernel. (The outer conjugation is needed: $\overline{K(t,\omega) f(t)} = \overline{f(t)}\,\overline{K(t,\omega)}$.)

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

**Proof.** The kernel is bounded and the integrand is integrable. The standard proof for the complex Fourier transform applies component-wise, and the result follows from the component-wise statement.

### The Inversion Theorem

**Theorem (inversion).** Let $f : \mathbb{R} \to \mathbb{B}$ be integrable and continuous at a point $t \in \mathbb{R}$, and let $F$ be integrable. Then

$$
f(t) = \int_{-\infty}^{\infty} \overline{W(t, \omega)} F(\omega) \, d\omega.
$$

**Proof.** The proof follows the standard proof of the inversion theorem for the complex Fourier transform, applied component-wise in the basis $\{e_0, \rho, \nu, \xi\}$ introduced below. The key step is the approximation of the identity by a sequence of Gaussian kernels, and the result follows from the corresponding statement for the complex transform.

### The Plancherel Theorem

**Theorem (Plancherel).** The transform extends uniquely to a unitary operator on the space $L^2(\mathbb{R}, \mathbb{B})$ of square-integrable biquaternion-valued functions, with

$$
\int_{-\infty}^{\infty} \|f(t)\|_E^2 \, dt = \int_{-\infty}^{\infty} \|F(\omega)\|_E^2 \, d\omega.
$$

**Proof.** The proof follows the standard proof of the Plancherel theorem, using the factorization into complex transforms established below. Since the factorization is an isometry on each complex component, the total norm is preserved.

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

The factorization shows that the biquaternion Fourier transform is not a fundamentally new operation: it is the ordinary complex Fourier transform applied entrywise to the coefficients, dressed in biquaternion language. The non-trivial content is the choice of root and the basis change that it induces.

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

The convective derivative $\tilde{D} = \tilde{U}^{\natural} \tilde{\nabla}$ becomes multiplication by the biquaternion

$$
\tilde{U}^{\natural} \cdot 2\pi \rho (\omega_0 e_0 + \omega_1 e_1 + \omega_2 e_2 + \omega_3 e_3),
$$

which depends on the velocity biquaternion $\tilde{U}$ and on the frequency variables. The multiplier is a biquaternion, and its vanishing determines the dispersion relation of the operator.

### The General Principle

The general principle is that the continuous Fourier transform **diagonalizes the constant-coefficient differential operators** on the four-dimensional subspaces. The symbol of the operator is a biquaternion-valued function of the frequency variables, and the solutions of the operator equation are determined by the support of the transform on the zero set of the symbol.

This is the same principle as in the complex and quaternion cases, and it is the reason the continuous Fourier transform is the natural tool for the analysis of the biquaternion differential operators.

## The Vanishing-Norm Issue

### Functions of Vanishing Norm

A function $f : \mathbb{R} \to \mathbb{B}$ may take values of vanishing norm on a set of positive measure. On such a set, the values are zero divisors, and the transform may not be invertible.

More precisely, if $f(t)$ is a zero divisor for some $t$, then there exists a nonzero biquaternion $\tilde{Z}(t)$ with $f(t) \circ \tilde{Z}(t) = 0$ or $\tilde{Z}(t) \circ f(t) = 0$. The kernel is invertible, so the product $W(t, \omega) f(t)$ is also a zero divisor, and the integral over $t$ may or may not preserve the information of $f(t)$.

### Consequences for the Transform

- **The transform is not necessarily invertible on functions that take zero-divisor values on a set of positive measure.**
- **The transform is invertible on functions of non-vanishing norm**, i.e., on functions whose values lie in the complement of the zero divisor set.

### Structural Interpretation

The vanishing-norm issue is a genuinely biquaternionic feature. It does not arise in the complex or quaternion Fourier transforms, because the complex and quaternion algebras are division algebras. The biquaternion algebra is not a division algebra, and this is reflected in the harmonic analysis.

The issue can be avoided by restricting to functions whose values lie in a subspace where the biquaternion norm is nonzero, such as the quaternion subspace $\mathbb{H}_{\mathbb{B}}$. On $\mathbb{H}_{\mathbb{B}}$, every nonzero value is invertible, and the transform is invertible on all functions. On the anti-Hermitian subspace $\mathbb{M}_-$, the functions with vanishing norm lie on a cone, and the transform is invertible only for functions whose values lie off the cone.

### The Open Question

The precise condition under which the transform is invertible on a function that takes zero-divisor values on a set of positive measure is not known. It depends on the cancellations in the integral $\int W(t, \omega) f(t) \, dt$, and it is not determined by the biquaternion norms of the values alone. This is one of the open questions listed below.

## The Two-Dimensional Kernel with One Unit per Variable

The transform above carries one real variable and one root. The transform of the signal-processing literature carries two variables and assigns one unit to each, and in the biquaternion algebra that assignment is a genuine choice, because the roots of $-1$ fall into the three families classified above.

**Definition.** Let $\rho_1$ and $\rho_2$ be roots of $-1$ in $\mathbb{B}$, not necessarily distinct and not necessarily commuting. For a function $f : \mathbb{R}^2 \to \mathbb{B}$, the **two-unit transform** is

$$
F(\omega_1, \omega_2) = \int_{\mathbb{R}^2} W_1(x_1, \omega_1) \, W_2(x_2, \omega_2) \, f(x_1, x_2) \, dx_1 dx_2,
\qquad
W_k(x_k, \omega_k) = \exp(-2\pi \rho_k \omega_k x_k),
$$

the order of the two kernel factors being part of the definition, because they need not commute. The discrete case places one kernel on each side of $f$; the placement is a convention here as it is for the one-unit transform, and the left-left placement is the one used below. The **two-unit kernel** is their product $K = W_1 W_2$.

**Closed form.** With $\theta_k = 2\pi \omega_k x_k$,

$$
K = \cos\theta_1 \cos\theta_2 \, e_0 - \cos\theta_1 \sin\theta_2 \, \rho_2 - \sin\theta_1 \cos\theta_2 \, \rho_1 + \sin\theta_1 \sin\theta_2 \, \rho_1 \rho_2 .
$$

The four coefficients are real. The first three terms are the one-unit kernel read on the two variables, and the fourth carries the product $\rho_1 \rho_2$, which is $\pm e_3$ when the two units are two of $e_1, e_2, e_3$ and is a general biquaternion for other pairs.

**Reduction to the one-unit kernel.** If the two units coincide, $\rho_1 = \rho_2 = \rho$, the exponents add and

$$
K = \cos(\theta_1 + \theta_2) \, e_0 - \sin(\theta_1 + \theta_2) \, \rho ,
$$

which is the kernel $W$ of this article read on the linear form $\omega_1 x_1 + \omega_2 x_2$, and it is the kernel of the two-dimensional transform of the discrete case. The one-unit theory is therefore the case in which the two units are equal, and the two-unit transform is its refinement.

**The kernel is invertible for every pair of roots.** The norm is multiplicative, $N(K) = N(W_1) N(W_2)$, and the inverse is the kernel with both frequencies negated and the two factors exchanged:

$$
K(x, \omega)^{-1} = W_2(x_2, -\omega_2) \, W_1(x_1, -\omega_1).
$$

For two pure roots the kernel is unitary in the sense of the previous section,

$$
N(K) = e_0, \qquad \overline{K(x, \omega)} = K(x, \omega)^{-1},
$$

and this holds for every pair of pure roots, commuting or not. The unit-norm property is thus a property of each factor and is inherited by the product.

**Frequency reversal.** Reversing the sign of the frequencies conjugates the kernel **and exchanges the two factors**:

$$
\overline{K(x, \omega)} = K^{\mathrm{ex}}(x, -\omega),
$$

where $K^{\mathrm{ex}}$ is the kernel with the two units interchanged. For two pure roots the identity is exact, and it reduces to the one-unit statement $\overline{W(t,\omega)} = W(t,-\omega)$ when there is only one unit to exchange. The form without the exchange, $\overline{K(x,\omega)} = K(x,-\omega)$, needs in addition that the two factors commute: it holds for two pure roots that are equal or opposite, and it fails for two pure roots that are neither, because those do not commute. Both identities are stated for pure roots; the first family $\rho = \pm i$ is excluded from them, as it is in the one-unit case.

**On the factorisation into complex transforms.** The factorisation of the next section diagonalises one root. Two elements that are simultaneously diagonalisable commute, so two roots that do not commute admit no common eigenbasis, and there is no basis in which both units of the two-unit kernel act diagonally at once. The pairs that do commute — equal roots, opposite roots, and any pair containing the central imaginary $i$ — keep a common eigenbasis, and there the one-unit factorisation applies to both variables. Whether the two-unit transform with a non-commuting pair still reduces to a fixed finite family of complex transforms is not settled here, and it is listed among the open questions.

## The Transform of a Measure, and the Failure of Positivity

**Definition.** Let $\mu$ be a finite positive measure on $\mathbb{R}^n$ and let $\rho$ be a pure root of $-1$. The **transform of the measure** is

$$
G(\omega) = \int_{\mathbb{R}^n} \chi_\omega(x) \, d\mu(x), \qquad \chi_\omega(x) = \exp\big(-2\pi \rho \langle \omega, x \rangle\big).
$$

Because $\chi_0 = e_0$ at every point, $G(0) = \mu(\mathbb{R}^n) \, e_0$: the value at zero frequency is the total mass, a positive real multiple of the identity.

**The quadratic form.** For coefficients $z_1, \dots, z_N$ in the centre $\mathbb{C}_{\mathbb{B}}$ (the complex scalars $z_k = \zeta_k e_0$, $\zeta_k \in \mathbb{C}$) and frequencies $\omega_1, \dots, \omega_N$,

$$
\sum_{k,l=1}^{N} \bar z_k z_l \, G(\omega_k - \omega_l) \;=\; \int_{\mathbb{R}^n} N\big(Z(x)\big) \, d\mu(x),
\qquad
Z(x) = \sum_{k=1}^{N} z_k \chi_{\omega_k}(x) ,
$$

the right-hand side being the integral of the **biquaternion norm** of the trigonometric sum. The identity is one line, because $\bar\chi_\omega \chi_\eta = \chi_{\eta - \omega}$ for a pure root, so each term of the sum reassembles a product inside the modulus. It is the exact content of the classical statement that the Fourier transform of a measure is a positive-definite function.

**The real-quaternion case.** If the root is a real quaternion and the coefficients are real, then $Z = A - B\rho$ with $A$ and $B$ real and the integrand is $A^2 + B^2 \ge 0$. The form is non-negative and the transform of the measure is positive definite, which is the hypothesis the classical theorem of Bochner runs on; the quaternion form of that statement, in one and in two variables, is the subject of *Quaternion Harmonic Analysis*.

**The biquaternion case: the form is the norm, and the norm is indefinite.** For $\mathbb{B}$ the integrand is the norm itself, and the norm is complex-valued:

$$
N(Q) = Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2, \qquad \Re N(Q) = \sum_{\mu=0}^{3} (\Re Q_\mu)^2 - \sum_{\mu=0}^{3} (\Im Q_\mu)^2
$$

in the eight real components of $Q$. The failure needs no zero divisor and no exceptional value. At $N = 1$, with the central imaginary unit for coefficient,

$$
z_1 = i: \qquad \bar z_1 z_1 \, G(0) = i^2 \, \mu(\mathbb{R}^n) = -\mu(\mathbb{R}^n) \, e_0 ,
$$

which is negative for every non-zero measure, because $N(i) = -1$. The scalar imaginary is a unit of the algebra — the element whose presence makes the algebra biquaternionic — and the norm is negative on it. Hence **the transform of a measure is not a positive-definite function for $\mathbb{B}$**, and the positivity a Bochner-type hypothesis would need is not available. The absence is the same indefiniteness the vanishing-norm section records, read at a different value: the norm vanishes on the null cone and it is negative on the centre.

**The repair, and what it costs.** Positivity returns when the norm is replaced by a definite pairing. The integrand of the Euclidean form is a sum of squares of moduli,

$$
\|Z(x)\|_E^2 = \sum_{\mu=0}^{3} \lvert Z_\mu(x) \rvert^2 \ge 0 ,
$$

so the Euclidean quadratic form is non-negative, and $\|\cdot\|_E$ is the pairing this article already uses for convergence. What the exchange costs is the algebra: the Euclidean form is not the norm of the transform, and it does not factor through the product of $\mathbb{B}$.

**Two hypotheses, and the same obstruction as before.** The identity requires central coefficients. For quaternion-valued coefficients the products $z_k \chi_{\omega_k}$ do not reassemble, and the two sides differ by terms of order one on random data: the coefficient has to commute with the kernel, which is a genuine restriction and not a technicality of the proof. It also requires a single root for the transform: with two units, one per variable, the collapse $\bar\chi_\omega \chi_\eta = \chi_{\eta - \omega}$ fails as soon as the two units differ, and the identity is false there. The Bochner-type positivity is therefore a one-root, central-coefficient statement even for $\mathbb{H}$, and for $\mathbb{B}$ it fails under those hypotheses as well.

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

7. **The factorisation of the two-unit transform.** The factorisation of the one-unit transform diagonalises one root. Two roots that do not commute admit no common eigenbasis, so a two-unit kernel with such a pair has no basis in which both units act diagonally, and it is not known whether its transform still reduces to a fixed finite family of complex transforms.

8. **Positivity for the transform of a measure.** The quadratic form of the transform of a measure is the integral of the norm, and the norm is indefinite, so the biquaternionic form of the Bochner-type hypothesis has no apparent source. Whether some pairing internal to the algebra supplies one is not known.

## Summary

The continuous biquaternion Fourier transform is defined by the kernel $W(t, \omega) = \exp(-2\pi \rho \omega t)$, where $\rho$ is a root of $-1$ in $\mathbb{B}$. The choice of root determines the nature of the transform: the scalar imaginary gives the ordinary complex transform, the unit pure real quaternions give the quaternion transform, and the non-trivial roots give genuinely biquaternionic transforms.

The transform is invertible on functions of non-vanishing norm, and it satisfies the Riemann–Lebesgue lemma, the inversion theorem, and the Plancherel theorem. It factorizes into four complex Fourier transforms, which is the computational and structural content of the theory.

The convolution theorem holds, with the non-commutativity requiring careful placement of the kernel. The transform diagonalizes the constant-coefficient differential operators of the analysis article: the gradient becomes a biquaternion-valued multiplier, the d'Alembertian becomes a scalar multiplier vanishing on the light cone, and the convective derivative becomes a biquaternion-valued multiplier depending on the velocity.

The vanishing-norm issue is a genuinely biquaternionic feature: functions that take zero-divisor values on a set of positive measure are not necessarily recoverable from their transform, and the precise invertibility condition is not known.

A two-unit kernel is recorded beside the one-unit kernel, one unit per variable. Its closed form carries the product of the two roots in its fourth term, it reduces to the one-unit kernel when the two roots coincide, it is invertible for every pair of roots, and its conjugate is the kernel with the two units exchanged. The transform of a finite positive measure has a quadratic form which is the integral of the biquaternion norm of a trigonometric sum: non-negative for real coefficients and a real root, which is the classical positive definiteness of a measure transform, and false for $\mathbb{B}$ at a single term with $z = i$, because $N(i) = -1$. The Euclidean pairing restores positivity and is not the norm of the algebra.

The continuous transform is the limit of the discrete transform as the sampling interval tends to zero, and it is related to the discrete transform by the Poisson summation formula and the sampling theorem.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra, $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ |
| $f : \mathbb{R} \to \mathbb{B}$ | Biquaternion-valued function of one real variable |
| $F = \mathcal{F}[f]$ | Continuous biquaternion Fourier transform of $f$ |
| $W(t,\omega) = \exp(-2\pi\rho\omega t)$ | Fourier kernel, placed on the left of $f$; the conjugate kernel $\overline{W}$ gives the inverse transform |
| $\rho$ | Root of $-1$ in $\mathbb{B}$ fixing the transform; a local notation, not the scalar imaginary $i$ |
| $\omega$ | Frequency variable, $\omega \in \mathbb{R}$ |
| $\rho_1, \rho_2$ | Roots of $-1$ attached to the two variables of the two-unit kernel; they need not be equal, and need not commute |
| $K = W_1W_2$ | Two-unit kernel, one unit per variable; the order of the factors is part of the definition, and $K(x,\omega)^{-1} = W_2(x_2,-\omega_2)W_1(x_1,-\omega_1)$ |
| $\mu$, $G(\omega) = \int \chi_\omega \, d\mu$ | Finite positive measure and its transform; $G(0) = \mu(\mathbb{R}^n)e_0$, and $\sum_{k,l}\bar z_kz_l G(\omega_k-\omega_l) = \int N(Z) \, d\mu$ for central coefficients |
| $\mathbf{Q} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3$ | Vector part of a biquaternion |
| $N(\tilde{Q}) = \tilde{Q}\tilde{Q}^{\natural}$ | Biquaternion norm; it vanishes on the zero divisors |
| $\tilde{\nabla}$ | Biquaternionic gradient on a four-dimensional subspace |
| $\Box = \partial_0^2 + \Delta$ | d'Alembertian, the scalar part of $\tilde{\nabla}\tilde{\nabla}^{\natural}$ |
| $\tilde{D} = \tilde{U}^{\natural}\tilde{\nabla}$ | Convective derivative with velocity $\tilde{U}$ |

## Further Reading

- S. Said, N. Le Bihan, S. J. Sangwine, "Fast complexified quaternion Fourier transform", *IEEE Transactions on Signal Processing* **56** (2008) 1522–1531, for the discrete biquaternion Fourier transform.
- S. J. Sangwine and T. A. Ell, "Complexification of the quaternion roots of $-1$", arXiv:math.RA/0506190 (2005), for the classification of the biquaternion roots of $-1$.
- S. J. Sangwine and D. Alfsmann, "Determination of the biquaternion divisors of zero, including the idempotents and nilpotents", arXiv:0812.1102 (2008), for the classification of the zero divisors.
- N. Le Bihan and J. Mars, "Singular value decomposition of quaternion matrices: a new tool for vector-sensor signal processing", *Signal Processing* **84** (2004) 1177–1199, for the quaternion signal processing background.
- T. A. Ell and S. J. Sangwine, "Hypercomplex Fourier transforms of color images", *IEEE Transactions on Image Processing* **16** (2007) 22–35, for the quaternion Fourier transform and its applications.
- S. Georgiev, J. Morais, K. I. Kou, and W. Sprößig, "Bochner–Minlos theorem and quaternion Fourier transform", in *Quaternion and Clifford–Fourier Transforms and Wavelets*, Trends in Mathematics (Springer, 2013), 105–120, for the quaternion theorem whose biquaternionic counterpart is examined in the section on the transform of a measure above: the two-dimensional transform with one unit per variable, the difference between its two orderings, and the positive definiteness of the transform of a measure, which holds there and fails here.
- S. Bochner, "Monotone Funktionen, Stieltjessche Integrale und harmonische Analyse", *Mathematische Annalen* **108** (1933) 378–410, for the classical theorem that a normalised positive-definite function is the Fourier transform of a measure, which is the statement the biquaternion algebra does not reproduce.
- R. Fueter, "Die Funktionentheorie der Differentialgleichungen $\Delta u = 0$ und $\Delta\Delta u = 0$ mit vier reellen Variablen", *Commentarii Mathematici Helvetici* **7** (1934–35) 307–330, for the analysis of quaternion-valued functions of four real variables.
- F. Brackx, R. Delanghe, and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the general Clifford analysis.
- W. R. Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original formulation of quaternions and biquaternions.

