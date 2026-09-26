
# __Topological Groups__

## Introduction

A topological group is a group with a topology for which the group operations are continuous — the combination of the two structures treated separately in *Transformation Groups* and in *Topological Spaces*, *Metric, Uniform and Complete Spaces*. The combination is far more rigid than either structure alone: the topology is determined by a neighbourhood base at the identity, it is automatically homogeneous, the group carries two natural uniform structures, and the quotient by a subgroup inherits both a group structure and a topology. Continuity of multiplication then forces a strong interplay between algebra and topology, so that compactness and connectedness become statements about subgroups, and the counting and averaging arguments of *Group Actions and Structure* acquire topological analogues.

This article develops that interplay: the axioms and their first consequences, the uniformity and the completion, subgroups and quotients, the standard separation and connectedness facts, compactness and local compactness, the profinite case, the Haar measure that integration on a group requires, and the structure theory of locally compact abelian groups with its Pontryagin duality. The final subject is Pontryagin duality, which identifies the category of locally compact abelian groups with its own dual and is the topological counterpart of the duality between a finite abelian group and its character group. The base ring $R$ is a commutative ring with identity $1 \neq 0$ and $F$, $K$ are fields as usual; the groups here are written multiplicatively unless abelian, and the identity is $e$. No physics is invoked.

## The Axioms and Their Consequences

### Definition

**Definition.** A **topological group** is a group $G$ with a topology such that both structure maps

$$
G \times G \to G, \quad (g, h) \mapsto gh, \qquad G \to G, \quad g \mapsto g^{-1},
$$

are continuous, the product carrying the product topology. Equivalently, the single map $G \times G \to G$, $(g, h) \mapsto g h^{-1}$, is continuous.

The equivalence is immediate: the map $g h^{-1}$ is continuous when multiplication and inversion are, and conversely $g h = g (h^{-1})^{-1}$ and $h^{-1} = e h^{-1}$ recover both maps from it.

**Example (the additive groups).** $\mathbb{R}$, $\mathbb{C}$, $\mathbb{Q}$, $\mathbb{Z}$ and $\mathbb{K}^n$ with addition and the usual topology are topological groups, abelian and written additively. The circle group $S^1 = \{z \in \mathbb{C} : |z| = 1\}$ with complex multiplication and the subspace topology is a compact topological group, isomorphic to $\mathbb{R}/\mathbb{Z}$.

**Example (matrix groups).** The general linear group $GL_n(\mathbb{K})$ with the topology induced from $\mathbb{K}^{n^2}$ is a topological group, locally compact, and non-compact for $n \geq 1$; the orthogonal group $O(n)$, the special orthogonal group $SO(n)$ and the unitary group $U(n)$ are compact topological groups. These are treated.

**Example (discrete and trivial).** Every group with the discrete topology is a topological group, and every group with the trivial topology is one. A discrete group is compact exactly when it is finite, and locally compact always.

**Example (function groups).** The set of all functions $X \to G$ from a set to a topological group, with pointwise multiplication and the product topology, is a topological group; the continuous functions $X \to G$, when $X$ is a topological space and $G$ is a topological group, form a subgroup in the subspace topology.

### Translations, Homogeneity, and the Local Base

**Definition.** For $g \in G$ the **left translation** $L_g$, the **right translation** $R_g$ and the **inner automorphism** $\operatorname{Ad}_g$ are

$$
L_g(h) = gh, \qquad R_g(h) = hg, \qquad \operatorname{Ad}_g(h) = g h g^{-1}.
$$

**Theorem.** Left and right translations are homeomorphisms of $G$; the inversion map is a homeomorphism; the inner automorphism $\operatorname{Ad}_g$ is a homeomorphism and an automorphism of $G$. Consequently $G$ is **homogeneous**: for any $g, h \in G$ there is a homeomorphism carrying $g$ to $h$, and every local property of $G$ at one point holds at every point.

**Proof.** $L_g$ is continuous with continuous inverse $L_{g^{-1}}$, since multiplication is continuous; likewise for $R_g$. Inversion is its own inverse and is continuous; $\operatorname{Ad}_g = L_g \circ R_{g^{-1}}$ is a homeomorphism and is conjugation, hence an automorphism. For homogeneity use $L_{h g^{-1}}$. $\square$

Homogeneity is the reason a topological group is described by data at $e$ alone.

**Definition.** A family $\mathcal{N}$ of neighbourhoods of $e$ is a **neighbourhood base at the identity** if every neighbourhood of $e$ contains a member of $\mathcal{N}$.

**Theorem (the local-base axioms).** Let $\mathcal{N}$ be the family of neighbourhoods of $e$ in a topological group $G$. Then

**(a)** for every $U \in \mathcal{N}$ there is $V \in \mathcal{N}$ with $V V \subseteq U$;

**(b)** for every $U \in \mathcal{N}$ there is $V \in \mathcal{N}$ with $V^{-1} \subseteq U$;

**(c)** for every $U \in \mathcal{N}$ and $g \in G$ there is $V \in \mathcal{N}$ with $g V g^{-1} \subseteq U$, and $\mathcal{N}$ is invariant under inversion as a family: $U \in \mathcal{N} \iff U^{-1} \in \mathcal{N}$;

**(d)** if $x \in U \in \mathcal{N}$ there is $V \in \mathcal{N}$ with $x V \subseteq U$.

Conversely, given a group $G$ and a filter base $\mathcal{N}$ of subsets containing $e$ satisfying (a), (b) and (c), the sets $g V$ with $g \in G$, $V \in \mathcal{N}$ form a base for a topology making $G$ a topological group with $\mathcal{N}$ as a neighbourhood base at $e$.

