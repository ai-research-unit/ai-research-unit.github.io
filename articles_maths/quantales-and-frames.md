
# __Quantales and Frames__

## Introduction

This is the fifth article of the Boolean system in Part V, and it occupies the **algebra slot** of that system for the *complete* and *topological* reading of the domain. The preceding articles developed the Boolean, Heyting, MV and effect algebras as finitary structures: finite meets, binary joins, a total or partial sum. Here the order is completed — arbitrary joins are available and finite meets distribute over them — and the resulting algebras are the **frames**, the algebraic form of a topological space, together with their non-idempotent generalisation, the **quantales**. This is the last of the algebraic articles of the Boolean category, and it is the one that connects the category to the topological slot.

The boundary against the general theory is deliberate. Topological spaces, open sets, continuity, compactness and sobriety are the subject of *Topological Spaces*, and the open-set lattice is used here as the standard example rather than constructed. The finitary Heyting structure was developed in *Heyting Algebras and Intuitionistic Logic*; the present article completes it. The Boolean case — Stone duality, the prime ideal space, the compact totally disconnected spaces — is not covered here, the topological slot of this category, and it is cited rather than repeated. The operator-algebraic and measure-theoretic quantales are not developed; only the algebraic theory and the pointfree topology are given.

Throughout, a frame is written $L$ and a quantale $Q$; a locale is a frame read in the opposite category and is also written $L$. The two-element frame is $\mathbf{2} = \{0,1\}$, and the open-set frame of a topological space $X$ is $\mathcal{O}(X)$. The category of frames, with frame homomorphisms, is **Frm**, and the category of locales is its opposite $\mathbf{Loc} = \mathbf{Frm}^{\mathrm{op}}$. The name *frame* is used for the algebra and *locale* for the same object when it is being used as a space; this dual usage is standard and is stated once here.

## Frames

### Complete Lattices and the Distribution Axiom

**Definition.** A **frame** is a complete lattice $L$ in which the finite meets distribute over arbitrary joins:

$$
a \wedge \bigvee_{i \in I} b_i = \bigvee_{i \in I} (a \wedge b_i)
$$

for every $a \in L$ and every family $(b_i)_{i \in I}$. A **frame homomorphism** is a map $f : L \to M$ preserving finite meets, including the empty meet $1$, and arbitrary joins, including the empty join $0$.

**Theorem.** Every frame is a complete Heyting algebra, with

$$
a \to b = \bigvee \{c \in L : c \wedge a \leq b\},
$$

and conversely every complete Heyting algebra is a frame. The underlying lattice of a frame is distributive.

**Proof.** The element displayed is the largest $c$ with $c\wedge a \leq b$ by the distribution axiom, so it is the relative pseudocomplement and residuation holds; this is the definition of a complete Heyting algebra. Conversely, in a complete Heyting algebra the distribution axiom follows from residuation: for every $i$ one has $a\wedge b_i \leq a\wedge\bigvee_i b_i$, so $\bigvee_i(a\wedge b_i)\leq a\wedge\bigvee_i b_i$, while $a\wedge\bigvee_i b_i \leq \bigvee_i(a\wedge b_i)$ follows by applying the adjunction to the element $\bigvee_i(a\wedge b_i)$, which satisfies $c\wedge a\leq \bigvee_i b_i$. Distributivity is immediate from the axiom applied to finite joins. $\square$

**Example (open sets).** Let $X$ be a topological space. The open sets, ordered by inclusion, form a frame $\mathcal{O}(X)$: the join of a family of open sets is its union, the meet of two is the intersection, and the distribution axiom is the set-theoretic identity

$$
U \cap \bigcup_{i} V_i = \bigcup_{i} (U \cap V_i).
$$

The relative pseudocomplement is $U \to V = \operatorname{int}\bigl((X \setminus U)\cup V\bigr)$, and the pseudocomplement is $\neg U = \operatorname{int}(X \setminus U)$, as in *Heyting Algebras and Intuitionistic Logic*. Every frame of the form $\mathcal{O}(X)$ is **spatial**, in the sense defined below.

**Example (ideals and down-sets).** Let $R$ be a commutative ring and let $\operatorname{Id}(R)$ be the set of ideals ordered by inclusion; it is a complete lattice under arbitrary sums and intersections, and it is a frame. Its elements are the ideals, not the ring. Let $P$ be a poset and let $\operatorname{Dn}(P)$ be the set of down-sets ordered by inclusion; arbitrary unions and intersections of down-sets are down-sets, and the distribution axiom holds, so $\operatorname{Dn}(P)$ is a frame. These two frames are the homes of the ideal theory of *Rings* and of the order theory of *Order Theory and Lattices*.

