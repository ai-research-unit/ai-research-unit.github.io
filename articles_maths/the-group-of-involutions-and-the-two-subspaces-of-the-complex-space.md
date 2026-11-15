# __The Group of Involutions and the Two Subspaces of the Complex Space__

## Introduction

The complex algebra carries one distinguished map beside its product: the conjugation. Read as an operation of the algebra, that map is an involution, and the family of all such involutions is a group. This article computes the group, gives the sign table of its members, lists the four fixed and anti-fixed spaces, names the one decomposition of the space that carries content, counts the intersections, and shows that every count is forced by the field property.

The answer is short. The group is $V_2$, the two-element group, which is here the Galois group of $\mathbb{C}/\mathbb{R}$. The four spaces are the whole space and the origin for the identity, the real line and the imaginary line for the conjugation. One decomposition carries content, and one intersection is non-zero. Every count is forced by one fact: $\mathbb{C}$ is commutative, so an anti-automorphism is an automorphism, and there is no room for a second proper involution.

The multiplication of the field is *Complex Algebra*; the class catalogue that records the fixed field is *The Classes of Element of the Complex Algebra*; the field property that forces the count is *The Specificities of the Complex Algebra*; the Galois reading of the same two-element group is *Galois Theory of ℂ/ℝ*. The two products the space carries are *The Two Products of the Complex Space*, and the two forms are *The Two Forms and the Two Algebraic Norms of the Complex Space*.

**Interpretation.** The element is $Q=q+iq'$ with the real coordinates $q$ and $q'$, and a second element is $Q_2=q_2+iq'_2$. The base involution is the bar, $\bar Q=q-iq'$, and the Hermitian conjugation is the same map, ${}^{*}=\bar{\cdot}$. The intrinsic conjugation ${}^{\natural}$ of the general theory is the identity map on $\mathbb{C}$, because it acts on a vector part and this algebra has none.

## The Group of Involutions

**Definition.** An **involution of the algebra** is a real-linear map $\mathrm{J}$ of $\mathbb{C}$ into itself with $\mathrm{J}^{2}=\mathrm{id}$ that is either an automorphism or an anti-automorphism of the ring, that is, $\mathrm{J}(Q_1Q_2)=\mathrm{J}(Q_1)\mathrm{J}(Q_2)$ or $\mathrm{J}(Q_1Q_2)=\mathrm{J}(Q_2)\mathrm{J}(Q_1)$ for all $Q_1,Q_2$.

**Theorem.** The involutions of $\mathbb{C}$ are exactly the identity and the conjugation, and they form the group $V_2$.

*Proof.* A real-linear $\mathrm{J}$ is determined by the two values $\mathrm{J}(1)$ and $\mathrm{J}(i)$, and the ring property forces $\mathrm{J}(1)=1$. The relation $i^{2}=-1$ is preserved or reversed, and in either case it gives $\mathrm{J}(i)^{2}=-1$, so $\mathrm{J}(i)$ is one of the two roots of $-1$, namely $i$ or $-i$. Both choices occur: $\mathrm{J}(i)=i$ gives the identity and $\mathrm{J}(i)=-i$ gives the conjugation, which is additive, real-linear, of order two, and multiplicative. Hence there are exactly two involutions, and a group of two elements is $V_2$.

**Remark (why the anti-automorphisms add nothing).** In a commutative ring an anti-automorphism is an automorphism, since the two product rules coincide. The definition above therefore names one class twice, and the count of two is a count of maps, not of kinds.

**Remark (the two surviving settings).** The general theory carries four settings of the involution, $\{\mathrm{id},{}^{\natural},{}^{*},{}^{\natural*}\}$. Here ${}^{\natural}$ is the identity and ${}^{*}$ is the bar, so the four settings collapse two-and-two and give the two maps of the theorem. The collapse is not an accident of notation: ${}^{\natural}$ negates the vector part of an element, and a complex element has no vector part.

## The Sign Table of the Two Involutions

Both involutions fix the unit and act on the imaginary unit by a sign. The table is the whole content of the section.

| involution | $1$ | $i$ | fixed space | anti-fixed space | sign on $\mathbb{R}$ | sign on $i\mathbb{R}$ |
|---|---|---|---|---|---|---|
| $\mathrm{id}$ | $1$ | $i$ | $\mathbb{C}$ | $\{0\}$ | $+$ | $+$ |
| $\bar{\cdot}$ | $1$ | $-i$ | $\mathbb{R}$ | $i\mathbb{R}$ | $+$ | $-$ |

