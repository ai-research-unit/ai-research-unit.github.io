# __Zero Divisors of the General Plain Sesqualgebra__

## Introduction

The general plain sesqualgebra is the operation $\tilde Q_1\star\tilde Q_2=\tilde Q_1\tilde Q_2^{*}$ on the
biquaternion space (*Introduction to the General Plain Sesqualgebra*). This
article studies its **zero divisors**: the nonzero elements that annihilate a nonzero element.

A zero divisor names a product, and the definition is relative; it is stated once for a general
product in *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* and is read here on the
block. The criterion of the block is **one element**: because the involution ${}^{*}$ is a
bijection of $\mathbb{B}$, the vanishing of $\tilde Q_1\star\tilde Q_2=\tilde Q_1\tilde Q_2^{*}$ is the
vanishing of the plain product $\tilde Q_1\tilde Q_2^{*}$, and $\tilde Q_2^{*}$ ranges over all of
$\mathbb{B}$ as $\tilde Q_2$ does, so the block's zero-divisor set is exactly the plain one, the
nonzero elements of the zero-divisor cone $\{C(\tilde Q)=\sum_\mu Q_\mu^{2}=0\}$, which is also the
common set of the four general products (*Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*). The **set** is
therefore inherited unchanged; what is not inherited is the **internal structure** the parent reads
on it. The parent reads a square, and its pure family is the nonzero nilpotents of index two; the
block reads its own square, the Hermitian element $\tilde Q\star\tilde Q=\tilde Q\tilde Q^{*}$, on
which the pure family is **not** square-zero, and it is the pure family that is the block's
nilpotent family, with the index three instead of two (*Nilpotents of the General Plain
Sesqualgebra*). The article states the coincidence, computes the annihilators, and separates the
part of the classification that survives from the part that does not.

**The results.** A nonzero biquaternion is a zero divisor of the block $\tilde Q_1\star\tilde Q_2=\tilde Q_1\tilde Q_2^{*}$ exactly when its central square vanishes, $C(\tilde Q_1)=Q_{1t}^{2}+(\vec Q_1,\vec Q_1)=0$; the block's zero-divisor set is therefore the parent's, the nonzero complex cone of complex dimension three, and it is the common set of the four general products. Every zero divisor of the block is two-sided, and the two annihilators coincide, each a complex plane of complex dimension two on the cone and $\{0\}$ off it. The parent's partition by the scalar coordinate survives: the pure family ($Q_{1t}=0$, isotropic) is the block's nilpotent family, of index three, and the non-pure family ($Q_{1t}\neq0$) consists of the complex multiples of the nontrivial idempotents, among which exactly the Hermitian idempotents $\tfrac12(e_t+\tilde\Xi)$ are idempotents of the block.

## The Criterion

**Theorem (the criterion of the block).** For nonzero $\tilde Q_1$, the following are equivalent:

1. $\tilde Q_1$ is a left zero divisor of $\star$: there is a nonzero $\tilde Q_2$ with
$\tilde Q_1\star\tilde Q_2=0$; 2. $\tilde Q_1$ is a right zero divisor of $\star$: there is a nonzero
$\tilde Q_2$ with $\tilde Q_2\star\tilde Q_1=0$; 3. $\tilde Q_1$ is a zero divisor of the plain product:
there is a nonzero $\tilde Q_2$ with $\tilde Q_1\tilde Q_2=0$; 4. $C(\tilde Q_1)=0$.

*Proof.* The equation $\tilde Q_1\star\tilde Q_2=\tilde Q_1\tilde Q_2^{*}=0$ is, because ${}^{*}$ is a
bijection, the existence of a nonzero $\tilde Q_2^{*}$ with $\tilde Q_1\tilde Q_2^{*}=0$, which is
(3). The right equation is the same: $\tilde Q_2\star\tilde Q_1=\tilde Q_2\tilde Q_1^{*}=0$, and applying
${}^{*}$ gives $\tilde Q_1\tilde Q_2^{*}=0$ again, which is (1). The equivalence of (3) and (4) is the
invertibility criterion of the parent algebra, reproduced in *Zero Divisors of the General Plain
Algebra*: $\tilde Q$ is a zero divisor of the plain product exactly when $C(\tilde Q)=0$.

