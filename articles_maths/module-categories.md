
# __Module Categories__

## Introduction

The collection of all left modules over a ring, together with the linear maps between them, is not merely a class of objects; it has a composition law, identities, and enough structure — a zero object, direct sums, kernels and cokernels — that the whole of linear algebra can be phrased as the study of this one object. It is a **category**, and the linear maps between modules are its **morphisms**. Organising module theory in this way is not decoration: it isolates the constructions that are defined by a universal property from those that depend on a presentation, and it makes precise the sense in which two rings have the same module theory.

This article develops the category $R\text{-}\mathbf{Mod}$ of left modules over a ring $R$, the functors between such categories, and the natural transformations between functors. It records the structural properties of $R\text{-}\mathbf{Mod}$ — the zero object, biproducts, kernels and cokernels with $\operatorname{coim}\cong\operatorname{im}$ — that other articles of this category abstract into the notions of additive and abelian category, and it states the two adjunctions that organise the fundamental functors: the free–forgetful adjunction and the tensor–hom adjunction. It closes with the notion of equivalence of module categories and its relation to Morita equivalence, which is treated in the category *Linear Spaces over Linear Algebras*, and with the relation to the abelian categories of this category.

Throughout, $R$ is a ring; where a statement needs commutativity that hypothesis is named, and where $R$ is not assumed commutative the side of the modules matters and is stated. The article uses the vocabulary of *Modules*, *Direct Sums, Free Modules and Rank*, *Exact Sequences*, *Projective and Injective Modules*, *The Balanced Product* and *Flatness and Exactness*. It is deliberately free of topology: no distance, no norm, no completion and no topological enrichment occurs, and the categorical constructions are those of pure algebra. The abstract theory of categories is developed in the companion article *Universal Properties and Categories* of the *Foundations of Algebra* category, being written in the same batch; the small amount of category theory needed here is recalled, so that the article is readable on its own.

## Categories, Functors and Natural Transformations

### Categories

**Definition.** A **category** $\mathcal{C}$ consists of a class of **objects**, a set $\mathcal{C}(A,B)$ of **morphisms** for each ordered pair of objects, a **composition** map $\mathcal{C}(B,C)\times\mathcal{C}(A,B)\to\mathcal{C}(A,C)$, $(g,f)\mapsto g\circ f$, and an **identity** $\operatorname{id}_A \in \mathcal{C}(A,A)$ for each object $A$, such that composition is associative and the identities are two-sided units.

**Definition.** The **opposite category** $\mathcal{C}^{\mathrm{op}}$ has the same objects, morphism sets $\mathcal{C}^{\mathrm{op}}(A,B)=\mathcal{C}(B,A)$, and composition $f\circ^{\mathrm{op}}g=g\circ f$. A statement about $\mathcal{C}$ dualises by being read in $\mathcal{C}^{\mathrm{op}}$.

**Definition.** A morphism $f:A\to B$ is a **monomorphism** if $fg=fh$ implies $g=h$, an **epimorphism** if $gf=hf$ implies $g=h$, and an **isomorphism** if it has a two-sided inverse. In $R\text{-}\mathbf{Mod}$ the monomorphisms are exactly the injective maps and the epimorphisms exactly the surjective maps.

*Proof of the last claim.* Injectivity is clearly sufficient for being a monomorphism, and conversely if $f$ is not injective, the inclusion $0\to\ker f$ and the zero map $\ker f\to A$ are distinct maps with the same composite with $f$. The argument for epimorphisms is dual, using the projection $B\to B/\operatorname{im}f$ and the zero map. $\square$

### Functors

**Definition.** A **covariant functor** $F:\mathcal{C}\to\mathcal{D}$ assigns to each object $A$ an object $FA$, and to each morphism $f:A\to B$ a morphism $Ff:FA\to FB$, with $F(\operatorname{id}_A)=\operatorname{id}_{FA}$ and $F(g\circ f)=Fg\circ Ff$. A **contravariant functor** reverses the arrows, so that $Ff:FB\to FA$ and $F(g\circ f)=Ff\circ Fg$.

