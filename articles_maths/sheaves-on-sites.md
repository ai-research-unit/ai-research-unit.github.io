
# __Sheaves on Sites__

## Introduction

A site is a small category equipped with a Grothendieck topology, that is, with a rule which says when a family of morphisms into a fixed object is to be regarded as a covering of that object. The data of a topology on a category replaces the data of the open sets of a topological space, and it is strictly more general: every topological space gives a site whose objects are its open sets, but a site may also be a category of rings, of group actions, or of finite diagrams, and the sheaf condition then becomes a gluing condition for the algebraic structures encoded by those objects. On a site one defines the presheaves, which are the contravariant set-valued functors, the sheaves, which are the presheaves satisfying the gluing axiom with respect to every covering, and the sheafification, which is the universal sheaf mapping out of a presheaf. The category of sheaves is a Grothendieck topos, so the machinery of *Topoi* applies, and the **cohomology of a site** is the right derived functor of the global sections functor; it is computed from injective resolutions, and in the presence of a covering it is approximated by the **Čech cohomology** of that covering, with the comparison given by a spectral sequence.

This article develops the presheaf category and the Yoneda embedding, sieves and Grothendieck topologies, the sheaf condition and the separation condition, the sheafification functor and its exactness, the cohomology of a site by derived functors and by the Čech complex, the Čech-to-derived spectral sequence, the functoriality of the cohomology under morphisms of sites, the comparison with the classical topological case, and the examples of the site of a group, of the site with the trivial and the chaotic topologies, and of a covering by a single morphism. It follows *Topoi*, *Homological Algebra*, *Derived Functors*, *Ext and Tor*, *Spectral Sequences* and *Abelian and Grothendieck Categories*, and it prepares.

Throughout, $\mathcal{C}$ is a small category, $J$ a Grothendieck topology on it, $(\mathcal{C},J)$ a site, $\widehat{\mathcal{C}}=\operatorname{Fun}(\mathcal{C}^{\mathrm{op}},\mathbf{Set})$ the category of presheaves, and $\mathbf{Sh}(\mathcal{C},J)$ the category of sheaves; the sheaves of abelian groups are written $\mathbf{Sh}(\mathcal{C},J;\mathbf{Ab})$ and form an abelian category with enough injectives. The cohomology of a site is the *algebraic* theory over a site; the cohomology of a topological space, the sheaf cohomology with supports, the Čech cohomology of an open cover and the Leray–Serre spectral sequence for a map of spaces belong to Part II, where the open sets and the continuous maps are available, and this article states the comparison with that theory only as a forward pointer.

## Presheaves and the Yoneda Embedding

**Definition.** A **presheaf** on $\mathcal{C}$ is a functor $F:\mathcal{C}^{\mathrm{op}}\to\mathbf{Set}$; a **morphism of presheaves** is a natural transformation. The presheaf represented by an object $c$ is the functor $h_c=\operatorname{Hom}_{\mathcal{C}}(-,c)$, and the **Yoneda embedding** is the functor $h:\mathcal{C}\to\widehat{\mathcal{C}}$, $c\mapsto h_c$. A presheaf of abelian groups is a functor $\mathcal{C}^{\mathrm{op}}\to\mathbf{Ab}$, and the category of such functors is abelian with the pointwise kernels and cokernels.

**Theorem (Yoneda).** For every presheaf $F$ and every object $c$ there is a natural bijection
$$
\operatorname{Hom}_{\widehat{\mathcal{C}}}(h_c,F)\cong F(c),
$$
given by evaluating a natural transformation at the identity of $c$. Consequently the Yoneda embedding is full and faithful, and every presheaf is a colimit of representable presheaves, the colimit being indexed by the category of elements of the presheaf.

*Proof.* The inverse of the evaluation map sends an element $x\in F(c)$ to the natural transformation whose component at $d$ carries $f:d\to c$ to the image of $x$ under the map $F(f):F(c)\to F(d)$; the two compositions are the identity by the functoriality of $F$ and the naturality of the transformation. The colimit description follows by computing the colimit of the representables over the category of elements. $\square$

