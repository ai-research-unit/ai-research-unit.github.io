# __Involutive Uniform Spaces__

## Introduction

A uniform space is a set with a structure that controls the small neighbourhoods of the diagonal, and an **involutive uniform space** is a uniform space with an involution that carries the structure to itself, that is, an involution that is uniformly continuous. This is the pattern of the group `- * Theory` applied to the uniform structure: the structure is preserved by the involution rather than merely the topology. The article develops the three constructions that the uniform version requires and that the topological version does not: the **orbit uniformity** on the quotient, which is the finest uniformity making the orbit map uniformly continuous; the fixed set, which is closed in a separated space and is the obstruction to the action being free; and the **completion**, which carries an involution extending the given one and which commutes with the formation of the orbit space. The last of these is the exact sense in which the uniform theory is better behaved than the topological theory: the completion of the orbit space is the orbit space of the completion, so that the free involutions of complete spaces can be classified by their behaviour on the completion.

The article continues *Spaces with an Involution and the Orbit Space* for the topological picture of the involution and its orbits, and it uses the uniform spaces of this Part: the entourages, the uniform continuity, the separated spaces and the completion. The topological involution of *Involutions on a Topological Space and the Fixed Set* is the special case in which only the topology is required to be preserved; here the uniformity is preserved as well, and the results are correspondingly finer. Nothing analytic and nothing geometric is used: the uniformity is an abstract structure of entourages, no metric is assumed, and no length or angle is read from the spaces.

## Uniform Spaces and Their Involutions

### Uniform Structures

**Definition.** A **uniform structure** on a set $X$ is a filter $\mathcal{U}$ of subsets of $X \times X$, the **entourages**, such that

for every $E \in \mathcal{U}$ the diagonal $\Delta_{X} \subseteq E$; for every $E \in \mathcal{U}$ the inverse $E^{-1} \in \mathcal{U}$; and for every $E \in \mathcal{U}$ there is $D \in \mathcal{U}$ with $D \circ D \subseteq E$,

where $E^{-1} = \{(y,x) : (x,y) \in E\}$ and $D \circ D$ is the set of pairs joined by a two-step chain in $D$. A **uniform space** is a set with a uniform structure. The **uniform topology** has as neighbourhoods of $x$ the sets $E[x] = \{y : (x,y) \in E\}$ for $E \in \mathcal{U}$. The space is **separated** when the intersection of all the entourages is the diagonal.

**Definition.** A map $f : X \to Y$ of uniform spaces is **uniformly continuous** when for every entourage $F$ of $Y$ there is an entourage $E$ of $X$ with $(x,x') \in E \Rightarrow (f(x),f(x')) \in F$. A uniformly continuous map is continuous for the uniform topologies, and a bijection that is uniformly continuous with uniformly continuous inverse is a **uniform isomorphism**.

### Uniformly Continuous Involutions

**Definition.** An **involutive uniform space** is a uniform space $X$ with an involution $\sigma$ that is uniformly continuous; in symbols, for every entourage $E$ the set

$$
(\sigma \times \sigma)^{-1}(E) = \{(x,x') : (\sigma x, \sigma x') \in E\}
$$

is an entourage. The involution is then a **uniform involution**.

**Proposition.** A uniformly continuous involution is a uniform isomorphism; the set of entourages fixed by $(\sigma\times\sigma)$ is a base of the uniformity; and the fixed set $X^{\sigma}$ with the subspace uniformity is an involutive uniform space on which the involution is the identity.

**Proof.** $\sigma^{-1} = \sigma$ is uniformly continuous, so $\sigma$ is a uniform isomorphism. For an entourage $E$, the set $E \cap (\sigma\times\sigma)(E)$ is an entourage, is fixed by $(\sigma\times\sigma)$ because $(\sigma\times\sigma)$ is an involution of $X\times X$, and is contained in $E$; hence the fixed entourages form a base. The fixed set carries the entourages $E \cap (X^{\sigma}\times X^{\sigma})$, and the involution is the identity on it.

