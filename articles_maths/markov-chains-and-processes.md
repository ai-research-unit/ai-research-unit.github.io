
# __Markov Chains and Processes__

## Introduction

A Markov process is a stochastic process whose future is independent of its past given its present. The state of the process at time $n$ is the only information relevant to the distribution of its subsequent trajectory, and the whole theory follows from that one hypothesis. The class is broad enough to contain the random walk, the Poisson process, the branching process, the diffusions and the solutions of stochastic differential equations, and narrow enough that the analysis is explicit: the transition operator, the stationary distribution, the generator and the spectral gap are computable objects, and the asymptotic behaviour of the process is read from them.

This article develops the theory in two stages. In discrete time it defines the Markov chain, the transition matrix and the Markov operator, classifies the states by recurrence and period, proves the existence and uniqueness of the stationary distribution for an irreducible positive recurrent chain, proves the ergodic theorem and the convergence to stationarity, and connects the rate to the spectral gap and, in the reversible case, to the eigenvalues of a symmetric operator. In continuous time it defines the transition semigroup and the generator, derives the Kolmogorov equations, treats the Poisson process and the birth–death chain as the basic examples, and states the Hille–Yosida and martingale-problem characterisations that make the passage to the diffusion theory possible.

The place of the article is fixed by four boundaries.

- The **probability frame** is *Measure-Theoretic Probability*, the **conditional expectation, the independence and the Borel–Cantelli and zero–one laws** are *Independence and Conditional Expectation*, the **law of large numbers and the central limit theorem** are *Laws of Large Numbers and the Central Limit Theorem*, and the **martingale theory** — the convergence theorem, the optional stopping theorem and the maximal inequality — is *Martingales*; all four are used here, and the martingale convergence theorem is the tool for the recurrence and the convergence of the bounded harmonic functions.
- The **Brownian motion and the stochastic calculus** — the construction of Brownian motion, the Itô integral, the diffusion processes and the Feller theory of one-dimensional diffusions — . Brownian motion is a Markov process, and its semigroup is the heat semigroup introduced here as an example; the construction and the calculus lie outside this article.
- The **ergodic theory** — the pointwise ergodic theorem for a measure-preserving transformation, the notion of ergodicity, mixing and the invariant measure — isand *Ergodic Theory of Group Actions*; the ergodic theorem for a Markov chain with an invariant distribution is the special case of the general theorem applied to the shift on the path space, and the ergodic theory of a group action is the framework for the random walk on a group. The present article proves the chain version directly and cites the general theorem.
- The **algebraic theory of the random walk on a group** — the convolution powers of the step distribution, the Fourier and spectral computation of the return probabilities, the mixing of a walk on a finite or compact group and the Diaconis–Shahshahani bound — iswith the compact-group transform of *Analysis on Compact Groups* and *The Peter–Weyl Theorem*; the results are cited and not re-derived. The **mixing times** of a finite chain and the concentration of a reversible chain are quoted from the standard theory. No physics is invoked.

Throughout, $E$ is a **state space** — countable with the discrete $\sigma$-algebra in the discrete theory, a Polish space with its Borel $\sigma$-algebra in the general theory — and $\{X_n\}_{n\geq0}$ is a sequence of $E$-valued random variables on a probability space $(\Omega,\mathcal{F},\mathbb{P})$. The **transition kernel** is written $p(x,B) = \mathbb{P}(X_{n+1}\in B \mid X_n = x)$, the **transition matrix** $P = (p_{xy})$ in the countable case, the **$n$-step transition** $p^{(n)}(x,B)$ or $p_{xy}^{(n)}$, and the **Markov operator** acts on functions by $Pf(x) = \int_E f(y)\,p(x,dy)$; the notation $\mathbb{E}_x$ and $\mathbb{P}_x$ marks the law of the chain started at $x$, so that $\mathbb{E}_x[f(X_n)] = P^nf(x)$, and $\mathbb{E}_\mu$ marks the law with initial distribution $\mu$.

## Markov Chains: Definitions and the Markov Property

### The Markov Property

**Definition.** A sequence $\{X_n\}$ of random variables with values in a countable state space $E$ is a **Markov chain** with transition matrix $P = (p_{xy})$ if the **Markov property** holds: for every $n$ and every $B \subseteq E$,

$$
\mathbb{P}(X_{n+1} \in B \mid X_0, X_1, \dots, X_n) = \mathbb{P}(X_{n+1} \in B \mid X_n) = p(X_n, B) \qquad \text{a.s.}
$$

