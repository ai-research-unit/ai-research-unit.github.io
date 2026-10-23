# __Split-Complex Higher Special Functions__

## Introduction

This article defines the split-complex higher special functions: the Gamma and Beta functions, the error function, the Airy functions, the Bessel functions, the hypergeometric function, and the Lambert $W$ function. Each function is defined once, its basic properties are recorded, and the relations among them are stated.

The article stands on *Split-Complex Elementary Functions*, which owns the exponential, the logarithm, the split-complex powers and the hyperbolic functions, and which states the Idempotent Principle. The algebra, its basis and its conjugation are those of *Split-Complex Algebra*; the norm and the group of units are those of *Norm and Invertibility in the General Split-Complex Algebra*; and the idempotents are those of *Square Roots of One and the Idempotents of the Split-Complex Algebra*. The spectral data are those of *Eigenbasis of a Split-Complex Number*: the eigenvalues

$$
\lambda_+=q+q'=Q_+, \qquad \lambda_-=q-q'=Q_-,
$$

the eigenprojections $\Pi_\pm=\tfrac12(1\pm j)$, the decomposition $Q=\lambda_+\Pi_++\lambda_-\Pi_-$, and the polynomial calculus $f(Q)=f(\lambda_+)\Pi_++f(\lambda_-)\Pi_-$ of §*Powers, Polynomial Calculus, and the Group of Units*. That article owns these results, and they are used here without proof. The idempotent coordinates and the eigenvalues are the same two numbers; this article writes $\lambda_\pm$ whenever the number is read as a value at an idempotent.

This article owns the higher special functions. Each is the componentwise extension of a real special function: the value is the pair of ordinary real values at $\lambda_+$ and $\lambda_-$, written in the idempotent basis. The extension is a theorem for power series and a definition for integrals, inverses and other real formulas (§*The Extension Principle*). The domain is the set of elements whose two eigenvalues lie in the domain of the real formula used; on its boundary the function is undefined, and the boundary is a union of eigenvalue conditions rather than a single curve.

Every numerical value displayed below was recomputed in double precision.

## The Extension Principle

The rule is the Idempotent Principle of *Split-Complex Elementary Functions*, §*The Idempotent Principle*, restated here for reference.

**Theorem (Idempotent Principle).** Let $\Phi(x)=\sum_{n\geq0}c_nx^n$ be a real power series with radius of convergence $\rho$, and let $Q\in\mathbb{D}$ have eigenvalues $\lambda_\pm$ with $\lvert\lambda_\pm\rvert<\rho$. Then the series $\sum c_nQ^n$ converges and

$$
\Phi(Q)=\Phi(\lambda_+)\Pi_++\Phi(\lambda_-)\Pi_-.
$$

For a function defined by an integral, an inverse or another real formula, the same display is the definition of its split-complex extension: the formula is applied to the two eigenvalues, and the value is defined exactly when the real formula is defined at both $\lambda_\pm$. The proof is in *Split-Complex Elementary Functions*, §*The Idempotent Principle*, and is not repeated.

Every function below is read through this rule. The Gamma and Beta functions are defined by integrals; the error, Airy, Bessel and hypergeometric functions by power series or by real formulas; the Lambert $W$ function by an inverse equation. In each case the split-complex function is the pair of ordinary real functions at $\lambda_+$ and $\lambda_-$, so the singular set is the union of the two preimages of the singular set of the real prototype.

## The Gamma Function

### Definition

The **split-complex gamma function** is defined for $Q$ with $\lambda_+>0$ and $\lambda_->0$ by

$$
\Gamma(Q) = \int_0^\infty t^{Q-1} \exp(-t) \, dt,
$$

where the integral is along the positive real axis and $t^{Q-1}$ is the split-complex power of *Split-Complex Elementary Functions*, §*The Power Function*. The integral is read componentwise, so by the Idempotent Principle

$$
\Gamma(Q) = \Gamma(\lambda_+) \Pi_+ + \Gamma(\lambda_-) \Pi_-.
$$

So the split-complex gamma function is the pair of ordinary real gamma functions at the two eigenvalues.

### Functional Equation

$$
\Gamma(Q + 1) = Q \Gamma(Q).
$$

This follows from integration by parts in each eigenvalue component.

### Special Values

$$
\Gamma(n + 1) = n!
$$

for non-negative integers $n$. The scalar $n+1$ has both eigenvalues equal to $n+1$, so the value is the scalar $n!$.

### Reflection Formula

$$
\Gamma(Q)\Gamma(1-Q)=\frac{\pi}{\sin(\pi\lambda_+)}\Pi_++\frac{\pi}{\sin(\pi\lambda_-)}\Pi_-,
$$

