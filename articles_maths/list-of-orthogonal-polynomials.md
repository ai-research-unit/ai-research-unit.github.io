
# __List of Orthogonal Polynomials__

## Introduction

This article lists the orthogonal polynomials the corpus introduces. An orthogonal polynomial sequence is a sequence $p_n$ of polynomials, of degree $n$, orthogonal with respect to a weight on an interval, and a row below names one family, records the weight, the recurrence and the differential equation that determine it, and points to the article that introduces it. Every row points to an article; this article introduces nothing and proves nothing. The families are grouped by the layer that introduces them: the four classical families of the real special functions, the generalised families of the spherical theory, and the zonal harmonics that make the addition theorem of a spherical harmonic expansion work. The rows that record a boundary — the monomials, which are not orthogonal; a weight with divergent moments, which generates no orthogonal sequence; the classical interval condition that fails for the Legendre weight on the whole line — stand beside the families as non-examples.

## The Classical Families

| Object | The weight, the recurrence and the equation | Introduced in |
|---|---|---|
| Legendre polynomials $P_n$ | weight $1$ on $[-1,1]$; $(n+1)P_{n+1} = (2n+1)xP_n - nP_{n-1}$; $(1-x^2)y'' - 2xy' + n(n+1)y = 0$ | *Real Special Functions*; *Ordinary Differential Equations* |
| Chebyshev polynomials of the first kind $T_n$ | weight $(1-x^2)^{-1/2}$ on $[-1,1]$; $T_{n+1} = 2xT_n - T_{n-1}$; $(1-x^2)y'' - xy' + n^2y = 0$ | *Real Special Functions*; *Complex Special Functions* |
| Hermite polynomials $H_n$ | weight $e^{-x^2}$ on $\mathbb R$; $H_{n+1} = 2xH_n - 2nH_{n-1}$; $y'' - 2xy' + 2ny = 0$ | *Real Special Functions*; *Fourier Analysis on Euclidean Spaces* |
| Laguerre polynomials $L_n$ | weight $e^{-x}$ on $[0,\infty)$; $(n+1)L_{n+1} = (2n+1-x)L_n - nL_{n-1}$; $xy'' + (1-x)y' + ny = 0$ | *Real Special Functions*; *Complex Special Functions* |
| the complex forms of the four families | the same weights and recurrences, with the orthogonality on the corresponding contour or curve | *Complex Special Functions* |
| the Hermite functions | $H_n(x)e^{-x^2/2}$; the eigenfunctions of the Fourier transform with eigenvalues $(-i)^n$ | *Fourier Analysis on Euclidean Spaces* |
| the Hermite expansion | the completion of the Hermite functions in $L^2(\mathbb R)$; the basis in which the Fourier transform is diagonal | *Fréchet Spaces* |

## The Generalised Families

| Object | The weight, the recurrence and the equation | Introduced in |
|---|---|---|
| Gegenbauer polynomials $C_n^{(\lambda)}$ | weight $(1-x^2)^{\lambda-1/2}$ on $[-1,1]$; the three-term recurrence of the Gegenbauer equation | *Symmetric Tensors and Spherical Harmonics* |
| associated Legendre functions $P_n^m$ | weight $1$ after the factor $(1-x^2)^{-m/2}$; the associated Legendre equation | *Symmetric Tensors and Spherical Harmonics* |
| spherical harmonics $Y_l^m$ | the surface measure on $S^{n-1}$; orthogonal for distinct $l$ or $m$, with the addition theorem | *Symmetric Tensors and Spherical Harmonics* |
| zonal harmonics | the spherical harmonics depending only on one axis; the reproducing kernel of the addition theorem | *Symmetric Tensors and Spherical Harmonics* |
| the harmonic polynomials of degree $l$ | the polynomials killed by the Laplacian; the decomposition of the polynomials into harmonic layers | *Symmetric Tensors and Spherical Harmonics* |

## The Generating Functions and the Orthogonality Constants

| Object | What it supplies | Introduced in |
|---|---|---|
| the Legendre generating function $(1-2xt+t^2)^{-1/2}=\sum_nP_n(x)t^n$ | the generating datum of the Legendre family, from which the recurrence and the values $P_n(1)=1$ follow | *Real Special Functions* |
| the Chebyshev identity $T_n(\cos\theta)=\cos n\theta$ | the trigonometric definition that makes $T_n$ a polynomial, and the extremal property of the family | *Real Special Functions* |
| the orthogonality constant $2/(2n+1)$ | the norm of $P_n$ in $L^2([-1,1],dx)$, and the normalisation of the expansion | *Real Special Functions* |
| the recurrence constants $2n$ and $n+1$ | the coefficients of the Hermite and Laguerre three-term recurrences | *Real Special Functions* |
| the normalisation of the Hermite functions | the constant $(\pi^{1/2}2^nn!)^{-1/2}$ that makes them an orthonormal basis of $L^2(\mathbb R)$ | *Fourier Analysis on Euclidean Spaces* |

