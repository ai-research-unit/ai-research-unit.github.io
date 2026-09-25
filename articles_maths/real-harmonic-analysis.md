# __Real Harmonic Analysis__

## Introduction

This article introduces harmonic analysis on the real line and on Euclidean space as the study of the Fourier transform, convolution, and the function spaces on which they act. The goal is to define the core objects precisely, establish their basic properties, and describe the theorems that give the subject its shape.

The treatment is mathematically honest: every claim is either proved or stated as a definition. Only the real analysis of the companion article is assumed; Lebesgue measure and integration are used throughout, and no complex analysis and no abstract topology are invoked. The Fourier transform is normalized so that the factor $2\pi$ sits in the exponent and no prefactor appears in either the transform or its inverse:

$$
\hat{f}(\xi) = \int_{\mathbb{R}} f(x) e^{-2\pi i \xi x} \, dx.
$$

With this normalization the transform is an isometry of $L^2$ and the inversion and Plancherel theorems carry no constants. The real line is treated first, and the definitions are then extended verbatim to $\mathbb{R}^n$ with the pairing $\xi \cdot x$ in place of the product $\xi x$.

## Fourier Series on the Circle

### Definition

Let $\mathbb{T} = \mathbb{R}/\mathbb{Z}$, identified with $[0, 1]$ with endpoints joined. For $f \in L^1(\mathbb{T})$ the **Fourier coefficients** are

$$
\hat{f}(n) = \int_0^1 f(x) e^{-2\pi i n x} \, dx, \qquad n \in \mathbb{Z},
$$

and the **partial sums** are $S_N f(x) = \sum_{n=-N}^{N} \hat{f}(n) e^{2\pi i n x}$.

### The Dirichlet and Fejér Kernels

Writing the partial sum as a convolution,

$$
S_N f(x) = (f * D_N)(x), \qquad D_N(x) = \sum_{n=-N}^{N} e^{2\pi i n x} = \frac{\sin((2N+1)\pi x)}{\sin(\pi x)},
$$

where $D_N$ is the **Dirichlet kernel**. The **Fejér kernel** is the Cesàro average $F_N = \frac{1}{N+1} \sum_{k=0}^{N} D_k$, explicitly

$$
F_N(x) = \frac{1}{N+1} \left( \frac{\sin((N+1)\pi x)}{\sin(\pi x)} \right)^{\!2},
$$

and the Cesàro means are $\sigma_N f = f * F_N$.

**Theorem (Fejér).** If $f : \mathbb{T} \to \mathbb{C}$ is continuous, then $\sigma_N f \to f$ uniformly on $\mathbb{T}$. If $f \in L^p(\mathbb{T})$ for $1 \le p < \infty$, then $\sigma_N f \to f$ in $L^p(\mathbb{T})$.

The Fejér kernel is non-negative, has integral $1$, and concentrates at the origin, which is why the Cesàro means behave better than the partial sums.

### Orthogonality, Plancherel, and Riemann–Lebesgue

The functions $e_n(x) = e^{2\pi i n x}$ form an orthonormal basis of $L^2(\mathbb{T})$: $\int_0^1 e_m \overline{e_n} = \delta_{mn}$.

**Theorem (Plancherel, circle).** For $f \in L^2(\mathbb{T})$,

$$
\sum_{n \in \mathbb{Z}} |\hat{f}(n)|^2 = \int_0^1 |f(x)|^2 \, dx,
$$

and $f \mapsto (\hat{f}(n))$ is a unitary isomorphism $L^2(\mathbb{T}) \to \ell^2(\mathbb{Z})$. Consequently, for $f, g \in L^2(\mathbb{T})$,

$$
\sum_{n \in \mathbb{Z}} \hat{f}(n) \overline{\hat{g}(n)} = \int_0^1 f(x) \overline{g(x)} \, dx.
$$

**Theorem (Riemann–Lebesgue).** If $f \in L^1(\mathbb{T})$, then $\hat{f}(n) \to 0$ as $|n| \to \infty$. The trigonometric polynomials are dense in $L^p(\mathbb{T})$ for $1 \le p < \infty$.

## The Fourier Transform on the Line

### Definition

For $f \in L^1(\mathbb{R})$ the **Fourier transform** is

$$
\hat{f}(\xi) = \int_{\mathbb{R}} f(x) e^{-2\pi i \xi x} \, dx.
$$

The integral converges absolutely and $\|\hat{f}\|_\infty \le \|f\|_1$.

### Basic Properties

**Linearity.** $\widehat{af + bg} = a \hat{f} + b \hat{g}$.

**Translation.** If $f_a(x) = f(x - a)$, then $\hat{f}_a(\xi) = e^{-2\pi i \xi a} \hat{f}(\xi)$.