**Example (complete Boolean algebras).** Every complete Boolean algebra is a frame, since a Boolean algebra is distributive and the join is arbitrary; by the theorem above it is therefore a complete Heyting algebra. A Boolean algebra is a frame exactly when it is complete as a lattice, so an incomplete Boolean algebra is not one. The measure algebra of *Measure Theory and Integration* is the standard atomless complete Boolean algebra, and being atomless it is not spatial as a locale, its point space being empty.

### Nuclei and Sublocales

**Definition.** A **nucleus** on a frame $L$ is a map $j : L \to L$ that is monotone and extensive ($a \leq j(a)$), idempotent, and preserves finite meets: $j(a\wedge b) = j(a)\wedge j(b)$ and $j(1) = 1$. The **fixed-point set** is

$$
L_j = \{a \in L : j(a) = a\}.
$$

**Theorem.** For every nucleus $j$ on a frame $L$, the fixed-point set $L_j$ is a frame for the order inherited from $L$, with joins $\bigvee_i a_i$ computed as $j\bigl(\bigvee_i a_i\bigr)$ and meets computed as in $L$; the map $j$ is a frame homomorphism onto $L_j$, and this correspondence is a bijection between nuclei and **sublocales** of $L$.

**Proof.** The set $L_j$ is closed under meets because $j$ preserves them, and it contains $1$. The join of a family in $L_j$ must be the least fixed point above the family, which is $j(\bigvee_i a_i)$; that this is fixed follows from idempotence and that it is the least follows from monotonicity. The distribution axiom in $L_j$ follows from the distribution axiom in $L$ and the preservation of meets. The correspondence with surjective frame homomorphisms is the standard equivalence between quotient frames and nuclei. $\square$

**Example (the double-negation nucleus).** The map $j(a) = \neg\neg a$ is a nucleus on any frame, as in *Heyting Algebras and Intuitionistic Logic*; its fixed points are the **regular elements**. For $L = \mathcal{O}(X)$ they are the regular open sets, and $L_j$ is the complete Boolean algebra of regular open sets, the **Booleanization** of the frame. It is the smallest dense sublocale of $L$: it contains no new open sets and every element of $L$ has a dense interior in $L_j$.

**Example (the open-set nucleus).** For a subspace $Y \subseteq X$, the map $U \mapsto U \cap Y$ on $\mathcal{O}(X)$ is not a nucleus; the correct construction is to take the frame $\mathcal{O}(Y)$, which is the image of the frame homomorphism $\mathcal{O}(X) \to \mathcal{O}(Y)$, $U \mapsto U\cap Y$. The nuclei of $\mathcal{O}(X)$ are exactly the sublocales, which include more than the subspaces: the sublocales of a locale form a frame under the reverse of inclusion, and the empty sublocale and the whole locale are among them.

## Locales and Pointfree Topology

### The Category of Locales

A continuous map $f : X \to Y$ of topological spaces induces a frame homomorphism $f^{-1} : \mathcal{O}(Y) \to \mathcal{O}(X)$, $V \mapsto f^{-1}(V)$, because preimages preserve unions and finite intersections. The assignment $X \mapsto \mathcal{O}(X)$ is therefore a contravariant functor on spaces, and it is turned into a covariant functor by passing to the opposite category.

**Definition.** The category **Loc** of **locales** is the opposite of the category **Frm** of frames and frame homomorphisms; a morphism $L \to M$ of locales is a frame homomorphism $M \to L$. The **open-set functor** is $\mathcal{O} : \mathbf{Top} \to \mathbf{Loc}$, and the **points** of a locale $L$ are the frame homomorphisms $p : L \to \mathbf{2}$; the set of points is written $\operatorname{pt}(L)$, with the topology whose open sets are

$$
\operatorname{pt}(L)_a = \{p : p(a) = 1\}, \qquad a \in L .
$$

The assignment $L \mapsto \operatorname{pt}(L)$ is a functor $\operatorname{pt} : \mathbf{Loc} \to \mathbf{Top}$.

**Theorem.** The functor $\mathcal{O}$ is left adjoint to $\operatorname{pt}$:

$$
\operatorname{Hom}_{\mathbf{Loc}}(\mathcal{O}(X), L) \cong \operatorname{Hom}_{\mathbf{Top}}(X, \operatorname{pt}(L)),
$$

the unit $X \to \operatorname{pt}(\mathcal{O}(X))$ assigns to a point $x$ the frame homomorphism $U \mapsto 1$ if $x \in U$ and $0$ otherwise.

**Proof.** A continuous map $g : X \to \operatorname{pt}(L)$ determines the frame homomorphism $L \to \mathcal{O}(X)$, $a \mapsto \{x : g(x)(a) = 1\}$, and conversely a frame homomorphism $L \to \mathcal{O}(X)$ determines $g$ by the same formula. The two assignments are mutually inverse and natural, which is the adjunction. The unit is the special case. $\square$

### Spatial and Sober Objects

**Definition.** A locale $L$ is **spatial** if the frame homomorphism

$$
L \longrightarrow \mathcal{O}(\operatorname{pt}(L)), \qquad a \mapsto \operatorname{pt}(L)_a,
$$

is an isomorphism; equivalently, if the points separate the elements of $L$. A topological space $X$ is **sober** if every nonempty closed irreducible subset of $X$ is the closure of a unique point.

**Theorem.** The adjunction $\mathcal{O} \dashv \operatorname{pt}$ restricts to an equivalence between the full subcategory of sober spaces and the full subcategory of spatial locales. In particular the open-set functor is full and faithful on sober spaces, and every locale is the quotient of a spatial locale by a sublocale.

**Proof.** The unit $X \to \operatorname{pt}(\mathcal{O}(X))$ is a homeomorphism exactly when $X$ is sober, and the counit is an isomorphism exactly when $L$ is spatial; the general adjunction theorem then gives the equivalence on the fixed objects. The last statement is the standard factorization of a locale through its spatial reflection and its Booleanization. $\square$

**Proposition.** If $X$ is a Hausdorff space then $X$ is sober. Every finite topological space is sober, and every totally ordered set with the order topology is sober.

**Proof.** In a Hausdorff space an irreducible closed set is a singleton: if $F$ were irreducible and contained two distinct points $x,y$, disjoint neighbourhoods of them would separate $F$ into two proper closed subsets. The finite and order-topology cases are checked directly. $\square$

**Remark.** Not every locale is spatial, and a locale can have no points at all. The standard examples are constructed from nuclei that leave only $0$ as a fixed point, giving the empty sublocale as the space of points while retaining a nontrivial algebra; the details are in *Stone Spaces*. This is the precise sense in which pointfree topology is not the topology of a set of points: the frame, not its spectrum, is the primary object, and the points are recovered only when they exist in sufficient supply.

### Compactness in Locales

**Definition.** A locale $L$ is **compact** if every subset $S \subseteq L$ with $\bigvee S = 1$ has a finite subset $F \subseteq S$ with $\bigvee F = 1$. It is **Hausdorff**, or **regular**, if the corresponding pointfree separation condition holds, formulated in the frame.

**Theorem.** If $X$ is a compact topological space then $\mathcal{O}(X)$ is a compact locale, and if $X$ is compact Hausdorff then $\mathcal{O}(X)$ is a compact Hausdorff locale. Conversely a spatial compact locale is $\mathcal{O}(X)$ for a compact space $X$.

**Proof.** The cover condition for $X$ is the statement that a family of open sets with union $X$ has a finite subfamily with union $X$, which is exactly the compactness of $\mathcal{O}(X)$; the spatial converse follows from the equivalence of the previous theorem. The Hausdorff locale conditions are the pointfree translations of the separation axioms and agree with the topological ones for spatial locales. $\square$

**Example (the Zariski locale).** Let $R$ be a commutative ring and let $\operatorname{Rad}(R)$ be its frame of radical ideals, ordered by inclusion. The **Zariski locale** of $R$ is this frame; its points are the prime ideals of $R$, and they form the Zariski spectrum of *Rings*. The construction is the algebraic prototype of a locale: the spectrum is recovered as the points, and the frame is the primary datum. The same construction with the frame of open sets of a space is the topological prototype, and the two are the standard examples of the theory.

## Quantales

### The Axioms

**Definition.** A **quantale** is a complete lattice $Q$ with an associative binary operation $\cdot$ that distributes over arbitrary joins on both sides:

$$
a \cdot \bigvee_i b_i = \bigvee_i (a \cdot b_i), \qquad \bigvee_i a_i \cdot b = \bigvee_i (a_i \cdot b) .
$$

