
# __Brownian Motion and Stochastic Calculus__

## Introduction

Brownian motion is the continuous-time random walk, and the stochastic calculus is the analysis of its functionals. The process is defined by three requirements — it starts at the origin, it has independent stationary increments, and its increments are Gaussian with variance equal to the elapsed time — and the requirement that its paths be continuous; from these, remarkably, follow the nowhere differentiability of the paths and the existence of a rich calculus in which the second-order variation of the process is the elapsed time. The calculus is the Itô calculus: the stochastic integral of an adapted integrand against the process, the change-of-variable formula known as Itô's formula, the change-of-measure theorem of Girsanov, and the stochastic differential equations built from them.

This article constructs Brownian motion, identifies it as a Markov process whose generator is half the Laplacian and whose transition semigroup is the heat semigroup, derives its basic martingales and the reflection principle, develops the Itô integral and the Itô formula, treats the stochastic differential equations with Lipschitz coefficients, states the Girsanov and Feynman–Kac theorems, and describes the probabilistic solution of the Dirichlet problem. The construction and the calculus are the two halves of the theory, and the applications — to the heat equation, to diffusions, to the potential theory of the Laplacian and to the invariance principle — are the reasons the subject is the meeting point of analysis and probability.

The place of the article is fixed by four boundaries.

- The **probability frame** is *Measure-Theoretic Probability* and *Independence and Conditional Expectation*, and the **martingale theory** — the maximal inequality, the convergence theorem, optional stopping and uniform integrability — is *Martingales*, used here without restatement. The **Markov chains and their generators** are *Markov Chains and Processes*, whose transition semigroups, generators and martingale problem are the discrete and the general framework that the Brownian motion instantiates.
- The **analysis of Euclidean space** — the Laplace operator, the heat equation, the Fourier transform, the Sobolev spaces, the harmonic functions and the Dirichlet problem — is the subject of the analysis articles of Part III, in particular *Fourier Analysis on Euclidean Spaces* and *Partial Differential Equations*: the heat kernel is the Fourier transform of the Gaussian, the fundamental solution of the heat equation is the Brownian transition density, and the potential-theoretic statements are proved by the analytic theory and quoted here. The **harmonic analysis** — the Fourier transform, the Schwartz space, the semigroups defined by multipliers — is that of *Fourier Analysis on Euclidean Spaces* and of *Harmonic Analysis on Groups*, and the **ergodic theory** of the shifts and the flows is.
- The **random walks on groups** and the **invariance principle for a random walk on a group** are; the **ergodic-theoretic aspects** of the Brownian flow are; and the **per-system analysis of a single number system** is Part V's. This article does not re-derive the Euclidean analysis it uses.

Throughout, $(\Omega,\mathcal{F},\{\mathcal{F}_t\}_{t\geq0},\mathbb{P})$ is a filtered probability space satisfying the usual conditions — the filtration is right-continuous and complete — and $B = \{B_t\}_{t\geq0}$ is a **standard Brownian motion** in $\mathbb{R}^d$: $B_0 = 0$ a.s., the increments $B_{t_1}-B_{t_0}, \dots, B_{t_n}-B_{t_{n-1}}$ over disjoint intervals are independent and centred Gaussian with covariances $(t_i - t_{i-1})I_d$, and $t\mapsto B_t$ is continuous a.s. The one-dimensional case is written $B_t$ without decoration, $\langle M\rangle_t$ denotes the predictable quadratic variation of a continuous local martingale, and $\Delta = \sum_{i=1}^d\partial_i^2$ is the Laplacian, with the convention that the Brownian generator is $\frac12\Delta$.

## The Construction of Brownian Motion

### The Kolmogorov Extension and Continuity

**Definition.** A standard Brownian motion in $\mathbb{R}^d$ is a stochastic process $\{B_t\}_{t\geq0}$ with $B_0 = 0$, continuous paths, independent increments, and

$$
B_t - B_s \sim N(0, (t-s)I_d) \qquad \text{for } 0 \leq s < t.
$$

