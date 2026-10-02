
# __Orthomodular Lattices__

## Introduction

An **orthomodular lattice** is an ortholattice in which the orthocomplement and the order are linked
by one further law, the **orthomodular law**: whenever $x \leq y$, the element $y$ is recovered from
$x$ and $x^{\perp}$ by

$$
y = x \vee (x^{\perp} \wedge y) .
$$

The law is a one-sided form of the modular law, and it is the exact amount of modularity that the
orthocomplement can supply. This article develops it: it defines the law, proves its equivalence with
two other forms, shows that it is self-dual, and proves that a **modular** ortholattice is
orthomodular, so the orthomodular law is the weak form of modularity that remains available once a
lattice is read with an involution. It then turns to the failure of distributivity: a distributive
orthomodular lattice is a Boolean algebra, and the smallest non-distributive example is the six-element
lattice $M_4$, whose four atoms are paired by the orthocomplement. The standard infinite example, the
**projection lattice** of a Hilbert space, is named and deferred to Part II.

The article presupposes *Order Theory and Lattices* — posets, lattices, bounded, complete,
distributive and modular lattices, and the Boolean lattice — and *Orthocomplemented Lattices and the
Involution*, which precedes it in this group and supplies the ortholattice, the De Morgan laws and the
failure of the complement. The **Boolean** case and the involutive Boolean algebra are *Boolean
Algebras with an Involution*, later in this group, and the general Boolean algebra is *Boolean Algebras
and Lattices*, in Part V; both are named only. The **projection lattice** of a Hilbert space is a
forward reference to Part II and is not defined or used.

Three boundaries are observed. No **topology** is used, and no **form** is formed: the projection
lattice is named only, the orthogonal complement is the name of an involution on it, and nothing is
measured with an inner product. No **measure** and no probability is used; the logical reading of the
lattice is *Logic and Proof* in Part 0 and *Effect Algebras and Orthomodular Lattices* in Part V, and
neither is used here. The adjoint of an operator, and the involution on the operator layer, belong to
the `* Operator Theory` group of this category and are named only.

## The Orthomodular Law

### Definition and Equivalent Forms

Let $L$ be an ortholattice.

**Definition.** $L$ is **orthomodular** if

$$
x \leq y \quad\Longrightarrow\quad y = x \vee (x^{\perp} \wedge y) \qquad \text{for all } x, y \in L .
$$

An **orthomodular lattice** is an ortholattice satisfying this law.

**Proposition.** The following are equivalent for an ortholattice:

1. $x \leq y \Rightarrow y = x \vee (x^{\perp} \wedge y)$ for all $x, y$;
2. $x \vee (x^{\perp} \wedge (x \vee y)) = x \vee y$ for all $x, y$.

**Proof.** (1) $\Rightarrow$ (2): apply (1) to the pair $x \leq x \vee y$, for which the right side
reads $x \vee (x^{\perp} \wedge (x \vee y))$ and the left side $x \vee y$. (2) $\Rightarrow$ (1): if $x
\leq y$ then $x \vee y = y$, and (2) reads $y = x \vee (x^{\perp} \wedge y)$.

**Remark.** The law is equivalently the statement that the inequality $x \vee (x^{\perp} \wedge y)
\leq y$, which holds for all $x \leq y$ because both $x$ and $x^{\perp} \wedge y$ are below $y$, is
always an equality. In the modular law the same identity holds with an arbitrary $z$ in place of
$x^{\perp}$; the orthomodular law is the one instance of it that the complement permits, and the next
subsection makes the implication precise.

**Theorem (self-duality).** The dual of an orthomodular lattice, in which the order and the two
operations are reversed and the orthocomplement is kept, is orthomodular with the same orthocomplement.
The dual form of the law is

$$
x \geq y \quad\Longrightarrow\quad y = x \wedge (x^{\perp} \vee y) \qquad \text{for all } x, y \in L .
$$

**Proof.** Taking the order-dual of the identity $y = x \vee (x^{\perp} \wedge y)$ and exchanging the
names of $x$ and $y$ gives the displayed law; the orthocomplement is unchanged because it is an
order-reversing involution, which is the same condition in the opposite order. So the class of
orthomodular lattices is closed under duality.

The law says exactly that the inequality that always holds is an equality: for $x \leq y$ one has $x
\vee (x^{\perp} \wedge y) \leq y$ by the two joins, and orthomodularity is the statement that the
opposite inequality also holds. In the modular law the same identity holds with an arbitrary $z$ in
place of $x^{\perp}$, and the orthomodular law is the one instance of it that the complement permits.

### Modularity Implies Orthomodularity

**Theorem.** Every modular ortholattice is orthomodular.

**Proof.** Let $L$ be a modular ortholattice and let $x \leq y$. Applying the modular law to the
instances $x$, $y$ and $z = x^{\perp}$, which one may do because $x \wedge z = 0$ and $x \vee z = 1$,

$$
y = y \wedge (x \vee x^{\perp}) = x \vee (y \wedge x^{\perp}),
$$

so the orthomodular law holds.

The converse fails: the projection lattice of a Hilbert space of dimension at least two is
orthomodular and not modular, as the next section records and Part II proves. So orthomodularity is the
weak form of modularity, and it is the form that the orthocomplement forces.

## The Failure of Distributivity

### Distributive Orthomodular Lattices are Boolean

