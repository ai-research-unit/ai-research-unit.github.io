# __Multifractal Analysis and the Legendre Transform__

## Introduction

The dimension of a measure is one number, and one number cannot describe a measure that is smooth on part of its support and concentrated on another. **Multifractal analysis** refines it: to every point $x$ one attaches the **local dimension** $\alpha(x)$ of the measure at $x$, to every value $\alpha$ one attaches the **level set** $K_\alpha=\{x:\alpha(x)=\alpha\}$, and to the measure one attaches the **multifractal spectrum** $f(\alpha)$ that records the dimension of each level set. The spectrum is not computed point by point; it is the **Legendre transform** of a single convex function $\tau$ obtained from the **moment sums** of the measure, and the identity between the two is the **multifractal formalism**. This is the second article of the category because the self-similar measure of *The Self-Similar Measure and the Invariant Measure* is the measure whose spectrum is exactly computable, and because the Legendre transform of the entropy is the same transform that produces the large-deviation rate function.

The article develops the multifractal formalism. It defines the local dimension and the level sets, defines the spectrum as the function that assigns to each exponent the dimension of its level set, defines the moment sums and proves that their growth exponent $\tau(q)$ is determined by the single equation $\sum_i p_i^q r_i^{-\tau(q)}=1$, and proves that $\tau$ is convex with $\tau(0)=-\dim_H\Lambda$ and $\tau(1)=0$. It defines the Legendre transform $f(\alpha)=\inf_q(q\alpha-\tau(q))$, states the **multifractal formalism** — the identity $f(\alpha)=\dim_H K_\alpha$ on the range of the exponents — and separates the cases: the formalism holds for the self-similar measures satisfying the open set condition together with a separation of the pieces, and it can fail, with the transform strictly above the true spectrum, when the pieces overlap. It computes the two worked families: the Bernoulli measures of the Cantor set, where the spectrum is the graph of the entropy reparametrised, and the self-similar measures of the Sierpiński gasket, where the spectrum lies between the dimension of the measure and the dimension of the set. And it reads the transform as the large-deviation rate function of the empirical frequencies of the Bernoulli sequence.

The local dimension of a measure and the exact dimension are *The Self-Similar Measure and the Invariant Measure*; the attractor, the iterated function system, the open set condition and the dimension of the **set** are *Fractal Geometry*, in Part IV, cited for the dimension of the level sets and not rebuilt; the Shannon–McMillan–Breiman theorem, the empirical frequencies and the rate functions are *Ergodic Theory* and *Laws of Large Numbers and the Central Limit Theorem*; the large-deviation theory is *Probability and Ergodic Theory*; the convex analysis of the transform, the subgradient and the conjugate function are the convex analysis of Part III. No physics is invoked.

## The Local Dimension and the Level Sets

### The Local Dimension

**Definition.** Let $\mu$ be a finite Borel measure on a metric space. The **local dimension** of $\mu$ at a point $x$ is

$$
\alpha(x)=\lim_{\rho\to 0}\frac{\log\mu(B(x,\rho))}{\log\rho},
$$

when the limit exists, and the point is then called a point of dimension $\alpha$. The definition is that of the dimension of a measure in *The Self-Similar Measure and the Invariant Measure*, where it is shown that for a self-similar measure it exists and is constant almost everywhere and equals $H(p)/\chi$; the present article keeps the whole function $\alpha(\cdot)$ instead of its essential value.

### The Level Sets and the Spectrum

**Definition.** For a real number $\alpha$ the **level set** is

$$
K_\alpha=\{x : \alpha(x)=\alpha\},
$$

with the conventions $K_{\ge\alpha}=\{x:\alpha(x)\ge\alpha\}$ and likewise for the inequalities; the **multifractal spectrum** of $\mu$ is the function

$$
f(\alpha)=\dim_H K_\alpha,
$$

where $\dim_H$ is the Hausdorff dimension of *Fractal Geometry* and $f(\alpha)=-\infty$ when the level set is empty. The **support** of the spectrum is the closure of the set of exponents $\alpha$ with $K_\alpha\ne\emptyset$; the spectrum is a function on that support and $-\infty$ outside.

