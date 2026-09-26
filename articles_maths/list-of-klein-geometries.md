
# __List of Klein Geometries__

## Introduction

This article lists the geometries of the corpus that are given by a pair $(G,H)$ of a Lie group $G$ and a closed subgroup $H$, the geometry being the homogeneous space $G/H$ on which $G$ acts transitively. The list gathers the classical geometries — Euclidean, spherical, elliptic, hyperbolic, affine, projective, conformal and Möbius — together with the flag manifolds, the symmetric spaces and the maximal model geometries of Thurston, and it records the classification of the geometries of constant curvature and their space forms. Every entry points to the article that introduces the geometry, and the article introduces nothing and proves nothing.

The property that the article gathers is that the geometry is homogeneous: the space is the orbit of a single point under a group of transformations, and the subgroup $H$ is the stabiliser of that point. The object is the homogeneous space $G/H$, and the classical geometries are the cases in which $G$ is the isometry group of a form or the linear group of a projective space.

The article records examples and non-examples side by side. Beside the homogeneous spaces it lists the geometries whose isometry group does not act transitively, the coset spaces that fail to be manifolds because the subgroup is not closed, and the geometries that are only locally homogeneous, each with the failure named and the article that records it.

## The Pairs and the Homogeneous Space

A homogeneous space is a manifold $G/H$ on which the Lie group $G$ acts transitively with stabiliser $H$; the tangent space at the identity coset carries the isotropy representation of $H$, and the geometry of $G/H$ is the study of the $G$-invariant structures it carries.

| Object | The property it has | Introduced in |
|---|---|---|
| the pair $(G,H)$ | a Lie group and a closed subgroup, the data of the geometry | *Homogeneous Spaces* |
| the homogeneous space $G/H$ | the orbit space of the transitive action, of dimension $\dim G - \dim H$ | *Homogeneous Spaces* |
| the orbit map $\theta_p(g) = g\cdot p$ | the surjection $G \to G/H$ exhibiting the principal $H$-bundle | *Homogeneous Spaces* |
| the isotropy representation | the linear action of $H$ on the tangent space $T_{eH}(G/H)$ | *Homogeneous Spaces* |
| the reductive decomposition $\mathfrak{g} = \mathfrak{h}\oplus\mathfrak{m}$ | the splitting with $[\mathfrak{h},\mathfrak{m}] \subseteq \mathfrak{m}$, carrying the geometry | *Homogeneous Spaces* |
| the $G$-invariant metric on $G/H$ | the metric determined by an $\operatorname{Ad}(H)$-invariant inner product on $\mathfrak{m}$ | *Homogeneous Spaces* |
| the isometry group $\operatorname{Isom}(M,g)$ | a Lie group by Myers–Steenrod, the ambient group of a geometry | *Homogeneous Spaces* |

The isotropy representation is the linear data that survives the passage from the pair $(G,H)$ to the space, and the invariant metric, the invariant complex structure and the invariant forms are all determined by invariant tensors on the tangent space at a single point. The transitivity is the whole content of the homogeneous case: it reduces the local differential geometry of the space to the linear algebra of $\mathfrak{g}$, $\mathfrak{h}$ and $\mathfrak{m}$.

## The Classical Geometries

The classical geometries of Part II are the cases of the construction in which $G$ is an isometry group, a linear group or a conformal group.

