
# Biquaternion Higher Special Functions

## Introduction

This article introduces the higher special functions of a biquaternion variable. It follows the article on biquaternion elementary functions, which defined the exponential, the trigonometric and hyperbolic functions, the logarithm, and the power functions, and which established the two regimes: the **oscillatory regime** ($\theta \neq 0$) and the **nilpotent regime** ($\theta = 0$), where $\theta = \sqrt{Q_1^2 + Q_2^2 + Q_3^2}$ is the complex norm of the vector part.

The goal is to define the Bessel functions, the orthogonal polynomials, the hypergeometric function, the gamma function, and the zeta function, and to establish their basic properties. The article is honest about what is fully understood and what is still open.

The treatment is purely mathematical. No physics is invoked. No examples are given. The biquaternion algebra $\mathbb{B}$ is assumed from the basic algebra article, together with its scalar-vector decomposition, its norm form, and its four conjugations. The elementary functions are assumed from the preceding article, together with the two regimes and the Hamilton polar form.

Throughout, a biquaternion is written

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3, \qquad Q_\mu \in \mathbb{C},
$$

or, more compactly, as

$$
\tilde{Q} = Q_0 e_0 + \mathbf{Q}, \qquad \mathbf{Q} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3.
$$

The complex norm of the vector part is $\theta = \sqrt{Q_1^2 + Q_2^2 + Q_3^2}$, and the axis is $\hat{n} = \mathbf{Q}/\theta$ when $\theta \neq 0$.

The higher special functions fall into two classes according to their definition:

- **Power-series functions.** These are defined by a power series, and the same technique as for the exponential applies: the series is summed in closed form in the two regimes. The Bessel functions, the orthogonal polynomials, and the hypergeometric function belong to this class.
- **Integral-defined functions.** These are defined by an integral over a real or complex parameter. The extension to biquaternions requires a notion of the integrand for biquaternion arguments, and the convergence and analyticity of the integral are not automatic. The gamma function and the zeta function belong to this class.

The first class is treated in full; the second is treated with the open questions stated honestly.

## Bessel Functions

### Definition

The **Bessel function of the first kind** of order $\nu$ is defined by the power series

$$
J_\nu(\tilde{Q}) = \sum_{m=0}^{\infty} \frac{(-1)^m}{m! \, \Gamma(m + \nu + 1)} \left(\frac{\tilde{Q}}{2}\right)^{2m+\nu}.
$$

The series converges for every $\tilde{Q} \in \mathbb{B}$, because the Euclidean norm grows at most exponentially with $m$. So $J_\nu$ is an entire function on $\mathbb{B}$ for every $\nu \in \mathbb{C}$.

### Reduction to the Vector Part

Write $\tilde{Q} = Q_0 e_0 + \mathbf{Q}$. The scalar part $Q_0 e_0$ commutes with $\mathbf{Q}$, so the powers of $\tilde{Q}$ do not simplify in the same way as for the exponential. The Bessel function of a general biquaternion is therefore not reducible to a simple closed form in terms of the scalar and vector parts.

However, there are two special cases in which the reduction works:

- **Pure biquaternions.** If $Q_0 = 0$, then $\tilde{Q} = \mathbf{Q}$, and the powers of $\mathbf{Q}$ simplify as in the elementary case.
- **Biquaternions with a single direction.** If $\tilde{Q} = Q_0 e_0 + \theta \hat{n}$ with $\hat{n}$ fixed, the powers of $\tilde{Q}$ can be computed by the binomial expansion, but the binomial coefficients are biquaternions in general.

We treat the pure case in detail, and we state the general case as an open problem.

### The Pure Case, Oscillatory Regime

Let $\tilde{Q} = \mathbf{Q} = \theta \hat{n}$ with $\theta \neq 0$ and $\hat{n}^2 = -e_0$. The powers of $\mathbf{Q}$ satisfy

$$
\mathbf{Q}^{2m+\nu} = \theta^{2m+\nu} \hat{n}^{2m+\nu}.
$$

The powers of $\hat{n}$ alternate:

$$
\hat{n}^{2k} = (-1)^k e_0, \qquad \hat{n}^{2k+1} = (-1)^k \hat{n}.
$$

Substituting into the series and separating even and odd powers, we obtain

$$
J_\nu(\theta \hat{n}) = \left(\sum_{m=0}^{\infty} \frac{(-1)^m \theta^{2m+\nu}}{m! \, \Gamma(m+\nu+1) 2^{2m+\nu}} \hat{n}^{2m+\nu}\right).
$$

The parity of $\hat{n}^{2m+\nu}$ depends on the parity of $\nu$. If $\nu$ is an integer, the sum splits into two cases: $\nu$ even gives only the identity $e_0$, and $\nu$ odd gives only $\hat{n}$. In general, for non-integer $\nu$, the series does not split into two separate series.

For integer $\nu = n$, the result is

$$
J_n(\theta \hat{n}) = \begin{cases} (-1)^{n/2} I_n(\theta) \, e_0 & \text{if } n \text{ is even}, \\ (-1)^{(n-1)/2} I_n(\theta) \, \hat{n} & \text{if } n \text{ is odd}, \end{cases}
$$

where $I_n(\theta)$ on the right is the ordinary complex modified Bessel function. The verification is a direct substitution of the alternating powers of $\hat{n}$.

### The Pure Case, Nilpotent Regime

Let $\tilde{Q} = \mathbf{Q}$ with $\theta = 0$ and $\mathbf{Q} \neq 0$. Then $\mathbf{Q}^2 = 0$, so $\mathbf{Q}^m = 0$ for all $m \geq 2$. The Bessel series truncates:

$$
J_\nu(\mathbf{Q}) = \frac{1}{\Gamma(\nu+1)} \left(\frac{\mathbf{Q}}{2}\right)^\nu + \frac{(-1)^1}{1! \, \Gamma(\nu+2)} \left(\frac{\mathbf{Q}}{2}\right)^{\nu+2} + \cdots
$$

Only the terms with $2m + \nu \leq 1$ contribute. For general $\nu$, the terms with $2m + \nu \geq 2$ vanish. So the series reduces to at most two terms, depending on the value of $\nu$. For integer $\nu = n \geq 0$, the series reduces to

$$
J_n(\mathbf{Q}) = \begin{cases} \frac{1}{n!} \left(\frac{\mathbf{Q}}{2}\right)^n & \text{if } n = 0 \text{ or } n = 1, \\ 0 & \text{if } n \geq 2, \end{cases}
$$

where for $n = 0$ the term is $e_0$ and for $n = 1$ the term is $\mathbf{Q}/2$. For non-integer $\nu$, the series reduces to the terms with $2m + \nu < 2$.

### The General Case

For a general biquaternion $\tilde{Q} = Q_0 e_0 + \mathbf{Q}$ with both $Q_0 \neq 0$ and $\mathbf{Q} \neq 0$, the Bessel function does not reduce to a closed form in terms of elementary functions. The powers of $\tilde{Q}$ involve the non-commutative products of $Q_0 e_0$ and $\mathbf{Q}$, and the series is a genuine biquaternion series.

The general case is open. The natural approach would be to use the Hamilton polar form $\tilde{Q} = e^{Q_0} \exp(\theta \hat{n})$ and to express $J_\nu(\tilde{Q})$ in terms of $J_\nu$ evaluated at the polar factors, but the functional equation for the Bessel function under multiplication does not hold in general, because the Bessel function is not multiplicative.

### Modified Bessel Functions

The **modified Bessel function** of the first kind is defined by

$$
I_\nu(\tilde{Q}) = \sum_{m=0}^{\infty} \frac{1}{m! \, \Gamma(m + \nu + 1)} \left(\frac{\tilde{Q}}{2}\right)^{2m+\nu}.
$$

The same analysis applies: in the pure oscillatory regime, the result is expressed in terms of the ordinary modified Bessel function; in the pure nilpotent regime, the series truncates.

## Orthogonal Polynomials

### Legendre Polynomials

