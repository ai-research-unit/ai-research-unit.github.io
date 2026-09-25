# __Split-Biquaternion Discrete Harmonic Analysis__

## Introduction

This article introduces harmonic analysis for split-biquaternion-valued sequences. It follows the elementary functions article, which defined the split biquaternion exponential, and it uses the division theory articles, which characterized the zero divisors as the union of two four-dimensional linear subspaces $Z_+$ and $Z_-$.

The treatment is purely mathematical. The goal is to define the discrete split-biquaternion Fourier transform, establish its basic properties, show how it decomposes into ordinary complex Fourier transforms via the idempotent decomposition, and identify the points where the split biquaternion structure creates genuinely new phenomena. The continuous analogue is the subject of the companion article on split biquaternion continuous harmonic analysis.

The key structural fact is the **idempotent decomposition**: the split biquaternion algebra is the direct sum of two copies of the quaternion algebra, and the idempotents $e_\pm = \tfrac{1}{2}(1 \pm j)$ commute with everything. So every power-series function of a split biquaternion, including the Fourier kernel, decomposes into two copies of the corresponding quaternion function, one for each idempotent component. This is the fundamental simplification relative to the biquaternion case.

Unlike the biquaternion case, the split biquaternion Fourier kernel is **not** defined by the split complex unit $j$, which is the only scalar candidate in the algebra. The unit $j$ satisfies $j^2 = +1$, not $j^2 = -1$, so the exponential $e^{j\theta} = \cosh\theta + j\sinh\theta$ is hyperbolic, not trigonometric. The Fourier kernel in the split biquaternion case is therefore defined by an element whose square is $-1$ in each idempotent component, and the kernel is the pair of the quaternion Fourier kernels of the two components.

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

**Notation.** To avoid collision with the standard basis $\{e_0, e_1, e_2, e_3\}$ and with the split complex unit $j$, the root of $-1$ used in the Fourier kernel of each idempotent component is denoted $\rho$ throughout. This is a local convention; the roots themselves are the objects classified in the article on split biquaternion roots of minus one.

## The Fourier Kernel

### Definition

Fix a root $\rho$ of $-1$ in the quaternion algebra $\mathbb{H}$, i.e., an element $\rho \in \mathbb{H}$ with

$$
\rho^2 = -1.
$$

The roots of $-1$ in $\mathbb{H}$ are exactly the unit pure real quaternions, i.e., the elements of the form $\rho = \mu$ with $\mu \in \mathbb{R}^3_{\mathbb{H}}$ and $|\mu| = 1$.

The **split biquaternion Fourier kernel** of length $N$ is the function

$$
W_N(n, u) = \exp\left(-2\pi \rho \frac{nu}{N}\right), \qquad n, u \in \{0, 1, \ldots, N-1\},
$$

where the exponential is the split biquaternion exponential and $\rho$ is viewed as an element of $\mathbb{H}_{\mathbb{D}}$ via the embedding $\mathbb{H} \hookrightarrow \mathbb{H}_{\mathbb{D}}$.

In the idempotent basis, the kernel decomposes:

$$
W_N(n, u) = \exp\left(-2\pi \rho \frac{nu}{N}\right) e_+ + \exp\left(-2\pi \rho \frac{nu}{N}\right) e_-,
$$

because the same root $\rho$ is used in both components. The kernel is the same in each idempotent component, so the split biquaternion kernel is the diagonal embedding of the quaternion kernel.

Since $\rho^2 = -1$, the kernel takes the closed form

$$
W_N(n, u) = \cos\left(2\pi \frac{nu}{N}\right) e_0 - \sin\left(2\pi \frac{nu}{N}\right) \rho,
$$

where the cosine and sine are the ordinary real trigonometric functions applied to the real argument $2\pi nu/N$. The kernel is therefore a unit quaternion in the sense that its quaternion norm is $e_0$:

$$
N(W_N(n, u)) = \cos^2\left(2\pi \frac{nu}{N}\right) + \sin^2\left(2\pi \frac{nu}{N}\right) = 1.
$$

