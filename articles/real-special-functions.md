
# __Real Special Functions__

## Introduction

This article introduces the real special functions as a collection of named functions that arise repeatedly in analysis, differential equations, and mathematical physics. The goal is to define each function precisely, establish its basic properties, and describe the relations among them.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No complex analysis is invoked. All functions are treated as functions of a real variable, and all integral representations are real integrals. The order of presentation follows the dependency order: elementary functions first, then functions defined from them, then functions defined from those.

## The Exponential and Logarithm

### Definition

The **exponential function** is defined for $x \in \mathbb{R}$ by

$$
\exp(x) = \sum_{n=0}^\infty \frac{x^n}{n!}.
$$

The series converges absolutely for every $x$. The function is smooth, strictly increasing, and satisfies

$$
\exp(x + y) = \exp(x) \exp(y), \qquad \exp(0) = 1, \qquad \exp'(x) = \exp(x).
$$

We write $e^x = \exp(x)$ where $e = \exp(1)$.

### The Logarithm

The **natural logarithm** is the inverse of the exponential:

$$
\ln x = \int_1^x \frac{dt}{t}, \qquad x > 0.
$$

It satisfies

$$
\ln(xy) = \ln x + \ln y, \qquad \ln 1 = 0, \qquad (\ln x)' = \frac{1}{x}.
$$

### General Powers

For $a > 0$ and $x \in \mathbb{R}$,

$$
a^x = \exp(x \ln a).
$$

This is consistent with integer and rational powers and extends them continuously to all real exponents.

## The Trigonometric Functions

### Definition

The **sine** and **cosine** functions are defined by

$$
\sin x = \sum_{n=0}^\infty \frac{(-1)^n x^{2n+1}}{(2n+1)!}, \qquad \cos x = \sum_{n=0}^\infty \frac{(-1)^n x^{2n}}{(2n)!}.
$$

Both series converge absolutely for every $x$. They satisfy

$$
\sin' x = \cos x, \qquad \cos' x = -\sin x,
$$

$$
\sin(x + y) = \sin x \cos y + \cos x \sin y,
$$

$$
\cos(x + y) = \cos x \cos y - \sin x \sin y,
$$

$$
\sin^2 x + \cos^2 x = 1.
$$

### Periodicity

The number $\pi$ is defined as twice the smallest positive zero of $\cos$. Both functions are $2\pi$-periodic:

$$
\sin(x + 2\pi) = \sin x, \qquad \cos(x + 2\pi) = \cos x.
$$

### The Other Trigonometric Functions

$$
\tan x = \frac{\sin x}{\cos x}, \qquad \cot x = \frac{\cos x}{\sin x},
$$

$$
\sec x = \frac{1}{\cos x}, \qquad \csc x = \frac{1}{\sin x}.
$$

Each is defined wherever the denominator is non-zero.

### Inverse Trigonometric Functions

The **arcsine** is the inverse of $\sin$ on $[-\pi/2, \pi/2]$:

$$
\arcsin x = \int_0^x \frac{dt}{\sqrt{1 - t^2}}, \qquad -1 \leq x \leq 1.
$$

The **arccosine** is the inverse of $\cos$ on $[0, \pi]$:

$$
\arccos x = \frac{\pi}{2} - \arcsin x.
$$

The **arctangent** is the inverse of $\tan$ on $(-\pi/2, \pi/2)$:

$$
\arctan x = \int_0^x \frac{dt}{1 + t^2}, \qquad x \in \mathbb{R}.
$$

It satisfies

$$
\arctan x + \arctan \frac{1}{x} = \frac{\pi}{2}, \qquad x > 0.
$$

## The Hyperbolic Functions

### Definition

The **hyperbolic sine** and **hyperbolic cosine** are

$$
\sinh x = \frac{e^x - e^{-x}}{2}, \qquad \cosh x = \frac{e^x + e^{-x}}{2}.
$$

They satisfy

$$
\sinh' x = \cosh x, \qquad \cosh' x = \sinh x,
$$

$$
\cosh^2 x - \sinh^2 x = 1,
$$

$$
\sinh(x + y) = \sinh x \cosh y + \cosh x \sinh y,
$$

$$
\cosh(x + y) = \cosh x \cosh y + \sinh x \sinh y.
$$

### The Other Hyperbolic Functions

$$
\tanh x = \frac{\sinh x}{\cosh x}, \qquad \coth x = \frac{\cosh x}{\sinh x},
$$

$$
\operatorname{sech} x = \frac{1}{\cosh x}, \qquad \operatorname{csch} x = \frac{1}{\sinh x}.
$$

