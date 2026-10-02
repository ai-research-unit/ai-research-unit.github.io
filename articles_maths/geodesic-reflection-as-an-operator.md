
# __Geodesic Reflection as an Operator__

## Introduction

A **geodesic reflection** is the isometry of a geometry that fixes a geodesic, or a totally geodesic hypersurface, point by point and reverses the direction normal to it; it is the reflection of the geometry, generalised from the Euclidean hyperplane to the sphere, the hyperbolic space and the symmetric spaces. The article reads it in the operator layer of this Part, in the **signed two-sided** slot: the reflection is the**signed conjugation** of the ambient Clifford algebra by a vector, $x \mapsto -a\,x\,a^{-1}$, whose geometric meaning is the reflection in the hyperplane orthogonal to $a$, and the sign is the grade involution that negates the vectors. The inversion of Möbius geometry is the same operator in the conformal model, and the symmetry of a geodesic is the family of reflections it generates.

The article develops the reflection in a geodesic hyperplane of the three constant-curvature geometries, its realisation as an inversion in the Möbius and conformal models, its expression as a signed two-sided operator of the Clifford algebra, the geodesic symmetry of a symmetric space and the fixed geodesic of the reflection, and the action of the reflection on the boundary at infinity. The Cartan–Dieudonné theorem closes the article with the statement that every isometry of the geometry is a product of reflections.

The article assumes *Euclidean Geometry*, *Spherical Geometry* and *Hyperbolic Geometry* for the constant-curvature spaces and their isometries; *Möbius and Lie Sphere Geometry* for the inversion and the conformal models; *Symmetric Spaces*, later in this Part, for the geodesic symmetry of a symmetric space; and *Clifford Algebras* of Part II, *The Signed Sandwich on an Ordered Algebra* of Part III, and *Reflections as Signed Two-Sided Operators on a Linear Space* and *The Signed Adjoint of the Reflection on a Linear Space* of Part I for the graded algebra, the signed sandwich and the adjoint of a reflection. The article owns the geometric instance of the signed two-sided operator. No physics is invoked.

## The Reflection in a Geodesic

### The Euclidean and the Spherical Cases

**Definition.** Let $(M,g)$ be a Riemannian manifold and let $\Sigma \subseteq M$ be a totally geodesic hypersurface. The **reflection in $\Sigma$** is the isometry $s_\Sigma$ fixing $\Sigma$ pointwise and reversing the normal direction, $s_\Sigma|_\Sigma = \mathrm{id}$ and $ds_\Sigma(\nu) = -\nu$ for a unit normal $\nu$ along $\Sigma$; it is defined when such an isometry exists, and it is then unique.

**Example (the Euclidean space).** For $M = \mathbb{R}^n$ and $\Sigma = a^\perp$ the hyperplane orthogonal to a nonzero vector $a$, the reflection is the linear map

$$
s_a(x) = x - 2\,\frac{\langle x, a\rangle}{\langle a,a\rangle}\, a ,
$$

the classical reflection; it is an orthogonal transformation of determinant $-1$, it is an involution, and in the orthogonal group $O(n)$ the reflections generate the group.

**Example (the sphere).** For $M = S^n \subseteq \mathbb{R}^{n+1}$ and $\Sigma = S^n \cap a^\perp$ the great sphere orthogonal to a unit vector $a$, the reflection is the restriction of the Euclidean reflection $x \mapsto x - 2\langle x,a\rangle a$, so it fixes the great sphere pointwise and reverses the normal $a$; on the sphere the reflections are the elements of $O(n+1)$ with an eigenvalue $-1$ on the ambient line, and they generate the orthogonal group of the sphere.

**Proposition.** A reflection is an involution and an isometry, it fixes the hypersurface $\Sigma$ and no point outside it is fixed; the differential at a point of $\Sigma$ has the eigenvalue $-1$ on the normal line and the eigenvalue $+1$ on the tangent space, so the reflection is orientation-reversing when it reverses the normal of a hypersurface in an odd-dimensional space in the appropriate sense, and its determinant in the ambient orthogonal group is $-1$.

**Proof.** The definition gives $s_\Sigma^2 = \mathrm{id}$ and $ds_\Sigma^2 = \mathrm{id}$; the fixed set of an isometry is a totally geodesic submanifold, hence the fixed set is exactly $\Sigma$; the eigenvalues of the differential are read from the two eigenspaces, and the determinant is the product, which is $-1$ for the reflection in a hypersurface of the ambient group.

### The Hyperbolic Case and the Geodesic Symmetry

**Definition.** In the hyperboloid model of the hyperbolic space,

$$
\mathbb{H}^n = \{x \in \mathbb{R}^{n,1} : B(x,x) = -1,\ x_0 > 0\}
$$

