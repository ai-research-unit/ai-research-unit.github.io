
# __List of Probability Distributions and Processes__

## Introduction

This article lists the probability distributions and the stochastic processes the corpus introduces. A probability distribution is a law on a measurable space, and a process is a family of random variables whose finite-dimensional laws are distributions; a row below names one, records its law, its moments and the convergence theorem attached to it, and points to the article that introduces it. Every row points to an article; this article introduces nothing and proves nothing. The objects are grouped by the layer that introduces them: the discrete distributions, the absolutely continuous and singular distributions, the general theory of laws and their characteristic functions, the processes built on the distributions, and the limit theorems that govern them. The rows that record a failure — a distribution with no mean, a limit theorem that needs a hypothesis it does not have, a stationary process that is not ergodic — stand beside them as non-examples.

## The Discrete Distributions

| Object | Its law, moments and characteristic function | Introduced in |
|---|---|---|
| the Bernoulli distribution $\mathrm{Bern}(p)$ | $p\delta_1+(1-p)\delta_0$ on $\{0,1\}$; mean $p$, variance $p(1-p)$; $\varphi(t)=1-p+pe^{it}$ | *Measure-Theoretic Probability* |
| the binomial distribution $\mathrm{Bin}(n,p)$ | $\sum_k\binom nk p^k(1-p)^{n-k}\delta_k$; mean $np$, variance $np(1-p)$; the sum of $n$ independent Bernoulli laws | *Measure-Theoretic Probability* |
| the Poisson distribution $\mathrm{Pois}(\lambda)$ | $e^{-\lambda}\sum_k\lambda^k\delta_k/k!$ on $\mathbb Z_{\geq0}$; mean and variance $\lambda$; $\varphi(t)=e^{\lambda(e^{it}-1)}$ | *Measure-Theoretic Probability* |
| the point mass $\delta_x$ | the law of the constant random variable; mean $x$, variance $0$; a degenerate distribution | *Measure-Theoretic Probability* |
| the uniform law on a finite set | equal mass on each point; the counting measure normalised | *Measure-Theoretic Probability* |

## The Absolutely Continuous and Singular Distributions

| Object | Its density, moments and characteristic function | Introduced in |
|---|---|---|
| the uniform distribution on $[0,1]$ | density $\mathbf 1_{[0,1]}$; mean $1/2$, variance $1/12$; the universal law of the quantile construction | *Measure-Theoretic Probability* |
| the normal distribution $N(\mu,\sigma^2)$ | density $(2\pi\sigma^2)^{-1/2}e^{-(x-\mu)^2/(2\sigma^2)}$; mean $\mu$, variance $\sigma^2$; $\varphi(t)=e^{i\mu t-\sigma^2t^2/2}$ | *Measure-Theoretic Probability*; *Laws of Large Numbers and the Central Limit Theorem* |
| the standard normal $N(0,1)$ | the limit law of the central limit theorem; all moments finite, the cumulants vanishing above the second | *Laws of Large Numbers and the Central Limit Theorem* |
| the Cauchy distribution | density $1/(\pi(1+x^2))$; no mean and no variance; $\varphi(t)=e^{-\lvert t\rvert}$ | *Measure-Theoretic Probability*; *Laws of Large Numbers and the Central Limit Theorem* |
| the Cantor distribution | singular continuous, supported on the Cantor set; distribution function the Cantor function; no density | *Measure-Theoretic Probability* |
| the stable and infinitely divisible laws | the class closed under convolution and scaling; their characteristic functions given by the Lévy–Khintchine representation | *Laws of Large Numbers and the Central Limit Theorem* |
| the Gaussian measure on a Banach space | the cylinder measure of a Gaussian process; its characteristic function is $e^{-\lVert x\rVert^2/2}$ | *Stochastic Partial Differential Equations* |
| the Wiener measure | the law of Brownian motion on the space of continuous paths | *Brownian Motion and Stochastic Calculus* |
| the equilibrium and harmonic measures | the distribution of the exit point of a Brownian path from a domain | *Potential Theory*; *Brownian Motion and Stochastic Calculus* |

## The Theory of Laws and Their Transforms

