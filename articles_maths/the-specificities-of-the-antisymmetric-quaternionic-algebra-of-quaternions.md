# __The Specificities of the Antisymmetric Quaternionic Algebra__

## Introduction

The antisymmetric quaternionic algebra of $\mathbb{H}$ is the quaternionic product
$\tilde p\diamond\tilde q=\tfrac12(\tilde p^{\natural}\tilde q-\tilde q^{\natural}\tilde p)=p_0\mathbf q-q_0\mathbf p-\mathbf p\times\mathbf q$ of *Introduction to the Antisymmetric
Quaternionic Algebra of Quaternions*. This article states what singles the block out among the six
products of the space: the identities it satisfies and those it fails, the classes its laws empty, and
the place it takes in the law table of *Definitions for the Study of the 6 Algebraic Structures*.

The block is **alternating** like its plain companion, and unlike it, it **fails the Jacobi identity**;
the two facts together isolate it, since it is the only alternating product of the six that is not a
Lie bracket. It has no unit, hence no inverse and no group of units, and no algebraic norm in the sense
of the block. Its idempotents reduce to $0$, and its nilpotents are the whole space. The idempotent and

**This is not the algebra $\mathbb{H}$.** The two share the space, the addition and the real scalars,
but $\diamond$ is a different multiplication, alternating, without a unit and without the Jacobi
identity. Throughout, the natural sign ${}^{\natural}$ is the quaternion conjugation, the bar is the
identity because $\mathbb{R}$ has no nontrivial involution, and the star coincides with the natural
sign and gives nothing new. The symbol $\diamond$ is reserved for this block.

The operation and its table are *Introduction to the Antisymmetric Quaternionic Algebra of
Quaternions*; the failure is *The Jacobi Failure and the Associator Defect of the Antisymmetric
Quaternionic Algebra*, the form is *The Invariant Bilinear Forms of the Antisymmetric Quaternionic
Algebra* and the operators are *The Adjoint Operators of the Antisymmetric Quaternionic Algebra*, all
below this article in this category. The comparator is *The Specificities of the Antisymmetric Plain
Algebra*, above this article in this category. The law vocabulary is *Definitions for the Study of the
6 Algebraic Structures* and the law table *The 6 Algebraic Structures over the Quaternion
$\mathbb{R}$ Space*.

**Conventions.** The algebra is $\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$ and
$e_1^2=e_2^2=e_3^2=-e_0$; a generic element is $\tilde q=q_0e_0+\mathbf q$, the centre is
$\mathbb{R}_{\mathbb{H}}=\mathbb{R}e_0$ and the vector subspace is $\mathrm{Vect}(\mathbb{H})=\{\mathbf q\}$.
The laws are those of *Definitions for the Study of the 6 Algebraic Structures*.

## The Two-Line Criterion

### The Alternation and the Vanishing Square

**Theorem.** The block is **alternating**,

$$
\tilde p\diamond\tilde p=0\qquad\text{for every }\tilde p,
$$

so every element is square-zero, and no element has an inverse in the block's sense.

*Proof.* The alternation is $\tfrac12(\tilde p^{\natural}\tilde p-\tilde p^{\natural}\tilde p)=0$, the two
terms of the difference coinciding; the square is $\tilde p\diamond\tilde p=0$; an inverse requires a
two-sided unit, which the block does not have.

### The Jacobi Failure

**Theorem (the failure, with witness).** The block does **not** satisfy the Jacobi identity. Its cyclic
sum has the closed form

$$
J(\tilde p,\tilde q,\tilde r)=-p_0\,(\mathbf q\times\mathbf r)+q_0\,(\mathbf p\times\mathbf r)-r_0\,(\mathbf p\times\mathbf q),
$$

and the witness $(e_0,e_1,e_2)$ gives

$$
J(e_0,e_1,e_2)=(e_0\diamond e_1)\diamond e_2+(e_1\diamond e_2)\diamond e_0+(e_2\diamond e_0)\diamond e_1=-e_3\neq0 .
$$

