# __The Hutchinson Operator and Its Adjoint__

## Introduction

An **iterated function system** on a complete metric space $(X,d)$ is a finite family of contractions $f_1,\dots,f_N : X \to X$, with the ratios $r_i < 1$; the lead article *Fractal Geometry* defines the system, constructs the **attractor** as the unique nonempty compact set $K$ with

$$
K = \bigcup_{i=1}^N f_i(K) ,
$$

and computes the dimension of the self-similar examples by the similarity dimension. This article reads the same data as an **operator**. The **Hutchinson operator** is the map

$$
F : \mathcal{K}(X) \to \mathcal{K}(X), \qquad F(A) = \bigcup_{i=1}^N f_i(A) ,
$$

on the space of the nonempty compact subsets with the Hausdorff metric; the defining equation of the attractor is the fixed-point equation $F(K) = K$, and the operator is a contraction of ratio $r = \max_i r_i$ on a complete metric space, so the existence and the uniqueness of the attractor are the theorem of Banach. The operator is not linear, but it is additive over the unions and monotone, its Lipschitz constant is $r$, and the iteration of $F$ from any compact set converges to $K$ at the geometric rate. The same reading applies to the measures: the **adjoint** of the transfer operator is the pushforward

$$
L\mu = \sum_{i=1}^N p_i\,(f_i)_\# \mu ,
$$

which acts on the probability measures with positive weights $p_i$ summing to one, is again a contraction of ratio $r$, this time in the Wasserstein metric, and has as its unique fixed point the **self-similar measure** of the weights. The pair — the fixed point of $F$ among the compact sets and the fixed point of $L$ among the measures — is the duality the article states: the geometry of the attractor and the measure that lives on it are the two faces of one operator system.

The content of the article is the operator form and not the re-derivation of the attractor. The contraction and the fixed point of the set operator are the lead article's, and the self-similar measure and the spectrum of the transfer operator are those of *Fractal Analysis*; the article states the adjoint relation, the duality between the two fixed points, the collage theorem and the convergence rates, and works the middle-thirds Cantor set as the computed example.

The article assumes *Metric, Uniform and Complete Spaces* for the complete metric space, the compactness and the theorem of Banach; *Metric Geometry* for the Hausdorff distance, the diameter, the convergence of the compact sets and the Blaschke selection theorem; *Fractal Geometry* for the iterated function systems, the attractor, the similarity dimension and the examples; *Measure Theory and Integration* for the probability measures, the pushforward, the weak convergence and the Prokhorov theorem; and *Fractal Analysis*'s *The Self-Similar Measure and the Invariant Measure* and *The Transfer Operator of the Limit Dynamical System* for the measure and the spectrum. No physics is invoked.

## The Space of Compact Sets and the Hausdorff Metric

**Definition.** For a metric space $(X,d)$ let $\mathcal{K}(X)$ be the set of the nonempty compact subsets of $X$; the **Hausdorff distance** is

$$
d_H(A,B) = \max\Bigl\{\sup_{a \in A} d(a,B),\ \sup_{b \in B} d(b,A)\Bigr\} , \qquad d(x,B) = \inf_{b \in B} d(x,b) .
$$

**Theorem (the completeness).** If $(X,d)$ is complete then $(\mathcal{K}(X), d_H)$ is complete; if $X$ is compact then $\mathcal{K}(X)$ is compact, by the **Blaschke selection theorem**. A sequence $A_n$ converges to $A$ in the Hausdorff metric if and only if every point of $A$ is the limit of a sequence of points of the $A_n$ and every limit of such a sequence lies in $A$.

**Proof sketch.** The distance function $d(\cdot,B)$ is $1$-Lipschitz, and the supprema in the definition are finite for compact sets; the completeness is proved by taking, for a Cauchy sequence $A_n$, the set of the limits of the Cauchy sequences of points $a_n \in A_n$, which is nonempty and compact, and by checking the two inclusions; the compactness in the compact case is the Blaschke theorem, a diagonal argument on the $\epsilon$-nets. The statements are those of *Metric Geometry*.

**Remark (the two levels of the space).** The space $\mathcal{K}(X)$ is the carrier of the **set operator** $F$, and the space $\mathcal{P}(X)$ of the Borel probability measures on $X$ is the carrier of the **measure operator** $L$; the two spaces are linked by the support map $\operatorname{supp} : \mathcal{P}(X) \to \mathcal{K}(X)$, which is upper semicontinuous in the weak topology. The duality of the article is the interaction of the two levels.

