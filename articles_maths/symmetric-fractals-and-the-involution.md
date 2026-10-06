# __Symmetric Fractals and the Involution__

## Introduction

A fractal is **symmetric** when it is invariant under an isometric involution of its ambient space: a map $\sigma$ with $\sigma^2 = \operatorname{id}$ and $d(\sigma x, \sigma y) = d(x,y)$ for which $\sigma(E) = E$. The simplest cases are the reflections of the line and of the plane, the point reflection and the antipodal map of the sphere; for each of them the space splits into the **fixed set** $\operatorname{Fix}\sigma = \{x : \sigma x = x\}$, an affine subspace, and the **exchanged pairs** $\{x, \sigma x\}$ with $x \notin \operatorname{Fix}\sigma$. A symmetric fractal carries this structure on itself: the fixed points $E^\sigma = E \cap \operatorname{Fix}\sigma$ form a closed subset, again a fractal in the examples; the pairs are exchanged; and the **quotient** $E/\sigma$, the set of the orbits, is a metric space whose geometry records the symmetry in the same way the half-interval records the symmetry of a segment.

This article is the geometric side of the involution. It defines the involution, the fixed set and the quotient; it states the theorems that the Hausdorff dimension is unchanged by the quotient and that the fixed set has dimension at most the dimension of $E$; it reads the three symmetric self-similar examples — the segment, the symmetric Cantor set and the symmetric gasket — with their tilings by the images of the contractions; and it compares the geometric involution with the **reversible** iterated function systems of *Fractal Analysis*, where the same involution appears as an algebraic symmetry of the maps. The operator side, the involution induced on the space of the compact sets and the symmetric attractor as its fixed point, is *The Involution on the Space of Compact Sets and the Symmetric Attractor*.

The article assumes *Metric Geometry* for the isometries, the affine subspaces and the Lipschitz maps; *Topological Spaces* for the quotient topology, the compactness and the connectedness; *Metric, Uniform and Complete Spaces* for the completeness and the contraction; *Fractal Geometry* for the iterated function systems, the self-similar sets and the dimension; and *Fractal Analysis*'s *Reversible Iterated Function Systems and the Involution* and *The Self-Similar Measure and the Involution* for the measure-theoretic reading, which is cited and not repeated. The group-theoretic face of the involution — the quasi-isometry and the boundary — is that of Part II. No physics is invoked.

## The Involution, the Fixed Set and the Exchanged Pairs

**Definition.** Let $(X,d)$ be a metric space. An **involution** is a map $\sigma : X \to X$ with $\sigma^2 = \operatorname{id}_X$; it is **isometric** when $d(\sigma x, \sigma y) = d(x,y)$ for all $x,y$. The **fixed set** is $\operatorname{Fix}\sigma = \{x : \sigma x = x\}$, and the **orbit** of a point is $\{x, \sigma x\}$, a singleton exactly on the fixed set.

**Theorem (the structure of an isometric involution).** Let $\sigma$ be an isometric involution of a complete geodesic metric space $X$.

**(a)** $\operatorname{Fix}\sigma$ is closed, and for $x \notin \operatorname{Fix}\sigma$ a geodesic from $x$ to $\sigma x$ meets $\operatorname{Fix}\sigma$ in its midpoint, which is a fixed point at the minimal distance from $x$.

**(b)** Every point of $X$ is at distance $d(x,\operatorname{Fix}\sigma) = \frac12 d(x,\sigma x)$ from the fixed set, and the nearest point is the midpoint of $x$ and $\sigma x$.

**(c)** The quotient map $q : X \to X/\sigma$, $q(x) = \{x,\sigma x\}$, is $1$-Lipschitz for the quotient metric $\bar d([x],[y]) = \min\{d(x,y), d(x,\sigma y)\}$, and it is an isometry on each component of $X \setminus \operatorname{Fix}\sigma$; for a reflection in a hyperplane of $\mathbb{R}^n$ the complement has two components and they are isometric.

