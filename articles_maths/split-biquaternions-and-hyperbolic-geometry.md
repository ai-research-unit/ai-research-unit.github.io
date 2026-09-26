
# __Split-Biquaternions and Hyperbolic Geometry__

## Introduction

This article is the hyperbolic-geometric slot of the split biquaternion system. It presents hyperbolic three-space as a model carried by the split biquaternion algebra: the points are the elements of the anti-Hermitian four-plane $\mathbb{M}_-$ whose Hermitian norm is $-1$, the isometry group is the restricted Lorentz group realised on that plane, and the boundary and the geodesics are read off from the null cone and from the two-dimensional subspaces of the algebra. The article continues the geometry of the same system from *Split-Biquaternion Geometry* and uses the Lorentz group of *Split-Biquaternion Rotations and the Lorentz Group*; it does not restate the forms, the invariant subspaces or the classification of isometries that are established there, but develops from them the metric geometry of the hyperbolic space itself.

The two-dimensional analogue is the hyperbolic geometry of the split complex plane, treated in *Hyperbolic Rotations* and in *Hyperbolic Geometry* in Part II; the general theory of hyperbolic manifolds, of their geodesics and of their boundaries is the subject of *Hyperbolic Geometry* and of *Pseudo-Riemannian and Lorentzian Geometry*, written in parallel, and is cited rather than reproduced. The corresponding construction for the biquaternion algebra, in which hyperbolic three-space appears through Hermitian matrices and $SL_2(\mathbb{C})$, is the subject of *Biquaternion Null Quadric and Projective Geometry* and of the written biquaternion articles; the present article is the split biquaternion realisation and not that one. The quaternion sphere $S^3$ is used as the comparison object throughout, as in *Quaternion Geometry*.

**Conventions.** The split biquaternion algebra is $\mathbb{H}_{\mathbb{D}} = \mathbb{D}\otimes_{\mathbb{R}}\mathbb{H}$ with the basis $e_0 = 1, e_1, e_2, e_3$, $e_k^2 = -e_0$, and the central split complex unit $j$, $j^2 = +e_0$. The Hermitian scalar form is $g(\tilde P,\tilde Q) = \operatorname{Sc}(\tilde P\tilde Q^{\dagger})$, of signature $(4,4)$ on $\mathbb{H}_{\mathbb{D}}$; its restrictions to the Hermitian subspace $\mathbb{M}_+$ and to the anti-Hermitian subspace $\mathbb{M}_-$ have signatures $(1,3)$ and $(3,1)$. The anti-Hermitian subspace is

$$
\mathbb{M}_- = \left\{a\,je_0 + v : a\in\mathbb{R},\ v\in\operatorname{Im}\mathbb{H}\right\}
= \left\{a\,je_0 + v_1e_1 + v_2e_2 + v_3e_3\right\},
$$

a real four-space with the $g$-orthogonal basis $(je_0,e_1,e_2,e_3)$ and the form

$$
g(\tilde X,\tilde X) = -a^2 + v_1^2 + v_2^2 + v_3^2 .
$$

An element of $\mathbb{M}_-$ of $g$-norm $-1$ is called a **split biquaternion of unit norm**; this is the indefinite unit condition, and it is the condition that selects the points of the hyperbolic space.

## The Hyperboloid Model

### The Hyperbolic Three-Space

**Definition.** The **hyperboloid model** of hyperbolic three-space is

$$
H^3 = \left\{\tilde X\in\mathbb{M}_- : g(\tilde X,\tilde X) = -1,\ a > 0\right\},
$$

where $\tilde X = a\,je_0 + v$; the sign condition $a > 0$ selects one of the two connected components of the level set $g = -1$.

**Theorem.** $H^3$ is a connected smooth three-dimensional submanifold of $\mathbb{M}_-$, diffeomorphic to $\mathbb{R}^3$; the diffeomorphism is

$$
v\longmapsto \sqrt{1 + \lvert v\rvert^2}\,je_0 + v, \qquad v\in\operatorname{Im}\mathbb{H}\cong\mathbb{R}^3,
$$

with inverse $\tilde X\mapsto\operatorname{Vect}(\tilde X)$. The tangent space at $\tilde X\in H^3$ is the $g$-orthogonal complement of $\tilde X$, and $g$ is positive definite on it.

