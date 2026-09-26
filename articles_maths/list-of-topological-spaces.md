
# __List of Topological Spaces__

## Introduction

This article lists the topological spaces that Parts I to III of the corpus introduce, each with the article that owns it and with the three properties that classify it: its separation, its compactness and its connectedness. The spaces are grouped by the way the corpus meets them — the number systems and the valued and arithmetic spaces of the algebra and number-theory articles, the spheres, balls and projective spaces of the geometry articles, the matrix groups and homogeneous spaces of the group articles, the spaces produced by the standard constructions, the totally disconnected spaces of the profinite, Cantor and Stone theory, the manifolds, and the pathological spaces that serve as counterexamples.

Every entry points to the article that introduces the space, and every space listed appears somewhere in Parts I to III. The article introduces nothing and proves nothing: it records the separation, compactness and connectedness that the introducing articles establish, and it neither restates a definition nor gives a proof.

The article records examples and non-examples side by side. Beside the spaces that are compact, metrisable or connected it lists the spaces that fail each property — the Sorgenfrey line, which is perfectly normal and separable and not metrisable; the long line, which is locally Euclidean and not paracompact; the topologist's sine curve, which is connected and not path connected; $\beta\mathbb{N}$, which is compact Hausdorff and not first countable — each with the failure named and the article that records it.

## The Number Systems and the Valued Spaces

The spaces of the algebra and number-theory articles are the ones whose topology is induced by an order, by an absolute value, or by a valuation. They are the models on which every other topology of the corpus is tested, and the article that introduces each one also fixes its topology.

| Space | Its separation, compactness and connectedness | Introduced in |
|---|---|---|
| $\mathbb{R}$ | metrisable and second countable; locally compact and $\sigma$-compact, not compact; connected and path connected; complete for the usual metric | *The Real Numbers* |
| $\mathbb{C}$ | $\mathbb{R}^2$ as a topological space; second countable, locally compact, connected, path connected, complete | *The Complex Numbers* |
| $\mathbb{Q}$ | countable and metrisable; totally disconnected, hence not connected; not locally compact and not complete; meagre in itself | *The Rational Numbers* |
| $\mathbb{Z}$, $\mathbb{N}$ | discrete, hence metrisable and totally disconnected; locally compact, not compact | *The Integers* |
| $[0,1]$ | compact, connected, path connected, metrisable and complete | *The Real Numbers* |
| $(0,1)$ | metrisable and connected, hence not totally disconnected; not compact; not complete for the usual metric, which is why completeness is not a topological property | *Metric, Uniform and Complete Spaces* |
| $\mathbb{R}^n$ | second countable, locally compact, $\sigma$-compact, connected and path connected; complete | *Euclidean Geometry* |
| $\mathbb{F}_q$ | the discrete topology on a finite set; compact, totally disconnected, metrisable | *Finite Fields* |
| $\mathbb{Q}_p$ | ultrametric, hence totally disconnected and zero-dimensional; locally compact, complete, not compact | *The $p$-adic Numbers* |
| $\mathbb{Z}_p$ | compact, totally disconnected and perfect, hence homeomorphic to the Cantor set; metrisable | *The $p$-adic Numbers* |
| $k[[t]]$, $k((t))$ | the $(t)$-adic topology, not discrete; totally disconnected; locally compact when $k$ is finite, $k[[t]]$ then compact | *Topological Rings and Fields*; *Formal Power Series and Completion* |
| $\mathbb{A}_{\mathbb{Q}}$, $\mathbb{A}_{\mathbb{Q}}^\times$ | the restricted-product topology; locally compact Hausdorff, not compact; totally disconnected at the non-archimedean places and connected at the archimedean one | *Adeles and Ideles* |
| $\mathcal{M}(A)$ | the Berkovich spectrum of a $K$-affinoid algebra; compact Hausdorff, and an $\mathbb{R}$-tree, hence path connected and contractible in the line case | *Berkovich Spaces* |
| $\operatorname{Spa}(A,A^+)$ | the adic spectrum with the spectral topology; quasi-compact and sober, Hausdorff for the analytic topology in the strongly noetherian case | *Adic Spaces* |

