# __Complex Harmonic Analysis__

## Introduction

This article introduces harmonic analysis on the complex plane as the study of the Fourier transform, convolution, and the function spaces on which they act, with the complex structure playing an essential role. The goal is to define the core objects precisely, establish their basic properties, and describe the theorems that give the subject its shape.

The treatment is mathematically honest: every claim is either proved or stated as a definition. The complex plane is used both as the domain of the functions and as the coefficient field. The interaction between the additive structure of $\mathbb{C} \cong \mathbb{R}^2$ and the multiplicative structure of $\mathbb{C}$ as a field is the source of the phenomena that distinguish complex harmonic analysis from real harmonic analysis in $\mathbb{R}^2$.

## The Complex Plane as a Locally Compact Abelian Group

### Additive Structure

The complex plane $\mathbb{C}$ is a locally compact abelian group under addition, isomorphic to $\mathbb{R}^2$. Its **characters** are the continuous homomorphisms

$$
\chi_\xi(z) = e^{2\pi i \operatorname{Re}(\bar{\xi} z)}, \qquad \xi \in \mathbb{C}.
$$

Equivalently, writing $\xi = u + iv$ and $z = x + iy$,

$$
\chi_\xi(z) = e^{2\pi i (ux + vy)}.
$$

The dual group $\hat{\mathbb{C}}$ is isomorphic to $\mathbb{C}$ itself, and the pairing is

$$
\langle \xi, z \rangle = \operatorname{Re}(\bar{\xi} z) = ux + vy.
$$

So complex harmonic analysis is, at the level of the additive group, the same as Fourier analysis on $\mathbb{R}^2$. The complex structure enters through the identification of $\mathbb{C}$ with itself as a dual object, and through the interaction with multiplication.

### Multiplicative Structure

The multiplicative group $\mathbb{C}^\times = \mathbb{C} \setminus \{0\}$ is also a locally compact abelian group, isomorphic to $\mathbb{R}_{>0} \times \mathbb{S}^1$ via the polar decomposition

$$
z = r e^{i\theta}, \qquad r > 0, \; \theta \in \mathbb{R}/2\pi\mathbb{Z}.
$$

Its characters are

$$
\chi_{\tau, n}(z) = r^{i \tau} e^{i n \theta}, \qquad \tau \in \mathbb{R}, \; n \in \mathbb{Z}.
$$

This is the starting point of **multiplicative harmonic analysis** on $\mathbb{C}$, which is the Mellin transform in disguise.

## The Fourier Transform on $\mathbb{C}$

### Definition

The **Fourier transform** of $f \in L^1(\mathbb{C})$ is

$$
\hat{f}(\xi) = \int_{\mathbb{C}} f(z) e^{-2\pi i \operatorname{Re}(\bar{\xi} z)} \, dz,
$$

where $dz$ is Lebesgue measure on $\mathbb{C} \cong \mathbb{R}^2$. Writing $z = x + iy$ and $\xi = u + iv$,

$$
\hat{f}(u, v) = \int_{\mathbb{R}^2} f(x, y) e^{-2\pi i (ux + vy)} \, dx \, dy.
$$

This is the ordinary two-dimensional Fourier transform. The complex notation is a convenience; the content is the same.

### Basic Properties

**Linearity.** $\widehat{af + bg} = a \hat{f} + b \hat{g}$.

**Translation.** If $f_w(z) = f(z - w)$, then $\hat{f}_w(\xi) = e^{-2\pi i \operatorname{Re}(\bar{\xi} w)} \hat{f}(\xi)$.

**Modulation.** If $f_\xi(z) = e^{2\pi i \operatorname{Re}(\bar{\xi} z)} f(z)$, then $\hat{f}_\xi(\eta) = \hat{f}(\eta - \xi)$.

**Scaling.** If $f_\lambda(z) = f(\lambda z)$ for $\lambda \in \mathbb{C}^\times$, then

$$
\widehat{f_\lambda}(\xi) = \frac{1}{|\lambda|^2} \hat{f}\left(\frac{\xi}{\bar{\lambda}}\right),
$$

where $\xi/\bar{\lambda}$ is complex division.

**Rotation.** If $f_\theta(z) = f(e^{i\theta} z)$, then $\hat{f}_\theta(\xi) = \hat{f}(e^{i\theta} \xi)$. The Fourier transform commutes with rotations.