**Proposition.** The presheaf category is complete and cocomplete, with limits and colimits computed pointwise, and it is cartesian closed: the exponential of the presheaves $F$ and $G$ is the presheaf $G^F$ with $G^F(c)=\operatorname{Hom}_{\widehat{\mathcal{C}}}(h_c\times F,G)$. The Yoneda embedding preserves the limits that exist in $\mathcal{C}$ and carries them to limits of representables.

*Proof.* The pointwise formulas are the definition of the limits and colimits in a functor category; the cartesian closedness is the computation of the natural transformations out of a product of representables, and the preservation of limits is the Yoneda lemma applied to the hom functors. $\square$

**Example.** For $\mathcal{C}$ the one-object category of a group $G$ the presheaves are the $G$-sets, and the Yoneda embedding sends the object to the regular $G$-set $G$ with the action of left translation; for $\mathcal{C}$ the category of open subsets of a space the presheaves are the contravariant systems of sets indexed by the open subsets, and the sheaves are the classical ones, a comparison developed in Part II.

## Sieves and Grothendieck Topologies

**Definition.** A **sieve** on an object $c$ is a set $S$ of morphisms with codomain $c$ closed under composition on the right: if $g\in S$ and $g=hf$ then $f\in S$ and $hf\in S$; equivalently, a subfunctor $S\subseteq h_c$. The **pullback** of a sieve $S$ on $c$ along $f:d\to c$ is the sieve $f^*S$ on $d$ consisting of the morphisms $g$ with $fg\in S$. The **maximal sieve** on $c$ is the whole hom-set $h_c$.

**Definition.** A **Grothendieck topology** on $\mathcal{C}$ assigns to each object $c$ a set $J(c)$ of sieves on $c$, the **covering sieves**, satisfying:
1. the maximal sieve lies in $J(c)$ for every $c$;
2. if $S\in J(c)$ and $f:d\to c$ then $f^*S\in J(d)$;
3. if $S\in J(c)$ and $R$ is a sieve on $c$ such that $f^*R\in J(d)$ for every $f\in S$, then $R\in J(c)$.

A **coverage** is an equivalent presentation by families of morphisms: a covering family of $c$ is a family $\{f_i:c_i\to c\}$ generating a covering sieve, and the axioms become the identity cover, the stability under pullback, and the transitivity of the covers. The pair $(\mathcal{C},J)$ is a **site**.

**Example.** The **trivial topology** has $J(c)=\{h_c\}$ for every $c$, so the only covering sieve is the maximal one, and every presheaf is a sheaf; the **chaotic topology** has $J(c)$ equal to the set of all sieves on $c$, and the sheaves are the presheaves constant on the connected components of $\mathcal{C}$; the **canonical topology** on a category $\mathcal{C}$ has as covering sieves those that are stable under pullback and epimorphic in the sense that the induced map of presheaves is an epimorphism, and every representable presheaf is a sheaf, so the topology is subcanonical. A subcanonical topology on the category of affine schemes with the Zariski covers gives the classical Zariski site of algebraic geometry, which is treated in Part II.

**Proposition.** A Grothendieck topology is determined by its covering families, and the pullback axiom is the assertion that the covers are stable under base change; the composition of two covering sieves is again covering, and the set of closed sieves, that is, of sieves $R$ with the property that $f^*R$ covers $d$ whenever $f:d\to c$ is in a covering sieve of $c$, is in bijection with the elements of the subobject classifier of the topos of sheaves.

*Proof.* The equivalence of the sieve and the family presentations is the definition of the sieve generated by a family, and the closure properties are the axioms (2) and (3). The identification of the closed sieves with the subobject classifier is the description of $\Omega$ in the previous article. $\square$

## Sheaves and Sheafification

**Definition.** A presheaf $F$ is a **sheaf** for $J$ if for every object $c$ and every covering sieve $S\in J(c)$ the canonical map
$$
F(c)\longrightarrow\varprojlim_{f\in S}F(\operatorname{dom}f)
$$
is a bijection, the limit being over the category whose objects are the morphisms in $S$ and whose morphisms are the commutative triangles. For a covering family $\{f_i:c_i\to c\}$, the limit is the equalizer of the two maps $\prod_iF(c_i)\rightrightarrows\prod_{i,j}F(c_i\times_cc_j)$ when the fibre products exist, which is the familiar gluing condition of the classical theory. A presheaf is **separated** if the canonical maps are injective for all covering sieves.

