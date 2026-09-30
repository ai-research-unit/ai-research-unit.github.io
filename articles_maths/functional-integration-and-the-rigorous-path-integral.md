
# __Functional Integration and the Rigorous Path Integral__

## Introduction

Functional integration is the integration of a functional over an infinite-dimensional space, and its first and most important instance is the integration of a functional of a path against the law of a stochastic process. The object that makes the definition possible is the **cylinder measure**: a finitely additive set function on the cylinder sets of a vector space, specified by a consistent family of finite-dimensional distributions. The first question of the theory is whether such an object is a measure at all — whether it is countably additive — and for a Gaussian cylinder measure the answer is decided by the covariance: on a Hilbert space the measure exists if and only if the covariance is trace class. The Wiener measure is the case in which this construction produces the law of Brownian motion, and the **Cameron–Martin theorem** identifies the translations under which that measure is quasi-invariant and those under which it is singular.

The second half of the article is the reading of the path integral in this language. The **Euclidean path integral**, the integral of $e^{-S_E}$ for the Euclidean action $S_E$, is a genuine integral against the Wiener measure, and the identity that makes it so is the **Feynman–Kac formula**, which represents the solution of the heat equation with a potential as an expectation. The **oscillatory path integral**, the integral of the factor $e^{iS}$, is not a measure: its would-be density has modulus one, no countably additive set function on the path space can carry such a density, and the object exists only as a limit of regularised or truncated oscillatory integrals, as the analytic continuation of the Euclidean integral, or as a distribution. That obstruction is a theorem of Cameron, and the article states it, supplies the finite-dimensional evidence for it, and describes the three constructions that replace the measure.

The place of the article is fixed by boundaries.

- The **measure theory** — the algebra of sets, the construction of measures, the product measures, the Radon–Nikodym theorem and the Fourier transform of a measure — is *Measure Theory and Integration* and *Measure-Theoretic Probability*; the Kolmogorov extension theorem used here is the one of the probability article. The **Hilbert space and the spectral theorem for self-adjoint operators** are *Banach and Hilbert Spaces* and *Unbounded Operators and Spectral Measures*.
- The **Brownian motion, the construction of its path measure, the Itô integral, the Girsanov theorem, the Feynman–Kac formula and the potential theory of the Laplacian** are *Brownian Motion and Stochastic Calculus*, where they are proved; this article re-uses them and develops the one object they leave largely unnamed, the integration over the path space itself. The **Gaussian measures that arise from stochastic equations and the cylindrical Wiener process** are *Stochastic Partial Differential Equations*. The **operator form of the time slicing** — the Lie–Trotter product formula and the convergence of the factorised semigroups — is *Semigroups and Evolution Equations*.
- The **oscillatory integrals and the stationary phase** are *Semiclassical Analysis* and *Microlocal Analysis*; the **Schwartz kernel and the Fourier transform of a distribution** are *Distributions and Fundamental Solutions*; the **Sobolev spaces and the embedding $H^1\subset C^{1/2}$** in one dimension are *Sobolev Spaces and Weak Solutions*. These are cited, not developed.
- The **physical formulation of the path integral** and the question of the measure in the biquaternionic framework belong to the physics corpus, in particular *The Path Integral in Biquaternionic Form* and *The Schrödinger Path Integral in Biquaternionic Form*. The mathematical object alone is treated here.

Throughout, $X$ is a real vector space with algebraic dual $X'$, $\mathcal{Z}(X)$ is its algebra of cylinder sets, and a cylinder measure is written $\mu$. The space $H$ is a real separable Hilbert space with inner product $\langle\cdot,\cdot\rangle$ linear in the second argument, orthonormal basis $(e_k)_{k\geq1}$, and $Q$ is a positive self-adjoint operator on $H$ with eigenvalues $(q_k)$. The path space is $C[0,1]$ with the supremum norm, the Wiener measure on it is $\mathbb{W}$, the canonical process is $x$, and the Brownian covariance kernel is $R(s,t)=\min(s,t)$. The Euclidean action is $S_E$, the potential is $V(t,x)$, and the sliced propagator is $K_n$ with the limit $K$.

## Cylinder Measures and the Extension Problem

### Cylinder Sets and Cylinder Measures

**Definition (cylinder set).** Let $X$ be a real vector space and $X'$ its algebraic dual. For $\varphi_1,\dots,\varphi_n\in X'$ and a Borel set $B\in\mathcal{B}(\mathbb{R}^n)$, the **cylinder set** is

$$
Z(\varphi_1,\dots,\varphi_n;B)=\{x\in X:(\varphi_1(x),\dots,\varphi_n(x))\in B\}.
$$

The cylinder sets form an algebra $\mathcal{Z}(X)$ — closed under finite unions, intersections and complements — and the **cylinder $\sigma$-algebra** is the $\sigma$-algebra that they generate. A set of the form $Z(\varphi;B)$ with a single functional is the simplest cylinder, the preimage of a Borel set of the line.

**Definition (cylinder measure).** A **cylinder measure** on $X$ is a finitely additive map $\mu:\mathcal{Z}(X)\to[0,1]$ with $\mu(X)=1$. The measure is **consistent** if it is compatible with the coordinate projections, that is,

$$
\mu\bigl(Z(\varphi_1,\dots,\varphi_n;\pi^{-1}B')\bigr)=\mu\bigl(Z(\varphi_1,\dots,\varphi_{n-1};B')\bigr)
$$

for every projection $\pi:\mathbb{R}^n\to\mathbb{R}^{n-1}$ onto the first $n-1$ coordinates. The measure is **$\sigma$-additive** if it is countably additive on the algebra $\mathcal{Z}(X)$.

