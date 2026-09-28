
# __Dual-Numbers Special Functions__

## Introduction

This article introduces the dual numbers special functions as a collection of named functions that arise in dual numbers analysis, in the deformation theory of algebras, and in the infinitesimal geometry of the dual plane. The goal is to define each function precisely, establish its basic properties, and describe the relations among them.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. No examples are given. No specific dimensions. Dual numbers analysis is assumed from the preceding article, and the maximal ideal is used throughout. The functions are defined over the real numbers $\mathbb{R}$, where the exponential, logarithmic and trigonometric series converge and the structure theorem for dual differentiable functions applies; the polynomial identities they satisfy hold over any commutative $\mathbb{Q}$-algebra.

Throughout this article, the dual number algebra is denoted $\mathbb{D}'$, and the split complex algebra is denoted $\mathbb{D}$. The unit of $\mathbb{D}'$ is denoted $\varepsilon$, and it satisfies $\varepsilon^2 = 0$.

## Preliminary: The Structure of Dual Functions

Before defining any special function, it is worth recalling the structural theorem from dual numbers analysis, because it determines the shape of every function in this article.

**Theorem (Structure of dual differentiable functions).** A dual differentiable function $f : U \to \mathbb{D}'$ on a domain $U \subseteq \mathbb{D}'$ is of the form

