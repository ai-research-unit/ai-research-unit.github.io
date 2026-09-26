# __List of Categories__

## Introduction

This article lists the categories the corpus meets, together with their objects, their morphisms and the functors between them. The categories are the ones attached to the algebraic layers — sets, posets, monoids, groups, abelian groups, rings and modules — and then the abstract categories the corpus builds on top of them: the additive and abelian categories, the Grothendieck categories, the derived and triangulated categories, the differential graded categories, the model categories and the higher categories, and the toposes that carry the sheaf-theoretic algebra.

Every entry points to the article that introduces the category and names its objects and morphisms. This article is a list: it introduces no definition, states no theorem, gives no proof, and carries no display mathematics. It records examples and non-examples side by side, a non-example being a category that fails one of the structural properties its neighbours have, with the failure named and the article that records it.

## Categories of the Algebraic Layers

Each layer of the object ladder carries its own category, whose objects are the structures of that layer and whose morphisms are the structure-preserving maps. The foundational article fixes the categories below the algebraic layers and names the algebraic ones; the module-theoretic articles develop the category of modules in detail.

| Category | Objects and morphisms | Introduced in |
|---|---|---|
| $\mathbf{Set}$ | sets and functions | *Universal Properties and Categories* |
| $\mathbf{Pos}$ | partially ordered sets and order-preserving maps | *Universal Properties and Categories* |
| $\mathbf{Mon}$ | monoids and monoid homomorphisms | *Universal Properties and Categories* |
| $\mathbf{Grp}$ | groups and group homomorphisms | *Universal Properties and Categories* |
| $\mathbf{Ring}$ | rings with unit and unital ring homomorphisms | *Universal Properties and Categories* |
| $R\text{-}\mathbf{Mod}$ | left $R$-modules and $R$-linear maps | *Module Categories* |
| $\mathbf{Mod}\text{-}R$, $R\text{-}\mathbf{mod}$ | right modules; finitely generated left modules | *Module Categories* |
| $\mathbf{Vect}_F$ | vector spaces over a field and linear maps | *Vector Spaces* |
| $R\text{-}\mathbf{Alg}$ | $R$-algebras and algebra homomorphisms | *Algebras* |
| $\mathsf{CAlg}_R$ | commutative unital $R$-algebras | *The Symmetric Algebra* |

## Functors and Natural Transformations

The maps between categories are the **functors**, the comparison between two functors is a **natural transformation**, and the equivalences of categories are the fully faithful and essentially surjective functors. The corpus meets the forgetful functors, whose left adjoints are the free constructions, the representable functors of the Yoneda embedding, the $\operatorname{Hom}$ and tensor functors that form the tensor–hom adjunction, and the derived functors of the homological articles.

| Functor or construction | The property it has | Introduced in |
|---|---|---|
| Functor $F : \mathcal{C} \to \mathcal{D}$ | preserves composition and identities; faithful, full, essentially surjective | *Universal Properties and Categories* |
| Natural transformation $\eta : F \Rightarrow G$ | a family of morphisms commuting with both functors | *Universal Properties and Categories* |
| Equivalence of categories | fully faithful and essentially surjective, hence invertible up to natural isomorphism | *Universal Properties and Categories* |
| Forgetful functor | discards structure; the typical right adjoint | *Universal Properties and Categories* |
| Free functor | left adjoint of a forgetful functor; the free monoid is the model case | *Universal Properties and Categories* |
| Representable functor | a functor naturally isomorphic to $\mathcal{C}(-,A)$; the Yoneda embedding | *Universal Properties and Categories* |
| Functor category $[\mathcal{C},\mathcal{D}]$, presheaf category $\widehat{\mathcal{C}}$ | functors as objects, natural transformations as morphisms | *Universal Properties and Categories* |
| Hom functor $\operatorname{Hom}_R(M,-)$ | left exact; right adjoint of $-\otimes_R M$ | *Module Categories* |
| Tensor functor $-\otimes_R M$ | right exact; left adjoint of $\operatorname{Hom}_R(M,-)$ | *The Balanced Product* |
| Derived functor $\mathbb{R}F$, $\mathbb{L}F$ | total right and left derived functors on the derived category | *Derived Functors* |
| Quillen functor | left or right adjoint between model categories with a derived adjunction | *Model Categories and Homotopy Theory* |

## Additive, Abelian and Grothendieck Categories

