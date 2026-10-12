# __Square Roots of Minus One, Zero and Plus One in the Antisymmetric Plain Algebra__

## Introduction

The antisymmetric plain algebra of $\mathbb{H}$ carries the cross product
$\tilde p\times\tilde q=\tfrac12(\tilde p\tilde q-\tilde q\tilde p)=\mathbf p\times\mathbf q$ of
*Introduction to the Antisymmetric Plain Algebra of Quaternions*. This article reads the three
central root equations of the block — the roots of $-1$, of $0$ and of $+1$ — the special case
$\tilde\xi\times\tilde\xi=\lambda e_0$ of the square roots of a central value, as defined in the
common apparatus of *Definitions for the Study of the 6 Algebraic Structures*.

The answer is forced by a single fact: the operation is alternating, so **the square of every element
is zero**, and the three equations collapse at once. The block has no root of $-1$ and no root of
$+1$, and its roots of $0$ are every nonzero element of the space.

**This is not the algebra $\mathbb{H}$.** The two share the space, the addition and the real scalars,
but $\times$ is a different multiplication, alternating and without a unit. Throughout, the natural
sign ${}^{\natural}$ is the quaternion conjugation, the bar is the identity because $\mathbb{R}$ has
no nontrivial involution, and the star coincides with the natural sign and gives nothing new.

The square and its polarisation are *Introduction to the Antisymmetric Plain Algebra of
Quaternions*; the zero divisors, which coincide with the roots of $0$, are *Zero Divisors of the
Antisymmetric Plain Algebra*, and the folding of the idempotents and of the nilpotents is *The
Specificities of the Antisymmetric Plain Algebra*, both below this article in this category. The
roots of the other five products are read in the comparison at the end.

**Conventions.** The algebra is $\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$ and
$e_1^2=e_2^2=e_3^2=-e_0$. A generic element is $\tilde q=q_0e_0+\mathbf q$ with
$\mathbf q=\sum_{k=1}^{3}q_ke_k$ and $q_\mu\in\mathbb{R}$; the **centre** is
$\mathbb{R}_{\mathbb{H}}=\mathbb{R}e_0$ and the **vector subspace** is
$\mathrm{Vect}(\mathbb{H})=\{\mathbf q\}$.

## The Notion and the Product

**Definition.** Let $\lambda\in\mathbb{R}$. A **root of $\lambda$ in the block** is a nonzero element
$\tilde\xi$ with

$$
\tilde\xi\times\tilde\xi=\lambda e_0 ,
$$

the central value $\lambda e_0$ being read in the space $\mathbb{H}$. The three values singled out are
$-1$, $+1$ and $0$: the roots of $-1$ are the imaginary units, the roots of $+1$ the involutions, and
the roots of $0$ the nonzero nilpotents of the block.

## The Three Equations and the Reduction

**Theorem (the reduction).** The three equations reduce to the three scalar equations

$$
0=-e_0,\qquad 0=0,\qquad 0=+e_0 ,
$$

and the root sets are

$$
\{\tilde\xi:\tilde\xi\times\tilde\xi=-e_0\}=\varnothing,\qquad
\{\tilde\xi:\tilde\xi\times\tilde\xi=0\}=\mathbb{H}\setminus\{0\},\qquad
\{\tilde\xi:\tilde\xi\times\tilde\xi=+e_0\}=\varnothing .
$$

*Proof.* The operation is alternating, $\tilde\xi\times\tilde\xi=0$ for every $\tilde\xi$; the left
side of each equation is therefore $0$, and the equations become $0=\lambda e_0$ for
$\lambda=-1,0,+1$. The first and the third are impossible, the second is an identity, and the
definition of a root excludes $\tilde\xi=0$ from the last set.

## The Roots of Zero

**Theorem.** The roots of $0$ are all the nonzero elements,

$$
\tilde\xi\times\tilde\xi=0\iff\tilde\xi\neq0 ,
$$

the whole four-dimensional space with the origin removed. The root set of $0$ is the **square-zero
set** and the **zero-divisor set** of the block, all three being the punctured space.

*Proof.* The square vanishes identically, so the equation is satisfied by every nonzero element and
by no other; and an element is a two-sided zero divisor of an alternating product exactly when it is
nonzero, with itself as partner (*Zero Divisors of the Antisymmetric Plain Algebra*, below this
article in this category).

**Remark (the whole space, and not only the vector subspace).** The root set of $0$ is the whole
space, and **not** the vector subspace: the scalar coordinate does not enter the square, since
$\tilde\xi\times\tilde\xi=0$ for a non-pure element as well. The set has real dimension four, and its
elements are pairwise partners of themselves.

## The Roots of Minus One and of Plus One

**Theorem.** The block has no root of $-1$ and no root of $+1$:

$$
\{\tilde\xi:\tilde\xi\times\tilde\xi=-e_0\}=\varnothing,\qquad
\{\tilde\xi:\tilde\xi\times\tilde\xi=+e_0\}=\varnothing .
$$

*Proof.* Either equation would read $0=\pm e_0$, a value with a nonzero scalar coordinate, against the
pure value $0$ of the square. There is no exceptional element and no exceptional central value.

