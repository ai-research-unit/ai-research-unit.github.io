
# __Involutive Group Actions on a Space__

## Introduction

An involutive group action is an action of a group with an involution in which the two involutions — the one on the group and the one on the space — are compatible, so that the space involution carries one orbit to another and descends to the quotient. The compatibility is a genuine constraint, and stating it correctly is the first result of the article: the anti-involution of the group cannot conjugate a left action unless it happens to be an automorphism, and the involution that does act on the space is the associated involutive automorphism. With the convention settled, the equivariant involution is exactly an action of the semidirect product of the group with the cyclic group of order two, the fixed set of the space involution is stable under the fixed subgroup, and the orbit space inherits an involution whose fixed points are computed by the fixed points of the space.

The article assumes the continuous involution, the associated involutive automorphism, the fixed and inverted subgroups and the split extension $G\rtimes_\alpha C_2$ from *Involutive Topological Groups*; the fixed set of a continuous involution of a space, its orbit space, the quotient map and its universal property, the failure of the orbit space to be Hausdorff, and the orbit space of a free involution as a two-fold covering from *Involutions on a Topological Space and the Fixed Set*, *Spaces with an Involution and the Orbit Space* and *The Orbit Space of a Free Involution*; and the group actions of *Group Actions and Structure*. The cohomology of the orbit space and the equivariant cohomology are *Algebraic Topology*, later in this part, and are named only.

Throughout, $G$ is a topological group with identity $e$ acting continuously on a topological space $X$, $\sigma$ is a continuous involution of $G$, $\alpha = \sigma\iota$ is the associated continuous involutive automorphism, $G^\alpha = I(\sigma)$ is the fixed subgroup, and the action map is written $(g, x)\mapsto g\cdot x$.

## Equivariant Involutions

**Definition.** Let $(G,\sigma)$ be an involutive topological group acting continuously on $X$. An **equivariant involution** of the action is a continuous involution $\tau$ of $X$ such that

$$
\tau(g\cdot x) = \alpha(g)\cdot \tau(x) \qquad \text{for all } g \in G,\ x \in X ,
$$

equivalently $\tau\,g\,\tau = \alpha(g)$ for every $g$ as operators on $X$. An action equipped with such a $\tau$ is an **involutive action**.

**Proposition (why the associated automorphism acts).** A map $\tau$ satisfying $\tau(g\cdot x) = \sigma(g)\cdot\tau(x)$ for all $g$ exists for an effective action only when $\sigma$ is an automorphism of $G$; for a genuine anti-involution and a faithful action no such $\tau$ exists, and the correct compatibility is the one with $\alpha = \sigma\iota$ above, equivalently $\tau(g\cdot x) = \sigma(g^{-1})\cdot\tau(x)$.

**Proof.** If $\tau(g\cdot x) = \sigma(g)\cdot\tau(x)$ then conjugating the operators gives $\tau\,g\,\tau = \sigma(g)$; the map $g\mapsto \tau g\tau$ is an automorphism of the image of $G$ in the homeomorphism group of $X$ and $g\mapsto \sigma(g)$ is an isomorphism onto that image only if $\sigma$ is a homomorphism, because $\tau(gh)\tau = \sigma(gh)$ while $(\tau g\tau)(\tau h\tau) = \sigma(g)\sigma(h)$; for an effective action the two force $\sigma(gh) = \sigma(g)\sigma(h)$. Since $\alpha$ is an automorphism the consistency holds, and $\alpha(g) = \sigma(g^{-1}) = \sigma(g)^{-1}$ is the equivalent form.

**Theorem (the extension).** An equivariant involution $\tau$ is exactly the action of the generator of the semidirect product $G\rtimes_\alpha C_2$ on $X$: the formulas

$$
(g, t^\epsilon)\cdot x = g\cdot \tau^\epsilon(x) \qquad (\epsilon \in \{0, 1\})
$$

define a continuous action of $G\rtimes_\alpha C_2$ on $X$, and conversely every continuous action of the extension restricts to an action of $G$ with equivariant involution the action of the generator.

