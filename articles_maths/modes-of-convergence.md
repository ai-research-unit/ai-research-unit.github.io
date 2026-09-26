
# __Modes of Convergence__

## Introduction

A limit in analysis is only as precise as the notion of convergence that carries it, and on a space of functions there is not one such notion but several. A sequence of functions can converge at every point, or uniformly, or off a null set, or in a mean; these are different conditions, ordered by implication in a definite way, and every theorem of analysis is stated with respect to one of them. This article fixes the vocabulary. It names the modes of convergence that the whole of Part III uses, defines each of them, relates them by the implications that hold and by the counterexamples that show the remaining implications false, and states the theorems that govern the interchange of a limit with an integral, a derivative and an infinite sum.

The article is a contract as much as a piece of mathematics. The names **pointwise**, **uniform**, **locally uniform**, **almost everywhere**, **almost uniform**, **in measure**, **in $L^p$**, **weak** and **weak-$\ast$** are fixed here, with the notation collected in the table at the end, and the other articles of this category use them in exactly this sense. Where two modes are commonly given the same name — convergence in measure is called convergence in probability on a space of total mass one, and weak convergence of measures is called weak-$\ast$ convergence of the corresponding functionals — the distinction is recorded and the name used by this corpus is the first of the two.

The prerequisites are the measure theory of *Measure Theory and Integration* — measurable functions, the integral, the convergence theorems, the $L^p$ spaces, and the notions of almost everywhere and of the product measure — together with the topological background of *Metric, Uniform and Complete Spaces*, *Topological Spaces* and *Nets, Filters and Convergence*, and the functional-analytic background of *Normed and Banach Spaces*, *Locally Convex Spaces* and *Duality Theory*. Set-theoretic and algebraic vocabulary is used in the sense of Part I. The article deliberately contains no arithmetic: the modes are introduced over a general measure space and a general normed space, and their arithmetic instances — the convergence of Dirichlet series, of $p$-adic sequences, of modular $q$-expansions — belong to the articles of this Part that develop those subjects. The theory of convergence in probability and almost sure convergence belongs. No physics is invoked.

## Convergence in a Topological and a Uniform Space

### Sequences, Nets and Filters

**Definition.** Let $X$ be a topological space. A sequence $(x_n)$ in $X$ **converges** to $x \in X$, written $x_n \to x$, if for every neighbourhood $U$ of $x$ there is $N$ with $x_n \in U$ for all $n \geq N$. The point $x$ is a **limit** of the sequence. A sequence is **convergent** if it has a limit.

A sequence is a function on the directed set $\mathbb{N}$; replacing $\mathbb{N}$ by an arbitrary directed set gives a **net**, and the same definition applies with the index set in place of $\mathbb{N}$. A **filter** on $X$ converges to $x$ if it contains every neighbourhood of $x$. Nets and filters carry the same convergence information, and in a first-countable space the topology is determined by its convergent sequences, so that sequences suffice for the metric and normed spaces that are the ambient spaces of this Part. The general theory is that of *Nets, Filters and Convergence*.

**Proposition (uniqueness).** If $X$ is Hausdorff, a sequence has at most one limit.

**Proof.** If $x \neq y$, choose disjoint neighbourhoods $U$ of $x$ and $V$ of $y$; a sequence converging to both lies eventually in each, hence eventually in $U \cap V = \emptyset$, a contradiction. $\square$

In a non-Hausdorff space a sequence may have several limits, and the notation $x_n \to x$ then asserts only that $x$ is one of them. Every space in this Part is Hausdorff, and the qualification is not repeated.

**Theorem (convergence and continuity).** A map $f : X \to Y$ of topological spaces is continuous at $x$ if and only if $f(x_\lambda) \to f(x)$ for every net $x_\lambda \to x$. For first-countable $X$ it suffices to test sequences.

**Proof.** If $f$ is continuous at $x$ and $V$ is a neighbourhood of $f(x)$, then $f^{-1}(V)$ is a neighbourhood of $x$, so $x_\lambda$ lies eventually in it and $f(x_\lambda)$ lies eventually in $V$. Conversely, if $f$ is not continuous at $x$, there is a neighbourhood $V$ of $f(x)$ with $f^{-1}(V)$ not a neighbourhood of $x$; the neighbourhoods of $x$ are directed by reverse inclusion, and choosing $x_U \in U \setminus f^{-1}(V)$ gives a net $x_U \to x$ with $f(x_U) \notin V$. $\square$

### Cauchy Sequences, Completeness and Compactness

**Definition.** Let $(X, \mathcal{U})$ be a uniform space, with entourages the members of $\mathcal{U}$. A sequence $(x_n)$ is **Cauchy** if for every entourage $U$ there is $N$ with $(x_m, x_n) \in U$ for all $m, n \geq N$. The space is **complete** if every Cauchy sequence converges. In a metric space the condition is that $d(x_m, x_n) \to 0$ as $m, n \to \infty$.

Convergent sequences are Cauchy, and the converse is the content of completeness; the two notions agree in a complete space and in a compact space. The following three facts are the ones this Part uses.

