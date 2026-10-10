
# __Effect Algebras and Orthomodular Lattices__

## Introduction

This is the fourth article of the Boolean system in Part V, and it occupies the **algebra slot** of that system for the *non-distributive* reading of the domain. The systems of the preceding three articles — Boolean, Heyting and MV — all rest on distributive lattices, and their complementation is unique. The algebras of this article, the **orthomodular lattices** and the **effect algebras**, retain an order and an orthocomplementation but abandon distributivity; the complement need not be a Boolean complement, and the lattice laws that the earlier articles used are replaced by weaker ones.

The boundary against the general theory is deliberate. Lattices, modularity and the forbidden-sublattice criterion are the subject of *Order Theory and Lattices*; the Boolean case is *Boolean Algebras and Lattices*; the distributive negations are *Heyting Algebras and Intuitionistic Logic* and *MV-Algebras and Many-Valued Logic*. The models of the present algebras come from functional analysis: the projection lattice of a Hilbert space is the standard orthomodular lattice, and the unit interval of a von Neumann algebra is the standard effect algebra. Those objects are constructed in *Banach and Hilbert Spaces* and *Operator Algebras*, and are used here as examples; the present article develops the abstract algebra only. No physics is invoked, and no topology, distance or Hilbert-space structure is developed beyond what the examples require.

Throughout, an ortholattice is written $(L, \wedge, \vee, {}^{\perp}, 0, 1)$ with orthocomplement $\alpha^{\perp}$, and an effect algebra is written $(E, \oplus, 0, 1)$ with orthosupplement $\alpha'$. When an effect algebra is lattice-ordered and its partial sum is the join on orthogonal pairs, its orthosupplement coincides with the orthocomplement of the resulting orthomodular lattice; this is stated precisely below. The projection lattice of a Hilbert space $H$ is written $P(H)$, and the effect algebra of all effects on $H$ is written $\mathcal{E}(H)$.

## Ortholattices

### Orthocomplementation

**Definition.** An **orthocomplementation** on a bounded lattice $L$ is a map $\alpha \mapsto \alpha^{\perp}$ such that for all $\alpha, \beta$:

$$
\alpha^{\perp\perp} = \alpha, \qquad \alpha \wedge \alpha^{\perp} = 0, \qquad \alpha \vee \alpha^{\perp} = 1, \qquad \alpha \leq \beta \implies \beta^{\perp} \leq \alpha^{\perp} .
$$

A lattice with an orthocomplementation is an **ortholattice**; its elements are **orthogonal**, written $\alpha \perp \beta$, when $\alpha \leq \beta^{\perp}$. The **interval** $[0,\alpha]$ is the set $\{\beta : 0 \leq \beta \leq \alpha\}$ with the inherited order.

**Theorem.** In an ortholattice, for all $\alpha, \beta$:

$$
0^{\perp} = 1, \qquad 1^{\perp} = 0, \qquad \alpha \perp \beta \iff \beta \perp \alpha, \qquad \alpha \perp \alpha \iff \alpha = 0,
$$

and the De Morgan laws hold in both forms

$$
(\alpha \wedge \beta)^{\perp} = \alpha^{\perp} \vee \beta^{\perp}, \qquad (\alpha \vee \beta)^{\perp} = \alpha^{\perp} \wedge \beta^{\perp} .
$$

**Proof.** The first two are the definition at $0$ and $1$. Orthogonality is symmetric because $\alpha \leq \beta^{\perp}$ is equivalent to $\beta \leq \alpha^{\perp}$, both following from $\beta^{\perp\perp} = \beta$ and the order reversal. $\alpha \perp \alpha$ means $\alpha \leq \alpha^{\perp}$, and then $\alpha = \alpha \wedge \alpha^{\perp} = 0$; the converse is clear. For De Morgan, $\alpha^{\perp} \vee \beta^{\perp} \leq (\alpha \wedge \beta)^{\perp}$ because $\alpha \wedge \beta \leq \alpha$ gives $\alpha^{\perp} \leq (\alpha\wedge \beta)^{\perp}$ and similarly for $\beta$. For the reverse, put $\delta = \alpha^{\perp} \vee \beta^{\perp}$. Since $\alpha^{\perp} \leq \delta$ and $\beta^{\perp} \leq \delta$, the order reversal of the orthocomplement gives $\delta^{\perp} \leq \alpha$ and $\delta^{\perp} \leq \beta$, hence $\delta^{\perp} \leq \alpha \wedge \beta$, whence $(\alpha \wedge \beta)^{\perp} \leq \delta$ by the order reversal again; the second law is the first applied to $\alpha^{\perp}$ and $\beta^{\perp}$.