**Proof.** The multiplication in the extension is $(g,t^\epsilon)(h,t^\delta) = (g\alpha^\epsilon(h), t^{\epsilon+\delta})$, and a direct computation gives $(g,t^\epsilon)\cdot((h,t^\delta)\cdot x) = g\cdot\tau^\epsilon(h\cdot\tau^\delta(x)) = g\,\alpha^\epsilon(h)\cdot\tau^{\epsilon+\delta}(x) = (g\alpha^\epsilon(h),t^{\epsilon+\delta})\cdot x$, using $\tau^\epsilon h \tau^\epsilon = \alpha^\epsilon(h)$; the unit acts by the identity because $\tau^0 = \mathrm{id}$. Continuity is the continuity of the action and of $\tau$, and the equivalence is the restriction to $G$ and the identification of the generator with $\tau$.

**Corollary.** The equivariant involutions of a fixed action are the involutions $\tau$ of $X$ with $\tau g\tau = \alpha(g)$ for all $g$; they are in bijection with the continuous extensions of the action to the semidirect product, so the existence of one is the statement that the action extends.

## The Fixed Set of the Space Involution

**Theorem (the fixed set is a $G^\alpha$-space).** Let $\tau$ be an equivariant involution and let $X^\tau$ be its fixed set, which is closed in $X$. Then $X^\tau$ is stable under the fixed subgroup $H = G^\alpha = I(\sigma)$, the action of $H$ on $X^\tau$ is continuous, and for $g \in G$ the translate $g\cdot X^\tau$ is the fixed set of the conjugate involution $g\,\tau\,g^{-1}$.

**Proof.** For $h \in H$ and $x \in X^\tau$ one has $\tau(h\cdot x) = \alpha(h)\cdot\tau(x) = h\cdot x$, so $h\cdot X^\tau\subseteq X^\tau$. For general $g$ and $x \in X^\tau$, the conjugate involution fixes $g\cdot x$; conversely an element $g\cdot x$ fixed by $g\tau g^{-1}$ has $x$ fixed by $\tau$ because $g$ acts injectively.

**Corollary (the fixed subgroup acts, the inverted subgroup inverts).** The fixed subgroup $H = G^\alpha$ acts on $X^\tau$ through the restricted action; the elements of the inverted set $G^\sigma = I(\alpha)$ act on $X^\tau$ by $\tau(g\cdot x) = g^{-1}\cdot x$, so they carry $X^\tau$ onto the fixed set of the conjugate involution and fix the fixed set only when $g^2 = e$.

**Proof.** For $g \in G^\sigma$ the dictionary gives $\alpha(g) = g^{-1}$, so $\tau(g\cdot x) = g^{-1}\cdot x$. The fixed set of the conjugate involution is $g\cdot X^\tau$, and $g\cdot X^\tau = X^\tau$ requires $g\in H$ and $g^2 = e$ by the stability criterion.

**Theorem (the fixed set of the restricted involution).** The involution $\tau$ restricts to a continuous involution of every closed $\tau$-stable subspace, and the fixed set of the restriction is the intersection; when $X$ is compact Hausdorff so is $X^\tau$, and when the action is effective the stabiliser of every point of $X^\tau$ is contained in $G^\alpha$.

**Proof.** A closed $\tau$-stable subspace carries the restricted homeomorphism, whose fixed set is the intersection. A closed subspace of a compact space is compact. For the stabiliser, $g\cdot x = x$ with $x \in X^\tau$ gives $\tau(x) = x$ and $\alpha(g)\cdot x = \tau(g\cdot x) = \tau(x) = x$, so $\alpha(g)$ and $g$ both stabilise $x$; effectiveness gives $\alpha(g) = g$, that is $g \in G^\alpha$.

## The Induced Involution on the Quotient

**Theorem (descent to the orbit space).** Let $\tau$ be an equivariant involution. Then $\tau$ maps orbits to orbits, $\tau(G\cdot x) = G\cdot\tau(x)$, and it induces a continuous involution $\bar\tau$ of the orbit space $X/G$ with the quotient topology; the quotient map $q : X\to X/G$ is equivariant, $q\tau = \bar\tau q$.

