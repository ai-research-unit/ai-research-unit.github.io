# __Split-Biquaternion Higher Special Functions__

## Introduction

This article introduces the higher special functions of a split biquaternion variable. It follows the article on split biquaternion elementary functions, which defined the exponential, the trigonometric and hyperbolic functions, the logarithm, and the power functions, and it uses the article on split biquaternion integration, which defined the integral and the Cauchy integral formula.

The goal is to define the Bessel functions, the orthogonal polynomials, the hypergeometric function, the gamma function, and the zeta function, and to establish their basic properties. The article is honest about what is fully understood and what is still open.

The treatment is purely mathematical. No physics is invoked. No examples are given. The split biquaternion algebra $\mathbb{H}_{\mathbb{D}}$ is assumed from the basic algebra article, together with its conjugations, its four fixed-point subspaces, and its idempotent decomposition. The elementary functions are assumed from the preceding article.

The key structural fact is the **idempotent decomposition**: the split biquaternion algebra is the direct sum of two copies of the quaternion algebra, and the idempotents $e_\pm$ commute with everything. So every function defined by a power series in the split biquaternion variable, with coefficients that are split complex scalars, reduces to the corresponding function of two ordinary quaternions, one for each idempotent component. This is the fundamental simplification relative to the biquaternion case.

For functions defined by integrals, the situation is different. The integral definitions require convergence conditions and a notion of the integrand for split biquaternion arguments. The gamma function and the zeta function are in this class, and their theory is only partially developed.

Throughout, a split biquaternion is written

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3, \qquad Q_\mu = q_\mu + j q'_\mu, \quad q_\mu, q'_\mu \in \mathbb{R}.
$$

The split complex unit is $j$, with $j^2 = +1$, and it commutes with the quaternion units. The quaternion conjugate is $\bar{\tilde{Q}} = Q_0 e_0 - \mathbf{Q}$. The norm form is $N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}}$.

The **idempotent components** of $\tilde{Q}$ are the real quaternions

$$
\tilde{Q}_+ = \sum_{\mu=0}^{3} (q_\mu + q'_\mu) e_\mu, \qquad \tilde{Q}_- = \sum_{\mu=0}^{3} (q_\mu - q'_\mu) e_\mu.
$$

## Bessel Functions

### Definition

The **Bessel function of the first kind** of order $\nu$ is defined by the power series

$$
J_\nu(\tilde{Q}) = \sum_{m=0}^{\infty} \frac{(-1)^m}{m! \, \Gamma(m + \nu + 1)} \left(\frac{\tilde{Q}}{2}\right)^{2m+\nu}.
$$

For integer order the series converges for every $\tilde{Q} \in \mathbb{H}_{\mathbb{D}}$, its terms decaying like $\|\tilde{Q}\|_E^{2m}/(4^m (m+n)!)$ up to a bounded factor. For non-integer $\nu$ the individual powers are defined through the power function $\exp((2m+\nu)\log \tilde{Q})$, which requires $\tilde{Q}$ to lie in the domain of the logarithm, so the series converges absolutely whenever the powers are defined: in the idempotent decomposition this means that both components $\tilde{Q}_\pm$ are nonzero, i.e. that $\tilde{Q}$ is not a zero divisor. The order is taken in $\mathbb{R}$ (or, more generally, $\nu \in \mathbb{D}$), since $\mathbb{D}$ contains no square root of $-1$ and hence no copy of $\mathbb{C}$.

### Computation via the Idempotent Decomposition

Because the idempotent decomposition separates the algebra into two commuting copies of $\mathbb{H}$, the Bessel function decomposes:

$$
J_\nu(\tilde{Q}) = J_{\nu_+}(\tilde{Q}_+) e_+ + J_{\nu_-}(\tilde{Q}_-) e_-,
$$

where $\nu = \nu_+ e_+ + \nu_- e_-$ and $J_{\nu_\pm}(\tilde{Q}_\pm)$ is the ordinary quaternion Bessel function of the component $\tilde{Q}_\pm$ with the order $\nu_\pm$ belonging to that component. The quaternion Bessel function is defined by the same power series, with $\tilde{Q}_\pm$ in place of $\tilde{Q}$, and it can be computed in closed form in the two regimes (pure oscillatory and pure nilpotent), as discussed in the biquaternion higher special functions article.

