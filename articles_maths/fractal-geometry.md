
# __Fractal Geometry__

## Introduction

A **fractal** is a set in a metric space whose irregularity is measured by a dimension that is not an integer: the middle-thirds Cantor set is a subset of the line with dimension $\log 2/\log 3$, the Sierpiński triangle a subset of the plane with dimension $\log 3/\log 2$, the Koch curve a curve of dimension $\log 4/\log 3$. These sets are all built by an exact recursion — a finite list of similarity maps applied again and again — and the recursion is what determines the dimension, by the balance of the number of pieces against the factor by which each piece is a scaled copy of the whole. A set with this property is **self-similar**, and for the self-similar sets satisfying a mild separation condition the dimension is exactly the growth rate $\log m / \log(1/r)$ of the construction, a number that is an integer only in the degenerate cases.

The theory is one of the corpus's two uses of a metric that is not a length. The topological dimension, the smallest integer such that the space is locally like Euclidean space of that dimension, is invariant under homeomorphism; the fractal dimensions are not, and this is exactly what makes them useful: they detect the metric structure, the way the parts of a set are distributed in the ambient space, and not merely the open sets. Two sets homeomorphic to the Cantor set — the middle-thirds set and the standard Cantor discontinuum of $\mathbb{R}$ — have the same topological dimension zero, and the theory of fractals is the study of the further metric information that the distance supplies. The dimensions are computed from covers by sets of prescribed diameter, and the whole theory is therefore available with a distance and nothing else; the corresponding *measures* — the Hausdorff measures, which assign to a set the limiting content in a fractional dimension — belong to Part III, where the measure and the integral are available, and only the critical exponent, a purely metric quantity, is used here.

This article defines the **box-counting dimension** and the **Hausdorff dimension** of a bounded set in a metric space, proves that the Hausdorff dimension never exceeds the box dimension and that neither is a topological invariant, and computes both for the standard examples: the Cantor set, the Sierpiński triangle and carpet, the Koch curve and the Menger sponge. It establishes the **similarity dimension** of a self-similar set by the open set condition and the **contraction mapping theorem** for the existence of the attractor of an iterated function system, and it gives the countable stability of the Hausdorff dimension and the failure of countable stability for the box dimension. The examples include the $p$-adic integers with the ultrametric of *Metric, Uniform and Complete Spaces*, which are self-similar of dimension $1$. The topological dimension is the subject of *Dimension Theory*, written in parallel, and the contrast between it and the fractal dimensions is stated here and computed there. The dynamical reading of a self-similar set as the repeller of a map — its relation to the shift, the coding and the invariant measures — is the subject of Part III, where the measure and the limit are available.

The article assumes *Metric, Uniform and Complete Spaces* for the distance, the diameter, completeness, the Lipschitz and Hölder conditions, the contraction mapping theorem and the Baire category theorem; *Topological Spaces* for compactness, the subspace topology, connectedness and the Cantor set as a topological space; and *Dimension Theory*, written in parallel, for the covering dimension, which is compared with the fractal dimensions and not re-derived. The Hausdorff measure as a measure, its measurability and its integration are Part III's, and the article uses only the covering numbers and the critical exponent. No physics is invoked.

## Covers, Diameters and Covering Numbers

**Definition.** Let $(X, d)$ be a metric space and $E \subseteq X$. The **diameter** of a nonempty set $U \subseteq X$ is

$$
\operatorname{diam} U = \sup\{d(x, y) : x, y \in U\},
$$

with $\operatorname{diam}\emptyset = 0$. A **$\delta$-cover** of $E$ is a countable family $\{U_i\}$ of subsets with $E \subseteq \bigcup_i U_i$ and $\operatorname{diam}U_i \leq \delta$ for every $i$. A set $E$ is **bounded** if $\operatorname{diam}E < \infty$, and the **covering number** is

$$
N(E, \delta) = \text{the least number of sets of diameter at most }\delta\text{ needed to cover }E,
$$

finite for bounded $E$ in a totally bounded space and infinite in general.

**Example.** In $\mathbb{R}^n$ with the Euclidean metric, a bounded set $E$ is covered by the balls of radius $\delta$ centred at the points of a maximal $\delta$-separated subset, and the covering number satisfies $N(E, \delta) \asymp (\operatorname{diam}E/\delta)^n$; the exponent $n$ of the ambient space is exactly what the box dimension recovers.

