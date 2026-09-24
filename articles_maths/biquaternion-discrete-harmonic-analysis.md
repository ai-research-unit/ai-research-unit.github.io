# __Biquaternion Discrete Harmonic Analysis__

## Introduction

This article introduces harmonic analysis for biquaternion-valued sequences. It follows the elementary functions article, which defined the biquaternion exponential, and it uses the division theory article, which characterized the zero divisors and the roots of $-1$.

The treatment is purely mathematical. The goal is to define the discrete biquaternion Fourier transform, establish its basic properties, show how it decomposes into ordinary complex Fourier transforms, and identify the points where the biquaternion structure creates genuinely new phenomena. The continuous analogue is the subject of the companion article on biquaternion continuous harmonic analysis.

The key structural fact is that the Fourier kernel is a biquaternion exponential, and the exponential is defined by a **root of $-1$**. The roots of $-1$ in $\mathbb{B}$ come in two families: the **degenerate roots** (the scalar imaginary $i$, and the unit pure real quaternions), and the **non-trivial roots** (the elements of the form $b\mu + d\nu i$ with $\mu \perp \nu$ and $b^2 - d^2 = 1$). The choice of root determines the nature of the transform. The degenerate roots give the ordinary complex or quaternion Fourier transform; the non-trivial roots give a genuinely biquaternionic transform.

A root of $-1$ is required because of the **de Moivre formula**: the identity

$$
e^{\rho\theta} = \cos\theta \, e_0 + \sin\theta \, \rho, \qquad \rho^2 = -e_0,
$$

holds for any root $\rho$ of $-1$, as a consequence of the alternating structure of the powers of $\rho$ and the power series of the exponential, cosine, and sine. A Fourier transform analyses a signal into sinusoidal components, and the sinusoids are the real and scalar multiples of the exponential of the root.

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

The **biquaternion Fourier kernel** of length $N$ is the function

$$
W_N(n, u) = \exp\left(-2\pi \rho \frac{nu}{N}\right), \qquad n, u \in \{0, 1, \ldots, N-1\}.
$$

Because $\rho^2 = -e_0$, the kernel takes the closed form

$$
W_N(n, u) = \cos\left(2\pi \frac{nu}{N}\right) e_0 - \sin\left(2\pi \frac{nu}{N}\right) \rho,
$$

where the cosine and sine are the ordinary complex trigonometric functions applied to the real argument $2\pi nu/N$. The kernel is therefore a unit biquaternion in the sense that its norm form is $e_0$:

$$
N(W_N(n, u)) = \cos^2\left(2\pi \frac{nu}{N}\right) + \sin^2\left(2\pi \frac{nu}{N}\right) = 1, \qquad N(W_N(n, u)) = e_0.
$$

In particular, the kernel is always invertible, regardless of the choice of root and the values of $n, u$.

### The Condition on the Root

A biquaternion $\rho$ satisfies $\rho^2 = -e_0$ if and only if it is a pure biquaternion (i.e., its scalar part vanishes) and

$$
\Re(\rho) \perp \Im(\rho), \qquad \|\Re(\rho)\|^2 - \|\Im(\rho)\|^2 = 1,
$$

where $\Re(\rho)$ and $\Im(\rho)$ are the real and imaginary quaternion parts of $\rho$, the orthogonality is with respect to the inner product on $\mathbb{H}$, and $\|\cdot\|$ is the norm on $\mathbb{H}$. This is the content of the classification of the biquaternion roots of $-1$ given in the division theory article.

The classification yields three families:

1. **Degenerate root of the first kind:** $\rho = \pm i$, the scalar imaginary.
2. **Degenerate root of the second kind:** $\rho = \pm \mu_{\mathbb{R}}$, a unit pure real quaternion.
3. **Non-trivial roots:** $\rho = b\mu + d\nu i$, where $\mu$ and $\nu$ are perpendicular unit pure real quaternions and $b, d \in \mathbb{R}$ satisfy $b^2 - d^2 = 1$.

The three families are distinct, and the choice of root determines the nature of the transform.

### The Choice of Root

The choice of the root $\rho$ is not neutral. The four cases are the following.

**Scalar imaginary, $\rho = i$.** The kernel reduces to the ordinary complex exponential, and the transform is the ordinary complex Fourier transform applied to each of the four complex coefficients of the signal.