**Proof.** (a), (b), (d) are the continuity of multiplication at $(e,e)$, of inversion at $e$ and of multiplication at $(e,x)$ respectively. For (c), $\operatorname{Ad}_g$ is a homeomorphism fixing $e$, so the image of a neighbourhood of $e$ is a neighbourhood of $e$. The converse is a standard verification that the generated topology is compatible with the operations; the axioms are exactly what the continuity conditions at the identity require. $\square$

**Corollary (topology from the identity).** A topological group is determined by the neighbourhood base at $e$; a subgroup is open if and only if it contains a neighbourhood of $e$, and an open subgroup is closed.

**Proof.** The sets $gV$ form a base, so the local base determines the topology. An open subgroup $H$ has all its cosets $gH$ open, so $G \setminus H = \bigcup_{g \notin H} gH$ is open and $H$ is closed. $\square$

The corollary is used constantly: in a topological group, a subgroup that is open is automatically closed, so there is no "open but not closed" subgroup, in contrast with the general topological case.

### Separation

**Theorem.** For a topological group $G$ the following are equivalent: $G$ is $T_0$; $G$ is $T_1$; $\{e\}$ is closed; $G$ is Hausdorff; $G$ is Tychonoff. In particular the weakest separation hypothesis implies all the others.

**Proof.** The set $N = \overline{\{e\}} = \bigcap \{U : U \text{ a neighbourhood of } e\}$ is a subgroup: it is contained in every neighbourhood of $e$, and if $x, y \in N$ and $U$ is a neighbourhood of $e$, choose $V$ with $V V \subseteq U$; then $x \in V$, $y \in V$ give $xy \in U$, and $x^{-1} \in U$ by the corresponding property of a neighbourhood base. Hence if $G$ is $T_0$ then $N = \{e\}$: for $x \neq e$ in $N$, $T_0$ provides an open set containing exactly one of $e, x$; if it contains $e$ it is a neighbourhood of $e$ and so contains $x$, a contradiction, and if it contains $x$ but not $e$, then translating it to $x^{-1}U$, a neighbourhood of $e$, gives $x \in x^{-1}U$ and $x^{-1} \in x^{-1}U$, whence $x = x^{-1}u$ and $x^{-1} = x^{-1}u'$ with $u, u' \in U$, so $u' = e$, contradicting $e \notin U$. Thus $\{e\}$ is closed and $G$ is $T_1$. Now let $g \neq h$ in $G$; then $gh^{-1} \neq e$, so there is a neighbourhood $U$ of $e$ with $gh^{-1} \notin U$; choose a symmetric $V$ with $V V \subseteq U$, and then $Vg$ and $Vh$ are disjoint neighbourhoods of $g$ and $h$, since a common point $vg = v'h$ would give $v^{-1}v' = gh^{-1} \in V^{-1}V = VV \subseteq U$. So $G$ is Hausdorff, and Tychonoff follows because a Hausdorff topological group is uniformisable, as the next section shows. $\square$

**Remark.** Thus in a topological group the weakest of the separation hypotheses implies all the rest up to Tychonoff, because homogeneity propagates the separation of $e$ from any other point everywhere. This is a general phenomenon: a Hausdorff topological group is Tychonoff and uniformisable, so its topology is described by a family of continuous left-invariant pseudometrics, and it is normal as soon as it is locally compact or metrisable.

## Uniformity and Completion

### The Left and Right Uniformities

Since the topology is homogeneous, the neighbourhoods of $e$ give uniform closeness everywhere.

**Definition.** The **left uniformity** $\mathcal{U}_L$ on $G$ has as a base the sets

$$
E_U = \{(g, h) : g^{-1} h \in U\}, \qquad U \text{ a neighbourhood of } e,
$$

and the **right uniformity** $\mathcal{U}_R$ has as a base the sets $F_U = \{(g, h) : g h^{-1} \in U\}$. The **two-sided uniformity** is the supremum of the two.

**Theorem.** $\mathcal{U}_L$ and $\mathcal{U}_R$ are uniform structures on $G$, both inducing the given topology; left translations are uniformly continuous for $\mathcal{U}_L$, right translations for $\mathcal{U}_R$, and inversion is a uniform isomorphism from $(G, \mathcal{U}_L)$ to $(G, \mathcal{U}_R)$. The sets $E_U$ with $U$ ranging over a neighbourhood base at $e$ form a base; symmetry uses $U \cap U^{-1}$ and the composition axiom uses the local-base axiom (a).

**Proof.** Each of the axioms (U1)–(U3) of a uniform structure is one of the local-base axioms at $e$: the diagonal is contained in $E_U$ because $g^{-1}g = e \in U$; the symmetry of the neighbourhood base under inversion gives $E_U^{-1} = E_{U^{-1}}$; and $E_V \circ E_V \subseteq E_U$ whenever $V V \subseteq U$. The uniform topology is the given topology because $E_U[g] = gU$ is a basic neighbourhood of $g$, and the sets $gU$ with $U$ a neighbourhood of $e$ form a base for the topology by the results of the previous section. For the statements about translations, $L_{g_0}$ is uniformly continuous because $(L_{g_0}(g), L_{g_0}(h)) \in E_U$ as soon as $(g, h) \in E_U$, the relation $g^{-1}h = (g_0 g)^{-1}(g_0 h)$ being translation-invariant on the left; right translations are uniformly continuous for the right uniformity for the same reason. Inversion carries $E_U$ to $F_U$, since $(g, h) \in E_U$ means $g^{-1}h \in U$ and then $(g^{-1}, h^{-1})$ satisfies $g^{-1}(h^{-1})^{-1} = g^{-1}h \in U$, that is $(g^{-1}, h^{-1}) \in F_U$; so inversion is a uniform isomorphism between the two uniformities. $\square$

