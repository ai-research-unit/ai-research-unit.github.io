
# __Laws of Large Numbers and the Central Limit Theorem__

## Introduction

The two limit theorems of classical probability theory answer the two questions one asks about a sum of independent random variables. The law of large numbers says that the average settles down: the sample mean of a large number of independent observations converges to the theoretical mean, in probability in its weak form and almost surely in its strong form. The central limit theorem says how the fluctuations around that limit are distributed: after centring and scaling by the square root of the number of terms, the fluctuations converge in distribution to the standard normal, whatever the distribution of the individual terms, provided only that the variance is finite. Together the two theorems are the reason the mean is a stable estimator and the normal distribution is universal.

This article proves both, together with the refinements that make them usable: the continuity theorem that converts the convergence of distributions into the convergence of characteristic functions, the Lindeberg–Feller condition that determines exactly when the triangular-array central limit theorem holds, the Berry–Esseen and Edgeworth estimates of the rate, the local limit theorem for lattice distributions, the Cramér large-deviation theorem for the tails, and the Lévy–Khintchine representation that describes the possible limit laws. The organisational frame is the characteristic function of *Measure-Theoretic Probability* and the independence and conditional expectation of *Independence and Conditional Expectation*.

Three boundaries are held.

- The **notation and the groundwork** are those of *Measure-Theoretic Probability*: $(\Omega,\mathcal{F},\mathbb{P})$, $\mu_X$, $\mathbb{E}$, $\operatorname{Var}$, a.s., $\varphi_X(t) = \mathbb{E}[e^{itX}]$, and the four modes of convergence with the implications established there. The **independence** and the **product measure** are *Independence and Conditional Expectation*, and the **conditional expectation** with its properties is used below.
- The **martingale theory** — the maximal inequalities of Doob, the optional stopping theorem, the martingale convergence theorem and the martingale central limit theorem — isand the **functional limit theory** and the invariance principle are; where a result belongs there it is named and deferred.
- The **ergodic-theoretic form** of the law of large numbers — the convergence of the time averages of a measure-preserving transformation, with independent sequences as the special case of a Bernoulli shift — isand the comparison is made in the prose rather than in the proofs. No physics is invoked.

Throughout, $X_1, X_2, \dots$ are independent and identically distributed real random variables with mean $\mu = \mathbb{E}[X_1] \in \mathbb{R}$ and variance $\sigma^2 = \operatorname{Var}(X_1) \in (0,\infty)$ when the variance is finite; $S_n = X_1 + \cdots + X_n$ is the partial sum, $\bar X_n = S_n/n$ the sample mean, and $Z_n = (S_n - n\mu)/(\sigma\sqrt n)$ the standardised sum. The characteristic function is $\varphi(t) = \mathbb{E}[e^{itX_1}]$, the standard normal distribution is $N(0,1)$ with distribution function $\Phi$, and $X_n \xrightarrow{d} X$ denotes convergence in distribution.

## Characteristic Functions and the Continuity Theorem

### The Continuity Theorem

The characteristic function is the tool that converts a statement about distributions into a statement about functions, and its usefulness rests on the converse of the elementary implication: convergence in distribution implies the pointwise convergence of the characteristic functions, and the converse holds provided the limit function is continuous.

