# __Operators on a Fixed Set__

## Introduction

There are two canonical ways to build a topology on a set: specify its open sets, or specify an operator on its subsets that is to be the closure. The second is the older and the more algebraic of the two. A **closure operator** on the power set of a set $X$ is a map $C$ satisfying the four **Kuratowski axioms** — it fixes the empty set, it is extensive, it is idempotent, and it distributes over finite unions — and the closed sets of a topology are recovered from $C$ as its fixed points. The **interior operator** $I$ is the dual operator, and it satisfies the dual axioms. Together they generate a small finite monoid of composed operators, and the study of that monoid is a complete and self-contained piece of the theory of a single topological space.

This article defines the two operators, proves the theorem that a closure operator is the same thing as a topology, records the relation $I = \complement\,C\,\complement$ that makes interior and closure dual, and develops the boundary as their meet. It then proves the two classical finiteness theorems for the monoid of operations: at most **fourteen** distinct sets arise from a fixed subset of a topological space by repeated closures and complements, and at most **seven** arise by repeated closures and interiors. Both bounds are sharp, and the sharpness is exhibited on a single subset of the real line.

The space is that of *Topological Spaces*: open and closed sets, interior and closure, and the definition of a topology by its closed sets. The preimage and direct image operators of a map, which act on the power sets as well, are the subject of *Continuous Maps as Operators*, and the adjunction the interior and the closure form when the power set is read as a Boolean algebra is the subject of *Operators on a Boolean Algebra*; the present article is the operator layer that those two presuppose. Nothing analytic and nothing geometric is used: the real line serves only as a carrier of a topology, and no length, order, derivative or integral is invoked.

## The Closure Operator

### The Kuratowski Axioms

Throughout, $X$ is a set, $\mathcal{P}(X)$ its power set, and $C : \mathcal{P}(X) \to \mathcal{P}(X)$ a map. The complement of $A$ is written $A^{c}$, and a **monoid** is a set with an associative operation and an identity.

**Definition.** The map $C$ is a **closure operator** on $X$, and satisfies the **Kuratowski closure axioms**, when for all $A, B \subseteq X$:

**(K1)** $C(\emptyset) = \emptyset$;

**(K2)** $A \subseteq C(A)$;

**(K3)** $C(C(A)) = C(A)$;

**(K4)** $C(A \cup B) = C(A) \cup C(B)$.

A subset $A$ is **closed** for $C$ when $C(A) = A$.

Axiom (K2) is **extensivity**, (K3) is **idempotence**, and (K4) is **additivity**. From the axioms the further properties follow: $C$ is **monotone**, since $A \subseteq B$ gives $B = A \cup B$ and $C(B) = C(A) \cup C(B)$, so $C(A) \subseteq C(B)$; and $C$ commutes with every finite union, since the empty case is (K1) and the binary case is (K4).

**Proposition.** The closed sets are exactly the fixed points of $C$, and $C(A)$ is the smallest closed set containing $A$.

**Proof.** If $C(A) = A$ then $A$ is closed; if $A$ is closed then $A \subseteq C(A)$ by (K2) and $C(A) = C(C(A)) = A$ by (K3), so $C(A) = A$. For the second, $C(A)$ is closed by (K3) and contains $A$ by (K2); if $F$ is closed and $A \subseteq F$ then $C(A) \subseteq C(F) = F$ by monotonicity.

### Topologies from Closure Operators

**Theorem.** Let $C$ be a closure operator on $X$ and let $\mathcal{F} = \{A : C(A) = A\}$ be the family of its fixed points. Then $\mathcal{F}$ is the family of closed sets of exactly one topology on $X$, and for that topology $C(A) = \overline{A}$, the closure of $A$.

