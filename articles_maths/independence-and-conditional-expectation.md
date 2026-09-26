
# __Independence and Conditional Expectation__

## Introduction

Independence and conditioning are the two operations that distinguish probability theory from measure theory. Independence is the statement that two experiments carry no information about each other, and it is expressed as the factorisation of a joint measure into a product; conditioning is the operation of updating a measure in the light of partial information, and it is expressed as a projection. The two are dual: the product measure is the construction that makes independence possible, and the conditional expectation is the operator that undoes it, and the interplay between them — the laws of large numbers, the martingale theory, the ergodic theorems — is the substance of the subject.

This article develops both. It defines independent events and independent random variables, constructs the product measure and the infinite product space by the Kolmogorov extension theorem, proves the Borel–Cantelli lemmas and the Kolmogorov zero–one law, defines the conditional expectation as a Radon–Nikodym derivative and identifies its $L^2$ projection character, records the properties that make it a working tool, constructs regular conditional probabilities and conditional distributions by disintegration, and introduces filtrations as the bookkeeping device for information that grows in time.

The place of the article is fixed by two boundaries.

- The **measure-theoretic frame** — probability spaces, random variables, distributions, expectation, moments, the modes of convergence and the characteristic function — is *Measure-Theoretic Probability*, the preceding article, and its notation is held here: $(\Omega,\mathcal{F},\mathbb{P})$, $\mu_X$, $F_X$, $\mathbb{E}$, $\operatorname{Var}$, a.s., $\sigma(X)$, and the four modes of convergence. The **general measure theory** — the Radon–Nikodym theorem, the product measure on two spaces, the monotone class theorem, the disintegration of measures — is *Measure Theory and Integration*, and the **modes of convergence** are *Modes of Convergence*.
- The **limit theorems** whose proofs use independence areand the **martingale theory** built on the filtration and the conditional expectation is. This article constructs the objects; two other articles use them.

No physics is invoked. Throughout, $(\Omega,\mathcal{F},\mathbb{P})$ is a probability space as in *Measure-Theoretic Probability*; a **$\pi$-system** is a family of sets closed under finite intersections, a **dynkin system** is a family containing $\Omega$ and closed under complements and countable disjoint unions, and a **filtration** is an increasing family $\{\mathcal{F}_n\}$ of sub-$\sigma$-algebras of $\mathcal{F}$, with $\mathcal{F}_\infty = \sigma(\bigcup_n \mathcal{F}_n)$. The conditional expectation of $X$ given $\mathcal{G}$ is written $\mathbb{E}[X \mid \mathcal{G}]$, and the conditional probability of $A$ given $\mathcal{G}$ is $\mathbb{P}(A \mid \mathcal{G}) = \mathbb{E}[\mathbf{1}_A \mid \mathcal{G}]$.

## Independent Events

### The Definition of Independence

**Definition.** Let $(\Omega,\mathcal{F},\mathbb{P})$ be a probability space. A finite or countable family of events $\{A_i\}_{i \in I}$ is **independent** if for every finite subset $J \subseteq I$,

$$
\mathbb{P}\!\left(\bigcap_{i \in J} A_i\right) = \prod_{i \in J}\mathbb{P}(A_i).
$$

The sub-$\sigma$-algebras $\{\mathcal{G}_i\}$ of $\mathcal{F}$ are **independent** if for every choice of sets $A_i \in \mathcal{G}_i$ and every finite set of distinct indices, the events $A_i$ are independent; and the random variables $\{X_i\}$ are independent if the $\sigma$-algebras $\sigma(X_i)$ are independent.

Two events of positive probability are independent exactly when $\mathbb{P}(A \mid B) = \mathbb{P}(A)$, so the definition is the formal statement that conditioning on $B$ does not change the probability of $A$. Independence of a family is stronger than pairwise independence: the events $A_1, A_2, A_3$ can be pairwise independent without being jointly independent, and the standard example is the family of three subsets of a four-point space corresponding to the binary triples of a two-dimensional vector space over $\mathbb{F}_2$ with the coordinate functionals.