**(a)** A uniform space $X$ has a completion $\widehat{X}$, unique up to uniform isomorphism, in which $X$ is dense and every uniformly continuous map from $X$ to a complete uniform space extends uniquely.

**(b)** A metric space is compact if and only if it is complete and totally bounded; in particular a closed bounded subset of $\mathbb{R}^n$ is compact.

**(c)** A uniform limit of continuous functions is continuous, and a Cauchy sequence with a convergent subsequence converges.

These are established in *Metric, Uniform and Complete Spaces* for metric and uniform spaces and in *Topological Spaces* for the general theory; they are quoted here because the modes below are defined by the existence of a bound or a limit, and the existence is supplied by completeness.

## Pointwise and Uniform Convergence

Let $X$ be a set and $Y$ a metric space with distance $d$; the space of all functions $f : X \to Y$ is written $Y^X$. For the measure-theoretic statements $X$ is a measure space $(X, \mathcal{A}, \mu)$, functions are measurable and finite almost everywhere, and the scalar field is $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$; for the topological statements $X$ is a topological space and $Y$ a normed space.

### Pointwise Convergence

**Definition.** A sequence $(f_n)$ in $Y^X$ **converges pointwise** to $f$ if $f_n(x) \to f(x)$ for every $x \in X$. The notation is $f_n \to f$ pointwise.

Pointwise convergence is convergence in the product topology of $Y^X = \prod_{x \in X} Y$, and a basis of neighbourhoods of $f$ is given by the sets

$$
\{g : d(g(x_i), f(x_i)) < \epsilon \ \text{for } i = 1, \dots, k\}
$$

for finite families $x_1, \dots, x_k$ and $\epsilon > 0$. The product topology is not metrisable when $X$ is uncountable, so pointwise convergence is genuinely a net notion; it is sequential convergence in the product topology when $X$ is countable. Pointwise convergence is the weakest mode, since it constrains the values one point at a time and imposes no uniformity.

**Example (pointwise convergence is not preserved by integration).** On $([0,1], \lambda)$ let $f_n = n\,\mathbf{1}_{(0, 1/n)}$. Then $f_n \to 0$ pointwise, but $\int f_n \, d\lambda = 1$ for every $n$, so $\int f_n \not\to \int f = 0$. A single domination hypothesis repairs this, as the dominated convergence theorem of *Measure Theory and Integration* states.

**Example (pointwise converges do not preserve continuity).** On $[0,1]$ the functions $f_n(x) = x^n$ are continuous and converge pointwise to the function that is $0$ on $[0,1)$ and $1$ at $1$, which is not continuous. The limit function is measurable and bounded, so the failure is not one of measurability but of uniformity.

### Uniform Convergence

**Definition.** Let $f_n, f : X \to Y$ with $Y$ a normed space. The sequence **converges uniformly** to $f$ if

$$
\|f_n - f\|_\infty = \sup_{x \in X} \|f_n(x) - f(x)\| \longrightarrow 0 ,
$$

written $f_n \rightrightarrows f$. When the supremum is infinite the condition fails, so uniform convergence requires the differences to be bounded for all large $n$. The quantity $\|f - g\|_\infty$ is the **supremum norm** (or uniform norm) on the space $B(X, Y)$ of bounded functions.

The definition is the statement that $f_n$ lies eventually in every ball of $B(X,Y)$ about $f$, so uniform convergence is convergence in the metric of the supremum norm. It implies pointwise convergence, and the converse fails exactly when the rate of convergence depends on $x$.

**Proposition (uniform Cauchy criterion).** Let $Y$ be complete. Then $(f_n)$ converges uniformly if and only if $(f_n)$ is Cauchy for the supremum norm, that is, if and only if

$$
\sup_{x \in X} \|f_m(x) - f_n(x)\| \longrightarrow 0 \qquad (m, n \to \infty).
$$

**Proof.** Uniform convergence implies the Cauchy condition by the triangle inequality. Conversely, if the condition holds, then for each $x$ the sequence $(f_n(x))$ is Cauchy in the complete space $Y$, so it has a limit $f(x)$; given $\epsilon > 0$, choose $N$ with $\sup_x \|f_m(x) - f_n(x)\| < \epsilon$ for $m, n \geq N$ and let $m \to \infty$ in the estimate $\|f_m(x) - f_n(x)\| < \epsilon$ to get $\|f(x) - f_n(x)\| \leq \epsilon$ for all $x$ and $n \geq N$. $\square$

**Theorem.** $B(X, Y)$ with the supremum norm is a Banach space when $Y$ is a Banach space; the subspace $C_b(X,Y)$ of bounded continuous functions is closed in it, hence itself a Banach space, and a uniform limit of continuous functions is continuous.

**Proof.** The norm axioms are immediate from those of $Y$. Completeness is the uniform Cauchy criterion. If $f_n \in C_b(X,Y)$ and $f_n \rightrightarrows f$, let $x_0 \in X$ and $\epsilon > 0$; choose $n$ with $\|f_n - f\|_\infty < \epsilon/3$ and a neighbourhood $U$ of $x_0$ with $\|f_n(x) - f_n(x_0)\| < \epsilon/3$ on $U$, then $\|f(x) - f(x_0)\| \leq \epsilon$ on $U$ by the triangle inequality. $\square$

