
# __Sets, Functions and Relations__

## Introduction

This article fixes the language in which the rest of the corpus is written. A set is a collection of objects, membership is the one primitive relation, and everything algebraic that follows — a group, a ring, a module, an algebra — is a set equipped with further structure. The three notions of the title are therefore not a preliminary to algebra but the alphabet of it: a group law is a function $G \times G \to G$, a subgroup is a subset closed under that function, an action is a function $G \times X \to X$, and a quotient is a set of equivalence classes. The article develops these notions concretely and proves the elementary propositions that other articles use without comment.

The treatment is deliberately naive about the foundations. The operations on sets are written down, the laws they satisfy are proved, and the axiom system that justifies them — the Zermelo–Fraenkel axioms with the axiom of choice, the cumulative hierarchy and the notion of an ordinal — is assumed as the ambient set theory and is not developed here. The theory of cardinality, including the countability of $\mathbb{N} \times \mathbb{N}$ and the uncountability of the power set of $\mathbb{N}$ and the arithmetic of infinite cardinals, belongs; the systematic theory of order, including lattices, completeness and the Knaster–Tarski theorem, belongs; and the propositional and predicate calculus, with the rules of inference and the structure of a formal pro, belongs. This article introduces only so much order and so much logic as the language of sets requires, and defers the rest.

One forward reference deserves to be stated at the outset, because it recurs throughout the corpus. The operations on subsets — union, intersection and complement — satisfy the same laws as the logical connectives of propositional logic, and the resulting structure is the first example of a **Boolean algebra**. That structure is developed as a subject in Part V, in the synthetic study of the Booleans, and the parallel with the algebra of propositions is drawn. Nothing in the present article depends on either.

## Sets and Membership

### Sets, Membership and Extensionality

A **set** is a collection of objects, its **elements**. One writes $x \in X$ for "$x$ is an element of $X$" and $x \notin X$ for its negation. Two sets are equal when they have the same elements: this is the **axiom of extensionality**,

$$
X = Y \quad \text{if and only if} \quad (z \in X \iff z \in Y) \ \text{for every } z.
$$

Extensionality is the principle that a set is determined by its members and by nothing else. It is the reason that two descriptions of the same collection describe the same set, and it is the tool with which every identity below is proved: to show that two sets are equal one shows that each element of one lies in the other.

The **empty set** $\emptyset$ is the set with no elements. Extensionality makes it unique: if $\emptyset'$ also had no elements, then no $z$ lies in one and not the other, so $\emptyset = \emptyset'$. A set is **nonempty** if it has at least one element, written $X \neq \emptyset$.

Membership is a relation between objects and sets, and it is not symmetric or transitive in general: $x \in X$ and $X \in Y$ do not imply $x \in Y$, and indeed the set-theoretic paradoxes show that not every property defines a set. The corpus avoids the paradoxes by never forming "the set of all sets with property $P$" without restriction; the restricted comprehension and replacement axioms that legitimate the constructions used here are the standard Zermelo–Fraenkel axioms, assumed as the ambient set theory and not developed here. The constructions below — pairing, union, power set, separation, replacement — are the ones the corpus uses, each licensed by the corresponding axiom of that ambient theory.

### Subsets

**Definition.** Let $A$ and $B$ be sets. Then $A$ is a **subset** of $B$, written $A \subseteq B$, if every element of $A$ is an element of $B$. If $A \subseteq B$ and $A \neq B$, then $A$ is a **proper subset** of $B$, written $A \subsetneq B$.

**Proposition.** The relation $\subseteq$ is reflexive, antisymmetric and transitive: $A \subseteq A$; if $A \subseteq B$ and $B \subseteq A$ then $A = B$; and if $A \subseteq B$ and $B \subseteq C$ then $A \subseteq C$.

**Proof.** Reflexivity and transitivity are immediate from the definition, since a condition true of every element of $A$ is true of every element of $A$, and a condition true of every element of $A$ and of every element of $B \supseteq A$ is true of every element of $A$. Antisymmetry is extensionality: $A \subseteq B$ and $B \subseteq A$ say exactly that $z \in A \iff z \in B$ for all $z$. $\square$

A relation that is reflexive, antisymmetric and transitive is a **partial order**; the subset relation is the model on which the general theory is built. The symbol $\subseteq$ is the order, and $A \subsetneq B$ is its strict part.

Given a set $X$ and a property $P$, the **separation** (or comprehension) principle lets one form the subset

