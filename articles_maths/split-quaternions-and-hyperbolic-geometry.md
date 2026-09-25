
# __Split-Quaternions and Hyperbolic Geometry__

## Introduction

This article builds the model of the hyperbolic plane on the split-quaternion algebra. It presents the hyperboloid model on the timelike sheet of the vector subspace, records the unit condition and the two-sheeted structure, identifies the upper half-plane and the disc as matrix models in which the group acts by fractional linear transformations, classifies the isometries, and relates the model to the rotations and the Lorentz group of the system and to the hyperbolic geometry of Part II.

The split-quaternion algebra, its vector subspace $V$, its norm form and its matrix model are assumed from *Split-Quaternion Algebra*; the roots of $\xi^2 = -1$ and the conjugacy-class description of the root set from *Split-Quaternion Roots of Minus One*; the adjoint action, the double cover and the elliptic, hyperbolic and parabolic one-parameter subgroups from *Split-Quaternion Rotations and the Lorentz Group*; and the induced metrics on the hyperboloids from *Split-Quaternion Geometry*, which supplies the geometry of the two forms. The hyperbolic plane itself, its models, its geodesics and its isometry classification are those of *Hyperbolic Geometry* and *Hyperbolic Rotations*; this article does not rebuild them, it realises them. Nothing physical is invoked.

## The Hyperboloid Model

**Definition.** The **timelike sheet** is the connected component of the level set $\{v \in V : N(v) = 1\}$ containing $e_1$:

$$
\mathbb{H}^{+} = \{v = b e_1 + c e_2 + d e_3 : b^2 - c^2 - d^2 = 1, \ b > 0\}.
$$

By *Split-Quaternion Rotations and the Lorentz Group*, §*The Trichotomy of Timelike, Lightlike and Spacelike Elements*, the group $\mathrm{SO}^{+}(2,1)$ acts transitively on $\mathbb{H}^{+}$ with stabiliser a copy of $SO(2)$, so that

$$
\mathbb{H}^{+} \cong \mathrm{SO}^{+}(2,1)/SO(2) \cong \mathrm{PSL}_2(\mathbb{R})/SO(2).
$$

**Theorem (The Hyperboloid Model).** The form $-B$ restricted to the tangent spaces of $\mathbb{H}^{+}$ is a Riemannian metric of constant curvature $-1$, and with this metric $\mathbb{H}^{+}$ is a model of the hyperbolic plane. The distance is

$$
\cosh d(v,w) = B(v,w) \qquad (v, w \in \mathbb{H}^{+}),
$$

and the isometry group is $\mathrm{PSL}_2(\mathbb{R})$, acting by the adjoint action. The geodesics are the intersections of $\mathbb{H}^{+}$ with the planes through the origin of $V$.

**Proof.** The induced metric and its curvature are (*Split-Quaternion Geometry*, §*The Unit Hyperboloids and Their Metrics*), where it is also shown that the induced form is definite on the sheet and that the geodesics are the central sections. The distance formula is the standard one for a hyperboloid model: for $v = w$ both sides are $1 = \cosh 0$, and for distinct points in the same sheet $B(v,w) \geq 1$ because the sheet lies in the closed half-space $b \geq 1$ and $B(e_1,w) = w_1 \geq 1$, with the general case following by transitivity. The group action is the double cover of *Split-Quaternion Rotations and the Lorentz Group*, §*The Double Cover of $\mathrm{SO}^{+}(2,1)$*, and the identification of the quotient with the hyperbolic plane is *Hyperbolic Geometry*. $\square$

The model is the hyperboloid model of the hyperbolic plane, and the vector space in which it sits is the vector subspace of the algebra, of signature $(2,1)$; the points of the model are precisely the solutions of $\xi^2 = -1$ in the sheet, by *Split-Quaternion Roots of Minus One*, §*The Equation and the Reduction to the Vector Subspace*.

## The Unit Condition and the Two-Sheeted Structure

**Theorem (The Two Sheets).** The level set $\{N = 1\}$ in $V$ has exactly two connected components, the timelike sheet $\mathbb{H}^{+}$ and its mirror $\mathbb{H}^{-} = \{b < 0\}$. The two sheets are exchanged by $v \mapsto -v$, by the conjugation $\bar{\cdot}$, and by the adjoint action of any unit of norm $-1$, such as $e_2$. The identity component $\mathrm{SO}^{+}(2,1)$ preserves each sheet; the full isometry group $O(2,1)$ exchanges them.