**Proof sketch.** (a) the fixed set is closed as the zero set of the continuous $d(x,\sigma x)$, and the midpoint of a geodesic from $x$ to $\sigma x$ is fixed because $\sigma$ reverses the geodesic and its endpoints; the minimality is the triangle inequality in the form $d(x,z) + d(\sigma x,z) \geq d(x,\sigma x)$ for $z \in \operatorname{Fix}\sigma$, with equality at the midpoint. (b) is the same inequality. (c) the quotient metric is well defined because the orbits are finite, and the minimum is attained; the Lipschitz property is the definition, and for two points of the same component of $X\setminus\operatorname{Fix}\sigma$ the second alternative exceeds the first, since a geodesic from $x$ to $\sigma y$ meets $\operatorname{Fix}\sigma$ while $x$ and $y$ lie on the same side of it, so $q$ is an isometry on each component. The statements are those of *Metric Geometry*.

**Example (the three involutions).** The reflection of the line, $\sigma(x) = -x$ or $\sigma(x) = 1-x$, has a point as its fixed set. The reflection of the plane, $\sigma(x,y) = (1-x,y)$, has a line. The point reflection $\sigma(x) = -x$ of $\mathbb{R}^d$ has the origin, and the antipodal map of the sphere has the empty fixed set. The midpoint at the minimal distance is the geometric content of the statement that the involution folds the space onto the half-space.

## The Symmetric Fractal, Its Fixed Set and Its Quotient

**Definition.** A set $E$ is $\sigma$-**invariant** when $\sigma(E) = E$; the restriction is then an isometric involution of $E$, the **fixed fractal** is $E^\sigma = E \cap \operatorname{Fix}\sigma$, and the **quotient** is $E/\sigma$, the space of the orbits with the quotient metric.

**Theorem (the dimensions of the symmetric parts).** Let $E$ be a nonempty compact $\sigma$-invariant set.

**(a)** The quotient has the same Hausdorff dimension as the set: $\dim_H(E/\sigma) = \dim_H E$.

**(b)** The fixed set has dimension at most the dimension of the set: $\dim_H E^\sigma \leq \dim_H E$. Equality holds when the fixed part already carries the dimension of $E$ — in particular when $E \subseteq \operatorname{Fix}\sigma$, and also when $E$ is a fixed fractal of full dimension with finitely many exchanged points added.

**(c)** The upper box dimension does not increase under the quotient: $\overline{\dim}_B(E/\sigma) \leq \overline{\dim}_B E$.

**Proof sketch.** (a) the quotient map $q$ is $1$-Lipschitz and onto, so $\dim_H(E/\sigma) \leq \dim_H E$; conversely, the preimage of a ball of radius $r$ about an orbit is the union of the two balls of radius $r$ about its members, so a cover of $E/\sigma$ by balls of radius $r$ pulls back to a cover of $E$ by twice as many balls of radius $2r$, giving $\mathcal{H}^s(E) \leq 2^{s+1}\mathcal{H}^s(E/\sigma)$ and hence $\dim_H E \leq \dim_H(E/\sigma)$. (b) the fixed set is a subset. (c) the quotient map is Lipschitz. The statements are the metric form of the elementary fact that a finite isometric group action does not change the Hausdorff dimension of a set, and the equality cases of (b) show where the dimension can sit: a set contained in the fixed hyperplane is symmetric without any exchanged pair, and a fixed fractal of full dimension carries the dimension even when exchanged pairs are present.

**Remark (dimension versus measure).** The dimension is preserved by the quotient, but the **measure** need not be: a self-similar measure that is not invariant under the involution pushes forward to a measure on the quotient whose dimension can be smaller, and the symmetry of the measure is exactly the condition in *The Self-Similar Measure and the Involution* of *Fractal Analysis*. This is the reason the article separates the geometric involution, which preserves the dimension, from the measure-theoretic one, which does not.

**Example (the fixed fractals).** For the segment $[0,1]$ with $\sigma(x) = 1-x$ the fixed set is the single point $\{\frac12\}$, of dimension zero. For the middle-thirds Cantor set $C$ with $\sigma(x) = 1-x$ the fixed set is empty, because $\frac12 \notin C$; the involution exchanges the two halves $C \cap [0,\frac12]$ and $C\cap[\frac12,1]$, which are isometric, and the quotient is a Cantor set of dimension $\log2/\log3$. For the product $E = C\times C$ with $\sigma(x,y) = (1-x,y)$ the fixed set is $\{\frac12\}\times C$, a Cantor set of dimension $\log2/\log3$, again a fractal, and the quotient is isometric to the half $[0,\frac12]\times C$. These three show the range: a point, the empty set, and a copy of the fractal itself.