| Geometry | The homogeneous space it is | Introduced in |
|---|---|---|
| Euclidean geometry | $\mathbb{R}^n = E(n)/O(n)$, of curvature zero | *Euclidean Geometry*; *Homogeneous Spaces* |
| spherical geometry | $S^n = O(n+1)/O(n)$, of curvature $+1$ | *Spherical Geometry*; *Homogeneous Spaces* |
| elliptic geometry | the quotient $S^n/\{\pm 1\}$ of the sphere by the antipodal map | *Spherical Geometry*, §Elliptic Geometry |
| hyperbolic geometry | $\mathbf{H}^n = SO(n,1)/SO(n)$, of curvature $-1$ | *Hyperbolic Geometry*; *Homogeneous Spaces* |
| non-Euclidean geometry | the spherical and hyperbolic geometries in the classical opposition to the Euclidean | *Non-Euclidean Geometry* |
| affine geometry | the affine space $\mathbb{A}^n = \operatorname{Aff}(n)/GL(n)$ | *Affine Spaces and Translations* |
| projective geometry | $\mathbb{P}^n = PGL(n+1)/P$ with $P$ the stabiliser of a flag | *Projective Geometry* |
| conformal geometry | the conformal sphere $S^n = O(n+1,1)/P$ with $P$ a parabolic subgroup | *Conformal Geometry* |
| Möbius geometry | the sphere $S^n$ with the Möbius group $O(n+1,1)/\{\pm 1\}$ | *Möbius and Lie Sphere Geometry* |
| Lie sphere geometry | the quadric of the oriented spheres, with group $PO(n+1,2)$ | *Möbius and Lie Sphere Geometry* |
| the Grassmannian $\mathrm{Gr}_k(\mathbb{R}^n)$ | $O(n)/(O(k)\times O(n-k))$, a homogeneous space of $O(n)$ | *Grassmannians and Stiefel Manifolds*; *Homogeneous Spaces* |
| the flag manifold $F\ell_n(\mathbb{K})$ | $GL(n,\mathbb{K})/B$ with $B$ the Borel subgroup of upper triangular matrices | *Flag Manifolds* |
| real projective space $\mathbb{RP}^n$ | $O(n+1)/(O(1)\times O(n))$, the Grassmannian of lines | *Projective Geometry*; *Grassmannians and Stiefel Manifolds* |
| the Stiefel manifold $V_k(\mathbb{R}^n)$ | $O(n)/O(n-k)$, the manifold of orthonormal $k$-frames | *Grassmannians and Stiefel Manifolds* |

Each geometry is read from its pair: the Euclidean geometry from the Euclidean group and the orthogonal stabiliser, the projective from the general linear group and a parabolic subgroup, the conformal from the pseudo-orthogonal group of a form of signature $(n+1,1)$. The generalised flag manifolds $G/P$ for a parabolic subgroup $P$ of a semisimple group are the geometries of the corresponding incidence structures, and they are the standard parabolic cases of the construction.

## The Geometries of Constant Curvature and the Space Forms

The geometries of constant curvature are the three model geometries, and their quotients by discrete groups are the space forms.

| Object | The property it has | Introduced in |
|---|---|---|
| the three model geometries | the complete simply connected manifolds of constant curvature $+1$, $0$, $-1$ | *Curvature and Geodesics* |
| the space-form theorem | every complete connected manifold of constant curvature is a quotient of a model | *Riemannian Geometry*; *Curvature and Geodesics* |
| a spherical space form | a quotient $S^n/\Gamma$ with $\Gamma$ a finite free subgroup of $O(n+1)$ | *Spherical Geometry*, §Spherical Space Forms |
| a hyperbolic space form | a quotient $\mathbf{H}^n/\Gamma$ by a free discrete group of isometries | *Hyperbolic Geometry*, §Hyperbolic Space Forms and the Trichotomy |
| a Euclidean space form | a compact flat manifold, the quotient of $\mathbb{R}^n$ by a torsion-free crystallographic group | *Symmetry, Point and Crystallographic Groups*; *Riemannian Geometry* |
| the spherical space form problem | the classification of the finite free orthogonal actions, of which the lens spaces are the three-dimensional cases | *Low-Dimensional Topology*; *Lens Spaces* |
| the lens spaces $L(p,q)$ | the quotients $S^3/(\mathbb{Z}/p)$ by a free cyclic action | *Lens Spaces* |
| the trichotomy of curvature | the division of the constant-curvature geometries by the sign of the curvature | *Curvature and Geodesics*; *Euclidean Geometry* |

The space-form theorem is proved by the comparison theory of the curvature, and it is the reason the geometries of constant curvature are exhausted by the three models and their discrete quotients. The spherical case is rigid and finite, the Euclidean case is classified by the Bieberbach theorems and finite in each dimension, and the hyperbolic case is the richest: its lattices deform in dimension two and are rigid in higher dimensions, which is the dichotomy recorded in the list of discrete geometric groups.