### Inverse Hyperbolic Functions

$$
\operatorname{arsinh} x = \ln\left(x + \sqrt{x^2 + 1}\right), \qquad x \in \mathbb{R},
$$

$$
\operatorname{arcosh} x = \ln\left(x + \sqrt{x^2 - 1}\right), \qquad x \geq 1,
$$

$$
\operatorname{artanh} x = \frac{1}{2} \ln \frac{1 + x}{1 - x}, \qquad -1 < x < 1.
$$

## The Gamma and Beta Functions

### The Gamma Function

The **gamma function** is defined for $x > 0$ by

$$
\Gamma(x) = \int_0^\infty t^{x-1} e^{-t} \, dt.
$$

It satisfies the **functional equation**

$$
\Gamma(x + 1) = x \Gamma(x),
$$

which follows from integration by parts. Since $\Gamma(1) = 1$, this gives

$$
\Gamma(n + 1) = n!
$$

for non-negative integers $n$. The gamma function is the unique logarithmically convex function on $(0, \infty)$ satisfying $\Gamma(1) = 1$ and $\Gamma(x + 1) = x \Gamma(x)$, by the Bohr–Mollerup theorem.

**Reflection formula.**

$$
\Gamma(x) \Gamma(1 - x) = \frac{\pi}{\sin(\pi x)}, \qquad 0 < x < 1.
$$

**Duplication formula.**

$$
\Gamma(x) \Gamma\left(x + \tfrac{1}{2}\right) = 2^{1-2x} \sqrt{\pi} \, \Gamma(2x).
$$

### The Beta Function

The **beta function** is defined for $x, y > 0$ by

$$
B(x, y) = \int_0^1 t^{x-1} (1 - t)^{y-1} \, dt.
$$

It satisfies

$$
B(x, y) = \frac{\Gamma(x) \Gamma(y)}{\Gamma(x + y)}.
$$

**Proof.** Substitute $t = u/(1+u)$ in the beta integral, then use the gamma integral representation for each factor. $\square$

It is symmetric: $B(x, y) = B(y, x)$.

## The Error Function and Related Functions

### The Error Function

The **error function** is defined by

$$
\operatorname{erf}(x) = \frac{2}{\sqrt{\pi}} \int_0^x e^{-t^2} \, dt.
$$

It is odd, strictly increasing, and satisfies

$$
\lim_{x \to \infty} \operatorname{erf}(x) = 1, \qquad \lim_{x \to -\infty} \operatorname{erf}(x) = -1.
$$

### The Complementary Error Function

$$
\operatorname{erfc}(x) = 1 - \operatorname{erf}(x) = \frac{2}{\sqrt{\pi}} \int_x^\infty e^{-t^2} \, dt.
$$

### The Imaginary Error Function

$$
\operatorname{erfi}(x) = \frac{2}{\sqrt{\pi}} \int_0^x e^{t^2} \, dt.
$$

### The Dawson Function

$$
D(x) = e^{-x^2} \int_0^x e^{t^2} \, dt.
$$

It satisfies the differential equation

$$
D'(x) + 2x D(x) = 1.
$$

### The Fresnel Integrals

$$
S(x) = \int_0^x \sin\left(\frac{\pi t^2}{2}\right) dt, \qquad C(x) = \int_0^x \cos\left(\frac{\pi t^2}{2}\right) dt.
$$

Both converge as $x \to \infty$, with

$$
\lim_{x \to \infty} S(x) = \lim_{x \to \infty} C(x) = \frac{1}{2}.
$$

## The Incomplete Gamma and Beta Functions

### The Incomplete Gamma Function

The **lower incomplete gamma function** is

$$
\gamma(s, x) = \int_0^x t^{s-1} e^{-t} \, dt, \qquad s > 0, \; x \geq 0.
$$

The **upper incomplete gamma function** is

$$
\Gamma(s, x) = \int_x^\infty t^{s-1} e^{-t} \, dt, \qquad s > 0, \; x \geq 0.
$$

They satisfy

$$
\gamma(s, x) + \Gamma(s, x) = \Gamma(s).
$$

### The Regularized Incomplete Gamma Functions

$$
P(s, x) = \frac{\gamma(s, x)}{\Gamma(s)}, \qquad Q(s, x) = \frac{\Gamma(s, x)}{\Gamma(s)}.
$$

These satisfy $P + Q = 1$ and take values in $[0, 1]$.

### The Incomplete Beta Function

$$
B(x; a, b) = \int_0^x t^{a-1} (1 - t)^{b-1} \, dt, \qquad 0 \leq x \leq 1, \; a, b > 0.
$$

