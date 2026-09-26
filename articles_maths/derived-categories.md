
# __Derived Categories__

## Introduction

The derived functors of a functor that is not exact are computed by a choice of resolution, and the comparison theorem says the choice does not matter: any two resolutions are linked by a chain map unique up to homotopy. The derived category turns this statement into structure. It adjoins to the complexes of an abelian category formal inverses for the quasi-isomorphisms, retaining the homotopy category as its place of computation, and in the derived category the exact functors are precisely those that were merely left or right exact before: $\operatorname{Hom}$ becomes $\operatorname{Hom}$ in the derived category, the tensor product becomes the derived tensor product, and a short exact sequence produces the distinguished triangles that carry the long exact sequences. The construction does not create new homological data; it repackages the data of resolutions, derived functors and spectral sequences into a single additive category in which the triangle replaces the exact sequence.

This article develops the homotopy category of complexes, the localisation of a category at a class of morphisms, the derived category of an abelian category, the structure of triangulated categories and the distinguished triangles, the identification of derived functors with functors on the derived category, the derived functors $\operatorname{RHom}$ and $\otimes^{\mathbb{L}}$, and the equivalences of derived categories that occur for rings of finite global dimension. It follows *Derived Functors*, *Ext and Tor* and *Spectral Sequences*, and it prepares.

Throughout, $\mathcal{A}$ is an abelian category, most often $R\text{-}\mathbf{Mod}$ for a commutative ring $R$ with $1\neq0$, and $D(\mathcal{A})$ is its derived category; $K(\mathcal{A})$ is the homotopy category. The article assumes the complexes, chain homotopies, mapping cones, resolutions and hom complexes of *Homological Algebra*, the derived functors of *Derived Functors*, and the Ext and Tor families of *Ext and Tor*. No topology and no form occurs; the words *localisation*, *limit* and *complete* are used in their algebraic senses. The derived categories of sheaves on a site and the six-functor formalism for a map of schemes belong to Part II, where they are treated in *Sheaves and Cohomology*; the triangulated and higher-categorical machinery that surrounds the theory borders andboth being written in this same batch, and this article keeps to the algebraic side and cites those companions.

## The Homotopy Category

### Complexes up to Homotopy

**Definition.** The **homotopy category** $K(\mathcal{A})$ has as objects the chain complexes of $\mathcal{A}$, and as morphisms the homotopy classes of chain maps:

$$
K(\mathcal{A})(C_\bullet,D_\bullet)=H^0\bigl(\operatorname{Hom}^\bullet(C_\bullet,D_\bullet)\bigr).
$$

Composition is induced by composition of chain maps, which descends to homotopy classes by the additivity of the hom functor.

**Proposition.** $K(\mathcal{A})$ is an additive category with biproducts, and the canonical functor $\mathbf{Ch}(\mathcal{A})\to K(\mathcal{A})$ is additive and the identity on objects. Homotopic maps become equal, so every null-homotopic complex is isomorphic to zero in $K(\mathcal{A})$.

*Proof.* The hom functor $\operatorname{Hom}^\bullet$ is a complex of abelian groups whose $H^0$ is chain maps modulo homotopy; composition is compatible with the differential and descends. Direct sums and their structure maps are those of $\mathbf{Ch}(\mathcal{A})$, and the homotopy relation is additive, so they descend. A complex with a contracting homotopy has the identity homotopic to zero, hence the identity is zero in $K(\mathcal{A})$ and the object is zero. $\square$

**Definition.** The full subcategories $K^+(\mathcal{A})$, $K^-(\mathcal{A})$ and $K^b(\mathcal{A})$ consist of the complexes bounded below, bounded above and bounded on both sides.

**Example.** Over a ring $R$, the complex $0\to R\xrightarrow{\operatorname{id}}R\to0$ is null-homotopic and therefore zero in $K(R\text{-}\mathbf{Mod})$, although it is not the zero complex. This is the essential difference between $\mathbf{Ch}$ and $K$: the homotopy category does not see contractible complexes.

### Shift and Mapping Cone

