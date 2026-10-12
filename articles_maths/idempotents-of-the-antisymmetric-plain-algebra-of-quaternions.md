# __Idempotents of the Antisymmetric Plain Algebra__

## Introduction

The idempotent is defined by an equation in which the product occurs, so it is a class of the
product and not of the space (*Definitions for the Study of the 6 Algebraic Structures*,
§*The Element Vocabulary*). The block of this article is the antisymmetric plain multiplication

$$
\tilde p\times\tilde q=\tfrac12\bigl(\tilde p\tilde q-\tilde q\tilde p\bigr)=\mathbf p\times\mathbf q,
$$

the cross product of the two vector parts, which is alternating (*Introduction to the Antisymmetric
Plain Algebra of Quaternions*). The article determines its idempotent set and states the
consequences of its being as small as possible.

The answer is the extreme absence. The idempotent equation of the block is
$\tilde\pi\times\tilde\pi=\tilde\pi$; its left side is zero for every element, and the equation
therefore reduces to $0=\tilde\pi$. **The block has one idempotent, the origin**, which is the
trivial idempotent of every product; it has **no nontrivial idempotent**, hence no orthogonal family,
no primitive idempotent and no projection, and no Peirce decomposition. The unit $e_0$ of the
ambient algebra is not an idempotent of the block, the block being a bracket and not a product. The
comparison with the parent product is the comparison of the origin alone with the two-point set
$\{0,e_0\}$, and the two companion articles that the vanishing square makes equal are *Square Roots
of Minus One, Zero and Plus One in the Antisymmetric Plain Algebra* and *Nilpotents of the
Antisymmetric Plain Algebra*, which are cited.

## The Notion and Its Product

**Definition (idempotent of a product).** Let $\star$ be a product on $\mathbb{H}$. An element
$\tilde\pi$ is an **idempotent of $\star$** when $\tilde\pi\star\tilde\pi=\tilde\pi$. The origin and,
when the product is unital, the unit are idempotents of every product; they are the **trivial
idempotents**, and the others are **nontrivial** (*Definitions for the Study of the 6 Algebraic
Structures*, §*The Element Vocabulary*).

Throughout this article the product is the antisymmetric plain multiplication $\times$, and
unqualified, *idempotent* means an idempotent of $\times$. The idempotent is the root of $+1$ in the
scaled sense of the definitions article, and the block's roots of $+1$ are treated in *Square Roots
of Minus One, Zero and Plus One in the Antisymmetric Plain Algebra*; the idempotent sets of the six
structures, and the table that compares them, are *Idempotents*.

## The Criterion

**Theorem (the idempotent set).** The idempotent equation of the block is satisfied by the origin
alone,

$$
\{\tilde\pi:\tilde\pi\times\tilde\pi=\tilde\pi\}=\{0\}.
$$

*Proof.* The block is alternating, $\tilde x\times\tilde x=0$ for every $\tilde x$, by
*Introduction to the Antisymmetric Plain Algebra of Quaternions*; read at $\tilde x=\tilde\pi$ this
gives $\tilde\pi\times\tilde\pi=0$. The idempotent equation becomes $0=\tilde\pi$, whose only
solution is the origin. The origin is an idempotent indeed, $0\times0=0=0$.

The criterion is the whole of the computation, because the left side of the equation is identically
zero and the equation constrains the right side alone. Every candidate idempotent is excluded at
once, and no coordinate computation is needed; the same criterion is recorded for the class of
nonzero idempotents in *Definitions for the Study of the 6 Algebraic Structures*, §*The Criterion for
an Empty Class*.

**Corollary (no nontrivial idempotent).** The block has no nontrivial idempotent. In particular the
unit $e_0$ of the ambient algebra is not an idempotent of the block:
$e_0\times e_0=\mathbf 0\times\mathbf 0=0\neq e_0$.

*Proof.* A nontrivial idempotent is one different from the origin and, when the product is unital,
from the unit; the theorem says that the origin is the only idempotent, so there is no nontrivial
one. The element $e_0$ satisfies $e_0\times e_0=0$ and $0\neq e_0$, so it is not an idempotent of
the block, although it is the unit of the parent product.

The equation is read in the product and not in the algebra, and the block is not the plain product.
The element $e_0$ is an idempotent of the parent and not of the block; the origin is an idempotent of
both, being the trivial idempotent of every product.

## The Absence of the Projector and of the Peirce Calculus

**Proposition (no nontrivial projector).** The only idempotent of the block is the origin, whose left
multiplication operator is the zero operator. The block therefore carries no nontrivial projector:
there is no nonzero idempotent element whose multiplication operator is a nonzero idempotent
operator.

*Proof.* By the theorem the only idempotent element is the origin, and $L_0=0$; the zero operator is a
projector, but there is no other idempotent element to produce one.

**Proposition (no Peirce decomposition).** The block has no Peirce decomposition relative to a
nontrivial idempotent, because it has no nontrivial idempotent, and the associativity the
construction also presupposes is unavailable in the block.