A consistent family of finite-dimensional distributions always defines a cylinder measure, by the prescription $\mu(Z(\varphi_1,\dots,\varphi_n;B))=\mu_{\varphi_1,\dots,\varphi_n}(B)$; the consistency is exactly what makes the prescription well defined on a set that has several representations. Finite additivity is then automatic, because a finite union of cylinder sets can be refined to a disjoint union over a common finite set of functionals. What is *not* automatic is countable additivity, and the whole difficulty of the subject is concentrated there.

**Example (the Gaussian cylinder measure).** Let $Q$ be a positive self-adjoint operator on $H$ and let $\varphi_i=\langle u_i,\cdot\rangle$. The matrix $(Q_\varphi)_{ij}=\langle Qu_i,u_j\rangle$ is positive definite when the $u_i$ are linearly independent, and the prescription

$$
\mu\bigl(Z(\varphi_1,\dots,\varphi_n;B)\bigr)=\frac{1}{(2\pi)^{n/2}\sqrt{\det Q_\varphi}}\int_Be^{-\frac12\langle Q_\varphi^{-1}y,y\rangle}\,dy
$$

is a cylinder measure on $H$, the **Gaussian cylinder measure with covariance $Q$**. Its characteristic functional is $\widehat\mu(\xi)=\exp\bigl(-\tfrac12\langle Q\xi,\xi\rangle\bigr)$ for $\xi\in H'=H$, and this functional determines the cylinder measure uniquely.

### Kolmogorov Extension and Its Limit

**Theorem (Kolmogorov extension).** Let $T$ be an arbitrary index set and let $X=\mathbb{R}^T$ carry the cylinder $\sigma$-algebra, generated by the coordinate functionals. Every consistent family of inner-regular Borel probability measures on the finite products extends to a unique probability measure on $X$.

The theorem is stated for the product space and it is complete there; the passage from the cylinder algebra to the generated $\sigma$-algebra is what the inner regularity supplies, and the measure obtained assigns to a general cylinder set the value prescribed by the family. There is no restriction on the cardinality of $T$. The theorem is therefore not a licence to extend a cylinder measure on a *subspace* of $\mathbb{R}^T$: it produces a measure on $\mathbb{R}^T$, and the question whether that measure is carried by a smaller space — a Hilbert space, a space of continuous functions, a space of distributions — is a separate question, and it is the one on which the path integral turns. A cylinder measure can be finite on every cylinder set and still fail to be $\sigma$-additive, because the countable operations that a $\sigma$-algebra permits are not visible in the finitely additive prescription.

### The Trace-Class Obstruction

**Theorem (existence of a Gaussian measure on a Hilbert space).** Let $Q$ be a positive self-adjoint operator on the separable Hilbert space $H$ with eigenvalues $(q_k)$. The Gaussian cylinder measure with covariance $Q$ extends to a Borel probability measure on $H$ if and only if

$$
\operatorname{Tr}Q=\sum_{k\geq1}q_k<\infty .
$$

*Proof.* Suppose first that $\mu$ is a Borel probability on $H$ with covariance $Q$. Then $\int_H\langle x,e_k\rangle^2\,d\mu(x)=q_k$ and $\|x\|^2=\sum_k\langle x,e_k\rangle^2$ for every $x$, so by the monotone convergence theorem

$$
\sum_kq_k=\sum_k\int_H\langle x,e_k\rangle^2\,d\mu(x)=\int_H\|x\|^2\,d\mu(x)<\infty,
$$

the last inequality because $\|x\|<\infty$ for $\mu$-almost every $x$. Conversely, suppose that $\sum_kq_k<\infty$, and let $(g_k)$ be independent real Gaussian variables with $g_k\sim N(0,q_k)$ on a common probability space. Then

$$
\mathbb{E}\Bigl\|\sum_{k=1}^{N}g_ke_k\Bigr\|^2=\sum_{k=1}^{N}q_k\le\operatorname{Tr}Q
$$

for every $N$, so the partial sums form a Cauchy sequence in $L^2$ and converge in $L^2(H)$ and almost surely to a random variable $X$ with values in $H$; the law of $X$ is a Borel probability on $H$ whose cylinder measure is the given one. $\square$

**Corollary (the identity covariance fails).** On an infinite-dimensional Hilbert space there is no Gaussian measure with covariance $Q=I$, because $\sum_k1$ diverges. The cylinder measure exists and is the only object available; the associated random element is **white noise**, whose realisations lie in a space of distributions and not in $H$.

The divergence in the corollary has a direct reading. In $n$ dimensions the Gaussian measure with covariance $I$ has density $(2\pi)^{-n/2}e^{-\|x\|^2/2}$, whose normalising constant tends to zero; the measure concentrates on the sphere of radius $\sqrt n$, which recedes to infinity, and no weak limit exists. The general criterion for a cylinder measure on a locally convex space to be $\sigma$-additive is **Sazonov's theorem**, which asks for the continuity of the characteristic functional in the Hilbert–Schmidt topology, and its nuclear-space form is **Minlos's theorem**; both are quoted. The Hilbert-space case used here is the elementary one above.

## Gaussian Measures on a Hilbert Space

### The Characteristic Functional

**Definition.** A Borel probability $\mu$ on $H$ is **Gaussian** with mean $m\in H$ and covariance operator $Q$ if

$$
\widehat\mu(\xi)=\int_He^{i\langle\xi,x\rangle}\,d\mu(x)=\exp\Bigl(i\langle m,\xi\rangle-\frac12\langle Q\xi,\xi\rangle\Bigr)
$$

for every $\xi\in H$. The operator $Q$ is then positive, self-adjoint and trace class; conversely, a positive self-adjoint trace-class operator $Q$ and a mean $m\in H$ determine exactly one Gaussian measure.

