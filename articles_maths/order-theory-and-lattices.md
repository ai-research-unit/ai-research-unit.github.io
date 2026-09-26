
# __Order Theory and Lattices__

## Introduction

A partial order records when one object is below another, and much of algebra is order in disguise: a subgroup is below another when it is contained in it, and a quotient is often the greatest object of a given kind. This article develops the theory of orders for its own sake: it defines partial, total and well-orders, isolates the two binary operations that an order may support — the least upper bound and the greatest lower bound — and studies the structures, the **lattices**, in which those operations are always defined. It then treats the two results that the corpus uses in its analysis: the **Galois connection**, the order-theoretic form of a closure, and the fixed-point theorem of **Knaster and Tarski**.

The article presupposes the language of *Sets, Functions and Relations* — subsets, ordered pairs, relations, equivalence relations and functions — and the propositional logic of *Logic and Proof*, and it uses the natural numbers as basic. Two boundaries are observed. The **axiom of choice** and Zorn's lemma are not proved or used here; they belong to the foundations, and the article distinguishes the results constructive in the order alone from those that require a choice principle. **Boolean algebra** is developed as a subject in Part V; the power-set lattice is introduced here as the standard example, and the general theory is deferred.

The article treats no topology. The words *complete*, *closed* and *limit* occur below with their order-theoretic meanings — an order-complete lattice, a closed element of a closure system, the supremum of a chain — and in those senses only. Where a result has a richer statement once a distance exists, the statement is given in the language of order and the enrichment is deferred to Part II.

## Orders

### Partial Orders

**Definition.** A **partial order** on a set $P$ is a relation $\leq$ that is reflexive, antisymmetric and transitive; the pair $(P, \leq)$ is a **partially ordered set**, or **poset**. A **strict partial order** is an irreflexive transitive relation $<$, and it is related to a partial order by the equivalences $x < y \iff x \leq y$ and $x \neq y$ and $x \leq y \iff x < y$ or $x = y$.

The standard order on $\mathbb{N}$ and the inclusion on the subsets of a set are partial orders, as noted in *Sets, Functions and Relations*. A partial order is a **total order** (or **linear order**) if any two elements are comparable: $x \leq y$ or $y \leq x$ for all $x, y \in P$. A **chain** in a poset is a subset that is totally ordered by the inherited relation; an **antichain** is a subset in which no two distinct elements are comparable. A **well-order** is a total order in which every nonempty subset has a least element; the usual order on $\mathbb{N}$ is the model, and the general theory of well-orders and of transfinite induction on them belongs.

**Example.** Let $P = \{1, 2, 3, 4, 6, 12\}$ with $x \leq y$ when $x$ divides $y$. This is a partial order that is not total: $2$ and $3$ are incomparable. The divisibility poset is the standard example in which meets and joins are familiar operations.

**Example.** Let $X$ be a set and let $P$ be the set of **partitions** of $X$, ordered by refinement: $\pi \leq \sigma$ when every block of $\pi$ is contained in a block of $\sigma$. This is a partial order, and it is the order that the equivalence relations of *Sets, Functions and Relations* inherit from set inclusion of relations.

**Example.** Any set $P$ carries the **discrete order**, in which $x \leq y$ only when $x = y$, and the **indiscrete order**, in which $x \leq y$ for all $x, y$. These are the extreme cases and are used in the theory of Galois connections below.

### Total Orders, Chains and Well-Orders

**Definition.** A **least element** of a subset $S \subseteq P$ is an $m \in S$ with $m \leq s$ for all $s \in S$; a **minimal element** is an $m \in S$ such that no $s \in S$ satisfies $s < m$. A **greatest** and a **maximal** element are defined dually.

A least element, when it exists, is unique by antisymmetry, and it is minimal; a minimal element need not be least when the order is partial, since it may be incomparable with other elements. In a total order the two notions coincide and the distinction disappears. This is the reason total orders are easier than partial orders, and it is the reason the key existence theorems for partial orders — Zorn's lemma, the well-ordering theorem — are equivalent to the axiom of choice.

**Proposition.** Let $(P, \leq)$ be a poset.

1. If every nonempty subset of $P$ has a least element, then $P$ is totally ordered and every strictly decreasing sequence $x_0 > x_1 > x_2 > \cdots$ terminates.
2. Conversely, if $P$ is totally ordered and every strictly decreasing sequence terminates, then every nonempty subset of $P$ has a least element.