*Proof.* The map displayed has $g$-norm $-(1+\lvert v\rvert^2) + \lvert v\rvert^2 = -1$ and $a = \sqrt{1+\lvert v\rvert^2} > 0$, so it lands in $H^3$; its inverse is the vector part, and the two are smooth and mutually inverse, so $H^3\cong\mathbb{R}^3$. For the tangent space, differentiate the relation $g(\tilde X,\tilde X) = -1$ along a curve in $H^3$ to obtain $g(\tilde X,\dot{\tilde X}) = 0$, so the tangent space lies in the orthogonal complement, which has dimension three because $g(\tilde X,\tilde X)\neq0$; hence they agree. The form is positive definite on that complement: the index of a form is additive over orthogonal direct sums of non-degenerate subspaces, the ambient form on $\mathbb{M}_-$ has index one, and the line $\mathbb{R}\tilde X$ already carries the negative direction, so the orthogonal complement has index zero. $\square$

The second component of the level set $g = -1$ is the image of $H^3$ under the central reflection $\tilde X\mapsto-\tilde X$, and is the second sheet; the two sheets together form the full level set and are interchanged by the group $O(3,1)$. The manifold $H^3$ is non-compact and simply connected, and its curvature is constant and negative.

### The Metric

**Definition.** The **hyperbolic distance** on $H^3$ is

$$
d_H(\tilde X,\tilde Y) = \operatorname{arcosh}\!\left(-g(\tilde X,\tilde Y)\right), \qquad \tilde X,\tilde Y\in H^3 .
$$

**Theorem.** The hyperbolic distance is a metric on $H^3$, it is invariant under every linear isometry of $(\mathbb{M}_-,g)$ that preserves the sheet, and $H^3$ with this metric is a complete Riemannian manifold of constant sectional curvature $-1$. Its isometry group is

$$
\operatorname{Isom}(H^3) = O^{\uparrow}(3,1),
$$

the subgroup of $O(3,1)$ preserving the chosen sheet, of index two in $O(3,1)$ and with identity component

$$
\operatorname{Isom}(H^3)_0 = SO^{+}(3,1)\cong PSL_2(\mathbb{C}) ,
$$

acting transitively and with isotropy at a point the group $SO(3)$; hence

$$
H^3\cong SO^{+}(3,1)/SO(3)\cong PSL_2(\mathbb{C})/PSU(2)
$$

as a homogeneous space, and the stabiliser of a point acts on the tangent space by the standard representation of $SO(3)$.

*Proof.* The argument $-g(\tilde X,\tilde Y)$ is at least $1$ for $\tilde X,\tilde Y$ on the same sheet, because the reverse Schwarz inequality for a form of signature $(3,1)$ gives $g(\tilde X,\tilde Y)^2\geq g(\tilde X,\tilde X)g(\tilde Y,\tilde Y) = 1$ with the negative sign of $g$; so the arcosh is defined and non-negative, and it vanishes exactly at $\tilde X = \tilde Y$. The triangle inequality is the corresponding form of the reverse Schwarz inequality, applied to the three pairs. Invariance under a linear isometry preserving the sheet is immediate from the invariance of $g$. Completeness is the completeness of the hyperboloid in the ambient Euclidean space. The curvature computation is the standard one for the hyperboloid model. The group $O(3,1)$ has four components, and the subgroup preserving a chosen sheet is of index two; its identity component is $SO^{+}(3,1)$, which is isomorphic to $PSL_2(\mathbb{C})$ by the standard two-to-one covering $SL_2(\mathbb{C})\to SO^{+}(3,1)$, and has trivial centre so that no further quotient is needed. The orbit and isotropy statements are the orbit theory of the Lorentzian form, treated in *Pseudo-Riemannian and Lorentzian Geometry*. $\square$

### Geodesics and Two-Dimensional Subspaces

**Theorem.** The geodesics of $H^3$ through a point $\tilde X$ are the intersections of $H^3$ with the two-dimensional real subspaces of $\mathbb{M}_-$ through the origin that are spanned by $\tilde X$ and a tangent vector, and are therefore the curves

$$
t\longmapsto \cosh t\,\tilde X + \sinh t\,\tilde V, \qquad \tilde X\in H^3,\ \tilde V\in T_{\tilde X}H^3,\ g(\tilde V,\tilde V) = 1,\ g(\tilde X,\tilde V) = 0 .
$$

