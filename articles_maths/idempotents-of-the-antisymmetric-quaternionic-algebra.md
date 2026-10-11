# __Idempotents of the Antisymmetric Quaternionic Algebra__

## Introduction

The idempotent is defined by an equation in which the product occurs, so it is a class of the
product and not of the space (*Definitions for the Study of the 12 Algebraic Structures*,
§*The Idempotent, the Projection and the Peirce Decomposition*). The block of this article is
the antisymmetric quaternionic multiplication
$$
\tilde P\diamond\tilde Q=\tfrac12\bigl(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P\bigr)
=P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q ,
$$
which is alternating and without a unit (*Introduction to the Antisymmetric Quaternionic Algebra
of Biquaternions*). The article determines its idempotent set.

The answer is the origin alone. The block is alternating, so $\tilde\Pi\diamond\tilde\Pi=0$ for
every element, and the idempotent equation $\tilde\Pi\diamond\tilde\Pi=\tilde\Pi$ is therefore
the equation $0=\tilde\Pi$: **the origin is the only idempotent of the block**, and both
nontrivial idempotents and projections are absent. The absence is not the absence of a projector
in the operator sense: the element $e_0$, although it is not an idempotent of the block, has a
left multiplication that is a projector, the projection onto the vector subspace, and that
separation of the element from its operator is the subject of *The Specificities of the
Antisymmetric Quaternionic Algebra*, to which the last section points. There is no Peirce
decomposition, since the product is not associative and there are no nontrivial idempotents to
decompose against.

## The Notion and Its Product

**Definition (idempotent of a product).** Let $\star$ be a product on $\mathbb{B}$. An element
$\tilde\Pi$ is an **idempotent of $\star$** when
$$
\tilde\Pi\star\tilde\Pi=\tilde\Pi .
$$
The origin and, when the product is unital, the unit are the **trivial idempotents**; the others
are **nontrivial**.

**Definition (projection).** When the product is the multiplication of a $*$-algebra, an
idempotent $\tilde\Pi$ with $\tilde\Pi^{*}=\tilde\Pi$ is a **projection**.

Throughout this article the product is the **antisymmetric quaternionic multiplication**
$\diamond$, and unqualified, *idempotent* means an idempotent of the block. The idempotent set
of the general plain product, to which the block is compared, is *Idempotents of the General
Plain Algebra*; the idempotents of the parent quaternionic product are *Idempotents of the
Quaternionic Product*.

## The Idempotent Equation

**Theorem (the only idempotent).** The identity element $e_0$ is not an idempotent of the
block, the origin is, and the idempotent set of the block is the origin alone:
$$
\{\tilde\Pi:\tilde\Pi\diamond\tilde\Pi=\tilde\Pi\}=\{0\}.
$$

*Proof.* The block is alternating, so $\tilde\Pi\diamond\tilde\Pi=0$ for every element
$\tilde\Pi$, by *Introduction to the Antisymmetric Quaternionic Algebra of Biquaternions*. The
idempotent equation reads $0=\tilde\Pi$, whose only solution is the origin. The element $e_0$ is
excluded because $e_0\diamond e_0=0\neq e_0$.

The idempotent equation is therefore the equation of the origin, and the idempotent set is the
smallest it can be. The absence is the mirror image of the absence of a unit: the block removes
the scalar part of the parent product, the idempotent equation of the parent reads
$\tilde\Pi^{\natural}\tilde\Pi=\tilde\Pi$ and has the two trivial solutions and a family besides,
and the removal of the scalar part leaves only the origin.

## Projections and the Peirce Decomposition

**Corollary (no nontrivial idempotent and no projection).** The block has no nontrivial
idempotent and no projection. Equivalently, the idempotent set is the trivial idempotent of
origin alone, and the additional Hermitian condition $\tilde\Pi^{*}=\tilde\Pi$ that a projection
imposes on an idempotent has no nonzero solution.

*Proof.* A nontrivial idempotent is an idempotent other than the origin and the unit; the block
has no unit, and its only idempotent is the origin, so there is no nontrivial idempotent. A
projection is an idempotent, so a projection is the origin, and the origin satisfies the
condition $\tilde\Pi^{*}=\tilde\Pi$; hence the projection set is the origin alone.

**Corollary (no Peirce decomposition).** The Peirce decomposition of the block does not exist:
the construction uses a nontrivial idempotent and the associativity of the product, and the
block has neither.

*Proof.* The Peirce decomposition is indexed by a pair $(\tilde\Pi,e-\tilde\Pi)$ of complementary
idempotents of an associative unital product (*Definitions for the Study of the 12 Algebraic
Structures*, §*The Idempotent, the Projection and the Peirce Decomposition*); the block has no
unit, no nontrivial idempotent and no associativity, so the three ingredients of the construction
are all absent.

