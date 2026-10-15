# __Idempotents of the Antisymmetric Quaternionic Algebra__

## Introduction

The idempotent is defined by an equation in which the product occurs, so it is a class of the product and not of the space (*Definitions for the Study of the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*). The block of this article is the antisymmetric quaternionic multiplication

$$
\tilde p\diamond\tilde q=\tfrac12\bigl(\tilde p^{\natural}\tilde q-\tilde q^{\natural}\tilde p\bigr)
=p_0\vec q-q_0\vec p-\vec p\times\vec q ,
$$

which is alternating and without a unit (*Introduction to the Antisymmetric Quaternionic Algebra of Quaternions*). The article determines its idempotent set.

The answer is the origin alone. The block is alternating, so $\tilde\Pi\diamond\tilde\Pi=0$ for every element, and the idempotent equation $\tilde\Pi\diamond\tilde\Pi=\tilde\Pi$ is therefore the equation $0=\tilde\Pi$: **the origin is the only idempotent of the block**, and both nontrivial idempotents and nontrivial projections are absent. The absence is not the absence of a projector in the operator sense: the element $e_0$, although it is not an idempotent of the block, has a left multiplication that is a projector, the projection onto the vector subspace, and that separation of the element from its operator is the subject of *The Specificities of the Antisymmetric Quaternionic Algebra*, to which the last section points. There is no Peirce decomposition, since the product is not associative and there are no nontrivial idempotents to decompose against.

**Conventions.** Throughout, $\tilde p=p_0e_0+\vec p$, $\tilde q=q_0e_0+\vec q$ and $\tilde\Pi=\pi_0e_0+\vec\pi$ name elements of $\mathbb{H}$ with real coefficients, $(\vec p,\vec q)$ is the dot product and $\vec p\times\vec q$ the cross product of the vector parts, and $\tilde q^{\natural}=q_0e_0-\vec q$ is the quaternion conjugation; the bar is the identity and the star coincides with the natural conjugation, so no bare bar is written on an element of this block, and the only conjugate of an element is its natural conjugate. The operation is written $\diamond$ and never $\wedge^{\natural}$ outside a citation, and unqualified, *idempotent* means an idempotent of the block. The centre is $\mathbb{R}_{\mathbb{H}}=\mathbb{R}e_0$, and $\mathrm{Vect}(\mathbb{H})$ is the vector subspace.

**Boundaries.** The operation and its alternation are *Introduction to the Antisymmetric Quaternionic Algebra of Quaternions*; the definition of the idempotent is *Definitions for the Study of the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, and the projection and the Peirce decomposition of an associative unital algebra are *Unital Algebras*, §*Idempotents and the Peirce Decomposition*. The idempotents of the general plain product, to which the block is compared, are *Idempotents of the General Plain Algebra*; the idempotent sets of the six structures are *Idempotents in the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*; the roots of $+1$ are *Square Roots of Minus One, Zero and Plus One in the Antisymmetric Quaternionic Algebra*; and the projector of the block is *The Specificities of the Antisymmetric Quaternionic Algebra*.

## The Notion and Its Product

**Definition (idempotent of a product).** Let $\star$ be a product on $\mathbb{H}$. An element $\tilde\Pi$ is an **idempotent of $\star$** when

$$
\tilde\Pi\star\tilde\Pi=\tilde\Pi .
$$

The origin is the **trivial idempotent**, and every other idempotent, the unit when the product is unital included, is **nontrivial**.

**Definition (projection).** When the product is the multiplication of a $*$-algebra, an idempotent $\tilde\Pi$ with $\tilde\Pi^{*}=\tilde\Pi$ is a **projection**. Over $\mathbb{R}$ the bar is the identity and the star is the natural conjugation, so the condition reads $\tilde\Pi^{\natural}=\tilde\Pi$.

Throughout this article the product is the **antisymmetric quaternionic multiplication** $\diamond$, and unqualified, *idempotent* means an idempotent of the block. The idempotent set of the general plain product, to which the block is compared, is *Idempotents of the General Plain Algebra*; the idempotent sets of the six structures of the real chapter are *Idempotents in the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*.

## The Idempotent Equation