**Remark.** The two uniformities coincide exactly when the identity has a neighbourhood base of **conjugation-invariant** sets: when every neighbourhood $U$ of $e$ contains a neighbourhood $V$ of $e$ with $g V g^{-1} \subseteq V$ for all $g \in G$, equivalently when the group carries a bi-invariant uniformity. This condition is strictly stronger than unimodularity. A locally compact group with an invariant neighbourhood base is unimodular, since its Haar measure is then invariant under every inner automorphism; the converse fails, the standard witness being the **Heisenberg group** of upper unitriangular $3 \times 3$ real matrices, in the coordinates

$$
\begin{pmatrix} 1 & x & z \\ 0 & 1 & y \\ 0 & 0 & 1 \end{pmatrix},
$$

where conjugation by $(a, b, c)$ sends $(x, y, z)$ to $(x, y, z - bx + ay)$, so no bounded neighbourhood of $e$ is conjugation-invariant; but the group is nilpotent and hence unimodular. Coincidence of the two uniformities is therefore a genuinely stronger condition than the vanishing of the modular function of the next section.

### The Completion and Its Structure

**Definition.** A topological group is **complete** if it is complete in the two-sided uniformity, the finest of the three; equivalently (Raĭkov) if it is closed in every Hausdorff topological group containing it as a subgroup. Completeness in the left uniformity is equivalent to completeness in the right one, since inversion interchanges the two and carries Cauchy filters to Cauchy filters, and it implies completeness in the two-sided uniformity; the three notions agree for locally compact Hausdorff groups.

**Theorem.** Every topological group $G$ has a completion $\hat G$: a complete Hausdorff topological group containing $G$ as a dense subgroup, the neighbourhood filter of the identity of $\hat G$ being generated by the closures of the corresponding neighbourhoods in $G$; it is unique up to a topological isomorphism fixing $G$.

**Proof.** Take the completion of $(G, \mathcal{U}_L \vee \mathcal{U}_R)$ as a uniform space, the two-sided uniformity being the one for which both multiplication and inversion are uniformly continuous, and let $\hat G$ be the set of Cauchy filters modulo the equivalence that identifies two filters when their intersection generates a filter (equivalently, when they have the same minimal Cauchy filter); define multiplication by the condition that if $\mathcal{F} \to g$ and $\mathcal{H} \to h$ then $\mathcal{F}\mathcal{H} \to gh$. The operation is well defined because the product of two-sided Cauchy filters is two-sided Cauchy and the product of filters meeting every neighbourhood of $e$ meets every neighbourhood of $gh$; associativity and the group axioms pass to the completion by continuity and density, inversion extends similarly, and the resulting group has the required universal property, since a uniformly continuous homomorphism into a complete Hausdorff group extends by the universal property of the uniform completion and preserves products by continuity. $\square$

**Example.** $\mathbb{Q}$ with the usual topology is a non-complete topological group whose completion is $\mathbb{R}$; $\mathbb{Z}$ with the $p$-adic topology completes to the additive group $\mathbb{Z}_p$, and $\mathbb{Q}$ with the $p$-adic topology to $\mathbb{Q}_p$.

**Corollary.** If $G$ is complete then every Cauchy filter in the two-sided uniformity converges; for $G$ Hausdorff a subgroup $H$ is complete exactly when it is closed in $G$, and a locally compact Hausdorff group is complete.

**Proof.** The statement about subgroups is the corresponding statement for uniform spaces, closedness being with respect to the ambient uniformity. For local compactness, a Cauchy filter in a locally compact group contains a set of compact closure, and a compact space is complete, so the filter has a cluster point which is a limit. $\square$

## Subgroups and Quotients

### Subgroups

**Definition.** A **topological subgroup** of $G$ is a subgroup $H$ with the subspace topology, making $H$ a topological group in its own right. The **closure** $\overline H$ of a subgroup is a subgroup. The set $\bigcap\{U : U \text{ a neighbourhood of } e\} = \overline{\{e\}}$ is a closed normal subgroup, and it is $\{e\}$ exactly when $G$ is $T_1$, hence in particular whenever $G$ is Hausdorff.

**Theorem.** If $H \leq G$ then $\overline H \leq G$; if $H$ is normal then $\overline H$ is normal. If $H$ is a subgroup and $U$ is open in $G$ with $H \cap U \neq \emptyset$, then $H \cap U$ is open in $H$.

**Proof.** For the closure of a subgroup, let $a, b \in \overline H$; the map $(x, y) \mapsto x y^{-1}$ is continuous and carries $H \times H$ into $H$, so it carries the closure of $H \times H$ into $\overline H$; since $\overline H \times \overline H \subseteq \overline{H \times H}$ in the product topology of a uniformisable space, $ab^{-1} \in \overline H$. Normality: conjugation by $g$ is a homeomorphism, so $\overline{gHg^{-1}} = g \overline H g^{-1}$. The last claim is the definition of the subspace topology. $\square$

**Theorem.** The connected component $G_e$ of the identity is a closed normal subgroup containing every connected subgroup that contains $e$, and $G/G_e$ is totally disconnected. The quotient $G/G_e$ is the **component group** of $G$.