More generally, on a state space with a $\sigma$-algebra, a **Markov kernel** is a map $p : E\times\mathcal{E}\to[0,1]$ with $p(x,\cdot)$ a probability measure for each $x$ and $p(\cdot,B)$ measurable for each $B$, and a Markov chain is defined by the same conditional identity with $p$ in place of the matrix.

The Markov property is the statement that the past and the future are conditionally independent given the present. It is a statement about a single step, but it propagates: iterating it shows that the conditional law of the whole future $(X_{n+1},X_{n+2},\dots)$ given $(X_0,\dots,X_n)$ depends only on $X_n$, and this **strong Markov property** is what makes the theory work at stopping times.

**Theorem (Chapman–Kolmogorov).** The $m+n$ step transitions are the compositions

$$
p^{(m+n)}(x,B) = \int_E p^{(m)}(x,dy)\,p^{(n)}(y,B), \qquad P^{m+n} = P^mP^n \text{ in the countable case}.
$$

*Proof.* Condition on $X_m$ and apply the Markov property to the last $n$ steps:
$\mathbb{P}_x(X_{m+n}\in B) = \sum_y \mathbb{P}_x(X_m=y)\mathbb{P}(X_{m+n}\in B\mid X_m=y) = \sum_y p^{(m)}(x,y)p^{(n)}(y,B)$. $\square$

**Theorem (strong Markov property).** Let $\tau$ be a stopping time for the natural filtration of the chain. Then conditionally on $\{\tau < \infty\}$ and $X_\tau = x$, the post-$\tau$ process $(X_{\tau+n})_{n\geq0}$ is a Markov chain with transition matrix $P$ started at $x$, and it is conditionally independent of $\mathcal{F}_\tau$ given $X_\tau$.

The strong Markov property is the extension of the Markov property to random times, and it is the reason the theory of passage times works: the law of the chain after the first visit to a set is the law of a fresh chain started there, independent of the history. The proof is a direct computation on the events $\{\tau = n\}$, using the ordinary Markov property at each $n$.

### The Markov Operator and Harmonic Functions

**Definition.** The **Markov operator** $P$ acts on bounded measurable functions by $Pf(x) = \int_E f(y)\,p(x,dy) = \mathbb{E}_x[f(X_1)]$ and on finite measures by $\mu P(B) = \int_E \mu(dx)p(x,B)$; it is positive and preserves constants. A bounded function $h$ is **harmonic** for $P$ if $Ph = h$, and **superharmonic** if $Ph \leq h$.

**Theorem.** Let $h$ be bounded and harmonic for a Markov chain and let $\mathcal{F}_n = \sigma(X_0,\dots,X_n)$. Then $\{h(X_n)\}$ is a martingale.

*Proof.* By the Markov property, $\mathbb{E}[h(X_{n+1})\mid\mathcal{F}_n] = \mathbb{E}_{X_n}[h(X_1)] = Ph(X_n) = h(X_n)$. $\square$

The theorem is the bridge between the Markov and martingale theories: harmonic functions produce martingales, the martingale convergence theorem controls their limits, and the identity $Ph = h$ is the discrete maximum principle. The classical application is the uniqueness of the bounded harmonic functions on a recurrent class — the boundary theory of the chain — and the same correspondence appears in the harmonic functions of a group and the random walks.

## Classification of States

### Communication and Irreducibility

**Definition.** For states $x, y \in E$ write $x \to y$ if $p^{(n)}(x,y) > 0$ for some $n \geq 0$ — one says $y$ is **reachable** from $x$ — and $x \leftrightarrow y$ if $x\to y$ and $y \to x$. The relation $\leftrightarrow$ is an equivalence relation on $E$, its classes are the **communicating classes**, and the chain (or the state $x$) is **irreducible** if there is one class.

**Definition.** The **period** of a state $x$ is $d(x) = \gcd\{n \geq 1 : p^{(n)}(x,x) > 0\}$; a state with $d(x) = 1$ is **aperiodic**. Period is a class property: communicating states have the same period, so one speaks of the period of an irreducible class. An irreducible class with period $d$ decomposes into $d$ cyclic subclasses cycled by the transition matrix.

### Recurrence and Transience

