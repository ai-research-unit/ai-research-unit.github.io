# __The Orbit Map__

## Introduction

A group $G$ acting on a set $X$ partitions it into orbits, and the orbit map sends a point to the orbit that contains it. When $X$ is a space and the action is by homeomorphisms, the orbit map becomes a continuous operator whose target carries the quotient topology, and the whole of the theory of quotients by an action is the theory of this one map. This article develops that operator: the preimage of a set of orbits is the union of the orbits it contains, so the orbit map reads the subsets of the quotient as exactly the $G$-invariant subsets of $X$; the direct image is the saturation operator, and it is the lower adjoint of the preimage in the order of the power sets. The quotient topology is then identified once: it is the finest topology on the set of orbits making the orbit map continuous, and it is the topology whose open sets are the invariant open sets of $X$.

The article treats an abstract group acting by homeomorphisms. When the group carries a topology and the action is required to be continuous in both variables, the orbit map is the quotient of a topological group by a subgroup, and the extra hypotheses and consequences — the openness of the orbit map as a map of groups, the Hausdorffness of the quotient, the existence of slices — belong to *Topological Groups*, later in this Part, and are named here only where the two subjects meet. The general quotient construction is that of *Topological Spaces*, whose identification topology is used with its meaning.

The operator language is the one fixed in *Continuous Maps as Operators*: a map carries the preimage operator, which is a Boolean and lattice homomorphism and defines continuity, and the direct image operator, which is its lower adjoint on the power sets. The orbit map is the first instance in which the preimage is not only a homomorphism but a **bijection onto a subalgebra**, the algebra of invariant sets, and the article is largely the statement and the exploitation of that fact. Nothing analytic and nothing geometric is used: no distance is chosen, and no length, angle or curve occurs.

## The Orbit Map of an Action

### Actions and Orbits

**Definition.** An **action** of a group $G$ on a set $X$ is a map $G \times X \to X$, written $(g,x) \mapsto gx$, with $ex = x$ and $(gh)x = g(hx)$ for all $g, h \in G$ and $x \in X$. The **orbit** of $x$ is the set $Gx = \{gx : g \in G\}$; the **stabiliser** of $x$ is the subgroup $G_x = \{g : gx = x\}$; the point $x$ is **fixed** by $G$ when $Gx = \{x\}$, equivalently $G_x = G$. The **orbit space** $X/G$ is the set of orbits, and the **orbit map** is

$$
\pi : X \longrightarrow X/G, \qquad \pi(x) = Gx .
$$

Two points lie in the same orbit exactly when one is carried to the other by an element of $G$, and this is an equivalence relation: reflexivity is $ex = x$, symmetry is $x = g^{-1}(gx)$, transitivity is $(gh)x = g(hx)$. The orbits are the equivalence classes, so they partition $X$, and the orbit map is the quotient map of that partition.

**Proposition.** The stabilisers of two points in the same orbit are conjugate: for $y = gx$,

$$
G_{gx} = g\,G_x\,g^{-1}.
$$

Consequently the orbit is $\{gx : g \in G\}$, and the assignment $gG_x \mapsto gx$ is a bijection of the set of left cosets of the stabiliser onto the orbit.

**Proof.** $h \in G_{gx}$ iff $hgx = gx$ iff $g^{-1}hg \in G_x$ iff $h \in gG_xg^{-1}$. The second statement is the same computation read on the left cosets: $gG_x = g'G_x$ iff $g^{-1}g' \in G_x$ iff $gx = g'x$.

The proposition is the set-theoretic skeleton of every orbit-space computation, and it is recorded here because the fibres of the orbit map are its orbits: $\pi^{-1}(\pi(x)) = Gx$, of cardinality $|G|/|G_x|$ when $G$ is finite.

### The Quotient Topology

From this point $X$ is a topological space and the action is **by homeomorphisms**: for every $g \in G$ the map $x \mapsto gx$ is a homeomorphism of $X$. No topology is placed on $G$.

**Definition.** The **orbit topology** on $X/G$ is the quotient (identification) topology of *Topological Spaces* for the surjection $\pi$: a set $U \subseteq X/G$ is open when $\pi^{-1}(U)$ is open in $X$. With this topology the orbit space is the **quotient of $X$ by $G$**, and the orbit map $\pi$ is the **quotient map**.

The definition is not a choice: the quotient topology is the finest topology on $X/G$ making $\pi$ continuous, and it is the only topology with the universal property proved below.

**Theorem.** The orbit map $\pi$ is continuous and surjective, and

$$
\pi^{-1}(U) = \bigcup_{O \in U} O \quad \text{for } U \subseteq X/G,
$$

so the preimage of a set of orbits is a union of orbits. A subset $U \subseteq X/G$ is open if and only if its preimage is open in $X$, if and only if its preimage is a $G$-invariant open set of $X$.