The **Legendre polynomials** $P_n(\tilde{Q})$ are defined by the generating function

$$
\frac{1}{\sqrt{1 - 2\tilde{Q} t + t^2}} = \sum_{n=0}^{\infty} P_n(\tilde{Q}) t^n, \qquad |t| < 1,
$$

where $t$ is a real parameter and the square root is the biquaternion square root (defined via the elementary functions). Equivalently, they satisfy the recurrence

$$
(n+1) P_{n+1}(\tilde{Q}) = (2n+1) \tilde{Q} P_n(\tilde{Q}) - n P_{n-1}(\tilde{Q}),
$$

with $P_0 = e_0$ and $P_1 = \tilde{Q}$.

The Legendre polynomials are polynomials in $\tilde{Q}$ with real coefficients (the coefficients are the ordinary Legendre coefficients, embedded as real scalars). So they are defined for every $\tilde{Q} \in \mathbb{B}$ by the recurrence, and the recurrence involves only the multiplication and addition of biquaternions.

**The pure oscillatory case.** For $\tilde{Q} = \theta \hat{n}$ with $\theta \neq 0$ and $\hat{n}^2 = -e_0$, the recurrence gives

$$
P_n(\theta \hat{n}) = \begin{cases} P_n(\theta) \, e_0 & \text{if } n \text{ is even}, \\ P_n(\theta) \, \hat{n} & \text{if } n \text{ is odd}, \end{cases}
$$

where $P_n(\theta)$ is the ordinary Legendre polynomial evaluated at the complex number $\theta$. This follows from the recurrence and the alternating powers of $\hat{n}$.

**The pure nilpotent case.** For $\tilde{Q} = \mathbf{Q}$ with $\mathbf{Q}^2 = 0$, the recurrence involves powers of $\mathbf{Q}$ that truncate. In particular, $P_n(\mathbf{Q})$ is a polynomial in $\mathbf{Q}$ of degree at most one, because $\mathbf{Q}^2 = 0$. The explicit form is obtained from the recurrence.

### Chebyshev Polynomials

The **Chebyshev polynomials of the first kind** $T_n(\tilde{Q})$ are defined by the recurrence

$$
T_{n+1}(\tilde{Q}) = 2\tilde{Q} T_n(\tilde{Q}) - T_{n-1}(\tilde{Q}),
$$

with $T_0 = e_0$ and $T_1 = \tilde{Q}$. The same analysis applies: in the pure oscillatory regime, the polynomials reduce to the ordinary Chebyshev polynomials evaluated at $\theta$, with the parity determined by $n$; in the pure nilpotent regime, the polynomials truncate.

### Hermite Polynomials

The **Hermite polynomials** $H_n(\tilde{Q})$ are defined by the recurrence

$$
H_{n+1}(\tilde{Q}) = 2\tilde{Q} H_n(\tilde{Q}) - 2n H_{n-1}(\tilde{Q}),
$$

with $H_0 = e_0$ and $H_1 = 2\tilde{Q}$. The same analysis applies.

### Laguerre Polynomials

The **Laguerre polynomials** $L_n(\tilde{Q})$ are defined by the recurrence

$$
(n+1) L_{n+1}(\tilde{Q}) = (2n+1-\tilde{Q}) L_n(\tilde{Q}) - n L_{n-1}(\tilde{Q}),
$$

with $L_0 = e_0$ and $L_1 = e_0 - \tilde{Q}$. The same analysis applies.

### The General Principle for Polynomials

The orthogonal polynomials are defined by three-term recurrences involving only the multiplication and addition of biquaternions. So they are defined for every $\tilde{Q} \in \mathbb{B}$, and they reduce to the ordinary polynomials in the two pure regimes:

- In the pure oscillatory regime, the polynomial $P_n(\theta \hat{n})$ reduces to $P_n(\theta) e_0$ or $P_n(\theta) \hat{n}$, depending on the parity of $n$.
- In the pure nilpotent regime, the polynomial truncates to a polynomial of degree at most one in $\mathbf{Q}$.

