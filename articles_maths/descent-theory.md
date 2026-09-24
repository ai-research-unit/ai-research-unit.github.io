
# __Descent Theory__

## Introduction

Descent theory asks when an object of a category can be reconstructed from its pullbacks along the members of a covering, together with the compatibilities between those pullbacks. The compatibilities are the **descent data**: for a covering $\{f_i:c_i\to c\}$ and an object $X$ over $c$, the data are the objects $X_i$ over $c_i$ obtained by pullback, together with isomorphisms between the two pullbacks of $X_i$ and $X_j$ to the fibre product $c_i\times_cc_j$, satisfying the cocycle condition on the triple products. A **descent datum** is exactly such a family, and the question is whether every descent datum arises from an object of the base category. When it does, the covering is **effective for descent**, and the comparison functor from the objects over $c$ to the descent data is an equivalence; when it does not, the obstruction is measured by cohomology. The theory originated in Grothendieck's work on the flat topology of schemes, where the theorem that the descent data for modules are always effective under a faithfully flat cover became a fundamental tool, and it is the categorical form of the gluing condition of the previous article: a sheaf is a presheaf whose sections satisfy descent, and a stack is a fibred category whose objects satisfy descent.

This article develops fibred and indexed categories, descent data and the descent category for a covering, the comparison functor and effective descent, faithfully flat descent for modules with the Amitsur complex, the monadic form of the theorem through the Barr–Beck theorem, the descent spectral sequence for a covering computed with the machinery of *Spectral Sequences*, the stack condition and the stackification, the example of Galois descent, and the cohomological obstructions to descent. It follows *Sheaves on Sites*, *Topoi*, *Spectral Sequences*, *Ext and Tor*, *Homological Algebra*, *K-Theory of Rings* and *Modules*, and it closes the site-theoretic arc of the category.

Throughout, $(\mathcal{C},J)$ is a site with a terminal object, $f:S'\to S$ is a morphism, and $\{f_i:c_i\to c\}$ is a covering family; the fibre products are assumed to exist in $\mathcal{C}$. The categories fibred over $\mathcal{C}$ are treated concretely, that is, as indexed families of categories with base-change functors, without the 2-categorical machinery; the passage to the homotopy-coherent theory of $\infty$-categories, to higher stacks and to the derived version of descent belongs to Part II, whereandtreat it, and this article cites it without using it. The topological descent, that is, the descent for sheaves on a space and the continuous maps, belongs to Part II as well.

## Fibred and Indexed Categories

**Definition.** An **indexed category** over $\mathcal{C}$ is a pseudofunctor $\mathbb{X}:\mathcal{C}^{\mathrm{op}}\to\mathbf{Cat}$: to each object $S$ a category $\mathbb{X}_S$, to each morphism $f:S'\to S$ a base-change functor $f^*:\mathbb{X}_S\to\mathbb{X}_{S'}$, to each composition a coherent isomorphism $(fg)^*\cong g^*f^*$, and to each identity a coherent isomorphism $\mathrm{id}^*\cong\mathrm{id}$, subject to the usual associativity and unit conditions. The **total category** $\int\mathbb{X}$ has as objects the pairs $(S,X)$ with $X$ an object of $\mathbb{X}_S$ and as morphisms the pairs $(f,\phi)$ with $f:S'\to S$ and $\phi:f^*X\to X'$, and it is fibred over $\mathcal{C}$ by the projection $(S,X)\mapsto S$. A fibred category is a **stack** when it satisfies the descent condition below.

**Proposition.** An indexed category is equivalent to a fibration over $\mathcal{C}$ with a cleavage, and the base-change functors are unique up to a canonical isomorphism; the fibre $\mathbb{X}_S$ over $S$ is the subcategory of the total category of the objects lying over $S$ and the morphisms lying over $\mathrm{id}_S$. The formation of the total category is inverse to the passage from a fibration to its indexed category, up to equivalence.

