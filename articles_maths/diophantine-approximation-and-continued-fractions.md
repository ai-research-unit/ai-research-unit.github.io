
# __Diophantine Approximation and Continued Fractions__

## Introduction

This is the second article of the Rational Numbers system in Part V, and it occupies the **analysis slot** of that system. The system is the field $\mathbb{Q}$ of *The Rational Numbers*, and the object of study is its approximation theory: how closely a real number can be approximated by rationals, and the continued fractions that furnish the best approximations. Where the algebra slot of the system constructed $\mathbb{Q}$ as the fraction field of $\mathbb{Z}$ and recorded its order and divisibility, this article treats $\mathbb{Q}$ as a dense subset of its completion and asks the analytic question of how well its elements approximate the reals outside it.

The analysis of $\mathbb{Q}$ is unusual among the systems of the ladder, because $\mathbb{Q}$ is not complete and so has no analysis of its own: its sequences, series and integrals all take place in the completion. What the system does support is the *approximation theory* of the completion by the system itself, and that is exactly Diophantine approximation. The relevance of the continued fractions is that they are the extremal instrument of this approximation: the convergents of a real number are its best rational approximations, and they are computed by the Euclidean algorithm of *The Integers* applied to the pair $(\alpha, 1)$.

The real line $\mathbb{R}$ is the completion of $\mathbb{Q}$ for the usual absolute value, constructed in *Metric, Uniform and Complete Spaces* and *Absolute Values, Valuations and Completions*, and its ordered field structure is from *Real-Closed and Complete Ordered Fields*; the arithmetic of $\mathbb{Q}$ and its places are from *The Rational Numbers*. The transcendence of $e$ and $\pi$ and the general theory of algebraic numbers are not used. Throughout, $\alpha$ is a real number, $p/q$ is a rational in lowest terms with $q > 0$, the distance from $\alpha$ to the nearest integer is $\lVert \alpha \rVert$, the continued fraction of $\alpha$ is $[a_0; a_1, a_2, \dots]$ with $a_0 \in \mathbb{Z}$ and $a_i \in \mathbb{N}_{\geq 1}$ for $i \geq 1$, and its convergents are $p_n/q_n$. The golden ratio is $\varphi = (1+\sqrt5)/2$.

## The Rationals and Their Completion

### Density and the Archimedean Property

**Theorem.** $\mathbb{Q}$ is dense in $\mathbb{R}$: for every real $\alpha$ and every $\varepsilon > 0$ there is $q \in \mathbb{Q}$ with $\lvert \alpha - q \rvert < \varepsilon$. Moreover $\mathbb{Q}$ is **Archimedean**: for every real $\alpha$ there is $n \in \mathbb{N}$ with $n > \alpha$.

**Proof.** Density follows from the Archimedean property, which holds in $\mathbb{R}$ as the completion of the Archimedean ordered field $\mathbb{Q}$: given $\alpha$ and $\varepsilon$, choose $n$ with $n\varepsilon > 1$ and then the integer $k = \lfloor n\alpha \rfloor$, so that $\lvert \alpha - k/n\rvert < 1/n < \varepsilon$. $\square$

**Remark.** Density gives approximations of order $1/q$ in the denominator, since the nearest rational with denominator $q$ is within $1/(2q)$ of any real. The Dirichlet theorem below shows that the irrationals admit approximations of order $1/q^2$, and the whole of Diophantine approximation is the study of how much better the order can be, and for which $\alpha$.

### The Two Completions

**Theorem (Ostrowski).** Every nontrivial absolute value on $\mathbb{Q}$ is equivalent either to the usual absolute value $\lvert\cdot\rvert_\infty$ or to a $p$-adic absolute value $\lvert\cdot\rvert_p$ for a prime $p$. The completion for $\lvert\cdot\rvert_\infty$ is $\mathbb{R}$; the completion for $\lvert\cdot\rvert_p$ is the field $\mathbb{Q}_p$ of $p$-adic numbers.

**Proof.** The classification is Ostrowski's theorem, proved in *Absolute Values, Valuations and Completions*; the completions are constructed there and in *Metric, Uniform and Complete Spaces*. $\square$

**Corollary (product formula).** For every nonzero rational $x$,

