
# __Involutions of the Operator Layer__

## Introduction

The two preceding articles of this Part put an involution on the **elements** of a lattice or a
relation algebra. This article puts the involution on the **operators** themselves. Given a poset $P$
with an order-reversing involution $x \mapsto x^{\perp}$, the **conjugate** of a monotone map $f : P \to
P$ is the map $f^{\perp} = {}^{\perp} \circ f \circ {}^{\perp}$, and the assignment $f \mapsto
f^{\perp}$ is an **involution of the operator layer**. It is an anti-automorphism for composition,
$(g \circ f)^{\perp} = f^{\perp} \circ g^{\perp}$, and it is order-reversing for the pointwise order; its
fixed elements are the operators commuting with the involution, and it exchanges left adjoints with
right adjoints, so it reverses every Galois connection. An order-**preserving** involution $\sigma$
gives the other case, the conjugation $f \mapsto \sigma \circ f \circ \sigma$, which is an
order-preserving automorphism of the operator monoid. This article develops both, the fixed part and
the adjoint operation.

The article presupposes *Operators on a Poset* — monotone maps, residuated maps, Galois connections,
the monoid of monotone maps — *Orthocomplemented Lattices and the Involution*, for the order-reversing
involution, and *Involutive Categories and the Dagger Functor*, for the abstract involution on
morphisms. The operator-algebraic and Hilbert-space adjoint is Part II and the `- * Operator Theory`
group, and is named only; here the operators are monotone maps of a poset and the involution acts on
them.

## Conjugation by the Involution

**Definition.** Let $P$ be a poset with an order-reversing involution ${}^{\perp}$ and let $f : P \to P$
be monotone. The **conjugate** of $f$ is

$$
f^{\perp} = {}^{\perp} \circ f \circ {}^{\perp} : P \to P, \qquad f^{\perp}(x) = (f(x^{\perp}))^{\perp}.
$$

**Theorem.** The conjugate of a monotone map is monotone, and the assignment $f \mapsto f^{\perp}$ is an
involution of the set of monotone maps. It is an anti-automorphism of the composition monoid and an
order-reversing map of the pointwise order:

$$
(f^{\perp})^{\perp} = f, \qquad (g \circ f)^{\perp} = f^{\perp} \circ g^{\perp}, \qquad
f \leq g \Rightarrow g^{\perp} \leq f^{\perp} .
$$

**Proof.** For monotonicity, if $x \leq y$ then $y^{\perp} \leq x^{\perp}$, so $f(y^{\perp}) \leq
f(x^{\perp})$ and $(f(y^{\perp}))^{\perp} \geq (f(x^{\perp}))^{\perp}$; comparing with the definition
gives $f^{\perp}(x) \leq f^{\perp}(y)$. The involution is $(f^{\perp})^{\perp} = {}^{\perp} \circ
{}^{\perp} \circ f \circ {}^{\perp} \circ {}^{\perp} = f$ because ${}^{\perp}$ has order two. For the
composition, $(g \circ f)^{\perp} = {}^{\perp} \circ g \circ f \circ {}^{\perp} = ({}^{\perp} \circ g
\circ {}^{\perp}) \circ ({}^{\perp} \circ f \circ {}^{\perp}) = g^{\perp} \circ f^{\perp}$. For the order,
$f \leq g$ pointwise gives $f(x^{\perp}) \leq g(x^{\perp})$, and applying the order-reversing
${}^{\perp}$ reverses the inequality, so $g^{\perp}(x) \leq f^{\perp}(x)$ for all $x$.

**Corollary.** The involution $f \mapsto f^{\perp}$ is an automorphism of the order-dual of the operator
monoid: it is a bijection that reverses the pointwise order and the composition. In particular it maps
the identity to the identity, the constant maps to the constant maps, and idempotents to idempotents.

**Proof.** The identity satisfies $\mathrm{id}^{\perp} = \mathrm{id}$; a constant map $c_a$ with value
$a$ satisfies $c_a^{\perp} = c_{a^{\perp}}$, so constants go to constants; and $f^2 = f$ implies
$(f^{\perp})^2 = (f^2)^{\perp} = f^{\perp}$ by the composition law.

**Definition.** The **fixed part** of the involution of the operator layer is the set of operators with
$f^{\perp} = f$.

**Theorem.** A monotone map $f$ is fixed by the conjugation exactly when it commutes with the
involution, $f \circ {}^{\perp} = {}^{\perp} \circ f$. The fixed part contains the identity and is
closed under composition; it is the centralizer of the involution in the monoid of monotone maps.

**Proof.** $f^{\perp} = {}^{\perp} \circ f \circ {}^{\perp} = f$ is exactly $f \circ {}^{\perp} =
{}^{\perp} \circ f$ after composing with ${}^{\perp}$ on one side and using that it is an involution.
The fixed elements of a monoid endomorphism are always a submonoid, which here is the centralizer of
${}^{\perp}$.

## The Adjoint Operation

**Theorem.** The conjugation reverses adjoint pairs: if $f \dashv g$ is a Galois connection between
posets with order-reversing involutions, then $g^{\perp} \dashv f^{\perp}$, that is, the left and the
right adjoints are exchanged.

