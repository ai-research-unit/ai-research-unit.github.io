# __Square Roots of Minus One, Zero and Plus One in the Antisymmetric Plain Algebra__

## Introduction

A root of a central value is defined by an equation in which the product occurs, so it belongs to
the product (*Definitions for the Study of the 12 Algebraic Structures*, §*Powers, the Square and
the Roots*). The block of this article is the antisymmetric plain multiplication
$$
\tilde\Xi\wedge\tilde Q=\tfrac12\bigl(\tilde\Xi\tilde Q-\tilde Q\tilde\Xi\bigr)=\mathbf\Xi\times\mathbf{Q},
$$
the cross product of the two vector parts, which is alternating and without a unit
(*Introduction to the Antisymmetric Plain Algebra of Biquaternions*). The article solves the three
equations
$$
\tilde\Xi\wedge\tilde\Xi=-e_0,\qquad
\tilde\Xi\wedge\tilde\Xi=0,\qquad
\tilde\Xi\wedge\tilde\Xi=+e_0 ,
$$
and the solution sets are decided by one fact: the block is alternating, so the left side is zero
for every element and the three equations reduce to the three scalar equations $0=-e_0$, $0=0$
and $0=+e_0$.

The outcome is the sharpest form of the absence law. The block has **no root of $-1$** and **no
root of $+1$**, because its square is never central and nonzero; its **roots of $0$ are all the
nonzero elements of the space**, because its square vanishes identically. Of the three central
values the block carries roots of one only, and that one totally. The roots of $0$ are the
square-zero elements of the block, which are the subject of *Nilpotents of the Antisymmetric
Plain Algebra*, and the zero divisors of the block, which are the same set (*Zero Divisors of the
Antisymmetric Plain Algebra*); the relation of the three sets to the idempotents is given at the
end, where the idempotent article of the block is cited.

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

Throughout this article the product is the **antisymmetric plain multiplication** $\wedge$, and
unqualified, *root* means a root of the block. The square of the block is the specialisation to
the block of the general square of *The Symmetric and Antisymmetric Parts of an Algebra Product*;
the roots of the three values in the general plain product, to which the block is compared, are
*Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*.

## The Common Reduction

**Proposition (the reduction).** For every element $\tilde\Xi$,
$$
\tilde\Xi\wedge\tilde\Xi=0 ,
$$
and consequently the three equations $\tilde\Xi\wedge\tilde\Xi=-e_0$, $\tilde\Xi\wedge\tilde\Xi=0$ and
$\tilde\Xi\wedge\tilde\Xi=+e_0$ are equivalent to the three scalar equations $0=-e_0$, $0=0$ and
$0=+e_0$.

*Proof.* The block is alternating, $\tilde X\wedge\tilde X=0$ for every $\tilde X$, by
*Introduction to the Antisymmetric Plain Algebra of Biquaternions*; read at $\tilde X=\tilde\Xi$
this is the display. Substituting the display into each of the three equations gives the
corresponding scalar equation.

The reduction is the whole of the computation, because the right side of each equation is central
and the left side is always zero, which is central. The three sets below are therefore read off
the three scalar equations alone, and no coordinate computation is needed.

## The Roots of Minus One

**Theorem (no roots of $-1$).** The block has no root of $-1$; equivalently, the equation
$\tilde\Xi\wedge\tilde\Xi=-e_0$ has no solution.

*Proof.* The reduction gives $\tilde\Xi\wedge\tilde\Xi=0$, and $0\neq-e_0$ because $e_0$ is
nonzero, the scalars of the field being of characteristic zero. Hence the equation fails for every
$\tilde\Xi$.

The absence is the absence of a square that is central and negative. The block removes the scalar
part of the parent product, and the root of $-1$ is a statement about the scalar part of a square;
with the scalar part removed the equation cannot be met. The imaginary units of the algebra, which
are the roots of $-1$ of the plain product, are roots of $-1$ of the plain product alone.

## The Roots of Zero

**Theorem (the roots of $0$ are all the nonzero elements).** The block's roots of $0$ are the
nonzero elements of $\mathbb{B}$,
$$
\{\tilde\Xi\neq0:\ \tilde\Xi\wedge\tilde\Xi=0\}=\mathbb{B}\setminus\{0\}.
$$