The order topology of $\mathbb{R}$ and the subspace topology of $\mathbb{Q}$ are those of *Topological Spaces*; the $p$-adic and archimedean completions of $\mathbb{Q}$ are compared in *Absolute Values, Valuations and Completions*. The adeles are the restricted product of the completions, so the two rows above and the two rows of the $p$-adic table sit in one family.

## The Spheres, Balls and Projective Spaces

The spaces of the geometry articles are the model spaces of constant curvature and the projective spaces built from a vector space. Their topology is the quotient or subspace topology of the Euclidean one, and their separation and compactness are therefore those of $\mathbb{R}^n$ and its quotients.

| Space | Its separation, compactness and connectedness | Introduced in |
|---|---|---|
| $S^n$, $n \geq 1$ | compact, connected, path connected for $n \geq 1$, Hausdorff and metrisable; a closed submanifold of $\mathbb{R}^{n+1}$ | *Spherical Geometry*; *Smooth Manifolds and Differential Geometry* |
| $S^0 = \{\pm1\}$ | the two-point discrete space; compact, totally disconnected | *Spherical Geometry* |
| $D^n$ | the closed unit ball; compact, connected, path connected, contractible | *Smooth Manifolds and Differential Geometry* |
| $\mathbf{H}^n$ | the hyperbolic space; connected, path connected, contractible and complete for the hyperbolic metric; not compact | *Hyperbolic Geometry* |
| $S^1$ | compact, connected, path connected; simultaneously the circle and the unitary group $U(1)$ | *Topological Spaces* |
| $T^n = \mathbb{R}^n/\mathbb{Z}^n$ | compact, connected, path connected; a Lie group and a symmetric space | *Topological Spaces* |
| $\mathbb{RP}^n = S^n/\{\pm1\}$ | compact, connected for $n \geq 1$; a manifold, connected even though $S^n$ is a double cover | *Projective Geometry*; *Smooth Manifolds and Differential Geometry* |
| $\mathbb{CP}^n$ | compact, connected, path connected; a complex manifold of dimension $n$ | *Topological Spaces*; *Several Complex Variables* |
| $\mathbb{HP}^n$ | compact, connected; a quaternionic manifold and the quotient of $S^{4n+3}$ by the unit quaternions | *CW Complexes and Cellular Approximation*; *Quaternion Geometry* |
| the lens space $L(p;q)$ | compact, connected, a closed $3$-manifold; homotopy equivalent to another lens space exactly when the parameters agree | *Lens Spaces* |
| the Grassmannian $G_k(\mathbb{R}^n)$ | compact and connected for $0 < k < n$; a manifold of dimension $k(n-k)$ | *Grassmannians and Stiefel Manifolds* |
| the Stiefel manifold $V_k(\mathbb{R}^n)$ | compact; connected for $k < n$, and $O(n)$ with two components for $k = n$ | *Grassmannians and Stiefel Manifolds* |
| the flag manifold | compact, connected, and the homogeneous space of a parabolic subgroup | *Flag Manifolds* |
| a space form $M^n$ | complete and connected with constant sectional curvature; by the space-form theorem a quotient of $S^n$, of $\mathbb{R}^n$ or of $\mathbf{H}^n$ by a group acting freely | *Curvature and Geodesics*; *Spherical Geometry*; *Hyperbolic Geometry* |

## The Matrix Groups and Homogeneous Spaces

A Lie group is a topological space as well as a group, and the corpus uses its topology throughout; the groups appear again as groups in *List of Topological Groups* and *List of Lie Groups*, and are recorded here only as spaces.

