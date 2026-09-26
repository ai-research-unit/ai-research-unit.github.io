
# __Probabilistic Number Theory__

## Introduction

Probabilistic number theory is the study of the distribution of the values of arithmetic functions and of the primes themselves. An arithmetic function is deterministic — its value at $n$ is determined by the prime factorisation — but its behaviour on the integers is irregular, and the discovery of the subject is that it becomes regular when read statistically: the number $\omega(n)$ of distinct prime factors of $n$ has the normal order $\log\log n$, with Gaussian fluctuations of order $\sqrt{\log\log n}$ about it, exactly as if the events " $p$ divides $n$ " were independent over the primes with probabilities $1/p$. The Erdős–Kac theorem makes the analogy precise, and the whole subject is the elaboration of this probabilistic model and of its limits.

This article develops the distribution theory of arithmetic functions. It sets up the arithmetic functions and their additive and multiplicative classes, states the Hardy–Ramanujan normal-order theorem and the Erdős–Kac central limit theorem, proves the Turán–Kubilius inequality as the variance estimate behind them, gives the Erdős–Wintner criterion for the existence of a limiting distribution, describes the Kubilius model and its fundamental lemma, records the local and the large-deviation theory, and treats the probabilistic models of the primes — the Cramér model, the Hardy–Littlewood conjectures and the parity obstruction — together with the statistical theory of the values of the Riemann zeta function. The boundary with the method itself is the subject of the first of the notes below.

The place of the article is fixed by four boundaries.

- The **probabilistic technique** — the union bound, the first and second moment methods, the local lemma, the alteration and container methods, the concentration inequalities — is *The Probabilistic Method*, and the present article is its arithmetic application: the model in which the divisibility events are independent is a probabilistic construction, and the theorems are the limit theorems of that model.
- The **probability theory** used — the probability space, the expectation, the independence, the central limit theorem, the laws of large numbers, the martingale theory and the entropy — is the block *Measure-Theoretic Probability* through *Ergodic Theory*, and in particular the central limit theorem of *Laws of Large Numbers and the Central Limit Theorem* is the theorem transferred to the arithmetic setting.
- The **arithmetic** — the primes, the fundamental theorem of arithmetic, the elementary and analytic estimates, the Riemann zeta function, the Dirichlet series, the character sums and the multiplicative functions — is the subject of the Part I arithmetic articles, in particular *The Prime Number Theorem* and *Analytic Number Theory*, and of *Modular Forms* and *Automorphic Forms* for the zeta function's analytic theory. The **combinatorial** counterpart of the same probabilistic counting — the orbit-counting lemma, the cycle index and the random generation of a finite group — is *Combinatorial Group Theory*, the Part I neighbour of this article and of *The Probabilistic Method*. The estimates of analytic number theory — the prime number theorem, the Mertens theorems, the Brun–Titchmarsh inequality, the large sieve — are used and cited, not proved.
- The **random walks on groups** and the probability of a random walk returning to a state — the model of the divisibility by the primes on the multiplicative monoid and the additive structure of $\mathbb{Z}$ — isand the **per-system analysis of $\mathbb{Z}$** and the **arithmetic of a single number system** is Part V's. No physics is invoked.

Throughout, $n$ is a positive integer, $p$ is a prime, $\omega(n)$ is the number of distinct primes dividing $n$, $\Omega(n)$ the number counted with multiplicity, $d(n)$ the number of divisors, $\sigma$ a complex variable, $\zeta(s)$ the Riemann zeta function, and $\pi(x)$ the prime counting function. The statements "for almost all $n$" and "for a density-one set of $n$" mean that the exceptional set has natural density $0$; $\Rightarrow$ denotes convergence in distribution of random variables as in *Measure-Theoretic Probability*, $N(0,1)$ is the standard Gaussian, and $\gamma$ is Euler's constant. The arithmetic functions are real or complex-valued functions on $\mathbb{N}$; an additive function satisfies $f(mn) = f(m) + f(n)$ when $(m,n)=1$, and a multiplicative function satisfies $f(mn) = f(m)f(n)$ when $(m,n)=1$.

