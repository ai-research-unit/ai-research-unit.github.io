
# __Universal Properties and Categories__

## Introduction

A universal property describes an object by the maps into or out of it, rather than by its internal construction. The free monoid on a set, the product of two sets, the quotient of a set by an equivalence relation and the type of functions from one type to another are all solutions to problems of the same shape: an object is required, together with a map satisfying a condition, such that every other candidate factors through it uniquely. Category theory is the language in which this shape is stated once and for all. A **category** carries objects and composable maps, a **functor** carries one category into another, a **natural transformation** compares two functors, and the notions of **limit**, **adjoint functor** and **monad** are the general forms of the universal constructions that algebra performs.

The article is the ninth and last of the foundational layer of the corpus, above *Sets, Functions and Relations*, *Order Theory and Lattices*, *Set-Theoretic Foundations*, *Formal Logic and Computability*, *Model Theory* and *Proof Theory and Type Theory*. Its examples are drawn from those articles: the category of sets and functions, the category attached to a partial order and the lattice constructions of *Order Theory and Lattices*, the models and structures of *Model Theory*, and the types and terms of *Proof Theory and Type Theory*. Its purpose is to fix the vocabulary that the remainder of the corpus uses, and in particular the language in whichstates its constructions. Because it is foundational, it develops no algebra of its own: the examples are the sets, orders, monoids and types that the earlier articles provide, and the algebraic categories whose objects are introduced later — groups, rings, modules, vector spaces — are named and deferred, not developed.

The article is written under the same restriction as the rest of the foundational layer. No distance, no topology, no form appears. Where a construction has a richer form once a topology is available — the topological group, the completion, the sheaf — the article states the algebraic or order-theoretic version and defers the enrichment to Part II. The general homological algebra over a ring, and the functors $\operatorname{Ext}$ and $\operatorname{Tor}$, belong to the module-theoretic articles and are not developed here; the categorical constructions that those articles use — in particular the universal property of the tensor product — are stated in the form in which they will be applied and are proved there.

## Categories, Functors and Natural Transformations

### Categories

**Definition.** A **category** $\mathcal{C}$ consists of

1. a class $\operatorname{Ob}(\mathcal{C})$ of **objects**;
2. for each pair of objects $A, B$, a set $\mathcal{C}(A,B)$ of **morphisms** from $A$ to $B$, written $f : A \to B$, with $A$ the **domain** and $B$ the **codomain**;
3. for each triple $A,B,C$ a **composition** function $\mathcal{C}(B,C) \times \mathcal{C}(A,B) \to \mathcal{C}(A,C)$, $(g,f) \mapsto g \circ f$;
4. for each object $A$ an **identity** morphism $\mathrm{id}_A : A \to A$;

subject to the axioms

$$
h \circ (g \circ f) = (h \circ g) \circ f, \qquad \mathrm{id}_B \circ f = f = f \circ \mathrm{id}_A
$$

for all $f : A \to B$, $g : B \to C$, $h : C \to D$. A category is **small** if its objects and morphisms form sets, and **locally small** if each $\mathcal{C}(A,B)$ is a set.

The class-and-set distinction is that of *Set-Theoretic Foundations*: the objects of a category are usually a proper class, which is why the definition says "class". A morphism $f : A \to B$ is an **isomorphism** if there is $g : B \to A$ with $g \circ f = \mathrm{id}_A$ and $f \circ g = \mathrm{id}_B$; the inverse is unique when it exists, and $A \cong B$ means that the two objects are isomorphic.

**Example (Set).** The category $\mathbf{Set}$ has all sets as objects and all functions as morphisms, with the usual composition and identity functions. It is locally small but not small.

**Example (Pos).** The category $\mathbf{Pos}$ has partially ordered sets as objects and order-preserving maps as morphisms; the facts used are those of *Order Theory and Lattices*.

**Example (a poset as a category).** A partially ordered set $(P, \leq)$ becomes a category whose objects are the elements of $P$, with a single morphism $x \to y$ when $x \leq y$ and none otherwise. Composition is transitivity and the identity is reflexivity. This example is the bridge between order theory and category theory: a **monotone map** is exactly a functor between such categories, and the order-theoretic constructions of *Order Theory and Lattices* are the categorical limits and colimits of the next sections.

**Definition.** A **monoid** is a set $M$ with an associative binary operation and an identity element; a **monoid homomorphism** is a function preserving the operation and the identity. Monoids are used in this article as the simplest algebraic example of a category, and their theory, like that of the groups that refine them, belongs to the algebraic articles of the corpus.

**Example (a monoid as a category).** A monoid $(M, \cdot, e)$ becomes a category with a single object $\ast$, whose morphisms $\ast \to \ast$ are the elements of $M$, with composition the multiplication and the identity $e$. Conversely a category with one object is a monoid. This example shows that the composition axiom is exactly associativity, and it is the reason the categorical formulation of a group action is stated with a single object.