**Proposition (the spectrum is concave).** The spectrum of a measure is a concave function of $\alpha$ wherever it is finite, it is $-\infty$ outside the closed interval of the exponents that occur, and its maximum is the dimension of the dimension-regular part of the support; in particular $f(\alpha)\le\dim_H\Lambda$ for every $\alpha$.

*Proof.* The set $K_{\ge\alpha}$ is decreasing in $\alpha$, so the level sets are nested and the spectrum is upper semicontinuous and concave by the standard convexity of the dimension as a function of the level; the bound is the monotonicity of the dimension. The full statement, with the concavity and the covering argument, is in *Fractal Geometry* and in the lecture notes of the thermodynamic formalism.

## The Moment Sums and the Growth Exponent

### The Moment Sums

**Definition.** Let $\mu=\mu_p$ be the self-similar measure of the iterated function system $S_1,\dots,S_m$ with ratios $r_i$ and weights $p$, and let $q\in\mathbb{R}$. The **moment sum** at level $n$ is

$$
S_n(q)=\sum_{|w|=n}\mu(S_w\Lambda)^q=\sum_{|w|=n}(p_{w_1}\cdots p_{w_n})^q ,
$$

the sum of the $q$-th powers of the masses of the level-$n$ pieces.

### The Growth Exponent

**Definition.** The **growth exponent** $\tau(q)$ is the number, when it exists, with $S_n(q)\asymp (r^n)^{\tau(q)}$ for a common ratio $r$, and in general the unique solution of the **equation of Bowen**,

$$
\sum_{i=1}^m p_i^{\,q}\,r_i^{-\tau(q)}=1 .
$$

**Theorem (the exponent exists, is convex and is finitely often differentiable).** For every $q$ the equation $\sum_i p_i^q r_i^{-\tau}=1$ has exactly one real solution $\tau(q)$; the function $\tau$ so defined is convex and decreasing, it satisfies $\tau(0)=-\dim_H\Lambda$ and $\tau(1)=0$, and it is real-analytic with $\tau'(q)$ equal to the mean logarithm of the weights under the Gibbs probability $q_i\propto p_i^q r_i^{-\tau(q)}$.

*Proof.* The function $\tau\mapsto\sum_i p_i^q r_i^{-\tau}$ is strictly decreasing from $+\infty$ to $0$ (the ratios satisfy $r_i<1$), so the solution is unique. Differentiating the identity $\sum_i p_i^q r_i^{-\tau(q)}=1$ with respect to $q$ gives $\sum_i p_i^q(\log p_i)r_i^{-\tau} - \tau'\sum_i p_i^q(\log r_i)r_i^{-\tau}=0$, whence $\tau'$ is the stated mean; differentiating twice gives the concavity of the mean and the convexity of $\tau$. The values: at $q=0$ the equation is $\sum_i r_i^{-\tau(0)}=1$, so $-\tau(0)$ is the similarity dimension $s$ of *Fractal Geometry*; at $q=1$ the equation is $\sum_i r_i^{-\tau(1)}=1$ with $\sum_i p_i=1$, whose solution is $\tau(1)=0$.

**Corollary (the two elementary derivations from $\tau$).** The exponent is obtained from the entropy in the limit $\tau'(0)=H(p)/\chi$ where $\chi=\sum_i p_i\log(1/r_i)$ is the Lyapunov exponent, and $\tau'(1)=-\sum_i p_i\log r_i$; the first is the dimension of the measure of *The Self-Similar Measure and the Invariant Measure*, and both are the derivatives of the same convex function.

## The Legendre Transform and the Multifractal Formalism

### The Legendre Transform

**Definition.** The **Legendre transform** of the convex function $\tau$ is

$$
\tau^*(\alpha)=\inf_{q\in\mathbb{R}}\bigl(q\alpha-\tau(q)\bigr) ,
$$

the concave conjugate; the infimum is attained at the $q$ with $\tau'(q)=\alpha$ when such a $q$ exists, and is $-\infty$ otherwise, so that $\tau^*$ is finite exactly on the closed interval between the one-sided limits $\tau'(+\infty)$ and $\tau'(-\infty)$.

