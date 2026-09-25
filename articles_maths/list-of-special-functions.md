
# __List of Special Functions__

## Introduction

This article lists the special functions the corpus introduces. A special function is a named solution of a differential equation or of a functional equation that the elementary functions do not solve, and a row below names one, records the equation it satisfies and the family it belongs to, and points to the article that introduces it. Every row points to an article; this article introduces nothing and proves nothing. The functions are grouped by the layer that introduces them: the elementary transcendentals, which are the degenerate cases against which the others are measured; the gamma and beta family and the error functions; the zeta and number-theoretic functions; the orthogonal polynomials and spherical functions; the Bessel, Airy and hypergeometric functions; and the elliptic integrals and elliptic functions. The rows that record a boundary — the Lambert $W$, which satisfies no linear equation; the gamma function, which has no zeros; the elliptic functions, which are not single-valued without their lattice — stand beside them as non-examples.

## The Elementary Transcendental Functions

| Object | The equation it solves | Introduced in |
|---|---|---|
| the exponential $e^x$ | $y' = y$, $y(0) = 1$; the sum $\sum x^n/n!$ | *Real Special Functions* |
| the logarithm $\ln x$ | $y' = 1/x$, $y(1) = 0$; the inverse of the exponential | *Real Special Functions* |
| the trigonometric functions $\sin$, $\cos$ | $y'' + y = 0$; defined by their power series and the differential system | *Real Special Functions* |
| the hyperbolic functions $\sinh$, $\cosh$, $\tanh$ | $y'' - y = 0$; the exponential in its even and odd parts | *Real Special Functions* |
| the inverse trigonometric and inverse hyperbolic functions | the equations $y' = 1/\sqrt{1-x^2}$, $y' = 1/\sqrt{1+x^2}$ | *Real Special Functions* |
| general powers $a^x$ | $y' = (\ln a) y$; the composition of the exponential and the logarithm | *Real Special Functions* |
| the complex exponential, logarithm and trigonometric functions | the same equations, with the multi-valuedness of the logarithm on $\mathbb C^\times$ | *Complex Special Functions* |
| the Lambert $W$ | $W e^W = x$; a functional equation, not a linear differential equation | *Real Special Functions*; *Complex Special Functions* |

## The Gamma and Beta Family

| Object | The equation or the functional equation it satisfies | Introduced in |
|---|---|---|
| the gamma function $\Gamma$ | $\Gamma(z+1) = z\Gamma(z)$, $\Gamma(1) = 1$; the integral $\int_0^\infty t^{z-1}e^{-t}dt$ | *Real Special Functions*; *Complex Special Functions* |
| the beta function $B$ | $B(x,y) = \Gamma(x)\Gamma(y)/\Gamma(x+y)$; the integral over the simplex | *Real Special Functions* |
| the digamma function $\psi$ | $\psi = \Gamma'/\Gamma$, the logarithmic derivative of the gamma function | *Dual-Numbers Special Functions* |
| the error function $\operatorname{erf}$ | $\operatorname{erf}' = 2e^{-x^2}/\sqrt\pi$; the incomplete gamma of order $1/2$ | *Real Special Functions*; *Complex Special Functions* |
| the complementary and imaginary error functions | the complements and the analytic continuation of $\operatorname{erf}$ | *Real Special Functions* |
| the Dawson function | $F' + 2xF = 1$; the imaginary error function | *Real Special Functions* |
| the Fresnel integrals | $C' = \cos(\pi x^2/2)$, $S' = \sin(\pi x^2/2)$ | *Real Special Functions* |
| the incomplete gamma and beta functions | the integral representations $\gamma(s,x)$, $B(x;a,b)$, and their functional equations | *Real Special Functions*; *Complex Special Functions* |
| the regularised incomplete gamma and beta functions | the ratios $P$, $Q$ and $I_x(a,b)$, with values in $[0,1]$ | *Real Special Functions* |

## The Zeta and Number-Theoretic Functions