For a Gaussian *cylinder* measure the defining formula is the same on the finite-dimensional projections, and the integral in the definition is then a finite-dimensional Gaussian integral rather than an integral over $H$.

**Proposition (the covariance as a quadratic form).** For a Gaussian measure with covariance $Q$, $\int_H\langle x,u\rangle\langle x,v\rangle\,d\mu(x)=\langle Qu,v\rangle$ and $\int_H\|x-m\|^2\,d\mu(x)=\operatorname{Tr}Q$. The second identity is the reason the trace-class condition is a condition on the *second* moment and not on higher ones: all moments of a Gaussian measure are determined by $m$ and $Q$, and the only one that can diverge is the second.

### Support and the Cameron–Martin Space

**Proposition (support).** A Gaussian measure $\mu$ on $H$ with covariance $Q$ is concentrated on the closure in $H$ of the range of $Q^{1/2}$; when $Q$ has trivial kernel, as in the cases below, that support is all of $H$.

**Definition (Cameron–Martin space).** The **Cameron–Martin space** of $\mu$ is the range $H_\mu=Q^{1/2}(H)$ equipped with the inner product $\langle u,v\rangle_{H_\mu}=\langle Q^{-1/2}u,Q^{-1/2}v\rangle$, the unique inner product for which $Q^{1/2}$ is an isometry from $H$ onto $H_\mu$. The Cameron–Martin norm is the inverse of the covariance quadratic form: $\|u\|_{H_\mu}^2=\langle Q^{-1}u,u\rangle$, whereas the covariance assigns to $u$ the value $\langle Qu,u\rangle$.

**Proposition (the Cameron–Martin space is null).** If $\dim H=\infty$ and $Q$ is injective, then $\mu(H_\mu)=0$.

*Proof.* Write $H_\mu=Q^{1/2}(H)$ and let $X$ be the $H$-valued Gaussian with law $\mu$, so that $X=\sum_kg_ke_k$ with independent $g_k\sim N(0,q_k)$. Membership of $H_\mu$ is equivalent to the finiteness of $\|Q^{-1/2}X\|^2=\sum_kg_k^2/q_k$. The $g_k^2/q_k$ are independent with mean one, so the sum diverges almost surely; hence $X\notin H_\mu$ almost surely. $\square$

The Cameron–Martin space is therefore a set of measure zero, and it is nevertheless the space that governs the theory: it is the tangent space at every point, the space of admissible translations, and the natural domain on which the quadratic form of $Q$ is finite.

### The Cylindrical Wiener Process

The Gaussian cylinder measure with $Q=I$ is the one that arises when a stochastic equation is driven by noise in a Hilbert space of infinite dimension, and its formal time integral is the **cylindrical Wiener process**: the series $W_t=\sum_k\beta_k(t)e_k$ with $(\beta_k)$ independent standard Brownian motions. The series does not converge in $H$, and the process is made sense of through the integrals $\int\Phi\,dW$ defined by the Hilbert–Schmidt isometry. This is the subject of *Stochastic Partial Differential Equations*, and it is the same failure of the trace-class condition, now in the noise index, that the corollary above records; the trace-class condition reappears there as the requirement that the noise covariance and the noise coefficient be Hilbert–Schmidt.

## The Wiener Measure

### The Covariance Kernel $\min(s,t)$

The path measure of Brownian motion is the case of the construction in which the cylinder measure does extend. Let $H=L^2(0,1)$ and let $Q$ be the positive self-adjoint operator with **integral kernel** $R(s,t)=\min(s,t)$:

$$
Q\psi(t)=\int_0^1\min(s,t)\psi(s)\,ds .
$$

**Theorem (the Wiener measure).** The operator $Q$ above has the following properties.

(i) $R$ is a positive-definite kernel, so $Q$ is positive and self-adjoint.

(ii) The eigenfunctions are $v_k(t)=\sqrt2\sin\bigl((k-\tfrac12)\pi t\bigr)$, $k\geq1$, with eigenvalues $\lambda_k=\left((k-\tfrac12)^2\pi^2\right)^{-1}$.

(iii) $\operatorname{Tr}Q=\sum_k\lambda_k=\tfrac12<\infty$, so the Gaussian cylinder measure with covariance $Q$ is a Borel probability measure on $L^2(0,1)$.

(iv) The measure admits a version with continuous paths, and the induced measure on $C[0,1]$ is the **Wiener measure** $\mathbb{W}$, the law of standard Brownian motion.

*Proof.* For (ii), the identity

$$
\int_0^1\min(s,t)\sin\bigl((k-\tfrac12)\pi s\bigr)\,ds=\frac{1}{(k-\frac12)^2\pi^2}\sin\bigl((k-\tfrac12)\pi t\bigr)
$$

is checked by splitting the integral at $s=t$ and using the boundary conditions $v(0)=0$, $v'(1)=0$ that the kernel imposes. For (iii), $\sum_{k\geq1}(k-\tfrac12)^{-2}=\pi^2/2$, so $\operatorname{Tr}Q=\frac12$, which is also $\int_0^1R(t,t)\,dt=\int_0^1t\,dt$. For (iv), the finite-dimensional distributions are those of Brownian motion and the moments $\mathbb{E}|x(t)-x(s)|^{2m}=C_m|t-s|^m$ satisfy Kolmogorov's continuity criterion, whose statement and proof are in *Brownian Motion and Stochastic Calculus*; the continuous version is unique up to indistinguishability. $\square$

The verification of (ii) by quadrature gives $(Qv_k)(t)/v_k(t)=0.4052847346,\,0.0450316372,\,0.0162113894$ for $k=1,2,3$, reproducing $\lambda_k$ to ten decimal places, and the partial sums of $\sum_k\lambda_k$ approach $0.49999\ldots$ as $k$ increases. The number $\tfrac12$ is the variance of $x(1)$, as it must be.

