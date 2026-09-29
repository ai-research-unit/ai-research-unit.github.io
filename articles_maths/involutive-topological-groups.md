# __Involutive Topological Groups__

## Introduction

An **involutive topological group** is a topological group together with an involution that is continuous. The two structures are those of *Involutive Groups* and *Topological Groups*, and the combination is not a sum of the two: continuity is a hypothesis with content, and once it holds the topology forces the involution to be a homeomorphism, closes its fixed set, closes the inverted subgroup and lets the involution pass to the completion.

Four additions are the substance of the article. The **fixed and the inverted sets are closed**, being the equalizers of continuous maps into a Hausdorff space; so the inverted set, which the abstract theory already knows to be a subgroup, is a closed subgroup, while the fixed set of an involution is closed and is a subgroup only under the abstract commuting criterion. A continuous involution **exchanges the left and the right uniformities**, hence preserves the two-sided uniformity and **extends to the completion**, so the completion of an involutive topological group is again one. The **quotient of the group by the inverted subgroup embeds in the fixed set**, by a continuous bijection onto its image, and the embedding is a homeomorphism onto a closed subspace as soon as the group is compact. And the **split extension by $C_2$ is a topological group exactly when the involutive automorphism defining it is continuous**, which is the condition under which the abstract extension theorem has a topological form.

Continuity itself is not automatic, with two exceptions. The **inversion is continuous by the axioms** of a topological group, so every topological group is an involutive topological group in a canonical way; and an **inner** involutive automorphism, the conjugation by an element whose square is central, is continuous because conjugation is. A general involution may fail to be continuous, and then its fixed set need not be closed: on $(\mathbb{R},+)$ a $\mathbb{Q}$-linear involution that permutes two elements of a Hamel basis is discontinuous, and its fixed subgroup is dense and not closed. On a compact group the continuity can be replaced by the closedness of the graph of the involution, and on a Polish group by the Baire property; the second statement is *Baire Spaces and Category* material and is named only.

**Layout and boundaries.** The article has six sections after the introduction: the continuous involutions and the two faces of the notion, with the continuity hypothesis and its two automatic cases; the fixed and the inverted sets, their closedness and the action of the involution on the identity component; the extension of the involution to the completion; stable subgroups, quotients and the embedding of the coset space in the fixed set; the split extension by $C_2$; and the abelian case with its computable examples. It closes with a comparison against the abstract theory and the usual summary apparatus. The abstract theory is *Involutive Groups*, whose dictionary of the fixed and the inverted sets, bijection $\sigma \leftrightarrow \sigma\iota$, quotient theorem and extension theorem are used without repetition; the topological background is *Topological Groups*, whose symbols $\mathcal{U}_L$, $\mathcal{U}_R$, $\hat G$, $G_e$ and $G/H$ are used with its meanings. Nothing from Part III is used: the Haar measure, the modular function and the invariant integral are named once, at the boundary, and the smooth theory of the order-two automorphisms of the classical groups is Part IV material, named once. Throughout $G$ is a topological group, Hausdorff when a separation hypothesis is needed, $e$ is its identity, $\sigma$ is an involution of $G$ in the sense of *Involutive Groups*, that is an anti-automorphism of order two, $\iota$ is the inversion, and $\alpha = \sigma\iota$ is the associated involutive automorphism, so that $\sigma = \iota\alpha$.

## Continuous Involutions

### The Two Faces

**Definition.** A **topological involution** of a topological group $G$ is a continuous involution of $G$: a map $\sigma : G \to G$ with $\sigma(ab) = \sigma(b)\sigma(a)$ and $\sigma^2 = \mathrm{id}$ which is continuous. An **involutive topological group** is a pair $(G,\sigma)$ with $\sigma$ a topological involution. A **continuous involutive automorphism** of $G$ is an automorphism $\alpha$ with $\alpha^2 = \mathrm{id}$ which is continuous.

**Theorem (the two faces).** Let $\sigma$ be an involution of $G$ and $\alpha = \sigma\iota$. Then $\sigma$ is continuous if and only if $\alpha$ is continuous, and $\sigma \mapsto \sigma\iota$ is a bijection from the topological involutions of $G$ onto the continuous involutive automorphisms of $G$.

**Proof.** The inversion is continuous by the axioms of a topological group, and the two maps satisfy $\sigma = \iota\alpha$ and $\alpha = \sigma\iota$, so each is continuous as soon as the other is. The map $\sigma \mapsto \sigma\iota$ is the abstract bijection of *Involutive Groups*, restricted to the continuous maps; it is bijective because $\sigma$ and $\alpha$ determine one another and surjective onto the continuous involutive automorphisms because $\alpha = \sigma\iota$ for $\sigma = \iota\alpha$.

