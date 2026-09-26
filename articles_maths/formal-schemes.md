
# __Formal Schemes__

## Introduction

A formal scheme is what a scheme becomes when the structure sheaf is allowed to take values in topological rings and the local models are formal spectra of **adic rings** rather than ordinary spectra of rings. The construction is the natural home of two closely related ideas. The first is completion: the completion of a scheme along a closed subscheme is not a scheme in general, because the completion of a local ring at its maximal ideal is not an algebraic localisation, but it is always a formal scheme, and it carries exactly the infinitesimal information along the subscheme. The second is degeneration: a family over the valuation ring of a local field has a generic fibre, which is a space over the field, and a special fibre, which is a space over the residue field, and the formal scheme is the object that remembers both and the way the second deforms into the first. Both ideas are used in the geometry of this Part: the rigid analytic spaces of *Rigid Analytic Geometry* arise as the generic fibres of formal schemes over the valuation ring, by Raynaud's theorem.

This article defines adic rings and their formal spectra, constructs the structure sheaf, states the definition of a formal scheme and of the locally noetherian one, treats ideals of definition and the reduction, and develops the two central technical theorems: the theorem on formal functions and formal GAGA. It then develops the deformation and completion examples, and closes with the precise relation to rigid analytic geometry. It assumes *Topological Rings and Fields* for the $I$-adic topology, the inverse limit and the completion of a ring; *Local Fields* for the valuation rings of a non-Archimedean field; and *Rigid Analytic Geometry* for the rigid spaces that the formal models describe. The analytic content of the theory — the theory of the integral, the limit and the measure — is Part III's; only the topology of the adic rings and the algebraic geometry of the formal spectra are used here. Throughout, $A$ is a commutative ring with identity, $I \subseteq A$ an ideal, and the $I$-adic topology on $A$ and the completion $\widehat{A} = \varprojlim_n A/I^n$ are those of *Topological Rings and Fields*. An adic ring is a topological ring in which the topology is $I$-adic for some ideal $I$.

---

## Adic Rings and the Formal Spectrum

### Adic Rings

**Definition.** A topological ring $A$ is **adic** if there is an ideal $I \subseteq A$, an **ideal of definition**, such that the sets $I^n$, $n \geq 0$, form a fundamental system of neighbourhoods of $0$. If $A$ is adic with ideal of definition $I$, then

**(AR1)** $A$ is **separated** if $\bigcap_{n \geq 0} I^n = 0$, and

**(AR2)** $A$ is **complete** if the natural map $A \to \varprojlim_n A/I^n$ is an isomorphism.

The **completion** of an adic ring is the complete adic ring $\widehat{A} = \varprojlim_n A/I^n$ with the inverse limit topology; the topology on $A$ depends only on the radical of an ideal of definition, since $\sqrt{I} = \sqrt{J}$ implies that the powers of $I$ and of $J$ are cofinal.

**Example ($\mathbb{Z}_p$ and $O$).** The ring $\mathbb{Z}_p$ is the $p$-adic completion of $\mathbb{Z}$, with ideal of definition $(p)$; the ring of integers $\mathcal{O}$ of a non-Archimedean local field is adic with ideal of definition $\mathfrak{m}$, and it is complete by *Local Fields*.

**Example (formal power series).** For any ring $B$ and any ideal $J \subseteq B$, the formal power series ring $B[[X_1, \dots, X_n]]$ with the $(J, X_1, \dots, X_n)$-adic topology is a complete adic ring whenever $B$ is $J$-adically complete. In particular $k[[X]]$ is adic and complete with ideal of definition $(X)$, and $\mathcal{O}[[X]]$ with the $(\mathfrak{m}, X)$-adic topology is the ring of the formal disc over $\mathcal{O}$.