**Definition.** The **shift** of a complex $C_\bullet$ by $n$ is the complex $C[n]_\bullet$ with $C[n]_k=C_{k+n}$ and differential $(-1)^nd$; a chain map $f:C\to D$ of degree $p$ is a morphism $C\to D[p]$ in the homotopy category.

**Proposition.** The mapping cone of a chain map $f:C\to D$ fits into a diagram

$$
C\xrightarrow{\ f\ }D\xrightarrow{\ i\ }\operatorname{Cone}(f)\xrightarrow{\ q\ }C[1],
$$

in which $i$ is the inclusion of $D$ as the degree-$0$ component of the cone and $q$ is the projection onto $C[1]$; the composite of any two consecutive maps is zero, and the induced maps on homology form the long exact sequence of *Homological Algebra*.

*Proof.* The maps are $i(d)=(d,0)$ and $q(c,d)=-c$, the sign being chosen with the cone's differential of *Homological Algebra* so that $q\,i=0$ and $i\,f=0$. The homology statement is the long exact sequence of the cone. $\square$

## Localisation

### The Universal Property

**Definition.** Let $\mathcal{C}$ be a category and $\Sigma$ a class of morphisms. A **localisation** of $\mathcal{C}$ at $\Sigma$ is a category $\mathcal{C}[\Sigma^{-1}]$ together with a functor $Q:\mathcal{C}\to\mathcal{C}[\Sigma^{-1}]$ that sends every morphism of $\Sigma$ to an isomorphism and is universal with this property: every functor $F:\mathcal{C}\to\mathcal{D}$ carrying $\Sigma$ to isomorphisms factors uniquely through $Q$, up to natural isomorphism.

**Proposition.** The localisation, when it exists, is unique up to equivalence of categories. It exists whenever the class $\Sigma$ admits a calculus of fractions; in that case the morphisms of $\mathcal{C}[\Sigma^{-1}]$ are represented by **roofs** $A\xleftarrow{s}B\xrightarrow{f}C$ with $s\in\Sigma$, two roofs being identified when they are linked by a commutative diagram of roofs.

*Proof.* Uniqueness is the universal property applied to the identity functor. For the calculus of fractions one imposes that $\Sigma$ be closed under composition and contain the identities, and the two conditions that every diagram with one arrow in $\Sigma$ can be completed to a commuting square with the other arrow in $\Sigma$, in both orientations; then the roofs compose and the identification relation is an equivalence, giving a category with the universal property. $\square$

**Example.** The localisation of a commutative ring at a multiplicative set, which is the article *Localization and Completion of Modules*, is the special case of the construction for the category with one object whose endomorphisms are the ring: the localised ring is the localisation of that one-object category at the multiplicative set, and its universal property is the same statement. The same construction applies to modules over the ring.

### Localising the Homotopy Category

**Definition.** A **quasi-isomorphism** is a chain map inducing isomorphisms on all homology groups. The **derived category** $D(\mathcal{A})$ is the localisation of the homotopy category at the class of quasi-isomorphisms:

$$
D(\mathcal{A})=K(\mathcal{A})[\mathrm{qis}^{-1}].
$$

The bounded versions $D^+(\mathcal{A})$, $D^-(\mathcal{A})$ and $D^b(\mathcal{A})$ are the localisations of $K^+$, $K^-$ and $K^b$ at the quasi-isomorphisms between their objects.

**Theorem.** The localisation $D(\mathcal{A})=K(\mathcal{A})[\mathrm{qis}^{-1}]$ exists, and the objects whose cohomology is bounded, bounded above or bounded below form full subcategories closed under the construction, so that the localisations of $K^b$, $K^-$ and $K^+$ at their quasi-isomorphisms are these subcategories. Moreover, when $\mathcal{A}$ has enough injectives the class of quasi-isomorphisms between complexes of injectives admits a calculus of fractions, so that every morphism of $D(\mathcal{A})$ is represented by a roof $A\xleftarrow{s}B\xrightarrow{f}C$ of chain maps with $s$ a quasi-isomorphism; dually when $\mathcal{A}$ has enough projectives.

