# __Square Roots of Zero and the Nilpotents of the Antisymmetric Quaternionic Algebra__

## Introduction

A root of a central value and a nilpotent are each defined by an equation in which the product
occurs, so both belong to the product (*Definitions for the Study of the 12 Algebraic Structures*,
§*Powers, the Square and the Roots* and §*The Nilpotent*). The block of this article is the
antisymmetric quaternionic multiplication
$$
\tilde\Xi\diamond\tilde Q=\tfrac12\bigl(\tilde\Xi^{\natural}\tilde Q-\tilde Q^{\natural}\tilde\Xi\bigr)
=\Xi_0\vec Q-Q_0\vec\Xi-\vec\Xi\times\vec Q ,
$$
which is alternating and without a unit (*Introduction to the Antisymmetric Quaternionic Algebra of
Biquaternions*).

The article treats two subjects, and in this order. The first is the square roots of the central
value $0$, the elements $\tilde\Xi\in\mathbb{B}$ with
$$
\tilde\Xi\diamond\tilde\Xi=0 .
$$
The second is the nilpotents of the block, the elements $\tilde\Upsilon$ one of whose powers
vanishes. The two subjects are one subject, because the root of $0$ is exactly the square-zero
element, and the nonzero square-zero elements are exactly the nilpotents of index two. The block is
alternating, so its square vanishes identically, $\tilde\Xi\diamond\tilde\Xi=0$ for every element,
and every element is a nilpotent: the root equation holds at every element and the root condition
is the sole condition that the element not be the origin.

The outcome is the extreme totality, and it is the sharpest form of the absence law read the other
way. The block has **all the nonzero elements as its roots of $0$**, and **every element as a
nilpotent**, of index two away from the origin and of index one at it; no element has index three or
more. The root set of $0$ is therefore the punctured space $\mathbb{B}\setminus\{0\}$, which is at
once the square-zero set and the zero-divisor set of the block, and the nilpotent set is the whole
space $\mathbb{B}$, which strictly contains the nilpotent cone $N(\tilde P)=0$ of the parent
quaternionic product.

The article is algebraic. It does not treat the roots of $+1$ or the idempotents, which
are *Square Roots of One and the Idempotents of the Antisymmetric Quaternionic Algebra*; the square
roots of a general right side, which is *Square Roots of a General Element in the Antisymmetric
Quaternionic Algebra*; the annihilators of an element, which are *Annihilators of the
Antisymmetric Quaternionic Algebra*; or the nilpotent cone of the parent product, which is
*Square Roots of Zero and the Nilpotents of the General Quaternionic Algebra*.

**The results.** For the antisymmetric quaternionic multiplication
$\tilde P\diamond\tilde Q=P_0\vec Q-Q_0\vec P-\vec P\times\vec Q$ the square of every
element vanishes, $\tilde P\diamond\tilde P=0$, so the root equation of $0$ is the scalar equation
$0=0$ and the root set of $0$ is the punctured space $\mathbb{B}\setminus\{0\}$; it is at once the
square-zero set and the zero-divisor set, and **every element of the space is a nilpotent**, of
index one at the origin and of index two elsewhere. The nilpotent set is the whole space
$\mathbb{B}$, the largest a nilpotent class can be, and it strictly contains the nilpotent cone
$N(\tilde\Upsilon)=0$ of the parent quaternionic product. The implication *nilpotent implies zero
divisor* holds for the block at every element other than the origin, and the nilpotents and the
idempotents meet at the origin alone.

## The Notion and Its Product

**Definition (root of a central value).** Let $\star$ be a product on $\mathbb{B}$ and let
$\lambda\in\mathbb{C}$. A **root of $\lambda$ in $\star$** is a nonzero element $\tilde\Xi$ with
$$
\tilde\Xi\star\tilde\Xi=\lambda e_0 .
$$
The three central values the biquaternion algebra singles out are $-1$, $+1$ and $0$: the roots of
$-1$ are the imaginary units, the roots of $+1$ are the involutions, and the roots of $0$ are the
nonzero nilpotents of the product (*Definitions for the Study of the 12 Algebraic Structures*,
§*Powers, the Square and the Roots*).

