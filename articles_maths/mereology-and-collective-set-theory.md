
# __Mereology and Collective Set Theory__

## Introduction

A set in the sense of Zermelo and Fraenkel is determined by its elements: the membership relation is primitive, the elements come first, and the axiom of extensionality says that two sets with the same elements are equal. **Mereology**, the collective set theory of Leśniewski, reverses the order of construction. The whole is primitive and the parts are what a division of the whole produces. There need be no atoms, no empty object, and no element that fails to be a part.

The theory is not a rival of set theory in its mathematical content. Its classical models are Boolean algebras with the least element deleted, and this article proves nothing that contradicts that. It is a different language, and the difference shows in one place especially: **the parthood relation of a mereology is a pre-order, and antisymmetry may fail.** Two elements may each be a part of the other and yet be distinct.

That failure is the subject of this article. A pre-order that is not antisymmetric is not an order, and the parts of order theory that use antisymmetry without saying so change when it is dropped: a least element is no longer unique, the two standard definitions of a proper part no longer agree, and one of the supplementation principles no longer follows from the other. The article also separates extensionality, which the axioms of parthood do not give in either case, from antisymmetry, with which it is often run together. It develops the theory with antisymmetry not assumed, marks each place where it is used and each place where it is not, and shows that a mereology without antisymmetry is recovered as an ordinary partial order by the one construction that its own order theory provides, namely the quotient that identifies mutual parts.

The article presupposes the relations, pre-orders, equivalence relations and quotients of *Sets, Functions and Relations*, and the partial orders, quotient orders and fixed-point theory of *Order Theory and Lattices*. The Boolean algebras against which classical mereology is measured belong to Part VI; the comparison at the end of the article is a citation, and no theorem of that Part is used. Among the number systems only $\mathbb{N}$ and $\mathbb{Z}$ are used.

Two conventions fix the position of the subject. The article contains no physics: the reading of a composite quantum system as a single whole rather than as a pair of parts is a physical interpretation, it belongs to the physics corpus, and it is only referred to. And the article is a theory of the division relation, not a theory of quantity or of measurement; the words *whole*, *part* and *sum* carry their technical mereological senses throughout.

## Collective Set Theory

### The Whole Before the Parts

The two theories differ in the order of construction, and the difference is visible in a single example.

**Example.** Let $M = \{1,2,3,4,5,6\}$ be a whole of six units, and consider the two collections of parts

$$
D_1 = \bigl\{\{1,2,3\},\,\{4,5,6\}\bigr\}, \qquad
D_2 = \bigl\{\{1,2\},\,\{3,4\},\,\{5,6\}\bigr\}.
$$

Each collection covers the whole, and neither has a member that meets another member. In a collective set theory the class of a collection is its **sum**, so both collections have the same sum $M$ and the two descriptions name the same whole:

$$
D_1 = D_2 .
$$

In Zermelo–Fraenkel set theory the elements come first and the whole is formed from them, so the two descriptions name different objects, since $\{3,4\} \in D_2$ while $\{3,4\} \notin D_1$:

$$
D_1 \neq D_2 .
$$

The example isolates the difference. In the first theory a whole has many divisions and the divisions are not distinguished; in the second the object is the collection of its elements and different collections are different objects.

Two consequences are stated at once, because the rest of the article depends on them. First, a mereology has no distinguished way of cutting a whole, so the theory must be able to say when two divisions give the same parts, and it does so with the division relation of the next section. Second, the relation between the parts of one division and the parts of another is a relation of the elements of the universe alone; no set-theoretic membership is involved at any point.

### Division and the Class

**Definition.** A **collective set theory**, or **mereology**, consists of a universe $M$ of **objects** together with a binary relation $\mid$ on $M$, the **division relation**. The expression $x \mid y$ is read *$x$ divides $y$*.

The division relation is required to satisfy the following postulates.

| Name | Statement |
|---|---|
| (EPT1) | $\forall x\; x \mid x$ |
| (EPT2) | $\forall x\,\forall y\,\forall z\;\bigl(x \mid y \wedge y \mid z \Rightarrow x \mid z\bigr)$ |
| (EPT3) | $\exists x\,\exists y\;\bigl(x \mid y \wedge y \mid x \wedge x \neq y\bigr)$ |
| (EPT3A) | $\forall x\,\exists y\;\bigl(x \mid y \wedge y \mid x \wedge x \neq y\bigr)$ |