**Proposition.** A presheaf is a sheaf if and only if it is separated and the canonical maps are surjective; the full subcategory $\mathbf{Sh}(\mathcal{C},J)\subseteq\widehat{\mathcal{C}}$ is closed under limits, and the inclusion has a left adjoint
$$
a\dashv i,\qquad i:\mathbf{Sh}(\mathcal{C},J)\hookrightarrow\widehat{\mathcal{C}},
$$
the **sheafification** or **associated sheaf** functor, which is left exact. The sheafification is computed by the **plus construction**: $F^{+}(c)$ is the filtered colimit over the covering sieves $S$ of $c$ of the compatible families $(x_f)_{f\in S}$ with $x_f\in F(\operatorname{dom}f)$ and $x_{fg}=F(g)x_f$, and $aF=(F^{+})^{+}$.

*Proof (in outline).* The plus construction produces a separated presheaf from an arbitrary one and a sheaf from a separated one; the two-step iteration is therefore a sheaf, and any morphism from $F$ to a sheaf factors uniquely through it, which gives the adjunction. The left exactness uses the stability of the covering sieves under pullback and the fact that the filtered colimit involved is over a filtering category; it is the property that makes the category of sheaves have the same finite limits as the presheaf category. $\square$

**Example.** For the trivial topology the sheafification is the identity; for the chaotic topology the sheafification of $F$ is the presheaf that is constant on each connected component with value the colimit of $F$ over that component; for the site of a group $G$ with the chaotic topology on the one-object groupoid, the sheaves are the $G$-sets with the trivial action, and the sheafification of a $G$-set is its set of orbits with the trivial action.

**Theorem.** The category of sheaves of abelian groups on a site is a Grothendieck abelian category: it is cocomplete, it has a generator, the filtered colimits are exact, and it has enough injectives. Consequently the functors of *Abelian and Grothendieck Categories* apply, the derived functors of the left exact additive functors are defined on it, and the global sections functor $\Gamma=\operatorname{Hom}_{\mathbf{Sh}}(1,-)$ has right derived functors computed from injective resolutions.

*Proof.* The category is a reflective subcategory of the abelian presheaf category $\operatorname{Fun}(\mathcal{C}^{\mathrm{op}},\mathbf{Ab})$ closed under filtered colimits and under kernels, and the reflection is exact; the existence of enough injectives is Grothendieck's theorem that a Grothendieck abelian category with a generator has enough injectives, applied to the sheaf category with the generator the direct sum of the sheafifications of the representable presheaves of abelian groups. $\square$

## Cohomology of a Site

**Definition.** Let $(\mathcal{C},J)$ be a site and let $F$ be a sheaf of abelian groups on it. The **cohomology groups of the site with coefficients in $F$** are
$$
H^p(\mathcal{C},J;F)=\mathbf{R}^p\Gamma(F),\qquad \Gamma(F)=F(1)=\operatorname{Hom}_{\mathbf{Sh}}(1,F),
$$
the right derived functors of the global sections functor, computed from an injective resolution $F\to I^\bullet$ as the cohomology of the complex $\Gamma(I^\bullet)$. The site has **cohomological dimension** at most $n$ if $H^p(\mathcal{C},J;F)=0$ for all $p>n$ and all sheaves $F$.

**Proposition.** The functor $\Gamma$ is left exact and additive, $H^0(\mathcal{C},J;F)=\Gamma(F)$ is the group of global sections, and a short exact sequence of sheaves $0\to F\to G\to H\to0$ induces a long exact sequence
$$
0\to H^0(F)\to H^0(G)\to H^0(H)\to H^1(F)\to H^1(G)\to\cdots
$$
in the cohomology of the site. A sheaf $F$ with $H^p(\mathcal{C},J;F)=0$ for all $p>0$ is **acyclic** for the topology, and a resolution of $F$ by acyclic sheaves computes the cohomology in place of an injective resolution.

*Proof.* The left exactness of $\Gamma$ is the statement that it preserves kernels, computed pointwise in the abelian presheaf category and then restricted to the sheaves; the long exact sequence is the standard long exact sequence of a right derived functor, and the acyclic resolution statement is the spectral-sequence argument comparing the two resolutions. $\square$

