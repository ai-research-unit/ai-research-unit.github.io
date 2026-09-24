
# __Presheaves and Sheaves__

## Introduction

A **sheaf** is the mathematical device that records, on a topological space, which local data can be glued. Its two axioms say that a function defined on a space can be reconstructed from its restrictions to the members of an open cover, and that two functions agreeing on every member of such a cover are equal; a presheaf is the weaker structure in which the restriction maps exist but the gluing is not required. Every sheaf is a presheaf, and every presheaf has a best approximation by a sheaf, its **sheafification**; the passage from a presheaf to its sheafification is the precise form of the statement that the local data determine the glueable part of the global data.

The purpose of this article is to set up the language for the whole of the present Part. The sheaf theory that follows — sheaf cohomology, Čech cohomology, derived functors, the de Rham complex and the sheaves of algebraic geometry — is all read on the definitions given here, and the notation of this article is held fixed for the other articles of the category. Three features of the presentation should be stressed at the outset.

First, the **category of values** matters and is stated every time. A sheaf is a sheaf *of sets*, or *of groups*, or *of abelian groups*, or *of rings*, or *of $R$-modules* for a commutative ring $R$, and the sheaf condition is imposed in that category; the gluing of functions is a gluing of values, and the identification of two local sections requires that the values be elements of a set. The corpus's default base is the commutative ring, and the default coefficients for the cohomological constructions that follow are abelian groups or modules; where a construction needs the values to form an abelian category, the category of sheaves of abelian groups (or of $\mathcal{O}_X$-modules) is named explicitly.

Second, the **two generalisations are not this article's**. Sheaves on a Grothendieck site, and the descent theory of sheaves along a cover in a general topology, are the subject of the companion articles *Sheaves on Sites* and *Descent Theory* of Part I, where the categorical machinery of *Categories* and *Homological Algebra* is available; the topological instance, in which the site is the poset of open sets of a topological space with the coverings given by open covers, is what is developed here. The derived functor theory that turns the global sections of a sheaf into cohomology is Part I's *Derived Functors*; its topological reading lies outside this article.

Third, the **analytic constructions are deferred**. The sheaf of smooth functions on a manifold, the sheaf of differential forms and the sheaf of solutions of a differential equation are standard examples; the first two are used, with the notions of smooth map and differential form taken from the *Differential Forms and Stokes' Theorem* and *Fibre Bundles, Connections and Curvature*, and anything requiring completeness of a space of functions, a limit of a sequence of functions or a measure belongs to Part III.

## Presheaves

Let $X$ be a topological space, so that the open subsets of $X$ form a partially ordered set $\mathrm{Op}(X)$ under inclusion, regarded as a category with one arrow $V \to U$ whenever $V \subseteq U$.

**Definition.** Let $\mathcal{C}$ be a category. A **presheaf on $X$ with values in $\mathcal{C}$** is a contravariant functor $\mathcal{F} : \mathrm{Op}(X)^{\mathrm{op}} \to \mathcal{C}$. Explicitly, it consists of an object $\mathcal{F}(U)$ of $\mathcal{C}$ for every open $U \subseteq X$, and a morphism $\rho^U_V = \mathcal{F}(V \hookrightarrow U) : \mathcal{F}(U) \to \mathcal{F}(V)$ for every inclusion $V \subseteq U$ — the **restriction map** — subject to $\rho^U_U = \mathrm{id}$ and $\rho^V_W \circ \rho^U_V = \rho^U_W$ for $W \subseteq V \subseteq U$. A morphism of presheaves $\varphi : \mathcal{F} \to \mathcal{G}$ is a natural transformation; that is, a family of morphisms $\varphi_U : \mathcal{F}(U) \to \mathcal{G}(U)$ commuting with all restrictions: $\rho^U_V \circ \varphi_U = \varphi_V \circ \rho^U_V$ for $V \subseteq U$.

The presheaves on $X$ with values in $\mathcal{C}$ form the functor category $\mathcal{C}^{\mathrm{Op}(X)^{\mathrm{op}}}$, written $\mathrm{PSh}(X,\mathcal{C})$; when $\mathcal{C}$ is the category of abelian groups this is an abelian category, with kernels and cokernels computed open by open: $(\ker\varphi)(U) = \ker\varphi_U$ and $(\operatorname{coker}\varphi)(U) = \operatorname{coker}\varphi_U$, and similarly for images, direct sums and the rest. This is the first place where the values matter, and it is the last place in the article where exactness is automatic.

