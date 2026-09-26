
# __Real Line Geometry and Isometries__

## Introduction

This is the fourth article of the Real Numbers system in Part V, and it occupies the **geometry slot** of that system. The system is the ordered field $\mathbb{R}$ of *The Real Numbers*, and the object of study is the real line as a geometric object: the distance $\lvert x - y\rvert$, the isometries it determines, the group they form, the reflections and translations that generate it, and the subsidiary notions of interval, midpoint, similarity and crystallographic symmetry that the line supports. The real line is the *first* object of the ladder that carries a distance, and its geometry is the base case of the whole geometric ladder of Part V.

The algebra and the order of $\mathbb{R}$, and the representations of the additive group, are the subjects of *Real Algebra* and *Real Representations*, and are used here rather than developed; the metric and uniform structure of the line is from *Metric, Uniform and Complete Spaces*, the topological structure from *Topological Spaces* and *Topological Groups*, and the length of an interval from *Measure Theory and Integration*. What this article develops is only the geometric content: the classification of the isometries, the structure of the isometry group, the symmetries of a lattice, the similarities and the cross-ratio, and the failure of a nontrivial rotation in one dimension — the failure that makes the geometry of the line the base case of the Cayley–Klein ladder rather than a degenerate case of the plane.

Throughout, $\mathbb{R}$ is the real line with its usual absolute value, $\lvert x - y\rvert$ is the distance between $x$ and $y$, and an **isometry** of $\mathbb{R}$ is a bijection $f : \mathbb{R} \to \mathbb{R}$ with $\lvert f(x) - f(y)\rvert = \lvert x - y\rvert$ for all $x, y$. The translation by $b$ is $T_b(x) = x+b$, the reflection in the point $b/2$ is $R_b(x) = b - x$, the dilation of ratio $a$ is $D_a(x) = ax$, and $\operatorname{Isom}(\mathbb{R})$ is the group of all isometries under composition. The infinite dihedral group is $D_\infty = \mathbb{Z} \rtimes \mathbb{Z}/2\mathbb{Z}$, and the cross-ratio of four distinct real points is written $(x_1, x_2; x_3, x_4)$.

## The Metric Geometry of the Line

### Distance and Its Properties

**Definition.** The **distance** on $\mathbb{R}$ is $d(x,y) = \lvert x-y\rvert$. A **metric space** structure of this kind satisfies, for all $x, y, z$,

$$
d(x,y) \geq 0, \quad d(x,y) = 0 \iff x = y, \quad d(x,y) = d(y,x), \quad d(x,z) \leq d(x,y) + d(y,z),
$$

and the last is the triangle inequality, which for the absolute value is the inequality $\lvert x + y\rvert \leq \lvert x\rvert + \lvert y\rvert$.

**Theorem.** $(\mathbb{R}, d)$ is a complete, connected, separable metric space, and the closed balls $\bar B(x, r) = [x-r, x+r]$ are the closed intervals. The topology determined by $d$ is the order topology of $\mathbb{R}$, so its open sets are the unions of open intervals.

**Proof.** Completeness is the Cauchy construction of *The Real Numbers*; connectedness is the intermediate value property of the order, proved in *Real Algebra* by the completeness of the order; separability is the density of $\mathbb{Q}$ by *The Rational Numbers*; the identification of the balls with the intervals is immediate from the definition of the absolute value, and the agreement of the metric and order topologies is the standard equivalence of the two descriptions of the neighbourhoods. $\square$

**Theorem.** The **convex** subsets of $\mathbb{R}$ are exactly the intervals, and every interval is the intersection of $\mathbb{R}$ with a closed or open interval of the extended line. For $x < y$, the **segment** between them is $[x,y]$, its **midpoint** is $(x+y)/2$, and it is the unique point equidistant from $x$ and $y$ lying between them.

**Proof.** Convexity of a set $A$ means that $x, y \in A$ and $x \leq z \leq y$ imply $z \in A$; the subsets with this property are the intervals in the sense of *Order Theory and Lattices*, and the interval notation of *Real Algebra* applies. The midpoint statement follows from the bijectivity and monotonicity of $x \mapsto 2x$. $\square$

**Remark.** The line is a **geodesic** metric space: every pair of points is joined by a segment of length $d(x,y)$, and the segment is unique. This is the weakest of the geometric properties that the later systems of the ladder will carry, and it is the reason the line is taken as the base case: the geometric ladder begins with the line, which has distance but no angle, and the two-dimensional systems, which have angle, come after.

