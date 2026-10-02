
# __Endomorphisms of a Relational Structure__

## Introduction

A **relational structure** is a set carrying a family of relations, and a map between two such
structures is a **homomorphism** when it carries every relation of the source into the
corresponding relation of the target. The maps of a structure into itself are its **endomorphisms**;
they compose, so they form a monoid, and the elements of that monoid that are invertible are the
automorphisms of the structure. This article develops that operator layer for relational structures:
the endomorphism monoid and its group of units, the **automorphism group** and its action on the
underlying set, the **embeddings** and the **strong endomorphisms**, the kernel of a strong
homomorphism and the first isomorphism theorem, and the special case of a single relation.

The article presupposes the language of *Sets, Functions and Relations* — sets, relations, the
converse, composition, functions and their injectivity, surjectivity and bijectivity, equivalence
relations and quotients — and the composition of maps. It is placed in the `- Operator Theory` group
of this category: it treats the maps of a structure and the structure they form, and it uses no
algebraic structure from another category.

Three boundaries are observed. No **topology**, no distance and no metric is used, so the notions of
convergence and continuity that a later part attaches to these maps have no place here. The
endomorphisms of a *poset* — the monotone maps — are the subject of *Operators on a Poset*, in this
group, and the automorphism group of a *poset* is the subject of *The Order Automorphism Group*
beside it; both are instances of the present theory, and the article says so rather than repeating
them. The **converse** relation and the operator it defines belong to *The Converse Relation as an
Operator*, in this group; it is used here only to describe the inverse image of a relation. Finally,
the systematic theory of **groups** is *Groups*, in this Part, and the theory of a group acting on a
set is *Transformation Groups*; here the only group that occurs is the group of units of an
endomorphism monoid, and its action is computed from the monoid.

## Relational Structures and Their Maps

### Structures and Homomorphisms

**Definition.** A **relational structure** is a pair $\mathcal{A} = (A, (R_i)_{i \in I})$ consisting
of a set $A$, the **domain**, and a family of relations $R_i \subseteq A^{n_i}$ on $A$, one for each
index $i$. A **binary** relational structure is one in which every relation is binary, $R_i
\subseteq A \times A$; the article works with binary structures and says where non-binary relations
would change a statement.

A **poset** $(P, \leq)$, a **graph** $(V, E)$ with $E$ a symmetric irreflexive relation on $V$, and a
set with an **equivalence relation** are the standard instances; so is a set with no relations at
all, which is the degenerate case in which every map is a homomorphism.

**Definition.** Let $\mathcal{A} = (A, (R_i))$ and $\mathcal{B} = (B, (S_i))$ be relational
structures over the same index set. A **homomorphism** from $\mathcal{A}$ to $\mathcal{B}$ is a
function $f : A \to B$ such that

$$
(x, y) \in R_i \quad\Longrightarrow\quad (f(x), f(y)) \in S_i
\qquad \text{for every } i \text{ and all } x, y \in A .
$$

A homomorphism is **strong** if the implication is an equivalence for every $i$:

$$
(x, y) \in R_i \quad\Longleftrightarrow\quad (f(x), f(y)) \in S_i .
$$

An **embedding** is an injective strong homomorphism. An **isomorphism** is a bijective strong
homomorphism, and two structures over the same index set are **isomorphic**, written $\mathcal{A}
\cong \mathcal{B}$, when an isomorphism $\mathcal{A} \to \mathcal{B}$ exists.

The three notions sit in a strict chain. Every strong homomorphism is a homomorphism, and every
embedding is a strong homomorphism; both inclusions are strict. A homomorphism establishes a
relation between the two structures but may collapse distinctions; a strong homomorphism
establishes a **reflection** of the relations as well, so that it does not identify related pairs
that were unrelated, nor separate pairs that were related.

**Example.** Let $A = \{1,2\}$ with $R = \{(1,2)\}$ and $B = \{u\}$ with $S = \{(u,u)\}$. The only
map $f : A \to B$ is a homomorphism, since $R \subseteq f^{-1}(S)$ holds vacuously on the one pair
of $R$; it is not strong, because $(f(2), f(1)) = (u,u) \in S$ while $(2,1) \notin R$.

