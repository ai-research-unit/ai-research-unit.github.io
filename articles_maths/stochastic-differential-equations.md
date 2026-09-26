
# __Stochastic Differential Equations__

## Introduction

A stochastic differential equation is an equation for a process whose infinitesimal increment has a deterministic part proportional to $dt$ and a random part proportional to the increment of a Brownian motion:

$$
dX_t = b(t,X_t)\,dt + \sigma(t,X_t)\,dB_t .
$$

The equation is not a differential equation in the classical sense, because the path $t\mapsto B_t$ is almost surely nowhere differentiable and the symbol $dB_t$ cannot be read as an infinitesimal; it is a bookkeeping device for an integral equation, $X_t = X_0+\int_0^tb(s,X_s)ds+\int_0^t\sigma(s,X_s)dB_s$, and the meaning of the second integral must be supplied by a definition. There are two definitions, the **Itô integral**, in which the integrand is evaluated at the left endpoint of each subinterval, and the **Stratonovich integral**, in which it is evaluated at the midpoint. The first has the better probabilistic properties — the integral of an adapted integrand is a martingale and the isometry $\mathbb{E}|\int\phi\,dB|^2=\mathbb{E}\int\phi^2dt$ holds — and the second has the better calculus: it obeys the classical chain rule, and the change-of-variables formula needs no second-order correction.

The two integrals differ by a correction term involving the quadratic variation, and the difference is the whole content of Itô's formula: for a smooth $f$,

$$
f(B_t) = f(B_0)+\int_0^tf'(B_s)\,dB_s+\frac12\int_0^tf''(B_s)\,ds ,
$$

the last term arising because the Brownian path accumulates quadratic variation $\langle B\rangle_t=t$ at a rate that makes the second-order Taylor term contribute at first order. Itô's formula is the fundamental theorem of the subject, and the generator $L$ of the process, defined by the equation $df(X_t)=Lf(X_t)dt+\text{martingale}$, is the object that connects the stochastic equation to the partial differential equations of this Part: the expectation $u(t,x)=\mathbb{E}_x[f(X_t)]$ solves the backward Kolmogorov equation $\partial_tu=Lu$, and with a killing or a discounting factor it solves the Feynman–Kac equation.

The article develops the Brownian motion and its quadratic variation; the Itô integral and its isometry; Itô's formula and the generator; the Stratonovich integral, the correction formula and the conversion between the two forms of an equation; existence and uniqueness of strong solutions by Picard iteration, weak solutions and the Yamada–Watanabe principle; Girsanov's theorem and the change of measure; the Markov property, the Kolmogorov equations and Feynman–Kac; and the standard examples, the geometric Brownian motion, the Ornstein–Uhlenbeck process and the Bessel process. The measure theory is that of *Measure Theory and Integration*, and the probability spaces, martingales and Brownian motion are the notions of the probability articles of this Part, written in parallel; the partial differential equations that appear are those of the earlier article of this Part, and the semigroup theory connecting them is that of the preceding article.

## Brownian Motion and the Itô Integral

### Brownian Motion

**Definition.** A **Brownian motion** on a probability space $(\Omega,\mathcal{F},\mathbb{P})$ with a filtration $(\mathcal{F}_t)_{t\ge0}$ satisfying the usual conditions is an adapted process $B = (B_t)_{t\ge0}$ with:

1. $B_0=0$ almost surely;
2. for $0\le s<t$ the increment $B_t-B_s$ is independent of $\mathcal{F}_s$ and is Gaussian with mean zero and variance $t-s$;
3. the paths $t\mapsto B_t$ are continuous almost surely.

Its **quadratic variation** on $[0,t]$ is $\langle B\rangle_t=t$, in the sense that for any sequence of partitions with mesh tending to $0$ the sums $\sum_i(B_{t_{i+1}}-B_{t_i})^2$ converge to $t$ in probability; equivalently, $\langle B\rangle_t=t$ and the process $B_t^2-t$ is a martingale.

**Remark (the two pathologies).** Brownian paths are continuous and nowhere differentiable, and they have infinite variation on every interval; consequently the Riemann–Stieltjes integral $\int\phi\,dB$ does not exist by the classical theory, and the choice of the point at which the integrand is evaluated matters. It is the finite quadratic variation, and not the finite variation, that makes the stochastic integral possible.