### Length and Measure

**Theorem (Lebesgue measure on the line).** There is a unique measure $\lambda$ on the Borel subsets of $\mathbb{R}$ with $\lambda([a,b]) = b-a$ for $a \leq b$, and $\lambda$ is the unique (up to a positive scalar multiple) measure on the Borel sets that is invariant under all translations: $\lambda(A + b) = \lambda(A)$.

**Proof.** The existence and the specification on the Borel sets are the construction of Lebesgue measure on $\mathbb{R}$ in *Measure Theory and Integration*; uniqueness up to scale is the standard argument by monotone classes, using that a translation-invariant measure is determined by its value on the unit interval. $\square$

**Corollary.** Every isometry of $\mathbb{R}$ preserves $\lambda$, since it preserves the length of intervals; the interval, its length and the distance therefore form a single geometric structure, and the group of transformations preserving all three is exactly $\operatorname{Isom}(\mathbb{R})$.

**Proof.** A measure preserving all intervals of the form $[a,b]$ agrees with $\lambda$ up to a scalar, and the scalar is $1$ because $[0,1]$ is preserved in length by an isometry; the last statement combines the preservation of distance with the classification theorem below. $\square$

## Isometries of the Line

### The Classification

**Theorem (classification of isometries).** Every isometry of $\mathbb{R}$ is of exactly one of the two forms

$$
T_b(x) = x + b \qquad (\text{a translation}), \qquad R_b(x) = b - x \qquad (\text{a reflection}).
$$

Consequently

$$
\operatorname{Isom}(\mathbb{R}) = \{T_b : b \in \mathbb{R}\} \cup \{R_b : b \in \mathbb{R}\},
$$

and the group is the disjoint union of the translations, which are orientation-preserving, and the reflections, which are orientation-reversing.

**Proof.** Let $f$ be an isometry and put $b = f(0)$. From $\lvert f(x) - b\rvert = \lvert x\rvert$ we get $f(x) = b + \sigma(x)x$ with $\sigma(x) \in \{1,-1\}$ for $x \neq 0$, and $f(0) = b$. On $(0,\infty)$ the sign $\sigma$ is constant: if $\sigma(x) \neq \sigma(y)$ for $x, y > 0$ then $\lvert f(x) - f(y)\rvert = x + y \neq \lvert x-y\rvert$, contradicting the isometry property, and the same argument applies on $(-\infty,0)$. If the two constants differed, then taking $x > 0 > y$ gives $\lvert f(x) - f(y)\rvert = \lvert x + y\rvert \neq \lvert x - y\rvert$ because $xy \neq 0$; hence $\sigma$ is constant on $\mathbb{R}\setminus\{0\}$ and $f = T_b$ or $f = R_b$. The two forms never coincide, since $T_b$ is strictly increasing and $R_b$ strictly decreasing. $\square$

**Theorem (composition laws).** For all $a, b \in \mathbb{R}$,

$$
T_a \circ T_b = T_{a+b}, \qquad T_a \circ R_b = R_{a+b}, \qquad R_a \circ T_b = R_{a-b}, \qquad R_a \circ R_b = T_{a-b} .
$$

Consequently the translations form a normal subgroup isomorphic to $(\mathbb{R}, +)$, the map $f \mapsto f(0) - 0$ restricted to the reflections is a torsor under the translations, and every reflection is an involution: $R_b \circ R_b = T_0 = \mathrm{id}$.

**Proof.** Each identity is an immediate computation: for instance $R_a(R_b(x)) = a - (b - x) = x + (a-b) = T_{a-b}(x)$, and $R_a(T_b(x)) = a - (x+b) = (a-b) - x = R_{a-b}(x)$. Normality of the translations is $R_a \circ T_b \circ R_a = T_{-b}$, which follows from the displayed laws. $\square$

| $\circ$ | $T_b$ | $R_b$ |
|---|---|---|
| $T_a$ | $T_{a+b}$ | $R_{a+b}$ |
| $R_a$ | $R_{a-b}$ | $T_{a-b}$ |

**Theorem (structure of the group).** There is a group isomorphism

$$
\operatorname{Isom}(\mathbb{R}) \cong \mathbb{R} \rtimes \mathbb{Z}/2\mathbb{Z},
$$

