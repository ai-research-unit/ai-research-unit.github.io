# __Split-Biquaternion Continuous Harmonic Analysis__

## Introduction

This article introduces harmonic analysis for split-biquaternion-valued functions of a real variable. It follows the article on split biquaternion discrete harmonic analysis, which defined the discrete split-biquaternion Fourier transform, and it uses the analysis article, which defined the split-biquaternion gradient, the d'Alembertian, and the convective derivative on the four-dimensional subspaces of $\mathbb{H}_{\mathbb{D}}$.

The treatment is purely mathematical. The goal is to define the continuous split-biquaternion Fourier transform, establish its basic properties, show how it decomposes into ordinary complex Fourier transforms via the idempotent decomposition, and identify the points where the split biquaternion structure creates genuinely new phenomena. The relation to the differential operators of the analysis article is the main structural content of this article.

The key structural fact is the same as in the discrete case: the **idempotent decomposition** of the split biquaternion algebra reduces the transform to two independent quaternion Fourier transforms, one for each idempotent component. The split complex unit $j$ does not appear in the kernel; it only appears in the idempotent decomposition that separates the two components. This is the fundamental simplification relative to the biquaternion case.

Throughout, a split biquaternion is written

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3, \qquad Q_\mu = q_\mu + j q'_\mu, \quad q_\mu, q'_\mu \in \mathbb{R}.
$$

The split complex unit is $j$, with $j^2 = +1$, and it commutes with the quaternion units. The quaternion conjugate is $\bar{\tilde{Q}} = Q_0 e_0 - \mathbf{Q}$. The norm form is $N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}}$.

The **idempotent components** of $\tilde{Q}$ are the real quaternions

$$
\tilde{Q}_+ = \sum_{\mu=0}^{3} (q_\mu + q'_\mu) e_\mu, \qquad \tilde{Q}_- = \sum_{\mu=0}^{3} (q_\mu - q'_\mu) e_\mu.
$$

The idempotent decomposition is $\tilde{Q} = \tilde{Q}_+ e_+ + \tilde{Q}_- e_-$, with $e_\pm = \tfrac{1}{2}(1 \pm j)$.

**Notation.** To avoid collision with the standard basis $\{e_0, e_1, e_2, e_3\}$ and with the split complex unit $j$, the root of $-1$ used in the Fourier kernel is denoted $\rho$ throughout. This is a local convention; the roots themselves are the objects classified in the article on split biquaternion roots of minus one.

## The Fourier Kernel

### Definition

Fix a root $\rho$ of $-1$ in the quaternion algebra $\mathbb{H}$, i.e., an element $\rho \in \mathbb{H}$ with

$$
\rho^2 = -1.
$$

The roots of $-1$ in $\mathbb{H}$ are exactly the unit pure real quaternions, i.e., the elements of the form $\rho = \mu$ with $\mu \in \mathbb{R}^3_{\mathbb{H}}$ and $|\mu| = 1$.

The **split biquaternion Fourier kernel** is the function

$$
W(t, \omega) = \exp(-2\pi \rho \omega t), \qquad t, \omega \in \mathbb{R},
$$

where the exponential is the split biquaternion exponential and $\rho$ is viewed as an element of $\mathbb{H}_{\mathbb{D}}$ via the embedding $\mathbb{H} \hookrightarrow \mathbb{H}_{\mathbb{D}}$.

Because $\rho^2 = -1$, the kernel takes the closed form

$$
W(t, \omega) = \cos(2\pi \omega t) \, e_0 - \sin(2\pi \omega t) \, \rho,
$$

where the cosine and sine are the ordinary real trigonometric functions applied to the real argument $2\pi \omega t$. The kernel is therefore a unit quaternion:

$$
N(W(t, \omega)) = \cos^2(2\pi \omega t) + \sin^2(2\pi \omega t) = 1.
$$

In particular, the kernel is always invertible, and its inverse is its quaternion conjugate:

