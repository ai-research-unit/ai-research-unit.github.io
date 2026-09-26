
# __Higher Algebra and Higher Categories__

## Introduction

An ordinary category has objects and morphisms; between two parallel morphisms there is only the question whether they are equal. In the homotopy theory of the preceding articles equality is the wrong relation: two maps are the same only up to a homotopy, two homotopies only up to a homotopy of homotopies, and so on without end. A **higher category** is the structure that keeps all of this data: an $\infty$-category has objects, morphisms, $2$-morphisms between parallel morphisms, $3$-morphisms between parallel $2$-morphisms, and so on, with composition defined only up to coherent higher morphisms. When all the $k$-morphisms for $k \geq 2$ are invertible, the result is an **$\infty$-category** in the sense of the term used throughout this corpus, and it is the natural home of the homotopy category of *Model Categories and Homotopy Theory*, of the derived categories and spectra of Part I and of the stable theory below.

The article develops the framework in the form in which it is used: **simplicial categories**, **complete Segal spaces**, and **quasi-categories** as three models of the same homotopy theory; the **homotopy category** and the **mapping spaces** of an $\infty$-category; limits and colimits, adjunctions and monoidal structures; and the **stable** case, in which the loops and suspension functors are inverse and the homotopy category is triangulated. It also introduces the **operadic** algebra of higher structures — $A_\infty$ and $E_n$ algebras and their modules — in the form needed for the recognition principle and for the multiplicative structures on algebraic $K$-theory.

The *algebraic* constructions are not the business of this article. Operads as algebraic objects, the theory of differential graded categories as a computational device, and the homological algebra of differential graded algebras are treated in the companion articles *Operads* and *Differential Graded Categories* of Part I; they are cited for the constructions, and what is supplied here is the homotopy-theoretic interpretation — the statement that a differential graded category presents an $\infty$-category, that an operad presents an $\infty$-operad, and that the algebraic invariants of Part I are the homotopy invariants of the present article. The triangulated structure of the stable homotopy category and the spectra that inhabit it are not covered here.

Throughout, $\infty$-category means $(\infty,1)$-category: all $k$-morphisms for $k \geq 2$ are invertible. The symbol $\Delta$ denotes the simplex category of *Model Categories and Homotopy Theory*, with $\Delta_n$ the standard simplex of *Simplicial and Singular Homology*.

## Simplicial Categories and Complete Segal Spaces

### Enriched Categories

**Definition.** Let $\mathcal{V}$ be a monoidal category with unit $I$. A **$\mathcal{V}$-enriched category** $\mathcal{C}$ consists of a class of objects, an object $\mathcal{C}(x,y) \in \mathcal{V}$ for each pair, a composition morphism $\mathcal{C}(y,z)\otimes\mathcal{C}(x,y) \to \mathcal{C}(x,z)$, and an identity morphism $I \to \mathcal{C}(x,x)$, subject to the associativity and unit diagrams in $\mathcal{V}$.

**Definition.** A **simplicial category** is a category enriched over the category $\mathbf{sSet}$ of simplicial sets with the cartesian monoidal structure. So for objects $x,y$ there is a simplicial set $\mathcal{C}(x,y)$, its $0$-simplices are the morphisms, its $1$-simplices are the homotopies between morphisms, its $2$-simplices the homotopies between homotopies, and composition is a map $\mathcal{C}(y,z)\times\mathcal{C}(x,y)\to\mathcal{C}(x,z)$.

**Definition.** A simplicial category is **locally Kan** if every mapping simplicial set $\mathcal{C}(x,y)$ is a Kan complex, in the sense of *Model Categories and Homotopy Theory*. It is **fibrant** if it is locally Kan. The **homotopy category** $\pi_0\mathcal{C}$ has the same objects and $\operatorname{Hom}_{\pi_0\mathcal{C}}(x,y) = \pi_0(\mathcal{C}(x,y))$, the set of components of the mapping space.

