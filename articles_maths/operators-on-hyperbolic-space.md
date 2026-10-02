
# __Operators on Hyperbolic Space__

## Introduction

The operators of hyperbolic space are its isometries, and the group they form is the pseudo-orthogonal group of the form of signature $(n,1)$: the matrix group $O(n,1)$ in the hyperboloid model, the Möbius group in the ball and half-space models. Beside the two-sided operator group, the hyperbolic space carries a distinguished **one-sided** operator, the **geodesic flow**, the one-parameter group that translates the points along the geodesics; it is the flow of the geodesic spray on the unit tangent bundle, and the article reads it in the **signed one-sided** slot of the category: the parameter is one, the direction of the geodesic carries a sign, and the reversal of the direction is the involution by which the signed operator is twisted.

The article develops the isometry group in the three standard models and its identification with the pseudo-orthogonal group, the one-parameter subgroups and their fixed points, the classification of the isometries into the elliptic, parabolic and hyperbolic types with the loxodromic refinement in odd dimension, the geodesic flow on the unit tangent bundle with its generator and its invariant volume, and the signed structure of the direction reversal under which the flow is reversed. The dynamical and the ergodic properties of the flow are the subject of Part III, and the article names them and keeps to the operator and the geometry.

The article assumes *Hyperbolic Geometry* for the models, the geodesics, the boundary at infinity and the classification of the isometries; *Euclidean Geometry* and *Spherical Geometry* for the comparison geometries; *Transformation Groups and the Erlangen Program*, *Homogeneous Spaces* and *Symmetric Spaces*, later in this Part, for the reading of the space as the quotient $SO^+(n,1)/SO(n)$ and for the geodesic symmetries; and *Smooth Dynamical Systems* and *Ergodic Theory* of Part III for the flow. No physics is invoked.

## The Isometry Group of Hyperbolic Space

### The Three Models and the Group

**Definition.** The **hyperbolic space** $\mathbb{H}^n$ is the simply connected complete Riemannian manifold of constant sectional curvature $-1$; it is realised as the hyperboloid

$$
\mathbb{H}^n = \{x \in \mathbb{R}^{n,1} : B(x,x) = -1,\ x_0 > 0\}
$$

with the form $B$ of signature $(n,1)$ restricted to the tangent spaces, as the Poincaré ball with the metric $4\,|dx|^2/(1 - |x|^2)^2$, and as the upper half-space with the metric $|dx|^2/x_n^2$. The **operators** of the hyperbolic space are its isometries, and they form the group $\operatorname{Isom}(\mathbb{H}^n)$.

**Theorem.** The isometry group of the hyperboloid model is

$$
\operatorname{Isom}(\mathbb{H}^n) \cong O(n,1) ,
$$

the group of the linear maps preserving the form $B$, and the orientation-preserving subgroup is $SO^+(n,1)$, the connected component of the identity, which acts transitively on $\mathbb{H}^n$ and has the stabiliser of a point conjugate to $O(n)$; consequently

$$
\mathbb{H}^n \cong SO^+(n,1)/SO(n)
$$

as a homogeneous space, and the isotropy representation of $SO(n)$ on the tangent space at a point is the standard one.

**Proof.** A linear map preserving $B$ preserves the hyperboloid and the time orientation of the component, hence acts by an isometry; conversely an isometry of the hyperboloid extends uniquely to a linear automorphism of the ambient form by the rigidity of the metric and the geodesic completeness, which is the classical statement of *Hyperbolic Geometry*. The transitivity is the Witt extension theorem applied to the form: two points of the hyperboloid are two vectors of the same norm, and an element of $O(n,1)$ carries one to the other; the stabiliser of a timelike vector is the orthogonal group of its complement, of signature $(n,0)$, and the quotient statement follows.

**Corollary (the dimensions).** The isometry group has dimension $\frac{n(n+1)}{2}$, equal to the dimension of $SO(n+1)$ and to the dimension of the group $O(n,1)$; the stabiliser of a point has dimension $\frac{n(n-1)}{2}$, and the two numbers differ by $n$, the dimension of the hyperbolic space; the agreement of the dimensions of the isometry group of the hyperbolic space and of the sphere is the numerical shadow of the fact that the two spaces are the two real forms of the same complex geometry.

### The Boundary and the Conformal Models

**Theorem.** In the Poincaré ball model the isometry group is the group of the Möbius transformations preserving the ball, which is the same group $O(n,1)$ acting by the conformal action on the boundary sphere $S^{n-1} = \partial\mathbb{H}^n$; the orientation-preserving isometries act on the boundary by the Möbius transformations classified in *The Möbius Transformation as an Operator*, and the correspondence is an isomorphism of groups.