$$
\{x \in X : P(x)\},
$$

and it is the only way in which subsets are formed in the corpus. In particular the **intersection** of $A$ and $B$ is $A \cap B = \{x \in A : x \in B\}$, and the **difference** is $A \setminus B = \{x \in A : x \notin B\}$.

### The Algebra of Subsets

Fix a set $X$, the **universe** of the discussion, and let $A, B, C \subseteq X$. The following operations are defined on the subsets of $X$.

**Definition.** The **union**, **intersection**, **complement** and **symmetric difference** are

$$
A \cup B = \{x \in X : x \in A \ \text{or} \ x \in B\}, \qquad A \cap B = \{x \in X : x \in A \ \text{and} \ x \in B\},
$$

$$
A^{\mathrm{c}} = \{x \in X : x \notin A\}, \qquad A \mathbin{\triangle} B = (A \setminus B) \cup (B \setminus A).
$$

The union and intersection of a family $(A_i)_{i \in I}$ of subsets of $X$ are

$$
\bigcup_{i \in I} A_i = \{x \in X : x \in A_i \ \text{for some } i \in I\}, \qquad \bigcap_{i \in I} A_i = \{x \in X : x \in A_i \ \text{for every } i \in I\}.
$$

For $I = \emptyset$ the union is $\emptyset$ and the intersection is $X$, by the convention on an empty disjunction and conjunction.

**Theorem.** For all $A, B, C \subseteq X$ the following laws hold.

1. **Idempotence.** $A \cup A = A$, $A \cap A = A$.
2. **Commutativity.** $A \cup B = B \cup A$, $A \cap B = B \cap A$.
3. **Associativity.** $(A \cup B) \cup C = A \cup (B \cup C)$, and likewise for $\cap$.
4. **Distributivity.** $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$ and $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$.
5. **Absorption.** $A \cup (A \cap B) = A$ and $A \cap (A \cup B) = A$.
6. **Identity.** $A \cup \emptyset = A$ and $A \cap X = A$.
7. **Complement.** $A \cup A^{\mathrm{c}} = X$ and $A \cap A^{\mathrm{c}} = \emptyset$.
8. **Double complement.** $(A^{\mathrm{c}})^{\mathrm{c}} = A$.
9. **De Morgan.** $(A \cup B)^{\mathrm{c}} = A^{\mathrm{c}} \cap B^{\mathrm{c}}$ and $(A \cap B)^{\mathrm{c}} = A^{\mathrm{c}} \cup B^{\mathrm{c}}$.

**Proof.** Each identity is proved by extensionality. For the first De Morgan law, an element $x$ lies in $(A \cup B)^{\mathrm{c}}$ exactly when it is not in $A \cup B$, that is, when it is in neither $A$ nor $B$; and $x \in A^{\mathrm{c}} \cap B^{\mathrm{c}}$ exactly when it is not in $A$ and not in $B$. The two conditions are the same. The second law is the first applied to the complements, or is proved in the same way. The first distributivity law: $x \in A \cap (B \cup C)$ when $x \in A$ and ($x \in B$ or $x \in C$), that is, when ($x \in A$ and $x \in B$) or ($x \in A$ and $x \in C$), that is, when $x \in (A \cap B) \cup (A \cap C)$. The remaining laws follow from the definitions in the same way, and the infinite distributive laws

$$
A \cap \bigcup_i B_i = \bigcup_i (A \cap B_i), \qquad A \cup \bigcap_i B_i = \bigcap_i (A \cup B_i)
$$

are proved by the same elementwise argument with a quantifier in place of a finite disjunction. $\square$

The laws listed are exactly the axioms of a **Boolean algebra**, with $\cup$, $\cap$, ${}^{\mathrm{c}}$, $\emptyset$ and $X$ playing the roles of sum, product, complement, zero and unit; the algebra of subsets and the algebra of propositions are the same set of laws read in two vocabularies.

**Remark (duality).** Every law in the list remains true when $\cup$ is interchanged with $\cap$ and $\emptyset$ with $X$. This **duality principle** reflects the symmetry of the defining laws and halves the work of verifying them; the complement is the operation that turns one half of the list into the other, since De Morgan's laws say that complement converts unions into intersections.

### The Power Set

**Definition.** The **power set** of $X$, written $\mathcal{P}(X)$, is the set of all subsets of $X$:

$$
\mathcal{P}(X) = \{A : A \subseteq X\}.
$$

The power set is a set by the power-set axiom of the ambient set theory.

