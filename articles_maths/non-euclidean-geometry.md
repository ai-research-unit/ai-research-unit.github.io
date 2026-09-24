
# __Non-Euclidean Geometry__

## Introduction

Non-Euclidean geometry is the name given to the geometries that satisfy all of Euclid's axioms except the parallel postulate, together with the study of what that single change entails. There are two such geometries: the **spherical** (or elliptic) geometry, of positive curvature, in which no two lines are parallel, and the **hyperbolic** geometry, of negative curvature, in which infinitely many lines through a point fail to meet a given line. Both were constructed in the nineteenth century as definitive answers to the question, two thousand years old, whether the parallel postulate is a consequence of the others; the answer is that it is not, and the two geometries are the proof. This article is the comparative article of the group: it takes the three model geometries — Euclidean, spherical and hyperbolic — develops them side by side, and exhibits the trichotomy that organises them.

The organising idea is that the three geometries are one family, read through the sign of a single number. In the synthetic formulation, the three differ in the parallel postulate and in the angle sum of a triangle; in the analytic formulation, they are the three complete simply connected Riemannian manifolds of constant curvature $K > 0$, $K = 0$ and $K < 0$; in the trigonometric formulation, they are the three cases of the same law of cosines with the circular, linear and hyperbolic functions; and in the algebra-of-Part-I formulation, they are the geometries of the three two-dimensional algebras $\mathbb{C}$, $\mathbb{D}'$ and $\mathbb{D}$, whose generators square to $-1$, $0$ and $+1$. The article develops each of the four readings and shows that they agree, so that a statement in one language can be read in the others.

The article assumes *Euclidean Geometry*, *Spherical Geometry* and *Hyperbolic Geometry*, which supply the three geometries in full, and *Curvature and Geodesics*, which supplies the curvature and the classification of the constant-curvature models. It uses *The Three Two-Dimensional Algebras and the Three Kinds of Rotation* for the algebra trichotomy, *Metric, Uniform and Complete Spaces* for the metric and limit notions that the comparison uses (the limits being those of a sequence of metric spaces, which is the ordinary theory of Part I), *Groups* and *Group Actions and Structure* for the symmetry groups, and *Riemannian Geometry* for the space-form theorems. The general limit theory of a sequence of Riemannian manifolds, which is a different and more delicate object, iswritten and in parallel, and it is cited only as the vehicle for the flat limit; the analytic theory of hyperbolic volume and of the spectral geometry of the quotients is Part III's. No physics is invoked.

## The Three Geometries

### The Parallel Postulate and Its Denials

The three geometries share the incidence, order, congruence and continuity axioms of Hilbert, and differ in the parallel axiom. In the plane, for a line $\ell$ and a point $P \notin \ell$, let $S(P, \ell)$ be the set of lines through $P$ that do not meet $\ell$.

**Definition.** The three model geometries are distinguished by the cardinality of $S(P, \ell)$:

| Geometry | $|S(P, \ell)|$ | Parallel postulate | Curvature sign |
|---|---|---|---|
| Euclidean | $1$ | Playfair's axiom | $K = 0$ |
| Spherical / elliptic | $0$ | no parallels | $K > 0$ |
| Hyperbolic | $|\mathbb{R}|$ | infinitely many parallels | $K < 0$ |

**Theorem.** The three rows are logically distinct: no one of the three parallel axioms is a consequence of the other axioms of Euclidean geometry.

**Proof sketch.** The upper half-plane model of *Hyperbolic Geometry* satisfies the incidence, order, congruence and continuity axioms and has infinitely many parallels through each exterior point; the round sphere or its antipodal quotient of *Spherical Geometry* satisfies them and has none. Since a statement and its negation cannot both follow from the remaining axioms, the parallel postulate is independent of them in each direction. $\square$

**Remark (history and logic).** The independence was established by the construction of the two models: the Beltrami–Klein and Poincaré models for the hyperbolic case, and the sphere itself, which was known since antiquity as a model in which all geodesics meet; the logical point is that the models are models of the non-parallel axioms in the Euclidean plane's own terms. The models are therefore the content of the theorem, and the remainder of this article is the comparison of their properties.

### The Angle Sum and the Defect

