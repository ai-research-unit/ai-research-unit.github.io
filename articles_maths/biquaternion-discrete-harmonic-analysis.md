# __Biquaternion Discrete Harmonic Analysis__

## Introduction

This article introduces harmonic analysis for biquaternion-valued sequences. It follows the elementary functions article, which defined the biquaternion exponential, and it uses the division theory article, which characterized the zero divisors and the roots of $-1$.

The treatment is purely mathematical. The goal is to define the discrete biquaternion Fourier transform, establish its basic properties, show how it decomposes into ordinary complex Fourier transforms, and identify the points where the biquaternion structure creates genuinely new phenomena. The transform of an infinite sequence, the **biquaternion Z transform**, is treated at the end of the article; it is the discrete analogue of the Laplace transform and the tool for linear recurrences with constant biquaternion coefficients. The continuous analogue is the subject of the companion article on biquaternion continuous harmonic analysis.

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

The scalar imaginary is $i$, which commutes with the quaternion units. The quaternion conjugate is $\tilde{Q}^{\natural} = Q_0 e_0 - \mathbf{Q}$, and the biquaternion norm is $N(\tilde{Q}) = \tilde{Q} \tilde{Q}^{\natural}$.

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

where the cosine and sine are the ordinary complex trigonometric functions applied to the real argument $2\pi nu/N$. The kernel is therefore a unit biquaternion in the sense that its biquaternion norm is $e_0$:

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

**The signal may have vanishing norm.** If a sample $f[n]$ has vanishing norm, $N(f[n]) = 0$, then $f[n]$ is a zero divisor, and it is not necessarily recoverable from the transform. The precise statement is the following.

**Theorem (invertibility).** If every sample $f[n]$ has non-vanishing norm, then the transform is invertible: the inverse formula reproduces $f[n]$ for every $n$.

**Proof.** Under the hypothesis, each $f[n]$ is invertible. The transform is a finite sum of products of invertible elements, and the inverse formula is verified by direct computation:

$$
\frac{1}{N} \sum_{u=0}^{N-1} \overline{W_N(n, u)} F[u] = \frac{1}{N} \sum_{u=0}^{N-1} \overline{W_N(n, u)} \sum_{m=0}^{N-1} W_N(m, u) f[m] = \frac{1}{N} \sum_{m=0}^{N-1} \left(\sum_{u=0}^{N-1} \overline{W_N(n, u)} W_N(m, u)\right) f[m].
$$

The inner sum is the standard orthogonality relation:

$$
\sum_{u=0}^{N-1} \overline{W_N(n, u)} W_N(m, u) = \begin{cases} N e_0 & \text{if } n = m, \\ 0 & \text{if } n \neq m, \end{cases}
$$

which holds because the kernel is the ordinary complex kernel in the direction $\rho$, and the orthogonality is the standard one. So the double sum reduces to $f[n]$.

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

The coefficients are obtained by resolving the vector part of the biquaternion in the three complex directions defined by the new basis. If the vector part of a biquaternion is $\mathbf{v} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3$ with $Q_1, Q_2, Q_3 \in \mathbb{C}$, then the coefficients are

$$
Q_\rho = \langle \rho, \mathbf{v} \rangle, \qquad Q_\nu = \langle \nu, \mathbf{v} \rangle, \qquad Q_\xi = \langle \xi, \mathbf{v} \rangle,
$$

where the pairing is the complex bilinear dot product $\sum_k Q_k P_k$ defined in *The Four Biquaternion Complex Products*, §*The Complex Bilinear Product $\tilde P\tilde Q$* (the polar form of the biquaternion norm, not the Hermitian inner product). The scalar coefficient $Q_0$ is unchanged.

### The Factorization

Writing each sample $f[n]$ in the new basis,

$$
f[n] = w[n] e_0 + Q_\rho[n] \rho + Q_\nu[n] \nu + Q_\xi[n] \xi,
$$

and substituting into the transform with the closed form of the kernel,

