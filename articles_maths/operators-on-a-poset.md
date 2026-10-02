
# __Operators on a Poset__

## Introduction

The **operators** on a poset are the maps that respect its order in one way or another, and this
article studies the three kinds that occur throughout the corpus: the **monotone** maps, which carry
the order forward; the **antitone** maps, which reverse it; and the **residuated** maps, which carry
the order forward and have a best possible two-sided inverse in the sense of a **Galois connection**.
The monotone maps form a monoid under composition, and the article examines that monoid: it contains
the identity and every constant map, its pointwise order makes it a lattice when the poset is a
lattice, and its group of units is the automorphism group treated in *The Order Automorphism Group*,
in this group. The antitone maps are organised by the parity of the composite, so that the monotone
and antitone maps together form a monoid in which the monotone maps have index at most two. The
residuated maps are the left adjoints, and a Galois connection is exactly a residuated map together
with its residual; the section proves that a map on a complete lattice is residuated precisely when it
preserves all joins, and it identifies the residuated maps of a power-set lattice with the relations.

The article presupposes *Order Theory and Lattices* — posets, chains, lattices, complete lattices,
monotone maps and the Galois connection, whose definition and elementary properties are recalled
there and used here — and *Sets, Functions and Relations* — sets, functions, relations and their
direct image. The monotone maps of a lattice are the subject of *Operators on a Lattice*, where the
preservation of the two operations is the point; the closure and interior operators are the subject of
*Closure Operators and the Consequence Operator*; the group of units of the monoid of monotone maps is
the subject of *The Order Automorphism Group*; the converse of a relation, which is the residual of the
direct image in the power-set case, is the subject of *The Converse Relation as an Operator*. All four
articles are in this group, and this article supplies the monoid in which they sit.

Three boundaries are observed. No **topology** is used: the order and the composition of maps are the
only tools, and the continuity of a map of a later part is not meant. The theory of **groups** is
*Groups*, in this Part, and only the group of units of a monoid is used. The adjoint of an operator in
the involutive sense, and the reading of the converse as an adjoint, belong to the `* Operator Theory`
group of this category, and are named only; the Galois connection here is the plain order-theoretic
adjunction of *Order Theory and Lattices* and carries no involution. Nothing linear and no **form** is
used.

## Monotone Maps

### The Monoid of Monotone Maps

Let $P$ and $Q$ be posets. A map $f : P \to Q$ is **monotone** if $x \leq y$ implies $f(x) \leq
f(y)$ for all $x, y \in P$. When $P = Q$ the monotone maps are the **endomorphisms** of the order, and
the set of them is written $\operatorname{End}(P)$.

**Theorem.** For a poset $P$ the set $\operatorname{End}(P)$ is a monoid under composition, with
identity $\mathrm{id}_P$, and it is a submonoid of the full transformation monoid $P^P$ of all maps
$P \to P$.

**Proof.** The composite of monotone maps is monotone, because $x \leq y$ gives $f(x) \leq f(y)$ and
then $g(f(x)) \leq g(f(y))$, so $\operatorname{End}(P)$ is closed under composition; composition of
functions is associative and $\mathrm{id}_P$ is monotone, so it is a monoid; and every element of it is
a map $P \to P$.

**Proposition (constants and identity).** For every $k \in P$ the constant map $\kappa_k : x \mapsto
k$ is monotone, so $\operatorname{End}(P)$ contains all $\lvert P \rvert$ constants; every constant is
idempotent, and $\kappa_k$ is a unit of the monoid only when $P$ has one element. The identity is
monotone, and it is the only monotone map that is also a two-sided identity for composition.

**Proof.** A constant map is monotone because the conclusion $k \leq k$ holds for all $x \leq y$. It
is idempotent because $\kappa_k \circ \kappa_k = \kappa_k$. A two-sided inverse of $\kappa_k$ would be
a monotone map $g$ with $g(k) = x$ for every $x$, which forces $P$ to be a single point; and a
two-sided identity is necessarily $\mathrm{id}_P$ by *Sets, Functions and Relations*.

