
# __Orthocomplemented Lattices and the Involution__

## Introduction

A **complement** of an element $x$ of a bounded lattice is an element $y$ with $x \wedge y = 0$ and $x
\vee y = 1$, and in a general lattice an element may have no complement or many. A lattice is
**orthocomplemented** when the complement can be chosen for every element in a way that is a
**involution** on the elements: a map $x \mapsto x^{\perp}$ of order two that reverses the order. This
article studies that involution and the structure it defines. It first records why the bare complement
fails in a general lattice — it need be neither unique nor always present, and a complemented lattice
need not carry an orthocomplement — then isolates the **orthocomplement** by the properties that make
it an order-reversing involution with $x \wedge x^{\perp} = 0$, proves the **De Morgan laws** from the
involution alone, and shows that a weaker map, a **semiorthocomplement**, is a genuine weakening only
on a lattice with no greatest element. The resulting structure, the **ortholattice**, is the lattice
read with an involution on its elements, and it is the base of *Orthomodular Lattices*, which follows
in this group.

The article presupposes *Order Theory and Lattices* — posets, lattices, bounded and complete
lattices, the distributive and modular laws, the complement in a bounded lattice, and the duality
principle — and *Operators on a Poset*, in this group — antitone maps, order-reversing involutions and
the parity monoid, of which the orthocomplement is the bijective order-two case. The **Boolean**
case, in which the complement is unique and the lattice distributive, is *Boolean Algebras with an
Involution*, later in this group, and the general Boolean algebra is *Boolean Algebras and Lattices*,
in Part V; both are named only. The orthocomplement of the **projection lattice** of a Hilbert space
is a forward reference to Part II and is not defined or used here.

Three boundaries are observed. No **topology** is used and no **form** is formed: the orthogonal
complement of a Hilbert space is named in *Orthomodular Lattices* and deferred, and nothing here is
measured. The theory of **groups** is *Groups*, in this Part; the lattice is read with its order and
its two operations alone. The adjoint of an operator, and the reading of the orthocomplement through
the operator layer, belong to the `* Operator Theory` group of this category and are named only.

## Complemented Lattices

### The Complement and its Failure

Let $L$ be a bounded lattice with least element $0$ and greatest element $1$.

**Definition.** A **complement** of $x \in L$ is an element $y \in L$ with $x \wedge y = 0$ and $x \vee
y = 1$. The lattice is **complemented** if every element has a complement.

**Proposition (failure of uniqueness).** In a general lattice a complement need not be unique. In the
five-element lattice $M_3$ with bottom $0$, top $1$ and three pairwise incomparable atoms $a, b, c$,
the element $a$ has the two complements $b$ and $c$; so $M_3$ is complemented and its complementation
is not a map.

**Proof.** In $M_3$ one has $a \wedge b = 0$ and $a \vee b = 1$, and likewise with $c$ in place of $b$,
so both $b$ and $c$ are complements of $a$; and $b \neq c$.

**Proposition (a complementation is a choice).** A choice of one complement for each element of a
complemented lattice is an arbitrary function on the lattice, not determined by the order; two
different choices may disagree on the same element. In $M_3$ the atom $a$ has the two complements $b$
and $c$, so two complementations of $M_3$ differ on $a$.

**Proof.** The two complements $b, c$ of $a$ are distinct, so the two functions that choose $b$ and
$c$ for $a$ differ; both satisfy the complement law at every element, since every atom is a complement
of every other atom and $0$ and $1$ are complementary.

The definition that follows is the way to make the complement canonical: the two extra requirements,
that the map be an involution and that it reverse the order, force it to be unique, and they are not
automatic. A complemented lattice need not carry any such map, and the clearest obstruction is a
cardinality one.

**Proposition (no orthocomplement in $M_3$).** In a nondegenerate lattice an order-reversing involution
with $x \wedge x^{\perp} = 0$ for all $x$ is fixed-point-free, so the lattice has even cardinality;
hence no lattice of odd cardinality greater than one is orthocomplemented. In particular $M_3$, which
has five elements, is complemented and carries no orthocomplement: an involution of the three atoms
would have to fix one of them, and a fixed atom $a$ satisfies $a \wedge a^{\perp} = a \neq 0$.