$$
W(t, \omega)^{-1} = \overline{W(t, \omega)} = \cos(2\pi \omega t) \, e_0 + \sin(2\pi \omega t) \, \rho.
$$

The kernel is the same in both idempotent components, so the split biquaternion kernel is the diagonal embedding of the quaternion kernel. This is the same as in the discrete case.

### The Condition on the Root

A quaternion $\rho$ satisfies $\rho^2 = -1$ if and only if it is a pure real quaternion of unit norm:

$$
\rho \in \mathbb{R}^3_{\mathbb{H}}, \qquad |\rho| = 1.
$$

So the roots of $-1$ in the quaternion algebra form the unit two-sphere $\mathbb{S}^2$ in the three-dimensional space of pure real quaternions. This is the same as in the discrete case.

The choice of root $\rho$ determines the **axis** of the Fourier transform. Different choices of $\rho$ give different decompositions, and the transforms are related by conjugation in the quaternion algebra.

## The Continuous Transform Pair

### Definition

Let $f : \mathbb{R} \to \mathbb{H}_{\mathbb{D}}$ be a split-biquaternion-valued function. The **continuous split-biquaternion Fourier transform** of $f$ is

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

**Theorem (Riemann–Lebesgue).** If $f : \mathbb{R} \to \mathbb{H}_{\mathbb{D}}$ is integrable, then

$$
\lim_{|\omega| \to \infty} \|F(\omega)\|_E = 0.
$$

**Proof.** The kernel is bounded and the integrand is integrable. The standard proof for the complex Fourier transform applies component-wise, and the result follows from the component-wise statement. $\square$

### The Inversion Theorem

**Theorem (inversion).** Let $f : \mathbb{R} \to \mathbb{H}_{\mathbb{D}}$ be integrable and continuous at a point $t \in \mathbb{R}$, and let $F$ be integrable. Then

$$
f(t) = \int_{-\infty}^{\infty} \overline{W(t, \omega)} F(\omega) \, d\omega.
$$

**Proof.** The proof follows the standard proof of the inversion theorem for the complex Fourier transform, applied component-wise in the idempotent basis. The key step is the approximation of the identity by a sequence of Gaussian kernels, and the result follows from the corresponding statement for the quaternion transform in each component. $\square$

### The Plancherel Theorem

**Theorem (Plancherel).** The transform extends uniquely to a unitary operator on the space $L^2(\mathbb{R}, \mathbb{H}_{\mathbb{D}})$ of square-integrable split-biquaternion-valued functions, with

$$
\int_{-\infty}^{\infty} \|f(t)\|_E^2 \, dt = \int_{-\infty}^{\infty} \|F(\omega)\|_E^2 \, d\omega.
$$

**Proof.** The proof follows the standard proof of the Plancherel theorem, using the factorization into quaternion transforms established below. Since the factorization is an isometry on each quaternion component, and the idempotent decomposition is a linear isomorphism that scales the Euclidean norm by the same factor $\sqrt{2}$ on the signal and on the transform (from $\|\tilde{Q}\|_E^2 = \frac12(\|\tilde{Q}_+\|_E^2 + \|\tilde{Q}_-\|_E^2)$, so that the factor cancels between the two sides), the total norm is preserved. $\square$

**Corollary (Parseval).** For $f, g \in L^2(\mathbb{R}, \mathbb{H}_{\mathbb{D}})$,

$$
\int_{-\infty}^{\infty} \overline{f(t)} g(t) \, dt = \int_{-\infty}^{\infty} \overline{F(\omega)} G(\omega) \, d\omega.
$$

## Factorization into Quaternion and Complex Fourier Transforms

### The Idempotent Decomposition of the Transform

The transform decomposes in the idempotent basis. Writing $f(t) = f_+(t) e_+ + f_-(t) e_-$ and using the fact that the kernel is the same in both components,

$$
F(\omega) = \left(\int_{-\infty}^{\infty} W(t, \omega) f_+(t) \, dt\right) e_+ + \left(\int_{-\infty}^{\infty} W(t, \omega) f_-(t) \, dt\right) e_-.
$$

