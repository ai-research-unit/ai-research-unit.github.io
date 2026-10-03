
# __Complex Special Functions__

## Introduction

This article introduces the complex special functions as a collection of named functions that arise repeatedly in complex analysis and differential equations. The goal is to define each function precisely, establish its basic properties, and describe the relations among them.

The treatment is mathematically honest: every claim is either proved or stated as a definition. Complex analysis is assumed: holomorphic functions, contour integrals, the Cauchy integral formula, Laurent series, and residues are used throughout. The order of presentation follows the dependency order: the complex exponential and its consequences first, then functions defined from them, then functions defined by series and integrals.

## The Complex Exponential and Logarithm

### The Complex Exponential

The **complex exponential** is defined for $A \in \mathbb{C}$ by

$$
\exp(A) = \sum_{n=0}^\infty \frac{A^n}{n!}.
$$

The series converges absolutely for every $A$. The function is entire, and it satisfies

$$
\exp(A + B) = \exp(A) \exp(B), \qquad \exp(0) = 1, \qquad \exp'(A) = \exp(A).
$$

For $A = a + i a'$ with $a, a' \in \mathbb{R}$,

$$
\exp(A) = e^a (\cos a' + i \sin a').
$$

This is **Euler's formula**, and it is the bridge between the exponential and the trigonometric functions. In particular, for $a' = \theta$,

$$
e^{i\theta} = \cos\theta + i \sin\theta.
$$

The exponential is $2\pi i$-periodic: $\exp(A + 2\pi i) = \exp(A)$.

### The Complex Logarithm

The **complex logarithm** is the multivalued inverse of the exponential:

$$
\log A = \ln|A| + i \arg A, \qquad A \neq 0.
$$

The argument is defined modulo $2\pi$, so the logarithm is defined modulo $2\pi i$. The **principal branch** is

$$
\operatorname{Log} A = \ln|A| + i \operatorname{Arg} A, \qquad -\pi < \operatorname{Arg} A \leq \pi.
$$

It is holomorphic on $\mathbb{C} \setminus (-\infty, 0]$, with derivative $1/A$. The branch cut along the negative real axis is the price of single-valuedness.

### Complex Powers

For $a \in \mathbb{C}$ and $A \neq 0$,

$$
A^a = \exp(a \log A).
$$

This is multivalued in general. The principal branch is obtained by using the principal branch of the logarithm.

## The Trigonometric and Hyperbolic Functions

### Trigonometric Functions

The **complex sine** and **cosine** are defined by

$$
\sin A = \frac{e^{iA} - e^{-iA}}{2i}, \qquad \cos A = \frac{e^{iA} + e^{-iA}}{2}.
$$

Both are entire. They satisfy

$$
\sin' A = \cos A, \qquad \cos' A = -\sin A,
$$

$$
\sin(A + B) = \sin A \cos B + \cos A \sin B,
$$

$$
\cos(A + B) = \cos A \cos B - \sin A \sin B,
$$

$$
\sin^2 A + \cos^2 A = 1.
$$

They are $2\pi$-periodic, and their zeros are real: $\sin A = 0$ iff $A = n\pi$, $\cos A = 0$ iff $A = \pi/2 + n\pi$.

**Unboundedness.** Unlike the real case, $\sin$ and $\cos$ are unbounded on $\mathbb{C}$. For $A = i a'$ with $a' \in \mathbb{R}$,

