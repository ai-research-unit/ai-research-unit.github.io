
# __Adic Spaces__

## Introduction

Rigid analytic geometry uses a Grothendieck topology on the maximal spectrum of an affinoid algebra, Berkovich geometry uses honest multiplicative seminorms on the whole algebra, and formal geometry uses the adic topology of a completion. Huber's **adic spaces** unify all three: the points are equivalence classes of continuous valuations on a **Huber ring**, the topology is a genuine topology, and every rigid space, every Berkovich space and every formal scheme of finite type over a complete adic ring appears as an adic space or as a closely related object. The construction is the modern language of non-Archimedean geometry, and it is the language in which perfectoid spaces are defined.

An adic space carries two structures at once, and this is the source of its power. On the algebraic side there is a sheaf of complete topological rings, so that the functor-of-points description of a formal scheme is retained; on the geometric side there is a genuine topological space of valuations, so that the connectedness, compactness and fibre-product properties of Berkovich geometry are retained. The price is that the points are equivalence classes of valuations rather than seminorms, and that the topology must be defined carefully, first as the **spectral topology** on the set of continuous valuations, then by restriction to the open subsets that admit the analytic structure. These two topologies are the technical heart of the theory.

This article defines Huber rings, continuous valuations, the adic spectrum and its two topologies, the structure sheaf and its completeness, the analytic open subsets, and the category of adic spaces with fibre products. It develops the comparison with rigid, Berkovich and formal geometry, treats the standard examples — the adic unit disc, the adic affine and projective lines, the adic fields and the finite-extension spaces — and closes with the tilting and perfectoid context up. It assumes *Topological Rings and Fields* for adic topologies and completions, *Local Fields* for valuations and value groups, *Rigid Analytic Geometry* and *Berkovich Spaces* for the two earlier geometries, and *Formal Schemes* for the formal models. As before, the analytic content belongs to Part III; only the topology, the valuations and the algebraic geometry of the spaces are used. Throughout, a **Huber ring** is a topological ring $A$ admitting an open subring $A_0$ whose induced topology is $I$-adic for some ideal of definition $I \subseteq A_0$; such an $A_0$ is a **ring of definition** and $I$ an **ideal of definition**. A Huber ring is **Tate** if it has a topologically nilpotent unit, and **complete** if it is complete for its topology.

---

## Huber Rings and Continuous Valuations

### Huber Rings

**Definition.** A topological ring $A$ is a **Huber ring** (or **f-adic ring**) if there is an open subring $A_0 \subseteq A$ and a finitely generated ideal $I \subseteq A_0$ such that the sets $I^n$ form a fundamental system of neighbourhoods of $0$ in $A_0$, with the topology on $A_0$ the subspace topology from $A$. The subring $A_0$ is a **ring of definition**. A Huber ring is **uniform** if its subring $A^\circ$ of power-bounded elements is bounded; and **Tate** if it contains an element $t$ which is a unit and topologically nilpotent.

**Example (affinoid algebras are Tate).** A $K$-affinoid algebra $A$ with the residue norm topology is a Tate Huber ring: the ring of definition is the unit ball $A^\circ = \{a : \lVert a \rVert \leq 1\}$, the ideal of definition is the topologically nilpotent ideal $A^{\circ\circ} = \{a : \lVert a \rVert < 1\}$, and the residue field element $K^\times$ gives a topologically nilpotent unit when the value group of $K$ is nontrivial.

**Example (complete adic rings).** A complete noetherian adic ring $A$ with ideal of definition $I$ is a Huber ring with $A_0 = A$ and the given $I$; it is Tate only in degenerate cases, since an adic ring whose topology is nontrivial and complete has no topologically nilpotent unit in general.