*Proof (in outline).* The localisation exists by the general construction of a category of fractions of Gabriel and Zisman, in which the morphisms are formal zigzags and the class of quasi-isomorphisms is saturated. The technical heart of the calculability is the replacement of an arbitrary complex by a complex of projectives or injectives without changing its quasi-isomorphism type: if every object of $\mathcal{A}$ embeds in an injective, then every complex admits a quasi-isomorphism into a complex of injectives, and between complexes of injectives every quasi-isomorphism is a homotopy equivalence, which makes the roofs composable and the Ore conditions verifiable. In general the morphisms of $D(\mathcal{A})$ are represented by three-arrow zigzags rather than by roofs, and the bounded subcategories are handled by the same replacements truncated at the ends. Dually with projectives. $\square$

**Proposition.** The canonical functor $K(\mathcal{A})\to D(\mathcal{A})$ is the identity on objects and is additive. A chain map becomes an isomorphism in $D(\mathcal{A})$ if and only if it is a quasi-isomorphism; a complex becomes isomorphic to zero in $D(\mathcal{A})$ if and only if it is acyclic.

*Proof.* The first statement is the definition of the localisation. For the second, the localisation inverts exactly the quasi-isomorphisms by construction, and a complex is acyclic exactly when the map from it to the zero complex is a quasi-isomorphism. $\square$

**Example.** In $D(R\text{-}\mathbf{Mod})$ the acyclic complex $0\to R\xrightarrow{\operatorname{id}}R\to0$ is zero, and a module $M$ placed in degree $0$ is isomorphic to any resolution of $M$: the resolution is exact except in degree $0$ with homology $M$, and the augmentation is a quasi-isomorphism. Hence a module and its projective resolution are the same object of the derived category, which is the sense in which resolutions compute derived functors.

## Triangulated Categories

### The Axioms

**Definition.** A **triangulated category** is an additive category $\mathcal{T}$ equipped with an equivalence $T$, the **translation** or shift, and a class of **distinguished triangles** $X\to Y\to Z\to TX$, called exact triangles, subject to the following axioms.

(i) The class is closed under isomorphism of triangles, and for every morphism $f:X\to Y$ there is a distinguished triangle $X\xrightarrow{f}Y\to Z\to TX$; a triangle of this form is an exact triangle on $f$.

(ii) The triangle $X\xrightarrow{\operatorname{id}}X\to0\to TX$ is distinguished.

(iii) A triangle $X\to Y\to Z\to TX$ is distinguished if and only if the rotated triangles $Y\to Z\to TX\to TY$ and $T^{-1}Z\to X\to Y\to Z$ are distinguished.

(iv) Given distinguished triangles on $f:X\to Y$, on $g:Y\to Z$ and on $gf:X\to Z$, together with morphisms of the first two triangles compatible with $f$ and $g$, the three triangles fit into the **octahedron** of the definition below.

**Definition (octahedral axiom).** The four objects $X,Y,Z$ and the three cones $Z'=\operatorname{Cone}(f)$, $X'=\operatorname{Cone}(g)$, $Y'=\operatorname{Cone}(gf)$ are the vertices of an octahedron whose faces are the four distinguished triangles on $f$, $g$, $gf$ and on the induced map $Z'\to Y'$; the axiom asserts that the induced maps can be chosen so that all faces commute, that the triangle $Z'\to Y'\to X'\to TZ'$ is distinguished, and that the two composites $X'\to TZ'\to TY$ and $X'\to TY'\to TY$ agree up to the sign forced by the translation.

**Theorem.** The derived category $D(\mathcal{A})$ is triangulated with translation $C\mapsto C[1]$ and distinguished triangles the images of the cone diagrams $C\to D\to\operatorname{Cone}(f)\to C[1]$ of the homotopy category.

*Proof.* Distinguished triangles are defined by the cone construction of *Homological Algebra*, and the axioms are verified using the explicit mapping-cylinder models of the maps, which exist because the localisation can be computed with complexes of injectives or projectives. The octahedral axiom follows from the construction of the mapping cone of a composition. $\square$