## The Maximal Model Geometries

Thurston's geometries are the maximal pairs $(X,G)$ of a simply connected space and a transitive group with compact stabilisers, and they are the geometries with which the low-dimensional classification is stated.

| Object | The property it has | Introduced in |
|---|---|---|
| a model geometry $(X,G)$ | a simply connected Riemannian manifold with a transitive group $G$ maximal among those with compact stabilisers | *Low-Dimensional Topology*, §Geometrisation and the Eight Model Geometries |
| the eight three-dimensional model geometries | $S^3$, $E^3$, $\mathbf{H}^3$, $S^2\times\mathbb{R}$, $\mathbf{H}^2\times\mathbb{R}$, $\widetilde{SL_2(\mathbb{R})}$, $\mathrm{Nil}$, $\mathrm{Sol}$ | *Low-Dimensional Topology*, §Geometrisation and the Eight Model Geometries |
| a geometric three-manifold | a quotient $X/\Gamma$ by a free properly discontinuous discrete group | *Low-Dimensional Topology* |
| the geometrisation theorem | every closed three-manifold decomposes into geometric pieces | *Low-Dimensional Topology*; *Ricci Flow* |
| the Seifert fibred and hyperbolic pieces | the two kinds of piece into which the torus decomposition splits a three-manifold | *Low-Dimensional Topology* |

In dimension two there are three model geometries, the spherical, Euclidean and hyperbolic, and they are the three cases of the trichotomy; in dimension three there are eight, the three of constant curvature together with the five product, fibre and solvable cases. The model geometry is a homogeneous space with a prescribed transitive group, and it is the form in which the uniformisation theorem and its three-dimensional analogue are stated.

## Symmetric Spaces and Parabolic Geometries

A symmetric space is a homogeneous space $G/H$ in which the stabiliser is the fixed-point set of an involution of $G$, and it is the case of the construction in which the curvature is parallel.

| Object | The property it has | Introduced in |
|---|---|---|
| a symmetric space $G/H$ | a homogeneous space with a Cartan involution $\sigma$ of $G$ whose fixed group is $H$ | *Symmetric Spaces* |
| the symmetric pair $(\mathfrak{g},\sigma)$ | the Lie algebra with the involution splitting $\mathfrak{g} = \mathfrak{h}\oplus\mathfrak{m}$ | *Symmetric Spaces* |
| a compact or noncompact symmetric space | the sign of the curvature, decided by the sign of the invariant form | *Symmetric Spaces* |
| the rank of a symmetric space | the dimension of a maximal flat totally geodesic submanifold | *Symmetric Spaces*; *Homogeneous Spaces* |
| a Hermitian symmetric space | a symmetric space with a parallel invariant complex structure | *Symmetric Spaces* |
| a locally symmetric space | a quotient of a symmetric space by a discrete group; equivalently $\nabla R = 0$ | *Symmetric Spaces* |
| the building at infinity of a symmetric space | the spherical building whose chambers are the Weyl chambers at infinity | *Buildings and Tits Systems*, §Trees and the Buildings at Infinity |

The symmetric spaces are the homogeneous spaces whose isotropy representation is the restriction of an involution, so that the geodesic symmetry at each point extends to a global symmetry; they are the geometries of constant curvature in rank one and the Hermitian, quaternionic and exceptional geometries above, and their classification is the classification of the real forms of the simple Lie algebras.

## Warnings

An object that a reader may expect among the Klein geometries, and does not find, is recorded with the reason.

| Object | Why it is not listed as a Klein geometry | Introduced in |
|---|---|---|
| a general Riemannian manifold | its isometry group need not act transitively, so it is not homogeneous | *Riemannian Geometry*; *Homogeneous Spaces* |
| a coset space $G/H$ with $H$ not closed | the quotient is not Hausdorff and not a manifold | *Homogeneous Spaces* |
| the flat torus and the Klein bottle | compact flat manifolds, quotients $\mathbb{R}^n/\Gamma$ of the Euclidean model by a discrete group rather than the model geometry $E(n)/O(n)$ itself | *Symmetry, Point and Crystallographic Groups*; *Low-Dimensional Topology* |
| the unit tangent bundle $SM$ | a manifold associated with a geometry, carrying the geodesic flow, not itself a Klein geometry | *The Geodesic Flow* |
| a locally homogeneous manifold | only its universal cover is a homogeneous space | *Homogeneous Spaces* |