The split complex order $\nu \in \mathbb{D}$ is decomposed in the idempotent basis as $\nu = \nu_+ e_+ + \nu_- e_-$ with $\nu_\pm \in \mathbb{R}$ (or, more generally, $\nu_\pm \in \mathbb{H}$), and the Bessel function of the component is taken with the corresponding order.

So the split biquaternion Bessel function is the pair of the quaternion Bessel functions of the two idempotent components. This is the cleanest form of the function, and it is the reason the split biquaternion Bessel function is simpler than the biquaternion Bessel function.

### The Pure Oscillatory Regime

For a component $\tilde{Q}_\pm = \theta_\pm \hat{n}_\pm$ with $\theta_\pm \neq 0$ and $\hat{n}_\pm^2 = -e_0$, the quaternion Bessel function is

$$
J_n(\theta_\pm \hat{n}_\pm) = I_n(\theta_\pm) \, \hat{n}_\pm^n = \begin{cases} (-1)^{n/2} I_n(\theta_\pm) \, e_0 & \text{if } n \text{ is even}, \\ (-1)^{(n-1)/2} I_n(\theta_\pm) \, \hat{n}_\pm & \text{if } n \text{ is odd}, \end{cases}
$$

where $I_n(\theta_\pm)$ on the right is the ordinary complex **modified** Bessel function evaluated at the real (or complex) number $\theta_\pm$. The two signs $(-1)^m$ in the defining series cancel, which is why the modified function appears in place of $J_n$.

### The Pure Nilpotent Regime

For a component $\tilde{Q}_\pm = \mathbf{Q}_\pm$ with $\mathbf{Q}_\pm^2 = 0$, the quaternion Bessel function truncates:

$$
J_n(\mathbf{Q}_\pm) = \begin{cases} \frac{1}{n!} \left(\frac{\mathbf{Q}_\pm}{2}\right)^n & \text{if } n = 0 \text{ or } n = 1, \\ 0 & \text{if } n \geq 2. \end{cases}
$$

For non-integer $\nu$, the series reduces to the terms with $2m + \nu < 2$.

### Modified Bessel Functions

The **modified Bessel function** of the first kind is defined by

$$
I_\nu(\tilde{Q}) = \sum_{m=0}^{\infty} \frac{1}{m! \, \Gamma(m + \nu + 1)} \left(\frac{\tilde{Q}}{2}\right)^{2m+\nu}.
$$

The same analysis applies: the function decomposes in the idempotent basis, and each component reduces to the ordinary quaternion modified Bessel function.

## Orthogonal Polynomials

### Legendre Polynomials

The **Legendre polynomials** $P_n(\tilde{Q})$ are defined by the generating function

$$
\frac{1}{\sqrt{1 - 2\tilde{Q} t + t^2}} = \sum_{n=0}^{\infty} P_n(\tilde{Q}) t^n, \qquad |t| < R(\tilde{Q}),
$$

where $t$ is a real parameter, the square root is the split biquaternion square root (defined via the elementary functions), and the radius $R(\tilde{Q})$ is the distance from the origin to the nearest value of $t$ at which $1 - 2\tilde{Q}t + t^2$ fails to be invertible. For $|\tilde{Q}| \le 1$ one has $R(\tilde{Q}) = 1$, but not in general: for $\tilde{Q} = 3e_0$ the quadratic vanishes at $t = 3 \pm 2\sqrt{2}$, so the series converges only for $|t| < 3 - 2\sqrt{2} \approx 0.172$. Equivalently, they satisfy the recurrence

$$
(n+1) P_{n+1}(\tilde{Q}) = (2n+1) \tilde{Q} P_n(\tilde{Q}) - n P_{n-1}(\tilde{Q}),
$$

with $P_0 = e_0$ and $P_1 = \tilde{Q}$.

The Legendre polynomials are polynomials in $\tilde{Q}$ with real coefficients, and they decompose in the idempotent basis:

$$
P_n(\tilde{Q}) = P_n(\tilde{Q}_+) e_+ + P_n(\tilde{Q}_-) e_-,
$$