**Example.** A simplicial model category — a model category that is enriched over $\mathbf{sSet}$ compatibly with the model structure — has, between cofibrant-fibrant objects, mapping spaces that compute the homotopy category: $\pi_0\mathcal{C}(x,y) \cong \operatorname{Hom}_{\operatorname{Ho}(\mathcal{C})}(x,y)$. The topological spaces with the Quillen structure and the simplicial sets under geometric realisation are the standard examples, and the homotopy-coherent structure of the homotopy category is exactly what the simplicial enrichment records.

**Theorem (Bergner).** The category of simplicial categories has a model structure in which the weak equivalences are the **Dwyer–Kan equivalences** — the simplicial functors that are essentially surjective and induce weak homotopy equivalences on all mapping spaces — the fibrant objects are the locally Kan simplicial categories, and the homotopy category is the homotopy category of $\infty$-categories.

*Proof sketch.* The model structure is transferred along the adjunction with bisimplicial sets and the weak equivalences are characterised as above. $\square$

### Complete Segal Spaces

**Definition.** A **Segal space** is a simplicial space $X : \Delta^{\mathrm{op}} \to \mathbf{sSet}$, $[n]\mapsto X_n$, such that the **Segal maps**

$$
X_n \longrightarrow X_1 \times_{X_0} X_1 \times_{X_0} \cdots \times_{X_0} X_1 \qquad (n \text{ factors})
$$

are weak equivalences of simplicial sets for $n \geq 2$, the fibre products being taken over the face maps $X_1 \to X_0$. A **complete Segal space** is a Segal space such that the map $X_0 \to X_1^{\mathrm{eq}}$, from the objects to the space of equivalences, is a weak equivalence, where $X_1^{\mathrm{eq}} \subseteq X_1$ is the union of the components of $X_1$ whose images in $\pi_0$ are isomorphisms.

**Remark.** The Segal condition says that an $n$-simplex of the $\infty$-category is precisely a composable chain of $n$ morphisms together with the composites and their higher coherence; the completeness condition says that the only invertible $1$-morphisms between a given pair are the ones exhibiting an identity, which is what forces the objects to be recovered from the morphisms.

**Theorem (Rezk).** There is a model structure on bisimplicial sets whose fibrant objects are the complete Segal spaces, and whose homotopy category is equivalent to the homotopy category of simplicial categories and hence to the homotopy category of $\infty$-categories.

*Proof sketch.* The model structure is the **Rezk model structure**, in which the cofibrations are the monomorphisms and the weak equivalences are detected by the **complete Segal space** condition on a fibrant replacement; the equivalence with simplicial categories is a Quillen equivalence. $\square$

**Definition.** A **quasi-category** is a simplicial set in which every **inner horn** $\Lambda^n_k \hookrightarrow \Delta_n$, with $0 < k < n$, admits a filler; that is, the weak Kan condition holds. Its objects are the $0$-simplices, its morphisms the $1$-simplices, and its $n$-morphisms the $n$-simplices; composition is defined only up to coherent choice of fillers.

**Theorem (Joyal, Lurie).** The category of simplicial sets carries a model structure — the **Joyal model structure** — whose fibrant objects are the quasi-categories and whose weak equivalences are the **categorical equivalences**; its homotopy category is equivalent to the homotopy category of complete Segal spaces and to that of simplicial categories.

*Proof sketch.* The model structure is constructed by transfer from the Rezk structure using the equivalence between simplicial sets and bisimplicial sets that are constant in one direction; the identification of the fibrant objects with quasi-categories is the **Joyal extension theorem**, a horn-filling characterisation. $\square$

**Remark.** The three models — simplicial categories, complete Segal spaces, quasi-categories — present the same homotopy theory; the passage between them is an equivalence of $\infty$-categories, and in practice one chooses whichever makes the construction at hand easiest. The quasi-category model is the one usually taken as the definition, and the complete Segal model is the one that generalises most directly to $(\infty,n)$-categories, where the Segal condition is imposed iteratively in $n$ simplicial directions.

## The Homotopy Category and Mapping Spaces

### The Homotopy Category of a Quasi-Category

