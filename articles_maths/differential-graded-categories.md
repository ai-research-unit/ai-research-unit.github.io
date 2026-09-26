
# __Differential Graded Categories__

## Introduction

A **differential graded category** is a category whose morphism sets are complexes and whose composition is a chain map. It is the many-object form of a differential graded algebra, and it is the setting in which the homological constructions of this Part are closed under passage to modules: the category of DG modules over a DGA is a DG category, and the resolutions, homotopies and derived categories of *Differential Graded Algebras* generalise verbatim once the objects are allowed to be many.

The article is the tenth of the category. It follows *Differential Graded Algebras*, of which it is the many-object generalisation, and it precedeswhere the composition is weakened to a family of higher operations, andwhose defining condition is a condition on a DG category with finitely many objects. Its three structural results are the construction of the **derived category** of a DG category as the localisation of the homotopy category at the quasi-isomorphisms, the **pretriangulated** structure that makes $H^0$ of a DG category triangulated, and the **derived Morita theory** that identifies the DG categories with equivalent derived categories. The tabulation of these results follows *Derived Categories*, where the triangulated formalism is developed for the derived category of an abelian category.

The article is algebraic. The model-category and higher-category formulations of the homotopy theory of DG categories, the topological constructions of the dg quotient in the homotopy-theoretic sense, and the geometric DG categories associated with spaces and sheaves belong to Part II, where the topological notions are available, and they are deferred. No manifold, no sheaf on a space, no spectrum and no norm is used.

Throughout, $k$ is a commutative ring with identity, later a field; a complex of $k$-modules is $\mathbb{Z}$-graded with a differential of degree $-1$; the Koszul sign rule $ab = (-1)^{\lvert a\rvert\lvert b\rvert}ba$ of *Differential Graded Algebras* is in force; and all DG structures are linear over $k$.

## Differential Graded Categories

**Definition.** A **differential graded category** $\mathcal{A}$ over $k$ consists of:

1. a class of objects $\operatorname{Ob}\mathcal{A}$;
2. for each pair $x,y$ of objects a complex of $k$-modules $\operatorname{Hom}_{\mathcal{A}}(x,y)$ whose elements are the **morphisms of degree $n$** in degree $n$;
3. for each triple $x,y,z$ a morphism of complexes $\circ : \operatorname{Hom}_{\mathcal{A}}(y,z)\otimes_k\operatorname{Hom}_{\mathcal{A}}(x,y) \to \operatorname{Hom}_{\mathcal{A}}(x,z)$, the **composition**, satisfying
   $$
   (f\circ g)\circ h = f\circ(g\circ h) ;
   $$
4. for each object $x$ a degree-$0$ cycle $1_x \in \operatorname{Hom}_{\mathcal{A}}(x,x)$ with $1_x\circ f = f$ and $g\circ1_x = g$.

The composition being a morphism of complexes means $d(f\circ g) = (df)\circ g + (-1)^{\lvert f\rvert}f\circ dg$, the graded Leibniz rule; the objects and the cycles of degree $0$ together with homotopy classes of morphisms will be seen to form the **homotopy category**.

**Definition.** A **DG functor** $F : \mathcal{A}\to\mathcal{B}$ is a map on objects together with morphisms of complexes $F_{x,y} : \operatorname{Hom}_{\mathcal{A}}(x,y)\to\operatorname{Hom}_{\mathcal{B}}(Fx,Fy)$ preserving the composition and the units. A DG functor is **quasi-fully faithful** if each $F_{x,y}$ is a quasi-isomorphism, and a **quasi-equivalence** if in addition every object of $\mathcal{B}$ is isomorphic in $H^0(\mathcal{B})$ to an object in the image.

**Definition.** The **homotopy category** $H^0(\mathcal{A})$ has the same objects as $\mathcal{A}$, and morphisms

$$
\operatorname{Hom}_{H^0(\mathcal{A})}(x,y) = H^0\bigl(\operatorname{Hom}_{\mathcal{A}}(x,y)\bigr) = \ker\bigl(d : \operatorname{Hom}^0\to\operatorname{Hom}^1\bigr)\big/\operatorname{im}\bigl(d : \operatorname{Hom}^{-1}\to\operatorname{Hom}^0\bigr) .
$$

Thus a morphism in $H^0(\mathcal{A})$ is a homotopy class of degree-$0$ cycles, and the composition is induced by that of $\mathcal{A}$; the definition is a verbatim generalisation of the homotopy category of DG modules of *Differential Graded Algebras*.

