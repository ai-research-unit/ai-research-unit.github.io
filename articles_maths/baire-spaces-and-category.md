
# __Baire Spaces and Category__

## Introduction

A subset of a topological space is **nowhere dense** if its closure has empty interior, and **meagre**, or of the **first category**, if it is a countable union of nowhere dense sets. Complements of meagre sets are **comeagre**, or **residual**, and the meagre sets behave as the topologically negligible sets of a space: they are closed under countable unions and under passage to subsets, and the complement of a meagre set is dense when the space is not itself meagre. A space in which no nonempty open set is meagre is a **Baire space**. The Baire category theorem, proved in *Metric, Uniform and Complete Spaces* for complete metric spaces and for locally compact Hausdorff spaces, is the reason the notion is useful: in such a space a countable intersection of dense open sets is dense, so a countable family of dense conditions is simultaneously satisfiable, and a countable family of nowhere dense obstructions cannot exhaust an open set.

This article develops the calculus of meagre sets, characterises Baire spaces in several equivalent ways, describes the spaces that are Baire without being complete, and gives the game-theoretic characterisation of Oxtoby: a space is Baire exactly when the first player has no winning strategy in the Banach–Mazur game of nested open sets. The completeness theory is that of *Metric, Uniform and Complete Spaces*, where the Baire category theorem is proved and where the completion is constructed; the Čech-complete spaces used here are the topological form of complete metrisability introduced in *Metrisation and Separation Axioms*. The applications of the Baire theorem to functional analysis — the open mapping, closed graph and uniform boundedness theorems — belong to Part III, where the norms and the limits they need are available, and they are deferred there. No measure, integral or analytic limit is used, and no physics is invoked.

## Meagre Sets and the Calculus of Category

### Nowhere Dense and Meagre Sets

**Definition.** Let $X$ be a topological space and $A \subseteq X$. Then $A$ is **nowhere dense** in $X$ if the interior of its closure is empty:
$$
\bigl(\overline{A}\bigr)^\circ = \emptyset .
$$
A set is **meagre**, or of the **first category**, if it is a countable union of nowhere dense sets; it is **of the second category** if it is not meagre; and it is **comeagre**, or **residual**, if its complement is meagre. A **Baire space** is a space in which the intersection of every countable family of dense open sets is dense.

The definition of a Baire space is given in this form, and equivalently in the three forms of the next section. Note that the property concerns only the topology: it is a statement about open dense families, and the metric enters only through the theorem that produces such families in complete spaces.

**Example.** In $\mathbb{R}$ a single point is nowhere dense, a countable set is meagre, and the rationals $\mathbb{Q}$ are meagre but dense. No interval is meagre in $\mathbb{R}$, because $\mathbb{R}$ is complete; the same computation in $\mathbb{Q}$ fails, and $\mathbb{Q}$ is meagre in itself, being a countable union of singletons. Thus meagreness is not absolute but depends on the ambient space, and this dependence is the reason the Baire property is stated for the space and not for the set.

**Example.** In a space with the discrete topology no nonempty set is nowhere dense unless it is empty, since the closure of a set is itself; the only meagre set is the empty set, and the space is Baire. The trivial topology on a set with more than one point is also Baire, since the only dense open set is the whole space.

### The Calculus of Category

**Proposition.** Let $X$ be a topological space. Then

**(i)** a subset of a nowhere dense set is nowhere dense, and the closure of a nowhere dense set is nowhere dense;

**(ii)** a finite union of nowhere dense sets is nowhere dense;

**(iii)** a countable union of meagre sets is meagre, and a subset of a meagre set is meagre;

**(iv)** the meagre sets form a σ-ideal in the boolean algebra of subsets of $X$;

**(v)** if $A$ is nowhere dense, then $X \setminus A$ contains a dense open set.

**Proof.** (i) If $A \subseteq B$ and $B$ is nowhere dense then $\overline{A} \subseteq \overline{B}$, so $(\overline{A})^\circ \subseteq (\overline{B})^\circ = \emptyset$. The closure has the same closure as the set. (ii) From (i) it suffices to treat closed nowhere dense sets, and if $F, G$ are closed with empty interior, then $F \cup G$ has empty interior because a nonempty open set inside $F \cup G$ meets $F$ or $G$ in a nonempty open set: if $U$ is open and nonempty and $U \subseteq F \cup G$, then $U \setminus F$ is open and either empty, in which case $U \subseteq F$, or nonempty and contained in $G$. (iii) is immediate from the definition and (i). (iv) restates (iii) together with the fact that the family is nonempty (it contains $\emptyset$). (v) $X \setminus \overline{A}$ is open and dense, since its complement $\overline A$ has empty interior. $\square$

