
# __Split-Complex Special Functions__

## Introduction

This article introduces the split complex special functions as a collection of named functions that arise repeatedly in split complex analysis, hyperbolic differential equations, and the geometry of the Lorentzian plane. The goal is to define each function precisely, establish its basic properties, and describe the relations among them.

The treatment is mathematically honest: every claim is either proved or stated as a definition. Split complex analysis is assumed from the article on split complex analysis, and the idempotent decomposition is used throughout. The order of presentation follows the dependency order: the split complex exponential and its consequences first, then functions defined from them, then functions defined by series and integrals.

## The Split Complex Exponential and Logarithm

### The Split Complex Exponential

The **split complex exponential** is defined for $Z \in \mathbb{D}$ by

$$
\exp(Z) = \sum_{n=0}^\infty \frac{Z^n}{n!}.
$$

The series converges absolutely for every $Z$ in the Euclidean norm. The function is entire in the split complex sense, and it satisfies

$$
\exp(Z + W) = \exp(Z) \exp(W), \qquad \exp(0) = 1, \qquad \exp'(Z) = \exp(Z).
$$

For $Z = x + jy$ with $x, y \in \mathbb{R}$,

$$
\exp(Z) = e^x (\cosh y + j \sinh y).
$$

This is the **split Euler formula**, and it is the bridge between the exponential and the hyperbolic functions. In particular, for $y = \theta$,

$$
e^{j\theta} = \cosh\theta + j \sinh\theta.
$$

The exponential is **not** periodic. Unlike the complex exponential, which is $2\pi i$-periodic, the split complex exponential is injective on the real axis and has no period.

### The Idempotent Form

In the idempotent basis, the exponential decomposes as

$$
\exp(Z) = e^{Z_+} \Pi_1 + e^{Z_-} \Pi_2, \qquad Z_+ = x + y, \quad Z_- = x - y.
$$

So the split complex exponential is the pair of ordinary real exponentials, one for each idempotent. This is the fundamental structural fact about the exponential, and it is the reason most split complex special functions are pairs of real special functions.

### The Split Complex Logarithm

The **split complex logarithm** is the inverse of the exponential. It is defined for $Z$ with $Z_+ > 0$ and $Z_- > 0$ by

$$
\log Z = \frac{1}{2} \log(Z_+ Z_-) + \frac{j}{2} \log\left(\frac{Z_+}{Z_-}\right).
$$

Equivalently, in the idempotent basis,

$$
\log Z = \log(Z_+) \Pi_1 + \log(Z_-) \Pi_2.
$$

The logarithm is defined only on the region where both idempotent components are positive. It is not defined on the null cone, because one of the components vanishes there.

The logarithm is split complex differentiable on its domain, with derivative $1/Z$. It satisfies

$$
\log(Z W) = \log Z + \log W
$$

whenever both sides are defined.

### Split Complex Powers

For $a \in \mathbb{D}$ and $Z$ in the domain of the logarithm,

$$
Z^a = \exp(a \log Z).
$$

This is single-valued on the domain of the logarithm, unlike the complex case, where the logarithm is multivalued. The reason is that the split complex exponential is injective on its domain, so the logarithm is single-valued.

## The Hyperbolic Functions

### Definition

The **split hyperbolic sine** and **cosine** are defined by

$$
\sinh Z = \frac{e^Z - e^{-Z}}{2}, \qquad \cosh Z = \frac{e^Z + e^{-Z}}{2}.
$$

They are entire in the split complex sense, and they satisfy

$$
\sinh' Z = \cosh Z, \qquad \cosh' Z = \sinh Z,
$$

$$
\cosh^2 Z - \sinh^2 Z = 1.
$$

In the idempotent basis,

$$
\sinh Z = \sinh(Z_+) \Pi_1 + \sinh(Z_-) \Pi_2,
$$

$$
\cosh Z = \cosh(Z_+) \Pi_1 + \cosh(Z_-) \Pi_2.
$$

So the split hyperbolic functions are pairs of ordinary real hyperbolic functions.

### The Other Hyperbolic Functions

$$
\tanh Z = \frac{\sinh Z}{\cosh Z}, \qquad \coth Z = \frac{\cosh Z}{\sinh Z}.
$$