**Proof.** The family $\mathcal{F}$ contains $X$ because $X \subseteq C(X) \subseteq X$ and contains $\emptyset$ by (K1). It is closed under finite unions because $C(A \cup B) = C(A) \cup C(B) = A \cup B$ when $A$ and $B$ are fixed, and under arbitrary intersections because if $A_i$ is fixed for all $i$ and $A = \bigcap_i A_i$, then $C(A) \subseteq C(A_i) = A_i$ for every $i$ by monotonicity, so $C(A) \subseteq A$, and $A \subseteq C(A)$ by (K2). Hence $\mathcal{F}$ is the closed-set family of a topology, and the closure in that topology is the smallest closed set containing $A$, which is $C(A)$ by the proposition. Uniqueness is that a topology is determined by its closed sets.

Conversely, the closure operator of a topology satisfies the four axioms, by the standard theorems of *Topological Spaces*: the empty set is closed, $A \subseteq \overline{A}$, $\overline{\overline{A}} = \overline{A}$, and $\overline{A \cup B} = \overline{A} \cup \overline{B}$. The two constructions are inverse, so there is a **bijection** between the topologies on $X$ and the closure operators on $X$.

**Theorem.** The closure operator determines the topology and the topology determines the closure operator; a map $f : X \to Y$ is continuous if and only if $f(\overline{A}) \subseteq \overline{f(A)}$ for every $A \subseteq X$, where the two closures are those of the two spaces.

**Proof.** The first statement is the pair of constructions above. The second is the closure criterion of *Topological Spaces*, restated as the commutation of the direct image operator $f_{*}$ of *Continuous Maps as Operators* with the two closure operators.

## The Interior Operator

### The Dual Axioms

**Definition.** A map $I : \mathcal{P}(X) \to \mathcal{P}(X)$ is an **interior operator** on $X$ when for all $A, B \subseteq X$:

**(I1)** $I(X) = X$;

**(I2)** $I(A) \subseteq A$;

**(I3)** $I(I(A)) = I(A)$;

**(I4)** $I(A \cap B) = I(A) \cap I(B)$.

A subset is **open** for $I$ when $I(A) = A$.

The axioms are the order-duals of the closure axioms: extensivity is replaced by intensivity, additivity by multiplicativity. An interior operator is monotone in the same way, and it commutes with every finite intersection by (I1) and (I4).

### Interior and Closure

**Theorem (the duality).** Let $C$ be a closure operator and define

$$
I(A) = C(A^{c})^{c} .
$$

Then $I$ is an interior operator, and $C$ is recovered from $I$ by the same formula, $C(A) = I(A^{c})^{c}$. Under this correspondence the closed sets of $C$ are the complements of the open sets of $I$, and the interior operator of a topology is obtained from its closure operator.

**Proof.** The two operations are mutually inverse because complementation is an involution of the power set. The axioms (I1)–(I4) are the translations of (K1)–(K4): $I(X) = C(\emptyset)^{c} = X$; $I(A) = C(A^{c})^{c} \subseteq A$ is (K2) applied to $A^{c}$; $I(I(A)) = C(C(A^{c})^{c})^{c} = C(C(A^{c}))^{c} = C(A^{c})^{c} = I(A)$ by (K3); and $I(A \cap B) = C(A^{c} \cup B^{c})^{c} = (C(A^{c}) \cup C(B^{c}))^{c} = I(A) \cap I(B)$ by (K4). The identification of the closed sets with the complements of the open sets is the standard duality of *Topological Spaces*.

The complement is therefore an **anti-isomorphism** of the Boolean algebra that conjugates the two operators, and this is the precise sense in which the closure and the interior are the same operator read on complementary sides.

**Corollary.** The closure is the smallest closed set containing $A$ and the interior is the largest open set contained in $A$; consequently each of the two operators determines the other.

**Proof.** The first clause is the proposition of the previous section and its dual, the dual being that $I(A)$ is open by (I3) and is contained in $A$ by (I2), and any open $U \subseteq A$ satisfies $U = I(U) \subseteq I(A)$ by monotonicity. The last statement is the theorem.

