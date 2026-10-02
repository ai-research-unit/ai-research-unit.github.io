
# __The Involution on the Closure Operators__

## Introduction

A closure operator on a poset is a monotone, extensive, idempotent map; an interior operator is
monotone, deflative and idempotent, and the two are dual to each other in the order. When the poset
carries an order-reversing involution ${}^{\perp}$, the operator-layer involution of *Involutions of the
Operator Layer* sends a closure operator to the map $c^{\perp} = {}^{\perp} \circ c \circ {}^{\perp}$,
and this article shows that $c^{\perp}$ is an **interior operator**, that the assignment exchanges the
two kinds of operator, and that it is the involution that reverses the Galois connection from which the
closure operator comes: if $c = g \circ f$ for a Galois connection $f \dashv g$, then $c^{\perp}$ is the
interior operator of the **reversed** connection $g^{\perp} \dashv f^{\perp}$. The fixed closure
operators are those commuting with the involution, and on a nondegenerate lattice the only fixed closure
operator is the identity. This closes the `- * Operator Theory` group and returns, with the involution
acting on the operators, to the closure operators of *Closure Operators and the Consequence Operator*.

The article presupposes *Closure Operators and the Consequence Operator*, for the closure and the
Galois connection, *Operators on a Poset*, for the residuation, *Orthocomplemented Lattices and the
Involution*, for the order-reversing involution, and *Involutions of the Operator Layer*, for the
conjugation. The topological closure and the interior of a topological space are Part II and are named
only; nothing topological is used.

## The Conjugate of a Closure Operator

**Definition.** Let $L$ be a poset with an order-reversing involution ${}^{\perp}$. For a closure
operator $c$ on $L$, its **conjugate** is $c^{\perp} = {}^{\perp} \circ c \circ {}^{\perp}$.

**Theorem.** If $c$ is a closure operator, then $c^{\perp}$ is an interior operator; if $i$ is an
interior operator, then $i^{\perp}$ is a closure operator. The assignment $c \mapsto c^{\perp}$ is an
involution that exchanges the closure operators and the interior operators of $L$.

**Proof.** Let $c$ be monotone, extensive ($c(x) \geq x$) and idempotent. The map $c^{\perp}$ is
monotone by *Involutions of the Operator Layer* (a conjugation by an order-reversing involution
preserves monotonicity). It is idempotent, $(c^{\perp})^2 = {}^{\perp} c^2 {}^{\perp} = {}^{\perp} c
{}^{\perp} = c^{\perp}$. For the deflation, $c(x^{\perp}) \geq x^{\perp}$, and applying the
order-reversing ${}^{\perp}$ gives $c^{\perp}(x) = (c(x^{\perp}))^{\perp} \leq (x^{\perp})^{\perp} =
x$. By duality, if $c$ is a closure operator with $c \geq \mathrm{id}$ and $c^2 = c$, then $c^{\perp}$
is monotone, idempotent and $\leq \mathrm{id}$, hence an interior operator. The same computation with
$c$ replaced by an interior operator $i$ shows that $i^{\perp}$ is a closure operator; and the
assignment is an involution because ${}^{\perp}$ is.

**Corollary (the open and closed sets).** The open sets of $c^{\perp}$, the fixed points of the interior
operator, are exactly the complements of the closed sets of $c$: $c^{\perp}(y) = y$ if and only if $y =
x^{\perp}$ for a fixed point $x$ of $c$. The fixed points of $c$ and of $c^{\perp}$ correspond under
${}^{\perp}$.

**Proof.** $c^{\perp}(y) = y$ means $(c(y^{\perp}))^{\perp} = y$, that is, $c(y^{\perp}) = y^{\perp}$;
writing $x = y^{\perp}$, the fixed points $y$ of $c^{\perp}$ are exactly the $x^{\perp}$ with $x$ fixed
by $c$.

## The Reversed Galois Connection

**Theorem.** Let $f \dashv g$ be a Galois connection between posets with order-reversing involutions,
and let $c = g \circ f$ be its closure operator. Then the conjugate $c^{\perp}$ is the interior operator
of the reversed connection $g^{\perp} \dashv f^{\perp}$:

$$
c^{\perp} = f^{\perp} \circ g^{\perp}, \qquad (g \circ f)^{\perp} = f^{\perp} \circ g^{\perp} .
$$

**Proof.** The conjugation is an anti-automorphism of composition, $(g \circ f)^{\perp} = f^{\perp}
\circ g^{\perp}$, and by *Involutions of the Operator Layer* the conjugation reverses the adjunction,
sending $f \dashv g$ to $g^{\perp} \dashv f^{\perp}$. So $c^{\perp} = f^{\perp} \circ g^{\perp}$ is the
composite of a left adjoint followed by a right adjoint — the right adjoint of the reversed connection
after its left adjoint — which is the interior operator $f^{\perp} \circ g^{\perp}$ of the reversed
connection.

