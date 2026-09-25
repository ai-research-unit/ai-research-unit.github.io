
# __List of Erlangen Program Geometries__

## Introduction

This article lists the geometries of the corpus in the form in which Klein's principle presents them: a geometry is the study of the invariants of a transformation group, and a geometric object is a figure on which the group acts. The list gathers the transformation-group form of Euclidean, affine, projective, hyperbolic, conformal, Möbius and symplectic geometry, together with the further homogeneous geometries of the corpus, the correspondence between each geometry and its automorphism group, and the invariant that the group of each geometry preserves. Every entry points to the article that introduces the geometry or the group, and the article introduces nothing and proves nothing.

The organising relation is the correspondence between a geometry and its automorphism group: the group acts transitively on the space, the stabiliser of a point is the subgroup that fixes it, and the space is recovered as the coset space $G/H$. The Erlangen principle belongs to the planned article *Transformation Groups and the Erlangen Program*; its statement is named here and pointed to, and the general theory of transformation groups is that of *Transformation Groups*.

The article records examples and non-examples side by side. Beside the geometries that a transformation group describes it lists the geometric theories whose isometry group is too small to describe them, the structure groups of bundles that are not transformation groups of a space, and the groups that are defined by a form rather than by an action, each with the failure named and the article that records it.

## Klein's Principle and Transformation Groups

The principle states that a geometry is the study of the invariants of a transformation group, so that the group is the primary datum and the geometric notions are those the group preserves.

| Object | The property it has | Introduced in |
|---|---|---|
| Klein's principle (the Erlangen program) | a geometry is the study of the invariants of a transformation group | *Transformation Groups and the Erlangen Program* (planned) |
| a transformation group | a group acting faithfully on a set with structure, through a permutation representation | *Transformation Groups* |
| the action $G\times X \to X$ | the map organising the geometry, with orbits and stabilisers | *Transformation Groups* |
| the automorphism group $\operatorname{Aut}(X)$ | the group of automorphisms of a structure on $X$ | *Transformation Groups* |
| the orbit $\operatorname{Orb}(x)$ and stabiliser $\operatorname{Stab}(x)$ | the orbit and the point stabiliser, related by the orbit–stabiliser theorem | *Transformation Groups* |
| the coset space $G/H$ | a transitive $G$-set, the homogeneous form of a geometry | *Transformation Groups*; *Homogeneous Spaces* |
| a measure-preserving transformation group | a group of automorphisms of a measure space, whose invariant is the measure | *Ergodic Theory* |

The ideal of the principle is that every geometric notion is a notion invariant under the group and conversely that every invariant of the group has a geometric meaning. The two classical cases at the extremes are the symmetric group $\operatorname{Sym}(X)$, under which no nontrivial structure is invariant, and the full group of all homeomorphisms of a manifold, under which only the topological invariants are invariant; the geometries of the list are the intermediate cases in which a form, a distance or a conformal or projective structure is preserved.

## The Correspondence between a Geometry and its Automorphism Group

Each geometry of the list carries a group, and the geometry is recovered from the group together with the subgroup fixing a point.

| Geometry | The transformation group it is the invariant theory of | Introduced in |
|---|---|---|
| a homogeneous geometry | the pair $(G,H)$ of a group and a stabiliser, with the space $G/H$ | *Homogeneous Spaces* |
| the transitivity of a geometry | the group acts transitively, so the space is a single orbit | *Transformation Groups*; *Homogeneous Spaces* |
| the invariant of a geometry | a function or tensor on the space fixed by the group action | *Transformation Groups* |
| the group of a geometry | the automorphism group of the structure, recovered as $\operatorname{Aut}(X, \text{structure})$ | *Transformation Groups* |
| the linear model of a geometry | the isotropy representation at a point, a linear representation of $H$ | *Homogeneous Spaces* |

The correspondence is exact when the geometry is homogeneous and the automorphism group is the full structure-preserving group: the space is the coset space, the stabiliser is the isotropy subgroup, and the local geometry is the isotropy representation. The hierarchy $\operatorname{Sym}(X) \supset \operatorname{Aut}(X, \text{structure}) \supset \cdots$ of the transformation-group article is the ordering of the geometries from the weakest to the strongest structure.

## The Classical Geometries as Instances

