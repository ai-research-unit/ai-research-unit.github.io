
# __Möbius and Lie Sphere Geometry__

## Introduction

The Möbius geometry of the sphere is the geometry of the conformal structure of *Conformal Geometry* seen through the generalised spheres: its transformations are the Möbius transformations, its objects are the points, the spheres and the hyperplanes of the conformal sphere, and its basic invariant is the cross ratio of four points, which the Möbius group preserves. Lie sphere geometry is the larger geometry obtained by orienting the spheres and forgetting the distinction between the points and the other spheres: its objects are the **oriented spheres** of the sphere, including the points as the degenerate spheres, together with the **oriented contact** relation between them, and its transformations are the **Lie sphere transformations**, which preserve the oriented contact and form the projective orthogonal group of a quadratic form of signature $(n+1,2)$. The Möbius group is the subgroup of the Lie sphere group that preserves the set of points; this containment is the precise relation between the two geometries, and it is the reason the two are treated in one article.

Both geometries are geometries of a quadratic form, and both are realised inside the Clifford algebras of *The Clifford Algebra*, earlier in this Part. The Möbius sphere is the projectivised null cone of the form of signature $(n+1,1)$, as in *Conformal Geometry*, and its transformations are the Vahlen matrices over the Clifford algebra $\mathrm{Cl}_{0,n}$; the Lie sphere geometry is the geometry of the quadric of the form of signature $(n+1,2)$, and the additional dimension is exactly the dimension that records the orientation and the radius of the spheres. The article develops the Möbius space, its cross ratio and its group; the oriented spheres, the Lie quadric and the Lie sphere group; the contact relation and the polarity that encodes it; the curvature spheres and the Dupin and isoparametric classes; and the Lie invariance of the whole apparatus. The manifold theory of the conformal structure is cited to *Conformal Geometry*, *Riemannian Geometry* and *Smooth Manifolds and Differential Geometry*, and the article keeps to the geometry of the forms.

## Möbius Geometry

### The Möbius Space

**Definition.** The **Möbius space** of dimension $n$ is the sphere $S^n$ with its conformal structure, and the **Möbius group** is the group $\operatorname{Möb}(n) = \operatorname{Conf}(S^n) = O(n+1,1)/\{\pm 1\}$ of *Conformal Geometry*, acting on the sphere by the Möbius transformations; the **Möbius sphere** is the projectivised null cone of the form $|u|^2 - v^2$ on $\mathbb{R}^{n+1,1}$, and the points of the sphere correspond to the null lines of that cone. A **generalised sphere** of the Möbius space is the intersection of the null cone with a hyperplane of $\mathbb{R}^{n+1,1}$, that is, the zero set of a linear form; the generalised spheres are the spheres and the hyperplanes of the sphere, and the Möbius group carries generalised spheres to generalised spheres.

**Proposition.** In the Möbius model a generalised sphere is represented by a nonzero vector $w \in \mathbb{R}^{n+1,1}$ up to scale, and the sphere is the set of the null lines $[z]$ with $\langle w, z\rangle = 0$; writing $z_\infty = (0, 1, 1)$ for the point at infinity of the embedding $z(x)$ of *Conformal Geometry*, the type is read from the form and the pairing with $z_\infty$:

| Invariants of $w$ | Generalised sphere |
|---|---|
| $\langle w,w\rangle > 0$, $\langle w,z_\infty\rangle \neq 0$ | A round hypersphere of $S^n$ |
| $\langle w,w\rangle > 0$, $\langle w,z_\infty\rangle = 0$ | A hyperplane, that is, a hypersphere through the point at infinity |
| $\langle w,w\rangle = 0$ | A single point, namely the point $[w]$ |
| $\langle w,w\rangle < 0$ | The empty set |

The Möbius group acts on the generalised spheres by the linear action on $w$, so the family of the generalised spheres carries a Möbius-invariant incidence structure.

**Proof.** A hyperplane of $\mathbb{R}^{n+1,1}$ is the kernel of a nonzero linear form, whose metric dual is a vector $w$ up to scale, and the intersection with the null cone is the set of the null lines orthogonal to $w$, which is the displayed condition. If $w$ is null then the hyperplane $w^{\perp}$ is tangent to the cone along the line $\mathbb{R}w$, so $S(w) = \{[w]\}$; if $\langle w,w\rangle < 0$ the vector $w$ is timelike, its orthogonal complement is positive definite and carries no null direction, so the generalised sphere is empty; if $\langle w,w\rangle>0$ the vector is spacelike, the complement has signature $(n,1)$ and its null directions form a cone whose projectivisation is a hypersphere of the round sphere, which is a hyperplane of the Euclidean space exactly when the sphere passes through $z_\infty$, that is, when $\langle w,z_\infty\rangle = 0$. The equivariance is the linearity of the action. $\square$

