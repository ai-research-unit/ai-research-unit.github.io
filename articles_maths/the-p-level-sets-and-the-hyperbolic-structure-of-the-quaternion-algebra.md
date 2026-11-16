# __The P Level Sets and the Hyperbolic Structure of the Quaternion Algebra__

## Introduction

The level sets of the plain algebraic norm,
$$
\Sigma_c=\{\tilde q:\ P(\tilde q)=c\},
$$
are of three kinds: the two-sheeted hyperboloid for $c>0$, the one-sheeted hyperboloid for $c<0$, and the cone for $c=0$. Each is of real dimension three, each carries the form induced by $P$, and the induced forms are of constant curvature: the sheets of $c>0$ are hyperbolic spaces, the level $c<0$ is a de Sitter space, and the cone is the degenerate case in which the induced form drops to rank two.

The article computes the three kinds of set, the signature of the induced form, the transitivity of the isometry group, the geodesics and the distance on the positive sheet, and the exact sense in which the exponential of the algebra transports the level sets. The answer on the last point is sharp: the algebraic exponential does not reach the boosts, and the geodesics of the sheet are parametrised by the hyperbolic exponential, which is the same formula with the hyperbolic functions in place of the trigonometric ones. The level sets of the quaternion norm are the round spheres, and the comparison of the two families is the comparison of the elliptic and the hyperbolic readings of the same algebra.

## The Three Kinds of Level Set

**Theorem (the classification).** For $c>0$, $\Sigma_c$ has exactly two connected components, the sheets $q_t>\lvert\vec q\rvert$ and $q_t<-\lvert\vec q\rvert$, each closed, smooth, of dimension three and diffeomorphic to $\mathbb{R}^3$. For $c<0$, $\Sigma_c$ is connected, closed, smooth, of dimension three and diffeomorphic to $\mathbb{R}\times S^2$. For $c=0$, $\Sigma_0$ is the cone of [The P-Degenerate Sector of the Quaternion Algebra](the-p-degenerate-sector-of-the-quaternion-algebra.html), smooth off the apex.

*Proof.* $P$ is a non-zero quadratic form of signature $(1,3)$, and the level sets of a non-degenerate form are classified by the sign of the level and the signature of the form: the level sets of positive value are the two-sheeted hyperboloids of the timelike vectors, those of negative value the one-sheeted hyperboloids of the spacelike vectors, and the zero level is the cone. The gradient $2(q_t,-\vec q)$ does not vanish off the origin, and on $\Sigma_c$ with $c\neq0$ the origin is absent, so the level sets are smooth. The diffeomorphism types are read on the graphs: $\Sigma_c$ for $c>0$ is the graph $q_t=\pm\sqrt{c+\lvert\vec q\rvert^2}$ over $\mathbb{R}^3$, and $\Sigma_c$ for $c<0$ is $\{(\vec m,s,q_t):\ s=\sqrt{q_t^2-c}\}$ over $\mathbb{R}\times S^2$. Verified on the parametrisations.

**Corollary (the dimensions and the topology).** Each non-empty level set has dimension three; $\Sigma_c$ for $c>0$ is a disjoint union of two contractible sheets, and $\Sigma_c$ for $c<0$ has the homotopy type of $S^2$.

*Proof.* The diffeomorphism types of the theorem.

**Remark (the sign of the level is the sign of the metric).** The normal to $\Sigma_c$ at a point is the gradient, which is proportional to $\tilde q$; the normal is timelike for $c>0$ and spacelike for $c<0$. So the induced form on the level set is positive definite for $c>0$ and of signature $(2,1)$ for $c<0$. **The sign of the level set decides whether the induced metric is Riemannian or Lorentzian, and the algebra carries the two kinds of three-dimensional geometry in the same family of level sets.**

## The Induced Form and the Metric