**Notation.** For $\mathcal{F}$ a presheaf of sets and $U$ open, an element $s \in \mathcal{F}(U)$ is a **section of $\mathcal{F}$ over $U$**, and its restriction $\rho^U_V(s)$ is written $s|_V$. The sections over $X$ are the **global sections**, and $\mathcal{F}(X)$ is also written $\Gamma(X,\mathcal{F})$ with $\Gamma(X,-)$ the **global sections functor**. For a fixed $R$, an $R$-module-valued presheaf is a presheaf of $R$-modules, and $\mathrm{PSh}(X,R)$ denotes the abelian category of presheaves of $R$-modules on $X$.

**Example (the constant presheaf).** Let $A$ be an abelian group. The **constant presheaf** is $\underline{A}^{\mathrm{pre}}(U) = A$ for every open $U \subseteq X$, with all restriction maps the identity. It is a presheaf of abelian groups; it is a sheaf when $X$ is connected, since the overlap graph of a cover of a connected space is connected, and its sheafification is the sheaf of locally constant functions with values in $A$, the **constant sheaf** $\underline{A}$, for which $\underline{A}(U) = A^{\pi_0(U)}$.

**Example (the failure of the constant presheaf).** Let $X = \{p,q\}$ be a two-point discrete space and let $A$ be an abelian group with an element $a \neq 0$. The cover $X = U \cup V$ with $U = \{p\}$, $V = \{q\}$ has empty overlap, so the matching condition is vacuous and every pair $(s_U,s_V) \in A\times A$ is a matching family; but $\underline{A}^{\mathrm{pre}}(X) = A$, so only the pairs with equal entries come from a global section. The presheaf is not a sheaf, and its sheafification has $\underline{A}^{+}(X) = A\times A$, the value of the constant sheaf at $X$.

**Example (functions).** Let $\mathcal{C}(U)$ be the set of continuous real-valued functions on $U$, and $\mathcal{C}^\infty(U)$ the set of smooth real-valued functions on $U$ when $X$ is a smooth manifold; the restriction maps are the ordinary restrictions of functions. Both are presheaves of commutative rings, and both satisfy the sheaf condition of the next section. The presheaf of *bounded* continuous functions on a non-compact space is a presheaf but not a sheaf; the subpresheaf of the **constant** functions of the sheaf of continuous functions is not a sheaf in general either, since two constant functions on disjoint open pieces need not extend to a single constant function on their union.

**Example (sections of a bundle).** Let $p: E \to X$ be a continuous map and let $\Gamma_p(U)$ be the set of continuous sections $s: U \to E$ with $p \circ s = \mathrm{id}_U$. Restriction of a section to a smaller open set makes $\Gamma_p$ a presheaf of sets, and it is a sheaf precisely because a section is a function: continuity is local, and two sections agreeing on each member of a cover agree on the union. The comrade *Fibre Bundles, Connections and Curvature* uses this presheaf throughout, and the sheaf of sections of a vector bundle is the prototype of a locally free sheaf of modules.

## The Sheaf Condition

**Definition.** A presheaf $\mathcal{F}$ of sets on $X$ — more generally, with values in a category in which the required limits exist — is a **sheaf** if for every open $U \subseteq X$, every open cover $U = \bigcup_{i \in I} U_i$ and every family of sections $s_i \in \mathcal{F}(U_i)$ with

$$
s_i|_{U_i \cap U_j} = s_j|_{U_i \cap U_j} \qquad \text{for all } i,j \in I,
$$

there is a unique $s \in \mathcal{F}(U)$ with $s|_{U_i} = s_i$ for all $i$. The two clauses are the **existence** and the **uniqueness** of the gluing, and they are independent: a presheaf may satisfy either without the other.

**Proposition (the equalizer form).** A presheaf $\mathcal{F}$ of sets is a sheaf if and only if for every open $U$ and every open cover $\{U_i\}_{i \in I}$ of $U$ the diagram