## The Boundary

**Definition.** The **boundary** of $A$ is

$$
\partial A = C(A) \cap C(A^{c}) .
$$

**Proposition.** The boundary satisfies $\partial A = \partial (A^{c})$; it is closed; it contains exactly the points all of whose neighbourhoods meet both $A$ and $A^{c}$; and

$$
C(A) = A \cup \partial A, \qquad I(A) = A \setminus \partial A, \qquad \partial A = C(A) \setminus I(A) .
$$

**Proof.** The symmetry is the commutativity of the intersection. The boundary is the intersection of two closed sets, hence closed. For the third clause, $x \in \partial A$ iff $x \in C(A)$ and $x \in C(A^{c})$, which is the neighbourhood criterion of *Topological Spaces*. For the display, $A \cup \partial A = A \cup (C(A) \cap C(A^{c})) = (A \cup C(A)) \cap (A \cup C(A^{c})) = C(A) \cap X = C(A)$, since $A \cup C(A^{c}) \supseteq A \cup A^{c} = X$; and $A \setminus \partial A = A \cap (C(A)^{c} \cup C(A^{c})^{c}) = (A \cap C(A)^{c}) \cup (A \cap C(A^{c})^{c}) = \emptyset \cup (A \cap I(A)) = I(A)$, using $C(A^{c})^{c} = I(A)$ and $C(A) \supseteq A$. The last identity is the complement of the first two.

**Remark.** A set is closed and open at once exactly when its boundary is empty, since $\partial A = \emptyset$ says $C(A) \subseteq I(A) \subseteq A \subseteq C(A)$, so $A$ is both closed and open. A set is closed exactly when it contains its boundary and open exactly when it misses its boundary, by the identities of the proposition.

## The Monoid Generated by Closure and Complement

### Composition of Operators

The operators on $\mathcal{P}(X)$ form a monoid under composition, with identity the identity map, and the closure, the interior and the complement are three of its elements. Two submonoids are of classical interest: the monoid $M^{\complement}$ generated by $C$ and the complement operator $K(A) = A^{c}$, and the monoid $M^{\mathrm{io}}$ generated by $C$ and $I$. Both are finite for every space, with bounds independent of $X$ and of its topology, and both are the subject of a sharp finiteness theorem.

### The Kuratowski Fourteen-Set Theorem

**Theorem (Kuratowski).** Let $X$ be a topological space and $A \subseteq X$. Then the set of subsets obtainable from $A$ by any finite sequence of closures and complements has at most **fourteen** elements. Equivalently, the monoid generated by the closure operator and the complement operator has at most fourteen elements.

**Proof sketch.** Since $C^{2} = C$ and $K^{2} = 1$, every word in the two operators is alternating, and it suffices to bound the alternating words. Two absorption identities hold in every space,

$$
CKCKCKC = CKC, \qquad KCKCKCKC = KCKC ,
$$

and their companion $CKCKCKCK = CKCK$, which shorten every alternating word of length at least eight: delete the first four letters of such a word and read the identity from the left, which is possible because each of the four length-eight alternating words reduces to a word of length at most four. What remains is an alternating word of length at most seven. There are fifteen of these, namely the identity and two words at each length from one to seven, and a direct enumeration using the three identities leaves exactly fourteen distinct operators, recorded in the table below. The identities themselves are the standard ones of the theory, proved from $I \subseteq 1 \subseteq C$ and the monotonicity of both operators; see the reference of Kuratowski and of Gardner and Jackson.

**Theorem (sharpness).** The bound fourteen is attained. In the real line with its usual topology, for

$$
A = (0,1) \cup (1,2) \cup \{3\} \cup \bigl((4,5) \cap \mathbb{Q}\bigr),
$$

the fourteen words of the table below give fourteen distinct subsets of $\mathbb{R}$.

