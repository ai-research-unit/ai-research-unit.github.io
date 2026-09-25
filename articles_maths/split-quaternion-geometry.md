
# __Split-Quaternion Geometry__

## Introduction

This article describes the geometry carried by the split-quaternion algebra. It separates the two quadratic forms of the system, the signature-$(2,2)$ form on the algebra and its restriction of signature $(2,1)$ to the vector subspace, and describes the geometry each determines: the null quadric with its ruling, and the hyperboloids and the Lorentzian geometry of the vector subspace. It records the isometry groups and the homogeneous descriptions, and compares the situation with the neighbouring systems. The skeleton follows the sibling articles *Quaternion Geometry* and *Split-Biquaternion Geometry*, named only; no result of theirs is used, and the definite case of the first and the signature-$(4,2)$ case of the second share nothing beyond the shape.

The split-quaternion algebra, its vector subspace $V$, its norm form $N$, its matrix model and its idempotents are assumed from *Split-Quaternion Algebra*; the signature of the restricted form and the isotropy are assumed from *Split-Quaternion Norm and Invertibility*, the null cone and its two families of maximal isotropic subspaces from *Split-Quaternion Zero Divisors*, the adjoint action and the Lorentz group from *Split-Quaternion Rotations and the Lorentz Group*, and the hyperbolic-plane model on the split-quaternions from *Split-Quaternions and Hyperbolic Geometry*, which owns the model. The Lorentzian and pseudo-Riemannian geometry of Part II is that of *Pseudo-Riemannian and Lorentzian Geometry*, the hyperboloid model and the hyperbolic isometries are those of *Hyperbolic Geometry* and *Hyperbolic Rotations*, and the projective geometry of the quadric is that of *Projective Geometry*. Nothing physical is invoked.

## The Two Quadratic Forms and the Geometry Each Determines

**Definition.** The two quadratic forms of the system are

$$
N : \mathbb{H}_{\mathrm{s}} \to \mathbb{R}, \quad N(x) = a^2 + b^2 - c^2 - d^2,
$$

of signature $(2,2)$ on the four-dimensional algebra, and its restriction

$$
N|_{V} : V \to \mathbb{R}, \quad N(b e_1 + c e_2 + d e_3) = b^2 - c^2 - d^2,
$$

of signature $(2,1)$ on the three-dimensional vector subspace. The two associated geometries are the **projective geometry** of the quadric $N = 0$ in $\mathbb{P}^3$, on the algebra, and the **Lorentzian geometry** of the vector subspace with the form of signature $(2,1)$.

**Theorem (The Two Geometries Are Related by Restriction and by the Ruling).** The vector subspace is the $-1$ eigenspace of the conjugation inside the algebra, and the restriction of $N$ to it is the form of the Lorentzian geometry. The null cone of the restriction is the intersection of the null cone of $N$ with $V$, and the two families of maximal isotropic subspaces of the algebra meet $V$ in the isotropic lines and planes of the restricted form.

**Proof.** The identification of $V$ with the $-1$ eigenspace of the conjugation is (*Split-Quaternion Algebra*, §*The Two Eigenspaces*), and the restriction of the form is computed in the same article, §*The Restricted Form on the Vector Subspace*. The statements about the cones and the isotropic subspaces are the definitions of *Split-Quaternion Norm and Invertibility*, §*Isotropy*, and *Split-Quaternion Zero Divisors*, §*The Two Families*. $\square$

The two geometries are genuinely different, and the geometry of the algebra is not the geometry of the vector subspace. The form on the algebra has four variables and produces a surface in projective three-space; the form on the vector subspace has three variables and produces the Lorentzian geometry of three-dimensional Minkowski space. The algebra structure relates them: conjugation is the involution whose $-1$ eigenspace is $V$, and the algebra automorphisms are the isometries of the restricted form, not of the full $(2,2)$ form.

## The Null Quadric and the Ruling

**Definition.** The **null quadric** of the algebra is the real projective quadric

$$
Q = \{[x] \in \mathbb{P}^3 : N(x) = 0\} = \{[x] : x \neq 0, \ N(x) = 0\},
$$

that is, the set of isotropic lines of the form.

**Theorem (The Quadric Is Doubly Ruled).** The quadric $Q$ is a smooth surface, and it is the union of the lines of the two families of maximal isotropic planes of (*Split-Quaternion Zero Divisors*, §*The Two Families*):

