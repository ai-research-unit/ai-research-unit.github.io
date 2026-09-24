
# __Proximity Spaces__

## Introduction

A topological space records nearness between a point and a set: a point lies in the closure of a set when every neighbourhood of the point meets the set. A **proximity space** records nearness between two sets, and it is strictly finer information: two sets can be near without intersecting, and the relation of nearness is required to satisfy axioms that make the corresponding closure operator a topology. The structure was described by Riesz in 1909, rediscovered and axiomatised by Efremovič in 1934 and published in 1951, and it sits between the topological and the uniform structures: every uniform space induces a proximity, every proximity induces a topology, and the passage from uniform to topological factors through the proximity. Separated proximities induce completely regular Hausdorff topologies, and conversely every completely regular Hausdorff topology is induced by proximities; the compactifications of the space are classified by the proximities on it.

This article develops the axioms of an Efremovič proximity, the induced closure and topology, the proximal maps, the exact relation to the uniform spaces of *Metric, Uniform and Complete Spaces*, and the classification of compactifications by the totally bounded proximities. The proximity relation is the set-to-set analogue of the point-to-set information of a topology, and the loss from a uniformity to its proximity is exactly the loss of the uniform cover data that the paracompactness and completion theories of the earlier articles use. No measure, integral, derivative or analytic limit is used, and no physics is invoked.

## The Proximity Relation

### The Axioms

**Definition.** A **proximity** on a set $X$ is a relation $\delta$ between subsets of $X$ that satisfies the following axioms for all $A, B, C \subseteq X$:

**(P1)** $A \delta B$ implies $B \delta A$;

**(P2)** $A \delta B$ implies $A \neq \emptyset$ and $B \neq \emptyset$;

**(P3)** $A \cap B \neq \emptyset$ implies $A \delta B$;

**(P4)** $A \delta (B \cup C)$ if and only if $A \delta B$ or $A \delta C$;

**(P5)** if for every $E \subseteq X$ one has $A \delta E$ or $B \delta (X \setminus E)$, then $A \delta B$.

One writes $A \delta B$ and says $A$ is **near** $B$, or that $A$ and $B$ are **proximal**; the negation is written $A \,\bar\delta\, B$ and one says $A$ and $B$ are **apart** or **far**. A **proximity space** is a pair $(X, \delta)$. A proximity is **separated** if $\{x\} \delta \{y\}$ implies $x = y$.

Axioms (P1), (P3) and (P4) say that nearness is a symmetric, additive relation that contains the intersection relation; axiom (P2) excludes the empty set from being near anything; and axiom (P5) is the **Efremovič axiom**, the strong axiom that distinguishes the proximities among the relations satisfying the first four. In the contrapositive form that is used below, (P5) reads
$$
A \,\bar\delta\, B \ \Longrightarrow \ \text{there is } E \subseteq X \text{ with } A \,\bar\delta\, E \text{ and } B \,\bar\delta\, (X \setminus E).
$$

**Definition.** For subsets $A, B \subseteq X$ one writes $A \ll B$, and says that $B$ is a **proximal neighbourhood** of $A$, or that $A$ is **strongly contained** in $B$, when
$$
A \,\bar\delta\, (X \setminus B).
$$

**Proposition.** The strong containment relation satisfies: $X \ll X$ and $\emptyset \ll X$; $A \ll B$ implies $A \subseteq B$; $A \subseteq B \ll C \subseteq D$ implies $A \ll D$; $A \ll B$ and $A \ll C$ imply $A \ll B \cap C$; $A \ll B$ implies $X \setminus B \ll X \setminus A$; and $A \ll B$ implies the existence of $E$ with $A \ll E \ll B$.

