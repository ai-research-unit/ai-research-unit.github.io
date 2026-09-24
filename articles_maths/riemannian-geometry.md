
# __Riemannian Geometry__

## Introduction

Riemannian geometry is the systematic study of a smooth manifold equipped with a positive definite metric. It is the point at which the linear algebra of the tangent spaces, the differential topology of the manifold, and the metric structure of Part II meet: the metric is a smooth field of inner products, the connection it determines is the unique one compatible with both the metric and the smooth structure, and the curvature of that connection is the invariant that distinguishes one metric on a manifold from another. This article is the reference for the metric, the Levi-Civita connection and the curvature; the companion article *Curvature and Geodesics* develops the same objects with an emphasis on what each curvature measures and on the three constant-curvature models, and the two are to be read together.

The article develops the theory in the order in which it is used. It defines Riemannian metrics, isometries and the induced distance; constructs the Levi-Civita connection and derives the curvature tensor with all its symmetries and the two Bianchi identities; defines the sectional, Ricci and scalar curvatures and proves Schur's theorem that a pointwise-constant sectional curvature is constant on a connected manifold of dimension at least three; treats geodesics, the exponential map, normal coordinates, the cut locus and the Hopf–Rinow theorem; develops Jacobi fields and the comparison theorems — the Rauch, Bonnet–Myers, Cartan–Hadamard and Hadamard theorems and Cartan's theorem on the determination of a manifold by its curvature; proves the Myers–Steenrod theorem that the isometry group of a Riemannian manifold is a Lie group; classifies the spaces of constant curvature; and treats submanifolds through the second fundamental form and the Gauss equation, ending with the Gauss–Bonnet theorem.

The article assumes *Smooth Manifolds and Differential Geometry* for manifolds, tangent spaces and the metric; it constructs the Levi–Civita connection and derives the curvature tensor, the structure equation and the Bianchi identity itself; the Chern–Weil construction is not used; uses *Curvature and Geodesics*, an earlier article of the same category, for the interpretation of the curvature invariants and the model geometries; the quadratic form theory of *Bilinear Forms*, *Quadratic Forms and Polarisation* and *Isometries and Orthogonal Transformations*; and the Lie group theory of *Lie Groups* and *The Lie Correspondence and the Adjoint Representation* for the isometry-group theorem. The solvability of the geodesic and Jacobi equations and the analytic core of the comparison theorems belong to Part III, where the differential equations and the limit are available, and they are stated here with proof sketches only. The metric is the base on which the complex, Hermitian, Kähler, quaternionic and hyperkähler structures are laid; those are developed in the articles of the same category being written in parallel, and they cite this one for the metric, the connection and the curvature. No physics is invoked.

## Riemannian Metrics and the Metric Structure

### Metrics and Isometries

**Definition.** A **Riemannian metric** on a smooth manifold $M$ is a smooth section $g$ of the bundle $S^2T^*M$ of symmetric bilinear forms such that $g_p$ is positive definite on $T_pM$ for every $p$. A **Riemannian manifold** is a pair $(M, g)$, and $n = \dim M$. In a chart with coordinates $x^i$ the **first fundamental form** is $ds^2 = \sum_{ij} g_{ij}\,dx^i dx^j$ with $g_{ij} = g(\partial_{x^i}, \partial_{x^j})$, a symmetric positive definite matrix of smooth functions, and the metric determines and is determined by these coefficients with the transformation law

$$
g'_{kl} = \sum_{ij} g_{ij}\,\frac{\partial x^i}{\partial y^k}\frac{\partial x^j}{\partial y^l}
$$

under a change of coordinates.

**Theorem.** Every smooth manifold carries a Riemannian metric, and the metrics on a fixed manifold form a convex set: if $g_1$ and $g_2$ are metrics and $t \in [0, 1]$ then $(1-t)g_1 + tg_2$ is a metric.

**Proof.** Existence is the partition-of-unity construction of *Smooth Manifolds and Differential Geometry*; convexity is immediate from the positivity and symmetry of the linear combination. $\square$

**Definition.** Let $(M, g)$ and $(N, h)$ be Riemannian manifolds. A smooth map $F : M \to N$ is a **local isometry** if $F^*h = g$, that is if

$$
h_{F(p)}\bigl(dF_p(v), dF_p(w)\bigr) = g_p(v, w)
$$