Uniform convergence is therefore the mode that is adapted to continuity: the limit of a uniformly convergent sequence of continuous functions is continuous, with the same modulus of continuity estimate, and the argument uses only the triangle inequality.

### Uniform Convergence on Compacta

**Definition.** A sequence $(f_n)$ of functions on a topological space $X$ with values in a normed space **converges uniformly on compacta** (or **locally uniformly**) to $f$ if $f_n|_K \rightrightarrows f|_K$ for every compact $K \subseteq X$; the notation is $f_n \rightrightarrows_{\mathrm{loc}} f$.

Uniform convergence implies locally uniform convergence, which implies pointwise convergence, and neither implication reverses: the functions $f_n(x) = x^n$ on $[0,1)$ converge uniformly on every compact subset of $[0,1)$ and not uniformly on $[0,1)$; the functions $f_n(x) = x/n$ on $\mathbb{R}$ converge uniformly to $0$ and the functions $f_n(x) = \min(1, |x|/n)$ converge locally uniformly but not uniformly. Locally uniform convergence is the natural mode for analytic functions, where the convergence is uniform on compacta of the domain but not on the whole domain, and for a locally compact space the two modes agree on each compact piece. On a compact space, uniformly on compacta and uniformly are the same condition.

**Theorem (Dini).** Let $X$ be compact, $f_n : X \to \mathbb{R}$ continuous and $f_n(x) \downarrow f(x)$ for every $x$, with $f$ continuous. Then $f_n \rightrightarrows f$.

**Proof.** Put $g_n = f_n - f \geq 0$, continuous and decreasing to $0$ pointwise. Given $\epsilon > 0$, the sets $U_n = \{x : g_n(x) < \epsilon\}$ are open, increase with $n$ and cover $X$; by compactness finitely many cover $X$, and since they increase, $U_N = X$ for some $N$. Hence $0 \leq g_n \leq \epsilon$ on $X$ for $n \geq N$. $\square$

Monotonicity is essential: on $[0,1]$ the functions $f_n(x) = \max(0, 1 - \lvert nx - 1\rvert)$ converge pointwise to $0$, the sequence is not monotone in $n$ at any point, and the convergence is not uniform, since $\|f_n\|_\infty = 1$ for every $n$. Dini's theorem is the standard device for upgrading a pointwise convergence that is monotone on a compact set.

**Theorem (Weierstrass $M$-test).** Let $f_n : X \to Y$, $Y$ a Banach space, satisfy $\|f_n\|_\infty \leq M_n$ with $\sum_n M_n < \infty$. Then $\sum_n f_n$ converges uniformly and absolutely, and its sum is continuous if the $f_n$ are continuous.

**Proof.** The partial sums form a Cauchy sequence for the supremum norm, since $\|\sum_{n=p}^{q} f_n\|_\infty \leq \sum_{n=p}^q M_n$, and $B(X,Y)$ is complete; continuity is the preceding theorem. $\square$

## Almost Everywhere and in Measure

Now $(X, \mathcal{A}, \mu)$ is a measure space and $f_n, f$ are measurable and finite almost everywhere; two functions equal $\mu$-a.e. are identified when a statement concerns only the measure.

### Convergence Almost Everywhere

**Definition.** $f_n \to f$ **almost everywhere** ($\mu$-a.e.) if there is a null set $N$ with $f_n(x) \to f(x)$ for every $x \notin N$; equivalently, $\mu(\limsup_n \{x : \|f_n(x) - f(x)\| > 0\}) = 0$.

Almost everywhere convergence is a statement about a set of full measure and is insensitive to the values on a null set, so it is a mode of convergence on the quotient of the measurable functions by a.e. equality. The limit is unique in that quotient. It does not imply convergence in any mean, and the example $f_n = n\mathbf{1}_{(0,1/n)}$ shows this on a space of finite measure; on a space of infinite measure the example $f_n = \mathbf{1}_{[n, n+1]}$ converges to $0$ a.e. and has $\int f_n = 1$ throughout.

**Remark (an a.e. limit need not be a pointwise limit).** Convergence a.e. is pointwise convergence after the removal of a null set. If the measure is complete, every set of measure zero is measurable and the removal changes nothing in the $\sigma$-algebra; if the measure is not complete, it is usual to pass to the completion, as in *Measure Theory and Integration*, and this article assumes a complete measure when a null set is cut out.

### Convergence in Measure

**Definition.** $f_n \to f$ **in measure**, written $f_n \xrightarrow{\mu} f$, if for every $\epsilon > 0$

$$
\mu\bigl(\{x : \|f_n(x) - f(x)\| > \epsilon\}\bigr) \longrightarrow 0 .
$$

Equivalently, for every $\epsilon > 0$ there is $N$ with $\mu(\{\|f_n - f\| > \epsilon\}) < \epsilon$ for $n \geq N$. Convergence in measure does not require the measure to be finite, and the limit is unique up to a null set.

**Theorem (a metric for convergence in measure).** On a $\sigma$-finite measure space the formula

