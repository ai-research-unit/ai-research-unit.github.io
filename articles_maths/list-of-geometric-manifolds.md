
# __List of Geometric Manifolds__

## Introduction

This article lists the manifolds and smooth structures that the corpus meets, with the data that separate them: their dimension, their curvature and their invariants. The list gathers the model spaces of constant curvature, the surfaces and the manifolds of dimension three and four, the complex, Kähler, quaternionic and exceptional-holonomy manifolds, the homogeneous and symmetric spaces, the space forms and the compact flat manifolds, and the smooth structures of the exotic phenomena. Every entry points to the article that introduces the manifold, and the article introduces nothing and proves nothing.

The manifolds of the list are geometric manifolds: they carry a metric, a complex structure, a form or a holonomy reduction that is stated in the entry, and the invariants recorded beside each are the ones the corpus computes for it, among them the Euler characteristic, the Betti and Hodge numbers, the signature and the fundamental group. The dimension is the first division of the list, because the classification of manifolds changes character at each of the low dimensions, and the curvature is the second, because the constant-curvature and holonomy-reduced cases are the ones the corpus treats in full.

The article records examples and non-examples side by side. Beside the manifolds it lists the compact spaces that fail to be manifolds, the manifolds that are homeomorphic but not diffeomorphic, and the exotic smooth structures, each with the failure named and the article that records it.

## The Model Manifolds and the Space Forms

The model manifolds are the complete simply connected manifolds of constant curvature, and the space forms are their quotients by discrete groups.

| Manifold | Dimension | Curvature | Invariants | Introduced in |
|---|---|---|---|---|
| $\mathbb{R}^n$ | $n$ | $0$ | contractible; Euler characteristic $1$ | *Euclidean Geometry*; *Smooth Manifolds and Differential Geometry* |
| $S^n$ | $n$ | $+1$ | compact, simply connected; $\chi = 1 + (-1)^n$ | *Spherical Geometry* |
| $\mathbf{H}^n$ | $n$ | $-1$ | contractible; infinite volume | *Hyperbolic Geometry* |
| $\mathbb{RP}^n$ | $n$ | $+1$ | $\pi_1 = \mathbb{Z}/2$; non-orientable for even $n$ | *Smooth Manifolds and Differential Geometry*; *Projective Geometry* |
| $\mathbb{CP}^n$ | $2n$ | positive | $h^{p,p} = 1$; $\chi = n+1$ | *Kähler Geometry* |
| $\mathbb{HP}^n$ | $4n$ | positive | quaternionic Kähler; $\chi = n+1$ | *Quaternionic Geometry* |
| the $n$-torus $T^n$ | $n$ | $0$ | $\pi_1 = \mathbb{Z}^n$; $\chi = 0$ | *Smooth Manifolds and Differential Geometry*; *Symmetry, Point and Crystallographic Groups* |
| the Klein bottle | $2$ | $0$ | non-orientable; $\chi = 0$ | *Symmetry, Point and Crystallographic Groups* |
| a spherical space form $S^n/\Gamma$ | $n$ | $+1$ | $\pi_1 = \Gamma$ finite; $\chi = \lvert\Gamma\rvert^{-1}\chi(S^n)$ | *Spherical Geometry*, §Spherical Space Forms |
| a hyperbolic space form $\mathbf{H}^n/\Gamma$ | $n$ | $-1$ | $\pi_1 = \Gamma$; rigidity in dimension $\geq 3$ | *Hyperbolic Geometry*, §Hyperbolic Space Forms and the Trichotomy |
| a compact flat manifold | $n$ | $0$ | torsion-free crystallographic fundamental group | *Symmetry, Point and Crystallographic Groups* |
| the lens space $L(p,q)$ | $3$ | $+1$ | $\pi_1 = \mathbb{Z}/p$; linking form $q^*/p$ | *Lens Spaces* |
| a nilmanifold $N/\Gamma$ | varies | — | lattice quotient of a nilpotent group; left-invariant metric | *Lattices in Lie Groups* |