Every geodesic is the orbit of a hyperbolic one-parameter subgroup of $SO^{+}(3,1)$, and the intersection of the geodesic with the plane $\operatorname{span}(\tilde X,\tilde V)$ is the hyperbola $\{-a^2 + \text{(one coordinate)}^2 = -1\}$ in that plane.

*Proof.* A geodesic of the hyperboloid model is the intersection of $H^3$ with a two-dimensional linear subspace $P$ on which the ambient form has signature $(1,1)$, because the second fundamental form of the hyperboloid in $\mathbb{M}_-$ is minus the ambient form and the geodesic curvature vanishes on such intersections. Parametrising the plane $P$ by an orthonormal pair $(\tilde X,\tilde V)$ with $g(\tilde X,\tilde X) = -1$, $g(\tilde V,\tilde V) = +1$, $g(\tilde X,\tilde V) = 0$ gives the displayed curve, which has $g$-norm $-1$ and is the unit hyperbola in the plane. The one-parameter group statement is the classification of the hyperbolic generators of $\mathfrak{so}(3,1)$; it is the second row of the three-row table of *Split-Biquaternion Rotations and the Lorentz Group*. $\square$

## The Boundary and the Conformal Model

### The Sphere at Infinity

**Definition.** The **boundary at infinity** of the hyperboloid model is the set of rays of the null cone,

$$
\partial H^3 = \left\{[\tilde X] : \tilde X\in\mathbb{M}_-,\ \tilde X\neq 0,\ g(\tilde X,\tilde X) = 0\right\},
$$

the projectivisation of the null cone in $\mathbb{M}_-$.

**Theorem.** The boundary is a two-sphere,

$$
\partial H^3\cong S^2 ,
$$

and the map $\tilde X = a\,je_0 + v\mapsto v/\lvert v\rvert$ realises the boundary as the unit sphere of $\operatorname{Im}\mathbb{H}$, the boundary point of a null vector being its direction. On the boundary the group $SO^{+}(3,1)$ acts by the conformal transformations of the round sphere, and the boundary carries a conformal structure rather than a Riemannian one.

*Proof.* A null vector has $-a^2 + \lvert v\rvert^2 = 0$, so $a = \pm\lvert v\rvert$ with $v\neq0$; the ray is determined by the direction of $v$ in the unit sphere of $\operatorname{Im}\mathbb{H}$, which is $S^2$, and by the sign of $a$, and two null vectors on the same ray have the same direction and the same sign. The conformal action is the standard boundary action of the isometry group of a hyperbolic space. $\square$

### The Boundary as the Projective Line Over the Complex Numbers

The boundary sphere has a preferred conformal structure, and it is the same structure that the complex projective line carries.

**Proposition.** The boundary sphere $\partial H^3$ is conformally equivalent to the Riemann sphere $\mathbb{C}P^1$; the equivalence is realised by stereographic projection from the null cone of $\mathbb{M}_-$ onto the plane $\{a = 1\}$ in the coordinates $\tilde X = a\,je_0 + v$, which is a copy of $\mathbb{R}^2$ completed by one point. Under this equivalence the action of $SO^{+}(3,1)$ on $\partial H^3$ becomes the action of $PSL_2(\mathbb{C})$ on $\mathbb{C}P^1$ by Möbius transformations,

$$
z\longmapsto\frac{\alpha z + \beta}{\gamma z + \delta}, \qquad \begin{pmatrix}\alpha & \beta\\ \gamma & \delta\end{pmatrix}\in SL_2(\mathbb{C}),
$$

and the isomorphism $SO^{+}(3,1)\cong PSL_2(\mathbb{C})$ is the isomorphism of their boundary actions.

*Proof.* Stereographic projection is conformal and sends the round sphere to the plane completed by a point, which is $\mathbb{C}P^1$; the identification of the boundary action with the Möbius action is the classical identification of the conformal group of the two-sphere with $PGL_2(\mathbb{C})$, and the isomorphism of $SO^{+}(3,1)$ with $PSL_2(\mathbb{C})$ is the standard exceptional isomorphism of the corresponding Lie algebras. $\square$

This is the point at which the complex numbers enter the split biquaternion description of hyperbolic three-space, and it is the reason why the isometry group of this hyperbolic space is also the group $SL_2(\mathbb{C})$ of the biquaternion algebra; the biquaternion realisation of the same geometry, through $2\times2$ Hermitian matrices, is treated in *Biquaternion Null Quadric and Projective Geometry* and is a different presentation of the same group.

### The Ball Model and the Upper Half-Space Model

