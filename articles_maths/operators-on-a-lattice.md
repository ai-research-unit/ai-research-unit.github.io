
# __Operators on a Lattice__

## Introduction

A lattice is a set carrying two binary operations, the meet and the join, and the maps that respect
those operations are the **operators** of the lattice. This article studies them. It defines the
lattice maps — the join-preserving, the meet-preserving and the fully preserving ones — and shows
where the three notions separate; it collects the endomorphisms of a lattice into a monoid whose
group of units is the automorphism group; it reads a **congruence** as the kernel of a
lattice homomorphism, constructs the quotient, and proves the first isomorphism theorem for
lattices; and it studies the family of congruences as a lattice in its own right, distributive by
the theorem of Funayama and Nakayama, and reads the lattice back through its operator layer.

The article presupposes *Order Theory and Lattices* — posets, lattices, the meet and the join, the
complete lattice and the sublattice — and the language of *Sets, Functions and Relations* —
relations, equivalence relations, quotients and functions. It uses no number system beyond the
two-element lattice, and no structure from a later category.

Three boundaries are observed. Nothing topological or metric is used: order-completeness is the
order-theoretic completeness of *Order Theory and Lattices* and is not the metric completeness of a
later part. No **form** and no linear structure appears. And the group-theoretic analogue of the
theory — normal subgroups, congruence relations on a group and the quotient group — is not used
here; it belongs to *Groups*, in this Part, and the comparison is drawn only at the points where the
lattice case is genuinely different. A group occurs here only as the group of units of a monoid, as
in *Sets, Functions and Relations*; its systematic theory is *Groups*. The operators that only
preserve an *order* and not the
operations are the subject of *Operators on a Poset*, in this category, and the operators of a
relational structure are the subject of *Endomorphisms of a Relational Structure* beside it.

## Lattice Maps

### The Three Preservation Properties

Let $L$ and $M$ be lattices, with meets written $\wedge$ and joins written $\vee$ in both.

**Definition.** A map $h : L \to M$ is **join-preserving** if

$$
h(x \vee y) = h(x) \vee h(y) \qquad \text{for all } x, y \in L,
$$

and **meet-preserving** if $h(x \wedge y) = h(x) \wedge h(y)$ for all $x, y \in L$. It is a **lattice
homomorphism** if it is both, a **lattice endomorphism** if in addition $M = L$, and a **lattice
isomorphism** if it is a bijective lattice homomorphism.

A join-preserving map is also called a **join-homomorphism** and a meet-preserving map a
**meet-homomorphism**. The three properties are not equivalent, and the examples below separate
them. Two consequences of the definitions are used constantly.

**Proposition.** Let $h : L \to M$ preserve joins. Then $h$ is monotone, and $h(x) \leq h(x \vee y)$
for all $x, y \in L$. Dually a meet-preserving map is monotone.

**Proof.** If $x \leq y$ then $x \vee y = y$, so $h(y) = h(x \vee y) = h(x) \vee h(y) \geq h(x)$. The
second statement is the first applied to the pair $x, x \vee y$. The dual argument, with the order
reversed and $\vee$ replaced by $\wedge$, gives monotonicity of a meet-preserving map.

**Proposition.** A bijective lattice homomorphism has a lattice-homomorphic inverse, so a bijective
homomorphism is an isomorphism of lattices.

**Proof.** Let $h$ be a bijective homomorphism and let $u, v \in M$, say $u = h(x)$, $v = h(y)$.
Then

$$
h^{-1}(u \vee v) = h^{-1}(h(x) \vee h(y)) = h^{-1}(h(x \vee y)) = x \vee y = h^{-1}(u) \vee h^{-1}(v),
$$

and the same computation with $\wedge$ gives the second half.

**Proposition.** A bijective monotone map of lattices need not be a lattice homomorphism.