The model spaces are the three of constant curvature together with the complex and quaternionic projective spaces; the space forms are their quotients, and the space-form theorem makes the constant-curvature cases exhaustive. The compact flat manifolds are the quotients by the torsion-free crystallographic groups, of which there are two in dimension two and ten in dimension three.

## Surfaces

A surface is a manifold of dimension two, classified by its genus, its orientability and its number of boundary components, and carrying a complete constant-curvature metric by uniformisation.

| Surface | Euler characteristic | Curvature | Invariants | Introduced in |
|---|---|---|---|---|
| the sphere $S^2$ | $2$ | $+1$ | $\pi_1$ trivial; the unique simply connected closed surface | *Spherical Geometry*; *Low-Dimensional Topology* |
| the torus $T^2$ | $0$ | $0$ | $\pi_1 = \mathbb{Z}^2$; abelian | *Low-Dimensional Topology* |
| the real projective plane $\mathbb{RP}^2$ | $1$ | $+1$ | non-orientable; the quotient of $S^2$ | *Low-Dimensional Topology* |
| the closed orientable surface of genus $g \geq 2$ | $2 - 2g$ | $-1$ | hyperbolic; mapping class group of virtual cohomological dimension $4g-5$ | *Low-Dimensional Topology*; *Mapping Class Groups* |
| the connected sum $M\# N$ | $\chi(M) + \chi(N) - 2$ | — | the connected-sum operation of the classification | *Low-Dimensional Topology* |
| a compact surface with boundary | $\chi$ and $\pi_1$ free | — | classified by $\chi$, orientability and boundary count | *Low-Dimensional Topology* |
| a Riemann surface | $2 - 2g$ | $-1$ for $g \geq 2$ | complex structure; moduli space of dimension $3g-3$ | *Algebraic Curves*; *Moduli Spaces* |

Every closed surface admits exactly one of the three geometries according to the sign of $\chi$: the sphere the spherical, the torus and the Klein bottle the Euclidean, and the surfaces of genus at least two the hyperbolic. The Euler characteristic and the orientability are the complete invariants of the closed case, and the uniformisation theorem realises the geometric structure.

## Manifolds in Dimension Three and Four

In dimension three the classification is by decomposition into geometric pieces, and in dimension four the topological and smooth classifications diverge.

| Manifold | Dimension | Curvature | Invariants | Introduced in |
|---|---|---|---|---|
| a closed three-manifold | $3$ | piecewise geometric | prime and torus decomposition; the eight geometries | *Low-Dimensional Topology*, §Geometrisation and the Eight Model Geometries |
| a Seifert fibred manifold | $3$ | one of six geometries | circle fibration with exceptional fibres | *Low-Dimensional Topology* |
| the figure-eight knot complement | $3$ | $-1$ | hyperbolic volume $2.0298832\ldots$ | *Low-Dimensional Topology* |
| the Weeks manifold | $3$ | $-1$ | minimal volume $0.94270736\ldots$ | *Low-Dimensional Topology* |
| a simply connected four-manifold | $4$ | — | intersection form; classification by Freedman | *Low-Dimensional Topology*, §Four-Manifolds and the Intersection Form |
| $\mathbb{CP}^2$ and $\overline{\mathbb{CP}^2}$ | $4$ | — | intersection forms of rank $1$ | *Low-Dimensional Topology*; *Kähler Geometry* |
| a $K3$ surface | $4$ | Ricci-flat | $b_2 = 22$, $h^{1,1} = 20$, $\chi = 24$ | *Calabi–Yau Manifolds* |
| a Calabi–Yau threefold | $6$ | Ricci-flat | Hodge numbers $h^{1,1}, h^{2,1}$; $c_1 = 0$ | *Calabi–Yau Manifolds* |
| a homotopy sphere $\Sigma \in \Theta_n$ | $n$ | — | $\Theta_n$ class; bounding obstruction $bP_{n+1}$ | *Cobordism and Surgery Theory* |
| a spin manifold | $n$ | — | spin structure; $\hat A$-genus; Dirac operator | *Spin Geometry* |