$$
F[u] = \sum_{n=0}^{N-1} \left(\cos\theta_n \, e_0 - \sin\theta_n \, \rho\right) \left(w[n] e_0 + Q_\rho[n] \rho + Q_\nu[n] \nu + Q_\xi[n] \xi\right),
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
F_0[u] = \sum_{n=0}^{N-1} \left(\cos\theta_n \, w[n] + \sin\theta_n \, Q_\rho[n]\right),
$$

$$
F_\rho[u] = \sum_{n=0}^{N-1} \left(\cos\theta_n \, Q_\rho[n] - \sin\theta_n \, w[n]\right),
$$

$$
F_\nu[u] = \sum_{n=0}^{N-1} \left(\cos\theta_n \, Q_\nu[n] + \sin\theta_n \, Q_\xi[n]\right),
$$

$$
F_\xi[u] = \sum_{n=0}^{N-1} \left(\cos\theta_n \, Q_\xi[n] - \sin\theta_n \, Q_\nu[n]\right).
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

1. **Change of basis.** For each $n$, write the sample $f[n]$ in the basis $\{e_0, \rho, \nu, \xi\}$, obtaining four complex coefficients $w[n], Q_\rho[n], Q_\nu[n], Q_\xi[n]$.
2. **Complex Fourier transforms.** Apply the ordinary complex Fourier transform to the four complex sequences obtained by combining the coefficients as above. The result is four complex spectra.
3. **Reassemble.** Combine the four complex spectra into the biquaternion spectrum $F[u]$.

The result is a fast algorithm for the discrete biquaternion Fourier transform, using existing complex FFT libraries. The cost is four complex FFTs of size $N$, which is $O(N \log N)$, as opposed to the naive evaluation of the transform, which is $O(N^2)$.

### Why This Matters

The factorization is a computational result, but it also has a structural meaning. It shows that the biquaternion Fourier transform is not a fundamentally new operation: it is the ordinary complex Fourier transform applied entrywise to the coefficients, dressed in biquaternion language. The non-trivial content is the **choice of root** and the **basis change** that it induces. Everything else is ordinary harmonic analysis.

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

The change of variables and the multiplicativity of the kernel in the index are justified by the closed form of the kernel.

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

More precisely, if $f[n]$ is a zero divisor, there exists a nonzero biquaternion $\tilde{R}$ with $f[n] \circ \tilde{R} = 0$ or $\tilde{R} \circ f[n] = 0$. The kernel is invertible, so multiplying $f[n]$ by the kernel gives another zero divisor, and the sum over $n$ may or may not preserve the information of $f[n]$.

### Consequences for the Transform

- **The transform is not necessarily invertible on signals containing zero-divisor samples.** The inverse transform may not recover the vanished information.
- **The transform is invertible on signals of non-vanishing norm.** If every sample has non-vanishing norm, the transform is invertible (Theorem above).

### Structural Interpretation

The vanishing-norm issue is a genuinely biquaternionic feature. It does not arise in the complex or quaternion Fourier transforms, because the complex and quaternion algebras are division algebras: every nonzero element has an inverse. The biquaternion algebra is not a division algebra, and this is reflected in the harmonic analysis.

The issue can be avoided by restricting the signals to a subspace where the biquaternion norm is nonzero, such as the quaternion subspace $\mathbb{H}_{\mathbb{B}}$. On $\mathbb{H}_{\mathbb{B}}$, every nonzero sample is invertible, and the transform is invertible on all signals. On the anti-Hermitian subspace $\mathbb{M}_-$, the samples with vanishing norm lie on a cone, and the transform is invertible only for signals whose samples lie off this cone.

### The Open Question

The precise condition under which the transform is invertible on a signal with zero-divisor samples is not known. It depends on the cancellations in the sum $\sum_n W_N(n, u) f[n]$, and it is not determined by the biquaternion norms of the samples alone. This is one of the open questions listed below.

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

## The Z Transform

### Definition

The transform pair above analyses a finite sequence; the transform of this section analyses an infinite one, and it is the discrete analogue of the Laplace transform rather than of the Fourier transform. Let $f = \{f_n\}_{n \ge 0}$ be a biquaternion-valued sequence. Its **Z transform** is

$$
\mathcal{X}[f](\tilde{Q}) = \sum_{n=0}^{\infty} f_n \tilde{Q}^{-n}, \qquad \tilde{Q} \in \mathbb{B}^{\times},
$$

