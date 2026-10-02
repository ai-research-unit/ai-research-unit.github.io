# __Involutive Proximity Spaces__

## Introduction

A proximity space is a set with a relation that records which pairs of subsets are **close** to one another, and it sits between the topology and the uniformity: every uniform space determines a proximity, every proximity determines a topology, and the proximity is the part of the uniform structure that survives the passage to the compactification. An **involutive proximity space** is a proximity space with an involution that preserves the closeness relation, and the pattern of the group `- * Theory` applies to it: the involution acts on the elements, and the orbit space, the fixed set and the completion all inherit a compatible structure. The proximity is the coarsest of the three structures, and the involution behaves best there, because a proximity is determined by a compactification and the involution extends to the compactification by the universal property of the completion. This is the structural reason that the orbit space of a compact Hausdorff space under a continuous involution is again compact Hausdorff, and it is the sense in which the involutive proximity space is the natural setting for the quotients of the later articles.

The article defines the proximity structure and the proximity involution, proves that the quotient carries a proximity making the orbit map a proximity map and that it is the finest such, proves that the fixed set is closed for a separated proximity, and connects the construction to the uniformity and to the completion. It continues *Involutive Uniform Spaces*, whose uniformity determines a proximity, and it uses the proximity spaces and their compactifications of this Part. Nothing analytic and nothing geometric is used: the proximity relation is an abstract relation on subsets, no metric is assumed, and no length or angle is read from the spaces.

## Proximity Spaces and Their Involutions

### Proximity Structures

**Definition.** A **proximity** on a set $X$ is a relation $\delta$ on the subsets of $X$, read "$A$ is close to $B$", such that for all $A, B, C \subseteq X$:

**(P1)** $A \delta B \Rightarrow B \delta A$;

**(P2)** $(A \cup B) \delta C \iff A \delta C \text{ or } B \delta C$;

**(P3)** $A \delta B \Rightarrow A \neq \emptyset$ and $B \neq \emptyset$;

**(P4)** $A \mathrel{\not\delta} B \Rightarrow$ there is $E \subseteq X$ with $A \mathrel{\not\delta} E$ and $E^{c} \mathrel{\not\delta} B$.

A **proximity space** is a set with a proximity. It is **separated** when $x \delta y$ only for $x = y$, where $x \delta y$ abbreviates $\{x\} \delta \{y\}$.

**Definition.** The **proximity topology** on a proximity space has for its closure operator

$$
x \in \overline{A} \iff \{x\} \delta A ,
$$

and the **proximity map** between proximity spaces is a map $f$ with

$$
A \delta B \Rightarrow f(A) \mathrel{\delta'} f(B) .
$$

Every proximity map is continuous for the proximity topologies, and the proximity topology is determined by the proximity, which is in turn determined by the topology together with the compactification in the compact case.

### Proximity Involutions

**Definition.** An **involutive proximity space** is a proximity space $X$ with an involution $\sigma$ that preserves the proximity,

$$
A \delta B \iff \sigma(A) \mathrel{\delta} \sigma(B) \qquad (A, B \subseteq X).
$$

The involution is then a **proximity involution**.

**Proposition.** A proximity involution is a proximity isomorphism and a homeomorphism of the proximity topology; the fixed set $X^{\sigma}$ with the subspace proximity is an involutive proximity space; and the invariant subsets form a Boolean subalgebra on which $\sigma$ acts as a proximity automorphism.

**Proof.** The inverse $\sigma^{-1} = \sigma$ preserves the proximity by the definition read backwards, so $\sigma$ is a proximity isomorphism; a proximity isomorphism is a homeomorphism of the proximity topologies. The fixed set carries the subspace proximity and the involution restricts to the identity. The invariant subsets are those with $\sigma(A) = A$, and the preservation of $\delta$ passes to them.

## The Orbit Proximity

### The Quotient Proximity

**Definition.** Let $X$ be an involutive proximity space and $\pi : X \to X/\sigma$ the orbit map. The **orbit proximity** on $X/\sigma$ is defined for $U, V \subseteq X/\sigma$ by

$$
U \mathrel{\tilde\delta} V \iff \pi^{-1}(U) \mathrel{\delta} \pi^{-1}(V) .
$$

**Theorem.** The relation $\tilde\delta$ is a proximity on $X/\sigma$; the orbit map is a proximity map for it; and the orbit proximity is the finest proximity on $X/\sigma$ making the orbit map a proximity map.

**Proof.** (P1) is the symmetry of $\delta$. (P2) is that $\pi^{-1}(U \cup W) = \pi^{-1}(U) \cup \pi^{-1}(W)$ together with (P2) for $\delta$. (P3) is that $U \neq \emptyset$ if and only if $\pi^{-1}(U) \neq \emptyset$. For (P4), let $U \mathrel{\not\tilde\delta} V$, so that $\pi^{-1}(U) \mathrel{\not\delta} \pi^{-1}(V)$; by (P4) in $X$ there is $E$ with $\pi^{-1}(U) \mathrel{\not\delta} E$ and $E^{c} \mathrel{\not\delta} \pi^{-1}(V)$. Put $F = E \cap \sigma(E)$, which is invariant and satisfies $F \subseteq E$ and $F^{c} = E^{c} \cup \sigma(E)^{c}$. The set $\pi^{-1}(U)$ is invariant, so $\pi^{-1}(U) \mathrel{\not\delta} \sigma(E)$, and (P2) gives $\pi^{-1}(U) \mathrel{\not\delta} E \cup \sigma(E)$, hence $\pi^{-1}(U) \mathrel{\not\delta} F$ because $F \subseteq E \cup \sigma(E)$. For the second half, (P4) applied in $X$ gives $E^{c} \mathrel{\not\delta} \pi^{-1}(V)$; applying the involution and using its preservation of $\delta$ gives $\sigma(E)^{c} \mathrel{\not\delta} \pi^{-1}(V)$; the contrapositive of (P2) then gives $F^{c} = E^{c} \cup \sigma(E)^{c} \mathrel{\not\delta} \pi^{-1}(V)$. Taking $W = \pi(F)$, which has $\pi^{-1}(W) = F$ because $F$ is invariant, gives $U \mathrel{\not\tilde\delta} W$ and $W^{c} \mathrel{\not\tilde\delta} V$, which is (P4). The orbit map is a proximity map by the definition of $\tilde\delta$. If $\delta'$ is any proximity making $\pi$ a proximity map, then $U \mathrel{\delta'} V$ gives $\pi^{-1}(U) \mathrel{\delta} \pi^{-1}(V)$, hence $U \mathrel{\tilde\delta} V$; so $\delta' \subseteq \tilde\delta$ and $\tilde\delta$ is the finest.