$$
\mathcal{F}(U) \longrightarrow \prod_{i \in I}\mathcal{F}(U_i) \rightrightarrows \prod_{(i,j) \in I \times I} \mathcal{F}(U_i \cap U_j)
$$

is an equalizer, where the two maps are $(s_i) \mapsto (s_i|_{U_i\cap U_j})$ and $(s_i) \mapsto (s_j|_{U_i\cap U_j})$. If the values lie in an abelian category, the same statement holds with the equalizer replaced by the exactness of

$$
0 \to \mathcal{F}(U) \to \prod_i \mathcal{F}(U_i) \to \prod_{i,j}\mathcal{F}(U_i\cap U_j),
$$

the second map being $(s_i) \mapsto \bigl(s_i|_{U_i\cap U_j} - s_j|_{U_i\cap U_j}\bigr)$.

*Proof.* Uniqueness of $s$ is exactly the injectivity of the first map, i.e. the statement that a section whose restrictions to all $U_i$ vanish is zero; existence is exactly the statement that a matching family lies in the image. The additive form is the equality $s_i|_{U_i\cap U_j} = s_j|_{U_i\cap U_j}$ rewritten. $\square$

**Remark.** It suffices to check the sheaf condition for covers of $U$ by two open sets, and, when $X$ has a basis $\mathcal{B}$ of open sets closed under finite intersections, to check it for covers of members of $\mathcal{B}$ by members of $\mathcal{B}$: the values on a basis determine the sheaf up to canonical isomorphism, as recorded below. The point is that the condition is a condition on all covers, but it is a *local* condition in each variable separately, so it can be tested on a basis and the general case is recovered by the transitivity of covering.

**Example (the failure of the sheaf condition).** Let $X = \mathbb{R}$ and let $\mathrm{Bd}(U)$ be the set of bounded continuous real-valued functions on $U$. The cover $\mathbb{R} = \bigcup_{n\geq1}(-n,n)$ admits the matching family given by the restrictions of the identity function, each bounded, but the identity function is not bounded; the existence clause of the sheaf condition fails. The sheafification of $\mathrm{Bd}$ is the sheaf of locally bounded continuous functions, which for $\mathbb{R}$ is the sheaf of all continuous functions.

**Example (the sheaf of continuous functions).** The presheaf $\mathcal{C}$ of continuous real-valued functions is a sheaf: continuity is a local condition, so a matching family of continuous functions glues to a unique continuous function. Thus a subsheaf of a sheaf need not be a sheaf unless it is closed under gluing, and the bounded functions form a *subpresheaf* of the sheaf of continuous functions.

**Definition.** Let $\varphi : \mathcal{F} \to \mathcal{G}$ be a morphism of sheaves of sets. It is a **monomorphism** if $\varphi_U$ is injective for every $U$. It is a **surjection** if for every $U$ and every $t \in \mathcal{G}(U)$ there is an open cover $U = \bigcup_{i\in I} U_i$ and sections $s_i \in \mathcal{F}(U_i)$ with $\varphi_{U_i}(s_i) = t|_{U_i}$; for a morphism of sheaves of abelian groups this is the same as being an epimorphism of the abelian category. A **subsheaf** is a subobject of $\mathcal{F}$ in $\mathrm{Sh}(X)$, and a **quotient sheaf** is a quotient object. With these definitions a morphism of sheaves of abelian groups is a surjection exactly when it is surjective on stalks, as shown below; it is *not* required to be surjective on sections, and this is the origin of the whole cohomological theory.

## Stalks and Germs

**Definition.** Let $\mathcal{F}$ be a presheaf of sets on $X$ and $x \in X$. The **stalk** of $\mathcal{F}$ at $x$ is the colimit

$$
\mathcal{F}_x = \varinjlim_{x \in U} \mathcal{F}(U)
$$

over the open neighbourhoods $U$ of $x$, ordered by reverse inclusion. An element of $\mathcal{F}_x$ is a **germ** at $x$, represented by a pair $(U,s)$ with $x \in U$ and $s \in \mathcal{F}(U)$, two representatives $(U,s)$ and $(V,t)$ defining the same germ if and only if there is an open $W$ with $x \in W \subseteq U\cap V$ and $s|_W = t|_W$. The germ of $s$ at $x$ is written $s_x$.

