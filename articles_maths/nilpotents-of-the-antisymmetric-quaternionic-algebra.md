# __Nilpotents of the Antisymmetric Quaternionic Algebra__

## Introduction

The nilpotent is defined by an equation in which the product occurs, so it is a class of the
product and not of the space (*Definitions for the Study of the 12 Algebraic Structures*,
§*The Nilpotent*). The block of this article is the antisymmetric quaternionic multiplication
$$
\tilde P\diamond\tilde Q=\tfrac12\bigl(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P\bigr)
=P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q ,
$$
which is alternating and without a unit (*Introduction to the Antisymmetric Quaternionic Algebra
of Biquaternions*). The article determines its nilpotent set and its index.

The answer is total. The block is alternating, so $\tilde\Upsilon\diamond\tilde\Upsilon=0$ for
every element, and therefore **every element of $\mathbb{B}$ is a nilpotent of the block, of
index two when it is nonzero and of index one at the origin**; the square-zero set is the punctured
space, and no element has index three or more. The nilpotent set of the block is thus the whole
space, the largest set a nilpotent class can be, and it strictly contains the nilpotent cone of
the parent quaternionic product, which is the zero-divisor cone $c=0$ and a proper cone. The
square-zero set is at once the zero-divisor set of the block and the root set of $0$, and the two
companion articles are cited. The higher powers are read with the left-nested bracketing of the
definitions, since the block is not associative.

## The Notion and Its Product

**Definition (nilpotent of a product).** Let $\star$ be a product on $\mathbb{B}$. An element
$\tilde\Upsilon$ is **nilpotent of $\star$** when some power of it vanishes,
$$
\tilde\Upsilon^{\star k}=0 \quad\text{for some } k\geq1 ,
$$
the power being the left-nested reading
$\tilde\Upsilon^{\star k}=\bigl(\cdots\bigl((\tilde\Upsilon\star\tilde\Upsilon)\star\tilde\Upsilon\bigr) \cdots\star\tilde\Upsilon\bigr)$ when the product is not associative. The least such $k$ is the
**index of nilpotency**, and an element of index two, $\tilde\Upsilon\star\tilde\Upsilon=0$ with
$\tilde\Upsilon\neq0$, is a **square-zero element of $\star$**. The origin is the trivial
nilpotent.

Throughout this article the product is the **antisymmetric quaternionic multiplication**
$\diamond$, and unqualified, *nilpotent* means a nilpotent of the block. The nilpotents of the
general plain product, to which the block is compared, are *Nilpotents of the General Plain
Algebra*; the nilpotent cone of the parent quaternionic product is *The Nilpotents and the Zero
Divisors of the Quaternionic Product*.

## The Criterion

**Theorem (the criterion for the block).** Every element of $\mathbb{B}$ is a nilpotent of the
antisymmetric quaternionic multiplication. Equivalently, the nilpotent set of the block is the
whole space, and the square-zero set is the punctured space.

*Proof.* The block is alternating, $\tilde\Upsilon\diamond\tilde\Upsilon=0$ for every element
$\tilde\Upsilon$, by *Introduction to the Antisymmetric Quaternionic Algebra of
Biquaternions*; the square therefore vanishes, so the element is nilpotent of index at most two,
and it is of index exactly two when it is nonzero. The set of the elements whose square vanishes
is the whole space, and the square-zero set, which excludes the origin, is the same space without
it.

The criterion is the alternation of the product read as an element statement, and it is met by
every element, the origin included. There is no hypothesis on the element, no scalar part and no
vector part to test: the equation $\tilde\Upsilon\diamond\tilde\Upsilon=0$ is an identity of the
block and not a condition on $\tilde\Upsilon$.

## The Index

**Proposition (index two, and no higher index).** For every element $\tilde\Upsilon$ and every
$k\geq2$ the left-nested power vanishes,
$$
\tilde\Upsilon^{\diamond k}=0 \quad (k\geq2),
$$
and the index of a nonzero element is exactly two while the index of the origin is one. The
block carries no nilpotent of index three or more.