with the ordinary real sine at each eigenvalue. The formula is read on $0<\lambda_\pm<1$, where both Gamma factors are defined by the integral.

## The Beta Function

### Definition

The **split-complex beta function** is defined for $Q_1,Q_2$ with $\lambda_{1+}>0$, $\lambda_{1-}>0$, $\lambda_{2+}>0$, $\lambda_{2-}>0$ by

$$
B(Q_1,Q_2) = \int_0^1 t^{Q_1-1} (1 - t)^{Q_2-1} \, dt.
$$

By the Idempotent Principle,

$$
B(Q_1,Q_2) = B(\lambda_{1+},\lambda_{2+}) \Pi_+ + B(\lambda_{1-},\lambda_{2-}) \Pi_-.
$$

### Relation to the Gamma Function

$$
B(Q_1,Q_2) = \frac{\Gamma(Q_1) \Gamma(Q_2)}{\Gamma(Q_1 + Q_2)}.
$$

This follows from the same substitution as in the real case, applied to each eigenvalue component.

### Symmetry

$$
B(Q_1,Q_2) = B(Q_2,Q_1).
$$

## The Error Function

### Definition

The **split-complex error function** is defined by the spectral formula

$$
\operatorname{erf}(Q) = \operatorname{erf}(\lambda_+) \Pi_+ + \operatorname{erf}(\lambda_-) \Pi_-,
$$

where $\operatorname{erf}$ on the right is the real error function. Equivalently,

$$
\operatorname{erf}(Q) = \frac{2}{\sqrt{\pi}} \int_0^Q \exp(-t^2) \, dt,
$$

read componentwise along a path from $0$ to $Q$. So the split-complex error function is the pair of ordinary real error functions at the two eigenvalues.

### Properties

$$
\frac{d}{dQ}\operatorname{erf}(Q) = \frac{2}{\sqrt{\pi}} \exp(-Q^2),
$$

$$
\lim_{Q \to \infty} \operatorname{erf}(Q) = 1, \qquad \lim_{Q \to -\infty} \operatorname{erf}(Q) = -1,
$$

where the limits are taken along the real axis.

### The Complementary Error Function

$$
\operatorname{erfc}(Q) = 1 - \operatorname{erf}(Q) = \frac{2}{\sqrt{\pi}} \int_Q^\infty \exp(-t^2) \, dt.
$$

By the Idempotent Principle, this is the ordinary real complementary error function at each eigenvalue.

## The Airy Functions

### Definition

The **split-complex Airy function** is defined by the spectral formula

$$
\operatorname{Ai}(Q) = \operatorname{Ai}(\lambda_+) \Pi_+ + \operatorname{Ai}(\lambda_-) \Pi_-,
$$

where $\operatorname{Ai}$ on the right is the real Airy function. Equivalently, in each eigenvalue coordinate it is the real Airy function, whose integral representation is

$$
\operatorname{Ai}(x) = \frac{1}{\pi} \int_0^\infty \cos\left(\frac{t^3}{3} + xt\right) dt.
$$

So the split-complex Airy function is the pair of ordinary real Airy functions at the two eigenvalues.

### Differential Equation

$$
\frac{d^2w}{dQ^2} - Q w = 0.
$$

This is Airy's equation in each eigenvalue coordinate.

### Asymptotics

For $\lambda_+ \to +\infty$,

$$
\operatorname{Ai}(\lambda_+) \sim \frac{1}{2 \sqrt{\pi} \lambda_+^{1/4}} \exp(-2 \lambda_+^{3/2}/3).
$$

For $\lambda_+ \to -\infty$,

$$
\operatorname{Ai}(\lambda_+) \sim \frac{1}{\sqrt{\pi} \lvert\lambda_+\rvert^{1/4}} \sin\left(\frac{2 \lvert\lambda_+\rvert^{3/2}}{3} + \frac{\pi}{4}\right).
$$

The same asymptotics hold for $\lambda_-$.

## The Bessel Functions

### Definition

The **split-complex Bessel function** of the first kind of real order $\nu$ is defined by the spectral formula

$$
J_\nu(Q) = J_\nu(\lambda_+) \Pi_+ + J_\nu(\lambda_-) \Pi_-,
$$

where $J_\nu$ on the right is the real Bessel function; for non-integer $\nu$ the eigenvalues are taken positive. Equivalently, at each eigenvalue it is the real series

$$
J_\nu(x) = \sum_{n=0}^\infty \frac{(-1)^n}{n! \, \Gamma(n + \nu + 1)} \left( \frac{x}{2} \right)^{2n + \nu},
$$