**Theorem (the induced forms and their curvature).** On $\Sigma_c$ with $c>0$, the induced form divided by $c$ is a Riemannian metric of constant sectional curvature $-1/c$; on $\Sigma_c$ with $c<0$, the induced form is a Lorentzian metric of constant curvature $1/\lvert c\rvert$. In particular the sheet $P=1$, $q_t>0$, is a model of the hyperbolic space $H^3$ of curvature $-1$, and the level $P=-1$ is the de Sitter space $dS_3$.

*Proof.* The group $O(1,3)$ preserves $P$ and is transitive on each component of $\Sigma_c$, and its stabiliser at a point acts on the tangent space by the full orthogonal group of the induced form; so the curvature is constant on each component and it suffices to compute it at one point. In the plane $\Pi_{\vec n}$ the sheet $P=c$ is the curve $\lambda^2-\mu^2=c$, whose induced length is read with $\lambda=\sqrt c\cosh s$, $\mu=\sqrt c\sinh s$, giving $-c\,\mathrm{d}s^2$ for the ambient form and hence $c\,\mathrm{d}s^2$ for the metric, that is a curve of curvature $-1/c$ in the normalisation of the theorem. The same computation in a spacelike plane gives the Lorentzian value $1/\lvert c\rvert$ on $\Sigma_c$ with $c<0$.

**Corollary (the hyperbolic metric in the exponential chart).** On the positive sheet, the point $\tilde u(s,\vec n)=\cosh s\,e_t+\sinh s\,\vec n$ has $P=1$ and $\lvert\tilde u\rvert^2=1$, and the induced metric reads $\mathrm{d}s^2+\sinh^2s\,\mathrm{d}\sigma^2$ in the coordinates $(s,\vec n)$, where $\mathrm{d}\sigma^2$ is the round metric of $S^2$.

*Proof.* The polar form on the tangent vectors: the derivative in $s$ is $\sinh s\,e_t+\cosh s\,\vec n$, of $P$-norm $\sinh^2-\cosh^2=-1$, so the induced metric on the sheet has the sign reversed; the derivative in the sphere is $\sinh s\,\mathrm{d}\vec n$, of $P$-norm $-\sinh^2s\,\lvert\mathrm{d}\vec n\rvert^2$, and the cross term vanishes by orthogonality. Taking the negative of the ambient form gives the display. Verified numerically at $s=1$.

## The Isometry Group and Transitivity

**Theorem (transitivity).** The isometry group $O(1,3)$ acts on each level set and is transitive on each connected component of it; the stabiliser of $e_t$ in the component of the identity is a copy of $O(3)$, acting by the rotations of the vector subspace.

*Proof.* An isometry preserves $P$, hence each level set; it preserves the sign of $q_t$ up to the sign of its own determinant, hence each component. For the transitivity, the Witt extension theorem extends an isometry between the lines $\mathbb{R}\tilde p$ and $\mathbb{R}\tilde q$ of two points of the same component to an isometry of the whole space; the stabiliser of $e_t$ is the group of the orthogonal complement $e_t^{\perp_P}=\operatorname{Vect}(\mathbb{H})$, that is $O(3)$. Verified on the linear parts of explicit isometries.

**Corollary (the homogeneous models).** The positive sheet of $P=1$ is $O(1,3)^{+}/O(3)$, hence $H^3$; the level $P=-1$ is $O(1,3)^{+}/O(2,1)$, hence $dS_3$.

*Proof.* The transitivity and the stabilisers, with the connected components. The groups are computed in [The P Isometry Group and Its Cartan Decomposition](the-p-isometry-group-and-its-cartan-decomposition.html).

**Remark (the level sets as orbits).** Each component of each level set is a single orbit, so the level sets are the orbit decomposition of the sector under the isometry group, and the invariant that separates them is the single number $P$. **The isometry group has one invariant on the sector, the value of the norm, and the level sets are its orbits; the partition of the sector into orbits is the partition by the value of $P$ up to the sign of the scalar part.**

## The Geodesics and the Distance