**Proof.** The two sheets are the intersections with the half-spaces $b>0$ and $b<0$, each diffeomorphic to a plane by *Split-Quaternion Roots of Minus One*, §*The Equation and the Reduction to the Vector Subspace*. Both $v \mapsto -v$ and the conjugation reverse the sign of $b$; the conjugation reverses it because the fixed-point decomposition $v = \operatorname{Sc}(v) + \operatorname{Vec}(v)$ with $\bar{v} = -v$ for $v \in V$ by (*Split-Quaternion Algebra*, §*The Two Eigenspaces*). The adjoint action of $e_2$ sends $e_1$ to $-e_1$ by the computation of *Split-Quaternion Rotations and the Lorentz Group*, §*The Adjoint Representation*, and has norm $-1$; the connected group $\mathrm{SO}^{+}(2,1)$ cannot exchange the two sheets because it cannot leave the connected component of the identity in the full isometry group, whose other components exchange the sheets. $\square$

**Corollary (The Unit Condition Selects an Orientation).** A hyperbolic-plane point on the split-quaternions is a split-quaternion $\xi$ with $\xi \in V$ and $N(\xi) = 1$ together with the choice of a sheet; the choice of sheet is the choice of orientation of the plane, and the group $\mathrm{PSL}_2(\mathbb{R})$ acts on each sheet.

**Proof.** Immediate from the two-sheeted structure and the transitivity of $\mathrm{PSL}_2(\mathbb{R})$ on each sheet. $\square$

The unit condition is therefore not simply $N = 1$ but "$N = 1$ and one sheet", and the two sheets are the two orientations. In the projective picture the two sheets have the same image, because $v$ and $-v$ define the same point of $\mathbb{P}(V)$.

## The Upper Half-Plane as a Matrix Model

The matrix model identifies the sheet with the upper half-plane by an explicit formula.

**Definition.** For $\xi = b e_1 + c e_2 + d e_3$ in the timelike sheet define

$$
\zeta(\xi) = \frac{c - b}{d + i} = \frac{(c-b)(d-i)}{1 + d^2} \in \mathbb{C},
$$

the ratio of the components of an eigenvector of $\Phi(\xi)$ for the eigenvalue $i$.

**Theorem (The Eigenline Model).** The map $\zeta$ is a bijection from the timelike sheet onto the upper half-plane

$$
\mathbb{H} = \{z \in \mathbb{C} : \operatorname{Im} z > 0\},
$$

with

$$
\operatorname{Im}\zeta(\xi) = \frac{b - c}{1 + d^2} > 0,
$$

and it is equivariant: for $g \in \mathrm{SL}_2(\mathbb{R})$ with $\Phi(g) = \begin{pmatrix}\alpha & \beta \\ \gamma & \delta\end{pmatrix}$,

$$
\zeta(g \xi g^{-1}) = \frac{\alpha\,\zeta(\xi) + \beta}{\gamma\,\zeta(\xi) + \delta}.
$$

The metric on the sheet is carried to the hyperbolic metric of the half-plane, $\mathrm{d}s^2 = |\mathrm{d}\zeta|^2/(\operatorname{Im}\zeta)^2$, and the two-sheeted structure corresponds to the pair consisting of the upper and the lower half-planes.

**Proof.** *Positivity.* On the sheet, $b = \sqrt{1 + c^2 + d^2}$, so $b - c > 0$ and the displayed formula gives $\operatorname{Im}\zeta > 0$. *Bijectivity.* Given $z = x + iy \in \mathbb{H}$, put

$$
M(z) = \begin{pmatrix} x/y & -(x^2+y^2)/y \\ 1/y & -x/y \end{pmatrix},
$$

which is traceless with determinant $1$; the element $\xi = \Phi^{-1}(M(z))$ then lies in $V$, has $N(\xi) = \det M(z) = 1$ and $b > 0$, so it lies in the sheet, and its matrix has $(z,1)$ as an eigenvector for $i$, so $\zeta(\xi) = z$. The two constructions are inverse, so $\zeta$ is a bijection. *Equivariance.* The eigenvector of $\Phi(g\xi g^{-1}) = \Phi(g)\Phi(\xi)\Phi(g)^{-1}$ for the eigenvalue $i$ is $\Phi(g)$ applied to the eigenvector of $\Phi(\xi)$, and the action of $\Phi(g)$ on the ratios of components of eigenvectors is exactly the fractional linear transformation displayed. *The metric.* The metric $-B$ on the sheet is invariant under the adjoint action, and the half-plane metric is invariant under the fractional linear action; the two metrics are proportional and agree at the point $\zeta = i$, so they agree. $\square$