**Conjugation.** $\widehat{\bar{f}}(\xi) = \overline{\hat{f}(-\xi)}$.

### The Plancherel Theorem

**Theorem.** The Fourier transform extends uniquely to a unitary operator

$$
\mathcal{F} : L^2(\mathbb{C}) \to L^2(\mathbb{C}),
$$

with

$$
\|\hat{f}\|_2 = \|f\|_2, \qquad \langle \hat{f}, \hat{g} \rangle = \langle f, g \rangle.
$$

This is the Plancherel theorem for $\mathbb{R}^2$, written in complex notation.

### The Inversion Theorem

**Theorem.** If $f \in L^1(\mathbb{C})$ and $\hat{f} \in L^1(\mathbb{C})$, then

$$
f(z) = \int_{\mathbb{C}} \hat{f}(\xi) e^{2\pi i \operatorname{Re}(\bar{\xi} z)} \, d\xi
$$

for almost every $z$.

## Convolution

### Definition

The **convolution** of $f, g : \mathbb{C} \to \mathbb{C}$ is

$$
(f * g)(z) = \int_{\mathbb{C}} f(z - w) g(w) \, dw,
$$

whenever the integral converges. This is the convolution on the additive group $\mathbb{C} \cong \mathbb{R}^2$.

### Basic Properties

**Commutativity.** $f * g = g * f$.

**Associativity.** $(f * g) * h = f * (g * h)$.

**Young's inequality.** If $1/p + 1/q = 1/r + 1$ with $1 \leq p, q, r \leq \infty$, then

$$
\|f * g\|_r \leq \|f\|_p \|g\|_q.
$$

**Convolution theorem.** If $f, g \in L^1(\mathbb{C})$, then

$$
\widehat{f * g}(\xi) = \hat{f}(\xi) \hat{g}(\xi).
$$

The convolution is the additive convolution. There is also a **multiplicative convolution** on $\mathbb{C}^\times$, defined by

$$
(f \star g)(z) = \int_{\mathbb{C}^\times} f(z/w) g(w) \frac{dw}{|w|^2},
$$

whose Fourier transform is the Mellin transform.

## The Paley–Wiener Theorem

### Functions of Exponential Type

A holomorphic function $F : \mathbb{C} \to \mathbb{C}$ is of **exponential type** if there exist constants $A, B > 0$ such that

$$
|F(z)| \leq A e^{B |z|}, \qquad z \in \mathbb{C}.
$$

The **indicator function** of $F$ is

$$
h_F(\theta) = \limsup_{r \to \infty} \frac{\log |F(r e^{i\theta})|}{r}.
$$

### The Paley–Wiener Theorem

**Theorem (Paley–Wiener).** The Fourier transform is a bijection between

- compactly supported $L^2$ functions on $\mathbb{R}$, and
- entire functions of exponential type whose restriction to $\mathbb{R}$ is in $L^2$.

More precisely, if $f \in L^2(\mathbb{R})$ is supported in $[-B, B]$, then $\hat{f}$ extends to an entire function of exponential type at most $2\pi B$, and conversely.

**Complex version.** The same theorem holds with $\mathbb{R}$ replaced by $\mathbb{C}$ and compact support replaced by support in a compact subset of $\mathbb{C}$. The Fourier transform of a compactly supported function on $\mathbb{C}$ is an entire function of exponential type on $\mathbb{C}$.

### The Paley–Wiener–Schwartz Theorem

**Theorem (Paley–Wiener–Schwartz).** The Fourier transform is a bijection between

- compactly supported distributions on $\mathbb{C}$, and
- entire functions of exponential type on $\mathbb{C}$ satisfying a growth condition.

This theorem is the foundation of the theory of **hyperfunctions**, which are the analytic functionals of Sato.

## The Cauchy–Riemann Operator and Harmonic Analysis

### The Cauchy–Riemann Operator

The **Cauchy–Riemann operator** is

$$
\bar{\partial} = \frac{\partial}{\partial \bar{z}} = \frac{1}{2}\left( \frac{\partial}{\partial x} + i \frac{\partial}{\partial y} \right).
$$

A function $f$ is holomorphic iff $\bar{\partial} f = 0$. The **Laplacian** on $\mathbb{C}$ is

$$
\Delta = 4 \partial \bar{\partial} = \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2},
$$