**Modulation.** If $g(x) = e^{2\pi i \eta x} f(x)$, then $\hat{g}(\xi) = \hat{f}(\xi - \eta)$.

**Scaling.** If $f_\lambda(x) = f(\lambda x)$ for $\lambda \neq 0$, then $\widehat{f_\lambda}(\xi) = |\lambda|^{-1} \hat{f}(\xi/\lambda)$.

**Conjugation.** $\widehat{\bar{f}}(\xi) = \overline{\hat{f}(-\xi)}$.

**Differentiation.** If $f$ is absolutely continuous with $f' \in L^1(\mathbb{R})$, then $\widehat{f'}(\xi) = 2\pi i \xi \, \hat{f}(\xi)$.

**Multiplication by the variable.** If $f \in L^1(\mathbb{R})$ and $x f(x) \in L^1(\mathbb{R})$, then $\hat{f}$ is differentiable and $\widehat{x f}(\xi) = \frac{i}{2\pi} \frac{d}{d\xi} \hat{f}(\xi)$.

**Theorem (Riemann–Lebesgue).** If $f \in L^1(\mathbb{R})$, then $\hat{f} \in C_0(\mathbb{R})$ and $\|\hat{f}\|_\infty \le \|f\|_1$. The transform of an interval indicator is computed explicitly; the span of step functions is dense in $L^1$, and $C_0(\mathbb{R})$ is closed.

## The Inversion Theorem and the Plancherel Theorem

### The Inversion Theorem

**Theorem (Inversion).** If $f \in L^1(\mathbb{R})$ and $\hat{f} \in L^1(\mathbb{R})$, then

$$
f(x) = \int_{\mathbb{R}} \hat{f}(\xi) e^{2\pi i \xi x} \, d\xi
$$

for almost every $x$, and for every $x$ if $f$ is continuous.

**Proof.** For $\epsilon > 0$ define $f_\epsilon(x) = \int \hat{f}(\xi) e^{-\pi \epsilon^2 \xi^2} e^{2\pi i \xi x} d\xi$. Since $\hat{f} \in L^1$, convolution with the Gaussian $G_\epsilon(x) = \epsilon^{-1} e^{-\pi x^2/\epsilon^2}$ gives $f_\epsilon = f * G_\epsilon$. As $(G_\epsilon)$ is an approximate identity, $f_\epsilon \to f$ in $L^1$ and at Lebesgue points, while dominated convergence gives $f_\epsilon(x) \to \int \hat{f}(\xi) e^{2\pi i \xi x} d\xi$ at every $x$. $\square$

### The Plancherel Theorem

**Theorem (Plancherel).** The Fourier transform on $L^1(\mathbb{R}) \cap L^2(\mathbb{R})$ satisfies $\|\hat{f}\|_2 = \|f\|_2$ and $\langle \hat{f}, \hat{g} \rangle = \langle f, g \rangle$, and extends uniquely to a unitary operator

$$
\mathcal{F} : L^2(\mathbb{R}) \to L^2(\mathbb{R}).
$$

**Proof.** For $f \in L^1 \cap L^2$, put $\tilde{f}(x) = \overline{f(-x)}$. Then $\widehat{f * \tilde{f}} = |\hat{f}|^2$, so inversion at $0$ gives $\int |\hat{f}|^2 = (f * \tilde{f})(0) = \int |f|^2$; polarization gives the inner-product identity. Since $L^1 \cap L^2$ is dense and $\mathcal{F}$ is an isometry there, it extends uniquely to an isometry of $L^2$ whose range is closed and dense. $\square$

For $f \in L^2(\mathbb{R})$ the transform is the $L^2$ limit of the truncated integrals, and $\mathcal{F}^2 f(x) = f(-x)$, $\mathcal{F}^{-1} = \mathcal{F}^3$, $\mathcal{F}^4 = \mathrm{Id}$.

## The Fourier Transform on $\mathbb{R}^n$

### Definition

For $f \in L^1(\mathbb{R}^n)$ the **Fourier transform** is

$$
\hat{f}(\xi) = \int_{\mathbb{R}^n} f(x) e^{-2\pi i \xi \cdot x} \, dx, \qquad \xi \cdot x = \sum_{j=1}^{n} \xi_j x_j.
$$

### Basic Properties

**Translation.** If $f_a(x) = f(x - a)$, then $\hat{f}_a(\xi) = e^{-2\pi i \xi \cdot a} \hat{f}(\xi)$.

**Modulation.** If $g(x) = e^{2\pi i \eta \cdot x} f(x)$, then $\hat{g}(\xi) = \hat{f}(\xi - \eta)$.