### The Orthomodular Law

**Definition.** An ortholattice $L$ is **orthomodular** if for all $\alpha, \beta$

$$
\alpha \leq \beta \implies \beta = \alpha \vee (\alpha^{\perp} \wedge \beta) .
$$

The condition is the **orthomodular law**. It is a weakened distributivity: in a distributive ortholattice the law holds because $\alpha \vee (\alpha^{\perp}\wedge \beta) = (\alpha\vee \alpha^{\perp})\wedge(\alpha\vee \beta) = \beta$ when $\alpha \leq \beta$.

**Theorem.** The following are equivalent in an ortholattice $L$, for all $\alpha, \beta$:

1. $\alpha \leq \beta$ implies $\beta = \alpha \vee (\alpha^{\perp} \wedge \beta)$;
2. $\alpha \leq \beta$ and $\alpha^{\perp} \wedge \beta = 0$ imply $\alpha = \beta$;
3. $\alpha \vee (\alpha^{\perp} \wedge (\alpha \vee \beta)) = \alpha \vee \beta$;
4. $\alpha \wedge (\alpha^{\perp} \vee (\alpha \wedge \beta)) = \alpha \wedge \beta$.

**Proof.** The equivalence of (1), (2) and (3) is the standard list of equivalent forms of the orthomodular law: (2) is the statement that no proper element of the interval $[\alpha,\beta]$ is orthogonal to $\alpha$, and (3) is (1) with the pair $(\alpha, \alpha \vee \beta)$ substituted for $(\alpha,\beta)$, so that $\alpha \vee \beta$ plays the role of the upper element. The form (4) is the **dual** of (3): applying (3) to the pair $(\alpha^{\perp}, \beta^{\perp})$ gives $\alpha^{\perp} \vee (\alpha \wedge (\alpha^{\perp} \vee \beta^{\perp})) = \alpha^{\perp} \vee \beta^{\perp}$, and taking orthocomplements of both sides and using the De Morgan laws gives $\alpha \wedge (\alpha^{\perp} \vee (\alpha \wedge \beta)) = \alpha \wedge \beta$. Since the class of ortholattices is self-dual, (4) is equivalent to (3). The verifications are in the standard references.

**Example (Boolean algebras).** A Boolean algebra is an ortholattice with $\alpha^{\perp} = \neg \alpha$, and it is orthomodular because it is distributive. Conversely, the next theorem shows that distributivity is the only case: an ortholattice can satisfy at most this much distributivity without collapsing to a Boolean algebra.

**Theorem.** An orthomodular lattice is a Boolean algebra if and only if it is distributive.

**Proof.** A Boolean algebra is distributive. Conversely, in a distributive orthomodular lattice every element has the unique complement $\neg \alpha = \alpha^{\perp}$, and the complemented distributive laws of *Boolean Algebras and Lattices* are satisfied; the verifications are the same as there, with the orthomodular law supplying the identity $\alpha \vee (\alpha^{\perp}\wedge \beta) = \alpha \vee \beta$ for $\alpha \leq \beta$.

The theorem is the reason the present article belongs to the Boolean category: the Boolean algebras are exactly the distributive members of the class, and every non-distributive orthomodular lattice is a witness that the Boolean laws are not forced by the order and the complement alone.

## The Projection Lattice

### Subspaces of a Hilbert Space

Let $H$ be a Hilbert space over $\mathbb{K} \in \{\mathbb{R}, \mathbb{C}\}$, with inner product written $\langle \cdot, \cdot \rangle$, and let $P(H)$ be the set of closed subspaces of $H$, ordered by inclusion. The meet of two closed subspaces is their intersection and the join is the closure of their sum,

$$
M \wedge N = M \cap N, \qquad M \vee N = \overline{M + N},
$$

and the orthocomplement is the orthogonal complement $M^{\perp}$. This makes $P(H)$ a complete ortholattice.

**Theorem.** $P(H)$ is an orthomodular lattice.

