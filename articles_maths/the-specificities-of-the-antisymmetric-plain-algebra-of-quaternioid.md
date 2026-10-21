# __The Specificities of the Antisymmetric Plain Algebra__

## Introduction

The antisymmetric plain algebra of $\mathbb{H}$ is the cross product
$\tilde q_1\times\tilde q_2=\tfrac12(\tilde q_1\tilde q_2-\tilde q_2\tilde q_1)=\vec q_1\times\vec q_2$ of
*Introduction to the Antisymmetric Plain Algebra*. This article states what singles
the block out among the companion products of the space: the two identities it satisfies, the classes its
laws empty, and the place it takes in the law table of *Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*.

The block is the **only** companion product that is at once alternating and Jacobi; the two
properties together make it the Lie product of the space. It has no unit, hence no inverse and no
group of units, and no algebraic norm in the sense of the block. Its idempotents reduce to $0$, and
its nilpotents are the whole space; the two classes, to which the biquaternion chapter gave
separate articles and which the real block gives the companion articles *Square Roots of One and the
Idempotents of the Antisymmetric Plain Algebra* and *Square Roots of Zero and the Nilpotents of the
Antisymmetric Plain Algebra*, are folded here.

**This is not the algebra $\mathbb{H}$.** The two share the space, the addition and the real scalars,
but $\times$ is a different multiplication, alternating and without a unit. Throughout, the natural
sign ${}^{\natural}$ is the quaternion conjugation, the bar is the identity because $\mathbb{R}$ has
no nontrivial involution, and the star coincides with the natural sign and gives nothing new.

The operation and its table are *Introduction to the Antisymmetric Plain Algebra*; the
Lie structure, the form and the operators are *The Lie Algebra of the Antisymmetric Plain Algebra*,
*The Killing Form of the Antisymmetric Plain Algebra* and *The Adjoint Operators and the Derivations
of the Antisymmetric Plain Algebra*, and the element theory is *Zero Divisors of the Antisymmetric
Plain Algebra*, *Square Roots of One and the Idempotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* and
*Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, all below this article
in this category. The law vocabulary is *Definitions for the Study of
the Algebraic Structures* and the law table *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*.

**Conventions.** The algebra is $\mathbb{H}$ with basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$ and
$\vec e_x^2=\vec e_y^2=\vec e_z^2=-e_t$; a generic element is $\tilde q=q_te_t+\vec q$, the centre is
$\mathbb{R}_{\mathbb{H}}=\mathbb{R}e_t$ and the vector subspace is $\mathrm{Vect}(\mathbb{H})=\{\vec q\}$.
The laws are those of *Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*.

## The Criterion

### The Two Properties

**Theorem (the isolating pair).** The block is **alternating**,

$$
\tilde q\times\tilde q=0\qquad\text{for every }\tilde q,
$$

and satisfies the **Jacobi identity**,

$$
\tilde q_1\times(\tilde q_2\times\tilde q_3)+\tilde q_2\times(\tilde q_3\times\tilde q_1)+\tilde q_3\times(\tilde q_1\times\tilde q_2)=0
\qquad\text{for all }\tilde q_1,\tilde q_2,\tilde q_3 .
$$

*Proof.* The alternation is $\tfrac12(\tilde q\tilde q-\tilde q\tilde q)=0$, the two terms of the
difference coinciding. The cyclic sum is the one of the vector product of the vector parts,
$(\vec q_1\times\vec q_2)\times\vec q_3+(\vec q_2\times\vec q_3)\times\vec q_1+(\vec q_3\times\vec q_1)\times\vec q_2$,
which vanishes by the anticommutativity of the vector product; it is verified on general elements and
on the $64$ triples of the units.

**Corollary (the block is the Lie product of the space).** An alternating bilinear rule satisfying
the Jacobi identity is a Lie bracket, so $(\mathbb{H},\times)$ is a Lie algebra. Among the companion
products of the space, the block is the only structure that is both alternating and Jacobi: the other
alternating product, the antisymmetric quaternionic operation, fails the Jacobi identity, and the four
remaining products are not alternating. The Lie structure is *The Lie Algebra of the Antisymmetric
Plain Algebra*, below this article in this category.

### The Laws That Follow

**Proposition.** The block is **flexible**, **power-associative** and **cube-zero**,