The block is therefore **not a Lie algebra**, and the failure is exactly the associator defect of the
parent quaternionic product: $J=\tfrac14\sum_\sigma\operatorname{sgn}(\sigma)\operatorname{assoc}(\tilde p_\sigma,\tilde q_\sigma,\tilde r_\sigma)$,
the associator being that of the product $\tilde p^{\natural}\tilde q$. The full reading is *The Jacobi
Failure and the Associator Defect of the Antisymmetric Quaternionic Algebra*, below this article in this
category.

*Proof.* Inserting the explicit form into the three terms gives the closed form, which is linear in the
scalar triple with the three cross products as coefficients; at $(e_0,e_1,e_2)$ only the first term
survives and equals $-(e_1\times e_2)=-e_3$. The associator identity is the criterion of *The Symmetric
and Antisymmetric Parts of an Algebra Product* read on the parent product, verified on general
elements.

**Remark (the contrast with the comparator).** The antisymmetric plain block of the same space is
alternating and **satisfies** the identities its alternation implies, the Jacobi identity included; the
antisymmetric quaternionic block shares the alternation and differs in the failure. This single failure
is the whole difference between the two antisymmetric blocks, and it is why the plain block is
$\mathfrak{su}(2)$ and this one is not.

## The Absence of a Unit, of an Inverse and of a Norm

**Theorem.** The block has no two-sided unit and no one-sided unit; hence it has no inverse, its group of
units is empty, and it carries no algebraic norm of the block.

*Proof.* Every value is pure, whereas $\tilde p\diamond\tilde q=\tilde p$ at a non-pure $\tilde p$
would be a non-pure value, and the scalar direction is not reached, $\tilde p\diamond\tilde q$ having
zero scalar part; the candidate $e_0$ gives $e_0\diamond\tilde q=\mathbf q$, the projection, which is
$\tilde q$ only on the vector subspace. No element is a unit on either side. The algebraic norm of a
product is a quadratic form multiplicative for the product; the diagonal form of the block is the
vanishing function $\tilde q\diamond\tilde q=0$, so its own algebraic norm is the zero form.

**Remark (the contrast with the quaternion norm).** The parent quaternionic product has the
multiplicative norm $N(\tilde q)=\tilde q^{\natural}\tilde q$ and the block does not inherit it: the
square map sees only the symmetric half, which collapses onto the scalar line, and the antisymmetric
half carries neither a square nor a norm. The symmetric half is *The Symmetric Quaternionic Algebra of
Quaternions*.

## The Folded Element Classes

### The Idempotents

**Theorem.** The idempotents of the block are only $0$,

$$
\tilde\pi\diamond\tilde\pi=\tilde\pi\iff\tilde\pi=0 .
$$

*Proof.* The square is zero for every element, so the equation is $\tilde\pi=0$. The idempotent theory
into this article.

### The Nilpotents

**Theorem.** The nilpotents of the block are the **whole space**: the origin is the trivial nilpotent of
index one, and every other element is a nilpotent of index two,

$$
\tilde\nu\diamond\tilde\nu=0\qquad\text{for every }\tilde\nu,\qquad
\tilde\nu\neq0\implies\tilde\nu\ \text{is of index }2 .
$$

The nonzero nilpotents are the punctured space. The class is the whole space and not the vector
subspace: the block's square vanishes on every element, the scalar direction included, since
$e_0\diamond e_0=0$.

*Proof.* The square vanishes identically, so every element is square-zero; the index is two for a
nonzero element and one for the origin. The reading is the one of *Definitions for the Study of the 6
Algebraic Structures*, where the class of nonzero nilpotents is the whole space for the two
antisymmetric structures.

## The Isolation among the Six

The following table, the law table of *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$
Space* read on the identities, shows the isolation of the block. The entries are the structures that
satisfy the identity.

| identity | $\mathrm{GPA}$ | $\mathrm{SPA}$ | $\mathrm{APA}$ | $\mathrm{GQA}$ | $\mathrm{SQA}$ | $\mathrm{AQA}$ |
|---|---|---|---|---|---|---|
| alternating | no | no | yes | no | no | **yes** |
| flexible | yes | yes | yes | no | yes | yes |
| power-associative | yes | yes | yes | no | yes | yes |
| Jordan identity | yes | yes | yes | yes | no | yes |
| associative | yes | no | no | no | no | no |
| Jacobi identity | no | no | yes | no | no | **no** |