The first two say that $\mid$ is a **pre-order**, in the sense of *Sets, Functions and Relations*. The third says that this pre-order is not antisymmetric. The fourth is a stronger form available in the same setting, that every object has a distinct partner in mutual division; it makes the system symmetric in the division relation, it is not used below, and all the results of the article are consequences of the first three alone.

The postulates deserve a comment each, because they are the point of the theory. Reflexivity says that every object divides itself, so an object is an improper part of itself and there are no exceptions. Transitivity says that the parts of a part are parts of the whole, which is what makes division a relation that can be composed. **Non-antisymmetry is the step that is usually taken and is here withheld.** In Zermelo–Fraenkel set theory, and in the order theory built on it, antisymmetry is the axiom that turns a pre-order into an order, and it is usually presented as forced by the meaning of equality. The next example shows that in one of the most familiar pre-orders of arithmetic it is simply false.

**Remark.** Antisymmetry is not a defect of a construction but a property of a relation, and (EPT3) asserts its failure for the division relation. The article therefore does not *add* a strange axiom; it declines to add the usual one.

### Sums

**Definition.** Let $\mathcal{S}$ be a nonempty collection of objects of $M$. A **sum** of $\mathcal{S}$, also called a **fusion**, is an object $s$ such that $x \mid s$ for every $x \in \mathcal{S}$, and $s \mid t$ for every $t$ with $x \mid t$ for all $x \in \mathcal{S}$.

This is the supremum of $\mathcal{S}$ in the pre-order $\mid$, in the sense of *Order Theory and Lattices*, and the mereological name is kept because the reading is different. The existence of sums is a postulate of **classical mereology** and is not assumed in this article; where a result needs it, the need is stated. Two features of the definition are worth recording.

First, a sum is unique up to mutual division when it exists: if $s$ and $s'$ are both sums of $\mathcal{S}$, then $s \mid s'$ and $s' \mid s$, and $s = s'$ only if the relation is antisymmetric. This is the general phenomenon of the next sections, met here first in the theory's central operation.

Second, the sum of a single object is that object, and the sum of two objects, when it exists, is the least object having both for parts. In the classical model the sums are the joins, which is why the last section of the article can compare the theory with Boolean algebra.

## The Division Relation

### Divisibility of the Integers

The division relation is not an invention of philosophy. The divisibility relation of the integers is the standard model, and it has exactly the properties (EPT1)–(EPT3).

**Definition.** On $\mathbb{Z}$, write $x \mid y$ when there is a $k \in \mathbb{Z}$ with $y = kx$; equivalently, when the remainder of $y$ on division by $x$ is $0$ for $x \neq 0$.

**Example.** The relation $\mid$ on $\mathbb{Z}$ is reflexive and transitive. It is not antisymmetric, since

$$
1 \mid -1, \qquad -1 \mid 1, \qquad 1 \neq -1 .
$$

The pair $\pm 1$ is exactly the pair of units of $\mathbb{Z}$, and the failure of antisymmetry is the presence of a nontrivial unit. The same phenomenon recurs for every pair of associates: $-6$ and $6$ divide each other, and so do $-20$ and $20$.

This example is the reason the article's conventions were chosen as they were. A reader who wants a picture of a mereology without antisymmetry can take the divisibility pre-order of $\mathbb{Z}$ and read divisibility as parthood; a reader who wants a picture of a *mereology* proper should imagine the same relation on a universe whose objects are wholes, with the units playing the role of the several ways in which one whole may be the same as another.

**Remark.** The divisibility relation of $\mathbb{N}$ is antisymmetric, while that of $\mathbb{Z}$ is not, and the two differ only in the units. The passage between them is the quotient construction below: the antisymmetrisation of $\mid$ on $\mathbb{Z}$ is exactly the divisibility order of $\mathbb{N}$.

**Remark (the quotient is not constrained by the postulates).** The postulates (EPT1)–(EPT3) constrain the relation and nothing else; they place no condition on the quotient $k$ in $y=kx$. In particular nothing in the axioms restricts $k$ to the units $\pm1$ or to any finite set, and a relation satisfying the postulates admits divisions with arbitrary integer quotients. A physical reading of the division relation may nevertheless impose such a restriction — the splitting of a whole into its divisions may be required to proceed in integral, or in unit, steps — but the restriction is then a separate hypothesis, not a theorem of the mereology. The distinction matters wherever the relation is used to select objects rather than to describe them: the reading of a bipartite quantum state in *Entangled Subsystems in the Biquaternion Framework* imposes a unit-quotient rule, and the exhaustiveness of the catalogue of states so obtained is a question about that hypothesis and not about the division relation.