where $P_n(\tilde{Q}_\pm)$ is the ordinary quaternion Legendre polynomial of the component. In the pure oscillatory regime the quaternion Legendre polynomial does **not** reduce to the ordinary Legendre polynomial at the same argument: for a component $\tilde{Q}_\pm = \theta\hat{n}$ with $\hat{n}^2 = -e_0$ one has $P_n(\theta\hat{n}) = P_n(i\theta)$ with $i$ replaced by $\hat{n}$, since the generator $\hat{n}$ plays the role of the imaginary unit. For instance $P_2(\theta\hat{n}) = -(3\theta^2+1)/2$, whereas the ordinary $P_2$ gives $(3\theta^2-1)/2$: only the even part of $P_n$ survives on $e_0$ and only the odd part on $\hat{n}$. The analogous statement is discussed in the biquaternion higher special functions article.

### Chebyshev Polynomials

The **Chebyshev polynomials of the first kind** $T_n(\tilde{Q})$ are defined by the recurrence

$$
T_{n+1}(\tilde{Q}) = 2\tilde{Q} T_n(\tilde{Q}) - T_{n-1}(\tilde{Q}),
$$

with $T_0 = e_0$ and $T_1 = \tilde{Q}$. The same analysis applies: the polynomials decompose in the idempotent basis, and each component reduces to the ordinary quaternion Chebyshev polynomial.

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

The orthogonal polynomials are defined by three-term recurrences involving only the multiplication and addition of split biquaternions. So they are defined for every $\tilde{Q} \in \mathbb{H}_{\mathbb{D}}$, and they decompose in the idempotent basis:

$$
P_n(\tilde{Q}) = P_n(\tilde{Q}_+) e_+ + P_n(\tilde{Q}_-) e_-,
$$

where $P_n(\tilde{Q}_\pm)$ is the ordinary quaternion polynomial of the component. In the pure oscillatory regime the quaternion polynomial is obtained from the ordinary polynomial by replacing $i$ with $\hat{n}$ (as for the Legendre polynomials above), not by evaluating the ordinary polynomial at the same argument.

The general case (with both scalar and vector parts nonzero, and with a general split complex norm) reduces to the quaternion case in each idempotent component, which is the standard theory of quaternion orthogonal polynomials.

## Hypergeometric Function

### Definition

The **Gauss hypergeometric function** is defined by the power series

$$
{}_2F_1(a, b; c; \tilde{Q}) = \sum_{n=0}^{\infty} \frac{(a)_n (b)_n}{(c)_n} \frac{\tilde{Q}^n}{n!},
$$

where $(a)_n = a(a+1) \cdots (a+n-1)$ is the Pochhammer symbol, and $a, b, c \in \mathbb{D}$. The series converges for $\|\tilde{Q}\|_E < 1$.

### Computation via the Idempotent Decomposition

The hypergeometric function decomposes in the idempotent basis:

$$
{}_2F_1(a, b; c; \tilde{Q}) = {}_2F_1(a_+, b_+; c_+; \tilde{Q}_+) e_+ + {}_2F_1(a_-, b_-; c_-; \tilde{Q}_-) e_-,
$$

where $a_\pm, b_\pm, c_\pm$ are the idempotent components of the parameters, and ${}_2F_1(a_\pm, b_\pm; c_\pm; \tilde{Q}_\pm)$ is the ordinary quaternion hypergeometric function of the component.

In the pure oscillatory regime the quaternion hypergeometric function does **not** reduce to the ordinary complex hypergeometric function: for a component $\tilde{Q}_\pm = \theta\hat{n}$ with $\hat{n}^2 = -e_0$ one has

$$
{}_2F_1(a, b; c; \theta\hat{n}) = \Big[\sum_k \frac{(a)_{2k}(b)_{2k}}{(c)_{2k}} \frac{(-1)^k \theta^{2k}}{(2k)!}\Big] e_0 + \Big[\sum_k \frac{(a)_{2k+1}(b)_{2k+1}}{(c)_{2k+1}} \frac{(-1)^k \theta^{2k+1}}{(2k+1)!}\Big] \hat{n},
$$

the Pochhammer symbols sitting at $2k$ and $2k+1$ rather than at $k$, which is the even/odd decomposition stated for the biquaternion case.

### The Generalized Hypergeometric Function

The **generalized hypergeometric function** ${}_pF_q$ is defined by

$$
{}_pF_q(a_1, \dots, a_p; b_1, \dots, b_q; \tilde{Q}) = \sum_{n=0}^{\infty} \frac{(a_1)_n \cdots (a_p)_n}{(b_1)_n \cdots (b_q)_n} \frac{\tilde{Q}^n}{n!}.
$$