**Scaling.** If $f_\lambda(x) = f(\lambda x)$ for $\lambda > 0$, then $\widehat{f_\lambda}(\xi) = \lambda^{-n} \hat{f}(\xi/\lambda)$.

**Rotation invariance.** If $R$ is orthogonal and $f_R(x) = f(Rx)$, then $\hat{f}_R(\xi) = \hat{f}(R\xi)$; the transform commutes with rotations.

**Differentiation.** For a multi-index $\alpha$, $\widehat{\partial^\alpha f}(\xi) = (2\pi i)^{|\alpha|} \xi^\alpha \hat{f}(\xi)$ whenever the derivatives lie in $L^1$. In particular the Laplacian has symbol $-4\pi^2 |\xi|^2$:

$$
\widehat{\Delta f}(\xi) = -4\pi^2 |\xi|^2 \hat{f}(\xi).
$$

### Inversion and Plancherel on $\mathbb{R}^n$

**Theorem (Inversion).** If $f \in L^1(\mathbb{R}^n)$ and $\hat{f} \in L^1(\mathbb{R}^n)$, then $f(x) = \int_{\mathbb{R}^n} \hat{f}(\xi) e^{2\pi i \xi \cdot x} d\xi$ for almost every $x$, and everywhere if $f$ is continuous.

**Theorem (Plancherel).** The Fourier transform extends uniquely to a unitary operator $\mathcal{F} : L^2(\mathbb{R}^n) \to L^2(\mathbb{R}^n)$, and for all $f, g \in L^2(\mathbb{R}^n)$,

$$
\|\hat{f}\|_2 = \|f\|_2, \qquad \langle \hat{f}, \hat{g} \rangle = \langle f, g \rangle.
$$

**Theorem (Riemann–Lebesgue).** If $f \in L^1(\mathbb{R}^n)$, then $\hat{f} \in C_0(\mathbb{R}^n)$ and $\|\hat{f}\|_\infty \le \|f\|_1$.

## Convolution

### Definition and Basic Properties

The **convolution** of measurable $f, g : \mathbb{R}^n \to \mathbb{C}$ is

$$
(f * g)(x) = \int_{\mathbb{R}^n} f(x - y) g(y) \, dy,
$$

defined whenever the integral converges for almost every $x$. Convolution is commutative, associative, bilinear, and translation invariant: $(\tau_a f) * g = \tau_a (f * g)$ for $\tau_a f(x) = f(x - a)$.

**Young's inequality.** If $1 \le p, q, r \le \infty$ and $\frac{1}{p} + \frac{1}{q} = \frac{1}{r} + 1$, then

$$
\|f * g\|_r \le \|f\|_p \, \|g\|_q.
$$

In particular $\|f * g\|_1 \le \|f\|_1 \|g\|_1$ and $\|f * g\|_p \le \|f\|_1 \|g\|_p$.

**Continuity.** If $f \in L^p$ and $g \in L^1$ with $1 \le p < \infty$, then $f * g \in L^p$ and $\|f * g\|_p \le \|f\|_p \|g\|_1$. If $f \in L^\infty$ and $g \in L^1$, then $f * g$ is bounded and uniformly continuous, with $\|f * g\|_\infty \le \|f\|_\infty \|g\|_1$.

### The Convolution Theorem

**Theorem.** If $f, g \in L^1(\mathbb{R}^n)$, then $f * g \in L^1(\mathbb{R}^n)$ and

$$
\widehat{f * g}(\xi) = \hat{f}(\xi) \hat{g}(\xi).
$$

**Proof.** By Fubini, $\widehat{f * g}(\xi) = \int g(y) e^{-2\pi i \xi \cdot y} \big( \int f(x - y) e^{-2\pi i \xi \cdot (x - y)} dx \big) dy$, and the inner integral is $\hat{f}(\xi)$. $\square$

The theorem extends to $L^2$ and to tempered distributions in the sense described below.

## Approximate Identities

### Definition

A family $(\phi_\epsilon)_{\epsilon > 0}$ in $L^1(\mathbb{R}^n)$ is an **approximate identity** if $\int \phi_\epsilon = 1$, $\sup_\epsilon \|\phi_\epsilon\|_1 < \infty$, and for every $\delta > 0$,

$$
\int_{|x| > \delta} |\phi_\epsilon(x)| \, dx \to 0 \qquad (\epsilon \to 0).
$$

The last condition says that the mass of $\phi_\epsilon$ concentrates near the origin.

**Theorem.** If $(\phi_\epsilon)$ is an approximate identity and $f \in L^p(\mathbb{R}^n)$ with $1 \le p < \infty$, then $\|f * \phi_\epsilon - f\|_p \to 0$. If $f \in L^\infty$ is uniformly continuous, then $f * \phi_\epsilon \to f$ uniformly. If $x$ is a Lebesgue point of $f \in L^p$, then $(f * \phi_\epsilon)(x) \to f(x)$.

