# __Complex Special Functions__

## Introduction

This article introduces the complex special functions as a collection of named functions that arise repeatedly in complex analysis and differential equations. The goal is to define each function precisely, establish its basic properties, and describe the relations among them.

The treatment is mathematically honest: every claim is either proved or stated as a definition. Complex analysis is assumed: holomorphic functions, contour integrals, the Cauchy integral formula, Laurent series, and residues are used throughout. The order of presentation follows the dependency order: the complex exponential and its consequences first, then functions defined from them, then functions defined by series and integrals.

## The Complex Exponential and Logarithm

### The Complex Exponential

The **complex exponential** is defined for $z \in \mathbb{C}$ by

$$
\exp(z) = \sum_{n=0}^\infty \frac{z^n}{n!}.
$$

The series converges absolutely for every $z$. The function is entire, and it satisfies

$$
\exp(z + w) = \exp(z) \exp(w), \qquad \exp(0) = 1, \qquad \exp'(z) = \exp(z).
$$

For $z = x + iy$ with $x, y \in \mathbb{R}$,

$$
\exp(z) = e^x (\cos y + i \sin y).
$$

This is **Euler's formula**, and it is the bridge between the exponential and the trigonometric functions. In particular, for $y = \theta$,

$$
e^{i\theta} = \cos\theta + i \sin\theta.
$$

The exponential is $2\pi i$-periodic: $\exp(z + 2\pi i) = \exp(z)$.

### The Complex Logarithm

The **complex logarithm** is the multivalued inverse of the exponential:

$$
\log z = \ln|z| + i \arg z, \qquad z \neq 0.
$$

The argument is defined modulo $2\pi$, so the logarithm is defined modulo $2\pi i$. The **principal branch** is

$$
\operatorname{Log} z = \ln|z| + i \operatorname{Arg} z, \qquad -\pi < \operatorname{Arg} z \leq \pi.
$$

It is holomorphic on $\mathbb{C} \setminus (-\infty, 0]$, with derivative $1/z$. The branch cut along the negative real axis is the price of single-valuedness.

### Complex Powers

For $a \in \mathbb{C}$ and $z \neq 0$,

$$
z^a = \exp(a \log z).
$$

This is multivalued in general. The principal branch is obtained by using the principal branch of the logarithm.

## The Trigonometric and Hyperbolic Functions

### Trigonometric Functions

The **complex sine** and **cosine** are defined by

$$
\sin z = \frac{e^{iz} - e^{-iz}}{2i}, \qquad \cos z = \frac{e^{iz} + e^{-iz}}{2}.
$$

Both are entire. They satisfy

$$
\sin' z = \cos z, \qquad \cos' z = -\sin z,
$$

$$
\sin(z + w) = \sin z \cos w + \cos z \sin w,
$$

$$
\cos(z + w) = \cos z \cos w - \sin z \sin w,
$$

$$
\sin^2 z + \cos^2 z = 1.
$$

They are $2\pi$-periodic, and their zeros are real: $\sin z = 0$ iff $z = n\pi$, $\cos z = 0$ iff $z = \pi/2 + n\pi$.

**Unboundedness.** Unlike the real case, $\sin$ and $\cos$ are unbounded on $\mathbb{C}$. For $z = iy$ with $y \in \mathbb{R}$,

$$
\sin(iy) = i \sinh y, \qquad \cos(iy) = \cosh y.
$$

### Hyperbolic Functions

The **complex hyperbolic sine** and **cosine** are defined by

$$
\sinh z = \frac{e^z - e^{-z}}{2}, \qquad \cosh z = \frac{e^z + e^{-z}}{2}.
$$

Both are entire, and they satisfy

$$
\sinh' z = \cosh z, \qquad \cosh' z = \sinh z,
$$

$$
\cosh^2 z - \sinh^2 z = 1.
$$

The relation between the trigonometric and hyperbolic functions is

$$
\sin(iz) = i \sinh z, \qquad \cos(iz) = \cosh z,
$$

$$
\sinh(iz) = i \sin z, \qquad \cosh(iz) = \cos z.
$$

### Other Trigonometric and Hyperbolic Functions

$$
\tan z = \frac{\sin z}{\cos z}, \qquad \cot z = \frac{\cos z}{\sin z},
$$

