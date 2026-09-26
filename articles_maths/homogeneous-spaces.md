
# __Homogeneous Spaces__

## Introduction

A **homogeneous space** is a manifold on which a group acts transitively: every point can be carried to every other by a symmetry of the space, so no point is distinguished and the space looks the same from anywhere. The sphere, seen from any of its points, is the same sphere; the real projective space, the hyperbolic space, the Grassmannian of $k$-planes and the space of complete flags in a vector space are all homogeneous, and in each case the transitive group is the group of linear transformations preserving the structure that defines the space. The notion is the geometric content of the orbit–stabiliser theorem of *Groups*: a transitive action of a group $G$ on a set $X$ is the same thing as a quotient $G/H$ of $G$ by the stabiliser $H$ of a chosen point, and when $G$ is a Lie group and $H$ a closed subgroup the quotient carries a smooth structure, a metric and a curvature of its own.

Homogeneity is a strong restriction, and it is the reason the theory can be organised. A homogeneous Riemannian manifold is complete; its curvature is a single algebraic datum at one point, transported everywhere by the group; its geodesics are the images of one-parameter subgroups under the action; and its isometry group is itself a Lie group acting transitively, so that the homogeneous space is recovered from the pair $(G, H)$. The theory is at its sharpest in the **symmetric** case, where the stabiliser is the fixed group of an involution and the curvature tensor is parallel; that case is, and the two articles are the framework in which the Grassmannians of *Grassmannians and Stiefel Manifolds* and the flag manifolds are read.

This article develops the theory from the orbit–stabiliser theorem. It shows that for a Lie group $G$ and a closed subgroup $H$ the quotient $G/H$ is a smooth manifold and the projection $G \to G/H$ is a principal $H$-bundle; computes the dimension and the examples (spheres, projective spaces, Grassmannians, Stiefel manifolds, hyperbolic spaces, orthogonal and unitary groups as quotients); treats invariant metrics, their existence by averaging on a compact group and by the reductive decomposition in general, the normal metrics and the geodesics; gives the Lie algebra decomposition $\mathfrak{g} = \mathfrak{h}\oplus\mathfrak{m}$ and the curvature formula for a normal homogeneous space; proves that the isometry group of a Riemannian manifold is a Lie group, so that a Riemannian homogeneous space is a quotient of its own isometry group; and describes the Cartan duality between the compact and noncompact families, the isotropy representation and the rank.

The article assumes *Smooth Manifolds and Differential Geometry* for manifolds, submanifolds, group actions and quotients; *Fibre Bundles, Connections and Curvature* for principal bundles and associated bundles; *Riemannian Geometry* and *Curvature and Geodesics* for the metric, the Levi-Civita connection, the geodesics and the curvature; *Grassmannians and Stiefel Manifolds* for the classical examples; *Euclidean Geometry*, *Spherical Geometry* and *Hyperbolic Geometry* for the model spaces; from Part I and Part II, *Groups*, *Group Actions and Structure*, *Transformation Groups*, *Matrix Groups and Classical Groups*, *Topological Groups*, *Lie Groups*, *The Lie Algebra and the Exponential Map* and *The Lie Correspondence and the Adjoint Representation* for the group theory, the Lie algebra and the exponential map, all cited and not re-derived. The invariant measure that makes the averaging over a compact group rigorous is the Haar measure of *Locally Compact Groups and Haar Measure*; the general harmonic analysis on a homogeneous space is Part III's. The symmetric case isand the generalised case of a complete flag isboth. No physics is invoked.

## Group Actions on Manifolds

### Transitive Actions and Orbits

**Definition.** Let $G$ be a group acting on a set $X$. The **orbit** of $x \in X$ is $G\cdot x = \{g\cdot x : g \in G\}$, the **stabiliser** of $x$ is $G_x = \{g \in G : g\cdot x = x\}$, a subgroup of $G$, and the action is **transitive** if $G\cdot x = X$ for some, hence every, $x$. A **$G$-space** is a set with a $G$-action, and a **$G$-equivariant** map is a map $f : X \to Y$ with $f(g\cdot x) = g\cdot f(x)$.

**Theorem (orbit–stabiliser).** For a group $G$ acting on a set $X$ and $x \in X$, the map

$$
\varphi_x : G/G_x \longrightarrow G \cdot x, \qquad \varphi_x(gG_x) = g \cdot x,
$$

is a well-defined $G$-equivariant bijection. In particular, if the action is transitive and $H = G_x$, then $X \cong G/H$ as $G$-sets.

