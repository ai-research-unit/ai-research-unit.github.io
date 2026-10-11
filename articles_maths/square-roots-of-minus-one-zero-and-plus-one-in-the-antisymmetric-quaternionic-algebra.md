# __Square Roots of Minus One, Zero and Plus One in the Antisymmetric Quaternionic Algebra__

## Introduction

A root of a central value is defined by an equation in which the product occurs, so it belongs
to the product (*Definitions for the Study of the 12 Algebraic Structures*, §*Powers, the Square
and the Roots*). The block of this article is the antisymmetric quaternionic multiplication
$$
\tilde P\diamond\tilde Q=\tfrac12\bigl(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P\bigr)
=P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q ,
$$
which is alternating and without a unit (*Introduction to the Antisymmetric Quaternionic Algebra
of Biquaternions*). The article solves the three equations
$$
\tilde P\diamond\tilde P=-e_0,\qquad
\tilde P\diamond\tilde P=0,\qquad
\tilde P\diamond\tilde P=+e_0 ,
$$
and the solution sets are decided by one fact: the block is alternating, so the left side is
zero for every element and the three equations reduce to the three scalar equations
$0=-e_0$, $0=0$ and $0=+e_0$.

The outcome is the sharpest form of the absence law. The block has **no root of $-1$** and **no
root of $+1$**, because its square is never central and nonzero; its **roots of $0$ are all the
nonzero elements of the space**, because its square vanishes identically. Of the three central
values the block carries roots of one only, and that one totally. The roots of $0$ are the
square-zero elements of the block, which are the subject of *Nilpotents of the Antisymmetric
Quaternionic Algebra*, and the zero divisors of the block, which are the same set
(*Zero Divisors of the Antisymmetric Quaternionic Algebra*); the relation of the three sets to
the idempotents is given at the end, where the idempotent article of the block is cited.

## The Notion and Its Product

**Definition (root of a central value).** Let $\star$ be a product on $\mathbb{B}$ and let
$\lambda\in\mathbb{C}$. A **root of $\lambda$ in $\star$** is a nonzero element $\tilde P$ with
$$
\tilde P\star\tilde P=\lambda e_0 .
$$
The three central values the biquaternion algebra singles out are $-1$, $+1$ and $0$.

Throughout this article the product is the **antisymmetric quaternionic multiplication**
$\diamond$, and unqualified, *root* means a root of the block. The square of the block is the
specialisation to the block of the general square of *The Symmetric and Antisymmetric Parts of
an Algebra Product*; the roots of the three values in the general plain product, to which the
block is compared, are *Square Roots of Minus One, Zero and Plus One in the General Plain
Algebra*.

## The Common Reduction

**Proposition (the reduction).** For every element $\tilde P$,
$$
\tilde P\diamond\tilde P = 0 ,
$$
and consequently the three equations $\tilde P\diamond\tilde P=-e_0$,
$\tilde P\diamond\tilde P=0$ and $\tilde P\diamond\tilde P=+e_0$ are equivalent to the three
scalar equations $0=-e_0$, $0=0$ and $0=+e_0$.

*Proof.* The block is alternating, $\tilde X\diamond\tilde X=0$ for every $\tilde X$, by
*Introduction to the Antisymmetric Quaternionic Algebra of Biquaternions*; read at
$\tilde X=\tilde P$ this is the display. Substituting the display into each of the three
equations gives the corresponding scalar equation.

The reduction is the whole of the computation, because the right side of each equation is
central and the left side is always zero, which is central. The three sets below are therefore
read off the three scalar equations alone, and no coordinate computation is needed.

## The Roots of Minus One

**Theorem (no roots of $-1$).** The block has no root of $-1$; equivalently, the equation
$\tilde P\diamond\tilde P=-e_0$ has no solution.

*Proof.* The reduction gives $\tilde P\diamond\tilde P=0$, and $0\neq-e_0$ because $e_0$ is
nonzero, the scalars of the field being of characteristic zero. Hence the equation fails for
every $\tilde P$.

The absence is the absence of a square that is central and negative. The block removes the
scalar part of the parent product, and the root of $-1$ is a statement about the scalar part of
a square; with the scalar part removed the equation cannot be met.

## The Roots of Zero

**Theorem (the roots of $0$ are all the nonzero elements).** The block's roots of $0$ are the
nonzero elements of $\mathbb{B}$,
$$
\{\tilde P\neq0:\ \tilde P\diamond\tilde P=0\}=\mathbb{B}\setminus\{0\}.
$$

*Proof.* The reduction gives $\tilde P\diamond\tilde P=0$ for every $\tilde P$, so the equation
$\tilde P\diamond\tilde P=0$ holds at every element and the root condition is exactly the
condition $\tilde P\neq0$, which excludes the origin alone.

The root set of $0$ is therefore the whole punctured space, and it is at once the square-zero
set of the block and its zero-divisor set: an element is a root of $0$ exactly when it is a
nonzero square-zero element, and by *Zero Divisors of the Antisymmetric Quaternionic Algebra* it
is then a two-sided zero divisor with itself as partner. The three names — root of $0$,
square-zero element, zero divisor — select one and the same set for the block, and the set is as
large as the space allows.

## The Roots of Plus One

**Theorem (no roots of $+1$).** The block has no root of $+1$; equivalently, the equation
$\tilde P\diamond\tilde P=+e_0$ has no solution.

*Proof.* The reduction gives $\tilde P\diamond\tilde P=0$, and $0\neq+e_0$ because $e_0$ is
nonzero. Hence the equation fails for every $\tilde P$.

