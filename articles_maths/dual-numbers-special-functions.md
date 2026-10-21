
# __Dual-Numbers Special Functions__

## Introduction

This article introduces the dual numbers special functions as a collection of named functions that arise in dual numbers analysis, in the deformation theory of algebras, and in the infinitesimal geometry of the dual plane. The goal is to define each function precisely, establish its basic properties, and describe the relations among them.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. No examples are given. No specific dimensions. Dual numbers analysis is assumed from the preceding article, and the maximal ideal is used throughout. The functions are defined over the real numbers $\mathbb{R}$, where the exponential, logarithmic and trigonometric series converge and the structure theorem for dual differentiable functions applies; the polynomial identities they satisfy hold over any commutative $\mathbb{Q}$-algebra.

Throughout this article, the dual number algebra is denoted $\mathbb{D}'$, and the split complex algebra is denoted $\mathbb{D}$. The unit of $\mathbb{D}'$ is denoted $\varepsilon$, and it satisfies $\varepsilon^2 = 0$.

## Preliminary: The Structure of Dual Functions

Before defining any special function, it is worth recalling the structural theorem from dual numbers analysis, because it determines the shape of every function in this article.

**Theorem (Structure of dual differentiable functions).** A dual differentiable function $f : \Omega \to \mathbb{D}'$ on a domain $\Omega \subseteq \mathbb{D}'$ is of the form

$$
f(q + \varepsilon q') = u(q) + \left( q' u'(q) + c(q) \right) \varepsilon,
$$

where $u$ and $c$ are ordinary differentiable functions of one real variable.

So every dual differentiable function is determined by two ordinary differentiable functions of one real variable. The real part depends only on $q$; the infinitesimal part is affine in $q'$, with slope the derivative $u'(q)$ of the real part. This is the fundamental constraint, and it is the reason the special functions of dual numbers analysis are simpler than the special functions of complex or split complex analysis.

The functions defined below are of two kinds:

- Functions defined by power series in $\varepsilon$, which are automatically dual differentiable.
- Functions defined by the action of the dual algebra on itself, which are not necessarily differentiable but have algebraic significance.

## The Dual Exponential

### Definition

The **dual exponential** is defined for $Q \in \mathbb{D}'$ by

$$
\exp(Q) = \sum_{n=0}^\infty \frac{Q^n}{n!}.
$$

Because $\varepsilon^2 = 0$, the series truncates at the first order in the infinitesimal part. For $Q = q + \varepsilon q'$,

$$
\exp(Q) = \exp(q) + \exp(q) q' \varepsilon = \exp(q) (1 + q' \varepsilon).
$$

So the dual exponential is the ordinary real exponential applied to the real part, multiplied by the factor $1 + \varepsilon q'$ in the infinitesimal part.

### Properties

The dual exponential satisfies

$$
\exp(Q_1 + Q_2) = \exp(Q_1) \exp(Q_2), \qquad \exp(0) = 1, \qquad \exp'(Q) = \exp(Q).
$$

**Proof.** The first identity follows from the truncated series and the addition formula for the real exponential:

$$
\exp(q_1 + \varepsilon q'_1) \exp(q_2 + \varepsilon q'_2) = \exp(q_1) (1 + \varepsilon q'_1) \cdot \exp(q_2) (1 + \varepsilon q'_2) = \exp(q_1+q_2) (1 + (q'_1 + q'_2)\varepsilon) = \exp((q_1 + q_2) + \varepsilon(q'_1 + q'_2)).
$$

The second is immediate. The third follows from term-by-term differentiation of the series, or from the structure theorem applied to the real part.

### The Dual Euler Formula

The dual analogue of Euler's formula is