The formula for $\zeta$ is the explicit form of the general statement of *Split-Quaternion Roots of Minus One*, §*The Root Set as a Homogeneous Space*: the root set is the homogeneous space $\mathbb{H}_{\mathrm{s}}^{\times}/\mathbb{C}^{\times}$, whose two components are the two copies of the hyperbolic plane, here presented as the upper and lower half-planes.

**Corollary (The Sheet as the Quotient).** The sheet is the quotient $\mathrm{SL}_2(\mathbb{R})/SO(2)$ with the coset description $\zeta(g \cdot i)$, and the isotropy group of the point $i$ is the group of elliptic elements fixing $i$, namely the image of $SO(2)$.

**Proof.** The action on $\mathbb{H}$ is transitive because $\mathrm{SL}_2(\mathbb{R})$ contains the translations and the dilations, and the stabiliser of $i$ is the group of matrices with $(\alpha i + \beta)/(\gamma i + \delta) = i$, which is the rotation group $SO(2)$. $\square$

## The Disc as a Matrix Model

**Definition.** The **Cayley transform** is

$$
w(\zeta) = \frac{\zeta - i}{\zeta + i},
$$

a biholomorphic map from the upper half-plane onto the unit disc

$$
\mathbb{D} = \{w \in \mathbb{C} : |w| < 1\}.
$$

**Theorem (The Disc Model).** The Cayley transform carries the hyperbolic metric of the half-plane to the metric

$$
\mathrm{d}s^2 = \frac{4\,|\mathrm{d}w|^2}{(1 - |w|^2)^2}
$$

on the disc, and the isometry group of the disc with this metric is the conjugate of $\mathrm{PSL}_2(\mathbb{R})$ in $\mathrm{PSL}_2(\mathbb{C})$, acting by fractional linear transformations preserving the disc. Under this identification the sheet of the hyperboloid model is carried to the disc, the boundary circle of the disc is the set of ideal points, and the group acts on the disc by matrices.

**Proof.** The Cayley transform is a biholomorphism of the two domains, and the pullback of the displayed metric is the half-plane metric; the isometry group of a Riemannian metric is transported by an isometry, so it is the conjugate of $\mathrm{PSL}_2(\mathbb{R})$; the boundary correspondence and the fractional linear form are the standard Cayley transform of the Möbius action. $\square$

**Corollary (The Three Matrix Models).** The hyperbolic plane on the split-quaternions therefore has three presentations, all carried by the same group of matrices: the hyperboloid sheet $\mathbb{H}^{+} \subset V$ with the metric $-B$ and the adjoint action; the upper half-plane with the fractional linear action of $\mathrm{SL}_2(\mathbb{R})$; and the disc with the Cayley-transformed action. The three are isometric by explicit formulas, and the passage between them is by the eigenline map and the Cayley transform.

**Proof.** Composition of the isometries supplied by the two theorems. $\square$

## The Classification of Isometries

**Theorem (The Three Types).** Let $g \in \mathrm{SL}_2(\mathbb{R})$ have trace $\tau = \alpha + \delta$. Then the isometry of the hyperbolic plane induced by $g$ is

1. **elliptic**, if $|\tau| < 2$; it has a fixed point in the interior, and in the sheet description it is conjugate to an element of the compact subgroup $SO(2)$;
2. **hyperbolic**, if $|\tau| > 2$; it has two fixed points on the boundary and no interior fixed point, and it translates along the geodesic joining them;
3. **parabolic**, if $|\tau| = 2$ and $g \neq \pm 1$; it has exactly one fixed point on the boundary and no interior fixed point.

The three types correspond to the three classes of the adjoint action of the unit group on the vector subspace: the elliptic isometries fix a vector of positive norm, the hyperbolic isometries fix a vector of negative norm and the two lightlike directions of its orthogonal plane, and the parabolic isometries fix a lightlike direction.

**Proof.** The classification of elements of $\mathrm{SL}_2(\mathbb{R})$ by trace is the standard one, treated in *Hyperbolic Geometry* and in *Hyperbolic Rotations*; the translation to the vector subspace is the fixed-direction computation of *Split-Quaternion Rotations and the Lorentz Group*, §*Elliptic and Hyperbolic One-Parameter Subgroups* and §*The Trichotomy of Timelike, Lightlike and Spacelike Elements*. $\square$

