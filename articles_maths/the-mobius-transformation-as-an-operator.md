
# __The Möbius Transformation as an Operator__

## Introduction

A **Möbius transformation** is a fractional linear map of the Riemann sphere, and it is the operator of the conformal and the hyperbolic geometries of this Part in their two-dimensional and three-dimensional instances. As a projectivity of the complex projective line it is an operator of the kind treated in *Operators on a Projective Space*, and the present article turns that reading to the complex line and follows the operator into the hyperbolic space that the line bounds. The transformation is an operator of the conformal sphere, it preserves the cross ratio of four points, and it extends to an isometry of hyperbolic space, where its action is the one that makes the hyperbolic isometry group a group of fractional linear operators.

The article develops the sphere and the fractional linear operator, the matrix group and its two-to-one covering of the operator group, the cross ratio and its role as the complete invariant, the classification of the operators by the trace of a matrix into the elliptic, parabolic, hyperbolic and loxodromic classes, and the action on hyperbolic space by the Poincaré extension, with the real and the complex cases distinguished. It fixes the operator conventions of the conformal and Möbius articles of this Part and identifies the subgroups of the operator group that preserve a point, a pair of points, or a hyperbolic subspace.

The article assumes *Projective Geometry* for the projective line and the cross ratio, *Conformal Geometry* and *Möbius and Lie Sphere Geometry* for the Möbius group and the conformal sphere, and *Hyperbolic Geometry* for the upper half-space model, the boundary at infinity, the Poincaré extension and the classification of the isometries. The measure theory of the boundary and the ergodic theory of the geodesic flow are Part III, and they are named only as forward references. No distance is introduced beyond those the cited articles fix, and no physics is invoked.

## The Sphere and the Fractional Linear Operator

### The Riemann Sphere

**Definition.** The **Riemann sphere** is the one-point compactification

$$
\hat{\mathbb{C}} = \mathbb{C} \cup \{\infty\} = \mathbb{P}^1(\mathbb{C}) ,
$$

the complex projective line, whose points are written in the affine coordinate $z = x_0/x_1$ on the chart $x_1 \neq 0$ together with the point $\infty = [1:0]$. Its conformal structure is the one of *Conformal Geometry* in dimension two, and its identification with the unit sphere $S^2$ is the stereographic projection, a conformal bijection.

**Definition.** A **Möbius transformation** is a map of the sphere

$$
z \longmapsto \frac{az + b}{cz + d}, \qquad a, b, c, d \in \mathbb{C}, \quad ad - bc \neq 0 ,
$$

with the conventions that the pole $-d/c$ is sent to $\infty$ and $\infty$ is sent to $a/c$ when $c \neq 0$, and that $\infty$ is sent to $\infty$ and $z$ to $(az+b)/d$ when $c = 0$; it is the operator of the sphere that the article studies.

**Proposition.** The Möbius transformations are exactly the projectivities of $\mathbb{P}^1(\mathbb{C})$, they form a group under composition, and the assignment of the quadruple $(a,b,c,d)$ to the transformation is a group homomorphism from the invertible matrices to the operator group with kernel the nonzero scalar matrices.

**Proof.** A projectivity of the projective line is induced by an invertible two-by-two matrix, and on the affine chart its formula is the fractional linear expression; conversely a fractional linear map with $ad-bc\neq0$ is induced by the matrix, so the two families agree. The composition of two fractional linear maps is computed from the matrix product, and the map is the identity exactly when the matrix is a scalar, which gives the kernel. The classical statement is in *Projective Geometry*.

### The Matrix and the Two-to-One Covering

**Theorem.** The operator group of the sphere is the projective general linear group

$$
\operatorname{Möb} = PSL(2,\mathbb{C}) = PGL(2,\mathbb{C}) = SL(2,\mathbb{C})/\{\pm I\} ,
$$

the quotient of the determinant-one matrices by the central element $-I$; the projection $SL(2,\mathbb{C}) \to PSL(2,\mathbb{C})$ is two-to-one, and the operator group acts on the sphere by the fractional linear formula, so the centre of $SL(2,\mathbb{C})$ is exactly the kernel of the action.

**Proof.** Every invertible matrix is a scalar multiple of a determinant-one matrix, and the scalar matrices act trivially on the sphere, so $PGL(2,\mathbb{C}) = PSL(2,\mathbb{C})$; the kernel of the action of $SL(2,\mathbb{C})$ consists of the scalar matrices of determinant one, which are $\pm I$. The covering is the two-to-one projection of the complex special linear group onto its adjoint form.

**Remark.** The two-to-one covering is the lowest-dimensional instance of the spin covering of the orthogonal group, and it is the reason the operator group of the hyperbolic three-space is the projective linear group rather than the linear group: the fractional linear operator and its negative are the same operator of the sphere, while the two corresponding elements of $SL(2,\mathbb{C})$ act on the spinor bundle with opposite signs. The spinor structure of the covering is cited to *Spin Geometry*, and the article keeps the operator group.

## The Cross Ratio and the Invariants

**Definition.** Let $z_1, z_2, z_3, z_4$ be four distinct points of the sphere. Their **cross ratio** is