**Proof.** The claim is a finite verification. The topological features of $A$ that matter are: the two open intervals $(0,1)$ and $(1,2)$ with the point $1$ between them and lying in neither; the isolated point $3$; and the pair $(4,5) \cap \mathbb{Q}$ and $(4,5) \setminus \mathbb{Q}$, whose closures are both $[4,5]$ and whose interiors are both empty. The fourteen iterates were computed on the finite Boolean algebra generated by these features, with the closure evaluated atomwise: the atoms are the six special points $0,1,2,3,4,5$, the six open intervals between and outside them, and the rational and irrational parts of $(4,5)$, fourteen atoms in all, and the closure of a union of atoms is the union of their closures. The fourteen sets are distinct, so the bound is attained and the monoid has exactly fourteen elements.

**Remark.** The number is a property of the topology and not of the set. In a discrete space the closure is the identity, so the monoid is generated by the complement alone and has order two. In the cofinite topology on an infinite set the closure of a finite set is itself and the closure of an infinite set is the whole space, and the monoid has order at most fourteen, with the bound generally not attained. The theorem is that fourteen is the universal bound, and the witness above is a space in which it is attained.

### The Operator Table

The fourteen words are listed, each rewritten through the interior operator $I = KCK$; the rewriting is by the identities $CK = KI$ and $KC = IK$, read as composition from the right.

| Word | Expression through $I$ |
|---|---|
| $1$ | $1$ |
| $C$ | $C$ |
| $K$ | $K$ |
| $CK$ | $KI$ |
| $KC$ | $IK$ |
| $CKC$ | $CIK$ |
| $KCK$ | $I$ |
| $CKCK$ | $CI$ |
| $KCKC$ | $IC$ |
| $CKCKC$ | $CIC$ |
| $KCKCK$ | $ICK$ |
| $CKCKCK$ | $CICK$ |
| $KCKCKC$ | $ICKC$ |
| $KCKCKCK$ | $ICI$ |

**Remark.** The table and the sharpness theorem together determine the multiplication of the monoid: the product of two words is their concatenation reduced by the three identities of the proof. The multiplication is not commutative, since $CK$ and $KC$ are distinct operators on the witness. The reader should note that $CI$ and $IC$ are different operators, the closure of the interior and the interior of the closure, and neither is the identity.

## The Monoid Generated by Closure and Interior

**Theorem.** Let $X$ be a topological space and $A \subseteq X$. The set of subsets obtainable from $A$ by any finite sequence of closures and interiors has at most **seven** elements. Equivalently, the monoid generated by $C$ and $I$ has at most seven elements, namely

$$
1,\ C,\ I,\ CI,\ IC,\ CIC,\ ICI,
$$

where juxtaposition is composition read from the right.

**Proof.** The relations $C^{2} = C$ and $I^{2} = I$ remove repeated letters, so a word is alternating. From $I \subseteq 1 \subseteq C$ and the monotonicity of both operators one has

$$
ICIC = IC, \qquad CICI = CI ,
$$

which are the two absorption identities of the monoid. An alternating word has one of the forms $1$, $C$, $I$, $(CI)^{m}$, $(IC)^{m}$, $(CI)^{m}C$ or $(IC)^{m}I$; the identities reduce every such word with $m \geq 2$ to one with $m = 1$, leaving exactly the seven words listed. The list is closed under composition with $C$ and with $I$ on the left, so it is the whole monoid.

**Theorem (sharpness).** The bound seven is attained, on the same witness $A$ of the preceding section, by the seven words $1, C, I, CI, IC, CIC, ICI$.

**Proof.** The same finite computation as before: the seven operators give seven distinct subsets of the real line for $A = (0,1)\cup(1,2)\cup\{3\}\cup((4,5)\cap\mathbb{Q})$, and the longer words coincide with shorter ones by the two absorption identities.

**Corollary.** The complement is not an element of the monoid generated by $C$ and $I$: that monoid has seven elements, and adjoining the complement gives the fourteen-element monoid of the Kuratowski theorem.