**Definition.** A functor $F:\mathcal{C}\to\mathcal{D}$ is **faithful** if the maps $\mathcal{C}(A,B)\to\mathcal{D}(FA,FB)$ are injective, **full** if they are surjective, and **essentially surjective** if every object of $\mathcal{D}$ is isomorphic to some $FA$. It is an **equivalence of categories** if it is full, faithful and essentially surjective; equivalently, if there is a functor $G:\mathcal{D}\to\mathcal{C}$ with $GF\cong\operatorname{id}_{\mathcal{C}}$ and $FG\cong\operatorname{id}_{\mathcal{D}}$.

**Example.** The **forgetful functor** $U:R\text{-}\mathbf{Mod}\to\mathbf{Ab}$ sends a module to its underlying abelian group and a linear map to itself. It is faithful and not full. Its left adjoint is **extension of scalars** $A\mapsto R\otimes_{\mathbb{Z}}A$, the free $R$-module on a basis of $A$ when $A$ is free; over a field $K$ it is $A\mapsto K\otimes_{\mathbb{Z}}A$, which for a free abelian group $A=\mathbb{Z}^{\oplus S}$ is the $K$-vector space with basis $S$. The **free-module functor** on sets is the functor $\mathbf{Set}\to R\text{-}\mathbf{Mod}$ of the free–forgetful adjunction below, which is the composite of the two when $A$ is a free abelian group.

**Example.** The functors $\operatorname{Hom}_R(M,-)$ and $-\otimes_RM$ of the articles on exact sequences and the balanced product are covariant functors $R\text{-}\mathbf{Mod}\to R\text{-}\mathbf{Mod}$, and $\operatorname{Hom}_R(-,N)$ is contravariant. The dual module functor $(-)^*=\operatorname{Hom}_R(-,R)$ is contravariant.

### Natural Transformations

**Definition.** Let $F,G:\mathcal{C}\to\mathcal{D}$ be functors. A **natural transformation** $\eta:F\to G$ assigns to each object $A$ a morphism $\eta_A:FA\to GA$ such that for every $f:A\to B$ the two composites agree:

$$
Gf\circ\eta_A=\eta_B\circ Ff : FA \longrightarrow GB .
$$

A natural transformation is a **natural isomorphism** if every $\eta_A$ is an isomorphism.

The requirement is not a convenience: it is the exact sense in which an isomorphism $M\otimes_RN\cong N\otimes_RM$ is *natural*, namely that it is a component of a natural isomorphism between the two functors, and therefore compatible with all induced maps.

**Example.** For a fixed $R$-module $N$ the associativity, commutativity and unit isomorphisms of the tensor product are natural transformations between the corresponding functors of the modules involved. The contraction $c:M^*\otimes_RM\to R$ is natural in $M$: it is a natural transformation to the constant functor $R$.

### The Category of Functors

For fixed $\mathcal{C}$ and $\mathcal{D}$ the functors $\mathcal{C}\to\mathcal{D}$ and the natural transformations between them themselves form a category, the **functor category** $\mathcal{D}^{\mathcal{C}}$, with composition defined componentwise. Taking $\mathcal{D}=\mathbf{Set}$ gives the category of presheaves on $\mathcal{C}$, the construction on which builds.

## The Category of Modules

### Objects and Morphisms

**Definition.** The category $R\text{-}\mathbf{Mod}$ has as objects the left $R$-modules and as morphisms the $R$-linear maps, with composition the ordinary composition of functions and identities the identity functions. The category of right $R$-modules is written $\mathbf{Mod}\text{-}R$, and for commutative $R$ the two coincide. The full subcategory of finitely generated modules is written $R\text{-}\mathbf{mod}$.

For commutative $R$ the set $\operatorname{Hom}_R(M,N)$ is again an $R$-module, by pointwise operations, and composition is $R$-bilinear. For noncommutative $R$ the hom set is only an abelian group; this is the reason the corpus works over commutative rings by default and names the noncommutative case when it occurs.

### The Hom Bifunctor

