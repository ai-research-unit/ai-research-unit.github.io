
# __List of Affine and Euclidean Groups__

## Introduction

This article lists the affine, Euclidean and similarity groups of the corpus — $\operatorname{Aff}(n)$, $E(n)$, $SE(n)$ and $\operatorname{Sim}(n)$ — together with the transformations that generate them and the theorem of Cartan–Dieudonné that controls the length of a product of reflections. The property the list gathers is that of a group of transformations of affine or Euclidean space defined by a semidirect product: the translations by a linear or orthogonal part. The affine group is the automorphism group of affine space, the Euclidean group is the isometry group of Euclidean space, and the similarity group is the group of transformations that multiply all distances by a common positive scalar.

Every entry points to the article that introduces the group or the theorem. The article introduces nothing and proves nothing: it records the semidirect product, the dimension, the generators and the classification of the plane isometries as the introducing articles give them, and it neither restates a definition nor gives a proof.

The article records examples and non-examples side by side. Beside the groups it lists the transformations that fail the property of their group: an affine map with a general linear part is not an isometry; a similarity with ratio different from $1$ does not preserve distance; a translation has no fixed point, so the isometries of the plane divide into those with a fixed point and those without; the line admits no non-trivial rotation, so the one-dimensional case is not a degenerate case of the plane; and the affine group of a general field is not the Euclidean group of a metric space, each with the failure named and the article that records it.

## The Affine Group

An affine space is a torsor for the additive group of a vector space: any two points determine a difference vector and no point is distinguished. The affine group is its automorphism group, the semidirect product of the translations with the general linear group.

| Object or property | The statement | Introduced in |
|---|---|---|
| the affine space $\mathbb{A}$ with direction $V$ | a set with a free and transitive action of $(V,+)$; the translation picture of geometry | *Affine Spaces and Translations* |
| the translation $t_v$ and the translation group $T(\mathbb{A})$ | $t_v(a) = a + v$; the translations form a normal subgroup $\cong (V,+)$, acting simply transitively | *Affine Spaces and Translations* |
| the affine group $\operatorname{Aff}(\mathbb{A}) = V \rtimes \operatorname{GL}(V)$ | the semidirect product with $(T,b)(T',b') = (TT',Tb'+b)$; the affine maps $x \mapsto Tx + b$ | *Affine Spaces and Translations* |
| the affine group as the automorphism group of affine space | $\operatorname{Aff}(V)$ is to the affine structure what $\operatorname{GL}(V)$ is to the linear structure | *Affine Spaces and Translations* |
| the affine invariants | incidence, parallelism, affine independence and the barycentres; the linear part is the homomorphism onto $\operatorname{GL}(V)$ | *Affine Spaces and Translations* |
| the barycentric coordinates $(\alpha_0,\ldots,\alpha_n)$ | affine combinations $\sum_i\lambda_ia_i$ with $\sum_i\lambda_i = 1$; the coordinate system of the affine structure | *Affine Spaces and Translations* |
| the affine subspace $B = a + W$ | a point and a direction; the incidence structure of affine geometry | *Affine Spaces and Translations* |
| the affine group of the line, $\operatorname{Aff}(\mathbb{R}) = \mathbb{R} \rtimes \mathbb{R}^\times$ | the group $x \mapsto ax + b$ of the line; the dilations and translations | *Real Line Geometry and Isometries* |

## The Euclidean Group

The Euclidean group is the isometry group of $\mathbb{R}^n$ with its positive definite inner product; every isometry is affine, with linear part orthogonal, and the group is the semidirect product of the translations with the orthogonal group.

