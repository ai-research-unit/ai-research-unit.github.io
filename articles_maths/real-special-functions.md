
# __Real Special Functions__

## Introduction

This article introduces the real special functions as a collection of named functions that arise repeatedly in analysis and differential equations. The goal is to define each function precisely, establish its basic properties, and describe the relations among them.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No complex analysis is invoked. All functions are treated as functions of a real variable, and all integral representations are real integrals. The order of presentation follows the dependency order: elementary functions first, then functions defined from them, then functions defined from those.

## The Exponential and Logarithm

### Definition

The **exponential function** is defined for $a \in \mathbb{R}$ by

$$
\exp(a) = \sum_{n=0}^\infty \frac{a^n}{n!}.
$$

The series converges absolutely for every $a$. The function is smooth, strictly increasing, and satisfies

$$
\exp(a + b) = \exp(a) \exp(b), \qquad \exp(0) = 1, \qquad \exp'(a) = \exp(a).
$$

We write $e^a = \exp(a)$ where $e = \exp(1)$.

### The Logarithm

The **natural logarithm** is the inverse of the exponential:

$$
\ln a = \int_1^a \frac{dt}{t}, \qquad a > 0.
$$

It satisfies

$$
\ln(ab) = \ln a + \ln b, \qquad \ln 1 = 0, \qquad (\ln a)' = \frac{1}{a}.
$$

### General Powers

For $c > 0$ and $a \in \mathbb{R}$,

$$
c^a = \exp(a \ln c).
$$

This is consistent with integer and rational powers and extends them continuously to all real exponents.

## The Trigonometric Functions

### Definition

The **sine** and **cosine** functions are defined by

$$
\sin a = \sum_{n=0}^\infty \frac{(-1)^n a^{2n+1}}{(2n+1)!}, \qquad \cos a = \sum_{n=0}^\infty \frac{(-1)^n a^{2n}}{(2n)!}.
$$

Both series converge absolutely for every $a$. They satisfy

$$
\sin' a = \cos a, \qquad \cos' a = -\sin a,
$$

$$
\sin(a + b) = \sin a \cos b + \cos a \sin b,
$$

$$
\cos(a + b) = \cos a \cos b - \sin a \sin b,
$$

$$
\sin^2 a + \cos^2 a = 1.
$$

### Periodicity

The number $\pi$ is defined as twice the smallest positive zero of $\cos$. Both functions are $2\pi$-periodic:

$$
\sin(a + 2\pi) = \sin a, \qquad \cos(a + 2\pi) = \cos a.
$$

### The Other Trigonometric Functions

$$
\tan a = \frac{\sin a}{\cos a}, \qquad \cot a = \frac{\cos a}{\sin a},
$$

$$
\sec a = \frac{1}{\cos a}, \qquad \csc a = \frac{1}{\sin a}.
$$

Each is defined wherever the denominator is non-zero.

### Inverse Trigonometric Functions

The **arcsine** is the inverse of $\sin$ on $[-\pi/2, \pi/2]$:

$$
\arcsin a = \int_0^a \frac{dt}{\sqrt{1 - t^2}}, \qquad -1 \leq a \leq 1.
$$

The **arccosine** is the inverse of $\cos$ on $[0, \pi]$:

$$
\arccos a = \frac{\pi}{2} - \arcsin a.
$$

The **arctangent** is the inverse of $\tan$ on $(-\pi/2, \pi/2)$:

$$
\arctan a = \int_0^a \frac{dt}{1 + t^2}, \qquad a \in \mathbb{R}.
$$

It satisfies

$$
\arctan a + \arctan \frac{1}{a} = \frac{\pi}{2}, \qquad a > 0.
$$

## The Hyperbolic Functions

### Definition

The **hyperbolic sine** and **hyperbolic cosine** are

$$
\sinh a = \frac{e^a - e^{-a}}{2}, \qquad \cosh a = \frac{e^a + e^{-a}}{2}.
$$

They satisfy

$$
\sinh' a = \cosh a, \qquad \cosh' a = \sinh a,
$$

$$
\cosh^2 a - \sinh^2 a = 1,
$$

$$
\sinh(a + b) = \sinh a \cosh b + \cosh a \sinh b,
$$

$$
\cosh(a + b) = \cosh a \cosh b + \sinh a \sinh b.
$$