**Example (the category of types).** The simply typed lambda calculus of *Proof Theory and Type Theory* yields a category $\mathbf{Type}$ whose objects are the types and whose morphisms $A \to B$ are the terms of type $A \to B$ modulo $\beta\eta$-conversion, with composition the substitution of one term into another. The categorical reading of the Curry–Howard correspondence is that this category has, for each pair of types, a product and an exponential, which is the content of the last section.

### Functors

**Definition.** A **functor** $F : \mathcal{C} \to \mathcal{D}$ assigns to each object $A$ of $\mathcal{C}$ an object $F(A)$ of $\mathcal{D}$, and to each morphism $f : A \to B$ a morphism $F(f) : F(A) \to F(B)$, such that

$$
F(\mathrm{id}_A) = \mathrm{id}_{F(A)}, \qquad F(g \circ f) = F(g) \circ F(f).
$$

A **contravariant functor** reverses the arrows: $F(f) : F(B) \to F(A)$ and $F(g \circ f) = F(f) \circ F(g)$. A functor preserves composition and identities but need not preserve the properties of morphisms: $F(f)$ can fail to be injective or surjective when $f$ is.

**Example (forgetful functors).** The functor $U : \mathbf{Pos} \to \mathbf{Set}$ sending a partially ordered set to its underlying set and an order-preserving map to itself is **forgetful**: it discards structure. The functor from monoids to sets is forgetful in the same sense. Forgetful functors are the typical right adjoints of the next sections, and the free constructions are their left adjoints.

**Example (hom-functors).** For a fixed object $A$ of a locally small category $\mathcal{C}$, the assignment $B \mapsto \mathcal{C}(A,B)$ extends to a functor $\mathcal{C}(A,-) : \mathcal{C} \to \mathbf{Set}$, called the **covariant hom-functor**, by sending $f : B \to C$ to the function $g \mapsto f \circ g$. Dually $B \mapsto \mathcal{C}(B,A)$ extends to a contravariant functor $\mathcal{C}(-,A)$. These functors are the subject of the Yoneda lemma.

### Natural Transformations

**Definition.** Let $F, G : \mathcal{C} \to \mathcal{D}$ be functors. A **natural transformation** $\eta : F \Rightarrow G$ assigns to each object $A$ of $\mathcal{C}$ a morphism $\eta_A : F(A) \to G(A)$ in $\mathcal{D}$ such that for every $f : A \to B$ the two composites

$$
F(A) \xrightarrow{\ \eta_A\ } G(A) \xrightarrow{\ G(f)\ } G(B), \qquad F(A) \xrightarrow{\ F(f)\ } F(B) \xrightarrow{\ \eta_B\ } G(B)
$$

are equal: $G(f) \circ \eta_A = \eta_B \circ F(f)$. The transformation is a **natural isomorphism** if every $\eta_A$ is an isomorphism, and then $F \cong G$.

**Definition.** A **functor category** $[\mathcal{C},\mathcal{D}]$ (also written $\mathcal{D}^{\mathcal{C}}$) has the functors $\mathcal{C} \to \mathcal{D}$ as objects and the natural transformations between them as morphisms, with composition defined objectwise. A **presheaf** on $\mathcal{C}$ is a functor $\mathcal{C}^{\mathrm{op}} \to \mathbf{Set}$, that is, a contravariant functor from $\mathcal{C}$ to sets.

**Example (the singleton map).** Let $\mathcal{P} : \mathbf{Set} \to \mathbf{Set}$ send a set to its power set and a function $f : X \to Y$ to the image map $A \mapsto f(A)$. The assignment $x \mapsto \{x\}$ is a natural transformation $\mathrm{id}_{\mathbf{Set}} \Rightarrow \mathcal{P}$: the square commutes because $f(\{x\}) = \{f(x)\}$. It is injective on every set and surjective only on the empty set and the singletons, so it is a natural transformation that is not an isomorphism; the same transformation is the unit of the power-set monad below.

**Definition.** A functor $F : \mathcal{C} \to \mathcal{D}$ is an **equivalence of categories** if there is a functor $G : \mathcal{D} \to \mathcal{C}$ and natural isomorphisms $G \circ F \cong \mathrm{id}_{\mathcal{C}}$ and $F \circ G \cong \mathrm{id}_{\mathcal{D}}$. An equivalence is the correct notion of sameness of categories: it need not be a bijection on objects, only on isomorphism classes.

**Theorem.** A functor $F : \mathcal{C} \to \mathcal{D}$ is an equivalence if and only if it is **fully faithful** (each map $\mathcal{C}(A,B) \to \mathcal{D}(F(A),F(B))$, $f \mapsto F(f)$, is a bijection) and **essentially surjective** (every object of $\mathcal{D}$ is isomorphic to $F(A)$ for some $A$).