**Corollary.** The involution reverses the Galois connection of $c$: the left adjoint of the reversed
connection is $g^{\perp}$, the conjugate of the right adjoint of the original, and the right adjoint of
the reversed connection is $f^{\perp}$, the conjugate of the original left adjoint. Hence the involution
on the closure operators is induced by the involution on the Galois connections, and the passage from
the closure to the interior is the passage from a connection to the reversed connection.

**Proof.** The theorem gives the adjunction $g^{\perp} \dashv f^{\perp}$; reading its two members
identifies the left and right adjoints as displayed.

## The Fixed Closure Operators

**Theorem.** A closure operator $c$ is fixed by the involution, $c^{\perp} = c$, if and only if $c$
commutes with ${}^{\perp}$. On a nondegenerate lattice with an orthocomplement the only fixed closure
operator is the identity, and the only fixed interior operator is the identity.

**Proof.** $c^{\perp} = {}^{\perp} c {}^{\perp} = c$ is exactly $c \circ {}^{\perp} = {}^{\perp} \circ
c$, by composing with ${}^{\perp}$ and using that it is an involution. If $c = c^{\perp}$, then $c$ is
at the same time extensive (as a closure operator) and deflative (as its own conjugate, an interior
operator), so $c = \mathrm{id}$; the same argument applies to an interior operator.

**Corollary.** The involution of the closure operators has a trivial fixed part on a nondegenerate
lattice, and its orbits are the pairs $\{c, c^{\perp}\}$ of a closure operator and the dual interior
operator, together with the identity, which is fixed.

**Proof.** The fixed part is the identity by the theorem; every other orbit is the pair of an operator
and its conjugate, which are distinct because a map that is both extensive and deflative is the
identity.

**Example (a poset).** Let $L$ be the power set of a poset $P$ ordered by inclusion, with the complement
of *Involutive Set Theory and the Symmetric Difference*, and let $c$ be the **down-closure**, assigning
to $A$ the set of elements below a member of $A$. Then $c$ is a closure operator and $c^{\perp}$ is the
map assigning to $A$ the complement of the down-closure of the complement, which is the **up-closure**,
an interior operator; the closed sets of $c$ are the down-sets and the open sets of $c^{\perp}$ are the
up-sets. The two families correspond under the complement.

## Summary

On a poset with an order-reversing involution the conjugation $c \mapsto c^{\perp} = {}^{\perp} \circ c
\circ {}^{\perp}$ sends a closure operator to an interior operator and back, and it is an involution
exchanging the two families. The open sets of $c^{\perp}$ are the complements of the closed sets of $c$,
and if $c = g \circ f$ comes from a Galois connection $f \dashv g$, then $c^{\perp} = f^{\perp} \circ
g^{\perp}$ is the interior operator of the **reversed** connection $g^{\perp} \dashv f^{\perp}$; so the
involution reverses the Galois connection and exchanges the left and right adjoints. A closure operator
is fixed exactly when it commutes with the involution, and on a nondegenerate lattice the only fixed
closure operator is the identity, so the involution pairs each closure operator with its dual interior
operator.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $c$ | A closure operator: monotone, extensive, idempotent |
| $i$ | An interior operator: monotone, deflative, idempotent |
| $c^{\perp} = {}^{\perp} \circ c \circ {}^{\perp}$ | The conjugate of $c$, an interior operator |
| $f \dashv g$ | A Galois connection with closure operator $c = g \circ f$ |
| $g^{\perp} \dashv f^{\perp}$ | The reversed connection, with interior operator $c^{\perp}$ |
| fixed part of the involution | Closure operators commuting with ${}^{\perp}$; only the identity |

## Further Reading

- Garrett Birkhoff, *Lattice Theory*, 3rd ed. (American Mathematical Society, 1967), for closure operators, interior operators and Galois connections.
- Marcel Erné, "Adjunctions and Galois connections: origins, history and development", in *Galois Connections and Applications* (Kluwer, 2004), for the duality of closures and interiors.
- Brian A. Davey and Hilary A. Priestley, *Introduction to Lattices and Order*, 2nd ed. (Cambridge University Press, 2002), for closure operators, their fixed points and the Galois connection of a closure.
- Chris Brink, Wolfram Kahl and Gunther Schmidt, *Relational Methods in Computer Science* (Springer, 1997), for the conjugation of closure operators by an involution.
- Rudolf Wille, "Restructuring lattice theory: an approach based on hierarchies of concepts", in *Ordered Sets* (Reidel, 1982), 445–470, for closure operators and their duals.