*Proof.* The reduction gives $\tilde\Xi\wedge\tilde\Xi=0$ for every $\tilde\Xi$, so the equation
$\tilde\Xi\wedge\tilde\Xi=0$ holds at every element and the root condition is exactly the condition
$\tilde\Xi\neq0$, which excludes the origin alone.

The root set of $0$ is therefore the whole punctured space, and it is at once the square-zero set
of the block and its zero-divisor set: an element is a root of $0$ exactly when it is a nonzero
square-zero element, and by *Zero Divisors of the Antisymmetric Plain Algebra* it is then a
two-sided zero divisor with itself as partner. The three names — root of $0$, square-zero element,
zero divisor — select one and the same set for the block, and the set is as large as the space
allows.

## The Roots of Plus One

**Theorem (no roots of $+1$).** The block has no root of $+1$; equivalently, the equation
$\tilde\Xi\wedge\tilde\Xi=+e_0$ has no solution.

*Proof.* The reduction gives $\tilde\Xi\wedge\tilde\Xi=0$, and $0\neq+e_0$ because $e_0$ is
nonzero. Hence the equation fails for every $\tilde\Xi$.

The roots of $+1$ are the involutions of the product, and the block has none. In particular the
element $e_0$ is not a root of $+1$ of the block, although it is the unit of the ambient algebra
and a root of $+1$ of the plain product; the equation is read in the product and not in the
algebra, and the product is not the plain one.

## The Three Sets Compared

| central value $\lambda$ | the equation | the root set of the block |
|---|---|---|
| $-1$ | $\tilde\Xi\wedge\tilde\Xi=-e_0$ | empty |
| $0$ | $\tilde\Xi\wedge\tilde\Xi=0$ | $\mathbb{B}\setminus\{0\}$, the punctured space |
| $+1$ | $\tilde\Xi\wedge\tilde\Xi=+e_0$ | empty |

The table is the reduction read value by value. Two of the three sets are empty and the third is
the complement of the origin, and the table is the opposite of the table of the general plain
algebra, where the three sets are three proper families: the roots of $-1$ there are the
imaginaries of the three families of *Square Roots of Minus One, Zero and Plus One in the General
Plain Algebra*, the roots of $0$ the pure isotropic cone, and the roots of $+1$ the involutions.
The difference is the removal of the scalar part: the three equations of the plain product are
three conditions on the square, and the square of the block is identically zero, so two conditions
are impossible and the third is vacuous.

## The Relation to the Idempotents and to the Zero Divisors

**Remark (the idempotents).** The idempotents of a product are its roots of $+1$ in a scaled
sense, and for the block neither notion has a nontrivial element: there is no root of $+1$ by the
theorem, and the idempotent equation $\tilde\Pi\wedge\tilde\Pi=\tilde\Pi$ is met by the origin
alone, since its left side is zero (*Idempotents of the Antisymmetric Plain Algebra*). The
coincidence is not a new fact; it is the same vanishing square read twice.

**Remark (the zero divisors and the nilpotents).** The roots of $0$ are the nonzero elements, and
so are the nilpotents and the zero divisors of the block. The three classes are one class,
$$
\{\text{roots of }0\}=\{\text{square-zero elements}\}=\{\text{zero divisors}\}=\mathbb{B}\setminus\{0\},
$$
and the equalities are the content of the two companion articles of the block. In particular the
implication *nilpotent implies zero divisor*, which for the parent product holds and for the plain
sesquilinear product fails, holds for the block in the total form: every element is a nilpotent
and every nonzero element is a two-sided zero divisor, with itself as the annihilating partner.
The origin is the single nilpotent that is not a zero divisor, and it is excluded by the definition
of the zero divisor, which requires both the element and its partner to be nonzero.

## The Relation to the Parent Product