**Corollary.** A topological involution is a homeomorphism of $G$ with $\sigma^{-1} = \sigma$, and so is a continuous involutive automorphism. An involutive topological group is therefore a topological group with a specified involutive topological automorphism, or anti-automorphism, of order two.

**Proof.** $\sigma$ is a bijection whose inverse is $\sigma$, which is continuous; a continuous bijection with continuous inverse is a homeomorphism.

**Example (the inversion, verdict: a continuous anti-automorphism, an automorphism only for abelian $G$).** The inversion $\iota(g) = g^{-1}$ is continuous by the definition of a topological group, so every topological group is an involutive topological group through the inversion, and this involution is continuous for free. It is an automorphism exactly when $G$ is abelian, by the abstract theorem, and on a nonabelian group it is a genuine anti-automorphism. Its fixed set is the $2$-torsion $G^\iota = \{g : g^2 = e\}$, a closed subset of a Hausdorff $G$ and a closed subgroup when $G$ is abelian; on the circle it is $\{\pm 1\}$ and on the torus $T^n$ it is $(\mathbb{Z}/2)^n$.

**Example (inner automorphisms, verdict: continuous automorphisms for free).** Let $u \in G$ with $u^2$ central and put $\alpha(g) = ugu^{-1}$, the inner automorphism $\operatorname{Ad}_u$. Then $\alpha^2(g) = u^2gu^{-2} = g$, so $\alpha$ is an involutive automorphism, and it is continuous because conjugation is continuous in both variables and the first variable $u$ is fixed. So an inner involutive automorphism is a continuous involutive automorphism without any further hypothesis. Its fixed subgroup is the centraliser $C_G(u)$, and the associated involution is $\sigma(g) = \alpha(g)^{-1} = ug^{-1}u^{-1}$, which is continuous and is an automorphism only for abelian $G$. In $O(2)$ the conjugation by a reflection is such an automorphism, with $C_G(u) = \{I, -I, u, -u\}$, of four elements.

**Example (discrete and trivial topologies, verdict: the topology adds nothing).** For the discrete topology every map is continuous and every subset is closed, so the involutive topological groups with $G$ discrete are exactly the abstract involutive groups of *Involutive Groups*; the same collapse occurs for the trivial topology, where the only requirement is that the involutive automorphism preserve the empty set and the whole set. The theory has content when the topology is Hausdorff and not discrete.

**Example (products, verdict: continuous automorphisms and continuous involutions).** For involutive topological groups $(G,\sigma)$ and $(H,\tau)$ the componentwise map $(\sigma,\tau)$ is a topological involution of $G \times H$ with fixed set $G^\sigma \times H^\tau$ and inverted set $I(\sigma) \times I(\tau)$. On $G \times G$ the swap $(x,y) \mapsto (y,x)$ is a continuous involutive automorphism with the diagonal as its fixed subgroup, and the twisted map $\rho(x,y) = (y^{-1},x^{-1})$ is a topological involution whose fixed set is the graph $\{(x,x^{-1})\}$ of the inversion, a closed set since the inversion is continuous, and the graph is a subgroup only when $G$ is abelian; the inverted set of $\rho$ is the diagonal.

### Continuity Is a Genuine Hypothesis

**Example (a discontinuous involutive automorphism, verdict: an order-two automorphism that is not continuous).** Let $G = (\mathbb{R},+)$ with the usual topology. Every group automorphism of $(\mathbb{R},+)$ is $\mathbb{Q}$-linear, because it fixes the rationals pointwise and additivity extends to rational scalars. Let $B$ be a Hamel basis of $\mathbb{R}$ over $\mathbb{Q}$ containing $1$ and $\sqrt{2}$, let $\alpha$ interchange $1$ and $\sqrt{2}$ and fix every other element of $B$, and extend $\mathbb{Q}$-linearly. Then $\alpha$ is additive, bijective and satisfies $\alpha^2 = \mathrm{id}$, so it is an involutive automorphism of the group $(\mathbb{R},+)$. It is **not continuous**: a continuous $\mathbb{Q}$-linear map $\mathbb{R} \to \mathbb{R}$ is $\mathbb{R}$-linear, so a continuous $\alpha$ would satisfy $\alpha(x) = cx$ with $c = \alpha(1) = \sqrt{2}$, and then $\alpha^2(x) = 2x \neq x$ for $x \neq 0$, contradicting $\alpha^2 = \mathrm{id}$. Its fixed subgroup $G^\alpha$ is the $\mathbb{Q}$-span of $B \setminus \{1,\sqrt{2}\}$, which has the cardinality of the continuum; the closed subgroups of $(\mathbb{R},+)$ are the discrete cyclic subgroups, which are countable, and $\mathbb{R}$ itself, so $G^\alpha$ is not closed, and being a subgroup whose closure is a subgroup it is dense. A discontinuous involution therefore has a fixed subgroup that the topology cannot separate from the whole group, and the closedness of the fixed set in the next section is the work of the continuity hypothesis.