**Remark (the kernel is forced).** The evaluation functionals $\delta_t:x\mapsto x(t)$ are not in $H=L^2(0,1)$ — they are distributions — so the cylinder measure cannot be described by a covariance matrix with entries $Q_{st}$ inside the Hilbert space; the kernel $R(s,t)$ is the distributional form of the covariance, and the scalar product it defines is the one on the Cameron–Martin space $H^1$ and not on $H$. The gain is that the measure is then supported on functions rather than on distributions.

### Path Regularity and the Support

**Proposition (regularity).** $\mathbb{W}$-almost every path is Hölder continuous of every exponent $\alpha<\tfrac12$ and of no exponent $\alpha>\tfrac12$; in particular the paths are not absolutely continuous with square-integrable derivative, and

$$
\mathbb{E}_{\mathbb{W}}\|x\|_{H^1}^2=\infty .
$$

*Proof.* The Hölder statement is Kolmogorov's criterion together with the law of the iterated logarithm, and it is in *Brownian Motion and Stochastic Calculus*. For the energy, discretise $[0,1]$ at the points $t_i=i/n$ with spacing $h=1/n$. The quadratic variation over the grid is $\sum_{i=0}^{n-1}\bigl(x(t_{i+1})-x(t_i)\bigr)^2$, whose expectation is $n\cdot h=1$; the discrete $H^1$ energy divides by the spacing, so it is $\frac1h\sum_{i=0}^{n-1}\bigl(x(t_{i+1})-x(t_i)\bigr)^2$ and its expectation is $\frac1h\cdot n\cdot h=n$. On a grid of $n$ points the expectation $\mathbb{E}\|x\|_{H^1}^2$ is therefore $n$, and its values $4,8,10$ for $n=4,8,10$ grow without bound; equivalently $H^1\subset C^{1/2}$ by the Sobolev embedding in dimension one, and the paths fail the exponent $\tfrac12$. $\square$

The proposition is the exact content of the statement that Brownian paths are rough: the measure is supported on a space of functions strictly larger than the Cameron–Martin space, and the Cameron–Martin space is the smallest space on which the paths can be compared.

## The Cameron–Martin Theorem

### Quasi-Invariance

**Theorem (Cameron–Martin).** Let $\mathbb{W}$ be the Wiener measure and let $h\in H^1_0(0,1)$, the space of absolutely continuous functions with $h(0)=0$ and $h'\in L^2(0,1)$, equipped with the norm $\|h\|_{H^1}^2=\int_0^1h'(t)^2\,dt$. Then the translated measure

$$
\mathbb{W}_h(A)=\mathbb{W}(A-h),\qquad A\in\mathcal{B}\bigl(C[0,1]\bigr),
$$

is absolutely continuous with respect to $\mathbb{W}$, and

$$
\frac{d\mathbb{W}_h}{d\mathbb{W}}(x)=\exp\Bigl(\int_0^1h'(t)\,dx(t)-\frac12\int_0^1h'(t)^2\,dt\Bigr),
$$

where the integral is the Itô integral of $h'$ against the canonical Brownian path. The space $H^1_0$ is the Cameron–Martin space of $\mathbb{W}$.

*Sketch.* In finite dimensions the statement is exact. If $\mu=N(0,C)$ on $\mathbb{R}^n$ with $C$ invertible and $\mu_v(A)=\mu(A-v)$, then

$$
\frac{d\mu_v}{d\mu}(y)=\exp\bigl(\langle v,C^{-1}y\rangle-\tfrac12\langle v,C^{-1}v\rangle\bigr),
$$

an identity verified by completing the square: the exponent is $-\tfrac12(y-v)^\top C^{-1}(y-v)+\tfrac12y^\top C^{-1}y$, and the density integrates to one, as the one-dimensional computation
$\mathbb{E}\bigl[e^{vX-v^2/2}\bigr]=1$ for $X\sim N(0,1)$ confirms; the numerical quadrature of the same identity for $v=0.3$ and $v=1.5$ returns $1.000000000000$. In infinite dimensions $C$ is a compact operator, so $C^{-1}$ is unbounded and $\langle v,C^{-1}v\rangle$ is finite exactly when $v$ lies in the range of $C^{1/2}$, which for the kernel $\min(s,t)$ is $H^1_0$; the quadratic form is then the Cameron–Martin norm and the linear form is the Itô integral. The translation $x\mapsto x+h$ is the shift of Brownian motion by the deterministic path $h$, and the identity is the Girsanov formula of *Brownian Motion and Stochastic Calculus* with $\theta=h'$ up to the sign of the direction of the shift. $\square$

**Example.** For $h(t)=t$ one has $\|h\|_{H^1}^2=\int_0^1dt=1$, and the discretised Cameron–Martin quadratic form of the Brownian covariance gives exactly $1.00000000$. For the rough vector $h(t_i)=(-1)^i\sqrt{1/n}$ on the grid of $n$ points the same form is $29.00$ at $n=8$ and $37.00$ at $n=10$, growing with the resolution: the rough vector is outside the Cameron–Martin space and the quadratic form diverges.

### Singularity Outside the Cameron–Martin Space

**Theorem (mutual singularity).** If $h\notin H^1_0(0,1)$, then $\mathbb{W}_h$ and $\mathbb{W}$ are mutually singular.

*Proof.* The finite-dimensional reductions of the two measures along a refining sequence of grids are Gaussian with means differing by the projection of $h$ and the same covariance. When the projection lies outside the range of $C^{1/2}$ the quadratic form of the difference diverges and the Hellinger affinity of the two finite-dimensional marginals tends to zero; by the martingale convergence of the affinities, the two measures are carried by disjoint sets. $\square$