**Definition.** A functor between triangulated categories is **exact** if it is additive, commutes with the translation up to natural isomorphism, and carries distinguished triangles to distinguished triangles.

**Definition.** A functor $H:\mathcal{T}\to\mathbf{Ab}$ from a triangulated category to abelian groups is **cohomological** if it carries every distinguished triangle $X\to Y\to Z\to TX$ to an exact sequence $H(X)\to H(Y)\to H(Z)$.

**Theorem.** For a cohomological functor $H$ and a distinguished triangle $X\to Y\to Z\to TX$, the rotated triangles give a long exact sequence

$$
\cdots\to H(T^nX)\to H(T^nY)\to H(T^nZ)\to H(T^{n+1}X)\to\cdots,
$$

and an exact functor between triangulated categories carries distinguished triangles to distinguished triangles, so it preserves these long exact sequences when the target is the derived category.

*Proof.* The composition of two consecutive maps of a distinguished triangle is zero, so the displayed sequence is a complex; exactness at each term is obtained by rotating the triangle and applying $H$ to the exact triangle on the relevant morphism, using that a rotation of a distinguished triangle is distinguished. $\square$

### Cohomological Functors and Homology

**Example.** The functor $H^0:D(\mathcal{A})\to\mathcal{A}$ sending a complex to its zeroth cohomology is **cohomological**: it carries distinguished triangles to long exact sequences. More generally $H^n$ is cohomological for every $n$, and the long exact homology sequence of a short exact sequence of complexes is the instance of the theorem for the triangle of the cone.

**Example.** For an object $M$ of $\mathcal{A}$ placed in degree $0$, the groups $\operatorname{Hom}_{D(\mathcal{A})}(M,N[n])$ are the derived functors $\operatorname{Ext}_{\mathcal{A}}^n(M,N)$; the proof is that the maps in the derived category from $M$ to $N[n]$ can be computed by a projective resolution of $M$ or an injective resolution of $N$, which is exactly the balanced computation of Ext. The derived category therefore contains the Ext groups as its hom groups.

## Derived Functors as Functors on the Derived Category

### Total Derived Functors

**Definition.** Let $F:\mathcal{A}\to\mathcal{B}$ be an additive functor between abelian categories. A **right derived functor** of $F$ is an exact functor $\mathbb{R}F:D(\mathcal{A})\to D(\mathcal{B})$ together with a natural transformation $Q_{\mathcal{B}}F\to\mathbb{R}FQ_{\mathcal{A}}$ that is universal among such; the **left derived functor** $\mathbb{L}F$ is defined dually. Universality means that any natural transformation from $Q_{\mathcal{B}}F$ to an exact functor factors uniquely through the comparison.

**Theorem.** If $\mathcal{A}$ has enough injectives then every left exact additive functor $F:\mathcal{A}\to\mathcal{B}$ has a right derived functor $\mathbb{R}F$, and if $\mathcal{A}$ has enough projectives then every right exact $F$ has a left derived functor $\mathbb{L}F$. In either case

$$
H^n\bigl(\mathbb{R}F(A)\bigr)\cong R^nF(A), \qquad H_n\bigl(\mathbb{L}F(A)\bigr)\cong L_nF(A),
$$

so the derived functors of *Derived Functors* are recovered as the cohomology of the total derived functor.

*Proof.* Define $\mathbb{R}F$ on the full subcategory of complexes of injectives by applying $F$ degreewise; a quasi-isomorphism between complexes of injectives is a homotopy equivalence, so this descends to the derived category, and the universal property of the localisation extends it to all of $D(\mathcal{A})$. The identification of the cohomology follows from the definition of $R^nF$. The projective case is dual. $\square$

**Corollary.** $\mathbb{R}\operatorname{Hom}_R(M,-)$ and $\mathbb{L}(-\otimes_RN)$ are exact functors on $D(R\text{-}\mathbf{Mod})$, and their cohomology in degree $n$ is $\operatorname{Ext}_R^n(M,-)$ and $\operatorname{Tor}_n^R(-,N)$ respectively.

### The Derived Hom and Tensor Product

**Definition.** For complexes $M,N$ over a ring $R$, the **derived hom** is

