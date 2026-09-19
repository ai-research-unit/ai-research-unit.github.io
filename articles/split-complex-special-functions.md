
# Split Complex Special Functions

## Introduction

This article introduces the split complex special functions as a collection of named functions that arise repeatedly in split complex analysis, hyperbolic differential equations, and the geometry of Minkowski space. The goal is to define each function precisely, establish its basic properties, and describe the relations among them.

The treatment is mathematically honest: every claim is either proved or stated as a definition. Split complex analysis is assumed from the article on split complex analysis, and the idempotent decomposition is used throughout. The order of presentation follows the dependency order: the split complex exponential and its consequences first, then functions defined from them, then functions defined by series and integrals.

## The Split Complex Exponential and Logarithm

### The Split Complex Exponential

The **split complex exponential** is defined for $z \in \mathbb{D}$ by

$$
\exp(z) = \sum_{n=0}^\infty \frac{z^n}{n!}.
$$

The series converges absolutely for every $z$ in the Euclidean norm. The function is entire in the split complex sense, and it satisfies

$$
\exp(z + w) = \exp(z) \exp(w), \qquad \exp(0) = 1, \qquad \exp'(z) = \exp(z).
$$

For $z = x + jy$ with $x, y \in \mathbb{R}$,

$$
\exp(z) = e^x (\cosh y + j \sinh y).
$$

This is the **split Euler formula**, and it is the bridge between the exponential and the hyperbolic functions. In particular, for $y = \theta$,

$$
e^{j\theta} = \cosh\theta + j \sinh\theta.
$$

The exponential is **not** periodic. Unlike the complex exponential, which is $2\pi i$-periodic, the split complex exponential is injective on the real axis and has no period.

### The Idempotent Form

In the idempotent basis, the exponential decomposes as

$$
\exp(z) = e^{z_+} e_+ + e^{z_-} e_-, \qquad z_+ = x + y, \quad z_- = x - y.
$$

So the split complex exponential is the pair of ordinary real exponentials, one for each idempotent. This is the fundamental structural fact about the exponential, and it is the reason most split complex special functions are pairs of real special functions.

### The Split Complex Logarithm

The **split complex logarithm** is the inverse of the exponential. It is defined for $z$ with $z_+ > 0$ and $z_- > 0$ by

$$
\log z = \frac{1}{2} \log(z_+ z_-) + \frac{j}{2} \log\left(\frac{z_+}{z_-}\right).
$$

Equivalently, in the idempotent basis,

$$
\log z = \log(z_+) e_+ + \log(z_-) e_-.
$$

The logarithm is defined only on the region where both idempotent components are positive. It is not defined on the light cone, because one of the components vanishes there.

The logarithm is split complex differentiable on its domain, with derivative $1/z$. It satisfies

$$
\log(z w) = \log z + \log w
$$

whenever both sides are defined.

### Split Complex Powers

For $a \in \mathbb{D}$ and $z$ in the domain of the logarithm,

$$
z^a = \exp(a \log z).
$$

This is single-valued on the domain of the logarithm, unlike the complex case, where the logarithm is multivalued. The reason is that the split complex exponential is injective on its domain, so the logarithm is single-valued.

## The Hyperbolic Functions

### Definition

The **split hyperbolic sine** and **cosine** are defined by

$$
\sinh z = \frac{e^z - e^{-z}}{2}, \qquad \cosh z = \frac{e^z + e^{-z}}{2}.
$$

They are entire in the split complex sense, and they satisfy

$$
\sinh' z = \cosh z, \qquad \cosh' z = \sinh z,
$$

$$
\cosh^2 z - \sinh^2 z = 1.
$$

In the idempotent basis,

$$
\sinh z = \sinh(z_+) e_+ + \sinh(z_-) e_-,
$$

$$
\cosh z = \cosh(z_+) e_+ + \cosh(z_-) e_-.
$$

So the split hyperbolic functions are pairs of ordinary real hyperbolic functions.