**Theorem (angle sum).** For a geodesic triangle in each geometry,

$$
A + B + C = \begin{cases} \pi + \Delta/R^2, & K = +1/R^2, \\ \pi, & K = 0, \\ \pi - \Delta/R^2, & K = -1/R^2, \end{cases}
$$

where $\Delta$ is the area of the triangle. In the spherical case the **spherical excess** $A + B + C - \pi$ is the area divided by $R^2$; in the hyperbolic case the **defect** $\pi - (A + B + C)$ is the area divided by $R^2$.

**Proof.** All three are the Gauss–Bonnet theorem for a geodesic triangle in a surface of constant curvature, which is the surface case of *Curvature and Geodesics*; the sign of the curvature is the sign of the deviation from $\pi$. $\square$

**Corollary.** A geodesic triangle in the positive-curvature case has angle sum greater than $\pi$, and its area is at most $2\pi R^2$, the area of a hemisphere; in the hyperbolic case the angle sum is less than $\pi$ and the area is at most $\pi R^2$. There is a bound on the area of a triangle in the non-Euclidean geometries and none in the Euclidean case, since a Euclidean triangle may be scaled without limit.

**Corollary (similarity).** In Euclidean geometry triangles with equal angles are similar, hence equal up to scale; in the spherical and hyperbolic geometries there is no similarity beyond congruence, because the angles of a triangle determine its area and hence, in these geometries, its size. Similarity is therefore a peculiarity of the flat case.

### The Comparison of the Trigonometries

**Theorem (the unified law of cosines).** Let $K$ be the curvature, so that the model has radius $R = 1/\sqrt{K}$ for $K > 0$ and $R = 1/\sqrt{-K}$ for $K < 0$, and let $s_K(t)$ be the solution of $s_K'' + K s_K = 0$ with $s_K(0) = 0$, $s_K'(0) = 1$:

$$
s_K(t) = \begin{cases} \sin(t\sqrt K)/\sqrt K, & K > 0, \\ t, & K = 0, \\ \sinh(t\sqrt{-K})/\sqrt{-K}, & K < 0. \end{cases}
$$

Then for a geodesic triangle with sides $a, b, c$ and the interior angle $C$ between the sides $a$ and $b$, writing $\tilde C = \pi - C$ for the exterior angle at that vertex,

$$
c_K(c) = c_K(a)c_K(b) - K\,s_K(a)s_K(b)\cos\tilde C ,
$$

where $c_K(t) = s_K'(t)$ is the cosine in the positive case, the constant $1$ in the flat case, and the hyperbolic cosine in the negative case. The three classical laws of cosines are the three cases: for $K > 0$ the formula reads $\cos c = \cos a\cos b + \sin a\sin b\cos C$, for $K = 0$ it reads $c^2 = a^2 + b^2 - 2ab\cos C$, and for $K < 0$ it reads $\cosh c = \cosh a\cosh b - \sinh a\sinh b\cos C$.

**Proof sketch.** In the flat and spherical cases this is the computation with the inner product of $\mathbb{R}^2$ and $\mathbb{R}^3$ respectively; in the hyperbolic case with the indefinite form of $\mathbb{R}^{1,2}$; the four laws of trigonometry of *Spherical Geometry* and *Hyperbolic Geometry* are instances. The single curvature factor $K$ multiplies the product of the two model sines, and the passage from the circular to the hyperbolic functions is the passage from the positive definite form to the indefinite; the exterior angle is used because the sign of the cosine term is the sign of the curvature in the interior-angle form. $\square$

**Corollary (the Euclidean limit).** As $K \to 0$ the functions $s_K \to t$ and $c_K \to 1$, and the unified law becomes $c^2 = a^2 + b^2 - 2ab\cos C$, the Euclidean law. Both the spherical and the hyperbolic geometries therefore converge to the Euclidean as the curvature tends to zero; the flat geometry is the boundary case of the family, not an exceptional one.

**Corollary (the sign is visible in the geometry).** Since $c_K(t) = 1 - Kt^2/2 + O(t^4)$, the angle sum's deviation from $\pi$ is proportional to $K$ times the area, and the size of the deviation is the size of the curvature: on a surface of small curvature and small area the three geometries are indistinguishable by any local test, which is the reason the question of the parallel postulate was resolved by constructing a model rather than by an experiment.