$$
\tanh z = \frac{\sinh z}{\cosh z}, \qquad \coth z = \frac{\cosh z}{\sinh z}.
$$

These are meromorphic, with poles where the denominator vanishes.

### Inverse Trigonometric Functions

The **complex arcsine** is defined by

$$
\arcsin z = -i \log\left( iz + \sqrt{1 - z^2} \right),
$$

where the square root and logarithm are multivalued. The **complex arctangent** is

$$
\arctan z = \frac{1}{2i} \log \frac{1 + iz}{1 - iz}.
$$

Both are multivalued, and both have branch cuts determined by the branch choices of the square root and logarithm.

## The Gamma Function

### Definition

The **gamma function** is defined for $\operatorname{Re} z > 0$ by

$$
\Gamma(z) = \int_0^\infty t^{z-1} e^{-t} \, dt.
$$

The integral converges absolutely for $\operatorname{Re} z > 0$ and defines a holomorphic function on that half-plane.

### Analytic Continuation

The functional equation

$$
\Gamma(z + 1) = z \Gamma(z)
$$

extends $\Gamma$ meromorphically to all of $\mathbb{C}$, with simple poles at $z = 0, -1, -2, \dots$ and residues

$$
\operatorname{Res}(\Gamma, -n) = \frac{(-1)^n}{n!}.
$$

The extended function has no zeros. It satisfies $\Gamma(n + 1) = n!$ for non-negative integers $n$.

### The Weierstrass Product

$$
\frac{1}{\Gamma(z)} = z e^{\gamma z} \prod_{n=1}^\infty \left( 1 + \frac{z}{n} \right) e^{-z/n},
$$

where $\gamma$ is the Euler–Mascheroni constant. This product converges uniformly on compact subsets of $\mathbb{C}$ and shows that $1/\Gamma$ is entire with zeros at $z = 0, -1, -2, \dots$.

### Reflection and Duplication

$$
\Gamma(z) \Gamma(1 - z) = \frac{\pi}{\sin(\pi z)},
$$

$$
\Gamma(z) \Gamma\left(z + \tfrac{1}{2}\right) = 2^{1-2z} \sqrt{\pi} \, \Gamma(2z).
$$

The reflection formula shows that $\Gamma$ has no zeros, since $1/\Gamma$ is entire and the right side has no zeros.

### The Beta Function

The **beta function** is defined for $\operatorname{Re} x > 0$, $\operatorname{Re} y > 0$ by

$$
B(x, y) = \int_0^1 t^{x-1} (1 - t)^{y-1} \, dt.
$$

It satisfies

$$
B(x, y) = \frac{\Gamma(x) \Gamma(y)}{\Gamma(x + y)}.
$$

**Proof.** Substitute $t = u/(1+u)$ in the beta integral, then use the gamma integral representation for each factor. $\square$

It is symmetric: $B(x, y) = B(y, x)$.

### Stirling's Formula

As $|z| \to \infty$ with $|\arg z| < \pi$,

$$
\Gamma(z) \sim \sqrt{2\pi} \, z^{z - 1/2} e^{-z}.
$$

This is the asymptotic expansion of the gamma function, and it is the source of most estimates involving factorials and binomial coefficients.

## The Riemann Zeta Function

### Definition

The **Riemann zeta function** is defined for $\operatorname{Re} s > 1$ by

$$
\zeta(s) = \sum_{n=1}^\infty \frac{1}{n^s}.
$$

The series converges absolutely for $\operatorname{Re} s > 1$ and defines a holomorphic function on that half-plane.

### Analytic Continuation

The zeta function extends meromorphically to all of $\mathbb{C}$, with a single simple pole at $s = 1$ with residue $1$. The continuation is given by the functional equation

$$
\zeta(s) = 2^s \pi^{s-1} \sin\left(\frac{\pi s}{2}\right) \Gamma(1 - s) \zeta(1 - s),
$$

which relates $\zeta(s)$ to $\zeta(1-s)$.

### The Euler Product

For $\operatorname{Re} s > 1$,

$$
\zeta(s) = \prod_p \frac{1}{1 - p^{-s}},
$$

where the product is over all primes $p$. This is the analytic form of the fundamental theorem of arithmetic, and it is the starting point of analytic number theory.

### Special Values