**Proof.** If $A, B$ are connected and contain $e$, then $AB$ is connected as the continuous image of $A \times B$ under multiplication, and $A^{-1}$ is connected as the continuous image of $A$ under inversion; hence $G_e G_e^{-1} \subseteq G_e$ and $G_e$ is a subgroup. It is closed because components are closed, and normal because $\operatorname{Ad}_g$ is a homeomorphism fixing $e$, so it preserves the component of $e$. A connected subset of $G/G_e$ has connected preimage in $G$ by the quotient map, which contains $G_e$ and is therefore contained in $G_e$; so the only connected subsets are singletons. $\square$

**Example.** In $GL_n(\mathbb{R})$ the identity component is $GL_n(\mathbb{R})^+$, the matrices of positive determinant, and the component group is $C_2$. In $O(n)$ the identity component is $SO(n)$ and the component group is $C_2$. For a discrete group the identity component is $\{e\}$, so the group is totally disconnected, and its open subgroups are all the subgroups, so the intersection of the open subgroups is trivial and the theorem is consistent.

**Definition.** A subgroup $H$ is **discrete** if the subspace topology on $H$ is discrete, and **dense** if $\overline H = G$.

**Theorem.** A subgroup $H$ of a Hausdorff group $G$ is discrete if and only if there is a neighbourhood $U$ of $e$ with $H \cap U = \{e\}$, and then $H$ is closed in $G$.

**Proof.** If $H$ is discrete then $\{e\}$ is open in $H$, so $H \cap U = \{e\}$ for some open $U$ in $G$; conversely that condition makes every singleton $H \cap hU$ open in $H$. For closedness, choose a symmetric neighbourhood $V$ of $e$ with $V V \subseteq U$, and suppose $x \in \overline H$; then there is a net $h_\alpha \in H$ with $h_\alpha \to x$. By continuity of multiplication at $(x, x^{-1})$ the products $h_\alpha h_\beta^{-1}$ lie in $U$ for all $\alpha, \beta$ large enough, and they lie in $H$; hence $h_\alpha h_\beta^{-1} = e$ for such $\alpha, \beta$, so the net is eventually constant and its limit $x$ lies in $H$. $\square$

### Quotients

**Definition.** Let $H \leq G$. The **coset space** $G/H$ is the set of left cosets with the quotient topology, $G$ acting on it transitively; the **quotient group** $G/H$ exists when $H \trianglelefteq G$, with the quotient topology and the induced group structure.

**Theorem.** The quotient map $\pi : G \to G/H$ is continuous and open. If $H \trianglelefteq G$ then $G/H$ is a topological group, and the quotient topology is the unique topology making it one with $\pi$ continuous. If $H$ is closed and $G$ is Hausdorff, then $G/H$ is Hausdorff.

**Proof.** $\pi$ is continuous by definition of the quotient topology, and open because for an open $W \subseteq G$ the set $\pi^{-1}(\pi(W)) = WH = \bigcup_{h \in H} Wh$ is open, so $\pi(W)$ is open; here $WH$ is open as a union of translates of $W$. If $H$ is normal, the group operations on $G/H$ are continuous because they are induced by the continuous operations on $G$ through the quotient map, using the characteristic property of the quotient topology twice. For Hausdorffness, $\pi(g) \neq \pi(h)$ means $h^{-1}g \notin H$; since $H$ is closed, $W = \{v : v h^{-1} g \notin H\}$ is an open neighbourhood of $e$, and choosing a symmetric $U$ with $U U \subseteq W$ the images of $gU$ and $hU$ are disjoint: a common point $gu = hu'$ would give $g^{-1}h = u u'^{-1} \in U U^{-1} = U U \subseteq W$, so that $e = (g^{-1}h)h^{-1}g \notin H$ by the defining property of $W$, a contradiction. $\square$

**Corollary.** The quotient $G/H$ is Hausdorff exactly when $H$ is closed in $G$; if $H$ is not closed then $G/H$ is not even $T_1$, since $\overline{\{e_H\}} = \overline H/H$.

**Proof.** If $G/H$ is Hausdorff then $\{e_H\}$ is closed, and $\pi^{-1}(\{e_H\}) = H$ is closed by continuity. The converse is the theorem, and the description of the closure of the identity coset follows because $\pi(\overline H) \subseteq \overline{\pi(H)} = \{e_H\}$. $\square$

**Theorem (first isomorphism).** Let $\varphi : G \to K$ be a continuous homomorphism of topological groups with $K$ Hausdorff. Then $\ker \varphi$ is a closed normal subgroup, and $\varphi$ induces a continuous injective homomorphism $\overline\varphi : G/\ker\varphi \to K$ with image $\operatorname{im}\varphi$; the induced map $\overline\varphi$ is an isomorphism of topological groups onto $\operatorname{im}\varphi$ exactly when $\varphi$ is open as a map onto its image.

**Proof.** The kernel is the preimage of the closed set $\{e_K\}$, hence closed, and is normal as in the abstract case. The induced map is a continuous bijection onto the image because $\pi^{-1}(\ker\varphi) = \ker\varphi$ makes $\overline\varphi$ well defined and injective. If $\varphi$ is open onto its image, then so is the induced bijection, and the characteristic property of the quotient topology makes it a homeomorphism; conversely a topological isomorphism onto the image forces $\varphi = \overline\varphi \circ \pi$ to be open, since $\pi$ is open. $\square$