### The Quotient by Mutual Division

A pre-order carries a canonical equivalence relation, and for the division relation it has a mereological reading.

**Definition.** Two objects are **mutual parts**, written $x \sim y$, when $x \mid y$ and $y \mid x$.

**Proposition.** The relation $\sim$ is an equivalence relation, and the classes are the maximal collections of objects that divide one another pairwise.

**Proof.** Reflexivity is (EPT1); symmetry is the definition; transitivity holds because $x \sim y$ and $y \sim z$ give $x \mid y \mid z$ and $z \mid y \mid x$, whence $x \mid z$ and $z \mid x$ by (EPT2). The second statement is immediate from the definition and (EPT2).

**Theorem.** The relation $\preceq$ on the quotient $M/{\sim}$ given by
$$
[x] \preceq [y] \quad\iff\quad x \mid y
$$
is well defined and is a partial order.

**Proof.** If $[x]=[x']$ and $[y]=[y']$ then $x' \mid x \mid y \mid y'$, so $x' \mid y'$ by (EPT2), and $\preceq$ does not depend on the representatives. Reflexivity and transitivity of $\preceq$ are those of $\mid$. For antisymmetry, if $[x] \preceq [y]$ and $[y] \preceq [x]$ then $x \sim y$, so $[x]=[y]$.

This is the general construction that turns a pre-order into an order, and it is the passage from a mereology without antisymmetry to a classical order structure. Two points are worth making explicit.

**Remark.** The objects of the quotient are the mutual-division classes, and in the divisibility model of $\mathbb{Z}$ they are the pairs $\{n,-n\}$ for $n \neq 0$. The quotient is the divisibility order of $\mathbb{N}$, and this is the precise sense in which $\mathbb{Z}$ and $\mathbb{N}$ carry one division relation, not two.

**Remark (the trap of the least element).** A theorem of *Order Theory and Lattices* states that a least element of a partial order, when it exists, is unique by antisymmetry. In a pre-order the corresponding statement is false as written: a least element is unique only up to mutual division, and the uniqueness statement belongs to the quotient. A computation that takes a minimum over a pre-order and asserts the result to be unique has used antisymmetry without saying so. The same trap occurs for maximal and minimal elements, and it is the reason this article states its results about $\sim$-classes rather than about objects wherever uniqueness is claimed.

## Parthood and Proper Parthood

### Parthood

**Definition.** The **parthood** relation of a mereology is the division relation, written $\le$ from here on: $x \le y$ means that $x$ is a **part** of $y$. An object is an **improper part** of itself and a **proper part** of $y$ when it is a part of $y$ and distinct from it; the symbol $<$ is reserved for the proper part and is made precise below.

In the classical theory $\le$ is required to be antisymmetric as well as reflexive and transitive, and the classical theory is therefore the special case of the present one in which no two distinct objects are mutual parts. The reader should keep the two readings in view: $\le$ is a pre-order in general and a partial order in the classical case, and every statement below is either proved from the pre-order axioms, in which case it holds in both cases, or has its antisymmetry hypothesis displayed.

### The Two Definitions of a Proper Part

In classical mereology the proper part has two standard definitions, and in a partial order they coincide.

**Definition.** For objects $x$ and $y$ the first proper-part relation, written (PP1), is given by

$$
x <_{1} y \quad\iff\quad x \le y \ \wedge\ x \neq y ,
$$

and the second, written (PP2), by

$$
x <_{2} y \quad\iff\quad x \le y \ \wedge\ y \nleq x .
$$

**Proposition.** If $x <_{2} y$ then $x <_{1} y$.

**Proof.** Suppose $x \le y$ and $y \nleq x$. If $x = y$ then $y \le x$ by reflexivity, which is the negation of the hypothesis; hence $x \neq y$, and $x <_{1} y$.

The converse is the statement that fails without antisymmetry, and it fails for the whole of the interesting case.

**Proposition.** For a reflexive transitive relation $\le$ on $M$, the following are equivalent.

1. $\le$ is antisymmetric.
2. The two proper-part relations agree: $x <_{1} y \iff x <_{2} y$ for all $x,y$.
3. Mutual parthood is equality: $x \sim y$ implies $x = y$.
4. The quotient $M/{\sim}$ is $M$ itself.

