
# __Pseudo-Riemannian and Lorentzian Geometry__

## Introduction

A pseudo-Riemannian metric is a smooth field of nondegenerate symmetric bilinear forms of a fixed signature $(p, q)$, positive definite on a $p$-dimensional subspace and negative definite on a complementary $q$-dimensional one at each point. When $q = 0$ this is a Riemannian metric and the geometry of *Riemannian Geometry*; when $p = 1$ and $q = n - 1$, or dually $q = 1$, it is a **Lorentzian** metric, and the pair $(M, g)$ is a Lorentzian manifold. The single change — nondegeneracy in place of positive definiteness — alters the theory in two places and leaves it intact everywhere else. It leaves intact the whole of the connection theory: the nondegeneracy of $g$ is exactly what the Koszul formula needs, so the Levi-Civita connection exists and is unique, the curvature tensor has the same symmetries, and the same Bianchi identities hold. It alters the metric theory, because a nondegenerate form of indefinite signature is not an inner product and defines no distance: the square $g(v, v)$ may be positive, negative or zero for a nonzero $v$, so there are three kinds of tangent vector and three kinds of curve, and the length of a curve may be imaginary or zero.

This article develops the theory of pseudo-Riemannian manifolds with an emphasis on the Lorentzian case, which is the richest and in which the new phenomena are all visible. It defines the signature and proves the invariance of the signature; defines the causal character of vectors and curves, the time-orientability and the causal relations, the cone structure and the model flat space; develops the Levi-Civita connection, geodesics, parallel transport and the exponential map, which carry over without change; treats the vanishing of the distance and the Lorentzian length and distance function that replace it; develops the curvature, in which the sectional curvature of a degenerate plane is undefined and the Ricci and scalar curvatures retain their meaning; classifies the complete simply connected pseudo-Riemannian manifolds of constant curvature into the three families of the flat, the sphere-like and the hyperboloid-like models; treats the quadric model spaces and the Lorentzian space forms; and closes with the isometric embedding theorem for indefinite metrics.

The article is the indefinite analogue of *Riemannian Geometry* and assumes *Smooth Manifolds and Differential Geometry*, *Curvature and Geodesics*, *Riemannian Geometry*, andtogether with the quadratic form theory of *Bilinear Forms*, *Quadratic Forms and Polarisation* and *Isometries and Orthogonal Transformations*, in particular Sylvester's law of inertia, and the orthogonal and pseudo-orthogonal groups of *Matrix Groups and Classical Groups*. The causal structure uses the theory of curves as smooth maps of *Smooth Manifolds and Differential Geometry* and the completeness and order of *Metric, Uniform and Complete Spaces*; the global limit arguments and the differential equations are Part III's, and they are stated here without pro. The mathematics is presented as mathematics: the Lorentzian manifolds are manifolds with a metric of signature $(1, n-1)$, the causal relations are relations on the points, and no physical object is introduced. No physics is invoked.

## Pseudo-Riemannian Metrics and Signature

### Metrics of Indefinite Signature

**Definition.** Let $V$ be a real vector space of finite dimension $n$. A symmetric bilinear form $g$ on $V$ is **nondegenerate** if the map $v \mapsto g(v, \cdot\,)$ is an isomorphism $V \to V^*$; its **signature** is the pair $(p, q)$ where $p$ is the dimension of a maximal subspace on which $g$ is positive definite and $q$ that of a maximal subspace on which it is negative definite. **Sylvester's law of inertia** states that $p$ and $q$ are well defined, depend only on $g$, and satisfy $p + q = n$ when $g$ is nondegenerate; the form is an inner product exactly when $q = 0$ or $p = 0$.

**Definition.** A **pseudo-Riemannian metric** of signature $(p, q)$ on a smooth manifold $M$ is a smooth section $g$ of $S^2T^*M$ such that $g_p$ is nondegenerate of signature $(p, q)$ at every $p$. A **pseudo-Riemannian manifold** is a pair $(M, g)$; it is **Lorentzian** if the signature is $(1, n-1)$ or, by the sign convention that does not change the geometry, $(n-1, 1)$. This article writes $g$ with signature $(p, q)$ and states the signature each time, and writes $\eta_{p,q}$ for the flat model below.

