# __Iterated Function Systems on the Real Line__

## Introduction

An **iterated function system** on the real line is a finite family of contractions $f_1,\dots,f_m$ of $\mathbb{R}$; it is read in three ways at once. As a recipe it builds a compact set by applying the maps to the pieces over and over; as an operator on the nonempty compact subsets it has a unique fixed point, the attractor, obtained from any starting set in the Hausdorff metric; and as a coding device it carries the shift space $\{1,\dots,m\}^{\mathbb{N}}$ onto that attractor, the address of a point being the sequence of maps that reaches it. This article develops the three readings for the line, states the open set condition in its one-dimensional form, introduces the similarity dimension solving $\sum_i r_i^s = 1$, works the address map and the identifications it makes when the pieces touch, and collects the standard examples as systems. The general theory — the Hutchinson operator on the compact subsets of a complete metric space, the open set condition, and the Moran–Hutchinson theorem — is the subject of the lead article *Fractal Geometry* of Part IV, and the measures carried by the attractors are those of the category `## Fractal Analysis` of Part III; both are cited and neither is restated.

The material of the first article of this subcategory, *Self-Similar Subsets of the Real Line*, is used throughout: the contractions of the line, the middle-third set and its levels, the digit coding and the binary tree. The distance, the diameter, the Hausdorff metric and the contraction mapping theorem are those of *Metric, Uniform and Complete Spaces*; the shift and its coding of the dynamics are those of *Symbolic Dynamics*; and the comparison of the limit set with the limit sets of the maps of Part III is deferred to those articles. What is developed here is the one-dimensional operator, its fixed point, its addresses and its examples.

Throughout, a **contraction** of the line is a map $f:\mathbb{R}\to\mathbb{R}$ with $d(f(x),f(y)) = r\,d(x,y)$ for some $r\in(0,1)$ and all $x,y$, so that a contraction is a similarity of ratio $r<1$; the maps are $f_1,\dots,f_m$ with ratios $r_1,\dots,r_m$, the alphabet is $\{1,\dots,m\}$, a **word** is a finite sequence $w=i_1\cdots i_k$, its length is $\lvert w\rvert = k$, the **cylinder** of $w$ is the map $f_w = f_{i_1}\circ\cdots\circ f_{i_k}$, and a **one-sided infinite word** is $\omega = (\omega_1,\omega_2,\dots) \in \{1,\dots,m\}^{\mathbb{N}}$.

## The Space of Compact Subsets

**Definition.** Let $\mathcal{K}(\mathbb{R})$ be the set of nonempty compact subsets of $\mathbb{R}$. For $A,B \in \mathcal{K}(\mathbb{R})$ the **Hausdorff distance** is

$$
d_H(A,B) = \max\Bigl\{\sup_{a\in A}\inf_{b\in B}d(a,b),\ \sup_{b\in B}\inf_{a\in A}d(a,b)\Bigr\}.
$$

**Theorem.** $(\mathcal{K}(\mathbb{R}), d_H)$ is a complete metric space, and the diameter is finite on it; a sequence converges in $d_H$ exactly when it converges in the sense that every point of the limit is a limit of points of the sequence and every convergent sequence of points of the sets converges into the limit.

*Proof.* The Hausdorff distance is a metric: the triangle inequality for $d_H$ is the triangle inequality for the two one-sided distances, and the other axioms are immediate. Completeness is the completeness of $\mathbb{R}$ upgraded to the hyperspace: a Cauchy sequence has the property that the sets eventually lie in a common bounded interval, and the set of limits of all sequences drawn from the sets is compact and is the limit. $\square$

**Definition.** Let $f_1,\dots,f_m$ be contractions with ratios $r_i<1$. The **Hutchinson operator** is

$$
F : \mathcal{K}(\mathbb{R}) \to \mathcal{K}(\mathbb{R}), \qquad F(S) = \bigcup_{i=1}^m f_i(S).
$$