**Proof.** If $gG_x = g'G_x$ then $g^{-1}g' \in G_x$, so $g\cdot x = g'\cdot x$; this is well definedness. It is injective because $g\cdot x = g'\cdot x$ gives $g^{-1}g' \in G_x$; it is surjective by transitivity; and it is equivariant by construction. $\square$

**Definition.** The action is **free** if every stabiliser is trivial, **effective** (or faithful) if the homomorphism $G \to \operatorname{Sym}(X)$ is injective, and **properly discontinuous** if every point has a neighbourhood $U$ with $g U \cap U \neq \emptyset$ for only finitely many $g$.

**Theorem.** For a topological group $G$ acting continuously on a topological space $X$, if $H$ is a closed subgroup then $G/H$ with the quotient topology is Hausdorff, the projection $G \to G/H$ is open, and the action map $G \times G/H \to G/H$, $(g, g'H) \mapsto gg'H$, is continuous; if $H$ is normal, $G/H$ is a topological group.

**Proof.** This is the quotient theory of *Topological Groups*: the map $G \to G/H$ is open and continuous, $H$ is closed, and the canonical bijection $G/G_x \to G\cdot x$ is a homeomorphism onto the orbit with the subspace topology. $\square$

### Smooth Actions

**Definition.** A **Lie group** is a smooth manifold with a group structure for which the multiplication and the inversion are smooth; this is the object of *Lie Groups*, whose theory is used here and not re-derived. A **smooth action** of a Lie group $G$ on a smooth manifold $M$ is a smooth map $G \times M \to M$, $(g, p) \mapsto g\cdot p$, satisfying $e\cdot p = p$ and $(gh)\cdot p = g\cdot(h\cdot p)$.

**Definition.** For $p \in M$ the **orbit map** is $\theta_p : G \to M$, $\theta_p(g) = g\cdot p$; its differential at the identity, composed with the exponential map of *The Lie Algebra and the Exponential Map*, describes the infinitesimal action: the **fundamental vector field** of $\xi \in \mathfrak{g}$ is

$$
\xi_M(p) = \left.\frac{d}{dt}\right|_{t=0} \exp(t\xi)\cdot p ,
$$

a smooth vector field on $M$ whose flow is the one-parameter group $\exp(t\xi)$.

**Theorem.** For a smooth action of a Lie group $G$ on a manifold $M$ and a point $p$, the stabiliser $G_p$ is a closed Lie subgroup of $G$, its Lie algebra is $\mathfrak{g}_p = \{\xi \in \mathfrak{g} : \xi_M(p) = 0\}$, and the orbit $G\cdot p$ is an immersed submanifold of $M$ with tangent space at $p$ the image of the differential of $\theta_p$, that is $\mathfrak{g}/\mathfrak{g}_p$.

**Proof sketch.** The stabiliser is closed as the preimage of $p$ under the continuous orbit map and is a Lie subgroup by the closed subgroup theorem of *Lie Groups*; the tangent claim follows by differentiating $g \mapsto g\cdot p$ at the identity. $\square$

## The Quotient $G/H$ as a Manifold

### The Manifold Structure

**Theorem (the quotient manifold theorem).** Let $G$ be a Lie group and $H$ a closed subgroup. Then the coset space $G/H$ has a unique smooth structure making the projection $\pi : G \to G/H$ a smooth submersion, of dimension

$$
\dim G/H = \dim G - \dim H .
$$

With this structure $G$ acts smoothly and transitively on $G/H$ by left translation, $H$ is the stabiliser of the identity coset, and the orbit map identifies every transitive smooth action of $G$ on a manifold with such a quotient.

**Proof sketch.** The quotient is locally modelled on a slice: the exponential map of a complement of $\mathfrak{h}$ in $\mathfrak{g}$ provides a local chart in which the action of $H$ is linear, and the quotient of that chart by the linear action of $H$ is a manifold; the charts patch because the construction is equivariant under $G$. Uniqueness follows from the universal property of the quotient, and the dimension count is the dimension of the slice. The details are the closed subgroup theorem of *Lie Groups*. $\square$

**Corollary.** A homogeneous space $G/H$ of a Lie group is a smooth manifold; if $G$ is compact so is $G/H$; and the map $\theta_p$ descends to an equivariant diffeomorphism $G/G_p \to G\cdot p$ for any smooth action.

### The Principal Bundle Structure

**Theorem.** For a Lie group $G$ and a closed subgroup $H$, the projection

$$
\pi : G \longrightarrow G/H
$$

is a principal $H$-bundle: $H$ acts on $G$ by right translation, the action preserves the fibres of $\pi$, and $\pi$ is locally trivial with fibre $H$. Equivalently, $G$ is the total space of a principal $H$-bundle over the homogeneous space $G/H$.

**Proof sketch.** Local sections of $\pi$ exist by the slice theorem: a neighbourhood of the identity coset is diffeomorphic to a neighbourhood of $0$ in a complement of $\mathfrak{h}$, and translating by $G$ gives a cover by trivialisations. The bundle theory is that of *Fibre Bundles, Connections and Curvature*. $\square$

**Corollary (dimension count).** The tangent bundle satisfies $TG/H \cong G \times_H (\mathfrak{g}/\mathfrak{h})$, the bundle associated to the principal bundle by the representation of $H$ on the quotient $\mathfrak{g}/\mathfrak{h}$; hence $\dim T(G/H) = \dim\mathfrak{g} - \dim\mathfrak{h}$.

**Definition.** The representation $H \to GL(\mathfrak{g}/\mathfrak{h})$ afforded by the adjoint action of $H$ on $\mathfrak{g}$ followed by the quotient projection is the **isotropy representation**, and the quotient $\mathfrak{g}/\mathfrak{h}$, identified with the tangent space $T_{eH}(G/H)$ by the differential of $\pi$, is the **isotropy space**. The action of $H$ on $T_{eH}(G/H)$ is the linearisation of the action of $H$ at the fixed point, and it is the local data from which the invariant geometry of $G/H$ is computed.

### Examples

**Example (spheres).** The sphere $S^n$ is the homogeneous space $SO(n+1)/SO(n)$, the stabiliser of a point being the rotations of the orthogonal complement; $\dim SO(n+1) - \dim SO(n) = n(n+1)/2 - n(n-1)/2 = n$, matching the dimension of the sphere. Likewise $S^{2n-1} = SU(n)/SU(n-1)$ and $S^{4n-1} = Sp(n)/Sp(n-1)$ realise the odd spheres as quotients of the unitary and symplectic groups, and $S^3 = SU(2) = Sp(1)$ as a group itself.

**Example (projective spaces).** $\mathbb{RP}^{n} = SO(n+1)/O(n)$ and $\mathbb{CP}^n = SU(n+1)/(SU(n)\times U(1))$; in each case the stabiliser is the image of the isotropy representation, the group preserving a line and its orthogonal complement. The dimension of $\mathbb{CP}^n$ is $(n+1)^2 - 1 - n^2 = 2n$, the real dimension of a complex $n$-manifold.

**Example (Grassmannians and Stiefel manifolds).** As in *Grassmannians and Stiefel Manifolds*,

$$
\mathrm{Gr}_k(\mathbb{R}^n) = O(n)/(O(k)\times O(n-k)), \qquad \dim = \tfrac{n(n-1)}{2} - \tfrac{k(k-1)}{2} - \tfrac{(n-k)(n-k-1)}{2} = k(n-k),
$$

and the Stiefel manifold $V_k(\mathbb{R}^n) = O(n)/O(n-k)$ is the quotient by the stabiliser of an orthonormal $k$-frame, of dimension $n(n-1)/2 - (n-k)(n-k-1)/2 = nk - k(k+1)/2$.

**Example (the model spaces).** $\mathbb{H}^n = SO(1,n)/SO(n)$ with the stabiliser $SO(n)$ of a point of the hyperboloid, of dimension $n(n+1)/2 - n(n-1)/2 = n$; the Euclidean space $\mathbb{R}^n = E(n)/O(n)$ with $E(n)$ the Euclidean isometry group; each model geometry of *Curvature and Geodesics* is a homogeneous space of its isometry group.

**Example (flag manifolds).** A **complete flag** in $\mathbb{K}^n$ is a chain $0 = V_0 \subset V_1 \subset \cdots \subset V_n = \mathbb{K}^n$ with $\dim V_i = i$, and the set of complete flags is the homogeneous space $GL(n,\mathbb{K})/B$ with $B$ the group of upper triangular matrices; the space of all flags, without fixing the dimensions, is the quotient of $GL(n,\mathbb{K})$ by a parabolic subgroup. The theory is.

## Invariant Metrics

### Existence

**Definition.** A Riemannian metric $g$ on a $G$-space $M$ is **$G$-invariant** if $g_{g\cdot p}(dL_g X, dL_g Y) = g_p(X, Y)$ for all $g \in G$ and all tangent vectors; equivalently, the left translations are isometries. A Riemannian manifold $(M, g)$ is **homogeneous** if its isometry group acts transitively.

**Theorem (existence on a compact group).** Let $G$ be a compact Lie group acting smoothly on a manifold $M$. If $M$ carries a Riemannian metric, then it carries a $G$-invariant one; and $G$ itself carries a bi-invariant Riemannian metric.

**Proof sketch.** For the first statement, average the metric over $G$ against the bi-invariant Haar measure of the compact group, whose existence is *Locally Compact Groups and Haar Measure*, written in parallel:

$$
\bar g_p(X, Y) = \int_G g_{g\cdot p}(dL_gX, dL_gY)\, d\mu(g),
$$

which is finite because $G$ is compact and $G$-invariant by the invariance of $\mu$. For the second, apply the first to the action of $G$ on $G$ by left translation, and the resulting metric is also right-invariant because the adjoint action of a compact group preserves a positive definite form. $\square$

**Remark.** The averaging argument uses the invariant measure, hence the measure theory; the statement of the theorem is nevertheless an ordinary statement about continuous functions on a compact group, and it is stated here with the measure-theoretic proof supplied by the companion article being written in parallel.

**Theorem (the reductive case).** Let $H$ be a closed subgroup of a Lie group $G$, and suppose the Lie algebra splits as a vector space,

$$
\mathfrak{g} = \mathfrak{h} \oplus \mathfrak{m}, \qquad [\mathfrak{h}, \mathfrak{m}] \subseteq \mathfrak{m},
$$

a **reductive decomposition** with $\mathfrak{m}$ an $\operatorname{Ad}(H)$-invariant complement of $\mathfrak{h}$. Then an $\operatorname{Ad}(H)$-invariant inner product on $\mathfrak{m}$ induces a $G$-invariant Riemannian metric on $G/H$.

**Proof sketch.** Left translation spreads the inner product on $\mathfrak{m} \cong T_{eH}(G/H)$ to a metric; $G$-invariance is automatic from the spreading, and the metric is well defined because the inner product on the isotropy space is $H$-invariant. $\square$

**Example.** For a compact $G$ and any closed $H$, the Killing form of $\mathfrak{g}$ restricted to an $\operatorname{Ad}(H)$-invariant complement is $\operatorname{Ad}(H)$-invariant and positive definite on the complement, so every homogeneous space of a compact Lie group carries an invariant metric, in agreement with the averaging theorem.

### Normal Metrics and Geodesics

**Definition.** A $G$-invariant metric on $G/H$ obtained from a positive definite $\operatorname{Ad}(H)$-invariant inner product on the reductive complement $\mathfrak{m}$ by the construction above is a **normal homogeneous metric** when the inner product is the restriction of an $\operatorname{Ad}(G)$-invariant inner product on $\mathfrak{g}$.

**Theorem.** On a homogeneous Riemannian manifold $(G/H, g)$ with an invariant metric:

**(a)** the metric is complete, and any two points are joined by a minimising geodesic;

**(b)** for a normal homogeneous metric, the geodesics through the identity coset are the curves $t \mapsto \exp(t\xi)H$ for $\xi \in \mathfrak{m}$.

**Proof sketch.** Part (a): the group $G$ acts transitively by isometries, so for any geodesic $\gamma$ and any $g$ the translate $g\cdot\gamma$ is a geodesic; every point and every direction is reached from the identity coset, so the exponential map of the metric is defined on all of $T_{eH}(G/H)$, which is completeness by the Hopf–Rinow theorem of *Riemannian Geometry*. Part (b): the one-parameter subgroup $\exp(t\xi)$ gives a curve whose velocity is invariant under left translation, and the invariance of the metric makes it a geodesic, the *canonical connection* of the reductive decomposition having no geodesic terms beyond the group translation; this is the model of the geodesics used for the Grassmannians in *Grassmannians and Stiefel Manifolds*. $\square$

**Corollary.** A homogeneous Riemannian manifold is complete, its exponential map is surjective, and if $G$ is compact its diameter is finite; the metric is bounded above and below by the metric of the group in the sense that the distance is controlled by the invariant inner product at the base point. For a compact homogeneous space the injectivity radius is positive, by the compactness of the space and the standard lower-bound estimate for the injectivity radius in terms of a curvature bound and the diameter, as in *Riemannian Geometry*.

## The Canonical Connection and Curvature

### The Lie Algebra Decomposition

**Definition.** For the reductive decomposition $\mathfrak{g} = \mathfrak{h}\oplus\mathfrak{m}$, let $p : \mathfrak{g} \to \mathfrak{m}$ and $p_{\mathfrak{h}} : \mathfrak{g}\to\mathfrak{h}$ be the projections, and define, for $\xi, \eta \in \mathfrak{m}$,

$$
[\xi, \eta]_{\mathfrak{m}} = p([\xi,\eta]) \in \mathfrak{m}, \qquad \text{and} \qquad U_\xi \eta = - \tfrac{1}{2}\,[\xi,\eta]_{\mathfrak{m}} + (\text{the symmetric part}),
$$

the **canonical connection** (or Nomizu connection) of the reductive decomposition.

**Theorem (Nomizu).** Let $(G/H, g)$ be a homogeneous Riemannian manifold. There is a unique $G$-invariant affine connection $\nabla^c$ on $G/H$, the **canonical connection**, whose torsion is the tensor $T(\xi,\eta) = -[\xi,\eta]_{\mathfrak{m}}$ and which is related to the Levi-Civita connection by

$$
\nabla^c_{\xi}\eta = \nabla^{\mathrm{LC}}_{\xi}\eta + \tfrac{1}{2}\,[\xi,\eta]_{\mathfrak{m}} ,
$$

for $\xi, \eta \in \mathfrak{m}$ extended to invariant vector fields. The canonical connection has parallel curvature and torsion, and it coincides with the Levi-Civita connection if and only if the decomposition satisfies $[\mathfrak{m},\mathfrak{m}] \subseteq \mathfrak{h}$, which is exactly the condition that $(G/H, g)$ be a Riemannian symmetric space.

**Proof sketch.** The invariance and the skew-symmetry requirements determine the connection uniquely; the comparison with the Levi-Civita connection is the Koszul formula of *Riemannian Geometry* applied to invariant fields, whose structure constants are the brackets of $\mathfrak{g}$. $\square$

**Corollary.** The homogeneous space is symmetric precisely when $[\mathfrak{m},\mathfrak{m}]\subseteq\mathfrak{h}$; then the canonical connection is the Levi-Civita connection, its curvature is parallel, and the space is a Riemannian symmetric space. The presence of a nonzero component $[\mathfrak{m},\mathfrak{m}]_{\mathfrak{m}}$ is the obstruction to symmetry, and it is the torsion of the canonical connection.

### The Curvature Formula

**Theorem (Nomizu).** For a normal homogeneous space $G/H$ with the metric induced from an $\operatorname{Ad}(G)$-invariant inner product $\langle\cdot,\cdot\rangle$ on $\mathfrak{g}$, the sectional curvature of the Levi-Civita connection at the identity coset is, for an orthonormal pair $\xi, \eta \in \mathfrak{m}$,

$$
K(\xi \wedge \eta) = \tfrac{1}{4}\bigl\|[\xi,\eta]_{\mathfrak{m}}\bigr\|^2 + \bigl\|[\xi,\eta]_{\mathfrak{h}}\bigr\|^2 ,
$$

where the subscripts denote the components in $\mathfrak{m}$ and $\mathfrak{h}$. Both terms are nonnegative; the second vanishes when the decomposition satisfies $[\mathfrak{m},\mathfrak{m}]\subseteq\mathfrak{m}$, and the first vanishes when $[\mathfrak{m},\mathfrak{m}]\subseteq\mathfrak{h}$. In particular every normal homogeneous space of a compact group has nonnegative sectional curvature.

**Proof sketch.** The metric on $G/H$ is the quotient metric of the Riemannian submersion $G \to G/H$, whose fibres are the orbits of right translation by $H$ and are totally geodesic in the bi-invariant metric of $G$; O'Neill's formula for the submersion, together with the O'Neill tensor $A_\xi\eta = \tfrac12[\xi,\eta]_{\mathfrak{h}}$ and the bi-invariant curvature $K_G(\xi,\eta) = \tfrac14\|[\xi,\eta]\|^2$ (verified from the Jacobi identity and the invariance of the inner product, and reducing to the standard formula for the curvature of a bi-invariant metric of Milnor), gives

$$
K_{G/H} = \tfrac14\|[\xi,\eta]\|^2 + \tfrac34\|[\xi,\eta]_{\mathfrak{h}}\|^2 = \tfrac14\|[\xi,\eta]_{\mathfrak{m}}\|^2 + \|[\xi,\eta]_{\mathfrak{h}}\|^2 ,
$$

which is the stated formula. $\square$

**Example.** For the Grassmannian $\mathrm{Gr}_k(\mathbb{R}^n) = O(n)/(O(k)\times O(n-k))$ the decomposition satisfies $[\mathfrak{m},\mathfrak{m}]\subseteq\mathfrak{h}$, so the first term vanishes and the curvature is $\|[\xi,\eta]\|^2 \geq 0$, in agreement with the formula $K = \|[X,Y]\|^2$ of *Grassmannians and Stiefel Manifolds*. For a bi-invariant metric on the group $G$ itself, that is $H = \{e\}$ and $\mathfrak{h} = 0$, the second term vanishes and the curvature is $\tfrac14\|[\xi,\eta]\|^2$, the classical value. The different normalisations of an invariant metric change the curvature by a positive factor, and this is the only ambiguity in the curvature of a homogeneous space.

**Corollary (the sign and the algebra).** A normal homogeneous space has nonnegative sectional curvature, and it is flat exactly when $[\mathfrak{m},\mathfrak{m}] = 0$, that is, when the complement is abelian; a flat homogeneous space is locally Euclidean, hence a quotient of $\mathbb{R}^n$ by a discrete group of translations by the Bieberbach theory. The curvature of a $G$-invariant, but not normal, metric need not have a sign: unlike the symmetric case, where the sign is determined by the type, a general homogeneous space may have curvature of varying sign, and the classification of the positively curved homogeneous spaces is a separate and delicate problem.

## The Isometry Group

**Theorem (Myers–Steenrod).** The isometry group $\operatorname{Isom}(M, g)$ of a Riemannian manifold is a Lie group in the compact-open topology, and it acts smoothly on $M$; its Lie algebra is the Lie algebra of complete Killing vector fields, and if $M$ is compact so is $\operatorname{Isom}(M, g)$.

**Proof sketch.** On the orthonormal frame bundle the isometries act freely and the action determines the isometry, so $\operatorname{Isom}(M,g)$ embeds in the frame bundle as a closed set; it is a Lie group by the closed subgroup theorem applied to the diffeomorphism group of the frame bundle, and the Killing field algebra is its Lie algebra. $\square$

**Corollary.** A connected homogeneous Riemannian manifold $(M, g)$ is, up to the kernel of the action, the quotient $\operatorname{Isom}(M,g)_0/H$ of the identity component of its isometry group by the stabiliser $H$ of a point; the stabiliser is compact, being a closed subgroup of the orthogonal group of the tangent space via the isotropy representation, and $M$ is the quotient of a Lie group by a compact subgroup.

**Corollary (Mostow–Palais).** The action of a compact Lie group on a manifold is locally linearisable at each point: for a compact $G$ acting smoothly on $M$ and $p \in M$, there is a $G_p$-invariant neighbourhood of the origin in $T_pM$ and an equivariant diffeomorphism onto a neighbourhood of $p$. Consequently the orbit structure of a compact group action is locally that of a linear action, and the orbit space is a manifold near a point of a principal orbit.

**Remark.** The isometry group is the largest group acting effectively and isometrically, and the homogeneous spaces of a fixed manifold are its orbit types. Two different groups may present the same homogeneous space: $\mathbb{RP}^{2} = O(3)/O(2) = SO(3)/SO(2)$, and the sphere $S^{2n-1}$ is a homogeneous space of $SO(2n)$, of $U(n)$ and of $SU(n)$. What is intrinsic is the pair (manifold, metric); the pair $(G, H)$ is extra structure, and the same manifold may be written as a quotient in many ways.

## Compact and Noncompact Duality

### The Two Types

**Definition.** A homogeneous space $G/H$ is of **compact type** if the Lie algebra $\mathfrak{g}$ admits an $\operatorname{Ad}(G)$-invariant inner product that is negative definite on $\mathfrak{h}$ and on the complement, as happens for a compact $G$; it is of **noncompact type** if the corresponding form is negative definite on $\mathfrak{h}$ and positive definite on the complement, as happens for a semisimple group without compact factors. A **symmetric pair** is a pair $(\mathfrak{g}, \sigma)$ with $\sigma$ an involution of $\mathfrak{g}$; the decomposition $\mathfrak{g} = \mathfrak{h}\oplus\mathfrak{m}$ into the $+1$- and $-1$-eigenspaces of $\sigma$ satisfies $[\mathfrak{h},\mathfrak{h}] \subseteq \mathfrak{h}$, $[\mathfrak{h},\mathfrak{m}]\subseteq \mathfrak{m}$, $[\mathfrak{m},\mathfrak{m}]\subseteq \mathfrak{h}$, the last of which is the symmetric condition of the previous section.

**Theorem (Cartan duality).** Let $\mathfrak{g} = \mathfrak{h}\oplus\mathfrak{m}$ be a symmetric pair of noncompact type. Then there is a unique (up to isomorphism) symmetric pair of compact type with the same $\mathfrak{h}$ that contains the same $\mathfrak{h}$, obtained by multiplying the $\mathfrak{m}$-part of the complexification by $i$; the corresponding homogeneous spaces are the **compact dual** of one another. Their curvatures are opposite in sign: the compact dual has nonnegative curvature and finite diameter, and the noncompact space has nonpositive curvature and infinite diameter.

**Proof sketch.** The construction is the real form theory of semisimple Lie algebras: the compact real form is obtained from any real form by taking the $+1$ eigenspace of the Cartan involution on $\mathfrak{h}$ and the $i$-multiple of the $-1$ eigenspace; the sign of the curvature follows from the curvature formula, in which the second term changes sign. $\square$

**Example.** The compact dual of the hyperbolic plane is the round sphere: $SO(1,2)/SO(2)$ dualises to $SO(3)/SO(2)$, and the two are the constant-curvature surfaces of curvature $-1$ and $+1$. The entire trichotomy of *Non-Euclidean Geometry* is a family of Cartan dualities; the Euclidean case is the intermediate flat limit.

**Example.** The compact dual of the complex hyperbolic space $\mathbb{CH}^n = SU(1,n)/U(n)$ is the complex projective space $\mathbb{CP}^n = SU(n+1)/U(n)$, and the dual of the quaternionic hyperbolic space is the quaternionic projective space. The duality is the structural reason the compact and noncompact families of Grassmannians, of projective spaces and of hyperbolic spaces have the same algebra and opposite curvature signs.

### Isotropy, Rank and Irreducibility

**Definition.** The **isotropy representation** of $G/H$ is the representation $H \to O(T_{eH}(G/H))$ induced by the linearisation of the action at the fixed point; a homogeneous space is **isotropy irreducible** if this representation is irreducible, and **weakly isotropy irreducible** if it is irreducible over $\mathbb{R}$ after restricting to the identity component. The **rank** of a symmetric space is the dimension of a maximal flat totally geodesic submanifold, equal to the dimension of a maximal abelian subspace of $\mathfrak{m}$.

**Theorem.** If $G/H$ is isotropy irreducible and $G$ is compact, then the invariant metric is unique up to scale, and the space is Einstein; the rank-one symmetric spaces are exactly the spaces of constant sectional curvature and the projective spaces over $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$ and the Cayley projective plane $\mathbb{OP}^2$, and they are characterised by the property that the isotropy representation is transitive on the unit sphere of the tangent space.

**Proof sketch.** The uniqueness of the invariant metric is Schur's lemma applied to the isotropy representation, since an invariant metric is an invariant bilinear form on an irreducible real representation and these are unique up to scale; the classification of the rank-one case is the classical one of the compact symmetric spaces of rank one, computed from the possible transitive actions of compact groups on spheres, of which there are exactly the listed families. $\square$

**Remark.** The classification of the symmetric spaces, with its list of the classical families $A$, $B$, $C$, $D$ and the exceptional spaces, is; the classification of the general homogeneous spaces is hopeless, but the classification under additional hypotheses — isotropy irreducible, normal, positively curved — is the content of the modern theory, and the positively curved homogeneous spaces have been classified by the work of Berger and Wilking. The homology and the cohomology of the classical homogeneous spaces are.

## Summary

A homogeneous space is a manifold with a transitive group of symmetries, and by the orbit–stabiliser theorem it is the coset space $G/H$ of the group by the stabiliser of a point. When $G$ is a Lie group and $H$ a closed subgroup, $G/H$ is a smooth manifold of dimension $\dim G - \dim H$, the projection $G \to G/H$ is a principal $H$-bundle, the tangent bundle is the associated bundle $G\times_H(\mathfrak{g}/\mathfrak{h})$, and the isotropy representation of $H$ on $\mathfrak{g}/\mathfrak{h}$ is the local linear data of the space; every transitive smooth action is of this form, and the sphere, the projective spaces, the Grassmannians, the Stiefel manifolds, the hyperbolic spaces, the Euclidean spaces and the flag manifolds are the standard examples.

A homogeneous space of a compact group carries an invariant Riemannian metric, constructed by averaging against the invariant measure; in general an invariant metric is given by an $\operatorname{Ad}(H)$-invariant inner product on a reductive complement $\mathfrak{m}$ of $\mathfrak{h}$ in $\mathfrak{g}$. Such a metric is complete, and for a normal metric the geodesics through the base point are the one-parameter subgroups $\exp(t\xi)H$; the canonical connection has torsion the component of the bracket in $\mathfrak{m}$ and coincides with the Levi-Civita connection exactly when $[\mathfrak{m},\mathfrak{m}]\subseteq\mathfrak{h}$, which is the symmetric case. The curvature of a normal homogeneous space is given by the Nomizu formula, $\tfrac14\|[\xi,\eta]_{\mathfrak{m}}\|^2 + \|[\xi,\eta]_{\mathfrak{h}}\|^2$ for an orthonormal pair, hence is nonnegative and vanishes exactly when $\mathfrak{m}$ is abelian; the compact dual of a noncompact symmetric space has the opposite curvature and finite diameter.

The isometry group of a Riemannian manifold is a Lie group, so a connected homogeneous Riemannian manifold is a quotient of its own isometry group by a compact stabiliser, and the action of a compact group is locally linearisable. The Cartan duality pairs the compact and noncompact symmetric spaces with the same isotropy algebra and opposite curvature signs; the hyperbolic space dualises to the sphere, and the complex and quaternionic hyperbolic spaces to the complex and quaternionic projective spaces. Isotropy irreducibility forces the invariant metric to be unique up to scale and the space to be Einstein, and the rank-one symmetric spaces are the spaces of constant curvature together with the projective planes over the four division algebras. The symmetric case, the flag case and the cohomology of the classical homogeneous spaces are not covered here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G/H$ | Homogeneous space of the Lie group $G$ by the closed subgroup $H$ |
| $G_x$, $G\cdot x$ | Stabiliser and orbit of $x$ |
| $\theta_p : G \to M$, $\theta_p(g) = g\cdot p$ | Orbit map |
| $\xi_M$ | Fundamental vector field of $\xi \in \mathfrak{g}$ |
| $\dim G/H = \dim G - \dim H$ | Dimension of a homogeneous space |
| $\pi : G \to G/H$ | Principal $H$-bundle projection; $G/H$ is the base |
| $TG/H \cong G\times_H(\mathfrak{g}/\mathfrak{h})$ | Tangent bundle as an associated bundle |
| $\mathfrak{g} = \mathfrak{h}\oplus\mathfrak{m}$ | Reductive decomposition; $[\mathfrak{h},\mathfrak{m}]\subseteq\mathfrak{m}$ |
| $\mathfrak{g} = \mathfrak{h}\oplus\mathfrak{m}$, $[\mathfrak{m},\mathfrak{m}]\subseteq\mathfrak{h}$ | Symmetric pair condition |
| Isotropy representation | $H \to O(T_{eH}(G/H))$; linearisation at the fixed point |
| $g$ | $G$-invariant Riemannian metric on $G/H$ |
| $\nabla^c$, $\nabla^{\mathrm{LC}}$ | Canonical connection; Levi-Civita connection |
| $K(\xi\wedge\eta) = \tfrac14\|[\xi,\eta]_{\mathfrak{m}}\|^2 + \|[\xi,\eta]_{\mathfrak{h}}\|^2$ | Curvature of a normal homogeneous space (Nomizu) |
| $\operatorname{Isom}(M,g)$ | Isometry group; a Lie group (Myers–Steenrod) |
| Compact / noncompact type, compact dual | Sign of the invariant form; Cartan duality |
| rank | Dimension of a maximal flat totally geodesic submanifold |
| Isotropy irreducible | Irreducible isotropy representation; forces uniqueness of the metric |
| $S^n = SO(n+1)/SO(n)$ | Sphere as a homogeneous space |
| $\mathrm{Gr}_k(\mathbb{R}^n) = O(n)/(O(k)\times O(n-k))$ | Grassmannian as a homogeneous space |









## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (Academic Press, 1978), for the quotient manifold theorem, invariant metrics and the curvature of homogeneous spaces.
- Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry, Volume II* (Interscience, 1969), for the canonical connection and the Nomizu curvature formula.
- Armand Borel, "Kählerian coset spaces of semisimple Lie groups", *Proceedings of the National Academy of Sciences* 40 (1954), 1147–1151, for the complex structure on the homogeneous spaces of compact groups.
- Shiu-Yuen Cheng and Shing-Tung Yau, "Differential equations on Riemannian manifolds and their geometric applications", *Communications on Pure and Applied Mathematics* 28 (1975), 333–354, for the isometry group and the Myers–Steenrod theorem.
- Katsumi Nomizu, "Invariant affine connections on homogeneous spaces", *American Journal of Mathematics* 76 (1954), 33–65, for the canonical connection.
- Sigurdur Helgason, *Groups and Geometric Analysis* (Academic Press, 1984), for the isotropy representation, the invariant theory and the spherical functions.
- Lionel Bérard-Bergery, "Quelques exemples de variétés riemanniennes complètes non compactes à courbure positive", *Journal für die reine und angewandte Mathematik* 371 (1986), 1–20, for the noncompact positively curved examples.