$$
\mathbb{R}\operatorname{Hom}_R(M,N)=\operatorname{Hom}_R^\bullet(M,I^\bullet)
$$

for an injective resolution $I^\bullet$ of $N$, and the **derived tensor product** is

$$
M\otimes_R^{\mathbb{L}}N=P_\bullet\otimes_RN
$$

for a projective resolution $P_\bullet$ of $M$; both are well-defined objects of $D(R\text{-}\mathbf{Mod})$.

**Theorem (adjunction).** The derived functors satisfy

$$
\operatorname{Hom}_{D(R\text{-}\mathbf{Mod})}(M\otimes_R^{\mathbb{L}}N,P)\cong\operatorname{Hom}_{D(R\text{-}\mathbf{Mod})}\bigl(M,\mathbb{R}\operatorname{Hom}_R(N,P)\bigr),
$$

so $-\otimes_R^{\mathbb{L}}N$ is left adjoint to $\mathbb{R}\operatorname{Hom}_R(N,-)$ on the derived category. There is also a natural isomorphism $M\otimes_R^{\mathbb{L}}N\cong N\otimes_R^{\mathbb{L}}M$.

*Proof.* The adjunction of the tensor product and Hom on the level of complexes, together with the fact that a complex of projectives computes the derived tensor product and a complex of injectives the derived hom, gives the displayed bijection; the universal property of the localisation shows that it is the hom set of the derived category. The commutativity follows from the corresponding isomorphism in the homotopy category and the symmetry of the resolutions. $\square$

**Example.** For modules $M,N$ placed in degree $0$, the cohomology of $\mathbb{R}\operatorname{Hom}_R(M,N)$ is $\operatorname{Ext}_R^\bullet(M,N)$ and the homology of $M\otimes_R^{\mathbb{L}}N$ is $\operatorname{Tor}_\bullet^R(M,N)$, with the extra structure that the derived objects carry: the cup product on $\mathbb{R}\operatorname{Hom}$ and the graded-commutative product on the derived tensor product, coming from the total complexes of *Homological Algebra*.

## Equivalences and Rings of Finite Global Dimension

### Coherent Sheaves and Perfect Complexes, Named Only

**Remark.** The **perfect complexes** are the complexes quasi-isomorphic to bounded complexes of finitely generated projective modules. They form a full triangulated subcategory of $D(R\text{-}\mathbf{Mod})$, and the derived tensor product restricts to it. In algebraic geometry the corresponding notion for sheaves on a scheme, together with the derived category of coherent sheaves and the six operations, is developed in Part II; here the definition is recorded in the module case as the object on which the K-theory is built.

### Rings of Finite Global Dimension

**Definition.** The **global dimension** of a ring $R$ is the supremum of the projective dimensions of its modules, equivalently the largest $n$ for which there exist modules $M,N$ with $\operatorname{Ext}_R^n(M,N)\neq0$.

**Theorem.** For a ring $R$ and an integer $n\ge0$ the following are equivalent: (i) every $R$-module has projective dimension at most $n$; (ii) $\operatorname{Ext}_R^k(-,-)=0$ for all $k>n$. Moreover the canonical functor $K^b(R\text{-}\mathbf{Proj})\to D^b(R\text{-}\mathbf{Mod})$ from the homotopy category of bounded complexes of projective modules is an equivalence if and only if $R$ has finite global dimension, that is, if and only if every module has finite projective dimension.

*Proof.* (i) and (ii) are equivalent because a module of projective dimension at most $n$ is exactly one with a projective resolution of length at most $n$, and $\operatorname{Ext}^k$ vanishes beyond the resolution length. If every module has finite projective dimension, resolving each term of a bounded complex and applying the horseshoe lemma produces a bounded complex of projectives quasi-isomorphic to it, and between bounded complexes of projectives a quasi-isomorphism is a homotopy equivalence, so the canonical functor is an equivalence. Conversely, if the functor is an equivalence, a module $M$ placed in degree $0$ is quasi-isomorphic to a bounded complex of projectives, and the cone of the comparison map exhibits a finite projective resolution of $M$; so the global dimension is finite. $\square$