**Theorem (stalk functor).** The assignment $\mathcal{F} \mapsto \mathcal{F}_x$, and on morphisms $\varphi \mapsto \varphi_x = \varinjlim_U \varphi_U$, defines a functor $\mathrm{PSh}(X) \to \mathcal{C}$ which is **exact** — the stalk is a filtered colimit of the values, and filtered colimits are exact in the categories of sets and of modules — and which is **conservative on sheaves**, though not on presheaves: a morphism of *sheaves* is an isomorphism if and only if every induced map of stalks is one. It has the following properties:

1. For a morphism of sheaves of sets, $\varphi$ is a monomorphism if and only if $\varphi_x$ is injective for every $x$; $\varphi$ is an epimorphism if and only if $\varphi_x$ is surjective for every $x$; and $\varphi$ is an isomorphism if and only if $\varphi_x$ is an isomorphism for every $x$.
2. If $\mathcal{F}$ is a sheaf then it is determined up to canonical isomorphism by the stalks together with the following description of its sections: for open $U$, $\mathcal{F}(U)$ is the set of families $(s_x)_{x\in U}$ with $s_x \in \mathcal{F}_x$ such that every $x \in U$ has a neighbourhood $V \subseteq U$ and a section $s' \in \mathcal{F}(V)$ with $s'_y = s_y$ for all $y \in V$.
3. The germ relation is functorial: $\varphi_x(s_x) = (\varphi_U(s))_x$ for every representative $(U,s)$.

*Proof.* Exactness of the filtered colimit functor in the second variable is the exactness of filtered colimits in the category of sets and of modules. For (1), if $\varphi_x$ is injective for every $x$ and $\varphi_U(s) = 0$, then $\varphi_x(s_x) = 0$ for every $x \in U$, so $s_x = 0$ for every $x$, and a section of a sheaf all of whose germs vanish is zero by the uniqueness axiom applied to a cover by small neighbourhoods; the converse is immediate. If $\varphi_x$ is surjective for every $x$ and $t \in \mathcal{G}(U)$, choose for each $x \in U$ a neighbourhood $U_x$ and $s_x \in \mathcal{F}(U_x)$ with $\varphi(s_x) = t|_{U_x}$; the uniqueness part of the sheaf axiom for $\mathcal{G}$ shows that the $s_x$ agree on overlaps after refining, and the existence part glues them. (2) is the reconstruction of a sheaf from its stalks, and uses both parts of the sheaf axiom. $\square$

**Theorem (the étalé space of a sheaf).** Let $\mathcal{F}$ be a sheaf of sets on $X$ and let

$$
L(\mathcal{F}) = \bigsqcup_{x\in X}\mathcal{F}_x, \qquad \pi : L(\mathcal{F}) \to X,\quad \pi(s_x) = x,
$$

with the topology in which a basis of open sets is given by the sets $U_s = \{s_x : x \in U\}$ for $U$ open and $s \in \mathcal{F}(U)$. Then $\pi$ is a local homeomorphism — an **étalé space** over $X$ — and the functor $\mathcal{F} \mapsto L(\mathcal{F})$ is an equivalence between the category of sheaves of sets on $X$ and the category of local homeomorphisms to $X$, with inverse the functor sending $p : E \to X$ to the sheaf of continuous sections of $p$. The stalk of the sections of $p$ at $x$ is the fibre $p^{-1}(x)$, and the equivalence is natural in $X$ and compatible with the sheaf of continuous sections of the previous example.

*Proof sketch.* Each $\pi|_{U_s}$ is a homeomorphism onto $U$, so $\pi$ is a local homeomorphism; conversely, if $p : E \to X$ is a local homeomorphism, the presheaf of continuous sections is a sheaf, since continuity is local. The two constructions are inverse up to canonical isomorphism: the canonical map $\mathcal{F}(U) \to \Gamma(U, L(\mathcal{F}))$, $s \mapsto (x \mapsto s_x)$, is an isomorphism by the reconstruction of a sheaf from its stalks, and the map $E \to L(\Gamma(-))$, $e \mapsto$ the germ of a local section through $e$, is a homeomorphism. $\square$

