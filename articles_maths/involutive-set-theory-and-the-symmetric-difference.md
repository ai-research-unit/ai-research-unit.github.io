
# __Involutive Set Theory and the Symmetric Difference__

## Introduction

On the subsets of a set $X$ two structures meet: the **symmetric difference** $A \triangle B =
(A \setminus B) \cup (B \setminus A)$, which makes $\mathcal{P}(X)$ an abelian group of exponent two,
and the **complement** $A \mapsto X \setminus A$, an order-reversing involution that is a translation of
that group. With the
intersection as a second, multiplicative operation the three together make $\mathcal{P}(X)$ a
**Boolean ring**, and the dictionary between this ring and the Boolean algebra of *Boolean Algebras and
Lattices* is the content of the **identification** of the two presentations. The complement is a
translation in the group, $A \mapsto X \triangle A$; it is an involution, and it is anti-multiplicative,
so its fixed part is trivial, and it must not be confused with the order-preserving involution of a
Boolean algebra treated in *Boolean Algebras with an Involution*. This article develops these three
structures and their interaction.

The article presupposes *Sets, Functions and Relations* — sets, the Boolean operations on the power
set, the complement — *Boolean Algebras and Lattices*, earlier in this Part, for the Boolean algebra,
and *Boolean Algebras with an Involution* and *Orthocomplemented Lattices and the Involution*, earlier
in this group, for the two kinds of involution. It is the set-theoretic base of the `- * Theory` group.

Three boundaries are observed. No **measure** is used; the counting of a finite set is used, a
distribution on the power set is not. No **category theory** and no **topology** is used; the Boolean
algebras of this category are reached through the Boolean-ring dictionary, and the Stone space is a
forward reference to Part V. The **ring with an involution** in the sense of an algebra with a star is
*Involutive Algebras* and the `- Algebras` group, and is named only; here the involution is the
complement on the power set.

## The Symmetric Difference

### Definition and the Group Structure

**Definition.** For subsets $A, B$ of a set $X$ the **symmetric difference** is

$$
A \triangle B = (A \setminus B) \cup (B \setminus A) = (A \cup B) \setminus (A \cap B) .
$$

**Theorem.** The symmetric difference is associative and commutative, has the empty set as identity, and
every element is its own inverse: $A \triangle A = \emptyset$. Hence $(\mathcal{P}(X), \triangle)$ is an
abelian group of exponent two, in which the third sum of a pair rewrites as

$$
A \triangle B = (A \cap \neg B) \cup (\neg A \cap B), \qquad A \triangle B = (A \cup B) \triangle
(A \cap B) .
$$

**Proof.** An element $x$ lies in the left side of the first expression exactly when it lies in one of
$A, B$ and not in both, which is a symmetric condition in the three sets for the associativity; the
empty set contributes nothing, and $A \triangle A = \emptyset$ because no $x$ can lie in exactly one of
the two copies of $A$. The rewritings are the same condition written with the complement and with the
union and intersection.

### The Boolean Ring

**Theorem.** The intersection distributes over the symmetric difference on both sides:

$$
A \cap (B \triangle C) = (A \cap B) \triangle (A \cap C), \qquad
(A \triangle B) \cap C = (A \cap C) \triangle (B \cap C),
$$

and it is associative and commutative; so $(\mathcal{P}(X), \triangle, \cap)$ is a commutative ring. The
ring is **Boolean**: every element is idempotent, $A \cap A = A$; its zero is $\emptyset$, and its
multiplicative identity is $X$, because $A \cap X = A$.

**Proof.** For the distributivity, $x$ lies in $A \cap (B \triangle C)$ exactly when $x \in A$ and $x$
lies in exactly one of $B, C$, which is the same as lying in exactly one of $A \cap B$, $A \cap C$; the
other side is the same. The idempotence and the identity element are immediate.

**Theorem (the dictionary).** The following relations hold and translate between the ring and the
Boolean algebra on the same power set:

$$
A \cup B = A \triangle B \triangle (A \cap B), \qquad A \setminus B = A \triangle (A \cap B),
\qquad X \triangle A = \neg A .
$$

**Proof.** The first identity is the complement of the second rewriting of the symmetric difference
above; the second holds because $A \triangle (A \cap B) = A \setminus B$; the third is $X \triangle A =
X \setminus A$, since $A \subseteq X$.

## The Complement as the Involution

**Theorem.** The complement $\neg A = X \setminus A$ is the translation by $X$ in the group
$(\mathcal{P}(X), \triangle)$, that is, $\neg A = X \triangle A$; it is an involution, $\neg\neg A = A$.
It is **not** a homomorphism of the group: translating twice by $X$ gives

$$
\neg(A \triangle B) = X \triangle A \triangle B = \neg A \triangle B,
\qquad \neg A \triangle \neg B = A \triangle B,
$$

so the two agree only when $X = \emptyset$. The complement is an affine involution of the group, that
is, the composite of the group automorphism $A \mapsto -A$, which is the identity, with the translation
by $X$.

**Proof.** $X \triangle A = X \setminus A$ because $A \subseteq X$, which is the definition of the
complement; translating twice by the same element of a group of exponent two is the identity; and the
computation of the group law is $X \triangle A \triangle B = \neg A \triangle B$ on one side and $(A
\triangle X) \triangle (B \triangle X) = A \triangle B$ on the other, using $X \triangle X =
\emptyset$. An affine map of an abelian group is a translation composed with a homomorphism, and here
the homomorphism is the identity because $-A = A$.