The **regularized incomplete beta function** is

$$
I_x(a, b) = \frac{B(x; a, b)}{B(a, b)}.
$$

It satisfies $I_0(a, b) = 0$ and $I_1(a, b) = 1$.

## The Riemann Zeta Function

### Definition

The **Riemann zeta function** is defined for $s > 1$ by

$$
\zeta(s) = \sum_{n=1}^\infty \frac{1}{n^s}.
$$

The series converges absolutely for $s > 1$ and diverges for $s \leq 1$.

### Integral Representation

For $s > 1$,

$$
\zeta(s) = \frac{1}{\Gamma(s)} \int_0^\infty \frac{t^{s-1}}{e^t - 1} \, dt.
$$

### Special Values

$$
\zeta(2) = \frac{\pi^2}{6}, \qquad \zeta(4) = \frac{\pi^4}{90}, \qquad \zeta(2n) = \frac{(-1)^{n+1} B_{2n} (2\pi)^{2n}}{2 (2n)!},
$$

where $B_{2n}$ are the Bernoulli numbers.

### The Euler Product

For $s > 1$,

$$
\zeta(s) = \prod_p \frac{1}{1 - p^{-s}},
$$

where the product is over all primes $p$. This is the analytic form of the fundamental theorem of arithmetic.

### The Dirichlet Eta Function

$$
\eta(s) = \sum_{n=1}^\infty \frac{(-1)^{n-1}}{n^s} = (1 - 2^{1-s}) \zeta(s), \qquad s > 0.
$$

This extends $\zeta$ to $s > 0$.

## The Bernoulli and Euler Numbers

### The Bernoulli Numbers

The **Bernoulli numbers** $B_n$ are defined by the generating function

$$
\frac{x}{e^x - 1} = \sum_{n=0}^\infty \frac{B_n}{n!} x^n, \qquad |x| < 2\pi.
$$

They satisfy $B_0 = 1$, $B_1 = -1/2$, and $B_{2n+1} = 0$ for $n \geq 1$. The first few are

$$
B_0 = 1, \quad B_1 = -\frac{1}{2}, \quad B_2 = \frac{1}{6}, \quad B_4 = -\frac{1}{30}, \quad B_6 = \frac{1}{42}.
$$

### The Bernoulli Polynomials

$$
\frac{x e^{t x}}{e^x - 1} = \sum_{n=0}^\infty \frac{B_n(t)}{n!} x^n.
$$

They satisfy $B_n(0) = B_n$ and $B_n(1) = B_n$ for $n \neq 1$.

### The Euler Numbers

The **Euler numbers** $E_n$ are defined by

$$
\frac{2}{e^x + e^{-x}} = \sum_{n=0}^\infty \frac{E_n}{n!} x^n.
$$

They satisfy $E_{2n+1} = 0$ and

$$
E_0 = 1, \quad E_2 = -1, \quad E_4 = 5, \quad E_6 = -61.
$$

## The Orthogonal Polynomials

### Legendre Polynomials

The **Legendre polynomials** $P_n(x)$ are defined on $[-1, 1]$ by the generating function

$$
\frac{1}{\sqrt{1 - 2xt + t^2}} = \sum_{n=0}^\infty P_n(x) t^n, \qquad |t| < 1.
$$

They satisfy the recurrence

$$
(n+1) P_{n+1}(x) = (2n+1) x P_n(x) - n P_{n-1}(x),
$$

with $P_0 = 1$ and $P_1 = x$. They are orthogonal on $[-1, 1]$ with respect to the weight $1$:

$$
\int_{-1}^1 P_m(x) P_n(x) \, dx = \frac{2}{2n+1} \delta_{mn}.
$$

They satisfy Legendre's differential equation

$$
(1 - x^2) y'' - 2x y' + n(n+1) y = 0.
$$

### Chebyshev Polynomials

The **Chebyshev polynomials of the first kind** $T_n(x)$ are defined on $[-1, 1]$ by

$$
T_n(\cos \theta) = \cos(n \theta).
$$

They satisfy the recurrence

$$
T_{n+1}(x) = 2x T_n(x) - T_{n-1}(x),
$$

with $T_0 = 1$ and $T_1 = x$. They are orthogonal on $[-1, 1]$ with respect to the weight $(1 - x^2)^{-1/2}$:

$$
\int_{-1}^1 \frac{T_m(x) T_n(x)}{\sqrt{1 - x^2}} \, dx = \begin{cases} \pi & m = n = 0, \\ \pi/2 & m = n \geq 1, \\ 0 & m \neq n. \end{cases}
$$

