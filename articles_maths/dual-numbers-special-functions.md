
# __Dual-Numbers Special Functions__

## Introduction

This article introduces the dual numbers special functions as a collection of named functions that arise in dual numbers analysis, in the deformation theory of algebras, and in the infinitesimal geometry of the dual plane. The goal is to define each function precisely, establish its basic properties, and describe the relations among them.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. No examples are given. No specific dimensions. Dual numbers analysis is assumed from the preceding article, and the maximal ideal is used throughout. The functions are defined over the real numbers $\mathbb{R}$, where the exponential, logarithmic and trigonometric series converge and the structure theorem for dual differentiable functions applies; the polynomial identities they satisfy hold over any commutative $\mathbb{Q}$-algebra.

Throughout this article, the dual number algebra is denoted $\mathbb{D}'$, and the split complex algebra is denoted $\mathbb{D}$. The unit of $\mathbb{D}'$ is denoted $\varepsilon$, and it satisfies $\varepsilon^2 = 0$.

## Preliminary: The Structure of Dual Functions

Before defining any special function, it is worth recalling the structural theorem from dual numbers analysis, because it determines the shape of every function in this article.

**Theorem (Structure of dual differentiable functions).** A dual differentiable function $f : U \to \mathbb{D}'$ on a domain $U \subseteq \mathbb{D}'$ is of the form

$$
f(a + \varepsilon a') = u(a) + \left( a' u'(a) + c(a) \right) \varepsilon,
$$

where $u$ and $c$ are ordinary differentiable functions of one real variable.

So every dual differentiable function is determined by two ordinary differentiable functions of one real variable. The real part depends only on $a$; the infinitesimal part is affine in $a'$, with slope the derivative $u'(a)$ of the real part. This is the fundamental constraint, and it is the reason the special functions of dual numbers analysis are simpler than the special functions of complex or split complex analysis.

The functions defined below are of two kinds:

- Functions defined by power series in $\varepsilon$, which are automatically dual differentiable.
- Functions defined by the action of the dual algebra on itself, which are not necessarily differentiable but have algebraic significance.

## The Dual Exponential

### Definition

The **dual exponential** is defined for $A \in \mathbb{D}'$ by

$$
\exp(A) = \sum_{n=0}^\infty \frac{A^n}{n!}.
$$

Because $\varepsilon^2 = 0$, the series truncates at the first order in the infinitesimal part. For $A = a + \varepsilon a'$,

$$
\exp(A) = e^a + e^a a' \varepsilon = e^a (1 + a' \varepsilon).
$$

So the dual exponential is the ordinary real exponential applied to the real part, multiplied by the factor $1 + \varepsilon a'$ in the infinitesimal part.

### Properties

The dual exponential satisfies

$$
\exp(A + B) = \exp(A) \exp(B), \qquad \exp(0) = 1, \qquad \exp'(A) = \exp(A).
$$

**Proof.** The first identity follows from the truncated series and the addition formula for the real exponential:

$$
\exp(a + \varepsilon a') \exp(b + \varepsilon b') = e^a (1 + \varepsilon a') \cdot e^b (1 + \varepsilon b') = e^{a+b} (1 + (a' + b')\varepsilon) = \exp((a + b) + \varepsilon(a' + b')).
$$

The second is immediate. The third follows from term-by-term differentiation of the series, or from the structure theorem applied to the real part.

### The Dual Euler Formula

The dual analogue of Euler's formula is