**Proposition.** The following are equivalent for a space $X$:

**(a)** $X$ is a Baire space;

**(b)** every countable union of nowhere dense closed sets has empty interior, and every countable union of nowhere dense sets has empty interior;

**(c)** every nonempty open subset of $X$ is of the second category in $X$;

**(d)** every comeagre subset of $X$ is dense;

**(e)** the complement of every meagre set is dense.

**Proof.** (a) $\Leftrightarrow$ (b): a set is dense open exactly when its complement is closed nowhere dense, and the intersection of the dense open sets $D_n$ has complement $\bigcup_n (X \setminus D_n)$, a countable union of nowhere dense closed sets; the intersection is dense iff this union has empty interior. (b) $\Leftrightarrow$ (c): an open set $U$ is meagre in $X$ iff it is a countable union of nowhere dense sets, and since $U$ is open, this union has empty interior iff its intersection with $U$ has empty interior; the equivalence is the statement that no nonempty open set is meagre. (c) $\Leftrightarrow$ (d) $\Leftrightarrow$ (e) restate that the complement of a comeagre set is meagre and that a set is dense iff it meets every nonempty open set. $\square$

### The Baire Property

**Definition.** A subset $A \subseteq X$ has the **Baire property**, and is called **almost open**, if there is an open set $U$ and a meagre set $M$ with
$$
A = U \,\triangle\, M = (U \setminus M) \cup (M \setminus U).
$$

**Theorem.** The sets with the Baire property form a σ-algebra containing every open set and every meagre set; every Borel set has the Baire property; and a set $A$ has the Baire property if and only if it is the union of an open set and a meagre set, if and only if it differs from a closed set by a meagre set.

**Proof sketch.** Open sets have the property with $M = \emptyset$, and meagre sets with $U = \emptyset$. For complements, if $A = U \triangle M$ then $X \setminus A = (X \setminus \overline{U}) \triangle M'$ with $M'$ meagre, using that $\overline{U} \setminus U$ is nowhere dense when $U$ is open. For countable unions, the family of symmetric differences is closed under the operation because a countable union of meagre sets is meagre, and the resulting σ-algebra contains the open sets; the Borel σ-algebra is the smallest such, so it is contained. The last characterisation follows from $\overline{U} \setminus U$ nowhere dense. $\square$

**Remark.** The Baire property is the topological counterpart of the notion of an almost-everywhere-defined object; the sets with the property are exactly those that can be corrected to an open set by a meagre set. The existence of sets without the Baire property requires the axiom of choice, and the standard construction is a transfinite recursion over the countable well-orderable conditions, which is out of the scope of this article. The property is used in descriptive set theory, where the Borel and analytic hierarchies are studied, and in the theory of the Banach–Mazur game of the fourth section.

**Theorem (Banach category theorem).** Let $\{U_s\}_{s \in S}$ be a family of pairwise disjoint open subsets of $X$, each meagre in $X$. Then $\bigcup_s U_s$ is meagre in $X$.

**Proof.** Write each $U_s = \bigcup_n F_{s,n}$ with $F_{s,n}$ closed nowhere dense in $X$ and $F_{s,n} \subseteq U_s$; the second property can be arranged because $U_s$ is open and the intersection of a nowhere dense set with an open set is nowhere dense in $X$. Then
$$
\bigcup_s U_s = \bigcup_n \Bigl(\bigcup_s F_{s,n}\Bigr),
$$
and it suffices to show that $G_n = \bigcup_s F_{s,n}$ is nowhere dense for each $n$. Suppose not, and let $W$ be a nonempty open set with $W \subseteq \overline{G_n}$. Choose a nonempty open $W_1 \subseteq W$ meeting $G_n$, and then $s$ with $W_1 \cap U_s \neq \emptyset$ and such that $W_1 \cap U_s$ meets $F_{s,n}$; this is possible because $W_1$ meets $G_n$ and $F_{t,n} \subseteq U_t$ with the $U_t$ pairwise disjoint, so a point of $W_1 \cap G_n$ lies in exactly one $U_s$ and in $F_{s,n}$. Put $W_2 = W_1 \cap U_s$, nonempty and open. Since $W_2 \subseteq W \subseteq \overline{G_n}$ and $F_{t,n} \cap U_s = \emptyset$ for $t \neq s$, every open subset of $W_2$ meets $F_{s,n}$, so $W_2 \subseteq \overline{F_{s,n}}$. But then $W_2$ is a nonempty open subset of $\overline{F_{s,n}}$, contradicting that $F_{s,n}$ is nowhere dense. Hence $G_n$ is nowhere dense and the union over $n$ is meagre. $\square$