**Theorem (the only idempotent).** The identity element $e_0$ is not an idempotent of the block, the origin is, and the idempotent set of the block is the origin alone:

$$
\{\tilde\Pi:\tilde\Pi\diamond\tilde\Pi=\tilde\Pi\}=\{0\}.
$$

*Proof.* The block is alternating, so $\tilde\Pi\diamond\tilde\Pi=0$ for every element $\tilde\Pi$, by *Introduction to the Antisymmetric Quaternionic Algebra of Quaternions*. The idempotent equation reads $0=\tilde\Pi$, whose only solution is the origin. The element $e_0$ is excluded because $e_0\diamond e_0=0\neq e_0$.

The idempotent equation is therefore the equation of the origin, and the idempotent set is the smallest it can be. The absence is the mirror image of the absence of a unit: the block removes the scalar part of the parent product, the idempotent equation of the parent reads $\tilde\Pi^{\natural}\tilde\Pi=\tilde\Pi$ and has the two solutions $0$ and $e_0$, and the removal of the scalar part leaves only the origin. The contrast with the four structures of the real chapter that carry the two-point set $\{0,e_0\}$ is the same contrast: the square of the block vanishes where theirs returns $e_0$ at the unit, so it cannot solve the idempotent equation at $e_0$.

## Projections and the Peirce Decomposition

**Corollary (no nontrivial idempotent and no nontrivial projection).** The block has no nontrivial idempotent and no nontrivial projection. Equivalently, the idempotent set is the trivial idempotent of origin alone, and the additional Hermitian condition $\tilde\Pi^{\natural}=\tilde\Pi$ that a projection imposes on an idempotent has no nonzero solution.

*Proof.* A nontrivial idempotent is an idempotent other than the origin; the block has only the origin as idempotent, so there is no nontrivial idempotent. A projection is an idempotent, so a projection is the origin, which satisfies the condition $\tilde\Pi^{\natural}=\tilde\Pi$; hence the projection set is the origin alone and there is no nontrivial projection. The element $e_0$ is conjugate to itself and is not an idempotent, so it is not a projection.

**Corollary (no Peirce decomposition).** The Peirce decomposition of the block does not exist: the construction uses a nontrivial idempotent and the associativity of the product, and the block has neither.

*Proof.* The Peirce decomposition is indexed by a pair $(\tilde\Pi,e-\tilde\Pi)$ of complementary idempotents of an associative unital product (*Unital Algebras*, §*Idempotents and the Peirce Decomposition*); the block has no unit, no nontrivial idempotent and no associativity, so the three ingredients of the construction are all absent.

The absence of the Peirce decomposition is not a defect of the block alone. Of the six structures only the general plain product is associative and unital, and only there does the Peirce decomposition follow from the idempotents; the antisymmetric structures fail it because they have no unit and no nontrivial idempotent, and the symmetric ones because they are not associative. The classification of the six by the projectors they carry, and the exact sense in which the block retains a projector, are *The Specificities of the Antisymmetric Quaternionic Algebra*.

## The Relation to the Roots of Plus One

**Remark (the scaled root).** For the general plain product the idempotents are the origin and the unit $e_0$, and the unit is its root of $+1$; a nontrivial idempotent other than the unit would be built as $\tfrac12(e_0+\vec u)$ from a pure root $\vec u$ of $+e_0$, and over $\mathbb{R}$ there is no nonzero pure element with square $+e_0$. The block has no root of $+1$ at all (*Square Roots of Minus One, Zero and Plus One in the Antisymmetric Quaternionic Algebra*), and its idempotent set is the origin alone; the two collapses have one cause, and neither produces a decomposition.

The common cause is not an accident: the idempotent equation and the root of $+1$ equation are both read from the square, and the square of the block vanishes identically. In the block the two equations collapse together, and they collapse differently: the idempotent equation $\tilde\Pi\diamond\tilde\Pi=\tilde\Pi$ becomes $0=\tilde\Pi$ and is solved by the origin alone, while the root of $+1$ equation $\tilde\Pi\diamond\tilde\Pi=e_0$ becomes $0=e_0$ and has no solution at all.

## The Element $e_0$ and Its Operator