**Proof.** (1) If $P$ had incomparable $x, y$ then $\{x, y\}$ would have no least element; and the terms of a strictly decreasing sequence form a nonempty subset without a least element. (2) If $S \neq \emptyset$ had no least element, then for each $x \in S$ the set $\{s \in S : s < x\}$ is nonempty, and a nonterminating strictly decreasing sequence is obtained by choosing $x_0 \in S$ and then $x_{n+1} < x_n$ for each $n$, contradicting the hypothesis. $\square$

The two directions are not on the same footing: (1) is a theorem of the order alone, whereas (2) selects infinitely many successive elements, and the selection is an instance of the axiom of dependent choice. Nothing in this article depends on (2); the statement is recorded because the condition of *no infinite descending sequence* is the form in which well-foundedness is verified elsewhere in the corpus, for instance as the termination of a rewriting process, and the choice principle that it hides is treated.

### Monotone Maps

**Definition.** Let $(P, \leq)$ and $(Q, \preceq)$ be posets. A function $f : P \to Q$ is **monotone** (or **order-preserving**, or **isotone**) if $x \leq y$ implies $f(x) \preceq f(y)$. It is an **order embedding** if in addition $f(x) \preceq f(y)$ implies $x \leq y$, and an **order isomorphism** if it is a bijective order embedding, in which case $f^{-1}$ is monotone and one writes $P \cong Q$. An **antitone** map reverses the order: $x \leq y$ implies $f(y) \preceq f(x)$.

**Proposition.** A bijection $f : P \to Q$ is an order isomorphism if and only if both $f$ and $f^{-1}$ are monotone.

**Proof.** If $f$ is an order isomorphism and $f(x) \preceq f(y)$, the defining property of an embedding gives $x \leq y$, so $f$ is monotone; and $f^{-1}(u) \leq f^{-1}(v)$ whenever $u \preceq v$, because applying $f$ gives $u \preceq v$, so $f^{-1}$ is monotone. Conversely, if both are monotone and $f(x) \preceq f(y)$, monotonicity of $f^{-1}$ gives $x = f^{-1}(f(x)) \leq f^{-1}(f(y)) = y$. $\square$

The **duality principle** for orders states that every order-theoretic statement has a dual, obtained by reversing every inequality and interchanging least with greatest, upper with lower, and $\vee$ with $\wedge$. A statement is a theorem of order theory exactly when its dual is, because the reverse relation of a partial order is again a partial order. The principle halves the work throughout the article, and it is used without further remark.

### Suprema and Infima

**Definition.** Let $(P, \leq)$ be a poset and $S \subseteq P$. An **upper bound** of $S$ is a $u \in P$ with $s \leq u$ for all $s \in S$; a **least upper bound** (or **supremum**, or **join**) is an upper bound $u$ with $u \leq u'$ for every upper bound $u'$. Dually, a **lower bound** and the **greatest lower bound** (or **infimum**, or **meet**) are defined, and the supremum and infimum are written

$$
\bigvee S = \sup S, \qquad \bigwedge S = \inf S,
$$

with $x \vee y = \sup\{x, y\}$ and $x \wedge y = \inf\{x, y\}$ for a two-element set.

A supremum, when it exists, is unique by antisymmetry: two least upper bounds are each $\leq$ the other. Whether a given subset has a supremum depends on the poset and on the subset; the existence is a fact about $(P, \leq)$ and $S$, not a definitional matter.

**Example.** In $(\mathcal{P}(\mathbb{N}), \subseteq)$ the chain of finite subsets $\{0\} \subseteq \{0,1\} \subseteq \{0,1,2\} \subseteq \cdots$ has supremum $\mathbb{N}$, which is not one of them; and in $(\mathbb{N}, \leq)$ the whole set $\mathbb{N}$ has no supremum, since no element bounds it. In the divisibility poset of the positive integers the supremum of $\{m, n\}$ is the least common multiple and the infimum is the greatest common divisor.

**Definition.** A poset is **order-complete** if every subset has a supremum and an infimum; it is **conditionally complete** if every subset that is bounded above has a supremum and every subset bounded below has an infimum. A poset is a **chain-complete** poset if every chain has a supremum.

Order-completeness is an internal notion of the order and requires no distance; it is distinct from the metric completeness of Part II, which is a statement about a distance and its limits. The two are related for the order-complete field of the later category — its order-completeness and its metric completeness are logically connected — but the relation is a theorem of Part III, and no part of it is presupposed here.