The complement is therefore the **involution** of the order, an order-reversing map of order two, and
it is a translation of the group, not an automorphism of it; its fixed part is trivial as soon as $X$
is nonempty.

**Theorem.** The complement has no fixed point in a nonempty $X$, and in the group
$(\mathcal{P}(X), \triangle)$ the **additive** involution is the identity, since every element is its
own inverse. The complement is not an involution of the multiplicative structure: it satisfies
$\neg(A \cap B) = \neg A \cup \neg B$, which differs from $\neg A \cap \neg B = \neg(A \cup B)$ whenever
$A \cup B \neq X$.

**Proof.** $A = \neg A$ would give $A = X \setminus A$, hence $A \subseteq X \setminus A$ and $A \cap A
= \emptyset$, so $A = \emptyset$ and then $X = \emptyset$. The additive involution is the identity
because $A \triangle A = \emptyset$ means $-A = A$. For the last statement, if $A \cup B \neq X$ pick $x
\notin A \cup B$; then $x \in \neg A \cap \neg B = \neg(A \cup B)$ but $x \notin \neg A \cup \neg B =
\neg(A \cap B)$.

**Corollary.** The complement is an anti-automorphism of the intersection and the union, and it is a
translation, not an automorphism, of the symmetric difference; it converts the ring multiplication
$A \cap B$ into the "dual" multiplication $A \star B = \neg(\neg A \cap \neg B) = A \cup B$.

**Proof.** The De Morgan laws are the first statement, and they say that the map $A \mapsto \neg A$
exchanges $\cap$ and $\star$; the second statement is the computation of the theorem, where the
translation by $X$ fails to be a homomorphism.

## The Identification with the Boolean Algebras of this Category

**Theorem.** Under the dictionary, a Boolean algebra and a Boolean ring on the same underlying set are
the same structure: setting $A \wedge B = A \cap B$, $A \vee B = A \triangle B \triangle (A \cap B)$
and $\neg A = X \triangle A$ recovers the Boolean operations from $\triangle$ and $\cap$, and conversely
$A \triangle B = (A \wedge \neg B) \vee (\neg A \wedge B)$ and $A \cap B = A \wedge B$ recover the ring
from the Boolean algebra.

**Proof.** The two translations are mutually inverse because the identities of the dictionary are
involutive, and each set of axioms is satisfied by the other: a complemented distributive lattice is a
Boolean ring with $x + y = (x \wedge \neg y) \vee (\neg x \wedge y)$ and $xy = x \wedge y$, and a
Boolean ring is a Boolean algebra with the meet $xy$ and the join $x + y + xy$, as *Boolean Algebras and
Lattices* records.

So the **symmetric difference is the product** (the group law, the addition of the ring) and the
**complement is the involution**; the intersection is the multiplication, and the power-set structure
with its two involutions — the additive one, which is the identity, and the complement, which is the
translation by $X$ — is the set-theoretic model of the structures treated in *Boolean Algebras with an
Involution*. There the involution is an order-preserving automorphism of order two, and the complement
is the order-reversing involution; here the complement appears in both roles at once, as the translation
of a group of exponent two and as the anti-automorphism of the intersection, which is why its fixed
part is trivial.

## Summary

The symmetric difference makes the power set an abelian group of exponent two, and with the intersection
it makes a Boolean ring whose zero is $\emptyset$ and whose identity is $X$; the dictionary
$A \cup B = A \triangle B \triangle (A \cap B)$, $A \setminus B = A \triangle (A \cap B)$ and $\neg A =
X \triangle A$ identifies the ring with the Boolean algebra on the same power set.

The complement is the involution of the order, the translation by $X$ in the group of exponent two; it
is an anti-automorphism of the intersection and the union and a translation, not an automorphism, of
the symmetric difference, and its fixed part is trivial for a nonempty $X$. Every element is its own
additive inverse, so the additive involution is the identity and
the only involution of the structure that carries information is the complement, which pairs $A$ with
$\neg A$. This is the set-theoretic model that leads to the involutive Boolean algebras of *Boolean
Algebras with an Involution*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A \triangle B$ | Symmetric difference; the additive group law |
| $A \cap B$ | Intersection; the multiplication of the Boolean ring |
| $\neg A = X \triangle A$ | Complement; the involution, the translation by $X$ |
| $x + x = 0$ | Exponent two: every element is its own additive inverse |
| identity of $\cap$ | The whole set $X$ |
| $\star$ | The dual multiplication $A \star B = A \cup B$ |

## Further Reading

- Garrett Birkhoff, *Lattice Theory*, 3rd ed. (American Mathematical Society, 1967), for Boolean algebras, Boolean rings and the dictionary between them.
- Paul R. Halmos, *Lectures on Boolean Algebras* (Van Nostrand, 1963), for the Boolean ring, the symmetric difference and the complement.
- Roman Sikorski, *Boolean Algebras*, 3rd ed. (Springer, 1969), for the arithmetic of Boolean rings and the representation of a Boolean algebra by a field of sets.
- Steven Givant and Paul Halmos, *Introduction to Boolean Algebras* (Springer, 2009), for the power-set model and the identification of the ring and the lattice presentation.
- Sabine Koppelberg, *Handbook of Boolean Algebras*, Vol. 1 (North-Holland, 1989), for the algebraic identities of Boolean rings and the complement as a translation.