The classical geometries are the standard instances of the principle, each with the group whose invariants it studies.

| Geometry | Its transformation group | Introduced in |
|---|---|---|
| Euclidean geometry | the Euclidean group $E(n) = \mathbb{R}^n \rtimes O(n)$ | *Euclidean Geometry* |
| affine geometry | the affine group $\operatorname{Aff}(n) = GL(n) \ltimes \mathbb{R}^n$ | *Affine Spaces and Translations* |
| projective geometry | the projective linear group $PGL(n+1,\mathbb{K})$ | *Projective Geometry* |
| hyperbolic geometry | the isometry group $O(n,1)$, orientation-preserving part $PSL(2,\mathbb{R})$ in dimension two | *Hyperbolic Geometry* |
| spherical geometry | the orthogonal group $O(n+1)$ | *Spherical Geometry* |
| conformal geometry | the conformal group $O(n+1,1)/\{\pm 1\}$ | *Conformal Geometry* |
| Möbius geometry | the Möbius group $\operatorname{Möb}(n) = O(n+1,1)/\{\pm 1\}$ | *Möbius and Lie Sphere Geometry* |
| symplectic geometry | the symplectic group $Sp(2n,\mathbb{R})$, preserving the form $\omega$ | *Symplectic Geometry*; *The Unitary and Symplectic Groups* |
| the linear classical geometry | the general linear group $GL(n,\mathbb{K})$ and its special, orthogonal, unitary and symplectic subgroups | *Matrix Groups and Classical Groups* |
| the geometry of a quadratic form | the orthogonal group $O(V,Q)$, the invariants of the form | *Isometries and Orthogonal Transformations* |

The instances are ordered by the size of the group: the general linear group gives the largest geometry and fewest invariants, the Euclidean and hyperbolic groups the metric geometries with distance and angle, the conformal group the angle alone, and the symplectic group a single alternating form. Each group is the automorphism group of the corresponding structure, so each geometry is the invariant theory of that group, which is the content of the principle.

## The Invariants of the Classical Geometries

The invariant that a geometry studies is the datum its group preserves, and the list of groups with their invariants is the concrete form of the Erlangen correspondence.

| Geometry | The invariant it studies | Introduced in |
|---|---|---|
| projective geometry | the cross ratio of four collinear points | *Projective Geometry*, §Coordinates, Frames and the Cross Ratio |
| Euclidean geometry | distance, angle, area and the congruence of figures | *Euclidean Geometry* |
| affine geometry | ratios of lengths on a line and the incidence of parallel lines | *Affine Spaces and Translations* |
| spherical geometry | the spherical distance and the spherical angle | *Spherical Geometry* |
| hyperbolic geometry | the hyperbolic distance and the hyperbolic angle | *Hyperbolic Geometry* |
| conformal geometry | the angle, preserved although the length is not | *Conformal Geometry* |
| Möbius geometry | the cross ratio of four points and the generalised spheres | *Möbius and Lie Sphere Geometry* |
| symplectic geometry | the symplectic form $\omega$ and the Hamiltonian vector field it defines | *Symplectic Geometry* |

The invariant theory of a geometry is not the whole of the geometry of that space: the differential geometry of a manifold uses the metric and its derivatives, which are not invariants of a finite-dimensional group, and the topological invariants are those of the homeomorphism group. The distinguishing feature of an Erlangen geometry is that its group is a finite-dimensional Lie group, so that its local invariants are finite in number and computable from the isotropy representation.

## Homogeneous Geometries Beyond the Classical List

The correspondence extends beyond the classical geometries to every space whose group acts transitively, with the stabiliser of a point supplying the local model.

| Geometry | Its transformation group | Introduced in |
|---|---|---|
| the geometry of a symmetric space | the isometry group $G$, with isotropy the fixed-point group $K$ of the geodesic symmetry | *Symmetric Spaces* |
| the geometry of a flag manifold | the general linear group acting transitively on the flags, with the parabolic stabilisers | *Flag Manifolds* |
| the geometry of a Grassmannian | the orthogonal or the general linear group acting transitively on the subspaces | *Grassmannians and Stiefel Manifolds* |
| the geometry of a reflection group | the group generated by the reflections in the walls of a chamber | *Coxeter Groups* |