**Proposition.** The power set $\mathcal{P}(X)$, ordered by $\subseteq$, has $\emptyset$ as least element and $X$ as greatest element; the union $A \cup B$ is the least subset of $X$ containing both $A$ and $B$, and the intersection $A \cap B$ is the greatest subset contained in both.

**Proof.** That $\emptyset \subseteq A \subseteq X$ for every $A \subseteq X$ is immediate. If $C \supseteq A$ and $C \supseteq B$, then $C$ contains every element of $A$ and of $B$, hence $C \supseteq A \cup B$; and $A \cup B$ itself contains both, so it is least. Dually, $A \cap B$ is contained in both and contains every set contained in both. $\square$

Thus $\mathcal{P}(X)$ carries a **lattice** structure — a partial order in which every pair has a least upper bound and a greatest lower bound — and the lattice is distributive and complemented, the first example of both a lattice and a Boolean algebra; the general theory is. The cardinality of $\mathcal{P}(X)$ is treated.

## Ordered Pairs and Products

### Ordered Pairs

Membership alone cannot distinguish the two elements of a two-element set: $\{a, b\} = \{b, a\}$. An **ordered pair** must record which coordinate is first, and it is defined by a set-theoretic trick due to Kuratowski.

**Definition.** For objects $a$ and $b$, the **ordered pair** is

$$
(a, b) = \{\{a\}, \{a, b\}\}.
$$

**Theorem.** For all $a, b, c, d$ one has $(a, b) = (c, d)$ if and only if $a = c$ and $b = d$.

**Proof.** If $a = c$ and $b = d$ the two pairs are equal by construction. Conversely suppose $\{\{a\},\{a,b\}\} = \{\{c\},\{c,d\}\}$. Every element of the left side is an element of the right, and conversely. The set $\{a\}$ is an element of the left side, so it equals $\{c\}$ or $\{c,d\}$. In the first case $a = c$; in the second case $a = c = d$, so again $a = c$. Since $\{a\} = \{c\}$ holds in either case, the two-element member of each side must also agree: $\{a, b\} = \{c, d\}$. Now $b$ lies in $\{a,b\}$, hence in $\{c,d\}$, so $b = c$ or $b = d$; if $b = c$ then $b = c = a$, and $\{c,d\}$ contains $d$, which must equal $a$ or $b$, so $d = b$; otherwise $b = d$ directly. Hence $a = c$ and $b = d$. $\square$

The definition is a coding whose only purpose is to reduce the ordered pair to a set that already exists; once the theorem is proved the coding is never used again, and the pair is treated as an object with two projections.

### The Cartesian Product

**Definition.** The **Cartesian product** of sets $X$ and $Y$ is

$$
X \times Y = \{(x, y) : x \in X, \ y \in Y\}.
$$

Its elements are **ordered pairs**; by the theorem, $(x, y) = (x', y')$ exactly when $x = x'$ and $y = y'$. The product is a set by the axioms of pairing, union and separation.

The product of a finite list $X_1, \ldots, X_n$ is defined recursively, $X_1 \times \cdots \times X_n = (X_1 \times \cdots \times X_{n-1}) \times X_n$, with elements the $n$-tuples $(x_1, \ldots, x_n)$. Two $n$-tuples are equal exactly when their entries agree coordinatewise.

**Example.** $\mathbb{N} \times \mathbb{N}$ is the set of ordered pairs of natural numbers; $\{0,1\} \times \{0,1\}$ has the four elements $(0,0), (0,1), (1,0), (1,1)$.

**Example.** The product is not commutative as a set when $X \neq Y$: $X \times Y$ and $Y \times X$ have different elements, though they are in bijection by $(x, y) \mapsto (y, x)$.

**Proposition.** For sets $X, Y, Z$ one has

$$
X \times (Y \cup Z) = (X \times Y) \cup (X \times Z), \qquad X \times (Y \cap Z) = (X \times Y) \cap (X \times Z).
$$

**Proof.** An element of the left side of the first identity is a pair $(x, w)$ with $x \in X$ and $w \in Y \cup Z$, so either $w \in Y$ or $w \in Z$; hence the pair lies in $X \times Y$ or in $X \times Z$. The converse is the reverse reading. The second identity is the same argument with "and" in place of "or". $\square$

### Families and Indexed Sets