The roots of $+1$ are the involutions of the product, and the block has none. In particular the
element $e_0$ is not a root of $+1$ of the block, although it is the unit of the ambient algebra
and a root of $+1$ of the plain product; the equation is read in the product and not in the
algebra, and the product is not the plain one.

## The Three Sets Compared

| central value $\lambda$ | the equation | the root set of the block |
|---|---|---|
| $-1$ | $\tilde P\diamond\tilde P=-e_0$ | empty |
| $0$ | $\tilde P\diamond\tilde P=0$ | $\mathbb{B}\setminus\{0\}$, the punctured space |
| $+1$ | $\tilde P\diamond\tilde P=+e_0$ | empty |

The table is the reduction read value by value. Two of the three sets are empty and the third is
the complement of the origin, and the table is the opposite of the table of the general plain
algebra, where the three sets are three proper families: the roots of $-1$ there are the
imaginaries of the three families of *Square Roots of Minus One, Zero and Plus One in the
General Plain Algebra*, the roots of $0$ the pure isotropic cone, and the roots of $+1$ the
involutions. The difference is the removal of the scalar part: the three equations of the plain
product are three conditions on the central square, and the central square of the block is
identically zero, so two conditions are impossible and the third is vacuous.

## The Relation to the Idempotents and to the Zero Divisors

**Remark (the idempotents).** The idempotents of a product are its roots of $+1$ in a scaled
sense, and for the block the two notions are both trivial: there is no root of $+1$ by the
theorem, and the idempotent equation $\tilde\Pi\diamond\tilde\Pi=\tilde\Pi$ is met by the origin
alone, since its left side is zero (*Idempotents of the Antisymmetric Quaternionic Algebra*).
The coincidence is not a new fact; it is the same vanishing square read twice.

**Remark (the zero divisors and the nilpotents).** The roots of $0$ are the nonzero elements,
and so are the nilpotents and the zero divisors of the block. The three classes are one class,
$$
\{\text{roots of }0\}=\{\text{square-zero elements}\}=\{\text{zero divisors}\}=\mathbb{B}\setminus\{0\},
$$
and the equalities are the content of the two companion articles of the block. In particular the
implication *nilpotent implies zero divisor*, which holds for the parent product and fails for the
plain sesquilinear product (*Definitions for the Study of the 12 Algebraic Structures*, §*The
Nilpotent*), holds
for the block at every nonzero nilpotent: every element is a nilpotent and every nonzero element is
a zero divisor, so the only element at which the implication is not read is the origin, the trivial
nilpotent, which is excluded from the zero divisors by their definition.

## The Relation to the Parent Product

**Remark (the parent squares).** The parent quaternionic product $\tilde P^{\natural}\tilde Q$
has the square $\tilde P^{\natural}\tilde P=N(\tilde P)e_0$, a central value; its three root
equations are the three conditions $N(\tilde P)=-1$, $N(\tilde P)=0$ and $N(\tilde P)=+1$ on
the norm $N(\tilde P)=\sum_\mu P_\mu^{2}$, whose zero set is the zero-divisor cone. The block
removes the scalar part of the parent, and with the scalar part removed the square loses the
norm: the three conditions become the single statement that the square is zero, and the two
non-vacuous conditions of the parent are replaced by the two empty sets above. The block's
root set of $0$, the whole punctured space, strictly contains the parent's root set of $0$, the
zero-divisor cone; the block's roots of $-1$ and $+1$ are empty where the parent's are the two
level sets of the norm.

## Summary

For the antisymmetric quaternionic multiplication $\tilde P\diamond\tilde Q=P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q$ the square of every element is zero,
$\tilde P\diamond\tilde P=0$, because the block is alternating; the three equations of the roots
of $-1$, of $0$ and of $+1$ therefore reduce to the three scalar equations $0=-e_0$, $0=0$ and
$0=+e_0$. The block has no root of $-1$ and no root of $+1$, and its roots of $0$ are all the
nonzero elements of the space. The root set of $0$ coincides with the square-zero set and with
the zero-divisor set of the block, all three being the punctured space; the idempotent set is
the origin alone, the idempotent equation being the scaled root of $+1$ equation. The comparison
with the parent quaternionic product is the comparison of a vanishing central square with a
nonvanishing one: the parent's three sets are the three level sets of the norm, and the block's
are two empty sets and the complement of the origin.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\diamond\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P)=P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q$ | the antisymmetric quaternionic multiplication, the operation $\mathrm{AQA}$ |
| $\tilde P\diamond\tilde P=0$ | the reduction, the square of every element |
| $\lambda\in\{-1,0,+1\}$ | the three central values whose roots are sought |
| $\mathbb{B}\setminus\{0\}$ | the root set of $0$, at once the square-zero set and the zero-divisor set of the block |
| $N(\tilde P)=\sum_\mu P_\mu^{2}$ | the norm of the parent product, whose level sets are the parent's three root sets |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the root of a central value, the power and the square, and for the relativity of the definitions to the product
- *Introduction to the Antisymmetric Quaternionic Algebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-quaternionic-algebra-of-biquaternions.md`), for the operation, its alternation and its table
- *Nilpotents of the Antisymmetric Quaternionic Algebra* (`articles_maths/nilpotents-of-the-antisymmetric-quaternionic-algebra.md`), for the square-zero set of the block, which is the root set of $0$
- *Zero Divisors of the Antisymmetric Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-antisymmetric-quaternionic-algebra.md`), for the coincidence of the square-zero set with the zero-divisor set
- *Idempotents of the Antisymmetric Quaternionic Algebra* (`articles_maths/idempotents-of-the-antisymmetric-quaternionic-algebra.md`), for the idempotent equation, met by the origin alone
- *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-general-plain-algebra.md`), for the three root sets of the plain product, against which the block's two empty sets are read