So the transform is the pair of the **quaternion Fourier transforms** of the two idempotent components:

$$
F(\omega) = F_+(\omega) e_+ + F_-(\omega) e_-,
$$

where $F_\pm(\omega) = \int_{-\infty}^{\infty} W(t, \omega) f_\pm(t) \, dt$ is the quaternion Fourier transform of the component $f_\pm$.

This is the fundamental simplification: the split biquaternion Fourier transform reduces to **two independent quaternion Fourier transforms**, one for each idempotent component.

### The Quaternion Fourier Transform

The quaternion Fourier transform of a quaternion-valued function $g : \mathbb{R} \to \mathbb{H}$ is defined by

$$
G(\omega) = \int_{-\infty}^{\infty} W(t, \omega) g(t) \, dt,
$$

where $W(t, \omega) = \exp(-2\pi \rho \omega t)$ and $\rho$ is a unit pure real quaternion.

The quaternion Fourier transform can be computed in several ways. The standard approach is to choose two other unit pure real quaternions $\nu$ and $\xi$ such that $\{\rho, \nu, \xi\}$ is an orthonormal basis of $\mathbb{R}^3_{\mathbb{H}}$, and to express $g(t)$ in the basis $\{e_0, \rho, \nu, \xi\}$:

$$
g(t) = g_0(t) e_0 + g_\rho(t) \rho + g_\nu(t) \nu + g_\xi(t) \xi, \qquad g_\bullet(t) \in \mathbb{C}.
$$

The quaternion Fourier transform then decomposes into **four complex Fourier transforms**, one for each complex coefficient, as discussed in the biquaternion continuous harmonic analysis article.

### The Full Factorization

Combining the idempotent decomposition with the quaternion Fourier transform factorization, the split biquaternion Fourier transform decomposes into **eight complex Fourier transforms**:

- Two idempotent components, each with four complex coefficients.

This is the total number of complex transforms required for a general split-biquaternion-valued function.

If the function takes values in a subspace with fewer complex components, the number of complex transforms is reduced:

- **Split complex subspace:** The function has two real components. The transform reduces to **two complex Fourier transforms** (one for each idempotent component, after splitting each component into real and imaginary parts; since the components are real scalars, only two real Fourier transforms are needed).
- **Quaternion subspace:** The function has four real components. The transform reduces to **four complex Fourier transforms** (one for each component of the quaternion Fourier transform).
- **General split biquaternion:** The function has eight real components. The transform requires **eight complex Fourier transforms**.

### Why This Matters

The factorization shows that the split biquaternion Fourier transform is not a fundamentally new operation: it is the quaternion Fourier transform applied to the two idempotent components, dressed in split biquaternion language. The non-trivial content is the **choice of root** $\rho$ and the **idempotent decomposition**. Everything else is ordinary harmonic analysis.

## The Convolution Theorem

### Definition of Convolution

Let $f, g : \mathbb{R} \to \mathbb{H}_{\mathbb{D}}$ be two split-biquaternion-valued functions. The **convolution** of $f$ and $g$ is

$$
(f * g)(t) = \int_{-\infty}^{\infty} f(\tau) g(t - \tau) \, d\tau,
$$

provided the integral converges. The convolution is **not commutative** in general, because the split biquaternion product is not commutative.

### The Convolution Theorem

**Theorem (convolution theorem).** Let $f, g : \mathbb{R} \to \mathbb{H}_{\mathbb{D}}$ be integrable, and let $\mathcal{F}$ denote the continuous split-biquaternion Fourier transform with the kernel on the left:

$$
\mathcal{F}[f](\omega) = \int_{-\infty}^{\infty} W(t, \omega) f(t) \, dt.
$$

Then

$$
\mathcal{F}[f * g](\omega) = \mathcal{F}[f](\omega) \cdot \mathcal{F}[g](\omega),
$$

where the product on the right is the split biquaternion product.

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

The convolution theorem implies that convolution in the time domain becomes **split biquaternion multiplication** in the frequency domain. The convolution is associative, distributive over addition, and not commutative.