## The Algebra Trichotomy

### The Three Two-Dimensional Algebras

The three geometries can be read from the three real two-dimensional algebras of *The Three Two-Dimensional Algebras and the Three Kinds of Rotation*, whose basis is $\{1, \omega\}$ and whose multiplication is determined by $\omega^2$:

| Algebra | $\omega^2$ | Number system | Rotation group | Geometry |
|---|---|---|---|---|
| $\mathbb{C}$ | $-1$ | complex numbers | $SO(2)$ | spherical / elliptic |
| $\mathbb{D}'$ | $0$ | dual numbers | transvections | Euclidean |
| $\mathbb{D}$ | $+1$ | split complex numbers | $SO(1,1)_0$ | hyperbolic |

**Theorem.** The three algebras are pairwise non-isomorphic over $\mathbb{R}$, and each is a quotient of the polynomial ring $\mathbb{R}[t]$ by an irreducible, a repeated linear, and a split linear factor respectively; the sign of $\omega^2$ is the sign of the curvature of the geometry whose rotation group the algebra generates.

**Proof.** The three polynomials $t^2 + 1$, $t^2$ and $t^2 - 1$ are pairwise non-proportional, so the quotients are non-isomorphic as $\mathbb{R}$-algebras; the identification of the rotation groups is the content of *The Three Two-Dimensional Algebras and the Three Kinds of Rotation*. The curvature sign is the sign of $\omega^2$ because the algebra is the infinitesimal model of the rotation group of the geometry, and the generator satisfies $\omega^2 = K$. $\square$

**Remark.** The correspondence is structural, not a coincidence of notation. The Lie algebra of rotations of the sphere is $\mathfrak{so}(2) = \mathbb{R}J$ with $J^2 = -1$; the Lie algebra of Euclidean rotations is the abelian algebra of transvections, whose generator squares to $0$; and the Lie algebra of the hyperbolic rotations is $\mathfrak{so}(1,1) = \mathbb{R}\omega$ with $\omega^2 = +1$. The three geometries are the three real forms of the two-dimensional rotation algebra, and their curvatures are the three values of the square of the generator.

### The Symmetry Groups

**Definition.** The **isometry group** of each model, orientation-preserving part:

| Geometry | Isometry group | Orientation-preserving | Dimension (plane) |
|---|---|---|---|
| Euclidean $\mathbb{R}^2$ | $\mathbb{R}^2 \rtimes O(2)$ | $\mathbb{R}^2 \rtimes SO(2)$ | $3$ |
| Spherical $S^2$ | $O(3)$ | $SO(3)$ | $3$ |
| Hyperbolic $\mathbb{H}^2$ | $PSL(2,\mathbb{R}) \rtimes \mathbb{Z}/2$ | $PSL(2, \mathbb{R})$ | $3$ |

**Theorem.** Each group acts transitively on the points of its model and, after a point is fixed, transitively on the frames at that point; each is a three-dimensional Lie group, so each model is a homogeneous space and a symmetric space. The stabiliser of a point is $O(2)$ in the Euclidean case, $O(2)$ in the spherical case and $O(2)$ in the hyperbolic case, so all three models are of the form $G/O(2)$ up to the compact factor.

**Proof sketch.** Transitivity on points and frames is the definition of a space of constant curvature and is verified in each case in the three articles; the dimensions are those of the groups $\mathbb{R}^2 \rtimes O(2)$, $O(3)$ and $PSL(2, \mathbb{R})$, all three-dimensional as Lie groups; the stabiliser identification is the classical fact that a frame at a point of a surface has two degrees of freedom. $\square$

The three homogeneous spaces $E(2)/O(2)$, $O(3)/O(2)$ and $PSL(2, \mathbb{R})/O(2)$ are the three two-dimensional symmetric spaces of rank one, the first non-compact flat, the second compact and the third non-compact; they are the model cases .

## The Model Comparison

### Triangles, Circles and Parallels

**Theorem (trigonometric identities in the three geometries).** For a right triangle with legs $a, b$ and hypotenuse $c$,