## Arithmetic Functions and Additive Functions

### The Classes

**Definition.** A function $f : \mathbb{N}\to\mathbb{C}$ is **additive** if $f(mn) = f(m)+f(n)$ whenever $(m,n)=1$, and **completely additive** if this holds for all $m,n$; it is **multiplicative** if $f(mn) = f(m)f(n)$ whenever $(m,n)=1$, and **completely multiplicative** if this holds for all $m,n$.

An additive function is determined by its values on the prime powers, $f(n) = \sum_{p^k\|n}f(p^k)$, and a multiplicative function by $f(n) = \prod_{p^k\|n}f(p^k)$. The prototype of an additive function is $\omega(n) = \sum_{p\mid n}1$, and the prototype of a multiplicative function is $d(n) = \prod_{p^k\|n}(k+1)$; the function $\Omega(n) = \sum_{p^k\|n}k$ is completely additive, and $\log n$ is completely additive.

**Example.** The von Mangoldt function $\Lambda$ is supported on the prime powers, $\Lambda(p^k) = \log p$; the Möbius function $\mu$ is multiplicative with $\mu(p) = -1$, $\mu(p^2) = 0$; the divisor function satisfies $d(p^k) = k+1$; and the sum-of-divisors function $\sigma$ satisfies $\sigma(p^k) = (p^{k+1}-1)/(p-1)$. The means of these functions are the content of the elementary estimates collected in *Analytic Number Theory* and *The Prime Number Theorem*, and the statistical statements below are statements about the whole distribution, not only the mean.

### The Model of Independent Divisibility

**Definition.** For a finite set of primes $P = \{p_1,\dots,p_r\}$ the **Kubilius model** attaches to each $p\in P$ an independent Bernoulli random variable $X_p$ with

$$
\mathbb{P}(X_p = 1) = \frac{1}{p}, \qquad \mathbb{P}(X_p = 0) = 1 - \frac{1}{p},
$$

and defines the model integer by the divisibility pattern: the model additive function is $f_P = \sum_{p\in P}f(p)X_p$, so that the $X_p$ play the role of the indicators $\mathbf{1}_{p\mid n}$.

The model is the source of the whole subject. For a fixed finite set of primes the Chinese remainder theorem gives the exact distribution of the vector $(\mathbf{1}_{p\mid n})_{p\in P}$ on $n \leq N$: a residue class modulo $\prod_{p\in P}p$ contains $N/\prod_{p\in P}p + O(1)$ integers up to $N$, so the indicators are asymptotically independent Bernoulli with the probabilities $1/p$ as $N\to\infty$ and then $P$ fixed. The **fundamental lemma** of Kubilius quantifies the discrepancy for the sets $P$ that arise, and it is the technical heart of the Erdős–Kac theorem.

**Lemma (fundamental lemma of Kubilius; sketch).** Let $P$ be a set of primes with $\prod_{p\in P}p \leq N$ and let $E\subseteq\{0,1\}^P$ be a set of divisibility patterns. Then

$$
\frac{1}{N}\#\left\{n\leq N : (\mathbf{1}_{p\mid n})_{p\in P}\in E\right\} = \mathbb{P}\bigl((X_p)_{p\in P}\in E\bigr) + O\!\left(\frac{1}{N}\prod_{p\in P}p\right),
$$

where the error term is uniform in $E$.

The lemma is the bridge between the deterministic counting and the probabilistic model: as long as the product of the primes involved is much smaller than $N$, the model is accurate to within a relative error that tends to zero. The condition is exactly the restriction that makes the model tractable, and the whole art of the subject is to choose the set $P$ — the "small primes" — so that the model applies to them and the "large primes" contribute only their mean.

## The Normal Order and the Erdős–Kac Theorem

### The Hardy–Ramanujan Theorem

**Theorem (Hardy–Ramanujan).** For almost all $n$, the number of distinct prime factors satisfies

$$
\omega(n) = \log\log n + O\!\left(\sqrt{\log\log n}\right),
$$