The assignment $(M,N)\mapsto\operatorname{Hom}_R(M,N)$ is a functor of two variables, a **bifunctor** $R\text{-}\mathbf{Mod}^{\mathrm{op}}\times R\text{-}\mathbf{Mod}\to\mathbf{Ab}$, contravariant in the first variable and covariant in the second: a map $f:M'\to M$ induces $f^*:\operatorname{Hom}_R(M,N)\to\operatorname{Hom}_R(M',N)$ by precomposition, and a map $g:N\to N'$ induces $g_*:\operatorname{Hom}_R(M,N)\to\operatorname{Hom}_R(M,N')$ by postcomposition. These two actions commute, $(g_*)\circ(f^*)=(f^*)\circ(g_*)$, which is the statement that the bifunctor is well defined.

### Zero Object, Products and Coproducts

**Definition.** An object $0$ of a category is a **zero object** if it is both initial and terminal: there is exactly one morphism from $0$ to any object and exactly one morphism from any object to $0$. A **biproduct** of $A$ and $B$ is an object $A\oplus B$ that is simultaneously a product, with projections $\pi_A,\pi_B$, and a coproduct, with inclusions $\iota_A,\iota_B$, satisfying $\pi_A\iota_A=\operatorname{id}_A$, $\pi_B\iota_B=\operatorname{id}_B$ and $\iota_A\pi_A+\iota_B\pi_B=\operatorname{id}_{A\oplus B}$.

**Proposition.** $R\text{-}\mathbf{Mod}$ has a zero object, the zero module, and every finite family of modules has a biproduct, the direct sum, which is at the same time the direct product.

*Proof.* The only linear map $0\to M$ and the only linear map $M\to0$ are the zero maps, so $0$ is initial and terminal. The direct sum $\bigoplus_{i}M_i$ with inclusions $\iota_i$ satisfies the universal property of the coproduct: a family of maps $f_i:M_i\to P$ extends uniquely to $\bigoplus_iM_i$. The direct product $\prod_iM_i$ with projections satisfies the universal property of the product. For a finite family the two objects coincide as constructed in *Direct Sums, Free Modules and Rank*, and the four identities of a biproduct hold. $\square$

The coincidence of finite products and finite coproducts is a strong structural feature. A category with a zero object and biproducts, in which every hom set is an abelian group and composition is bilinear, is called **additive**; $R\text{-}\mathbf{Mod}$ is the basic example, and the axioms and consequences of additivity are not covered here.

### Kernels and Cokernels

**Definition.** A **kernel** of $f:A\to B$ is a morphism $\ker f\to A$ that is universal among morphisms $X\to A$ with $f\circ(-)=0$. A **cokernel** is the dual notion: a morphism $B\to\operatorname{coker}f$ universal among morphisms $B\to Y$ with $(-)\circ f=0$. A category has kernels and cokernels if they exist for every morphism.

**Proposition.** $R\text{-}\mathbf{Mod}$ has all kernels and cokernels: $\ker f$ is the submodule $\{a:f(a)=0\}$ with its inclusion, and $\operatorname{coker}f$ is the quotient $B/\operatorname{im}f$ with the projection.

*Proof.* A linear map $g:X\to A$ with $fg=0$ has image in $\{a:f(a)=0\}$, and the induced map $X\to\ker f$ is the unique one whose composite with the inclusion is $g$. The cokernel statement is dual, using that a linear map $h:B\to Y$ with $hf=0$ vanishes on $\operatorname{im}f$ and therefore factors uniquely through $B/\operatorname{im}f$. $\square$

**Proposition.** The canonical map $\operatorname{coim}f=\operatorname{coker}(\ker f\to A)\to\ker(B\to\operatorname{coker}f)=\operatorname{im}f$ is an isomorphism; it is the first isomorphism theorem in categorical form.

*Proof.* The map is the one induced on the quotient $A/\ker f$ by $f$, and the first isomorphism theorem identifies $A/\ker f$ with $\operatorname{im}f$. $\square$