**Remark (what isolates the block).** The block is the **only** structure of the six that is alternating
and **fails** the Jacobi identity. It is one of the two alternating structures, the other being the
antisymmetric plain one, which satisfies the identity; and among the six it is the only one whose
alternation is not balanced by the Lie law. The block is therefore the second of the two antisymmetric
structures in the order of the catalogue, separated from its companion by the Jacobi identity alone.

## The Boundary of the Criterion

**Proposition.** The criterion of isolation is exactly the pair (alternating, Jacobi fails). Neither
property alone isolates the block: the antisymmetric plain structure is alternating and satisfies
Jacobi, and the general quaternionic structure fails Jacobi without being alternating. The criterion
does not reach the element theory, which is read from the vanishing square and is common to the two
antisymmetric blocks.

*Proof.* The first failure is the law table's Jacobi row, whose vanishing for $\mathrm{AQA}$ is the
witness $(e_0,e_1,e_2)$; the second is the alternation row. The element theory needs only
$\tilde p\diamond\tilde p=0$ and is identical in the two alternating structures.

## Summary

The antisymmetric quaternionic block is alternating, $\tilde p\diamond\tilde p=0$, and **fails the
Jacobi identity**, with the closed form $J=-p_0(\mathbf q\times\mathbf r)+q_0(\mathbf p\times\mathbf r)-r_0(\mathbf p\times\mathbf q)$
and the witness $J(e_0,e_1,e_2)=-e_3$; it is therefore not a Lie algebra, and this failure is exactly
the associator defect of the parent quaternionic product, $J=\tfrac14\sum_\sigma\operatorname{sgn}(\sigma)\operatorname{assoc}$.
The block is the only structure of the six that is alternating and not Lie, and this pair isolates it
from its plain companion, which satisfies the identity. It has no unit on either side, hence an empty
group of units and no algebraic norm of its own, the diagonal form of the operation being the zero
function and the square map seeing only the symmetric half. Its idempotents reduce to $0$ and its
nilpotents are the whole space, the class being folded here; both are shared with the antisymmetric
plain block, whose Jacobi identity holds.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde p\diamond\tilde p=0$ | the alternation, shared with the plain block |
| $J(\tilde p,\tilde q,\tilde r)=-p_0(\mathbf q\times\mathbf r)+q_0(\mathbf p\times\mathbf r)-r_0(\mathbf p\times\mathbf q)$ | the cyclic sum, the failure |
| $J(e_0,e_1,e_2)=-e_3$ | the witness of the failure |
| $\tfrac14\sum_\sigma\operatorname{sgn}(\sigma)\operatorname{assoc}$ | the failure as the associator defect of the parent |
| $\{0\}$ | the idempotents, folded here |
| $\mathbb{H}$ | the nilpotent set, the whole space, folded here |
| $\varnothing$ | the group of units, the algebraic norm taken as nonzero |
| $\mathrm{AQA}$ | the only alternating structure that is not Lie |

## Further Reading

- *Introduction to the Antisymmetric Quaternionic Algebra of Quaternions*, for the operation, its table and the absence of a unit.
- *The Jacobi Failure and the Associator Defect of the Antisymmetric Quaternionic Algebra*, below this article in this category, for the failure in full.
- *The Invariant Bilinear Forms of the Antisymmetric Quaternionic Algebra* and *The Adjoint Operators of the Antisymmetric Quaternionic Algebra*, both below this article in this category, for the form and the operators.
- *The Symmetric and Antisymmetric Parts of an Algebra Product*, for the criterion relating the failure to the associator.
- *The Specificities of the Antisymmetric Plain Algebra*, above this article in this category, for the comparator whose Jacobi identity holds.
- *Definitions for the Study of the 6 Algebraic Structures* and *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, for the law vocabulary and the law table.
