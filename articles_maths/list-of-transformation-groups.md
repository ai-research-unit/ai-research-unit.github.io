
# __List of Transformation Groups__

## Introduction

This article lists the transformation groups of the corpus — the groups that are realised as the transformations of a set carrying a structure — together with the structure each preserves and the article that introduces it. The umbrella notion is that of *Transformation Groups*: a group acts on a set $X$ through a homomorphism $\rho : G \to \operatorname{Sym}(X)$, the action is faithful when that homomorphism is injective, and an automorphism group $\operatorname{Aut}(X)$ is the subgroup of $\operatorname{Sym}(X)$ preserving whatever structure $X$ carries. The list is the entry point for the families that the rest of the category develops: the linear, classical, projective, affine, Euclidean, isometry, Möbius, conformal, symplectic, discrete and automorphism families, each of which is a catalogue of its own.

Every entry points to the article that introduces the group or the action. The article introduces nothing and proves nothing: it records what each group preserves, and it neither restates a definition nor gives a proof.

The article records examples and non-examples side by side. Beside the groups that act faithfully on a space it lists the actions that fail faithfulness — the action of $GL_n$ on the projective space, whose kernel is the scalars — the isometry group of a general Riemannian manifold, which is too small for the manifold to be a homogeneous space, the structure group of a bundle, which acts on the fibres and not on the base, and the mapping class group, which acts on the curve complex rather than on the surface by a faithful action of homeomorphisms, each with the failure named and the article that records it. The Erlangen program itself is the subject of *Transformation Groups and the Erlangen Program*, and the general theory is taken from *Transformation Groups*.

## The Transformations of a Set and the Hierarchy of Automorphisms

The hierarchy $\operatorname{Sym}(X) \supset \operatorname{Aut}(X, \text{structure}) \supset \cdots$ records that a transformation group is determined by what it is required to preserve: each layer of structure cuts down the group.

| Object | The property it has | Introduced in |
|---|---|---|
| the symmetric group $\operatorname{Sym}(X)$ | the group of all bijections of a bare set; the largest transformation group of $X$ | *Transformation Groups* |
| the symmetric group $S_n$ | $\operatorname{Sym}(\{1,\ldots,n\})$, of order $n!$ | *Transformation Groups*; *Groups* |
| an action $G \times X \to X$, $a\cdot x$ | a homomorphism $\rho : G \to \operatorname{Sym}(X)$; the realisation of an abstract group by transformations | *Transformation Groups*; *Group Actions and Structure* |
| a faithful action | $\ker\rho = 1$; the group is a subgroup of $\operatorname{Sym}(X)$ | *Transformation Groups* |
| the orbit and the stabiliser | $\operatorname{Orb}(x)$ and $\operatorname{Stab}(x)$, with the orbit–stabiliser theorem and $G/H$ for a transitive action | *Group Actions and Structure*; *Transformation Groups* |
| Cayley's embedding $G \hookrightarrow \operatorname{Sym}(G)$ | the left regular action; every group is a transformation group of itself | *Transformation Groups* |
| the automorphism group $\operatorname{Aut}(X)$ | the transformations preserving the structure on $X$; $\operatorname{Aut}(X) = \operatorname{End}(X)^\times$ | *Transformation Groups* |
| the inner automorphisms $\operatorname{Inn}(G)$ | the conjugations $x \mapsto gxg^{-1}$; $\operatorname{Inn}(G) \cong G/Z(G)$ | *Transformation Groups*; *List of Automorphism Groups* |
| the automorphism group $\operatorname{Aut}(G)$ of a group | the transformations preserving the group operation, with $\operatorname{Out}(G) = \operatorname{Aut}(G)/\operatorname{Inn}(G)$ | *List of Automorphism Groups* |
| the transformation group of a ring $\operatorname{Aut}(R)$ | the automorphisms preserving addition and multiplication; the Frobenius in prime characteristic | *Ring and Field Automorphisms*; *List of Automorphism Groups* |
| the transformation group of an algebra $\operatorname{Aut}_R(A)$ | the $R$-algebra automorphisms; $\operatorname{Der}_R(A)$ the infinitesimal ones | *Automorphisms and Derivations of Algebras* |
| the transformation group of a module $\operatorname{Aut}_A(M)$ | the $A$-linear automorphisms; $\operatorname{End}_A(M)$ the monoid | *Automorphisms of Modules over an Algebra* |