### The Convolution Theorem in the Idempotent Basis

In the idempotent basis, the convolution decomposes:

$$
(f * g)_+ = f_+ * g_+, \qquad (f * g)_- = f_- * g_-,
$$

where $*$ on the right is the quaternion convolution. So the split biquaternion convolution is the pair of the quaternion convolutions of the two idempotent components. This is the cleanest form of the convolution theorem.

## The Relation to the Differential Operators

The continuous Fourier transform is the natural tool for analysing the differential operators of the analysis article. This is the main structural content of the continuous theory.

### The Gradient

Let $\tilde{\nabla}$ be the split biquaternion gradient on a four-dimensional subspace $V \subset \mathbb{H}_{\mathbb{D}}$, with coordinates $x_0, x_1, x_2, x_3$. For a function $\tilde{F} : V \to \mathbb{H}_{\mathbb{D}}$, the Fourier transform in the variable $x_0$ (with the other coordinates treated as parameters, or with a full four-dimensional transform) diagonalizes the partial derivative $\partial_0$:

$$
\mathcal{F}[\partial_0 \tilde{F}](\omega) = 2\pi \rho \omega \, \mathcal{F}[\tilde{F}](\omega),
$$

where the sign depends on the convention for the kernel.

If the transform is taken in all four variables, the gradient becomes multiplication by the split biquaternion

$$
2\pi \rho (\omega_0 e_0 + \omega_1 e_1 + \omega_2 e_2 + \omega_3 e_3),
$$

where $\omega_0, \omega_1, \omega_2, \omega_3$ are the frequency variables conjugate to $x_0, x_1, x_2, x_3$. The precise form depends on the placement of the root $\rho$ and on the choice of basis, but the structural fact is that the gradient becomes a split-biquaternion-valued multiplier.

### The d'Alembertian

The d'Alembertian $\Box = \partial_0^2 + \Delta$ is a scalar operator, and it commutes with the Fourier transform. Under the transform,

$$
\mathcal{F}[\Box \tilde{F}](\omega) = \left((2\pi \omega_0)^2 - (2\pi)^2 (\omega_1^2 + \omega_2^2 + \omega_3^2)\right) \mathcal{F}[\tilde{F}](\omega) = -4\pi^2 (\omega_0^2 - \omega_1^2 - \omega_2^2 - \omega_3^2) \mathcal{F}[\tilde{F}](\omega).
$$

The multiplier is a scalar (times $e_0$), and it vanishes on the **light cone**

$$
\omega_0^2 = \omega_1^2 + \omega_2^2 + \omega_3^2.
$$

So the Fourier transform of a solution of $\Box \tilde{F} = 0$ is supported on the light cone.

### The Square of the Gradient

The square of the gradient $\tilde{\nabla}^2 = (\partial_0^2 - \Delta) + 2\sum_k e_k \partial_0 \partial_k$ is a split-biquaternion-valued operator. Under the transform, it becomes multiplication by

$$
-4\pi^2 \Big[\Big(\omega_0^2 - \sum_k \omega_k^2\Big) e_0 + 2\omega_0 \sum_k e_k \omega_k\Big],
$$

which is a split-biquaternion-valued multiplier.

### The Convective Derivative

The convective derivative $\tilde{D} = \bar{\tilde{U}} \tilde{\nabla}$ becomes multiplication by the split biquaternion

$$
\bar{\tilde{U}} \cdot 2\pi \rho (\omega_0 e_0 + \omega_1 e_1 + \omega_2 e_2 + \omega_3 e_3),
$$

which depends on the velocity split biquaternion $\tilde{U}$ and on the frequency variables.

### The General Principle

The general principle is that the continuous Fourier transform **diagonalizes the constant-coefficient differential operators** on the four-dimensional subspaces. The symbol of the operator is a split-biquaternion-valued function of the frequency variables, and the solutions of the operator equation are determined by the support of the transform on the zero set of the symbol.

### The Operators in the Idempotent Basis

