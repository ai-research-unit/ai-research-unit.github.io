
# __The Order Automorphism Group__

## Introduction

An **order automorphism** of a poset is a bijection that preserves the order in both directions, and
the order automorphisms of a poset $P$ form a group under composition, written
$\operatorname{Aut}(P)$. This article studies that group as an operator layer of the order: it proves
that $\operatorname{Aut}(P)$ is the group of units of the monoid of monotone self-maps of $P$ and a
subgroup of the symmetric group $\operatorname{Sym}(P)$, that an order automorphism preserves every
meet and join that exists, so that for a lattice the order automorphisms and the lattice
automorphisms coincide; it computes the **fixed-point structure** of a single automorphism, which is a
subposet closed under the joins and meets that exist; it studies the action of $\operatorname{Aut}(P)$
on the elements of $P$ and on the **ideals** of $P$, and shows that the action on the ideals is
faithful; and it presents the **linear** and the **affine** orders as the two extreme cases, the one
with the smallest possible automorphism group and the other with a large and highly homogeneous one.

The article presupposes *Order Theory and Lattices* — posets, chains, lattices, meets and joins,
monotone maps and the least and greatest elements — and *Sets, Functions and Relations* — bijections,
the symmetric group and group actions in the elementary sense. The monoid of monotone maps and the
endomorphism monoid of a poset are the subject of *Operators on a Poset*, in this group, and this
article uses the group of units of that monoid without repeating its construction. The lattice
automorphisms and the congruence theory of a lattice are the subject of *Operators on a Lattice*, in
this group; the statement that, for a lattice, the two notions of automorphism coincide is proved
here because the article needs it. The endomorphism monoid and the automorphism group of a general
**relational structure** are the subject of *Endomorphisms of a Relational Structure*, in this group,
of which this article is the order instance; the order automorphisms of a **linear order** are the
rigid case of that theory.

Three boundaries are observed. No **topology** is used: the order automorphisms of a dense order are
computed with the order alone, and the topological dynamics of a later part is not used. The theory of
**groups** is *Groups*, in this Part, and the theory of a group acting on a set is *Transformation
Groups*; here a group occurs only as the group of units of a monoid of monotone maps, and the action
is computed from the composition of maps. The order automorphisms of a **linear space**, and the
affine group of a geometry, are Part IV and are named once to mark the boundary; no scalar, no
distance and no **form** is used.

## Order Automorphisms

### Definition and the Group Structure

Let $(P, \leq)$ be a poset.

**Definition.** An **order automorphism** of $P$ is a bijection $f : P \to P$ such that

$$
x \leq y \quad\Longleftrightarrow\quad f(x) \leq f(y) \qquad \text{for all } x, y \in P .
$$

The set of order automorphisms of $P$ is written $\operatorname{Aut}(P)$, and $\operatorname{End}(P)$
denotes the set of monotone self-maps of $P$, a monoid under composition with identity
$\mathrm{id}_P$, treated in *Operators on a Poset*.

**Theorem.** $\operatorname{Aut}(P)$ is the group of units of the monoid $\operatorname{End}(P)$, and
it is a subgroup of the symmetric group $\operatorname{Sym}(P)$.

**Proof.** The composite of two order automorphisms is an order automorphism, because the equivalences
compose, and the inverse of an order automorphism is an order automorphism, because the defining
equivalence is symmetric in $f$ and $f^{-1}$. So $\operatorname{Aut}(P)$ is closed under composition
and inverses, contains $\mathrm{id}_P$, and is a group. A bijection $f$ is a unit of
$\operatorname{End}(P)$ exactly when $f$ and $f^{-1}$ are monotone, which is exactly the defining
equivalence; so the units are the order automorphisms. Since every order automorphism is a bijection
of $P$, the group is a subgroup of $\operatorname{Sym}(P)$.

**Corollary.** $\operatorname{Aut}(P)$ is the stabiliser of the relation $\leq$ in the action of
$\operatorname{Sym}(P)$ on the set of binary relations on $P$: it is the set of bijections of $P$
that fix $\leq$ as a relation, that is, that carry the relation onto itself.

**Proof.** A bijection $f$ fixes $\leq$ as a relation exactly when $(x,y) \in \leq$ if and only if
$(f(x), f(y)) \in \leq$, which is the definition of an order automorphism.

**Example.** For the two-element antichain on $\{a, b\}$ every bijection is an order automorphism, so
$\operatorname{Aut}(P) = \operatorname{Sym}(P)$ has two elements. For the two-element chain
$\{0 < 1\}$, the identity is the only order automorphism, so $\operatorname{Aut}(P)$ is trivial. The
same set therefore carries two orders whose automorphism groups differ, and the automorphism group is
an invariant of the order and not of the set.