$$
\zeta(2) = \frac{\pi^2}{6}, \qquad \zeta(4) = \frac{\pi^4}{90}, \qquad \zeta(2n) = \frac{(-1)^{n+1} B_{2n} (2\pi)^{2n}}{2 (2n)!},
$$

where $B_{2n}$ are the Bernoulli numbers. The values at negative integers are

$$
\zeta(-n) = (-1)^n \frac{B_{n+1}}{n+1}, \qquad n \geq 0.
$$

In particular, $\zeta(0) = -1/2$ and $\zeta(-1) = -1/12$.

### The Riemann Hypothesis

The **Riemann hypothesis** states that all non-trivial zeros of $\zeta$ lie on the critical line $\operatorname{Re} s = 1/2$. It is the most famous open problem in mathematics, and it is equivalent to a sharp estimate on the error term in the prime number theorem.

## The Incomplete Gamma and Beta Functions

### The Incomplete Gamma Function

The **lower incomplete gamma function** is

$$
\gamma(s, z) = \int_0^z t^{s-1} e^{-t} \, dt, \qquad \operatorname{Re} s > 0.
$$

The **upper incomplete gamma function** is

$$
\Gamma(s, z) = \int_z^\infty t^{s-1} e^{-t} \, dt, \qquad \operatorname{Re} s > 0,
$$

where the integral is along a ray from $z$ to infinity avoiding the negative real axis. They satisfy

$$
\gamma(s, z) + \Gamma(s, z) = \Gamma(s).
$$

Both extend meromorphically in $s$ and are entire in $z$.

### The Regularized Incomplete Gamma Functions

$$
P(s, z) = \frac{\gamma(s, z)}{\Gamma(s)}, \qquad Q(s, z) = \frac{\Gamma(s, z)}{\Gamma(s)}.
$$

These satisfy $P + Q = 1$.

### The Incomplete Beta Function

$$
B(z; a, b) = \int_0^z t^{a-1} (1 - t)^{b-1} \, dt, \qquad \operatorname{Re} a > 0, \; \operatorname{Re} b > 0,
$$

where the integral is along a path from $0$ to $z$ avoiding the branch points $0$ and $1$. The **regularized incomplete beta function** is

$$
I_z(a, b) = \frac{B(z; a, b)}{B(a, b)}.
$$

It satisfies $I_0(a, b) = 0$ and $I_1(a, b) = 1$, and it extends meromorphically in $a$ and $b$.

## The Error Function

### Definition

The **error function** is defined by

$$
\operatorname{erf}(z) = \frac{2}{\sqrt{\pi}} \int_0^z e^{-t^2} \, dt.
$$

The integral is along any path from $0$ to $z$. The integrand is entire, so $\operatorname{erf}$ is entire. It is odd, and it satisfies

$$
\operatorname{erf}'(z) = \frac{2}{\sqrt{\pi}} e^{-z^2}.
$$

### The Complementary Error Function

$$
\operatorname{erfc}(z) = 1 - \operatorname{erf}(z) = \frac{2}{\sqrt{\pi}} \int_z^\infty e^{-t^2} \, dt.
$$

The integral is along a ray from $z$ to infinity avoiding the essential singularity at infinity.

### Asymptotics

As $|z| \to \infty$ with $|\arg z| < 3\pi/4$,

$$
\operatorname{erfc}(z) \sim \frac{e^{-z^2}}{\sqrt{\pi} z}.
$$

This asymptotic expansion is used in the theory of the heat equation and in probability.

## The Orthogonal Polynomials

### Legendre Polynomials

The **Legendre polynomials** $P_n(z)$ are defined by the generating function

$$
\frac{1}{\sqrt{1 - 2zt + t^2}} = \sum_{n=0}^\infty P_n(z) t^n, \qquad |t| < 1,
$$

where the square root is the principal branch. They satisfy the recurrence

$$
(n+1) P_{n+1}(z) = (2n+1) z P_n(z) - n P_{n-1}(z),
$$

with $P_0 = 1$ and $P_1 = z$. They satisfy Legendre's differential equation

$$
(1 - z^2) y'' - 2z y' + n(n+1) y = 0.
$$

They are orthogonal on $[-1, 1]$ with respect to the weight $1$:

$$
\int_{-1}^1 P_m(x) P_n(x) \, dx = \frac{2}{2n+1} \delta_{mn}.
$$

