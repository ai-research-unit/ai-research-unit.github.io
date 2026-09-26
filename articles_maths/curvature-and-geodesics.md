
# __Curvature and Geodesics__

## Introduction

A Riemannian metric is a distance that varies from point to point. It assigns to each tangent space a positive definite inner product, and the assignment varies smoothly; the geometry of the resulting manifold is the study of the consequences of that variation. Three objects carry the whole of the theory. The **Levi-Civita connection** is the unique rule for differentiating vector fields that is compatible with the metric and free of torsion; it makes it possible to compare tangent vectors at different points by **parallel transport**. The **geodesics** are the curves that parallel-transport their own tangent vector, and they are exactly the curves that minimise length locally; they define the **exponential map** of the metric, which is not the exponential map of a Lie algebra. The **curvature** measures the failure of parallel transport to be independent of the path, and it appears in three increasing averages: the **sectional curvature** of a plane, the **Ricci curvature** of a direction, and the **scalar curvature** of a point.

This article develops these objects and explains what each measures. It defines the Levi-Civita connection by the Koszul formula and proves uniqueness; it defines parallel transport and the curvature tensor, and proves the symmetries of the curvature and the two Bianchi identities; it defines the sectional, Ricci and scalar curvatures and states what each detects; it writes the geodesic equation, explains why a geodesic minimises length locally, and contrasts the metric exponential with the Lie-algebra exponential; it treats the three simply connected complete surfaces of constant curvature — elliptic, Euclidean and hyperbolic — and identifies them with the geometries of the three two-dimensional algebras of *The Three Two-Dimensional Algebras and the Three Kinds of Rotation*; and it states the Gauss–Bonnet theorem, which relates the integral of the curvature of a compact surface to its Euler characteristic. The point of the article is the final observation: the topology of a manifold is fixed, but the metric on it is not, and curvature is the invariant that distinguishes two metrics with the same underlying space.

The article assumes *Smooth Manifolds and Differential Geometry* for manifolds, tangent spaces, vector fields and the Riemannian metric; it defines the connection on the tangent bundle, its curvature and the Bianchi identity itself; the quadratic forms of *Bilinear Forms*, *Quadratic Forms and Polarisation* and *Isometries and Orthogonal Transformations*; and *The Three Two-Dimensional Algebras and the Three Kinds of Rotation* for the three model geometries in dimension two. The existence, uniqueness and smooth-dependence theory of the geodesic equation, the first-variation computation and the completeness theory that depend on limits belong to Part III, where the differential equations and the limit are available; they are stated here and not proved. The comparison theorems and the submanifold theory are not developed here, and the systematic account of them is not part of this article. No physics is invoked.

## The Metric as a Distance

### Length and the Riemannian Distance

Let $(M, g)$ be a Riemannian manifold of dimension $n$, with the conventions of *Smooth Manifolds and Differential Geometry*: for each $p \in M$ the bilinear form $g_p$ is a positive definite inner product on $T_pM$, and in a chart with coordinates $x^i$ the coefficients are $g_{ij} = g(\partial_{x^i}, \partial_{x^j})$. The **speed** of a smooth curve $\gamma$ is $|\gamma'|_g = \sqrt{g(\gamma', \gamma')}$ and the **length** is the integral of the speed. The **Riemannian distance** $d_g(p, q)$ is the infimum of the lengths of the piecewise smooth curves joining $p$ to $q$, and it is a metric whose topology is the topology of $M$.

**Definition.** The **volume form** of an oriented Riemannian manifold is the unique $n$-form $\mathrm{vol}_g \in \Omega^n(M)$ that assigns the value $1$ to every positively oriented orthonormal frame; in a positively oriented chart,

$$
\mathrm{vol}_g = \sqrt{\det(g_{ij})}\; dx^1 \wedge \cdots \wedge dx^n .
$$

It is the top form whose integral is the Riemannian volume, and its existence is the form theory.

### The Metric Topology and the Distance Function

**Definition.** The **distance function** from a point $p$ is $r_p(x) = d_g(p, x)$. It is continuous for the metric topology, and it is smooth away from the **cut locus** of $p$, the set of points at which the minimising geodesics from $p$ cease to be minimising; the cut locus is closed and of empty interior, and its complement is star-shaped with respect to $p$ in the sense of the exponential map below.