## The Hutchinson Operator

**Definition.** For an iterated function system $f_1,\dots,f_N$ on $X$ the **Hutchinson operator** is

$$
F(A) = \bigcup_{i=1}^N f_i(A) , \qquad A \in \mathcal{K}(X) .
$$

**Theorem (the contraction and the fixed point).** Let $(X,d)$ be complete and let each $f_i$ be a contraction of ratio $r_i$, with $r = \max_i r_i \in [0,1)$. Then $F$ maps $\mathcal{K}(X)$ into itself, it is a contraction of ratio $r$,

$$
d_H\bigl(F(A), F(B)\bigr) \leq r\, d_H(A,B) \qquad (A, B \in \mathcal{K}(X)) ,
$$

and it has a unique fixed point $K \in \mathcal{K}(X)$, the **attractor** of the system. For every $A \in \mathcal{K}(X)$ the iterates $F^n(A)$ converge to $K$ with $d_H(F^n(A), K) \leq r^n (1-r)^{-1} d_H(A, F(A))$.

**Proof sketch.** The image of a compact set under a continuous map is compact, and the finite union of compact sets is compact, so $F$ maps $\mathcal{K}(X)$ into itself. The Hausdorff inequality follows from the pointwise inequality $d(f_i(a), f_i(b)) \leq r_i d(a,b)$ and the two supprema in the definition; the fixed point is the Banach theorem on the complete space $(\mathcal{K}(X),d_H)$, and the rate is the standard geometric bound. The construction of the attractor as the limit of the iterates of any compact set is that of the lead article *Fractal Geometry*; the operator form is what is read here.

**Theorem (the collage theorem).** For every $A \in \mathcal{K}(X)$,

$$
d_H(A, K) \leq \frac{1}{1-r}\, d_H\bigl(A, F(A)\bigr) .
$$

**Proof sketch.** The triangle inequality in the Hausdorff metric and the contraction give $d_H(A,K) \leq d_H(A, F(A)) + r\, d_H(A, K)$, and the rearrangement gives the bound. The inequality is the quantitative form of the statement that a compact set which is nearly invariant under $F$ is near the attractor, and it is the operator statement used in the inverse problem of the fractal image compression.

**Remark (what kind of operator $F$ is).** The operator $F$ is **union-additive**, $F(A \cup B) = F(A) \cup F(B)$, and monotone, $A \subseteq B \Rightarrow F(A) \subseteq F(B)$; it is not additive over the union of the functions, and it is not linear. It is a nonlinear contraction, and the Banach theorem applies to it in its metric form; the fixed-point equation is the self-similarity $K = \bigcup_i f_i(K)$, which is the definition of the attractor.

## The Adjoint Action on the Measures

**Definition (the transfer operator and its adjoint).** Let $p_1,\dots,p_N > 0$ with $\sum_i p_i = 1$. The **transfer operator** acts on the bounded continuous functions by

$$
(T\varphi)(x) = \sum_{i=1}^N p_i\, \varphi\bigl(f_i(x)\bigr) ,
$$

and its **adjoint** acts on the finite Borel measures by

$$
L\mu = \sum_{i=1}^N p_i\,(f_i)_\# \mu , \qquad \int_X \varphi\, d(L\mu) = \int_X (T\varphi)\, d\mu .
$$

The last identity is the defining adjoint relation; it holds for every bounded continuous $\varphi$ and every finite measure $\mu$, and it says that $L$ is the transpose of $T$ under the duality pairing $\langle \varphi, \mu\rangle = \int \varphi\, d\mu$.

**Theorem (the properties of the pair).** **(a)** $T$ is a positive linear contraction of the space of the bounded continuous functions with the sup norm, of norm one, and it preserves the constants. **(b)** $L$ maps the probability measures into themselves, is continuous for the weak topology, and is a contraction of ratio $r$ for the **Wasserstein** metric $W_1$. **(c)** $L$ has a unique fixed point $\mu$ in the probability measures,

$$
\mu = \sum_{i=1}^N p_i\,(f_i)_\# \mu ,
$$

the **self-similar measure** of the weights; it is the invariant measure of the random walk that applies the map $f_i$ with probability $p_i$, and its support is the attractor, $\operatorname{supp}\mu = K$.