| Space | Its separation, compactness and connectedness | Introduced in |
|---|---|---|
| $GL_n(\mathbb{R})$ | locally compact Hausdorff, second countable, not compact; two components, separated by the sign of the determinant | *The General Linear Group*; *Lie Groups* |
| $GL_n(\mathbb{C})$ | locally compact Hausdorff, second countable, not compact; connected | *The General Linear Group* |
| $SL_n(\mathbb{R})$, $SL_n(\mathbb{C})$ | locally compact Hausdorff, not compact; connected, and simply connected for the complex case | *The Special Linear Group and the Determinant* |
| $O(n)$, $U(n)$, $Sp(n)$ | compact, Hausdorff, metrisable; $O(n)$ has two components, $U(n)$ and $Sp(n)$ are connected | *Isometries and Orthogonal Transformations*; *The Unitary and Symplectic Groups* |
| $SO(n)$, $SU(n)$ | compact and connected; $SU(n)$ is simply connected, and $SO(n)$ has fundamental group $\mathbb{Z}/2$ for $n \geq 3$ | *The Rotation Group and Orientation*; *The Unitary and Symplectic Groups* |
| $G/H$ | the homogeneous space of a closed subgroup; locally compact Hausdorff, and compact when $H$ is cocompact | *Homogeneous Spaces* |
| $\operatorname{Gr}(k,n) = GL_n/H$ | the Grassmannian as a homogeneous space; compact, connected, and a projective variety when the field is algebraically closed | *Homogeneous Spaces*; *Grassmannians and Stiefel Manifolds* |
| a symmetric space $G/K$ | complete, connected, and a Riemannian manifold with the invariant metric when $K$ is a maximal compact subgroup | *Symmetric Spaces* |
| $LG = C^\infty(S^1,G)$ | the loop group; a Fréchet manifold, not locally compact; connected when $G$ is | *Loop Groups* |

The passage from the group to the homogeneous space is the construction of *Homogeneous Spaces*; the compact groups among these are the groups of *Analysis on Compact Groups*, whose Haar measure is normalised to a probability measure.

## Spaces Built by a Construction

The corpus constructs spaces as well as naming them, and the constructions are entries of the list in their own right, since each turns a space or a family of spaces into a new one with a definite separation, compactness and connectedness.

| Construction and its result | Its separation, compactness and connectedness | Introduced in |
|---|---|---|
| the subspace $A \subseteq X$ | hereditary for $T_0$ to complete regularity and for metrisability; compactness need not pass to a subspace | *Topological Spaces* |
| the product $\prod_i X_i$ | arbitrary products preserve $T_0$ to complete regularity and compactness (Tychonoff); normality and metrisability do not survive | *Topological Spaces* |
| the quotient $X/{\sim}$ | the finest topology making the quotient map continuous; Hausdorffness and first countability are not automatic | *Topological Spaces* |
| the one-point compactification $X^+$ | compact and Hausdorff when $X$ is locally compact Hausdorff; not metrisable for an uncountable discrete $X$ | *Topological Spaces* |
| the cone, suspension and mapping cylinder | built by a quotient of a product with an interval; compact when the source is compact | *CW Complexes and Cellular Approximation* |
| the adjunction space $X \cup_f Y$ | a quotient of the disjoint union; Hausdorffness requires $f$ to be closed or the pair to be a relative CW pair | *CW Complexes and Cellular Approximation* |
| the CW complex | Hausdorff and paracompact; compact exactly when the cell complex is finite | *CW Complexes and Cellular Approximation* |
| the simplicial complex | metrisable and compact when finite, and Hausdorff for the weak topology in general | *Simplicial and Singular Homology* |
| the covering space $\tilde X \to X$ | locally homeomorphic to $X$, hence carries the same local separation and compactness; $\tilde X$ is compact exactly when the covering is finite over a compact base | *The Fundamental Group and Covering Spaces* |
| the inverse limit $\varprojlim X_i$ | a closed subspace of the product; compact when the $X_i$ are compact Hausdorff | *Nets, Filters and Convergence*; *Topological Groups* |
| the nerve $\lvert N(\mathcal{U})\rvert$ of a cover | a simplicial complex, hence metrisable; homotopy equivalent to the space when the cover is good | *Čech Cohomology* |

## The Totally Disconnected, Cantor and Stone Spaces