Each of these is a homogeneous geometry in the exact sense of the principle: the space is the coset space of the group by the stabiliser, the invariant theory is the invariant theory of the group, and the local model is the isotropy representation. The symmetric spaces and the flag manifolds are the families in which the correspondence is developed in the corpus, and the reflection groups are the discrete counterpart, whose chambers are the fundamental domains of the group action.

## Warnings

An object that a reader may expect among the Erlangen program geometries, and does not find, is recorded with the reason.

| Object | Why it is not listed as an Erlangen geometry | Introduced in |
|---|---|---|
| the Riemannian geometry of a general manifold | its isometry group need not act transitively, so no transformation group describes it | *Riemannian Geometry*; *Homogeneous Spaces* |
| spin geometry and the group $\operatorname{Spin}(n)$ | a structure group of a bundle, not the transformation group of a space | *Spin Geometry*; *The Clifford, Pin and Spin Groups* |
| the orthogonal group $O(n)$ as a geometry | a group defined by a form; the geometry it belongs to is the orthogonal geometry of the form | *Isometries and Orthogonal Transformations* |
| the symplectomorphism group | the automorphisms of a symplectic manifold, generally larger than the finite-dimensional $Sp(2n,\mathbb{R})$ | *Diffeomorphism Groups*; *Symplectic Geometry* |
| the conformal group in dimension two | infinite-dimensional, so the invariant theory is not the finite-dimensional one | *Complex Analysis*; *Conformal Geometry* |

## Summary

This article has listed the geometries of the corpus in the form of Klein's principle. The principle and the transformation group open the list, with the action, the orbit, the stabiliser and the automorphism group; the correspondence between a geometry and its automorphism group follows, with the homogeneous space $G/H$ and the isotropy representation as the local model; the classical geometries are the instances, Euclidean, affine, projective, spherical, hyperbolic, conformal, Möbius and symplectic, each with the group whose invariants it studies; and the invariants themselves — the cross ratio, the distance and angle, the conformal angle, the symplectic form and the invariant measure — close it, and the homogeneous geometries beyond the classical list — the symmetric spaces, the flag manifolds, the Grassmannians and the reflection groups — show the correspondence at work outside it. Beside the examples stand the non-examples: a general Riemannian manifold has no transitive transformation group, spin geometry is a structure group rather than a transformation group, and the symplectomorphism group is larger than the finite-dimensional symplectic group.

## Summary of Notation

A catalogue denotes its objects by name rather than by symbol. The symbols that appear in the tables are the following, and they are the symbols of the articles that introduce them.

| Symbol | Meaning |
|---|---|
| $\operatorname{Sym}(X)$, $\operatorname{Aut}(X)$ | Symmetric group, automorphism group of a structure |
| $\operatorname{Orb}(x)$, $\operatorname{Stab}(x)$, $G/H$ | Orbit, stabiliser, coset space of a transitive action |
| $E(n)$ | The Euclidean isometry group, $\mathbb{R}^n\rtimes O(n)$ |
| $GL(n,\mathbb{K})$, $PGL(n+1,\mathbb{K})$ | General linear and projective linear groups |
| $O(n+1)$, $O(n,1)$, $O(n+1,1)$ | Spherical, hyperbolic and conformal groups |
| $\operatorname{Möb}(n) = O(n+1,1)/\{\pm 1\}$ | Möbius group |
| $Sp(2n,\mathbb{R})$, $\omega$ | Symplectic group and symplectic form |
| $O(V,Q)$ | Orthogonal group of a quadratic form |
| $\operatorname{Aff}(n)$ | The affine group, $GL(n)\ltimes\mathbb{R}^n$ |
| $\operatorname{Spin}(n)$ | The spin group, the double cover of $SO(n)$ |

## Further Reading

- Felix Klein, *Vergleichende Betrachtungen über neuere geometrische Forschungen* (Erlangen, 1872), for the original statement of the programme that defines a geometry by its transformation group.
- Felix Klein, *Vorlesungen über höhere Geometrie* (Springer, 1926), for the classical geometries and their transformation groups in the Erlangen form.
- Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry*, Volume II (Interscience, 1969), for the homogeneous spaces and the correspondence between a geometry and its automorphism group.
- Michael Artin, *Geometry* (Prentice Hall, 1991), for the classical geometries and their invariants in the transformation-group form.