The same analysis applies: the function decomposes in the idempotent basis, and each component reduces to the ordinary quaternion generalized hypergeometric function.

## The Gamma Function

### The Definition Problem

The **gamma function** of a split biquaternion variable could be defined by the integral

$$
\Gamma(\tilde{Q}) = \int_0^\infty t^{\tilde{Q}-1} e^{-t} \, dt,
$$

where $t$ is a positive real number, $t^{\tilde{Q}-1} = \exp((\tilde{Q}-1) \log t)$ is the split biquaternion power, and $e^{-t}$ is the ordinary real exponential.

### The Obstruction

The integral is defined component-wise, but the integrand is a split-biquaternion-valued function of the real variable $t$, and the convergence of the integral depends on the growth of $t^{\tilde{Q}-1}$ as $t \to 0$ and as $t \to \infty$.

In the idempotent basis, the power decomposes:

$$
t^{\tilde{Q}-1} = t^{\tilde{Q}_+ - 1} e_+ + t^{\tilde{Q}_- - 1} e_-,
$$

where $t^{\tilde{Q}_\pm - 1}$ is the ordinary quaternion power of the component. The quaternion power involves the quaternion logarithm, which is multivalued, and the convergence of the integral depends on the behavior of each component.

**As $t \to 0$.** The quaternion power $t^{\tilde{Q}_\pm - 1}$ involves $\log t$, which tends to $-\infty$. In the pure oscillatory regime, the power oscillates, and the integral may not converge. In the pure nilpotent regime, the power converges if the real part of the scalar part of $\tilde{Q}_\pm$ is positive.

**As $t \to \infty$.** The factor $e^{-t}$ dominates, so the integral converges for all $\tilde{Q}$ with finite scalar part.

So the integral converges in the pure nilpotent regime if the real part of the scalar part is positive, and its convergence in the oscillatory regime is an open problem.

### What Is Known

The gamma function is well-defined in the pure nilpotent regime for suitable values of the scalar part, and it decomposes in the idempotent basis:

$$
\Gamma(\tilde{Q}) = \Gamma(\tilde{Q}_+) e_+ + \Gamma(\tilde{Q}_-) e_-,
$$

where $\Gamma(\tilde{Q}_\pm)$ is the quaternion gamma function of the component. The quaternion gamma function is defined by the same integral, and its convergence and analyticity are the same as for the split biquaternion case.

The functional equation $\Gamma(\tilde{Q}+1) = \tilde{Q} \Gamma(\tilde{Q})$ holds in each idempotent component if the quaternion functional equation holds. The reflection formula and the analytic continuation are open problems.

### The Open Questions

1. **Convergence.** For which split biquaternions $\tilde{Q}$ does the integral converge?

2. **Functional equation.** Does the functional equation hold in each component, and hence for the split biquaternion?

3. **Analytic continuation.** Can the gamma function be continued beyond the region of convergence of the integral?

4. **The reflection formula.** Does the reflection formula hold in each component?

## The Zeta Function

### The Definition Problem

The **Riemann zeta function** of a split biquaternion variable could be defined by the Dirichlet series

$$
\zeta(\tilde{Q}) = \sum_{n=1}^{\infty} \frac{1}{n^{\tilde{Q}}},
$$

where $n^{\tilde{Q}} = \exp(\tilde{Q} \log n)$ is the split biquaternion power.

### The Obstruction

The series is a series of split biquaternions. The convergence depends on the behavior of $n^{\tilde{Q}}$ as $n \to \infty$. In the idempotent basis, the series decomposes:

$$
\zeta(\tilde{Q}) = \zeta(\tilde{Q}_+) e_+ + \zeta(\tilde{Q}_-) e_-,
$$

where $\zeta(\tilde{Q}_\pm)$ is the quaternion zeta function of the component. The convergence of the quaternion zeta function depends on the quaternion power, which involves the quaternion logarithm, and the theory is largely open.

In the pure oscillatory regime, $n^{\tilde{Q}_\pm}$ oscillates, and the series may converge conditionally or may not converge at all. In the pure nilpotent regime, $n^{\tilde{Q}_\pm}$ converges absolutely if the real part of the scalar part is greater than 1.

### What Is Known