The constants are the reason the monoid is large: they forget the argument and produce a fixed output.
In an operator algebra with an addition the constants play the role of the multiples of the identity;
on a poset there is no addition, and the constants are simply the maps of rank one in the pointwise
order introduced below.

### The Pointwise Order

The set $P^P$ of all self-maps carries the **pointwise order**: $f \leq g$ when $f(x) \leq g(x)$ for
every $x \in P$. The monotone maps are not closed under taking complements in $P^P$, but two closure
properties hold.

**Proposition.** The pointwise order on $\operatorname{End}(P)$ is a partial order, and
$\operatorname{End}(P)$ is closed under the pointwise meet and the pointwise join when those exist in
$P$: if $P$ is a lattice then $f \wedge g$ and $f \vee g$, defined pointwise, are monotone, so
$\operatorname{End}(P)$ is a lattice. If $P$ is a complete lattice then $\operatorname{End}(P)$ is
complete, with joins and meets computed pointwise.

**Proof.** The pointwise order is the restriction of the product order on $P^P$, hence a partial
order. If $f$ and $g$ are monotone and $x \leq y$ then $f(x) \leq f(y)$ and $g(x) \leq g(y)$, so
$f(x) \vee g(x) \leq f(y) \vee g(y)$ whenever the join exists, and likewise for the meet; so the
pointwise operations stay in $\operatorname{End}(P)$. For a complete lattice the same argument applied
to an arbitrary family gives $\bigvee_i f_i$ and $\bigwedge_i f_i$ pointwise.

**Corollary.** The constants are the elements of $\operatorname{End}(P)$ of the form $P \to \{k\}$,
and each constant is both below and above no other constant; two distinct constants are incomparable in
the pointwise order when $P$ is an antichain, and are comparable when $P$ is a chain.

**Proof.** Two constants $\kappa_k, \kappa_l$ satisfy $\kappa_k \leq \kappa_l$ pointwise exactly when
$k \leq l$; so they are comparable exactly when $k$ and $l$ are, which for a chain is always and for an
antichain only when $k = l$.

### Idempotents, Retractions and the Units

**Definition.** A map $e \in \operatorname{End}(P)$ is **idempotent** if $e \circ e = e$; its **image**
$e(P)$ is then the set of its fixed points, and $e$ is a **retraction** of $P$ onto $e(P)$.

**Proposition.** Let $e \in \operatorname{End}(P)$ be idempotent. The image $e(P)$ is a subposet of
$P$, and $e$ is the identity on $e(P)$. If $P$ is a lattice and $e$ preserves the meet and the join,
then $e(P)$ is a sublattice. The idempotent monotone maps that are also extensive are the closure
operators, and those that are also intensive are the interior operators; both are treated in *Closure
Operators and the Consequence Operator*, in this group.

**Proof.** The image is a subposet because $e$ is monotone; an element of the image is $e(x)$, and
$e(e(x)) = e(x)$ by idempotence; so $e$ fixes its image. If $e$ preserves $\wedge$ and $\vee$ then
$e(x) \vee e(y) = e(x \vee y) \in e(P)$ and similarly for the meet, so the image is closed under the
operations.

**Theorem.** The group of units of $\operatorname{End}(P)$ is the order automorphism group
$\operatorname{Aut}(P)$, so a monotone map is invertible in the monoid exactly when it is an order
automorphism.

**Proof.** A two-sided inverse of a map is its inverse function, and $f^{-1}$ is monotone exactly when
$f$ is an order isomorphism; so the units are the order automorphisms. The group is treated in *The
Order Automorphism Group*, in this group.

## Antitone Maps

### Definition and the Parity Monoid

A map $f : P \to Q$ is **antitone** if $x \leq y$ implies $f(y) \leq f(x)$ for all $x, y \in P$. The
antitone self-maps of $P$ are written $\operatorname{Anti}(P)$.