**Example (the ring of definition of $\mathbb{Z}_p$).** $\mathbb{Z}_p$ with the $p$-adic topology is Huber with $A_0 = \mathbb{Z}_p$, $I = (p)$; $\mathbb{Q}_p$ with the $p$-adic topology is Huber with ring of definition $\mathbb{Z}_p$ and $I = (p)$, and it is Tate because $p$ is a topologically nilpotent unit in $\mathbb{Q}_p$.

**Definition.** A **continuous valuation** on a Huber ring $A$ is a map $\lvert \cdot \rvert : A \to \Gamma \cup \{0\}$, where $\Gamma$ is a totally ordered abelian group written multiplicatively, such that $\lvert 0 \rvert = 0$, $\lvert 1 \rvert = 1$, $\lvert ab \rvert = \lvert a \rvert \lvert b \rvert$, $\lvert a + b \rvert \leq \max(\lvert a \rvert, \lvert b \rvert)$, and $\lvert \cdot \rvert$ is continuous for the topology of $A$ and the order topology on $\Gamma$. Two valuations are **equivalent** if one is a power of the other with a positive exponent, that is, if there is an order isomorphism of their value groups making the two maps agree; equivalence classes are the points. The **support** of a valuation is the prime ideal $\mathfrak{p} = \{a : \lvert a \rvert = 0\}$; the valuation is **non-degenerate** if the support contains no open ideal, and **analytic** if in addition the topology of $A$ is the topology induced by the valuation.

**Proposition.** Let $A$ be a Huber ring and $\lvert \cdot \rvert$ a continuous valuation with value group $\Gamma$. Then the sets

$$
A^\circ = \{a \in A : \lvert a \rvert \leq 1\}, \qquad A^{\circ\circ} = \{a \in A : \lvert a \rvert < 1\}
$$

are an open subring and an open ideal of $A$ respectively, and the pair is a ring of definition. If $\lvert \cdot \rvert$ is continuous then it is bounded by a constant multiple of the norm of any fixed ring of definition, and its support is a prime ideal.

**Proof.** Multiplicativity makes $A^\circ$ closed under multiplication, and the ultrametric inequality makes it closed under addition; continuity of the valuation at $0$ makes $A^\circ$ a neighbourhood of $0$, hence open, and it is a subring containing $1$. The set $A^{\circ\circ}$ is an ideal contained in $A^\circ$ by the same two properties and is open, and its complement in $A^\circ$ is the set of units of $A^\circ$ because an element of value $1$ has inverse of value $1$. The boundedness statement follows because a continuous homomorphism from a topological group to an ordered group with the order topology is bounded on a neighbourhood of $0$. $\square$

### The Adic Spectrum

**Definition.** Let $A$ be a Huber ring. The **adic spectrum** $\operatorname{Spa}(A, A^+)$ of a **Huber pair** $(A, A^+)$, where $A^+ \subseteq A$ is an open and integrally closed subring, is the set of equivalence classes of continuous valuations $\lvert \cdot \rvert$ on $A$ such that $\lvert a \rvert \leq 1$ for all $a \in A^+$. The two natural topologies on $\operatorname{Spa}(A, A^+)$ are:

**(a)** the **spectral topology**, generated by the subsets

$$
\{x : \lvert f(x) \rvert \leq 1\} \quad \text{and} \quad \{x : \lvert f(x) \rvert \geq 1\} \qquad (f \in A);
$$

**(b)** the **analytic topology**, generated by the **rational subsets**

$$
R\Bigl(\frac{f_1, \dots, f_n}{g}\Bigr) = \{x : \lvert f_i(x) \rvert \leq \lvert g(x) \rvert \neq 0 \text{ for all } i\},
$$

which generate the analytic topology; that topology refines the spectral one, since $\{x : \lvert f(x)\rvert \leq 1\} = R(f/1)$ and $\{x : \lvert f(x)\rvert \geq 1\} = R(1/f)$ are rational subsets.