The three-dimensional case is governed by Thurston's geometrisation theorem, proved by Perelman's Ricci flow, so that every closed three-manifold decomposes into pieces each of which is the quotient of one of the eight model geometries. The four-dimensional case is exceptional: the topological classification of the simply connected case is Freedman's, by the intersection form, while the smooth classification is obstructed by the gauge-theoretic invariants of Donaldson and Seiberg–Witten, and the two do not agree.

## Complex, Kähler and of Special Holonomy

The manifolds with a reduced holonomy carry the richest invariants of the list, and their classification is the classification of the holonomy groups.

| Manifold | Dimension | Holonomy | Invariants | Introduced in |
|---|---|---|---|---|
| a complex manifold | $2n$ | $GL(n,\mathbb{C})$ | complex structure $J$; Dolbeault cohomology | *Kähler Geometry* |
| a Kähler manifold | $2n$ | $U(n)$ | Hodge numbers $h^{p,q}$; Kähler form $\Omega$ | *Kähler Geometry* |
| a Calabi–Yau manifold | $2n$ | $SU(n)$ | $c_1 = 0$; holomorphic volume form | *Calabi–Yau Manifolds* |
| a hyperkähler manifold | $4n$ | $Sp(n)$ | three Kähler forms; Ricci-flat | *Hyperkähler Geometry* |
| a quaternionic Kähler manifold | $4n$ | $Sp(n)\cdot Sp(1)$ | Einstein; twistor space | *Quaternionic Geometry* |
| a $G_2$-manifold | $7$ | $G_2$ | associative $3$-form; $\chi = 0$ for full holonomy | *G2 and Spin(7) Manifolds* |
| a $\mathrm{Spin}(7)$-manifold | $8$ | $\mathrm{Spin}(7)$ | Cayley $4$-form; $\hat A$-genus | *G2 and Spin(7) Manifolds* |
| a symmetric space $G/H$ | varies | $H$ | $\nabla R = 0$; rank and restricted roots | *Symmetric Spaces* |
| a Grassmannian $\mathrm{Gr}_k(\mathbb{R}^n)$ | $k(n-k)$ | — | compact symmetric space of rank $\min(k,n-k)$ | *Grassmannians and Stiefel Manifolds* |
| a flag manifold $F\ell_n(\mathbb{C})$ | $2\binom{n}{2}$ | — | Euler characteristic $n!$; Schubert cells | *Flag Manifolds* |

The holonomy reduction is the organising principle: the Berger list of holonomy groups gives the possible parallel structures, and each row of the table is the manifold of one holonomy group. The Calabi–Yau, hyperkähler, quaternionic Kähler, $G_2$ and $\mathrm{Spin}(7)$ manifolds are the Ricci-flat or Einstein cases, and they are the manifolds of the exceptional and special-holonomy families of the corpus.

## Smooth Structures and Exotic Phenomena

A topological manifold may carry several smooth structures, and the corpus records the cases in which the smooth classification differs from the topological one.

| Object | The property it has | Introduced in |
|---|---|---|
| a smooth structure on a topological manifold | a maximal compatible atlas, classifying the smooth manifolds | *Smooth Manifolds and Differential Geometry* |
| an exotic sphere | a homotopy sphere homeomorphic but not diffeomorphic to $S^n$ | *Cobordism and Surgery Theory* |
| the group $\Theta_n$ of homotopy spheres | the oriented homotopy $n$-spheres under connected sum, finite for $n \neq 4$ | *Cobordism and Surgery Theory* |
| an exotic $\mathbb{R}^4$ | a smooth structure on $\mathbb{R}^4$ not diffeomorphic to the standard one | *Low-Dimensional Topology* |
| the failure of the $h$-cobordism theorem in dimension four | the obstruction that makes dimension four exceptional | *Low-Dimensional Topology* |
| a wild manifold | a space that is not a manifold but shares some of its properties | *Wild and Exotic Manifolds* (planned) |
| the Alexander horned sphere | a sphere embedded in $\mathbb{R}^3$ whose complement is not simply connected | *Wild and Exotic Manifolds* (planned) |
| the Whitehead manifold | contractible but not homeomorphic to $\mathbb{R}^3$ | *Wild and Exotic Manifolds* (planned) |