**Example (a DGA with one object).** Let $A$ be a DGA. The DG category with one object $x$ and $\operatorname{Hom}(x,x) = A$ is a DG category; conversely every DG category with one object is a DGA. This is the precise sense in which a DG category is an "algebra with several objects", and it is why every notion of the previous article has a many-object generalisation and every theorem about DG categories specialises to a theorem about DGAs.

**Example (the DG category of complexes).** Let $A$ be a DGA. The **DG category $\operatorname{DG}(A)$ of DG $A$-modules** has as objects the DG $A$-modules, and

$$
\operatorname{Hom}_{\operatorname{DG}(A)}(M,N)^n = \operatorname{Hom}^n_A(M,N) = \prod_{i\in\mathbb{Z}}\operatorname{Hom}_k(M_i,N_{i+n}) ,
$$

with differential $(df)(m) = d_Nf(m) - (-1)^{\lvert f\rvert}f(d_Mm)$ and composition the composition of maps. Then $\operatorname{Hom}^0$-cycles are the morphisms of DG modules, $\operatorname{Hom}^0$-boundaries are the null-homotopic maps, and $H^0(\operatorname{DG}(A)) = K(A)$ is exactly the homotopy category of *Differential Graded Algebras*. Taking $A = k$ gives the DG category of complexes of $k$-modules, written $\mathbf{Ch}(k)$.

**Example (a dg category from an algebra and a set of modules).** Let $A$ be a $k$-algebra and let $M_1,\dots,M_n$ be $A$-modules with a chosen projective resolution $P_i\to M_i$. The DG category with objects $1,\dots,n$ and $\operatorname{Hom}(i,j) = \operatorname{Hom}_A(P_i,P_j)$ with the differential $f\mapsto d_Pf - (-1)^{\lvert f\rvert}fd_P$ has $H^0$ equal to the full subcategory of the derived category $D(A)$ on the classes of the $M_i$. Every finite configuration of objects of a derived category can be encoded in this way, and this is the construction by which a DG category carries a homological invariant of an algebra.

**Proposition.** Let $\mathcal{A}$ be a DG category and $x,y\in\operatorname{Ob}\mathcal{A}$. Then $\operatorname{Hom}_{\mathcal{A}}(x,x)$ is a DGA, the **endomorphism DGA** of $x$, and $\operatorname{Hom}_{\mathcal{A}}(x,y)$ is a DG left module over $\operatorname{Hom}(y,y)$ and a DG right module over $\operatorname{Hom}(x,x)$, so that it is a DG bimodule.

*Proof.* The composition restricts to $\operatorname{Hom}(x,x)\otimes\operatorname{Hom}(x,x)\to\operatorname{Hom}(x,x)$, which is associative with the unit $1_x$ and compatible with the differential; the graded Leibniz rule is inherited from the composition being a chain map. The module structures are the two restrictions of the composition, and their compatibility is the associativity of $\circ$. $\square$

## Modules over a Differential Graded Category

**Definition.** Let $\mathcal{A}$ be a small DG category. A **DG module** over $\mathcal{A}$ (equivalently, a **DG functor** $\mathcal{A}\to\mathbf{Ch}(k)$) consists of a complex $M(x)$ for each object $x$ and, for each pair $x,y$, a morphism of complexes $\operatorname{Hom}_{\mathcal{A}}(x,y)\otimes_kM(x)\to M(y)$ compatible with the composition and the units. A **morphism of DG modules** is a family $f_x : M(x)\to N(x)$ compatible with the actions, and the collection of DG modules is itself a DG category $\mathcal{A}\text{-Mod}$ with $\operatorname{Hom}_{\mathcal{A}\text{-Mod}}(M,N)^n = \prod_x\operatorname{Hom}^n_k(M(x),N(x))$ with the sum differential.

**Example (the representable modules).** For an object $x$ the **representable** DG module $\mathbf{h}_x = \operatorname{Hom}_{\mathcal{A}}(x,-)$ is defined by $\mathbf{h}_x(y) = \operatorname{Hom}_{\mathcal{A}}(x,y)$; the Yoneda lemma, in its DG form, states that the DG module morphisms $\mathbf{h}_x\to M$ are exactly the elements of $M(x)$ of degree $0$ commuting with the differentials. The **free** DG modules are the direct sums of the representables, and the DG category of DG modules over $\mathcal{A}$ is the same thing as the DG category of DG modules over the DG "algebra" $\mathcal{A}$ in the many-object sense.