$$
d_\mu(f, g) = \inf \Bigl\{ \epsilon > 0 : \mu\bigl(\{\|f - g\| > \epsilon\}\bigr) \leq \epsilon \Bigr\}
$$

defines a metric on the measurable functions, and $f_n \xrightarrow{\mu} f$ if and only if $d_\mu(f_n, f) \to 0$. The metric is complete, so the measurable functions modulo a.e. equality form a complete metric space under it.

**Proof sketch.** The triangle inequality uses the union bound: if $\|f - g\| \leq \epsilon$ off a set of measure $\leq \epsilon$ and $\|g - h\| \leq \delta$ off a set of measure $\leq \delta$, then $\|f - h\| \leq \epsilon + \delta$ off the union, of measure $\leq \epsilon + \delta$. The stated equivalence follows from the definitions, and completeness is proved by extracting a subsequence that converges a.e. and applying the Cauchy condition to its differences. $\square$

The metric $d_\mu$ is a device of convenience; the defining statement is the measure estimate. On a finite measure space one may use $d_\mu(f,g) = \int \min(1, \|f - g\|) \, d\mu$ instead, whose convergence to zero is equivalent to convergence in measure.

### The Relations Between the Modes

**Theorem (Egorov).** Let $\mu(X) < \infty$ and $f_n \to f$ a.e., with the $f_n$ measurable. Then for every $\epsilon > 0$ there is a measurable set $E$ with $\mu(E) < \epsilon$ such that $f_n \rightrightarrows f$ on $X \setminus E$: the convergence is **almost uniform**. In particular $f_n \xrightarrow{\mu} f$.

**Proof.** For fixed $k$ the sets $E_{n,k} = \bigcup_{m \geq n} \{\|f_m - f\| > 1/k\}$ decrease as $n$ increases and, by a.e. convergence, have intersection null; finiteness of the measure gives $\mu(E_{n,k}) \to 0$ as $n \to \infty$. Choose $n_k$ with $\mu(E_{n_k,k}) < \epsilon/2^k$ and put $E = \bigcup_k E_{n_k,k}$, of measure $< \epsilon$. On $X \setminus E$ one has $\|f_m - f\| \leq 1/k$ for $m \geq n_k$, since a point outside $E$ lies outside every $E_{n_k,k}$, so the convergence is uniform. $\square$

**Theorem (Riesz).** If $f_n \xrightarrow{\mu} f$ then some subsequence converges to $f$ a.e.

**Proof.** Choose $n_1 < n_2 < \cdots$ with $\mu(\{\|f_{n_k} - f\| > 2^{-k}\}) \leq 2^{-k}$; the Borel–Cantelli lemma makes the limsup of these sets null, and off it $\|f_{n_k} - f\| \leq 2^{-k}$ for all large $k$. $\square$

**Theorem (convergence a.e. versus in measure).** If $\mu(X) < \infty$, convergence a.e. implies convergence in measure. The converse fails: on $[0,1]$ the indicator functions of the dyadic intervals $\bigl[k/2^m, (k+1)/2^m\bigr)$, enumerated with $m$ increasing and $k = 0, \dots, 2^m - 1$ for each $m$, converge to $0$ in measure and have no pointwise limit at any point of $[0,1)$.

**Proof.** The forward implication is Egorov's theorem. For the example, the $n$-th function in the enumeration has support of length $2^{-m}$, so it converges to $0$ in measure; but for every $x \in [0,1)$ the value $1$ occurs for one $k$ at each level $m$ with $k \leq 2^m x < k+1$, hence infinitely often, so the sequence does not converge at $x$. $\square$

The exact relation is therefore: a.e. convergence and convergence in measure do not imply one another on a general space, on a finite measure space a.e. convergence implies convergence in measure, and in measure convergence implies a.e. convergence along a subsequence. Both are implied by almost uniform convergence, which on a finite measure space is equivalent to a.e. convergence by Egorov. The four modes and their implications are tabulated in the closing section.

**Example (convergence in measure without a dominating function).** On $([0,1], \lambda)$ let $g_n = n\,\mathbf{1}_{(0,1/n)}$. Then $g_n \to 0$ in measure and in fact a.e., but $\int g_n = 1$ for all $n$, so no domination by an integrable function can hold and the conclusion of the dominated convergence theorem fails. Convergence in measure controls the size of the set where the functions are large, not the size of the values.

## Convergence in $L^p$

### Definition and Completeness

Let $1 \leq p \leq \infty$ and let $L^p(\mu)$ be the Lebesgue space of *Measure Theory and Integration*, a Banach space for the norm $\|f\|_p = (\int \|f\|^p \, d\mu)^{1/p}$ when $p < \infty$, and $\|f\|_\infty$ the essential supremum when $p = \infty$.

**Definition.** $f_n \to f$ **in $L^p$**, written $f_n \xrightarrow{L^p} f$, if $\|f_n - f\|_p \to 0$.

Convergence in $L^p$ is convergence in the metric of the norm, and it is a mode of convergence of the functions themselves, not of their values: the functions are identified when they agree a.e., and both the hypothesis and the conclusion are insensitive to null sets.

**Theorem (Riesz–Fischer).** $L^p(\mu)$ is complete for every $1 \leq p \leq \infty$.