**Remark.** The disjointness of the open sets is exactly what replaces the countable index set that the definition of meagreness supplies: without it the union of uncountably many nowhere dense sets can have interior, as the singletons of $\mathbb{R}$ show. The theorem is the reason a space that is a union of disjoint open meagre sets is meagre, and its classical consequence is that a space in which every open subspace is meagre in itself is meagre.

## Baire Spaces

### The Baire Category Theorem

**Theorem (Baire category theorem).** Every complete metric space is a Baire space, and every locally compact Hausdorff space is a Baire space.

The proof for complete metric spaces is the nested-ball argument, and the proof for locally compact Hausdorff spaces is the nested-compact-neighbourhood argument; both are given in *Metric, Uniform and Complete Spaces*, where the theorem is proved and where its use in the construction of the completion is recorded. The present article takes the theorem as its starting point and develops the surrounding theory.

**Corollary.** A complete metric space is not meagre in itself; a countable complete metric space has an isolated point; and a countable locally compact Hausdorff space has an isolated point. The last two are the standard applications of the theorem to countability, and the first is the statement that the space is of the second category in itself.

**Proof.** If a complete metric space $X$ were meagre in itself, then $X$ would be a countable union of nowhere dense closed sets, contradicting the theorem in the form (b) applied to the nonempty open set $X$. For the second statement, a countable complete metric space is its own countable union of singletons, and the theorem forces one singleton to have nonempty interior, so it is an isolated point. The locally compact case is the same with the local form of the theorem. $\square$

### Čech-Complete Spaces and Completeness

The Baire property holds for a class of spaces strictly larger than the complete metric ones, and *Metrisation and Separation Axioms* introduced the topological form of complete metrisability.

**Definition.** A topological space $X$ is **Čech-complete** if it is a $G_\delta$ subset of some compactification; a metrisable Čech-complete space is exactly a completely metrisable space, that is, a space that admits a complete metric.

**Theorem.** Every Čech-complete space is a Baire space; more generally, a space containing a dense Čech-complete subspace is a Baire space.

**Proof sketch.** A Čech-complete space is a $G_\delta$, say $X = \bigcap_n G_n$, in a compact Hausdorff space $\beta X$, with each $G_n$ open and dense in the closure of $X$. Given dense open sets $D_n \subseteq X$, extend each to a dense open set of the ambient compact space and intersect with the $G_n$; the intersection is a countable intersection of dense open sets in the compact Hausdorff space, which is Baire, hence dense there and therefore dense in $X$. The argument for a dense Čech-complete subspace is the same with the subspace playing the role of the extension. $\square$

**Corollary.** The irrational numbers are a Baire space, being a $G_\delta$ in the complete space $\mathbb{R}$; the rational numbers are not a Baire space, being meagre in themselves. A Baire space need not be Čech-complete: the Sorgenfrey line is a Baire space, it is neither locally compact nor completely metrisable, and it is a Moore space that is not metrisable, so it is not Čech-complete either. Thus the class of Baire spaces properly contains the Čech-complete spaces and is properly contained in the class of spaces that are nonmeagre in themselves.

**Example (the irrationals).** The set $\mathbb{R} \setminus \mathbb{Q}$ is the intersection over $q \in \mathbb{Q}$ of the open dense sets $\mathbb{R} \setminus \{q\}$, a countable intersection; hence it is a $G_\delta$ in the complete space $\mathbb{R}$ and is completely metrisable, with a complete metric obtained by transporting the metric of $\mathbb{R}$ through the homeomorphism with a closed subspace of a countable product. It is a Baire space in which the rationals, which are dense, form a meagre set, so it exhibits a dense meagre subset of a Baire space.