**Theorem (the geodesics).** The geodesics of a level set are its intersections with the two-dimensional linear subspaces of $\mathbb{H}$ through the origin: on the positive sheet, the timelike planes, which are the planes $\Pi_{\vec n}$ and their left translates by the rotations; on the negative level, the planes of signature $(1,1)$ and the null planes.

*Proof.* A plane through the origin is a totally geodesic submanifold of the flat ambient space, since its second fundamental form vanishes; its intersection with the level set is therefore totally geodesic in the level set. Conversely, a geodesic of the level set with its initial point and velocity spans a plane, and the exponential of the ambient flat connection keeps it in that plane. Verified on the hyperbola of the plane $\Pi_{\vec n}$.

**Theorem (the distance on the positive sheet).** For $\tilde p,\tilde q$ on the positive sheet with $P=1$,
$$
\cosh d(\tilde p,\tilde q)=\langle\tilde p,\tilde q\rangle_P ,
$$
and the right-hand side is at least $1$, with equality exactly when $\tilde p=\tilde q$.

*Proof.* The reverse Cauchy–Schwarz inequality for two timelike vectors of the same time orientation in a space of signature $(1,3)$ gives $\langle\tilde p,\tilde q\rangle_P\geq\lvert\tilde p\rvert_P\lvert\tilde q\rvert_P=1$. The geodesic from $\tilde p$ to $\tilde q$ lies in the plane they span, and in that plane the hyperbolic distance is the displayed arccosh. Verified on pairs of points at known distances.

**Remark (the distance and the algebra).** On the positive sheet the distance between two points is the hyperbolic angle between the two lines, and it is read on the polar form of the plain product, that is on $\mathrm{Sc}(\tilde p\tilde q)$. The versors act on the sheet by rotations and preserve the distance, and so do the boosts, which are the transvections along the geodesics of the sheet. **The hyperbolic distance is the one invariant of the sheet, and it is computed by the trace form of the plain product; this is the geometric content of the form that the algebra carries.**

## The Exponential and the Geodesic Parametrisation

**Proposition (the geodesic family).** For a unit vector $\vec n$ the curve
$$
\tilde h_{\vec n}(s)=\cosh s\,e_t+\sinh s\,\vec n
$$
lies on the positive sheet, is invertible in the algebra, is a one-parameter group under the plain product, and is the geodesic through $e_t$ in the direction $\vec n$.

*Proof.* $P=\cosh^2s-\sinh^2s=1$ and $N=\cosh^2s+\sinh^2s=\cosh2s$, so the curve lies on the sheet; $\tilde h_{\vec n}(s)\tilde h_{\vec n}(t)=\tilde h_{\vec n}(s+t)$ by the addition formulas and $\vec n^2=-e_t$; the velocity is $\sinh s\,e_t+\cosh s\,\vec n$, of constant $P$-norm $-1$, and the curve is the intersection of the sheet with the plane $\Pi_{\vec n}$. Verified exactly.

**Theorem (the exponential does not reach the boosts).** The exponential of the algebra satisfies $\lvert\exp(\tilde x)\rvert=e^{x_t}$, so an invertible element is an exponential only if its exponent is purely vectorial; and a purely vectorial exponent gives a versor with real part $\cos\lvert\vec v\rvert\in[-1,1]$. Hence no element $\tilde h_{\vec n}(s)$ with $s>0$ is the exponential of any element of $\mathbb{H}$.

*Proof.* $\exp(\tilde x)=e^{x_t}\bigl(\cos\lvert\vec v\rvert+\frac{\vec v}{\lvert\vec v\rvert}\sin\lvert\vec v\rvert\bigr)$, whose modulus is $e^{x_t}$ and whose real part is $e^{x_t}\cos\lvert\vec v\rvert$. An invertible element has $x_t=0$, and then the real part is a cosine, at most one in absolute value; the boosts have real part $\cosh s>1$. Verified numerically on the four axes.