**Example.** In the model of *Conformal Geometry*, with $z(x) = (x, (|x|^2-1)/2, (|x|^2+1)/2)$ and the pairing $\langle z, w\rangle = x\cdot w_0 + z_1 w_1 - z_2 w_2$ for $z = (x, z_1, z_2)$ and $w = (w_0, w_1, w_2)$, the round sphere with centre $c$ and radius $r$ is represented by
$$
w = \left(-c,\ \frac{1 - |c|^2 + r^2}{2},\ -\frac{1 + |c|^2 - r^2}{2}\right)
$$
up to scale, for which $\langle w,w\rangle = r^2$ and $\langle z(x), w\rangle = \tfrac{1}{2}(|x-c|^2 - r^2)$, so that the zero set is the sphere; the sphere contains the point at infinity exactly in the limiting case $r = \infty$, in which it is a hyperplane; for $r = 0$ the vector is the point vector of $c$, of norm zero, and for the limit $r \to \infty$ the normalised vectors converge to the vectors of the hyperplanes. The hyperplane $a\cdot x = b$ with $|a| = 1$ is represented by $w = (a, b, b)$, for which $\langle z(x),w\rangle = a\cdot x - b$ and $\langle w,w\rangle = 1$, so a hyperplane is a space-like generalised sphere orthogonal to $z_\infty = (0,1,1)$, which is the null vector of the point at infinity of the embedding $z(x)$.

### The Cross Ratio

**Definition.** Let $z_1, z_2, z_3, z_4$ be null vectors of $\mathbb{R}^{n+1,1}$ representing four points of the Möbius sphere, with the pairings $\langle z_i, z_j\rangle \neq 0$ for the pairs in the denominator. The **Möbius cross ratio** is
$$
[z_1 : z_2 : z_3 : z_4] = \frac{\langle z_1, z_2\rangle\,\langle z_3, z_4\rangle}{\langle z_1, z_3\rangle\,\langle z_2, z_4\rangle},
$$
a nonzero scalar determined by the four points up to the scaling of the representatives.

**Proposition.** The cross ratio is invariant under the Möbius group, in the sense that the value is unchanged by the linear action of $O(n+1,1)$ on the representatives; it recovers the conformal structure of the sphere, since the distance of two points is determined by the cross ratio with two auxiliary points, and the ratio is the complete invariant of the configuration of four points in general position.

**Proof.** The action multiplies every $z_i$ by the same linear transformation, and the pairings transform by $\langle gz_i, gz_j\rangle = \langle z_i, z_j\rangle$ because $g \in O(n+1,1)$ preserves the form, so the numerator and the denominator of the cross ratio are unchanged. For the metric, the null vector of a point $x$ of the unit sphere in the model is $(x,1)$, whose pairing with the vector of a point $y$ is $\langle x,y\rangle - 1 = \cos d(x,y) - 1$, so the cross ratio determines $\cos d$ and hence the distance; the completeness of the invariant is the classical statement that the Möbius group acts transitively on the ordered quadruples in general position, with the cross ratio as the invariant. $\square$

**Remark.** The cross ratio is the Möbius analogue of the conformal invariants of *Conformal Geometry*: it is the simplest invariant that detects the conformal structure, and it is the source of the "Möbius-invariant" metric quantities of the submanifold theory, in which the Möbius geometry of a submanifold is developed from the cross ratio and its infinitesimal versions.

### Möbius Structures and the Submanifold Theory

**Definition.** A **Möbius structure** on a smooth manifold $M$ of dimension $n \geq 3$ is a conformal structure; by Liouville's theorem of *Conformal Geometry* the Möbius automorphisms of a Möbius structure are the conformal automorphisms, and the local Möbius geometry is the local conformal geometry. For a submanifold $N \subseteq S^n$ the **Möbius geometry of the submanifold** is the study of the Möbius invariants of the embedding, that is, the quantities invariant under the Möbius group rather than under the isometries of the sphere.

**Remark.** The Möbius geometry of a hypersurface is developed from the **Möbius second fundamental form**, the trace-free part of the second fundamental form with respect to a Möbius-invariant metric on the hypersurface, and from the **Möbius curvature spheres**, which are the spheres tangent to the hypersurface at a point with the appropriate order of contact; the Möbius invariants are the conformal invariants of the embedding, and they are the subject of the conformal submanifold theory. The classical classes are the **Möbius isoparametric** hypersurfaces, characterised by the constancy of the Möbius invariants, and the Dupin hypersurfaces of the next section; the theory is in the references, and the article records the definitions and the place of the objects in the Möbius geometry.