**Proof.** Continuity is the definition of the quotient topology. For the formula, $x \in \pi^{-1}(U)$ iff $\pi(x) \in U$ iff the orbit of $x$ is a member of $U$. The set $\pi^{-1}(U)$ is a union of orbits, hence invariant: $g\pi^{-1}(U) = \pi^{-1}(U)$ for every $g$, since $g$ permutes each orbit. Conversely an invariant set $W$ satisfies $W = \pi^{-1}(\pi(W))$, so it is the preimage of a set of orbits.

## The Orbit Map as an Operator

### The Preimage and the Invariant Subsets

A subset $A \subseteq X$ is **invariant** under $G$, or **saturated**, when $gA = A$ for every $g \in G$, equivalently when $A = \pi^{-1}(\pi(A))$, equivalently when $A$ is a union of orbits. The invariant subsets form a subalgebra of the Boolean algebra $\mathcal{P}(X)$: they are closed under complement, finite and arbitrary unions and intersections, and they contain $\emptyset$ and $X$. The algebra is written $\mathcal{P}(X)^{G}$.

**Theorem.** The preimage operator of the orbit map,

$$
\pi^{-1} : \mathcal{P}(X/G) \longrightarrow \mathcal{P}(X)^{G},
$$

is a bijection onto the invariant subalgebra, and it is an isomorphism of Boolean algebras and of complete lattices: it preserves $\emptyset$, $X/G$, arbitrary unions, arbitrary intersections and complements.

**Proof.** The map is well defined by the theorem above, and it lands in the invariant sets. It is injective because $\pi$ is surjective: $\pi^{-1}(U) = \pi^{-1}(V)$ implies $U = \pi(\pi^{-1}(U)) = \pi(\pi^{-1}(V)) = V$. It is surjective onto the invariant sets because an invariant $W$ equals $\pi^{-1}(\pi(W))$. It preserves the Boolean operations because the preimage does, by *Continuous Maps as Operators*.

The theorem is the precise sense in which the subsets of the orbit space are the invariant subsets of $X$: the preimage identifies the two algebras, and the orbit map gives an isomorphism of the algebra of the quotient onto the algebra of invariants, read backwards. The inverse is the direct image.

### Saturation and the Direct Image

**Definition.** The **saturation** of a subset $A \subseteq X$ is

$$
\operatorname{sat}(A) = \pi^{-1}(\pi(A)) = \bigcup_{x \in A} Gx = \bigcup_{g \in G} gA ,
$$

the smallest invariant set containing $A$. The **direct image** of the orbit map is the map $\pi_{*} : \mathcal{P}(X) \to \mathcal{P}(X/G)$ sending $A$ to the set of orbits that meet $A$.

**Proposition.** The saturation is a closure operator on the power set: it is extensive, monotone and idempotent, and it preserves arbitrary unions. It is the composite $\pi^{-1}\pi_{*}$, and its image is the invariant subalgebra.

**Proof.** $A \subseteq \operatorname{sat}(A)$ because $x \in Gx$; monotonicity and union preservation are the corresponding properties of the preimage and the direct image; idempotence is $\pi^{-1}\pi_{*}\pi^{-1}\pi_{*} = \pi^{-1}\pi_{*} $, which uses $\pi_{*}\pi^{-1} = \mathrm{id}$ on the quotient and $\pi^{-1}\pi_{*} = \mathrm{id}$ on the invariants. The image is the invariant subalgebra by the previous theorem.

The saturation is the operator that sends a set to the union of the orbits it meets. It is not the closure of a topology; it is the closure operator of the partition into orbits, and the two are compared in *Continuous Maps and the Orbit Map*, where a group action and a topology on the same space are read together.

### The Adjoint Pair

**Theorem.** The direct image and the preimage of the orbit map are adjoint,

$$
\pi_{*} \dashv \pi^{-1}, \qquad \pi_{*}(A) \subseteq U \iff A \subseteq \pi^{-1}(U),
$$

and the preimage is a bijection onto the invariants, so the unit and the counit of the adjunction are the saturation and the identity:

$$
\pi^{-1}\pi_{*}(A) = \operatorname{sat}(A), \qquad \pi_{*}\pi^{-1}(U) = U .
$$

**Proof.** The adjunction is the Galois connection of *Continuous Maps as Operators* for the particular map $\pi$. The two composites are the definitions: $\pi^{-1}\pi_{*}(A)$ is the union of the orbits meeting $A$, and $\pi_{*}\pi^{-1}(U)$ is the set of orbits contained in the union of the orbits of $U$, which is $U$.

The adjunction is a **reflection**: the preimage is fully faithful, the counit is an isomorphism, and the invariant subalgebra is a reflective subcategory of the power set, with the saturation the reflection. This is the operator content of the orbit map, and it is what makes the quotient computable: a statement about subsets of $X/G$ is a statement about invariant subsets of $X$.