$$
Q = \bigcup_{\ell \in \mathbb{P}^1} \mathbb{P}(R_\ell) = \bigcup_{\ell \in \mathbb{P}^1} \mathbb{P}(K_\ell),
$$

where $\mathbb{P}(R_\ell)$ denotes the projective line of the plane $R_\ell$. Every point of $Q$ lies in exactly one plane of the first family and exactly one plane of the second; the two families are parametrised by the same projective line and are exchanged by transposition.

**Proof.** An isotropic line is a line of rank-one matrices by *Split-Quaternion Zero Divisors*, §*The Zero Divisor Set as the Null Cone*, and a rank-one matrix lies in exactly one plane of each family by the corollary of the theorem on the two families there. Each plane $\mathbb{P}(R_\ell)$ is a projective line contained in $Q$, since the plane $R_\ell$ is totally isotropic; and the union of these lines is $Q$, because every isotropic line lies in some plane of the family. $\square$

**Corollary (The Quadric Is a Torus).** The quadric $Q$ is homeomorphic to a two-dimensional torus:

$$
Q \cong \mathbb{P}^1 \times \mathbb{P}^1 \cong S^1 \times S^1 .
$$

**Proof.** Send a point of $Q$ to the pair consisting of the plane of the first family containing it, which is an element of $\mathbb{P}^1$, and its position inside that plane, which is a point of the projective line $\mathbb{P}(R_\ell) \cong \mathbb{P}^1$. The theorem shows that the map is a bijection; both $\mathbb{P}^1$ and the family of planes are circles over the reals, so the product is a torus. $\square$

**Corollary (The Ruling in Coordinates).** In the angular coordinates of *Split-Quaternion Norm and Invertibility*, §*Isotropy*, a point of $Q$ is the line of $(\cos\alpha, \sin\alpha, \cos\beta, \sin\beta)$, and the ruling is described by the two combinations $\alpha+\beta$ and $\alpha-\beta$: the image line of the rank-one matrices depends only on $\alpha+\beta$, so the family of the planes $R_\ell$ is the family of loci of constant $\alpha+\beta$, while the kernel line depends only on $\alpha-\beta$, so the family $K_\ell$ is the family of loci of constant $\alpha-\beta$. The identification $(\alpha,\beta) \sim (\alpha+\pi,\beta+\pi)$ leaves both combinations of angles unchanged, so the two combinations are coordinates on the torus of lines, and the two rulings are its two families of circles.

The quadric is the projective image of the ruling by maximal isotropic planes, and it is the natural projective object of the system: a smooth quadric surface with the two rulings, on which the algebra's structure group acts.

**Theorem (The Group Action on the Quadric).** The unit group acts on $Q$ by conjugation, and the action descends to an action of $\mathrm{PSL}_2(\mathbb{R}) \cong \mathrm{SO}^{+}(2,1)$, of dimension three, on the torus $Q$; the kernel of the action is the centre $\mathbb{R}^{\times}$ of the unit group.

**Proof.** Conjugation by a unit is an algebra automorphism and preserves $N$, so it maps isotropic lines to isotropic lines; this gives the action of $\mathbb{H}_{\mathrm{s}}^{\times}$ on $Q$. The kernel of the action on the projective space is the set of units acting trivially on all lines of $\mathbb{H}_{\mathrm{s}}$, which is the centre $\mathbb{R}^{\times}$; the quotient is $\mathrm{PGL}_2(\mathbb{R})$ by the corollary of *Split-Quaternion Rotations and the Lorentz Group*, §*The Adjoint Representation*. $\square$

## The Unit Hyperboloids and Their Metrics

The level sets of the two forms carry metrics of opposite character.

**Theorem (The Level Set in the Algebra).** The set

$$
U = \{x \in \mathbb{H}_{\mathrm{s}} : N(x) = 1\}
$$

is a connected smooth three-dimensional submanifold of $\mathbb{R}^4$, equal as a set to the norm-one group $\mathrm{SL}_2(\mathbb{R})$. The polar form $B$ restricts to a pseudo-Riemannian metric of signature $(2,1)$ on it, and the metric is bi-invariant under left and right translations, so that $U$ is a three-dimensional Lorentzian group manifold.