A **family** is a function whose values are being regarded as a collection. Formally, an **indexed family** of sets $(A_i)_{i \in I}$ is a function $A$ with domain the index set $I$, and $A_i$ is the value at $i$. The index is a label, not a quantity: the same set may occur at several indices, which is the only difference between a family and a subset of some ambient collection.

**Definition.** The **Cartesian product** of a family $(A_i)_{i \in I}$ is

$$
\prod_{i \in I} A_i = \Big\{ f : I \to \bigcup_{i \in I} A_i \ : \ f(i) \in A_i \ \text{for every } i \in I \Big\},
$$

the set of choice functions selecting one element from each $A_i$.

For a finite index set this agrees with the recursive product above: a function on $\{1, \ldots, n\}$ is a tuple. For an infinite index set it is the general notion, and it is the object to which the axiom of choice is addressed: the assertion that $\prod_i A_i$ is nonempty whenever every $A_i$ is nonempty *is* the axiom of choice, and its equivalence with Zorn's lemma and the well-ordering theorem is treated. The **disjoint union** of the family is

$$
\bigsqcup_{i \in I} A_i = \bigcup_{i \in I} (\{i\} \times A_i),
$$

which attaches the index to each element and so keeps the pieces apart even when the sets $A_i$ overlap.

## Relations

### Relations on a Set

**Definition.** A **relation** from $X$ to $Y$ is a subset $R \subseteq X \times Y$. For $(x, y) \in R$ one writes $x \mathrel{R} y$. A relation **on** $X$ is a subset $R \subseteq X \times X$.

The **inverse** of $R \subseteq X \times Y$ is $R^{-1} = \{(y, x) : (x, y) \in R\} \subseteq Y \times X$, and the **composite** of $R \subseteq X \times Y$ with $S \subseteq Y \times Z$ is

$$
S \circ R = \{(x, z) : \text{there exists } y \in Y \text{ with } x \mathrel{R} y \text{ and } y \mathrel{S} z\}.
$$

Composition of relations is associative, $(T \circ S) \circ R = T \circ (S \circ R)$, by the associativity of the existential quantifier, and the identity relation $\Delta_X = \{(x,x) : x \in X\}$ is a two-sided identity.

A relation $R$ on $X$ is **reflexive** if $x \mathrel{R} x$ for all $x \in X$; **irreflexive** if $x \mathrel{R} x$ for no $x$; **symmetric** if $x \mathrel{R} y$ implies $y \mathrel{R} x$; **antisymmetric** if $x \mathrel{R} y$ and $y \mathrel{R} x$ imply $x = y$; and **transitive** if $x \mathrel{R} y$ and $y \mathrel{R} z$ imply $x \mathrel{R} z$. A relation that is reflexive and transitive is a **preorder**, and the preorders on $X$ correspond to the *quotients* of $X$ by equivalence relations equipped with an order, a fact used below.

### Equivalence Relations

**Definition.** An **equivalence relation** on a set $X$ is a relation $\sim$ that is reflexive, symmetric and transitive. For $x \in X$ its **equivalence class** is

$$
[x] = \{y \in X : y \sim x\}.
$$

**Lemma.** If $\sim$ is an equivalence relation on $X$ then $x \sim y$ if and only if $[x] = [y]$.

**Proof.** If $[x] = [y]$ then $x \in [x] = [y]$, so $x \sim y$. Conversely if $x \sim y$ and $z \in [x]$, then $z \sim x$ and $x \sim y$, so $z \sim y$ by transitivity, and $z \in [y]$; thus $[x] \subseteq [y]$, and symmetry gives the reverse inclusion. $\square$

**Proposition.** The equivalence classes of a relation $\sim$ on $X$ are nonempty, pairwise disjoint, and their union is $X$.

**Proof.** Each class is nonempty because $x \in [x]$ by reflexivity. If $[x] \cap [y] \neq \emptyset$, choose $z$ in the intersection; then $z \sim x$ and $z \sim y$, so by symmetry and transitivity $x \sim y$, and the lemma gives $[x] = [y]$. If $[x] \neq [y]$ the classes are therefore disjoint. Finally every $x$ lies in $[x]$, so the union of all classes is $X$. $\square$

The set of equivalence classes is the **quotient** of $X$ by $\sim$, written

$$
X / {\sim} = \{[x] : x \in X\},
$$

and the **quotient map** $\pi : X \to X/{\sim}$, $\pi(x) = [x]$, is surjective. In other articles the quotient of a group by a normal subgroup, of a ring by an ideal, and of a module by a submodule are all quotients of this form, and the universal property of a quotient — that a function on $X$ which is constant on classes factors uniquely through $\pi$ — is the same statement in each case.