One family of spaces is separated out because it is totally disconnected, and the corpus meets it in the profinite, Galois and Boolean-algebra articles as well as in the topological ones. Its members are the compact totally disconnected Hausdorff spaces, equivalently the Stone spaces of Boolean algebras.

| Space | Its separation, compactness and connectedness | Introduced in |
|---|---|---|
| the Cantor set $\{0,1\}^{\mathbb{N}}$, $2^{\mathbb{N}}$ | compact, metrisable, perfect, totally disconnected; uncountable, and homeomorphic to $\mathbb{Z}_p$ | *Descriptive Set Theory*; *Continuum Theory* |
| the Baire space $\mathbb{N}^{\mathbb{N}}$ | completely metrisable and zero-dimensional, hence totally disconnected; not compact; homeomorphic to the irrational numbers | *Baire Spaces and Category*; *Descriptive Set Theory* |
| a profinite group $\varprojlim G_i$ | compact Hausdorff and totally disconnected; metrisable exactly when the inverse system has a countable cofinal subsystem | *Profinite Groups and the Krull Topology* |
| the Galois group $G_K = \operatorname{Gal}(\overline K/K)$ | compact totally disconnected for the Krull topology; metrisable for a countable field | *Galois Theory*; *Galois Cohomology* |
| the Stone space of a Boolean algebra | compact, totally disconnected, Hausdorff; the spectral space of the algebra | *Boolean Rings and Stone Duality* |
| $\beta\mathbb{N}$ | compact Hausdorff and extremally disconnected; not first countable at a free ultrafilter, hence not metrisable | *Nets, Filters and Convergence*; *Metrisation and Separation Axioms* |
| the solenoid $\varprojlim S^1$ | compact and connected, dense image of $\mathbb{R}$; not path connected and not locally connected | *Abelian Topological Groups*; *Pontryagin Duality* |
| the Bohr compactification $bG$ | compact Hausdorff, with a dense image of $G$; totally disconnected when $G$ is discrete abelian | *Pontryagin Duality* |
| $\operatorname{Spec} R$ with the Zariski topology | $T_0$ and quasi-compact, and not $T_1$ whenever a nonzero prime is contained in another; totally disconnected in the constructible sense | *Schemes*; *Commutative Algebras* |

Stone duality turns the first five rows into one statement, and the profinite groups are exactly the compact totally disconnected groups, by the theorem of *Profinite Groups and the Krull Topology*. The solenoid is the standard compact connected space that fails to be path connected, and the Cantor set is the standard compact totally disconnected space with no isolated points.

## The Manifolds of the Corpus

A manifold is a space that is locally Euclidean; the corpus uses smooth, complex, Riemannian and symplectic manifolds, and each carries the topology of its local models together with the extra structure.

| Space | Its separation, compactness and connectedness | Introduced in |
|---|---|---|
| a topological manifold $M$ | locally Euclidean Hausdorff and second countable, hence paracompact and metrisable | *Smooth Manifolds and Differential Geometry* |
| a smooth manifold | a manifold with a maximal smooth atlas; the same separation as the underlying manifold | *Smooth Manifolds and Differential Geometry* |
| a Riemannian manifold $(M,g)$ | a manifold with the metric-induced topology, which agrees with the given one | *Riemannian Geometry* |
| a Lorentzian manifold | a pseudo-Riemannian manifold of index one; Hausdorff and second countable, not necessarily compact, and the metric topology agrees with the manifold topology | *Pseudo-Riemannian and Lorentzian Geometry* |
| a Riemann surface | a connected complex one-dimensional manifold; Hausdorff, second countable, not compact unless closed | *Algebraic Curves* |
| a Kähler manifold | a complex manifold with a compatible symplectic form; compact and connected when it is a closed Kähler manifold | *Kähler Geometry* |
| a Calabi–Yau manifold | a compact connected Kähler manifold with trivial canonical bundle | *Calabi–Yau Manifolds* |
| a symplectic manifold $(M,\omega)$ | a manifold with a closed non-degenerate two-form; Hausdorff and second countable, even-dimensional | *Symplectic Geometry* |
| a closed surface | compact, connected, metrisable; classified by the genus and the orientability | *Low-Dimensional Topology* |
| a knot complement $S^3 \setminus K$ | connected, Hausdorff, second countable and not compact; an open $3$-manifold | *Knot Theory* |
| a closed hyperbolic $3$-manifold | compact, connected, and complete for the hyperbolic metric | *Low-Dimensional Topology*; *Hyperbolic Geometry* |