and more precisely $|\omega(n) - \log\log n| \leq (1+\varepsilon)\sqrt{2\log\log n\log\log\log n}$ for almost all $n$ and every $\varepsilon > 0$; the function $\log\log n$ is the **normal order** of $\omega(n)$.

The theorem is the first statement of the regularity of $\omega$: although $\omega(n)$ takes the values $0, 1, 2, \dots$ on a set of positive density (the primes have $\omega = 1$, and a positive proportion of $n$ is prime-free of a prescribed set), the overwhelming majority of integers have about $\log\log n$ prime factors. The proof is the estimate of the moments of the model: the mean of $\omega$ is $\sum_{p\leq n}1/p = \log\log n + O(1)$ by the Mertens theorem, and the variance is the same quantity, so Chebyshev's inequality — the second moment method of *The Probabilistic Method* — gives the concentration.

### The Erdős–Kac Theorem

**Theorem (Erdős–Kac).** For $n$ chosen uniformly at random from $\{1,\dots,N\}$,

$$
\frac{\omega(n) - \log\log N}{\sqrt{\log\log N}} \Longrightarrow N(0,1) \qquad \text{as } N\to\infty,
$$

convergence in distribution to the standard Gaussian.

*Proof (sketch).* Write $\omega = \sum_{p\leq N}\mathbf{1}_{p\mid n}$, split the primes into the small ones $p \leq N^{1/\log\log N}$ and the large ones, and let $Y = \sum_{p\leq N^{1/\log\log N}}\mathbf{1}_{p\mid n}$ be the small-prime part. By the fundamental lemma the small-prime indicators behave as independent Bernoulli$(1/p)$ variables, so $Y$ is a sum of independent bounded variables with mean $\mu = \sum_{p\leq N^{1/\log\log N}}1/p = \log\log N + O(\log\log\log N)$ and variance $\mu - \sum1/p^2 = \log\log N + O(1)$; the Lindeberg–Feller central limit theorem of *Laws of Large Numbers and the Central Limit Theorem* applies, and $(Y - \log\log N)/\sqrt{\log\log N}$ is asymptotically Gaussian. The large-prime part $\omega - Y$ counts the primes $p > N^{1/\log\log N}$ dividing $n$: each contributes at most one, and the total number of such primes dividing $n$ is $O(\log\log\log N)$ for almost all $n$, so its variance is $o(\log\log N)$ and it is negligible after normalisation. $\square$

The theorem is the central limit theorem of number theory, and the shape of the statement — the mean and the variance both equal to $\log\log N$ — is the signature of the Poisson limit of rare events: the number of prime factors below $N^{1/\log\log N}$ is a sum of many independent indicators with small probabilities, and its limiting law is Gaussian rather than Poisson because the mean $\log\log N$ diverges. The theorem also holds for $\Omega(n)$ and, with the constants of the multiplicative model, for $\log d(n)$: the normal order of $\log d(n)$ is $(\log 2)\log\log n$ and the fluctuations are Gaussian of order $\sqrt{\log\log n}$.

**Remark.** The theorem is the arithmetic analogue of the law of large numbers of *Laws of Large Numbers and the Central Limit Theorem*, with the independent sequence replaced by the indicators of divisibility: the independence in the arithmetic model is asymptotic, and the proof is the reduction of the arithmetic sum to an independent sum by the fundamental lemma. The same reduction, applied to a general additive function, gives the criterion of the next section.

## The Turán–Kubilius Inequality and the Second Moment

**Theorem (Turán–Kubilius inequality).** There is an absolute constant $C$ such that for every complex additive function $f$ and every $N \geq 2$,

$$
\sum_{n\leq N}\left|f(n) - \sum_{p\leq N}\frac{f(p)}{p}\right|^2 \leq C\,N\sum_{p\leq N}\frac{|f(p)|^2}{p}.
$$

