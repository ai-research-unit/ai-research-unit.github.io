
# __Abelian and Grothendieck Categories__

## Introduction

The category $R\text{-}\mathbf{Mod}$ has a structure that the previous article of this category exhibited in detail: a zero object, finite biproducts, kernels and cokernels, and the identity of the coimage with the image. Left and right exactness are defined by these data, and the whole of homological algebra — resolutions, derived functors, long exact sequences — uses nothing else. It is therefore possible to carry that theory to any category with the same structure, and to ask which of the familiar constructions are categorical and which depend on the ring. The answer is the theory of **abelian categories**, invented for exactly this purpose by Buchsbaum, Grothendieck and Mac Lane, and the special class of **Grothendieck categories** in which the homological constructions behave best.

This article develops additive and abelian categories, exact sequences in them, the Freyd–Mitchell embedding theorem that identifies every small abelian category with a full subcategory of a module category, and the Grothendieck categories — the abelian categories with a generator, all colimits and exact filtered colimits — together with the Gabriel–Popescu theorem that describes them as quotients of module categories. It is the abstract framework of this category, and the reason statements about modules are frequently proved once in the abstract setting.

Throughout, $\mathcal{A}$, $\mathcal{B}$ are additive or abelian categories, and the motivating example is $\mathcal{A}=R\text{-}\mathbf{Mod}$ for a ring $R$. The article assumes the categorical vocabulary of the companion article *Module Categories* — categories, functors, natural transformations, representability, limits and colimits, biproducts — and it uses the module-theoretic results of the articles *Exact Sequences* and *Projective and Injective Modules* only as examples. No topology and no form enters; the words *complete*, *filtered* and *limit* are used in their algebraic and categorical senses, and the article contains no distance, norm or topological enrichment. Where a construction is taken from the theory of sheaves or of schemes it is named, not used, and the reader is directed forward.

## Additive Categories

### The Axioms

**Definition.** A category $\mathcal{A}$ is **preadditive** if every hom set $\mathcal{A}(A,B)$ carries the structure of an abelian group and composition is bilinear:

$$
(g+g')\circ f=g\circ f+g'\circ f, \qquad g\circ(f+f')=g\circ f+g\circ f' .
$$

A preadditive category is **additive** if it has a zero object and a biproduct $A\oplus B$ for every pair of objects, where a **biproduct** is an object that is simultaneously a product with projections $\pi_A,\pi_B$ and a coproduct with inclusions $\iota_A,\iota_B$, subject to the identities

$$
\pi_A\iota_A=\operatorname{id}_A,\quad \pi_B\iota_B=\operatorname{id}_B,\quad \pi_B\iota_A=0,\quad \pi_A\iota_B=0,\quad \iota_A\pi_A+\iota_B\pi_B=\operatorname{id}_{A\oplus B}.
$$

**Proposition.** In an additive category the product and the coproduct of two objects, when both exist, are canonically isomorphic, and the structure maps satisfy the biproduct identities. Finite products and finite coproducts therefore coincide.

*Proof.* Write $A\coprod B$ for the coproduct with inclusions and $A\prod B$ for the product with projections. The universal properties give a map $A\coprod B\to A\prod B$ whose composites with the inclusions are the inclusion followed by each projection; explicitly, the four composites are the two identities and the two zero maps. A map $A\prod B\to A\coprod B$ is constructed from the identities and the zero maps; the two composites are identities by the universal properties and uniqueness. The resulting identities are the biproduct axioms. $\square$

**Example.** $R\text{-}\mathbf{Mod}$ is additive: the hom sets are abelian groups, composition is $R$-bilinear, $0$ is a zero object, and the direct sum is a biproduct. The abelian groups themselves form the additive category $\mathbf{Ab}$, and the category of finitely generated projective $R$-modules is additive but not abelian.

### Additive Functors and Matrices

**Definition.** A functor $F:\mathcal{A}\to\mathcal{B}$ between additive categories is **additive** if the maps $\mathcal{A}(A,B)\to\mathcal{B}(FA,FB)$ are group homomorphisms. An additive functor necessarily preserves zero objects, biproducts and finite direct sums.

**Proposition.** An additive functor $F$ satisfies $F(A\oplus B)\cong FA\oplus FB$ compatibly with the inclusions and projections, and $F(0)\cong0$.

*Proof.* Additivity gives $F(0)=F(0+0)=F(0)+F(0)$, so $F(0)=0$; the biproduct identities are preserved because they are equations between composites of morphisms, and additivity preserves sums of morphisms. $\square$

**Proposition.** The functors $\operatorname{Hom}_{\mathcal{A}}(A,-)$ and $\operatorname{Hom}_{\mathcal{A}}(-,A)$ with values in $\mathbf{Ab}$ are additive, and $\operatorname{Hom}_{\mathcal{A}}(A,B)$ is the group of morphisms that the bifunctor assigns to the pair.

**Example.** For a ring $R$ and a fixed module $M$, the functors $\operatorname{Hom}_R(M,-)$, $\operatorname{Hom}_R(-,M)$ and $-\otimes_RM$ are additive; the last is a functor on $R\text{-}\mathbf{Mod}$ only because $R$ is commutative, since otherwise the tensor product of two left modules is not defined.

## Abelian Categories

### Kernels, Cokernels and the Abelian Axiom

**Definition.** In an additive category, a **kernel** of $f:A\to B$ is a morphism $k:K\to A$ with $fk=0$ that is universal among such morphisms: every $g$ with $fg=0$ factors uniquely through $k$. A **cokernel** is the dual notion, a morphism $c:B\to C$ with $cf=0$ universal among such morphisms. The **image** of $f$ is the kernel of its cokernel, and the **coimage** is the cokernel of its kernel; both carry canonical maps into and out of $B$.

**Definition.** An additive category $\mathcal{A}$ is **abelian** if every morphism has a kernel and a cokernel, and for every $f:A\to B$ the canonical map

$$
\operatorname{coim}f \longrightarrow \operatorname{im}f
$$

is an isomorphism, where $\operatorname{coim}f=\operatorname{coker}(\ker f\to A)$ and $\operatorname{im}f=\ker(B\to\operatorname{coker}f)$.

The condition is exactly the categorical form of the first isomorphism theorem, and it is what makes exactness statable: a sequence is exact at a term when the image of the incoming morphism equals the kernel of the outgoing one as subobjects of that term.

**Example.** $R\text{-}\mathbf{Mod}$ is abelian. So is the category of abelian sheaves on a site, and so is the category of left modules over a sheaf of rings; the latter two are named here and developed, for sheaves on a space, in Part II.

**Example.** The category of finitely generated free abelian groups is additive and is not abelian, although it has kernels and cokernels as a category. For $f=\cdot 2:\mathbb{Z}\to\mathbb{Z}$ the kernel in the subcategory is $0$ (a map from a finitely generated free group killed by $f$ is zero), so the coimage is $\mathbb{Z}$; the cokernel in the subcategory is likewise $0$ (any map from $\mathbb{Z}$ to a finitely generated free group killing $2$ is zero), so the image is again $\mathbb{Z}$; but the canonical map $\operatorname{coim}f\to\operatorname{im}f$ is multiplication by $2$, which is not an isomorphism. The kernels and the cokernels computed inside the subcategory therefore disagree with those computed in $\mathbf{Ab}$, and the abelian axiom fails.

**Example.** The category of abelian groups equipped with a finite filtration, with the filtration-preserving homomorphisms, is additive and fails the abelian axiom: the image of a morphism carries the induced filtration while the coimage carries the quotient filtration, and the two can differ, so the canonical map from the coimage to the image need not be an isomorphism. Such categories lie outside the reach of homological algebra as developed here.

### Elementary Consequences

**Proposition.** In an abelian category the following hold for every morphism $f$.

(i) $f$ is a monomorphism if and only if $\ker f=0$, and an epimorphism if and only if $\operatorname{coker}f=0$.

(ii) $f$ factors as a monomorphism after an epimorphism, $A\to\operatorname{coim}f\xrightarrow{\cong}\operatorname{im}f\to B$; this is the **epi–mono factorisation**.

(iii) $f$ is an isomorphism if and only if it is both a monomorphism and an epimorphism.

*Proof.* (i) If $f$ is a monomorphism and $k:\ker f\to A$, then $fk=0=f0$, so $k=0$, and the universal property of the zero map gives $\ker f=0$. Conversely if $\ker f=0$ and $fg=fh$, then $f(g-h)=0$ and the map $g-h$ factors through $\ker f=0$, so $g=h$. The cokernel statement is dual. (ii) The canonical map $A\to\operatorname{coim}f$ is an epimorphism by definition of the cokernel, and $\operatorname{im}f\to B$ is a monomorphism by definition of the kernel; the abelian axiom inserts the isomorphism between them. (iii) A monomorphism that is an epimorphism has $\ker f=0=\operatorname{coker}f$, so the factorisation is an isomorphism. $\square$

**Proposition.** An additive functor between abelian categories preserves kernels if and only if it preserves the multiplicative relation defining a kernel; a covariant additive functor is left exact precisely when it sends exact sequences $0\to A\to B\to C$ to exact sequences, right exact precisely when it sends $A\to B\to C\to0$ to exact sequences, and exact when it does both.

*Proof.* This is the definition of exactness read through the functor: preservation of the kernel of $B\to C$ is the exactness at $B$, and preservation of the cokernel is exactness at $C$. Additivity supplies the compatibility with the zero objects. $\square$

### Exact Sequences and the Diagram Lemmas

**Definition.** A sequence $\cdots\to A_{i+1}\to A_i\to A_{i-1}\to\cdots$ in an abelian category is **exact** if at each $A_i$ the image of the incoming morphism equals the kernel of the outgoing one. A **short exact sequence** is $0\to A\to B\to C\to0$, exact at all three terms.

**Theorem (snake).** In a commutative diagram with exact rows

$$
A\to B\to C\to 0, \qquad 0\to A'\to B'\to C',
$$

and maps $a:A\to A'$, $b:B\to B'$, $c:C\to C'$ commuting with the rows, there is an exact sequence

$$
\ker a\to\ker b\to\ker c\xrightarrow{\ \partial\ }\operatorname{coker}a\to\operatorname{coker}b\to\operatorname{coker}c,
$$

and the connecting morphism $\partial$ is natural in the diagram.

*Proof.* The construction of $\partial$ in the category of modules used elements; in an abelian category it is performed with the epi–mono factorisation instead. The map $\ker c\to C$ is a monomorphism, and composing with the epimorphism $B\to C$ and forming a pullback produces the object $B\times_C\ker c$; the composite into $B'$ lands in the image of $A'$, and the comparison with the kernel gives $\partial$. The verification of exactness is by the universal properties, with no elements used; the details are the standard argument of Mitchell's theory of the embedding into module categories, and reduce to the module case after applying the Freyd–Mitchell theorem below. $\square$

**Theorem (five).** Consider a commutative diagram with exact rows $A_1\to A_2\to A_3\to A_4\to A_5$ and $B_1\to\cdots\to B_5$ and vertical maps $\alpha_i:A_i\to B_i$. If $\alpha_1,\alpha_2,\alpha_4,\alpha_5$ are isomorphisms then so is $\alpha_3$; if $\alpha_2,\alpha_4$ are monomorphisms and $\alpha_1$ an epimorphism then $\alpha_3$ is a monomorphism, and dually for epimorphisms.

*Proof.* The argument is the diagram chase of the article *Exact Sequences*; it uses only exactness, composition and the abelian axiom, so it applies verbatim in every abelian category once exactness is stated categorically. Alternatively, embed the finite diagram in $R\text{-}\mathbf{Mod}$ by the Freyd–Mitchell theorem and chase elements there. $\square$

**Corollary.** A map of short exact sequences $0\to A\to B\to C\to0$ and $0\to A'\to B'\to C'\to0$ whose outer vertical maps are isomorphisms has an isomorphism for its middle vertical map.

### Projective and Injective Objects

**Definition.** An object $P$ of an abelian category is **projective** if $\operatorname{Hom}(P,-)$ is exact, equivalently if every epimorphism $X\to Y$ admits a lift along every morphism $P\to Y$. An object $I$ is **injective** if $\operatorname{Hom}(-,I)$ is exact, equivalently if every monomorphism $X\to Y$ admits an extension of every morphism $X\to I$.

**Definition.** An abelian category has **enough projectives** if every object is the image of an epimorphism from a projective, and **enough injectives** if every object is a subobject of an injective.

**Theorem.** $R\text{-}\mathbf{Mod}$ has enough projectives, the free modules, and enough injectives, via the construction of the article *Projective and Injective Modules*. The same statement holds in every Grothendieck category, below, for injectives.

*Proof.* For projectives, every module is a quotient of a free module. For injectives, embed a module into a product of copies of an injective cogenerator; the general Grothendieck case is the theorem of Grothendieck, proved below. $\square$

Enough projectives and enough injectives are precisely the hypotheses under which the derived functors are defined. An abelian category with neither is outside the theory's reach: the full subcategory of finitely generated modules over a ring is abelian, but the injective hull of a finitely generated module need not be finitely generated, so it generally has not enough injectives; and the category of sheaves on a compact space has enough injectives and rarely has enough projectives.

## The Freyd–Mitchell Embedding Theorem

### Statement

The elementary results of the preceding section were proved by the same element chases used for modules. The embedding theorem legitimises this once and for all.

**Theorem (Freyd–Mitchell).** Every small abelian category $\mathcal{A}$ admits a full, faithful and exact functor into the category $R\text{-}\mathbf{Mod}$ of left modules over some ring $R$. Consequently every finite diagram in $\mathcal{A}$ can be realised in a module category, and every statement about finitely many objects and morphisms that is expressible by exactness, composition and the abelian axioms and that holds in all module categories holds in every abelian category.

*Proof (in outline).* The category of additive functors from $\mathcal{A}^{\mathrm{op}}$ to $\mathbf{Ab}$ is abelian, and evaluation at an object is exact; the **Yoneda embedding** $A\mapsto\mathcal{A}(-,A)$ is full, faithful and left exact. It remains to correct the failure of exactness, and to reduce to a module category over a ring rather than a functor category. Mitchell's argument forms the ring $R=\operatorname{End}(\mathcal{P})^{\mathrm{op}}$ of endomorphisms of a suitable projective generator of the functor category and shows that the functor category has a full exact subcategory equivalent to $R\text{-}\mathbf{Mod}$ containing the image of $\mathcal{A}$. $\square$

### Consequences

**Corollary.** The snake lemma, the five lemma, the $3\times3$ lemma and every other diagram lemma stated for modules hold in every abelian category.

**Corollary.** A sequence in a small abelian category is exact if and only if it is exact after applying the embedding; an object is projective or injective if and only if its image is, since the embedding is full, faithful and exact.

**Remark.** The theorem requires $\mathcal{A}$ to be small, so that the functor category can be a set-theoretic category and the indexing sums over all objects make sense. For a large abelian category one applies the theorem to the small subcategory generated by any finite diagram, which is the form in which it is used. The embedding is not canonical; it is a tool for transferring computations, not data attached to $\mathcal{A}$.

## Grothendieck Categories

### The AB Conditions

Grothendieck isolated a list of exactness conditions on the coproducts of an abelian category.

**Definition.** An abelian category satisfies **AB3** if it has all small coproducts, **AB4** if AB3 holds and every small coproduct is exact as a functor of its factors, and **AB5** if AB3 holds and filtered colimits are exact. The dual conditions are **AB3***, **AB4***, **AB5***. A category satisfies **AB6** if filtered colimits commute with arbitrary products.

**Definition.** An object $G$ of an abelian category is a **generator** if the representable functor $\operatorname{Hom}(G,-)$ is faithful, equivalently if for every nonzero $f:A\to B$ there is $g:G\to A$ with $fg\neq0$.

**Proposition.** In $R\text{-}\mathbf{Mod}$ the regular module $R$ is a generator and the conditions AB3, AB4, AB5 hold: direct sums and filtered colimits are exact.

*Proof.* The functor $\operatorname{Hom}_R(R,-)$ is the identity, hence faithful, so $R$ generates; the exactness of direct sums and of filtered colimits is the statement recorded in *Module Categories*. $\square$

### Definition and First Properties

**Definition.** A **Grothendieck category** is an abelian category satisfying AB5 that has a generator, equivalently — the equivalence is a theorem of Grothendieck — an abelian category satisfying AB5 with a set of generators.

**Example.** The category $R\text{-}\mathbf{Mod}$ is a Grothendieck category. The category of left modules over a sheaf of rings on a site, and the category of presheaves of abelian groups on a small category, are Grothendieck categories; the first is developed, the second is the functor category $\mathbf{Ab}^{\mathcal{C}^{\mathrm{op}}}$ and is the reason the theory applies to sheaves at all.

**Theorem.** A Grothendieck category has all small colimits, is complete, has enough injectives, and has an injective cogenerator.

*Proof.* AB3 gives all small coproducts, and the existence of all filtered colimits follows from AB5 together with the construction of a general colimit as a quotient of a coproduct, so all small colimits exist; all small limits exist by the dual argument, using that an abelian category has finite limits and products. For enough injectives one uses the generator $G$: since $G$ generates, the evaluation map embeds $A$ into the product $\prod_{x\in\operatorname{Hom}(A,G)}G$, and the same construction applied to the cokernel of the embedding, repeated along the ordinals, produces an increasing chain of embeddings whose transfinite colimit is injective; AB5, the exactness of filtered colimits, is exactly what is needed for the colimit to behave and for the iteration to terminate in an injective envelope. $\square$

**Remark.** The proof of enough injectives is the place where AB5 is used and where it cannot be weakened: an abelian category satisfying only AB3 need not have enough injectives. This is the technical reason Grothendieck categories are the natural setting for the cohomological theory of sheaves, where injective resolutions are the only ones generally available.

### Injectives and Resolutions

**Definition.** An **injective resolution** of an object $A$ is an exact sequence $0\to A\to I^0\to I^1\to\cdots$ with every $I^n$ injective. Dually a **projective resolution** is an exact sequence $\cdots\to P_1\to P_0\to A\to0$ with every $P_n$ projective.

**Corollary.** In a Grothendieck category every object has an injective resolution; in an abelian category with enough projectives every object has a projective resolution.

*Proof.* Embed $A$ in an injective $I^0$, embed the cokernel in an injective $I^1$, and iterate; the construction is the standard one. The projective case is dual. $\square$

Resolutions are the input to the derived-functor theory; their existence in a Grothendieck category is what makes sheaf cohomology, which is developed in Part II, a derived-functor theory in the sense of this category.

## The Gabriel–Popescu Theorem

### Localising Subcategories and Quotients

**Definition.** A full subcategory $\mathcal{S}$ of an abelian category $\mathcal{A}$ is a **Serre subcategory** if for every short exact sequence $0\to A\to B\to C\to0$ in $\mathcal{A}$ the middle object $B$ lies in $\mathcal{S}$ if and only if $A$ and $C$ do. A Serre subcategory is **localising** if the quotient functor $\mathcal{A}\to\mathcal{A}/\mathcal{S}$ has a right adjoint.

**Proposition.** The quotient $\mathcal{A}/\mathcal{S}$ of an abelian category by a Serre subcategory is abelian, and the quotient functor is exact. Its objects are the objects of $\mathcal{A}$, and a morphism becomes an isomorphism exactly when its kernel and cokernel lie in $\mathcal{S}$.

*Proof.* The calculus of fractions in the quotient admits a description in which a morphism $A\to B$ is represented by a diagram $A'\leftarrow A$ with kernel and cokernel in $\mathcal{S}$ followed by $A'\to B$ with the same property; the abelian axioms are verified on these representatives. Exactness of the quotient functor is immediate from the characterisation of the isomorphisms. $\square$

### The Theorem

**Theorem (Gabriel–Popescu).** Let $\mathcal{A}$ be a Grothendieck category with generator $G$, and put $R=\operatorname{End}_{\mathcal{A}}(G)^{\mathrm{op}}$, so that $\operatorname{Hom}_{\mathcal{A}}(G,A)$ is a left $R$-module by precomposition. Then:

(i) the functor $H=\operatorname{Hom}_{\mathcal{A}}(G,-):\mathcal{A}\to R\text{-}\mathbf{Mod}$ is full and faithful, hence left exact;

(ii) $H$ has a left adjoint $T=-\otimes_RG:R\text{-}\mathbf{Mod}\to\mathcal{A}$ sending $R$ to $G$, the functor $T$ is exact, and its kernel $\mathcal{S}=\{M:T(M)=0\}$ is a localising subcategory of $R\text{-}\mathbf{Mod}$;

(iii) the induced functor $R\text{-}\mathbf{Mod}/\mathcal{S}\to\mathcal{A}$ is an equivalence. In this form every Grothendieck category is a quotient of a module category.

*Proof (in outline).* The functor $H$ is left exact because it is a hom functor, and faithful by the definition of a generator; the fullness is the substance of the theorem and is proved by showing that a natural transformation $\operatorname{Hom}_{\mathcal{A}}(G,A)\to\operatorname{Hom}_{\mathcal{A}}(G,B)$ of $R$-modules is induced by a morphism $A\to B$, using that every object of a Grothendieck category is a quotient of a coproduct of copies of the generator. For the adjunction, the left adjoint $T$ sends the free module $R$ to $G$ and is right exact, so it is determined by this value; the unit and counit are isomorphisms on $G$, and since $G$ generates they are isomorphisms everywhere on the image, which is what makes the induced functor on the quotient an equivalence. The kernel $\mathcal{S}$ is closed under subobjects, quotients and extensions and, being the kernel of a functor with a right adjoint $H$, the quotient functor has the right adjoint that makes it localising. Exactness of $T$ follows from the equivalence in (iii), since an equivalence is exact and the quotient functor is exact. $\square$

**Corollary.** Every Grothendieck category is equivalent to a quotient of a module category by a localising subcategory. When that subcategory is a **hereditary torsion class** — closed under subobjects as well as under quotients and extensions — the quotient is the category of modules over $R$ equipped with the corresponding **Gabriel topology**, that is, the full subcategory of $R\text{-}\mathbf{Mod}$ of the modules that are torsion-free and injective for the topology. The abelian categories that arise in algebraic geometry and in the theory of sites are all of the torsion-theoretic form.

**Example.** The category of abelian groups is $R\text{-}\mathbf{Mod}$ for $R=\mathbb{Z}$, with the trivial Gabriel topology; it is the basic Grothendieck category. A quotient of $\mathbb{Z}\text{-}\mathbf{Mod}$ by a localising subcategory is the category of modules over a ring with a Gabriel topology, and the simplest nontrivial quotient is that by the Serre subcategory of torsion groups, whose quotient is the category of $\mathbb{Q}$-vector spaces when the localising subcategory is chosen to invert multiplication by each prime.

## Relations to the Module Categories of This Part

### The Module Theory as the Source of the Notions

Every axiom of an abelian category is an abstracted property of $R\text{-}\mathbf{Mod}$, and every theorem about modules stated in exactness terms — the snake lemma, the five lemma, the splitting lemma, the classification of extensions — is a categorical statement. The article *Exact Sequences* proves these for modules by element chases; the Freyd–Mitchell theorem says that no generality is lost, so the module proofs are proofs of the categorical statements. The articlethen develops chain complexes and resolutions abstractly, andattaches to a left exact functor its right derived functors in any abelian category with enough injectives.

### Where the Abstraction Is Needed

The abstraction is not idle generality. Three of the settings of this category are Grothendieck categories that are not module categories: the category of sheaves of abelian groups on a site, the category of sheaves of modules over a sheaf of rings, and the categories of comodules and descent data; and the derived categories are built from abelian categories of this generality. In each case the existence of enough injectives, the exactness of filtered colimits and the presence of a generator are hypotheses that must be checked, and the Gabriel–Popescu theorem is the criterion that decides whether the category is a module category in disguise.

### What Does Not Abstract

Not every notion of module theory has an abstract analogue. The tensor product of two objects is not defined in a general abelian category: it needs a monoidal structure, and the tensor–hom adjunction is an extra datum. Hence flatness, the derived functor $\operatorname{Tor}$, and the whole multiplicative theory remain properties of module categories or of monoidal abelian categories, not of abelian categories as such. Similarly the rank and the determinant require a notion of free object or of dualisable object. The abelian-category theory of this article abstracts the additive part of module theory; the multiplicative part is abstracted by the monoidal and closed-category machinery, and the tensor and the balanced product keep their module-theoretic and algebra-theoretic settings.

## Summary

An additive category is a preadditive category with a zero object and biproducts, and in such a category finite products and finite coproducts coincide. An abelian category is an additive category in which every morphism has a kernel and a cokernel and the canonical map $\operatorname{coim}f\to\operatorname{im}f$ is an isomorphism; the module categories $R\text{-}\mathbf{Mod}$ are the archetypes, and in every abelian category the epi–mono factorisation, the snake lemma and the five lemma hold.

The Freyd–Mitchell theorem embeds every small abelian category fully, faithfully and exactly into a module category, so every diagram chase valid for modules is valid in general. A Grothendieck category is an abelian category satisfying AB5 with a generator; it is complete and cocomplete, has filtered colimits exact, and has enough injectives as well as an injective cogenerator, so every object has an injective resolution. The Gabriel–Popescu theorem embeds a Grothendieck category with generator $G$ fully and faithfully, by $\operatorname{Hom}_{\mathcal{A}}(G,-)$, into the category of modules over $R=\operatorname{End}_{\mathcal{A}}(G)^{\mathrm{op}}$, and exhibits it as the quotient of that module category by a localising subcategory; when the subcategory is a hereditary torsion class the quotient is a category of modules with a Gabriel topology.

The abstraction abstracts the additive part of module theory only. The tensor product, flatness, $\operatorname{Tor}$ and the determinant need a monoidal or a duality structure that an abelian category does not carry, and they remain where this part put them, in the module and algebra categories.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{A}$, $\mathcal{B}$ | additive or abelian categories |
| $\mathcal{A}(A,B)$ | abelian group of morphisms |
| $A\oplus B$, $\pi_A$, $\iota_A$ | biproduct with projections and inclusions |
| $\ker f$, $\operatorname{coker}f$ | kernel and cokernel of a morphism |
| $\operatorname{im}f$, $\operatorname{coim}f$ | image and coimage |
| $0\to A\to B\to C\to0$ | short exact sequence |
| $\partial$ | connecting morphism of the snake lemma |
| AB3, AB4, AB5 | existence and exactness of small coproducts, filtered colimits |
| $G$ | a generator; $\operatorname{Hom}(G,-)$ faithful |
| $R=\operatorname{End}_{\mathcal{A}}(G)^{\mathrm{op}}$ | endomorphism ring of a generator, acting on $\operatorname{Hom}_{\mathcal{A}}(G,-)$ on the left |
| $\mathcal{A}/\mathcal{S}$ | quotient by a Serre or localising subcategory |
| $T=-\otimes_RG$ | left adjoint of $\operatorname{Hom}_{\mathcal{A}}(G,-)$ in the Gabriel–Popescu theorem |
| $I^\bullet$, $P_\bullet$ | injective and projective resolutions |
| $R\text{-}\mathbf{Mod}$ | the category of left $R$-modules |









## Further Reading

- Michael Barr, *Exact Categories and Categories of Sheaves* (Springer Lecture Notes in Mathematics 236, 1971), for abelian categories and their exact completions.
- D. A. Buchsbaum, "Exact categories and duality", *Transactions of the American Mathematical Society* 80 (1955), 1–34, for the origin of the abelian-category axioms.
- Peter Freyd, *Abelian Categories: An Introduction to the Theory of Functors* (Harper and Row, 1964), for the embedding theorem and the functor-category constructions.
- Pierre Gabriel, "Des catégories abéliennes", *Bulletin de la Société Mathématique de France* 90 (1962), 323–448, for Grothendieck categories, localisation and the Gabriel–Popescu theorem.
- Pierre Gabriel and Nicolas Popescu, "Caractérisation des catégories abéliennes avec générateurs et limites inductives exactes", *Comptes Rendus de l'Académie des Sciences de Paris* 258 (1964), 4188–4190, for the theorem itself.
- Alexander Grothendieck, "Sur quelques points d'algèbre homologique", *Tohoku Mathematical Journal* 9 (1957), 119–221, for AB5, enough injectives and the foundations of homological algebra in abelian categories.
- Saunders Mac Lane, *Categories for the Working Mathematician*, 2nd ed. (Springer, 1998), for additive categories, abelian categories and the Yoneda embedding.
- Barry Mitchell, "The full imbedding theorem", *American Journal of Mathematics* 86 (1964), 619–637, for the Freyd–Mitchell embedding.