## The Orthogonal Polynomials of the Hypercomplex Systems

| Object | The weight, the recurrence and the equation | Introduced in |
|---|---|---|
| the biquaternion Legendre, Chebyshev and Hermite polynomials $P_n(\tilde Q)$, $T_n(\tilde Q)$, $H_n(\tilde Q)$ | the same recurrences in the biquaternion algebra; they reduce to the complex polynomials in the oscillatory regime and truncate in the nilpotent regime | *Biquaternion Higher Special Functions* |
| the split-biquaternion orthogonal polynomials | the same recurrences in the split-biquaternion algebra, with the two regimes of that algebra | *Split-Biquaternion Higher Special Functions* |
| the split-complex Legendre, Chebyshev and Hermite polynomials | the recurrences in the split-complex algebra, with the hyperbolic parametrisation | *Split-Complex Special Functions* |

## Warnings

Two families that a reader may expect are absent. The **Jacobi polynomials** $P_n^{(\alpha,\beta)}$, the two-parameter family with weight $(1-x)^\alpha(1+x)^\beta$ on $[-1,1]$ whose special cases are the Legendre, Chebyshev and Gegenbauer families, are not introduced anywhere in Parts I to III; the corpus treats their special cases directly and does not name the general family. The **Chebyshev polynomials of the second kind** $U_n$, orthogonal with weight $(1-x^2)^{1/2}$, are likewise not introduced. Both are therefore absent from the tables, and the record of their absence is this paragraph.

## Boundary Cases

| Object | The boundary it records | Introduced in |
|---|---|---|
| the monomials $1, x, x^2, \dots$ | not orthogonal with respect to Lebesgue measure on $[-1,1]$: $\int_{-1}^1 x^m x^n\,dx \neq 0$ for $m+n$ even | *Real Special Functions* |
| the Legendre weight on the whole line | the integral $\int_{\mathbb R} P_mP_n\,dx$ diverges, so the Legendre polynomials are orthogonal only on the finite interval | *Real Special Functions* |
| a weight with divergent moments | no orthogonal sequence exists, the moments $\int x^n w(x)\,dx$ being the data of the three-term recurrence | *Complex Special Functions* |
| the second solution of the Legendre equation | $Q_n$ is not a polynomial; the polynomial solution is the one orthogonal with respect to the weight | *Ordinary Differential Equations* |
| the associated Legendre functions at $m > n$ | vanish identically; the spherical harmonic $Y_l^m$ then carries no function | *Symmetric Tensors and Spherical Harmonics* |

## Summary

This list gathers the orthogonal polynomials of the corpus: the Legendre, Chebyshev of the first kind, Hermite and Laguerre families with their weights, recurrences and equations; their complex forms; the Hermite functions and the Hermite expansion; and the Gegenbauer, associated Legendre and spherical-harmonic families of the spherical theory. Each row records the weight that defines the orthogonality and the recurrence that generates the sequence, and the closing table records the families that are absent and the boundary cases.

## Summary of Notation

The objects are named by their standard letters; the symbols in the tables are collected here.

| Symbol | Meaning |
|---|---|
| $P_n$, $T_n$, $H_n$, $L_n$ | Legendre, Chebyshev of the first kind, Hermite, Laguerre polynomials |
| $C_n^{(\lambda)}$, $P_n^m$ | Gegenbauer polynomials, associated Legendre functions |
| $Y_l^m$ | spherical harmonics |
| $w(x)$, $d\mu$ | the weight, and the measure $w(x)\,dx$ it defines |
| $\langle p_m, p_n\rangle_w$ | the inner product with respect to the weight |

## Further Reading

- Gábor Szegő, *Orthogonal Polynomials*, 4th ed. (American Mathematical Society, 1975), for the classical and generalised orthogonal polynomials with their weights, recurrences and asymptotic theory.
- Theodore S. Chihara, *An Introduction to Orthogonal Polynomials* (Gordon and Breach, 1978), for the three-term recurrence as the generating datum and the moment problem it solves.
- Richard Askey, *Orthogonal Polynomials and Special Functions* (SIAM, 1975), for the Jacobi family and its classical special cases.