*Proof (sketch).* Write the averaged function $A_N = \sum_{p\leq N}f(p)/p$ and expand the square as a double sum over $n \leq N$. The diagonal $(p = q)$ contributes $\sum_{p\leq N}|f(p)|^2\sum_{n\leq N}\mathbf{1}_{p\mid n} \leq N\sum_p|f(p)|^2/p$, which is the right-hand side; the off-diagonal is estimated by the Chinese remainder theorem, $\sum_{n\leq N}\mathbf{1}_{p\mid n,q\mid n} = N/(pq) + O(1)$, with the summation grouped according to the size of $pq$, and the resulting error is absorbed in the constant $C$. The inequality is the standard one; the point of the sketch is that the main term is the sum of the variances of the prime contributions. $\square$

The inequality is the variance estimate of the subject: it says that the second moment of an additive function about its mean is controlled by the sum of the variances of the prime contributions, and it is the arithmetic form of the law of large numbers. Applied to $f = \omega$, it gives $\sum_{n\leq N}(\omega(n)-\log\log N)^2 = O(N\log\log N)$, which is the concentration behind the Hardy–Ramanujan theorem; applied to $f(n) = \sum_{p\mid n}f(p)$ for a general additive $f$, it reduces the problem of the distribution of $f$ to the distribution of the model sum $\sum_pf(p)X_p$, which is a sum of independent variables and falls under the Lindeberg–Feller criterion.

**Theorem (Erdős–Wintner).** A real additive function $f$ has a limiting distribution — that is, the distributions of $f(n)$ for $n$ uniform on $\{1,\dots,N\}$ converge weakly as $N\to\infty$ — if and only if the two series

$$
\sum_{\substack{p\\|f(p)|\leq1}}\frac{|f(p)|}{p}, \qquad \sum_{\substack{p\\|f(p)|>1}}\frac{f(p)^2}{p}
$$

converge, with the contribution of the prime powers also convergent.

The criterion is the arithmetic form of the three-series theorem: the small values $|f(p)|\leq1$ must be summable in the mean, and the large ones must be square-summable with the weight $1/p$, which is exactly the condition for the model sum of independent variables to converge. When the criterion holds the limiting distribution is the law of the convergent sum, and when it fails no limiting distribution exists; the theorem reduces the classification of the additive functions to the summability of a series over the primes.

## The Distribution of the Values

### The Local and the Local Limit Theorems

**Theorem (smoothing and the local limit theorem; sketch).** Let $f$ be additive with $\mathbb{E}[f] = \mu(N)$ and $\operatorname{Var}(f) = v(N)^2$, where the moments are those of the model. Then for $f$ in a suitable class — the strongly additive functions with $f(p)$ varying slowly and not congruent to a fixed function modulo a lattice — the law of $f(n)$ admits a density after smoothing over intervals of length $v(N)^{1/2+\varepsilon}$, and the density is uniformly Gaussian:

$$
\mathbb{P}\bigl(f(n) - \mu(N) \in [a,b]\,v(N)\bigr) \longrightarrow \frac{1}{\sqrt{2\pi}}\int_a^be^{-t^2/2}\,dt.
$$

The local limit theorem is the refinement of the central limit theorem from the distribution function to the density, and it is the form in which the theorem is applied to the count of integers with a prescribed number of prime factors: the number of $n \leq N$ with $\omega(n) = k$ is, for $k$ near $\log\log N$, asymptotic to $N/\sqrt{2\pi\log\log N}$ times the Gaussian density at $(k - \log\log N)/\sqrt{\log\log N}$, with a congruence correction when the values of $f(p)$ lie on a lattice.

### The Sathe–Selberg Formula and the Large Deviations

**Theorem (Sathe–Selberg; sketch).** For $k = o(\log\log N)$ the number of $n\leq N$ with exactly $k$ prime factors is

$$
\#\{n\leq N : \Omega(n) = k\} \sim \frac{N}{\log N}\frac{(\log\log N)^{k-1}}{(k-1)!},
$$

and the same asymptotic formula, with a further factor $1 + o(1)$, holds for $\omega(n) = k$ in the same range of $k$.

