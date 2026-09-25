
# __Effect Algebras and Orthomodular Lattices__

## Introduction

This is the fourth article of the Boolean system in Part V, and it occupies the **algebra slot** of that system for the *non-distributive* reading of the domain. The systems of the preceding three articles — Boolean, Heyting and MV — all rest on distributive lattices, and their complementation is unique. The algebras of this article, the **orthomodular lattices** and the **effect algebras**, retain an order and an orthocomplementation but abandon distributivity; the complement need not be a Boolean complement, and the lattice laws that the earlier articles used are replaced by weaker ones.

The boundary against the general theory is deliberate. Lattices, modularity and the forbidden-sublattice criterion are the subject of *Order Theory and Lattices*; the Boolean case is *Boolean Algebras and Lattices*; the distributive negations are *Heyting Algebras and Intuitionistic Logic* and *MV-Algebras and Many-Valued Logic*. The models of the present algebras come from functional analysis: the projection lattice of a Hilbert space is the standard orthomodular lattice, and the unit interval of a von Neumann algebra is the standard effect algebra. Those objects are constructed in *Banach and Hilbert Spaces* and *Operator Algebras*, and are used here as examples; the present article develops the abstract algebra only. No physics is invoked, and no topology, distance or Hilbert-space structure is developed beyond what the examples require.

Throughout, an ortholattice is written $(L, \wedge, \vee, {}^{\perp}, 0, 1)$ with orthocomplement $a^{\perp}$, and an effect algebra is written $(E, \oplus, 0, 1)$ with orthosupplement $a'$. When an effect algebra is lattice-ordered and its partial sum is the join on orthogonal pairs, its orthosupplement coincides with the orthocomplement of the resulting orthomodular lattice; this is stated precisely below. The projection lattice of a Hilbert space $H$ is written $P(H)$, and the effect algebra of all effects on $H$ is written $\mathcal{E}(H)$.

## Ortholattices

### Orthocomplementation

**Definition.** An **orthocomplementation** on a bounded lattice $L$ is a map $a \mapsto a^{\perp}$ such that for all $a, b$:

$$
a^{\perp\perp} = a, \qquad a \wedge a^{\perp} = 0, \qquad a \vee a^{\perp} = 1, \qquad a \leq b \implies b^{\perp} \leq a^{\perp} .
$$

A lattice with an orthocomplementation is an **ortholattice**; its elements are **orthogonal**, written $a \perp b$, when $a \leq b^{\perp}$. The **interval** $[0,a]$ is the set $\{x : 0 \leq x \leq a\}$ with the inherited order.

**Theorem.** In an ortholattice, for all $a, b$:

$$
0^{\perp} = 1, \qquad 1^{\perp} = 0, \qquad a \perp b \iff b \perp a, \qquad a \perp a \iff a = 0,
$$

and the De Morgan laws hold in both forms

$$
(a \wedge b)^{\perp} = a^{\perp} \vee b^{\perp}, \qquad (a \vee b)^{\perp} = a^{\perp} \wedge b^{\perp} .
$$

**Proof.** The first two are the definition at $0$ and $1$. Orthogonality is symmetric because $a \leq b^{\perp}$ is equivalent to $b \leq a^{\perp}$, both following from $b^{\perp\perp} = b$ and the order reversal. $a \perp a$ means $a \leq a^{\perp}$, and then $a = a \wedge a^{\perp} = 0$; the converse is clear. For De Morgan, $a^{\perp} \vee b^{\perp} \leq (a \wedge b)^{\perp}$ because $a \wedge b \leq a$ gives $a^{\perp} \leq (a\wedge b)^{\perp}$ and similarly for $b$. For the reverse, put $d = a^{\perp} \vee b^{\perp}$. Since $a^{\perp} \leq d$ and $b^{\perp} \leq d$, the order reversal of the orthocomplement gives $d^{\perp} \leq a$ and $d^{\perp} \leq b$, hence $d^{\perp} \leq a \wedge b$, whence $(a \wedge b)^{\perp} \leq d$ by the order reversal again; the second law is the first applied to $a^{\perp}$ and $b^{\perp}$. $\square$

### The Orthomodular Law

**Definition.** An ortholattice $L$ is **orthomodular** if for all $a, b$

$$
a \leq b \implies b = a \vee (a^{\perp} \wedge b) .
$$