**Proof.** For $M \subseteq N$ one has $N = M \oplus (M^{\perp} \cap N)$: every $n \in N$ decomposes as $n = m + (n - m)$ with $m$ the orthogonal projection of $n$ onto $M$, the difference lying in $M^{\perp} \cap N$, and the sum is direct because $M \cap M^{\perp} = 0$. Hence $N = M \vee (M^{\perp} \cap N)$, which is the orthomodular law.

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

The two are different, so distributivity fails.

The two-dimensional case already exhibits the failure in its simplest form: the **orthomodular lattice of the plane** is the set $\{0, H\} \cup \{\text{lines through } 0\}$, and three distinct lines $L_1, L_2, L_3$ generate the sublattice with elements $0, L_1, L_2, L_3, H$, in which $L_i \wedge L_j = 0$ and $L_i \vee L_j = H$ for $i \neq j$. This is the five-element modular orthomodular lattice $M_3$, and it is non-distributive, since $L_1 \wedge (L_2 \vee L_3) = L_1$ while $(L_1 \wedge L_2) \vee (L_1 \wedge L_3) = 0$. The six-element **benzene ring** $O_6$, the cycle of four atoms $\alpha, \beta, \gamma, \delta$ with $\alpha \perp \beta$, $\beta \perp \gamma$, $\gamma \perp \delta$ and $\delta \perp \alpha$, is the smallest non-modular orthomodular lattice.

**Remark.** The projection lattice is the standard orthomodular lattice. The **coordinatisation** problem — which orthomodular lattices are isomorphic to a lattice $P(H)$ — is the subject of the theorem of Piron and of the deeper results of the literature; the present article uses only the examples and the abstract theory.

## Effect Algebras

### The Axioms

**Definition.** An **effect algebra** is a set $E$ with distinguished elements $0$ and $1$ and a **partial** binary operation $\oplus$, defined on some pairs and written $\alpha \perp \beta$ when $\alpha \oplus \beta$ is defined, such that

**(EA1)** if $\alpha \perp \beta$, then $\beta \perp \alpha$ and $\alpha \oplus \beta = \beta \oplus \alpha$;

**(EA2)** if $\alpha \perp \beta$ and $\alpha \oplus \beta \perp \gamma$, then $\beta \perp \gamma$, $\alpha \perp \beta \oplus \gamma$, and $(\alpha \oplus \beta) \oplus \gamma = \alpha \oplus (\beta \oplus \gamma)$;

**(EA3)** for every $\alpha \in E$ there is a unique $\alpha' \in E$ with $\alpha \perp \alpha'$ and $\alpha \oplus \alpha' = 1$;

**(EA4)** if $\alpha \perp 1$, then $\alpha = 0$.

The element $\alpha'$ is the **orthosupplement** of $\alpha$. The relation $\leq$ is defined by

$$
\alpha \leq \beta \iff \text{there is } \gamma \in E \text{ with } \alpha \perp \gamma \text{ and } \alpha \oplus \gamma = \beta,
$$

and the element $\gamma$, when it exists, is unique and is written $\beta \ominus \alpha$.

**Theorem.** In an effect algebra the relation $\leq$ is a partial order with least element $0$ and greatest element $1$; moreover $\alpha \oplus 0 = \alpha$ for all $\alpha$, $\alpha'' = \alpha$, $0' = 1$, $1' = 0$, and