**Remark.** The two topologies are genuinely different, and the analytic topology is the one used for the geometry. The spectral topology is compact and makes $\operatorname{Spa}(A, A^+)$ a spectral space, but the rational subsets form a basis only for the analytic topology; the analytic topology is the topology generated by the rational subsets, and it is the right topology for gluing. A subset that is open in the spectral topology is open in the analytic topology, but not conversely; the difference is the source of the technical care that the theory requires.

**Theorem.** Let $(A, A^+)$ be a Huber pair with $A$ complete. Then $\operatorname{Spa}(A, A^+)$ with the spectral topology is compact and satisfies the following separation property: it is a spectral space in the sense of Hochster, that is, it is homeomorphic to the spectrum of a ring with the Zariski topology; in particular it is quasi-compact and sober. It is Hausdorff for the analytic topology when $A$ is strongly noetherian, and it is then a compact Hausdorff space on the rational subsets.

**Proof.** The compactness of the spectral topology is Huber's theorem: a continuous valuation on a Huber ring is bounded on a ring of definition, so that the continuous valuations with $\lvert a\rvert \leq 1$ on $A^+$ embed as a closed subspace of a product of compact intervals attached to the rings of definition, and Tychonoff gives compactness; the spectral-space property is the statement that the topology has a basis of quasi-compact opens closed under finite intersections and that every irreducible closed subset has a generic point, both of which follow from the corresponding properties of the spectra of the rings of definition. Hausdorffness for the analytic topology in the strongly noetherian case is Huber's theorem, using the noetherian hypothesis to control the rational subsets. $\square$

---

## The Structure Sheaf and Analytic Adic Spaces

### The Structure Sheaf

**Definition.** Let $(A, A^+)$ be a Huber pair with $A$ complete. The **structure presheaf** $O_{\operatorname{Spa}(A, A^+)}$ assigns to a rational subset $R = R(f_1, \dots, f_n/g)$ the completion of the localisation

$$
A\Bigl[\tfrac{1}{g}\Bigr] = A\Bigl[\frac{f_1}{g}, \dots, \frac{f_n}{g}\Bigr]
$$

for the topology of the rational subset, namely the topology in which the denominators are inverted; the sections form a complete Huber ring, and the restriction maps are the evident continuous homomorphisms.

**Theorem (the sheaf property).** Let $(A, A^+)$ be a Huber pair with $A$ complete. Then the structure presheaf on $\operatorname{Spa}(A, A^+)$ is a sheaf for the analytic topology on the rational subsets: for every admissible covering by rational subsets and every compatible family of sections there is a unique global section. The stalks are the local rings $O_x$ with maximal ideal the functions of value $0$ at $x$, and the completion of the stalk at its maximal ideal is the **completed local ring** $\widehat{O_x}$, whose residue field is $\mathcal{H}(x)$, the completed residue field of the valuation.

**Proof.** The sheaf property is Huber's theorem; it is proved by reducing to the case of a Tate ring, where the rational subsets generate the topology and the sections can be computed by a Mittag–Leffler argument on the completions, and then treating the general case by a noetherian approximation. The description of the stalks is standard. The proof is quoted as a standard theorem. $\square$

**Definition.** An **affinoid adic space** is a space of the form $\operatorname{Spa}(A, A^+)$ for a complete Huber pair, with the analytic topology and the structure sheaf. A **locally adic space** is a topologically ringed space locally isomorphic to an affinoid adic space. An **adic space** in Huber's sense is a locally adic space satisfying a further "noetherian-like" hypothesis, or, in the general sense used here, any locally adic space; the article adopts the general convention and calls them all adic spaces. The space is **analytic** if all its points are analytic valuations.

**Proposition.** The affinoid adic spaces form a full subcategory of the category of adic spaces, and the structure sheaf of an affinoid space has global sections $A$ when $A$ is complete and the pair is of definition.

**Proof.** The first statement is immediate from the definition of local isomorphism; the second is the sheaf property applied to the covering by the whole space, whose ring of sections is the completion of $A$ at the topology, which is $A$ by completeness. $\square$

### Fibre Products and Morphisms

