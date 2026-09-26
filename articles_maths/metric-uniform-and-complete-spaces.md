
# __Metric, Uniform and Complete Spaces__

## Introduction

A topological space remembers which sets are open, and nothing more; the real line has more structure than , because distances between points can be compared. This article develops the two layers that sit between topology and analysis: **metric spaces**, where a distance function is given, and **uniform spaces**, where only the family of entourages — the relations "closer than $\epsilon$" — is remembered. The distinction matters because the notions the corpus needs most are not topological. Cauchy sequences, completeness, uniform continuity and uniform convergence are properties of a metric or of a uniformity, and a homeomorphism can destroy all of them: the open interval $(0, 1)$ is homeomorphic to $\mathbb{R}$ but is not complete, and the map $x \mapsto 1/x$ is a homeomorphism of $(0, 1)$ onto $(1, \infty)$ that is not uniformly continuous. The uniform structure is exactly what survives, and it is the structure a topological group carries, which is why the completion of a topological group is a construction in uniform spaces rather than in topological spaces. This article is the second of the three preparation articles; the last chapter, **Baire category**, supplies the counting arguments that measure theory and functional analysis use.

Throughout, $R$ denotes a commutative ring with identity $1 \neq 0$ and $F$, $K$ denote fields; the metric examples are mostly $\mathbb{R}$, $\mathbb{C}$ and their powers, and $\mathbb{K}$ means $\mathbb{R}$ or $\mathbb{C}$ when only those two are meant. The topological background — open and closed sets, continuity, products and quotients, nets and filters, compactness — is assumed, and the concrete theory of the real line likewise. No physics is invoked.

## Metric Spaces

### Metrics and the Metric Topology

**Definition.** A **metric** on a set $X$ is a function $d : X \times X \to \mathbb{R}$ such that for all $x, y, z \in X$,

$$
d(x, y) \geq 0, \qquad d(x, y) = 0 \iff x = y, \qquad d(x, y) = d(y, x), \qquad d(x, z) \leq d(x, y) + d(y, z).
$$

The pair $(X, d)$ is a **metric space**; the last condition is the **triangle inequality**. Dropping the separation requirement $d(x, y) = 0 \Rightarrow x = y$ gives a **pseudometric**; a pseudometric fails to distinguish the points at distance zero, and the induced topology on the quotient by that relation is the one carried by the associated metric space.

**Definition.** The **open ball** of radius $r > 0$ about $x$ is $B(x, r) = \{y : d(x, y) < r\}$, and the **closed ball** is $\overline{B}(x, r) = \{y : d(x, y) \leq r\}$. The **metric topology** is the family of unions of open balls; the balls form a base for it and the balls of rational radius form a neighbourhood base at each point.

**Theorem.** The metric topology is a topology, and it is Hausdorff, first countable, normal and metrisable by construction. A set $U$ is open exactly when for every $x \in U$ there is $r > 0$ with $B(x, r) \subseteq U$.

**Pro.** The empty union gives $\emptyset$ and $X = \bigcup_{x} B(x, 1)$; arbitrary unions of balls are open by definition, and if $U, V$ are open and $x \in U \cap V$ choose $r_1, r_2$ with $B(x, r_i)$ inside the respective set; then $B(x, \min(r_1, r_2)) \subseteq U \cap V$. Hausdorffness uses $d(x, y) > 0$ and the balls of radius $d(x,y)/2$; first countability uses the rational radii; normality is shown. $\square$

**Example (Euclidean spaces).** On $\mathbb{K}^n$ the **Euclidean metric** is $d(x, y) = \left(\sum_{i=1}^n |x_i - y_i|^2\right)^{1/2}$, and the **sup metric** $d_\infty(x, y) = \max_i |x_i - y_i|$ induces the same topology; both are special cases of the $\ell^p$ metrics for $1 \leq p \leq \infty$.

**Example (discrete and induced metrics).** The **discrete metric** is $d(x, y) = 1$ for $x \neq y$, giving the discrete topology. Any subset $A$ of a metric space is a metric space with the restricted metric, and its metric topology is the subspace topology.

**Example ($p$-adic metric).** On $\mathbb{Q}$ fix a prime $p$ and put $d(x, y) = p^{-v_p(x - y)}$, where $v_p$ is the exponent of $p$ in the rational $x - y$ and $v_p(0) = +\infty$. The strong triangle inequality $d(x, z) \leq \max(d(x,y), d(y,z))$ holds, so the metric is **ultrametric** and every triangle is isosceles with the two longer sides equal. The completion is the field $\mathbb{Q}_p$ of $p$-adic numbers, and the same construction applied to a field with an absolute value gives its completion.

