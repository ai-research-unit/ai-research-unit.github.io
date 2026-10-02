
# __Groupoids with an Involution__

## Introduction

A **groupoid** is a category in which every morphism is invertible. The assignment of the inverse,
$f \mapsto f^{-1}$, is the **canonical involution** on the morphisms of a groupoid: it is of order two,
it fixes every identity, and it reverses the composition, $(g \circ f)^{-1} = f^{-1} \circ g^{-1}$. It
is therefore an **anti-automorphism** of the partial multiplication, and in the language of the
preceding article it makes every groupoid a dagger category with the inversion as dagger. This article
studies that involution: its orbits, which are the pairs $\{f, f^{-1}\}$ together with the self-inverse
morphisms, its fixed elements, which are the morphisms of order at most two, and the non-abelian case,
in which inversion is not a homomorphism and the fixed elements are not closed under composition.

The article presupposes *Universal Properties and Categories* — categories, functors, the opposite
category, isomorphisms — and *Involutive Categories and the Dagger Functor*, which precedes it in this
group and treats the general contravariant involution on the morphisms. The **group** is the one-object
case, developed in *Groups*, later in this Part; the article uses the symmetric group $S_3$ as a
one-object example and does not develop the general theory of groups. The relation algebra of a groupoid
and the convolution algebra are *Groupoid C\*-Algebras*, in another Part, and are named only.

Three boundaries are observed. No **measure** and no representation of a groupoid is used. No
**topology** is used; the topological and smooth groupoids belong to later Parts and are named only. No
**form** is used and no C\*-algebra is formed.

## Groupoids and Inversion

### The Groupoid

**Definition.** A **groupoid** is a category $\mathcal{G}$ in which every morphism is an isomorphism.
The objects of $\mathcal{G}$ are its **points**, the morphisms are its **arrows**, and the composition
is defined for the composable pairs; for each arrow $f : A \to B$ there is a unique arrow $f^{-1} : B
\to A$ with $f \circ f^{-1} = \mathrm{id}_B$ and $f^{-1} \circ f = \mathrm{id}_A$. A groupoid with one
object is a **group**, the arrows being its elements.

**Theorem.** In a groupoid the inversion is an involution on the arrows, fixes the identities, and
reverses the composition:

$$
(f^{-1})^{-1} = f, \qquad \mathrm{id}_A^{-1} = \mathrm{id}_A, \qquad
(g \circ f)^{-1} = f^{-1} \circ g^{-1},
$$

and it exchanges the hom-sets, carrying $\mathrm{Hom}(A,B)$ to $\mathrm{Hom}(B,A)$. Hence inversion is
an anti-automorphism of the partial multiplication, and it is the dagger of *Involutive Categories and
the Dagger Functor*; the groupoid with inversion is a dagger category in which every morphism is
unitary.

**Proof.** The inverse is unique in a category, so $(f^{-1})^{-1} = f$ because $f$ is an inverse of
$f^{-1}$; the identity is its own inverse; and $f^{-1} \circ g^{-1}$ is a two-sided inverse of $g \circ
f$ because $(g \circ f) \circ (f^{-1} \circ g^{-1}) = \mathrm{id}$ and the composite in the other order
is $\mathrm{id}$. The exchange of hom-sets is the definition of the target and source of $f^{-1}$.

**Example.** A group $G$ with one object is a groupoid, and the inversion is the group inversion, an
anti-automorphism; the abelian groups are exactly those for which it is an automorphism, as the next
section proves.

### The Involution and the Orbit Decomposition

**Theorem (orbits of inversion).** The orbits of the involution $f \mapsto f^{-1}$ on the arrows of a
groupoid are of size one or two; an orbit is a singleton exactly when $f = f^{-1}$, and then $f$ is an
endomorphism with $f \circ f = \mathrm{id}$, that is, $f$ is an **involution of its object**. The
fixed elements of the inversion are exactly the self-inverse arrows, and they include all the
identities.

**Proof.** An orbit $\{f, f^{-1}\}$ is a singleton exactly when $f = f^{-1}$; then $A = B$ because the
sources and targets must agree, and $f \circ f = f \circ f^{-1} = \mathrm{id}_A$, so $f^2 =
\mathrm{id}$. Conversely $f^2 = \mathrm{id}$ with $f$ an endomorphism gives $f = f^{-1}$ by uniqueness
of inverses.

**Corollary.** For a finite group $G$, the number of orbits of the inversion is $(|G| + \#\{g : g^2 =
e\})/2$, where the second term is the number of elements of order at most two.

**Proof.** The orbits are the fixed elements, one each, and the remaining $|G| - \#\{g : g^2 = e\}$
elements, paired.