**Remark (the parent squares).** The parent general plain bilinear product $\tilde\Xi\tilde Q$ has
the square
$$
\tilde\Xi^{2}=\bigl[\Xi_0^{2}-(\mathbf\Xi,\mathbf\Xi)\bigr]e_0+2\Xi_0\mathbf\Xi ,
$$
whose central part is $\Xi_0^{2}-(\mathbf\Xi,\mathbf\Xi)$ and whose vector part is $2\Xi_0\mathbf\Xi$; its
three root equations are therefore the pairs $2\Xi_0\mathbf\Xi=0$ and
$\Xi_0^{2}-(\mathbf\Xi,\mathbf\Xi)=\lambda$ over $\lambda=-1,0,+1$, and not the three level sets of one
quadratic form. The algebraic norm of the parent, $N(\tilde\Xi)=\Xi_0^{2}+(\mathbf\Xi,\mathbf\Xi)$, is the central
part of the conjugated square $\tilde\Xi\tilde\Xi^{\natural}$ and it is not the central part of
$\tilde\Xi^{2}$. The block removes the scalar part of the parent, and with the scalar part removed
the square loses its central part: the three conditions become the single statement that the
square is zero, and the two non-vacuous conditions of the parent are replaced by the two empty
tables above. The block's root set of $0$, the whole punctured space, strictly contains the
parent's root set of $0$, the pure isotropic cone; the block's roots of $-1$ and $+1$ are empty
where the parent's are nonempty families of the plain product.

## Summary

For the antisymmetric plain multiplication $\tilde\Xi\wedge\tilde Q=\mathbf\Xi\times\mathbf{Q}$ the
square of every element is zero, $\tilde\Xi\wedge\tilde\Xi=0$, because the block is alternating; the
three equations of the roots of $-1$, of $0$ and of $+1$ therefore reduce to the three scalar
equations $0=-e_0$, $0=0$ and $0=+e_0$. The block has no root of $-1$ and no root of $+1$, and
its roots of $0$ are all the nonzero elements of the space. The root set of $0$ coincides with the
square-zero set and with the zero-divisor set of the block, all three being the punctured space;
the idempotent set is the origin alone, the idempotent equation being the scaled root of $+1$
equation. The comparison with the parent product is the comparison of a vanishing square with a
nonvanishing one: the parent's root sets are three proper families, read from the two conditions
$2\Xi_0\mathbf\Xi=0$ and $\Xi_0^{2}-(\mathbf\Xi,\mathbf\Xi)=\lambda$ on the square, while the block's are
the two empty sets and the complement of the origin, read from the single condition that its square
is zero.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Xi\wedge\tilde Q=\tfrac12(\tilde\Xi\tilde Q-\tilde Q\tilde\Xi)=\mathbf\Xi\times\mathbf{Q}$ | the antisymmetric plain multiplication, the operation $\mathrm{APA}$ |
| $\tilde\Xi\wedge\tilde\Xi=0$ | the reduction, the square of every element |
| $\lambda\in\{-1,0,+1\}$ | the three central values whose roots are sought |
| $\mathbb{B}\setminus\{0\}$ | the root set of $0$, at once the square-zero set and the zero-divisor set of the block |
| $N(\tilde\Xi)=\Xi_0^{2}+(\mathbf\Xi,\mathbf\Xi)$ | the algebraic norm of the parent product, the central part of $\tilde\Xi\tilde\Xi^{\natural}$, not of $\tilde\Xi^{2}$ |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the root of a central value, the power and the square, and for the relativity of the definitions to the product
- *Introduction to the Antisymmetric Plain Algebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-plain-algebra-of-biquaternions.md`), for the operation, its alternation and its table
- *Nilpotents of the Antisymmetric Plain Algebra* (`articles_maths/nilpotents-of-the-antisymmetric-plain-algebra.md`), for the square-zero set of the block, which is the root set of $0$
- *Zero Divisors of the Antisymmetric Plain Algebra* (`articles_maths/zero-divisors-of-the-antisymmetric-plain-algebra.md`), for the coincidence of the square-zero set with the zero-divisor set
- *Idempotents of the Antisymmetric Plain Algebra* (`articles_maths/idempotents-of-the-antisymmetric-plain-algebra.md`), for the idempotent equation, met by the origin alone
- *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-general-plain-algebra.md`), for the three root sets of the plain product, against which the block's two empty sets are read