**Remark.** A uniform structure is finer than its topology, and two different uniform structures can induce the same topology; thus an involution that is continuous need not be uniformly continuous, and the involutive uniform space is a strictly stronger object than a topological space with a continuous involution. The completion below is the construction that most clearly separates the two.

## The Orbit Uniformity

### The Quotient Uniformity

**Definition.** Let $X$ be an involutive uniform space and $\pi : X \to X/\sigma$ the orbit map. The **orbit uniformity** on $X/\sigma$ is the uniformity generated as a filter by the sets

$$
(\pi \times \pi)(E), \qquad E \text{ a } \sigma\text{-invariant entourage of } X .
$$

**Theorem.** The sets $(\pi\times\pi)(E)$ for $\sigma$-invariant entourages $E$ form a base for a uniformity on $X/\sigma$; the orbit map is uniformly continuous for it; and the orbit uniformity is the finest uniformity on $X/\sigma$ making the orbit map uniformly continuous.

**Proof.** The diagonal is contained in every $(\pi\times\pi)(E)$ because $\Delta_{X} \subseteq E$. The inverse is contained because $E^{-1}$ is invariant when $E$ is, and $(\pi\times\pi)(E^{-1}) = (\pi\times\pi)(E)^{-1}$. For the composition, let $E$ be a $\sigma$-invariant entourage and choose an invariant $D$ with $D \circ D \subseteq E$, possible by intersecting a suitable entourage with its translate. If $[x]$ and $[y]$ are $(\pi\times\pi)(D)$-related and $[y]$ and $[z]$ are $(\pi\times\pi)(D)$-related, then there are representatives $x', y', y'', z'$ with $(x',y') \in D$ and $(y'',z') \in D$; since $y'$ and $y''$ are in the same orbit, say $y'' = \sigma^{k}y'$ with $k \in \{0,1\}$, the invariance of $D$ gives $(\sigma^{k}x', y'') \in D$, whence $(\sigma^{k}x', z') \in D \circ D \subseteq E$ and $([x],[z]) \in (\pi\times\pi)(E)$. Hence the base is a uniformity. Uniform continuity of $\pi$ is the definition; if another uniformity on $X/\sigma$ makes $\pi$ uniformly continuous, then it contains $(\pi\times\pi)(E)$ for every entourage $E$, hence contains the orbit uniformity, which is therefore the finest.

### The Orbit Map and Its Properties

**Theorem.** The orbit map is uniformly continuous, surjective and open for the uniform topologies, and it is the quotient map of the involution. If $X$ is separated then the orbit uniformity is separated.

**Proof.** The first clauses are the theorem and the fact that the orbit map is open and surjective in the topological quotient, which the uniform topology refines compatibly. For separatedness, let $(x,y)$ be in every entourage of the orbit uniformity, so that for every invariant entourage $E$ the pair $(\pi x, \pi y)$ lies in $(\pi\times\pi)(E)$; unwinding, for every entourage $E$ there are representatives with $(x', y') \in E$. Taking $E$ small in a separated space forces $x' = y'$ in the limit, that is, $\pi x = \pi y$; the argument is the standard one for the separation of the quotient uniformity.

**Remark.** The orbit uniformity is not the finest uniformity inducing the quotient topology; it is the finest uniformity making the orbit map uniformly continuous, and the two can differ when the topology does not determine the uniformity. This is the reason the completion behaves as it does.

## The Fixed Set

**Theorem.** The fixed set $X^{\sigma}$ of a uniform involution is closed in $X$ when $X$ is separated, and it is the set on which the involution is the identity; the involution restricts to a free involution of the complement when the space is separated, and the complement is open.

**Proof.** The fixed set is the preimage of the diagonal under the uniformly continuous map $x \mapsto (x, \sigma x)$, and the diagonal is closed in the product of a separated uniform space with itself; hence the fixed set is closed. The remaining clauses are the topological ones of *Involutions on a Topological Space and the Fixed Set*, valid because a uniform involution is continuous.

**Example.** On the real line with its usual uniformity the map $x \mapsto -x$ is a uniform involution; its fixed set is $\{0\}$, closed; the orbit space is the half-line with the quotient uniformity, and on the complement of the fixed set the orbit map is locally a uniform isomorphism.

**Example (a free uniform involution).** On the disjoint union $\mathbb{R} \sqcup \mathbb{R}$ the map exchanging the two copies is a free uniform involution, and its orbit space carries the uniformity of $\mathbb{R}$; on the real line itself the map $x \mapsto -x$ is a uniform involution with the fixed point $0$.

## Completion and the Involution

### The Extended Involution

**Theorem.** Let $X$ be an involutive uniform space with completion $\hat X$, the separated complete uniform space containing $X$ as a dense subspace. Then the involution $\sigma$ extends to exactly one uniformly continuous involution $\hat\sigma$ of $\hat X$, and the fixed set of $\hat\sigma$ is a closed set containing the closure of $X^{\sigma}$:

$$
\overline{X^{\sigma}} \ \subseteq \ (\hat X)^{\hat\sigma} .
$$

The containment can be strict, and it is strict exactly when the completion creates a fixed point that the closure of $X^{\sigma}$ does not contain.

**Proof.** The inclusion $X \to \hat X$ is uniformly continuous, and $\hat X$ is complete and separated, so the uniformly continuous map $\sigma : X \to X \subseteq \hat X$ extends uniquely to a uniformly continuous $\hat\sigma : \hat X \to \hat X$. The composite $\hat\sigma \circ \hat\sigma$ is a uniformly continuous extension of the identity on the dense subspace $X$, hence the identity by uniqueness; so $\hat\sigma$ is an involution. Its fixed set is closed, being the preimage of the diagonal of the separated space $\hat X \times \hat X$ under the continuous map $x \mapsto (x, \hat\sigma x)$, and it contains $X^{\sigma}$, hence also the closure of $X^{\sigma}$.

**Example (completion creates a fixed point).** On $X = \mathbb{R} \setminus \{0\}$ with its usual uniformity the involution $x \mapsto -x$ is free, and the fixed set of $\sigma$ is empty. The completion of $X$ is $\mathbb{R}$, the involution extends to $\hat\sigma(x) = -x$, and its fixed set is $\{0\}$, which strictly contains the closure of the empty set. So a free involution need not remain free after completion: the completion can add a fixed point at a hole of the space.

**Corollary.** If $X$ is separated then $X^{\sigma}$ is closed in $X$ and is a subspace of the fixed set of $\hat\sigma$; the involution $\sigma$ is free exactly when $X^{\sigma} = \emptyset$, but the extension $\hat\sigma$ is free only when the completion introduces no fixed point.

### Completion of the Orbit Space

**Theorem.** The completion of the orbit space is the orbit space of the completion:

$$
\widehat{X/\sigma} \ \cong \ \hat X / \hat\sigma ,
$$

by a uniform isomorphism, naturally in the involutive uniform space $X$. The orbit of a point of $X$ has for its image the orbit of the same point under $\hat\sigma$.

**Proof.** The orbit map $\pi : X \to X/\sigma$ is uniformly continuous and the completion $\widehat{X/\sigma}$ is complete and separated, so $\pi$ extends uniquely to a uniformly continuous map $\hat\pi : \hat X \to \widehat{X/\sigma}$; this map is $\hat\sigma$-invariant because $\pi\sigma = \pi$ and both sides are continuous extensions from the dense subspace $X$, so it descends to a uniformly continuous map $\hat X/\hat\sigma \to \widehat{X/\sigma}$. In the other direction, the composite $X \to \hat X \to \hat X/\hat\sigma$ is uniformly continuous and $\sigma$-invariant, so it factors through a uniformly continuous map $X/\sigma \to \hat X/\hat\sigma$; the target is complete and separated, since the quotient of a complete separated uniform space by a finite group of uniform isomorphisms is complete and separated, so this map extends to $\widehat{X/\sigma} \to \hat X/\hat\sigma$. The two composites are uniformly continuous and agree on the dense images of $X$ in each completion, so they are identities by uniqueness of the extension; hence the two maps are inverse uniform isomorphisms.

**Corollary.** The completion functor on involutive uniform spaces is compatible with the orbit functor: completing and then quotienting gives the same result as quotienting and then completing. In particular a free involution of a complete separated space restricts to the dense subspaces on which it is free, and the completion of a free involution of a space can acquire fixed points at the holes of the space, as the example above shows.

**Proof.** The theorem is the compatibility of the two functors on objects; the statement about free involutions is the corollary of the previous section.

## Summary

An involutive uniform space is a uniform space with a uniformly continuous involution, equivalently a uniform isomorphism of order two; the invariant entourages form a base of the uniformity, and the fixed set is a closed involutive uniform subspace when the space is separated. The orbit space carries the orbit uniformity, generated by the images of the invariant entourages, and it is the finest uniformity making the orbit map uniformly continuous; the orbit map is surjective, uniformly continuous and open, and the orbit uniformity is separated when the space is. The completion of the space carries a unique uniformly continuous involution extending the given one, its fixed set is closed and contains the closure of the fixed set of the given involution and may be strictly larger, and the completion of the orbit space is the orbit space of the completion, $\widehat{X/\sigma} \cong \hat X/\hat\sigma$. The uniform theory is thus compatible with the involution in a way that is finer than the topological theory: the completion, which is not visible topologically, is carried along by the involution.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{U}$ | The uniformity, a filter of entourages on $X \times X$ |
| $E^{-1}$, $D\circ D$ | Inverse and two-step composite of an entourage |
| $\Delta_{X}$ | The diagonal; contained in every entourage |
| separated | The intersection of the entourages is the diagonal |
| $\sigma$ | A uniform involution; uniformly continuous with $\sigma^{2} = \mathrm{id}$ |
| $(\sigma\times\sigma)$-invariant $E$ | An involutive uniform space's invariant entourage |
| $X^{\sigma}$ | The fixed set; closed for separated $X$ |
| $\pi : X \to X/\sigma$ | The orbit map, uniformly continuous and open |
| orbit uniformity | Generated by $(\pi\times\pi)(E)$ for invariant entourages $E$ |
| $\hat X$, $\hat\sigma$ | The completion, and the extended uniform involution |
| $\overline{X^{\sigma}} \subseteq (\hat X)^{\hat\sigma}$ | The fixed set of the completion contains the closure, possibly strictly |
| $\widehat{X/\sigma} \cong \hat X/\hat\sigma$ | Completion commutes with the orbit functor |

## Further Reading

- Nicolas Bourbaki, *General Topology*, Chapters 1–4 (Springer, 1995), for uniform spaces, entourages, uniform continuity, separatedness and the completion.
- John L. Kelley, *General Topology* (Van Nostrand, 1955; reprinted Springer, 1975), for the uniform structure, the quotient uniformity and the completion.
- Ryszard Engelking, *General Topology* (Heldermann, revised ed. 1989), for uniform spaces, the uniformity of a quotient and the extension of uniformly continuous maps to the completion.
- I. M. James, *Topological and Uniform Spaces* (Springer, 1987), for the comparison of the topological and the uniform structure and the quotient constructions.
- Andre Weil, *Sur les espaces à structure uniforme et sur la topologie générale* (Hermann, 1937), for the original theory of uniform spaces and the completion.
- Walter Roelcke and Susanne Dierolf, *Uniform Structures on Topological Groups and their Quotients* (McGraw-Hill, 1981), for quotient uniformities, completions and the functorial behaviour of the completion.