**Remark.** The étalé space is the reason the gluing axiom may be replaced by a topology on the total space of germs, and the reason the constant sheaf $\underline{A}$ is the sheaf of sections of the projection $X \times A \to X$ with $A$ discrete: its sections over a connected open set are, canonically, the elements of $A$.

## Sheafification and the Category of Sheaves

**Theorem (sheafification).** Let $\mathcal{F}$ be a presheaf of sets on $X$. There is a sheaf $\mathcal{F}^{+}$, the **sheafification** (or **associated sheaf**) of $\mathcal{F}$, together with a morphism of presheaves $\eta : \mathcal{F} \to \mathcal{F}^{+}$, such that for every sheaf $\mathcal{G}$ and every morphism of presheaves $\varphi : \mathcal{F} \to \mathcal{G}$ there is a unique morphism of sheaves $\bar\varphi : \mathcal{F}^{+} \to \mathcal{G}$ with $\bar\varphi \circ \eta = \varphi$:

$$
\operatorname{Hom}_{\mathrm{PSh}}(\mathcal{F}, \mathcal{G}) \cong \operatorname{Hom}_{\mathrm{Sh}}(\mathcal{F}^{+}, \mathcal{G}).
$$

The sheafification has the same stalks as $\mathcal{F}$, $\mathcal{F}^{+}_x \cong \mathcal{F}_x$ for every $x$, and is the unique sheaf with this property up to canonical isomorphism; explicitly, $\mathcal{F}^{+}$ is the sheaf of sections of the étalé space $L(\mathcal{F}) = \bigsqcup_x \mathcal{F}_x$. The functor $\mathcal{F} \mapsto \mathcal{F}^{+}$ is left adjoint to the inclusion $\mathrm{Sh}(X) \hookrightarrow \mathrm{PSh}(X)$, and for a sheaf $\mathcal{G}$ it has the further universal property that a morphism of presheaves $\mathcal{F} \to \mathcal{G}$ factors uniquely through the canonical morphism to the image sheaf.

*Proof.* The adjunction is the statement that $\eta$ is the unit of an adjunction whose right adjoint is the inclusion; the existence of the left adjoint follows from the Freyd adjoint functor theorem applied to the inclusion of sheaves, which preserves limits, or, constructively, by taking the sheaf of sections of the étalé space and observing that the map from $\mathcal{F}$ to that sheaf has the required universal property: any $\varphi : \mathcal{F} \to \mathcal{G}$ with $\mathcal{G}$ a sheaf induces a map of étalé spaces $L(\mathcal{F}) \to L(\mathcal{G})$, hence a map of their sheaves of sections. The stalk computation is the definition of $L(\mathcal{F})$. $\square$

**Theorem (exactness properties).** Let $\varphi : \mathcal{F} \to \mathcal{G}$ be a morphism of sheaves of abelian groups on $X$.

1. The kernel of a morphism of sheaves, computed in presheaves, is a sheaf: if $s$ is a section of $\mathcal{F}$ over $U$ with $\varphi(s) = 0$, then $\varphi(s|_V) = 0$ for every $V \subseteq U$, so the sections killed by $\varphi$ satisfy the sheaf condition with the restriction maps inherited from $\mathcal{F}$, and $\ker$ in $\mathrm{PSh}$ and in $\mathrm{Sh}$ agree.
2. The cokernel in $\mathrm{Sh}$ is the sheafification of the presheaf cokernel, $(\operatorname{coker}_{\mathrm{Sh}}\varphi) = (\operatorname{coker}_{\mathrm{PSh}}\varphi)^{+}$, and the image sheaf is $(\operatorname{im}\varphi)^{+}$.
3. The inclusion $\mathrm{Sh}(X) \hookrightarrow \mathrm{PSh}(X)$ is left exact but not right exact, and the sheafification functor is exact.
4. The category $\mathrm{Sh}(X,R)$ of sheaves of $R$-modules is an abelian category in which the stalk functor is exact; the category $\mathrm{Sh}(X,\mathbf{Ab})$ is a Grothendieck category, has a generator and all colimits, and has enough injectives.