**Proof.** (1)$\Rightarrow$(2): given $x <_{1} y$, suppose $y \le x$; with $x \le y$ antisymmetry gives $x = y$, contradicting $x \neq y$; hence $y \nleq x$ and $x <_{2} y$. The reverse inclusion is the previous proposition. (2)$\Rightarrow$(3): if $x \sim y$ with $x \neq y$, then $x <_{1} y$, so $x <_{2} y$, so $y \nleq x$, contradicting $y \mid x$. (3)$\Rightarrow$(1): if $x \le y$ and $y \le x$ then $x \sim y$, so $x = y$. (3)$\iff$(4) is the definition of the quotient.

The proposition is the first precise statement of what antisymmetry buys in this theory: it is not a convenience of notation but the exact condition under which the two definitions of a proper part agree. In a mereology without antisymmetry the two definitions are genuinely different relations, and every subsequent statement must choose one. The article uses the first,

$$
x < y \quad\iff\quad x \le y \ \wedge\ x \neq y ,
$$

and says explicitly when a result changes under the other reading.

### Mutual Parts

**Definition.** Objects $x$ and $y$ are **mutual parts** when $x \le y$ and $y \le x$ with $x \neq y$; they are the nontrivial classes of $\sim$.

Under (PP1) mutual parts are proper parts of one another; under (PP2) neither is a proper part of the other, since each is a part of the other. The same pair of objects is therefore a pair of proper parts in one convention and a pair of improper parts in the other, which is the sharpest form of the ambiguity the last subsection described. The mutual-parts configuration is not exotic: it is what a unit of a ring is, it is what a nontrivial class of $\sim$ is, and it is the configuration that (EPT3) guarantees to exist.

**Example.** In the divisibility relation of $\mathbb{Z}$ the mutual parts of $1$ are exactly $\pm 1$. In a whole divided in two ways, the two descriptions of the whole are mutual parts of one another.

## Supplementation

### Overlap, Disjointness and the Two Principles

**Definition.** Two objects **overlap**, written $x \circ y$, when they have a common part: there is $z$ with $z \le x$ and $z \le y$. They are **disjoint**, written $x \perp y$, when they do not overlap.

In a pre-order the relation $\circ$ is reflexive and symmetric but need not be transitive, and it is the mereological reading of the conjunction one expects: overlapping objects share a piece. Two supplementation principles relate overlap and parthood.

**Definition.** The **strong supplementation principle** and the **weak supplementation principle** are as follows.

| Name | Statement |
|---|---|
| (SSP) | $x \nleq y \;\Rightarrow\; \exists z\,(z \le x \wedge z \nleq y)$ |
| (WSP) | $x < y \;\Rightarrow\; \exists z\,(z < y \wedge z \nleq x)$ |

Both are read as universally quantified over $x$ and $y$, and $<$ is the first proper-part relation of the previous section unless stated otherwise. In words, (SSP) says that an object that is not a part of another has some part that the other lacks, and (WSP) says that a proper part of a whole leaves a remainder in the whole that is not a part of it. The two are not of the same strength, and the difference between them is the content of the rest of this section.

### The Two Forms of Strong Supplementation

The literature states strong supplementation in two forms, which differ exactly in whether the witness is required to be disjoint from the second object or merely not a part of it. The **disjoint form** is

$$
x \nleq y \;\Rightarrow\; \exists z\,(z \le x \wedge z \perp y) ,
$$

written $(\mathrm{SSP}_\perp)$ below.

**Proposition.** $(\mathrm{SSP}_\perp)$ implies (SSP).

**Proof.** Let $z \le x$ and $z \perp y$. If $z \le y$ then $z$ overlaps $y$, since $z \le z$ and $z \le y$; hence $z \nleq y$. So a witness for $(\mathrm{SSP}_\perp)$ is a witness for (SSP).

The converse fails, and the failure is visible in the smallest possible order.

### The Two-Element Order

**Example.** Let $M = \{a,b\}$ with $a \le a$, $b \le b$ and $a \le b$, and with $b \nleq a$. The relation is reflexive, transitive and antisymmetric, and the only ordered pair with $x \nleq y$ is $(b,a)$.

*Strong supplementation in the non-part form holds.* The witness is $z = b$, since $b \le b$ and $b \nleq a$.

*Strong supplementation in the disjoint form fails.* A witness for $(b,a)$ would need $z \le b$ and $z \perp a$. The elements below $b$ are $a$ and $b$; the element $a$ overlaps $a$, and $b$ overlaps $a$ because $a \le b$ and $a \le a$. Neither is disjoint from $a$, so no witness exists.