**Definition.** The **Klein model** is the image of $H^3$ under the central projection of the hyperboloid onto the affine plane $\{a = 1\}$ along rays from the origin; it is the open unit ball of $\operatorname{Im}\mathbb{H}$.

**Proposition.** The central projection is a diffeomorphism from $H^3$ onto the open unit ball of $\mathbb{R}^3$, and it carries the geodesics of $H^3$ to the straight chords of the ball. The composition of the central projection with the inverse of the stereographic projection is the **Poincaré ball model**, in which the geodesics are circular arcs orthogonal to the boundary sphere and the metric is $4\lvert dv\rvert^2/(1 - \lvert v\rvert^2)^2$. The **upper half-space model** is obtained by a conformal transformation of the boundary sphere carrying a point of the boundary to infinity; in that model the geodesics are vertical rays and the semicircles orthogonal to the boundary plane, and the metric is $\lvert dv\rvert^2/v_3^2$ for a coordinate $v_3 > 0$.

*Proof.* The central projection sends the ray through $\tilde X = aje_0 + v$ to $v/a$ with $\lvert v\rvert < a$, and $a^2 = 1+\lvert v\rvert^2$ gives $\lvert v/a\rvert < 1$, so the image is the open unit ball, and it is a diffeomorphism because the inverse is $v\mapsto\sqrt{1+\lvert v\rvert^2}\,je_0 + v$ with $v$ in the ball. Lines through the origin of the ball are the intersections of two-dimensional subspaces with the hyperboloid and are therefore geodesics; conversely every geodesic lies in such a subspace, so the geodesics are the chords. The conformal statements are the standard equivalences of the models of hyperbolic space, in *Hyperbolic Geometry*. $\square$

## The Isometries and Their Classification

### The Three Types

The classification of one-parameter subgroups established in *Split-Biquaternion Rotations and the Lorentz Group* acquires a geometric meaning in the action on $H^3$.

**Theorem.** Every non-identity element of $SO^{+}(3,1)$ is of exactly one of the following three types, according to the behaviour of its action on $H^3$:

- **Elliptic.** The element fixes a point of $H^3$; its geodesic displacement is zero; it rotates the tangent space at the fixed point. The elliptic elements form the conjugates of the maximal compact subgroup $SO(3)$.
- **Hyperbolic.** The element fixes no point of $H^3$ and fixes exactly two points of $\partial H^3$; it translates along the geodesic joining them, by a distance $\ell > 0$ called the translation length, and the geodesic is the unique invariant geodesic.
- **Parabolic.** The element fixes no point of $H^3$ and fixes exactly one point of $\partial H^3$; it translates every point by an unbounded amount and preserves the horospheres based at the fixed boundary point.

*Proof.* The fixed points of an element of $SO^{+}(3,1)$ on $H^3\cup\partial H^3$ correspond to the lines in $\mathbb{M}_-$ spanned by eigenvectors of the corresponding linear map, and the type is determined by the sign of the $g$-norm of such an eigenvector: timelike (a point of $H^3$), spacelike (a geodesic, whose endpoints are two null eigenvectors) or null (a boundary point). The normal forms are those of the generator, given by the three-row table of *Split-Biquaternion Rotations and the Lorentz Group*. $\square$

**Proposition.** The elliptic type is realised inside the split biquaternion algebra by the unitary group of *Split-Biquaternion Rotations and the Lorentz Group*, which acts on $H^3$ by rotations about the fixed point $je_0$; the hyperbolic type is realised by the split complex hyperbolic units acting on the neutral planes, transported to $H^3$; the parabolic type is not realised by an element of the algebra, because $\mathbb{H}_{\mathbb{D}}\cong\mathbb{H}\oplus\mathbb{H}$ is semisimple and has no non-zero nilpotent element.

*Proof.* The assertions about the elliptic and parabolic types are those of the cited article, transported through the identification $H^3 = SO^{+}(3,1)\cdot je_0$; the hyperbolic displacements are the split complex units, which furnish one-parameter subgroups of hyperbolic type after conjugation into $SO^{+}(3,1)$. $\square$

### Horospheres and the Busemann Function

**Definition.** For a boundary point $\xi = [\tilde N]\in\partial H^3$ and a real number $s$, the **horosphere** centred at $\xi$ is

$$
\operatorname{Hor}(\xi,s) = \left\{\tilde X\in H^3 : -\log\!\left(-g(\tilde X,\tilde N)\right) = s\right\},
$$