### The Other Hyperbolic Functions

$$
\tanh z = \frac{\sinh z}{\cosh z}, \qquad \coth z = \frac{\cosh z}{\sinh z}.
$$

These are defined wherever the denominator is invertible. The denominator $\cosh z$ is invertible unless $\cosh(z_+) = 0$ or $\cosh(z_-) = 0$, which never happens for real $z_+$ and $z_-$. So $\tanh$ is defined on all of $\mathbb{D}$, and $\coth$ is defined except on the light cone.

### Inverse Hyperbolic Functions

The **split inverse hyperbolic sine** is defined by

$$
\operatorname{arsinh} z = \log\left(z + \sqrt{z^2 + 1}\right),
$$

where the square root is the split complex square root. The **split inverse hyperbolic cosine** is

$$
\operatorname{arcosh} z = \log\left(z + \sqrt{z^2 - 1}\right),
$$

defined for $z$ with $z_+ \geq 1$ and $z_- \geq 1$. The **split inverse hyperbolic tangent** is

$$
\operatorname{artanh} z = \frac{1}{2} \log \frac{1 + z}{1 - z},
$$

defined for $z$ with $|z_+| < 1$ and $|z_-| < 1$.

In the idempotent basis, each of these is the ordinary real inverse hyperbolic function applied to the corresponding component.

## The Gamma Function

### Definition

The **split complex gamma function** is defined for $z$ with $z_+ > 0$ and $z_- > 0$ by

$$
\Gamma(z) = \int_0^\infty t^{z-1} e^{-t} \, dt,
$$

where the integral is along the positive real axis, and $t^{z-1}$ is the split complex power. In the idempotent basis,

$$
\Gamma(z) = \Gamma(z_+) e_+ + \Gamma(z_-) e_-.
$$

So the split complex gamma function is the pair of ordinary real gamma functions, one for each idempotent.

### Functional Equation

$$
\Gamma(z + 1) = z \Gamma(z).
$$

This follows from integration by parts, exactly as in the real case.

### Special Values

$$
\Gamma(n + 1) = n!
$$

for non-negative integers $n$, where the factorial is the ordinary real factorial applied to each idempotent component.

### Reflection Formula

$$
\Gamma(z) \Gamma(1 - z) = \frac{\pi}{\sin(\pi z)},
$$

where the sine is the ordinary real sine applied to each idempotent component.

## The Beta Function

### Definition

The **split complex beta function** is defined for $x, y$ with $x_+ > 0$, $x_- > 0$, $y_+ > 0$, $y_- > 0$ by

$$
B(x, y) = \int_0^1 t^{x-1} (1 - t)^{y-1} \, dt.
$$

In the idempotent basis,

$$
B(x, y) = B(x_+, y_+) e_+ + B(x_-, y_-) e_-.
$$

### Relation to the Gamma Function

$$
B(x, y) = \frac{\Gamma(x) \Gamma(y)}{\Gamma(x + y)}.
$$

This follows from the same substitution as in the real case, applied to each idempotent component.

### Symmetry

$$
B(x, y) = B(y, x).
$$

## The Error Function

### Definition

The **split complex error function** is defined by

$$
\operatorname{erf}(z) = \frac{2}{\sqrt{\pi}} \int_0^z e^{-t^2} \, dt,
$$

where the integral is along a path from $0$ to $z$ that does not cross the light cone. In the idempotent basis,

$$
\operatorname{erf}(z) = \operatorname{erf}(z_+) e_+ + \operatorname{erf}(z_-) e_-.
$$

So the split complex error function is the pair of ordinary real error functions.

### Properties

$$
\operatorname{erf}'(z) = \frac{2}{\sqrt{\pi}} e^{-z^2},
$$

$$
\lim_{z \to \infty} \operatorname{erf}(z) = 1, \qquad \lim_{z \to -\infty} \operatorname{erf}(z) = -1,
$$