$$
\lvert x \rvert_\infty \prod_p \lvert x \rvert_p = 1 .
$$

**Proof.** Both sides are multiplicative, and it suffices to check the formula for $x = \pm p$; the left side is $p \cdot (1/p) = 1$. $\square$

**Remark.** The product formula is the arithmetic expression of the fact that $\mathbb{Q}$ has one Archimedean place and one place for each prime, and it is the origin of the parallel between Diophantine approximation in $\mathbb{R}$ and in the $p$-adic fields. The present article treats the Archimedean place, where the continued fractions live; the non-Archimedean approximation is developed with the $p$-adic analysis of Part III.

## Diophantine Approximation

### Dirichlet's Theorem

**Theorem (Dirichlet).** For every real $\alpha$ and every integer $N \geq 1$ there are $p \in \mathbb{Z}$ and $q \in \mathbb{N}$ with $1 \leq q \leq N$ and

$$
\lvert q\alpha - p \rvert < \frac{1}{N} .
$$

Consequently there are infinitely many $p/q$ with

$$
\left\lvert \alpha - \frac{p}{q} \right\rvert < \frac{1}{q^2} .
$$

**Proof.** Consider the $N+1$ fractional parts $\{0\}, \{\alpha\}, \dots, \{N\alpha\}$ in $[0,1)$, partitioned into $N$ intervals of length $1/N$. Two of them lie in the same interval, say $0 \leq i < j \leq N$; then $\lvert (j-i)\alpha - k\rvert < 1/N$ for $k = \lfloor j\alpha\rfloor - \lfloor i\alpha\rfloor$, giving the first statement with $q = j-i$ and $p = k$. For the second, apply the first with $N$ arbitrary and note that $q \leq N$ gives $1/(qN) \leq 1/q^2$; repeating with larger $N$ produces infinitely many distinct fractions, since a fixed $p/q$ satisfies $\lvert q\alpha - p\rvert \geq c > 0$ for irrational $\alpha$. $\square$

**Corollary.** For every irrational $\alpha$ the inequality $\lvert \alpha - p/q \rvert < 1/q^2$ has infinitely many solutions; and for almost every $\alpha$ in the sense of Lebesgue measure, the sharper inequality $\lvert \alpha - p/q\rvert < 1/(q^2\log q)$ has infinitely many solutions while $\lvert \alpha - p/q\rvert < 1/(q^2\log^{1+\varepsilon}q)$ has only finitely many for every $\varepsilon > 0$. This is Khintchine's theorem on the metric theory of Diophantine approximation.

### The Theorem of Hurwitz

**Definition.** An irrational $\alpha$ is **badly approximable** if there is $c > 0$ such that $\lvert \alpha - p/q \rvert > c/q^2$ for all $p/q$. The Lagrange constant of $\alpha$ is $\liminf_{q\to\infty} q\lVert q\alpha\rVert$.

**Theorem (Hurwitz).** For every irrational $\alpha$ there are infinitely many $p/q$ with

$$
\left\lvert \alpha - \frac{p}{q} \right\rvert < \frac{1}{\sqrt5\, q^2} .
$$

The constant $\sqrt5$ is best possible: for $\alpha = \varphi = (1+\sqrt5)/2$ and every $c > \sqrt5$, the inequality $\lvert \varphi - p/q\rvert < 1/(c q^2)$ has only finitely many solutions. Thus $\varphi$ is badly approximable and its Lagrange constant is $1/\sqrt5$.

**Proof.** Since $\alpha$ lies between consecutive convergents, the determinant identity gives

$$
\left\lvert \alpha - \frac{p_n}{q_n} \right\rvert + \left\lvert \alpha - \frac{p_{n+1}}{q_{n+1}} \right\rvert = \left\lvert \frac{p_n}{q_n} - \frac{p_{n+1}}{q_{n+1}} \right\rvert = \frac{1}{q_n q_{n+1}} .
$$