## Lattices

### Definition and Examples

**Definition.** A **lattice** is a poset $(L, \leq)$ in which every pair of elements has a supremum and an infimum; one writes $x \vee y$ and $x \wedge y$ for them. A **sublattice** of $L$ is a subset closed under $\vee$ and $\wedge$, with the inherited order.

Thus a lattice is a poset with two binary operations, and the order is recoverable from either operation by

$$
x \leq y \iff x \vee y = y \iff x \wedge y = x.
$$

**Example.** The power set $\mathcal{P}(X)$ with $\subseteq$ is a lattice, with $A \vee B = A \cup B$ and $A \wedge B = A \cap B$. This is the lattice of subsets of the next-to-last section.

**Example.** Every total order is a lattice, with $x \vee y = \max(x,y)$ and $x \wedge y = \min(x,y)$. Thus $(\mathbb{N}, \leq)$ is a lattice, and so is any chain.

**Example.** The set of positive divisors of a fixed positive integer, ordered by divisibility, is a lattice with join the least common multiple and meet the greatest common divisor.

**Example.** The set of partitions of a set $X$, ordered by refinement, is a lattice: the meet of two partitions is the partition into the nonempty intersections of their blocks, and the join is obtained by the transitive closure of the relation "lies in a common block"; the lattice is isomorphic to that of the equivalence relations on $X$ under inclusion.

**Example.** The set of subgroups of a group, ordered by inclusion, is a lattice with join the generated subgroup and meet the intersection, and the set of normal subgroups is a sublattice of it. These examples are named for orientation and are treated, where the objects are introduced; no result about them is used here.

### The Algebraic Characterisation

The operations of a lattice satisfy identities dual to one another, and conversely a set with two such operations is a lattice; the proof is the standard one of Birkhoff.

**Theorem.** Let $L$ be a set with two binary operations $\vee, \wedge$ satisfying, for all $x, y, z$,

**L1 (idempotence)** $x \vee x = x$, $x \wedge x = x$;

**L2 (commutativity)** $x \vee y = y \vee x$, $x \wedge y = y \wedge x$;

**L3 (associativity)** $x \vee (y \vee z) = (x \vee y) \vee z$, $x \wedge (y \wedge z) = (x \wedge y) \wedge z$;

**L4 (absorption)** $x \vee (x \wedge y) = x$, $x \wedge (x \vee y) = x$.

Then the relation $x \leq y \iff x \vee y = y$ is a partial order under which $x \vee y$ and $x \wedge y$ are the supremum and infimum of $\{x, y\}$. Conversely, the operations of a lattice satisfy L1 to L4.

**Proof.** Reflexivity is idempotence. Antisymmetry: $x \vee y = y$ and $y \vee x = x$ give $x = y$ by commutativity. Transitivity: if $x \vee y = y$ and $y \vee z = z$, then $x \vee z = x \vee (y \vee z) = (x \vee y) \vee z = y \vee z = z$ by associativity. So $\leq$ is a partial order. To see that $x \vee y$ is the supremum: $x \vee (x \vee y) = (x \vee x) \vee y = x \vee y$ shows $x \leq x \vee y$, and $y \vee (x \vee y) = (y \vee x) \vee y = y \vee y = y$ shows $y \leq x \vee y$; if $x \leq u$ and $y \leq u$, then $(x \vee y) \vee u = x \vee (y \vee u) = x \vee u = u$, so $x \vee y \leq u$. The infimum is dual, using absorption to show $x \wedge y \leq x$. The converse is verified in any lattice from the properties of suprema and infima. $\square$

The theorem is the prototype of a recurring pattern in the corpus: a structure defined by a universal property or an order has an equivalent purely algebraic presentation by operations and identities, and one passes between the two without comment. The **duality** of lattices is now visible in the identity system, which is closed under interchanging $\vee$ with $\wedge$.

### Sublattices, Homomorphisms and Products

**Definition.** Let $L$ and $M$ be lattices. A **lattice homomorphism** is a map $h : L \to M$ with $h(x \vee y) = h(x) \vee h(y)$ and $h(x \wedge y) = h(x) \wedge h(y)$ for all $x, y$. A surjective lattice homomorphism is a **lattice quotient map**, and a bijective one is a **lattice isomorphism**.