**Theorem (compact groups: the closed graph suffices).** Let $G$ be compact Hausdorff and let $\sigma$ be an involution of $G$ whose graph $\{(g,\sigma(g))\}$ is closed in $G \times G$. Then $\sigma$ is a topological involution.

**Proof.** For a map $f : X \to Y$ with closed graph, with $X$ compact and $Y$ Hausdorff, the projection $\pi : X \times Y \to X$ is closed and $f^{-1}(F) = \pi(\mathrm{graph}(f) \cap (X \times F))$ is closed for every closed $F \subseteq Y$, so $f$ is continuous; the graph of $\sigma$ is closed by hypothesis.

**Remark (automatic continuity).** Continuity is often automatic when a regularity hypothesis replaces the graph condition: a homomorphism between topological groups that is Baire measurable is continuous when the groups are Polish, so on a Polish group the continuity of an involution can be replaced by its Baire measurability. This is *Baire Spaces and Category*, and nothing in this article uses it.

## The Fixed and the Inverted Sets

### Closedness

**Definition.** For an involution $\sigma$ of $G$ the **fixed set** is $G^\sigma = \{g : \sigma(g) = g\}$ and the **inverted set** is $I(\sigma) = \{g : \sigma(g) = g^{-1}\}$; for an involutive automorphism $\alpha$ the same two sets are written $G^\alpha$ and $I(\alpha)$.

**Theorem.** Let $\sigma$ be a topological involution of a Hausdorff group $G$ and $\alpha = \sigma\iota$. Then $G^\sigma$ and $I(\sigma)$ are closed in $G$; the inverted set $I(\sigma) = G^\alpha$ is a closed subgroup; $G^\sigma = I(\alpha)$; and if $G$ is compact then both are compact.

**Proof.** The fixed set $G^\sigma$ is the equalizer of the continuous maps $\sigma$ and $\mathrm{id}_G$, and the inverted set $I(\sigma)$ is the equalizer of $\sigma$ and $\iota$; the equalizer of two continuous maps into a Hausdorff space is closed, being the preimage of the diagonal under the continuous map $(\sigma, \iota)$. That $I(\sigma)$ is a subgroup, and the two dictionary identities, are the abstract theorem of *Involutive Groups*; a closed subset of a compact space is compact.

**Theorem (the identity component).** Let $\alpha$ be a continuous involutive automorphism of $G$. Then $\alpha(G_e) = G_e$, and $\alpha$ induces a continuous involutive automorphism of the component group $G/G_e$. Moreover $\alpha$ preserves connectedness, compactness, local compactness, total disconnectedness and discreteness of a subspace, and it carries an open subgroup to an open subgroup, a closed subgroup to a closed subgroup and a normal subgroup to a normal subgroup.

**Proof.** $\alpha$ is a homeomorphism and an automorphism fixing $e$, so it carries the component of $e$ into itself and, being bijective with inverse $\alpha$, onto itself; the remaining statements are the preservation properties of a homeomorphism for the topological notions and of an automorphism for the subgroup notions.

**Corollary (an open fixed subgroup).** If $G$ is connected and $G^\alpha$ is open then $\alpha = \mathrm{id}$; if $G$ is compact and $G^\alpha$ is open then $G^\alpha$ has finite index in $G$.

**Proof.** An open subgroup of a connected group is the whole group, and $G^\alpha = G$ says $\alpha = \mathrm{id}$. If $G$ is compact, the cosets of the open subgroup $G^\alpha$ are pairwise disjoint open sets covering $G$, so there are finitely many.

### The Dictionary and the Two Kinds

**Theorem (the dictionary).** For an involution $\sigma$ of $G$ with $\alpha = \sigma\iota$,

$$
G^\sigma = I(\alpha), \qquad I(\sigma) = G^\alpha .
$$

So the fixed set of the involution is the inverted set of the associated automorphism, and conversely; the subgroup among the two is $I(\sigma) = G^\alpha$, and the set that may fail to be a subgroup is the fixed set $G^\sigma = I(\alpha)$.

**Proof.** $I(\alpha) = \{g : \alpha(g) = g^{-1}\} = \{g : \sigma\iota(g) = g^{-1}\} = \{g : \sigma(g^{-1}) = g^{-1}\} = \{g : \sigma(g) = g\} = G^\sigma$, and the second identity is the same computation with the roles of $\sigma$ and $\alpha$ exchanged.

**Remark (the two kinds).** The two order-two maps are not the same kind of object. An **involutive automorphism** of the topological group is a topological symmetry of the group, and its fixed set $G^\alpha$ is a closed subgroup; a general **involution** is an anti-automorphism, its inverted set $I(\sigma) = G^\alpha$ is the closed subgroup and its fixed set $G^\sigma = I(\alpha)$ is generally only a closed set, a subgroup exactly when its elements commute pairwise, which is the abstract criterion. The two kinds are interchanged by composition with the inversion, and the inversion is continuous, so every topological statement about one kind is a topological statement about the other. The classification of the involutions of an algebra into the first and the second kind by their action on the centre has no counterpart here: what a topological group offers in its place is the division between the inner involutions and the outer ones, the inner ones being continuous automatically.