**Proof sketch.** Given an equivalence, the full faithfulness follows from the natural isomorphism and the essential surjectivity from the counit. Conversely, choose for each object $D$ of $\mathcal{D}$ an object $G(D)$ of $\mathcal{C}$ and an isomorphism $\varepsilon_D : F(G(D)) \to D$, and define $G$ on morphisms by transporting along $\varepsilon$ and using full faithfulness. The natural transformations $\varepsilon$ and the analogous $\eta : \mathrm{id}_{\mathcal{C}} \Rightarrow G \circ F$ are then isomorphisms. $\square$

## Universal Properties

### Initial and Terminal Objects

**Definition.** An object $I$ of a category $\mathcal{C}$ is **initial** if for every object $A$ there is exactly one morphism $I \to A$. It is **terminal** if for every $A$ there is exactly one morphism $A \to I$. An object that is both is a **zero object**.

**Proposition.** Initial and terminal objects are unique up to isomorphism when they exist.

**Proof.** If $I$ and $I'$ are initial, the unique morphisms $I \to I'$ and $I' \to I$ compose to the unique endomorphisms of $I$ and $I'$, which are the identities; hence they are inverse isomorphisms. The terminal case is dual. $\square$

**Example.** In $\mathbf{Set}$ the empty set is initial and every singleton is terminal. In the category attached to a poset, an initial object is a least element and a terminal object a greatest element. In the category of monoids, the one-element monoid is both initial and terminal, hence a zero object. In the category of types of the previous section, the empty type is initial and the unit type is terminal, in the reading of *Proof Theory and Type Theory*.

### Products and Coproducts

**Definition.** Let $A$ and $B$ be objects of a category $\mathcal{C}$. A **product** of $A$ and $B$ is an object $A \times B$ with morphisms $\pi_1 : A \times B \to A$ and $\pi_2 : A \times B \to B$, the **projections**, such that for every object $X$ and every pair of morphisms $f : X \to A$, $g : X \to B$ there is a unique morphism $\langle f, g\rangle : X \to A \times B$ with $\pi_1 \circ \langle f,g\rangle = f$ and $\pi_2 \circ \langle f,g\rangle = g$. A **coproduct** $A + B$ is the dual: morphisms $\iota_1 : A \to A+B$, $\iota_2 : B \to A+B$, and for every $X$ with $f : A \to X$, $g : B \to X$ a unique $[f,g] : A+B \to X$ with $[f,g]\circ\iota_1 = f$ and $[f,g]\circ\iota_2 = g$.

**Proposition.** Products and coproducts are unique up to isomorphism when they exist.

**Proof.** If $(A\times B, \pi_1,\pi_2)$ and $(P, p_1, p_2)$ are both products, the universal property applied to $P$ gives a morphism $P \to A \times B$, and applied to $A\times B$ gives one back; the composites satisfy the universal property of the identity and hence equal $\mathrm{id}$ by uniqueness. $\square$

**Example.** In $\mathbf{Set}$ the product is the Cartesian product with its coordinate projections, and the coproduct is the disjoint union with its inclusions. In the category attached to a poset, the product is the greatest lower bound and the coproduct the least upper bound, when they exist: the universal property of a product is exactly the property of a meet in *Order Theory and Lattices*. In the category of types, the product and coproduct are the product and sum types of *Proof Theory and Type Theory*, and the universal property is the typing of the pairing and case-splitting rules.

**Definition.** A **cartesian closed category** has a terminal object, a product $A \times B$ for every pair, and for every pair $A, B$ an object $B^A$ together with an **evaluation** morphism $\mathrm{ev} : B^A \times A \to B$ such that for every $f : X \times A \to B$ there is a unique $\lambda f : X \to B^A$ with $\mathrm{ev} \circ (\lambda f \times \mathrm{id}_A) = f$. The object $B^A$ is the **exponential**.

**Theorem.** The category of types of *Proof Theory and Type Theory* is cartesian closed, with the unit type as terminal object, the product types as products and the function types as exponentials.

**Proof sketch.** The projections and pairing are the elimination rules of the product, and the evaluation and currying are the rules for the function type; the uniqueness clauses are the $\beta\eta$-equalities of the typed calculus, which hold by construction in the category of types modulo $\beta\eta$-conversion. $\square$

### Universal Arrows and Free Objects

**Definition.** Let $F : \mathcal{C} \to \mathcal{D}$ be a functor and $D$ an object of $\mathcal{D}$. A **universal arrow** from $D$ to $F$ is a pair $(C, u)$ with $C$ an object of $\mathcal{C}$ and $u : D \to F(C)$ a morphism such that for every $C'$ and every $v : D \to F(C')$ there is a unique $f : C \to C'$ with $F(f) \circ u = v$.

