
# __Hyperbolic Geometry__

## Introduction

Hyperbolic geometry is the geometry of constant negative curvature. It is the third of the model geometries of *Curvature and Geodesics*, the one in which the parallel postulate fails in the direction of too many parallels: through a point outside a line there pass infinitely many lines not meeting it, the angles of a triangle sum to less than two right angles, and two geodesics may diverge from one another at an exponential rate. It is the geometry of the algebra $\mathbb{D}$ of split complex numbers with $\omega^2 = +1$, whose hyperbolic rotations are the Lorentz boosts, the $\omega^2 = +1$ case of *The Three Two-Dimensional Algebras and the Three Kinds of Rotation*.

Hyperbolic geometry is the richest of the three model geometries and the one with the deepest connection to the rest of mathematics. Its isometry group in dimension two is the projective linear group $PSL(2, \mathbb{R})$, so its geometry is the geometry of Möbius transformations and of the Riemann sphere with a real boundary; its discrete subgroups are the Fuchsian and Kleinian groups, whose quotient surfaces carry the moduli spaces of complex structures. It is for this reason that the hyperbolic structure on a surface is the geometric realisation of its complex structure, and the deformation theory of the one is the deformation theory of the other.

This article develops hyperbolic geometry from its models. It gives the upper half-plane, the Poincaré disk, the hyperboloid in its Weierstrass coordinates and the Beltrami–Klein ball with its Cayley–Klein metric, with the isometries between them; computes the geodesics and the distance in each; proves the trigonometric laws, which differ from the spherical and Euclidean ones only in the signs and the hyperbolic functions; relates the angle sum to the area through the hyperbolic Gauss–Bonnet theorem; treats the angle of parallelism and the ideal points at infinity; identifies the isometry group with a projective linear group and classifies its elements; and introduces the discrete groups and the space forms, with the Mostow rigidity theorem and the boundary to the Teichmüller theory of the sibling articles.

The article assumes *Smooth Manifolds and Differential Geometry* for manifolds and metrics; *Curvature and Geodesics* and *Riemannian Geometry* for geodesics, curvature, the exponential map, the Gauss–Bonnet theorem and the classification of the space forms; *Pseudo-Riemannian and Lorentzian Geometry* for the quadric space forms, of which the hyperboloid model is the Riemannian member and the Lorentzian hyperboloid $H^{1,n-1}$ the indefinite one; *Euclidean Geometry* for the comparison; *The Three Two-Dimensional Algebras and the Three Kinds of Rotation* for the split-complex case; and *Matrix Groups and Classical Groups* for $SL(2, \mathbb{R})$, $PSL(2, \mathbb{R})$ and the Möbius transformations. The analytic theory of the boundary, the limit set and the ergodic theory of the geodesic flow belongs to Part III, and it is cited rather than developed. No physics is invoked.

## The Models of Hyperbolic Space

### The Upper Half-Plane Model

**Definition.** The **upper half-plane** is $\mathbb{H}^2 = \{z \in \mathbb{C} : \operatorname{Im} z > 0\}$ with the **hyperbolic metric**

$$
g = \frac{dx^2 + dy^2}{y^2}, \qquad z = x + iy, \quad y > 0 .
$$

The pair $(\mathbb{H}^2, g)$ is the **Poincaré upper half-plane model** of the hyperbolic plane. In $n$ dimensions the **upper half-space model** is $\mathbb{H}^n = \{(x_1, \ldots, x_n) : x_n > 0\}$ with the metric

$$
g = \frac{dx_1^2 + \cdots + dx_n^2}{x_n^2} .
$$

**Proposition.** The metric $g$ is positive definite and conformal to the Euclidean metric: it is $y^{-2}$ times the Euclidean metric at the point $z = x + iy$. Its coefficients are $g_{11} = g_{22} = y^{-2}$, $g_{12} = 0$, and its determinant is $y^{-4}$.

**Theorem.** The upper half-plane model has constant sectional curvature $-1$; its geodesics are the vertical lines $x = \mathrm{const}$ and the semicircles with centres on the real axis and radius $r > 0$, and its isometries are the **Möbius transformations**

$$
z \longmapsto \frac{az + b}{cz + d}, \qquad a, b, c, d \in \mathbb{R}, \quad ad - bc > 0,
$$

together with the reflection $z \mapsto -\bar z$. The orientation-preserving isometries form the group $PSL(2, \mathbb{R}) = SL(2, \mathbb{R})/\{\pm I\}$.

**Proof sketch.** The Christoffel symbols of $g$ give $\Gamma^1_{11} = \Gamma^1_{22} = \Gamma^2_{12} = 0$, $\Gamma^1_{12} = -1/y$, $\Gamma^2_{11} = 1/y$, $\Gamma^2_{22} = -1/y$, and the geodesic equation reduces to the statement that the curves are the lines and semicircles orthogonal to the boundary; the curvature is computed from the second derivatives of the metric and is $-1$. A Möbius transformation with real coefficients preserves the upper half-plane, and a direct computation gives