with the form $B$ of signature $(n,1)$, a **geodesic hyperplane** is the intersection of $\mathbb{H}^n$ with a linear hyperplane $a^\perp$ for a spacelike vector $a$, that is, one with $B(a,a) > 0$; the **reflection** in it is the restriction of the linear map

$$
s_a(x) = x - 2\,\frac{B(x,a)}{B(a,a)}\, a ,
$$

which fixes $a^\perp$ pointwise and sends $a$ to $-a$.

**Proposition.** The map $s_a$ is an element of $O(n,1)$ and it preserves the hyperboloid and the time orientation, so it is an isometry of $\mathbb{H}^n$; it is the reflection in the totally geodesic hypersurface $\mathbb{H}^n \cap a^\perp$, it is an involution, and it is realised as an inversion in the Möbius model of the boundary.

**Proof.** The form is preserved because the reflection formula is the orthogonal reflection in the hyperplane $a^\perp$ with respect to $B$, and this reflection lies in $O(n,1)$; it preserves the hyperboloid because it preserves the form and the sign of the time coordinate, and the fixed set is the geodesic hypersurface. The realisation by an inversion is the statement of the next section.

**Definition.** Let $p \in \mathbb{H}^n$. The **geodesic symmetry** at $p$ is the isometry $s_p$ fixing $p$ with $ds_p = -\mathrm{id}$ on the tangent space $T_p\mathbb{H}^n$; in the hyperboloid model it is the reflection in the timelike line $\mathbb{R}p$,

$$
s_p(x) = -x + 2\,\frac{B(x,p)}{B(p,p)}\, p = -\bigl(x - 2\,B(x,p)\,p\bigr) ,
$$

using $B(p,p) = -1$; it fixes $p$, reverses every geodesic through $p$, and it is the reflection in the point $p$ of the hyperbolic space.

**Proposition.** The geodesic symmetry at $p$ is an isometry of order two, it reverses the geodesic through $p$ in every direction, and the composition $s_q \circ s_p$ of the symmetries at two points is the translation along the geodesic joining them; the hyperbolic space is the model of a symmetric space in the sense of *Symmetric Spaces*.

**Proof.** The formula is the reflection in the line $\mathbb{R}p$ in the ambient form, so it preserves the form and the hyperboloid, it fixes $p$ and reverses the tangent space, and its square is the identity; the composition of two-point symmetries acts on the geodesic through $p$ and $q$ by the translation of twice the distance, which is the defining property of a symmetric space. The statement is in *Hyperbolic Geometry* and *Symmetric Spaces*.

## The Inversion and the Möbius Reflection

### The Inversion

**Definition.** The **inversion** in the sphere of radius $r$ about the origin of $\mathbb{R}^n$ is the map

$$
i(x) = \frac{r^2}{|x|^2}\, x ,
$$

extended to the conformal sphere by $i(0) = \infty$ and $i(\infty) = 0$; it is a conformal map, an involution, and it is the Möbius transformation with the property that every sphere through the origin is carried to a hyperplane not through the origin.

**Proposition.** The inversion is the reflection in the sphere: it fixes the sphere of inversion pointwise, it exchanges the interior and the exterior, and it reverses the normal direction on the sphere; it is the conformal analogue of the reflection in a hyperplane, and the hyperplane reflection is the limit of the inversions as the radius tends to infinity.

**Proof.** The computation of the differential of $i$ gives $di = \frac{r^2}{|x|^2}\left(I - 2\frac{xx^{\mathsf T}}{|x|^2}\right)$, which is a reflection composed with a positive scalar, so the inversion is conformal and reverses the normal on the sphere of inversion; the image of a sphere through the origin is computed by the standard formula of the inversion, and the limit of a large sphere is a hyperplane.

### The Reflection in a Geodesic as a Möbius Involution

**Theorem.** In the Poincaré ball model of the hyperbolic space, the geodesic hyperplane with the boundary sphere $\Sigma_\infty$ is the intersection of the ball with a sphere orthogonal to the boundary sphere, and the reflection in the geodesic hyperplane is the restriction to the ball of the **inversion** in that orthogonal sphere; on the boundary the reflection acts as the Möbius involution fixing $\Sigma_\infty$ pointwise, and the reflection is determined by its boundary action.

**Proof.** The isometry group of the ball model is the Möbius group acting on the ball, and the isometries fixing a geodesic hyperplane pointwise are the inversions in the spheres orthogonal to the boundary; the fixed set of such an inversion on the boundary is the intersection of the sphere with the boundary sphere, which is the boundary of the geodesic hyperplane. The statement is in *Hyperbolic Geometry* and *Möbius and Lie Sphere Geometry*.