**Example.** $\mathbb{R}/\mathbb{Z} \cong S^1$ as topological groups; $\mathbb{Z} \subseteq \mathbb{R}$ is a discrete closed subgroup with compact quotient. The quotient of $\mathbb{R}^n$ by a lattice $\Lambda \cong \mathbb{Z}^n$ is the $n$-torus $T^n = \mathbb{R}^n/\mathbb{Z}^n$.

## Connectedness, Compactness and Local Compactness

### Connectedness

**Theorem.** If $G$ is connected then every neighbourhood of $e$ generates $G$. Conversely, if $G$ is locally compact and every neighbourhood of $e$ generates $G$, then $G$ is connected. If $G$ is locally compact, then the identity component $G_e$ is the intersection of the open subgroups of $G$. A quotient of a connected group is connected, and the product of connected groups is connected.

**Proof.** Let $U$ be a neighbourhood of $e$; replacing it by its interior and then by $U \cap U^{-1}$ we may suppose it open and symmetric. Then $\langle U \rangle = \bigcup_{n \geq 1} U^n$ is open, and it is closed because its complement is a union of cosets of the subgroup $\langle U \rangle$, each a translate of the open set $\langle U \rangle$; so if $G$ is connected, $\langle U \rangle = G$. Conversely, let $G$ be locally compact and suppose that every neighbourhood of $e$ generates $G$; were $G$ disconnected, the component group $G/G_e$ would be a nontrivial locally compact totally disconnected group, so by van Dantzig's theorem a neighbourhood $W \neq G/G_e$ of the identity coset would contain a compact open subgroup $K_0 \subseteq W$ proper in $G/G_e$, and the preimage $H$ of $K_0$ in $G$ would be a proper open subgroup; then $H$ is a neighbourhood of $e$ with $\langle H \rangle = H \neq G$, a contradiction, so $G$ is connected. For the statement on the identity component, each open subgroup is closed and contains $G_e$, so $G_e$ is contained in their intersection. Conversely, $G/G_e$ is totally disconnected and locally compact, so by van Dantzig's theorem its identity has a neighbourhood base of compact open subgroups; pulling these back along $G \to G/G_e$ gives open subgroups of $G$ whose intersection is $G_e$. The quotient and product statements are the general topological statements. $\square$

**Theorem.** A topological group is locally connected if and only if the identity has a neighbourhood base of connected sets; a connected locally compact group is $\sigma$-compact.

**Proof.** The first statement is the translation of local connectedness to the identity. For the second, a connected locally compact group is generated by a compact neighbourhood of $e$, and $G = \bigcup_n K^n$ with $K$ compact, each $K^n$ compact as a continuous image of a product, so $G$ is $\sigma$-compact. $\square$

### Compactness

**Theorem.** A compact subgroup of a Hausdorff group is closed. A closed subgroup of a compact group is compact, and a quotient of a compact group by a closed normal subgroup is compact.

**Proof.** A compact subset of a Hausdorff space is closed, and the continuous image of a compact space is compact. $\square$

**Theorem.** In a compact Hausdorff group $G$ a closed subgroup $H$ of finite index is open, and conversely an open subgroup has finite index. Consequently a compact totally disconnected group has a neighbourhood base at $e$ of open subgroups.

**Proof.** If $H$ is open then its cosets are pairwise disjoint open sets covering the compact space $G$, so there are finitely many and $H$ has finite index; being open, $H$ is closed. Conversely, if $H$ is closed of finite index, then $G \setminus H = \bigcup_{g \notin H} gH$ is a finite union of closed cosets, so $H$ is open. For the last statement, the identity component $G_e$ is trivial in a totally disconnected group, and by the previous theorem applied to the compact group $G$ it is the intersection of the open subgroups of $G$; a standard compactness argument upgrades this to a neighbourhood base. $\square$

**Theorem (open mapping for compact groups).** A continuous bijective homomorphism from a compact group onto a Hausdorff group is a homeomorphism.

**Proof.** A continuous bijection from a compact space to a Hausdorff space is a homeomorphism. $\square$

**Example.** $S^1$, $O(n)$, $U(n)$ and the $p$-adic integers $\mathbb{Z}_p$ are compact; $\mathbb{Z}_p$ is moreover totally disconnected, and its open subgroups $p^n\mathbb{Z}_p$ form a neighbourhood base.

### Local Compactness and Haar Measure

**Theorem.** Every Hausdorff locally compact group carries a nonzero left-invariant Radon measure $\mu$, finite on compact sets, unique up to a positive scalar. This is the **Haar measure**, for which the measure-theoretic apparatus is developed.

**Definition.** The **modular function** $\Delta : G \to (0, +\infty)$ is defined by $\mu(Ag) = \Delta(g)\mu(A)$ for a left Haar measure $\mu$. It is a continuous homomorphism, and $G$ is **unimodular** when $\Delta \equiv 1$. A left Haar measure is right-invariant exactly when $\Delta \equiv 1$.

**Theorem.** Compact groups, discrete groups and locally compact abelian groups are unimodular. On a compact group the normalised Haar measure, with $\mu(G) = 1$, is the unique bi-invariant probability measure, and it is the averaging device that replaces the division by $|G|$ in the orthogonality relations of the representation theory of finite groups.

**Proof.** For a compact group, $\Delta(G)$ is a compact subgroup of $(0,\infty)$, hence $\{1\}$; for a discrete group the counting measure is bi-invariant; for abelian $G$ left and right translations coincide. The normalisation is by dividing by $\mu(G) < \infty$. $\square$