**Proof.** The map is an order-reversing bijection, so it carries the least element to the greatest,
$0^{\perp} = 1$. If $x = x^{\perp}$ then $x \wedge x^{\perp} = x$, so $x = 0$ by the complement law;
and $0 = 0^{\perp} = 1$, so the lattice is a single point. Hence in a nondegenerate lattice the
involution has no fixed point, it pairs the elements, and the cardinality is even. For $M_3$ the
involution permutes the three atoms, every permutation of a three-element set has a fixed point, and a
fixed atom is a fixed point of the involution, which is impossible.

### The Orthocomplement

**Definition.** An **orthocomplement** on $L$ is a map ${}^{\perp} : L \to L$ with

$$
x^{\perp\perp} = x, \qquad x \leq y \Rightarrow y^{\perp} \leq x^{\perp}, \qquad
x \wedge x^{\perp} = 0, \qquad x \vee x^{\perp} = 1
$$

for all $x, y \in L$. An **ortholattice** is a bounded lattice together with an orthocomplement; an
**orthoposet** is a poset with an order-reversing involution, no meet or join being required.

The first two conditions say that ${}^{\perp}$ is an **order-reversing involution**, equivalently an
order isomorphism $L \to L^{\mathrm{op}}$ of order two, in the sense of *Operators on a Poset*; the
last two say that it is a complement.

**Proposition.** An orthocomplement is unique when it exists. It satisfies $0^{\perp} = 1$ and
$1^{\perp} = 0$.

**Proof.** If ${}^{\perp}$ and ${}^{\prime}$ are orthocomplements and $x \in L$, then from $x^{\perp}
\wedge x = 0$ one gets $x^{\prime} \leq (x^{\perp})^{\perp} = x$ by the order reversal and the
complement laws applied to $x^{\perp}$; symmetrically $x^{\perp} \leq x^{\prime}$; so $x^{\perp} =
x^{\prime}$ and the two maps agree. For the bounds, $0 \wedge 0^{\perp} = 0$ gives $0^{\perp} \geq 0$,
and $0 \vee 0^{\perp} = 1$ gives $0^{\perp} = 1$ because $0^{\perp}$ is an upper bound of $0$ equal to
the join; dually $1^{\perp} = 0$.

**Proposition (no fixed points, nondegenerate case).** If $x = x^{\perp}$ then $x \wedge x^{\perp} =
x$, so $x = 0$, and $x \vee x^{\perp} = x$, so $x = 1$; hence $0 = 1$ and the lattice is a single
point. In a nondegenerate ortholattice the involution is fixed-point-free.

**Proof.** Substitute $x = x^{\perp}$ in the two complement laws, which become $x \wedge x = 0$ and $x
\vee x = 1$, that is, $x = 0$ and $x = 1$.

**Example (the power set).** The power-set lattice $\mathcal{P}(X)$ with the set complement $A^{\perp}
= X \setminus A$ is an ortholattice: the complement is an involution, reverses inclusion, and $A \cap
A^{\perp} = \emptyset$, $A \cup A^{\perp} = X$. It is **Boolean**, its orthocomplement is its unique
complementation, and the general Boolean case is treated in *Boolean Algebras with an Involution*,
later in this group.

**Example (the smallest ortholattice).** The smallest nondegenerate ortholattice is the Boolean
lattice $B_2$ on four elements $\{0, a, b, 1\}$ with $a^{\perp} = b$ and $b^{\perp} = a$, the unique
complementation of $B_2$. Every nondegenerate ortholattice has even cardinality, so no lattice of odd
cardinality is orthocomplemented; $M_3$ is complemented and, having five elements, is not.

## The De Morgan Laws

**Theorem.** In an ortholattice $L$ the involution satisfies the **De Morgan laws**

