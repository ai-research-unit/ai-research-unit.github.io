
# __Metric Geometry__

## Introduction

Metric geometry is the geometry of a set with a distance, developed with the distance alone: the objects are the **distance spaces**, the maps are the **isometries**, and the concepts are the betweenness of the points, the metric segments, the lengths of the curves, the convexity, the embeddability into a Euclidean or a Hilbert space, the convergence of the spaces themselves, and the curvature conditions expressed by the comparison of the triangles. The subject begins with the observation that the triangle equality $d(x,y) = d(x,z) + d(z,y)$ defines a notion of "between" which is the metric remnant of the affine structure, and that the whole of the convexity theory follows from it: a complete metrically convex space has segments, a length space has geodesics, and the conditions of the triangle comparison classify the spaces of negative and of positive curvature without any appeal to a differentiable structure. It ends, in the modern development, with a distance on the collection of the compact metric spaces themselves, the **Gromov–Hausdorff distance**, which makes that collection a metric space whose convergent sequences are the natural approximations of one space by another, and with the classes of the **CAT** and the **Alexandrov** spaces, defined by the triangle comparisons and stable under the Gromov–Hausdorff convergence.

The article belongs to this Part because the distance is the one structure that the Part adds, and because its parent is *Metric, Uniform and Complete Spaces*, where the metric, the completeness, the uniform continuity and the isometry group are introduced; the present article develops the geometry that the distance supports, and it cites the parent for those foundations. The **Riemannian** geometry is the geometry agents' and is cited here for the differentiable side of the same questions: the geodesics of a Riemannian manifold, the curvature, the theorem of Myers and Steenrod that the isometries of a Riemannian manifold are smooth, and the theorems of Cartan–Hadamard and of Toponogov, which are the differentiable prototypes of the metric curvature conditions of the present article. The quasi-isometries, the word metrics, the growth and the Gromov boundary are the subject of *Geometric Group Theory* and of *Hyperbolic Groups* of this Part, and they are cited rather than developed. The article keeps to the distance, and no measure, no integral and no differentiability is used: the lengths are defined by the suprema over the finite partitions, and the curvatures by the comparison of the triangles.

## Distance Spaces and Metric Betweenness

### Distance Spaces and Their Morphisms