**Proof.** The last property is the Efremovič axiom: from $A \ll B$, that is $A \bar\delta (X \setminus B)$, choose $E$ with $A \bar\delta E$ and $(X \setminus B) \bar\delta (X \setminus E)$; then $A \bar\delta E$ gives $A \ll X \setminus E$, and $(X\setminus B)\bar\delta(X\setminus E)$ gives, taking complements and using the symmetry, $X \setminus E \ll B$. The other properties are immediate from (P1)–(P4): for instance $A \ll B$ means $A \bar\delta (X \setminus B)$, so no point of $A$ lies in $X \setminus B$ by (P3), whence $A \subseteq B$; and $A \ll B, A \ll C$ give $A \bar\delta (X\setminus B), A \bar\delta(X \setminus C)$, which by (P4) in the form $A \bar\delta \bigl((X\setminus B) \cup (X\setminus C)\bigr)$ gives $A \ll B \cap C$. $\square$

### The Induced Topology

**Theorem.** Let $(X, \delta)$ be a proximity space and define, for $A \subseteq X$,
$$
\operatorname{cl}_\delta(A) = \{ x \in X : \{x\} \delta A \} .
$$
Then $\operatorname{cl}_\delta$ is a Kuratowski closure operator, so it is the closure operator of a topology on $X$, the **topology induced by the proximity**.

**Proof.** One checks the four axioms. $A \subseteq \operatorname{cl}_\delta(A)$ by (P3). Monotonicity follows from (P4): if $A \subseteq B$ then $B = A \cup B$, so $A \delta E$ implies $B \delta E$. Idempotence uses the Efremovič axiom: if $x \in \operatorname{cl}_\delta(\operatorname{cl}_\delta(A))$ and $x \notin \operatorname{cl}_\delta(A)$, then $\{x\} \bar\delta A$, so there is $E$ with $\{x\} \bar\delta E$ and $A \bar\delta (X \setminus E)$; the second says $\operatorname{cl}_\delta(A) \subseteq E$, so $\{x\} \delta \operatorname{cl}_\delta(A)$ contradicts $\{x\} \bar\delta E$. Additivity $\operatorname{cl}_\delta(A \cup B) = \operatorname{cl}_\delta(A) \cup \operatorname{cl}_\delta(B)$ is (P4). Finally $\operatorname{cl}_\delta(\emptyset) = \emptyset$ by (P2). $\square$

**Proposition.** The topology induced by a proximity is completely regular. It is $T_1$, equivalently Hausdorff, exactly when the proximity is separated, and in that case it is a completely regular Hausdorff, that is a Tychonoff, topology.

**Proof.** Complete regularity is proved by imitating Urysohn's lemma: given a point $x$ and a closed set $F$ with $x \notin F$, one has $\{x\} \bar\delta F$, and the Efremovič axiom produces a sequence of sets between $\{x\}$ and $X \setminus F$ related by strong containment, which yields a continuous function separating them. The singleton $\{x\}$ is closed exactly when $\{y\}\delta\{x\}$ forces $y = x$, which is the separation condition. $\square$

**Example (the discrete proximity).** On any set $X$ let $A \delta B$ if and only if $A \cap B \neq \emptyset$. This is a proximity, the **discrete proximity**; it is the smallest proximity on $X$ in the order of the next section, and its induced topology is the discrete topology. The associated uniform structure is the discrete uniformity, in which every entourage is a neighbourhood condition.

**Example (the metric proximity).** On a metric space $(X,d)$ let
$$
A \delta B \iff d(A,B) = 0, \qquad d(A,B) = \inf \{ d(a,b) : a \in A, b \in B \} .
$$
This is a separated proximity, the **metric proximity**, and it satisfies the Efremovič axiom because the function $d(\cdot, B)$ is continuous and positive away from $B$: if $d(A,B) > 0$ then $E = \{x : d(x,B) < d(A,B)/2\}$ witnesses (P5), since $A$ is far from $E$ and $X \setminus E$ is far from $B$. The induced topology is the metric topology, and the induced closure is the metric closure. The metric proximity is the proximity of the metric uniformity of the next section, and it is the unique compatible proximity when the metric space is compact, but not in general: $\mathbb{R}$ with its usual metric carries the metric proximity as well as the finer Čech–Stone proximity of the third example below.