**Proof.** Take the four-element set $\{0, x, y, 1\}$ with two lattice structures: the Boolean
lattice $L$ in which $0$ is least, $1$ greatest and $x$ and $y$ are incomparable, and the chain $M$
with $0 < x < y < 1$. Every relation of $L$ is a relation of $M$, so the identity map $L \to M$ is
monotone and bijective. It is not join-preserving: $x \vee y = 1$ in $L$, so the image of $x \vee y$
is $1$, while $x \vee y = y$ in $M$, so the join of the images is $y$. The order does not determine
the operations of a lattice, and a bijection that preserves the order need not preserve them.

**Example (monotone but not join-preserving).** In the diamond $M_3$ with elements $0, a, b, c, 1$
and $a, b, c$ the three pairwise incomparable coatoms, define

$$
f(0) = 0, \quad f(a) = a, \quad f(b) = b, \quad f(c) = b, \quad f(1) = 1 .
$$

This map is monotone. It is not join-preserving, because $b \vee c = 1$ gives $f(b \vee c) = f(1) =
1$, while $f(b) \vee f(c) = b \vee b = b$, and $b \neq 1$. It is not meet-preserving either:
$a \wedge c = 0$ gives $f(a \wedge c) = 0$, while $f(a) \wedge f(c) = a \wedge b = 0$, so this
instance agrees, but $a \wedge b = 0$ gives $0$, while $f(a) \wedge f(b) = a \wedge b = 0$ agrees
also; the failure of the meet is read on $c$ and the pair, where $b \wedge c = 0$ with image $0$
against $b \wedge b = b$.

**Example (join-preserving but not meet-preserving).** In the same lattice define $g(c) = 1$ and
$g(x) = x$ for the other four elements. Then $g$ is join-preserving — the check is the finite table
of the join of $M_3$, and the only new values are at $c$ and at joins involving $c$, where $g$
sends the join to $1$ — while it is not meet-preserving, since $g(a \wedge c) = g(0) = 0$ and
$g(a) \wedge g(c) = a \wedge 1 = a$.

**Example (constant maps).** For a fixed $k \in M$ the constant map $h(x) = k$ is both
join-preserving and meet-preserving, since $k \vee k = k$ and $k \wedge k = k$. So the constant maps
are lattice homomorphisms, and this is the reason the preservation of the operations is a stronger
condition than a naive reading of "structure-preserving" suggests. The constants are the maps that
forget all of $L$; they are the elements of $\operatorname{End}(L)$ that are neither injective nor
surjective, and they play the role of the zero of an operator algebra when the lattice is bounded.

**Remark (bounded lattices).** If $L$ and $M$ are bounded, with least and greatest elements $0_L,
1_L$ and $0_M, 1_M$, a **bounded lattice homomorphism** is one that also satisfies $h(0_L) = 0_M$
and $h(1_L) = 1_M$. The constant maps are then homomorphisms only in the degenerate case $k = 0_M =
1_M$. The distinction is recorded because the representation theorems of the corpus work with
bounded homomorphisms, while the theory of congruences below works with the unital notions.

### The Endomorphism Monoid

**Definition.** The set of lattice endomorphisms of $L$, written $\operatorname{End}(L)$, is a monoid
under composition, with identity $\mathrm{id}_L$; its group of units is the **automorphism group**
$\operatorname{Aut}(L)$.

**Proposition.** $\operatorname{End}(L)$ is a monoid, and $\operatorname{Aut}(L)$ is a group.

**Proof.** The composite of two lattice homomorphisms is a lattice homomorphism: $h(g(x \vee y)) =
h(g(x) \vee g(y)) = h(g(x)) \vee h(g(y))$, and dually for the meet. Composition is associative and
$\mathrm{id}_L$ is a two-sided identity by *Sets, Functions and Relations*. A unit of the monoid is
a bijective endomorphism with inverse in the monoid; by the proposition above that inverse is a
lattice homomorphism, so the units are exactly the automorphisms, and they form a group.

