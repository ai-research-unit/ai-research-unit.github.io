# __Hermitian Manifolds and the Geodesic Involution__

## Introduction

The **geodesic involution** is the map of the tangent bundle that reverses every tangent vector, $\iota(v) = -v$, together with its conjugate on the manifold, the geodesic symmetry $\sigma_p$ of a normal neighbourhood of $p$. It is the same map in two coordinates: the exponential map at $p$ intertwines $\iota$ with $\sigma_p$, so $\sigma_p = \exp_p\circ\iota\circ\exp_p^{-1}$, and the symmetry is the geometric face of the linear involution of the tangent space. When the manifold carries a complex structure $J$ compatible with the metric, the geodesic involution is automatically compatible with it at the centre, because $-\mathrm{id}$ commutes with every operator; the question is whether the compatibility persists in a neighbourhood, and the answer is that it does exactly when the complex structure is parallel, which is the condition that makes the symmetric space a **Hermitian symmetric space**.

The article develops the geodesic involution and its compatibility with the complex structure. It defines the involution of the tangent bundle and the geodesic symmetry of a normal neighbourhood and shows that the exponential map conjugates them; it proves that the differential of the symmetry commutes with the complex structure at the centre, so the symmetry is complex-linear there; it proves that the symmetry is holomorphic on a neighbourhood exactly when the complex structure is parallel there, equivalently when the metric is Kähler and the space is locally symmetric; it reads the tangent-space splitting under the involution and the complex structure, and it states the condition on the Cartan decomposition that makes the symmetric space Hermitian; and it gives the examples of the flat, the projective and the hyperbolic Hermitian symmetric spaces.

The article assumes the geodesic symmetry and the locally symmetric spaces of *The Geodesic Symmetry and Locally Symmetric Spaces*, the symmetric spaces and the Cartan decomposition of *Riemannian Symmetric Spaces and the Involution* and the isometric involution of the two following articles of this category; the exponential map and the geodesics of *Riemannian Geometry*. The complex structure, the Hermitian metric, the fundamental form and the Kähler condition are *Hermitian Geometry and Almost Complex Structures* in a later category of this Part; the Hermitian symmetric spaces, the group involution and the Bergman metric are *Hermitian Symmetric Spaces and the Group Involution* and *Hermitian Symmetric Spaces and the Bergman Metric* in later categories; all are named below as forward references, and the article states the compatibility of the involution with the complex structure without developing the holomorphic geometry. No physics is invoked.

## The Geodesic Involution

### On the Tangent Space and on the Manifold

**Definition.** The **geodesic involution** of a Riemannian manifold $(M, g)$ is the fibre-preserving involution of the tangent bundle

$$
\iota : TM \longrightarrow TM, \qquad \iota(v) = -v,
$$

that reverses every tangent vector. It is smooth, it commutes with the bundle projection, and it restricts on each fibre $T_pM$ to the central symmetry $-\mathrm{id}$. Its orbits are the pairs $\{v, -v\}$ at the nonzero vectors and the single zero vector; the orbit space $TM/\iota$ is the **unoriented tangent bundle**, in which a direction is a line through the origin rather than an oriented vector.

**Definition.** The **geodesic symmetry** at $p$ is the conjugate of $\iota$ by the exponential map,

$$
\sigma_p = \exp_p\circ\iota\circ\exp_p^{-1} : U \longrightarrow U, \qquad \sigma_p\bigl(\exp_p(v)\bigr) = \exp_p(-v),
$$

on a normal neighbourhood $U$ of $p$; the previous articles of this category use it as the defining involution of a locally symmetric space.

**Theorem.** The geodesic symmetry is an involution of the normal neighbourhood, fixing $p$ alone and reversing every geodesic through $p$, and its differential at $p$ is the geodesic involution of the tangent space:

$$
\sigma_p^2 = \mathrm{id}, \qquad d(\sigma_p)_p = -\mathrm{id} = \iota|_{T_pM} .
$$

Along the geodesic $\gamma$ with $\gamma(0)=p$ the symmetry acts by $\gamma(t)\mapsto\gamma(-t)$, and on the tangent bundle along $\gamma$ its differential acts by the transport followed by the reversal, $d(\sigma_p)_{\gamma(t)} = -\iota\circ P_{t\to -t}$, where $P$ is the parallel transport along the geodesic.