**Unit pure real quaternion, $\rho = \mu_{\mathbb{R}}$.** The kernel is a real quaternion exponential, and the transform is the ordinary quaternion Fourier transform. The quaternion Fourier transform itself has several conventions (left, right, two-sided), and the choice of convention must be stated.

**Non-trivial root, signal in a subspace.** If $\rho$ is a non-trivial root and the signal takes values in the real quaternion subspace $\mathbb{H}_{\mathbb{B}}$ or in the imaginary translate $i \mathbb{H}_{\mathbb{B}}$, the transform reduces to **two** ordinary complex Fourier transforms. The two complex transforms are coupled by the real and imaginary parts of the signal.

**Non-trivial root, fully biquaternion signal.** If $\rho$ is a non-trivial root and the signal takes values in the full biquaternion algebra, the transform requires **four** ordinary complex Fourier transforms. This is the generic case.

The non-trivial roots exist because the biquaternion algebra is not a division algebra: the equation $\rho^2 = -e_0$ has solutions beyond the degenerate ones. This is the first place where the biquaternion structure enters the harmonic analysis in an essential way.

## The Discrete Transform Pair

### Definition

Let $f : \{0, 1, \ldots, N-1\} \to \mathbb{B}$ be a biquaternion-valued sequence. The **discrete biquaternion Fourier transform** of $f$ is the sequence $F : \{0, 1, \ldots, N-1\} \to \mathbb{B}$ defined by

$$
F[u] = \sum_{n=0}^{N-1} W_N(n, u) f[n], \qquad u \in \{0, 1, \ldots, N-1\},
$$

where $W_N(n, u)$ is the kernel defined above. The **inverse transform** is

$$
f[n] = \frac{1}{N} \sum_{u=0}^{N-1} W_N(n, u)^{-1} F[u], \qquad n \in \{0, 1, \ldots, N-1\}.
$$

Since the kernel is a unit biquaternion, its inverse is its quaternion conjugate:

$$
W_N(n, u)^{-1} = \overline{W_N(n, u)} = \cos\left(2\pi \frac{nu}{N}\right) e_0 + \sin\left(2\pi \frac{nu}{N}\right) \rho.
$$

So the inverse transform is

$$
f[n] = \frac{1}{N} \sum_{u=0}^{N-1} \overline{W_N(n, u)} F[u], \qquad n \in \{0, 1, \ldots, N-1\}.
$$

The placement of the kernel on the **left** of $f[n]$ is a choice. An alternative transform has the kernel on the right:

$$
F[u] = \sum_{n=0}^{N-1} f[n] \, W_N(n, u).
$$

The two transforms are closely related: the conjugate of the left-kernel transform of $f$ equals the right-kernel transform of the conjugate of $f$, with a sign change in the kernel. (The outer conjugation is needed: $\overline{K(t,\omega) f(t)} = \overline{f(t)}\,\overline{K(t,\omega)}$.)

### Invertibility

The invertibility of the transform depends on the properties of the kernel and of the signal.

**The kernel has unit norm.** For every $n$ and $u$, the kernel $W_N(n, u)$ satisfies $N(W_N(n, u)) = e_0$, as shown above. So the kernel is always invertible.

**The signal may have vanishing norm.** If a sample $f[n]$ has vanishing norm form, $N(f[n]) = 0$, then $f[n]$ is a zero divisor, and it is not necessarily recoverable from the transform. The precise statement is the following.

**Theorem (invertibility).** If every sample $f[n]$ has non-vanishing norm form, then the transform is invertible: the inverse formula reproduces $f[n]$ for every $n$.

**Proof.** Under the hypothesis, each $f[n]$ is invertible. The transform is a finite sum of products of invertible elements, and the inverse formula is verified by direct computation:

$$
\frac{1}{N} \sum_{u=0}^{N-1} \overline{W_N(n, u)} F[u] = \frac{1}{N} \sum_{u=0}^{N-1} \overline{W_N(n, u)} \sum_{m=0}^{N-1} W_N(m, u) f[m] = \frac{1}{N} \sum_{m=0}^{N-1} \left(\sum_{u=0}^{N-1} \overline{W_N(n, u)} W_N(m, u)\right) f[m].
$$

The inner sum is the standard orthogonality relation:

$$
\sum_{u=0}^{N-1} \overline{W_N(n, u)} W_N(m, u) = \begin{cases} N e_0 & \text{if } n = m, \\ 0 & \text{if } n \neq m, \end{cases}
$$