**Proof.** The ball model is conformally equivalent to the hyperboloid by the projection from the hyperboloid to the ball along the lines through the origin, and the conformal factors cancel in the isometry condition, so the isometry group is the conformal group of the ball; the conformal maps of the sphere are the Möbius transformations by Liouville, and the subgroup preserving the ball is the required group. The statement is in *Hyperbolic Geometry* and *Möbius and Lie Sphere Geometry*.

## The One-Parameter Subgroups

**Definition.** A **one-parameter subgroup** of the isometry group is a continuous homomorphism $t \mapsto g_t$ from the additive group $\mathbb{R}$ into $\operatorname{Isom}(\mathbb{H}^n)$; it is the exponential of an element $\xi$ of the Lie algebra $\mathfrak{so}(n,1)$, $g_t = \exp(t\xi)$, and it acts on $\mathbb{H}^n$ as a one-parameter group of isometries. The one-parameter subgroups are the **one-sided operators** of the hyperbolic space, the two-sided operators being the general isometries.

**Theorem.** A one-parameter subgroup of $SO^+(n,1)$ is, up to conjugacy, of exactly one of the three types:

- **elliptic**: conjugate to a rotation of $\mathbb{H}^n$ about a point, with the generator the rotation in an $\mathfrak{so}(2)$ inside the isotropy $\mathfrak{so}(n)$; the subgroup has a fixed point in the interior;
- **parabolic**: conjugate to the group of the translations of the horospheres, with the generator nilpotent and exactly one fixed point on the boundary;
- **hyperbolic**: conjugate to the group of the translations along a geodesic, with the generator semisimple and two fixed points on the boundary, and the subgroup acting on the geodesic by $t \mapsto$ the translation of length $t$.

**Proof.** The classification of the elements of $SO^+(n,1)$ by the location of the eigenvalues of the corresponding matrix in $O(n,1)$ gives the three types according to the eigenvalues on the unit circle, the real eigenvalue of modulus different from one with a Jordan block, and the two real eigenvalues; the fixed points are the eigenvectors in the ambient space, projected to the interior or to the boundary according to the sign of the norm. The statement is in *Hyperbolic Geometry* and *Symmetric Spaces*.

**Proposition.** The orbit of a point under a hyperbolic one-parameter subgroup is the geodesic through the point in the direction of the axis, the orbit under a parabolic subgroup is a horosphere, and the orbit under an elliptic subgroup is a sphere about the fixed point; the three orbit types are the three kinds of the orbits of the one-sided operators.

**Proof.** The geodesic through a point in a direction is the orbit of the point under the translation along it, which is the hyperbolic subgroup by definition; the horospheres are the orbits of the parabolic group by the definition of the horospherical coordinates, and the spheres about a point are the orbits of the rotations. The statement is the elementary geometry of the model, in *Hyperbolic Geometry*.

## The Classification of the Isometries

**Definition.** An isometry $g \in \operatorname{Isom}(\mathbb{H}^n)$ is **elliptic** when it has a fixed point in $\mathbb{H}^n$, **parabolic** when it has no fixed point in $\mathbb{H}^n$ and exactly one fixed point on the boundary, and **hyperbolic** when it has no fixed point in $\mathbb{H}^n$ and exactly two fixed points on the boundary; the **translation length** of a hyperbolic isometry is the infimum of the distances $d(x,gx)$, attained along the axis, the geodesic joining the two boundary fixed points.

**Theorem.** Every isometry of $\mathbb{H}^n$ is elliptic, parabolic or hyperbolic; the elliptic isometries are the conjugates of the rotations and form the isotropy subgroups, the parabolic ones are the conjugates of the horospherical translations, and the hyperbolic ones are the conjugates of the translations along a geodesic, with the axis as the invariant geodesic and the translation length as the invariant. In dimension $n = 3$ the two-dimensional rotation about the axis may be added to the translation, giving the **loxodromic** isometries, which have two boundary fixed points and a screw motion along the axis.

**Proof.** The classification is by the fixed points on the boundary and in the interior, and it is the classification of the elements of $O(n,1)$ by their eigenvectors and by the corresponding one-parameter subgroups; the translation length is the logarithm of the eigenvalue ratio of the hyperbolic part. The statement is in *Hyperbolic Geometry*, and it is the same classification as the one of the Möbius operators by the trace, read in the conformal model.