The condition is the **orthomodular law**. It is a weakened distributivity: in a distributive ortholattice the law holds because $a \vee (a^{\perp}\wedge b) = (a\vee a^{\perp})\wedge(a\vee b) = b$ when $a \leq b$.

**Theorem.** The following are equivalent in an ortholattice $L$, for all $a, b$:

1. $a \leq b$ implies $b = a \vee (a^{\perp} \wedge b)$;
2. $a \leq b$ and $a^{\perp} \wedge b = 0$ imply $a = b$;
3. $a \vee (a^{\perp} \wedge (a \vee b)) = a \vee b$;
4. $a \wedge (a^{\perp} \vee (a \wedge b)) = a \wedge b$.

**Proof.** The equivalence of (1), (2) and (3) is the standard list of equivalent forms of the orthomodular law: (2) is the statement that no proper element of the interval $[a,b]$ is orthogonal to $a$, and (3) is (1) with the pair $(a, a \vee b)$ substituted for $(a,b)$, so that $a \vee b$ plays the role of the upper element. The form (4) is the **dual** of (3): applying (3) to the pair $(a^{\perp}, b^{\perp})$ gives $a^{\perp} \vee (a \wedge (a^{\perp} \vee b^{\perp})) = a^{\perp} \vee b^{\perp}$, and taking orthocomplements of both sides and using the De Morgan laws gives $a \wedge (a^{\perp} \vee (a \wedge b)) = a \wedge b$. Since the class of ortholattices is self-dual, (4) is equivalent to (3). The verifications are in the standard references. $\square$

**Example (Boolean algebras).** A Boolean algebra is an ortholattice with $a^{\perp} = \neg a$, and it is orthomodular because it is distributive. Conversely, the next theorem shows that distributivity is the only case: an ortholattice can satisfy at most this much distributivity without collapsing to a Boolean algebra.

**Theorem.** An orthomodular lattice is a Boolean algebra if and only if it is distributive.

**Proof.** A Boolean algebra is distributive. Conversely, in a distributive orthomodular lattice every element has the unique complement $\neg a = a^{\perp}$, and the complemented distributive laws of *Boolean Algebras and Lattices* are satisfied; the verifications are the same as there, with the orthomodular law supplying the identity $a \vee (a^{\perp}\wedge b) = a \vee b$ for $a \leq b$. $\square$

The theorem is the reason the present article belongs to the Boolean category: the Boolean algebras are exactly the distributive members of the class, and every non-distributive orthomodular lattice is a witness that the Boolean laws are not forced by the order and the complement alone.

## The Projection Lattice

### Subspaces of a Hilbert Space

Let $H$ be a Hilbert space over $\mathbb{K} \in \{\mathbb{R}, \mathbb{C}\}$, with inner product written $\langle \cdot, \cdot \rangle$, and let $P(H)$ be the set of closed subspaces of $H$, ordered by inclusion. The meet of two closed subspaces is their intersection and the join is the closure of their sum,

$$
M \wedge N = M \cap N, \qquad M \vee N = \overline{M + N},
$$

and the orthocomplement is the orthogonal complement $M^{\perp}$. This makes $P(H)$ a complete ortholattice.

**Theorem.** $P(H)$ is an orthomodular lattice.

**Proof.** For $M \subseteq N$ one has $N = M \oplus (M^{\perp} \cap N)$: every $n \in N$ decomposes as $n = m + (n - m)$ with $m$ the orthogonal projection of $n$ onto $M$, the difference lying in $M^{\perp} \cap N$, and the sum is direct because $M \cap M^{\perp} = 0$. Hence $N = M \vee (M^{\perp} \cap N)$, which is the orthomodular law. $\square$

### Failure of Distributivity

**Theorem.** $P(H)$ is distributive if and only if $\dim H \leq 1$.

**Proof.** If $\dim H = 1$ then $P(H) = \{0, H\}$ is the two-element Boolean algebra. Suppose $\dim H \geq 2$ and let $L_1 \neq L_2$ be two distinct one-dimensional subspaces. Then

$$
L_1 \wedge (L_1^{\perp} \vee L_2) = L_1 \wedge H = L_1,
$$

because $L_2 \not\subseteq L_1^{\perp}$ forces $L_1^{\perp} \vee L_2 = H$, while

$$
(L_1 \wedge L_1^{\perp}) \vee (L_1 \wedge L_2) = 0 \vee 0 = 0 .
$$

The two are different, so distributivity fails. $\square$

