# __Operators on a Boolean Algebra__

## Introduction

A topological space carries a Boolean algebra, namely its power set with the operations of union, intersection and complement, and its topology is a pair of subfamilies of that algebra, the open sets and the closed sets. The **interior** and the **closure** are the two operators on this algebra that the topology singles out, and their relation is an adjunction: the closure is the left adjoint of the interior, and the interior is the right adjoint of the closure, once the open sets and the closed sets are read as two lattices with the complement identifying them. This article states and proves that adjunction, identifies exactly when it extends from the two sublattices to the whole Boolean algebra, and places the two operators among the Boolean homomorphisms of the algebra, where the preimage operators of continuous maps live.

The article is the structural companion of *Operators on a Fixed Set*: the closure and the interior were there read as operators on the power set, with their axioms and the monoid they generate, and they are read here as a pair of adjoint maps between the lattice of open sets and the lattice of closed sets, with the Boolean algebra in the background. The preimage operator of a continuous map, which is the other natural algebra homomorphism of the power set, was fixed in *Continuous Maps as Operators* and is used to identify which Boolean homomorphisms arise from continuous maps.

The space is that of *Topological Spaces*. The algebra of clopen sets, which is a Boolean algebra in its own right and the object of Stone duality, is named and not developed, since the corpus treats no duality theory of that kind at this point. Nothing analytic and nothing geometric is used: no distance is chosen, and no measure, integral, length or angle occurs.

## The Boolean Algebra of a Space

### The Power Set as a Boolean Algebra

**Definition.** The **Boolean algebra of a space** $X$ is its power set $\mathcal{P}(X)$ with the operations

$$
A \cup B, \qquad A \cap B, \qquad A^{c}, \qquad \emptyset, \qquad X ,
$$

the partial order of inclusion, and the derived operations $A \setminus B = A \cap B^{c}$ and the symmetric difference $A \triangle B = (A \setminus B) \cup (B \setminus A)$.

Every subset is an element of the algebra, and the operations satisfy the Boolean laws: distributivity of each of $\cup$ and $\cap$ over the other, the identities $A \cap A^{c} = \emptyset$ and $A \cup A^{c} = X$, and the De Morgan laws $(A \cap B)^{c} = A^{c} \cup B^{c}$ and $(A \cup B)^{c} = A^{c} \cap B^{c}$. The algebra is **complete**: every family of elements has a least upper bound, the union, and a greatest lower bound, the intersection.

The clopen subsets of $X$ form a subalgebra under the same operations, written $\mathcal{C}(X)$. It is the Boolean algebra that carries the topological information of a totally disconnected compact space, and it is the carrier of Stone duality; here it serves only as an example of a subalgebra.

### Lattices of Open and Closed Sets

**Definition.** The **lattice of open sets** $\mathcal{O}(X)$ is the family of open subsets with the order of inclusion; the **lattice of closed sets** $\mathcal{F}(X)$ is the family of closed subsets. Both are complete lattices: the join of a family of open sets is its union, the meet is the interior of the intersection; for closed sets the join is the closure of the union and the meet is the intersection.

The complement is a bijection and reverses the order, so it is an **anti-isomorphism** of the two lattices,

$$
\complement : \mathcal{O}(X) \longrightarrow \mathcal{F}(X), \qquad U \mapsto U^{c},
$$

and its inverse is its own composite with itself. The two lattices are the same poset read in opposite directions, and the open sets determine the closed sets and conversely.

**Definition.** The **closure operator** is the map

$$
C : \mathcal{O}(X) \longrightarrow \mathcal{F}(X), \qquad C(U) = \overline{U},
$$

sending an open set to its closure; the **interior operator** is the map

$$
I : \mathcal{F}(X) \longrightarrow \mathcal{O}(X), \qquad I(F) = \operatorname{int} F ,
$$

sending a closed set to its interior. Both are monotone, and both are order-preserving.

## The Closure and the Interior as Adjoints

### The Adjoint Pair

