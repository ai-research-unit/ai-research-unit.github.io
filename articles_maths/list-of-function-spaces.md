
# __List of Function Spaces__

## Introduction

This article lists the function spaces the corpus meets. A function space is a collection of functions carrying a topology — usually a norm or a family of seminorms — in which limits may be taken, and the rows below name each such space, record the norm or the topology that makes it a space of analysis, record whether that topology is complete, and point to the article that introduces the space. Every row points to an article; this article introduces nothing and proves nothing. The spaces are grouped by the layer that introduces them — the measurable and sequence spaces, the continuous and smooth spaces, the smoothness scales, and the analytic and test-function spaces — and the spaces that fail completeness, or that carry no norm at all, are recorded beside the complete ones as non-examples, so that the class is visibly a proper part of the class above it.

## The Measurable and Sequence Spaces

| Object | The norm it carries, and its completeness | Introduced in |
|---|---|---|
| $L^p(\mu)$, $1 \leq p < \infty$ | $\lVert f\rVert_p = \left(\int \lvert f\rvert^p d\mu\right)^{1/p}$; complete by the Riesz–Fischer theorem | *Measure Theory and Integration* |
| $L^\infty(\mu)$ | essential supremum norm $\lVert f\rVert_\infty = \inf\{c : \lvert f\rvert \leq c \text{ a.e.}\}$; complete | *Measure Theory and Integration* |
| $L^2(\mu)$ | the norm of the inner product $\langle f,g\rangle = \int f\bar g\,d\mu$; complete, and the basic Hilbert space | *Banach and Hilbert Spaces* |
| $\ell^p$, $1 \leq p < \infty$ | $\lVert(x_n)\rVert_p = \left(\sum_n \lvert x_n\rvert^p\right)^{1/p}$; complete | *Normed and Banach Spaces* |
| $\ell^\infty$ | $\lVert(x_n)\rVert_\infty = \sup_n \lvert x_n\rvert$; complete | *Normed and Banach Spaces* |
| $c_0$, $c$ | sup norm; complete, and closed subspaces of $\ell^\infty$ | *Normed and Banach Spaces* |
| $B(X,Y)$, $C_b(X,Y)$ | operator norm and sup norm; complete when $Y$ is complete | *Normed and Banach Spaces*; *Metric, Uniform and Complete Spaces* |
| $L^p(0,T;V)$, Bochner space | $\left(\int_0^T \lVert u(t)\rVert_V^p dt\right)^{1/p}$; complete when $V$ is Banach | *Sobolev Spaces and Weak Solutions* |

The measurable spaces are the ones on which the integral is available, and their completeness is the completeness that makes the convergence theorems of the integral into existence theorems for limits.

## The Continuous and Smooth Spaces

| Object | The norm or topology it carries, and its completeness | Introduced in |
|---|---|---|
| $C(K)$, $K$ compact | supremum norm $\lVert f\rVert_\infty$; complete | *Normed and Banach Spaces* |
| $C_0(X)$, $C_c(X)$ | sup norm; $C_0$ complete, $C_c$ dense in $C_0$ | *Fourier Analysis on Euclidean Spaces*; *Modes of Convergence* |
| $C^k(U,Y)$, $0 \leq k < \infty$ | the seminorms of the derivatives up to order $k$ on compacta; complete | *Differential Calculus on Normed Spaces* |
| $C^\infty(U) = \mathcal E(\Omega)$ | the increasing seminorms $\sup_K \lvert\partial^\alpha f\rvert$, $K$ compact, $\lvert\alpha\rvert \leq n$; a Fréchet space, hence complete | *Fréchet Spaces* |
| $\mathcal O(\Omega)$, holomorphic functions | the seminorms of the supremum on compacta; a Fréchet space, hence complete and Montel | *Fréchet Spaces* |
| $B M O$, bounded mean oscillation | $\sup_Q \frac{1}{\lvert Q\rvert}\int_Q \lvert f - f_Q\rvert$, a seminorm modulo constants; complete | *Besov and Triebel–Lizorkin Spaces* |

## The Smoothness Scales