**Corollary.** A reflection in a geodesic of the hyperbolic plane is an inversion in a circle orthogonal to the boundary circle, and its two fixed points on the boundary are the endpoints of the geodesic; the geodesic itself is the fixed point set in the interior, and the reflection is the Möbius involution classified in *The Möbius Transformation as an Operator*.

**Proof.** The two-dimensional case is the intersection of a circle orthogonal to the boundary circle, whose fixed points on the boundary are the two intersection points; the geodesic joining them is fixed pointwise, and the classification of the Möbius involutions by their fixed points is the one of the companion article.

## The Reflection as a Signed Two-Sided Operator

### The Clifford Formula

**Definition.** Let $(V,q)$ be a quadratic space with polar form $B$ and let $a \in V$ with $q(a) \neq 0$. In the Clifford algebra $\mathrm{Cl}(V,q)$ the **reflection in the hyperplane** $a^\perp$ is the signed conjugation by the vector $a$,

$$
\rho_a(x) = -\,a\,x\,a^{-1} = a\,\alpha(x)\,a^{-1},
$$

where $\alpha$ is the grade involution, which acts on the vectors by $x \mapsto -x$ and on the scalars by the identity; the vector $a$ is the **reflection element**, and the sign in the formula is the sign of the odd part of the grading.

**Theorem.** For every vector $x \in V$ the signed conjugation of the definition is the reflection

$$
\rho_a(x) = x - 2\,\frac{B(x,a)}{q(a)}\,a ,
$$

so it is the reflection in the hyperplane $a^\perp$; the map $\rho_a$ is the signed two-sided operator $\Theta^{\alpha}_{a,a^{-1}}$ of *The Signed Sandwich on an Ordered Algebra*, and it is the operator form of the geodesic reflection in the constant-curvature geometries.

**Proof.** In the Clifford algebra the vector identity $ax + xa = 2B(x,a)$ holds; multiplying by $a^{-1}$ on the right gives $a x a^{-1} = 2B(x,a)\,a^{-1} - x = 2B(x,a)\,a/q(a) - x$, since $a^{-1} = a/q(a)$; the negative of this is the reflection formula. The identification with the signed sandwich is the definition of the reflection element $a$ with $a^{-1} = a/q(a)$, and the geometric instances are the Euclidean and hyperbolic reflections of the previous sections.

**Corollary (the Cartan–Dieudonné theorem).** Every orthogonal transformation of a nondegenerate quadratic space is the product of at most $\dim V$ reflections,

$$
O(V,q) \ni T = \rho_{a_1}\circ\cdots\circ\rho_{a_k}, \qquad k \leq \dim V ,
$$

and the number of the factors is the dimension of the space of the vectors moved by $T$; the orientation-preserving transformations are the products of an even number of reflections.

**Proof.** The classical theorem is proved by induction on the dimension: if $T$ moves a vector $v$ then the composition $\rho_{T(v)-v}\circ T$ fixes $v$, reduces to the hyperplane $v^\perp$ and the induction applies; the parity statement follows because each reflection has determinant $-1$. The statement and the proof are in *Clifford Algebras* and *The Signed Adjoint of the Reflection on a Linear Space*.

**Remark (the sign and the two sides).** The reflection is the signed two-sided operator with the two parameters $a$ and $a^{-1}$, and the sign is the grade involution; the two-sided form records that the reflection is the conjugation, while a general isometry of the geometry is a product of these signed operators. The sign is what distinguishes the reflection in the hyperplane from the two-sided operator $x \mapsto axa^{-1}$ without the twist, which is a rotation-like map rather than a reflection, and it is the reason the reflection is placed in the signed two-sided slot of the category.

## The Symmetry of a Geodesic

**Definition.** Let $\gamma \subseteq M$ be a geodesic of a Riemannian manifold. A **symmetry of the geodesic** is an isometry of $M$ that preserves $\gamma$ and reverses its parameter, $f(\gamma(t)) = \gamma(-t)$ after the choice of the origin; the full group of the isometries preserving $\gamma$ contains the translations along $\gamma$, and the symmetries are the coset reversing the parameter.

**Proposition.** The reflection in a geodesic hyperplane $\Sigma$ fixes pointwise every geodesic contained in $\Sigma$, and for a geodesic $\gamma$ orthogonal to $\Sigma$ it reverses $\gamma$; the geodesic symmetry at $p$ reverses every geodesic through $p$, so the composition of the two symmetries at the endpoints of a geodesic segment is the reflection in the perpendicular bisector hypersurface, and the three operators generate the symmetric group of the motions of the geodesic.