where $\tilde N$ is a null vector on the ray $\xi$, normalised so that the sign of $g(\tilde X,\tilde N)$ is positive for all $\tilde X\in H^3$.

**Proposition.** Every horosphere is a smooth surface diffeomorphic to $\mathbb{R}^2$, it is orthogonal to every geodesic ending at $\xi$, and the parabolic one-parameter subgroups act simply transitively on it. In the upper half-space model with $\xi$ the point at infinity, the horospheres are the horizontal planes.

*Proof.* The function $\tilde X\mapsto-\log(-g(\tilde X,\tilde N))$ is the Busemann function of the ray $\xi$; its level sets are the horospheres, and the standard properties of the Busemann function give the orthogonality to the geodesics ending at $\xi$ and the transitivity of the parabolic stabiliser, whose Lie algebra is the nilpotent part of the Iwasawa decomposition of $\mathfrak{so}(3,1)$; in the upper half-space model the level sets of the height function are horizontal planes. $\square$

Note that the parabolic subgroups of $SO^{+}(3,1)$ are represented by nilpotent elements of the Lie algebra although the split biquaternion algebra contains no nilpotent; the nilpotents reside in the Lie algebra of the isometry group and not in the coefficient algebra. This is the geometric form of the negative statement of *Split-Biquaternion Rotations and the Lorentz Group*.

## Comparison with the One-Dimensional and the Spherical Cases

The split biquaternion hyperbolic geometry is the three-dimensional member of a family that begins in dimension one with the split complex plane and continues in the opposite direction with the quaternion sphere.

| Feature | $\mathbb{D}$ (dimension $1$) | $\mathbb{H}_{\mathbb{D}}$ (dimension $3$) | $\mathbb{H}$ (sphere) |
|---|---|---|---|
| Ambient form | $x^2 - y^2$ on $\mathbb{D}$ | $g$ on $\mathbb{M}_-\sim(3,1)$ | $\lvert q\rvert^2$ on $\mathbb{H}$ |
| Level set | hyperbola $c^2 - s^2 = 1$ | hyperboloid $g = -1$ | sphere $S^3$ |
| Space | $H^1\cong\mathbb{R}$ | $H^3\cong\mathbb{R}^3$ | $S^3$ |
| Curvature | $-1$ | $-1$ | $+1$ |
| Isometry group | $O^{\uparrow}(1,1)$ | $O^{\uparrow}(3,1)$ | $O(4)$ |
| Identity component | $SO^{+}(1,1)$, one-dimensional | $SO^{+}(3,1)\cong PSL_2(\mathbb{C})$ | $SO(4)\cong(S^3\times S^3)/\{\pm1\}$ |
| Boundary | two points | $S^2\cong\mathbb{C}P^1$ | empty |
| Geodesics | the two branches | hyperbolas in $(1,1)$-planes | great circles |
| Stabiliser of a point | trivial | $SO(3)$ | $SO(3)$ |
| Isometries | hyperbolic only | elliptic, hyperbolic, parabolic | elliptic only |

Two features of the table deserve emphasis. First, the one-dimensional case has only hyperbolic isometries: the group $SO^{+}(1,1)$ is a single one-parameter family, and the three types of the three-dimensional case collapse to one because there is no compact isotropy and no nilpotent part. The passage to dimension three creates the compact rotations of $\operatorname{Im}\mathbb{H}$ and, at the same time, the parabolic boundary-fixing isometries. Second, the compact case is exactly complementary: the quaternion sphere has only elliptic isometries, no boundary, and the form is definite, while the split biquaternion hyperbolic space has a boundary of dimension two, a non-compact isometry group and a non-compact space.

The relation to the split complex plane is not merely an analogy: the split complex hyperbolic one-parameter group $\{e^{\theta j}\}$ of *Hyperbolic Rotations* sits inside the split biquaternion algebra as the one-parameter group of the neutral plane, and its action on $H^1$ is the restriction of the action on $H^3$ to the invariant geodesic of a hyperbolic isometry. In this sense the one-dimensional hyperbolic geometry is the skeleton of the three-dimensional one, the remaining content being the compact rotations of the two-sphere at infinity and the parabolic translations.

## Summary