The dichotomy is the sharp form of the statement that the Brownian measure does not live on a space of smooth paths: it is quasi-invariant under exactly the $H^1$ shifts, and it is carried to a singular measure by every other translation. The Cameron–Martin space is thus the largest space of directions in which the measure may be differentiated.

## The Feynman–Kac Formula and the Euclidean Path Integral

### The Formula

**Theorem (Feynman–Kac).** Let $V:\mathbb{R}^d\to\mathbb{R}$ be continuous and bounded below, let $f$ be bounded and continuous, and let $\mathbb{E}^x$ denote the expectation for Brownian motion started at $x$. Then

$$
u(t,x)=\mathbb{E}^x\Bigl[\exp\Bigl(-\int_0^tV(x_s)\,ds\Bigr)f(x_t)\Bigr]
$$

is the unique bounded solution of the initial-value problem

$$
\partial_tu=\tfrac12\Delta u-Vu,\qquad u(0,\cdot)=f .
$$

The proof is the Itô formula applied to the process $e^{-\int_0^sV(x_r)dr}u(t-s,x_s)$ together with the martingale property; it is given in *Brownian Motion and Stochastic Calculus*, and the result is quoted here as the identity that identifies the Euclidean path integral.

**Verification of the closed forms.** For a constant potential $V$ the solution is $u(t,x)=e^{-Vt}(P_tf)(x)$, and the finite-difference residual of this expression for the backward equation is $8\cdot10^{-9}$ at $(t,x)=(0.3,0.2)$, with the grid spacing $h=10^{-4}$. For the quadratic potential $V(x)=\tfrac12x^2$ the solution with $f\equiv1$ is

$$
u(t,x)=(\cosh t)^{-1/2}\exp\Bigl(-\tfrac12x^2\tanh t\Bigr),
$$

whose residual for $\partial_tu=\tfrac12u_{xx}-\tfrac12x^2u$ is at most $10^{-8}$ at $(t,x)=(0.3,0.0),(0.5,0.4),(0.2,1.1)$, and which satisfies the initial condition $u(0,x)=1$ to twelve decimal places; by the Feynman–Kac theorem the identity of the closed form and the path expectation follows.

### The Euclidean Action as a Measure

Write the Euclidean action of a path $x$ over $[0,t]$ with a potential $V$ as

$$
S_E[x]=\int_0^t\Bigl(\tfrac12|\dot x_s|^2+V(x_s)\Bigr)\,ds .
$$

The kinetic part is not a weight in the Feynman–Kac formula: it is the *measure*. Indeed the Wiener measure is the Gaussian measure whose covariance $Q=(-\Delta)^{-1}$ inverts the kinetic form, so that the quadratic functional $\tfrac12\int|\dot x|^2$ appears as the exponent of the Gaussian density, while the potential enters as the multiplicative density $\exp\bigl(-\int_0^tV(x_s)ds\bigr)$. The Feynman–Kac theorem therefore reads, as a correspondence between the formal path integral on the left and the genuine integral on the right,

$$
\int e^{-S_E[x]}\,\mathcal{D}x\ \longleftrightarrow\ \int_{C[0,t]}f(x_t)\,d\mu_V,\qquad d\mu_V=\exp\Bigl(-\int_0^tV(x_s)\,ds\Bigr)d\mathbb{W},
$$

and the statement is exact as long as the density is integrable. This is the precise sense in which the Euclidean path integral is an integral with respect to a measure: the free weight is a genuine measure and the interaction is a genuine function, and the two are combined by the ordinary operations of integration.

### The Free Euclidean Field

The construction is not special to the heat equation. Let $M$ be a compact Riemannian manifold, or the torus $\mathbb{T}^d$, and let $C=(-\Delta+m^2)^{-1}$ with $m>0$. The operator $C$ is compact, positive, self-adjoint, and trace class, because its eigenvalues $\bigl(\lambda_k+m^2\bigr)^{-1}$ are summable; the Gaussian measure with covariance $C$ therefore exists on $L^2(M)$, and its formal density against the flat reference is $\exp\bigl(-\tfrac12\int_M(|\nabla\phi|^2+m^2\phi^2)\bigr)$, the **free Euclidean field** of mass $m$. This is the model case of constructive quantum field theory: the free measure is a Gaussian measure in the sense of this article, and the interacting measure, when it exists, is obtained from it by a density $\exp(-S_{\mathrm{int}})$ together with a renormalisation of the density so that the total mass remains one. That construction — the cluster expansion, the $\mathcal P(\varphi)_2$ models, the renormalisation of the products of a distributional field — is beyond the scope of this article and is treated in the references.

## The Oscillatory Path Integral and the Fresnel Obstruction

### Oscillatory Integrals by Regularisation

**Definition (oscillatory Gaussian integral).** For $a>0$ the integral $\int_{\mathbb{R}}e^{iax^2/2}\,dx$ is defined as the limit, if it exists, of the absolutely convergent integrals in which the integrand is damped:

$$
\int_{-\infty}^{\infty}e^{\frac{i}{2}ax^2}\,dx=\lim_{\varepsilon\to0+}\int_{-\infty}^{\infty}e^{-\frac12(\varepsilon-ia)x^2}\,dx=\lim_{\varepsilon\to0+}\sqrt{\frac{2\pi}{\varepsilon-ia}}=\sqrt{\frac{2\pi}{-ia}}=\sqrt{\frac{2\pi}{a}}\,e^{i\pi/4}.
$$

The regularisation makes the integrand integrable, the Gaussian integral is elementary, and the limit exists and is independent of the damping. The result has modulus $\sqrt{2\pi/a}$ and argument $\pi/4$; numerically, with $\varepsilon=10^{-8}$ the value is $1.7724538598+1.7724538420\,i$ and $\sqrt{2\pi}e^{i\pi/4}=1.7724538509+1.7724538509\,i$ to eight decimals. The same formula extends to $\mathbb{R}^n$ by

