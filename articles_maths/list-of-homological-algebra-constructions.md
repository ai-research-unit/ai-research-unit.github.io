# __List of Homological Algebra Constructions__

## Introduction

This article lists the constructions of homological algebra the corpus meets: the complexes and exact sequences, the projective, injective and free resolutions, the derived functors with their long exact sequences, the functors $\operatorname{Ext}$ and $\operatorname{Tor}$, the spectral sequences and the derived and triangulated categories. For each construction the list records what it measures — the failure of exactness, the torsion, the extension classes, the filtration of a graded group, the resolution-independence of a derived functor — and the exact sequences it produces.

Every entry points to the article that introduces the construction. This article is a list: it introduces no definition, states no theorem, gives no proof, and carries no display mathematics. It records examples and non-examples side by side, a non-example being a construction that fails to have the invariance or the exactness its neighbour has, with the failure named and the article that records it.

## Complexes and Exact Sequences

A **chain complex** is a graded module with a square-zero endomorphism, and its **homology** measures the failure of the complex to be exact; a **chain map** commutes with the differentials, a **chain homotopy** is the algebraic form of a homotopy, and the **mapping cone** is the complex that carries the induced map on homology. A **short exact sequence** produces the **long exact sequence** in homology through the connecting homomorphism, and the **snake lemma** is its first instance.

| Construction | What it measures and produces | Introduced in |
|---|---|---|
| Chain and cochain complex $(C_\bullet,d_\bullet)$ | the data $d^2=0$; the complex that computes homology | *Homological Algebra* |
| Cycles, boundaries and homology $H_n(C)$ | how far the complex is from exact | *Homological Algebra* |
| Morphism of complexes | a map commuting with the differentials; it induces a map on homology | *Homological Algebra* |
| Chain homotopy $\varphi \simeq \psi$ | a map that induces the same map on homology | *Homological Algebra* |
| Mapping cone $\operatorname{Cone}(f)$ | the complex carrying the long exact sequence of a map | *Homological Algebra* |
| Short exact sequence | a sequence exact at three terms; the basic input of the theory | *Exact Sequences* |
| Snake lemma and the connecting homomorphism | the map producing the long exact sequence | *Exact Sequences* |
| Long exact sequence in homology | the exact sequence extending a short exact sequence of complexes | *Homological Algebra* |
| Splitting lemma | the criterion for a short exact sequence to split | *Exact Sequences* |
| Non-example: an additive functor that is not exact | fails to preserve exactness: the failure is what the derived functors measure | *Derived Functors* |
| Non-example: a non-additive functor | fails to have derived functors in the classical sense: additivity is required | *Derived Functors* |

## Resolutions

A **resolution** of a module is a complex exact except in degree zero, whose zeroth homology is the module; a **projective resolution** uses projectives, an **injective resolution** injectives, and a **free resolution** free modules. The **comparison theorem** states that any two resolutions are linked by a chain map unique up to homotopy, so that a functor evaluated on a resolution gives a resolution-independent answer; the **horseshoe lemma** builds a resolution of a middle term from resolutions of the ends.

| Construction | What it measures and produces | Introduced in |
|---|---|---|
| Projective resolution $P_\bullet \to M$ | the module as the cokernel of the last map; the input to the left derived functors | *Projective and Injective Modules* |
| Injective resolution $M \to I^\bullet$ | the module as the kernel of the first map; the input to the right derived functors | *Projective and Injective Modules* |
| Free resolution | a projective resolution by free modules; exists over every ring | *Homological Algebra* |
| Augmentation $\varepsilon$, $\eta$ | the map to or from the module, making the complex a resolution | *Homological Algebra* |
| Comparison theorem | maps of resolutions exist and are unique up to homotopy | *Homological Algebra* |
| Horseshoe lemma | resolutions of the ends of a short exact sequence give one of the middle | *Homological Algebra* |
| Filtration of a complex $F_pC$ | the data on which a spectral sequence is built | *Spectral Sequences* |
| Non-example: a resolution by non-projective modules | fails the comparison theorem: the answer depends on the resolution | *Homological Algebra* |
| Non-example: a module without a projective resolution | does not occur over a ring: enough projectives always exist in $R\text{-}\mathbf{Mod}$ | *Homological Algebra* |