## Summary

This article has listed the geometries of the corpus that are homogeneous spaces $G/H$ of a Lie group by a closed subgroup. The pairs and their invariant data open the list; the classical geometries follow, with Euclidean space $E(n)/O(n)$, the sphere $O(n+1)/O(n)$, the elliptic and hyperbolic geometries, the affine and projective spaces, the conformal and Möbius geometries, the Lie sphere geometry, and the Grassmannian, Stiefel and flag manifolds as homogeneous spaces of the orthogonal and general linear groups; the geometries of constant curvature and their space forms, spherical, Euclidean, hyperbolic and lens, are recorded with the space-form theorem; the eight maximal model geometries of Thurston are gathered with the geometries of low-dimensional topology; and the symmetric spaces close the list. Beside the examples stand the non-examples: a general Riemannian manifold is not homogeneous, a coset space by a non-closed subgroup is not a manifold, and the compact flat manifolds are quotients of a model rather than Klein geometries in the strict sense.

## Summary of Notation

A catalogue denotes its objects by name rather than by symbol. The symbols that appear in the tables are the following, and they are the symbols of the articles that introduce them.

| Symbol | Meaning |
|---|---|
| $G/H$, $\mathfrak{g}$, $\mathfrak{h}$, $\mathfrak{m}$ | Homogeneous space, Lie algebra, isotropy algebra, isotropy complement |
| $E(n)$, $O(n)$, $SO(n)$ | Euclidean and orthogonal groups |
| $\mathbb{R}^n$, $S^n$, $\mathbf{H}^n$, $\mathbb{A}^n$, $\mathbb{P}^n$ | Euclidean, spherical, hyperbolic, affine and projective spaces |
| $O(n+1,1)$, $SO(n,1)$ | Conformal and hyperbolic isometry groups |
| $O(n+1,1)/\{\pm 1\}$, $PO(n+1,2)$ | Möbius group; Lie sphere group |
| $\mathrm{Gr}_k(\mathbb{R}^n)$, $V_k(\mathbb{R}^n)$, $F\ell_n(\mathbb{K})$ | Grassmannian, Stiefel manifold, flag manifold |
| $S^n/\Gamma$, $\mathbf{H}^n/\Gamma$, $L(p,q)$ | Spherical and hyperbolic space forms; lens space |
| $S^3$, $E^3$, $\mathbf{H}^3$, $S^2\times\mathbb{R}$, $\mathbf{H}^2\times\mathbb{R}$, $\widetilde{SL_2(\mathbb{R})}$, $\mathrm{Nil}$, $\mathrm{Sol}$ | The eight three-dimensional model geometries |
| $(\mathfrak{g},\sigma)$, rank | Symmetric pair and rank of a symmetric space |
| $\mathbb{Z}$ | The standard number systems of the corpus |
| $\operatorname{Isom}(M,g)$ | Isometry group of a metric, a Lie group by Myers–Steenrod |
| $\operatorname{Aff}(n)$ | The affine group, $GL(n)\ltimes\mathbb{R}^n$ |
| $\operatorname{Ad}(H)$ | The adjoint action of the isotropy group on $\mathfrak{m}$ |

## Further Reading

- Felix Klein, *Vorlesungen über höhere Geometrie* (Springer, 1926), for the classical geometries as homogeneous spaces and the classification of the geometries of constant curvature.
- Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry*, Volume II (Interscience, 1969), for the homogeneous spaces, the isotropy representation and the invariant connections.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (American Mathematical Society, 2001), for the homogeneous spaces, the symmetric spaces and their classification.
- William P. Thurston, *Three-Dimensional Geometry and Topology*, Volume 1 (Princeton University Press, 1997), for the eight model geometries and the geometric structures on three-manifolds.