where $\mathbb{Z}/2\mathbb{Z} = \{1, -1\}$ acts on $\mathbb{R}$ by multiplication, the translation $T_b$ corresponding to $(b, 1)$ and the reflection $R_b$ to $(b, -1)$.

**Proof.** The map $(b, \varepsilon) \mapsto T_b$ for $\varepsilon = 1$ and $\mapsto R_b$ for $\varepsilon = -1$ is bijective by the classification, and the composition laws give

$$
(b,\varepsilon)(c,\eta) = (b + \varepsilon c, \varepsilon\eta),
$$

which is the semidirect product law for the action of $\{\pm1\}$ on $\mathbb{R}$. $\square$

**Theorem (fixed points and transitivity).** A translation $T_b$ with $b \neq 0$ has no fixed point; the identity $T_0$ fixes everything. A reflection $R_b$ fixes exactly the point $b/2$. The group $\operatorname{Isom}(\mathbb{R})$ acts transitively on $\mathbb{R}$, the stabiliser of a point is of order $2$, and the action on the set of ordered pairs at a fixed distance is transitive.

**Proof.** $T_b(x) = x$ gives $b = 0$; $R_b(x) = x$ gives $x = b/2$. Given $x, y$ there is a translation taking $x$ to $y$ (namely $T_{y-x}$), so the action is transitive; the stabiliser of $x$ is $\{\mathrm{id}, R_{2x}\}$; and given two ordered pairs with equal distance, a translation followed if necessary by the reflection in the midpoint carries one to the other. $\square$

### Orientation, Similarities and the Affine Group

**Definition.** The **similarity group** of the line is the group $\operatorname{Sim}(\mathbb{R}) = \{x \mapsto ax + b : a \neq 0\}$, the affine group $\operatorname{Aff}(\mathbb{R}) \cong \mathbb{R} \rtimes \mathbb{R}^\times$; the **ratio** of the similarity $x \mapsto ax+b$ is $\lvert a\rvert$, and it is **direct** if $a > 0$. A map is **affine** if it is of this form.

**Theorem.** An isometry is a similarity of ratio $1$; a similarity of ratio $r$ multiplies every distance by $r$, and the direct similarities form the subgroup $\mathbb{R} \rtimes \mathbb{R}_{>0}$ of index $2$, with $\operatorname{Isom}(\mathbb{R}) \leq \operatorname{Sim}(\mathbb{R})$. The group $\operatorname{Aff}(\mathbb{R})$ is exactly the group of transformations preserving the cross-ratio

$$
(x_1, x_2; x_3, x_4) = \frac{(x_3 - x_1)(x_4 - x_2)}{(x_3 - x_2)(x_4 - x_1)},
$$

for four distinct points, in the sense that a map preserving it in general position is affine.

**Proof.** The distance scaling is the identity $\lvert (ax_1+b) - (ax_2+b)\rvert = \lvert a\rvert\lvert x_1 - x_2\rvert$. The cross-ratio is invariant under $x \mapsto ax+b$ by direct substitution. Conversely, a bijection preserving the cross-ratio of every quadruple in general position carries three points to three points and is determined by them, hence agrees with the unique affine map taking three points to their images. $\square$

**Remark.** The classification of isometries is the statement that the line has exactly two "directions" of rigid motion, the translations and the reflections, and that the orientation is a two-valued invariant. This is the one-dimensional case of the fact that the isometry group of $\mathbb{R}^n$ is the semidirect product of the translations and the orthogonal group $O(n)$, whose identity component is the rotation group $SO(n)$; in dimension one $SO(1)$ is trivial, which is the precise sense in which the line admits no nontrivial rotation.

### The Failure of Rotation

**Theorem.** Every isometry of $\mathbb{R}$ that fixes a point and preserves orientation is the identity. Hence there is no nontrivial rotation of the real line.

**Proof.** By the classification, an orientation-preserving isometry is a translation $T_b$, and if it fixes a point $x$ then $b = 0$, so it is the identity. $\square$

**Remark.** A rotation is, by definition, an orientation-preserving isometry with a fixed point; the theorem therefore rules it out in one dimension, and the first genuine rotation must appear in a two-dimensional system. This is the geometric content of the ladder: the complex plane, whose isometry group contains the rotations $z \mapsto e^{i\theta} z$, is the first system in which rotation is nontrivial, and the real line is its degenerate one-dimensional base case, with the orthogonal group $O(1) = \{\pm 1\}$ in place of $O(2)$. The complex rotations are the subject, which belongs to the Complex Numbers system of this Part and completes the ladder begun here.