where the limits are taken along the real axis.

### The Complementary Error Function

$$
\operatorname{erfc}(z) = 1 - \operatorname{erf}(z) = \frac{2}{\sqrt{\pi}} \int_z^\infty e^{-t^2} \, dt.
$$

In the idempotent basis, this is the ordinary real complementary error function applied to each component.

## The Airy Functions

### Definition

The **split complex Airy function** is defined by

$$
\operatorname{Ai}(z) = \frac{1}{\pi} \int_0^\infty \cos\left(\frac{t^3}{3} + zt\right) dt,
$$

where the cosine is the ordinary real cosine applied to each idempotent component. In the idempotent basis,

$$
\operatorname{Ai}(z) = \operatorname{Ai}(z_+) e_+ + \operatorname{Ai}(z_-) e_-.
$$

So the split complex Airy function is the pair of ordinary real Airy functions.

### Differential Equation

$$
y'' - z y = 0.
$$

This is Airy's equation, and it holds in each idempotent component separately.

### Asymptotics

For $z_+ \to +\infty$,

$$
\operatorname{Ai}(z_+) \sim \frac{1}{2 \sqrt{\pi} z_+^{1/4}} e^{-2 z_+^{3/2}/3}.
$$

For $z_+ \to -\infty$,

$$
\operatorname{Ai}(z_+) \sim \frac{1}{\sqrt{\pi} |z_+|^{1/4}} \sin\left(\frac{2 |z_+|^{3/2}}{3} + \frac{\pi}{4}\right).
$$

The same asymptotics hold for the minus component.

## The Bessel Functions

### Definition

The **split complex Bessel function** of the first kind of order $\nu$ is defined by

$$
J_\nu(z) = \sum_{n=0}^\infty \frac{(-1)^n}{n! \, \Gamma(n + \nu + 1)} \left( \frac{z}{2} \right)^{2n + \nu},
$$

where the power and the gamma function are split complex. In the idempotent basis,

$$
J_\nu(z) = J_\nu(z_+) e_+ + J_\nu(z_-) e_-.
$$

So the split complex Bessel function is the pair of ordinary real Bessel functions.

### Differential Equation

$$
z^2 y'' + z y' + (z^2 - \nu^2) y = 0.
$$

This is Bessel's equation, and it holds in each idempotent component separately.

### Modified Bessel Functions

The **split complex modified Bessel function** of the first kind is

$$
I_\nu(z) = \sum_{n=0}^\infty \frac{1}{n! \, \Gamma(n + \nu + 1)} \left( \frac{z}{2} \right)^{2n + \nu}.
$$

In the idempotent basis, this is the ordinary real modified Bessel function applied to each component.

## The Hypergeometric Function

### Definition

The **split complex Gauss hypergeometric function** is defined for $|z_+| < 1$ and $|z_-| < 1$ by

$$
{}_2F_1(a, b; c; z) = \sum_{n=0}^\infty \frac{(a)_n (b)_n}{(c)_n} \frac{z^n}{n!},
$$

where $(a)_n = a(a+1) \cdots (a+n-1)$ is the Pochhammer symbol, and all operations are split complex. In the idempotent basis,

$$
{}_2F_1(a, b; c; z) = {}_2F_1(a_+, b_+; c_+; z_+) e_+ + {}_2F_1(a_-, b_-; c_-; z_-) e_-.
$$

So the split complex hypergeometric function is the pair of ordinary real hypergeometric functions.

### Differential Equation

$$
z(1 - z) y'' + [c - (a + b + 1) z] y' - ab y = 0.
$$

This is the hypergeometric equation, and it holds in each idempotent component separately.

### Special Cases

$$
{}_2F_1(1, 1; 2; z) = -\frac{\log(1 - z)}{z},
$$

$$
{}_2F_1(a, b; b; z) = (1 - z)^{-a},
$$

$$
{}_2F_1\left(\frac{1}{2}, \frac{1}{2}; \frac{3}{2}; z^2\right) = \frac{\arcsin z}{z},
$$