| Object or property | The statement | Introduced in |
|---|---|---|
| the Euclidean group $E(n) = \mathbb{R}^n \rtimes O(n)$ | the maps $x \mapsto Ax + b$ with $A$ orthogonal; the isometry group of $\mathbb{R}^n$ | *Euclidean Geometry*; *Symmetry, Point and Crystallographic Groups* |
| the dimension of $E(n)$ | $n(n+1)/2$: $n$ translations and $n(n-1)/2$ rotations | *Euclidean Geometry* |
| the special Euclidean group $SE(n) = \mathbb{R}^n \rtimes SO(n)$ | the orientation-preserving isometries; the rigid motions | *Euclidean Geometry*; *The Rotation Group and Orientation* |
| the linear part $\ell(A,b) = A$ | the homomorphism $E(n) \to O(n)$; every isometry is affine with orthogonal linear part | *Symmetry, Point and Crystallographic Groups*; *Affine Spaces and Translations* |
| the isometry group of a form of arbitrary signature | $E(\mathbb{A}) = V \rtimes O(V,Q)$ with distance $d(a,b)^2 = Q(a-b)$ | *Affine Spaces and Translations* |
| the squared distance $d(a,b)^2 = Q(a-b)$ | the quantity an isometry preserves; the Euclidean case is $Q$ positive definite | *Affine Spaces and Translations*; *Metric, Uniform and Complete Spaces* |
| the classification of the plane isometries | translation, rotation, reflection and glide reflection; those with a fixed point are the rotations and reflections | *Euclidean Geometry* |
| the isometries of the line | $T_b(x) = x+b$ and $R_b(x) = b-x$; $\operatorname{Isom}(\mathbb{R}) = \mathbb{R} \rtimes \mathbb{Z}/2\mathbb{Z}$ | *Real Line Geometry and Isometries* |
| the Euclidean group as a topological group | a closed subgroup of the affine group, locally compact, with $O(n)$ a maximal compact subgroup | *Topological Groups*; *Matrix Groups and Classical Groups* |

## The Similarity Group and the Generators

The similarity group allows a common positive scale, and its elements together with the reflections generate the whole group of the Euclidean structure. The generators are translations, rotations, reflections, glide reflections and dilatations.

| Object or property | The statement | Introduced in |
|---|---|---|
| the similarity group $\operatorname{Sim}(n) = \mathbb{R}^n \rtimes (\mathbb{R}_{>0} \times O(n))$ | the maps $x \mapsto \lambda Ax + b$ with $\lambda > 0$; the similarities of Euclidean space | *Euclidean Geometry*; *Isometries and Orthogonal Transformations* |
| the similarities of the line | $\operatorname{Sim}(\mathbb{R}) = \mathbb{R} \rtimes \mathbb{R}^\times$; the dilations $D_a(x) = ax$ | *Real Line Geometry and Isometries* |
| the dilatation $D_a$ | $x \mapsto ax$; it multiplies every distance by $\lvert a\rvert$ and fixes the origin | *Real Line Geometry and Isometries* |
| the multiplier of a similarity | $q(Tv) = c\,q(v)$; the similarities of a quadratic form, with multiplier group $\mu$ | *Isometries and Orthogonal Transformations* |
| the translations as generators | the translation subgroup is normal and the quotient is the linear part; every element is a linear part and a translation | *Affine Spaces and Translations* |
| the reflections as generators | the reflections $\tau_v$ generate the orthogonal group; the equal-norm lemma reduces a product to a single reflection | *Isometries and Orthogonal Transformations* |
| Cartan–Dieudonné, linear form | every isometry of an $n$-dimensional non-degenerate quadratic space is a product of at most $n$ reflections | *Isometries and Orthogonal Transformations* |
| Cartan–Dieudonné, affine form | every isometry of affine $n$-space is a product of at most $n+1$ reflections | *Isometries and Orthogonal Transformations*; *Euclidean Geometry* |
| the plane isometries from reflections | a rotation is a product of two reflections in lines through its centre; a translation is a product of two reflections in parallel lines | *Euclidean Geometry*; *The Rotation Group and Orientation* |
| the rotation and reflection matrices | $R(\theta)$ and $S(\theta)$; $\operatorname{SO}(2) \cong S^1$ | *The Rotation Group and Orientation* |

## The Structures Preserved and Their Invariants

The affine and Euclidean groups are the automorphism groups of two nested structures on the same set of points: the affine structure of incidence and parallelism, and the Euclidean structure of distance and angle.