## The Families of Transformation Groups

Each family is the transformation group of a space with a definite structure, and each is developed in a catalogue or an article of its own. The table is the entry point of the category.

| Family | The structure preserved | Introduced in |
|---|---|---|
| the linear groups $GL(V)$, $SL(V)$ | the linear structure of a vector space | *The General Linear Group*; *List of Linear Geometric Groups* |
| the classical groups $O(V,Q)$, $U(V,h)$, $Sp(V,\omega)$ | a quadratic, Hermitian or symplectic form | *Matrix Groups and Classical Groups*; *List of Classical Geometric Groups* |
| the projective groups $PGL(V)$, $PSL(V)$, $PO$, $PSU$, $PSp$ | the incidence structure of a projective space; the quotients by the centre | *Projective Geometry*; *List of Projective Geometric Groups* |
| the affine group $\operatorname{Aff}(n) = \mathbb{R}^n \rtimes GL(n)$ | the affine structure; the automorphism group of affine space | *Affine Spaces and Translations*; *List of Affine and Euclidean Groups* |
| the Euclidean group $E(n) = \mathbb{R}^n \rtimes O(n)$ | the Euclidean distance and its isometries | *Euclidean Geometry*; *List of Affine and Euclidean Groups*; *List of Isometry and Symmetry Groups* |
| the similarity group $\operatorname{Sim}(n)$ | the distance up to a scalar; translations, rotations, reflections and dilatations | *Euclidean Geometry*; *List of Affine and Euclidean Groups* |
| the isometry groups $\operatorname{Isom}(\mathbb{R}^n)$, $\operatorname{Isom}(\mathbb{H}^n)$, $\operatorname{Isom}(S^n)$ | a metric; the model spaces of constant curvature | *Non-Euclidean Geometry*; *List of Isometry and Symmetry Groups* |
| the Möbius and conformal groups $\operatorname{Möb}(n)$, $\operatorname{Conf}(M)$ | a conformal structure; the Möbius group generated by inversions | *Möbius and Lie Sphere Geometry*; *Conformal Geometry*; *List of Möbius and Conformal Groups* |
| the symplectic group $Sp(2n,\mathbb{R})$ and the symplectomorphisms | a symplectic form, and the group of diffeomorphisms preserving it | *Symplectic Geometry*; *List of Symplectic Geometries* |
| the orthogonal group of a quadratic space | a quadratic form, through the reflection theorem of Cartan–Dieudonné | *Isometries and Orthogonal Transformations* |
| the discrete geometric groups | a lattice or a crystallographic structure; discreteness and cocompactness | *Symmetry, Point and Crystallographic Groups*; *List of Discrete Geometric Groups* |
| the homeomorphism and diffeomorphism groups | a topological or smooth structure; infinite-dimensional transformation groups | *Diffeomorphism Groups*; *List of Diffeomorphism and Homeomorphism Groups* |
| the mapping class group $\operatorname{Mod}(S)$ | the isotopy classes of homeomorphisms; it acts on the curve complex | *Mapping Class Groups* |
| the birational group $\operatorname{Bir}(X)$ | the birational equivalence of a variety | *Algebraic Geometry* |
| a Lie group acting on itself | the left translations; the group as a homogeneous space of itself | *Lie Groups*; *Homogeneous Spaces* |
| the Thompson groups $F$, $T$, $V$ | the piecewise-linear homeomorphisms of the interval, the circle and the Cantor set | *Thompson Groups and the Cantor Set* |
| the Galois group $\operatorname{Gal}(L/K)$ | the field automorphisms fixing $K$; the transformation group of a field extension | *Galois Theory*; *List of Automorphism Groups* |

## The Erlangen Program and the Klein Geometries

Klein's principle reads a geometry as the study of the invariants of a transformation group, and a geometry so presented is a pair $(G,H)$ with $G$ a Lie group, $H$ a closed subgroup and $G/H$ the homogeneous space. The program and its limits are the subject of *Transformation Groups and the Erlangen Program*, and the geometries it organises are catalogued separately.