the generating function of the sequence, and the variable ranges over the units of $\mathbb{B}$ because its negative powers occur in the definition. Substituting $\tilde{Q} = e^{s}$ turns the sum into $\sum_n f_n e^{-ns}$, the discrete Laplace transform of the sequence, and the region of convergence discussed below is the analogue of the half-plane of the continuous theory. Evaluating the transform at the $N$-th roots of unity instead, $\tilde{Q} = e^{2\pi i u/N}$, returns the ordinary complex discrete Fourier transform of the periodisation of the sequence, which is the degenerate case $\rho = i$ of the transform pair above.

The sample $f_n$ is written on the **left** of the variable, so the variable plays the role that the kernel played above. This is the mirror image of the convention of the transform pair, and it is not neutral: the rules below move powers of $\tilde{Q}$ through the sequence, and with the variable placed on the left the $\tilde Q'$-scaling rule would require every sample to commute with $\tilde Q'$. The two conventions are interconverted by the quaternion conjugate. Writing

$$
\mathcal{Y}[f](\tilde{Q}) = \sum_{n=0}^{\infty} \tilde{Q}^{-n} f_n
$$

for the transform with the variable on the left,

$$
\overline{\mathcal{X}[f](\tilde{Q})} = \mathcal{Y}[\bar f](\bar{\tilde{Q}}),
$$

because quaternion conjugation reverses products and $\overline{\tilde{Q}^{-1}} = \bar{\tilde{Q}}^{-1}$.

### The Region of Convergence

Two norms describe the size of a biquaternion, and the choice between them is the whole difficulty of the convergence question. The **Euclidean norm** $\lVert\tilde{Q}\rVert = \left(\sum_\mu \lvert Q_\mu\rvert^2\right)^{1/2}$ is the norm of the metric structure of *Biquaternion Analysis*; the **multiplicative real norm** $r(\tilde{Q}) = \sqrt{\lvert N(\tilde{Q})\rvert}$ is the unique real norm that is multiplicative and normalised on the real scalars, by *Biquaternion Norm and Invertibility*. Only the second reduces the question to scalars, because only the second is multiplicative:

$$
r(f_n \tilde{Q}^{-n}) = r(f_n)\,r(\tilde{Q})^{-n}.
$$

So a sequence that grows at most geometrically, $r(f_n) \le \sigma_f^{\,n}$, has terms of seminorm tending to zero as soon as $r(\tilde{Q}) > \sigma_f$, and the Z-transform literature takes the **region of convergence** to be this set, with $\sigma_f$ the **radius of convergence**. Two corrections come from the vanishing of $r$ on the zero divisors.

**Vanishing of the seminorm is not convergence.** The first standard idempotent of *Biquaternion Idempotents and Projections* is

$$
\tilde\Pi_1 = \tfrac12(e_0 + ie_3), \qquad \tilde\Pi_1^2 = \tilde\Pi_1, \qquad N(\tilde\Pi_1) = 0, \qquad r(\tilde\Pi_1) = 0,
$$

and its powers are $\tilde\Pi_1^{\,k} = \tilde\Pi_1$ for $k \ge 1$. Multiplicativity of $r$ then gives

$$
r(\tilde\Pi_1^{\,k}) = r(\tilde\Pi_1)^k = 0 \qquad\text{for every } k,
$$

so every term of the geometric series $\sum_k \tilde\Pi_1^{\,k}$ has seminorm zero, while the partial sums

$$
S_K = \sum_{k=0}^{K-1} \tilde\Pi_1^{\,k} = e_0 + (K-1)\tilde\Pi_1, \qquad r(S_K) = \sqrt{K},
$$

are unbounded in both norms. The point lies inside the claimed region $r(\tilde{Q}) < 1$, and the geometric identity

$$
\sum_{k=0}^{\infty} \tilde{Q}^{k} = (e_0 - \tilde{Q})^{-1}
$$