for all $p$ and all $v, w \in T_pM$; it is an **isometry** if in addition it is a diffeomorphism. The isometries of $(M, g)$ form a group $\operatorname{Isom}(M, g)$ under composition, and a local isometry is an isometry onto its image.

**Definition.** $(M, g)$ and $(N, h)$ are **isometric** if there is an isometry between them, and **locally isometric** if every point of $M$ has a neighbourhood isometric to an open set of $N$. A **flat** manifold is one locally isometric to Euclidean space.

**Theorem.** A local isometry preserves the Levi-Civita connection, the curvature tensor, the geodesics and the length of every curve; an isometry preserves the distance, $d_h(F(p), F(q)) = d_g(p, q)$.

**Proof.** The pullback of the Levi-Civita connection of $h$ along a local isometry is a metric and torsion-free connection on $M$, hence equals the Levi-Civita connection of $g$ by uniqueness; the curvature is natural for the connection, and the geodesic equation is therefore preserved; length is preserved by the definition of the pullback metric. $\square$

### The Riemannian Distance

**Definition.** The **length** of a piecewise smooth curve $\gamma : [a, b] \to M$ is

$$
L_g(\gamma) = \int_a^b \sqrt{g_{\gamma(t)}(\gamma'(t), \gamma'(t))}\, dt,
$$

and the **Riemannian distance** is

$$
d_g(p, q) = \inf\{ L_g(\gamma) : \gamma \text{ piecewise smooth from } p \text{ to } q \}.
$$

**Theorem.** The distance $d_g$ is a metric, its metric topology is the topology of $M$, and a distance-preserving bijection $M \to M$ is automatically smooth and hence an isometry.

**Proof sketch.** The metric axioms and the topology statement are as in *Smooth Manifolds and Differential Geometry*. For the second statement, a distance-preserving map preserves the length of every curve, so it preserves the geodesics and the exponential map; since $\exp_p$ is a local diffeomorphism, the map is smooth in normal coordinates. $\square$

**Definition.** The **diameter** of a Riemannian manifold is $\operatorname{diam}(M, g) = \sup_{p,q} d_g(p, q) \in [0, \infty]$, and the **volume** is the integral $\int_M \mathrm{vol}_g$ of the volume form when $M$ is oriented and the integral converges.

## Connections and Curvature

### The Levi-Civita Connection

**Definition.** A connection $\nabla$ on $TM$ is **metric** if $X\,g(Y, Z) = g(\nabla_XY, Z) + g(Y, \nabla_XZ)$ and **torsion-free** if $\nabla_XY - \nabla_YX = [X, Y]$.

**Theorem (fundamental theorem).** On a Riemannian manifold there is exactly one connection that is both metric and torsion-free, the **Levi-Civita connection**, given by the Koszul formula

$$
2\,g(\nabla_XY, Z) = X\,g(Y, Z) + Y\,g(Z, X) - Z\,g(X, Y) - g(X, [Y, Z]) + g(Y, [Z, X]) + g(Z, [X, Y]).
$$

**Proof.** The right-hand side is $C^\infty(M)$-linear in $X, Y, Z$, hence a tensor, and nondegeneracy of $g$ determines $\nabla_XY$; the two properties follow by substitution, the metricity from the first three terms and the torsion-freeness from the last three. $\square$

**Definition.** In a coordinate frame the connection is described by the **Christoffel symbols**

$$
\Gamma^k_{ij} = \frac{1}{2}\sum_l g^{kl}\bigl(\partial_{x^i}g_{jl} + \partial_{x^j}g_{il} - \partial_{x^l}g_{ij}\bigr),
$$

which are symmetric in $i, j$, and the connection form is $\theta^i_{\ j} = \sum_k \Gamma^i_{jk}dx^k$.

**Remark.** The symmetry $\Gamma^k_{ij} = \Gamma^k_{ji}$ is exactly the torsion-freeness, and the vanishing of $\nabla g$ is exactly the metricity. Both are visible in the Koszul formula and neither survives if the metric is dropped: a general connection has neither property, and the pair of properties is what makes the Levi-Civita connection canonical.

### The Curvature Tensor

**Definition.** The **curvature tensor** is

$$
R(X, Y)Z = \nabla_X\nabla_YZ - \nabla_Y\nabla_XZ - \nabla_{[X, Y]}Z,
$$