**Example.** On $(\mathbb{R}, +)$ the Haar measure is Lebesgue measure; on $(\mathbb{R}_{>0}, \cdot)$ it is $dx/x$; and on $GL_n(\mathbb{R})$ the bi-invariant Haar measure is $|\det A|^{-n} \prod_{i,j} dA_{ij}$, the group being unimodular because $\operatorname{Ad}(A)$ acts on $\mathfrak{gl}_n$ with eigenvalues $\lambda_i \lambda_j^{-1}$, whose product is $1$. A first non-unimodular example is the affine group $\mathbb{R}^n \rtimes GL_n(\mathbb{R})$: its left Haar measure is $|\det A|^{-(n+1)} \, dx \, dA$ and its modular function is $\Delta(x, A) = |\det A|^{-1}$, so that already the group of the maps $x \mapsto ax + b$ of the line with $a > 0$ has $\Delta(a, b) = a^{-1}$ and is not unimodular.

**Theorem (invariant integration).** If $\mu$ is a left Haar measure on $G$ and $f \in L^1(\mu)$, then for every $g \in G$,

$$
\int_G f(gx) \, d\mu(x) = \int_G f(x) \, d\mu(x), \qquad \int_G f(x^{-1}) \, d\mu(x) = \int_G f(x) \, \Delta(x^{-1}) \, d\mu(x).
$$

**Proof.** The first identity is the invariance of $\mu$ under $L_g$. For the second, the image of $\mu$ under inversion is a right Haar measure, hence of the form $\Delta(x^{-1}) \, d\mu(x)$ with $\Delta$ the modular function, and the change of variable $y = x^{-1}$ converts the integral of $f(x^{-1})$ into the integral of $f(x)\Delta(x^{-1})$. $\square$

## Profinite Groups

### Definition and Examples

**Definition.** A **profinite group** is a topological group that is the inverse limit of an inverse system of finite groups, each carrying the discrete topology, the limit carrying the subspace topology of the product. Equivalently, a profinite group is a compact Hausdorff totally disconnected topological group.

**Example.** The group $\mathbb{Z}_p$ of $p$-adic integers is $\varprojlim_n \mathbb{Z}/p^n\mathbb{Z}$; the profinite completion of $\mathbb{Z}$ is $\hat{\mathbb{Z}} = \varprojlim_n \mathbb{Z}/n\mathbb{Z} \cong \prod_p \mathbb{Z}_p$, the product over the primes. The absolute Galois group of a field and the Galois group of an infinite Galois extension are profinite, the finite quotients being the Galois groups of the finite intermediate extensions; this is the **fundamental theorem of Galois theory** for infinite extensions, where the closed subgroups, not all subgroups, correspond to intermediate extensions.

**Theorem.** A profinite group is compact, Hausdorff and totally disconnected; its open subgroups are exactly its closed subgroups of finite index, and they form a neighbourhood base at the identity. Conversely, a compact Hausdorff totally disconnected group is profinite, being the inverse limit of its finite quotients.

**Proof.** The product of finite discrete groups is compact Hausdorff by Tychonoff, and a closed subgroup of it is compact Hausdorff; total disconnectedness comes from the fact that the projection to each finite quotient is a continuous map onto a discrete space, so a connected subset projects to a singleton in each coordinate. The identification of the open subgroups with the closed finite-index ones is the theorem of the preceding section. For the converse, the finite quotients $G/N$ with $N$ an open normal subgroup form an inverse system by normality, and the natural map $G \to \varprojlim G/N$ is a continuous bijection from a compact to a Hausdorff space, hence a homeomorphism; it is injective because the open subgroups separate points, and surjective by compactness. $\square$

### The Profinite Completion

**Definition.** The **profinite completion** of an abstract group $G$ is $\hat G^{\mathrm{pf}} = \varprojlim_{N \trianglelefteq G, \ [G:N] < \infty} G/N$, with the natural map $G \to \hat G^{\mathrm{pf}}$; it is injective exactly when $G$ is **residually finite**. A group is residually finite if every nontrivial element survives in some finite quotient. The hat carries two meanings in this article and they are kept apart: $\hat G$ is the completion of a topological group in its two-sided uniformity, while $\hat G^{\mathrm{pf}}$ is the profinite completion of an abstract group.

**Theorem.** The profinite completion $\hat G^{\mathrm{pf}}$ is profinite, $\hat G^{\mathrm{pf}}$ contains $G$ as a dense subgroup, and the assignment is functorial: a homomorphism $G \to H$ induces $\hat G^{\mathrm{pf}} \to \hat H^{\mathrm{pf}}$, continuous. Free groups, finitely generated linear groups and finitely generated abelian groups are residually finite.

**Proof.** Density: an element of $\hat G^{\mathrm{pf}}$ is a compatible family of cosets, and any basic neighbourhood fixes finitely many coordinates, hence contains an element of the image of $G$ by compatibility and the Chinese remainder-type argument. Functoriality: a homomorphism carries each finite-index normal subgroup of $H$ to one of $G$ after intersection, so it induces maps on the finite quotients, compatible with the system. Residual finiteness of free groups is the standard consequence of their linearity; of finitely generated abelian groups, by reduction modulo primes. $\square$

**Example.** $\hat{\mathbb{Z}} = \mathbb{Z}^{\mathrm{pf}} \cong \prod_p \mathbb{Z}_p$, and the natural map $\mathbb{Z} \to \hat{\mathbb{Z}}$ has dense image. For $GL_n(\mathbb{Z})$, the congruence subgroups give the profinite completion $\varprojlim_m GL_n(\mathbb{Z}/m\mathbb{Z})$.

