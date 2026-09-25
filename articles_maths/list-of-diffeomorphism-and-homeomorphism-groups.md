
# __List of Diffeomorphism and Homeomorphism Groups__

## Introduction

This article lists the groups of homeomorphisms, diffeomorphisms, mapping classes and birational maps that the corpus meets, together with the automorphism groups of a topological or a smooth structure. The property that the article gathers is that the group is a group of symmetries of a *structure* on a space rather than of a form or a distance, and the entries are grouped by the category in which the structure lives: topological, smooth, symplectic or algebraic. Every entry points to the article that introduces the group, and the article introduces nothing and proves nothing.

The unifying feature of the list is that the groups are typically infinite-dimensional and that the algebraic object studied is not the group itself but its connected components, its isotopy or homotopy type, or its quotient by the identity component. The mapping class group, the flux group and the Torelli group are the quotients and subgroups by which the large transformation groups are made tractable, and the homeomorphism group of the Cantor set is the one case in which the group itself is simple and the topological structure gives the complete invariant.

The article records examples and non-examples side by side. Beside the transformation groups it lists the groups that are only quotients of them, the groups that fail to be finite-dimensional Lie groups, and the groups whose elements are only locally defined, each with the failure named and the article that records it.

## Homeomorphism Groups

A homeomorphism group is the group of all self-homeomorphisms of a topological space, the $C^0$ member of the hierarchy of structure-preserving transformation groups.

| Group | The property it has | Introduced in |
|---|---|---|
| $\operatorname{Homeo}(X)$ | the group of all homeomorphisms $X \to X$, the $C^0$-ambient group | *Diffeomorphism Groups* |
| $\operatorname{Aut}(X)$ | the group of automorphisms of a structure on a set $X$, of which $\operatorname{Homeo}(X)$ is the topological case | *Transformation Groups* |
| $\operatorname{Sym}(X)$ | the group of all bijections, the automorphism group of a bare set | *Transformation Groups* |
| the symplectic homeomorphism group | the $C^0$-closure of $\operatorname{Ham}(M,\omega)$ in $\operatorname{Homeo}(M)$, a closed subgroup that is not a Lie group | *Diffeomorphism Groups*, §The $C^0$-Closure and the Rigidity |
| $\operatorname{Homeo}_0(S,\partial S)$ | the homeomorphisms of a surface isotopic to the identity relative to the boundary | *Mapping Class Groups* |

The homeomorphism group is the group whose quotient by its identity component is the mapping class group, and the difference between a homeomorphism and a diffeomorphism is invisible to the topology but visible to the smooth structure: the two groups have the same set of connected components on a smooth manifold but not the same local structure.

## Diffeomorphism Groups

A diffeomorphism group is the group of self-diffeomorphisms of a smooth manifold, the smooth member of the hierarchy, together with its structure-preserving subgroups.

| Group | The property it has | Introduced in |
|---|---|---|
| $\operatorname{Diff}(M)$ | the group of smooth diffeomorphisms $M \to M$ | *Diffeomorphism Groups* |
| $\operatorname{Diff}^k(M)$ | the group of $C^k$ diffeomorphisms | *Diffeomorphism Groups* |
| $\operatorname{Diff}_0(M)$ | the identity component, the diffeomorphisms isotopic to the identity | *Diffeomorphism Groups* |
| $\operatorname{Diff}^+(M)$ | the orientation-preserving diffeomorphisms, an index-two subgroup | *Diffeomorphism Groups* |
| $\operatorname{Diff}(M,\Omega)$ | the volume-preserving diffeomorphisms, $\mathcal{L}_X\Omega = 0$ | *Diffeomorphism Groups* |
| $\operatorname{Symp}(M,\omega)$ | the symplectomorphisms, the diffeomorphisms preserving a symplectic form | *Diffeomorphism Groups* |
| $\operatorname{Ham}(M,\omega)$ | the Hamiltonian group, the identity component of the group of exact symplectomorphisms | *Diffeomorphism Groups* |
| the Hofer metric $d_H$ | the metric on $\operatorname{Ham}(M,\omega)$ defined by the Hofer length | *Diffeomorphism Groups* |
| the flux homomorphism | the map from $\pi_0(\operatorname{Symp})$ to $H^1$, whose image is the flux group | *Diffeomorphism Groups* |
| the Virasoro cocycle | the cocycle on the Lie algebra of vector fields of the circle | *Diffeomorphism Groups* |

The Lie algebra of $\operatorname{Diff}(M)$ is the Lie algebra of vector fields, the exponential is the time-one map of the flow, and the group is the differentiable structure's own symmetry group; it is infinite-dimensional and its subgroups defined by a preserved structure — a volume form, a symplectic form, a contact form — recover the classical transformation groups of Part II. The Hofer metric and the flux homomorphism are the two invariants that survive the passage from the Lie algebra to the group and give the symplectomorphism group its large-scale geometry.

## The Mapping Class Group

The mapping class group is the group of isotopy classes of orientation-preserving homeomorphisms or diffeomorphisms of a surface, equivalently the component group of the orientation-preserving diffeomorphism group.