The general case (with both $Q_0 \neq 0$ and $\mathbf{Q} \neq 0$) does not reduce to a closed form, because the recurrence involves the non-commutative product $Q_0 \mathbf{Q}$, and the polynomial is a genuine biquaternion polynomial.

## Hypergeometric Function

### Definition

The **Gauss hypergeometric function** is defined by the power series

$$
{}_2F_1(a, b; c; \tilde{Q}) = \sum_{n=0}^{\infty} \frac{(a)_n (b)_n}{(c)_n} \frac{\tilde{Q}^n}{n!},
$$

where $(a)_n = a(a+1) \cdots (a+n-1)$ is the Pochhammer symbol, and $a, b, c \in \mathbb{C}$. The series converges for $\|\tilde{Q}\|_E < 1$.

### The Pure Oscillatory Case

For $\tilde{Q} = \theta \hat{n}$ with $\theta \neq 0$ and $\hat{n}^2 = -e_0$, the powers of $\tilde{Q}$ alternate. Separating even and odd powers,

$$
{}_2F_1(a, b; c; \theta \hat{n}) = \left(\sum_{n=0}^{\infty} \frac{(a)_{2n} (b)_{2n}}{(c)_{2n}} \frac{(-1)^n \theta^{2n}}{(2n)!}\right) e_0 + \left(\sum_{n=0}^{\infty} \frac{(a)_{2n+1} (b)_{2n+1}}{(c)_{2n+1}} \frac{(-1)^n \theta^{2n+1}}{(2n+1)!}\right) \hat{n}.
$$

The two series are not the ordinary hypergeometric function evaluated at $\theta$, because the Pochhammer symbols are evaluated at $2n$ and $2n+1$, not at $n$. They are the **even and odd parts** of the hypergeometric function, and they can be expressed in terms of ${}_2F_1$ with different parameters. The precise form is an open problem.

### The Pure Nilpotent Case

For $\tilde{Q} = \mathbf{Q}$ with $\mathbf{Q}^2 = 0$, the powers of $\tilde{Q}$ truncate, and the hypergeometric series reduces to

$$
{}_2F_1(a, b; c; \mathbf{Q}) = e_0 + \frac{ab}{c} \mathbf{Q}.
$$

The higher terms vanish because $\mathbf{Q}^n = 0$ for $n \geq 2$. This is the analogue of the linear approximation of the hypergeometric function near zero.

### Special Cases

The special cases of the hypergeometric function that involve only the elementary functions (the logarithm, the arcsine, the power function) reduce to the elementary functions of a biquaternion variable, which are treated in the preceding article. The general hypergeometric function does not reduce to the elementary functions.

### The Generalized Hypergeometric Function

The **generalized hypergeometric function** ${}_pF_q$ is defined by

$$
{}_pF_q(a_1, \dots, a_p; b_1, \dots, b_q; \tilde{Q}) = \sum_{n=0}^{\infty} \frac{(a_1)_n \cdots (a_p)_n}{(b_1)_n \cdots (b_q)_n} \frac{\tilde{Q}^n}{n!}.
$$

The same analysis applies: in the pure oscillatory regime, the series splits into even and odd parts; in the pure nilpotent regime, the series truncates.

## The Gamma Function

### The Definition Problem

The **gamma function** of a complex variable is defined by the integral

$$
\Gamma(z) = \int_0^\infty t^{z-1} e^{-t} \, dt, \qquad \operatorname{Re} z > 0.
$$

The natural extension to a biquaternion variable would be

$$
\Gamma(\tilde{Q}) = \int_0^\infty t^{\tilde{Q}-1} e^{-t} \, dt,
$$

where $t$ is a positive real number, $t^{\tilde{Q}-1} = \exp((\tilde{Q}-1) \log t)$ is the biquaternion power, and $e^{-t}$ is the ordinary real exponential.

### The Obstruction

The integral is defined component-wise, but the integrand is a biquaternion-valued function of the real variable $t$, and the convergence of the integral depends on the growth of $t^{\tilde{Q}-1}$ as $t \to 0$ and as $t \to \infty$.

