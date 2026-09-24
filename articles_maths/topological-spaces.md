
# __Topological Spaces__

## Introduction

A group carries an operation, and to speak of an operation that is *continuous* one needs a topology. This article develops the topology that the rest of the corpus uses: the axioms of a topological space, the constructions that build new spaces from old (subspaces, products, quotients), the two notions of convergence (nets and filters) that survive when sequences do not suffice, the separation axioms that make limits unique and quotients well behaved, and the properties — connectedness and compactness — that topological groups and measure theory actually invoke. It is a preparation, rather than a general course in topology: spaces that are not at least Tychonoff appear only as counterexamples, and the metrisation theory, dimension theory and homotopy theory are omitted.

The material is standard and is stated with proofs or with an explicit citation to the standard literature. Throughout, $R$ denotes a commutative ring with identity $1 \neq 0$ and $F$, $K$ denote fields; the topological examples are mostly $\mathbb{R}$ and $\mathbb{C}$, and the article on *Metric, Uniform and Complete Spaces*, written in parallel, takes up the metric case in detail. The value system is that of the corpus: a topology is described by open sets and their finite intersections and arbitrary unions, and every subsequent statement is checked against that description. No physics is invoked.

The article onmay be consulted for the concrete theory of the real line, which is the model case of everything below.

## Topological Spaces

### The Axioms

**Definition.** A **topology** on a set $X$ is a family $\tau$ of subsets of $X$, called the **open sets**, such that

**(T1)** $\emptyset \in \tau$ and $X \in \tau$;

**(T2)** if $U_i \in \tau$ for all $i \in I$, then $\bigcup_{i \in I} U_i \in \tau$;

**(T3)** if $U, V \in \tau$, then $U \cap V \in \tau$, and hence any finite intersection of open sets is open.

A **topological space** is a pair $(X, \tau)$; when no confusion can arise one writes $X$. A set $F \subseteq X$ is **closed** if its complement $X \setminus F$ is open. By De Morgan's laws, the closed sets are closed under finite unions and arbitrary intersections, contain $\emptyset$ and $X$, and the axioms (T1)–(T3) could equally well be stated for closed sets.

The condition (T3) is finite and not countable: the intersection of countably many open sets need not be open. In $\mathbb{R}$ with its usual topology,

$$
\bigcap_{n \geq 1} \left(-\tfrac{1}{n}, \tfrac{1}{n}\right) = \{0\},
$$

which is not open.

**Definition.** A **neighbourhood** of a point $x \in X$ is a subset $N \subseteq X$ containing an open set $U$ with $x \in U$. A neighbourhood need not be open. A family $\mathcal{N}_x$ of neighbourhoods of $x$ is a **neighbourhood base** at $x$ if every neighbourhood of $x$ contains a member of $\mathcal{N}_x$.

**Definition.** The **interior** $\operatorname{int} A$ of a set $A$ is the union of all open sets contained in $A$, an open set; $A$ is open exactly when $A = \operatorname{int} A$. The **closure** $\overline{A}$ is the intersection of all closed sets containing $A$, a closed set; $A$ is closed exactly when $A = \overline{A}$. The **boundary** is $\partial A = \overline{A} \cap \overline{X \setminus A}$, and the three sets $\operatorname{int} A$, $\partial A$ and $\operatorname{int}(X \setminus A)$ partition $X$:

$$
\operatorname{int} A = \bigcup \{U : U \text{ open}, \ U \subseteq A\}, \qquad
\overline{A} = \bigcap \{F : F \text{ closed}, \ A \subseteq F\}.
$$

**Proposition.** Let $A \subseteq X$. Then $x \in \overline{A}$ if and only if every neighbourhood of $x$ meets $A$. Consequently $x \in \operatorname{int} A$ if and only if $A$ is a neighbourhood of $x$, and $X = \operatorname{int} A \sqcup \partial A \sqcup \operatorname{int}(X \setminus A)$.

**Proof.** If $x \notin \overline{A}$ then $X \setminus \overline{A}$ is an open neighbourhood of $x$ disjoint from $A$. Conversely if $N$ is a neighbourhood of $x$ disjoint from $A$, choose an open $U \subseteq N$ with $x \in U$; then $U \cap A = \emptyset$, so $X \setminus U$ is a closed set containing $A$, hence $\overline{A} \subseteq X \setminus U$ and $x \notin \overline{A}$. The second claim follows from the first applied to $X \setminus A$. $\square$

### Examples and Comparisons

**Example (metric topology).** If $(X, d)$ is a metric space, the **metric topology** on $X$ has for open sets the unions of open balls $B(x, r) = \{y : d(x, y) < r\}$. The axioms are verified in *Metric, Uniform and Complete Spaces*; every metric space is a topological space in this way, and the balls with rational radius around points of a dense subset form a countable base when $X$ is separable.

**Example (discrete and trivial).** The **discrete** topology $\tau = \mathcal{P}(X)$ makes every set open; the **trivial** (or indiscrete) topology $\tau = \{\emptyset, X\}$ makes only those two sets open. Every function out of a discrete space is continuous, and every function into a trivial space is continuous.

**Example (cofinite).** The **cofinite** topology on $X$ has as open sets $\emptyset$ and the sets with finite complement. It is the discrete topology when $X$ is finite, and it is $T_1$ but not Hausdorff when $X$ is infinite.