**Definition.** A **morphism of adic spaces** is a morphism of topologically ringed spaces which is local on the stalks and which pulls back rational subsets to rational subsets; equivalently, a morphism is a continuous map with a compatible continuous morphism of sheaves. A morphism is **affinoid** if it is locally of the form $\operatorname{Spa}(B, B^+) \to \operatorname{Spa}(A, A^+)$ induced by a continuous homomorphism $A \to B$.

**Theorem.** The category of adic spaces has fibre products, and the fibre product of affinoid spaces is the adic spectrum of the completed tensor product:

$$
\operatorname{Spa}(B, B^+) \times_{\operatorname{Spa}(A, A^+)} \operatorname{Spa}(C, C^+) = \operatorname{Spa}\bigl(B \widehat{\otimes}_A C, \ B^+ \widehat{\otimes}_{A^+} C^+\bigr),
$$

where $\widehat{\otimes}$ denotes the completion of the tensor product for the appropriate Huber topology.

**Proof.** The completed tensor product is the coproduct in the category of complete Huber pairs, and the universal property of the adic spectrum then gives the fibre product. The existence of the general fibre product follows by gluing the affine pieces; the details are standard. $\square$

---

## Comparison with the Earlier Geometries

### Rigid Analytic Geometry

**Theorem (rigid spaces as adic spaces).** Let $K$ be a complete non-Archimedean field and let $X$ be a rigid analytic space over $K$ in the sense of *Rigid Analytic Geometry*. Then there is an adic space $X^{\mathrm{ad}}$ over $\operatorname{Spa}(K, \mathcal{O})$ and a functorial isomorphism

$$
\{\text{rigid spaces over } K\} \xrightarrow{\ \sim\ } \{\text{adic spaces over } \operatorname{Spa}(K, \mathcal{O})\}
$$

in the quasi-compact and quasi-separated case, under which affinoid algebras correspond to complete Tate Huber rings of definition and the rigid G-topology corresponds to the analytic topology.

**Proof.** The functor is constructed affine-locally: a $K$-affinoid algebra $A$ corresponds to the Huber pair $(A, A^\circ)$ with $A^\circ$ the unit ball, and the points of $\operatorname{Spa}(A, A^\circ)$ are the continuous multiplicative seminorms, with the classical points among them. The comparison of the sheaf theories is Huber's theorem, using Tate's acyclicity on the rigid side. It is quoted as standard. $\square$

### Berkovich Spaces

**Theorem (Berkovich spaces as adic spaces).** Let $K$ be a complete non-Archimedean field. The **Berkovich spectrum** $M(A)$ of a $K$-affinoid algebra $A$ is the set of points of $\operatorname{Spa}(A, A^\circ)$ whose valuation takes values in $\mathbb{R}_{\geq 0}$, that is, the points with value group a subgroup of $\mathbb{R}_{>0}$; the Berkovich topology agrees with the analytic topology on this subset, and the completed residue fields $\mathcal{H}(x)$ agree.

**Proof.** A bounded multiplicative seminorm on $A$ is a continuous valuation whose value group may be taken to be a subgroup of $\mathbb{R}_{>0}$ after passing to an equivalent representative; the equivalence is the standard normalisation. The agreement of the topologies follows from the fact that the rational subsets are generated by the conditions $\lvert f \rvert \leq \lvert g \rvert$, which are exactly the conditions defining the Berkovich topology, and the agreement of the completed residue fields is immediate from the definitions. $\square$

**Remark.** The comparison shows exactly what is lost and gained in the passage from Berkovich to adic geometry: the adic spectrum contains points whose value groups are non-Archimedean and not embeddable in $\mathbb{R}_{>0}$, which are absent from the Berkovich space; and it contains the non-analytic points, which are the points coming from the formal geometry. Both are needed for the perfectoid theory.

### Formal Schemes