**Definition.** A map $f : X \to Y$ between metric spaces is **Hölder** of exponent $\alpha > 0$ if $d_Y(f(x), f(x')) \leq c\,d_X(x, x')^\alpha$ for some constant $c$; it is **Lipschitz** if this holds with $\alpha = 1$, and **bi-Lipschitz** if in addition it has a bi-Lipschitz inverse. Bi-Lipschitz maps are the natural equivalences of the theory: they preserve the covering numbers up to a constant and therefore every dimension considered below.

## The Box-Counting Dimension

**Definition.** For a bounded set $E$ in a metric space, the **lower and upper box-counting dimensions** are

$$
\underline{\dim}_B E = \liminf_{\delta \to 0}\frac{\log N(E, \delta)}{\log(1/\delta)}, \qquad \overline{\dim}_B E = \limsup_{\delta \to 0}\frac{\log N(E, \delta)}{\log(1/\delta)} ,
$$

and the **box-counting dimension** is $\dim_B E = \underline{\dim}_B E = \overline{\dim}_B E$ when the two agree. The quantity does not change if $N(E,\delta)$ is replaced by the number of closed balls of radius $\delta$ that meet $E$, or by the number of cubes of side $\delta$ that meet $E$ in $\mathbb{R}^n$.

**Example (the segment and the smooth curve).** For a bounded interval $I \subseteq \mathbb{R}$, $N(I, \delta) \asymp \delta^{-1}$ and $\dim_B I = 1$; for a compact curve with nonvanishing curvature, $N(E,\delta) \asymp \delta^{-1}$ and $\dim_B E = 1$; for a bounded region with interior, $N(E, \delta) \asymp \delta^{-n}$ and $\dim_B E = n$. The box dimension of a smooth object is its ordinary dimension, so the concept is an extension and not a competing notion.

**Theorem (properties).** For bounded subsets of a metric space, the box dimensions satisfy:

**(a)** monotonicity: $E \subseteq E'$ implies $\underline{\dim}_B E \leq \underline{\dim}_B E'$ and $\overline{\dim}_B E \leq \overline{\dim}_B E'$;

**(b)** finite stability: $\dim_B(E_1 \cup \cdots \cup E_k) = \max_i \dim_B E_i$;

**(c)** bi-Lipschitz invariance: if $f$ is bi-Lipschitz then $\dim_B f(E) = \dim_B E$;

**(d)** for bounded $E_1, E_2$, $\overline{\dim}_B(E_1 \times E_2) \leq \overline{\dim}_B E_1 + \overline{\dim}_B E_2$;

**(e)** countable sets can have positive box dimension, and the box dimensions are not countably stable.

**Proof sketch.** (a) and (b) are the corresponding properties of the covering number, a cover of the union being the union of the covers; (c) follows because a bi-Lipschitz map changes the covering number by at most a power factor; (d) is the product of covers; (e) is the example below. $\square$

**Example (a countable set of box dimension $\tfrac{1}{2}$).** Let $E = \{0\}\cup\{1/n : n \geq 1\} \subseteq \mathbb{R}$. The set is countable, hence of Hausdorff dimension zero. To compute its covering number, fix $\delta$; the points $1/n$ with $1/n \geq \sqrt{\delta}$ number about $\delta^{-1/2}$ and are pairwise farther apart than $\delta$, so each needs its own set, while the remaining points, which lie in $[0,\sqrt{\delta}]$, are covered by about $\sqrt{\delta}/\delta = \delta^{-1/2}$ sets of diameter $\delta$. Hence $N(E, \delta) \asymp \delta^{-1/2}$ and

$$
\dim_B E = \lim_{\delta \to 0}\frac{\log\bigl(c\,\delta^{-1/2}\bigr)}{\log(1/\delta)} = \frac{1}{2} .
$$

The set is compact, countable, of topological dimension zero and of box dimension $1/2$: no integer, no topological invariant, and not the Hausdorff dimension, which is zero.

**Remark.** The box dimension is the dimension appropriate to the covering numbers; it is a metric invariant but not a topological one, and it is not stable under countable unions. The Hausdorff dimension, defined next, is countably stable and is the dimension of the theory; the box dimension is the more computable of the two and often coincides with it.

## The Hausdorff Dimension

**Definition.** Let $E$ be a subset of a metric space. For $s \geq 0$ and $\delta > 0$ put

$$
\mathcal{H}^s_\delta(E) = \inf\left\{\sum_i (\operatorname{diam}U_i)^s : \{U_i\}\ \text{a countable }\delta\text{-cover of } E\right\}, \qquad \mathcal{H}^s(E) = \sup_{\delta>0}\mathcal{H}^s_\delta(E) .
$$

The quantity $\mathcal{H}^s(E)$ is the **Hausdorff $s$-content**. It is monotone and countably subadditive in $E$, and it is decreasing in $s$; the **Hausdorff dimension** is the critical exponent

$$
\dim_H E = \inf\{s \geq 0 : \mathcal{H}^s(E) = 0\} = \sup\{s \geq 0 : \mathcal{H}^s(E) = \infty\} ,
$$

the infimum and the supremum being taken in $[0,\infty]$, with the convention that $\dim_H E = 0$ for a finite set and $\dim_H E = \infty$ when $\mathcal{H}^s(E) = \infty$ for every $s$.

**Remark (what is deferred, and why the dimension is available).** The value $\mathcal{H}^s(E)$ is defined by covers and diameters, hence by the distance alone; the assignment $E \mapsto \mathcal{H}^s(E)$ extends to a **Borel measure** on the metric space, the **Hausdorff $s$-measure**, whose measurable sets, null sets, integrals and the measure-theoretic dimension theory are the subject of Part III, where the measure and the integral are available. This article uses only the critical exponent and the elementary covering estimates for it: the exponent depends on the distance and on nothing else, which is why it belongs here, while statements about the measure of a set and its integration belong to Part III and are cited there. The symbol $\mathcal{H}^s$ is used below only as the cover-defined content.

**Theorem.** For subsets of a metric space the Hausdorff dimension satisfies:

**(a)** monotonicity: $E \subseteq E'$ implies $\dim_H E \leq \dim_H E'$;

**(b)** countable stability: $\dim_H\bigl(\bigcup_{i=1}^\infty E_i\bigr) = \sup_i \dim_H E_i$;

**(c)** $\dim_H E = 0$ for every countable $E$;

**(d)** Hölder invariance: if $f$ is Hölder of exponent $\alpha$ then $\dim_H f(E) \leq \dim_H E/\alpha$; in particular a Lipschitz map does not increase the Hausdorff dimension, and a bi-Lipschitz map preserves it.

**Proof sketch.** (a) is immediate from the covers. (b) is the countable subadditivity of $\mathcal{H}^s$, with the reverse inequality from (a). (c) follows because a point has dimension zero and a countable union is countably stable. (d) follows because the image of a $\delta$-cover under a Hölder map is a $c\delta^\alpha$-cover whose contribution to the $s$-content picks up the factor $\delta^{s\alpha}$, and the two exponents must balance. $\square$

**Theorem (comparison).** For every bounded set $E$,

$$
\dim_H E \leq \underline{\dim}_B E \leq \overline{\dim}_B E ,
$$

and the inequalities can be strict on both sides. The Hausdorff dimension is countably stable and the box dimension is not; equality holds for the self-similar sets satisfying the open set condition, below.

**Proof sketch.** Covering $E$ by $N(E,\delta)$ sets of diameter $\delta$ gives $\mathcal{H}^s_\delta(E) \leq N(E,\delta)\delta^s$, which tends to $0$ for $s > \underline{\dim}_B E$; hence $\dim_H E \leq \underline{\dim}_B E$. $\square$

**Example (the strictness of the first inequality).** The set $E = \{0\} \cup \{1/n\}$ of the previous section has $\dim_H E = 0 < \tfrac12 = \dim_B E$; the set of irrationals in a bounded interval has $\dim_H = 1 = \dim_B$; the set of rationals in a bounded interval has $\dim_H = 0$ and $\dim_B = 1$, so the second inequality is strict as well.

## Self-Similar Sets

### Iterated Function Systems

**Definition.** An **iterated function system** (IFS) on a complete metric space $X$ is a finite family of contractions $f_1, \ldots, f_m : X \to X$ with ratios $r_i < 1$, $d(f_i(x), f_i(y)) \leq r_i\,d(x,y)$. A set $\Lambda \subseteq X$ is **invariant** for the system if

$$
\Lambda = \bigcup_{i=1}^m f_i(\Lambda) .
$$

The system is **self-similar** if each $f_i$ is a similarity, $d(f_i(x), f_i(y)) = r_i\,d(x,y)$, and the **similarity dimension** of the system is the unique $s \geq 0$ with

$$
\sum_{i=1}^m r_i^{\,s} = 1 .
$$

The left side is strictly decreasing in $s$, tending to $m > 1$ at $s = 0$ and to $0$ as $s\to\infty$, so $s$ exists and is unique; it is positive.

**Theorem (the attractor).** Let $f_1, \ldots, f_m$ be an iterated function system on a complete metric space $X$. There is exactly one nonempty compact set $\Lambda$ invariant for the system, the **attractor**; it is the limit, in the Hausdorff metric, of the iterates of any nonempty compact set, and

$$
\Lambda = \bigcap_{k=1}^\infty \bigcup_{|i| = k} f_{i_1}\circ\cdots\circ f_{i_k}(X) ,
$$

where the union is over the words of length $k$.

**Proof sketch.** On the set $\mathcal{K}(X)$ of nonempty compact subsets of $X$ with the Hausdorff distance, the map $F(S) = \bigcup_i f_i(S)$ is a contraction with ratio $\max_i r_i < 1$, and $\mathcal{K}(X)$ is complete, so the contraction mapping theorem of *Metric, Uniform and Complete Spaces* gives a unique fixed point; the explicit intersection is the image of the fixed point under the iteration. $\square$

**Definition (the open set condition).** The system satisfies the **open set condition** if there is a nonempty bounded open set $V$ with $\bigcup_{i=1}^m f_i(V) \subseteq V$ and the images $f_i(V)$ pairwise disjoint.

**Theorem (Moran, Hutchinson).** Let $f_1,\ldots,f_m$ be a self-similar IFS on $\mathbb{R}^n$ satisfying the open set condition. Then

$$
\dim_H \Lambda = \dim_B \Lambda = s, \qquad \sum_{i=1}^m r_i^{\,s} = 1 ,
$$

and $0 < \mathcal{H}^s(\Lambda) < \infty$.

**Proof sketch.** The open set condition arranges that the $k$-th level pieces $f_{i_1}\circ\cdots\circ f_{i_k}(V)$ are disjoint and each is a scaled copy of $V$, so the cover of $\Lambda$ by the level-$k$ pieces is close to optimal; the upper bound on the dimension is the count $\sum_{|i|=k}(\operatorname{diam} f_{i_1}\cdots f_{i_k}(V))^s \leq (\operatorname{diam}V)^s(\sum_i r_i^s)^k$, which stays bounded exactly at the root $s$, and the lower bound uses the disjointness and the mass distribution principle, which is the measure-theoretic input of Part III quoted here only in its covering form. $\square$

### The Standard Examples

**Example (the middle-thirds Cantor set).** Let $f_1, f_2 : \mathbb{R}\to\mathbb{R}$ be $f_1(x) = x/3$ and $f_2(x) = x/3 + 2/3$; the attractor is the middle-thirds Cantor set $\Lambda$. The ratios are $r_1 = r_2 = 1/3$, so the similarity dimension solves $2\cdot 3^{-s} = 1$, giving

$$
\dim_H \Lambda = \dim_B \Lambda = \frac{\log 2}{\log 3} = 0.6309\ldots ,
$$

the open set condition holding with $V = (0,1)$. Every point of $\Lambda$ has a base-three expansion in the digits $\{0, 2\}$, and the coding of a point by its digit sequence is a homeomorphism of $\Lambda$ onto $\{0,1\}^{\mathbb{N}}$; this is the standard Cantor set of *Topological Spaces*, which is compact, perfect and totally disconnected.

**Example (the Sierpiński triangle and carpet).** The Sierpiński triangle is the attractor of three similarities of ratio $1/2$ centred at the vertices of a triangle, so $3\cdot 2^{-s} = 1$ and

$$
\dim_H = \frac{\log 3}{\log 2} = 1.5849\ldots .
$$

The Sierpiński carpet is the attractor of eight similarities of ratio $1/3$ on the unit square, so $8\cdot 3^{-s} = 1$ and $\dim_H = \log 8/\log 3 = 1.8927\ldots$; the Menger sponge, the three-dimensional analogue, has $m = 20$ maps of ratio $1/3$ and $\dim_H = \log 20/\log 3 = 2.7268\ldots$.

**Example (the Koch curve).** The Koch curve is the attractor of four similarities of ratio $1/3$ that replace a segment by the four sides of the standard bump; $4\cdot 3^{-s} = 1$ gives

$$
\dim_H = \frac{\log 4}{\log 3} = 1.2618\ldots ,
$$

and the Koch snowflake, the union of three rotated copies, has the same dimension and is a closed curve of infinite length enclosing a finite area.

**Example (the $p$-adic integers).** Let $X = \mathbb{Z}_p$ with the ultrametric $d(x,y) = p^{-v_p(x-y)}$ of *Metric, Uniform and Complete Spaces*. The maps $x \mapsto px + a$ for $a = 0, 1, \ldots, p-1$ are similarities of ratio $1/p$ and satisfy the open set condition with $V = \mathbb{Z}_p$; the system has $m = p$ maps and

$$
\dim_H \mathbb{Z}_p = \frac{\log p}{\log p} = 1 ,
$$

the attractor being the whole of $\mathbb{Z}_p$. The $p$-adic integers are thus a self-similar set of dimension one whose topology is that of the Cantor set, of topological dimension zero: the same space carries two metrics of different Hausdorff dimension, and the dimension is a statement about the distance and not about the open sets.

**Example (cardinality does not determine the dimension).** The middle-thirds Cantor set is uncountable and has dimension $\log2/\log3$, while a convergent sequence with its limit is countable and has dimension zero; cardinality and dimension are therefore independent in one direction. For the other direction, let $\Lambda$ be the Cantor-type set obtained at level $k$ by keeping $2^k$ intervals of length $2^{-k^2}$ inside the intervals of level $k-1$: the dissection is consistent because $2\cdot 2^{-(k+1)^2} \leq 2^{-k^2}$, the set is compact, perfect and totally disconnected, hence uncountable and homeomorphic to the Cantor set, while its covering numbers satisfy $N(\Lambda, \delta_k)\asymp 2^k$ at $\delta_k = 2^{-k^2}$ and the box dimension is

$$
\lim_{k\to\infty}\frac{\log 2^k}{\log 2^{k^2}} = \lim_{k\to\infty}\frac{1}{k} = 0 .
$$

Dimension, cardinality and topological dimension are three independent invariants.

## The Shape of the Theory

**Theorem (the dimension of a product).** For Borel sets in Euclidean space,

$$
\dim_H(E_1\times E_2) \geq \dim_H E_1 + \dim_H E_2 , \qquad \dim_H(E_1\times E_2) \leq \dim_H E_1 + \overline{\dim}_B E_2 ,
$$

and the first inequality can be strict; the box dimension satisfies $\overline{\dim}_B(E_1\times E_2) \leq \overline{\dim}_B E_1 + \overline{\dim}_B E_2$.

**Proof sketch.** The upper bound is the product of covers; the lower bound is the Marstrand product theorem, whose proof uses a Fubini-type argument with the Hausdorff measure and therefore belongs to Part III, quoted here as standard. $\square$

**Remark (the local structure, deferred).** For a self-similar attractor $\Lambda$ with the open set condition, the local dimension at a point — the exponent of the growth of the Hausdorff content of $\Lambda \cap B(x, r)$ as $r \to 0$ — equals the global dimension $s$ at almost every point, the exception set being of vanishing content; the precise statement, its almost-everywhere qualifier and its proof require the Hausdorff measure as a measure and the mass distribution principle in full, and they are therefore given in Part III, where the measure and the limit are available. The attractor is the repeller of a map on the ambient space, the coding by the shift makes it a subshift of finite type, and the local dimension is computed from the entropy of the shift and the Lyapunov exponent of the map, which are the invariants of the dynamical systems of Part III.

**Remark (the topological dimension and the fractal dimension).** The **topological (covering) dimension** $\dim_{top}$ of *Dimension Theory*, written in parallel, is the largest integer $n$ such that every finite open cover has a refinement of order $n+1$, and it is a topological invariant. The **fractal dimensions** satisfy

$$
\dim_{top} E \leq \dim_H E \leq \dim_B E ,
$$

with the first inequality strict precisely when $E$ is the kind of set the theory calls fractal: a set with $\dim_H E > \dim_{top}E$ is a fractal in the sense of Mandelbrot, so the Cantor set, the Sierpiński triangle and the Koch curve are fractals, and a segment, a disk and a sphere are not.

**Remark (the regularisation of a fractal).** The dimension bounds the roughness of the image of a set under a map: a rectifiable curve has box dimension $1$, the Koch curve has $\log4/\log3 > 1$, and by part (d) of the theorem on the Hausdorff dimension, the image of a set of dimension $d$ under a Hölder map of exponent $\alpha$ has dimension at most $d/\alpha$. Smooth maps can therefore only lower the dimension, and the only way a map can raise it is by failing to be Hölder of the appropriate exponent.

## Summary

The box-counting dimension of a bounded set in a metric space is the exponent of the growth of its covering number, $\dim_B E = \lim \log N(E,\delta)/\log(1/\delta)$; it is monotone, finitely stable, bi-Lipschitz invariant, sub-additive on products, and not countably stable — a countable set can have positive box dimension, the set $\{0\}\cup\{1/n\}$ having box dimension $1/2$. The Hausdorff dimension is the critical exponent of the series $\sum_i(\operatorname{diam}U_i)^s$ over the countable covers of $E$; it is monotone, countably stable, zero on every countable set, and decreases by at most the factor $1/\alpha$ under a Hölder map of exponent $\alpha$, so that it is bi-Lipschitz invariant. For every bounded set $\dim_H E \leq \underline{\dim}_B E \leq \overline{\dim}_B E$, and both inequalities can be strict; the box dimension is the more computable and the Hausdorff dimension the more stable of the two.

An iterated function system is a finite family of contractions of a complete metric space, and it has a unique nonempty compact invariant set, the attractor, obtained as the fixed point of the contraction on the space of compact sets with the Hausdorff metric. For a self-similar system satisfying the open set condition the Hausdorff and box dimensions of the attractor are both equal to the similarity dimension $s$, the unique solution of $\sum_i r_i^s = 1$; the Cantor set has dimension $\log2/\log3$, the Sierpiński triangle $\log3/\log2$, the Koch curve $\log4/\log3$, the Sierpiński carpet $\log8/\log3$ and the Menger sponge $\log20/\log3$. The $p$-adic integers are a self-similar set of dimension one whose topological dimension is zero, so the fractal dimension depends on the metric and not only on the topology. The topological dimension is at most the Hausdorff dimension, with equality exactly for the sets that are not fractal; the dynamical reading of the attractor, its coding by the shift and its local dimension in the sense of the measure, belong to Part III, and the measure-theoretic development of the Hausdorff content used here belongs there as well.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(X, d)$, $E$, $\Lambda$ | Metric space; bounded subset; attractor of an iterated function system |
| $\operatorname{diam} U$ | Diameter, $\sup\{d(x,y)\}$ over $U$ |
| $\delta$-cover, $N(E,\delta)$ | Cover by sets of diameter at most $\delta$; covering number |
| $\underline{\dim}_B E$, $\overline{\dim}_B E$, $\dim_B E$ | Lower, upper and (when equal) box-counting dimension |
| $\mathcal{H}^s_\delta(E)$, $\mathcal{H}^s(E)$ | Hausdorff $s$-content of a $\delta$-cover; the cover-defined content |
| $\dim_H E$ | Hausdorff dimension; the critical exponent of $\mathcal{H}^s$ |
| $f_i$, $r_i$, $m$ | Contractions, their ratios, their number |
| The open set condition | Disjoint images of an open set under the maps |
| $\sum_i r_i^s = 1$ | Similarity dimension of a self-similar system |
| $\dim_{top} E$ | Topological (covering) dimension; $\dim_{top} \leq \dim_H \leq \dim_B$ |
| $\log2/\log3$, $\log3/\log2$, $\log4/\log3$ | Dimensions of the Cantor set, the Sierpiński triangle, the Koch curve |
| Hölder, Lipschitz, bi-Lipschitz | $d(fx, fx') \leq c\,d(x,x')^\alpha$; $\alpha = 1$; with bi-Lipschitz inverse |

## Further Reading

- Kenneth Falconer, *Fractal Geometry: Mathematical Foundations and Applications* (Wiley, 3rd edition, 2014), for the box and Hausdorff dimensions and the self-similar sets.
- Benoit B. Mandelbrot, *The Fractal Geometry of Nature* (Freeman, 1982), for the examples and the definition of a fractal by dimension.
- John E. Hutchinson, "Fractals and self-similarity", *Indiana University Mathematics Journal* 30 (1981), 713–747, for the attractor and the open set condition.
- Patrizia A. P. Moran, "Additive functions of intervals and Hausdorff measure", *Mathematical Proceedings of the Cambridge Philosophical Society* 42 (1946), 15–23, for the exact dimension of a self-similar set.
- Kenneth Falconer, *Techniques in Fractal Geometry* (Wiley, 1997), for the product formulae and the local structure of self-similar sets.
- Pertti Mattila, *Geometry of Sets and Measures in Euclidean Spaces* (Cambridge University Press, 1995), for the Marstrand product theorem and the measure-theoretic dimension theory.
- Christopher J. Bishop and Yuval Peres, *Fractal Sets in Probability and Analysis* (Cambridge University Press, 2017), for the local dimension and the multifractal formalism.