**Theorem (relations with the other modes).** Let $f_n, f \in L^p(\mu)$.

**(a)** Convergence in $L^p$ implies convergence in measure, for every $p < \infty$, by Chebyshev's inequality $\mu(\{\|f_n - f\| > \epsilon\}) \leq \epsilon^{-p} \|f_n - f\|_p^p$, with no hypothesis on the measure.

**(b)** Convergence in measure does not imply convergence in $L^p$, by the sequence $g_n = n^{1/p}\mathbf{1}_{(0,1/n)}$, which converges to $0$ a.e. and in measure and has $\|g_n\|_p = 1$.

**(c)** Convergence in $L^p$ does not imply convergence a.e.; the sliding dyadic intervals of the previous section converge to $0$ in $L^p$ for every finite $p$ and converge at no point of $[0,1)$.

**(d)** Convergence a.e. does not imply convergence in $L^p$, by the same sequence $g_n$.

**(e)** If $\mu(X) < \infty$ and $q \geq p$ then $L^q(\mu) \subseteq L^p(\mu)$ and convergence in $L^q$ implies convergence in $L^p$; the inclusion reverses for a counting measure on a countable set.

The three counterexamples are the standard ones and should be read as a single table of failures, given in the closing section.

### Uniform Integrability and the Vitali Theorem

**Definition.** A family $\mathcal{F} \subseteq L^1(\mu)$ is **uniformly integrable** if

$$
\lim_{c \to \infty} \sup_{f \in \mathcal{F}} \int_{\{\|f\| > c\}} \|f\| \, d\mu = 0 .
$$

On a finite measure space this is equivalent to the conjunction of boundedness in $L^1$ and the condition that for every $\epsilon > 0$ there is $\delta > 0$ with $\mu(A) < \delta \Rightarrow \sup_f \int_A \|f\| \, d\mu < \epsilon$; the second condition is what rules out the concentration of mass on small sets seen in the example $g_n$.

**Theorem (Vitali convergence theorem).** Let $\mu(X) < \infty$, let $f_n \to f$ in measure and suppose the family $\{f_n\}$ is uniformly integrable and $f \in L^1$. Then $f_n \to f$ in $L^1$.

**Proof sketch.** Given $\epsilon > 0$, uniform integrability gives $c$ with $\sup_n \int_{\{|f_n| > c\}} |f_n| < \epsilon$; Fatou's lemma applied to a subsequence gives the same estimate for $f$. Split $|f_n - f| \leq 2c$ on the set where both are bounded by $c$ and use convergence in measure to make the integral of the bounded part small, and the tail estimate for the rest. $\square$

**Corollary (the dominated convergence theorem).** If $f_n \to f$ a.e. and $|f_n| \leq g$ with $g \in L^1$, then the family is uniformly integrable and $f_n \to f$ in $L^1$.

Uniform integrability is thus the exact replacement for a dominating function: it is the hypothesis under which convergence in measure upgrades to convergence in $L^1$, and it is the hypothesis used in the martingale theory of the probability articles of this Part.

## Weak and Weak-$\ast$ Convergence

### The Weak Topology

Let $X$ be a normed space over $\mathbb{K}$ with dual $X'$, the Banach space of bounded linear functionals. The notation is that of *Normed and Banach Spaces* and *Duality Theory*.

**Definition.** A sequence $(x_n)$ in $X$ **converges weakly** to $x \in X$, written $x_n \rightharpoonup x$, if $\varphi(x_n) \to \varphi(x)$ for every $\varphi \in X'$. The **weak topology** $\sigma(X, X')$ is the coarsest topology making every $\varphi \in X'$ continuous; it is locally convex and Hausdorff, and weak convergence is convergence in it.

**Theorem (properties of weak convergence).**

**(a)** Weak limits are unique; $x_n \rightharpoonup x$ implies $x_n$ is bounded, and $\|x\| \leq \liminf_n \|x_n\|$, so the norm is weakly lower semicontinuous.

**(b)** Norm convergence implies weak convergence; the converse fails unless $X$ is finite-dimensional, by the sequence $e_n$ of unit vectors of $\ell^2$, which satisfies $\langle e_n, y \rangle \to 0$ for every $y$ and has $\|e_n\| = 1$.

**(c)** If $x_n \rightharpoonup x$ and $\|x_n\| \to \|x\|$, then $x_n \to x$ in norm when $X$ is uniformly convex, in particular when $X$ is a Hilbert space.

**(d)** (Mazur) Every norm-closed convex subset of $X$ is weakly closed, and the weak closure of a convex set is its norm closure; equivalently, every weak limit is a norm limit of convex combinations.

**Proof sketch.** (a) A weakly convergent sequence is pointwise bounded on $X'$, hence bounded by the uniform boundedness principle, a consequence of Baire's theorem for the complete space $X'$; in a Hilbert space it follows alternatively from the uniform boundedness principle applied to the functionals $x \mapsto \langle x_n, x \rangle$. Lower semicontinuity of the norm is the estimate $\|\varphi(x)\| \leq \liminf \|\varphi(x_n)\| \leq \|\varphi\| \liminf \|x_n\|$ followed by the Hahn–Banach theorem. (c) Expanding $\|x_n - x\|^2 = \|x_n\|^2 - 2\operatorname{Re}\langle x_n, x\rangle + \|x\|^2$ in a Hilbert space. (d) The second dual statement is the Hahn–Banach separation theorem, from *Duality Theory*. $\square$