**Definition.** A DG module $M$ is **semi-free** if it is the union of a transfinite chain of submodules obtained from free modules by adjoining generators one at a time, and **h-projective** if for every acyclic DG module $N$ the complex $\operatorname{Hom}_{\mathcal{A}\text{-Mod}}(M,N)$ is acyclic. A DG module $M$ is **compact** (or **perfect**) if the functor $\operatorname{Hom}(M,-)$ commutes with arbitrary direct sums; the full DG subcategory of compact DG modules is written $\mathrm{perf}(\mathcal{A})$.

**Theorem (standard).** Let $\mathcal{A}$ be a small DG category.

1. Every DG module admits a semi-free resolution, and the category of DG modules has enough h-projectives.
2. The compact DG modules are exactly the DG modules that are homotopy equivalent to a direct summand of a finite semi-free module, and they form a DG category $\mathrm{perf}(\mathcal{A})$ closed under the operations of shift and cone.
3. The representable modules $\mathbf{h}_x$ are compact when $\mathcal{A}$ has finite-dimensional Hom complexes, and the Yoneda embedding $\mathcal{A}\to\mathrm{perf}(\mathcal{A})$, $x\mapsto\mathbf{h}_x$, is a quasi-fully faithful DG functor.

*Proof (outline).* Statement 1 is the generator-by-generator construction of the previous article carried out over the many objects of $\mathcal{A}$; statement 2 is the identification of the compact objects of a category of DG modules with the finite semi-free ones, which is the same argument as the corresponding statement for modules over a ring, applied to the free modules on the representables. Statement 3 follows from the Yoneda lemma: $\operatorname{Hom}(\mathbf{h}_x,N)\cong N(x)$, so $\operatorname{Hom}(\mathbf{h}_x,-)$ commutes with direct sums, and the finite-dimensionality of the Hom complexes of $\mathcal{A}$ makes the direct sum of finitely many representables compact. $\square$

## The Derived Category of a DG Category

**Definition.** The **derived category** $D(\mathcal{A})$ of a small DG category $\mathcal{A}$ is the localisation of the homotopy category $H^0(\mathcal{A}\text{-Mod})$ at the quasi-isomorphisms. Equivalently it is $H^0$ of the DG category of h-projective DG modules, or of the semi-free DG modules, by the resolution theorem; the equivalence of the descriptions is the many-object form of the statement for a DGA, and the construction of the localisation by locally presentable methods is algebraic, the model-categorical presentation being Part II's.

**Theorem (standard).** Let $\mathcal{A}$ be a small DG category.

1. $D(\mathcal{A})$ is a triangulated category, with the shift induced by the shift of complexes and the distinguished triangles induced by the mapping cones.
2. The compact objects of $D(\mathcal{A})$ are the objects of $H^0(\mathrm{perf}(\mathcal{A}))$, and $D(\mathcal{A})$ is compactly generated when $\mathcal{A}$ has finitely many objects and finite-dimensional Hom complexes.
3. A DG functor $F : \mathcal{A}\to\mathcal{B}$ induces a triangulated functor $D(\mathcal{A})\to D(\mathcal{B})$; $F$ is a quasi-equivalence if and only if $F$ is fully faithful on $H^0$ and essentially surjective, and then $D(\mathcal{A})\simeq D(\mathcal{B})$.
4. Every quasi-equivalence of DG categories induces an equivalence of derived categories, and the **derived Morita theory** states the converse: two small DG categories have equivalent derived categories if and only if their DG categories of compact modules are quasi-equivalent,
   $$
   D(\mathcal{A})\simeq D(\mathcal{B}) \iff \mathrm{perf}(\mathcal{A})\simeq_{\mathrm{qe}}\mathrm{perf}(\mathcal{B}) ,
   $$
   where $\simeq_{\mathrm{qe}}$ denotes quasi-equivalence. In that case $\mathcal{A}$ and $\mathcal{B}$ are **derived Morita equivalent**.

*Proof (outline).* Statement 1: the shift and the cone are given by the corresponding operations on complexes, and the axioms of a triangulated category are verified on the level of cones; statement 2 is the compactness criterion for the semi-free modules; statement 3 is the Yoneda embedding applied to $\mathcal{B}$-modules restricted along $F$. Statement 4 is the many-object form of the tilting theory: a quasi-equivalence $\mathrm{perf}(\mathcal{A})\to\mathrm{perf}(\mathcal{B})$ induces an equivalence of the DG categories of all modules and hence of the derived categories, while an equivalence of derived categories preserves the compact objects and restricts to a quasi-equivalence of the compact DG categories. $\square$