| Object or statement | The content | Introduced in |
|---|---|---|
| the affine structure | the torsor of the translations; its automorphism group is $\operatorname{Aff}(V)$ and it contains no metric | *Affine Spaces and Translations* |
| the Euclidean structure | the positive definite inner product $\langle x,y\rangle = \sum_i x_iy_i$ and the norm $\lvert x\rvert$; its automorphism group is $O(n)$ at a point | *Euclidean Geometry* |
| the affine invariants | incidence, parallelism, affine independence and the barycentres; the affine maps preserve all of them | *Affine Spaces and Translations* |
| the affine subspaces and the incidence theory | $B = a + W$; two subspaces with the same direction are equal or disjoint | *Affine Spaces and Translations* |
| the parallel postulate and Playfair's form | exactly one line through a point parallel to a given line; the axiom that distinguishes Euclidean from hyperbolic geometry | *Euclidean Geometry*; *Non-Euclidean Geometry* |
| congruence and similarity | figures related by an isometry, and by a similarity $\mathbb{R}^n \rtimes (\mathbb{R}_{>0} \times O(n))$ | *Euclidean Geometry* |
| the congruence theorems and the orthogonal group | the synthetic criteria SSS, SAS, ASA correspond to facts about $O(n)$ | *Euclidean Geometry* |
| the Pythagorean theorem and the angle sum | the classical theorems of the metric geometry, proved from the congruence criteria | *Euclidean Geometry* |
| the regular polygons and the Platonic solids | the regular $m$-gon with symmetry group $D_m$; the five regular solids and their symmetry groups | *Euclidean Geometry* |
| the crystallographic restriction | a periodic lattice admits a rotation of order $1,2,3,4$ or $6$ only; the bridge to the crystallographic groups | *Euclidean Geometry*; *Symmetry, Point and Crystallographic Groups* |
| the Euclidean space as a flat model | the complete simply connected model of curvature zero; the geodesics are the lines | *Euclidean Geometry*; *Non-Euclidean Geometry* |

## Non-examples and Warnings

| Object | Why the expected statement fails | Introduced in |
|---|---|---|
| a general affine map $x \mapsto Tx + b$ | it is not an isometry when the linear part is not orthogonal; it preserves incidence and parallelism and not distance | *Affine Spaces and Translations* |
| a similarity with ratio $\lambda \neq 1$ | it does not preserve distance; it multiplies it by $\lambda$, so it is not in $E(n)$ | *Euclidean Geometry* |
| a translation | it has no fixed point; the isometries with a fixed point are only the rotations and the reflections | *Euclidean Geometry* |
| a glide reflection | it preserves orientation and is not a rotation when its translation part is non-zero; it has no fixed point | *Euclidean Geometry* |
| the one-dimensional case | there is no non-trivial rotation of the line; the Cayley–Klein ladder degenerates, and the line is the base case rather than a case of the plane | *Real Line Geometry and Isometries* |
| the affine group of a general field | it is a group of transformations of an affine space over $F$, not the isometry group of a metric space; the Euclidean group needs an ordered field and a form | *Affine Spaces and Translations* |
| the affine group $\operatorname{Aff}(n)$ | it is not compact and not unimodular for $n \geq 1$; it is a Lie group of dimension $n^2+n$ | *Affine Spaces and Translations*; *Lie Groups* |

Objects that a reader may expect in a list of affine and Euclidean groups, and does not find here.