**Corollary (The Isometry Types and the Roots of $\pm 1$).** The elliptic one-parameter subgroups are generated by the solutions of $\xi^2 = -1$, which are the points of the sheet; the hyperbolic subgroups are generated by the solutions of $\eta^2 = +1$ lying in $V$, which are spacelike vectors of norm $-1$ and not points of the sheet; the parabolic subgroups are generated by the nilpotents.

**Proof.** The three statements are the classification of the one-parameter subgroups, all three types being treated in the corollary of *Split-Quaternion Rotations and the Lorentz Group*, §*Elliptic and Hyperbolic One-Parameter Subgroups*, together with the identification of the sheet with the solutions of $\xi^2 = -1$. $\square$

## The Relation to the Rotations and the Lorentz Group

**Theorem (Equivariance of the Model).** The identification of the sheet with the hyperbolic plane intertwines the adjoint action of $\mathrm{SL}_2(\mathbb{R})$ on the sheet with the fractional linear action of $\mathrm{SL}_2(\mathbb{R})$ on the half-plane, and the double cover $\mathrm{SL}_2(\mathbb{R}) \to \mathrm{SO}^{+}(2,1)$ is the statement that the same group of matrices acts by adjoint transformations on the hyperboloid and by Möbius transformations on the half-plane. The centre $\{\pm 1\}$ acts trivially in both descriptions.

**Proof.** The equivariance is the theorem on the eigenline model; the double cover is *Split-Quaternion Rotations and the Lorentz Group*, §*The Double Cover of $\mathrm{SO}^{+}(2,1)$*; the triviality of the centre is the statement that $\mathrm{PSL}_2(\mathbb{R})$ is the effective group of the action. $\square$

The model is therefore a realisation of the homogeneous space of *Split-Quaternion Rotations and the Lorentz Group*, §*The Adjoint Action on the Vector Subspace*, and the group action of the two articles is the same action in two presentations. The orbit of a point of the sheet is the sheet, and the stabiliser is the compact subgroup, so the geometry of the model is exactly the quotient $\mathrm{PSL}_2(\mathbb{R})/SO(2)$.

## The Relation to the Hyperbolic Geometry of Part II

**Theorem (Dictionary with Part II).** Under the identification of the sheet with the hyperbolic plane, the following objects correspond: the geodesics of the model are the intersections of the sheet with the central planes of $V$, and under $\zeta$ they are the vertical lines and the semicircles orthogonal to the real axis of the half-plane; the ideal points are the isotropic lines of the form, that is the points of the null cone, and under $\zeta$ they are the real axis together with the point at infinity; the angle between two geodesics is the angle measured by the metric $-B$ on the sheet and by the hyperbolic metric in the half-plane; the area element is the invariant measure $\mathrm{d}x\,\mathrm{d}y/y^2$; and the isometry group is $\mathrm{PSL}_2(\mathbb{R})$.

**Proof.** The geodesics of a hyperboloid model are the central sections by *Split-Quaternion Geometry*, §*The Lorentzian Geometry of the Vector Subspace*, and their images under the biholomorphism $\zeta$ are the standard geodesics of the half-plane; the identification of the boundary with the null cone is the statement that the boundary of the hyperbolic plane in this model is the set of isotropic directions, which is the light cone; the remaining identifications are those of *Hyperbolic Geometry*. $\square$

**Corollary (The Boundary Is the Projective Null Quadric of the Subspace).** The ideal boundary of the hyperbolic plane in this model is the projective null cone of the restricted form, a circle; the full projective null quadric $Q$ of the algebra, a torus, is a different object, the boundary being the projection of the cone of $V$ only.

**Proof.** The boundary is the projective image of the lightlike directions of $V$, a circle by *Split-Quaternion Norm and Invertibility*, §*Isotropy*; the quadric $Q$ of the algebra is the torus of *Split-Quaternion Geometry*, §*The Null Quadric and the Ruling*, and it contains the boundary circle as a subvariety. $\square$

## The Invariant Distance and the Area Form

**Theorem (Distance and Area in the Three Models).** In the half-plane model the distance and the area element are

$$
\cosh d(z,w) = 1 + \frac{|z-w|^2}{2\,\operatorname{Im}z\,\operatorname{Im}w}, \qquad \mathrm{d}A = \frac{\mathrm{d}x\,\mathrm{d}y}{y^2},
$$

in the disc model they are obtained from these by the Cayley transform, and in the hyperboloid model they are the distance $\cosh d(v,w) = B(v,w)$ and the area element induced by $-B$ on the sheet. The three expressions agree under the identifications of the previous sections, and the function $\cosh d$ is the one whose value at the identity determines the metric.