$$
[z_1 : z_2 : z_3 : z_4] = \frac{(z_1 - z_3)(z_2 - z_4)}{(z_1 - z_4)(z_2 - z_3)} ,
$$

the expression computed in any affine chart, with the value at $\infty$ taken as the limit.

**Theorem.** The Möbius operators are exactly the bijections of the sphere preserving the cross ratio of every quadruple of distinct points, and they act sharply triply transitively on the sphere: the action on the ordered triples of distinct points is simply transitive, so every operator is determined by the images of three points.

**Proof.** A Möbius transformation carries the quadruple to another quadruple with the same cross ratio, since each factor transforms by the common denominator of the fractional formula; conversely a bijection preserving the cross ratio of every quadruple preserves the cross ratio with three fixed points, hence the value of the fourth in the coordinate in which the three are $0,1,\infty$, which forces the fractional linear formula. The triple transitivity is *Projective Geometry*, and the stabiliser of three points acts trivially on the fourth and therefore is trivial.

**Corollary (the real cross ratio and the hyperbolic distance).** If the four points lie on the real projective line then their cross ratio is real, and for two points $z, w$ of the upper half-plane and two boundary points the cross ratio computes the hyperbolic distance of *Hyperbolic Geometry*; the Möbius operators with real coefficients preserve the upper half-plane and the hyperbolic metric.

**Proof.** The real line is carried to the real line by a real fractional linear map, so the cross ratio of four real points is real and is preserved; the distance formula of the upper half-plane is the cross ratio with the boundary points of the geodesic through the two points, and the invariance of the cross ratio is the invariance of the distance.

## The Classification of the Möbius Operators

**Definition.** Let $T$ be a Möbius operator represented by a matrix $A \in SL(2,\mathbb{C})$. Its **trace** is defined up to sign, $\operatorname{tr} T = \pm\operatorname{tr} A$, and the operator is **elliptic** when $|\operatorname{tr} A| < 2$, **parabolic** when $|\operatorname{tr} A| = 2$, and **hyperbolic** when $|\operatorname{tr} A| > 2$; when the trace is not real the operator is **loxodromic**, a rotation composed with a hyperbolic motion.

**Theorem.** The number of fixed points of a Möbius operator on the sphere and the type are decided by the trace: an elliptic operator with real trace has two fixed points, conjugate under the antipodal involution and not on the real line, and acts as a rotation of the sphere about them; a parabolic operator has exactly one fixed point and acts as a limit rotation; a hyperbolic operator with real trace has two fixed points on the real line and acts as a translation along the geodesic joining them; a loxodromic operator has two fixed points and acts as a screw motion.

**Proof sketch.** Normalise the matrix by conjugacy in $SL(2,\mathbb{C})$ to its Jordan form: the elliptic case has eigenvalues $e^{\pm i\theta}$, conjugate on the unit circle and giving a diagonal matrix with fixed points $0$ and $\infty$; the parabolic case is the Jordan block with the single fixed point; the hyperbolic case has positive real eigenvalues $\lambda, \lambda^{-1}$ and acts by $z \mapsto \lambda^2 z$; the loxodromic case has complex eigenvalues of nonunit modulus. The fixed points of the fractional formula are the roots of $cz^2 + (d-a)z - b = 0$, and the discriminant is $\operatorname{tr}^2 - 4$.

**Remark.** The classification is the two-dimensional form of the classification of the isometries of hyperbolic space, and the three real types are the elliptic, parabolic and hyperbolic classes of *Hyperbolic Geometry*; the loxodromic type has no real three-space analogue in dimension two and appears as the general complex class. The distinction by the trace is the same as the sign trichotomy of the quadratic form $x^2 - y^2$ of the split-complex algebra, and the operator reading collects the cases in one determinant-two group.

## The Action on Hyperbolic Space

### The Poincaré Extension

**Theorem.** The operator group $PSL(2,\mathbb{C})$ acts on the upper half-space

$$
\mathbb{H}^3 = \{(x, t) : x \in \mathbb{C},\ t > 0\}
$$

as its orientation-preserving isometry group, by the action of $SL(2,\mathbb{C})$ on the quaternionic coordinates $(z, t) \mapsto (z + t j)$ and the formula

$$
g \cdot (z + tj) = (a(z + tj) + b)(c(z + tj) + d)^{-1} ,
$$

for $g$ the class of $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$; the action on the boundary sphere $\hat{\mathbb{C}}$ is the fractional linear action, and it is the conformal boundary action of *Hyperbolic Geometry*.

**Proof.** The formula is the Poincaré extension of the boundary map, and it is well defined because the quaternionic inverse is available wherever the denominator is invertible; the differential of the action at a point scales the hyperbolic metric by the same positive factor from the numerator and the denominator, so the action is isometric, and every orientation-preserving isometry of the half-space extends to a conformal map of the boundary, which is Möbius. The statement and the proof are in *Hyperbolic Geometry*.

