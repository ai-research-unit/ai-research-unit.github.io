
# __Split-Complex Special Functions__

## Introduction

This article introduces the split complex special functions as a collection of named functions that arise repeatedly in split complex analysis, hyperbolic differential equations, and the geometry of the Lorentzian plane. The goal is to define each function precisely, establish its basic properties, and describe the relations among them.

The treatment is mathematically honest: every claim is either proved or stated as a definition. Split complex analysis is assumed from the article on split complex analysis, and the idempotent decomposition is used throughout. The order of presentation follows the dependency order: the split complex exponential and its consequences first, then functions defined from them, then functions defined by series and integrals.

## The Split Complex Exponential and Logarithm

### The Split Complex Exponential

The **split complex exponential** is defined for $A \in \mathbb{D}$ by

$$
\exp(A) = \sum_{n=0}^\infty \frac{A^n}{n!}.
$$

The series converges absolutely for every $A$ in the Euclidean norm. The function is entire in the split complex sense, and it satisfies

$$
\exp(A + B) = \exp(A) \exp(B), \qquad \exp(0) = 1, \qquad \exp'(A) = \exp(A).
$$

For $A = a + ja'$ with $a, a' \in \mathbb{R}$,

$$
\exp(A) = e^a (\cosh a' + j \sinh a').
$$

This is the **split Euler formula**, and it is the bridge between the exponential and the hyperbolic functions. In particular, for $a' = \theta$,

$$
e^{j\theta} = \cosh\theta + j \sinh\theta.
$$

The exponential is **not** periodic. Unlike the complex exponential, which is $2\pi i$-periodic, the split complex exponential is injective on the real axis and has no period.

### The Idempotent Form

In the idempotent basis, the exponential decomposes as

$$
\exp(A) = e^{A_+} \Pi_1 + e^{A_-} \Pi_2, \qquad A_+ = a + a', \quad A_- = a - a'.
$$

So the split complex exponential is the pair of ordinary real exponentials, one for each idempotent. This is the fundamental structural fact about the exponential, and it is the reason most split complex special functions are pairs of real special functions.

### The Split Complex Logarithm

The **split complex logarithm** is the inverse of the exponential. It is defined for $A$ with $A_+ > 0$ and $A_- > 0$ by

$$
\log A = \frac{1}{2} \log(A_+ A_-) + \frac{j}{2} \log\left(\frac{A_+}{A_-}\right).
$$

Equivalently, in the idempotent basis,

$$
\log A = \log(A_+) \Pi_1 + \log(A_-) \Pi_2.
$$

The logarithm is defined only on the region where both idempotent components are positive. It is not defined on the null cone, because one of the components vanishes there.

The logarithm is split complex differentiable on its domain, with derivative $1/A$. It satisfies

$$
\log(A B) = \log A + \log B
$$

whenever both sides are defined.

### Split Complex Powers

For $a \in \mathbb{D}$ and $A$ in the domain of the logarithm,

$$
A^a = \exp(a \log A).
$$

This is single-valued on the domain of the logarithm, unlike the complex case, where the logarithm is multivalued. The reason is that the split complex exponential is injective on its domain, so the logarithm is single-valued.

## The Hyperbolic Functions

### Definition

The **split hyperbolic sine** and **cosine** are defined by

$$
\sinh A = \frac{e^A - e^{-A}}{2}, \qquad \cosh A = \frac{e^A + e^{-A}}{2}.
$$

They are entire in the split complex sense, and they satisfy

$$
\sinh' A = \cosh A, \qquad \cosh' A = \sinh A,
$$

$$
\cosh^2 A - \sinh^2 A = 1.
$$

In the idempotent basis,

$$
\sinh A = \sinh(A_+) \Pi_1 + \sinh(A_-) \Pi_2,
$$

$$
\cosh A = \cosh(A_+) \Pi_1 + \cosh(A_-) \Pi_2.
$$

So the split hyperbolic functions are pairs of ordinary real hyperbolic functions.

### The Other Hyperbolic Functions

$$
\tanh A = \frac{\sinh A}{\cosh A}, \qquad \coth A = \frac{\cosh A}{\sinh A}.
$$

These are defined wherever the denominator is invertible. The denominator $\cosh A$ is invertible unless $\cosh(A_+) = 0$ or $\cosh(A_-) = 0$, which never happens for real $A_+$ and $A_-$. So $\tanh$ is defined on all of $\mathbb{D}$, and $\coth$ is defined except on the null cone.

### Inverse Hyperbolic Functions

The **split inverse hyperbolic sine** is defined by

$$
\operatorname{arsinh} A = \log\left(A + \sqrt{A^2 + 1}\right),
$$

where the square root is the split complex square root. The **split inverse hyperbolic cosine** is

$$
\operatorname{arcosh} A = \log\left(A + \sqrt{A^2 - 1}\right),
$$

