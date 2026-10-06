# __Fractal Trees and Dendrites__

## Introduction

A **continuum** is a compact connected metric space, and a **dendrite** is a continuum that is locally connected and contains no simple closed curve. The second condition says that the space has no cycles; the first says that it is not pathologically broken, and together they give the topological form of a tree: in a dendrite any two points are joined by a unique arc. The end compactification of a locally finite tree is a dendrite, the branch points being the vertices and the ends being a closed subset of the Cantor set; the Julia set of $z \mapsto z^2 + i$ is a dendrite; and the limit space of the Fabrykowski–Gupta group is a dendrite, which is why the dendrite is the topological shape that the self-similar groups of *Limit Spaces and Schreier Graphs* produce.

The dendrite separates the two notions of dimension completely. Its **topological dimension** is always one: a dendrite is a one-dimensional Peano continuum, whatever its metric, because the local structure is a finite tree at every point. Its **Hausdorff dimension** is a metric invariant of the particular embedding, and it can be strictly greater than one: the dendrite Julia sets have Hausdorff dimension strictly greater than one, and the dimension of any dendrite can be increased without bound by snowflaking the metric, as in *Rectifiability and the Geometry of Fractal Curves*. The dendrite is therefore the simplest space in which the fractal property is not a property of the shape: the same dendrite, with two metrics, has two different Hausdorff dimensions and one topological dimension.

This article defines the continua, the cut points, the local cut points, the branch points and the ends, characterises the dendrites by the uniqueness of the arc and by the connectedness of the intersection of two subcontinua, proves that the topological dimension is one and that the end space is totally disconnected, computes the end compactification of the regular tree and its end space, and states the occurrence of dendrites as the tree-like Julia sets and as the limit spaces of self-similar groups. The **end space and its Cantor structure** are the objects that connect the dendrites to the boundaries of *The Dimension of the Boundary of a Hyperbolic Group*, and the metric tree of *Metric Geometry* is the metric counterpart of the dendrite here.

The article assumes *Metric, Uniform and Complete Spaces* for compactness, completeness, the diameter and the Hausdorff distance; *Topological Spaces* for connectedness, local connectedness, continua, the arc and the simple closed curve, and the Cantor set; *Dimension Theory*, written in parallel, for the covering dimension, which is quoted and not re-derived; *Metric Geometry* for the real tree and the four-point condition; and *Fractal Geometry* for the covering numbers and the Hausdorff dimension. The construction of the limit space of a self-similar group and the Schreier graphs attached to it are the subject of *Limit Spaces and Schreier Graphs*, and they are cited and not repeated; the Hausdorff dimension of the end space is the subject of *The Dimension of the Boundary of a Hyperbolic Group*. No physics is invoked.

## Continua and Dendrites

**Definition.** A **continuum** is a compact connected metric space. A point $p$ of a continuum $X$ is a **cut point** when $X \setminus \{p\}$ is disconnected, a **local cut point** when $p$ is a cut point of some connected neighbourhood of $p$, and an **end** (an end point) when $X \setminus \{p\}$ is connected, which for a dendrite means that $p$ has order one. The **order** of a point $p$ is the number of components of $X \setminus \{p\}$ when this number is finite, and a **branch point** is a point of order at least three. An **arc** is a homeomorphic copy of $[0,1]$, and a **simple closed curve** is a homeomorphic copy of the circle.

**Definition (dendrite).** A **dendrite** is a locally connected continuum containing no simple closed curve.

**Theorem (characterisations of a dendrite).** For a continuum $X$ the following are equivalent:

**(a)** $X$ is a dendrite;

**(b)** any two points of $X$ are joined by a unique arc;

**(c)** the intersection of any two subcontinua of $X$ is connected;

**(d)** $X$ is a Peano continuum and $\dim_{top} X = 1$ with no simple closed curve.

**Proof sketch.** (a)$\Rightarrow$(b): a Peano continuum is arcwise connected, so two points are joined by an arc; a second arc joining them would with the first contain a simple closed curve, which is excluded. (b)$\Rightarrow$(c): if two subcontinua met in a disconnected set, choosing points in two different components and joining them within each subcontinuum would produce a circle. (c)$\Rightarrow$(a): the failure of local connectedness produces a small circle, and the local connectedness follows from the "connected intersection" property applied to a nested sequence of neighbourhoods; the absence of circles is (b) again. (d) is the theorem of Whyburn that a one-dimensional Peano continuum with no circle is a dendrite, and conversely. The characterisation (b) is the one used below.

**Example (the arc and the end compactification of a tree).** An interval is a dendrite, being a locally connected continuum with no circle; its interior points have order two and its endpoints have order one. The end compactification of a locally finite tree, defined below, is a dendrite whose branch points are the vertices of order at least three and whose ends are the points of the end space. A dendrite can therefore be as simple as an arc and as complicated as a Cantor set of rays; the topology admits both, and the metric decides the dimension.