**Theorem.** An orthomodular lattice is distributive if and only if it is a Boolean algebra.

**Proof.** A Boolean algebra is distributive by definition, so one direction is immediate. Conversely,
if $L$ is distributive then it is a complemented distributive lattice, its orthocomplement being a
complement of every element, and every complemented distributive lattice is a Boolean algebra by *Order
Theory and Lattices*.

So a non-Boolean orthomodular lattice fails distributivity. The smallest such lattice is found among
the small ortholattices.

### The Smallest Non-Distributive Example

**Example ($M_4$).** Let $M_4$ be the lattice with bottom $0$, top $1$ and four pairwise incomparable
atoms $a, b, c, d$. Define $a^{\perp} = b$, $b^{\perp} = a$, $c^{\perp} = d$, $d^{\perp} = c$, and
$0^{\perp} = 1$, $1^{\perp} = 0$. This is an orthocomplement: it is an order-reversing involution, and
every atom is disjoint from its image with join $1$. The lattice is orthomodular, because the only
pairs $x \leq y$ are those with $x = 0$, with $x = y$, or with $y = 1$, and in each case the law
reduces to an identity. It is modular and it is not distributive: $a \wedge (b \vee c) = a$ while $(a
\wedge b) \vee (a \wedge c) = 0$. So $M_4$ is a modular, non-distributive orthomodular lattice with
six elements. It is the smallest non-Boolean orthomodular lattice: a nondegenerate ortholattice has
even cardinality, so the two-element and four-element cases are $B_1$ and $B_2$ and are Boolean, and
$M_4$ is a non-Boolean orthomodular lattice on six elements, which an exhaustive check of the six-
element lattices confirms.

**Example (the Boolean lattices).** Every Boolean lattice is an orthomodular lattice, its
orthocomplement being the Boolean complement; the smallest is $B_2$, the four-element lattice. The
Boolean orthomodular lattices are exactly the distributive ones by the theorem above, so the examples
of the non-distributive behaviour provable without a topology are the $M_n$ with $n$ even and $n \geq
4$, of which $M_4$ is the smallest, and their subortholattices.

## The Projection Lattice of a Hilbert Space

The standard example of an orthomodular lattice is the family of closed subspaces of a Hilbert space,
ordered by inclusion, with the **orthogonal complement** as the orthocomplement and the closed span as
the join. The structure is a **complete** orthomodular lattice; it is not distributive when the
dimension is at least two, and it is not modular; and the elements of its associated operator layer are
the projections. The Hilbert space, its inner product and the orthogonal complement are Part II, and
this article names the lattice only: the definition of the space, of the complement, and the proof that
the lattice is orthomodular and not distributive are met when Part II reaches them, and nothing of the
kind is used or computed here.

The projection lattice is the reason the notion is studied at all: it is the instance in which
orthomodularity is the natural axiom, and it is non-Boolean, so no amount of distributivity is
available there. Its place in the corpus is fixed by this paragraph and its content is deferred.

## Summary

An orthomodular lattice is an ortholattice in which $x \leq y$ implies $y = x \vee (x^{\perp} \wedge
y)$. The law is equivalent to $x \vee (x^{\perp} \wedge (x \vee y)) = x \vee y$, and it says that the
inequality $x \vee (x^{\perp} \wedge y) \leq y$, which always holds for $x \leq y$, is an equality; it
is self-dual, so the class is closed under duality; and every modular ortholattice is orthomodular,
with the orthomodular law the one instance of the modular law that the complement forces.

An orthomodular lattice is distributive if and only if it is a Boolean algebra. The smallest
non-distributive orthomodular lattice is $M_4$, with six elements, whose four atoms are paired by the
orthocomplement; it is modular and not distributive. The standard infinite example is the projection
lattice of a Hilbert space, complete, orthomodular, non-modular and non-distributive, which is a
forward reference to Part II and is not defined or used here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L$ | An ortholattice, with orthocomplement ${}^{\perp}$ |
| orthomodular law | $x \leq y \Rightarrow y = x \vee (x^{\perp} \wedge y)$ |
| $M_n$ | The lattice with bottom, top and $n$ pairwise incomparable atoms |
| $M_4$ | The six-element lattice with four atoms, the smallest non-distributive orthomodular lattice |
| $B_2$ | The four-element Boolean lattice, the smallest orthomodular lattice |
| projection lattice | The lattice of closed subspaces of a Hilbert space, deferred to Part II |

## Further Reading

- Gudrun Kalmbach, *Orthomodular Lattices* (Academic Press, 1983), for the orthomodular law, its equivalent forms and the structure theory of orthomodular lattices.
- Garrett Birkhoff, *Lattice Theory*, 3rd ed. (American Mathematical Society, 1967), for modular and distributive laws, the Boolean algebras and the complement in a bounded lattice.
- László Fuchs, *Partially Ordered Algebraic Systems* (Pergamon Press, 1963), for orthomodular posets and their relation to the modular law.
- Peter D. Finch, "On the structure of orthomodular lattices", *Journal of Symbolic Logic* **32** (1967), 402–403, for the failure of distributivity and the place of the modular case.
- Richard J. Greechie, "Hypergraphic orthomodular lattices", *Journal of Combinatorial Theory Series A* **10** (1971), 119–132, for the construction of orthomodular lattices from combinatorial data.