with the ordinary real gamma function. So the split-complex Bessel function is the pair of ordinary real Bessel functions at the two eigenvalues.

### Differential Equation

$$
Q^2 \frac{d^2w}{dQ^2} + Q \frac{dw}{dQ} + (Q^2 - \nu^2) w = 0.
$$

This is Bessel's equation in each eigenvalue coordinate.

### Modified Bessel Functions

The **split-complex modified Bessel function** of the first kind is defined by the spectral formula

$$
I_\nu(Q) = I_\nu(\lambda_+) \Pi_+ + I_\nu(\lambda_-) \Pi_-,
$$

where $I_\nu$ on the right is the real modified Bessel function; for non-integer $\nu$ the eigenvalues are taken positive. At each eigenvalue it is the real series

$$
I_\nu(x) = \sum_{n=0}^\infty \frac{1}{n! \, \Gamma(n + \nu + 1)} \left( \frac{x}{2} \right)^{2n + \nu}.
$$

By the Idempotent Principle, it is the ordinary real modified Bessel function at each eigenvalue.

## The Hypergeometric Function

### Definition

The **split-complex Gauss hypergeometric function**, for real parameters $a,b,c$ with $c$ not a nonpositive integer and $\lvert\lambda_+\rvert<1$, $\lvert\lambda_-\rvert<1$, is defined by

$$
{}_2F_1(a, b; c; Q) = \sum_{n=0}^\infty \frac{(a)_n (b)_n}{(c)_n} \frac{Q^n}{n!},
$$

where $(a)_n=a(a+1)\cdots(a+n-1)$ is the Pochhammer symbol and the power is split-complex. By the Idempotent Principle,

$$
{}_2F_1(a, b; c; Q) = {}_2F_1(a, b; c; \lambda_+) \Pi_+ + {}_2F_1(a, b; c; \lambda_-) \Pi_-.
$$

So the split-complex hypergeometric function is the pair of ordinary real hypergeometric functions at the two eigenvalues.

### Differential Equation

$$
Q(1 - Q) \frac{d^2w}{dQ^2} + [c - (a + b + 1) Q] \frac{dw}{dQ} - ab\,w = 0.
$$

This is the hypergeometric equation in each eigenvalue coordinate.

### Special Cases

$$
{}_2F_1(1, 1; 2; Q) = -\frac{\log(1 - Q)}{Q},
\qquad \lambda_\pm\neq0,
$$

$$
{}_2F_1(a, b; b; Q) = (1 - Q)^{-a},
$$

$$
{}_2F_1\left(\frac{1}{2}, \frac{1}{2}; \frac{3}{2}; Q^2\right)
=\frac{\arcsin\lambda_+}{\lambda_+}\Pi_++\frac{\arcsin\lambda_-}{\lambda_-}\Pi_-,
\qquad \lambda_\pm\neq0,
$$

with the ordinary real arcsine at each eigenvalue. The first two displays are read through the Idempotent Principle, and the logarithm and the power are those of *Split-Complex Elementary Functions*, §*The Power Function*.

### The Generalized Hypergeometric Function

$$
{}_pF_q(a_1, \dots, a_p; b_1, \dots, b_q; Q) = \sum_{n=0}^\infty \frac{(a_1)_n \cdots (a_p)_n}{(b_1)_n \cdots (b_q)_n} \frac{Q^n}{n!}.
$$

By the Idempotent Principle, it is the ordinary real generalized hypergeometric function at each eigenvalue.

## The Lambert W Function

### Definition

The **split-complex Lambert W function** is the inverse of

$$
Q \mapsto Q \exp(Q).
$$

That is, $W(Q)$ is any solution of

$$
W(Q) \exp(W(Q)) = Q.
$$

By the Idempotent Principle,

$$
W(Q) = W(\lambda_+) \Pi_+ + W(\lambda_-) \Pi_-,
$$

where $W$ on the right is the ordinary real Lambert W function, with a choice of branch at each eigenvalue.

### Derivative

$$
\frac{d}{dQ}W(Q) = \frac{W(Q)}{Q(1 + W(Q))},
$$

defined wherever the denominator is invertible.

### Branches

The split-complex Lambert W function is defined at each eigenvalue, so it inherits the two real branches $W_0$ and $W_{-1}$ of the ordinary Lambert W function independently at $\lambda_+$ and at $\lambda_-$; its branches are the four combinations obtained by choosing one of $W_0$ and $W_{-1}$ for $\lambda_+$ and one for $\lambda_-$. On the region where $\lambda_+ > -1/e$ and $\lambda_- > -1/e$, the principal branch $W_0$, taken at both eigenvalues, is defined, and it is split-complex differentiable away from $\lambda_\pm=-1/e$.