fails there, because $e_0 - \tilde\Pi_1 = \tilde\Pi_2$ is the complementary idempotent and is again a zero divisor. The series converges exactly when the powers $\tilde{Q}^k$ tend to zero, equivalently, the algebra being finite-dimensional, when every eigenvalue of $\tilde{Q}$, read in the $2\times2$ complex matrix representation of *Biquaternion 2×2 Matrix Element Representation*, has modulus less than one; the sum is then $(e_0 - \tilde{Q})^{-1}$, as the identity $(e_0 - \tilde{Q})S_K = e_0 - \tilde{Q}^K$ shows. The obstruction is the summation and not the multiplication: a finite sum of products is always defined, and only the passage to the limit fails.

**The seminorm radius is the geometric mean of the eigenvalues.** By the same representation the eigenvalues $\lambda_1, \lambda_2$ of $\tilde{Q}$ satisfy $\lambda_1\lambda_2 = N(\tilde{Q})$, so $r(\tilde{Q}) = \sqrt{\lvert\lambda_1\lambda_2\rvert}$ is the geometric mean of their moduli. The region in which the series in $\tilde{Q}^{-1}$ actually converges is governed by the smaller of the two: for a positive real $c$ the series $\sum_k (c\tilde{Q}^{-1})^k$ converges exactly when $c < \min(\lvert\lambda_1\rvert, \lvert\lambda_2\rvert)$. The geometric mean never falls below the minimum, so the region $r(\tilde{Q}) > \sigma_f$ always **contains** the true region and may contain divergent points. For

$$
\tilde{Q} = 3e_0 + ie_1, \qquad N(\tilde{Q}) = 8, \qquad r(\tilde{Q}) = 2\sqrt2 \approx 2.83,
$$

the eigenvalues are $4$ and $2$. With $\sigma_f = 2.5$ the point lies in the region, although $\sum_k (2.5\,\tilde{Q}^{-1})^k$ diverges, its partial sums reaching Euclidean norm $6.8 \times 10^{19}$ at $k = 200$. For an element with real quaternion coordinates the two eigenvalues are conjugate, $r$ is their common modulus, and the two regions coincide, so the correction concerns the biquaternions proper and not the quaternion subspace. In the applications the variable is a complex scalar, where $\tilde{Q}^{-n}$ has norm $\lvert \tilde{Q}\rvert^{-n}$ and the classical theory of the complex Z transform carries over to the coefficients unchanged.

### The Calculation Rules

Each row below is an identity of series, valid wherever the series concerned converge; the rows built from the central calculus carry the commutation hypothesis displayed with them. The sequences are $f$ and $g$, the constants are $c_1, c_2 \in \mathbb{B}$ and $\tilde P, \tilde Q' \in \mathbb{B}$, and $k$ is a non-negative integer.

| Property | Sequence | Transform |
|---|---|---|
| Left linearity | $c_1f + c_2g$ | $c_1\mathcal{X}[f](\tilde{Q}) + c_2\mathcal{X}[g](\tilde{Q})$, for any constants |
| Right linearity | $fc_1 + gc_2$ | $\mathcal{X}[f](\tilde{Q})c_1 + \mathcal{X}[g](\tilde{Q})c_2$, for $c_1\tilde{Q} = \tilde{Q}c_1$ and $c_2\tilde{Q} = \tilde{Q}c_2$ |
| Two-sided linearity | $c_1f + gc_2$ | $c_1\mathcal{X}[f](\tilde{Q}) + \mathcal{X}[g](\tilde{Q})c_2$, for $c_2\tilde{Q} = \tilde{Q}c_2$ |
| $\tilde Q'$-scaling | $f_n\tilde Q'^n$ | $\mathcal{X}[f](\tilde Q'^{-1}\tilde{Q})$, for $\tilde Q'\tilde{Q} = \tilde{Q}\tilde Q'$ |
| $n$-scaling | $nf_n$ | $-\tilde{Q}\,\dfrac{d}{d\tilde{Q}}\mathcal{X}[f](\tilde{Q})$, for $\tilde{Q}$ central |
| Shifting | $f_{n+k}$ | $\mathcal{X}[f](\tilde{Q})\tilde{Q}^{k} - \sum_{n=0}^{k-1} f_n\tilde{Q}^{k-n}$ |
| Inverse shifting | $f_{n-k}$ ($0$ for $n<k$) | $\mathcal{X}[f](\tilde{Q})\tilde{Q}^{-k}$ |
| Convolution | $\sum_{j=0}^{n} f_{n-j}g_j$ | $\mathcal{X}[f](\tilde{Q})\mathcal{X}[g](\tilde{Q})$, for $\tilde{Q}$ central |

The shifting rows need no hypothesis, because $\tilde{Q}^{-(n+k)} = \tilde{Q}^{-n}\tilde{Q}^{-k}$ for the powers of a single element. The $\tilde Q'$-scaling row compares $(\tilde Q'\tilde{Q}^{-1})^n$ with $\tilde Q'^n\tilde{Q}^{-n}$ and therefore needs $\tilde Q'\tilde{Q} = \tilde{Q}\tilde Q'$, and the convolution row needs each $g_j$ to commute with $\tilde{Q}$, which the centrality of $\tilde{Q}$ supplies. The linearity rows show where the non-commutativity bites: a constant written on the right of a sequence may be moved outside the transform only if it commutes with the variable.