## The Schwartz Space and Tempered Distributions

### The Schwartz Space

The **Schwartz space** $\mathcal{S}(\mathbb{R}^n)$ is the set of smooth $\phi$ with $\|\phi\|_{\alpha, \beta} = \sup_x |x^\alpha \partial^\beta \phi(x)| < \infty$ for all multi-indices $\alpha, \beta$. The seminorms $\|\cdot\|_{\alpha, \beta}$ make $\mathcal{S}(\mathbb{R}^n)$ a Fréchet space, closed under differentiation and multiplication by polynomials.

**Theorem.** The Fourier transform is a bijection $\mathcal{F} : \mathcal{S}(\mathbb{R}^n) \to \mathcal{S}(\mathbb{R}^n)$. Indeed $\widehat{\partial^\alpha \phi} = (2\pi i)^{|\alpha|} \xi^\alpha \hat{\phi}$ and $\widehat{x^\alpha \phi} = (-2\pi i)^{-|\alpha|} \partial^\alpha \hat{\phi}$, so the seminorms of $\hat{\phi}$ are controlled by those of $\phi$ and conversely. The inversion formula and Plancherel's identity hold on $\mathcal{S}(\mathbb{R}^n)$ with no further hypotheses.

### Tempered Distributions

A **tempered distribution** is a continuous linear functional on $\mathcal{S}(\mathbb{R}^n)$; the space is denoted $\mathcal{S}'(\mathbb{R}^n)$ and contains $L^p(\mathbb{R}^n)$ for $1 \le p \le \infty$, all finite measures, and all polynomials. The operations are defined by duality:

- **Differentiation:** $\langle \partial^\alpha T, \phi \rangle = (-1)^{|\alpha|} \langle T, \partial^\alpha \phi \rangle$.
- **Multiplication:** for $f$ smooth of polynomial growth, $\langle f T, \phi \rangle = \langle T, f \phi \rangle$.
- **Fourier transform:** $\langle \hat{T}, \phi \rangle = \langle T, \hat{\phi} \rangle$.

These extend the classical operations, and the Fourier transform is a bijection $\mathcal{S}'(\mathbb{R}^n) \to \mathcal{S}'(\mathbb{R}^n)$.

**Examples.** The delta distribution $\langle \delta, \phi \rangle = \phi(0)$ has $\hat{\delta} = 1$ and $\hat{1} = \delta$. The principal value $\mathrm{p.v.}(1/x)$ has Fourier transform $-i\pi \, \mathrm{sgn}(\xi)$. For $0 < \alpha < n$, the transform of $|x|^{-\alpha}$ is a constant multiple of $|\xi|^{\alpha - n}$.

## The Hardy–Littlewood Maximal Function

### Definition and the Maximal Inequality

For $f \in L^1_{\mathrm{loc}}(\mathbb{R}^n)$ the **Hardy–Littlewood maximal function** is

$$
Mf(x) = \sup_{r > 0} \frac{1}{|B(x, r)|} \int_{B(x, r)} |f(y)| \, dy.
$$

**Theorem (Hardy–Littlewood).** There is a dimensional constant $C_n$ such that for every $f \in L^1(\mathbb{R}^n)$ and every $\lambda > 0$,

$$
|\{x : Mf(x) > \lambda\}| \le \frac{C_n}{\lambda} \|f\|_1.
$$

**Proof.** For each $x$ with $Mf(x) > \lambda$ choose a ball $B(x, r_x)$ with average exceeding $\lambda$. These balls cover the level set; a Vitali covering argument extracts a disjoint subcollection $B_j$ whose $3$-fold dilates cover it. Hence $|\{Mf > \lambda\}| \le 3^n \sum_j |B_j| \le 3^n \lambda^{-1} \|f\|_1$. $\square$

**Theorem.** For $1 < p \le \infty$ there is $C_{n,p}$ with $\|Mf\|_p \le C_{n,p} \|f\|_p$.

The case $p = \infty$ is immediate; the case $1 < p < \infty$ follows from the weak $(1,1)$ estimate and the $L^\infty$ estimate by interpolation. The operator $M$ is not bounded on $L^1$: for $f = \mathbf{1}_{[0,1]}$ on $\mathbb{R}$ one has $Mf(x) \gtrsim 1/x$ for large $x$, and $1/x \notin L^1$.

### The Lebesgue Differentiation Theorem

**Theorem (Lebesgue).** If $f \in L^1_{\mathrm{loc}}(\mathbb{R}^n)$, then

$$
\lim_{r \to 0} \frac{1}{|B(x, r)|} \int_{B(x, r)} f(y) \, dy = f(x)
$$