**Corollary.** The real Möbius group $PSL(2,\mathbb{R})$ is the orientation-preserving isometry group of the hyperbolic plane acting on the upper half-plane, and the subgroup $PSU(2) = PSL(2,\mathbb{C})$-stabilising a hyperbolic point is the rotation group of the hyperbolic sphere; the fixed points of the operator in the interior are the interior fixed points of its isometric action, and the classification by the trace is the classification of the isometries.

### The Subgroups of the Operator Group

**Definition.** The **stabiliser of a point** $z_0$ of the sphere is the subgroup of $PSL(2,\mathbb{C})$ fixing $z_0$, a conjugate of the group of the affine fractional linear maps $z \mapsto az + b$ with $a \neq 0$ modulo scalars; the **stabiliser of a pair** of points is the group of the fractional linear maps preserving the pair, a conjugate of the diagonal group and its extension by the inversion exchanging the two points.

**Proposition.** The stabiliser of a point is the semidirect product of the rotations about the point and the translations, of real dimension $4$; the stabiliser of a hyperbolic geodesic is a conjugate of the group of the real fractional linear maps extended by the involution exchanging the endpoints; the operator group preserves the cross ratio of the four points consisting of the two endpoints of a geodesic and a pair of points on it, and this cross ratio is the translation length.

**Proof.** A fractional linear map fixing $\infty$ is affine, and the affine group of the complex line is the semidirect product of the translations and the multiplications; the stabiliser of a geodesic is the stabiliser of its two boundary points, which is the real fractional linear group extended by the exchange, and the cross ratio of the four points computes the distance along the geodesic by the distance formula.

**Remark (the limit set and the forward reference).** A discrete subgroup of the operator group has a limit set on the boundary sphere, and the geodesic flow on the quotient is the dynamical system that Part III studies; the measure-theoretic and the ergodic statements about the flow are cited there, and the present article keeps the operator and its isometric action. This is the boundary between the geometry of the operator and the analysis of its flow, and it is the point at which the hyperbolic geometry of this Part meets the dynamical systems of Part III.

## Summary

The Möbius transformations are the fractional linear operators $z \mapsto (az+b)/(cz+d)$ of the Riemann sphere, and they are exactly the projectivities of the complex projective line; the operator group is $PSL(2,\mathbb{C}) = SL(2,\mathbb{C})/\{\pm I\}$, a two-to-one quotient of the determinant-one matrices, and it acts sharply triply transitively. The operators are exactly the cross-ratio-preserving bijections of the sphere, and the cross ratio of four points, reduced to the real line, is the hyperbolic distance. The operators are classified by the trace of a matrix into the elliptic, parabolic, hyperbolic and loxodromic classes, according to the number and the position of the fixed points and to the nature of the eigenvalues. The group acts on the upper half-space by the Poincaré extension as its orientation-preserving isometry group, the real subgroup $PSL(2,\mathbb{R})$ is the orientation-preserving isometry group of the hyperbolic plane, and the stabilisers of a point, a pair of points and a geodesic are the conjugates of the affine, the diagonal and the real groups. The discrete subgroups, their limit sets and the geodesic flow on their quotients are the dynamical systems of Part III.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\hat{\mathbb{C}} = \mathbb{P}^1(\mathbb{C})$ | Riemann sphere, the complex projective line |
| $z \mapsto (az+b)/(cz+d)$ | Fractional linear (Möbius) operator |
| $ad - bc \neq 0$ | Nondegeneracy of the matrix |
| $PSL(2,\mathbb{C}) = PGL(2,\mathbb{C})$ | Operator group of the sphere |
| $SL(2,\mathbb{C}) \to PSL(2,\mathbb{C})$ | Two-to-one covering, kernel $\{\pm I\}$ |
| $[z_1:z_2:z_3:z_4]$ | Cross ratio; complete invariant of the quadruples |
| $\operatorname{tr} T = \pm\operatorname{tr} A$ | Trace of the operator, defined up to sign |
| elliptic, parabolic, hyperbolic, loxodromic | Types by $|\operatorname{tr}| < 2$, $= 2$, $> 2$, non-real trace |
| $\mathbb{H}^3$ | Upper half-space, hyperbolic three-space |
| Poincaré extension | The isometric action of $PSL(2,\mathbb{C})$ on $\mathbb{H}^3$ |
| $PSL(2,\mathbb{R})$ | Orientation-preserving isometry group of the hyperbolic plane |
| limit set | Boundary accumulation set of a discrete subgroup (Part III) |

## Further Reading

- Alan F. Beardon, *The Geometry of Discrete Groups* (Springer, 1983), for Möbius transformations, the cross ratio and the classification.
- John B. Conway, *Functions of One Complex Variable*, 2nd ed. (Springer, 1978), for the fractional linear maps and the Riemann sphere.
- John G. Ratcliffe, *Foundations of Hyperbolic Manifolds*, 2nd ed. (Springer, 2006), for the Poincaré extension and the isometry groups.
- Joseph Lehner, *Discontinuous Groups and Automorphic Functions* (American Mathematical Society, 1964), for the discrete subgroups and their limit sets.
- William F. Reynolds, "Hyperbolic geometry on a hyperboloid", *American Mathematical Monthly* 100 (1993), 442–455, for the models and their isometry groups.