## The Non-metrisable and Pathological Spaces

The remaining spaces of the corpus are the counterexamples. They are recorded with the property they fail, since their role is to show that the implications among separation, metrisability, compactness and paracompactness do not reverse.

| Space | The property it has, and the one it fails | Introduced in |
|---|---|---|
| the Sorgenfrey line $\mathbb{R}_S$ | perfectly normal, separable, Lindelöf, paracompact and Baire; not second countable, not metrisable, not locally compact and not locally metrisable, and its square is not normal | *Metrisation and Separation Axioms*; *Paracompactness and Partitions of Unity* |
| the Sorgenfrey plane $\mathbb{R}_S^2$ | separable and first countable; not normal, hence not paracompact; a product of paracompact spaces that is not paracompact | *Metrisation and Separation Axioms* |
| the Niemytzki plane | separable, first countable, Tychonoff and locally metrisable; not normal and not paracompact | *Metrisation and Separation Axioms*; *Paracompactness and Partitions of Unity* |
| the long line $L$ | connected, locally Euclidean, normal and locally metrisable; not paracompact, not second countable and not metrisable | *Paracompactness and Partitions of Unity* |
| the ordinal spaces $[0,\omega_1)$, $[0,\omega_1]$ | ordered, normal, locally metrisable; first countable and countably compact but not compact, and not compact respectively; neither metrisable nor paracompact | *Paracompactness and Partitions of Unity* |
| the topologist's sine curve | compact and connected; not path connected and not locally connected | *Topological Spaces*; *Continuum Theory* |
| the Warsaw circle | compact connected metric, with the Čech cohomology of a circle; not locally connected, and not homotopy equivalent to $S^1$ | *Continuum Theory* |
| the comb space | compact, connected and contractible; not locally connected at the points of the limiting segment | *Continuum Theory* |
| the pseudo-arc | compact, connected, metrisable and hereditarily indecomposable; not path connected and not locally connected | *Continuum Theory* |
| the Hilbert cube $[0,1]^{\mathbb{N}}$ | compact, connected, metrisable, contractible; universal among separable metrisable spaces | *Metrisation and Separation Axioms*; *Continuum Theory* |
| the indiscrete space on two points | compact, connected, and regular, completely regular and normal; not $T_0$ | *Topological Spaces* |
| the cofinite topology on an infinite set | compact, connected and $T_1$; not Hausdorff | *Topological Spaces* |
| $\{0,1\}^{I}$ for uncountable $I$ | compact Hausdorff; not first countable and not metrisable | *Metrisation and Separation Axioms* |

## Warnings

Objects that a reader may expect to find among the topological spaces, and does not.

| Object | Why it is not listed as a topological space | Introduced in |
|---|---|---|
| the octonions $\mathbb{O}$ | a non-associative algebra, named in the corpus as a division algebra and not equipped with a topology of its own | *Octonion Algebra*; *Normed Division Algebras and the Hurwitz Theorem* |
| a group such as the free group $F_2$ | an object of Part I, with no topology attached until it is made a topological group | *Combinatorial Group Theory* |
| the orthogonal group $O(n)$ | a Lie group and a compact space, but it is defined by a form, so it is a geometric group and not a space of this list | *Isometries and Orthogonal Transformations* |
| the Zariski topology on $\mathbb{R}^n$ | a topology introduced with the algebraic structure of a real variety; recorded here through $\operatorname{Spec} R$ and not as a separate space | *Real Algebraic Geometry* |
| the Alexander horned sphere | a subset of $\mathbb{R}^3$ that is homeomorphic to $S^2$ and whose complement is not simply connected; a counterexample in the list of non-examples in topology | *Low-Dimensional Topology* |