In particular, the kernel is always invertible, regardless of the choice of root and the values of $n, u$.

### The Condition on the Root

A quaternion $\rho$ satisfies $\rho^2 = -1$ if and only if it is a pure real quaternion of unit norm:

$$
\rho \in \mathbb{R}^3_{\mathbb{H}}, \qquad |\rho| = 1.
$$

So the roots of $-1$ in the quaternion algebra form the unit two-sphere $\mathbb{S}^2$ in the three-dimensional space of pure real quaternions.

The choice of root $\rho$ is not neutral, but the resulting transforms for different choices of $\rho$ are related by conjugation in the quaternion algebra. Specifically, if $\rho' = u \rho u^{-1}$ for some unit quaternion $u$, then the corresponding kernels are related by conjugation, and the transforms are equivalent up to a change of basis.

### The Choice of Root

The choice of the root $\rho$ determines the **axis** of the Fourier transform, i.e., the direction in the space of pure quaternions along which the transform decomposes the signal. Different choices of $\rho$ give different decompositions, and the transforms are related by conjugation.

There are three natural choices:

**$\rho = e_1$.** The kernel is the ordinary complex exponential in the $e_1$ direction, embedded in the quaternion algebra. The transform decomposes the signal into components along the $e_1$ axis.

**$\rho = e_2$.** Similarly, with the $e_2$ axis.

**$\rho = e_3$.** Similarly, with the $e_3$ axis.

The three choices are related by the quaternion multiplication, and they correspond to three different but equivalent decompositions of the signal.

### The Kernel in the Split Complex Subspace

If the signal takes values in the split complex subspace $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ (i.e., if all coefficients are split complex scalars), then the kernel acts on each coefficient separately. The kernel is the quaternion kernel $\cos\theta - \sin\theta \rho$, and it multiplies the split complex coefficients. Since the root $\rho$ is a real quaternion, it commutes with the split complex coefficients, and the transform reduces to the ordinary complex Fourier transform applied to each of the four complex coefficients (after splitting into real and split parts).

## The Discrete Transform Pair

### Definition

Let $f : \{0, 1, \ldots, N-1\} \to \mathbb{H}_{\mathbb{D}}$ be a split-biquaternion-valued sequence. The **discrete split-biquaternion Fourier transform** of $f$ is the sequence $F : \{0, 1, \ldots, N-1\} \to \mathbb{H}_{\mathbb{D}}$ defined by

$$
F[u] = \sum_{n=0}^{N-1} W_N(n, u) f[n], \qquad u \in \{0, 1, \ldots, N-1\},
$$

where $W_N(n, u)$ is the kernel defined above. The **inverse transform** is

$$
f[n] = \frac{1}{N} \sum_{u=0}^{N-1} W_N(n, u)^{-1} F[u], \qquad n \in \{0, 1, \ldots, N-1\}.
$$

Since the kernel is a unit quaternion, its inverse is its quaternion conjugate:

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

The two transforms are closely related: the conjugate of the left-kernel transform of $f$ equals the right-kernel transform of the conjugate of $f$, with a sign change in the kernel. (The outer conjugation is needed: $\overline{K_u[n] f[n]} = \overline{f[n]}\,\overline{K_u[n]}$.)

### Invertibility

The invertibility of the transform depends on the properties of the kernel and of the signal.

**The kernel has unit norm.** For every $n$ and $u$, the kernel $W_N(n, u)$ satisfies $N(W_N(n, u)) = e_0$, as shown above. So the kernel is always invertible.

**The signal may have vanishing norm.** A sample $f[n]$ with $N(f[n]) = 0$ is a zero divisor, and it is not necessarily recoverable from the transform. The zero divisor set is the union of the two four-dimensional linear subspaces $Z_+$ and $Z_-$, described in the article on split biquaternion zero divisors.

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

### Invertibility in the Idempotent Basis