### The Other Hyperbolic Functions

$$
\tanh a = \frac{\sinh a}{\cosh a}, \qquad \coth a = \frac{\cosh a}{\sinh a},
$$

$$
\operatorname{sech} a = \frac{1}{\cosh a}, \qquad \operatorname{csch} a = \frac{1}{\sinh a}.
$$

### Inverse Hyperbolic Functions

$$
\operatorname{arsinh} a = \ln\left(a + \sqrt{a^2 + 1}\right), \qquad a \in \mathbb{R},
$$

$$
\operatorname{arcosh} a = \ln\left(a + \sqrt{a^2 - 1}\right), \qquad a \geq 1,
$$

$$
\operatorname{artanh} a = \frac{1}{2} \ln \frac{1 + a}{1 - a}, \qquad -1 < a < 1.
$$

## The Gamma and Beta Functions

### The Gamma Function

The **gamma function** is defined for $a > 0$ by

$$
\Gamma(a) = \int_0^\infty t^{a-1} e^{-t} \, dt.
$$

It satisfies the **functional equation**

$$
\Gamma(a + 1) = a \Gamma(a),
$$

which follows from integration by parts. Since $\Gamma(1) = 1$, this gives

$$
\Gamma(n + 1) = n!
$$

for non-negative integers $n$. The gamma function is the unique logarithmically convex function on $(0, \infty)$ satisfying $\Gamma(1) = 1$ and $\Gamma(a + 1) = a \Gamma(a)$, by the Bohr–Mollerup theorem.

**Reflection formula.**

$$
\Gamma(a) \Gamma(1 - a) = \frac{\pi}{\sin(\pi a)}, \qquad 0 < a < 1.
$$

**Duplication formula.**

$$
\Gamma(a) \Gamma\left(a + \tfrac{1}{2}\right) = 2^{1-2a} \sqrt{\pi} \, \Gamma(2a).
$$

### The Beta Function

The **beta function** is defined for $a, b > 0$ by

$$
B(a, b) = \int_0^1 t^{a-1} (1 - t)^{b-1} \, dt.
$$

It satisfies

$$
B(a, b) = \frac{\Gamma(a) \Gamma(b)}{\Gamma(a + b)}.
$$

**Proof.** Substitute $t = u/(1+u)$ in the beta integral, then use the gamma integral representation for each factor.

It is symmetric: $B(a, b) = B(b, a)$.

## The Error Function and Related Functions

### The Error Function

The **error function** is defined by

$$
\operatorname{erf}(a) = \frac{2}{\sqrt{\pi}} \int_0^a e^{-t^2} \, dt.
$$

It is odd, strictly increasing, and satisfies

$$
\lim_{a \to \infty} \operatorname{erf}(a) = 1, \qquad \lim_{a \to -\infty} \operatorname{erf}(a) = -1.
$$

### The Complementary Error Function

$$
\operatorname{erfc}(a) = 1 - \operatorname{erf}(a) = \frac{2}{\sqrt{\pi}} \int_a^\infty e^{-t^2} \, dt.
$$

### The Imaginary Error Function

$$
\operatorname{erfi}(a) = \frac{2}{\sqrt{\pi}} \int_0^a e^{t^2} \, dt.
$$

### The Dawson Function

$$
D(a) = e^{-a^2} \int_0^a e^{t^2} \, dt.
$$

It satisfies the differential equation

$$
D'(a) + 2a D(a) = 1.
$$

### The Fresnel Integrals

$$
S(a) = \int_0^a \sin\left(\frac{\pi t^2}{2}\right) dt, \qquad C(a) = \int_0^a \cos\left(\frac{\pi t^2}{2}\right) dt.
$$

Both converge as $a \to \infty$, with

$$
\lim_{a \to \infty} S(a) = \lim_{a \to \infty} C(a) = \frac{1}{2}.
$$

## The Incomplete Gamma and Beta Functions

### The Incomplete Gamma Function

The **lower incomplete gamma function** is

$$
\gamma(s, a) = \int_0^a t^{s-1} e^{-t} \, dt, \qquad s > 0, \; a \geq 0.
$$

The **upper incomplete gamma function** is

$$
\Gamma(s, a) = \int_a^\infty t^{s-1} e^{-t} \, dt, \qquad s > 0, \; a \geq 0.
$$

