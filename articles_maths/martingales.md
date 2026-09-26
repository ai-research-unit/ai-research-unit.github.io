
# __Martingales__

## Introduction

A martingale is the mathematical model of a fair game. The process records the fortune of a gambler, the filtration records the history of the play, and the defining relation — the conditional expectation of tomorrow's fortune given today's history equals today's fortune — is the statement that the game offers no advantage at any time. The theory built on this definition is the most useful part of probability: the maximal inequalities control the size of a process at all times, the convergence theorem decides when a process has a limit, the optional stopping theorem permits the replacement of a fixed time by a random one, and the tools apply to sums of independent variables, to likelihood ratios, to branching processes and to the fluctuations of an estimator.

This article develops the discrete-time theory. It defines the filtration, the stopping time and the three varieties of the martingale, gives the standard examples, proves the Doob decomposition, the maximal inequality and the upcrossing inequality, establishes the almost-sure and $L^p$ convergence theorems, characterises the uniformly integrable martingales and proves the optional stopping theorem in the forms in which it is used, and derives the martingale central limit theorem as the bridge to the continuous-time theory.

The place of the article is fixed by three boundaries.

- The **probability notation** is *Measure-Theoretic Probability*: $(\Omega,\mathcal{F},\mathbb{P})$, $\mathbb{E}$, a.s., the four modes of convergence and the characteristic function. The **conditional expectation**, the **filtration**, the **adapted and predictable processes** and the **Borel–Cantelli and zero–one laws** are *Independence and Conditional Expectation*; this article uses them throughout and adds to them the stopping time, the martingale and the maximal inequality. The **law of large numbers and the central limit theorem** are *Laws of Large Numbers and the Central Limit Theorem*, and the martingale versions proved here contain them.
- The **Markov chains and processes** are the subject, and the **Brownian motion and stochastic calculus**; the continuous-time martingale theory — the optional stopping theorem for continuous time, the Doob–Meyer decomposition, the quadratic variation and the stochastic integral — is developed there on the basis of the discrete theory here, and the bridge to it is the martingale functional central limit theorem stated in the last section.
- The **ergodic theory** iswhere the martingale convergence theorem is a tool of the proof of the individual ergodic theorem in the form of the Hopf maximal inequality; that use is cited and not rehearsed. No physics is invoked.

Throughout, $(\Omega,\mathcal{F},\{\mathcal{F}_n\},\mathbb{P})$ is a filtered probability space as in *Independence and Conditional Expectation*, with $\mathcal{F}_0 \subseteq \mathcal{F}_1 \subseteq \cdots \subseteq \mathcal{F}$ and $\mathcal{F}_\infty = \sigma(\bigcup_n\mathcal{F}_n)$; a process $\{X_n\}_{n\geq0}$ is adapted when $X_n$ is $\mathcal{F}_n$-measurable and integrable when $\mathbb{E}|X_n| < \infty$ for every $n$. The conditional expectation is written $\mathbb{E}[X \mid \mathcal{F}_n]$, and $\wedge$ denotes the minimum of two numbers.

## Filtrations, Stopping Times and the Definitions

### The Martingale Definitions

**Definition.** An adapted integrable process $\{X_n\}$ is a **martingale** if

$$
\mathbb{E}[X_{n+1} \mid \mathcal{F}_n] = X_n \qquad \text{a.s. for every } n \geq 0;
$$

it is a **submartingale** if $\mathbb{E}[X_{n+1} \mid \mathcal{F}_n] \geq X_n$ a.s., and a **supermartingale** if the inequality is reversed. Equivalently, $\mathbb{E}[X_{m} \mid \mathcal{F}_n] = X_n$ a.s. for all $m \geq n$, by the tower property of *Independence and Conditional Expectation*.

The three notions are ordered by the sign of the drift: a submartingale tends to increase, a supermartingale to decrease, and a martingale to stay level. Every martingale is both a submartingale and a supermartingale, and a process that is both is a martingale. The names come from the gambler's fortune, and the convention is that of the gambler: a supermartingale is an unfavourable game.