**Example (a Baire space that is not metrisable).** The space $\{0,1\}^{I}$ for uncountable $I$ is compact Hausdorff and therefore Baire; it is not first countable and hence carries no metric. It is the standard witness that the Baire property does not imply metrisability, and it is the ambient space of the inverse limits, written.

### Permanence and the Local Nature of Baireness

**Theorem.** The Baire property is local: $X$ is a Baire space if and only if every point of $X$ has an open neighbourhood that is a Baire space (with the subspace topology), and if and only if $X$ is covered by open Baire subspaces.

**Proof.** If $X$ is Baire and $U \subseteq X$ is open, then $U$ is Baire: given dense open sets $D_n \subseteq U$, the sets $D_n \cup (X \setminus \overline{U})$ are dense open in $X$, their intersection is dense in $X$, and within $U$ it is contained in $\bigcap_n D_n$, which is therefore dense in $U$. Conversely, if $X = \bigcup_s U_s$ with each $U_s$ open and Baire, let $D_n$ be dense open in $X$; then $D_n \cap U_s$ is dense open in $U_s$, so $\bigcap_n D_n \cap U_s$ is dense in $U_s$ by the Baire property of $U_s$, and hence $\bigcap_n D_n$ is dense in each $U_s$ and therefore in $X$. $\square$

**Theorem.** Every open subspace of a Baire space is a Baire space; every comeagre subset of a Baire space is a Baire space; every dense $G_\delta$ subset of a Baire space is a Baire space; every topological sum of Baire spaces is a Baire space; and a space containing a dense Baire subspace is a Baire space.

**Proof.** The open case was proved above. If $C$ is comeagre in the Baire space $X$, then $C$ contains a dense $G_\delta$ set $G = \bigcap_n G_n$ with each $G_n$ open dense in $X$; the sets $G_n \cap C$ are dense open in $C$ and their intersection is $G$, so it suffices to prove the $G_\delta$ case. If $G = \bigcap_n G_n$ is dense in the Baire space $X$ with $G_n$ open dense, and $D_n$ are dense open in $G$, extend each $D_n$ to a dense open set of $X$ by adding the complement of $\overline{G}$; the countable intersection is dense in $X$ and its trace on $G$ lies in $\bigcap_n D_n$, which is therefore dense in $G$. The statement for sums is immediate from the definition, since a dense open set of a sum restricts to a dense open set of each summand. For the last statement, let $Y$ be dense in $X$ and Baire, and let $D_n$ be dense open in $X$; then $D_n \cap Y$ is dense open in $Y$, so their intersection is dense in $Y$ and hence dense in $X$. $\square$

**Remark.** A closed subspace of a Baire space need not be Baire, and this is the sharpest limitation of the permanence theory. The space $X = (\mathbb{R} \times (0,\infty)) \cup (\mathbb{Q} \times \{0\})$ is Baire, because the open upper half-plane is dense in it and is completely metrisable; but the closed subspace $\mathbb{Q} \times \{0\}$ is homeomorphic to $\mathbb{Q}$ and is meagre in itself. So the Baire property is inherited by open subspaces, by comeagre subspaces and by dense $(G_\delta)$ subspaces, but not by closed ones.

**Theorem.** The product of countably many complete metric spaces is a complete metric space, hence a Baire space; more generally, an arbitrary product of complete metric spaces is a Baire space. The product of two Baire spaces need not be Baire.

**Proof sketch.** The countable product carries the complete metric $d(x,y) = \sum_n 2^{-n} \min(1, d_n(x_n, y_n))$, and the category theorem applies. The arbitrary product statement is proved by a direct argument on the product uniformity, reducing to the finite-intersection behaviour of the basic open sets; it is recorded as an exercise in Bourbaki's *General Topology*. The failure of productivity is the theorem of Oxtoby and of Fleissner and Kunen: there are Baire spaces $X$ and $Y$ for which $X \times Y$ is meagre in itself. The counterexamples use the axiom of choice and are not constructed here. $\square$

**Remark.** The failure of productivity is the sharpest difference between the Baire property and compactness: the arbitrary product of compact spaces is compact, while the product of as few as two Baire spaces can fail to be Baire. Products of compact Hausdorff spaces are compact, and products of complete metric spaces are Baire in every cardinality, so the failure occurs among the Baire spaces that are neither, and it is a matter of the structure of the factors rather than of their number.