| Object or principle | The statement or the structure | Introduced in |
|---|---|---|
| Klein's principle | a geometry is the study of the invariants of a transformation group; the correspondence $G \to \operatorname{Aut}(X)$ | *Transformation Groups and the Erlangen Program* |
| a Klein geometry $(G,H)$ | a Lie group and a closed subgroup, with the homogeneous space $G/H$ as the model space | *List of Klein Geometries*; *Homogeneous Spaces* |
| homogeneous spaces | $G/H$ with the smooth structure making $G \to G/H$ a submersion, of dimension $\dim G - \dim H$ | *Homogeneous Spaces*; *Lie Groups* |
| Euclidean, affine, projective geometry | the geometries of the corresponding groups $E(n)$, $\operatorname{Aff}(n)$, $PGL(n+1)$ | *List of Erlangen Program Geometries*; *List of Klein Geometries* |
| hyperbolic, spherical geometry | the geometries of $O(n,1)$ and $O(n+1)$; the space forms | *List of Erlangen Program Geometries*; *List of Riemannian Geometries* |
| conformal and Möbius geometry | the geometries of $O(n+1,1)$ and of the Möbius group | *List of Möbius and Conformal Groups*; *List of Erlangen Program Geometries* |
| symplectic geometry | the geometry of the symplectic group and the symplectic form | *List of Symplectic Geometries*; *List of Erlangen Program Geometries* |
| the limits of the program | a Riemannian manifold of general curvature is not a Klein geometry; its isometry group need not act transitively | *Transformation Groups and the Erlangen Program* |

## The Constructions on an Action

An action is a homomorphism $G \to \operatorname{Sym}(X)$, and the constructions of the group theory of actions are the transformations of the group into $\operatorname{Sym}(X)$ and of the set into its orbits.

| Object or construction | The property it has | Introduced in |
|---|---|---|
| the action on the cosets $G/H$ | the transitive $G$-set of the left cosets; every transitive $G$-set is of this form | *Group Actions and Structure*; *Transformation Groups* |
| the conjugation action $G$ on itself | $g \cdot x = gxg^{-1}$; its orbits are the conjugacy classes and its fixed points the centre | *Group Actions and Structure* |
| the fixed-point set $\operatorname{Fix}(a)$ | the points fixed by $a$; the fixed-point formula of Burnside's lemma counts them | *Group Actions and Structure* |
| the double coset $HaK$ | the orbits of $H$ on $G/K$; the decomposition that generalises the coset decomposition | *Group Actions and Structure* |
| the class equation | $\lvert G\rvert = \lvert Z(G)\rvert + \sum_i [G : C_G(x_i)]$; the counting identity of the conjugation action | *Group Actions and Structure* |
| the restriction of an action to a subgroup | $G$ acting on $X$ restricts to $H \leq G$; the orbits refine | *Group Actions and Structure*; *Transformation Groups* |
| the product action on $X \times Y$ | $g\cdot(x,y) = (gx, gy)$; the action of a direct product $G_1 \times G_2$ | *Group Actions and Structure* |
| the induced action on the powers | the action of $G$ on the subsets, on the $k$-subsets and on the functions of a $G$-set | *Group Actions and Structure* |
| Burnside's lemma | the number of orbits is the average number of fixed points, $\lvert X/G\rvert = \tfrac1{\lvert G\rvert}\sum_g \lvert\operatorname{Fix}(g)\rvert$ | *Group Actions and Structure* |

## Non-examples and Warnings

| Object | Why the expected statement fails | Introduced in |
|---|---|---|
| the action of $GL_n(K)$ on $P^{n-1}(K)$ | it is not faithful; the kernel is the group of scalars, and the faithful group is the projective quotient $PGL_n(K)$ | *Projective Geometry*; *List of Projective Geometric Groups* |
| the trivial action of a group on a set | it is not faithful, except for the trivial group; $\ker\rho = G$ | *Group Actions and Structure* |
| the isometry group of a general Riemannian manifold | it need not act transitively, so the manifold is not a homogeneous space; the Erlangen principle does not apply | *Transformation Groups and the Erlangen Program* |
| the structure group of a principal bundle | it acts on the fibres of the bundle and not on the base; it is a transformation group of the total space only through the local trivialisations | *Fibre Bundles, Connections and Curvature* |
| the mapping class group of a surface | it does not act by homeomorphisms on the surface itself; it acts faithfully on the set of isotopy classes of simple closed curves | *Mapping Class Groups* |
| an abstract group with no faithful action registered | a group is a transformation group only through an action; the correspondence $G \to \operatorname{Aut}(X)$ requires the action to be named | *Transformation Groups* |
| the symplectomorphism group of a symplectic manifold | it is infinite-dimensional and not the finite-dimensional symplectic group $Sp(2n,\mathbb{R})$ | *Symplectic Geometry* |