## The Symmetric Self-Similar Sets and Their Tilings

**Definition.** An iterated function system $f_1,\dots,f_N$ on $X$ is $\sigma$-**reversible** when $\sigma$ conjugates the maps to the system: there is an involutive permutation $\tau$ of $\{1,\dots,N\}$ with

$$
\sigma \circ f_i = f_{\tau(i)} \circ \sigma \qquad (i = 1,\dots,N) .
$$

**Theorem (the symmetry of the attractor).** If the system is $\sigma$-reversible then the Hutchinson operator commutes with the involution, $\sigma(F(A)) = F(\sigma(A))$, and the attractor is $\sigma$-invariant. The fixed set of the attractor is determined by the maps that preserve the fixed set and by the intersections of the pieces with the fixed set, and is computed from the restricted system in the examples.

**Proof sketch.** The commutation is the computation $\sigma(F(A)) = \bigcup_i \sigma(f_i(A)) = \bigcup_i f_{\tau(i)}(\sigma(A)) = F(\sigma(A))$, using that $\tau$ is a permutation; the invariance of $K$ follows from the uniqueness of the fixed point of $F$ applied to $\sigma(K)$. The fixed set is computed case by case: the pieces with $\tau(i) = i$ contribute their intersections with the fixed set, and the exchanged pairs contribute nothing to it directly. The operator form of the commutation, on the space of the compact sets, is the subject of *The Involution on the Space of Compact Sets and the Symmetric Attractor*.

**Example (the segment).** On $[0,1]$ the system $f_1(x) = \frac{x}{2}$, $f_2(x) = \frac{x}{2}+\frac12$ with $\sigma(x) = 1-x$ is reversible with $\tau$ transposing $1$ and $2$; the attractor is the whole segment, the fixed set is the single point $\{\frac12\}$, and the quotient is the half-segment $[0,\frac12]$, a fundamental domain. The two tiles $f_1([0,1]) = [0,\frac12]$ and $f_2([0,1]) = [\frac12,1]$ are exchanged, and the segment is tiled by the two.

**Example (the symmetric Cantor set).** On $[0,1]$ the system $f_1(x) = \frac{x}{3}$, $f_2(x) = \frac{x}{3}+\frac23$ with $\sigma(x) = 1-x$ is reversible with the same transposition, since $\sigma(f_1(x)) = 1-\frac x3 = \frac{1-x}{3}+\frac23 = f_2(\sigma(x))$. The attractor is the middle-thirds Cantor set, which is symmetric, the fixed set is empty because $\frac12$ lies in the removed middle third, and the quotient is the half $C\cap[0,\frac12]$, a Cantor set of the same dimension. The system is the standard example in which the involution has no fixed point and the quotient is nonetheless a fundamental domain; the **tiling** is the decomposition of $C$ into the two exchanged halves, each a scaled copy of $C$.

**Example (the symmetric gasket).** On the equilateral triangle with the vertices $v_1 = (0,0)$, $v_2 = (1,0)$, $v_3 = (\frac12,\frac{\sqrt3}{2})$ the system $f_i(x) = \frac{x+v_i}{2}$ with the reflection $\sigma$ in the vertical axis is reversible, transposing $f_1$ and $f_2$ and fixing $f_3$. The attractor is the Sierpiński gasket of dimension $\log3/\log2$, the fixed set is the intersection with the axis, and that intersection is **countable**: it is the orbit of the midpoint $(\frac12,0)$ of the base under the contraction $f_3$, namely the points $(\frac12, \frac{\sqrt3}{2}(1-2^{-k}))$ for $k \geq 0$ together with the apex, so its Hausdorff dimension is zero. The example is the sharp case of the theorem: the fixed set is a fractal in the topological sense — a closed countable set — and its dimension is strictly smaller than the dimension of the gasket, so the symmetry is almost entirely in the exchanged pairs.

**Remark (the tilings).** In each of the examples the attractor is the union of the tiles $f_i(K)$, and the involution pairs the tiles: the tiles are exchanged by $\tau$, and the tiles with $\tau(i) = i$ are fixed. The self-similar **tiling** of the set is the decomposition of $K$ into the $\tau$-orbits of the tiles, and the quotient $K/\sigma$ is tiled by one tile from each exchanged pair together with the fixed tiles. This is the geometric content of reversibility, and it is the structure that the reversible systems of *Fractal Analysis* use in the construction of the self-similar measures invariant under the involution.

