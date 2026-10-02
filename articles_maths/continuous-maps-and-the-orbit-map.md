# __Continuous Maps and the Orbit Map__

## Introduction

An action of a group $G$ on a space $X$ is a family of homeomorphisms of $X$ indexed by the group, and it is continuous when this family depends continuously on the group element. The orbit map of *The Orbit Map* is the quotient map of the action, and it is continuous and open; this article reads the orbit map as a continuous operator in the company of the action itself, and it develops the two maps that the action induces: the map that a continuous equivariant map induces on the orbit spaces, and the **fixed-point set** $X^{G}$ on which the action is trivial. The induced map on the quotient is the functoriality of the construction $X \mapsto X/G$, and the fixed-point set is the other extreme of the same construction; the two together are the operator content of a group action as it is used in the equivariant theory of the later articles of this Part.

The article assumes *The Orbit Map* for the quotient topology, the universal property and the preimage and direct image operators of the orbit map, and *Continuous Maps as Operators* for the operator language. It treats an abstract group acting by homeomorphisms; the continuity of the action in a topology on $G$, the homogeneous space $G/H$, and the completion of the quotient belong to *Topological Groups*, later in this Part, and are named only where the two subjects meet. The involution is the special case $G = \mathbb{Z}/2$, and the articles of the group `- * Theory` take up that case in detail.

Nothing analytic and nothing geometric is used. The circle, the sphere and projective space occur only as quotients of an action, and no distance, length, angle or curvature is read from them.

## The Action as an Operator

### The Action and Its Homeomorphisms

**Definition.** An action of $G$ on a topological space $X$ is **continuous**, or the action is **by homeomorphisms**, when for every $g \in G$ the map

$$
\ell_{g} : X \longrightarrow X, \qquad \ell_{g}(x) = gx,
$$

is a homeomorphism. When $X$ and a topological group $G$ are both given, the action is **jointly continuous** when the map $G \times X \to X$, $(g,x) \mapsto gx$, is continuous for the product topology.

The assignment $g \mapsto \ell_{g}$ is a group homomorphism from $G$ to the group of homeomorphisms of $X$: $\ell_{e} = \mathrm{id}_{X}$ and $\ell_{gh} = \ell_{g}\ell_{h}$. The action is the same thing as this homomorphism, and the operator $\ell_{g}$ is the element of the action that acts on the space.

**Proposition.** Each $\ell_{g}$ is a homeomorphism with inverse $\ell_{g^{-1}}$, and it carries orbits to orbits: $\ell_{g}(Gx) = Gx$ for every $g$ and every $x$. Consequently every $\ell_{g}$ is a homeomorphism of each orbit and induces the identity map on the orbit space, $\pi \circ \ell_{g} = \pi$.

**Proof.** $\ell_{g}\ell_{g^{-1}} = \ell_{e} = \mathrm{id}$ and likewise in the other order, so $\ell_{g}$ is a bijection with continuous inverse. For the orbit statement, $\ell_{g}(Gx) = (gG)x = Gx$ since $gG = G$. The last identity is the orbit statement read through the orbit map.

The operators $\ell_{g}$ are the symmetries of the action. They are homeomorphisms of $X$ that preserve every orbit, and they are the reason the preimage operator of the orbit map lands in the invariant algebra: the invariant sets are exactly the sets carried to themselves by all the $\ell_{g}$.

### The Orbit Map as a Continuous Operator

**Theorem.** The orbit map $\pi : X \to X/G$ is continuous, surjective and open, and its fibres are the orbits.

**Proof.** This is the corresponding theorem of *The Orbit Map*: the quotient topology makes $\pi$ continuous, the orbits are the classes of the relation, and the openness uses only that each $\ell_{g}$ is a homeomorphism, since $\pi^{-1}(\pi(A)) = \bigcup_{g \in G}\ell_{g}(A)$ is a union of open sets when $A$ is open.

**Corollary.** The orbit map is a quotient map in the strong sense: a set $U \subseteq X/G$ is open if and only if $\pi^{-1}(U)$ is open, and a map out of $X/G$ is continuous if and only if its composite with $\pi$ is continuous.

**Proof.** The two statements are the definition of the quotient topology and its universal property, both in *The Orbit Map*.

The orbit map is therefore a continuous operator with all the good properties a surjection can have: open, surjective, with the quotient topology, and its preimage is the isomorphism of the algebra of the orbit space onto the algebra of invariant sets. The only property it can fail to have is closedness, which holds for finite $G$ and can fail for infinite $G$, and injectivity, which holds exactly for the trivial action.