**Example (Morita equivalence of algebras as a special case).** Let $A$ and $B$ be $k$-algebras, regarded as DG categories with one object, concentrated in degree $0$. Then $D(\mathcal{A})\simeq D(\mathcal{B})$ if and only if $A$ and $B$ are Morita equivalent in the classical sense: the equivalence of derived categories of DG modules restricts to an equivalence of the categories of modules, because the objects in degree $0$ are the only ones present. The derived Morita theory of the theorem is therefore a genuine generalisation of the Morita equivalence of algebras, in which a DG category can have several objects and a nontrivial cohomological grading, and it is the reason the theory is the natural home of tilting theory.

**Example (the derived category of a ring, and of the polynomial algebra).** For a ring $R$, regarded as a DG category with one object, $D(R)$ is the classical derived category of *Derived Categories*, and $\mathrm{perf}(R)$ consists of the perfect complexes, that is, the bounded complexes of finitely generated projective modules. For the polynomial algebra $k[x_1,\dots,x_n]$ the DG category of compact modules is generated by the free module of rank one, and the equivalence of the derived category with the DG category of DG modules over the Koszul dual is the Koszul duality of *Koszul Duality* read on the level of DG categories: the Koszul dual of the symmetric algebra is the exterior algebra, and the Koszul complex is the tilting object realising the equivalence.

## Why the Enrichment is Necessary

The categories $D(\mathcal{A})$ of the previous section are triangulated, and the triangulated formalism is adequate for the statement of many results of *Derived Categories*; it is not adequate for their proofs, and the DG enrichment repairs exactly the defects. The three defects are these.

**The cone is not functorial.** In a triangulated category the cone of a morphism is well defined only up to a non-canonical isomorphism, because the axioms of a triangulated category require the existence of a triangle completing a morphism but not the functoriality of the completion. In a pretriangulated DG category the cone of a morphism of DG modules is a concrete complex, and the assignment $f\mapsto\operatorname{Cone}(f)$ is functorial on the level of the DG category, not merely on the level of the homotopy category.

**The Hom sets have no higher structure.** In a triangulated category the only structure on morphisms is the abelian group structure, and the composition is not part of the data beyond being a bilinear map. In a DG category the Hom complexes carry all the higher operations, and the information lost in passing to $H^0$ is exactly the information that the homotopy transfer allows one to recover up to quasi-isomorphism.

**The quotient is not computable.** The Verdier quotient of a triangulated category by a triangulated subcategory exists, but its construction is not compatible with the formation of Hom sets in a way that admits functorial calculations. The DG quotient of Keller's theorem is compatible, and it produces the Verdier quotient on $H^0$ while remaining a DG category.

**Definition.** A **DG enhancement** of a triangulated category $\mathcal{T}$ is a pretriangulated DG category $\mathcal{A}$ with $H^0(\mathcal{A})\simeq\mathcal{T}$. The enhancement is unique when it exists, in the sense that two enhancements of the same triangulated category that are both generated by a set of objects with finite-dimensional Hom complexes are quasi-equivalent; the uniqueness is a consequence of derived Morita theory, and it is the reason the enrichment is a property of the triangulated data rather than an additional choice.

**Remark.** Not every triangulated category admits a DG enhancement, and the obstruction is an element of a Hochschild-type cohomology group of the category; the examples of non-enhanceable triangulated categories are constructed by Muro, Schwede and Strickland from the stable homotopy category. The construction of the enhancement from a triangulated category that admits one, and the obstruction theory of the failure, are algebraic statements of the kind assembled here; the stable-homotopy examples and the topological constructions belong to Part II.

## Pretriangulated Structures and the DG Quotient

**Definition.** A DG category $\mathcal{A}$ is **pretriangulated** if the image of the Yoneda embedding $\mathcal{A}\to\mathrm{DG}(\mathcal{A})$ is closed under shifts and mapping cones up to homotopy equivalence; equivalently, if for every object $x$ and every integer $n$ there is an object $x[n]$ representing the shift, and for every morphism $f : x\to y$ there is an object $\operatorname{Cone}(f)$ with the universal property of a cone. Then $H^0(\mathcal{A})$ is a triangulated category.