The two rows differ in one entry, the sign on the imaginary line. Every statement of the article is read from that entry: the fixed space of the conjugation is the real line because the sign is $+$ there, and its anti-fixed space is the imaginary line because the sign is $-$ there.

## The Four Spaces

**Definition.** For an involution $\mathrm{J}$ the **fixed space** is $F_{\mathrm{J}}=\{Q:\mathrm{J}(Q)=Q\}$ and the **anti-fixed space** is $A_{\mathrm{J}}=\{Q:\mathrm{J}(Q)=-Q\}$. Both are real subspaces.

### The Two Trivial Spaces of the Identity

The identity fixes every element and anti-fixes none: $F_{\mathrm{id}}=\mathbb{C}$ and $A_{\mathrm{id}}=\{0\}$. The two spaces are the whole and the origin, and neither carries information. A decomposition built on them is the trivial one, $\mathbb{C}=\mathbb{C}\oplus\{0\}$.

### The Real Line

**Proposition.** $F_{\bar{\cdot}}=\mathbb{R}$.

*Proof.* Write $Q=q+iq'$. The condition $\bar Q=Q$ reads $q-iq'=q+iq'$, hence $q'=0$, hence $Q\in\mathbb{R}$; and every real $q$ satisfies it.

The real line is a subfield, of real dimension one. It is the fixed field of the group $V_2$ in the sense of Galois theory, which is the content of *Galois Theory of ℂ/ℝ*.

### The Imaginary Line

**Proposition.** $A_{\bar{\cdot}}=i\mathbb{R}$.

*Proof.* The condition $\bar Q=-Q$ reads $q-iq'=-q-iq'$, hence $q=0$, hence $Q=iq'$ with $q'$ real; and every such element satisfies it.

The imaginary line is a real subspace of dimension one, and it is not a subalgebra: the product of $i$ with $i$ is $-1$, which is real. It is exactly the set on which the conjugation is the negative of the identity.

**Theorem.** $\mathbb{C}=F_{\bar{\cdot}}\oplus A_{\bar{\cdot}}=\mathbb{R}\oplus i\mathbb{R}$ as real vector spaces, and the decomposition is direct.

*Proof.* Every $Q=q+iq'$ is the sum of $q$ in the real line and $iq'$ in the imaginary line, and the two lines meet only at the origin.

## The One Content-Bearing Decomposition

**Definition.** The decomposition attached to $\mathrm{J}$ is **content-bearing** when both summands are non-zero.

**Theorem.** Exactly one of the two decompositions is content-bearing, namely $\mathbb{C}=\mathbb{R}\oplus i\mathbb{R}$.

*Proof.* The decomposition of the identity is $\mathbb{C}\oplus\{0\}$, and its second summand is zero, so it carries no content. The decomposition of the conjugation has the two lines of dimension one, so both summands are non-zero.

**Remark (the count of decompositions).** The count of decompositions equals the count of non-identity elements of the group. Here there is one, because there is one proper involution; a larger involution group would give one decomposition per proper involution, and the count would rise with it.

## The One Non-Zero Intersection

The four spaces are $\mathbb{C}$, $\mathbb{R}$, $\{0\}$ and $i\mathbb{R}$. The table gives the six pairwise intersections with their real dimensions.

| the pair | the intersection | real dimension |
|---|---|---|
| $F_{\mathrm{id}}\cap F_{\bar{\cdot}}$ | $\mathbb{R}$ | $1$ |
| $F_{\mathrm{id}}\cap A_{\bar{\cdot}}$ | $i\mathbb{R}$ | $1$ |
| $F_{\mathrm{id}}\cap A_{\mathrm{id}}$ | $\{0\}$ | $0$ |
| $F_{\bar{\cdot}}\cap A_{\mathrm{id}}$ | $\{0\}$ | $0$ |
| $F_{\bar{\cdot}}\cap A_{\bar{\cdot}}$ | $\{0\}$ | $0$ |
| $A_{\bar{\cdot}}\cap A_{\mathrm{id}}$ | $\{0\}$ | $0$ |

### The Two Non-Zero Entries

**Proposition.** Of the six pairs, two meet non-trivially, and both have the whole algebra as a member: $\mathbb{C}\cap\mathbb{R}=\mathbb{R}$ and $\mathbb{C}\cap i\mathbb{R}=i\mathbb{R}$.