**Definition (nilpotent of a product).** Let $\star$ be a product on $\mathbb{B}$. An element
$\tilde\Upsilon$ is **nilpotent of $\star$** when some power of it vanishes,
$$
\tilde\Upsilon^{\star k}=0 \quad\text{for some } k\geq1 ,
$$
the power being the left-nested reading
$$
\tilde\Upsilon^{\star k}=\bigl(\cdots\bigl((\tilde\Upsilon\star\tilde\Upsilon)\star\tilde\Upsilon\bigr)\cdots\star\tilde\Upsilon\bigr)
$$
when the product is not associative. The least such $k$ is the
**index of nilpotency**, and an element of index two, $\tilde\Upsilon\star\tilde\Upsilon=0$ with
$\tilde\Upsilon\neq0$, is a **square-zero element of $\star$**. The origin is the trivial nilpotent,
of index one (*Definitions for the Study of the 12 Algebraic Structures*, §*The Nilpotent*).

Throughout this article the product is the **antisymmetric quaternionic multiplication** $\diamond$,
and unqualified, *root* means a root of the block and *nilpotent* means a nilpotent of the block.
The block is not associative, so the power of the definition is read with its left-nested bracketing.
The root of $0$ is the square-zero element by the definitions article, and for the block both
classes are read through the one vanishing square.

## The Roots of Zero

**The root set of $0$ is the punctured space: $\{\tilde\Xi\neq0:\tilde\Xi\diamond\tilde\Xi=0\}=\mathbb{B}\setminus\{0\}$.**

The reduction of the block is the vanishing square, $\tilde\Xi\diamond\tilde\Xi=0$ for every element
$\tilde\Xi$ (*Introduction to the Antisymmetric Quaternionic Algebra of Biquaternions* for the
alternation it is read from, and *Square Roots of One and the Idempotents of the Antisymmetric
Quaternionic Algebra*, §*The Roots of One*, where it is stated). The equation of the roots of $0$ is
therefore the scalar equation $0=0$, satisfied at every element, and the root condition is the
condition $\tilde\Xi\neq0$ alone.

**Theorem (the roots of $0$ are all the nonzero elements).** The block's roots of $0$ are the
nonzero elements of $\mathbb{B}$,
$$
\{\tilde\Xi\neq0:\ \tilde\Xi\diamond\tilde\Xi=0\}=\mathbb{B}\setminus\{0\}.
$$

*Proof.* The reduction gives $\tilde\Xi\diamond\tilde\Xi=0$ for every $\tilde\Xi$, so the equation
$\tilde\Xi\diamond\tilde\Xi=0$ holds at every element and the root condition is exactly the
condition $\tilde\Xi\neq0$, which excludes the origin alone.

The root set of $0$ is therefore the whole punctured space, and it is as large as the space allows.
It is at once the square-zero set of the block and its zero-divisor set: an element is a root of $0$
exactly when it is a nonzero square-zero element, and by *Zero Divisors of the Antisymmetric
Quaternionic Algebra* it is then a two-sided zero divisor with itself as partner. The three names —
root of $0$, square-zero element, zero divisor — select one and the same set for the block. The
classes of the block that are not sets of the vanishing square, the roots of $+1$ and the
idempotents, are read in *Square Roots of One and the Idempotents of the Antisymmetric Quaternionic
Algebra*.

## The Nilpotents

**Every element of the block is a nilpotent: the nilpotent set is the whole space, the origin is of index one and every other element is of index two.**

### The Criterion

**Theorem (every element is a nilpotent).** Every element of $\mathbb{B}$ is a nilpotent of the
block,
$$
\tilde\Upsilon\diamond\tilde\Upsilon=0 \quad\text{for every } \tilde\Upsilon ,
$$
the origin being of index one and every other element of index two.

*Proof.* The block is alternating, $\tilde X\diamond\tilde X=0$ for every element $\tilde X$, by
*Introduction to the Antisymmetric Quaternionic Algebra of Biquaternions*; at
$\tilde X=\tilde\Upsilon$ this gives the display, so every element is nilpotent of index at most two,
and the nonzero elements have nonvanishing first power and are of index exactly two. The origin has
vanishing first power and is of index one.

The criterion is the alternation of the product read as an element statement, and it is met by every
element, the origin included. There is no hypothesis on the element, no scalar part and no vector
part to test: the equation $\tilde\Upsilon\diamond\tilde\Upsilon=0$ is an identity of the block and
not a condition on $\tilde\Upsilon$. It is the statement of §*The Roots of Zero*, read with the
element in place of the unknown of the root equation.

