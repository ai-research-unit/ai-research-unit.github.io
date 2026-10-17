# __Introduction to the Antisymmetric Quaternionic Algebra__

## Introduction

The underlying real space of the quaternion algebra $\mathbb{H}$ carries the general quaternionic
bilinear product $\tilde p^{\natural}\tilde q$, the product of *Introduction to the General
Quaternionic Algebra of Quaternions*, with the quaternion conjugation read on the first factor. The
exchange of the two arguments splits that product into a symmetric and an antisymmetric part, and this
article reads the **antisymmetric part** as a multiplication in its own right:

$$
\tilde p\diamond\tilde q=\tfrac12\bigl(\tilde p^{\natural}\tilde q-\tilde q^{\natural}\tilde p\bigr)
=p_0\vec q-q_t\vec p-\vec p\times\vec q,
$$

the quaternionic product with its scalar part removed. The space $\mathbb{H}$ with this operation is
the **antisymmetric quaternionic algebra** of the block, the operation named $\mathrm{AQA}$ in
*The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*.

**This is not the algebra $\mathbb{H}$.** The two share the space, the addition and the real scalars,
but $\diamond$ is a different multiplication: it is alternating, it is not associative, it has no unit,
and it **fails the Jacobi identity**, unlike the antisymmetric plain half of the same space.
Throughout, the natural sign ${}^{\natural}$ is the quaternion conjugation, the bar is the identity
because $\mathbb{R}$ has no nontrivial involution, and the star coincides with the natural sign and
gives nothing new. The symbol $\diamond$ is reserved for this block, the star $\star$ for the parent
product $\tilde p^{\natural}\tilde q$ of the general quaternionic block.

The article owns the operation as a multiplication: the rule, the class, the laws, the sixteen products
of the basis, the image, the absence of a unit and the reconstruction of the parent product from its
two halves. The element theory is the companion articles of the same section, all below this article
in this category — *Zero Divisors of the Antisymmetric Quaternionic Algebra* and *The Specificities of
the Antisymmetric Quaternionic Algebra*; the defect theory is *The Jacobi Failure and the Associator
Defect of the Antisymmetric Quaternionic Algebra*, the form is *The Invariant Bilinear Forms of the
Antisymmetric Quaternionic Algebra*, the operators are *The Adjoint Operators of the Antisymmetric
Quaternionic Algebra*, and the matrix readings are its two representation articles, also below this
article in this category. The split that produces the block is *The Symmetric and Antisymmetric Parts
of an Algebra Product*; the comparator, whose Jacobi identity holds, is the block of *Introduction to
the Antisymmetric Plain Algebra of Quaternions*, above this article in this category.

**Conventions.** The algebra is $\mathbb{H}$ with basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$ and $\vec e_x\vec e_y=\vec e_z$, so that
$\vec e_x^2=\vec e_y^2=\vec e_z^2=-e_t$ and $e_j\vec e_k=-\vec e_ke_j$ for $j\neq k$. A generic element is
$\tilde q=q_te_t+\vec q$ with $\vec q=\sum_{k=1}^{3}q_k\vec e_k$ and $q_\mu\in\mathbb{R}$;
$\vec p\cdot\vec q$ is the Euclidean dot product and $\vec p\times\vec q$ the vector
product of the vector parts. The parent product is $\tilde p^{\natural}\tilde q$, of scalar–vector rule
$\tilde p^{\natural}\tilde q=(p_0q_t+\vec p\cdot\vec q)+p_0\vec q-q_t\vec p-\vec p\times\vec q$;
the **quaternion form** is $N(\tilde p,\tilde q)=p_0q_t+\vec p\cdot\vec q$. The circle $\circ$
is reserved for the composition of maps.

## The Antisymmetrised Quaternionic Product

### The Rule

**Definition.** The **antisymmetrised quaternionic product** of two quaternions is

$$
\tilde p\diamond\tilde q=\tfrac12\bigl(\tilde p^{\natural}\tilde q-\tilde q^{\natural}\tilde p\bigr).
$$

