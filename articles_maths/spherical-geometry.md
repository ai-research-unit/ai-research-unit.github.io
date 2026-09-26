
# __Spherical Geometry__

## Introduction

Spherical geometry is the geometry of the unit sphere with the distance measured along the surface. It is the model geometry of constant positive curvature: the round sphere of radius $R$ has sectional curvature $K = 1/R^2$ on every plane, its geodesics are the great circles, and its triangles have angle sum greater than $\pi$, with the excess equal to the area. It is one of the three model geometries of *Curvature and Geodesics* — the elliptic member of the trichotomy — and its two-dimensional geometry is the geometry of the algebra $\mathbb{C}$ with the elliptic rotation group $SO(2)$, the case $\omega^2 = -1$ of *The Three Two-Dimensional Algebras and the Three Kinds of Rotation*.

Spherical geometry differs from Euclidean geometry in a way that changes its logical character: any two great circles meet, so there are no parallel lines at all, and the parallel postulate fails in the direction of "no parallels" rather than of "too many". This makes spherical geometry a geometry of **antipodal pairs**: every point has a unique antipode at the maximum distance $\pi R$, and each pair of antipodal points is joined by infinitely many minimising geodesics. The quotient of the sphere by the antipodal map repairs this defect and gives **elliptic geometry**, the geometry of the real projective plane, which is the genuinely two-dimensional positive-curvature model. This article treats both.

The article first defines the round sphere as a Riemannian manifold and computes its metric, its distance and its geodesics. It then develops spherical trigonometry — the spherical law of cosines, the law of sines, the polar triangle, Girard's theorem on the area of a spherical triangle, and the right-triangle formulae — and relates them to the Euclidean theorems they generalise, with the Euclidean ones recovered as the limit of small triangles. It treats the isometry group $O(n+1)$ and the classification of its finite subgroups, which is the classification of the finite groups of rotations of the sphere and the source of the exceptional groups $A_4$, $S_4$, $A_5$. It develops the elliptic quotient, the three-dimensional sphere and the Hopf fibration, and the spherical space forms, which are the complete constant-curvature manifolds of positive curvature.

The article assumes *Smooth Manifolds and Differential Geometry* for the sphere as a submanifold and the induced metric; *Curvature and Geodesics* and *Riemannian Geometry* for geodesics, curvature and the classification of the space forms; *Euclidean Geometry* for the comparison and the crystallographic restriction; *Groups* and *Group Actions and Structure* for the finite group theory; *Matrix Groups and Classical Groups* for $O(n)$ and $SU(2)$; *The Three Two-Dimensional Algebras and the Three Kinds of Rotation* for the elliptic case; andfor the Hopf fibration. The classification of the three-dimensional spherical space forms, the lens spaces, is the subject, and is not developed here. No physics is invoked.

## The Sphere and Its Metric

### The Round Sphere

**Definition.** The **sphere** of radius $R > 0$ in $\mathbb{R}^{n+1}$ is

$$
S^n_R = \{x \in \mathbb{R}^{n+1} : \langle x, x\rangle = R^2\},
$$

and the **round metric** $g_R$ is the restriction of the standard inner product of $\mathbb{R}^{n+1}$ to the tangent spaces of $S^n_R$: for $x \in S^n_R$ and $v, w \in T_xS^n_R$,

$$
g_R(v, w) = \langle v, w\rangle .
$$

The pair $(S^n_R, g_R)$ is a compact Riemannian manifold of dimension $n$; for $R = 1$ it is the unit sphere $S^n$.

**Proposition.** The round metric is well defined (the tangent space at $x$ is the orthogonal complement of $x$), it is positive definite, and the inclusion $S^n_R \hookrightarrow \mathbb{R}^{n+1}$ is an isometric embedding with second fundamental form $\mathrm{II}(X, Y) = -\frac{1}{R}g_R(X, Y)N$ for the outward unit normal $N(x) = x/R$.

**Proof.** Differentiate $\langle x, x\rangle = R^2$ along a curve in the sphere to get $\langle x, x'\rangle = 0$, so $T_xS^n_R = x^\perp$; the restriction of the positive definite form is positive definite. The second fundamental form is computed from $\nabla_XN = X/R$ in the flat connection. $\square$

