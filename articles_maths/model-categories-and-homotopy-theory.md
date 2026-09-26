
# __Model Categories and Homotopy Theory__

## Introduction

The constructions of the preceding articles — homotopy of maps, homotopy equivalence, the homotopy extension property, the homotopy lifting property, the long exact sequence of a fibration — are not special to topological spaces. They make sense in any category in which one can say which maps are to be inverted, which maps allow a lift and which allow an extension; and the same formal arguments compute homotopy groups of simplicial sets, the derived functors of a module category, and the stable homotopy of spectra. A **model category** is the axiomatisation of exactly this structure: a bicomplete category with three classes of maps — **weak equivalences**, **cofibrations** and **fibrations** — subject to axioms that make the associated **homotopy category**, obtained by formally inverting the weak equivalences, as computable as the homotopy category of spaces.

The theory belongs to this Part because it is a theory of *deformation*: the axioms are statements about the existence of lifts and extensions of a homotopy, and every model category has an intrinsic notion of cylinder and path object that plays the role of $X \times I$ and of the path space of *Homotopy Groups and Fibrations*. It is homotopical algebra rather than homological algebra: the algebraic theory of derived categories, of resolutions and of $\operatorname{Ext}$ in an abelian category is the subject of Part I's *Derived Categories* and *Homological Algebra*, and is not developed here. What is developed here is the categorical framework, its homotopy category, the **Quillen functors** and their derived functors, and the standard examples: topological spaces, simplicial sets, chain complexes, and spectra. The last of these is the setting of the stable theory , and the framework is what makes "stable" a structural rather than a computational statement.

The two constructions of Part I on which article 10 builds — operads and differential graded categories — are cited there; the model-category framework of the present article is what allows them to be interpreted homotopically.

Throughout, $\mathcal{C}$ is a category with all small limits and colimits, called **bicomplete**, and $\operatorname{Ho}(\mathcal{C})$ denotes its homotopy category. The letters $\mathcal{W}$, $\mathcal{C}\mathrm{of}$ and $\mathcal{F}\mathrm{ib}$ denote the classes of weak equivalences, cofibrations and fibrations.

## The Axioms

### Model Structures

**Definition.** A **model structure** on a bicomplete category $\mathcal{C}$ is a choice of three classes of morphisms — weak equivalences $\mathcal{W}$, cofibrations $\mathcal{C}\mathrm{of}$, fibrations $\mathcal{F}\mathrm{ib}$ — such that:

1. **Two-out-of-three.** If $f$ and $g$ are composable and two of $f$, $g$, $gf$ are weak equivalences, so is the third; all identities are weak equivalences; and each class is closed under retracts.
2. **Lifting.** Cofibrations have the left lifting property with respect to acyclic fibrations (fibrations that are weak equivalences), and acyclic cofibrations have the left lifting property with respect to fibrations: given a commutative square with $i$ in the first class and $p$ in the second, a diagonal filler exists.
3. **Factorisation.** Every morphism admits two factorisations, one as an acyclic cofibration followed by a fibration, and one as a cofibration followed by an acyclic fibration.

A **model category** is a bicomplete category equipped with a model structure. The morphisms in $\mathcal{W} \cap \mathcal{C}\mathrm{of}$ are **acyclic cofibrations** and those in $\mathcal{W}\cap\mathcal{F}\mathrm{ib}$ are **acyclic fibrations**, also called trivial cofibrations and trivial fibrations.

**Definition.** An object $X$ is **cofibrant** if the unique map $\varnothing \to X$ is a cofibration, and **fibrant** if the unique map $X \to \ast$ is a fibration. A **cofibrant replacement** of $X$ is a weak equivalence $QX \to X$ with $QX$ cofibrant, and a **fibrant replacement** is a weak equivalence $X \to RX$ with $RX$ fibrant.

**Example (topological spaces).** On the category of compactly generated weak Hausdorff spaces with the Quillen model structure, the weak equivalences are the weak homotopy equivalences of *Homotopy Groups and Fibrations*, the fibrations are the Serre fibrations, the cofibrations are the retracts of relative cell complexes, and every object is fibrant. In the **Strøm model structure** on all topological spaces the weak equivalences are the genuine homotopy equivalences and the fibrations are the Hurewicz fibrations; here the two notions of homotopy equivalence coincide in the homotopy category, at the cost of a coarser notion of weak equivalence.