## The Induced Map on the Quotient

### Equivariant Maps

**Definition.** Let $G$ act on $X$ and on $Y$ by homeomorphisms. A continuous map $f : X \to Y$ is **equivariant**, or a **$G$-map**, when

$$
f(gx) = g\,f(x) \qquad (g \in G,\ x \in X),
$$

writing the two actions with the same letter. When the two actions differ, the condition is written $f(gx) = g \cdot_{Y} f(x)$ and the two actions are distinguished by their spaces.

An equivariant map carries the orbit of $x$ into the orbit of $f(x)$: $f(Gx) \subseteq Gf(x)$. For a surjective equivariant map the inclusion is an equality, and then $f$ carries orbits onto orbits.

**Proposition.** The composite of two equivariant maps is equivariant, the identity is equivariant for the action on a single space, and a bijective equivariant map with equivariant inverse is an isomorphism of the two $G$-spaces.

**Proof.** Immediate from the definition and associativity of composition.

### The Induced Map on the Orbit Space

**Theorem.** Let $f : X \to Y$ be a continuous equivariant map. Then there is exactly one map

$$
\bar f : X/G \longrightarrow Y/G
$$

with $\bar f \circ \pi_{X} = \pi_{Y} \circ f$, and it is continuous. The assignment $f \mapsto \bar f$ preserves identities and composition, so $X \mapsto X/G$ is a functor from the category of $G$-spaces and equivariant maps to the category of topological spaces.

**Proof.** The composite $\pi_{Y} \circ f$ is continuous and constant on the orbits of $X$, since $f(Gx) \subseteq Gf(x)$ makes its value on the orbit of $x$ equal to the orbit of $f(x)$. By the universal property of *The Orbit Map* it factors through the orbit map of $X$ by a unique continuous $\bar f$. Functoriality is uniqueness: for $g : Y \to Z$ the composite $\overline{g \circ f}$ and $\bar g \circ \bar f$ have the same composite with $\pi_{X}$, so they are equal.

The induced map has the further property that it is the restriction of $f$ to the quotients: a point of $X/G$ is the orbit of $x$, and $\bar f$ sends it to the orbit of $f(x)$. In the language of operators, the square

$$
\pi_{Y} \circ f = \bar f \circ \pi_{X}
$$

is a naturality identity, and it says that the orbit map is a **natural transformation** from the functor $X \mapsto X$ to the functor $X \mapsto X/G$. The transformation is not an isomorphism for a nontrivial action, and the failure of injectivity of $\pi$ is exactly the failure of the two functors to agree.

**Corollary.** A continuous map $f : X \to Y$ that is not equivariant need not induce a map on the quotients. It induces one exactly when it is equivariant, that is, exactly when it carries each orbit into an orbit.