$$
\frac{|f'(z)|}{\operatorname{Im} f(z)} = \frac{1}{\operatorname{Im} z},
$$

which is exactly the conformality factor of $g$, so $f^*g = g$; the real Möbius transformations and the reflection generate all the isometries, since an isometry is determined by the image of a frame.

**Definition.** The **cross-ratio** of four distinct real numbers or boundary points $z_1, z_2, z_3, z_4$ is

$$
[z_1, z_2; z_3, z_4] = \frac{(z_1 - z_3)(z_2 - z_4)}{(z_1 - z_4)(z_2 - z_3)},
$$

invariant under Möbius transformations.

**Theorem (distance formula).** For $z, w \in \mathbb{H}^2$,

$$
\cosh d(z, w) = 1 + \frac{|z - w|^2}{2\operatorname{Im} z\,\operatorname{Im} w},
$$

and for points on the imaginary axis $z = it$, $w = is$,

$$
d(it, is) = |\log(t/s)| .
$$

**Proof sketch.** The distance along the imaginary axis is $\int_s^t dy/y = \log(t/s)$ for $t > s$; the group $PSL(2, \mathbb{R})$ acts transitively on pairs of points at a given distance, and any two points are carried to two points of a vertical geodesic, which gives the general formula; the displayed identity is checked directly.

**Corollary.** The hyperbolic metric is complete and the hyperbolic distance is unbounded, so $\mathbb{H}^2$ has infinite diameter. Its area element is $dA = dx\,dy/y^2$, and the area of the region $\{x_0 \leq x \leq x_1,\ y \geq y_0\}$ is $(x_1 - x_0)/y_0$, finite in the horizontal direction and infinite in the vertical.

### The Poincaré Disk Model

**Definition.** The **Poincaré disk** is the unit disk $\mathbb{D}^2 = \{z \in \mathbb{C} : |z| < 1\}$ with the metric

$$
g_{\mathbb{D}} = \frac{4\,|dz|^2}{(1 - |z|^2)^2}.
$$

**Theorem.** The **Cayley transform**

$$
C(z) = \frac{z - i}{z + i}
$$

is a biholomorphic isometry from the upper half-plane model onto the Poincaré disk, with inverse $C^{-1}(w) = i(1 + w)/(1 - w)$.

**Proof.** The Cayley transform is a Möbius transformation carrying the real axis to the unit circle and the upper half-plane to the disk; the identity $|C'(z)|/(1 - |C(z)|^2) = 1/(2\operatorname{Im} z)$ gives $C^*(g_{\mathbb{D}}) = g$.

**Proposition (disk distance).** For $z, w$ in the disk,

$$
\cosh d(z, w) = 1 + \frac{2|z - w|^2}{(1 - |z|^2)(1 - |w|^2)} .
$$

**Corollary (geodesics in the disk).** The geodesics of the Poincaré disk are the diameters and the arcs of circles orthogonal to the boundary circle $|z| = 1$.

### The Hyperboloid and Beltrami–Klein Models

**Definition.** The **hyperboloid model** of $\mathbb{H}^n$ is the quadric

$$
\mathcal{H}^n = \{x \in \mathbb{R}^{n+1} : \langle x, x\rangle_{1,n} = 1,\ x_0 > 0\}
$$

in the pseudo-Euclidean space $\mathbb{R}^{1,n}$ with $\langle x, x\rangle_{1,n} = x_0^2 - x_1^2 - \cdots - x_n^2$, for the radius of curvature $1$; for general $R$ the quadric is $\langle x, x\rangle_{1,n} = R^2$. Its points are spacelike, and the positive direction of the form is the normal rather than a tangent direction, so the ambient form is negative definite on $x^\perp$ and its negative restricts to $\mathcal{H}^n$ as a Riemannian metric, complete of constant curvature $-1/R^2$. The companion quadric of the same pencil, $\langle x, x\rangle_{1,n} = -R^2$, is the one-sheeted hyperboloid, whose points are timelike and whose induced metric is indefinite of signature $(1, n-1)$; that member of the family is the Lorentzian hyperboloid $H^{1,n-1}$ of *Pseudo-Riemannian and Lorentzian Geometry*, of which $\mathcal{H}^n$ is the Riemannian counterpart.

**Proposition.** The hyperboloid model is complete with constant curvature $-1$, its isometry group is the group $O(1, n)^+$ of pseudo-orthogonal transformations preserving the upper sheet, and the orthogonal projection to the plane $x_0 = 1$ along the origin gives the **Beltrami–Klein model**, in which geodesics are the chords of the unit ball.

**Proof sketch.** The tangent space at $x \in \mathcal{H}^n$ is $x^\perp$, on which the ambient form is negative definite because the only positive direction of the form, the $x_0$ axis, is represented at $x$ by the normal $x$ itself and not by a tangent vector; the negative of the restriction is the Riemannian metric, and the Gauss equation for the quadric gives $K = -1$. The group $O(1,n)$ acts transitively by isometries and the stabiliser of a point is $O(n)$.

**Theorem.** The four models are isometric: the upper half-plane, the Poincaré disk, the hyperboloid and the Beltrami–Klein model describe the same connected, complete, simply connected Riemannian manifold of constant sectional curvature $-1$, denoted $\mathbb{H}^n$.

**Proof.** Each is complete, simply connected and of constant curvature $-1$, so each is isometric to the classification model of *Riemannian Geometry*; the explicit maps are the Cayley transform, the stereographic projection to the disk, and the projection from the hyperboloid.

**Weierstrass coordinates.** The quadric may be parametrised by the geodesic polar coordinates of the model itself. Let the hyperboloid have radius of curvature $R$, let $\rho$ be the geodesic distance of a point from the vertex $v = (R, 0, \ldots 0)$, and let $l = (l_1, \ldots, l_n)$ be the unit vector of $\mathbb{R}^n$ that is the direction of the point. The **Weierstrass coordinates** of the point are

$$
X_0 = R\cosh\frac{\rho}{R},\qquad X_i = R\sinh\frac{\rho}{R}\,l_i,\qquad \sum_{i=1}^n l_i^2 = 1 ,
$$

and they satisfy $\langle X, X\rangle_{1,n} = R^2$ identically, so they parametrise the hyperboloid by the pair $(\rho, l)$. They are the coordinates in which the quadric is written without the embedding; the point $X$ is the ambient vector and not a chart, and the two are related by the normalisation that fixes the value of the form.

**Proposition.** In Weierstrass coordinates the induced metric of the hyperboloid is

$$
ds^2 = d\rho^2 + R^2\sinh^2\frac{\rho}{R}\;d\Omega_{n-1}^2 ,
$$

where $d\Omega_{n-1}^2$ is the round metric of the unit sphere on the direction $l$.

**Proof.** Since $\sum_i l_i^2 = 1$ the direction satisfies $l\cdot dl = 0$ and $|dl|^2 = d\Omega_{n-1}^2$. Differentiating, $dX_0 = \sinh(\rho/R)\,d\rho$ and $dX_i = \cosh(\rho/R)\,l_i\,d\rho + R\sinh(\rho/R)\,dl_i$, whence

$$
-\langle dX, dX\rangle_{1,n} = \sum_i dX_i^2 - dX_0^2 = \Bigl(\cosh^2\frac{\rho}{R} - \sinh^2\frac{\rho}{R}\Bigr) d\rho^2 + R^2\sinh^2\frac{\rho}{R}\,|dl|^2 ,
$$

which is the displayed metric.

**Remark (the interchange $R \mapsto iR$).** The same construction on the sphere of radius $R$ has $X_0 = R\cos(\rho/R)$, $X_i = R\sin(\rho/R)\,l_i$ and metric $d\rho^2 + R^2\sin^2(\rho/R)\,d\Omega_{n-1}^2$. The two parametrisations and the two metrics are interchanged by $\rho/R \mapsto i\rho/R$, that is by $R \mapsto iR$ at fixed $\rho$, the hyperbolic functions becoming circular ones; the interchange is the algebraic expression of the change of sign of the ambient form. Both metrics expand as $d\rho^2 + \rho^2\,d\Omega_{n-1}^2$ to leading order, with the first correction of opposite sign,

$$
R^2\sinh^2\frac{\rho}{R} = \rho^2 + \frac{\rho^4}{3R^2} + \cdots , \qquad R^2\sin^2\frac{\rho}{R} = \rho^2 - \frac{\rho^4}{3R^2} + \cdots ,
$$

so small geodesic balls recover the Euclidean metric in both geometries and the deviation is measured by $\rho^2/R^2$, with the curvature $-1/R^2$ and $+1/R^2$ as its coefficient.

**The Cayley–Klein metric.** The projection of the upper sheet to the plane $x_0 = R$ along the rays through the origin is the **Beltrami–Klein model**, carried by the open ball $B^n_R$ of radius $R$, in the coordinates $u_i = R\,x_i/x_0$. A geodesic of the hyperboloid is the intersection with a two-plane through the origin, and the projection carries that plane to a line, so the image of the geodesic is a chord of the ball and the geodesics of the model are the chords. The metric that makes the chords geodesics is the **Cayley–Klein metric**, defined projectively by the boundary.

**Definition.** Let $p, q$ be distinct points of the ball $B^n_R$, and let the line through them meet the boundary sphere in the two points $a, b$, ordered so that $a, p, q, b$ occur in this order. The **Cayley–Klein distance** is

$$
d(p, q) = \frac{R}{2}\left|\log\frac{|pa|\,|qb|}{|pb|\,|qa|}\right| .
$$

Equivalently, in the coordinates of the ball,

$$
\cosh\frac{d(p,q)}{R} = \frac{R^2 - p\cdot q}{\sqrt{(R^2 - |p|^2)(R^2 - |q|^2)}} .
$$

**Proposition.** The Cayley–Klein distance is the distance of the hyperboloid: for the points $x, y$ of the sheet of radius $R$ projecting to $p, q$,

$$
\cosh\frac{d(p,q)}{R} = \frac{\langle x, y\rangle_{1,n}}{R^2} .
$$

**Proof.** Write $u_i = R\,x_i/x_0$. Then $|u|^2 = R^2(x_0^2 - R^2)/x_0^2$ because $\langle x,x\rangle_{1,n} = R^2$, so

$$
R^2 - |u|^2 = \frac{R^4}{x_0^2}, \qquad R^2 - u\cdot v = \frac{R^2\,\langle x, y\rangle_{1,n}}{x_0y_0} ,
$$

and substituting the two into the right-hand side of the disc formula gives $\langle x, y\rangle_{1,n}/R^2$. The right-hand side is $\ge 1$ by the reversed Cauchy inequality, with equality only for $p = q$, so it is a distance.

**Remark.** The cross-ratio and the disc formula are the two faces of the same quantity, and the identification of the cross-ratio form with the metric is the classical **Cayley–Klein construction**: the boundary sphere is the absolute, and a metric is obtained from the cross-ratio of the points with the absolute. The form is the projective model of hyperbolic geometry, since the geodesics are the straight chords and the isometries are the projective transformations that preserve the absolute; it is the model in which hyperbolic geometry is closest to the Euclidean in appearance and the model in which the geodesics are the easiest to draw, the price being that the metric is not the Euclidean metric of the ball and that the angles are not the Euclidean angles.

## Geodesics, Ideal Points and Trigonometry

### The Boundary at Infinity

**Definition.** The **boundary at infinity** of the upper half-plane model is $\partial\mathbb{H}^2 = \mathbb{R} \cup \{\infty\}$, and of the disk model the unit circle. A **geodesic** has two distinct endpoints on the boundary, and two geodesics are asymptotic if they have a common endpoint. The boundary is the set of equivalence classes of geodesic rays that remain at bounded distance, and it carries a natural circle topology; it is the **conformal boundary** of the model.

**Definition.** An **ideal point** is a point of the boundary, and an **ideal triangle** is a triangle all of whose vertices are ideal; an **ideal polygon** is defined similarly. All ideal triangles in $\mathbb{H}^2$ are congruent, because any three distinct boundary points can be carried to any other three by a Möbius transformation.

**Proposition (area of an ideal triangle).** Every ideal triangle has area $\pi$.

**Proof.** By the transitivity of $PSL(2, \mathbb{R})$ on triples of boundary points, it suffices to treat the ideal triangle with vertices $-1, 1, \infty$. Its sides are the semicircle $x^2 + y^2 = 1$ (the geodesic from $-1$ to $1$) and the vertical lines $x = \pm 1$, so it is the region

$$
D = \{(x, y) : -1 < x < 1,\ y > \sqrt{1 - x^2}\}.
$$

Its hyperbolic area is the integral of the area form $dA = y^{-2}dx\,dy$ over $D$:

$$
\int_D \frac{dx\,dy}{y^2} = \int_{-1}^{1}\left(\int_{\sqrt{1-x^2}}^{\infty}\frac{dy}{y^2}\right) dx = \int_{-1}^{1}\frac{dx}{\sqrt{1-x^2}} = \bigl[\arcsin x\bigr]_{-1}^{1} = \pi .
$$

The computation is the elementary integral of the $2$-form $y^{-2}dx\wedge dy$ over a region of $\mathbb{H}^2$, which is the top-form integral read on an oriented surface patch. The agreement with the angle-sum formula below, in which all three angles of an ideal triangle are zero, is the two-dimensional Gauss–Bonnet theorem.

### Hyperbolic Trigonometry

**Theorem (angle sum and area).** For a hyperbolic triangle with angles $A, B, C$ and area $\Delta$,

$$
A + B + C = \pi - \Delta, \qquad \text{so} \qquad \Delta = \pi - (A + B + C).
$$

**Proof.** This is the Gauss–Bonnet theorem of *Riemannian Geometry* for a geodesic triangle in a surface of curvature $-1$: the boundary term contributes the sum of the exterior angles and the angle sum appears with the sign appropriate to negative curvature.

**Corollary.** The angle sum of a hyperbolic triangle is less than $\pi$, and every hyperbolic triangle has area less than $\pi$; the area is the **hyperbolic defect** $\pi - (A+B+C)$.

**Theorem (hyperbolic law of cosines).** For a hyperbolic triangle with sides $a, b, c$ and opposite angles $A, B, C$,

$$
\cosh c = \cosh a\cosh b - \sinh a\sinh b\cos C,
$$

and cyclically.

**Theorem (hyperbolic law of sines).**

$$
\frac{\sinh a}{\sin A} = \frac{\sinh b}{\sin B} = \frac{\sinh c}{\sin C}.
$$

**Theorem (right hyperbolic triangles).** If $C = \pi/2$ then

$$
\cosh c = \cosh a\cosh b, \qquad \cos A = \frac{\cosh a\,\sin B}{\cosh b}, \qquad \sin A = \frac{\sinh a}{\sinh c}.
$$

**Proof sketch (of the laws).** The laws are proved by the same two-vector computation as in the spherical case, with the positive definite inner product of the hyperboloid replaced by the indefinite form $\langle\cdot,\cdot\rangle_{1,2}$ of $\mathbb{R}^{1,2}$; the sign change in the form changes $\cos$ to $\cosh$ and $\sin$ to $\sinh$ throughout, which is the structural reason the two trigonometries differ only in the signs and the functions.

**Corollary (the Euclidean limit).** For small sides, $\cosh x \to 1 + x^2/2$ and $\sinh x \to x$, and the hyperbolic law of cosines becomes the Euclidean law $c^2 = a^2 + b^2 - 2ab\cos C$; the hyperbolic Pythagorean theorem becomes $c^2 = a^2 + b^2$. As in the spherical case, the Euclidean theory is the flat limit, and the deviation from it is measured by the area of the triangle.

### The Angle of Parallelism

**Definition.** Let $P$ be a point at hyperbolic distance $d$ from a geodesic line $\ell$, and let $Q$ be the foot of the perpendicular from $P$ to $\ell$. The **angle of parallelism** $\Pi(d)$ is the angle at $P$ between the perpendicular $PQ$ and either of the two geodesic rays from $P$ asymptotic to $\ell$.

**Theorem (Lobachevsky).** The angle of parallelism satisfies

$$
\tan\frac{\Pi(d)}{2} = e^{-d}, \qquad \text{equivalently} \qquad \cos\Pi(d) = \tanh d .
$$

**Proof sketch.** In the upper half-plane place $\ell$ as the imaginary axis and $P = (t, u)$; the asymptotic rays from $P$ are the geodesics through $P$ with endpoint $0$ and $\infty$, and the angle between them is computed from the hyperbolic right triangle with vertices $0$, $P$ and the foot; the right-triangle formulae give the displayed relation.

**Corollary.** As $d \to 0$ the angle of parallelism tends to $\pi/2$, and as $d \to \infty$ it decays exponentially to $0$: at small distances hyperbolic geometry resembles the Euclidean, and at large distances the departure is exponential. For every angle in $(0, \pi/2)$ there is a unique distance realising it, and for every point and every line there are exactly two rays from the point asymptotic to the line; the lines through the point that meet the line are the finitely many directions between the two asymptotic rays, and the lines that do not meet it fill an open set of directions, so there are infinitely many parallels.

## The Isometry Group and Discrete Groups

### The Two-Dimensional Case

**Theorem.** The orientation-preserving isometry group of $\mathbb{H}^2$ is $PSL(2, \mathbb{R})$, acting by Möbius transformations; the full isometry group is $PSL(2, \mathbb{R}) \rtimes \mathbb{Z}/2$, where the $\mathbb{Z}/2$ acts by $z \mapsto -\bar z$. The action is transitive on points, and the stabiliser of a point is the compact group $SO(2)$, so $\mathbb{H}^2 \cong PSL(2, \mathbb{R})/SO(2)$ is a homogeneous space.

**Proof sketch.** The group $PSL(2, \mathbb{R})$ acts transitively on the boundary $\mathbb{R} \cup \{\infty\}$ and, given three boundary points, is determined; it acts transitively on pairs of boundary points and hence on geodesics; and the stabiliser of $i$ is the rotation group generated by $z \mapsto -1/z$ and the translations by the circle action, which is $SO(2)$.

**Definition.** A Möbius transformation $f \in PSL(2, \mathbb{R})$, other than the identity, is **elliptic** if it has a fixed point in $\mathbb{H}^2$, **parabolic** if it has exactly one fixed point on the boundary, and **hyperbolic** if it has two fixed points on the boundary and none in $\mathbb{H}^2$. The three cases are distinguished by the absolute value of the trace: $|\operatorname{tr}| < 2$ elliptic, $= 2$ parabolic, $> 2$ hyperbolic.

**Proposition.** A hyperbolic element acts as a translation along its axis, the geodesic joining its two boundary fixed points, with a well-defined **translation length**; a parabolic element acts as a limit rotation about its single boundary fixed point; an elliptic element acts as a rotation about its fixed point in $\mathbb{H}^2$.

**Proof sketch.** Normalise the element by conjugacy: a hyperbolic element with fixed points $0, \infty$ is $z \mapsto \lambda z$ with $\lambda > 1$, a parabolic element with fixed point $\infty$ is $z \mapsto z + t$, and an elliptic element with fixed point $i$ is a rotation.

**Example (the hyperbolic rotation and the algebra $\mathbb{D}$).** The hyperbolic element $z \mapsto \lambda z$ acts on the imaginary axis by $it \mapsto i\lambda t$, which is $d \mapsto d + \log\lambda$ in the distance; its infinitesimal generator is the **hyperbolic rotation** or **Lorentz boost** of the split-complex algebra $\mathbb{D}$ of *The Three Two-Dimensional Algebras and the Three Kinds of Rotation*, in which $\omega^2 = +1$. The trace classification $\operatorname{tr}^2 - 4 \gtrless 0$ is the same sign trichotomy as the quadratic form $x^2 - y^2$ on the algebra, and it is the two-dimensional case of the correspondence between the three model geometries and the three real two-dimensional algebras.

### The Three-Dimensional Case

**Theorem.** The orientation-preserving isometry group of $\mathbb{H}^3$, in the upper half-space model with coordinates $(z, t) \in \mathbb{C} \times \mathbb{R}_{>0}$, is $PSL(2, \mathbb{C})$, acting on the boundary $\mathbb{C} \cup \{\infty\} = S^2$ by Möbius transformations and extended to the interior by the **Poincaré extension**. The full isometry group is $PSL(2, \mathbb{C}) \rtimes \mathbb{Z}/2$.

**Proof sketch.** An orientation-preserving isometry of $\mathbb{H}^3$ extends to a conformal map of the boundary sphere, and the conformal maps of $S^2$ are the Möbius transformations $PSL(2, \mathbb{C})$; conversely each Möbius transformation extends uniquely to an isometry of the hyperbolic three-space by the Poincaré extension.

**Remark.** In dimension two the boundary is the circle with its rotation group $PSL(2, \mathbb{R})$, and in dimension three the boundary is the Riemann sphere with its Möbius group $PSL(2, \mathbb{C})$; in both cases the isometry group of hyperbolic space is the Möbius group of the boundary. This is the geometric form of the fact that the hyperbolic isometries are exactly the conformal automorphisms of the boundary, and it is the reason hyperbolic geometry is the natural home of the theory of Kleinian groups.

### Fuchsian and Kleinian Groups

**Definition.** A **Fuchsian group** is a discrete subgroup $\Gamma \leq PSL(2, \mathbb{R})$, and a **Kleinian group** is a discrete subgroup of $PSL(2, \mathbb{C})$. A **fundamental domain** for a discrete group $\Gamma$ acting on $\mathbb{H}^n$ is an open set $D$ with $\gamma D \cap D = \emptyset$ for every $\gamma \neq 1$ and $\bigcup_{\gamma \in \Gamma} \overline{\gamma D} = \mathbb{H}^n$.

**Theorem.** A discrete subgroup $\Gamma \leq \operatorname{Isom}(\mathbb{H}^n)$ acting freely and properly discontinuously on $\mathbb{H}^n$ has a quotient $\mathbb{H}^n/\Gamma$ that is a complete hyperbolic manifold; conversely every complete hyperbolic manifold arises in this way, with $\Gamma$ isomorphic to the fundamental group. A Fuchsian group with a finite-area fundamental domain gives a hyperbolic surface, whose area is $2\pi|\chi(\Sigma)|$ by Gauss–Bonnet.

**Proof sketch.** The quotient of a simply connected complete manifold by a free properly discontinuous isometric action is complete and hyperbolic; conversely the universal cover of a complete hyperbolic manifold is complete, simply connected and of curvature $-1$, hence isometric to $\mathbb{H}^n$ by Cartan's theorem, and the deck transformations are isometries. The area statement is the Gauss–Bonnet theorem for a compact surface of curvature $-1$.

**Theorem (Mostow rigidity).** Let $M$ and $N$ be complete finite-volume hyperbolic manifolds of dimension $n \geq 3$. If $\pi_1(M) \cong \pi_1(N)$ then $M$ and $N$ are isometric. Consequently the hyperbolic structure of a finite-volume hyperbolic manifold of dimension at least three is unique, and the deformation space is a single point.

**Proof sketch.** The isomorphism of fundamental groups is realised by a boundary map of the universal covers, equivariant for the two actions by the Mostow extension; the boundary map is conformal, hence Möbius, and therefore extends to an isometry.

**Remark.** Mostow rigidity fails in dimension two, where the deformation space of a hyperbolic surface is the Teichmüller space of positive dimension. The two-dimensional theory — the Teichmüller space, the mapping class group and its action, the moduli of complex structures, and the Bers and Fenchel–Nielsen coordinates — is not developed here. What belongs to this article is the geometry and the isometry group; the deformation theory of the discrete subgroups and of the quotient surfaces is not.

## Hyperbolic Space Forms and the Trichotomy

**Definition.** A **hyperbolic space form** is a complete connected Riemannian manifold of constant sectional curvature $-1$; equivalently, by the space-form theorem, a quotient $\mathbb{H}^n/\Gamma$ of the model by a discrete group of isometries acting freely and properly discontinuously.

**Theorem.** Every complete hyperbolic manifold is $\mathbb{H}^n/\Gamma$ for a discrete group $\Gamma \leq \operatorname{Isom}(\mathbb{H}^n)$ acting freely and properly discontinuously; the manifold is compact or of finite volume when the fundamental domain is, and its fundamental group is $\Gamma$.

**Corollary (surfaces).** Every compact orientable surface of genus $g \geq 2$ admits a hyperbolic structure; the area is $-2\pi\chi(\Sigma) = 4\pi(g-1)$ and the structure is not unique — the Teichmüller space of a genus-$g$ surface has real dimension $6g - 6$.

**Corollary (the trichotomy).** The complete connected constant-curvature geometries are exactly the spherical case of quotients of $S^n$ (finite fundamental group), the Euclidean case of quotients of $\mathbb{R}^n$ (virtually abelian fundamental group, by the Bieberbach theorems), and the hyperbolic case of quotients of $\mathbb{H}^n$ (with fundamental group containing a free group of rank two whenever the quotient is non-compact of finite volume). The three differ by the sign of the curvature, by the parallel postulate, and by the growth of the fundamental group; the comparison is not covered here.

## Summary

Hyperbolic $n$-space is the complete simply connected Riemannian manifold of constant sectional curvature $-1$. It is realised by four isometric models: the upper half-plane or half-space with the metric $y^{-2}\sum dx_i^2$, the Poincaré disk with the metric $4|dz|^2/(1-|z|^2)^2$, the hyperboloid $\{x : \langle x,x\rangle_{1,n} = 1,\ x_0>0\}$ in pseudo-Euclidean space, and its Beltrami–Klein projective image. The geodesics are the lines and semicircles orthogonal to the boundary in the half-plane model, the diameters and orthogonal arcs in the disk, and the chords in the Beltrami–Klein model; the distance is given by the cross-ratio and by the formula $\cosh d(z,w) = 1 + |z-w|^2/(2\operatorname{Im}z\operatorname{Im}w)$.

The hyperboloid of radius $R$ is parametrised by its **Weierstrass coordinates** $X_0 = R\cosh(\rho/R)$, $X_i = R\sinh(\rho/R)l_i$, in which the metric reads $d\rho^2 + R^2\sinh^2(\rho/R)\,d\Omega_{n-1}^2$ and the curvature appears as the sign of the $\rho^4/3R^2$ correction to the Euclidean metric of a small geodesic ball; the spherical counterpart follows by $R \mapsto iR$, the hyperbolic functions becoming circular. The Beltrami–Klein ball carries the **Cayley–Klein metric**, whose distance is the cross-ratio of the two points with the two boundary points of their chord, equivalently $\cosh(d/R) = (R^2 - p\cdot q)/\sqrt{(R^2-|p|^2)(R^2-|q|^2)}$, and this is the hyperbolic distance because it equals $\langle x,y\rangle_{1,n}/R^2$ for the two points of the hyperboloid that project to $p$ and $q$.

The angles of a hyperbolic triangle sum to $\pi$ minus its area, the area is the defect, and the trigonometric laws are the spherical laws with the circular functions replaced by the hyperbolic ones: $\cosh c = \cosh a\cosh b - \sinh a\sinh b\cos C$, and $\sinh a/\sin A$ is constant. Small triangles recover Euclidean trigonometry, the deviation being measured by the area. The angle of parallelism satisfies $\tan(\Pi(d)/2) = e^{-d}$, decaying exponentially, so through a point outside a line there are infinitely many parallels, two asymptotic rays and an open set of directions between them.

The orientation-preserving isometry group is $PSL(2, \mathbb{R})$ in dimension two and $PSL(2, \mathbb{C})$ in dimension three, acting on the half-space by Möbius transformations and their Poincaré extension; the elements are classified as elliptic, parabolic and hyperbolic by the trace, corresponding to the sign of the quadratic form of the algebra $\mathbb{D}$ and to the three kinds of two-dimensional rotation. The discrete subgroups — the Fuchsian and Kleinian groups — produce complete hyperbolic manifolds as quotients, and the hyperbolic area of a compact surface is $4\pi(g-1)$. Mostow rigidity makes the hyperbolic structure of a finite-volume manifold of dimension at least three unique, while in dimension two the structures deform, and that deformation is the Teichmüller theory of the sibling articles. Hyperbolic geometry completes the trichotomy of the model geometries and is the geometry in which the parallel postulate fails in the direction of infinitely many parallels.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}^n$ | Hyperbolic $n$-space; the complete simply connected model of curvature $-1$ |
| $g = y^{-2}\sum_i dx_i^2$ | Hyperbolic metric in the upper half-plane/half-space model |
| $g_{\mathbb{D}} = 4|dz|^2/(1-|z|^2)^2$ | Hyperbolic metric in the Poincaré disk model |
| $C(z) = (z-i)/(z+i)$ | Cayley transform, upper half-plane $\to$ disk |
| $\cosh d(z,w) = 1 + |z-w|^2/(2\operatorname{Im}z\operatorname{Im}w)$ | Distance in the upper half-plane model |
| $[z_1,z_2;z_3,z_4]$ | Cross-ratio; Möbius invariant, encodes distance and endpoints |
| $\partial\mathbb{H}^n$ | Boundary at infinity; $\mathbb{R}\cup\{\infty\}$ for $n=2$, $\mathbb{C}\cup\{\infty\}$ for $n=3$ |
| Ideal point, ideal triangle | Boundary point; triangle with ideal vertices, of area $\pi$ |
| $\Delta = \pi - (A+B+C)$ | Hyperbolic area via the defect |
| $\cosh c = \cosh a\cosh b - \sinh a\sinh b\cos C$ | Hyperbolic law of cosines |
| $\sinh a/\sin A = \sinh b/\sin B = \sinh c/\sin C$ | Hyperbolic law of sines |
| $\Pi(d)$, $\tan(\Pi(d)/2) = e^{-d}$ | Angle of parallelism |
| $PSL(2,\mathbb{R})$, $PSL(2,\mathbb{C})$ | Orientation-preserving isometry groups of $\mathbb{H}^2$ and $\mathbb{H}^3$ |
| Elliptic, parabolic, hyperbolic element | $|\operatorname{tr}| < 2$, $=2$, $>2$; rotation, limit rotation, translation |
| Fuchsian, Kleinian group | Discrete subgroup of $PSL(2,\mathbb{R})$, of $PSL(2,\mathbb{C})$ |
| $\mathbb{H}^n/\Gamma$ | Complete hyperbolic manifold; $\Gamma \cong \pi_1$ |
| Mostow rigidity | $\dim \geq 3$, finite volume: homotopy equivalent implies isometric |
| $\mathcal{H}^n$ | Hyperboloid model: the quadric $\langle x,x\rangle_{1,n}=1$, $x_0>0$, in $\mathbb{R}^{1,n}$ |
| $X_0 = R\cosh(\rho/R)$, $X_i = R\sinh(\rho/R)l_i$ | Weierstrass coordinates on the hyperboloid of radius $R$ |
| $ds^2 = d\rho^2 + R^2\sinh^2(\rho/R)\,d\Omega_{n-1}^2$ | Hyperboloid metric in Weierstrass coordinates |
| $R \mapsto iR$ | Interchange of the hyperbolic and the spherical parametrisation and metric |
| $B^n_R$ | Beltrami–Klein ball of radius $R$, the projective model |
| $d(p,q) = \frac{R}{2}\left\lvert\log\frac{\lvert pa\rvert\,\lvert qb\rvert}{\lvert pb\rvert\,\lvert qa\rvert}\right\rvert$ | Cayley–Klein distance, as a cross-ratio with the boundary points $a,b$ |
| $\cosh\frac{d(p,q)}{R} = \frac{R^2 - p\cdot q}{\sqrt{(R^2-\lvert p\rvert^2)(R^2-\lvert q\rvert^2)}}$ | Cayley–Klein distance in the coordinates of the ball |
| $\cosh\frac{d}{R} = \frac{\langle x,y\rangle_{1,n}}{R^2}$ | The same distance on the hyperboloid |





