# __Real Structures on a Riemannian Manifold__

## Introduction

A **real structure** on a smooth manifold is a smooth involution, and its fixed points are the **real points**, the locus on which the involution acts trivially. On a Riemannian manifold the involution is required to be an isometry, and the metric then restricts the real points severely: they form a **totally geodesic** submanifold, the invariant metric descends to the quotient, and when the manifold also carries a complex structure the anti-holomorphic involutions — the ones that reverse the complex structure — have fixed sets of half the real dimension, the **real forms**. The real structure is thus the isometric involution read on the point set, and the real points are its fixed set.

The article develops the real structure on a Riemannian manifold. It defines the isometric involution and its real points, and proves that the real points are a disjoint union of totally geodesic submanifolds; it reads the differential at a real point as an orthogonal involution and the splitting of the tangent space, and shows that in the anti-holomorphic case the complex structure exchanges the two pieces, so that the real points have half the dimension and are totally real; it proves that the invariant metric descends to the quotient and that the quotient is a Riemannian manifold in the free case and a Riemannian orbifold with the image of the real points as singular locus otherwise; and it works the examples of the Euclidean conjugation, the real projective space inside the complex projective space and the real forms of the Grassmannians.

The article assumes the smooth real structure, the real points and the descent of the invariant structures from *Real Structures on a Smooth Manifold* of Part III, and the fixed set, the tube theorem and the quotient from *Isometric Involutions and the Fixed-Point Set* and *Isometric Involutions and the Two-Fold Quotient of a Riemannian Manifold* of this category. The complex structure, the holomorphic tangent bundle and the Hermitian metric are *Hermitian Geometry and Almost Complex Structures* in a later category of this Part, and *Real Structures on a Complex Manifold* there is the article that develops the anti-holomorphic involutions; both are named below as forward references, and the article states the compatibility condition and the Riemannian consequences without developing the holomorphic side. No physics is invoked.

## Isometric Real Structures

### Definition and Real Points

**Definition.** A **real structure** on a Riemannian manifold $(M, g)$ is an isometric involution,

$$
\sigma : M \longrightarrow M, \qquad \sigma^2 = \mathrm{id}, \qquad \sigma^*g = g,
$$

that is a smooth involution which is an isometry; its **real points** are the fixed points

$$
M^\sigma = \{x \in M : \sigma(x) = x\},
$$

and the real structure is **free** when $M^\sigma$ is empty. The involution is the isometric case of the smooth real structure of *Real Structures on a Smooth Manifold* of Part III, and the real points are its set of fixed points. The two-fold quotient $M/\sigma$ and the projection are those of the preceding article of this category.

**Proposition.** The real points form a subset of $M$ that is invariant under the isometry group commuting with $\sigma$, and the metric is invariant under the involution, so the linear isotropy at a real point preserves the splitting of the tangent space. The identity is a real structure whose real points are all of $M$, and an involution and its companion $\sigma\circ F$ for an isometry $F$ have the same type, the real points being carried by $F$.

**Proof.** The invariance of the real points under the commuting isometries and the invariance of the metric are the definitions; the statements about the identity and the companion are immediate, since $\sigma F$ is an involution exactly when $F$ commutes with $\sigma$, and then the real points correspond under $F$.

### The Real Points Are Totally Geodesic

**Theorem.** Each connected component of the real points $M^\sigma$ is a **totally geodesic** submanifold of $(M, g)$; at a real point $p$ the tangent space splits as

$$
T_pM = V_+\oplus V_-, \qquad d\sigma_p = +\mathrm{id}\ \text{on}\ V_+, \qquad d\sigma_p = -\mathrm{id}\ \text{on}\ V_-,
$$

with $V_+ = T_pM^\sigma$; the real points have codimension equal to the multiplicity of the eigenvalue $-1$ of $d\sigma_p$, they are the singular locus of the quotient $M/\sigma$, and the normal exponential map is a diffeomorphism onto a tubular neighbourhood on which the involution acts as $\xi\mapsto-\xi$.

**Proof.** This is the fixed-set theorem and the tube theorem of *Isometric Involutions and the Fixed-Point Set*, applied to the isometric involution $\sigma$. The metric enters only in the assertion that the components are totally geodesic, which is the fixed-geodesic argument: a geodesic with initial velocity in $V_+$ is fixed by $\sigma$ and remains in the real points.

**Corollary.** The real points of a real structure with a single real point are that point, and the real structure is a geodesic symmetry; the real points of a reflection in a hypersurface are the hypersurface; and the real structure of a compact manifold with no real point is a free involution, the quotient being a Riemannian manifold. The real points of the identity are the whole manifold, and those of the antipodal map of the sphere are empty.

## The Compatibility with a Complex Structure

### Holomorphic and Anti-Holomorphic Involutions