## The Banach–Mazur Game

### The Game

The game-theoretic characterisation of the Baire property turns a statement about countable families of dense open sets into a statement about two players alternately choosing nested open sets.

**Definition.** Let $X$ be a nonempty topological space. The **Banach–Mazur game** $BM(X)$ is played as follows. Two players, I and II, alternately choose nonempty open subsets
$$
U_1 \supseteq U_2 \supseteq U_3 \supseteq \cdots,
$$
with player I choosing $U_1, U_3, U_5, \ldots$ and player II choosing $U_2, U_4, \ldots$, each move being a nonempty open subset of the previous move. Player II wins the play if
$$
\bigcap_{n \geq 1} U_n \neq \emptyset,
$$
and player I wins otherwise. A **strategy** for a player is a function that assigns a legal move to every finite sequence of previous moves; it is **winning** if it produces a win against every play of the opponent.

**Theorem (Oxtoby).** A nonempty topological space $X$ is a Baire space if and only if player I has no winning strategy in the Banach–Mazur game $BM(X)$.

**Proof sketch (one direction).** If $X$ is not Baire, there is a countable family of closed nowhere dense sets $F_n$ whose union has nonempty interior $W$. Player I chooses $U_1 = W$ and, at his $n$-th move, chooses $U_{2n+1}$ a nonempty open subset of $U_{2n} \setminus F_n$; this is possible because $F_n$ is nowhere dense and $U_{2n}$ is nonempty open. The intersection of the play lies in $W \setminus \bigcup_n F_n = \emptyset$, so player I wins. Hence Baireness excludes a winning strategy for I. The converse, that a Baire space admits no winning strategy for the first player, is Oxtoby's theorem; the proof analyses a putative winning strategy and extracts from it a countable family of closed nowhere dense sets covering an open set, violating the Baire property. $\square$

**Theorem (the general Banach–Mazur game).** Let $Y$ be a topological space, $X \subseteq Y$, and $\mathcal{W}$ a family of subsets of $Y$ each with nonempty interior and meeting every nonempty open subset of $Y$. In the game $MB(X, Y, \mathcal{W})$, in which the players alternately choose members of $\mathcal{W}$ forming a descending sequence and player I wins if
$$
X \cap \Bigl(\bigcap_{n} W_n\Bigr) \neq \emptyset,
$$
player II has a winning strategy if and only if $X$ is meagre in $Y$; and if $Y$ is a complete metric space, player I has a winning strategy if and only if $X$ is comeagre in some nonempty open subset of $Y$.

**Proof sketch.** If $X = \bigcup_n N_n$ with each $N_n$ nowhere dense, player II answers the $n$-th move of I by choosing a member of $\mathcal{W}$ inside the previous move and disjoint from $\overline{N_n}$, which is possible because $\overline{N_n}$ is nowhere dense and the previous move is a nonempty open set. The intersection of the play then avoids each $N_n$ and hence avoids $X$, so II wins. Conversely a winning strategy for II assigns to each move of I a set avoiding $X$ on a dense open piece, which expresses $X$ as a countable union of nowhere dense sets. The statement about complete metric $Y$ is the dual and uses the Baire category theorem. $\square$

**Corollary.** A nonempty Baire space is not meagre in itself, but a nonmeagre space need not be Baire: the space $X = [0,1] \cup ([2,3] \cap \mathbb{Q})$ is nonmeagre, since it contains the interval $[0,1]$, and it is not Baire, since $[2,3] \cap \mathbb{Q}$ is a nonempty open meagre subset. A weakly $\alpha$-favourable space — one in which player II has a winning strategy in $BM(X)$ — is a Baire space. The converse fails: a Baire space need not be weakly $\alpha$-favourable. The general game is determined when the target set has the Baire property, and there are sets lacking it for which the game is not determined, assuming the axiom of choice.

**Remark.** The corollary is the reason the game is a useful refinement of the category notion: it distinguishes Baire spaces by the strength of the second player's position. The Choquet game and the strong Choquet game refine the construction further, and the spaces in which the second player has a winning strategy in the strong Choquet game are exactly the Choquet-complete spaces, a class sitting between the Čech-complete spaces and the Baire spaces; the descriptive set theory of these games belongs to Part III, where the Polish spaces and their Borel and analytic sets are developed.