**As $t \to 0$.** The biquaternion power $t^{\tilde{Q}-1}$ involves $\log t$, which tends to $-\infty$. The behavior depends on the scalar part $Q_0$ and on the vector part $\mathbf{Q}$. In the oscillatory regime, the power is $t^{Q_0-1}(\cos((Q_0-1)\log t \cdot \hat{n}) + \cdots)$, which oscillates and may not converge. In the nilpotent regime, the power is $t^{Q_0-1}(e_0 + (Q_0-1)\log t \cdot \mathbf{Q})$, which converges if $\operatorname{Re} Q_0 > 0$.

**As $t \to \infty$.** The factor $e^{-t}$ dominates, so the integral converges for all $\tilde{Q}$ with $\operatorname{Re} Q_0 < \infty$.

So the integral converges in the nilpotent regime if $\operatorname{Re} Q_0 > 0$, and its convergence in the oscillatory regime is an open problem.

### What Is Known

The gamma function is well-defined in the nilpotent regime for $\operatorname{Re} Q_0 > 0$, and it can be computed in closed form. However, the analytic continuation, the functional equation $\Gamma(\tilde{Q}+1) = \tilde{Q} \Gamma(\tilde{Q})$, and the reflection formula are not established in general. These are open problems.

### The Open Questions

1. **Convergence.** For which biquaternions $\tilde{Q}$ does the integral converge?

2. **Functional equation.** Does the functional equation $\Gamma(\tilde{Q}+1) = \tilde{Q} \Gamma(\tilde{Q})$ hold? The proof in the complex case uses integration by parts, which requires the boundary terms to vanish. In the biquaternion case, the boundary terms involve the biquaternion power, and their vanishing is not automatic.

3. **Analytic continuation.** Can the gamma function be continued beyond the region of convergence of the integral?

4. **The reflection formula.** Does the reflection formula $\Gamma(\tilde{Q}) \Gamma(e_0 - \tilde{Q}) = \pi / \sin(\pi \tilde{Q})$ hold?

These questions are open.

## The Zeta Function

### The Definition Problem

The **Riemann zeta function** of a complex variable is defined by the Dirichlet series

$$
\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s}, \qquad \operatorname{Re} s > 1.
$$

The natural extension to a biquaternion variable would be

$$
\zeta(\tilde{Q}) = \sum_{n=1}^{\infty} \frac{1}{n^{\tilde{Q}}},
$$

where $n^{\tilde{Q}} = \exp(\tilde{Q} \log n)$ is the biquaternion power.

### The Obstruction

The series is a series of biquaternions. The convergence depends on the behavior of $n^{\tilde{Q}}$ as $n \to \infty$. In the oscillatory regime, $n^{\tilde{Q}}$ involves $\cos(\theta \log n)$ and $\sin(\theta \log n)$, which oscillate. The series may converge conditionally or may not converge at all, depending on $\tilde{Q}$.

In the nilpotent regime, $n^{\tilde{Q}} = n^{Q_0}(e_0 + Q_0 \log n \cdot \mathbf{Q})$, and the series converges absolutely if $\operatorname{Re} Q_0 > 1$.

### What Is Known

Almost nothing is known about the biquaternion zeta function. The following are open problems.

### The Open Questions

1. **Convergence.** For which biquaternions $\tilde{Q}$ does the series converge?

2. **The Euler product.** The Euler product $\zeta(s) = \prod_p (1 - p^{-s})^{-1}$ requires the multiplicativity of the power function, which does not hold in the biquaternion case. Is there an analogue?

3. **Analytic continuation.** Can the zeta function be continued beyond the region of convergence?

4. **Special values.** Are there biquaternion analogues of the special values $\zeta(2) = \pi^2/6$, $\zeta(4) = \pi^4/90$, etc.?

5. **The functional equation.** Is there a biquaternion analogue of the functional equation relating $\zeta(\tilde{Q})$ to $\zeta(e_0 - \tilde{Q})$?

6. **The Riemann hypothesis.** Is there an analogue of the Riemann hypothesis?