$$
(x \wedge y)^{\perp} = x^{\perp} \vee y^{\perp}, \qquad (x \vee y)^{\perp} = x^{\perp} \wedge y^{\perp}
\qquad \text{for all } x, y \in L .
$$

**Proof.** Let $u = x^{\perp} \vee y^{\perp}$. Since $x \wedge y \leq x$ and $x \wedge y \leq y$, the
order reversal gives $(x \wedge y)^{\perp} \geq x^{\perp}$ and $(x \wedge y)^{\perp} \geq y^{\perp}$,
so $(x \wedge y)^{\perp} \geq u$. Conversely let $v$ be any upper bound of $x^{\perp}$ and $y^{\perp}$;
then $v^{\perp} \leq x$ and $v^{\perp} \leq y$ by the order reversal applied to $x^{\perp} \leq v$ and
$y^{\perp} \leq v$, so $v^{\perp} \leq x \wedge y$, and applying the order reversal again gives $v \geq
(x \wedge y)^{\perp}$. Hence $(x \wedge y)^{\perp}$ is the least upper bound $u$. The second law is the
same argument with the roles of the two bounds exchanged, or the first law applied to $x^{\perp}$ and
$y^{\perp}$ and then the involution.

**Corollary.** The two De Morgan laws are equivalent for an order-reversing involution, and each of
them together with the involution determines the other; the involution alone already forces both, so no
distributivity is needed. In a complete ortholattice the laws extend to arbitrary families,
$(\bigwedge_i x_i)^{\perp} = \bigvee_i x_i^{\perp}$ and $(\bigvee_i x_i)^{\perp} = \bigwedge_i
x_i^{\perp}$.

**Proof.** The argument of the theorem uses only that the map is an order-reversing involution, not
the complement laws. The infinitary statement is the same argument with the arbitrary join in place of
the binary one, and it uses the completeness to form the bounds.

The De Morgan laws are the arithmetic of the involution: they say that ${}^{\perp}$ exchanges the meet
and the join. With $0^{\perp} = 1$ and $1^{\perp} = 0$ they make the involution an isomorphism of the
ortholattice with its opposite, and the opposite of an ortholattice is the same ortholattice with the
same involution.

## Semiorthocomplements

A lattice may have a least element and still fail to be bounded, and the notion that follows is the
involution one half of a complement on such a lattice.

**Definition.** Let $L$ be a lattice with least element $0$. A **semiorthocomplement** on $L$ is a map
${}^{\perp} : L \to L$ that is an order-reversing involution and satisfies

$$
x \wedge x^{\perp} = 0 \qquad \text{for all } x \in L .
$$

No greatest element is required, and the join $x \vee x^{\perp}$ is not required to be a top.

**Theorem.** Let ${}^{\perp}$ be a semiorthocomplement on $L$. Then for every $x \in L$,

$$
(x \vee x^{\perp})^{\perp} = x^{\perp} \wedge x = 0, \qquad x \vee x^{\perp} = 0^{\perp},
$$

so the element $x \vee x^{\perp}$ is the same for all $x$. If $L$ has a greatest element $1$, then
$1 \vee 1^{\perp} = 1 = 0^{\perp}$, the four defining identities of an orthocomplement hold, and $L$
is an ortholattice.

**Proof.** By the De Morgan theorem, which uses only that the map is an order-reversing involution,
$(x \vee x^{\perp})^{\perp} = x^{\perp} \wedge x^{\perp\perp} = x^{\perp} \wedge x = 0$; applying the
involution to both sides gives $x \vee x^{\perp} = 0^{\perp}$, since $0^{\perp\perp} = 0$. So the join
is independent of $x$ and equals $0^{\perp}$. If a greatest element $1$ exists, then taking $x = 1$
gives $0^{\perp} = 1 \vee 1^{\perp} = 1$, so $x \vee x^{\perp} = 1$ for every $x$ and the complement
laws hold.