| Group | The property it has | Introduced in |
|---|---|---|
| $\operatorname{Mod}(S) = \pi_0\operatorname{Diff}^+(S)$ | the mapping class group of an oriented surface | *Mapping Class Groups* |
| $\operatorname{Mod}^{\pm}(S)$ | the extended mapping class group, including the orientation-reversing classes | *Mapping Class Groups* |
| a Dehn twist $T_a$ | the mapping class supported on an annulus about a simple closed curve | *Mapping Class Groups* |
| a pseudo-Anosov class | a class of stretch factor $\lambda > 1$, of positive topological entropy | *Mapping Class Groups* |
| the Torelli group $\mathcal{I}(S)$ | the kernel of the action on homology | *Mapping Class Groups* |
| the braid group $B_n = \operatorname{Mod}(D^2,n)$ | the mapping class group of the disk with $n$ marked points | *Mapping Class Groups*; *Braid Groups* |
| $Sp_{2g}(\mathbb{Z})$ | the target of the symplectic representation of $\operatorname{Mod}(S_g)$ | *Mapping Class Groups*; *The Unitary and Symplectic Groups* |
| the curve complex $\mathcal{C}(S)$ | the complex on which $\operatorname{Mod}(S)$ acts, encoding the Nielsen–Thurston classification | *Mapping Class Groups* |
| the mapping torus $M_f$ | the three-manifold of a mapping class, hyperbolic exactly for the pseudo-Anosov classes | *Mapping Class Groups*; *Low-Dimensional Topology* |

The mapping class group is the quotient of the homeomorphism group by its identity component, and the Nielsen–Thurston classification of its elements — finite order, reducible or pseudo-Anosov — is the surface analogue of the classification of the Möbius transformations. The Torelli group, the Johnson homomorphism and the Miller–Morita–Mumford classes measure the deviation of the group from its homology approximation, and the Dehn twists generate it.

## Birational Maps and Algebraic Automorphisms

In algebraic geometry the analogue of the diffeomorphism group is the group of birational maps, and for a smooth or topological structure there is in addition the automorphism group of the structure itself.

| Group | The property it has | Introduced in |
|---|---|---|
| the birational maps of a variety | the rational maps with a rational inverse, forming a group under composition | *Algebraic Geometry*, §Rational Maps, Function Fields and Birational Geometry |
| the automorphisms of a variety | the birational maps that are everywhere defined isomorphisms | *Algebraic Geometry* |
| the blow-up | the birational map replacing a subvariety by the projectivised normal directions | *Algebraic Geometry* |
| $\operatorname{Aut}_k(M_n(k)) \cong PGL_n(k)$ | the automorphism group of a matrix algebra, an algebraic transformation group | *Automorphisms and Derivations of Algebras* |
| $\operatorname{Aut}(G)$ | the group of automorphisms of a group, a transformation group of the underlying set | *Transformation Groups* |
| $\operatorname{Inn}(G) \cong G/Z(G)$ | the inner automorphisms, the image of the conjugation action | *Transformation Groups* |

The birational group is the algebraic analogue of the group of homeomorphisms of a compact manifold, but it is larger than the automorphism group of the variety and its elements are only partially defined: a birational map is an isomorphism on a dense open set and may contract or blow up a subvariety. The passage from the birational group to the automorphism group is the algebraic analogue of the passage from all homeomorphisms to those preserving the smooth structure, and the blow-up is the elementary move by which the two are related.

## The Cantor Set and the Thompson Groups

The homeomorphism group of the Cantor set is the one infinite transformation group of the list whose algebraic structure is simple, and its finitely generated subgroups — the Thompson groups — are the standard examples.

| Group | The property it has | Introduced in |
|---|---|---|
| the Cantor set | the compact, perfect, totally disconnected space of the corpus | *Symbolic Dynamics*; *Dimension Theory* |
| the full shift | a homeomorphism of the Cantor set, conjugate to the middle-third set | *Symbolic Dynamics* |
| the homeomorphism group of the Cantor set | the group of all self-homeomorphisms of the Cantor set, a simple group | *Thompson Groups and the Cantor Set* (planned) |
| Thompson's group $V$ | the finitely presented subgroup acting on the Cantor set by prefix replacement | *Thompson Groups and the Cantor Set* (planned) |
| Thompson's groups $F$ and $T$ | the subgroups acting on the interval and the circle; $T$ acts on the boundary of the disk | *Thompson Groups and the Cantor Set* (planned) |
| the stabiliser of a point of the Cantor set | the subgroup fixing a point, related to Thompson's group $F$ | *Thompson Groups and the Cantor Set* (planned) |

The Cantor set is the unique compact, perfect, totally disconnected metrisable space up to homeomorphism, so its homeomorphism group is a complete invariant of that class of space; the result, and the simplicity of the group, belong to the planned article, to which every entry of this section points. The relation to the rest of the list is that Thompson's group $V$ is a finitely presented group of homeomorphisms of a totally disconnected space, so it sits beside the mapping class groups as a group whose elements are transformations of a low-dimensional space.

## Warnings

