# __Rectifiability and the Geometry of Fractal Curves__

## Introduction

A **curve** is the image of a continuous map of an interval. Its **length** is the supremum of the lengths of the polygons inscribed in it, and the curve is **rectifiable** when this supremum is finite. Rectifiability is the property that separates the curves of ordinary geometry from the curves of fractal geometry. A circle, a graph of a smooth function and a polygonal arc are rectifiable; they can be traversed at unit speed, and their length is the integral of the speed. The **Koch curve** is not: at its $n$-th stage it is a polygonal arc of length $3(4/3)^n$, so its length is infinite, and yet it is a curve in the topological sense, homeomorphic to an interval, and of Hausdorff dimension $\log 4/\log 3$. The roughness that the dimension detects is exactly what the length fails to see, and the two notions of size — the $1$-dimensional length and the $s$-dimensional content of *Fractal Geometry* — disagree at every scale on such a curve.

This article defines the length of a curve, proves the arc-length reparametrisation, and shows that every rectifiable curve has Hausdorff dimension one and finite positive one-dimensional content. It then states the criterion that makes the converse work: a set of finite one-dimensional content is rectifiable exactly when it has an approximate tangent line at almost every point, a theorem whose proof uses the measure and the structure theorem of *Geometric Measure Theory* and is therefore cited there and not repeated. The **Koch curve** is computed as the standard counterexample, and the **snowflake metric** $d^\alpha$ with $0 < \alpha < 1$ is computed as the operation that turns a rectifiable curve into a non-rectifiable one: the snowflaked interval is a topological curve of dimension $1/\alpha$, so rectifiability is not a topological property.

The article assumes *Metric, Uniform and Complete Spaces* for the distance, the diameter, completeness, the Lipschitz and Hölder conditions, uniform convergence and the length of a curve as a sup of inscribed polygons; *Topological Spaces* for compactness, connectedness and the homeomorphism of an interval with its image; and *Fractal Geometry* for the covering numbers, the Hausdorff content $\mathcal{H}^s$, the dimension $\dim_H$ and the self-similar sets. The normalisation of the Hausdorff *measure* — the constant $\beta_s$ that distinguishes the measure of *Geometric Measure Theory* from the cover-defined content used here — is immaterial for the dimension and is fixed there; here $\mathcal{H}^s$ is the cover-defined content of *Fractal Geometry*.

## Length and Variation

**Definition.** Let $X$ be a metric space and let $\gamma : [a,b] \to X$ be continuous. For a partition $\mathcal{P} = \{a = t_0 < t_1 < \cdots < t_k = b\}$ write

$$
L(\gamma, \mathcal{P}) = \sum_{i=1}^{k} d\bigl(\gamma(t_{i-1}), \gamma(t_i)\bigr) ,
$$

and define the **length** of $\gamma$ as

$$
\ell(\gamma) = \sup_{\mathcal{P}} L(\gamma, \mathcal{P}) \in [0,\infty] .
$$

The curve is **rectifiable** when $\ell(\gamma) < \infty$, and a subset $E \subseteq X$ is a **rectifiable curve** when it is the image of a rectifiable map of an interval. A curve is **of bounded variation** when its coordinate functions in $\mathbb{R}^n$ are of bounded variation; for a real-valued function on an interval this is the same as finite total variation, and the length of the graph is the total variation of the two coordinate functions.

**Theorem (elementary properties).** For continuous $\gamma : [a,b] \to X$:

**(a)** $\ell(\gamma)$ is additive over subdivisions, $\ell(\gamma|_{[a,c]}) + \ell(\gamma|_{[c,b]}) = \ell(\gamma)$, and it is invariant under a monotone continuous reparametrisation of $[a,b]$;

**(b)** $\ell$ is lower semicontinuous under uniform convergence: if $\gamma_k \to \gamma$ uniformly then $\ell(\gamma) \leq \liminf_k \ell(\gamma_k)$;