**Remark.** The classification is the hyperbolic instance of the classification of the elements of a semisimple Lie group by the growth of the powers, and the three types correspond to the compact, the unipotent and the semisimple elements of *Lie Groups*; the article records only the geometric classification, and the group-theoretic one is in *Lie Groups* and *Symmetric Spaces*.

## The Geodesic Flow

### The Unit Tangent Bundle and the Flow

**Definition.** The **unit tangent bundle** of the hyperbolic space is

$$
S\mathbb{H}^n = \{(x, v) : x \in \mathbb{H}^n,\ v \in T_x\mathbb{H}^n,\ g_x(v,v) = 1\} ,
$$

a manifold of dimension $2n - 1$. The **geodesic flow** is the one-parameter group of diffeomorphisms

$$
\phi_t : S\mathbb{H}^n \longrightarrow S\mathbb{H}^n, \qquad \phi_t(x,v) = (\gamma_{x,v}(t), \dot\gamma_{x,v}(t)) ,
$$

where $\gamma_{x,v}$ is the geodesic with the initial point $x$ and the initial velocity $v$; the flow translates the base point along the geodesic and carries the velocity by the parallel transport.

**Proposition.** The geodesic flow is a one-parameter group of diffeomorphisms of $S\mathbb{H}^n$, $\phi_{t+s} = \phi_t\circ\phi_s$, and it is the flow of the **geodesic spray**, the vector field on $S\mathbb{H}^n$ whose value at $(x,v)$ is the tangent vector of the curve $t \mapsto \phi_t(x,v)$ at $t = 0$; the flow preserves the volume of the Liouville measure on the unit tangent bundle, and it commutes with the isometries acting on the bundle by the differentials.

**Proof.** The geodesic equation is a second-order ordinary differential equation on the base with the solution depending smoothly on the initial data, so the flow is a one-parameter group of diffeomorphisms; the computation of the Lie derivative of the Liouville volume in the geodesic spray shows that it vanishes by the skew-symmetry of the Riemannian connection, and the isometries carry the geodesics to the geodesics and commute with the flow by definition. The statement is the standard one, in *Hyperbolic Geometry* and *Riemannian Geometry*.

### The Generator and the Signed Structure

**Definition.** The **direction reversal** is the involution of the unit tangent bundle

$$
\sigma : S\mathbb{H}^n \longrightarrow S\mathbb{H}^n, \qquad \sigma(x,v) = (x,-v) ;
$$

the **signed geodesic flow** is the flow together with the reversal, and the pair satisfies

$$
\sigma \circ \phi_t = \phi_{-t} \circ \sigma ,
$$

so the reversal conjugates the flow to its inverse. The article calls the flow the **signed one-sided operator** of the hyperbolic space, the one-sided datum being the parameter $t$ and the sign being the reversal $\sigma$.

**Proposition.** The signed geodesic flow is a one-parameter group of diffeomorphisms of $S\mathbb{H}^n$ generated by the geodesic spray, and the reversal $\sigma$ is the involutive automorphism of the flow that reverses the time; the fixed point set of $\sigma$ is empty on the level sets of the flow (a geodesic is not fixed by the reversal), while the base point is fixed and the velocity is negated, so the reversal is an involution without fixed points on each flow line.

**Proof.** The relation $\sigma\phi_t = \phi_{-t}\sigma$ is the equality of the geodesic with the reversed velocity traversed backwards, which is the same geodesic traversed forwards, $\gamma_{x,-v}(t) = \gamma_{x,v}(-t)$; the fixed points of $\sigma$ are the pairs with $v = -v$, that is, $v = 0$, which are not in the unit tangent bundle, so the reversal has no fixed point. The statement is elementary and is recorded in *Hyperbolic Geometry*.

**Remark (the geodesic symmetries and the flow).** The geodesic symmetry at a point $p$ reverses every geodesic through $p$, so it satisfies $s_p\circ\phi_t = \phi_{-t}\circ s_p$ on the geodesics through $p$, and it is the pointwise form of the reversal on the flow lines through $p$; the signed flow and the geodesic symmetries are the one-sided and the two-sided forms of the same reversal. This is the reason the geodesic flow is the distinguished one-sided operator of the hyperbolic space.

## The Quotients and the Forward Reference