**Example (the fine proximity).** Let $X$ be a completely regular Hausdorff space and let $\beta X$ be its Stone–Čech compactification. Define
$$
A \delta B \iff \operatorname{cl}_{\beta X}(A) \cap \operatorname{cl}_{\beta X}(B) \neq \emptyset .
$$
This is a separated proximity inducing the given topology on $X$; it is the **Čech–Stone proximity**, and it is the finest proximity inducing that topology. When $X$ is normal the closures in $\beta X$ of two closed subsets of $X$ are disjoint exactly when the subsets are disjoint, so the Čech–Stone proximity is then simply
$$
A \delta B \iff \operatorname{cl}_X(A) \cap \operatorname{cl}_X(B) \neq \emptyset ,
$$
and this relation, closure-intersection, is a proximity exactly for the normal spaces.

### Algebraic Properties of the Nearness Relation

**Proposition.** In a proximity space:

**(i)** $A \delta B$ if and only if $\operatorname{cl}_\delta(A) \delta \operatorname{cl}_\delta(B)$; the proximity is determined by its restriction to closed sets;

**(ii)** for closed sets $A$ and $B$ in a separated proximity, $A \delta B$ does not force $A \cap B \neq \emptyset$: in the metric proximity of the plane the graph of $1/x$ and the $x$-axis are disjoint closed sets at distance zero, hence near, whereas for a normal space with the Čech–Stone proximity two closed sets are near exactly when they meet;

**(iii)** if $A \delta B$ and $A \subseteq A'$, $B \subseteq B'$, then $A' \delta B'$;

**(iv)** if $A \delta B$ then $A \neq \emptyset$ and $B \neq \emptyset$, and $A \delta X$ for every nonempty $A$.

**Proof.** (i) If $x \in \operatorname{cl}_\delta(A)$ then $\{x\}\delta A$, so by additivity $\operatorname{cl}_\delta(A)\delta B$ whenever $A \delta B$; applying this twice gives the forward implication, and the converse is monotonicity. (ii) is the example of a metric space with two closed sets at distance zero but disjoint, such as the graph of $1/x$ and the $x$-axis in the plane. (iii) and (iv) are immediate from (P1)–(P4). $\square$

## Proximal Maps

**Definition.** Let $(X, \delta)$ and $(Y, \varepsilon)$ be proximity spaces. A map $f : X \to Y$ is **proximally continuous**, or a **proximity map**, if
$$
A \delta B \implies f[A] \,\varepsilon\, f[B]
$$
for all $A, B \subseteq X$; equivalently, if $C \ll_\varepsilon D$ implies $f^{-1}[C] \ll_\delta f^{-1}[D]$. A bijective proximity map whose inverse is a proximity map is a **proximity isomorphism**, and the proximity spaces with the proximity maps form a category.

**Proposition.** Every proximally continuous map is continuous for the induced topologies; the composition of proximity maps is a proximity map; and the proximity isomorphisms are exactly the homeomorphisms that preserve the nearness relation.

**Proof.** Continuity is the clause $\{x\}\delta A \Rightarrow \{f(x)\}\varepsilon f[A]$, which says that $f$ maps the closure of $A$ into the closure of $f[A]$, the defining property of continuity in the closure formulation. Composition and the characterisation of isomorphisms are immediate from the definition. $\square$

**Proposition.** A compact Hausdorff space $K$ carries a unique compatible proximity, namely the one for which $A$ and $B$ are near exactly when their closures meet.

**Proof.** A compact Hausdorff space carries exactly one uniformity inducing its topology, a standard theorem of the uniform theory of *Metric, Uniform and Complete Spaces*; since a uniformity determines the proximity it induces, the compatible proximity is unique. For the closure-intersection relation, two closed sets are far precisely when they are disjoint, and this relation satisfies the proximity axioms on a compact Hausdorff space. $\square$

**Remark.** The uniqueness of the proximity on a compact space does not mean that every continuous map into it is proximally continuous. A uniformly continuous map between metric spaces preserves the metric proximity, but a merely continuous one need not: on $\mathbb{R}$ with its usual metric the sets $A = \mathbb{N}$ and $B = \{\, n + 1/(2n) : n \geq 1 \,\}$ are near, since their distance is at most $1/2$ and tends to $0$, while their images under $x \mapsto x^2$ are $\{\, n^2 \,\}$ and $\{\, n^2 + 1 + 1/(4n^2) \,\}$, whose distance is at least $1$; so $x \mapsto x^2$ is continuous and not proximally continuous. The correct general statement is that every continuous map from $X$ into a compact Hausdorff space is proximally continuous when the proximity on $X$ is the Čech–Stone proximity, because such a map extends over $\beta X$; a general proximity on $X$ need not make all its continuous maps proximal.

