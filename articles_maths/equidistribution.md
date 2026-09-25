
# __Equidistribution__

## Introduction

A sequence of points in a compact space is equidistributed when every region receives its fair share of the sequence, in the limit and in the mean. The notion is the quantitative and sequential companion of the ergodic theorem: where the ergodic theorem averages a function along the orbit of a measure-preserving transformation, equidistribution averages the point masses along a sequence, and where the ergodic theorem needs an invariant measure, equidistribution needs a prescribed one. The two are linked by the *unique ergodicity* of a topological dynamical system — a system with exactly one invariant measure is equidistributed along every orbit — and by the mean ergodic theorem, which for a uniquely ergodic system converts the spatial average into the temporal one.

The subject has two sources. The first is the arithmetic of fractional parts: Weyl's theorem that a polynomial sequence with an irrational coefficient is equidistributed modulo one, and the quantitative discrepancy estimates that measure how fast. The second is homogeneous dynamics: the horocycle orbits of *Homogeneous Dynamics* and the unipotent orbits of *Ratner's Theorems* are equidistributed in their closures, and the theorems there are exactly the statements that make the orbits of a flow equidistribute. The two sources meet in the harmonic-analytic criterion for equidistribution: a sequence on a compact abelian group is equidistributed if and only if its averages against every character tend to the integral of the character, and this criterion is the harmonic analysis of the first articles of the category applied to a sequence.

This article develops the notion and its principal theorems: the definition, Weyl's criterion via characters and matrix coefficients, Weyl's theorem for polynomial sequences, the discrepancy and the Erdős–Turán inequality, the equidistribution of horocycle and unipotent orbits with the quantitative versions, the relation to unique ergodicity, and the almost periodic theory that supplies the mean. Three boundaries are held.

- The **homogeneous flows** — the geodesic and horocycle flows, the nilmanifolds, the ergodic and mixing theorems — are *Homogeneous Dynamics*, and the **classification** of unipotent orbit closures and invariant measures is *Ratner's Theorems*; this article uses both and concentrates on the *distributions* of sequences and orbits and on the quantitative estimates.
- The **harmonic analysis** used in the criteria is the first articles of the category: the dual group $G^\vee$ and the characters of *Harmonic Analysis on Groups*, the matrix coefficients and the orthogonality of *Analysis on Compact Groups*. The **ergodic theory** is *Ergodic Theory of Group Actions*.
- The **specific systems** — the distribution of the fractional parts of a particular algebraic number, the equidistribution of the primes, and the equidistribution on a number system — belong to Part V, where the arithmetic functions are developed; this article states the general theorems and defers the applications. No physics is invoked.

Throughout, $X$ is a compact metric space with a Borel probability measure $\mu$, and a sequence $(x_n)_{n\geq1}$ in $X$ is **equidistributed** (or **uniformly distributed**) with respect to $\mu$ if

$$
\frac{1}{N}\sum_{n=1}^{N} f(x_n) \longrightarrow \int_X f \, d\mu \qquad \text{for every } f \in C(X),
$$

the limit being as $N\to\infty$. For $X = [0,1)$ the measure is Lebesgue measure and the notation $\{x\}$ is the fractional part; for a compact group $K$ the reference measure is the normalised Haar measure $dk$ of *Analysis on Compact Groups*. The notation $\chi$, $K^\vee$ or $G^\vee$, $\operatorname{Irr}(K)$, and the Fourier transform are those of the first articles of the category.

## Equidistribution of Sequences

### The Definition and Its First Form

**Definition.** Let $X$ be a compact metric space with a Borel probability measure $\mu$. A sequence $(x_n)$ in $X$ is **equidistributed** with respect to $\mu$ if the empirical measures

$$
\mu_N = \frac{1}{N}\sum_{n=1}^{N}\delta_{x_n}
$$

converge weakly to $\mu$: $\int f\,d\mu_N \to \int f\,d\mu$ for every $f \in C(X)$.

Weak convergence against all continuous functions is equivalently tested against a convergence-determining class, and the character criterion below reduces it to the harmonic analysis of $X$ when $X$ is a group. On the circle $[0,1) = \mathbb{R}/\mathbb{Z}$ the condition says that the asymptotic proportion of the first $N$ points lying in an interval $[a,b)$ tends to $b-a$ for every interval; equidistribution is a statement about the limit of the empirical distribution, and the speed of the convergence is measured by the discrepancy.