**Proof.** The complement is not obtained from $C$ and $I$ alone, since $C$ and $I$ are monotone and the complement is order-reversing; adjoining it produces the larger monoid of the previous section.

## Summary

A **closure operator** on the power set of a set $X$ is a map $C$ that fixes the empty set, is extensive, is idempotent and distributes over finite unions; its fixed points are the closed sets of exactly one topology, and the assignment $C \mapsto \{A : C(A) = A\}$ is a bijection between the closure operators and the topologies on $X$. The **interior operator** $I$ is the dual, $I(A) = C(A^{c})^{c}$, and it satisfies the dual axioms; the complement is an anti-isomorphism that conjugates the two operators. The **boundary** is $\partial A = C(A)\cap C(A^{c})$, closed and symmetric in $A$ and $A^{c}$, and it satisfies $C(A) = A \cup \partial A$ and $I(A) = A \setminus \partial A$. The operators on the power set form a monoid under composition. The submonoid generated by the closure and the complement has at most **fourteen** elements, the **Kuratowski fourteen-set theorem**, and the bound is attained on the real line by $A = (0,1)\cup(1,2)\cup\{3\}\cup((4,5)\cap\mathbb{Q})$; the submonoid generated by the closure and the interior has at most **seven** elements, namely $1, C, I, CI, IC, CIC, ICI$, with the absorption identities $ICIC = IC$ and $CICI = CI$, and this bound is attained on the same witness. Both finiteness theorems are computations of the operator layer of a single topological space, and both are sharp.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $X$ | A fixed set; $\mathcal{P}(X)$ its power set |
| $A, B, F$ | Subsets; $A^{c}$ the complement; $F$ usually closed |
| $C$ | Closure operator, with $C(A) = \overline{A}$ in the induced topology |
| $I$ | Interior operator, $I(A) = C(A^{c})^{c}$ |
| (K1)–(K4) | The Kuratowski closure axioms |
| (I1)–(I4) | The dual interior axioms |
| $K$ | The complement operator, $K(A) = A^{c}$ |
| $\partial A$ | Boundary, $C(A) \cap C(A^{c})$ |
| $M^{\complement}$ | Monoid generated by $C$ and $K$; exactly $14$ elements |
| $M^{\mathrm{io}}$ | Monoid generated by $C$ and $I$; exactly $7$ elements |
| $1, C, I, CI, IC, CIC, ICI$ | The seven elements of $M^{\mathrm{io}}$ |
| fourteen words | $1, C, K, CK, KC, CKC, KCK, CKCK, KCKC, CKCKC, KCKCK, CKCKCK, KCKCKC, KCKCKCK$ |
| witness | $A = (0,1)\cup(1,2)\cup\{3\}\cup((4,5)\cap\mathbb{Q})$, on which both bounds are attained |

## Further Reading

- Casimir Kuratowski, "Sur l'opération $\bar{A}$ de l'analyse générale", *Fundamenta Mathematicae* 3 (1922), 182–199, for the four closure axioms and the operator calculus.
- Casimir Kuratowski, "Sur l'opération $\bar{A}$", *Fundamenta Mathematicae* 6 (1924), 124–125, for the fourteen-set theorem.
- Kazimierz Kuratowski and Andrzej Mostowski, *Set Theory* (North-Holland, 1976), for the closure operator, the closed-set construction and the duality with the interior operator.
- John L. Kelley, *General Topology* (Van Nostrand, 1955; reprinted Springer, 1975), for the closure axioms as a definition of a topology.
- James R. Munkres, *Topology* (Prentice Hall, 2nd ed. 2000), for the interior, closure and boundary of a set and their standard identities.
- B. J. Gardner and Marcel Jackson, "The Kuratowski closure-complement theorem", *New Zealand Journal of Mathematics* 38 (2008), 9–44, for the monoid of the closure and complement operators and the fourteen-element classification.
