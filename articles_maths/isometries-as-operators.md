# __Isometries as Operators__

## Introduction

An isometry of a Riemannian manifold is a map, and this article reads it as an **operator**. Its differential is a bundle isomorphism of the tangent bundle that preserves the metric on each fibre, so an isometry is an operator on the tangent bundle and, by extension, on every tensor bundle built from it. The assignment of its differential to an isometry is a faithful representation of the isometry group by operators, and the action of the group on the manifold is the geometric form of that representation: a symmetry of the metric is, at the operator level, a bundle automorphism that fixes the metric, and the infinitesimal version of the same statement is a Killing field.

The article develops the operator reading. It defines the differential operator of an isometry and proves that it preserves the metric, the Levi-Civita connection, the geodesics, the curvature and the volume form; it shows that the isometry group acts faithfully on the tangent bundle and is a Lie group, the theorem of Myers–Steenrod being cited from *Riemannian Geometry*; it identifies the Killing fields as the infinitesimal operators and characterises them by the skew-adjointness of $\nabla X$; it develops the isotropy representation at a point and the orbit of the group; and it proves that the fixed set of an isometry is a disjoint union of totally geodesic submanifolds.

The article assumes the Riemannian metric, the Levi-Civita connection, the geodesics, the curvature and the holonomy of *Curvature and Geodesics* and *Riemannian Geometry*, and it cites *Smooth Manifolds and Differential Geometry* for the tangent bundle, the tensor bundles and the Lie derivative. The **linear** isometries of a quadratic form, their generation by reflections and the orthogonal group $O(V,q)$ are *Isometries and Orthogonal Transformations* later in this Part, and the homogeneity of a space under its isometry group is *Homogeneous Spaces*; both are cited rather than restated. The spectral theory of the operators induced on a space of functions belongs to Part III and is not developed here. No physics is invoked.

## The Differential as a Bundle Operator

### The Differential of an Isometry

**Definition.** Let $(M, g)$ and $(N, h)$ be Riemannian manifolds. A smooth map $F : M \to N$ is a **local isometry** if $F^*h = g$, that is if

$$
h_{F(p)}\bigl(dF_p(v), dF_p(w)\bigr) = g_p(v, w)
$$

for every $p \in M$ and all $v, w \in T_pM$; it is an **isometry** if in addition it is a diffeomorphism. The isometries of $(M, g)$ onto itself form a group under composition, written $\operatorname{Isom}(M, g)$, and a local isometry is an isometry onto its image.

**Proposition.** A map $F : (M, g) \to (N, h)$ is an isometry if and only if it is a diffeomorphism with $F^*h = g$. The identity is an isometry, the composite of two isometries is an isometry, and the inverse of an isometry is an isometry.

**Proof.** The pullback of a metric along a diffeomorphism is a metric, and $F^*h = g$ is symmetric in $F$ and $F^{-1}$, since $(F^{-1})^*g = h$ is the same equation. Composition is associative and $(G \circ F)^*h = F^*(G^*h) = F^*h = g$ when $F^*h = g$ and $G^*h = h$.

An isometry preserves the length of every curve and therefore the Riemannian distance, $d_h(F(p), F(q)) = d_g(p, q)$; no other property of the differential is used at this point, and the linear condition above is the whole of the definition.

### The Action on the Tangent Bundle

**Theorem.** Let $F : (M, g) \to (N, h)$ be an isometry. Then its differential

$$
dF : TM \longrightarrow TN, \qquad (p, v) \longmapsto \bigl(F(p), dF_p(v)\bigr),
$$

is a bundle isomorphism whose restriction $dF_p : T_pM \to T_{F(p)}N$ to each fibre is a linear isometry of the inner product spaces $(T_pM, g_p)$ and $(T_{F(p)}N, h_{F(p)})$.

**Proof.** The differential of a diffeomorphism is a bundle isomorphism, and the metric compatibility is exactly the defining equation $h(dF_pv, dF_pw) = g_p(v, w)$ written on each fibre. The inverse of $dF$ is $d(F^{-1})$, so the restriction is invertible, and a linear isomorphism preserving the inner product is a linear isometry.