### Chebyshev Polynomials

The **Chebyshev polynomials of the first kind** $T_n(z)$ are defined by

$$
T_n(z) = \cos(n \arccos z),
$$

where the arccos is the principal branch. They satisfy the recurrence

$$
T_{n+1}(z) = 2z T_n(z) - T_{n-1}(z),
$$

with $T_0 = 1$ and $T_1 = z$. They are orthogonal on $[-1, 1]$ with respect to the weight $(1 - x^2)^{-1/2}$:

$$
\int_{-1}^1 \frac{T_m(x) T_n(x)}{\sqrt{1 - x^2}} \, dx = \begin{cases} \pi & m = n = 0, \\ \pi/2 & m = n \geq 1, \\ 0 & m \neq n. \end{cases}
$$

### Hermite Polynomials

The **Hermite polynomials** $H_n(z)$ are defined by

$$
H_n(z) = (-1)^n e^{z^2} \frac{d^n}{dz^n} e^{-z^2}.
$$

They satisfy the recurrence

$$
H_{n+1}(z) = 2z H_n(z) - 2n H_{n-1}(z),
$$

with $H_0 = 1$ and $H_1 = 2z$. They are orthogonal on $\mathbb{R}$ with respect to the weight $e^{-x^2}$:

$$
\int_{-\infty}^\infty H_m(x) H_n(x) e^{-x^2} \, dx = 2^n n! \sqrt{\pi} \, \delta_{mn}.
$$

### Laguerre Polynomials

The **Laguerre polynomials** $L_n(z)$ are defined by

$$
L_n(z) = \frac{e^z}{n!} \frac{d^n}{dz^n} (z^n e^{-z}).
$$

They satisfy the recurrence

$$
(n+1) L_{n+1}(z) = (2n+1-z) L_n(z) - n L_{n-1}(z),
$$

with $L_0 = 1$ and $L_1 = 1 - z$. They are orthogonal on $[0, \infty)$ with respect to the weight $e^{-x}$:

$$
\int_0^\infty L_m(x) L_n(x) e^{-x} \, dx = \delta_{mn}.
$$

## The Bessel Functions

### Definition

The **Bessel function of the first kind** of order $\nu$ is

$$
J_\nu(z) = \sum_{n=0}^\infty \frac{(-1)^n}{n! \, \Gamma(n + \nu + 1)} \left( \frac{z}{2} \right)^{2n + \nu}.
$$

The series converges absolutely for all $z$, so $z^{-\nu} J_\nu(z)$ is entire. It satisfies Bessel's differential equation

$$
z^2 y'' + z y' + (z^2 - \nu^2) y = 0.
$$

### The Bessel Function of the Second Kind

$$
Y_\nu(z) = \frac{J_\nu(z) \cos(\nu \pi) - J_{-\nu}(z)}{\sin(\nu \pi)}, \qquad \nu \notin \mathbb{Z},
$$

with the limit taken for integer $\nu$. It is the second linearly independent solution of Bessel's equation. It has a branch point at $z = 0$.

### Modified Bessel Functions

The **modified Bessel function of the first kind** is

$$
I_\nu(z) = \sum_{n=0}^\infty \frac{1}{n! \, \Gamma(n + \nu + 1)} \left( \frac{z}{2} \right)^{2n + \nu}.
$$

It satisfies

$$
z^2 y'' + z y' - (z^2 + \nu^2) y = 0.
$$

### Integral Representations

For $\operatorname{Re} \nu > -1/2$,

$$
J_\nu(z) = \frac{1}{\sqrt{\pi} \, \Gamma(\nu + 1/2)} \left( \frac{z}{2} \right)^\nu \int_{-1}^1 (1 - t^2)^{\nu - 1/2} e^{izt} \, dt.
$$

This representation is the source of most asymptotic estimates.

### Asymptotics

As $|z| \to \infty$ with $|\arg z| < \pi$,

$$
J_\nu(z) \sim \sqrt{\frac{2}{\pi z}} \cos\left(z - \frac{\nu \pi}{2} - \frac{\pi}{4}\right),
$$

$$
I_\nu(z) \sim \frac{e^z}{\sqrt{2 \pi z}}, \qquad |\arg z| < \frac{\pi}{2}.
$$