**Definition.** Let $P$ and $Q$ be posets and $g : P \to Q$, $h : Q \to P$ monotone maps. Then $g$ is **left adjoint** to $h$, written $g \dashv h$, when

$$
g(p) \leq q \iff p \leq h(q) \qquad (p \in P,\ q \in Q).
$$

The relation is a **Galois connection**: $g$ is the lower and $h$ the upper adjoint, and each determines the other.

**Theorem.** The closure is left adjoint to the interior between the lattice of open sets and the lattice of closed sets:

$$
C \dashv I, \qquad \overline{U} \subseteq F \iff U \subseteq \operatorname{int} F \qquad (U \in \mathcal{O}(X),\ F \in \mathcal{F}(X)).
$$

**Proof.** Suppose $\overline{U} \subseteq F$. Then $U \subseteq \overline{U} \subseteq F$, and since $U$ is open and $F$ is closed with $U \subseteq F$, the open set $U$ is contained in the largest open set inside $F$, which is $\operatorname{int} F$. Conversely suppose $U \subseteq \operatorname{int} F$. Then $\overline{U} \subseteq \overline{\operatorname{int} F}$, and since $\operatorname{int} F \subseteq F$ with $F$ closed, the closure of $\operatorname{int} F$ is contained in $F$. Hence $\overline{U} \subseteq F$.

The adjunction is the exact sense in which the interior is the best open approximation from below and the closure the best closed approximation from above: the theorem says that the closure of $U$ is the smallest closed set containing $U$ and the interior of $F$ the largest open set contained in $F$, which is the content of *Operators on a Fixed Set*, read as a Galois connection between the two lattices.

### The Two Readings of the Adjunction

**Corollary.** The adjunction has the two equivalent forms

$$
C(U) = \bigcap \{\, F \in \mathcal{F}(X) : U \subseteq I(F) \,\} \quad \text{and} \quad I(F) = \bigcup \{\, U \in \mathcal{O}(X) : C(U) \subseteq F \,\},
$$

which express each operator through the other.

**Proof.** In a Galois connection $g \dashv h$, the lower adjoint is determined by $g(p) = \bigwedge\{q : p \leq h(q)\}$ and the upper adjoint by $h(q) = \bigvee\{p : g(p) \leq q\}$; the stated formulas are these.

**Remark.** The adjunction is not symmetric: the closure is the lower adjoint and the interior the upper adjoint, and reversing the roles is not possible without replacing one of the two lattices by its opposite. Read on the opposite lattice, the interior becomes a left adjoint and the closure a right adjoint, and this is the same statement seen through the complement anti-isomorphism of the two lattices.

## When the Adjunction is Global

### The Condition

The adjunction of the theorem is stated for $U$ open and $F$ closed. The natural question is when it holds for all pairs of subsets, that is, when

$$
\overline{A} \subseteq B \iff A \subseteq \operatorname{int} B \qquad (A, B \subseteq X)
$$

for arbitrary $A$ and $B$. The answer is that this is a strong condition on the topology.

**Theorem.** The global adjunction holds for every pair of subsets of $X$ if and only if every open subset of $X$ is closed.

**Proof.** Suppose every open set is closed. Then every closed set is open as well, since the complement of a closed set is open and hence closed. If $\overline{A} \subseteq B$ then $A \subseteq \overline{A} \subseteq B$, and $\overline{A}$ is closed, hence open and contained in $B$, so $\overline{A} \subseteq \operatorname{int} B$ and $A \subseteq \operatorname{int} B$. Conversely if $A \subseteq \operatorname{int} B$ then $\overline{A} \subseteq \overline{\operatorname{int} B} = \operatorname{int} B \subseteq B$, since $\operatorname{int} B$ is open and hence closed. For the converse direction, suppose the global adjunction holds and let $U$ be open. Take $A = B = U$: the right side $U \subseteq \operatorname{int} U = U$ is true, so the left side $\overline{U} \subseteq U$ is true, whence $\overline{U} = U$ and $U$ is closed.