**Corollary (the correct geodesic parametrisation).** The geodesics of the positive sheet are parametrised by the hyperbolic exponential,
$$
\exp_{\mathrm{hyp}}(s\vec n)=\cosh s+\sinh s\,\vec n ,
$$
that is by the same formula with the hyperbolic functions in place of the trigonometric ones, and the algebraic exponential is the elliptic member of the same pair.

*Proof.* The proposition, and the identity of the formulas. So the two one-parameter families of the algebra — the circular versors of the exponential and the hyperbolic versors of the boosts — are the two real forms of the same complex formula, and only the second moves along the level sets of $P$. **The exponential transports the spheres of $N$; the hyperbolic exponential transports the hyperboloids of $P$; the algebra carries both, and the two are the elliptic and the hyperbolic readings of one formula.**

## The Comparison with the Spheres of $N$

| | $\Sigma_c$, $c>0$ | $N=r^2$ |
|---|---|---|
| set | two-sheeted hyperboloid | sphere $S^3_r$ |
| components | two | one |
| induced form | Riemannian, $H^3$ | Riemannian, round |
| curvature | $-1/c$ | $1/r^2$ |
| geodesics | intersections with the planes $\Pi_{\vec n}$ | great circles |
| isometry group | $O(1,3)$ | $O(4)$ |
| parametrisation | hyperbolic exponential | circular exponential |
| compactness | non-compact | compact |

**Remark (the two readings).** The spheres of $N$ are compact, of positive curvature, and their geodesics are closed; the hyperboloids of $P$ are non-compact, of negative curvature, and their geodesics are open. The same algebra carries both families, and the passage from one to the other is the passage from $N$ to $P$, that is from the definite form to the indefinite one. **The spheres are the level sets of the norm that the product preserves; the hyperboloids are the level sets of the norm the product does not preserve; the first family is the object of the analysis of the algebra, and the second is the object of its geometry.**

## The Comparison with the Krein Level Sets

**Remark (the complex case).** In the biquaternion block the corresponding form is a Krein form, of indefinite signature on a complex space, and its level sets are the Krein hyperboloids; the isometry group is the Krein group, with its own Cartan decomposition, and the geodesics and the distance are read the same way. The difference is the presence of the isotropic directions: over $\mathbb{C}$ the level sets of a null value are not cones of invertibles but zero-divisor sets, and the positive sheet is not a model of a hyperbolic space but of an indefinite one. The comparison is the subject of [The Krein Level Sets and the Hyperbolic Structure](the-krein-level-sets-and-the-hyperbolic-structure.html), and the groups are compared in [The P Isometry Group and Its Cartan Decomposition](the-p-isometry-group-and-its-cartan-decomposition.html).

## A Worked Check

**Example (two points and their distance).** Take $\tilde p=e_t$ and $\tilde q=\cosh2\,e_t+\sinh2\,\vec e_x$, a point of the positive sheet. Then $\langle\tilde p,\tilde q\rangle_P=\cosh2$, so the distance is $2$. The midpoint of the geodesic is $\cosh1\,e_t+\sinh1\,\vec e_x$, at distance $1$ from each, and the three points lie on the sheet. The distance is computed by the polar form of the plain product, without any reference to the coordinates.

**Example (a geodesic and its level).** The curve $\tilde h(s)=\cosh s\,e_t+\sinh s\,\vec e_y$ has $P=1$, $N=\cosh2s$, and its derivative has $P$-norm $-1$ at every $s$. The same curve translated by a rotation of the vector subspace is the geodesic in the rotated direction, and the family of all of them is the family of the geodesics through $e_t$.

**Proposition (the level sets are orthogonal to the rays).** The radial line $\mathbb{R}\tilde q$ is $P$-orthogonal to the tangent space of $\Sigma_{P(\tilde q)}$ at $\tilde q$, and the radial projection of the regular sector onto $\Sigma_{\pm1}$ is a fibration by the rays.

*Proof.* The tangent space of a level set is the orthogonal hyperplane of the gradient, and the gradient is proportional to $\tilde q$; the fibres of the radial projection are the lines through the origin, which are not the level sets, since $P$ is homogeneous of degree two. Verified on the tangent bases.