for almost every $x$.

**Proof.** It suffices to prove the statement for $f \in L^1$. For $\epsilon > 0$ write $f = g + h$ with $g$ continuous and $\|h\|_1 < \epsilon$. For $g$ the statement holds at every point, while the maximal inequality bounds the measure of the set where the oscillation of the averages of $h$ exceeds $\lambda$ by $C_n \|h\|_1/\lambda$. Letting $\epsilon \to 0$ gives the result. $\square$

A point where the conclusion holds is a **Lebesgue point** of $f$. The maximal function gives the quantitative form of the theorem.

## The Hilbert Transform

### Definition

The **Hilbert transform** of $f \in L^p(\mathbb{R})$, $1 \le p < \infty$, is the principal value integral

$$
Hf(x) = \frac{1}{\pi} \, \mathrm{p.v.} \int_{\mathbb{R}} \frac{f(x - t)}{t} \, dt
= \frac{1}{\pi} \lim_{\epsilon \to 0} \int_{|t| > \epsilon} \frac{f(x - t)}{t} \, dt.
$$

The singular integral converges almost everywhere for $f$ in $L^p$, $1 \le p < \infty$, and in $L^2$ it converges in norm.

### The Fourier Multiplier

**Theorem.** On $L^2(\mathbb{R})$ the Hilbert transform is given by the multiplier

$$
\widehat{Hf}(\xi) = -i \, \mathrm{sgn}(\xi) \, \hat{f}(\xi).
$$

**Proof.** Let $K_\epsilon(x) = \frac{1}{\pi x} \mathbf{1}_{|x| > \epsilon}$ and $H_\epsilon f = f * K_\epsilon$. A computation gives

$$
\hat{K}_\epsilon(\xi) = -i \, \mathrm{sgn}(\xi) \left( 1 - \frac{2}{\pi} \mathrm{Si}(2\pi |\xi| \epsilon) \right),
$$

where $\mathrm{Si}(t) = \int_0^t \frac{\sin s}{s} ds$ is the sine integral. These multipliers are bounded uniformly in $\epsilon$ and converge pointwise to $-i \, \mathrm{sgn}(\xi)$; Plancherel gives $\|H_\epsilon f\|_2 \le C \|f\|_2$, and the convolution theorem with dominated convergence identifies the limit on a dense subset of $L^2$. $\square$

### Basic Properties

**Isometry on $L^2$.** Since $|-i \, \mathrm{sgn}(\xi)| = 1$ for $\xi \neq 0$, Plancherel gives

$$
\|Hf\|_2 = \|f\|_2, \qquad H^2 = -I, \qquad H^* = -H,
$$

so $H$ is a skew-adjoint isometry of $L^2(\mathbb{R})$, the operator corresponding to the conjugate-function operator of Fourier series.

**Boundedness on $L^p$.** The Hilbert transform is bounded on $L^p(\mathbb{R})$ for every $1 < p < \infty$: there is $C_p$ with $\|Hf\|_p \le C_p \|f\|_p$ (the Riesz theorem for the conjugate function). It is not bounded on $L^1$ and not bounded on $L^\infty$.

**Weak $(1,1)$.** For $f \in L^1(\mathbb{R})$ there is $C$ with $|\{x : |Hf(x)| > \lambda\}| \le C \lambda^{-1} \|f\|_1$ (Kolmogorov). Together with the $L^2$ isometry this yields the $L^p$ bounds by interpolation. The truncated maximal Hilbert transform $H^* f = \sup_{\epsilon > 0} |H_\epsilon f|$ obeys the same weak $(1,1)$ and strong $L^p$ bounds.

## Interpolation and $L^p$ Theory

### The Riesz–Thorin Theorem

**Theorem (Riesz–Thorin).** Let $1 \le p_0, p_1, q_0, q_1 \le \infty$ and let $T$ be a linear operator bounded from $L^{p_0}$ to $L^{q_0}$ with norm $M_0$ and from $L^{p_1}$ to $L^{q_1}$ with norm $M_1$. For $0 < \theta < 1$ define

$$
\frac{1}{p} = \frac{1 - \theta}{p_0} + \frac{\theta}{p_1}, \qquad \frac{1}{q} = \frac{1 - \theta}{q_0} + \frac{\theta}{q_1}.
$$

Then $T$ is bounded from $L^p$ to $L^q$ with norm at most $M_0^{1 - \theta} M_1^{\theta}$.

The conclusion holds for sublinear operators as well, by the same three-lines argument applied to an analytic family $z \mapsto \langle T f_z, g_z \rangle$ built from $L^p$ functions with suitable complex exponents.

### The Hausdorff–Young Theorem