**Proposition (the transform is the concave envelope parametrised by the derivative).** Where $\tau$ is differentiable and $\alpha=\tau'(q)$ with $q$ in the range of the derivative, the transform takes the value $\tau^*(\alpha)=q\alpha-\tau(q)$.

*Proof.* The function $q\mapsto q\alpha-\tau(q)$ is concave, since it is affine minus convex; its derivative at $q'$ is $\alpha-\tau'(q')$, which vanishes at $q'=q$ by the choice of $\alpha=\tau'(q)$, so the infimum is attained there. The value is the stated one. (Fermat's rule for a concave differentiable function is the convex analysis of Part III.)

### The Multifractal Formalism

**Definition.** The measure $\mu$ satisfies the **multifractal formalism** at the exponent $\alpha$ if

$$
f(\alpha)=\tau^*(\alpha)\qquad\text{and}\qquad f(\alpha)=q\alpha-\tau(q)\quad\text{with }\tau'(q)=\alpha .
$$

**Theorem (the formalism for the self-similar measures).** Let $S_1,\dots,S_m$ be a self-similar iterated function system satisfying the open set condition, and let the ratios be distinct or the pieces separated in the sense that the $n$-th level pieces have pairwise disjoint neighbourhoods of comparable size; let $p$ be a probability vector and $\mu_p$ the self-similar measure. Then the local dimension exists at every point, the level sets are nonempty exactly on the interval of exponents $[\tau'(+\infty),\tau'(-\infty)]$, and the multifractal formalism holds:

$$
\dim_H K_\alpha=\inf_{q}(q\alpha-\tau(q))=\tau^*(\alpha)
$$

for every $\alpha$ in that interval.

*Proof sketch.* The upper bound $f(\alpha)\le\tau^*(\alpha)$ is the covering of $K_\alpha$ at level $n$ by the pieces of mass about $r^n$ and of size about $r^n$, with the exponent $q$ chosen to balance the two; it uses only the definition of $\tau$. The lower bound is the mass distribution principle of *Fractal Geometry* applied to the **Gibbs measure** $q$ of the theorem on the growth exponent: the Gibbs measure gives to the level-$n$ pieces the masses proportional to $p^q r^{-n\tau(q)}$, it is supported on a subset of $K_\alpha$ with $\alpha=\tau'(q)$, and its local dimension there is $q\alpha-\tau(q)$; the Hausdorff dimension of that subset is at least that value. The full argument, and the precise separation hypotheses, are those of the multifractal formalism in the lecture notes of Falconer and Pesin.

**Theorem (the failure in general).** The formalism can fail: there are self-similar measures for which the union of the pieces overlaps so much that some level set has Hausdorff dimension strictly less than $\tau^*(\alpha)$, or is empty while the transform is finite. In particular the equality requires more than the existence of the measure, and the transform is only an upper bound in general.

*Proof sketch.* For overlapping constructions one produces a family of pieces whose diameters are much smaller than the diameters prescribed by the ratios — the "$\tau$-covering" fails because the pieces coincide — and this lowers the dimension of the level set without changing the moment sums and hence $\tau$. The explicit overlapping examples (the multiplicative chaos and the random constructions) are in the literature; the point recorded here is that the formalism is a theorem under the open set condition and a conjecture or falsehood outside it.

## The Computed Examples

### The Bernoulli Measures on the Cantor Set

Take the middle-thirds Cantor set, $S_0(x)=\tfrac13x$, $S_1(x)=\tfrac13x+\tfrac23$, so $r_1=r_2=\tfrac13$ and $\dim_H\Lambda=\log2/\log3=0.630930$. For the weights $p=(p_0,p_1)$ the exponent is $\tau(q)=-\log_3(p_0^q+p_1^q)$ and the spectrum is parametrised by

$$
\alpha(q)=\frac{p_0^q\log(1/p_0)+p_1^q\log(1/p_1)}{(p_0^q+p_1^q)\log3},
\qquad
f(\alpha(q))=q\alpha(q)-\tau(q).
$$

The uniform weights $p=(\tfrac12,\tfrac12)$ give $\alpha=\log2/\log3$ for every $q$, so the spectrum is the single point $f(\log2/\log3)=\log2/\log3$: the measure is dimension-regular and multifractal analysis returns the dimension of the measure. The biased weights $p=(\tfrac13,\tfrac23)$ give a genuine spectrum, computed at the integers below.