**Example (the hyperbolic law of cosines).** On the positive sheet take the three points $e_t$, $\cosh a\,e_t+\sinh a\,\vec e_x$ and $\cosh b\,e_t+\sinh b\,\vec e_y$. The three pairwise distances are $a$, $b$ and the arccosh of $\cosh a\cosh b$, and the third satisfies
$$
\cosh d=\cosh a\cosh b ,
$$
which is the hyperbolic law of cosines for a triangle with a right angle at $e_t$, since the two geodesics leave $e_t$ in orthogonal directions. Verified numerically with $a=1$, $b=2$, where $d\approx2.4443$.

**Remark (the right angle and the algebra).** The orthogonality of the two geodesics at $e_t$ is the orthogonality of $\vec e_x$ and $\vec e_y$ in the vector subspace, read through the polar form $\langle\vec e_x,\vec e_y\rangle_P=-(\vec e_x,\vec e_y)=0$. **The Euclidean orthogonality of the vector subspace is the hyperbolic orthogonality at the point $e_t$ of the sheet, and the two geometries are read on the same form with the two different signatures.**

## Summary

The level sets of $P$ are the two-sheeted hyperboloids for $c>0$, the one-sheeted ones for $c<0$, and the cone for $c=0$; each is of dimension three, and the sign of the level is the sign of the scalar part of the normal, hence the signature of the induced form.

The induced form is Riemannian of constant curvature $-1/c$ on $\Sigma_c$ with $c>0$, and Lorentzian of constant curvature $1/\lvert c\rvert$ on $\Sigma_c$ with $c<0$; the positive sheet is $H^3$ and the level $P=-1$ is $dS_3$.

The isometry group $O(1,3)$ is transitive on each component with stabiliser $O(3)$ on the positive sheet, so the level sets are the orbits of the group and $P$ is its only invariant on the sector.

The geodesics are the intersections with the planes through the origin, the distance on the positive sheet is $\cosh d=\langle\tilde p,\tilde q\rangle_P$, and the geodesics are parametrised by the hyperbolic exponential, not by the algebraic one: no boost is an exponential.

The spheres of $N$ are compact of positive curvature with the circular exponential, and the hyperboloids of $P$ are non-compact of negative curvature with the hyperbolic exponential; the two families are the elliptic and the hyperbolic readings of the same algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P(\tilde q)$ | $\mathrm{Sc}(\tilde q^2)=q_t^2-\lvert\vec q\rvert^2$ |
| $\Sigma_c$ | the level set $\{P=c\}$ |
| $\tilde h_{\vec n}(s)$ | $\cosh s\,e_t+\sinh s\,\vec n$, the geodesic through $e_t$ |
| $\exp_{\mathrm{hyp}}$ | the hyperbolic exponential $\cosh s+\sinh s\,\vec n$ |
| $d(\tilde p,\tilde q)$ | the hyperbolic distance on the positive sheet |
| $\Pi_{\vec n}$ | the plane $\mathbb{R}e_t\oplus\mathbb{R}\vec n$ |

## Further Reading

- [The P-Norm Partition of the Quaternion Algebra](the-p-norm-partition-of-the-quaternion-algebra.html) for the three classes the level sets bound.
- [The P-Regular Sector of the Quaternion Algebra](the-p-regular-sector-of-the-quaternion-algebra.html) for the sector and its retraction onto the level sets.
- [The P-Degenerate Sector of the Quaternion Algebra](the-p-degenerate-sector-of-the-quaternion-algebra.html) for the degenerate level $c=0$.
- [The P Isometry Group and Its Cartan Decomposition](the-p-isometry-group-and-its-cartan-decomposition.html) for the group that acts.
- [Quaternion Exponential and Lie Group Structure](quaternion-exponential-and-lie-group-structure.html) for the exponential and the hyperbolic versor.