### Preservation of Meets, Joins and Bounds

**Proposition.** Let $f$ be an order automorphism of $P$. If a subset $S \subseteq P$ has a least
upper bound $s$, then $f(S)$ has the least upper bound $f(s)$; dually for the greatest lower bound.
In particular $f$ preserves the least element, the greatest element, the atoms and the coatoms of a
bounded or atomic poset, and the covering relation: $x \lessdot y$ if and only if $f(x) \lessdot
f(y)$.

**Proof.** If $s = \bigvee S$ then $f(s)$ is an upper bound of $f(S)$ by monotonicity. If $u$ is an
upper bound of $f(S)$, then $f^{-1}(u)$ is an upper bound of $S$ by monotonicity of $f^{-1}$, so $s
\leq f^{-1}(u)$ and $f(s) \leq u$. Hence $f(s)$ is the least upper bound. The statements about the
least element, the atoms, the coatoms and the cover relation follow by applying the first statement to
the empty set, to a singleton up-set, and to a two-element set with no element strictly between.

**Theorem.** Let $L$ be a lattice. A map $f : L \to L$ is an order automorphism if and only if it is a
lattice automorphism.

**Proof.** A lattice automorphism preserves $\wedge$ and $\vee$, hence is monotone and has monotone
inverse, so it is an order automorphism. Conversely, an order automorphism $f$ preserves the least
upper bound of $\{x,y\}$ by the proposition, so $f(x \vee y) = f(x) \vee f(y)$, and dually for the
meet; so it is a lattice automorphism.

The theorem is the reason the two notions are not distinguished in the lattice articles: for a
lattice, $\operatorname{Aut}(P)$ as computed here equals the automorphism group of the lattice
computed algebraically in *Operators on a Lattice*. For a poset that is not a lattice the two notions
separate, since a poset may have no meets or joins.

### The Fixed-Point Structure

**Definition.** For $f \in \operatorname{Aut}(P)$ the **fixed-point set** is
$\operatorname{Fix}(f) = \{x \in P : f(x) = x\}$, and the automorphism is **fixed-point-free** if
$\operatorname{Fix}(f) = \emptyset$.

**Proposition.** For every $f \in \operatorname{Aut}(P)$ the fixed-point set is a subposet of $P$
closed under the joins and the meets that exist in $P$; and $\operatorname{Fix}(f) =
\operatorname{Fix}(f^{-1})$. Consequently $\operatorname{Fix}(f)$ is a sublattice of $L$ whenever $L$
is a lattice and $\operatorname{Fix}(f)$ is nonempty.

**Proof.** If $x, y$ are fixed and $x \vee y$ exists, then $f(x \vee y) = f(x) \vee f(y) = x \vee y$
by the preservation of joins, so $x \vee y$ is fixed; the argument for the meet is dual, and the
statement for $f^{-1}$ is the same equivalence. A nonempty subset of a lattice closed under the two
operations is a sublattice.

**Example.** A chain with a least element has trivial automorphism group, since the least element is
fixed and then every element is fixed by induction along the chain; the natural numbers with their
order and every finite chain are therefore rigid. A chain without a least element may be rigid or not,
and the two-element antichain admits the fixed-point-free transposition. So the fixed-point-free
automorphisms occur only on posets of greater symmetry than a chain.

**Proposition (orbits of an automorphism of finite order).** Let $f \in \operatorname{Aut}(P)$ satisfy
$f^n = \mathrm{id}$ for some $n \geq 1$. Then $P$ is the disjoint union of $\operatorname{Fix}(f)$ and
of orbits of size greater than one, each of which divides $n$.

**Proof.** Every element not fixed has an orbit under the cyclic group generated by $f$; the orbit of
$x$ has cardinality equal to the least $k \geq 1$ with $f^k(x) = x$, which divides $n$; and an orbit
of size one is a fixed point. The orbits partition $P$.

**Proposition (the stabiliser).** For each $x \in P$ the set of automorphisms fixing $x$ is a subgroup
of $\operatorname{Aut}(P)$, the **stabiliser** of $x$; every element of the stabiliser restricts to an
order automorphism of the principal ideal ${\downarrow} x$ and of the principal filter ${\uparrow} x$.

**Proof.** The stabiliser is the set of $f$ with $f(x) = x$, which is closed under composition and
inverses. An order automorphism fixing $x$ carries ${\downarrow} x = \{y : y \leq x\}$ onto itself,
because $y \leq x$ if and only if $f(y) \leq f(x) = x$, and similarly for ${\uparrow} x$.