If both terms were at least $1/(\sqrt5 q_n^2)$ and $1/(\sqrt5 q_{n+1}^2)$ respectively, then with $t = q_{n+1}/q_n$ one would get $\sqrt5 \geq t + 1/t$, that is $t \in [1/\varphi, \varphi]$. But the ratios satisfy $t_{n+1} = a_{n+2} + 1/t_n \geq 1 + 1/t_n$, so $t_n \leq \varphi$ forces $t_{n+1} \geq \varphi$, with equality only when $t_n = \varphi$ and $a_{n+2} = 1$; hence the failures cannot occur at every index, and infinitely many convergents satisfy the bound. For $\alpha = \varphi$ all partial quotients are $1$, every ratio tends to $\varphi$, and a direct computation with $\varphi^2 = \varphi + 1$ gives $\lim q_n^2\lvert \varphi - p_n/q_n\rvert = 1/\sqrt5$, so no larger constant can replace $\sqrt5$. The computation is Hurwitz's; the details are in the references. $\square$

### Liouville Numbers and Roth's Theorem

**Definition.** A real $\alpha$ is a **Liouville number** if for every $n$ there is a rational $p/q$ with

$$
0 < \left\lvert \alpha - \frac{p}{q} \right\rvert < \frac{1}{q^n} .
$$

**Theorem (Liouville).** If $\alpha$ is algebraic of degree $n \geq 2$ over $\mathbb{Q}$, then there is $c > 0$ such that

$$
\left\lvert \alpha - \frac{p}{q} \right\rvert > \frac{c}{q^n}
$$

for every rational $p/q$. Consequently no algebraic irrational is a Liouville number, and every Liouville number is transcendental.

**Proof.** Let $f$ be the minimal polynomial of $\alpha$ over $\mathbb{Z}$, of degree $n$, and let $M$ bound $\lvert f'\rvert$ on the interval between $\alpha$ and the rational. If $p/q$ is close to $\alpha$ then $q^n f(p/q)$ is a nonzero integer, so $\lvert q^n f(p/q)\rvert \geq 1$; the mean value theorem gives $\lvert f(p/q)\rvert \leq M\lvert \alpha - p/q\rvert$, hence $\lvert \alpha - p/q\rvert \geq 1/(Mq^n)$. The last statement follows because a Liouville number has approximations beating every power $q^{-n}$, which an algebraic irrational cannot have. $\square$

**Example.** The number $\alpha = \sum_{k\geq 1} 10^{-k!}$ is a Liouville number: the truncations $p/q$ with $q = 10^{m!}$ approximate $\alpha$ with error $O(q^{-(m+1)})$, which beats every power. Hence $\alpha$ is transcendental, and this is Liouville's original construction of a transcendental number.

**Theorem (Roth).** If $\alpha$ is an algebraic irrational and $\varepsilon > 0$, then

$$
\left\lvert \alpha - \frac{p}{q} \right\rvert > \frac{1}{q^{2+\varepsilon}}
$$

for all but finitely many $p/q$.

**Proof.** Roth's theorem is the sharp form of Liouville's bound: the exponent $n$ of the degree is replaced by $2 + \varepsilon$, and the theorem is best possible in the sense that the exponent $2$ cannot be attained. The proof is Roth's and is outside the scope of this article; it is given in the references. $\square$

**Remark.** The Dirichlet theorem, Liouville's theorem and Roth's theorem together bracket the approximation exponent of an algebraic irrational between $2$ and $2 + \varepsilon$: every irrational has infinitely many approximations of order $2$, no algebraic irrational admits approximations of order $2 + \varepsilon$, and whether a given $\alpha$ has approximations of order exactly $2$ is the question of whether $\alpha$ is badly approximable, for which the continued fractions give the criterion.

## Continued Fractions

### Finite Continued Fractions

**Definition.** A **finite continued fraction** is an expression

$$
[a_0; a_1, \dots, a_n] = a_0 + \cfrac{1}{a_1 + \cfrac{1}{a_2 + \cdots + \cfrac{1}{a_n}}},
$$

with $a_0 \in \mathbb{Z}$, $a_i \in \mathbb{N}_{\geq 1}$ for $i \geq 1$, and $a_n \geq 2$ when $n \geq 1$ for uniqueness. Its value is a rational number.

**Theorem.** Every rational number has a finite continued fraction, unique under the stated conditions, obtained by the Euclidean algorithm: if $r_0 = r$, $r_{k+1} = 1/(r_k - \lfloor r_k\rfloor)$ and $a_k = \lfloor r_k \rfloor$, the algorithm terminates and $r = [a_0; a_1, \dots, a_n]$.