| Object | What it carries | Introduced in |
|---|---|---|
| the distribution function $F_X(x)=\mathbb P(X\leq x)$ | a right-continuous nondecreasing function determining the law | *Measure-Theoretic Probability* |
| the law $\mu_X=\mathbb P\circ X^{-1}$ | the pushforward of the probability measure; a probability measure on the range | *Measure-Theoretic Probability* |
| the Lebesgue decomposition of a law | the split into an absolutely continuous, a discrete and a singular continuous part | *Measure-Theoretic Probability* |
| the quantile function $F^{-1}$ and the Skorokhod representation | every law on $\mathbb R$ is $F^{-1}(U)$ for $U$ uniform, so $[0,1]$ is universal | *Measure-Theoretic Probability* |
| the expectation, variance and covariance | the moments as integrals, with the monotone and dominated convergence theorems | *Measure-Theoretic Probability* |
| the characteristic function $\varphi_X(t)=\mathbb E[e^{itX}]$ | the Fourier transform of the law; it determines the law and inverts it | *Measure-Theoretic Probability*; *Laws of Large Numbers and the Central Limit Theorem* |
| the moment generating function and the cumulants | the exponential moments where they exist, and the cumulant expansion | *Measure-Theoretic Probability* |
| the Lévy–Khintchine representation | the characteristic function of an infinitely divisible law as an exponential of a Lévy measure | *Laws of Large Numbers and the Central Limit Theorem* |
| the Markov operator and the transition kernel | the action of a Markov chain on functions and on measures | *Markov Chains and Processes* |

## The Processes

| Object | Its definition, and the theorem attached to it | Introduced in |
|---|---|---|
| a sequence of independent random variables | the product law; the setting of the law of large numbers and the central limit theorem | *Measure-Theoretic Probability* |
| the simple random walk | the sum of independent Bernoulli steps; recurrent in dimension one and two, transient from three | *Markov Chains and Processes*; *Random Walks on Groups* |
| a Markov chain | the Markov property and the transition operator; recurrence, transience and the ergodic theorem | *Markov Chains and Processes* |
| a Markov process in continuous time and its semigroup | the transition semigroup and its generator; the martingale problem | *Markov Chains and Processes* |
| the Poisson process | the counting process with independent stationary increments of Poisson law; its generator is the difference operator | *Markov Chains and Processes* |
| Brownian motion | continuous paths, independent stationary Gaussian increments; quadratic variation $\langle B\rangle_t=t$ and Lévy's characterisation | *Brownian Motion and Stochastic Calculus* |
| a martingale | the conditional-expectation identity $\mathbb E[M_{n+1}\mid\mathcal F_n]=M_n$; optional stopping and the convergence theorem | *Martingales* |
| a stationary process | the law invariant under the shift; the ergodic theorem and its mean-square form | *Laws of Large Numbers and the Central Limit Theorem*; *Ergodic Theory* |
| a Gaussian process | every finite-dimensional law is Gaussian; determined by its mean and covariance | *Stochastic Partial Differential Equations* |
| white noise | the distributional derivative of Brownian motion; the Gaussian field with delta covariance | *Stochastic Partial Differential Equations* |
| the Ornstein–Uhlenbeck process | the Gaussian stationary Markov process with an exponential covariance; the Brownian motion in a quadratic potential | *Brownian Motion and Stochastic Calculus*; *Ergodic Theory* |
| the solution of a stochastic differential equation | the Itô and Stratonovich integrals; existence, uniqueness and the Markov property | *Stochastic Differential Equations* |

## The Convergence Theorems