**Example (sums of independent variables).** Let $\{Y_n\}$ be independent integrable variables and let $\mathcal{F}_n = \sigma(Y_0,\dots,Y_n)$. Then $S_n = \sum_{k=1}^n Y_k$ is a martingale if $\mathbb{E}Y_k = 0$ for every $k$, a submartingale if $\mathbb{E}Y_k \geq 0$, and a supermartingale if $\mathbb{E}Y_k \leq 0$; the verification is $\mathbb{E}[S_{n+1}\mid\mathcal{F}_n] = S_n + \mathbb{E}[Y_{n+1}]$ by independence. This is the fundamental example, and it shows that the martingale theory contains the theory of sums of independent variables.

**Example (conditional expectations).** For an integrable $X$ and a filtration $\{\mathcal{F}_n\}$, the process $X_n = \mathbb{E}[X \mid \mathcal{F}_n]$ is a uniformly integrable martingale, by the tower property. The process is the archetype of a martingale closed by a terminal variable, and it is the object of Lévy's theorem below.

**Example (likelihood ratios).** Let $\mathbb{Q} \ll \mathbb{P}$ on $\mathcal{F}_\infty$ with density $Z = d\mathbb{Q}/d\mathbb{P}$, and let $Z_n = \mathbb{E}[Z \mid \mathcal{F}_n]$. Then $\{Z_n\}$ is a martingale, the **likelihood ratio process**, and the change of measure $\mathbb{Q}|_{\mathcal{F}_n} = Z_n\,\mathbb{P}|_{\mathcal{F}_n}$ is the basis of the sequential analysis and of the Girsanov theorem.

**Proposition (closure properties).** The martingales form a vector space. If $X$ is a martingale and $\varphi$ is convex with $\varphi(X_n)$ integrable for every $n$, then $\{\varphi(X_n)\}$ is a submartingale, by Jensen's inequality for the conditional expectation; in particular $\{|X_n|\}$ and $\{X_n^2\}$ are submartingales when integrable. If $X$ and $Y$ are martingales and $H$ is bounded and predictable, then the **martingale transform** $(H \cdot X)_n = \sum_{k=1}^n H_k(X_k - X_{k-1})$ is a martingale; this is the discrete stochastic integral, and it is the statement that a bounded predictable strategy applied to a fair game remains fair.

### Stopping Times

**Definition.** A **stopping time** with respect to $\{\mathcal{F}_n\}$ is a random variable $\tau$ with values in $\{0,1,\dots\} \cup \{\infty\}$ such that $\{\tau \leq n\} \in \mathcal{F}_n$ for every $n$. For a stopping time $\tau$ the **$\sigma$-algebra at $\tau$** is

$$
\mathcal{F}_\tau = \{A \in \mathcal{F}_\infty : A \cap \{\tau \leq n\} \in \mathcal{F}_n \text{ for every } n\},
$$

and the **stopped process** is $X_n^\tau = X_{n\wedge\tau}$.

A stopping time is a rule for stopping that uses only the information available at the time of stopping: the event that the process has stopped by time $n$ must be decidable at time $n$. The distinction between stopping times and arbitrary random times is exactly the measurability requirement, and it is what makes the optional stopping theorem work. The standard examples are the first passage times $\tau_a = \inf\{n : S_n \geq a\}$, which are stopping times because $\{\tau_a \leq n\} = \{\max_{k\leq n}S_k \geq a\}$ is in $\mathcal{F}_n$, and a deterministic time is a stopping time.

**Proposition (basic properties).** If $\tau, \sigma$ are stopping times then $\tau \wedge \sigma$, $\tau \vee \sigma$ and $\tau + \sigma$ are stopping times; and $X^\tau$ is adapted, $\mathcal{F}_\tau$-measurable at $\tau$, and a martingale (respectively submartingale, supermartingale) whenever $X$ is one. The last statement is the first form of optional stopping, and its proof is the direct computation of the conditional expectation of $X_{n\wedge\tau}$.