| Object | The norm it carries, and its completeness | Introduced in |
|---|---|---|
| $W^{k,p}(\Omega)$, $W^{k,p}_0(\Omega)$ | $\lVert f\rVert_{W^{k,p}}^p = \sum_{\lvert\gamma\rvert\leq k}\lVert\partial^\gamma f\rVert_p^p$; a Banach space, hence complete | *Sobolev Spaces and Weak Solutions* |
| $H^k(\Omega) = W^{k,2}(\Omega)$ | the inner product $\sum_{\lvert\gamma\rvert\leq k}\langle\partial^\gamma f,\partial^\gamma g\rangle$; a Hilbert space | *Sobolev Spaces and Weak Solutions* |
| $H^{-1}(\Omega)$ | the operator norm in the dual of $H^1_0(\Omega)$; complete | *Sobolev Spaces and Weak Solutions* |
| $H^s(\mathbb R^n)$, $s \in \mathbb R$ | $\lVert f\rVert_{H^s}^2 = \int(1+\lvert\xi\rvert^2)^s\lvert\hat f(\xi)\rvert^2 d\xi$; complete | *Fourier Analysis on Euclidean Spaces* |
| $H^s_p$, Bessel-potential space | $\lVert f\rVert = \lVert(1-\Delta)^{s/2}f\rVert_p$; complete | *Interpolation Theory* |
| $C^{k,\alpha}$, Hölder space | $\lVert f\rVert = \sum_{\lvert\gamma\rvert\leq k}\lVert\partial^\gamma f\rVert_\infty + \sup_{x\neq y}\frac{\lvert\partial^\gamma f(x)-\partial^\gamma f(y)\rvert}{\lvert x-y\rvert^\alpha}$; complete | *Besov and Triebel–Lizorkin Spaces* |
| $\Lambda^s = C^s$, Hölder–Zygmund space | the Besov norm $B^s_{\infty,\infty}$; complete | *Besov and Triebel–Lizorkin Spaces* |
| $B^s_{p,q}$, Besov space | the mixed $\ell^q(L^p)$ norm of the Littlewood–Paley blocks; a quasi-Banach space, complete | *Besov and Triebel–Lizorkin Spaces* |
| $F^s_{p,q}$, Triebel–Lizorkin space | the mixed $L^p(\ell^q)$ norm of the Littlewood–Paley blocks; complete | *Besov and Triebel–Lizorkin Spaces* |
| $H^1$, real Hardy space | $\lVert f\rVert_{H^1} = \lVert \sup_t \lvert f * \phi_t\rvert\rVert_1$; complete, and the borderline case $F^0_{1,2}$ | *Besov and Triebel–Lizorkin Spaces* |
| $L^{p,q}$, Lorentz space | the norm of the decreasing rearrangement, $\lVert f\rVert = \left(\int_0^\infty (t^{1/p}f^*(t))^q \frac{dt}{t}\right)^{1/q}$; complete | *Interpolation Theory* |

## The Analytic and Test-Function Spaces

| Object | The norm or topology it carries, and its completeness | Introduced in |
|---|---|---|
| $H^p(\mathbb D)$, Hardy space | $\lVert f\rVert_{H^p} = \sup_{0<r<1}\left(\frac{1}{2\pi}\int_0^{2\pi}\lvert f(re^{i\theta})\rvert^p d\theta\right)^{1/p}$; complete | *Complex Harmonic Analysis* |
| $A^p(\mathbb D)$, Bergman space | $\left(\frac{1}{\pi}\int_{\mathbb D}\lvert f\rvert^p dA\right)^{1/p}$; complete | *Complex Harmonic Analysis* |
| $\mathcal B$, Bloch space | $\sup_z (1-\lvert z\rvert^2)\lvert f'(z)\rvert$; complete modulo constants | *Complex Harmonic Analysis* |
| $PW_B$, Paley–Wiener space | the $L^2$ norm of the boundary function; a closed subspace of $L^2$ | *Complex Harmonic Analysis* |
| $\mathcal S(\mathbb R^n)$, Schwartz class | the seminorms $p_{\alpha,\beta}(f) = \sup_x \lvert x^\alpha\partial^\beta f\rvert$; a Fréchet space, hence complete | *Fourier Analysis on Euclidean Spaces*; *Fréchet Spaces* |
| $\mathcal D(\Omega) = C_c^\infty(\Omega)$ | the LF inductive limit of the $\mathcal D_K$; complete, and not normable | *Distributions and Fundamental Solutions* |
| $\mathcal D_K(\Omega)$ | the seminorms $\sup_K \lvert\partial^\alpha f\rvert$; a Fréchet space | *Distributions and Fundamental Solutions* |
| $\mathcal D'(\Omega)$, $\mathcal E'(\Omega)$, $\mathcal S'(\mathbb R^n)$ | the strong dual topologies; complete | *Distributions and Fundamental Solutions* |