**Proof sketch.** (a) the positivity is clear, the norm is at most one by $\sum p_i = 1$, and the constants are preserved. (b) the Wasserstein distance satisfies $W_1((f_i)_\#\mu, (f_i)_\#\nu) \leq r_i W_1(\mu,\nu)$ because the transportation cost is contracted by the map, so the average over $i$ gives the ratio $r$; the completeness of the Wasserstein space of the probability measures on a complete separable space is the theorem of *Measure Theory and Integration*. (c) the Banach theorem gives the unique fixed point; the support identity is the invariance of $\operatorname{supp}\mu$ under the averaged pushforward and the surjectivity of the union. The measure and its properties are those of *Fractal Analysis*'s *The Self-Similar Measure and the Invariant Measure*; the operator relation is what is stated here.

**Remark (the two fixed points are one system).** The set operator $F$ and the measure operator $L$ share the same data — the maps and the ratios — and their fixed points are linked by
$\operatorname{supp}\mu = K$. The support map intertwines the two: $F(\operatorname{supp}\mu) = \operatorname{supp}(L\mu)$, so a fixed point of $L$ has the attractor as its support. This is the precise sense of the duality: the attractor is the geometric fixed point and the self-similar measure is the measure-theoretic fixed point of the same operator system, and the two are not independent but the two projections of one object.

**Example (the middle-thirds Cantor set).** For $X = [0,1]$, $f_1(x) = x/3$, $f_2(x) = x/3 + 2/3$ and $p_1 = p_2 = 1/2$, the attractor is the middle-thirds Cantor set $C$ and the self-similar measure is the Cantor measure. The operator computations at the first levels are the following. The Hutchinson operator sends $[0,1]$ to $C_1 = [0,\frac13]\cup[\frac23,1]$ and $C_1$ to the four intervals of $C_2$; the Hausdorff distance from the level-$n$ approximation to the attractor is

$$
d_H(C_n, C) = \frac{1}{2}\cdot 3^{-(n+1)} ,
$$

which is $\frac16$ for $n=0$, $\frac1{18}$ for $n=1$ and $\frac1{54}$ for $n=2$, decreasing by the factor $\frac13$ at each step, the ratio $r$ of the contraction (checked numerically at the levels $n=0,1,2$ against the approximations $C_6$ and $C_8$). The measure of each of the $2^n$ cylinders of the level $n$ is $2^{-n}$, so the Cantor measure of a cylinder of side $3^{-n}$ is comparable to $(3^{-n})^{\log2/\log3}$, the Ahlfors-regular form with exponent the dimension of the set.

## The Duality and Its Consequences

**Theorem (the address map).** Let $\Sigma = \{1,\dots,N\}^{\mathbb{N}}$ be the full shift of *Symbolic Dynamics*, with the Bernoulli measure $\mathbf{p}$ of the weights, and let $\Pi(\omega) = \lim_{n\to\infty} f_{\omega_1}\circ\cdots\circ f_{\omega_n}(x_0)$ be the address map, well defined on the whole of $\Sigma$ and continuous. Then $\Pi$ is onto $K$, it is injective at the points with a unique address, the ambiguity being confined to the overlaps $f_i(K)\cap f_j(K)$, and

$$
\mu = \Pi_\# \mathbf{p} .
$$

**Proof sketch.** The compositions $f_{\omega_1}\circ\cdots\circ f_{\omega_n}$ are contractions of ratio $r^n$, so the sets $f_{\omega_1}\circ\cdots\circ f_{\omega_n}(X)$ are nested and have diameter at most $r^n\operatorname{diam}X$; their intersection is a single point, which does not depend on $x_0$, so the limit exists and the convergence is uniform in $\omega$. The surjectivity is the definition of the attractor as the closure of the set of the fixed points of the finite compositions, and the continuity is the uniform contraction; the identity of the measures is the invariance of $\mathbf p$ under the shift and the fixed-point property of $\mu$. These are the coding statements of the lead article and of *Symbolic Dynamics*; they are recorded here because they identify the measure fixed point with the pushforward of the Bernoulli measure, which is the operator content of the duality.

**Remark (the dimension of the measure and the pressure).** The **dimension of the self-similar measure** $\mu$ is

$$
\dim_H \mu = \frac{\sum_i p_i \log p_i}{\sum_i p_i \log r_i} ,
$$

the ratio of the entropy of the weights to the Lyapunov exponent of the system, and it equals the similarity dimension $\dim_H K$ for the **natural** weights $p_i = r_i^{s}$ with $s$ the similarity dimension of the lead article. The identity is the theorem of the dimension of a self-similar measure; the variational interpretation — the maximal entropy, the pressure and the Gibbs property — is that of *Ergodic Theory* and *Fractal Analysis*'s *The Self-Similar Measure and the Invariant Measure*, and the spectrum of the transfer operator is that of *The Transfer Operator of the Limit Dynamical System*. The operator pair $(T,L)$ is thus the analytic face of the same system whose geometric face is $(F,K)$.

**Remark (the involution to come).** When the system carries an involution permuting the maps, the Hutchinson operator commutes with the induced involution on the compact sets and the fixed point becomes symmetric; the geometry of the symmetric fractals is *Symmetric Fractals and the Involution* and the operator form on the compact sets is *The Involution on the Space of Compact Sets and the Symmetric Attractor*. The transfer operator and its adjoint are the tools by which the symmetric fixed point is exhibited there.

## Summary

The Hutchinson operator of an iterated function system is the map $F(A) = \bigcup_i f_i(A)$ on the nonempty compact subsets with the Hausdorff metric; it is a contraction of ratio $r = \max r_i$ on a complete space, and its unique fixed point is the attractor, the fixed-point equation $K = \bigcup_i f_i(K)$ being the self-similarity. The operator is nonlinear but union-additive and monotone, and the collage theorem measures the distance to the attractor by the invariance defect. The adjoint of the transfer operator $T\varphi = \sum p_i \varphi\circ f_i$ is the pushforward $L\mu = \sum p_i (f_i)_\#\mu$, a contraction of ratio $r$ in the Wasserstein metric whose unique fixed point is the self-similar measure, supported on the attractor; the attractor and the measure are the two faces of the same operator system, linked by the support map and by the address map $\mu = \Pi_\#\mathbf p$. The dimension of the self-similar measure is the ratio of the entropy to the Lyapunov exponent, equal to the similarity dimension for the natural weights. The iteration systems, the attractor and the similarity dimension are those of *Fractal Geometry*, the self-similar measure and the spectrum are those of *Fractal Analysis*, the Hausdorff and Wasserstein metrics are those of *Metric Geometry* and *Measure Theory and Integration*, and the symmetric case is treated in the two articles on the involution. No physics is invoked.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{K}(X)$, $d_H$ | Nonempty compact subsets; Hausdorff metric |
| $f_1,\dots,f_N$, $r_i$, $r$ | Contractions, their ratios, and $r=\max r_i$ |
| $F$ | Hutchinson operator, $F(A)=\bigcup_i f_i(A)$ |
| $K$ | Attractor, the unique fixed point of $F$ |
| $p_i$, $\mu$ | Weights with $\sum p_i=1$; self-similar measure, the fixed point of $L$ |
| $T$, $L=T^*$ | Transfer operator on the functions; its adjoint on the measures |
| $W_1$ | Wasserstein metric, in which $L$ is a contraction of ratio $r$ |
| $\Pi$, $\Sigma$, $\mathbf p$ | Address map; shift space; Bernoulli measure, with $\mu=\Pi_\#\mathbf p$ |
| $C_n$ | Level-$n$ approximation of the middle-thirds Cantor set |
| $\operatorname{supp}\mu = K$ | The support of the self-similar measure is the attractor |

## Further Reading

- John E. Hutchinson, "Fractals and self-similarity", *Indiana University Mathematics Journal* 30 (1981), 713–747, for the operator, the attractor and the measure.
- Michael F. Barnsley, *Fractals Everywhere* (Academic Press, 2nd edition, 1993), for the Hausdorff metric, the collage theorem and the inverse problem.
- Kenneth Falconer, *Techniques in Fractal Geometry* (Wiley, 1997), and *Fractal Geometry: Mathematical Foundations and Applications* (Wiley, 3rd edition, 2014), for the dimension of the self-similar measure and the pressure.
- David Ruelle, *Thermodynamic Formalism* (Addison-Wesley, 1978), for the transfer operator, the pressure and the Gibbs measures.
- Peter Walters, *An Introduction to Ergodic Theory* (Springer, 1982), for the invariant measure, the entropy and the variational principle.
- Cédric Villani, *Optimal Transport: Old and New* (Springer, 2009), for the Wasserstein metric and the contraction of the pushforward.