### Equivalent Metrics

**Definition.** Two metrics $d_1, d_2$ on $X$ are **topologically equivalent** if they induce the same topology, **strongly equivalent** if there are constants $c, C > 0$ with $c\,d_1 \leq d_2 \leq C\,d_1$, and **uniformly equivalent** if for every $\epsilon > 0$ there are $\delta_1, \delta_2 > 0$ with $d_1(x, y) < \delta_1 \Rightarrow d_2(x, y) < \epsilon$ and $d_2(x, y) < \delta_2 \Rightarrow d_1(x, y) < \epsilon$.

**Proposition.** Strong equivalence implies uniform equivalence, which implies topological equivalence; neither converse holds in general. Two metrics $d_1, d_2$ are uniformly equivalent exactly when they have the same uniformly continuous maps into every metric space, and exactly when they have the same Cauchy sequences.

**Proof.** The implications are immediate from the definitions. For the failure of the converses, the usual metric $|x - y|$ on $\mathbb{R}$ and the metric $|\arctan x - \arctan y|$ induce the same topology but not the same uniformity, since points far apart can be made $\arctan$-close: with $x = M$ and $y = M + 1$ the first distance is $1$ while the second tends to $0$ as $M \to \infty$. On the other hand $d$ and $\min(d, 1)$ are uniformly equivalent but not strongly equivalent. $\square$

The point is that the metric, and not merely its topology, controls Cauchy sequences. Completeness is therefore a property of the metric or of the uniform structure, and not of the topology.

## Continuity, Lipschitz Maps and Isometries

### Continuity and Lipschitz Conditions

**Definition.** A map $f : X \to Y$ between metric spaces is **continuous at** $x$ if for every $\epsilon > 0$ there is $\delta > 0$ with $d_X(x, x') < \delta \Rightarrow d_Y(f(x), f(x')) < \epsilon$; it is **continuous** if continuous at every point. It is **uniformly continuous** if for every $\epsilon > 0$ there is $\delta > 0$ such that $d_X(x, x') < \delta \Rightarrow d_Y(f(x), f(x')) < \epsilon$ for all $x, x'$; the difference is that $\delta$ no longer depends on the point.