*Pro.* (1) A subsheaf of a sheaf is a sheaf: the kernel of $\varphi$ is the subsheaf of $\mathcal{F}$ whose sections over $U$ are the sections killed by $\varphi_U$, and the gluing of such sections is again killed. (2) The presheaf cokernel need not satisfy the sheaf condition, so it is replaced by its sheafification, which has the required universal property by adjunction; the same applies to the image, and the two are related by the exact sequence $0 \to \ker \to \mathcal{F} \to \operatorname{im} \to 0$ and the isomorphism $\operatorname{im}\cong \mathcal{F}/\ker$ in $\mathrm{Sh}$. (3) The inclusion preserves all limits, hence kernels; it does not preserve cokernels, as (2) shows, and the sheafification functor is left exact because it is a left adjoint, and right exact because it preserves stalks and exactness of stalks detects exactness of morphisms of sheaves. (4) See *Homological Algebra* of Part I for abelian categories and Grothendieck categories, andfor the existence of injectives and its consequence, the definition of $H^i(X,\mathcal{F})$. $\square$

**Example (the exponential sequence and the failure of right exactness).** On the topological space $X = \mathbb{C}^*$ with the sheaf $\mathcal{O}$ of continuous complex-valued functions and the sheaf $\mathcal{O}^*$ of continuous nowhere-zero complex-valued functions, the exponential sequence of sheaves

$$
0 \to \underline{\mathbb{Z}} \to \mathcal{O} \xrightarrow{\ \exp\ } \mathcal{O}^* \to 0
$$

is exact — $\exp$ is locally surjective — but the map on global sections $\exp: \mathcal{O}(X) \to \mathcal{O}^*(X)$ is not surjective, since the identity function of $\mathbb{C}^*$ has no continuous logarithm. The cokernel of $\exp$ on sections is therefore nonzero, and it is the first Čech cohomology of $\underline{\mathbb{Z}}$, ascomputes; this is the standard illustration of why the exactness of a sequence of sheaves must be tested on stalks and not on global sections.

## Operations on Sheaves

### Restriction, Direct and Inverse Image

**Definition.** Let $f : X \to Y$ be continuous. For a sheaf $\mathcal{F}$ on $X$, the **direct image** (or **pushforward**) $f_*\mathcal{F}$ is the sheaf on $Y$ with $(f_*\mathcal{F})(V) = \mathcal{F}(f^{-1}(V))$ for $V \subseteq Y$ open, restrictions induced by those of $\mathcal{F}$. For a sheaf $\mathcal{G}$ on $Y$, the **inverse image** (or **pullback**) $f^{-1}\mathcal{G}$ is the sheafification of the presheaf $U \mapsto \varinjlim_{V \supseteq f(U)}\mathcal{G}(V)$; equivalently it is the sheaf of sections of the fibre product $X\times_Y L(\mathcal{G}) \to X$.

**Theorem (adjunction and stalks).** For continuous $f : X \to Y$ and sheaves $\mathcal{F}$ on $X$, $\mathcal{G}$ on $Y$, there is a natural bijection

$$
\operatorname{Hom}_X(f^{-1}\mathcal{G}, \mathcal{F}) \cong \operatorname{Hom}_Y(\mathcal{G}, f_*\mathcal{F}),
$$

so that $f^{-1}$ is left adjoint to $f_*$. Moreover $(f^{-1}\mathcal{G})_x \cong \mathcal{G}_{f(x)}$ for every $x \in X$, and $f^{-1}$ is exact; the functor $f_*$ is left exact and preserves limits, but not colimits in general.

*Proof.* A morphism $f^{-1}\mathcal{G} \to \mathcal{F}$ is determined by its effect on sections over open $U \subseteq X$, which factors through the colimit defining $f^{-1}$ and hence gives maps $\mathcal{G}(V) \to \mathcal{F}(f^{-1}(V))$ for $V \supseteq f(U)$; assembling them defines a morphism $\mathcal{G} \to f_*\mathcal{F}$, and the two constructions are inverse. The stalk formula follows from the description by the fibre product, and exactness of $f^{-1}$ from the stalk formula and the exactness of the stalk functor. $\square$