Almost nothing is known about the split biquaternion zeta function. The following are open problems.

### The Open Questions

1. **Convergence.** For which split biquaternions $\tilde{Q}$ does the series converge?

2. **The Euler product.** For positive integer bases the power function is multiplicative: $m^{\tilde{Q}} n^{\tilde{Q}} = \exp(\tilde{Q}\log m)\exp(\tilde{Q}\log n) = (mn)^{\tilde{Q}}$, because the two exponents commute as multiples of $\tilde{Q}$. Hence the Euler product $\prod_p (1 - p^{-\tilde{Q}})^{-1} = \sum_n n^{-\tilde{Q}}$ holds in the region of absolute convergence, and no separate obstruction arises; what remains open is the analytic continuation of the individual factors $p^{-\tilde{Q}}$.

3. **Analytic continuation.** Can the zeta function be continued beyond the region of convergence?

4. **Special values.** Are there split biquaternion analogues of the special values $\zeta(2) = \pi^2/6$, $\zeta(4) = \pi^4/90$, etc.?

5. **The functional equation.** Is there a split biquaternion analogue of the functional equation relating $\zeta(\tilde{Q})$ to $\zeta(e_0 - \tilde{Q})$?

6. **The Riemann hypothesis.** Is there an analogue of the Riemann hypothesis?

## Special Functions from the Analysis

### The Setting

The analysis article defined the split biquaternion gradient $\tilde{\nabla}$, the d'Alembertian $\Box$, and the convective derivative $\tilde{D}$ on a four-dimensional subspace $V \subset \mathbb{H}_{\mathbb{D}}$. The solutions of the equations

$$
\tilde{\nabla}\tilde{F} = 0, \qquad \Box\tilde{F} = 0
$$

are the split biquaternion analogues of holomorphic functions and harmonic functions. The special functions of the analysis are the kernels and fundamental solutions associated with these equations.

### The Cauchy Kernel

The **Cauchy kernel** is the fundamental solution of the gradient:

$$
\tilde{G}(\tilde{X}) = \frac{\bar{\tilde{X}}}{\|\tilde{X}\|_E^4}, \qquad \tilde{X} \neq 0.
$$

It satisfies $\tilde{\nabla}\tilde{G} = 2\pi^2 \delta_0 e_0$ in the sense of distributions. In the idempotent basis, it decomposes:

$$
\tilde{G}(\tilde{X}) = \tilde{G}(\tilde{X}_+) e_+ + \tilde{G}(\tilde{X}_-) e_-,
$$

where $\tilde{G}(\tilde{X}_\pm)$ is the quaternion Cauchy kernel of the component.

### The Poisson Kernel

The **Poisson kernel** for the ball of radius $r$ is

$$
P(\tilde{X}, \tilde{Y}) = \frac{r^2 - \|\tilde{X}\|_E^2}{2\pi^2 r \|\tilde{X} - \tilde{Y}\|_E^4}, \qquad \|\tilde{X}\|_E < r, \quad \|\tilde{Y}\|_E = r.
$$

It solves the Dirichlet problem for the d'Alembertian on the ball, and it decomposes in the idempotent basis into the quaternion Poisson kernels of the two components.

### The Green's Function

The **Green's function** for the d'Alembertian on a domain $\Omega$ satisfies

$$
\Box_{\tilde{X}} G(\tilde{X}, \tilde{Y}) = \delta(\tilde{X} - \tilde{Y}) e_0, \qquad G(\tilde{X}, \tilde{Y}) = 0 \text{ for } \tilde{X} \in \partial \Omega.
$$

Its construction is standard from the fundamental solution, and it decomposes in the idempotent basis.

### The Open Questions

1. **Explicit forms.** What are the explicit forms of the Poisson kernel and the Green's function in the two regimes?

2. **The relation to Clifford analysis.** How do these kernels relate to the corresponding kernels in Clifford analysis with split signature?

3. **The Hardy spaces.** What are the split biquaternion analogues of the Hardy spaces $H^p$ and the Bergman spaces?

4. **The reproducing kernel.** Is there a reproducing kernel for the space of functions satisfying $\tilde{\nabla}\tilde{F} = 0$ on a domain?

## The General Principle

The higher special functions of a split biquaternion variable fall into two classes.