$$
(\tilde q_1\times\tilde q_2)\times\tilde q_1=\tilde q_1\times(\tilde q_2\times\tilde q_1),\qquad
(\tilde q\times\tilde q)\times\tilde q=\tilde q\times(\tilde q\times\tilde q),\qquad
\tilde q\times(\tilde q\times\tilde q)=0,
$$

and it is **not** associative and **not** alternative: the associator
$(\tilde q_1\times\tilde q_2)\times\tilde q_3-\tilde q_1\times(\tilde q_2\times\tilde q_3)$ does not vanish, and
the right alternative law fails at $\vec e_x,\vec e_y,\vec e_y$.

*Proof.* A bilinear alternating rule is antisymmetric, and the implications "alternating and bilinear
$\Rightarrow$ flexible, power-associative, cube-zero" of *Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* give the first three; flexibility is checked at $\vec e_x,\vec e_y$, where
$(\vec e_x\times \vec e_y)\times \vec e_x=\vec e_z\times \vec e_x=\vec e_y$ and $\vec e_x\times(\vec e_y\times \vec e_x)=\vec e_x\times(-\vec e_z)=\vec e_y$. The
associator is read on the units, where $(\vec e_x\times \vec e_y)\times \vec e_y=\vec e_z\times \vec e_y=-\vec e_x$ is different
from $\vec e_x\times(\vec e_y\times \vec e_y)=0$, so the rule is not associative; the same triple is the failure of
the right alternative law.

## The Absence of a Unit, of an Inverse and of a Norm

**Theorem.** The block has no two-sided unit and no one-sided unit; hence it has no inverse, its group
of units is empty, and it carries no algebraic norm in the sense of the block.

*Proof.* Every value is pure, whereas $\tilde q_1\times\tilde q_2=\tilde q_1$ at a non-pure $\tilde q_1$
would be a non-pure value; and the scalar direction is not reached at all, $\tilde q_1\times\tilde q_2$
having zero scalar part. So no element is a unit on either side, the inverse being defined relative to
a two-sided unit. The algebraic norm of a product is a quadratic form multiplicative for the product;
the diagonal form of the block is the vanishing function $\tilde q\times\tilde q=0$, so the block's own
algebraic norm is the zero form, and the norms $\langle\cdot\rangle_{\natural}$ and $\langle\cdot,\cdot\rangle_{\natural}$ of the space are not multiplicative for
$\times$.

**Remark (the contrast with the plain and symmetric blocks).** The plain algebra has the unit $e_t$
and the multiplicative norm $\langle\tilde q\rangle_{\natural}=\tilde q\tilde q^{\natural}$; the symmetric plain algebra
keeps the unit $e_t$, but it is no longer a division algebra and its norm is no longer multiplicative;
the antisymmetric block has neither, its two quadratic objects $\langle\cdot\rangle_{\natural}$ and $\langle\cdot,\cdot\rangle_{\natural}$ being carried by the
symmetric products instead. The absence is *definitional*, not accidental: it follows from alternation
alone.

## The Folded Element Classes

### The Idempotents

**Theorem.** The idempotents of the block are only $0$,

$$
\tilde\pi\times\tilde\pi=\tilde\pi\iff\tilde\pi=0 .
$$

*Proof.* The square is zero for every element, so the equation is $\tilde\pi=0$. The idempotent set
is the origin alone; its own article is *Square Roots of One and the Idempotents of the
Antisymmetric Plain Algebra*, below this article in this category, and the class is folded here.

### The Nilpotents

**Theorem.** The nilpotents of the block are the **whole space**: the origin is the trivial nilpotent
of index one, and every other element is a nilpotent of index two,

$$
\tilde\nu\times\tilde\nu=0\qquad\text{for every }\tilde\nu,\qquad
\tilde\nu\neq0\implies\tilde\nu\ \text{is of index }2 .
$$

The nonzero nilpotents are the punctured space, and the class coincides with the zero-divisor set and
with the root set of $0$ (*Square Roots of Zero and the Nilpotents of the Antisymmetric Plain
Algebra* and *Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, both below this article in this
category).

*Proof.* The square vanishes identically, so every element is square-zero; the index of nilpotency is
two for a nonzero element, the square being zero and the element itself nonzero, and one for the
origin. The reading is the one of *Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*, where the
class of nonzero nilpotents is the whole space for the two antisymmetric structures.