| Geometry | Pythagorean relation | Circle circumference | Circle area |
|---|---|---|---|
| Euclidean | $c^2 = a^2 + b^2$ | $2\pi r$ | $\pi r^2$ |
| Spherical | $\cos c = \cos a\cos b$ | $2\pi R\sin(r/R)$ | $2\pi R^2(1 - \cos(r/R))$ |
| Hyperbolic | $\cosh c = \cosh a\cosh b$ | $2\pi R\sinh(r/R)$ | $2\pi R^2(\cosh(r/R) - 1)$ |

**Proof sketch.** The Pythagorean relations are the right-triangle cases of the unified law of cosines. The circumference and area of a geodesic circle are computed by integrating the metric in geodesic polar coordinates; in the model of curvature $K$ these are the standard formulae, with the expansion $2\pi r(1 - Kr^2/6 + \cdots)$ for the circumference in each case. $\square$

**Corollary.** In the spherical case the circumference of a circle is less than $2\pi r$ and attains a maximum $2\pi R$ at $r = \pi R/2$, after which it decreases; in the hyperbolic case it is greater than $2\pi r$ and grows exponentially. In both non-Euclidean cases the ratio of circumference to radius depends on the radius, so $\pi$ is not a geometric constant of the space; the Euclidean case is exactly the one in which the ratio is constant, which is the analytic form of the parallel postulate.

**Corollary (volume growth).** The volume of a ball of radius $r$ in the model of curvature $K$ satisfies

$$
\operatorname{vol} B(r) = \begin{cases} \omega_{n-1}\int_0^r \bigl(\sin(t\sqrt K)/\sqrt K\bigr)^{n-1}dt, & K > 0, \\ \omega_{n-1}r^n/n, & K = 0, \\ \omega_{n-1}\int_0^r \bigl(\sinh(t\sqrt{-K})/\sqrt{-K}\bigr)^{n-1}dt, & K < 0, \end{cases}
$$

with $\omega_{n-1}$ the volume of the unit sphere $S^{n-1}$. The spherical volume is bounded by the total volume of the sphere; the Euclidean volume grows polynomially; the hyperbolic volume grows exponentially. The exponential growth is the geometric shape of negative curvature and is the source of most of the large-scale differences between the three cases.

### The Gauss–Bonnet Theorem in the Three Geometries

**Theorem (Gauss–Bonnet for a geodesic polygon).** For a geodesic $n$-gon with angles $\alpha_1, \ldots, \alpha_n$ in the model of curvature $K$ and radius $R = 1/\sqrt{|K|}$,

$$
\sum_{i=1}^{n}\alpha_i = (n - 2)\pi + K\,\Delta ,
$$

where $\Delta$ is the area of the polygon, so that the angle sum exceeds the Euclidean value by $K\Delta$.

**Proof.** Triangulate the polygon into $n-2$ triangles by diagonals drawn from a single vertex, so that no vertex of the triangulation lies in the interior; applying the angle-sum theorem to each triangle and summing, the angles at the boundary vertices contribute exactly the angles of the polygon and the areas add. $\square$

**Corollary (the area of a compact surface).** A compact oriented surface of constant curvature $K$ has $K \cdot \operatorname{area} = 2\pi\chi(M)$, so the sign of $K$ is the sign of the Euler characteristic: the positive-curvature surfaces are the sphere and the projective plane, the flat surfaces are the torus and the Klein bottle, and the negative-curvature surfaces are all the others.

### The Parallel Families and the Boundary

**Theorem (the structure of the parallels).** Let $\ell$ be a geodesic and $P$ a point at distance $d$ from it.

**(a)** In Euclidean geometry there is exactly one line through $P$ not meeting $\ell$, and it is at constant distance $d$ from $\ell$.

**(b)** In spherical geometry no line through $P$ fails to meet $\ell$; every pair of geodesics meets in two antipodal points, or in one point in elliptic space.

**(c)** In hyperbolic geometry there are two geodesics through $P$ asymptotic to $\ell$, making the angle of parallelism $\Pi(d) = 2\arctan(e^{-d})$ with the perpendicular, infinitely many lines through $P$ meeting $\ell$ within the cone they bound, and infinitely many not meeting it; the lines not meeting $\ell$ diverge exponentially and are at unbounded distance from it.

