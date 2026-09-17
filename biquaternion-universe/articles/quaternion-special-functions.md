
# Quaternion Special Functions

## Introduction

This article introduces the quaternion special functions as a collection of named functions that arise in quaternion analysis, in Clifford analysis, and in the geometry of the quaternion space. The goal is to define each function precisely, establish its basic properties, and describe the relations among them.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. No examples are given. The quaternion algebra is assumed from the article on quaternion algebra, and the scalar-vector decomposition is used throughout. The order of presentation follows the dependency order: the quaternion exponential and its consequences first, then functions defined from them, then functions defined by series and integrals.

Throughout this article, the quaternion algebra is denoted $\mathbb{H}$, and its basis is $e_0 = 1, e_1, e_2, e_3$. The scalar imaginary of the complex numbers is denoted $i$, so that it does not collide with the quaternion units.

## The Quaternion Exponential and Logarithm

### The Quaternion Exponential

The **quaternion exponential** is defined for $q \in \mathbb{H}$ by

$$
\exp(q) = \sum_{n=0}^\infty \frac{q^n}{n!}.
$$

The series converges absolutely for every $q$, because the quaternion norm is submultiplicative. The function is entire in the quaternion sense, and it satisfies

$$
\exp(p + q) = \exp(p) \exp(q) \quad \text{only if } pq = qp,
$$

$$
\exp(0) = 1, \qquad \exp'(q) = \exp(q).
$$

**Caution.** The exponential is not multiplicative in general, because $\mathbb{H}$ is not commutative. The identity $\exp(p + q) = \exp(p) \exp(q)$ holds if and only if $p$ and $q$ commute.

For a pure quaternion $\mathbf{q} \in \mathbb{R}^3_{\mathbb{H}}$ with $|\mathbf{q}| = \theta$, the exponential is

$$
\exp(\mathbf{q}) = \cos\theta + \frac{\mathbf{q}}{\theta} \sin\theta.
$$

This is the **quaternion Euler formula**, and it is the bridge between the exponential and the trigonometric functions. In particular, for a unit pure quaternion $\omega$ and $\theta \in \mathbb{R}$,

$$
\exp(\omega \theta) = \cos\theta + \omega \sin\theta.
$$

This is a unit quaternion, and it lies on the unit sphere $\mathbb{S}^3$.

For a general quaternion $q = q_0 + \mathbf{q}$ with $\mathbf{q} \neq 0$ and $\theta = |\mathbf{q}|$,

$$
\exp(q) = e^{q_0} \left( \cos\theta + \frac{\mathbf{q}}{\theta} \sin\theta \right).
$$

So the exponential is the product of a real exponential and a unit quaternion. This is the quaternion analogue of the polar form of a complex number.

### The Quaternion Logarithm

The **quaternion logarithm** is the inverse of the exponential. It is defined for $q$ with $q \notin (-\infty, 0]$ by

$$
\log(q) = \log|q| + \frac{\mathbf{q}}{|\mathbf{q}|} \arccos\left(\frac{q_0}{|q|}\right).
$$

The logarithm is defined on the complement of the non-positive real axis, and it is single-valued on that domain. It satisfies

$$
\log(pq) = \log(p) + \log(q) \quad \text{only if } pq = qp,
$$

$$
\log(1) = 0, \qquad \log'(q) = q^{-1}.
$$

**Caution.** The logarithm is not additive in general, because $\mathbb{H}$ is not commutative. The identity $\log(pq) = \log(p) + \log(q)$ holds if and only if $p$ and $q$ commute.

### Quaternion Powers

For $a \in \mathbb{H}$ and $q$ in the domain of the logarithm,

$$
q^a = \exp(a \log q).
$$

This is single-valued on the domain of the logarithm. It satisfies

$$
q^{a + b} = q^a q^b \quad \text{only if } a \text{ and } b \text{ commute with } \log q.
$$

The power is not multiplicative in general, because $\mathbb{H}$ is not commutative.

## The Trigonometric and Hyperbolic Functions

### Trigonometric Functions

The **quaternion sine** and **cosine** are defined by

$$
\sin(q) = \frac{e^{e_1 q} - e^{-e_1 q}}{2 e_1}, \qquad \cos(q) = \frac{e^{e_1 q} + e^{-e_1 q}}{2},
$$

where $e_1$ is a fixed quaternion unit. These definitions depend on the choice of $e_1$, because $\mathbb{H}$ is not commutative. A more invariant definition uses the scalar-vector decomposition:

$$
\sin(q) = \sin(q_0) \cosh(|\mathbf{q}|) + \frac{\mathbf{q}}{|\mathbf{q}|} \cos(q_0) \sinh(|\mathbf{q}|),
$$

$$
\cos(q) = \cos(q_0) \cosh(|\mathbf{q}|) - \frac{\mathbf{q}}{|\mathbf{q}|} \sin(q_0) \sinh(|\mathbf{q}|).
$$

These functions are entire, and they satisfy

$$
\sin' = \cos, \qquad \cos' = -\sin,
$$

$$
\sin^2(q) + \cos^2(q) = 1.
$$

**Caution.** The addition formulas for the trigonometric functions do not hold in general, because $\mathbb{H}$ is not commutative. They hold only for commuting arguments.

### Hyperbolic Functions

The **quaternion hyperbolic sine** and **cosine** are defined by

$$
\sinh(q) = \frac{e^q - e^{-q}}{2}, \qquad \cosh(q) = \frac{e^q + e^{-q}}{2}.
$$

They are entire, and they satisfy

$$
\sinh' = \cosh, \qquad \cosh' = \sinh,
$$

$$
\cosh^2(q) - \sinh^2(q) = 1.
$$

The relation between the trigonometric and hyperbolic functions is the same as in the real case:

$$
\sin(e_1 q) = e_1 \sinh(q), \qquad \cos(e_1 q) = \cosh(q),
$$

where $e_1$ is a quaternion unit.

### Other Functions

$$
\tan(q) = \frac{\sin(q)}{\cos(q)}, \qquad \coth(q) = \frac{\cosh(q)}{\sinh(q)}.
$$

These are meromorphic in the quaternion sense, with singularities where the denominator is not invertible.

## The Quaternion Gamma Function

### Definition

The **quaternion gamma function** is defined for $q$ with $q_0 > 0$ by

$$
\Gamma(q) = \int_0^\infty t^{q-1} e^{-t} \, dt,
$$

where the integral is along the positive real axis, $t^{q-1}$ is the quaternion power, and $e^{-t}$ is the quaternion exponential. Because the integrand is a function of the real variable $t$ and the quaternion $q$ appears only in the exponent, the integral converges for $q_0 > 0$.

### Properties

$$
\Gamma(q + 1) = q \Gamma(q).
$$

This follows from integration by parts, exactly as in the real case, and it holds because the quaternion multiplication by $q$ commutes with the integration over the real variable $t$.

$$
\Gamma(n + 1) = n!
$$

for non-negative integers $n$, where the factorial is the ordinary real factorial.

### The Reflection Formula

$$
\Gamma(q) \Gamma(1 - q) = \frac{\pi}{\sin(\pi q)},
$$

where the sine is the quaternion sine. This follows from the real reflection formula, applied to the scalar-vector decomposition.

**Caution.** The reflection formula holds only for $q$ in the domain where both sides are defined, and the sine is the quaternion sine with the appropriate branch.

## The Quaternion Beta Function

### Definition

The **quaternion beta function** is defined for $p, q$ with $p_0 > 0$ and $q_0 > 0$ by

$$
B(p, q) = \int_0^1 t^{p-1} (1 - t)^{q-1} \, dt,
$$

where the integral is along the positive real axis and the powers are quaternion powers.

### Relation to the Gamma Function

$$
B(p, q) = \frac{\Gamma(p) \Gamma(q)}{\Gamma(p + q)}.
$$

This follows from the same substitution as in the real case, applied to the scalar-vector decomposition.

### Symmetry

$$
B(p, q) = B(q, p).
$$

## The Quaternion Error Function

### Definition

The **quaternion error function** is defined by

$$
\operatorname{erf}(q) = \frac{2}{\sqrt{\pi}} \int_0^q e^{-t^2} \, dt,
$$

where the integral is along a path from $0$ to $q$ that does not cross the singularities of the integrand, and the exponential is the quaternion exponential.

### Properties

$$
\operatorname{erf}'(q) = \frac{2}{\sqrt{\pi}} e^{-q^2},
$$

$$
\lim_{q \to \infty} \operatorname{erf}(q) = 1, \qquad \lim_{q \to -\infty} \operatorname{erf}(q) = -1,
$$

where the limits are taken along the real axis.

### The Complementary Error Function

$$
\operatorname{erfc}(q) = 1 - \operatorname{erf}(q) = \frac{2}{\sqrt{\pi}} \int_q^\infty e^{-t^2} \, dt.
$$

## The Quaternion Airy Function

### Definition