**Theorem (Hausdorff–Young).** Let $1 \le p \le 2$ and let $q$ be the conjugate exponent, $\frac{1}{p} + \frac{1}{q} = 1$. If $f \in L^p(\mathbb{R}^n)$, then $\hat{f} \in L^q(\mathbb{R}^n)$ and

$$
\|\hat{f}\|_q \le \|f\|_p.
$$

**Proof.** The transform is bounded $L^1 \to L^\infty$ with norm $1$ and $L^2 \to L^2$ with norm $1$ by Plancherel. Riesz–Thorin interpolation between $(p_0, q_0) = (1, \infty)$ and $(p_1, q_1) = (2, 2)$ gives the result. $\square$

The endpoints are sharp: at $p = 1$ the transform is bounded but need not be integrable, and at $p = 2$ it is an isometry. For $p > 2$ the inequality fails, because the Fourier transform of an $L^p$ function need not lie in $L^q$; the defining integral need not converge absolutely, so the transform is taken in the distributional sense.

### The Marcinkiewicz Interpolation Theorem

**Theorem (Marcinkiewicz).** Let $T$ be a sublinear operator of weak type $(p_0, p_0)$ and weak type $(p_1, p_1)$, where $1 \le p_0 < p_1 \le \infty$. Then $T$ is of strong type $(p, p)$ for every $p_0 < p < p_1$. This is the distribution-function form of interpolation; it produces the $L^p$ bounds for the Hilbert transform and the maximal function from their weak endpoint estimates.

## Littlewood–Paley Theory

### The Littlewood–Paley Decomposition

Choose $\psi \in \mathcal{S}(\mathbb{R}^n)$ whose Fourier transform is supported in the annulus $\{1/2 \le |\xi| \le 2\}$ and satisfies $\sum_{j \in \mathbb{Z}} \hat{\psi}(2^{-j} \xi) = 1$ for $\xi \neq 0$. Set $\widehat{\Delta_j f}(\xi) = \hat{\psi}(2^{-j} \xi) \hat{f}(\xi)$, so $\Delta_j f$ has frequency support in the annulus $2^{j-1} \le |\xi| \le 2^{j+1}$, and $f = \sum_j \Delta_j f$ for $f$ in a suitable space.

### The Square Function

The **Littlewood–Paley square function** of $f$ is

$$
S f(x) = \left( \sum_{j \in \mathbb{Z}} |\Delta_j f(x)|^2 \right)^{\!1/2}.
$$

**Theorem (Littlewood–Paley).** For $1 < p < \infty$ there are constants depending only on $n$, $p$, and $\psi$ such that

$$
c_{n,p} \|f\|_p \le \|S f\|_p \le C_{n,p} \|f\|_p.
$$

For $p = 2$ the two-sided bound follows from Plancherel: because at most finitely many annuli overlap at each frequency and their multipliers sum to $1$, the quantity $\sum_j |\hat{\psi}(2^{-j}\xi)|^2$ is bounded above and below on $\mathbb{R}^n \setminus \{0\}$.

### Bernstein Inequalities

**Theorem (Bernstein).** Suppose the Fourier transform of $f$ is supported in $\{|\xi| \le R\}$. Then for every multi-index $\alpha$ and all $1 \le p \le q \le \infty$,

$$
\|\partial^\alpha f\|_q \le C R^{|\alpha| + n(1/p - 1/q)} \|f\|_p,
$$

with $C$ independent of $R$ and $f$. Conversely, if the support lies in $\{R/2 \le |\xi| \le 2R\}$, then $\|\partial^\alpha f\|_p \ge c R^{|\alpha|} \|f\|_p$ for a constant $c > 0$ independent of $R$ and $f$.

These inequalities are the mechanism by which Littlewood–Paley theory converts frequency localization into size estimates; they underlie multiplier theorems and Sobolev embedding.

## Sobolev Spaces

### Definition

For an integer $k \ge 0$ and $1 \le p \le \infty$, the **Sobolev space** $W^{k,p}(\mathbb{R}^n)$ is the set of $f \in L^p(\mathbb{R}^n)$ whose distributional derivatives $\partial^\alpha f$ of order $|\alpha| \le k$ all lie in $L^p$, with

$$
\|f\|_{W^{k,p}} = \left( \sum_{|\alpha| \le k} \|\partial^\alpha f\|_p^p \right)^{\!1/p}
$$

for $p < \infty$, and the corresponding supremum for $p = \infty$.

### Characterization by the Fourier Transform

For $p = 2$ the Fourier transform gives a complete description. For real $s$, the **Sobolev space** $H^s(\mathbb{R}^n)$ is the set of tempered distributions $f$ with