**Definition.** The **inverse image** of a relation $S \subseteq B \times B$ under $f : A \to B$ is

$$
f^{-1}(S) = \{(x,y) \in A \times A : (f(x), f(y)) \in S\}.
$$

The inverse image is a relation on $A$, and it is the exact object that the two definitions above
compare: $f$ is a homomorphism $\mathcal{A} \to \mathcal{B}$ exactly when $R_i \subseteq f^{-1}
(S_i)$ for every $i$, and it is strong exactly when $R_i = f^{-1}(S_i)$ for every $i$. In particular
a strong homomorphism is the same thing as a map under which each relation is the inverse image of
its target relation.

### Embeddings and Strong Homomorphisms

**Proposition.** Let $f : \mathcal{A} \to \mathcal{B}$ be a strong homomorphism.

1. If $f$ is injective it is an embedding, and if $f$ is bijective it is an isomorphism.
2. If $g : \mathcal{B} \to \mathcal{C}$ is a strong homomorphism then $g \circ f$ is strong.
3. If $g \circ f$ is strong, then $f$ is strong.

**Proof.** (1) Immediate from the definitions. (2) For each $i$, $(g \circ f)^{-1}(T_i) = f^{-1}(g^{-1}
(T_i)) = f^{-1}(S_i) = R_i$, using that $g$ and $f$ are strong. (3) If $(f(x), f(y)) \in S_i$ then
$(g(f(x)), g(f(y))) \in T_i$, so $(x,y) \in (g \circ f)^{-1}(T_i) = R_i$; the converse is the
definition of a homomorphism.

**Proposition.** A bijective homomorphism is an isomorphism if and only if it is strong.

**Proof.** A bijective strong homomorphism is an isomorphism by definition, and an isomorphism is
strong by definition. For the necessity of strength, let $A = \{1,2\}$ with $R = \{(1,2)\}$ and $B =
\{u,v\}$ with $S = \{(u,u),(u,v)\}$, and let $f(1) = u$, $f(2) = v$. Then $f$ is a bijective
homomorphism: the only pair of $R$ maps to $(u,v) \in S$. It is not strong, because $(f(1), f(1)) =
(u,u) \in S$ while $(1,1) \notin R$.

## The Endomorphism Monoid

### Composition and Units

Fix a relational structure $\mathcal{A} = (A, (R_i))$ and let $\operatorname{End}(\mathcal{A})$ be
the set of homomorphisms $\mathcal{A} \to \mathcal{A}$, the **endomorphisms** of $\mathcal{A}$.

**Proposition.** $\operatorname{End}(\mathcal{A})$ is a monoid under composition, with identity
$\mathrm{id}_A$.

**Proof.** The composite of two endomorphisms is a homomorphism, because a homomorphism is a map
with $R_i \subseteq f^{-1}(S_i)$ and the inverse image composes: $(g \circ f)^{-1}(R_i) = f^{-1}
(g^{-1}(R_i)) \supseteq f^{-1}(S_i) \supseteq R_i$ when $g^{-1}(R_i) \supseteq R_i$ and $f^{-1}(S_i)
\supseteq R_i$. Composition of functions is associative and $\mathrm{id}_A$ is a two-sided identity,
by *Sets, Functions and Relations*.

**Definition.** An **automorphism** of $\mathcal{A}$ is a bijective endomorphism whose inverse is
also an endomorphism; equivalently, by the proposition above, an endomorphism that is an
isomorphism $\mathcal{A} \to \mathcal{A}$. The set of automorphisms is written
$\operatorname{Aut}(\mathcal{A})$.

**Theorem.** $\operatorname{Aut}(\mathcal{A})$ is the group of units of the monoid
$\operatorname{End}(\mathcal{A})$.