**Proof.** The set is the level set of a regular value of $N$, since the gradient $2x$ does not vanish on it, so it is a smooth three-dimensional submanifold; it is connected because $\{N>0\}$ is connected by *Split-Quaternion Norm and Invertibility*, §*The Group of Units*, and the map $x \mapsto x/\sqrt{N(x)}$ is a retraction of $\{N>0\}$ onto it. The identification with the norm-one group is the same section. At the identity the tangent space is $V$, on which $B$ has signature $(2,1)$; left translations carry this form to a metric on all of $U$, and the form is invariant under left and right translations because $B$ is associative. $\square$

The quadric $U$ in $\mathbb{R}^{2,2}$ is the three-dimensional Lorentzian space form of signature $(2,1)$, the analogue for this signature of the de Sitter and anti-de Sitter quadrics; the Part II treatment of the space forms is in *Pseudo-Riemannian and Lorentzian Geometry*.

**Theorem (The Level Sets in the Vector Subspace).** In the vector subspace, the level sets of the restricted form are as follows.

1. The set $\{v \in V : N(v) = 1\}$ is a hyperboloid of two sheets. The induced form $B$ is definite on each sheet; hence $-B$ is a Riemannian metric of constant curvature $-1$, and each sheet is a copy of the hyperbolic plane, on which $\mathrm{SO}^{+}(2,1)$ acts transitively with stabiliser $SO(2)$.
2. The set $\{v \in V : N(v) = -1\}$ is a one-sheeted hyperboloid, connected. The induced form $B$ is indefinite of signature $(1,1)$ on it, and it is a Lorentzian surface, on which $\mathrm{SO}^{+}(2,1)$ acts transitively with stabiliser the one-parameter hyperbolic subgroup.
3. The set $\{v \in V : N(v) = 0\}$ is the light cone, a singular cone on the circle of isotropic lines.

**Proof.** *Induced metric.* At $v = e_1$ the tangent space to the level set $\{N=1\}$ is $v^{\perp} = \operatorname{span}\{e_2,e_3\}$, on which $B$ is negative definite; the group acts transitively on the level set by *Split-Quaternion Rotations and the Lorentz Group*, §*The Trichotomy of Timelike, Lightlike and Spacelike Elements*, so definiteness holds everywhere and the metric is Riemannian up to sign. At $v = e_2$ the tangent space to the level set $\{N=-1\}$ is $v^{\perp} = \operatorname{span}\{e_1,e_3\}$, on which $B = b'^2 - d'^2$ is indefinite of signature $(1,1)$, and transitivity again carries the statement everywhere. The curvature and the identification of each sheet with the hyperbolic plane are the hyperboloid model of *Hyperbolic Geometry*; the model built on the split-quaternions is *Split-Quaternions and Hyperbolic Geometry*. *Singularity of the cone.* The gradient of the restricted form vanishes at the origin, and the cone is a cone on its link, which is the circle of isotropic lines. The stabilisers are those computed in *Split-Quaternion Rotations and the Lorentz Group*, §*The Trichotomy of Timelike, Lightlike and Spacelike Elements*. $\square$

**Corollary (The Three Geometries of the Level Sets).** The level sets of the two forms give three geometries of different character: the Riemannian hyperbolic plane on each sheet of the timelike hyperboloid, the Lorentzian geometry of the one-sheeted hyperboloid and of the four-dimensional unit hyperboloid, and the degenerate light-cone geometry of the null level set. All three are acted on by the same group $\mathrm{SO}^{+}(2,1)$ in the vector subspace, and by the norm-one group in the algebra.

## The Isometry Group and the Homogeneous Description

**Theorem (The Isometry Groups).** The isometry group of the restricted form is $O(2,1)$, whose identity component is $\mathrm{SO}^{+}(2,1) \cong \mathrm{PSL}_2(\mathbb{R})$; the isometry group of the full form is $O(2,2)$, of dimension six. The algebra automorphisms form the subgroup $\mathrm{PGL}_2(\mathbb{R}) \cong SO(2,1)$, which is strictly smaller than the isometry group of the full form.

**Proof.** The orthogonal groups of the two forms are described in *Isometries and Orthogonal Transformations*, and the identification of the identity component of the first with $\mathrm{PSL}_2(\mathbb{R})$ is the double cover of *Split-Quaternion Rotations and the Lorentz Group*, §*The Double Cover of $\mathrm{SO}^{+}(2,1)$*. The automorphism group is $\mathrm{PGL}_2(\mathbb{R})$ by *Split-Quaternion Matrix Representations*, §*Uniqueness up to Conjugacy*, and it acts on the algebra preserving $N$, hence is a subgroup of $O(2,2)$; it is not all of it, since $\dim O(2,2) = 6$ and $\dim PGL_2(\mathbb{R}) = 3$. $\square$