### The Index

**The index of a nonzero element is exactly two and the index of the origin is one; the block carries no nilpotent of index three or more.**

**Proposition (index two, and no higher index).** For every element $\tilde\Upsilon$ and every
$k\geq2$ the left-nested power vanishes,
$$
\tilde\Upsilon^{\diamond k}=0 \quad (k\geq2),
$$
and the index of a nonzero element is exactly two while the index of the origin is one. The block
carries no nilpotent of index three or more.

*Proof.* The left-nested square is $\tilde\Upsilon\diamond\tilde\Upsilon=0$; the third power is
$\bigl(\tilde\Upsilon\diamond\tilde\Upsilon\bigr)\diamond\tilde\Upsilon=0\diamond\tilde\Upsilon=0$,
and each higher power is formed from a vanishing power and vanishes again. A nonzero element has a
nonvanishing first power and a vanishing second power, so its index is exactly two; the origin has a
vanishing first power, so its index is one.

The boundedness of the index is a second sense in which the block is extreme. In the general plain
algebra the index is two or nothing, and an element is a nilpotent exactly on the pure isotropic
cone; here the index is two for every nonzero element, and the membership test is vacuous. The block
has the largest nilpotent set and the smallest positive index.

### The Nilpotent Class

**The nilpotent class of the block is the whole space $\mathbb{B}$, and the square-zero set is the punctured space $\mathbb{B}\setminus\{0\}$.**

**Proposition (the class is the whole space).** The set of the nilpotents of the block is the whole
space, and the set of the square-zero elements is the punctured space:
$$
\{\tilde\Upsilon:\tilde\Upsilon\diamond\tilde\Upsilon=0\}=\mathbb{B},
\qquad
\{\tilde\Upsilon\neq0:\tilde\Upsilon\diamond\tilde\Upsilon=0\}=\mathbb{B}\setminus\{0\} .
$$

*Proof.* The criterion gives $\tilde\Upsilon\diamond\tilde\Upsilon=0$ at every element, so the first
set is the whole space; the square-zero element of the definitions article is required to be nonzero
and to be of index two, so the second set is the same space without the origin, which is the trivial
nilpotent of index one.

The class is the largest a nilpotent class can be, and the square-zero set is the punctured space,
which is the most a square-zero set can be without containing the origin. The two sets differ by the
origin alone, which is a nilpotent but not a square-zero element, its index being one.

### The Relation to the Zero Divisors and to the Roots of Zero

**The nonzero nilpotents, the zero divisors and the roots of $0$ are one and the same set, the punctured space; the implication *nilpotent implies zero divisor* holds in the total form, with the origin as its only excluded element.**

**Proposition (the three classes coincide).** The nonzero nilpotents, the zero divisors and the roots
of $0$ of the block are one and the same set,
$$
\{\tilde\Upsilon\neq0:\tilde\Upsilon\diamond\tilde\Upsilon=0\}
=\mathbb{B}\setminus\{0\}
=\{\tilde\Xi\neq0:\tilde\Xi\diamond\tilde\Xi=0\}.
$$

*Proof.* The first equality says that the nonzero square-zero elements are the whole punctured
space, which is §*The Nilpotent Class*; the second says that the root set of $0$ is the same
punctured space, which is §*The Roots of Zero*. The zero divisors are that set once more, a nonzero
square-zero element being a zero divisor with itself as partner, by *Zero Divisors of the
Antisymmetric Quaternionic Algebra*.

| class | set of the block |
|---|---|
| root of $0$ | $\mathbb{B}\setminus\{0\}$ |
| square-zero element | $\mathbb{B}\setminus\{0\}$ |
| nilpotent | $\mathbb{B}$ |
| zero divisor | $\mathbb{B}\setminus\{0\}$ |

**Corollary (the implication *nilpotent implies zero divisor*).** For the block the implication
*nilpotent implies zero divisor* holds at every element other than the origin: the nilpotent set is
the whole space, the zero-divisor set is the punctured space, and the two differ by the origin
alone, which is the trivial nilpotent and is excluded from the zero divisors by their definition.