## The Action on the Elements and on the Ideals

### The Action on the Elements

The group $\operatorname{Aut}(P)$ **acts** on $P$ by evaluation, $(f, x) \mapsto f(x)$. The **orbit**
of $x$ is $\operatorname{Aut}(P) \cdot x = \{f(x) : f \in \operatorname{Aut}(P)\}$, and the orbits
partition $P$ as in *Endomorphisms of a Relational Structure*. Two elements in the same orbit have the
same order-theoretic position: they have the same set of lower bounds up to an automorphism, the same
upper bounds, and the same rank in a graded poset.

**Proposition.** The orbits of the action of $\operatorname{Aut}(P)$ on $P$ are the smallest subsets
invariant under every order automorphism; an order isomorphism of posets carries the orbits of the one
onto the orbits of the other, preserving the inherited order. The number of orbits and the order type
of each orbit are therefore invariants of the order type of $P$.

**Proof.** An invariant subset is a union of orbits, by definition of an orbit, and the orbit of $x$ is
contained in every invariant subset containing $x$. An order isomorphism conjugates the automorphism
group of the one poset onto that of the other, hence permutes the orbits of the one onto the orbits of
the other, and it preserves the inherited order.

### The Action on the Ideals

**Definition.** A **down-set**, or **ideal**, in $P$ is a subset $D \subseteq P$ such that $y \leq x
\in D$ implies $y \in D$. The family of down-sets, ordered by inclusion, is written $O(P)$, and the
**principal ideal** generated by $x$ is ${\downarrow} x = \{y \in P : y \leq x\}$.

In a lattice the word ideal is often reserved for a down-set that is also closed under finite joins;
this article uses the down-set sense throughout, and says so when the stronger notion is meant. The
family $O(P)$ is a complete lattice under inclusion, with the union as join and the intersection as
meet, by *Order Theory and Lattices*.

**Proposition.** Every order automorphism $f$ of $P$ maps down-sets to down-sets, and the map

$$
O(f) : D \mapsto f(D), \qquad O(P) \to O(P),
$$

is an order automorphism of $O(P)$. The assignment $f \mapsto O(f)$ is a bijection between
$\operatorname{Aut}(P)$ and a subgroup of $\operatorname{Aut}(O(P))$, and it is a homomorphism of
groups: $O(\mathrm{id}_P) = \mathrm{id}_{O(P)}$ and $O(g \circ f) = O(g) \circ O(f)$.