defined for $A$ with $A_+ \geq 1$ and $A_- \geq 1$. The **split inverse hyperbolic tangent** is

$$
\operatorname{artanh} A = \frac{1}{2} \log \frac{1 + A}{1 - A},
$$

defined for $A$ with $|A_+| < 1$ and $|A_-| < 1$.

In the idempotent basis, each of these is the ordinary real inverse hyperbolic function applied to the corresponding component.

## The Gamma Function

### Definition

The **split complex gamma function** is defined for $A$ with $A_+ > 0$ and $A_- > 0$ by

$$
\Gamma(A) = \int_0^\infty t^{A-1} e^{-t} \, dt,
$$

where the integral is along the positive real axis, and $t^{A-1}$ is the split complex power. In the idempotent basis,

$$
\Gamma(A) = \Gamma(A_+) \Pi_1 + \Gamma(A_-) \Pi_2.
$$

So the split complex gamma function is the pair of ordinary real gamma functions, one for each idempotent.

### Functional Equation

$$
\Gamma(A + 1) = A \Gamma(A).
$$

This follows from integration by parts, exactly as in the real case.

### Special Values

$$
\Gamma(n + 1) = n!
$$

for non-negative integers $n$, where the factorial is the ordinary real factorial applied to each idempotent component.

### Reflection Formula

$$
\Gamma(A) \Gamma(1 - A) = \frac{\pi}{\sin(\pi A)},
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
\operatorname{erf}(A) = \frac{2}{\sqrt{\pi}} \int_0^A e^{-t^2} \, dt,
$$

where the integral is along a path from $0$ to $A$ that does not cross the null cone. In the idempotent basis,

$$
\operatorname{erf}(A) = \operatorname{erf}(A_+) \Pi_1 + \operatorname{erf}(A_-) \Pi_2.
$$

So the split complex error function is the pair of ordinary real error functions.

### Properties

$$
\operatorname{erf}'(A) = \frac{2}{\sqrt{\pi}} e^{-A^2},
$$

$$
\lim_{A \to \infty} \operatorname{erf}(A) = 1, \qquad \lim_{A \to -\infty} \operatorname{erf}(A) = -1,
$$

where the limits are taken along the real axis.

### The Complementary Error Function

$$
\operatorname{erfc}(A) = 1 - \operatorname{erf}(A) = \frac{2}{\sqrt{\pi}} \int_A^\infty e^{-t^2} \, dt.
$$

In the idempotent basis, this is the ordinary real complementary error function applied to each component.

## The Airy Functions

### Definition

The **split complex Airy function** is defined by

$$
\operatorname{Ai}(A) = \frac{1}{\pi} \int_0^\infty \cos\left(\frac{t^3}{3} + At\right) dt,
$$

where the cosine is the ordinary real cosine applied to each idempotent component. In the idempotent basis,

$$
\operatorname{Ai}(A) = \operatorname{Ai}(A_+) \Pi_1 + \operatorname{Ai}(A_-) \Pi_2.
$$

So the split complex Airy function is the pair of ordinary real Airy functions.

### Differential Equation

$$
w'' - A w = 0.
$$

This is Airy's equation, and it holds in each idempotent component separately.

### Asymptotics

For $A_+ \to +\infty$,

$$
\operatorname{Ai}(A_+) \sim \frac{1}{2 \sqrt{\pi} A_+^{1/4}} e^{-2 A_+^{3/2}/3}.
$$

For $A_+ \to -\infty$,

$$
\operatorname{Ai}(A_+) \sim \frac{1}{\sqrt{\pi} |A_+|^{1/4}} \sin\left(\frac{2 |A_+|^{3/2}}{3} + \frac{\pi}{4}\right).
$$

The same asymptotics hold for the minus component.

## The Bessel Functions

### Definition

The **split complex Bessel function** of the first kind of order $\nu$ is defined by

$$
J_\nu(A) = \sum_{n=0}^\infty \frac{(-1)^n}{n! \, \Gamma(n + \nu + 1)} \left( \frac{A}{2} \right)^{2n + \nu},
$$

where the power and the gamma function are split complex. In the idempotent basis,

$$
J_\nu(A) = J_\nu(A_+) \Pi_1 + J_\nu(A_-) \Pi_2.
$$

So the split complex Bessel function is the pair of ordinary real Bessel functions.

### Differential Equation

$$
A^2 w'' + A w' + (A^2 - \nu^2) w = 0.
$$

This is Bessel's equation, and it holds in each idempotent component separately.

### Modified Bessel Functions

The **split complex modified Bessel function** of the first kind is

$$
I_\nu(A) = \sum_{n=0}^\infty \frac{1}{n! \, \Gamma(n + \nu + 1)} \left( \frac{A}{2} \right)^{2n + \nu}.
$$

In the idempotent basis, this is the ordinary real modified Bessel function applied to each component.