**Example (Sorgenfrey).** The **Sorgenfrey line** has for a base the half-open intervals $[a, b)$ with $a < b$ in $\mathbb{R}$. It is finer than the usual topology, is separable and first countable, and its square is not normal, the standard example of a failure of normality under products.

**Definition.** If $\tau_1$ and $\tau_2$ are topologies on $X$ with $\tau_1 \subseteq \tau_2$, then $\tau_1$ is **coarser** than $\tau_2$ and $\tau_2$ is **finer**. The discrete topology is the finest and the trivial topology the coarsest on $X$. The set of topologies on $X$ is partially ordered by inclusion, and the supremum of a family of topologies is the topology generated by their union, while the infimum is the intersection of the families.

The comparison of topologies is not a technicality. In a topological group the group topology is often specified as the coarsest topology making certain maps continuous, or as the finest making certain subgroups open, and the two constructions, the initial and the final topology, are precisely the infimum-type and supremum-type operations of the next sections.

## Bases, Subbases and Local Bases

### Bases and Subbases

**Definition.** A family $\mathcal{B}$ of open sets of a topological space $X$ is a **base** for the topology if every open set is a union of members of $\mathcal{B}$. A family $\mathcal{S}$ of open sets is a **subbase** if the finite intersections of members of $\mathcal{S}$ form a base; equivalently, $\mathcal{S}$ generates the topology as the smallest topology containing it.

**Proposition (base criterion).** A family $\mathcal{B}$ of subsets of $X$ is a base for some topology on $X$ if and only if $\bigcup \mathcal{B} = X$ and for all $B_1, B_2 \in \mathcal{B}$ and every $x \in B_1 \cap B_2$ there is $B_3 \in \mathcal{B}$ with $x \in B_3 \subseteq B_1 \cap B_2$. The sets that are unions of members of $\mathcal{B}$ then form a topology, the **generated** topology.

**Proof.** The conditions are necessary because $X$ is open in the generated topology, hence a union of base elements, and $B_1 \cap B_2$ is open, hence a union of base elements through each of its points. They are sufficient because the empty union gives $\emptyset$, the covering condition gives $X$, arbitrary unions are unions, and if $U = \bigcup B_i$ and $V = \bigcup C_j$, then $U \cap V = \bigcup_{i,j} B_i \cap C_j$, and each $B_i \cap C_j$ is a union of base elements by the hypothesis applied at each of its points. $\square$

**Definition.** A topological space is **first countable** if every point has a countable neighbourhood base, and **second countable** if it has a countable base. First countability is a local condition, inherited by subspaces and countable products; second countability is inherited by subspaces and countable products, and implies separability and the Lindelöf property.

**Proposition.** In a first countable space, the closure of $A$ is the set of limits of sequences in $A$: $x \in \overline{A}$ if and only if some sequence in $A$ converges to $x$. In a second countable space every open cover has a countable subcover.

**Proof.** If $x \in \overline{A}$ and $(U_n)$ is a decreasing countable neighbourhood base at $x$, choose $a_n \in A \cap U_n$, which is nonempty by the closure criterion; then $a_n \to x$. Conversely a limit of points of $A$ lies in $\overline{A}$. The second statement follows by choosing, for each $x$ in the space, a base element $B_x$ containing $x$ and contained in some member of the cover, and reducing to the countable set of the $B_x$. $\square$

### Neighbourhood Bases at a Point

For many constructions it is the neighbourhood base at a single point that matters, and for groups that point is the identity.

**Proposition.** Let $\mathcal{N}_x$ be a neighbourhood base at $x$, consisting of open sets. Then $U \subseteq X$ is a neighbourhood of $x$ if and only if $U$ contains a member of $\mathcal{N}_x$; and the data $(\mathcal{N}_x)_{x \in X}$ determines the topology, since $U$ is open if and only if $U$ is a neighbourhood of each of its points.

**Proof.** Immediate from the definitions. $\square$

This is the form in which the topology of a topological group will be specified: a local base at the identity, translated to every other point by the group operation, determines the whole topology. The analogous statement for topological vector spaces uses a neighbourhood base at $0$.

## Continuity, Homeomorphism and Embedding

### Continuity

**Definition.** Let $X$ and $Y$ be topological spaces. A function $f : X \to Y$ is **continuous at** $x \in X$ if for every neighbourhood $V$ of $f(x)$ there is a neighbourhood $U$ of $x$ with $f(U) \subseteq V$. It is **continuous** if it is continuous at every point, equivalently if $f^{-1}(V)$ is open in $X$ for every open $V \subseteq Y$; equivalently, by the proposition on neighbourhood bases, if

$$
\forall x \in X \ \ \forall V \ni f(x) \ \ \exists U \ni x : \ f(U) \subseteq V .
$$

**Theorem.** For $f : X \to Y$ the following are equivalent: (a) $f$ is continuous; (b) $f^{-1}(F)$ is closed for every closed $F \subseteq Y$; (c) $f(\overline{A}) \subseteq \overline{f(A)}$ for every $A \subseteq X$; (d) for every $x \in X$ and every neighbourhood $V$ of $f(x)$ there is a neighbourhood $U$ of $x$ with $f(U) \subseteq V$.