### The Itô Integral

**Definition.** Let $(\mathcal{F}_t)$ be the filtration and let $\mathcal{H}^2$ be the space of progressively measurable processes $\phi$ with $\mathbb{E}\int_0^T\phi_s^2ds<\infty$. For a **simple** process $\phi_s=\sum_i\xi_i\mathbf{1}_{(t_i,t_{i+1}]}(s)$ with $\xi_i$ bounded and $\mathcal{F}_{t_i}$-measurable, the **Itô integral** is

$$
\int_0^T\phi_s\,dB_s = \sum_i\xi_i\bigl(B_{t_{i+1}}-B_{t_i}\bigr),
$$

the integrand being evaluated at the **left** endpoint of each interval.

**Theorem (Itô isometry and the extension).** For simple $\phi$,

$$
\mathbb{E}\left[\int_0^T\phi_s\,dB_s\right] = 0, \qquad
\mathbb{E}\left|\int_0^T\phi_s\,dB_s\right|^2 = \mathbb{E}\int_0^T\phi_s^2\,ds ,
$$

and the integral extends uniquely to an isometry $\mathcal{H}^2\to L^2(\Omega)$; the extended stochastic process $t\mapsto\int_0^t\phi_s\,dB_s$ is a continuous martingale with quadratic variation $\langle\int\phi\,dB\rangle_t=\int_0^t\phi_s^2ds$.

*Proof.* For simple processes the two identities follow from the independence and the Gaussian moments of the increments: cross terms vanish because the $\xi_i\xi_j$ with $i<j$ are $\mathcal{F}_{t_j}$-measurable and the conditional mean of $B_{t_{j+1}}-B_{t_j}$ vanishes. The isometry makes the map an isometry from the dense subspace of simple processes into $L^2(\Omega)$, and the completeness of $L^2$ gives the extension. The martingale property follows by conditioning on $\mathcal{F}_s$ and using the independence of the increments beyond $s$. $\square$

**Definition.** For a general integrand $\phi\in\mathcal{H}^2$ the integral is the $L^2$ limit of the integrals of an approximating sequence of simple processes.

**Example (integrating the Brownian motion against itself).** With $\phi_s=B_s$ the Itô integral is $\int_0^tB_s\,dB_s=\frac12(B_t^2-t)$: the integral differs from the naive $\frac12B_t^2$ by $-\frac t2$, and the correction is the quadratic variation. With $\phi$ the left-continuous evaluation the value is forced by the isometry; evaluating at the midpoint instead gives the Stratonovich integral below, which is exactly $\frac12B_t^2$.

## Itô's Formula and the Generator