The formula is the local form of the Erdős–Kac theorem, and it is the arithmetic form of the Poisson approximation of the model: the Prime Number Theorem gives the case $k=1$, and the sum of the formula over all $k$ in the range reproduces the fact that most integers have their normal number of prime factors. Summing over $k \leq \theta\log\log N$ and using Stirling's formula for the dominant term gives, for fixed $0 < \theta < 1$,

$$
\#\{n\leq N : \omega(n)\leq\theta\log\log N\} = N(\log N)^{-2+\theta(1+\log(1/\theta))+o(1)} \quad (\log\log N\to\infty),
$$

and summing over $k \geq (1+\theta)\log\log N$ gives the corresponding upper tail; both are powers of $\log N$.

**Theorem (large deviations; sketch).** The upper deviations from the normal order are governed by the Poisson rate function $I(\theta) = (1+\theta)\log(1+\theta) - \theta$: for fixed $\theta > 0$,

$$
\#\{n\leq N : \omega(n)\geq(1+\theta)\log\log N\} = N(\log N)^{-I(\theta)+o(1)},
$$

and for fixed $0<\phi<1$ the Sathe–Selberg sum over $k\leq\phi\log\log N$ gives

$$
\#\{n\leq N : \omega(n)\leq\phi\log\log N\} = N(\log N)^{-2+\phi-\phi\log\phi+o(1)}.
$$

In particular the deviations decay only like powers of $\log N$ — far slower than exponentially in $N$ — which is why the exceptional sets of the arithmetic statements, the integers with very few or very many prime factors, are large in the logarithmic scale though their density tends to zero.

## The Probabilistic Models of the Primes

### The Cramér Model

**Definition.** The **Cramér model** treats the indicator $\mathbf{1}_{n \text{ prime}}$ as an independent Bernoulli random variable with probability $1/\log n$, so that the number of primes in disjoint intervals is a sum of independent variables. The model is a heuristic, not a theorem; it predicts that the primes have the same statistical behaviour as a sequence of independent events with density $1/\log n$.

Under the model the prime number theorem holds with probability one, the maximal gap between consecutive primes below $x$ is of order $\log^2x$, and the count of primes in $[x,x+y]$ is Gaussian with mean $y/\log x$ and variance $y/\log x$ for $y$ large. The model is now supported by the resolution of the famous conjectures of Cramér type under the assumption of the Riemann hypothesis, and its failures are as important as its successes.

### The Hardy–Littlewood Conjectures and the Parity Obstruction

**Conjecture (Hardy–Littlewood).** For a finite admissible prime pattern $\mathcal{H} = \{h_1,\dots,h_k\}$ the number of $n\leq x$ with all of $n+h_i$ prime is asymptotic to

$$
\mathfrak{S}(\mathcal{H})\frac{x}{(\log x)^k}, \qquad \mathfrak{S}(\mathcal{H}) = \prod_p\left(1 - \frac{1}{p}\right)^{-k}\left(1 - \frac{\nu_{\mathcal{H}}(p)}{p}\right),
$$

where $\nu_{\mathcal{H}}(p)$ is the number of distinct residues of $\mathcal{H}$ modulo $p$ and the product is the **singular series**.

The conjecture is the quantitative form of the independence of the prime events in the pattern, and the singular series is the correction for the arithmetic obstructions at the small primes: it is the ratio of the model probability to the naive density $1/(\log x)^k$, and its Euler product is the exact form of the independence in the model. The parity obstruction is the reason the model cannot be made a theorem by the known sieve methods: the sieves cannot distinguish integers with an even number of prime factors from those with an odd number, so they cannot detect the primes themselves, and the twin prime conjecture and the Goldbach conjecture remain beyond the unconditional reach of the method. Theorems that approximate the conjectures — the bounded gaps between primes of Zhang, Maynard and Tao, and the partial results on the prime patterns — are proved by different methods and are cited from *Analytic Number Theory*.

**Remark.** The model also fails for the fine structure of the distribution of the primes in short intervals: the Cramér model predicts a Gaussian distribution with variance $y/\log x$, whereas the true variance exhibits the correlations of the primes within the intervals, and the discrepancy is the manifestation of the arithmetic of the singular series. This is the reason the subject distinguishes the "statistical" statements, which the model supports, from the "individual" statements, which it does not.