**Remark (an element that is not an idempotent but has a projector).** The element $e_0$ is not an idempotent of the block, since $e_0\diamond e_0=0$; it is nevertheless the element whose left multiplication is a projector, because

$$
L_{e_0}\tilde x=e_0\diamond\tilde x=\vec x , \qquad L_{e_0}^{2}=L_{e_0},
$$

the projection onto the vector subspace along the centre. The right multiplication is the negative of that projection, $\tilde x\diamond e_0=-\vec x$, and it is a projector as well up to the sign. The element and its operator are two different objects, and the block separates them: the element $e_0$ is not idempotent, while the operator $L_{e_0}$ is idempotent. The separation, the exact projector class of the block and the comparison with the other five are *The Specificities of the Antisymmetric Quaternionic Algebra*; what is recorded here is only that the idempotent equation of the block and the projector equation of its operators are not the same equation.

## Summary

For the antisymmetric quaternionic multiplication $\tilde p\diamond\tilde q=p_0\vec q-q_0\vec p-\vec p\times\vec q$ the square of every element is zero, so the idempotent equation $\tilde\Pi\diamond\tilde\Pi=\tilde\Pi$ is the equation $0=\tilde\Pi$ and the idempotent set is the origin alone. The element $e_0$ is not an idempotent of the block; the block has no nontrivial idempotent and no nontrivial projection; and the Peirce decomposition does not exist, its three ingredients — a unit, a nontrivial idempotent and associativity — being all absent. The absence agrees with the absence of roots of $+1$, the two being the same vanishing square read twice. The element $e_0$, although not idempotent, has an idempotent left multiplication, the projection onto the vector subspace; the element and its operator are distinct objects, and their separation is the subject of the specificities of the block. Compared with the four structures of the real chapter whose idempotent set is $\{0,e_0\}$, the block is the one that loses the unit point, its square vanishing where theirs returns $e_0$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde p\diamond\tilde q=\tfrac12(\tilde p^{\natural}\tilde q-\tilde q^{\natural}\tilde p)=p_0\vec q-q_0\vec p-\vec p\times\vec q$ | the antisymmetric quaternionic multiplication, the operation $\mathrm{AQA}$ |
| $\tilde\Pi\diamond\tilde\Pi=0$ | the reduction, the square of every element |
| $\{0\}$ | the idempotent set of the block, the origin alone |
| $e_0$ | the algebra unit, not an idempotent of the block, with $L_{e_0}$ the projection onto the vector subspace |
| $\mathrm{Vect}(\mathbb{H})$ | the image of $L_{e_0}$, the vector subspace |
| $\{0,e_0\}$ | the idempotent set of the four structures of the plain and quaternionic families |

## Further Reading

- *Definitions for the Study of the Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-quaternion-r-space.md`), for the idempotent and its place in the element vocabulary.
- *Unital Algebras* (`articles_maths/unital-algebras.md`), §*Idempotents and the Peirce Decomposition*, for the orthogonal, complete and primitive families, the projection and the four Peirce spaces of an associative unital algebra.
- *Introduction to the Antisymmetric Quaternionic Algebra of Quaternions* (`articles_maths/introduction-to-the-antisymmetric-quaternionic-algebra-of-quaternions.md`), for the operation and its alternation.
- *Idempotents in the Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/idempotents-in-the-algebraic-structures-over-the-quaternion-r-space.md`), for the idempotent sets of the six structures of the real chapter.
- *Idempotents of the General Plain Algebra* (`articles_maths/idempotents-of-the-general-plain-algebra-of-quaternions.md`), above this article in this category, for the set $\{0,e_0\}$ to which the block is the counterpoint.
- *Square Roots of Minus One, Zero and Plus One in the Antisymmetric Quaternionic Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-antisymmetric-quaternionic-algebra-of-quaternions.md`), for the absence of a root of $+1$ in the block.
- *The Specificities of the Antisymmetric Quaternionic Algebra* (`articles_maths/the-specificities-of-the-antisymmetric-quaternionic-algebra-of-quaternions.md`), for the projector $L_{e_0}$ and the separation of the element from its operator.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, Colloquium Publications 39, 1968), for idempotents and the Peirce decomposition of an algebra.
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for idempotents, projections and the Peirce decomposition of an associative algebra.