*Weak supplementation fails.* The only proper part of $b$ is $a$, and $a \nleq a$ is false, so the required remainder does not exist.

The order is therefore a model of (SSP) and of antisymmetry in which (WSP) fails. Two conclusions follow, and they are the main points of the section.

**Conclusion 1: the two forms of strong supplementation are not equivalent.** The non-part form is strictly weaker than the disjoint form, and the two-element order separates them.

**Conclusion 2: antisymmetry alone does not make the non-part form imply weak supplementation.** The order above is antisymmetric, so the classical claim that weak supplementation follows from strong supplementation must be read with the disjoint form of the latter.

The positive statement is the following. Its proof applies the disjoint form to the pair $(y,x)$, and the step that needs the disjointness is the observation that $y$ itself is not disjoint from $x$, because $x$ is a common part of the two; the witness therefore cannot be $y$ and is a proper part of it.

**Theorem.** If $\le$ is reflexive and antisymmetric and satisfies $(\mathrm{SSP}_\perp)$, then (WSP) holds.

**Proof.** Let $x < y$, so $x \le y$ and $x \neq y$. By antisymmetry $y \nleq x$. Apply $(\mathrm{SSP}_\perp)$ to the pair $(y,x)$: there is $z$ with $z \le y$ and $z \perp x$. If $z = y$ then $y \perp x$, which is impossible because $x$ is a common part of $y$ and of $x$, since $x \le y$ and $x \le x$. Hence $z \neq y$, so $z < y$, and $z \perp x$ gives $z \nleq x$. Thus $z$ is the remainder required by (WSP).

**Remark.** The theorem is proved from reflexivity, antisymmetry and the disjoint form of strong supplementation; transitivity is not used. That the argument does not need transitivity is not an accident of the proof but a feature of the statement: supplementation constrains a pair of objects directly, and the composition of parts is not involved. The failure of the implication for the non-part form is likewise independent of transitivity, as the two-element order, which is transitive, shows.

**Remark (the failure of antisymmetry and weak supplementation).** There is a companion statement in the other direction, and it is the reason the source literature cares about antisymmetry here. If $\le$ is transitive and contains two distinct mutual parts $u$ and $v$, then (WSP) under (PP1) fails. Indeed $u < v$, and any $z$ with $z \le v$ satisfies $z \le u$ by $v \le u$ and transitivity, so $z \nleq u$ has no solution; there is no remainder. A single pair of mutual parts therefore destroys weak supplementation, in every ordering and with no other hypothesis, and this is how the failure of antisymmetry is seen to be a strong condition on the theory and not a technicality.

### The Second Definition and the Recovery of Weak Supplementation

The last remark reads $<$ as (PP1), and that reading is the whole reason the failure of antisymmetry destroys weak supplementation. Under (PP2) the classical implication survives without the antisymmetry hypothesis. Write $(\mathrm{WSP}_\perp)$ for weak supplementation in the disjoint form read with the second proper-part relation,

$$
x <_{2} y \;\Rightarrow\; \exists z\,\bigl(z <_{2} y \wedge z \perp x\bigr),
$$

which implies the non-part form (WSP) read with $<_2$, because disjointness implies non-part.

**Theorem.** If $\le$ is reflexive and transitive and satisfies $(\mathrm{SSP}_\perp)$, then $(\mathrm{WSP}_\perp)$ holds. No antisymmetry hypothesis is made, and transitivity is the only order axiom used beyond reflexivity.

**Proof.** Let $x <_{2} y$, so that $x \le y$ and $y \nleq x$. Apply $(\mathrm{SSP}_\perp)$ to the pair $(y,x)$: there is $z$ with $z \le y$ and $z \perp x$. If $y \le z$, then $x \le y \le z$ gives $x \le z$ by transitivity, and with $x \le x$ the element $x$ is a common part of $x$ and of $z$, contradicting $z \perp x$. Hence $y \nleq z$, and with $z \le y$ this is $z <_{2} y$. The element $z$ is a proper part of $y$ under (PP2) and is disjoint from $x$, which is what $(\mathrm{WSP}_\perp)$ demands.