**Proposition (the $\pi$–$\lambda$ criterion).** Let $\mathcal{P}_i$ be $\pi$-systems generating the $\sigma$-algebras $\mathcal{G}_i$. If $\mathbb{P}(\bigcap_{i\in J} A_i) = \prod_i \mathbb{P}(A_i)$ holds for all finite $J$ and all $A_i \in \mathcal{P}_i$, then the $\sigma$-algebras $\mathcal{G}_i$ are independent.

The proposition is the standard reduction: independence is checked on a generating $\pi$-system, and the passage to the generated $\sigma$-algebra is the monotone class argument of *Measure Theory and Integration*. It is what makes independence of random variables checkable through the distribution functions or the characteristic functions, since the half-lines form a $\pi$-system generating the Borel $\sigma$-algebra.

### The Borel–Cantelli Lemmas

**Definition.** For a sequence of events $\{A_n\}$, the event that **$A_n$ occurs infinitely often** is

$$
\limsup_n A_n = \bigcap_{n\geq1}\bigcup_{m \geq n} A_m = \{A_n \text{ infinitely often}\}, \qquad \text{written } \{A_n \text{ i.o.}\}.
$$

**Theorem (first Borel–Cantelli lemma).** If $\sum_{n\geq1}\mathbb{P}(A_n) < \infty$ then $\mathbb{P}(A_n \text{ i.o.}) = 0$.

*Proof.* For every $n$, the event $\{A_n \text{ i.o.}\}$ is contained in $\bigcup_{m\geq n}A_m$, whence

$$
\mathbb{P}(A_n \text{ i.o.}) \leq \mathbb{P}\!\left(\bigcup_{m \geq n}A_m\right) \leq \sum_{m\geq n}\mathbb{P}(A_m) \longrightarrow 0
$$

as $n\to\infty$ because the tail of a convergent series tends to $0$. $\square$

The first lemma requires no independence and is the standard tool for almost-sure statements: it shows that a sequence whose probabilities are summable occurs only finitely often, almost surely.

**Theorem (second Borel–Cantelli lemma).** If the events $\{A_n\}$ are independent and $\sum_{n\geq1}\mathbb{P}(A_n) = \infty$ then $\mathbb{P}(A_n \text{ i.o.}) = 1$.

*Proof.* By the continuity from below it suffices to show $\mathbb{P}(\bigcup_{n\leq m \leq N}A_m) \to 1$ as $N\to\infty$ for each fixed $n$. Using the independence,

$$
\mathbb{P}\!\left(\bigcap_{m=n}^{N} A_m^c\right) = \prod_{m=n}^{N}\bigl(1 - \mathbb{P}(A_m)\bigr) \leq \prod_{m=n}^{N}\exp\bigl(-\mathbb{P}(A_m)\bigr) = \exp\!\left(-\sum_{m=n}^{N}\mathbb{P}(A_m)\right),
$$

which tends to $0$ as $N\to\infty$ because the series diverges. Hence $\mathbb{P}(\bigcup_{m\geq n}A_m) = 1$ for every $n$, and the intersection over $n$ of these events has probability one. $\square$

The two lemmas are the standard criterion for the almost-sure occurrence of infinitely many events, and the independence in the second is essential: the events $A_n = [0,1/n]$ in $[0,1]$ with Lebesgue measure have divergent probability sum but do not occur infinitely often, since their intersection is empty. The pair is applied throughout the strong law of large numbers and the theory of records, and it is the model for the more delicate zero–one laws below.

## Independent Random Variables

### Product Measures and the Extension Theorem

**Definition.** Let $(S_1,\mathcal{S}_1,\mu_1)$ and $(S_2,\mathcal{S}_2,\mu_2)$ be probability spaces. The **product measure** $\mu_1 \otimes \mu_2$ on $(S_1\times S_2, \mathcal{S}_1\otimes\mathcal{S}_2)$ is the unique measure with

