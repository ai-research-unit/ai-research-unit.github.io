# __The Specificities of the Antisymmetric Plain Algebra__

## Introduction

The antisymmetric plain algebra of $\mathbb{H}$ is the cross product
$\tilde p\times\tilde q=\tfrac12(\tilde p\tilde q-\tilde q\tilde p)=\mathbf p\times\mathbf q$ of
*Introduction to the Antisymmetric Plain Algebra of Quaternions*. This article states what singles
the block out among the six products of the space: the two identities it satisfies, the classes its
laws empty, and the place it takes in the law table of *Definitions for the Study of the 6 Algebraic
Structures*.

The block is the **only** product of the six that is at once alternating and Jacobi; the two
properties together make it the Lie product of the space. It has no unit, hence no inverse and no
group of units, and no algebraic norm in the sense of the block. Its idempotents reduce to $0$, and
its nilpotents are the whole space. The idempotent and the nilpotent theory, which the biquaternion
chapter gave separate articles, are folded here.

**This is not the algebra $\mathbb{H}$.** The two share the space, the addition and the real scalars,
but $\times$ is a different multiplication, alternating and without a unit. Throughout, the natural
sign ${}^{\natural}$ is the quaternion conjugation, the bar is the identity because $\mathbb{R}$ has
no nontrivial involution, and the star coincides with the natural sign and gives nothing new.

The operation and its table are *Introduction to the Antisymmetric Plain Algebra of Quaternions*; the
Lie structure, the form and the operators are *The Lie Algebra of the Antisymmetric Plain Algebra*,
*The Killing Form of the Antisymmetric Plain Algebra* and *The Adjoint Operators and the Derivations
of the Antisymmetric Plain Algebra*, and the element theory is *Zero Divisors of the Antisymmetric
Plain Algebra* and *Square Roots of Minus One, Zero and Plus One in the Antisymmetric Plain
Algebra*, all below this article in this category. The law vocabulary is *Definitions for the Study of
the 6 Algebraic Structures* and the law table *The 6 Algebraic Structures over the Quaternion
$\mathbb{R}$ Space*.

**Conventions.** The algebra is $\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$ and
$e_1^2=e_2^2=e_3^2=-e_0$; a generic element is $\tilde q=q_0e_0+\mathbf q$, the centre is
$\mathbb{R}_{\mathbb{H}}=\mathbb{R}e_0$ and the vector subspace is $\mathrm{Vect}(\mathbb{H})=\{\mathbf q\}$.
The laws are those of *Definitions for the Study of the 6 Algebraic Structures*.

## The Criterion

### The Two Properties

**Theorem (the isolating pair).** The block is **alternating**,

$$
\tilde p\times\tilde p=0\qquad\text{for every }\tilde p,
$$

and satisfies the **Jacobi identity**,

$$
\tilde p\times(\tilde q\times\tilde r)+\tilde q\times(\tilde r\times\tilde p)+\tilde r\times(\tilde p\times\tilde q)=0
\qquad\text{for all }\tilde p,\tilde q,\tilde r .
$$

*Proof.* The alternation is $\tfrac12(\tilde p\tilde p-\tilde p\tilde p)=0$, the two terms of the
difference coinciding. The cyclic sum is the one of the vector product of the vector parts,
$(\mathbf p\times\mathbf q)\times\mathbf r+(\mathbf q\times\mathbf r)\times\mathbf p+(\mathbf r\times\mathbf p)\times\mathbf q$,
which vanishes by the anticommutativity of the vector product; it is verified on general elements and
on the $64$ triples of the units.

**Corollary (the block is the Lie product of the space).** An alternating bilinear rule satisfying
the Jacobi identity is a Lie bracket, so $(\mathbb{H},\times)$ is a Lie algebra. Among the six
products of the space, the block is the only structure that is both alternating and Jacobi: the other
alternating product, the antisymmetric quaternionic operation, fails the Jacobi identity, and the four
remaining products are not alternating. The Lie structure is *The Lie Algebra of the Antisymmetric
Plain Algebra*, below this article in this category.