The theorem is the reason an isometry may be read as an operator: it acts linearly and isometrically on each tangent space, and the action varies smoothly with the point. The word **operator** is used in this Part for a map of this kind, a bundle endomorphism defined by a geometric object, and never for a map of a space of functions; the latter belongs to Part III.

**Theorem (faithfulness).** Let $M$ be connected. An isometry $F$ of $(M, g)$ is determined by its value $F(p)$ and its differential $dF_p$ at one point $p$. Consequently the assignment

$$
\operatorname{Isom}(M, g) \longrightarrow \operatorname{Aut}(TM), \qquad F \longmapsto dF,
$$

is a faithful representation of the isometry group by bundle automorphisms of the tangent bundle.

**Proof.** If $F$ and $G$ have $F(p) = G(p)$ and $dF_p = dG_p$, then $H = G^{-1} \circ F$ fixes $p$ and has $dH_p = \mathrm{id}$. Since an isometry intertwines the exponential maps, $\exp_p \circ\, dH_p = H \circ \exp_p$, so $H$ fixes a whole normal neighbourhood of $p$; the set of points fixed by $H$ is closed in $M$, and it is open because each of its points has a normal neighbourhood that it fixes; by connectedness it is all of $M$, so $H = \mathrm{id}$ and $F = G$. The assignment is a homomorphism because $d(G \circ F) = dG \circ dF$ by the chain rule, and it is injective by the first statement.

### The Action on Tensor Fields

**Theorem.** An isometry $F$ of $(M, g)$ preserves the Levi-Civita connection, the geodesics, the curvature tensor and the volume form up to sign:

**(a)** $F^*\nabla = \nabla$, that is $dF(\nabla_XY) = \nabla_{dF(X)}dF(Y)$ for all vector fields $X, Y$;

**(b)** if $\gamma$ is a geodesic then $F \circ \gamma$ is a geodesic, and $F(\exp_p(v)) = \exp_{F(p)}(dF_p(v))$ for every $v$ for which the exponential is defined;

**(c)** $dF(R(X, Y)Z) = R\bigl(dF(X), dF(Y)\bigr)dF(Z)$;

**(d)** $F^*\mathrm{vol}_g = \det(dF)\,\mathrm{vol}_g = \pm\,\mathrm{vol}_g$, the sign being $+$ if and only if $F$ preserves the orientation.