**Example (the $I$-adic completion of a noetherian ring).** If $A$ is noetherian and $I \subseteq A$ an ideal, then $\widehat{A}$ is a complete noetherian adic ring with ideal of definition $I\widehat{A}$, and $\widehat{A}/I^n\widehat{A} \cong A/I^n$; this is the basic source of adic rings in algebraic geometry, and it is the content of the Krull intersection theorem and the Artin–Rees lemma for the noetherian case.

### The Formal Spectrum

**Definition.** Let $A$ be an adic ring with ideal of definition $I$. The **formal spectrum** $\operatorname{Spf} A$ is the set of **open prime ideals** of $A$, that is, the prime ideals $\mathfrak{p}$ containing $I$ (equivalently, containing $I^n$ for some $n$), equipped with the topology whose closed sets are the sets

$$
V(f) = \{\mathfrak{p} \in \operatorname{Spf} A : f \in \mathfrak{p}\}, \qquad f \in A .
$$

For $f \in A$ the **formal localisation** of $A$ at $f$ is

$$
A_{\{f\}} = \varprojlim_n (A_f / I^n A_f),
$$

the $I$-adic completion of the localisation $A_f$. The **structure sheaf** $O_{\operatorname{Spf} A}$ is the sheaf associated to the presheaf $D(f) \mapsto A_{\{f\}}$, where $D(f) = \operatorname{Spf} A \setminus V(f)$.

**Theorem.** Let $A$ be an adic ring with ideal of definition $I$. Then $(\operatorname{Spf} A, O_{\operatorname{Spf} A})$ is a topologically ringed space: it is a ringed space whose structure sheaf takes values in topological rings, the restriction maps are continuous, and for every open prime $\mathfrak{p}$ the stalk is the local ring $A_{\mathfrak{p}}$ completed at $\mathfrak{p}$, that is, $\varprojlim_n (A_{\mathfrak{p}}/\mathfrak{p}^n A_{\mathfrak{p}})$.

**Proof.** The set of open primes is the set of primes containing $I$; the topology generated by the $D(f)$ is the Zariski topology inherited from $\operatorname{Spec}(A/I)$ together with the extra open sets obtained by allowing $f \in A$, and the family $\{D(f)\}_{f \in A}$ is a basis closed under finite intersections because $D(f) \cap D(g) = D(fg)$. The presheaf is separated and satisfies the sheaf axiom because it is the inverse limit of the sheaves $D(f) \mapsto (A/I^n)_f$ on $\operatorname{Spec}(A/I^n)$, each of which is a sheaf, and an inverse limit of sheaves with surjective transition maps is a sheaf. The stalk computation is the standard one for the Zariski topology together with the completion. $\square$

**Definition.** A **formal scheme** is a topologically ringed space $(X, O_X)$ which is locally isomorphic to $(\operatorname{Spf} A, O_{\operatorname{Spf} A})$ for an adic ring $A$. It is **locally noetherian** if the rings $A$ may be taken noetherian; it is **adic** if it admits a global ideal of definition, that is, a sheaf of ideals $\mathcal{I} \subseteq O_X$ such that $\mathcal{I}^n$ form a fundamental system of neighbourhoods of $0$ at every point. A **morphism** of formal schemes is a morphism of topologically ringed spaces, that is, a continuous map together with a morphism of sheaves of topological rings which is continuous on sections.

**Remark.** A scheme is a formal scheme for the discrete topology: a ring with discrete topology is adic with ideal of definition $0$, and its formal spectrum is its spectrum. Thus the category of schemes embeds in the category of formal schemes as a full subcategory, and the theory below specialises to the usual theory of schemes when all the ideals of definition vanish. What is genuinely new is the case in which the ideal of definition is nontrivial, and the topology is not discrete.

---

## Ideals of Definition and the Reduction

### The Reduction

**Definition.** Let $(X, O_X)$ be a formal scheme and let $\mathcal{I} \subseteq O_X$ be a sheaf of ideals of definition. The **reduction** (or **special fibre**) of $X$ with respect to $\mathcal{I}$ is the closed subscheme

$$
X_0 = (X, O_X/\mathcal{I}) ,
$$