**Definition.** For $f: X \to Y$ and a sheaf $\mathcal{F}$ on $X$, the **support** is the closed set $\operatorname{Supp}\mathcal{F} = \{x \in X: \mathcal{F}_x \neq 0\}$, for sheaves of abelian groups. For an open immersion $j: U \hookrightarrow X$, the **extension by zero** $j_!\mathcal{F}$ is the sheafification of the presheaf $V \mapsto \mathcal{F}(V)$ for $V \subseteq U$ and $V \mapsto 0$ otherwise; it is the subsheaf of $j_*\mathcal{F}$ of sections with support in $U$. The **skyscraper sheaf** at $x \in X$ with value $A$ is $(i_x)_*A$ for $i_x: \{x\} \hookrightarrow X$ the inclusion, with stalk $A$ at $x$ and $0$ elsewhere; it is the typical example of a sheaf that is not constant, and the basic building block of the flasque resolutions.

### Sheaves of Modules and Ringed Spaces

**Definition.** A **ringed space** is a pair $(X,\mathcal{O}_X)$ with $X$ a topological space and $\mathcal{O}_X$ a sheaf of commutative rings with unit on $X$ — the **structure sheaf** — whose restriction maps are ring homomorphisms; it is a **locally ringed space** if every stalk $\mathcal{O}_{X,x}$ is a local ring. A sheaf of $\mathcal{O}_X$-modules is a sheaf $\mathcal{F}$ of abelian groups together with a multiplication $\mathcal{O}_X(U)\times\mathcal{F}(U) \to \mathcal{F}(U)$ for every open $U$, compatible with restrictions. The category $\mathcal{O}_X\text{-}\mathbf{Mod}$ is abelian, and the constructions $\mathcal{F}\otimes_{\mathcal{O}_X}\mathcal{G}$, $\mathcal{H}om_{\mathcal{O}_X}(\mathcal{F},\mathcal{G})$ and the direct and inverse images of modules are defined by sheafification of the corresponding presheaf constructions.

**Example.** The sheaf $\mathcal{O}_X$ of continuous real-valued functions on a topological space, or of smooth functions on a manifold, is the **structure sheaf** of a ringed space; the sheaf of sections of a vector bundle is a locally free $\mathcal{O}_X$-module of finite rank, and conversely by the discussion of *Fibre Bundles, Connections and Curvature* every locally free module of finite rank arises this way when $X$ is paracompact. The structure sheaves of algebraic geometry and the coherent sheaves of modules over them are not covered here.

### Sheaves on a Basis

**Theorem (descent to a basis).** Let $X$ have a basis $\mathcal{B}$ of open sets closed under finite intersections. The restriction functor from sheaves on $X$ to the data of objects $\mathcal{F}(B)$ for $B \in \mathcal{B}$ and restriction maps for inclusions of basis elements is fully faithful; a datum extends to a sheaf if and only if it satisfies the sheaf condition for covers of members of $\mathcal{B}$ by members of $\mathcal{B}$, and the extension is unique up to canonical isomorphism. Consequently, sheaf-theoretic statements that are local in the Zariski topology of a ring — the topology generated by the distinguished open sets $D(f) = \{\mathfrak{p}: f \notin \mathfrak{p}\}$ of a commutative ring, with $D(f)\cap D(g) = D(fg)$ — may be verified on the distinguished opens.

*Proof.* Given such a datum, define for open $U$ the set of matching families on covers of $U$ by members of $\mathcal{B}$ modulo the equivalence of common refinement; the axioms are verified directly, and the two constructions are inverse up to canonical isomorphism. $\square$

## Summary

A presheaf on a topological space $X$ with values in a category $\mathcal{C}$ is a contravariant functor on the poset of open sets; a sheaf is a presheaf in which sections over the members of an open cover that agree on overlaps glue uniquely. For sheaves with values in an abelian category the sheaf condition is the exactness of a two-term sequence of products of section sets, which makes the sheaf condition itself a diagrammatic statement and separates existence from uniqueness. The stalk at a point is the filtered colimit of sections over neighbourhoods, the stalk functor is exact and conservative, and a morphism of sheaves is a monomorphism or epimorphism exactly when it is so on every stalk, though it need not be surjective on global sections; the étalé space establishes the equivalence between sheaves of sets and local homeomorphisms over $X$, and identifies the constant sheaf with the sheaf of sections of $X\times A$ for discrete $A$.

