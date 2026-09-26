
# __List of Isometry and Symmetry Groups__

## Introduction

This article lists the isometry and symmetry groups of the corpus: the isometry group of a metric space, the isometry groups of the three model geometries, $\operatorname{Isom}(\mathbb{R}^n) = E(n)$, $\operatorname{Isom}(S^n) = O(n+1)$ and $\operatorname{Isom}(\mathbb{H}^n) = O(n,1)$, the crystallographic, wallpaper and frieze groups as the discrete subgroups of a Euclidean isometry group, and the symmetry groups of the regular polytopes. The property the list gathers is that of a group of distance-preserving maps of a metric space: an isometry satisfies $d(fx,fy) = d(x,y)$, and the symmetry group of a figure is the subgroup of the isometries that preserve it.

Every entry points to the article that introduces the group. The article introduces nothing and proves nothing: it records the space, the metric, the group and its structure as the introducing articles give them, and it neither restates a definition nor gives a proof.

The article records examples and non-examples side by side. Beside the groups it lists the cases in which the expected structure fails: the isometry group of a general metric space need not be a Lie group and need not act transitively, unlike the isometry groups of the model spaces; $O(n,1)$ is non-compact while $O(n+1)$ is compact, so the constant-curvature trichotomy is also a compactness trichotomy; the orientation-preserving isometry group of the hyperbolic plane is $\operatorname{PSL}(2,\mathbb{R})$, which is only half of the full group; the symmetry group of a bounded figure fixes a point while that of a periodic figure does not; and the crystallographic restriction forbids a lattice rotation of order other than $1$, $2$, $3$, $4$ or $6$, each with the failure named and the article that records it.

## The Isometry Group of a Metric Space

The isometry group is introduced for an arbitrary distance space and then refined for the model geometries, where it is a Lie group with a definite dimension.

| Object or statement | The content | Introduced in |
|---|---|---|
| the isometry group $\operatorname{Isom}(X)$ | the bijections with $d(fx,fy) = d(x,y)$; a group under composition | *Metric, Uniform and Complete Spaces*; *Metric Geometry* |
| the compact-open topology on $\operatorname{Isom}(X)$ | the topology in which the isometry group is a topological group; closed in the space of maps | *Metric Geometry*; *Topological Groups* |
| the Euclidean case | $\operatorname{Isom}(\mathbb{R}^n) = E(n) = \mathbb{R}^n \rtimes O(n)$, of dimension $n(n+1)/2$ | *Euclidean Geometry*; *Symmetry, Point and Crystallographic Groups* |
| the Myers–Steenrod theorem | the isometries of a Riemannian manifold are smooth, so its isometry group is a Lie group | *Riemannian Geometry*; *Metric Geometry* |
| the isometry group of a homogeneous space | a space $G/H$ with $G$-invariant metric has $\operatorname{Isom}(X) \supseteq G$; the model spaces are symmetric spaces $G/O(2)$ | *Non-Euclidean Geometry*; *Symmetric Spaces* |
| the trichotomy of the model geometries | $E(2) = \mathbb{R}^2 \rtimes O(2)$, $O(3)$ and $\operatorname{PSL}(2,\mathbb{R})\rtimes\mathbb{Z}/2$, all of dimension three | *Non-Euclidean Geometry*; *The Three Two-Dimensional Algebras and the Three Kinds of Rotation* |
| the isometry group of a discrete space | every bijection is an isometry; $\operatorname{Isom}(X) = \operatorname{Sym}(X)$ when the distance separates the points | *Metric, Uniform and Complete Spaces* |
| the isometry group as a transformation group | $\operatorname{Isom}(X)$ acting on $X$, with the action faithful and the orbit the metric class of a point | *Transformation Groups*; *Group Actions and Structure* |

## The Three Model Geometries

Each of the three complete simply connected spaces of constant curvature has its isometry group, and the three groups are the source of the whole geometry of this Part.