that is, the ordinary scheme whose structure sheaf is the quotient by the ideal of definition; the **thickenings** are the schemes $X_n = (X, O_X/\mathcal{I}^{n+1})$, so that $X_0$ is the first thickening and $X$ is the inverse limit of the $X_n$ in the category of formal schemes.

**Proposition.** Let $X$ be a locally noetherian formal scheme and let $\mathcal{I}$ be an ideal of definition. Then the reduction $X_0$ is a locally noetherian scheme, and the topological space of $X$ is that of $X_0$. If $X_0$ is of finite type over a field $k$, then $X$ is a formal deformation of $X_0$ over the adic ring in question in the sense that each thickening $X_n$ is a scheme over the appropriate Artinian quotient.

**Proof.** The topological space of a formal scheme is the set of open primes, and the open primes of $A$ are the primes of $A/I$; hence $X$ and $X_0$ have the same underlying topological space. Local noetherianity passes to quotients, and the structure of the thickenings is the statement that $O_X/\mathcal{I}^{n+1}$ is a sheaf of rings with nilpotents controlled by $\mathcal{I}$. $\square$

**Remark.** The choice of ideal of definition is not unique, but the reductions for two ideals of definition with the same radical differ by a nilpotent thickening, and all the invariants of $X$ that are constructed from the thickenings depend only on the formal scheme, not on the chosen ideal. This is the reason the definition of a formal scheme is formulated with a topology rather than with a fixed ideal.

### Coherent Sheaves

**Definition.** Let $X$ be a formal scheme. A sheaf of $O_X$-modules $\mathcal{F}$ is **coherent** if, locally on affine opens $\operatorname{Spf} A$, it is the sheaf associated to a finitely generated $A$-module; it is **complete** if moreover $\mathcal{F} = \varprojlim_n \mathcal{F}/\mathcal{I}^n\mathcal{F}$ for an ideal of definition $\mathcal{I}$.