### Properties of the Orbit Map

**Theorem.** The orbit map is a surjective proximity map, it is continuous and open for the proximity topologies, and the orbit proximity is separated when the proximity of $X$ is separated.

**Proof.** Surjectivity and the proximity-map property are the construction; the topological clauses are those of the involution of a topological space, since the proximity topology of the orbit proximity is the quotient topology. For separatedness, suppose the singleton classes of $x$ and of $y$ are close for $\tilde\delta$. Then the orbits $\{x,\sigma x\}$ and $\{y,\sigma y\}$ are close for $\delta$; by (P2), applied to finite unions in both variables, some point of the first orbit is close to some point of the second, and separatedness gives equality of those two points, so the two orbits meet and the two classes coincide.

**Remark.** The orbit proximity is the finest making the orbit map a proximity map, in contrast with the orbit uniformity, which is the finest making it uniformly continuous; the two constructions agree when the uniformity is the one determined by the proximity, which happens exactly when the proximity is totally bounded. This is why the proximity quotient is the more robust of the two for the compact case.

## The Fixed Set

**Theorem.** The fixed set of a proximity involution of a separated proximity space is closed in the proximity topology, and it is a proximity subspace on which the involution is the identity.

**Proof.** A separated proximity induces a Hausdorff proximity topology, because the topology is completely regular and $T_{1}$; this is the standard theorem relating proximities to topologies. The map $x \mapsto (x, \sigma x)$ is continuous, and $X^{\sigma}$ is its preimage of the diagonal $\Delta_{X} \subseteq X \times X$. The diagonal of a Hausdorff space is closed, so the preimage is closed. The rest is the definition.

**Example.** On the real line with the proximity determined by its usual uniformity, the involution $x \mapsto -x$ has the fixed set $\{0\}$, closed; the orbit proximity on the half-line is the proximity induced by the usual uniformity of the half-line.

**Example (a free proximity involution).** The exchange of the two copies of $\mathbb{R} \sqcup \mathbb{R}$ is a free proximity involution, and the orbit proximity is the usual proximity of $\mathbb{R}$.

## Proximity, Uniformity and Completion

### The Proximity of a Uniformity

**Definition.** A uniform space $X$ with uniform structure $\mathcal{U}$ determines a proximity $\delta_{\mathcal{U}}$ by

$$
A \mathrel{\delta_{\mathcal{U}}} B \iff E[A] \cap B \neq \emptyset \text{ for every entourage } E ,
$$

where $E[A] = \{y : (x,y) \in E \text{ for some } x \in A\}$; equivalently, $A$ and $B$ are **not** close when some entourage separates them.

**Theorem.** The relation $\delta_{\mathcal{U}}$ is a proximity; it induces the uniform topology; a uniformly continuous map is a proximity map for the determined proximities; and an involution of $X$ is a proximity involution for $\delta_{\mathcal{U}}$ exactly when it preserves the closeness relation, which holds in particular when it is uniformly continuous.

**Proof.** The axioms (P1)–(P4) are the standard verification for the proximity of a uniformity, with (P4) using the two-step entourage; the induced topology is the uniform topology because $x \in \overline{A}$ iff every entourage neighbourhood of $x$ meets $A$. A uniformly continuous map carries close sets to close sets, since the preimage of an entourage is an entourage. For the involution, a uniformly continuous $\sigma$ preserves $\delta_{\mathcal{U}}$; the converse can hold without uniform continuity, since the proximity forgets the higher uniformity.

### Completion and the Involution