## The Airy Functions

### Definition

The **Airy function** $\operatorname{Ai}(z)$ is defined by the contour integral

$$
\operatorname{Ai}(z) = \frac{1}{2\pi i} \int_C \exp\left(\frac{t^3}{3} - zt\right) dt,
$$

where $C$ is a contour in the complex plane that starts at infinity along the ray $\arg t = -\pi/3$ and ends at infinity along the ray $\arg t = \pi/3$. The integral converges because of the cubic term.

It satisfies Airy's differential equation

$$
y'' - z y = 0.
$$

The second solution $\operatorname{Bi}(z)$ is defined by a similar contour integral with a different contour.

### Asymptotics

As $|z| \to \infty$ with $|\arg z| < \pi$,

$$
\operatorname{Ai}(z) \sim \frac{1}{2 \sqrt{\pi} z^{1/4}} e^{-2 z^{3/2}/3}.
$$

As $|z| \to \infty$ with $|\arg(-z)| < 2\pi/3$,

$$
\operatorname{Ai}(z) \sim \frac{1}{\sqrt{\pi} (-z)^{1/4}} \sin\left(\frac{2 (-z)^{3/2}}{3} + \frac{\pi}{4}\right).
$$

The Airy functions are the simplest example of functions with a Stokes phenomenon: the asymptotic expansion changes form across certain rays in the complex plane.

## The Hypergeometric Function

### Definition

The **Gauss hypergeometric function** is defined for $|z| < 1$ by

$$
{}_2F_1(a, b; c; z) = \sum_{n=0}^\infty \frac{(a)_n (b)_n}{(c)_n} \frac{z^n}{n!},
$$

where $(a)_n = a(a+1) \cdots (a+n-1)$ is the Pochhammer symbol. The series converges for $|z| < 1$ and extends analytically to $\mathbb{C} \setminus [1, \infty)$.

It satisfies the hypergeometric differential equation

$$
z(1 - z) y'' + [c - (a + b + 1) z] y' - ab y = 0.
$$

### Integral Representation

For $\operatorname{Re} c > \operatorname{Re} b > 0$,

$$
{}_2F_1(a, b; c; z) = \frac{\Gamma(c)}{\Gamma(b) \Gamma(c - b)} \int_0^1 t^{b-1} (1 - t)^{c-b-1} (1 - zt)^{-a} \, dt.
$$

The integral is along a path from $0$ to $1$ avoiding the branch point at $t = 1/z$.

### Special Cases

$$
{}_2F_1(1, 1; 2; z) = -\frac{\log(1 - z)}{z},
$$

$$
{}_2F_1(a, b; b; z) = (1 - z)^{-a},
$$

$$
{}_2F_1\left(\frac{1}{2}, \frac{1}{2}; \frac{3}{2}; z^2\right) = \frac{\arcsin z}{z}.
$$

### The Generalized Hypergeometric Function

$$
{}_pF_q(a_1, \dots, a_p; b_1, \dots, b_q; z) = \sum_{n=0}^\infty \frac{(a_1)_n \cdots (a_p)_n}{(b_1)_n \cdots (b_q)_n} \frac{z^n}{n!}.
$$

Most named special functions are special cases of ${}_pF_q$.

## The Elliptic Integrals and Elliptic Functions

### Complete Elliptic Integrals

The **complete elliptic integral of the first kind** is

$$
K(k) = \int_0^{\pi/2} \frac{d\theta}{\sqrt{1 - k^2 \sin^2 \theta}}, \qquad 0 \leq k < 1.
$$

The **complete elliptic integral of the second kind** is

$$
E(k) = \int_0^{\pi/2} \sqrt{1 - k^2 \sin^2 \theta} \, d\theta.
$$

Both extend analytically in $k$ to $\mathbb{C} \setminus \{\pm 1\}$.

### Relation to the Hypergeometric Function

$$
K(k) = \frac{\pi}{2} \, {}_2F_1\left(\frac{1}{2}, \frac{1}{2}; 1; k^2\right),
$$

$$
E(k) = \frac{\pi}{2} \, {}_2F_1\left(-\frac{1}{2}, \frac{1}{2}; 1; k^2\right).
$$

### Elliptic Functions

The **Weierstrass elliptic function** $\wp(z)$ is defined by