**(c)** $\gamma$ is rectifiable if and only if it has a Lipschitz reparametrisation, if and only if the function $s(t) = \ell(\gamma|_{[a,t]})$ satisfies $s(t) - s(t') \geq d(\gamma(t), \gamma(t'))$ and is finite;

**(d)** if $\gamma$ is rectifiable then $s$ is continuous, non-decreasing and finite, and $\gamma(t) = \tilde{\gamma}(s(t))$ for a unique map $\tilde{\gamma}$ on $[0, \ell(\gamma)]$, the **arc-length parametrisation**.

**Proof sketch.** (a) is the additivity of the supremum over partitions and the triangle inequality. (b) a partition of $\gamma$ is approximated by the same partition of $\gamma_k$ for large $k$. (c) if $\ell(\gamma) < \infty$ then $d(\gamma(t),\gamma(t')) \leq \ell(\gamma|_{[t,t']}) = s(t') - s(t)$, so $s$ is monotone and $\tilde\gamma$ is $1$-Lipschitz; conversely a Lipschitz map has finite length bounded by the Lipschitz constant times the length of the interval. (d) $s$ is continuous because $d(\gamma(t),\gamma(t')) \to 0$ as $t \to t'$ by uniform continuity of $\gamma$ on the compact interval, and $s$ is onto $[0,\ell(\gamma)]$ by the intermediate value theorem; $\tilde\gamma$ is well defined because $s(t)=s(t')$ forces $\gamma(t)=\gamma(t')$.

**Example (smooth and piecewise smooth curves in $\mathbb{R}^n$).** If $\gamma$ is $C^1$ then $\tilde\gamma$ is $1$-Lipschitz, hence differentiable almost everywhere with $|\tilde\gamma'| \leq 1$ by Rademacher's theorem, and

$$
\ell(\gamma) = \int_a^b |\gamma'(t)|\,dt .
$$

The formula is the classical integral formula for arc length, and it is the case of the **area formula** of *Geometric Measure Theory* for one-dimensional domains; for a merely Lipschitz curve it is the same formula with $\gamma'$ existing almost everywhere.

## The Arc-Length Parametrisation

**Theorem (unit speed, and the integral formula).** Let $\gamma$ be rectifiable and let $\tilde\gamma : [0,\ell] \to X$ be its arc-length parametrisation. Then $\tilde\gamma$ is $1$-Lipschitz with $\ell(\tilde\gamma|_{[0,s]}) = s$ for every $s$; if $X = \mathbb{R}^n$ then $|\tilde\gamma'(s)| = 1$ for almost every $s$, and more generally for a Lipschitz $\gamma$

$$
\ell(\gamma) = \int_a^b |\gamma'(t)|\,dt .
$$

**Proof sketch.** By construction $\ell(\tilde\gamma|_{[0,s]}) = s$, so the length grows at unit rate; in $\mathbb{R}^n$ the function $s \mapsto \tilde\gamma(s)$ is Lipschitz with $|\tilde\gamma'| \le 1$ almost everywhere, and if $|\tilde\gamma'| < 1$ on a set of positive measure then the length of the restriction would be strictly less than the parameter increment, a contradiction; the general formula follows by reparametrising $\gamma$ by $s$.

The arc-length parametrisation is therefore the **normalisation** of a rectifiable curve: it is the unique reparametrisation that traverses the curve at unit speed almost everywhere, and it makes the measure-theoretic and the geometric notions of length coincide. Its existence is the content of rectifiability, and it is the reason that rectifiable curves behave like intervals and not like fractals.

**Remark (why the parametrisation is not bi-Lipschitz in general).** The arc-length parametrisation is $1$-Lipschitz, but its inverse need not be Lipschitz: a simple rectifiable curve can return arbitrarily close to an earlier point while the parameter is far ahead, as a curve that nearly closes on itself does. What is true is the dimension statement of the next section, and the sharper statement that a rectifiable curve is the image of an interval under a Lipschitz map, hence of Hausdorff dimension at most one.

## Rectifiable Curves Have Dimension One

**Theorem.** Let $E \subseteq X$ be the image of a non-constant rectifiable curve. Then

$$
\dim_H E = 1 , \qquad \text{and} \qquad 0 < \mathcal{H}^1(E) \leq \ell(\gamma) ,
$$

with $\mathcal{H}^1(E) = \ell(\gamma)$ when $\gamma$ is injective.

**Proof sketch.** A Lipschitz map of an interval is Hölder of exponent $1$, and the Hölder rule $\dim_H f(E) \leq \dim_H E$ of *Fractal Geometry* gives $\dim_H E \leq 1$ because the interval has dimension one. For the reverse inequality, choose $s < t$ with $\gamma(s) \neq \gamma(t)$; the sub-arc between them has length at least $d(\gamma(s),\gamma(t)) > 0$, and the covering content of the sub-arc is at least its diameter, so $\mathcal{H}^1(E) \geq d(\gamma(s),\gamma(t)) > 0$ and $E$ has positive one-dimensional content; a set of positive $\mathcal{H}^1$ has $\dim_H \geq 1$. The equality $\mathcal{H}^1(E) = \ell(\gamma)$ for injective $\gamma$ is the case $m=1$ of the area formula, proved in *Geometric Measure Theory*, where the one-dimensional Hausdorff measure is constructed; the covering content of *Fractal Geometry* differs from it by the constant $\beta_1 = 2$.

**Corollary.** A rectifiable curve is never a fractal in the sense of *Fractal Geometry*: its topological dimension, its Hausdorff dimension and its box dimension all equal one, and its length is its one-dimensional content. The fractal curves are exactly the curves of dimension strictly greater than one, and they have infinite length in every neighbourhood of every point, as the Koch curve shows.

## Rectifiability and Approximate Tangents

The dimension alone does not characterise rectifiability; the missing information is the existence of a tangent line at almost every point. For a set of finite $\mathcal{H}^1$-content the right notion is the **approximate tangent**: a line $V$ is an approximate tangent line of $E$ at $x$ when, for every $\varepsilon > 0$, the set $E \cap B(x,r)$ is contained, for $r$ small enough, in the $\varepsilon r$-neighbourhood of the line $x + V$, up to an $\mathcal{H}^1$-null set.

**Theorem (the one-dimensional structure theorem; *Geometric Measure Theory*).** Let $E \subseteq \mathbb{R}^n$ be a set with $\mathcal{H}^1(E) < \infty$.

**(a)** $E$ has an approximate tangent line at $\mathcal{H}^1$-almost every point $x \in E$ if and only if $E$ is **countably rectifiable**: up to an $\mathcal{H}^1$-null set, $E$ is contained in a countable union of Lipschitz images of $\mathbb{R}$.

**(b)** A connected set with $\mathcal{H}^1(E) < \infty$ is a rectifiable curve (the theorem of Besicovitch on continua of finite length).

**Proof sketch.** The proof of (a) is the case $m=1$ of the Besicovitch–Federer structure theorem: a Lipschitz image of an interval has a tangent at almost every point because a Lipschitz function has a derivative almost everywhere (Rademacher), and conversely the failure of an approximate tangent at a set of positive content forces the content to be infinite by the differentiation theory of measures; the argument uses the measure-theoretic differentiation and the Vitali covering theorem, and it is given in *Geometric Measure Theory*. Part (b) is the classical theorem of Besicovitch that the one-dimensional structure of a continuum of finite length is that of an interval; it is stated there as well.

So rectifiability of a curve is the conjunction of two independent properties: finite length, which is a statement about the covering at all scales, and the existence of an approximate tangent almost everywhere, which is a statement about the first-order behaviour at the points of the set. The fractal curves are those that possess the second only in a degenerate way, and the Koch curve is the standard example.

## The Koch Curve

**Definition (the Koch curve).** Let $K_0 = [0,1]$ and let

$$
S_1(z) = \frac{z}{3}, \qquad S_2(z) = \frac{(1+i\sqrt3)z}{6} + \frac13, \qquad S_3(z) = \frac{(1-i\sqrt3)z}{6} + \frac{3+i\sqrt3}{6}, \qquad S_4(z) = \frac{z+2}{3}
$$

be the four maps of the plane that replace an interval by the four sides of the equilateral triangle erected on it as in the standard construction. The **Koch curve** is the attractor $K$ of the iterated function system $\{S_1,S_2,S_3,S_4\}$, with $\dim_H K = \log 4/\log 3$.

**Theorem (the curve is not rectifiable).** Let $K_n = F^n(K_0)$ with $F = \bigcup_{i}S_i$. Then $K_n$ is a polygonal arc of $4^n$ segments each of length $3^{-n}$, its length is

$$
\ell(K_n) = 4^n \cdot 3^{-n} = \left(\frac{4}{3}\right)^{n} \cdot 1 \longrightarrow \infty ,
$$

so $\ell(K) = \infty$ and $K$ is not rectifiable. The one-dimensional content of $K$ is zero, and for $s = \log 4/\log 3$ the $s$-content of each stage is the constant one:

$$
\mathcal{H}^s(K_n) = 4^n \cdot (3^{-n})^{s} = 4^n \cdot 3^{-n \log 4/\log 3} = 4^n \cdot 4^{-n} = 1 .
$$

**Proof sketch.** Each map is a similarity of ratio $1/3$ and there are four of them, so the $n$-th stage has $4^n$ segments of length $3^{-n}$; the total length is their number times their length and it diverges because $4/3 > 1$. The similarity dimension $s$ solves $\sum_i (1/3)^s = 4 \cdot 3^{-s} = 1$, that is $3^s = 4$ and $s = \log 4/\log 3 = 1.2618\ldots$, by the Moran–Hutchinson theorem of *Fractal Geometry*. At each stage the $s$-content $4^n (3^{-n})^s$ equals one, and since the stage is a $3^{-n}$-cover of $K$ whose content is bounded below times one, the content of $K$ is positive and finite; the dimension is $s$ and not one. The value $s > 1$ is exactly the failure of the Hölder balance that would be needed for a Lipschitz parametrisation, and the infinite length in every sub-arc is the geometric form of that failure.

**Remark (topological curve, fractal dimension).** The Koch curve is homeomorphic to $[0,1]$: it is the image of the Cantor-type coding of the iterated function system, and the coding is continuous and injective. It is therefore a curve in the sense of topology and not a curve in the sense of length, and no homeomorphism of it onto an interval can be Lipschitz. This is the precise sense in which rectifiability is a metric and not a topological property, and it is why the length is the wrong instrument for a fractal curve.

## The Snowflake Metric

**Definition.** For a metric space $(X,d)$ and a real number $0 < \alpha < 1$, the **snowflake** of $(X,d)$ is the metric space $(X, d^\alpha)$, where

$$
d^\alpha(x,y) = d(x,y)^\alpha .
$$

The map is called snowflaking because it is the metric form of the construction of the snowflake curve: the image of the linear interval under the power map $x \mapsto x^\alpha$. The triangle inequality of $d^\alpha$ follows from the concavity of the power on $[0,\infty)$, and $d^\alpha$ and $d$ have the same topology because they induce the same uniform structure of Cauchy sequences.

**Theorem (snowflaking changes the dimension).** For every bounded $E \subseteq X$ and every $0 < \alpha < 1$,

$$
\dim_H (E, d^\alpha) = \frac{1}{\alpha}\,\dim_H (E, d) , \qquad \dim_B (E, d^\alpha) = \frac{1}{\alpha}\,\dim_B (E, d) .
$$

**Proof sketch.** A set $U$ has $d^\alpha$-diameter $(\operatorname{diam}_d U)^\alpha$, so a $d$-cover by sets of diameter at most $\delta$ is a $d^\alpha$-cover by sets of diameter at most $\delta^\alpha$ and conversely; replacing $\delta$ by $\delta^\alpha$ in the exponent of the covering number multiplies the exponent by $1/\alpha$.

**Example (a topological curve of dimension two).** Take $X = [0,1]$ with the Euclidean metric and $\alpha = \tfrac12$. Then $\dim_H([0,1],d^{1/2}) = 2$: the snowflaked interval is a set homeomorphic to an interval whose Hausdorff dimension is two, and its one-dimensional content is zero. Its length is infinite, because the inscribed polygon with the $n$ vertices at the parameter values $k/n$ has $d^{1/2}$-length

$$
\sum_{k=1}^{n} \left(\frac{1}{n}\right)^{1/2} = n^{1/2} \longrightarrow \infty .
$$

So the snowflaking map $x \mapsto x^{1/2}$ turns the standard rectifiable curve into a non-rectifiable one and increases its dimension from one to two, while the topology is unchanged: it is a homeomorphism of the interval onto its image. The map $x \mapsto x^\alpha$ with $\alpha < 1$ is the standard source of fractal curves with prescribed dimension between one and $1/\alpha$, and it is the reason that the dimension of a curve cannot be read from its topology.

**Remark (the inverse direction).** For a self-similar set of dimension $s$ the same computation run backwards identifies $s$ as the exponent for which the "$s$-length" $\sum_i (\operatorname{diam}U_i)^s$ balances; the similarity dimension of *Fractal Geometry* is exactly this balance. When $s > 1$ the balance cannot be achieved by any Lipschitz parametrisation, and that is the obstruction to rectifiability stated in the previous section.

## Rectifiability and Dimension One

**Theorem (the two ends of the spectrum).** For a subset of a metric space the assertions assemble as follows:

**(a)** if $E$ is a rectifiable curve then $\dim_H E = 1$ and $0 < \mathcal{H}^1(E) < \infty$;

**(b)** if $E$ is self-similar with $m$ maps of ratio $r$ satisfying the open set condition then $\dim_H E = \log m/\log(1/r)$, which exceeds one exactly when $m > 1/r$.

The rectifiable curves are the sets of dimension one that are straight at every scale, on which the length and the one-dimensional content agree; the fractal curves are the sets of dimension strictly greater than one, on which there is no length at all. The middle of the spectrum — sets of dimension one with finite positive content that are not rectifiable — is non-empty and is exactly the class of the structure theorem: the sets of finite content without an approximate tangent almost everywhere, which are necessarily totally disconnected, the standard examples of Besicovitch.

**Theorem (the trichotomy of dimension one).** For a compact $E \subseteq \mathbb{R}^n$ of Hausdorff dimension one the alternatives are:

**(a)** $\mathcal{H}^1(E) \in (0,\infty)$ and $E$ has an approximate tangent line $\mathcal{H}^1$-almost everywhere: $E$ is countably rectifiable;

**(b)** $\mathcal{H}^1(E) \in (0,\infty)$ and $E$ fails to have an approximate tangent on a set of positive content: $E$ is purely unrectifiable, and then it is totally disconnected;

**(c)** $\mathcal{H}^1(E) = \infty$: the length diverges, as for the Koch curve.

**Proof sketch.** The alternatives are the structure theorem of the previous section together with the definition of rectifiability: (a) is countable rectifiability at finite content, (b) is the failure of the approximate tangent, and (c) is the divergence of the length. For a **connected** $E$ only (a) and (c) occur, because a continuum of finite content is a rectifiable curve by the theorem of Besicovitch; the middle class (b) is therefore necessarily totally disconnected. The distinction between (a) and (b) is invisible to the dimension, which is one in both cases, and it is detected by the tangent, which is the first-order data that the dimension omits.

## Summary

A curve in a metric space has a length, the supremum of the lengths of the inscribed polygons; it is rectifiable when the length is finite, and then it admits an arc-length parametrisation, which is $1$-Lipschitz with unit speed almost everywhere. Every rectifiable curve has Hausdorff dimension one and finite positive one-dimensional content, and it is countably rectifiable; conversely a set of finite content that has an approximate tangent line almost everywhere is rectifiable, and a connected set of finite content is a rectifiable curve. The Koch curve is the standard curve that is a curve topologically and not metrically: its $n$-th stage is a polygonal arc of length $(4/3)^n$ and its Hausdorff dimension is $\log 4/\log 3 = 1.2618\ldots$, and it has infinite length in every sub-arc. Snowflaking, the replacement of the distance $d$ by $d^\alpha$ with $0 < \alpha < 1$, multiplies the Hausdorff and box dimensions by $1/\alpha$ and is the standard construction of a non-rectifiable curve from a rectifiable one: the snowflaked interval of exponent $1/2$ is homeomorphic to an interval and has dimension two. Rectifiability is thus a metric property, invisible to the topology and detected by the approximate tangent; the measure-theoretic content of the structure theorem, the one-dimensional Hausdorff measure as a measure and the integral formula belong to *Geometric Measure Theory*, where the measure and the integral are available, and the covering-theoretic content used here is that of *Fractal Geometry*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\gamma$, $\ell(\gamma)$ | Curve, its length as a supremum over inscribed polygonal arcs |
| Rectifiable | Finite length; equivalently a Lipschitz reparametrisation exists |
| $s(t)$, $\tilde\gamma$ | Arc-length function; the arc-length parametrisation, of unit speed |
| $\mathcal{H}^1(E)$, $\mathcal{H}^s(E)$ | Cover-defined one- and $s$-dimensional content of *Fractal Geometry* |
| Approximate tangent line | Tangent up to an $\mathcal{H}^1$-null set in the limit of the blow-ups |
| Countably rectifiable | Contained up to an $\mathcal{H}^1$-null set in countably many Lipschitz images of $\mathbb{R}$ |
| $K$, $K_n$, $\log 4/\log 3$ | Koch curve; its $n$-th polygonal stage; its dimension $1.2618\ldots$ |
| $d^\alpha$, snowflake | The metric $d(x,y)^\alpha$, $0<\alpha<1$; $\dim_H$ multiplied by $1/\alpha$ |
| $1/\alpha$ | Dimension of the snowflaked interval of exponent $\alpha$ |

## Further Reading

- Kenneth Falconer, *The Geometry of Fractal Sets* (Cambridge University Press, 1986), for the length, the content and the Besicovitch structure of one-dimensional sets.
- Kenneth Falconer, *Fractal Geometry: Mathematical Foundations and Applications* (Wiley, 3rd edition, 2014), for the covering numbers, the Hausdorff content and the self-similar sets used here.
- Herbert Federer, *Geometric Measure Theory* (Springer, 1969), for the structure theorem, the approximate tangents and the area formula in the case $m=1$.
- Pertti Mattila, *Geometry of Sets and Measures in Euclidean Spaces* (Cambridge University Press, 1995), for the rectifiability of sets of finite content and the differentiation theory.
- Abram S. Besicovitch, "On the fundamental geometrical properties of linearly measurable plane sets of points", *Mathematische Annalen* 98 (1928), 295–329, for the structure of continua of finite length.
- Christopher J. Bishop and Yuval Peres, *Fractal Sets in Probability and Analysis* (Cambridge University Press, 2017), for the snowflaking and the snowflaked curves.
- John E. Hutchinson, "Fractals and self-similarity", *Indiana University Mathematics Journal* 30 (1981), 713–747, for the self-similar curves and the open set condition.