**Proof.** The first statements are the definition of the geodesic symmetry of *The Geodesic Symmetry and Locally Symmetric Spaces*, read through the conjugation by the exponential map; the differential at the centre is $d(\exp_p)_0\circ(-\mathrm{id})\circ(d\exp_p)_0^{-1} = -\mathrm{id}$, since $d(\exp_p)_0=\mathrm{id}$. Along the geodesic the symmetry reverses the parameter, and its differential at $\gamma(t)$ carries the tangent vector at $\gamma(t)$ to the corresponding vector at $\gamma(-t)$, which is the transport followed by the reversal of the direction; the reversal is the involution $\iota$.

### The Involution as the Centrepiece

**Proposition.** Every isometric involution of a Riemannian manifold with a fixed point $p$ at which the differential is $-\mathrm{id}$ is the geodesic symmetry at $p$; every reflection in a totally geodesic submanifold is a composition of the geodesic symmetries of the points of the submanifold with a reflection of the normal bundle, and the geodesic involution of the tangent space is the linear model of all of them. The geodesic involution is the unique isometric involution of the tangent space with the zero section as fixed set and the differential $-\mathrm{id}$ there.

**Proof.** The uniqueness of the isometric involution with $d=-id$ at a fixed point is the uniqueness of the geodesic symmetry of *The Geodesic Symmetry and Locally Symmetric Spaces*. On the tangent space, an isometry of the Euclidean space fixing the origin is linear, and the linear isometry with differential $-\mathrm{id}$ at the origin is $-\mathrm{id}$ itself; the zero section is its fixed set. The reflection statement is the tube theorem of *Isometric Involutions and the Fixed-Point Set*, the reflection being the reversal in the normal direction.

## The Compatibility with the Complex Structure

### The Involution Commutes with the Complex Structure

Suppose now that $(M, g, J)$ is a **Hermitian manifold**: $J$ is an almost complex structure, $J^2 = -\mathrm{id}$, and the metric is Hermitian, $g(JX, JY) = g(X, Y)$. The complex structure, the Hermitian metric and the fundamental form are the subject of *Hermitian Geometry and Almost Complex Structures* in a later category of this Part, and are used here only through the compatibility of $J$ with the involution.

**Theorem.** The geodesic involution commutes with every complex structure on the tangent space:

$$
\iota\circ J = J\circ\iota, \qquad \iota(Jv) = -Jv = J(-v) = J\iota(v).
$$

Consequently the differential of the geodesic symmetry at its centre is complex-linear, $d(\sigma_p)_p\circ J_p = J_p\circ d(\sigma_p)_p$, and the symmetry is a **holomorphic** map at $p$: it agrees with a holomorphic map to the first order. The symmetry reverses the **holomorphic** and the **anti-holomorphic** directions without exchanging them, in contrast with the anti-holomorphic real structures of *Real Structures on a Riemannian Manifold*, which exchange the two types.

**Proof.** The identity is the fact that $-\mathrm{id}$ is a scalar and commutes with every operator; the complex-linearity of $d(\sigma_p)_p=-\mathrm{id}$ is the same statement. The holomorphy at the point is the complex-linearity of the differential, and the comparison with the anti-holomorphic case is the commutation rule $d\sigma\circ J = -J\circ d\sigma$ of the real structure.

### The Parallel Complex Structure

**Theorem (the compatibility condition, quoted from the Hermitian geometry).** The geodesic symmetry is holomorphic on a whole neighbourhood of $p$ exactly when the complex structure is **parallel** at $p$ in the sense of the Levi-Civita connection,

$$
(\nabla J)_p = 0 \quad \text{equivalently} \quad \nabla J = 0 \text{ on the neighbourhood},
$$

and when this holds at every point the metric is **Kähler** and the manifold is **locally Hermitian symmetric**; conversely a Kähler manifold that is locally symmetric is Hermitian symmetric, its geodesic symmetry being holomorphic.