**Corollary.** The global adjunction holds in the discrete spaces, in the indiscrete spaces, in every disjoint union of indiscrete spaces, and more generally whenever every open set is closed; and it fails in every space in which some open set is not closed, in particular in $\mathbb{R}$ and in every Hausdorff space that is not discrete.

**Proof.** In a discrete space every set is clopen, and in an indiscrete space the only open sets are $\emptyset$ and $X$, both closed; a disjoint union of spaces with the property has the property, since its open sets are unions of open sets of the summands. In a space with an open set $U$ that is not closed the pair $A = B = U$ refutes the global adjunction by the last part of the proof. A Hausdorff space that is not discrete has a point $x$ that is not isolated; then $X \setminus \{x\}$ is open, and it is not closed, because its complement $\{x\}$ is not open.

### The Failing Example, and the Exact Boundary

**Example.** The failure is witnessed by $A = \{0\}$ and $B = [0,1]$ in $\mathbb{R}$: the closure of $A$ is $\{0\}$, which is contained in $B$, while $A$ is not contained in the interior of $B$, which is $(0,1)$. The open–closed adjunction of the theorem avoids this pair because $B = [0,1]$ is closed but $A = \{0\}$ is not open, and the theorem holds precisely for the pairs that the two lattices supply.

**Remark.** The failure of the global adjunction is the failure of the closure to preserve the joins of the whole power set. A left adjoint between complete lattices preserves all joins, and the closure preserves finite unions, which is (K4) of *Operators on a Fixed Set*, but not arbitrary ones: in $\mathbb{R}$ the union of the singletons $\{q\}$ with $q \in \mathbb{Q}$ has closure $\mathbb{R}$, while the union of their closures is $\mathbb{Q}$, and the two differ. The adjunction therefore lives on the open lattice, where the joins are unions of open sets and the closure does preserve them, since the closure of a union of open sets equals the closure of the union of their closures. Dually the interior preserves the finite intersections, which is (I4), but not arbitrary ones, and that is why the adjunction is not global either.

## Boolean Homomorphisms and the Operators of a Map

**Definition.** A map $\varphi : \mathcal{P}(Y) \to \mathcal{P}(X)$ is a **Boolean homomorphism** when it preserves the Boolean operations: $\varphi(B \cup C) = \varphi(B) \cup \varphi(C)$, $\varphi(B \cap C) = \varphi(B) \cap \varphi(C)$, $\varphi(B^{c}) = \varphi(B)^{c}$, $\varphi(\emptyset) = \emptyset$ and $\varphi(Y) = X$.

**Theorem.** A map $\varphi : \mathcal{P}(Y) \to \mathcal{P}(X)$ is a Boolean homomorphism preserving arbitrary unions if and only if it is the preimage operator $\varphi = f^{-1}$ of a unique map $f : X \to Y$.

**Proof.** The preimage operator is a Boolean homomorphism preserving arbitrary unions by *Continuous Maps as Operators*. Conversely, let $\varphi$ preserve the Boolean operations and arbitrary unions. For each $y \in Y$ put $A_{y} = \varphi(\{y\})$; the sets $A_{y}$ are disjoint and their union is $X$, because the singletons are disjoint with union $Y$ and the operations are preserved. Define $f(x) = $ the unique $y$ with $x \in A_{y}$. Then for $B \subseteq Y$, $\varphi(B) = \varphi(\bigcup_{y \in B}\{y\}) = \bigcup_{y \in B} A_{y} = f^{-1}(B)$. Uniqueness is that $f$ is recovered from the family $A_{y}$, and a map with the same preimage operator has the same fibres.

**Corollary.** The closure and the interior are not Boolean homomorphisms: the closure does not preserve complements, since $\overline{A^{c}}$ need not be $\overline{A}^{c}$, and it does not preserve meets; the interior does not preserve joins. The preimage operators of continuous maps are the Boolean homomorphisms that preserve arbitrary unions, and they are the operators of the algebra that come from geometry; the closure and the interior are operators that come from the topology itself.