### The Elementary Sequences

In the table below the entry $n$ abbreviates the sequence $ne_0$, and the variable is a complex scalar, the case used in the applications. The rows whose base is a biquaternion carry the commutation hypotheses displayed, and the two scalar rows use the $n$-scaling rule, which a complex scalar satisfies.

| $f_n$ | $\mathcal{X}[f](\tilde{Q})$ |
|---|---|
| $e_0$ | $(e_0 - \tilde{Q}^{-1})^{-1}$ |
| $n$ | $\tilde{Q}(\tilde{Q} - e_0)^{-2}$ |
| $n^2$ | $(\tilde{Q} + \tilde{Q}^2)(\tilde{Q} - e_0)^{-3}$ |
| $\tilde P^n$, for $\tilde P\tilde{Q} = \tilde{Q}\tilde P$ | $(e_0 - \tilde P\tilde{Q}^{-1})^{-1}$ |
| $n\tilde P^n$, for $\tilde P\tilde{Q} = \tilde{Q}\tilde P$ | $\tilde P\tilde{Q}^{-1}(e_0 - \tilde P\tilde{Q}^{-1})^{-2}$ |
| $\dfrac{\tilde Q'^n}{n!}$, for $\tilde Q'\tilde{Q} = \tilde{Q}\tilde Q'$ | $e^{\tilde Q'\tilde{Q}^{-1}}$ |

### Recurrence Relations

The purpose of the transform is the solution of linear recurrences with constant biquaternion coefficients,

$$
\sum_{m=0}^{M} f_{n+m}p_m = g_n, \qquad n \ge 0,
$$

where the coefficients $p_m$ are biquaternions and the right-hand side $g$ is a known sequence. Transforming both sides with the shifting and linearity rules converts the recurrence into an algebraic equation for $\mathcal{X}[f]$, which is solved in the algebra; the sequence is then read off the table of elementary sequences. It is the discrete analogue of the Laplace-transform solution of a linear differential equation with constant coefficients.

**Example.** Let $u = e_1 + e_2$, so that $u^2 = -2e_0$, and let

$$
f_{n+2} = f_{n+1}(u - e_0) + f_nu, \qquad f_0 = e_0, \qquad f_1 = u .
$$

Transforming both sides and using the shifting rule, with $\tilde{Q}$ central,

$$
\tilde{Q}^2\bigl(\mathcal{X}[f] - e_0 - u\tilde{Q}^{-1}\bigr) = \tilde{Q}\bigl(\mathcal{X}[f] - e_0\bigr)(u - e_0) + \mathcal{X}[f]u,
$$

which, after $e_0u = u$ and $e_0^2 = e_0$, is the linear equation

$$
\mathcal{X}[f](\tilde{Q})\,(\tilde{Q}^2 + \tilde{Q} - \tilde{Q}u - u) = \tilde{Q}^2 + \tilde{Q} .
$$

The left factor is the product $(\tilde{Q} + e_0)(\tilde{Q} - u)$ of two commuting factors, and $\tilde{Q}^2 + \tilde{Q} = \tilde{Q}(\tilde{Q} + e_0)$, so