**Proof.** (a) $\Leftrightarrow$ (b) by complements. (a) $\Leftrightarrow$ (c): if $f$ is continuous and $x \in \overline{A}$, then every neighbourhood $V$ of $f(x)$ has open preimage containing $x$, which meets $A$, so $V$ meets $f(A)$ and $f(x) \in \overline{f(A)}$. Conversely if (c) holds and $V \subseteq Y$ is open, put $A = X \setminus f^{-1}(V)$; then $f(\overline{A}) \subseteq \overline{f(A)} \subseteq Y \setminus V$, so $\overline{A} \subseteq X \setminus f^{-1}(V)$ and $f^{-1}(V)$ is open. (a) $\Leftrightarrow$ (d) is the definition. $\square$

**Theorem.** Compositions of continuous maps are continuous, and the identity is continuous. If $f : X \to Y$ is continuous and $A \subseteq X$ carries the subspace topology, then $f|_A$ is continuous.

**Proof.** For a composite, $(g \circ f)^{-1}(W) = f^{-1}(g^{-1}(W))$, open when $W$ is open. For the restriction, $(f|_A)^{-1}(V) = A \cap f^{-1}(V)$, open in the subspace topology. $\square$

The two theorems say that topological spaces and continuous maps form a category, and that restrictions and composites are morphisms in it.

### Homeomorphism and Embedding

**Definition.** A **homeomorphism** is a bijective continuous map $f : X \to Y$ whose inverse is continuous. Spaces are **homeomorphic**, written $X \cong Y$, if such an $f$ exists; a homeomorphism is an isomorphism in the category of topological spaces.

**Definition.** An **embedding** is an injective continuous map $f : X \to Y$ that is a homeomorphism onto its image $f(X)$ with the subspace topology. A continuous map is **open** if the image of every open set is open, and **closed** if the image of every closed set is closed; a bijective map is a homeomorphism exactly when it is continuous and open, equivalently continuous and closed.

**Remark.** Continuity is not a property preserved under arbitrary bijections: a continuous bijection need not have continuous inverse. The identity map from the discrete topology to the trivial topology on a set with more than one point is a continuous bijection that is not a homeomorphism. This is the reason the quotient topology below is the *final* topology for the quotient map and not the topology carried by an arbitrary bijection.

## Subspaces, Products and Quotients

### Subspaces

**Definition.** Let $(X, \tau)$ be a topological space and $A \subseteq X$. The **subspace topology** on $A$ is $\tau_A = \{U \cap A : U \in \tau\}$. The map $A \hookrightarrow X$ is then continuous, and $\tau_A$ is the coarsest topology on $A$ making the inclusion continuous; it is the **initial** topology with respect to the single map $A \to X$.

The subspace topology is characterised by a universal property: a map $f : Z \to A$ is continuous if and only if the composite $Z \to A \hookrightarrow X$ is continuous. Closed sets of the subspace are the intersections $A \cap F$ with $F$ closed in $X$; the closure of $B \subseteq A$ in the subspace topology is $\overline B \cap A$, where $\overline B$ is the closure in $X$.

### Products

**Definition.** Let $(X_i)_{i \in I}$ be topological spaces. The **product topology** on $X = \prod_i X_i$ is the topology generated by the subbase consisting of the sets $\pi_i^{-1}(U_i)$ for $i \in I$ and $U_i$ open in $X_i$, where $\pi_i : X \to X_i$ is the projection. A base is given by the products $\prod_i U_i$ with $U_i$ open in $X_i$ and $U_i = X_i$ for all but finitely many $i$, that is,

$$
\mathcal{B} = \Big\{ \prod_{i \in I} U_i : U_i \text{ open in } X_i, \ U_i = X_i \text{ for all but finitely many } i \Big\}.
$$

The restriction "all but finitely many" is essential and is the difference between the product topology and the box topology; only the former has the characteristic property of the theorem below when $I$ is infinite.

**Theorem (characteristic property).** The product topology is the coarsest topology making every projection $\pi_i$ continuous, and a map $f : Z \to \prod_i X_i$ is continuous if and only if every composite $\pi_i \circ f$ is continuous.

**Proof.** The topology generated by the $\pi_i^{-1}(U_i)$ is by construction the coarsest making all $\pi_i$ continuous, and it is the topology whose base is displayed above. If $f$ is continuous then so is each $\pi_i \circ f$. Conversely, if each $\pi_i \circ f$ is continuous, then $f^{-1}(\pi_i^{-1}(U_i)) = (\pi_i\circ f)^{-1}(U_i)$ is open, and these sets generate the product topology, so $f^{-1}$ of every open set is open. $\square$

**Theorem.** If $f_i : X_i \to Y_i$ are continuous, then $\prod_i f_i : \prod_i X_i \to \prod_i Y_i$ is continuous. The projections are open maps. A sequence in a countable product converges if and only if each coordinate sequence converges.

**Proof.** $(\prod_i f_i)^{-1}(\prod_i V_i) = \prod_i f_i^{-1}(V_i)$, open when each factor is open. For openness of $\pi_i$: the image of a basic open set of $\prod_j X_j$ is either $X_i$ or an open set. The statement on sequences follows from the continuity of the projections and, conversely, from the definition of the product topology, whose basic neighbourhoods constrain only finitely many coordinates at a time. $\square$

### Quotients and Identification Topologies