It is the antisymmetrisation of the parent product $\tilde p^{\natural}\tilde q$, the operation called
the antisymmetric part of the product in *The Symmetric and Antisymmetric Parts of an Algebra Product*,
and the operation named $\mathrm{AQA}$ in *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*. The space $\mathbb{H}$ with $\diamond$ is the **antisymmetric quaternionic
algebra** of the block.

### The Coordinate and Scalar–Vector Forms

The parent product reads
$\tilde p^{\natural}\tilde q=(p_0q_t+\vec p\cdot\vec q)+p_0\vec q-q_t\vec p-\vec p\times\vec q$,
and its exchange $\tilde q^{\natural}\tilde p$ differs in the sign of the scalar part, in the order of
the mixed terms and in the sign of the cross term. Subtracting and halving, the scalar part cancels and
the operation is

$$
\tilde p\diamond\tilde q=p_0\vec q-q_t\vec p-\vec p\times\vec q .
$$

Read on the coordinates,

$$
\tilde p\diamond\tilde q
=(p_0q_x-q_tp_1-p_2q_z+p_3q_y)\vec e_x
+(p_0q_y-q_tp_2-p_3q_x+p_1q_z)\vec e_y
+(p_0q_z-q_tp_3-p_1q_y+p_2q_x)\vec e_z .
$$

**Remark (the scalar part of the parent is removed).** The operation is the parent product with its
scalar coordinate deleted: the scalar value $p_0q_t+\vec p\cdot\vec q$ of the parent is the
trace of its $2\times2$ model, and the antisymmetrisation kills the trace. Every value is a pure
element.

### Bilinearity and the Class

**Proposition.** The operation is $\mathbb{R}$-**bilinear** and **alternating**,

$$
\tilde p\diamond\tilde q=-\tilde q\diamond\tilde p,\qquad \tilde p\diamond\tilde p=0 ,
$$

it is neither commutative nor associative, and it is not the antisymmetric plain operation: at the
units $\tilde p=e_t,\tilde q=\vec e_x$ it gives $e_t\diamond \vec e_x=\vec e_x$, while $e_t\times \vec e_x=0$.

*Proof.* The difference of two biadditive maps is biadditive; the exchange of the arguments reverses
the difference, which is the alternation. The computation on the units is the table below.

## The Identity with the Quaternionic Bracket

**Definition.** The **quaternionic bracket** of the parent product is

$$
[\tilde p,\tilde q]_{\natural}=\tilde p^{\natural}\tilde q-\tilde q^{\natural}\tilde p .
$$

**Proposition.** The operation is half the quaternionic bracket,

$$
[\tilde p,\tilde q]_{\natural}=2\,(\tilde p\diamond\tilde q),
$$

and it is the commutator of the parent product, which is its structural reason: the commutator of a
product is alternating, and it satisfies the Jacobi identity exactly when the parent is associative;
the parent quaternionic product is not associative, hence the failure read below.

*Proof.* The identity is the definition against the definition of the halved difference.

## The Image, the Absence of a Unit and the Reconstruction

**Proposition (the image).** The image of the block is the vector subspace,

$$
\mathbb{H}\diamond\mathbb{H}=\mathrm{Vect}(\mathbb{H})=\{\vec q\}=\{q_t=0\},
$$

of real dimension three, and the block is onto it, since $\vec e_x\diamond \vec e_y=-\vec e_z$ and its images
generate the vector subspace. The left action of $e_t$ is the projection onto the vector subspace,
$e_t\diamond\tilde q=\vec q$, and the right action is its negative, $\tilde q\diamond e_t=-\vec q$.

**Proposition (no unit).** The block has no left unit, no right unit and no two-sided unit. The
candidate $e_t$ has $e_t\diamond\tilde q=\vec q$, which is not $\tilde q$ at a non-pure element, and
no other candidate reaches the scalar direction, every value being pure.

**Proposition (the reconstruction).** The parent product is the sum of its two halves,