A category with a zero object, biproducts, and kernels and cokernels in which every such canonical map is an isomorphism is called **abelian**. The category $R\text{-}\mathbf{Mod}$ is abelian; the abstract definition, its consequences and its generalisations are not covered here.

## Exactness, Additivity and Exact Functors

### Additive Functors

**Definition.** A functor $F:\mathcal{A}\to\mathcal{B}$ between additive categories is **additive** if the maps $\mathcal{A}(A,B)\to\mathcal{B}(FA,FB)$ are group homomorphisms, equivalently if $F(A\oplus B)\cong FA\oplus FB$ compatibly with the structure maps. A covariant additive functor is **left exact** if it preserves kernels, **right exact** if it preserves cokernels, and **exact** if it preserves both; for the contravariant case the variance is reversed.

**Theorem.** For every $R$-module $M$ the functors $\operatorname{Hom}_R(M,-)$ and $\operatorname{Hom}_R(-,M)$ are additive and left exact, and $-\otimes_RM$ is additive and right exact; over a commutative ring all three are additive.

*Proof.* Additivity is immediate. Left exactness of $\operatorname{Hom}_R(M,-)$ in the second variable and of $\operatorname{Hom}_R(-,M)$ in the first, together with right exactness of $-\otimes_RM$, are the theorems of the articles on exact sequences and flatness and exactness. $\square$

### Exact Sequences as Categorical Data

An exact sequence of modules is a diagram in $R\text{-}\mathbf{Mod}$; exactness at a term says that the image of one morphism equals the kernel of the next, both being subobjects of the middle module. The categorical formulation of exactness is the basis of the definition of an abelian category and of the derived-functor theory of . In particular a short exact sequence $0\to A\to B\to C\to0$ is simultaneously a kernel–cokernel diagram, and the snake lemma and the five lemma are statements about the category $R\text{-}\mathbf{Mod}$ that generalise verbatim to every abelian category.

### Projectives, Injectives and the Hom Functors

The representability of the functors attached to a module is what makes the classes of projective and injective modules categorical.

**Proposition.** (i) $P$ is projective if and only if $\operatorname{Hom}_R(P,-)$ is exact. (ii) $I$ is injective if and only if $\operatorname{Hom}_R(-,I)$ is exact. (iii) $N$ is flat if and only if $-\otimes_RN$ is exact.

*Proof.* These are the theorems of the articles on projective and injective modules and on flatness and exactness, restated as exactness of the corresponding functors. $\square$

**Remark.** Projectivity and injectivity are therefore properties of the functors $\operatorname{Hom}_R(P,-)$ and $\operatorname{Hom}_R(-,I)$, and flatness a property of $-\otimes_RN$. The categories over which every module is projective are exactly the semisimple rings; over a field, for instance, every module is free and hence projective. The categorified statements — enough projectives, enough injectives, the derived functors — measure the failure of these functors to be exact.

## Adjunctions

### The Free–Forgetful Adjunction

**Definition.** An **adjunction** $F\dashv G$ between functors $F:\mathcal{C}\to\mathcal{D}$ and $G:\mathcal{D}\to\mathcal{C}$ consists of a natural bijection

$$
\mathcal{D}(FA,B)\cong\mathcal{C}(A,GB)
$$

for all objects $A$ of $\mathcal{C}$ and $B$ of $\mathcal{D}$. Then $F$ is the **left adjoint** of $G$ and $G$ the **right adjoint** of $F$.

**Theorem.** The free-module functor $F:\mathbf{Set}\to R\text{-}\mathbf{Mod}$ that sends a set $X$ to the free module $R^{(X)}$ on $X$ is left adjoint to the forgetful functor $U:R\text{-}\mathbf{Mod}\to\mathbf{Set}$: for every set $X$ and every module $M$ there is a natural bijection $\operatorname{Hom}_R(R^{(X)},M)\cong\operatorname{Hom}_{\mathbf{Set}}(X,UM)$.

*Proof.* A linear map out of the free module on $X$ is determined by its values on the basis $X$, and these may be prescribed arbitrarily; the correspondence between a linear map and the restriction of its underlying function to $X$ is the required bijection. Naturality is immediate. $\square$