**Example (free monoid).** Let $U : \mathbf{Mon} \to \mathbf{Set}$ be the forgetful functor from monoids to sets. For a set $X$, let $X^*$ be the set of finite words in the alphabet $X$, with concatenation and the empty word as multiplication and identity; this is the **free monoid** on $X$. The insertion $u : X \to U(X^*)$ sending a letter to the one-letter word, with $X^*$, is a universal arrow from $X$ to $U$. Indeed, a monoid homomorphism $X^* \to M$ is determined by its values on the one-letter words, and any function $X \to U(M)$ extends uniquely to a homomorphism.

**Remark.** The free group on a set, the free module on a set, the free algebra of a signature and the tensor product of modules are all universal arrows of the same shape, and their constructions belong,andall. The present article supplies the schema; those articles supply the objects.

## Limits and Colimits

### Diagrams and Cones

**Definition.** Let $\mathcal{J}$ be a small category, the **index category**, and $\mathcal{C}$ a category. A **diagram** of shape $\mathcal{J}$ in $\mathcal{C}$ is a functor $D : \mathcal{J} \to \mathcal{C}$. A **cone** over $D$ is an object $L$ of $\mathcal{C}$ with morphisms $\lambda_j : L \to D(j)$ for each object $j$ of $\mathcal{J}$, such that for every morphism $u : j \to k$ of $\mathcal{J}$ one has $D(u) \circ \lambda_j = \lambda_k$. A **cocone** is the dual, with morphisms $D(j) \to L$ and the reverse equations.

**Definition.** A **limit** of $D$ is a cone $(\varprojlim D, \lambda_j)$ such that for every cone $(L', \lambda'_j)$ there is a unique morphism $h : L' \to \varprojlim D$ with $\lambda_j \circ h = \lambda'_j$ for all $j$. A **colimit** $\varinjlim D$ is the dual notion.

**Example.** The limit of the empty diagram is the terminal object and its colimit the initial object. The limit of a diagram with two objects and no nonidentity morphisms is the product, and the colimit is the coproduct. The limit of a diagram $\cdot \rightrightarrows \cdot$ (two parallel morphisms) is the **equaliser**, and the colimit is the **coequaliser**. In $\mathbf{Set}$, the equaliser of $f, g : A \to B$ is $\{a \in A : f(a) = g(a)\}$ with its inclusion, and the coequaliser is the quotient of $B$ by the least equivalence relation generated by the pairs $(f(a), g(a))$. The quotient construction of *Sets, Functions and Relations* is therefore the coequaliser of the two projections of the equivalence relation, and this is its categorical characterisation.

**Definition.** A category is **complete** if it has all small limits, and **cocomplete** if it has all small colimits. A functor **preserves limits** if it carries every limit cone to a limit cone, and **preserves** a limit **up to isomorphism** if it carries a limiting cone to a cone that is again limiting.

**Theorem.** A category is complete if and only if it has all small products and all equalisers. It is cocomplete if and only if it has all small coproducts and all coequalisers.

**Proof sketch.** A limit of an arbitrary small diagram is built as the equaliser of two morphisms between products indexed by the objects and by the morphisms of the index category: one of the two maps uses the projections of the diagram and the other the action of the diagram's morphisms. The converse is immediate. $\square$

**Example.** $\mathbf{Set}$ is complete and cocomplete: products, coproducts, equalisers and coequalisers are constructed as above, and the theorem gives all small limits and colimits. The category of types with sums and products is similarly complete and cocomplete for the limits and colimits generated by the type formers. The category attached to a poset is complete exactly when the poset has all meets of small subsets, and the completeness of a lattice in the sense of *Order Theory and Lattices* is this condition.

## Adjoint Functors

### Definition and Examples

**Definition.** Let $F : \mathcal{C} \to \mathcal{D}$ and $G : \mathcal{D} \to \mathcal{C}$ be functors. $F$ is **left adjoint** to $G$, written $F \dashv G$, if there is a bijection

$$
\mathcal{D}(F(C), D) \cong \mathcal{C}(C, G(D))
$$

for all objects $C$ of $\mathcal{C}$ and $D$ of $\mathcal{D}$, natural in $C$ and in $D$. The functor $G$ is the **right adjoint** of $F$.

**Example.** The free-monoid functor $(-)^* : \mathbf{Set} \to \mathbf{Mon}$ is left adjoint to the forgetful functor $U : \mathbf{Mon} \to \mathbf{Set}$: the universal property of the free monoid is exactly the natural bijection $\mathbf{Mon}(X^*, M) \cong \mathbf{Set}(X, U(M))$. In the same way, a forgetful functor from any category of algebras to sets has a left adjoint, the free algebra on the set.