They satisfy

$$
\gamma(s, a) + \Gamma(s, a) = \Gamma(s).
$$

### The Regularized Incomplete Gamma Functions

$$
P(s, a) = \frac{\gamma(s, a)}{\Gamma(s)}, \qquad Q(s, a) = \frac{\Gamma(s, a)}{\Gamma(s)}.
$$

These satisfy $P + Q = 1$ and take values in $[0, 1]$.

### The Incomplete Beta Function

$$
B(c; a, b) = \int_0^c t^{a-1} (1 - t)^{b-1} \, dt, \qquad 0 \leq c \leq 1, \; a, b > 0.
$$

The **regularized incomplete beta function** is

$$
I_c(a, b) = \frac{B(c; a, b)}{B(a, b)}.
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
\frac{a}{e^a - 1} = \sum_{n=0}^\infty \frac{B_n}{n!} a^n, \qquad |a| < 2\pi.
$$

They satisfy $B_0 = 1$, $B_1 = -1/2$, and $B_{2n+1} = 0$ for $n \geq 1$. The first few are

$$
B_0 = 1, \quad B_1 = -\frac{1}{2}, \quad B_2 = \frac{1}{6}, \quad B_4 = -\frac{1}{30}, \quad B_6 = \frac{1}{42}.
$$

### The Bernoulli Polynomials

$$
\frac{a e^{t a}}{e^a - 1} = \sum_{n=0}^\infty \frac{B_n(t)}{n!} a^n.
$$

They satisfy $B_n(0) = B_n$ and $B_n(1) = B_n$ for $n \neq 1$.

### The Euler Numbers

The **Euler numbers** $E_n$ are defined by

$$
\frac{2}{e^a + e^{-a}} = \sum_{n=0}^\infty \frac{E_n}{n!} a^n.
$$

They satisfy $E_{2n+1} = 0$ and

$$
E_0 = 1, \quad E_2 = -1, \quad E_4 = 5, \quad E_6 = -61.
$$

## The Orthogonal Polynomials

### Legendre Polynomials

The **Legendre polynomials** $P_n(a)$ are defined on $[-1, 1]$ by the generating function

$$
\frac{1}{\sqrt{1 - 2at + t^2}} = \sum_{n=0}^\infty P_n(a) t^n, \qquad |t| < 1.
$$

They satisfy the recurrence

$$
(n+1) P_{n+1}(a) = (2n+1) a P_n(a) - n P_{n-1}(a),
$$

with $P_0 = 1$ and $P_1 = a$. They are orthogonal on $[-1, 1]$ with respect to the weight $1$:

$$
\int_{-1}^1 P_m(a) P_n(a) \, da = \frac{2}{2n+1} \delta_{mn}.
$$

They satisfy Legendre's differential equation

$$
(1 - a^2) w'' - 2a w' + n(n+1) w = 0.
$$

### Chebyshev Polynomials

The **Chebyshev polynomials of the first kind** $T_n(a)$ are defined on $[-1, 1]$ by

$$
T_n(\cos \theta) = \cos(n \theta).
$$

They satisfy the recurrence

$$
T_{n+1}(a) = 2a T_n(a) - T_{n-1}(a),
$$

with $T_0 = 1$ and $T_1 = a$. They are orthogonal on $[-1, 1]$ with respect to the weight $(1 - a^2)^{-1/2}$:

$$
\int_{-1}^1 \frac{T_m(a) T_n(a)}{\sqrt{1 - a^2}} \, da = \begin{cases} \pi & m = n = 0, \\ \pi/2 & m = n \geq 1, \\ 0 & m \neq n. \end{cases}
$$

### Hermite Polynomials

The **Hermite polynomials** $H_n(a)$ are defined on $\mathbb{R}$ by

$$
H_n(a) = (-1)^n e^{a^2} \frac{d^n}{da^n} e^{-a^2}.
$$

They satisfy the recurrence

$$
H_{n+1}(a) = 2a H_n(a) - 2n H_{n-1}(a),
$$

with $H_0 = 1$ and $H_1 = 2a$. They are orthogonal on $\mathbb{R}$ with respect to the weight $e^{-a^2}$:

$$
\int_{-\infty}^\infty H_m(a) H_n(a) e^{-a^2} \, da = 2^n n! \sqrt{\pi} \, \delta_{mn}.
$$

### Laguerre Polynomials

The **Laguerre polynomials** $L_n(a)$ are defined on $[0, \infty)$ by

$$
L_n(a) = \frac{e^a}{n!} \frac{d^n}{da^n} (a^n e^{-a}).
$$

They satisfy the recurrence

$$
(n+1) L_{n+1}(a) = (2n+1-a) L_n(a) - n L_{n-1}(a),
$$

with $L_0 = 1$ and $L_1 = 1 - a$. They are orthogonal on $[0, \infty)$ with respect to the weight $e^{-a}$:

$$
\int_0^\infty L_m(a) L_n(a) e^{-a} \, da = \delta_{mn}.
$$

## The Bessel Functions

### Definition

The **Bessel function of the first kind** of order $\nu \geq 0$ is

$$
J_\nu(a) = \sum_{n=0}^\infty \frac{(-1)^n}{n! \, \Gamma(n + \nu + 1)} \left( \frac{a}{2} \right)^{2n + \nu}.
$$

The powers are real for every $a$ when $\nu$ is an integer; when $\nu$ is not an integer they are real only for $a > 0$, which is therefore the domain of the real function $J_\nu$ in that case.

It satisfies Bessel's differential equation

$$
a^2 w'' + a w' + (a^2 - \nu^2) w = 0.
$$

### The Bessel Function of the Second Kind

$$
Y_\nu(a) = \frac{J_\nu(a) \cos(\nu \pi) - J_{-\nu}(a)}{\sin(\nu \pi)}, \qquad \nu \notin \mathbb{Z},
$$

with the limit taken for integer $\nu$. It is the second linearly independent solution of Bessel's equation.

### Modified Bessel Functions

The **modified Bessel function of the first kind** is

$$
I_\nu(a) = \sum_{n=0}^\infty \frac{1}{n! \, \Gamma(n + \nu + 1)} \left( \frac{a}{2} \right)^{2n + \nu},
$$

with the same domain convention as for $J_\nu$: all real $a$ when $\nu$ is an integer, and $a > 0$ otherwise.

It satisfies

$$
a^2 w'' + a w' - (a^2 + \nu^2) w = 0.
$$

### Asymptotics

As $a \to \infty$,

$$
J_\nu(a) \sim \sqrt{\frac{2}{\pi a}} \cos\left(a - \frac{\nu \pi}{2} - \frac{\pi}{4}\right),
$$

$$
I_\nu(a) \sim \frac{e^a}{\sqrt{2 \pi a}}.
$$

## The Airy Functions

### Definition

The **Airy function** $\operatorname{Ai}(a)$ is defined by

$$
\operatorname{Ai}(a) = \frac{1}{\pi} \int_0^\infty \cos\left(\frac{t^3}{3} + a t\right) dt.
$$

It satisfies Airy's differential equation

$$
w'' - a w = 0.
$$

The second solution $\operatorname{Bi}(a)$ is defined by

$$
\operatorname{Bi}(a) = \frac{1}{\pi} \int_0^\infty \left( e^{-t^3/3 + a t} + \sin\left(\frac{t^3}{3} + a t\right) \right) dt.
$$

### Asymptotics

As $a \to +\infty$,

$$
\operatorname{Ai}(a) \sim \frac{1}{2 \sqrt{\pi} a^{1/4}} e^{-2 a^{3/2}/3}.
$$

As $a \to -\infty$,

$$
\operatorname{Ai}(a) \sim \frac{1}{\sqrt{\pi} |a|^{1/4}} \sin\left(\frac{2 |a|^{3/2}}{3} + \frac{\pi}{4}\right).
$$

## The Hypergeometric Function

### Definition

The **Gauss hypergeometric function** is defined for $|d| < 1$ by

$$
{}_2F_1(a, b; c; d) = \sum_{n=0}^\infty \frac{(a)_n (b)_n}{(c)_n} \frac{d^n}{n!},
$$

where $(a)_n = a(a+1) \cdots (a+n-1)$ is the Pochhammer symbol.

It satisfies the hypergeometric differential equation

$$
d(1 - d) w'' + [c - (a + b + 1) d] w' - ab w = 0.
$$