These questions are entirely open. The biquaternion zeta function is a research problem, not a developed theory.

## Special Functions from the Analysis

### The Setting

The analysis article defined the biquaternion gradient $\tilde{\nabla}$, the d'Alembertian $\Box$, and the convective derivative $\tilde{D}$ on a four-dimensional subspace $V \subset \mathbb{B}$. The solutions of the equations

$$
\tilde{\nabla}\tilde{F} = 0, \qquad \Box\tilde{F} = 0
$$

are the biquaternion analogues of holomorphic functions and harmonic functions. The special functions of the analysis are the kernels and fundamental solutions associated with these equations.

### The Cauchy Kernel

The **Cauchy kernel** is the fundamental solution of the gradient:

$$
\tilde{G}(\tilde{X}) = \frac{\bar{\tilde{X}}}{\|\tilde{X}\|_E^4}, \qquad \tilde{X} \neq 0.
$$

It satisfies $\tilde{\nabla}\tilde{G} = 2\pi^2 \delta_0 e_0$ in the sense of distributions, where $\delta_0$ is the Dirac delta at the origin.

In the oscillatory regime, $\tilde{G}(\theta \hat{n}) = -\theta \hat{n} / \theta^4 = -\hat{n}/\theta^3$, which is the quaternion analogue of the Cauchy kernel $1/z$ in complex analysis.

In the nilpotent regime, $\tilde{G}(\mathbf{Q}) = -\mathbf{Q}/\|\mathbf{Q}\|_E^4$, which is singular at the origin.

### The Poisson Kernel

The **Poisson kernel** for the ball of radius $r$ is

$$
P(\tilde{X}, \tilde{Y}) = \frac{r^2 - \|\tilde{X}\|_E^2}{2\pi^2 r \|\tilde{X} - \tilde{Y}\|_E^4}, \qquad \|\tilde{X}\|_E < r, \quad \|\tilde{Y}\|_E = r.
$$

It is the kernel that solves the Dirichlet problem for the d'Alembertian on the ball. It is the biquaternion analogue of the Poisson kernel in complex analysis.

### The Green's Function

The **Green's function** for the d'Alembertian on a domain $\Omega$ is the function $G(\tilde{X}, \tilde{Y})$ that satisfies

$$
\Box_{\tilde{X}} G(\tilde{X}, \tilde{Y}) = \delta(\tilde{X} - \tilde{Y}) e_0, \qquad G(\tilde{X}, \tilde{Y}) = 0 \text{ for } \tilde{X} \in \partial \Omega.
$$

Its construction is standard from the fundamental solution of the d'Alembertian, and it is the biquaternion analogue of the Green's function in the theory of elliptic partial differential equations.

### The Open Questions

1. **Explicit forms.** What are the explicit forms of the Poisson kernel and the Green's function in the oscillatory and nilpotent regimes?

2. **The relation to Clifford analysis.** How do these kernels relate to the corresponding kernels in Clifford analysis?

3. **The Hardy spaces.** What are the biquaternion analogues of the Hardy spaces $H^p$ and the Bergman spaces?

4. **The reproducing kernel.** Is there a reproducing kernel for the space of functions satisfying $\tilde{\nabla}\tilde{F} = 0$ on a domain?

These questions are open.

## The General Principle

The higher special functions of a biquaternion variable fall into two classes.

**Power-series functions.** These are defined by a power series in $\tilde{Q}$, and the series can be summed in closed form in the two pure regimes (pure oscillatory and pure nilpotent). The Bessel functions, the orthogonal polynomials, and the hypergeometric function belong to this class. The general case (with both $Q_0 \neq 0$ and $\mathbf{Q} \neq 0$) does not reduce to a closed form in terms of the elementary functions, because the powers of $\tilde{Q}$ involve the non-commutative product $Q_0 \mathbf{Q}$.

**Integral-defined functions.** These are defined by an integral over a real or complex parameter, and the extension to biquaternions requires a notion of the integrand for biquaternion arguments. The gamma function and the zeta function belong to this class. The convergence and analyticity of the integral are not automatic, and the theory is largely open.