**Example (simplicial sets).** On the category $\mathbf{sSet}$ of simplicial sets, the **Quillen model structure** has as weak equivalences the maps whose geometric realisation is a weak homotopy equivalence, as cofibrations the monomorphisms, and as fibrations the **Kan fibrations**, characterised by the right lifting property against the horn inclusions $\Lambda^n_k \hookrightarrow \Delta_n$. The fibrant objects are the **Kan complexes**, and the homotopy category is equivalent to the homotopy category of CW complexes.

**Example (chain complexes).** On the category $\mathrm{Ch}_{\geq 0}(R)$ of nonnegatively graded chain complexes of $R$-modules, the **projective model structure** has as weak equivalences the quasi-isomorphisms, as fibrations the degreewise surjections, and as cofibrations the degreewise split injections with projective cokernel. The cofibrant objects are the complexes of projectives, and the homotopy category is the *derived category* $D_{\geq 0}(R)$ of Part I's *Derived Categories*, written in parallel; the identification of the two constructions is a theorem of that article and is quoted here.

**Example (spectra).** On a category of spectra there are model structures whose weak equivalences are the stable homotopy isomorphisms, that is, isomorphisms on all $\pi_k$ for $k \in \mathbb{Z}$; the homotopy category is the **stable homotopy category**. The construction requires a symmetric monoidal smash product, and the technical choices among the available models — sequential spectra, symmetric spectra, orthogonal spectra — do not change the homotopy category.

### The Small Object Argument

**Theorem (factorisation).** Let $\mathcal{I}$ be a set of morphisms of a bicomplete category $\mathcal{C}$ whose domains are small, in the sense that the representable functors commute with sufficiently long transfinite compositions. Then every morphism of $\mathcal{C}$ factors as a morphism in the class of transfinite composites of pushouts of elements of $\mathcal{I}$ followed by a morphism having the right lifting property with respect to $\mathcal{I}$.

*Proof sketch.* Given $f : X \to Y$, define a transfinite sequence $X = X_0 \to X_1 \to \cdots$ by pushing out, at each stage, over all commutative squares from elements of $\mathcal{I}$ into the current map, and take the colimit; smallness of the domains makes the colimit-detection work, and the resulting map $X_\infty \to Y$ has the right lifting property by construction, while $X \to X_\infty$ is a transfinite composite of pushouts. $\square$

**Corollary.** Every model category has functorial factorisations, and the classes $\mathcal{C}\mathrm{of}$ and $\mathcal{F}\mathrm{ib}$ are determined by each other through the lifting property and the factorisation axiom.

**Remark.** The small object argument is the technical heart of the theory and the reason the axioms are stated with a generating set of cofibrations; it is what produces the cofibrant replacements needed to define the homotopy category.

## The Homotopy Category

### Localisation

**Definition.** The **homotopy category** $\operatorname{Ho}(\mathcal{C})$ of a model category $\mathcal{C}$ is the localisation $\mathcal{C}[\mathcal{W}^{-1}]$: the category obtained from $\mathcal{C}$ by adjoining formal inverses to all weak equivalences.

**Theorem (existence).** The localisation $\mathcal{C}[\mathcal{W}^{-1}]$ exists and has the same objects as $\mathcal{C}$; its morphisms are computed by

$$
\operatorname{Hom}_{\operatorname{Ho}(\mathcal{C})}(X,Y) \cong \pi\bigl(\operatorname{Hom}_{\mathcal{C}}(QX, RY)\bigr),
$$

the homotopy classes of morphisms between a cofibrant replacement of $X$ and a fibrant replacement of $Y$, where the homotopy relation is defined through cylinder and path objects.

*Proof sketch.* Cofibrant and fibrant replacements exist by the factorisation axiom, weak equivalences between cofibrant (or fibrant) objects are the homotopy equivalences of a cylinder-object deformation, and the quotient of $\operatorname{Hom}_{\mathcal{C}}(QX,RY)$ by this relation is a category in which weak equivalences become isomorphisms; the universal property of the localisation shows it is $\operatorname{Ho}(\mathcal{C})$. $\square$

**Definition.** Two morphisms $f, g : X \to Y$ between cofibrant-fibrant objects are **left homotopic** if they factor through a **cylinder object** $X \sqcup X \to \mathrm{Cyl}(X) \xrightarrow{\sim} X$ and **right homotopic** if they factor through a **path object** $Y \to \mathrm{Path}(Y) \xrightarrow{\sim} Y\times Y$; for cofibrant-fibrant objects the two relations coincide and are an equivalence relation.