| $q$ | $\tau(q)$ | $\alpha(q)$ | $f(\alpha(q))$ |
|---|---|---|---|
| $-3$ | $-3.107211$ | $0.929897$ | $0.317521$ |
| $-2$ | $-2.203114$ | $0.873814$ | $0.455486$ |
| $-1$ | $-1.369070$ | $0.789690$ | $0.579380$ |
| $0$ | $-0.630930$ | $0.684535$ | $0.630930$ |
| $1$ | $0.000000$ | $0.579380$ | $0.579380$ |
| $2$ | $0.535026$ | $0.495256$ | $0.455486$ |
| $3$ | $1.000000$ | $0.439174$ | $0.317521$ |

The spectrum is supported on the exponents $[\alpha({\to}+\infty),\alpha({\to}-\infty)]=[-\log_3\tfrac23,-\log_3\tfrac13]=[0.369070,1]$, it vanishes at both ends, and its maximum $0.630930=\log2/\log3$ at $q=0$ is the dimension of the **support**; the value at $q=1$, $0.579380=H(p)/\log3$, is the dimension of the **measure** of *The Self-Similar Measure and the Invariant Measure*. The two are different, which is the phenomenon the spectrum records; the values were recomputed from the equation $\sum_i p_i^q r_i^{-\tau}=1$ on the grid above.

### The Self-Similar Measures on the Sierpiński Gasket

Take the Sierpiński gasket, the attractor of three maps of ratio $r=\tfrac12$ on the ternary tree of *Fractal Geometry*, of dimension $\log3/\log2=1.584963$. The exponent solves $\sum_i p_i^q2^{\tau(q)}=1$, so $\tau(q)=-\log_2\sum_i p_i^q$. The uniform weights $p_i=\tfrac13$ give the constant $\alpha=\log3/\log2$ and the single-point spectrum $f=1.584963$; the biased weights $p=(\tfrac12,\tfrac14,\tfrac14)$ give the values:

| $q$ | $\tau(q)$ | $\alpha(q)$ | $f(\alpha(q))$ |
|---|---|---|---|
| $-2$ | $-5.169925$ | $1.888889$ | $1.392147$ |
| $-1$ | $-3.321928$ | $1.800000$ | $1.521928$ |
| $0$ | $-1.584963$ | $1.666667$ | $1.584963$ |
| $1$ | $0.000000$ | $1.500000$ | $1.500000$ |
| $2$ | $1.415037$ | $1.333333$ | $1.251629$ |
| $3$ | $2.678072$ | $1.200000$ | $0.921928$ |

The spectrum is supported on $[1,2]$, its maximum $1.584963=\log3/\log2$ at $q=0$ is the dimension of the gasket, and the value at $q=1$, $1.5$, is the dimension of the measure; the dimension of the measure is strictly below the dimension of the set, and the spectrum fills the gap. The self-similar measure on the gasket is the measure whose multifractal spectrum the thermodynamic formalism of Part III produces, and it is the input of the Dirichlet form of the next article.

## The Large-Deviation Reading

**Remark (the transform is a rate function).** The measure $\nu_p$ on the boundary is the product measure of the weights $p_x$, and the level set $K_\alpha$ is, up to the coding, the set of sequences whose **empirical frequency** deviates from $p$ so as to produce the exponent $\alpha$. The logarithmic moment generating function of the empirical frequency is
$$
\Lambda(q)=\log\sum_{x\in X}p_x^q e^{q\log(1/r_{\text{size}})},
$$
and the growth exponent $\tau$ is its Legendre dual; the multifractal spectrum is the rate function of the large deviations of the empirical frequencies, and the **Cramér** or **Gärtner–Ellis** theorem of *Laws of Large Numbers and the Central Limit Theorem* is the probabilistic form of the Legendre identity. The heuristic is exact for the Bernoulli measures because the empirical frequencies are the means of independent random variables; for the general self-similar measures the corresponding statement is the thermodynamic formalism of *Ergodic Theory*, in which the pressure replaces the logarithm of the moment generating function and the equilibrium state replaces the product measure.

## Summary