The test-function spaces are the ones whose duals are the distributions, and the last three rows are recorded here as spaces, their distribution-theoretic content belonging to the catalogue of distributions.

## Spaces Without a Norm, and Spaces That Are Not Complete

| Object | The property that fails | Introduced in |
|---|---|---|
| $L^p(\mu)$ with $0 < p < 1$ | carries a quasi-norm but no norm, and is not locally convex | *Locally Convex Spaces* |
| $\mathcal D(\Omega)$, $C_c^\infty(\Omega)$ | complete in its LF topology, but no norm defines that topology | *Distributions and Fundamental Solutions* |
| $\mathcal P([0,1])$, the polynomials | dense in $C[0,1]$ under the supremum norm, hence normed but not complete; its completion is $C[0,1]$ | *Metric, Uniform and Complete Spaces* |
| $c_{00}$, finitely supported sequences | dense in $\ell^p$, hence normed but not complete | *Normed and Banach Spaces* |
| $C([0,1])$ under the $L^2$ norm | the norm is genuine, but the space is not complete; its completion is $L^2([0,1])$ | *Measure Theory and Integration* |
| Riemann integrable functions under the supremum norm | a pointwise limit of Riemann integrable functions need not be Riemann integrable, so the space is not complete | *Real Integration* |
| a countable direct sum $\bigoplus_n X_n$ of nonzero Banach spaces | incomplete under each of the sum, maximum and Euclidean norms; its completions are the sequences with $\sum_i \lVert x_i\rVert < \infty$ and those with $\lVert x_i\rVert \to 0$ | *Normed and Banach Spaces* |

## Summary

This list gathers the function spaces of the corpus in four families: the measurable spaces $L^p$ and their discrete counterparts $\ell^p$; the continuous and smooth spaces $C^k$, $C^\infty$ and the holomorphic spaces; the smoothness scales $W^{k,p}$, $H^s$, the Hölder, Besov, Triebel–Lizorkin and Hardy spaces; and the analytic and test-function spaces $H^p$, $A^p$, the Schwartz class and $\mathcal D$. Each row records the norm or the topology the space carries and whether it is complete, and the final table records the spaces for which completeness or normability fails.

## Summary of Notation

The objects of this list are named rather than denoted; the few symbols used in the tables are collected here.

| Symbol | Meaning |
|---|---|
| $\mathbb K$ | $\mathbb R$ or $\mathbb C$ |
| $\mu$ | a measure, so that $L^p(\mu)$ is a Lebesgue space |
| $\Omega$, $U$ | an open subset of $\mathbb R^n$, or of a normed space |
| $K$ | a compact set |
| $p,q$ | conjugate exponents, $1/p + 1/q = 1$ |
| $k,\alpha,s$ | differentiability order, Hölder exponent, real smoothness index |
| $\mathcal D$, $\mathcal S$, $\mathcal E$ | test functions, Schwartz class, smooth functions |
| $\mathcal D'$, $\mathcal S'$, $\mathcal E'$ | their duals, the spaces of distributions |

## Further Reading

- Albrecht Pietsch, *History of Banach Spaces and Linear Operators* (Birkhäuser, 2007), for the catalogue of the classical Banach function spaces and their completeness.
- Hans Triebel, *Theory of Function Spaces* (Birkhäuser, 1983), for the Sobolev, Hölder, Besov and Triebel–Lizorkin scales tabulated side by side.
- Nelson Dunford and Jacob T. Schwartz, *Linear Operators, Part I* (Interscience, 1958), for the standard function spaces of analysis with their norms and completeness properties.