*Proof.* The Peirce decomposition is defined relative to a nontrivial idempotent of an associative
product; the block has none, and it is not associative (*The Specificities of the Antisymmetric
Plain Algebra*). The idempotent calculus of the parent — the left ideals, the direct sum
decompositions and the Peirce decomposition — has no entry point here.

**Remark.** The vanishing square makes the two levels of the idempotent theory collapse onto the
trivial one. An idempotent of an alternating product cannot exist off the origin, because the square
of every element vanishes; the block is the extreme case of the collapse, and the Peirce calculus,
the ideals and the module theory built from idempotents have no entry point in it. These
constructions belong to the plain product and to its blocks.

## The Comparison with the Parent Product

**Remark (the parent idempotents).** The parent general plain bilinear product is associative and
unital, and its idempotents are the two-point set $\{0,e_0\}$: the equation $\tilde x^2=\tilde x$
reads $\tilde x(\tilde x-e_0)=0$, and the parent is a division product, so $\tilde x=0$ or
$\tilde x=e_0$ (*The Specificities of the General Plain Algebra*; *Idempotents*). The block is the
antisymmetric half of that product, and the comparison is the comparison of a one-point set with a
two-point set: the block keeps the trivial idempotent and loses $e_0$, and it loses with it the
entire idempotent calculus. The count is the point of the article — one idempotent for the block
against two for the parent — and it is decided by the single value of the square at $e_0$, which is
$e_0$ in the parent and $0$ in the block.

**Remark (the contrast with the biquaternion chapter).** Over $\mathbb{C}$ the same parent product
carries the idempotent family $\tfrac12(e_0+\tilde\Xi i)$ over the roots $\tilde\Xi$ of $-1$, of real
dimension four, and the four general products of the biquaternion space carry four idempotent sets
whose sizes range from the trivial pair to the continuum (*Idempotents*). The real block is poorer
than any of them: it has the origin alone, and the complexification does not enlarge its idempotent
set, the equation $0=\tilde\pi$ being independent of the field.

## Summary

For the antisymmetric plain multiplication $\tilde p\times\tilde q=\mathbf p\times\mathbf q$ the
idempotent equation $\tilde\pi\times\tilde\pi=\tilde\pi$ reduces to $0=\tilde\pi$, because the block
is alternating; the block has one idempotent, the origin, and no nontrivial idempotent. The unit
$e_0$ of the ambient algebra is not an idempotent of the block, the block being a bracket. No
orthogonal family, no primitive idempotent, no projection and no Peirce decomposition exists, and the
only projector the block carries is the zero operator, from the origin. The comparison with the
parent product is the comparison of the origin alone with the two-point set $\{0,e_0\}$, and the
idempotent calculus — the left ideals, the direct sum decompositions, the Peirce decomposition —
belongs to the parent and not to the block.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde p\times\tilde q=\tfrac12(\tilde p\tilde q-\tilde q\tilde p)=\mathbf p\times\mathbf q$ | the antisymmetric plain multiplication, the operation $\mathrm{APA}$ |
| $\tilde\pi\times\tilde\pi=\tilde\pi$ | the idempotent equation, equivalent to $0=\tilde\pi$ |
| $\{0\}$ | the idempotent set of the block, the trivial idempotent alone |
| $L_{\tilde\pi}$ | the left multiplication operator of an idempotent, the zero operator at the origin |
| $\{0,e_0\}$ | the idempotents of the parent product, of which the block keeps only the origin |

## Further Reading

- *Definitions for the Study of the 6 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-6-algebraic-structures.md`), for the idempotent of a general product, the relativity of the definition and the criterion for an empty class
- *Introduction to the Antisymmetric Plain Algebra of Quaternions* (`articles_maths/introduction-to-the-antisymmetric-plain-algebra-of-quaternions.md`), for the operation, its alternation and its table
- *The Specificities of the General Plain Algebra* (`articles_maths/the-specificities-of-the-general-plain-algebra-of-quaternions.md`), for the two-point idempotent set of the parent division product
- *Idempotents* (`articles_maths/quaternion-idempotents.md`), for the idempotent sets of the six structures side by side
- *Idempotents* (`articles_maths/idempotents.md`), for the four idempotent sets of the biquaternion chapter, against which the real block's origin alone is read
- *Square Roots of Minus One, Zero and Plus One in the Antisymmetric Plain Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-antisymmetric-plain-algebra-of-quaternions.md`), for the roots of $+1$, which are the idempotents in the scaled sense
- *Nilpotents of the Antisymmetric Plain Algebra* (`articles_maths/nilpotents-of-the-antisymmetric-plain-algebra-of-quaternions.md`), for the other face of the same vanishing square
- *The Specificities of the Antisymmetric Plain Algebra* (`articles_maths/the-specificities-of-the-antisymmetric-plain-algebra-of-quaternions.md`), for the folded reading of the idempotent set of the block
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for idempotents, the Peirce decomposition and the radical.
- Israel Nathan Herstein, *Topics in Algebra* (Wiley, 2nd ed. 1975), for idempotents and the ideal theory of a ring.