**Example.** On a metric space the identity map from the Čech–Stone proximity to the metric proximity is proximally continuous, because the Čech–Stone proximity is finer; the identity in the other direction is not proximally continuous unless the two proximities agree, which happens exactly when the metric space is compact. This is the standard example of two distinct proximities inducing the same topology.

## The Relation to Uniform Spaces

### From Uniformity to Proximity

**Definition.** Let $(X, \mathcal{U})$ be a uniform space, with $\mathcal{U}$ the uniformity of entourages. Define
$$
A \delta_{\mathcal{U}} B \iff A \times B \text{ meets every } U \in \mathcal{U} .
$$
An **entourage** is a subset $U \subseteq X \times X$ containing the diagonal and closed under the formation of the inverse and of an iterate, in the sense of *Metric, Uniform and Complete Spaces*.

**Theorem.** The relation $\delta_{\mathcal{U}}$ of the definition is a proximity on $X$, the **proximity induced by the uniformity**; its induced topology is the topology of the uniform space, and every uniformly continuous map between uniform spaces is proximally continuous for the induced proximities.

**Proof.** Symmetry is the symmetry of the entourages; the empty set fails to meet an entourage, giving (P2); $\delta_{\mathcal{U}}$ contains the intersection relation because an entourage contains the diagonal, giving (P3); the additivity (P4) is the distributivity of the product over the union in the second variable. For the Efremovič axiom, suppose $A \times B$ fails to meet the entourage $U$; choose a symmetric entourage $V$ with $V \circ V \subseteq U$ and put $E = V[B] = \{x : (b,x) \in V \text{ for some } b \in B\}$. Then $A \times E$ misses $V$, because $(a,e) \in V$ with $e \in V[B]$ produces $b \in B$ with $(e,b) \in V$ and hence $(a,b) \in V \circ V \subseteq U$, and $(X \setminus E) \times B$ misses $V$ by the definition of $E$. Hence $A \bar\delta E$ and $(X \setminus E) \bar\delta B$, as required. The statement about the topology is the definition of the uniform topology, and the statement about maps is the definition of uniform continuity. $\square$

**Theorem.** Every proximity is induced by a uniformity, namely by the finest uniformity inducing it, and the metric proximities are exactly those induced by the uniformities of metric spaces. The equivalence classes of uniformities under the relation of inducing the same proximity are in bijection with the proximities, so the passage from uniformity to proximity is a quotient of the uniform structure by the covering data it forgets.

**Proof sketch.** Given a proximity $\delta$, the family of all covers of $X$ whose members are proximal neighbourhoods of the form $\{x : \{x\} \ll U\}$ generates a uniformity whose induced proximity is the original one; the assertion is the standard construction of the **proximal uniformity** of a proximity space, and the details use the strong containment of the preceding sections. The statements about metrics are the observation that the metric proximity of a metric space is the proximity of its metric uniformity. $\square$

### Totally Bounded Proximities and Compactifications

**Definition.** A proximity is **totally bounded** if it is induced by a totally bounded uniformity, equivalently if the finest uniformity inducing it is totally bounded.

**Theorem (Smirnov).** Let $X$ be a completely regular Hausdorff space. There is a bijective correspondence, up to equivalence, between the compactifications of $X$ and the totally bounded proximities on $X$: to a compactification $\gamma X$ one assigns the proximity
$$
A \delta_\gamma B \iff \operatorname{cl}_{\gamma X}(A) \cap \operatorname{cl}_{\gamma X}(B) \neq \emptyset ,
$$
and to a totally bounded proximity one assigns its completion, which is compact. Under this correspondence, finer proximities correspond to larger compactifications, the Čech–Stone proximity corresponds to $\beta X$, and the one-point compactification of a locally compact space corresponds to the coarsest totally bounded proximity.