## The Involution and the Completion

**Theorem (uniform continuity).** Let $\alpha$ be a continuous involutive automorphism and $\sigma$ a topological involution of $G$, with the left and right uniformities $\mathcal{U}_L$ and $\mathcal{U}_R$ of *Topological Groups*. Then $\alpha$ is uniformly continuous for $\mathcal{U}_L$ and for $\mathcal{U}_R$; the involution $\sigma = \iota\alpha$ is a uniform isomorphism from $(G,\mathcal{U}_L)$ to $(G,\mathcal{U}_R)$ and from $(G,\mathcal{U}_R)$ to $(G,\mathcal{U}_L)$; and both preserve the two-sided uniformity $\mathcal{U}_L \vee \mathcal{U}_R$.

**Proof.** Let $W$ be a neighbourhood of $e$. By continuity of $\alpha$ at $e$ there is a neighbourhood $V$ with $\alpha(V) \subseteq W$. If $(x,y) \in E_V$, that is $x^{-1}y \in V$, then $\alpha(x)^{-1}\alpha(y) = \alpha(x^{-1}y) \in W$, so $(\alpha(x),\alpha(y)) \in E_W$; thus $\alpha$ carries $E_V$ into $E_W$ and is uniformly continuous for $\mathcal{U}_L$, and the computation with $xy^{-1}$ in place of $x^{-1}y$ gives the same for $\mathcal{U}_R$. Inversion carries $E_U$ to $F_U$ and $F_U$ to $E_U$ for every neighbourhood $U$, by the uniformity theory of *Topological Groups*; composing, $\sigma = \iota\alpha$ carries $E_V$ into $F_W$ and, by the same argument applied to the right uniformity, $F_V$ into $E_W$, so it is a uniform isomorphism between the two uniformities in both directions. A map uniformly continuous for each of two uniformities is uniformly continuous for their supremum.

**Theorem (extension to the completion).** Let $\sigma$ be a topological involution of a Hausdorff group $G$ with completion $\hat G$ in the two-sided uniformity. Then $\sigma$ extends uniquely to a continuous involution $\hat\sigma$ of $\hat G$; the pair $(\hat G, \hat\sigma)$ is an involutive topological group containing $(G,\sigma)$ as a dense subgroup; and $G^{\hat\sigma} \cap G = G^\sigma$, $I(\hat\sigma) \cap G = I(\sigma)$. A continuous involutive automorphism extends in the same way to a continuous involutive automorphism.

**Proof.** A uniformly continuous map from $G$ into a complete Hausdorff uniform space extends uniquely to the completion; applying this to $\sigma : G \to \hat G$, uniformly continuous for the two-sided uniformity, gives a continuous $\hat\sigma : \hat G \to \hat G$ extending $\sigma$. The identity $\hat\sigma^2 = \mathrm{id}$ holds on the dense subset $G$ and the anti-multiplicativity $\hat\sigma(xy) = \hat\sigma(y)\hat\sigma(x)$ holds on the dense subset $G \times G$; both sides of each identity are continuous, so both hold on the whole of $\hat G$, and $\hat\sigma$ is a topological involution. The two intersections record that $\hat\sigma$ restricts to $\sigma$.

**Remark.** The fixed and inverted sets of the extension are closed in the Hausdorff $\hat G$ and contain the closures of $G^\sigma$ and of $I(\sigma)$; so the inverted set of the extension is a closed subgroup of $\hat G$ containing the closure of $I(\sigma)$, and the completion of an involutive topological group carries the involution. The assignment is functorial for uniformly continuous morphisms, and the completion of the completion is the completion.

**Example.** The completion of $\mathbb{Q}$ with the usual topology is $\mathbb{R}$, and the inversion of $\mathbb{Q}$ extends to the inversion of $\mathbb{R}$; with the $p$-adic topology on $\mathbb{Z}$ the inversion extends to the inversion of $\mathbb{Z}_p$. In both cases the fixed set of the inversion is trivial, a torsion-free group having no element of order two, so the extension adds no fixed point and both extension theorems hold with $G^\sigma = \{e\}$.

## Subgroups, Quotients and the Coset Space

### Stable Subgroups and Quotients

**Definition.** A subgroup $H \leq G$ is **$\sigma$-stable** if $\sigma(H) = H$; a $\sigma$-stable $H$ carries the restricted involution $\sigma|_H$, and when $H$ is closed and normal it carries the induced involution $\bar\sigma$ on the quotient $G/H$.

