# __Idempotents of the General Plain Algebra__

## Introduction

The algebra article defined the quaternion algebra $\mathbb{H}$, its natural conjugation and its
remarkable real subspaces. This article treats the **idempotents** of $\mathbb{H}$ — the elements
satisfying $\tilde\Pi^2 = \tilde\Pi$ — and the projection and direct sum structure they carry.

Idempotents are the algebraic form of a projection. In the complexified block they do four separate
jobs at once: they give the direct sum decompositions of the algebra into left ideals, they classify
the non-pure zero divisors, they are in bijection with the roots of $-1$, and they drive the Peirce
decomposition. Over $\mathbb{R}$ every one of these jobs collapses, because the only idempotents are
$0$ and the unit $e_0$: there is no nontrivial decomposition, no non-pure zero divisor to attach to an
idempotent, and no root of $-1$ to be in bijection with. The interest of the article is exactly this
collapse, and it is proved from the division property alone.

The article is one of the last entries of the *Common Theory* of the block, after *Square Roots of a
General Element in the General Plain Algebra* and before *Nilpotents of the General Plain Algebra* and
*The Specificities of the General Plain Algebra*, all of them neighbours in this category. Its proofs
use only the algebra article and the division property of *Norm and Invertibility in the General Plain
Algebra*, above this article in this category; the relations to the zero divisors, to the nilpotents
and to the roots are pointers, and no claim of those articles is re-derived here.

## Conventions

The algebra is $\mathbb{H}$, the four-dimensional real algebra with basis $e_0 = 1, e_1, e_2, e_3$,
$e_k^2 = -e_0$ and $e_1e_2 = e_3 = -e_2e_1$. A general element is $\tilde q = q_0e_0 + \mathbf q$ with
$q_0 \in \mathbb{R}$ and $\mathbf q = q_1e_1 + q_2e_2 + q_3e_3$; the scalar part is
$q_0 = \mathrm{Sc}(\tilde q)$ and the vector part is $\mathbf q$. The natural conjugation is
$\tilde q^{\natural} = q_0e_0 - \mathbf q$, and the quaternion norm is
$N(\tilde q) = \tilde q\tilde q^{\natural} = q_0^2 + |\mathbf q|^2$, positive definite over
$\mathbb{R}$ by *Norm and Invertibility in the General Plain Algebra*, above this article in this
category. Every nonzero element is invertible, $\tilde q^{-1} = \tilde q^{\natural}/N(\tilde q)$, so
there is no zero divisor: $\tilde p\tilde q = 0$ forces $\tilde p = 0$ or $\tilde q = 0$. The centre
is the scalar line $\mathbb{R}e_0$ and the vector subspace is $\mathrm{Vect}(\mathbb{H})$.

The plain product throughout is the general plain bilinear product $\tilde p\tilde q$, the
multiplication of the algebra — the only one of the six products of *The 6 Products of the Quaternion
Real Space* that is associative with a two-sided unit, and the one the equation
$\tilde\Pi^2 = \tilde\Pi$ presupposes. An idempotent is written $\tilde\Pi$ and a generic element
$\tilde q$. The general definition of an idempotent is *Definitions for the Study of the 6 Algebraic
Structures*, §*The Element Vocabulary*; the orthogonal, complete and primitive families and the
Peirce decomposition are defined in the body of this article, and their general associative form is
*Unital Algebras*, §*Idempotents and the Peirce Decomposition*. The six structures the plain product
belongs to are *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*.

## Definition

An element $\tilde\Pi$ of $\mathbb{H}$ is an **idempotent of the general plain algebra** when

$$
\tilde\Pi^2 = \tilde\Pi ,
$$

the square being read in the general plain bilinear product. The equation names a product, so the
notion is relative to it; the general definition of an idempotent is *Definitions for the Study of the
6 Algebraic Structures*, §*The Element Vocabulary*, and the orthogonal, complete and primitive
families are defined in §*Orthogonal and Complete Families* below. Throughout this article the product
is the general plain bilinear product, and another product is named where it is meant.