**Example (rational rotation).** The sequence $x_n = n\alpha$ with $\alpha = p/q$ rational is periodic of period $q$, and its empirical measures converge to the uniform measure on the finite set $\{0, 1/q, \dots, (q-1)/q\}$, not to Lebesgue measure; the sequence is not equidistributed. The failure is the arithmetic content of the notion: equidistribution of $n\alpha$ will require $\alpha$ irrational.

### Weyl's Criterion

**Theorem (Weyl's criterion).** A sequence $(x_n)$ in $[0,1)$ is equidistributed if and only if for every nonzero integer $k$,

$$
\frac{1}{N}\sum_{n=1}^{N} e^{2\pi i k x_n} \longrightarrow 0 \qquad \text{as } N \to \infty.
$$

*Proof.* If the sequence is equidistributed, the average of the continuous function $x\mapsto e^{2\pi ikx}$ tends to its integral, which is $0$ for $k \neq 0$. Conversely, the exponentials with $k \in \mathbb{Z}$ span a self-adjoint algebra of functions separating points, so by the Stone–Weierstrass theorem they are dense in $C([0,1))$, and the hypothesis tested against them extends to every continuous function. $\square$

The criterion is the $\mathbb{R}/\mathbb{Z}$ case of the general statement on a compact group, and it is the reason equidistribution is a chapter of harmonic analysis.

**Theorem (Weyl's criterion on a compact group).** Let $K$ be a compact group with normalised Haar measure $dk$ and let $(x_n)$ be a sequence in $K$. Then $(x_n)$ is equidistributed if and only if

$$
\frac{1}{N}\sum_{n=1}^{N} \pi_{ij}(x_n) \longrightarrow \int_K \pi_{ij}(k)\, dk = 0 \qquad \text{for every } \pi \in \operatorname{Irr}(K),\ i,j,
$$

where $\pi_{ij}$ are the matrix coefficients of $\pi$; equivalently, if and only if $\frac{1}{N}\sum_n \pi(x_n) \to 0$ in each irreducible representation $\pi$ other than the trivial one, and the trivial representation contributes $\frac{1}{N}\sum_n 1 = 1$.

*Proof.* The matrix coefficients span the representative-function algebra $A(K)$, which is dense in $C(K)$ by the Peter–Weyl theorem of *The Peter–Weyl Theorem*; testing against a dense subalgebra suffices. The integral of a nontrivial matrix coefficient is $0$ by the orthogonality relations of *Analysis on Compact Groups*. $\square$

**Corollary (abelian case).** For a compact abelian group $K$ the criterion reduces to testing against the characters: $(x_n)$ is equidistributed if and only if $\frac{1}{N}\sum_n \chi(x_n) \to 0$ for every nontrivial character $\chi \in K^\vee$. This is the Pontryagin-dual form of Weyl's criterion, and on $K = \mathbb{R}/\mathbb{Z}$ it is the statement above.

### The Circle and the Torus

**Example ($\{n\alpha\}$).** For irrational $\alpha$ the sequence $x_n = n\alpha$ is equidistributed on $[0,1)$. By Weyl's criterion it suffices to show $\frac{1}{N}\sum_{n=1}^N e^{2\pi i kn\alpha} \to 0$ for $k \neq 0$; the sum is the geometric series

$$
\frac{1}{N}\sum_{n=1}^{N} \zeta^n = \frac{\zeta(1-\zeta^N)}{N(1-\zeta)}, \qquad \zeta = e^{2\pi i k\alpha} \neq 1,
$$

whose modulus is at most $\frac{1}{N}\cdot\frac{2}{|1-\zeta|}$, which tends to $0$ as $N\to\infty$. The irrationality of $\alpha$ is exactly what makes $\zeta \neq 1$ for every $k \neq 0$.

**Example (the torus).** Let $\alpha = (\alpha_1, \dots, \alpha_d) \in \mathbb{R}^d$ and let $x_n = n\alpha$ modulo $\mathbb{Z}^d$. The sequence is equidistributed in $T^d$ if and only if $1, \alpha_1, \dots, \alpha_d$ are rationally independent. The criterion is the same: the characters of $T^d$ are $\chi_m(x) = e^{2\pi i \langle m, x\rangle}$, and the average is a geometric series that vanishes unless $\langle m, \alpha\rangle \in \mathbb{Z}$; the rational-independence condition excludes the latter for every nonzero $m$. This is the sequential form of the ergodicity of the translation of a torus in *Ergodic Theory of Group Actions*, and the two statements are the same harmonic computation.

## Weyl's Theorem for Polynomial Sequences

### Polynomials with an Irrational Coefficient

**Theorem (Weyl).** Let $p(n) = \alpha_k n^k + \alpha_{k-1} n^{k-1} + \cdots + \alpha_1 n + \alpha_0$ be a real polynomial of degree $k \geq 1$. If at least one of the coefficients $\alpha_1, \dots, \alpha_k$ is irrational, then the sequence $\{p(n)\}$ is equidistributed modulo $1$.

The theorem contains the linear case and is proved by an induction on the degree that reduces the degree by differencing. The essential step is the estimate of van der Corput, which converts the exponential sum of degree $k$ into an average of sums of degree $k-1$.

**Lemma (van der Corput).** For complex numbers $z_1, \dots, z_N$ with $|z_n| \leq 1$ and any $H$ with $1 \le H \le N$,

$$
\left|\frac{1}{N}\sum_{n=1}^{N} z_n\right|^2 \le \frac{1}{N}\sum_{h=0}^{H-1}\Bigl(1 - \frac{h}{H}\Bigr)\left|\frac{1}{N}\sum_{n=1}^{N-h} z_{n+h}\overline{z_n}\right| + \frac{2H}{N} + \frac{1}{H}.
$$

Applied with $z_n = e^{2\pi i p(n)}$ the product $z_{n+h}\overline{z_n}$ is the exponential of a polynomial of degree $k-1$ in $n$, so the estimate reduces the degree by one and the induction can proceed; the final step is the geometric series of the linear case. The reader will recognise the inequality as an averaging form of the Cauchy–Schwarz inequality, and it is the standard tool of the subject.

**Corollary.** For irrational $\alpha$ and any $k \geq 1$ the sequence $\{\alpha n^k\}$ is equidistributed; in particular $\{n^2\alpha\}$ is equidistributed, a statement that has no elementary proof of the same simplicity as the linear case. The corollary is the classical equidistribution of the fractional parts of a quadratic polynomial, and it is the base of the applications to the distribution of lattice points on circles and to the Waring problem.

### Sequences on Nilmanifolds

**Theorem (Green–Tao).** Let $N$ be a connected simply connected nilpotent Lie group with a lattice $\Gamma$, and let $g : \mathbb{Z} \to N$ be a polynomial sequence — that is, a sequence whose finite differences of some fixed order are eventually constant. Then the orbit $g(n)\Gamma$ is equidistributed in a closed subset of $N/\Gamma$ that is a finite union of orbits of closed subgroups, unless the sequence is periodic modulo a proper closed subgroup; the precise carrier of the equidistribution is determined by the group generated by the values of $g$ modulo $\Gamma$.

The theorem is the polynomial equidistribution that generalises Weyl's theorem to the nilpotent case: a polynomial sequence on a nilmanifold is equidistributed in its algebraic closure, and the only obstruction is a finite union of proper orbits. It is the model of the distribution theory of the arithmetically interesting sequences — the prime values of polynomials, the values of the Möbius function — and it is the reason the nilpotent case is developed in full before the semisimple one. The abelian case of the statement is Weyl's theorem; the difference is the appearance of the commutators of $N$, which allow a larger closed subgroup to be the carrier of the equidistribution.

## Discrepancy

### The Definition and the Erdős–Turán Inequality

**Definition.** For a sequence $(x_n)$ in $[0,1)$ and an integer $N \geq 1$, the **discrepancy** is

$$
D_N(x_1, \dots, x_N) = \sup_{0 \le a < b \le 1} \left|\frac{\#\{1 \le n \le N : x_n \in [a,b)\}}{N} - (b-a)\right|,
$$

the largest deviation of the empirical measure from the uniform measure over intervals.

The discrepancy measures the rate of equidistribution, and the quantitative theorems give upper and lower bounds for it. The main analytic inequality is due to Erdős and Turán.

**Theorem (Erdős–Turán).** There is an absolute constant $C$ such that for every sequence $(x_n)$ in $[0,1)$ and every $H \geq 1$,

$$
D_N(x_1, \dots, x_N) \le C\left(\frac{1}{H} + \sum_{k=1}^{H}\frac{1}{k}\left|\frac{1}{N}\sum_{n=1}^{N} e^{2\pi i k x_n}\right|\right).
$$

The inequality converts an estimate of the exponential sums — the Fourier coefficients of the empirical measure — into an estimate of the discrepancy, and it is the quantitative form of Weyl's criterion: the criterion says that the sums vanish in the limit, and the inequality says how quickly they must vanish for the discrepancy to be small. Its proof uses a trigonometric approximation of the indicator function of an interval by a Fejér kernel; the constant is absolute and the optimal version has been improved by later authors.

**Corollary.** If the exponential sums satisfy $\left|\frac{1}{N}\sum_{n\le N} e^{2\pi i kx_n}\right| \le K/N$ uniformly in $k$, then $D_N = O((\log N)/N)$; this is the rate attained by the sequence $\{n\alpha\}$ for an irrational $\alpha$ with bounded partial quotients, and it is, up to the logarithm, the best possible, since $D_N \geq c\log N/N$ along a subsequence for every sequence.

### The Circle and Continued Fractions

**Theorem (the three-distance theorem).** For irrational $\alpha$ the points $\{n\alpha\}$, $n = 1, \dots, N$, cut the circle into $N+1$ intervals whose lengths take at most three distinct values, and the pattern is determined by the continued fraction expansion of $\alpha$. Consequently the discrepancy is controlled by the continued fraction data: if $[0;a_1,a_2,\dots]$ is the expansion of $\alpha$ and $q_m \le N < q_{m+1}$ are its denominators, then

$$
N D_N(\alpha) \ll 1 + \sum_{i=1}^{m} a_i,
$$

by a theorem of Ostrowski, so the discrepancy is small exactly when the partial quotients are small on average. It is $O((\log N)/N)$ for bounded partial quotients, the golden ratio, whose partial quotients are all $1$, attains this order up to a constant, and $N D_N(\alpha)$ is unbounded as $N \to \infty$ for every irrational $\alpha$.

The theorem is the quantitative theory of the linear sequence, and it is the reason the continued fraction expansion appears throughout equidistribution: the Diophantine properties of $\alpha$ determine the rate, and the theory of continued fractions is the subject, where the expansion is developed.

## Equidistribution of Orbits

### Horocycles and the Furstenberg Theorem

**Theorem (Furstenberg).** Let $\Gamma \le SL_2(\mathbb{R})$ be a lattice, $G = SL_2(\mathbb{R})$, and let $U$ be the horocycle subgroup. Then for every $x \in G/\Gamma$ the orbit $\{u_t x\}$ is equidistributed with respect to the invariant measure:

$$
\frac{1}{T}\int_0^T f(u_t x)\, dt \longrightarrow \int_{G/\Gamma} f\, d\mu \qquad \text{for every } f \in C_c(G/\Gamma).
$$

The theorem is stated here for the homogeneous case because it is the continuous-parameter analogue of Weyl's criterion: the time average against every continuous function converges, and the convergence holds for every starting point, not merely almost every one. The proof uses the commutation relation $a_su_ta_s^{-1} = u_{e^st}$ to rescale the horocycle and the ergodicity of the geodesic flow; the two flows are two aspects of one equidistribution theorem, and the details are in *Homogeneous Dynamics*.

### Unipotent Orbits and Ratner's Theorem

**Theorem (Ratner's equidistribution; stated in *Ratner's Theorems*).** Let $H$ be a subgroup generated by unipotent one-parameter subgroups and let $x \in G/\Gamma$. Then the orbit $Hx$ is equidistributed in its closure $\overline{Hx} = Lx$ with respect to the normalised invariant measure $\mu_{Lx}$, and the convergence is uniform as $x$ ranges over a compact subset of $X$.

The statement is the general equidistribution theorem of the subject; the horocycle theorem is the case $G = SL_2(\mathbb{R})$, $H = U$. Its uniformity is what makes it applicable to arithmetic: the equidistribution is not merely a statement about a fixed orbit but about a family of orbits varying continuously.

### Effective Equidistribution

**Theorem (effective Ratner; Green–Tao, Strömbergsson, Lindenstrauss–Mohammadi–Wang).** Under suitable hypotheses on $G$, $\Gamma$ and the unipotent flow, the equidistribution in Ratner's theorem holds with an explicit rate: for every $f$ in a suitable Sobolev space and every $x$ in a compact set,

$$
\frac{1}{T}\int_0^T f(u_tx)\,dt - \int f\,d\mu = O_f\left(T^{-\eta}\right)
$$

for an exponent $\eta > 0$ depending on $G$ and on the flow, with the constant depending on finitely many Sobolev norms of $f$.

The effective theorems are the quantitative form of Ratner's equidistribution, and they are needed whenever the equidistribution is to be applied with an error term: the counting of rational points, the quantitative Oppenheim conjecture, and the distribution of the values of a quadratic form at integer points. The exponent $\eta$ is not explicit in Ratner's original theorem and comes from the shearing estimates of the proof; the modern effective versions use the spectral gap of the action and the decay of matrix coefficients, which is the Howe–Moore theorem of *Ergodic Theory of Group Actions*.

## Unique Ergodicity

### The Equivalence with Uniform Convergence

**Definition.** A continuous map $T : X \to X$ of a compact metric space is **uniquely ergodic** if it has exactly one invariant Borel probability measure $\mu$; the map is **minimal** if every orbit is dense.

**Theorem.** Let $T$ be a continuous map of a compact metric space $X$ with a unique invariant probability measure $\mu$. Then for every $x \in X$ and every $f \in C(X)$,

$$
\frac{1}{N}\sum_{n=0}^{N-1} f(T^n x) \longrightarrow \int_X f\, d\mu,
$$

and the convergence is uniform in $x \in X$. Conversely, if the averages converge for every $f \in C(X)$ and every $x$, and the limit is independent of $x$, then $T$ is uniquely ergodic and the limit is the integral against the unique invariant measure.

*Proof.* The set of invariant probability measures is convex and compact, and an extreme point is ergodic; uniqueness of the measure therefore gives the ergodicity of $\mu$. For each $x$, let $\nu$ be a weak limit point of the empirical measures; it is $T$-invariant, so $\nu = \mu$, and every limit point is $\mu$, hence the averages converge. The uniformity follows from the compactness of $C(X)$ and the fact that a pointwise-convergent sequence of continuous functions on a compact space whose limit is continuous is uniformly convergent. The converse is the standard argument: an invariant measure is recovered as a limit of empirical measures, and the assumed independence of $x$ makes it unique. $\square$

**Corollary.** If $T$ is uniquely ergodic, then every orbit is equidistributed with respect to the invariant measure. If in addition $T$ is minimal, the union of the orbits is a single minimal set and the equidistribution is uniform over the space; unique ergodicity alone allows the presence of a wandering set of measure zero.

**Example (translations and horocycles).** The translation $x \mapsto x + \alpha$ of the circle is uniquely ergodic exactly when $\alpha$ is irrational; the horocycle flow of *Homogeneous Dynamics* is uniquely ergodic; and a unipotent flow on a nilmanifold is uniquely ergodic exactly when it is minimal, by the Green–Parry–Auslander theorem. In each case the ergodic theorem supplies the equidistribution, and the unique ergodicity supplies it for every point rather than almost every one.

### The Topological Reading

The relevance of unique ergodicity to equidistribution is that it removes the null set from the ergodic theorem. For a measure-preserving transformation the pointwise ergodic theorem holds only almost surely; for a uniquely ergodic continuous map it holds for every point. The mechanism is the continuity of the map, which makes the invariant measures a compact convex set and forces the empirical measures to converge to the only extreme point. The topological dynamics of continuous maps — minimality, recurrence, the structure of the invariant measures — is not covered here, and this article uses only the equidistribution consequence.

## Almost Periodic Functions and the Mean

### The Mean and the Bohr Compactification

**Definition.** A bounded continuous function $f : \mathbb{R} \to \mathbb{C}$ is **almost periodic** (in the sense of Bohr) if its translates $\{f(\cdot + t) : t \in \mathbb{R}\}$ form a relatively compact subset of the space of bounded continuous functions with the supremum norm. Equivalently, $f$ is a uniform limit of finite trigonometric sums $\sum_j c_j e^{i\lambda_j t}$.

The mean of an almost periodic function does not require an equidistribution theorem for its existence.

**Theorem (Bohr).** Every almost periodic function has a mean,

$$
M(f) = \lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T} f(t)\, dt,
$$

and the mean is multiplicative and positive; the almost periodic functions form a commutative $\mathrm{C}^*$-algebra isometrically isomorphic to $C(b\mathbb{R})$, where $b\mathbb{R}$ is the Bohr compactification of the discrete group $\mathbb{R}$, and the mean corresponds to integration against the normalised Haar measure of $b\mathbb{R}$.

The Bohr compactification is the dual, in the sense of Pontryagin, of the group $\mathbb{R}$ with the discrete topology; the identification is the one of *Pontryagin Duality*, and the mean is the Haar integral of the compact group. The theorem is the reason the equidistribution of a sequence against characters and the mean of an almost periodic function are the same phenomenon: both are the statement that a translation-invariant averaging procedure recovers the Haar integral.

### Besicovitch Theory and the Discrete Mean

**Definition.** A bounded measurable function $f : \mathbb{R} \to \mathbb{C}$ is **Besicovitch almost periodic** if it is the limit, in the mean-square seminorm

$$
\|f\|_B = \left(\overline{\lim}_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}|f(t)|^2\,dt\right)^{1/2},
$$

of finite trigonometric sums $\sum_j c_j e^{i\lambda_j t}$; the space is the quotient by the functions of seminorm zero. A bounded sequence on $\mathbb{Z}$ is Besicovitch almost periodic when the same holds with the discrete mean $\lim_N \frac{1}{N}\sum_{n\le N}$ in place of the integral.

The Besicovitch theory relaxes the *uniform* approximation of Bohr to mean-square approximation and admits a mean for a wider class of functions, which is what makes it the natural tool for equidistribution: the empirical measures of a sequence test a function by its discrete averages, and a mean-square control is exactly what a Weyl-type criterion delivers.

**Theorem (Bohr compactification of $\mathbb{Z}$).** The Bohr compactification of the discrete group $\mathbb{Z}$ is the circle group $\mathbb{R}/\mathbb{Z}$, and the algebra of Bohr almost periodic sequences on $\mathbb{Z}$ is isometrically $C(\mathbb{R}/\mathbb{Z})$; the mean $M(f) = \lim_N\frac{1}{N}\sum_{n \le N} f(n)$ of such a sequence is the integral of the corresponding continuous function over the circle with its normalised Haar measure.

Consequently a sequence $(x_n)$ in a compact abelian group $K$ is equidistributed if and only if the discrete means $\frac{1}{N}\sum_{n\le N}\varphi(x_n)$ converge to the group integral $\int_K \varphi \, dk$ for every almost periodic $\varphi$ on $K$; the Weyl criterion is the case in which $\varphi$ runs over the characters, and the passage from the characters to all almost periodic functions is the density of the trigonometric polynomials in $\| \cdot \|_B$. This is the conceptual statement that unifies the two halves of the article: equidistribution is the coincidence of the discrete mean along the sequence with the Haar integral on the group, and the almost periodic theory is the arena in which the coincidence is expressed.

## Summary

A sequence in a compact space with a prescribed probability measure is equidistributed when its empirical measures converge weakly to the measure, and on a compact group Weyl's criterion reduces the test to the matrix coefficients: the sequence is equidistributed if and only if its averages against every nontrivial irreducible representation vanish, equivalently against every nontrivial character in the abelian case. On the circle this criterion proves the equidistribution of $\{n\alpha\}$ for irrational $\alpha$ by a geometric-series estimate, and on the torus it proves the equidistribution of a translation exactly when the coordinates are rationally independent. Weyl's theorem extends the circle criterion to polynomial sequences whose coefficients are not all rational, and the van der Corput inequality, which lowers the degree of an exponential sum by one, is the engine of the induction; the nilmanifold generalisation carries the same statement to the polynomial orbits of a nilpotent group.

The discrepancy measures the rate, and the Erdős–Turán inequality bounds it by the exponential sums; the resulting rate for $\{n\alpha\}$ is governed by the partial quotients of $\alpha$ through the three-distance theorem, with $O((\log N)/N)$ for bounded quotients and a matching lower bound along a subsequence. In homogeneous dynamics the horocycle orbits are equidistributed for every point (Furstenberg) and the unipotent orbits are equidistributed in their closures uniformly (Ratner), with effective versions carrying explicit rates that come from the shearing estimates and the spectral gap. Unique ergodicity is the topological condition that upgrades equidistribution from almost everywhere to everywhere, and the almost periodic theory of Bohr identifies the mean of a function with a Haar integral on the Bohr compactification, so that equidistribution is the coincidence of a discrete mean with a group integral.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $X$, $\mu$, $C(X)$ | Compact metric space, Borel probability measure, continuous functions |
| $\mu_N = \frac{1}{N}\sum_{n\le N}\delta_{x_n}$ | Empirical measure of the first $N$ points |
| equidistributed | $\mu_N \to \mu$ weakly |
| $\{x\}$ | Fractional part of a real number; $[0,1)=\mathbb{R}/\mathbb{Z}$ |
| $K$, $dk$ | Compact group, normalised Haar measure |
| $\chi$, $G^\vee$ | Character and abelian dual group |
| $\pi_{ij}$, $\operatorname{Irr}(K)$ | Matrix coefficients and irreducible representations of a compact group |
| $D_N$ | Discrepancy: maximal deviation over intervals |
| Erdős–Turán | bound of $D_N$ by exponential sums; quantitative Weyl criterion |
| van der Corput | inequality lowering the degree of an exponential sum by one |
| three-distance theorem | the gaps of $\{n\alpha\}$, $n\le N$, take at most three lengths |
| $u_t$, $U$ | Horocycle subgroup and its flow on $G/\Gamma$ |
| uniquely ergodic | exactly one invariant probability measure |
| minimal | every orbit is dense |
| almost periodic, $M(f)$ | Bohr almost periodicity and the mean |
| $b\mathbb{R}$ | Bohr compactification of the discrete group $\mathbb{R}$ |







## Further Reading

- Hermann Weyl, "Über die Gleichverteilung von Zahlen mod. Eins", *Mathematische Annalen* 77 (1916), 313–352, for the criterion and the polynomial equidistribution theorem.
- L. Kuipers and H. Niederreiter, *Uniform Distribution of Sequences* (Wiley, 1974; reprinted Dover, 2006), for the systematic theory of discrepancy and the Erdős–Turán inequality.
- Paul Erdős and Pál Turán, "On the distribution of roots of polynomials", *Annals of Mathematics* 51 (1950), 105–119, for the discrepancy inequality.
- Hugh L. Montgomery, *Ten Lectures on the Interface between Analytic Number Theory and Harmonic Analysis* (AMS, 1994), for the interaction of exponential sums, discrepancy and harmonic analysis.
- Norbert Wiener, *The Fourier Integral and Certain of Its Applications* (Cambridge University Press, 1933), for the almost periodic theory and the mean.
- Harald Bohr, *Almost Periodic Functions* (Chelsea, 1947), for the Bohr compactification and the mean.
- Ben Green and Terence Tao, "The quantitative behaviour of polynomial orbits on nilmanifolds", *Annals of Mathematics* 175 (2012), 465–540, and Ben Green, Terence Tao and Tamar Ziegler, "An inverse theorem for the Gowers $U^{s+1}$-norm", *Annals of Mathematics* 176 (2012), 1231–1372, for the nilpotent equidistribution theory.
- Alexander Gorodnik and Amos Nevo, *The Ergodic Theory of Lattice Subgroups* (Princeton University Press, 2010), for the quantitative equidistribution of homogeneous orbits.
- Manfred Einsiedler and Thomas Ward, *Ergodic Theory with a View towards Number Theory* (Springer, 2011), for the equidistribution of homogeneous orbits and its arithmetic applications.