$$
\mathrm{GQA}=\mathrm{SQA}+\mathrm{AQA},\qquad
\tilde p^{\natural}\tilde q=N(\tilde p,\tilde q)e_t+\tilde p\diamond\tilde q ,
$$

the symmetric half being $\tfrac12(\tilde p^{\natural}\tilde q+\tilde q^{\natural}\tilde p)=N(\tilde p,\tilde q)e_t$,
which collapses onto the scalar line. The square map sees only the symmetric half,
$\tilde q^{\natural}\tilde q=N(\tilde q,\tilde q)e_t$, so the antisymmetric half carries no square and
no norm.

**Remark (the splitting realises one half by an element).** The left multiplication by $e_t$ is the
projection onto the vector subspace, and the right one is its negative: this is the property the
specificities article reads as the block's criterion.

## The Sixteen Brackets of the Basis

The scalar unit acts by the projection and the vector units multiply by minus the cross product:

| $\diamond$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $0$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
| $\vec e_x$ | $-\vec e_x$ | $0$ | $-\vec e_z$ | $\vec e_y$ |
| $\vec e_y$ | $-\vec e_y$ | $\vec e_z$ | $0$ | $-\vec e_x$ |
| $\vec e_z$ | $-\vec e_z$ | $-\vec e_y$ | $\vec e_x$ | $0$ |

The table has three kinds of entries: the zero diagonal $\tilde p\diamond\tilde p=0$; the eight mixed
entries $e_t\diamond \vec e_k=\vec e_k$ and $\vec e_k\diamond e_t=-\vec e_k$, which are the projection and its negative; and
the six pure entries $e_j\diamond \vec e_k=-e_j\times \vec e_k$.

## The Failure of the Jacobi Identity

**Definition.** The **cyclic sum** of the block at a triple is

$$
J(\tilde p,\tilde q,\tilde r)
=(\tilde p\diamond\tilde q)\diamond\tilde r
+(\tilde q\diamond\tilde r)\diamond\tilde p
+(\tilde r\diamond\tilde p)\diamond\tilde q .
$$

**Theorem (the failure).** The cyclic sum does not vanish; its closed form is

$$
J(\tilde p,\tilde q,\tilde r)
=-p_0\,(\vec q\times\vec r)+q_t\,(\vec p\times\vec r)-r_0\,(\vec p\times\vec q),
$$

and the catalogue witness is the triple $(e_t,\vec e_x,\vec e_y)$, where

$$
J(e_t,\vec e_x,\vec e_y)=(e_t\diamond \vec e_x)\diamond \vec e_y+(\vec e_x\diamond \vec e_y)\diamond e_t+(\vec e_y\diamond e_t)\diamond \vec e_x
=\vec e_x\diamond \vec e_y+(-\vec e_z)\diamond e_t+(-\vec e_y)\diamond \vec e_x=-\vec e_z .
$$

The block therefore satisfies the Jacobi identity nowhere but on the triples whose scalar parts satisfy
the linear condition $J=0$, and it is not a Lie algebra; the full reading is *The Jacobi Failure and
the Associator Defect of the Antisymmetric Quaternionic Algebra*, below this article in this category.

*Proof.* Inserting the explicit form into the three terms and collecting gives the closed form, which
is linear in the scalar triple $(p_0,q_t,r_0)$ with the three cross products as coefficients; at
$(e_t,\vec e_x,\vec e_y)$ only the first term survives and equals $-(\vec e_x\times \vec e_y)=-\vec e_z$. The count of nonzero
basis triples is $18$ of the $64$.

**Remark (the comparator).** The antisymmetric plain block of the same space differs in this alone: it
satisfies the cyclic sum identically, its closed form being zero, and is the Lie algebra
$\mathfrak{su}(2)$ of *The Lie Algebra of the Antisymmetric Plain Algebra*.

## The Placement of the Block among the Six