**Corollary.** Left adjoints preserve colimits and right adjoints preserve limits. In particular the free functor preserves coproducts — the free module on a disjoint union is the direct sum — and $R\text{-}\mathbf{Mod}$ has all colimits, and all limits, because $\mathbf{Set}$ does and the functors transfer them.

### The Tensor–Hom Adjunction

**Theorem.** For $R$-modules $M,N,P$ there is a natural isomorphism

$$
\operatorname{Hom}_R(M\otimes_RN,P)\cong\operatorname{Hom}_R\bigl(M,\operatorname{Hom}_R(N,P)\bigr),
$$

so that $- \otimes_RN$ is left adjoint to $\operatorname{Hom}_R(N,-)$.

*Proof.* This is the tensor–hom adjunction of the articles on the balanced product and on flatness and exactness: the map on the left is sent to $m\mapsto(n\mapsto\varphi(m\otimes n))$, and the two constructions are inverse and natural. $\square$

**Corollary.** $-\otimes_RN$ preserves all colimits, hence is right exact and distributes over direct sums and cokernels; $\operatorname{Hom}_R(N,-)$ preserves all limits, hence is left exact.

The adjunction is the structural explanation of the asymmetry recorded in *Exact Sequences*: the left adjoint does not preserve limits, and the right adjoint does not preserve colimits, so neither functor is exact in general. Flatness of $N$ is exactly the additional condition for the left adjoint to preserve the particular limit that is a kernel.

## Generators, Representability and the Regular Module

### The Regular Module

**Definition.** The **regular left $R$-module** is $R$ acting on itself by left multiplication. The **regular right module** is $R$ acting by right multiplication. The ring $R$ is a left and a right module over itself, and $\operatorname{End}_R(R)$ is the ring $R$ acting by right multiplication.

**Proposition.** The regular module $R$ is a **generator** of $R\text{-}\mathbf{Mod}$: for every module $M$ there is a set $X$ and a surjection $R^{(X)}\to M$; equivalently, every module is a quotient of a free module.

*Proof.* Choose a generating set $X$ of $M$, which exists by taking $X=M$; the linear map $R^{(X)}\to M$ sending the basis element $x$ to $x$ is surjective. $\square$

**Proposition.** The functor $\operatorname{Hom}_R(R,-)$ is naturally isomorphic to the identity functor of $R\text{-}\mathbf{Mod}$: a linear map $R\to M$ is determined by the image of $1$, and every element of $M$ occurs. Dually $\operatorname{Hom}_R(-,R)$ is the dual-module functor on the side on which $R$ acts.

The regular module is the object through which the ring is recovered from its category: $\operatorname{End}_R(R)\cong R$ as rings, so a ring is an endomorphism ring of a module over itself. This is the first instance of the general principle that a category of modules determines the ring up to equivalence, treated below.

### Representable Functors and the Yoneda Lemma

**Definition.** A functor $F:\mathcal{C}^{\mathrm{op}}\to\mathbf{Set}$ is **representable** if there is an object $A$ and a natural isomorphism $F\cong\mathcal{C}(-,A)$; dually a covariant functor is representable if it is naturally isomorphic to $\mathcal{C}(A,-)$.

**Lemma (Yoneda).** For every functor $F:\mathcal{C}^{\mathrm{op}}\to\mathbf{Set}$ and every object $A$ there is a bijection $\operatorname{Nat}(\mathcal{C}(-,A),F)\cong F(A)$; consequently the functor $A\mapsto\mathcal{C}(-,A)$ is a full embedding $\mathcal{C}^{\mathrm{op}}\hookrightarrow[\mathcal{C},\mathbf{Set}]$.

*Proof.* A natural transformation $\eta:\mathcal{C}(-,A)\to F$ is determined by $\eta_A(\operatorname{id}_A)\in F(A)$, by naturality applied to the maps into $A$; conversely an element $u\in F(A)$ defines $\eta$ by $\eta_B(f)=F(f)(u)$. The two assignments are inverse. Fullness and faithfulness follow by applying the bijection to representable functors. $\square$