which holds because the kernel is the ordinary complex kernel in the direction $\rho$, and the orthogonality is the standard one. So the double sum reduces to $f[n]$. $\square$

**The transform is not invertible on signals containing zero-divisor samples.** If some $f[n]$ is a zero divisor, the inverse may not reproduce it. The precise condition under which the transform is invertible on a signal with zero-divisor samples is not known; it depends on the cancellations in the sum.

### Symmetry of the Spectrum

For a signal $f$ that takes values in the real quaternion subspace $\mathbb{H}_{\mathbb{B}}$ and a root $\rho$, the spectrum satisfies a **conjugate symmetry** analogous to the Hermitian symmetry of the ordinary Fourier transform of a real signal.

**Theorem (conjugate symmetry).** Let $f : \{0, 1, \ldots, N-1\} \to \mathbb{H}_{\mathbb{B}}$ be a real quaternion-valued signal, and let $F$ be its discrete biquaternion Fourier transform with respect to a root $\rho$. Then

$$
F[N-u] = \overline{F[u]}, \qquad u = 1, \ldots, N-1.
$$

**Proof.** The proof uses the reality of $f$, i.e., $\overline{f[n]} = f[n]$ for every $n$, and the identity

$$
\overline{W_N(n, N-u)} = W_N(n, u),
$$

which follows from the closed form of the kernel and the parity of the cosine and sine. Then

$$
F[N-u] = \sum_{n=0}^{N-1} W_N(n, N-u) f[n] = \sum_{n=0}^{N-1} \overline{W_N(n, u)} \overline{f[n]} = \overline{\sum_{n=0}^{N-1} W_N(n, u) f[n]} = \overline{F[u]}.
$$

$\square$

The symmetry is the biquaternion analogue of the Hermitian symmetry $F[-u] = F[u]^*$ of the ordinary Fourier transform of a real signal. It is the basis for reconstructing a real signal from half of its spectrum, and it is the reason the standard techniques of real-signal processing extend to the biquaternion setting, provided the signal is real quaternion-valued.

## Factorization into Four Complex Fourier Transforms

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

The coefficients are obtained by resolving the vector part of the biquaternion in the three complex directions defined by the new basis. If the vector part of a biquaternion is $\mathbf{v} = x e_1 + y e_2 + z e_3$ with $x, y, z \in \mathbb{C}$, then the coefficients are

$$
Q_\rho = \langle \rho, \mathbf{v} \rangle, \qquad Q_\nu = \langle \nu, \mathbf{v} \rangle, \qquad Q_\xi = \langle \xi, \mathbf{v} \rangle,
$$

where the inner product is the complex bilinear inner product defined in the basic algebra article. The scalar coefficient $Q_0$ is unchanged.

### The Factorization

Writing each sample $f[n]$ in the new basis,

$$
f[n] = w[n] e_0 + x'[n] \rho + y'[n] \nu + z'[n] \xi,
$$

and substituting into the transform with the closed form of the kernel,