**Theorem (Itô's formula, one-dimensional).** Let $f\in C^{1,2}([0,\infty)\times\mathbb{R})$ and let $X_t = X_0+\int_0^tb_s\,ds+\int_0^t\sigma_s\,dB_s$ with $b,\sigma$ in the appropriate integrability classes. Then almost surely, for all $t$,

$$
f(t,X_t) = f(0,X_0)+\int_0^t\Bigl(\partial_sf(s,X_s)+b_s\partial_xf(s,X_s)+\tfrac12\sigma_s^2\partial_{xx}f(s,X_s)\Bigr)ds+\int_0^t\sigma_s\partial_xf(s,X_s)\,dB_s .
$$

*Proof.* Quoted as standard. The proof is a Taylor expansion along a partition: the first-order terms converge to the drift and the stochastic integral, and the second-order term in $x$ leaves the sum $\sum(\Delta X_i)^2$, which converges to the quadratic variation $\int\sigma_s^2ds$ rather than to zero. The third- and higher-order terms are of higher order by the finite quadratic variation and the continuity of the paths. $\square$

**Definition.** For a diffusion $dX_t=b(t,X_t)dt+\sigma(t,X_t)dB_t$ with $\sigma\sigma^{\mathrm{T}}$ the diffusion matrix, the **generator** is the second-order operator

$$
Lf(t,x) = b(t,x)\cdot\nabla_xf(t,x)+\frac12\operatorname{tr}\bigl(\sigma\sigma^{\mathrm{T}}(t,x)\nabla_x^2f(t,x)\bigr),
$$

so that $df(t,X_t) = \bigl(\partial_t+L\bigr)f(t,X_t)dt+\nabla_xf(t,X_t)^{T}\sigma(t,X_t)dB_t$; the last differential is a martingale differential, and the finite-variation part of $f(t,X_t)$ is $\bigl(\partial_t+L\bigr)f\,dt$.

**Corollary (Dynkin's formula).** If $\tau$ is a stopping time with $\mathbb{E}_x[\tau]<\infty$ and $f$ is $C^2$ with compact support, then

$$
\mathbb{E}_x\bigl[f(X_\tau)\bigr] = f(x)+\mathbb{E}_x\left[\int_0^\tau Lf(X_s)\,ds\right] .
$$

*Proof.* Apply Itô's formula to $f(X_t)$, note that the stochastic integral is a martingale, and take expectations at the stopping time $\tau$; the optional stopping theorem for a bounded martingale and a truncation argument for the integrability of $\tau$ justify the passage. $\square$

**Remark (the generator and the operators of the previous articles).** The generator $L$ is an elliptic second-order operator with the ellipsoid of the diffusion matrix as its symbol, so the backward equation $\partial_tu+Lu=0$ is a parabolic equation of the type studied in the earlier article of this Part: elliptic when the diffusion matrix is positive definite, degenerate when it is not, and with the boundary conditions supplied by the problem. The transition semigroup $P_tf(x)=\mathbb{E}_x[f(X_t)]$ is a strongly continuous semigroup on a suitable Banach space whose generator is $L$, and the well-posedness theory of the semigroup article applies to it; this is the precise point of contact between the stochastic and the deterministic theories.

## The Stratonovich Integral

**Definition.** For a process $\phi$ and a partition with mesh $|\pi|\to0$, the **Stratonovich integral** is the limit in probability of the midpoint sums

$$
\int_0^T\phi_s\circ dB_s = \lim_{|\pi|\to0}\sum_i\phi\left(\frac{t_i+t_{i+1}}{2}\right)\bigl(B_{t_{i+1}}-B_{t_i}\bigr).
$$

**Theorem (Itô–Stratonovich correction).** For a continuous semimartingale $\phi$ and Brownian motion $B$,

$$
\int_0^t\phi_s\circ dB_s = \int_0^t\phi_s\,dB_s+\frac12\langle\phi,B\rangle_t ,
$$

where $\langle\phi,B\rangle_t$ is the joint quadratic variation; in particular, if $\phi_s=f(B_s)$ for a $C^1$ function $f$, then

$$
\int_0^tf(B_s)\circ dB_s = \int_0^tf(B_s)\,dB_s+\frac12\int_0^tf'(B_s)\,ds .
$$

*Proof.* Quoted as standard. The midpoint value differs from the left endpoint by $\frac12(\phi_{t_{i+1}}-\phi_{t_i})$, and the sum of these differences times the corresponding Brownian increment converges to $\frac12\langle\phi,B\rangle_t$ by the definition of the joint quadratic variation; for $\phi=f(B)$ the joint variation is computed from the quadratic variation of $B$, giving the second formula. $\square$

**Theorem (the Stratonovich chain rule).** If $X_t = X_0+\int_0^t\sigma(X_s)\circ dB_s+\int_0^tb(X_s)ds$ is a Stratonovich equation and $f\in C^3$, then

$$
f(X_t) = f(X_0)+\int_0^tf'(X_s)\circ dX_s ,
$$

so the classical chain rule holds and the change of variables requires no second-order term.

*Proof.* Quoted as standard. The correction term of the Itô–Stratonovich formula is exactly the second-order term of Itô's formula, so the two formulas combine to the classical one. $\square$

**Theorem (conversion between Itô and Stratonovich forms).** In one dimension, the Itô equation $dX_t=b(X_t)dt+\sigma(X_t)dB_t$ is equivalent to the Stratonovich equation

$$
dX_t = \Bigl(b(X_t)-\tfrac12\sigma'(X_t)\sigma(X_t)\Bigr)dt+\sigma(X_t)\circ dB_t ,
$$

and conversely; in several dimensions the correction term is $\frac12\sum_{j,k}\sigma^j_k\partial_{x_j}\sigma^i_k$ in the $i$-th component.

*Proof.* Apply the Stratonovich chain rule to $\sigma(X_t)$ and substitute the Itô equation: the cross variation $\langle\sigma(X),B\rangle_t=\int\sigma'\sigma\,ds$ produces the drift correction, and the equivalence follows. $\square$

**Remark (which calculus to use).** The Itô form is the one in which the generator, the martingale property and the martingale problem are stated, and it is the form in which the theory is proved. The Stratonovich form is the one in which the equation is written when the noise is a limit of smooth processes, and the one in which the transformation rules of differential geometry apply; for a stochastic flow of diffeomorphisms, the Stratonovich equation is the one whose solutions depend smoothly on the initial datum. The two are equivalent, and the conversion rule above is the dictionary.

## Existence, Uniqueness and the Martingale Problem

**Definition.** A **strong solution** of the equation $dX_t=b(t,X_t)dt+\sigma(t,X_t)dB_t$ with initial datum $X_0$ on a given probability space with a given Brownian motion $B$ is an adapted continuous process $X$ satisfying the integral equation almost surely. A **weak solution** is a tuple $(\Omega,\mathcal{F},\mathbb{P},\mathcal{F}_t,B,X)$ with the same property; **pathwise uniqueness** means that two solutions on the same space with the same $B$ agree almost surely, and **uniqueness in law** means that any two weak solutions have the same law.

**Theorem (existence and pathwise uniqueness under Lipschitz conditions).** Let $b$ and $\sigma$ be measurable, locally Lipschitz in $x$ uniformly in $t$, and of at most linear growth: $|b(t,x)|+|\sigma(t,x)|\le C(1+|x|)$. Then for every $X_0\in L^2(\Omega)$ the equation has a strong solution, unique among solutions with $\mathbb{E}\int_0^T|X_t|^2dt<\infty$; the solution is a continuous semimartingale, and it satisfies $\mathbb{E}[\sup_{t\le T}|X_t|^2]<\infty$.

*Proof.* Quoted as standard (the Picard iteration for stochastic equations). One defines $X^{(0)}_t=X_0$ and $X^{(n+1)}_t = X_0+\int_0^tb(s,X^{(n)}_s)ds+\int_0^t\sigma(s,X^{(n)}_s)dB_s$; the Lipschitz condition and the Burkholder–Davis–Gundy inequality give $\mathbb{E}[\sup_{t\le T}|X^{(n+1)}_t-X^{(n)}_t|^2]\le C\int_0^T\mathbb{E}[\sup_{s\le t}|X^{(n)}_s-X^{(n-1)}_s|^2]dt$, whose iteration converges geometrically, so the sequence converges uniformly on $[0,T]$ in $L^2$ and the limit solves the equation. Pathwise uniqueness follows from the same estimate applied to the difference of two solutions, whose initial datum is zero: the difference is bounded by a constant times its own integral, hence vanishes by Gronwall's inequality. $\square$

**Theorem (Yamada–Watanabe).** Pathwise uniqueness implies uniqueness in law, and if in addition a weak solution exists then a strong solution exists.

*Proof.* Quoted as standard. The principle is proved by constructing the solution as a measurable functional of the driving Brownian motion, using the almost sure convergence of a Picard-type iteration under the weaker hypotheses; uniqueness in law then follows from pathwise uniqueness by an approximation of the coefficients by Lipschitz ones. $\square$

**Definition.** The **martingale problem** for the generator $L$ and the initial law $\mu$ asks for a process $X$ with $X_0\sim\mu$ such that $f(X_t)-\int_0^tLf(X_s)ds$ is a martingale for every $f$ in the domain of $L$. A solution of the martingale problem is a weak solution of the stochastic equation, and conversely.

**Theorem (Stroock–Varadhan).** If $L$ is the generator of a diffusion with bounded measurable coefficients and a uniformly elliptic diffusion matrix, then the martingale problem for $L$ and any initial law is well posed: there is a unique solution law, and the associated transition kernels form a Feller semigroup.

*Proof.* Quoted as standard (Stroock–Varadhan). The existence is by a compactness argument on the laws of approximating processes with smooth coefficients, using the tightness supplied by the uniformity of the oscillation estimates; the uniqueness is by the identification of the generator through the maximum principle for the associated parabolic equation. $\square$

**Example (a Lipschitz equation).** The equation $dX_t=-\theta X_tdt+\sigma dB_t$ with constants $\theta,\sigma$ satisfies the Lipschitz hypotheses, and its solution is

$$
X_t = e^{-\theta t}X_0+\sigma\int_0^te^{-\theta(t-s)}dB_s ,
$$

the Ornstein–Uhlenbeck process; if $X_0$ is Gaussian so is $X_t$, with mean $e^{-\theta t}\mathbb{E}X_0$ and variance $e^{-2\theta t}\operatorname{Var}X_0+\frac{\sigma^2}{2\theta}(1-e^{-2\theta t})$, tending to the stationary value $\sigma^2/(2\theta)$ as $t\to\infty$. The example is the standard mean-reverting diffusion and the standard instance in which the solution is written explicitly.

**Remark (non-Lipschitz coefficients).** Without the Lipschitz condition the two uniqueness notions separate, and the classical examples exhibit the two possible failures. Girsanov's example is the one-dimensional equation $dX_t=|X_t|^{\alpha}dB_t$ with $X_0=0$ and $0<\alpha<\frac12$: the process $X\equiv0$ is a solution and there are nontrivial solutions as well, so uniqueness in law fails and hence, by the implication part of the Yamada–Watanabe theorem, pathwise uniqueness fails too. Tanaka's equation $dX_t=\operatorname{sgn}(X_t)\,dB_t$, $X_0=0$, exhibits the sharper phenomenon of pathwise non-uniqueness together with uniqueness in law: by Lévy's characterisation every solution is a Brownian motion, so the law is unique, while two solutions driven by the same $B$ need not coincide. The distinction is not a technicality: it separates the equations that determine the path from the Brownian motion (strong solutions, dependent on $B$) from those that determine only the law (weak solutions, which may be constructed on a different probability space).

## Girsanov's Theorem and the Change of Measure

**Theorem (Girsanov).** Let $B$ be a Brownian motion on $(\Omega,\mathcal{F},(\mathcal{F}_t),\mathbb{P})$ and let $\theta$ be an adapted process satisfying Novikov's condition $\mathbb{E}\exp\bigl(\frac12\int_0^T\theta_s^2ds\bigr)<\infty$. Then

$$
\frac{d\mathbb{Q}}{d\mathbb{P}}\Bigr|_{\mathcal{F}_t} = \exp\left(-\int_0^t\theta_s\,dB_s-\frac12\int_0^t\theta_s^2\,ds\right)
$$

defines a probability measure $\mathbb{Q}\sim\mathbb{P}$, and the process

$$
\tilde B_t = B_t+\int_0^t\theta_s\,ds
$$

is a Brownian motion under $\mathbb{Q}$.

*Proof.* Quoted as standard. The exponential is a positive martingale under Novikov's condition, so $\mathbb{Q}$ is a probability measure equivalent to $\mathbb{P}$; Bayes' rule shows that $\tilde B$ has the martingale property and the correct quadratic variation $t$ under $\mathbb{Q}$, and Lévy's characterisation of Brownian motion (a continuous local martingale with $\langle\tilde B\rangle_t=t$ is a Brownian motion) identifies it. $\square$

**Corollary (removing a drift).** An equation with a drift, $dX_t=b(t,X_t)dt+dB_t$, can be transformed into a driftless equation by the change of measure with $\theta_t=b(t,X_t)$; consequently the law of the solution with drift is absolutely continuous with respect to that of the driftless solution on each finite time interval, with the Radon–Nikodym density given above.

## The Markov Property and the Kolmogorov Equations

**Theorem (Markov property and the transition semigroup).** Under the hypotheses ensuring existence and uniqueness, the solution of $dX_t=b(t,X_t)dt+\sigma(t,X_t)dB_t$ has the Markov property: for $s<t$ and bounded measurable $f$,

$$
\mathbb{E}\bigl[f(X_t)\,\big|\,\mathcal{F}_s\bigr] = P_{s,t}f(X_s), \qquad P_{s,t}f(x) = \mathbb{E}_x\bigl[f(X_{t-s})\bigr],
$$

and for time-homogeneous coefficients the kernels $P_t$ form a semigroup, $P_{s,t}=P_{0,t-s}$ and $P_{s+t}=P_sP_t$.

*Proof.* The solution restarted at time $s$ from $X_s$ solves the same equation driven by the shifted Brownian motion by the strong uniqueness; the conditional expectation depends on $\mathcal{F}_s$ only through $X_s$, which is the Markov property, and the semigroup law is the composition of the transitions. $\square$

**Theorem (backward and forward Kolmogorov equations).** Let $u(t,x)=\mathbb{E}_x[f(X_t)]$ for $f$ smooth. Then $u$ solves the **backward Kolmogorov equation**

$$
\partial_tu = Lu, \qquad u(0,x)=f(x),
$$

in the classical sense when the coefficients and $f$ are smooth, and more generally in the weak sense. If $X$ has a transition density $p(t,x,y)$ with respect to Lebesgue measure, then $p$ solves the **forward Kolmogorov** or **Fokker–Planck equation**

$$
\partial_tp = L^*p, \qquad L^*p = -\sum_i\partial_{x_i}(b_ip)+\frac12\sum_{i,j}\partial_{x_ix_j}\bigl((\sigma\sigma^{\mathrm{T}})_{ij}p\bigr),
$$

with the initial condition $p(0,\cdot,y)\to\delta_y$.

*Proof.* Apply Itô's formula to $u(T-t,X_t)$: the drift is $(-\partial_tu+Lu)(T-t,X_t)$ and the stochastic integral is a martingale; taking expectations over $[0,T]$ and using $u(0,X_T)=f(X_T)$ gives the backward equation when the drift vanishes for every $f$, and the Fokker–Planck equation is the formal adjoint obtained by integrating the backward equation against a test function. $\square$

**Theorem (Feynman–Kac).** Let $V$ be bounded and continuous and let $f$ be bounded. Then

$$
u(t,x) = \mathbb{E}_x\left[\exp\left(-\int_0^tV(X_s)ds\right)f(X_t)\right]
$$

is the unique bounded solution of $\partial_tu = Lu - Vu$ with $u(0,x)=f(x)$.

*Proof.* Quoted as standard (the Feynman–Kac formula). Let $Z_t = \exp(-\int_0^tV(X_s)ds)\,u(t,X_t)$. Itô's formula applied to the product gives
$dZ_t = e^{-\int_0^tV}\bigl(\partial_tu+Lu-Vu\bigr)(t,X_t)\,dt+d(\text{martingale})$;
when $\partial_tu=Lu-Vu$ the finite-variation part vanishes, so $Z$ is a martingale, and taking expectations between $0$ and $t$ gives $\mathbb{E}_x[Z_t]=Z_0=u(0,x)=f(x)$, which is the formula. Uniqueness follows from the maximum principle and the boundedness of $V$. $\square$

**Example (geometric Brownian motion).** For $dX_t=\mu X_tdt+\sigma X_tdB_t$ with constants $\mu,\sigma$, the solution is

$$
X_t = X_0\exp\left(\Bigl(\mu-\frac{\sigma^2}{2}\Bigr)t+\sigma B_t\right),
$$

obtained by applying Itô's formula to $\log X_t$: the Itô correction $-\frac12\sigma^2dt$ is exactly the term the naive calculus would miss, and without it the formula would not solve the equation. The process is the standard model of multiplicative noise, and its log-normal marginal law is the elementary consequence of the formula.

## Summary

A stochastic differential equation $dX_t=b(t,X_t)dt+\sigma(t,X_t)dB_t$ is an integral equation driven by Brownian motion, whose paths are continuous, nowhere differentiable and of quadratic variation $\langle B\rangle_t=t$. The Itô integral evaluates the integrand at the left endpoint, is a martingale with the isometry $\mathbb{E}|\int\phi\,dB|^2=\mathbb{E}\int\phi^2ds$, and satisfies Itô's formula $df(t,X_t)=(\partial_t+L)f\,dt+\nabla f^{\mathrm{T}}\sigma\,dB_t$ with the second-order correction; the Stratonovich integral evaluates the midpoint, differs from the Itô integral by $\frac12\langle\phi,B\rangle_t$, obeys the classical chain rule, and is converted to the Itô form by the drift correction $-\frac12\sigma'\sigma$. The generator $L=b\cdot\nabla+\frac12\operatorname{tr}(\sigma\sigma^{\mathrm{T}}\nabla^2)$ governs the process: Dynkin's formula holds, the transition kernels form a semigroup with generator $L$, and the expectations solve the backward Kolmogorov and Feynman–Kac equations, with the Fokker–Planck equation as the adjoint. Existence and pathwise uniqueness hold for locally Lipschitz coefficients by Picard iteration together with the Burkholder–Davis–Gundy inequality; Yamada–Watanabe passes from pathwise uniqueness to uniqueness in law and from a weak solution to a strong one, and the Stroock–Varadhan martingale problem characterises the weak solutions. Girsanov's theorem changes the measure by an exponential martingale and converts a drift into a Brownian motion, and the standard explicit examples are the Ornstein–Uhlenbeck process and the geometric Brownian motion.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(\Omega,\mathcal{F},(\mathcal{F}_t),\mathbb{P})$ | Filtered probability space |
| $B_t$ | Brownian motion; $B_0=0$, $\langle B\rangle_t=t$ |
| $\langle\cdot,\cdot\rangle_t$ | Quadratic variation and joint quadratic variation |
| $X_t$ | Solution process of the stochastic equation |
| $b$, $\sigma$, $\sigma\sigma^{\mathrm{T}}$ | Drift, diffusion coefficient, diffusion matrix |
| $\int\phi\,dB$, $\int\phi\circ dB$ | Itô and Stratonovich integrals |
| Itô formula | $df=(\partial_t+L)f\,dt+\nabla f^{\mathrm{T}}\sigma\,dB$ |
| $L$, $L^*$ | Generator and its formal adjoint |
| $\mathbb{E}_x$ | Expectation for the process started at $x$ |
| $P_t$, $P_{s,t}$ | Transition semigroup and kernels |
| $p(t,x,y)$ | Transition density; Feynman–Kac solution $u$ |
| $\theta$, $\mathbb{Q}$ | Girsanov integrand and the equivalent measure |
| $\tau$ | Stopping time; Dynkin's formula |

## Further Reading

- Kiyosi Itô, "Stochastic Integral", *Proceedings of the Imperial Academy* 20 (1944), for the construction of the integral.
- Kiyosi Itô, "On a Formula Concerning Stochastic Differentials", *Nagoya Mathematical Journal* 3 (1951), for Itô's formula.
- Ruslan L. Stratonovich, "A New Representation for Stochastic Integrals and Equations", *SIAM Journal on Control* 4 (1966), for the symmetric integral and the chain rule.
- Bernt Øksendal, *Stochastic Differential Equations: An Introduction with Applications* (Springer, 6th ed. 2003), for a systematic introduction with the standard examples.
- Ioannis Karatzas and Steven E. Shreve, *Brownian Motion and Stochastic Calculus* (Springer, 2nd ed. 1991), for the Itô integral, Girsanov's theorem and the martingale problem.
- Daniel W. Stroock and S. R. Srinivasa Varadhan, *Multidimensional Diffusion Processes* (Springer, 1979), for the martingale problem and the well-posedness theory.
- Philip E. Protter, *Stochastic Integration and Differential Equations* (Springer, 2nd ed. 2005), for semimartingale integration and the general theory.
- Alexander D. Wentzell, *A Course in the Theory of Stochastic Processes* (McGraw-Hill, 1981), for the generator and the Kolmogorov equations.
- Toshio Yamada and Shinzo Watanabe, "On the Uniqueness of Solutions of Stochastic Differential Equations", *Journal of Mathematics of Kyoto University* 11 (1971), for the Yamada–Watanabe principle.