The proof is due to Smirnov and is the proximity-theoretic form of the classification of the compactifications of a completely regular space; the completion of the totally bounded uniform space is compact by the theorem on total boundedness and completeness in *Metric, Uniform and Complete Spaces*, and the nearness relation extends to the completion.

**Corollary.** A space admits a compatible proximity if and only if it is completely regular and Hausdorff; on a compact Hausdorff space the compatible proximity is unique; and on a wide class of noncompact spaces, among them the Euclidean spaces, there are many compatible proximities, one for each of the compactifications classified by the theorem.

**Proof.** A proximity induces a completely regular topology, and conversely every completely regular Hausdorff space carries at least the Čech–Stone proximity, so a topology is proximisable exactly when it is completely regular and Hausdorff. A compact Hausdorff space carries exactly one compatible uniformity, a standard theorem of the uniform theory of *Metric, Uniform and Complete Spaces*, and every compatible proximity is induced by a compatible uniformity; since a uniformity determines the proximity it induces, the compatible proximity on a compact Hausdorff space is unique. The Euclidean spaces are locally compact and noncompact, so they carry the Čech–Stone proximity, the one-point-compactification proximity and the intermediate ones, one for each compactification. $\square$

## The Relation to Topological Spaces

### Proximisable Topologies

**Theorem.** A topological space admits a proximity inducing its topology if and only if it is completely regular and Hausdorff; and a completely regular Hausdorff space admits a finest compatible proximity, the Čech–Stone proximity, and for a normal space this proximity is the closure-intersection relation.

**Proof.** The necessity is complete regularity of proximity topologies; the sufficiency is the Čech–Stone proximity. The finest property is the statement that the proximity assigned to a compactification in Smirnov's correspondence is finer for larger compactifications and that $\beta X$ is the largest compactification; and for normal $X$ the closures in $\beta X$ of disjoint closed sets of $X$ are disjoint, which identifies the fine proximity with closure-intersection. $\square$

**Theorem.** Under the order $\delta_1 \leq \delta_2$ defined by $A \delta_1 B \Rightarrow A \delta_2 B$, the family of proximities inducing a fixed completely regular topology is a complete lattice, and its finest element is the Čech–Stone proximity.

**Proof.** The pointwise infimum and supremum of a family of proximities is again a proximity, and the compatible ones are closed under these operations, which gives the complete lattice; the finest element exists by the preceding theorem. $\square$

### Proximity and the Earlier Structures

**Remark.** The proximity sits above the topology constructed here and below the uniformity of *Metric, Uniform and Complete Spaces*, and the two arrows are the ones that make the earlier and later structures comparable. The covering-theoretic description of the uniform structure, as in *Paracompactness and Partitions of Unity*, is finer than the proximity: a proximity remembers only which pairs of sets are near, while a uniformity remembers which covers are uniform, and many uniformities induce the same proximity. The quotient of the uniform structures on a set by the relation of inducing the same proximity is the set of proximities, and the quotient of the proximities by the induced topology is the set of completely regular topologies, so the theory is the middle term of the chain
$$
\text{topology} \;\longleftarrow\; \text{proximity} \;\longleftarrow\; \text{uniformity} .
$$

**Remark.** The completely regular topology of a proximity is the initial topology for the family of proximally continuous maps into the compact Hausdorff spaces, but the proximity is *not* recovered from the continuous maps alone: the identity of a completely regular space into its Stone–Čech compactification is proximally continuous precisely for the Čech–Stone proximity, and a coarser proximity on the same space admits fewer proximal maps. The proximity records the compactification data, and the compactification data determine which continuous maps into compact spaces are proximal.

## Summary

A **proximity** on a set $X$ is a relation $\delta$ of nearness between subsets, symmetric, additive in the second variable, containing the intersection relation, and satisfying the **Efremovič axiom**: if $A$ and $B$ are far, then a set $E$ separates them, with $A$ far from $E$ and $B$ far from $X \setminus E$. The **strong containment** $A \ll B$ means that $A$ is far from $X \setminus B$, and it satisfies the properties of a set neighbourhood relation. The relation $\operatorname{cl}_\delta(A) = \{x : \{x\}\delta A\}$ is a Kuratowski closure operator, so a proximity induces a topology; the induced topology is completely regular, and it is Hausdorff exactly when the proximity is **separated**. A proximity map preserves nearness; the proximity maps are continuous for the induced topologies, and a compact Hausdorff space carries a unique compatible proximity, namely the closure-intersection relation.