**Definition.** A **discrete group of isometries** is a subgroup $\Gamma \subseteq \operatorname{Isom}(\mathbb{H}^n)$ whose action is properly discontinuous; the quotient $\Gamma\backslash\mathbb{H}^n$ is a complete hyperbolic manifold, and the flow descends to the unit tangent bundle of the quotient, $S(\Gamma\backslash\mathbb{H}^n) = \Gamma\backslash S\mathbb{H}^n$.

**Theorem.** The geodesic flow on the quotient of the hyperbolic space by a discrete group of isometries is the flow that Part III studies: its periodic orbits are the closed geodesics of the quotient, its recurrence and its ergodic properties with respect to the Liouville measure are the subject of *Smooth Dynamical Systems* and *Ergodic Theory*, and the present article keeps the flow as the one-sided operator of the geometry.

**Proof.** The closed geodesics of the quotient are the projections of the geodesics of the hyperbolic space whose endpoints are joined by an element of the discrete group, so they are the periodic orbits of the flow; the descent of the flow and of the measure to the quotient is the standard reduction, and the ergodic theory is the analysis of the flow, in Part III.

**Remark.** The quotient construction and the flow are the point at which the hyperbolic geometry of this Part meets the dynamical systems of Part III; the article states the descent and names the ergodic theory, and it does not use the analytic structure of the flow beyond its definition as a one-sided operator.

## Summary

The operators of hyperbolic space are its isometries, and the group is $\operatorname{Isom}(\mathbb{H}^n) = O(n,1)$ in the hyperboloid model, with the orientation-preserving subgroup $SO^+(n,1)$ acting transitively and the space realising the homogeneous space $SO^+(n,1)/SO(n)$ of dimension $\frac{n(n+1)}{2}$; in the ball and half-space models the group is the Möbius group of the boundary. The one-parameter subgroups are the one-sided operators, and they are elliptic (a fixed interior point), parabolic (one boundary fixed point, the horospherical translations) or hyperbolic (two boundary fixed points, the translations along the axis). Every isometry is elliptic, parabolic or hyperbolic by the fixed points, with the loxodromic refinement in dimension three; the translation length is the invariant of the hyperbolic type. The geodesic flow $\phi_t$ on the unit tangent bundle is the distinguished one-sided operator, its generator is the geodesic spray, and it preserves the Liouville volume; the direction reversal $\sigma(x,v) = (x,-v)$ is the sign, and it satisfies $\sigma\phi_t = \phi_{-t}\sigma$. The flow descends to the quotients by the discrete groups, and its periodic orbits are the closed geodesics; the ergodic theory of the flow is Part III.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}^n$ | Hyperbolic space of dimension $n$ |
| $B$ | Form of signature $(n,1)$ on $\mathbb{R}^{n,1}$ |
| $\operatorname{Isom}(\mathbb{H}^n) \cong O(n,1)$ | Isometry group (operator group) |
| $SO^+(n,1)$ | Orientation-preserving isometry group |
| $SO^+(n,1)/SO(n)$ | Homogeneous model of $\mathbb{H}^n$ |
| elliptic, parabolic, hyperbolic | Isometry types by the fixed points |
| loxodromic | Screw type in dimension three |
| translation length | Infimum of $d(x,gx)$, attained on the axis |
| $S\mathbb{H}^n$ | Unit tangent bundle, dimension $2n-1$ |
| $\phi_t$ | Geodesic flow |
| geodesic spray | Generator of the geodesic flow |
| $\sigma(x,v) = (x,-v)$ | Direction reversal, the sign of the operator |
| $\Gamma\backslash\mathbb{H}^n$ | Quotient by a discrete group of isometries |

## Further Reading

- John G. Ratcliffe, *Foundations of Hyperbolic Manifolds*, 2nd ed. (Springer, 2006), for the models, the isometry groups and the geodesic flow.
- Sigurdur Helgason, *Differential Geometry, Lie Groups and Symmetric Spaces* (Academic Press, 1978), for the homogeneous models and the isometry groups.
- Dmitri V. Alekseevskii, "Hyperbolic space", in *Encyclopaedia of Mathematics* (Kluwer, 1990), for the classification of the isometries.
- Werner Ballmann, Mikhael Gromov and Viktor Schroeder, *Manifolds of Nonpositive Curvature* (Birkhäuser, 1985), for the geodesic flow and the rank.
- Anthony W. Knapp, *Representation Theory of Semisimple Groups* (Princeton University Press, 1986), for the one-parameter subgroups and the classification of the elements.
- Peter J. Nicholls, *The Ergodic Theory of Discrete Groups* (Cambridge University Press, 1989), for the geodesic flow of the quotients (Part III).