## The Structure of Locally Compact Abelian Groups

### Duality of Finite Groups as the Model

**Definition.** Let $G$ be a locally compact abelian group. A **character** of $G$ is a continuous homomorphism $G \to S^1$. The set of characters, written $G^\vee$, is the **Pontryagin dual**; it is a group under pointwise multiplication and is given the compact-open topology, which makes it a locally compact abelian group. The symbol $G^\vee$ is used throughout in preference to a hat, which is reserved for completions.

**Example.** For a finite abelian group $G$, the dual $G^\vee$ is the character group $\operatorname{Hom}(G, S^1) = \operatorname{Hom}(G, \mathbb{C}^\times)$; it has the same order as $G$ and $G \cong G^\vee$ non-canonically, the isomorphism being canonical only after a choice of roots of unity. For $G = \mathbb{Z}/n\mathbb{Z}$ the dual is $\mu_n$, the group of $n$-th roots of unity, also cyclic of order $n$.

**Example (characters and inversion on $\mathbb{Z}/n\mathbb{Z}$).** A character is determined by its value on the generator $1$, and that value $\zeta$ must satisfy $\zeta^n = 1$ because $n \cdot 1 = 0$; hence every character of $\mathbb{Z}/n\mathbb{Z}$ is of the form $\chi_k(m) = e^{2\pi i k m/n}$ for a unique $k \in \mathbb{Z}/n\mathbb{Z}$, and $k \mapsto \chi_k$ is an isomorphism of $\mathbb{Z}/n\mathbb{Z}$ onto $\mu_n$. The orthogonality relation

$$
\frac{1}{n}\sum_{m=0}^{n-1} \chi_k(m)\overline{\chi_l(m)} = \delta_{kl}
$$

holds: the sum is $\frac{1}{n}\sum_m e^{2\pi i (k-l)m/n}$, which is $1$ for $k = l$ and the average of the $n$-th roots of unity for $k \neq l$, hence $0$. The normalised counting measure $f \mapsto \frac{1}{n}\sum_m f(m)$ is the Haar measure of the finite group, and the corresponding transform and inversion,

$$
\hat f(k) = \frac{1}{n}\sum_{m=0}^{n-1} f(m)\overline{\chi_k(m)}, \qquad
f(m) = \sum_{k=0}^{n-1} \hat f(k)\chi_k(m),
$$

hold for every $f : \mathbb{Z}/n\mathbb{Z} \to \mathbb{C}$; this is the discrete Fourier transform of the cyclic group, and the inversion formula is the expansion of $f$ in the orthogonal basis of characters. The same two displays, with the sum over $G$ replaced by Haar integration and the factor $1/n$ by the normalised Haar measure, are the orthogonality and inversion statements for a general compact abelian group.

**Example.** $\mathbb{R}^\vee \cong \mathbb{R}$ via $\xi \mapsto (x \mapsto e^{2\pi i \xi x})$; $(S^1)^\vee \cong \mathbb{Z}$; $\mathbb{Z}^\vee \cong S^1$; and $(\mathbb{Z}_p)^\vee \cong \mu_{p^\infty}$, the Prüfer group, with the discrete topology.

### Pontryagin Duality

**Theorem (Pontryagin).** For every locally compact abelian group $G$, the evaluation map

$$
G \longrightarrow G^{\vee\vee}, \qquad g \longmapsto \left(\chi \mapsto \chi(g)\right),
$$

is an isomorphism of topological groups. The assignment $G \mapsto G^\vee$ is a contravariant functor that is an equivalence of categories between locally compact abelian groups and their duals, carrying compact groups to discrete groups and conversely, and products to products.

**Proof sketch.** The evaluation map is a well-defined continuous homomorphism. Injectivity: if $\chi(g) = 1$ for all characters $\chi$, then $g$ is trivial, using the separation of points of $G$ by characters, which follows from the existence of enough Haar-integrable functions and the construction of characters from them. Surjectivity and the topological statement are the substance of the theorem and are proved by reducing to the cases $G = \mathbb{R}^n \times T^m \times D$ with $D$ discrete, using structure theory; the general case follows from the structure theorem below. That compactness and discreteness are interchanged is the statement that a compact group has a discrete dual and conversely, the standard compactness argument being that the dual of a discrete group is a closed subgroup of a product of circles. $\square$

**Theorem (structure of locally compact abelian groups).** Every locally compact abelian group is of the form $\mathbb{R}^n \times K$ with $K$ a locally compact abelian group containing an open compact subgroup, and modulo these the classification reduces to that of discrete abelian groups and compact abelian groups; the compactly generated case is $\mathbb{R}^n \times \mathbb{Z}^m \times F$ with $F$ finite.

**Proof sketch.** The identity component is a connected locally compact abelian group, hence of the form $\mathbb{R}^n \times K$ with $K$ compact by the solution of Hilbert's fifth problem in the abelian case; passing to the quotient by the identity component reduces to a totally disconnected locally compact abelian group, which contains an open compact subgroup. The compactly generated refinement uses that a compactly generated locally compact group is up to compact subgroups $\mathbb{R}^n \times \mathbb{Z}^m$ together with a finite group. $\square$

**Example.** $\mathbb{Z}^\vee = S^1$ and $(S^1)^\vee = \mathbb{Z}$ illustrate the interchange of discrete and compact. The Fourier transform on a group $G$ with Haar measure is the map $f \mapsto \hat f(\chi) = \int_G f(x)\overline{\chi(x)}\,dx$, defined on $G^\vee$; on $\mathbb{R}$ it is the classical Fourier transform, on $S^1$ the Fourier series, on a finite abelian group the discrete Fourier transform, and the inversion formula holds in each case with the appropriate dual Haar measure. The Pontryagin theorem is what makes the same theorem true in all of them.