The invertibility condition is cleaner in the idempotent basis. Writing $f[n] = f_+[n] e_+ + f_-[n] e_-$ with $f_\pm[n] \in \mathbb{H}$, the sample $f[n]$ is invertible if and only if both components $f_+[n]$ and $f_-[n]$ are nonzero. So the transform is invertible on a signal if and only if, for every $n$, both idempotent components of $f[n]$ are nonzero.

This is a **linear** condition in the idempotent basis, in contrast to the quadratic condition in the biquaternion case. The reason is that the split biquaternion algebra is semisimple, and the invertibility criterion is the pair of the invertibility criteria in the two quaternion components.

### Symmetry of the Spectrum

For a signal $f$ that takes values in the quaternion subspace $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ (i.e., all coefficients are real) and a root $\rho$, the spectrum satisfies a **conjugate symmetry** analogous to the Hermitian symmetry of the ordinary Fourier transform of a real signal.

**Theorem (conjugate symmetry).** Let $f : \{0, 1, \ldots, N-1\} \to \mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ be a real quaternion-valued signal, and let $F$ be its discrete split-biquaternion Fourier transform with respect to a root $\rho$. Then

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

The symmetry is the split biquaternion analogue of the Hermitian symmetry $F[-u] = F[u]^*$ of the ordinary Fourier transform of a real signal. It is the basis for reconstructing a real signal from half of its spectrum.

## Factorization into Complex Fourier Transforms

### The Idempotent Decomposition of the Transform

The transform decomposes in the idempotent basis. Writing $f[n] = f_+[n] e_+ + f_-[n] e_-$ and using the fact that the kernel is the same in both components,

$$
F[u] = \left(\sum_{n=0}^{N-1} W_N(n, u) f_+[n]\right) e_+ + \left(\sum_{n=0}^{N-1} W_N(n, u) f_-[n]\right) e_-.
$$

So the transform is the pair of the **quaternion Fourier transforms** of the two idempotent components:

$$
F[u] = F_+[u] e_+ + F_-[u] e_-,
$$

where $F_\pm[u] = \sum_{n=0}^{N-1} W_N(n, u) f_\pm[n]$ is the quaternion Fourier transform of the component $f_\pm$.

This is the fundamental simplification: the split biquaternion Fourier transform reduces to **two independent quaternion Fourier transforms**, one for each idempotent component. The transform is not a new operation; it is the quaternion Fourier transform applied to each of the two components separately.

### The Quaternion Fourier Transform

The quaternion Fourier transform of a quaternion-valued sequence $g : \{0, 1, \ldots, N-1\} \to \mathbb{H}$ is defined by

$$
G[u] = \sum_{n=0}^{N-1} W_N(n, u) g[n],
$$

where $W_N(n, u) = \exp(-2\pi \rho nu/N)$ and $\rho$ is a unit pure real quaternion.

The quaternion Fourier transform can be computed in several ways. The standard approach is to choose two other unit pure real quaternions $\nu$ and $\xi$ such that $\{\rho, \nu, \xi\}$ is an orthonormal basis of $\mathbb{R}^3_{\mathbb{H}}$, and to express $g[n]$ in the basis $\{e_0, \rho, \nu, \xi\}$:

$$
g[n] = g_0[n] e_0 + g_\rho[n] \rho + g_\nu[n] \nu + g_\xi[n] \xi, \qquad g_\bullet[n] \in \mathbb{C}.
$$

The quaternion Fourier transform then decomposes into **four complex Fourier transforms**, one for each complex coefficient, as discussed in the biquaternion discrete harmonic analysis article.

### The Full Factorization

Combining the idempotent decomposition with the quaternion Fourier transform factorization, the split biquaternion Fourier transform decomposes into **eight complex Fourier transforms**:

- Two idempotent components, each with four complex coefficients.

This is the total number of complex transforms required for a general split-biquaternion-valued signal.

If the signal takes values in a subspace with fewer complex components (for example, the quaternion subspace, where the coefficients are real), the number of complex transforms is reduced. Specifically:

- **Split complex subspace:** The signal has two real components per sample (real and split parts). The transform reduces to **two complex Fourier transforms** (one for each idempotent component, after splitting each component into real and imaginary parts, but since the components are real scalars, only two real Fourier transforms are needed).
- **Quaternion subspace:** The signal has four real components per sample. The transform reduces to **four complex Fourier transforms** (one for each component of the quaternion Fourier transform, but since the coefficients are real, the transforms are real Fourier transforms).
- **General split biquaternion:** The signal has eight real components per sample. The transform requires **eight complex Fourier transforms** (four per idempotent component).

### The Fast Algorithm

The factorization gives a fast algorithm for the discrete split-biquaternion Fourier transform:

1. **Idempotent decomposition.** Decompose each sample $f[n]$ into its two idempotent components $f_+[n]$ and $f_-[n]$.
2. **Quaternion Fourier transform.** Apply the quaternion Fourier transform to each component. This requires four complex Fourier transforms per component (for a general quaternion-valued sequence).
3. **Reassemble.** Combine the two transformed components into the split biquaternion spectrum $F[u] = F_+[u] e_+ + F_-[u] e_-$.

The cost is eight complex FFTs of size $N$, which is $O(N \log N)$, as opposed to the naive evaluation, which is $O(N^2)$.

If the signal takes values in the quaternion subspace, only four complex FFTs are needed. If it takes values in the split complex subspace, only two are needed.

### Why This Matters

The factorization is a computational result, but it also has a structural meaning. It shows that the split biquaternion Fourier transform is not a fundamentally new operation: it is the quaternion Fourier transform applied to the two idempotent components, dressed in split biquaternion language. The non-trivial content is the **choice of root** $\rho$ and the **idempotent decomposition**. Everything else is ordinary harmonic analysis.

## The Convolution Theorem

### Definition of Convolution

Let $f, g : \mathbb{Z} \to \mathbb{H}_{\mathbb{D}}$ be two split-biquaternion-valued sequences, extended to $\mathbb{Z}$ by $f[n] = g[n] = 0$ outside the support $\{0, 1, \ldots, N-1\}$. The **convolution** of $f$ and $g$ is

$$
(f * g)[n] = \sum_{m \in \mathbb{Z}} f[m] g[n - m].
$$

The convolution is **not commutative** in general, because the split biquaternion product is not commutative.

### The Convolution Theorem

**Theorem (convolution theorem).** Let $f, g$ be split-biquaternion-valued sequences with finite support, and let $\mathcal{F}$ denote the discrete split-biquaternion Fourier transform with the kernel on the left:

$$
\mathcal{F}[f][u] = \sum_{n=0}^{N-1} W_N(n, u) f[n].
$$

Then

$$
\mathcal{F}[f * g][u] = \mathcal{F}[f][u] \cdot \mathcal{F}[g][u],
$$

where the product on the right is the split biquaternion product.

**Proof.** Compute

$$
\mathcal{F}[f * g][u] = \sum_{n=0}^{N-1} W_N(n, u) \sum_{m=0}^{N-1} f[m] g[n-m] = \sum_{m=0}^{N-1} \sum_{n=0}^{N-1} W_N(n, u) f[m] g[n-m].
$$

Change variables $n = m + k$, so that $W_N(n, u) = W_N(m + k, u) = W_N(m, u) W_N(k, u)$. Then

$$
\mathcal{F}[f * g][u] = \sum_{m=0}^{N-1} \sum_{k=0}^{N-1} W_N(m, u) f[m] W_N(k, u) g[k] = \left(\sum_{m=0}^{N-1} W_N(m, u) f[m]\right) \left(\sum_{k=0}^{N-1} W_N(k, u) g[k]\right) = \mathcal{F}[f][u] \cdot \mathcal{F}[g][u].
$$

$\square$

**Corollary (right-kernel case).** For the transform with the kernel on the right,

$$
\mathcal{F}_{\text{right}}[f * g][u] = \mathcal{F}_{\text{right}}[g][u] \cdot \mathcal{F}_{\text{right}}[f][u].
$$