**Theorem (the adic generic fibre).** Let $\mathfrak{X}$ be a formal scheme locally of finite type over $\operatorname{Spf} R$ for a complete adic ring $R$ with a topologically nilpotent unit (equivalently, $R$ Tate). Then there is an adic space $\mathfrak{X}^{\mathrm{ad}}$ with the same underlying set of points as the rigid generic fibre of *Formal Schemes*, obtained by taking the adic spectrum of the Huber pairs of the affinoid localisations and gluing; the analytic points of $\mathfrak{X}^{\mathrm{ad}}$ are exactly the points of the rigid generic fibre $\mathfrak{X}_K$.

**Proof.** This is the adic form of Raynaud's theorem; the formal affine pieces $\operatorname{Spf} A$ give the Huber pairs $(A \otimes_R K, A^\circ)$ and the gluing is compatible with the formal gluing. The identification of the analytic points follows from the comparison with the rigid theory. It is quoted as standard. $\square$

**Remark.** The adic framework has a further advantage over both the rigid and the formal framework: it contains the analytic points and the non-analytic points in one object, and it has honest fibre products and a good theory of proper morphisms without the restriction to the quasi-compact case. This is why it is the language of perfectoid spaces.

---

## Examples

**Example (the adic unit disc).** Let $K$ be a complete non-Archimedean field. The adic unit disc is

$$
\mathbb{D}^{\mathrm{ad}} = \operatorname{Spa}(K\langle T\rangle, \mathcal{O}\langle T\rangle),
$$

a Tate affinoid adic space whose analytic points are the Berkovich points of the disc of *Berkovich Spaces* and whose non-analytic points are the "residue disc" points coming from the reduction. Its rational subsets $\lvert f \rvert \leq \lvert g \rvert$ give the Weierstrass, Laurent and rational domains of the rigid theory.

**Example (the adic affine and projective lines).** $\mathbb{A}^{1,\mathrm{ad}} = \bigcup_n \operatorname{Spa}(K\langle T/n\rangle, \mathcal{O}\langle T/n\rangle)$ with the analytic topology, and the **adic projective line** is glued from two copies along the open annulus; it is the adic space underlying the projective line, compact for the spectral topology, and its analytic points are the Berkovich projective line of *Berkovich Spaces*.

**Example (adic fields).** For a complete non-Archimedean field $K$ the space $\operatorname{Spa}(K, \mathcal{O})$ is a single point, the valuation of $K$; but the space $\operatorname{Spa}(K, \mathcal{O}_K)$ contains additional points when $K$ is not discretely valued, corresponding to the extensions of the valuation to the algebraic closure. In particular $\operatorname{Spa}(\mathbb{C}_p, \mathcal{O}_{\mathbb{C}_p})$ is a rich space with a point for each extension of the $p$-adic valuation, and this is the base of the perfectoid constructions.

**Example (the adic spectrum as a functor).** The constructions are functorial in the Huber pair: a continuous homomorphism $A \to B$ with $A^+ \to B^+$ induces a morphism $\operatorname{Spa}(B, B^+) \to \operatorname{Spa}(A, A^+)$, the map on points being the composition of a valuation with the homomorphism, and a $\mathbb{Z}$-algebra homomorphism of Huber pairs is adic if it is continuous and bounded. This functoriality is what makes adic spaces a category with the expected limits and colimits.

**Example (the perfectoid disc, anticipation).** The disc $\operatorname{Spa}(K\langle T^{1/p^\infty}\rangle, \cdots)$ with all $p$-power roots of $T$ adjoined is the standard example of a perfectoid affinoid space; its tilt is the disc over the tilt of $K$, and the tilting equivalence is not covered here.

---

## Summary