**Example.** In $\mathbf{Set}$, the product functor $(-) \times A$ is left adjoint to the exponential functor $(-)^A$: the bijection $\mathbf{Set}(X \times A, B) \cong \mathbf{Set}(X, B^A)$ is currying, and it is the equational form of the cartesian closed condition. This is the categorical form of the rule that a function of two variables is the same thing as a function of one variable with values in functions, which is the rule for the function type in *Proof Theory and Type Theory*.

**Example.** In the category attached to a poset, $F \dashv G$ is a **Galois connection** in the sense of *Order Theory and Lattices*: monotone maps with $F(x) \leq y \iff x \leq G(y)$. The Knaster–Tarski fixed-point theorem is the special case in which the two adjoints coincide.

**Proposition (uniqueness).** Left adjoints are unique up to natural isomorphism, and right adjoints are unique up to natural isomorphism.

**Proof.** If $F$ and $F'$ are both left adjoint to $G$, the natural bijections give a natural bijection $\mathcal{D}(F(C), D) \cong \mathcal{D}(F'(C), D)$ for all $D$, and the Yoneda lemma below identifies $F(C)$ with $F'(C)$ naturally. $\square$

### Unit and Counit

**Definition.** Let $F \dashv G$ with bijection $\varphi_{C,D} : \mathcal{D}(F(C),D) \to \mathcal{C}(C,G(D))$. The **unit** $\eta : \mathrm{id}_{\mathcal{C}} \Rightarrow G \circ F$ has components $\eta_C = \varphi_{C,F(C)}(\mathrm{id}_{F(C)}) : C \to G(F(C))$, and the **counit** $\varepsilon : F \circ G \Rightarrow \mathrm{id}_{\mathcal{D}}$ has components $\varepsilon_D = \varphi_{G(D),D}^{-1}(\mathrm{id}_{G(D)}) : F(G(D)) \to D$.

**Theorem (triangular identities).** With the notation above, the composites

$$
F \xrightarrow{\ F\eta\ } F \circ G \circ F \xrightarrow{\ \varepsilon F\ } F,
\qquad
G \xrightarrow{\ \eta G\ } G \circ F \circ G \xrightarrow{\ G\varepsilon\ } G
$$

are the identities of $F$ and of $G$. Conversely, a pair of natural transformations $\eta : \mathrm{id}_{\mathcal{C}} \Rightarrow G \circ F$ and $\varepsilon : F \circ G \Rightarrow \mathrm{id}_{\mathcal{D}}$ satisfying the two identities makes $F$ left adjoint to $G$.

**Proof sketch.** The first identity is checked on components using the naturality of $\varphi$: $(\varepsilon F)_C \circ (F\eta)_C = \varepsilon_{F(C)} \circ F(\eta_C)$, and under the adjunction bijection this is the identity of $F(C)$. The converse defines $\varphi$ by $\varphi(f) = G(f) \circ \eta_C$ and $\varphi^{-1}(g) = \varepsilon_D \circ F(g)$, and the triangular identities are what make the two inverse. $\square$

The unit and counit are the useful form of an adjunction: the unit is the insertion of an object into its free algebra, and the counit is the evaluation of a free algebra on its generators. In the free-monoid example, $\eta_X : X \to U(X^*)$ is the insertion of letters and $\varepsilon_M : U(M)^* \to M$ is the multiplication of a word in $M$.

**Theorem (general adjoint functor theorem, statement).** Let $G : \mathcal{D} \to \mathcal{C}$ be a functor with $\mathcal{D}$ complete and locally small. Then $G$ has a left adjoint if and only if $G$ preserves all small limits and satisfies the **solution set condition**: for every object $C$ of $\mathcal{C}$ there is a set of objects $D_i$ of $\mathcal{D}$ such that every morphism $C \to G(D)$ factors through some $C \to G(D_i)$. Freyd's special form replaces the solution set condition by the hypotheses that $\mathcal{C}$ be well powered and that the hom-sets of $\mathcal{D}$ be small. The theorem is what turns the existence of free objects, of products and of quotients in a concrete algebraic category into a set-theoretic verification.

## The Yoneda Lemma

### Presheaves and Representables

**Definition.** Let $\mathcal{C}$ be locally small. The **Yoneda embedding** is the functor $Y : \mathcal{C} \to [\mathcal{C}^{\mathrm{op}}, \mathbf{Set}]$ sending an object $A$ to the presheaf $\mathcal{C}(-,A)$ and a morphism $f : A \to B$ to the natural transformation $\mathcal{C}(-,A) \Rightarrow \mathcal{C}(-,B)$ given by composition with $f$. A presheaf is **representable** if it is naturally isomorphic to $\mathcal{C}(-,A)$ for some $A$, and then $A$ **represents** it.