**Proof.** The half-plane formulas are the standard ones of *Hyperbolic Geometry*; the agreement is by the invariance under the group action, which acts transitively and preserves all three expressions. $\square$

**Corollary (The Geodesics Are the Invariant Curves).** The geodesics are the images of the vertical lines and the semicircles orthogonal to the boundary in the half-plane; in the disc they are the diameters and the arcs orthogonal to the boundary circle; and in the hyperboloid model the central sections. The boundary is at infinity: no geodesic reaches it in finite time, and the metric is complete.

**Proof.** The geodesics of the hyperboloid model are the central sections, the Cayley transform and the eigenline map are isometries, and completeness is the standard property of the hyperboloid model. $\square$

## Summary

The hyperbolic plane is realised on the split-quaternion algebra by the timelike sheet $\mathbb{H}^{+}$ of the hyperboloid $N = 1$ in the vector subspace, with the metric $-B$ of constant curvature $-1$, the distance given by $\cosh d(v,w) = B(v,w)$, and the isometry group $\mathrm{PSL}_2(\mathbb{R}) \cong \mathrm{SO}^{+}(2,1)$ acting by the adjoint action. The sheet is the homogeneous space $\mathrm{PSL}_2(\mathbb{R})/SO(2)$, the points of the model are the solutions of $\xi^2 = -1$ lying in the sheet, and the geodesics are the central sections.

The unit condition is $N = 1$ together with a choice of sheet; the level set has two sheets, exchanged by $v \mapsto -v$, by the conjugation and by any unit of norm $-1$, and preserved by the identity component of the isometry group. The two sheets are the two half-planes of the matrix model.

The matrix models are explicit. The eigenline map $\zeta(\xi) = (c-b)/(d+i)$ is a bijection from the sheet onto the upper half-plane with inverse given by the traceless determinant-one matrix $M(z)$, and it intertwines the adjoint action with the fractional linear action of $\mathrm{SL}_2(\mathbb{R})$; the metric becomes $|\mathrm{d}\zeta|^2/(\operatorname{Im}\zeta)^2$. The Cayley transform carries the half-plane to the disc with the metric $4|\mathrm{d}w|^2/(1-|w|^2)^2$ and the conjugated matrix action. The isometries are classified by the trace into elliptic, hyperbolic and parabolic types, matching the three classes of one-parameter subgroups generated by the roots of $-1$, the roots of $+1$ and the nilpotents. The ideal boundary is the projective null cone of the vector subspace, a circle, and the full null quadric of the algebra, a torus, is the larger projective object.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\mathbb{H}^{+}$ | the timelike sheet of $\{N=1\}$ in $V$ | this article |
| $-B$ on $\mathbb{H}^{+}$ | the hyperbolic metric of curvature $-1$ | *Split-Quaternion Geometry* |
| $\cosh d(v,w) = B(v,w)$ | the hyperbolic distance on the sheet | this article |
| $\mathrm{PSL}_2(\mathbb{R}) \cong \mathrm{SO}^{+}(2,1)$ | the isometry group | *Split-Quaternion Rotations and the Lorentz Group* |
| $\zeta(\xi) = (c-b)/(d+i)$ | the eigenline map to the upper half-plane | this article |
| $\mathbb{H}$ | the upper half-plane | *Hyperbolic Geometry* |
| $M(z)$ | the traceless determinant-one matrix of a point of the half-plane | this article |
| $w = (\zeta-i)/(\zeta+i)$ | the Cayley transform to the disc | this article |
| $\mathbb{D}$ | the unit disc, with metric $4|\mathrm{d}w|^2/(1-|w|^2)^2$ | this article |
| elliptic, hyperbolic, parabolic | the three types of isometry, by the trace | *Hyperbolic Geometry* |
| ideal boundary | the projective null cone of $V$, a circle | this article |
| $Q$ | the null quadric of the algebra, a torus | *Split-Quaternion Geometry* |

## Further Reading

- John G. Ratcliffe, *Foundations of Hyperbolic Manifolds* (Springer, 2006), for the hyperboloid, half-plane, disc and Klein models and the classification of the isometries.
- Alan F. Beardon, *The Geometry of Discrete Groups* (Springer, 1983), for the action of $\mathrm{SL}_2(\mathbb{R})$ by Möbius transformations and the trace classification.
- Joseph Lehner, *A Short Course in Automorphic Functions* (Holt, Rinehart and Winston, 1966), for the Cayley transform, the disc model and the boundary of the hyperbolic plane.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the hyperboloid model of the hyperbolic plane inside a Clifford algebra of signature $(2,1)$.