**Remark.** Positive definiteness and nondegeneracy are different conditions. The form $dx^2 - dy^2$ on $\mathbb{R}^2$ is nondegenerate of signature $(1,1)$ but vanishes on the two diagonal lines, so it is not an inner product and no norm is defined from it. The form $dx^2$ on $\mathbb{R}^2$ is positive semidefinite and degenerate; degeneracy is a separate failure, and it is the one that destroys the Koszul formula. A pseudo-Riemannian metric has neither failure.

**Theorem.** A smooth manifold carries a pseudo-Riemannian metric of signature $(p, q)$ if and only if its tangent bundle admits a subbundle of rank $p$ on which a Riemannian metric exists, equivalently if and only if the structure group of $TM$ reduces to $O(p, q)$. In the Lorentzian case, a closed connected manifold carries a Lorentzian metric if and only if its Euler characteristic vanishes.

**Proof sketch.** Given such a subbundle, choose a Riemannian metric $h$ and put $g = h|_{E} \oplus (-h)|_{E^\perp}$ on the decomposition $TM = E \oplus E^\perp$; the converse is the definition. For the Lorentzian statement, a Lorentzian metric produces a timelike, hence nowhere-zero, vector field, and a closed manifold admits a nowhere-zero vector field exactly when its Euler characteristic vanishes, by the Poincaré–Hopf theorem; conversely a nowhere-zero vector field $X$ gives the splitting $TM = \mathbb{R}X \oplus X^\perp$ and one defines $g = -h|_{X} \oplus h|_{X^\perp}$ for a Riemannian $h$. The Poincaré–Hopf theorem is a consequence of the degree theory of *Differential Topology*, applied to the zero set of a generic vector field. $\square$

### Causal Character of Vectors and Curves

**Definition.** Let $(M, g)$ be a pseudo-Riemannian manifold and $v \in T_pM$ nonzero. Then $v$ is **spacelike** if $g(v, v) > 0$, **timelike** if $g(v, v) < 0$, and **null** (or **lightlike**) if $g(v, v) = 0$. The set of null vectors in $T_pM$ is the **null cone** (or **light cone**); it is a cone, and it is the zero set of the quadratic form $q(v) = g(v, v)$, which is nondegenerate but indefinite. In a Lorentzian manifold the timelike vectors at $p$ form two open convex cones, and $p$ is **time-orientable** at $p$ if one of them is designated the future.

**Definition.** A nonzero vector field $X$ on a Lorentzian manifold $(M, g)$ is **timelike** if $g(X, X) < 0$ everywhere; the manifold is **time-orientable** if it admits a timelike vector field, and a **time orientation** is the choice of such a field up to multiplication by a positive function. A curve $\gamma$ is **timelike**, **null** or **spacelike** according to the character of its velocity $\gamma'(t)$, and it is **causal** if it is timelike or null everywhere.

**Proposition.** A connected Lorentzian manifold is either time-orientable or has a time-orientable double cover.

**Proof.** The set of time orientations at the points is a two-sheeted covering space of $M$; if it is disconnected the manifold is time-orientable, and if it is connected the covering is the double cover. $\square$

### The Flat Model

**Definition.** The **flat pseudo-Riemannian space** of signature $(p, q)$ is $\mathbb{R}^{p,q} = (\mathbb{R}^{p+q}, \eta_{p,q})$ with

$$
\eta_{p,q} = \sum_{i=1}^{p} dx_i^2 - \sum_{j=1}^{q} dy_j^2 ,
$$

the standard form of signature $(p, q)$; its isometry group is the pseudo-orthogonal group $O(p, q)$, which acts transitively, and the model is the flat simply connected pseudo-Riemannian manifold of that signature.

**Example (the Minkowski plane).** In signature $(1,1)$ the null cone at the origin consists of the two lines $x = \pm y$; there are two timelike cones, given by $|x| > |y|$ with $x > 0$ and with $x < 0$, and the form takes opposite signs on them. In the plane the causal structure is a partial order after a time orientation is chosen: $(t_1, x_1) \leq (t_2, x_2)$ if $t_2 - t_1 \geq |x_2 - x_1|$.

**Definition.** For a causal curve $\gamma$ the **Lorentzian length** is