These are defined wherever the denominator is invertible. The denominator $\cosh Z$ is invertible unless $\cosh(Z_+) = 0$ or $\cosh(Z_-) = 0$, which never happens for real $Z_+$ and $Z_-$. So $\tanh$ is defined on all of $\mathbb{D}$, and $\coth$ is defined except on the null cone.

### Inverse Hyperbolic Functions

The **split inverse hyperbolic sine** is defined by

$$
\operatorname{arsinh} Z = \log\left(Z + \sqrt{Z^2 + 1}\right),
$$

where the square root is the split complex square root. The **split inverse hyperbolic cosine** is

$$
\operatorname{arcosh} Z = \log\left(Z + \sqrt{Z^2 - 1}\right),
$$

defined for $Z$ with $Z_+ \geq 1$ and $Z_- \geq 1$. The **split inverse hyperbolic tangent** is

$$
\operatorname{artanh} Z = \frac{1}{2} \log \frac{1 + Z}{1 - Z},
$$

defined for $Z$ with $|Z_+| < 1$ and $|Z_-| < 1$.

In the idempotent basis, each of these is the ordinary real inverse hyperbolic function applied to the corresponding component.

## The Gamma Function

### Definition

The **split complex gamma function** is defined for $Z$ with $Z_+ > 0$ and $Z_- > 0$ by

$$
\Gamma(Z) = \int_0^\infty t^{Z-1} e^{-t} \, dt,
$$

where the integral is along the positive real axis, and $t^{Z-1}$ is the split complex power. In the idempotent basis,

$$
\Gamma(Z) = \Gamma(Z_+) \Pi_1 + \Gamma(Z_-) \Pi_2.
$$

So the split complex gamma function is the pair of ordinary real gamma functions, one for each idempotent.

### Functional Equation

$$
\Gamma(Z + 1) = Z \Gamma(Z).
$$

This follows from integration by parts, exactly as in the real case.

### Special Values

$$
\Gamma(n + 1) = n!
$$

for non-negative integers $n$, where the factorial is the ordinary real factorial applied to each idempotent component.

### Reflection Formula

$$
\Gamma(Z) \Gamma(1 - Z) = \frac{\pi}{\sin(\pi Z)},
$$

where the sine is the ordinary real sine applied to each idempotent component.

## The Beta Function

### Definition

The **split complex beta function** is defined for $p, q$ with $p_+ > 0$, $p_- > 0$, $q_+ > 0$, $q_- > 0$ by

$$
B(p, q) = \int_0^1 t^{p-1} (1 - t)^{q-1} \, dt.
$$

In the idempotent basis,

$$
B(p, q) = B(p_+, q_+) \Pi_1 + B(p_-, q_-) \Pi_2.
$$

### Relation to the Gamma Function

$$
B(p, q) = \frac{\Gamma(p) \Gamma(q)}{\Gamma(p + q)}.
$$

This follows from the same substitution as in the real case, applied to each idempotent component.

### Symmetry

$$
B(p, q) = B(q, p).
$$

## The Error Function

### Definition

The **split complex error function** is defined by

$$
\operatorname{erf}(Z) = \frac{2}{\sqrt{\pi}} \int_0^Z e^{-t^2} \, dt,
$$

where the integral is along a path from $0$ to $Z$ that does not cross the null cone. In the idempotent basis,

$$
\operatorname{erf}(Z) = \operatorname{erf}(Z_+) \Pi_1 + \operatorname{erf}(Z_-) \Pi_2.
$$

So the split complex error function is the pair of ordinary real error functions.

### Properties

$$
\operatorname{erf}'(Z) = \frac{2}{\sqrt{\pi}} e^{-Z^2},
$$

$$
\lim_{Z \to \infty} \operatorname{erf}(Z) = 1, \qquad \lim_{Z \to -\infty} \operatorname{erf}(Z) = -1,
$$

where the limits are taken along the real axis.

### The Complementary Error Function

$$
\operatorname{erfc}(Z) = 1 - \operatorname{erf}(Z) = \frac{2}{\sqrt{\pi}} \int_Z^\infty e^{-t^2} \, dt.
$$

In the idempotent basis, this is the ordinary real complementary error function applied to each component.

## The Airy Functions

### Definition

The **split complex Airy function** is defined by

$$
\operatorname{Ai}(Z) = \frac{1}{\pi} \int_0^\infty \cos\left(\frac{t^3}{3} + Zt\right) dt,
$$