$$
\sin(i a') = i \sinh a', \qquad \cos(i a') = \cosh a'.
$$

### Hyperbolic Functions

The **complex hyperbolic sine** and **cosine** are defined by

$$
\sinh A = \frac{e^A - e^{-A}}{2}, \qquad \cosh A = \frac{e^A + e^{-A}}{2}.
$$

Both are entire, and they satisfy

$$
\sinh' A = \cosh A, \qquad \cosh' A = \sinh A,
$$

$$
\cosh^2 A - \sinh^2 A = 1.
$$

The relation between the trigonometric and hyperbolic functions is

$$
\sin(iA) = i \sinh A, \qquad \cos(iA) = \cosh A,
$$

$$
\sinh(iA) = i \sin A, \qquad \cosh(iA) = \cos A.
$$

### Other Trigonometric and Hyperbolic Functions

$$
\tan A = \frac{\sin A}{\cos A}, \qquad \cot A = \frac{\cos A}{\sin A},
$$

$$
\tanh A = \frac{\sinh A}{\cosh A}, \qquad \coth A = \frac{\cosh A}{\sinh A}.
$$

These are meromorphic, with poles where the denominator vanishes.

### Inverse Trigonometric Functions

The **complex arcsine** is defined by

$$
\arcsin A = -i \log\left( iA + \sqrt{1 - A^2} \right),
$$

where the square root and logarithm are multivalued. The **complex arctangent** is

$$
\arctan A = \frac{1}{2i} \log \frac{1 + iA}{1 - iA}.
$$

Both are multivalued, and both have branch cuts determined by the branch choices of the square root and logarithm.

## The Gamma Function

### Definition

The **gamma function** is defined for $\operatorname{Re} A > 0$ by

$$
\Gamma(A) = \int_0^\infty t^{A-1} e^{-t} \, dt.
$$

The integral converges absolutely for $\operatorname{Re} A > 0$ and defines a holomorphic function on that half-plane.

### Analytic Continuation

The functional equation

$$
\Gamma(A + 1) = A \Gamma(A)
$$

extends $\Gamma$ meromorphically to all of $\mathbb{C}$, with simple poles at $A = 0, -1, -2, \dots$ and residues

$$
\operatorname{Res}(\Gamma, -n) = \frac{(-1)^n}{n!}.
$$

The extended function has no zeros. It satisfies $\Gamma(n + 1) = n!$ for non-negative integers $n$.

### The Weierstrass Product

$$
\frac{1}{\Gamma(A)} = A e^{\gamma A} \prod_{n=1}^\infty \left( 1 + \frac{A}{n} \right) e^{-A/n},
$$

where $\gamma$ is the Euler–Mascheroni constant. This product converges uniformly on compact subsets of $\mathbb{C}$ and shows that $1/\Gamma$ is entire with zeros at $A = 0, -1, -2, \dots$.

### Reflection and Duplication

$$
\Gamma(A) \Gamma(1 - A) = \frac{\pi}{\sin(\pi A)},
$$

$$
\Gamma(A) \Gamma\left(A + \tfrac{1}{2}\right) = 2^{1-2A} \sqrt{\pi} \, \Gamma(2A).
$$

The reflection formula shows that $\Gamma$ has no zeros, since $1/\Gamma$ is entire and the right side has no zeros.

### The Beta Function

The **beta function** is defined for $\operatorname{Re} a > 0$, $\operatorname{Re} b > 0$ by

$$
B(a, b) = \int_0^1 t^{a-1} (1 - t)^{b-1} \, dt.
$$

It satisfies

$$
B(a, b) = \frac{\Gamma(a) \Gamma(b)}{\Gamma(a + b)}.
$$

**Proof.** Substitute $t = u/(1+u)$ in the beta integral, then use the gamma integral representation for each factor.

It is symmetric: $B(a, b) = B(b, a)$.

### Stirling's Formula

As $|A| \to \infty$ with $|\arg A| < \pi$,

$$
\Gamma(A) \sim \sqrt{2\pi} \, A^{A - 1/2} e^{-A}.
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
\gamma(s, A) = \int_0^A t^{s-1} e^{-t} \, dt, \qquad \operatorname{Re} s > 0.
$$

The **upper incomplete gamma function** is

$$
\Gamma(s, A) = \int_A^\infty t^{s-1} e^{-t} \, dt, \qquad \operatorname{Re} s > 0,
$$

where the integral is along a ray from $A$ to infinity avoiding the negative real axis. They satisfy

$$
\gamma(s, A) + \Gamma(s, A) = \Gamma(s).
$$

Both extend meromorphically in $s$ and are entire in $A$.

### The Regularized Incomplete Gamma Functions

$$
P(s, A) = \frac{\gamma(s, A)}{\Gamma(s)}, \qquad Q(s, A) = \frac{\Gamma(s, A)}{\Gamma(s)}.
$$

These satisfy $P + Q = 1$.

### The Incomplete Beta Function

$$
B(A; a, b) = \int_0^A t^{a-1} (1 - t)^{b-1} \, dt, \qquad \operatorname{Re} a > 0, \; \operatorname{Re} b > 0,
$$

where the integral is along a path from $0$ to $A$ avoiding the branch points $0$ and $1$. The **regularized incomplete beta function** is

$$
I_A(a, b) = \frac{B(A; a, b)}{B(a, b)}.
$$

It satisfies $I_0(a, b) = 0$ and $I_1(a, b) = 1$, and it extends meromorphically in $a$ and $b$.

## The Error Function

### Definition

The **error function** is defined by

$$
\operatorname{erf}(A) = \frac{2}{\sqrt{\pi}} \int_0^A e^{-t^2} \, dt.
$$

The integral is along any path from $0$ to $A$. The integrand is entire, so $\operatorname{erf}$ is entire. It is odd, and it satisfies

$$
\operatorname{erf}'(A) = \frac{2}{\sqrt{\pi}} e^{-A^2}.
$$

### The Complementary Error Function

$$
\operatorname{erfc}(A) = 1 - \operatorname{erf}(A) = \frac{2}{\sqrt{\pi}} \int_A^\infty e^{-t^2} \, dt.
$$

The integral is along a ray from $A$ to infinity avoiding the essential singularity at infinity.

### Asymptotics

As $|A| \to \infty$ with $|\arg A| < 3\pi/4$,

$$
\operatorname{erfc}(A) \sim \frac{e^{-A^2}}{\sqrt{\pi} A}.
$$

This asymptotic expansion is used in the theory of the heat equation and in probability.

## The Orthogonal Polynomials

### Legendre Polynomials

The **Legendre polynomials** $P_n(A)$ are defined by the generating function

$$
\frac{1}{\sqrt{1 - 2At + t^2}} = \sum_{n=0}^\infty P_n(A) t^n, \qquad |t| < 1,
$$

where the square root is the principal branch. They satisfy the recurrence

$$
(n+1) P_{n+1}(A) = (2n+1) A P_n(A) - n P_{n-1}(A),
$$

with $P_0 = 1$ and $P_1 = A$. They satisfy Legendre's differential equation

$$
(1 - A^2) w'' - 2A w' + n(n+1) w = 0.
$$

They are orthogonal on $[-1, 1]$ with respect to the weight $1$:

$$
\int_{-1}^1 P_m(a) P_n(a) \, da = \frac{2}{2n+1} \delta_{mn}.
$$

### Chebyshev Polynomials

The **Chebyshev polynomials of the first kind** $T_n(A)$ are defined by

$$
T_n(A) = \cos(n \arccos A),
$$

where the arccos is the principal branch. They satisfy the recurrence

$$
T_{n+1}(A) = 2A T_n(A) - T_{n-1}(A),
$$

with $T_0 = 1$ and $T_1 = A$. They are orthogonal on $[-1, 1]$ with respect to the weight $(1 - a^2)^{-1/2}$:

$$
\int_{-1}^1 \frac{T_m(a) T_n(a)}{\sqrt{1 - a^2}} \, da = \begin{cases} \pi & m = n = 0, \\ \pi/2 & m = n \geq 1, \\ 0 & m \neq n. \end{cases}
$$

### Hermite Polynomials

The **Hermite polynomials** $H_n(A)$ are defined by

$$
H_n(A) = (-1)^n e^{A^2} \frac{d^n}{dA^n} e^{-A^2}.
$$

They satisfy the recurrence

$$
H_{n+1}(A) = 2A H_n(A) - 2n H_{n-1}(A),
$$

with $H_0 = 1$ and $H_1 = 2A$. They are orthogonal on $\mathbb{R}$ with respect to the weight $e^{-a^2}$:

$$
\int_{-\infty}^\infty H_m(a) H_n(a) e^{-a^2} \, da = 2^n n! \sqrt{\pi} \, \delta_{mn}.
$$

### Laguerre Polynomials

The **Laguerre polynomials** $L_n(A)$ are defined by

$$
L_n(A) = \frac{e^A}{n!} \frac{d^n}{dA^n} (A^n e^{-A}).
$$

They satisfy the recurrence

$$
(n+1) L_{n+1}(A) = (2n+1-A) L_n(A) - n L_{n-1}(A),
$$

with $L_0 = 1$ and $L_1 = 1 - A$. They are orthogonal on $[0, \infty)$ with respect to the weight $e^{-a}$:

$$
\int_0^\infty L_m(a) L_n(a) e^{-a} \, da = \delta_{mn}.
$$

## The Bessel Functions

### Definition

The **Bessel function of the first kind** of order $\nu$ is

$$
J_\nu(A) = \sum_{n=0}^\infty \frac{(-1)^n}{n! \, \Gamma(n + \nu + 1)} \left( \frac{A}{2} \right)^{2n + \nu}.
$$

The series converges absolutely for all $A$, so $A^{-\nu} J_\nu(A)$ is entire. It satisfies Bessel's differential equation

$$
A^2 w'' + A w' + (A^2 - \nu^2) w = 0.
$$

### The Bessel Function of the Second Kind

$$
Y_\nu(A) = \frac{J_\nu(A) \cos(\nu \pi) - J_{-\nu}(A)}{\sin(\nu \pi)}, \qquad \nu \notin \mathbb{Z},
$$

with the limit taken for integer $\nu$. It is the second linearly independent solution of Bessel's equation. It has a branch point at $A = 0$.

### Modified Bessel Functions

The **modified Bessel function of the first kind** is

$$
I_\nu(A) = \sum_{n=0}^\infty \frac{1}{n! \, \Gamma(n + \nu + 1)} \left( \frac{A}{2} \right)^{2n + \nu}.
$$

It satisfies

$$
A^2 w'' + A w' - (A^2 + \nu^2) w = 0.
$$

### Integral Representations

For $\operatorname{Re} \nu > -1/2$,

$$
J_\nu(A) = \frac{1}{\sqrt{\pi} \, \Gamma(\nu + 1/2)} \left( \frac{A}{2} \right)^\nu \int_{-1}^1 (1 - t^2)^{\nu - 1/2} e^{iAt} \, dt.
$$

This representation is the source of most asymptotic estimates.

### Asymptotics

As $|A| \to \infty$ with $|\arg A| < \pi$,

$$
J_\nu(A) \sim \sqrt{\frac{2}{\pi A}} \cos\left(A - \frac{\nu \pi}{2} - \frac{\pi}{4}\right),
$$

$$
I_\nu(A) \sim \frac{e^A}{\sqrt{2 \pi A}}, \qquad |\arg A| < \frac{\pi}{2}.
$$

## The Airy Functions

### Definition

The **Airy function** $\operatorname{Ai}(A)$ is defined by the contour integral

$$
\operatorname{Ai}(A) = \frac{1}{2\pi i} \int_C \exp\left(\frac{t^3}{3} - At\right) dt,
$$

where $C$ is a contour in the complex plane that starts at infinity along the ray $\arg t = -\pi/3$ and ends at infinity along the ray $\arg t = \pi/3$. The integral converges because of the cubic term.

It satisfies Airy's differential equation

$$
w'' - A w = 0.
$$

The second solution $\operatorname{Bi}(A)$ is defined by a similar contour integral with a different contour.

### Asymptotics

As $|A| \to \infty$ with $|\arg A| < \pi$,

$$
\operatorname{Ai}(A) \sim \frac{1}{2 \sqrt{\pi} A^{1/4}} e^{-2 A^{3/2}/3}.
$$

As $|A| \to \infty$ with $|\arg(-A)| < 2\pi/3$,

$$
\operatorname{Ai}(A) \sim \frac{1}{\sqrt{\pi} (-A)^{1/4}} \sin\left(\frac{2 (-A)^{3/2}}{3} + \frac{\pi}{4}\right).
$$

The Airy functions are the simplest example of functions with a Stokes phenomenon: the asymptotic expansion changes form across certain rays in the complex plane.

## The Hypergeometric Function

### Definition

The **Gauss hypergeometric function** is defined for $|A| < 1$ by

$$
{}_2F_1(a, b; c; A) = \sum_{n=0}^\infty \frac{(a)_n (b)_n}{(c)_n} \frac{A^n}{n!},
$$

where $(a)_n = a(a+1) \cdots (a+n-1)$ is the Pochhammer symbol. The series converges for $|A| < 1$ and extends analytically to $\mathbb{C} \setminus [1, \infty)$.

It satisfies the hypergeometric differential equation

$$
A(1 - A) w'' + [c - (a + b + 1) A] w' - ab w = 0.
$$

### Integral Representation

For $\operatorname{Re} c > \operatorname{Re} b > 0$,

$$
{}_2F_1(a, b; c; A) = \frac{\Gamma(c)}{\Gamma(b) \Gamma(c - b)} \int_0^1 t^{b-1} (1 - t)^{c-b-1} (1 - At)^{-a} \, dt.
$$

The integral is along a path from $0$ to $1$ avoiding the branch point at $t = 1/A$.

### Special Cases

$$
{}_2F_1(1, 1; 2; A) = -\frac{\log(1 - A)}{A},
$$

$$
{}_2F_1(a, b; b; A) = (1 - A)^{-a},
$$

$$
{}_2F_1\left(\frac{1}{2}, \frac{1}{2}; \frac{3}{2}; A^2\right) = \frac{\arcsin A}{A}.
$$

### The Generalized Hypergeometric Function

$$
{}_pF_q(a_1, \dots, a_p; b_1, \dots, b_q; A) = \sum_{n=0}^\infty \frac{(a_1)_n \cdots (a_p)_n}{(b_1)_n \cdots (b_q)_n} \frac{A^n}{n!}.
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

The **Weierstrass elliptic function** $\wp(A)$ is defined by

$$
\wp(A) = \frac{1}{A^2} + \sum_{(m, n) \neq (0, 0)} \left( \frac{1}{(A - m\omega_1 - n\omega_2)^2} - \frac{1}{(m\omega_1 + n\omega_2)^2} \right),
$$

where $\omega_1, \omega_2$ are the periods. It is meromorphic and doubly periodic, and it satisfies the differential equation

$$
\wp'(A)^2 = 4 \wp(A)^3 - g_2 \wp(A) - g_3.
$$

Elliptic functions are the inverse functions of elliptic integrals, and they are the natural setting for the theory of doubly periodic meromorphic functions.

## The Lambert W Function

### Definition

The **Lambert W function** is the multivalued inverse of

$$
f(B) = B e^B.
$$

That is, $W(A)$ is any solution of

$$
W(A) e^{W(A)} = A.
$$

The function has infinitely many branches $W_k(A)$ for $k \in \mathbb{Z}$, with branch points at $A = 0$ and $A = -1/e$.

### Derivative

$$
W'(A) = \frac{W(A)}{A(1 + W(A))}, \qquad A \neq 0, \; A \neq -1/e.
$$

### Applications

The Lambert W function solves equations of the form $a e^A + b A + c = 0$. It appears in combinatorics (tree enumeration), in the analysis of delay differential equations, and in the inversion of the iterated exponential $c^c = a$, where $c = e^{W(\ln a)}$.

## Summary

The complex special functions are the named functions that recur in complex analysis and in differential equations. The exponential is defined by its series and is entire, and the trigonometric and hyperbolic functions are built from it; the logarithm is its multivalued inverse and is the first function of the article whose domain is more than the plane.

Integral representations supply the next family: the gamma function as $\Gamma(A) = \int_0^\infty t^{A-1}e^{-t}\,dt$ for $\operatorname{Re} A > 0$ together with its analytic continuation, the Riemann zeta function as the Dirichlet series that continues meromorphically, and the incomplete gamma and beta functions that refine them. The error function, the orthogonal polynomials and the Bessel functions carry the same pattern to integrals and to the solutions of the classical differential equations.

The article closes with the higher transcendental functions: the Airy functions as contour integrals, the Gauss hypergeometric function ${}_2F_1(a,b;c;A)$ and its analytic continuation, the elliptic integrals and elliptic functions, and the Lambert $W$ function as the multivalued inverse of $B \mapsto Be^B$. Each is defined precisely, and its elementary properties, its differential equation and its relations to the others are recorded.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A = a + i a'$ | Complex variable |
| $e^A, \log A$ | Complex exponential, logarithm |
| $\sin A, \cos A, \tan A$ | Complex trigonometric functions |
| $\sinh A, \cosh A, \tanh A$ | Complex hyperbolic functions |
| $\Gamma(A)$ | Gamma function |
| $B(a, b)$ | Beta function |
| $\zeta(s)$ | Riemann zeta function |
| $\gamma(s, A), \Gamma(s, A)$ | Incomplete gamma functions |
| $B(A; a, b), I_A(a, b)$ | Incomplete beta functions |
| $\operatorname{erf}(A), \operatorname{erfc}(A)$ | Error function, complementary error function |
| $P_n, T_n, H_n, L_n$ | Legendre, Chebyshev, Hermite, Laguerre polynomials |
| $J_\nu, Y_\nu, I_\nu$ | Bessel functions |
| $\operatorname{Ai}, \operatorname{Bi}$ | Airy functions |
| ${}_pF_q$ | Generalized hypergeometric function |
| $K(k), E(k)$ | Complete elliptic integrals |
| $\wp(A)$ | Weierstrass elliptic function |
| $W_k(A)$ | Lambert W function, branch $k$ |

## Further Reading

- E. T. Whittaker and G. N. Watson, *A Course of Modern Analysis* (Cambridge, 1927), for the classical treatment.
- N. N. Lebedev, *Special Functions and Their Applications* (Dover, 1972), for a thorough treatment of the classical functions.
- G. E. Andrews, R. Askey, and R. Roy, *Special Functions* (Cambridge, 1999), for the modern unified approach.
- M. Abramowitz and I. A. Stegun, *Handbook of Mathematical Functions* (Dover, 1965), for tables and formulas.
- F. W. J. Olver, A. B. Olde Daalhuis, D. W. Lozier and others (eds.), *NIST Digital Library of Mathematical Functions* (National Institute of Standards and Technology, 2010–), for the modern reference.