*Proof.* The left-nested square is $\tilde\Upsilon\diamond\tilde\Upsilon=0$; the third power is
$\bigl(\tilde\Upsilon\diamond\tilde\Upsilon\bigr)\diamond\tilde\Upsilon =0\diamond\tilde\Upsilon=0$, and each higher power is formed from a vanishing power and therefore
vanishes again. A nonzero element has a nonvanishing first power and a vanishing second power,
so its index is exactly two; the origin has vanishing first power, so its index is one.

The boundedness of the index is a second sense in which the block is extreme. In the general
plain algebra the index is two or nothing, and an element is a nilpotent exactly on the pure
isotropic cone; here the index is two for every nonzero element, and the membership test is
vacuous. The block has the largest nilpotent set and the smallest positive index.

## The Relation to the Zero Divisors

**Proposition (every nonzero nilpotent is a two-sided zero divisor).** Every nonzero nilpotent
$\tilde\Upsilon$ of the block satisfies $\tilde\Upsilon\diamond\tilde\Upsilon=0$ on both sides,
so it lies in its own left annihilator and in its own right annihilator, and it is a two-sided
zero divisor with itself as the annihilating partner.

*Proof.* The square is zero by the criterion, so the element is a partner of itself on the left
and on the right; the partner is nonzero because the nilpotent is, and the definition of the
zero divisor is met (*Definitions for the Study of the 12 Algebraic Structures*, §*The Zero
Divisor and the Annihilator*). The annihilators of the two sides coincide by the alternation of
the block (*Zero Divisors of the Antisymmetric Quaternionic Algebra*).

The implication *nilpotent implies zero divisor* therefore holds for the block at every nonzero
nilpotent: the nilpotent set is the whole space, the zero-divisor set is the punctured space, and
the two differ by the origin alone, which is the trivial nilpotent and is excluded from the zero
divisors by their definition. Of the four general products the implication holds for two and fails
for one, at the plain sesquilinear product whose only square-zero element is the origin
(*Definitions for the Study of the 12 Algebraic Structures*, §*The Nilpotent*); for the block it holds at every
element other than the origin, the origin being the trivial nilpotent and not a zero divisor.

## The Relation to the Idempotents

**Remark (the two classes meet at the origin).** No nonzero element of the block is both an
idempotent and a nilpotent. The idempotent set of the block is the origin alone
(*Idempotents of the Antisymmetric Quaternionic Algebra*), so an idempotent of the block is the
origin, which is the trivial nilpotent; and a nonzero nilpotent has vanishing square while a
nonzero idempotent would satisfy $\tilde\Pi\diamond\tilde\Pi=\tilde\Pi\neq0$. The two classes
therefore meet at the origin and nowhere else.

The statement is the sharp form of a general fact. In an associative unital product the
idempotents and the nilpotents are disjoint outside the origin, and in the block they are the
origin and the whole space, the two extremes that the definitions allow: the smallest idempotent
set and the largest nilpotent set.

## The Conjugations and the Matrix Model

**Proposition (the conjugations preserve the nilpotent class).** The natural conjugation
${}^{\natural}$, the complex conjugation $\overline{\cdot}$ and the star ${}^{*}$ carry the
nilpotent set of the block onto itself, the set being the whole space; and on the values of the
block the natural conjugation acts as the negative of the identity,
$$
(\tilde P\diamond\tilde Q)^{\natural}=-\tilde P\diamond\tilde Q .
$$

*Proof.* The nilpotent set is the whole space, so a bijection carries it onto itself. For the
display, the natural conjugation is an anti-automorphism of the plain product, so
$(\tilde P^{\natural}\tilde Q)^{\natural}=\tilde Q^{\natural}\tilde P$; applying it to the two
terms of the definition of the block gives
$\tfrac12(\tilde Q^{\natural}\tilde P-\tilde P^{\natural}\tilde Q)=-\tilde P\diamond\tilde Q$.