A quantale is **unital** if it has an element $e$ with $e\cdot a = a\cdot e = a$ for all $a$, and **commutative** if $\cdot$ is commutative. A **quantale homomorphism** preserves arbitrary joins and the multiplication, and the unit when there is one.

**Theorem.** A frame is exactly a quantale $Q$ in which the multiplication is commutative and agrees with the meet, $a \cdot b = a \wedge b$. In that case $1$ is a unit, the multiplication is idempotent, and the quantale axioms reduce to the frame axiom.

**Proof.** In a frame the meet is commutative and associative with unit $1$, and it distributes over arbitrary joins by the frame axiom, so the frame is a quantale with $\cdot = \wedge$. Conversely, if in a quantale the multiplication is the meet, then the distribution axiom of the frame is exactly the distribution of $\cdot$ over arbitrary joins, and the lattice is complete by hypothesis. $\square$

**Example (relations).** Let $X$ be a set and let $Q = \mathcal{P}(X \times X)$ be the set of binary relations on $X$, ordered by inclusion. The join is union, and the product is composition of relations:

$$
R \cdot S = \{(x,z) : \text{there is } y \text{ with } (x,y) \in R \text{ and } (y,z) \in S\}.
$$

Composition is associative and distributes over arbitrary unions, and the identity relation is the unit, so $Q$ is a unital quantale, non-commutative when $X$ has at least two elements. This is the standard non-commutative example, and it is the quantale of the monoid $X$ under the discrete structure.

**Example (ideals of a ring).** Let $R$ be a commutative ring and let $\operatorname{Id}(R)$ be its frame of ideals. The product of ideals, $IJ = \{\sum_k i_k j_k : i_k \in I, j_k \in J\}$, is associative and distributes over arbitrary sums of ideals, and the unit ideal $R$ is the unit; hence $\operatorname{Id}(R)$ is a commutative unital quantale whose join is the sum of ideals. The ideals form both a frame and a quantale, and the two structures are different: the frame operations are intersection and sum, the quantale product is the ideal product. This is the algebraic example that shows the quantale axioms to be strictly weaker than the frame axioms.

**Example (the free quantale).** For a monoid $M$, the power set $\mathcal{P}(M)$ with

$$
A \cdot B = \{ab : a \in A,\ b \in B\}, \qquad \bigvee_i A_i = \bigcup_i A_i
$$

is a unital quantale, and it is the free unital quantale on the monoid $M$; when $M$ is the free monoid on a set, this is the quantale of formal languages. The construction is the quantale analogue of the free Boolean algebra of *Boolean Algebras and Lattices*.

### Modules, Involutions and the Relation to Frames

**Definition.** A **left module** over a quantale $Q$ is a complete lattice $M$ with an action $Q \times M \to M$, $(a,x)\mapsto a\cdot x$, associative and distributing over joins in both variables. An **involution** on a quantale is a map ${}^{*}$ with $a^{**} = a$, $(a\cdot b)^{*} = b^{*}\cdot a^{*}$ and $(\bigvee_i a_i)^{*} = \bigvee_i a_i^{*}$; the pair is an **involutive quantale**.

**Theorem.** Let $Q$ be an involutive quantale. Then the involution is an order isomorphism, and its fixed points,

$$
Q^{*} = \{a \in Q : a^{*} = a\},
$$

form a frame for the order inherited from $Q$, with the joins and meets of $Q$.

**Proof.** The involution preserves arbitrary joins by hypothesis and is its own inverse, so it is a poset isomorphism and preserves arbitrary meets as well; the fixed points are therefore closed under arbitrary joins and meets, and they inherit the distribution of the multiplication from $Q$. $\square$

**Example (the quantale of a group).** Let $G$ be a group and let $Q = \mathcal{P}(G)$ with convolution

$$
A \cdot B = \{ab : a \in A,\ b \in B\}, \qquad A^{*} = \{a^{-1} : a \in A\}.
$$

This is an involutive unital quantale, with unit $\{e\}$, and it is the quantale of the group algebra at the level of subsets. Its fixed points under ${}^{*}$ are the inverse-closed subsets, and they form a frame; the subgroups are among them but do not themselves form a distributive lattice in general, the subgroup lattice of $\mathbb{Z}/2 \times \mathbb{Z}/2$ being the non-distributive lattice $M_3$ of *Effect Algebras and Orthomodular Lattices*.