where the cosine is the ordinary real cosine applied to each idempotent component. In the idempotent basis,

$$
\operatorname{Ai}(Z) = \operatorname{Ai}(Z_+) \Pi_1 + \operatorname{Ai}(Z_-) \Pi_2.
$$

So the split complex Airy function is the pair of ordinary real Airy functions.

### Differential Equation

$$
y'' - Z y = 0.
$$

This is Airy's equation, and it holds in each idempotent component separately.

### Asymptotics

For $Z_+ \to +\infty$,

$$
\operatorname{Ai}(Z_+) \sim \frac{1}{2 \sqrt{\pi} Z_+^{1/4}} e^{-2 Z_+^{3/2}/3}.
$$

For $Z_+ \to -\infty$,

$$
\operatorname{Ai}(Z_+) \sim \frac{1}{\sqrt{\pi} |Z_+|^{1/4}} \sin\left(\frac{2 |Z_+|^{3/2}}{3} + \frac{\pi}{4}\right).
$$

The same asymptotics hold for the minus component.

## The Bessel Functions

### Definition

The **split complex Bessel function** of the first kind of order $\nu$ is defined by

$$
J_\nu(Z) = \sum_{n=0}^\infty \frac{(-1)^n}{n! \, \Gamma(n + \nu + 1)} \left( \frac{Z}{2} \right)^{2n + \nu},
$$

where the power and the gamma function are split complex. In the idempotent basis,

$$
J_\nu(Z) = J_\nu(Z_+) \Pi_1 + J_\nu(Z_-) \Pi_2.
$$

So the split complex Bessel function is the pair of ordinary real Bessel functions.

### Differential Equation

$$
Z^2 y'' + Z y' + (Z^2 - \nu^2) y = 0.
$$

This is Bessel's equation, and it holds in each idempotent component separately.

### Modified Bessel Functions

The **split complex modified Bessel function** of the first kind is

$$
I_\nu(Z) = \sum_{n=0}^\infty \frac{1}{n! \, \Gamma(n + \nu + 1)} \left( \frac{Z}{2} \right)^{2n + \nu}.
$$

In the idempotent basis, this is the ordinary real modified Bessel function applied to each component.

## The Hypergeometric Function

### Definition

The **split complex Gauss hypergeometric function** is defined for $|Z_+| < 1$ and $|Z_-| < 1$ by

$$
{}_2F_1(a, b; c; Z) = \sum_{n=0}^\infty \frac{(a)_n (b)_n}{(c)_n} \frac{Z^n}{n!},
$$

where $(a)_n = a(a+1) \cdots (a+n-1)$ is the Pochhammer symbol, and all operations are split complex. In the idempotent basis,

$$
{}_2F_1(a, b; c; Z) = {}_2F_1(a_+, b_+; c_+; Z_+) \Pi_1 + {}_2F_1(a_-, b_-; c_-; Z_-) \Pi_2.
$$

So the split complex hypergeometric function is the pair of ordinary real hypergeometric functions.

### Differential Equation

$$
Z(1 - Z) y'' + [c - (a + b + 1) Z] y' - ab y = 0.
$$

This is the hypergeometric equation, and it holds in each idempotent component separately.

### Special Cases

$$
{}_2F_1(1, 1; 2; Z) = -\frac{\log(1 - Z)}{Z},
$$

$$
{}_2F_1(a, b; b; Z) = (1 - Z)^{-a},
$$

$$
{}_2F_1\left(\frac{1}{2}, \frac{1}{2}; \frac{3}{2}; Z^2\right) = \frac{\arcsin Z}{Z},
$$

where the arcsine is the ordinary real arcsine applied to each idempotent component.

### The Generalized Hypergeometric Function

$$
{}_pF_q(a_1, \dots, a_p; b_1, \dots, b_q; Z) = \sum_{n=0}^\infty \frac{(a_1)_n \cdots (a_p)_n}{(b_1)_n \cdots (b_q)_n} \frac{Z^n}{n!}.
$$

In the idempotent basis, this is the ordinary real generalized hypergeometric function applied to each component.

## The Lambert W Function

### Definition

The **split complex Lambert W function** is the inverse of

$$
Z \mapsto Z e^Z.
$$

That is, $W(Z)$ is any solution of

$$
W(Z) e^{W(Z)} = Z.
$$