$$
\mathcal{X}[f](\tilde{Q}) = \tilde{Q}(\tilde{Q} - u)^{-1} = (e_0 - u\tilde{Q}^{-1})^{-1}.
$$

By the table this is the transform of the sequence $f_n = u^n$, which satisfies the recurrence because $u^{n+1}(u - e_0) + u^{n+1} = u^{n+2}$, and satisfies the initial values. The solution is

$$
f_n = (e_1 + e_2)^n, \qquad n \ge 0 .
$$

An inhomogeneous recurrence is treated in the same way: the transform of the known right-hand side is inserted, the resulting equation for $\mathcal{X}[f]$ is decomposed in powers of $\tilde{Q}^{-1}$, and each term is read off the table.

## The Commutative Alternative: The Reduced Biquaternion Transform

Everything in this article is the transform of $\mathbb{B}$, whose product is non-commutative and whose convolution theorem therefore fixes the kernel to one side. A commutative four-dimensional algebra has a discrete transform of its own, due to Pei, Chang and Ding, and it is the corpus's only worked instance of a discrete hypercomplex transform over a commutative algebra; it is recorded here because it is the case in which the phenomena of the previous sections disappear.

The algebra is $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C}$, the reduced biquaternion algebra of *List of Algebras by Dimension*, and the transform is the **discrete reduced biquaternion Fourier transform** (DRBFT). The paper distinguishes two kernel conventions: **type 1**, with two imaginary units, whose advantage is that the even-even, even-odd, odd-even and odd-odd components of a real signal separate in the frequency domain, and **type 2**, with one imaginary unit, chosen for its similarity to the ordinary complex transform. Both are implemented by the reduction of *Harmonic Analysis over Hypercomplex Systems*: the signal is split by the idempotents into two complex signals, and the transform is then a pair of complex two-dimensional transforms, so a DRBFT of either type costs two complex DFTs, the same count the quaternion Fourier transform costs. The convolution is implemented with six complex two-dimensional transforms, and one convolution in this algebra equals two conventional ones.

The convolution theorem is the sharpest contrast with the theorem of this article. The convolution here is commutative, the kernel needs no side convention, and the product in the frequency domain is the transform of the convolution whichever DRBFT type is used; the paper reports that for the quaternion transform the corresponding identity holds only in a restricted one-side form, which is consistent with the one-sided theorem proved above for $\mathbb{B}$ and with its loss of commutativity. Two consequences of the commutative product are the ones the paper emphasises: a cascade of linear time-invariant filters multiplies in the frequency domain exactly as in the complex case, whereas the paper reports the cascade of quaternion filters to be difficult to analyse; and the **correlation** is a special case of the convolution, so the convolution algorithms serve it, with the **phase-only correlation** obtained by normalising the phase in the frequency domain, the paper's discrete definition of which uses the binary exclusive-or operation.

The price is the vanishing-norm phenomenon of the previous section, which the commutative algebra has as well: the norm is the determinant, it vanishes on two ideals, and so the transform has no single magnitude to be stationary in. The applications are to colour. A colour image is represented in the brightness–hue–saturation space, and the correlation and phase-only correlation are used for colour template matching and colour-sensitive edge detection. The colour space is three-dimensional and the algebra four-dimensional, so the representation is not unique; the paper removes the redundancy with a **simplified polar form**, treated with the other polar forms of the family in *Biquaternion Polar Element Representation*.

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