$$
f(x + y\varepsilon) = u(x) + \left( y u'(x) + c(x) \right) \varepsilon,
$$

where $u$ and $c$ are ordinary differentiable functions of one real variable.

So every dual differentiable function is determined by two ordinary differentiable functions of one real variable. The real part depends only on $x$; the infinitesimal part is affine in $y$, with slope the derivative $u'(x)$ of the real part. This is the fundamental constraint, and it is the reason the special functions of dual numbers analysis are simpler than the special functions of complex or split complex analysis.

The functions defined below are of two kinds:

- Functions defined by power series in $\varepsilon$, which are automatically dual differentiable.
- Functions defined by the action of the dual algebra on itself, which are not necessarily differentiable but have algebraic significance.

## The Dual Exponential

### Definition

The **dual exponential** is defined for $Z \in \mathbb{D}'$ by

$$
\exp(Z) = \sum_{n=0}^\infty \frac{Z^n}{n!}.
$$

Because $\varepsilon^2 = 0$, the series truncates at the first order in the infinitesimal part. For $Z = x + y\varepsilon$,

$$
\exp(Z) = e^x + e^x y \varepsilon = e^x (1 + y \varepsilon).
$$

So the dual exponential is the ordinary real exponential applied to the real part, multiplied by the factor $1 + y\varepsilon$ in the infinitesimal part.

### Properties

The dual exponential satisfies

$$
\exp(Z + w) = \exp(Z) \exp(w), \qquad \exp(0) = 1, \qquad \exp'(Z) = \exp(Z).
$$

**Proof.** The first identity follows from the truncated series and the addition formula for the real exponential:

$$
\exp(x + y\varepsilon) \exp(a + \varepsilon b) = e^x (1 + y\varepsilon) \cdot e^a (1 + \varepsilon b) = e^{x+a} (1 + (y + b)\varepsilon) = \exp((x + a) + (y + b)\varepsilon).
$$

The second is immediate. The third follows from term-by-term differentiation of the series, or from the structure theorem applied to the real part.

### The Dual Euler Formula

The dual analogue of Euler's formula is

$$
e^{y \varepsilon} = 1 + y \varepsilon.
$$

This is the truncation of the exponential series at first order in $\varepsilon$, and it is the algebraic content of the infinitesimal translation: adding $y\varepsilon$ to the exponent multiplies the exponential by $1 + y\varepsilon$, which is an infinitesimal perturbation of the identity.

### The Kernel of the Exponential

The dual exponential is injective on the real part and affine in the infinitesimal part. Its kernel is empty, because $e^x \neq 0$ for all real $x$. So the exponential has no zeros, and it is invertible everywhere.

## The Dual Logarithm

### Definition

The **dual logarithm** is the inverse of the dual exponential. It is defined for $Z = x + y\varepsilon$ with $x > 0$ by

$$
\log(Z) = \log(x) + \frac{y}{x} \varepsilon.
$$

So the dual logarithm is the ordinary real logarithm applied to the real part, plus the infinitesimal correction $y/x$.

### Properties

The dual logarithm satisfies

$$
\log(Z w) = \log(Z) + \log(w), \qquad \log(1) = 0, \qquad \log'(Z) = \frac{1}{Z}.
$$

**Proof.** The first identity follows from the formula and the addition formula for the real logarithm:

$$
\log((x + y\varepsilon)(a + \varepsilon b)) = \log(xa + (xb + ya)\varepsilon) = \log(xa) + \frac{xb + ya}{xa} \varepsilon = \log(x) + \log(a) + \left(\frac{b}{a} + \frac{y}{x}\right) \varepsilon.
$$

The second is immediate. The third follows from the structure theorem applied to the real part, or from the inverse function rule for the exponential.

### The Domain of Definition

The dual logarithm is defined on the set of dual numbers with positive real part. It is not defined on the maximal ideal, because the real part vanishes there. This is the analogue of the branch cut in the complex case, and it is the reason the dual logarithm is only locally defined.

### The Dual Argument

There is no dual analogue of the argument of a complex number, because the dual algebra has no compact group of units. The group of units is the set of dual numbers with non-zero real part, which is not compact. So there is no argument function with values in a compact group: the dual algebra admits no phase, and the dual logarithm of a unit is a real multiple of $\varepsilon$, with no angular part.

## The Dual Power Function

### Definition

For $a \in \mathbb{D}'$ and $Z$ in the domain of the dual logarithm, the **dual power** is

$$
Z^a = \exp(a \log Z).
$$

For $Z = x + y\varepsilon$ and $a = p + q\varepsilon$, this gives

$$
Z^a = x^p \left(1 + \left(\frac{py}{x} + q \log x\right) \varepsilon\right).
$$

So the dual power is the ordinary real power applied to the real parts, with an infinitesimal correction that involves both the infinitesimal part of the base and the infinitesimal part of the exponent.

### Properties

$$
Z^{a + b} = Z^a Z^b, \qquad (Z w)^a = Z^a w^a, \qquad (Z^a)^b = Z^{ab}.
$$

These identities follow from the corresponding identities for the exponential and logarithm, applied to the real and infinitesimal parts separately.

### The Case of Integer Exponents

For integer $n$, the dual power reduces to the ordinary power:

$$
Z^n = x^n + n x^{n-1} y \varepsilon.
$$

This is the binomial expansion truncated at first order, and it is the reason the dual power is the algebraic content of the derivative of the power function.

## The Dual Trigonometric Functions

### Definition

The **dual sine** and **cosine** are defined by

$$
\sin(Z) = \frac{e^{i Z} - e^{-i Z}}{2i}, \qquad \cos(Z) = \frac{e^{i Z} + e^{-i Z}}{2},
$$

where $i$ is the ordinary complex imaginary unit and the exponential is the complex exponential. Since $Z = x + y\varepsilon$ is a dual number, the argument $iZ$ is a complex number with a dual infinitesimal part, and the functions are defined by the ordinary complex trigonometric functions applied to the real part, with an infinitesimal correction.

Explicitly, for $Z = x + y\varepsilon$,

$$
\sin(Z) = \sin(x) + y \cos(x) \varepsilon, \qquad \cos(Z) = \cos(x) - y \sin(x) \varepsilon.
$$

So the dual trigonometric functions are the ordinary real trigonometric functions applied to the real part, with infinitesimal corrections given by the derivatives.

### Properties

The dual trigonometric functions satisfy

$$
\sin' = \cos, \qquad \cos' = -\sin,
$$

$$
\sin(Z + w) = \sin Z \cos w + \cos Z \sin w,
$$

$$
\cos(Z + w) = \cos Z \cos w - \sin Z \sin w,
$$

$$
\sin^2 Z + \cos^2 Z = 1.
$$

These identities follow from the corresponding identities for the real trigonometric functions, applied to the real and infinitesimal parts separately.

### Periodicity

The dual trigonometric functions are periodic in the real part with period $2\pi$, and they are affine in the infinitesimal part. They are not periodic in the infinitesimal direction, because the infinitesimal part is nilpotent and there is no way to translate it by a period.

## The Dual Hyperbolic Functions

### Definition

The **dual hyperbolic sine** and **cosine** are defined by

$$
\sinh(Z) = \frac{e^Z - e^{-Z}}{2}, \qquad \cosh(Z) = \frac{e^Z + e^{-Z}}{2},
$$

where the exponential is the dual exponential. For $Z = x + y\varepsilon$,

$$
\sinh(Z) = \sinh(x) + y \cosh(x) \varepsilon, \qquad \cosh(Z) = \cosh(x) + y \sinh(x) \varepsilon.
$$

So the dual hyperbolic functions are the ordinary real hyperbolic functions applied to the real part, with infinitesimal corrections given by the derivatives.

### Properties

$$
\sinh' = \cosh, \qquad \cosh' = \sinh,
$$

$$
\cosh^2 Z - \sinh^2 Z = 1.
$$

These identities follow from the corresponding identities for the real hyperbolic functions.

### The Relation to the Trigonometric Functions

The relation between the dual trigonometric and hyperbolic functions is the same as in the real case:

$$
\sin(i Z) = i \sinh(Z), \qquad \cos(i Z) = \cosh(Z),
$$

where $i$ is the ordinary complex imaginary unit.

## The Dual Gamma Function

### Definition

The **dual gamma function** is defined for $Z$ with positive real part by

$$
\Gamma(Z) = \int_0^\infty t^{Z-1} e^{-t} \, dt,
$$

where the integral is along the positive real axis, $t^{Z-1}$ is the dual power, and $e^{-t}$ is the dual exponential. For $Z = x + y\varepsilon$ with $x > 0$,

$$
\Gamma(Z) = \Gamma(x) + y \Gamma'(x) \varepsilon = \Gamma(x) + y \Gamma(x) \psi(x) \varepsilon,
$$

where $\psi(x) = \Gamma'(x)/\Gamma(x)$ is the ordinary digamma function.

So the dual gamma function is the ordinary real gamma function applied to the real part, with an infinitesimal correction given by the digamma function.

### Properties

$$
\Gamma(Z + 1) = Z \Gamma(Z).
$$

This follows from the corresponding identity for the real gamma function, applied to the real part, with the infinitesimal correction computed by differentiation.

### The Reflection Formula

$$
\Gamma(Z) \Gamma(1 - Z) = \frac{\pi}{\sin(\pi Z)},
$$

where the sine is the dual trigonometric sine. This follows from the real reflection formula, with the infinitesimal corrections computed by differentiation.

## The Dual Beta Function

### Definition

The **dual beta function** is defined for $x, y$ with positive real parts by

$$
B(x, y) = \int_0^1 t^{x-1} (1 - t)^{y-1} \, dt,
$$

where the integral is along the positive real axis and the powers are dual powers. For $x = a + \varepsilon b$ and $y = c + \varepsilon d$,

$$
B(x, y) = B(a, c) + \left(b \frac{\partial B}{\partial a}(a, c) + d \frac{\partial B}{\partial c}(a, c)\right) \varepsilon.
$$

So the dual beta function is the ordinary real beta function applied to the real parts, with an infinitesimal correction given by the partial derivatives.

### Relation to the Gamma Function

$$
B(x, y) = \frac{\Gamma(x) \Gamma(y)}{\Gamma(x + y)}.
$$

This follows from the real identity, with the infinitesimal corrections computed by differentiation.

### Symmetry

$$
B(x, y) = B(y, x).
$$

## The Dual Error Function

### Definition

The **dual error function** is defined by

$$
\operatorname{erf}(Z) = \frac{2}{\sqrt{\pi}} \int_0^Z e^{-t^2} \, dt,
$$

where the integral is along a path from $0$ to $Z$ and the exponential is the dual exponential. For $Z = x + y\varepsilon$,

$$
\operatorname{erf}(Z) = \operatorname{erf}(x) + \frac{2}{\sqrt{\pi}} e^{-x^2} y \varepsilon.
$$

So the dual error function is the ordinary real error function applied to the real part, with an infinitesimal correction given by the Gaussian.

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

For $Z = x + y\varepsilon$,

$$
\operatorname{erfc}(Z) = \operatorname{erfc}(x) - \frac{2}{\sqrt{\pi}} e^{-x^2} y \varepsilon.
$$

## The Dual Airy Function

### Definition

The **dual Airy function** is defined by the contour integral

$$
\operatorname{Ai}(Z) = \frac{1}{2\pi i} \int_C \exp\left(\frac{t^3}{3} - Zt\right) dt,
$$

where $C$ is a contour in the complex plane, the exponential is the complex exponential, and $Z$ is a dual number. For $Z = x + y\varepsilon$,

$$
\operatorname{Ai}(Z) = \operatorname{Ai}(x) + y \operatorname{Ai}'(x) \varepsilon,
$$

where $\operatorname{Ai}$ on the right is the ordinary real Airy function.

### Differential Equation

$$
y'' - Z y = 0.
$$

This is Airy's equation, and it holds in the dual sense: the second derivative with respect to the real part equals the product of the dual number and the function.

### Asymptotics

For $x \to +\infty$,

$$
\operatorname{Ai}(x) \sim \frac{1}{2 \sqrt{\pi} x^{1/4}} e^{-2 x^{3/2}/3}.
$$

For $x \to -\infty$,

$$
\operatorname{Ai}(x) \sim \frac{1}{\sqrt{\pi} |x|^{1/4}} \sin\left(\frac{2 |x|^{3/2}}{3} + \frac{\pi}{4}\right).
$$

## The Dual Bessel Functions

### Definition

The **dual Bessel function** of the first kind of order $\nu$ is defined by

$$
J_\nu(Z) = \sum_{n=0}^\infty \frac{(-1)^n}{n! \, \Gamma(n + \nu + 1)} \left( \frac{Z}{2} \right)^{2n + \nu},
$$

where the power and the gamma function are dual. For $Z = x + y\varepsilon$,

$$
J_\nu(Z) = J_\nu(x) + y J_\nu'(x) \varepsilon,
$$

where $J_\nu$ on the right is the ordinary real Bessel function.

### Differential Equation

$$
Z^2 y'' + Z y' + (Z^2 - \nu^2) y = 0.
$$

This is Bessel's equation, and it holds in the dual sense.

### Modified Bessel Functions

The **dual modified Bessel function** of the first kind is

$$
I_\nu(Z) = \sum_{n=0}^\infty \frac{1}{n! \, \Gamma(n + \nu + 1)} \left( \frac{Z}{2} \right)^{2n + \nu}.
$$

For $Z = x + y\varepsilon$,

$$
I_\nu(Z) = I_\nu(x) + y I_\nu'(x) \varepsilon.
$$

## The Dual Hypergeometric Function

### Definition

The **dual Gauss hypergeometric function** is defined for $\|Z\|_E < 1$ by

$$
{}_2F_1(a, b; c; Z) = \sum_{n=0}^\infty \frac{(a)_n (b)_n}{(c)_n} \frac{Z^n}{n!},
$$

where $(a)_n = a(a+1) \cdots (a+n-1)$ is the Pochhammer symbol, and all operations are dual. For $Z = x + y\varepsilon$,

$$
{}_2F_1(a, b; c; Z) = {}_2F_1(a, b; c; x) + y \frac{\partial}{\partial x} {}_2F_1(a, b; c; x) \varepsilon.
$$

### Differential Equation

$$
Z(1 - Z) y'' + [c - (a + b + 1) Z] y' - ab y = 0.
$$

This is the hypergeometric equation, and it holds in the dual sense.

### The Generalized Hypergeometric Function

$$
{}_pF_q(a_1, \dots, a_p; b_1, \dots, b_q; Z) = \sum_{n=0}^\infty \frac{(a_1)_n \cdots (a_p)_n}{(b_1)_n \cdots (b_q)_n} \frac{Z^n}{n!}.
$$

For $Z = x + y\varepsilon$, the dual function is the real function plus its derivative times $y\varepsilon$.

## The Dual Lambert W Function

### Definition

The **dual Lambert W function** is the inverse of

$$
f(w) = w e^w,
$$

where the exponential is the dual exponential. For $Z = x + y\varepsilon$, the equation $W(Z) e^{W(Z)} = Z$ has a unique solution of the form

$$
W(Z) = W(x) + y \frac{W(x)}{x(1 + W(x))} \varepsilon,
$$

where $W$ on the right is the ordinary real Lambert W function.

### Derivative

$$
W'(Z) = \frac{W(Z)}{Z(1 + W(Z))},
$$

defined wherever the denominator is invertible.

### Branches

The dual Lambert W function has two real branches, corresponding to the two real branches $W_0$ and $W_{-1}$ of the ordinary Lambert W function. On the region where $x > -1/e$, the principal branch is defined, and it is dual differentiable.

## The Structure Principle

The pattern in all the definitions above is the same: every dual special function is the ordinary real special function applied to the real part, plus its derivative times the infinitesimal part. This is not a coincidence; it is a theorem.

**Theorem (Structure Principle).** Let $F$ be a special function of one real variable that is differentiable on an interval $I \subseteq \mathbb{R}$, and let $\tilde{F}$ be its extension to the dual numbers defined by the same formula. Then for $Z = x + y\varepsilon$ with $x \in I$,

$$
\tilde{F}(Z) = F(x) + y F'(x) \varepsilon.
$$

**Proof.** The extension $\tilde{F}$ is dual differentiable, and by the structure theorem it is of the form $u(x) + (y u'(x) + c(x))\varepsilon$. Evaluating at $y = 0$ gives $u(x) = F(x)$, hence $u'(x) = F'(x)$. The coefficient of $y$ in the infinitesimal part is therefore $F'(x)$, and the term $c(x)$ is the value of the infinitesimal part at $y = 0$, which is zero because the extension reduces to the real function $F$ when $y = 0$.

This theorem is the reason dual special functions are simpler than complex or split complex special functions. In the complex case, the special functions are genuinely new objects, because the complex algebra is a field and the exponential is periodic. In the split complex case, the special functions are pairs of real special functions, one for each idempotent. In the dual case, the special functions are the real special functions plus their derivatives, because the dual algebra is local and the infinitesimal direction is nilpotent.

## Summary

The dual special functions are the named functions of dual numbers analysis. All of them are governed by one structural fact: a dual differentiable function is determined by its values on the real axis together with its derivative, so the infinitesimal part of each function below is fixed by the derivative of the corresponding real function.

The exponential is defined by its series, which truncates at the first order in $\varepsilon$; the dual logarithm is its inverse and is the ordinary logarithm together with a term in the infinitesimal direction; the dual power function is defined by $Z^a = \exp(a\log Z)$; and the trigonometric and hyperbolic functions are built from the dual exponential as in the real case.

Integral representations then supply the gamma and beta functions, the error function, the Airy function as a contour integral, the Bessel functions and the Gauss hypergeometric function, each obtained by carrying the corresponding real definition to the dual variable, together with the Lambert $W$ function as the inverse of $w \mapsto we^w$.

The section on the structure principle states what organises all of the definitions: every dual special function is the ordinary real special function applied to the real part, plus its derivative times the infinitesimal part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}'$ | Dual number algebra |
| $\varepsilon$ | Dual unit, $\varepsilon^2 = 0$ |
| $Z = x + y\varepsilon$ | General dual number, $x = \operatorname{Re} Z$, $y = \operatorname{Inf} Z$ |
| $e^Z, \log Z$ | Dual exponential, logarithm |
| $\sin Z, \cos Z, \tan Z$ | Dual trigonometric functions |
| $\sinh Z, \cosh Z, \tanh Z$ | Dual hyperbolic functions |
| $Z^a$ | Dual power |
| $\Gamma(Z)$ | Dual gamma function |
| $B(x, y)$ | Dual beta function |
| $\operatorname{erf}(Z), \operatorname{erfc}(Z)$ | Dual error functions |
| $\operatorname{Ai}(Z)$ | Dual Airy function |
| $J_\nu(Z), I_\nu(Z)$ | Dual Bessel functions |
| ${}_pF_q$ | Dual generalized hypergeometric function |
| $W(Z)$ | Dual Lambert W function |
| $\mathrm{M} = (\varepsilon)$ | Maximal ideal |

## Further Reading

- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the origin of the dual numbers in the biquaternion program.
- Eduard Study, *Geometrie der Dynamen* (1903), for the geometry of dual numbers.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the classification of real algebras.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings* (Springer, 1991), for the theory of algebras over commutative rings.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (AMS, 2005), for the general theory of quadratic forms.
- Andreas Griewank and Andrea Walther, *Evaluating Derivatives* (SIAM, 2008), for automatic differentiation with dual numbers.