**Proposition.** A DG category is pretriangulated if and only if $H^0(\mathcal{A})$ can be equipped with a triangulation for which the shift functor is induced by the shift of the Hom complexes; every DG category has a pretriangulated hull, and the construction is functorial and universal.

*Proof.* If the cones exist, the octahedral and rotation axioms for the triangles canonically induced by cones follow from the corresponding identities for mapping cones of complexes, which hold in any DG category by the same computations as in the category of complexes. Conversely a triangulation determines the cones up to isomorphism, and the morphisms between cones are the morphisms induced on $H^0$. The pretriangulated hull is constructed by adjoining the shifts and the cones formally, that is, by taking the smallest pretriangulated DG subcategory of the DG module category containing the image of the Yoneda embedding. $\square$

**Definition.** Let $\mathcal{A}$ be a pretriangulated DG category and let $\mathcal{B}$ be a full DG subcategory that is pretriangulated. The **DG quotient** $\mathcal{A}/\mathcal{B}$ is the DG category with the same objects as $\mathcal{A}$ and Hom complexes obtained from those of $\mathcal{A}$ by adjoining formal inverses to the morphisms whose cone lies in $\mathcal{B}$; its $H^0$ is the Verdier quotient of triangulated categories, $H^0(\mathcal{A}/\mathcal{B}) = H^0(\mathcal{A})/H^0(\mathcal{B})$.

**Theorem (Keller, standard).** For a pretriangulated DG category $\mathcal{A}$ and a pretriangulated full DG subcategory $\mathcal{B}$, the DG quotient $\mathcal{A}/\mathcal{B}$ exists, is pretriangulated, and satisfies $H^0(\mathcal{A}/\mathcal{B}) = H^0(\mathcal{A})/H^0(\mathcal{B})$. The DG quotient is the correct homotopy-theoretic quotient: it is characterised by the property that a DG functor out of $\mathcal{A}$ that is null-homotopic on $\mathcal{B}$ factors through it.

The DG quotient is the construction that makes the theory homotopy-theoretic rather than merely homological: the Verdier quotient of triangulated categories is not in general the derived category of an algebra, whereas the DG quotient is always the $H^0$ of a DG category, and the theorem asserts that the one is recovered from the other. The homotopy-theoretic refinement of the quotient, and the model structure on DG categories in which it is computed, belong to Part II.

## $A_\infty$-Categories and the Weakening of the Composition

**Definition.** An **$A_\infty$-category** over $k$ consists of a class of objects, graded Hom complexes $\operatorname{Hom}(x,y)$ and morphisms of graded $k$-modules

$$
m_n : \operatorname{Hom}(x_{n-1},x_n)\otimes_k\cdots\otimes_k\operatorname{Hom}(x_0,x_1)\to\operatorname{Hom}(x_0,x_n), \qquad n\geq1,
$$

of degree $2-n$, satisfying the **Stasheff identities**

$$
\sum_{n = r+s+t}(-1)^{rs+t}\,m_{r+1+t}\bigl(\mathrm{id}^{\otimes r}\otimes m_s\otimes\mathrm{id}^{\otimes t}\bigr) = 0 .
$$

The case $n = 1$ is a differential, $n = 2$ is a composition, $n = 3$ is a homotopy measuring the failure of associativity, and the higher operations measure the higher homotopies. A DG category is exactly an $A_\infty$-category with $m_n = 0$ for $n\geq3$, so the $A_\infty$-notion is the homotopy-coherent weakening of the notion of this article, and it enjoys the corresponding **homotopy transfer theorem**: the homology of an $A_\infty$-category carries an $A_\infty$-structure inherited from a choice of homotopy splitting. The notion, its morphisms and its relation to the quoted algebras are developed in that article, below this one in the menu; the DG categories of this article are the strict case of the theory.

## Summary

A **differential graded category** $\mathcal{A}$ over $k$ has Hom complexes $\operatorname{Hom}_{\mathcal{A}}(x,y)$ with composition that is a chain map and satisfies the Koszul sign rule and the unitality identities; the **homotopy category** $H^0(\mathcal{A})$ has the same objects and morphisms the degree-$0$ homotopy classes of morphisms, and the endomorphism complex $\operatorname{Hom}_{\mathcal{A}}(x,x)$ is a DGA, so that a DG category is an algebra with several objects. The standard examples are the DG category with one object and endomorphism DGA a given DGA, the DG category $\operatorname{DG}(A)$ of DG modules over a DGA $A$ with $H^0 = K(A)$, the DG category of complexes of $k$-modules, and the DG category built from a finite set of modules over an algebra together with chosen projective resolutions.