## Category in Concrete Spaces

### The Rationals and the Irrationals

**Example.** The space $\mathbb{Q}$ of rationals with the usual topology is meagre in itself: it is the countable union of the singletons, each nowhere dense because $\mathbb{Q}$ has no isolated points. Hence $\mathbb{Q}$ is not a Baire space, and a countable intersection of dense open subsets of $\mathbb{Q}$ can be empty. The space $\mathbb{R} \setminus \mathbb{Q}$ of irrationals is a Baire space: it is a $G_\delta$ in the complete space $\mathbb{R}$, hence completely metrisable and therefore Baire. The rationals are the unique countable metrisable space without isolated points, and the irrationals are the unique completely metrisable separable space that is zero-dimensional, nowhere locally compact and has no isolated points; both uniqueness statements belong to the descriptive theory of the Polish spaces, which is developed in Part III.

### The Baire Space of Sequences

**Definition.** The **Baire space** of sequences is the set $\mathbb{N}^{\mathbb{N}}$ of all sequences of naturals with the product topology, where $\mathbb{N}$ is discrete.

**Theorem.** The space $\mathbb{N}^{\mathbb{N}}$ is completely metrisable, zero-dimensional, and a Baire space; every Polish space is a continuous image of it.

**Proof sketch.** The metric $d(x,y) = 2^{-n}$ for the least $n$ with $x_n \neq y_n$, and $d(x,x) = 0$, is complete and induces the product topology: a basic open set fixes finitely many coordinates, and a Cauchy sequence stabilises coordinatewise. The basic open sets are also closed, because two distinct coordinate values are separated, so the space is zero-dimensional. Baireness is the category theorem for the complete metric. The statement about continuous images is the standard representation of a separable completely metrisable space as a quotient of $\mathbb{N}^{\mathbb{N}}$, and is proved by choosing a complete metric and encoding a point as a sequence of nested basic open sets; it is a theorem of descriptive set theory and is cited rather than proved here. $\square$

**Remark (a collision of names).** The phrase *Baire space* denotes two different objects in the literature: the class of spaces defined in this article, in which no nonempty open set is meagre, and the particular completely metrisable space $\mathbb{N}^{\mathbb{N}}$. The corpus uses **Baire space** for the class and **the Baire space of sequences** for $\mathbb{N}^{\mathbb{N}}$, and writes $\mathbb{N}^{\mathbb{N}}$ or $\mathcal{N}$ when the particular space is meant. The notation $\mathcal{N}$ is the standard one in descriptive set theory.

### Meagre Sets and the Size of a Space

**Theorem.** A nonempty Baire space is not meagre in itself; a comeagre subset of a Baire space is dense and is itself a Baire space; a countable intersection of comeagre sets is comeagre and dense; and a countable complete metric space has an isolated point, so a countable space that is dense in itself is not completely metrisable.

**Proof.** The first statement is form (c) of the characterisation applied to the open set $X$. The second and third are the permanence theorem above. For the last, a countable complete metric space is the countable union of its singletons, and the category theorem forces one singleton to have nonempty interior, so that point is isolated; a countable space with no isolated points, such as $\mathbb{Q}$, therefore admits no complete metric. $\square$

**Theorem.** Let $X$ be a Baire space and let $(F_n)$ be a countable family of closed subsets with $X = \bigcup_n F_n$. Then some $F_n$ has nonempty interior. In particular, a Baire space that is a countable union of closed nowhere dense sets is empty.

**Proof.** If every $F_n$ had empty interior, the union would be a countable union of nowhere dense closed sets with nonempty interior $X$, contradicting form (b) of the characterisation of Baire spaces. $\square$

### The Relation to Part III

The Baire category theorem is used in analysis to prove the theorems that guarantee that a continuous linear map which is almost everywhere defined is everywhere defined and bounded. These are the open mapping theorem, the closed graph theorem and the uniform boundedness principle, and their statements require the normed and Banach spaces of the linear-spaces slot of this Part together with the limits of Part III; they belong to Part III, and the present article stops at the category statement. What is recorded here is the topological input: a complete normed space is a Baire space, and a countable intersection of dense open conditions in it is dense. The same input is used in the theory of the irrationals, in the existence of the completion, and in the proof that a quotient of a complete normed space by a closed subspace is complete when the map is open, all of which belong to the categories that own the norms.