### Partitions

**Definition.** A **partition** of a set $X$ is a family $\mathcal{P}$ of nonempty subsets of $X$ that are pairwise disjoint and whose union is $X$.

The proposition above says that the equivalence classes of any equivalence relation form a partition. The converse is also true, and it gives a complete dictionary between the two notions.

**Theorem.** Let $X$ be a set. The map sending an equivalence relation to the set of its classes is a bijection between the equivalence relations on $X$ and the partitions of $X$.

**Proof.** Injectivity: if two equivalence relations have the same classes then $x \sim y$ holds for the first exactly when $x$ lies in the same class as $y$, which is the same condition for the second. Surjectivity: given a partition $\mathcal{P}$, define $x \sim y$ to mean that $x$ and $y$ lie in a common member of $\mathcal{P}$. This is reflexive and symmetric immediately, and transitive because two members of $\mathcal{P}$ that meet a common element coincide, a partition being pairwise disjoint. Its classes are exactly the members of $\mathcal{P}$. $\square$

The theorem gives two ways of presenting a quotient, by the relation or by the partition; in group theory the partition is into the cosets of a normal subgroup, in ring theory into the cosets of an ideal.

### Order Relations

**Definition.** A **partial order** on a set $X$ is a relation $\leq$ that is reflexive, antisymmetric and transitive. A **total order** (or **linear order**) is a partial order in which any two elements are comparable, that is, $x \leq y$ or $y \leq x$ for all $x, y \in X$. A **strict partial order** is an irreflexive transitive relation, written $<$.

The subset relation $\subseteq$ on $\mathcal{P}(X)$ is a partial order that is not total as soon as $X$ has two elements: $\{a\}$ and $\{b\}$ are incomparable. The usual order on $\mathbb{N}$ is total. Every partial order gives rise to a strict order by $x < y \iff x \leq y$ and $x \neq y$, and every strict order to a partial order by $x \leq y \iff x < y$ or $x = y$; the two notions carry the same information.

An element $m \in X$ is **maximal** if $m \leq x$ implies $x = m$, and **maximum** (or greatest) if $x \leq m$ for all $x$; the two differ when the order is partial, since a maximum is unique but maxima need not exist. A total order in which every nonempty subset has a least element is a **well-order**, the object on which transfinite induction is performed. The systematic theory of orders is the subject, and Zorn's lemma is treated with the axiom of choice.

## Functions

### Functions as a Special Kind of Relation

**Definition.** A **function** from $X$ to $Y$ is a relation $f \subseteq X \times Y$ such that for every $x \in X$ there is exactly one $y \in Y$ with $(x, y) \in f$. One writes $f : X \to Y$ and $f(x) = y$ for that unique $y$.

Thus a function is a relation with a uniqueness and an existence condition. The **graph** of a function is the relation $f$ itself; the notation $x \mapsto f(x)$ records the rule. The set $X$ is the **domain** and $Y$ the **codomain**; the **image** is

$$
\operatorname{im} f = f(X) = \{f(x) : x \in X\} \subseteq Y.
$$

Two functions are equal when they have the same domain, the same codomain and the same values; alternatively, when their graphs are equal as sets. The **identity function** on $X$ is $\mathrm{id}_X : X \to X$, $\mathrm{id}_X(x) = x$, whose graph is the diagonal $\Delta_X$. The set of all functions from $X$ to $Y$ is written $Y^X$.

**Example.** The quotient map $\pi : X \to X/{\sim}$ is a function because each $x$ has exactly one class. The relation $\{(x, y) : x^2 + y^2 = 1\}$ is not a function, since it assigns two values to most $x$, whereas $\{(x, y) : y = x^2\}$ is one.

### Composition

**Definition.** Let $f : X \to Y$ and $g : Y \to Z$. The **composite** $g \circ f : X \to Z$ is defined by $(g \circ f)(x) = g(f(x))$.

**Proposition.** Composition is associative: $h \circ (g \circ f) = (h \circ g) \circ f$ whenever the composites are defined. The identity functions are two-sided identities: $f \circ \mathrm{id}_X = f = \mathrm{id}_Y \circ f$.

**Proof.** For each $x$, both sides of the associativity identity evaluate to $h(g(f(x)))$, so the two functions agree at every point. The identities are immediate from the definitions. $\square$