The anti-Hermitian four-plane $\mathbb{M}_-$ of the split biquaternion algebra, with the Hermitian form $g$ of signature $(3,1)$, carries the hyperboloid model of hyperbolic three-space: the points are the elements of Hermitian norm $-1$ with a positive $je_0$-coordinate, the space is diffeomorphic to $\mathbb{R}^3$, and its metric is $d_H(\tilde X,\tilde Y) = \operatorname{arcosh}(-g(\tilde X,\tilde Y))$, complete of constant curvature $-1$. Its isometry group is $O(3,1)/\{\pm1\}$, acting transitively with isotropy $SO(3)$, so that $H^3\cong SO^{+}(3,1)/SO(3)$.

The geodesics are the intersections of $H^3$ with the two-dimensional subspaces of signature $(1,1)$, equivalently the orbits of the hyperbolic one-parameter subgroups, and they are hyperbolas in their planes. The boundary at infinity is the projectivised null cone and is a two-sphere, conformally equivalent to the Riemann sphere, on which $SO^{+}(3,1)$ acts as $PSL_2(\mathbb{C})$ by Möbius transformations. The Klein model is the open unit ball with chords as geodesics; the Poincaré ball and upper half-space models are obtained conformally.

The isometries are of three types: elliptic, fixing a point and rotating about it, and conjugate into the compact $SO(3)$; hyperbolic, translating along a unique geodesic and fixing its two boundary points; and parabolic, fixing a single boundary point and acting simply transitively on horospheres. The elliptic type is the one realised by the unitary group inside the split biquaternion algebra; the parabolic type is not realised by any element of the algebra, since the algebra is semisimple and has no non-zero nilpotent, and the nilpotents belong to the Lie algebra of the isometry group alone. The comparison with the split complex case collapses the three types to one and the comparison with the quaternion sphere collapses them to the elliptic type only.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}_{\mathbb{D}} = \mathbb{D}\otimes_{\mathbb{R}}\mathbb{H}$ | The split biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $j$ | Split complex unit, $j^2 = +e_0$, central |
| $g(\tilde P,\tilde Q) = \operatorname{Sc}(\tilde P\tilde Q^{\dagger})$ | Hermitian scalar form, signature $(4,4)$ |
| $\mathbb{M}_- = \{a\,je_0 + v\}$ | Anti-Hermitian subspace, signature $(3,1)$ |
| $g(\tilde X,\tilde X) = -a^2 + v_1^2 + v_2^2 + v_3^2$ | The Lorentzian form on $\mathbb{M}_-$ |
| $H^3 = \{\tilde X\in\mathbb{M}_- : g(\tilde X,\tilde X) = -1,\ a > 0\}$ | Hyperboloid model of hyperbolic three-space |
| $d_H(\tilde X,\tilde Y) = \operatorname{arcosh}(-g(\tilde X,\tilde Y))$ | Hyperbolic distance |
| $SO^{+}(3,1)$, $O^{\uparrow}(3,1)$ | Restricted Lorentz group and its sheet-preserving extension |
| $\partial H^3$ | Boundary at infinity, the projectivised null cone $\cong S^2$ |
| $PSL_2(\mathbb{C})$ | Isometry group of $H^3$ through its boundary action |
| $\operatorname{Hor}(\xi,s)$ | Horosphere centred at the boundary point $\xi$ |
| $H^1\cong\mathbb{R}$ | One-dimensional hyperbolic space, the split complex case |
| $e^{\theta j} = \cosh\theta + j\sinh\theta$ | Split complex unit, hyperbolic one-parameter group |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (Academic Press, 1978), for the hyperboloid model, the Iwasawa decomposition and the horospheres.
- John G. Ratcliffe, *Foundations of Hyperbolic Manifolds* (Springer, 2006), for the models of hyperbolic space and their conformal equivalences.
- Lars V. Ahlfors, *Möbius Transformations in Several Dimensions* (University of Minnesota, 1981), for the boundary action and the identification of the conformal group of the sphere.
- Alan F. Beardon, *The Geometry of Discrete Groups* (Springer, 1983), for the classification of isometries into elliptic, hyperbolic and parabolic types.
- Barrett O'Neill, *Semi-Riemannian Geometry with Applications to Relativity* (Academic Press, 1983), for the reverse Schwarz inequality for forms of signature $(3,1)$ and the geodesics of the hyperboloid.
- Bruno P. Zimmermann, *Computational Group Theory and Physics* (Cambridge University Press, 1994), for the exceptional isomorphism $SO^{+}(3,1)\cong PSL_2(\mathbb{C})$ from the Lie-algebra side.