**Definition (homotopy relation).** Let $\mathcal{C}$ be a quasi-category and $f, g : \Delta_1 \to \mathcal{C}$ two morphisms with the same source and target. A **homotopy** from $f$ to $g$ is a map $\Delta_1\times\Delta_1 \to \mathcal{C}$ whose restriction to $\Delta_1 \times \{0\}$ is $f$, to $\Delta_1\times\{1\}$ is $g$, and whose restriction to $\{0\}\times\Delta_1$ and $\{1\}\times\Delta_1$ is the constant simplex at the source and target respectively. Homotopy is an equivalence relation, and the **homotopy category** $\operatorname{Ho}(\mathcal{C})$ has the objects of $\mathcal{C}$ and the homotopy classes of $1$-simplices as morphisms; composition is well defined by the inner horn filling condition.

**Theorem.** For a quasi-category $\mathcal{C}$, $\operatorname{Ho}(\mathcal{C})$ is a category; the construction is natural in $\mathcal{C}$, and for the quasi-category $\operatorname{Sing}(X)$ associated to a topological space $X$ it recovers the fundamental groupoid, $\operatorname{Ho}(\operatorname{Sing} X) \cong \Pi_1(X)$.

**Definition (mapping spaces).** For objects $x, y$ of a quasi-category $\mathcal{C}$ the **mapping space** $\operatorname{Map}_{\mathcal{C}}(x,y)$ is the simplicial set whose $n$-simplices are the maps $\Delta_{n+1} \to \mathcal{C}$ restricting to the constant simplex at $x$ on $\{0\}\times\Delta_n$ and at $y$ on $\{1\}\times\Delta_n$. It is a Kan complex, and $\pi_0\operatorname{Map}_{\mathcal{C}}(x,y) \cong \operatorname{Hom}_{\operatorname{Ho}(\mathcal{C})}(x,y)$.

**Example.** In the quasi-category of spaces, the mapping space $\operatorname{Map}(X,Y)$ has as its $0$-simplices the continuous maps and as its $1$-simplices the homotopies; $\pi_n \operatorname{Map}(X,Y) \cong \pi_n(Y^X)$ for the mapping space with the compact–open topology, so the simplicial mapping space refines the topological one into a homotopy-coherent object.

**Example.** In the quasi-category of chain complexes with the $\infty$-categorical localisation at quasi-isomorphisms, the mapping space between complexes $M$ and $N$ has homotopy groups $\pi_k\operatorname{Map}(M,N) \cong \operatorname{Ext}^{-k}_R(M,N)$, with the Ext groups of the planned *Ext and Tor* of Part I. This is the precise sense in which the higher structure is the derived structure: the derived Hom is a mapping space, not just a graded group.

### Limits, Colimits and Adjunctions

**Definition.** Let $\mathcal{C}$ be an $\infty$-category and $p : K \to \mathcal{C}$ a diagram, $K$ an $\infty$-category. A **limit** of $p$ is an object $\lim p$ together with a natural transformation exhibiting it as representing the functor $x \mapsto \operatorname{Map}_{\mathcal{C}^K}(\text{const}_x, p)$; a **colimit** is defined dually. Equivalently, in the quasi-category model, limits are terminal objects of the slice $\infty$-category $\mathcal{C}_{/p}$ and colimits initial objects of $\mathcal{C}_{p/}$.

**Definition.** An **adjunction** between $\infty$-categories is a pair of functors $F : \mathcal{C} \to \mathcal{D}$, $G : \mathcal{D}\to\mathcal{C}$ together with a **unit** transformation $\mathrm{id}_{\mathcal{C}} \to GF$ and a **counit** $FG \to \mathrm{id}_{\mathcal{D}}$ satisfying the triangle identities up to coherent homotopy; equivalently, a natural equivalence of mapping spaces $\operatorname{Map}_{\mathcal{D}}(F x, y) \simeq \operatorname{Map}_{\mathcal{C}}(x, Gy)$.

**Theorem.** An adjunction between $\infty$-categories induces an adjunction between the homotopy categories; conversely, an adjunction between homotopy categories lifts to the $\infty$-categories exactly when it is compatible with the mapping spaces, and the obstruction to the lift is a family of higher coherence data.

