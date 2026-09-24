
# __Euclidean Geometry__

## Introduction

Euclidean geometry is the geometry of the plane and of space with the notions of length and angle that are taught first: the geometry in which the sum of the angles of a triangle is two right angles, in which there is exactly one line through a given point parallel to a given line, and in which the distance between two points is the square root of the sum of the squares of the coordinate differences. It is the geometry of $\mathbb{R}^n$ with the standard positive definite inner product, and it is one of the three model geometries of constant curvature: it is the model of curvature zero, sitting between the spherical geometry of positive curvature and the hyperbolic geometry of negative curvature. It is also the geometry of the algebra $\mathbb{D}'$ of dual numbers, the parabolic case of *The Three Two-Dimensional Algebras and the Three Kinds of Rotation*.

This article develops the subject in the two languages that are needed for its later use. It first treats the **synthetic** formulation, in the tradition of Euclid and Hilbert: the primitive notions of point, line and incidence; the axioms of incidence, order, congruence and continuity; the parallel postulate and Playfair's form of it; congruence and similarity of triangles; and the classical theorems — the angle sum, the Pythagorean theorem, Thales' theorem, the law of cosines — with their proofs from the congruence criteria. It then treats the **analytic** formulation: Cartesian coordinates, the identification of the Euclidean plane and space with $\mathbb{R}^n$ equipped with the standard inner product, the Euclidean group of rigid motions as the semidirect product $\mathbb{R}^n \rtimes O(n)$, the classification of the isometries of the plane, and the correspondence between the congruence theorems of the synthetic theory and the algebraic facts about the orthogonal group. The article closes with the regular polygons, the Platonic solids and the Euclidean tilings, and with the crystallographic restriction, which is the bridge.

The article assumes the metric and topological background of *Metric, Uniform and Complete Spaces*; the linear algebra of *Vector Spaces*, *Bilinear Forms*, *Isometries and Orthogonal Transformations* and *The Determinant and Alternating Forms*; the group theory of *Groups*, *Group Actions and Structure* and *Matrix Groups and Classical Groups*; for the geometry of the sphere and of the constant-curvature models, the results are stated as standard. The crystallographic groups themselves are not covered here, and the boundary is stated in the text. No physics is invoked.

## The Euclidean Space and Its Group

### The Inner Product Space

**Definition.** Euclidean $n$-space is the real vector space $\mathbb{R}^n$ with the **standard inner product**

$$
\langle x, y\rangle = \sum_{i=1}^{n} x_i y_i ,
$$

the **norm** $|x| = \sqrt{\langle x, x\rangle}$, and the **distance** $d(x, y) = |x - y|$. The inner product is a positive definite symmetric bilinear form; in the notation of *Bilinear Forms* it is the standard form of signature $(n, 0)$.

**Theorem (Cauchy–Schwarz).** For all $x, y \in \mathbb{R}^n$,

$$
|\langle x, y\rangle| \leq |x|\,|y| ,
$$

with equality if and only if $x$ and $y$ are linearly dependent.

**Proof.** The quadratic $|x + ty|^2 = |x|^2 + 2t\langle x, y\rangle + t^2|y|^2$ is nonnegative for all real $t$; its discriminant is at most zero, which is the inequality, and equality forces a double root, hence dependence. $\square$

**Corollary.** The distance $d$ is a metric on $\mathbb{R}^n$, its metric topology is the standard topology, and the triangle inequality $|x + z| \leq |x| + |y| + |z - y|$ holds in the form $d(x, z) \leq d(x, y) + d(y, z)$.

**Definition.** The **angle** between nonzero vectors $x, y$ is the unique $\theta \in [0, \pi]$ with

$$
\cos\theta = \frac{\langle x, y\rangle}{|x|\,|y|},
$$

which is well defined by the Cauchy–Schwarz inequality. The vectors are **orthogonal** if $\langle x, y\rangle = 0$ and **parallel** if one is a scalar multiple of the other.

### The Euclidean Group