**Proof.** If $f \in \operatorname{End}(\mathcal{A})$ has a two-sided inverse $g \in
\operatorname{End}(\mathcal{A})$, then $f$ is bijective as a function and $g$ is its inverse
function; so $f$ is a bijective endomorphism with endomorphic inverse, that is, an automorphism. If
$f$ is an automorphism, its inverse function is an endomorphism, so $f$ is a unit. The units of a
monoid always form a group under the monoid operation: the identity is a unit, a product of units is
a unit, and a unit has an inverse that is a unit. The set $\operatorname{Aut}(\mathcal{A})$ is
therefore a group, and it is the group of units of $\operatorname{End}(\mathcal{A})$.

The systematic theory of a group, and of a group acting on a set, is *Groups* and *Transformation
Groups*, in this Part; here a group is used only as the group of units of a monoid, and the action
below is computed directly from the composition of maps.

**Corollary.** A bijective endomorphism of $\mathcal{A}$ need not be an automorphism: by the last
proposition of the previous subsection a bijective homomorphism $\mathcal{A} \to \mathcal{A}$ may
fail to be strong, and then its inverse function is not an endomorphism, so it is not a unit of
$\operatorname{End}(\mathcal{A})$.

### The Automorphism Group and Its Action

Because $\operatorname{Aut}(\mathcal{A})$ is a group of bijections of $A$, it is a subgroup of the
symmetric group $\operatorname{Sym}(A)$, the group of all bijections of $A$ under composition. The
inclusion

$$
\operatorname{Aut}(\mathcal{A}) \;\leq\; \operatorname{Sym}(A)
$$

is the precise sense in which the automorphism group measures the symmetry of the structure: it is
the set of bijections that preserve every relation.

**Definition.** The **action** of $\operatorname{Aut}(\mathcal{A})$ on $A$ is the map

$$
\operatorname{Aut}(\mathcal{A}) \times A \to A, \qquad (g, x) \mapsto g(x).
$$

The **orbit** of $x \in A$ is $G \cdot x = \{g(x) : g \in \operatorname{Aut}(\mathcal{A})\}$, and the
**stabiliser** of $x$ is $G_x = \{g : g(x) = x\}$.

**Proposition.** The orbits of the action of $\operatorname{Aut}(\mathcal{A})$ on $A$ partition
$A$, and the orbit of $x$ is the smallest invariant subset containing $x$.

**Proof.** The relation $x \sim y$ given by $y = g(x)$ for some $g \in \operatorname{Aut}(\mathcal{A})$
is reflexive (the identity), symmetric (inverse) and transitive (composition), so it is an
equivalence relation and its classes are the orbits. If $D \subseteq A$ is invariant under every
automorphism and $x \in D$, then $g(x) \in D$ for every $g$, so the orbit of $x$ is contained in
$D$; this proves the minimality.

**Proposition.** Every relation $R_i$ of $\mathcal{A}$ is invariant under
$\operatorname{Aut}(\mathcal{A})$: if $(x,y) \in R_i$ and $g \in \operatorname{Aut}(\mathcal{A})$
then $(g(x), g(y)) \in R_i$. Consequently each $R_i$ is a union of orbits of the action of
$\operatorname{Aut}(\mathcal{A})$ on $A \times A$.

**Proof.** The first statement is the definition of an endomorphism applied to $g$. For the second,
the action on $A \times A$ given by $g \cdot (x,y) = (g(x), g(y))$ is an action, and the first
statement says that $R_i$ is closed under it; a subset closed under a group action is a union of
orbits.

**Example.** For a set $A$ with no relations, every function $A \to A$ is an endomorphism, so
$\operatorname{End}(\mathcal{A})$ is the full transformation monoid $A^A$ and
$\operatorname{Aut}(\mathcal{A}) = \operatorname{Sym}(A)$. For $|A| = n$ this gives $n^n$
endomorphisms and $n!$ automorphisms, and the orbit of every element is the whole of $A$: a set with
no structure has no invariant partition.