## The Structure of a Dendrite

**Theorem (the topological dimension).** Every dendrite is a one-dimensional Peano continuum, $\dim_{top} X = 1$, and it is a continuous image of the interval; it is homeomorphic to the interval exactly when it is an arc.

**Proof sketch.** A locally connected continuum is a Peano continuum, and every Peano continuum is a continuous image of the interval by the theorem of Hahn and Mazurkiewicz; the uniqueness of the arc of the characterisation above then singles out the arc among them. The covering dimension is one because the small connected neighbourhoods of a point of a dendrite are finite trees, of covering dimension one, and the countable sum theorem of *Dimension Theory* bounds the dimension of a compact space covered by one-dimensional closed pieces whose intersections have dimension zero. The characterisation of the arc is the theorem of Hausdorff that a continuum in which every point is of order at most two and which has two endpoints is an arc.

**Theorem (the ends and the branch points).** In a dendrite $X$:

**(a)** a point of order two lies in the interior of a maximal arc, the **free arc**, whose interior points are all of order two, and two different free arcs meet in at most one point;

**(b)** the **end space** $E(X)$, the set of the ends with the topology induced by $X$, is compact, totally disconnected and hence of topological dimension zero;

**(c)** if $X$ is the end compactification of a locally finite tree then $E(X)$ is a closed subspace of the Cantor set, and it is the whole Cantor set for the regular tree.

**Proof sketch.** (a) is the classical decomposition theorem of continua: the points of order two form the interiors of the maximal arcs, and a branching point is the only place where two free arcs can meet, so two free arcs meet in at most one point (Whyburn). (b) the ends form a closed subset of the compactum $X$, and the components of $X \setminus F$ for finite $F$ shrink to points, so distinct ends are separated by a clopen set and $E(X)$ is totally disconnected. (c) for the regular tree the end space is a self-similar Cantor set, computed below.

**Remark (why the ends are the boundary).** For a dendrite that is the end compactification of a tree, the end space is exactly the boundary at infinity of the tree in the sense of *Metric Geometry* and of *Hyperbolic Groups*: a ray of the tree converges to its end. The dendrite is thus the compactification of the tree by its ends, and the metric on the ends inherited from the tree is the visual metric. This is the bridge between the continuum theory of dendrites and the geometric group theory of *Limit Spaces and Schreier Graphs*.

## Trees and Their End Compactifications

**Definition (the regular tree and its end compactification).** Let $T_r$ be the rooted tree in which each vertex at depth $n \geq 1$ has $r-1$ children and the root has $r$ children, with all edges of length one. A **ray** is an infinite path from the root without backtracking, an **end** is an equivalence class of rays that eventually agree, and the **end compactification** $\overline{T_r} = T_r \cup E(T_r)$ carries the topology in which a sequence of vertices converges to an end when the rays through the vertices converge to it.

**Theorem (the end compactification is a dendrite).** For $r \geq 2$ the space $\overline{T_r}$ is a dendrite: it is compact, connected, locally connected and contains no simple closed curve. Its branch points are exactly the vertices of order at least three, and they are countable; its ends are the points of $E(T_r)$, which is a Cantor set for $r \geq 3$ and a single point for $r = 2$.

**Proof sketch.** Compactness: a sequence of vertices leaves every finite subtree in a ray, and every subsequence has a limit in $E(T_r)$, which is closed. Connectedness: any two points are joined by a finite path or a ray, and a vertex and an end are joined by the ray to the end. Local connectedness: the ball of radius $2^{-n}$ around a vertex is a finite tree with the ends attached along its boundary leaves, a contractible and locally connected neighbourhood. No simple closed curve: the space is a tree together with the ends, and a circle would give two distinct arcs between two points, contradicting the uniqueness of the path in the tree. The branch points are the vertices with at least three neighbours, the ends of the tree being of order one.

**Theorem (the end space and its dimension).** The end space $E(T_r)$ is a Cantor set for $r \geq 3$. With the visual metric $d(\xi,\eta) = r^{\,-\ell(\xi,\eta)}$, where $\ell(\xi,\eta)$ is the length of the common initial path of two rays, the number of cylinders of diameter $r^{-n}$ is

$$
N\bigl(E(T_r), r^{-n}\bigr) \asymp (r-1)^{n} ,
$$

so

$$
\dim_H E(T_r) = \frac{\log(r-1)}{\log r} .
$$

For $r = 3$ this is $\log 2/\log 3 = 0.6309\ldots$; for $r = 4$ it is $\log 3/\log 4 = 0.7924\ldots$. Since the dimension is less than one, the dendrite $\overline{T_r}$ itself has