**Definition.** Let $X$ be a topological space, $Y$ a set, and $q : X \to Y$ a surjection. The **quotient topology**, or **identification topology**, on $Y$ is the family of sets $V \subseteq Y$ with $q^{-1}(V)$ open in $X$. It is the finest topology making $q$ continuous; equivalently it is the **final** topology with respect to $q$. The map $q$ is a **quotient map**.

**Theorem (characteristic property).** Let $q : X \to Y$ be a quotient map. A map $f : Y \to Z$ is continuous if and only if $f \circ q : X \to Z$ is continuous.

**Proof.** If $f$ is continuous, so is $f \circ q$. Conversely, if $f \circ q$ is continuous and $W \subseteq Z$ is open, then $q^{-1}(f^{-1}(W)) = (f \circ q)^{-1}(W)$ is open in $X$, so $f^{-1}(W)$ is open in $Y$ by definition of the quotient topology. $\square$

**Example (circle).** Let $X = [0, 1]$ and let $q$ identify $0$ with $1$, that is, $Y = X/{\sim}$ with $0 \sim 1$. Then $Y \cong S^1 = \{z \in \mathbb{C} : |z| = 1\}$ by $t \mapsto e^{2\pi i t}$, and the quotient topology is the usual one.

**Example (torus and projective spaces).** The $n$-torus is $T^n = \mathbb{R}^n/\mathbb{Z}^n$, where $\mathbb{Z}^n$ acts by translation; the real projective space is $\mathbb{R}P^n = S^n/{\pm 1}$, and the complex projective space is $\mathbb{C}P^n = S^{2n+1}/S^1$ with $S^1$ acting by scalar multiplication. Each is a quotient by a group action, and the quotient map is open in every case; the quotient is Hausdorff here because it is metrisable, not because the quotient map is open — a surjective open map of a Hausdorff space can have a non-Hausdorff target.

**Proposition.** If $q : X \to Y$ is an open continuous surjection, or a closed continuous surjection, then $q$ is a quotient map. A quotient map need not be open or closed.

**Proof.** Let $q$ be open and $V \subseteq Y$ with $q^{-1}(V)$ open. Then $V = q(q^{-1}(V))$ is open, so every set with open preimage is open, and the quotient topology consists exactly of those sets; so $q$ is a quotient map. The closed case is dual. Openness and closedness are sufficient conditions for being a quotient map, not necessary ones; standard examples of quotient maps that are neither open nor closed are collected in the counterexample literature. $\square$

The quotient construction is the one topological groups use: if $H$ is a subgroup of a topological group $G$, the quotient $G/H$ of *Transformation Groups*' coset space is given the quotient topology, and the group operations descend to it; this is treated.

## Convergence: Nets and Filters

Sequences are insufficient in general topological spaces: the closure of a set need not be the set of limits of its sequences, and a function may fail to be continuous even when it preserves sequential limits. Two equivalent remedies are used, nets and filters.

### Nets

**Definition.** A **directed set** is a pair $(A, \leq)$ with $\leq$ reflexive and transitive such that every two elements have an upper bound. A **net** in $X$ is a function $A \to X$, written $(x_\alpha)_{\alpha \in A}$. It **converges** to $x \in X$ if for every neighbourhood $U$ of $x$ there is $\alpha_0$ with $x_\alpha \in U$ for all $\alpha \geq \alpha_0$; one writes $x_\alpha \to x$. The net **has $x$ as a cluster point** if for every neighbourhood $U$ of $x$ and every $\alpha$ there is $\beta \geq \alpha$ with $x_\beta \in U$. In symbols,

$$
x_\alpha \to x \iff \forall U \ni x \ \ \exists \alpha_0 \ \ \forall \alpha \geq \alpha_0 : \ x_\alpha \in U .
$$

**Theorem.** Let $A \subseteq X$. Then $x \in \overline{A}$ if and only if there is a net in $A$ converging to $x$.

**Proof.** If $x \in \overline{A}$, direct the neighbourhoods of $x$ by reverse inclusion and choose $x_U \in U \cap A$, nonempty by the closure criterion; the resulting net converges to $x$. Conversely, if $x_\alpha \in A$ and $x_\alpha \to x$, then every neighbourhood of $x$ meets $A$, so $x \in \overline{A}$. $\square$

**Theorem.** A map $f : X \to Y$ is continuous if and only if $x_\alpha \to x$ in $X$ implies $f(x_\alpha) \to f(x)$ in $Y$.

**Proof.** If $f$ is continuous and $V$ is a neighbourhood of $f(x)$, then $f^{-1}(V)$ is a neighbourhood of $x$, so eventually $x_\alpha \in f^{-1}(V)$ and $f(x_\alpha) \in V$. Conversely, if $f$ is not continuous at $x$, there is a neighbourhood $V$ of $f(x)$ with $f^{-1}(V)$ not a neighbourhood of $x$; for every neighbourhood $U$ of $x$ choose $x_U \in U \setminus f^{-1}(V)$. Then $x_U \to x$ but $f(x_U) \notin V$, so $f(x_U) \not\to f(x)$. $\square$

### Filters