An **additive category** has a zero object, finite biproducts and abelian groups of morphisms; an **abelian category** adds kernels and cokernels with the coimage isomorphic to the image, which is exactly the structure in which the homological constructions of the corpus run. A **Grothendieck category** is an abelian category with a generator, small coproducts and exact filtered colimits. The motif is the category of modules, and the Freyd–Mitchell and Gabriel–Popescu theorems say how general the notion is.

| Category | The structure it has | Introduced in |
|---|---|---|
| Additive category | a zero object, biproducts and abelian hom groups | *Abelian and Grothendieck Categories* |
| Abelian category | additive with kernels, cokernels and $\operatorname{coim} \cong \operatorname{im}$ | *Abelian and Grothendieck Categories* |
| Grothendieck category | abelian with a generator, coproducts and exact filtered colimits | *Abelian and Grothendieck Categories* |
| Serre or localising quotient $\mathcal{A}/\mathcal{S}$ | the quotient of an abelian category by a localising subcategory | *Abelian and Grothendieck Categories* |
| $R\text{-}\mathbf{Mod}$ | the prototype abelian category; the input of the Freyd–Mitchell theorem | *Module Categories* |
| Non-example: $\mathbf{Grp}$ | has a zero object, the trivial group, but fails to be additive: the coproduct is the free product, not the direct product | *Abelian and Grothendieck Categories* |
| Non-example: $\mathbf{Set}$ | a cartesian closed category that fails to be abelian: it has no zero object | *Abelian and Grothendieck Categories* |
| Non-example: the category of fields | fails to have a coproduct, hence is not abelian | *Tensor Products of Algebras* |

## Derived and Triangulated Categories

A **derived category** is obtained from the homotopy category of complexes by formally inverting the quasi-isomorphisms; it carries a **triangulated** structure, in which the distinguished triangle replaces the exact sequence, and the derived functors become exact. A **differential graded category** is the many-object form of a differential graded algebra, and its derived category is again triangulated on the zeroth cohomology.

| Category | The structure it has | Introduced in |
|---|---|---|
| Category of complexes $\mathbf{Ch}(\mathcal{A})$ | chain complexes and chain maps over an abelian category | *Homological Algebra* |
| Homotopy category $K(\mathcal{A})$ | complexes and chain maps up to chain homotopy | *Derived Categories* |
| Derived category $D(\mathcal{A}) = K(\mathcal{A})[\Sigma^{-1}]$ | the localisation at the quasi-isomorphisms | *Derived Categories* |
| Triangulated category | an additive category with a translation and distinguished triangles | *Derived Categories* |
| Differential graded category | a category whose hom sets are complexes and whose composition is a chain map | *Differential Graded Categories* |
| Pretriangulated DG category | a DG category whose $H^0$ is triangulated | *Differential Graded Categories* |
| Perfect or compact objects $\mathrm{perf}(\mathcal{A})$ | the compact DG modules; the derived Morita invariant | *Differential Graded Categories* |
| Non-example: $K(\mathcal{A})$ | fails to be triangulated in the naive sense: the triangle is only canonical in $D(\mathcal{A})$ | *Derived Categories* |

## Homotopical and Higher Categories

A **model category** is a bicomplete category with classes of weak equivalences, cofibrations and fibrations from which a homotopy category is computed by formally inverting the weak equivalences. A **higher category** keeps the higher morphisms and the coherence between them, and its stable case is the home of the triangulated categories. These two frames belong to Part II, where the homotopy-theoretic notions are available.

| Category | The structure it has | Introduced in |
|---|---|---|
| Model category | weak equivalences, cofibrations and fibrations with the lifting and factorisation axioms | *Model Categories and Homotopy Theory* |
| Homotopy category $\operatorname{Ho}(\mathcal{C})$ | the localisation of a model category at its weak equivalences | *Model Categories and Homotopy Theory* |
| Simplicial category | a category enriched in simplicial sets, presenting an $\infty$-category | *Higher Algebra and Higher Categories* |
| Quasi-category | a simplicial set in which every inner horn has a filler | *Higher Algebra and Higher Categories* |
| Stable $\infty$-category | suspension and loops are inverse equivalences; the homotopy category is triangulated | *Higher Algebra and Higher Categories* |
| Non-example: the naive homotopy category of spaces | fails to be the localisation: its morphisms are homotopy classes, not the derived mapping spaces | *Model Categories and Homotopy Theory* |

## Categories with Extra Structure

Beyond the linear categories the corpus meets the **toposes**, which behave like the category of sets and carry a subobject classifier; the **sites** and their categories of **sheaves**; and the **monoidal categories**, in which the objects carry a product with a unit, whose monoids and their modules are the operads and their algebras.