$$
(\mu_1\otimes\mu_2)(A_1\times A_2) = \mu_1(A_1)\mu_2(A_2) \qquad \text{for } A_i \in \mathcal{S}_i,
$$

and its existence is the product measure theorem of *Measure Theory and Integration*. The random variables $X_1, \dots, X_n$ are independent if and only if the law of the vector $(X_1,\dots,X_n)$ is the product $\mu_{X_1}\otimes\cdots\otimes\mu_{X_n}$.

**Theorem (Kolmogorov extension theorem).** Let $(S_n,\mathcal{S}_n)$ be standard Borel spaces and let $\mu_n$ be a probability measure on $\prod_{i\leq n}S_i$, the family $\{\mu_n\}$ being consistent in the sense that $\mu_{n+1}(\cdot \times S_{n+1}) = \mu_n$. Then there is a unique probability measure $\mu$ on the product $\prod_{n\geq1}S_n$ with the cylindrical marginals $\mu_n$; the coordinate maps of the product are independent random variables with laws $\mu_{X_n} = $ the one-dimensional marginal.

The extension theorem is the construction of the countable product of probability spaces, and it is the reason an infinite sequence of independent random variables exists at all. Its hypothesis of consistency is automatic in the applications, and the proof is the Carathéodory extension theorem applied to the algebra of cylinders, together with a compactness argument on the approximating finite-dimensional measures. The continuity of the measures on a projective system of compact classes is the inner regularity that makes the extension possible. The theorem is also the source of the **canonical model**: the sequence space $(S^{\mathbb{N}}, \mathcal{S}^{\otimes\mathbb{N}}, \mu)$ carries the coordinate process, and every sequence of independent random variables with laws $\mu_{X_n}$ is a measurable image of it.

### Independence Criteria

**Theorem (factorisation criteria).** For random variables $X$ and $Y$ with values in standard Borel spaces the following are equivalent:

1. $X$ and $Y$ are independent;
2. the joint law is the product of the marginals: $\mu_{(X,Y)} = \mu_X \otimes \mu_Y$;
3. $\mathbb{E}[f(X)g(Y)] = \mathbb{E}[f(X)]\,\mathbb{E}[g(Y)]$ for all bounded measurable $f,g$;
4. $\mathbb{E}[e^{i\langle s,X\rangle + i\langle t,Y\rangle}] = \varphi_X(s)\varphi_Y(t)$ for all $s,t$ (Kac's criterion).

*Proof.* The equivalence of 1 and 2 is the definition; 2 implies 3 by Fubini, and 3 implies 2 by taking $f = \mathbf{1}_{A}$, $g = \mathbf{1}_{B}$ and the $\pi$–$\lambda$ criterion; the equivalence with 4 follows because the exponentials span a convergence-determining class. $\square$

The boundedness in 3 is essential: uncorrelated is weaker than independent, and the equality $\mathbb{E}[XY] = \mathbb{E}[X]\mathbb{E}[Y]$ for the two moments alone does not imply independence. The criterion 4 is the one usually applied, because it is stated in terms of characteristic functions and is therefore amenable to the Fourier analysis of *Measure-Theoretic Probability* and *Fourier Analysis on Euclidean Spaces*.

## Zero–One Laws

### The Kolmogorov Zero–One Law

**Definition.** For a sequence of random variables $\{X_n\}$ on a common probability space, the **tail $\sigma$-algebra** is

$$
\mathcal{T} = \bigcap_{n\geq1}\sigma(X_n, X_{n+1}, \dots),
$$

the $\sigma$-algebra of the events whose occurrence does not depend on finitely many of the $X_n$.

An event is in the tail when it is determined by the limiting behaviour of the sequence: the event that $\sum_n X_n$ converges, that $\limsup_n X_n > 0$, that the sample mean converges, and that $X_n \to X$ are all tail events, as is the event that $X_n$ takes a value infinitely often when the $X_n$ are independent and identically distributed.

**Theorem (Kolmogorov's zero–one law).** Let $\{X_n\}$ be independent random variables. Then every tail event has probability $0$ or $1$.

*Proof.* For each $n$ the $\sigma$-algebras $\sigma(X_1,\dots,X_n)$ and $\sigma(X_{n+1},X_{n+2},\dots)$ are independent, so the algebra $\sigma(X_1,X_2,\dots)$ generated by all the $X_i$ is independent of the tail $\sigma$-algebra: a decisive argument is to note that for each $n$, $\mathcal{T} \subseteq \sigma(X_{n+1},X_{n+2},\dots)$, and the union of the $\sigma(X_1,\dots,X_n)$ over $n$ is a $\pi$-system generating $\sigma(X_1,X_2,\dots)$ that is independent of $\mathcal{T}$; hence $\mathcal{T}$ is independent of $\sigma(X_1,X_2,\dots)$, and since $\mathcal{T} \subseteq \sigma(X_1,X_2,\dots)$, the $\sigma$-algebra $\mathcal{T}$ is independent of itself, which forces every event in it to have probability $0$ or $1$. $\square$

The theorem is the reason a candidate limit of an independent sequence either exists a.s. or fails a.s., with no intermediate probability; it is the abstract form of the statement that a series of independent terms converges or diverges almost surely, and it is the first of a family of zero–one laws.

**Theorem (Hewitt–Savage).** Let $\{X_n\}$ be an exchangeable sequence — one whose finite-dimensional distributions are invariant under permutations of the indices. Then every **exchangeable event**, one that is invariant under finite permutations, has probability $0$ or $1$.

The Hewitt–Savage theorem contains the Kolmogorov law as a special case, since a tail event of an exchangeable sequence is exchangeable, and it is the zero–one law behind de Finetti's theorem: an exchangeable sequence of indicator variables is a mixture of independent sequences with a common success probability, and the mixing measure is the law of the limiting frequency.

### The Martingale Zero–One Law, Briefly

The zero–one laws have a limiting form in the martingale theory: if $X$ is bounded and $\mathbb{E}[X \mid \mathcal{F}_n] = \mathbb{E}[X]$ for all $n$ and $\mathcal{F}_\infty = \sigma(\bigcup_n\mathcal{F}_n)$ then $X = \mathbb{E}[X]$ a.s., which is the statement that the tail of the filtration contributes no information. The Lévy downward theorem makes the same point for a decreasing family, and it is the abstract form of the fact that the conditional expectation on a decreasing family of $\sigma$-algebras converges to the conditional expectation on the intersection. This is the point at which the present article hands over to the martingale theory.

## Conditional Expectation

### The Definition of Conditional Expectation

**Definition.** Let $X$ be an integrable random variable on $(\Omega,\mathcal{F},\mathbb{P})$ and let $\mathcal{G} \subseteq \mathcal{F}$ be a sub-$\sigma$-algebra. The **conditional expectation** of $X$ given $\mathcal{G}$ is the integrable $\mathcal{G}$-measurable random variable $\mathbb{E}[X \mid \mathcal{G}]$ satisfying

$$
\int_G \mathbb{E}[X \mid \mathcal{G}]\, d\mathbb{P} = \int_G X\, d\mathbb{P} \qquad \text{for every } G \in \mathcal{G}.
$$

**Theorem (existence and uniqueness).** For integrable $X$ the conditional expectation exists and is unique up to a.s. equality; for $X \geq 0$ it exists in $[0,\infty]$ without the integrability assumption.

*Proof.* The measure $\nu(G) = \int_G X^+\,d\mathbb{P} - \int_G X^-\,d\mathbb{P}$ on $(\Omega,\mathcal{G})$ is finite and absolutely continuous with respect to $\mathbb{P}|_{\mathcal{G}}$; the Radon–Nikodym theorem of *Measure Theory and Integration* supplies a $\mathcal{G}$-measurable density $Y$ with $\nu(G) = \int_G Y\,d\mathbb{P}$, and $Y$ is the conditional expectation. If $Y'$ is another, then $\int_G (Y - Y')\,d\mathbb{P} = 0$ for all $G \in \mathcal{G}$, including $G = \{Y > Y'\}$ and $G = \{Y < Y'\}$, so $Y = Y'$ a.s. $\square$

**Definition.** The **conditional probability** of $A$ given $\mathcal{G}$ is $\mathbb{P}(A \mid \mathcal{G}) = \mathbb{E}[\mathbf{1}_A \mid \mathcal{G}]$, and for a random variable $Y$ the conditional expectation given $Y$ is $\mathbb{E}[X \mid Y] = \mathbb{E}[X \mid \sigma(Y)]$.

The conditional expectation is a random variable, not a number: it is the best guess of $X$ available to an observer who knows the information in $\mathcal{G}$. The phrase "the" conditional expectation suppresses the a.s. ambiguity, which is harmless as long as no uncountable family of conditions is being handled simultaneously; the question of choosing the versions coherently is the content of the regular conditional probability below.

### The $L^2$ Projection

**Theorem (projection character).** If $X \in L^2(\Omega,\mathcal{F},\mathbb{P})$ and $\mathcal{G} \subseteq \mathcal{F}$ then $\mathbb{E}[X \mid \mathcal{G}]$ is the orthogonal projection of $X$ onto the closed subspace $L^2(\Omega,\mathcal{G},\mathbb{P})$ of $\mathcal{G}$-measurable square-integrable functions.

*Proof.* The subspace is closed because $L^2$ convergence preserves measurability up to a.s. equality. For $X \in L^2$ and $Z \in L^2(\mathcal{G})$ the defining relation gives $\mathbb{E}[(X - \mathbb{E}[X\mid\mathcal{G}])Z] = 0$, since $Z$ is $\mathcal{G}$-measurable, so the difference is orthogonal to $L^2(\mathcal{G})$; the projection is characterised by this orthogonality, and the projection is the conditional expectation by uniqueness. $\square$

The projection picture is the geometric content of conditioning, and it is the reason the conditional expectation is the minimum-mean-square-error predictor: among all $\mathcal{G}$-measurable functions $Z$, the conditional expectation minimises $\mathbb{E}[(X - Z)^2]$ over $Z \in L^2(\mathcal{G})$. It also explains the conditional variance decomposition

$$
\operatorname{Var}(X) = \mathbb{E}\bigl[\operatorname{Var}(X \mid \mathcal{G})\bigr] + \operatorname{Var}\bigl(\mathbb{E}[X \mid \mathcal{G}]\bigr),
$$

which is the Pythagorean theorem for the orthogonal decomposition $X = \mathbb{E}[X\mid\mathcal{G}] + (X - \mathbb{E}[X\mid\mathcal{G}])$.

### Properties

**Theorem (properties of conditional expectation).** Let $X, Y$ be integrable and let $\mathcal{G}, \mathcal{H}$ be sub-$\sigma$-algebras of $\mathcal{F}$.

1. **Linearity.** $\mathbb{E}[aX + bY \mid \mathcal{G}] = a\,\mathbb{E}[X \mid \mathcal{G}] + b\,\mathbb{E}[Y \mid \mathcal{G}]$ a.s.
2. **Positivity and monotonicity.** $X \geq 0$ implies $\mathbb{E}[X \mid \mathcal{G}] \geq 0$ a.s.; $X \leq Y$ implies $\mathbb{E}[X\mid\mathcal{G}] \leq \mathbb{E}[Y\mid\mathcal{G}]$ a.s.
3. **Tower property.** If $\mathcal{H} \subseteq \mathcal{G}$ then $\mathbb{E}\bigl[\mathbb{E}[X \mid \mathcal{G}] \mid \mathcal{H}\bigr] = \mathbb{E}[X \mid \mathcal{H}]$ a.s.; in particular $\mathbb{E}[\mathbb{E}[X\mid\mathcal{G}]] = \mathbb{E}[X]$.
4. **Pull-out.** If $Y$ is bounded and $\mathcal{G}$-measurable then $\mathbb{E}[YX \mid \mathcal{G}] = Y\,\mathbb{E}[X \mid \mathcal{G}]$ a.s.
5. **Independence.** If $X$ is independent of $\mathcal{G}$ then $\mathbb{E}[X \mid \mathcal{G}] = \mathbb{E}[X]$ a.s.
6. **Jensen.** If $\varphi$ is convex and $\varphi(X)$ is integrable then $\varphi(\mathbb{E}[X\mid\mathcal{G}]) \leq \mathbb{E}[\varphi(X)\mid\mathcal{G}]$ a.s.
7. **Convergence.** If $X_n \to X$ a.s. with $|X_n| \leq Y$ integrable, then $\mathbb{E}[X_n\mid\mathcal{G}] \to \mathbb{E}[X\mid\mathcal{G}]$ a.s.

*Proof.* Each property is proved by checking the defining integral identity on sets of $\mathcal{G}$: linearity and positivity by the linearity and positivity of the integral; the tower property by reducing to $\mathcal{H}$-sets; pull-out by the localising $\pi$–$\lambda$ argument; independence because the constant $\mathbb{E}[X]$ is $\mathcal{G}$-measurable and satisfies the defining relation by the factorisation criterion; Jensen by the supporting line of a convex function and the positivity of the conditional expectation; and the convergence statement by the conditional form of the dominated convergence theorem, applied to the positive and negative parts. $\square$

**Corollary (conditional Cauchy–Schwarz and conditional Hölder).** The conditional expectation is a contraction on $L^p$: $\|\mathbb{E}[X \mid \mathcal{G}]\|_p \leq \|X\|_p$ for $1 \leq p \leq \infty$; and $\left|\mathbb{E}[XY\mid\mathcal{G}]\right| \leq \mathbb{E}[|X|^p\mid\mathcal{G}]^{1/p}\mathbb{E}[|Y|^q\mid\mathcal{G}]^{1/q}$ for conjugate $p,q$. The contraction property follows from Jensen applied to $|x|^p$, and the conditional Hölder inequality from the ordinary Hölder applied conditionally.

## Conditional Distributions

### Regular Conditional Probability

**Definition.** Let $X$ be a random variable with values in a measurable space $(S,\mathcal{S})$ and let $\mathcal{G} \subseteq \mathcal{F}$ be a sub-$\sigma$-algebra. A **regular conditional probability** for $X$ given $\mathcal{G}$ is a map $\omega \mapsto \mu_\omega$ from $\Omega$ to the probability measures on $(S,\mathcal{S})$ such that $\omega \mapsto \mu_\omega(B)$ is $\mathcal{G}$-measurable for each $B$ and

$$
\mathbb{P}(X \in B \mid \mathcal{G})(\omega) = \mu_\omega(B) \qquad \text{for a.e. } \omega, \text{ for every } B \in \mathcal{S}.
$$

**Theorem (disintegration; existence on standard Borel spaces).** If $(S,\mathcal{S})$ is a standard Borel space then a regular conditional probability for $X$ given $\mathcal{G}$ exists, and it is unique up to a.s. equality. Consequently for integrable $g$,

$$
\mathbb{E}[g(X) \mid \mathcal{G}](\omega) = \int_S g(x)\, \mu_\omega(dx) \qquad \text{a.s.}
$$

The theorem is the disintegration of the joint law of $(X, \mathcal{G})$-measurable information, and its proof is a measurable selection argument: the conditional probabilities of a countable generating algebra of $\mathcal{S}$ are chosen measurably and extended by the Carathéodory theorem. On a general measurable space the regular conditional probability can fail to exist, which is the reason the standard Borel hypothesis is imposed. The case $\mathcal{G} = \sigma(Y)$ gives the **conditional distribution of $X$ given $Y$**, written $\mu_{X\mid Y}(y, dx)$ with $y \mapsto \mu_{X \mid Y}(y,\cdot)$ measurable, and the **Bayes formula** $\mathbb{P}(Y \in A \mid X = x) = \mathbb{P}(X = x \mid Y \in A)\mathbb{P}(Y \in A)/\mathbb{P}(X = x)$ is the discrete-case form of the change of variable between the two conditional distributions.

**Example (Gaussian conditioning).** Let $(X,Y)$ be jointly Gaussian with means $\mu_X, \mu_Y$, variances $\sigma_X^2, \sigma_Y^2$ and correlation $\rho$. Then the conditional law of $Y$ given $X = x$ is normal with

$$
\mathbb{E}[Y \mid X = x] = \mu_Y + \rho\frac{\sigma_Y}{\sigma_X}(x - \mu_X), \qquad \operatorname{Var}(Y \mid X = x) = \sigma_Y^2(1 - \rho^2),
$$

and the conditional expectation is affine in $x$. The example is the prototype of the conditional expectation as a regression, and it shows that the conditional variance is independent of $x$ exactly in the Gaussian case, which is the defining property of the family.

## Filtrations and Martingales

### Filtrations

**Definition.** A **filtration** on $(\Omega,\mathcal{F},\mathbb{P})$ is an increasing family of sub-$\sigma$-algebras $\mathcal{F}_0 \subseteq \mathcal{F}_1 \subseteq \cdots \subseteq \mathcal{F}$; the triple $(\Omega,\mathcal{F},\{\mathcal{F}_n\},\mathbb{P})$ is a **filtered probability space**. A process $\{X_n\}$ is **adapted** if $X_n$ is $\mathcal{F}_n$-measurable for every $n$; it is **predictable** if $X_n$ is $\mathcal{F}_{n-1}$-measurable; and it is **integrable** if $\mathbb{E}|X_n| < \infty$ for every $n$. The **natural filtration** of a process $\{X_n\}$ is $\mathcal{F}_n = \sigma(X_0,\dots,X_n)$.

The filtration is the mathematical encoding of the information available at time $n$: an adapted process is one whose value at time $n$ is known by time $n$, a predictable process is one whose value at time $n$ is known by time $n-1$, and the conditional expectation $\mathbb{E}[X \mid \mathcal{F}_n]$ is the best estimate of $X$ given the information up to time $n$. The tower property of the conditional expectation is the consistency of these estimates, and it is the defining property of the martingale theory.

**Definition.** An adapted integrable process $\{X_n\}$ is a **martingale** if $\mathbb{E}[X_{n+1} \mid \mathcal{F}_n] = X_n$ a.s. for every $n$; a **submartingale** if $\mathbb{E}[X_{n+1} \mid \mathcal{F}_n] \geq X_n$ a.s.; and a **supermartingale** if the inequality reverses. The definitions extend to continuous time with an increasing family $\{\mathcal{F}_t\}_{t\geq0}$.

The **optional stopping** theorem, the **maximal inequalities**, the **Doob decomposition** and the **martingale convergence theorem** are the content, where the filtration theory is developed in full. The present article has supplied the conditional expectation and the filtration; the martingale theory is the systematic exploitation of the tower property, and its continuous-time form lies outside this article.

## Summary

A family of events is independent when the probability of every finite intersection is the product of the probabilities, a family of random variables is independent when their $\sigma$-algebras are, and independence is equivalent to the joint law being the product of the marginals, to the factorisation of expectations of products of bounded functions, and to the factorisation of the characteristic function. The product measure on two spaces is the measure-theoretic construction of independence, and the Kolmogorov extension theorem builds the countable product so that an infinite sequence of independent random variables exists; the sequence space with the coordinate process is the canonical model.

The first Borel–Cantelli lemma states that summable probabilities imply finitely many occurrences, with no independence needed; the second states that independent events with divergent probability sum occur infinitely often, almost surely. Kolmogorov's zero–one law states that every tail event of an independent sequence has probability $0$ or $1$, and the Hewitt–Savage theorem extends this to the exchangeable events of an exchangeable sequence. The conditional expectation $\mathbb{E}[X\mid\mathcal{G}]$ is the a.s. unique integrable $\mathcal{G}$-measurable random variable with the same integral as $X$ on every set of $\mathcal{G}$; it exists by the Radon–Nikodym theorem, is the orthogonal projection of $X$ onto $L^2(\mathcal{G})$ when $X \in L^2$, satisfies linearity, positivity, the tower property, pull-out, invariance under independence, Jensen and the conditional convergence theorems, and it is a contraction on every $L^p$. Regular conditional probabilities exist on standard Borel spaces by disintegration, and they give the conditional distribution and the Bayes formula. A filtration is the record of the information available at each time, an adapted process is one known in time, and a martingale is an adapted integrable process whose conditional expectation one step ahead is its present value; the martingale theory is not covered here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(\Omega, \mathcal{F}, \mathbb{P})$ | Probability space, as fixed in *Measure-Theoretic Probability* |
| a.s. | Almost surely; synonym of almost everywhere |
| independent | finite intersections factor; joint law is the product |
| i.o. | $\{A_n \text{ i.o.}\}=\bigcap_n\bigcup_{m\ge n}A_m$ |
| $\mu_1\otimes\mu_2$ | Product measure on $S_1\times S_2$ |
| i.i.d. | independent and identically distributed |
| $\pi$-system, dynkin system | closed under finite intersections; closed under complements and disjoint unions |
| $\mathcal{T}=\bigcap_n\sigma(X_n,X_{n+1},\dots)$ | Tail $\sigma$-algebra |
| $\mathbb{E}[X\mid\mathcal{G}]$ | Conditional expectation, the $\mathcal{G}$-measurable integral matching $X$ |
| $\mathbb{P}(A\mid\mathcal{G})$ | $\mathbb{E}[\mathbf{1}_A\mid\mathcal{G}]$ |
| $\mathbb{E}[X\mid Y]$ | $\mathbb{E}[X\mid\sigma(Y)]$ |
| $\operatorname{Var}(X\mid\mathcal{G})$ | Conditional variance $\mathbb{E}[(X-\mathbb{E}[X\mid\mathcal{G}])^2\mid\mathcal{G}]$ |
| $\mu_{X\mid Y}(y,dx)$ | Regular conditional distribution of $X$ given $Y$ |
| $\{\mathcal{F}_n\}$, $\mathcal{F}_\infty$ | Filtration, $\sigma(\bigcup_n\mathcal{F}_n)$ |
| adapted, predictable | $X_n$ is $\mathcal{F}_n$-measurable; $X_n$ is $\mathcal{F}_{n-1}$-measurable |
| martingale | $\mathbb{E}[X_{n+1}\mid\mathcal{F}_n]=X_n$ a.s. |





## Further Reading

- Patrick Billingsley, *Probability and Measure* (Wiley, 3rd edition, 1995), for independence, the Borel–Cantelli lemmas and the product measure construction.
- Andrei N. Kolmogorov, *Foundations of the Theory of Probability* (Chelsea, 1950), for the original statements of the extension theorem and the zero–one law.
- Kai Lai Chung, *A Course in Probability Theory* (Academic Press, 3rd edition, 2001), for conditional expectation, the regular conditional probability and the zero–one laws.
- Joseph L. Doob, *Stochastic Processes* (Wiley, 1953), for the systematic development of conditioning, filtrations and the martingale theory that follows.
- Paul R. Halmos, *Measure Theory* (Van Nostrand, 1950), for the product measure, the Radon–Nikodym theorem and the monotone class arguments used throughout.
- Edwin Hewitt and Leonard J. Savage, "Symmetric measures on Cartesian products", *Transactions of the American Mathematical Society* 80 (1955), 470–501, for the exchangeable zero–one law.
- Bruno de Finetti, "La prévision: ses lois logiques, ses sources subjectives", *Annales de l'Institut Henri Poincaré* 7 (1937), 1–68, for exchangeability and the representation theorem.
- David Williams, *Probability with Martingales* (Cambridge University Press, 1991), for a concise treatment of conditional expectation and the martingale theory.