$$
\dim_H \overline{T_r} = 1 ,
$$

being a countable union of arcs together with an end set of dimension strictly less than one.

**Proof sketch.** The cylinders of level $n$ correspond to the rays of length $n$; the root has $r$ of them and each subsequent vertex $r-1$, so there are $r(r-1)^{n-1} \asymp (r-1)^n$ cylinders, each of diameter exactly $r^{-n}$, and the box and Hausdorff dimensions are the exponent $\log(r-1)/\log r$ by the Moran–Hutchinson theorem of *Fractal Geometry*. The end set is a Cantor set because the cylinders of each level are pairwise disjoint closed sets whose union is the whole and each contains at least two of the next level. The dendrite is the union of its arcs, countably many of them, each of dimension one, and of the end set of dimension $\log(r-1)/\log r < 1$; a countable union of one-dimensional arcs has dimension one, and adjoining a set of smaller dimension does not change it.

## Fractal Dendrites: Dimension Greater than One

A dendrite of Hausdorff dimension strictly greater than one cannot be a countable union of arcs, and the tree-like dendrites above are therefore not fractal. The fractal dendrites are the continua that are locally trees and globally of dimension greater than one, and the standard family is the tree-like Julia sets.

**Theorem (the tree-like Julia sets).** Let $P_c(z) = z^2 + c$. Suppose that $c$ is a Misiurewicz parameter in the Mandelbrot set, that is, the critical point $0$ is preperiodic to a repelling cycle. Then the Julia set $J_c$ is a dendrite: it is connected, locally connected, nowhere dense, and its complement is connected. For such $J_c$ the Hausdorff dimension satisfies $1 \leq \dim_H J_c \leq 2$, and for the parameter $c = i$ it is strictly between one and two; the value is not given by a closed formula and is obtained numerically, a computation of *The Hausdorff Dimension of the Julia Sets*.

**Proof sketch.** For a Misiurewicz parameter the critical orbit is eventually periodic and never enters the Fatou set, and the Julia set is connected by the theorem of Douady–Hubbard and locally connected by the theorem of Douady–Hubbard and Shishikura for this class. The Fatou set is the basin of infinity, whose complement is the connected filled Julia set; the basin is simply connected, so the complement of the Julia set is connected, and the Julia set has empty interior, being the boundary of the basin. A locally connected continuum of empty interior with connected complement is a dendrite, as in the characterisation theorem above. The dimension lies in $[1,2]$ because a compact planar set of empty interior that contains arcs has dimension at least one, and a planar set has dimension at most two; the value for $c=i$ is not given by a closed formula and is obtained numerically, and it is computed in *The Hausdorff Dimension of the Julia Sets*.

**Example (the arc, the circle and the dendrite).** For $c = -2$ the Julia set is the interval $[-2,2]$, a dendrite of dimension one and an arc. For $c = 0$ the Julia set is the unit circle, not a dendrite, because the circle is a simple closed curve. For $c = i$ the Julia set is a dendrite of dimension strictly greater than one. The family therefore exhibits, in one parameter, a dendrite of dimension one, a non-dendrite, and a dendrite of dimension greater than one, so the dendrite is neither the cause nor the consequence of the fractal dimension.

**Remark (the dimension is a metric and not a topological statement).** Since every dendrite is of topological dimension one, the dendrites of dimension greater than one exist because the homeomorphism to the tree model is not bi-Lipschitz. Snowflaking the metric of the arc, $d \mapsto d^\alpha$ with $0 < \alpha < 1$, produces a dendrite of Hausdorff dimension $1/\alpha$, which can be made arbitrarily large; this is the construction of *Rectifiability and the Geometry of Fractal Curves* and it shows that the Hausdorff dimension of a dendrite has no upper bound over all metrics. For a planar dendrite with the induced Euclidean metric, the dimension is at most two, and the tree-like Julia sets above attain values strictly between one and two.

## Self-Similar Dendrites and Limit Spaces

**Definition (self-similar dendrite).** A dendrite $X$ is **self-similar** when there is a finite family of similarities $\{f_i\}$ of $X$ with $\bigcup_i f_i(X) = X$ and the pieces $f_i(X)$ meet only in branch points and ends. The end space of such a dendrite carries the same iterated function system, and it is a self-similar Cantor set when the pieces are disjoint on the ends, as for the regular tree above.

**Theorem (the self-similar dendrites of the limit spaces).** Let $G$ be a self-similar group acting on a rooted tree, and suppose that the limit space of the action is a dendrite. Then $G$ is a regular branch group, the dendrite is the limit space of the action, and the ends of the dendrite are the boundary of the tree quotiented by the action; the Fabrykowski–Gupta group is the standard instance, and its limit space is a dendrite on which the group acts by similarities.