**Power-series functions.** These are defined by a power series in $\tilde{Q}$, and the series decomposes in the idempotent basis into two copies of the corresponding quaternion function. The Bessel functions, the orthogonal polynomials, and the hypergeometric function belong to this class. The quaternion functions, in turn, reduce in the pure oscillatory regime to the corresponding ordinary complex functions evaluated with $i$ replaced by the generator $\hat{n}$ of the component (for the Bessel function this is the modified function $I_n$, for the orthogonal polynomials and the hypergeometric function the argument $i\theta$).

**Integral-defined functions.** These are defined by an integral over a real or complex parameter, and the extension to split biquaternions requires a notion of the integrand for split biquaternion arguments. The gamma function and the zeta function belong to this class. The convergence and analyticity of the integral are not automatic, and the theory is largely open.

**Functions from the analysis.** These arise as kernels and fundamental solutions of the differential operators of the analysis. The Cauchy kernel, the Poisson kernel, and the Green's function belong to this class. Their construction is standard, and they decompose in the idempotent basis.

The common thread is the **idempotent decomposition**: the split biquaternion algebra is the direct sum of two copies of the quaternion algebra, and every power-series function of a split biquaternion reduces to the corresponding function of two ordinary quaternions. The integral-defined functions are more complicated, because the integral must be defined and convergent in each component.

## Open Questions

1. **The general case for power-series functions.** How do the Bessel functions, the orthogonal polynomials, and the hypergeometric function behave in the general case, with both scalar and vector parts nonzero and with a general split complex norm?

2. **The gamma function.** Can the integral defining $\Gamma(\tilde{Q})$ be made to converge for a general split biquaternion, and does the functional equation hold?

3. **The zeta function.** Can the split biquaternion zeta function be defined, and what are its properties? Is there an analogue of the Riemann hypothesis?

4. **The special functions from the analysis.** What are the explicit forms of the Poisson kernel, the Green's function, and the reproducing kernel for the spaces of functions satisfying $\tilde{\nabla}\tilde{F} = 0$ or $\Box\tilde{F} = 0$?

5. **The relation to Clifford analysis.** How do the split biquaternion special functions relate to the corresponding functions in Clifford analysis with split signature?

6. **The extension to several variables.** Can the special functions be extended to functions of several split biquaternion variables, and what replaces the idempotent decomposition?

7. **The relation to the split complex case.** How do the split biquaternion special functions relate to the split complex special functions?

## Summary

The higher special functions of a split biquaternion variable fall into three classes.

**Power-series functions.** The Bessel functions, the orthogonal polynomials, and the hypergeometric function are defined by power series, and the series decompose in the idempotent basis into two copies of the corresponding quaternion function. In the pure oscillatory regime the quaternion functions are the ordinary complex functions with $i$ replaced by the generator $\hat{n}$ of the component, as in the Bessel, Legendre and hypergeometric cases above. This is the cleanest and most fully developed part of the theory.

**Integral-defined functions.** The gamma function and the zeta function are defined by integrals or series that require a notion of the split biquaternion power for real arguments. The convergence and analyticity are established only in special cases, and the functional equations are open.

**Functions from the analysis.** The Cauchy kernel, the Poisson kernel, and the Green's function are the kernels and fundamental solutions of the differential operators of the analysis. They decompose in the idempotent basis, and their construction is standard.

The common thread is the idempotent decomposition: the split biquaternion algebra is the direct sum of two copies of the quaternion algebra, and every power-series function reduces to the corresponding function of two ordinary quaternions. The integral-defined functions are more complicated, because the integral must be defined and convergent in each component.

The split biquaternion special functions are therefore a partially developed subject: the power-series functions are well understood via the idempotent decomposition, while the integral-defined functions are open problems. The theory is simpler than the biquaternion case, because the idempotent decomposition reduces everything to two copies of the quaternion case, and the quaternion case is itself well understood.

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original formulation of quaternions and their complexification.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), Chapter 3, for the special functions of split biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the classification of real algebras.
- F. Brackx, R. Delanghe, and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the general Clifford analysis.
- R. Fueter, "Die Funktionentheorie der Differentialgleichungen $\Delta u = 0$ und $\Delta\Delta u = 0$ mit vier reellen Variablen", *Commentarii Mathematici Helvetici* **7** (1934–35) 307–330, for the analysis of quaternion-valued functions of four real variables.