Every lattice homomorphism is monotone, since $x \leq y$ implies $y = x \vee y$ and hence $h(y) = h(x) \vee h(y)$, that is $h(x) \leq h(y)$; the converse fails, and the order-embedding that is not a lattice homomorphism is the standard warning that the order and the operations carry different data.

**Definition.** The **product** of lattices $L$ and $M$ is the set $L \times M$ with the componentwise operations, $(x_1, y_1) \vee (x_2, y_2) = (x_1 \vee x_2, y_1 \vee y_2)$ and likewise for $\wedge$; the order is componentwise. The product is a lattice, and the projections are lattice homomorphisms.

### Complete Lattices

**Definition.** A **complete lattice** is a poset in which every subset has a supremum and an infimum. A **complete sublattice** is a subset closed under arbitrary suprema and infima taken in the ambient lattice.

Every complete lattice has a least element $\bigvee \emptyset$ and a greatest element $\bigwedge \emptyset$, written $0$ and $1$ when there is no risk of confusion; the empty supremum is the bottom and the empty infimum the top. A finite lattice is complete, since the supremum of a finite set is obtained by iterating the binary join.

**Theorem.** A poset $L$ is a complete lattice if and only if every subset has a supremum. Dually, it is complete if and only if every subset has an infimum.

**Proof.** Suppose every subset of $L$ has a supremum, and let $S \subseteq L$. The set $S^{\ell}$ of lower bounds of $S$ is nonempty, since it contains the least element $\bigvee \emptyset$ of $L$; let $m = \bigvee S^{\ell}$. Every $s \in S$ is an upper bound of $S^{\ell}$, so $m \leq s$, and $m$ is therefore a lower bound of $S$; and if $u$ is a lower bound of $S$ then $u \in S^{\ell}$, so $u \leq m$. Hence $m = \bigwedge S$. The infimum of the empty set is the supremum $\bigvee L$ of all of $L$, which exists by hypothesis, so every subset has an infimum. The dual argument reverses $\leq$. $\square$

**Example.** The power set $\mathcal{P}(X)$ is complete: the supremum of a family of subsets is its union and the infimum is its intersection, both of which are subsets of $X$. The lattice of partitions of a set is complete, but its *join* is not the union, which makes the completeness a genuine fact.

**Example.** $\mathcal{P}(X)$ is a complete lattice, while $\mathbb{N}$ with its usual order is not: it has no greatest element, and the subset $\mathbb{N}$ of itself has no supremum inside it. The finite subsets of $\mathbb{N}$ form a lattice that is not complete, since their supremum in $\mathcal{P}(\mathbb{N})$ is $\mathbb{N}$, which is not finite; completeness of a lattice is therefore not inherited by a sublattice.

**Definition.** A **directed supremum** is the supremum of a subset $D$ that is **directed**: every finite subset of $D$ has an upper bound in $D$. A lattice is **upward directed complete** (a **DCPO**) if every directed subset has a supremum; such orders are the domain of the least-fixed-point theory used in the semantics of recursion, and they are named here so that other articles can use the vocabulary.

### Distributive Lattices

**Definition.** A lattice $L$ is **distributive** if the two distributive laws hold for all $x, y, z$:

$$
x \wedge (y \vee z) = (x \wedge y) \vee (x \wedge z), \qquad x \vee (y \wedge z) = (x \vee y) \wedge (x \vee z).
$$

Either law implies the other in a lattice, so it is enough to verify one.

**Example.** The power-set lattice is distributive, with $\cap$ distributing over $\cup$ and conversely, by the theorem of *Sets, Functions and Relations*. Every chain is distributive, because in a chain each of the four elements $x, y, z$ is comparable and the two sides reduce to the median. The divisibility lattice of the positive integers is distributive: in that lattice the meet is the greatest common divisor and the join is the least common multiple, and the prime factorisations give $\gcd(m, \operatorname{lcm}(n,p)) = \operatorname{lcm}(\gcd(m,n), \gcd(m,p))$, which is the distributive law read in the lattice.

**Example.** The lattice $M_3$, the "diamond", has elements $0, 1, a, b, c$ with $a, b, c$ pairwise incomparable and $0 < a, b, c < 1$. It is not distributive: $a \wedge (b \vee c) = a \wedge 1 = a$, whereas $(a \wedge b) \vee (a \wedge c) = 0 \vee 0 = 0$.

### Modular Lattices

**Definition.** A lattice $L$ is **modular** if for all $x, y, z \in L$,