**Definition.** For a state $x$ let $\tau_x^+ = \inf\{n \geq 1 : X_n = x\}$ be the first return time. The state $x$ is **recurrent** if $\mathbb{P}_x(\tau_x^+ < \infty) = 1$ and **transient** if $\mathbb{P}_x(\tau_x^+ < \infty) < 1$; it is **positive recurrent** if additionally $\mathbb{E}_x[\tau_x^+] < \infty$, and **null recurrent** if it is recurrent with $\mathbb{E}_x[\tau_x^+] = \infty$. Let $N_x = \sum_{n\geq0}\mathbf{1}_{\{X_n = x\}}$ be the number of visits to $x$.

**Theorem (recurrence criterion).** A state $x$ is recurrent if and only if $\sum_{n\geq0}p^{(n)}(x,x) = \infty$; it is transient if and only if the series converges, in which case $N_x < \infty$ a.s. and $\mathbb{E}_x[N_x] = 1/(1 - \mathbb{P}_x(\tau_x^+ < \infty))$.

*Proof.* Decompose the expected number of visits into the sum of the probabilities of return, and use the strong Markov property at the successive return times: the number of visits is a geometric random variable with success probability $1 - \mathbb{P}_x(\tau_x^+<\infty) < 1$ in the transient case. In the recurrent case the expectation diverges. $\square$

The criterion is the standard test for recurrence, and it is the form in which the recurrence of the simple random walk on $\mathbb{Z}^d$ is decided: the return probabilities are of order $n^{-d/2}$, whose sum diverges for $d \leq 2$ and converges for $d \geq 3$, which is Pólya's theorem.

**Theorem (Pólya).** The simple symmetric random walk on $\mathbb{Z}^d$ is recurrent for $d = 1, 2$ and transient for $d \geq 3$.

The example is the classical illustration of the dimension dependence of recurrence, and it parallels the classification of Brownian motion — point recurrent in dimension one, neighbourhood recurrent but not point recurrent in dimension two, transient in dimension at least three — which is the reason the random walk on a group is treated as a geometric object.

## Stationary Distributions and the Ergodic Theorem

### Stationary Distributions

**Definition.** A probability measure $\pi$ on $E$ is **stationary** (or invariant) for the chain if $\pi P = \pi$, that is $\sum_x \pi(x)p(x,y) = \pi(y)$ for every $y$ in the countable case. A chain with initial distribution $\pi$ is then a stationary process: the law of $(X_n,X_{n+1},\dots)$ does not depend on $n$.

**Theorem (existence and uniqueness).** Let the chain be irreducible and positive recurrent. Then there is a unique stationary distribution $\pi$, and it is given by

$$
\pi(x) = \frac{1}{\mathbb{E}_x[\tau_x^+]},
$$

so that positive recurrence is exactly the existence of a stationary distribution for an irreducible chain. An irreducible chain that is null recurrent or transient has no stationary probability measure.

The theorem is the ergodic statement of the classification: the chain admits an equilibrium measure exactly when the mean return time is finite. For a finite chain irreducibility alone suffices, since every state is positive recurrent, and the stationary distribution is then the Perron–Frobenius eigenvector of the stochastic matrix $P$ for the eigenvalue $1$: the theorem of Perron and Frobenius states that a nonnegative irreducible matrix has a simple positive eigenvalue equal to its spectral radius, with positive left and right eigenvectors, and $P$ is a nonnegative matrix with spectral radius $1$.

**Theorem (ergodic theorem for Markov chains).** Let the chain be irreducible positive recurrent with stationary distribution $\pi$ and let $f$ be integrable with respect to $\pi$. Then for every initial distribution,

$$
\frac{1}{n}\sum_{k=0}^{n-1}f(X_k) \longrightarrow \int_E f\,d\pi \qquad \text{a.s.}
$$

*Proof (sketch).* The argument is the regenerative decomposition at the successive visits to a fixed state $x$: the chain decomposes into independent and identically distributed **excursions** away from $x$, by the strong Markov property, and the empirical average over an excursion converges by the law of large numbers of *Laws of Large Numbers and the Central Limit Theorem*. The ratio of the excursion sums to the excursion lengths gives the identity $\int f\,d\pi = \mathbb{E}_x\bigl[\sum_{k<\tau_x^+}f(X_k)\bigr]/\mathbb{E}_x[\tau_x^+]$. The full statement is the special case of the pointwise ergodic theorem, applied to the shift on the canonical path space with the invariant measure $\pi$. $\square$