In the idempotent basis,

$$
W(Z) = W(Z_+) \Pi_1 + W(Z_-) \Pi_2,
$$

where $W$ on the right is the ordinary real Lambert W function.

### Derivative

$$
W'(Z) = \frac{W(Z)}{Z(1 + W(Z))},
$$

defined wherever the denominator is invertible.

### Branches

The split complex Lambert W function is defined componentwise, so it inherits the two real branches $W_0$ and $W_{-1}$ of the ordinary Lambert W function independently in each idempotent component; its branches are the four combinations obtained by choosing one of $W_0$ and $W_{-1}$ for $Z_+$ and one for $Z_-$. On the region where $Z_+ > -1/e$ and $Z_- > -1/e$, the principal branch $W_0$, taken in both components, is defined, and it is split complex differentiable.

## The Idempotent Principle

The pattern in all the definitions above is the same: every split complex special function is the pair of ordinary real special functions, one for each idempotent component. This is not a coincidence; it is a theorem.

**Theorem (Idempotent Principle).** Let $F$ be a split complex special function defined by a formula that involves only the split complex algebra operations, the split complex exponential, and the split complex logarithm. Then $F$ decomposes in the idempotent basis as

$$
F(Z) = F_+(Z_+) \Pi_1 + F_-(Z_-) \Pi_2,
$$

where $F_+$ and $F_-$ are the corresponding real special functions.

**Proof.** The split complex algebra is isomorphic to $\mathbb{R} \oplus \mathbb{R}$ via the idempotent decomposition. Every operation in the split complex algebra corresponds to the componentwise operation in $\mathbb{R} \oplus \mathbb{R}$. Every split complex special function is defined by a formula built from these operations, so it decomposes componentwise.

This theorem is the reason split complex special functions are simpler than complex special functions. In the complex case, the special functions are genuinely new objects, because the complex algebra is a field and the exponential is periodic. In the split complex case, the special functions are pairs of real special functions, because the split complex algebra is a product of two copies of $\mathbb{R}$ and the exponential is injective.

## Summary

The split complex special functions are the named functions that arise in split complex analysis, in hyperbolic geometry and in the theory of the wave equation. Each is obtained by carrying the corresponding real or complex definition to the split complex variable by means of the split complex exponential and the algebra operations.

The exponential is defined by its series, and the hyperbolic functions are built from it, the trigonometric functions being replaced by their hyperbolic analogues because $j^2 = +1$. Integral representations then supply the gamma and beta functions, the error function, the Airy function, the Bessel functions and the Gauss hypergeometric function, together with the Lambert $W$ function as the inverse of $W \mapsto We^W$.

The section on the idempotent principle states what organises the whole collection: every split complex special function is the pair of ordinary real special functions obtained by evaluating it on the two idempotent components, one for $\Pi_1$ and one for $\Pi_2$, so that each definition is a real definition applied twice.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | Split complex algebra |
| $j$ | Split imaginary unit, $j^2 = +1$ |
| $e^Z, \log Z$ | Split complex exponential, logarithm |
| $\sinh Z, \cosh Z, \tanh Z$ | Split hyperbolic functions |
| $\Gamma(Z)$ | Split complex gamma function |
| $B(p, q)$ | Split complex beta function; arguments $p, q$ |
| $\operatorname{erf}(Z), \operatorname{erfc}(Z)$ | Split error function, complementary error function |
| $\operatorname{Ai}(Z)$ | Split Airy function |
| $J_\nu(Z), I_\nu(Z)$ | Split Bessel functions |
| ${}_pF_q$ | Split generalized hypergeometric function |
| $W(Z)$ | Split Lambert W function |
| $\Pi_1 = (1 + j)/2$ | Positive idempotent |
| $\Pi_2 = (1 - j)/2$ | Negative idempotent |
| $Z = Z_+ \Pi_1 + Z_- \Pi_2$ | Idempotent decomposition |

## Further Reading

- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the geometric interpretation of split complex numbers.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- Vladimir V. Kisil, *Geometry of Möbius Transformations: Elliptic, Parabolic and Hyperbolic Actions of $SL(2,\mathbb{R})$* (Imperial College Press, 2012), for the analytic applications.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the classification of real algebras.
- Walter Rudin, *Real and Complex Analysis* (McGraw-Hill, 1987), for the comparison with the complex case.