### Weak-$\ast$ Convergence

**Definition.** Let $X$ be a normed space and $X'$ its dual. A sequence $(\varphi_n) \subseteq X'$ **converges weak-$\ast$** to $\varphi \in X'$, written $\varphi_n \xrightarrow{w^*} \varphi$, if $\varphi_n(x) \to \varphi(x)$ for every $x \in X$. The weak-$\ast$ topology $\sigma(X', X)$ is the coarsest making the evaluations $x : X' \to \mathbb{K}$ continuous.

**Theorem (Banach–Alaoglu).** The closed unit ball of $X'$ is compact in the weak-$\ast$ topology. If $X$ is separable, the weak-$\ast$ topology on the ball is metrisable, so the ball is sequentially compact.

Weak-$\ast$ convergence is weaker than weak convergence on $X'$; the two coincide when $X$ is reflexive. The sequence $e_n$ in $\ell^1 = (c_0)'$ satisfies $e_n(x) = x_n \to 0$ for every $x \in c_0$, so $e_n \xrightarrow{w^*} 0$, while $e_n$ has no weak limit in $\ell^1$: the functional $\varphi(y) = \sum_n y_n$ in $(\ell^1)' = \ell^\infty$ has $\varphi(e_n) = 1$ for every $n$, so the only possible weak limit, forced to be $0$ by testing against the coordinate functionals, is not one. Banach–Alaoglu is the compactness theorem that produces minimisers in the variational arguments , and it is the source of the compactness in the duality theory.

### Convergence of Measures

Let $X$ be a locally compact Hausdorff space and let $M(X)$ be the space of finite signed Radon measures, identified by the Riesz representation theorem with the dual of $C_0(X)$, the continuous functions vanishing at infinity, in the norm of total variation.

**Definition.** A sequence $(\mu_n) \subseteq M(X)$ **converges weakly** to $\mu$ if $\int \varphi \, d\mu_n \to \int \varphi \, d\mu$ for every $\varphi \in C_0(X)$; it **converges vaguely** if this holds for every $\varphi \in C_c(X)$, the continuous functions of compact support. On a compact $X$ the two agree.

**Theorem (portmanteau).** For finite positive measures on a metric space $X$, weak convergence of $\mu_n$ to $\mu$ is equivalent to each of: $\limsup_n \mu_n(F) \leq \mu(F)$ for every closed $F$; $\liminf_n \mu_n(U) \geq \mu(U)$ for every open $U$; $\mu_n(A) \to \mu(A)$ for every Borel $A$ with $\mu(\partial A) = 0$; and $\int \varphi \, d\mu_n \to \int \varphi \, d\mu$ for every bounded uniformly continuous $\varphi$.

**Example (approximation of the Dirac measure).** On $\mathbb{R}$ let $\mu_n$ be the measure with density $n\,\mathbf{1}_{[0,1/n]}$ with respect to Lebesgue measure. Then $\int \varphi \, d\mu_n \to \varphi(0)$ for every $\varphi \in C_c(\mathbb{R})$, so $\mu_n$ converges vaguely, and weakly, to the Dirac measure $\delta_0$. The sequence of densities converges to $0$ a.e.; the convergence of the measures is a different statement from the a.e. convergence of the densities, and the distinction is the one between the mode of the previous sections and the mode of this one.

These definitions are the ones used for the convergence of measures, and for the convergence of the invariant measures in the ergodic theory of the Part.

## Interchange of Limits

The purpose of distinguishing the modes is that each is the hypothesis of a theorem in which two limits are exchanged. The results of this section are the ones used constantly in the remainder of the Part; the measure-theoretic ones are stated in *Measure Theory and Integration* and are collected here in the vocabulary of this article.

### Limit and Integral

**Theorem.** Let $f_n : X \to \mathbb{K}$ be measurable on the measure space $(X, \mathcal{A}, \mu)$.

**(a) (monotone convergence)** If $0 \leq f_n \uparrow f$ a.e. then $\int f_n \to \int f$, both sides in $[0, +\infty]$.

**(b) (Fatou)** If $f_n \geq 0$ a.e. then $\int \liminf_n f_n \leq \liminf_n \int f_n$.

**(c) (dominated convergence)** If $f_n \to f$ a.e. and $\|f_n\| \leq g$ with $g \in L^1$, then $\int f_n \to \int f$ and $f_n \to f$ in $L^1$.

**(d) (uniform convergence on a finite measure space)** If $\mu(X) < \infty$ and $f_n \rightrightarrows f$, then $f_n \to f$ in $L^1$ and $\int f_n \to \int f$.

