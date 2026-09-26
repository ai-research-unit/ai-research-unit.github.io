
# __List of Non-Examples in Geometry__

## Introduction

This article lists the objects of the corpus that fail one geometric property, each with the property it breaks and the article that records the failure. Every entry points to the article that introduces the object, and the article introduces nothing and proves nothing.

The list gathers the objects that look like manifolds, or like standard manifolds, and are not: the Alexander horned sphere, a topological sphere whose embedding is wild; the Whitehead manifold, contractible and not homeomorphic to $\mathbb{R}^3$; the exotic spheres, homeomorphic to $S^7$ and not diffeomorphic to it; the exceptional smooth structures on $\mathbb{R}^4$ and the $E_8$ manifold, which is a topological four-manifold with no smooth structure; the singular curves and the spaces with a singular point that fail the local Euclidean condition; the long line, which is locally Euclidean and not second countable; the non-orientable surfaces, which fail orientability; and the Kodaira–Thurston manifold and the non-spin manifolds, which fail the Kähler and the spin conditions. The objects are grouped by the property they fail: tameness of an embedding, the smooth structure, the manifold condition, the countability axioms, orientability, and the symplectic and spin structures.

The article records examples and non-examples side by side. The typical row names an object and the property it *fails*, so that the object can be read as the boundary of the definition it is usually taken to test; where the corpus also states the positive property the object retains, both are named.

## Wild Embeddings

A tame embedding is one that can be straightened by an ambient homeomorphism; the objects of this group are the embeddings that cannot.

| Object | The property it breaks | Introduced in |
|---|---|---|
| the Alexander horned sphere | homeomorphic to $S^2$ but not tamely embedded in $S^3$: the bounded complementary domain is not simply connected | *Wild and Exotic Manifolds* (planned) |
| a wild knot | a knot in $S^3$ not isotopic to a polygonal one; it is excluded from the theory | *Knot Theory* |

The horned sphere is the standard wild embedding of a sphere, and the failure is visible in the complement, which has a non-trivial fundamental group in contrast to the tame case; the wild knot is the corresponding phenomenon in dimension one, and the corpus excludes it from knot theory. Both show that the homeomorphism type of an embedded object does not determine its position, so that tameness is a genuine additional hypothesis.

## Exotic Structures

An exotic structure is a smooth structure on a topological manifold that is not the standard one, so that the topological and the smooth classifications differ.

| Object | The property it breaks | Introduced in |
|---|---|---|
| the Whitehead manifold | a contractible open three-manifold that is not homeomorphic to $\mathbb{R}^3$ | *Wild and Exotic Manifolds* (planned) |
| the exotic spheres of Milnor | the $28$ oriented diffeomorphism classes of smooth structures on the topological seven-sphere: homeomorphic to $S^7$ but not diffeomorphic to it | *Cobordism and Surgery Theory*, §Homotopy Spheres and Exotic Spheres |
| an exotic smooth structure on $\mathbb{R}^4$ | a smooth structure on the topological $\mathbb{R}^4$ not diffeomorphic to the standard one; $\mathbb{R}^4$ is the only Euclidean space with this property | *Low-Dimensional Topology* |
| the $E_8$ manifold | a closed simply connected topological four-manifold with intersection form $E_8$, which is not smoothable | *Low-Dimensional Topology* |
| a topological manifold with no smooth structure | a topological manifold carrying no smooth atlas, such as the $E_8$ manifold | *Low-Dimensional Topology*, §Four-Manifolds and the Intersection Form |
| a non-smoothable intersection form | a form realised by a topological four-manifold but by no smooth one; the obstruction is the Donaldson invariant | *Low-Dimensional Topology* |

The exotic spheres are detected by the signature of a bounding manifold through the Hirzebruch signature theorem, and the class $\Theta_7 \cong \mathbb{Z}/28$ counts them; the exotic structures on $\mathbb{R}^4$ and the non-smoothability of the $E_8$ manifold show that the same phenomenon occurs in dimension four for the simplest topological manifolds. The Whitehead manifold fails a different property: it is contractible and simply connected at infinity in a weaker sense, so its homotopy type does not determine its homeomorphism type.

## Failures of the Manifold Condition

An object fails the manifold condition when some point has no neighbourhood homeomorphic to an open subset of $\mathbb{R}^n$.