| Category | The structure it has | Introduced in |
|---|---|---|
| Monoidal category | a category with a product functor, a unit and coherence axioms | *Operads* |
| Presheaf category $\widehat{\mathcal{C}}$ | functors $\mathcal{C}^{\mathrm{op}} \to \mathbf{Set}$ | *Presheaves and Sheaves* |
| Category of sheaves $\mathbf{Sh}(\mathcal{C},J)$ | presheaves satisfying the sheaf condition for a topology $J$ | *Sheaves on Sites* |
| Grothendieck topos | a category equivalent to the sheaves on a site | *Topoi* |
| Elementary topos | a cartesian closed category with a subobject classifier and effective equivalence relations | *Topoi* |
| Opposite category $\mathcal{C}^{\mathrm{op}}$ | the category with the arrows reversed | *Module Categories* |
| Slice category $\mathcal{C}/X$ | objects over $X$ and the commuting triangles between them | *Topoi* |
| Non-example: the category of groups as a topos | fails to have a subobject classifier | *Topoi* |

## Summary

The list gathers the categories of the corpus. The categories of the algebraic layers are $\mathbf{Set}$, $\mathbf{Pos}$, $\mathbf{Mon}$, $\mathbf{Grp}$, $\mathbf{Ring}$, $R\text{-}\mathbf{Mod}$, $\mathbf{Vect}_F$, $R\text{-}\mathbf{Alg}$ and $\mathsf{CAlg}_R$, with the functors, natural transformations and adjunctions between them. The abstract categories are the additive, abelian and Grothendieck categories, with the Serre quotients; the category of complexes, its homotopy category and the derived and triangulated categories, together with the differential graded and pretriangulated categories; the model categories, their homotopy categories, and the simplicial, quasi- and stable $\infty$-categories; and the monoidal categories, presheaf categories, sheaf categories and toposes. The non-examples — $\mathbf{Grp}$, $\mathbf{Set}$, the category of fields, the naive homotopy category of complexes, the naive homotopy category of spaces and the category of groups as a topos — each name the structural axiom that fails.

## Summary of Notation

The article denotes its objects by name; the symbols appearing in the tables are the standard ones of the introducing articles.

| Symbol | Meaning |
|---|---|
| $\mathcal{C}$, $\mathcal{D}$, $\mathcal{A}$, $\mathcal{B}$ | categories; $\mathcal{C}^{\mathrm{op}}$ the opposite category |
| $\mathcal{C}(A,B)$, $\operatorname{Hom}_{\mathcal{C}}(A,B)$ | morphisms from $A$ to $B$ |
| $\mathbf{Set}, \mathbf{Pos}, \mathbf{Mon}, \mathbf{Grp}, \mathbf{Ring}$ | categories of sets, posets, monoids, groups, rings |
| $R\text{-}\mathbf{Mod}$, $\mathbf{Mod}\text{-}R$, $R\text{-}\mathbf{mod}$ | modules over $R$, right and finitely generated |
| $\mathbf{Vect}_F$, $R\text{-}\mathbf{Alg}$, $\mathsf{CAlg}_R$ | vector spaces, algebras, commutative algebras |
| $F \dashv G$ | adjunction, $F$ left adjoint to $G$ |
| $\widehat{\mathcal{C}}$ | presheaf category |
| $\mathbf{Sh}(\mathcal{C},J)$ | category of sheaves on a site |
| $\mathbf{Ch}(\mathcal{A})$, $K(\mathcal{A})$, $D(\mathcal{A})$ | complexes, homotopy category, derived category |
| $\operatorname{Ho}(\mathcal{C})$ | homotopy category of a model category |
| $\mathcal{A}/\mathcal{S}$ | quotient by a localising subcategory |
| $\mathbb{R}F$, $\mathbb{L}F$ | total right and left derived functors |

## Further Reading

- Saunders Mac Lane, *Categories for the Working Mathematician* (Springer, 2nd ed. 1998), for the categories of the algebraic layers, functors, natural transformations and adjunctions.
- Peter Freyd, *Abelian Categories* (Harper and Row, 1964), for additive and abelian categories and the embedding theorem.
- Charles A. Weibel, *An Introduction to Homological Algebra* (Cambridge University Press, 1994), for the homotopy and derived categories and the triangulated formalism.
- Mark Hovey, *Model Categories* (American Mathematical Society, 1999), for the model-category axioms and the associated homotopy categories.
- Saunders Mac Lane and Ieke Moerdijk, *Sheaves in Geometry and Logic* (Springer, 1992), for presheaves, sheaves, sites and toposes.