The **quaternion Airy function** is defined by the contour integral

$$
\operatorname{Ai}(q) = \frac{1}{2\pi i} \int_C \exp\left(\frac{t^3}{3} - qt\right) dt,
$$

where $C$ is a contour in the complex plane, the exponential is the quaternion exponential, and $q$ is a quaternion. Because the integrand is a function of the complex variable $t$ and the quaternion $q$ appears only in the exponent, the integral converges and defines an entire function of $q$.

### Differential Equation

$$
y'' - q y = 0.
$$

This is Airy's equation, and it holds in the quaternion sense.

### Asymptotics

For $q$ with $q_0 \to +\infty$ along the real axis,

$$
\operatorname{Ai}(q) \sim \frac{1}{2 \sqrt{\pi} q^{1/4}} e^{-2 q^{3/2}/3}.
$$

For $q$ with $q_0 \to -\infty$ along the real axis,

$$
\operatorname{Ai}(q) \sim \frac{1}{\sqrt{\pi} |q|^{1/4}} \sin\left(\frac{2 |q|^{3/2}}{3} + \frac{\pi}{4}\right).
$$

The same asymptotics hold for the vector part, with the appropriate modifications.

## The Quaternion Bessel Functions

### Definition

The **quaternion Bessel function** of the first kind of order $\nu$ is defined by

$$
J_\nu(q) = \sum_{n=0}^\infty \frac{(-1)^n}{n! \, \Gamma(n + \nu + 1)} \left( \frac{q}{2} \right)^{2n + \nu},
$$

where the power and the gamma function are quaternion. The series converges absolutely for all $q$, because the quaternion norm is submultiplicative.

### Differential Equation

$$
q^2 y'' + q y' + (q^2 - \nu^2) y = 0.
$$

This is Bessel's equation, and it holds in the quaternion sense.

### Modified Bessel Functions

The **quaternion modified Bessel function** of the first kind is

$$
I_\nu(q) = \sum_{n=0}^\infty \frac{1}{n! \, \Gamma(n + \nu + 1)} \left( \frac{q}{2} \right)^{2n + \nu}.
$$

It satisfies

$$
q^2 y'' + q y' - (q^2 + \nu^2) y = 0.
$$

### The Relation to the Dirac Operator

The Bessel functions of the quaternion variable are the radial parts of the monogenic functions on $\mathbb{R}^4$. They appear in the separation of variables for the Dirac equation in spherical coordinates, and they are the quaternion analogues of the cylindrical harmonics in complex analysis.

## The Quaternion Hypergeometric Function

### Definition

The **quaternion Gauss hypergeometric function** is defined for $|q| < 1$ by

$$
{}_2F_1(a, b; c; q) = \sum_{n=0}^\infty \frac{(a)_n (b)_n}{(c)_n} \frac{q^n}{n!},
$$

where $(a)_n = a(a+1) \cdots (a+n-1)$ is the Pochhammer symbol, and all operations are quaternion. The series converges for $|q| < 1$.

### Differential Equation

$$
q(1 - q) y'' + [c - (a + b + 1) q] y' - ab y = 0.
$$

This is the hypergeometric equation, and it holds in the quaternion sense.

### Special Cases

$$
{}_2F_1(1, 1; 2; q) = -\frac{\log(1 - q)}{q},
$$

$$
{}_2F_1(a, b; b; q) = (1 - q)^{-a},
$$

$$
{}_2F_1\left(\frac{1}{2}, \frac{1}{2}; \frac{3}{2}; q^2\right) = \frac{\arcsin(q)}{q}.
$$

### The Generalized Hypergeometric Function

$$
{}_pF_q(a_1, \dots, a_p; b_1, \dots, b_q; q) = \sum_{n=0}^\infty \frac{(a_1)_n \cdots (a_p)_n}{(b_1)_n \cdots (b_q)_n} \frac{q^n}{n!}.
$$

Most special functions of quaternion analysis are special cases of ${}_pF_q$.

## The Quaternion Lambert W Function

### Definition

The **quaternion Lambert W function** is the inverse of

$$
f(w) = w e^w,
$$

where the exponential is the quaternion exponential. That is, $W(q)$ is any solution of

$$
W(q) e^{W(q)} = q.
$$

### Derivative

$$
W'(q) = \frac{W(q)}{q(1 + W(q))},
$$

defined wherever the denominator is invertible.

### Branches

The quaternion Lambert W function has infinitely many branches, because the quaternion exponential is not injective. The principal branch is defined on the complement of the cut locus, and it is single-valued on that domain.