**Proof.** The induced map is well defined on orbits precisely when $f(x)$ and $f(x')$ lie in the same orbit whenever $x$ and $x'$ do; for the action of $G$ on $X$ this is the condition $f(Gx) \subseteq Gf(x)$, which is equivariance. Continuity of the induced map is the universal property.

### The Equivariant Universal Property

**Theorem.** Let $Y$ carry the trivial action, $gy = y$ for all $g$. Then every continuous map $f : X \to Y$ is equivariant, and the correspondence $f \leftrightarrow \bar f$ is a bijection

$$
\{\, \text{continuous } f : X \to Y \,\} \ \longleftrightarrow \ \{\, \text{continuous } \bar f : X/G \to Y \,\} .
$$

**Proof.** With the trivial action on $Y$, equivariance is the condition $f(gx) = f(x)$, which is invariance, and the stated bijection is the universal property of the orbit map proved in *The Orbit Map*.

The theorem identifies the orbit space as the **coequaliser** of the action: mapping out of $X/G$ is the same as mapping out of $X$ while killing the action. It also shows that the fixed-point set and the orbit space are dual in the simplest possible way: maps out of the quotient are the invariant maps, and maps into the quotient are the orbits.

## The Fixed Points

### The Fixed Set

**Definition.** The **fixed set** of the action is

$$
X^{G} = \{\, x \in X : gx = x \text{ for every } g \in G \,\} = \bigcap_{g \in G} X^{g},
$$

where $X^{g} = \mathrm{Fix}(g)$ is the set of fixed points of the single homeomorphism $\ell_{g}$.

A point is fixed exactly when its orbit is a singleton, so the points of $X^{G}$ are the orbits of the action that are single points, and $X^{G}$ is a union of orbits. The complementary extreme is a **free** action, one for which $X^{G} = \emptyset$ and every stabiliser is trivial; the free case is the subject of the next group of articles.

**Proposition.** The fixed set is the set of common fixed points of the operators $\ell_{g}$. An equivariant map $f : X \to Y$ satisfies $f(X^{G}) \subseteq Y^{G}$.

**Proof.** The first statement is the definition. For the second, if $x \in X^{G}$ then $g f(x) = f(gx) = f(x)$ for every $g$, so $f(x)$ is fixed.

The fixed-point assignment is functorial: it sends an equivariant map to its restriction $f|_{X^{G}} : X^{G} \to Y^{G}$. On a single space the fixed set carries the subspace topology.

### Closedness of the Fixed Set

**Theorem.** The fixed set $X^{G}$ is closed in $X$ when $X$ is Hausdorff and the action is by homeomorphisms.

**Proof.** For a single $g$ the fixed set $X^{g}$ is the set of points where the two continuous maps $\mathrm{id}_{X}$ and $\ell_{g}$ agree, so it is the preimage of the diagonal $\Delta_{X} \subseteq X \times X$ under the continuous map $x \mapsto (x, gx)$. When $X$ is Hausdorff the diagonal is closed, so $X^{g}$ is closed. The fixed set of the whole action is the intersection of the closed sets $X^{g}$, hence closed.

**Corollary.** If the group is generated by finitely many elements $g_{1}, \ldots, g_{n}$ with each $\ell_{g_{i}}$ continuous, then $X^{G} = X^{g_{1}} \cap \cdots \cap X^{g_{n}}$ is closed for a Hausdorff $X$. In particular the fixed set of an involution of a Hausdorff space is closed.

**Proof.** If $G$ is generated by the $g_{i}$, a point is fixed by every element exactly when it is fixed by each generator, and a finite union of closed sets is closed. An involution generates a group of order two, so the case of one generator is the case of an involution.

The closedness uses the Hausdorff hypothesis and fails without it. Let $L$ be the line with two origins, the quotient of $\mathbb{R} \times \{0,1\}$ by the identification $(x,0) \sim (x,1)$ for $x \neq 0$, and let $\sigma$ exchange the two copies; the map descends to a continuous involution of $L$ with no fixed point among the origins, since $\sigma$ interchanges them. The fixed set of $\sigma$ is the image of $\{(x,i) : x \neq 0\}$, a copy of $\mathbb{R} \setminus \{0\}$, and it is not closed in $L$, because each of the two origins is a limit point of it. The space $L$ is not Hausdorff, and this is exactly what the proof uses: the diagonal of $L \times L$ is not closed, so the equaliser of $\mathrm{id}$ and $\sigma$ need not be closed.

### Fixed Points and the Orbit Map

**Theorem.** Let the action be by homeomorphisms. Then the orbit map restricts to a homeomorphism

$$
\pi|_{X^{G}} : X^{G} \longrightarrow \pi(X^{G}) ,
$$

and its image $\pi(X^{G})$ is the set of singleton orbits. Every orbit of a fixed point is a singleton, and the preimage of a singleton orbit is a singleton.

**Proof.** If $x$ is fixed then $\pi^{-1}(\pi(x)) = Gx = \{x\}$, so the restriction is injective; it is continuous because $\pi$ is, and it is open because $\pi$ is open, so it is a homeomorphism onto its image. The image consists exactly of the singleton orbits, and the last statement is the definition of a singleton fibre together with the orbit description.

**Corollary.** The fixed set is a union of orbits on which the quotient map is injective, and the complement of the fixed set in an orbit consists of the nonfixed points. If the action is free, the fixed set is empty and the orbit map is injective nowhere except on the empty set.

**Proof.** The fixed set is a union of its singleton orbits, and every other point has an orbit of at least two points.

**Remark.** The image $\pi(X^{G})$ need not be closed in $X/G$ even when $X^{G}$ is closed in $X$: the quotient map need not be closed for an infinite group. When $G$ is finite the orbit map is closed, so the image of the closed fixed set is closed. This is the same finiteness hypothesis that governs closedness of the orbit map in *The Orbit Map*.

## Worked Examples

**Example (a translation action).** Let $G = \mathbb{Z}$ act on $\mathbb{R}$ by $n \cdot x = x + n$. No point is fixed, so $X^{G} = \emptyset$ and the action is free; the orbit space is the circle. An equivariant map is $f(x) = x + h(x)$ with $h$ continuous and of period one, since $f(x+n) = f(x)+n$ forces $h(x+n) = h(x)$; the induced map on the circle is the map that this function defines on the quotient.

**Example (a finite order action).** Let $G = \mathbb{Z}/2$ act on the sphere $S^{n}$ by the antipodal map. The action is free, so $X^{G} = \emptyset$; the orbit space is real projective space; and every equivariant map $S^{n} \to S^{n}$ induces a map $\mathbb{RP}^{n} \to \mathbb{RP}^{n}$.

**Example (an action with fixed points).** Let $G = \mathbb{Z}/2$ act on the sphere $S^{n}$ by the involution $\sigma(x_{0}, x_{1}, \ldots, x_{n}) = (-x_{0}, x_{1}, \ldots, x_{n})$. The fixed set is the sphere $S^{n-1} = \{x : x_{0} = 0\}$, which is closed, and the orbit map restricts to a homeomorphism of it onto its image in the quotient. The quotient is obtained from the closed hemisphere $\{x : x_{0} \geq 0\}$ by identifying each boundary point $x$ with $\sigma(x)$, and the image of the fixed set is the image of the boundary sphere. This is the prototypical action with a fixed set of positive dimension, and it is the model for the equivariant structures of the next articles.

**Example (a trivial action).** Let $G$ act by $gx = x$. Then $X^{G} = X$, every orbit is a singleton, the orbit map is a homeomorphism, and every continuous map $X \to Y$ with a trivial action on $Y$ is equivariant. The example is the degenerate case in which the orbit space and the fixed set coincide.

## Summary

An action of a group on a space is a homomorphism into its homeomorphism group, and it is continuous when each group element acts by a homeomorphism. The orbit map is continuous, surjective and open, with the orbits as fibres, and it is the quotient map of the action. A continuous equivariant map between two spaces with actions induces a unique continuous map on the orbit spaces, and the assignment is a functor; a map that is not equivariant induces no map on the quotients, and a map into a space with the trivial action always does, which is the universal property of the quotient. The fixed set $X^{G}$ is the intersection of the fixed sets $X^{g}$ of the individual homeomorphisms; it is closed when the space is Hausdorff, because each $X^{g}$ is the equaliser of $\mathrm{id}$ and $\ell_{g}$ and the diagonal of a Hausdorff space is closed; and an equivariant map carries the fixed set into the fixed set. The orbit map restricts to a homeomorphism of the fixed set onto the set of singleton orbits, which need not be closed when the group is infinite and is closed when the group is finite.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G$, $X$, $Y$ | A group, and two spaces with actions of $G$ by homeomorphisms |
| $\ell_{g}$ | The homeomorphism $x \mapsto gx$ |
| $\pi_{X} : X \to X/G$ | The orbit map of $X$; continuous, surjective and open |
| equivariant, $G$-map | $f(gx) = g f(x)$; the maps that induce maps on the quotients |
| $\bar f$ | The induced map $X/G \to Y/G$, unique with $\bar f\pi_{X} = \pi_{Y} f$ |
| $X \mapsto X/G$ | The quotient functor on $G$-spaces and equivariant maps |
| trivial action | $gy = y$; then every continuous map into $Y$ is equivariant |
| $X^{G}$, $X^{g}$ | The fixed set of the whole action, and of the single element $g$ |
| $\mathrm{Fix}(g)$, $\ell_{g}$ | The same set as $X^{g}$, in the operator notation |
| free action | $X^{G} = \emptyset$ and every stabiliser trivial |
| $\pi|_{X^{G}}$ | A homeomorphism onto the set of singleton orbits |
| $\Delta_{X}$ | The diagonal in $X \times X$, closed exactly when $X$ is Hausdorff |

## Further Reading

- James R. Munkres, *Topology* (Prentice Hall, 2nd ed. 2000), for quotient maps, the universal property and the induced maps on quotients.
- Nicolas Bourbaki, *General Topology*, Chapters 1–4 (Springer, 1995), for the action of a group by homeomorphisms and the fixed points of a family of maps.
- Glen E. Bredon, *Introduction to Compact Transformation Groups* (Academic Press, 1972), for the functoriality of the orbit space, the fixed-point set and the equivariant maps.
- Tammo tom Dieck, *Transformation Groups* (de Gruyter, 1987), for the equivariant category, the fixed-point functors and their adjointness with the orbit functor.
- Saunders Mac Lane, *Categories for the Working Mathematician*, 2nd ed. (Springer, 1998), for natural transformations, functors and coequalisers.
- Ryszard Engelking, *General Topology* (Heldermann, revised ed. 1989), for the closedness of the fixed set of a family of continuous maps into a Hausdorff space.