**Example.** For the complete graph $K_n$, whose edge relation $E$ is the relation $\neq$ on an
$n$-element set, a map $f$ is an endomorphism exactly when $x \neq y$ implies $f(x) \neq f(y)$,
that is, exactly when $f$ is injective. So $\operatorname{End}(K_n)$ is the monoid of injective maps
of an $n$-element set, and $\operatorname{Aut}(K_n) = \operatorname{Sym}(A)$. For the graph with the
empty edge relation the condition is vacuous, so every map is an endomorphism, and the automorphism
group is again $\operatorname{Sym}(A)$; the two structures have the same automorphism group and
different endomorphism monoids, which shows that the automorphism group alone does not recover the
structure.

## Kernels and Quotients

### The Kernel of a Strong Homomorphism

**Definition.** Let $f : \mathcal{A} \to \mathcal{B}$ be a homomorphism. Its **kernel** is the
equivalence relation $\ker f = \{(x,y) : f(x) = f(y)\}$ on $A$. A **congruence** of $\mathcal{A}$ is
an equivalence relation $\theta$ on $A$ that is compatible with every relation: if $x \mathrel{\theta}
x'$, $y \mathrel{\theta} y'$ and $(x,y) \in R_i$, then $(x',y') \in R_i$.

**Proposition.** The kernel of a strong homomorphism is a congruence. The kernel of a homomorphism
that is not strong need not be a congruence.

**Proof.** Let $f$ be strong, let $x \mathrel{\theta} x'$ and $y \mathrel{\theta} y'$ with $\theta =
\ker f$, and let $(x,y) \in R_i$. Then $f(x) = f(x')$ and $f(y) = f(y')$, so $(f(x'), f(y')) =
(f(x), f(y)) \in S_i$, and strength gives $(x',y') \in R_i$. For the failure, take $A = \{1,2,3\}$
with $R = \{(1,2)\}$, $B = \{u,v\}$ with $S = \{(u,v)\}$, and $f(1) = u$, $f(2) = v$, $f(3) = u$.
The map is a homomorphism and is not strong, since $(f(3), f(2)) = (u,v) \in S$ while $(3,2) \notin
R$. Its kernel identifies $1$ with $3$, and the pair $(1,2) \in R$ is not accompanied by $(3,2) \in
R$, so $\ker f$ is not compatible with $R$ and is not a congruence.

**Definition.** For a congruence $\theta$ of $\mathcal{A}$ the **quotient structure** $\mathcal{A}/
\theta$ has domain the set $A/\theta$ of classes, with relations

$$
([x], [y]) \in R_i/\theta \quad\Longleftrightarrow\quad (x', y') \in R_i
\text{ for some } x' \mathrel{\theta} x, \ y' \mathrel{\theta} y .
$$

**Proposition.** The relation $R_i/\theta$ is well defined, and the quotient map $\pi : A \to
A/\theta$ is a strong homomorphism $\mathcal{A} \to \mathcal{A}/\theta$.

**Proof.** Well-definedness is the compatibility of $\theta$ with $R_i$: if $x' \mathrel{\theta} x$
and $y' \mathrel{\theta} y$ both satisfy $(x',y') \in R_i$, then by symmetry and transitivity any
other representatives do too. The map $\pi$ is a homomorphism because $(x,y) \in R_i$ gives $([x],
[y]) \in R_i/\theta$ directly; it is strong because $([x],[y]) \in R_i/\theta$ means precisely that
some related representatives exist, and compatibility moves the relation to $x$ and $y$.

### The First Isomorphism Theorem

**Theorem.** Let $f : \mathcal{A} \to \mathcal{B}$ be a surjective strong homomorphism. Then the map

$$
\bar f : \mathcal{A}/{\ker f} \to \mathcal{B}, \qquad \bar f([x]) = f(x),
$$

is an isomorphism of relational structures.

**Proof.** The map is well defined and injective because $[x] = [x']$ exactly when $f(x) = f(x')$,
and it is surjective because $f$ is. It is strong: $([x],[y]) \in R_i/\ker f$ says that there are
$x' \in [x]$, $y' \in [y]$ with $(x',y') \in R_i$, which is equivalent to $(f(x), f(y)) \in S_i$ by
compatibility and strength. So $\bar f$ is a bijective strong homomorphism, hence an isomorphism.

The statement is the relational analogue of the first isomorphism theorem for lattices established
in *Operators on a Lattice*, and it is the form of the theorem that the same result takes for
groups, rings and modules in their own categories.