**Proposition.** The composite of two antitone maps is monotone; the composite of a monotone and an
antitone map, in either order, is antitone. Consequently the union
$\operatorname{End}(P) \cup \operatorname{Anti}(P)$ is a monoid under composition, and
$\operatorname{End}(P)$ is a submonoid of index at most two in it.

**Proof.** If $f, g$ are antitone and $x \leq y$ then $f(y) \leq f(x)$, so $g(f(y)) \leq g(f(x))$, and
$g \circ f$ is monotone. If $f$ is monotone and $g$ antitone then $g \circ f$ is antitone, and likewise
$f \circ g$. The union is closed under composition by these two computations and contains
$\mathrm{id}_P$; the antitone maps form a coset of $\operatorname{End}(P)$ when there is at least one
antitone map, so the index is one or two.

**Corollary.** The square $f \circ f$ of an antitone map is monotone. An antitone map that is a
bijection and has order two is an **order-reversing involution**; its fixed-point set consists of the
elements comparable with all their images, and the order-reversing involutions of a poset are the
antitone maps $f$ with $f^2 = \mathrm{id}_P$ and $f$ bijective.

**Proof.** The square is a composite of two antitone maps, hence monotone, by the proposition. The
remaining statements are the definitions.

An order-reversing involution on a lattice is the structure read with an involution on its elements,
and it is the subject of *Orthocomplemented Lattices and the Involution*, in the `* Theory` group of
this category. Here only its place in the parity monoid is recorded.

### Reduction to the Opposite Poset

Let $P^{\mathrm{op}}$ denote $P$ with the opposite order, in which $x \leq^{\mathrm{op}} y$ means $y
\leq x$.

**Proposition.** A map $f : P \to Q$ is antitone if and only if it is monotone as a map $P \to
Q^{\mathrm{op}}$, equivalently as a map $P^{\mathrm{op}} \to Q$. Hence the antitone maps are the
monotone maps of the opposite order, and an antitone bijection $P \to P$ is an order isomorphism $P
\to P^{\mathrm{op}}$, that is, an isomorphism of $P$ with its opposite poset.

**Proof.** The condition $x \leq y \Rightarrow f(y) \leq f(x)$ is exactly $x \leq y \Rightarrow
f(x) \leq^{\mathrm{op}} f(y)$. The statements about bijections are the definition of an isomorphism of
posets.

So nothing new is needed for the antitone maps beyond the duality principle of *Order Theory and
Lattices*: their theory is the theory of the monotone maps of the opposite order. In particular
$\operatorname{Anti}(P) \cong \operatorname{End}(P^{\mathrm{op}})$ as sets, and the parity monoid of
the previous subsection is the set of monotone maps of $P$ and of $P^{\mathrm{op}}$ together.

## Residuated Maps and Galois Connections

### Residuated Pairs

**Definition.** A monotone map $f : P \to Q$ is **residuated**, with **residual** $g : Q \to P$, if

$$
f(p) \leq q \quad\Longleftrightarrow\quad p \leq g(q) \qquad \text{for all } p \in P, q \in Q .
$$

Equivalently, the pair $f \dashv g$ is a **Galois connection** between $P$ and $Q$ in the sense of
*Order Theory and Lattices*, with $f$ the **left adjoint** and $g$ the **right adjoint**. The
residual, when it exists, is unique, and it is written $f^{\sharp}$ when the dependence on $f$ is the
only one in view.

**Proposition.** If $f$ is residuated with residual $g$, then $g$ is monotone, $p \leq g(f(p))$ for all
$p$, $f(g(q)) \leq q$ for all $q$, and $f = f g f$ and $g = g f g$. The maps $g f$ and $f g$ are a
closure operator on $P$ and an interior operator on $Q$ respectively. A residuated map with residual
$g$ is injective exactly when $g f = \mathrm{id}_P$, and surjective exactly when $f g = \mathrm{id}_Q$.