**Proof.** The Galois condition is $f(x) \leq y \Leftrightarrow x \leq g(y)$. Replacing $x$ by
$x^{\perp}$ and $y$ by $y^{\perp}$ and using the involutions, $f(x^{\perp}) \leq y^{\perp} \Leftrightarrow
x^{\perp} \leq g(y^{\perp})$, which becomes $y \leq f^{\perp}(x) \Leftrightarrow g^{\perp}(y) \leq x$
after applying ${}^{\perp}$ and rewriting; this is the Galois condition $g^{\perp} \dashv f^{\perp}$.

**Corollary.** The conjugation carries the set of left adjoints bijectively onto the set of right
adjoints and exchanges the two; it is the **adjoint operation** of the scope, an order-reversing
involution between the two families of residuated maps.

**Proof.** A left adjoint $f$ has a right adjoint $g$, and the theorem gives the right adjoint
$g^{\perp}$ of $f^{\perp}$; applying the conjugation twice returns $f$ and $g$, so the map is a
bijection exchanging the two families.

**Example (relations).** Let the poset be the lattice of relations on a set with the converse as the
involution, in the sense of *The Converse as an Adjoint*: for an operator $F$ on relations put
$F^{\perp}(R) = (F(R^{-1}))^{-1}$. Then $F \mapsto F^{\perp}$ is the conjugation, the fixed operators
are those with $F(R^{-1}) = F(R)^{-1}$, that is, those commuting with the converse, and the conjugation
is an anti-automorphism of the composition of operators. The left-composition operator $L_R(S) = R;S$
of *The Converse as an Adjoint* has the conjugate $L_R^{\perp}(S) = (L_R(S^{-1}))^{-1} = (R;S^{-1})^{-1}
= S;R^{-1}$, the right-composition by the converse of $R$; this is computed again in *The Converse
Relation as an Adjoint*.

**Example (a Boolean lattice).** Let $P$ be a Boolean lattice and let ${}^{\perp}$ be the complement.
For a monotone map $f$ the conjugate is $f^{\perp}(x) = \neg f(\neg x)$, the **dual** of $f$; the fixed
maps are those commuting with the complement, and the conjugation exchanges the meet-preserving maps
with the join-preserving maps, because it reverses the composition and the order.

## The Order-Preserving Case

**Definition.** Let $P$ have an order-**preserving** involution $\sigma$. The **conjugate** of a
monotone map $f$ is $f^{\sigma} = \sigma \circ f \circ \sigma$.

**Theorem.** If $\sigma$ is an order-preserving involution, then $f \mapsto f^{\sigma}$ is an involution
of the set of monotone maps, an **automorphism** of the composition monoid, and an order-preserving map
of the pointwise order:

$$
(f^{\sigma})^{\sigma} = f, \qquad (g \circ f)^{\sigma} = g^{\sigma} \circ f^{\sigma}, \qquad
f \leq g \Rightarrow f^{\sigma} \leq g^{\sigma} .
$$

**Proof.** The same computations as before, with $\sigma$ order-preserving, so that $f \leq g$ gives
$\sigma \circ f \circ \sigma \leq \sigma \circ g \circ \sigma$.

**Corollary.** An order-preserving involution of the base gives an ordinary automorphism of the operator
monoid, and its fixed part is again the centralizer of $\sigma$. The order-reversing case is the one
relevant to an orthocomplement, and it is the case of the rest of the group.

**Proof.** The fixed equation is the same $f \circ \sigma = \sigma \circ f$; the last assertion records
that an orthocomplement is order-reversing.

## Summary

An order-reversing involution ${}^{\perp}$ of a poset acts on the operators by conjugation, $f^{\perp}
= {}^{\perp} \circ f \circ {}^{\perp}$; this is an involution of the operator layer, an
**anti-automorphism** of composition and an **order-reversing** map of the pointwise order, and its
fixed elements are the operators commuting with ${}^{\perp}$. It exchanges left and right adjoints, so
it reverses every Galois connection, and it carries left adjoints bijectively onto right adjoints. An
order-preserving involution $\sigma$ gives instead the conjugation $f \mapsto \sigma \circ f \circ
\sigma$, an order-preserving automorphism of the operator monoid with the same fixed part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $f^{\perp} = {}^{\perp} \circ f \circ {}^{\perp}$ | The conjugate of $f$ by an order-reversing involution |
| $f^{\sigma} = \sigma \circ f \circ \sigma$ | The conjugate by an order-preserving involution |
| fixed part | Operators with $f^{\perp} = f$, the centralizer of ${}^{\perp}$ |
| adjoint operation | The exchange of left and right adjoints by the conjugation |
| $L_R$, $L_R^{\perp} = R_{R^{-1}}$ | Left composition by $R$ and its conjugate, right composition by $R^{-1}$ |

## Further Reading

- Garrett Birkhoff, *Lattice Theory*, 3rd ed. (American Mathematical Society, 1967), for monotone maps, residuated maps and Galois connections and their duals.
- Marcel Erné, "Adjunctions and Galois connections: origins, history and development", in *Galois Connections and Applications* (Kluwer, 2004), for the exchange of adjoints under duality.
- Chris Brink, Wolfram Kahl and Gunther Schmidt, *Relational Methods in Computer Science* (Springer, 1997), for the conjugation of operators on relations by the converse.
- Brian A. Davey and Hilary A. Priestley, *Introduction to Lattices and Order*, 2nd ed. (Cambridge University Press, 2002), for monotone maps, adjoints and the duality of Galois connections.
- Richard Bird and Oege de Moor, *Algebra of Programming* (Prentice Hall, 1997), for the dual of a map under an involution and the algebra of operators.