The proof never separates a pair of mutual parts, and the reason is visible in the definitions: at distinct mutual parts $u$ and $v$ one has $u \le v$ and $v \le u$, so $v \nleq u$ fails, $u <_{2} v$ fails, and the second proper-part relation is empty there. Weak supplementation has no instance to satisfy at such a pair, which is why antisymmetry is not needed. The antisymmetry in the positive theorem of the previous subsection is therefore an artefact of reading $<$ as (PP1); under (PP2) it can be dropped.

The sharpest evidence is a single structure on which the two readings disagree.

**Example.** Let $M = \{a,b,c\}$ with $a \le b$, $b \le a$, $c \le c$ and no other pairs, so that $c$ is incomparable with $a$ and with $b$. The relation is reflexive and transitive and is not antisymmetric, since $a$ and $b$ are distinct mutual parts.

- $(\mathrm{SSP}_\perp)$ holds, and not vacuously. An incomparable pair has $c$ as one member. If $x = c$, the witness is $z = c$, a part of $x$ disjoint from the other element; if $x \neq c$, the only $y$ with $x \nleq y$ is $c$, and the witness is $z = x$, a part of $x$ disjoint from $c$.
- (WSP) under (PP1) fails: $a <_{1} b$, and no $z$ with $z <_{1} b$ is disjoint from $a$, since the only element below $b$ other than $b$ is $a$, and $a$ overlaps $a$.
- $(\mathrm{WSP}_\perp)$ and (WSP) hold under (PP2), vacuously, because $<_{2}$ is empty.

One structure therefore satisfies $(\mathrm{SSP}_\perp)$ and the failure of antisymmetry, fails weak supplementation under the first proper-part relation, and satisfies it under the second. The definition of the proper part, and not only the strength of the supplementation principle, decides the theory. The comparison is collected in the table.

| Proper part | Does (SSP$_\perp$) imply weak supplementation? | Is antisymmetry needed? |
|---|---|---|
| $<_1$, the first definition (PP1) | no | yes; a distinct mutual pair refutes (WSP) |
| $<_2$, the second definition (PP2) | yes, with a disjoint witness | no; reflexivity and transitivity suffice |

## Extensionality

**Definition.** Parthood $\le$ is **extensional** when objects with the same proper parts are equal:

$$
\forall z\,(z < x \iff z < y) \;\Rightarrow\; x = y .
$$

The condition is written (EXT) below.

Extensionality is the mereological form of the axiom of the same name in set theory, and it is a separate postulate: the parthood axioms do not imply it. What is less often said is that it is also independent of antisymmetry, in the strong sense that neither property implies the other. Two orders of two elements settle it.

**Example (antisymmetry without extensionality).** Let $M = \{a,b\}$ with the discrete relation, $a \le a$ and $b \le b$ only. This is antisymmetric and transitive, and neither element has a proper part; the two proper-part collections are equal, while $a \neq b$. Extensionality fails. The order is the two-element antichain, and it is the standard warning that a partial order may have two minimal elements that no part distinguishes.

**Example (extensionality without antisymmetry).** Let $M = \{a,b\}$ with the indiscrete relation $x \le y$ for all $x,y$. Antisymmetry fails and $a$ and $b$ are mutual parts. Under (PP1) the proper parts of $a$ are exactly $\{b\}$ and those of $b$ are exactly $\{a\}$, so the two collections differ and (EXT) holds vacuously. Extensionality is therefore compatible with the failure of antisymmetry.

The two examples should be read together with the last section of the article. Under (PP2) the second example loses its extensionality, since with no proper parts at all the two collections are both empty; the definition of a proper part must be fixed before the question can be asked, and the answer depends on the choice. What does not depend on the choice is the general point, that the failure of antisymmetry and the failure of extensionality are two different things, and a theory may have either without the other.

**Remark.** The quotient of *The Quotient by Mutual Division* is the passage that repairs the failure of antisymmetry, and it does so at the cost of identifying objects. It is not the same operation as imposing extensionality. The first collapses the pre-order to a partial order by dividing by an equivalence relation; the second forbids two distinct objects to have the same parts. A structure may need one, the other, both or neither.

### Extensionality and the Two Proper-Part Relations

The independence of extensionality and antisymmetry recorded above holds when $<$ is read as (PP1). Under (PP2) the two are not independent: extensionality implies antisymmetry.

**Theorem.** Under the second proper-part relation (PP2), (EXT) implies antisymmetry. Under the first (PP1) it does not.