The monoid of join-preserving maps and the monoid of meet-preserving maps are defined the same way;
each contains $\operatorname{End}(L)$, and each is closed under composition.

**Notation.** $\operatorname{End}_\vee(L)$ and $\operatorname{End}_\wedge(L)$ denote the monoids of
join-preserving and of meet-preserving self-maps of $L$. The inclusions

$$
\operatorname{End}(L) \;\subseteq\; \operatorname{End}_\vee(L), \qquad
\operatorname{End}(L) \;\subseteq\; \operatorname{End}_\wedge(L)
$$

are strict for a lattice with more than one element, because of the constants. The two monoids
differ; the duality principle interchanges them.

**Example (idempotent endomorphisms).** An endomorphism $e$ with $e \circ e = e$ is a
**retraction** of $L$ onto the sublattice $e(L)$, which is the set of fixed points of $e$. In the
power-set lattice $\mathcal{P}(X)$ of a set $X$ the maps $A \mapsto A \cap Y$ and $A \mapsto A \cup
Y$, for a fixed $Y \subseteq X$, are idempotent lattice endomorphisms, with images the sublattices
$[\emptyset, Y]$ and $[Y, X]$. The lattice endomorphisms of $\mathcal{P}(X)$ are not the only maps
that preserve the binary operations for that reason: a lattice homomorphism preserves $\wedge$ and
$\vee$ as *binary* operations, and it need not preserve the empty join or the empty meet, so the
values $e(\emptyset)$ and $e(X)$ are not determined and the constants of the lattice are not
forced. The two
examples above are the retractions onto the principal ideals and the principal filters, and the
general classification of the idempotent endomorphisms of a power-set lattice is not needed here.

**Example.** For the two-element lattice $\mathbf{2} = \{0, 1\}$ every map $\mathbf{2} \to
\mathbf{2}$ is monotone, so $|\operatorname{End}(\mathbf{2})| = 4$: the identity, the two constants
and the negation. The negation is an automorphism and the two constants are not, so
$\operatorname{Aut}(\mathbf{2})$ has two elements.

## Congruences

### Congruences and Quotients

**Definition.** A **congruence** on a lattice $L$ is an equivalence relation $\theta$ on $L$ that is
compatible with the operations:

$$
x \mathrel{\theta} x' \ \text{and} \ y \mathrel{\theta} y'
\quad\Longrightarrow\quad
(x \vee y) \mathrel{\theta} (x' \vee y') \ \text{and} \ (x \wedge y) \mathrel{\theta} (x' \wedge y').
$$

The set of congruences of $L$, ordered by inclusion of relations, is written $\operatorname{Con}(L)$.

**Proposition.** The quotient set $L/\theta$ carries a unique lattice structure for which the
quotient map $\pi : L \to L/\theta$, $x \mapsto [x]$, is a lattice homomorphism.

**Proof.** Define $[x] \vee [y] = [x \vee y]$ and $[x] \wedge [y] = [x \wedge y]$. The compatibility
of $\theta$ is exactly the statement that these definitions do not depend on the representatives.
The lattice axioms for $L/\theta$ — idempotence, commutativity, associativity and absorption in the
form of *Order Theory and Lattices* — are read off from those of $L$ class by class, and $\pi$ is a
homomorphism by construction. Uniqueness is clear, since a lattice structure on $L/\theta$ for which
$\pi$ is a homomorphism must satisfy these equations.

Thus a congruence is the same thing as a **kernel**: the relation $x \mathrel{\theta} y$, and the
quotient $L/\theta$ is the image of the operator $\pi$. The word *kernel* is used in the
set-theoretic sense here — the relation that a map collapses — and not in the sense of a group
homomorphism, which belongs to *Groups*; for lattices the relation determines the map up to the
obvious identification, and the quotient is the lattice it presents.

**Definition.** For $a \in L$ the **principal congruence** $\theta(a)$ is the smallest congruence
identifying $a$ with the least element $0$, when $L$ is bounded; more generally, for $a, b \in L$ the
principal congruence $\theta(a, b)$ is the smallest congruence with $a \mathrel{\theta} b$.