## The Statistical Theory of the Riemann Zeta Function

### Selberg's Central Limit Theorem

**Theorem (Selberg).** Let $t$ be chosen uniformly at random from $[T,2T]$. Then, as $T\to\infty$,

$$
\frac{\log|\zeta(1/2+it)|}{\sqrt{\frac{1}{2}\log\log T}} \Longrightarrow N(0,1),
$$

and more generally

$$
\frac{\log\zeta(1/2+it)}{\sqrt{\frac{1}{2}\log\log T}} \Longrightarrow \mathcal{N}_{\mathbb{C}},
$$

where $\mathcal{N}_{\mathbb{C}}$ is the standard complex Gaussian, in the sense that the real and imaginary parts are independent centred Gaussians of variance $1/2$.

Selberg's theorem is the central limit theorem for the values of the zeta function, and the mechanism is the same as in the Erdős–Kac theorem: the Dirichlet polynomial approximation of $\zeta(1/2+it)$ is a sum of terms $n^{-1/2-it}$ whose phases $n^{-it}$ behave like independent random variables, and the logarithm converts the product into a sum of independent contributions. The theorem is the foundation of the statistical theory of the zeta function, and it is the reason the values of $\zeta$ on the critical line are called "random": they obey the Gaussian law of the model. The statistical distribution of the zeros — the random-matrix model of Montgomery and Odlyzko, in which the zeros behave like the eigenvalues of a random unitary matrix — is the other half of the picture, and its analytic input is the explicit formula and the pair correlation, cited from *Analytic Number Theory* and *Automorphic Forms*.

### The Distribution of the Divisor Function and the Local Statistics

**Theorem (Erdős–Kac for $d$; sketch).** For $n$ uniform on $\{1,\dots,N\}$,

$$
\frac{\log d(n) - (\log2)\log\log N}{(\log2)\sqrt{\log\log N}} \Longrightarrow N(0,1),
$$

and the normal order of $\log d(n)$ is $(\log2)\log\log N$.

The theorem is the multiplicative counterpart of the Erdős–Kac theorem and it is proved by the same reduction: $\log d(n) = \sum_{p^k\|n}\log(k+1)$ is additive, its mean over the model is $(\log2)\log\log N$, and its variance is $(\log2)^2\log\log N$, computed from the distribution $\mathbb{P}(v_p = k) = (1-1/p)p^{-k}$ of the exponent of $p$. The statement is the reason the divisor function is "lognormally distributed", and it is the model for the statistical theory of any multiplicative function.

## Summary

Probabilistic number theory reads the arithmetic functions statistically, and its central observation is that the indicators of divisibility by the primes behave, in the relevant range, like independent random variables with probabilities $1/p$. The Kubilius model makes this precise: the fundamental lemma shows that the divisibility patterns modulo a set of primes with product much smaller than $N$ are equidistributed, so the model sum reproduces the arithmetic sums with a vanishing relative error. The mean and the variance of $\omega(n)$ are both $\log\log n$ by the Mertens theorem, so $\log\log n$ is the normal order of $\omega$ (Hardy–Ramanujan) and the normalised difference is asymptotically Gaussian (Erdős–Kac); the Turán–Kubilius inequality is the second moment estimate behind both, and the Erdős–Wintner criterion classifies the additive functions with a limiting distribution by the summability of two series over the primes.