**Proof.** (a) The pullback $F^*\nabla$ defined by $(F^*\nabla)_XY = d(F^{-1})\bigl(\nabla_{dF(X)}dF(Y)\bigr)$ is a connection on $TM$; it is metric because $F$ is, and torsion-free because the differential commutes with the Lie bracket, so by the uniqueness in the fundamental theorem of Riemannian geometry it equals $\nabla$. (b) is (a) read on the geodesic equation $\nabla_{\gamma'}\gamma' = 0$, and the exponential statement is the uniqueness of the geodesic with a given initial velocity. (c) follows by substituting (a) into the definition $R(X,Y)Z = \nabla_X\nabla_YZ - \nabla_Y\nabla_XZ - \nabla_{[X,Y]}Z$. (d) The volume form is characterised by its value on a positively oriented orthonormal frame; the differential carries such a frame to an orthonormal frame, whose orientation is that of the original exactly when $\det(dF_p) > 0$, and $\det(dF_p) = \pm1$ since $dF_p$ is a linear isometry.

**Corollary (holonomy).** An isometry $F$ conjugates the holonomy group at $p$ to that at $F(p)$:

$$
\operatorname{Hol}_{F(p)} = dF_p\,\operatorname{Hol}_p\,(dF_p)^{-1}.
$$

**Proof.** Parallel transport along a loop $\gamma$ based at $p$ is carried by $dF$ to parallel transport along the loop $F\circ\gamma$ based at $F(p)$, by part (a); the two transports therefore correspond under conjugation by $dF_p$, and the statement follows for the groups generated by all loops.

## The Isometry Group

### The Group of Operators and Its Topology

**Definition.** The **isometry group** $\operatorname{Isom}(M, g)$ is the group of the isometries of $(M, g)$ onto itself, with the compact-open topology, equivalently the topology of uniform convergence on compact subsets of $M$.

**Proposition.** The isometry group is closed in the group of homeomorphisms of $M$ with the compact-open topology, it acts on $M$ by the evaluation $(F, p) \mapsto F(p)$, and the action is continuous. If $M$ is compact the group is compact, and if $(M, g)$ is proper, in the sense that every closed ball is compact, the group is locally compact and acts properly.

**Proof.** A limit of isometries uniformly on compact sets is a map preserving the distance, hence a distance-preserving homeomorphism, hence an isometry by the Myers–Steenrod theorem cited below; the closedness follows. The evaluation is continuous by the definition of the compact-open topology, and the compactness and properness statements are the Ascoli argument applied to the uniformly equicontinuous family of the isometries, whose modulus of continuity is $1$.

### The Lie Structure

**Theorem (Myers–Steenrod).** For a connected Riemannian manifold $(M, g)$ the isometry group is a Lie group, its action on $M$ is smooth, and its Lie algebra is the Lie algebra of the Killing fields of $(M, g)$. An isometry is determined by its value and its differential at one point, so

$$
\dim\operatorname{Isom}(M, g) \leq \frac{n(n+1)}{2}, \qquad n = \dim M .
$$

The theorem is proved in *Riemannian Geometry*, where the group is realised as a closed subgroup of the bundle of orthonormal frames; it is cited here because the operator reading uses it: the tangent-bundle representation of the theorem above is a smooth representation of a Lie group.

### Orbits and Homogeneity

**Definition.** The **orbit** of $p$ under the isometry group is $\operatorname{Isom}(M, g)\cdot p = \{F(p) : F \in \operatorname{Isom}(M, g)\}$, the **isotropy group** at $p$ is the subgroup $\operatorname{Isom}_p = \{F : F(p) = p\}$ that fixes $p$, and the manifold is **homogeneous** if the action is transitive, that is if the orbit is all of $M$.

**Proposition.** For a connected Riemannian manifold the orbits of the isometry group are disjoint and cover $M$, each orbit is a submanifold, and the isotropy groups at two points of one orbit are conjugate, $\operatorname{Isom}_{F(p)} = F\,\operatorname{Isom}_p\,F^{-1}$. If $M$ is homogeneous with $G = \operatorname{Isom}(M, g)$ and $H = \operatorname{Isom}_p$ for a fixed $p$, then $M \cong G/H$ as a smooth manifold and the metric is $G$-invariant.

**Proof.** Two orbits are equal or disjoint because the group acts by bijections; the orbit is the image of the smooth map $F \mapsto F(p)$ from a Lie group, and it is an immersed submanifold of constant rank, hence a submanifold. The conjugation statement is $(F G F^{-1})(F p) = F p$ for $G \in \operatorname{Isom}_p$, and conversely. The identification $M \cong G/H$ is the orbit–stabiliser theorem, and the invariance of the metric is the fact that the elements of $G$ are isometries; the quotient manifold theory is that of *Homogeneous Spaces*, where the invariant metrics and the isotropy representation are developed.

## Killing Fields as Infinitesimal Operators

### Definition and Skew-Adjointness

**Definition.** A **Killing field** on $(M, g)$ is a vector field $X$ whose local flow consists of local isometries, equivalently a vector field with

$$
\mathcal{L}_X g = 0,
$$

where $\mathcal{L}_X$ is the Lie derivative. The Killing fields form a vector space $\mathfrak{k}(M, g)$, closed under the Lie bracket of vector fields.

**Theorem.** A vector field $X$ is a Killing field if and only if the endomorphism $\nabla X$ of $TM$ defined by $Y \mapsto \nabla_YX$ is skew-adjoint for the metric,

$$
g(\nabla_YX, Z) + g(Y, \nabla_ZX) = 0 \qquad (Y, Z),
$$

equivalently $\nabla X \in \mathfrak{so}(TM, g)$.

**Proof.** For the Lie derivative of the metric,

$$
(\mathcal{L}_Xg)(Y, Z) = X\,g(Y, Z) - g([X, Y], Z) - g(Y, [X, Z]),
$$

and substituting $X\,g(Y,Z) = g(\nabla_XY,Z)+g(Y,\nabla_XZ)$, $[X,Y] = \nabla_XY-\nabla_YX$ and $[X,Z] = \nabla_XZ-\nabla_ZX$ gives $(\mathcal{L}_Xg)(Y,Z) = g(\nabla_YX,Z)+g(Y,\nabla_ZX)$. This vanishes for all $Y, Z$ exactly when $Y \mapsto \nabla_YX$ is skew-adjoint.

The skew-adjoint endomorphism $\nabla X$ is the **infinitesimal operator** of the isometry: it is the derivative at $t = 0$ of the differential operators $d\varphi_t$ of the flow.

### The Flow of a Killing Field

**Theorem.** Let $X$ be a complete Killing field with flow $\varphi_t$. Then every $\varphi_t$ is an isometry, the flow is a one-parameter subgroup of $\operatorname{Isom}(M, g)$, and

$$
\frac{d}{dt}\Big|_{t=0} d(\varphi_t)_p = \nabla X\big|_p
$$

as an endomorphism of $T_pM$. Consequently the Lie algebra of the isometry group, when $\operatorname{Isom}(M, g)$ is given its Lie structure, is exactly the Lie algebra of the complete Killing fields.

**Proof.** The flow of a Killing field consists of local isometries by the definition of the Lie derivative, and a local isometry defined on the whole manifold is an isometry; the flow identity $\varphi_{s+t} = \varphi_s \circ \varphi_t$ makes the family a one-parameter subgroup. The derivative of the differential is computed by commuting the two derivatives, and it is the covariant derivative: for a geodesic $\gamma$ with $\gamma'(0)=v$, the Jacobi-type equation satisfied by $\partial_s\varphi_s(\gamma(t))$ at $s = 0$ gives $\nabla_vX$ as the value. The identification of the two Lie algebras is Myers–Steenrod together with the fact that every one-parameter subgroup of the isometry group is generated by a complete Killing field.

**Corollary (the Killing equation).** In a chart a Killing field satisfies

$$
\nabla_iX_j + \nabla_jX_i = 0, \qquad X_j = g_{ji}X^i ,
$$

a linear first-order system; hence $\dim\mathfrak{k}(M,g) \le \frac{n(n+1)}{2}$, and the equality holds exactly on the spaces of constant curvature.

**Proof.** The equation is the skew-adjointness of the previous theorem written with lowered indices. A Killing field is determined by $X(p)$ and $\nabla X|_p$, and $\nabla X$ is skew-adjoint, so the values at a point span a space of dimension $n + \frac{n(n-1)}{2} = \frac{n(n+1)}{2}$; the bound follows. Equality forces the metric to be of constant curvature, the classical theorem of the maximality of the isometry group.

## The Isotropy Representation

### The Linear Isotropy

**Theorem.** For $p \in M$ the map

$$
\rho_p : \operatorname{Isom}_p \longrightarrow O(T_pM, g_p), \qquad \rho_p(F) = dF_p,
$$

is an injective homomorphism of groups, and its image, the **linear isotropy group** at $p$, is a closed subgroup of the orthogonal group. If $M$ is connected, $\rho_p$ is an isomorphism onto the linear isotropy group.

**Proof.** The map is a homomorphism by the chain rule and injective by faithfulness: an isometry fixing $p$ and acting trivially on $T_pM$ is the identity. The image is the set of the $dF_p$ for $F$ fixing $p$; it is the intersection of the closed set $\operatorname{Isom}(M,g)$-translates and is closed in $O(T_pM,g_p)$, being the isotropy of a continuous action. Surjectivity of $\rho_p$ onto its image is the definition.

**Corollary.** The linear isotropy group is a subgroup of a compact group, hence it is compact when $\operatorname{Isom}_p$ is compact and in particular when $M$ is compact; the orbits of $\operatorname{Isom}_p$ on the unit sphere of $T_pM$ are the directions in which the space looks alike, and the space is **isotropic** at $p$ when the linear isotropy group acts transitively on the unit sphere.

### The Isotropy and the Orbits

**Proposition.** The isotropy representations at the points of one orbit are conjugate by the differentials of the isometries carrying one point to the other: if $q = F(p)$ then $\rho_q = \operatorname{Ad}(dF_p)\circ\rho_p$, identified through $dF_p : T_pM \to T_qM$. On a homogeneous space the isotropy representation at the base point is the adjoint action of the isotropy subgroup on the complement of its Lie algebra, which is the representation of *Homogeneous Spaces*.

**Proof.** For $G \in \operatorname{Isom}_p$ one has $FGF^{-1} \in \operatorname{Isom}_{F(p)}$ and $d(FGF^{-1})_{F(p)} = dF_p\,dG_p\,(dF_p)^{-1}$; this is the stated conjugation, and on a homogeneous space it is the adjoint action on the quotient $\mathfrak{g}/\mathfrak{h}$ once the complement is identified with the tangent space by the orbit map.

## The Fixed Set of an Isometry

### The Fixed-Point Submanifolds

**Theorem.** Let $F$ be an isometry of $(M, g)$ and let

$$
\operatorname{Fix}(F) = \{x \in M : F(x) = x\}
$$

be its fixed set. Then each connected component of $\operatorname{Fix}(F)$ is a totally geodesic submanifold of $M$; near a fixed point $p$ the component is

$$
\exp_p\bigl(\operatorname{Fix}(dF_p)\cap U_p\bigr),
$$

where $\operatorname{Fix}(dF_p)$ is the fixed subspace of the linear isometry $dF_p$ and $U_p$ is a normal neighbourhood of $0$ in $T_pM$ on which $\exp_p$ is a diffeomorphism.

**Proof.** Because $F$ is an isometry it commutes with the exponential, $F(\exp_p v) = \exp_{F(p)}(dF_p v)$; at a fixed point, $F(\exp_p v) = \exp_p(dF_pv)$ for $v \in U_p$. Since $\exp_p$ is a diffeomorphism on $U_p$, a point $\exp_p v$ is fixed by $F$ exactly when $dF_pv = v$, so the fixed set near $p$ is the exponential image of the fixed subspace of the orthogonal map $dF_p$, a linear subspace. The fixed set is therefore locally a submanifold, and the tangent space of the component at $p$ is $\operatorname{Fix}(dF_p)$. A geodesic through $p$ with velocity in $\operatorname{Fix}(dF_p)$ stays in the fixed set, because $dF_p$ fixes its velocity and the exponential image is fixed; hence the component is totally geodesic, and the geodesics of the induced metric are the ambient geodesics.

**Corollary.** If $M$ is connected and $F$ fixes a point $p$ with $dF_p = \mathrm{id}$, then $F = \mathrm{id}$. The fixed set of a nontrivial isometry has empty interior, and the fixed set of an involution is the same as the fixed set of its differential-fixed components, which is the form in which it reappears in *Isometric Involutions and the Fixed-Point Set*.

**Proof.** The first statement is the faithfulness argument of the tangent-bundle representation. If the fixed set had interior it would contain a normal neighbourhood of one of its points, and then the isometry would fix a full bundle of directions there, forcing $dF_p = \mathrm{id}$ at that point and hence $F = \mathrm{id}$.

### Examples

**Example (the model geometries).** On $\mathbb{R}^n$ the reflection in a hyperplane has a hyperplane as its fixed set; on the sphere $S^n$ the reflection in a great subsphere $S^k$ has that subspace as a totally geodesic fixed set; on hyperbolic space the reflection in a totally geodesic hyperplane has that hyperplane. In each case the fixed set is totally geodesic, as the theorem requires, and the components are read off from the linear part.

## Summary

An isometry $F$ of a Riemannian manifold $(M, g)$ is an operator through its differential $dF : TM \to TM$, a bundle isomorphism that restricts to a linear isometry on each tangent space; the assignment $F \mapsto dF$ is a faithful representation of the isometry group by bundle automorphisms, an isometry being determined by its value and differential at one point. The differential preserves the Levi-Civita connection, the geodesics, the exponential map, the curvature tensor and the volume form up to the sign of the orientation, and it conjugates the holonomy group at a point to that at the image point.

The isometry group, with the compact-open topology, is a Lie group by the theorem of Myers–Steenrod, its Lie algebra being that of the Killing fields; it is compact for a compact manifold and acts properly for a proper one. Its orbits are the components of the space under the symmetries, its isotropy group at a point acts linearly on the tangent space by the injective **linear isotropy representation** into the orthogonal group, and a manifold on which the action is transitive is the homogeneous space $G/H$ with an invariant metric, the isotropy representation being the adjoint action on the complement.

A Killing field is a vector field with $\mathcal{L}_Xg = 0$, equivalently a field whose covariant derivative $\nabla X$ is skew-adjoint; its flow is a one-parameter group of isometries, and $\nabla X$ is the infinitesimal operator of that group, so the Lie algebra of the isometry group is the algebra of the complete Killing fields. The Killing fields are determined at a point by $(X(p), \nabla X|_p)$ with $\nabla X$ skew, which gives the bound $\dim\operatorname{Isom}(M,g) \le \frac{n(n+1)}{2}$. The fixed set of an isometry is a disjoint union of totally geodesic submanifolds, the component through a fixed point $p$ being the exponential image of the fixed subspace of $dF_p$; an isometry fixing a point with identity differential is the identity.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(M, g)$, $n = \dim M$ | Riemannian manifold and its dimension |
| $F$, $dF$, $dF_p$ | Isometry, its differential as a bundle map, and its value at $p$ |
| $F^*h = g$ | The defining equation of an isometry or local isometry |
| $\operatorname{Isom}(M, g)$ | Isometry group, with the compact-open topology |
| $\operatorname{Aut}(TM)$ | Bundle automorphisms of the tangent bundle |
| $F^*\nabla = \nabla$, $F^*\mathrm{vol}_g = \pm\mathrm{vol}_g$ | Preservation of the connection and of the volume form |
| $\operatorname{Hol}_p$ | Holonomy group at $p$, conjugated by $dF_p$ |
| $\operatorname{Isom}_p$ | Isotropy group at $p$ |
| $\rho_p(F) = dF_p$ | Linear isotropy representation, into $O(T_pM, g_p)$ |
| Orbits, homogeneous space $G/H$ | The orbit of the isometry group; the space when transitive |
| Killing field $X$, $\mathcal{L}_Xg = 0$ | Infinitesimal isometry; vanishing Lie derivative of the metric |
| $\nabla X$, $\nabla X \in \mathfrak{so}(TM, g)$ | Skew-adjoint infinitesimal operator of the Killing field |
| $\nabla_iX_j + \nabla_jX_i = 0$ | Killing equation in a chart |
| $\mathfrak{k}(M, g)$ | Lie algebra of the Killing fields |
| $\operatorname{Fix}(F)$, $\operatorname{Fix}(dF_p)$ | Fixed set of the isometry; fixed subspace of its differential |

## Further Reading

- Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry, Volume I* (Interscience, 1963), for the isometry group, the Killing fields and the holonomy.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (Academic Press, 1978), for the isometry group as a Lie group, the isotropy representation and the homogeneous-space formulation.
- Shoshichi Kobayashi, *Transformation Groups in Differential Geometry* (Springer, 1972), for the fixed-point sets of isometries and the action on the frame bundle.
- Manfredo P. do Carmo, *Riemannian Geometry* (Birkhäuser, 1992), for the Myers–Steenrod theorem and the Killing equation.
- John M. Lee, *Introduction to Riemannian Manifolds*, 2nd ed. (Springer, 2018), for the modern account of isometries, the isometry group and its Lie algebra.
