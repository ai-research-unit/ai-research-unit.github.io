
# __Boolean Algebras with an Involution__

## Introduction

Two different involutions act on the elements of a Boolean algebra. The **complement** $\neg$ is an
order-reversing involution, of order two, that exchanges the meet and the join; it is the canonical
involution of the structure, and it is an anti-automorphism, not an automorphism. An **involution** of
a Boolean algebra, in the sense of this article, is on the contrary an order-preserving map $\sigma$ of
order two that preserves the Boolean operations, that is, a Boolean automorphism with $\sigma^2 =
\mathrm{id}$. A **Boolean algebra with an involution** is a Boolean algebra $B$ together with such a
$\sigma$; its **fixed part** $B^{\sigma}$, the elements with $\sigma x = x$, is a Boolean subalgebra,
and the pair $(B, \sigma)$ has a representation by a power set with an involution induced by an
involutive permutation of the underlying set. This article separates the two involutions, treats the
morphisms of the involutive structure and the fixed part, and gives the representation.

The article presupposes *Order Theory and Lattices* — distributive, complemented and Boolean lattices
— and *Boolean Algebras and Lattices*, earlier in this Part, where the complement and the Boolean
homomorphisms are fixed; it uses *Orthocomplemented Lattices and the Involution*, earlier in this group,
for the order-reversing involution, and *Involutive Set Theory and the Symmetric Difference*, which
follows, for the power-set representation. The **Stone** representation of a general Boolean algebra is
*Stone Duality and Boolean Algebras*, in Part V, and is named only; the article proves the
representation for the finite power-set case and states the general case as a forward reference. The
complement and the involution of a Boolean **ring** are *Involutive Algebras* and the `- Algebras`
group; the star of an algebra with involution is not used here.

Three boundaries are observed. No **topology** is used; the Stone space is named and deferred to Part
V. No **form** is used, and the **measure** theory of a Boolean algebra is not touched. The reading of
the Boolean operations as connectives is *Logic and Proof*, in Part 0, and is named only.

## The Complement as an Involution

**Definition.** Let $B$ be a Boolean algebra. The **complement** is the map $\neg : B \to B$ with $x
\wedge \neg x = 0$ and $x \vee \neg x = 1$; it is the orthocomplement of *Orthocomplemented Lattices and
the Involution*, the unique complement of each element.

**Theorem.** The complement is an order-reversing involution and satisfies the De Morgan laws and the
two unit laws:

$$
\neg\neg x = x, \qquad x \leq y \Rightarrow \neg y \leq \neg x, \qquad
\neg(x \wedge y) = \neg x \vee \neg y, \qquad \neg(x \vee y) = \neg x \wedge \neg y, \qquad
\neg 0 = 1, \quad \neg 1 = 0 .
$$

It is an anti-automorphism of the Boolean algebra: it reverses the order and exchanges the two
operations, and it is not an automorphism unless the algebra is trivial.

**Proof.** The involution, the order reversal and the De Morgan laws are those of an orthocomplement in
a Boolean algebra, proved in *Orthocomplemented Lattices and the Involution*. The last assertion is the
definition of an anti-automorphism: an automorphism is order-preserving, while the complement reverses
the order, and it preserves the meet, while the complement exchanges the meet and the join.

So the complement is the order-reversing involution of the structure, and it is not an automorphism.
An **involution of a Boolean algebra** in the sense used below is a second, order-preserving map; the
two commute, since an automorphism of a Boolean algebra preserves the complement.

**Proposition.** If $B$ is a Boolean algebra with an involution $\sigma$, then $\sigma \circ \neg =
\neg \circ \sigma$, and $\sigma$ is determined by its restriction to the atoms in the finite case.

**Proof.** An automorphism of a Boolean algebra preserves the complement, which is defined by the two
Boolean identities, so $\sigma(\neg x) = \neg \sigma(x)$; for the finite case, every element is the
join of the atoms below it and an automorphism permutes the atoms.