## Lie Sphere Geometry

### Oriented Spheres and the Lie Quadric

**Definition.** Let $n \geq 2$ and let $\mathbb{R}^{n+1,2}$ be the real vector space of dimension $n+3$ with the form of signature $(n+1,2)$. The **Lie quadric** is the set of null lines of this form,
$$
\mathcal{Q}^{n+1} = \{[z] : z \in \mathbb{R}^{n+1,2}\setminus\{0\},\ \langle z,z\rangle = 0\} \subseteq \mathbb{P}(\mathbb{R}^{n+1,2}),
$$
the projectivised null cone of the form, a smooth quadric of dimension $n+1$. The **Lie sphere geometry** of the sphere $S^n$ is the geometry of the quadric $\mathcal{Q}^{n+1}$ with the incidence relation defined by the polarity of the form, and its transformations are the **Lie sphere transformations**, the projective orthogonal transformations of the form, that is, the group $PO(n+1,2) = O(n+1,2)/\{\pm 1\}$.

**Theorem.** The points of the Lie quadric $\mathcal{Q}^{n+1}$ parametrise the oriented spheres of $S^n$, the degenerate spheres being the points of $S^n$; the group $PO(n+1,2)$ acts transitively on the quadric and preserves the relation of **oriented contact**, where two oriented spheres are in oriented contact if and only if the corresponding null lines are orthogonal, $\langle z, z'\rangle = 0$, that is, if and only if the two points of the quadric span a line contained in the quadric; the Lie sphere transformations are exactly the transformations of the set of oriented spheres that preserve the oriented contact.

**Proof sketch.** An oriented sphere of $S^n$ is described by its centre and its oriented radius, and the assignment of a null line of $\mathbb{R}^{n+1,2}$ is the classical "Lie correspondence": the extra dimension of the form records the radius and the orientation, and the points of the sphere correspond to the null lines of a fixed hyperplane of the form, so that the quadric contains the Möbius model as the set of the degenerate spheres. Oriented contact means that the two spheres touch at a point with the same oriented tangent hyperplane, and the algebra of the contact is the polarity of the quadric: the tangent hyperplane at a point of the quadric is the polar hyperplane of the point, and the two points are conjugate exactly when the corresponding spheres are in oriented contact, a computation in the model of the next subsection. The preservation of the contact by the orthogonal group and the converse are in the references. $\square$

**Example (the classical model).** Take $n = 2$, so that the sphere is the round two-sphere and the oriented spheres are the oriented circles, with the points as the degenerate circles; the Lie quadric is a smooth three-dimensional quadric in $\mathbb{P}(\mathbb{R}^{3,2})$, and the Lie sphere group is $PO(3,2)$, of dimension $10$; the Möbius group $\operatorname{Möb}(2) = PO(3,1)$ is the subgroup preserving the point set, of dimension $6$; the Lie sphere transformations include the **Laguerre transformations** and the inversions, and they are the transformations of the oriented circles preserving the oriented contact, which is the classical Lie sphere geometry of the plane and of the two-sphere.

### The Model and the Contact Form

**Remark.** The Lie quadric is described concretely by the **Lie form** on $\mathbb{R}^{n+1,2}$: in the coordinates $(u, v, s, t)$ with $u \in \mathbb{R}^{n}$ and $v, s, t \in \mathbb{R}$, the form
$$
\langle z, z\rangle = |u|^2 + 2vs - 2t^2
$$
has the signature $(n+1,2)$, since $|u|^2$ is positive definite in one dimension and the pair $(v,s)$ carries the form $2vs$ of signature $(1,1)$; the null lines of this form are the oriented spheres, with the points as the degenerate spheres, and the polarity $\langle z, z'\rangle = 0$ is the oriented contact. The model is the refinement of the null-cone model of the Möbius geometry: the extra dimension records the orientation and the radius, and the passage to the Möbius cone is the map that sends an oriented sphere to its underlying point sphere on the points and forgets the orientation and the radius of the other spheres.

**Remark.** The **Laguerre geometry** is the geometry of the oriented spheres and the oriented planes with the oriented contact in the Euclidean space, in which the planes form a distinguished family; it is the Lie sphere geometry with the family of the "plane" spheres distinguished, and the **Laguerre group** is the corresponding subgroup of the Lie sphere group, the stabiliser of the family of the planes. The Laguerre transformations preserve the oriented planes and the oriented contact, and the Laguerre geometry is the classical geometry of the "oriented spheres and planes" of the Euclidean space; the theory is in the references.