Associativity makes the set of functions $X \to X$ under composition a monoid, whose invertible elements are the symmetric group $\operatorname{Sym}(X)$. Composition is not commutative in general: on $X = \{1,2\}$ the transposition and the constant map do not commute.

### Injective, Surjective and Bijective Functions

**Definition.** A function $f : X \to Y$ is **injective** (one-to-one) if $f(x) = f(x')$ implies $x = x'$; **surjective** (onto) if for every $y \in Y$ there is $x \in X$ with $f(x) = y$; and **bijective** if it is both injective and surjective.

Injectivity says that distinct inputs have distinct outputs, surjectivity that the image is the whole codomain, and bijectivity that $f$ matches the elements of $X$ with those of $Y$ exactly.

**Proposition.** Let $f : X \to Y$ and $g : Y \to Z$.

1. If $f$ and $g$ are injective then $g \circ f$ is injective; if $g \circ f$ is injective then $f$ is injective.
2. If $f$ and $g$ are surjective then $g \circ f$ is surjective; if $g \circ f$ is surjective then $g$ is surjective.
3. If $f$ and $g$ are bijective then $g \circ f$ is bijective.

**Proof.** (1) If $(g \circ f)(x) = (g \circ f)(x')$ then $g(f(x)) = g(f(x'))$, so $f(x) = f(x')$ by injectivity of $g$ and then $x = x'$ by injectivity of $f$. If $g \circ f$ is injective and $f(x) = f(x')$, then $(g \circ f)(x) = (g \circ f)(x')$, so $x = x'$. (2) If $z \in Z$, surjectivity of $g \circ f$ gives $x$ with $g(f(x)) = z$, so $z$ is the image under $g$ of $f(x)$. If $g \circ f$ is surjective and $z \in Z$, choose $x$ with $(g \circ f)(x) = z$; then $z = g(f(x))$ lies in the image of $g$. (3) Immediate from (1) and (2). $\square$

**Definition.** A **bijection** from $X$ to $Y$ is a bijective function; one writes $X \cong Y$ when a bijection exists, and says that $X$ and $Y$ are **equipotent**. Equipotence is reflexive, symmetric and transitive, and it is the relation on which the theory of cardinality is founded.

### Inverses

**Definition.** Let $f : X \to Y$. A **left inverse** of $f$ is a function $g : Y \to X$ with $g \circ f = \mathrm{id}_X$; a **right inverse** is a function $h : Y \to X$ with $f \circ h = \mathrm{id}_Y$; a **two-sided inverse** is a function that is both, and it is then written $f^{-1}$.

**Proposition.** A function $f : X \to Y$ is injective if and only if it has a left inverse, surjective if and only if it has a right inverse, and bijective if and only if it has a two-sided inverse, which is then unique.

**Pro.** If $g \circ f = \mathrm{id}_X$ and $f(x) = f(x')$ then $x = g(f(x)) = g(f(x')) = x'$, so $f$ is injective. Conversely, an injective $f$ has a left inverse: fix $x_0 \in X$ when $X \neq \emptyset$ and define $g(y) = x$ if $y = f(x)$, and $g(y) = x_0$ if $y \notin \operatorname{im} f$; the two cases are unambiguous by injectivity. If $f \circ h = \mathrm{id}_Y$ and $y \in Y$, then $y = f(h(y))$ lies in the image, so $f$ is surjective. Conversely a surjective $f$ has a right inverse, whose existence on each fibre is an appeal to the axiom of choice when $Y$ is infinite — the axiom is stated and discussed. Finally, if $f$ is bijective, define $f^{-1}(y)$ to be the unique $x$ with $f(x) = y$; this is a two-sided inverse, and it is unique because any two-sided inverse $g$ satisfies $g = g \circ f \circ f^{-1} = f^{-1}$. $\square$

**Corollary.** If $f$ is bijective then $(f^{-1})^{-1} = f$, and if $g \circ f$ is a bijection with $f$ and $g$ bijective then $(g \circ f)^{-1} = f^{-1} \circ g^{-1}$.

### Images and Preimages

**Definition.** For $f : X \to Y$ and subsets $A \subseteq X$, $B \subseteq Y$, the **image** of $A$ and the **preimage** of $B$ are

$$
f(A) = \{f(x) : x \in A\} \subseteq Y, \qquad f^{-1}(B) = \{x \in X : f(x) \in B\} \subseteq X.
$$

The notation $f^{-1}(B)$ for the preimage does not presuppose that $f$ is invertible: it denotes a subset of $X$ and is defined for every function.