**Theorem (existence).** Standard Brownian motion exists, and the law of the process is a probability measure $\mathbb{W}$ — the **Wiener measure** — on the space $C([0,\infty),\mathbb{R}^d)$ of continuous paths.

*Proof (sketch).* The Kolmogorov extension theorem of *Independence and Conditional Expectation* produces a process $\{X_t\}$ on the product space $\mathbb{R}^{[0,\infty)}$ with the prescribed finite-dimensional Gaussian distributions, since the family is consistent. The continuity of the paths is then obtained by the Kolmogorov continuity criterion: if $\mathbb{E}|X_t - X_s|^\alpha \leq C|t-s|^{1+\beta}$ for some $\alpha, \beta > 0$, then the process has a modification with Hölder-continuous paths of order $\gamma < \beta/\alpha$. For Brownian motion, $\mathbb{E}|B_t - B_s|^{2m} = C_m\,(t-s)^m$, so the criterion applies with $\alpha = 2m$ and $\beta = m-1$ for every $m$, and it gives a modification whose paths are locally Hölder of order $\gamma < (m-1)/(2m)$; letting $m\to\infty$ gives every $\gamma < 1/2$, and passing to the modification yields the continuous process, whose law is the Wiener measure on $C([0,\infty))$. $\square$

The construction is the standard one and it identifies the two normalisations: the quadratic variation of the increments, $\mathbb{E}|B_t-B_s|^2 = d(t-s)$, is the one that produces the $1/2$-Hölder continuity, and the higher moments supply the exponent. The proof also shows that the path space may be taken to be the compact-open $C([0,\infty),\mathbb{R}^d)$, on which the Wiener measure is a Borel probability measure.

**Theorem (regularity and irregularity of the paths).** Brownian paths are locally Hölder-continuous of every order $\gamma < 1/2$ and of no order $\gamma > 1/2$; the modulus of continuity at a point is

$$
\limsup_{h\to0}\frac{|B_{t+h}-B_t|}{\sqrt{2h\log(1/h)}} = 1 \qquad \text{a.s.}
$$

and the paths are nowhere differentiable, a.s.: for every $t$, $\limsup_{h\to0}|B_{t+h}-B_t|/h = \infty$.

*Proof (sketch).* The upper bound of the modulus is Borel–Cantelli applied to the dyadic increments; the lower bound is the independence of the increments, together with the second Borel–Cantelli lemma of *Independence and Conditional Expectation*, which shows that the dyadic oscillations are large infinitely often. Non-differentiability is immediate from the modulus and the scaling $B_{t+h}-B_t \sim \sqrt h\,N(0,1)$. $\square$

The theorem is the precise statement of the roughness of the Brownian path: the path is continuous but has no tangent anywhere, and the correct scaling is the square root of the time increment. This is what forces the stochastic calculus to be a second-order calculus, because the second-order term of the Taylor expansion of a smooth function along the path does not vanish in the limit.

### Quadratic Variation

**Definition.** For a partition $\Pi = \{0 = t_0 < t_1 < \dots < t_n = t\}$ of $[0,t]$ the **quadratic variation** of a process $X$ along $\Pi$ is $V_\Pi(X)_t = \sum_{i}(X_{t_{i+1}}-X_{t_i})^2$, and the process has finite quadratic variation if the sums converge in probability as the mesh of the partition tends to $0$.

**Theorem (quadratic variation of Brownian motion).** The quadratic variation of Brownian motion exists and equals the elapsed time:

$$
\sum_{i=1}^{n}(B_{t_{i+1}}-B_{t_i})^2 \longrightarrow t \qquad \text{in } L^2 \text{ and a.s. along refining sequences},
$$

as the mesh of the partition tends to $0$. In particular the total variation of the path is infinite a.s. on every interval.

*Proof.* The expectation of the sum is $t$ and the variance is $2\sum_i(t_{i+1}-t_i)^2 \leq 2\,t\,|\Pi|$, which tends to $0$; the $L^2$ convergence follows, and the almost-sure statement from a subsequence and a Borel–Cantelli argument. $\square$