## The Monogenic Special Functions

### The Cauchy Kernel

The **Cauchy kernel** is the function

$$
E(q) = \frac{q^{-1}}{|q|^2} = \frac{\bar{q}}{|q|^4}, \qquad q \neq 0.
$$

It is the fundamental solution of the Dirac operator:

$$
D E = \delta_0
$$

in the sense of distributions. It is the quaternion analogue of the kernel $1/z$ in complex analysis.

### The Monogenic Exponential

The **monogenic exponential** is the function

$$
f(q) = e^{q_0} \left( \cos|\mathbf{q}| + \frac{\mathbf{q}}{|\mathbf{q}|} \sin|\mathbf{q}| \right),
$$

which is the quaternion exponential written in scalar-vector form. It is monogenic in the sense that $D f = 0$ on the appropriate domain, and it is the starting point for the construction of monogenic functions by power series.

### The Monogenic Power Functions

The **monogenic power functions** are the functions

$$
f_n(q) = q^n, \qquad n \in \mathbb{Z},
$$

which are monogenic on the appropriate domains. For negative $n$, the functions have singularities at the origin, and the Laurent expansion of a monogenic function is expressed in terms of these powers.

### The Monogenic Bessel Functions

The **monogenic Bessel functions** are the radial monogenic functions, which are the solutions of the Dirac equation in spherical coordinates. They are expressed in terms of the ordinary Bessel functions of the radial variable, with coefficients that depend on the angular variables.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | Quaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis |
| $q = q_0 + \mathbf{q}$ | General quaternion |
| $e^q, \log q$ | Quaternion exponential, logarithm |
| $\sin q, \cos q, \tan q$ | Quaternion trigonometric functions |
| $\sinh q, \cosh q, \tanh q$ | Quaternion hyperbolic functions |
| $q^a$ | Quaternion power |
| $\Gamma(q)$ | Quaternion gamma function |
| $B(p, q)$ | Quaternion beta function |
| $\operatorname{erf}(q), \operatorname{erfc}(q)$ | Quaternion error functions |
| $\operatorname{Ai}(q)$ | Quaternion Airy function |
| $J_\nu(q), I_\nu(q)$ | Quaternion Bessel functions |
| ${}_pF_q$ | Quaternion generalized hypergeometric function |
| $W(q)$ | Quaternion Lambert W function |
| $E(q) = q^{-1}/\|q\|^2$ | Cauchy kernel |
| $D$ | Dirac operator |

## The Structure Principle

The pattern in all the definitions above is the same: every quaternion special function is defined by a formula that involves the quaternion algebra operations, the quaternion exponential, and the quaternion logarithm. Unlike the complex case, the resulting functions are not determined by a single scalar variable, because $\mathbb{H}$ is four-dimensional and non-commutative. The functions depend on the scalar part and the vector part separately, and the non-commutativity prevents the simple identities that hold in the commutative case.

**Theorem (Structure Principle for quaternion special functions).** Let $F$ be a special function of one real variable that is analytic on an interval $I \subseteq \mathbb{R}$, and let $\tilde{F}$ be its extension to the quaternions defined by the same power series. Then for $q$ with $q_0 \in I$ and $\mathbf{q}$ arbitrary,

$$
\tilde{F}(q) = \sum_{n=0}^\infty \frac{F^{(n)}(q_0)}{n!} \mathbf{q}^n,
$$

where the powers $\mathbf{q}^n$ are the quaternion powers of the vector part.

**Proof.** The extension is defined by the same power series, and the series converges because the quaternion norm is submultiplicative. The powers of $q$ decompose into the scalar and vector parts, and the series can be reorganized in terms of the powers of $\mathbf{q}$. $\square$

This theorem is the reason quaternion special functions are richer than real or complex special functions. In the real case, the function is determined by its values on the real line. In the complex case, the function is determined by its values on the real line and the Cauchy–Riemann equations. In the quaternion case, the function depends on the full four-dimensional variable, and the non-commutativity prevents the simple identities that hold in the commutative case.

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original formulation.
- Rudolf Fueter, "Die Funktionentheorie der Differentialgleichungen $\Delta u = 0$ und $\Delta \Delta u = 0$ mit vier reellen Variablen" (1935), for the origin of monogenic functions.
- F. Brackx, R. Delanghe, and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the general Clifford theory.
- John Ryan, *Clifford Algebras in Analysis and Related Topics* (CRC Press, 1996), for the analytic theory.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton, 1989), for the role of the Dirac operator in geometry.