**Theorem (the operator is a contraction).** If $r = \max_i r_i < 1$ then $d_H(F(S),F(S')) \leq r\,d_H(S,S')$ for all $S,S' \in \mathcal{K}(\mathbb{R})$. Consequently $F$ has a unique fixed point $\Lambda \in \mathcal{K}(\mathbb{R})$, the **attractor** of the system, and $\Lambda = \lim_{k\to\infty}F^k(S)$ in $d_H$ for every $S\in\mathcal{K}(\mathbb{R})$; moreover

$$
\Lambda = \bigcap_{k\geq0}\ \overline{\bigcup_{\lvert w\rvert = k} f_w(S_0)}, \qquad S_0 \ \text{a nonempty compact set,}
$$

and $\Lambda$ is the unique nonempty compact set with $\Lambda = \bigcup_i f_i(\Lambda)$.

*Proof.* For $S,S'$ one has $f_i(S) \subseteq f_i(S')$ thickened by $r_i d_H(S,S')$, and summing over $i$ gives $d_H(F(S),F(S')) \leq \max_i r_i\, d_H(S,S')$; this is the contraction estimate. The contraction mapping theorem of *Metric, Uniform and Complete Spaces*, applied on the complete space $\mathcal{K}(\mathbb{R})$, gives the unique fixed point and the convergence of the iterates; the displayed intersection is the standard description of the limit, and the last sentence restates the fixed-point property in the form used in the first article. $\square$

**Remark.** The theorem is the one-dimensional instance of the attractor theorem of *Fractal Geometry*, which states it for a complete metric space; no generality is added here. The reader who wants the theorem in that generality, with the Hausdorff metric on the hyperspace of a complete metric space, is referred to the lead article.

## The Open Set Condition on the Line

**Definition.** The system $f_1,\dots,f_m$ satisfies the **open set condition** if there is a nonempty bounded open set $V \subseteq \mathbb{R}$ with

$$
\bigcup_{i=1}^m f_i(V) \subseteq V \qquad\text{and}\qquad f_i(V)\cap f_j(V) = \varnothing \ \ (i\neq j).
$$

**Theorem (the one-dimensional form).** For contractions of the line the open set condition holds with some open interval $V=(a,b)$ if and only if there is an open interval $I$ with $f_i(I) \subseteq I$ for every $i$ and the intervals $f_1(I),\dots,f_m(I)$ pairwise disjoint. If the ratios are placed consecutively inside $I$, this holds exactly when $\sum_i r_i\leq1$; in particular for equal ratios it is $mr\leq1$, and for $m=2$ it is $r_1+r_2\leq1$.

*Proof.* An open set of the line is a disjoint union of open intervals, and the images under a similarity of the component containing the attractor give the interval $I$; conversely $I$ is an open set. The pieces $f_i(I)$ are intervals of length $r_i\lvert I\rvert$ placed inside $I$, and pairwise disjointness forces the total length $\sum_ir_i\lvert I\rvert$ to be at most $\lvert I\rvert$, which is $\sum_ir_i\leq1$; when the pieces are consecutive and the sum is at most $1$ they can be placed disjointly, and for equal ratios the condition reads $mr\leq1$. $\square$

**Definition.** For ratios $r_1,\dots,r_m$ the **similarity dimension** is the unique $s\geq0$ with

$$
\sum_{i=1}^m r_i^{\,s} = 1 .
$$

The left side is strictly decreasing in $s$, from $m>1$ at $s=0$ to $0$ as $s\to\infty$, so $s$ exists, is unique and is positive; when $r_i = r$ for all $i$ it is $s = \log m/\log(1/r)$.

**Theorem (Moran–Hutchinson, quoted).** If the system satisfies the open set condition, the attractor has

$$
\dim_H\Lambda = \dim_B\Lambda = s, \qquad \sum_{i=1}^m r_i^{\,s} = 1,
$$

and $0 < \mathcal{H}^s(\Lambda) < \infty$. The theorem is that of *Fractal Geometry*; it is stated here only to fix the dimension of the one-dimensional examples.

**Remark (the failure without separation).** The open set condition is not necessary for the existence of the attractor, only for the dimension formula. When the images overlap the attractor can be a set of dimension larger than, equal to, or smaller than the similarity dimension, and the last case is the interesting one; the example is given below. The phenomenon of overlapping self-similar sets, and the exact dimension in the presence of overlaps, is the subject of the general theory of *Fractal Geometry* and of its references.

## The Address Map

**Definition.** On the shift space $\Sigma = \{1,\dots,m\}^{\mathbb{N}}$ put, with $r=\max_ir_i$, the **ultrametric**

$$
d_\Sigma(\omega,\tau) = r^{\,k}, \qquad k = \min\{n : \omega_n \neq \tau_n\},
$$

with $d_\Sigma(\omega,\omega)=0$; the space $\Sigma$ is compact, perfect and totally disconnected, hence a Cantor space, and it is the boundary of the rooted tree of the finite words on the alphabet $\{1,\dots,m\}$, exactly as in the first article for the binary alphabet. Its Hausdorff dimension is $\dim_H\Sigma = \log m/\log(1/r)$, because the level-$k$ cylinders all have diameter $r^k$ and there are $m^k$ of them.

**Theorem (the address map).** For a system of contractions with $r=\max_i r_i$, there is a unique map

$$
\pi : \Sigma \to \Lambda, \qquad \pi(\omega) = \lim_{k\to\infty} f_{\omega_1}\circ\cdots\circ f_{\omega_k}(x_0),
$$

the limit being independent of the base point $x_0$; the map $\pi$ is Lipschitz with the metric $d_\Sigma$ and satisfies $d(\pi(\omega),\pi(\tau)) \leq \operatorname{diam}(\Lambda)\,r^{\,k}$ with $k$ the length of the longest common prefix, so by the Hölder invariance of *Fractal Geometry* it does not increase the dimension, $\dim_H\Lambda \leq \log m/\log(1/r)$. The map $\pi$ is surjective onto $\Lambda$, and it is injective if and only if the pieces $f_1(\Lambda),\dots,f_m(\Lambda)$ are pairwise disjoint; under the **strong separation condition** below it is a homeomorphism.

*Proof.* The sequence $f_{\omega_1}\cdots f_{\omega_k}(x_0)$ is Cauchy with $d \leq r^k\operatorname{diam}\Lambda$, since two terms with the same $k$-th prefix differ by $r^k$ times the diameter of the base set; the limit exists by completeness and depends on $\omega$ alone, because changing the base point changes the limit by at most $r^k\operatorname{diam}\Lambda$. The Lipschitz estimate is the same computation: points of $\Sigma$ agreeing on the first $k$ digits have images within $r^k\operatorname{diam}\Lambda$. Surjectivity follows because an attractor point is $\pi(\omega)$ for the digits $\omega_n$ that select the level-$n$ piece containing it, and the bound $\dim_H\Lambda\leq\log m/\log(1/r)$ is the Hölder invariance with exponent $1$. If two pieces $f_i(\Lambda)$, $f_j(\Lambda)$ meet, a point of the intersection has the two addresses $i\omega$ and $j\tau$, so $\pi$ is not injective; conversely if the pieces are pairwise disjoint, the cylinder $f_i(\Lambda)$ and its complement separate the addresses, and induction on the level gives injectivity. A continuous bijection from the compact $\Sigma$ onto the Hausdorff space $\Lambda$ is a homeomorphism. $\square$

**Definition.** The system satisfies the **strong separation condition** if the pieces $f_1(\Lambda),\dots,f_m(\Lambda)$ are pairwise disjoint, equivalently if $\pi$ is injective. The strong separation condition implies the open set condition but is not implied by it.

**Example (the identification at a touch).** For the two-halves system $f_1(x)=x/2$, $f_2(x)=x/2+1/2$, the attractor is $\Lambda=[0,1]$, the open set condition holds with $V=(0,1)$, and the pieces $f_1(\Lambda)=[0,\tfrac12]$, $f_2(\Lambda)=[\tfrac12,1]$ meet at the single point $1/2$. The address map is therefore not injective: the dyadic rationals $k/2^n$ have exactly two addresses, for instance

$$
\frac12 = \pi(1,2,2,2,\dots) = \pi(2,1,1,1,\dots),
$$

the first because $1/2=f_1(1)$ and $1=\pi(2,2,2,\dots)$, the second because $1/2=f_2(0)$ and $0=\pi(1,1,1,\dots)$. The set of points with two addresses is the countable set of dyadic rationals, and $\pi$ is the identity after this identification: $\Lambda=[0,1]$ with the binary expansion read off the addresses.

**Theorem (countability of the ambiguities).** If the system satisfies the open set condition and the pieces are intervals, then the set of points of $\Lambda$ with more than one address is countable, and each point has at most two addresses.

*Proof.* The level-$n$ pieces are $m^n$ closed intervals whose interiors are pairwise disjoint under the open set condition. Call two level-$n$ pieces **adjacent** when they meet; their intersection is then a single point, a shared endpoint. A point with two addresses $\omega\neq\tau$ agrees with both until the first place $n$ where they differ and then lies in the intersection of two adjacent level-$n$ pieces; conversely a point of the intersection of two adjacent level-$n$ pieces carries the two addresses read along the two pieces. For each $n$ the number of adjacent pairs of level-$n$ pieces is finite, so the set of points with more than one address is a countable union of finite sets, hence countable. At a point of a Cantor-type attractor at most two intervals can meet, since three would force two of them to lie on the same side of the point and to have overlapping interiors; hence at most two addresses. $\square$

## The Examples as Systems

**Example (the two halves, and the interval).** $f_1(x) = x/2$, $f_2(x) = x/2 + 1/2$: two contractions of ratio $1/2$, open set condition with $V=(0,1)$, similarity dimension $s=1$, attractor $[0,1]$, and the dyadic identifications of the previous section. The system is the model of the interval as a self-similar set and of the address map that identifies the two expansions of a dyadic rational.

**Example (the middle-third set).** $f_1(x)=x/3$, $f_2(x)=x/3+2/3$: the attractor is the middle-third Cantor set of the first article, of digits $\{0,2\}$ and dimension $\log2/\log3$, with the strong separation condition holding because the pieces $[0,1/3]$ and $[2/3,1]$ are disjoint; the address map is the homeomorphism of the digit coding.

**Example (three thirds, and the interval).** $f_1(x)=x/3$, $f_2(x)=x/3+1/3$, $f_3(x)=x/3+2/3$: three contractions of ratio $1/3$, open set condition with $V=(0,1)$, similarity dimension $s=1$, attractor $[0,1]$. The pieces are consecutive and touch, and the address map is the ternary expansion; the multivalued points are the ternary rationals with two expansions.

**Example (an overlap that lowers the dimension).** $f_1(x)=x/2$, $f_2(x)=x/2+1/4$, $f_3(x)=x/2+1/2$: three contractions of ratio $1/2$, whose pieces $[0,\tfrac12]$, $[\tfrac14,\tfrac34]$, $[\tfrac12,1]$ overlap, so the open set condition fails. The similarity dimension solves $3\cdot2^{-s}=1$, namely $s=\log3/\log2 = 1.5849\ldots$, but the attractor is the interval $[0,1]$, of dimension $1$: the set $[0,1]$ is compact and invariant, and by uniqueness it is the attractor. The similarity dimension therefore overestimates the dimension when the pieces overlap, and the exact dimension of an overlapping self-similar set is a delicate question of the general theory.

**Example (the $1/4$-Cantor system).** $f_1(x)=x/2$, $f_2(x)=x/4+3/4$: the unequal-ratio system of the first article, with similarity dimension $s=\log\varphi/\log2=0.6942\ldots$; the strong separation condition holds, so the address map is a homeomorphism and the dimension formula applies.

**Example (a system with a reflection).** $f_1(x) = x/3$, $f_2(x) = 1 - x/3$: the second map is orientation-reversing, of ratio $1/3$ and fixed point $3/4$. Since $f_2=\sigma\circ f_1$ with the reflection $\sigma(x)=1-x$, the attractor satisfies $\sigma(\Lambda)=\Lambda$ and is symmetric about $1/2$. The pieces $f_1(\Lambda)\subseteq[0,\tfrac13]$ and $f_2(\Lambda)\subseteq[\tfrac23,1]$ are disjoint, so the strong separation condition holds and the address map is a homeomorphism; the construction is the one-dimensional model of the reversible systems of Part III.

## The Limit Set and the Shift

**Theorem (the coding of the dynamics).** For every $\omega\in\Sigma$ the address map satisfies

$$
\pi(\omega) = f_{\omega_1}\bigl(\pi(\sigma\omega)\bigr),
$$

so the shift sends an address of a point to an address of the point of $\Lambda$ that $f_{\omega_1}$ carries to it; equivalently, on the piece $f_{\omega_1}(\Lambda)$ the inverse branch of $f_{\omega_1}$ is the map $\pi\circ\sigma\circ\pi^{-1}$ wherever $\pi^{-1}$ is single-valued. The topological entropy of the full shift is $\log m$, the number of words of length $n$ being $m^n$.

*Proof.* The identity is the definition of the address map read one step at a time: the address $\omega$ names the first piece $f_{\omega_1}$ and then the address $\sigma\omega$ inside it. The entropy of the full $m$-shift is $\log m$ by the standard count of the words of length $n$. The entropy of the attractor as a repeller and the identification of $\Lambda$ with the limit set of the inverse branches are the subject of *Symbolic Dynamics* and of Part III. $\square$

**Remark.** The attractor is the repeller of the map that is the inverse of the branches on the pieces; the reading of a self-similar set as the limit set of a map, its coding by the shift and the computation of its local dimension, is the dynamical part of the theory and is deferred to Part III. The one-dimensional material developed here is the concrete model on which the general theory of *Fractal Geometry* is read.

## Summary

An iterated function system on the line is a finite family of contractions $f_1,\dots,f_m$ of ratios $r_i<1$. On the nonempty compact subsets with the Hausdorff metric the Hutchinson operator $F(S)=\bigcup_if_i(S)$ is a contraction of ratio $\max_ir_i$, so it has a unique fixed point, the attractor $\Lambda$, which is the limit of the iterates of any compact set and the unique nonempty compact set with $\Lambda=\bigcup_if_i(\Lambda)$. The open set condition holds with an interval $V$ exactly when the pieces can be placed disjointly inside an interval, and for equal ratios this is $mr\leq1$; under it the attractor has Hausdorff and box dimension equal to the similarity dimension solving $\sum_ir_i^s=1$, by the Moran–Hutchinson theorem of *Fractal Geometry*. The address map carries the shift space onto the attractor, is Hölder with the ratio of the system, is surjective always, and is a homeomorphism exactly when the pieces are pairwise disjoint; the identifications occur at the points where the pieces touch, and they are countable under the open set condition.

The examples are the interval, the middle-third set, the unequal-ratio set and the systems with touching or overlapping pieces; an overlap can lower the dimension below the similarity dimension, the three-halves system of ratio $1/2$ having similarity dimension $\log3/\log2$ and attractor $[0,1]$ of dimension $1$. The dynamics of the attractor is coded by the shift, of entropy $\log m$, and the whole development is the one-dimensional instance of *Fractal Geometry*; the real quadratic family and its bifurcations are the subject of *The Real Quadratic Family and Its Bifurcations*, and the self-similar measures are the subject of `## Fractal Analysis` of Part III.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $f_1,\dots,f_m$, $r_i$ | The contractions and their ratios |
| $\mathcal{K}(\mathbb{R})$, $d_H$ | Nonempty compact subsets; the Hausdorff metric |
| $F(S)=\bigcup_if_i(S)$ | The Hutchinson operator; its contraction ratio $\max_ir_i$ |
| $\Lambda$, $f_w$ | The attractor; the piece of a finite word $w$ |
| Open set condition | Disjoint images $f_i(V)\subseteq V$ of an open set $V$ |
| $\sum_i r_i^s=1$, $s$ | The similarity dimension |
| $\Sigma$, $\pi$, $d_\Sigma$ | The shift space, the address map, its ultrametric |
| Strong separation | The pieces $f_i(\Lambda)$ pairwise disjoint; $\pi$ a homeomorphism |
| $\sigma$ | The one-sided shift on $\Sigma$ |
| Moran–Hutchinson | $\dim_H\Lambda=\dim_B\Lambda=s$ under the open set condition (quoted) |

## Further Reading

- John E. Hutchinson, "Fractals and self-similarity", *Indiana University Mathematics Journal* **30** (1981), 713–747, for the Hutchinson operator, the attractor and the open set condition.
- Michael F. Barnsley, *Fractals Everywhere*, 2nd edition (Academic Press, 1993), for the iterated function systems, the address map and the examples.
- Patrizia A. P. Moran, "Additive functions of intervals and Hausdorff measure", *Mathematical Proceedings of the Cambridge Philosophical Society* **42** (1946), 15–23, for the similarity dimension of a separated self-similar set.
- Kenneth Falconer, *Fractal Geometry: Mathematical Foundations and Applications*, 3rd edition (Wiley, 2014), for the open set condition, the overlaps problem and the examples.
- Kenneth Falconer, *Techniques in Fractal Geometry* (Wiley, 1997), for the Hausdorff metric on the hyperspace and the dimension of self-similar sets.