The two-dimensional case already exhibits the failure in its simplest form: the **orthomodular lattice of the plane** is the set $\{0, H\} \cup \{\text{lines through } 0\}$, and three distinct lines $L_1, L_2, L_3$ generate the sublattice with elements $0, L_1, L_2, L_3, H$, in which $L_i \wedge L_j = 0$ and $L_i \vee L_j = H$ for $i \neq j$. This is the five-element modular orthomodular lattice $M_3$, and it is non-distributive, since $L_1 \wedge (L_2 \vee L_3) = L_1$ while $(L_1 \wedge L_2) \vee (L_1 \wedge L_3) = 0$. The six-element **benzene ring** $O_6$, the cycle of four atoms $a, b, c, d$ with $a \perp b$, $b \perp c$, $c \perp d$ and $d \perp a$, is the smallest non-modular orthomodular lattice.

**Remark.** The projection lattice is the standard orthomodular lattice. The **coordinatisation** problem — which orthomodular lattices are isomorphic to a lattice $P(H)$ — is the subject of the theorem of Piron and of the deeper results of the literature; the present article uses only the examples and the abstract theory.

## Effect Algebras

### The Axioms

**Definition.** An **effect algebra** is a set $E$ with distinguished elements $0$ and $1$ and a **partial** binary operation $\oplus$, defined on some pairs and written $a \perp b$ when $a \oplus b$ is defined, such that

**(EA1)** if $a \perp b$, then $b \perp a$ and $a \oplus b = b \oplus a$;

**(EA2)** if $a \perp b$ and $a \oplus b \perp c$, then $b \perp c$, $a \perp b \oplus c$, and $(a \oplus b) \oplus c = a \oplus (b \oplus c)$;

**(EA3)** for every $a \in E$ there is a unique $a' \in E$ with $a \perp a'$ and $a \oplus a' = 1$;

**(EA4)** if $a \perp 1$, then $a = 0$.

The element $a'$ is the **orthosupplement** of $a$. The relation $\leq$ is defined by

$$
a \leq b \iff \text{there is } c \in E \text{ with } a \perp c \text{ and } a \oplus c = b,
$$

and the element $c$, when it exists, is unique and is written $b \ominus a$.

**Theorem.** In an effect algebra the relation $\leq$ is a partial order with least element $0$ and greatest element $1$; moreover $a \oplus 0 = a$ for all $a$, $a'' = a$, $0' = 1$, $1' = 0$, and