*Proof.* The table gives the six intersections, and the only non-zero entries are the first two.

**Proposition.** The real line and the imaginary line meet only at the origin.

*Proof.* An element of both is $q=iq'$ with $q$ and $q'$ real, hence $q=q'=0$.

**Theorem.** Among the spaces of one kind, exactly one pair meets non-trivially, and the intersection is the real line: the two fixed spaces meet in $\mathbb{R}$, while the two anti-fixed spaces meet in $\{0\}$.

*Proof.* The fixed spaces are $\mathbb{C}$ and $\mathbb{R}$, whose intersection is $\mathbb{R}$; the anti-fixed spaces are $\{0\}$ and $i\mathbb{R}$, whose intersection is $\{0\}$.

**Remark (why the count is one and not two).** Read over all six pairs the number of non-zero intersections is two, and the second one adds nothing: $\mathbb{C}\cap i\mathbb{R}$ is the anti-fixed space read once more, not a new space. The count that carries information is the count of the same-kind comparisons, and that count is one. The real line is therefore the one non-zero intersection: it is at once the fixed space of the conjugation, the fixed field of the group, and the meet of the whole algebra with the proper fixed space.

**Remark (the count of pairs).** Here four spaces give six pairs, and one same-kind pair meets non-trivially. The number of pairs rises with the number of spaces, and the number of spaces rises with the number of involutions; the group has two elements, so it produces four spaces.

## Why the Count Is Forced

Four statements were proved and each reduces to a count of elements of $V_2$. Two involutions give one proper involution, hence one content-bearing decomposition and one proper fixed space; the proper fixed space can meet the whole algebra in one non-trivial way, and it meets the anti-fixed space trivially.

The strongest objection is that the classification of the real-linear involutions of the plane is larger than the classification of the algebra involutions. There are, for instance, the reflections, and any real-linear map with square one and eigenvalues $+1$ and $-1$ is an involution of the space. The answer is that those maps are not involutions of the algebra: the definition requires the product to be preserved or reversed, and a reflection does not preserve it. If the wider class were admitted, the group would be infinite, the fixed spaces would be arbitrary lines, and no count would be forced at all. The algebra structure is what makes the count finite and what makes it two.

The second objection is that a larger group might be expected. The answer is again the field property: a second proper involution would have to send $i$ to a root of $-1$ different from $\pm i$, and there is none. A larger group needs a larger algebra, with a vector part to negate; the complex algebra is one-dimensional and carries none.

## Summary

The involutions of the complex algebra are the identity and the conjugation, and they form $V_2$: the intrinsic conjugation is the identity here, and in a commutative ring an anti-automorphism is an automorphism. The sign table has one non-trivial entry, the sign on the imaginary line. The four spaces are $\mathbb{C}$ and $\{0\}$ for the identity, $\mathbb{R}$ and $i\mathbb{R}$ for the conjugation; the real line is a subfield and the imaginary line is a subspace that is not a subalgebra. One decomposition, $\mathbb{C}=\mathbb{R}\oplus i\mathbb{R}$, carries content, and one intersection of two spaces of one kind, the real line, is non-zero. Every count follows from the field property: one proper involution, one proper fixed space, and no second root of $-1$ to build a second one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $Q=q+iq'$ | a complex element, with the real coordinates $q$ and $q'$ |
| $\bar Q=q-iq'$ | the conjugation; ${}^{*}=\bar{\cdot}$; ${}^{\natural}=\mathrm{id}$ |
| $\mathrm{J}$ | an involution of the algebra, real-linear, of order two |
| $F_{\mathrm{J}}$, $A_{\mathrm{J}}$ | the fixed space and the anti-fixed space of $\mathrm{J}$ |
| $V_2$ | the two-element group of the involutions, here the Galois group of $\mathbb{C}/\mathbb{R}$ |

## Further Reading

- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for algebras with involution, the group they generate and the decomposition attached to each.
- Serge Lang, *Algebra*, Graduate Texts in Mathematics 211 (Springer, third edition, 2002), for automorphisms of a field extension, the Galois group of a quadratic extension and its fixed field.
- Emil Artin, *Galois Theory*, Notre Dame Mathematical Lectures 2 (Dover, 1998), for the correspondence between the subgroups of the Galois group and the intermediate fields in the quadratic case.
- Nathan Jacobson, *Basic Algebra I* (Dover, second edition, 2009), for the field axioms and the two roots of $-1$ in the complex field.