$$
F[u] = \sum_{n=0}^{N-1} \left(\cos\theta_n \, e_0 - \sin\theta_n \, \rho\right) \left(w[n] e_0 + x'[n] \rho + y'[n] \nu + z'[n] \xi\right),
$$

where $\theta_n = 2\pi nu/N$.

Expanding the product and using the multiplication rules of the basis $\{e_0, \rho, \nu, \xi\}$:

$$
e_0 e_0 = e_0, \quad e_0 \rho = \rho, \quad e_0 \nu = \nu, \quad e_0 \xi = \xi,
$$

$$
\rho e_0 = \rho, \quad \rho \rho = -e_0, \quad \rho \nu = \xi, \quad \rho \xi = -\nu,
$$

and collecting terms by basis element, we obtain four sums:

$$
F[u] = F_0[u] e_0 + F_\rho[u] \rho + F_\nu[u] \nu + F_\xi[u] \xi,
$$

where

$$
F_0[u] = \sum_{n=0}^{N-1} \left(\cos\theta_n \, w[n] + \sin\theta_n \, x'[n]\right),
$$

$$
F_\rho[u] = \sum_{n=0}^{N-1} \left(\cos\theta_n \, x'[n] - \sin\theta_n \, w[n]\right),
$$

$$
F_\nu[u] = \sum_{n=0}^{N-1} \left(\cos\theta_n \, y'[n] + \sin\theta_n \, z'[n]\right),
$$

$$
F_\xi[u] = \sum_{n=0}^{N-1} \left(\cos\theta_n \, z'[n] - \sin\theta_n \, y'[n]\right).
$$

### The Complex Fourier Transforms

Each of the four sums is a complex linear combination of the cosine and sine sums with the same argument $\theta_n = 2\pi nu/N$. Using the complex exponential, we can write each sum as a combination of two ordinary complex Fourier transforms:

$$
F_\bullet[u] = \frac{1}{2}\left(\hat{G}_\bullet^{(+)}[u] + \hat{G}_\bullet^{(-)}[u]\right) + \frac{1}{2i}\left(\hat{G}_\bullet^{(+)}[u] - \hat{G}_\bullet^{(-)}[u]\right),
$$

where $\hat{G}_\bullet^{(\pm)}[u]$ are the ordinary complex Fourier transforms of the sequences $G_\bullet^{(\pm)}[n]$ defined by

$$
G_\bullet^{(\pm)}[n] = G_\bullet[n] \exp\left(\pm 2\pi i \frac{n}{N}\right),
$$

and $G_\bullet[n]$ are the complex coefficients of $f[n]$ in the new basis. The precise form depends on the pairing of the real and imaginary parts.

Concretely, the factorization is the following algorithm:

1. **Change of basis.** For each $n$, write the sample $f[n]$ in the basis $\{e_0, \rho, \nu, \xi\}$, obtaining four complex coefficients $w[n], x'[n], y'[n], z'[n]$.
2. **Complex Fourier transforms.** Apply the ordinary complex Fourier transform to the four complex sequences obtained by combining the coefficients as above. The result is four complex spectra.
3. **Reassemble.** Combine the four complex spectra into the biquaternion spectrum $F[u]$.

The result is a fast algorithm for the discrete biquaternion Fourier transform, using existing complex FFT libraries. The cost is four complex FFTs of size $N$, which is $O(N \log N)$, as opposed to the naive evaluation of the transform, which is $O(N^2)$.

### Why This Matters

The factorization is a computational result, but it also has a structural meaning. It shows that the biquaternion Fourier transform is not a fundamentally new operation: it is the ordinary complex Fourier transform applied to the entries of the matrix representation, dressed in biquaternion language. The non-trivial content is the **choice of root** and the **basis change** that it induces. Everything else is ordinary harmonic analysis.

## The Convolution Theorem

### Definition of Convolution

Let $f, g : \mathbb{Z} \to \mathbb{B}$ be two biquaternion-valued sequences, extended to $\mathbb{Z}$ by $f[n] = g[n] = 0$ outside the support $\{0, 1, \ldots, N-1\}$. The **convolution** of $f$ and $g$ is

$$
(f * g)[n] = \sum_{m \in \mathbb{Z}} f[m] g[n - m].
$$

The convolution is **not commutative** in general, because the biquaternion product is not commutative. The order of the factors matters.

### The Convolution Theorem

**Theorem (convolution theorem).** Let $f, g$ be biquaternion-valued sequences with finite support, and let $\mathcal{F}$ denote the discrete biquaternion Fourier transform with the kernel on the left:

$$
\mathcal{F}[f][u] = \sum_{n=0}^{N-1} W_N(n, u) f[n].
$$

Then

$$
\mathcal{F}[f * g][u] = \mathcal{F}[f][u] \cdot \mathcal{F}[g][u],
$$

where the product on the right is the biquaternion product.

**Proof.** Compute

$$
\mathcal{F}[f * g][u] = \sum_{n=0}^{N-1} W_N(n, u) \sum_{m=0}^{N-1} f[m] g[n-m] = \sum_{m=0}^{N-1} \sum_{n=0}^{N-1} W_N(n, u) f[m] g[n-m].
$$

Change variables $n = m + k$, so that $W_N(n, u) = W_N(m + k, u) = W_N(m, u) W_N(k, u)$ (the kernel is multiplicative in the index because the exponential is). Then

$$
\mathcal{F}[f * g][u] = \sum_{m=0}^{N-1} \sum_{k=0}^{N-1} W_N(m, u) f[m] W_N(k, u) g[k] = \left(\sum_{m=0}^{N-1} W_N(m, u) f[m]\right) \left(\sum_{k=0}^{N-1} W_N(k, u) g[k]\right) = \mathcal{F}[f][u] \cdot \mathcal{F}[g][u].
$$

The change of variables and the multiplicativity of the kernel in the index are justified by the closed form of the kernel. $\square$

**Corollary (right-kernel case).** For the transform with the kernel on the right,

$$
\mathcal{F}_{\text{right}}[f * g][u] = \mathcal{F}_{\text{right}}[g][u] \cdot \mathcal{F}_{\text{right}}[f][u].
$$

The order of the factors is reversed, because the kernel is on the other side.

### Consequences

The convolution theorem implies that convolution in the signal domain becomes **biquaternion multiplication** in the frequency domain. This is the basis for filtering: a biquaternion-valued filter can be applied by pointwise multiplication in the frequency domain.

It also implies that the convolution is:

- **Associative:** $(f * g) * h = f * (g * h)$.
- **Distributive over addition:** $f * (g + h) = f * g + f * h$.
- **Not commutative:** $f * g \neq g * f$ in general.

The non-commutativity is a genuinely biquaternionic feature of the harmonic analysis. In the complex and quaternion cases, the convolution is also non-commutative, but the quaternion case has been studied; the biquaternion case is a natural extension.

## The Vanishing-Norm Issue

### Samples of Vanishing Norm

A sample $f[n]$ with $N(f[n]) = 0$ is a zero divisor. Such samples have the property that they cannot necessarily be recovered from the transform.

More precisely, if $f[n]$ is a zero divisor, there exists a nonzero biquaternion $\tilde{Z}$ with $f[n] \circ \tilde{Z} = 0$ or $\tilde{Z} \circ f[n] = 0$. The kernel is invertible, so multiplying $f[n]$ by the kernel gives another zero divisor, and the sum over $n$ may or may not preserve the information of $f[n]$.

### Consequences for the Transform

- **The transform is not necessarily invertible on signals containing zero-divisor samples.** The inverse transform may not recover the vanished information.
- **The transform is invertible on signals of non-vanishing norm.** If every sample has non-vanishing norm form, the transform is invertible (Theorem above).

### Structural Interpretation

The vanishing-norm issue is a genuinely biquaternionic feature. It does not arise in the complex or quaternion Fourier transforms, because the complex and quaternion algebras are division algebras: every nonzero element has an inverse. The biquaternion algebra is not a division algebra, and this is reflected in the harmonic analysis.

The issue can be avoided by restricting the signals to a subspace where the norm form is nonzero, such as the quaternion subspace $\mathbb{H}_{\mathbb{B}}$. On $\mathbb{H}_{\mathbb{B}}$, every nonzero sample is invertible, and the transform is invertible on all signals. On the anti-Hermitian subspace $\mathbb{M}_-$, the samples with vanishing norm lie on a cone, and the transform is invertible only for signals whose samples lie off this cone.

### The Open Question

The precise condition under which the transform is invertible on a signal with zero-divisor samples is not known. It depends on the cancellations in the sum $\sum_n W_N(n, u) f[n]$, and it is not determined by the norms of the samples alone. This is one of the open questions listed below.

## The Two-Dimensional Transform

### Definition

For a biquaternion-valued image $f : \{0, 1, \ldots, M-1\} \times \{0, 1, \ldots, N-1\} \to \mathbb{B}$, the **two-dimensional discrete biquaternion Fourier transform** is

$$
F[u, v] = \sum_{m=0}^{M-1} \sum_{n=0}^{N-1} W_M(m, u) \, f[m, n] \, W_N(n, v),
$$

where $W_M$ and $W_N$ are the one-dimensional kernels of lengths $M$ and $N$, respectively. The two kernels can also be placed both on the left, or both on the right, depending on the convention.

### Factorization

The two-dimensional transform factorizes into four two-dimensional complex transforms, just as in the one-dimensional case. The change of basis is the same: write each sample in the basis $\{e_0, \rho, \nu, \xi\}$, apply the two-dimensional complex transform to the four complex sequences, and reassemble.

### Separability

The two-dimensional kernel is **separable**, in the sense that

$$
W_{M \times N}((m, n), (u, v)) = W_M(m, u) \, W_N(n, v).
$$

This follows from the multiplicativity of the exponential. The separability is what allows the two-dimensional transform to be computed as a sequence of one-dimensional transforms.

## Higher-Dimensional Transforms

The generalization to higher dimensions is straightforward. The transform of a biquaternion-valued function on $\{0, 1, \ldots, N_1 - 1\} \times \cdots \times \{0, 1, \ldots, N_d - 1\}$ is defined by $d$ kernels, one for each dimension. The transform factorizes into $4$ complex transforms per biquaternion component, in the fully general case, or fewer in the degenerate cases.

The higher-dimensional transform is separable, and it can be computed by applying one-dimensional transforms along each dimension in turn.

## Open Questions

1. **Wavelets.** Can a biquaternion wavelet transform be defined, and what are its properties? The wavelet kernel is more general than the Fourier kernel, and the biquaternion structure may introduce new phenomena.

2. **Time-frequency analysis.** Can a biquaternion time-frequency distribution (Wigner, spectrogram, etc.) be defined, and what are its properties?

3. **Non-commutative filtering.** What are the implications of the non-commutativity of the biquaternion product for signal processing? Convolution is not commutative, and the standard filtering theory assumes commutativity.

4. **The spectrum and vanishing norms.** It is not known whether the spectrum of a biquaternion Fourier transform of a real or imaginary quaternion signal can have samples with vanishing norm. If it can occur, it would mean that the transform is not invertible on such signals.

5. **The precise invertibility condition.** Under what conditions on the zero-divisor samples is the transform invertible? The answer is not known.

6. **The relation to the continuous transform.** How does the discrete transform relate to the continuous transform of the companion article? The sampling and periodization theorems should be stated.

7. **The Clifford algebra framework.** How does the biquaternion discrete Fourier transform fit into the general theory of Clifford algebra Fourier transforms?

## Summary

The discrete biquaternion Fourier transform is defined by the kernel $W_N(n, u) = \exp(-2\pi \rho nu/N)$, where $\rho$ is a root of $-1$ in $\mathbb{B}$. The choice of root determines the nature of the transform: the scalar imaginary gives the ordinary complex transform, the unit pure real quaternions give the quaternion transform, and the non-trivial roots give genuinely biquaternionic transforms.

The transform is invertible on signals of non-vanishing norm, and it satisfies the conjugate symmetry for real quaternion signals. It factorizes into four complex Fourier transforms, which gives a fast algorithm using existing complex FFT libraries. The convolution theorem holds, with the non-commutativity requiring careful placement of the kernel.

The vanishing-norm issue is a genuinely biquaternionic feature: signals containing zero-divisor samples are not necessarily recoverable from their transform, and the precise invertibility condition is not known.

The discrete transform is the discrete analogue of the continuous transform of the companion article, and it is the basis for the biquaternion signal processing applications.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra, $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ |
| $f : \{0,\dots,N-1\} \to \mathbb{B}$ | Biquaternion-valued sequence |
| $F[u]$ | Discrete biquaternion Fourier transform of $f$, defined by $F[u] = \sum_n W_N(n,u)f[n]$ |
| $W_N(n,u) = \exp(-2\pi\rho nu/N)$ | Discrete Fourier kernel, placed on the left of $f$; $\overline{W_N(n,u)}$ gives the inverse transform |
| $\rho$ | Root of $-1$ in $\mathbb{B}$; the degenerate roots give the complex or quaternion transform, the non-trivial roots a genuinely biquaternionic one |
| $N$ | Number of samples, in the kernel $W_N$ |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$ | Norm form; not to be confused with the sample count $N$ |
| $\mathbf{Q} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3$ | Vector part of a biquaternion |
| $e^{\rho\theta} = \cos\theta\,e_0 + \sin\theta\,\rho$ | de Moivre formula, valid for every root $\rho$ of $-1$ |

## Further Reading

- S. Said, N. Le Bihan, S. J. Sangwine, "Fast complexified quaternion Fourier transform", *IEEE Transactions on Signal Processing* **56** (2008) 1522–1531, for the definition and factorization of the biquaternion Fourier transform.
- S. J. Sangwine and T. A. Ell, "Complexification of the quaternion roots of $-1$", arXiv:math.RA/0506190 (2005), for the classification of the biquaternion roots of $-1$.
- S. J. Sangwine and D. Alfsmann, "Determination of the biquaternion divisors of zero, including the idempotents and nilpotents", arXiv:0812.1102 (2008), for the classification of the zero divisors.
- N. Le Bihan and J. Mars, "Singular value decomposition of quaternion matrices: a new tool for vector-sensor signal processing", *Signal Processing* **84** (2004) 1177–1199, for the quaternion signal processing background.
- T. A. Ell and S. J. Sangwine, "Hypercomplex Fourier transforms of color images", *IEEE Transactions on Image Processing* **16** (2007) 22–35, for the quaternion Fourier transform and its applications.
- W. R. Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original formulation of quaternions and biquaternions.