where $\partial = \partial/\partial z$.

### The Fourier Transform and the Laplacian

The Fourier transform diagonalizes the Laplacian:

$$
\widehat{\Delta f}(\xi) = -4 \pi^2 |\xi|^2 \hat{f}(\xi).
$$

This is the algebraic content of the Fourier transform on $\mathbb{C}$: it turns differentiation into multiplication by the symbol $-4\pi^2 |\xi|^2$.

The Cauchy–Riemann operator has symbol

$$
\widehat{\bar{\partial} f}(\xi) = \pi i \xi \hat{f}(\xi),
$$

where $\bar{\xi}$ is the complex conjugate of $\xi$. The symbol vanishes on the set $\bar{\xi} = 0$, which is the origin. This is the reason the Cauchy–Riemann operator is elliptic: its symbol vanishes only at the origin.

### The Fundamental Solution of the Laplacian

The **fundamental solution** of the Laplacian on $\mathbb{C}$ is

$$
\Phi(z) = \frac{1}{2\pi} \log |z|.
$$

It satisfies

$$
\Delta \Phi = \delta_0
$$

in the sense of distributions. The Fourier transform of $\Phi$ is the tempered distribution

$$
\hat{\Phi}(\xi) = -\frac{1}{4\pi^2 |\xi|^2},
$$

which is defined by principal value.

### The Fundamental Solution of the Cauchy–Riemann Operator

The **fundamental solution** of the Cauchy–Riemann operator is

$$
\frac{1}{\pi z},
$$

which satisfies

$$
\bar{\partial}\left( \frac{1}{\pi z} \right) = \delta_0
$$

in the sense of distributions. This is the starting point of the theory of the **Bochner–Martinelli integral** and of the solution of the $\bar{\partial}$-equation.

## Holomorphic Functions and Harmonic Analysis

### The Hardy Spaces

The **Hardy space** $H^p(\mathbb{D})$ on the unit disk $\mathbb{D} = \{z : |z| < 1\}$ is the set of holomorphic functions $f$ on $\mathbb{D}$ with

$$
\|f\|_{H^p} = \sup_{0 < r < 1} \left( \frac{1}{2\pi} \int_0^{2\pi} |f(r e^{i\theta})|^p \, d\theta \right)^{1/p} < \infty
$$

for $1 \leq p < \infty$, and

$$
\|f\|_{H^\infty} = \sup_{z \in \mathbb{D}} |f(z)| < \infty
$$

for $p = \infty$.

**Theorem (Fatou).** Every $f \in H^p$ has a boundary value $f(e^{i\theta})$ for almost every $\theta$, and the boundary function is in $L^p(\mathbb{T})$.

**Theorem (F. and M. Riesz).** If $f \in H^1$ and its boundary function is real-valued, then $f$ is constant.

The Hardy spaces are the natural setting for the study of holomorphic functions with controlled growth, and they are connected to the Fourier series on the circle by the boundary value theorem.

### The Paley–Wiener Space

The **Paley–Wiener space** $PW_B$ is the set of entire functions of exponential type at most $2\pi B$ whose restriction to $\mathbb{R}$ is in $L^2$. By the Paley–Wiener theorem, it is the image of the compactly supported $L^2$ functions on $[-B, B]$ under the Fourier transform.

The Paley–Wiener space is a reproducing kernel Hilbert space, with reproducing kernel

$$
K_B(z, w) = \frac{\sin(2\pi B (z - \bar{w}))}{\pi (z - \bar{w})}.
$$

It is the natural setting for the sampling theorem of Shannon, which states that a function in $PW_B$ is determined by its values on the lattice $\mathbb{Z}/(2B)$.

### The Bergman Space

The **Bergman space** $A^p(\mathbb{D})$ is the set of holomorphic functions $f$ on $\mathbb{D}$ with

$$
\|f\|_{A^p} = \left( \int_{\mathbb{D}} |f(z)|^p \, dx \, dy \right)^{1/p} < \infty.
$$

For $p = 2$, the Bergman space is a reproducing kernel Hilbert space, with reproducing kernel

$$
K(z, w) = \frac{1}{\pi (1 - z \bar{w})^2}.
$$

It is the natural setting for the study of holomorphic functions with controlled $L^p$ growth on the disk.

### The Bloch Space