**Theorem.** Let $\sigma$ be a topological involution of $G$ and $H$ a $\sigma$-stable subgroup. Then $\sigma|_H$ is a topological involution of $H$ with the subspace topology and $H \cap G^\sigma = H^{\sigma|_H}$, $H \cap I(\sigma) = I(\sigma|_H)$. If in addition $H$ is closed and normal then $\bar\sigma$ is a topological involution of the topological group $G/H$, and

$$
\pi(G^\sigma) \subseteq (G/H)^{\bar\sigma}, \qquad \pi(I(\sigma)) \subseteq I(\bar\sigma),
$$

where $\pi : G \to G/H$ is the quotient map. Both inclusions can be strict.

**Proof.** The restriction is continuous because $\sigma$ is, and the induced map is continuous because $\sigma$ and $\pi$ are; the abstract statements are the proposition of *Involutive Groups*, and $G/H$ is a topological group with the quotient topology because $H$ is closed and normal, with the quotient map continuous and open. The strictness is the abstract example recalled below.

**Remark (the inclusion can be strict).** The topology does not repair the abstract failure. For $G = \mathbb{Z}/4\mathbb{Z}$ with the inversion and $H = \{0,2\}$ the fixed set $G^\iota$ is $H$ itself, so $\pi(G^\iota) = \{0\}$, while the induced involution on $G/H \cong \mathbb{Z}/2\mathbb{Z}$ is the identity and its fixed set is the whole quotient. The example is discrete, so it is a statement of the abstract theory read in the topological language; the inclusion is strict because an element of the quotient can be fixed with no fixed representative.

### The Coset Space and the Fixed Set

**Theorem (the symmetric map).** Let $\sigma$ be a topological involution of a Hausdorff group $G$, put $\alpha = \sigma\iota$ and $I(\sigma) = G^\alpha$, a closed subgroup, and define

$$
\varphi : G \to G, \qquad \varphi(g) = g^{-1}\sigma(g)^{-1} = g^{-1}\alpha(g).
$$

Then $\varphi$ is continuous, takes its values in the fixed set $G^\sigma$, is constant on the left cosets of $I(\sigma)$, and induces a continuous bijection

$$
\bar\varphi : G/I(\sigma) \longrightarrow \varphi(G) \subseteq G^\sigma, \qquad gI(\sigma) \longmapsto g^{-1}\alpha(g),
$$

onto its image. If $G$ is compact, then $G/I(\sigma)$ is compact Hausdorff, the image $\varphi(G)$ is a closed subspace of $G^\sigma$, and $\bar\varphi$ is a homeomorphism of $G/I(\sigma)$ onto $\varphi(G)$.

**Proof.** The map $\varphi$ is continuous, being a composite of the continuous operations of the group. Using $\alpha^2 = \mathrm{id}$,

$$
\alpha(\varphi(g)) = \alpha(g^{-1})\alpha(\alpha(g)) = \alpha(g)^{-1}g = \varphi(g)^{-1},
$$

so $\varphi(g)$ lies in $I(\alpha) = G^\sigma$, which is the statement that the image is in the fixed set. If $h \in I(\sigma) = G^\alpha$ then $\alpha(h) = h$ and

$$
\varphi(hg) = (hg)^{-1}\alpha(hg) = g^{-1}h^{-1}h\,\alpha(g) = g^{-1}\alpha(g) = \varphi(g),
$$