### Curvature Spheres, Dupin and Isoparametric Hypersurfaces

**Definition.** Let $f : N \to S^n$ be an immersed hypersurface with a unit normal field and principal curvatures $\kappa_1, \ldots, \kappa_{n-1}$ at each point. A **curvature sphere** of the hypersurface at a point is an oriented sphere tangent to the hypersurface at the point whose oriented curvature in the normal direction is one of the principal curvatures; the curvature spheres form the **curvature sphere congruence** of the hypersurface, a family of oriented spheres depending on the point and the choice of the principal curvature.

**Theorem (Lie's invariance of the curvature spheres).** A Lie sphere transformation maps the curvature sphere congruence of a hypersurface to the curvature sphere congruence of the image hypersurface; consequently the **Dupin property**, the property that at each point the curvature spheres are in oriented contact with the common tangent sphere and form a system of spheres in oriented contact along each of the $n-1$ curvature foliations, is invariant under the Lie sphere transformations, and the **Dupin hypersurfaces** are the Lie-invariant class of the hypersurfaces whose curvature sphere congruences have the contact structure in the strongest sense.

The theorem is the classical invariance of Lie; the curvature spheres are defined by the contact of the sphere with the hypersurface, which is a Lie-invariant notion, and the invariance of the congruence is the infinitesimal form of the preservation of the oriented contact. The **isoparametric hypersurfaces**, the hypersurfaces whose principal curvatures are constant along the curvature foliations and whose focal sets are the submanifolds of the ambient space, are the special Dupin hypersurfaces for which the principal curvatures are constant; the classification of the isoparametric hypersurfaces of the sphere is the classical theory of Cartan, Münzner and their successors, and the Lie sphere geometry is the natural setting for its formulation, since the Lie sphere transformations relate the isoparametric hypersurfaces of the various ambient spheres. The statements are in the references.

## The Relation between the Two Geometries

**Theorem.** The Möbius geometry is the Lie sphere geometry with the set of the points distinguished: the Möbius group $\operatorname{Möb}(n) = O(n+1,1)/\{\pm 1\}$ is the subgroup of the Lie sphere group $PO(n+1,2)$ that preserves the set of the degenerate spheres, and the embedding of the Möbius model into the Lie model,
$$
\mathbb{R}^{n+1,1} \hookrightarrow \mathbb{R}^{n+1,2},
$$
as the hyperplane of the form cut out by the coordinates of the orientation, realises the Möbius space as the set of the point spheres of the Lie quadric; the Lie sphere group contains the Möbius group as the subgroup preserving the point spheres, and it acts transitively on the oriented spheres; the two geometries have the same local invariants of the conformal structure, and the Lie sphere geometry carries in addition the invariants of the oriented contact, of which the curvature sphere congruence of a hypersurface is the basic example.

**Proof sketch.** The stabiliser of the subspace $\mathbb{R}^{n+1,1}$ in $O(n+1,2)$ is the group $O(n+1,1)$ of the form restricted to the hyperplane, which proves the containment of the Möbius group; the set of the point spheres is the subvariety of the quadric corresponding to the fixed hyperplane, and its preservation is exactly the preservation of the subspace. The Lie sphere transformations that preserve the points are the Möbius transformations, and the general Lie sphere transformation is a Möbius transformation followed by a transformation of the orientation, which gives the generation. The invariants statement is the dimension count of the two groups. $\square$

**Corollary.** A conformal structure of dimension $n \geq 3$, that is, a Möbius structure, determines a Lie sphere structure, and the Lie sphere invariants include the Möbius invariants; the Möbius invariants of the submanifolds of *Conformal Geometry* are the Lie sphere invariants that involve the point spheres, and the curvature sphere congruences of the Lie sphere geometry carry the additional invariants that are invisible to the conformal structure alone.

**Remark.** The two geometries are the geometries of the two quadratic forms $\mathbb{R}^{n+1,1}$ and $\mathbb{R}^{n+1,2}$ attached to the conformal sphere, and the passage between them is the addition of the dimension of the orientation; the same passage occurs in the Clifford algebra, where the Vahlen matrices of *Conformal Geometry* over $\mathrm{Cl}_{0,n}$ realise the Möbius group and the corresponding matrices over the Clifford algebra of the extended form realise the Lie sphere group, the addition of the dimension of the orientation being the algebraic form of the passage from the Möbius to the Lie model. The theory of the conformal groups of *The Clifford, Pin and Spin Groups* is the source of the identification.

## Summary

The **Möbius geometry** of dimension $n$ is the geometry of the sphere $S^n$ with its conformal structure, its transformations are the Möbius group $\operatorname{Möb}(n) = O(n+1,1)/\{\pm 1\}$ of *Conformal Geometry*, and its model is the projectivised null cone of the form $|u|^2 - v^2$ on $\mathbb{R}^{n+1,1}$; the **generalised spheres** are the null lines orthogonal to a vector, and they are the spheres, the hyperplanes and their degenerate cases according to the type of the vector. The **Möbius cross ratio** $[z_1:z_2:z_3:z_4] = \frac{\langle z_1,z_2\rangle\langle z_3,z_4\rangle}{\langle z_1,z_3\rangle\langle z_2,z_4\rangle}$ is the basic Möbius invariant, it recovers the conformal distance, and it is the source of the Möbius invariants of the submanifold theory, whose classes include the Möbius isoparametric hypersurfaces. The **Lie sphere geometry** is the geometry of the **Lie quadric** $\mathcal{Q}^{n+1} \subseteq \mathbb{P}(\mathbb{R}^{n+1,2})$, the projectivised null cone of the form of signature $(n+1,2)$; the quadric parametrises the **oriented spheres** of $S^n$, with the points as the degenerate spheres, and the **Lie sphere group** $PO(n+1,2)$ acts transitively on it preserving the **oriented contact**, where two oriented spheres are in oriented contact if and only if the corresponding points of the quadric are polar, $\langle z,z'\rangle = 0$. The Lie sphere transformations preserve the **curvature sphere congruence** of a hypersurface, whence the Lie invariance of the **Dupin** and the **isoparametric** hypersurfaces; the **Laguerre geometry** is the variant in which the planes are distinguished. The Möbius geometry is the Lie sphere geometry with the set of the points distinguished: the Möbius group is the subgroup of the Lie sphere group preserving the point spheres, and the Möbius model embeds in the Lie model as the hyperplane $\mathbb{R}^{n+1,1} \hookrightarrow \mathbb{R}^{n+1,2}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S^n$, $\operatorname{Möb}(n) = O(n+1,1)/\{\pm 1\}$ | Möbius space and Möbius group |
| $\mathbb{R}^{n+1,1}$, $|u|^2 - v^2$ | Möbius model space and its form |
| $\mathcal{N}$, $[z]$ | Null cone and its lines; points of the Möbius sphere |
| generalised sphere | Null lines orthogonal to a vector $w$; sphere, hyperplane, degenerate |
| $[z_1:z_2:z_3:z_4]$ | Möbius cross ratio |
| $\mathcal{Q}^{n+1} \subseteq \mathbb{P}(\mathbb{R}^{n+1,2})$ | Lie quadric; oriented spheres of $S^n$ |
| $\mathbb{R}^{n+1,2}$, signature $(n+1,2)$ | Lie model space and its form |
| $PO(n+1,2)$ | Lie sphere group |
| $\langle z, z'\rangle = 0$ | Oriented contact via the polarity |
| curvature sphere | Oriented sphere tangent with curvature a principal curvature |
| Dupin hypersurface | Curvature spheres in oriented contact along the curvature foliations |
| isoparametric hypersurface | Constant principal curvatures along the curvature foliations |
| $PO(n+1,1)$ | Möbius group as the point-preserving subgroup; Laguerre variant |

## Further Reading

- Thomas E. Cecil and Patrick J. Ryan, *Geometry of Hypersurfaces* (Springer, 2015), for the Möbius and Lie sphere geometry of the hypersurfaces, the curvature spheres and the Dupin theory.
- Thomas E. Cecil, *Lie Sphere Geometry: With Applications to Submanifolds* (Springer, second edition, 2008), for the Lie quadric, the Lie sphere group and the oriented contact.
- Shiing-Shen Chern and Jürgen K. Moser, "Real Hypersurfaces in Complex Manifolds", *Acta Mathematica* 133 (1974), 219–271, for the Möbius invariants and the Möbius geometry of the hypersurfaces.
- Huafei Sun and Changping Wang, "Möbius Geometry of Hypersurfaces", in *Möbius Geometry* (Science Press, 2008), for the Möbius second fundamental form and the Möbius isoparametric hypersurfaces.
- Wilhelm Blaschke, *Vorlesungen über Differentialgeometrie III* (Springer, 1929), for the classical Laguerre and Lie sphere geometries.
- Lars V. Ahlfors, "Möbius Transformations in $\mathbb{R}^n$ Expressed through $2\times2$ Matrices of Clifford Numbers", *Complex Variables* 5 (1986), 215–224, for the Clifford realisation of the Möbius group.