$$
\|f\|_{H^s}^2 = \int_{\mathbb{R}^n} (1 + |\xi|^2)^s \, |\hat{f}(\xi)|^2 \, d\xi < \infty.
$$

**Theorem.** For every real $s$, $H^s(\mathbb{R}^n)$ is a Hilbert space under the inner product $\langle f, g \rangle_{H^s} = \int (1 + |\xi|^2)^s \hat{f}(\xi) \overline{\hat{g}(\xi)} d\xi$, and the Fourier transform is a unitary isomorphism onto $L^2(\mathbb{R}^n, (1 + |\xi|^2)^s d\xi)$. For $s = k$ a non-negative integer, $H^k(\mathbb{R}^n) = W^{k,2}(\mathbb{R}^n)$ with equivalent norms.

The **homogeneous** Sobolev space $\dot{H}^s$ uses the seminorm $\|f\|_{\dot{H}^s}^2 = \int |\xi|^{2s} |\hat{f}(\xi)|^2 d\xi$, and $\partial^\alpha : H^s \to H^{s - |\alpha|}$ is bounded for all real $s$.

### Sobolev Embedding

**Theorem (Sobolev embedding).** Let $k \ge 1$ and $1 \le p < \infty$. If $k < n/p$, then $W^{k,p}(\mathbb{R}^n) \subset L^q(\mathbb{R}^n)$ continuously for $\frac{1}{q} = \frac{1}{p} - \frac{k}{n}$. If $k = n/p$, then $W^{k,p}(\mathbb{R}^n) \subset L^q(\mathbb{R}^n)$ for every $p \le q < \infty$. If $k > n/p$, then $W^{k,p}(\mathbb{R}^n) \subset C^m(\mathbb{R}^n)$ for $m < k - n/p$, after modification on a null set.

**Theorem.** If $s > n/2$, then every class in $H^s(\mathbb{R}^n)$ has a representative in $C_0(\mathbb{R}^n)$, and $\|f\|_\infty \le C_{n,s} \|f\|_{H^s}$.

**Proof.** By Cauchy–Schwarz, $\int |\hat{f}| = \int (1 + |\xi|^2)^{-s/2} (1 + |\xi|^2)^{s/2} |\hat{f}| \le \big( \int (1 + |\xi|^2)^{-s} d\xi \big)^{1/2} \|f\|_{H^s}$, and the first factor is finite exactly when $2s > n$. $\square$

### The Riesz Potential

For $0 < \alpha < n$ the **Riesz potential** of order $\alpha$ is the operator $\widehat{I_\alpha f}(\xi) = |\xi|^{-\alpha} \hat{f}(\xi)$, the fractional integral $(-\Delta)^{-\alpha/2}$ up to a constant.

**Theorem (Hardy–Littlewood–Sobolev).** If $0 < \alpha < n$, $1 < p < q < \infty$, and $\frac{1}{q} = \frac{1}{p} - \frac{\alpha}{n}$, then $\|I_\alpha f\|_q \le C_{n, \alpha, p} \|f\|_p$.

The Riesz potential saturates the Sobolev embedding: it maps $L^p$ into $L^q$ in exactly the range dictated by a gain of $\alpha$ derivatives.

## The Uncertainty Principle

### The Heisenberg Inequality

**Theorem (Heisenberg).** Let $f \in L^2(\mathbb{R})$ with $\|f\|_2 = 1$, $x f \in L^2(\mathbb{R})$, and $\xi \hat{f} \in L^2(\mathbb{R})$. Then

$$
\left( \int_{\mathbb{R}} x^2 |f(x)|^2 \, dx \right)^{\!1/2}
\left( \int_{\mathbb{R}} \xi^2 |\hat{f}(\xi)|^2 \, d\xi \right)^{\!1/2}
\ge \frac{1}{4\pi}.
$$

Equivalently, for any centers $x_0, \xi_0 \in \mathbb{R}$ the same lower bound holds with $(x - x_0)^2$ and $(\xi - \xi_0)^2$.

**Proof.** By translation and modulation one may take $x_0 = \xi_0 = 0$. Integration by parts and Plancherel give