## Further Reading

- John G. Ratcliffe, *Foundations of Hyperbolic Manifolds*, 2nd ed. (Springer, 2006), for the models, the isometry groups and the space forms.
- John Stillwell, *Sources of Hyperbolic Geometry* (American Mathematical Society and London Mathematical Society, 1996), for the original papers of Beltrami and Klein with commentary, and for the Cayley–Klein construction.
- William F. Reynolds, "Hyperbolic geometry on a hyperboloid", *American Mathematical Monthly* **100** (1993), 442–455, for the Weierstrass coordinates and the hyperboloid model.
- D. M. Y. Sommerville, *The Elements of Non-Euclidean Geometry* (Bell, 1914; Dover, 2005), for the Cayley–Klein metric and the Weierstrass coordinates in the classical notation.
- James W. Anderson, *Hyperbolic Geometry*, 2nd ed. (Springer, 2005), for an elementary development of the models and trigonometry.
- Alan F. Beardon, *The Geometry of Discrete Groups* (Springer, 1983), for Möbius transformations, Fuchsian groups and their classification.
- D. B. A. Epstein and A. Marden, "Convex hulls in hyperbolic space, a theorem of Sullivan, and measured pleated surfaces", in *Analytical and Geometric Aspects of Hyperbolic Space* (Cambridge University Press, 1987), for the boundary theory.
- William P. Thurston, *Three-Dimensional Geometry and Topology, Volume I* (Princeton University Press, 1997), for hyperbolic three-manifolds and their geometry.
- G. D. Mostow, *Strong Rigidity of Locally Symmetric Spaces* (Princeton University Press, 1973), for the rigidity theorem.
- Peter Buser, *Geometry and Spectra of Compact Riemann Surfaces* (Birkhäuser, 1992), for the hyperbolic geometry of surfaces and its use in Teichmüller theory.