**Proposition.** The intersection of a family of congruences is a congruence, and the congruences
of $L$ form a complete lattice in which

$$
\bigwedge_i \theta_i = \bigcap_i \theta_i, \qquad
\bigvee_i \theta_i = \text{the smallest congruence containing } \textstyle\bigcup_i \theta_i .
$$

**Proof.** The intersection of equivalence relations is an equivalence relation, and it inherits
compatibility from the members of the family. So the intersection of any family of congruences is a
congruence, and it is the greatest lower bound in $\operatorname{Con}(L)$. A greatest lower bound
for every subset gives a smallest congruence containing a given relation, by intersecting the
congruences that contain it; that congruence is the join of the family. A complete lattice is thus
obtained.

The description of the join is not effective — it says the smallest congruence containing the union
exists, not how to compute it — and for the finite lattices that occur in examples the congruence
generated by a set of pairs is computed by closing under the operations and transitivity.

### The Kernel of a Homomorphism

**Definition.** Let $h : L \to M$ be a lattice homomorphism. The **kernel** of $h$ is the relation

$$
\ker h = \{(x, y) \in L \times L : h(x) = h(y)\}.
$$

**Proposition.** For every lattice homomorphism $h : L \to M$ the relation $\ker h$ is a congruence
on $L$, and for every congruence $\theta$ on $L$ the quotient map $\pi : L \to L/\theta$ satisfies
$\ker \pi = \theta$.

**Proof.** The relation $\ker h$ is the kernel of the underlying function and is therefore an
equivalence relation. If $h(x) = h(x')$ and $h(y) = h(y')$ then $h(x \vee y) = h(x) \vee h(y) =
h(x') \vee h(y') = h(x' \vee y')$, so $\ker h$ is compatible with $\vee$; the argument for
$\wedge$ is the same. The second statement is the definition of the quotient operations.

**Theorem (first isomorphism theorem for lattices).** Let $h : L \to M$ be a surjective lattice
homomorphism. Then the map

$$
\bar h : L/{\ker h} \to M, \qquad \bar h([x]) = h(x),
$$

is a lattice isomorphism.

**Proof.** The map $\bar h$ is well defined, because $[x] = [x']$ says exactly that $h(x) = h(x')$.
It is injective by the same equivalence, and it is surjective because $h$ is. It preserves the
operations: $\bar h([x] \vee [y]) = \bar h([x \vee y]) = h(x \vee y) = h(x) \vee h(y) = \bar h([x])
\vee \bar h([y])$, and the same with $\wedge$. So $\bar h$ is a bijective homomorphism, hence an
isomorphism.

The theorem says that a congruence and a quotient are two descriptions of the same passage from a
lattice to one of its homomorphic images, and that the passage is an isomorphism exactly when the
homomorphism is surjective. It is the lattice case of the first isomorphism theorem that the whole
corpus uses, and the same statement for groups, rings and modules is proved in their own
categories.

### The Lattice of Congruences

**Theorem (Funayama–Nakayama).** The congruence lattice $\operatorname{Con}(L)$ of a lattice $L$ is
distributive: for congruences $\theta_1, \theta_2, \theta_3$,

$$
\theta_1 \wedge (\theta_2 \vee \theta_3) = (\theta_1 \wedge \theta_2) \vee (\theta_1 \wedge \theta_3).
$$

The theorem is quoted from the literature; its proof is not reproduced, and the finite instances are
checked in the companion file. It is what makes $\operatorname{Con}(L)$ a distributive lattice for
every lattice $L$, and it is the reason the congruence lattice is a useful invariant: the class of
distributive lattices is much better behaved than the class of all lattices.