**Proof.** Suppose $u$ and $v$ are distinct mutual parts, so that $u \le v$ and $v \le u$ with $u \neq v$. For every $z$, transitivity applied to $u \le v$ and $v \le u$ gives $z \le u \iff z \le v$ and $u \nleq z \iff v \nleq z$, the second because $v \le z$ together with $u \le v$ would give $u \le z$, and conversely. Hence

$$
z <_{2} u \iff z \le u \wedge u \nleq z \iff z \le v \wedge v \nleq z \iff z <_{2} v ,
$$

so $u$ and $v$ have the same (PP2)-proper parts and, being distinct, violate (EXT). This is the contrapositive of the first claim. For the second, the two-element indiscrete pre-order is not antisymmetric and satisfies (EXT) under (PP1), as the earlier example showed, because its two elements are proper parts of one another under (PP1) and are thereby distinguished.

The extensionality principle of the source literature is therefore not independent of antisymmetry as such; it is independent of it only under the first proper-part relation, and under the second it is exactly the axiom that forbids distinct mutual parts. This is the same phenomenon as in supplementation: the proper-part relation, fixed before the question is asked, decides the answer.

## Mereology and Boolean Algebra

The classical theory is a special case of the present one, and the comparison was known before the theories were put in the present form.

**Theorem (Clay; Loeb).** A structure satisfying the axioms of classical mereology — parthood a partial order, sums of nonempty collections, and extensionality — is isomorphic to a Boolean algebra with the least element deleted. Under the isomorphism parthood is inclusion, the sum of a collection is its join, and the whole of the universe is the greatest element.

The theorem is stated here as a citation; the Boolean algebras are the subject of Part VI and no result of that Part is used in this article. Three points of comparison make the statement concrete.

**The least element.** A Boolean algebra has a least element $0$, the empty join, and it is deleted because a mereology has no empty part: the sum of a collection of parts is a part, and a collection has at least one member by the definition of sum. The deletion is not a defect but the content of the correspondence: a Boolean algebra is a mereology with one additional object, the empty one, and the additional object is exactly the one that is a part of everything.

**The class operation.** In the classical model the class of a collection and its sum are the same object, which is the property the example of the first section displayed. In a Boolean algebra this is the statement that a supremum is determined by the elements below it, and it is the order-theoretic content of the claim that a whole is divided in many ways and remains one whole.

**The failure of antisymmetry.** The theorem is a statement about the classical theory, in which antisymmetry holds. Its extension to the non-antisymmetric case is the passage to the quotient: by *The Quotient by Mutual Division*, a mereology whose relation is a pre-order has a quotient that is a partial order, and the quotient satisfies the hypotheses of the theorem whenever the sums and the extensionality are preserved by the identification of mutual parts. The source literature makes the same observation in the other direction, that a model of mereology without antisymmetry becomes a classical model once an order relation is defined from the division relation, and the construction that does it is the quotient of the article.

**Remark.** The comparison also fixes what a mereology is not. It is not a theory of sets with a different membership; it is the theory of the order structure that remains when the empty object is removed. What the non-antisymmetric theory adds is the possibility that two objects occupy the same position in that order and are nevertheless two, which the Boolean reading cannot express.

## Summary

Mereology, or collective set theory, takes the whole as primitive and the division relation as fundamental. The relation satisfies (EPT1)–(EPT3): it is reflexive and transitive, and it is not antisymmetric. Non-antisymmetry is not an oddity of the axioms but a property of familiar relations, of which the divisibility of $\mathbb{Z}$ is the standard example, where $1$ and $-1$ divide each other and are distinct.

Two objects that divide each other are mutual parts, and mutual parthood is an equivalence relation whose classes are the objects of a quotient on which the division relation becomes a partial order. This quotient is the passage from a mereology without antisymmetry to a classical order, and in the divisibility example it is the passage from $\mathbb{Z}$ to $\mathbb{N}$. A least element of a pre-order is unique only up to mutual division; the uniqueness statement of order theory belongs to the quotient.

The proper part has two standard definitions, $x <_{1} y$ when $x \le y$ and $x \neq y$, and $x <_{2} y$ when $x \le y$ and $y \nleq x$. The second implies the first always; the first implies the second exactly when the relation is antisymmetric. Antisymmetry is therefore the exact condition under which the two definitions agree, and a theory without it must choose; the article chooses the first.