**Theorem (homotopy limits and colimits).** The homotopy limits and homotopy colimits of *Model Categories and Homotopy Theory* are the limits and colimits of the associated $\infty$-category. In particular a model category's homotopy category is the homotopy category of an $\infty$-category, and the $\infty$-categorical (co)limit is the homotopy-invariant one; ordinary (co)limits are recovered by taking diagrams that are already cofibrant-fibrant.

**Example.** The homotopy pullback of $X \to Z \leftarrow Y$ is the $\infty$-categorical pullback, computed by the homotopy fibre product; its homotopy groups fit in the **Mayer–Vietoris** sequence of *Simplicial and Singular Homology* when the diagram is a cover, and in the **Eilenberg–Moore** spectral sequence in general.

### Monoidal Structures

**Definition.** A **monoidal $\infty$-category** is a coCartesian fibration $\mathcal{C}^\otimes \to \Delta^{\mathrm{op}}$ satisfying the Segal conditions, whose fibre over $[1]$ is $\mathcal{C}$ and over $[0]$ a point; this packages the tensor product, its unit, associativity and the coherence data of the associator, unitors and higher coherences of Mac Lane. A **symmetric monoidal** structure replaces $\Delta^{\mathrm{op}}$ by the category $\mathbf{Fin}_*$ of finite pointed sets.

**Example.** The $\infty$-category of spectra with the smash product is symmetric monoidal; so is the $\infty$-category of chain complexes with the tensor product, and the $\infty$-category of spaces with the cartesian product. The homotopy category of a symmetric monoidal $\infty$-category is a symmetric monoidal category in the ordinary sense, but the converse fails: symmetric monoidal structures do not in general lift from homotopy categories, and the obstruction is the higher coherence.

**Remark.** The stable homotopy category is symmetric monoidal, and this is the structure in which the multiplication of the sphere spectrum lives; the language of symmetric monoidal $\infty$-categories is what makes the statement "the sphere spectrum is the unit" meaningful without a choice of model. The details are not covered here.

## Operadic Higher Algebra

### Operads and their Algebras

**Definition.** An **operad** $\mathcal{O}$ in a symmetric monoidal category $(\mathcal{V},\otimes,I)$ consists of objects $\mathcal{O}(n)$ for $n \geq 0$ with $\Sigma_n$-actions, an identity $I \to \mathcal{O}(1)$, and composition maps

$$
\mathcal{O}(k) \otimes \mathcal{O}(n_1)\otimes\cdots\otimes\mathcal{O}(n_k) \longrightarrow \mathcal{O}(n_1 + \cdots + n_k)
$$

satisfying the associativity, equivariance and unit axioms. The algebraic theory of operads, with the examples of the associative and commutative operads, is that of the companion article *Operads* of Part I, written in parallel; the present article uses its homotopy-theoretic refinement.

**Definition.** An **$\infty$-operad** is a coCartesian fibration $\mathcal{O}^\otimes \to \mathbf{Fin}_*$ satisfying the Segal-type conditions that encode composition up to coherent homotopy. An **algebra over** an $\infty$-operad $\mathcal{O}$ in a symmetric monoidal $\infty$-category $\mathcal{C}$ is a section of $\mathcal{O}^\otimes \to \mathbf{Fin}_*$ that is a morphism of coCartesian fibrations; the $\infty$-category of such algebras is written $\mathrm{Alg}_{\mathcal{O}}(\mathcal{C})$.

**Theorem (rectification).** Let $R$ be a commutative ring with $1 \neq 0$. The $\infty$-operad associated to a differential graded operad and the algebras over it in the $\infty$-category of chain complexes are equivalent to the differential graded algebras over the operad, computed by the projective model structure on chain complexes. In particular the $\infty$-categorical and the differential graded constructions present the same homotopy theory.

*Proof sketch.* The model structure on differential graded operads and on their algebras is transferred from the projective model structure on chain complexes, and the comparison with the $\infty$-operadic definition is a Quillen equivalence; the algebraic details are those of *Operads* and *Differential Graded Categories* of Part I. $\square$