**Example.** In topological spaces with the Quillen structure, a cylinder object of a CW complex $X$ is $X \times I$ and a path object is the space of paths $I \to X$; the homotopy category is the homotopy category of CW complexes, so $\operatorname{Ho}(\mathbf{Top}) \simeq \operatorname{Ho}(\mathbf{sSet})$, and both are equivalent to the category of CW complexes and homotopy classes of maps.

**Remark.** The homotopy relation on maps of a model category is the exact generalisation of homotopy of continuous maps of *The Fundamental Group and Covering Spaces*: cylinder object for $X \times I$, path object for the space of paths, cofibration for a pair with the HEP, fibration for a map with the HLP. The translation is:
- HEP $\leftrightarrow$ cofibration;
- HLP $\leftrightarrow$ fibration;
- deformation retract $\leftrightarrow$ acyclic cofibration with a section.

### Homotopy (Co)limits

**Definition.** Let $F : \mathcal{I} \to \mathcal{C}$ be a diagram in a model category. The **homotopy colimit** and **homotopy limit** are the total left and right derived functors of the colimit and limit functors; concretely, $\operatorname{hocolim} F$ is computed by cofibrantly replacing the diagram in the projective model structure on $\mathcal{C}^{\mathcal{I}}$ and then taking the colimit, and $\operatorname{holim} F$ by fibrant replacement and limit.

**Example.** The homotopy colimit of the diagram $X \xleftarrow{f} Z \xrightarrow{g} Y$ is the **double mapping cylinder** of $f$ and $g$, and its homology fits in the **Mayer–Vietoris sequence** of *Simplicial and Singular Homology* even when $f$ and $g$ are not cofibrations. The homotopy limit of the same diagram is the **homotopy fibre product**, and it appears in the Eilenberg–Moore and Bousfield–Kan spectral sequences.

**Theorem (homotopy invariance).** A weak equivalence of diagrams induces a weak equivalence of homotopy colimits and of homotopy limits, whereas the ordinary colimit and limit are not homotopy invariant.

*Proof.* Derived functors of a Quillen functor preserve weak equivalences between cofibrant (respectively fibrant) objects by Ken Brown's lemma, and the replacement makes the diagram cofibrant (respectively fibrant). $\square$

## Quillen Functors and Derived Functors

### Adjunctions

**Definition.** Let $\mathcal{C}$ and $\mathcal{D}$ be model categories. An adjunction $F \dashv G$ with $F : \mathcal{C} \to \mathcal{D}$ the left adjoint is a **Quillen adjunction** if $F$ preserves cofibrations and acyclic cofibrations, equivalently if $G$ preserves fibrations and acyclic fibrations. In that case $F$ and $G$ are **left** and **right Quillen functors**.