| Object | The property it breaks | Introduced in |
|---|---|---|
| a singular plane curve | not a manifold at a node or a cusp; the tangent space has dimension larger than the local dimension | *Algebraic Curves*, §Plane Curves |
| the pseudo-arc | a continuum that is not locally Euclidean at any point, hence not a manifold | *Continuum Theory* |
| the figure-eight curve | the union of two circles meeting at a point, not a manifold at the point of tangency | *Continuum Theory*, §Cut Points and the Structure of Arcs |
| the quotient of a Lie group by a dense subgroup | not a manifold: the quotient by the irrational line is not locally Euclidean | *Lie Groups* |
| the orbifold quotient $\mathbb{R}^n/\Gamma$ of a crystallographic group | not a manifold at the fixed points of the elements of finite order, at which it is singular | *Symmetry, Point and Crystallographic Groups*, §The Classical Counts |
| the solenoid | a hyperbolic attractor that is not a manifold | *Hyperbolic Dynamics and Anosov Systems* |
| the null cone $\mathcal{N}$ of the biquaternion algebra | not a manifold at the origin, though $\mathcal{N}\setminus\{0\}$ is a smooth real six-manifold | *Biquaternion Topology* |
| the zero-divisor set of the split biquaternions | not a manifold at the origin | *Split-Biquaternion Zero Divisors* |
| a supermanifold | a supermanifold that is not a manifold: the odd directions have no topological model | *Supergeometry* |
| a Gromov–Hausdorff limit of manifolds | may be a space that is not a manifold at all | *Gromov–Hausdorff Convergence* |
| the Zariski topology on a variety | not Hausdorff, and so not a manifold; the manifold condition includes the separation axioms | *Algebraic Geometry* |
| the preimage of a critical value | it may fail to be a submanifold altogether, the regular value theorem requiring regularity | *Differential Topology*, §Critical Points and Regular Values |

The singularities of algebraic curves and surfaces are the geometric source of the failure: the tangent space at a singular point is larger than the local dimension, and the resolution of the singularity, the blow-up, is the operation that replaces the point by the projective tangent cone. The singular locus may reduce to a single point, as for the figure-eight curve and the zero-divisor set, or fill a whole subvariety, as for the null cone; the pseudo-arc fails at every point and shows that compactness and connectedness are far from the manifold condition, and the Gromov–Hausdorff limit shows that the limit of a sequence of manifolds need not be a manifold. Two failures are not singularities of a single space: the orbifold quotient is singular along the fixed-point set of the group, and the preimage of a critical value fails to be a submanifold although the map defining it is smooth.

## The Countability Axioms

The long line satisfies the local model of a manifold and fails the countability axioms that the definition of a manifold requires.

| Object | The property it breaks | Introduced in |
|---|---|---|
| the long line | every point has a neighbourhood homeomorphic to an open interval of $\mathbb{R}$, but it is not second countable, so it is not a manifold in the sense of the corpus | *Paracompactness and Partitions of Unity*, §The Smirnov Metrisation Theorem |
| the long line | countably compact but not compact, and not paracompact, so no smooth partition of unity subordinates to a cover | *Paracompactness and Partitions of Unity*, §The Smirnov Metrisation Theorem |
| the long ray $[0,\omega_1)$ | locally metrisable and not paracompact; not second countable | *Paracompactness and Partitions of Unity*, §The Smirnov Metrisation Theorem |

The long line is the standard example that local Euclideanity does not imply the countability and paracompactness that the definition of a manifold imposes, and the smooth theory of the corpus uses the existence of partitions of unity, which fails there. The example is the boundary of the definition rather than a manifold with an unusual smooth structure.

## Orientability and the Non-Orientable Surfaces

A non-orientable surface is a manifold that fails the consistency of the local orientations, so that the integral fundamental class and the integral degree are not available.

| Object | The property it breaks | Introduced in |
|---|---|---|
| the projective plane $\mathbb{RP}^2$ | non-orientable: $w_1(T\mathbb{RP}^2) \neq 0$, the first Stiefel–Whitney class being the obstruction to orientation | *Low-Dimensional Topology*; *Characteristic Classes* |
| the Klein bottle | non-orientable: it admits no consistent orientation of its tangent bundle | *Low-Dimensional Topology* |
| the Möbius band | a non-orientable surface with boundary, so a manifold with boundary, not a closed manifold | *Poincaré Duality*; *Topological K-Theory* |
| the connected sum $N_k$ of $k$ projective planes | non-orientable of genus $k$, with $H_1(N_k;\mathbb{Z}) = \mathbb{Z}^{k-1}\oplus\mathbb{Z}/2$ | *Cup and Cap Products* |
| a non-orientable manifold in the degree theory | the integral degree is not defined; only the degree modulo $2$ remains | *Degree Theory and the Brouwer Fixed-Point Theorem* |