## Summary

A topological group is a group whose multiplication and inversion are continuous; equivalently the map $(g, h) \mapsto gh^{-1}$ is continuous. Left and right translations are homeomorphisms and inversion is a homeomorphism, so the group is homogeneous and is determined by a neighbourhood base at the identity, subject to the three local-base axioms. A topological group is $T_0$ if and only if it is Hausdorff and then Tychonoff, so separation is cheap; every subgroup that is open is closed.

The neighbourhoods of $e$ generate the left and right uniformities, which induce the topology; the group is complete exactly when its uniform structure is complete, for which the two-sided uniformity is used, and the left and right uniformities agree exactly when the identity has a neighbourhood base of conjugation-invariant sets, a condition strictly stronger than unimodularity. Every topological group has a completion, unique up to isomorphism fixing $G$, obtained from the uniform completion with the group operation extended by continuity; a locally compact Hausdorff group is complete. Subgroups and quotients behave as expected: closures of subgroups are subgroups, the identity component is a closed normal subgroup, $G/H$ carries the quotient topology and is Hausdorff exactly when $H$ is closed, and the quotient map is open. A connected group is generated by each neighbourhood of $e$, and conversely a locally compact group generated by each neighbourhood of $e$ is connected; compact subgroups of Hausdorff groups are closed, open subgroups of compact groups have finite index, a continuous bijection from a compact group onto a Hausdorff group is a homeomorphism, and every locally compact Hausdorff group carries a Haar measure, unique up to scale, with modular function $\Delta$ and unimodularity for compact, discrete and abelian groups.

A profinite group is a compact Hausdorff totally disconnected group, equivalently an inverse limit of finite groups; its open subgroups are its finite-index closed subgroups and form a neighbourhood base, and every group has a profinite completion, injective precisely for residually finite groups. Finally, Pontryagin duality identifies a locally compact abelian group with its double dual and the category of such groups with its own opposite, exchanging compactness and discreteness; the structure theorem $\mathbb{R}^n \times K$ and the Fourier transform realise the classical Fourier analysis of $\mathbb{R}$, $S^1$, $\mathbb{Z}$ and finite abelian groups as instances of one theory.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G, H, K$ | Topological groups; $e$ the identity |
| $L_g, R_g$, $\operatorname{Ad}_g$ | Left and right translations; inner automorphism |
| $\mathcal{N}$ | Neighbourhood base at the identity |
| $\mathcal{U}_L, \mathcal{U}_R$ | Left and right uniformities |
| $E_U$ | Entourage $\{(g,h) : g^{-1}h \in U\}$ |
| $\hat G$ | Completion of a topological group in its two-sided (Raĭkov) uniformity |
| $G/H$, $\pi$ | Coset space or quotient group with quotient topology, and the quotient map |
| $G/H$ Hausdorff | Exactly when $H$ is closed |
| $G_e$, $G/G_e$ | Identity component (closed normal, intersection of the open subgroups) and component group |
| $\mu$, $\Delta$ | Haar measure and modular function |
| unimodular | $\Delta \equiv 1$; left Haar measure is right-invariant |
| $\mathbb{Z}_p$, $\mathbb{Q}_p$ | $p$-adic integers and numbers |
| $\hat G^{\mathrm{pf}}$, $\hat{\mathbb{Z}}$ | Profinite completion of an abstract group; $\hat{\mathbb{Z}} = \mathbb{Z}^{\mathrm{pf}}$ |
| $\varprojlim$ | Inverse limit of finite groups |
| residually finite | Every nontrivial element survives in a finite quotient |
| $G^\vee$, $\chi$, $\chi_k$ | Pontryagin dual and a character; characters of $\mathbb{Z}/n\mathbb{Z}$ |
| $\hat f$ | Fourier transform of $f$ on a locally compact abelian group |
| $\mu_n$, $\mu_{p^\infty}$ | Group of $n$-th roots of unity, Prüfer group |



## Further Reading

- Lev S. Pontryagin, *Topological Groups* (Gordon and Breach, 2nd ed. 1966), for the classical development of the theory and of duality.
- Nicolas Bourbaki, *General Topology*, Chapters 1–4 and *Topological Vector Spaces*, Chapters 1–5 (Springer, 1995, 1987), for uniformity and completion in the group setting.
- Edwin Hewitt and Kenneth A. Ross, *Abstract Harmonic Analysis I* (Springer, 2nd ed. 1979), for Haar measure, the structure of locally compact groups and Pontryagin duality.
- Lynn H. Loomis, *An Introduction to Abstract Harmonic Analysis* (Van Nostrand, 1953; reprinted Dover, 2011), for a concise account of invariant integration and duality.
- Walter Rudin, *Fourier Analysis on Groups* (Interscience, 1962; reprinted Wiley, 1990), for the harmonic analysis of locally compact abelian groups.
- John S. Wilson, *Profinite Groups* (Oxford University Press, 1998), for the profinite theory and its use in Galois theory.
- Luis Ribes and Pavel Zalesskii, *Profinite Groups* (Springer, 2nd ed. 2010), for inverse limits, completions and the Galois correspondence for closed subgroups.
- Karl H. Hofmann and Sidney A. Morris, *The Structure of Compact Groups* (De Gruyter, 3rd ed. 2013), for the structure theory of compact and locally compact groups.