**Example.** A field has global dimension $0$: every module is free, so $\operatorname{Ext}^n=0$ for $n\ge1$ and $D^b$ is the homotopy category of bounded complexes of vector spaces. A principal ideal domain that is not a field has global dimension $1$: every module has a free resolution of length one, so $\operatorname{Ext}^n=0$ for $n\ge2$ and every bounded complex is quasi-isomorphic to a bounded complex of free modules by the structure theorem. Both examples show that when the global dimension is finite every object of $D^b(R\text{-}\mathbf{Mod})$ is isomorphic to a bounded complex of projective modules, so that $D^b(R\text{-}\mathbf{Mod})\simeq K^b(R\text{-}\mathbf{Proj})$ and no objects beyond these complexes appear; it is the unbounded complexes, and the rings of infinite global dimension, that require the full localisation.

**Remark.** The derived category of a ring is not abelian in general: it is triangulated, and a triangulated category has no notion of kernel and cokernel that would make it abelian. It is therefore not a module category over any ring, and the Gabriel–Popescu theory of *Abelian and Grothendieck Categories* does not apply to it. The triangulated structure is the replacement, and it is the reason the articles that work in the derived setting use triangles and exact triangles rather than short exact sequences.

## The Triangle of a Short Exact Sequence

### Distinguished Triangles from Short Exact Sequences

**Proposition.** A short exact sequence of complexes $0\to A_\bullet\to B_\bullet\to C_\bullet\to0$ gives a distinguished triangle

$$
A_\bullet\to B_\bullet\to C_\bullet\to A_\bullet[1]
$$

in $D(\mathcal{A})$, and the long exact homology sequence is the long exact sequence of this triangle under the cohomological functor $H^0$.

*Proof.* The sequence is degreewise a surjection $B^n\to C^n$ of modules, so a degreewise section of the underlying sets exists; the standard construction of *Homological Algebra* assembles it into a chain map $C_\bullet\to A_\bullet[1]$ whose mapping cone is quasi-isomorphic to $B_\bullet$, and the comparison with the mapping cone of $A_\bullet\to B_\bullet$ gives the distinguished triangle. The long exact sequence is the theorem on cohomological functors applied to it. $\square$

**Corollary.** The connecting morphism of the long exact sequence is, in the derived category, the morphism $C\to A[1]$ of the triangle; the naturality of the connecting morphism is the functoriality of the cone construction.

### The Octahedron in Practice

**Proposition.** A composition of morphisms in $D(\mathcal{A})$ and distinguished triangles on the two composites and on the middle morphism fit into the octahedron; equivalently, the induced maps on cohomology fit into the braid diagram of a composition of two connecting morphisms, which is the algebraic content of the octahedral axiom. The formulation is used to compare the two spectral sequences of a double complex, as in *Spectral Sequences*.

**Theorem (Verdier).** In a triangulated category the octahedral axiom is equivalent to the following sharpened form: for a composition $X\xrightarrow{f}Y\xrightarrow{g}Z$ with cones $Z'=\operatorname{Cone}(f)$, $X'=\operatorname{Cone}(g)$ and $Y'=\operatorname{Cone}(gf)$, there is a morphism $Z'\to Y'$ completing the diagrams to a distinguished triangle $Z'\to Y'\to X'\to TZ'$ such that the composite $X'\to TZ'\to TY$ differs from the structure morphism $X'\to TY$ by the sign forced by the translation. Thus the axiom asserts the functoriality of the cone construction on a composition, not merely the existence of a fourth triangle.

*Proof.* This is the classical form of the axiom, due to Verdier; the equivalence with the version stated above is the standard rearrangement of the diagrams, and the comparison of signs is the comparison of the two rotations of the triangle on $gf$. The proof is a diagram chase in the triangulated category, and is standard. $\square$

## Summary