Of the two supplementation principles, strong supplementation has a non-part form and a disjoint form, and the disjoint form is strictly stronger. The two-element chain satisfies the non-part form and antisymmetry while failing weak supplementation, so the classical derivation of weak supplementation from strong supplementation requires the disjoint form. Positive version: a reflexive antisymmetric relation satisfying the disjoint form satisfies weak supplementation, and the proof does not use transitivity. In the other direction, one pair of distinct mutual parts in a transitive relation destroys weak supplementation outright when $<$ is read as (PP1). The reading decides the matter: under (PP2) strong supplementation in the disjoint form implies weak supplementation using reflexivity and transitivity alone, with no antisymmetry, because the second proper-part relation is empty at a pair of mutual parts and weak supplementation has no instance there to satisfy. A single structure of three elements, a pair of mutual parts together with an element incomparable with both, satisfies the disjoint form and the failure of antisymmetry, fails weak supplementation under (PP1) and satisfies it under (PP2).

Extensionality is a separate postulate and is independent of antisymmetry in both directions when $<$ is read as (PP1), the two-element antichain showing antisymmetry without extensionality and the two-element indiscrete order showing extensionality without antisymmetry. Under (PP2) the two are not independent: extensionality implies antisymmetry, since distinct mutual parts have the same proper parts, so the reading that recovers weak supplementation also makes extensionality equivalent to antisymmetry. Finally, the classical theory is a Boolean algebra with the least element deleted, and on the quotient the non-antisymmetric theory reduces to the classical one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M$ | Universe of objects of a collective set theory |
| $\mid$ | Division relation, a pre-order |
| $\le$ | Parthood, the same relation read as parts |
| $<$ | Proper part: $x < y$ iff $x \le y$ and $x \neq y$ |
| $<_{1}$, $<_{2}$ | The two definitions of a proper part, (PP1) and (PP2) |
| $\sim$ | Mutual parthood: $x \sim y$ iff $x \mid y$ and $y \mid x$ |
| $M/{\sim}$ | Quotient by mutual parthood, a partial order |
| $\preceq$ | The order induced on $M/{\sim}$ |
| $x \circ y$ | Overlap: $x$ and $y$ have a common part |
| $x \perp y$ | Disjointness: the negation of overlap |
| (SSP) | Strong supplementation, non-part form |
| $(\mathrm{SSP}_\perp)$ | Strong supplementation, disjoint form |
| (WSP) | Weak supplementation, non-part form |
| $(\mathrm{WSP}_\perp)$ | Weak supplementation, disjoint form |
| (EXT) | Extensionality of parthood |

## Further Reading

- Stanisław Leśniewski, "O podstawach matematyki", *Przegląd Filozoficzny* **30** (1927), 164–206, for the founding papers of mereology.
- Peter Simons, *Parts: A Study in Ontology* (Clarendon Press, 1987), for the standard modern development of classical mereology, the classical axioms and the supplementation principles.
- Achille C. Varzi, "The extensionality of parthood and composition", *The Philosophical Quarterly* **58** (2008), 108–133, and "A note on the transitivity of parthood", *Applied Ontology* **1** (2006), 141–146, for the interaction of parthood with extensionality and transitivity.
- A. J. Cotnoir, "Antisymmetry and non-extensional mereology", *The Philosophical Quarterly* (2010), 396–405, and A. J. Cotnoir and A. Bacon, "Non-wellfounded mereology", *The Review of Symbolic Logic* **5** (2012), 187–204, for mereology without antisymmetry and the non-wellfounded case.
- Lidia Obojska, "Some remarks on supplementation principles in the absence of antisymmetry", *The Review of Symbolic Logic* **6** (2013), 343–347, for the failure of weak supplementation under a failure of antisymmetry, and Lidia Obojska, "Bi-particle entanglement and its quaternion representation", *Journal of Physics Communications* **2** (2018) 085021, §2, for the presentation of the non-standard collective set theory used in this article; the same author's "Patterns of maximally entangled states within the algebra of biquaternions", *Journal of Physics Communications* **4** (2020) 055018, imposes the unit-quotient rule discussed in the second remark of *Divisibility of the Integers*.
- Robert E. Clay, "Relation of Leśniewski's mereology to Boolean algebra", *The Journal of Symbolic Logic* **39** (1974), 638–648, and Iris Loeb, "From mereology to Boolean algebra", in *The History and Philosophy of Polish Logic* (Palgrave Macmillan, 2014), for the correspondence between classical mereology and Boolean algebra without a least element.
- The physics corpus, in particular *Entangled Subsystems in the Biquaternion Framework*, for the reading of a composite quantum system as a single whole rather than as a pair of parts.