**Proof.** The reflection fixes $\Sigma$ pointwise and reverses the normal, so a geodesic in $\Sigma$ is fixed pointwise and a geodesic orthogonal to $\Sigma$ is reversed; composing the geodesic symmetries at the two endpoints of a segment gives an isometry fixing the midpoint and reversing the segment, which is the reflection in the perpendicular bisector. The statement is the elementary geometry of the symmetric space, in *Symmetric Spaces*.

**Theorem (the fixed geodesic of the reflection).** Let $s$ be an involution of a simply connected space of constant curvature that fixes a complete geodesic $\gamma$ pointwise and reverses the normal to it. Then $s$ is the reflection in the totally geodesic hypersurface $\gamma^\perp$; the fixed set of $s$ is that hypersurface, and $\gamma$ is one of the geodesics orthogonal to it, reversed by $s$. In particular the reflections and the geodesic symmetries are exactly the involutions of the isometry group with a totally geodesic fixed set of codimension one.

**Proof.** In the constant-curvature space the isometry group is the orthogonal group of the ambient form, and an involution of the group with a fixed geodesic is an orthogonal involution with $+1$ on the tangent space of the fixed hypersurface and $-1$ on the normal, which is the reflection; the geodesic is reversed because its tangent lies along the normal. The statement is the standard classification of the involutions, in *Symmetric Spaces*.

## Summary

A geodesic reflection is the isometry fixing a totally geodesic hypersurface $\Sigma$ pointwise and reversing the normal, generalising the Euclidean reflection $s_a(x) = x - 2\langle x,a\rangle a/\langle a,a\rangle$ to the sphere, the hyperbolic space and the symmetric spaces; it is an involution with the eigenvalue $-1$ on the normal and $+1$ on the tangent space. In the hyperboloid model it is $s_a(x) = x - 2B(x,a)a/B(a,a)$ for a spacelike $a$, and the geodesic symmetry at $p$ is the reflection $s_p(x) = -x - 2B(x,p)p$ in the timelike line through $p$, whose compositions give the translations. In the Möbius and Poincaré models the reflection in a geodesic is the **inversion** in the sphere orthogonal to the boundary, and on the boundary it is the Möbius involution fixing the boundary of the geodesic hyperplane. In the Clifford algebra the reflection is the **signed two-sided operator** $\rho_a(x) = -a x a^{-1} = a\alpha(x)a^{-1}$, the signed conjugation by the vector $a$ with the grade involution, and the Cartan–Dieudonné theorem expresses every orthogonal transformation as a product of at most $\dim V$ such reflections. The reflections and the geodesic symmetries are the involutions of the isometry group with a totally geodesic fixed set, and the two-point symmetries generate the translations along the geodesics.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $s_\Sigma$ | Reflection in a totally geodesic hypersurface $\Sigma$ |
| $s_a(x) = x - 2\langle x,a\rangle a/\langle a,a\rangle$ | Euclidean reflection in $a^\perp$ |
| $\mathbb{H}^n = \{x : B(x,x) = -1,\ x_0 > 0\}$ | Hyperboloid model, $B$ of signature $(n,1)$ |
| $s_a(x) = x - 2B(x,a)a/B(a,a)$ | Reflection in a geodesic hyperplane (spacelike $a$) |
| $s_p(x) = -x - 2B(x,p)p$ | Geodesic symmetry at $p$ |
| $i(x) = r^2 x/|x|^2$ | Inversion in a sphere |
| $\rho_a(x) = -a x a^{-1} = a\alpha(x)a^{-1}$ | Reflection as a signed two-sided operator |
| $\alpha$ | Grade involution, $x \mapsto -x$ on the vectors |
| Cartan–Dieudonné | Every orthogonal map is at most $\dim V$ reflections |
| Möbius involution | Boundary action of a reflection in a geodesic |

## Further Reading

- Marcel Berger, *Geometry I* (Springer, 1987), for the reflections, the inversions and the classical geometries.
- Dmitri V. Alekseevskii and Helmut Baum, "Reflections", in *Encyclopaedia of Mathematics* (Kluwer, 1990), for the reflection in a symmetric space.
- John G. Ratcliffe, *Foundations of Hyperbolic Manifolds*, 2nd ed. (Springer, 2006), for the hyperboloid model, the reflections and the geodesic symmetries.
- Percival F. Smith, *An Introduction to Riemannian Geometry and the Tensor Calculus* (Cambridge University Press, 1938), for the geodesic symmetries and the symmetric spaces.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2001), for the reflection formula $x \mapsto -axa^{-1}$ and the Cartan–Dieudonné theorem.
- O. Timothy O'Meara, *Introduction to Quadratic Forms* (Springer, 1973), for the orthogonal groups and the generation by reflections.