### Special Cases

$$
{}_2F_1(1, 1; 2; a) = -\frac{\ln(1 - a)}{a},
$$

$$
{}_2F_1(a, b; b; c) = (1 - c)^{-a},
$$

$$
{}_2F_1\left(\frac{1}{2}, \frac{1}{2}; \frac{3}{2}; a^2\right) = \frac{\arcsin a}{a}.
$$

### The Generalized Hypergeometric Function

$$
{}_pF_q(a_1, \dots, a_p; b_1, \dots, b_q; c) = \sum_{n=0}^\infty \frac{(a_1)_n \cdots (a_p)_n}{(b_1)_n \cdots (b_q)_n} \frac{c^n}{n!}.
$$

Most named special functions are special cases of ${}_pF_q$.

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

That is, $W(a)$ is the unique real solution of

$$
W(a) e^{W(a)} = a.
$$

For $a \geq 0$, there is a unique real solution $W_0(a) \geq 0$. For $-1/e \leq a < 0$, there are two real solutions $W_{-1}(a) \leq -1$ and $W_0(a) \geq -1$.

### Derivative

$$
W'(a) = \frac{W(a)}{a(1 + W(a))}, \qquad a \neq 0, \; a \neq -1/e.
$$

### Applications

The Lambert W function solves equations of the form $a e^d + b d + c = 0$. It appears in combinatorics, in the enumeration of labelled trees, and in the analysis of delay differential equations.

## Summary

The real special functions are the named functions that recur throughout analysis and in differential equations, and they are the base case from which the special functions of every other system of the corpus are obtained.

The elementary functions come first: the exponential, defined by its series, its inverse the logarithm, the trigonometric functions defined by their series, and the hyperbolic functions defined from the exponential. Integral representations then supply the higher functions: the gamma and beta functions with the functional equation, the error function and its relatives, the incomplete gamma and beta functions, and the Riemann zeta function as a Dirichlet series.

The arithmetic families follow, the Bernoulli and Euler numbers defined by generating functions, and then the classical special functions of analysis and mathematical physics: the orthogonal polynomials, the Bessel functions, the Airy function, the Gauss hypergeometric function, the elliptic integrals, and the Lambert $W$ function as the inverse of $w \mapsto we^w$. Each function is defined precisely, and its elementary properties, its differential equation, its recurrence relations and its relations to the others are recorded.

## Summary of Notation

| symbol | meaning |
|---|---|
| $e^a, \ln a$ | Exponential, logarithm |
| $\sin a, \cos a, \tan a$ | Trigonometric functions |
| $\arcsin a, \arccos a, \arctan a$ | Inverse trigonometric functions |
| $\sinh a, \cosh a, \tanh a$ | Hyperbolic functions |
| $\Gamma(a)$ | Gamma function |
| $B(a, b)$ | Beta function |
| $\operatorname{erf}(a), \operatorname{erfc}(a)$ | Error function, complementary error function |
| $\gamma(s, a), \Gamma(s, a)$ | Incomplete gamma functions |
| $B(c; a, b), I_c(a, b)$ | Incomplete beta functions |
| $\zeta(s)$ | Riemann zeta function |
| $B_n, E_n$ | Bernoulli, Euler numbers |
| $P_n, T_n, H_n, L_n$ | Legendre, Chebyshev, Hermite, Laguerre polynomials |
| $J_\nu, Y_\nu, I_\nu$ | Bessel functions |
| $\operatorname{Ai}, \operatorname{Bi}$ | Airy functions |
| ${}_pF_q$ | Generalized hypergeometric function |
| $K(k), E(k)$ | Complete elliptic integrals |
| $W(a)$ | Lambert W function |

## Further Reading

- N. N. Lebedev, *Special Functions and Their Applications* (Dover, 1972), for a thorough treatment of the classical functions.
- G. E. Andrews, R. Askey, and R. Roy, *Special Functions* (Cambridge, 1999), for the modern unified approach.
- M. Abramowitz and I. A. Stegun, *Handbook of Mathematical Functions* (Dover, 1965), for tables and formulas.
- E. T. Whittaker and G. N. Watson, *A Course of Modern Analysis* (Cambridge, 1927), for the classical treatment.
- NIST Digital Library of Mathematical Functions, for the modern reference.