## Derived Functors

The **right derived functors** of a left exact functor and the **left derived functors** of a right exact one are computed by evaluating the functor on a resolution and taking homology; they are independent of the resolution by the comparison theorem, the connecting homomorphism extends a short exact sequence to a long exact sequence, and the family is characterised as a universal delta-functor. The vanishing on **acyclic** objects, the technique of **dimension shifting** and the composition of functors are the computational tools.

| Construction | What it measures and produces | Introduced in |
|---|---|---|
| Right derived functor $R^nF$ | the failure of a left exact functor to be exact | *Derived Functors* |
| Left derived functor $L_nG$ | the failure of a right exact functor to be exact | *Derived Functors* |
| Connecting homomorphism $\delta^n$ | the map turning a short exact sequence into a long exact one | *Derived Functors* |
| Long exact sequence of derived functors | the exact sequence continuing the four terms of a half-exact functor | *Derived Functors* |
| Delta-functor | the abstract family of which the derived functors are the universal example | *Derived Functors* |
| Acyclic objects and dimension shifting | the objects on which the higher functors vanish; the device reducing a computation in degree $n$ to degree $1$ | *Derived Functors* |
| Grothendieck spectral sequence | the derived functors of a composite $G \circ F$ from those of $F$ and $G$ | *Spectral Sequences* |
| Non-example: a functor that is not left or right exact | fails to have the classical derived functors with the long exact sequence | *Derived Functors* |
| Non-example: a resolution by objects that are not $F$-acyclic | fails to compute the derived functor: only an $F$-acyclic resolution gives $H^n(F(Q^\bullet)) \cong R^nF(A)$ | *Derived Functors* |

## Ext and Tor

The **Ext groups** $\operatorname{Ext}_R^n(M,N)$ are the right derived functors of $\operatorname{Hom}_R(M,-)$, with $\operatorname{Ext}^1$ classifying the extensions of $M$ by $N$; the **Tor groups** $\operatorname{Tor}_n^R(M,N)$ are the left derived functors of $-\otimes_R N$, with $\operatorname{Tor}_1$ detecting the torsion. Both are balanced — Ext computable from either variable, Tor from either — and both produce the long exact sequences, the Künneth and universal-coefficient theorems and the group cohomology as the case $R = \mathbb{Z}[G]$.

| Construction | What it measures and produces | Introduced in |
|---|---|---|
| $\operatorname{Ext}_R^n(M,N)$ | the right derived functors of $\operatorname{Hom}_R(M,-)$; the extension classes in degree $1$ | *Ext and Tor* |
| $\operatorname{Tor}_n^R(M,N)$ | the left derived functors of $-\otimes_R N$; the torsion in degree $1$ | *Ext and Tor* |
| $\operatorname{Ext}^1(M,N)$ | the extensions $0 \to N \to E \to M \to 0$ up to equivalence | *Ext and Tor* |
| $\operatorname{Tor}_1(M,N)$ | the torsion pairing; $\operatorname{Tor}_1(M,\mathbb{Z}/n\mathbb{Z}) = M/nM$ | *Ext and Tor* |
| Balance of Ext and Tor | Ext computable from either variable, Tor from either | *Ext and Tor* |
| Long exact sequences in Ext and Tor | the exact sequences produced by a short exact sequence in either variable | *Ext and Tor* |
| Künneth theorem | the homology of a tensor product of complexes from the homologies | *Ext and Tor* |
| Universal coefficient theorem | the relation of homology with arbitrary coefficients to homology with $\mathbb{Z}$ coefficients | *Ext and Tor* |
| Group cohomology $H^n(G,M)$ | the case $R = \mathbb{Z}[G]$; the cohomology of a group | *Group Cohomology* |
| Schur multiplier $H_2(G,\mathbb{Z})$ | the second homology, the kernel of the universal central extension | *Group Cohomology* |
| Non-example: $\operatorname{Ext}^1(M,N)$ for a free $M$ | vanishes over a field or a free module: the sequence always splits | *Ext and Tor* |
| Non-example: $\operatorname{Tor}_1(M,N)$ for a flat $N$ | vanishes: flatness is exactly the vanishing of $\operatorname{Tor}_1$ | *Ext and Tor* |