**Proof.** Parts (a) and (b) are in *Euclidean Geometry* and *Spherical Geometry*; part (c) is the angle-of-parallelism theorem of *Hyperbolic Geometry*. $\square$

**Remark (the conformal boundary).** The spherical and Euclidean models have no boundary, while the hyperbolic space has a boundary at infinity $\partial\mathbb{H}^n$ on which the isometry group acts by Möbius transformations. The presence or absence of this boundary is the deepest structural difference among the three: the compact spherical and flat models have finite diameter, while the hyperbolic model is non-compact with exponential growth. The trichotomy is therefore also a statement about compactness, about the growth of the fundamental group and about the boundary.

## Models, Embeddings and Consistency

### The Embedding Into Euclidean Space

**Theorem (Hilbert).** The hyperbolic plane cannot be isometrically embedded as a complete surface in $\mathbb{R}^3$; it admits incomplete analytic embeddings into $\mathbb{R}^3$, and complete isometric embeddings into $\mathbb{R}^{3,1}$ — or into $\mathbb{R}^5$ by the Nash embedding theorem.

**Proof sketch.** The hyperboloid model is a complete isometric embedding into the pseudo-Euclidean space $\mathbb{R}^{3,1}$; Hilbert's theorem excludes a complete embedding into the Euclidean three-space by an argument on the asymptotic behaviour of an isometric immersion, using the exponential growth of the area. $\square$

**Remark.** The theorem is the reason the hyperbolic plane is usually presented by models — the disk, the half-plane, the Beltrami–Klein projective model — rather than as a surface in space. The spherical plane embeds in $\mathbb{R}^3$ as the sphere and the Euclidean plane embeds in itself; the hyperbolic plane embeds only in a higher-dimensional or indefinite ambient space, and the obstruction is the exponential growth of its volume.

### Consistency and Categorical Reading

**Theorem (relative consistency).** The hyperbolic and spherical geometries are consistent if and only if the Euclidean geometry is: a model of the Euclidean axioms that satisfies the denial of the parallel postulate is constructed inside Euclidean space itself, by the Poincaré disk and the sphere.

**Proof.** The upper half-plane and the disk models are subsets of the Euclidean plane with a redefined notion of distance, and the verification of the incidence, order, congruence and continuity axioms is a computation in Euclidean geometry, so any contradiction in the hyperbolic theory would give one in the Euclidean; conversely the Euclidean plane embeds in the hyperbolic as the horosphere limit. The spherical model is a subset of Euclidean three-space. $\square$

**Remark (the categorical picture).** The three geometries are the three complete simply connected Riemannian surfaces of constant curvature, and the theorem of *Riemannian Geometry* classifies them: for each real $K$ there is exactly one, and these are the spherical, flat and hyperbolic planes. The uniqueness is what makes the comparison of this article possible: there is one geometry for each sign and no more, so a property of the sign of the curvature is a property of the geometry.

## Summary

Non-Euclidean geometry consists of the two geometries that deny the parallel postulate: the spherical (elliptic) geometry of positive curvature, in which no two lines are parallel, and the hyperbolic geometry of negative curvature, in which infinitely many lines through a point avoid a given line. The construction of models of both — the sphere and its antipodal quotient, and the disk and half-plane models — proves that the parallel postulate is independent of the other axioms of Euclid.

The three geometries form one family read through the sign of the curvature. The angle sum of a triangle is $\pi + K\Delta$, with $K$ the curvature and $\Delta$ the area, so the spherical excess and the hyperbolic defect are the two signs of the same formula; triangles have bounded area in the non-Euclidean cases and unbounded area in the flat case; and similarity of triangles exists only in the flat case, because the angles determine the area. The unified law of cosines has the three classical laws as the cases $K > 0$, $K = 0$ and $K < 0$, and recovers the Euclidean law as $K \to 0$.