and $R(X, Y, Z, W) = g(R(X, Y)Z, W)$ is its fully covariant form. The curvature form in a frame is $\mathcal{R} = d\theta + \theta\wedge\theta$, by the structure equation, and $\Omega$ is never used for it here.

**Theorem (symmetries and Bianchi identities).**

**(a)** $R(X, Y) = -R(Y, X)$ and $R(X, Y, Z, W) = -R(X, Y, W, Z)$, hence $R(X, Y, Z, Z) = 0$.

**(b)** $R(X, Y, Z, W) = R(Z, W, X, Y)$.

**(c)** $R(X, Y, Z, W) + R(Y, Z, X, W) + R(Z, X, Y, W) = 0$ (first Bianchi identity).

**(d)** $(\nabla_XR)(Y, Z) + (\nabla_YR)(Z, X) + (\nabla_ZR)(X, Y) = 0$ as operators, the second Bianchi identity.

**Proof.** Antisymmetry is the definition and the metricity; the symmetry in the pairs follows by writing the first Bianchi identity in the $(0,4)$ form and combining the permutations; the first Bianchi identity is the cyclic sum of $\nabla_X\nabla_YZ$ in which the bracket terms cancel by the Jacobi identity of the Lie bracket; the second is $d^\nabla\mathcal{R} = 0$, the Bianchi identity stated as standard. $\square$

**Definition.** The **curvature operator** is $R(X, Y)$ as an endomorphism of $TM$; the tensor has $\frac{1}{12}n^2(n^2-1)$ independent components, the number left by the symmetries.

### The Three Curvatures

**Definition.** For a two-plane $\sigma \subseteq T_pM$ with basis $v, w$, the **sectional curvature** is

$$
K(\sigma) = \frac{R(v, w, w, v)}{g(v,v)g(w,w) - g(v,w)^2};
$$

the **Ricci tensor** is $\operatorname{Ric}(X, Y) = \sum_i R(e_i, X, Y, e_i)$ for an orthonormal frame $e_i$; and the **scalar curvature** is $S = \sum_i \operatorname{Ric}(e_i, e_i)$. The manifold is **Einstein** if $\operatorname{Ric} = \lambda g$ for a function $\lambda$, and in that case $\lambda = S/n$ and $S$ is constant when $n \geq 3$ and the manifold is connected.

**Theorem (Schur).** If $n \geq 3$ and the sectional curvature $K(\sigma)$ depends only on the point $p$, not on the two-plane $\sigma$, then $K$ is constant on a connected manifold.

**Proof sketch.** The contraction of the second Bianchi identity gives

$$
dS = 2\sum_i (\nabla_{e_i}\operatorname{Ric})(e_i, \cdot\,).
$$

If the curvature is isotropic with value $K$ at each point then $\operatorname{Ric} = (n-1)Kg$ and $S = n(n-1)K$, so the two sides are $n(n-1)\,dK$ and $2(n-1)\,dK$; comparing them gives $(n-1)(n-2)\,dK = 0$, so a connected manifold of dimension $n \geq 3$ has constant $K$. $\square$

**Proposition.** In dimension two the sectional curvature is a function $K : M \to \mathbb{R}$, the Gaussian curvature, and the curvature tensor is determined by it; in dimension three the curvature is determined by the Ricci tensor.

**Proof.** The symmetries of $R$ leave one independent component in dimension two and the Ricci tensor in dimension three; in dimension two the single value is $K$ itself, and in dimension three the map from curvature to Ricci is injective, since the Weyl tensor vanishes. $\square$

## Geodesics, the Exponential Map and Completeness

### Geodesics and the Exponential Map