## The Comparison with the Reversible Systems

**Remark (the geometric and the algebraic involution).** The involution of this article is a map of the space, and the symmetry it detects is a property of the **set**; the reversible iterated function system of *Fractal Analysis* is the same data read as a property of the **maps**, the relation $\sigma \circ f_i = f_{\tau(i)}\circ\sigma$, together with the invariant measure it forces. The two are linked by the theorem above: the reversibility of the system makes the attractor symmetric, and the symmetry of the attractor is the geometric face of the relation. The corpus keeps the two distinct: a $*$ group is the involutive form of the plain group, the involution is on the object, the adjoint is on the operator, and the dagger is reserved for the adjoint of an operator. The measure-theoretic companion, the self-similar measure invariant under the involution and the dimension of its quotient, is *The Self-Similar Measure and the Involution*.

**Remark (the involution and the boundary of a group).** The involution also acts on the boundary of a hyperbolic group when the group carries an involutive automorphism induced by an isometry of the Cayley graph with a fixed vertex; the boundary involution is an isometry of the visual metric and the fixed set of the boundary is a fractal. This is the group-theoretic face of the same construction, and it belongs to Part II and to *The Dimension of the Boundary of a Hyperbolic Group*.

## Summary

An isometric involution of a metric space has a closed fixed set, folds the space onto a half, and gives a quotient on which the quotient map is an isometry on each half. A $\sigma$-invariant compact set has a quotient of the same Hausdorff dimension as the set, a fixed set of dimension at most that of the set with equality only when the set is contained in the fixed set, and a box dimension not increased by the quotient. The symmetric self-similar sets are generated by the $\sigma$-reversible systems, for which the Hutchinson operator commutes with the involution and the attractor is symmetric; the segment has the point $\{\frac12\}$ as its fixed set, the middle-thirds Cantor set has the empty fixed set and a half-Cantor quotient, and the symmetric Sierpiński gasket has a countable, zero-dimensional fixed set and its symmetry carried by the exchanged pairs. The tiling of a symmetric self-similar set is the decomposition of its tiles into the orbits of the transposition. The reversible systems and the invariant measure are *Fractal Analysis*'s, the operator form of the involution on the compact sets is *The Involution on the Space of Compact Sets and the Symmetric Attractor*, the iterated function systems and the dimension are *Fractal Geometry*'s, and the isometries and the quotients are those of *Metric Geometry* and *Topological Spaces*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma$ | Isometric involution, $\sigma^2=\operatorname{id}$ |
| $\operatorname{Fix}\sigma$, $E^\sigma$ | Fixed set of $\sigma$; the fixed fractal $E\cap\operatorname{Fix}\sigma$ |
| $\{x,\sigma x\}$ | Orbit, a singleton on the fixed set and a pair otherwise |
| $q$, $\bar d$, $E/\sigma$ | Quotient map; quotient metric; quotient space of the orbits |
| $\dim_H(E/\sigma)=\dim_H E$ | The quotient preserves the Hausdorff dimension |
| $\tau$ | Involutive permutation of the maps with $\sigma\circ f_i=f_{\tau(i)}\circ\sigma$ |
| $f_i(K)$, exchanged tiles | The tiles of the attractor; the pairs under $\tau$ |
| $\{\frac12\}$, $\varnothing$, countable | Fixed sets of the segment, the Cantor set, the gasket |

## Further Reading

- John E. Hutchinson, "Fractals and self-similarity", *Indiana University Mathematics Journal* 30 (1981), 713–747, for the iterated function systems, the attractor, the invariant measure and the reversible structure.
- Michael F. Barnsley, *Fractals Everywhere* (Academic Press, 2nd edition, 1993), for the self-similar sets, their tilings by the images of the contractions and the symmetries of the attractor.
- Kenneth Falconer, *Fractal Geometry: Mathematical Foundations and Applications* (Wiley, 3rd edition, 2014), for the self-similar sets, the open set condition and the dimension.
- Christoph Bandt, "Self-similar sets 5: integer matrices and fractal tilings of $\mathbb{R}^n$", *Proceedings of the American Mathematical Society* 112 (1991), 549–562, for the self-similar tilings and the symmetry of the tiles.