**Example.** For a chain $C_n = \{0 < 1 < \cdots < n-1\}$ a congruence is described by the partition
of the chain into consecutive intervals, since a class of a congruence on a chain is an interval and
the congruence is determined by its classes. The congruence is therefore determined by the set of
gaps at which a cut is made, so $\operatorname{Con}(C_n)$ has $2^{n-1}$ elements and is the lattice
of subsets of an $(n-1)$-element set, which is distributive. For $n = 3$ the four congruences are
the identity, the two that identify one adjacent pair, and the universal relation, and they form the
four-element Boolean lattice.

**Example.** The diamond $M_3$ is **simple**: its congruence lattice is the two-element chain. Let
$\theta \neq \mathrm{id}$, so $x \mathrel{\theta} y$ for two distinct elements $x, y$.

- If $0 \mathrel{\theta} a$ with $a$ a coatom, then for any other coatom $c$ the compatibility with
  the join gives $c = 0 \vee c \mathrel{\theta} a \vee c = 1$, so every coatom other than $a$ is
  identified with $1$. In particular $b \mathrel{\theta} 1$ for a coatom $b \neq a$, and
  compatibility with the meet then gives $0 = b \wedge c \mathrel{\theta} 1 \wedge c = c$ for a third
  coatom $c$; so $0 \mathrel{\theta} c$, and with $c \mathrel{\theta} 1$ from the first step,
  transitivity gives $0 \mathrel{\theta} 1$ and $\theta$ is universal. The case $1 \mathrel{\theta}
  a$ is dual.
- If $a \mathrel{\theta} b$ with $a \neq b$ two coatoms, then $a \vee b = 1$ gives $1 \mathrel{\theta}
  b$, compatibility with the meet gives $c = 1 \wedge c \mathrel{\theta} b \wedge c = 0$ for the third
  coatom $c$, and compatibility with the join gives $1 = c \vee a \mathrel{\theta} 0 \vee a = a$; so
  $0 \mathrel{\theta} c$ and $c \mathrel{\theta} 1$, whence $0 \mathrel{\theta} 1$ and $\theta$ is
  universal.

Every nontrivial congruence is therefore universal, and $M_3$ is simple. A **simple lattice** is one
whose only congruences are the identity and the universal relation.

## The Operator View of a Lattice

The materials assembled so far organise the lattice at the operator layer: the endomorphisms of $L$
form the monoid $\operatorname{End}(L)$, the congruences form the distributive lattice
$\operatorname{Con}(L)$, and the quotient is the operator that carries a congruence to its image.
The two descriptions are joined by the kernel–image correspondence:

$$
\theta \;\longmapsto\; L/\theta, \qquad h \;\longmapsto\; \ker h,
$$

which are inverse up to isomorphism on the congruences and the surjective endomorphic images, and
which make the congruence lattice the operator-theoretic invariant of the lattice: two lattices with
isomorphic congruence lattices satisfy the same lattice of quotient operators.

**Definition.** The **operator view** of a lattice $L$ is the data of the monoid
$\operatorname{End}(L)$ acting on $L$ by evaluation, together with the lattice
$\operatorname{Con}(L)$ of kernels of that action. A **lattice congruence** of the operator view is
a congruence in the sense above, and a **quotient operator** is the map $L \to L/\theta$.

The operator view is what makes the theory of lattices available to the rest of the corpus: a
statement about a homomorphic image of a lattice is a statement about an operator on it, and the
equivalence relations that a given family of operators preserves are the congruences of the family.
This reading is used in *Order Theory and Lattices* for the closure operators, and it is the point
at which the lattice theory of the present article meets the operator theory of the categories
below it.

**Remark.** The two-element lattice $\mathbf{2}$ plays the role of the initial operator view: the
maps $L \to \mathbf{2}$ are the characteristic functions of the subsets of $L$ that are **filters**
or **ideals** in the appropriate sense, and a congruence of $L$ is determined by the homomorphisms
from $L$ into a distributive lattice that identify it. The analysis of that determination is the
representation theory of distributive lattices, stated in *Order Theory and Lattices* and
completed by the Stone representation in Part II, where a topology is available; the congruence
lattice here is the algebraic half of it.