$$
x \leq z \implies x \vee (y \wedge z) = (x \vee y) \wedge z.
$$

Every distributive lattice is modular: expanding by distributivity gives $(x \vee y) \wedge z = (x \wedge z) \vee (y \wedge z) = x \vee (y \wedge z)$ when $x \leq z$. The converse fails, and $M_3$ is the standard witness, since it satisfies the modular law (any two of $a, b, c$ with $x \leq z$ reduce the identity to an identity in the diamond, as one checks) but not distributivity.

**Example.** The lattice $N_5$, the "pentagon", has elements $0 < a < c < 1$ and $b$ incomparable with $a, c$ but $0 < b < 1$. It is not modular: $a \leq c$ while $a \vee (b \wedge c) = a \vee 0 = a$ and $(a \vee b) \wedge c = 1 \wedge c = c$.

The two examples are canonical: a lattice is modular if and only if it has no sublattice isomorphic to $N_5$, and distributive if and only if it has no sublattice isomorphic to $N_5$ or $M_3$. This is the characterisation of Dedekind, and it is standard.

**Example.** The lattice of subgroups of a group is modular, and the lattice of normal subgroups is modular; the lattice of submodules of a module and the lattice of ideals of a commutative ring are modular but not distributive in general. These lattices are treated in the categories that introduce their objects —and— and they are named here as the principal applications of modularity, not used as results.

### Complemented Lattices and Boolean Lattices

**Definition.** A lattice $L$ with least element $0$ and greatest element $1$ is **complemented** if for every $x$ there is $y$ with $x \vee y = 1$ and $x \wedge y = 0$; such a $y$ is a **complement** of $x$. A lattice is a **Boolean lattice** (or **Boolean algebra**) if it is distributive and complemented.

In a distributive complemented lattice the complement is unique: if $y$ and $y'$ both complement $x$, then