**Definition.** A **filter** on $X$ is a nonempty family $\mathcal{F}$ of subsets of $X$, none of them empty, closed under finite intersections and under supersets: if $A, B \in \mathcal{F}$ then $A \cap B \in \mathcal{F}$, and if $A \in \mathcal{F}$ and $A \subseteq B$ then $B \in \mathcal{F}$; the first closure property and the nonemptiness make $X \in \mathcal{F}$. A **filter base** is a family $\mathcal{B}$ such that every finite intersection of members contains a member, and the filter it generates is the family of supersets of members of $\mathcal{B}$. A filter **converges** to $x$, written $\mathcal{F} \to x$, if every neighbourhood of $x$ belongs to $\mathcal{F}$; $x$ is a **cluster point** of $\mathcal{F}$ if every neighbourhood of $x$ meets every member of $\mathcal{F}$.

The neighbourhood filter $\mathcal{N}_x$ of all neighbourhoods of $x$ is the filter generated by any neighbourhood base at $x$, and $\mathcal{N}_x \to x$.

**Theorem.** A set $A$ is closed if and only if no filter that contains $A$ and converges in $X$ converges to a point outside $A$; equivalently, if a filter on $A$ converges in $X$ to $x$, then $x \in A$. A space is Hausdorff if and only if every filter converges to at most one point.

**Proof.** If $A$ is closed, $A \in \mathcal{F}$ and $\mathcal{F} \to x \notin A$, then $X \setminus A$ is a neighbourhood of $x$, so $X \setminus A \in \mathcal{F}$ and $\emptyset = A \cap (X \setminus A) \in \mathcal{F}$, impossible. Conversely if $A$ is not closed pick $x \in \overline{A} \setminus A$; the family $\{A \cap U : U \in \mathcal{N}_x\}$ is a filter base on $A$, since a finite intersection of its members contains $A \cap (U_1 \cap \cdots \cap U_n)$, and the filter it generates contains $A$ and converges to $x \notin A$. For the second statement, if $x \neq y$ have disjoint neighbourhoods $U, V$, a filter converging to both would contain $U \cap V = \emptyset$; conversely, if some two distinct points $x, y$ have no disjoint neighbourhoods, then the family $\{U \cap V : U \in \mathcal{N}_x, V \in \mathcal{N}_y\}$ consists of nonempty sets and a finite intersection of its members contains $(\bigcap_i U_i) \cap (\bigcap_i V_i)$, so it is a filter base; the filter it generates contains $\mathcal{N}_x$ and $\mathcal{N}_y$ and therefore converges to both $x$ and $y$. $\square$

### Equivalence and Ultrafilters

A net $(x_\alpha)_{\alpha \in A}$ generates the filter of sets containing some tail of the net, and a filter generates a net by directing its members by reverse inclusion and choosing a point of each. Under this correspondence convergence and cluster points are preserved, so the two languages are interchangeable; nets are used for the theorems and filters for the compactness proofs.

**Definition.** An **ultrafilter** is a filter maximal under inclusion. Every filter is contained in an ultrafilter, by Zorn's lemma, and an ultrafilter $\mathcal{U}$ has the property that for every $A \subseteq X$, exactly one of $A$ and $X \setminus A$ lies in $\mathcal{U}$.

**Theorem.** A space $X$ is compact if and only if every ultrafilter on $X$ converges. It is compact and Hausdorff if and only if every ultrafilter converges to a unique point.

**Proof.** If $X$ is compact and an ultrafilter $\mathcal{U}$ converges at no point, then for every $x$ there is a neighbourhood $U_x \notin \mathcal{U}$, and by maximality $X \setminus U_x \in \mathcal{U}$. Finitely many of the $U_x$ cover $X$, so the intersection of the corresponding complements is empty and $\emptyset \in \mathcal{U}$, a contradiction. Conversely, if every ultrafilter converges and $\{U_i\}$ is an open cover with no finite subcover, the complements $X \setminus U_i$ have the finite intersection property — a finite intersection of them is the complement of a finite union, which is nonempty — so they generate a filter, hence are contained in an ultrafilter $\mathcal{U}$. A limit point of $\mathcal{U}$ lies in some $U_i$, and $U_i$, being a neighbourhood of that point, then belongs to $\mathcal{U}$; but $\mathcal{U}$ also contains $X \setminus U_i$, and $U_i \cap (X \setminus U_i) = \emptyset$, a contradiction. Uniqueness in the Hausdorff case is the preceding theorem. $\square$

## Separation Axioms

### The Axioms

**Definition.** A topological space $X$ is:

- **$T_0$** if for every two distinct points some open set contains exactly one of them;
- **$T_1$** if for every two distinct points each has a neighbourhood missing the other, equivalently if points are closed;
- **Hausdorff**, or **$T_2$**, if every two distinct points have disjoint neighbourhoods;
- **regular**, or **$T_3$**, if it is $T_1$ and every point has a neighbourhood base of closed neighbourhoods, equivalently if a point and a disjoint closed set can be separated by disjoint open sets;
- **normal**, or **$T_4$**, if it is $T_1$ and any two disjoint closed sets can be separated by disjoint open sets.

The implications

$$
T_4 \Rightarrow T_3 \Rightarrow T_2 \Rightarrow T_1 \Rightarrow T_0
$$

hold, and they do not reverse in general: the cofinite topology on an infinite set is $T_1$ but not Hausdorff. Normality in particular is not productive, since the Sorgenfrey line is normal while its square is not, and the standard counterexamples separating the remaining axioms are collected in the counterexample literature.