$$
1 = \int_{\mathbb{R}} |f|^2 = -\int_{\mathbb{R}} x \, \frac{d}{dx} |f|^2 \, dx \le 2 \int_{\mathbb{R}} |x| \, |f| \, |f'| \, dx
\le 2 \left( \int_{\mathbb{R}} x^2 |f|^2 \right)^{\!1/2} \left( \int_{\mathbb{R}} |f'|^2 \right)^{\!1/2},
$$

and $\|f'\|_2 = 2\pi \|\xi \hat{f}\|_2$ by Plancherel and the differentiation rule. $\square$

Equality holds if and only if $f(x) = c \, e^{-a x^2}$ for some $a > 0$ and $c \in \mathbb{C}$, so the Gaussian is the unique minimizer of the uncertainty product.

### Qualitative Forms

**Theorem.** There is no nonzero $f \in L^2(\mathbb{R})$ such that both $f$ and $\hat{f}$ are compactly supported.

**Proof.** If $f$ is compactly supported, then $\hat{f}(\xi) = \int f(x) e^{-2\pi i \xi x} dx$ extends to an entire function of the complex variable $\xi$; if $\hat{f}$ were also compactly supported, the identity theorem for holomorphic functions would force $\hat{f} \equiv 0$. $\square$

**Theorem (Amrein–Berthier–Benedicks).** If $f \in L^2(\mathbb{R})$ and both $f$ and $\hat{f}$ are supported on sets of finite Lebesgue measure, then $f = 0$.

These statements are the qualitative counterparts of the Heisenberg inequality: a function and its transform cannot both be concentrated, in the strong sense of compact or finite-measure support.

## Summary

Harmonic analysis on the real line and on Euclidean space is the study of the Fourier transform, of convolution, and of the function spaces on which the two act. It begins on the circle, where the Fourier coefficients of an $L^1$ function are defined and the Fourier series is developed, and passes to the line, where the Fourier transform $\hat{f}(\xi) = \int_{\mathbb{R}} f(x)e^{-2\pi i\xi x}\,dx$ and its inversion and Plancherel theorems are established, and then to $\mathbb{R}^n$.

Convolution and the approximate identities built from it form the second theme, together with the Schwartz space and its tempered distributions. The theory is then developed in the $L^p$ setting: the Hardy–Littlewood maximal function with its maximal inequality, the Hilbert transform as a principal value integral, and the interpolation results organised by the Riesz–Thorin theorem.

The remaining sections take up the finer structure of the subject: the Littlewood–Paley decomposition, the Sobolev spaces and their role in regularity, and the uncertainty principle in its Heisenberg form, which bounds a function and its transform simultaneously.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{T} = \mathbb{R}/\mathbb{Z}$ | Circle, identified with $[0, 1]$ |
| $\hat{f}(n)$ | Fourier coefficient on the circle |
| $D_N, F_N$ | Dirichlet, Fejér kernels |
| $\hat{f}(\xi) = \int f(x) e^{-2\pi i \xi \cdot x} dx$ | Fourier transform on $\mathbb{R}^n$ |
| $\mathcal{F}$ | Fourier transform operator |
| $f * g$ | Convolution |
| $\phi_\epsilon$ | Approximate identity |
| $\mathcal{S}(\mathbb{R}^n)$ | Schwartz space |
| $\mathcal{S}'(\mathbb{R}^n)$ | Tempered distributions |
| $\delta$ | delta distribution |
| $Mf$ | Hardy–Littlewood maximal function |
| $Hf$ | Hilbert transform |
| $R_j$ | Riesz transform |
| $S f$ | Littlewood–Paley square function |
| $\Delta_j$ | Littlewood–Paley frequency projection |
| $W^{k,p}(\mathbb{R}^n)$ | Sobolev space, integer order |
| $H^s(\mathbb{R}^n)$ | Sobolev space, real order |
| $I_\alpha$ | Riesz potential |

## Further Reading

- Antoni Zygmund, *Trigonometric Series* (Cambridge, 1959), for the classical theory of Fourier series.
- Yitzhak Katznelson, *An Introduction to Harmonic Analysis* (Dover, 1976), for Fourier series and the circle.
- Elias M. Stein and Guido Weiss, *Introduction to Fourier Analysis on Euclidean Spaces* (Princeton, 1971), for the classical Fourier transform on $\mathbb{R}^n$.
- Elias M. Stein, *Singular Integrals and Differentiability Properties of Functions* (Princeton, 1970), for the maximal function, the Hilbert transform, and Calderón–Zygmund theory.
- Elias M. Stein, *Harmonic Analysis: Real-Variable Methods, Orthogonality, and Oscillatory Integrals* (Princeton, 1993), for Littlewood–Paley theory and the square function.
- Loukas Grafakos, *Classical Fourier Analysis* and *Modern Fourier Analysis* (Springer, 2014), for a systematic modern account.
- Gerald B. Folland, *Real Analysis: Modern Techniques and Their Applications* (Wiley, 1999), for the maximal function and distribution theory.
- Robert A. Adams and John J. F. Fournier, *Sobolev Spaces* (Academic Press, 2003), for Sobolev embedding and the Riesz potential.
- Elias M. Stein and Rami Shakarchi, *Fourier Analysis: An Introduction* (Princeton, 2003), for the circle and the line together, including the uncertainty principle.
