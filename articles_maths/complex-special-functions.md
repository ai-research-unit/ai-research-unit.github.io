
# __Complex Special Functions__

## Introduction

This article introduces the complex special functions as a collection of named functions that arise repeatedly in complex analysis and differential equations. The goal is to define each function precisely, establish its basic properties, and describe the relations among them.

The treatment is mathematically honest: every claim is either proved or stated as a definition. Complex analysis is assumed: holomorphic functions, contour integrals, the Cauchy integral formula, Laurent series, and residues are used throughout. The order of presentation follows the dependency order: the complex exponential and its consequences first, then functions defined from them, then functions defined by series and integrals.

## The Complex Exponential and Logarithm

### The Complex Exponential

The **complex exponential** is defined for $Q \in \mathbb{C}$ by

$$
\exp(Q) = \sum_{n=0}^\infty \frac{Q^n}{n!}.
$$

The series converges absolutely for every $Q$. The function is entire, and it satisfies

$$
\exp(Q_1 + Q_2) = \exp(Q_1) \exp(Q_2), \qquad \exp(0) = 1, \qquad \exp'(Q) = \exp(Q).
$$

For $Q = q + i q'$ with $q, q' \in \mathbb{R}$,

$$
\exp(Q) = \exp(q) (\cos q' + i \sin q').
$$

This is **Euler's formula**, and it is the bridge between the exponential and the trigonometric functions. In particular, for $q' = \theta$,

$$
\exp(i\theta) = \cos\theta + i \sin\theta.
$$

The exponential is $2\pi i$-periodic: $\exp(Q + 2\pi i) = \exp(Q)$.

The modulus used below is the Hermitian norm of the layer, the bracket carrying the bar: $\langle Q\rangle_{*} = \langle Q,Q\rangle_{*} = Q\bar Q = q^2+q'^2$.

### The Complex Logarithm

A **logarithm** of $Q \in \mathbb{C}^\times$ is a complex number $Q_{\log}$ with $\exp(Q_{\log}) = Q$. The definition is an equation, not a formula; the formula is what solving the equation gives.

The element and its logarithm carry two different pairs of real coordinates, and they must not be mixed:

$$
Q = q+iq', \qquad Q_{\log} = q_{\log}+i q'_{\log}, \qquad
q_{\log}=\operatorname{Re}Q_{\log}, \quad q'_{\log}=\operatorname{Im}Q_{\log}, \quad Q\neq0.
$$

The subscript is a label, not an operation: $q_{\log}$ is the real coordinate of $Q_{\log}$, not the logarithm of $q$. Euler's formula turns $\exp(Q_{\log}) = Q$ into the pair of real equations

$$
\exp(q_{\log})\cos q'_{\log} = q, \qquad \exp(q_{\log})\sin q'_{\log} = q'.
$$

Taking moduli in $\exp(Q_{\log})=Q$ gives $\exp(q_{\log})=\sqrt{\langle Q\rangle_{*}}$, and squaring gives

$$
\exp(2q_{\log}) = \langle Q\rangle_{*}, \qquad \text{so} \qquad q_{\log}=\tfrac12\ln\langle Q\rangle_{*}.
$$

Dividing by $\exp(q_{\log})$ gives

$$
\exp(iq'_{\log}) = \frac{Q}{\sqrt{\langle Q\rangle_{*}}} = \frac{q}{\sqrt{\langle Q\rangle_{*}}}+i\frac{q'}{\sqrt{\langle Q\rangle_{*}}},
$$

so $q'_{\log}$ is an argument of $Q$. The two coordinates of the logarithm are therefore