**Corollary.** The universal properties used throughout the corpus are representability statements. The tensor product represents the multilinear maps, the direct sum represents the families of maps, the kernel represents the maps killed by $f$, and the localisation represents the maps inverting a set. In every case the object is determined up to a unique isomorphism by the property.

**Example.** The functor $M\mapsto M\otimes_RN$ is not representable by a module in general: a representable functor $\operatorname{Hom}_R(A,-)$ is left exact, whereas $-\otimes_RN$ is left exact only when $N$ is flat. The functor $M\mapsto\operatorname{Hom}_R(N,M)$ is representable, by the module $N$ itself, since that is what $\operatorname{Hom}_R(N,-)$ means; the tensor–hom adjunction exhibits $-\otimes_RN$ as its left adjoint. When $N$ is finitely generated and projective the left adjoint is representable too, by the dual module $N^*=\operatorname{Hom}_R(N,R)$, since the natural map $N^*\otimes_RM\to\operatorname{Hom}_R(N,M)$ is then an isomorphism.

## Equivalence of Module Categories and Morita Equivalence

### Equivalence

**Definition.** Two rings $R$ and $S$ are **Morita equivalent** if the categories $R\text{-}\mathbf{Mod}$ and $S\text{-}\mathbf{Mod}$ are equivalent as additive categories. The relation is an equivalence relation on rings.

**Theorem.** A right exact additive functor $F:R\text{-}\mathbf{Mod}\to S\text{-}\mathbf{Mod}$ that preserves direct sums is naturally isomorphic to $F(R)\otimes_R-$, and it is an equivalence exactly when the right $R$-module $F(R)$ is a finitely generated projective generator of $R\text{-}\mathbf{Mod}$. Equivalently, the equivalences are the functors $P\otimes_R-$ for an $(S,R)$-bimodule $P$ that is a finitely generated projective generator as a right $R$-module; the bimodule is then the endomorphism ring in the sense that the left action of $S$ on $P$ identifies $S\cong\operatorname{End}_R(P)$, an anti-isomorphism being unnecessary because $P$ is a right module.

*Proof.* This is the Eilenberg–Watts theorem. The forward direction is the construction of the bimodule $P=F(R)$ and the natural isomorphism $F(M)\cong F(R)\otimes_RM$ for a right exact additive functor preserving direct sums. The converse is the Morita theorem, which identifies the inverse as $\operatorname{Hom}_S(P,-)$. $\square$

**Example.** The matrix ring $M_n(R)$ is Morita equivalent to $R$: the functor $R\text{-}\mathbf{Mod}\to M_n(R)\text{-}\mathbf{Mod}$ sending a module $M$ to the column module $M^n$, with $M_n(R)$ acting on the left by matrix multiplication, is an equivalence, with inverse $N\mapsto e_{11}N$; the progenerator is the left module $R^n$, and $\operatorname{End}_R(R^n)\cong M_n(R)$. Two rings $R$ and $S$ are Morita equivalent if and only if $S\cong\operatorname{End}_R(P)^{\mathrm{op}}$ for a finitely generated projective generator $P$ of $R\text{-}\mathbf{Mod}$; for a right $R$-module progenerator the anti-isomorphism is not needed and $S\cong\operatorname{End}_R(P)$, which is the form in which the Eilenberg–Watts theorem above produces it.

**Remark.** Morita equivalence preserves the categorical properties of modules — projectivity, injectivity, flatness, exactness, the existence of projective covers — but it does not preserve the ring: $R$ and $M_n(R)$ have isomorphic module categories while being different rings, and the centre is preserved up to isomorphism. The precise statement, the construction of the bimodule and the classification of equivalences belong to of the category *Linear Spaces over Linear Algebras*; here only the definition and the prototypical example are needed, to record that a module category is an invariant of the ring strictly coarser than the ring itself.

### The Centre and the Category

**Proposition.** If $R$ and $S$ are Morita equivalent then their centres are isomorphic as rings. Consequently two commutative rings are Morita equivalent if and only if they are isomorphic.