## Symmetry of the Line

### Discrete Subgroups

**Theorem.** Every subgroup $G \leq (\mathbb{R}, +)$ is either dense in $\mathbb{R}$ or of the form $a\mathbb{Z}$ for some $a \geq 0$.

**Proof.** If $G = \{0\}$ then $G = 0 \cdot \mathbb{Z}$. Otherwise let $a = \inf\{g \in G : g > 0\}$, which exists as an infimum in the complete order. If $a > 0$, then $a \in G$: were $a \notin G$, the definition of the infimum would give $h < g$ in $G$ with $a < h < g < 2a$, and then $0 < g - h < a$ with $g - h \in G$, contradicting the minimality of $a$; given $g \in G$, write $g = na + r$ with $n \in \mathbb{Z}$ and $0 \leq r < a$ by the division algorithm applied to $\lfloor g/a\rfloor$, so $r \in G$ and $r < a$, forcing $r = 0$; hence $G = a\mathbb{Z}$. If $a = 0$, then for every $\varepsilon > 0$ there is $g \in G$ with $0 < g < \varepsilon$, and the integer multiples of $g$ meet every interval of length $g$, so $G$ is dense. $\square$

**Corollary.** The additive group $\mathbb{Z}$ is a discrete subgroup of $\mathbb{R}$, its cosets are the residue classes modulo $1$, and the quotient $\mathbb{R}/\mathbb{Z}$ is the circle group, of which $\mathbb{R}$ is the universal cover. A subgroup of $\mathbb{R}$ is discrete if and only if it is cyclic.

**Proof.** The quotient is the circle group of *Topological Groups*, and the covering statement is the standard quotient map; a subgroup is discrete exactly when the infimum $a$ of its positive elements is positive, which is the cyclic case above. $\square$

### Crystallographic Symmetry in One Dimension

**Definition.** A **discrete subgroup** of $\operatorname{Isom}(\mathbb{R})$ is a subgroup whose action on $\mathbb{R}$ is properly discontinuous: for every $x$ there is a neighbourhood $U$ of $x$ such that $g(U) \cap U = \varnothing$ for all $g \neq \mathrm{id}$.

**Theorem.** A discrete subgroup $\Gamma \leq \operatorname{Isom}(\mathbb{R})$ that contains a nontrivial translation is generated by a translation and possibly one reflection, and is therefore

$$
\Gamma = a\mathbb{Z} \quad \text{or} \quad \Gamma = D_\infty(a) = a\mathbb{Z} \rtimes \{\mathrm{id}, R_0\},
$$

where $a > 0$ is the least positive translation length. A discrete subgroup containing no nontrivial translation is finite, of order at most $2$; it is trivial or generated by a reflection.

**Proof.** Let $G = \Gamma \cap \{T_b\}$ be the translation subgroup, a discrete subgroup of $(\mathbb{R},+)$ by the proper discontinuity, hence $a\mathbb{Z}$ by the previous theorem. If $\Gamma$ contains a reflection $R_b$, then $R_b^2 = \mathrm{id}$ and $R_b T_{na} R_b = T_{-na}$, so $\Gamma = a\mathbb{Z} \cup R_b\, a\mathbb{Z}$, which is the infinite dihedral group; conjugating by a translation if necessary puts $b = 0$. If $\Gamma$ has no reflection and no nontrivial translation, it is trivial; and a group of reflections alone has order at most $2$, since $R_a R_b = T_{a-b}$ is a translation, so two distinct reflections generate one. $\square$

**Corollary (one-dimensional crystallography).** The symmetry groups of a periodic subset of the line are exactly the infinite dihedral groups $D_\infty(a)$ and their subgroups, and the symmetry group of $\mathbb{Z}$ itself is $D_\infty = D_\infty(1) = \mathbb{Z} \rtimes \mathbb{Z}/2\mathbb{Z}$, generated by $x \mapsto x+1$ and $x \mapsto -x$.

**Proof.** A symmetry group of a periodic pattern is a discrete subgroup of $\operatorname{Isom}(\mathbb{R})$ containing a translation, and the classification above applies; the symmetries of $\mathbb{Z}$ are the maps $x \mapsto \pm x + n$ with $n \in \mathbb{Z}$, which form $D_\infty$. $\square$

