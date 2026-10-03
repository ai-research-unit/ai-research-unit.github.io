# __The Geodesic Symmetry and Locally Symmetric Spaces__

## Introduction

A geodesic through a point runs in two directions, and the map that reverses it is the oldest symmetry of a Riemannian manifold. On a normal neighbourhood of a point $p$ the map that sends $\gamma(t)$ to $\gamma(-t)$ along every geodesic through $p$ is well defined and smooth, it fixes $p$, and its differential at $p$ is $-\mathrm{id}$; this is the **geodesic symmetry** at $p$. It is a local isometry exactly when the curvature is parallel at $p$, and a manifold is **locally symmetric** when this holds at every point, equivalently when $\nabla R = 0$. The geodesic symmetry is therefore the geometric face of the single equation $\nabla R = 0$, and the passage from the local symmetries to the global ones is the passage from the locally symmetric spaces to the symmetric spaces.

The article develops the geodesic symmetry and the locally symmetric spaces. It defines the symmetry in normal coordinates, proves that it is an involution and that it is the unique local isometry fixing $p$ with differential $-\mathrm{id}$; it proves the equivalence of the local symmetry, the parallelism of the curvature and the equation $\nabla R = 0$; it shows that on a locally symmetric space the curvature and all its covariant derivatives are parallel, so the curvature operator is preserved by the symmetry; and it states the globalisation theorem of Cartan: a complete, simply connected, locally symmetric manifold is a symmetric space, every local symmetry extending to a global one, and a general locally symmetric space is a quotient of such a space by a discrete group of isometries.

The article assumes the metric, the connection, the geodesics, the exponential map, the curvature and the Jacobi fields of *Curvature and Geodesics*, *Riemannian Geometry* and *The Geodesic Flow Operator* of this category. The symmetric spaces themselves, the Cartan decomposition, the classification and the rank theory are *Symmetric Spaces* of a later category of this Part, and the group-theoretic side is *Riemannian Symmetric Spaces and the Involution*, the following article of this category. No physics is invoked.

## The Local Geodesic Symmetry

### Definition in Normal Coordinates

**Definition.** Let $(M, g)$ be a Riemannian manifold and $p \in M$. On a normal neighbourhood $U$ of $p$, on which the exponential map $\exp_p$ is a diffeomorphism from a ball of $T_pM$ onto $U$, the **geodesic symmetry** at $p$ is

$$
\sigma_p : U \longrightarrow U, \qquad \sigma_p\bigl(\exp_p(v)\bigr) = \exp_p(-v),
$$

equivalently, on a geodesic $\gamma$ with $\gamma(0) = p$, the map $\sigma_p(\gamma(t)) = \gamma(-t)$. The manifold is symmetric at $p$ if there is a global isometry with these two properties, and **symmetric** if it is connected and symmetric at every point.

**Theorem.** The geodesic symmetry is well defined, smooth and an involution of $U$, it fixes $p$ and only $p$ in $U$, and its differential at $p$ is $-\mathrm{id}$:

$$
\sigma_p(p) = p, \qquad \sigma_p^2 = \mathrm{id}_U, \qquad d(\sigma_p)_p = -\mathrm{id}_{T_pM} .
$$

**Proof.** The exponential map is a diffeomorphism on a ball of $T_pM$, and the reflection $v \mapsto -v$ is a diffeomorphism of the ball, so the composition is a smooth map; applying it twice returns the original point, $\sigma_p^2 = \mathrm{id}$. The fixed points in $U$ are the images of the fixed points of $v\mapsto -v$, that is of $v = 0$, so $p$ is the only fixed point; and the differential at $0$ of $v \mapsto -v$ is $-\mathrm{id}$, which is $d(\sigma_p)_p$ because $d(\exp_p)_0 = \mathrm{id}_{T_pM}$.

### Uniqueness and the Involution Property

**Theorem.** A local isometry defined on a connected neighbourhood of $p$ with $F(p) = p$ and $dF_p = -\mathrm{id}$ coincides with $\sigma_p$ on a normal neighbourhood. Consequently the geodesic symmetry at $p$, when it is a local isometry, is the unique local isometry with these two properties, and it reverses every geodesic through $p$.