*Proof.* The centre of $R$ is the ring of natural endomorphisms of the identity functor of $R\text{-}\mathbf{Mod}$, namely the endomorphisms of the regular module that commute with all endomorphisms; an equivalence of categories induces a ring isomorphism between the rings of natural endomorphisms of the two identity functors. If $R$ is commutative and $S$ is Morita equivalent to $R$, then $S\cong Z(S)\cong Z(R)\cong R$ as rings, so the two rings are isomorphic. $\square$

### Left and Right Modules

For a ring $R$ the categories $R\text{-}\mathbf{Mod}$ and $\mathbf{Mod}\text{-}R$ are equivalent when $R$ is commutative, and in general $R\text{-}\mathbf{Mod}$ is equivalent to $\mathbf{Mod}\text{-}R^{\mathrm{op}}$. The bimodule ${}_S P_R$ is the natural home of the tensor product $P\otimes_R-$ giving a functor from right $R$-modules to left $S$-modules. These side conventions are the reason the corpus states the side of the modules whenever the ring is not commutative, and they are the reason the balanced product is stated for a right and a left module.

## Standard Constructions as Limits and Colimits

### Limits and Colimits

**Definition.** A **diagram** in $\mathcal{C}$ is a functor from a small category to $\mathcal{C}$. A **limit** of a diagram is an object representing the functor that assigns to $X$ the set of cones over the diagram; a **colimit** is the dual notion. Products and kernels are limits; coproducts, cokernels and quotients are colimits.

**Theorem.** The category $R\text{-}\mathbf{Mod}$ is complete and cocomplete: every small diagram has a limit and a colimit.

*Proof.* The forgetful functor to $\mathbf{Set}$ has a left adjoint, hence preserves limits, and it creates them: a limit cone in $\mathbf{Set}$ over the underlying diagram carries a unique module structure making it a limit cone in $R\text{-}\mathbf{Mod}$, the operations being defined componentwise and the universal property being that of the underlying sets. For colimits, take the quotient of the direct sum of the objects of the diagram by the relations imposed by the arrows, the filtered case being the direct limit of the articles on modules. $\square$

**Examples.** The kernel of $f$ is the limit of the diagram $\bullet\rightrightarrows\bullet$ built from $f$ and the zero map; the cokernel is the colimit. The equaliser of $f,g:M\to N$ is $\{m:f(m)=g(m)\}$, a limit, and the coequaliser is $N/\operatorname{im}(f-g)$, a colimit. The pushout of $B\leftarrow A\to C$ is $(B\oplus C)/\{(a,-a)\}$, and the pullback of $B\to D\leftarrow C$ is $\{(b,c):f(b)=g(c)\}\subseteq B\oplus C$.

### Filtered Colimits

**Definition.** A small category is **filtered** if every finite diagram in it has a cone. A **filtered colimit** is the colimit of a diagram indexed by a filtered category.

**Proposition.** Filtered colimits in $R\text{-}\mathbf{Mod}$ commute with finite limits, and in particular with finite direct sums, kernels and tensor products. The functor $\varinjlim$ over a filtered index category is exact.

*Proof.* An element of a filtered colimit of modules is represented by an element of one of the modules and two representatives agree when they become equal at a later stage; this description implies that finite limits and finite colimits commute, and exactness follows. $\square$

**Example.** Every module is the filtered colimit of its finitely generated submodules; this is the finiteness reduction used by the ideal criterion of the article on flatness and exactness, and it is the reason Lazard's theorem can be phrased as "flat means a filtered colimit of free modules".

## Summary

The left $R$-modules and the $R$-linear maps between them form the category $R\text{-}\mathbf{Mod}$, with composition of maps and identity maps. A functor between categories preserves composition and identities; the module-theoretic functors $\operatorname{Hom}_R(M,-)$, $\operatorname{Hom}_R(-,M)$ and $-\otimes_RM$ are additive, and their exactness properties are the categorical form of projectivity, injectivity and flatness. A natural transformation compares two functors by a commuting square for every morphism, and the naturality of the structural isomorphisms of the tensor product is what makes them usable under all induced maps.