### Consequences

The convolution theorem implies that convolution in the signal domain becomes **split biquaternion multiplication** in the frequency domain. This is the basis for filtering.

It also implies that the convolution is:

- **Associative:** $(f * g) * h = f * (g * h)$.
- **Distributive over addition:** $f * (g + h) = f * g + f * h$.
- **Not commutative:** $f * g \neq g * f$ in general.

### The Convolution Theorem in the Idempotent Basis

In the idempotent basis, the convolution decomposes:

$$
(f * g)_+ = f_+ * g_+, \qquad (f * g)_- = f_- * g_-,
$$

where $*$ on the right is the quaternion convolution. So the split biquaternion convolution is the pair of the quaternion convolutions of the two idempotent components. This is the cleanest form of the convolution theorem, and it shows that the non-commutativity is inherited from the quaternion case in each component.

## The Vanishing-Norm Issue

### Samples of Vanishing Norm

A sample $f[n]$ with $N(f[n]) = 0$ is a zero divisor. Such samples have the property that they cannot necessarily be recovered from the transform.

In the idempotent basis, a sample $f[n] = f_+[n] e_+ + f_-[n] e_-$ has vanishing norm form if and only if $f_+[n] = 0$ or $f_-[n] = 0$. So the vanishing-norm samples are exactly the samples with a vanishing idempotent component.

### Consequences for the Transform

- **The transform is not necessarily invertible on signals containing zero-divisor samples.**
- **The transform is invertible on signals where both idempotent components of every sample are nonzero.**

The precise condition under which the transform is invertible on a signal with zero-divisor samples is not known; it depends on the cancellations in the sum.

### Structural Interpretation

The vanishing-norm issue is a genuinely split biquaternion feature. It does not arise in the quaternion Fourier transform, because the quaternion algebra is a division algebra. It arises in the biquaternion case as well, but the zero divisor structure is different: in the split biquaternion case, the zero divisor set is the union of two four-dimensional linear subspaces, while in the biquaternion case, it is a complex cone of complex dimension $3$ (real dimension $6$).

The issue can be avoided by restricting the signals to a subspace where the norm form is nonzero, such as the quaternion subspace $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$. On the quaternion subspace, every nonzero sample is invertible, and the transform is invertible on all signals.

## The Two-Dimensional Transform

### Definition

For a split-biquaternion-valued image $f : \{0, 1, \ldots, M-1\} \times \{0, 1, \ldots, N-1\} \to \mathbb{H}_{\mathbb{D}}$, the **two-dimensional discrete split-biquaternion Fourier transform** is

$$
F[u, v] = \sum_{m=0}^{M-1} \sum_{n=0}^{N-1} W_M(m, u) \, f[m, n] \, W_N(n, v),
$$

where $W_M$ and $W_N$ are the one-dimensional kernels of lengths $M$ and $N$, respectively.

### Factorization

The two-dimensional transform factorizes in the same way as the one-dimensional transform. In the idempotent basis, it reduces to two copies of the two-dimensional quaternion Fourier transform, one for each component. Each quaternion transform, in turn, factorizes into four two-dimensional complex transforms.

### Separability

The two-dimensional kernel is **separable**, because the exponential factorizes:

$$
W_{M \times N}((m, n), (u, v)) = W_M(m, u) \, W_N(n, v).
$$

This follows from the multiplicativity of the exponential. The separability is what allows the two-dimensional transform to be computed as a sequence of one-dimensional transforms.

## Higher-Dimensional Transforms

The generalization to higher dimensions is straightforward. The transform of a split-biquaternion-valued function on $\{0, 1, \ldots, N_1 - 1\} \times \cdots \times \{0, 1, \ldots, N_d - 1\}$ is defined by $d$ kernels, one for each dimension. The transform factorizes into the idempotent components, each of which is a quaternion transform, and each quaternion transform factorizes into four complex transforms.

The higher-dimensional transform is separable, and it can be computed by applying one-dimensional transforms along each dimension in turn.