**Theorem.** The round sphere has constant sectional curvature $K = 1/R^2$; its geodesics are the **great circles**, the intersections $S^n_R \cap P$ with two-dimensional linear subspaces $P$ through the origin, parametrised proportionally to arclength; and its distance is

$$
d_R(x, y) = R\arccos\!\left(\frac{\langle x, y\rangle}{R^2}\right) = R\,\theta(x, y),
$$

where $\theta(x, y) \in [0, \pi]$ is the **central angle** between the two position vectors.

**Proof sketch.** The Gauss equation with the second fundamental form above gives $K = R^{-2}$, since for orthonormal $X, Y$ in the tangent plane, $K = g(\mathrm{II}(X, X), \mathrm{II}(Y, Y)) - |\mathrm{II}(X, Y)|^2 = R^{-2}$. A great circle has constant speed and its acceleration is normal to the sphere, hence tangential acceleration zero, so it is a geodesic; conversely the geodesic equation on the sphere has as its solutions the intersections with the two-planes, by isometry and homogeneity. The distance formula is the polar-coordinate computation: the minimising curve is the shorter arc of the great circle through $x$ and $y$, subtending the central angle $\theta$. $\square$

**Corollary.** The diameter of $S^n_R$ is $\pi R$, attained exactly by antipodal pairs $y = -x$, and two distinct non-antipodal points are joined by exactly one minimising geodesic; antipodal points are joined by infinitely many, each of length $\pi R$. Every geodesic is periodic of length $2\pi R$.

**Corollary (area and volume).** The $n$-volume of $S^n_R$ is

$$
\operatorname{vol}(S^n_R) = \frac{2\pi^{(n+1)/2}}{\Gamma((n+1)/2)}\,R^n ,
$$

in particular $2\pi R$ for the circle $S^1_R$, $4\pi R^2$ for the two-sphere, and $2\pi^2R^3$ for the three-sphere.

The volume formula uses the Gamma function, which is a closed form of an integral; the integral is the elementary one of the elementary functions, and the recurrence is the standard reduction for the surface area of a sphere. The analytic theory of the integral is not developed here.

### The Spherical Isometry Group

**Theorem.** The isometry group of the round sphere is the orthogonal group $O(n+1)$, acting on $S^n_R$ by restriction, and the group of orientation-preserving isometries is $SO(n+1)$. The action is transitive on points and, after a point is fixed, transitive on the orthonormal frames of the tangent space.

**Proof.** Every $A \in O(n+1)$ preserves the ambient inner product and the sphere, so its restriction is an isometry. Conversely an isometry of the sphere extends to a linear map of $\mathbb{R}^{n+1}$ preserving the inner product: an isometry $F$ with $F(x) = y$ composes with an element of $O(n+1)$ to fix $x$; the composition of the differential with the identity shows the extension is linear, and the Myers–Steenrod theorem of *Riemannian Geometry* gives the smoothness. $\square$

**Corollary.** Two points are related by an isometry if and only if they have the same distance from a fixed base point, and the round sphere is a homogeneous space $O(n+1)/O(n)$.

**Definition.** The **isometry group** acts with stabiliser $O(n)$ at a point, and the **round sphere is a symmetric space** in the sense, with the geodesic symmetry at $x$ given by the restriction of the reflection $v \mapsto v - 2\langle v, x\rangle x/R^2$.

## Spherical Trigonometry

### Spherical Triangles and the Angle Sum

**Definition.** A **spherical triangle** is a region of the sphere bounded by three arcs of great circles, each of length less than $\pi R$, together with its three vertices. Its **sides** are the lengths of the arcs, written $a, b, c$ measured as angles at the centre when $R = 1$, and its **angles** $A, B, C$ are the dihedral angles between the planes of the sides.