| Space | The isometry group | The structure and dimension | Introduced in |
|---|---|---|---|
| $\mathbb{R}^n$, curvature $0$ | $\operatorname{Isom}(\mathbb{R}^n) = \mathbb{R}^n \rtimes O(n)$ | dimension $n(n+1)/2$; non-compact; the translations are normal and simply transitive | *Euclidean Geometry*; *Affine Spaces and Translations* |
| $S^n_R$, curvature $+1/R^2$ | $\operatorname{Isom}(S^n) = O(n+1)$ | dimension $n(n+1)/2$; compact; $\operatorname{SO}(n+1)$ is the orientation-preserving part | *Spherical Geometry* |
| $\mathbb{H}^n$, curvature $-1$ | $\operatorname{Isom}(\mathbb{H}^n) = O(n,1)$ | dimension $n(n+1)/2$; non-compact; $O(n,1)^0$ is the identity component | *Hyperbolic Geometry*; *Pseudo-Riemannian and Lorentzian Geometry* |
| the hyperbolic plane $\mathbb{H}^2$ | $\operatorname{Isom}(\mathbb{H}^2) = \operatorname{PGL}(2,\mathbb{R})$; orientation-preserving $\operatorname{PSL}(2,\mathbb{R})$ | dimension three; the boundary $\partial\mathbb{H}^2$ is the projective line | *Hyperbolic Geometry*; *Möbius and Lie Sphere Geometry* |
| the hyperbolic three-space $\mathbb{H}^3$ | $\operatorname{Isom}(\mathbb{H}^3) = \operatorname{PGL}(2,\mathbb{C})$; orientation-preserving $\operatorname{PSL}(2,\mathbb{C})$ | dimension six; the boundary is the Riemann sphere | *Hyperbolic Geometry*; *Möbius and Lie Sphere Geometry* |
| the hyperboloid model | $\mathbb{H}^n = H^{1,n}$ in $\mathbb{R}^{1,n}$; the isometries are the Lorentz group $O(n,1)$ | the quadric model of hyperbolic space | *Hyperbolic Geometry*; *Pseudo-Riemannian and Lorentzian Geometry* |
| the elliptic quotient | $\mathbb{E}^n = S^n/\{\pm1\}$; $\operatorname{Isom}(\mathbb{E}^n) = O(n+1)/\{\pm I\}$ | curvature $+1$; $\mathbb{E}^2 = \mathbb{RP}^2$ | *Spherical Geometry* |
| the boundary at infinity | $\partial\mathbb{H}^n$ carries a Möbius action of $\operatorname{Isom}(\mathbb{H}^n)$; $S^n$ and $\mathbb{E}^n$ have no boundary | the structural difference of the hyperbolic model | *Hyperbolic Geometry*; *Non-Euclidean Geometry* |

## The Discrete Subgroups and the Crystallographic Groups

A crystallographic group is a discrete subgroup of a Euclidean isometry group with compact quotient; the finite point groups and the lattices are the two ingredients, and the classification is finite in each dimension.

| Object or statement | The content | Introduced in |
|---|---|---|
| the symmetry group of a figure | $\operatorname{Sym}(F) = \{g \in E(n) : gF = F\}$; a group under composition | *Symmetry, Point and Crystallographic Groups* |
| a finite symmetry group fixes a point | a bounded figure has a finite symmetry group conjugate to a finite subgroup of $O(n)$ | *Symmetry, Point and Crystallographic Groups*; *Finite Groups and Symmetry* |
| the point group $P = \ell(\Gamma)$ | the finite image of a crystallographic group in $O(n)$ | *Symmetry, Point and Crystallographic Groups* |
| the translation subgroup $T_\Gamma$ | $\Gamma \cap \mathbb{R}^n$, a lattice of rank $n$; its basis $b_1,\ldots,b_n$ | *Symmetry, Point and Crystallographic Groups* |
| the crystallographic restriction | a lattice-compatible rotation has order $1,2,3,4$ or $6$; the pivot identity $2\cos(2\pi/k) \in \mathbb{Z}$ | *Symmetry, Point and Crystallographic Groups*; *Euclidean Geometry* |
| the Bieberbach theorems | a crystallographic group is determined up to finite index by its point group and lattice; finitely many in each dimension | *Symmetry, Point and Crystallographic Groups* |
| the flat quotient $\mathbb{R}^n/\Gamma$ | a compact flat orbifold, a flat manifold when $\Gamma$ is torsion-free | *Symmetry, Point and Crystallographic Groups* |
| the classical counts | $2$ crystallographic groups on the line, $7$ frieze groups, $17$ wallpaper groups, $230$ space groups in three dimensions, $4894$ in four | *Symmetry, Point and Crystallographic Groups*; *Euclidean Geometry* |
| the discrete isometry groups of the line | $D_\infty = \mathbb{Z} \rtimes \mathbb{Z}/2\mathbb{Z}$; the discrete subgroups are $a\mathbb{Z}$ and $D_\infty(a)$ | *Real Line Geometry and Isometries* |
| the Fuchsian and Kleinian groups | the discrete subgroups of $\operatorname{PSL}(2,\mathbb{R})$ and $\operatorname{PSL}(2,\mathbb{C})$; the surfaces and three-manifolds they uniformise | *Hyperbolic Geometry*; *Hyperbolic Groups* |
| the space forms | the complete constant-curvature manifolds $S^n/\Gamma$, $\mathbb{R}^n/\Gamma$, $\mathbb{H}^n/\Gamma$ for $\Gamma$ discrete acting freely | *Riemannian Geometry*; *Hyperbolic Geometry*; *Spherical Geometry* |