Hypothesis (c) cannot be replaced by convergence in measure alone, by the example $g_n = n\mathbf{1}_{(0,1/n)}$, and the finiteness of the measure cannot be dropped in (d): the functions $\mathbf{1}_{[n,n+1]}$ on $\mathbb{R}$ converge to $0$ uniformly on compacta, and hence pointwise, while $\int \mathbf{1}_{[n,n+1]} \, d\lambda = 1$ for every $n$. The uniform-integrability theorem of the preceding section is the exact intermediate hypothesis.

### Limit and Derivative

**Theorem.** Let $f_n : (a,b) \to \mathbb{R}$ be differentiable with $f_n(x_0)$ convergent for some $x_0$ and $f_n' \rightrightarrows g$ uniformly on $(a,b)$. Then $f_n$ converges uniformly to a differentiable $f$ with $f' = g$, and

$$
\frac{d}{dx} \lim_{n} f_n = \lim_n \frac{d}{dx} f_n .
$$

**Proof sketch.** For $x \in (a,b)$ the mean value theorem gives $\|f_m(x) - f_n(x) - (f_m(x_0) - f_n(x_0))\| \leq \|f_m' - f_n'\|_\infty \, |x - x_0|$; the uniform Cauchy hypothesis for the derivatives and the convergence at $x_0$ therefore imply the uniform Cauchy condition for the $f_n$, so there is a uniform limit $f$. Passing to the limit in the difference quotient, the same estimate shows that $f$ is differentiable with derivative $g$. $\square$

The theorem uses the mean value theorem and hence the order of $\mathbb{R}$; it has no general form in a non-Archimedean field, where the mean value theorem fails, and the appropriate substitute in that setting is discussed. Pointwise convergence of the derivatives does not suffice: the functions $f_n(x) = x^n/n$ on $[0,1]$ converge uniformly to $0$, their derivatives $x^{n-1}$ converge pointwise to $0$ on $[0,1)$ and to $1$ at $1$, and the limit of the derivatives is not the derivative of the limit at $1$.

### Limit and Infinite Sum

**Theorem.** Let $f_n : X \to Y$ with $Y$ a Banach space and suppose $\sum_n \|f_n\|_\infty < \infty$. Then $\sum_n f_n$ converges uniformly and absolutely, and

$$
\sum_n \int_X f_n \, d\mu = \int_X \Bigl( \sum_n f_n \Bigr) d\mu, \qquad \frac{d}{dx} \sum_n f_n = \sum_n f_n'
$$

whenever the right-hand side converges uniformly and the functions are differentiable; the first identity requires the $f_n$ integrable and $\sum_n \int \|f_n\| < \infty$.

The hypotheses are those of the Weierstrass $M$-test together with the two preceding theorems applied to the partial sums. The interchange of a sum and an integral is the monotone or dominated convergence theorem applied to the partial sums, and the interchange with a derivative is the derivative theorem applied to them.

## The Vocabulary and the Implications

The modes fixed by this article, with their notation, are the following.

| Mode | Notation | Definition |
|---|---|---|
| Pointwise | $f_n \to f$ pointwise | $f_n(x) \to f(x)$ for every $x$ |
| Uniform | $f_n \rightrightarrows f$ | $\sup_x \|f_n(x) - f(x)\| \to 0$ |
| Locally uniform | $f_n \rightrightarrows_{\mathrm{loc}} f$ | uniform on every compact set |
| Almost everywhere | $f_n \to f$ $\mu$-a.e. | pointwise off a $\mu$-null set |
| Almost uniform | $f_n \rightrightarrows f$ off $E$, $\mu(E) < \epsilon$ | Egorov's conclusion |
| In measure | $f_n \xrightarrow{\mu} f$ | $\mu(\{\|f_n - f\| > \epsilon\}) \to 0$ |
| In $L^p$ | $f_n \xrightarrow{L^p} f$ | $\|f_n - f\|_p \to 0$ |
| Weak | $f_n \rightharpoonup f$ | $\varphi(f_n) \to \varphi(f)$ for all $\varphi \in X'$ |
| Weak-$\ast$ | $f_n \xrightarrow{w^*} f$ | $f_n(x) \to f(x)$ for all $x \in X$, the $f_n$ lying in $X'$ |
| Weakly (of measures) | $\mu_n \to \mu$ | $\int \varphi \, d\mu_n \to \int \varphi \, d\mu$, $\varphi \in C_0(X)$ |

The implication scheme is the following; every arrow is an implication, and every omitted arrow is false in general.

| Hypothesis $\backslash$ Conclusion | pointwise | a.e. | in measure | $L^p$ |
|---|---|---|---|---|
| uniform | yes | yes | yes, $\mu$ finite | yes on finite measure |
| locally uniform | yes | yes | on compacta | on compacta |
| almost everywhere | no | — | yes, $\mu$ finite | no |
| in measure | no | subsequence | — | no |
| in $L^p$ | no | no | yes | — |

The three failures that account for the gaps are: the sequence $n\mathbf{1}_{(0,1/n)}$ (in measure and a.e., not in $L^1$, no domination); the sliding dyadic intervals (in $L^p$ and in measure, a.e. along no full sequence); and the sequence $x^n$ on $[0,1]$ (pointwise, not uniform). Uniform convergence is the only mode that survives every operation of elementary analysis without a supplementary hypothesis of integrability or of compactness.