**Theorem (Yoneda lemma).** For a locally small category $\mathcal{C}$, an object $A$ and a presheaf $F : \mathcal{C}^{\mathrm{op}} \to \mathbf{Set}$, the map

$$
[\mathcal{C}^{\mathrm{op}},\mathbf{Set}](\mathcal{C}(-,A), F) \longrightarrow F(A), \qquad \eta \mapsto \eta_A(\mathrm{id}_A),
$$

is a bijection, natural in $A$ and in $F$.

**Proof.** Given $\eta : \mathcal{C}(-,A) \Rightarrow F$, the component $\eta_A$ sends $\mathrm{id}_A$ to an element of $F(A)$; this defines the map. In the other direction, an element $x \in F(A)$ determines $\eta_x$ by $\eta_x{}_B(f) = F(f)(x)$ for $f : B \to A$; naturality is the equation $F(g)(F(f)(x)) = F(f \circ g)(x)$ for $g : C \to B$, which holds because $F$ is a functor. The two assignments are inverse: from $x$ one recovers $x$ as $\eta_x{}_A(\mathrm{id}_A)$, and from $\eta$ one recovers $\eta$ because $\eta_B(f) = \eta_B(\mathcal{C}(-,A)(f)(\mathrm{id}_A)) = F(f)(\eta_A(\mathrm{id}_A))$ by naturality. Naturality in $A$ and $F$ is a diagram chase. $\square$

### Consequences

**Corollary (Yoneda embedding is full and faithful).** The functor $Y$ is fully faithful: for all $A, B$ the map $\mathcal{C}(A,B) \to [\mathcal{C}^{\mathrm{op}},\mathbf{Set}](\mathcal{C}(-,A),\mathcal{C}(-,B))$ is a bijection.

**Proof.** Apply the Yoneda lemma with $F = \mathcal{C}(-,B)$: the natural transformations $\mathcal{C}(-,A) \Rightarrow \mathcal{C}(-,B)$ correspond bijectively to the elements of $\mathcal{C}(A,B)$, and the correspondence is composition with $f$. $\square$

**Corollary (representing objects are unique).** If $\mathcal{C}(-,A) \cong \mathcal{C}(-,B)$ then $A \cong B$.

**Corollary (a universal property determines its object).** An object defined by a universal property is determined up to isomorphism, and any two objects satisfying the property are canonically isomorphic. This is the corollary that justifies the whole practice of algebra by universal properties: a free object, a product, a tensor product or a quotient is determined by its mapping property, and the explicit construction is used only to prove existence.

**Corollary (limits by representability).** A cone $(\varprojlim D, \lambda_j)$ over a diagram $D : \mathcal{J} \to \mathcal{C}$ is a limit if and only if the presheaf $\mathcal{C}(-, \varprojlim D)$ is naturally isomorphic to the presheaf $X \mapsto \varprojlim_j \mathcal{C}(X, D(j))$ of cones over $D$ with apex $X$.

The last corollary is the reason limits are a universal property: a limit is the representing object of the functor of cones, and the Yoneda lemma then characterises it up to isomorphism.

## Monads

### Definition and Examples

**Definition.** A **monad** on a category $\mathcal{C}$ is a triple $(T, \eta, \mu)$ consisting of a functor $T : \mathcal{C} \to \mathcal{C}$ and natural transformations $\eta : \mathrm{id}_{\mathcal{C}} \Rightarrow T$ and $\mu : T \circ T \Rightarrow T$ satisfying

$$
\mu \circ T\mu = \mu \circ \mu T, \qquad \mu \circ T\eta = \mathrm{id}_T = \mu \circ \eta T.
$$

A **comonad** is the dual.

**Example (the list monad).** On $\mathbf{Set}$, let $T(X) = X^*$ be the free monoid on $X$, $\eta_X : X \to X^*$ the insertion of one-letter words and $\mu_X : (X^*)^* \to X^*$ the flattening of a list of lists into a single list by concatenation. The two monad laws are the statement that flattening is associative and that flattening a list of one-letter lists reproduces the list. The same data arise in the category of types as the type of lists, and the monad laws are the equations of the **fold** operations.

**Example (the power-set monad).** $T(X) = \mathcal{P}(X)$, with $\eta_X(x) = \{x\}$ and $\mu_X(\mathcal{A}) = \bigcup \mathcal{A}$, is a monad on $\mathbf{Set}$; the monad laws are the elementary properties of union and singleton.

**Example (a closure operator).** In a poset, a monotone map $T$ with $x \leq T(x)$ and $T(T(x)) \leq T(x)$ is a monad on the poset regarded as a category; a **closure operator** in the sense of *Order Theory and Lattices* is exactly a monad that is **idempotent**, that is, $\mu$ is an isomorphism. This example is the reason the general theory of monads subsumes both algebraic closure and the algebraic operations of the next sections.