**Proof.** Since $\tau(g\cdot x) = \alpha(g)\cdot\tau(x)$ and $\alpha(G) = G$, the image of an orbit under $\tau$ is the orbit of $\tau(x)$. The induced map is well defined, continuous by the universal property of the quotient map, and its square is the identity because $\tau^2 = \mathrm{id}$; equivariance of $q$ is the definition of $\bar\tau$.

**Theorem (the fixed orbits).** The fixed points of the induced involution are the orbits $G\cdot x$ with $\tau(x) = g\cdot x$ for some $g \in G$. The natural map

$$
\rho : X^\tau/G^\alpha \longrightarrow (X/G)^{\bar\tau}, \qquad \rho(G^\alpha\cdot x) = G\cdot x ,
$$

is well defined and injective; it is surjective exactly when every $\tau$-stable orbit contains a $\tau$-fixed point, and it may fail to be surjective.

**Proof.** If $x \in X^\tau$ then $\bar\tau(G\cdot x) = G\cdot\tau(x) = G\cdot x$, so the orbit is fixed and $\rho$ is well defined, because $X^\tau$ is $G^\alpha$-stable. Two fixed points with the same orbit differ by an element $g$ with $g\cdot x = y$; applying $\tau$ gives $\alpha(g)\cdot x = y$, so $\alpha(g)^{-1}g$ stabilises $x$, and for an effective action $g \in G^\alpha$; this gives injectivity in the effective case. For the failure of surjectivity it suffices that a group element carries an orbit to itself without fixing a point of it, the standard example being a free involution on $S^1$ whose orbit space has one point.

**Corollary (free and transitive cases).** If the action of $G$ is transitive then $X/G$ is a point and $\bar\tau$ is the identity; if $\tau$ is free then $X^\tau = \varnothing$ and $(X/G)^{\bar\tau}$ is the set of orbits $G\cdot x$ with $\tau(x)\in G\cdot x$. If in addition $G$ acts freely and $\tau$ commutes with $G$, then $X\to X/G$ is a covering and the induced involution is the deck transformation of a two-fold covering.

**Proof.** The transitive case is immediate. For the free case, $X^\tau = \varnothing$ makes $\rho$ empty. When $\tau$ commutes with the action and acts freely with a free $G$-action, the quotient by the group generated by $G$ and $\tau$ is a two-fold covering, by the theory of the orbit space of a free involution.

**Remark (the orbit space need not be Hausdorff).** The quotient $X/G$ and its fixed set $(X/G)^{\bar\tau}$ need not be Hausdorff, and the induced involution is continuous for the quotient topology regardless; Hausdorffness requires the action to be proper or the orbit space to be separated, as *Spaces with an Involution and the Orbit Space* records. The closedness of $(X/G)^{\bar\tau}$ therefore requires the Hausdorff hypothesis, exactly as in the group case.

## Functions and Cohomology

**Proposition (the induced involution on functions).** Let $C(X)$ be the algebra of continuous functions $X\to k$. The formula $\tau^*f = f\circ\tau$ is an involution of $C(X)$, the subalgebra of $G$-invariants $C(X)^G$ is stable under it, and $C(X)^G$ with the involution $\tau^*$ is the algebra of continuous functions on the orbit space with the induced involution,

$$
C(X)^G \;\cong\; C(X/G) , \qquad \tau^*\text{ on } C(X)^G \;\longleftrightarrow\; \bar\tau^*\text{ on } C(X/G) .
$$

**Proof.** $\tau^*$ is an algebra involution because $\tau$ is a homeomorphism of order two. A $G$-invariant function $f$ satisfies $(\tau^* f)(g\cdot x) = f(\tau(g\cdot x)) = f(\alpha(g)\cdot\tau(x)) = f(\tau(x))$, so $\tau^*f$ is again $G$-invariant. The identification with $C(X/G)$ is the universal property of the quotient map, and the two involutions correspond because $\bar\tau q = q\tau$.