| Object | Why it is not listed | Introduced in |
|---|---|---|
| the isometry groups $\operatorname{Isom}(\mathbb{H}^n) = O(n,1)$ and $\operatorname{Isom}(S^n) = O(n+1)$ | they are the isometry groups of the non-Euclidean model spaces and are catalogued with the isometry and symmetry groups | *List of Isometry and Symmetry Groups* |
| the crystallographic, wallpaper and frieze groups | they are the discrete subgroups of $E(n)$ and are catalogued with the discrete geometric groups | *Symmetry, Point and Crystallographic Groups*; *List of Discrete Geometric Groups* |
| $\operatorname{PGL}(n+1)$ and the projective transformations | the projective group is not a semidirect product of this kind and is catalogued with the projective groups | *List of Projective Geometric Groups* |
| the Möbius and conformal groups | they are the transformations of a conformal structure and are catalogued with the Möbius groups | *List of Möbius and Conformal Groups* |
| the Galilean and Poincaré groups | they are the symmetry groups of space–time, a physical construction outside this list | *Pseudo-Riemannian and Lorentzian Geometry*; *Split-Biquaternion Rotations and the Lorentz Group* |

## Summary

This article has listed the affine and Euclidean groups of the corpus: the affine group $\operatorname{Aff}(n) = \mathbb{R}^n \rtimes GL(n)$, the automorphism group of affine space, with the translations as a simply transitive normal subgroup, the affine maps $x \mapsto Tx+b$, the barycentric coordinates and the affine invariants; the Euclidean group $E(n) = \mathbb{R}^n \rtimes O(n)$ with the special group $SE(n) = \mathbb{R}^n \rtimes SO(n)$, the linear part, the dimension $n(n+1)/2$ and the classification of the plane isometries; the similarity group $\operatorname{Sim}(n) = \mathbb{R}^n \rtimes (\mathbb{R}_{>0} \times O(n))$ with the dilatations; the generators — translations, rotations, reflections and glide reflections — and Cartan–Dieudonné's theorem that every isometry is a product of at most $n+1$ reflections. Beside the examples stand the non-examples: the affine maps that are not isometries, the similarities of ratio not one, the translations and glide reflections without fixed points, and the absence of a non-trivial rotation of the line. The list introduces and proves nothing; it is the index of the affine and Euclidean groups of the corpus.

## Summary of Notation

A catalogue denotes its objects by name rather than by symbol. The symbols that appear in the tables are those of the articles that introduce them.

| Symbol | Meaning |
|---|---|
| $\mathbb{A}$, $V$ | an affine space, its direction vector space |
| $a + v$, $b - a$ | the action of $V$ on $\mathbb{A}$, the difference of two points |
| $t_v$, $T(\mathbb{A})$ | translation by $v$, the translation group |
| $\operatorname{Aff}(n) = \mathbb{R}^n \rtimes GL(n)$, or $V \rtimes GL(V)$ over a general vector space | the affine group; the maps $x \mapsto Tx+b$ |
| $(\alpha_0,\ldots,\alpha_n)$ | barycentric coordinates; affine combinations |
| $E(n) = \mathbb{R}^n \rtimes O(n)$ | the Euclidean isometry group |
| $SE(n) = \mathbb{R}^n \rtimes SO(n)$ | the orientation-preserving Euclidean group |
| $\operatorname{Sim}(n) = \mathbb{R}^n \rtimes (\mathbb{R}_{>0} \times O(n))$ | the similarity group |
| $\ell(A,b) = A$ | the linear part of an affine map |
| $Q$, $d(a,b)^2 = Q(a-b)$ | the quadratic form and the squared distance |
| $T_b$, $R_b$, $D_a$ | translation, reflection and dilation of the line |
| $\tau_v$ | the reflection in the vector $v$ |
| $GL(V)$, $O(n)$, $SO(n)$ | the linear, orthogonal and special orthogonal groups |

## Further Reading

- Marcel Berger, *Geometry I* (Springer, 1987), for affine spaces, the affine and Euclidean groups and the classification of the isometries.
- Jean Dieudonné, *La géométrie des groupes classiques* (Springer, 3rd ed. 1971), for the orthogonal and unitary groups and the reflection theorem of Cartan–Dieudonné.
- David Hilbert, *Grundlagen der Geometrie* (Teubner, 1899), for the synthetic axioms of Euclidean geometry and the relation between the synthetic and analytic formulations.
- John Stillwell, *The Four Pillars of Geometry* (Springer, 2005), for the affine and Euclidean transformations and the geometry they organise.