The non-orientable surfaces are the two-dimensional instances of the failure of orientability, and the invariant that survives is the degree modulo $2$; the Stiefel–Whitney class $w_1$ is the obstruction to orientability in general. The projective plane and the Klein bottle show that the failure has a global effect: the integral fundamental class and the integral degree are unavailable, and only the mod-$2$ theory survives.

## The Symplectic and the Spin Structures

Two further structures have their standard failures, witnessed by the four-dimensional instances below: the symplectic structure is strictly weaker than the Kähler one, and the spin structure is strictly stronger than the orientation.

| Object | The property it breaks | Introduced in |
|---|---|---|
| the Kodaira–Thurston manifold | compact and symplectic but not Kähler: its first Betti number is odd | *Kähler Geometry*, §Examples |
| a non-spin manifold | oriented but with $w_2 \neq 0$, so it carries no spin structure | *Spin Geometry*, §The Definition; *Characteristic Classes* |

The Kodaira–Thurston manifold is the quotient of the Heisenberg group by a lattice, and it shows that the containment of the Kähler manifolds in the symplectic ones is strict. The second class $w_2$ is the obstruction to a spin structure, so a manifold may be orientable and still carry no spinor bundle and no Dirac operator; the two conditions are successive refinements of the tangent bundle, and neither is automatic.

## Summary

This article has listed the objects of the corpus that fail one geometric property, each with the property it breaks. The Alexander horned sphere and the wild knot are the wild embeddings; the Whitehead manifold, the exotic spheres, the exotic structures on $\mathbb{R}^4$ and the $E_8$ manifold are the exotic structures; the singular plane curve, the pseudo-arc, the figure-eight curve, the quotient by a dense subgroup, the solenoid, the null cone and the Zariski topology fail the manifold condition; the long line fails the countability axioms while satisfying the local model; the orbifold quotient and the preimage of a critical value fail to be manifolds without failing smoothness; the Kodaira–Thurston manifold is symplectic and not Kähler, and a non-spin manifold carries no spin structure; and the projective plane, the Klein bottle and the Möbius band fail orientability. The objects are grouped by the property they test, and the positive property each retains is named beside the failure.

## Summary of Notation

A catalogue denotes its objects by name rather than by symbol. The symbols that appear in the tables are the following, and they are the symbols of the articles that introduce them.

| Symbol | Meaning |
|---|---|
| $S^2$, $S^3$, $S^7$ | Sphere of the wild embedding, the complement and the exotic structure |
| $\mathbb{R}^3$, $\mathbb{R}^4$ | Euclidean spaces of the Whitehead manifold and the exotic structures |
| $\Theta_7$ | Group of the smooth structures on the topological seven-sphere, $\Theta_7 \cong \mathbb{Z}/28$ |
| $\mathbb{RP}^2$, $N_k$ | Projective plane, connected sum of $k$ projective planes |
| $w_1$, $w_2$ | First and second Stiefel–Whitney classes, the obstructions to orientation and to a spin structure |
| $\mathbb{R}^n/\Gamma$ | Compact flat orbifold of a crystallographic group |
| $\deg_2$ | Degree modulo $2$ |
| $E_8$ | Intersection form of the non-smoothable four-manifold |
| $\mathcal{N}$ | The null cone of the biquaternion algebra |

## Further Reading

- Robion Kirby and Laurence Taylor, "A Survey of 4-Manifolds through the Eyes of Surgery", in *Surveys on Surgery Theory* (Princeton University Press, 2000), for the exotic smooth structures on four-manifolds and the failure of smoothing.
- John Milnor, "On Manifolds Homeomorphic to the 7-Sphere", *Annals of Mathematics* 64 (1956), for the exotic spheres and the computation of $\Theta_7$.
- Michael H. Freedman and Frank Quinn, *Topology of 4-Manifolds* (Princeton University Press, 1990), for the topological classification, the $E_8$ manifold and the non-smoothability.
- J. H. C. Whitehead, "A Certain Open Manifold whose Group is Unity", *Quarterly Journal of Mathematics* 6 (1935), 268–279, for the Whitehead manifold.
- Ralph H. Fox and Emil Artin, "Some Wild Cells and Spheres in Three-Dimensional Space", *Annals of Mathematics* 49 (1948), 979–990, for the horned sphere and the wild embeddings.