**Definition.** An **isometry** of Euclidean space is a map $F : \mathbb{R}^n \to \mathbb{R}^n$ with $d(Fx, Fy) = d(x, y)$ for all $x, y$. The isometries form a group $E(n)$, the **Euclidean group**.

**Theorem.** Every isometry of $\mathbb{R}^n$ is of the form

$$
F(x) = Ax + b, \qquad A \in O(n), \quad b \in \mathbb{R}^n ,
$$

and the representation is unique. Consequently $E(n)$ is the semidirect product $\mathbb{R}^n \rtimes O(n)$, with multiplication $(A, b)(A', b') = (AA', Ab' + b)$, and it is a Lie group of dimension $n(n+1)/2$; the subgroup of orientation-preserving isometries is $\mathbb{R}^n \rtimes SO(n)$.

**Proof sketch.** An isometry fixes the origin after a translation, and an isometry fixing the origin preserves the norm, hence the inner product by polarisation, so its linear part lies in $O(n)$; conversely every such map is an isometry. The semidirect product structure is the composition law, and the Lie group structure is the manifold structure of the semidirect product of the manifold $\mathbb{R}^n$ with the Lie group $O(n)$ of *Matrix Groups and Classical Groups*. $\square$

**Definition.** A **rigid motion** is an orientation-preserving isometry. An isometry $F(x) = Ax + b$ is a **translation** if $A = I$, a **rotation** if it has a fixed point and $A \in SO(n)$, a **reflection** if it has a fixed hyperplane and $A$ has determinant $-1$, and a **glide reflection** if it is the composition of a reflection and a translation parallel to its fixed hyperplane.

**Theorem (classification of plane isometries).** Every isometry of the Euclidean plane is exactly one of: the identity; a translation; a rotation about a point; a reflection in a line; or a glide reflection.

**Proof sketch.** Write $F(x) = Ax + b$. If $A = I$ the map is a translation or the identity. Otherwise $A \neq I$; if $A$ has a fixed vector, solving $x = Ax + b$ gives a fixed point and the map is a rotation or reflection according to the determinant; if $A$ has no fixed vector, which happens exactly when $A$ is a reflection matrix and $b$ is not orthogonal to the reflection axis, the map is a glide reflection. The cases exhaust the possibilities for the orthogonal part. $\square$

**Example (the three kinds of rotation).** In the plane the orientation-preserving isometries with a fixed point form the group $SO(2) = \{R_\theta\}$, whose generating rotations satisfy $R_\theta^2 = -1$ for $\theta = \pi/2$: this is the **elliptic** rotation, the geometry of the algebra $\mathbb{C}$. The parabolic and hyperbolic analogues — the transvections of $\mathbb{D}'$ and the boosts of $\mathbb{D}$ — are not Euclidean isometries, but they are the Euclidean and hyperbolic cases of the correspondence of *The Three Two-Dimensional Algebras and the Three Kinds of Rotation*: the parabolic rotations generate the translations of the Euclidean line, and the hyperbolic rotations generate the Lorentz boosts.

## The Incidence Structure and the Parallel Postulate

### Primitive Notions and Axioms

The synthetic theory begins with **points**, **lines** and the **incidence** relation, and builds the plane and space from axioms. The **incidence axioms** state that two distinct points determine a unique line; that every line contains at least two points; that there exist three non-collinear points; and, in space, that three non-collinear points determine a unique plane and that two planes meeting in a point meet in a line. The **order axioms** of Hilbert place the points of a line in a betweenness relation, making each line a dense linear order; the **congruence axioms** give the relations of congruence of segments and of angles and the transport of a segment or an angle along a ray; and the **continuity axioms** are the axiom of Archimedes and the completeness axiom, which make the line isomorphic to $\mathbb{R}$.

**Definition.** Two lines in the plane are **parallel** if they are coplanar and do not meet; a **transversal** of two lines is a line meeting both.