**Proof.** The algorithm is the Euclidean algorithm of *The Integers* applied to the numerator and denominator: the pair $(p, q)$ is replaced by $(q, p \bmod q)$, and the remainders strictly decrease, so the algorithm terminates after finitely many steps. Reading the quotients in reverse gives the continued fraction. $\square$

**Definition.** For an infinite continued fraction $[a_0; a_1, a_2, \dots]$ the **convergents** are the rationals

$$
\frac{p_n}{q_n} = [a_0; a_1, \dots, a_n], \qquad p_{-2} = 0,\ p_{-1} = 1,\ q_{-2} = 1,\ q_{-1} = 0,
$$

defined for $n \geq 0$ by the recurrences

$$
p_n = a_n p_{n-1} + p_{n-2}, \qquad q_n = a_n q_{n-1} + q_{n-2}.
$$

**Theorem.** The convergents satisfy

$$
p_n q_{n-1} - p_{n-1} q_n = (-1)^{n-1}, \qquad p_n q_{n-2} - p_{n-2} q_n = (-1)^n a_n,
$$

so that $p_n$ and $q_n$ are coprime, and for every $n$,

$$
\left\lvert \alpha - \frac{p_n}{q_n} \right\rvert < \frac{1}{q_n q_{n+1}} < \frac{1}{q_n^2} .
$$

**Proof.** The determinant identities are inductions on $n$ from the recurrences; the coprimality is the first identity. The estimate follows from the identity

$$
\alpha - \frac{p_n}{q_n} = \frac{(-1)^n}{q_n}\cdot\frac{1}{q_n \alpha_{n+1} + q_{n-1}}, \qquad \alpha_{n+1} = [a_{n+1}; a_{n+2}, \dots] > 1,
$$

which is obtained by iterating the transformation $\alpha = a_0 + 1/\alpha_1$. $\square$

### The Best Approximation Property

**Theorem.** The convergents are the best approximations: if $p/q$ is a rational with $0 < q \leq q_n$ and $p/q \neq p_n/q_n$, then

$$
\lvert q\alpha - p \rvert > \lvert q_n \alpha - p_n \rvert, \qquad \text{so in particular} \qquad \left\lvert \alpha - \frac{p}{q} \right\rvert > \left\lvert \alpha - \frac{p_n}{q_n} \right\rvert .
$$

**Proof.** If $p/q$ lies strictly between the convergents $p_{n-1}/q_{n-1}$ and $p_n/q_n$ then $q \geq q_n + q_{n-1} > q_n$, and otherwise $\lvert q\alpha - p\rvert \geq \lvert q_n\alpha - p_n\rvert$ by a direct estimate using the determinant identity; the standard argument is in the references. $\square$

**Corollary.** Every rational with $\lvert \alpha - p/q\rvert < 1/(2q^2)$ is a convergent of $\alpha$, so the approximations of Dirichlet and Hurwitz are always found among the convergents.

### Infinite Continued Fractions and Quadratic Irrationals

**Theorem.** Every irrational $\alpha$ has a unique infinite continued fraction $[a_0; a_1, a_2, \dots]$, and the convergents converge to $\alpha$:

$$
\alpha = \lim_{n\to\infty} \frac{p_n}{q_n}, \qquad \left\lvert \alpha - \frac{p_n}{q_n} \right\rvert < \frac{1}{q_n q_{n+1}} .
$$

The map $\alpha \mapsto (a_0, a_1, a_2, \dots)$ is a bijection from the irrationals to the sequences with $a_i \geq 1$ for $i \geq 1$, and $\alpha$ is rational exactly when its expansion is finite.

**Proof.** Since $q_n \geq q_{n-1} + q_{n-2}$, the denominators grow at least as fast as the Fibonacci numbers, so $q_n \to \infty$ and the estimate of the preceding theorem shows that the convergents are Cauchy; their limit $\alpha$ is irrational if the expansion is infinite, and the uniqueness of the expansion follows by induction from the uniqueness of the integer part. $\square$