$$
\int_{\mathbb{R}^n}e^{\frac{i}{2}|x|^2}\,dx=(2\pi i)^{n/2},
$$

in which the regularisation is applied in each coordinate. The truncated integral $\int_{-A}^{A}e^{iax^2/2}\,dx$ also converges to the same value as $A\to\infty$, but the convergence is slow — the tail decays like $A^{-1}$ and the integral is not absolutely convergent — so a cut-off is a legitimate definition only in the limit.

### Cameron's Theorem: There Is No Feynman Measure

**Proposition (the finite-dimensional obstruction).** On $\mathbb{R}^n$ the modulus of the oscillatory Gaussian is $|(2\pi i)^{n/2}|=(2\pi)^{n/2}$, which grows exponentially in the dimension: it is $6.283185$, $39.478418$ and $248.050213$ for $n=2,4,6$. The would-be density $e^{i|x|^2/2}$ has modulus one and the constant grows, so no normalisation of the finite-dimensional oscillatory integrals can yield a family of marginals of a single countably additive complex measure in the limit.

**Theorem (Cameron).** Let $S$ be the action of a Lagrangian system. The path-integral functional $C[0,t]\ni x\mapsto e^{iS[x]}$ is not the restriction to the cylinder algebra of a countably additive complex measure on the path space. What exists in its place is a finitely additive cylinder functional of infinite total variation; the "integral" is a distribution on a space of test functionals, or the limit of a family of regularised Wiener integrals, and not an integral against a measure.

The theorem is the sharp statement that the oscillatory integral is not a measure; it is due to Cameron, whose family of integrals connects the Wiener integral to the Feynman integral by continuing the variance from the real to the imaginary axis, and the detailed treatment is in the references. The elementary content of the obstruction is already visible above: the oscillatory functional assigns total variation one to every cylinder and its total variation over a refining family is unbounded, whereas a complex measure has finite total variation.

### What Replaces the Measure

Three constructions produce the oscillatory integral without a measure.

- **Analytic continuation (the imaginary-time construction).** Replace the time $t$ by $-i\tau$, so that the oscillatory factor $e^{iS}$ becomes the real exponential $e^{-S_E}$ of the Euclidean action, and the integral becomes a Wiener integral, which is a measure. The Feynman integral is then recovered by continuing the resulting function of $\tau$ back to $\tau=i t$; for the free particle and the oscillator the continuation is elementary, and it is the content of the explicit kernels of the next section. For an interaction the construction is the Euclidean field-theoretic one, and its success is the existence theorem for the interacting measure.
- **Fresnel integrals.** The free oscillatory integral is defined as the Fourier transform of the Gaussian $e^{i\langle\cdot,\cdot\rangle/2}$ in the distributional sense; the result is the Fresnel integral on the Hilbert space, an object defined by the regularised limit of the previous paragraph and its finite-dimensional products. The integral is then an element of a space of distributions, paired with test functionals.
- **Time slicing.** The integral is defined as the limit of the finite-dimensional oscillatory integrals obtained by discretising the time interval. The next section computes the sliced integrals for a quadratic action; they converge to the explicit kernel in the free and oscillatory cases, and their Euclidean version converges to the Wiener integral. The convergence is the Lie–Trotter product formula at the operator level.

## Time Slicing and the Limit of the Sliced Kernels

### The Sliced Kernel

Discretise the time interval $[0,t]$ into $n$ steps of length $\varepsilon=t/n$ and write $x_j$ for the position at time $j\varepsilon$. For a particle of mass $m$ in a potential $V$ the **$n$-th sliced kernel** between $x_a$ at time $0$ and $x_b$ at time $t$ is the finite-dimensional oscillatory integral

$$
K_n(x_a,x_b;t)=\Bigl(\frac{m}{2\pi i\varepsilon}\Bigr)^{n/2}\int_{\mathbb{R}^{n-1}}\exp\bigl(iS_n(x_0,\dots,x_n)\bigr)\,dx_1\cdots dx_{n-1},
$$

with $x_0=x_a$, $x_n=x_b$ and

$$
S_n=\sum_{j=0}^{n-1}\frac{m}{2\varepsilon}(x_{j+1}-x_j)^2-\frac{m\omega^2\varepsilon}{2}\Bigl[\frac{x_0^2+x_n^2}{2}+\sum_{j=1}^{n-1}x_j^2\Bigr]
$$

for the harmonic potential $V(x)=\tfrac12m\omega^2x^2$, the potential being integrated over the slices by the trapezoidal rule; the second term is absent for the free particle.

### Exactness for a Quadratic Action

**Proposition (quadratic actions are exact).** If $S_n$ is quadratic in the intermediate positions, write it as $S_n=\tfrac12\xi^\top B\xi-c^\top\xi+d$ in the variables $\xi=(x_1,\dots,x_{n-1})$, with $B$ symmetric and invertible. Then the integral defining $K_n$ is a Gaussian integral and evaluates to

$$
K_n=\Bigl(\frac{m}{2\pi i\varepsilon}\Bigr)^{n/2}(2\pi)^{(n-1)/2}\frac{e^{i\pi\,\mathrm{sgn}(B)/4}}{\sqrt{|\det B|}}\exp\Bigl(i\bigl(d-\tfrac12c^\top B^{-1}c\bigr)\Bigr),
$$

where $\mathrm{sgn}(B)$ is the signature of $B$ and the phase $e^{i\pi\,\mathrm{sgn}(B)/4}$ is the Fresnel normalisation of the finite-dimensional oscillatory Gaussian. For the free particle the kernel is independent of $n$ and equals the exact propagator