**Theorem (Lévy's continuity theorem).** Let $\mu_n$ be probability measures on $\mathbb{R}$ with characteristic functions $\varphi_n$ and suppose $\varphi_n(t) \to \varphi(t)$ for every $t$ and $\varphi$ is continuous at $t=0$. Then $\varphi$ is the characteristic function of a probability measure $\mu$ and $\mu_n \to \mu$ weakly.

*Proof.* The measures $\mu_n$ are tight: by the estimate of the next lemma, a uniform bound of the integrals of $1-\Re\varphi_n$ over a neighbourhood of $0$ controls the mass outside a large compact set, and the assumed convergence to a function continuous at $0$ gives that bound. Tightness supplies a weakly convergent subsequence $\mu_{n_k} \to \mu$, whose characteristic function is $\varphi$ by the elementary direction; the limit is independent of the subsequence because the limit function $\varphi$ is the same, so the whole sequence converges. $\square$

**Lemma (tail estimate).** For a probability measure with characteristic function $\varphi$ and any $u > 0$,

$$
\mu\bigl((-\infty, -2/u] \cup [2/u, \infty)\bigr) \leq \frac{2}{u}\int_{-u}^{u}\bigl(1 - \Re\varphi(t)\bigr)\, dt.
$$

*Proof.* Integrate the identity $1 - \Re\varphi(t) = \int (1 - \cos tx)\, d\mu(x)$ over $-u \le t \le u$ and use $(1/u)\int_{-u}^u(1-\cos tx)\,dt = 1 - \sin(ux)/(ux)$, which is at least $1/2$ for $|ux| \ge 2$; this last inequality gives, after dividing by $u$, the bound $\mu(|x|\ge 2/u)\le \frac{2}{u}\int_{-u}^{u}(1 - \Re\varphi(t))\,dt$ on the union of the two tails. $\square$

The continuity theorem is the reason the central limit theorem is proved by computing the limit of the characteristic functions: one computes $\varphi_{Z_n}(t) \to e^{-t^2/2}$ for every $t$, observes that the limit is continuous, and invokes Lévy. The same pattern proves the convergence of the binomial to the normal, of the Poisson to the normal in the appropriate regime, and of the triangular-array limits of the next sections.

## The Weak Law of Large Numbers

### The Chebyshev Case

**Theorem (weak law, finite variance).** Let $X_1, X_2, \dots$ be independent with common mean $\mu$ and common finite variance $\sigma^2$. Then the sample mean converges in probability to $\mu$: $\bar X_n \xrightarrow{\mathbb{P}} \mu$.

*Proof.* The mean and variance of the sample mean are $\mathbb{E}[\bar X_n] = \mu$ and $\operatorname{Var}(\bar X_n) = \sigma^2/n$, the second because the variances of independent terms add. The Chebyshev inequality of *Measure-Theoretic Probability* then gives

$$
\mathbb{P}\bigl(|\bar X_n - \mu| \geq \varepsilon\bigr) \leq \frac{\operatorname{Var}(\bar X_n)}{\varepsilon^2} = \frac{\sigma^2}{n\varepsilon^2} \longrightarrow 0
$$

for every $\varepsilon > 0$. $\square$

The proof shows that the weak law at finite variance is a variance computation, and that the rate is $O(1/n)$. The assumption of a common variance is unnecessary and the next theorem removes both it and the assumption of identical moments.

### The Khinchin Theorem and Truncation

**Theorem (Khinchin's weak law).** Let $X_1, X_2, \dots$ be independent and identically distributed with $\mathbb{E}|X_1| < \infty$ and mean $\mu$. Then $\bar X_n \xrightarrow{\mathbb{P}} \mu$.

*Proof.* Truncate: let $Y_{n,i} = X_i\mathbf{1}_{\{|X_i| \le n\}}$. The truncated variables have $\mathbb{E}Y_{n,i} \to \mu$, and since $\bar Y_n$ is the average of $n$ such variables,

$$
\operatorname{Var}(\bar Y_n) = \frac{1}{n}\operatorname{Var}(Y_{n,1}) \leq \frac{1}{n}\mathbb{E}\bigl[X_1^2\mathbf{1}_{\{|X_1|\le n\}}\bigr] \leq \mathbb{E}\bigl[|X_1|\mathbf{1}_{\{|X_1|\le n\}}\bigr] \longrightarrow 0
$$

by dominated convergence, because $|X_1|\mathbf{1}_{\{|X_1|\le n\}}\le|X_1| \in L^1$; hence $\bar Y_n \xrightarrow{\mathbb{P}} \mu$ by Chebyshev. It remains to control the discarded mass: $\mathbb{P}(\bigcup_{i\le n}\{X_i \neq Y_{n,i}\}) \leq n\mathbb{P}(|X_1| > n) \to 0$ since $n\mathbf{1}_{\{|X_1|>n\}}\le|X_1|\mathbf{1}_{\{|X_1|>n\}}$ and $X_1$ is integrable, and on the complement the two averages coincide. $\square$

The truncation argument is the standard method for extracting a law of large numbers from an integrability hypothesis, and it identifies the correct hypothesis: the weak law holds precisely when the truncated means converge to $\mu$, which fails exactly for the distributions with $\mathbb{E}|X_1| = \infty$ and a Cauchy-like tail. The prototypical failure is the Cauchy distribution, whose characteristic function is $e^{-|t|}$ and for which the sample mean has the same Cauchy distribution for every $n$, so it does not converge.

## The Strong Law of Large Numbers

### The Maximal Inequality

**Theorem (Kolmogorov's maximal inequality).** Let $X_1, \dots, X_n$ be independent with $\mathbb{E}X_i = 0$ and finite variance, and let $S_k = X_1 + \cdots + X_k$. Then for every $\lambda > 0$,

$$
\mathbb{P}\!\left(\max_{1\leq k\leq n}|S_k| \geq \lambda\right) \leq \frac{1}{\lambda^2}\sum_{k=1}^{n}\mathbb{E}[X_k^2] = \frac{\mathbb{E}[S_n^2]}{\lambda^2}.
$$

*Proof.* Let $A$ be the event that the maximum exceeds $\lambda$ and let $A_k$ be the event that the first crossing occurs at $k$: $A_k = \{|S_1| < \lambda, \dots, |S_{k-1}| < \lambda, |S_k| \geq \lambda\}$. Then $A$ is the disjoint union of the $A_k$ and

$$
\mathbb{E}[S_n^2] \geq \sum_{k=1}^{n}\mathbb{E}\bigl[S_n^2\mathbf{1}_{A_k}\bigr] = \sum_{k=1}^{n}\left(\mathbb{E}\bigl[S_k^2\mathbf{1}_{A_k}\bigr] + 2\mathbb{E}\bigl[S_k(S_n - S_k)\mathbf{1}_{A_k}\bigr] + \mathbb{E}\bigl[(S_n-S_k)^2\mathbf{1}_{A_k}\bigr]\right).
$$

The cross term vanishes because $S_k\mathbf{1}_{A_k}$ is $\sigma(X_1,\dots,X_k)$-measurable and $S_n - S_k$ is independent of that $\sigma$-algebra with mean zero; dropping the two nonnegative terms leaves $\mathbb{E}[S_n^2] \geq \sum_k \lambda^2\mathbb{P}(A_k) = \lambda^2\mathbb{P}(A)$. $\square$

The inequality is the martingale-type maximal bound in its independent-sum form, and it is the reason the strong law can be proved before the martingale theory is available; the general maximal inequality of Doob, contains it. The proof uses the independence only through the orthogonality of the past and the future, which is exactly the property the martingale theory abstracts.

### The Kolmogorov Strong Law

**Theorem (strong law of large numbers; Kolmogorov).** Let $X_1, X_2, \dots$ be independent and identically distributed with $\mathbb{E}|X_1| < \infty$ and mean $\mu$. Then

$$
\bar X_n \longrightarrow \mu \qquad \text{a.s.}
$$

*Proof (sketch).* It suffices to treat the mean-zero case by centring. Assume first a finite fourth moment; the estimate $\mathbb{E}[S_n^4] \leq Cn^2$ (obtained by expanding the fourth power and using independence) together with the first Borel–Cantelli lemma applied to the events $\{|\bar X_{n}| \geq \varepsilon\}$ along the subsequence $n = 2^k$ gives convergence along that subsequence; the maximal inequality extends it to the intermediate integers, using that the increments between $2^k$ and $2^{k+1}$ are controlled by the maximal inequality. For the general case, truncate at the level $n$ and use the three-series-type estimate to show that the truncated and untruncated averages have the same limit a.s.; the details are the standard argument. $\square$

**Theorem (Etemadi).** The strong law holds for a sequence of pairwise independent and identically distributed integrable random variables: the full independence of Kolmogorov is not needed.

*Proof (sketch).* The maximal inequality of Kolmogorov is replaced by a maximal inequality for pairwise independent variables, valid because the variance of a sum of pairwise independent variables is still the sum of the variances; the truncation argument is then the same. $\square$

**Theorem (converse).** If the $X_n$ are independent and identically distributed with $\mathbb{E}|X_1| = \infty$ then $\limsup_n |\bar X_n| = \infty$ a.s., so the sample mean does not converge.

The strong law is the probabilistic form of the pointwise ergodic theorem, and the correspondence is exact: the Bernoulli shift has i.i.d. coordinates, the time averages of the shift are the sample means, and the ergodic theorem, asserts the same almost-sure convergence for every measure-preserving transformation and every stationary process, with the independence and the identical distribution replaced by stationarity and the mean replaced by the space average.

**Example (Borel's normal numbers).** Let $X_n$ be the $n$-th binary digit of a number $x \in [0,1]$, for $x$ chosen with Lebesgue measure. The digit sequence is i.i.d. Bernoulli$(1/2)$, so by the strong law the frequency of $1$s in the first $n$ digits tends to $1/2$ almost surely; applying the same theorem to the indicators of each finite block of digits shows that the frequency of every block of length $k$ tends to $2^{-k}$. The conclusion is Borel's theorem that almost every real number is normal to base $2$, and the argument extends to every base. Normality is a tail event of the digit sequence, so Kolmogorov's zero–one law already forces its probability to be $0$ or $1$; the strong law identifies it as $1$.

## The Central Limit Theorem

### The Lindeberg–Lévy Theorem

**Theorem (central limit theorem).** Let $X_1, X_2, \dots$ be independent and identically distributed with mean $\mu$ and finite positive variance $\sigma^2$. Then the standardised sums converge in distribution to the standard normal:

$$
Z_n = \frac{S_n - n\mu}{\sigma\sqrt n} \xrightarrow{d} N(0,1).
$$

*Proof.* By Lévy's continuity theorem it suffices to show $\varphi_{Z_n}(t) \to e^{-t^2/2}$ for every $t$. By independence, $\varphi_{Z_n}(t) = \varphi(t/(\sigma\sqrt n))^n$ after centring, and the expansion of the characteristic function of a mean-zero unit-variance variable is

$$
\varphi(u) = 1 - \frac{u^2}{2} + o(u^2) \qquad \text{as } u \to 0,
$$

because $\varphi(u) = \mathbb{E}[1 + iuX_1 - u^2X_1^2/2 + o(u^2))] = 1 - u^2/2 + o(u^2)$. Putting $u = t/(\sigma\sqrt n)$ and raising to the $n$-th power,

$$
\varphi_{Z_n}(t) = \left(1 - \frac{t^2}{2n} + o\!\left(\frac{1}{n}\right)\right)^n \longrightarrow e^{-t^2/2},
$$

which is the characteristic function of $N(0,1)$; the limit is continuous at $0$, so Lévy's theorem applies. $\square$

**Example (de Moivre–Laplace).** For $X_i$ Bernoulli$(p)$ the statement is the convergence of the standardised binomial to the normal: if $S_n \sim \mathrm{Bin}(n,p)$ then $(S_n - np)/\sqrt{np(1-p)} \xrightarrow{d} N(0,1)$. The computation is the case $\sigma^2 = p(1-p)$ of the theorem, and it is the oldest form of the central limit theorem.

### Triangular Arrays and the Lindeberg Condition

**Theorem (Lindeberg–Feller).** For each $n$ let $X_{n,1}, \dots, X_{n,k_n}$ be independent with mean zero and finite variances, let $s_n^2 = \sum_{i} \operatorname{Var}(X_{n,i})$ and let $S_n = \sum_i X_{n,i}$. If the **Lindeberg condition** holds — that for every $\varepsilon > 0$,

$$
\frac{1}{s_n^2}\sum_{i=1}^{k_n}\mathbb{E}\!\left[X_{n,i}^2\,\mathbf{1}_{\{|X_{n,i}| > \varepsilon s_n\}}\right] \longrightarrow 0 \qquad \text{as } n\to\infty \text{ with } s_n\to\infty
$$

— then $S_n/s_n \xrightarrow{d} N(0,1)$. Conversely, if in addition the **Feller condition** $\max_i \operatorname{Var}(X_{n,i})/s_n^2 \to 0$ holds and $S_n/s_n \xrightarrow{d} N(0,1)$, then the Lindeberg condition holds.

The Lindeberg condition says that the individual terms are asymptotically negligible relative to the total fluctuation, and under the Feller condition it is exactly the hypothesis under which the normal law is the limit; when it fails, the limit is one of the stable laws of the next section. The sufficiency is proved by the characteristic-function computation of the i.i.d. case, applied term by term and using the Lindeberg condition to control the tails; the necessity is the statement that any other asymptotic behaviour of the tails prevents the normal limit.

**Corollary (Lyapunov's condition).** If the third absolute moments are finite and satisfy $\sum_i \mathbb{E}|X_{n,i}|^3 = o(s_n^3)$, then the Lindeberg condition holds and the normal limit follows. Lyapunov's condition is the practical sufficient condition, and it is the form in which the theorem is applied to sums of independent but not identically distributed terms.

## Rates and Refinements

### The Berry–Esseen Theorem

**Theorem (Berry–Esseen).** Let $X_1, X_2, \dots$ be independent and identically distributed with mean $\mu$, variance $\sigma^2$ and finite third absolute moment $\rho = \mathbb{E}|X_1 - \mu|^3$. Then there is an absolute constant $C$ with

$$
\sup_{x \in \mathbb{R}}\left|\mathbb{P}(Z_n \leq x) - \Phi(x)\right| \leq \frac{C\rho}{\sigma^3\sqrt n}.
$$

The theorem supplies the rate of the central limit theorem: the Kolmogorov distance between the law of the standardised sum and the normal is $O(n^{-1/2})$, with a constant depending only on the standardised third moment. The order $n^{-1/2}$ is optimal, and the best constant is known to lie between approximately $0.4$ and $0.5$; its exact value is not known. The proof is an application of the smoothing inequality, which compares two distribution functions through the integrals of their characteristic functions against a kernel, together with the estimate of the difference of the characteristic functions by the third-moment bound.

**Theorem (Edgeworth expansion).** Under one extra moment condition the distribution function admits the asymptotic expansion

$$
\mathbb{P}(Z_n \leq x) = \Phi(x) + \frac{\lambda_3}{6\sqrt n}(x^2 - 1)\Phi'(x) + o\!\left(\frac{1}{\sqrt n}\right),
$$

where $\lambda_3 = \mathbb{E}[(X_1-\mu)^3]/\sigma^3$ is the standardised third cumulant, so that the leading correction to the normal is a signed term measuring the skewness and vanishing identically for a symmetric distribution.

The Edgeworth expansion is the systematic refinement of the central limit theorem, and it is the reason the cumulants of *Measure-Theoretic Probability* are the natural coefficients: the term of order $n^{-k/2}$ is a polynomial in the cumulants up to order $k+2$, and the expansion can be carried to any order at which the moments exist.

### The Local Limit Theorem

**Theorem (local limit theorem).** Let $X_n$ be independent and identically distributed lattice-valued random variables with span $1$, mean $\mu$, finite variance $\sigma^2$, and suppose the characteristic function has $|\varphi(t)| < 1$ for $0 < |t| \le \pi$. Then

$$
\sup_{k \in \mathbb{Z}}\left|\sigma\sqrt n\,\mathbb{P}\!\left(\sum_{i=1}^{n}X_i = k\right) - \frac{1}{\sqrt{2\pi}}\,e^{-(k-n\mu)^2/(2n\sigma^2)}\right| \longrightarrow 0.
$$

The local theorem is the strengthening of the central limit theorem from the distribution function to the point probabilities; the hypothesis on the characteristic function excludes the periodic distributions, for which the lattice has a proper sublattice as its support and the local statement holds on that sublattice. The proof is the inversion formula of the characteristic function, applied to the probability of a single value and estimated by splitting the range of integration near $0$ and away from it.

### Large Deviations

**Theorem (Cramér).** Let $X_1, X_2, \dots$ be independent and identically distributed with a finite moment generating function in a neighbourhood of the origin, and let $I(x) = \sup_{t}(tx - \log M(t))$ be the Legendre transform of the cumulant generating function $M(t) = \mathbb{E}[e^{tX_1}]$. Then for $x > \mu$,

$$
\frac{1}{n}\log\mathbb{P}\!\left(\bar X_n \geq x\right) \longrightarrow -I(x) \qquad \text{as } n \to \infty,
$$

and the analogous statement holds for $x < \mu$ with the reflected rate function.

Cramér's theorem describes the probability of a deviation of the mean of order $1$, which lies outside the range of the central limit theorem, and it is the prototype of the large-deviation theory. The rate function $I$ is nonnegative, convex, vanishes exactly at $x = \mu$, and is strictly convex where it is finite; the proof is the exponential version of the Chebyshev inequality — the exponential tilt — together with a lower bound from the change of measure that concentrates the sum at the required value.

## Stable and Infinitely Divisible Laws

### The Lévy–Khintchine Representation

The central limit theorem describes the limit of sums with finite variance. The general question — which laws are the possible limits of sums of independent variables — is answered by the representation theorem of Lévy and Khintchine.

**Definition.** A probability measure $\mu$ is **infinitely divisible** if for every $n$ it is the $n$-fold convolution power of a probability measure. A measure $\mu$ is **stable** with exponent $\alpha \in (0,2]$ if for independent copies $X, X'$ of $\mu$ and all $a, b > 0$ there are $c>0$ and $d \in \mathbb{R}$ with $aX + bX' \stackrel{d}{=} cX + d$.

**Theorem (Lévy–Khintchine).** A probability measure $\mu$ on $\mathbb{R}$ is infinitely divisible if and only if its characteristic function has the form

$$
\varphi(t) = \exp\!\left(i\gamma t - \frac{\sigma^2 t^2}{2} + \int_{\mathbb{R}}\left(e^{itx} - 1 - itx\,\mathbf{1}_{\{|x|\le1\}}\right)\nu(dx)\right)
$$

for a real $\gamma$, a $\sigma^2 \geq 0$ and a measure $\nu$ on $\mathbb{R}\setminus\{0\}$ with $\int \min(1,x^2)\,\nu(dx) < \infty$; the triple $(\gamma,\sigma^2,\nu)$ is unique, and $\nu$ is the **Lévy measure**.

The normal law is the case $\nu = 0$, and the stable laws are the infinitely divisible laws with a scaling property, whose characteristic functions are $e^{-c|t|^\alpha}$ up to drift for $\alpha \neq 1$ and $e^{-c|t|(1 + i\beta\operatorname{sgn}(t)\log|t|)}$ for $\alpha = 1$; they are the only possible limits in the central limit theorem without the finite-variance hypothesis. The Cauchy law is stable with exponent $1$, the normal with exponent $2$, and for $\alpha < 2$ the stable laws have heavy tails $\mathbb{P}(|X| > x) \sim Cx^{-\alpha}$; the classical central limit theorem is the statement that the finite-variance case has exponent $2$ with a finite second moment.

## The Multidimensional and Functional Versions

### The Multivariate Central Limit Theorem

**Theorem (Cramér–Wold).** Let $X_1, X_2, \dots$ be independent and identically distributed random vectors in $\mathbb{R}^d$ with mean $\mu$ and covariance matrix $\Sigma$. Then $\sqrt n(\bar X_n - \mu) \xrightarrow{d} N(0,\Sigma)$; equivalently, for every $a \in \mathbb{R}^d$ the scalar sequence $a \cdot X_i$ satisfies the one-dimensional central limit theorem with variance $a^\top\Sigma a$.

The reduction is the Cramér–Wold device: a sequence of random vectors converges in distribution to a vector $X$ if and only if every linear functional of it converges to the corresponding functional of $X$. The multivariate theorem is therefore a corollary of the one-dimensional theorem, applied to every direction simultaneously, and the covariance matrix is the covariance of the limit.

### The Invariance Principle

**Theorem (Donsker).** Let $X_1, X_2, \dots$ be independent and identically distributed with mean $0$ and variance $\sigma^2$, and for $t \in [0,1]$ let

$$
W_n(t) = \frac{1}{\sigma\sqrt n}\left(S_{\lfloor nt\rfloor} + (nt - \lfloor nt\rfloor)X_{\lfloor nt\rfloor+1}\right)
$$

be the linearly interpolated random walk. Then $W_n$ converges in distribution to standard Brownian motion on $[0,1]$, in the topology of uniform convergence on the space of continuous functions.

Donsker's theorem is the functional form of the central limit theorem, and it is the reason the central limit theorem is only the first of an infinite family of asymptotic statements about the random walk: the partial-sum process itself converges, after rescaling, to a Brownian motion, and every continuous functional of the walk converges to the corresponding functional of Brownian motion. The construction of Brownian motion and the stochastic calculus that this theorem initiates are not covered here, where the invariance principle is developed; the present article records it as the functional closure of the central limit theorem.

## Summary

The characteristic function converts convergence in distribution into pointwise convergence: by Lévy's continuity theorem, if the characteristic functions converge to a function continuous at the origin then the measures converge weakly, and the tail estimate behind the proof is the only technical input. The weak law of large numbers asserts that the sample mean converges in probability to the mean; it follows from Chebyshev's inequality when the variance is finite, with the rate $O(1/n)$, and from Khinchin's truncation argument when only the first moment is finite. The strong law asserts almost-sure convergence; it follows from Kolmogorov's maximal inequality, which is the maximal bound for independent partial sums and the precursor of the martingale maximal inequality, and it holds for pairwise independent variables by Etemadi's refinement and fails exactly when the first moment is infinite. Borel's theorem on normal numbers is the special case of the binary digits.

The central limit theorem asserts that the standardised sums of independent identically distributed variables with finite positive variance converge in distribution to the standard normal, and the proof is the computation $\varphi(t/\sqrt n)^n \to e^{-t^2/2}$ together with Lévy's theorem. The triangular-array version holds exactly under the Lindeberg condition, and the Lyapunov condition is its practical sufficient form. The rate is governed by the Berry–Esseen theorem, of order $n^{-1/2}$ in the Kolmogorov distance with a constant depending on the standardised third moment, with the Edgeworth expansion supplying the successive corrections from the cumulants; the local limit theorem sharpens the convergence to the point probabilities of a lattice law, and Cramér's theorem gives the exponential rate of the large deviations. The possible limits of sums of independent variables are the infinitely divisible laws, represented by the Lévy–Khintchine formula with the triple $(\gamma,\sigma^2,\nu)$, and the stable laws are the limits in the absence of a finite variance. In several dimensions the Cramér–Wold device reduces the theorem to the one-dimensional case, and in the functional setting Donsker's invariance principle upgrades the central limit theorem to the convergence of the rescaled random walk to Brownian motion.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $X_i$, $S_n$, $\bar X_n$ | i.i.d. variables, partial sum, sample mean |
| $\mu$, $\sigma^2$ | Mean and variance of $X_1$ |
| $Z_n = (S_n - n\mu)/(\sigma\sqrt n)$ | Standardised sum |
| $\varphi(t) = \mathbb{E}[e^{itX_1}]$ | Characteristic function |
| $\Phi$, $N(0,1)$ | Standard normal distribution function and law |
| $\xrightarrow{\mathbb{P}}$, $\xrightarrow{d}$, a.s. | Convergence in probability, in distribution, almost surely |
| $\bar X_n \to \mu$ | Weak and strong laws of large numbers |
| Lindeberg condition | asymptotic negligibility of individual terms in a triangular array |
| $\rho = \mathbb{E}\|X_1-\mu\|^3$ | Third absolute moment, in Berry–Esseen |
| $\lambda_3$, Edgeworth | standardised third cumulant, expansion in cumulants |
| $M(t) = \mathbb{E}[e^{tX_1}]$, $I(x)$ | Moment generating function and its Legendre transform (rate function) |
| $(\gamma,\sigma^2,\nu)$ | Lévy–Khintchine triple; $\nu$ the Lévy measure |
| stable law, $\alpha$ | self-similar limit law with exponent $\alpha\in(0,2]$ |
| $W_n(t)$ | Rescaled, interpolated random walk |
| Cramér–Wold | vector convergence tested against all linear functionals |





## Further Reading

- Patrick Billingsley, *Probability and Measure* (Wiley, 3rd edition, 1995), and *Convergence of Probability Measures* (Wiley, 2nd edition, 1999), for the continuity theorem, the laws of large numbers and the invariance principle.
- Kai Lai Chung, *A Course in Probability Theory* (Academic Press, 3rd edition, 2001), for the weak and strong laws, the Kolmogorov maximal inequality and the central limit theorem.
- William Feller, *An Introduction to Probability Theory and Its Applications*, Vol. II (Wiley, 2nd edition, 1971), for the Lindeberg–Feller theorem, the local limit theorem and the infinitely divisible laws.
- Boris V. Gnedenko and Andrey N. Kolmogorov, *Limit Distributions for Sums of Independent Random Variables* (Addison-Wesley, 1954), for the stable laws and the general limit theory.
- Michel Loève, *Probability Theory* (Springer, 4th edition, 1977), for the triangular-array theory and the rates of convergence.
- Andrew C. Berry, "The accuracy of the Gaussian approximation to the sum of independent variates", *Transactions of the American Mathematical Society* 49 (1941), 122–136, and Carl-Gustav Esseen, "On the Liapunov limit of error in the theory of probability", *Arkiv för Matematik, Astronomi och Fysik* 28A (1942), 1–19, for the Berry–Esseen theorem.
- Harald Cramér, "Sur un nouveau théorème-limite de la théorie des probabilités", *Actualités Scientifiques et Industrielles* 736 (1938), 5–23, for the large-deviation theorem.
- Monroe D. Donsker, "Justification and extension of Doob's heuristic approach to the Kolmogorov–Smirnov theorems", *Annals of Mathematical Statistics* 23 (1952), 277–281, for the invariance principle.