### The Laws That Follow

**Proposition.** The block is **flexible**, **power-associative** and **cube-zero**,

$$
(\tilde p\times\tilde q)\times\tilde p=\tilde p\times(\tilde q\times\tilde p),\qquad
(\tilde p\times\tilde p)\times\tilde p=\tilde p\times(\tilde p\times\tilde p),\qquad
\tilde p\times(\tilde p\times\tilde p)=0,
$$

and it is **not** associative and **not** alternative: the associator
$(\tilde p\times\tilde q)\times\tilde r-\tilde p\times(\tilde q\times\tilde r)$ does not vanish, and
the right alternative law fails at $e_1,e_2,e_2$.

*Proof.* A bilinear alternating rule is antisymmetric, and the implications "alternating and bilinear
$\Rightarrow$ flexible, power-associative, cube-zero" of *Definitions for the Study of the 6
Algebraic Structures* give the first three; flexibility is checked at $e_1,e_2$, where
$(e_1\times e_2)\times e_1=e_3\times e_1=e_2$ and $e_1\times(e_2\times e_1)=e_1\times(-e_3)=e_2$. The
associator is read on the units, where $(e_1\times e_2)\times e_2=e_3\times e_2=-e_1$ is different
from $e_1\times(e_2\times e_2)=0$, so the rule is not associative; the same triple is the failure of
the right alternative law.

## The Absence of a Unit, of an Inverse and of a Norm

**Theorem.** The block has no two-sided unit and no one-sided unit; hence it has no inverse, its group
of units is empty, and it carries no algebraic norm in the sense of the block.

*Proof.* Every value is pure, whereas $\tilde p\times\tilde q=\tilde p$ at a non-pure $\tilde p$
would be a non-pure value; and the scalar direction is not reached at all, $\tilde p\times\tilde q$
having zero scalar part. So no element is a unit on either side, the inverse being defined relative to
a two-sided unit. The algebraic norm of a product is a quadratic form multiplicative for the product;
the diagonal form of the block is the vanishing function $\tilde q\times\tilde q=0$, so the block's own
algebraic norm is the zero form, and the norms $N$ and $B$ of the space are not multiplicative for
$\times$.

**Remark (the contrast with the plain and symmetric blocks).** The plain algebra has the unit $e_0$
and the multiplicative norm $N(\tilde q)=\tilde q\tilde q^{\natural}$; the symmetric plain algebra
keeps the unit $e_0$, but it is no longer a division algebra and its norm is no longer multiplicative;
the antisymmetric block has neither, its two quadratic objects $N$ and $B$ being carried by the
symmetric products instead. The absence is *definitional*, not accidental: it follows from alternation
alone.

## The Folded Element Classes

### The Idempotents

**Theorem.** The idempotents of the block are only $0$,

$$
\tilde\pi\times\tilde\pi=\tilde\pi\iff\tilde\pi=0 .
$$

*Proof.* The square is zero for every element, so the equation is $\tilde\pi=0$. The idempotent
theory of the biquaternion block, where nontrivial idempotents exist, is *Idempotents of the
Antisymmetric Plain Algebra* of the biquaternion chapter; here the class reduces to the origin and is
folded into this article.

### The Nilpotents

**Theorem.** The nilpotents of the block are the **whole space**: the origin is the trivial nilpotent
of index one, and every other element is a nilpotent of index two,

$$
\tilde\nu\times\tilde\nu=0\qquad\text{for every }\tilde\nu,\qquad
\tilde\nu\neq0\implies\tilde\nu\ \text{is of index }2 .
$$

The nonzero nilpotents are the punctured space, and the class coincides with the zero-divisor set and
with the root set of $0$ (*Square Roots of Minus One, Zero and Plus One in the Antisymmetric Plain
Algebra* and *Zero Divisors of the Antisymmetric Plain Algebra*, both below this article in this
category).