$$
L_g(\gamma) = \int_a^b \sqrt{|g_{\gamma(t)}(\gamma'(t), \gamma'(t))|}\, dt ,
$$

and the **Lorentzian distance** is

$$
d_g(p, q) = \sup\{ L_g(\gamma) : \gamma \text{ causal from } p \text{ to } q \},
$$

with value $0$ if no causal curve joins the two points. It is not a metric: it is not symmetric, it satisfies a reverse triangle inequality $d_g(p, r) \geq d_g(p, q) + d_g(q, r)$ along causal chains, and it vanishes on many pairs of distinct points.

## The Levi-Civita Connection in the Indefinite Case

### Existence and Uniqueness

**Theorem (fundamental theorem of pseudo-Riemannian geometry).** On a pseudo-Riemannian manifold $(M, g)$ there is exactly one connection $\nabla$ that is metric, $X\,g(Y, Z) = g(\nabla_XY, Z) + g(Y, \nabla_XZ)$, and torsion-free, $\nabla_XY - \nabla_YX = [X, Y]$. It is given by the Koszul formula

$$
2\,g(\nabla_XY, Z) = X\,g(Y, Z) + Y\,g(Z, X) - Z\,g(X, Y) - g(X, [Y, Z]) + g(Y, [Z, X]) + g(Z, [X, Y]),
$$

and in a coordinate frame it has the Christoffel symbols

$$
\Gamma^k_{ij} = \frac{1}{2}\sum_l g^{kl}\bigl(\partial_{x^i}g_{jl} + \partial_{x^j}g_{il} - \partial_{x^l}g_{ij}\bigr).
$$

**Proof.** The proof of the Riemannian case used only the nondegeneracy of $g$: the right-hand side of the Koszul formula is a tensor, and since the pairing $g(\,\cdot\,, \,\cdot\,)$ is nondegenerate, a vector field is determined by its pairings with all $Z$. Metricity and torsion-freeness follow by substitution exactly as before. $\square$