**Theorem (angle sum and Girard's formula).** For a spherical triangle on the sphere of radius $R$ with angles $A, B, C$ and area $\Delta$,

$$
A + B + C = \pi + \frac{\Delta}{R^2}, \qquad \text{so} \qquad \Delta = R^2(A + B + C - \pi).
$$

**Proof sketch.** The lune bounded by the two great circles through a vertex of angle $A$ has area $2AR^2$, and the three such lunes, together with their antipodal lunes, have total area $4R^2(A+B+C)$. These six lunes cover the sphere with multiplicity one at every point except on the triangle and on its antipodal triangle, where the multiplicity is three; counting the eight triangles cut out by the three great circles therefore gives $4R^2(A+B+C) = 4\pi R^2 + 4\Delta$, which rearranges to the statement. $\square$

**Corollary.** The angle sum of a spherical triangle exceeds $\pi$, by the **spherical excess** $\Delta/R^2$; as $R \to \infty$ with the side lengths held fixed the excess tends to zero and the Euclidean angle sum $\pi$ is recovered.

### The Spherical Laws

**Theorem (spherical law of cosines).** For a spherical triangle on the unit sphere with sides $a, b, c$ and opposite angles $A, B, C$,

$$
\cos c = \cos a\cos b + \sin a\sin b\cos C,
$$

and cyclically in the other five pairings.

**Proof sketch.** Place the vertices as unit vectors $u, v, w$ with angles $a = \arccos\langle v, w\rangle$, $b = \arccos\langle w, u\rangle$, $c = \arccos\langle u, v\rangle$, and let $A, B, C$ be the angles between the tangent vectors along the sides. The decomposition of $w$ in the basis $u$ and an orthonormal vector in the plane $\mathrm{span}(u, w)$ gives $\cos a = \cos b\cos c + \sin b\sin c\cos A$; rearranging the labels gives the law. $\square$

**Theorem (spherical law of sines).** With the same notation,

$$
\frac{\sin a}{\sin A} = \frac{\sin b}{\sin B} = \frac{\sin c}{\sin C}.
$$

**Proof sketch.** Compute the volume of the parallelepiped spanned by $u, v, w$ in two ways, using the spherical law of cosines in one relation and the antisymmetry of the determinant in the other. $\square$

**Theorem (Pythagoras for right spherical triangles).** If $C = \pi/2$ then

$$
\cos c = \cos a\cos b, \qquad \cos A = \frac{\tan b}{\tan c}, \qquad \sin A = \frac{\sin a}{\sin c}.
$$

**Proof.** Put $C = \pi/2$ in the law of cosines for the first formula; the remaining two are the law of sines and the law of cosines applied to the polar triangle. $\square$

**Corollary (the Euclidean limit).** For small sides $a, b, c \ll 1$ the expansions $\cos x = 1 - x^2/2 + O(x^4)$ and $\sin x = x + O(x^3)$ recover the Euclidean law of cosines $c^2 = a^2 + b^2 - 2ab\cos C$ and the Euclidean Pythagorean theorem $c^2 = a^2 + b^2$. Spherical trigonometry therefore contains Euclidean trigonometry as its flat limit, which is the statement that the sphere of large radius approaches the plane.

### Polar Triangles

**Definition.** For a spherical triangle $ABC$ not containing a pair of antipodal vertices, the **polar triangle** $A'B'C'$ has as vertices the poles of the great circles through the opposite sides: $A'$ is the pole of $BC$ on the same side as $A$, and so on.

**Theorem.** The polar triangle has sides $a' = \pi - A$, $b' = \pi - B$, $c' = \pi - C$ and angles $A' = \pi - a$, $B' = \pi - b$, $C' = \pi - c$.

**Proof.** The side $B'C'$ lies on the great circle through the poles of $AC$ and $AB$, which is the polar of $A$; the angle between the planes through the origin associated with the sides is the supplement of the corresponding side of the original triangle. $\square$

**Corollary.** Every theorem about sides has a dual statement about angles, and conversely; this is the **duality** of spherical trigonometry, and it is the reason the laws of cosines and sines come in the two interchanged forms.

## Elliptic Geometry

### The Antipodal Quotient

**Definition.** **Elliptic $n$-space** is the quotient

$$
\mathbb{E}^n = S^n / \{\pm 1\},
$$

where the antipodal map $x \mapsto -x$ acts freely and properly discontinuously; for $n = 2$ it is the real projective plane $\mathbb{RP}^2$, and for general $n$ it is $\mathbb{RP}^n$. The round metric descends to the quotient, because the antipodal map is an isometry, giving the **elliptic metric** on $\mathbb{E}^n$.

**Theorem.** Elliptic $n$-space is a compact Riemannian manifold of constant sectional curvature $+1$, and its distance is

$$
d(\{x, -x\}, \{y, -y\}) = \min\bigl(d_{S^n}(x, y),\, \pi - d_{S^n}(x, y)\bigr),
$$

so that the diameter of elliptic space is $\pi/2$, half that of the sphere.

**Proof.** The quotient metric is well defined by equivariance, and the curvature is unchanged by the local isometry of the covering $S^n \to \mathbb{E}^n$. The distance in the quotient is the minimum over the lifts, and the two lifts of a point are antipodal, so the two candidates are $\theta$ and $\pi - \theta$. $\square$

**Theorem (no parallels).** In elliptic geometry any two lines meet in exactly one point, so the parallel postulate fails with no parallels at all.

**Proof.** A line is the image of a great circle; two great circles meet in an antipodal pair, which is a single point in the quotient. $\square$

**Remark (the two conventions of the elliptic plane).** The sphere itself is sometimes called the **double elliptic plane**, because each pair of antipodal points is a single point of the elliptic plane doubled; this is why the sphere is simply connected while the elliptic plane has fundamental group $\mathbb{Z}/2\mathbb{Z}$. Both are models of positive curvature: the sphere is the simply connected one, and the elliptic plane is the quotient by the antipodal involution, the simplest spherical space form.

### The Finite Rotation Groups

**Definition.** A **finite rotation group** of the sphere $S^2$ is a finite subgroup $\Gamma \leq SO(3)$; its **orbit** of a point $x$ is $\Gamma x$, and the quotient $S^2/\Gamma$ is a spherical orbifold.

**Theorem.** Every finite subgroup of $SO(3)$ is one of: the cyclic group $C_m$ of rotations about a fixed axis; the dihedral group $D_m$ of order $2m$ preserving a regular $m$-gon; or one of the three groups of the Platonic solids, the tetrahedral group $A_4$ of order $12$, the octahedral group $S_4$ of order $24$ and the icosahedral group $A_5$ of order $60$.

**Proof sketch.** The group acts on the sphere; the orbits of the vertices of the convex hull of a generic orbit give a spherical tiling whose faces are congruent spherical polygons. Let $v, e, f$ be the numbers of vertices, edges and faces of the tiling and let $q$ be the number of faces at a vertex. Counting incidences gives $qf = 2e$ and $pf = 2e$ for the number $p$ of sides of a face, and the spherical Euler formula $v - e + f = 2$ together with the angle-sum formula gives $1/p + 1/q > 1/2$. The integer solutions with $p, q \geq 2$ are $(p, q) = (2, q)$ — the cyclic and dihedral families — and $(3,3), (3,4), (3,5), (4,3), (5,3)$ — the five Platonic cases, the last three up to interchange being $A_4$, $S_4$ and $A_5$. $\square$

**Corollary.** The finite subgroups of $O(3)$ that act freely on $S^2$ — those containing no rotation with a fixed point — are the trivial group and the cyclic groups of order $2$ acting by the antipodal map: the sphere and the elliptic space are the only two-dimensional spherical space forms up to isometry. In particular a finite free action of $SO(3)$ on $S^2$ is trivial, because every nontrivial rotation has an axis.

## The Three-Sphere and the Hopf Fibration

### The Unit Quaternions

**Theorem.** The unit sphere $S^3$, identified with the group of unit quaternions of *The Three Two-Dimensional Algebras and the Three Kinds of Rotation*, is a Lie group of dimension $3$ under quaternion multiplication, and the map

$$
\Phi : S^3 \longrightarrow SO(3), \qquad \Phi(q)(p) = qpq^{-1}, \quad p \in \operatorname{Im}\mathbb{H},
$$

is a surjective two-to-one Lie group homomorphism with kernel $\{\pm 1\}$. It identifies $S^3$ with $SU(2)$ and exhibits $S^3$ as the double cover of $SO(3)$.

**Proof sketch.** Unit quaternions are closed under multiplication and the norm is multiplicative, so $S^3$ is a group; conjugation by a unit quaternion preserves the imaginary subspace and the norm, so $\Phi(q) \in SO(3)$; the kernel consists of the unit quaternions commuting with every imaginary quaternion, namely $\{\pm 1\}$; both sides have dimension three, so the differential is an isomorphism and the map is a covering. $\square$

**Corollary.** The fundamental group of $SO(3)$ is $\mathbb{Z}/2\mathbb{Z}$, and $S^3$ is simply connected; the two are the two-dimensional rotation groups that the quaternion algebra distinguishes.

### The Hopf Fibration

**Definition.** The **Hopf map** is

$$
h : S^3 \longrightarrow S^2, \qquad h(q) = q\,e_1\,q^{-1} \in \operatorname{Im}\mathbb{H},
$$

using the identification of the imaginary subspace with $\mathbb{R}^3$ and restricting to unit vectors; equivalently, viewing $S^3 \subset \mathbb{C}^2$ as pairs $(z_1, z_2)$ with $|z_1|^2 + |z_2|^2 = 1$, the map is $h(z_1, z_2) = (2z_1\bar z_2, |z_1|^2 - |z_2|^2)$.

**Theorem.** The Hopf map is a smooth submersion, its fibre over every point is a great circle of $S^3$, and it is a fibre bundle with structure group $U(1) = S^1$; the sphere $S^3$ is the total space of a principal $S^1$-bundle over $S^2$.

**Proof sketch.** The map $\Phi$ has image $SO(3)$ and the stabiliser of a point of $S^2$ is a circle $SO(2)$, so the preimage of a point under the quotient $S^3 \to SO(3) \to S^2$ is a coset of the circle $\{e^{i\theta}\}$, a great circle. The local trivialisations come from local sections of the fibration, and the transition functions are circle-valued. The bundle theory is . $\square$

**Corollary.** The Hopf fibration is the standard nontrivial principal circle bundle and the first example of the relation between the homotopy groups of spheres; it realises $S^3$ as the total space of a bundle whose base is $S^2$ and whose fibre is $S^1$, and it is the geometric form of the double cover $SU(2) \to SO(3)$.

## Spherical Space Forms

**Definition.** A **spherical space form** is a complete connected Riemannian manifold of constant sectional curvature $+1$.

**Theorem.** Every spherical space form is isometric to a quotient $S^n/\Gamma$, where $\Gamma$ is a finite subgroup of $O(n+1)$ acting freely on $S^n$. In particular, a spherical space form is covered by the round sphere, its fundamental group is $\Gamma$, and its curvature is $+1$.

**Proof sketch.** The universal cover is complete, simply connected and of constant curvature $+1$, hence is isometric to the round sphere by Cartan's classification, and the covering group is a finite group of isometries acting freely, so it lies in $O(n+1)$. $\square$

**Corollary.** The fundamental group of a spherical space form is finite, the first Betti number is zero when the dimension is positive, and all such manifolds are compact with diameter at most $\pi$.

**Corollary (low dimensions).** In dimension two the only spherical space forms are the round sphere and the elliptic plane, by the classification of the finite subgroups of $O(3)$ above. In dimension three the free actions of finite subgroups of $O(4)$ are the cyclic ones giving the **lens spaces** and the other groups giving the remaining three-dimensional spherical space forms; their classification is the content, and it uses the same space-form theorem proved here. In dimension four and above the classification is not known in general, and it is equivalent to a question about free finite group actions on spheres.

**Remark (the trichotomy).** The spherical space forms complete the positive-curvature end of the trichotomy of *Curvature and Geodesics*: complete connected constant-curvature manifolds are either spherical (finite fundamental group, finite diameter), Euclidean (a finite cover of a flat torus by the Bieberbach theorems) or hyperbolic (infinite fundamental group, exponential volume growth). The Euclidean end is the subject of *Euclidean Geometry* and the hyperbolic end; the three together are the content.

## Summary

The round sphere $S^n_R$ is the compact Riemannian manifold of constant sectional curvature $1/R^2$; its geodesics are the great circles, its distance is $R$ times the central angle, its diameter is $\pi R$, and its isometry group is $O(n+1)$. Two points are joined by a unique minimising geodesic unless they are antipodal, in which case there are infinitely many of equal length.

Spherical trigonometry governs triangles bounded by great circles: the angle sum exceeds $\pi$ by the spherical excess $\Delta/R^2$, the spherical law of cosines reads $\cos c = \cos a\cos b + \sin a\sin b\cos C$, the law of sines is the constancy of $\sin a/\sin A$, and for a right triangle $\cos c = \cos a\cos b$. In the limit of small triangles the Euclidean law of cosines and the Pythagorean theorem are recovered, so the sphere of large radius approximates the plane. The polar triangle exchanges sides and supplements of angles, giving the duality of the trigonometric laws.

Elliptic space is the quotient of the sphere by the antipodal map; it has constant curvature $+1$, diameter $\pi/2$, fundamental group $\mathbb{Z}/2\mathbb{Z}$, and in it any two lines meet in exactly one point, so there are no parallels. The finite subgroups of $SO(3)$ are the cyclic, the dihedral and the three exceptional groups $A_4$, $S_4$, $A_5$ of the Platonic solids; the only finite free actions on $S^2$ are the trivial one and the antipodal one, so the sphere and the elliptic plane are the only two-dimensional spherical space forms.

The unit three-sphere is the group of unit quaternions, identified with $SU(2)$ and double-covering $SO(3)$; the Hopf map $S^3 \to S^2$ is a principal circle bundle whose fibres are great circles, and it is the geometric form of that double cover. Every spherical space form is a quotient of the round sphere by a finite group of isometries acting freely, so its fundamental group is finite and its curvature is $+1$; in dimension three the classification is that of the lens spaces and the remaining space forms, written in parallel, and it completes the positive-curvature end of the trichotomy of the model geometries.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S^n_R$ | Round sphere of radius $R$ in $\mathbb{R}^{n+1}$; $S^n = S^n_1$ |
| $g_R$, $\langle\cdot,\cdot\rangle$ | Round metric, the restriction of the standard inner product |
| $d_R(x,y) = R\arccos(\langle x,y\rangle/R^2)$ | Spherical distance, $R$ times the central angle |
| Great circle | Geodesic of the sphere; $S^n_R \cap P$ for a two-plane $P$ |
| $O(n+1)$, $SO(n+1)$ | Isometry group of $S^n_R$ and its orientation-preserving subgroup |
| $a, b, c$; $A, B, C$ | Sides and angles of a spherical triangle |
| $\Delta = R^2(A+B+C-\pi)$ | Girard's formula for the area via the spherical excess |
| $\cos c = \cos a\cos b + \sin a\sin b\cos C$ | Spherical law of cosines |
| $\sin a/\sin A = \sin b/\sin B = \sin c/\sin C$ | Spherical law of sines |
| Polar triangle | Triangle with sides $\pi - A$, etc.; realises the side–angle duality |
| $\mathbb{E}^n = S^n/\{\pm 1\}$ | Elliptic space; $\mathbb{E}^2 = \mathbb{RP}^2$; curvature $+1$, diameter $\pi/2$ |
| $C_m$, $D_m$, $A_4$, $S_4$, $A_5$ | Finite rotation groups of $S^2$ |
| $\Phi : S^3 \to SO(3)$ | Two-to-one cover by the unit quaternions; $S^3 \cong SU(2)$ |
| $h : S^3 \to S^2$ | Hopf map; principal $S^1$-bundle with great-circle fibres |
| Spherical space form | Complete constant-curvature $+1$ manifold $S^n/\Gamma$, $\Gamma$ finite acting freely |



## Further Reading

- John G. Ratcliffe, *Foundations of Hyperbolic Manifolds*, 2nd ed. (Springer, 2006), for spherical and hyperbolic geometry developed uniformly from the models.
- Harold S. M. Coxeter, *Introduction to Geometry*, 2nd ed. (Wiley, 1969), for spherical trigonometry and the Platonic solids.
- Marcel Berger, *Geometry I* (Springer, 1987), for the isometry groups of the sphere and the classification of the finite rotation groups.
- Glen E. Bredon, *Introduction to Compact Transformation Groups* (Academic Press, 1972), for free finite group actions on spheres and the spherical space form problem.
- Joseph A. Wolf, *Spaces of Constant Curvature*, 6th ed. (AMS Chelsea, 2011), for the space forms in all signatures and dimensions.
- Michael Atiyah and Friedrich Hirzebruch, "Quelques théorèmes de non-plongement pour les variétés différentiables", *Bulletin de la Société Mathématique de France* 87 (1959), 383–396, for applications of the spherical space forms.
- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002), for the fundamental group of $SO(3)$ and the Hopf fibration.