Idempotents encode direct summands of the regular module,
$\mathbb{H} = \mathbb{H}\tilde\Pi \oplus \mathbb{H}(e_0 - \tilde\Pi)$ on the left and
$\mathbb{H} = \tilde\Pi\mathbb{H} \oplus (e_0 - \tilde\Pi)\mathbb{H}$ on the right, and every such
decomposition arises from an idempotent. A primitive idempotent — one that is not a sum of two
nonzero orthogonal idempotents — generates a minimal left ideal. Over $\mathbb{R}$ the possibilities
are as small as an algebra permits, and the sections below compute them.

## The Idempotents

**Theorem (the idempotents of the plain product).** The idempotents of the general plain product are
exactly $0$ and $e_0$.

**Proof.** If $\tilde\Pi^2 = \tilde\Pi$ then $\tilde\Pi(\tilde\Pi - e_0) = \tilde\Pi^2 - \tilde\Pi = 0$.
By the absence of zero divisors (*Zero Divisors of the General Plain Algebra*, above this article in
this category), one of the two factors vanishes: either $\tilde\Pi = 0$ or $\tilde\Pi - e_0 = 0$,
that is $\tilde\Pi = e_0$. Both elements are idempotent, $0^2 = 0$ and $e_0^2 = e_0$.

The theorem is the extreme case of the classification of the complexified block, where every
idempotent is $\tfrac12 e_0 \pm \tfrac12\tilde\Xi i$ over a root $\tilde\Xi$ of $-1$; over
$\mathbb{R}$ the central unit $i$ is not available, the family is empty, and only the two trivial
idempotents remain.

**Remark (the two idempotents are as different as possible).** The idempotent $0$ is not a unit, and
it is not a zero divisor either, a zero divisor being required to be nonzero; the idempotent $e_0$ is
the unit of the algebra. Neither is a zero divisor, and no other element of the algebra is idempotent.
The complexified block places a whole manifold of nontrivial idempotents between the two, and the
manifold is what disappears.

## Orthogonal and Complete Families

An **orthogonal family** is a family of idempotents with $\tilde\Pi_i\tilde\Pi_j = 0$ for
$i \neq j$; it is **complete** when the sum of its members is $e_0$. A nonzero idempotent is
**primitive** when it is not the sum of two nonzero orthogonal idempotents.

**Theorem (the families).** In the plain product:

- every orthogonal family contains at most one nonzero idempotent;
- the only complete orthogonal family of nonzero idempotents is the singleton $\{e_0\}$;
- the unit $e_0$ is the only primitive idempotent, and $0$ is not primitive.

**Proof.** By the theorem above every idempotent is $0$ or $e_0$. Two distinct nonzero idempotents
would both be $e_0$, which is not orthogonal to itself, $e_0e_0 = e_0 \neq 0$; so no orthogonal
family contains two nonzero members. A complete orthogonal family of nonzero idempotents sums to
$e_0$, and since it contains at most one nonzero idempotent it is either empty, with sum
$0 \neq e_0$, or the singleton $\{e_0\}$. For primitivity, $e_0$ is not a sum of two nonzero
orthogonal idempotents because there are no two distinct nonzero idempotents to sum; and $0$ is not
primitive under the convention that a primitive idempotent is nonzero.

**Corollary (no nontrivial decomposition).** The only decompositions of the algebra carried by an
idempotent are the two trivial ones: for $\tilde\Pi = e_0$,

$$
\mathbb{H} = e_0\mathbb{H} \oplus (e_0 - e_0)\mathbb{H} = \mathbb{H} \oplus \{0\} ,
$$

and for $\tilde\Pi = 0$,

$$
\mathbb{H} = 0\cdot\mathbb{H} \oplus (e_0 - 0)\mathbb{H} = \{0\} \oplus \mathbb{H} .
$$

There is no proper nonzero direct summand of the regular module in the plain product.

## The Peirce Decomposition

For an idempotent $\tilde\Pi$ the **Peirce decomposition** is the direct sum

$$
\mathbb{H} = \tilde\Pi\mathbb{H}\tilde\Pi \;\oplus\; \tilde\Pi\mathbb{H}(e_0 - \tilde\Pi)
\;\oplus\; (e_0 - \tilde\Pi)\mathbb{H}\tilde\Pi \;\oplus\; (e_0 - \tilde\Pi)\mathbb{H}(e_0 - \tilde\Pi),
$$

the four **Peirce spaces** of the idempotent.

**Theorem (the Peirce decomposition is trivial).** For each of the two idempotents of the plain
product one Peirce space is the whole algebra and the other three are $\{0\}$:

$$
\tilde\Pi = e_0 : \quad \mathbb{H} = \mathbb{H} \oplus \{0\} \oplus \{0\} \oplus \{0\} ,
\qquad
\tilde\Pi = 0 : \quad \mathbb{H} = \{0\} \oplus \{0\} \oplus \{0\} \oplus \mathbb{H} .
$$

**Proof.** For $\tilde\Pi = e_0$ the four spaces are $e_0\mathbb{H}e_0 = \mathbb{H}$,
$e_0\mathbb{H}(e_0 - e_0) = 0$, $(e_0 - e_0)\mathbb{H}e_0 = 0$ and
$(e_0 - e_0)\mathbb{H}(e_0 - e_0) = 0$. For $\tilde\Pi = 0$ the same computation exchanges the outer
factors.

So the Peirce decomposition of the plain product is the trivial one, with Peirce spaces $\mathbb{H}$
and $\{0\}$ and no off-diagonal space. In particular the two off-diagonal Peirce units, which in the
complexified block generate the minimal ideals, do not exist over $\mathbb{R}$: such a unit satisfies
$\tilde\Upsilon^2 = 0$ with $\tilde\Upsilon \neq 0$, and there is none (*Nilpotents of the General
Plain Algebra*, below this article in this category).

## Idempotents and the Zero Divisors

A nontrivial idempotent is always a zero divisor, since

$$
\tilde\Pi(e_0 - \tilde\Pi) = \tilde\Pi - \tilde\Pi^2 = 0
$$

with both factors nonzero unless $\tilde\Pi$ is $0$ or $e_0$. Conversely, in the complexified block
every non-pure zero divisor is a complex multiple of a nontrivial idempotent,
$\tilde Q = 2Q_0\tilde\Pi$.

Over $\mathbb{R}$ both statements are vacuous, and the reason is one and the same: there are no
nontrivial idempotents and no zero divisors. The only idempotents are $0$ and $e_0$; the element $0$
is not a zero divisor by the requirement that a divisor be nonzero, and $e_0$ is a unit. So **no
idempotent of the plain product is a zero divisor**, which is the exact opposite of the complexified
reading, where the nontrivial idempotents sit inside the zero-divisor cone as its non-pure family. The
zero-divisor set is empty (*Zero Divisors of the General Plain Algebra*, above this article in this
category), and the idempotent reading of it has nothing to describe.

## Idempotents and the Roots of the Central Values

The idempotent equation is not a central-value equation, but the affine change of variable
$\tilde\Xi = 2\tilde\Pi - e_0$ carries the one into the other: $\tilde\Pi^2 = \tilde\Pi$ holds exactly
when $\tilde\Xi^2 = e_0$, since
$\tilde\Xi^2 = 4\tilde\Pi^2 - 4\tilde\Pi + e_0 = e_0$. The named central values are the three
$c = -1, 0, +1$ of *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*; the
two read here are $c = +1$, whose roots the affine map ties to the idempotents, and $c = -1$, whose
roots are the unit sphere of the vector subspace.

**Proposition (roots of $+1$).** The solutions of $\tilde x^2 = e_0$ are exactly $\pm e_0$.

**Proof.** $\tilde x^2 - e_0 = (\tilde x - e_0)(\tilde x + e_0) = 0$, and the absence of zero divisors
forces $\tilde x = e_0$ or $\tilde x = -e_0$; both square to $e_0$.

So the idempotents and the roots of $+1$ are different sets, carried one to the other by the affine
map: the first is $\{0, e_0\}$ and the second is $\{e_0, -e_0\}$, with $\tilde\Xi = 2\tilde\Pi - e_0$
sending $e_0$ to $e_0$ and $0$ to $-e_0$. They meet in the unit $e_0$ alone, and $-e_0$ is the one
root of $+1$ that is not idempotent, since $(-e_0)^2 = e_0 \neq -e_0$. The roots of
$-1$, the unit sphere of the vector subspace, have no counterpart in the idempotent set over
$\mathbb{R}$: the bijection $\tilde\Xi \mapsto \tfrac12(e_0 + \tilde\Xi i)$ of the complexified block
needs the central unit $i$, and without it the roots of $-1$ and the idempotents are two disjoint
families. The root sets of the three central values are *Square Roots of Minus One, Zero and Plus One
in the General Plain Algebra*, above this article in this category.