A **Huber ring** is a topological ring with an open subring of definition whose topology is $I$-adic for a finitely generated ideal of definition $I$; a Huber ring is **Tate** if it has a topologically nilpotent unit. A **continuous valuation** is a multiplicative map to a totally ordered group that is continuous for the topology, and the **adic spectrum** $\operatorname{Spa}(A, A^+)$ for a Huber pair is the set of equivalence classes of continuous valuations bounded by $1$ on the open integrally closed subring $A^+$. It carries two topologies: the **spectral topology**, compact and spectral in Hochster's sense, and the **analytic topology**, generated by the rational subsets $R(f_1, \dots, f_n/g)$, which is the topology used for geometry.

The **structure sheaf** assigns to a rational subset the completion of the localisation at the dividing element, and it is a sheaf for the analytic topology; the completions of the stalks have residue fields $\mathcal{H}(x)$ the completed residue fields of the points. An **affinoid adic space** is the adic spectrum of a complete Huber pair, a **locally adic space** is locally of this form, and the category has fibre products given by completed tensor products of Huber pairs. Rigid analytic spaces, Berkovich spaces and the generic fibres of formal schemes all embed in the category of adic spaces: a $K$-affinoid algebra $A$ corresponds to the pair $(A, A^\circ)$, the Berkovich points are the points with values in $\mathbb{R}_{>0}$, and the analytic points of the adic generic fibre of a formal scheme are the rigid generic fibre. The adic framework contains analytic and non-analytic points in a single object, and it is the setting of **perfectoid spaces**, whose tilting equivalence is taken up. The constructions use only the adic topology, the valuations and the algebraic geometry; the analysis on these spaces belongs to Part III.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$ | A Huber ring (f-adic ring) |
| $A_0$, $I$ | A ring of definition and an ideal of definition |
| $A^+$ | An open integrally closed subring, part of a Huber pair |
| $\operatorname{Spa}(A, A^+)$ | The adic spectrum |
| $\lvert \cdot \rvert$ | A continuous valuation |
| $\Gamma$ | Value group of a valuation |
| $\mathfrak{p}$ | Support $\{a : \lvert a \rvert = 0\}$ of a valuation |
| $R(f_1, \dots, f_n/g)$ | Rational subset $\{\lvert f_i \rvert \leq \lvert g \rvert \neq 0\}$ |
| $O_{\operatorname{Spa}(A, A^+)}$ | Structure sheaf of complete topological rings |
| $\mathcal{H}(x)$ | Completed residue field at a point |
| $\widehat{O_x}$ | Completed local ring at a point |
| $\mathbb{D}^{\mathrm{ad}}$, $\mathbb{A}^{1,\mathrm{ad}}$ | The adic unit disc and the adic affine line |
| $\mathcal{O}$, $\mathfrak{m}$, $k$ | Valuation ring, maximal ideal and residue field of $K$ |
| $A \widehat{\otimes}_B C$ | Completed tensor product of Huber rings |





## Further Reading

- Roland Huber, *Étale Cohomology of Rigid Analytic Varieties and Adic Spaces* (Vieweg, 1996), for the definition of adic spaces, the two topologies and the structure sheaf.
- Roland Huber, "A generalization of formal schemes and rigid analytic varieties", *Mathematische Zeitschrift* **217** (1994), 513–551, for the foundational theorems and the comparison with rigid and formal geometry.
- Peter Scholze, "Perfectoid spaces", *Publications Mathématiques de l'IHÉS* **116** (2012), 245–313, for the use of adic spaces in the perfectoid theory.
- Torsten Wedhorn, *Adic Spaces*, lecture notes (2019), for a systematic modern development with full proofs.
- Brian Conrad, "Several approaches to non-Archimedean geometry", in *$p$-adic Geometry* (American Mathematical Society, 2008), for a comparison of the rigid, Berkovich and adic approaches.
- Michael Temkin, "Introduction to Berkovich analytic spaces", in *Berkovich Spaces and Applications* (Springer, 2015), for the Berkovich side of the comparison.
- Kiran S. Kedlaya, *Sheaves, Stacks, and Shtukas* (lecture notes, 2013), for the sheaf theory on adic spaces and the route to perfectoid spaces.