## The Hypergeometric Function

### Definition

The **split complex Gauss hypergeometric function** is defined for $|A_+| < 1$ and $|A_-| < 1$ by

$$
{}_2F_1(a, b; c; A) = \sum_{n=0}^\infty \frac{(a)_n (b)_n}{(c)_n} \frac{A^n}{n!},
$$

where $(a)_n = a(a+1) \cdots (a+n-1)$ is the Pochhammer symbol, and all operations are split complex. In the idempotent basis,

$$
{}_2F_1(a, b; c; A) = {}_2F_1(a_+, b_+; c_+; A_+) \Pi_1 + {}_2F_1(a_-, b_-; c_-; A_-) \Pi_2.
$$

So the split complex hypergeometric function is the pair of ordinary real hypergeometric functions.

### Differential Equation

$$
A(1 - A) w'' + [c - (a + b + 1) A] w' - ab w = 0.
$$

This is the hypergeometric equation, and it holds in each idempotent component separately.

### Special Cases

$$
{}_2F_1(1, 1; 2; A) = -\frac{\log(1 - A)}{A},
$$

$$
{}_2F_1(a, b; b; A) = (1 - A)^{-a},
$$

$$
{}_2F_1\left(\frac{1}{2}, \frac{1}{2}; \frac{3}{2}; A^2\right) = \frac{\arcsin A}{A},
$$

where the arcsine is the ordinary real arcsine applied to each idempotent component.

### The Generalized Hypergeometric Function

$$
{}_pF_q(a_1, \dots, a_p; b_1, \dots, b_q; A) = \sum_{n=0}^\infty \frac{(a_1)_n \cdots (a_p)_n}{(b_1)_n \cdots (b_q)_n} \frac{A^n}{n!}.
$$

In the idempotent basis, this is the ordinary real generalized hypergeometric function applied to each component.

## The Lambert W Function

### Definition

The **split complex Lambert W function** is the inverse of

$$
A \mapsto A e^A.
$$

That is, $W(A)$ is any solution of

$$
W(A) e^{W(A)} = A.
$$

In the idempotent basis,

$$
W(A) = W(A_+) \Pi_1 + W(A_-) \Pi_2,
$$

where $W$ on the right is the ordinary real Lambert W function.

### Derivative

$$
W'(A) = \frac{W(A)}{A(1 + W(A))},
$$

defined wherever the denominator is invertible.

### Branches

The split complex Lambert W function is defined componentwise, so it inherits the two real branches $W_0$ and $W_{-1}$ of the ordinary Lambert W function independently in each idempotent component; its branches are the four combinations obtained by choosing one of $W_0$ and $W_{-1}$ for $A_+$ and one for $A_-$. On the region where $A_+ > -1/e$ and $A_- > -1/e$, the principal branch $W_0$, taken in both components, is defined, and it is split complex differentiable.

## The Idempotent Principle

The pattern in all the definitions above is the same: every split complex special function is the pair of ordinary real special functions, one for each idempotent component. This is not a coincidence; it is a theorem.

**Theorem (Idempotent Principle).** Let $F$ be a split complex special function defined by a formula that involves only the split complex algebra operations, the split complex exponential, and the split complex logarithm. Then $F$ decomposes in the idempotent basis as

$$
F(A) = F_+(A_+) \Pi_1 + F_-(A_-) \Pi_2,
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
| $A = a + ja'$ | General split complex number, $a = \operatorname{Re} A$, $a' = \operatorname{Im} A$ |
| $e^A, \log A$ | Split complex exponential, logarithm |
| $\sinh A, \cosh A, \tanh A$ | Split hyperbolic functions |
| $\Gamma(A)$ | Split complex gamma function |
| $B(p, q)$ | Split complex beta function; arguments $p, q$ |
| $\operatorname{erf}(A), \operatorname{erfc}(A)$ | Split error function, complementary error function |
| $\operatorname{Ai}(A)$ | Split Airy function |
| $J_\nu(A), I_\nu(A)$ | Split Bessel functions |
| ${}_pF_q$ | Split generalized hypergeometric function |
| $W(A)$ | Split Lambert W function |
| $\Pi_1 = (1 + j)/2$ | Positive idempotent |
| $\Pi_2 = (1 - j)/2$ | Negative idempotent |
| $A = A_+ \Pi_1 + A_- \Pi_2$ | Idempotent decomposition |

## Further Reading

- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the geometric interpretation of split complex numbers.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- Vladimir V. Kisil, *Geometry of Möbius Transformations: Elliptic, Parabolic and Hyperbolic Actions of $SL(2,\mathbb{R})$* (Imperial College Press, 2012), for the analytic applications.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the classification of real algebras.
- Walter Rudin, *Real and Complex Analysis* (McGraw-Hill, 1987), for the comparison with the complex case.