**Remark.** The quantale of a $\mathbb{C}$-algebra — the lattice of closed left ideals with the product inherited from the algebra — is the standard operator-algebraic example; it is studied in *Operator Algebras* and is not developed here. The construction shows that the quantale axioms apply far beyond the frame case, and it is the reason quantales appear in the algebraic foundations of topology, of logic and of representation theory. No analysis is used in the present article.

## Summary

A frame is a complete lattice in which finite meets distribute over arbitrary joins; equivalently, it is a complete Heyting algebra. The open sets of a topological space form the standard example, the ideals of a commutative ring and the down-sets of a poset form algebraic examples, and every complete Boolean algebra is a frame. Frame homomorphisms preserve finite meets and arbitrary joins; nuclei, the monotone extensive idempotent meet-preserving maps, correspond bijectively to sublocales, and the double-negation nucleus gives the Booleanization of a frame, the complete Boolean algebra of its regular elements.

A locale is a frame read in the opposite category. The open-set functor $\mathcal{O}$ from spaces to locales is left adjoint to the points functor $\operatorname{pt}$, whose points are the frame homomorphisms to the two-element frame; the adjunction restricts to an equivalence between sober spaces and spatial locales. A locale may have no points, and locality is the generalisation of topology in which the frame is primary. Compactness and the separation axioms translate into the frame, and the Zariski locale of a commutative ring is the algebraic prototype.

A quantale is a complete lattice with an associative multiplication distributing over arbitrary joins; the frames are exactly the idempotent commutative unital quantales with the meet as product. The binary relations on a set under composition, the ideals of a commutative ring under ideal product, the power set of a monoid under convolution and the subsets of a group under convolution and inversion are the standard examples, unital, commutative or involutive as the case may be, and they show that the quantale axioms are strictly weaker than the frame axioms. The Boolean system's algebra thus reaches, at this article, the complete distributive case and its non-idempotent generalisation; the Boolean case itself, with its Stone space, is not covered here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L$ | A frame (also read as a locale) |
| $Q$ | A quantale |
| $\bigvee, \bigwedge$ | Arbitrary join and meet in a frame |
| $a \to b$ | Relative pseudocomplement, $\bigvee\{c : c\wedge a \leq b\}$ |
| $\neg a$ | Pseudocomplement, $a \to 0$ |
| $\mathcal{O}(X)$ | Frame of open sets of a topological space |
| $\operatorname{Id}(R)$ | Frame and quantale of ideals of a commutative ring |
| $\operatorname{Dn}(P)$ | Frame of down-sets of a poset |
| $j$ | Nucleus; $L_j$ its frame of fixed points |
| $\mathbf{2}$ | Two-element frame |
| $\operatorname{pt}(L)$ | Points of a locale, the frame homomorphisms $L \to \mathbf{2}$ |
| $\mathbf{Frm}, \mathbf{Loc}$ | Categories of frames and of locales, $\mathbf{Loc} = \mathbf{Frm}^{\mathrm{op}}$ |
| $\cdot$ | Multiplication of a quantale |
| $e$ | Unit of a unital quantale |
| ${}^{*}$ | Involution of an involutive quantale |
| $\mathcal{P}(X\times X)$ | Quantale of relations on $X$ under composition |





## Further Reading

- Peter T. Johnstone, *Stone Spaces* (Cambridge University Press, 1982), for frames, locales, nuclei, spatiality and the adjunction with topological spaces.
- Peter T. Johnstone, *Sketches of an Elephant: A Topos Theory Compendium* (Oxford University Press, 2002), for the place of locales in topos theory and the non-spatial examples.
- Jorge Picado and Aleš Pultr, *Frames and Locales: Topology without Points* (Birkhäuser, 2012), for a systematic modern treatment with the separation and compactness conditions.
- Francis Borceux, *Handbook of Categorical Algebra 3: Categories of Sheaves* (Cambridge University Press, 1994), for quantales, quantale modules and the categorical theory.
- Kimmo I. Rosenthal, *The Theory of Quantaloids* (Pitman, 1996), for quantales, involutive quantales and their modules.
- David Kruml and Jan Paseka, "Algebraic and Categorical Aspects of Quantales", in *Handbook of Algebra* 5 (Elsevier, 2008), for the algebraic theory of quantales and the frame-quantale comparison.
- Michael Artin, *Grothendieck Topologies* (Harvard University Press, 1962), for the Zariski topology and the localic spectrum of a ring.