The formula $\int f\,d\pi = \mathbb{E}_x[\sum_{k<\tau_x^+}f(X_k)]/\mathbb{E}_x[\tau_x^+]$ is the **Kac formula**, and it is the bridge between the Markov classification and the ergodic theory: the stationary measure is the expected occupation measure of an excursion normalised by its expected duration.

### Convergence to Stationarity

**Theorem (convergence theorem).** Let the chain be irreducible, aperiodic and positive recurrent with stationary distribution $\pi$. Then for every initial distribution $\mu$,

$$
\| \mu P^n - \pi \|_{\mathrm{TV}} \longrightarrow 0,
$$

where $\|\cdot\|_{\mathrm{TV}}$ is the total variation norm; and if the chain is periodic with period $d$, the convergence holds along each residue class modulo $d$ with the appropriate limiting measure.

*Proof (sketch).* The argument is coupling: two copies of the chain are run independently until they meet, and after the meeting they are glued; the coupling inequality bounds the total variation distance by the probability that the two copies have not met by time $n$, which tends to $0$ for an irreducible aperiodic positive recurrent chain. $\square$

The convergence theorem is the Markov-chain form of mixing, and it is the reason the Markov chain Monte Carlo method works. The rate is governed by the **spectral gap**.

**Theorem (spectral gap and mixing).** Let the chain be finite, irreducible and aperiodic with transition matrix $P$ and stationary distribution $\pi$, and let $1 = \lambda_1 > |\lambda_2| \geq \cdots$ be the eigenvalues of $P$ (as an operator on $L^2(\pi)$). Then the second eigenvalue satisfies $|\lambda_2| < 1$ and

$$
\|\mu P^n - \pi\|_{\mathrm{TV}} \leq \frac{1}{2}\left(\frac{\mu(x)}{\pi(x)}\right)_{\max}^{1/2} |\lambda_2|^n,
$$

so the chain mixes at a geometric rate determined by the spectral gap $1 - |\lambda_2|$.

**Definition.** The chain is **reversible** with respect to $\pi$ if the **detailed balance** equations hold:

$$
\pi(x)p(x,y) = \pi(y)p(y,x) \qquad \text{for all } x,y,
$$

in which case $\pi$ is stationary automatically. A reversible chain is self-adjoint on $L^2(\pi)$, so its eigenvalues are real, and the spectral gap is the Poincaré constant of the Dirichlet form

$$
\mathcal{E}(f,f) = \frac{1}{2}\sum_{x,y}\pi(x)p(x,y)\bigl(f(x)-f(y)\bigr)^2, \qquad \mathrm{Gap} = \inf_{f \perp 1}\frac{\mathcal{E}(f,f)}{\|f\|_{L^2(\pi)}^2}.
$$

The Dirichlet form is the discrete analogue of the energy form of a diffusion, and the variational formula for the gap is the discrete Poincaré inequality. The whole apparatus is the finite-state model of the spectral theory of the heat semigroup and of the Laplace operator on a group in *Analysis on Compact Groups*.

## General State Spaces and Continuous Time

### Kernels and the General Markov Property

**Definition.** A Markov kernel $p$ on a Polish space $E$ and a probability measure $\mu$ on $E$ determine a probability measure $\mathbb{P}_\mu$ on $E^{\mathbb{N}}$ — the **canonical chain** — by the Ionescu Tulcea theorem, such that the coordinate process is a Markov chain with kernel $p$ and initial law $\mu$; the measure is the unique one with the prescribed finite-dimensional marginals. A kernel $p$ is **Feller** if $Pf$ is continuous and bounded whenever $f$ is continuous and bounded.

The construction of the canonical chain is the measurable counterpart of the Kolmogorov extension theorem of *Independence and Conditional Expectation*, with the conditional distributions supplied by the kernel; the Ionescu Tulcea theorem is the version for dependent sequences, and it makes the Markov chain an object of measure theory rather than a heuristic. The Feller property is the regularity hypothesis under which the semigroup theory of the next subsection applies, and it is automatic for the transition kernels of a random walk on a topological group.

### Transition Semigroups and Generators

**Definition.** A **transition semigroup** on a measurable space $E$ is a family $\{P_t\}_{t\geq0}$ of Markov kernels with $P_0 = I$ and $P_{s+t} = P_sP_t$. Under appropriate regularity it is a **Feller semigroup** when each $P_t$ maps $C_0(E)$ into itself and $P_tf \to f$ uniformly for $f \in C_0(E)$ as $t\to0$. The **generator** is the operator