## Spectral Sequences

A **spectral sequence** is a sequence of pages $E^r$ with differentials, converging to the graded pieces of the homology of a filtered object; it replaces one unknown group by successive approximations. The **spectral sequence of a double complex**, the **Grothendieck spectral sequence** of a composite of functors and the **five-term exact sequence** are the algebraic cases; the **Lyndon–Hochschild–Serre spectral sequence** of a group extension and the **Künneth and base-change spectral sequences** are the computed examples.

| Construction | What it measures and produces | Introduced in |
|---|---|---|
| Filtered complex and associated graded | the data producing the spectral sequence; $\operatorname{gr}_pC = F_pC/F_{p+1}C$ | *Spectral Sequences* |
| Pages $E^r_{p,q}$ and differentials $d^r$ | the successive approximations of the answer | *Spectral Sequences* |
| Convergence $E^2_{p,q} \Rightarrow H_{p+q}$ | the stabilisation of the pages to the graded pieces of the homology | *Spectral Sequences* |
| Spectral sequence of a double complex | the two filtrations of the total complex; the horizontal and vertical homology | *Spectral Sequences* |
| Grothendieck spectral sequence | the derived functors $R^pG(R^qF(A))$ as the $E_2$-page | *Spectral Sequences* |
| Five-term exact sequence | the low-degree terms of a converging spectral sequence | *Spectral Sequences* |
| Edge homomorphisms | the maps from the corner terms to the target | *Spectral Sequences* |
| Lyndon–Hochschild–Serre spectral sequence | the spectral sequence of a group extension | *Spectral Sequences* |
| Künneth and base-change spectral sequences | the algebraic applications of the machinery | *Spectral Sequences* |
| Non-example: a spectral sequence that does not converge | fails to give the graded pieces: convergence requires a bounded filtration or a first-quadrant page | *Spectral Sequences* |
| Non-example: reading $E^2$ as the answer | fails to account for the differentials: only $E^\infty$ gives the graded pieces | *Spectral Sequences* |

## Derived and Triangulated Categories

The **derived category** $D(\mathcal{A})$ is the localisation of the category of complexes at the quasi-isomorphisms, and it makes the derived functors into ordinary functors: $\operatorname{Hom}$ becomes $\mathbb{R}\operatorname{Hom}$, the tensor product becomes $\otimes^{\mathbb{L}}$, and a short exact sequence becomes a **distinguished triangle** in the **triangulated** structure. The homotopy category $K(\mathcal{A})$ is the place where the computations are made, and the bounded variants $D^\pm$, $D^b$ are the ones used by the later articles.

| Construction | What it measures and produces | Introduced in |
|---|---|---|
| Homotopy category $K(\mathcal{A})$ | complexes modulo chain homotopy; the intermediate step of the construction | *Derived Categories* |
| Localisation at the quasi-isomorphisms | the formal inversion producing the derived category | *Derived Categories* |
| Derived category $D(\mathcal{A})$, $D^\pm$, $D^b$ | the category in which the derived functors are exact | *Derived Categories* |
| Shift $C[n]$ and translation functor $T$ | the structure making the triangles stable under shift | *Derived Categories* |
| Distinguished triangle $X \to Y \to Z \to TX$ | the replacement of the exact sequence; it produces the long exact sequence in homology | *Derived Categories* |
| Triangulated category | the additive category with the shift and the triangles, satisfying the axioms | *Derived Categories* |
| $\mathbb{R}\operatorname{Hom}_R(M,N)$ and $M \otimes_R^{\mathbb{L}} N$ | the derived hom and tensor; the exact functors on the derived category | *Derived Categories* |
| $\operatorname{Hom}_{D(\mathcal{A})}(M,N[n]) = \operatorname{Ext}^n_{\mathcal{A}}(M,N)$ | the identification of the derived-category hom groups with Ext | *Derived Categories* |
| Perfect complexes | the complexes quasi-isomorphic to bounded complexes of finitely generated projectives; a full triangulated subcategory | *Derived Categories* |
| Equivalence for a ring of finite global dimension | $D^b(R\text{-}\mathbf{Mod}) \cong K^b(R\text{-}\mathbf{Proj})$, so the derived category adds nothing in that case | *Derived Categories* |
| Derived equivalence and tilting | the equivalence induced by a tilting module; two derived equivalent algebras | *Tilting Theory* |
| Non-example: the naive category of complexes | fails to be derived: quasi-isomorphisms are not yet invertible | *Derived Categories* |
| Non-example: the derived category as an abelian category | fails to be abelian in general, which is why the triangle replaces the exact sequence | *Derived Categories* |