**Corollary.** A lattice with a semiorthocomplement has a **thin** element $t = 0^{\perp} = x \vee
x^{\perp}$, the same for every $x$, with $t^{\perp} = 0$. On the interval $[0, t]$ the map ${}^{\perp}$
restricts to an orthocomplement of the sublattice of elements below $t$, which is the largest
orthocomplemented part of $L$; and if $L$ is bounded, then $t = 1$ and $L$ is itself an ortholattice.

**Proof.** The element $t$ is fixed by the theorem, and $t^{\perp} = (0^{\perp})^{\perp} = 0$. For $x
\leq t$ one has $x^{\perp} \geq t^{\perp} = 0$; the identities $x \vee x^{\perp} = t$ and $x \wedge
x^{\perp} = 0$ give the complement laws on $[0, t]$, and the involution restricts to an involution
there.

**Remark (the weakening is not visible in a bounded lattice).** The theorem shows that a
semiorthocomplement on a bounded lattice is already an orthocomplement, so the notion is strictly
weaker than the orthocomplement only on a lattice that has a least element and no greatest element.
A finite lattice is bounded, its greatest element being the join of all its elements, so a strict
example is infinite; the thin element $t$ then plays the role the top would play, and the interval
$[0, t]$ is the largest orthocomplemented part.

## Summary

A complement of an element of a bounded lattice is an element with the two complement laws; it need
not be unique, a choice of complements is not determined by the order, and a complemented lattice need
not carry an orthocomplement at all: the orthocomplement is fixed-point-free, so a nondegenerate
ortholattice has even cardinality, and $M_3$, with five elements, is complemented and not
orthocomplemented. An orthocomplement is a map that is an order-reversing involution and a complement;
it is unique when it exists and it exchanges $0$ and $1$. The structure it defines, the ortholattice,
satisfies both De Morgan laws, and those laws follow from the involution alone, with no distributivity.

A semiorthocomplement is an order-reversing involution with $x \wedge x^{\perp} = 0$ on a lattice that
need only have a least element; for it the join $x \vee x^{\perp}$ is the same thin element $t =
0^{\perp}$ for every $x$. On a bounded lattice $t = 1$ and a semiorthocomplement is already an
orthocomplement, so the notion is a strict weakening only without a greatest element, and the interval
$[0,t]$ is then the largest orthocomplemented part. The Boolean case, in which the complement is
unique, and the projection lattice of a Hilbert space, in which the orthocomplement is the orthogonal
complement, are the subject of *Boolean Algebras with an Involution*, later in this group, and of Part
II respectively.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L$, $0$, $1$ | Bounded lattice, with least and greatest element |
| $x^{\perp}$ | Orthocomplement of $x$: an order-reversing involution with $x \wedge x^{\perp} = 0$, $x \vee x^{\perp} = 1$ |
| ${}^{\perp}$ | The involution on the elements of an ortholattice |
| $M_3$ | The five-element lattice with three atoms, complemented but not orthocomplemented |
| $x'$, $y'$ | Arbitrary complements of $x$, $y$ in a complemented lattice |
| $t = 0^{\perp}$ | The thin element of a lattice with a semiorthocomplement, $t = x \vee x^{\perp}$ |
| $[0, t]$ | The largest orthocomplemented part of a semiorthocomplemented lattice |

## Further Reading

- Garrett Birkhoff, *Lattice Theory*, 3rd ed. (American Mathematical Society, 1967), for complemented, orthocomplemented and orthomodular lattices, the De Morgan laws and the failure of the complement.
- Gudrun Kalmbach, *Orthomodular Lattices* (Academic Press, 1983), for orthocomplementation, the semiorthocomplement and the structure of ortholattices.
- Laszlo Fuchs, *Partially Ordered Algebraic Systems* (Pergamon Press, 1963), for orthocomplemented posets and the order-reversing involution.
- Peter G. Vámos, "The structure of semi-orthocomplemented lattices", *Acta Mathematica Academiae Scientiarum Hungaricae* **11** (1960), 115–120, for the thin element and the largest orthocomplemented part.
- George Grätzer, *General Lattice Theory*, 2nd ed. (Birkhäuser, 1998), for the complement in a bounded lattice, $M_3$ and the modular and distributive laws.