Suppose now that $M$ carries an **almost complex structure** $J$, a field of endomorphisms with $J^2 = -\mathrm{id}$, and that the metric is **Hermitian** for it, $g(JX, JY) = g(X, Y)$. The complex structure, the Hermitian metric and the fundamental form are the subject of *Hermitian Geometry and Almost Complex Structures* in a later category of this Part, and are named here as forward references; the field $J$ enters only through the following compatibility, and no holomorphic object is used. The differential of the real structure extends $\mathbb{C}$-linearly to the complexified tangent bundle, and the involution is **holomorphic** if it commutes with $J$ and **anti-holomorphic** if it anticommutes:

$$
\sigma\ \text{holomorphic} : \ d\sigma\circ J = J\circ d\sigma, \qquad
\sigma\ \text{anti-holomorphic} : \ d\sigma\circ J = -J\circ d\sigma.
$$

**Theorem.** Let $\sigma$ be an isometric real structure compatible with $J$ and let $p$ be a real point.

**(a)** If $\sigma$ is holomorphic, the eigenspaces $V_+$ and $V_-$ of $d\sigma_p$ are complex subspaces, $V_+$ is a complex submanifold and the real points are a complex submanifold when they are nonempty.

**(b)** If $\sigma$ is anti-holomorphic, the operator $J$ interchanges the eigenspaces, $J(V_+) = V_-$ and $J(V_-) = V_+$, so the two have the same dimension and the real points have half the real dimension of $M$, that is the dimension of the complex manifold; the real points are then **totally real**, $V_+\cap JV_+ = \{0\}$, and they are a **real form** of $M$.

**Proof.** For a holomorphic involution, $d\sigma_p$ commutes with $J$, so it preserves the complex structure of $T_pM$ and its eigenspaces are $J$-invariant, hence complex; the real points are then a complex submanifold by the fixed-set theorem applied in the holomorphic category. For an anti-holomorphic involution, if $v\in V_+$ then $Jv\in V_-$ because $d\sigma_p(Jv) = -Jd\sigma_p(v) = -Jv$, and symmetrically; the map $v\mapsto Jv$ is an isomorphism from $V_+$ onto $V_-$, so the dimensions agree and $\dim V_+ = \frac12\dim M$. Totally real means $V_+\cap JV_+ = \{0\}$, which holds because $V_+\cap V_-=0$; and a totally real submanifold of half the dimension is a real form by the definition of the smooth article.

**Corollary.** On a complex manifold of complex dimension $n$ the real points of an anti-holomorphic isometric involution have real dimension $n$ when they are nonempty; the real points of a holomorphic isometric involution are a complex submanifold of some complex dimension $k$ with $0 \leq k \leq n$. The geodesic symmetry at a point of a Hermitian manifold is holomorphic, since $-\mathrm{id}$ commutes with $J$, and its real points are the single point.

### The Differential and the Normal Bundle

**Proposition.** At a real point of an anti-holomorphic involution the normal bundle of the real points is the image of the tangent bundle under $J$, $\nu = J(TM^\sigma)$, and the differential induces the identification $V_- = JV_+$; the real points are therefore a **Lagrangian-like** totally real submanifold, in the sense that no nonzero tangent vector is a normal vector rotated by the complex structure. The complexified tangent space decomposes under the involution into the $(+1)$- and $(-1)$-eigenspaces of $d\sigma$, which the anti-holomorphic involution interchanges in a way that pairs the two types.

**Proof.** The normal bundle is $V_-$, and $V_- = JV_+$ by the theorem; the statement that $V_+\cap JV_+=\{0\}$ is total reality. The complexified statement is the eigenvalue computation of the previous theorem, the anti-holomorphic involution relating $T^{1,0}$ and $T^{0,1}$.

## The Quotient and the Descended Metric

**Theorem.** The invariant metric descends to the two-fold quotient: the quotient $M/\sigma$ carries the metric $g_\sigma$ with $\pi^*g_\sigma = g$, it is a Riemannian manifold when the real structure is free and a Riemannian orbifold with the image of the real points as singular locus otherwise, and the curvature of the quotient at a regular point is the curvature of $M$ at its preimages. The projection is a local isometry on the complement of the real points, and the quotient is locally modelled at the image of a real point by $V_+\times(V_-/\{\pm1\})$.

**Proof.** This is the quotient theorem of *Isometric Involutions and the Two-Fold Quotient of a Riemannian Manifold*; the only additional content of the present article is that the quotient inherits the complex structure when the involution is holomorphic, and does not when it is anti-holomorphic, the anti-holomorphic quotient being a real-analytic orbifold rather than a complex one.

**Remark.** An anti-holomorphic involution has no nonzero fixed tangent vector compatible with the complex structure in the holomorphic sense: the quotient $M/\sigma$ is not a complex manifold, and the real points are its boundary-like singular locus. The real structures on a complex manifold, the real forms, the real algebraic geometry of the real points and the quotients by the anti-holomorphic involutions are *Real Structures on a Complex Manifold* in a later category of this Part.

## Examples