## Involutive Boolean Algebras and their Homomorphisms

**Definition.** An **involution** of a Boolean algebra $B$ is a map $\sigma : B \to B$ with $\sigma^2 =
\mathrm{id}$, $\sigma(x \wedge y) = \sigma x \wedge \sigma y$, $\sigma(x \vee y) = \sigma x \vee \sigma
y$, $\sigma 0 = 0$ and $\sigma 1 = 1$. A **Boolean algebra with an involution** is a pair $(B, \sigma)$
with $\sigma$ an involution.

**Proposition.** An involution of a Boolean algebra is a Boolean automorphism of order two; conversely
every Boolean automorphism of order two is an involution. It preserves the complement, the order, and
every Boolean expression in the elements.

**Proof.** The preservation of the meet and the join together with $\sigma 0 = 0$ and $\sigma 1 = 1$
makes $\sigma$ a Boolean homomorphism; the involution makes it bijective with inverse itself, hence an
automorphism of order two. The preservation of the complement follows from the identities and the
uniqueness of the complement.

**Definition.** A **morphism of involutive Boolean algebras** $(B, \sigma) \to (B', \sigma')$ is a
Boolean homomorphism $h : B \to B'$ with $h \circ \sigma = \sigma' \circ h$. The involutive Boolean
algebras and their morphisms form a category, and the forgetful functor to Boolean algebras is faithful
but not full.

**Proof.** The composition of two such homomorphisms commutes with the involutions, so the class is a
category; the forgetful functor is injective on hom-sets but its image omits the homomorphisms that do
not commute with the involutions, so it is not full.

**Example (the power set).** Let $X$ be a set and let $s : X \to X$ be an **involution of the set**,
$s^2 = \mathrm{id}_X$. The map $\sigma_s$ on the power set $\mathcal{P}(X)$ defined by $\sigma_s(A) =
s(A)$ is an involution of the Boolean algebra $\mathcal{P}(X)$; it is the involution induced by $s$.
Every involution of a finite power set is of this form, with $s$ the restriction of $\sigma$ to the
atoms, that is, the singletons.

## The Fixed Part

**Definition.** The **fixed part** of an involutive Boolean algebra $(B, \sigma)$ is $B^{\sigma} = \{x
\in B : \sigma x = x\}$.

**Theorem.** The fixed part is a Boolean subalgebra of $B$ containing $0$ and $1$. Its atoms, when
$B$ is finite, are the **orbits** of $\sigma$ on the atoms of $B$; in particular every orbit of atoms a
singleton $\{a\}$ with $\sigma a = a$ contributes one atom, and every two-element orbit $\{a, \sigma
a\}$ contributes the element $a \vee \sigma a$, which is fixed and is an atom of the fixed part.

**Proof.** Fixed elements are closed under the Boolean operations because $\sigma$ preserves them, and
$0, 1$ are fixed. An element of $B$ is the join of the atoms below it, and it is fixed if and only if
the set of atoms below it is stable under $\sigma$; so the fixed elements are exactly the unions of
orbits, and the minimal such unions are the orbits, which are therefore the atoms of the fixed part.

**Corollary.** For a finite Boolean algebra with $n$ atoms, the fixed part has one atom per orbit of
$\sigma$ on the atoms, so its cardinality is $2^{f + (n - f)/2}$, where $f$ is the number of atoms
fixed by $\sigma$; in particular the number of fixed atoms and $n$ have the same parity.

**Proof.** The orbits are the $f$ fixed atoms and the $(n-f)/2$ two-element orbits; the fixed part is
the power set of its atoms by the theorem.

**Example.** On $\mathcal{P}(X)$ with the involution $s$, the fixed part is the power set of the set of
**orbits** of $s$ on $X$: a subset is fixed exactly when it is a union of orbits, so $A$ is determined
by which orbits it meets, and the fixed part is $\mathcal{P}(X/{\sim})$ with ${\sim}$ the orbit
relation. The map $A \mapsto$ its set of orbits is a Boolean isomorphism onto the power set of
$X/{\sim}$.