## Summary

This article has listed the topological spaces of Parts I to III with their separation, their compactness and their connectedness, grouped into the valued and arithmetic spaces of the number theory articles, the spheres and projective spaces of the geometry articles, the matrix groups and homogeneous spaces, the constructions that build new spaces, the totally disconnected and Stone spaces, the manifolds, and the pathological counterexamples. The entries range from $\mathbb{R}$ and the $p$-adic fields through the spheres, projective spaces, Grassmannians and flag manifolds to the profinite groups, the Cantor set, the solenoid and $\beta\mathbb{N}$, and each is recorded with the properties that the introducing article establishes. Beside the examples stand the non-examples — the Sorgenfrey line and plane, the long line, the ordinal spaces, the topologist's sine curve, the Warsaw circle and the pseudo-arc — each with the property it fails. The list introduces and proves nothing; it is the index of the spaces of the corpus.

## Summary of Notation

A catalogue denotes its objects by name rather than by symbol, and the names are those of the articles that introduce them. The symbols that appear in the tables are the following.

| Symbol | Meaning |
|---|---|
| $X$, $Y$, $M$ | a topological space, a topological space, a manifold |
| $\mathbb{R}$, $\mathbb{C}$, $\mathbb{Q}$, $\mathbb{Z}$, $\mathbb{N}$ | the real, complex, rational, integer and natural numbers with their standard topologies |
| $\mathbb{F}_q$, $\mathbb{Q}_p$, $\mathbb{Z}_p$ | the finite field of $q$ elements and the $p$-adic field and integers |
| $\mathbb{A}_{\mathbb{Q}}$ | the adeles of $\mathbb{Q}$ |
| $S^n$, $D^n$, $T^n$ | the $n$-sphere, the closed $n$-ball, the $n$-torus |
| $\mathbb{RP}^n$, $\mathbb{CP}^n$, $\mathbb{HP}^n$ | the real, complex and quaternionic projective spaces |
| $\mathbf{H}^n$ | hyperbolic $n$-space |
| $G_k(\mathbb{R}^n)$, $V_k(\mathbb{R}^n)$ | the Grassmannian and the Stiefel manifold of $k$-planes in $\mathbb{R}^n$ |
| $G/H$ | a homogeneous space |
| $X^+$, $X/{\sim}$, $\prod_i X_i$ | one-point compactification, quotient, product |
| $\beta\mathbb{N}$, $bG$ | the Stone–Čech compactification of $\mathbb{N}$; the Bohr compactification |
| $\operatorname{Spec} R$ | the prime spectrum with the Zariski topology |
| $\mathcal{M}(A)$, $\operatorname{Spa}(A,A^+)$ | the Berkovich spectrum and the adic spectrum |
| $\mathbb{R}_S$, $L$, $[0,\omega_1)$ | the Sorgenfrey line, the long line, the first uncountable ordinal space |
| $\{0,1\}^{\mathbb{N}}$, $\mathbb{N}^{\mathbb{N}}$ | the Cantor set and the Baire space of sequences |

## Further Reading

- Ryszard Engelking, *General Topology* (Heldermann, rev. ed. 1989), for the separation axioms, compactness, paracompactness and metrisation theorems in their standard order.
- James R. Munkres, *Topology* (Pearson, 2nd ed. 2000), for the constructions of subspaces, products, quotients and compactifications and the classical examples.
- Lynn A. Steen and J. Arthur Seebach, *Counterexamples in Topology* (Springer, 2nd ed. 1978), for the Sorgenfrey line and plane, the Niemytzki plane, the long line, the ordinal spaces, $\beta\mathbb{N}$ and the other counterexamples tabulated above.
- Stephen Willard, *General Topology* (Addison-Wesley, 1970), for the spaces of the real line, the Cantor set and the Baire space and their homeomorphism types.