**Proof.** If $D$ is a down-set and $y' \leq x' \in f(D)$, say $x' = f(x)$ with $x \in D$, then
$f^{-1}(y') \leq f^{-1}(x') = x \in D$, so $f^{-1}(y') \in D$ and $y' = f(f^{-1}(y')) \in f(D)$. So
$O(f)$ is well defined, and $O(f^{-1})$ is its inverse, so $O(f)$ is a bijection; it preserves
inclusion in both directions because $f$ does, so it is an order automorphism of $O(P)$. The
composition law is the associativity of image: $O(g \circ f)(D) = (g \circ f)(D) = g(f(D)) =
O(g)(O(f)(D))$.

**Theorem.** The action of $\operatorname{Aut}(P)$ on the ideals is faithful: if $O(f) =
\mathrm{id}_{O(P)}$ then $f = \mathrm{id}_P$. Hence $\operatorname{Aut}(P)$ embeds in
$\operatorname{Aut}(O(P))$.

**Proof.** If $O(f)$ fixes every down-set, then it fixes the principal ideal ${\downarrow} x$ for every
$x$; so $f({\downarrow} x) = {\downarrow} x$, and applying $f$ to $x$ gives $f(x) \in {\downarrow} x$,
so $f(x) \leq x$; applying the same to $f^{-1}$ gives $f^{-1}(x) \leq x$, that is, $x \leq f(x)$. So
$f(x) = x$ for every $x$ and $f$ is the identity.

### The Linear and the Affine Orders

The two extremes of the theory are the orders whose automorphism group is as small as possible and
those whose automorphism group is as large and as homogeneous as possible.

**Proposition (rigidity of the linear orders).** The only order automorphism of the natural numbers
with the usual order is the identity, and every well-order is rigid: a well-order has no nontrivial
order automorphism.

**Proof.** Let $f$ be an order automorphism of a well-order. The least element $0$ is fixed: $0 \leq
f(0)$ always, and $f^{-1}(0) \leq 0$ forces $f^{-1}(0) = 0$, that is, $f(0) = 0$. Suppose $f$ fixes
every element below $x$. An order automorphism carries the set $P(x) = \{y : y < x\}$ of predecessors
of $x$ onto the set of predecessors of $f(x)$, because $y < x$ if and only if $f(y) < f(x)$; by the
induction hypothesis $f(P(x)) = P(x)$, so the predecessors of $f(x)$ are exactly those of $x$, and in
a chain an element is determined by its set of predecessors. So $f(x) = x$, and by induction over the
well-order $f$ is the identity. The natural numbers are a well-order, so the finite chains and
$\mathbb{N}$ are rigid.

**Example (the largest automorphism group).** For the **discrete order** on a set $X$, in which no two
distinct elements are comparable, every bijection is an order automorphism, so
$\operatorname{Aut}(P) = \operatorname{Sym}(X)$: this is the largest possible automorphism group of an
order on $X$. The discrete order and the well-orders are the extremes of the linear case, the one
maximally symmetric and the other rigid.

**Example (the affine order).** A chain that is dense and has no least and no greatest element, and in
which any two of its points are separated by a further point, is **homogeneous**: its automorphism
group is transitive on the $n$-element subsets of its points for every $n$. The rational line with its
usual order is the standard example, and since the rationals are built in *Rings and Fields*, in this
Part, the example is a forward reference; the order alone is what the computation uses. The **affine
order** of the line, whose order automorphisms include the translations, is the opposite extreme to
the well-orders: its automorphism group is large and moves every finite level. Both extremes are named
here to fix the range of the theory, and no scalar, no distance and no affine structure of the line is
invoked.

## Summary

An order automorphism of a poset is a bijection preserving the order in both directions; the order
automorphisms form the group $\operatorname{Aut}(P)$ of units of the monoid of monotone self-maps, and
it is a subgroup of the symmetric group $\operatorname{Sym}(P)$. An order automorphism preserves every
join, every meet, the least and the greatest elements, the atoms, the coatoms and the cover relation;
for a lattice the order automorphisms are exactly the lattice automorphisms, and the two notions of
automorphism coincide.

The fixed-point set of an automorphism is a subposet closed under the joins and meets that exist, an
automorphism of finite order decomposes the poset into its fixed points and orbits of size dividing
the order, and the stabiliser of an element acts on the down-set and up-set it generates. The group
acts on the elements, with the orbits the smallest invariant subsets, and on the ideals, with the
action faithful: $\operatorname{Aut}(P)$ embeds in the automorphism group of the lattice of down-sets.
The well-orders, and among them the finite chains and the natural numbers, are rigid; the discrete
order has the full symmetric group as its automorphism group; and the dense affine orders, whose
rational example is built in *Rings and Fields*, have large and highly homogeneous automorphism
groups.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{Aut}(P)$ | Group of order automorphisms of the poset $P$ |
| $\operatorname{End}(P)$ | Monoid of monotone self-maps of $P$ |
| $\operatorname{Sym}(P)$ | Group of all bijections of the underlying set of $P$ |
| $\operatorname{Fix}(f)$ | Fixed-point set of an automorphism $f$ |
| ${\downarrow} x$, ${\uparrow} x$ | Principal ideal and principal filter generated by $x$ |
| $O(P)$ | Family of down-sets (ideals) of $P$, a complete lattice under inclusion |
| $O(f)$ | Automorphism of $O(P)$ induced by $f \in \operatorname{Aut}(P)$, $D \mapsto f(D)$ |
| $\lessdot$ | Cover relation: $x \lessdot y$ with no element strictly between |
| $\mathbb{N}$ | The natural numbers with their usual order, a rigid chain |

## Further Reading

- Garrett Birkhoff, *Lattice Theory*, 3rd ed. (American Mathematical Society, 1967), for the automorphism group of an order, its action on the lattice of ideals and the rigidity of chains.
- Brian A. Davey and Hilary A. Priestley, *Introduction to Lattices and Order*, 2nd ed. (Cambridge University Press, 2002), for order automorphisms, the preservation of joins and meets and the lattice of down-sets.
- Joseph Rosenstein, *Linear Orderings* (Academic Press, 1982), for the automorphism groups of linear orders, the rigid well-orders and the homogeneous dense orders.
- Rudolf Fraïssé, *Theory of Relations*, rev. ed. (North-Holland, 2000), for the automorphism group of a relational structure and the orbits of its action.
- Manfred Droste and Warren B. Powell, "The automorphism group of a linearly ordered set", *Order* **3** (1986), 387–396, for the homogeneity and transitivity of the automorphism groups of dense linear orders.
- Peter M. Neumann, "The structure of the automorphism group of a linearly ordered set", *Journal of the London Mathematical Society* **s2-12** (1976), 348–352, for the classification of the automorphism groups of linear orders.