**Proof sketch.** The limit space of a self-similar group is the quotient of the boundary of the tree by the equivalence relation generated by the action, and it is connected exactly when the action is transitive on the levels; the absence of a circle is the contraction property of the action, which is proved in *Limit Spaces and Schreier Graphs*, where the construction, the finite-state condition and the examples are given. The Fabrykowski–Gupta group is a self-similar group generated by two automorphisms of the binary tree whose limit space is a dendrite; the branch points are the images of the vertices under the equivalence relation, and the ends are the images of the ends of the tree.

**Remark (the link to the boundary).** The end space of a self-similar dendrite is a quotient of the boundary $\partial T$ of the tree, and when the action is free on the ends it is the whole boundary. The **Hausdorff dimension of the boundary**, with the visual metric, is the subject of *The Dimension of the Boundary of a Hyperbolic Group*, where the general formula and the case of the free group are computed; the dendrite here and the hyperbolic boundary there are two readings of the same end space, one topological and one metric. The distinction between the two is exactly the distinction made in this article between the topological dimension of the dendrite and the Hausdorff dimension of its end set.

## Summary

A dendrite is a locally connected continuum with no simple closed curve, equivalently a continuum in which any two points are joined by a unique arc, or one in which the intersection of two subcontinua is connected. Every dendrite has topological dimension one, but its Hausdorff dimension is a metric invariant that can be strictly greater than one and is unbounded over the choice of metric; it equals one for the dendrites that are countable unions of arcs together with an end set of smaller dimension, such as the end compactification of a locally finite tree, whose end space is a Cantor set of Hausdorff dimension $\log(r-1)/\log r$ in the visual metric of the regular tree $T_r$, and a dendrite of Hausdorff dimension strictly greater than one cannot be a countable union of arcs. The dendrites of dimension greater than one are the tree-like Julia sets, such as $J_i$, and the limit spaces of the self-similar groups. The end space of a dendrite is compact and totally disconnected, it is the boundary of the tree in the sense of *Metric Geometry*, and its metric reading, the Hausdorff dimension with the visual metric, is the subject of *The Dimension of the Boundary of a Hyperbolic Group*; the topological theory of the continua used here is that of *Topological Spaces* and *Dimension Theory*, and the limit space construction is that of *Limit Spaces and Schreier Graphs*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| Continuum | Compact connected metric space |
| Dendrite | Locally connected continuum containing no simple closed curve |
| Cut point, branch point | Point whose removal disconnects; point of order at least three |
| End, $E(X)$ | Point of order one, up to the local structure; the end space |
| Arc, simple closed curve | Homeomorphic copies of $[0,1]$ and of the circle |
| $T_r$, $\overline{T_r}$ | The rooted tree with $r$ branches at the root and $r-1$ thereafter; its end compactification |
| $E(T_r)$, $\ell(\xi,\eta)$ | End space of $T_r$; length of the common initial path |
| $\log(r-1)/\log r$ | Hausdorff dimension of $E(T_r)$ in the visual metric |
| $J_c$, $J_i$ | Julia set of $z^2+c$; the tree-like dendrite |
| $\dim_{top}$, $\dim_H$ | Topological dimension; Hausdorff dimension |

## Further Reading

- Gordon T. Whyburn, *Analytic Topology* (American Mathematical Society Colloquium Publications 28, 1942), for the continua, the cut points, the branch points and the structure of dendrites.
- Sam B. Nadler Jr., *Continuum Theory: An Introduction* (Marcel Dekker, 1992), for the modern treatment of dendrites and the end space.
- Kazimierz Kuratowski, *Topology, Volume II* (Academic Press, 1968), for the end compactification and the continua of finite length.
- Volodymyr Nekrashevych, *Self-Similar Groups* (American Mathematical Society, 2005), for the limit spaces and the dendrites of the self-similar groups.
- John Milnor, *Dynamics in One Complex Variable* (Princeton University Press, 3rd edition, 2006), for the tree-like Julia sets and the Mandelbrot set.
- Mitsuhiro Shishikura, "The Hausdorff dimension of the boundary of the Mandelbrot set and Julia sets", *Annals of Mathematics* 147 (1998), 225–267, for the dimension two boundary parameters.
- Christopher J. Bishop and Yuval Peres, *Fractal Sets in Probability and Analysis* (Cambridge University Press, 2017), for the Cantor sets and the end spaces of the trees.
- Andreas W. M. Dress, "Trees, tight extensions of metric spaces, and the cohomological dimension of certain groups", *Advances in Mathematics* 53 (1984), 321–402, for the real trees and the four-point condition, compared with the dendrites here.