## Summary

A lattice map may preserve the join, the meet, or both; a join-preserving map is monotone, and the
three notions are distinct, as the diamond $M_3$ shows. The lattice endomorphisms form the monoid
$\operatorname{End}(L)$, whose group of units is the automorphism group $\operatorname{Aut}(L)$;
the constants are endomorphisms, so the monoid is large and its units are few.

A congruence of a lattice is an equivalence relation compatible with the meet and the join; it is
exactly the kernel of a lattice homomorphism, the quotient $L/\theta$ carries a unique lattice
structure making the quotient map a homomorphism, and the first isomorphism theorem identifies a
surjective homomorphic image with the quotient by its kernel. The congruences form a complete
lattice under inclusion, in which the meet is the intersection and the join is the smallest
congruence containing the union, and by the theorem of Funayama and Nakayama this lattice is
distributive. A lattice with no nontrivial congruence is simple, and the diamond is the smallest
example.

The operator view reads the lattice through these two layers: the endomorphism monoid acting on the
lattice, and the distributive lattice of congruences that are the kernels of that action. The
quotient by a congruence is the canonical operator from a lattice to a homomorphic image, and the
kernel–image correspondence is the algebraic content of the first isomorphism theorem.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L, M$ | Lattices, with meet $\wedge$ and join $\vee$ |
| $h : L \to M$ | A map of lattices; join-preserving, meet-preserving, or a homomorphism |
| $\operatorname{End}(L)$ | Monoid of lattice endomorphisms of $L$ under composition |
| $\operatorname{End}_\vee(L)$, $\operatorname{End}_\wedge(L)$ | Monoids of join-preserving and of meet-preserving self-maps of $L$ |
| $\operatorname{Aut}(L)$ | Automorphism group of $L$, the group of units of $\operatorname{End}(L)$ |
| $\theta$ | A congruence of $L$: an equivalence compatible with $\wedge$ and $\vee$ |
| $L/\theta$, $\pi$ | Quotient lattice and quotient map $x \mapsto [x]$ |
| $\ker h$ | Kernel of a homomorphism, $\{(x,y) : h(x) = h(y)\}$ |
| $\operatorname{Con}(L)$ | Lattice of congruences of $L$, ordered by inclusion |
| $\theta(a), \theta(a,b)$ | Principal congruences |
| $\mathbf{2}$ | The two-element lattice, the simplest congruence lattice and target of the maps $L \to \mathbf{2}$ |
| $\bigvee_i \theta_i$ | Join of congruences, the smallest congruence containing their union |

## Further Reading

- Garrett Birkhoff, *Lattice Theory*, 3rd ed. (American Mathematical Society, 1967), for the classical account of lattice homomorphisms, congruences and quotient lattices.
- George Grätzer, *Lattice Theory: Foundation* (Birkhäuser, 2011), for the congruence lattice of a lattice, the theorem of Funayama and Nakayama, and the congruence lattice of a finite lattice.
- George Grätzer, *General Lattice Theory*, 2nd ed. (Birkhäuser, 2003), for the systematic treatment of congruences, simple lattices and the distributivity of $\operatorname{Con}(L)$.
- N. Funayama and T. Nakayama, "On the distributivity of a lattice of lattice-congruences", *Proceedings of the Imperial Academy of Tokyo* **18** (1942), 553–554, for the original theorem that the congruence lattice of a lattice is distributive.
- Steven Roman, *Lattices and Ordered Sets* (Springer, 2008), for an introduction to lattices, homomorphisms and congruences with the operator and order-theoretic aspects emphasised.
- Rudolf Wille, "Restructuring lattice theory: an approach based on hierarchies of concepts", in *Ordered Sets* (Reidel, 1982), for the operator view of a lattice through its homomorphisms into the two-element lattice.