*Proof.* The definition of the zero divisor requires a nonzero partner of a nonzero element
(*Definitions for the Study of the 12 Algebraic Structures*, §*The Zero Divisor and the
Annihilator*); a nonzero nilpotent has itself as a partner and is therefore a zero divisor, while
the origin is excluded. The implication is a statement of a product and not of the twelve, and its
reading for each product is *Definitions for the Study of the 12 Algebraic Structures*, §*The
Nilpotent*.

### The Relation to the Idempotents

**No nonzero element is both an idempotent and a nilpotent; the two classes meet at the origin alone.**

**Remark (the two classes meet at the origin).** No nonzero element of the block is both an
idempotent and a nilpotent. The idempotent set of the block is the origin alone (*Square Roots of
One and the Idempotents of the Antisymmetric Quaternionic Algebra*), so an idempotent of the block
is the origin, which is the trivial nilpotent; and a nonzero nilpotent has a vanishing square while
a nonzero idempotent would satisfy $\tilde\Pi\diamond\tilde\Pi=\tilde\Pi\neq0$. The two classes
therefore meet at the origin and nowhere else.

The statement is the sharp form of a general fact. In an associative unital product the idempotents
and the nilpotents are disjoint outside the origin, and in the block they are the origin and the
whole space, the two extremes that the definitions allow: the smallest idempotent set and the
largest nilpotent set.

### The Conjugations and the Matrix Model

**The conjugations carry the nilpotent class onto itself, and on the values of the block the natural conjugation acts as the negative of the identity, $(\tilde P\diamond\tilde Q)^{\natural}=-\tilde P\diamond\tilde Q$, while the complex conjugation is an automorphism and the star is the negative of the complex conjugation; in either matrix model the square of every element is the zero matrix.**

**Proposition (the conjugations preserve the class).** The natural conjugation ${}^{\natural}$, the
complex conjugation $\overline{\cdot}$ and the star ${}^{*}$ carry the nilpotent set of the block
onto itself, the set being the whole space; and on the values of the block
$$
(\tilde P\diamond\tilde Q)^{\natural}=-\tilde P\diamond\tilde Q , \qquad
\overline{\tilde P\diamond\tilde Q}=\bar{\tilde P}\diamond\bar{\tilde Q} , \qquad
(\tilde P\diamond\tilde Q)^{*}=-\overline{\tilde P\diamond\tilde Q} .
$$

*Proof.* The nilpotent set is the whole space, so a bijection carries it onto itself. For the first
display, the natural conjugation is an anti-automorphism of the plain product, so
$(\tilde P^{\natural}\tilde Q)^{\natural}=\tilde Q^{\natural}\tilde P$; applying it to the two terms
of the definition of the block gives
$\tfrac12(\tilde Q^{\natural}\tilde P-\tilde P^{\natural}\tilde Q)=-\tilde P\diamond\tilde Q$. The
complex conjugation is an automorphism of the plain product with
$\bar{\tilde P^{\natural}}=\bar{\tilde P}^{\natural}$, so it passes through the definition and gives
the second display. The star is the composite of the complex conjugation and the natural
conjugation; applying the first display and then the second gives
$(\tilde P\diamond\tilde Q)^{*}=\overline{-(\tilde P\diamond\tilde Q)}=-\overline{\tilde P\diamond\tilde Q}$.

**Remark (the matrix model).** In either matrix model of the block the square of an element
vanishes, so the matrix of the square is the zero matrix and the nilpotent set is the whole matrix
space: $\mathsf{M}(\tilde P\diamond\tilde P)=\mathsf{M}(0)=0$ for every $\tilde P$, in the $2\times2$
model and in the $4\times4$ model alike (*The Antisymmetric Quaternionic Algebra in the $2\times2$
Matrix Element Representation $M_2(\mathbb{C})$*, *The Antisymmetric Quaternionic Algebra in the
$4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$*). The matrix models therefore carry no
nilpotent condition beyond the vanishing of the square.

### The Comparison with the Parent Product

**The nilpotent set of the block is the whole space and strictly contains the nilpotent cone $N(\tilde P)=0$ of the parent quaternionic product, the difference being the complement of the cone.**