## Summary

The higher special functions of a split-complex variable are the componentwise extensions of the real special functions to the two eigenvalues. The Gamma function is

$$
\Gamma(Q)=\Gamma(\lambda_+)\Pi_++\Gamma(\lambda_-)\Pi_-,
$$

defined on the elements with $\lambda_\pm>0$ by the integral; it satisfies $\Gamma(Q+1)=Q\Gamma(Q)$ and the reflection formula with the ordinary real sine at each eigenvalue. The Beta function is $B(Q_1,Q_2)=B(\lambda_{1+},\lambda_{2+})\Pi_++B(\lambda_{1-},\lambda_{2-})\Pi_-$, and $B(Q_1,Q_2)=\Gamma(Q_1)\Gamma(Q_2)/\Gamma(Q_1+Q_2)$.

The error function, the Airy function, the Bessel functions and the hypergeometric function are the pairs of their real prototypes at $\lambda_+$ and $\lambda_-$:

$$
\operatorname{erf}(Q)=\operatorname{erf}(\lambda_+)\Pi_++\operatorname{erf}(\lambda_-)\Pi_-,\qquad
\operatorname{Ai}(Q)=\operatorname{Ai}(\lambda_+)\Pi_++\operatorname{Ai}(\lambda_-)\Pi_-,
$$

$$
J_\nu(Q)=J_\nu(\lambda_+)\Pi_++J_\nu(\lambda_-)\Pi_-,\qquad
{}_2F_1(a,b;c;Q)={}_2F_1(a,b;c;\lambda_+)\Pi_++{}_2F_1(a,b;c;\lambda_-)\Pi_-.
$$

The Airy, Bessel and hypergeometric functions satisfy their differential equations in each eigenvalue coordinate, and the modified Bessel and generalized hypergeometric functions follow by the same rule. The Lambert $W$ function is defined by the equation $W(Q)\exp(W(Q))=Q$ and is the pair of real branches at the two eigenvalues; its branches are the four combinations of $W_0$ and $W_{-1}$ at $\lambda_+$ and $\lambda_-$.

The common rule is the Idempotent Principle of *Split-Complex Elementary Functions*: a power series is applied to the two eigenvalues, and an integral, an inverse or another real formula is extended by the same display. The value is defined exactly when the real prototype is defined at both eigenvalues, so the singular set is the union of the two eigenvalue conditions and not a single curve.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | Split-complex algebra |
| $j$ | Split imaginary unit, $j^2=+1$ |
| $Q=q+jq'$ | General split-complex number, $q=\operatorname{Re}Q$, $q'=\operatorname{Im}Q$ |
| $\lambda_\pm=q\pm q'=Q_\pm$ | Eigenvalues, equal to the idempotent coordinates |
| $\Pi_\pm=\tfrac12(1\pm j)$ | Eigenprojections, the standard idempotents |
| $\Gamma(Q)=\Gamma(\lambda_+)\Pi_++\Gamma(\lambda_-)\Pi_-$ | Split-complex gamma function |
| $B(Q_1,Q_2)$ | Split-complex beta function |
| $\operatorname{erf}(Q), \operatorname{erfc}(Q)$ | Split error function, complementary error function |
| $\operatorname{Ai}(Q)$ | Split Airy function |
| $J_\nu(Q), I_\nu(Q)$ | Split Bessel functions |
| ${}_2F_1(a,b;c;Q),\; {}_pF_q$ | Split hypergeometric and generalized hypergeometric functions |
| $(a)_n=a(a+1)\cdots(a+n-1)$ | Pochhammer symbol |
| $W(Q)$ | Split Lambert $W$ function |
| $Q=\lambda_+\Pi_++\lambda_-\Pi_-$ | Eigenvalue decomposition |

## Further Reading

- [Split-Complex Elementary Functions](split-complex-elementary-functions.html), for the Idempotent Principle, the split-complex powers and the hyperbolic functions.
- G. N. Watson, *A Treatise on the Theory of Bessel Functions*, 2nd edition (Cambridge University Press, 1944), for the Bessel functions, their equations and their series.
- Earl D. Rainville, *Special Functions* (Macmillan, 1960), for the hypergeometric function and its special cases.
- E. T. Whittaker and G. N. Watson, *A Course of Modern Analysis*, 4th edition (Cambridge University Press, 1927), for the Gamma function, the Beta function and the asymptotic expansions.
- G. Baley Price, *An Introduction to Multicomplex Spaces and Functions* (Marcel Dekker, 1991), for the extension of the special functions to the multicomplex algebra.