**Proof sketch.** The differential of the symmetry commutes with $J$ at the centre, and one differentiates this commutation along the normal neighbourhood; the derivative of the relation is the vanishing of $\nabla J$ transported by the symmetry, so the holomorphy of the symmetry on the neighbourhood is equivalent to the parallelism of $J$ there. The Kähler condition enters because $\nabla J=0$ with the Levi-Civita connection is equivalent to the closedness of the fundamental form together with the integrability of $J$, and this is developed in *Hermitian Geometry and Almost Complex Structures*. The local symmetry is *The Geodesic Symmetry and Locally Symmetric Spaces*, and the combination of $\nabla J=0$ and $\nabla R=0$ is the locally Hermitian symmetric condition.

**Corollary.** On a Hermitian manifold the geodesic symmetry at a point is holomorphic at the point always, and holomorphic on a neighbourhood exactly when the complex structure is parallel there; on a Hermitian symmetric space, where the symmetry is defined globally, it is a global holomorphic isometry.

## Hermitian Symmetric Spaces

**Definition.** A **Hermitian symmetric space** is a symmetric space that is Hermitian, equivalently a connected Kähler manifold with, at every point, a holomorphic involutive isometry fixing the point with differential $-\mathrm{id}$. The geodesic symmetry of a Hermitian symmetric space is a global holomorphic isometry, and the space is homogeneous under its group of holomorphic isometries.

**Theorem.** A Hermitian symmetric space is a symmetric space whose complex structure is parallel; the geodesic symmetry at every point is then holomorphic, its differential $-\mathrm{id}$ being complex-linear, and the parallel complex structure is the one for which the symmetric structure is complex. In the Cartan decomposition the complex structure is an endomorphism of $\mathfrak{p}$ with $J^2 = -\mathrm{id}$, and the complexified tangent space $\mathfrak{p}\otimes\mathbb{C}$ splits into the $(+i)$- and $(-i)$-eigenspaces $\mathfrak{p}_+\oplus\mathfrak{p}_-$; the symmetric space is Hermitian exactly when

$$
[\mathfrak{p}_+,\mathfrak{p}_+] = 0,
$$

equivalently when the centre of $\mathfrak{k}$ is one-dimensional in the compact type and the complexified isotropy has a one-dimensional centre.

**Proof sketch.** The holomorphy of the geodesic symmetry is the compatibility theorem above, and the parallelism of $J$ is its metric content. The decomposition $\mathfrak{p}\otimes\mathbb{C}=\mathfrak{p}_+\oplus\mathfrak{p}_-$ is the eigenspace decomposition of the complex structure acting on the tangent space, whose eigenvalues are $\pm i$; the vanishing $[\mathfrak{p}_+,\mathfrak{p}_+]=0$ is the integrability of the almost complex structure, the Nijenhuis tensor being expressed by the bracket of the two eigenspaces, and it also forces the isotropy to have the one-dimensional centre from which $J$ is built. The details are the theory of the Hermitian symmetric spaces, in the later categories of this Part.

**Corollary.** A Hermitian symmetric space is Kähler, its complex structure is parallel, and its curvature tensor is invariant under $J$: $R(JX, JY) = R(X, Y)$. The Ricci form is invariant, and the space is **Einstein** when it is irreducible; the Bergman metric, the bounded symmetric domains and the classification are the subjects of the later Hermitian symmetric articles.

## Examples

**Example (the flat space).** On $\mathbb{C}^n$ with the Euclidean Hermitian metric the complex structure is parallel, the geodesic symmetry at a point is $v\mapsto 2p-v$, holomorphic, and the space is a flat Hermitian symmetric space; the geodesic involution of the tangent space is the central symmetry, commuting with $J$.

**Example (the complex projective space).** The complex projective space $\mathbb{CP}^n$ with the Fubini–Study metric is a Hermitian symmetric space of compact type: the geodesic symmetry at a point is the holomorphic map induced by the reflection in the corresponding complex line, the complex structure is parallel and the space is Kähler, of positive holomorphic sectional curvature. The complex Grassmannians are Hermitian symmetric in the same way, the symmetry at a subspace being induced by the reflection fixing the subspace and reversing its orthogonal complement, which is complex-linear.