**Proof.** Two local isometries with the same value and the same differential at $p$ agree on a connected normal neighbourhood, by the faithfulness argument of *Isometries as Operators*: the composition $F^{-1}\circ\sigma_p$ fixes $p$ with identity differential, so it is the identity. The reversal of the geodesics follows from the definition through the exponential, $\sigma_p(\exp_p v) = \exp_p(-v)$, and the uniqueness of the geodesic with a given initial velocity.

## Locally Symmetric Spaces

### The Three Characterisations

**Definition.** A Riemannian manifold is **locally symmetric** if every point has a neighbourhood on which the geodesic symmetry is a local isometry, equivalently if the local geodesic symmetry at each point is a local isometry.

**Theorem (three characterisations).** For a Riemannian manifold $(M, g)$ the following are equivalent:

**(a)** the local geodesic symmetry at every point is a local isometry;

**(b)** the curvature tensor is parallel, $\nabla R = 0$;

**(c)** the curvature operator is parallel along every curve, equivalently $R$ is invariant under the parallel transport, $P_\gamma R = R$ for every curve.

**Proof sketch.** In **normal coordinates** centred at $p$ the metric has the expansion

$$
g_{ij}(x) = \delta_{ij} - \frac{1}{3}R_{ikjl}(p)\,x^kx^l + O(|x|^3),
$$

in which the curvature at $p$ appears at the second order. The reflection $x\mapsto -x$ is a local isometry for $g$ exactly when all the coefficients of the odd orders vanish; those coefficients are the odd covariant derivatives of the curvature, so the reflection is an isometry on a normal neighbourhood exactly when all the odd covariant derivatives of the curvature vanish there. On an open set this is equivalent to $\nabla R = 0$ there: the parallelism of $R$ forces the vanishing of every covariant derivative, by the theorem below, while the vanishing of the odd derivatives includes the first, $\nabla R = 0$. The third-order coefficient is $\nabla R$ itself, so $\nabla R = 0$ is the obstruction seen at the first order, and applying the argument in a neighbourhood of each point gives (a)$\iff$(b). The equivalence of (b) and (c) is the fact that the covariant derivative of a tensor vanishes exactly when the tensor is parallel along every curve, which is the holonomy principle of *The Parallel Transport Operator*; and (c) is the statement that the curvature is invariant under the transport. The details of the expansion, and of the identification of the odd coefficients with the odd covariant derivatives of the curvature, are in the references.

**Corollary.** A manifold of constant curvature is locally symmetric, since its curvature is a constant multiple of the metric and the metric is parallel. A Riemannian product of locally symmetric manifolds is locally symmetric, since the curvature of the product is the sum of the curvatures of the factors, each parallel. A covering of a locally symmetric manifold is locally symmetric, and so is a quotient by a discrete group of isometries acting freely and properly.

**Proof.** For the constant curvature the tensor $R = \lambda g\wedge g$ is parallel because $g$ is parallel. For the product, the curvature splits and the covariant derivative respects the splitting. The covering and quotient statements are local, and a local symmetry lifts through a covering and descends through a quotient by isometries.

### Parallel Curvature

**Theorem.** On a locally symmetric manifold the covariant derivatives of the curvature vanish to all orders,

$$
\nabla R = 0 \implies \nabla^kR = 0 \quad (k \geq 0),
$$

so the curvature is determined by its value at one point, the curvature operator $\mathcal{R}$ is parallel, and the isometry group acts on the curvature operator by conjugation, $dF_p\,\mathcal{R}_p\,(dF_p)^{-1} = \mathcal{R}_{F(p)}$ with the identification induced by $dF_p$.

**Proof.** The identity $\nabla R = 0$ is differentiated with the Ricci identity to give $\nabla_{X,Y}^2R - \nabla_{Y,X}^2R = R(X,Y)\cdot R$, and the right side is a contraction of $R$ with the parallel $R$, hence vanishes when $\nabla R = 0$; iterating gives the vanishing of all the higher derivatives. The invariance of the operator under transport is the parallel nature of the curvature, and the isometry statement is the naturality of the curvature under an isometry.

## The Symmetry as an Operator

### The Differential and the Fixed Point