*Proof.* The cleavage chooses a cartesian morphism over each base-change, and the coherence isomorphisms of the pseudofunctor are the unique comparison isomorphisms between the chosen cartesian morphisms; the two constructions are inverse by the universal property of the cartesian morphisms. $\square$

**Example.** The fundamental example is the indexed category of modules: for a ring homomorphism $f:R\to R'$ the base change is the extension of scalars $-\otimes_RR'$ of *Extension of Scalars*, the fibre over $R$ is the category of $R$-modules, and the total category is the category of modules over all the rings, fibred over the category of rings. Another example is the indexed category of quasi-coherent sheaves over a site of schemes, the geometric case treated in Part II.

## Descent Data for a Covering

**Definition.** Let $\mathbb{X}$ be an indexed category over $\mathcal{C}$ and let $\mathcal{U}=\{f_i:c_i\to c\}$ be a covering family. A **descent datum** for $\mathcal{U}$ with values in $\mathbb{X}$ is a family $(X_i,\phi_{ij})$ with $X_i\in\mathbb{X}_{c_i}$ and isomorphisms
$$
\phi_{ij}:f_{ij,2}^*X_j\xrightarrow{\ \sim\ }f_{ij,1}^*X_i
$$
over the fibre product $c_{ij}=c_i\times_cc_j$, where $f_{ij,1},f_{ij,2}$ are the two projections, subject to the **cocycle condition** on the triple fibre products $c_{ijk}$: the two ways of comparing $f^*X$ on $c_{ijk}$ coincide. The **descent category** $\mathrm{Desc}(\mathcal{U},\mathbb{X})$ has the descent data as objects and, as morphisms, the families of morphisms over the $c_i$ commuting with the isomorphisms $\phi_{ij}$.

**Definition.** The **comparison functor** is
$$
\mathbb{X}_c\longrightarrow\mathrm{Desc}(\mathcal{U},\mathbb{X}),\qquad X\mapsto (f_i^*X,\ \text{the canonical isomorphisms}),
$$
and the covering $\mathcal{U}$ is **effective for descent** in $\mathbb{X}$ if the comparison functor is an equivalence of categories. The fibred category $\mathbb{X}$ is a **stack** over the site $(\mathcal{C},J)$ if for every object $c$ and every covering family $\mathcal{U}$ of $c$ the comparison functor is an equivalence; it is a **prestack** if the comparison functor is fully faithful, that is, if the descent data have no nontrivial automorphisms beyond those coming from the base.

**Proposition.** The comparison functor is fully faithful for every covering if and only if the base-change functors are compatible with the localisation, which holds for the indexed categories of modules and of sheaves. For the indexed category of sets valued functors on a category, the stack condition is exactly the sheaf condition of *Sheaves on Sites*, and for the indexed category of categories the stack condition is the effective descent of the objects together with the compatible descent of the morphisms.

*Proof.* The full faithfulness of the comparison functor is the statement that a morphism of the base is determined by its pullbacks along a covering, which is the separatedness of the corresponding presheaf of morphisms. The identification with the sheaf condition is the description of a sheaf as a functor whose values satisfy the gluing axiom, applied to the constant indexed category with fibres the category of sets. $\square$

**Example.** For the covering of a set $c$ by the single map $\{c_i\}\to c$ of the members of an open cover in a topological space, a descent datum is precisely a compatible family of sections, and the descent condition is the sheaf condition; this is the sense in which descent generalises gluing, and the topological case is treated in Part II.

## Faithfully Flat Descent

**Theorem (Grothendieck, faithfully flat descent).** Let $R\to R'$ be a faithfully flat ring homomorphism. Then the comparison functor
$$
{}_{R}\mathbf{Mod}\longrightarrow\mathrm{Desc}(R'/R),\qquad M\mapsto (M\otimes_RR',\ \text{canonical}),
$$
from the category of $R$-modules to the category of $R'$-modules with descent data is an equivalence of categories. Equivalently, the category of $R$-modules is equivalent to the category of modules over the cosimplicial ring
$$
R\rightrightarrows R'\rightrightarrows R'\otimes_RR'\cdots
$$
built from the tensor powers, with the coface and codegeneracy maps given by the algebra structure and the unit.