$$
\exp(\varepsilon q') = 1 + \varepsilon q'.
$$

This is the truncation of the exponential series at first order in $\varepsilon$, and it is the algebraic content of the infinitesimal translation: adding $\varepsilon q'$ to the exponent multiplies the exponential by $1 + \varepsilon q'$, which is an infinitesimal perturbation of the identity.

### The Kernel of the Exponential

The dual exponential is injective on the real part and affine in the infinitesimal part. Its kernel is empty, because $\exp(q) \neq 0$ for all real $q$. So the exponential has no zeros, and it is invertible everywhere.

## The Dual Logarithm

### Definition

The **dual logarithm** is the inverse of the dual exponential. A logarithm of $Q$ is written $Q_{\log}$, and for $Q = q + \varepsilon q'$ with $q > 0$ it is

$$
Q_{\log} = \log(q) + \frac{q'}{q} \varepsilon.
$$

So the dual logarithm is the ordinary real logarithm applied to the real part, plus the infinitesimal correction $q'/q$.

### Properties

The dual logarithm satisfies

$$
\log(Q_1 Q_2) = \log(Q_1) + \log(Q_2), \qquad \log(1) = 0, \qquad \log'(Q) = \frac{1}{Q}.
$$

**Proof.** The first identity follows from the formula and the addition formula for the real logarithm:

$$
\log((q_1 + \varepsilon q'_1)(q_2 + \varepsilon q'_2)) = \log(q_1q_2 + (q_1q'_2 + q'_1q_2)\varepsilon) = \log(q_1q_2) + \frac{q_1q'_2 + q'_1q_2}{q_1q_2} \varepsilon = \log(q_1) + \log(q_2) + \left(\frac{q'_2}{q_2} + \frac{q'_1}{q_1}\right) \varepsilon.
$$

The second is immediate. The third follows from the structure theorem applied to the real part, or from the inverse function rule for the exponential.

### The Domain of Definition

The dual logarithm is defined on the set of dual numbers with positive real part. It is not defined on the maximal ideal, because the real part vanishes there. This is the analogue of the branch cut in the complex case, and it is the reason the dual logarithm is only locally defined.

### The Dual Argument

There is no dual analogue of the argument of a complex number, because the dual algebra has no compact group of units. The group of units is the set of dual numbers with non-zero real part, which is not compact. So there is no argument function with values in a compact group: the dual algebra admits no phase, and the dual logarithm of a unit is a real multiple of $\varepsilon$, with no angular part.

## The Dual Power Function

### Definition

For $Q_1$ in the domain of the dual logarithm and $Q_2 \in \mathbb{D}'$, the **dual power** is

$$
Q_1^{Q_2} = \exp(Q_2 \log Q_1).
$$

For $Q_1 = q_1 + \varepsilon q'_1$ and $Q_2 = q_2 + \varepsilon q'_2$, this gives

$$
Q_1^{Q_2} = q_1^{q_2} \left(1 + \left(\frac{q_2 q'_1}{q_1} + q'_2 \log q_1\right) \varepsilon\right).
$$

So the dual power is the ordinary real power applied to the real parts, with an infinitesimal correction that involves both the infinitesimal part of the base and the infinitesimal part of the exponent.

### Properties

$$
Q_1^{Q_2 + Q_3} = Q_1^{Q_2} Q_1^{Q_3}, \qquad (Q_1 Q_2)^{Q_3} = Q_1^{Q_3} Q_2^{Q_3}, \qquad (Q_1^{Q_2})^{Q_3} = Q_1^{Q_2Q_3}.
$$

These identities follow from the corresponding identities for the exponential and logarithm, applied to the real and infinitesimal parts separately.

### The Case of Integer Exponents

For integer $n$, the dual power reduces to the ordinary power:

$$
Q^n = q^n + n q^{n-1} q' \varepsilon.
$$

This is the binomial expansion truncated at first order, and it is the reason the dual power is the algebraic content of the derivative of the power function.

## The Dual Trigonometric Functions

### Definition

The **dual sine** and **cosine** are defined by

$$
\sin(Q) = \frac{\exp(i Q) - \exp(-i Q)}{2i}, \qquad \cos(Q) = \frac{\exp(i Q) + \exp(-i Q)}{2},
$$

where $i$ is the ordinary complex imaginary unit and the exponential is the complex exponential. Since $Q = q + \varepsilon q'$ is a dual number, the argument $iQ$ is a complex number with a dual infinitesimal part, and the functions are defined by the ordinary complex trigonometric functions applied to the real part, with an infinitesimal correction.

Explicitly, for $Q = q + \varepsilon q'$,

$$
\sin(Q) = \sin(q) + q' \cos(q) \varepsilon, \qquad \cos(Q) = \cos(q) - q' \sin(q) \varepsilon.
$$

So the dual trigonometric functions are the ordinary real trigonometric functions applied to the real part, with infinitesimal corrections given by the derivatives.

### Properties

The dual trigonometric functions satisfy

$$
\sin' = \cos, \qquad \cos' = -\sin,
$$

$$
\sin(Q_1 + Q_2) = \sin Q_1 \cos Q_2 + \cos Q_1 \sin Q_2,
$$

$$
\cos(Q_1 + Q_2) = \cos Q_1 \cos Q_2 - \sin Q_1 \sin Q_2,
$$

$$
\sin^2 Q + \cos^2 Q = 1.
$$

These identities follow from the corresponding identities for the real trigonometric functions, applied to the real and infinitesimal parts separately.

### Periodicity

The dual trigonometric functions are periodic in the real part with period $2\pi$, and they are affine in the infinitesimal part. They are not periodic in the infinitesimal direction, because the infinitesimal part is nilpotent and there is no way to translate it by a period.

## The Dual Hyperbolic Functions

### Definition

The **dual hyperbolic sine** and **cosine** are defined by

$$
\sinh(Q) = \frac{\exp(Q) - \exp(-Q)}{2}, \qquad \cosh(Q) = \frac{\exp(Q) + \exp(-Q)}{2},
$$

where the exponential is the dual exponential. For $Q = q + \varepsilon q'$,

$$
\sinh(Q) = \sinh(q) + q' \cosh(q) \varepsilon, \qquad \cosh(Q) = \cosh(q) + q' \sinh(q) \varepsilon.
$$

So the dual hyperbolic functions are the ordinary real hyperbolic functions applied to the real part, with infinitesimal corrections given by the derivatives.

### Properties

$$
\sinh' = \cosh, \qquad \cosh' = \sinh,
$$

$$
\cosh^2 Q - \sinh^2 Q = 1.
$$

These identities follow from the corresponding identities for the real hyperbolic functions.

### The Relation to the Trigonometric Functions

The relation between the dual trigonometric and hyperbolic functions is the same as in the real case:

$$
\sin(i Q) = i \sinh(Q), \qquad \cos(i Q) = \cosh(Q),
$$

where $i$ is the ordinary complex imaginary unit.

## The Dual Gamma Function

### Definition

The **dual gamma function** is defined for $Q$ with positive real part by

$$
\Gamma(Q) = \int_0^\infty t^{Q-1} \exp(-t) \, dt,
$$

where the integral is along the positive real axis, $t^{Q-1}$ is the dual power, and $\exp(-t)$ is the dual exponential. For $Q = q + \varepsilon q'$ with $q > 0$,

$$
\Gamma(Q) = \Gamma(q) + q' \Gamma'(q) \varepsilon = \Gamma(q) + q' \Gamma(q) \psi(q) \varepsilon,
$$

where $\psi(q) = \Gamma'(q)/\Gamma(q)$ is the ordinary digamma function.

So the dual gamma function is the ordinary real gamma function applied to the real part, with an infinitesimal correction given by the digamma function.

### Properties

$$
\Gamma(Q + 1) = Q \Gamma(Q).
$$

This follows from the corresponding identity for the real gamma function, applied to the real part, with the infinitesimal correction computed by differentiation.

### The Reflection Formula

$$
\Gamma(Q) \Gamma(1 - Q) = \frac{\pi}{\sin(\pi Q)},
$$

where the sine is the dual trigonometric sine. This follows from the real reflection formula, with the infinitesimal corrections computed by differentiation.

## The Dual Beta Function

### Definition

The **dual beta function** is defined for $Q_1, Q_2$ with positive real parts by

$$
B(Q_1, Q_2) = \int_0^1 t^{Q_1-1} (1 - t)^{Q_2-1} \, dt,
$$

where the integral is along the positive real axis and the powers are dual powers. For $Q_1 = q_1 + \varepsilon q'_1$ and $Q_2 = q_2 + \varepsilon q'_2$,

$$
B(Q_1, Q_2) = B(q_1, q_2) + \left(q'_1 \frac{\partial B}{\partial q_1}(q_1, q_2) + q'_2 \frac{\partial B}{\partial q_2}(q_1, q_2)\right) \varepsilon.
$$

So the dual beta function is the ordinary real beta function applied to the real parts, with an infinitesimal correction given by the partial derivatives.

### Relation to the Gamma Function

$$
B(Q_1, Q_2) = \frac{\Gamma(Q_1) \Gamma(Q_2)}{\Gamma(Q_1 + Q_2)}.
$$

This follows from the real identity, with the infinitesimal corrections computed by differentiation.

### Symmetry

$$
B(Q_1, Q_2) = B(Q_2, Q_1).
$$

## The Dual Error Function

### Definition

The **dual error function** is defined by

$$
\operatorname{erf}(Q) = \frac{2}{\sqrt{\pi}} \int_0^Q \exp(-t^2) \, dt,
$$

where the integral is along a path from $0$ to $Q$ and the exponential is the dual exponential. For $Q = q + \varepsilon q'$,

$$
\operatorname{erf}(Q) = \operatorname{erf}(q) + \frac{2}{\sqrt{\pi}} \exp(-q^2) q' \varepsilon.
$$

So the dual error function is the ordinary real error function applied to the real part, with an infinitesimal correction given by the Gaussian.

### Properties

$$
\operatorname{erf}'(Q) = \frac{2}{\sqrt{\pi}} \exp(-Q^2),
$$

$$
\lim_{Q \to \infty} \operatorname{erf}(Q) = 1, \qquad \lim_{Q \to -\infty} \operatorname{erf}(Q) = -1,
$$

where the limits are taken along the real axis.

### The Complementary Error Function

$$
\operatorname{erfc}(Q) = 1 - \operatorname{erf}(Q) = \frac{2}{\sqrt{\pi}} \int_Q^\infty \exp(-t^2) \, dt.
$$

For $Q = q + \varepsilon q'$,

$$
\operatorname{erfc}(Q) = \operatorname{erfc}(q) - \frac{2}{\sqrt{\pi}} \exp(-q^2) q' \varepsilon.
$$

## The Dual Airy Function

### Definition

The **dual Airy function** is defined by the contour integral

$$
\operatorname{Ai}(Q) = \frac{1}{2\pi i} \int_C \exp\left(\frac{t^3}{3} - Qt\right) dt,
$$

where $C$ is a contour in the complex plane, the exponential is the complex exponential, and $Q$ is a dual number. For $Q = q + \varepsilon q'$,

$$
\operatorname{Ai}(Q) = \operatorname{Ai}(q) + q' \operatorname{Ai}'(q) \varepsilon,
$$

where $\operatorname{Ai}$ on the right is the ordinary real Airy function.

### Differential Equation

$$
w'' - Q w = 0.
$$

This is Airy's equation, and it holds in the dual sense: the second derivative with respect to the real part equals the product of the dual number and the function.

### Asymptotics

For $q \to +\infty$,

$$
\operatorname{Ai}(q) \sim \frac{1}{2 \sqrt{\pi} q^{1/4}} \exp(-2 q^{3/2}/3).
$$

For $q \to -\infty$,

$$
\operatorname{Ai}(q) \sim \frac{1}{\sqrt{\pi} |q|^{1/4}} \sin\left(\frac{2 |q|^{3/2}}{3} + \frac{\pi}{4}\right).
$$

## The Dual Bessel Functions

### Definition

The **dual Bessel function** of the first kind of order $\nu$ is defined by

$$
J_\nu(Q) = \sum_{n=0}^\infty \frac{(-1)^n}{n! \, \Gamma(n + \nu + 1)} \left( \frac{Q}{2} \right)^{2n + \nu},
$$

where the power and the gamma function are dual. For $Q = q + \varepsilon q'$,

$$
J_\nu(Q) = J_\nu(q) + q' J_\nu'(q) \varepsilon,
$$

where $J_\nu$ on the right is the ordinary real Bessel function.

### Differential Equation

$$
Q^2 w'' + Q w' + (Q^2 - \nu^2) w = 0.
$$

This is Bessel's equation, and it holds in the dual sense.

### Modified Bessel Functions

The **dual modified Bessel function** of the first kind is

$$
I_\nu(Q) = \sum_{n=0}^\infty \frac{1}{n! \, \Gamma(n + \nu + 1)} \left( \frac{Q}{2} \right)^{2n + \nu}.
$$

For $Q = q + \varepsilon q'$,

$$
I_\nu(Q) = I_\nu(q) + q' I_\nu'(q) \varepsilon.
$$

## The Dual Hypergeometric Function

### Definition

The **dual Gauss hypergeometric function** is defined for $\|Q\|_E < 1$ by

$$
{}_2F_1(a, b; c; Q) = \sum_{n=0}^\infty \frac{(a)_n (b)_n}{(c)_n} \frac{Q^n}{n!},
$$

where $(a)_n = a(a+1) \cdots (a+n-1)$ is the Pochhammer symbol, and all operations are dual. For $Q = q + \varepsilon q'$,

$$
{}_2F_1(a, b; c; Q) = {}_2F_1(a, b; c; q) + q' \frac{\partial}{\partial q} {}_2F_1(a, b; c; q) \varepsilon.
$$

### Differential Equation

$$
Q(1 - Q) w'' + [c - (a + b + 1) Q] w' - ab w = 0.
$$

This is the hypergeometric equation, and it holds in the dual sense.

### The Generalized Hypergeometric Function

$$
{}_pF_q(a_1, \dots, a_p; b_1, \dots, b_q; Q) = \sum_{n=0}^\infty \frac{(a_1)_n \cdots (a_p)_n}{(b_1)_n \cdots (b_q)_n} \frac{Q^n}{n!}.
$$

For $Q = q + \varepsilon q'$, the dual function is the real function plus its derivative times $q'\varepsilon$.

## The Dual Lambert W Function

### Definition

The **dual Lambert W function** is the inverse of

$$
f(Q) = Q \exp(Q),
$$

where the exponential is the dual exponential. For $Q = q + \varepsilon q'$, the equation $W(Q) \exp(W(Q)) = Q$ has a unique solution of the form

$$
W(Q) = W(q) + q' \frac{W(q)}{q(1 + W(q))} \varepsilon,
$$

where $W$ on the right is the ordinary real Lambert W function.

### Derivative

$$
W'(Q) = \frac{W(Q)}{Q(1 + W(Q))},
$$

defined wherever the denominator is invertible.

### Branches

The dual Lambert W function has two real branches, corresponding to the two real branches $W_0$ and $W_{-1}$ of the ordinary Lambert W function. On the region where $q > -1/e$, the principal branch is defined, and it is dual differentiable.

## The Structure Principle

The pattern in all the definitions above is the same: every dual special function is the ordinary real special function applied to the real part, plus its derivative times the infinitesimal part. This is not a coincidence; it is a theorem.

**Theorem (Structure Principle).** Let $F$ be a special function of one real variable that is differentiable on an interval $I \subseteq \mathbb{R}$, and let $F^{\mathrm{ext}}$ be its extension to the dual numbers defined by the same formula. Then for $Q = q + \varepsilon q'$ with $q \in I$,

$$
F^{\mathrm{ext}}(Q) = F(q) + q' F'(q) \varepsilon.
$$

**Proof.** The extension $F^{\mathrm{ext}}$ is dual differentiable, and by the structure theorem it is of the form $u(q) + (q' u'(q) + c(q))\varepsilon$. Evaluating at $q' = 0$ gives $u(q) = F(q)$, hence $u'(q) = F'(q)$. The coefficient of $q'$ in the infinitesimal part is therefore $F'(q)$, and the term $c(q)$ is the value of the infinitesimal part at $q' = 0$, which is zero because the extension reduces to the real function $F$ when $q' = 0$.

This theorem is the reason dual special functions are simpler than complex or split complex special functions. In the complex case, the special functions are genuinely new objects, because the complex algebra is a field and the exponential is periodic. In the split complex case, the special functions are pairs of real special functions, one for each idempotent. In the dual case, the special functions are the real special functions plus their derivatives, because the dual algebra is local and the infinitesimal direction is nilpotent.

## Summary

The dual special functions are the named functions of dual numbers analysis. All of them are governed by one structural fact: a dual differentiable function is determined by its values on the real axis together with its derivative, so the infinitesimal part of each function below is fixed by the derivative of the corresponding real function.

The exponential is defined by its series, which truncates at the first order in $\varepsilon$; the dual logarithm is its inverse and is the ordinary logarithm together with a term in the infinitesimal direction; the dual power function is defined by $Q_1^{Q_2} = \exp(Q_2\log Q_1)$; and the trigonometric and hyperbolic functions are built from the dual exponential as in the real case.

Integral representations then supply the gamma and beta functions, the error function, the Airy function as a contour integral, the Bessel functions and the Gauss hypergeometric function, each obtained by carrying the corresponding real definition to the dual variable, together with the Lambert $W$ function as the inverse of $Q \mapsto Q\exp(Q)$.

The section on the structure principle states what organises all of the definitions: every dual special function is the ordinary real special function applied to the real part, plus its derivative times the infinitesimal part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}'$ | Dual number algebra |
| $\varepsilon$ | Dual unit, $\varepsilon^2 = 0$ |
| $Q = q + \varepsilon q'$ | General dual number, $q = \operatorname{Re} Q$, $q' = \operatorname{Inf} Q$ |
| $\exp(Q), \log Q$ | Dual exponential, logarithm |
| $\sin Q, \cos Q, \tan Q$ | Dual trigonometric functions |
| $\sinh Q, \cosh Q, \tanh Q$ | Dual hyperbolic functions |
| $Q_1^{Q_2}$ | Dual power |
| $\Gamma(Q)$ | Dual gamma function |
| $B(Q_1, Q_2)$ | Dual beta function |
| $\operatorname{erf}(Q), \operatorname{erfc}(Q)$ | Dual error functions |
| $\operatorname{Ai}(Q)$ | Dual Airy function |
| $J_\nu(Q), I_\nu(Q)$ | Dual Bessel functions |
| ${}_pF_q$ | Dual generalized hypergeometric function |
| $W(Q)$ | Dual Lambert W function |
| $\mathrm{M} = (\varepsilon)$ | Maximal ideal |

## Further Reading

- Eduard Study, *Geometrie der Dynamen* (1903), for the geometry of dual numbers.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings* (Springer, 1991), for the theory of algebras over commutative rings.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (AMS, 2005), for the general theory of quadratic forms.
- Andreas Griewank and Andrea Walther, *Evaluating Derivatives* (SIAM, 2008), for automatic differentiation with dual numbers.