The block is the antisymmetrisation of the general quaternionic product, the second of the two
antisymmetric operations of the six, set out in *The 6 Products of the Quaternioid $\mathbb{R}$ Space*
and structured in *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*: the two
antisymmetric structures are this one and the antisymmetric plain one, and the law table separates them
on the Jacobi identity, which the plain one satisfies and this one fails (*The Specificities of the
Antisymmetric Plain Algebra* and *The Specificities of the Antisymmetric Quaternionic Algebra*). The
block agrees with its plain companion on alternation, on the properties that alternation implies, and
on the element theory, and differs on the identity and the structure it defines.

## Summary

The antisymmetrised quaternionic multiplication is
$\tilde p\diamond\tilde q=\tfrac12(\tilde p^{\natural}\tilde q-\tilde q^{\natural}\tilde p)=p_0\vec q-q_t\vec p-\vec p\times\vec q$, the anticommutative half of the general
quaternionic product, of quaternion bracket $[\tilde p,\tilde q]_{\natural}=2(\tilde p\diamond\tilde q)$.
It is $\mathbb{R}$-bilinear and alternating, with $\tilde p\diamond\tilde p=0$; its image is the vector
subspace $\mathrm{Vect}(\mathbb{H})$; the left multiplication by $e_t$ is the projection onto the vector
subspace and the right one its negative; and it has no unit. The parent product is reconstructed as
$\mathrm{GQA}=\mathrm{SQA}+\mathrm{AQA}$, and the square map sees only the symmetric half. Unlike its
plain companion it **fails the Jacobi identity**: the cyclic sum has the closed form
$-p_0(\vec q\times\vec r)+q_t(\vec p\times\vec r)-r_0(\vec p\times\vec q)$ and the
witness $(e_t,\vec e_x,\vec e_y)$ gives $-\vec e_z$. This failure is the whole difference between the two
antisymmetric blocks.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde p\diamond\tilde q=\tfrac12(\tilde p^{\natural}\tilde q-\tilde q^{\natural}\tilde p)$ | the antisymmetrised quaternionic multiplication, the operation $\mathrm{AQA}$ |
| $p_0\vec q-q_t\vec p-\vec p\times\vec q$ | its scalar–vector form |
| $[\tilde p,\tilde q]_{\natural}=\tilde p^{\natural}\tilde q-\tilde q^{\natural}\tilde p=2(\tilde p\diamond\tilde q)$ | the quaternionic bracket, twice the operation |
| $\tilde p\diamond\tilde p=0$ | the alternation, the vanishing square |
| $e_t\diamond\tilde q=\vec q$ | the left projection onto the vector subspace |
| $\mathrm{Vect}(\mathbb{H})$ | the image, the vector subspace |
| $\mathrm{GQA}=\mathrm{SQA}+\mathrm{AQA}$ | the reconstruction of the parent product |
| $J(\tilde p,\tilde q,\tilde r)$ | the cyclic sum, nonzero, the Jacobi defect |
| $J(e_t,\vec e_x,\vec e_y)=-\vec e_z$ | the witness of the failure |

## Further Reading

- *Introduction to the General Quaternionic Algebra of Quaternions*, for the parent product, its scalar–vector rule and its laws.
- *The Symmetric and Antisymmetric Parts of an Algebra Product*, for the split, its two projections and the admissibility conditions.
- *The 6 Products of the Quaternioid $\mathbb{R}$ Space* and *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*, for the six products and their names.
- *Introduction to the Antisymmetric Plain Algebra of Quaternions*, above this article in this category, for the comparator whose Jacobi identity holds.
- *The Jacobi Failure and the Associator Defect of the Antisymmetric Quaternionic Algebra*, below this article in this category, for the failure in full.
- *The Invariant Bilinear Forms of the Antisymmetric Quaternionic Algebra* and *The Adjoint Operators of the Antisymmetric Quaternionic Algebra*, both below this article in this category, for the form and the operators.
- *Zero Divisors of the Antisymmetric Quaternionic Algebra* and *The Specificities of the Antisymmetric Quaternionic Algebra*, both below this article in this category, for the element theory.