## The Relation Case

### Endomorphisms of a Single Relation

When $\mathcal{A} = (A, R)$ carries a single binary relation, the definitions above simplify to
statements about $R$ alone, and the endomorphisms are the maps $f$ with

$$
(x,y) \in R \ \Longrightarrow \ (f(x), f(y)) \in R .
$$

**Definition.** A **strong endomorphism** of $(A,R)$ is a map $f$ with $(x,y) \in R \iff (f(x),f(y))
\in R$ for all $x,y$; an **embedding** of $(A,R)$ into $(B,S)$ is an injective map $f$ with
$(x,y) \in R \iff (f(x),f(y)) \in S$.

**Proposition.** The strong endomorphisms of $(A,R)$ form a submonoid of $\operatorname{End}(A,R)$,
and an injective strong endomorphism of a finite structure is an automorphism.

**Proof.** The first statement is part (2) of the proposition on strong homomorphisms. For the
second, an injective self-map of a finite set is bijective, and a bijective strong endomorphism is an
automorphism.

**Example.** Let $R$ be an equivalence relation on $A$. A map $f$ is an endomorphism of $(A,R)$
exactly when it sends each class into a class: $x \mathrel{R} y$ implies $f(x) \mathrel{R} f(y)$. It
may merge classes but neither split one nor create relation across classes whose images lie in
distinct classes. An automorphism is a bijection that carries each class onto a class, so it permutes
the classes among those of equal size and acts bijectively within each class; the automorphism group
is the wreath product of the symmetric groups of the classes over the permutations of the classes of
equal size, and it is the direct product of those symmetric groups when the classes have pairwise
distinct sizes.

**Example.** Let $R$ be a strict partial order on $A$, that is, an irreflexive transitive relation.
An endomorphism is a monotone map for the strict order, an embedding is an order embedding, and the
automorphisms are the order automorphisms. The theory of these maps is the subject of *Operators on a
Poset* and of *The Order Automorphism Group*, in this group, and is not repeated here; they are
quoted as the standard instance of the present theory.

### Preservation under Homomorphic Images

Some properties of a relation are preserved by a homomorphism and some are not, and the distinction
is exactly the strength of the maps used.

**Proposition.** Let $f : (A,R) \to (B,S)$ be a homomorphism.

1. If $f$ is surjective and $R$ is reflexive, then $S$ is reflexive.
2. If $f$ is surjective and $R$ is symmetric, then $S$ is symmetric.
3. If $R$ is transitive, then $S$ is transitive on the image of $f$.
4. If $f$ is surjective and strong, then $S$ is irreflexive whenever $R$ is, and $S$ is
   antisymmetric whenever $R$ is.

**Proof.** (1) If $R$ is reflexive and $y = f(x) \in B$, then $(x,x) \in R$ gives $(y,y) \in S$.
(2) If $(u,v) \in S$ with $u = f(x)$, $v = f(y)$, then $(x,y) \in R$, so $(y,x) \in R$ and $(v,u) \in
S$. (3) If $(u,v), (v,w) \in S$ with $u = f(x)$, $v = f(y)$, $w = f(z)$, then $(x,y), (y,z) \in R$,
so $(x,z) \in R$ and $(u,w) \in S$. (4) If $S$ contained $(y,y)$ then by surjectivity $y = f(x)$ for
some $x$, and strength gives $(x,x) \in R$, contradicting irreflexivity. If $(u,v) \in S$ and $(v,u)
\in S$, write $u = f(x)$, $v = f(y)$ by surjectivity; strength gives $(x,y) \in R$ and $(y,x) \in
R$, so $x = y$ by antisymmetry and $u = v$.

**Remark.** Antisymmetry is **not** preserved by a homomorphism that is not strong: the map $f(1) =
u$, $f(2) = v$ from $(\{1,2\}, \{(1,2)\})$ to $(\{u,v\}, \{(u,v),(v,u)\})$ is a homomorphism whose
target relation is symmetric, hence not antisymmetric, while the source relation is antisymmetric.
Reflexivity is not reflected either: the target may relate a pair whose preimages are unrelated, as
the first example of the article shows. The list therefore separates the properties that a
homomorphism carries forward from those that only a strong map reflects.