**Theorem (The Homogeneous Descriptions).** The level sets are homogeneous spaces of the isometry group:

$$
\{N = 1\} \subset V \ \cong\ \mathrm{SO}^{+}(2,1)/SO(2),
$$

each sheet being one connected component of the coset space; and

$$
\{N = -1\} \subset V \ \cong\ \mathrm{SO}^{+}(2,1)/SO(1,1),
$$

and the nappes of the light cone are orbits with stabiliser the one-parameter unipotent group of null transvections of *Split-Quaternion Rotations and the Lorentz Group*, §*The Trichotomy of Timelike, Lightlike and Spacelike Elements*.

**Proof.** Transitivity on each level set and the computation of the stabilisers are that section, and the orbit–stabiliser theorem gives the display. $\square$

**Corollary (The Decomposition of the Vector Subspace).** The vector subspace decomposes into the orbits

$$
V = \{0\} \ \sqcup\ \{N = 1\} \ \sqcup\ \{N = -1\} \ \sqcup\ \{N = 0, v \neq 0\},
$$

and the last term is the union of the two nappes of the cone. The trichotomy of timelike, lightlike and spacelike elements is the orbit decomposition of the Lorentzian geometry.

## The Lorentzian Geometry of the Vector Subspace

The geometry of $V$ is three-dimensional Minkowski geometry, and its features are those of Part II.

**Theorem (The Causal Structure and the Hyperbolic Geometry).** The form $N$ on $V$ is indefinite and isotropic, so the vector subspace carries the full causal trichotomy: every nonzero vector is timelike ($N > 0$), lightlike ($N = 0$) or spacelike ($N < 0$), and the lightlike vectors form a cone, which the quaternion case does not have. The hyperboloid model of the hyperbolic plane is the sheet $N = 1$, with the metric $-B$; the isometry group of that metric is $\mathrm{PSL}_2(\mathbb{R})$, acting by the adjoint action, and the geodesics of the model are the intersections of the sheet with the planes through the origin.

**Proof.** The causal trichotomy is the orbit decomposition above; the metric and curvature on the sheet are the theorem on the level sets; the geodesics of a hyperboloid model are the orthogonal intersections with central planes, as treated in *Hyperbolic Geometry*, and the group action is the double cover. $\square$

**Corollary (The Lorentzian Surfaces).** The one-sheeted hyperboloid $N = -1$ and the nappes of the light cone carry the Lorentzian and degenerate geometries of the three-dimensional Minkowski space, with the causality relations inherited from $V$; the intersections of the hyperboloids with the central planes through the origin are the geodesics, timelike, lightlike or spacelike according to the type of the plane.

**Proof.** The induced metrics are those computed above; the geodesic statement is the standard reduction to central planes, as in *Pseudo-Riemannian and Lorentzian Geometry*. $\square$

## The Incidence Geometry of the Ruling

The two families of maximal isotropic planes give the quadric an incidence structure, and it is the projective geometry of the product $\mathbb{P}^1\times\mathbb{P}^1$.

**Theorem (The Incidence of the Two Families).** Every plane of the first family meets every plane of the second family in exactly one point of the quadric, and the resulting map

$$
\mathbb{P}^1 \times \mathbb{P}^1 \longrightarrow Q, \qquad (\ell, \ell') \longmapsto R_\ell \cap K_{\ell'},
$$

is a bijection. Two distinct planes of the same family meet only in the origin, so no two lines of the same family meet in $Q$; two lines of different families meet in exactly one point.