*Proof.* The square vanishes identically, so every element is square-zero; the index of nilpotency is
two for a nonzero element, the square being zero and the element itself nonzero, and one for the
origin. The reading is the one of *Definitions for the Study of the 6 Algebraic Structures*, where the
class of nonzero nilpotents is the whole space for the two antisymmetric structures.

## The Isolation among the Six

The following table, the law table of *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$
Space* read on the identities, shows the isolation of the block. The entries are the structures that
satisfy the identity.

| identity | $\mathrm{GPA}$ | $\mathrm{SPA}$ | $\mathrm{APA}$ | $\mathrm{GQA}$ | $\mathrm{SQA}$ | $\mathrm{AQA}$ |
|---|---|---|---|---|---|---|
| alternating | no | no | **yes** | no | no | yes |
| flexible | yes | yes | yes | no | yes | yes |
| power-associative | yes | yes | yes | no | yes | yes |
| Jordan identity | yes | yes | yes | yes | no | yes |
| associative | yes | no | no | no | no | no |
| Jacobi identity | no | no | **yes** | no | no | no |

**Remark (what isolates the block).** Two readings single the block out. First, $\mathrm{APA}$ is the
**only** structure that is both alternating and Jacobi, hence the only Lie structure of the six, and
it is the only one that is alternating together with $\mathrm{AQA}$. Second, the block has no unit
while the general plain structure does, is not associative while the general plain structure is, and
fails the norm while the plain and symmetric structures carry one. The block is therefore
$\mathrm{APA}$, the first of the two antisymmetric structures in the order of the catalogue, paired
with the antisymmetric quaternionic structure and separated from it by the Jacobi identity alone.

## The Boundary of the Criterion

**Proposition.** The criterion of isolation is the pair (alternating, Jacobi). Alternation alone does
not isolate the block: the antisymmetric quaternionic structure is alternating and fails Jacobi. In the
law table the Jacobi identity alone already points at the block, since it is the only structure whose
product satisfies the identity; alternation is the further demand that turns a Jacobi product into a
Lie product. The criterion does not reach the element theory of the symmetric blocks, which is read on
the basis.

*Proof.* The failure of alternation alone is the witness $(e_0,e_1,e_2)$ of the antisymmetric
quaternionic structure, whose cyclic sum is a nonzero multiple of $e_3$; the Jacobi row of the table is
zero for every structure but the block. The element theory of the symmetric structures requires a
basis computation, as the table of empty classes records.

## Summary

The antisymmetric plain block is isolated among the six products by a single pair of identities: it is
alternating, $\tilde p\times\tilde p=0$, and it satisfies the Jacobi identity, so it is the unique Lie
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
| $\tilde p\times\tilde p=0$ | the alternation, the isolating law |
| $\tilde p\times(\tilde q\times\tilde r)+\text{cyclic}=0$ | the Jacobi identity, the second isolating law |
| $\{0\}$ | the idempotents, folded here |
| $\mathbb{H}$ | the nilpotent set, the whole space, folded here |
| $\varnothing$ | the group of units, the algebraic norm taken as nonzero |
| $\mathrm{APA}$ | the unique Lie structure of the six |

## Further Reading

- *Introduction to the Antisymmetric Plain Algebra of Quaternions*, for the operation, its table and the absence of a unit.
- *The Lie Algebra of the Antisymmetric Plain Algebra*, below this article in this category, for the Lie structure.
- *The Killing Form of the Antisymmetric Plain Algebra* and *The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra*, both below this article in this category, for the form and the derivations.
- *Zero Divisors of the Antisymmetric Plain Algebra* and *Square Roots of Minus One, Zero and Plus One in the Antisymmetric Plain Algebra*, both below this article in this category, for the element classes folded here.
- *Definitions for the Study of the 6 Algebraic Structures* and *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, for the law vocabulary and the law table.