## Summary

A set is **nowhere dense** when its closure has empty interior, and **meagre** when it is a countable union of nowhere dense sets; the meagre sets form a σ-ideal, their complements are the **comeagre** sets, and a set is **almost open**, or has the **Baire property**, when it differs from an open set by a meagre set. A **Baire space** is one in which the intersection of countably many dense open sets is dense, equivalently one in which no nonempty open set is meagre, equivalently one in which every comeagre set is dense. The **Baire category theorem** states that complete metric spaces and locally compact Hausdorff spaces are Baire, and the same holds for **Čech-complete** spaces and for spaces with a dense Čech-complete subspace.

Baireness is local: a space is Baire exactly when it is covered by open Baire subspaces; open subspaces, comeagre subspaces, dense $G_\delta$ subspaces and topological sums of Baire spaces are Baire; a space containing a dense Baire subspace is Baire; and a closed subspace of a Baire space need not be Baire. An arbitrary product of complete metric spaces is Baire, while the product of two Baire spaces need not be Baire. The rationals are meagre in themselves and are not Baire, while the irrationals are completely metrisable and Baire; the Sorgenfrey line is a Baire space that is neither locally compact nor completely metrisable nor Čech-complete; and the space $\mathbb{N}^{\mathbb{N}}$ is a completely metrisable Baire space whose name collides with the class of Baire spaces, and which the corpus calls the **Baire space of sequences**. The **Banach–Mazur game** of nested open sets characterises the class: a space is Baire if and only if the first player has no winning strategy, and the general game with a target set identifies the meagre sets as exactly those on which the second player has a winning strategy. The functional-analytic consequences of the category theorem belong to Part III, where the norms and the limits are available.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $X, Y$ | Topological spaces |
| $\overline{A}$, $A^\circ$ | Closure and interior of $A$ |
| nowhere dense | $(\overline{A})^\circ = \emptyset$ |
| meagre, first category | Countable union of nowhere dense sets |
| comeagre, residual | Complement of a meagre set |
| second category | Not meagre |
| Baire space | Every countable intersection of dense open sets is dense |
| Baire property, almost open | $A = U \,\triangle\, M$, $U$ open, $M$ meagre |
| Banach category theorem | Disjoint open meagre sets have meagre union |
| $G_\delta$ | Countable intersection of open sets |
| Čech-complete | $G_\delta$ in a compactification; complete metrisability when metrisable |
| $BM(X)$ | Banach–Mazur game of nested nonempty open sets |
| $MB(X,Y,\mathcal{W})$ | General Banach–Mazur game with target $X$ and admissible family $\mathcal{W}$ |
| $\mathbb{N}^{\mathbb{N}}$, $\mathcal{N}$ | The Baire space of sequences |
| $\mathbb{Q}$, $\mathbb{R} \setminus \mathbb{Q}$ | The rationals (meagre, not Baire) and the irrationals (Baire) |
| $\{0,1\}^{I}$ | Compact Hausdorff non-metrisable Baire space |



## Further Reading

- John C. Oxtoby, *Measure and Category* (Springer, 2nd ed. 1980), for the calculus of meagre sets, the Baire category theorem and the Banach–Mazur game. The measure-theoretic chapters are the subject of Part III.
- John C. Oxtoby, "The Banach–Mazur Game and Banach Category Theorem", in *Contributions to the Theory of Games*, Volume III, Annals of Mathematics Studies 39 (Princeton, 1957), 159–163, for the game characterisation.
- Ryszard Engelking, *General Topology* (Heldermann, revised ed. 1989), for Baire spaces, Čech-completeness and the permanence properties.
- Kazimierz Kuratowski, *Topology*, Volume I (Academic Press, 1966), for the classical treatment of category and the Baire property.
- Alexander S. Kechris, *Classical Descriptive Set Theory* (Springer, 1995), for the Baire space of sequences, the Baire property and the game characterisations.
- Zdeněk Frolík, "Baire Spaces and Some Generalisations", *Bulletin de l'Académie Polonaise des Sciences* 9 (1961), 105–107, for the relation between Baireness and completeness conditions.
- R. Telgársky, "Topological Games: On the 50th Anniversary of the Banach–Mazur Game", *Rocky Mountain Journal of Mathematics* 17 (1987), 227–276, for the survey of the game and its refinements.