**Remark (cohomology, deferred).** The involution $\tau$ acts on the cohomology of $X$ by transport of structure, the action of $G\rtimes_\alpha C_2$ acts on the equivariant cohomology, and the Lefschetz fixed-point theorem relates the fixed set $X^\tau$ to the trace of the induced involution. All of this needs the cohomology of *Algebraic Topology*, later in this part, and the equivariant cohomology of *Equivariant Cohomology*, which is later still; this article states the topological action and its quotient and defers the cohomological statements entirely.

## Summary

An involutive action is an action of a group $G$ with involution $\sigma$ together with an involution $\tau$ of the space satisfying $\tau(g\cdot x) = \alpha(g)\cdot\tau(x)$ for the associated involutive automorphism $\alpha = \sigma\iota$; the anti-involution $\sigma$ itself cannot conjugate a faithful left action, so the automorphism $\alpha$ is the correct involution to use, and the compatibility is equivalently $\tau(g\cdot x) = \sigma(g^{-1})\cdot\tau(x)$. An equivariant involution is exactly an action of the semidirect product $G\rtimes_\alpha C_2$ extending the given one. The fixed set $X^\tau$ is closed and is stable under the fixed subgroup $G^\alpha = I(\sigma)$, the inverted set $G^\sigma$ carries it to the fixed sets of the conjugate involutions, and the stabiliser of a fixed point lies in $G^\alpha$ for an effective action. The involution maps orbits to orbits and descends to a continuous involution of the orbit space $X/G$; the fixed orbits are those with $\tau(x) = g\cdot x$, the natural map $X^\tau/G^\alpha\to(X/G)^{\bar\tau}$ is injective and may fail to be surjective, and the orbit space carries the involution of a two-fold covering when the action and the involution are free and commute. On functions the involution acts by $\tau^*f = f\circ\tau$, restricts to the invariants and corresponds to the induced involution on the quotient. The cohomological consequences are Part II's algebraic topology and are named only.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma$ | the continuous involution of the group |
| $\alpha = \sigma\iota$ | the associated involutive automorphism, the involution that acts |
| $\tau$ | the equivariant involution of the space |
| $\tau(g\cdot x) = \alpha(g)\cdot\tau(x)$ | the compatibility, equivalently $\tau(g\cdot x) = \sigma(g^{-1})\cdot\tau(x)$ |
| $G\rtimes_\alpha C_2$ | the extension whose generator acts by $\tau$ |
| $X^\tau$ | the closed fixed set, a $G^\alpha$-space |
| $G^\alpha = I(\sigma)$ | the fixed subgroup, acting on $X^\tau$ |
| $G^\sigma = I(\alpha)$ | the inverted set, carrying $X^\tau$ to conjugate fixed sets |
| $X/G$ | the orbit space with the quotient topology |
| $\bar\tau$ | the induced involution, $q\tau = \bar\tau q$ |
| $X^\tau/G^\alpha \to (X/G)^{\bar\tau}$ | the injection of fixed orbits, not always onto |
| $\tau^*f = f\circ\tau$ | the involution on the continuous functions |

## Further Reading

- Glen E. Bredon, *Introduction to Compact Transformation Groups* (Academic Press, 1972), for group actions on spaces, orbit spaces and equivariant maps.
- Tammo tom Dieck, *Transformation Groups* (De Gruyter, 1987), for equivariant topology, the orbit space and the Borel construction.
- Nicolas Bourbaki, *General Topology*, Chapters 1–4 (Springer, 1995), for quotient topologies, the universal property of the quotient map and the separation axioms.
- Lev S. Pontryagin, *Topological Groups* (Gordon and Breach, second edition, 1966), for continuous group actions and the topology of orbit spaces.
- Alexander Arhangel'skii and Mikhail Tkachenko, *Topological Groups and Related Structures* (Atlantis Press, 2008), for the action of a topological group on a space and the orbit-space topologies.