| Object | The equation or the product it satisfies | Introduced in |
|---|---|---|
| the Riemann zeta function $\zeta$ | the functional equation relating $\zeta(s)$ and $\zeta(1-s)$; the Euler product over the primes | *Zeta Functions*; *Real Special Functions* |
| the Dirichlet eta function $\eta$ | $\eta(s) = (1-2^{1-s})\zeta(s)$; the alternating series | *Real Special Functions* |
| a Dirichlet $L$-function | the functional equation of the character, and the Euler product | *Zeta Functions*; *Analytic Number Theory* |
| the Bernoulli numbers $B_n$ | the generating function $t/(e^t-1) = \sum B_n t^n/n!$ | *Real Special Functions* |
| the Bernoulli polynomials | $B_n(x+1) - B_n(x) = nx^{n-1}$; the generating function | *Real Special Functions* |
| the Euler numbers $E_n$ | $\operatorname{sech} t = \sum E_n t^n/n!$; the tangent numbers | *Real Special Functions* |
| the Möbius and Euler totient functions | the Dirichlet convolution $\mu * 1 = \varepsilon$, and the Dirichlet series | *Combinatorial Functions and Generating Functions* |

## Orthogonal Polynomials and Spherical Functions

| Object | The differential equation it solves | Introduced in |
|---|---|---|
| the Legendre polynomials $P_n$ | $(1-x^2)y'' - 2xy' + n(n+1)y = 0$; the Legendre equation | *Real Special Functions*; *Ordinary Differential Equations* |
| the Chebyshev polynomials $T_n$ | $(1-x^2)y'' - xy' + n^2y = 0$; the Chebyshev equation | *Real Special Functions*; *Complex Special Functions* |
| the Hermite polynomials $H_n$ | $y'' - 2xy' + 2ny = 0$; the Hermite equation, and the Fourier transform's eigenfunctions | *Real Special Functions*; *Fourier Analysis on Euclidean Spaces* |
| the Laguerre polynomials $L_n$ | $xy'' + (1-x)y' + ny = 0$; the Laguerre equation | *Real Special Functions*; *Complex Special Functions* |
| the Gegenbauer polynomials $C_n^{(\lambda)}$ | the Gegenbauer equation; the Chebyshev and Legendre cases at $\lambda = 1$ and $\lambda = 1/2$ | *Symmetric Tensors and Spherical Harmonics* |
| the associated Legendre functions $P_n^m$ | the associated Legendre equation, with the $(1-x^2)^{-m/2}$ factor | *Symmetric Tensors and Spherical Harmonics* |
| the spherical harmonics $Y_l^m$ | the Laplace equation on the sphere; the eigenfunctions of the spherical Laplacian | *Symmetric Tensors and Spherical Harmonics* |

## Bessel, Airy and Hypergeometric Functions

| Object | The equation it solves | Introduced in |
|---|---|---|
| the Bessel function $J_\nu$ | $x^2y'' + xy' + (x^2-\nu^2)y = 0$; Bessel's equation | *Real Special Functions*; *Ordinary Differential Equations* |
| the Bessel function of the second kind $Y_\nu$ | the same equation, the second solution at an integer order | *Real Special Functions* |
| the modified Bessel functions $I_\nu$, $K_\nu$ | $x^2y'' + xy' - (x^2+\nu^2)y = 0$ | *Real Special Functions* |
| the Airy function $\operatorname{Ai}$ | $y'' - xy = 0$; the Airy equation, solved by the Fourier integral | *Real Special Functions*; *Complex Special Functions* |
| the hypergeometric function ${}_2F_1$ | the hypergeometric equation $x(1-x)y'' + (c-(a+b+1)x)y' - aby = 0$ | *Real Special Functions*; *Complex Special Functions* |
| the confluent hypergeometric and Whittaker functions | the confluent equation obtained as $c \to \infty$ | *Complex Special Functions* |
| the generalised hypergeometric function ${}_pF_q$ | the generalised equation of order $p$, $q$ | *Real Special Functions* |
| the complete elliptic integrals $K$, $E$ | the hypergeometric cases ${}_2F_1(1/2,1/2;1;m)$ and ${}_2F_1(-1/2,1/2;1;m)$ | *Real Special Functions*; *Complex Special Functions* |