The **Bloch space** $\mathcal{B}$ is the set of holomorphic functions $f$ on $\mathbb{D}$ with

$$
\|f\|_{\mathcal{B}} = |f(0)| + \sup_{z \in \mathbb{D}} (1 - |z|^2) |f'(z)| < \infty.
$$

It is a Banach space, and it is the natural setting for the study of holomorphic functions with bounded mean oscillation of the derivative.

## The Mellin Transform

### Definition

The **Mellin transform** of a function $f : (0, \infty) \to \mathbb{C}$ is

$$
\mathcal{M} f(s) = \int_0^\infty x^{s-1} f(x) \, dx,
$$

whenever the integral converges. For $f \in L^1((0, \infty), x^{\sigma-1} dx)$, the transform converges for $\operatorname{Re} s = \sigma$ and defines a holomorphic function on a vertical strip.

### Relation to the Fourier Transform

Under the change of variables $x = e^t$, the Mellin transform becomes the Fourier transform:

$$
\mathcal{M} f(\sigma + i\tau) = \int_{-\infty}^\infty e^{(\sigma + i\tau) t} f(e^t) \, dt = \hat{g}(-\tau/2\pi),
$$

where $g(t) = e^{\sigma t} f(e^t)$. So the Mellin transform is the Fourier transform in logarithmic coordinates.

### The Mellin Convolution

The **Mellin convolution** is

$$
(f \star g)(x) = \int_0^\infty f(x/y) g(y) \frac{dy}{y}.
$$

It satisfies

$$
\mathcal{M}(f \star g)(s) = \mathcal{M} f(s) \, \mathcal{M} g(s),
$$

which is the multiplicative analogue of the convolution theorem.

### The Mellin Inversion

**Theorem.** If $f$ is continuous and $\mathcal{M} f$ is integrable on the line $\operatorname{Re} s = \sigma$, then

$$
f(x) = \frac{1}{2\pi i} \int_{\sigma - i\infty}^{\sigma + i\infty} \mathcal{M} f(s) x^{-s} \, ds.
$$

This is a contour integral along a vertical line in the complex plane, and it is evaluated by residues when $\mathcal{M} f$ is meromorphic.

## The Radon Transform

### Definition

The **Radon transform** of a function $f : \mathbb{R}^2 \to \mathbb{C}$ is

$$
Rf(\theta, t) = \int_{x \cos\theta + y \sin\theta = t} f(x, y) \, ds,
$$

where the integral is over the line with normal direction $(\cos\theta, \sin\theta)$ and signed distance $t$ from the origin.

### The Fourier Slice Theorem

**Theorem (Fourier Slice).** The one-dimensional Fourier transform of $Rf(\theta, \cdot)$ is the restriction of the two-dimensional Fourier transform of $f$ to the line through the origin in direction $(\cos\theta, \sin\theta)$:

$$
\widehat{Rf(\theta, \cdot)}(\sigma) = \hat{f}(\sigma \cos\theta, \sigma \sin\theta).
$$

**Proof.** Write the definition of the Radon transform, take the Fourier transform in $t$, and change variables. $\square$

The Fourier slice theorem is the mathematical basis of computed tomography: it says that the Radon transform can be inverted by taking Fourier transforms along lines, and this is what the filtered back-projection algorithm does.

### The Inversion Formula

**Theorem.** For suitable $f$,

$$
f(x, y) = \frac{1}{2} \int_0^{2\pi} \int_{-\infty}^\infty \widehat{Rf(\theta, \cdot)}(\sigma) |\sigma| e^{2\pi i \sigma (x \cos\theta + y \sin\theta)} \, d\sigma \, d\theta.
$$

The factor $|\sigma|$ is the **ramp filter**, and it is the source of the high-frequency amplification in tomography.

## The Wavelet Transform

### Definition

The **continuous wavelet transform** of $f \in L^2(\mathbb{R})$ with respect to a wavelet $\psi \in L^2(\mathbb{R})$ is

$$
W_\psi f(a, b) = \frac{1}{\sqrt{|a|}} \int_{\mathbb{R}} f(t) \overline{\psi\left( \frac{t - b}{a} \right)} \, dt, \qquad a \neq 0, \; b \in \mathbb{R}.
$$

The parameter $a$ is the **scale**, and $b$ is the **translation**. The wavelet $\psi$ is assumed to satisfy the **admissibility condition**