$$
K(x_a,x_b;t)=\Bigl(\frac{m}{2\pi it}\Bigr)^{1/2}\exp\Bigl(\frac{im(x_b-x_a)^2}{2t}\Bigr).
$$

*Proof of the last claim.* The free action is quadratic in all the $x_j$, so the Gaussian integral is exact for every $n$, and the explicit computation by completing the square gives the same value for every $n$; alternatively the semigroup property of the free kernel gives the same recursion in $n$. $\square$

**Verification.** With $m=1$, $t=1$, $x_a=0$, $x_b=0.3$, the exact kernel is $0.29449920074-0.26911923724\,i$, and the sliced kernels for $n=2,4,6$ are $0.29449920074-0.26911923724\,i$ to fifteen decimal places; the determinant formula above reproduces the exact kernel and the agreement is not an approximation.

### Convergence to the Wiener Measure and to the Oscillator Kernel

**Theorem (the harmonic oscillator).** For the harmonic potential the sliced kernels converge as $n\to\infty$ to the **Mehler kernel**

$$
K(x_a,x_b;t)=\Bigl(\frac{\omega}{2\pi i\sin\omega t}\Bigr)^{1/2}\exp\Bigl(\frac{i\omega}{2\sin\omega t}\bigl((x_a^2+x_b^2)\cos\omega t-2x_ax_b\bigr)\Bigr).
$$

**Verification.** With $m=1$, $\omega=t=1$, $x_a=0$, $x_b=0.3$, the Mehler value is $0.31627748765-0.29850880428\,i$ and the errors of the sliced kernels are $8.44\cdot10^{-3}$, $2.08\cdot10^{-3}$, $5.18\cdot10^{-4}$ at $n=2,4,8$, decreasing by a factor four when $n$ is doubled: the convergence is of second order in the time step.

**Remark (the operator form, and the two limits).** The same computation at the level of operators is the Lie–Trotter product formula $e^{-iHt}=\lim_{n}\bigl(e^{-iH_0t/n}e^{-iVt/n}\bigr)^n$ of *Semigroups and Evolution Equations*: the resolution of the identity inserted between consecutive factors is the integral over $x_j$. In imaginary time the same product formula is a strongly convergent approximation of the semigroup $e^{t(\Delta/2-V)}$, and the sliced integrals converge to the Wiener integral of the Feynman–Kac formula, which is a measure; in real time the products converge only in a weak or distributional sense, which is the operator shadow of the absence of the measure. The two limits of this section are thus the two halves of the article: the Euclidean slicing converges to a measure, and the oscillatory slicing converges to a kernel or a distribution.

## Summary

A cylinder measure on a vector space is a finitely additive set function on the algebra generated by the finite-dimensional projections; it is specified by a consistent family of finite-dimensional distributions, and its countable additivity is not automatic. For a Gaussian cylinder measure on a separable Hilbert space with covariance operator $Q$, the measure is a genuine Borel probability if and only if $\operatorname{Tr}Q=\sum_kq_k<\infty$: if the measure exists then the second moment $\int\|x\|^2d\mu=\operatorname{Tr}Q$ is finite, and if the trace is finite the series $\sum_kg_ke_k$ with independent $g_k\sim N(0,q_k)$ converges almost surely, and its law is the measure. The identity covariance is the boundary case in which the trace diverges: there is no Gaussian measure with covariance $I$, white noise is the associated distribution-valued object, and the general criteria for the extension are the theorems of Sazonov and Minlos. The Gaussian measure is determined by its mean and its covariance through the characteristic functional $\exp(i\langle m,\xi\rangle-\tfrac12\langle Q\xi,\xi\rangle)$; it is concentrated on the closure of the range of $Q^{1/2}$, and its Cameron–Martin space $H_\mu=Q^{1/2}(H)$ is the range with the inverse covariance as inner product, a null set in infinite dimension and nevertheless the space of admissible translations.

The Wiener measure is the Gaussian measure on $L^2(0,1)$ with the covariance kernel $R(s,t)=\min(s,t)$; its eigenfunctions are $\sqrt2\sin((k-\tfrac12)\pi t)$, its eigenvalues are $((k-\tfrac12)^2\pi^2)^{-1}$, its trace is $\tfrac12$, and the Kolmogorov continuity criterion upgrades it to a measure on $C[0,1]$, the law of Brownian motion. Its paths are Hölder of every exponent below $\tfrac12$ and not of exponent $\tfrac12$; the Cameron–Martin space is $H^1_0(0,1)$ with norm $\int(h')^2$, and the measure is quasi-invariant under exactly these translations, with the Radon–Nikodym derivative $\exp(\int h'\,dx-\tfrac12\|h\|^2_{H^1})$, and mutually singular under every other translation. The finite-dimensional model of the theorem is the translated Gaussian $\mu_v\ll\mu$ with density $\exp(\langle v,C^{-1}y\rangle-\tfrac12\langle v,C^{-1}v\rangle)$, finite exactly when $v$ lies in the range of $C^{1/2}$.