$$
Lf = \lim_{t\to0}\frac{P_tf - f}{t},
$$

defined on the domain of functions for which the limit exists uniformly.

**Theorem (Hille–Yosida).** A linear operator $L$ on $C_0(E)$ is the generator of a Feller semigroup if and only if its domain is dense, $L$ is dissipative and the range of $\lambda - L$ is dense for some (equivalently every) $\lambda > 0$.

The Hille–Yosida theorem is the functional-analytic characterisation of the generators of Markov semigroups, and it is the bridge from the probabilistic to the analytic description of a Markov process. The semigroup is the collection of transition probabilities; the generator is the local description of the motion; and the resolvent $(\lambda - L)^{-1}$ is the Laplace transform of the semigroup, $(\lambda-L)^{-1}f(x) = \int_0^\infty e^{-\lambda t}P_tf(x)\,dt$.

### Continuous-Time Markov Chains and the Poisson Process

**Definition.** A **continuous-time Markov chain** on a countable state space is a family $\{X_t\}_{t\geq0}$ with the Markov property in continuous time and transition probabilities $p_t(x,y)$; the **$Q$-matrix** or **generator** has entries $q_{xy} = \lim_{t\to0}(p_t(x,y) - \delta_{xy})/t$ and satisfies $q_{xy} \geq 0$ for $x \neq y$ and $\sum_y q_{xy} = 0$.

**Theorem (Kolmogorov equations).** For a continuous-time Markov chain with generator $Q$, the transition probabilities satisfy the **backward equation** $\partial_t p_t = Qp_t$ and, when the chain is non-explosive, the **forward equation** $\partial_tp_t = p_tQ$; for a finite state space both reduce to $P_t = e^{tQ}$.

**Example (the Poisson process).** Let $X_t$ be the number of arrivals by time $t$ with rate $\lambda > 0$: the increments are independent, stationary, with $X_{t+s} - X_s \sim \mathrm{Pois}(\lambda t)$. The Poisson process is the continuous-time Markov chain with $q_{n,n+1} = \lambda$ and $q_{n,n} = -\lambda$, its holding times are independent exponentials of rate $\lambda$, and its generator is the difference operator $(Lf)(n) = \lambda(f(n+1)-f(n))$. The Poisson process is the prototypical point process, and it is the building block of the jump processes and of the Itô integral with respect to a Poisson random measure.

**Example (birth–death chains).** A birth–death chain has $q_{n,n+1} = b_n$, $q_{n,n-1} = a_n$, with the other off-diagonal entries zero; the simple random walk on $\mathbb{Z}$ is the case $a_n = b_n = 1/2$ after normalising the time, and the recurrence classification is the same as in discrete time. The stationary distribution, when it exists, has $\pi(n) = \pi(0)\prod_{k<n}b_k/a_{k+1}$, and the product converges exactly in the positive recurrent case.

### The Martingale Problem

**Theorem (Stroock–Varadhan).** Let $L$ be the generator of a Feller semigroup on a Polish space $E$ and let $\mu$ be an initial law. There exists a unique probability measure on the path space under which the coordinate process has initial law $\mu$ and, for every $f$ in the domain of $L$, $f(X_t) - f(X_0) - \int_0^t Lf(X_s)\,ds$ is a martingale.

The martingale problem is the coordinate-free characterisation of the law of a Markov process, and it is the formulation in which the existence and uniqueness of the diffusions associated with a second-order operator are proved; the corresponding stochastic integral representation is the content of the stochastic calculus. The discrete analogue of the martingale problem is the statement of *Martingales* that $h(X_n)$ is a martingale for harmonic $h$, and the parallel is exact: the generator is the operator whose harmonic functions produce the martingales of the process.

## Summary

A Markov chain is a sequence whose future is conditionally independent of its past given its present, so that the one-step transition kernel, iterated by the Chapman–Kolmogorov equations, determines the whole law; the strong Markov property extends the same statement to stopping times. The Markov operator acts on functions by $Pf(x)=\mathbb{E}_x[f(X_1)]$, and a bounded harmonic function produces a martingale, which is the link with *Martingales*. The communicating classes and the period organise the state space, and a state is recurrent exactly when the sum of its return probabilities diverges; the simple symmetric random walk is recurrent in dimensions one and two and transient in dimension at least three by Pólya's theorem.