The infinite-sequence analogue is the **biquaternion Z transform**, $\mathcal{X}[f](\tilde{Q}) = \sum_{n \ge 0} f_n\tilde{Q}^{-n}$, the discrete Laplace transform of a sequence. Its calculation rules are those of the complex Z transform, with the commutation hypotheses that the non-commutative product imposes, and its convergence is the place where the zero divisors enter a transform: the multiplicative real norm $r = \sqrt{\lvert N\rvert}$ vanishes on them, so the region $r(\tilde{Q}) > \sigma_f$ of the transform literature contains the true region of convergence and may contain divergent points, the standard idempotent $\tilde\Pi_1$ and its complement being the sharpest example. The transform solves linear recurrences with constant biquaternion coefficients by turning them into algebraic equations.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra, $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ |
| $f : \{0,\dots,N-1\} \to \mathbb{B}$ | Biquaternion-valued sequence |
| $F[u]$ | Discrete biquaternion Fourier transform of $f$, defined by $F[u] = \sum_n W_N(n,u)f[n]$ |
| $W_N(n,u) = \exp(-2\pi\rho nu/N)$ | Discrete Fourier kernel, placed on the left of $f$; $\overline{W_N(n,u)}$ gives the inverse transform |
| $\rho$ | Root of $-1$ in $\mathbb{B}$; the degenerate roots give the complex or quaternion transform, the non-trivial roots a genuinely biquaternionic one |
| $N$ | Number of samples, in the kernel $W_N$ |
| $N(\tilde{Q}) = \tilde{Q}\tilde{Q}^{\natural}$ | Biquaternion norm; not to be confused with the sample count $N$ |
| $\mathbf{Q} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3$ | Vector part of a biquaternion |
| $e^{\rho\theta} = \cos\theta\,e_0 + \sin\theta\,\rho$ | de Moivre formula, valid for every root $\rho$ of $-1$ |
| $\mathcal{X}[f](\tilde{Q}) = \sum_{n \ge 0} f_n\tilde{Q}^{-n}$ | Biquaternion Z transform of a sequence, the variable on the right of the sample |
| $\mathcal{Y}[f](\tilde{Q}) = \sum_{n \ge 0} \tilde{Q}^{-n}f_n$ | The Z transform with the variable on the left; $\overline{\mathcal{X}[f](\tilde{Q})} = \mathcal{Y}[\bar f](\bar{\tilde{Q}})$ |
| $\tilde{Q} \in \mathbb{B}^{\times}$ | The variable of the Z transform, a unit of the algebra |
| $r(\tilde{Q}) = \sqrt{\lvert N(\tilde{Q})\rvert}$ | The multiplicative real norm; a seminorm on $\mathbb{B}$, vanishing on the zero divisors |
| $\sigma_f$ | Radius of convergence of the Z transform, the geometric growth rate of $r(f_n)$ |

## Further Reading

- S. Said, N. Le Bihan, S. J. Sangwine, "Fast complexified quaternion Fourier transform", *IEEE Transactions on Signal Processing* **56** (2008) 1522–1531, for the definition and factorization of the biquaternion Fourier transform.
- S. J. Sangwine and T. A. Ell, "Complexification of the quaternion roots of $-1$", arXiv:math.RA/0506190 (2005), for the classification of the biquaternion roots of $-1$.
- S. J. Sangwine and D. Alfsmann, "Determination of the biquaternion divisors of zero, including the idempotents and nilpotents", arXiv:0812.1102 (2008), for the classification of the zero divisors.
- N. Le Bihan and J. Mars, "Singular value decomposition of quaternion matrices: a new tool for vector-sensor signal processing", *Signal Processing* **84** (2004) 1177–1199, for the quaternion signal processing background.
- T. A. Ell and S. J. Sangwine, "Hypercomplex Fourier transforms of color images", *IEEE Transactions on Image Processing* **16** (2007) 22–35, for the quaternion Fourier transform and its applications.
- W. R. Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original formulation of quaternions and biquaternions.
- W. Bi, Z.-F. Cai, and K. I. Kou, "Biquaternion Z transform", arXiv:2108.02975 (2021), for the biquaternion Z transform, its calculation rules and its table of elementary transforms, and the solution of biquaternion recurrence relations.

- Soo-Chang Pei, Ja-Han Chang and Jian-Jiun Ding, "Commutative reduced biquaternions and their Fourier transform for signal and image processing applications", *IEEE Transactions on Signal Processing* **52** (2004) 2012–2022, for the reduced biquaternion algebra — the commutative four-dimensional algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C}$, equivalently the double-complex, tessarine or commutative hypercomplex algebra — and for the discrete reduced biquaternion Fourier transform, its convolution and correlation theorems, its phase-only correlation and its colour-image applications.