## The Universal Property

### Invariant Maps

**Definition.** A map $f : X \to Y$ is **$G$-invariant** when $f(gx) = f(x)$ for all $g \in G$ and $x \in X$, equivalently when $f$ is constant on each orbit, equivalently when $f$ factors through $\pi$ as a map of sets.

**Theorem (universal property of the orbit map).** Let $f : X \to Y$ be a continuous $G$-invariant map. Then there is exactly one map $\bar f : X/G \to Y$ with $f = \bar f \circ \pi$, and $\bar f$ is continuous when $X/G$ carries the orbit topology.

**Proof.** For existence, $\bar f(Gx) = f(x)$ is well defined because $f$ is constant on the orbit. For uniqueness, $\pi$ is surjective. For continuity, compute the preimage: $\pi^{-1}(\bar f^{-1}(V)) = f^{-1}(V)$ is open for open $V$, and a set of orbits is open exactly when its preimage is open.

The theorem characterises the orbit topology: any topology on $X/G$ for which every continuous invariant map out of $X$ factors continuously through $\pi$ must contain the orbit topology, and the orbit topology is the finest such. The orbit map is therefore the **coequaliser** of the maps $(g, \cdot)$ and the projection, in the category of topological spaces, and it is initial among the quotients of $X$ that identify each orbit to a point.

**Corollary.** The continuous functions on the orbit space are exactly the continuous invariant functions on $X$, and the correspondence $f \leftrightarrow \bar f$ is a bijection.

**Proof.** Every continuous $\bar f$ gives a continuous invariant $f = \bar f\pi$; every continuous invariant $f$ gives a unique continuous $\bar f$ by the theorem; the two assignments are inverse because $\pi$ is surjective.

### The Identification of the Quotient Topology

**Proposition.** The orbit topology is the unique topology on $X/G$ with the universal property of the theorem. It is also the **final** topology for the single map $\pi$: the finest topology making $\pi$ continuous.

**Proof.** Let $\sigma$ be a topology on $X/G$ with the universal property. The identity map from $(X/G,\sigma)$ to $(X/G,\text{orbit})$ is continuous: its composite with $\pi$ is $\pi$, which is continuous for $\sigma$ by definition, so the universal property applies to $\sigma$ with the target the orbit space. Symmetrically the identity in the other direction is continuous, so the two topologies agree. The final topology is the orbit topology by the previous subsection.

The identification is worth stating because it is what a reader uses: the orbit topology is not an extra datum, it is forced by the requirement that the orbit map be continuous and that no unnecessary open sets be added.

## Properties of the Orbit Map

### Openness, Closedness and the Fibres

**Theorem.** If the action is by homeomorphisms, the orbit map is **open**: for open $A \subseteq X$, the set $\pi(A)$ is open, since

$$
\pi^{-1}(\pi(A)) = \bigcup_{g \in G} gA
$$

is a union of open sets. The orbit map is **closed** when the action is by homeomorphisms and $G$ is finite, since then $\pi^{-1}(\pi(F)) = \bigcup_{g \in G} gF$ is a finite union of closed sets; for an infinite $G$ it need not be closed.

**Proof.** The invariance formula is the definition of the saturation, and $gA$ is open for each $g$ because $g$ is a homeomorphism. The closed statement is the same with $F$ closed and the union finite.

The fibres of the orbit map are the orbits, and the map is injective on the fixed set: if $x$ is fixed then $\pi^{-1}(\pi(x)) = \{x\}$. In general the restriction

$$
\pi|_{X^{G}} : X^{G} \longrightarrow \pi(X^{G})
$$

is a homeomorphism onto its image, where $X^{G} = \{x : Gx = \{x\}\}$ is the fixed set.

**Proposition.** The orbit map is a homeomorphism exactly when the action is trivial; it is injective exactly when every orbit is a singleton, that is, exactly when $X = X^{G}$.

**Proof.** The orbit map is injective precisely when distinct points lie in distinct orbits, which is the same as every orbit being a singleton. A continuous open bijection is a homeomorphism.

### Examples

**Example (a translation action).** Let $G = \mathbb{Z}$ act on $\mathbb{R}$ by $n \cdot x = x + n$. The orbits are the cosets of $\mathbb{Z}$, the orbit space is the circle, and the orbit map is the standard quotient $\mathbb{R} \to \mathbb{R}/\mathbb{Z}$. The invariant open sets of $\mathbb{R}$ are the unions of cosets, and they are exactly the preimages of the open sets of the circle; the saturation of an open interval is the union of the cosets it meets.