**Proposition.** Let $f : X \to Y$, let $A, A' \subseteq X$ and $B, B' \subseteq Y$, and let $(A_i)$ and $(B_j)$ be families.

1. $f(A \cup A') = f(A) \cup f(A')$, and $f(\bigcup_i A_i) = \bigcup_i f(A_i)$.
2. $f(A \cap A') \subseteq f(A) \cap f(A')$, with equality for all $A, A'$ if and only if $f$ is injective.
3. $f^{-1}(B \cup B') = f^{-1}(B) \cup f^{-1}(B')$ and $f^{-1}(B \cap B') = f^{-1}(B) \cap f^{-1}(B')$, and both identities hold for arbitrary families.
4. $f^{-1}(Y \setminus B) = X \setminus f^{-1}(B)$ and, for $A \subseteq X$, $f(X \setminus A) \subseteq Y \setminus f(A)$, with equality for all $A$ if and only if $f$ is surjective.
5. $A \subseteq f^{-1}(f(A))$ and $f(f^{-1}(B)) = B \cap \operatorname{im} f$.

**Proof.** (1) $y$ lies in $f(A \cup A')$ exactly when $y = f(x)$ for some $x$ in $A$ or in $A'$, which is exactly the condition that $y \in f(A) \cup f(A')$; the family case is the same with a quantifier. (2) If $y \in f(A \cap A')$ then $y = f(x)$ with $x \in A \cap A'$, so $y \in f(A) \cap f(A')$. If $f$ is injective and $y \in f(A) \cap f(A')$, then $y = f(x) = f(x')$ with $x \in A$, $x' \in A'$, and injectivity gives $x = x' \in A \cap A'$. Conversely equality fails for injectivity only if some $x \neq x'$ has $f(x) = f(x')$, and then $A = \{x\}$, $A' = \{x'\}$ give $f(A) \cap f(A') \neq \emptyset = f(A \cap A')$. (3) $x \in f^{-1}(B \cap B')$ exactly when $f(x) \in B$ and $f(x) \in B'$, that is, when $x$ lies in both preimages; the union is the same argument with "or", and the family statements are analogous. (4) $x \in f^{-1}(Y \setminus B)$ exactly when $f(x) \notin B$, that is, when $x \notin f^{-1}(B)$. For the second, if $y \in f(X \setminus A)$ then $y = f(x)$ with $x \notin A$, so $y \notin f(A)$ and $y \in Y \setminus f(A)$. If $f$ is surjective and $y \in Y \setminus f(A)$, choose $x$ with $f(x) = y$; then $x \notin A$, so $y \in f(X \setminus A)$. Conversely, if equality always holds then $A = \emptyset$ gives $f(X) = Y \setminus f(\emptyset) = Y$, so $f$ is surjective. (5) If $x \in A$ then $f(x) \in f(A)$, so $x \in f^{-1}(f(A))$; and $y \in f(f^{-1}(B))$ exactly when $y = f(x)$ for some $x$ with $f(x) \in B$, that is, when $y \in B$ and $y \in \operatorname{im} f$. $\square$

**Remark.** Preimages behave better than images: they preserve unions, intersections and complements without exception, whereas images preserve only unions in general. This asymmetry is used silently throughout the corpus.

## The Algebra of Subsets as a Boolean Algebra

### The Boolean Algebra Axioms

The nine laws listed for $\cup$, $\cap$ and complement are, after the omission of those that follow from the others, the axioms of a **Boolean algebra**: a distributive lattice with a least element $0$ and a greatest element $1$ in which every element has a complement. The subsets of a fixed set, with the operations above, form the **power-set algebra** of $X$, the standard example; under the **characteristic function** $\chi_A : X \to \{0,1\}$, which takes the value $1$ on $A$ and $0$ off it, the operations become the pointwise operations $\min$, $\max$ and $1 - (\cdot)$ on $\{0,1\}$, and $A \mapsto \chi_A$ is a bijection from $\mathcal{P}(X)$ to $\{0,1\}^X$.

**Remark.** The power-set algebra $\mathcal{P}(X)$ and the algebra of propositions built from $|X|$ atoms are the same Boolean algebra, the translation sending a subset to the disjunction of the atoms it contains. The general theory of Boolean algebras — atoms, homomorphisms, quotients, and the representation of a finite one as a power set — belongs to Part V, and the logical reading.

## Summary

A set is determined by its elements (extensionality). Subsets are ordered by inclusion, which is reflexive, antisymmetric and transitive; the operations of union, intersection, complement and symmetric difference on the subsets of a fixed universe satisfy idempotence, commutativity, associativity, distributivity, absorption, the identity and complement laws, double complement, and the De Morgan laws. The power set $\mathcal{P}(X)$ is a distributive complemented lattice, and these are the axioms of a Boolean algebra, studied in Part V.

Ordered pairs are coded as $\{\{a\},\{a,b\}\}$, which makes $(a,b) = (c,d)$ exactly when $a = c$ and $b = d$; the Cartesian product $X \times Y$ is the set of ordered pairs, the product of a family is the set of choice functions, and the axiom of choice is the assertion that this set is nonempty when every factor is.

A relation on $X$ is a subset of $X \times X$; an equivalence relation is reflexive, symmetric and transitive, its classes partition $X$, and the map from equivalence relations to partitions is a bijection. A partial order is reflexive, antisymmetric and transitive; a total order has every pair comparable; the general theory is. A function is a relation with exactly one value at each point of the doma; composition is associative; injective, surjective and bijective functions are characterised by the existence of left, right and two-sided inverses; and preimages preserve all the set operations while images preserve only unions in general.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\in$, $\notin$ | Membership and its negation |
| $\emptyset$ | The empty set |
| $A \subseteq B$, $A \subsetneq B$ | Subset; proper subset |
| $\mathcal{P}(X)$ | Power set of $X$; set of all subsets |
| $A \cup B$, $A \cap B$ | Union and intersection |
| $A^{\mathrm{c}}$, $A \setminus B$ | Complement in a fixed universe; set difference |
| $A \mathbin{\triangle} B$ | Symmetric difference |
| $\bigcup_i A_i$, $\bigcap_i A_i$ | Union and intersection of a family |
| $\chi_A$ | Characteristic (indicator) function of $A$ |
| $(a,b)$ | Ordered pair, coded as $\{\{a\},\{a,b\}\}$ |
| $X \times Y$, $\prod_{i \in I} A_i$ | Cartesian product of two sets; of a family |
| $\bigsqcup_i A_i$ | Disjoint union of a family |
| $R \subseteq X \times Y$, $x \mathrel{R} y$ | Relation from $X$ to $Y$ and its notation |
| $R^{-1}$, $S \circ R$ | Inverse relation; composition of relations |
| $\Delta_X$ | Identity (diagonal) relation on $X$ |
| $\sim$, $[x]$, $X/{\sim}$ | Equivalence relation; class of $x$; quotient set |
| $\pi : X \to X/{\sim}$ | Quotient map |
| $\leq$, $<$, $\subseteq$ | Partial order; strict order; inclusion |
| $f : X \to Y$, $x \mapsto f(x)$ | Function, domain $X$, codomain $Y$, and its rule |
| $\mathrm{id}_X$ | Identity function on $X$ |
| $g \circ f$ | Composite, $(g \circ f)(x) = g(f(x))$ |
| $Y^X$ | Set of functions from $X$ to $Y$ |
| $\operatorname{im} f = f(X)$ | Image of $f$ |
| $f(A)$, $f^{-1}(B)$ | Image of a subset; preimage of a subset |
| $X \cong Y$ | Equipotence: a bijection $X \to Y$ exists |





## Further Reading

- Paul R. Halmos, *Naive Set Theory* (Van Nostrand, 1960; reprinted Springer, 1974), for the elementary development of sets, relations, functions and the power set used here.
- Nicolas Bourbaki, *Théorie des ensembles* (Hermann, 1970), for the formal treatment of relations, correspondences and the calculus of sets.
- Kenneth Kunen, *Set Theory: An Introduction to Independence Proofs* (North-Holland, 1980), for the axiomatic basis against which the naive operations of this article are justified.
- Thomas Jech, *Set Theory*, 3rd millennium ed. (Springer, 2003), for the standard reference on the axiom system, ordinals and cardinals.
- Patrick Suppes, *Axiomatic Set Theory* (Van Nostrand, 1960; reprinted Dover, 1972), for a careful account of the set-theoretic definition of ordered pairs and relations.
- Herbert B. Enderton, *Elements of Set Theory* (Academic Press, 1977), for functions and relations developed from the axioms with full proofs.
- Garrett Birkhoff, *Lattice Theory*, 3rd ed. (American Mathematical Society, 1967), for the power-set algebra as the model of a Boolean algebra.