**Theorem (Ken Brown's lemma).** If $F$ is left Quillen then $F$ preserves weak equivalences between cofibrant objects; if $G$ is right Quillen it preserves weak equivalences between fibrant objects.

*Proof.* A weak equivalence between cofibrant objects factors as an acyclic cofibration with a retraction, and $F$ preserves acyclic cofibrations and retracts; the details are the standard factorisation argument. $\square$

**Definition (total derived functors).** For a Quillen adjunction $F \dashv G$, the **total left derived functor** $\mathbb{L}F : \operatorname{Ho}(\mathcal{C}) \to \operatorname{Ho}(\mathcal{D})$ is defined on objects by $\mathbb{L}F(X) = F(QX)$ and the **total right derived functor** $\mathbb{R}G(Y) = G(RY)$; by Ken Brown's lemma these are well defined and the adjunction descends to an adjunction $\mathbb{L}F \dashv \mathbb{R}G$ between the homotopy categories.

**Corollary (the general shape of a derived functor).** The construction specialises to the derived functors of homological algebra: on chain complexes with the projective model structure, the total left derived functor of $-\otimes_R M$ is $\operatorname{Tor}_*^R(-,M)$ and the total right derived functor of $\operatorname{Hom}_R(-,N)$ is $\operatorname{Ext}^*_R(-,N)$, the functors of the planned *Ext and Tor* of Part I. The model-category framework thus accounts for the existence and the universal property of the derived functors that the algebraic articles construct by resolutions.

**Remark.** This is the point at which the homotopical algebra of the present article and the homological algebra of Part I meet: the resolutions of Part I are the cofibrant replacements of the projective model structure, the long exact sequences are the long exact sequences of a cofibre sequence, and the derived category is the homotopy category. The details are the subject of *Derived Categories*, written in parallel.

### Simplicial Sets

**Definition.** The category $\Delta$ has as objects the finite nonempty ordered sets $[n] = \{0 < 1 < \cdots < n\}$ and as morphisms the order-preserving maps. A **simplicial set** is a functor $\Delta^{\mathrm{op}} \to \mathbf{Set}$; a **simplicial object** in a category $\mathcal{C}$ is a functor $\Delta^{\mathrm{op}}\to\mathcal{C}$. The value on $[n]$ is the set of $n$-simplices, the face maps $\partial_i$ are induced by the injections omitting $i$, and the degeneracies $s_i$ by the surjections repeating $i$.

**Theorem (geometric realisation).** There is a Quillen adjunction $|\!-\!| \dashv \operatorname{Sing}$ between simplicial sets with the Quillen model structure and topological spaces with the Quillen model structure, where $|\Delta_n|$ is the standard simplex of *Simplicial and Singular Homology* and $\operatorname{Sing}(X)_n = \operatorname{Hom}_{\mathbf{Top}}(\Delta_n, X)$. The derived functors give equivalences of homotopy categories

$$
\operatorname{Ho}(\mathbf{sSet}) \simeq \operatorname{Ho}(\mathbf{Top}),
$$

and $\operatorname{Sing}$ carries the CW complexes to the Kan complexes.

**Theorem (Dold–Kan correspondence).** For a commutative ring $R$ with $1 \neq 0$, there is an equivalence of categories between simplicial $R$-modules and nonnegatively graded chain complexes of $R$-modules, under which the homotopy groups of a simplicial module correspond to the homology of the associated complex, and the **normalised** chain complex is obtained by quotienting by the degenerate simplices.

*Proof sketch.* The functor sends a simplicial module $M_\bullet$ to the complex with $C_n = M_n / (\text{degenerate } n\text{-simplices})$ and boundary $\sum_i (-1)^i \partial_i$; the inverse is the "Dold–Kan" functor and the two are quasi-inverse. $\square$

**Corollary.** The homotopy groups of a simplicial abelian group agree with the homology of its normalised chain complex, and the singular chains of *Simplicial and Singular Homology* are the normalised chains of the simplicial module $\operatorname{Sing}(X) \otimes R$. This identifies the singular complex with a simplicial object and is the entry point of the simplicial methods in the sheaf theory of articles 16–21.

## Localisations, Monoidal Structure and Comparison

### Bousfield Localisation

**Definition.** Let $\mathcal{C}$ be a model category and $S$ a set of morphisms of $\mathcal{C}$. The **left Bousfield localisation** $L_S\mathcal{C}$, if it exists, is the model structure on $\mathcal{C}$ with the same cofibrations as $\mathcal{C}$ and with weak equivalences the **$S$-local equivalences**: the morphisms $f$ such that $f^* : \operatorname{Map}(Y,Z)\to\operatorname{Map}(X,Z)$ is a weak equivalence of simplicial sets for every $S$-local object $Z$, an object being $S$-local when $\operatorname{Map}(s,Z)$ is a weak equivalence for all $s\in S$. The fibrant objects of $L_S\mathcal{C}$ are the $S$-local objects, and the identity is a left Quillen functor $\mathcal{C}\to L_S\mathcal{C}$ whose total left derived functor is the localisation of the homotopy category at the images of the maps in $S$.

**Theorem (existence of localisations).** Let $\mathcal{C}$ be a left proper, combinatorial model category and $S$ a set of morphisms. Then the left Bousfield localisation $L_S\mathcal{C}$ exists and is again combinatorial and left proper, and it is the universal model category under $\mathcal{C}$ in which the morphisms of $S$ become weak equivalences. This is Smith's theorem, and it is the technical device by which the stable homotopy category of spectra, constructed as a localisation of the category of spectra with the levelwise structure, is obtained from a simpler model structure; the construction and the resulting stable homotopy category are not covered here.

**Example (localisations at a set of primes and at the rationals).** Localising the model category of spaces at the maps $S^{n+1}\to S^{n+1}$ of degree $p$ for a prime $p$ makes the $p$-local spheres into the local objects, and the resulting homotopy category is that of $p$-local spaces; localising at the maps of degree $m$ for all $m\neq0$ gives the rational homotopy category, in which the homotopy groups are rational vector spaces and the algebraic models of Quillen and Sullivan apply. In each case the localisation exists by the theorem, and the localised category is where the corresponding invariant lives.

### Monoidal and Enriched Structure

**Definition.** A **monoidal model category** is a model category with a symmetric monoidal structure, a unit, and the **pushout-product axiom**: for a cofibration $i$ and a cofibration $j$ the induced map $i\square j$ on the pushout-product is a cofibration, acyclic if either $i$ or $j$ is. A **simplicial model category** is a model category enriched over simplicial sets with a compatible action, so that the mapping objects $\operatorname{Map}(X,Y)$ are simplicial sets and the axioms of Quillen's homotopical algebra hold.

**Theorem.** Let $\mathcal{C}$ be a monoidal model category.

1. The homotopy category $\operatorname{Ho}(\mathcal{C})$ inherits a symmetric monoidal structure, and the monoids and the modules over a monoid may be defined homotopically: a **monoid** is a monoid object in $\operatorname{Ho}(\mathcal{C})$ together with a multiplication that is associative up to coherent homotopy, and the resulting homotopy theory of monoids and their modules is the homotopical algebra of the structures of Part I's *Algebras* and *Differential Graded Algebras*, carried out at the level of homotopy.
2. If $\mathcal{C}$ is simplicial, then for cofibrant $X$ and fibrant $Y$ the simplicial set $\operatorname{Map}(X,Y)$ has homotopy groups computing the homotopy classes of maps and the higher homotopies, and $\pi_0\operatorname{Map}(X,Y)$ is the morphism set of the homotopy category.
3. In a simplicial model category one may form the **simplicial localisation** of Dwyer and Kan, an $\infty$-category whose homotopy category is $\operatorname{Ho}(\mathcal{C})$ and whose mapping spaces are the $\operatorname{Map}(X,Y)$; this construction is the bridge to the higher-categorical formulation, and Quillen-equivalent model categories present equivalent $\infty$-categories, so the homotopy theory is an invariant of the underlying homotopy theory rather than of the chosen model structure.

*Pro.* (1) the pushout-product axiom makes the tensor product of cofibrant objects homotopy invariant and the derived tensor product well defined on the homotopy category, and the coherence of the associativity is the content of the monoidal structure on the homotopy category; the higher coherence for monoids requires the simplicial or $\infty$-categorical enrichment. (2) is Quillen's axiom SM7 and its consequences, computing the homotopy classes of maps as $\pi_0$ of the function complex. (3) is the Dwyer–Kan simplicial localisation; the proof of the invariance is the theorem that the simplicial localisation depends only on the homotopy theory, quoted as standard and expounded. $\square$

**Remark (the two languages).** A model category is a strict presentation of a homotopy theory: it names the cofibrations and the fibrations, it makes the constructions of homotopy limits and derived functors available by explicit replacements, and it is the setting in which the classical computations of the subject are performed. An $\infty$-category is the intrinsic object: it retains only the homotopy theory and has the mapping spaces as its primary data, so it is well suited to the multiplicative and higher-structural statements for which a model-categorical presentation would require an elaborate coherence machine. The two are not rivals; a Quillen adjunction is presented by a pair of adjoint functors, an $\infty$-categorical adjunction by a coherent datum, and every model category presents an $\infty$-category whose theory is independent of the presentation. The present article uses the model-categorical language, other articles the higher-categorical one, and the bridge is the simplicial localisation of the theorem above.

## Summary

A model category is a bicomplete category with three classes of morphisms — weak equivalences, cofibrations and fibrations — satisfying two-out-of-three, lifting, and factorisation. Cofibrant and fibrant objects and their replacements are defined from the factorisations, and the small object argument manufactures them. The homotopy category is the localisation at the weak equivalences, and its morphisms are computed as homotopy classes of maps between replacements; cylinder and path objects generalise $X\times I$ and the path space, so cofibrations generalise maps with the homotopy extension property and fibrations generalise maps with the homotopy lifting property.

Homotopy colimits and limits are the derived functors of colimit and limit; they are homotopy invariant, unlike their ordinary counterparts, and the double mapping cylinder and homotopy fibre product are the basic examples. A Quillen adjunction is an adjunction whose left adjoint preserves cofibrations and acyclic cofibrations; Ken Brown's lemma makes the total derived functors well defined, and on chain complexes with the projective model structure the total derived functors are $\operatorname{Tor}$ and $\operatorname{Ext}$, which is how the framework accounts for the derived functors of Part I. The standard examples are topological spaces with the Quillen and Strøm structures, simplicial sets with the Quillen structure and the Kan complexes as fibrant objects, chain complexes with the projective structure, and spectra with the stable structure; the Dold–Kan correspondence identifies simplicial modules with nonnegatively graded chain complexes, and geometric realisation gives an equivalence between the homotopy categories of simplicial sets and of spaces. Localisation at a set of morphisms, when it exists by Smith's theorem, is the device that produces the $p$-local, the rational and the stable homotopy categories from the levelwise ones, and the monoidal and simplicial enrichments make the tensor product, the function complexes and the monoids homotopy invariant. A simplicial model category presents an $\infty$-category by the simplicial localisation of Dwyer and Kan, and Quillen-equivalent model categories present equivalent $\infty$-categories; another article develops that intrinsic language.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{C}$, $\mathcal{D}$ | Bicomplete categories with model structures |
| $\mathcal{W}$, $\mathcal{C}\mathrm{of}$, $\mathcal{F}\mathrm{ib}$ | Weak equivalences, cofibrations, fibrations |
| Acyclic (trivial) | In $\mathcal{W}\cap\mathcal{C}\mathrm{of}$ or $\mathcal{W}\cap\mathcal{F}\mathrm{ib}$ |
| $QX$, $RX$ | Cofibrant and fibrant replacements of $X$ |
| $\operatorname{Cyl}(X)$, $\mathrm{Path}(Y)$ | Cylinder and path objects; homotopy of morphisms |
| $\operatorname{Ho}(\mathcal{C}) = \mathcal{C}[\mathcal{W}^{-1}]$ | Homotopy category; morphisms $\pi\operatorname{Hom}(QX,RY)$ |
| $\operatorname{hocolim}$, $\operatorname{holim}$ | Homotopy colimit and limit; derived functors of colim and lim |
| $\mathbb{L}F$, $\mathbb{R}G$ | Total left and right derived functors of a Quillen adjunction |
| $\Delta$, $\mathbf{sSet}$, $\operatorname{Sing}$, $|\!-\!|$ | Simplex category, simplicial sets, singular functor, geometric realisation |
| $\Lambda^n_k$ | Simplicial horn; Kan fibration has the RLP against its inclusion |
| $\mathrm{Ch}_{\geq 0}(R)$ | Nonnegatively graded chain complexes; projective model structure |
| Dold–Kan | Equivalence simplicial $R$-modules $\leftrightarrow$ chain complexes |
| $L_S\mathcal{C}$ | Left Bousfield localisation at a set of morphisms $S$ |
| $\operatorname{Map}(X,Y)$ | Function complex in a simplicial model category; $\pi_0\operatorname{Map}(X,Y) = \operatorname{Ho}(\mathcal{C})(X,Y)$ |
| Pushout-product $i\square j$ | Axiom making the monoidal structure homotopy invariant |
| Dwyer–Kan localisation | Simplicial localisation presenting an $\infty$-category |
| $R$ | Commutative ring with identity $1 \neq 0$ |









## Further Reading

- Daniel G. Quillen, *Homotopical Algebra* (Springer Lecture Notes in Mathematics 43, 1967), for the original axioms and the homotopy category.
- William G. Dwyer and J. Spaliński, *Homotopy Theories and Model Categories* (Handbook of Algebraic Topology, 1995), for a modern exposition of the axioms and the small object argument.
- Mark Hovey, *Model Categories* (American Mathematical Society, 1999), for the factorisations, the homotopy category and the examples.
- Philip S. Hirschhorn, *Model Categories and Their Localizations* (American Mathematical Society, 2003), for homotopy limits and colimits and localisations of model structures.
- Paul G. Goerss and John F. Jardine, *Simplicial Homotopy Theory* (Birkhäuser, 1999), for simplicial sets, Kan fibrations and the Dold–Kan correspondence.
- Michael A. Mandell, J. Peter May, Stefan Schwede and Brooke Shipley, *Model Categories of Diagram Spectra* (Proceedings of the London Mathematical Society 82, 2001), for the symmetric monoidal model structure on spectra.
- Charles A. Weibel, *An Introduction to Homological Algebra* (Cambridge University Press, 1994), for the classical derived functors that the model-category framework recovers.