**Theorem (Lagrange).** An irrational $\alpha$ is a quadratic irrational, that is, $\alpha$ satisfies a quadratic equation over $\mathbb{Q}$, if and only if its continued fraction is eventually periodic.

**Proof.** If the expansion is eventually periodic then $\alpha$ is fixed by a fractional linear transformation with integer coefficients, hence satisfies a quadratic equation. Conversely, if $\alpha$ is a root of an integer quadratic then the complete quotients $\alpha_n$ all lie in the same finite set of quadratic irrationals of bounded height, so two of them coincide and the expansion repeats. The argument is Lagrange's; the details are in the references. $\square$

**Example.** $\sqrt2 = [1; 2, 2, 2, \dots]$ with convergents $1, 3/2, 7/5, 17/12, \dots$, all of them solving the Pell equation $x^2 - 2y^2 = \pm 1$; and $\varphi = [1; 1, 1, 1, \dots]$ with convergents $F_{n+1}/F_n$ the ratios of consecutive Fibonacci numbers. The number $e$ has the non-periodic expansion $[2; 1, 2, 1, 1, 4, 1, 1, 6, \dots]$, which shows that eventual periodicity genuinely characterises the quadratic irrationals.

### Pell's Equation

**Theorem.** Let $D$ be a positive nonsquare integer. The equation $x^2 - Dy^2 = 1$ has infinitely many solutions in integers, all obtained from the convergents of $\sqrt D$; if the period of the continued fraction of $\sqrt D$ is $\ell$, then the fundamental solution is $p_{\ell-1} + q_{\ell-1}\sqrt D$ when $\ell$ is even and $p_{2\ell-1} + q_{2\ell-1}\sqrt D$ when $\ell$ is odd, and every solution is a power of the fundamental one in $\mathbb{Z}[\sqrt D]$.

**Proof.** The periodicity of the expansion of the quadratic irrational $\sqrt D$ is Lagrange's theorem; substituting the periodic tail into the transformation $\alpha = a_0 + 1/\alpha_1$ gives a quadratic equation whose solutions are units of norm $1$ in $\mathbb{Z}[\sqrt D]$, that is, solutions of the Pell equation. The powers of the fundamental unit give all solutions because the units of $\mathbb{Z}[\sqrt D]$ form a cyclic group up to sign. The argument is standard and is in the references. $\square$

**Example.** For $D = 2$ the period of $\sqrt2$ is $1$ and the fundamental solution is $3 + 2\sqrt2$, giving $3^2 - 2\cdot 2^2 = 1$; its powers $17 + 12\sqrt2$, $99 + 70\sqrt2, \dots$ give the whole solution set. For $D = 61$ the fundamental solution is $1766319049 + 226153980\sqrt{61}$, which shows that the size of the fundamental solution is not controlled by $D$.

## The Gauss Map and the Metric Theory

### The Gauss Map

**Definition.** The **Gauss map** is

$$
T : (0,1) \longrightarrow [0,1), \qquad T(x) = \frac{1}{x} - \left\lfloor \frac{1}{x} \right\rfloor = \left\{ \frac{1}{x} \right\}, \qquad T(0) = 0 .
$$

The continued fraction digits of $x \in (0,1)$ are the successive integer parts of the iterates: with $x_0 = x$, $x_{n+1} = T(x_n)$ and $a_{n+1} = \lfloor 1/x_n \rfloor$, one has $x = [0; a_1, a_2, \dots]$.

**Theorem (Gauss measure).** The measure

$$
d\mu = \frac{1}{\log 2}\,\frac{dx}{1+x}
$$

is $T$-invariant, $\mu(T^{-1}A) = \mu(A)$ for every measurable $A$, and it is ergodic with respect to $T$.

**Proof.** For an interval $[0,t]$ one computes $T^{-1}([0,t]) = \bigcup_{k \geq 1} [1/(k+t), 1/k]$ and verifies $\mu(T^{-1}([0,t])) = \mu([0,t])$ by the telescoping of $\log(1 + 1/k)$; the intervals generate the Borel sets, so the measure is invariant, and the ergodicity is proved by showing that the only invariant functions are constant, using the decay of the iterates. The computation is Gauss's and the ergodicity is standard; both are in the references. $\square$