**Remark.** Everything in this section and the next carries over verbatim from the Riemannian case, and no new phenomenon appears. Parallel transport is an isometry of tangent spaces, $\nabla_{\gamma'}\gamma' = 0$ is the geodesic equation, the exponential map is a local diffeomorphism at the origin of each tangent space, and normal coordinates put the metric into the form $g_{ij} = \eta_{ij} - \frac{1}{3}\sum_{kl}R_{ikjl}x^kx^l + O(|x|^3)$. The exponential map is defined by the same differential equation, whose solvability is the theory of Part III.

**Definition.** The **isometry group** $\operatorname{Isom}(M, g)$ consists of the diffeomorphisms preserving $g$; the **Killing fields** are the vector fields whose flows preserve $g$, characterised by $g(\nabla_YX, Z) + g(Y, \nabla_ZX) = 0$. The Myers–Steenrod theorem holds in the indefinite case: the isometry group is a Lie group and its Lie algebra is the Killing fields.

### Curvature in the Indefinite Case

**Definition.** The **curvature tensor** is $R(X, Y)Z = \nabla_X\nabla_YZ - \nabla_Y\nabla_XZ - \nabla_{[X,Y]}Z$, with $R(X, Y, Z, W) = g(R(X, Y)Z, W)$, and the curvature form is $\mathcal{R} = d\theta + \theta\wedge\theta$ in a frame.

**Theorem (symmetries).** The tensor satisfies

$$
R(X, Y, Z, W) = -R(Y, X, Z, W) = -R(X, Y, W, Z) = R(Z, W, X, Y)
$$

and the first Bianchi identity $R(X, Y, Z, W) + R(Y, Z, X, W) + R(Z, X, Y, W) = 0$; the second Bianchi identity $(\nabla_XR)(Y, Z) + (\nabla_YR)(Z, X) + (\nabla_ZR)(X, Y) = 0$ holds as an operator identity.

**Proof.** The proofs use only the metricity, the torsion-freeness and the Jacobi identity, none of which refers to the signature. $\square$

**Definition.** Let $\sigma$ be a two-dimensional subspace of $T_pM$. It is **nondegenerate** if $g|_{\sigma \times \sigma}$ is nondegenerate, and if it is nondegenerate the **sectional curvature** of $\sigma$ is

$$
K(\sigma) = \frac{R(v, w, w, v)}{g(v, v)g(w, w) - g(v, w)^2}
$$

for a basis $v, w$ of $\sigma$; the number is independent of the basis. If $\sigma$ is degenerate — which happens exactly when it is tangent to the null cone — the denominator vanishes for some basis and the sectional curvature is not defined.

**Remark.** In a Lorentzian manifold the planes through a null vector and other null vectors are degenerate, and the sectional curvature is defined only on the spacelike and the timelike planes. The curvature of a plane is bounded neither above nor below in general, because the denominator can be arbitrarily small on nondegenerate planes approaching the null cone. This is the first genuine difference from the Riemannian case: the sectional curvature no longer determines the curvature tensor at a point, since it is not defined on the degenerate planes, and one must use the algebraic classification of the curvature tensor instead.

**Definition.** The **Ricci tensor** is $\operatorname{Ric}(X, Y) = \sum_i R(e_i, X, Y, e_i)$ for a frame with $g(e_i, e_j) = \epsilon_i\delta_{ij}$, $\epsilon_i = \pm 1$; the **scalar curvature** is $S = \sum_i \epsilon_i\operatorname{Ric}(e_i, e_i)$; the **Einstein tensor** is $G = \operatorname{Ric} - \frac{1}{2}Sg$; and the manifold is **Einstein** if $\operatorname{Ric} = \lambda g$. The contracted second Bianchi identity reads $\operatorname{div}G = 0$ as before, where the divergence is taken with respect to the pseudo-Riemannian metric.

**Remark.** The Ricci and scalar curvatures retain their meaning because they are traces and do not divide by a metric norm. The Einstein condition is a metric equation, the equation $\operatorname{Ric} - \frac{1}{2}Sg = \Lambda g$ for a constant $\Lambda$ determining the constant-curvature Einstein metrics, and its study as an equation belongs to Part III, where the differential equations are available; here it is a condition on the curvature.

## Causal Structure

### The Causal Relations

**Definition.** Let $(M, g)$ be a time-oriented Lorentzian manifold and $p, q \in M$. Then $p$ **causally precedes** $q$, written $p \preceq q$, if there is a causal curve from $p$ to $q$; $p$ **chronologically precedes** $q$, written $p \ll q$, if there is a timelike curve from $p$ to $q$; and $p$ and $q$ are **causally related** if one precedes the other. The relation $\preceq$ is reflexive and transitive; it is a partial order when the manifold contains no closed causal curve, in which case the manifold is **causal**.

**Definition.** The **chronological future** of $p$ is $I^+(p) = \{q : p \ll q\}$ and the **causal future** is $J^+(p) = \{q : p \preceq q\}$; the corresponding pasts are $I^-(p)$ and $J^-(p)$. The futures are open and the causal futures are closed when the metric is sufficiently regular; a **Cauchy surface** is a closed acausal set met exactly once by every inextendible causal curve.

**Definition.** A Lorentzian manifold is **globally hyperbolic** if it admits a Cauchy surface, equivalently if it is causal and the sets $J^+(p) \cap J^-(q)$ are compact for all $p, q$. A globally hyperbolic manifold is isometric to a product $\mathbb{R} \times \Sigma$ with a metric of the form $-N^2dt^2 + g_t$ on the slices, where $N$ and $g_t$ vary with $t$; this is the splitting theorem, and its proof uses the limit arguments and the differential equations of Part III.

**Example (the flat case).** In $\mathbb{R}^{1,n-1}$ the causal future of a point is the closed solid cone with apex at the point, the chronological future is its interior, the set $J^+(p) \cap J^-(q)$ is compact when $p \ll q$, and every spacelike hyperplane $t = \mathrm{const}$ is a Cauchy surface; the flat space is globally hyperbolic. In a flat torus obtained from $\mathbb{R}^{1,1}$ by a translation, there are closed timelike curves, and the space is not causal.

### The Metric Cone and the Absence of a Distance

**Remark (why the distance fails).** A nondegenerate indefinite form is not the square of a norm, and the triangle inequality fails for the Lorentzian length. The Lorentzian distance $d_g$ is not symmetric, $d_g(p, q) \neq d_g(q, p)$ in general, it takes the value $0$ on causally unrelated pairs and on pairs joined only by null curves, and it satisfies the reverse triangle inequality on causal chains. It is a **time separation** rather than a metric, and the topology of a Lorentzian manifold is not recovered from it: two points on a null geodesic at positive separation have Lorentzian distance zero, so they cannot be separated by the function. The Riemannian distance function is replaced by the causal relations, and the topology is recovered instead from the chronological futures $I^\pm(p)$, which form a base for the manifold topology.

**Proposition.** The sets $I^+(p)$ and $I^-(p)$ are open, and the map $p \mapsto I^+(p)$ is a homeomorphism onto its image in the hyperspace of open sets; consequently the causal structure determines the topology of a Lorentzian manifold.

**Proof sketch.** The chronological future is open because the timelike condition is open and the flow of a timelike field moves backwards in time; the second statement follows by taking the intersections of the futures with a small sphere and identifying the point as the unique one whose future has the given germ. $\square$

## The Classification of Pseudo-Riemannian Space Forms

### The Three Families

**Definition.** A pseudo-Riemannian manifold is a **space form** of curvature $k$ if it is complete, simply connected and of constant sectional curvature $k$ on every nondegenerate two-plane.

**Theorem (classification).** For a fixed signature $(p, q)$ with $p + q = n \geq 2$ and a real number $k$, the complete simply connected pseudo-Riemannian manifolds of signature $(p, q)$ and constant sectional curvature $k$ are, up to isometry and scaling, exactly the following:

**(a)** $k = 0$: the flat space $\mathbb{R}^{p,q}$;

**(b)** $k > 0$: the pseudo-sphere $S^{p,q}$ of curvature $k$, the quadric of unit spacelike vectors in $\mathbb{R}^{p+1,q}$ with the induced metric;

**(c)** $k < 0$: the pseudo-hyperboloid $H^{p,q}$ of curvature $k$, the quadric of unit timelike vectors in $\mathbb{R}^{p,q+1}$ with the induced metric.

In each case the isometry group is the orthogonal group of the ambient form — $O(p+1, q)$ for the pseudo-sphere and $O(p, q+1)$ for the pseudo-hyperboloid — or a subgroup of it, acting transitively, and the manifold is a homogeneous space.

**Proof sketch.** The quadrics are nondegenerate because the normal vector is non-null at every point of the quadric, so the induced metric is nondegenerate; the orthogonal group of the ambient form acts transitively by isometries, and the stabiliser of a point is $O(p, q)$, giving a homogeneous space. The curvature is computed from the second fundamental form and the Gauss equation, and it is the constant $k$; conversely, Cartan's theorem for indefinite metrics, proved as in the Riemannian case, identifies a complete simply connected constant-curvature manifold with the model. $\square$

| Family | Model | Ambient form | Isometry group | Stabiliser |
|---|---|---|---|---|
| Flat | $\mathbb{R}^{p,q}$ | $\eta_{p,q}$ | $\mathbb{R}^{p,q} \rtimes O(p,q)$ | $O(p,q)$ |
| Sphere-like | $S^{p,q}$ | $\eta_{p+1,q}$ | $O(p+1,q)$ | $O(p,q)$ |
| Hyperboloid-like | $H^{p,q}$ | $\eta_{p,q+1}$ | $O(p,q+1)$ | $O(p,q)$ |

### The Lorentzian Space Forms

**Definition.** In the Lorentzian signature the three families above specialise as follows. The flat case is the flat Lorentzian space $\mathbb{R}^{1,n-1}$, whose isometry group is the semi-direct product $\mathbb{R}^{1,n-1} \rtimes O(1, n-1)$; the sphere-like case is the **Lorentzian sphere** $S^{1,n-1}$, the quadric of unit spacelike vectors in $\mathbb{R}^{2,n-1}$, of constant positive curvature, which is diffeomorphic to $\mathbb{R}^{n-1} \times S^1$; and the hyperboloid-like case is the **Lorentzian hyperboloid** $H^{1,n-1}$, the quadric of unit timelike vectors in $\mathbb{R}^{1,n}$, of constant negative curvature, which is diffeomorphic to $\mathbb{R} \times S^{n-1}$. Each carries the induced metric of signature $(1, n-1)$.

**Example (the two-dimensional Lorentzian space forms).** In signature $(1,1)$ the sphere-like model $S^{1,1}$ is the quadric $\langle x, x\rangle = 1$ of unit spacelike vectors in $\mathbb{R}^{2,1}$, a one-sheeted hyperboloid of revolution with the induced Lorentzian metric of constant positive curvature; the hyperboloid-like model $H^{1,1}$ is the quadric $\langle x, x\rangle = -1$ of unit timelike vectors in $\mathbb{R}^{1,2}$, a one-sheeted hyperboloid of revolution with the induced Lorentzian metric of constant negative curvature. Each is homogeneous under the appropriate pseudo-orthogonal group — $O(2,1)$ for the first and $O(1,2)$ for the second — and each is the Lorentzian analogue of the round sphere and of the hyperbolic plane.

**Remark (the anti-isometry and the sign conventions).** The signature $(p, q)$ and the signature $(q, p)$ describe the same geometry with the overall sign of $g$ reversed, since $-g$ has the same connection, the same geodesics and the curvature tensor of $-R$; the pair $(K, S)$ changes sign while the causal cones are exchanged. The corpus fixes the Lorentzian signature to be $(1, n-1)$ and states it at each use.

## The Isometric Embedding Theorem

**Theorem (Nash, indefinite case).** Every pseudo-Riemannian manifold of signature $(p, q)$ and dimension $n$ admits an isometric embedding into the flat pseudo-Riemannian space $\mathbb{R}^{p', q'}$ for some $p' \geq p$, $q' \geq q$ with $p' + q'$ finite, and the embedding may be taken proper; consequently every pseudo-Riemannian metric is the pullback of a flat metric along an embedding.

**Proof sketch.** The proof follows the Nash iteration for Riemannian embeddings, with the metric replaced by its nondegenerate indefinite version; the crucial point is that the formal solution of the isometric embedding equation has a solution depending on the same data, and the quadratic correction step uses the fact that the flat space has enough dimensions to absorb the error. The iteration is an analytic construction using the implicit function theorem and the convergence of a sequence, and it belongs to Part III; the theorem is quoted here as standard. $\square$

**Corollary.** The classification of pseudo-Riemannian manifolds up to isometry is the classification of the submanifolds of the flat spaces with nondegenerate induced metric; this is the analogue of the Whitney embedding theorem for the metric category, and it shows that the theory of *Riemannian Geometry* has a metric analogue for every signature.

## Summary

A pseudo-Riemannian metric is a smooth field of nondegenerate symmetric bilinear forms of fixed signature $(p, q)$; the signature is invariant by Sylvester's law of inertia, and a Lorentzian metric is one of signature $(1, n-1)$. Nondegeneracy in place of positive definiteness is enough for the entire connection theory: the Levi-Civita connection exists and is unique by the Koszul formula, parallel transport is an isometry, geodesics and the exponential map are defined by the same equations, normal coordinates have the same form, and the curvature tensor satisfies the same symmetries and Bianchi identities.

The indefinite metric defines no norm, hence no distance. A nonzero tangent vector is spacelike, timelike or null according to the sign of $g(v, v)$; the null vectors form the light cone; the causal relations $\preceq$ and $\ll$ replace the metric as the structure of the space, and they determine the topology, though not through a distance function. A time-oriented Lorentzian manifold is causal when it contains no closed causal curve, and globally hyperbolic when it has a Cauchy surface; a globally hyperbolic manifold splits as a product with a lapse function. The Lorentzian length is the integral of the square root of the absolute value of $g(\gamma', \gamma')$, and the Lorentzian distance is a supremum over causal curves, with a reverse triangle inequality and many vanishing values.

The sectional curvature is defined only on nondegenerate two-planes, so it no longer determines the curvature tensor and it is unbounded near the null cone; the Ricci and scalar curvatures retain their meaning as traces, and the Einstein tensor satisfies the contracted Bianchi identity. The complete simply connected pseudo-Riemannian manifolds of constant curvature fall into three families — the flat space $\mathbb{R}^{p,q}$, the pseudo-sphere $S^{p,q}$ and the pseudo-hyperboloid $H^{p,q}$ — each homogeneous under a pseudo-orthogonal group; in Lorentzian signature they are the flat space, the Lorentzian sphere and the Lorentzian hyperboloid. Finally, every pseudo-Riemannian manifold embeds isometrically into a flat pseudo-Riemannian space by the indefinite Nash theorem, which places the metric theory of every signature on the same footing as the Riemannian case.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(p, q)$ | Signature of a nondegenerate symmetric bilinear form; $p$ positive, $q$ negative directions |
| $g$ (signature $(p,q)$) | Pseudo-Riemannian metric; the signature is stated at each use |
| $\eta_{p,q} = \sum_{i=1}^p dx_i^2 - \sum_{j=1}^q dy_j^2$ | Flat metric of signature $(p,q)$ |
| $\mathbb{R}^{p,q}$ | Flat pseudo-Riemannian space $(\mathbb{R}^{p+q}, \eta_{p,q})$ |
| Spacelike, timelike, null | $g(v,v) > 0$, $< 0$, $= 0$ for $v \neq 0$ |
| Null cone, light cone | $\{v : g(v,v) = 0\}$ in a tangent space |
| Time-orientable | Admits a timelike vector field; the choice is a time orientation |
| $p \preceq q$, $p \ll q$ | Causal and chronological precedence |
| $I^\pm(p)$, $J^\pm(p)$ | Chronological and causal future and past |
| Causality, global hyperbolicity | No closed causal curve; existence of a Cauchy surface |
| Cauchy surface | Closed acausal set met once by every inextendible causal curve |
| $L_g(\gamma) = \int\sqrt{|g(\gamma',\gamma')|}\,dt$ | Lorentzian length of a causal curve |
| $d_g(p,q) = \sup_\gamma L_g(\gamma)$ | Lorentzian distance; not a metric, reverse triangle inequality |
| $\nabla$, $\Gamma^k_{ij}$, $\theta^i_{\ j}$, $\mathcal{R}$ | Levi-Civita connection, Christoffel symbols, connection form, curvature $2$-form |
| $R(X,Y,Z,W)$ | Curvature tensor with the standard symmetries and Bianchi identities |
| $K(\sigma)$ | Sectional curvature of a nondegenerate two-plane $\sigma$; undefined on degenerate planes |
| $\operatorname{Ric}$, $S$, $G = \operatorname{Ric}-\frac12Sg$ | Ricci tensor, scalar curvature, Einstein tensor |
| $\operatorname{Isom}(M,g)$, Killing field | Isometry group and its Lie algebra of Killing fields |
| $S^{p,q}$, $H^{p,q}$ | Sphere-like and hyperboloid-like quadrics of constant curvature |
| $O(p,q)$ | Pseudo-orthogonal group of $\eta_{p,q}$; the isometry group of $\mathbb{R}^{p,q}$ is $\mathbb{R}^{p,q}\rtimes O(p,q)$ |
| Nash embedding | Every pseudo-Riemannian manifold embeds isometrically in a flat one |



## Further Reading

- Barrett O'Neill, *Semi-Riemannian Geometry with Applications to Relativity* (Academic Press, 1983), for the complete theory of indefinite metrics, causal structure included.
- John K. Beem, Paul E. Ehrlich and Kevin L. Easley, *Global Lorentzian Geometry*, 2nd ed. (Marcel Dekker, 1996), for causal structure, global hyperbolicity and the Cauchy problem.
- Stephen W. Hawking and George F. R. Ellis, *The Large Scale Structure of Space-Time* (Cambridge University Press, 1973), for the causal structure and the singularity theorems stated mathematically.
- Demetrios Christodoulou, *Mathematical Problems of General Relativity I* (European Mathematical Society, 2008), for the analytic theory of the Einstein equations.
- Robert M. Wald, *General Relativity* (University of Chicago Press, 1984), for the geometry of Lorentzian manifolds and the classification of the curvature.
- Miguel Sánchez, "On the geometry of index form and conjugate points in Lorentzian manifolds", *Journal of Mathematical Physics* 38 (1997), for the Morse index theory in the Lorentzian case.
- Robert Bartnik, "The mass of an asymptotically flat manifold", *Communications on Pure and Applied Mathematics* 39 (1986), 661–693, for an application of the scalar curvature to the geometry of Lorentzian manifolds.
