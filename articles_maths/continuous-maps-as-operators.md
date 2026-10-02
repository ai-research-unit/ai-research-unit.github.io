# __Continuous Maps as Operators__

## Introduction

A continuous map $f : X \to Y$ is a map of spaces, and every map of spaces acts on the structures the spaces carry. It pulls back an open set of $Y$ to an open set of $X$, and this **preimage operator** $f^{-1}$ is the whole of continuity: the map is continuous exactly when $f^{-1}$ carries $\mathcal{O}(Y)$ into $\mathcal{O}(X)$. It also pushes forward a subset of $X$ to a subset of $Y$, and the two operators are adjoint to one another in the order of the power sets. Reading a continuous map as a pair of operators on the algebras of open sets, and reading composition as composition of operators, is the entry point of this article.

The article develops the preimage operator and the direct image operator, the adjunction between them, the functoriality of the assignment $f \mapsto f^{-1}$ — contravariant on the spaces, covariant on the algebras — and the induced map on the algebra of open sets together with what it preserves and what it does not. It is the operator layer of the distance: the operators it studies are the maps of the topological category itself, read on the lattice of open sets, and every later article of the operator group adds a further operator on top of them.

The background is *Topological Spaces*: open and closed sets, the interior and the closure, continuity, and the subspace, product and quotient topologies. What the preimage does to a topology, and how a topology is generated, is the content of *Topological Spaces* and is used here without repetition. The map $x \mapsto gx$ of a group action, which is the second source of operators in this group, is the subject of *The Orbit Map*; the operators that a closure and an interior are in their own right are the subject of *Operators on a Fixed Set*. Nothing analytic is used — no derivative, no integral and no measure — and nothing geometric: no distance is chosen, so no length, angle or curvature occurs.

## The Two Operators of a Map

### The Preimage Operator

Throughout, $X$ and $Y$ are topological spaces and $f : X \to Y$ is a map. The power set of $X$ is written $\mathcal{P}(X)$ and the family of open sets is written $\mathcal{O}(X)$, so that $\mathcal{O}(X) \subseteq \mathcal{P}(X)$; a subset of $X$ is written $A$, and its complement is written $A^{c}$.

**Definition.** The **preimage operator** of $f$ is the map

$$
f^{-1} : \mathcal{P}(Y) \longrightarrow \mathcal{P}(X), \qquad f^{-1}(B) = \{x \in X : f(x) \in B\}.
$$

Its restriction to the open sets is written $f^{-1} : \mathcal{O}(Y) \to \mathcal{O}(X)$ when that restriction is under discussion.

The preimage is determined by the implication $x \in f^{-1}(B) \iff f(x) \in B$, and it extends the map on points: for a singleton, $f^{-1}(\{y\})$ is the fibre of $f$ over $y$.

**Proposition (the preimage is a lattice homomorphism).** For every family $(B_i)_{i \in I}$ in $\mathcal{P}(Y)$ and all $B, C \subseteq Y$,

$$
f^{-1}\Bigl(\bigcup_{i \in I} B_i\Bigr) = \bigcup_{i \in I} f^{-1}(B_i), \qquad
f^{-1}(B \cap C) = f^{-1}(B) \cap f^{-1}(C), \qquad
f^{-1}(B^{c}) = f^{-1}(B)^{c},
$$

and consequently $f^{-1}(\emptyset) = \emptyset$ and $f^{-1}(Y) = X$.

**Proof.** For the union, $x$ lies in the left side exactly when $f(x) \in B_i$ for some $i$, which is the right side. The intersection and the complement are the same computation on the two clauses. The last two identities are the cases of the empty union and of the union of the whole family.

The preimage therefore preserves arbitrary unions, finite intersections and complements; it is a homomorphism of the **Boolean algebra** $\mathcal{P}(Y)$ into $\mathcal{P}(X)$, and a homomorphism of the **complete lattice** of subsets for arbitrary joins and finite meets. It reverses no order: $f^{-1}$ is monotone, $B \subseteq C \Rightarrow f^{-1}(B) \subseteq f^{-1}(C)$.