## Representation

**Theorem (finite representation).** Every involution $\sigma$ of a finite Boolean algebra $B$
is induced by an involution $s$ of the set of atoms of $B$, and $B \cong \mathcal{P}(\mathrm{At}(B))$
as Boolean algebras, with $\sigma$ corresponding to $\sigma_s$. Hence every finite Boolean algebra with
an involution is isomorphic to a power set with an involution, and the fixed part is the power set of
the orbits.

**Proof.** The atoms are permuted by $\sigma$ because $\sigma$ is an automorphism and the atoms are the
elements covering $0$; the restriction $s$ is an involution, and the induced map $\sigma_s$ agrees with
$\sigma$ on the atoms, hence on all joins of atoms, which is all of $B$.

**Theorem (general representation, forward reference).** Every Boolean algebra with an involution
$(B, \sigma)$ is isomorphic to the Boolean algebra of clopen subsets of a compact Hausdorff space $S$
carrying a homeomorphism $s$ with $s^2 = \mathrm{id}$, in such a way that $\sigma$ corresponds to the
map $U \mapsto s^{-1}(U)$ on clopen sets, and the fixed part $B^{\sigma}$ corresponds to the clopen
subsets fixed by that map. The space is the Stone space of $B$ and the theorem is the Stone
representation, which is *Stone Duality and Boolean Algebras*, in Part V; this article states it and
does not prove it.

The finite theorem is the case in which the space is discrete and the algebra is a power set, and it is
the case used in the examples of this article.

## Summary

A Boolean algebra carries the **complement**, an order-reversing involution that exchanges the meet and
the join and is an anti-automorphism, and it may carry an **involution** $\sigma$, an order-preserving
automorphism of order two; the two commute and are different. An involutive Boolean algebra is a pair
$(B, \sigma)$; its morphisms are the Boolean homomorphisms commuting with the involutions.

The **fixed part** $B^{\sigma}$ is a Boolean subalgebra; over a finite algebra its atoms are the orbits
of $\sigma$ on the atoms of $B$, so its cardinality is $2^{f + (n-f)/2}$ for $n$ atoms with $f$ of them
fixed. Every finite Boolean algebra with an involution is a power set with the involution induced by an
involution of the underlying set, and the general case is the Stone representation, deferred to Part V;
the fixed part is the power set of the orbits.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\neg$ | The complement, an order-reversing involution and an anti-automorphism |
| $(B, \sigma)$ | A Boolean algebra with an involution $\sigma$ |
| $B^{\sigma}$ | The fixed part, $\{x : \sigma x = x\}$ |
| $\sigma_s$ | The involution of $\mathcal{P}(X)$ induced by an involution $s$ of $X$ |
| orbit | A set $\{a, \sigma a\}$ of atoms; the atoms of the fixed part |
| $\mathrm{At}(B)$ | The set of atoms of $B$ |

## Further Reading

- Garrett Birkhoff, *Lattice Theory*, 3rd ed. (American Mathematical Society, 1967), for Boolean algebras, the complement and the anti-automorphism.
- Paul R. Halmos, *Lectures on Boolean Algebras* (Van Nostrand, 1963), for Boolean algebras, homomorphisms and involutions, and the Stone representation.
- Roman Sikorski, *Boolean Algebras*, 3rd ed. (Springer, 1969), for involutions and the structure of the fixed part.
- Steven Givant and Paul Halmos, *Introduction to Boolean Algebras* (Springer, 2009), for the power-set representation and involutions of Boolean algebras.
- Sabine Koppelberg, *Handbook of Boolean Algebras*, Vol. 1 (North-Holland, 1989), for the Stone duality and the representation of endomorphisms.