The distribution theory extends from $\omega$ to the local limit theorems, to the large deviations, to the divisor function — whose logarithm is lognormal with normal order $(\log2)\log\log N$ — and to the values of the Riemann zeta function on the critical line, where Selberg's central limit theorem is the analogue of the Erdős–Kac theorem for the Dirichlet polynomial. The probabilistic models of the primes — the Cramér model, with the independent indicators of density $1/\log n$, and the Hardy–Littlewood conjectures, with the singular series as the arithmetic correction — give the quantitative predictions for the prime patterns, and their limitations are the parity obstruction of the sieve methods and the failure for the fine local statistics. The method that supplies the technique is *The Probabilistic Method*; the group-theoretic counterpart of the model, the random walk on the multiplicative monoid and on a group, is.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $f$, additive / multiplicative | $f(mn)=f(m)+f(n)$ / $f(mn)=f(m)f(n)$ when $(m,n)=1$ |
| $\omega(n)$, $\Omega(n)$, $d(n)$ | distinct, counted-with-multiplicity prime factors, divisors |
| $\Lambda$, $\mu$, $\sigma$ | von Mangoldt, Möbius, sum-of-divisors functions |
| $X_p$ | independent Bernoulli$(1/p)$ indicator of the Kubilius model |
| $P$, $E$ | finite set of primes; set of divisibility patterns |
| $\omega$, $\Omega$ normal order | $\log\log n$ |
| Erdős–Kac | $(\omega(n)-\log\log N)/\sqrt{\log\log N}\Rightarrow N(0,1)$ |
| $A_N=\sum_{p\le N}f(p)/p$ | mean of the model |
| Turán–Kubilius | $\sum_{n\le N}\lvert f(n)-A_N\rvert^2\le CN\sum_{p\le N}\lvert f(p)\rvert^2/p$ |
| Erdős–Wintner | limiting distribution iff $\sum_{\lvert f(p)\rvert\le1}\lvert f(p)\rvert/p$ and $\sum_{\lvert f(p)\rvert>1}f(p)^2/p$ converge |
| $v(N)$, local limit | model variance; Gaussian density after smoothing |
| Cramér model | independent indicators of density $1/\log n$ |
| $\mathfrak{S}(\mathcal{H})$ | singular series of the pattern $\mathcal{H}$ |
| Selberg CLT | $\log\lvert\zeta(1/2+it)\rvert/\sqrt{\frac12\log\log T}\Rightarrow N(0,1)$ |
| $\mathcal{N}_{\mathbb{C}}$ | standard complex Gaussian |



## Further Reading

- P. D. T. A. Elliott, *Probabilistic Number Theory I, II* (Springer, 1979, 1980), for the systematic theory of additive functions and the Erdős–Wintner criterion.
- Mark Kac, *Statistical Independence in Probability, Analysis and Number Theory* (Wiley, 1959), for the Kubilius model and the Erdős–Kac theorem.
- G. H. Hardy and S. Ramanujan, "The normal number of prime factors of a number $n$", *Quarterly Journal of Mathematics* 48 (1917), 76–92, for the normal order of $\omega$.
- Paul Erdős and Mark Kac, "The Gaussian law of errors in the theory of additive number theoretic functions", *American Journal of Mathematics* 62 (1940), 738–742, for the central limit theorem.
- Paul Turán, "On a theorem of Hardy and Ramanujan", *Journal of the London Mathematical Society* 9 (1934), 274–276, and J. Kubilius, *Probabilistic Methods in the Theory of Numbers* (American Mathematical Society, 1964), for the variance inequality and the model.
- H. Cramér, "On the order of magnitude of the difference between consecutive prime numbers", *Acta Arithmetica* 2 (1936), 23–46, for the Cramér model.
- G. H. Hardy and J. E. Littlewood, "Some problems of 'partitio numerorum' III", *Acta Mathematica* 44 (1923), 1–70, for the singular series and the prime-pair conjectures.
- Atle Selberg, "Contributions to the theory of the Riemann zeta-function", *Archiv for Mathematik og Naturvidenskab* 48 (1946), 89–155, for the central limit theorem for $\log\zeta$.
- Hugh L. Montgomery, "The pair correlation of zeros of the zeta function", in *Analytic Number Theory* (American Mathematical Society, 1973), 181–193, for the random-matrix statistics of the zeros.
- Terence Tao and Van Vu, *Additive Combinatorics* (Cambridge University Press, 2006), and K. Soundararajan, "The distribution of values of the Riemann zeta function", in *Proceedings of the International Congress of Mathematicians* (2014), for the probabilistic viewpoint on the zeta function.