## Summary

The list gathers the homological constructions of the corpus. The complex and the exact sequence supply the homology, the chain maps and homotopies, the mapping cone and the long exact sequence; the resolutions supply the projective, injective and free inputs, with the comparison theorem making the answer independent of the choice; the derived functors continue a half-exact functor into a long exact sequence and are characterised as universal delta-functors; $\operatorname{Ext}$ and $\operatorname{Tor}$ are the derived functors of $\operatorname{Hom}$ and of the tensor product, balanced in their two variables, with $\operatorname{Ext}^1$ classifying extensions, $\operatorname{Tor}_1$ detecting torsion and group cohomology as the case of a group ring; the spectral sequences organise the homology of a filtered or doubly graded object into pages that converge to the answer, with the Grothendieck, Lyndon–Hochschild–Serre and Künneth cases as the computed examples; and the derived and triangulated categories repackage the whole theory into a single additive category in which the triangle replaces the exact sequence and the derived functors are exact. The non-examples — a non-exact functor, a non-additive functor, a resolution by non-projective objects, a resolution by objects that are not acyclic for the functor, a vanishing Ext or Tor with the reason, a non-convergent spectral sequence, the misreading of $E^2$ as the answer, the naive category of complexes and the derived category mistaken for an abelian category — each name the failure.

## Summary of Notation

The article denotes its objects by name; the symbols appearing in the tables are those of the introducing articles.

| Symbol | Meaning |
|---|---|
| $(C_\bullet,d_\bullet)$, $H_n(C)$ | chain complex, homology |
| $Z_n$, $B_n$ | cycles and boundaries |
| $\operatorname{Cone}(f)$ | mapping cone |
| $P_\bullet \to M$, $M \to I^\bullet$ | projective and injective resolutions |
| $R^nF$, $L_nG$ | right and left derived functors |
| $\operatorname{Ext}_R^n(M,N)$, $\operatorname{Tor}_n^R(M,N)$ | Ext and Tor |
| $E^r_{p,q}$, $d^r$, $E^\infty_{p,q}$ | pages, differentials, stable terms of a spectral sequence |
| $K(\mathcal{A})$, $D(\mathcal{A})$, $D^b$ | homotopy and derived categories |
| $\mathbb{R}\operatorname{Hom}$, $\otimes^{\mathbb{L}}$ | derived hom and tensor |
| $X \to Y \to Z \to TX$ | distinguished triangle |
| $H^n(G,M)$ | group cohomology |
| $\mathbb{Z}$, $\mathbb{Z}[G]$ | the integers, and the group ring over them |

## Further Reading

- Sergei Gelfand and Yuri Manin, *Methods of Homological Algebra* (Springer, 2nd ed. 2003), for complexes, resolutions, derived functors and spectral sequences.
- Charles Weibel, *An Introduction to Homological Algebra* (Cambridge University Press, 1994), for Ext and Tor, the spectral sequences and the derived categories.
- Saunders Mac Lane, *Homology* (Springer, 1995), for the classical treatment of the functors $\operatorname{Ext}$ and $\operatorname{Tor}$ and the Künneth and universal-coefficient theorems.
- Amnon Neeman, *Triangulated Categories* (Princeton University Press, 2001), for the triangulated structure, the distinguished triangles and the derived categories.