**Example (the Euclidean conjugation).** On $\mathbb{C}^n$ with the Euclidean metric the conjugation $\sigma(z) = \bar z$ is an isometric, anti-holomorphic involution; its real points are $\mathbb{R}^n$, a totally geodesic real submanifold of half the dimension, and a real form of $\mathbb{C}^n$. The quotient $\mathbb{C}^n/\sigma$ is an orbifold with the image of $\mathbb{R}^n$ as its singular locus, and the invariant Euclidean metric descends to it; the quotient is not a complex manifold, the involution being anti-holomorphic rather than holomorphic.

**Example (the complex projective space).** On $\mathbb{CP}^n$ with the Fubini–Study metric the conjugation $\sigma([z]) = [\bar z]$ is an isometric, anti-holomorphic involution whose real points are the real projective space $\mathbb{RP}^n$; the inclusion $\mathbb{RP}^n\subseteq\mathbb{CP}^n$ is **totally geodesic** for the Fubini–Study metric, the real points have real dimension $n$, and they are a real form of the complex projective space. The same holds for the complex Grassmannian $\mathrm{Gr}_k(\mathbb{C}^n)$ with the conjugation induced by $\bar z$, whose real points are the real Grassmannian $\mathrm{Gr}_k(\mathbb{R}^n)$, a totally geodesic real form.

**Example (the sphere and the geodesic symmetry).** On the round sphere $S^n$ the reflection in a great subsphere is an isometric real structure whose real points are that subsphere, a real form of the sphere; the antipodal map is a free real structure, its quotient being $\mathbb{RP}^n$. The geodesic symmetry of a Riemannian manifold is the real structure with the single real point $p$, and it is the reason the real points of a general isometric involution include the degenerate case of a point.

## Summary

A **real structure** on a Riemannian manifold is an isometric involution $\sigma$; its **real points** $M^\sigma$ are the fixed points, and each connected component is a **totally geodesic** submanifold, by the fixed-geodesic argument, of codimension equal to the multiplicity of the eigenvalue $-1$ of the differential at a real point. The tangent space splits as $V_+\oplus V_-$, the involution acting as $+\mathrm{id}$ on $V_+ = T M^\sigma$ and $-\mathrm{id}$ on $V_-$; the real points are the singular locus of the two-fold quotient, and the normal exponential is a diffeomorphism onto a tube on which the involution is $\xi\mapsto-\xi$.

When the manifold carries a complex structure $J$ compatible with the metric, the real structure is **holomorphic** if it commutes with $J$ and **anti-holomorphic** if it anticommutes. A holomorphic isometric involution has complex eigenspaces and the real points are a complex submanifold; an anti-holomorphic one interchanges the eigenspaces by $J$, so the real points are totally real, of half the real dimension, and are a **real form**. The invariant metric descends to the quotient, which is a Riemannian manifold in the free case and a Riemannian orbifold with the image of the real points as singular locus otherwise; the anti-holomorphic quotient is a real-analytic orbifold, not a complex manifold. The conjugation of $\mathbb{C}^n$ has the real form $\mathbb{R}^n$; the conjugation of $\mathbb{CP}^n$ has the totally geodesic real form $\mathbb{RP}^n$; the real Grassmannian is the real form of the complex Grassmannian; and the geodesic symmetry is the real structure whose only real point is its centre. The holomorphic side is *Real Structures on a Complex Manifold* in a later category of this Part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma$, $\sigma^2=\mathrm{id}$, $\sigma^*g=g$ | Isometric real structure |
| $M^\sigma$ | Real points: the fixed set of the involution |
| Free real structure | No real point |
| $T_pM = V_+\oplus V_-$ | Fixed and normal directions at a real point |
| $V_+ = T_pM^\sigma$ | Tangent space of the real points |
| Totally geodesic | The real points are geodesically closed |
| $d\sigma\circ J = J\circ d\sigma$ | Holomorphic involution: complex real points |
| $d\sigma\circ J = -J\circ d\sigma$ | Anti-holomorphic involution: $J(V_+)=V_-$ |
| Totally real, real form | $V_+\cap JV_+=\{0\}$; real points of half the real dimension |
| $M/\sigma$, $g_\sigma$ | Two-fold quotient and the descended metric |
| Singular locus | The image of the real points in the quotient |

## Further Reading

- Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry, Volume II* (Interscience, 1969), for the real structures, the real forms and the anti-holomorphic involutions of a complex manifold.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (Academic Press, 1978), for the symmetric spaces, the real forms and the fixed sets of the involutions.
- Klaus Fritzsche and Hans Grauert, *From Holomorphic Functions to Complex Manifolds* (Springer, 2002), for the anti-holomorphic involutions and the real analytic subsets they fix.
- Armand Borel and Lizhen Ji, *Compactifications of Symmetric and Locally Symmetric Spaces* (Birkhäuser, 2006), for the real forms of the symmetric spaces and their totally geodesic embeddings.
- John M. Lee, *Introduction to Riemannian Manifolds*, 2nd ed. (Springer, 2018), for the isometric involutions, the invariant metrics and the quotients.