The exotic spheres are detected by the surgery obstruction and the $bP_{n+1}$ computation, and the exotic smooth structures on $\mathbb{R}^4$ are the phenomenon that makes dimension four alone among the Euclidean spaces exceptional. The wild objects are the non-manifolds and the non-standard embeddings that share some property of the manifolds; they are treated in the planned article, to which the last rows point.

## Warnings

An object that a reader may expect among the geometric manifolds, and does not find, is recorded with the reason.

| Object | Why it is not listed as a geometric manifold | Introduced in |
|---|---|---|
| the topologist's sine curve | not a manifold at any point of the limiting segment | *Continuum Theory* |
| the Warsaw circle | a compact connected space that is not a manifold | *Continuum Theory* |
| the pseudo-arc | a hereditarily indecomposable continuum, not a manifold | *Continuum Theory* |
| the long line | locally Euclidean but not second countable, so outside the definition used here | *Paracompactness and Partitions of Unity* |
| the comb space | not locally connected and not a manifold | *Continuum Theory*, §Peano Continua |
| the solenoid | an indecomposable continuum, not a manifold | *Continuum Theory*, §The Standard Indecomposable Continua |

## Summary

This article has listed the manifolds and smooth structures of the corpus, with their dimension, curvature and invariants. The model manifolds and the space forms open the list, from $\mathbb{R}^n$, $S^n$ and $\mathbf{H}^n$ to the projective spaces, the tori, the flat manifolds and the lens spaces; the surfaces follow, classified by genus and Euler characteristic and uniformised by the three geometries; the three- and four-dimensional cases are recorded with geometrisation, the eight model geometries and the intersection form; the complex, Kähler, Calabi–Yau, hyperkähler, quaternionic and exceptional-holonomy manifolds are gathered by their holonomy; and the smooth structures close the list with the exotic spheres, the exotic $\mathbb{R}^4$ and the wild objects. Beside the examples stand the non-examples: the topologist's sine curve, the Warsaw circle, the pseudo-arc, the long line, the comb space and the solenoid each fail a defining property of a manifold, with the failure named.

## Summary of Notation

A catalogue denotes its objects by name rather than by symbol. The symbols that appear in the tables are the following, and they are the symbols of the articles that introduce them.

| Symbol | Meaning |
|---|---|
| $\mathbb{R}^n$, $S^n$, $\mathbf{H}^n$, $T^n$, $\mathbb{RP}^n$, $\mathbb{CP}^n$, $\mathbb{HP}^n$ | Euclidean space, sphere, hyperbolic space, torus, projective spaces |
| $S^n/\Gamma$, $\mathbf{H}^n/\Gamma$, $N/\Gamma$ | Spherical, hyperbolic and nilmanifold quotients |
| $L(p,q)$ | Lens space |
| $\chi$, $b_i$, $h^{p,q}$ | Euler characteristic, Betti numbers, Hodge numbers |
| $\Theta_n$, $bP_{n+1}$ | Group of homotopy spheres; boundary of the parallelizable case |
| $U(n)$, $SU(n)$, $Sp(n)$, $Sp(n)\cdot Sp(1)$, $G_2$, $\mathrm{Spin}(7)$ | Holonomy groups |
| $\mathrm{Gr}_k(\mathbb{R}^n)$, $F\ell_n(\mathbb{C})$ | Grassmannian and flag manifold |
| $\mathbb{Z}$ | The standard number systems of the corpus |

## Further Reading

- John M. Lee, *Introduction to Smooth Manifolds* (Springer, 2nd ed. 2013), for the definition of a manifold, the tangent bundle and the standard examples.
- Michael Spivak, *A Comprehensive Introduction to Differential Geometry*, Volume I (Publish or Perish, 3rd ed. 1999), for the model manifolds, the space forms and the classical examples.
- Michael Freedman and Frank Quinn, *Topology of 4-Manifolds* (Princeton University Press, 1990), for the topological classification of four-manifolds and the intersection form.
- Dominic Joyce, *Compact Manifolds with Special Holonomy* (Oxford University Press, 2000), for the Calabi–Yau, hyperkähler, $G_2$ and $\mathrm{Spin}(7)$ manifolds by their holonomy.