Objects that a reader may expect in a list of transformation groups, and does not find here.

| Object | Why it is not listed | Introduced in |
|---|---|---|
| $O(V,Q)$, $U(V,h)$, $Sp(V,\omega)$ as groups | they are defined by a form, so they are introduced among the classical geometric groups and are listed there | *List of Classical Geometric Groups* |
| the spin and pin groups | they are constructed from the Clifford algebra and are listed with it | *List of Clifford Algebras and Spin Groups* |
| the infinite-dimensional Lie groups | recorded with Hilbert's fifth problem; they are transformation groups without a finite dimension | *Hilbert's Fifth Problem and Infinite-Dimensional Lie Theory* |
| the absolute Galois group | it acts on the algebraic closure; it is not the transformation group of a finite-dimensional geometry | *Galois Cohomology*; *List of Automorphism Groups* |
| the $p$-adic algebraic groups | they act on buildings and on $p$-adic symmetric spaces; recorded among the topological groups | *List of Topological Groups*; *Buildings and Tits Systems* |

## Summary

This article has listed the transformation groups of the corpus: the transformations of a bare set and the hierarchy $\operatorname{Sym}(X) \supset \operatorname{Aut}(X)$, with the actions, orbits, stabilisers and automorphism groups of a group, a ring, an algebra and a module; the families in which the category is developed — the linear, classical, projective, affine, Euclidean, isometry, Möbius, conformal, symplectic, discrete, homeomorphism and automorphism families, each with the structure it preserves; and the Erlangen program, which reads a geometry as the invariants of a transformation group and presents it as a Klein geometry $G/H$. Beside the examples stand the non-examples: the unfaithful action on projective space, the trivial action, the isometry group of a general Riemannian manifold, the structure group of a bundle, and the mapping class group acting on the curve complex. The list introduces and proves nothing; it is the entry point of the geometric-group family of the corpus.

## Summary of Notation

A catalogue denotes its objects by name rather than by symbol. The symbols that appear in the tables are those of the introducing articles.

| Symbol | Meaning |
|---|---|
| $\operatorname{Sym}(X)$, $S_n$ | the symmetric group of a set; the symmetric group on $n$ letters |
| $\operatorname{Aut}(X)$, $\operatorname{End}(X)$ | the automorphism group and the endomorphism monoid of a structure |
| $\rho : G \to \operatorname{Sym}(X)$ | the permutation representation of an action; $\ker\rho = 1$ when faithful |
| $\operatorname{Orb}(x)$, $\operatorname{Stab}(x)$, $G/H$ | orbit, stabiliser and coset space of a transitive action |
| $\operatorname{Aut}(G)$, $\operatorname{Inn}(G)$, $\operatorname{Out}(G)$ | the automorphism, inner and outer groups of a group |
| $E(n)$, $\operatorname{Aff}(n)$, $\operatorname{Sim}(n)$ | the Euclidean, affine and similarity groups |
| $GL(V)$, $SL(V)$, $PGL(V)$, $PSL(V)$ | the linear and projective linear groups |
| $O(V,Q)$, $U(V,h)$, $Sp(V,\omega)$ | the classical groups of a quadratic, Hermitian and symplectic form |
| $\operatorname{Möb}(n)$, $\operatorname{Conf}(M)$ | the Möbius group and the conformal group |
| $\operatorname{Isom}(X)$, $\operatorname{Diff}(M)$, $\operatorname{Homeo}(X)$ | the isometry, diffeomorphism and homeomorphism groups |
| $\operatorname{Mod}(S)$, $\operatorname{Bir}(X)$ | the mapping class group and the birational group |
| $(G,H)$, $G/H$ | a Klein geometry and its homogeneous space |

## Further Reading

- Felix Klein, *Vergleichende Betrachtungen über neuere geometrische Forschungen* (Erlangen, 1872), for the original statement of the Erlangen programme, that a geometry is the study of the invariants of a transformation group.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (American Mathematical Society, 2001), for the homogeneous spaces, the Klein geometries and the correspondence between a geometry and its automorphism group.
- John L. Alperin and Rowen B. Bell, *Groups and Representations* (Springer, 1995), for group actions, automorphism groups and the realisation of a group by transformations.
- Benson Farb and Dan Margalit, *A Primer on Mapping Class Groups* (Princeton University Press, 2012), for the mapping class group and its action on the curve complex.