**Definition.** A **distance space**, or metric space, is a set $X$ with a function $d : X \times X \to [0,\infty)$ which is symmetric, vanishes exactly on the diagonal and satisfies the triangle inequality, as in *Metric, Uniform and Complete Spaces*; a map $f : X \to Y$ between distance spaces is an **isometry** if it is a bijection preserving the distances, $d_Y(f(x),f(x')) = d_X(x,x')$, an **isometric embedding** if it preserves the distances without being surjective, and a **Lipschitz map** of constant $L$ if $d_Y(f(x),f(x')) \leq L\,d_X(x,x')$. The **isometry group** $\operatorname{Isom}(X)$ is the group of the isometries of $X$ onto itself, with the compact-open topology of *Topological Spaces*; the group acts on the space, and the space is **two-point homogeneous** if for every two pairs of points with the same distance there is an isometry carrying one pair to the other.

**Proposition.** The isometries preserve every metric notion: the diameter, the balls and the spheres, the boundedness, the completeness and the total boundedness, the betweenness and the segments below, the length of a curve, and the Hausdorff dimension-type invariants defined from the covering numbers; the isometry group of a compact metric space is compact in the compact-open topology, and that of a proper metric space, in which every closed ball is compact, is locally compact and acts properly.

**Proof.** Each of the listed notions is defined from the distance by a formula with quantifiers, and a bijection preserving the distance preserves the formula; the compactness of the isometry group of a compact space is the Ascoli-type statement that a uniformly equicontinuous family of maps of a compact space is compact in the compact-open topology, applied to the family of the isometries, which is uniformly equicontinuous with the constant $1$. The properness statement is the same argument on the closed balls. $\square$

**Remark.** The distance on a space is a complete invariant of its metric geometry, but not of its topology alone: a set may carry two metrics with the same topology and different isometry groups, and the metric geometry of a space is the study of the quantity $\operatorname{Isom}(X)$ and of the invariants of the distance rather than of the topology. The **normed** spaces of *Normed and Banach Spaces* are the distance spaces whose distance comes from a norm, $d(x,y) = \|x - y\|$, and their geometry, with the translation invariance and the homogeneity, is the linear part of the metric geometry; the general distance space has neither the translations nor the scalars, and the betweenness below replaces them.

### Betweenness and Metric Segments

**Definition.** Let $X$ be a distance space and let $x, y, z \in X$. The point $z$ is **between** $x$ and $y$ if
$$
d(x,y) = d(x,z) + d(z,y),
$$
the equality of the triangle inequality; the **metric interval** is $[x,y] = \{z : z \text{ is between } x \text{ and } y\}$, and it always contains $x$ and $y$. A **midpoint** of $x$ and $y$ is a point $z$ with $d(x,z) = d(z,y) = \frac12 d(x,y)$, and a **metric segment** from $x$ to $y$ is a subset $S \subseteq [x,y]$ containing $x, y$ which is isometric to the interval $[0, d(x,y)]$ of the real line with its usual distance, the isometry sending $0$ to $x$ and $d(x,y)$ to $y$; a distance space is **geodesic** if every two of its points are joined by a metric segment.

**Proposition.** The betweenness relation determines the metric intervals, and it is preserved by the isometries; a point $z$ between $x$ and $y$ is unique with a given distance from $x$ exactly when the space is "uniquely geodesic" on the interval, and the metric interval of two points of a normed space is the set of the points of the affine segment that are metric between, which contains the affine segment and may be strictly larger in the non-strictly-convex norms.

**Proof.** The statements about the isometries and the intervals are immediate from the definitions. In a normed space the triangle equality $\|x-z\| + \|z-y\| = \|x-y\|$ holds exactly for the points $z$ of the affine segment $[x,y]$ when the norm is strictly convex, and for a larger set in the general case, the set of the points $z$ for which $x - z$ and $z - y$ are positively proportional in the norm, which is the equality case of the triangle inequality of the norm; the classical characterisation of that equality case is in *Normed and Banach Spaces*. $\square$

**Definition.** A distance space is **metrically convex**, in the sense of Menger, if for every distinct points $x, y$ there is a point $z$, distinct from both, between them; it is **convex** if every two points have a midpoint, and **strictly convex** if the midpoint is unique when it exists.

**Theorem (Menger).** A complete metrically convex distance space is geodesic: every two points are joined by a metric segment. Consequently a closed subset of a complete space that is metrically convex in itself carries segments, and the metric segments of a complete space are the images of the intervals under the isometric embeddings.

**Proof sketch.** The proof iterates the midpoints: a midpoint of $x$ and $y$ is constructed by the metric convexity, then the midpoints of the halves, and the induction produces a map of the dyadic rationals of the interval into the space which preserves the distances of the dyadic rationals; the completeness extends the map to the whole interval by the limits of the Cauchy sequences, the extension is an isometric embedding of the interval because the distance is continuous, and its image is a metric segment. The completeness is used exactly for the extension, and the construction is the classical one of Menger; the details are in the references. $\square$

### Lengths and Intrinsic Metrics

**Definition.** Let $\gamma : [a,b] \to X$ be a curve in a distance space. The **length** of $\gamma$ is the supremum
$$
\ell(\gamma) = \sup\Bigl\{\sum_{i=0}^{n-1} d(\gamma(t_i), \gamma(t_{i+1})) : a = t_0 < t_1 < \cdots < t_n = b\Bigr\}
$$
over the finite partitions of the interval, and $\gamma$ is **rectifiable** if the length is finite; the length of the restriction of $\gamma$ to $[a,t]$ is a nondecreasing function of $t$, and if $\gamma$ is rectifiable the reparametrisation by this function is the **arc-length parametrisation**, an isometry from an interval of the line onto the image in the sense that the length of every subcurve equals the length of the corresponding interval. The **intrinsic metric** of $X$ is
$$
d_i(x,y) = \inf\{\ell(\gamma) : \gamma \text{ rectifiable from } x \text{ to } y\},
$$
and $X$ is a **length space** if $d_i = d$; the intrinsic metric always satisfies $d_i \geq d$, and $d_i$ is itself a metric when the space is connected by the rectifiable curves.

**Proposition.** The length is additive over the concatenation of the curves and invariant under the isometries and under the reparametrisations; the arc-length parametrisation exists for every rectifiable curve and is unique up to the choice of the origin; a metric segment is a length-minimising curve, so a geodesic space is a length space, and the converse fails: a length space has the segments only when it is complete and locally compact, by the theorem below.

**Proof.** The additivity follows by refining the partitions across the concatenation point; the invariance under the isometries is the definition; the arc-length parametrisation is the standard monotone reparametrisation by the length function, and it is an isometry onto the image relative to the length of the subcurves, which are the distances in the parametrisation. A metric segment has $\ell(\gamma) = d(x,y)$ because the sum of the distances along it telescopes; the converse statement is the theorem of the next paragraph. $\square$

**Theorem (Hopf–Rinow, metric form).** Let $X$ be a complete, locally compact length space. Then every two points of $X$ are joined by a metric segment, and every closed bounded subset of $X$ is compact. Consequently the complete locally compact length spaces are exactly the "geodesic" spaces of the metric geometry, and the theorem is the metric form of the theorem of Hopf and Rinow for the Riemannian manifolds of *Riemannian Geometry*.

**Proof sketch.** The family of the curves of length at most $d(x,y)$ is uniformly equicontinuous and, by the local compactness, has a convergent subsequence; the limit is a curve of minimal length because the length is lower semicontinuous with respect to the uniform convergence, and the minimal curve is a metric segment because the restriction of a minimiser to a subinterval is minimal and the minimality forces the equality of the triangle inequality at every intermediate point. The compactness of the closed bounded sets follows from the completeness and the total boundedness, the last obtained by covering a ball by finitely many smaller balls and using the geodesics to bound the covering numbers. The details are in the references. $\square$

**Example.** The Euclidean space $\mathbb{R}^n$ with the distance of the norm is a complete locally compact length space, and its metric segments are the affine segments; the sphere $S^n$ with the great-circle distance is a complete compact length space whose metric segments are the arcs of the great circles of length at most $\pi$, and it is not uniquely geodesic beyond the diameter. The space $\mathbb{Q}$ of the rationals with the usual distance is metrically convex but not complete, and it has no segment between two distinct rationals that is isometric to a real interval in the rationals, which shows that the completeness in Menger's theorem cannot be dropped. The discrete metric space on two points with the distance $1$ is complete and has no midpoint, so the metric convexity cannot be dropped either.

## Euclidean Embedding and the Cayley–Menger Determinants

### The Cayley–Menger Determinant

**Definition.** Let $x_0, \ldots, x_k$ be points of a distance space and let $d_{ij} = d(x_i, x_j)$. The **Cayley–Menger determinant** is
$$
\operatorname{CM}(x_0,\ldots,x_k) = \det\begin{pmatrix} 0 & 1 & 1 & \cdots & 1 \\ 1 & 0 & d_{01}^2 & \cdots & d_{0k}^2 \\ 1 & d_{10}^2 & 0 & \cdots & d_{1k}^2 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & d_{k0}^2 & d_{k1}^2 & \cdots & 0 \end{pmatrix},
$$
the determinant of the $(k+2) \times (k+2)$ matrix with the vanishing diagonal, the unit border and the squares of the distances off the border.

**Theorem (the volume formula).** Let $x_0, \ldots, x_k$ be points of the Euclidean space $\mathbb{R}^k$ and let $V$ be the volume of the simplex they span. Then
$$
\operatorname{CM}(x_0,\ldots,x_k) = (-1)^{k+1}\, 2^k\, (k!)^2\, V^2 ,
$$
so that the Cayley–Menger determinant has the sign $(-1)^{k+1}$ for the $k+1$ points spanning a nondegenerate simplex of $\mathbb{R}^k$, vanishes exactly for the points lying in an affine subspace of dimension at most $k-1$, and its absolute value is determined by the volume.

**Proof sketch.** The determinant is the Gram determinant computation: the matrix of the squared distances is obtained from the matrix of the inner products of the translated vectors by a change of basis involving the bordering vector, and the determinant of the Gram matrix of the edges of the simplex is $(k!)^2V^2$; assembling the two gives the displayed identity. The statement is verified by the explicit computation of the low cases, in which the determinant of the three points of the plane is $-16V^2$ and that of the four points of the space is $288V^2$, and the general case follows by the same assembly. The details are in the references. $\square$

**Theorem (Menger; the embedding criterion).** A metric space $X$ is isometric to a subset of the Euclidean space $\mathbb{R}^n$ if and only if every subset of $n+3$ points of $X$ is isometric to a subset of $\mathbb{R}^n$; for a finite set $x_0, \ldots, x_m$ the criterion is that the Cayley–Menger determinants satisfy
$$
(-1)^{k+1}\operatorname{CM}(x_{i_0},\ldots,x_{i_k}) \geq 0
$$
for every subset of $k+1$ points with $k \leq n$, and that $\operatorname{CM}$ vanish for every subset of $n+2$ points. Consequently the metric geometry of the finite subsets of $\mathbb{R}^n$ is the geometry of the signs of the Cayley–Menger determinants, and the **four-point property** of a metric space, the condition that every four points embed in the Euclidean plane, is the case $n = 2$ of the criterion.

**Proof sketch.** The necessity is the volume formula, which gives the signs of the determinants for the points of a Euclidean space. For the sufficiency, the vanishing of the determinants of the $(n+2)$-tuples makes the ambient affine dimension at most $n$, the signs give the positive semidefiniteness of the Gram matrix of the edges, and the standard construction of the coordinates from a positive semidefinite Gram matrix produces the isometric embedding; the reduction to the subsets of $n+3$ points is the finite characterisation of Menger, in which the conditions of the higher-dimensional tuples are implied by those of the tuples of $n+3$ points. The details are in the references. $\square$

**Theorem (Schoenberg).** A metric space $X$ embeds isometrically into a Hilbert space if and only if every finite subset of $X$ embeds isometrically into a finite-dimensional Euclidean space; equivalently, if and only if the function $(x,y) \mapsto d(x,y)^2$ is of **negative type**, that is, if the matrix of the values is conditionally negative definite on the finitely supported functions with the vanishing sum. The metric spaces of the negative type include the subsets of the Hilbert spaces and the metric trees, and the condition is the Hilbert-space form of the finite-dimensional criterion of Menger.

**Proof sketch.** The finite-dimensional Euclidean embeddings combine to a Hilbert-space embedding when the dimension is unbounded because the embeddings may be chosen coherently on the increasing finite subsets, each extending the previous one by the positive semidefiniteness of the Gram matrices; the equivalence with the negative type is the algebraic form of the sign conditions of the Cayley–Menger determinants, the conditionally negative definite functions being exactly the squared distances of a Hilbert-space embedding by the standard construction going back to Schoenberg. $\square$

## Trees and the Four-Point Condition

**Definition.** A metric space $X$ satisfies the **four-point condition** if for every four points $x, y, z, w$
$$
d(x,y) + d(z,w) \leq \max\{d(x,z) + d(y,w),\ d(x,w) + d(y,z)\},
$$
equivalently if the largest of the three sums of the opposite pairs of the four points is attained at least twice; a metric space is a **real tree** if it is a length space satisfying the four-point condition, and a space is **$0$-hyperbolic** if it satisfies the four-point condition.

**Theorem.** A metric space satisfies the four-point condition if and only if every four-point subset of it is isometric to a subset of a real tree; a complete metric space satisfies the four-point condition if and only if it is a real tree. The real trees are the geodesic $0$-hyperbolic spaces, and every two points of a real tree are joined by a unique metric segment; the condition for the general $\delta$ is the **Gromov hyperbolicity**, the four-point condition with $\delta$ in place of $0$, treated in *Hyperbolic Groups*.

**Proof sketch.** For four points of a real tree the three sums of the opposite pairs are computed from the structure of the tree, whose minimal subtree is a "spider" with four legs and a centre, and the two largest of the three sums are equal, which gives the inequality; conversely the four-point condition for the triples and the quadruples gives the tree structure of the finite subsets, and the completeness and the length structure extend the finite trees to the whole space by the limits of the segments. The details are in the references. $\square$

**Example.** The Euclidean plane fails the four-point condition: the four vertices of the unit square have $d(x,y) + d(z,w) = 2\sqrt2$ for the two opposite pairs, while the sums of the pairs of the adjacent vertices are $2$, so the largest sum is not attained twice. A star with three leaves at the distances $1, 2, 3$ from the centre satisfies the condition, the two largest sums of the opposite pairs being equal, and it is the minimal subtree of the four points; this is the computation that verifies the theorem in a case with the segment structure.

## The Gromov–Hausdorff Distance

### The Gromov–Hausdorff Distance

**Definition.** Let $(Z,d)$ be a metric space and let $A, B \subseteq Z$ be nonempty closed subsets. The **Hausdorff distance** is
$$
d_H(A,B) = \max\Bigl\{\sup_{a\in A} d(a,B),\ \sup_{b\in B} d(b,A)\Bigr\},
$$
the smallest number $\varepsilon$ such that each set is contained in the $\varepsilon$-neighbourhood of the other. The **Gromov–Hausdorff distance** of two compact metric spaces $X, Y$ is
$$
d_{GH}(X,Y) = \inf\bigl\{ d_H(f(X), g(Y)) : Z \text{ a metric space},\ f : X \to Z,\ g : Y \to Z \text{ isometric embeddings} \bigr\},
$$
the infimum over all the ambient spaces and all the pairs of the isometric embeddings into a common space.

**Theorem.** The Gromov–Hausdorff distance is a metric on the set of the isometry classes of the compact metric spaces; the convergence in this metric, the **Gromov–Hausdorff convergence**, means that there are isometric embeddings of the spaces into a common space whose images have the Hausdorff distance tending to zero. The Gromov–Hausdorff limit of a sequence of compact metric spaces is unique up to the isometry, the isometry classes form a complete metric space with this distance when augmented by an extra point at infinity for the unbounded spaces, and the pointed version, for the spaces with a chosen base point, defines the **pointed Gromov–Hausdorff convergence** of the noncompact locally compact spaces.

**Proof sketch.** The triangle inequality for $d_{GH}$ is proved by the composition of the embeddings into the successive common spaces; the nondegeneracy uses the fact that a Hausdorff distance zero between closed subsets of a common space forces the equality of the sets. For the completeness one takes a Cauchy sequence in the Gromov–Hausdorff sense, chooses the embeddings so that the successive images approximate each other, and forms the limit as the completion of the union of the images modulo the equivalence of the sequences that approach each other; the uniqueness of the limit is the same argument. The details are in the references. $\square$

**Theorem (Gromov; the precompactness).** Let $\mathcal{C}$ be a collection of compact metric spaces with the diameters bounded and the **entropy** bounded: for some sequence $\varepsilon_k \to 0$ and some constants $N_k$, every space of the collection is covered by at most $N_k$ balls of radius $\varepsilon_k$. Then the collection is relatively compact in the Gromov–Hausdorff topology, that is, every sequence of the spaces has a convergent subsequence whose limit is a compact metric space. Thus the compactness in the Gromov–Hausdorff sense is the uniform boundedness of the diameters and of the covering numbers, the metric replacement of the total boundedness of the single space.

**Proof sketch.** For each $k$ choose a finite $\varepsilon_k$-net of each space, with at most $N_k$ points; the nets are finite metric spaces with the distances bounded, and a diagonal argument over the successive levels $k$, with the nets refining each other, produces a subsequence for which the nets converge to a limit net, the limit space being obtained as the completion of the union of the limit nets with the limiting distances. The proof is the classical diagonal extraction of Gromov, and the details are in the references. $\square$

**Example.** The spheres of the fixed dimension with the radii tending to zero converge in the Gromov–Hausdorff sense to the one-point space, since the sphere of radius $r$ has the diameter $\pi r \to 0$; the spheres of dimension $n$ and the radii tending to a limit $r > 0$ converge to the sphere of the radius $r$. The "collapse" of a sequence of the flat tori of the shrinking diameter gives the limit a lower dimension, the circles converging to a point and the two-dimensional tori converging to a circle when one of the periods shrinks; the limit depends on the ratio of the periods, which is the phenomenon of the lower-dimensional collapse. The convergence is not the convergence of the covering dimensions alone: the entropy bounds are the necessary and sufficient data.

### Curvature Conditions in the Metric Sense

**Definition.** Let $k$ be a real number and let $M^2_k$ be the **model surface** of the constant curvature $k$: the Euclidean plane for $k = 0$, the sphere of the radius $1/\sqrt{k}$ for $k > 0$, and the hyperbolic plane of the curvature $k$ for $k < 0$. A **geodesic triangle** in a length space is a triangle with the metric segments as the sides, and a **comparison triangle** in $M_k^2$ is a triangle with the same side lengths. A length space is a **CAT($k$)** space if the space is geodesic and for every geodesic triangle with the perimeter $< 2\pi/\sqrt{k}$ (no condition for $k \leq 0$) the distances of the points of the triangle are no larger than the distances of the corresponding points of the comparison triangle in $M^2_k$; a **complete** length space is an **Alexandrov space of curvature $\geq k$**, written CBB($k$), if the reverse comparison holds, the distances of the points of the triangle being no smaller than those of the comparison triangle.

**Theorem.** The CAT($k$) spaces and the CBB($k$) spaces are closed under the pointed Gromov–Hausdorff limits, and the classes of the Riemannian manifolds with the corresponding curvature bound are the differentiable instances: a complete Riemannian manifold has the sectional curvature at most $k$ exactly when it is locally CAT($k$), and at least $k$ exactly when it is CBB($k$). A CAT($0$) space is uniquely geodesic, the distance functions to the geodesics are convex, the balls are convex, and a complete CAT($0$) space is contractible; a CAT($k$) space with $k > 0$ has the diameter at most $\pi/\sqrt{k}$ by the theorems of Bonnet–Myers type, and the other local properties of the curvature are the metric forms of the comparison theorems of the Riemannian geometry of *Riemannian Geometry*.

**Proof sketch.** The comparison conditions are formulated with the distances only, so they pass to the limits of the spaces because the distances of the limit space are the limits of the distances of the approximating spaces, and the metric segments pass to the limits by the lower semicontinuity of the length; the convexity of the distance functions in a CAT($0$) space follows from the comparison of the triangles with the Euclidean triangles, in which the corresponding statement is the convexity of the distance to a line; the contractibility follows from the existence and the uniqueness of the geodesics from a fixed point, with the homotopy shrinking along them. The identification of the conditions with the curvature bounds of the Riemannian manifolds is the theorem of Toponogov, which is the differentiable form of the comparison and is stated in *Riemannian Geometry*. $\square$

**Example.** The Euclidean spaces, the Hilbert spaces and the Euclidean trees are CAT($0$) and hence CBB($0$); the round spheres are CAT($k$) with $k = 1$ and the hyperbolic spaces are CAT($-1$) and CBB($-1$). The Euclidean cone over a metric space is CAT($0$) when the base is a CAT($1$) space, and hence in particular when the base satisfies the four-point condition of the preceding section, the trees being CAT($k$) for every $k$; the cone over the circle of the circumference $2\pi$ is the Euclidean plane and the cone over a tree is a flat surface, and the example is the basic computation of the link between the tree condition and the curvature.

## Isometries of Distance Spaces

**Definition.** The **isometry group** $\operatorname{Isom}(X)$ of a distance space $X$ is the group of the isometries onto itself, with the compact-open topology; a **local isometry** is a map that preserves the distances locally, that is, on a neighbourhood of each point, and the space is **locally homogeneous** if the local isometries act transitively on the small balls. The group of the isometries of a compact space is compact, of a proper space is locally compact, and the group acts continuously on the space by the evaluation.

**Theorem (Mazur–Ulam; the normed case).** Every surjective isometry of a real normed space onto itself is affine: it is the composition of a linear isometry with a translation; consequently the isometry group of a normed space is the semidirect product of the group of the linear isometries with the group of the translations, and the metric geometry of the normed spaces is the geometry of the unit ball of the norm, whose linear isometries are the linear maps preserving the ball. The theorem is stated in *Normed and Banach Spaces*, and it shows that in the normed case the metric geometry has the affine structure of the ambient linear space.

**Theorem (Myers–Steenrod; the Riemannian case).** Every isometry of a connected Riemannian manifold onto itself is smooth, so that the group of the Riemannian isometries is a Lie group and the metric isometry group coincides with the smooth isometry group of the metric tensor; the proof is in the Riemannian geometry of *Riemannian Geometry*, and the statement is the differentiable refinement of the metric notion of the present article. The metric geometry of a Riemannian manifold is therefore the geometry of its distance, and the metric betweenness, the metric segments and the metric curvature conditions of this article coincide with the geodesics and the curvature bounds of the Riemannian geometry, by the theorem of Hopf–Rinow in the metric form above and the comparison theorem of Toponogov.

**Remark.** The isometry group is the complete invariant of the metric geometry in the sense that a metric space is determined by its distance and the isometries are the automorphisms of that structure; the metric geometry of a space is thus the study of the space up to the isometries, and the invariants of the geometry are the quantities defined from the distance that are invariant under the isometry group. The **Gromov–Hausdorff** distance of the preceding section is the corresponding notion for the spaces themselves: the isometry classes are the objects, the Gromov–Hausdorff distance is the distance between them, and the curvature conditions, the entropy bounds and the diameter bounds are the invariants of the classes. The quasi-isometries, the word metrics and the coarse invariants are the large-scale version of the same circle of ideas, in *Geometric Group Theory*, and the hyperbolic spaces and their boundaries are the invariants of the negative-curvature classes, in *Hyperbolic Groups*.

## Summary

A **distance space** is a set with a distance, its morphisms are the **isometries** and the isometric embeddings, and its geometry is the theory of the quantities defined from the distance. The **betweenness** $d(x,y) = d(x,z)+d(z,y)$ defines the **metric intervals**, the midpoints and the **metric segments**, and *Metric, Uniform and Complete Spaces*, the parent article, supplies the completeness and the uniform continuity used throughout. The **Cayley–Menger determinant** of $k+1$ points satisfies $\operatorname{CM} = (-1)^{k+1}2^k(k!)^2V^2$ for the points of $\mathbb{R}^k$, and the criterion of **Menger** embeds a metric space in $\mathbb{R}^n$ exactly when every subset of $n+3$ points does, the sign conditions of the determinants being the criterion for a finite set; the theorem of **Schoenberg** embeds a space in a Hilbert space exactly when the squared distance is of negative type. The **length** of a curve is the supremum of the sums over the finite partitions, the **arc-length parametrisation** exists for every rectifiable curve, and a **length space** is one whose distance is the infimum of the lengths; a complete metrically convex space is geodesic (Menger), and a complete locally compact length space is geodesic with the compact closed bounded sets (Hopf–Rinow, metric form). The **four-point condition** $d(x,y)+d(z,w) \leq \max\{d(x,z)+d(y,w), d(x,w)+d(y,z)\}$ characterises the subsets of the **real trees** and, with the completeness and the length structure, the trees themselves; the condition with $\delta$ is the Gromov hyperbolicity of *Hyperbolic Groups*. The **Gromov–Hausdorff distance** makes the isometry classes of the compact metric spaces a metric space, the **pointed** version handles the noncompact spaces, and the **precompactness** theorem of Gromov characterises the relatively compact collections by the bounds on the diameters and the covering numbers. The **CAT($k$)** and the **CBB($k$)** conditions compare the triangles with the model surfaces $M^2_k$ and are stable under the Gromov–Hausdorff limits; the Riemannian manifolds with the curvature bounds are their differentiable instances, by the comparison theorems of *Riemannian Geometry*. The **isometry group** is compact for a compact space and locally compact for a proper one; the theorem of **Mazur–Ulam** makes the surjective isometries of a normed space affine, the theorem of **Myers–Steenrod** makes the isometries of a Riemannian manifold smooth, and *Geometric Group Theory* develops the coarse version of the theory.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(X,d)$ | Distance space; $d$ the distance |
| $\operatorname{Isom}(X)$ | Isometry group, with the compact-open topology |
| $z \in [x,y]$ | Betweenness: $d(x,y) = d(x,z) + d(z,y)$ |
| midpoint, metric segment | $d(x,z)=d(z,y)=\frac12d(x,y)$; isometric image of an interval |
| $\ell(\gamma)$ | Length as the supremum over the finite partitions |
| $d_i$ | Intrinsic metric; length space when $d_i = d$ |
| $\operatorname{CM}(x_0,\ldots,x_k)$ | Cayley–Menger determinant |
| $(-1)^{k+1}2^k(k!)^2V^2$ | Value of CM for $k+1$ points of $\mathbb{R}^k$ |
| four-point condition | $d(x,y)+d(z,w) \leq \max\{d(x,z)+d(y,w), d(x,w)+d(y,z)\}$ |
| real tree, $0$-hyperbolic | Length space with the four-point condition |
| $d_H$, $d_{GH}$ | Hausdorff and Gromov–Hausdorff distances |
| $M^2_k$, CAT($k$), CBB($k$) | Model surface; triangle comparison conditions |
| entropy bounds | Uniform bounds on the covering numbers; Gromov precompactness |



## Further Reading

- Leonard M. Blumenthal, *Theory and Applications of Distance Geometry* (Clarendon Press, 1953), for the betweenness, the Cayley–Menger determinants and the embedding theorems of Menger.
- Karl Menger, "Untersuchungen über allgemeine Metrik", *Mathematische Annalen* 100 (1928), 75–163, for the metric convexity and the embedding criterion.
- Dmitri Burago, Yuri Burago and Sergei Ivanov, *A Course in Metric Geometry* (American Mathematical Society, 2001), for the length spaces, the Hopf–Rinow theorem, the Gromov–Hausdorff distance and the curvature conditions.
- Mikhael Gromov, "Groups of Polynomial Growth and Expanding Maps", *Publications Mathématiques de l'IHÉS* 53 (1981), 53–73, for the Gromov–Hausdorff convergence and the precompactness theorem.
- Martin R. Bridson and André Haefliger, *Metric Spaces of Non-Positive Curvature* (Springer, 1999), for the CAT($k$) spaces, the trees and the four-point condition.
- Yu. G. Reshetnyak, "Two-Dimensional Manifolds of Bounded Curvature", in *Geometry IV* (Springer, 1993), for the Alexandrov spaces of curvature bounded below and the triangle comparison.
- Isaac J. Schoenberg, "Metric Spaces and Positive Definite Functions", *Transactions of the American Mathematical Society* 44 (1938), 522–536, for the negative type and the Hilbert-space embedding.