### Algebras for a Monad, and Monads from Adjunctions

**Definition.** An **algebra** for a monad $(T,\eta,\mu)$ on $\mathcal{C}$ is a pair $(A, a)$ with $a : T(A) \to A$ a morphism satisfying $a \circ \eta_A = \mathrm{id}_A$ and $a \circ \mu_A = a \circ T(a)$. A **homomorphism** of algebras $(A,a) \to (B,b)$ is a morphism $f : A \to B$ with $f \circ a = b \circ T(f)$. The resulting category is the **Eilenberg–Moore category** $\mathcal{C}^T$.

**Example.** For the list monad, an algebra is a set $A$ with a function $a : A^* \to A$ that is a left inverse to the insertion and is compatible with flattening; by the first law, $a$ is determined by its values on two-letter words, and the second law makes the resulting binary operation associative with the empty word as identity. Thus the algebras for the list monad are exactly the monoids, and the Eilenberg–Moore category of the list monad is the category of monoids. This is the general phenomenon: **an algebraic theory is a monad, and its models are its algebras**.

**Theorem.** Every adjunction $F \dashv G$ between categories $\mathcal{C}$ and $\mathcal{D}$ gives rise to a monad on $\mathcal{C}$ with $T = G \circ F$, $\eta$ the unit of the adjunction and $\mu = G\varepsilon F$; dually it gives a comonad on $\mathcal{D}$. Conversely every monad arises from an adjunction, in fact from two: the **Kleisli** adjunction, whose category has the objects of $\mathcal{C}$ and whose morphisms $A \to B$ are the morphisms $A \to T(B)$ composed through $\mu$, and the Eilenberg–Moore adjunction, whose category is $\mathcal{C}^T$.

**Proof sketch.** For the first statement, the triangular identities of the adjunction give the two monad laws, and the verification is a calculation with $\eta$ and $\varepsilon$. For the converse, the Kleisli category has the free algebras as its objects, and the Eilenberg–Moore category has all algebras; the two adjunctions induce the given monad because $G \circ F$ recovers $T$ on both. $\square$

**Remark.** The monadicity theorem of Beck gives a criterion for a right adjoint to be the Eilenberg–Moore comparison functor, hence for a category to be the category of algebras of a monad over another. The theory is the categorical form of universal algebra, and it is used in the corpus for the algebraic theories whose models are groups, rings and modules, whose constructions are in the corresponding articles .

## Universal Properties in Algebra

### The Pattern of Universal Constructions

The constructions of algebra are of two related kinds: those that freely add structure, and those that impose relations.

**Definition.** Let $\mathcal{C}$ be a category and let $R$ be a relation on the morphisms of $\mathcal{C}$, that is, a set of pairs of parallel morphisms. A **quotient** of $A$ by $R$ is a coequaliser of the two morphisms of a pair in $R$, when it exists. A **free object** on a set $X$ with respect to a forgetful functor $U$ is the universal arrow from $X$ to $U$.

**Example (quotient in Set).** The coequaliser of two maps $f, g : A \to B$ in $\mathbf{Set}$ is the quotient of $B$ by the smallest equivalence relation containing all pairs $(f(a), g(a))$, with the universal property that a function on the quotient is a function on $B$ constant on the equivalence classes. The quotients of *Sets, Functions and Relations* are the coequalisers of this form.

**Example (tensor product, stated).** For modules $M$ and $N$ over a commutative ring $R$, the tensor product $M \otimes_R N$ is characterised by the universal property that $R$-bilinear maps $M \times N \to P$ correspond naturally to $R$-linear maps $M \otimes_R N \to P$. The construction and the proof of existence belong and *Linear Spaces*; the universal property is recorded here because it is the prototype of a **representable functor** defined by multilinear data, and becauseuses the same form of argument.

### The Categorical Content of the Curry–Howard Correspondence

The categories of *Proof Theory and Type Theory* assemble into a picture that the categorical language describes.

**Theorem.** The simply typed lambda calculus gives a cartesian closed category: the objects are the types, the morphisms $A \to B$ are the terms of type $B$ in a context containing a variable of type $A$, modulo $\beta\eta$-conversion, and the constructions of products and exponentials are the type formers with their introduction and elimination rules. Under the Curry–Howard correspondence, a term is a derivation, and the commutative diagrams of the category are the equations between derivations induced by $\beta\eta$-conversion.

**Proof sketch.** Composition is substitution, which is associative by the substitution lemma; the identity is the variable; the terminal object is the unit type, the product is the product type with the pairing and projections, and the exponential is the function type with abstraction and evaluation. The universal properties are the typing rules, and uniqueness is the $\eta$-equation. $\square$

## Summary