## Summary

Convergence in analysis is carried by several inequivalent modes, and this article fixes them for the whole of Part III. On a function space they are pointwise convergence, uniform convergence and uniform convergence on compacta; in measure theory they are convergence almost everywhere, almost uniformly, in measure and in $L^p$; in the normed and locally convex setting they are weak and weak-$\ast$ convergence, and for measures they are weak and vague convergence.

Uniform convergence is convergence in the supremum norm: it is characterised by the uniform Cauchy criterion, it turns the bounded functions on a complete space into a Banach space, and it is the mode that preserves continuity. Pointwise convergence is convergence in the product topology and preserves no continuity and no integral. Dini's theorem upgrades a monotone pointwise convergence on a compact space to uniform convergence, and the Weierstrass $M$-test upgrades an absolutely summable family to a uniformly convergent series.

On a measure space, convergence a.e. is pointwise convergence off a null set — a strictly weaker condition than pointwise convergence — and it neither implies nor is implied by convergence in measure; on a finite measure space it implies convergence in measure and is equivalent to almost uniform convergence by Egorov's theorem, while convergence in measure implies a.e. convergence along a subsequence by Riesz's theorem. Convergence in $L^p$ implies convergence in measure, is implied by it together with uniform integrability, and is controlled by the Vitali theorem; the dominated convergence theorem is its principal special case. In a normed space weak convergence is convergence of the values under every bounded functional, boundedness and lower semicontinuity of the norm accompany it, and weak-$\ast$ convergence on a dual space is governed by the Banach–Alaoglu theorem. For measures, weak convergence is the weak-$\ast$ convergence of the associated functionals on $C_0(X)$, and the portmanteau theorem gives its equivalent forms.

Finally, each mode is the hypothesis of an interchange theorem: the monotone, Fatou and dominated convergence theorems for the integral, the uniform convergence of the derivatives for the derivative, and the Weierstrass test for an infinite sum. The counterexamples of this article mark the boundary of each.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $x_n \to x$, $x_\lambda \to x$ | Convergence of a sequence, of a net |
| $f_n \to f$ pointwise | Pointwise convergence of functions |
| $f_n \rightrightarrows f$ | Uniform convergence |
| $f_n \rightrightarrows_{\mathrm{loc}} f$ | Uniform convergence on compacta (locally uniform) |
| $\|f\|_\infty$ | Supremum norm, essential supremum in the measure setting |
| $B(X, Y)$, $C_b(X, Y)$ | Bounded functions, bounded continuous functions |
| $f_n \to f$ $\mu$-a.e. | Convergence almost everywhere |
| $f_n \xrightarrow{\mu} f$ | Convergence in measure |
| $d_\mu$ | Metric for convergence in measure |
| $f_n \xrightarrow{L^p} f$, $\|f\|_p$ | Convergence in $L^p$, $L^p$ norm |
| uniform integrability | $\lim_{c \to \infty} \sup_f \int_{\{|f| > c\}} \lvert f \rvert \, d\mu = 0$ |
| $X'$ | Dual space of a normed space |
| $x_n \rightharpoonup x$, $\sigma(X, X')$ | Weak convergence and weak topology |
| $\varphi_n \xrightarrow{w^*} \varphi$, $\sigma(X', X)$ | Weak-$\ast$ convergence and weak-$\ast$ topology |
| $\mu_n \to \mu$ | Weak convergence of measures, $\int \varphi \, d\mu_n \to \int \varphi \, d\mu$ |
| $M(X)$, $C_0(X)$, $C_c(X)$ | Finite Radon measures, functions vanishing at infinity, compact support |
| $\mathbf{1}_A$ | Indicator of a set |
| $L^p(\mu)$ | Lebesgue space |









## Further Reading

- Walter Rudin, *Principles of Mathematical Analysis*, 3rd ed. (McGraw-Hill, 1976), for uniform convergence, Dini's theorem and the interchange of limit and derivative.
- Walter Rudin, *Real and Complex Analysis*, 3rd ed. (McGraw-Hill, 1987), for the measure-theoretic modes, Egorov's theorem and the $L^p$ theory.
- Paul R. Halmos, *Measure Theory* (Van Nostrand, 1950; reprinted Springer, 1974), for convergence in measure and uniform integrability.
- Gerald B. Folland, *Real Analysis: Modern Techniques and Their Applications*, 2nd ed. (Wiley, 1999), for the modes of convergence collected with their counterexamples and for the weak topologies.
- Nelson Dunford and Jacob T. Schwartz, *Linear Operators, Part I* (Interscience, 1958), for weak and weak-$\ast$ convergence, Banach–Alaoglu and the uniform boundedness principle.
- K. R. Parthasarathy, *Probability Measures on Metric Spaces* (Academic Press, 1967), for the portmanteau theorem and weak convergence of measures.
- Patrick Billingsley, *Convergence of Probability Measures*, 2nd ed. (Wiley, 1999), for the theory of weak convergence of measures in the metric setting.
- Kosaku Yosida, *Functional Analysis*, 6th ed. (Springer, 1980), for the functional-analytic convergence theorems and their hypotheses.