## Elliptic Integrals and Elliptic Functions

| Object | The equation or the property it satisfies | Introduced in |
|---|---|---|
| the incomplete elliptic integrals $F$, $E$, $\Pi$ | the integral forms, and the addition theorems of the elliptic theory | *Real Special Functions*; *Complex Special Functions* |
| the Jacobi elliptic functions $\operatorname{sn}$, $\operatorname{cn}$, $\operatorname{dn}$ | the addition theorems and the double periodicity in the lattice | *Elliptic Functions and Integrals* (planned) |
| the Weierstrass function $\wp$ | $\wp'^2 = 4\wp^3 - g_2\wp - g_3$; the associated elliptic curve | *Elliptic Functions and Integrals* (planned) |
| the elliptic modular function $j$ | the modular invariance $j(\gamma\tau) = j(\tau)$ and the $j$-invariant of the curve | *Elliptic Functions and Integrals* (planned) |

## Boundary Cases

| Object | The boundary it records | Introduced in |
|---|---|---|
| the gamma function at its poles | has simple poles at $0,-1,-2,\dots$ and no zeros; the reciprocal $1/\Gamma$ is entire | *Complex Special Functions* |
| the elementary functions as hypergeometric cases | the exponential, the logarithm and the trigonometric functions are degenerate ${}_2F_1$ cases, which is why they carry no independent equation | *Real Special Functions* |
| the Lambert $W$ | satisfies a functional equation, not a linear differential equation, and is multiply valued | *Real Special Functions* |
| the Bessel functions at an integer order | the second solution $Y_n$ requires the limit of $Y_\nu$, the logarithmic case | *Real Special Functions* |
| the elliptic functions | not single-valued on $\mathbb C$; defined on the torus $\mathbb C/\Lambda$ by their lattice | *Elliptic Functions and Integrals* (planned) |

## Summary

This list gathers the special functions of the corpus: the elementary transcendentals and the Lambert $W$; the gamma, beta, error, incomplete and Fresnel functions; the zeta function with its Dirichlet relatives and the Bernoulli and Euler numbers; the Legendre, Chebyshev, Hermite, Laguerre, Gegenbauer and spherical functions; the Bessel, Airy and hypergeometric functions; and the elliptic integrals, with the elliptic functions that the planned article introduces. Each row records the equation the function solves, and the closing table records the boundaries of the class.

## Summary of Notation

The objects are named by their standard letters; the few symbols used in the tables are collected here.

| Symbol | Meaning |
|---|---|
| $\Gamma$, $B$ | the gamma and beta functions |
| $\zeta$, $\eta$, $L(s,\chi)$ | the Riemann zeta, Dirichlet eta and Dirichlet $L$-functions |
| $P_n, T_n, H_n, L_n$ | Legendre, Chebyshev, Hermite, Laguerre polynomials |
| $J_\nu$, $I_\nu$, $\operatorname{Ai}$ | Bessel, modified Bessel and Airy functions |
| ${}_2F_1$, ${}_pF_q$ | hypergeometric and generalised hypergeometric functions |
| $K$, $E$, $\Pi$ | complete and incomplete elliptic integrals |
| $W$ | the Lambert $W$ function |

## Further Reading

- Milton Abramowitz and Irene A. Stegun, *Handbook of Mathematical Functions* (National Bureau of Standards, 1964; reprinted Dover, 1965), for the catalogue of the elementary and higher special functions with their equations.
- Edmund T. Whittaker and George N. Watson, *A Course of Modern Analysis*, 4th ed. (Cambridge University Press, 1927), for the gamma, hypergeometric, Bessel and elliptic functions treated from their differential equations.
- NIST Digital Library of Mathematical Functions, released at <https://dlmf.nist.gov/>, for the modern reference tables of the special functions and their recurrences.