**Theorem (continuity is the preimage condition).** The map $f$ is continuous if and only if $f^{-1}(V) \in \mathcal{O}(X)$ for every $V \in \mathcal{O}(Y)$; in that case $f^{-1}$ restricts to a map of the open lattices, and it also restricts to a map of the closed lattices, $f^{-1} : \mathcal{F}(Y) \to \mathcal{F}(X)$, where $\mathcal{F}$ denotes the closed sets.

**Proof.** The first statement is the definition of continuity in the preimage form. For the second, if $F \subseteq Y$ is closed then $f^{-1}(F) = f^{-1}(F^{c})^{c}$ is the complement of the open set $f^{-1}(F^{c})$, hence closed.

### The Direct Image and the Adjunction

**Definition.** The **direct image operator** of $f$ is the map

$$
f_{*} : \mathcal{P}(X) \longrightarrow \mathcal{P}(Y), \qquad f_{*}(A) = \{f(x) : x \in A\} = f(A).
$$

Unlike the preimage, the direct image is not a Boolean homomorphism: it preserves unions, $f_{*}(\bigcup_i A_i) = \bigcup_i f_{*}(A_i)$, but it does not preserve complements, and it preserves intersections only for maps that are injective on the sets in question. It is monotone as well.

**Theorem (the Galois connection).** For $A \subseteq X$ and $B \subseteq Y$,

$$
f_{*}(A) \subseteq B \iff A \subseteq f^{-1}(B).
$$

**Proof.** Both sides say that $f(x) \in B$ for every $x \in A$: the left says every value $f(x)$ with $x \in A$ lies in $B$, and the right says every $x \in A$ lies in the set of points mapped into $B$.

The theorem is a **Galois connection** between the two power sets ordered by inclusion, with $f_{*}$ the lower and $f^{-1}$ the upper adjoint; equivalently, $f_{*} \dashv f^{-1}$. Two consequences are used repeatedly. The preimage is the **largest** $A$ with $f_{*}(A) \subseteq B$, and the direct image is the **smallest** $B$ with $A \subseteq f^{-1}(B)$; taking $B = f_{*}(A)$ gives $A \subseteq f^{-1}(f_{*}(A))$, and taking $A = f^{-1}(B)$ gives $f_{*}(f^{-1}(B)) \subseteq B$. Equality holds on a set $A$ exactly when $A$ is **saturated**, that is, a union of fibres, and on a set $B$ exactly when $B$ is contained in the image of $f$.

**Corollary.** The preimage commutes with every union and every intersection, the direct image with every union; the preimage is injective exactly when $f$ is surjective, and the direct image is injective exactly when $f$ is injective.

**Proof.** The commutation with unions is the proposition above. For intersections, the preimage side is the proposition; for the direct image, $f_{*}(\bigcap_i A_i) \subseteq \bigcap_i f_{*}(A_i)$ always, and the reverse inclusion fails exactly when two points of distinct $A_i$ have the same image. The injectivity statements follow by applying the adjunction to singletons: $f^{-1}$ has trivial kernel on singletons exactly when every $y$ has a preimage, and $f_{*}$ does exactly when no fibre has two points.

### Continuity in the Operator Language

The adjunction lets continuity be stated without naming a single open set twice, and it is worth doing so, because the same pattern recurs for the orbit map and for the equivariant maps of the later articles.

**Theorem.** The map $f$ is continuous if and only if

$$
f_{*}\bigl(\overline{A}\bigr) \subseteq \overline{f_{*}(A)}, \qquad A \subseteq X,
$$

where the closures are taken in $X$ and in $Y$; equivalently, if and only if $f^{-1}$ carries closed sets to closed sets, or if and only if $\overline{f^{-1}(B)} \subseteq f^{-1}(\overline{B})$ for every $B \subseteq Y$.