**Example (the operads $A_\infty$ and $E_n$).** The **associative** $\infty$-operad $\mathrm{Ass}$ has $\mathrm{Ass}(n)$ a point with the trivial $\Sigma_n$-action; its algebras are the $A_\infty$-algebras, and in the stable setting they are the ring spectra. The **little $n$-discs** $\infty$-operad $E_n$ has as its $k$-th space the configuration space of $k$ disjoint discs in the unit disc of $\mathbb{R}^n$; $\mathrm{Alg}_{E_1}$ is the $\infty$-category of $A_\infty$-algebras, and $\mathrm{Alg}_{E_\infty}$ is the $\infty$-category of $E_\infty$-algebras, whose homotopy categories are the commutative monoids when the coefficient ring contains $\mathbb{Q}$.

**Theorem (May, recognition principle).** A pointed space $X$ is weakly equivalent to a loop space $\Omega^n Y$ for some $Y$ if and only if $X$ is grouplike with respect to an $E_n$-algebra structure; for $n = \infty$ the group-like $E_\infty$-spaces are the infinite loop spaces, and their spectra are the connective spectra. This is the recognition principle.

*Proof sketch.* The little discs operad acts on $\Omega^n Y$ by the "configuration of discs" multiplication, and conversely the action of $E_n$ on a grouplike space $X$ allows the construction of a classifying space $BX$ by a bar construction, using the operadic action to define a monad; iterating $n$ times yields $Y$ with $\Omega^n Y \simeq X$. $\square$

**Remark.** The recognition principle is the reason $\infty$-operads are needed in the stable theory: the multiplication on a loop space is not associative on the nose but only up to coherent homotopy, and the operadic structure is precisely the bookkeeping of that coherence. The classical form of the theory, with operads in topological spaces rather than in $\infty$-categories, is that of *Operads* in Part I.

### Modules over Algebras

**Definition.** Let $A$ be an algebra over an $\infty$-operad $\mathcal{O}$ in a symmetric monoidal $\infty$-category $\mathcal{C}$. A **left module** over $A$ is an algebra over the $\infty$-operad $\mathcal{O}\times\mathrm{LM}$ associated to the operad of a point and a left module, where $\mathrm{LM}(k) = \emptyset$ for $k$ not in $\{1,2\}$, $\mathrm{LM}(1)$ is a point, and $\mathrm{LM}(2)$ is a point with the trivial action; the $\infty$-category of left $A$-modules is written $\mathrm{LMod}_A(\mathcal{C})$. Right modules are defined analogously and bimodules as algebras over the two-coloured operad.

**Theorem (bar and cobar constructions).** For an $\infty$-operad $\mathcal{O}$, an $\mathcal{O}$-algebra $A$ in $\mathcal{C}$ and a left $A$-module $M$, there is a **bar construction** $B(A,M)$ and a **cobar construction** $\Omega(A,M)$ forming an adjunction between suitably connective modules and coalgebras; the adjunction is an equivalence in the range of a spectral sequence whose $E^2$ page is $\operatorname{Tor}$ of the associated graded.

*Proof sketch.* The construction is the two-sided simplicial bar resolution, whose geometric realisation computes the homotopy quotient; the spectral sequence is the one of *The Leray–Serre Spectral Sequence* applied to the resulting simplicial object. $\square$

**Example.** For a ring spectrum $R$ the $\infty$-category of $R$-modules is stable and symmetric monoidal, with a dualisable theory of perfect modules; this is the framework of **algebraic $K$-theory**, where the $K$-theory of $R$ is defined as the $K$-theory of the $\infty$-category of perfect $R$-modules.

## The Stable Case

### Stability

**Definition.** An $\infty$-category $\mathcal{C}$ with a zero object is **stable** if it is pointed and the loop functor $\Omega : \mathcal{C} \to \mathcal{C}$ and the suspension functor $\Sigma : \mathcal{C}\to\mathcal{C}$ are inverse equivalences.

**Theorem.** Let $\mathcal{C}$ be a stable $\infty$-category. Then:

1. $\operatorname{Ho}(\mathcal{C})$ is a triangulated category, with the triangles induced by the cofibre sequences; the shift is the suspension, and the octahedral axiom is a consequence of the $\infty$-categorical structure.
2. $\mathcal{C}$ is additive and every square that is a pushout is also a pullback; the fibre and cofibre sequences coincide.
3. The homotopy category is an abelian category if and only if $\mathcal{C}$ is equivalent to the derived category of an abelian category in a bounded range.

*Proof sketch.* The identification of pushouts and pullbacks in the stable setting follows from the invertibility of $\Sigma$ and $\Omega$; the triangulated structure is defined by the cofibre sequences and the octahedral axiom is verified from the higher coherence, which is the standard argument of Lurie's *Higher Algebra*. $\square$

**Example.** The stable homotopy category of spectra is the homotopy category of the stable $\infty$-category of spectra; the derived category of a ring is the homotopy category of the stable $\infty$-category of chain complexes localised at quasi-isomorphisms, whose trivially fibrant replacement is the **dg-nerve** of the differential graded category. The identification is the theorem relating the two constructions, and it is quoted from *Derived Categories* of Part I.

**Remark.** The triangulated structure is thus a *shadow* of the stable $\infty$-categorical structure: it remembers the triangles but forgets the coherence, and some constructions — the formation of the mapping cone in families, the tensor product of spectra, the multiplicative structure on $K$-theory — require the $\infty$-categorical structure and cannot be performed in a triangulated category alone.

### Spectra and the Sphere

**Definition.** A **spectrum** is a sequence of pointed spaces $E_n$ with structure maps $\Sigma E_n \to E_{n+1}$; its **homotopy groups** are $\pi_k(E) = \operatorname{colim}_n \pi_{k+n}(E_n)$. The **sphere spectrum** $\mathbb{S}$ has $E_n = S^n$ with the identity structure maps, and $\pi_k(\mathbb{S}) = \pi_k^s$ the stable stems.

**Theorem.** The $\infty$-category of spectra is stable, symmetric monoidal under the smash product $\wedge$ with unit $\mathbb{S}$, and the initial object is the zero object; the suspension spectrum functor $\Sigma^\infty : \mathcal{S} \to \mathrm{Sp}$ from spaces is left adjoint to the zero-space functor $\Omega^\infty$, and $\Omega^\infty\Sigma^\infty X$ is the group completion of $X$ as an $E_\infty$-space.

*Proof sketch.* Stability is the statement that $\Sigma$ is an equivalence on spectra, which holds because a spectrum is, by definition, a sequence of spaces in which the shifted structure maps are equivalences in the colimit; the symmetric monoidal structure is the smash product with unit $\mathbb{S}$, constructed on a suitable model. $\square$

**Example.** The **Eilenberg–MacLane spectrum** $H\pi$ for an abelian group $\pi$ has $\pi_0 \cong \pi$ and all other homotopy groups zero, and its associated infinite loop space is $K(\pi,0)$; the general $K(\pi,n)$ of *Classifying Spaces and Cohomology Operations*, is the $n$-fold delooping of $H\pi$ and corresponds to the spectrum $\Sigma^{-n}H\pi$. The representability of cohomology by spectra is not covered here.

## Summary

A higher category is a structure with objects, morphisms, and morphisms between morphisms at every level; an $\infty$-category or $(\infty,1)$-category has all $k$-morphisms for $k \geq 2$ invertible. Three equivalent models are developed: simplicial categories, with homotopy-coherent mapping spaces; complete Segal spaces, in which the Segal conditions encode composition and completeness encodes the objects; and quasi-categories, the weak Kan simplicial sets, whose homotopy category and mapping spaces generalise the homotopy category and the mapping space of topological spaces. Each model carries a model structure whose homotopy category is the homotopy category of $\infty$-categories, so the three present the same theory.