**Functions from the analysis.** These arise as kernels and fundamental solutions of the differential operators of the analysis. The Cauchy kernel, the Poisson kernel, and the Green's function belong to this class. Their construction is standard, but their explicit forms and their properties are open in the general biquaternion case.

The common thread is the **complex norm** $\theta$: the two regimes $\theta \neq 0$ and $\theta = 0$ determine the behavior of the powers of $\tilde{Q}$, and hence the behavior of every special function defined by a power series. The integral-defined functions depend on $\theta$ in a more complicated way, and their theory is less developed.

## Open Questions

1. **The general case for power-series functions.** How do the Bessel functions, the orthogonal polynomials, and the hypergeometric function behave for a general biquaternion with both $Q_0 \neq 0$ and $\mathbf{Q} \neq 0$?

2. **The gamma function.** Can the integral defining $\Gamma(\tilde{Q})$ be made to converge for a general biquaternion, and does the functional equation hold?

3. **The zeta function.** Can the biquaternion zeta function be defined, and what are its properties? Is there an analogue of the Riemann hypothesis?

4. **The special functions from the analysis.** What are the explicit forms of the Poisson kernel, the Green's function, and the reproducing kernel for the spaces of functions satisfying $\tilde{\nabla}\tilde{F} = 0$ or $\Box\tilde{F} = 0$?

5. **The relation to Clifford analysis.** How do the biquaternion special functions relate to the corresponding functions in Clifford analysis?

6. **The extension to several variables.** Can the special functions be extended to functions of several biquaternion variables, and what replaces the two-regime structure?

7. **The polar representations.** How do the higher special functions interact with the Hamilton and complex polar forms?

## Summary

The higher special functions of a biquaternion variable fall into three classes.

**Power-series functions.** The Bessel functions, the orthogonal polynomials, and the hypergeometric function are defined by power series, and the series can be summed in closed form in the two pure regimes. In the pure oscillatory regime, the functions reduce to the ordinary functions evaluated at the complex norm $\theta$, with a parity factor depending on the power of the axis $\hat{n}$. In the pure nilpotent regime, the series truncate to polynomials in $\mathbf{Q}$ of degree at most one. The general case is open.

**Integral-defined functions.** The gamma function and the zeta function are defined by integrals or series that require a notion of the biquaternion power for real arguments. The convergence and analyticity are established only in special cases, and the functional equations are open.

**Functions from the analysis.** The Cauchy kernel, the Poisson kernel, and the Green's function are the kernels and fundamental solutions of the differential operators of the analysis. Their construction is standard, but their explicit forms and properties in the general biquaternion case are open.

The common thread is the complex norm $\theta$: the two regimes $\theta \neq 0$ and $\theta = 0$ determine the behavior of the powers of $\tilde{Q}$, and hence the behavior of every special function defined by a power series. The integral-defined functions depend on $\theta$ in a more complicated way, and their theory is less developed.

The biquaternion special functions are therefore a partially developed subject: the power-series functions in the two pure regimes are well understood, while the general case and the integral-defined functions are open problems.

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original formulation.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), Chapter 3, for the special functions of biquaternions.
- S. J. Sangwine, T. A. Ell, and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636, for the polar forms and the representation theory.
- S. J. Sangwine, "Biquaternion (complexified quaternion) roots of $-1$", *Advances in Applied Clifford Algebras* **16** (2006) 63–68, for the roots of $-1$.
- S. J. Sangwine and D. Alfsmann, "Determination of the biquaternion divisors of zero, including the idempotents and nilpotents", *Advances in Applied Clifford Algebras* **20** (2010) 401–416, for the zero divisors and nilpotents.
- R. Fueter, "Die Funktionentheorie der Differentialgleichungen $\Delta u = 0$ und $\Delta\Delta u = 0$ mit vier reellen Variablen", *Commentarii Mathematici Helvetici* **7** (1934–35) 307–330, for the analysis of quaternion-valued functions of four real variables.
- F. Brackx, R. Delanghe, and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the general Clifford analysis.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.