**Proof.** The first form is the closure criterion of *Topological Spaces*: a point of $f_{*}(\overline A)$ has a preimage $x \in \overline A$, every neighbourhood of $x$ meets $A$, and continuity carries the image of such a neighbourhood into a neighbourhood of $f(x)$, so every neighbourhood of $f(x)$ meets $f_{*}(A)$ and $f(x) \in \overline{f_{*}(A)}$. The equivalence with the closed-set form is the theorem of the first subsection. The third form is the preimage of the closure criterion applied to $B$: $f_{*}(\overline{f^{-1}(B)}) \subseteq \overline{f_{*}(f^{-1}(B))} \subseteq \overline B$ by the adjunction, and applying $f^{-1}$ gives the displayed inclusion.

A continuous map, therefore, is a map whose direct image does not increase the closure and whose preimage does not decrease it. The two statements are the same statement read through the adjunction.

## Functoriality

### Composition and the Identity

**Theorem.** For maps $f : X \to Y$ and $g : Y \to Z$,

$$
(g \circ f)^{-1} = f^{-1} \circ g^{-1}, \qquad (g \circ f)_{*} = g_{*} \circ f_{*}, \qquad \mathrm{id}_{X}^{-1} = \mathrm{id}_{\mathcal{P}(X)} .
$$

If $f$ and $g$ are continuous then so is $g \circ f$, and the identities above hold with $\mathcal{O}$ and $\mathcal{F}$ in place of $\mathcal{P}$.

**Proof.** For the first, $x \in (g \circ f)^{-1}(C)$ iff $g(f(x)) \in C$ iff $f(x) \in g^{-1}(C)$ iff $x \in f^{-1}(g^{-1}(C))$. The direct image is the same computation in the other order, and the identity is immediate. Continuity of a composite is the statement that $(g \circ f)^{-1} = f^{-1} \circ g^{-1}$ carries open sets to open sets when each factor does.

The two assignments are therefore **functors**, and they run in opposite directions. The preimage is a **contravariant** functor from the category of topological spaces and continuous maps to the category of algebras: it reverses the arrows, sending $f : X \to Y$ to $f^{-1} : \mathcal{P}(Y) \to \mathcal{P}(X)$. The direct image is a **covariant** functor on the same category with the same objects.

**Corollary (the contravariance is not a defect).** The preimage of an inclusion is a restriction, $(\iota_{A})^{-1}(B) = B \cap A$, and the preimage of a constant map is either the whole space or the empty set. The preimage of a homeomorphism is a Boolean and lattice isomorphism, and $f$ is a homeomorphism exactly when $f^{-1}$ is a bijection of the open lattices that is an order isomorphism.

**Proof.** The restriction formula is the definition; the homeomorphism statement is that a bijection carries the topology of $X$ onto the topology of $Y$ exactly when it and its inverse are continuous.

### The Category of Open Lattices

The preimage operator forgets the points and keeps the lattice, and a natural question is how much is lost. For a map of spaces the assignment $X \mapsto \mathcal{O}(X)$ with $f \mapsto f^{-1}$ is a contravariant functor into the category whose objects are the complete lattices and whose morphisms preserve arbitrary joins and finite meets — the homomorphisms displayed in the proposition above. This functor remembers the topology and the map on open sets, but not the points of $X$ that no open set distinguishes; two spaces with the same lattice of opens are the same space.

**Proposition.** A bijection $f : X \to Y$ is a homeomorphism if and only if $f^{-1} : \mathcal{O}(Y) \to \mathcal{O}(X)$ is bijective.

**Proof.** If $f$ is a homeomorphism, $f^{-1}$ on subsets is a bijection carrying the topology of $Y$ onto that of $X$. Conversely, if the restriction of $f^{-1}$ to the open sets is a bijection onto $\mathcal{O}(X)$, then every open set of $X$ is the preimage of an open set of $Y$, so $f$ is continuous and open, and a continuous open bijection is a homeomorphism.

The proposition says that the open lattice is a complete invariant of the topology, and the functor of preimages is faithful on homeomorphisms. It is not an equivalence with the whole category of spaces, since a map of lattices in the reverse direction need not come from a continuous map to each point; the spaces whose points are recovered from the lattice are the $T_0$ spaces, and the reconstruction is the subject of the point-free topology named in the Further Reading.

## The Induced Map on the Algebra of Open Sets

### What the Preimage Preserves