The category $R\text{-}\mathbf{Mod}$ has a zero object and finite biproducts, so it is additive; it has all kernels and cokernels, and the canonical map $\operatorname{coim}f\to\operatorname{im}f$ is always an isomorphism, so it is the prototypical abelian category. It is complete and cocomplete, and filtered colimits are exact. The free–forgetful adjunction makes the free functor left adjoint to the forgetful functor, and the tensor–hom adjunction makes $-\otimes_RN$ left adjoint to $\operatorname{Hom}_R(N,-)$; left adjoints preserve colimits and right adjoints preserve limits, which is the reason the tensor product is right exact and $\operatorname{Hom}$ is left exact. The Yoneda lemma identifies universal properties with representability, and the regular module $R$ is a generator whose endomorphism ring is $R$.

Two rings are Morita equivalent when their module categories are equivalent; matrix rings over $R$ are the basic examples, the centre is an invariant so that two commutative rings are Morita equivalent only when they are isomorphic, and the classification is treated in of the category *Linear Spaces over Linear Algebras*. The abstract notions of additive and abelian category that $R\text{-}\mathbf{Mod}$ exemplifies, and the Grothendieck categories that generalise it, are not covered here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{C}$, $\mathcal{D}$ | categories; $\mathcal{C}^{\mathrm{op}}$ the opposite category |
| $\mathcal{C}(A,B)$, $\operatorname{Hom}_{\mathcal{C}}(A,B)$ | morphisms from $A$ to $B$ |
| $\operatorname{id}_A$ | identity morphism of $A$ |
| $F:\mathcal{C}\to\mathcal{D}$ | functor; faithful, full, essentially surjective, equivalence |
| $\eta:F\to G$ | natural transformation, component $\eta_A$ |
| $\mathcal{D}^{\mathcal{C}}$ | functor category |
| $R\text{-}\mathbf{Mod}$, $\mathbf{Mod}\text{-}R$, $R\text{-}\mathbf{mod}$ | left modules, right modules, finitely generated left modules |
| $\operatorname{Hom}_R(M,N)$ | $R$-module of linear maps |
| $f_*$, $f^*$ | postcomposition and precomposition |
| $0$, $A\oplus B$ | zero object, biproduct |
| $\ker f$, $\operatorname{coker}f$, $\operatorname{coim}f$, $\operatorname{im}f$ | kernel, cokernel, coimage, image |
| $F\dashv G$ | adjunction, $F$ left adjoint, $G$ right adjoint |
| $R^{(X)}$ | free $R$-module on the set $X$ |
| $\operatorname{End}_R(M)$ | ring of endomorphisms of $M$ |
| $\varinjlim$, $\varprojlim$ | filtered colimit, limit |
| $M_n(R)$ | ring of $n\times n$ matrices over $R$ |







## Further Reading

- Michael Artin, *Algebra*, 2nd ed. (Pearson, 2011), for categories of modules and the language of universal properties.
- Francis Borceux, *Handbook of Categorical Algebra 1: Basic Category Theory* (Cambridge University Press, 1994), for categories, functors, natural transformations and representability.
- Henri Cartan and Samuel Eilenberg, *Homological Algebra* (Princeton University Press, 1956), for the additive and abelian structure of module categories.
- Pierre Gabriel, "Des catégories abéliennes", *Bulletin de la Société Mathématique de France* 90 (1962), 323–448, for the abelian-category viewpoint and the embedding theorem.
- Saunders Mac Lane, *Categories for the Working Mathematician*, 2nd ed. (Springer, 1998), for adjunctions, limits and the Yoneda lemma.
- Barry Mitchell, "The full imbedding theorem", *American Journal of Mathematics* 86 (1964), 619–637, for the embedding of abelian categories into module categories.
- Joseph J. Rotman, *An Introduction to Homological Algebra* (Springer, 2nd ed. 2009), for module categories read homologically.
- Charles A. Weibel, *An Introduction to Homological Algebra* (Cambridge University Press, 1994), for additive and abelian categories in the service of homological algebra.