where the arcsine is the ordinary real arcsine applied to each idempotent component.

### The Generalized Hypergeometric Function

$$
{}_pF_q(a_1, \dots, a_p; b_1, \dots, b_q; z) = \sum_{n=0}^\infty \frac{(a_1)_n \cdots (a_p)_n}{(b_1)_n \cdots (b_q)_n} \frac{z^n}{n!}.
$$

In the idempotent basis, this is the ordinary real generalized hypergeometric function applied to each component.

## The Lambert W Function

### Definition

The **split complex Lambert W function** is the inverse of

$$
f(w) = w e^w.
$$

That is, $W(z)$ is any solution of

$$
W(z) e^{W(z)} = z.
$$

In the idempotent basis,

$$
W(z) = W(z_+) e_+ + W(z_-) e_-,
$$

where $W$ on the right is the ordinary real Lambert W function.

### Derivative

$$
W'(z) = \frac{W(z)}{z(1 + W(z))},
$$

defined wherever the denominator is invertible.

### Branches

The split complex Lambert W function has two real branches, corresponding to the two real branches $W_0$ and $W_{-1}$ of the ordinary Lambert W function. On the region where $z_+ > -1/e$ and $z_- > -1/e$, the principal branch is defined, and it is split complex differentiable.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | Split complex algebra |
| $j$ | Split imaginary unit, $j^2 = +1$ |
| $e^z, \log z$ | Split complex exponential, logarithm |
| $\sinh z, \cosh z, \tanh z$ | Split hyperbolic functions |
| $\Gamma(z)$ | Split complex gamma function |
| $B(x, y)$ | Split complex beta function |
| $\operatorname{erf}(z), \operatorname{erfc}(z)$ | Split error function, complementary error function |
| $\operatorname{Ai}(z)$ | Split Airy function |
| $J_\nu(z), I_\nu(z)$ | Split Bessel functions |
| ${}_pF_q$ | Split generalized hypergeometric function |
| $W(z)$ | Split Lambert W function |
| $e_+ = (1 + j)/2$ | Positive idempotent |
| $e_- = (1 - j)/2$ | Negative idempotent |
| $z = z_+ e_+ + z_- e_-$ | Idempotent decomposition |

## The Idempotent Principle

The pattern in all the definitions above is the same: every split complex special function is the pair of ordinary real special functions, one for each idempotent component. This is not a coincidence; it is a theorem.

**Theorem (Idempotent Principle).** Let $F$ be a split complex special function defined by a formula that involves only the split complex algebra operations, the split complex exponential, and the split complex logarithm. Then $F$ decomposes in the idempotent basis as

$$
F(z) = F_+(z_+) e_+ + F_-(z_-) e_-,
$$

where $F_+$ and $F_-$ are the corresponding real special functions.

**Proof.** The split complex algebra is isomorphic to $\mathbb{R} \oplus \mathbb{R}$ via the idempotent decomposition. Every operation in the split complex algebra corresponds to the componentwise operation in $\mathbb{R} \oplus \mathbb{R}$. Every split complex special function is defined by a formula built from these operations, so it decomposes componentwise. $\square$

This theorem is the reason split complex special functions are simpler than complex special functions. In the complex case, the special functions are genuinely new objects, because the complex algebra is a field and the exponential is periodic. In the split complex case, the special functions are pairs of real special functions, because the split complex algebra is a product of two copies of $\mathbb{R}$ and the exponential is injective.

## Further Reading

- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the geometric interpretation of split complex numbers.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- Vladimir V. Kisil, *Geometry of Möbius Transformations: Elliptic, Parabolic and Hyperbolic Actions of SL(2, ℝ)* (Imperial College Press, 2012), for the analytic applications.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the classification of real algebras.
- Walter Rudin, *Real and Complex Analysis* (McGraw-Hill, 1987), for the comparison with the complex case.