**Proof.** The failure for a pair of complements is immediate in $\mathbb{R}$, where $\overline{\mathbb{Q}} = \mathbb{R}$ while $\overline{\mathbb{Q}^{c}} = \mathbb{R}$, so $\overline{\mathbb{Q}^{c}} \neq \overline{\mathbb{Q}}^{c} = \emptyset$. The meet failure is $\overline{\mathbb{Q} \cap \mathbb{Q}^{c}} = \emptyset$ while $\overline{\mathbb{Q}} \cap \overline{\mathbb{Q}^{c}} = \mathbb{R}$. The identification of the union-preserving Boolean homomorphisms with the preimage operators is the theorem.

## Summary

The power set of a space is a complete Boolean algebra, and the open sets and the closed sets are two complete lattices inside it, exchanged by the complement anti-isomorphism. The closure is a map from the open lattice to the closed lattice and the interior a map back, and they are adjoint: $\overline{U} \subseteq F$ if and only if $U \subseteq \operatorname{int} F$ for open $U$ and closed $F$, so the closure is the left adjoint of the interior. Each adjoint is recovered from the other by the Galois formulas for the smallest closed set containing $U$ and the largest open set contained in $F$. The adjunction extends to all pairs of subsets exactly when every open set is closed, a condition that holds in the discrete spaces, the indiscrete spaces and their disjoint unions, and fails in every space with an open set that is not closed, such as $\mathbb{R}$; the obstruction is that the closure preserves finite unions but not arbitrary ones, so it is a left adjoint on the open lattice and not on the whole power set. Among the operators of the algebra, the Boolean homomorphisms preserving arbitrary unions are exactly the preimage operators of maps, and they include the operators of continuous maps; the closure and the interior are not of this kind.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{P}(X)$ | The power set of $X$, a complete Boolean algebra |
| $\mathcal{O}(X)$, $\mathcal{F}(X)$ | Complete lattices of open sets and of closed sets |
| $\mathcal{C}(X)$ | The clopen subsets, a Boolean subalgebra |
| $\complement$ | Complement, an anti-isomorphism $\mathcal{O}(X) \to \mathcal{F}(X)$ |
| $C(U) = \overline{U}$ | Closure, a map $\mathcal{O}(X) \to \mathcal{F}(X)$ |
| $I(F) = \operatorname{int} F$ | Interior, a map $\mathcal{F}(X) \to \mathcal{O}(X)$ |
| $C \dashv I$, $g \dashv h$ | Adjunction (Galois connection); $g(p) \leq q \iff p \leq h(q)$ |
| global adjunction | $\overline{A} \subseteq B \iff A \subseteq \operatorname{int} B$ for all $A, B$; holds iff every open set is closed |
| $\varphi$ | A Boolean homomorphism $\mathcal{P}(Y) \to \mathcal{P}(X)$ |
| $f^{-1}$ | The preimage operator; every union-preserving Boolean homomorphism is one |

## Further Reading

- Garrett Birkhoff, *Lattice Theory* (American Mathematical Society, 3rd ed. 1967), for Galois connections, adjoint pairs and the calculus of closure and interior operators.
- Peter T. Johnstone, *Stone Spaces* (Cambridge University Press, 1982), for the lattice of open sets as a frame, the adjunction of closure and interior, and Stone duality.
- Brian A. Davey and Hilary A. Priestley, *Introduction to Lattices and Order* (Cambridge University Press, 2nd ed. 2002), for adjunctions between posets and the two equivalent forms of a Galois connection.
- Steven Vickers, *Topology via Logic* (Cambridge University Press, 1989), for the point-free reading of the algebra of open sets.
- Kazimierz Kuratowski and Andrzej Mostowski, *Set Theory* (North-Holland, 1976), for the Boolean algebra of subsets and its complete-lattice structure.
- Paul R. Halmos, *Lectures on Boolean Algebras* (Van Nostrand, 1963; reprinted Springer, 1974), for Boolean homomorphisms and the representation theory of Boolean algebras.