| Object | What it asserts | Introduced in |
|---|---|---|
| the weak law of large numbers | the empirical mean converges in probability to the mean; the Chebyshev case needs a finite variance, Khinchin's theorem does not | *Laws of Large Numbers and the Central Limit Theorem* |
| the strong law of large numbers | the empirical mean converges almost surely; Kolmogorov's theorem under the first moment | *Laws of Large Numbers and the Central Limit Theorem* |
| the central limit theorem | the standardised sum converges in distribution to $N(0,1)$; the Lindeberg–Lévy theorem | *Laws of Large Numbers and the Central Limit Theorem* |
| the Lindeberg–Feller theorem | the central limit theorem for triangular arrays under the Lindeberg condition | *Laws of Large Numbers and the Central Limit Theorem* |
| the Berry–Esseen theorem | the rate $O(n^{-1/2})$ of the convergence, with a constant depending on a third moment | *Laws of Large Numbers and the Central Limit Theorem* |
| the local limit theorem | the density converges pointwise to the Gaussian density | *Laws of Large Numbers and the Central Limit Theorem* |
| large deviations | the exponential rate of decay of the probability of a deviation; the Cramér rate function | *Laws of Large Numbers and the Central Limit Theorem* |
| the invariance principle (Donsker) | the rescaled random walk converges in distribution to Brownian motion | *Laws of Large Numbers and the Central Limit Theorem*; *Brownian Motion and Stochastic Calculus* |
| the martingale convergence theorem | a bounded submartingale converges almost surely | *Martingales* |
| the optional stopping theorem | the expectation identity preserved at a stopping time | *Martingales* |
| the ergodic theorem | time averages converge to space averages; Birkhoff's almost-sure and von Neumann's mean-square forms | *Ergodic Theory* |

## Distributions and Processes That Fail a Hypothesis

| Object | The failure | Introduced in |
|---|---|---|
| the Cauchy distribution | has no mean and no variance, so the law of large numbers and the central limit theorem do not apply; the sample mean has the same law | *Measure-Theoretic Probability* |
| a law with an infinite second moment | the central limit theorem fails; the limit is a stable law with index $\alpha<2$ | *Laws of Large Numbers and the Central Limit Theorem* |
| a distribution that is not determined by its moments | the moment sequence does not determine the law, so the moments do not give the characteristic function | *Measure-Theoretic Probability* |
| a stationary but not ergodic process | the time averages need not converge to the space average | *Ergodic Theory* |
| the empirical measure of a non-ergodic system | converges to a mixture, not to a single distribution | *Ergodic Theory* |
| a Markov chain that is not irreducible | has no unique stationary distribution, and the convergence to stationarity fails | *Markov Chains and Processes* |
| the sample paths of Brownian motion | are almost surely nowhere differentiable and of infinite variation, so the classical integral does not exist | *Brownian Motion and Stochastic Calculus* |

## Summary

This list gathers the probability distributions and processes of the corpus: the Bernoulli, binomial, Poisson and degenerate discrete laws, the uniform, normal and Cauchy laws with the Cantor distribution and the stable and infinitely divisible family, the theory of the law, the distribution function and the characteristic function, the Markov chains, Poisson process, Brownian motion, martingales, stationary and Gaussian processes and white noise, and the limit theorems — the laws of large numbers, the central limit theorem and its refinements, the invariance principle, the martingale convergence theorem and the ergodic theorem. The closing table records the distributions and processes that fail a hypothesis of the theory.

## Summary of Notation

The objects are named by their standard symbols; the tables use the following.

| Symbol | Meaning |
|---|---|
| $\mathrm{Bern}(p)$, $\mathrm{Bin}(n,p)$, $\mathrm{Pois}(\lambda)$ | Bernoulli, binomial, Poisson laws |
| $N(\mu,\sigma^2)$, $N(0,1)$ | normal and standard normal laws |
| $\mu_X=\mathbb P\circ X^{-1}$ | the law of $X$ |
| $F_X$, $F^{-1}$, $\varphi_X$ | distribution function, quantile function, characteristic function |
| $\mathbb E$, $\operatorname{Var}$, $\operatorname{Cov}$ | expectation, variance, covariance |
| $M_n$, $\mathcal F_n$ | martingale and its filtration |
| $B_t$ | Brownian motion |
| $T_t$, $L$ | transition semigroup and its generator |

## Further Reading

- William Feller, *An Introduction to Probability Theory and Its Applications*, 3rd ed., 2 vols. (Wiley, 1968–1971), for the catalogue of distributions with their moments and generating functions.
- Patrick Billingsley, *Probability and Measure*, 3rd ed. (Wiley, 1995), for the measure-theoretic foundations and the limit theorems.
- Daniel W. Stroock and S. R. Srinivasa Varadhan, *Multidimensional Diffusion Processes* (Springer, 1979), for the Markov processes and the martingale problem.