**Proof.** These are the elementary properties of a Galois connection established in *Order Theory and
Lattices*: monotonicity of the right adjoint, the two unit and counit inequalities, the triangle
identities, and the closure and interior properties. For injectivity, $f(p) = f(p')$ gives $p = g(f(p))
= g(f(p')) = p'$ when $gf = \mathrm{id}_P$, and conversely $gf = \mathrm{id}_P$ follows from
injectivity because $p \leq g(f(p))$ and $f(p) = f(g(f(p)))$ gives $g(f(p)) = p$; surjectivity is dual.

**Theorem.** Let $P$ be a complete lattice. A monotone map $f : P \to Q$ is residuated if and only if
it preserves all joins: $f(\bigvee_i p_i) = \bigvee_i f(p_i)$ for every family in $P$. In that case the
residual is given by

$$
g(q) = \bigvee \{p \in P : f(p) \leq q\}.
$$

**Proof.** If $f$ is residuated then it preserves joins, by *Order Theory and Lattices*. Conversely, if
$f$ preserves all joins, define $g(q) = \bigvee\{p : f(p) \leq q\}$, which exists because $P$ is
complete. Then $f(p) \leq q$ implies $p \leq g(q)$ by definition of the join; and $p \leq g(q)$ gives
$f(p) \leq f(g(q)) = \bigvee\{f(p') : f(p') \leq q\} \leq q$, using the preservation of joins. So $f
\dashv g$.

**Corollary.** On a complete lattice, the residuated maps into a poset are exactly the join-preserving
maps, and the residual is the greatest $p$ with $f(p) \leq q$. The composite of two residuated maps is
residuated, with residual the composite of the residuals in the reverse order; and the identity is
residuated, with itself as residual. Hence the residuated maps $P \to P$ form a submonoid of
$\operatorname{End}(P)$.

**Proof.** The characterisation of the residual and the composition law $(f_2 f_1)^{\sharp} = f_1^{\sharp}
f_2^{\sharp}$ are the composition of adjunctions for posets, in *Order Theory and Lattices*, restated in
the language of residuals.

### The Galois Connection as a Pair of Residuated Maps

A Galois connection $f \dashv g$ is exactly a residuated pair: $f$ is the residuated map and $g$ its
residual. Read from the other side, $g$ is a map whose opposite is residuated, and one says that $g$ is
the **right adjoint**; the pair is a single datum with two equivalent descriptions. The two composites
$g f$ and $f g$ are the closure operator and the interior operator of the connection, and the closed
elements of $g f$ are the image of $g$, the open elements of $f g$ the image of $f$; this is the
content of *Closure Operators and the Consequence Operator*, in this group, and is not repeated.

**Example.** The relation-induced Galois connection of *Order Theory and Lattices* is the standard
source of residuated pairs: a relation $R \subseteq X \times Y$ gives the antitone maps $A \mapsto
A^{\uparrow}$ and $B \mapsto B^{\downarrow}$, and the induced maps $A \mapsto A^{\uparrow\downarrow}$
and $B \mapsto B^{\downarrow\uparrow}$ are closure operators. In the language of this article the two
maps are the residuals of each other for the opposite orders, and the polarities are the residuated
pairs between $\mathcal{P}(X)^{\mathrm{op}}$ and $\mathcal{P}(Y)^{\mathrm{op}}$.

### The Residuated Maps of a Power Set

**Theorem.** Let $X$ and $Y$ be sets. A map $f : \mathcal{P}(X) \to \mathcal{P}(Y)$ is residuated if
and only if it preserves arbitrary unions, and then there is a unique relation $R \subseteq X \times
Y$ with

$$
f(A) = R[A] = \{y \in Y : (x,y) \in R \text{ for some } x \in A\}, \qquad
g(B) = \{x \in X : (x,y) \in R \Rightarrow y \in B\},
$$

where $g$ is the residual of $f$. Hence the residuated maps $\mathcal{P}(X) \to \mathcal{P}(Y)$ are in
bijection with the relations $X \to Y$, and the residual is the map that sends $B$ to the set of
points all of whose $R$-relatives lie in $B$.

**Proof.** A map out of a complete lattice is residuated exactly when it preserves joins, and the join
in $\mathcal{P}(X)$ is the union, so $f(A) = f(\bigcup_{x \in A}\{x\}) = \bigcup_{x \in A} f(\{x\})$.
Put $R = \{(x,y) : y \in f(\{x\})\}$; the relation is determined by $f$ and determines it, and the
displayed formula for $f$ follows. By the theorem on residuals, $g(B) = \bigcup\{A : f(A) \subseteq
B\}$. Now $f(A) \subseteq B$ holds if and only if $f(\{x\}) \subseteq B$ for every $x \in A$, that is,
$R[\{x\}] \subseteq B$ for every $x \in A$. It follows that the union $\bigcup\{A : f(A) \subseteq
B\}$ is the set of $x$ with $R[\{x\}] \subseteq B$, which is the displayed set of points all of whose
$R$-relatives lie in $B$.

**Corollary.** The direct image of a relation and its residual are the two maps of a Galois connection
between the power-set lattices, and they are inverse to each other on the level of the relation: the
map $f \mapsto R$ of the theorem is a bijection, so the residuated maps of a power set are exactly the
direct images of relations and nothing else is needed to describe them.

## Summary

The monotone self-maps of a poset form the monoid $\operatorname{End}(P)$, a submonoid of the full
transformation monoid $P^P$, containing the identity and all constants; under the pointwise order it
is a lattice when $P$ is a lattice and complete when $P$ is complete; its idempotents are the
retractions and its units are the order automorphisms. The antitone maps together with the monotone
ones form a monoid $\operatorname{End}(P) \cup \operatorname{Anti}(P)$ in which the parity of the
composite is additive, and the antitone maps are exactly the monotone maps of the opposite order.

A residuated map is a left adjoint, and a Galois connection is a residuated map together with its
residual; on a complete lattice the residuated maps are exactly the join-preserving maps, the residual
is unique and is the greatest preimage, and the residuated self-maps form a submonoid of
$\operatorname{End}(P)$. For a power-set lattice a residuated map is exactly the direct image of a
relation, and its residual is the map sending a set to the points all of whose relatives lie in it.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{End}(P)$ | Monoid of monotone self-maps of $P$ under composition |
| $P^P$ | Full transformation monoid of all self-maps of $P$ |
| $\kappa_k$ | Constant map $x \mapsto k$ |
| $\operatorname{Anti}(P)$ | Set of antitone self-maps of $P$ |
| $\operatorname{End}(P) \cup \operatorname{Anti}(P)$ | Parity monoid: monotone and antitone maps |
| $P^{\mathrm{op}}$ | $P$ with the opposite order |
| $f \dashv g$ | Galois connection: $f$ left adjoint (residuated), $g$ right adjoint (residual) |
| $f^{\sharp}$ | Residual of a residuated map $f$ |
| $R[A]$ | Direct image of $A$ under the relation $R$ |
| $g(B) = \{x : (x,y) \in R \Rightarrow y \in B\}$ | Residual of the direct image |

## Further Reading

- Garrett Birkhoff, *Lattice Theory*, 3rd ed. (American Mathematical Society, 1967), for residuated maps, their characterisation by the preservation of joins, and the monoid of monotone maps.
- Brian A. Davey and Hilary A. Priestley, *Introduction to Lattices and Order*, 2nd ed. (Cambridge University Press, 2002), for Galois connections, residuated pairs and the pointwise order on the monotone maps.
- Peter T. Johnstone, *Stone Spaces* (Cambridge University Press, 1982), for residuated maps, the residual of a join-preserving map and the identification with relations in the power-set case.
- Marcel Erné, "The ABC of order and topology", in *Category Theory at Work* (Heldermann, 1991), for the lattice of monotone maps and its operators.
- Rudolf Fraïssé, *Theory of Relations*, rev. ed. (North-Holland, 2000), for relations, their direct images and residuals and the Galois connections they induce.
- Chris Brink, Wolfram Kahl and Gunther Schmidt, eds., *Relational Methods in Computer Science* (Springer, 1997), for residuated maps of power sets and their identification with relations.