The homotopy category $K(\mathcal{A})$ of complexes has as morphisms the chain maps modulo homotopy; it is additive, contractible complexes are zero in it, and the mapping cone produces the cone diagrams whose homology is the long exact sequence. The derived category $D(\mathcal{A})$ is the localisation of $K(\mathcal{A})$ at the quasi-isomorphisms; it exists by the general construction of a category of fractions, and its morphisms are computable by roofs once complexes of injectives or of projectives are available; a module becomes isomorphic to any of its resolutions in $D(\mathcal{A})$.

The derived category is triangulated: it carries a translation and a class of distinguished triangles with the cone construction, rotation, the octahedral axiom, and a long exact sequence for every cohomological functor. The hom groups are the Ext groups, $\operatorname{Hom}_{D(\mathcal{A})}(M,N[n])=\operatorname{Ext}^n_{\mathcal{A}}(M,N)$, so the derived category is the natural home of Ext. Every left exact functor with enough injectives has a total right derived functor $\mathbb{R}F$ whose cohomology recovers $R^nF$, and every right exact functor with enough projectives has $\mathbb{L}F$ with homology $L_nF$; the total derived functors are exact, they satisfy the derived tensor–hom adjunction, and the derived tensor product is commutative.

For a ring of finite global dimension the derived category of bounded complexes is equivalent to the homotopy category of bounded complexes of projectives, so the theory adds nothing in that case; the general theory is genuinely larger because the derived category need not be abelian. The derived categories of sheaves, the six operations for schemes and the geometric applications are part of Part II, and the model-category and higher-categorical formulations that underlie the construction are treated .

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K(\mathcal{A})$, $K^+$, $K^-$, $K^b$ | homotopy category of complexes, bounded below, above, both |
| $\mathbf{Ch}(\mathcal{A})$ | category of chain complexes |
| $D(\mathcal{A})$, $D^\pm$, $D^b$ | derived category and its bounded variants |
| $\Sigma$, $\mathcal{C}[\Sigma^{-1}]$ | a class of morphisms and the localisation at it |
| $C[n]$ | shift of a complex by $n$ |
| $\operatorname{Cone}(f)$ | mapping cone, the third vertex of a distinguished triangle |
| $T$ | translation functor of a triangulated category |
| $X\to Y\to Z\to TX$ | distinguished triangle |
| $\mathbb{R}F$, $\mathbb{L}F$ | total right and left derived functors |
| $\mathbb{R}\operatorname{Hom}_R(M,N)$ | derived hom complex |
| $M\otimes_R^{\mathbb{L}}N$ | derived tensor product |
| $\operatorname{Hom}_{D(\mathcal{A})}(M,N[n])=\operatorname{Ext}^n_{\mathcal{A}}(M,N)$ | hom groups of the derived category |
| $R$ | commutative ring with $1\neq0$ unless stated |





## Further Reading

- Alexander Beilinson, Joseph Bernstein and Pierre Deligne, "Faisceaux pervers", *Astérisque* 100 (1982), for the triangulated formalism and the t-structures of derived categories.
- Alexei I. Bondal and Mikhail M. Kapranov, "Enhanced triangulated categories", *Mathematics of the USSR Sbornik* 70 (1991), 93–107, for the limits of the triangulated formalism.
- Pierre Deligne, *Cohomologie à supports propres*, in *Théorie des topos et cohomologie étale des schémas* (Springer Lecture Notes in Mathematics 305, 1973), for derived categories and the six operations.
- Robin Hartshorne, *Residues and Duality* (Springer Lecture Notes in Mathematics 20, 1966), for the derived category in algebraic geometry.
- Luc Illusie, *Complexe cotangent et déformations I* (Springer Lecture Notes in Mathematics 239, 1971), for derived categories in deformation theory.
- Masaki Kashiwara and Pierre Schapira, *Categories and Sheaves* (Springer, 2006), for triangulated categories and derived functors in the categorical setting.
- Amnon Neeman, *Triangulated Categories* (Princeton University Press, 2001), for the axioms and their consequences.
- Jean-Louis Verdier, "Catégories dérivées: quelques résultats", in *Séminaire de Géométrie Algébrique du Bois-Marie*, SGA 4½ (Springer Lecture Notes in Mathematics 569, 1977), for the localisation theorem and the octahedral axiom.