$$
\alpha \leq \beta \iff \beta' \leq \alpha', \qquad \beta \ominus \alpha = (\alpha \oplus \beta')' .
$$

**Proof.** Reflexivity is $\alpha \oplus 0 = \alpha$, which follows from (EA3) applied to $\alpha'$ and (EA1); antisymmetry and transitivity are the standard cancellativity and associativity consequences of (EA2) and (EA3). The order-reversing property of the orthosupplement and the formula for the difference are the standard identities of the theory: if $\alpha \le \beta$, say $\beta = \alpha \oplus \gamma$, then $\beta' = (\alpha\oplus \gamma)' = \alpha' \ominus \gamma \le \alpha'$. The full verification is in the standard references.

### The Standard Examples

**Example (the unit interval).** Let $E = [0,1] \subseteq \mathbb{R}$ with $\alpha \oplus \beta$ defined exactly when $\alpha + \beta \leq 1$, in which case $\alpha \oplus \beta = \alpha + \beta$. The axioms hold with $\alpha' = 1 - \alpha$. This effect algebra is lattice-ordered, and its partial sum is the truncated addition of *MV-Algebras and Many-Valued Logic*; it is the effect algebra of a single real interval. Every positive element generates $1$: for $\alpha > 0$, some $n$-fold multiple of $\alpha$ equals $1$, so $[0,1]$ has no nontrivial proper ideals and is simple.

**Example (projections).** Let $H$ be a Hilbert space and let $P(H)$ be its projection lattice. Define $M \oplus N = M \vee N$ when $M \perp N$, that is, when $M \subseteq N^{\perp}$. Then $P(H)$ is an effect algebra with orthosupplement $M' = M^{\perp}$. Here the operation is the join, and the effect algebra is lattice-ordered; this is the case in which the order alone determines the sum.

**Example (effects of an operator algebra).** Let $M$ be a von Neumann algebra and let

$$
\mathcal{E}(M) = \{\alpha \in M : 0 \leq \alpha \leq 1\}
$$

be its set of **effects**, the self-adjoint elements with spectrum in $[0,1]$. Define $\alpha \oplus \beta$ exactly when $\alpha + \beta \leq 1$, in which case $\alpha \oplus \beta = \alpha + \beta$, and put $\alpha' = 1 - \alpha$. The axioms hold, and $\mathcal{E}(M)$ is the **standard effect algebra** of $M$; the projections are exactly the elements $p$ with $p = p^2$, and they form the orthomodular lattice $P(M)$ inside $\mathcal{E}(M)$. When $M = B(H)$ one writes $\mathcal{E}(H)$.

The projection lattice and the standard effect algebra are the two levels of the same structure: the projections are the *sharp* effects, those that are idempotent, and the effects are the unit interval of the surrounding operator algebra. That operator algebra and the norm on it belong to *Operator Algebras* and *Banach and Hilbert Spaces*; the present article takes only the order and the partial sum.

### Elementary Consequences

**Theorem.** In an effect algebra $E$, for all $\alpha, \beta, \gamma$:

$$
\alpha \perp \beta \implies \alpha \oplus \beta \geq \alpha, \qquad \alpha \leq \beta \implies \beta \ominus \alpha \leq \beta, \qquad \alpha \le \beta \iff \alpha' \ge \beta',
$$

and if $\alpha \perp \gamma$ and $\beta \perp \gamma$ with $\alpha \oplus \gamma = \beta \oplus \gamma$, then $\alpha = \beta$.

**Proof.** The first is clear from the order definition, the second follows from $\beta = \alpha \oplus (\beta \ominus \alpha)$. The third was stated above. For the cancellation, $\alpha \oplus \gamma = \beta \oplus \gamma$ and the associativity of $\oplus$ applied to $(\alpha\oplus \gamma)\oplus \gamma'$ give $\alpha \oplus (\gamma \oplus \gamma') = \beta \oplus (\gamma \oplus \gamma')$, that is, $\alpha \oplus 1 = \beta \oplus 1$, and by (EA4) applied after subtracting $1$ from the order relation, $\alpha = \beta$; the argument uses the standard rewritings and is in the references.

**Definition.** A **sub-effect-algebra** is a subset containing $0, 1$ and closed under $\oplus$ and ${}'$. An **ideal** of $E$ is a subset $I$ with $0 \in I$, closed under $\oplus$, and downward closed. The **compatibility** relation is

$$
\alpha \leftrightarrow \beta \iff \text{there exist } \alpha_1, \beta_1, \gamma \in E \text{ with } \alpha = \alpha_1 \oplus \gamma,\ \beta = \beta_1 \oplus \gamma,\ \alpha_1 \perp \beta_1 .
$$

Two elements are compatible exactly when they lie in a common Boolean sub-effect-algebra; a maximal such subalgebra is a **block**, and the blocks are the pieces from which the non-distributive algebra is assembled.

## The Two Directions of Generalisation

### Orthomodular Lattices as Effect Algebras

**Theorem.** Let $L$ be an orthomodular lattice. Define $\alpha \oplus \beta = \alpha \vee \beta$ exactly when $\alpha \perp \beta$. Then $L$ is an effect algebra, with orthosupplement $\alpha' = \alpha^{\perp}$, and the effect-algebra order is the lattice order. Conversely, an effect algebra that is a lattice and in which $\alpha \oplus \beta = \alpha \vee \beta$ for orthogonal $\alpha,\beta$ is an orthomodular lattice, with $\alpha^{\perp} = \alpha'$.

**Proof.** The axioms (EA1)–(EA4) are the ortholattice laws for orthogonal pairs: (EA1) is the symmetry of orthogonality, (EA2) is associativity for pairwise orthogonal elements, which holds in any lattice because all three joins agree, (EA3) is the existence of the orthocomplement, and (EA4) is $\alpha \le 1^{\perp} = 0$. The orthomodular law is exactly what is needed for the effect-algebra order to recover the lattice order on the whole lattice and not only on the orthogonal pairs: if $\alpha \leq \beta$ in $L$, then $\beta = \alpha \vee (\alpha^{\perp}\wedge \beta) = \alpha \oplus (\alpha^{\perp}\wedge \beta)$ with $\alpha \perp \alpha^{\perp}\wedge \beta$, so $\alpha \leq \beta$ in the effect-algebra order; the converse is immediate.

### MV-Algebras as Lattice-Ordered Effect Algebras

**Theorem.** An effect algebra is an MV-algebra if and only if it is lattice-ordered and satisfies the **Riesz decomposition property**: if $\gamma \leq \alpha \oplus \beta$, then $\gamma = \alpha_1 \oplus \beta_1$ with $\alpha_1 \leq \alpha$ and $\beta_1 \leq \beta$.

**Proof.** In an MV-algebra the partial sum $\alpha \oplus \beta$ defined exactly when $\alpha \odot \neg \beta = 0$ makes it an effect algebra, and the lattice order together with Riesz decomposition is the standard characterisation of the MV-algebras among the effect algebras; the decomposition property is what converts the partial sum into the total $\oplus$ of *MV-Algebras and Many-Valued Logic*. The argument is due to Mundici and is quoted.

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

**Definition.** A **state** on an effect algebra $E$ is a function $s : E \to [0,1]$ with $s(1) = 1$ and $s(\alpha \oplus \beta) = s(\alpha) + s(\beta)$ whenever $\alpha \perp \beta$. The set of states is the **state space** $S(E)$, a convex set. A state is **faithful** if $s(\alpha) = 0$ implies $\alpha = 0$, and **sharp** if $s(\alpha) \in \{0,1\}$ for all $\alpha$.

**Theorem.** On the effect algebra $[0,1]$ the only state is the identity.

**Proof.** Let $s$ be a state. Additivity on the partial sum gives $s(k/n) = k/n$ for all $0 \leq k \leq n$ by $k$-fold addition of $1/n$, and monotonicity, which follows from the order definition, gives $s(\alpha) = \alpha$ for irrational $\alpha$ as well.

**Theorem (Gleason).** Let $H$ be a Hilbert space with $\dim H \geq 3$. Then every state $s$ on the projection lattice $P(H)$ has the form

$$
s(M) = \operatorname{tr}(\rho \, p_M)
$$

for a unique positive trace-class operator $\rho$ of trace one, where $p_M$ is the orthogonal projection onto $M$; conversely every such operator defines a state. In the finite-dimensional case with $\dim H \geq 3$ the same formula holds, and the state $M \mapsto \dim M / \dim H$ is the one given by the scalar density $\rho = (\dim H)^{-1} I$, which is faithful.

**Proof.** The theorem is Gleason's; the argument uses the additivity of $s$ on families of mutually orthogonal subspaces and the classification of the resulting measures. In finite dimension the trace formula follows from the spectral theorem for the density operator. The hypothesis $\dim H \geq 3$ is necessary: for $\dim H = 2$ the projection lattice is the diamond $\{0, L_1, L_2, H\}$ of the two lines $L_1 \neq L_2$ and the whole plane, and there are states on it that are not of the trace form, which is the finite-dimensional content of the hidden-variable question below.

The state space is the mathematical subject of the **hidden-variable question**: an orthomodular lattice may admit no state at all, and the finite **Greechie diagrams** exhibit orthomodular lattices with only two-valued states or with none, showing that the axioms do not force the existence of a probability measure. This is a theorem about finite lattices and their states, and the present article records it as such.

### Blocks

**Definition.** Two elements $\alpha, \beta$ of an effect algebra are **compatible**, written $\alpha \leftrightarrow \beta$, if there exist $\alpha_1, \beta_1, \gamma$ with

$$
\alpha = \alpha_1 \oplus \gamma, \qquad \beta = \beta_1 \oplus \gamma, \qquad \alpha_1 \perp \beta_1 .
$$

A **block** is a maximal set of pairwise compatible elements; a block is a Boolean sub-effect-algebra.

**Theorem.** Every orthomodular lattice is the union of its blocks, and the centre

$$
Z(L) = \{\alpha \in L : \alpha \leftrightarrow \beta \text{ for every } \beta \in L\}
$$

of an orthomodular lattice is a Boolean algebra.

**Proof.** In an orthomodular lattice, two elements are compatible exactly when they generate a Boolean subalgebra, and every element belongs to a maximal such subalgebra, so the blocks cover $L$. The centre consists of the elements compatible with all others, so the sublattice it generates is Boolean; the verification is the standard centre theorem for orthomodular lattices.

**Example.** The projection lattice $P(H)$ is irreducible for $\dim H \geq 2$, its centre being $\{0, I\}$; its blocks are the Boolean algebras of projections lying in a maximal commutative subalgebra of the operator algebra, and the spectral theorem states that every projection lies in one of them. The standard effect algebra $\mathcal{E}(H)$ contains $P(H)$ as its sharp elements, and the projections of $\mathcal{E}(H)$ are exactly the elements $\alpha$ with $\alpha = \alpha^2$. The operator algebra, its norm and its commutative subalgebras belong to *Operator Algebras*; only the compatibility and the block structure are used here.

## Summary

An ortholattice is a bounded lattice with an order-reversing involution $\alpha \mapsto \alpha^{\perp}$ satisfying $\alpha \wedge \alpha^{\perp} = 0$ and $\alpha \vee \alpha^{\perp} = 1$; it is orthomodular when $\alpha \leq \beta$ implies $\beta = \alpha \vee (\alpha^{\perp}\wedge \beta)$, and an orthomodular lattice is a Boolean algebra exactly when it is distributive. The projection lattice $P(H)$ of a Hilbert space is the standard orthomodular lattice; it is distributive only for $\dim H \leq 1$, and for $\dim H \geq 2$ its failure of distributivity is witnessed already by three lines in a plane. An effect algebra is a set with a partial commutative associative sum, a top $1$ and an orthosupplement $\alpha'$ with $\alpha \oplus \alpha' = 1$; every orthomodular lattice is an effect algebra with the sum equal to the join on orthogonal pairs, and the lattice-ordered effect algebras with the Riesz decomposition property are exactly the MV-algebras, so the Boolean algebras are the common distributive case.

The effects of a von Neumann algebra, the self-adjoint elements with spectrum in $[0,1]$, form the standard effect algebra $\mathcal{E}(M)$, in which the projections are the idempotent elements and form the orthomodular lattice $P(M)$; the operators and their norm belong to functional analysis, and the present article uses only the order and the partial sum. States are the additive functionals to $[0,1]$; on the unit interval the identity is the only state, and on the projection lattice of a Hilbert space of dimension at least three Gleason's theorem identifies the states with the density operators. The compatibility relation organises an orthomodular lattice into Boolean blocks, its centre is a Boolean algebra, and every orthomodular lattice is covered by its blocks. The Boolean system thus supports one algebra and no analysis, and the non-distributive generalisations of this article are its widest purely algebraic extension, the analysis entering only through the operator-algebra models of Part III.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L$ | An ortholattice or orthomodular lattice |
| $\alpha^{\perp}$ | Orthocomplement, an order-reversing involution |
| $\alpha \perp \beta$ | Orthogonality, $\alpha \leq \beta^{\perp}$ |
| $\alpha \wedge \beta$, $\alpha \vee \beta$ | Meet and join of the lattice order |
| $0, 1$ | Least and greatest elements |
| $P(H)$ | Projection lattice of a Hilbert space, ordered by inclusion |
| $M^{\perp}$ | Orthogonal complement of a closed subspace |
| $E$ | An effect algebra |
| $\oplus$ | Partial commutative associative sum |
| $\alpha'$ | Orthosupplement, $\alpha \oplus \alpha' = 1$ |
| $\beta \ominus \alpha$ | Difference, the unique $\gamma$ with $\alpha \oplus \gamma = \beta$ when $\alpha \leq \beta$ |
| $\mathcal{E}(M)$, $\mathcal{E}(H)$ | Standard effect algebra of the effects, $\{\alpha : 0 \leq \alpha \leq 1\}$ |
| $\alpha \leftrightarrow \beta$ | Compatibility |
| $Z(E)$ | Centre, the elements compatible with everything |
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