**Theorem.** The distance function satisfies $|\nabla r_p|_g = 1$ at every point where it is smooth. Its Hessian and its Laplacian are the invariants that carry the curvature: the Hessian comparison theorem and the Laplacian comparison theorem compare them with the corresponding objects of the constant-curvature model, and their proofs are analytic and belong to Part III, where the differential equations are available. The comparison is the analytical form of the statement that curvature controls the rate at which geodesics spread.

The statement is recorded here because it is the bridge between the metric and the curvature. The Laplace–Beltrami operator, of which $\Delta$ is the case, is the Laplace–de Rham operator acting on functions, and the comparison theorems for it are proved in Part III with the differential equations.

## The Levi-Civita Connection

### The Koszul Formula

**Definition.** A **connection** on the tangent bundle $TM$ is an $\mathbb{R}$-bilinear map $\nabla : \mathfrak{X}(M) \times \mathfrak{X}(M) \to \mathfrak{X}(M)$ such that $\nabla_{fX}Y = f\nabla_XY$ and $\nabla_X(fY) = X(f)Y + f\nabla_XY$ for $f \in C^\infty(M)$; it is the covariant derivative specialised to the tangent bundle. It is **metric** if

$$
X\,g(Y, Z) = g(\nabla_XY, Z) + g(Y, \nabla_XZ),
$$

and **torsion-free** if

$$
\nabla_XY - \nabla_YX = [X, Y].
$$

**Theorem (fundamental theorem of Riemannian geometry).** On a Riemannian manifold $(M, g)$ there is exactly one connection $\nabla$ that is metric and torsion-free. It is the **Levi-Civita connection**, and it is determined by the **Koszul formula**

$$
2\,g(\nabla_XY, Z) = X\,g(Y, Z) + Y\,g(Z, X) - Z\,g(X, Y) - g(X, [Y, Z]) + g(Y, [Z, X]) + g(Z, [X, Y]).
$$

**Proof.** The right-hand side is manifestly $\mathbb{R}$-linear in $X$ and, by the Leibniz rule for $X, Y, Z$ acting on functions, it is $C^\infty(M)$-linear in each of $X, Y, Z$. It therefore defines a tensor, and since $g$ is nondegenerate it determines the vector field $\nabla_XY$ uniquely. The two required properties follow by substituting into the formula and cancelling terms: metricity uses the first three terms and the skew symmetry of the bracket, torsion-freeness uses the last three and the identity $[X, Y] = -[Y, X]$. $\square$

**Definition.** In a chart the Christoffel symbols are

$$
\nabla_{\partial_{x^i}}\partial_{x^j} = \sum_k \Gamma^k_{ij}\,\partial_{x^k},
\qquad
\Gamma^k_{ij} = \frac{1}{2}\sum_l g^{kl}\Bigl(\partial_{x^i}g_{jl} + \partial_{x^j}g_{il} - \partial_{x^l}g_{ij}\Bigr),
$$

where $(g^{kl})$ is the inverse matrix of $(g_{ij})$. The connection form of $\nabla$ in the coordinate frame is the matrix $\theta = (\theta^i_{\ j})$ of $1$-forms with $\theta^i_{\ j} = \sum_k \Gamma^i_{jk}dx^k$; the connection-form letter is $\theta$ and not $\omega$, which is reserved for the symplectic form.

### Parallel Transport

**Definition.** A vector field $V$ along a curve $\gamma$ is **parallel** if $\nabla_{\gamma'}V = 0$. For each curve $\gamma : [a, b] \to M$ and each $v \in T_{\gamma(a)}M$ there is a unique parallel field $V$ along $\gamma$ with $V(a) = v$; the proof is the existence and uniqueness theory for the linear equation $\nabla_{\gamma'}V = 0$, which is that of Part III, where the differential equations are available; the **parallel transport** is the linear isomorphism

$$
P_\gamma : T_{\gamma(a)}M \longrightarrow T_{\gamma(b)}M, \qquad P_\gamma(v) = V(b).
$$

The transport is an isometry of tangent spaces because $\nabla$ is metric:

$$
g_{\gamma(b)}\bigl(P_\gamma(v), P_\gamma(w)\bigr) = g_{\gamma(a)}(v, w).
$$

**Proposition.** Parallel transport is invariant under reparametrisation and is compatible with concatenation and reversal of curves. Its dependence on the path is measured by the curvature.

**Proof.** The parallel field along a reparametrised curve is the reparametrised field; concatenation composes the transports and reversal inverts them, since the equation $\nabla_{\gamma'}V = 0$ is preserved by reversing the curve. $\square$

**Definition.** The **holonomy group** of $\nabla$ at $p$ is the group of isometries of $T_pM$ obtained as parallel transport around piecewise smooth loops based at $p$. It is a subgroup of the orthogonal group of the metric at $p$, and the **restricted holonomy group** is the subgroup obtained from loops homotopic to the constant loop. The Lie algebra of the holonomy group is spanned by the curvature endomorphisms, which is the Ambrose–Singer theorem.

## Geodesics and the Metric Exponential

### The Geodesic Equation

**Definition.** A smooth curve $\gamma$ is a **geodesic** if its velocity is parallel along itself,

$$
\nabla_{\gamma'}\gamma' = 0 .
$$

In a chart, writing $\gamma(t) = (x^1(t), \ldots, x^n(t))$, this is the system

$$
\frac{d^2x^k}{dt^2} + \sum_{i, j} \Gamma^k_{ij}\,\frac{dx^i}{dt}\frac{dx^j}{dt} = 0, \qquad k = 1, \ldots, n,
$$

the **geodesic equation**. It is a second-order ordinary differential equation; the *equation* is written here, and its solvability — the existence, uniqueness and smooth dependence on initial conditions of its solutions — is the theory of differential equations and belongs to Part III. What the equation says is that a geodesic is a curve that does not turn: its acceleration in the sense of the connection vanishes.

**Definition.** The **exponential map** of the metric at $p$ is

$$
\exp_p : U_p \subseteq T_pM \longrightarrow M, \qquad \exp_p(v) = \gamma_v(1),
$$

where $U_p$ is the set of vectors $v$ for which the geodesic $\gamma_v$ with $\gamma_v(0) = p$ and $\gamma_v'(0) = v$ is defined up to time $1$. The set $U_p$ is an open neighbourhood of $0$ in $T_pM$ containing a ball of some radius on which the geodesics exist, and $\exp_p$ is a local diffeomorphism at $0$ with $d(\exp_p)_0 = \mathrm{id}_{T_pM}$.

**Theorem (Gauss lemma).** For $v \in U_p$ and $w \in T_{v}(T_pM) \cong T_pM$,

$$
g_{\exp_p(v)}\bigl(d(\exp_p)_v(v),\, d(\exp_p)_v(w)\bigr) = g_p(v, w).
$$

In words, the radial geodesics leave $p$ orthogonally to the spheres of constant radius, and the exponential map is a radial isometry.

**Proof sketch.** The identity is the first-variation computation for the length applied to a geodesic and a variation by a family of geodesics; the derivative of $t \mapsto g(\gamma_v'(t), \partial_s\gamma_s(t))$ at $s = 0$ vanishes because $\gamma_v$ is a geodesic. $\square$

**Definition.** The **normal coordinates** at $p$ are obtained by choosing an orthonormal basis $u_1, \ldots, u_n$ of $T_pM$ and, for a point $x$ near $p$, taking the unique $v \in T_pM$ with $\exp_p(v) = x$ and setting $x^i = v^i$, where $v = \sum_i v^i u_i$. Equivalently, the coordinates are the coefficients of $v$ in the orthonormal basis, so that the geodesic through $p$ in the direction $u_i$ is the $i$-th coordinate axis. In normal coordinates $g_{ij}(p) = \delta_{ij}$ and the first derivatives of $g_{ij}$ vanish at $p$, so the Christoffel symbols vanish at $p$ and the metric is Euclidean to second order there; the second derivatives of the metric at $p$ are exactly the curvature.

### Geodesics Minimise Locally

**Definition.** A curve joining $p$ to $q$ is **locally minimising** if every sufficiently short subarc of it has length not exceeding the length of any nearby curve with the same endpoints.

**Theorem.** Every geodesic is locally minimising. Conversely, a locally minimising curve, parametrised proportionally to arclength and of class $C^2$, satisfies the geodesic equation.

**Proof sketch.** For a geodesic $\gamma$ and a nearby curve $\sigma$ from $\gamma(a)$ to $\gamma(b)$ with $b - a$ small, the comparison formula

$$
L_g(\sigma) - L_g(\gamma) = \tfrac{1}{2}\int_a^b g\!\left(\frac{D}{dt}\,\frac{\partial \sigma}{\partial s}, \frac{\partial\sigma}{\partial s}\right) dt
$$

expresses the length difference, to second order, as the integral of the squared normal component of the variation, which is nonnegative; the converse is the first-variation formula, whose vanishing for all variations supported in the interior is exactly the geodesic equation. Both computations use the calculus of variations of Part III, where the analytic details are supplied; the results are standard. $\square$

**Example (Euclidean and spherical geodesics).** In $\mathbb{R}^n$ with the standard metric the Christoffel symbols vanish, so the geodesics are the straight lines. On the round sphere $S^{n-1}$ the geodesics are the great circles: the intersection of the sphere with a plane through the origin. In the hyperbolic metric $g = (dx_1^2 + \cdots + dx_n^2)/y^2$ on the upper half-space, the geodesics are the vertical lines and the semicircles orthogonal to the boundary.

### The Metric Exponential and the Lie-Algebra Exponential

The exponential map defined here must not be confused with the exponential map of a Lie group. For a Lie group $G$ with Lie algebra $\mathfrak{g}$ and a left-invariant metric, a one-parameter subgroup $t \mapsto \exp(tX)$ of *Lie Groups* is a geodesic of the metric if and only if the metric is **bi-invariant**, and in that case the two exponentials agree: $\exp_e(v) = \exp(v)$ for the identification $T_eG \cong \mathfrak{g}$. For a general left-invariant metric the group exponential and the metric exponential differ, and the geodesics are the solutions of the **Euler–Arnold equation**, whose study belongs to the geometry of Lie groups. The distinction is the reason the two constructions carry the same name: each is the solution of the flow of a natural vector field — the right-invariant field for the group exponential, the geodesic spray for the metric exponential — and they coincide only when the metric is compatible with the group structure in the strongest sense.

## Curvature

### The Curvature Tensor

**Definition.** The **curvature tensor** of the Levi-Civita connection is

$$
R(X, Y)Z = \nabla_X\nabla_YZ - \nabla_Y\nabla_XZ - \nabla_{[X, Y]}Z,
$$

a $(1, 3)$-tensor, and the associated $(0, 4)$-tensor is $R(X, Y, Z, W) = g(R(X, Y)Z, W)$.

The curvature form is read on $TM$: in a coordinate frame the curvature form is the matrix $\mathcal{R} = d\theta + \theta \wedge \theta$, and $R(X, Y)Z$ is its evaluation on $X, Y$ applied to $Z$.

**Theorem (symmetries).** The $(0,4)$-curvature tensor satisfies

$$
R(X, Y, Z, W) = -R(Y, X, Z, W) = -R(X, Y, W, Z) = R(Z, W, X, Y),
$$

the **first Bianchi identity**

$$
R(X, Y, Z, W) + R(Y, Z, X, W) + R(Z, X, Y, W) = 0,
$$

and, for the Levi-Civita connection, the **second Bianchi identity**

$$
(\nabla_X R)(Y, Z)W + (\nabla_Y R)(Z, X)W + (\nabla_Z R)(X, Y)W = 0.
$$

**Proof sketch.** The first symmetry is the definition; the second and third follow from metricity and from the vanishing of the torsion; the first Bianchi identity is the cyclic sum of the three curvature terms, in which the bracket terms cancel by the Jacobi identity; the second Bianchi identity is the exterior covariant derivative identity $d^\nabla \mathcal{R} = 0$, read on the tangent bundle. $\square$

### Sectional Curvature

**Definition.** Let $\sigma \subseteq T_pM$ be a two-dimensional subspace with an orthonormal basis $v, w$. The **sectional curvature** of $\sigma$ is

$$
K(\sigma) = R(v, w, w, v) = g\bigl(R(v, w)w, v\bigr).
$$

The definition is independent of the orthonormal basis chosen, by the symmetries of $R$; for a general basis $v, w$ of $\sigma$,

$$
K(\sigma) = \frac{R(v, w, w, v)}{g(v, v)g(w, w) - g(v, w)^2}.
$$

**Theorem.** The sectional curvature determines the curvature tensor completely: if two $(0,4)$-tensors with the symmetries above have the same sectional curvatures on every two-plane, they are equal. Consequently the curvature of a Riemannian manifold is exactly the assignment to each point and each two-plane of the number $K(\sigma)$.

**Proof sketch.** The symmetries express a $(0,4)$-tensor as a linear combination of the quadrilateral expressions $R(v, w, w, v)$; polarisation in each argument recovers the full tensor from the values of $K$ on the planes. $\square$

**Remark (what $K$ measures).** The sectional curvature is the curvature of the surface swept out by the geodesics in the plane $\sigma$: it is the Gaussian curvature of the two-dimensional submanifold $\exp_p(\sigma \cap U_p)$. Positive $K$ means that nearby geodesics in that plane converge, as they do on the sphere; negative $K$ means that they diverge, as they do in the hyperbolic plane; $K = 0$ means that they neither converge nor diverge, as they do in the Euclidean plane. This is the statement that curvature measures the spreading of geodesics, and it is the model for the Jacobi-field comparison theory.

**Example.** The round sphere $S^n$ of radius $r$ has $K = 1/r^2$ on every plane; Euclidean space has $K = 0$; the hyperbolic space of curvature $-1/r^2$ has $K = -1/r^2$. These are the three simply connected complete manifolds of constant curvature, and by the classification their universal covers exhaust the possibilities.

### Ricci and Scalar Curvature

**Definition.** The **Ricci tensor** is the trace of the curvature over one pair of arguments,

$$
\operatorname{Ric}(X, Y) = \sum_{i=1}^{n} R(e_i, X, Y, e_i),
$$

where $e_1, \ldots, e_n$ is an orthonormal frame; it is a symmetric $(0, 2)$-tensor. The **scalar curvature** is the trace of the Ricci tensor,

$$
S = \sum_{i=1}^{n} \operatorname{Ric}(e_i, e_i).
$$

**Proposition.** In an orthonormal frame, $\operatorname{Ric}(v, v)$ is the sum of the sectional curvatures of the planes spanned by $v$ and the frame vectors orthogonal to $v$. The scalar curvature is the total of the sectional curvatures over an orthonormal basis of two-planes, up to the normalisation of the double count.

**Proof.** Substitute the definition of sectional curvature into the trace: $\operatorname{Ric}(v, v) = \sum_i R(e_i, v, v, e_i) = \sum_i K(e_i \wedge v)$ when the frame is orthonormal and $v$ is one of its members. $\square$

**Remark (what each measures).** The Ricci curvature is the average of the sectional curvatures in the directions orthogonal to $v$, so $\operatorname{Ric}(v, v) > 0$ means that, on average, the geodesics starting in the direction $v$ spread more slowly than in Euclidean space; it is the curvature that controls the growth of the volume element along a geodesic and, through it, the behaviour of the distance function. The scalar curvature is a single number at each point, the weakest of the three invariants, and it is the one that appears in the variational problems of the theory. The chain

$$
R \;\longrightarrow\; K \;\longrightarrow\; \operatorname{Ric} \;\longrightarrow\; S
$$

goes from the complete curvature information to successively averaged shadows of it; each level is the trace of the one before, and each loses information.

### The Second Bianchi Identity and Its Contractions

**Definition.** The **Einstein tensor** is $G = \operatorname{Ric} - \frac{1}{2}S g$.

**Theorem (contracted Bianchi identity).** The divergence of the Einstein tensor vanishes:

$$
\operatorname{div} G = 0, \qquad \text{equivalently} \qquad \sum_i (\nabla_{e_i}\operatorname{Ric})(e_i, X) = \tfrac{1}{2}\,dS(X).
$$

**Proof.** Contract the second Bianchi identity in two pairs of indices. $\square$

The contracted identity is the reason the Einstein tensor is the natural divergence-free object built by tracing the curvature, and it is the curvature equation that the analysis of the metric, in Part III, takes up.

## The Three Constant-Curvature Models

By the classification of the simply connected complete Riemannian manifolds of constant sectional curvature, there are exactly three families, one for each sign of $K$. Each has the geometry of one of the three two-dimensional algebras of *The Three Two-Dimensional Algebras and the Three Kinds of Rotation*, and each is the symmetric space of a classical group.

### The Elliptic Model

**Definition.** The **round sphere** of radius $r$ is

$$
S^n_r = \{x \in \mathbb{R}^{n+1} : \langle x, x\rangle = r^2\}
$$

with the metric induced by the standard inner product. Its sectional curvature is $K = 1/r^2$ on every plane, its geodesics are the great circles, and its isometry group is the orthogonal group $O(n+1)$, acting transitively.

The sphere is compact, its diameter is $\pi r$, and every pair of geodesics meets, so there are no parallel lines: the elliptic geometry is the one in which the parallel postulate fails in the direction of no parallels. In dimension two it is the geometry of the algebra $\mathbb{C}$ with $\omega^2 = -1$, whose rotation group $SO(2)$ is the elliptic rotation group.

### The Euclidean Model

**Definition.** Euclidean space $\mathbb{R}^n$ with the standard metric has $K = 0$ on every plane, its geodesics are the straight lines, and its isometry group is the Euclidean group $E(n) = \mathbb{R}^n \rtimes O(n)$ acting transitively.

It is the geometry in which the parallel postulate holds: through each point outside a given line there is exactly one line not meeting it, and the angle sum of a triangle is $\pi$. In dimension two it is the geometry of the algebra $\mathbb{D}'$ with $\omega^2 = 0$, whose rotation group is the transvection group, the parabolic rotation group.

### The Hyperbolic Model

**Definition.** **Hyperbolic space** $\mathbb{H}^n_r$ is the complete simply connected Riemannian manifold of constant sectional curvature $-1/r^2$; a concrete model is the upper half-space with the metric $g = (dx_1^2 + \cdots + dx_n^2)/y^2$, whose geodesics are the vertical lines and the semicircles orthogonal to the boundary.

Hyperbolic space is non-compact, its geodesics diverge exponentially, and through each point outside a given geodesic there are infinitely many geodesics not meeting it: the parallel postulate fails in the direction of too many parallels, and the angle sum of a triangle is less than $\pi$. In dimension two it is the geometry of the algebra $\mathbb{D}$ with $\omega^2 = +1$, whose identity component of the rotation group is $SO(1,1)_0$, the hyperbolic rotation group. The metric is developed.

### The Comparison Table

| Model | $K$ | Geodesics | Parallel postulate | Angle sum of a triangle | Isometry group | Algebra |
|---|---|---|---|---|---|---|
| Elliptic $S^n_r$ | $+1/r^2$ | great circles | no parallels | $> \pi$ | $O(n+1)$ | $\mathbb{C}$ |
| Euclidean $\mathbb{R}^n$ | $0$ | straight lines | exactly one parallel | $= \pi$ | $\mathbb{R}^n \rtimes O(n)$ | $\mathbb{D}'$ |
| Hyperbolic $\mathbb{H}^n_r$ | $-1/r^2$ | lines and semicircles | infinitely many parallels | $< \pi$ | $O(n,1)$ | $\mathbb{D}$ |

The table is the reason the three two-dimensional algebras of *The Three Two-Dimensional Algebras and the Three Kinds of Rotation* are the three model geometries: the sign of the square of their generator is the sign of the curvature of the geometry their rotation group implements.

## The Gauss–Bonnet Theorem

### The Surface Case

**Theorem (Gauss–Bonnet).** Let $M$ be a compact oriented Riemannian surface with Gaussian curvature $K$ and Euler characteristic $\chi(M)$. Then

$$
\int_M K\, \mathrm{vol}_g = 2\pi\,\chi(M).
$$

**Proof sketch.** For a geodesic triangle with interior angles $\alpha, \beta, \gamma$ the Gauss–Bonnet formula with boundary is $\int_T K\,\mathrm{vol}_g = \alpha + \beta + \gamma - \pi$; triangulating the surface and summing, the boundary terms cancel in pairs and the angle sums contribute $2\pi$ times the alternating count of the vertices, faces and edges, which is $2\pi\chi(M)$. $\square$

**Corollary (angle sums).** A geodesic triangle in the sphere of radius $1$ has angle sum $\pi + \mathrm{area}$; a Euclidean triangle has angle sum $\pi$; a hyperbolic triangle has angle sum $\pi - \mathrm{area}$. This is the quantitative form of the comparison table above: the sign of $K$ is the sign of the deviation of the angle sum from $\pi$.

**Corollary (topological obstruction).** A compact surface admits a metric of constant curvature $+1$ only if $\chi(M) > 0$, a metric of curvature $0$ only if $\chi(M) = 0$, and a metric of constant curvature $-1$ only if $\chi(M) < 0$. The Euler characteristic therefore obstructs the existence of the three geometries, and the classification of the compact surfaces with these geometries is the uniformisation stated.

### The Higher-Dimensional Case

**Theorem (generalised Gauss–Bonnet–Chern).** Let $M$ be a compact oriented Riemannian manifold of even dimension $2k$. Then the integral of the Pfaffian of the curvature form,

$$
\int_M \operatorname{Pf}\!\left(\frac{\mathcal{R}}{2\pi}\right) = \chi(M),
$$

equals the Euler characteristic.

The form $\operatorname{Pf}(\mathcal{R}/2\pi)$ is the Euler class of the tangent bundle constructed by the Chern–Weil homomorphism, and the theorem identifies its integral with the topological Euler characteristic. In dimension two it reduces to the surface case above.

**Remark (curvature and topology).** The Gauss–Bonnet theorem is the first and simplest instance of a general principle: the integral of a curvature expression is a topological invariant. The principle is made systematic by the Chern–Weil construction, which turns invariant polynomials in the curvature of any connection into characteristic classes of the bundle, and it is the reason curvature, although it is a local differential-geometric datum, computes global topological information. The shape of the metric — which curves are geodesics, how fast they spread, where they focus — is what separates one geometry from another on the same manifold; the topology is what the integral of the curvature cannot change.

## Summary

On a Riemannian manifold the metric defines a length for each curve and a distance for each pair of points, whose topology is the topology of the manifold. The fundamental theorem of Riemannian geometry gives a unique metric and torsion-free connection, the Levi-Civita connection, determined by the Koszul formula and read in a chart from the Christoffel symbols. The connection defines parallel transport, an isometry of tangent spaces along each curve, whose path-dependence is the curvature; the holonomy group consists of the transports around loops and its Lie algebra is spanned by the curvature.

A geodesic is a curve whose velocity is parallel along itself; it satisfies the second-order geodesic equation, and it is exactly the locally length-minimising curve. The metric exponential map sends a tangent vector to the endpoint of the geodesic it generates, and it is a local diffeomorphism whose derivative at the origin is the identity; the Gauss lemma makes the radial geodesics orthogonal to the geodesic spheres. Normal coordinates make the metric Euclidean to first order at a point, with the curvature appearing in the second order. The metric exponential agrees with the Lie-algebra exponential exactly for a bi-invariant metric; the general relation is the Euler–Arnold equation.

The curvature tensor has the algebraic symmetries of a curvature form and satisfies the first and second Bianchi identities. The sectional curvature of a plane is the Gaussian curvature of the surface it sweeps out and measures the convergence or divergence of geodesics in that plane; the Ricci tensor is its average over the directions orthogonal to a given vector and controls the growth of the volume element; the scalar curvature is the trace of the Ricci tensor and is the weakest of the three. The contraction of the second Bianchi identity says that the Einstein tensor $\operatorname{Ric} - \frac{1}{2}Sg$ has vanishing divergence.

The complete simply connected manifolds of constant curvature are the round sphere ($K = 1/r^2$), Euclidean space ($K = 0$) and hyperbolic space ($K = -1/r^2$), the three model geometries whose two-dimensional cases are the geometries of the algebras $\mathbb{C}$, $\mathbb{D}'$ and $\mathbb{D}$. The Gauss–Bonnet theorem integrates the curvature of a compact oriented surface to $2\pi$ times its Euler characteristic and, in its generalised form, identifies the integral of the Pfaffian of the curvature form with the Euler characteristic in every even dimension; it is the first instance of the principle that an integral of curvature is a topological invariant, and it shows that the topology constrains, while the metric realises, the geometry.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(M, g)$, $g_{ij}$, $g^{ij}$ | Riemannian manifold; metric coefficients and their inverse matrix |
| $\nabla$, $\nabla_XY$ | Levi-Civita connection; covariant derivative of $Y$ along $X$ |
| $\theta = (\theta^i_{\ j})$, $\Gamma^k_{ij}$ | Connection form and Christoffel symbols; $\theta$ is the connection-form letter of half A |
| $P_\gamma$ | Parallel transport along the curve $\gamma$; an isometry of tangent spaces |
| $\operatorname{Hol}_p$ | Holonomy group at $p$; its Lie algebra is spanned by the curvature |
| $R(X,Y)Z = \nabla_X\nabla_YZ - \nabla_Y\nabla_XZ - \nabla_{[X,Y]}Z$ | Curvature tensor |
| $\mathcal{R} = d\theta + \theta\wedge\theta$ | Curvature $2$-form, matrix-valued, in a frame; no bare $\Omega$ is used |
| $K(\sigma) = R(v,w,w,v)$ | Sectional curvature of the two-plane $\sigma$ with orthonormal basis $v,w$ |
| $\operatorname{Ric}(X,Y) = \sum_i R(e_i,X,Y,e_i)$ | Ricci tensor; average of sectional curvatures |
| $S = \sum_i \operatorname{Ric}(e_i,e_i)$ | Scalar curvature |
| $G = \operatorname{Ric} - \frac12 Sg$ | Einstein tensor; $\operatorname{div} G = 0$ |
| $\nabla_{\gamma'}\gamma' = 0$ | Geodesic equation in invariant form |
| $\ddot x^k + \sum_{ij}\Gamma^k_{ij}\dot x^i\dot x^j = 0$ | Geodesic equation in a chart |
| $\exp_p : T_pM \to M$ | Exponential map of the metric; $d(\exp_p)_0 = \mathrm{id}$ |
| Gauss lemma | $g(d\exp_p(v), d\exp_p(w)) = g(v,w)$ for the radial direction |
| Normal coordinates | Coordinates in which $g_{ij}(p) = \delta_{ij}$ and $\partial_k g_{ij}(p) = 0$ |
| $\mathrm{vol}_g = \sqrt{\det(g_{ij})}\,dx^1\wedge\cdots\wedge dx^n$ | Riemannian volume form |
| $K = 1/r^2,\ 0,\ -1/r^2$ | Curvatures of the elliptic, Euclidean and hyperbolic models |
| $S^n_r$, $\mathbb{H}^n_r$ | Round sphere and hyperbolic space of radius $r$ |
| $\int_M K\,\mathrm{vol}_g = 2\pi\chi(M)$ | Gauss–Bonnet theorem for a compact oriented surface |
| $\operatorname{Pf}(\mathcal{R}/2\pi)$ | Pfaffian form; its integral is the Euler characteristic |



## Further Reading

- Manfredo P. do Carmo, *Riemannian Geometry* (Birkhäuser, 1992), for the Levi-Civita connection, geodesics, curvature and the Gauss–Bonnet theorem.
- John M. Lee, *Introduction to Riemannian Manifolds*, 2nd ed. (Springer, 2018), for a complete modern treatment with normal coordinates and Jacobi fields.
- Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry, Volume I* (Interscience, 1963), for connections, holonomy and the structure equations.
- Michael Spivak, *A Comprehensive Introduction to Differential Geometry, Volume II* (Publish or Perish, 3rd ed. 1999), for the classical development of curvature and geodesics.
- Barrett O'Neill, *Semi-Riemannian Geometry with Applications to Relativity* (Academic Press, 1983), for the same theory with an indefinite metric.
- Shiing-Shen Chern, "A simple intrinsic proof of the Gauss–Bonnet formula for closed Riemannian manifolds", *Annals of Mathematics* 45 (1944), 747–752, for the generalised Gauss–Bonnet theorem.
- Richard S. Hamilton, "Three-manifolds with positive Ricci curvature", *Journal of Differential Geometry* 17 (1982), 255–306, for the Ricci flow that the Ricci curvature generates.