For a continuous $f$ the preimage restricts to a map

$$
f^{-1} : \mathcal{O}(Y) \longrightarrow \mathcal{O}(X)
$$

which preserves the empty set, the whole set, arbitrary unions and finite intersections. These are exactly the operations from which the topology is built, so the restriction is the induced map on the algebra of open sets that the menu of this article names: the algebra is the open lattice, and the induced map is the preimage.

**Theorem.** For a continuous $f$ the restricted preimage $f^{-1} : \mathcal{O}(Y) \to \mathcal{O}(X)$ preserves the whole set, finite intersections and arbitrary unions, and it therefore has a **right adjoint** in the order of the lattices, given by

$$
f_{\forall}(U) = \bigcup \{\, V \in \mathcal{O}(Y) : f^{-1}(V) \subseteq U \,\},
$$

so that $f^{-1} \dashv f_{\forall}$, that is,

$$
f^{-1}(V) \subseteq U \iff V \subseteq f_{\forall}(U)
$$

for every open $U \subseteq X$ and every open $V \subseteq Y$. The preimage has a **left adjoint** exactly when it preserves all intersections of open sets, and when it exists that adjoint sends $W$ to the smallest open set of $Y$ containing $f_{*}(W)$.

**Proof.** The preimage of the whole set is the whole set and the preimage commutes with intersections, so the restriction to open sets preserves the top and finite meets; it commutes with arbitrary unions, so $f_{\forall}(U)$ is a legitimate open set, being a union of open sets. For the equivalence, if $f^{-1}(V) \subseteq U$ then $V$ is one of the open sets whose union is $f_{\forall}(U)$, so $V \subseteq f_{\forall}(U)$; conversely $f^{-1}(f_{\forall}(U)) = \bigcup \{f^{-1}(V) : f^{-1}(V) \subseteq U\} \subseteq U$, so $V \subseteq f_{\forall}(U)$ gives $f^{-1}(V) \subseteq f^{-1}(f_{\forall}(U)) \subseteq U$. For the left adjoint, a monotone map of complete lattices has a left adjoint exactly when it preserves all meets; when it does, the left adjoint is the meet $\bigwedge\{V : W \subseteq f^{-1}(V)\}$, the smallest open set containing $f_{*}(W)$.

The two adjoints of the preimage on the powersets are the direct image and the **universal image**

$$
\forall_{f}(A) = \{\, y \in Y : f^{-1}(\{y\}) \subseteq A \,\},
$$

and the pair satisfies $f_{*} \dashv f^{-1} \dashv \forall_{f}$ on the Boolean algebras. The restriction of this triple to the open lattices keeps only the lower adjunction of the preimage, because the direct image of an open set need not be open and the universal image of an open set need not be open. This is the reason the open lattice carries one adjunction and the power set two.

### What the Preimage Does Not Preserve

The restriction of $f^{-1}$ to the open sets does not determine the direct image, and the direct image of an open set need not be open. The right adjoint $f_{\forall}$ repairs the defect from the side of the target: $f_{\forall}(U)$ is the largest open set of $Y$ whose preimage lies in $U$, and it is the best open approximation to a direct image that the preimage operator can certify.

**Example (an open set whose image is not open).** Let $f : \mathbb{R} \to \mathbb{R}$ be the map $f(x) = x^{2}$ in the usual topology. The image of the open interval $(-1, 1)$ is $[0, 1)$, which is not open; its interior is $(0,1)$. The function is continuous and not open, and the failure of openness is exactly the failure of $f_{*}$ to land in $\mathcal{O}(\mathbb{R})$. Its right adjoint is the operator $f_{\forall}$: the largest open $V \subseteq \mathbb{R}$ with $f^{-1}(V) \subseteq (-2,2)$ is $V = (-4,4)$, since $f^{-1}((-4,4)) = (-2,2)$ and any larger open set contains a value above $4$, whose preimage leaves $(-2,2)$.