The Feynman–Kac formula identifies the Euclidean path integral with an integral against the Wiener measure: $u(t,x)=\mathbb{E}^x[\exp(-\int_0^tV(x_s)ds)f(x_t)]$ solves $\partial_tu=\tfrac12\Delta u-Vu$, the free kinetic weight being the measure and the potential being the density $\exp(-\int V)$, and the same construction on a compact manifold with covariance $(-\Delta+m^2)^{-1}$ gives the free Euclidean field, a genuine Gaussian measure and the starting point of constructive field theory. The oscillatory path integral has no such reading: the factor $e^{iS}$ has modulus one and the finite-dimensional normalisation $(2\pi i)^{n/2}$ grows like $(2\pi)^{n/2}$, so no countably additive complex measure can carry the density, and Cameron's theorem states the obstruction for a general action. What replaces the measure is analytic continuation to imaginary time, which turns the integral into the Euclidean one; the Fresnel integral, which defines the free oscillatory integral distributionally by the regularised limit $\int e^{iax^2/2}dx=\sqrt{2\pi/a}e^{i\pi/4}$; and the time slicing, in which the finite-dimensional oscillatory integrals over the slices converge. The slices are exact for a quadratic action — the free kernel is reproduced for every $n$ — and for the oscillator they converge to the Mehler kernel at second order in the time step, while their Euclidean version converges to the Wiener integral. The Euclidean slicing therefore converges to a measure and the oscillatory slicing to a kernel or a distribution, and the trace-class condition of the first section is the reason for the difference.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $X$, $X'$ | real vector space and its algebraic dual |
| $\mathcal{Z}(X)$ | algebra of cylinder sets |
| $Z(\varphi_1,\dots,\varphi_n;B)$ | cylinder set of a finite list of functionals |
| $\mu$, $\widehat\mu$ | cylinder measure and its characteristic functional |
| $H$, $\langle\cdot,\cdot\rangle$, $(e_k)$ | separable Hilbert space, inner product, orthonormal basis |
| $Q$, $q_k$, $\operatorname{Tr}Q$ | covariance operator, its eigenvalues, its trace |
| $H_\mu=Q^{1/2}(H)$ | Cameron–Martin space with inverse-covariance inner product |
| $W_t=\sum_k\beta_ke_k$ | cylindrical Wiener process (does not converge in $H$) |
| $\mathbb{W}$, $x$ | Wiener measure on $C[0,1]$ and the canonical path |
| $R(s,t)=\min(s,t)$ | Brownian covariance kernel |
| $\lambda_k=((k-\tfrac12)^2\pi^2)^{-1}$ | eigenvalues of the Wiener covariance |
| $H^1_0(0,1)$ | Cameron–Martin space of the Wiener measure |
| $d\mathbb{W}_h/d\mathbb{W}$ | Cameron–Martin density, $\exp(\int h'dx-\tfrac12\|h\|^2)$ |
| $V$, $S_E$, $\mathcal{D}x$ | potential, Euclidean action, formal path measure |
| $u(t,x)$ | Feynman–Kac solution of the backward equation |
| $C=(-\Delta+m^2)^{-1}$ | covariance of the free Euclidean field |
| $K_n$, $K$ | sliced kernel and its limit (free and Mehler) |
| $(2\pi i)^{n/2}$, $\sqrt{2\pi/a}e^{i\pi/4}$ | oscillatory Gaussian normalisations |

## Further Reading

- Norbert Wiener, "Differential space", *Journal of Mathematics and Physics* **2** (1923), 131–174, for the construction of the path measure.
- R. H. Cameron and W. T. Martin, "Transformations of Wiener integrals under translations", *Annals of Mathematics* **45** (1944), 386–396, for the quasi-invariance, the admissible shifts and the Radon–Nikodym derivative.
- R. H. Cameron, "A family of integrals serving to connect the Wiener and Feynman integrals", *Journal of Mathematics and Physics* **39** (1960), 126–140, for the regularised definition and the absence of a Feynman measure.
- I. M. Gel'fand and A. M. Yaglom, "Integration in function spaces and its application to quantum physics", *Journal of Mathematical Physics* **1** (1960), 48–69, for the cylinder-measure viewpoint and the formal path measure.
- Leonard Gross, "Abstract Wiener spaces", *Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability* **2** (1965), 31–42, for the abstract Wiener space and the Cameron–Martin space of a Gaussian measure.
- Hui-Hsiung Kuo, *Gaussian Measures in Banach Spaces* (Springer, 1975), for the Gaussian measures, the Sazonov and Minlos theorems and the structure of the Cameron–Martin space.
- Barry Simon, *Functional Integration and Quantum Physics* (Academic Press, 1979), for the Feynman–Kac formula, the Euclidean path integral and the free field as a Gaussian measure.
- James Glimm and Arthur Jaffe, *Quantum Physics: A Functional Integral Point of View* (Springer, 2nd edition, 1987), for the construction of the interacting measures and the renormalisation of the density.
- Sergio Albeverio, Raphael Høegh-Krohn and Sonia Mazzucchi, *Mathematical Theory of Feynman Path Integrals* (Springer, 2nd edition, 2008), for the Fresnel integrals, the oscillatory integrals and the analytic continuation.
- Gerald W. Johnson and Michel L. Lapidus, *The Feynman Integral and Feynman's Operational Calculus* (Oxford University Press, 2000), for the time slicing, the product formula and the operator-theoretic treatment.
- *Measure Theory and Integration* (`articles_maths/measure-theory-and-integration.md`), companion article, for the construction of measures, the product measures and the Radon–Nikodym theorem.
- *Brownian Motion and Stochastic Calculus* (`articles_maths/brownian-motion-and-stochastic-calculus.md`), companion article, for the Wiener measure, the Itô integral, the Girsanov theorem and the Feynman–Kac formula.
- *Stochastic Partial Differential Equations* (`articles_maths/stochastic-partial-differential-equations.md`), companion article, for the Gaussian measures in infinite dimension and the cylindrical Wiener process.
- *Semigroups and Evolution Equations* (`articles_maths/semigroups-and-evolution-equations.md`), companion article, for the Lie–Trotter product formula and the operator form of the time slicing.
- *Hypercomplex Integration* (`articles_maths/hypercomplex-integration.md`), companion article, for the integration of algebra-valued functions, which is the measure-theoretic integral of this article with values in an algebra.