$$
\wp(z) = \frac{1}{z^2} + \sum_{(m, n) \neq (0, 0)} \left( \frac{1}{(z - m\omega_1 - n\omega_2)^2} - \frac{1}{(m\omega_1 + n\omega_2)^2} \right),
$$

where $\omega_1, \omega_2$ are the periods. It is meromorphic and doubly periodic, and it satisfies the differential equation

$$
\wp'(z)^2 = 4 \wp(z)^3 - g_2 \wp(z) - g_3.
$$

Elliptic functions are the inverse functions of elliptic integrals, and they are the natural setting for the theory of doubly periodic meromorphic functions.

## The Lambert W Function

### Definition

The **Lambert W function** is the multivalued inverse of

$$
f(w) = w e^w.
$$

That is, $W(z)$ is any solution of

$$
W(z) e^{W(z)} = z.
$$

The function has infinitely many branches $W_k(z)$ for $k \in \mathbb{Z}$, with branch points at $z = 0$ and $z = -1/e$.

### Derivative

$$
W'(z) = \frac{W(z)}{z(1 + W(z))}, \qquad z \neq 0, \; z \neq -1/e.
$$

### Applications

The Lambert W function solves equations of the form $a e^z + b z + c = 0$. It appears in combinatorics (tree enumeration), in the analysis of delay differential equations, and in the solution of the time-dependent Schrödinger equation for certain potentials.

## Summary

The complex special functions are the named functions that recur in complex analysis and in differential equations. The exponential is defined by its series and is entire, and the trigonometric and hyperbolic functions are built from it; the logarithm is its multivalued inverse and is the first function of the article whose domain is more than the plane.

Integral representations supply the next family: the gamma function as $\Gamma(z) = \int_0^\infty t^{z-1}e^{-t}\,dt$ for $\operatorname{Re} z > 0$ together with its analytic continuation, the Riemann zeta function as the Dirichlet series that continues meromorphically, and the incomplete gamma and beta functions that refine them. The error function, the orthogonal polynomials and the Bessel functions carry the same pattern to integrals and to the solutions of the classical differential equations.

The article closes with the higher transcendental functions: the Airy functions as contour integrals, the Gauss hypergeometric function ${}_2F_1(a,b;c;z)$ and its analytic continuation, the elliptic integrals and elliptic functions, and the Lambert $W$ function as the multivalued inverse of $w \mapsto we^w$. Each is defined precisely, and its elementary properties, its differential equation and its relations to the others are recorded.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $e^z, \log z$ | Complex exponential, logarithm |
| $\sin z, \cos z, \tan z$ | Complex trigonometric functions |
| $\sinh z, \cosh z, \tanh z$ | Complex hyperbolic functions |
| $\Gamma(z)$ | Gamma function |
| $B(x, y)$ | Beta function |
| $\zeta(s)$ | Riemann zeta function |
| $\gamma(s, z), \Gamma(s, z)$ | Incomplete gamma functions |
| $B(z; a, b), I_z(a, b)$ | Incomplete beta functions |
| $\operatorname{erf}(z), \operatorname{erfc}(z)$ | Error function, complementary error function |
| $P_n, T_n, H_n, L_n$ | Legendre, Chebyshev, Hermite, Laguerre polynomials |
| $J_\nu, Y_\nu, I_\nu$ | Bessel functions |
| $\operatorname{Ai}, \operatorname{Bi}$ | Airy functions |
| ${}_pF_q$ | Generalized hypergeometric function |
| $K(k), E(k)$ | Complete elliptic integrals |
| $\wp(z)$ | Weierstrass elliptic function |
| $W_k(z)$ | Lambert W function, branch $k$ |

## Further Reading

- E. T. Whittaker and G. N. Watson, *A Course of Modern Analysis* (Cambridge, 1927), for the classical treatment.
- N. N. Lebedev, *Special Functions and Their Applications* (Dover, 1972), for a thorough treatment of the classical functions.
- G. E. Andrews, R. Askey, and R. Roy, *Special Functions* (Cambridge, 1999), for the modern unified approach.
- M. Abramowitz and I. A. Stegun, *Handbook of Mathematical Functions* (Dover, 1965), for tables and formulas.
- NIST Digital Library of Mathematical Functions, for the modern reference.