## The Symmetry Groups of Figures and Polytopes

The finite symmetry groups are the finite subgroups of the orthogonal group: the cyclic and dihedral families in the plane, and the polyhedral groups in space, with the rotation groups of the Platonic solids and their full symmetry groups.

| Object | The content | Introduced in |
|---|---|---|
| the symmetry of a regular $m$-gon | the rotation group $C_m$ and the full symmetry group $D_m$, of order $2m$ | *Euclidean Geometry*; *Symmetry, Point and Crystallographic Groups* |
| the finite subgroups of $O(2)$ | the cyclic groups $C_m$ and the dihedral groups $D_m$ | *Symmetry, Point and Crystallographic Groups*; *Finite Groups and Symmetry* |
| the finite subgroups of $SO(3)$ | the cyclic, dihedral and polyhedral families: $T$, $O$, $I$ of orders $12$, $24$, $60$ | *Symmetry, Point and Crystallographic Groups*; *Spherical Geometry* |
| the tetrahedral group $T \cong A_4$ | the rotation group of the tetrahedron | *Symmetry, Point and Crystallographic Groups*; *Spherical Geometry* |
| the octahedral group $O \cong S_4$ | the rotation group of the cube and the octahedron | *Symmetry, Point and Crystallographic Groups*; *Spherical Geometry* |
| the icosahedral group $I \cong A_5$ | the rotation group of the dodecahedron and the icosahedron; the smallest nonabelian simple group | *Symmetry, Point and Crystallographic Groups*; *Spherical Geometry*; *Finite Groups and Symmetry* |
| the full symmetry groups of the Platonic solids | $T_d$, $O_h$, $I_h$ of orders $24$, $48$, $120$; the reflections adjoined to the rotations | *Symmetry, Point and Crystallographic Groups* |
| the binary polyhedral groups | $2T$, $2O$, $2I$ in $Sp(1)$, of orders $24$, $48$, $120$; the preimages in the double cover $S^3 \to SO(3)$ | *Symmetry, Point and Crystallographic Groups*; *Quaternion Rotations and Reflections* |
| the Platonic solids and the regular polytopes | the tetrahedron, cube, octahedron, dodecahedron, icosahedron; their symmetry groups | *Euclidean Geometry* |
| the finite rotation group as a spherical symmetry | a finite subgroup of $SO(3)$ is the symmetry group of a spherical figure; the source of $A_4$, $S_4$, $A_5$ | *Spherical Geometry* |

## Non-examples and Warnings

| Object | Why the expected statement fails | Introduced in |
|---|---|---|
| the isometry group of a general metric space | it need not be a Lie group and need not act transitively; a space with a discrete metric has $\operatorname{Isom}(X) = \operatorname{Sym}(X)$ | *Metric Geometry*; *Metric, Uniform and Complete Spaces* |
| the isometry group of the hyperbolic space | $O(n,1)$ is non-compact and has four components; its identity component is the relevant group, unlike the compact $O(n+1)$ | *Hyperbolic Geometry*; *Pseudo-Riemannian and Lorentzian Geometry* |
| the orientation-preserving hyperbolic isometry group | $\operatorname{PSL}(2,\mathbb{R})$ is only the index-two part of $\operatorname{Isom}(\mathbb{H}^2) = \operatorname{PGL}(2,\mathbb{R})$ | *Hyperbolic Geometry*; *Möbius and Lie Sphere Geometry* |
| the symmetry group of a periodic figure | it does not fix a point and is infinite; only the symmetry group of a bounded figure is finite and conjugate to a subgroup of $O(n)$ | *Symmetry, Point and Crystallographic Groups* |
| the rotation of a periodic plane figure | an order $5$, $7$ or higher rotation is incompatible with a lattice; the crystallographic restriction is a genuine obstruction | *Symmetry, Point and Crystallographic Groups*; *Euclidean Geometry* |
| a hyperbolic space form of dimension $n \geq 3$ | the Mostow rigidity theorem gives that homotopy equivalence implies isometry; the deformation theory of the two-dimensional case does not survive | *Hyperbolic Geometry* |
| the isometry group of a symmetric space | it is generally larger than the group $G$ defining the space as $G/H$; the full isometry group can be larger, and the maximal compact subgroup appears in both | *Symmetric Spaces* |

Objects that a reader may expect in a list of isometry and symmetry groups, and does not find here.