so $\varphi$ is constant on left cosets and $\bar\varphi$ is well defined, and it is continuous because $\varphi$ is and the quotient map is continuous. For injectivity, suppose $\varphi(g) = \varphi(g')$ and write $g' = ug$; since $\alpha(g) = g\,\varphi(g)$,

$$
\varphi(g') = (ug)^{-1}\alpha(ug) = g^{-1}u^{-1}\alpha(u)\,\alpha(g) = g^{-1}u^{-1}\alpha(u)\,g\,\varphi(g),
$$

and equality with $\varphi(g)$ gives $g^{-1}u^{-1}\alpha(u)g = e$, that is $\alpha(u) = u$, so $u \in G^\alpha = I(\sigma)$ and $g' \in I(\sigma)g$. Thus $\bar\varphi$ is injective, and it is a bijection onto its image. If $G$ is compact then $G/I(\sigma)$ is compact, the subgroup $I(\sigma)$ is closed so $G/I(\sigma)$ is Hausdorff, the image $\varphi(G)$ is compact and hence closed in $G^\sigma$, and a continuous bijection from a compact space onto a Hausdorff space is a homeomorphism.

**Example (the inversion of the circle, verdict: the degenerate case).** For $G = S^1$ with $\sigma = \iota$ the associated automorphism is $\alpha = \mathrm{id}$, so $I(\sigma) = G$, the coset space is a single point, and $\varphi$ is the constant map $g \mapsto e$. The fixed set is $\{\pm 1\}$ and the image is $\{e\}$, so the theorem is sharp: the coset space can be trivial while the fixed set is not.

**Example (the swap of the torus, verdict: a homeomorphism onto the whole fixed set).** For $G = S^1 \times S^1$ with the involutive automorphism $\alpha(x,y) = (y,x)$ the associated involution is $\sigma(x,y) = (y^{-1},x^{-1})$. The inverted subgroup is the diagonal $I(\sigma) = \{(x,x)\}$ and the fixed set is the anti-diagonal $G^\sigma = \{(x,x^{-1})\}$, both circles; the coset space $G/I(\sigma)$ is a circle and $\varphi(x,y) = (x^{-1}y, y^{-1}x) = (t,t^{-1})$ with $t = x^{-1}y$ is a homeomorphism of the coset space onto the anti-diagonal. Here the image is the whole fixed set.

**Example (a reflection of the torus, verdict: a homeomorphism onto a proper closed piece of the fixed set).** For the same group and the involutive automorphism $\alpha(x,y) = (x,y^{-1})$ the inverted subgroup is $I(\sigma) = S^1 \times \{\pm 1\}$ and the fixed set is $G^\sigma = \{\pm 1\} \times S^1$; the coset space $G/I(\sigma)$ is a circle and $\varphi(x,y) = (1,y^{-2})$ maps it homeomorphically onto the single circle $\{1\} \times S^1$, which is a proper closed subspace of the two-circle fixed set. The image of the coset space is therefore not the whole fixed set, and the second component of $G^\sigma$ is invisible to the symmetric map.

### The Split Extension by $C_2$

**Theorem (the extension is topological exactly when the involution is).** Let $\alpha$ be an involutive automorphism of $G$ and let the semidirect product $G \rtimes_\alpha C_2$ carry the product topology, with $C_2 = \{1,t\}$ discrete and $t$ acting through $\alpha$. Then the multiplication and the inversion of the semidirect product are continuous if and only if $\alpha$ is continuous, so $G \rtimes_\alpha C_2$ is a topological group exactly when $\alpha$ is a continuous involutive automorphism; in that case $G$ is an open, hence closed, normal subgroup of index two, and the fixed subgroup $G^\alpha$ is the centraliser of $t$.

**Proof.** The product is $(g,t^\epsilon)(h,t^\delta) = (g\,\alpha^\epsilon(h), t^{\epsilon+\delta})$. Its continuity is equivalent to the continuity of $(g,h) \mapsto \alpha^\epsilon(h)$ for each $\epsilon$, the case $\epsilon = 0$ being the projection and the case $\epsilon = 1$ being $\alpha$; and the inversion is $(g,t^\epsilon)^{-1} = (\alpha^\epsilon(g^{-1}), t^{-\epsilon})$, continuous for the same reason, the case $\epsilon = 0$ being the inversion of $G$, which is continuous by the axioms. So the semidirect product is a topological group exactly when $\alpha$ is continuous. Then $\{1\}$ is open in the discrete $C_2$, so $G \times \{1\}$ is open, hence closed, in $G \times C_2$, and it is normal of index two by the abstract theorem; finally $(g,1)(1,t) = (g,t)$ and $(1,t)(g,1) = (\alpha(g),t)$, so $(g,1)$ centralises $(1,t)$ exactly when $\alpha(g) = g$.

**Example.** With $G = S^1$ and $\alpha$ the inversion the semidirect product is the group $O(2)$ of rotations and reflections of the circle, the reflections forming the other coset and acting on the rotations by inversion; the conjugation by a reflection realises the involutive automorphism, and its fixed subgroup is the centraliser of the reflection, of four elements. With $G = C_n$ finite cyclic and $\alpha$ the inversion the construction gives the dihedral group $D_n$, and with $G = \mathbb{Z}$ discrete it gives the infinite dihedral group; in each case all the maps are continuous, the extension is a topological group, and the abstract extension theorem acquires a topological form.

## The Abelian Case

**Theorem.** Let $G$ be abelian. Then every anti-automorphism of $G$ is an automorphism, so the topological involutions of $G$ are the continuous automorphisms of order dividing two; they form a subgroup of $\mathrm{Aut}(G)$, the composite of two of them being one of them, and the inversion is among them. The fixed set of the inversion is the $2$-torsion $G^\iota = \{g : g^2 = e\}$, a closed subgroup of a Hausdorff $G$.

**Proof.** The degeneration of anti-automorphisms to automorphisms is the corollary of *Involutive Groups*, and the topological involutions are the elements of order dividing two of the group of continuous automorphisms, which is closed under composition. The fixed set $G^\iota$ is the equalizer of the continuous maps $\iota$ and $\mathrm{id}$, hence closed, and it is a subgroup because $G$ is abelian.

**Example (the additive real spaces, verdict: continuous automorphisms, rarely involutions).** On $G = (\mathbb{R}^n,+)$ the continuous group automorphisms are the invertible real matrices, and the topological involutions are the matrices $A$ with $A^2 = I$; among them are the inversion $-I$, the sign changes $\operatorname{diag}(\pm 1, \ldots, \pm 1)$ and the swap of two coordinates, and there are others, such as a swap of two coordinate blocks. The fixed subgroup is the eigenspace of $A$ for the eigenvalue $1$. Here anti-automorphisms and automorphisms coincide because the group is abelian, and the discontinuous order-two automorphisms of the first section, as many as the order-two $\mathbb{Q}$-linear maps of a Hamel basis, are precisely what the continuity condition removes.

**Example (the circle and the torus, verdict: continuous automorphisms).** On $S^1$ the continuous automorphisms are the identity and the inversion, so the circle has exactly two topological involutions; the fixed subgroup of the inversion is $\{\pm 1\}$. On the torus $T^n = \mathbb{R}^n/\mathbb{Z}^n$ each $A \in GL_n(\mathbb{Z})$ acts by a continuous automorphism, and $A^2 = I$ gives a topological involution whose fixed subgroup is $\{x \in T^n : (A-I)x \in \mathbb{Z}^n\}$; for $A = -I$ it is the $2$-torsion $(\mathbb{Z}/2)^n$, and for the swap of two coordinates it is the diagonal circle.

## What the Topology Adds

The comparison is between the abstract involutive group and its topological form. The new datum is continuity, and its consequences are the following.

- **Continuity is a hypothesis.** The inversion and the inner involutions are continuous for free; a general involution may be discontinuous, as the $\mathbb{Q}$-linear involution of $(\mathbb{R},+)$ shows. On a compact group the continuity can be replaced by the closedness of the graph, and on a Polish group by the Baire property. Abstractly the question does not arise.
- **The fixed and the inverted sets are closed**, being equalizers; so the inverted subgroup $I(\sigma) = G^\alpha$ is a closed subgroup and the fixed set $G^\sigma$ is closed, and both are compact when $G$ is. Abstractly the fixed set is only a set.
- **The involution exchanges the left and the right uniformities**, hence preserves the two-sided uniformity and extends to the completion, and the completion of an involutive topological group is again one. There is no completion in the abstract theory.
- **The quotient by the inverted subgroup embeds in the fixed set** by a continuous bijection onto its image, and compactness upgrades the embedding to a homeomorphism onto a closed piece of the fixed set. Abstractly one knows only that the inverted set is a subgroup; the coset space and its map into the fixed set are new objects.
- **The split extension by $C_2$ is a topological group exactly when the involutive automorphism is continuous**, so continuity is the condition under which the abstract extension theorem acquires a topological form.
- **The involution preserves the identity component and the topological properties** of the group and of its subgroups, and it acts on the component group $G/G_e$ and on the set of open subgroups; an open fixed subgroup is the whole group when the group is connected and has finite index when the group is compact.
- **On an abelian group** the involutions are the continuous automorphisms of order two, a strictly smaller set than the abstract automorphisms of order two and often computable, as on $\mathbb{R}^n$, $S^1$ and $T^n$.
- **The Haar measure is named and not used.** For a locally compact $G$ an involution carries a left Haar measure to a right Haar measure, hence to a left Haar measure when $G$ is unimodular, and then it is measure-preserving; the integral that makes this a statement about measures, the modular function and the harmonic analysis built on them are *Locally Compact Groups and Haar Measure* and *Analysis on Groups* in Part III. Nothing here uses the measure.

## Summary

An involutive topological group is a topological group with a continuous involution, that is with a continuous anti-automorphism of order two; the datum is the same as a continuous involutive automorphism $\alpha = \sigma\iota$, the two are interchanged by the continuous inversion, and either is a homeomorphism of the group. The inversion is continuous by the axioms, and an inner involutive automorphism, the conjugation by an element of central square, is continuous because conjugation is; an outer involution may be discontinuous, and on $(\mathbb{R},+)$ a $\mathbb{Q}$-linear involution of a Hamel basis is discontinuous with a dense fixed subgroup, so continuity is a genuine hypothesis, replaceable on a compact group by the closedness of the graph.

The fixed set $G^\sigma$ and the inverted set $I(\sigma)$ are closed, being equalizers of continuous maps into a Hausdorff space; the inverted set $I(\sigma) = G^\alpha$ is a closed subgroup while the fixed set $G^\sigma = I(\alpha)$ is a closed set, a subgroup exactly when its elements commute pairwise; and both are compact when $G$ is. The involution preserves the identity component and the topological properties of the group and its subgroups, an open fixed subgroup is the whole group when the group is connected and has finite index when the group is compact, and the involution descends to the component group.

A continuous involution is uniformly continuous for the two-sided uniformity and exchanges the left and the right uniformities, so it extends uniquely to a continuous involution of the completion $\hat G$, the completion is again an involutive topological group, and the fixed and the inverted sets of the extension meet $G$ in those of $G$. On a stable subgroup the involution restricts and on the quotient by a stable closed normal subgroup it descends, the abstract strictness of the image of the fixed set being unrepaired by the topology. The symmetric map $\varphi(g) = g^{-1}\sigma(g)^{-1}$ is continuous, takes its values in the fixed set, and induces a continuous bijection of the coset space $G/I(\sigma)$ onto its image, which is a homeomorphism onto a closed subspace of the fixed set when the group is compact; the image need not be the whole fixed set, as the reflection of the torus shows. The semidirect product $G \rtimes_\alpha C_2$ with the product topology is a topological group exactly when $\alpha$ is continuous, and then $G$ is an open normal subgroup of index two with $G^\alpha$ the centraliser of the added element, so that $O(2)$, the dihedral groups and the infinite dihedral group arise in this way. On an abelian group the topological involutions are the continuous automorphisms of order two, among them the inversion and the sign changes, computable on $\mathbb{R}^n$, $S^1$ and $T^n$, with the closed $2$-torsion subgroup as the fixed subgroup of the inversion.

## Summary of Notation

| symbol | meaning |
|---|---|
| $G$, $e$ | a topological group, Hausdorff when needed, and its identity |
| $\sigma$ | a topological involution of $G$, that is a continuous anti-automorphism of order two |
| $\iota$ | the inversion $\iota(g) = g^{-1}$, continuous by the axioms |
| $\alpha = \sigma\iota$ | the continuous involutive automorphism associated with $\sigma$ |
| $G^\sigma$, $G^\alpha$ | the fixed sets $\{g : \sigma(g) = g\}$ and $\{g : \alpha(g) = g\}$ |
| $I(\sigma)$, $I(\alpha)$ | the inverted sets $\{g : \sigma(g) = g^{-1}\}$ and $\{g : \alpha(g) = g^{-1}\}$ |
| $G^\sigma = I(\alpha)$, $I(\sigma) = G^\alpha$ | the dictionary: the fixed set of the involution is the inverted set of the automorphism |
| $\mathcal{U}_L$, $\mathcal{U}_R$, $E_U$ | the left and right uniformities and their basic entourages, from *Topological Groups* |
| $\hat G$ | the completion in the two-sided uniformity, carrying the extended involution |
| $G_e$, $G/G_e$ | the identity component, preserved by the involution, and the component group |
| $\varphi$ | the symmetric map $g \mapsto g^{-1}\sigma(g)^{-1} = g^{-1}\alpha(g)$ |
| $G/I(\sigma)$ | the coset space of left cosets, embedding in the fixed set $G^\sigma$ |
| $G \rtimes_\alpha C_2$ | the split extension, a topological group exactly when $\alpha$ is continuous |
| $\operatorname{Ad}_u$, $C_G(u)$ | the inner automorphism and the centraliser, the fixed subgroup of $\operatorname{Ad}_u$ |
| $S^1$, $T^n$ | the circle group and the torus $\mathbb{R}^n/\mathbb{Z}^n$ |
| Hamel basis | a basis of $\mathbb{R}$ as a vector space over $\mathbb{Q}$, used for the discontinuous examples |
| $\mu$, $\Delta$ | Part III: Haar measure and modular function, named here only |
| Baire measurable | Part II, *Baire Spaces and Category*: the hypothesis that can replace continuity |

## Further Reading

- Lev S. Pontryagin, *Topological Groups* (Gordon and Breach, second edition, 1966), for the classical theory of the continuous automorphisms, the uniformities and the completions.
- Nicolas Bourbaki, *General Topology*, Chapters 3 and 4 (Springer, 1995), for uniform structures, uniform continuity and the completion used here.
- Edwin Hewitt and Kenneth A. Ross, *Abstract Harmonic Analysis I* (Springer, second edition, 1979), for the topological structure of locally compact groups and for the automorphisms in the compact and the abelian cases.
- Karl H. Hofmann and Sidney A. Morris, *The Structure of Compact Groups* (De Gruyter, third edition, 2013), for the continuous automorphisms, the fixed subgroups and the topological splitting of compact groups.
- Jean Dieudonné, *La géométrie des groupes classiques* (Springer, third edition, 1971), for the order-two automorphisms of the classical groups, which are Part IV material.
- Sigurdur Helgason, *Differential Geometry, Lie Groups and Symmetric Spaces* (AMS, 2001), for the symmetric spaces that a fixed subgroup defines; the smooth theory is Part III and the geometry is Part IV, and neither is used here.
- B. J. Pettis, "On continuity and openness of homomorphisms in topological groups", *Annals of Mathematics* **52** (1950), 293–308, for the automatic continuity of Baire-measurable homomorphisms used in the remark on the continuity hypothesis.