*Proof (in outline).* The functor is fully faithful by the exactness of $-\otimes_RR'$ and the faithful flatness, which lets one descend the equalities of morphisms from the tensor powers. For the essential surjectivity, a descent datum $(M',\phi)$ is turned into an $R$-module by taking the equalizer of the pair of maps $M'\rightrightarrows M'\otimes_RR'$ whose first member is the descent isomorphism $\phi$ and whose second is the canonical map $m'\mapsto1\otimes m'$,
$$
0\to M\to M'\rightrightarrows M'\otimes_RR',
$$
and the flatness of $R'$ over $R$ shows that $M\otimes_RR'\cong M'$ compatibly with $\phi$; the cocycle condition is what makes the equalizer compute the correct module and makes the two constructions inverse. $\square$

**Definition.** The **Amitsur complex** of a faithfully flat cover $R\to R'$ is the cosimplicial object with terms $R'\otimes_RR'\otimes_R\cdots\otimes_RR'$ and the coface maps inserting $1$ in the consecutive positions; for an $R$-module $M$ the complex
$$
0\to M\to M\otimes_RR'\to M\otimes_RR'\otimes_RR'\to\cdots
$$
is the **Amitsur cochain complex**, and its cohomology computes the descent obstruction: $H^0$ is the module $M$ itself and the higher cohomology vanishes whenever the descent is effective.

**Proposition.** For a faithfully flat cover the Amitsur complex of $M$ is exact in positive degrees — it is a resolution of $M$ by the tensor powers of $R'$ — so $H^0=M$ and $H^n=0$ for $n\ge1$, and every descent datum of $R'$-modules is effective. Comparing the cohomology of the base with the cohomology of the cover in the derived setting is the Grothendieck spectral sequence of the composite of the two global-section functors, developed in *Spectral Sequences* and applied to the cosimplicial object of the cover; the obstruction to descending a more general structure is the usual Čech-style obstruction of *Sheaves on Sites*. The complex is the algebraic form of the cosimplicial object attached to a covering of a site.

*Proof (in outline).* The exactness of the Amitsur complex in positive degrees is faithfully flat descent applied to the modules of the complex: a cycle in degree $n$ is a tensor that becomes a coboundary after the faithfully flat extension, and faithful flatness lets the coboundary descend. The comparison with a spectral sequence is the standard one for a cosimplicial object, filtered by the cosimplicial degree, and belongs to the Grothendieck theory of *Spectral Sequences*. $\square$

**Example.** Let $k\to K$ be a finite Galois extension of fields with group $\Gamma$. Then the descent data for the cover are the $K$-vector spaces with a semilinear action of $\Gamma$, and the faithfully flat descent theorem specialises to **Galois descent**: the $k$-vector spaces are equivalent to the $K$-vector spaces with a semilinear $\Gamma$-action. The identification of the automorphism group with $\Gamma$ and the semilinearity belong to the theory of *Fields*, and the cohomological obstructions to the descent of more general structures are the Galois cohomology groups $H^1(\Gamma,-)$.

## Monadic Descent

**Definition.** A **monad** on a category $\mathcal{A}$ is an endofunctor $\mathbb{T}:\mathcal{A}\to\mathcal{A}$ with natural transformations $\eta:\mathrm{id}\to\mathbb{T}$ and $\mu:\mathbb{T}^2\to\mathbb{T}$ satisfying the associativity and unit laws. The **Eilenberg–Moore category** $\mathcal{A}^{\mathbb{T}}$ has as objects the pairs $(A,a)$ with $a:\mathbb{T}A\to A$ satisfying $a\eta_A=\mathrm{id}$ and $a\mu_A=a\mathbb{T}a$, and as morphisms the morphisms of $\mathcal{A}$ commuting with the structure maps.