**Axiom (Euclid's fifth postulate).** If a line meets two lines so as to make the interior angles on one side sum to less than two right angles, then the two lines meet on that side.

**Axiom (Playfair).** Through a point not on a given line there passes exactly one line parallel to the given line.

**Theorem.** Euclid's fifth postulate and Playfair's axiom are equivalent, given the other incidence and congruence axioms.

**Proof sketch.** Playfair implies Euclid: if the two lines did not meet, the line through the given point parallel to the first would make with the transversal the supplementary angle prescribed, and the angle sum would be two right angles, contradicting the hypothesis. Euclid implies Playfair: given a line and a point, construct the parallel by copying the angle, which exists by the congruence axioms, and a second parallel would meet the first by the fifth postulate applied to a suitable transversal. $\square$

**Remark.** The parallel postulate is exactly what fails in spherical geometry, where any two great circles meet, and what holds in the opposite extreme in hyperbolic geometry, where infinitely many parallels pass through a point. The three geometries of constant curvature are therefore distinguished, at the level of the synthetic axioms, by the number of parallels: zero, one, or infinitely many.

### Consequences of the Parallel Postulate

**Theorem (angle sum).** In Euclidean geometry the sum of the interior angles of a triangle is two right angles; more generally the sum of the interior angles of a convex $n$-gon is $(n-2)\pi$.

**Proof sketch.** Draw through a vertex the unique parallel to the opposite side; the alternate interior angles are congruent to the two base angles, and the three angles at the vertex sum to a straight angle. The polygon case follows by triangulation from one vertex. $\square$

**Theorem (exterior angle).** An exterior angle of a triangle is the sum of the two remote interior angles, and is greater than either of them.

**Theorem (Pythagoras).** In a right triangle with legs $a, b$ and hypotenuse $c$,

$$
a^2 + b^2 = c^2 .
$$

**Proof.** Let the altitude from the right angle meet the hypotenuse at $D$, dividing it into segments of lengths $m$ and $n$, with $c = m + n$. The two smaller triangles are similar to the original, because they share an acute angle with it, so $a^2 = mc$ and $b^2 = nc$ by the similarity ratios. Adding,

$$
a^2 + b^2 = (m + n)c = c^2 . \qquad \square
$$

**Theorem (law of cosines).** In a triangle with sides $a, b, c$ and the angle $\gamma$ between the sides $a$ and $b$,

$$
c^2 = a^2 + b^2 - 2ab\cos\gamma .
$$

For $\gamma = \pi/2$ this is Pythagoras, and the law is the synthetic statement of the polarisation identity for the inner product. In the analytic language it is the immediate computation $|x - y|^2 = |x|^2 + |y|^2 - 2\langle x, y\rangle$ with $\langle x, y\rangle = ab\cos\gamma$.

**Theorem (Thales).** An angle inscribed in a semicircle is a right angle: if $A, B$ are the ends of a diameter of a circle and $C$ a point on the circle, then the angle at $C$ between $CA$ and $CB$ is a right angle.

**Proof.** Let $O$ be the centre. The triangles $OAC$ and $OBC$ are isosceles with $OA = OC = OB = r$, so the angle at $A$ equals the angle at $C$ in the first and the angle at $B$ equals the angle at $C$ in the second; the three angles of the triangle $ABC$ sum to $\pi$, and the angle at $C$ is the sum of the two equal angles, which gives it $\pi/2$. $\square$

## Coordinates and the Algebraic Model

### Cartesian Coordinates

**Definition.** A **Cartesian coordinate system** on the Euclidean plane is the choice of an origin $O$, two perpendicular oriented unit vectors $u_1, u_2$, and the map sending a point $P$ to the pair $(x_1, x_2)$ with $\overrightarrow{OP} = x_1u_1 + x_2u_2$. The **distance formula** is $d(P, Q) = \sqrt{(x_1 - y_1)^2 + (x_2 - y_2)^2}$, and the **dot product** is $\langle x, y\rangle = x_1y_1 + x_2y_2$. In dimension $n$ the same construction with $n$ orthonormal vectors identifies Euclidean space with $\mathbb{R}^n$.

**Theorem (the analytic model).** The map from the synthetic Euclidean plane to $\mathbb{R}^2$ determined by a choice of Cartesian coordinates is a bijection carrying incidence, betweenness, congruence of segments and congruence of angles to the corresponding algebraic relations; consequently the synthetic theory is a model of the analytic one and conversely.

**Proof sketch.** The correspondence is by construction: lines become the solution sets of linear equations, betweenness becomes the order of the affine parameter, segment congruence becomes equality of the norms of the difference vectors, and angle congruence becomes equality of the cosines. The verification of the axioms is a direct computation in each case, and the two theories prove the same theorems because they have the same models. $\square$

**Remark.** The analytic model is the reason Euclidean geometry is the geometry of the standard inner product: every synthetic theorem becomes a computation with the positive definite form $\sum x_i^2$, and the failure of the parallel postulate in the other two geometries becomes a statement about the sign of the quadratic form that replaces it.

### The Orthogonal Group and Congruence

**Definition.** The **orthogonal group** $O(n)$ is the group of linear isometries of $\mathbb{R}^n$, $O(n) = \{A : A^TA = I\}$, and $SO(n)$ is its subgroup of determinant one. A subset $X \subseteq \mathbb{R}^n$ is **congruent** to $Y$ if $Y = F(X)$ for some $F \in E(n)$.

**Theorem (congruence criteria).** Two triangles are congruent if they have (SSS) three pairs of equal sides, (SAS) two pairs of equal sides and the included angles equal, or (ASA) two pairs of equal angles and the included sides equal.

**Proof sketch.** Place one triangle with a vertex at the origin and two sides along the axes. The SAS condition determines the images of the three vertices under an isometry, since an isometry is determined by the image of two points and the choice of side; the SSS condition determines the third vertex up to reflection across the side, and the reflection is an isometry; the ASA condition determines the two rays and hence their intersection. $\square$

**Remark.** The congruence criteria are the synthetic shadows of the statement that an isometry is determined by its action on an affine frame; in the analytic model, an isometry is $x \mapsto Ax + b$ and a triangle determines $A$ and $b$ up to the stabiliser of the frame. Similarity — the same shape up to scaling — is the corresponding statement for the group $\mathbb{R}^n \rtimes (\mathbb{R}_{>0} \times O(n))$.

## Regular Polygons, Polytopes and Tilings

### Regular Polygons and the Platonic Solids

**Definition.** A **regular polygon** with $m$ sides is a plane polygon whose sides all have the same length and whose angles are all equal; its **rotation group** is the cyclic group $C_m$ of order $m$ of rotations by multiples of $2\pi/m$, and its full symmetry group is the dihedral group $D_m$ of order $2m$.

**Theorem.** The regular polygons exist for every $m \geq 3$, with the vertices at the $m$-th roots of unity in $\mathbb{C}$: $z_k = e^{2\pi i k/m}$.

**Definition.** A **regular polyhedron** is a convex polyhedron whose faces are congruent regular polygons and whose vertex figures are congruent. In Euclidean three-space there are exactly five: the tetrahedron, the cube, the octahedron, the dodecahedron and the icosahedron, with faces of $3, 4, 3, 5, 3$ sides respectively.

**Proof sketch.** At a vertex at least three faces must meet, and the angle sum of the faces at a vertex is less than $2\pi$. If the faces are regular $m$-gons, the condition is $k(1 - 2/m) < 2$, with $k \geq 3$; the integer solutions are $(m, k) = (3,3), (3,4), (3,5), (4,3), (5,3)$, the five solids of the statement. $\square$

**Theorem.** The symmetry group of the tetrahedron is the alternating group $A_4$ of order $12$, of the cube and the octahedron the symmetric group $S_4$ of order $24$, and of the dodecahedron and the icosahedron the alternating group $A_5$ of order $60$; these are the finite rotation groups of the sphere, leading to the classification.

### Tilings and the Crystallographic Restriction

**Definition.** A **tiling** of the plane is a countable family of polygons whose union is the plane and whose interiors are disjoint. A **regular tiling** has congruent regular polygonal tiles meeting vertex to vertex. A tiling is **periodic** if its symmetry group contains two independent translations, and its symmetry group is then a **wallpaper group**.

**Theorem (the three regular tilings).** The regular tilings of the Euclidean plane are exactly the triangular, the square and the hexagonal tiling, with $m$ the number of sides of the tile and $k$ the number of tiles at a vertex satisfying $1/m + 1/k = 1/2$; the solutions are $(m, k) = (3, 6), (4, 4), (6, 3)$.

**Theorem (crystallographic restriction).** If a finite-order rotation is a symmetry of a periodic plane tiling, its order is $2, 3, 4$ or $6$. Equivalently, a finite subgroup of the rotation group of a lattice in the plane is cyclic of order $1, 2, 3, 4$ or $6$.

**Proof sketch.** Let $R$ be a rotation of order $m$ preserving a lattice $L = \mathbb{Z}u_1 \oplus \mathbb{Z}u_2$. In the lattice basis, $R$ has an integer matrix, so its trace $2\cos(2\pi/m)$ is an integer; since $\cos(2\pi/m) \in [-1, 1]$, the trace lies in $\{-2, -1, 0, 1, 2\}$, giving $m \in \{1, 2, 3, 4, 6\}$. $\square$

**Remark (boundary with the crystallographic groups).** The symmetry groups of periodic tilings , more generally, the discrete subgroups of the Euclidean group $E(n)$ that contain a full lattice of translations, are the **crystallographic groups**: the $17$ wallpaper groups in the plane and the $230$ space groups in three-space, or $219$ once the enantiomorphic pairs are identified. Their classification, their structure as extensions of a lattice by a point group, and the Bieberbach theorems belong, the application article of this category, and the crystallographic restriction proved here is the finiteness statement that the classification there takes as its starting point. What belongs to Euclidean geometry is the geometry of the Euclidean group and the regular configurations it acts on; what belongs to the other article is the group theory of the discrete subgroups.

## The Euclidean Distance and Its Geometry

**Proposition.** The straight line is the unique curve of shortest length between two points of Euclidean space, and the geodesics of $\mathbb{R}^n$ with the standard metric are exactly the straight lines.

**Proof.** For any curve $\gamma$ from $x$ to $y$, the fundamental theorem of calculus gives

$$
|y - x| = \left|\int_a^b \gamma'(t)\,dt\right| \leq \int_a^b |\gamma'(t)|\,dt = L(\gamma),
$$

with equality exactly when $\gamma'$ is always a nonnegative multiple of the constant direction $y - x$, which is the straight segment. $\square$

**Theorem.** The isometry group $E(n)$ is exactly the group of bijections of $\mathbb{R}^n$ preserving the Euclidean distance, and it is generated by reflections: every isometry is a product of at most $n + 1$ reflections in hyperplanes.

**Proof sketch.** Reflections generate the orthogonal group of the linear part by the Cartan–Dieudonné theorem, and a reflection in an affine hyperplane supplies the translation part. $\square$

**Remark (Euclidean geometry as a model of curvature zero).** The Euclidean space $\mathbb{R}^n$ with the standard metric is the complete simply connected Riemannian manifold of constant sectional curvature zero; its isometry group is $E(n)$, acting transitively on points and, through the stabiliser $O(n)$, on frames. Its geometry is the flat case of the trichotomy of *Curvature and Geodesics*, and the parallel postulate holds in it exactly because the curvature vanishes. The relation between the curvature and the parallel postulate is made precise by the Jacobi-field comparison of *Riemannian Geometry*: zero curvature is the boundary case in which the comparison field is linear.

## Summary

Euclidean $n$-space is $\mathbb{R}^n$ with the standard positive definite inner product, norm and distance; the Cauchy–Schwarz inequality makes the distance a metric and makes the angle well defined. Every isometry is uniquely of the form $x \mapsto Ax + b$ with $A \in O(n)$, so the Euclidean group is the semidirect product $\mathbb{R}^n \rtimes O(n)$ of dimension $n(n+1)/2$; in the plane the isometries are the identity, the translations, the rotations, the reflections and the glide reflections, and the orientation-preserving ones are the elliptic rotations of the algebra $\mathbb{C}$.

Synthetically the plane is built from incidence, order, congruence and continuity axioms, and the parallel postulate is equivalent to Playfair's axiom that through a point outside a line there is exactly one parallel. From the postulate follow the angle sum $\pi$ of a triangle, the exterior-angle theorem, the Pythagorean theorem, the law of cosines and Thales' theorem; the congruence criteria SSS, SAS and ASA are the synthetic form of the statement that an isometry is determined by an affine frame. Cartesian coordinates identify the synthetic plane with the analytic model, in which all these theorems are computations with the standard inner product and the parallel postulate is the vanishing of the curvature.

The regular polygons exist for every number of sides, the regular polyhedra in three-space are the five Platonic solids, and the regular tilings of the plane are the triangular, square and hexagonal ones; the finite rotation symmetries of a periodic plane pattern have order $1, 2, 3, 4$ or $6$ by the crystallographic restriction, and the discrete groups that realise these symmetries are the crystallographic groups treated. Finally the geodesics of Euclidean space are the straight lines and the straight segment is the unique shortest curve between two points, so Euclidean geometry is the flat member of the trichotomy of the model geometries, the member in which precisely one parallel passes through each exterior point.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle x, y\rangle = \sum_i x_iy_i$ | Standard positive definite inner product on $\mathbb{R}^n$ |
| $|x| = \sqrt{\langle x, x\rangle}$ | Euclidean norm |
| $d(x, y) = |x - y|$ | Euclidean distance |
| $\theta$, $\cos\theta = \langle x,y\rangle/(|x||y|)$ | Angle between nonzero vectors |
| $E(n) = \mathbb{R}^n \rtimes O(n)$ | Euclidean group of isometries; dimension $n(n+1)/2$ |
| $O(n)$, $SO(n)$ | Orthogonal and special orthogonal groups |
| Translation, rotation, reflection, glide reflection | The plane isometries in the classification |
| $\overrightarrow{OP} = \sum_i x_iu_i$ | Cartesian coordinates with orthonormal frame $u_i$ |
| Congruent, similar | Related by an isometry; related by a similarity $\mathbb{R}^n\rtimes(\mathbb{R}_{>0}\times O(n))$ |
| $C_m$, $D_m$ | Rotation and symmetry groups of a regular $m$-gon; $|D_m| = 2m$ |
| Platonic solids | Tetrahedron, cube, octahedron, dodecahedron, icosahedron |
| Crystallographic restriction | A periodic lattice rotation has order $1, 2, 3, 4$ or $6$ |
| Wallpaper group | Symmetry group of a periodic plane tiling; classified |
| Curvature zero | The Euclidean space is the flat simply connected complete model |







## Further Reading

- David Hilbert, *Foundations of Geometry* (Open Court, 1902; reprinted by Dover), for the axiomatic treatment of the incidence, order, congruence and continuity axioms and the parallel postulate.
- Robin Hartshorne, *Geometry: Euclid and Beyond* (Springer, 2000), for the synthetic theory with Hilbert's axioms and their models.
- Marvin J. Greenberg, *Euclidean and Non-Euclidean Geometries: Development and History*, 4th ed. (W. H. Freeman, 2008), for the parallel postulate and the construction of the non-Euclidean models.
- Harold S. M. Coxeter, *Introduction to Geometry*, 2nd ed. (Wiley, 1969), for the classical theorems, regular polygons and polyhedra, and the Euclidean tilings.
- Marcel Berger, *Geometry I* (Springer, 1987), for the group-theoretic treatment of the Euclidean group and its subgroups.
- Ludwig Bieberbach, "Über die Bewegungsgruppen der Euklidischen Räume I", *Mathematische Annalen* 70 (1911), 297–336, for the crystallographic groups and their classification.
- Branko Grünbaum and G. C. Shephard, *Tilings and Patterns* (W. H. Freeman, 1987), for the classification of tilings and the symmetry of periodic patterns.