## Summary

A relational structure is a set with a family of relations; a homomorphism is a map carrying each
relation into the corresponding one, a strong homomorphism carries each relation onto it in the
sense that the source relation is the inverse image of the target relation, an embedding is an
injective strong homomorphism, and an isomorphism is a bijective one.

The endomorphisms of a structure form a monoid $\operatorname{End}(\mathcal{A})$ under composition
with identity $\mathrm{id}_A$, and its group of units is the automorphism group
$\operatorname{Aut}(\mathcal{A})$, a subgroup of the symmetric group of the domain. A bijective
endomorphism need not be an automorphism; it is one exactly when it is strong. The automorphism
group acts on the domain, the orbits partition it, and every relation of the structure is a union of
orbits of the induced action on pairs.

The kernel of a strong homomorphism is a congruence, and a congruence is the kernel of the quotient
map; the quotient structure is well defined, the quotient map is strong, and the first isomorphism
theorem identifies a surjective strong homomorphic image with the quotient by its kernel. For a
single relation the strong endomorphisms form a submonoid, an injective strong endomorphism of a
finite structure is an automorphism, and reflexivity, symmetry and transitivity are preserved by
homomorphisms while irreflexivity and antisymmetry are reflected by strong ones.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{A} = (A, (R_i)_{i \in I})$ | Relational structure with domain $A$ and relations $R_i$ |
| $f : \mathcal{A} \to \mathcal{B}$ | Homomorphism: $R_i \subseteq f^{-1}(S_i)$ for all $i$ |
| $f^{-1}(S)$ | Inverse image relation, $\{(x,y) : (f(x), f(y)) \in S\}$ |
| strong | Homomorphism with $R_i = f^{-1}(S_i)$ for all $i$ |
| embedding | Injective strong homomorphism |
| isomorphism, $\mathcal{A} \cong \mathcal{B}$ | Bijective strong homomorphism |
| $\operatorname{End}(\mathcal{A})$ | Monoid of endomorphisms of $\mathcal{A}$ |
| $\operatorname{Aut}(\mathcal{A})$ | Automorphism group, the group of units of $\operatorname{End}(\mathcal{A})$ |
| $\operatorname{Sym}(A)$ | Group of all bijections of $A$; $\operatorname{Aut}(\mathcal{A}) \leq \operatorname{Sym}(A)$ |
| $G \cdot x$, $G_x$ | Orbit and stabiliser of $x$ under $G = \operatorname{Aut}(\mathcal{A})$ |
| $\ker f$ | Kernel of a homomorphism, $\{(x,y) : f(x) = f(y)\}$ |
| congruence $\theta$ | Equivalence relation compatible with every $R_i$ |
| $\mathcal{A}/\theta$ | Quotient structure |

## Further Reading

- Roland Fraïssé, *Theory of Relations*, rev. ed. (North-Holland, 2000), for relational structures, homomorphisms, embeddings and the theory of relations.
- Gunther Schmidt, *Relational Mathematics*, Encyclopedia of Mathematics and its Applications 132 (Cambridge University Press, 2011), for the algebra of relations and the maps preserving them.
- Stanley Burris and H. P. Sankappanavar, *A Course in Universal Algebra* (Springer, 1981), for the homomorphism, congruence and quotient theory of structures with operations and relations.
- Boris M. Schein, "Relation algebras and function semigroups", *Semigroup Forum* **1** (1970), 1–62, for endomorphism monoids of relations and the structure they carry.
- Frank Harary, *Graph Theory* (Addison-Wesley, 1969), for graph homomorphisms, embeddings and automorphism groups as the standard instance.
- Brian A. Davey and Hilary A. Priestley, *Introduction to Lattices and Order*, 2nd ed. (Cambridge University Press, 2002), for the order-theoretic instance, the monotone maps and the order automorphisms, treated in *Operators on a Poset* and *The Order Automorphism Group*.