**Proposition.** Let $\sigma_p$ be the geodesic symmetry at $p$. Its differential is the reflection of the normal neighbourhood, and the fixed point $p$ is **isolated**: the fixed subspace of $d(\sigma_p)_p = -\mathrm{id}$ is the zero subspace, so the fixed set of the symmetry is the single point $p$, in contrast with the general isometry, whose fixed set is a union of positive-dimensional totally geodesic submanifolds.

**Proof.** The fixed subspace of $-\mathrm{id}$ on $T_pM$ is $\{0\}$, and by the fixed-set theorem of *Isometries as Operators* the component through $p$ of the fixed set is the exponential image of that subspace, hence the point $p$. This is the sharp case of that theorem: an involution with $-\mathrm{id}$ as its differential has a zero-dimensional fixed set.

### The Action on the Curvature Operator

**Proposition.** When $\sigma_p$ is a local isometry it preserves the metric, the connection, the curvature and the curvature operator; on the normal neighbourhood it acts on the curvature operator by

$$
d(\sigma_p)\,\mathcal{R}_{\,x}\bigl(X\wedge Y\bigr)\ =\ \mathcal{R}_{\sigma_p(x)}\bigl(d\sigma_p X\wedge d\sigma_p Y\bigr),
$$

with the tangent spaces identified by $d\sigma_p$, and at the centre it conjugates by $-\mathrm{id}$; since $-\mathrm{id}$ commutes with every operator, $\mathcal{R}_p$ is itself preserved.

**Proof.** The symmetry is an isometry of the normal neighbourhood, so it preserves the connection and the curvature by *Isometries as Operators*, which is the first statement; the formula is the naturality of the curvature operator, and at the centre the conjugation by $-\mathrm{id}$ is the identity because $(-\mathrm{id})\,\mathcal{R}_p\,(-\mathrm{id}) = \mathcal{R}_p$.

**Corollary.** The curvature operator of a locally symmetric space is invariant under the transport, and the holonomy algebra, being generated by the transported curvature by Ambrose–Singer, is generated by the curvature at $p$ alone.

## The Passage to Symmetric Spaces

**Theorem (Cartan).** Let $(M, g)$ be a complete, simply connected, locally symmetric Riemannian manifold. Then for every $p$ the local geodesic symmetry $\sigma_p$ extends to a global isometry of $M$ onto itself, with $\sigma_p(p)=p$ and $d(\sigma_p)_p=-\mathrm{id}$, so $M$ is a symmetric space.

**Proof sketch.** Define the extension along the geodesics from $p$ by $\gamma(t)\mapsto\gamma(-t)$; this is well defined on the whole of $M$ because $M$ is complete; it is smooth because every point is joined to $p$ by geodesics that depend smoothly on the endpoint through the exponential map, and simply connected because the different geodesics from $p$ to a point give the same value of the extension, the ambiguity being measured by the holonomy of a loop, which the parallel curvature makes trivial. The extension is then a local isometry, and a local isometry defined on all of a complete connected manifold is an isometry. The details are in *Symmetric Spaces*, where the geodesic symmetry is taken as the definition and the equivalence with the present local condition is proved.

**Corollary (the general locally symmetric space).** A complete locally symmetric manifold is the quotient $\tilde M/\Gamma$ of its simply connected cover $\tilde M$, which is a symmetric space, by a discrete group $\Gamma$ of isometries of $\tilde M$ acting freely and properly discontinuously; conversely every such quotient is locally symmetric.

**Proof.** The universal cover of a complete manifold is complete and is locally symmetric with the pulled-back metric; it is simply connected, so it is a symmetric space by the theorem. The deck transformations are isometries acting freely and properly discontinuously, and the quotient recovers $M$. The converse is the covering statement of the preceding section.

## Examples

**Example (the model spaces).** Euclidean space is locally symmetric with the symmetry $x\mapsto 2p-x$, the global reflection through $p$. The sphere $S^n$ is symmetric, the symmetry at $p$ being the restriction of the reflection of $\mathbb{R}^{n+1}$ in the line through $p$; on the geodesic through $p$ it sends $\gamma(t)$ to $\gamma(-t)$, as the definition requires. Hyperbolic space, the complex projective space and the other rank-one symmetric spaces are symmetric in the same way.