An object that a reader may expect among the diffeomorphism and homeomorphism groups, and does not find, is recorded with the reason.

| Object | Why it is not listed as a diffeomorphism or homeomorphism group | Introduced in |
|---|---|---|
| $\operatorname{Diff}(M)$ as a finite-dimensional Lie group | it is infinite-dimensional, a Fréchet manifold, not a Lie group in the sense of the list | *Diffeomorphism Groups* |
| $\pi_0\operatorname{Diff}(S)$ | it is the mapping class group, recorded above as a quotient of $\operatorname{Diff}(S)$ rather than as that group | *Mapping Class Groups* |
| a birational map of $\mathbb{P}^2$ as an automorphism | it is only a rational map, defined on a dense open set | *Algebraic Geometry* |
| the orthogonal group $O(n)$ | defined by a form, it belongs to the classical groups rather than the structure-preserving groups | *Isometries and Orthogonal Transformations* |
| the general linear group $GL(n,\mathbb{R})$ | the automorphism group of a vector space, a finite-dimensional linear group | *The General Linear Group* |
| the isometry group $\operatorname{Isom}(M,g)$ | defined by a metric rather than by a structure on the space; it belongs to the isometry groups of the Riemannian list | *Riemannian Geometry*, §Isometries and the Myers–Steenrod Theorem |

## Summary

This article has listed the groups of homeomorphisms, diffeomorphisms, mapping classes and birational maps of the corpus. The homeomorphism groups open the list, with $\operatorname{Homeo}(X)$ as the $C^0$ member of the hierarchy and with the Cantor set as the space whose homeomorphism group is simple; the diffeomorphism groups follow, with $\operatorname{Diff}(M)$, its identity component, its orientation-preserving and volume-preserving subgroups, and the symplectomorphism and Hamiltonian groups with their flux and Hofer invariants; the mapping class group is the component group of the surface diffeomorphisms, with its Dehn twists, its pseudo-Anosov classes, its Torelli subgroup and its braid-group specialisation; and the birational and algebraic automorphism groups close the list. Beside the examples stand the non-examples: the diffeomorphism group is not a finite-dimensional Lie group, the mapping class group is a quotient of the diffeomorphism group and not the group itself, and a birational map is only locally defined.

## Summary of Notation

A catalogue denotes its objects by name rather than by symbol. The symbols that appear in the tables are the following, and they are the symbols of the articles that introduce them.

| Symbol | Meaning |
|---|---|
| $\operatorname{Homeo}(X)$, $\operatorname{Homeo}_0(S,\partial S)$ | Homeomorphism group; its identity component relative to the boundary |
| $\operatorname{Diff}(M)$, $\operatorname{Diff}^k(M)$, $\operatorname{Diff}_0(M)$, $\operatorname{Diff}^+(M)$ | Diffeomorphism group, its $C^k$ version, its identity component, its orientation-preserving subgroup |
| $\operatorname{Diff}(M,\Omega)$ | Volume-preserving diffeomorphisms |
| $\operatorname{Symp}(M,\omega)$, $\operatorname{Ham}(M,\omega)$ | Symplectomorphisms; Hamiltonian group |
| $d_H$, $\Gamma$ | Hofer metric; flux group |
| $\operatorname{Mod}(S)$, $\operatorname{Mod}^{\pm}(S)$, $\mathcal{I}(S)$ | Mapping class group, extended mapping class group, Torelli group |
| $T_a$, $\mathcal{C}(S)$ | Dehn twist; curve complex |
| $B_n$ | Braid group $= \operatorname{Mod}(D^2,n)$ |
| $\operatorname{Aut}(X)$, $\operatorname{Inn}(G)$, $\operatorname{Sym}(X)$ | Automorphism group of a structure; inner automorphisms; symmetric group |
| $V$, $F$, $T$ | Thompson groups (planned article) |
| $\mathbb{Z}$, $\mathbb{R}$ | The standard number systems of the corpus |
| $\operatorname{Isom}(M,g)$ | Isometry group of a metric, a Lie group by Myers–Steenrod |
| $\operatorname{Aff}(n)$ | The affine group, $GL(n)\ltimes\mathbb{R}^n$ |
| $\mathbb{P}^n$ | Projective space; the plane $\mathbb{P}^2$ of the birational maps |
| $\mathcal{L}_X$ | The Lie derivative along the field $X$ |

## Further Reading

- Augustin Banyaga, *The Structure of Classical Diffeomorphism Groups* (Kluwer, 1997), for the diffeomorphism groups, their subgroups and the flux homomorphism.
- Dusa McDuff and Dietmar Salamon, *Introduction to Symplectic Topology* (Oxford University Press, 3rd ed. 2017), for the symplectomorphism and Hamiltonian groups and the Hofer metric.
- Benson Farb and Dan Margalit, *A Primer on Mapping Class Groups* (Princeton University Press, 2012), for the mapping class group, the Dehn twists and the Nielsen–Thurston classification.
- James Belk, *The Structure of Thompson's Groups $F$ and $T$* (Ph.D. thesis, Cornell University, 2004), for the homeomorphism group of the Cantor set and the Thompson groups.