## Idempotents and the Units

**Proposition.** Every idempotent of the plain product is either the zero element or a unit.

**Proof.** The idempotents are $0$ and $e_0$; the element $e_0$ is the unit and a nonzero element,
hence invertible with $e_0^{-1} = e_0$.

This is a reading of the division property: an idempotent that is neither $0$ nor a unit would be a
non-invertible nonzero element, and there is none. In the complexified block the same reading fails,
the nontrivial idempotents being non-invertible and of vanishing norm.

## Summary

An idempotent of the quaternion algebra is an element $\tilde\Pi$ with $\tilde\Pi^2 = \tilde\Pi$.
Over the general plain product the idempotents are exactly $0$ and the unit $e_0$: the equation gives
$\tilde\Pi(\tilde\Pi - e_0) = 0$, and the absence of zero divisors leaves only the two trivial
solutions. There is no nontrivial idempotent, no orthogonal family of two nonzero idempotents, no
complete orthogonal family but the singleton $\{e_0\}$, no primitive idempotent but $e_0$, and no
nontrivial direct sum decomposition of the algebra; the Peirce decomposition is the trivial one, with
Peirce spaces $\mathbb{H}$ and $\{0\}$ and no off-diagonal unit. No idempotent is a zero divisor, since
$0$ is excluded from the zero divisors and $e_0$ is a unit, and the idempotents meet the roots of $+1$
in the unit $e_0$ alone.

This is the collapse of the complexified block, where the idempotents form a real four-dimensional
manifold, are in bijection with the roots of $-1$, classify the non-pure zero divisors, and generate
the minimal left ideals. The neighbouring classes are *Zero Divisors of the General Plain Algebra*,
above this article in this category, and *Nilpotents of the General Plain Algebra*, below it: the
zero-divisor set of the plain product is empty and the nilpotent class reduces to the origin.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Pi$ | Idempotent, $\tilde\Pi^2 = \tilde\Pi$ |
| $e_0$ | The unit and the only nonzero idempotent |
| $\tilde\Pi(e_0 - \tilde\Pi) = 0$ | Orthogonality of an idempotent to its complement |
| $\mathbb{H} = \tilde\Pi\mathbb{H} \oplus (e_0 - \tilde\Pi)\mathbb{H}$ | The direct sum decomposition carried by an idempotent |
| $\tilde\Pi\mathbb{H}\tilde\Pi$ etc. | The four Peirce spaces |
| $\tilde x^2 = e_0$ | Root equation of $+1$, with solutions $\pm e_0$ |
| $N(\tilde q) = q_0^2 + \lvert\mathbf q\rvert^2$ | Quaternion norm, positive definite |
| $\mathbb{R}e_0$, $\mathrm{Vect}(\mathbb{H})$ | Centre and vector subspace |

## Further Reading

- *Definitions for the Study of the 6 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-6-algebraic-structures.md`), §*The Element Vocabulary*, for the general definition of an idempotent.
- *Unital Algebras* (`articles_maths/unital-algebras.md`), §*Idempotents and the Peirce Decomposition*, for the orthogonal, complete and primitive families and the four Peirce spaces of an associative unital algebra.
- *Norm and Invertibility in the General Plain Algebra* (`articles_maths/norm-and-invertibility-in-the-general-plain-algebra-of-quaternions.md`), for the division property on which the classification rests.
- *Zero Divisors of the General Plain Algebra* (`articles_maths/zero-divisors-of-the-general-plain-algebra-of-quaternions.md`), above this article in this category, for the empty zero-divisor set and the two families of the complexified block.
- *Nilpotents of the General Plain Algebra* (`articles_maths/nilpotents-of-the-general-plain-algebra-of-quaternions.md`), below this article in this category, for the square-zero class, the off-diagonal Peirce units and the disjointness of the two classes.
- *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-general-plain-algebra-of-quaternions.md`), above this article in this category, for the root sets of the three central values.
- *Idempotents of the General Plain Algebra* (`articles_maths/idempotents-of-the-general-plain-algebra.md`), the complexified counterpart, for the idempotent manifold, the bijection with the roots of $-1$ and the minimal left ideals.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for idempotents, the Peirce decomposition and the structure of the regular module.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for idempotents, projections and their lifting in rings.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the quaternion algebra and its idempotents.