The **local dimension** $\alpha(x)$ is the exponent of the decay of the mass of the ball $\mu(B(x,\rho))$; the **level set** $K_\alpha$ collects the points of dimension $\alpha$, and the **multifractal spectrum** $f(\alpha)=\dim_H K_\alpha$ measures the level sets. The **moment sums** $S_n(q)=\sum_{|w|=n}\mu(S_w\Lambda)^q$ have the growth exponent $\tau(q)$ determined by the equation of Bowen $\sum_i p_i^q r_i^{-\tau(q)}=1$; $\tau$ is convex and decreasing, with $\tau(0)=-\dim_H\Lambda$ and $\tau(1)=0$. The **multifractal formalism** is the identity $f(\alpha)=\tau^*(\alpha)=\inf_q(q\alpha-\tau(q))$ on the range of the exponents; it is a theorem for the self-similar measures under the open set condition together with the separation of the pieces, and it can fail when the pieces overlap, the transform then being only an upper bound. For the Cantor set with $r_i=\tfrac13$ the exponent is $\tau(q)=-\log_3(p_0^q+p_1^q)$ and the spectrum is supported on $[0.369070,1]$ for $p=(\tfrac13,\tfrac23)$, with the maximum $0.630930=\log2/\log3$ at $q=0$ and the value $0.579380=H(p)/\log3$ at $q=1$; for the Sierpiński gasket with $r=\tfrac12$ the spectrum of $p=(\tfrac12,\tfrac14,\tfrac14)$ is supported on $[1,2]$, runs from $1.392147$ through $1.584963=\log3/\log2$ to $0.921928$, and separates the dimension of the measure from the dimension of the set. The tables were recomputed from the equation of Bowen on a grid of $q$; the theorems of validity and of failure are quoted from the multifractal literature, and the dimension of the sets is that of *Fractal Geometry*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\alpha(x)$ | Local dimension of the measure at $x$ |
| $K_\alpha=\{x:\alpha(x)=\alpha\}$ | Level set of the exponent $\alpha$ |
| $f(\alpha)=\dim_H K_\alpha$ | Multifractal spectrum |
| $S_n(q)=\sum_{|w|=n}\mu(S_w\Lambda)^q$ | Moment sum at level $n$ |
| $\sum_i p_i^q r_i^{-\tau(q)}=1$ | The equation of Bowen for the growth exponent |
| $\tau(q)$, $\tau(0)=-\dim_H\Lambda$, $\tau(1)=0$ | Growth exponent and its two values |
| $q_i\propto p_i^q r_i^{-\tau(q)}$ | The Gibbs probability of the exponent |
| $\tau^*(\alpha)=\inf_q(q\alpha-\tau(q))$ | The Legendre transform |
| $[\tau'(+\infty),\tau'(-\infty)]$ | The support of the spectrum |

## Further Reading

- Kenneth Falconer, *Techniques in Fractal Geometry* (Wiley, 1997), for the moment sums, the Legendre transform and the multifractal formalism.
- Kenneth Falconer, *Fractal Geometry: Mathematical Foundations and Applications* (Wiley, 3rd ed. 2014), for the Hausdorff dimension of the level sets and the mass distribution principle.
- Yakov B. Pesin, *Dimension Theory in Dynamical Systems* (University of Chicago Press, 1997), for the dimension spectrum and the thermodynamic formalism.
- Yakov B. Pesin and Howard Weiss, "A multifractal analysis of equilibrium measures for conformal expanding maps and Moran-like geometric constructions", *Journal of Statistical Physics* **86** (1997), 233–275, for the formalism for the self-similar measures.
- Manfred Arbeiter and Niels Patzschke, "Random self-similar multifractals", *Mathematische Nachrichten* **181** (1996), 5–42, for the random and overlapping constructions.
- Julien Barral and Stéphane Seuret, "The singularity spectrum of Lévy processes in multifractal time", *Advances in Mathematics* **214** (2007), 437–468, for the failure of the formalism outside the open set condition.
- Peter Walters, *An Introduction to Ergodic Theory* (Springer, 1982), and David Ruelle, *Thermodynamic Formalism* (Addison-Wesley, 1978), for the pressure, the equilibrium states and the large-deviation reading.