The quadratic variation is the central object of the stochastic calculus: it is the reason the Itô formula has a second-order term, the reason the stochastic integral is not the Stieltjes integral along the path, and the quantity that characterises Brownian motion among the continuous martingales by Lévy's theorem below.

## The Heat Semigroup and the Generator

### The Transition Density

**Definition.** The **Brownian transition density** in $\mathbb{R}^d$ is the Gaussian kernel

$$
p_t(x,y) = (2\pi t)^{-d/2}\exp\!\left(-\frac{|x-y|^2}{2t}\right), \qquad t > 0,
$$

and the Brownian **transition semigroup** is $P_tf(x) = \mathbb{E}^x[f(B_t)] = \int_{\mathbb{R}^d}p_t(x,y)f(y)\,dy$, where $\mathbb{E}^x$ is the law of the motion started at $x$, so that $\{x + B_t\}$ under $\mathbb{P}$ has the law of $B$ under $\mathbb{P}^x$.

**Theorem (the semigroup property and the generator).** The kernels satisfy the Chapman–Kolmogorov relation $\int p_s(x,z)p_t(z,y)\,dz = p_{s+t}(x,y)$, so that $\{P_t\}$ is a semigroup, and

$$
P_t = e^{t\Delta/2} \qquad \text{on } L^2(\mathbb{R}^d),
$$

the semigroup generated by half the Laplacian; in particular the generator of Brownian motion is $L = \frac12\Delta$, and the transition density is the fundamental solution of the heat equation.

*Proof.* The Chapman–Kolmogorov identity is the addition formula for Gaussians, obtained by completing the square in the exponent. The spectral description follows from the Fourier transform: $\widehat{p_t}(\xi) = e^{-t|\xi|^2/2}$, by the computation of the Gaussian integral, so $P_t$ multiplies the Fourier transform by $e^{-t|\xi|^2/2}$; differentiating at $t=0$ gives multiplication by $-|\xi|^2/2$, which is the Fourier multiplier of $\frac12\Delta$. $\square$

The identification is the reason Brownian motion is the probabilistic model of the heat equation: the function $u(t,x) = P_tf(x) = \mathbb{E}^x[f(B_t)]$ solves

$$
\partial_tu = \frac{1}{2}\Delta u, \qquad u(0,\cdot) = f,
$$

and the transition density is the heat kernel. The Fourier computation is that of *Fourier Analysis on Euclidean Spaces*, and the same computation in the group setting — the heat kernel on a Lie group and its semigroup — is *Harmonic Analysis on Groups* and *Analysis on Compact Groups*.

### The Basic Martingales and Lévy's Characterisation

**Theorem (Brownian martingales).** Let $\mathbb{P}^x$ be the law started at $x$. The following are martingales with respect to the Brownian filtration: the coordinate processes $B_t^i$ under $\mathbb{P}^0$; the processes $B_t^iB_t^j - \delta_{ij}t$; the processes $|B_t|^2 - dt$; and, for $\sigma \in \mathbb{R}$, the exponential martingales

$$
\exp\!\left(\sigma \cdot B_t - \frac{\sigma^2t}{2}\right) = \exp\!\left(\sum_i\sigma_iB_t^i - \frac{|\sigma|^2t}{2}\right).
$$

*Proof.* The verification is the Markov property and the increment law: for the squares, $\mathbb{E}^x[B_{t+s}^iB_{t+s}^j - \delta_{ij}(t+s)\mid\mathcal{F}_t] = B_t^iB_t^j - \delta_{ij}t$ because the cross terms have zero mean and the increment contributes $\delta_{ij}s$; the exponential martingale is the characteristic function of the Gaussian increment, which multiplies by $e^{|\sigma|^2s/2}$. $\square$