**Example (a closed map that is not open).** The inclusion $\iota : [0,1] \to \mathbb{R}$ is closed and continuous; it is not open, since $[0,1]$ is open in itself and its image is not open in $\mathbb{R}$. The preimage operator of $\iota$ is $B \mapsto B \cap [0,1]$, which is surjective onto the open sets of the subspace and preserves all the lattice operations.

**Remark.** A continuous bijection need not have continuous inverse, so the induced map on the open lattices need not be bijective even when the map on points is: the identity from the discrete topology to the trivial topology on a set with two points is a continuous bijection whose preimage operator is injective but not surjective onto the open sets. The point of the operator language is that this is visible as a property of $f^{-1}$ alone.

## Summary

Every map $f : X \to Y$ carries two operators on the power sets: the preimage $f^{-1}$, which is a homomorphism of the Boolean algebra and of the complete-lattice structure and is the operator that defines continuity, and the direct image $f_{*}$, which preserves unions and is the lower adjoint of the preimage in the Galois connection $f_{*}(A) \subseteq B \iff A \subseteq f^{-1}(B)$. The map is continuous exactly when the preimage restricts to the open sets, equivalently to the closed sets, equivalently when the direct image does not increase closures. Composition is composition of operators, so the preimage is a contravariant functor and the direct image a covariant one, and the identity map gives the identity operator. On the algebra of open sets the restricted preimage preserves the whole set, finite intersections and arbitrary unions, so it has a right adjoint $f_{\forall}$, the largest open set whose preimage lies in a given open set, and a left adjoint exactly when it preserves all intersections; the direct image of an open set need not be open, and that failure is why the open lattice keeps only the one adjunction. A homeomorphism is exactly a bijection whose preimage operator is a bijection of the open lattices, so the open lattice is a complete invariant of the topology.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $X, Y, Z$ | Topological spaces |
| $f, g$ | Maps, continuous when a continuity hypothesis is in force |
| $\mathcal{P}(X)$ | Power set of $X$, as a Boolean algebra and complete lattice |
| $\mathcal{O}(X)$, $\mathcal{F}(X)$ | Lattice of open sets, lattice of closed sets of $X$ |
| $A, B, C$ | Subsets; $U, V, W$ open; $F$ closed; $A^{c}$ the complement of $A$ |
| $f^{-1}$ | Preimage operator, $f^{-1}(B) = \{x : f(x) \in B\}$ |
| $f_{*}$, $f(A)$ | Direct image operator, $f_{*}(A) = \{f(x) : x \in A\}$ |
| $f_{*}(A) \subseteq B \iff A \subseteq f^{-1}(B)$ | The Galois connection; $f_{*} \dashv f^{-1}$ |
| $\forall_{f}(A)$ | Universal image $\{y : f^{-1}(\{y\}) \subseteq A\}$; $f^{-1} \dashv \forall_{f}$ |
| saturated set | A set $A$ with $f^{-1}(f_{*}(A)) = A$, a union of fibres |
| $\overline{A}$, $\operatorname{int} A$ | Closure and interior; $\partial A$ the boundary |
| $f_{\forall}$ | Right adjoint of the restricted preimage: the largest open $V \subseteq Y$ with $f^{-1}(V) \subseteq U$ |
| $T_0$ | The separation axiom under which the open lattice determines the points |

## Further Reading

- James R. Munkres, *Topology* (Prentice Hall, 2nd ed. 2000), for continuity, the preimage and the closure criterion in their standard form.
- Nicolas Bourbaki, *General Topology*, Chapters 1–4 (Springer, 1995), for the algebra of the preimage and the induced maps on open and closed sets.
- Garrett Birkhoff, *Lattice Theory* (American Mathematical Society, 3rd ed. 1967), for Galois connections, adjoint pairs of lattice maps and their calculus.
- Peter T. Johnstone, *Stone Spaces* (Cambridge University Press, 1982), for the open lattice as a frame and for the point-free reading of a continuous map.
- Steven Vickers, *Topology via Logic* (Cambridge University Press, 1989), for the point-free topology and the reconstruction of the points from the lattice of opens.
- Ryszard Engelking, *General Topology* (Heldermann, revised ed. 1989), for the categorical properties of the category of topological spaces and its functors.