**Proposition.** A space is Hausdorff if and only if the diagonal $\Delta_X = \{(x, x)\} \subseteq X \times X$ is closed. If $f, g : X \to Y$ are continuous with $Y$ Hausdorff, then the set $\{x : f(x) = g(x)\}$ is closed; in particular a continuous map into a Hausdorff space is determined by its values on a dense subset.

**Proof.** $\Delta_X$ is closed exactly when for $x \neq y$ there are basic open sets $U, V$ with $(x, y) \in U \times V$ disjoint from $\Delta_X$, that is, $U \cap V = \emptyset$. For the second statement apply the first to $X \to Y \times Y$, $x \mapsto (f(x), g(x))$. $\square$

### The Separation Theorems

**Theorem (Urysohn's lemma).** If $X$ is normal and $A, B \subseteq X$ are disjoint closed sets, then there is a continuous $f : X \to [0, 1]$ with $f = 0$ on $A$ and $f = 1$ on $B$.

**Theorem (Tietze extension theorem).** If $X$ is normal, $A \subseteq X$ closed, and $f : A \to [a, b]$ continuous, then $f$ extends to a continuous $g : X \to [a, b]$.

Both are standard, and each implies the other; Urysohn's lemma is the source of the partition of unity, which measure theory and the theory of integration on topological groups use.

**Theorem.** Every compact Hausdorff space is normal, hence satisfies Tietze and Urysohn. Every metric space is normal.

**Proof.** If $X$ is compact Hausdorff and $A, B$ disjoint closed sets, compactness gives each $a \in A$ a neighbourhood with closure disjoint from $B$; a finite subcover and a second compactness argument separate $A$ from $B$. For a metric space, separate disjoint closed $A, B$ by the open sets $\{x : d(x, A) < d(x, B)\}$ and $\{x : d(x, B) < d(x, A)\}$. $\square$

**Remark.** Hausdorffness is the working hypothesis in this category. It guarantees uniqueness of limits of nets and filters, it is inherited by subspaces and arbitrary products, and it makes a quotient $G/H$ of a topological group Hausdorff exactly when $H$ is closed, asshows. Regularity is inherited by subspaces and products; normality is inherited by closed subspaces but not by arbitrary products.

## Connectedness

### Connected Spaces

**Definition.** A topological space $X$ is **connected** if it is not the union of two disjoint nonempty open sets; equivalently, if the only subsets that are both open and closed are $\emptyset$ and $X$. A **separation** of $X$ is a pair of disjoint nonempty open sets whose union is $X$. A subset $A \subseteq X$ is connected if it is connected in the subspace topology.

**Theorem.** Continuous images of connected spaces are connected. If $A \subseteq X$ is connected and $A \subseteq B \subseteq \overline{A}$, then $B$ is connected. Arbitrary unions of connected sets with a common point are connected.

**Proof.** If $f : X \to Y$ is continuous and $f(X) = U \sqcup V$ with $U, V$ disjoint nonempty open, then $X = f^{-1}(U) \sqcup f^{-1}(V)$ is a separation. If $B = U \sqcup V$ is a separation with $U, V$ open in $B$, then $A \cap U$ and $A \cap V$ are open in $A$ and cannot both be nonempty; say $A \subseteq U$. Then $A \subseteq B \setminus V$, which is closed in $B$, so $\overline{A} \cap B \subseteq B \setminus V$ and $V = \emptyset$, a contradiction. For a union, any separation restricts to a separation of each connected set, forcing each to lie on one side; the common point forces all on the same side. $\square$

**Theorem.** The connected subsets of $\mathbb{R}$ are exactly the intervals. In particular $\mathbb{R}$ and every interval are connected, and the intermediate value theorem is the statement that the continuous image of an interval is an interval.

**Proof.** A subset with a gap $a < c < b$, $a, b \in A$, $c \notin A$, is separated by $A \cap (-\infty, c)$ and $A \cap (c, \infty)$, so a connected subset is an interval. Conversely, if an interval $J$ had a separation $J = U \sqcup V$ with $U, V$ nonempty and open in $J$, pick $u \in U$, $v \in V$ and let $s = \sup(U \cap [u, v])$, a point of $J$ lying between $u$ and $v$ and in the closure of $U \cap [u, v]$. Since $U$ and $V$ partition $J$, the point $s$ lies in one of them; if $s \in U$, openness of $U$ in $J$ gives points of $U \cap [u, v]$ above $s$, contradicting the defining property of the supremum, and if $s \in V$, openness of $V$ gives a whole interval around $s$ inside $V$, so that $\sup(U \cap [u,v]) < s$, again a contradiction. $\square$

### Components and Path Connectedness

**Definition.** The **connected component** of $x \in X$ is the union of all connected subsets containing $x$, itself connected by the union theorem. The components partition $X$; each is closed, and a connected space has exactly one component. The space is **totally disconnected** if every component is a singleton.

**Definition.** A **path** in $X$ from $x$ to $y$ is a continuous map $\gamma : [0, 1] \to X$ with $\gamma(0) = x$, $\gamma(1) = y$; the space is **path connected** if every two points are joined by a path. It is **locally (path) connected** if every point has a neighbourhood base of (path) connected neighbourhoods.

**Proposition.** A path connected space is connected. The converse fails: the **topologist's sine curve**, the union of the graph of $\sin(1/x)$ for $x > 0$ with the segment $\{0\} \times [-1, 1]$, is connected but not path connected.

**Proof.** A path connected space is the union of the images of paths from a fixed base point, each connected, sharing that point. The sine curve is the closure of a connected graph and hence connected; it is not path connected because a path approaching the segment has no limit, so no path reaches it from the graph. $\square$

**Example.** A discrete space with more than one point is totally disconnected. The rationals $\mathbb{Q}$ are totally disconnected: a connected subset is an interval, and no interval of rationals with more than one point is connected. A profinite group, treated, is compact, Hausdorff and totally disconnected, and this is why it is assembled from finite quotients.

**Theorem.** The product of connected spaces is connected, and the product of path connected spaces is path connected.

**Proof.** For two spaces $X, Y$ and $(x, y) \in X \times Y$, the union $\{x\} \times Y \cup X \times \{y\}$ is connected, and $X \times Y$ is the union over $y' \in Y$ of these connected sets, all meeting $\{x\} \times Y$; the union theorem gives connectedness. For a general product fix a point $(x_i)_{i \in I}$; for each finite set $F \subseteq I$ the set of points agreeing with $(x_i)$ outside $F$ is homeomorphic to the finite product $\prod_{i \in F} X_i$, hence connected, and all of these sets contain $(x_i)$, so their union is connected; that union is dense, since a basic open set constrains only finitely many coordinates, so its closure, which is the whole product, is connected as well. Path connectedness is immediate from the coordinate-wise construction of paths. $\square$

## Compactness

### Compact Spaces

**Definition.** An **open cover** of $X$ is a family of open sets whose union is $X$. The space $X$ is **compact** if every open cover has a finite subcover. A subset $K \subseteq X$ is compact if it is compact in the subspace topology.

**Theorem (finite intersection property).** $X$ is compact if and only if every family of closed subsets of $X$ with the finite intersection property has nonempty intersection.

**Proof.** Take complements: a cover with no finite subcover is a family of closed sets with the finite intersection property and empty intersection, and conversely. $\square$

**Theorem.** A closed subset of a compact space is compact, and a compact subset of a Hausdorff space is closed. Continuous images of compact spaces are compact. A compact Hausdorff space is normal.

**Proof.** For the first, add the complement to an open cover of the closed subset. For the second, if $K$ is compact in a Hausdorff $X$ and $x \notin K$, separate $x$ from each point of $K$; compactness gives finitely many neighbourhoods whose intersection is disjoint from a neighbourhood of $K$, so $X \setminus K$ is open. For the third, the preimage of a cover is a cover. Normality was stated above. $\square$

**Theorem (tube lemma).** Let $Y$ be compact and let $N$ be an open set in $X \times Y$ containing $\{x_0\} \times Y$. Then there is a neighbourhood $U$ of $x_0$ with $U \times Y \subseteq N$.

**Proof.** For each $y \in Y$ choose a basic neighbourhood $U_y \times V_y \subseteq N$ of $(x_0, y)$; finitely many $V_y$ cover $Y$, and $U = \bigcap U_y$ works. $\square$

**Corollary.** The product of finitely many compact spaces is compact.

**Proof.** For two spaces, let $\{W_i\}$ be an open cover of $X \times Y$. For $x \in X$ the slice $\{x\} \times Y$ is compact, being homeomorphic to the compact space $Y$, so it is covered by finitely many of the $W_i$; their union is an open set containing the slice, so the tube lemma gives a neighbourhood $U_x$ of $x$ with $U_x \times Y$ covered by those same finitely many members of the cover. Finitely many of the $U_x$ cover $X$ by compactness, and the corresponding finitely many members of $\{W_i\}$ then cover $X \times Y$. Induction gives the finite case. $\square$

**Theorem (Tychonoff).** An arbitrary product of compact spaces is compact: if each $X_i$ is compact, then so is

$$
\prod_{i \in I} X_i
$$

with the product topology.

The proof is by ultrafilters: given an ultrafilter on the product, its coordinate images generate ultrafilters on the compact factors, each converging, and the limit in the product is the limit of the original ultrafilter. The theorem is equivalent to the axiom of choice modulo the other axioms of set theory, and it is the compactness input for the existence of limits of inverse systems, hence for profinite groups.

**Example (Heine–Borel).** A subset of $\mathbb{R}^n$ is compact if and only if it is closed and bounded,

$$
K \subseteq \mathbb{R}^n \text{ compact} \iff K \text{ closed and bounded}.
$$

In a general metric space compactness is equivalent to sequential compactness and to completeness together with total boundedness, the standard metric characterisation of compactness, and it is the reason metric arguments may use sequences where general topological arguments may not.

### Local Compactness and One-Point Compactification

**Definition.** A space $X$ is **locally compact** if every point has a neighbourhood base of compact neighbourhoods; equivalently, every point has a compact neighbourhood, provided $X$ is Hausdorff. It is **$\sigma$-compact** if it is a countable union of compact subsets.

**Definition.** The **one-point compactification** of a locally compact Hausdorff space $X$ that is not compact is $X^+ = X \cup \{\infty\}$, with open sets the open sets of $X$ and the sets $\{\infty\} \cup (X \setminus K)$ for $K \subseteq X$ compact. Then $X^+$ is compact Hausdorff and $X$ is an open dense subspace; in symbols the new neighbourhoods of the point at infinity are

$$
\{\infty\} \cup (X \setminus K), \qquad K \subseteq X \text{ compact}.
$$

**Example.** The one-point compactification of $\mathbb{R}^n$ is $S^n$; of $\mathbb{R}$ is $S^1$; of a discrete space is the **Alexandrov compactification**, with $\infty$ the only non-isolated point. The one-point compactification of the natural numbers is the convergent sequence $\{0\} \cup \{1/n\}$.

**Remark.** Local compactness and $\sigma$-compactness are the hypotheses under which measure theory produces the standard measures. A locally compact Hausdorff group admits a Haar measure, and a locally compact Hausdorff space has a rich supply of continuous functions of compact support; both facts are used . The relevant topological input is exhausted by the results above: Tychonoff for products and inverse limits, the quotient topology for coset spaces, and the separation theorems for the construction of functions.

## Summary

A topological space is a set with a family of open sets closed under arbitrary unions and finite intersections. Closed sets are their complements, neighbourhoods are supersets of open sets containing a point, and interior, closure and boundary are organised by the criterion $x \in \overline{A}$ if and only if every neighbourhood of $x$ meets $A$. A base generates the topology by unions and a subbase by finite intersections; a neighbourhood base at a single point determines the topology, which is the form used for topological groups.

Continuity is the condition that preimages of open sets are open, and it is equivalent to $f(\overline{A}) \subseteq \overline{f(A)}$ and to net preservation. Homeomorphisms are the isomorphisms; subspaces carry the coarsest topology making the inclusion continuous, products the coarsest topology making the projections continuous, and quotients the finest topology making the quotient map continuous. Each construction is characterised by a universal property, and quotient maps are detected by testing maps out of the quotient.

Nets and filters give equivalent accounts of convergence; a space is Hausdorff exactly when limits are unique, and compact exactly when every ultrafilter converges. The separation axioms run $T_0 \Rightarrow T_1 \Rightarrow$ Hausdorff $\Rightarrow$ regular $\Rightarrow$ normal, with Urysohn's lemma and the Tietze extension theorem available in normal spaces and hence in compact Hausdorff and in metric spaces. Connectedness is the refusal to split into two disjoint nonempty open pieces; the connected subsets of $\mathbb{R}$ are intervals, components are closed, and path connectedness is stronger. Compactness is the finite subcover property, equivalent to the finite intersection property for closed sets; it is preserved by continuous images and finite products, arbitrary products are compact by Tychonoff, a compact subset of a Hausdorff space is closed and a compact Hausdorff space is normal, and local compactness supplies the one-point compactification used in measure theory and in the theory of locally compact groups.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $X, Y, Z$ | Topological spaces |
| $\tau$ | A topology; a family of open sets |
| $U, V$ | Open sets; $F$ closed |
| $N$ | Neighbourhood of a point; need not be open |
| $\operatorname{int} A$, $\overline{A}$, $\partial A$ | Interior, closure and boundary of $A$ |
| $x \in \overline{A}$ | Closure criterion: every neighbourhood of $x$ meets $A$ |
| $\mathcal{B}$, $\mathcal{S}$ | Base and subbase for a topology |
| $f : X \to Y$ continuous | $f^{-1}(V)$ open for every open $V$ |
| $X \cong Y$ | Homeomorphic spaces |
| $A \subseteq X$ | Subspace topology $U \cap A$ |
| $X \times Y$, $\prod_i X_i$, $\pi_i$ | Product and projections; product topology |
| $X/{\sim}$, $q : X \to Y$ | Quotient (identification) topology and quotient map |
| $S^1$, $T^n$, $\mathbb{R}P^n$, $\mathbb{C}P^n$ | Standard quotients |
| $(x_\alpha)_{\alpha \in A}$, $x_\alpha \to x$ | Net and its convergence |
| $\mathcal{F}$, $\mathcal{N}_x$ | Filter and the neighbourhood filter at $x$; filter convergence |
| $\mathcal{U}$ | Ultrafilter |
| $T_0, T_1, T_2, T_3, T_4$ | Separation axioms; Hausdorff, regular, normal |
| $\Delta_X \subseteq X \times X$ | Diagonal; closed exactly when $X$ is Hausdorff |
| connected, path connected | No separation; path-joined |
| $\sigma$-compact | Countable union of compact sets |
| $X^+ = X \cup \{\infty\}$ | One-point compactification |



## Further Reading

- James R. Munkres, *Topology* (Prentice Hall, 2nd ed. 2000), for the standard first course, including nets, filters and Tychonoff's theorem.
- John L. Kelley, *General Topology* (Van Nostrand, 1955; reprinted Springer, 1975), for the classical treatment with nets as the primary convergence notion.
- Nicolas Bourbaki, *General Topology*, Chapters 1–4 (Springer, 1995), for filters, uniform structures and the separation axioms in their systematic form.
- Stephen Willard, *General Topology* (Addison-Wesley, 1970; reprinted Dover, 2004), for a clear account of separation axioms and counterexamples.
- Lynn A. Steen and J. Arthur Seebach, *Counterexamples in Topology* (Springer, 2nd ed. 1978), for the spaces that separate the axioms.
- Ryszard Engelking, *General Topology* (Heldermann, revised ed. 1989), for a comprehensive reference including compactness and paracompactness.
- Kiyosi Itô, ed., *Encyclopedic Dictionary of Mathematics* (MIT Press, 2nd ed. 1987), for concise statements of the standard theorems used in the later articles.