| coordinate | real formula |
|---|---|
| $q_{\log}=$ | $\tfrac12\ln(q^2+q'^2)$ |
| $q'_{\log}=$ | $\arctan\dfrac{q'}{q}$ if $q>0$<br>$\arctan\dfrac{q'}{q}+\pi\operatorname{sgn}q'$ if $q<0$<br>$\operatorname{sgn}(q')\dfrac{\pi}{2}$ if $q=0$ |

The logarithm is

$$
Q_{\log} = \ln\sqrt{\langle Q\rangle_{*}} + i\arg Q = \ln\sqrt{\langle Q\rangle_{*}} + i(\operatorname{Arg} Q + 2\pi k), \qquad k \in \mathbb{Z}.
$$

The first coordinate is unique. The second is one number for each choice of $k$, and the values differ by $2\pi$. Hence every $Q\neq0$ has a logarithm, and no logarithm is unique.

**Example.** Take $Q=3+4i$. Then $\sqrt{\langle Q\rangle_{*}}=\sqrt{9+16}=5$, so $q_{\log}=\ln 5=1.6094379$. The angle equations read $\cos q'_{\log}=3/5$ and $\sin q'_{\log}=4/5$, so

$$
q'_{\log}=\arg(3+4i)=\arctan\frac{4}{3}=0.9272952\ \text{rad}.
$$

The logarithm is the number $Q_{\log}=1.6094379+0.9272952\,i$. Exponentiating it back gives $5(\cos 0.9272952+i\sin 0.9272952)=3.0000000+4.0000000\,i$, which is $Q$ up to rounding. The choice $q'_{\log}=0.9272952+2\pi k$ gives the same $Q$ for every integer $k$.

### The Two Compositions

The word "inverse" covers two different identities, and the exponential and the logarithm satisfy them in opposite strengths.

**Right inverse.** For every $Q \neq 0$ and every logarithm $Q_{\log}$ of $Q$,

$$
\exp(Q_{\log}) = Q.
$$

**Proof.** Put $q_{\log} = \ln\sqrt{\langle Q\rangle_{*}}$ and $q'_{\log} = \arg Q$, so $Q_{\log} = q_{\log}+iq'_{\log}$. Then

$$
\exp(Q_{\log}) = \exp(q_{\log})\bigl(\cos q'_{\log}+i\sin q'_{\log}\bigr) = \sqrt{\langle Q\rangle_{*}}\left(\frac{q}{\sqrt{\langle Q\rangle_{*}}}+i\frac{q'}{\sqrt{\langle Q\rangle_{*}}}\right) = q+iq' = Q,
$$

by the two equations solved above. No branch is preferred: every choice of $\arg Q$ gives the same $Q$, because $\exp$ is $2\pi i$-periodic.

**Left inverse, up to the kernel.** For every $Q \neq 0$ and every logarithm $Q_{\log}$ of $Q$,

$$
\log(\exp(Q_{\log})) = Q_{\log} + 2\pi i k, \qquad k \in \mathbb{Z},
$$

where the integer depends on the branch of $\log$. With the principal branch, writing $Q_{\log} = \ln r + i\theta$ with $r=\sqrt{\langle Q\rangle_{*}}>0$,

$$
\operatorname{Log}(\exp(Q_{\log})) = \ln r + i\operatorname{Arg}(\exp(Q_{\log})), \qquad \operatorname{Arg}(\exp(Q_{\log})) \equiv \theta \pmod{2\pi}.
$$

**Proof.** Since $\exp(Q_{\log}) = Q$, both $\log(\exp(Q_{\log}))$ and $Q_{\log}$ are logarithms of $Q$. If $Q_{\log}+h$ is another logarithm of $Q$, then $\exp h = 1$, so $h \in 2\pi i\mathbb{Z}$. The principal value is the representative whose imaginary part lies in $(-\pi,\pi]$. Every complex number is a logarithm of its exponential, so the statement covers every possible argument of $\exp$.

The asymmetry is the content of the word "multivalued". The exponential forgets the imaginary part modulo $2\pi$; the logarithm cannot recover what was forgotten. Thus $\exp$ is surjective but not injective, while $\log$ is a right inverse of $\exp$ and only a left inverse modulo $2\pi i$. In group language, $\exp$ is a surjective homomorphism from $(\mathbb{C},+)$ to $(\mathbb{C}^\times,\cdot)$ with kernel $2\pi i\mathbb{Z}$, and a branch of $\log$ picks one representative in each coset $Q_{\log}+2\pi i\mathbb{Z}$. The table records the two identities with a numerical instance of each.

| identity | holds? | example |
|---|---|---|
| $\exp(Q_{\log}) = Q$ | always, for $Q \neq 0$ | $Q = 3+4i$, $Q_{\log} = 1.6094379 + 0.9272952\,i$ |
| $\log(\exp(Q_{\log})) = Q_{\log}$ | only modulo $2\pi i$ | $Q_{\log} = 1+4i$, $\operatorname{Log}(\exp(Q_{\log})) = 1 - 2.2831853\,i$ |

### The Principal Logarithm

Single-valuedness is bought by restricting the target of the exponential. Define the **principal strip**

$$
S = \{\ln r + i\theta : r > 0,\ -\pi < \theta \leq \pi\}.
$$

On $S$ the exponential is injective. If $\exp W_1 = \exp W_2$ with $W_1, W_2 \in S$, then $W_1 - W_2 \in 2\pi i\mathbb{Z}$; the imaginary part of $W_1 - W_2$ lies in $(-2\pi, 2\pi)$, and the only multiple of $2\pi$ in that interval is $0$. Therefore $W_1 = W_2$.

The exponential maps $S$ onto $\mathbb{C}^\times$: for $Q \neq 0$, the number $\ln\sqrt{\langle Q\rangle_{*}} + i\operatorname{Arg} Q$ lies in $S$ and exponentiates to $Q$. The restriction is therefore a bijection, and its inverse is the **principal logarithm**

$$
\operatorname{Log} Q = \ln\sqrt{\langle Q\rangle_{*}} + i \operatorname{Arg} Q, \qquad -\pi < \operatorname{Arg} Q \leq \pi.
$$

By construction, $\exp(\operatorname{Log} Q) = Q$ for every $Q \neq 0$, and $\operatorname{Log}(\exp(Q_{\log})) = Q_{\log}$ exactly when $Q_{\log} \in S$.

The inverse is discontinuous on the negative real axis. For $Q = -1$, the formula gives $\operatorname{Log}(-1) = i\pi$, the upper endpoint of the strip. Approaching $-1$ from the upper half-plane gives $\operatorname{Arg} Q \to \pi$ and $\operatorname{Log} Q \to i\pi$; approaching from the lower half-plane gives $\operatorname{Arg} Q \to -\pi$ and $\operatorname{Log} Q \to -i\pi$. The two limits differ by $2\pi i$, so the principal branch cannot be continued continuously across the negative real axis. That ray is the **branch cut**. It is an artefact of the strip, not of the exponential, and any ray from $0$ to $\infty$ can replace it. On the cut itself the principal value is still defined, and $\exp(\operatorname{Log} Q) = Q$ still holds; it is continuity, not the inverse identity, that fails.

### The Derivative of the Logarithm

The inverse is holomorphic, and its derivative is forced by the identity it satisfies.

**Inverse function theorem.** The exponential is holomorphic and $\exp'(Q_{\log}) = \exp(Q_{\log}) \neq 0$ at every point. Hence $\exp$ is locally biholomorphic, and on a neighbourhood of $Q = \exp(Q_{\log})$ the local inverse has derivative

$$
(\exp^{-1})'(Q) = \frac{1}{\exp'(Q_{\log})} = \frac{1}{\exp(Q_{\log})} = \frac{1}{Q}.
$$

The principal logarithm is that local inverse, so $\operatorname{Log}' Q = 1/Q$ on $\mathbb{C} \setminus (-\infty, 0]$.

**Chain rule check.** Differentiating $\exp(\operatorname{Log} Q) = Q$ gives

$$
\exp(\operatorname{Log} Q)\operatorname{Log}' Q = 1,
$$

hence $\operatorname{Log}' Q = 1/Q$. The same computation applies to any branch of $\log$, and it shows that all branches have the same derivative.

**Cartesian check.** Write $\operatorname{Log} Q = \ln r + i\theta$ with $Q = q+iq'$ and $r^2 = q^2+q'^2$. Off the cut and away from the imaginary axis, with the quadrant correction of $\operatorname{Arg}$,

$$
\ln r = \tfrac12\ln(q^2+q'^2), \qquad \theta = \arctan\frac{q'}{q},
$$

and therefore

$$
\frac{\partial \ln r}{\partial q} = \frac{q}{r^2}, \quad \frac{\partial \ln r}{\partial q'} = \frac{q'}{r^2}, \qquad \frac{\partial \theta}{\partial q} = -\frac{q'}{r^2}, \quad \frac{\partial \theta}{\partial q'} = \frac{q}{r^2}.
$$

The Cauchy–Riemann equations hold, $\partial_q \ln r = \partial_{q'}\theta$ and $\partial_{q'}\ln r = -\partial_q\theta$, and the derivative is

$$
\frac{\partial \ln r}{\partial q} + i\frac{\partial \theta}{\partial q} = \frac{q - iq'}{q^2+q'^2} = \frac{1}{q+iq'} = \frac{1}{Q}.
$$

The three computations agree: $\operatorname{Log}$ is holomorphic exactly where $\operatorname{Arg}$ is differentiable, that is, off the branch cut, and its derivative is $1/Q$.

### Complex Powers

For $a \in \mathbb{C}$ and $Q \neq 0$,

$$
Q^a = \exp(a \log Q).
$$

Because $\log Q = \operatorname{Log} Q + 2\pi i k$, the values are

$$
Q^a = \exp(a \operatorname{Log} Q)\exp(2\pi i k a), \qquad k \in \mathbb{Z}.
$$

The factor $\exp(2\pi i k a)$ equals $1$ for every $k$ exactly when $a \in \mathbb{Z}$. If $a = p/q$ is rational in lowest terms, it takes $q$ distinct values; otherwise the set of values is infinite. The principal branch is obtained by using the principal branch of the logarithm.

## The Trigonometric and Hyperbolic Functions

### Trigonometric Functions

The **complex sine** and **cosine** are defined by

$$
\sin Q = \frac{\exp(iQ) - \exp(-iQ)}{2i}, \qquad \cos Q = \frac{\exp(iQ) + \exp(-iQ)}{2}.
$$

Both are entire. They satisfy

$$
\sin' Q = \cos Q, \qquad \cos' Q = -\sin Q,
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

They are $2\pi$-periodic, and their zeros are real: $\sin Q = 0$ iff $Q = n\pi$, $\cos Q = 0$ iff $Q = \pi/2 + n\pi$.

**Unboundedness.** Unlike the real case, $\sin$ and $\cos$ are unbounded on $\mathbb{C}$. For $Q = i q'$ with $q' \in \mathbb{R}$,

$$
\sin(i q') = i \sinh q', \qquad \cos(i q') = \cosh q'.
$$

### Hyperbolic Functions

The **complex hyperbolic sine** and **cosine** are defined by

$$
\sinh Q = \frac{\exp(Q) - \exp(-Q)}{2}, \qquad \cosh Q = \frac{\exp(Q) + \exp(-Q)}{2}.
$$

Both are entire, and they satisfy

$$
\sinh' Q = \cosh Q, \qquad \cosh' Q = \sinh Q,
$$

$$
\cosh^2 Q - \sinh^2 Q = 1.
$$

The relation between the trigonometric and hyperbolic functions is

$$
\sin(iQ) = i \sinh Q, \qquad \cos(iQ) = \cosh Q,
$$

$$
\sinh(iQ) = i \sin Q, \qquad \cosh(iQ) = \cos Q.
$$

### Other Trigonometric and Hyperbolic Functions

$$
\tan Q = \frac{\sin Q}{\cos Q}, \qquad \cot Q = \frac{\cos Q}{\sin Q},
$$

$$
\tanh Q = \frac{\sinh Q}{\cosh Q}, \qquad \coth Q = \frac{\cosh Q}{\sinh Q}.
$$

These are meromorphic, with poles where the denominator vanishes.

### Inverse Trigonometric Functions

The **complex arcsine** is defined by

$$
\arcsin Q = -i \log\left( iQ + \sqrt{1 - Q^2} \right),
$$

where the square root and logarithm are multivalued. The **complex arctangent** is

$$
\arctan Q = \frac{1}{2i} \log \frac{1 + iQ}{1 - iQ}.
$$

Both are multivalued, and both have branch cuts determined by the branch choices of the square root and logarithm.

## The Gamma Function

### Definition

The **gamma function** is defined for $\operatorname{Re} Q > 0$ by

$$
\Gamma(Q) = \int_0^\infty t^{Q-1} \exp(-t) \, dt.
$$

The integral converges absolutely for $\operatorname{Re} Q > 0$ and defines a holomorphic function on that half-plane.

### Analytic Continuation

The functional equation

$$
\Gamma(Q + 1) = Q \Gamma(Q)
$$

extends $\Gamma$ meromorphically to all of $\mathbb{C}$, with simple poles at $Q = 0, -1, -2, \dots$ and residues

$$
\operatorname{Res}(\Gamma, -n) = \frac{(-1)^n}{n!}.
$$

The extended function has no zeros. It satisfies $\Gamma(n + 1) = n!$ for non-negative integers $n$.

### The Weierstrass Product

$$
\frac{1}{\Gamma(Q)} = Q \exp(\gamma Q) \prod_{n=1}^\infty \left( 1 + \frac{Q}{n} \right) \exp(-Q/n),
$$

where $\gamma$ is the Euler–Mascheroni constant. This product converges uniformly on compact subsets of $\mathbb{C}$ and shows that $1/\Gamma$ is entire with zeros at $Q = 0, -1, -2, \dots$.

### Reflection and Duplication

$$
\Gamma(Q) \Gamma(1 - Q) = \frac{\pi}{\sin(\pi Q)},
$$

$$
\Gamma(Q) \Gamma\left(Q + \tfrac{1}{2}\right) = 2^{1-2Q} \sqrt{\pi} \, \Gamma(2Q).
$$

The reflection formula shows that $\Gamma$ has no zeros, since $1/\Gamma$ is entire and the right side has no zeros.

### The Beta Function

The **beta function** is defined for $\operatorname{Re} a > 0$, $\operatorname{Re} b > 0$ by

$$
B(a, b) = \int_0^1 t^{a-1} (1 - t)^{b-1} \, dt.
$$

It satisfies

$$
B(a, b) = \frac{\Gamma(a) \Gamma(b)}{\Gamma(a + b)}.
$$

**Proof.** Substitute $t = u/(1+u)$ in the beta integral, then use the gamma integral representation for each factor.

It is symmetric: $B(a, b) = B(b, a)$.

### Stirling's Formula

As $\sqrt{\langle Q\rangle_{*}} \to \infty$ with $|\arg Q| < \pi$,

$$
\Gamma(Q) \sim \sqrt{2\pi} \, Q^{Q - 1/2} \exp(-Q).
$$

This is the asymptotic expansion of the gamma function, and it is the source of most estimates involving factorials and binomial coefficients.

## The Riemann Zeta Function

### Definition

The **Riemann zeta function** is defined for $\operatorname{Re} s > 1$ by

$$
\zeta(s) = \sum_{n=1}^\infty \frac{1}{n^s}.
$$

The series converges absolutely for $\operatorname{Re} s > 1$ and defines a holomorphic function on that half-plane.

### Analytic Continuation

The zeta function extends meromorphically to all of $\mathbb{C}$, with a single simple pole at $s = 1$ with residue $1$. The continuation is given by the functional equation

$$
\zeta(s) = 2^s \pi^{s-1} \sin\left(\frac{\pi s}{2}\right) \Gamma(1 - s) \zeta(1 - s),
$$

which relates $\zeta(s)$ to $\zeta(1-s)$.

### The Euler Product

For $\operatorname{Re} s > 1$,

$$
\zeta(s) = \prod_p \frac{1}{1 - p^{-s}},
$$

where the product is over all primes $p$. This is the analytic form of the fundamental theorem of arithmetic, and it is the starting point of analytic number theory.

### Special Values

$$
\zeta(2) = \frac{\pi^2}{6}, \qquad \zeta(4) = \frac{\pi^4}{90}, \qquad \zeta(2n) = \frac{(-1)^{n+1} B_{2n} (2\pi)^{2n}}{2 (2n)!},
$$

where $B_{2n}$ are the Bernoulli numbers. The values at negative integers are

$$
\zeta(-n) = (-1)^n \frac{B_{n+1}}{n+1}, \qquad n \geq 0.
$$

In particular, $\zeta(0) = -1/2$ and $\zeta(-1) = -1/12$.

### The Riemann Hypothesis

The **Riemann hypothesis** states that all non-trivial zeros of $\zeta$ lie on the critical line $\operatorname{Re} s = 1/2$. It is the most famous open problem in mathematics, and it is equivalent to a sharp estimate on the error term in the prime number theorem.

## The Incomplete Gamma and Beta Functions

### The Incomplete Gamma Function

The **lower incomplete gamma function** is

$$
\gamma(s, Q) = \int_0^Q t^{s-1} \exp(-t) \, dt, \qquad \operatorname{Re} s > 0.
$$

The **upper incomplete gamma function** is

$$
\Gamma(s, Q) = \int_Q^\infty t^{s-1} \exp(-t) \, dt, \qquad \operatorname{Re} s > 0,
$$

where the integral is along a ray from $Q$ to infinity avoiding the negative real axis. They satisfy

$$
\gamma(s, Q) + \Gamma(s, Q) = \Gamma(s).
$$

Both extend meromorphically in $s$ and are entire in $Q$.

### The Regularized Incomplete Gamma Functions

$$
P(s, Q) = \frac{\gamma(s, Q)}{\Gamma(s)}, \qquad 1 - P(s, Q) = \frac{\Gamma(s, Q)}{\Gamma(s)}.
$$

### The Incomplete Beta Function

$$
B(Q; a, b) = \int_0^Q t^{a-1} (1 - t)^{b-1} \, dt, \qquad \operatorname{Re} a > 0, \; \operatorname{Re} b > 0,
$$

where the integral is along a path from $0$ to $Q$ avoiding the branch points $0$ and $1$. The **regularized incomplete beta function** is

$$
I_Q(a, b) = \frac{B(Q; a, b)}{B(a, b)}.
$$

It satisfies $I_0(a, b) = 0$ and $I_1(a, b) = 1$, and it extends meromorphically in $a$ and $b$.

## The Error Function

### Definition

The **error function** is defined by

$$
\operatorname{erf}(Q) = \frac{2}{\sqrt{\pi}} \int_0^Q \exp(-t^2) \, dt.
$$

The integral is along any path from $0$ to $Q$. The integrand is entire, so $\operatorname{erf}$ is entire. It is odd, and it satisfies

$$
\operatorname{erf}'(Q) = \frac{2}{\sqrt{\pi}} \exp(-Q^2).
$$

### The Complementary Error Function

$$
\operatorname{erfc}(Q) = 1 - \operatorname{erf}(Q) = \frac{2}{\sqrt{\pi}} \int_Q^\infty \exp(-t^2) \, dt.
$$

The integral is along a ray from $Q$ to infinity avoiding the essential singularity at infinity.

### Asymptotics

As $\sqrt{\langle Q\rangle_{*}} \to \infty$ with $|\arg Q| < 3\pi/4$,

$$
\operatorname{erfc}(Q) \sim \frac{\exp(-Q^2)}{\sqrt{\pi} Q}.
$$

This asymptotic expansion is used in the theory of the heat equation and in probability.

## The Orthogonal Polynomials

### Legendre Polynomials

The **Legendre polynomials** $P_n(Q)$ are defined by the generating function

$$
\frac{1}{\sqrt{1 - 2Qt + t^2}} = \sum_{n=0}^\infty P_n(Q) t^n, \qquad |t| < 1,
$$

where the square root is the principal branch. They satisfy the recurrence

$$
(n+1) P_{n+1}(Q) = (2n+1) Q P_n(Q) - n P_{n-1}(Q),
$$

with $P_0 = 1$ and $P_1 = Q$. They satisfy Legendre's differential equation

$$
(1 - Q^2) w'' - 2Q w' + n(n+1) w = 0.
$$

They are orthogonal on $[-1, 1]$ with respect to the weight $1$:

$$
\int_{-1}^1 P_m(a) P_n(a) \, da = \frac{2}{2n+1} \delta_{mn}.
$$

### Chebyshev Polynomials

The **Chebyshev polynomials of the first kind** $T_n(Q)$ are defined by

$$
T_n(Q) = \cos(n \arccos Q),
$$

where the arccos is the principal branch. They satisfy the recurrence

$$
T_{n+1}(Q) = 2Q T_n(Q) - T_{n-1}(Q),
$$

with $T_0 = 1$ and $T_1 = Q$. They are orthogonal on $[-1, 1]$ with respect to the weight $(1 - a^2)^{-1/2}$:

$$
\int_{-1}^1 \frac{T_m(a) T_n(a)}{\sqrt{1 - a^2}} \, da = \begin{cases} \pi & m = n = 0, \\ \pi/2 & m = n \geq 1, \\ 0 & m \neq n. \end{cases}
$$

### Hermite Polynomials

The **Hermite polynomials** $H_n(Q)$ are defined by

$$
H_n(Q) = (-1)^n \exp(Q^2) \frac{d^n}{dQ^n} \exp(-Q^2).
$$

They satisfy the recurrence

$$
H_{n+1}(Q) = 2Q H_n(Q) - 2n H_{n-1}(Q),
$$

with $H_0 = 1$ and $H_1 = 2Q$. They are orthogonal on $\mathbb{R}$ with respect to the weight $\exp(-a^2)$:

$$
\int_{-\infty}^\infty H_m(a) H_n(a) \exp(-a^2) \, da = 2^n n! \sqrt{\pi} \, \delta_{mn}.
$$

### Laguerre Polynomials

The **Laguerre polynomials** $L_n(Q)$ are defined by

$$
L_n(Q) = \frac{\exp(Q)}{n!} \frac{d^n}{dQ^n} (Q^n \exp(-Q)).
$$

They satisfy the recurrence

$$
(n+1) L_{n+1}(Q) = (2n+1-Q) L_n(Q) - n L_{n-1}(Q),
$$

with $L_0 = 1$ and $L_1 = 1 - Q$. They are orthogonal on $[0, \infty)$ with respect to the weight $\exp(-a)$:

$$
\int_0^\infty L_m(a) L_n(a) \exp(-a) \, da = \delta_{mn}.
$$

## The Bessel Functions

### Definition

The **Bessel function of the first kind** of order $\nu$ is

$$
J_\nu(Q) = \sum_{n=0}^\infty \frac{(-1)^n}{n! \, \Gamma(n + \nu + 1)} \left( \frac{Q}{2} \right)^{2n + \nu}.
$$

The series converges absolutely for all $Q$, so $Q^{-\nu} J_\nu(Q)$ is entire. It satisfies Bessel's differential equation

$$
Q^2 w'' + Q w' + (Q^2 - \nu^2) w = 0.
$$

### The Bessel Function of the Second Kind

$$
Y_\nu(Q) = \frac{J_\nu(Q) \cos(\nu \pi) - J_{-\nu}(Q)}{\sin(\nu \pi)}, \qquad \nu \notin \mathbb{Z},
$$

with the limit taken for integer $\nu$. It is the second linearly independent solution of Bessel's equation. It has a branch point at $Q = 0$.

### Modified Bessel Functions

The **modified Bessel function of the first kind** is

$$
I_\nu(Q) = \sum_{n=0}^\infty \frac{1}{n! \, \Gamma(n + \nu + 1)} \left( \frac{Q}{2} \right)^{2n + \nu}.
$$

It satisfies

$$
Q^2 w'' + Q w' - (Q^2 + \nu^2) w = 0.
$$

### Integral Representations

For $\operatorname{Re} \nu > -1/2$,

$$
J_\nu(Q) = \frac{1}{\sqrt{\pi} \, \Gamma(\nu + 1/2)} \left( \frac{Q}{2} \right)^\nu \int_{-1}^1 (1 - t^2)^{\nu - 1/2} \exp(iQt) \, dt.
$$

This representation is the source of most asymptotic estimates.

### Asymptotics

As $\sqrt{\langle Q\rangle_{*}} \to \infty$ with $|\arg Q| < \pi$,

$$
J_\nu(Q) \sim \sqrt{\frac{2}{\pi Q}} \cos\left(Q - \frac{\nu \pi}{2} - \frac{\pi}{4}\right),
$$

$$
I_\nu(Q) \sim \frac{\exp(Q)}{\sqrt{2 \pi Q}}, \qquad |\arg Q| < \frac{\pi}{2}.
$$

## The Airy Functions

### Definition

The **Airy function** $\operatorname{Ai}(Q)$ is defined by the contour integral

$$
\operatorname{Ai}(Q) = \frac{1}{2\pi i} \int_C \exp\left(\frac{t^3}{3} - Qt\right) dt,
$$

where $C$ is a contour in the complex plane that starts at infinity along the ray $\arg t = -\pi/3$ and ends at infinity along the ray $\arg t = \pi/3$. The integral converges because of the cubic term.

It satisfies Airy's differential equation

$$
w'' - Q w = 0.
$$

The second solution $\operatorname{Bi}(Q)$ is defined by a similar contour integral with a different contour.

### Asymptotics

As $\sqrt{\langle Q\rangle_{*}} \to \infty$ with $|\arg Q| < \pi$,

$$
\operatorname{Ai}(Q) \sim \frac{1}{2 \sqrt{\pi} Q^{1/4}} \exp(-2 Q^{3/2}/3).
$$

As $\sqrt{\langle Q\rangle_{*}} \to \infty$ with $|\arg(-Q)| < 2\pi/3$,

$$
\operatorname{Ai}(Q) \sim \frac{1}{\sqrt{\pi} (-Q)^{1/4}} \sin\left(\frac{2 (-Q)^{3/2}}{3} + \frac{\pi}{4}\right).
$$

The Airy functions are the simplest example of functions with a Stokes phenomenon: the asymptotic expansion changes form across certain rays in the complex plane.

## The Hypergeometric Function

### Definition

The **Gauss hypergeometric function** is defined for $\sqrt{\langle Q\rangle_{*}} < 1$ by

$$
{}_2F_1(a, b; c; Q) = \sum_{n=0}^\infty \frac{(a)_n (b)_n}{(c)_n} \frac{Q^n}{n!},
$$

where $(a)_n = a(a+1) \cdots (a+n-1)$ is the Pochhammer symbol. The series converges for $\sqrt{\langle Q\rangle_{*}} < 1$ and extends analytically to $\mathbb{C} \setminus [1, \infty)$.

It satisfies the hypergeometric differential equation

$$
Q(1 - Q) w'' + [c - (a + b + 1) Q] w' - ab w = 0.
$$

### Integral Representation

For $\operatorname{Re} c > \operatorname{Re} b > 0$,

$$
{}_2F_1(a, b; c; Q) = \frac{\Gamma(c)}{\Gamma(b) \Gamma(c - b)} \int_0^1 t^{b-1} (1 - t)^{c-b-1} (1 - Qt)^{-a} \, dt.
$$

The integral is along a path from $0$ to $1$ avoiding the branch point at $t = 1/Q$.

### Special Cases

$$
{}_2F_1(1, 1; 2; Q) = -\frac{\log(1 - Q)}{Q},
$$

$$
{}_2F_1(a, b; b; Q) = (1 - Q)^{-a},
$$

$$
{}_2F_1\left(\frac{1}{2}, \frac{1}{2}; \frac{3}{2}; Q^2\right) = \frac{\arcsin Q}{Q}.
$$

### The Generalized Hypergeometric Function

$$
{}_pF_q(a_1, \dots, a_p; b_1, \dots, b_q; Q) = \sum_{n=0}^\infty \frac{(a_1)_n \cdots (a_p)_n}{(b_1)_n \cdots (b_q)_n} \frac{Q^n}{n!}.
$$

Most named special functions are special cases of ${}_pF_q$.

## The Elliptic Integrals and Elliptic Functions

### Complete Elliptic Integrals

The **complete elliptic integral of the first kind** is

$$
K(k) = \int_0^{\pi/2} \frac{d\theta}{\sqrt{1 - k^2 \sin^2 \theta}}, \qquad 0 \leq k < 1.
$$

The **complete elliptic integral of the second kind** is

$$
E(k) = \int_0^{\pi/2} \sqrt{1 - k^2 \sin^2 \theta} \, d\theta.
$$

Both extend analytically in $k$ to $\mathbb{C} \setminus \{\pm 1\}$.

### Relation to the Hypergeometric Function

$$
K(k) = \frac{\pi}{2} \, {}_2F_1\left(\frac{1}{2}, \frac{1}{2}; 1; k^2\right),
$$

$$
E(k) = \frac{\pi}{2} \, {}_2F_1\left(-\frac{1}{2}, \frac{1}{2}; 1; k^2\right).
$$

### Elliptic Functions

The **Weierstrass elliptic function** $\wp(Q)$ is defined by

$$
\wp(Q) = \frac{1}{Q^2} + \sum_{(m, n) \neq (0, 0)} \left( \frac{1}{(Q - m\omega_1 - n\omega_2)^2} - \frac{1}{(m\omega_1 + n\omega_2)^2} \right),
$$

where $\omega_1, \omega_2$ are the periods. It is meromorphic and doubly periodic, and it satisfies the differential equation

$$
\wp'(Q)^2 = 4 \wp(Q)^3 - g_2 \wp(Q) - g_3.
$$

Elliptic functions are the inverse functions of elliptic integrals, and they are the natural setting for the theory of doubly periodic meromorphic functions.

## The Lambert W Function

### Definition

The **Lambert W function** is the multivalued inverse of

$$
f(Q) = Q \exp(Q).
$$

That is, $W(Q)$ is any solution of

$$
W(Q) \exp(W(Q)) = Q.
$$

The function has infinitely many branches $W_k(Q)$ for $k \in \mathbb{Z}$, with branch points at $Q = 0$ and $Q = -1/e$.

### Derivative

$$
W'(Q) = \frac{W(Q)}{Q(1 + W(Q))}, \qquad Q \neq 0, \; Q \neq -1/e.
$$

### Applications

The Lambert W function solves equations of the form $a \exp(Q) + b Q + c = 0$. It appears in combinatorics (tree enumeration), in the analysis of delay differential equations, and in the inversion of the iterated exponential $c^c = a$, where $c = \exp(W(\ln a))$.

## Summary

The complex special functions are the named functions that recur in complex analysis and in differential equations. The exponential is defined by its series and is entire, and the trigonometric and hyperbolic functions are built from it; the logarithm is its multivalued inverse: $\exp(Q_{\log}) = Q$ for every $Q \neq 0$, while $\log(\exp(Q_{\log}))$ recovers $Q_{\log}$ only modulo $2\pi i$.

Integral representations supply the next family: the gamma function as $\Gamma(Q) = \int_0^\infty t^{Q-1}\exp(-t)\,dt$ for $\operatorname{Re} Q > 0$ together with its analytic continuation, the Riemann zeta function as the Dirichlet series that continues meromorphically, and the incomplete gamma and beta functions that refine them. The error function, the orthogonal polynomials and the Bessel functions carry the same pattern to integrals and to the solutions of the classical differential equations.

The article closes with the higher transcendental functions: the Airy functions as contour integrals, the Gauss hypergeometric function ${}_2F_1(a,b;c;Q)$ and its analytic continuation, the elliptic integrals and elliptic functions, and the Lambert $W$ function as the multivalued inverse of $Q \mapsto Q\exp(Q)$. Each is defined precisely, and its elementary properties, its differential equation and its relations to the others are recorded.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $Q = q + i q'$ | Complex variable |
| $\exp(Q), \log Q$ | Complex exponential, logarithm |
| $\operatorname{Log} Q$ | Principal branch of the complex logarithm |
| $Q_{\log} = q_{\log} + iq'_{\log}$ | A logarithm of $Q$, with $q_{\log} = \ln\sqrt{\langle Q\rangle_{*}}$ and $q'_{\log} = \arg Q$ |
| $\sin Q, \cos Q, \tan Q$ | Complex trigonometric functions |
| $\sinh Q, \cosh Q, \tanh Q$ | Complex hyperbolic functions |
| $\Gamma(Q)$ | Gamma function |
| $B(a, b)$ | Beta function |
| $\zeta(s)$ | Riemann zeta function |
| $\gamma(s, Q), \Gamma(s, Q)$ | Incomplete gamma functions |
| $B(Q; a, b), I_Q(a, b)$ | Incomplete beta functions |
| $\operatorname{erf}(Q), \operatorname{erfc}(Q)$ | Error function, complementary error function |
| $P_n, T_n, H_n, L_n$ | Legendre, Chebyshev, Hermite, Laguerre polynomials |
| $J_\nu, Y_\nu, I_\nu$ | Bessel functions |
| $\operatorname{Ai}, \operatorname{Bi}$ | Airy functions |
| ${}_pF_q$ | Generalized hypergeometric function |
| $K(k), E(k)$ | Complete elliptic integrals |
| $\wp(Q)$ | Weierstrass elliptic function |
| $W_k(Q)$ | Lambert W function, branch $k$ |

## Further Reading

- E. T. Whittaker and G. N. Watson, *A Course of Modern Analysis* (Cambridge, 1927), for the classical treatment.
- N. N. Lebedev, *Special Functions and Their Applications* (Dover, 1972), for a thorough treatment of the classical functions.
- G. E. Andrews, R. Askey, and R. Roy, *Special Functions* (Cambridge, 1999), for the modern unified approach.
- M. Abramowitz and I. A. Stegun, *Handbook of Mathematical Functions* (Dover, 1965), for tables and formulas.
- F. W. J. Olver, A. B. Olde Daalhuis, D. W. Lozier and others (eds.), *NIST Digital Library of Mathematical Functions* (National Institute of Standards and Technology, 2010–), for the modern reference.