**Example ($S_3$).** In the symmetric group $S_3$ the elements of order at most two are the identity and
the three transpositions, so the inversion has $4$ fixed points and $(6 + 4)/2 = 5$ orbits; the two
$3$-cycles form one orbit, because the inverse of a $3$-cycle is the other $3$-cycle.

## The Non-Abelian Case

**Theorem.** In a group $G$ the inversion is an automorphism if and only if $G$ is abelian; for a
non-abelian group it is an anti-automorphism that is not a homomorphism.

**Proof.** Inversion is a homomorphism exactly when $(gh)^{-1} = g^{-1}h^{-1}$ for all $g, h$; but
$(gh)^{-1} = h^{-1}g^{-1}$, so the two agree for all pairs exactly when the group is abelian. An
automorphism is a homomorphism that is bijective, and the inversion is always bijective.

**Theorem (the fixed elements are not a subgroup).** In a non-abelian group the set of fixed elements
of the inversion is not closed under multiplication, and it is not a subgroup. It contains the identity
and, when the group is finite, the elements of order two, which in a non-abelian group need not commute.

**Proof.** In $S_3$ the transpositions $(12)$ and $(13)$ are fixed by the inversion because they are of
order two, while their product $(12)(13) = (132)$ is a $3$-cycle and is not fixed; so the fixed set is
not closed under multiplication.

**Theorem (what the involution does not fix).** In a groupoid the inversion fixes exactly the
self-inverse arrows and exchanges each remaining arrow with its inverse, so it fixes no arrow of order
greater than two, and on a non-abelian group it reverses the order of every product that is not
commutative. The involution therefore carries information only about the self-inverse arrows and the
pairing of the rest.

**Proof.** The fixed elements are the self-inverse arrows by the orbit theorem, and on a non-abelian
group there are pairs $g, h$ with $gh \neq hg$, for which $(gh)^{-1} = h^{-1}g^{-1} \neq g^{-1}h^{-1}$,
so inversion does not preserve the product.

**Example (a group with a second involution).** Let $G$ be a group and let $\sigma$ be an automorphism
of $G$ with $\sigma^2 = \mathrm{id}$; then $\sigma$ is an involution of the group, the fixed subgroup is
$G^{\sigma} = \{g : \sigma g = g\}$, and the orbits of $\sigma$ on $G$ are the pairs $\{g, \sigma g\}$.
Inversion and $\sigma$ commute when $\sigma(g^{-1}) = (\sigma g)^{-1}$, which holds for every
automorphism, so the two involutions generate a group of order at most four acting on $G$; the
transformations of the form $g \mapsto (\sigma g)^{-1}$ are the **anti-involutions** of the group.

## Summary

A groupoid is a category with every morphism invertible, and its inversion is the canonical involution
on the arrows: it is of order two, fixes the identities, exchanges the hom-sets and reverses the
composition, so it is an anti-automorphism and the dagger of the groupoid. Its orbits are the pairs
$\{f, f^{-1}\}$ and the self-inverse arrows, and its fixed elements are exactly the arrows of order at
most two, which include the identities. For a finite group the number of orbits is $(|G| + \#\{g : g^2
= e\})/2$.

In the non-abelian case the inversion is not an automorphism of the group, and the fixed elements are
not closed under multiplication, as $S_3$ shows; the involution fixes the elements of order at most two
and pairs the rest, so it carries no information about the order beyond that pairing. A second
involution of the group, an automorphism of order two, commutes with the inversion and with it generates
a group of involutions on the group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{G}$ | A groupoid |
| $f^{-1}$ | The inverse of $f$; the canonical involution on the arrows |
| $\mathrm{id}_A$ | The identity at the object $A$; fixed by the inversion |
| self-inverse | $f = f^{-1}$, equivalently $f^2 = \mathrm{id}$; the fixed elements |
| orbit | $\{f, f^{-1}\}$, of size one or two |
| $G^{\sigma}$ | The fixed subgroup of an automorphism $\sigma$ of order two |

## Further Reading

- Saunders Mac Lane, *Categories for the Working Mathematician*, 2nd ed. (Springer, 1998), for groupoids, the opposite category and isomorphisms.
- Nicolás Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for groups, the inversion and anti-automorphisms.
- Ronald Brown, *Topology and Groupoids* (BookSurge, 2006), for groupoids, their morphisms and the involution of inversion.
- Philip J. Higgins, *Notes on Categories and Groupoids* (Van Nostrand Reinhold, 1971), for groupoids, subgroupoids and morphisms of groupoids.
- Jean-Pierre Serre, *Trees* (Springer, 1980), for groups acting on groupoids and the fixed subgroup of an involution.