**Theorem (Lévy's characterisation of Brownian motion).** Let $M$ be a continuous local martingale with $M_0 = 0$ and $\langle M\rangle_t = t$ for every $t$. Then $M$ is a standard Brownian motion.

Lévy's theorem characterises Brownian motion by its quadratic variation among the continuous local martingales, and it is the reason the quadratic variation is the fundamental invariant of the calculus. Its proof uses the exponential martingales of the theorem above and the uniqueness of the Fourier transform, and it is the tool by which processes known to be martingales with deterministic quadratic variation are identified as Brownian motions — the Brownian component of a filtered process, for instance.

## The Itô Integral

### The Definition and the Isometry

**Definition.** Let $\{H_t\}$ be a progressively measurable process with $\mathbb{E}\int_0^T H_s^2\,ds < \infty$. The **Itô integral** $\int_0^T H_s\,dB_s$ is defined first for simple predictable integrands $H = \sum_i \xi_i\mathbf{1}_{(t_i,t_{i+1}]}$, by

$$
\int_0^T H_s\,dB_s = \sum_i \xi_i\,(B_{t_{i+1}} - B_{t_i}),
$$

and extended to all integrands in $L^2(d\mathbb{P}\times dt)$ by continuity, using the **Itô isometry**

$$
\mathbb{E}\left[\left(\int_0^T H_s\,dB_s\right)^2\right] = \mathbb{E}\int_0^T H_s^2\,ds.
$$

The isometry is the statement that the stochastic integral is an isometry from $L^2(d\mathbb{P}\times dt)$ into $L^2(\mathbb{P})$, and it is the reason the integral exists for every square-integrable adapted integrand. The extension from simple integrands is by density, and the result is a continuous local martingale with $\langle\int H\,dB\rangle_t = \int_0^t H_s^2\,ds$; the independence of the increments and the predictability of $H$ are both used, and the integral is the limit of Riemann sums in which the integrand is evaluated at the left endpoint — the choice of endpoint is the difference between the Itô and the Stratonovich integrals.

### Itô's Formula

**Theorem (Itô's formula).** Let $f : \mathbb{R}\times\mathbb{R}\to\mathbb{R}$ be of class $C^{1,2}$ and let $X_t = X_0 + \int_0^t K_s\,ds + \int_0^t H_s\,dB_s$ be a continuous semimartingale. Then

$$
f(t, X_t) = f(0, X_0) + \int_0^t \partial_tf(s,X_s)\,ds + \int_0^t \partial_xf(s,X_s)\,dX_s + \frac{1}{2}\int_0^t \partial_x^2f(s,X_s)\,d\langle X\rangle_s,
$$

where the middle integral is the sum of a Lebesgue integral against $K$ and an Itô integral against $H$, and $\langle X\rangle_s = \int_0^s H_u^2\,du$ is the quadratic variation of the martingale part. For the Brownian motion itself, with $dX = dB$ and $d\langle X\rangle = dt$,

$$
f(B_t) = f(B_0) + \int_0^t f'(B_s)\,dB_s + \frac{1}{2}\int_0^t f''(B_s)\,ds.
$$

*Proof (sketch).* Expand $f$ to second order and sum over the increments of a partition:
$f(B_{t_{i+1}}) - f(B_{t_i}) = f'(B_{t_i})\Delta_i + \frac12f''(B_{t_i})\Delta_i^2 + o(\Delta_i^2)$, with $\Delta_i = B_{t_{i+1}}-B_{t_i}$. The first terms converge to the stochastic integral, and the second-order terms converge to the time integral because $\sum\Delta_i^2\to t$ in probability by the quadratic variation theorem; the cross terms vanish in the limit. $\square$

The formula is the chain rule of the stochastic calculus, and the additional term $\frac12f''\,dt$ is the whole difference from the classical calculus: it arises because the Brownian path has nonzero quadratic variation. It is the source of the solvable models of the theory — the Ornstein–Uhlenbeck process, geometric Brownian motion, the Bessel processes and the representation of harmonic functions — and it is the continuous form of the Itô formula for a discrete process, which differs from the classical chain rule by a quadratic term of the same origin.

**Definition.** The **Stratonovich integral** is $\int_0^t f(B_s)\circ dB_s = \int_0^t f(B_s)\,dB_s + \frac12\langle f(B),B\rangle_t = \int_0^tf(B_s)\,dB_s+\frac12\int_0^tf'(B_s)\,ds$; it is defined by the midpoint Riemann sums, and it obeys the classical chain rule $df(B_t) = f'(B_t)\circ dB_t$. The two integrals differ by half the quadratic covariation, and the Itô convention is the one that makes the integral a martingale.

### Integration by Parts and the Product Rule

**Theorem (product rule).** For continuous semimartingales $X$ and $Y$,

$$
d(X_tY_t) = X_t\,dY_t + Y_t\,dX_t + d\langle X,Y\rangle_t,
$$

where $\langle X,Y\rangle$ is the quadratic covariation; in particular for two Brownian motions with correlation $\rho$, $\langle B^1,B^2\rangle_t = \rho t$.

The product rule is the Itô formula for the multiplication map, and it differs from the classical Leibniz rule by the covariation term. Its discrete prototype is the summation-by-parts identity for sums of independent variables with an error term of the order of the variances, and it is the reason the quadratic variation is the bookkeeping device of the whole calculus.

## Stochastic Differential Equations

### Existence and Uniqueness

**Definition.** A **stochastic differential equation** with drift $b$ and diffusion $\sigma$ is

$$
dX_t = b(t, X_t)\,dt + \sigma(t,X_t)\,dB_t, \qquad X_0 = \xi,
$$

an integral equation $X_t = \xi + \int_0^t b(s,X_s)\,ds + \int_0^t\sigma(s,X_s)\,dB_s$. A **strong solution** is an adapted continuous process satisfying the equation pathwise for a given Brownian motion; a **weak solution** is a pair (process, Brownian motion) on a probability space satisfying the equation.

**Theorem (Itô).** Suppose $b$ and $\sigma$ are measurable and satisfy the Lipschitz and linear-growth conditions

$$
|b(t,x)-b(t,y)| + |\sigma(t,x)-\sigma(t,y)| \leq K|x-y|, \qquad |b(t,x)|^2 + |\sigma(t,x)|^2 \leq K^2(1+|x|^2),
$$

and let $\xi$ be a square-integrable initial condition independent of the Brownian motion. Then the equation has a unique strong solution, which is a continuous adapted process with $\mathbb{E}[\sup_{t\leq T}|X_t|^2] < \infty$ for every $T$.

*Proof (sketch).* Use the Picard iteration $X^{(0)} = \xi$, $X^{(n+1)}_t = \xi + \int_0^tb(s,X^{(n)}_s)ds + \int_0^t\sigma(s,X^{(n)}_s)dB_s$, and estimate the successive differences by the Itô isometry and the Lipschitz condition. The estimates are summable in $n$ after taking the sup over $t \leq T$ and using the Doob maximal inequality of *Martingales* and the Gronwall lemma, so the iteration converges uniformly on $[0,T]$ in $L^2$; the limit solves the equation. Uniqueness follows by applying the same estimate to the difference of two solutions. $\square$

### The Markov Property and Examples

**Theorem.** Under the hypotheses of the existence theorem the solution is a **Markov process** with transition kernel $\mathbb{P}(X_{t+s}\in B \mid X_t = x) = \mathbb{P}(X_s^{(x)}\in B)$, and it is a **strong Markov process**: the post-$\tau$ process is a fresh solution started at $X_\tau$ after a stopping time $\tau$. Its generator is the second-order operator

$$
L = b(x)\cdot\nabla + \frac{1}{2}\sum_{i,j}(\sigma\sigma^\top)_{ij}(x)\,\partial_i\partial_j,
$$

in the sense that $f(X_t) - f(X_0) - \int_0^tLf(X_s)\,ds$ is a local martingale, which is the martingale problem of *Markov Chains and Processes* for the diffusion $X$.

**Example (geometric Brownian motion).** The equation $dX_t = \mu X_t\,dt + \sigma X_t\,dB_t$ has the solution

$$
X_t = X_0\exp\!\left(\left(\mu - \frac{\sigma^2}{2}\right)t + \sigma B_t\right),
$$

obtained by applying Itô's formula to $\log X_t$; the exponential is the **stochastic exponential** of the process $(\mu-\sigma^2/2)t + \sigma B_t$, and the drift correction $- \sigma^2/2$ is the Itô correction. The process is the standard model of a multiplicative growth process with noise, and the martingale $e^{\sigma B_t - \sigma^2t/2}$ of the previous section is the case $\mu = 0$ after normalisation.

**Example (the Ornstein–Uhlenbeck process).** The equation $dX_t = -\theta X_t\,dt + \sigma\,dB_t$ with $\theta > 0$ has the stationary Gaussian solution

$$
X_t = e^{-\theta t}X_0 + \sigma\int_0^t e^{-\theta(t-s)}\,dB_s,
$$

with $\operatorname{Var}(X_t) = \frac{\sigma^2}{2\theta}(1 - e^{-2\theta t})$, and the stationary distribution $N(0,\sigma^2/2\theta)$. The process is the continuous-time analogue of an autoregressive sequence, it is reversible with respect to the stationary law, and its spectral decomposition is the model of the spectral theory of the Markov chains of *Markov Chains and Processes*.

**Example (Bessel processes).** For a $d$-dimensional Brownian motion the radial process $R_t = |B_t|$ satisfies

$$
dR_t = \frac{d-1}{2R_t}\,dt + dB_t^{\mathrm{Bessel}}, \qquad R_0 = |B_0|,
$$

where $B^{\mathrm{Bessel}}$ is a one-dimensional Brownian motion; the drift $(d-1)/(2R_t)$ is the **Bessel drift** and the equation is a stochastic differential equation with a non-Lipschitz coefficient at the origin, whose boundary behaviour is governed by the Feller test. The comparison of the Bessel dimension with the divergence of the integral $\int R_t^{-1}\,dt$ is the continuous form of Pólya's recurrence theorem of *Markov Chains and Processes*.

## Girsanov, Feynman–Kac and the Dirichlet Problem

### The Girsanov Theorem

**Theorem (Girsanov).** Let $\theta = \{\theta_t\}$ be an adapted process with $\int_0^T\theta_s^2\,ds < \infty$ a.s. and suppose the exponential martingale

$$
Z_t = \exp\!\left(-\int_0^t\theta_s\,dB_s - \frac{1}{2}\int_0^t\theta_s^2\,ds\right)
$$

is a uniformly integrable martingale (which holds, by Novikov's condition, when $\mathbb{E}\exp(\frac12\int_0^T\theta_s^2ds) < \infty$). Then $Z_T$ defines a probability measure $\mathbb{Q} = Z_T\mathbb{P}$ on $\mathcal{F}_T$ and, under $\mathbb{Q}$, the process

$$
\tilde B_t = B_t + \int_0^t\theta_s\,ds
$$

is a standard Brownian motion on $[0,T]$.

Girsanov's theorem is the change of measure that removes a drift from a diffusion, and it is the reason the stochastic calculus can be transferred between processes with different drifts: under the new measure the process $\tilde B$ has the law of a Brownian motion, and a stochastic differential equation with drift becomes an equation without drift. The theorem is the continuous form of the likelihood ratio process of *Martingales*, and it is the basis of the martingale method of mathematical finance and of the weak solutions of the stochastic differential equations — by Girsanov, an equation with a bounded measurable drift has a weak solution obtained by translating a Brownian motion.

### The Feynman–Kac Formula

**Theorem (Feynman–Kac).** Let $V : \mathbb{R}^d\to\mathbb{R}$ be bounded and continuous from below, let $f$ be bounded and continuous, and define

$$
u(t,x) = \mathbb{E}^x\!\left[\exp\!\left(-\int_0^tV(B_s)\,ds\right)f(B_t)\right].
$$

Then $u$ is of class $C^{1,2}$ on $(0,\infty)\times\mathbb{R}^d$, and it solves the parabolic equation

$$
\partial_tu = \frac{1}{2}\Delta u - Vu, \qquad u(0,\cdot) = f.
$$

The Feynman–Kac formula is the representation of the solution of the heat equation with a potential as an expectation, and it is the reason the semigroup $e^{t(\Delta/2 - V)}$, which is not a Markov semigroup when $V$ changes sign, is still accessible by probabilistic methods. The proof is the Itô formula applied to the process $e^{-\int_0^tV(B_s)ds}u(t-s,B_s)$ and the martingale property together with the boundedness that permits taking expectations.

### The Dirichlet Problem

**Theorem (Kakutani's formula).** Let $D \subseteq \mathbb{R}^d$ be a bounded domain with smooth (or merely regular) boundary, let $\tau_D = \inf\{t : B_t \notin D\}$, and let $\varphi$ be continuous on $\partial D$. Then the function

$$
u(x) = \mathbb{E}^x\bigl[\varphi(B_{\tau_D})\bigr], \qquad x \in D,
$$

is the unique continuous solution of the Dirichlet problem $\Delta u = 0$ in $D$, $u = \varphi$ on $\partial D$; the boundary values are taken because $\mathbb{P}^x(\tau_D < \infty) = 1$ and $\lim_{x\to y}u(x) = \varphi(y)$ for regular boundary points $y$.

Kakutani's formula is the probabilistic solution of the Dirichlet problem, and it identifies Brownian motion as the tool of classical potential theory: the harmonic measure of the domain is the law of $B_{\tau_D}$, the value of the harmonic function is the average of the boundary data against it, and the boundaries are regular exactly when the motion leaves the domain continuously. The smoothness of the boundary is not needed: the Wiener criterion characterises the regular points in terms of the capacity of the complement, and it is the potential-theoretic statement of the strong Markov property.

**Theorem (exit and occupation).** The moment generating function of the exit time is characterised by $\mathbb{E}^x[e^{-\lambda\tau_D}]$, the solution of $\frac12\Delta v = \lambda v$ in $D$ with $v|_{\partial D} = 1$; and for the one-dimensional interval $D = (-a,b)$ the exit distribution is explicit: a Brownian motion started at $0$ leaves $(-a,b)$ at $b$ with probability $a/(a+b)$, the continuous form of the gambler's ruin formula of *Martingales*.

## Summary

Brownian motion is constructed from the Gaussian increment law by the Kolmogorov extension and continuity criteria, its law is the Wiener measure on the continuous path space, its paths are Hölder of every order below $1/2$ and of no higher order, nowhere differentiable, and of infinite total variation on every interval; its quadratic variation is the elapsed time. It is the Markov process whose transition density is the Gaussian heat kernel, whose transition semigroup is $e^{t\Delta/2}$ on $L^2(\mathbb{R}^d)$, and whose generator is half the Laplacian; the function $u(t,x) = \mathbb{E}^x[f(B_t)]$ solves the heat equation. The coordinate processes, the products $B_t^iB_t^j - \delta_{ij}t$, the squared norm $|B_t|^2 - dt$ and the exponentials $e^{\sigma\cdot B_t - |\sigma|^2t/2}$ are martingales, and Lévy's characterisation identifies a continuous local martingale with quadratic variation $t$ as a Brownian motion.

The Itô integral is defined for simple predictable integrands by the left-endpoint Riemann sums, is extended by the Itô isometry, and produces a continuous local martingale with quadratic variation $\int_0^tH_s^2ds$. Itô's formula is the change-of-variable formula for the integral, with the second-order term $\frac12f''d\langle X\rangle$ accounting for the nonzero quadratic variation; the Stratonovich integral is the midpoint version obeying the classical chain rule, and the two differ by half the covariation. Stochastic differential equations with Lipschitz coefficients have unique strong solutions, which are strong Markov processes with generator $b\cdot\nabla + \frac12\sigma\sigma^\top:\partial^2$, and the standard examples are geometric Brownian motion, the Ornstein–Uhlenbeck process and the Bessel processes. Girsanov's theorem changes the measure to remove a drift, Feynman–Kac represents the solution of the heat equation with a potential as an expectation, and Kakutani's formula solves the Dirichlet problem by the exit law of the motion, placing Brownian motion at the centre of the potential theory of the Laplacian.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $B_t$, $\{B_t\}_{t\ge0}$ | Standard Brownian motion in $\mathbb{R}^d$ |
| $\mathbb{W}$ | Wiener measure on $C([0,\infty),\mathbb{R}^d)$ |
| $\mathbb{P}^x$, $\mathbb{E}^x$ | Law and expectation of the motion started at $x$ |
| $V_\Pi(X)_t$ | Quadratic variation along a partition; $\langle X\rangle_t$ its limit |
| $p_t(x,y)$ | Brownian transition density, the Gaussian heat kernel |
| $P_t$, $\Delta$, $L$ | Transition semigroup $e^{t\Delta/2}$, Laplacian, generator $\frac12\Delta$ |
| $\int_0^tH_s\,dB_s$ | Itô integral; Itô isometry $\mathbb{E}(\int H\,dB)^2=\mathbb{E}\int H^2ds$ |
| $\langle X,Y\rangle_t$ | Quadratic covariation |
| Stratonovich $\circ$ | Midpoint integral, classical chain rule |
| $b$, $\sigma$ | Drift and diffusion coefficients of an SDE |
| $Z_t$, $\theta$, $\mathbb{Q}=Z_T\mathbb{P}$ | Girsanov density, shift, changed measure |
| $V$, Feynman–Kac | Potential and the representation of $e^{t(\Delta/2-V)}$ |
| $\tau_D$, Kakutani | Exit time from $D$; $u(x)=\mathbb{E}^x[\varphi(B_{\tau_D})]$ |
| Bessel drift | $(d-1)/(2R_t)$ in the radial SDE |



## Further Reading

- Ioannis Karatzas and Steven E. Shreve, *Brownian Motion and Stochastic Calculus* (Springer, 2nd edition, 1998), for the construction, the Itô calculus, the stochastic differential equations and the Girsanov theorem.
- Daniel Revuz and Marc Yor, *Continuous Martingales and Brownian Motion* (Springer, 3rd edition, 1999), for Lévy's characterisation, the Bessel processes and the general theory of continuous local martingales.
- Bernt Øksendal, *Stochastic Differential Equations: An Introduction with Applications* (Springer, 6th edition, 2003), for an accessible treatment of the Itô formula, the Feynman–Kac formula and the Dirichlet problem.
- Ioannis Karatzas and Steven E. Shreve, *Methods of Mathematical Finance* (Springer, 1998), for the Girsanov theorem, the martingale representation and the applications of the change of measure.
- Kiyosi Itô, "On stochastic differential equations", *Memoirs of the American Mathematical Society* 4 (1951), 1–51, and "Stochastic integral", *Proceedings of the Imperial Academy of Tokyo* 20 (1944), 519–524, for the original construction of the integral and the formula.
- Norbert Wiener, "Differential space", *Journal of Mathematics and Physics* 2 (1923), 131–174, for the construction of the Wiener measure.
- Joseph L. Doob, *Stochastic Processes* (Wiley, 1953), for the martingale theory underlying the calculus.
- Sidney C. Port and Charles J. Stone, *Brownian Motion and Classical Potential Theory* (Academic Press, 1978), for Kakutani's formula, the harmonic measure and the Dirichlet problem.
- Daniel W. Stroock and S. R. Srinivasa Varadhan, *Multidimensional Diffusion Processes* (Springer, 1979), for the martingale problem and the general theory of diffusions that the SDE theory instantiates.