In the idempotent basis, the differential operators act componentwise on the two idempotent components. For a function $\tilde{F} = \tilde{F}_+ e_+ + \tilde{F}_- e_-$ with $\tilde{F}_\pm \in \mathbb{H}$, the gradient acts as

$$
\tilde{\nabla} \tilde{F} = (\tilde{\nabla} \tilde{F}_+) e_+ + (\tilde{\nabla} \tilde{F}_-) e_-,
$$

where $\tilde{\nabla}$ on the right is the quaternion gradient acting on each component. The d'Alembertian and the convective derivative act in the same way. So the split biquaternion analysis is the quaternion analysis applied to each of the two idempotent components separately, and the Fourier transform diagonalizes the operators in each component.

## The Vanishing-Norm Issue

### Functions of Vanishing Norm

A function $f : \mathbb{R} \to \mathbb{H}_{\mathbb{D}}$ may take values of vanishing norm form on a set of positive measure. In the idempotent basis, such values are exactly those with a vanishing idempotent component: $f_+(t) = 0$ or $f_-(t) = 0$.

### Consequences for the Transform

- **The transform is not necessarily invertible on functions that take zero-divisor values on a set of positive measure.**
- **The transform is invertible on functions where both idempotent components are nonzero almost everywhere.**

The precise condition under which the transform is invertible on a function with zero-divisor values is not known; it depends on the cancellations in the integral.

### Structural Interpretation

The vanishing-norm issue is a genuinely split biquaternion feature. It does not arise in the quaternion Fourier transform, because the quaternion algebra is a division algebra. It arises in the biquaternion case as well, but the zero divisor structure is different: in the split biquaternion case, the zero divisor set is the union of two four-dimensional linear subspaces, while in the biquaternion case, it is a complex cone of complex dimension $3$ (real dimension $6$).

The issue can be avoided by restricting to functions whose values lie in a subspace where the norm form is nonzero, such as the quaternion subspace $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$. On the quaternion subspace, every nonzero value is invertible, and the transform is invertible on all functions.

## The Relation to the Discrete Transform

### Sampling

The continuous transform is the limit of the discrete transform as the number of samples $N$ tends to infinity and the sampling interval tends to zero. The precise relation is the standard one: if $f$ is a function of bounded variation and $F$ is its continuous transform, then the discrete transform of the samples $f(nT)$ for $n \in \mathbb{Z}$ approximates $F$ as the sampling interval $T$ tends to zero.

### Periodization

Conversely, the discrete transform is the periodization of the continuous transform. If $f$ is a function with continuous transform $F$, then the discrete transform of the samples $f(nT)$ is the periodization of $F$:

$$
F_{\text{disc}}[u] = \frac{1}{T} \sum_{k \in \mathbb{Z}} F\left(\frac{u}{NT} + \frac{k}{T}\right).
$$

This is the standard Poisson summation formula, and it holds in the split biquaternion case with the same proof, because the kernel is the ordinary complex kernel in the direction $\rho$.

### The Sampling Theorem

The **sampling theorem** (or Shannon–Nyquist theorem) states that a function whose continuous transform is supported in a bounded interval $[-W, W]$ can be reconstructed from its samples at the rate $1/(2W)$. The split biquaternion version of the sampling theorem holds under the same conditions, with the reconstruction formula

$$
f(t) = \sum_{n \in \mathbb{Z}} f(nT) \operatorname{sinc}\left(\frac{t - nT}{T}\right),
$$

where the sinc function is the ordinary real sinc, and the convergence is in the appropriate sense. The proof is the same as in the complex case, because the reconstruction is component-wise.

## Open Questions

1. **The precise invertibility condition.** Under what conditions on the zero-divisor values is the continuous transform invertible? The answer is not known.

2. **The support of the transform of solutions of $\tilde{\nabla}\tilde{F} = 0$.** The Fourier transform of a solution of the gradient equation $\tilde{\nabla}\tilde{F} = 0$ is supported on a set determined by the symbol of the gradient. What is the structure of this set?