**Theorem (equidistribution and the Gauss–Kuzmin law).** For almost every $x \in (0,1)$ with respect to Lebesgue measure, and for every interval $A$, the visit frequencies of the orbit of $x$ under the Gauss map tend to $\mu(A)$. In particular the digit distribution converges: for each $k \geq 1$,

$$
\lim_{n\to\infty} \frac{1}{n}\#\{i \leq n : a_i = k\} = \mu\left(\left[\frac{1}{k+1}, \frac{1}{k}\right]\right) = \frac{1}{\log 2}\log\left(1 + \frac{1}{k(k+2)}\right),
$$

with the error in the approximation $\mu(T^{-n}([0,t])) = \log(1+t)/\log 2 + O(\lambda^n)$ for some $\lambda < 1$.

**Proof.** The limit of the frequencies is the Birkhoff ergodic theorem applied to the indicator of the interval, and the identification of the limit with the Gauss measure is the invariance; the exponential error is the Gauss–Kuzmin theorem, proved by the bounded distortion of the inverse branches of $T$ and a contraction argument on the space of densities. The details are in *Measure Theory and Integration* and in the references. $\square$

### The Constrained Averages

**Theorem (Khinchin's constant).** For almost every $x$ the geometric mean of the partial quotients converges:

$$
\lim_{n\to\infty} (a_1 a_2 \cdots a_n)^{1/n} = K_0, \qquad K_0 = \prod_{k=1}^{\infty}\left(1 + \frac{1}{k(k+2)}\right)^{\log_2 k} = 2.6854520010\dots .
$$

**Theorem (Lévy's constant).** For almost every $x$ the denominators of the convergents grow exponentially:

$$
\lim_{n\to\infty} q_n^{1/n} = e^{\pi^2/(12\log 2)} = 3.2758229187\dots .
$$

**Proof.** Both statements are the ergodic theorem applied to the functions $\log a_1$ and $\log q_1$, whose almost-everywhere constancy is the ergodicity of the Gauss map; the evaluation of the integrals gives the constants. The results are Khinchin's and Lévy's and are in the references. $\square$

**Theorem (Borel).** The set of $x \in (0,1)$ for which the digit frequencies exist and equal the Gauss–Kuzmin values has full Lebesgue measure; the continued fraction expansion is therefore "normal" for almost every $x$.

**Proof.** The ergodicity of the Gauss map gives the existence of the frequencies on a full-measure set, and the identification of the limits with the Gauss measure gives the values; the argument is Borel's normal number theorem, applied to the sequence of digits. $\square$

### The Lagrange Spectrum

**Theorem.** An irrational $\alpha$ is badly approximable if and only if its continued fraction has bounded partial quotients. Consequently the set of badly approximable numbers has Lebesgue measure zero, and the Lagrange constants of the badly approximable numbers form the **Lagrange spectrum**, a closed subset of $(0, \tfrac{1}{\sqrt5}]$ whose largest element is $1/\sqrt5$, attained only by the golden ratio and its images, and whose structure near that value is the Markov spectrum.

**Proof.** If the partial quotients are bounded by $M$, the estimate $q_{n+1} \leq (M+1)q_n$ bounds the ratio and the approximation constant from below; conversely a large partial quotient produces an unusually good approximation, so an unbounded expansion cannot be badly approximable. The measure-zero statement follows from the Gauss–Kuzmin law, and the structure of the spectrum is the classical theory of Markov; the details are in the references. $\square$

**Remark.** The Gauss map converts the arithmetic of the continued fraction into the ergodic theory of an expanding map of the interval, and the consequence is that almost every real number has a completely determined digit statistics while the exceptional set — the badly approximable numbers, containing the golden ratio and all the quadratic irrationals — carries the extremal approximation behaviour. This is the exact sense in which Diophantine approximation is a metric theory with an arithmetic skeleton: the typical $\alpha$ is described by the Gauss measure, and the extremal $\alpha$ is described by the continued fraction alone.

## Summary

$\mathbb{Q}$ is dense and Archimedean in its completions, and by Ostrowski's theorem its nontrivial absolute values are the usual one and the $p$-adic ones, with $\mathbb{R}$ and $\mathbb{Q}_p$ as completions and the product formula $\lvert x\rvert_\infty\prod_p \lvert x\rvert_p = 1$ linking them. Diophantine approximation studies the Archimedean place: Dirichlet's pigeonhole theorem gives infinitely many rationals with $\lvert \alpha - p/q\rvert < 1/q^2$ for every irrational $\alpha$; Hurwitz's theorem improves the constant to $1/(\sqrt5 q^2)$ and the constant is best possible, attained by the golden ratio, which is the worst approximable irrational. Liouville's theorem bounds the approximation of an algebraic irrational of degree $n$ below by $c/q^n$, which exhibits the Liouville numbers as transcendental, and Roth's theorem sharpens the bound to $c/q^{2+\varepsilon}$ for every $\varepsilon > 0$.

Continued fractions are the extremal instrument of the theory: finite continued fractions are the Euclidean algorithm in another notation, the convergents satisfy the recurrence $p_n = a_np_{n-1} + p_{n-2}$, $q_n = a_nq_{n-1}+q_{n-2}$ and the determinant identity $p_nq_{n-1} - p_{n-1}q_n = (-1)^{n-1}$, and they are the best approximations of the second kind, with $\lvert \alpha - p_n/q_n\rvert < 1/(q_nq_{n+1})$. Every irrational has a unique infinite expansion, and by Lagrange's theorem the expansion is eventually periodic exactly for the quadratic irrationals; the periodicity solves Pell's equation, whose solutions are the powers of the fundamental unit of $\mathbb{Z}[\sqrt D]$. The analysis slot of the system $\mathbb{Q}$ is thus the theory of its approximation by its own elements, and it is the point at which the arithmetic of the field becomes a question of real analysis.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{Q}$ | The rational numbers |
| $\mathbb{R}$ | The completion of $\mathbb{Q}$ for $\lvert\cdot\rvert_\infty$ |
| $\lvert\cdot\rvert_p$, $\lvert\cdot\rvert_\infty$ | $p$-adic and usual absolute values |
| $\mathbb{Q}_p$ | The $p$-adic numbers, completion for $\lvert\cdot\rvert_p$ |
| $p/q$ | Rational in lowest terms, $q > 0$ |
| $\lVert \alpha\rVert$ | Distance from $\alpha$ to the nearest integer |
| $\varphi$ | Golden ratio $(1+\sqrt5)/2$ |
| $[a_0; a_1, a_2, \dots]$ | Continued fraction |
| $p_n/q_n$ | $n$-th convergent |
| $a_n$ | Partial quotients |
| $\alpha_n$ | Complete quotients $[a_n; a_{n+1}, \dots]$ |
| $c$, $\varepsilon$ | Approximation constants and exponent |
| $T(x)$ | Gauss map, $T(x) = 1/x - \lfloor 1/x\rfloor$ on $(0,1]$ |
| $\mu$ | Gauss measure, $d\mu = \frac{1}{\log 2}\frac{dx}{1+x}$ |
| $K_0$ | Khinchin's constant, $2.6854520010\dots$ |
| $D$ | Positive nonsquare integer in Pell's equation |

## Further Reading

- Wolfgang M. Schmidt, *Diophantine Approximation* (Springer, 1980), for a systematic treatment of approximation constants, Roth's theorem and its generalisations.
- John W. S. Cassels, *An Introduction to Diophantine Approximation* (Cambridge University Press, 1957), for Dirichlet's and Hurwitz's theorems and the classical bounds.
- Serge Lang, *Introduction to Diophantine Approximations* (Springer, 2nd ed. 1995), for Liouville numbers, Roth's theorem and the approximation of algebraic numbers.
- G. H. Hardy and E. M. Wright, *An Introduction to the Theory of Numbers* (Oxford University Press, 6th ed. 2008), for continued fractions, their convergence and Pell's equation.
- Andrew M. Rockett and Peter Szüsz, *Continued Fractions* (World Scientific, 1992), for the recurrence relations, the best approximation property and the periodicity theorem.
- Aleksandr Ya. Khinchin, *Continued Fractions* (University of Chicago Press, 1964), for the metric theory, the Gauss map and the measure-theoretic results.
- Michel Waldschmidt, *Diophantine Approximation on Linear Algebraic Groups* (Springer, 2000), for the modern transcendence-theoretic developments.