In the language of Part I the three geometries are the geometries of the three real two-dimensional algebras $\mathbb{C}$, $\mathbb{D}'$ and $\mathbb{D}$, whose generators satisfy $\omega^2 = -1, 0, +1$; the sign is the sign of the curvature and the three rotation groups are $SO(2)$, the transvection group and $SO(1,1)_0$. The isometry groups are $\mathbb{R}^2 \rtimes O(2)$, $O(3)$ and $PSL(2, \mathbb{R}) \rtimes \mathbb{Z}/2$, all three-dimensional, making each model a homogeneous space $G/O(2)$ and a symmetric space.

The circumference and area of a circle grow as the circular, linear and hyperbolic functions of the radius, so $\pi$ is a geometric constant only in the flat case and the volume of a ball grows polynomially in the flat case and exponentially in the hyperbolic; the Gauss–Bonnet theorem makes the sign of the curvature the sign of the Euler characteristic of a compact surface; and the parallels are one, none or infinitely many according to the sign. Each geometry is consistent relative to the Euclidean, each is unique for its sign of curvature, and the hyperbolic plane cannot be completely embedded in Euclidean three-space, which is why it is studied through its models.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$ | Constant sectional curvature: $+1/R^2$, $0$ or $-1/R^2$ |
| $R = 1/\sqrt{|K|}$ | Radius of the model |
| $S(P, \ell)$ | The lines through $P$ not meeting $\ell$; of size $1$, $0$, $|\mathbb{R}|$ |
| $\Delta$ | Area of a geodesic triangle or polygon |
| $A + B + C = \pi + K\Delta$ | Unified angle-sum formula; spherical excess and hyperbolic defect |
| $s_K(t)$, $c_K(t) = s_K'(t)$ | Model sine and cosine: $\sin/\cos$, $t/1$, $\sinh/\cosh$ |
| $c_K(c) = c_K(a)c_K(b) - Ks_K(a)s_K(b)\cos C$ | Unified law of cosines |
| $\omega^2 = -1, 0, +1$ | The three algebras $\mathbb{C}$, $\mathbb{D}'$, $\mathbb{D}$ and their geometries |
| $SO(2)$, transvections, $SO(1,1)_0$ | Rotation groups of the three geometries |
| $E(2) = \mathbb{R}^2\rtimes O(2)$, $O(3)$, $PSL(2,\mathbb{R})$ | Isometry groups, orientation-preserving versions |
| $G/O(2)$ | The model as a homogeneous and symmetric space |
| $2\pi r$, $2\pi R\sin(r/R)$, $2\pi R\sinh(r/R)$ | Circumference of a circle in the three geometries |
| $\operatorname{vol}B(r)$ | Ball volume: polynomial flat, bounded spherical, exponential hyperbolic |
| $\sum\alpha_i = (n-2)\pi + K\Delta$ | Gauss–Bonnet for a geodesic polygon |
| $\Pi(d) = 2\arctan(e^{-d})$ | Angle of parallelism; hyperbolic only |
| Hilbert's theorem | No complete isometric embedding of $\mathbb{H}^2$ in $\mathbb{R}^3$ |





## Further Reading

- David Hilbert, *Foundations of Geometry* (Open Court, 1902; reprinted by Dover), for the axiomatic framework and the independence of the parallel postulate.
- Marvin J. Greenberg, *Euclidean and Non-Euclidean Geometries: Development and History*, 4th ed. (W. H. Freeman, 2008), for the historical development and the model constructions.
- Nikolai I. Lobachevsky, *Geometrical Researches on the Theory of Parallels* (University of Texas Press, 1891), for the original hyperbolic trigonometry.
- János Bolyai, "The absolute science of space" (Appendix to the *Tentamen*, 1832), for the parallel construction and the hyperbolic trigonometric laws.
- Harold S. M. Coxeter, *Non-Euclidean Geometry*, 6th ed. (Mathematical Association of America, 1998), for a compact comparison of the three geometries.
- John G. Ratcliffe, *Foundations of Hyperbolic Manifolds*, 2nd ed. (Springer, 2006), for the model spaces and the space-form classification.
- David Hilbert, "Über Flächen von konstanter Gaussscher Krümmung", *Transactions of the American Mathematical Society* 2 (1901), 87–99, for the non-embeddability of the hyperbolic plane in Euclidean three-space.