**Example (the complex hyperbolic space and the ball).** The complex hyperbolic space $\mathbb{CH}^n$ and the unit ball with the Bergman metric are Hermitian symmetric spaces of noncompact type: the complex structure is parallel, the geodesic symmetry at a point is holomorphic, and the space is the bounded symmetric domain of the rank-one case. The correspondence between the bounded symmetric domains and the Hermitian symmetric spaces of noncompact type is the Harish-Chandra realization, and it is the subject of *Hermitian Symmetric Spaces and the Bergman Metric* in a later category of this Part.

## Summary

The **geodesic involution** is the map $\iota(v) = -v$ of the tangent bundle, and the **geodesic symmetry** $\sigma_p = \exp_p\circ\iota\circ\exp_p^{-1}$ on a normal neighbourhood is its conjugate by the exponential map; the symmetry is the unique isometric involution fixing $p$ alone with differential $-\mathrm{id}$ at $p$, and the involution of the tangent space is the linear model of every reflection. On a Hermitian manifold the involution commutes with the complex structure, $\iota J = J\iota$, because $-\mathrm{id}$ is a scalar, so the differential of the symmetry at its centre is complex-linear and the symmetry is holomorphic at $p$; it reverses the holomorphic and the anti-holomorphic directions without exchanging them, in contrast with the anti-holomorphic real structures. The symmetry is holomorphic on a neighbourhood exactly when the complex structure is parallel, $\nabla J = 0$ there, and then the metric is Kähler and the manifold locally Hermitian symmetric; a Kähler locally symmetric manifold is Hermitian symmetric.

A **Hermitian symmetric space** is a symmetric space that is Hermitian, equivalently a Kähler manifold with, at each point, a holomorphic involutive isometry of differential $-\mathrm{id}$. Its tangent-space splitting $V_+\oplus V_-$ is complex because $J$ commutes with the involution, and in the Cartan decomposition the complex structure is an endomorphism of $\mathfrak{p}$ with $\mathfrak{p}\otimes\mathbb{C} = \mathfrak{p}_+\oplus\mathfrak{p}_-$ and $[\mathfrak{p}_+,\mathfrak{p}_+]=0$. Such a space is Kähler with parallel complex structure and $J$-invariant curvature, and it is Einstein when irreducible; the flat space, the complex projective space, the complex Grassmannians and the complex hyperbolic space with the Bergman metric are the standard examples, the last corresponding to the bounded symmetric domains in the Harish-Chandra realization. The holomorphic geometry, the group involution and the Bergman metric are the later Hermitian symmetric articles of this Part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\iota(v) = -v$ | Geodesic involution of the tangent bundle |
| $\sigma_p = \exp_p\circ\iota\circ\exp_p^{-1}$ | Geodesic symmetry; conjugate of the involution |
| $d(\sigma_p)_p = -\mathrm{id}$ | Differential at the centre; the linear involution |
| $TM/\iota$ | Unoriented tangent bundle; quotient by the involution |
| $J$, $J^2=-\mathrm{id}$, $g(JX,JY)=g(X,Y)$ | Complex structure and Hermitian metric |
| $\iota J = J\iota$ | Compatibility: the involution is complex-linear |
| $(\nabla J)_p = 0$, $\nabla J=0$ | Parallel complex structure; Kähler; the symmetry holomorphic |
| Hermitian symmetric space | Kähler symmetric space with holomorphic geodesic symmetry |
| $V_+\oplus V_-$, complex splitting | Eigenspaces of the involution, both $J$-invariant |
| $\mathfrak{p}_+\oplus\mathfrak{p}_-$, $[\mathfrak{p}_+,\mathfrak{p}_+]=0$ | Hermitian condition in the Cartan decomposition |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (Academic Press, 1978), for the Hermitian symmetric spaces, the holomorphic geodesic symmetry and the Cartan decomposition.
- Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry, Volume II* (Interscience, 1969), for the Hermitian and Kähler manifolds and the parallel complex structure.
- Arthur L. Besse, *Einstein Manifolds* (Springer, 1987), for the Hermitian symmetric spaces, their curvature, the Ricci form and the Einstein condition.
- Ottmar Loos, *Bounded Symmetric Domains and Jordan Pairs* (University of California, Irvine, 1977), for the bounded symmetric domains and the Hermitian symmetric spaces of noncompact type.
- Andrei Moroianu, *Lectures on Kähler Geometry* (Cambridge University Press, 2007), for the Kähler condition, the Hermitian metrics and the parallel complex structure.