An irreducible chain has a stationary distribution exactly when it is positive recurrent, the stationary masses being the reciprocals of the mean return times, and for a finite chain the stationary distribution is the Perron–Frobenius eigenvector of the transition matrix for the eigenvalue one. The ergodic theorem states that the empirical occupation measure converges to the stationary distribution, and it is the Markov case of the pointwise ergodic theorem; the Kac formula identifies the stationary measure with the normalised expected occupation measure of an excursion. An irreducible aperiodic positive recurrent chain converges to stationarity in total variation, the rate being governed by the spectral gap, and a reversible chain is self-adjoint on $L^2(\pi)$ with the gap given by the Poincaré inequality for the Dirichlet form.

On a general state space the chain is built from a Markov kernel by the Ionescu Tulcea theorem, the Feller property makes the semigroup theory available, and the Hille–Yosida theorem characterises the generators of Feller semigroups; the generator is the local description of the motion, the resolvent is the Laplace transform of the semigroup, and the martingale problem of Stroock and Varadhan characterises the law of the process by its generator. The Kolmogorov forward and backward equations describe the continuous-time chains, with the Poisson process as the basic jump process and the birth–death chain as the basic one-dimensional example; the Feller semigroups and the martingale problem are the point of departure.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $E$, $\{X_n\}$, $\{X_t\}$ | State space and discrete- or continuous-time process |
| $p(x,B)$, $P=(p_{xy})$ | Transition kernel, transition matrix |
| $p^{(n)}$, $P^n$ | $n$-step transition, Chapman–Kolmogorov $P^{m+n}=P^mP^n$ |
| $Pf(x)=\int f\,dp(x,\cdot)$ | Markov operator |
| $\mathbb{P}_x$, $\mathbb{E}_x$, $\mathbb{P}_\mu$ | Law and expectation started at $x$ or with initial law $\mu$ |
| $\tau_x^+$ | First return time to $x$ |
| recurrent, transient, positive/null recurrent | $\mathbb{P}_x(\tau_x^+<\infty)=1$; $<1$; $\mathbb{E}_x\tau_x^+<\infty$ or $=\infty$ |
| period $d(x)$ | $\gcd\{n\ge1 : p^{(n)}(x,x)>0\}$ |
| stationary $\pi$ | $\pi P=\pi$; $\pi(x)=1/\mathbb{E}_x[\tau_x^+]$ in the irreducible positive recurrent case |
| reversible, detailed balance | $\pi(x)p(x,y)=\pi(y)p(y,x)$ |
| spectral gap, Dirichlet form | $1-\|\lambda_2\|$; $\mathcal{E}(f,f)=\frac12\sum\pi(x)p(x,y)(f(x)-f(y))^2$ |
| $P_t$, $L$, $q_{xy}$ | Transition semigroup, generator, $Q$-matrix |
| Hille–Yosida | characterisation of Feller generators |
| martingale problem | $f(X_t)-f(X_0)-\int_0^tLf(X_s)ds$ is a martingale |





## Further Reading

- J. R. Norris, *Markov Chains* (Cambridge University Press, 1997), for the discrete and continuous-time chains, recurrence, stationarity and the convergence theorems.
- David A. Levin, Yuval Peres and Elizabeth L. Wilmer, *Markov Chains and Mixing Times* (AMS, 2nd edition, 2017), for the convergence to stationarity, the spectral gap, coupling and the Dirichlet form.
- Kai Lai Chung, *Markov Chains with Stationary Transition Probabilities* (Springer, 2nd edition, 1967), for the classical account of recurrence, stationarity and the ergodic theorem for chains.
- Daniel W. Stroock, *An Introduction to Markov Processes* (Springer, 2nd edition, 2014), for the Feller semigroups, the generator and the martingale problem.
- Stewart N. Ethier and Thomas G. Kurtz, *Markov Processes: Characterization and Convergence* (Wiley, 1986), for the Hille–Yosida theorem, the martingale problem and the convergence of Markov processes.
- Andrey N. Kolmogorov, "Über die analytischen Methoden in der Wahrscheinlichkeitsrechnung", *Mathematische Annalen* 104 (1931), 415–458, for the forward and backward equations.
- George Pólya, "Über eine Aufgabe der Wahrscheinlichkeitsrechnung betreffend die Irrfahrt im Straßennetz", *Mathematische Annalen* 84 (1921), 149–160, for the recurrence and transience of the simple random walk.
- David Aldous and James Fill, *Reversible Markov Chains and Random Walks on Graphs* (available from the authors, 2002), for the reversible theory, the Dirichlet form and the spectral gap.