A **DG module** over $\mathcal{A}$ is a DG functor $\mathcal{A}\to\mathbf{Ch}(k)$; the representables $\mathbf{h}_x = \operatorname{Hom}_{\mathcal{A}}(x,-)$ satisfy the DG Yoneda lemma, the semi-free and h-projective modules are the resolutions, and the **compact** modules $\mathrm{perf}(\mathcal{A})$ are the DG modules homotopy equivalent to direct summands of finite semi-free ones. The **derived category** $D(\mathcal{A})$ is the localisation of $H^0(\mathcal{A}\text{-Mod})$ at the quasi-isomorphisms; it is triangulated, its compact objects are $H^0(\mathrm{perf}(\mathcal{A}))$, a quasi-equivalence of DG categories induces an equivalence of derived categories, and **derived Morita theory** states the converse: $D(\mathcal{A})\simeq D(\mathcal{B})$ if and only if $\mathrm{perf}(\mathcal{A})$ and $\mathrm{perf}(\mathcal{B})$ are quasi-equivalent. For one-object DG categories concentrated in degree $0$ this reduces to the Morita equivalence of algebras.

A DG category is **pretriangulated** when it is closed under shifts and cones, equivalently when $H^0(\mathcal{A})$ carries a triangulation; the pretriangulated hull is the universal such enlargement, and the **DG quotient** $\mathcal{A}/\mathcal{B}$ by a pretriangulated subcategory exists, is pretriangulated, and has $H^0(\mathcal{A}/\mathcal{B}) = H^0(\mathcal{A})/H^0(\mathcal{B})$, by Keller's theorem. The homotopy-theoretic refinements — the model structure on DG categories, the topological constructions, and the geometric DG categories of sheaves on a space — belong to Part II. The weakening of the composition to a sequence of higher operations $m_n$ of degree $2-n$ satisfying the Stasheff identities gives the $A_\infty$-categories, of which the DG categories of this article are the strict case, and which are not covered here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k$ | ground commutative ring, later a field |
| $\mathcal{A}$, $\mathcal{B}$ | small DG categories |
| $\operatorname{Hom}_{\mathcal{A}}(x,y)$ | Hom complex, a complex of $k$-modules |
| $1_x$ | identity morphism of $x$, a degree-$0$ cycle |
| $H^0(\mathcal{A})$ | homotopy category, degree-$0$ cohomology of the Hom complexes |
| $\mathcal{A}\text{-Mod}$, $\operatorname{DG}(A)$ | DG modules over a DG category, over a DGA |
| $\mathbf{h}_x$, $\operatorname{Hom}_{\mathcal{A}}(x,-)$ | representable DG module |
| $D(\mathcal{A})$ | derived category, localisation at quasi-isomorphisms |
| $\mathrm{perf}(\mathcal{A})$ | DG category of compact (perfect) modules |
| $\simeq_{\mathrm{qe}}$ | quasi-equivalence of DG categories |
| $x[n]$, $\operatorname{Cone}(f)$ | shift and cone in a pretriangulated DG category |
| $\mathcal{A}/\mathcal{B}$ | DG quotient |
| $m_n$ | higher compositions of an $A_\infty$-category, degree $2-n$ |





## Further Reading

- Bernhard Keller, "Deriving DG categories", *Annales scientifiques de l'École Normale Supérieure* **27** (1994), 63–102, for the derived category of a DG category and the quasi-equivalence formalism.
- Bernhard Keller, "On differential graded categories", *Proceedings of the International Congress of Mathematicians* (Madrid, 2006), 151–190, for a survey of the theory, the DG quotient and derived Morita equivalence.
- Alexey Bondal and Mikhail Kapranov, "Enhanced triangulated categories", *Mathematics of the USSR–Sbornik* **70** (1991), 93–107, for pretriangulated DG categories and the pretriangulated hull.
- Vladimir Drinfeld, "DG quotients of DG categories", *Journal of Algebra* **272** (2004), 643–691, for the DG quotient and its homotopy-theoretic properties.
- Bertrand Toën, "The homotopy theory of dg-categories and derived Morita theory", *Inventiones Mathematicae* **167** (2007), 615–667, for the model structure and the Morita theory of DG categories.