The homotopy category of an $\infty$-category has homotopy classes of morphisms as its morphisms, computed by inner horn filling, and the mapping spaces have homotopy groups that compute the higher Ext groups. Limits, colimits and adjunctions are defined by mapping-space conditions and are the homotopy-invariant versions of their ordinary counterparts, so the homotopy limits of a model category are the limits of its $\infty$-category. Monoidal $\infty$-categories and $\infty$-operads package tensor products and operadic composition with coherence; the associative and $E_n$ operads give $A_\infty$ and $E_n$ algebras, the rectification theorem identifies the $\infty$-categorical and differential graded constructions, and the recognition principle characterises the $n$-fold loop spaces as the grouplike $E_n$-spaces and the connective spectra as the grouplike $E_\infty$-spaces. A stable $\infty$-category is one in which loops and suspension are inverse; its homotopy category is triangulated, and the triangulated structure is the shadow of a structure that also keeps the coherence, which is why the tensor product of spectra and the multiplicative structure on $K$-theory require the higher setting.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\infty$-category | $(\infty,1)$-category; all $k$-morphisms for $k\geq2$ invertible |
| $\mathcal{C}(x,y)$ | Mapping space of a simplicial category or $\infty$-category |
| $\pi_0\mathcal{C}$, $\operatorname{Ho}(\mathcal{C})$ | Homotopy category |
| $\operatorname{Map}_{\mathcal{C}}(x,y)$ | Mapping space of a quasi-category; a Kan complex |
| $\Lambda^n_k$ | Inner horn ($0<k<n$); its fillers define a quasi-category |
| Segal space, complete Segal space | Simplicial space with the Segal and completeness conditions |
| Dwyer–Kan equivalence | Weak equivalence of simplicial categories |
| $\mathcal{C}^\otimes \to \mathbf{Fin}_*$ | Symmetric monoidal $\infty$-category as a coCartesian fibration |
| $\mathcal{O}^\otimes \to \mathbf{Fin}_*$, $\mathrm{Alg}_{\mathcal{O}}(\mathcal{C})$ | $\infty$-operad and its algebras |
| $\mathrm{Ass}$, $E_n$, $E_\infty$ | Associative and little discs operads; $A_\infty$ and $E_\infty$ algebras |
| $\mathrm{LMod}_A(\mathcal{C})$ | Left $A$-modules over an algebra in an $\infty$-operad |
| $B(A,M)$, $\Omega(A,M)$ | Bar and cobar constructions |
| Stable $\infty$-category | $\Omega$ and $\Sigma$ are inverse equivalences; $\operatorname{Ho}$ is triangulated |
| $\mathbb{S}$, $\pi_k^s$ | Sphere spectrum and stable stems |
| $H\pi$, $K(\pi,n)$ | Eilenberg–MacLane spectrum and space |
| $\Sigma$, $\Omega$, $\Sigma^\infty$, $\Omega^\infty$ | Suspension, loops, and their stabilisations |
| $\Delta$, $\Delta_n$ | Simplex category; standard $n$-simplex |





## Further Reading

- Jacob Lurie, *Higher Topos Theory* (Princeton University Press, 2009), for quasi-categories, mapping spaces and limits and colimits.
- Jacob Lurie, *Higher Algebra* (self-published, 2017), for $\infty$-operads, monoidal $\infty$-categories, stable $\infty$-categories and the bar construction.
- Charles Rezk, *A Model for the Homotopy Theory of Homotopy Theory* (Transactions of the American Mathematical Society 353, 2001), for complete Segal spaces.
- Julia E. Bergner, *A Survey of $(\infty,1)$-Categories* (in *Towards Higher Categories*, Springer, 2010), for the comparison of the models.
- André Joyal, *Quasi-Categories and Kan Complexes* (Journal of Pure and Applied Algebra 175, 2002), for the Joyal model structure and the homotopy category of a quasi-category.
- J. Peter May, *The Geometry of Iterated Loop Spaces* (Springer Lecture Notes in Mathematics 271, 1972), for the recognition principle and $E_n$-operads.
- Michael A. Mandell, *Cochain Multiplications* (in *Structured Ring Spectra*, Cambridge University Press, 2004), for the rectification of differential graded algebras to $E_\infty$-ring spectra.
- Mark Hovey, *Model Categories* (American Mathematical Society, 1999), for the model structures used in the comparison.