**Proof.** By the computation in *Split-Quaternion Zero Divisors*, §*The Two Families*, the intersection $R_\ell \cap K_{\ell'}$ consists of the matrices $uv^{\top}$ with $\mathbb{R}u = \ell$ and $\mathbb{R}v^{\perp} = \ell'$, a one-dimensional space; its projectivisation is a single point of $Q$. For the bijectivity, a point of $Q$ determines the plane of each family containing it, and the two planes determine the point back; the statement about the intersection of two planes of the same family follows because $\operatorname{im} M \subseteq \ell \cap \ell' = 0$ for distinct $\ell, \ell'$. $\square$

**Corollary (The Action on the Ruling).** The inner automorphisms of the algebra, that is the action of $\mathrm{PSL}_2(\mathbb{R})$, preserve each of the two families and act on each by Möbius transformations of the parameter $\mathbb{P}^1$; the anti-automorphism $\tau$ of transposition exchanges the two families. The group therefore acts on $Q = \mathbb{P}^1\times\mathbb{P}^1$ diagonally, on each factor by a Möbius transformation.

**Proof.** For a unit $g$, conjugation sends a rank-one matrix $M$ to $gMg^{-1}$, whose image is $g(\operatorname{im} M)$ and whose kernel is $g(\ker M)$; hence it carries $R_\ell$ to $R_{g\ell}$ and $K_{\ell'}$ to $K_{g\ell'}$, preserving each family. The action of an invertible matrix on the lines of $\mathbb{R}^2$ is the Möbius action on $\mathbb{P}^1$. Transposition exchanges the families by *Split-Quaternion Zero Divisors*, §*The Two Families*. $\square$

## The Geometry of the Distinguished Subspaces

Every distinguished subspace of the algebra inherits a form, and the inherited form determines a geometry of lower dimension.

| Subspace | Inherited form | Geometry |
|---|---|---|
| $S = \mathbb{R}\cdot 1$ | $a^2$ | definite; the unit level set is $\{\pm 1\}$ |
| $V$ | $b^2 - c^2 - d^2$, signature $(2,1)$ | the Lorentzian geometry of the vector subspace |
| $\mathbb{R}[e_1] = \operatorname{span}\{1,e_1\}$ | $a^2 + b^2$ | definite; a copy of the complex plane as a metric plane |
| $\mathbb{D}_2 = \operatorname{span}\{1,e_2\}$ | $a^2 - c^2$, signature $(1,1)$ | two null lines, $\mathbb{R}(1\pm e_2)$; the unit hyperbola $a^2 - c^2 = 1$ |
| $\mathbb{D}_3 = \operatorname{span}\{1,e_3\}$ | $a^2 - d^2$, signature $(1,1)$ | two null lines, $\mathbb{R}(1\pm e_3)$ |
| $\mathbb{H}_{\mathrm{s}}u_\pm$, $u_\pm\mathbb{H}_{\mathrm{s}}$ | identically zero | isotropic planes, ruling the quadric |

**Theorem (The Two-Dimensional Geometries).** On each split-complex subalgebra the inherited form has signature $(1,1)$; the null lines are the lines $\mathbb{R}(1\pm e_2)$ and $\mathbb{R}(1\pm e_3)$, and they are the two isotropic lines of the subalgebra. The isometry group of the subalgebra form is the group $O(1,1)$ of hyperbolic rotations, acting on the hyperbola $a^2 - c^2 = 1$ with two orbits, the two branches; the distance on a branch is the logarithm of the ratio of the two coordinates in the null basis. The subalgebra $\mathbb{R}[e_1]$ is definite, its form is positive definite, and its geometry is Euclidean; its unit circle is the compact group $SO(2)$ of the elliptic subgroup of *Split-Quaternion Rotations and the Lorentz Group*, §*Elliptic and Hyperbolic One-Parameter Subgroups*.

**Proof.** The forms are read from the norm form on the corresponding coordinates. In the null basis $n_{\pm} = \tfrac12(1 \pm e_2)$ of the split-complex subalgebra the form $a^2 - c^2$ becomes a product, $N(p n_+ + q n_-) = pq$, so the null lines are the coordinate axes and the hyperbola is $pq = 1$; hyperbolic rotations are the maps $(p,q)\mapsto(\lambda p, \lambda^{-1} q)$, and the invariant distance is $\log(\lambda)$. The definite case is the standard Euclidean geometry of the plane. $\square$

## Comparison with the Neighbouring Systems

| | $\mathbb{H}$ | $\mathbb{H}_{\mathrm{s}}$ |
|---|---|---|
| form on the algebra | definite, signature $(4,0)$ | indefinite, signature $(2,2)$ |
| null quadric | empty | a torus, doubly ruled |
| form on the vector part | definite, signature $(3,0)$ | indefinite, signature $(2,1)$, isotropic |
| level set of norm one | the sphere $S^3$, compact | the quadric $U \cong \mathrm{SL}_2(\mathbb{R})$, a Lorentzian three-manifold |
| level sets in the vector part | the sphere $S^2$ | two hyperbolic planes and a one-sheeted hyperboloid |
| causality | none | the full trichotomy |
| isometry group of the vector form | $O(3)$ | $O(2,1)$, with identity component $\mathrm{PSL}_2(\mathbb{R})$ |

The quaternion column is the definite geometry of *Quaternion Geometry*, in which the unit sphere is compact and there is no cone. The single cause of every difference is the sign pattern of the form. The eight-dimensional relative $\mathbb{H}_{\mathbb{D}}$ of the notation table is a later system of Part V, treated under Split-Biquaternions, and nothing of it is used here; the geometry of the present system is the three-dimensional Lorentzian geometry of the vector subspace together with the ruled quadric of the algebra, and the eight-dimensional system carries a different geometry.

## Summary

The split-quaternion system carries two quadratic forms: the form $N$ of signature $(2,2)$ on the four-dimensional algebra, and its restriction of signature $(2,1)$ to the three-dimensional vector subspace. The first determines the projective null quadric $Q$, a smooth doubly ruled surface homeomorphic to a torus, whose two rulings are the families of maximal isotropic planes; the unit group acts on it through $\mathrm{PSL}_2(\mathbb{R}) \cong \mathrm{SO}^{+}(2,1)$. The set $\{N=1\}$ in the algebra is the connected Lorentzian three-manifold $U \cong \mathrm{SL}_2(\mathbb{R})$ with a bi-invariant metric of signature $(2,1)$.

The second form determines the Lorentzian geometry of the vector subspace. The level set $N=1$ is a two-sheeted hyperboloid, each sheet a copy of the hyperbolic plane with the metric $-B$ and the group $\mathrm{SO}^{+}(2,1)$ acting transitively with stabiliser $SO(2)$; the level set $N=-1$ is a connected one-sheeted hyperboloid with an induced Lorentzian metric; and the level set $N=0$ is the light cone, a singular cone on the circle of isotropic lines. The nonzero vectors split into the timelike, lightlike and spacelike classes, so the full causal trichotomy is present, unlike in the quaternion case, where the form is definite and only the sphere occurs. The isometry group of the restricted form is $O(2,1)$ with identity component $\mathrm{PSL}_2(\mathbb{R})$, and the algebra automorphisms form the smaller group $\mathrm{PGL}_2(\mathbb{R}) \cong SO(2,1)$ inside the six-dimensional isometry group $O(2,2)$ of the full form. The eight-dimensional relative is a later system of Part V, named only.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $N(x) = a^2+b^2-c^2-d^2$ | the form of signature $(2,2)$ on the algebra | *Split-Quaternion Algebra* |
| $N|_{V} = b^2-c^2-d^2$ | the restricted form of signature $(2,1)$ | *Split-Quaternion Algebra* |
| $Q \subset \mathbb{P}^3$ | the projective null quadric, the set of isotropic lines | this article |
| $R_\ell$, $K_\ell$ | the two families of maximal isotropic planes | *Split-Quaternion Zero Divisors* |
| $Q \cong S^1 \times S^1$ | the quadric as a torus, with its rulings | this article |
| $U = \{N=1\} \cong \mathrm{SL}_2(\mathbb{R})$ | the unit quadric in the algebra, a Lorentzian three-manifold | this article |
| $\{N=1\}$, $\{N=-1\}$, $\{N=0\}$ in $V$ | the two-sheeted hyperboloid, the one-sheeted hyperboloid, the light cone | this article |
| $-B$ on a sheet | the hyperbolic metric of curvature $-1$ | this article |
| $O(2,1)$, $\mathrm{SO}^{+}(2,1) \cong \mathrm{PSL}_2(\mathbb{R})$ | the isometry group of the restricted form | *Split-Quaternion Rotations and the Lorentz Group* |
| $O(2,2)$ | the isometry group of the full form | this article |
| $\mathrm{PGL}_2(\mathbb{R}) \cong SO(2,1)$ | the algebra automorphism group | *Split-Quaternion Matrix Representations* |
| timelike, lightlike, spacelike | the causal trichotomy in $V$ | *Split-Quaternion Rotations and the Lorentz Group* |

## Further Reading

- Barrett O'Neill, *Semi-Riemannian Geometry with Applications to Relativity* (Academic Press, 1983), for the causal structure of Minkowski space, the hyperboloids and their induced metrics.
- John G. Ratcliffe, *Foundations of Hyperbolic Manifolds* (Springer, 2006), for the hyperboloid model, its geodesics and the classification of isometries.
- Igor R. Shafarevich, *Basic Algebraic Geometry 1* (Springer, 2013), for quadric surfaces, their rulings and their projective geometry.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the orthogonal groups of the low-dimensional indefinite forms and their spin covers.