**Definition.** Let $\mathcal{U}=\{f_i:c_i\to c\}$ be a covering family and let $F$ be a sheaf of abelian groups. The **Čech complex** of the covering relative to $F$ is the cochain complex
$$
\check C^p(\mathcal{U},F)=\prod_{i_0,\dots,i_p}F(c_{i_0}\times_c\cdots\times_cc_{i_p}),
$$
with the alternating sum of the pullbacks as differential, and the **Čech cohomology** $\check H^p(\mathcal{U},F)$ is the cohomology of this complex; the Čech cohomology of the site is the filtered colimit of $\check H^p(\mathcal{U},F)$ over the coverings $\mathcal{U}$ of the objects.

**Theorem (Čech-to-derived spectral sequence).** For every covering family $\mathcal{U}$ of the terminal object and every sheaf $F$ there is a spectral sequence
$$
E_2^{p,q}=\check H^p(\mathcal{U},\underline{H}{}^q(F))\Longrightarrow H^{p+q}(\mathcal{C},J;F),
$$
where $\underline{H}{}^q(F)$ is the presheaf of the local cohomology groups of $F$. In particular, if the covering is acyclic for $F$ in all degrees, the edge maps give isomorphisms $\check H^p(\mathcal{U},F)\cong H^p(\mathcal{C},J;F)$.

*Proof (in outline).* The Čech complex is the total complex of a double complex whose columns are the complexes computing the local cohomology of $F$ on the pieces of the covering, and the spectral sequence of the double complex of *Spectral Sequences* has the stated $E_2$ page; the edge maps identify the abutment with the derived functors of the global sections because the Čech resolution of the covering computes the cohomology of the site when the pieces are acyclic. $\square$

**Example.** For the chaotic topology on a category with a terminal object the covers are all the sieves, the sheaf condition is very strong, and the cohomology reduces to that of the constant sheaves on the components; for the trivial topology the covers are trivial and the cohomology vanishes in positive degrees; for the site associated with a group $G$ and a $G$-module $M$, with the one-object groupoid of $G$ and the trivial topology, so that the sheaves are exactly the $G$-sets, the cohomology of the site is the group cohomology $H^p(G,M)$, computed from the standard resolution of $\mathbb{Z}$ by the free $G$-modules; the same groups arise from the canonical topology, since a presheaf on a groupoid is a sheaf for the canonical topology as soon as it is a sheaf for the trivial one. The last example identifies the site-theoretic cohomology with a classical algebraic invariant and shows that the theory of this article contains, as special cases, the cohomology theories of the algebraic objects introduced earlier in the corpus.

## Functoriality and Morphisms of Sites

**Definition.** A **morphism of sites** $f:(\mathcal{C},J)\to(\mathcal{D},K)$ is a functor $f:\mathcal{C}\to\mathcal{D}$ carrying covering sieves of $J$ to covering sieves of $K$, in the sense that the image under $f$ of a covering family generates a covering family. A functor of sites carrying covering sieves to covering sieves induces a geometric morphism $f:\mathbf{Sh}(\mathcal{C},J)\to\mathbf{Sh}(\mathcal{D},K)$ with inverse image $f^*$ the sheafification of the pullback presheaf $H\mapsto H\circ f^{\mathrm{op}}$ and direct image $f_*$ the restriction $F\mapsto F\circ f$.

**Proposition.** The inverse image $f^*$ is left exact and the direct image $f_*$ is right adjoint to it; $f^*$ preserves the finite limits and the colimits, and the cohomology of a site is contravariant in the site and covariant in the coefficients. For a sheaf $G$ on $(\mathcal{D},K)$ there is a **Leray spectral sequence**
$$
E_2^{p,q}=H^p(\mathcal{C},J;\mathbf{R}^qf_*G)\Longrightarrow H^{p+q}(\mathcal{D},K;G),
$$
whose edge maps give the functoriality of the global cohomology in the morphism of sites.

*Proof.* The left exactness of $f^*$ is the definition of a morphism of sites, and the adjunction $f^*\dashv f_*$ is the adjunction between the pullback and the pushforward of presheaves restricted to the sheaves, with the sheafification taken into account. The spectral sequence is the Grothendieck spectral sequence for the composite of the global sections functors, applied to the triangle of functors $\Gamma_{\mathcal{D}}\cong\Gamma_{\mathcal{C}}\circ f_*$. $\square$