$$
C_\psi = \int_{\mathbb{R}} \frac{|\hat{\psi}(\xi)|^2}{|\xi|} \, d\xi < \infty.
$$

### The Inversion Formula

**Theorem.** If $\psi$ is admissible and $f \in L^2(\mathbb{R})$, then

$$
f(t) = \frac{1}{C_\psi} \int_{\mathbb{R}} \int_{\mathbb{R}} W_\psi f(a, b) \frac{1}{\sqrt{|a|}} \psi\left( \frac{t - b}{a} \right) \frac{da \, db}{a^2}.
$$

The inversion formula reconstructs $f$ from its wavelet transform.

### Relation to the Fourier Transform

The wavelet transform localizes in both frequency and position, unlike the Fourier transform, which localizes only in frequency. This is the source of its usefulness in signal processing and image analysis. The **uncertainty principle** states that no transform can localize perfectly in both, and the wavelet transform achieves the optimal trade-off.

### The Complex Wavelet Transform

In the complex setting, the wavelet $\psi$ is allowed to be complex-valued, and the transform becomes

$$
W_\psi f(a, b) = \frac{1}{\sqrt{|a|}} \int_{\mathbb{C}} f(z) \overline{\psi\left( \frac{z - b}{a} \right)} \, dz, \qquad a \in \mathbb{C}^\times, \; b \in \mathbb{C}.
$$

The complex wavelet transform is used in image processing, where it provides both magnitude and phase information, and in the analysis of oriented textures.

## Summary

Harmonic analysis on $\mathbb{C}$ is the study of the Fourier transform, of convolution, and of the function spaces on which the two act, with the complex structure playing an essential part. The plane is first a locally compact abelian group under addition, isomorphic to $\mathbb{R}^2$, and its characters $\chi_\xi(z) = e^{2\pi i \operatorname{Re}(\bar{\xi}z)}$ are the exponentials from which the transform is built.

The Fourier transform on $\mathbb{C}$ is the transform on that group, written in the complex variable, and convolution is the group convolution on $\mathbb{R}^2$. The Paley–Wiener theorem relates the decay of the transform to the holomorphic extension of the function. The article then takes up the interaction of the transform with holomorphy: the Cauchy–Riemann operator and the Laplacian, the Hardy spaces of holomorphic functions on the disc, and the theorems describing how harmonic analysis restricts to the holomorphic category.

The last three sections extend the transform beyond the group setting: the Mellin transform on the multiplicative half-line, the Radon transform of a function on $\mathbb{R}^2$ along lines, and the continuous wavelet transform. In each case the definition, the basic properties and the relation to the Fourier transform are recorded.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{C}$ | Complex plane |
| $\chi_\xi(z) = e^{2\pi i \operatorname{Re}(\bar{\xi} z)}$ | Character of $\mathbb{C}$ |
| $\hat{f}$ | Fourier transform |
| $f * g$ | Additive convolution |
| $f \star g$ | Multiplicative (Mellin) convolution |
| $\bar{\partial} = \partial/\partial \bar{z}$ | Cauchy–Riemann operator |
| $\Delta$ | Laplacian |
| $H^p(\mathbb{D})$ | Hardy space |
| $PW_B$ | Paley–Wiener space |
| $A^p(\mathbb{D})$ | Bergman space |
| $\mathcal{B}$ | Bloch space |
| $\mathcal{M} f$ | Mellin transform |
| $Rf$ | Radon transform |
| $W_\psi f$ | Wavelet transform |

## Further Reading

- Elias M. Stein and Guido Weiss, *Introduction to Fourier Analysis on Euclidean Spaces* (Princeton, 1971), for the classical treatment.
- Elias M. Stein, *Singular Integrals and Differentiability Properties of Functions* (Princeton, 1970), for the Calderón–Zygmund theory.
- Walter Rudin, *Real and Complex Analysis* (McGraw-Hill, 1987), for the interaction between real and complex methods.
- John B. Garnett, *Bounded Analytic Functions* (Academic Press, 1981), for the Hardy spaces and the Paley–Wiener theorem.
- Sigurdur Helgason, *The Radon Transform* (Birkhäuser, 1980), for the Radon transform and its applications.
- Ingrid Daubechies, *Ten Lectures on Wavelets* (SIAM, 1992), for the wavelet transform.