## The Doob Decomposition and the Maximal Inequality

### The Doob Decomposition

**Theorem (Doob decomposition).** Let $\{X_n\}$ be a submartingale. Then there is a martingale $\{M_n\}$ and a predictable increasing process $\{A_n\}$ with $A_0 = 0$ such that

$$
X_n = M_n + A_n \qquad \text{for all } n,
$$

and the decomposition is unique up to an a.s. equivalence. Here predictable means $A_n$ is $\mathcal{F}_{n-1}$-measurable, and increasing means $A_{n+1} \geq A_n$ a.s. The first differences are $A_{n+1} - A_n = \mathbb{E}[X_{n+1} - X_n \mid \mathcal{F}_n]$.

The decomposition separates a submartingale into its martingale part and its systematic drift, and it is the discrete form of the Doob–Meyer decomposition of continuous-time semimartingales. The predictable increasing process is the compensator, and in the theory of the stochastic integral it is the object against which an integrand is integrated.

### Doob's Maximal Inequality

**Theorem (Doob's maximal inequality).** Let $\{X_n\}$ be a nonnegative submartingale and let $X_n^* = \max_{0\leq k\leq n}X_k$. Then for every $\lambda > 0$,

$$
\lambda\,\mathbb{P}(X_n^* \geq \lambda) \leq \mathbb{E}\bigl[X_n\,\mathbf{1}_{\{X_n^* \geq \lambda\}}\bigr] \leq \mathbb{E}[X_n].
$$

*Proof.* Let $\tau = \inf\{k : X_k \geq \lambda\}\wedge n$; the event $\{X_n^* \geq \lambda\}$ is $\mathcal{F}_\tau$-measurable, and $X_\tau \geq \lambda$ on it. The stopped submartingale satisfies $\mathbb{E}[X_n \mid \mathcal{F}_\tau] \geq X_\tau$, whence

$$
\mathbb{E}[X_n] \geq \mathbb{E}[X_n\mathbf{1}_{\{X_n^*\geq\lambda\}}] \geq \mathbb{E}[X_\tau \mathbf{1}_{\{X_n^*\geq\lambda\}}] \geq \lambda\,\mathbb{P}(X_n^*\geq\lambda).
$$

$\square$

The maximal inequality is the martingale form of the Kolmogorov inequality of *Laws of Large Numbers and the Central Limit Theorem*, and it is the engine of the almost-sure convergence theorem below. Its $L^p$ version is the following.

**Theorem (Doob's $L^p$ inequality).** For a nonnegative submartingale and $p > 1$,

$$
\|X_n^*\|_p \leq \frac{p}{p-1}\,\|X_n\|_p,
$$

and for a martingale the same inequality holds with $|X|$ in place of $X$ and $X_n^{**} = \max_{k\leq n}|X_k|$.

The constant $p/(p-1)$ is the best possible, and the inequality is the reason the martingale transform and the stochastic integral are bounded operators on $L^p$. The case $p = 2$ gives $\|X_n^*\|_2 \leq 2\|X_n\|_2$ and is the form used in the martingale central limit theorem.

### The Upcrossing Inequality

**Definition.** For $a < b$ the number of **upcrossings** $U_n(a,b)$ of the interval $[a,b]$ by the process $\{X_k\}$ up to time $n$ is the number of times the process passes from below $a$ to above $b$: it is defined by the successive passage times

$$
\sigma_1 = \inf\{k : X_k \leq a\}, \quad \tau_1 = \inf\{k \geq \sigma_1 : X_k \geq b\}, \quad \sigma_2 = \inf\{k \geq \tau_1 : X_k \leq a\}, \dots
$$

and $U_n(a,b) = \#\{j : \tau_j \leq n\}$.

**Theorem (upcrossing inequality).** Let $\{X_n\}$ be a submartingale and $a < b$. Then

$$
\mathbb{E}\bigl[U_n(a,b)\bigr] \leq \frac{\mathbb{E}\bigl[(X_n - a)^+\bigr]}{b-a} \leq \frac{\mathbb{E}|X_n| + |a|}{b-a}.
$$

*Proof.* The process $(X_{n\wedge\tau_j} - a)^+$ increased at each upcrossing by at least $b - a$; summing the expected increments of the submartingale $(X_n - a)^+$ over the intervals and comparing with the upcrossing count gives the bound. Alternatively, apply the optional stopping theorem to the submartingale $(X_n - a)^+$ at the passage times; the bounded number of crossings and the monotone convergence complete the estimate. $\square$

The upcrossing inequality is the criterion for convergence: a process that cannot cross an interval infinitely often must converge. Its content is quantitative, and it is the reason the convergence theorem of the next section has no hypotheses beyond the boundedness of the expectations.

## Convergence Theorems

### Almost-Sure Convergence

**Theorem (martingale convergence theorem).** Let $\{X_n\}$ be a submartingale with $\sup_n\mathbb{E}[X_n^+] < \infty$. Then $X_n$ converges a.s. to an integrable limit $X_\infty$ as $n\to\infty$.

*Proof.* Fix $a < b$ and let $U_\infty(a,b)$ be the total number of upcrossings. The upcrossing inequality gives $\mathbb{E}U_\infty(a,b) \leq \sup_n(\mathbb{E}[X_n^+] + |a|)/(b-a) < \infty$ by monotone convergence, so $U_\infty(a,b) < \infty$ a.s. The event $\{\liminf X_n < \limsup X_n\}$ is the union over rational $a < b$ of the events $\{U_\infty(a,b) = \infty\}$, hence a null set; the limit $X_\infty = \lim_n X_n$ therefore exists a.s. in $[-\infty,\infty]$. The negative parts are controlled because $\mathbb{E}X_n$ is nondecreasing, so $\sup_n\mathbb{E}|X_n| < \infty$; Fatou's lemma then gives $\mathbb{E}|X_\infty| \leq \liminf_n\mathbb{E}|X_n| \leq \sup_n\mathbb{E}|X_n| < \infty$, and $X_\infty$ is integrable. $\square$

**Corollary (the martingale case).** A martingale that is bounded in $L^1$ converges a.s. to an integrable limit. The limit need not be the $L^1$ limit, and the process need not be uniformly integrable: the multiplicative martingale $M_0 = 1$, $M_{n+1} = 2M_n$ on a head and $M_{n+1} = 0$ on a tail, with independent fair tosses, is nonnegative with $\mathbb{E}M_n = 1$ for every $n$, and $M_n \to 0$ a.s. because a tail eventually occurs, but $M_n$ does not converge to $0$ in $L^1$ since $\mathbb{E}M_n = 1$.

### $L^p$ Convergence and Uniform Integrability

**Definition.** A family $\{X_i\}$ of integrable random variables is **uniformly integrable** if

$$
\lim_{K\to\infty}\sup_i \mathbb{E}\bigl[|X_i|\mathbf{1}_{\{|X_i|>K\}}\bigr] = 0.
$$

**Theorem (uniform integrability and convergence).** Let $\{X_n\}$ be a submartingale. The following are equivalent: $\{X_n\}$ is uniformly integrable; $X_n \to X_\infty$ a.s. and in $L^1$ for some integrable $X_\infty$; and there is an integrable $X_\infty$ with $X_n = \mathbb{E}[X_\infty \mid \mathcal{F}_n]$ for every $n$. If $\sup_n\mathbb{E}|X_n|^p < \infty$ for some $p > 1$ then the process is uniformly integrable and $X_n \to X_\infty$ in $L^p$.

*Proof (sketch).* Uniform integrability gives $\sup_n\mathbb{E}|X_n| < \infty$, so $X_\infty$ exists a.s. by the convergence theorem; the uniform integrability upgrades the almost-sure convergence to $L^1$ convergence by the theorem of Vitali, and the $L^1$ convergence gives $X_n = \mathbb{E}[X_\infty\mid\mathcal{F}_n]$ by passing to the limit in the defining identity. Conversely a process closed by an integrable terminal variable is uniformly integrable by the absolute continuity of the integral. $\square$

**Theorem (Lévy's upward theorem).** For an integrable $X$ and a filtration $\{\mathcal{F}_n\}$,

$$
\mathbb{E}[X \mid \mathcal{F}_n] \longrightarrow \mathbb{E}[X \mid \mathcal{F}_\infty] \qquad \text{a.s. and in } L^1.
$$

Lévy's theorem is the convergence theorem applied to the uniformly integrable martingale $\mathbb{E}[X\mid\mathcal{F}_n]$, together with the identification of the limit as the conditional expectation on $\mathcal{F}_\infty$; the downward version, for a decreasing family of $\sigma$-algebras, is proved by the same method and gives the martingale form of the zero–one law of *Independence and Conditional Expectation*.

### Optional Stopping

**Theorem (optional stopping).** Let $\{X_n\}$ be a uniformly integrable martingale and let $\sigma \leq \tau$ be stopping times. Then $X_\sigma, X_\tau$ are integrable and

$$
\mathbb{E}[X_\tau \mid \mathcal{F}_\sigma] = X_\sigma \qquad \text{a.s.}; \qquad \text{in particular } \mathbb{E}[X_\tau] = \mathbb{E}[X_0].
$$

*Proof.* The stopped process $X^\tau$ is a uniformly integrable martingale, and by the convergence theorem it converges a.s. and in $L^1$ to $X_\tau$. Applying the martingale property at the stopping time $\sigma$ to the stopped process gives the displayed identity, the measurability of $X_\sigma$ being established by the definition of $\mathcal{F}_\sigma$. $\square$

**Corollary.** If $\{X_n\}$ is a martingale and $\tau$ is a stopping time with $\mathbb{P}(\tau \leq N) = 1$ for some finite $N$, then $\mathbb{E}[X_\tau] = \mathbb{E}[X_0]$. Consequently for a simple symmetric random walk $\{S_n\}$ and the passage times $\tau_a = \inf\{n : S_n = a\}$, $\tau_{-b} = \inf\{n : S_n = -b\}$, the **gambler's ruin** probability is

$$
\mathbb{P}(\tau_a < \tau_{-b}) = \frac{b}{a+b}, \qquad \mathbb{E}[\tau_a \wedge \tau_{-b}] = ab.
$$

The corollary is the standard application of optional stopping to the random walk: the probability of ruin is obtained from the martingale $S_n$ stopped at $\tau_a \wedge \tau_{-b}$, and the expected duration from the martingale $S_n^2 - n$. The boundedness hypothesis is essential: the simple random walk stopped at $\tau_a$ alone has $\mathbb{E}[S_{\tau_a}] = a \neq 0 = \mathbb{E}[S_0]$, and the resolution is that $\tau_a$ is unbounded and $S$ is not uniformly integrable.

## The Martingale Central Limit Theorem

**Theorem (martingale central limit theorem).** Let $\{X_n\}$ be a martingale with $X_0 = 0$ and $\mathbb{E}X_n^2 < \infty$, let $d_k = X_k - X_{k-1}$ be the differences, and let $\langle X\rangle_n = \sum_{k=1}^n\mathbb{E}[d_k^2 \mid \mathcal{F}_{k-1}]$ be the predictable quadratic variation. Suppose

$$
\frac{1}{s_n^2}\sum_{k=1}^n\mathbb{E}\bigl[d_k^2\,\mathbf{1}_{\{|d_k| > \varepsilon s_n\}} \mid \mathcal{F}_{k-1}\bigr] \longrightarrow 0 \ \text{ in probability for every } \varepsilon > 0, \qquad \frac{\langle X\rangle_n}{s_n^2} \longrightarrow 1 \ \text{ in probability},
$$

where $s_n^2 = \mathbb{E}X_n^2$. Then $X_n/s_n \xrightarrow{d} N(0,1)$.

The theorem is the martingale form of the Lindeberg–Feller theorem of *Laws of Large Numbers and the Central Limit Theorem*, with the deterministic variances replaced by the predictable quadratic variation. Its proof is the characteristic-function computation with the conditional expectation in place of the independence, and it is the discrete prototype of the stochastic integral central limit theorems. Together with the martingale maximal inequality it yields the functional version: the rescaled process $X_{\lfloor nt\rfloor}/\sqrt n$, with the time variable, converges to a Brownian motion with variance determined by the limit of the quadratic variation. That functional statement is the subject, where the continuous-time martingale theory, the Doob–Meyer decomposition and the stochastic integral are constructed.

## Applications

### Branching Processes

**Example (Galton–Watson).** Let a population start with one individual, each individual having an independent and identically distributed number of children with mean $m > 0$, and let $Z_n$ be the population at generation $n$ and $\mathcal{F}_n = \sigma(Z_0,\dots,Z_n)$. Then $M_n = Z_n/m^n$ is a martingale, since $\mathbb{E}[Z_{n+1}\mid\mathcal{F}_n] = mZ_n$; it is nonnegative, so it converges a.s. to a limit $M_\infty \geq 0$ by the martingale convergence theorem. The limit is zero on the extinction event and positive on the survival event, and the extinction probability is the smallest fixed point of the generating function in $[0,1]$; the finite-mean case is thus decided by the martingale convergence theorem, and the branching process is the classical example of a nonnegative martingale whose limit is not constant.

### Radon–Nikodym Derivatives and the Kakutani Theorem

**Example (the density is a martingale).** For $\mathbb{Q} \ll \mathbb{P}$ with density $Z$ on $\mathcal{F}_\infty$, the likelihood ratio process $Z_n = \mathbb{E}[Z\mid\mathcal{F}_n]$ is a uniformly integrable martingale by Lévy's theorem, converging a.s. and in $L^1$ to $Z$. The setting is the abstract form of the sequential likelihood ratio, and the failure of uniform integrability is exactly the event that $\mathbb{Q}$ is singular on $\mathcal{F}_\infty$: if $Z_n \to 0$ a.s. then $\mathbb{Q}$ and $\mathbb{P}$ are mutually singular. Kakutani's theorem applies this to product measures: for two product measures on a sequence space the densities form a martingale, and the two measures are equivalent exactly when the Hellinger products do not diverge, and mutually singular otherwise.

### The Strong Law for Martingales

**Theorem (strong law for martingales).** Let $\{X_n\}$ be a martingale and let $\{b_n\}$ be a positive increasing sequence with $b_n \to \infty$ and

$$
\sum_{n\geq1} \frac{\mathbb{E}\bigl[(X_n - X_{n-1})^2\bigr]}{b_n^2} < \infty.
$$

Then $X_n/b_n \to 0$ a.s.

The theorem is the martingale form of the strong law of large numbers, and it recovers the classical result by taking $X_n = S_n - n\mu$ and $b_n = n$ in the independent case, in which the series is $\sigma^2\sum_n n^{-2} < \infty$; the summability hypothesis replaces the identical distribution. The proof combines the convergence theorem applied to the martingale $X_n/b_n$ with a summation by parts (the Kronecker lemma), and it is the reason the strong law holds under hypotheses far weaker than independence.

## Summary

A martingale is an adapted integrable process whose conditional expectation one step ahead is its present value; a submartingale has nonnegative drift and a supermartingale nonpositive drift. The fundamental examples are the partial sums of independent mean-zero variables, the conditional expectations $\mathbb{E}[X\mid\mathcal{F}_n]$, the likelihood ratio process of an absolutely continuous change of measure, and the martingale transform of a martingale by a bounded predictable integrand; convex functions of a martingale are submartingales by Jensen, and every submartingale is the sum of a martingale and a predictable increasing compensator by the Doob decomposition.

A stopping time is a stopping rule that uses only the information available at the time, and the $\sigma$-algebra $\mathcal{F}_\tau$ collects the events decidable by then. Doob's maximal inequality bounds the distribution of the running maximum by the expectation of the terminal value, and its $L^p$ form bounds the $L^p$ norm of the running maximum by $p/(p-1)$ times the terminal norm; the upcrossing inequality bounds the expected number of crossings of an interval by the expectation of the terminal positive part, and it is the engine of the martingale convergence theorem: a submartingale with bounded positive part converges almost surely to an integrable limit. The convergence is in $L^1$ and in $L^p$ exactly when the process is uniformly integrable, or when it is closed by a terminal variable; Lévy's theorem identifies the limit of $\mathbb{E}[X\mid\mathcal{F}_n]$ as $\mathbb{E}[X\mid\mathcal{F}_\infty]$, and the optional stopping theorem states that a uniformly integrable martingale sampled at stopping times preserves its conditional expectations, with the gambler's ruin formulas as the classical application. The martingale central limit theorem replaces the deterministic variances of the classical theorem by the predictable quadratic variation and leads to the functional limit theorem and the Brownian motion; the applications to branching processes, to the Radon–Nikodym derivatives and to the strong law complete the discrete theory.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\{\mathcal{F}_n\}$, $\mathcal{F}_\infty$ | Filtration and its limit $\sigma$-algebra |
| $X_n$, $d_n = X_n - X_{n-1}$ | Adapted process and its differences |
| martingale, submartingale, supermartingale | $\mathbb{E}[X_{n+1}\mid\mathcal{F}_n]$ equals, is at least, is at most $X_n$ a.s. |
| $H\cdot X$ | Martingale transform $\sum_k H_k(X_k - X_{k-1})$ |
| $\tau$, $\mathcal{F}_\tau$ | Stopping time and the $\sigma$-algebra at $\tau$ |
| $X^\tau = X_{n\wedge\tau}$ | Stopped process |
| $X_n^* = \max_{k\le n}X_k$ | Running maximum |
| $U_n(a,b)$ | Number of upcrossings of $[a,b]$ |
| Doob decomposition | $X = M + A$, $M$ martingale, $A$ predictable increasing |
| uniformly integrable | $\sup_i\mathbb{E}[\|X_i\|\mathbf{1}_{\{\|X_i\|>K\}}]\to0$ |
| $\langle X\rangle_n$ | Predictable quadratic variation $\sum_k\mathbb{E}[d_k^2\mid\mathcal{F}_{k-1}]$ |
| Lévy's theorem | $\mathbb{E}[X\mid\mathcal{F}_n]\to\mathbb{E}[X\mid\mathcal{F}_\infty]$ a.s. and in $L^1$ |
| optional stopping | $\mathbb{E}[X_\tau\mid\mathcal{F}_\sigma]=X_\sigma$ for UI martingales, $\sigma\le\tau$ |
| Galton–Watson | branching process martingale $Z_n/m^n$ |



## Further Reading

- Joseph L. Doob, *Stochastic Processes* (Wiley, 1953), for the original systematic development of the martingale theory, the maximal inequalities and the convergence theorems.
- J. L. Doob, "Regularity properties of certain families of chance variables", *Transactions of the American Mathematical Society* 47 (1940), 455–486, for the upcrossing argument and the convergence theorem.
- David Williams, *Probability with Martingales* (Cambridge University Press, 1991), for a concise and complete treatment of discrete-time martingales and optional stopping.
- Patrick Billingsley, *Probability and Measure* (Wiley, 3rd edition, 1995), for the martingale theory set in the measure-theoretic framework, and *Convergence of Probability Measures* (Wiley, 2nd edition, 1999), for the martingale central limit theorem.
- Kai Lai Chung, *A Course in Probability Theory* (Academic Press, 3rd edition, 2001), for the martingale law of large numbers and its applications.
- Paul-André Meyer, *Probability and Potentials* (Blaisdell, 1966), for the Doob–Meyer decomposition and the general theory of processes that the continuous-time theory requires.
- Olav Kallenberg, *Foundations of Modern Probability* (Springer, 2nd edition, 2002), for a comprehensive account including uniform integrability, the optional stopping theorem and the applications to branching processes.