**Theorem (Grothendieck's theorem on formal functions).** Let $f : X \to Y$ be a proper morphism of locally noetherian formal schemes, let $\mathcal{I} \subseteq O_Y$ be an ideal of definition and let $\mathcal{F}$ be a coherent $O_X$-module. Then for every $q \geq 0$ the sheaf $R^q f_*(\mathcal{F})$ is a coherent $O_Y$-module, and the natural map

$$
\bigl(R^q f_*(\mathcal{F})\bigr)^\wedge \longrightarrow \varprojlim_n R^q f_*\bigl(\mathcal{F} \otimes_{O_X} O_X/\mathcal{I}^n O_X\bigr)
$$

is an isomorphism; in particular the cohomology of $\mathcal{F}$ on the thickenings determines $R^q f_*(\mathcal{F})$.

**Proof.** The theorem is Grothendieck's theorem on formal functions, proved by reducing to the affine case and using the Artin–Rees lemma and the Mittag–Leffler condition on the inverse system of cohomology modules; the noetherian hypotheses make the cohomology modules finitely generated and the inverse systems satisfy the Mittag–Leffler condition on the relevant subquotients. It is quoted here as a standard theorem of the theory. $\square$

**Theorem (formal GAGA).** Let $A$ be a complete noetherian adic ring with ideal of definition $I$, let $X$ be a formal scheme proper over $\operatorname{Spf} A$, and let $X_0$ be its reduction. Then the functor

$$
\mathcal{F} \longmapsto \mathcal{F}_0 = \mathcal{F} \otimes_{O_X} O_{X_0}
$$

from coherent $O_X$-modules to coherent $O_{X_0}$-modules is fully faithful, its essential image is the coherent sheaves on $X_0$ that are "algebraisable" over $\operatorname{Spf} A$, and for a coherent $\mathcal{F}$ the module of global sections $\Gamma(X, \mathcal{F})$ is a finitely generated $A$-module. For $X$ projective over $\operatorname{Spf} A$ the functor is an equivalence between coherent $O_X$-modules and coherent $O_{X_0}$-modules equipped with a compatible $I$-adic completion.

**Proof.** This is Grothendieck's formal GAGA, the formal analogue of the GAGA theorem of Serre; the proof proceeds by the theorem on formal functions for the structure morphism, which gives the finiteness of the cohomology and the comparison with the thickenings, together with the algebraic GAGA applied to each thickening and a limit argument. It is quoted as standard. $\square$

**Remark.** Formal GAGA is the exact analogue for formal schemes of the rigid GAGA of *Rigid Analytic Geometry*, and the two are linked by Raynaud's theorem below: a coherent sheaf on a proper rigid space can be described on a formal model, and formal GAGA then compares its cohomology with that of the reduction. This is one of the standard routes from the analytic to the algebraic geometry of a degeneration.

---

## Completions and Formal Models

### Completion along a Closed Subscheme

**Definition.** Let $X$ be a scheme and $Y \subseteq X$ a closed subscheme with ideal sheaf $\mathcal{I}_Y$. The **formal completion of $X$ along $Y$** is the formal scheme

$$
\widehat{X}_{/Y} = \bigl(Y, \varprojlim_n O_X/\mathcal{I}_Y^{\,n}\bigr),
$$

whose underlying topological space is $Y$ and whose structure sheaf is the inverse limit of the structure sheaves of the infinitesimal neighbourhoods of $Y$ in $X$.

**Theorem (universal property of the completion).** Let $X$ be a scheme, $Y \subseteq X$ a closed subscheme and $\widehat{X}_{/Y}$ the formal completion. Then for every formal scheme $Z$ over $X$ whose image lies in $Y$, there is a unique morphism $Z \to \widehat{X}_{/Y}$ over $X$. Consequently the completion is the universal formal scheme over $X$ supported on $Y$.

**Proof.** The morphism $Z \to X$ has image in $Y$, so on structure sheaves it factors through $O_X/\mathcal{I}_Y^{\,n}$ for every $n$ by the continuity of the morphism and the nilpotence of $\mathcal{I}_Y$ on the image; passing to the inverse limit gives the morphism to the completion. Uniqueness is the uniqueness of the induced maps on the quotients. $\square$

**Example (completion at a point).** Let $X$ be a smooth curve over a field $k$ and let $Y = \{p\}$ be a closed point. Then $\widehat{X}_{/Y} = \operatorname{Spf} \widehat{O}_{X,p}$, where $\widehat{O}_{X,p} \cong k[[t]]$ is the completion of the local ring at $p$, and the formal scheme is the **formal disc** around $p$. If $k$ is the residue field of a non-Archimedean field $K$ with valuation ring $\mathcal{O}$ and uniformiser $t$, the same object with $\mathcal{O}[[t]]$ in place of $k[[t]]$ is the formal model of the rigid unit disc.

**Example (completion along a divisor).** Let $X$ be a smooth surface over a field and let $D \subseteq X$ be a smooth divisor. Then $\widehat{X}_{/D}$ has reduction $D$ and records the first-order and higher neighbourhoods of $D$ in $X$; for a degeneration of a curve over a disc, this is precisely the formal neighbourhood that controls the limit mixed structure.

**Example (the $p$-adic formal projective line).** Let $\widehat{\mathbb{P}}^1$ be the completion of $\mathbb{P}^1_\mathbb{Z}$ along its special fibre over a prime $p$. Then $\widehat{\mathbb{P}}^1$ is a formal scheme over $\operatorname{Spf}\mathbb{Z}_p$ whose reduction is $\mathbb{P}^1_{\mathbb{F}_p}$ and whose generic fibre is the rigid projective line $\mathbb{P}^{1,\mathrm{rig}}_{\mathbb{Q}_p}$ of *Rigid Analytic Geometry*. The same construction with the other prime ideals of $\mathbb{Z}$ produces the formal models used in the theory of rigid curves.

### Formal Models of Rigid Spaces

**Theorem (Raynaud; the formal side).** Let $K$ be a complete non-Archimedean field with valuation ring $\mathcal{O}$, and let $X$ be a quasi-compact and quasi-separated rigid analytic space over $K$. Then there is a formal scheme $\mathfrak{X}$ of finite type over $\operatorname{Spf}\mathcal{O}$ whose **generic fibre** $\mathfrak{X}_K$ — obtained by replacing the structure sheaf $O_{\mathfrak{X}}$ with $O_{\mathfrak{X}} \otimes_\mathcal{O} K$ on the same underlying space — is isomorphic to $X$. Two formal models of $X$ differ by an **admissible blow-up**, that is, by a blow-up along a sheaf of ideals of definition, and the category of rigid spaces is the localisation of the category of formal $\mathcal{O}$-schemes of finite type at the admissible blow-ups.

**Proof.** The existence of a formal model is proved by choosing an admissible affinoid covering of $X$, taking the formal spectra of the rings of definition of the affinoid algebras, and gluing; the generic fibre is identified with the rigid space by comparing the algebras of the covering. The statement about blow-ups is the statement that the generic fibre is unchanged by an admissible blow-up, and the localisation statement is Raynaud's theorem itself. It is quoted here as standard; the rigid statement was given in *Rigid Analytic Geometry*. $\square$

**Definition.** A formal model $\mathfrak{X}$ is **semi-stable** (or **polystable**) if its reduction $X_0$ is a divisor with normal crossings, and **strictly semi-stable** if in addition the components are smooth and the intersections are transversal. The **generic fibre** of a semi-stable model is the basic object of the theory of degenerations, and the **skeleton** of the rigid space retracts onto the dual graph of $X_0$, as in *Berkovich Spaces*.

**Example (the Tate curve).** Let $q \in K^\times$ with $\lvert q \rvert < 1$, let $v$ be the valuation normalised by $v(\pi) = 1$, and put $n = v(q)$. Then there is a formal scheme $\mathfrak{X}$ over $\operatorname{Spf}\mathcal{O}$, obtained by gluing a cyclically ordered chain of $n$ copies of the formal projective line and identifying the two ends with the $q$-adic identification, whose reduction is a cycle of $n$ rational curves and whose generic fibre $\mathfrak{X}_K$ is the **Tate curve** $K^\times/q^{\mathbb{Z}}$. It is the standard example of a formal model with a reduction of type $I_n$, the elliptic curve having split multiplicative reduction. The construction shows that a formal model can encode a rigid space whose reduction is not smooth, and it is the standard degeneration of an elliptic curve.

**Example (formal deformations of the affine line).** The formal scheme $\operatorname{Spf}\mathcal{O}[[X]]$ has reduction $\mathbb{A}^1_k$ and generic fibre the rigid closed unit disc of *Rigid Analytic Geometry*; the Weierstrass and Tate parameters of that disc are the formal parameters of the model. This is the simplest instance of the dictionary between the formal and the rigid theory, and it underlies the treatment of the disc and its subdomains.

---

## Summary

An **adic ring** is a topological ring whose topology is given by the powers of an ideal of definition $I$; it is complete when $A \cong \varprojlim_n A/I^n$. The **formal spectrum** $\operatorname{Spf} A$ is the set of open prime ideals with the Zariski topology, equipped with the structure sheaf whose sections on $D(f)$ are the $I$-adic completion of the localisation $A_f$; it is a topologically ringed space with stalks the completed local rings. A **formal scheme** is a topologically ringed space locally isomorphic to a formal spectrum, and it is locally noetherian when the local rings may be taken noetherian. The category of schemes embeds fully in the category of formal schemes via the discrete topology.

An **ideal of definition** $\mathcal{I}$ on a formal scheme determines its **reduction** (special fibre) $X_0 = (X, O_X/\mathcal{I})$ and the thickenings $X_n$; the underlying topological space is that of $X_0$. **Coherent** $O_X$-modules are locally finitely generated and **complete** when they equal the inverse limit of their quotients. Grothendieck's **theorem on formal functions** says that for a proper morphism of locally noetherian formal schemes the higher direct images of a coherent sheaf are coherent and are computed as the inverse limit of the cohomology of the thickenings, and **formal GAGA** identifies the coherent modules on a proper formal scheme with the algebraisable coherent modules on its reduction together with a compatible completion.

The **formal completion** $\widehat{X}_{/Y}$ of a scheme along a closed subscheme is the universal formal scheme over $X$ supported on $Y$; it is the formal disc near a point, the formal neighbourhood of a divisor, and the $p$-adic formal projective line when applied to $\mathbb{P}^1_\mathbb{Z}$ along its special fibre. By **Raynaud's theorem**, every quasi-compact and quasi-separated rigid analytic space is the generic fibre of a formal $\mathcal{O}$-scheme of finite type, two models differing by an admissible blow-up, and the rigid category is the localisation of the formal category at those blow-ups. Semi-stable models, the Tate curve and the formal model of the unit disc are the standard examples. The constructions use only the $I$-adic topology, the inverse limit and the completion of *Topological Rings and Fields*; the analytic theory belongs to Part III.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$ | A commutative adic ring |
| $I$ | An ideal of definition of $A$ |
| $\widehat{A} = \varprojlim_n A/I^n$ | The $I$-adic completion |
| $\operatorname{Spf} A$ | The formal spectrum, the set of open prime ideals |
| $A_{\{f\}} = \varprojlim_n (A_f/I^nA_f)$ | Formal localisation at $f$ |
| $O_{\operatorname{Spf} A}$ | Structure sheaf of topological rings |
| $X$, $O_X$ | A formal scheme and its structure sheaf |
| $\mathcal{I}$ | A sheaf of ideals of definition |
| $X_0 = (X, O_X/\mathcal{I})$ | Reduction (special fibre) |
| $X_n = (X, O_X/\mathcal{I}^{n+1})$ | Thickenings |
| $\widehat{X}_{/Y}$ | Formal completion of $X$ along the closed subscheme $Y$ |
| $\mathcal{F}$, $R^q f_*$ | Coherent module and higher direct images |
| $\mathfrak{X}$, $\mathfrak{X}_K$ | A formal $\mathcal{O}$-model and its generic fibre |
| $\mathcal{O}$, $\mathfrak{m}$, $k$ | Valuation ring, maximal ideal and residue field of the base field |
| $q$, $n = v(q)$ | Tate parameter with $\lvert q \rvert < 1$ and the length of the reduction cycle |

## Further Reading

- Alexander Grothendieck, *Éléments de Géométrie Algébrique III*, *Publications Mathématiques de l'IHÉS* **11** (1961) and **17** (1963), for the formal spectrum, the theorem on formal functions and formal GAGA.
- Robin Hartshorne, *Algebraic Geometry* (Springer, 1977), Chapter II and III, for the formal completion and the theorem on formal functions in the scheme-theoretic setting.
- Michel Raynaud, "Géométrie analytique rigide d'après Tate, Kiehl, …", *Mémoires de la Société Mathématique de France* **39–40** (1974), 319–327, for formal models and the generic fibre.
- Siegfried Bosch, *Lectures on Formal and Rigid Geometry* (Springer, 2014), for a systematic development of adic rings, formal schemes and their rigid generic fibres.
- Lucien Illusie, "Déformations de groupes de Barsotti–Tate", in *Séminaire sur les pinceaux arithmétiques* (Astérisque **127**, 1985), for formal deformations and their applications.
- Pierre Deligne and Michael Rapoport, "Les schémas de modules de courbes elliptiques", in *Modular Functions of One Variable II* (Springer, 1973), for formal models and degenerations of curves.
- Gerd Faltings and Ching-Li Chai, *Degeneration of Abelian Varieties* (Springer, 1990), for semi-stable models, Tate curves and the formal theory of degenerations.