**Example (the flat torus).** The flat torus $\mathbb{T}^n = \mathbb{R}^n/\mathbb{Z}^n$ is locally symmetric, since it is flat and flatness gives $\nabla R = 0$; but the local symmetry $x\mapsto 2p-x$ of the Euclidean space does not descend to the torus, because it does not commute with the translations of the lattice in general. The torus is therefore locally symmetric and not symmetric, and its simply connected cover $\mathbb{R}^n$ is the symmetric space of which it is a quotient, which is the corollary above read on the simplest example.

**Example (a product).** A product $M_1\times M_2$ of symmetric spaces is symmetric: the symmetry at $(p_1, p_2)$ is the product $\sigma_{p_1}\times\sigma_{p_2}$, whose differential is $-\mathrm{id}$ on each factor, hence $-\mathrm{id}$ on the sum. The decomposable symmetric spaces are the products of the irreducible ones, and the irreducibility of the symmetric space coincides with the irreducibility of the holonomy representation, which is the de Rham decomposition read on this class of examples.

## Summary

The **geodesic symmetry** at $p$ is $\sigma_p(\exp_p v) = \exp_p(-v)$; it is a smooth involution of a normal neighbourhood with the single fixed point $p$ and the differential $-\mathrm{id}$ at $p$, and it is the unique local isometry with these two properties. A Riemannian manifold is **locally symmetric** when the geodesic symmetry at each point is a local isometry, and this holds exactly when $\nabla R = 0$, exactly when the curvature is parallel along every curve, equivalently when the curvature is invariant under the parallel transport. In normal coordinates the metric is $g_{ij}=\delta_{ij}-\frac13R_{ikjl}(0)x^kx^l+O(|x|^3)$, and the reflection $x\mapsto -x$ preserves the metric precisely when the third-order coefficients vanish, that is when $\nabla R = 0$ at the point.

On a locally symmetric manifold all the covariant derivatives of the curvature vanish, $\nabla^kR=0$, the curvature is determined by its value at one point, and the curvature operator is parallel and is preserved by the symmetry; the holonomy algebra is generated by the curvature at a single point. A complete, simply connected, locally symmetric manifold is a **symmetric space**, by the globalisation theorem of Cartan: every local symmetry extends to a global isometry with $\sigma_p(p)=p$ and $d(\sigma_p)_p=-\mathrm{id}$. The general complete locally symmetric manifold is a quotient of a symmetric space by a discrete group of isometries acting freely and properly discontinuously; the flat spaces are the constant-curvature examples with $\nabla R=0$, the sphere, the hyperbolic space and the complex projective space are the simply connected rank-one examples, and the flat torus is locally symmetric but not symmetric.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma_p$, $U$, $\exp_p$ | Geodesic symmetry at $p$; normal neighbourhood; exponential |
| $\sigma_p(\exp_p v) = \exp_p(-v)$ | Definition of the symmetry |
| $\sigma_p^2=\mathrm{id}$, $d(\sigma_p)_p=-\mathrm{id}$ | Involution; differential at the fixed point |
| $\nabla R = 0$ | The local symmetry equation |
| $g_{ij}=\delta_{ij}-\frac13R_{ikjl}x^kx^l+O(|x|^3)$ | Normal-coordinate expansion of the metric |
| $\nabla^kR=0$ | All the covariant derivatives vanish on a locally symmetric space |
| $\mathcal{R}$, $P_\gamma$ | Curvature operator, parallel on a locally symmetric space |
| Cartan extension | A complete simply connected locally symmetric space is symmetric |
| $\tilde M/\Gamma$ | Locally symmetric space as a quotient of a symmetric space |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (Academic Press, 1978), for the geodesic symmetry, the locally symmetric spaces and the globalisation theorem.
- Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry, Volume II* (Interscience, 1969), for the condition $\nabla R=0$ and the local theory of the symmetric spaces.
- Élie Cartan, *Leçons sur la géométrie des espaces de Riemann*, 2nd ed. (Gauthier-Villars, 1946), for the original account of the symmetry of a Riemannian manifold and the extension of the local symmetries.
- Manfredo P. do Carmo, *Riemannian Geometry* (Birkhäuser, 1992), for the normal-coordinate expansion of the metric and the Jacobi fields.
- Sylvestre Gallot, Dominique Hulin and Jacques Lafontaine, *Riemannian Geometry*, 3rd ed. (Springer, 2004), for the locally symmetric spaces and the de Rham decomposition.