The absence of the Peirce decomposition is not a defect of the block alone. Of the twelve
structures only the general plain product carries the Peirce decomposition as a theorem of its own
idempotents, and the symmetric and antisymmetric halves fail it for their own reasons; the general
quaternionic product is the border case, where the projectors exist but are indexed by the plain
idempotents. The classification of the twelve by the projectors they carry, and the exact sense in
which the block retains a projector, are *The Specificities of the Antisymmetric Quaternionic
Algebra*.

## The Relation to the Roots of Plus One

**Remark (the scaled root).** For the general plain product the idempotents are the roots of
$+1$ read in the scaled sense, the plain product carrying the family
$\tfrac12(e_0+\tilde\Xi i)$ over the roots $\tilde\Xi$ of $-1$ (*Definitions for the Study of the 12
Algebraic Structures*, §*The Idempotent, the Projection and the Peirce Decomposition* and
§*Powers, the Square and the Roots*). The block has no root of $+1$
(*Square Roots of Minus One, Zero and Plus One in the Antisymmetric Quaternionic Algebra*), and
its idempotent set is the origin alone; the two collapses have one cause, and neither produces a
decomposition.

The common cause is not an accident: the idempotent equation and the root of $+1$ equation are
both read from the square, and the square of the block vanishes identically. In the block the two
equations collapse together, and they collapse differently: the idempotent equation
$\tilde\Pi\diamond\tilde\Pi=\tilde\Pi$ becomes $0=\tilde\Pi$ and is solved by the origin alone,
while the root of $+1$ equation $\tilde\Pi\diamond\tilde\Pi=e_0$ becomes $0=e_0$ and has no
solution at all.

## The Element $e_0$ and Its Operator

**Remark (an element that is not an idempotent but has a projector).** The element $e_0$ is not
an idempotent of the block, since $e_0\diamond e_0=0$; it is nevertheless the element whose left
multiplication is a projector, because
$$
L_{e_0}\tilde X=e_0\diamond\tilde X=\mathbf X , \qquad L_{e_0}^{2}=L_{e_0} ,
$$
the projection onto the vector subspace along the centre. The element and its operator are two
different objects, and the block separates them: the element $e_0$ is not idempotent, while the
operator $L_{e_0}$ is idempotent. The separation, the exact projector class of the block and the
comparison with the other eleven are *The Specificities of the Antisymmetric Quaternionic
Algebra*; what is recorded here is only that the idempotent equation of the block and the
projector equation of its operators are not the same equation.

## Summary

For the antisymmetric quaternionic multiplication $\tilde P\diamond\tilde Q=P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q$ the square of every element is zero, so the idempotent
equation $\tilde\Pi\diamond\tilde\Pi=\tilde\Pi$ is the equation $0=\tilde\Pi$ and the idempotent
set is the origin alone. The element $e_0$ is not an idempotent of the block; the block has no
nontrivial idempotent and no projection; and the Peirce decomposition does not exist, its three
ingredients — a unit, a nontrivial idempotent and associativity — being all absent. The absence
agrees with the absence of roots of $+1$, the two being the same vanishing square read twice.
The element $e_0$, although not idempotent, has an idempotent left multiplication, the projection
onto the vector subspace; the element and its operator are distinct objects, and their
separation is the subject of the specificities of the block.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\diamond\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P)=P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q$ | the antisymmetric quaternionic multiplication, the operation $\mathrm{AQA}$ |
| $\tilde\Pi\diamond\tilde\Pi=0$ | the reduction, the square of every element |
| $\{0\}$ | the idempotent set of the block, the origin alone |
| $e_0$ | the algebra unit, not an idempotent of the block, with $L_{e_0}$ the projection onto the vector subspace |
| $\mathrm{Vect}(\mathbb{B})$ | the image of $L_{e_0}$, the vector subspace |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the idempotent, the projection and the Peirce decomposition of a general product, and for the relativity of the definitions
- *Introduction to the Antisymmetric Quaternionic Algebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-quaternionic-algebra-of-biquaternions.md`), for the operation, its alternation and its table
- *The Specificities of the Antisymmetric Quaternionic Algebra* (`articles_maths/the-specificities-of-the-antisymmetric-quaternionic-algebra.md`), for the projector class of the block and for the element $e_0$ whose left multiplication is a projector
- *Square Roots of Minus One, Zero and Plus One in the Antisymmetric Quaternionic Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-antisymmetric-quaternionic-algebra.md`), for the absence of roots of $+1$, which is the same vanishing square
- *Idempotents of the General Plain Algebra* (`articles_maths/idempotents-of-the-general-plain-algebra.md`), for the idempotent set of the plain product, against which the origin alone is read