3. **The Plancherel theorem for general functions.** Under what conditions does the Plancherel theorem hold for functions that take zero-divisor values? The current statement requires square-integrability, which is a norm condition and does not detect the zero divisors.

4. **Wavelets and time-frequency analysis.** Can a split biquaternion wavelet transform be defined, and what are its properties? Can a split biquaternion time-frequency distribution be defined?

5. **The relation to the analysis article.** The connection between the continuous Fourier transform and the differential operators is established at the level of symbols. What are the deeper consequences for the structure of the solutions of the operator equations?

6. **The Clifford algebra framework.** How does the split biquaternion continuous Fourier transform fit into the general theory of Clifford algebra Fourier transforms with split signature?

7. **The relation to the biquaternion case.** The split biquaternion transform reduces to two quaternion transforms, while the biquaternion transform reduces to four complex transforms. What are the advantages and disadvantages of each in applications?


## Summary

The continuous split-biquaternion Fourier transform is defined by the kernel $W(t, \omega) = \exp(-2\pi \rho \omega t)$, where $\rho$ is a unit pure real quaternion (a root of $-1$ in the quaternion algebra). The kernel is the same in both idempotent components, so the transform decomposes into two independent quaternion Fourier transforms, one for each component.

The transform is invertible on functions where both idempotent components are nonzero almost everywhere, and it satisfies the Riemann–Lebesgue lemma, the inversion theorem, and the Plancherel theorem. It factorizes into eight complex Fourier transforms for a general split-biquaternion-valued function, four for a quaternion-valued function, and two for a split-complex-valued function. The convolution theorem holds, with the non-commutativity inherited from the quaternion case.

The transform diagonalizes the constant-coefficient differential operators of the analysis article: the gradient becomes a split-biquaternion-valued multiplier, the d'Alembertian becomes a scalar multiplier vanishing on the light cone, and the convective derivative becomes a split-biquaternion-valued multiplier depending on the velocity. In the idempotent basis, the operators act componentwise, and the transform diagonalizes them in each quaternion component.

The vanishing-norm issue is a genuinely split biquaternion feature: functions that take zero-divisor values on a set of positive measure are not necessarily recoverable from their transform, and the precise invertibility condition is not known.

The continuous transform is the limit of the discrete transform as the sampling interval tends to zero, and it is related to the discrete transform by the Poisson summation formula and the sampling theorem.

The key simplification relative to the biquaternion case is the **idempotent decomposition**: the split biquaternion algebra is the direct sum of two copies of the quaternion algebra, so the split biquaternion Fourier transform reduces to two quaternion Fourier transforms. The split complex unit $j$ does not appear in the kernel; it only appears in the idempotent decomposition that separates the two components.

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original formulation of quaternions.
- S. Said, N. Le Bihan, S. J. Sangwine, "Fast complexified quaternion Fourier transform", *IEEE Transactions on Signal Processing* **56** (2008) 1522–1531, for the definition and factorization of the biquaternion Fourier transform, which is closely related.
- S. J. Sangwine and T. A. Ell, "Complexification of the quaternion roots of $-1$", arXiv:math.RA/0506190 (2005), for the classification of the biquaternion roots of $-1$, which provides background for the quaternion roots.
- S. J. Sangwine and D. Alfsmann, "Determination of the biquaternion divisors of zero, including the idempotents and nilpotents", arXiv:0812.1102 (2008), for the classification of the zero divisors, which provides background for the split biquaternion zero divisors.
- N. Le Bihan and J. Mars, "Singular value decomposition of quaternion matrices: a new tool for vector-sensor signal processing", *Signal Processing* **84** (2004) 1177–1199, for the quaternion signal processing background.
- T. A. Ell and S. J. Sangwine, "Hypercomplex Fourier transforms of color images", *IEEE Transactions on Image Processing* **16** (2007) 22–35, for the quaternion Fourier transform and its applications.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the algebraic structure of the split biquaternions.
- F. Brackx, R. Delanghe, and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the general Clifford analysis with split signature.