A category consists of objects, morphisms with domains and codomains, associative composition and identities. The examples include the category of sets, the category of partially ordered sets, a partially ordered set regarded as a category, a monoid regarded as a one-object category, and the category of types of the typed lambda calculus. A functor preserves composition and identities; a natural transformation compares two functors by a family of morphisms commuting with the action of both; an equivalence of categories is a fully faithful and essentially surjective functor.

Initial and terminal objects, products and coproducts, and more generally limits and colimits of diagrams, are defined by universal properties and are unique up to isomorphism when they exist. Limits are the representing objects of the functors of cones; a category is complete exactly when it has all small products and equalisers, and cocomplete exactly when it has all small coproducts and coequalisers. Products and coproducts in a poset are meets and joins, and in the category of types they are the product and sum types.

An adjunction $F \dashv G$ is a natural bijection between the morphisms $F(C) \to D$ and $C \to G(D)$; the free-forgetful adjunctions, currying and the Galois connections of order theory are the standard examples. An adjunction is equivalently given by a unit and a counit satisfying the triangular identities, and the adjoint functor theorem gives a criterion for a left adjoint to exist. The Yoneda lemma identifies the natural transformations from a representable presheaf into a presheaf $F$ with the elements of $F(A)$; it makes the Yoneda embedding full and faithful and shows that an object defined by a universal property is determined up to isomorphism.

A monad is a functor with a unit and a multiplication satisfying associativity and the unit laws; the list monad and the power-set monad are the standard examples, and the algebras for the list monad are the monoids. Every adjunction produces a monad, and every monad arises from the Kleisli and Eilenberg–Moore adjunctions. In algebra, free objects are universal arrows from a set to a forgetful functor, quotients are coequalisers, and the tensor product is the representing object of the bilinear maps; the constructions themselves belong to the algebraic other articles, and the categorical schema is the one fixed here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{C}, \mathcal{D}$ | Categories |
| $\operatorname{Ob}(\mathcal{C})$ | Class of objects of $\mathcal{C}$ |
| $\mathcal{C}(A,B)$, $\operatorname{Hom}(A,B)$ | Morphisms from $A$ to $B$ |
| $g \circ f$, $\mathrm{id}_A$ | Composition and identity morphism |
| $\mathbf{Set}$, $\mathbf{Pos}$, $\mathbf{Mon}$ | Categories of sets, posets, monoids |
| $F : \mathcal{C} \to \mathcal{D}$ | Functor; contravariant functor reverses arrows |
| $\eta : F \Rightarrow G$ | Natural transformation; natural isomorphism $F \cong G$ |
| $[\mathcal{C},\mathcal{D}]$, $\mathcal{D}^{\mathcal{C}}$ | Functor category |
| $A \times B$, $A + B$ | Product and coproduct |
| $B^A$, $\mathrm{ev}$ | Exponential and evaluation; cartesian closed category |
| $I$, $A \times B$, $A+B$, equaliser, coequaliser | Constructions by universal property |
| $\varprojlim D$, $\varinjlim D$ | Limit and colimit of a diagram $D$ |
| $F \dashv G$ | $F$ left adjoint to $G$ |
| $\eta$, $\varepsilon$ | Unit and counit of an adjunction |
| $\mathcal{C}(-,A)$, $Y$ | Representable presheaf; Yoneda embedding |
| $(T,\eta,\mu)$ | Monad; $\mathcal{C}^T$ Eilenberg–Moore category |
| $X^*$ | Free monoid on $X$ |
| $\otimes_R$ | Tensor product over $R$ (universal property stated here) |





## Further Reading

- Saunders Mac Lane, *Categories for the Working Mathematician*, 2nd ed. (Springer, 1998), for the canonical treatment of categories, functors, limits, adjoints and monads.
- Samuel Eilenberg and Saunders Mac Lane, "General theory of natural equivalences", *Transactions of the American Mathematical Society* **58** (1945), 231–294, for the origin of categories, functors and natural transformations.
- Nobuo Yoneda, "On the homology theory of modules", *Journal of the Faculty of Science, University of Tokyo* **7** (1954), 193–227, for the lemma that carries his name.
- Peter Freyd, *Abelian Categories: An Introduction to the Theory of Functors* (Harper and Row, 1964), for adjoint functors and the adjoint functor theorems.
- Saunders Mac Lane, "Groups, categories and duality", *Proceedings of the National Academy of Sciences* **34** (1948), 263–267, for the categorical treatment of groups and the origin of monads.
- Michael Barr and Charles Wells, *Category Theory for Computing Science*, 3rd ed. (Les Publications CRM, 1999), for limits, adjunctions and the categorical reading of type theories.
- Joachim Lambek and Philip J. Scott, *Introduction to Higher Order Categorical Logic* (Cambridge University Press, 1986), for cartesian closed categories and the Curry–Howard correspondence.