$$
y = y \wedge 1 = y \wedge (x \vee y') = (y \wedge x) \vee (y \wedge y') = 0 \vee (y \wedge y') = y \wedge y',
$$

and symmetrically $y' = y \wedge y'$, so $y = y'$. The complement is then written $x^{\mathrm{c}}$ or $\neg x$.

**Example.** The power-set lattice $\mathcal{P}(X)$ is a Boolean lattice, with complement the relative complement in $X$ and with $0 = \emptyset$, $1 = X$. This is the first example of a Boolean algebra, introduced in *Sets, Functions and Relations* and studied as a subject in Part V. The finite Boolean algebras are exactly the power-set lattices of finite sets, and the representation of an arbitrary Boolean algebra is the Stone representation, which needs a topology and belongs to Part II.

## Galois Connections

### Definition and Basic Properties

**Definition.** Let $(P, \leq)$ and $(Q, \preceq)$ be posets. A **Galois connection** (or **adjunction** between posets) between them is a pair of monotone maps $f : P \to Q$ and $g : Q \to P$ such that, for all $p \in P$ and $q \in Q$,

$$
f(p) \preceq q \iff p \leq g(q).
$$

One says that $f$ is **left adjoint** to $g$ and writes $f \dashv g$; the identity characterising the connection is called the **adjunction identity**.

**Proposition.** Let $f \dashv g$ be a Galois connection.

1. $p \leq g(f(p))$ for all $p$, and $f(g(q)) \preceq q$ for all $q$.
2. $f = f g f$ and $g = g f g$.
3. If $f$ has a left inverse then $g(f(p)) = p$, and dually.
4. $f$ preserves all suprema that exist in $P$, and $g$ preserves all infima that exist in $Q$.

**Proof.** (1) Take $q = f(p)$ in the adjunction identity; then $f(p) \preceq f(p)$ holds, so $p \leq g(f(p))$. The second is the same with $p = g(q)$. (2) From $p \leq g(f(p))$ and monotonicity of $f$, $f(p) \preceq f(g(f(p)))$; from (1) applied to $q = f(p)$, $f(g(f(p))) \preceq f(p)$. Antisymmetry gives $f(p) = f(g(f(p)))$. The identity for $g$ is dual. (3) If $h \circ f = \mathrm{id}_P$, then $h(f(g(f(p)))) = g(f(p))$ because $h \circ f$ is the identity, while $f(g(f(p))) = f(p)$ by (2) and hence $h(f(g(f(p)))) = h(f(p)) = p$. So $p = g(f(p))$, and the reverse inequality is (1). (4) Let $S \subseteq P$ have supremum $s$. Since $f$ is monotone, $f(s)$ is an upper bound of $f(S)$. If $u$ is any upper bound of $f(S)$, then for each $t \in S$ one has $f(t) \preceq u$, hence $t \leq g(u)$; so $g(u)$ is an upper bound of $S$ and $s \leq g(u)$, whence $f(s) \preceq u$. Thus $f(s)$ is the least upper bound of $f(S)$. The statement for $g$ is dual. $\square$

### The Galois Connection Induced by a Relation

The standard source of Galois connections is a relation between two sets, and it is the one used by the polarity and closure constructions of the corpus.

**Definition.** Let $R \subseteq X \times Y$ be a relation. For $A \subseteq X$ and $B \subseteq Y$ put

$$
A^{\uparrow} = \{y \in Y : x \mathrel{R} y \text{ for every } x \in A\}, \qquad B^{\downarrow} = \{x \in X : x \mathrel{R} y \text{ for every } y \in B\}.
$$

Both maps reverse inclusions, so they are antitone, and the pair $(\uparrow, \downarrow)$ is a Galois connection between $(\mathcal{P}(X), \subseteq^{\mathrm{op}})$ and $(\mathcal{P}(Y), \subseteq^{\mathrm{op}})$; equivalently, the induced maps $A \mapsto A^{\uparrow\downarrow}$ and $B \mapsto B^{\downarrow\uparrow}$ are closure operators.

**Proposition.** For all $A \subseteq X$ and $B \subseteq Y$ one has $A \subseteq A^{\uparrow\downarrow}$ and $B \subseteq B^{\downarrow\uparrow}$, and the maps $A \mapsto A^{\uparrow\downarrow}$ and $B \mapsto B^{\downarrow\uparrow}$ are idempotent and monotone; moreover $A \subseteq B^{\downarrow}$ if and only if $B \subseteq A^{\uparrow}$.

**Proof.** If $x \in A$ and $y \in A^{\uparrow}$, then $x \mathrel{R} y$ by the definition of $A^{\uparrow}$, so $x \in A^{\uparrow\downarrow}$. This gives the first inclusion, and the second is symmetric. Idempotence and monotonicity follow from the general properties of a Galois connection, or directly by the same elementwise argument. The final equivalence is the adjunction identity, since $A \subseteq B^{\downarrow}$ says that every $x \in A$ satisfies $x \mathrel{R} y$ for every $y \in B$. $\square$

### Closure Operators

**Definition.** A **closure operator** on a poset $P$ is a monotone map $c : P \to P$ that is **increasing** ($x \leq c(x)$) and **idempotent** ($c(c(x)) = c(x)$). An element with $c(x) = x$ is **closed**.

By the propositions above, a Galois connection $f \dashv g$ yields closure operators $g f$ on $P$ and $f g$ on $Q$, and every closure operator that preserves meets arises in this way from the map to its closed elements. The closed elements of a closure operator on a complete lattice form a complete lattice under the inherited order: their infimum is the infimum in the ambient lattice, which is again closed, and their supremum is the closure of the ambient supremum. This is the order-theoretic form of the statement that a closed subset system is itself complete, and it recurs in every category of the corpus.

**Example.** The map $S \mapsto \overline{S}$ of topological closure is increasing, monotone and idempotent, and the closed sets form a complete lattice; the statement is deferred to Part II, where the topology exists. The order-theoretic content is already visible here: a closure operator determines its closed elements, and those form a complete lattice.

## The Knaster–Tarski Theorem

### Fixed Points of Monotone Maps

**Definition.** Let $L$ be a lattice and $f : L \to L$. A **fixed point** of $f$ is an $x$ with $f(x) = x$. The **least fixed point** is the least such $x$, written $\mu f$, and the **greatest fixed point** is the greatest, written $\nu f$.

The fixed points of a monotone map of a complete lattice are themselves a complete lattice; this is the content of the theorem, and it is the reason a recursive definition has a canonical solution.

**Theorem (Knaster–Tarski).** Let $L$ be a complete lattice and let $f : L \to L$ be monotone. Then the set $\operatorname{Fix}(f)$ of fixed points of $f$, with the order inherited from $L$, is a complete lattice. In particular

$$
\mu f = \bigwedge \{x \in L : f(x) \leq x\}, \qquad \nu f = \bigvee \{x \in L : x \leq f(x)\},
$$

are the least and greatest fixed points of $f$.

**Proof.** Put $A = \{x \in L : f(x) \leq x\}$ and $a = \bigwedge A$; the set $A$ is nonempty, since the greatest element $1$ of $L$ satisfies $f(1) \leq 1$. For each $x \in A$ one has $a \leq x$, so by monotonicity $f(a) \leq f(x) \leq x$; hence $f(a)$ is a lower bound of $A$ and $f(a) \leq a$. Applying $f$ to this inequality and using monotonicity gives $f(f(a)) \leq f(a)$, so $f(a) \in A$; then $a \leq f(a)$ because $a$ is a lower bound of $A$. Antisymmetry gives $f(a) = a$, so $a$ is a fixed point, and it is the least because every fixed point lies in $A$. The greatest fixed point is obtained by the dual argument applied to the set $\{x : x \leq f(x)\}$ and its supremum, or equivalently by applying the argument just given to the same map on the lattice with the reverse order.

It remains to record why $\operatorname{Fix}(f)$ is a complete lattice, not merely a set with a least and a greatest element. The set is nonempty, since $f(0) \geq 0$ forces $f(0) = 0$ and dually $f(1) = 1$. For a nonempty $S \subseteq \operatorname{Fix}(f)$ the ambient infimum $a = \bigwedge S$ satisfies $f(a) \leq a$, and the iterates $a \geq f(a) \geq f(f(a)) \geq \cdots$ descend from $a$; the greatest fixed point below every member of $S$ is obtained by continuing the descent along the ordinals until it stabilises, and that construction — the standard proof of the completeness half of the theorem — is the transfinite recursion treated. Granting it, $\operatorname{Fix}(f)$ has arbitrary infima and is therefore a complete lattice by the theorem above. $\square$

**Corollary.** Every monotone map of a complete lattice has a least and a greatest fixed point, and every monotone map of a finite lattice has a least and a greatest fixed point.

The theorem is due to Knaster and Tarski; the finite case is the fixed-point theorem behind inductive definitions. It is constructive, producing the fixed point by a single application of $\bigwedge$ and using no choice, which distinguishes it from Zorn's lemma, whose maximal element is asserted and needs the axiom of choice. The two are often used in tandem.

**Example.** On the power set $\mathcal{P}(X)$ ordered by inclusion, a monotone map $F : \mathcal{P}(X) \to \mathcal{P}(X)$ has least fixed point $\mu F = \bigcap \{S : F(S) \subseteq S\}$ and greatest fixed point $\nu F = \bigcup \{S : S \subseteq F(S)\}$. Applied to the operator of an inductively defined set — the closure under a family of constructors — the least fixed point is the set generated by the constructors, which is the order-theoretic content of inductive definition in *Logic and Proof*. For a closure operator $c$ on a complete lattice the two formulas give $\mu c = c(0)$ and $\nu c = 1$, since the fixed points are the closed elements. The instance in topology is deferred to Part II.

## The Lattice of Subsets

### The Power-Set Lattice

The power set of a set, ordered by inclusion, is simultaneously the most important example and the universal one; its lattice properties were computed in *Sets, Functions and Relations* and are collected here. It is complete, distributive and complemented, hence a Boolean lattice, and every finite Boolean lattice is isomorphic to the power set of the set of its atoms: the atoms are the singletons, every element is the join of the atoms below it, and the assignment of that set of atoms is a lattice isomorphism.

### Subset Lattices and the Boolean Case

A **lattice of sets** is a family $\mathcal{L} \subseteq \mathcal{P}(X)$ closed under the unions and intersections that it contains; the concept is used throughout the corpus, where representation theorems identify an abstract lattice with a lattice of sets. The distributive lattices are exactly the sublattices of power-set lattices, by the representation theorem of Birkhoff, and the finite case is the statement above. The general representation of a Boolean algebra as an algebra of subsets requires a topology, and it is the Stone representation theorem of Part II; the Boolean algebra as an abstract structure is the subject of Part V.

**Remark.** The chain of inclusions

$$
\text{lattices} \;\supset\; \text{modular lattices} \;\supset\; \text{distributive lattices} \;\supset\; \text{Boolean lattices}
$$

is strict, with witnesses $N_5$ for the first inclusion, $M_3$ for the second, and a three-element chain for the third, that chain being distributive and bounded but not complemented. Each class is closed under the formation of products, the first three are closed under sublattices, and in the Boolean case one requires in addition closure under complement and under $0$ and $1$. The characterising forbidden sublattices are $N_5$ for modularity and $N_5, M_3$ for distributivity.

## Summary

A partial order is a reflexive, antisymmetric, transitive relation; a total order compares every pair, and a well-order is a total order in which every nonempty subset has a least element, whence there is no infinite strictly descending sequence, the converse deduction requiring a choice principle. A poset is complete when every subset has a supremum and an infimum; the supremum and infimum of a subset, when they exist, are unique.

A lattice is a poset in which every pair has a supremum and an infimum, and equivalently a set with two binary operations satisfying idempotence, commutativity, associativity and absorption; a lattice is complete when these operations are defined for arbitrary subsets, and finite lattices are complete. Distributive lattices satisfy the distributive laws, modular lattices the modular law, and Boolean lattices are the distributive complemented ones, in which the complement is unique; the power-set lattice is the standard example. The sublattice characterisations — no $N_5$ for modular, no $N_5$ or $M_3$ for distributive — are Dedekind's.

A Galois connection between posets is a pair of monotone adjoint maps $f \dashv g$ with $f(p) \preceq q \iff p \leq g(q)$; it induces closure operators $gf$ and $fg$, the left adjoint preserves suprema and the right adjoint infima, and the closed elements of a closure operator on a complete lattice form a complete lattice. The Knaster–Tarski theorem states that a monotone map of a complete lattice has a least fixed point $\bigwedge\{x: f(x) \leq x\}$ and a greatest fixed point $\bigvee\{x: x \leq f(x)\}$, and that the fixed points form a complete lattice; the construction uses no choice principle, which is why it is used for inductive definitions while Zorn's lemma, treated, is used for maximal objects.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\leq$, $<$ | Partial order and its strict part |
| $(P, \leq)$ | Partially ordered set (poset) |
| $\bigvee S = \sup S$, $\bigwedge S = \inf S$ | Supremum and infimum of a subset |
| $x \vee y$, $x \wedge y$ | Join (least upper bound) and meet (greatest lower bound) of a pair |
| $L$, $M$ | Lattices |
| $0$, $1$ | Least and greatest elements of a bounded lattice; $\bigvee\emptyset$, $\bigwedge\emptyset$ |
| $x^{\mathrm{c}}$ | Complement of $x$ in a complemented lattice |
| $N_5$, $M_3$ | Pentagons and diamond; forbidden sublattices for modularity and distributivity |
| $f \dashv g$ | Galois connection (adjunction): $f(p) \preceq q \iff p \leq g(q)$ |
| $A^{\uparrow}$, $B^{\downarrow}$ | Polar maps of a relation $R \subseteq X \times Y$ |
| $c : P \to P$ | Closure operator: monotone, increasing, idempotent |
| $\operatorname{Fix}(f)$ | Set of fixed points of $f$ |
| $\mu f$, $\nu f$ | Least and greatest fixed points of $f$ |
| $\mathcal{P}(X)$ | Power-set lattice, complete, distributive and complemented |
| DCPO | Poset in which every directed subset has a supremum |





## Further Reading

- Garrett Birkhoff, *Lattice Theory*, 3rd ed. (American Mathematical Society, 1967), for the classical development of lattices, modularity, distributivity and representation theorems.
- George Grätzer, *Lattice Theory: Foundation* (Birkhäuser, 2011), for a comprehensive modern account of the algebraic and order-theoretic theory of lattices.
- Steven Roman, *Lattices and Ordered Sets* (Springer, 2008), for an introduction that develops the algebraic characterisation, Galois connections and fixed-point theorems.
- Rudolf Wille, "Restructuring lattice theory: an approach based on hierarchies of concepts", in *Ordered Sets* (Reidel, 1982), for Galois connections and their role in concept analysis.
- Alfred Tarski, "A lattice-theoretical fixpoint theorem and its applications", *Pacific Journal of Mathematics* **5** (1955), 285–309, for the Knaster–Tarski fixed-point theorem in the form used here.
- Bronisław Knaster, "Un théorème sur les fonctions d'ensembles", *Annales de la Société Polonaise de Mathématique* **6** (1928), 133–134, for the original fixed-point result.
- Brian A. Davey and Hilary A. Priestley, *Introduction to Lattices and Order*, 2nd ed. (Cambridge University Press, 2002), for Galois connections, closure operators and the representation of distributive lattices.