$$
e^{\varepsilon a'} = 1 + \varepsilon a'.
$$

This is the truncation of the exponential series at first order in $\varepsilon$, and it is the algebraic content of the infinitesimal translation: adding $\varepsilon a'$ to the exponent multiplies the exponential by $1 + \varepsilon a'$, which is an infinitesimal perturbation of the identity.

### The Kernel of the Exponential

The dual exponential is injective on the real part and affine in the infinitesimal part. Its kernel is empty, because $e^a \neq 0$ for all real $a$. So the exponential has no zeros, and it is invertible everywhere.

## The Dual Logarithm

### Definition

The **dual logarithm** is the inverse of the dual exponential. It is defined for $A = a + \varepsilon a'$ with $a > 0$ by

$$
\log(A) = \log(a) + \frac{a'}{a} \varepsilon.
$$

So the dual logarithm is the ordinary real logarithm applied to the real part, plus the infinitesimal correction $a'/a$.

### Properties

The dual logarithm satisfies

$$
\log(A B) = \log(A) + \log(B), \qquad \log(1) = 0, \qquad \log'(A) = \frac{1}{A}.
$$

**Proof.** The first identity follows from the formula and the addition formula for the real logarithm:

$$
\log((a + \varepsilon a')(b + \varepsilon b')) = \log(ab + (ab' + a'b)\varepsilon) = \log(ab) + \frac{ab' + a'b}{ab} \varepsilon = \log(a) + \log(b) + \left(\frac{b'}{b} + \frac{a'}{a}\right) \varepsilon.
$$

The second is immediate. The third follows from the structure theorem applied to the real part, or from the inverse function rule for the exponential.

### The Domain of Definition

The dual logarithm is defined on the set of dual numbers with positive real part. It is not defined on the maximal ideal, because the real part vanishes there. This is the analogue of the branch cut in the complex case, and it is the reason the dual logarithm is only locally defined.

### The Dual Argument

There is no dual analogue of the argument of a complex number, because the dual algebra has no compact group of units. The group of units is the set of dual numbers with non-zero real part, which is not compact. So there is no argument function with values in a compact group: the dual algebra admits no phase, and the dual logarithm of a unit is a real multiple of $\varepsilon$, with no angular part.

## The Dual Power Function

### Definition

For $B \in \mathbb{D}'$ and $A$ in the domain of the dual logarithm, the **dual power** is

$$
A^B = \exp(B \log A).
$$

For $A = a + \varepsilon a'$ and $B = b + \varepsilon b'$, this gives

$$
A^B = a^b \left(1 + \left(\frac{b a'}{a} + b' \log a\right) \varepsilon\right).
$$

So the dual power is the ordinary real power applied to the real parts, with an infinitesimal correction that involves both the infinitesimal part of the base and the infinitesimal part of the exponent.

### Properties

$$
A^{B + C} = A^B A^C, \qquad (A B)^C = A^C B^C, \qquad (A^B)^C = A^{BC}.
$$

These identities follow from the corresponding identities for the exponential and logarithm, applied to the real and infinitesimal parts separately.

### The Case of Integer Exponents

For integer $n$, the dual power reduces to the ordinary power:

$$
A^n = a^n + n a^{n-1} a' \varepsilon.
$$

This is the binomial expansion truncated at first order, and it is the reason the dual power is the algebraic content of the derivative of the power function.

## The Dual Trigonometric Functions

### Definition

The **dual sine** and **cosine** are defined by

$$
\sin(A) = \frac{e^{i A} - e^{-i A}}{2i}, \qquad \cos(A) = \frac{e^{i A} + e^{-i A}}{2},
$$

where $i$ is the ordinary complex imaginary unit and the exponential is the complex exponential. Since $A = a + \varepsilon a'$ is a dual number, the argument $iA$ is a complex number with a dual infinitesimal part, and the functions are defined by the ordinary complex trigonometric functions applied to the real part, with an infinitesimal correction.

Explicitly, for $A = a + \varepsilon a'$,

$$
\sin(A) = \sin(a) + a' \cos(a) \varepsilon, \qquad \cos(A) = \cos(a) - a' \sin(a) \varepsilon.
$$

So the dual trigonometric functions are the ordinary real trigonometric functions applied to the real part, with infinitesimal corrections given by the derivatives.

### Properties

The dual trigonometric functions satisfy

$$
\sin' = \cos, \qquad \cos' = -\sin,
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

These identities follow from the corresponding identities for the real trigonometric functions, applied to the real and infinitesimal parts separately.

### Periodicity

The dual trigonometric functions are periodic in the real part with period $2\pi$, and they are affine in the infinitesimal part. They are not periodic in the infinitesimal direction, because the infinitesimal part is nilpotent and there is no way to translate it by a period.

## The Dual Hyperbolic Functions

### Definition

The **dual hyperbolic sine** and **cosine** are defined by

$$
\sinh(A) = \frac{e^A - e^{-A}}{2}, \qquad \cosh(A) = \frac{e^A + e^{-A}}{2},
$$

where the exponential is the dual exponential. For $A = a + \varepsilon a'$,

$$
\sinh(A) = \sinh(a) + a' \cosh(a) \varepsilon, \qquad \cosh(A) = \cosh(a) + a' \sinh(a) \varepsilon.
$$

So the dual hyperbolic functions are the ordinary real hyperbolic functions applied to the real part, with infinitesimal corrections given by the derivatives.

### Properties

$$
\sinh' = \cosh, \qquad \cosh' = \sinh,
$$

$$
\cosh^2 A - \sinh^2 A = 1.
$$

These identities follow from the corresponding identities for the real hyperbolic functions.

### The Relation to the Trigonometric Functions

The relation between the dual trigonometric and hyperbolic functions is the same as in the real case:

$$
\sin(i A) = i \sinh(A), \qquad \cos(i A) = \cosh(A),
$$

where $i$ is the ordinary complex imaginary unit.

## The Dual Gamma Function

### Definition

The **dual gamma function** is defined for $A$ with positive real part by

$$
\Gamma(A) = \int_0^\infty t^{A-1} e^{-t} \, dt,
$$

where the integral is along the positive real axis, $t^{A-1}$ is the dual power, and $e^{-t}$ is the dual exponential. For $A = a + \varepsilon a'$ with $a > 0$,

$$
\Gamma(A) = \Gamma(a) + a' \Gamma'(a) \varepsilon = \Gamma(a) + a' \Gamma(a) \psi(a) \varepsilon,
$$

where $\psi(a) = \Gamma'(a)/\Gamma(a)$ is the ordinary digamma function.

So the dual gamma function is the ordinary real gamma function applied to the real part, with an infinitesimal correction given by the digamma function.

### Properties

$$
\Gamma(A + 1) = A \Gamma(A).
$$

This follows from the corresponding identity for the real gamma function, applied to the real part, with the infinitesimal correction computed by differentiation.

### The Reflection Formula

$$
\Gamma(A) \Gamma(1 - A) = \frac{\pi}{\sin(\pi A)},
$$

where the sine is the dual trigonometric sine. This follows from the real reflection formula, with the infinitesimal corrections computed by differentiation.

## The Dual Beta Function

### Definition

The **dual beta function** is defined for $A, C$ with positive real parts by

$$
B(A, C) = \int_0^1 t^{A-1} (1 - t)^{C-1} \, dt,
$$

where the integral is along the positive real axis and the powers are dual powers. For $A = a + \varepsilon a'$ and $C = c + \varepsilon c'$,

$$
B(A, C) = B(a, c) + \left(a' \frac{\partial B}{\partial a}(a, c) + c' \frac{\partial B}{\partial c}(a, c)\right) \varepsilon.
$$

So the dual beta function is the ordinary real beta function applied to the real parts, with an infinitesimal correction given by the partial derivatives.

### Relation to the Gamma Function

$$
B(A, C) = \frac{\Gamma(A) \Gamma(C)}{\Gamma(A + C)}.
$$

This follows from the real identity, with the infinitesimal corrections computed by differentiation.

### Symmetry

$$
B(A, C) = B(C, A).
$$

## The Dual Error Function

### Definition

The **dual error function** is defined by

$$
\operatorname{erf}(A) = \frac{2}{\sqrt{\pi}} \int_0^A e^{-t^2} \, dt,
$$

where the integral is along a path from $0$ to $A$ and the exponential is the dual exponential. For $A = a + \varepsilon a'$,

$$
\operatorname{erf}(A) = \operatorname{erf}(a) + \frac{2}{\sqrt{\pi}} e^{-a^2} a' \varepsilon.
$$

So the dual error function is the ordinary real error function applied to the real part, with an infinitesimal correction given by the Gaussian.

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

For $A = a + \varepsilon a'$,

$$
\operatorname{erfc}(A) = \operatorname{erfc}(a) - \frac{2}{\sqrt{\pi}} e^{-a^2} a' \varepsilon.
$$

## The Dual Airy Function

### Definition

The **dual Airy function** is defined by the contour integral

$$
\operatorname{Ai}(A) = \frac{1}{2\pi i} \int_C \exp\left(\frac{t^3}{3} - Zt\right) dt,
$$

where $C$ is a contour in the complex plane, the exponential is the complex exponential, and $A$ is a dual number. For $A = a + \varepsilon a'$,

$$
\operatorname{Ai}(A) = \operatorname{Ai}(a) + a' \operatorname{Ai}'(a) \varepsilon,
$$

where $\operatorname{Ai}$ on the right is the ordinary real Airy function.

### Differential Equation

$$
w'' - A w = 0.
$$

This is Airy's equation, and it holds in the dual sense: the second derivative with respect to the real part equals the product of the dual number and the function.

### Asymptotics

For $a \to +\infty$,

$$
\operatorname{Ai}(a) \sim \frac{1}{2 \sqrt{\pi} a^{1/4}} e^{-2 a^{3/2}/3}.
$$

For $a \to -\infty$,

$$
\operatorname{Ai}(a) \sim \frac{1}{\sqrt{\pi} |a|^{1/4}} \sin\left(\frac{2 |a|^{3/2}}{3} + \frac{\pi}{4}\right).
$$

## The Dual Bessel Functions

### Definition

The **dual Bessel function** of the first kind of order $\nu$ is defined by

$$
J_\nu(A) = \sum_{n=0}^\infty \frac{(-1)^n}{n! \, \Gamma(n + \nu + 1)} \left( \frac{A}{2} \right)^{2n + \nu},
$$

where the power and the gamma function are dual. For $A = a + \varepsilon a'$,

$$
J_\nu(A) = J_\nu(a) + a' J_\nu'(a) \varepsilon,
$$

where $J_\nu$ on the right is the ordinary real Bessel function.

### Differential Equation

$$
A^2 w'' + A w' + (A^2 - \nu^2) w = 0.
$$

This is Bessel's equation, and it holds in the dual sense.

### Modified Bessel Functions

The **dual modified Bessel function** of the first kind is

$$
I_\nu(A) = \sum_{n=0}^\infty \frac{1}{n! \, \Gamma(n + \nu + 1)} \left( \frac{A}{2} \right)^{2n + \nu}.
$$

For $A = a + \varepsilon a'$,

$$
I_\nu(A) = I_\nu(a) + a' I_\nu'(a) \varepsilon.
$$

## The Dual Hypergeometric Function

### Definition

The **dual Gauss hypergeometric function** is defined for $\|A\|_E < 1$ by

$$
{}_2F_1(a, b; c; A) = \sum_{n=0}^\infty \frac{(a)_n (b)_n}{(c)_n} \frac{A^n}{n!},
$$

where $(a)_n = a(a+1) \cdots (a+n-1)$ is the Pochhammer symbol, and all operations are dual. For $A = a + \varepsilon a'$,

$$
{}_2F_1(a, b; c; A) = {}_2F_1(a, b; c; a) + a' \frac{\partial}{\partial a} {}_2F_1(a, b; c; a) \varepsilon.
$$

### Differential Equation

$$
A(1 - A) w'' + [c - (a + b + 1) A] w' - ab w = 0.
$$

This is the hypergeometric equation, and it holds in the dual sense.

### The Generalized Hypergeometric Function

$$
{}_pF_q(a_1, \dots, a_p; b_1, \dots, b_q; A) = \sum_{n=0}^\infty \frac{(a_1)_n \cdots (a_p)_n}{(b_1)_n \cdots (b_q)_n} \frac{A^n}{n!}.
$$

For $A = a + \varepsilon a'$, the dual function is the real function plus its derivative times $a'\varepsilon$.

## The Dual Lambert W Function

### Definition

The **dual Lambert W function** is the inverse of

$$
f(B) = B e^B,
$$

where the exponential is the dual exponential. For $A = a + \varepsilon a'$, the equation $W(A) e^{W(A)} = A$ has a unique solution of the form

$$
W(A) = W(a) + a' \frac{W(a)}{a(1 + W(a))} \varepsilon,
$$

where $W$ on the right is the ordinary real Lambert W function.

### Derivative

$$
W'(A) = \frac{W(A)}{A(1 + W(A))},
$$

defined wherever the denominator is invertible.

### Branches

The dual Lambert W function has two real branches, corresponding to the two real branches $W_0$ and $W_{-1}$ of the ordinary Lambert W function. On the region where $a > -1/e$, the principal branch is defined, and it is dual differentiable.

## The Structure Principle

The pattern in all the definitions above is the same: every dual special function is the ordinary real special function applied to the real part, plus its derivative times the infinitesimal part. This is not a coincidence; it is a theorem.

**Theorem (Structure Principle).** Let $F$ be a special function of one real variable that is differentiable on an interval $I \subseteq \mathbb{R}$, and let $\tilde{F}$ be its extension to the dual numbers defined by the same formula. Then for $A = a + \varepsilon a'$ with $a \in I$,

$$
\tilde{F}(A) = F(a) + a' F'(a) \varepsilon.
$$

**Proof.** The extension $\tilde{F}$ is dual differentiable, and by the structure theorem it is of the form $u(a) + (a' u'(a) + c(a))\varepsilon$. Evaluating at $a' = 0$ gives $u(a) = F(a)$, hence $u'(a) = F'(a)$. The coefficient of $a'$ in the infinitesimal part is therefore $F'(a)$, and the term $c(a)$ is the value of the infinitesimal part at $a' = 0$, which is zero because the extension reduces to the real function $F$ when $a' = 0$.

This theorem is the reason dual special functions are simpler than complex or split complex special functions. In the complex case, the special functions are genuinely new objects, because the complex algebra is a field and the exponential is periodic. In the split complex case, the special functions are pairs of real special functions, one for each idempotent. In the dual case, the special functions are the real special functions plus their derivatives, because the dual algebra is local and the infinitesimal direction is nilpotent.

## Summary

The dual special functions are the named functions of dual numbers analysis. All of them are governed by one structural fact: a dual differentiable function is determined by its values on the real axis together with its derivative, so the infinitesimal part of each function below is fixed by the derivative of the corresponding real function.

The exponential is defined by its series, which truncates at the first order in $\varepsilon$; the dual logarithm is its inverse and is the ordinary logarithm together with a term in the infinitesimal direction; the dual power function is defined by $A^B = \exp(B\log A)$; and the trigonometric and hyperbolic functions are built from the dual exponential as in the real case.

Integral representations then supply the gamma and beta functions, the error function, the Airy function as a contour integral, the Bessel functions and the Gauss hypergeometric function, each obtained by carrying the corresponding real definition to the dual variable, together with the Lambert $W$ function as the inverse of $B \mapsto Be^B$.

The section on the structure principle states what organises all of the definitions: every dual special function is the ordinary real special function applied to the real part, plus its derivative times the infinitesimal part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}'$ | Dual number algebra |
| $\varepsilon$ | Dual unit, $\varepsilon^2 = 0$ |
| $A = a + \varepsilon a'$ | General dual number, $a = \operatorname{Re} A$, $a' = \operatorname{Inf} A$ |
| $e^A, \log A$ | Dual exponential, logarithm |
| $\sin A, \cos A, \tan A$ | Dual trigonometric functions |
| $\sinh A, \cosh A, \tanh A$ | Dual hyperbolic functions |
| $A^B$ | Dual power |
| $\Gamma(A)$ | Dual gamma function |
| $B(A, C)$ | Dual beta function |
| $\operatorname{erf}(A), \operatorname{erfc}(A)$ | Dual error functions |
| $\operatorname{Ai}(A)$ | Dual Airy function |
| $J_\nu(A), I_\nu(A)$ | Dual Bessel functions |
| ${}_pF_q$ | Dual generalized hypergeometric function |
| $W(A)$ | Dual Lambert W function |
| $\mathrm{M} = (\varepsilon)$ | Maximal ideal |

## Further Reading

- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the origin of the dual numbers in the biquaternion program.
- Eduard Study, *Geometrie der Dynamen* (1903), for the geometry of dual numbers.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the classification of real algebras.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings* (Springer, 1991), for the theory of algebras over commutative rings.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (AMS, 2005), for the general theory of quadratic forms.
- Andreas Griewank and Andrea Walther, *Evaluating Derivatives* (SIAM, 2008), for automatic differentiation with dual numbers.