**Corollary (the set).** The zero-divisor set of the block is

$$
\boxed{\;\mathcal{Z}_\star=\{\tilde Q\neq0: C(\tilde Q)=0\}=\{\tilde Q\neq0: Q_t^{2}+(\vec Q,\vec Q)=0\}\;},
$$

the nonzero elements of the complex cone $\mathcal{N}$, of complex dimension three; every zero
divisor of the block is **two-sided**, and the set is the common zero-divisor set of the four
general products.

*Proof.* The criterion gives the set, and the equivalence of the one-sided statements makes every
member two-sided. The cone is the zero set of a non-degenerate quadratic form on $\mathbb{C}^{4}$,
hence of complex dimension three, and it is the common set by *Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*,
§*The Four General Products Coincide*.

**Remark (the criterion of the block is one element, like the parent's).** Unlike the symmetric
plain sesqualgebra, whose criterion is a bilinear equation in the element and its partner, the
block's criterion is a single quadratic equation $C(\tilde Q_1)=0$ in the element alone, and the
reason is that its annihilation equation $\tilde Q_1\tilde Q_2^{*}=0$ still has the element alone on
the left. The block changes the square and not the shape of the criterion, and its zero divisors
are a cone.

## The Two Annihilators

The annihilator of an element is the kernel of the left or the right multiplication, the two
coinciding because the star is an anti-automorphism of order two, with the common annihilator the
conjugate of the plain annihilator. The annihilators, the plain reading, the rank table and the
reading on the remarkable subspaces are the companion article *Annihilators of the General Plain
Sesqualgebra*, below this article in this category.

## The Two Families, and What the Block Does to Them

**The parent's partition by the scalar coordinate survives: the pure family ($Q_t=0$, isotropic) is the block's nilpotent family, of index three rather than two, and the non-pure family ($Q_t\neq0$) is the nonzero complex multiples of the nontrivial idempotents, among which exactly the Hermitian idempotents $\tfrac12(e_t+\tilde\Xi)$ are idempotents of the block.**

The plain product partitions its zero divisors by the scalar coordinate (*Zero Divisors of the
General Plain Algebra*): the **pure family** has $Q_t=0$ and $(\vec Q,\vec Q)=0$, and its
nonzero members are the nilpotents, $\tilde Q^{2}=0$; the **non-pure family** has $Q_t\neq0$, and
its members are the nonzero complex multiples of the nontrivial idempotents
$\tfrac12(e_t+\tilde\Xi i)$ over the roots $\tilde\Xi$ of $-1$. The partition is by the scalar
coordinate, which is a datum of the element and not of the product, so it survives verbatim for the
block; what does not survive is the **reading of the two families through the square**.

**Proposition (the pure family is not square-zero for the block).** Let $\tilde Q$ be a nonzero
pure zero divisor, $\tilde Q=\vec Q$ with $(\vec Q,\vec Q)=0$. Then its plain square
vanishes, but its block-square does not:

$$
\boxed{\;\tilde Q^{2}=0,\qquad \tilde Q\star\tilde Q=\tilde Q\tilde Q^{*}=\mathrm{Sc}\bigl(\tilde Q\tilde Q^{*}\bigr)e_t+\mathrm{Vect}\bigl(\tilde Q\tilde Q^{*}\bigr)\neq0\;}.
$$

*Proof.* The plain square vanishes because $\tilde Q^{2}=(\vec Q,\vec Q)e_t$ by the product
rule and $(\vec Q,\vec Q)=0$. For the block-square,
$\mathrm{Sc}(\tilde Q\tilde Q^{*})=\sum_\mu\lvert Q_\mu\rvert^{2}=\langle\tilde Q\rangle_{*}$, the algebraic norm
of the block, which is positive for $\tilde Q\neq0$ by the definiteness of *Norm and Invertibility
in the General Plain Sesqualgebra*; so the block-square is nonzero. The witness $\tilde Q=\vec e_x+i\vec e_y$
has $\tilde Q\star\tilde Q=2e_t+2i\vec e_z$.

**Remark (the index of the pure family is raised).** The parent calls the pure family the nonzero
**nilpotents** of index two; the block calls the same family its nonzero **nilpotents** of index
three, because the block-square of a pure zero divisor does not vanish and the third power does
(*Square Roots of Zero and the Nilpotents of the General Plain Sesqualgebra*). The pure zero divisors are therefore a family of
zero divisors that **are** nilpotents of the block, with the index raised from two to three, and
the non-pure zero divisors are the family that is **not** nilpotent. The partition of the parent is
kept, and the index attached to each family is read from the square of the product in force.

**Proposition (the non-pure family and the idempotents of the block).** The non-pure zero divisors
are the nonzero complex multiples of the nontrivial idempotents of the plain product, and among
them exactly the **Hermitian idempotents** $\tfrac12(e_t+\tilde\Xi)$ over the real unit vectors
$\vec u$ are idempotents of the block; the others are zero divisors of the block and not
idempotents of it.

*Proof.* The plain description is *N-Regularity and Degeneracy in the Biquaternion Algebra*, §*The Zero Divisors*. An idempotent of
the block is a Hermitian idempotent of the plain product (*Idempotents of the General Plain
Sesqualgebra*), and a Hermitian idempotent $\tilde\Pi$ has
$\tilde\Pi\star\tilde\Pi=\tilde\Pi\tilde\Pi^{*}=\tilde\Pi^{2}=\tilde\Pi$; the Hermitian ones are
those with a real root $\tilde\Xi=\pm\vec u$, that is the family $\tfrac12(e_t+\tilde\Xi)$. A
multiple $\lambda\tilde\Pi$ with $\lambda\neq1$ is a zero divisor but is idempotent for neither
product unless $\lambda=1$.

**Remark (the scalar part of a block idempotent is fixed).** The block idempotents
$\tfrac12(e_t+\tilde\Xi)$ have scalar part $\tfrac12$, which is the positive value the algebraic
norm $\langle\tilde\Pi\rangle_{*}=\mathrm{Sc}(\tilde\Pi\star\tilde\Pi)=\sum_\mu\lvert\Pi_\mu\rvert^{2}$ forces on
any idempotent of the block; in particular
$C\bigl(\tfrac12(e_t+\tilde\Xi)\bigr)=\tfrac14(1-(\vec u,\vec u))=0$, so every block idempotent is
a zero divisor, of the non-pure family. The unit $e_t$ is not a zero divisor, $c(e_t)=1$.

## The Comparison with the Parent and with the Four General Products

**The block shares the criterion $C(\tilde Q)=0$, the nonzero cone, the two-sidedness and the pure family with the parent and with the four general products, and it changes only the square-theoretic index of the pure family, from two to three.**

| clause | general plain algebra | general plain sesqualgebra |
|---|---|---|
| criterion | $C(\tilde Q)=Q_t^{2}+(\vec Q,\vec Q)=0$ | $C(\tilde Q)=0$, the same |
| the set | the cone $\mathcal{N}$ without the origin | the same cone without the origin |
| sides | left and right, generally distinct sets of partners | left and right, with the same annihilator |
| pure family | $Q_t=0$, isotropic, the nonzero nilpotents of index two | $Q_t=0$, isotropic, the nonzero nilpotents of index three |
| non-pure family | $Q_t\neq0$, multiples of idempotents, not nilpotent | the same; those that are block-idempotent are the Hermitian ones |
| annihilator of a zero divisor | the plain annihilator $\langle\tilde Q_1\rangle_{\natural*}=\{\tilde Q_2:\tilde Q_1\tilde Q_2=0\}$, of dimension two; the two sides are generally different | the same space carried through the involution, of dimension two, equal on the two sides |

The block's set is the common set of the four general products, and the coincidence is a theorem of
the space and not a property of the block (*Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*). What the block adds
is the reading of the set through its own square: the scalar-coordinate partition is inherited,
because it is a partition of the elements, and the **index** attached to the pure family is read
from the square in force, so it becomes three in place of two. The four general products share the
set, the pure family and the criterion $Q_t=0$; they do not share the square, and the index of
nilpotency is the visible consequence.

## Summary

The zero divisors of the general plain sesqualgebra are decided by one equation in the element
alone, and the equation is the parent's: because $\tilde Q_1\star\tilde Q_2=\tilde Q_1\tilde Q_2^{*}$ and
${}^{*}$ is a bijection, an element is a zero divisor of the block exactly when it is a zero
divisor of the plain product, that is exactly when its central square vanishes,
$C(\tilde Q)=Q_t^{2}+(\vec Q,\vec Q)=0$ with $\tilde Q\neq0$. The **set** is the nonzero
zero-divisor cone, of complex dimension three, which is the common set of the four general
products, and every member is **two-sided**. The **annihilators** are equal on the two sides and
are the image under the involution of the plain annihilator
$\langle\tilde Q_1\rangle_{\natural*}=\{\tilde Q_2:\tilde Q_1\tilde Q_2=0\}$, a **complex plane of dimension two** for every
nonzero zero divisor and the origin otherwise; the two-sided annihilator is $\{0\}$. The **two
families** of the parent are inherited as a partition of the elements, since the partition is read
on the scalar coordinate: the pure family has $Q_t=0$ and isotropic vector part, and the non-pure
family consists of the nonzero complex multiples of the nontrivial idempotents. What changes is the
**square-theoretic reading**: a pure zero divisor is a nilpotent of index two for the parent and a
nilpotent of **index three** for the block, its block-square being the nonzero Hermitian element
$\tilde Q\tilde Q^{*}$ with positive scalar part; the non-pure zero divisors are nilpotent for
neither; and of the non-pure multiples, exactly the Hermitian idempotents $\tfrac12(e_t+\tilde\Xi)$
are idempotents of the block. The block keeps the set, keeps the criterion, the partition and the
annihilators, and changes the index.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde Q_1\star\tilde Q_2=\tilde Q_1\tilde Q_2^{*}$ | the product of the block |
| $C(\tilde Q)=\tilde Q\tilde Q^{\natural}=Q_t^{2}+(\vec Q,\vec Q)$ | the central square |
| $\mathcal{Z}_\star=\{\tilde Q\neq0:C(\tilde Q)=0\}$ | the zero-divisor set, the nonzero cone |
| $\tilde Q_1\star\tilde Q_2=0\Leftrightarrow\tilde Q_1\tilde Q_2^{*}=0$ | the annihilation equation |
| $A_\star(\tilde Q)$, $B_\star(\tilde Q)$ | the left and the right annihilators, equal |
| $\langle\tilde Q_1\rangle_{\natural*}^{*}$, $\langle\tilde Q_1\rangle_{\natural*}=\{\tilde Q_2:\tilde Q_1\tilde Q_2=0\}$ | the common annihilator, the plain annihilator carried through the involution |
| $Q_t=0$ | the pure family, isotropic: the nilpotents of the block, index three |
| $Q_t\neq0$ | the non-pure family, multiples of the idempotents, not nilpotent |
| $\tfrac12(e_t+\tilde\Xi)$ | the Hermitian idempotents, zero divisors and block idempotents |

## Further Reading

- [Introduction to the General Plain Sesqualgebra](introduction-to-the-general-plain-sesqualgebra.html), for the product, the class and the involution in the second slot.
- [Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternion-c-space.html), for the relative definitions of the zero divisor and the annihilator.
- [Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](zero-divisors-in-the-algebraic-structures-over-the-biquaternion-c-space.html), for the theorem that the four zero-divisor sets coincide and for the one-sided inverse equations.
- [N-Regularity and Degeneracy in the Biquaternion Algebra](n-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the criterion $C(\tilde Q)=0$, the pure and the non-pure families and their geometry.
- [Norm and Invertibility in the General Plain Sesqualgebra](norm-and-invertibility-in-the-general-plain-sesqualgebra.html), for the algebraic norm, the invertibility criterion and the definiteness of the scalar form.
- [Square Roots of One and the Idempotents of the General Plain Sesqualgebra](square-roots-of-one-and-the-idempotents-of-the-general-plain-sesqualgebra.html), for the Hermitian idempotents that are the block idempotents among the non-pure zero divisors.
- [Square Roots of Zero and the Nilpotents of the General Plain Sesqualgebra](square-roots-of-zero-and-the-nilpotents-of-the-general-plain-sesqualgebra.html), for the pure family read as the nilpotent family, of index three.
- [Annihilators of the General Plain Sesqualgebra](annihilators-of-the-general-plain-sesqualgebra.html), below this article in this category, the companion article, for the coincident annihilators and the reading of the plain annihilator