| Object | Why it is not listed | Introduced in |
|---|---|---|
| the Euclidean group $E(n)$ and the affine group | they are listed with the affine and Euclidean groups; here they appear as the isometry group of $\mathbb{R}^n$ | *List of Affine and Euclidean Groups* |
| the orthogonal, unitary and symplectic groups | they are the classical groups, defined by a form rather than by a distance | *List of Classical Geometric Groups* |
| the Möbius and conformal groups | they preserve angles and not distances; $\operatorname{Möb}(n) = O(n+1,1)/\{\pm1\}$ is catalogued separately | *List of Möbius and Conformal Groups* |
| the isometry groups of the CAT($0$) and Gromov-hyperbolic spaces | they are metric-geometric generalisations of the symbol $\operatorname{Isom}(X)$ | *Metric Geometry*; *Hyperbolic Groups* |
| the Lorentz and Poincaré groups | they are the symmetry groups of Minkowski space, a physical construction | *Pseudo-Riemannian and Lorentzian Geometry*; *Split-Biquaternion Rotations and the Lorentz Group* |

## Summary

This article has listed the isometry and symmetry groups of the corpus: the isometry group $\operatorname{Isom}(X)$ of a metric space with its compact-open topology, the Myers–Steenrod theorem that it is a Lie group for a Riemannian manifold, and its identification with $\operatorname{Sym}(X)$ in the discrete case; the isometry groups of the three model geometries, $\operatorname{Isom}(\mathbb{R}^n) = E(n)$, $\operatorname{Isom}(S^n) = O(n+1)$ and $\operatorname{Isom}(\mathbb{H}^n) = O(n,1)$, with the hyperbolic case read through $\operatorname{PGL}(2,\mathbb{R})$ and $\operatorname{PGL}(2,\mathbb{C})$; the crystallographic, wallpaper and frieze groups with the point group, the lattice, the crystallographic restriction and the Bieberbach theorems; and the symmetry groups of the regular polygons and the Platonic solids, with the polyhedral groups $T$, $O$, $I$ and their binary covers. Beside the examples stand the non-examples: the general metric space whose isometry group need not be a Lie group, the non-compact hyperbolic group and its orientation-preserving part, the periodic figure whose symmetry group is infinite, and the forbidden lattice rotations. The list introduces and proves nothing; it is the index of the isometry and symmetry groups of the corpus.

## Summary of Notation

A catalogue denotes its objects by name rather than by symbol. The symbols that appear in the tables are those of the articles that introduce them.

| Symbol | Meaning |
|---|---|
| $X$, $d(x,y)$ | a metric space, its distance |
| $\operatorname{Isom}(X)$ | the isometry group, with the compact-open topology |
| $\operatorname{Sym}(F)$, $\operatorname{Sym}(X)$ | the symmetry group of a figure, of a set |
| $E(n) = \mathbb{R}^n \rtimes O(n)$ | the Euclidean isometry group |
| $S^n_R$, $O(n+1)$, $SO(n+1)$ | the round sphere, its isometry group and the orientation-preserving part |
| $\mathbb{H}^n$, $O(n,1)$ | hyperbolic space, its isometry group; the Lorentz-type group |
| $\operatorname{PSL}(2,\mathbb{R})$, $\operatorname{PGL}(2,\mathbb{R})$ | the orientation-preserving and full isometry groups of $\mathbb{H}^2$ |
| $\mathbb{E}^n = S^n/\{\pm1\}$ | elliptic space |
| $\Gamma \leq E(n)$, $T_\Gamma$, $P = \ell(\Gamma)$ | a crystallographic group, its translation lattice, its point group |
| $\mathbb{R}^n/\Gamma$ | the compact flat orbifold or flat manifold |
| $C_m$, $D_m$ | the rotation and symmetry groups of the regular $m$-gon |
| $T$, $O$, $I$ | the rotation groups of the tetrahedron, octahedron and icosahedron |
| $T_d$, $O_h$, $I_h$ | the full symmetry groups of the Platonic solids |
| $2T$, $2O$, $2I$ | the binary polyhedral groups in $Sp(1)$ |
| $D_\infty$ | the infinite dihedral group |

## Further Reading

- Marcel Berger, *Geometry I* (Springer, 1987), for the isometry groups of the model spaces and the classification of the isometries.
- Ludwig Bieberbach, *Über die Bewegungsgruppen der euklidischen Räume* (Mathematische Annalen 70, 1911 and 72, 1912), for the structure and finiteness of the crystallographic groups.
- John Conway, Olaf Delgado Friedrichs, Daniel Huson and William Thurston, *On Three-dimensional Space Groups* (Beiträge zur Algebra und Geometrie 42, 2001), for the classification of the three-dimensional crystallographic groups.
- Harold S. M. Coxeter, *Regular Polytopes* (Dover, 3rd ed. 1973), for the symmetry groups of the regular polytopes and the reflection groups.