## The Isolation among the Companion Products

The following table, the law table of *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* read on the identities, shows the isolation of the block. The entries are the structures that
satisfy the identity.

| identity | $\mathrm{SPA}$ | $\mathrm{APA}$ | $\mathrm{GQA}$ |
|---|---|---|---|
| alternating | no | **yes** | no |
| flexible | yes | yes | no |
| power-associative | yes | yes | no |
| Jordan identity | yes | yes | yes |
| associative | no | no | no |
| Jacobi identity | no | **yes** | no |

**Remark (what isolates the block).** Two readings single the block out. First, $\mathrm{APA}$ is the
**only** structure that is both alternating and Jacobi, hence the only Lie structure of the companion
products. Second, the block has no unit while the symmetric plain structure does, is not associative,
and fails the norm while the symmetric plain structure carries one. The block is therefore
$\mathrm{APA}$, the Lie bracket of the space.

## The Boundary of the Criterion

**Proposition.** The criterion of isolation is the pair (alternating, Jacobi). Alternation alone does
not isolate the block: the antisymmetric quaternionic structure is alternating and fails Jacobi. In the
law table the Jacobi identity alone already points at the block, since it is the only structure whose
product satisfies the identity; alternation is the further demand that turns a Jacobi product into a
Lie product. The criterion does not reach the element theory of the symmetric blocks, which is read on
the basis.

*Proof.* The failure of alternation alone is the witness $(e_t,\vec e_x,\vec e_y)$ of the antisymmetric
quaternionic structure, whose cyclic sum is a nonzero multiple of $\vec e_z$; the Jacobi row of the table is
zero for every structure but the block. The element theory of the symmetric structures requires a
basis computation, as the table of empty classes records.

## Summary

The antisymmetric plain block is isolated among the companion products by a single pair of identities: it is
alternating, $\tilde q\times\tilde q=0$, and it satisfies the Jacobi identity, so it is the unique Lie
structure of the space. Its laws are those the two properties force: flexible, power-associative and
cube-zero, and neither associative nor alternative in the nonzero sense. The block has no unit on
either side, hence an empty group of units and no algebraic norm of its own, the diagonal form of the
operation being the zero function. Its idempotents reduce to $0$ and its nilpotents are the whole
space, the class being folded here; both are shared with the antisymmetric quaternionic block, whose
Jacobi identity fails. The block is therefore one of the two degenerate antisymmetric structures, and
the Jacobi identity is the whole of the difference between them.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde q\times\tilde q=0$ | the alternation, the isolating law |
| $\tilde q_1\times(\tilde q_2\times\tilde q_3)+\text{cyclic}=0$ | the Jacobi identity, the second isolating law |
| $\{0\}$ | the idempotents, folded here |
| $\mathbb{H}$ | the nilpotent set, the whole space, folded here |
| $\varnothing$ | the group of units, the algebraic norm taken as nonzero |
| $\mathrm{APA}$ | the unique Lie structure of the companion products |

## Further Reading

- [Introduction to the Antisymmetric Plain Algebra](introduction-to-the-antisymmetric-plain-algebra-of-quaternioid.html), for the operation, its table and the absence of a unit.
- [The Lie Algebra of the Antisymmetric Plain Algebra](the-lie-algebra-of-the-antisymmetric-plain-algebra-of-quaternioid.html), below this article in this category, for the Lie structure.
- [The Killing Form of the Antisymmetric Plain Algebra](the-killing-form-of-the-antisymmetric-plain-algebra-of-quaternioid.html) and [The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra](the-adjoint-operators-and-the-derivations-of-the-antisymmetric-plain-algebra-of-quaternioid.html), both below this article in this category, for the form and the derivations.
- [Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](zero-divisors-in-the-algebraic-structures-over-the-biquaternion-c-space.html), [Square Roots of One and the Idempotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](square-roots-of-one-and-the-idempotents-in-the-algebraic-structures-over-the-biquaternion-c-space.html) and [Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](square-roots-of-zero-and-the-nilpotents-in-the-algebraic-structures-over-the-biquaternion-c-space.html), all below this article in this category, for the element classes folded here.
- [Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space](definitions-for-the-study-of-the-algebraic-structures-over-the-quaternioid-r-space.html) and [The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space](the-algebraic-structures-over-the-quaternioid-r-space.html), for the law vocabulary and the law table.