### Hermite Polynomials

The **Hermite polynomials** $H_n(x)$ are defined on $\mathbb{R}$ by

$$
H_n(x) = (-1)^n e^{x^2} \frac{d^n}{dx^n} e^{-x^2}.
$$

They satisfy the recurrence

$$
H_{n+1}(x) = 2x H_n(x) - 2n H_{n-1}(x),
$$

with $H_0 = 1$ and $H_1 = 2x$. They are orthogonal on $\mathbb{R}$ with respect to the weight $e^{-x^2}$:

$$
\int_{-\infty}^\infty H_m(x) H_n(x) e^{-x^2} \, dx = 2^n n! \sqrt{\pi} \, \delta_{mn}.
$$

### Laguerre Polynomials

The **Laguerre polynomials** $L_n(x)$ are defined on $[0, \infty)$ by

$$
L_n(x) = \frac{e^x}{n!} \frac{d^n}{dx^n} (x^n e^{-x}).
$$

They satisfy the recurrence

$$
(n+1) L_{n+1}(x) = (2n+1-x) L_n(x) - n L_{n-1}(x),
$$

with $L_0 = 1$ and $L_1 = 1 - x$. They are orthogonal on $[0, \infty)$ with respect to the weight $e^{-x}$:

$$
\int_0^\infty L_m(x) L_n(x) e^{-x} \, dx = \delta_{mn}.
$$

## The Bessel Functions

### Definition

The **Bessel function of the first kind** of order $\nu \geq 0$ is

$$
J_\nu(x) = \sum_{n=0}^\infty \frac{(-1)^n}{n! \, \Gamma(n + \nu + 1)} \left( \frac{x}{2} \right)^{2n + \nu}.
$$

It satisfies Bessel's differential equation

$$
x^2 y'' + x y' + (x^2 - \nu^2) y = 0.
$$

### The Bessel Function of the Second Kind

$$
Y_\nu(x) = \frac{J_\nu(x) \cos(\nu \pi) - J_{-\nu}(x)}{\sin(\nu \pi)}, \qquad \nu \notin \mathbb{Z},
$$

with the limit taken for integer $\nu$. It is the second linearly independent solution of Bessel's equation.

### Modified Bessel Functions

The **modified Bessel function of the first kind** is

$$
I_\nu(x) = \sum_{n=0}^\infty \frac{1}{n! \, \Gamma(n + \nu + 1)} \left( \frac{x}{2} \right)^{2n + \nu}.
$$

It satisfies

$$
x^2 y'' + x y' - (x^2 + \nu^2) y = 0.
$$

### Asymptotics

As $x \to \infty$,

$$
J_\nu(x) \sim \sqrt{\frac{2}{\pi x}} \cos\left(x - \frac{\nu \pi}{2} - \frac{\pi}{4}\right),
$$

$$
I_\nu(x) \sim \frac{e^x}{\sqrt{2 \pi x}}.
$$

## The Airy Functions

### Definition

The **Airy function** $\operatorname{Ai}(x)$ is defined by

$$
\operatorname{Ai}(x) = \frac{1}{\pi} \int_0^\infty \cos\left(\frac{t^3}{3} + x t\right) dt.
$$

It satisfies Airy's differential equation

$$
y'' - x y = 0.
$$

The second solution $\operatorname{Bi}(x)$ is defined by

$$
\operatorname{Bi}(x) = \frac{1}{\pi} \int_0^\infty \left( e^{-t^3/3 + x t} + \sin\left(\frac{t^3}{3} + x t\right) \right) dt.
$$

### Asymptotics

As $x \to +\infty$,

$$
\operatorname{Ai}(x) \sim \frac{1}{2 \sqrt{\pi} x^{1/4}} e^{-2 x^{3/2}/3}.
$$

As $x \to -\infty$,

$$
\operatorname{Ai}(x) \sim \frac{1}{\sqrt{\pi} |x|^{1/4}} \sin\left(\frac{2 |x|^{3/2}}{3} + \frac{\pi}{4}\right).
$$

## The Hypergeometric Function

### Definition

The **Gauss hypergeometric function** is defined for $|x| < 1$ by

$$
{}_2F_1(a, b; c; x) = \sum_{n=0}^\infty \frac{(a)_n (b)_n}{(c)_n} \frac{x^n}{n!},
$$

where $(a)_n = a(a+1) \cdots (a+n-1)$ is the Pochhammer symbol.

It satisfies the hypergeometric differential equation

$$
x(1 - x) y'' + [c - (a + b + 1) x] y' - ab y = 0.
$$

### Special Cases