**Remark (the parent nilpotents).** The parent quaternionic product $\tilde P^{\natural}\tilde Q$ has
the square $\tilde P^{\natural}\tilde P=N(\tilde P)e_0$, with $N(\tilde P)=\sum_\mu P_\mu^{2}$ the
algebraic norm, so its square-zero set is the cone $N(\tilde P)=0$, which is also its zero-divisor
cone; its nilpotents are the square-zero elements of that cone, the index being two there by the
central-square identity (*Square Roots of Zero and the Nilpotents of the General Quaternionic
Algebra*). The block is the parent with the scalar part removed, and with the scalar part removed
the parent's square, a central reading of the algebraic norm, becomes the zero of the block: the
parent's cone widens to the whole space, and the parent's index two is kept by every nonzero
element. The block's nilpotent set strictly contains the parent's, and the difference is the
complement of the cone, on which the parent's square is a nonzero central value and the block's
square is zero. The nilpotent sets of the twelve structures of the biquaternion space are read side
by side in *Nilpotents in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, and
the real-space analogue is *Nilpotents in the 6 Algebraic Structures over the Quaternion
$\mathbb{R}$ Space*.

## Summary

For the antisymmetric quaternionic multiplication
$\tilde P\diamond\tilde Q=P_0\vec Q-Q_0\vec P-\vec P\times\vec Q$ the square of every
element vanishes, so the equation of the roots of $0$ holds at every element and the root set of $0$
is the punctured space, at once the square-zero set and the zero-divisor set of the block. Every
element is a nilpotent: the square-zero set is the punctured space, the index of a nonzero element
is exactly two, the index of the origin is one, and no element has index three or more; the
nilpotent set is therefore the whole space, and it strictly contains the nilpotent cone
$N(\tilde\Upsilon)=0$ of the parent quaternionic product, which is the zero-divisor cone. Every
nonzero nilpotent is a two-sided zero divisor with itself as the annihilating partner, and the
implication *nilpotent implies zero divisor* holds for the block at every element other than the
origin. The nilpotents and the idempotents meet at the origin alone, the idempotent set being the
origin. The conjugations carry the class onto itself; on the values of the block the natural
conjugation acts as the negative of the identity, the complex conjugation is an automorphism, and
the star is the negative of the complex conjugation; in either matrix model the square is the zero
matrix.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\diamond\tilde Q=P_0\vec Q-Q_0\vec P-\vec P\times\vec Q$ | the antisymmetric quaternionic multiplication, the operation $\mathrm{AQA}$ |
| $\tilde\Upsilon\diamond\tilde\Upsilon=0$ | the criterion, the vanishing square of every element |
| $\mathbb{B}\setminus\{0\}$ | the root set of $0$, at once the square-zero set and the zero-divisor set |
| $\mathbb{B}$ | the nilpotent set of the block, the whole space |
| $2$ | the index of nilpotency of every nonzero element, the origin being of index one |
| $N(\tilde\Upsilon)=\sum_\mu\Upsilon_\mu^{2}$ | the algebraic norm of the parent product, whose vanishing cone is the parent's nilpotent set |
| $\mathsf{M}(\tilde P\diamond\tilde P)=0$ | the square of every element in either matrix model |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the root of a central value, the nilpotent, the index of nilpotency, the square-zero element and the relativity of the definitions
- *Introduction to the Antisymmetric Quaternionic Algebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-quaternionic-algebra-of-biquaternions.md`), for the operation, its alternation and its table
- *Square Roots of One and the Idempotents of the Antisymmetric Quaternionic Algebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-antisymmetric-quaternionic-algebra.md`), for the reduction of the vanishing square and for the idempotent set, which meets the nilpotents at the origin
- *Square Roots of a General Element in the Antisymmetric Quaternionic Algebra* (`articles_maths/square-roots-of-a-general-element-in-the-antisymmetric-quaternionic-algebra.md`), for the general equation $\tilde\Xi\diamond\tilde\Xi=a$ and for the square roots of the origin, which are the whole space
- *Zero Divisors of the Antisymmetric Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-antisymmetric-quaternionic-algebra.md`), for the coincidence of the square-zero set with the zero-divisor set and for the annihilating partner
- *Annihilators of the Antisymmetric Quaternionic Algebra* (`articles_maths/annihilators-of-the-antisymmetric-quaternionic-algebra.md`), for the annihilators of an element, which contain it
- *Square Roots of Zero and the Nilpotents of the General Quaternionic Algebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-general-quaternionic-algebra.md`), for the nilpotent cone $N=0$ of the parent product
- *Nilpotents in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/nilpotents-in-the-12-algebraic-structures-over-the-biquaternion-c-space.md`), for the square-zero sets of the twelve structures side by side