**Remark (the failure is structural).** The plain algebra has infinitely many roots of $-1$, the pure
unit quaternions, because a pure square can be a negative scalar; the antisymmetric block has none,
because a square is not a scalar at all but the zero element, whatever the coordinate of the alleged
root. The absence is the same fact as the totality of the roots of $0$.

## The Idempotents

**Theorem.** The idempotents of the block are only $0$:

$$
\tilde\pi\times\tilde\pi=\tilde\pi\iff\tilde\pi=0 .
$$

*Proof.* By alternation the left-hand side is $0$ for every $\tilde\pi$, so the equation is
$\tilde\pi=0$. The idempotents are the roots of $+1$ halved by the affine map
$\tilde\xi\mapsto\tfrac12(e_0+\tilde\xi)$ of the common apparatus; the map is never hit, the root set
of $+1$ being empty, and $0$, which is not a root of $+1$, is the degenerate idempotent.

## The Degeneracy of the Three Classes

**Proposition.** The three root classes of the block collapse onto two: the class of $0$, of real
dimension four, and the empty class shared by $-1$ and $+1$. The only nondegenerate class is the root
set of $0$, and it is the **maximum possible**, the whole punctured space; the other two are the
**minimum possible**, empty.

*Proof.* The root set of $0$ is $\mathbb{H}\setminus\{0\}$ by the preceding theorem, of real dimension
four; the root sets of $\pm1$ are empty. No other central value gives anything new: for
$\lambda\neq0$ the equation is $0=\lambda e_0$, impossible, and for $\lambda=0$ it is universal.

**Remark (what the degeneracy says).** The three central values are carried by the block into the two
extremes, and the passage is blind to the element: **the specification of the root is by the target
value alone**, the value $0$ accepting every nonzero element and every other value accepting none.
This is the opposite of the plain or the quaternionic block, where the roots of a central value form
a sphere or a pair and degenerate only on a lower-dimensional family.

## The Comparison with the Other Five Structures

On the box of elements with coordinates in $\{-1,0,1\}$ the six products give the following root
counts, and the spherical families are indicated in the continuous reading.

| product | roots of $-1$ | roots of $0$ | roots of $+1$ | idempotents |
|---|---|---|---|---|
| GPA, $\tilde p\tilde q$ | the pure unit quaternions | none | $\pm e_0$ | $\{0,e_0\}$ |
| SPA, $\tilde p\bullet\tilde q$ | the pure unit quaternions | none | $\pm e_0$ | $\{0,e_0\}$ |
| APA, $\tilde p\times\tilde q$ | none | the punctured space | none | $\{0\}$ |
| GQA, $\tilde p^{\natural}\tilde q$ | none | none | the unit sphere | $\{0,e_0\}$ |
| SQA, $\tilde p^{\natural}\tilde q$ symmetrised | none | none | the unit sphere | $\{0,e_0\}$ |
| AQA, $\tilde p\diamond\tilde q$ | none | the punctured space | none | $\{0\}$ |

**Remark (the pairing of the blocks).** The two **general** products and their symmetric halves share
their root pattern, and the two **antisymmetric** halves share theirs: the splitting into symmetric and
antisymmetric parts is what decides the root theory, not the choice of the parent. The block is one of
the two members of the degenerate antisymmetric family, the other being
*Introduction to the Antisymmetric Quaternionic Algebra of Quaternions*, below this article in this
category.
eight-dimensional complex analogue; the comparison is *Square Roots of Minus One, Zero and Plus One in

## Summary

The antisymmetric plain block forces its whole root theory from one fact: the operation is
alternating, so $\tilde\xi\times\tilde\xi=0$ for every element and the three central equations
$\tilde\xi\times\tilde\xi=\lambda e_0$ reduce to $0=\lambda e_0$. Hence the block has no root of $-1$
and no root of $+1$, and its roots of $0$ are every nonzero element, the punctured four-dimensional
space, which is at once the square-zero set and the zero-divisor set. The idempotents are only $0$,
the halved roots of $+1$ being an empty class. The three root classes collapse onto the two extremes,
the empty class and the total punctured one, and the degeneracy is shared with the antisymmetric
quaternionic block, while the general and symmetric blocks have spheres or pairs.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\xi\times\tilde\xi=\lambda e_0$ | the root equation of the block |
| $\{\tilde\xi\times\tilde\xi=-e_0\}=\varnothing$ | no imaginary unit |
| $\{\tilde\xi\times\tilde\xi=0\}=\mathbb{H}\setminus\{0\}$ | the roots of $0$, the punctured space |
| $\{\tilde\xi\times\tilde\xi=+e_0\}=\varnothing$ | no involution |
| $\{0\}$ | the idempotents, the halved roots of $+1$ |

## Further Reading

- *Introduction to the Antisymmetric Plain Algebra of Quaternions*, for the operation and the vanishing of the square.
- *Zero Divisors of the Antisymmetric Plain Algebra*, below this article in this category, for the identity of the root set of $0$ with the zero-divisor set.
- *The Specificities of the Antisymmetric Plain Algebra*, below this article in this category, for the folding of the idempotents and of the nilpotents.
- *Introduction to the Antisymmetric Quaternionic Algebra of Quaternions*, below this article in this category, for the companion degenerate block.
- *Definitions for the Study of the 6 Algebraic Structures*, for the general notion of a root of a central value and the halving construction of the idempotents.