**Theorem (Barr–Beck, monadicity).** Let $F:\mathcal{A}\to\mathcal{B}$ be a functor with a left adjoint $L:\mathcal{B}\to\mathcal{A}$, with the induced monad $\mathbb{T}=F\circ L$ on $\mathcal{B}$. Then the comparison functor $\mathcal{A}\to\mathcal{B}^{\mathbb{T}}$ is an equivalence if and only if $F$ creates coequalizers of the pairs of the form $(LFLx\rightrightarrows Lx)$ for every object $x$ of $\mathcal{B}$: the functor must reflect isomorphisms and preserve the coequalizers of the $F$-split pairs. When these conditions hold, the descent data over $\mathcal{A}$ are exactly the algebras over the monad, and the comparison functor is an equivalence.

**Corollary.** Faithfully flat descent for modules is the case of the monadicity theorem in which $\mathcal{B}=\mathbf{Mod}_R$, $\mathcal{A}=\mathbf{Mod}_{R'}$, and $F=-\otimes_RR'$: the monad is $M\mapsto M\otimes_RR'$ with the multiplication induced by the multiplication of $R'$, the Eilenberg–Moore algebras are the $R'$-modules with descent data, and the flatness and the faithfulness of the cover are exactly the conditions under which the coequalizers are created. The same pattern gives the descent for the modules over a sheaf of rings on a site and for the quasi-coherent sheaves of the geometric case of Part II.

*Proof.* The monadicity theorem is quoted; the identification of the algebras with the descent data is the computation of the monad in the module case, where the structure map $M\otimes_RR'\otimes_RR'\to M\otimes_RR'$ is the multiplication of the tensor factors and the coherence is the cocycle condition. The creation of the coequalizers is the flatness of $R'$ together with the faithfulness of the cover. $\square$

**Example.** For a cover by a single faithfully flat morphism that is also finite and locally free, the monad is the one attached to a finite projective algebra and the descent data are the modules over the algebra with the compatible action of the dual; this is the algebraic form of the descent of vector bundles, and the geometric case belongs to Part II.

## Stacks and Stackification

**Definition.** A **stack** over a site $(\mathcal{C},J)$ is an indexed category $\mathbb{X}$ over $\mathcal{C}$ such that for every object and every covering the comparison functor of descent data is an equivalence; equivalently, a fibred category over $\mathcal{C}$ in which the descent data for every covering are effective. A **stack in groupoids** is a stack whose fibres are groupoids, and the **stackification** of a prestack is the universal stack mapping to it, computed by the associated-sheaf construction on the descent categories, applied to the objects in each fibre and to the morphisms.

**Theorem (stackification).** Every prestack over a site has a stackification, unique up to equivalence, and the stackification is left exact in the sense that it preserves the finite limits of the prestacks; the stackification of the prestack of the sets is the associated sheaf, and the stackification of the prestack of the categories is the stack of the categories with the effective descent data. For a site with a subcanonical topology the representable prestacks are already stacks.

*Proof.* The stackification is constructed by composing the descent comparison with the associated sheaf functor on the fibres, and the universal property follows from the adjunction between the prestacks and the stacks; the identification with the associated sheaf is the case of the discrete fibres, and the left exactness is the exactness of the sheafification. $\square$

**Example.** For the site of a group $G$ with the trivial topology the stacks are the categories with an action of $G$, that is, the $G$-objects in the 2-category of categories; for the étale site of a scheme the stacks are the étale stacks, whose geometric theory belongs to Part II; the stack of the torsors under a sheaf of groups is the classifying stack, and its sections over a cover are the cohomology classes of $H^1$ of the cover.

**Remark.** The homotopy-coherent refinement of the descent, in which the cocycle condition holds only up to higher coherence and the stacks are replaced by the $\infty$-stacks, and the derived refinement, in which the modules are replaced by the complexes and the descent is the descent for the derived categories, belong to Part II, whereandtreat them. The present article uses only the strict, one-categorical form, which is the one needed for the algebraic descent of modules and sheaves.

## Summary

An indexed category over a site assigns a category to every object and a base-change functor to every morphism; a descent datum for a covering is a family of objects over the members of the cover with compatible isomorphisms over the fibre products satisfying the cocycle condition, and the covering is effective for descent when the comparison functor from the objects of the base to the descent data is an equivalence. The fundamental theorem is the faithfully flat descent of Grothendieck: for a faithfully flat ring homomorphism the category of modules over the base is equivalent to the category of modules over the cover equipped with descent data, and the equivalence is computed by the Amitsur complex, whose positive cohomology vanishes exactly when the descent is effective. The same statement is the module case of the monadicity theorem of Barr–Beck, where the descent data are the algebras over the monad induced by the extension of scalars, and the flatness and the faithfulness of the cover are the hypotheses under which the required coequalizers are created. A stack is an indexed category whose descent data are effective, every prestack has a stackification, and the stack condition on the discrete fibres is exactly the sheaf condition of *Sheaves on Sites*.

In this way descent theory unifies the gluing of the sheaves with the reconstruction of the algebraic objects from a cover, the cohomology of a site measures the obstruction to the effectivity of the descent, and the spectral sequence of the Amitsur complex relates the cohomology of the base to that of the cover. The strict theory is complete as an algebraic tool; the homotopy-coherent and the derived refinements, and the geometric descent of the quasi-coherent sheaves, belong to Part II.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{X}$ | indexed category over $\mathcal{C}$ |
| $\mathbb{X}_S$ | fibre over the object $S$ |
| $f^*$ | base-change functor |
| $\int\mathbb{X}$ | total category of the indexed category |
| $\mathcal{U}=\{f_i:c_i\to c\}$ | covering family |
| $\mathrm{Desc}(\mathcal{U},\mathbb{X})$ | descent category |
| $\phi_{ij}$ | descent isomorphism over $c_i\times_cc_j$ |
| $R\to R'$ | faithfully flat cover |
| Amitsur complex | $R\rightrightarrows R'\rightrightarrows R'\otimes_RR'\cdots$ |
| $\mathbb{T}$ | monad, $\mathbb{T}=F\circ L$ |
| $\mathcal{A}^{\mathbb{T}}$ | Eilenberg–Moore category of a monad |
| $H^p(G,M)$ | group cohomology of the descent |



## Further Reading

- Michael Artin, Alexander Grothendieck and Jean-Louis Verdier, *Théorie des topos et cohomologie étale des schémas (SGA 4)* (Springer Lecture Notes in Mathematics 269, 270, 305, 1972–1973), for the descent theory of sites and the stacks.
- Michael Barr and Jon Beck, "Homology and standard constructions", in *Seminar on Triples and Categorical Homology Theory* (Springer Lecture Notes in Mathematics 80, 1969), for the monadicity theorem.
- Alexander Grothendieck, *Technique de descente et théorèmes d'existence en géométrie algébrique (FGA)* (Séminaire Bourbaki, 1959–1962), for the faithfully flat descent and the Amitsur complex.
- Alexander Grothendieck, "Sur quelques points d'algèbre homologique", *Tohoku Mathematical Journal* 9 (1957), 119–221, for the spectral sequences and the abelian-category methods used in the descent.
- Peter T. Johnstone, *Sketches of an Elephant: A Topos Theory Compendium* (Oxford University Press, 2002), for the descent, the stacks and the internal theory.
- Saunders Mac Lane and Ieke Moerdijk, *Sheaves in Geometry and Logic: A First Introduction to Topos Theory* (Springer, 1992), for the descent theory in the topos-theoretic form.
- Angelo Vistoli, "Grothendieck topologies, fibered categories and descent theory", in *Fundamental Algebraic Geometry* (American Mathematical Society, 2005), for the systematic treatment of the fibred categories, the descent and the stacks.