**Definition.** A **geodesic** is a curve with $\nabla_{\gamma'}\gamma' = 0$; in a chart it satisfies $\ddot x^k + \sum_{ij}\Gamma^k_{ij}\dot x^i\dot x^j = 0$. A geodesic is **complete** if it is defined for all real $t$. The **exponential map** at $p$ is $\exp_p(v) = \gamma_v(1)$ for the maximal geodesic with $\gamma_v(0) = p$, $\gamma_v'(0) = v$, and the manifold is **geodesically complete** if $\exp_p$ is defined on all of $T_pM$ for one, hence every, $p$.

**Theorem.** Every geodesic has constant speed: $g(\gamma', \gamma')$ is constant along $\gamma$, and a geodesic parametrised by arclength is locally minimising.

**Proof.** Differentiate $g(\gamma', \gamma')$ along $\gamma$ and use metricity and the geodesic equation:

$$
\frac{d}{dt}g(\gamma', \gamma') = 2g(\nabla_{\gamma'}\gamma', \gamma') = 0 .
$$

The local minimising property is the Gauss lemma and the first-variation computation of *Curvature and Geodesics*. $\square$

**Definition.** The **normal coordinates** at $p$ are the coordinates $x^i$ defined by $x = \exp_p(v)$, $x^i = v^i$ for an orthonormal basis $e_i$ of $T_pM$. In them $g_{ij}(p) = \delta_{ij}$, $\partial_k g_{ij}(p) = 0$, and

$$
g_{ij}(x) = \delta_{ij} - \frac{1}{3}\sum_{k,l} R_{ikjl}(p)\,x^kx^l + O(|x|^3),
$$

where $R_{ikjl} = R(e_i, e_k, e_j, e_l)$; the curvature is exactly the second-order term.

### Completeness and the Hopf–Rinow Theorem

**Definition.** A Riemannian manifold is **metrically complete** if $(M, d_g)$ is a complete metric space in the sense of *Metric, Uniform and Complete Spaces*, and **finitely compact** if every closed bounded subset is compact.

**Theorem (Hopf–Rinow).** For a connected Riemannian manifold $(M, g)$ the following are equivalent:

**(a)** $(M, d_g)$ is complete;

**(b)** $M$ is geodesically complete;

**(c)** every closed bounded subset of $M$ is compact;

and any of them implies that every pair of points is joined by a minimising geodesic.

**Proof sketch.** Completeness implies geodesic completeness because a geodesic that existed only up to a finite time $\tau$ would make the points $\gamma(t_n)$ a Cauchy sequence with no limit in $M$; geodesic completeness gives finite compactness because a bounded set is contained in a geodesic ball $\exp_p(\overline{B}(0, r))$, whose image is compact; finite compactness gives completeness because a Cauchy sequence is bounded and has a convergent subsequence; and if the distance from $p$ to $q$ is $d$, a minimising sequence of curves gives directions whose exponential images converge, and the limit is a minimising geodesic. The argument uses the local compactness of the exponential map and the limit of a sequence, which belongs to Part III. $\square$

**Definition.** The **cut locus** of $p$ is the set of points $\exp_p(v)$ such that the geodesic $t \mapsto \exp_p(tv)$ is minimising on $[0, 1]$ but not on $[0, 1 + \epsilon]$. The **injectivity radius** at $p$ is the largest $r$ with $\exp_p$ injective on the ball of radius $r$ in $T_pM$; the **injectivity radius** of $M$ is the infimum over $p$.

**Theorem.** The exponential map at $p$ is a diffeomorphism from the open ball of radius $\operatorname{inj}(p)$ onto its image; on that ball the distance from $p$ is realised by the radial geodesics and the metric is the pullback of the Euclidean metric along the exponential, up to the curvature correction displayed above.

**Proof sketch.** Beyond the injectivity radius two geodesics meet, and the minimising property fails at the first conjugate point or the first self-intersection; within it, the Gauss lemma shows the exponential is a radial isometry and a local diffeomorphism, and injectivity makes it a diffeomorphism. $\square$

## Jacobi Fields and Comparison Theorems

### Jacobi Fields

**Definition.** A **Jacobi field** along a geodesic $\gamma$ is a vector field $J$ along $\gamma$ satisfying the **Jacobi equation**

$$
\frac{D^2J}{dt^2} + R(J, \gamma')\gamma' = 0 ,
$$

where $D/dt$ is the covariant derivative along $\gamma$. The Jacobi equation is the linearisation of the geodesic equation: $J$ is the variation field of a family of geodesics, $\partial_s\gamma_s$ at $s = 0$.

**Proposition.** The Jacobi fields along a geodesic form a real vector space of dimension $2n$, and the map from a Jacobi field to its initial data $(J(0), \tfrac{DJ}{dt}(0))$ is a linear isomorphism onto $T_{\gamma(0)}M \oplus T_{\gamma(0)}M$.

**Proof.** The Jacobi equation is a second-order linear ordinary differential equation, and the existence and uniqueness theory of Part III identifies its solution space with the space of initial data; the equation is that of the linearisation of the geodesic flow. $\square$

**Definition.** Points $p = \gamma(0)$ and $q = \gamma(t_0)$ are **conjugate along $\gamma$** if there is a nonzero Jacobi field along $\gamma$ vanishing at $t = 0$ and $t = t_0$. The **multiplicity** is the dimension of the space of such fields.

**Theorem.** A geodesic is minimising up to but not beyond its first conjugate point: if $q$ is the first conjugate point of $p$ along $\gamma$, then $\gamma$ is the unique minimiser from $p$ to $q$, and no geodesic from $p$ to a point beyond $q$ on $\gamma$ is minimising.

**Proof sketch.** The second variation of length along a geodesic with a Jacobi field vanishing at the endpoints is negative when a conjugate point lies between, which is the classical index-form argument of the calculus of variations; it belongs to Part III. $\square$

### The Comparison Theorems

**Theorem (Rauch).** Let $\gamma$ be a geodesic in $(M, g)$ and let $\tilde\gamma$ be a geodesic in a manifold $(\tilde M, \tilde g)$ of constant curvature $\tilde K$, with $|\gamma'(0)| = |\tilde\gamma'(0)|$ and $\tilde K \geq K$ along the corresponding planes. Then the norm of a Jacobi field $J$ along $\gamma$ with $J(0) = 0$ and $|DJ/dt(0)| = 1$ is bounded below by the corresponding norm in the comparison manifold for as long as the comparison field exists, and dually if $\tilde K \leq K$.

In the constant-curvature model the comparison fields are explicit: with $s(t)$ for the solution of the model Jacobi equation,

$$
s_{\tilde K}(t) = \begin{cases} \sin(t\sqrt{\tilde K})/\sqrt{\tilde K}, & \tilde K > 0, \\ t, & \tilde K = 0, \\ \sinh(t\sqrt{-\tilde K})/\sqrt{-\tilde K}, & \tilde K < 0. \end{cases}
$$

**Proof sketch.** One compares the two scalar functions $|J|^2$ and the model $s^2$ by means of the Riccati equation satisfied by the logarithmic derivative of $|J|$ and the Sturm comparison theorem for ordinary differential equations; the argument belongs to Part III. $\square$

**Theorem (Bonnet–Myers).** If $(M, g)$ is complete and connected of dimension $n$ and there is a constant $k > 0$ with $\operatorname{Ric}(v, v) \geq (n-1)k$ for every unit $v$ and every point, then $M$ is compact, its diameter is at most $\pi/\sqrt{k}$, its fundamental group is finite, and its universal cover is compact.

**Proof sketch.** The Rauch comparison applied to the average of the sectional curvatures along a geodesic shows that a geodesic of length $\pi/\sqrt{k}$ has a conjugate point; by the minimising theorem it is not minimising, so the diameter is bounded; Hopf–Rinow then makes the manifold compact. Finiteness of the fundamental group follows from the compactness of the universal cover and the fact that the covering group acts properly discontinuously. $\square$

**Theorem (Cartan–Hadamard).** If $(M, g)$ is complete, connected and simply connected with $K \leq 0$ everywhere, then $\exp_p : T_pM \to M$ is a diffeomorphism for every $p$, and $M$ is diffeomorphic to $\mathbb{R}^n$.

**Proof sketch.** Nonpositive curvature makes the comparison field $s(t) = t$ grow at least linearly, so no Jacobi field vanishes twice and there are no conjugate points; the exponential is then a local diffeomorphism with no critical points, and a covering map, which is injective when the manifold is simply connected. The result is the Hadamard theorem, and the version for $K < 0$ is Cartan's. $\square$

**Theorem (Cartan, on curvature determination).** Let $M$ and $\tilde M$ be complete connected Riemannian manifolds of the same dimension and let $F : T_pM \to T_{\tilde p}\tilde M$ be a linear isometry such that the curvature tensors correspond, $F^*\tilde R = R$ in the sense of parallel transport along geodesics from $p$ and $\tilde p$. Then there is a local, and by completeness global, isometry $\varphi : M \to \tilde M$ with $d\varphi_p = F$. In particular a complete simply connected manifold of constant sectional curvature $k$ is isometric to the model space of curvature $k$, and this determines it up to isometry.

**Proof sketch.** Define $\varphi = \exp_{\tilde p} \circ F \circ \exp_p^{-1}$ and show by the Jacobi equation that $\varphi$ is a local isometry; the comparison of the curvature tensors is what makes the Jacobi fields correspond. $\square$

**Corollary.** The complete simply connected manifolds of constant sectional curvature $k$ are exactly the round sphere of radius $1/\sqrt k$ for $k > 0$, Euclidean space for $k = 0$, and hyperbolic space of curvature $k$ for $k < 0$; up to isometry and scaling there are therefore exactly three.

## Isometries and the Myers–Steenrod Theorem

**Definition.** A **Killing field** on $(M, g)$ is a vector field $X$ whose local flow consists of local isometries, equivalently

$$
g(\nabla_YX, Z) + g(Y, \nabla_ZX) = 0
$$

for all $Y, Z$; the Killing fields form a Lie algebra $\mathfrak{isom}(M, g)$ under the bracket.

**Definition.** The isometry group $\operatorname{Isom}(M, g)$ is given the compact-open topology, equivalently the topology of uniform convergence on compact sets; the group is closed in the group of homeomorphisms of $M$ and acts on $M$ continuously.

**Theorem (Myers–Steenrod).** The isometry group of a connected Riemannian manifold is a Lie group, its action on $M$ is smooth, and its Lie algebra is the Lie algebra of Killing fields.

**Proof sketch.** Fix $p$ and choose an orthonormal frame at $p$; an isometry is determined by its value at $p$ and its differential there, so the group embeds in the bundle of orthonormal frames, which is a smooth manifold; the image is the set of frames of the form $(F(p), dF_p(e_i))$ for $F \in \operatorname{Isom}$, and this set is closed and defined by smooth equations, so it is a submanifold. The smooth action and the Lie algebra statement follow from the exponential map. $\square$

**Corollary.** The isometry group is a closed subgroup of the bundle of orthonormal frames, hence is a Lie group; for a compact manifold the group is compact. The isometries of the model spaces are the orthogonal, Euclidean and pseudo-orthogonal groups $O(n+1)$, $\mathbb{R}^n\rtimes O(n)$ and $O(n,1)$.

## Submanifolds and the Second Fundamental Form

### The Gauss Formula and the Second Fundamental Form

Let $S \subseteq M$ be a regular submanifold of a Riemannian manifold $(M, g)$, with the induced metric, and let $\nabla$ and $\nabla^S$ be the Levi-Civita connections of $M$ and of $S$.

**Definition.** The **second fundamental form** is the symmetric $(0,2)$-tensor on $S$ with values in the normal bundle,

$$
\mathrm{II}(X, Y) = \bigl(\nabla_XY\bigr)^{\perp}, \qquad X, Y \in \mathfrak{X}(S),
$$

the normal component of the covariant derivative in $M$; the **Gauss formula** is

$$
\nabla_XY = \nabla^S_XY + \mathrm{II}(X, Y).
$$

For a hypersurface with a chosen unit normal $N$, the scalar form is $\mathrm{II}(X, Y) = h(X, Y)N$ and $h(X, Y) = g(\nabla_XY, N)$.

**Theorem (Gauss equation).** For all $X, Y, Z, W \in \mathfrak{X}(S)$,

$$
g^S\bigl(R^S(X, Y)Z, W\bigr) = g\bigl(R(X, Y)Z, W\bigr) + g\bigl(\mathrm{II}(X, Z), \mathrm{II}(Y, W)\bigr) - g\bigl(\mathrm{II}(X, W), \mathrm{II}(Y, Z)\bigr).
$$

**Proof.** Substitute the Gauss formula into the definition of $R^S$ and take the tangential part. $\square$

**Corollary (theorema egregium).** The Gaussian curvature of a surface in $\mathbb{R}^3$ is an intrinsic invariant: in the notation of the Gauss equation, $K^S = \det(\mathrm{II})$ for a surface with the principal curvatures as eigenvalues of the shape operator, and $K^S$ is determined by the metric alone.

**Proof.** In $\mathbb{R}^3$ the curvature $R$ of the ambient space vanishes, so the Gauss equation gives $K^S = g(\mathrm{II}(X, X), \mathrm{II}(Y, Y)) - |\mathrm{II}(X, Y)|^2$ for an orthonormal basis $X, Y$ of the tangent plane, which depends only on the induced metric. $\square$

**Definition.** The **mean curvature** of a hypersurface is the trace $H = \sum_i h(e_i, e_i)$ in an orthonormal tangent frame; the hypersurface is **minimal** if $H = 0$, and a submanifold is **totally geodesic** if $\mathrm{II} = 0$, equivalently if its geodesics are geodesics of the ambient manifold.

**Example (the sphere as a hypersurface).** For $S^{n} \subseteq \mathbb{R}^{n+1}$ with the unit outward normal $N(x) = x$, the second fundamental form is $\mathrm{II}(X, Y) = -g(X, Y)N$ and the mean curvature is $-n$; the Gauss equation recovers $K = 1$ on every plane. The sphere is not minimal but is totally umbilic, and it is an Einstein manifold.

## Gauss–Bonnet and Characteristic Classes

**Theorem (Gauss–Bonnet, surface case).** For a compact oriented Riemannian surface $M$ with Gaussian curvature $K$ and volume form $\mathrm{vol}_g$,

$$
\int_M K\,\mathrm{vol}_g = 2\pi\,\chi(M).
$$

**Theorem (generalised Gauss–Bonnet–Chern).** For a compact oriented Riemannian manifold of even dimension $2k$, the integral of the Pfaffian of the curvature form is the Euler characteristic:

$$
\int_M \operatorname{Pf}\!\left(\frac{\mathcal{R}}{2\pi}\right) = \chi(M).
$$

The form $\operatorname{Pf}(\mathcal{R}/2\pi)$ is the Chern–Weil form of the Pfaffian invariant polynomial, and it represents the Euler class $e(TM)$. The Pontryagin classes $p_j(TM)$ arise from the invariant polynomials $\operatorname{tr}(\mathcal{R}/2\pi)^{2j}$, and they give the signature formula, whose integral is the signature of the manifold when the dimension is a multiple of four. The characteristic classes therefore depend only on the topology of the manifold, while the curvature forms that represent them depend on the metric; the equality of the two is the content of the Chern–Weil theorem.

**Remark (curvature and topology).** The framework of this article is the passage from a local differential-geometric datum — the metric and its curvature — to global topological invariants. The Gauss–Bonnet theorem is the model: a curvature integral equals a characteristic number. The comparison theorems are the other direction: a pointwise curvature bound constrains the global topology, forcing compactness (Bonnet–Myers), a Euclidean structure (Cartan–Hadamard) or a bound on the volume growth. Both directions are developed for pseudo-Riemannian metrics.

## Summary

A Riemannian metric is a smooth field of positive definite inner products; it assigns a length to every curve, a distance to every pair of points, and a volume to every oriented region. Every smooth manifold carries one, the metrics on a fixed manifold are convex, and an isometry is a diffeomorphism preserving the metric and hence the length, the distance, the geodesics and the curvature.

The Levi-Civita connection is the unique metric and torsion-free connection, determined by the Koszul formula and written in coordinates with the Christoffel symbols; its curvature tensor has the algebraic symmetries $R(X,Y) = -R(Y,X)$, $R(X,Y,Z,W) = R(Z,W,X,Y)$ and the first Bianchi identity, and it satisfies the second Bianchi identity. Tracing gives the sectional curvature $K$, the Ricci tensor and the scalar curvature $S$; in dimension two the curvature is the Gaussian curvature $K$, in dimension three the Ricci tensor, and in every dimension the sectional curvature determines the tensor. Schur's theorem says that a pointwise-isotropic sectional curvature is constant in dimension at least three.

Geodesics are the curves with vanishing acceleration, they have constant speed and are locally minimising, and the exponential map sends a tangent vector to the endpoint of the geodesic it generates; normal coordinates make the metric Euclidean to first order, with the curvature in the second order. The Hopf–Rinow theorem identifies metric completeness, geodesic completeness and finite compactness, and produces a minimising geodesic between any two points. Jacobi fields are the variation fields of families of geodesics and satisfy the Jacobi equation; conjugate points are the zeros of Jacobi fields, and a geodesic is minimising only up to its first conjugate point. The Rauch comparison theorem compares Jacobi fields with those of a constant-curvature model, and it yields the Bonnet–Myers theorem — a positive Ricci bound forces compactness and bounds the diameter — and the Cartan–Hadamard theorem — nonpositive curvature makes the exponential a diffeomorphism. Cartan's theorem identifies a complete simply connected manifold of constant curvature with the corresponding model, so there are exactly three complete simply connected constant-curvature geometries.

The isometry group of a connected Riemannian manifold is a Lie group by the Myers–Steenrod theorem, its Lie algebra being that of the Killing fields. A submanifold inherits a metric, its second fundamental form measures the failure of its geodesics to be ambient geodesics, and the Gauss equation relates its curvature to the ambient curvature and the second fundamental form; the Gaussian curvature of a surface is intrinsic by the theorema egregium. Finally the Gauss–Bonnet theorem and its generalised form identify the integrals of the curvature of the tangent bundle with the Euler characteristic, the first case of the Chern–Weil principle that an integral of curvature is a topological invariant.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(M, g)$, $g_{ij}$, $g^{ij}$ | Riemannian manifold; metric coefficients and inverse |
| $ds^2 = \sum_{ij}g_{ij}dx^idx^j$ | First fundamental form |
| $L_g(\gamma)$, $d_g(p,q)$ | Length of a curve; Riemannian distance |
| $\operatorname{Isom}(M,g)$ | Isometry group; a Lie group by Myers–Steenrod |
| $\nabla$, $\Gamma^k_{ij}$, $\theta^i_{\ j}$ | Levi-Civita connection; Christoffel symbols; connection form |
| $R(X,Y)Z$, $R(X,Y,Z,W)$ | Curvature tensor and its fully covariant form |
| $\mathcal{R} = d\theta+\theta\wedge\theta$ | Curvature $2$-form in a frame; no bare $\Omega$ is used |
| $K(\sigma)$ | Sectional curvature of the two-plane $\sigma$ |
| $\operatorname{Ric}$, $S$, $G = \operatorname{Ric}-\frac12Sg$ | Ricci tensor, scalar curvature, Einstein tensor |
| Einstein manifold | $\operatorname{Ric} = \lambda g$; then $\lambda = S/n$ |
| $\nabla_{\gamma'}\gamma'=0$ | Geodesic equation |
| $\exp_p : T_pM \to M$ | Exponential map; normal coordinates |
| $\operatorname{inj}(p)$, cut locus | Injectivity radius and the cut locus |
| $J$, $\frac{D^2J}{dt^2} + R(J,\gamma')\gamma' = 0$ | Jacobi field and the Jacobi equation |
| Conjugate points | Zeros of a Jacobi field; the limit of the minimising range |
| $s_{\tilde K}(t)$ | Comparison field in the constant-curvature model |
| Hopf–Rinow | Completeness $\iff$ geodesic completeness $\iff$ finite compactness |
| Bonnet–Myers | $\operatorname{Ric} \geq (n-1)k > 0$ implies compact, $\operatorname{diam} \leq \pi/\sqrt k$ |
| Cartan–Hadamard | $K \leq 0$, complete, simply connected implies $\exp_p$ a diffeomorphism |
| Killing field | Vector field with $g(\nabla_YX,Z)+g(Y,\nabla_ZX)=0$; $\operatorname{Lie}\operatorname{Isom}$ |
| $\mathrm{II}(X,Y)$ | Second fundamental form; Gauss formula and Gauss equation |
| $H$, minimal, totally geodesic | Mean curvature $H = \operatorname{tr}\mathrm{II}$; $H=0$; $\mathrm{II}=0$ |
| $\chi(M)$, $\operatorname{Pf}(\mathcal{R}/2\pi)$ | Euler characteristic; Gauss–Bonnet–Chern integrand |
| $p_j(TM)$ | Pontryagin classes from traces of the curvature |



## Further Reading

- Manfredo P. do Carmo, *Riemannian Geometry* (Birkhäuser, 1992), for the full course: connection, curvature, Jacobi fields and comparison theorems.
- John M. Lee, *Introduction to Riemannian Manifolds*, 2nd ed. (Springer, 2018), for a modern account with normal coordinates, the cut locus and completeness.
- Jeff Cheeger and David G. Ebin, *Comparison Theorems in Riemannian Geometry* (North-Holland, 1975), for the Rauch, Bonnet–Myers and Cartan–Hadamard theorems in detail.
- Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry, Volume I* (Interscience, 1963), for connections, holonomy and the structure equations.
- Barrett O'Neill, *Semi-Riemannian Geometry with Applications to Relativity* (Academic Press, 1983), for the indefinite version of the whole theory.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (Academic Press, 1978), for the isometry-group and symmetric-space theory.
- Shiing-Shen Chern, "A simple intrinsic proof of the Gauss–Bonnet formula for closed Riemannian manifolds", *Annals of Mathematics* 45 (1944), 747–752, for the generalised Gauss–Bonnet theorem.