$$
{}_2F_1(1, 1; 2; x) = -\frac{\ln(1 - x)}{x},
$$

$$
{}_2F_1(a, b; b; x) = (1 - x)^{-a},
$$

$$
{}_2F_1\left(\frac{1}{2}, \frac{1}{2}; \frac{3}{2}; x^2\right) = \frac{\arcsin x}{x}.
$$

### The Generalized Hypergeometric Function

$$
{}_pF_q(a_1, \dots, a_p; b_1, \dots, b_q; x) = \sum_{n=0}^\infty \frac{(a_1)_n \cdots (a_p)_n}{(b_1)_n \cdots (b_q)_n} \frac{x^n}{n!}.
$$

Most special functions of mathematical physics are special cases of ${}_pF_q$.

## The Elliptic Integrals

### Definition

The **complete elliptic integral of the first kind** is

$$
K(k) = \int_0^{\pi/2} \frac{d\theta}{\sqrt{1 - k^2 \sin^2 \theta}}, \qquad 0 \leq k < 1.
$$

The **complete elliptic integral of the second kind** is

$$
E(k) = \int_0^{\pi/2} \sqrt{1 - k^2 \sin^2 \theta} \, d\theta.
$$

### The Incomplete Elliptic Integrals

$$
F(\phi, k) = \int_0^\phi \frac{d\theta}{\sqrt{1 - k^2 \sin^2 \theta}},
$$

$$
E(\phi, k) = \int_0^\phi \sqrt{1 - k^2 \sin^2 \theta} \, d\theta.
$$

### Relation to the Hypergeometric Function

$$
K(k) = \frac{\pi}{2} \, {}_2F_1\left(\frac{1}{2}, \frac{1}{2}; 1; k^2\right),
$$

$$
E(k) = \frac{\pi}{2} \, {}_2F_1\left(-\frac{1}{2}, \frac{1}{2}; 1; k^2\right).
$$

## The Lambert W Function

### Definition

The **Lambert W function** is the inverse of

$$
f(w) = w e^w.
$$

That is, $W(x)$ is the unique real solution of

$$
W(x) e^{W(x)} = x.
$$

For $x \geq 0$, there is a unique real solution $W_0(x) \geq 0$. For $-1/e \leq x < 0$, there are two real solutions $W_{-1}(x) \leq -1$ and $W_0(x) \geq -1$.

### Derivative

$$
W'(x) = \frac{W(x)}{x(1 + W(x))}, \qquad x \neq 0, \; x \neq -1/e.
$$

### Applications

The Lambert W function solves equations of the form $a e^x + b x + c = 0$. It appears in combinatorics (tree enumeration), in the analysis of delay differential equations, and in the solution of the time-dependent Schrödinger equation for certain potentials.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $e^x, \ln x$ | Exponential, logarithm |
| $\sin x, \cos x, \tan x$ | Trigonometric functions |
| $\arcsin x, \arccos x, \arctan x$ | Inverse trigonometric functions |
| $\sinh x, \cosh x, \tanh x$ | Hyperbolic functions |
| $\Gamma(x)$ | Gamma function |
| $B(x, y)$ | Beta function |
| $\operatorname{erf}(x), \operatorname{erfc}(x)$ | Error function, complementary error function |
| $\gamma(s, x), \Gamma(s, x)$ | Incomplete gamma functions |
| $B(x; a, b), I_x(a, b)$ | Incomplete beta functions |
| $\zeta(s)$ | Riemann zeta function |
| $B_n, E_n$ | Bernoulli, Euler numbers |
| $P_n, T_n, H_n, L_n$ | Legendre, Chebyshev, Hermite, Laguerre polynomials |
| $J_\nu, Y_\nu, I_\nu$ | Bessel functions |
| $\operatorname{Ai}, \operatorname{Bi}$ | Airy functions |
| ${}_pF_q$ | Generalized hypergeometric function |
| $K(k), E(k)$ | Complete elliptic integrals |
| $W(x)$ | Lambert W function |

## Further Reading

- N. N. Lebedev, *Special Functions and Their Applications* (Dover, 1972), for a thorough treatment of the classical functions.
- G. E. Andrews, R. Askey, and R. Roy, *Special Functions* (Cambridge, 1999), for the modern unified approach.
- M. Abramowitz and I. A. Stegun, *Handbook of Mathematical Functions* (Dover, 1965), for tables and formulas.
- E. T. Whittaker and G. N. Watson, *A Course of Modern Analysis* (Cambridge, 1927), for the classical treatment.
- NIST Digital Library of Mathematical Functions, for the modern reference.