Every presheaf has a sheafification, left adjoint to the inclusion of sheaves and having the same stalks; sheafification is exact, the inclusion is left exact and not right exact, and the cokernel and image in the category of sheaves are the sheafified presheaf cokernel and image. The category of sheaves of $R$-modules is abelian with exact stalk functors, and is a Grothendieck category with enough injectives — the property that makes the derived functor definition of sheaf cohomology available. Continuous maps induce the adjoint pair of direct and inverse image functors, with the stalk formula $(f^{-1}\mathcal{G})_x\cong\mathcal{G}_{f(x)}$ and exactness of $f^{-1}$; restriction, extension by zero, support and the skyscraper sheaf complete the list of elementary operations. A sheaf of modules over a structure sheaf is the notion of a sheaf on a ringed space, and the data of a sheaf may be tested and even reconstructed on any basis closed under finite intersections.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{Op}(X)$ | the poset of open subsets of $X$, as a category |
| $\mathcal{F}, \mathcal{G}$ | presheaves or sheaves on $X$; $\mathcal{F}(U) = \Gamma(U,\mathcal{F})$ |
| $\rho^U_V : \mathcal{F}(U)\to\mathcal{F}(V)$, $s\|_V$ | restriction map and restriction of a section |
| $\Gamma(X,-)$ | global sections functor; $\Gamma(X,\mathcal{F}) = \mathcal{F}(X)$ |
| $\mathrm{PSh}(X,\mathcal{C})$, $\mathrm{Sh}(X,\mathcal{C})$ | categories of presheaves and sheaves with values in $\mathcal{C}$ |
| $\underline{A}^{\mathrm{pre}}$, $\underline{A}$ | constant presheaf and constant sheaf with value $A$ |
| $\mathcal{F}_x$, $s_x$ | stalk at $x$ and germ of a section |
| $L(\mathcal{F}) = \bigsqcup_x\mathcal{F}_x$ | étalé space of $\mathcal{F}$; local homeomorphism over $X$ |
| $\mathcal{F}^{+}$, $\eta : \mathcal{F}\to\mathcal{F}^{+}$ | sheafification (associated sheaf) and its unit |
| $\ker,\operatorname{coker},\operatorname{im}$ | sheaf kernel, cokernel (sheafified), image sheaf |
| $f_*\mathcal{F}$, $f^{-1}\mathcal{G}$ | direct and inverse image; $f^{-1}\dashv f_*$ |
| $\operatorname{Supp}\mathcal{F}$ | support of a sheaf of abelian groups |
| $j_!\mathcal{F}$, $(i_x)_*A$ | extension by zero; skyscraper sheaf at $x$ |
| $\mathcal{O}_X$, $\mathcal{O}_X\text{-}\mathbf{Mod}$ | structure sheaf of a ringed space; its modules |
| $\mathcal{H}om_{\mathcal{O}_X}$, $\otimes_{\mathcal{O}_X}$ | sheaf hom and tensor product of modules |





## Further Reading

- Roger Godement, *Topologie algébrique et théorie des faisceaux* (Hermann, 1958), for the foundational treatment of sheaves, stalks and flasque sheaves.
- Jean-Pierre Serre, *Faisceaux algébriques cohérents* (Annals of Mathematics 61, 1955), for the sheaf-theoretic method in algebraic geometry.
- Alexander Grothendieck, *Sur quelques points d'algèbre homologique* (Tohoku Mathematical Journal 9, 1957), for abelian categories, the existence of injectives and the foundations of sheaf cohomology.
- Robin Hartshorne, *Algebraic Geometry* (Springer, 1977), for the sheaf theory of schemes and coherent sheaves, in the form used by the later articles of this Part.
- Saunders Mac Lane and Ieke Moerdijk, *Sheaves in Geometry and Logic* (Springer, 1992), for the categorical treatment of sheaves, the associated sheaf and the étalé space.
- Masaki Kashiwara and Pierre Schapira, *Sheaves on Manifolds* (Springer, 1990), for the topological and analytic refinements of the theory, including the constructions deferred here to Part III.