**Remark.** The corollary is the one-dimensional case of the crystallographic classification, and it is the exact analogue of the statement that a two-dimensional wallpaper group is a discrete subgroup of $\operatorname{Isom}(\mathbb{R}^2)$; the point of separating it here is that the line's symmetry types are determined entirely by the translation lattice and the presence or absence of a reflection, whereas from dimension two onward the rotational parts of the point group make the classification genuinely richer.

## The Line as a Riemannian Manifold

### The Riemannian Structure

**Definition.** The **standard Riemannian metric** on $\mathbb{R}$ is the tensor field $g = dx \otimes dx$, which assigns to each tangent space the inner product $\langle \partial_x, \partial_x\rangle = 1$. The **length** of a piecewise $\mathcal{C}^1$ curve $\gamma : [c,d] \to \mathbb{R}$ is

$$
L(\gamma) = \int_c^d \lvert \gamma'(t)\rvert\,dt ,
$$

and the **intrinsic distance** associated with $g$ is the infimum of the lengths of the curves joining two points.

**Theorem.** The intrinsic distance of the standard metric is the distance $\lvert x - y\rvert$, and the infimum is attained by the affine curve $\gamma(t) = x + t(y-x)$; the metric is geodesic. The line is complete and connected, and its only isometries are the $T_b$ and $R_b$.

**Proof.** The length of the affine curve is $\lvert y-x\rvert$, and no curve can be shorter because $\lvert\int \gamma'\rvert \leq \int\lvert\gamma'\rvert$ together with the fundamental theorem of calculus gives $\lvert\gamma(d) - \gamma(c)\rvert \leq L(\gamma)$. Hence the intrinsic distance is $\lvert x-y\rvert$, and the isometries are those of the metric space, classified earlier. $\square$

### Geodesics and the Classification

**Definition.** A **geodesic** is a curve of locally minimal length, equivalently a curve $\gamma$ whose acceleration vanishes: in the standard coordinate, $\gamma'' = 0$.

**Theorem.** The geodesics of $\mathbb{R}$ are exactly the affine maps $\gamma(t) = at + b$ with $a \neq 0$, traversed at constant speed $\lvert a\rvert$; every pair of points is joined by a unique geodesic segment, and the exponential map at $p$ is $\exp_p(v) = p + v$, a global isometry from the tangent line to $\mathbb{R}$.

**Proof.** The geodesic equation in one dimension is $\gamma'' = 0$ because the Christoffel symbols vanish in the standard coordinate, so the affine maps are the geodesics; uniqueness follows by integrating the equation with prescribed initial data. $\square$

**Theorem (classification in dimension one).** Every connected one-dimensional Riemannian manifold is flat, and the curvature tensor vanishes identically; a complete connected one-dimensional Riemannian manifold is isometric either to the line $\mathbb{R}$ with the metric $r\,dx \otimes dx$, $r>0$, or to the circle $\mathbb{R}/a\mathbb{Z}$ of circumference $a$. The line is the universal covering of the circle, and the isometry group of the circle $\mathbb{R}/a\mathbb{Z}$ is the orthogonal group $O(2)$, which contains the genuine rotations $x \mapsto x + \theta$.

**Proof.** In one dimension the Riemann curvature tensor has no nonzero components, so every such manifold is flat and is locally isometric to $\mathbb{R}$; a complete and connected one is therefore either a line or a circle by the classification of the one-dimensional manifolds, and the covering statement is the standard quotient $\mathbb{R} \to \mathbb{R}/a\mathbb{Z}$. The isometry group of the circle is $O(2)$ acting on the angle. $\square$

**Remark.** The classification is the precise sense in which the line is the base case of the geometric ladder. In dimension one the three model geometries of the Cayley–Klein ladder coincide: Euclidean, spherical and hyperbolic geometry all degenerate to the line with its affine structure, and the sectional curvature of a one-dimensional manifold is vacuous, so no curvature invariant distinguishes them. The first genuine divergence of the three geometries, and the first genuine rotation, occur in dimension two, and it is there that the ladder of the systems of Part V begins to separate.

### The Line as the Universal Cover

**Theorem.** Every connected one-dimensional manifold is homeomorphic either to $\mathbb{R}$ or to the circle; consequently every one-dimensional Riemannian manifold has the line as its universal cover, and the fundamental group is either trivial or infinite cyclic.

**Proof.** A connected one-dimensional manifold is covered by open intervals, and the connectedness together with the second countability makes it an interval or a circle; the universal cover of the circle is the line, with deck transformation group $\mathbb{Z}$ generated by the translation $T_a$. $\square$