$$
a \leq b \iff b' \leq a', \qquad b \ominus a = (a \oplus b')' .
$$

**Proof.** Reflexivity is $a \oplus 0 = a$, which follows from (EA3) applied to $a'$ and (EA1); antisymmetry and transitivity are the standard cancellativity and associativity consequences of (EA2) and (EA3). The order-reversing property of the orthosupplement and the formula for the difference are the standard identities of the theory: if $a \le b$, say $b = a \oplus c$, then $b' = (a\oplus c)' = a' \ominus c \le a'$. The full verification is in the standard references. $\square$

### The Standard Examples

**Example (the unit interval).** Let $E = [0,1] \subseteq \mathbb{R}$ with $a \oplus b$ defined exactly when $a + b \leq 1$, in which case $a \oplus b = a + b$. The axioms hold with $a' = 1 - a$. This effect algebra is lattice-ordered, and its partial sum is the truncated addition of *MV-Algebras and Many-Valued Logic*; it is the effect algebra of a single real interval. Every positive element generates $1$: for $a > 0$, some $n$-fold multiple of $a$ equals $1$, so $[0,1]$ has no nontrivial proper ideals and is simple.

**Example (projections).** Let $H$ be a Hilbert space and let $P(H)$ be its projection lattice. Define $M \oplus N = M \vee N$ when $M \perp N$, that is, when $M \subseteq N^{\perp}$. Then $P(H)$ is an effect algebra with orthosupplement $M' = M^{\perp}$. Here the operation is the join, and the effect algebra is lattice-ordered; this is the case in which the order alone determines the sum.

**Example (effects of an operator algebra).** Let $M$ be a von Neumann algebra and let

$$
\mathcal{E}(M) = \{a \in M : 0 \leq a \leq 1\}
$$

be its set of **effects**, the self-adjoint elements with spectrum in $[0,1]$. Define $a \oplus b$ exactly when $a + b \leq 1$, in which case $a \oplus b = a + b$, and put $a' = 1 - a$. The axioms hold, and $\mathcal{E}(M)$ is the **standard effect algebra** of $M$; the projections are exactly the elements $p$ with $p = p^2$, and they form the orthomodular lattice $P(M)$ inside $\mathcal{E}(M)$. When $M = B(H)$ one writes $\mathcal{E}(H)$.

The projection lattice and the standard effect algebra are the two levels of the same structure: the projections are the *sharp* effects, those that are idempotent, and the effects are the unit interval of the surrounding operator algebra. That operator algebra and the norm on it belong to *Operator Algebras* and *Banach and Hilbert Spaces*; the present article takes only the order and the partial sum.

### Elementary Consequences

**Theorem.** In an effect algebra $E$, for all $a, b, c$:

$$
a \perp b \implies a \oplus b \geq a, \qquad a \leq b \implies b \ominus a \leq b, \qquad a \le b \iff a' \ge b',
$$

and if $a \perp c$ and $b \perp c$ with $a \oplus c = b \oplus c$, then $a = b$.

**Proof.** The first is clear from the order definition, the second follows from $b = a \oplus (b \ominus a)$. The third was stated above. For the cancellation, $a \oplus c = b \oplus c$ and the associativity of $\oplus$ applied to $(a\oplus c)\oplus c'$ give $a \oplus (c \oplus c') = b \oplus (c \oplus c')$, that is, $a \oplus 1 = b \oplus 1$, and by (EA4) applied after subtracting $1$ from the order relation, $a = b$; the argument uses the standard rewritings and is in the references. $\square$

**Definition.** A **sub-effect-algebra** is a subset containing $0, 1$ and closed under $\oplus$ and ${}'$. An **ideal** of $E$ is a subset $I$ with $0 \in I$, closed under $\oplus$, and downward closed. The **compatibility** relation is

$$
a \leftrightarrow b \iff \text{there exist } a_1, b_1, c \in E \text{ with } a = a_1 \oplus c,\ b = b_1 \oplus c,\ a_1 \perp b_1 .
$$

Two elements are compatible exactly when they lie in a common Boolean sub-effect-algebra; a maximal such subalgebra is a **block**, and the blocks are the pieces from which the non-distributive algebra is assembled.

## The Two Directions of Generalisation

### Orthomodular Lattices as Effect Algebras

**Theorem.** Let $L$ be an orthomodular lattice. Define $a \oplus b = a \vee b$ exactly when $a \perp b$. Then $L$ is an effect algebra, with orthosupplement $a' = a^{\perp}$, and the effect-algebra order is the lattice order. Conversely, an effect algebra that is a lattice and in which $a \oplus b = a \vee b$ for orthogonal $a,b$ is an orthomodular lattice, with $a^{\perp} = a'$.

**Proof.** The axioms (EA1)–(EA4) are the ortholattice laws for orthogonal pairs: (EA1) is the symmetry of orthogonality, (EA2) is associativity for pairwise orthogonal elements, which holds in any lattice because all three joins agree, (EA3) is the existence of the orthocomplement, and (EA4) is $a \le 1^{\perp} = 0$. The orthomodular law is exactly what is needed for the effect-algebra order to recover the lattice order on the whole lattice and not only on the orthogonal pairs: if $a \leq b$ in $L$, then $b = a \vee (a^{\perp}\wedge b) = a \oplus (a^{\perp}\wedge b)$ with $a \perp a^{\perp}\wedge b$, so $a \leq b$ in the effect-algebra order; the converse is immediate. $\square$

### MV-Algebras as Lattice-Ordered Effect Algebras

**Theorem.** An effect algebra is an MV-algebra if and only if it is lattice-ordered and satisfies the **Riesz decomposition property**: if $c \leq a \oplus b$, then $c = a_1 \oplus b_1$ with $a_1 \leq a$ and $b_1 \leq b$.

**Proof.** In an MV-algebra the partial sum $a \oplus b$ defined exactly when $a \odot \neg b = 0$ makes it an effect algebra, and the lattice order together with Riesz decomposition is the standard characterisation of the MV-algebras among the effect algebras; the decomposition property is what converts the partial sum into the total $\oplus$ of *MV-Algebras and Many-Valued Logic*. The argument is due to Mundici and is quoted. $\square$

The two theorems place the Boolean category in a single picture. An effect algebra is a partial sum with a top and an orthosupplement; adding lattice-orderedness and the Riesz decomposition property gives the MV-algebras; adding instead the condition that the sum be the join on orthogonal pairs gives the orthomodular lattices; and requiring both distributivity and compatibility with the lattice order returns the Boolean algebras. The classes are summarised by the table.

| Structure | Order | Sum | Complement |
|---|---|---|---|
| Boolean algebra | distributive lattice | join, total | Boolean complement |
| MV-algebra | distributive lattice | truncated, total | involution $\neg$ |
| Heyting algebra | distributive lattice | not a monoid | pseudocomplement |
| Orthomodular lattice | orthomodular lattice | join on orthogonal pairs | orthocomplement |
| Effect algebra | partial order | partial, axioms (EA1)–(EA4) | orthosupplement |

## States and Blocks

### States

**Definition.** A **state** on an effect algebra $E$ is a function $s : E \to [0,1]$ with $s(1) = 1$ and $s(a \oplus b) = s(a) + s(b)$ whenever $a \perp b$. The set of states is the **state space** $S(E)$, a convex set. A state is **faithful** if $s(a) = 0$ implies $a = 0$, and **sharp** if $s(a) \in \{0,1\}$ for all $a$.

**Theorem.** On the effect algebra $[0,1]$ the only state is the identity.

**Proof.** Let $s$ be a state. Additivity on the partial sum gives $s(k/n) = k/n$ for all $0 \leq k \leq n$ by $k$-fold addition of $1/n$, and monotonicity, which follows from the order definition, gives $s(a) = a$ for irrational $a$ as well. $\square$

**Theorem (Gleason).** Let $H$ be a Hilbert space with $\dim H \geq 3$. Then every state $s$ on the projection lattice $P(H)$ has the form

$$
s(M) = \operatorname{tr}(\rho \, p_M)
$$

for a unique positive trace-class operator $\rho$ of trace one, where $p_M$ is the orthogonal projection onto $M$; conversely every such operator defines a state. In the finite-dimensional case with $\dim H \geq 3$ the same formula holds, and the state $M \mapsto \dim M / \dim H$ is the one given by the scalar density $\rho = (\dim H)^{-1} I$, which is faithful.

**Proof.** The theorem is Gleason's; the argument uses the additivity of $s$ on families of mutually orthogonal subspaces and the classification of the resulting measures. In finite dimension the trace formula follows from the spectral theorem for the density operator. The hypothesis $\dim H \geq 3$ is necessary: for $\dim H = 2$ the projection lattice is the diamond $\{0, L_1, L_2, H\}$ of the two lines $L_1 \neq L_2$ and the whole plane, and there are states on it that are not of the trace form, which is the finite-dimensional content of the hidden-variable question below. $\square$

The state space is the mathematical subject of the **hidden-variable question**: an orthomodular lattice may admit no state at all, and the finite **Greechie diagrams** exhibit orthomodular lattices with only two-valued states or with none, showing that the axioms do not force the existence of a probability measure. This is a theorem about finite lattices and their states, and the present article records it as such.

### Blocks

**Definition.** Two elements $a, b$ of an effect algebra are **compatible**, written $a \leftrightarrow b$, if there exist $a_1, b_1, c$ with

$$
a = a_1 \oplus c, \qquad b = b_1 \oplus c, \qquad a_1 \perp b_1 .
$$

A **block** is a maximal set of pairwise compatible elements; a block is a Boolean sub-effect-algebra.

**Theorem.** Every orthomodular lattice is the union of its blocks, and the center

$$
Z(L) = \{a \in L : a \leftrightarrow b \text{ for every } b \in L\}
$$

of an orthomodular lattice is a Boolean algebra.

**Proof.** In an orthomodular lattice, two elements are compatible exactly when they generate a Boolean subalgebra, and every element belongs to a maximal such subalgebra, so the blocks cover $L$. The center consists of the elements compatible with all others, so the sublattice it generates is Boolean; the verification is the standard center theorem for orthomodular lattices. $\square$

**Example.** The projection lattice $P(H)$ is irreducible for $\dim H \geq 2$, its center being $\{0, I\}$; its blocks are the Boolean algebras of projections lying in a maximal commutative subalgebra of the operator algebra, and the spectral theorem states that every projection lies in one of them. The standard effect algebra $\mathcal{E}(H)$ contains $P(H)$ as its sharp elements, and the projections of $\mathcal{E}(H)$ are exactly the elements $a$ with $a = a^2$. The operator algebra, its norm and its commutative subalgebras belong to *Operator Algebras*; only the compatibility and the block structure are used here.

## Summary

An ortholattice is a bounded lattice with an order-reversing involution $a \mapsto a^{\perp}$ satisfying $a \wedge a^{\perp} = 0$ and $a \vee a^{\perp} = 1$; it is orthomodular when $a \leq b$ implies $b = a \vee (a^{\perp}\wedge b)$, and an orthomodular lattice is a Boolean algebra exactly when it is distributive. The projection lattice $P(H)$ of a Hilbert space is the standard orthomodular lattice; it is distributive only for $\dim H \leq 1$, and for $\dim H \geq 2$ its failure of distributivity is witnessed already by three lines in a plane. An effect algebra is a set with a partial commutative associative sum, a top $1$ and an orthosupplement $a'$ with $a \oplus a' = 1$; every orthomodular lattice is an effect algebra with the sum equal to the join on orthogonal pairs, and the lattice-ordered effect algebras with the Riesz decomposition property are exactly the MV-algebras, so the Boolean algebras are the common distributive case.

The effects of a von Neumann algebra, the self-adjoint elements with spectrum in $[0,1]$, form the standard effect algebra $\mathcal{E}(M)$, in which the projections are the idempotent elements and form the orthomodular lattice $P(M)$; the operators and their norm belong to functional analysis, and the present article uses only the order and the partial sum. States are the additive functionals to $[0,1]$; on the unit interval the identity is the only state, and on the projection lattice of a Hilbert space of dimension at least three Gleason's theorem identifies the states with the density operators. The compatibility relation organises an orthomodular lattice into Boolean blocks, its center is a Boolean algebra, and every orthomodular lattice is covered by its blocks. The Boolean system thus supports one algebra and no analysis, and the non-distributive generalisations of this article are its widest purely algebraic extension, the analysis entering only through the operator-algebra models of Part III.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L$ | An ortholattice or orthomodular lattice |
| $a^{\perp}$ | Orthocomplement, an order-reversing involution |
| $a \perp b$ | Orthogonality, $a \leq b^{\perp}$ |
| $a \wedge b$, $a \vee b$ | Meet and join of the lattice order |
| $0, 1$ | Least and greatest elements |
| $P(H)$ | Projection lattice of a Hilbert space, ordered by inclusion |
| $M^{\perp}$ | Orthogonal complement of a closed subspace |
| $E$ | An effect algebra |
| $\oplus$ | Partial commutative associative sum |
| $a'$ | Orthosupplement, $a \oplus a' = 1$ |
| $b \ominus a$ | Difference, the unique $c$ with $a \oplus c = b$ when $a \leq b$ |
| $\mathcal{E}(M)$, $\mathcal{E}(H)$ | Standard effect algebra of the effects, $\{a : 0 \leq a \leq 1\}$ |
| $a \leftrightarrow b$ | Compatibility |
| $Z(E)$ | Center, the elements compatible with everything |
| $S(E)$ | State space |
| $H$ | A Hilbert space over $\mathbb{K} \in \{\mathbb{R}, \mathbb{C}\}$ |

## Further Reading

- Garrett Birkhoff and John von Neumann, "The logic of quantum mechanics", *Annals of Mathematics* 37 (1936), for the origin of orthomodular lattices as models of non-distributive logic, treated as mathematics.
- D. J. Foulis and M. K. Bennett, "Effect algebras and unsharp quantum logics", *Foundations of Physics* 24 (1994), for the axioms of effect algebras and their elementary theory.
- Stan Gudder, "Effect algebras and uniquely complemented partial groups", *International Journal of Theoretical Physics* 37 (1998), for the structure of effect algebras and their blocks.
- Gudrun Kalmbach, *Orthomodular Lattices* (Academic Press, 1983), for the systematic theory of orthomodular lattices, their states and their coordinatisation.
- Anatolij Dvurečenskij and Sylvia Pulmannová, *New Trends in Quantum Structures* (Kluwer, 2000), for effect algebras, the Riesz decomposition property and the MV-algebra connection.
- Andrew M. Gleason, "Measures on the closed subspaces of a Hilbert space", *Journal of Mathematics and Mechanics* 6 (1957), for the classification of states on projection lattices.
- Richard J. Greechie, "Orthomodular lattices admitting no states", *Journal of Combinatorial Theory* 10 (1971), for the finite examples with no state, presented by the diagrams bearing his name.