**Remark (the matrix model).** In either matrix model of the block the square of an element
vanishes, so the matrix of the square is the zero matrix and the nilpotent set is the whole
matrix space: $\mathsf{M}(\tilde P\diamond\tilde P)=\mathsf{M}(0)=0$ for every $\tilde P$, in the
$2\times2$ model and in the $4\times4$ model alike (*The Antisymmetric Quaternionic Algebra in
the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*, *The Antisymmetric Quaternionic
Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$*). The matrix models
therefore carry no nilpotent condition beyond the vanishing of the square.

## The Relation to the Parent Product

**Remark (the parent's nilpotent cone).** The parent quaternionic product
$\tilde P^{\natural}\tilde Q$ has the square $\tilde P^{\natural}\tilde P=N(\tilde P)e_0$, so
its square-zero set is the cone $N(\tilde P)=0$ of its algebraic norm, which is the zero-divisor cone, a proper
cone of the space; its nilpotents are the square-zero elements of that cone, the index being two
there by the central-square identity (*The Nilpotents and the Zero Divisors of the Quaternionic
Product*). The block is the parent with the scalar part removed, and with the scalar part removed
the square of the parent, which was a central reading of the parent's algebraic norm, becomes the zero of the block:
the parent's cone widens to the whole space, and the parent's index two is kept by every nonzero
element. The block's nilpotent set strictly contains the parent's, and the difference is the
complement of the cone, on which the parent's square is a nonzero central value and the block's
square is zero.

## Summary

For the antisymmetric quaternionic multiplication $\tilde P\diamond\tilde Q=P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q$ every element is a nilpotent: the square
$\tilde\Upsilon\diamond\tilde\Upsilon$ vanishes identically, the square-zero set is the punctured
space, the index of a nonzero element is exactly two and no element has index three or more. The
nilpotent set is therefore the whole space, and it strictly contains the nilpotent cone
$N(\tilde\Upsilon)=0$ of the parent quaternionic product, which is the zero-divisor cone. Every
nonzero nilpotent is a two-sided zero divisor with itself as the annihilating partner, and the
implication *nilpotent implies zero divisor* holds for the block at every element other than the
origin; the
nilpotents and the idempotents meet at the origin alone, the idempotent set being the origin. The
conjugations carry the class onto itself, and on the values of the block the natural conjugation
acts as the negative of the identity; in either matrix model the square is the zero matrix.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\diamond\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P)=P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q$ | the antisymmetric quaternionic multiplication, the operation $\mathrm{AQA}$ |
| $\tilde\Upsilon\diamond\tilde\Upsilon=0$ | the criterion, the vanishing square of every element |
| $\mathbb{B}$ | the nilpotent set of the block, the whole space |
| $2$ | the index of nilpotency of every nonzero element |
| $N(\tilde\Upsilon)=\sum_\mu\Upsilon_\mu^{2}$ | the algebraic norm of the parent product, whose vanishing cone is the parent's nilpotent set |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the nilpotent, the index of nilpotency, the square-zero element and the relativity of the definitions to the product
- *Introduction to the Antisymmetric Quaternionic Algebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-quaternionic-algebra-of-biquaternions.md`), for the operation, its alternation and its table
- *Zero Divisors of the Antisymmetric Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-antisymmetric-quaternionic-algebra.md`), for the coincidence of the square-zero set with the zero-divisor set and for the annihilators
- *Idempotents of the Antisymmetric Quaternionic Algebra* (`articles_maths/idempotents-of-the-antisymmetric-quaternionic-algebra.md`), for the idempotent set, the origin alone, which meets the nilpotents at the origin
- *Square Roots of Minus One, Zero and Plus One in the Antisymmetric Quaternionic Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-antisymmetric-quaternionic-algebra.md`), for the root set of $0$, which is the square-zero set
- *Nilpotents of the General Quaternionic Algebra* (`articles_maths/nilpotents-of-the-general-quaternionic-algebra.md`), for the nilpotent cone of the parent product