**Corollary.** The circle is the quotient of the line by the discrete subgroup $a\mathbb{Z}$ of the isometry group, and the projection $\mathbb{R} \to \mathbb{R}/a\mathbb{Z}$ is the quotient map of the action of the translation group; this identifies the geometry of the circle with the geometry of the line together with the choice of a lattice, in the sense of the crystallographic classification above.

## Summary

The real line is the first system of the ladder to carry a distance: $d(x,y) = \lvert x-y\rvert$ makes $\mathbb{R}$ a complete, connected, separable metric space whose topology is the order topology, whose convex subsets are the intervals, and whose segments have unique midpoints. The length of an interval is the restriction of Lebesgue measure, the unique translation-invariant Borel measure up to scale, and every isometry preserves it. Every isometry of the line is a translation $T_b(x) = x+b$ or a reflection $R_b(x) = b-x$, with the composition laws $T_aT_b = T_{a+b}$, $T_aR_b = R_{a+b}$, $R_aT_b = R_{a-b}$ and $R_aR_b = T_{a-b}$, so that $\operatorname{Isom}(\mathbb{R}) \cong \mathbb{R} \rtimes \mathbb{Z}/2\mathbb{Z}$, with the translations as the identity component, the reflections as the orientation-reversing elements, and the stabiliser of a point of order two.

The similarities $x \mapsto ax+b$ form the affine group $\mathbb{R} \rtimes \mathbb{R}^\times$, of which the isometries are the ratio-one elements, and the affine group is exactly the group preserving the cross-ratio. An orientation-preserving isometry with a fixed point is the identity, so the line admits no nontrivial rotation: the first genuine rotation requires two dimensions, and this is the sense in which the real line is the base case of the Cayley–Klein ladder completed by the complex and other two-dimensional systems. The subgroups of $(\mathbb{R},+)$ are dense or cyclic, the discrete subgroups of $\operatorname{Isom}(\mathbb{R})$ are trivial, cyclic, of order two, or infinite dihedral, and the symmetry group of the integer lattice is $D_\infty = \mathbb{Z} \rtimes \mathbb{Z}/2\mathbb{Z}$; this is the one-dimensional crystallographic classification, and it closes the geometry of the system $\mathbb{R}$ at its base case.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{R}$ | The real line |
| $d(x,y) = \lvert x-y\rvert$ | Distance |
| $\lvert x\rvert$ | Absolute value, the distance to $0$ |
| $\bar B(x,r)$ | Closed ball, the interval $[x-r, x+r]$ |
| $\lambda$ | Lebesgue measure on the line |
| $T_b$ | Translation $x \mapsto x + b$ |
| $R_b$ | Reflection $x \mapsto b - x$ |
| $\operatorname{Isom}(\mathbb{R})$ | Isometry group, $\mathbb{R} \rtimes \mathbb{Z}/2\mathbb{Z}$ |
| $\operatorname{Sim}(\mathbb{R})$, $\operatorname{Aff}(\mathbb{R})$ | Similarity and affine groups, $\mathbb{R} \rtimes \mathbb{R}^\times$ |
| $D_a$ | Dilation $x \mapsto ax$ |
| $D_\infty$, $D_\infty(a)$ | Infinite dihedral group, $a\mathbb{Z} \rtimes \mathbb{Z}/2\mathbb{Z}$ |
| $(x_1,x_2;x_3,x_4)$ | Cross-ratio |
| $a\mathbb{Z}$ | Discrete subgroup of translations of step $a$ |



## Further Reading

- John Stillwell, *Geometry of Surfaces* (Springer, 1992), for the classification of the isometries of the line and the plane and their groups.
- Marcel Berger, *Geometry I* (Springer, 1987), for the geometry of the line, the affine group and the cross-ratio.
- Heinrich W. Guggenheimer, *Differential Geometry* (Dover, 1977), for the one-dimensional case of the classification of isometries and the notion of a geodesic.
- David Hilbert and Stephan Cohn-Vossen, *Geometry and the Imagination* (Chelsea, 1952), for symmetry groups and the crystallographic viewpoint.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the Cayley–Klein ladder and the place of the one-dimensional case within it.
- H. S. M. Coxeter, *Introduction to Geometry* (Wiley, 2nd ed. 1969), for reflections, translations, similarities and the cross-ratio.