**Example (the antipodal action).** Let $G = \mathbb{Z}/2$ act on the sphere $S^{n}$ by $x \mapsto -x$. The action is free, every orbit has two points, and the orbit space is real projective space $\mathbb{RP}^{n}$. The orbit map is open and closed, since $G$ is finite, and the invariant subsets of $S^{n}$ are those closed under the antipodal pairing.

**Example (a trivial action on a nontrivial space).** Let $G$ act on a space $X$ by $gx = x$. Every orbit is a singleton, $\pi$ is a homeomorphism, and the invariant subsets are all subsets; the universal property degenerates to the statement that every continuous map is invariant.

**Example (a free action of a finite group).** Let $G = \mathbb{Z}/3$ act on the circle $S^{1}$ by a homeomorphism of order three with no fixed points, for instance by the map that carries $z$ to $\omega z$ with $\omega = e^{2\pi i/3}$ on the unit circle. The orbit map is a three-sheeted covering and the quotient is again a circle. The action is free, so the fibres have three points, and $\pi$ is open and closed.

**Remark.** The orbit space of an action of a topological group on a Hausdorff space is not automatically Hausdorff, and the failure for the group $\mathbb{Z}/2$ is the subject of *Spaces with an Involution and the Orbit Space*, where the exact condition is identified. For an abstract group acting by homeomorphisms the general criterion is the closedness of the orbit equivalence relation in $X \times X$, used there in the special case of an involution.

## Summary

Let a group $G$ act on a topological space $X$ by homeomorphisms. The orbits partition $X$, the orbit map $\pi$ sends a point to its orbit, and the orbit space $X/G$ carries the quotient topology: a set of orbits is open exactly when its preimage, a union of orbits, is open in $X$. The orbit map is continuous, surjective and open; its fibres are the orbits; it is closed when $G$ is finite and need not be when $G$ is infinite; and it is a homeomorphism exactly when the action is trivial. As an operator the orbit map has a preimage that is a bijection onto the Boolean algebra of invariant subsets of $X$ and preserves all the Boolean and lattice operations, and a direct image that is the saturation operator and the lower adjoint of the preimage in a Galois connection whose unit is the saturation and whose counit is the identity. The universal property identifies the quotient topology uniquely: every continuous map out of $X$ that is constant on the orbits factors uniquely through a continuous map on $X/G$. The continuous functions on the quotient are exactly the continuous invariant functions on $X$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G$ | A group, acting on a set or space |
| $X$, $Y$ | Topological spaces; $X$ carries the action |
| $Gx$, $G_x$ | The orbit of $x$, and its stabiliser |
| $X/G$, $\pi$ | Orbit space, and the orbit map $\pi(x) = Gx$ |
| orbit topology | $U \subseteq X/G$ open iff $\pi^{-1}(U)$ open; the quotient topology |
| $X^{G}$ | The fixed set $\{x : Gx = \{x\}\}$ |
| invariant, saturated set | A union of orbits; $gA = A$; $A = \pi^{-1}(\pi(A))$ |
| $\mathcal{P}(X)^{G}$ | The Boolean subalgebra of invariant subsets |
| $\pi^{-1}$ | Preimage operator: a Boolean and lattice isomorphism onto $\mathcal{P}(X)^{G}$ |
| $\pi_{*}$ | Direct image operator: $A \mapsto$ the set of orbits meeting $A$ |
| $\operatorname{sat}(A)$ | Saturation $\pi^{-1}\pi_{*}(A) = \bigcup_{g} gA$, a closure operator |
| $\pi_{*} \dashv \pi^{-1}$ | The adjunction; $\pi^{-1}\pi_{*} = \operatorname{sat}$, $\pi_{*}\pi^{-1} = \mathrm{id}$ |
| $G$-invariant map | A map constant on orbits; $f = \bar f \circ \pi$ |
| $\bar f$ | The induced map on the orbit space, unique and continuous |
| $\mathbb{R}/\mathbb{Z}$, $S^{1}$, $\mathbb{RP}^{n}$ | The standard orbit spaces of the examples |

## Further Reading

- James R. Munkres, *Topology* (Prentice Hall, 2nd ed. 2000), for quotient maps, the identification topology and the universal property.
- Nicolas Bourbaki, *General Topology*, Chapters 1–4 (Springer, 1995), for the identification topology and the quotient by a group action.
- John L. Kelley, *General Topology* (Van Nostrand, 1955; reprinted Springer, 1975), for the quotient map as a coequaliser and the invariance of the saturation.
- Saunders Mac Lane, *Categories for the Working Mathematician*, 2nd ed. (Springer, 1998), for reflective subcategories, the unit and the counit of an adjunction.
- Ryszard Engelking, *General Topology* (Heldermann, revised ed. 1989), for the quotient topology and its preservation properties.
- Glen E. Bredon, *Introduction to Compact Transformation Groups* (Academic Press, 1972), for the orbit space of a group action and the slice theorems that a topological group supplies.