## Open Questions

1. **Wavelets.** Can a split biquaternion wavelet transform be defined, and what are its properties? The wavelet kernel is more general than the Fourier kernel, and the split biquaternion structure may introduce new phenomena.

2. **Time-frequency analysis.** Can a split biquaternion time-frequency distribution (Wigner, spectrogram, etc.) be defined, and what are its properties?

3. **Non-commutative filtering.** What are the implications of the non-commutativity of the split biquaternion product for signal processing? Convolution is not commutative, and the standard filtering theory assumes commutativity.

4. **The spectrum and vanishing norms.** It is not known whether the spectrum of a split biquaternion Fourier transform of a signal in a subspace can have samples with vanishing norm. If it can occur, it would mean that the transform is not invertible on such signals.

5. **The precise invertibility condition.** Under what conditions on the zero-divisor samples is the transform invertible? The answer is not known.

6. **The relation to the continuous transform.** How does the discrete transform relate to the continuous transform of the companion article? The sampling and periodization theorems should be stated.

7. **The Clifford algebra framework.** How does the split biquaternion discrete Fourier transform fit into the general theory of Clifford algebra Fourier transforms?

8. **Comparison with the biquaternion case.** The split biquaternion transform reduces to two quaternion transforms, while the biquaternion transform reduces to four complex transforms. What are the advantages and disadvantages of each in applications?

## Summary

The discrete split-biquaternion Fourier transform is defined by the kernel $W_N(n, u) = \exp(-2\pi \rho nu/N)$, where $\rho$ is a unit pure real quaternion (a root of $-1$ in the quaternion algebra). The kernel is the same in both idempotent components, so the transform decomposes into two independent quaternion Fourier transforms, one for each component.

The transform is invertible on signals where both idempotent components of every sample are nonzero, and it satisfies the conjugate symmetry for real quaternion signals. It factorizes into eight complex Fourier transforms for a general split-biquaternion-valued signal, four for a quaternion-valued signal, and two for a split-complex-valued signal. The convolution theorem holds, with the non-commutativity inherited from the quaternion case.

The vanishing-norm issue is a genuinely split biquaternion feature: signals containing zero-divisor samples (i.e., samples with a vanishing idempotent component) are not necessarily recoverable from their transform, and the precise invertibility condition is not known.

The key simplification relative to the biquaternion case is the **idempotent decomposition**: the split biquaternion algebra is the direct sum of two copies of the quaternion algebra, so the split biquaternion Fourier transform reduces to two quaternion Fourier transforms. The split complex unit $j$ does not appear in the kernel; it only appears in the idempotent decomposition that separates the two components.

The discrete transform is the discrete analogue of the continuous transform of the companion article, and it is the basis for the split biquaternion signal processing applications.

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original formulation of quaternions.
- S. Said, N. Le Bihan, S. J. Sangwine, "Fast complexified quaternion Fourier transform", *IEEE Transactions on Signal Processing* **56** (2008) 1522–1531, for the definition and factorization of the biquaternion Fourier transform, which is closely related.
- S. J. Sangwine and T. A. Ell, "Complexification of the quaternion roots of $-1$", arXiv:math.RA/0506190 (2005), for the classification of the biquaternion roots of $-1$, which provides background for the quaternion roots.
- S. J. Sangwine and D. Alfsmann, "Determination of the biquaternion divisors of zero, including the idempotents and nilpotents", arXiv:0812.1102 (2008), for the classification of the zero divisors, which provides background for the split biquaternion zero divisors.
- N. Le Bihan and J. Mars, "Singular value decomposition of quaternion matrices: a new tool for vector-sensor signal processing", *Signal Processing* **84** (2004) 1177–1199, for the quaternion signal processing background.
- T. A. Ell and S. J. Sangwine, "Hypercomplex Fourier transforms of color images", *IEEE Transactions on Image Processing* **16** (2007) 22–35, for the quaternion Fourier transform and its applications.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the algebraic structure of the split biquaternions.