**Theorem.** Let $X$ be an involutive proximity space with completion $\hat X$: the complete separated proximity space containing $X$ as a dense subspace, which is the Smirnov compactification when the proximity is totally bounded. Then the involution $\sigma$ extends to exactly one proximity involution $\hat\sigma$ of $\hat X$, and the completion of the orbit space is the orbit space of the completion:

$$
\widehat{X/\sigma} \ \cong \ \hat X / \hat\sigma .
$$

**Proof.** The inclusion $X \to \hat X$ is a proximity map and $\hat X$ is complete and separated, so $\sigma : X \to X \subseteq \hat X$ extends uniquely to a proximity map $\hat\sigma : \hat X \to \hat X$, by the universal property of the completion for proximity maps into complete separated spaces; the composite $\hat\sigma\circ\hat\sigma$ extends the identity on the dense subspace, hence is the identity, so $\hat\sigma$ is an involution. The orbit map $\pi : X \to X/\sigma$ is a proximity map into a complete separated space, so it extends to $\hat X \to \widehat{X/\sigma}$ and descends to $\hat X/\hat\sigma \to \widehat{X/\sigma}$; conversely the composite $X \to \hat X \to \hat X/\hat\sigma$ extends from the dense subspace to $\widehat{X/\sigma} \to \hat X/\hat\sigma$. The two composites agree on the dense images and are therefore identities, so the maps are inverse proximity isomorphisms.

**Corollary.** For a totally bounded proximity the completion is compact Hausdorff, so the orbit space of a compact Hausdorff space with a continuous proximity involution is compact Hausdorff, obtained as the completion of the orbit proximity; and the orbit proximity is totally bounded when the proximity is.

**Proof.** The completion of a totally bounded proximity is compact Hausdorff by the Smirnov theorem; the orbit proximity is the quotient, and the completion of the orbit space is the orbit space of the completion by the theorem; a quotient of a totally bounded proximity by a proximity involution is totally bounded because closeness in the quotient lifts to closeness in the space.

## Summary

A proximity on a set is a symmetric, additive, nondegenerate and separating relation of closeness on its subsets; it induces a topology by $x \in \overline{A} \iff \{x\} \delta A$, and a proximity map is a map carrying close sets to close sets. An involutive proximity space has an involution preserving the closeness relation, so it is a proximity isomorphism and a homeomorphism, and its fixed set is a closed proximity subspace for a separated proximity. The orbit space carries the orbit proximity, defined by pulling back closeness along the orbit map; it is a proximity, it makes the orbit map a proximity map, it is the finest such, and it is separated when the proximity of the space is. Every uniformity determines a proximity preserving the topology, uniformly continuous maps are proximity maps, and a uniformly continuous involution is a proximity involution. The completion of an involutive proximity space carries a unique extended proximity involution, and the completion of the orbit space is the orbit space of the completion, $\widehat{X/\sigma} \cong \hat X/\hat\sigma$; for a totally bounded proximity the completion is compact Hausdorff, which is how the compact quotients of this category are produced.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\delta$ | The proximity relation; $A \delta B$ means $A$ is close to $B$ |
| (P1)–(P4) | Symmetry, additivity, nondegeneracy, separation of a proximity |
| proximity topology | $x \in \overline{A} \iff \{x\} \delta A$ |
| proximity map | $A \delta B \Rightarrow f(A) \delta' f(B)$ |
| $\sigma$ | A proximity involution; $A \delta B \iff \sigma A \delta\sigma B$ |
| $X^{\sigma}$ | The fixed set; closed for a separated proximity |
| $\tilde\delta$ | The orbit proximity; $U \tilde\delta V \iff \pi^{-1}U \delta \pi^{-1}V$ |
| finest proximity | The orbit proximity is the finest making $\pi$ a proximity map |
| $\delta_{\mathcal{U}}$ | The proximity determined by a uniformity $\mathcal{U}$ |
| $\hat X$, $\hat\sigma$ | The completion, and the extended proximity involution |
| $\widehat{X/\sigma} \cong \hat X/\hat\sigma$ | Completion commutes with the orbit functor |
| Smirnov compactification | The completion of a totally bounded proximity |

## Further Reading

- Somashekhar A. Naimpally and Brian D. Warrack, *Proximity Spaces* (Cambridge University Press, 1970), for the axioms of a proximity, proximity maps and the orbit construction.
- Ryszard Engelking, *General Topology* (Heldermann, revised ed. 1989), for proximity spaces, the proximity of a uniformity and the Smirnov compactification.
- Wolfgang J. Thron, *Topological Structures* (Holt, Rinehart and Winston, 1966), for the relation between proximity, uniformity and topology.
- Eduard Čech, *Topological Spaces* (Academia, 1966; revised English edition, Wiley, 1966), for proximity spaces, uniform spaces and the completion that the compactification defines.
- Nicolas Bourbaki, *General Topology*, Chapters 1–4 (Springer, 1995), for uniform spaces and the proximity they determine.
- John L. Kelley, *General Topology* (Van Nostrand, 1955; reprinted Springer, 1975), for uniform spaces, their proximities and their completions.