**Definition.** $f$ is **Lipschitz** with constant $L \geq 0$ if $d_Y(f(x), f(x')) \leq L\,d_X(x, x')$ for all $x, x'$, and a **contraction** if it is Lipschitz with $L < 1$. It is an **isometry** if $d_Y(f(x), f(x')) = d_X(x, x')$ for all $x, x'$.

**Proposition.** Lipschitz implies uniformly continuous, which implies continuous. An isometry is injective and uniformly continuous, and a bijective isometry is a homeomorphism whose inverse is an isometry.

**Proof.** Given $L$, take $\delta = \epsilon / \max(L, 1)$; given uniform continuity, take $\delta$ at the point; injectivity of an isometry follows from $d_Y(f(x), f(x')) = 0 \Rightarrow x = x'$. $\square$

**Theorem (Banach fixed point theorem).** Let $(X, d)$ be a complete metric space and let $f : X \to X$ be a contraction with constant $L < 1$. Then $f$ has exactly one fixed point $x^*$, and for every $x_0 \in X$ the iterates $x_{n+1} = f(x_n)$ converge to $x^*$ with the estimate

$$
d(x_n, x^*) \leq \frac{L^n}{1 - L} \, d(x_1, x_0).
$$

**Proof.** For $m > n$, the triangle inequality and the geometric bound give $d(x_n, x_m) \leq \frac{L^n}{1-L} d(x_1, x_0)$, so $(x_n)$ is Cauchy; let $x^*$ be its limit, which exists by completeness. Continuity of $f$ gives $f(x^*) = \lim f(x_n) = \lim x_{n+1} = x^*$. If $y$ is another fixed point, then $d(x^*, y) = d(f(x^*), f(y)) \leq L\,d(x^*, y)$, forcing $d(x^*, y) = 0$. The estimate follows by letting $m \to \infty$. $\square$

The theorem is the standard existence proof for solutions of differential and integral equations: the solution operator is a contraction on a suitable complete space of functions, and completeness is exactly the hypothesis the argument consumes.

**Example (the missing point).** On the incomplete space $X = (0, 1]$ with the usual metric, the map $f(x) = x/2$ is a contraction with $L = 1/2$, and the iterates from $x_0$ are $x_n = x_0/2^n$, a Cauchy sequence whose limit $0$ lies outside $X$: the map has no fixed point in $X$. The single missing point is precisely what the theorem needs, so completeness cannot be dropped. On $X = [0, 1]$ the map $f(x) = (x+1)/3$ has $L = 1/3$ and fixed point $x^* = 1/2$; from $x_0 = 0$ the iterates are

$$
x_n = \tfrac{1}{2} - \tfrac{1}{2 \cdot 3^n}, \qquad d(x_n, x^*) = \frac{1}{2 \cdot 3^n},
$$

and the estimate of the theorem gives $\frac{L^n}{1-L} d(x_1, x_0) = \frac{(1/3)^n}{2/3}\cdot\frac{1}{3} = \frac{1}{2\cdot 3^n}$, the same number: the bound is attained.

**Example (an integral equation).** On the complete space $C([0,1])$ with the sup metric, the operator

$$
(Tf)(x) = 1 + \tfrac{1}{2}\int_0^x f(t)\,dt
$$

satisfies $\|Tf - Tg\|_\infty \leq \tfrac{1}{2}\|f - g\|_\infty$, so it is a contraction with $L = 1/2$ and therefore has exactly one fixed point. Starting from $f_0 = 1$ the iterates are the partial sums

$$
f_n(x) = \sum_{k=0}^{n} \frac{1}{k!}\left(\frac{x}{2}\right)^{k},
$$

by induction on $n$, since integrating the $k$-th term of $f_n$ produces the $(k+1)$-st term of $f_{n+1}$; the limit is $f(x) = e^{x/2}$, the solution of the initial value problem $f' = f/2$, $f(0) = 1$. The error estimate reads $\|f_n - f\|_\infty \leq \frac{(1/2)^n}{1 - 1/2}\cdot\frac{1}{2} = 2^{-n}$, and the supremum of the error is attained at $x = 1$, since every term of the series increases with $x$; there the error is the tail of $\sum_k (1/2)^k/k!$ and is smaller than the bound. This is the Picard iteration for the equation, and it shows why the complete space has to be a space of functions rather than a space of points.

### Isometries and the Failure of Topological Invariance

**Definition.** Metric spaces $X, Y$ are **isometric** if there is a bijective isometry $X \to Y$; an isometry of a metric space onto itself is an **isometry** of the space, and the isometries form a group under composition.

**Example.** The isometry group of $\mathbb{R}^n$ with the Euclidean metric is the Euclidean group $E(n) = \mathbb{R}^n \rtimes O(n)$, the semidirect product of the translations with the orthogonal group; the isometry group of the sphere $S^{n-1}$ with the chordal metric is $O(n)$.

**Remark.** Isometric spaces are homeomorphic, but not conversely: $(0,1)$ with the usual metric is homeomorphic to $\mathbb{R}$ by $x \mapsto \tan(\pi(x - 1/2))$, yet the two are not isometric, since $\mathbb{R}$ is complete and $(0,1)$ is not and isometry preserves Cauchy sequences. This is the cleanest illustration that completeness is uniform and not topological.

## Cauchy Sequences and Completeness

### Cauchy Sequences

**Definition.** A sequence $(x_n)$ in a metric space is **Cauchy** if for every $\epsilon > 0$ there is $N$ with $m, n \geq N \Rightarrow d(x_m, x_n) < \epsilon$. Every convergent sequence is Cauchy, and every Cauchy sequence is bounded.

**Proposition.** Let $f : X \to Y$ be uniformly continuous and let $(x_n)$ be Cauchy in $X$. Then $(f(x_n))$ is Cauchy in $Y$. Continuity alone does not suffice: the homeomorphism $x \mapsto 1/x$ of $(0,1)$ onto $(1,\infty)$ carries the Cauchy sequence $1/n$ to the unbounded sequence $n$.

**Proof.** Given $\epsilon$ choose $\delta$ for uniform continuity and $N$ for the Cauchy condition; then $m, n \geq N$ gives $d_Y(f(x_m), f(x_n)) < \epsilon$. For the counterexample, $d(f(1/n), f(1/m)) = |n - m|$ is unbounded. $\square$

### Complete Spaces

**Definition.** A metric space is **complete** if every Cauchy sequence converges. A subset $A$ of a metric space is complete if it is complete in the restricted metric.

**Theorem.** A subspace $A$ of a complete metric space $X$ is complete if and only if $A$ is closed in $X$.

**Proof.** If $A$ is closed and $(a_n)$ is Cauchy in $A$, it converges in $X$ to some $x$, which lies in $\overline A = A$; so $A$ is complete. Conversely, if $A$ is complete and $x \in \overline A$, choose $a_n \in A$ with $d(a_n, x) < 1/n$; then $(a_n)$ is Cauchy, so it converges to a point of $A$, which must be $x$; hence $A$ is closed. $\square$

**Theorem.** $\mathbb{K}^n$ with the Euclidean metric is complete. More generally, a finite product of complete metric spaces, with any of the standard product metrics, is complete.

**Pro.** A Cauchy sequence in $\mathbb{K}^n$ has Cauchy coordinate sequences, since each coordinate difference is bounded by the norm of the difference. By completeness of $\mathbb{K}$ , each coordinate converges, and the coordinatewise limit is the limit of the sequence because finitely many coordinates are involved. $\square$

**Example.** $\mathbb{R}^n$ is complete; so is every closed subset of it. The rationals $\mathbb{Q}$ with $|x - y|$ are not complete, the sequence of decimal truncations of $\sqrt{2}$ being Cauchy without a rational limit; nor is $(0, 1)$, nor $\mathbb{Q}$ with the $p$-adic metric, whose completion is $\mathbb{Q}_p$.

**Remark.** Completeness is preserved by isometry, and by uniform equivalence of metrics, but not by homeomorphism. A complete metric space may therefore be homeomorphic to an incomplete one, and a space may admit both complete and incomplete metrics; the question of which topological spaces admit a complete metric is answered by the metrisation theorems, and the answer is the completely metrisable spaces, which are the $G_\delta$ subsets of their completions.

## The Completion

### Construction

**Theorem (completion).** Let $(X, d)$ be a metric space. There exist a complete metric space $(\hat X, \hat d)$ and an isometric embedding $\iota : X \to \hat X$ with dense image. The pair $(\hat X, \iota)$ is unique up to a unique isometry: if $(\hat X', \iota')$ has the same properties, there is a unique isometry $\hat X \to \hat X'$ carrying $\iota$ to $\iota'$.

**Construction.** Let $\mathcal{C}$ be the set of Cauchy sequences in $X$, and define an equivalence relation on $\mathcal{C}$ by

$$
(x_n) \sim (y_n) \iff \lim_{n \to \infty} d(x_n, y_n) = 0.
$$

The limit exists because $\left(d(x_n, y_n)\right)$ is Cauchy in $\mathbb{R}$: the estimate $|d(x_n,y_n) - d(x_m,y_m)| \leq d(x_n,x_m) + d(y_n,y_m)$ shows it. Let $\hat X = \mathcal{C}/{\sim}$ and put

$$
\hat d([(x_n)], [(y_n)]) = \lim_{n \to \infty} d(x_n, y_n).
$$

**Well-definedness and completeness.** The limit is independent of the representatives, because replacing one Cauchy sequence by an equivalent one changes $d(x_n, y_n)$ by a quantity tending to $0$. The function $\hat d$ is a metric: symmetry and the triangle inequality pass to the limit from $d$, and $\hat d = 0$ exactly for equivalent sequences, which is the definition of the class. Completeness holds because a Cauchy sequence in $\hat X$ can be replaced by a Cauchy sequence in the dense copy $\iota(X)$ and then by a diagonal sequence in $X$ whose class is its limit.

**The embedding.** The map $\iota(x) = [(x, x, x, \ldots)]$ is an isometry, since constant sequences satisfy $\hat d(\iota x, \iota y) = d(x, y)$, and its image is dense: a class $[(x_n)]$ is the limit of the classes $\iota(x_k)$ as $k \to \infty$, because $d(x_n, x_k)$ is small for $n, k$ large.

**Uniqueness.** Let $(\hat X', \iota')$ have the same properties. Define $\Phi : \hat X \to \hat X'$ by $\Phi(\lim \iota(x_n)) = \lim \iota'(x_n)$ for a Cauchy sequence $(x_n)$; the definition is forced, and the limits exist by completeness of $\hat X'$. The map is well defined and isometric because $\iota, \iota'$ are isometric and limits are unique, and it is surjective by density of $\iota'(X)$. Uniqueness of $\Phi$ is clear from the defining formula, since $X$ is dense. $\square$

### The Universal Property

**Theorem.** Let $Y$ be a complete metric space and $f : X \to Y$ uniformly continuous. Then $f$ extends uniquely to a uniformly continuous map $\hat f : \hat X \to Y$, and $\hat f \circ \iota = f$.

**Proof.** For $p \in \hat X$ choose $x_n \in X$ with $\iota(x_n) \to p$; then $(x_n)$ is Cauchy, so $(f(x_n))$ is Cauchy by uniform continuity and converges in $Y$; set $\hat f(p) = \lim f(x_n)$. The value is independent of the chosen sequence, and uniform continuity of $\hat f$ follows by applying the given $\delta$ of $f$ to the dense subset and passing to limits. Uniqueness is from density and continuity. $\square$

Thus the completion is characterised by a universal property: it is the initial complete space receiving a uniformly continuous map from $X$. This is the sense in which the completion is a universal construction, and it is this characterisation, not the particular construction by Cauchy sequences, that is used in practice. Repeating the construction starting from $\mathbb{Q}$ with the usual metric yields $\mathbb{R}$; starting from $\mathbb{Q}$ with the $p$-adic metric yields $\mathbb{Q}_p$; starting from a field with an absolute value yields its completion, a construction taken up with valuations in the companion category.

## Uniform Spaces

### Entourages and the Uniform Structure

Completeness is not topological, so it must be defined from data finer than a topology but coarser than a metric. That data is the uniformity.

**Definition.** A **uniform structure** on a set $X$ is a filter $\mathcal{U}$ on $X \times X$ whose members, called **entourages**, satisfy

**(U1)** the diagonal $\Delta_X = \{(x, x)\} \subseteq E$ for every $E \in \mathcal{U}$;

**(U2)** if $E \in \mathcal{U}$ then $E^{-1} = \{(y, x) : (x, y) \in E\} \in \mathcal{U}$;

**(U3)** for every $E \in \mathcal{U}$ there is $D \in \mathcal{U}$ with $D \circ D \subseteq E$, where $D \circ D = \{(x, z) : \exists y, (x, y), (y, z) \in D\}$.

The pair $(X, \mathcal{U})$ is a **uniform space**; a family $\mathcal{B} \subseteq \mathcal{U}$ is a **base** if every entourage contains a member of $\mathcal{B}$, and the structure is generated by any base satisfying the three conditions with $E$ ranging over the base (with (U3) interpreted for a base as: for each $B$ there is $D$ with $D \circ D \subseteq B$).

**Definition (uniform topology).** A set $U \subseteq X$ is open in the **uniform topology** if for every $x \in U$ there is $E \in \mathcal{U}$ with $E[x] = \{y : (x, y) \in E\} \subseteq U$. The sets $E[x]$ form a neighbourhood base at $x$, and the uniform topology is a topology.

**Example (metric uniformity).** A metric $d$ generates the uniformity with base

$$
E_\epsilon = \{(x, y) : d(x, y) < \epsilon\}, \qquad \epsilon > 0.
$$

The axioms (U1)–(U3) hold, and the uniform topology is the metric topology. Two metrics induce the same uniformity exactly when they are uniformly equivalent, so the uniformity remembers exactly what the metric remembers beyond the topology.

**Definition (uniform continuity).** A map $f : X \to Y$ between uniform spaces is **uniformly continuous** if for every entourage $F$ of $Y$ there is an entourage $E$ of $X$ with $(x, y) \in E \Rightarrow (f(x), f(y)) \in F$. The composite of uniformly continuous maps is uniformly continuous, so uniform spaces form a category.

**Definition.** A filter $\mathcal{F}$ on a uniform space is **Cauchy** if for every entourage $E$ there is $A \in \mathcal{F}$ with $A \times A \subseteq E$. A uniform space is **complete** if every Cauchy filter converges; equivalently every Cauchy net converges. Uniformly continuous maps carry Cauchy filters to Cauchy filters, hence extend to completions, and every uniform space has a completion with the same universal property as in the metric case.

**Example (subspaces and products).** The subspace uniformity on $A \subseteq X$ has entourages $E \cap (A \times A)$; the product uniformity on $\prod_i X_i$ has a base of the sets $\{(x, y) : (x_i, y_i) \in E_i \text{ for all } i\}$ over finite sets of coordinates. Both induce the corresponding topological constructions, and both make the canonical maps uniformly continuous.

**Remark.** Every topological group carries two natural uniform structures, the left and the right uniformity generated by the neighbourhoods of the identity; the group topology is recovered from either, and the group is complete exactly when either uniform structure is complete. The two agree exactly when every neighbourhood of the identity contains a conjugation-invariant neighbourhood, a condition stronger than unimodularity: a locally compact group with such a neighbourhood base is unimodular, while the Heisenberg group is unimodular and its two uniformities nevertheless differ. The details are. A uniformity is thus not an optional refinement: it is the structure a topological group actually has.

## Uniform Convergence

### The Sup Metric

**Definition.** Let $X$ be a set, $(Y, d)$ a metric space, and let $B(X, Y)$ be the set of bounded functions $f : X \to Y$. The **sup metric** on $B(X, Y)$ is

$$
d_\infty(f, g) = \sup_{x \in X} d(f(x), g(x)).
$$

**Proposition.** $d_\infty$ is a metric on $B(X, Y)$, and it is complete when $(Y, d)$ is complete.

**Proof.** The metric axioms are inherited from $d$ pointwise, with the supremum finite by boundedness. For completeness, let $(f_n)$ be Cauchy in the sup metric; then $(f_n(x))$ is Cauchy in $Y$ for each $x$, with limit $f(x)$. Given $\epsilon > 0$, choose $N$ with $d_\infty(f_m, f_n) < \epsilon/2$ for $m, n \geq N$; passing to the limit in $m$ gives $d(f_n(x), f(x)) \leq \epsilon/2$ for all $x$, so $f$ is bounded and $d_\infty(f_n, f) \leq \epsilon/2$; hence $f_n \to f$. $\square$

**Definition.** A sequence $(f_n)$ of functions $X \to Y$ **converges uniformly** to $f$ if for every $\epsilon > 0$ there is $N$ with $d(f_n(x), f(x)) < \epsilon$ for all $n \geq N$ and all $x \in X$; equivalently, if $d_\infty(f_n, f) \to 0$ when the functions are bounded. It **converges pointwise** if $f_n(x) \to f(x)$ for each $x$.

**Theorem.** Uniform convergence implies pointwise convergence, and the converse fails: $f_n(x) = x^n$ on $[0,1]$ converges pointwise to the discontinuous function that is $0$ below $1$ and $1$ at $1$, but not uniformly.

**Theorem (continuity of the uniform limit).** If $f_n : X \to Y$ are continuous and $f_n \to f$ uniformly, then $f$ is continuous.

**Proof.** Given $x$ and $\epsilon > 0$, choose $n$ with $d(f_n(z), f(z)) < \epsilon/3$ for all $z$, then $\delta$ with $d(f_n(x), f_n(x')) < \epsilon/3$ when $d(x, x') < \delta$. The triangle inequality gives $d(f(x), f(x')) < \epsilon$. $\square$

**Corollary.** The continuous bounded functions on a metric space form a closed subset $C_b(X, Y) \subseteq B(X, Y)$; when $Y$ is complete, $C_b(X, Y)$ is complete.

**Proof.** The limit of a uniformly convergent sequence of continuous functions is continuous, which is closedness in the sup metric; a closed subset of a complete space is complete. $\square$

### Uniform Convergence in Analysis

**Theorem (Cauchy criterion).** A sequence $(f_n)$ converges uniformly to a bounded limit if and only if for every $\epsilon > 0$ there is $N$ with $d_\infty(f_m, f_n) < \epsilon$ for $m, n \geq N$.

**Proof.** This is the completeness of the sup metric for bounded functions, together with the observation that a uniformly Cauchy sequence is bounded. $\square$

**Theorem (interchange of limit and integral).** Let $f_n : [a, b] \to \mathbb{R}$ be Riemann integrable with $f_n \to f$ uniformly. Then $f$ is Riemann integrable and

$$
\int_a^b f = \lim_{n \to \infty} \int_a^b f_n.
$$

**Proof.** Uniform convergence controls the difference of the integrals: $\left|\int f_n - \int f\right| \leq (b - a) \sup |f_n - f| \to 0$. Integrability of $f$ follows from the standard criterion, since $f$ can be approximated uniformly by integrable functions. $\square$

**Theorem (Dini).** Let $X$ be compact, $f_n : X \to \mathbb{R}$ continuous with $f_n \to f$ pointwise and $f_n \geq f_{n+1}$ for all $n$, with $f$ continuous. Then $f_n \to f$ uniformly.

**Proof.** The functions $g_n = f_n - f$ decrease to $0$; given $\epsilon > 0$ the open sets $U_n = \{x : g_n(x) < \epsilon\}$ increase and cover $X$, so by compactness $U_N = X$ for some $N$, giving uniform convergence. $\square$

Uniform convergence is the metric form of a statement about uniform spaces: the pointwise convergence uniformity on a set of functions is not complete, while the uniformity of uniform convergence is, and it is the latter that has a complete function space. The distinction is taken up again in measure theory, where almost everywhere convergence replaces pointwise convergence and the dominated convergence theorem replaces uniform convergence.

## Baire Category

### Nowhere Dense Sets and Meagre Sets

**Definition.** A subset $A$ of a topological space $X$ is **nowhere dense** if $\operatorname{int}\overline{A} = \emptyset$; **meagre**, or of the **first category**, if it is a countable union of nowhere dense sets; and of the **second category** otherwise. A space is a **Baire space** if every countable intersection of dense open sets is dense; equivalently, if no nonempty open set is meagre.

**Proposition.** A countable union of meagre sets is meagre; a subset of a meagre set is meagre; nowhere dense sets are meagre and have empty interior. The relation between meagreness and "small" in the measure-theoretic sense is one of analogy, not implication: $\mathbb{R}$ decomposes as the union of a meagre set and a set of measure zero, and in that decomposition the meagre piece may have full measure while the null piece may be comeagre.

**Proof.** Countable unions of countable unions are countable unions, and a subset of a nowhere dense set is nowhere dense. For the decomposition, enumerate the rationals as $q_1, q_2, \ldots$ and let $I_{n,k}$ be an open interval about $q_n$ of length $2^{-n-k}$; then $G_k = \bigcup_n I_{n,k}$ is open and dense with Lebesgue measure at most $\sum_{n \geq 1} 2^{-n-k} = 2^{-k}$, so $N = \bigcap_k G_k$ is a countable intersection of dense open sets, hence comeagre, and has measure zero. Its complement is therefore meagre and of full measure. $\square$

### The Baire Category Theorem

**Theorem (Baire).** Every complete metric space is a Baire space. Every locally compact Hausdorff space is a Baire space.

**Proof (complete metric case).** Let $U_1, U_2, \ldots$ be dense open sets; we show $\bigcap_n U_n$ is dense. Let $V$ be a nonempty open set and pick $x_1 \in V \cap U_1$ with a radius $r_1 < 1$ and $\overline{B}(x_1, r_1) \subseteq V \cap U_1$, possible by density and openness. Inductively, having chosen $x_n$ and $r_n < 1/n$, choose $x_{n+1} \in B(x_n, r_n) \cap U_{n+1}$ and $r_{n+1} < 1/(n+1)$ with $\overline{B}(x_{n+1}, r_{n+1}) \subseteq B(x_n, r_n) \cap U_{n+1}$. The centres form a Cauchy sequence, since $x_m \in B(x_n, r_n)$ for $m > n$ and $r_n \to 0$; by completeness they converge to some $x$, which lies in $\overline{B}(x_n, r_n)$ for every $n$, hence in $U_n$ for every $n$ and in $V$ for the initial choice. Thus $\bigcap_n U_n$ meets every nonempty open set and is dense. The locally compact case is the same argument with compact neighbourhoods in place of closed balls. $\square$

**Corollary.** $\mathbb{R}$ is not a countable union of nowhere dense sets, and $\mathbb{Q}$ is meagre in $\mathbb{R}$; consequently $\mathbb{Q}$ is not a Baire space and the irrationals form a dense set of the second category.

**Proof.** $\mathbb{R}$ is complete, hence Baire, so it cannot be meagre; $\mathbb{Q}$ is a countable union of singletons, each nowhere dense. A Baire space is not meagre in itself, and every subset of a meagre set is meagre, so $\mathbb{Q}$ is not Baire. Since $\mathbb{R} = \mathbb{Q} \cup (\mathbb{R} \setminus \mathbb{Q})$ is not meagre and $\mathbb{Q}$ is, the irrationals are not meagre. $\square$

### Consequences

**Theorem.** The set of continuous functions $f : [0, 1] \to \mathbb{R}$ that are differentiable at at least one point is meagre in $C[0, 1]$ with the sup metric; in particular there exist continuous nowhere differentiable functions.

**Proof sketch.** For $n \in \mathbb{N}$ let $A_n$ be the set of $f$ for which some point $x$ satisfies $|f(x + h) - f(x)| \leq n|h|$ for all small $h$. Each $A_n$ is closed and has empty interior in the sup metric, using a piecewise linear sawtooth perturbation of small sup norm and large slope. The set of functions differentiable somewhere is contained in $\bigcup_n A_n$, a countable union of nowhere dense sets, hence meagre; the space $C[0,1]$ is complete and therefore not meagre, so the complement is nonempty and in fact of the second category. $\square$

**Remark (the Baire category method).** The theorem is used as a tool in three shapes. It proves **existence** without construction, as in the theorem above. It proves **open mapping principles**: the open mapping theorem, the closed graph theorem and the uniform boundedness principle for Banach spaces are all consequences of the Baire category theorem for the complete space on which the operators act, and they are treated with normed spaces in the companion category. It proves **genericity** statements, since a countable intersection of dense open sets is a residual set and "most" points may be taken to mean "complementary to a meagre set". The method is used in measure theory in the companion article, where it supplies the decomposition of the line into a meagre set and a null set, and in the theory of locally compact groups; the open mapping and closed graph theorems for Banach spaces rest on it as well.

## Summary

A metric space is a set with a distance; the balls form a base for a Hausdorff, first countable, normal topology, and the metric determines more than that topology. Topological, uniform and strong equivalence of metrics are distinct, and only the last two preserve Cauchy sequences. Continuity, uniform continuity, the Lipschitz condition, contraction and isometry form a hierarchy; the Banach fixed point theorem gives the unique fixed point of a contraction on a complete space, with the geometric error estimate, and is the standard existence proof for solutions of equations.

A sequence is Cauchy when its terms become arbitrarily close; a space is complete when every Cauchy sequence converges, and closed subspaces of complete spaces are complete while completeness is not a topological property. Every metric space has a completion, constructed from equivalence classes of Cauchy sequences, unique up to a unique isometry, and characterised by the universal property that uniformly continuous maps into complete spaces extend uniquely. Completing $\mathbb{Q}$ gives $\mathbb{R}$ with the usual metric and $\mathbb{Q}_p$ with the $p$-adic metric.

A uniform space is a set with a filter of entourages satisfying the diagonal, symmetry and composition axioms; it carries a topology, a notion of uniform continuity and a notion of Cauchy filter, and it is the structure that completeness really belongs to. Every metric space and every topological group carries a uniform structure, and the completion of a topological group is a construction in uniform spaces.

Uniform convergence is convergence in the sup metric; it preserves continuity and integrability, is characterised by the Cauchy criterion, and is forced by pointwise convergence in the presence of compactness and monotonicity by Dini's theorem. Finally, Baire's theorem states that complete metric spaces and locally compact Hausdorff spaces are Baire; hence the reals are not a countable union of nowhere dense sets, the rationals are both meagre and not Baire, the irrationals are dense and of the second category, and continuous nowhere differentiable functions exist because the differentiable ones form a meagre set.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $d(x, y)$ | Metric or distance on a set $X$ |
| $B(x, r)$, $\overline{B}(x, r)$ | Open and closed balls |
| $d_\infty$ | Sup metric on bounded functions |
| $L$ | Lipschitz constant |
| $C([0,1])$, $\|f\|_\infty$ | Continuous functions on $[0,1]$ with the sup norm |
| $T$ | Contraction or integral operator, e.g. $(Tf)(x) = 1 + \tfrac{1}{2}\int_0^x f$ |
| contraction | Lipschitz map with constant $L < 1$ |
| $x_n \to x$, Cauchy | Convergence and Cauchy condition |
| $(X, d)$ complete | Every Cauchy sequence converges |
| $\hat X$, $\hat d$, $\iota$ | Completion and its isometric embedding |
| $\mathcal{U}$, $E$ | Uniform structure and an entourage |
| $\Delta_X$ | Diagonal in $X \times X$ |
| $E[x]$, $E \circ E$ | Set of points $E$-close to $x$; compositions of entourages |
| $B(X, Y)$, $C_b(X, Y)$ | Bounded functions, continuous bounded functions |
| $f_n \to f$ uniformly | Convergence in the sup metric |
| nowhere dense, meagre | $\operatorname{int}\overline{A} = \emptyset$; countable union of nowhere dense sets |
| Baire space | Countable intersection of dense open sets is dense |



## Further Reading

- Walter Rudin, *Principles of Mathematical Analysis* (McGraw-Hill, 3rd ed. 1976), for metric spaces and uniform convergence at the level used here.
- Nicolas Bourbaki, *General Topology*, Chapters 1–4 (Springer, 1995), for the systematic theory of uniform spaces and completions.
- James R. Munkres, *Topology* (Prentice Hall, 2nd ed. 2000), for the Baire category theorem and its consequences.
- John L. Kelley, *General Topology* (Van Nostrand, 1955; reprinted Springer, 1975), for uniform spaces and the completion of a uniform space.
- Stephen Willard, *General Topology* (Addison-Wesley, 1970; reprinted Dover, 2004), for metric completeness and the metrisation theorems.
- Ryszard Engelking, *General Topology* (Heldermann, revised ed. 1989), for a comprehensive reference on uniform spaces and completeness.
- John C. Oxtoby, *Measure and Category* (Springer, Graduate Texts in Mathematics 2, 2nd ed. 1980), for the analogy between meagre and null sets and the Baire category method.