Every uniform space **induces a proximity**, by declaring two sets near when their product meets every entourage; the induced proximity determines the uniform topology, uniformly continuous maps are proximity maps, and every proximity arises from a uniformity, so the passage from uniformity to proximity is a surjection whose fibres are the uniformities inducing the same nearness. A proximity is **totally bounded** when its proximal uniformity has finite uniform covers, and by **Smirnov's theorem** the compactifications of a completely regular Hausdorff space correspond bijectively to its totally bounded proximities, the finer proximities giving the larger compactifications and the **Čech–Stone proximity** giving the Stone–Čech compactification. A topology is proximisable exactly when it is completely regular and Hausdorff; the compatible proximities form a complete lattice, whose finest element is the Čech–Stone proximity; for a normal space this finest proximity is the **closure-intersection** relation, and on a compact Hausdorff space the proximity is unique. The proximity is thus the middle term between the topology and the uniformity of *Metric, Uniform and Complete Spaces*, coarser than the uniform structure by exactly the covering data of *Paracompactness and Partitions of Unity* that it forgets.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(X, \delta)$ | Proximity space |
| $A \delta B$ | $A$ is near $B$ (proximal) |
| $A \,\bar\delta\, B$ | $A$ and $B$ are apart (far) |
| $A \ll B$ | Strong containment; $A \,\bar\delta\, (X \setminus B)$ |
| separated proximity | $\{x\}\delta\{y\} \Rightarrow x=y$; induced topology Hausdorff |
| $\operatorname{cl}_\delta(A)$ | $\{x : \{x\}\delta A\}$, the induced closure |
| discrete proximity | $A \delta B \iff A \cap B \neq \emptyset$ |
| metric proximity | $A \delta B \iff d(A,B)=0$ |
| Čech–Stone proximity | $A\delta B \iff \operatorname{cl}_{\beta X}A \cap \operatorname{cl}_{\beta X}B \neq \emptyset$ |
| closure-intersection proximity | $\operatorname{cl}_X A \cap \operatorname{cl}_X B \neq \emptyset$; a proximity exactly for normal $X$ |
| totally bounded proximity | Its proximal uniformity has finite uniform covers |
| $\delta_{\mathcal{U}}$ | Proximity induced by the uniformity $\mathcal{U}$ |
| $\beta X$, $\gamma X$ | Stone–Čech and a general compactification of $X$ |
| $\delta_\gamma$ | Totally bounded proximity of the compactification $\gamma X$ |

## Further Reading

- Somashekhar A. Naimpally and Brian D. Warrack, *Proximity Spaces* (Cambridge Tracts in Mathematics and Mathematical Physics 59, Cambridge University Press, 1970), for the systematic theory of proximities and their topology.
- Ryszard Engelking, *General Topology* (Heldermann, revised ed. 1989), for proximities, the fine proximity and the relation to uniformities and compactifications.
- V. A. Efremovič, "Infinitesimal Spaces" (Russian), *Doklady Akademii Nauk SSSR* 76 (1951), 341–343, for the original axioms.
- F. Riesz, "Stetigkeit und abstrakte Mengenlehre", *Rapports du 4e Congrès des Mathématiciens* (Rome, 1909), 18–24, for the first description of the nearness relation.
- A. D. Wallace, "Separation Spaces", *Annals of Mathematics* 42 (1941), 687–697, for the equivalent formulation as a separation space.
- Yu. M. Smirnov, "On Proximity Spaces", *Matematicheskii Sbornik* 31 (1952), 543–574, for the classification of compactifications by totally bounded proximities.
- John R. Isbell, *Uniform Spaces* (Mathematical Surveys and Monographs 12, American Mathematical Society, 1964), for the uniform-space background and the fine uniformity.