**Remark.** The Leray spectral sequence of this proposition is the site-theoretic form of the corresponding spectral sequence for a map of topological spaces, and the topological Leray–Serre spectral sequence, together with the sheaf cohomology of a space and the interplay with the continuous maps, belongs to Part II, where the open sets and the topology are available. The present article uses only the site-theoretic statement, and the reader who wants the topological form should consult *Sheaves and Cohomology* and *Algebraic Topology* of that Part.

## Summary

A Grothendieck topology on a small category is a rule assigning the covering sieves to the objects, stable under pullback and transitive; a site is a small category with such a topology. A presheaf is a contravariant set-valued functor, a sheaf is a presheaf satisfying the gluing condition with respect to every covering sieve, and the inclusion of the sheaves into the presheaves has a left exact left adjoint, the sheafification, computed by the two-step plus construction; the category of sheaves is a Grothendieck topos, and its abelian variant is a Grothendieck abelian category with enough injectives. The cohomology of a site with coefficients in a sheaf of abelian groups is the right derived functor of the global sections functor; it is computed from injective or acyclic resolutions, it satisfies the long exact sequence of a short exact sequence of coefficients, it is approximated by the Čech cohomology of a covering through the Čech-to-derived spectral sequence, and it is functorial in the site through the geometric morphisms, with the Leray spectral sequence describing the change.

The examples identify the theory with classical algebraic invariants in special cases: the topologies on a small category of presheaves with the trivial or the chaotic topology, the site of a group with the group cohomology as its cohomology, and the classical topological sheaves, whose comparison is deferred to Part II. Another article turns the gluing condition into an equivalence of categories, the descent theorem, and reads the cohomological obstructions as the failure of that equivalence.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{C}$ | small category |
| $J$ | Grothendieck topology |
| $(\mathcal{C},J)$ | site |
| $h_c=\operatorname{Hom}_{\mathcal{C}}(-,c)$ | representable presheaf |
| $\widehat{\mathcal{C}}$ | presheaf category |
| $\mathbf{Sh}(\mathcal{C},J)$ | sheaf category |
| $a\dashv i$ | sheafification adjunction |
| $F^{+}$ | plus construction of a presheaf |
| $\Gamma(F)=F(1)$ | global sections functor |
| $H^p(\mathcal{C},J;F)$ | cohomology of the site |
| $\check C^p(\mathcal{U},F)$, $\check H^p(\mathcal{U},F)$ | Čech complex and cohomology of a covering |
| $f^*\dashv f_*$ | geometric morphism induced by a morphism of sites |
| $\Omega$ | subobject classifier |



## Further Reading

- Michael Artin, Alexander Grothendieck and Jean-Louis Verdier, *Théorie des topos et cohomologie étale des schémas (SGA 4)* (Springer Lecture Notes in Mathematics 269, 270, 305, 1972–1973), for the cohomology of sites and the Čech-to-derived comparison.
- Michael Artin, *Grothendieck Topologies* (Harvard University notes, 1962), for the original axiomatic treatment of the topologies and the sheaves.
- Francis Borceux, *Handbook of Categorical Algebra 3: Categories of Sheaves* (Cambridge University Press, 1994), for the sheafification, the plus construction and the cohomology.
- Alexander Grothendieck, "Sur quelques points d'algèbre homologique", *Tohoku Mathematical Journal* 9 (1957), 119–221, for the abelian-category foundations and the derived functors.
- Peter T. Johnstone, *Sketches of an Elephant: A Topos Theory Compendium* (Oxford University Press, 2002), for the exhaustive account of the sites and the sheaf cohomology.
- Saunders Mac Lane and Ieke Moerdijk, *Sheaves in Geometry and Logic: A First Introduction to Topos Theory* (Springer, 1992), for the Čech cohomology, the comparison and the examples.
- Jean-Pierre Serre, "Faisceaux algébriques cohérents", *Annals of Mathematics* 61 (1955), 197–278, for the sheaf-theoretic cohomology in its classical form.
