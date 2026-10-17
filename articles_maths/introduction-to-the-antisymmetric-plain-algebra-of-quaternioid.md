# __Introduction to the Antisymmetric Plain Algebra__

## Introduction

The underlying real space of the quaternion algebra $\mathbb{H}$ carries the general plain bilinear
product $\tilde q_1\tilde q_2$, the multiplication of *Introduction to the General Plain Algebra of
Quaternions*. The exchange of the two arguments splits that product into a symmetric and an
antisymmetric part, and each part is again a real bilinear product of the same space. This article
reads the **antisymmetric part** as a multiplication in its own right:

$$
\tilde q_1\times\tilde q_2=\tfrac12\bigl(\tilde q_1\tilde q_2-\tilde q_2\tilde q_1\bigr)=\vec q_1\times\vec q_2,
$$

the cross product of the two vector parts. The space $\mathbb{H}$ with this operation is written
$\mathbb{H}^{\times}$ and is the **antisymmetric plain algebra** of the block, the operation named
$\mathrm{APA}$ in *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*.

**This is not the algebra $\mathbb{H}$.** The two share the space, the addition and the real
scalars, but $\times$ is a different multiplication from $\tilde q_1\tilde q_2$: it is alternating, it
is not associative, and $e_t$ is not a unit. Throughout, the natural sign ${}^{\natural}$ is the
quaternion conjugation, the bar is the identity because $\mathbb{R}$ has no nontrivial involution,
and the star coincides with the natural sign and gives nothing new.

The article owns the operation as a multiplication: the rule, the class, the laws, the sixteen
products of the basis, the image, the absence of a unit and the reconstruction of the plain product
from its two halves. The element theory of the block is the companion articles of the same section,
all below this article in this category — *Zero Divisors in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*,
*Square Roots of One and the Idempotents in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*, *Square Roots of Zero
and the Nilpotents of the Antisymmetric Plain Algebra* and *The
Specificities of the Antisymmetric Plain Algebra*; the Lie theory is
*The Lie Algebra of the Antisymmetric Plain Algebra*, *The Killing Form of the Antisymmetric Plain
Algebra* and *The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra*, and
the matrix readings are its two representation articles, also below this article in this category.
The split that produces the block, with its two projections, is *The Symmetric and Antisymmetric
Parts of an Algebra Product*; the symmetric half is *Introduction to the Symmetric Plain Algebra of
Quaternions*.

**Conventions.** The algebra is $\mathbb{H}$ with basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$ and $\vec e_x \vec e_y=\vec e_z$, so
that $\vec e_x^2=\vec e_y^2=\vec e_z^2=-e_t$ and $\vec e_\mu \vec e_\nu=-\vec e_\nu \vec e_\mu$ for $\mu\neq\nu$. A generic element is
$\tilde q=q_te_t+\vec q$ with $\vec q=\sum_{k=1}^{3}q_k\vec e_k$ and $q_\mu\in\mathbb{R}$;
$\vec q_1\cdot\vec q_2$ is the Euclidean dot product and $\vec q_1\times\vec q_2$ the vector
product of the vector parts. The plain product is $\tilde q_1\tilde q_2$, its scalar–vector rule is
$\tilde q_1\tilde q_2=(q_{1t}q_{2t}-\vec q_1\cdot\vec q_2)+q_{1t}\vec q_2+q_{2t}\vec q_1+\vec q_1\times\vec q_2$,
and the symbol $\circ$ is reserved for the composition of maps.

## The Antisymmetric Part of the Plain Product

### The Rule

**Definition.** The **antisymmetric plain product** of two quaternions is

$$
\tilde q_1\times\tilde q_2=\tfrac12\bigl(\tilde q_1\tilde q_2-\tilde q_2\tilde q_1\bigr).
$$

It is the **antisymmetrisation** of the general plain bilinear product $\tilde q_1\tilde q_2$, the
operation called the antisymmetric part of the product in *The Symmetric and Antisymmetric Parts of
an Algebra Product*, and the operation named $\mathrm{APA}$ in *The Algebraic Structures over the
Quaternioid $\mathbb{R}$ Space*. The space $\mathbb{H}$ with the product $\times$ is written
$\mathbb{H}^{\times}$ and is the **antisymmetric plain algebra** of the block.

### The Coordinate and Scalar–Vector Forms

The plain product reads $\tilde q_1\tilde q_2=(q_{1t}q_{2t}-\vec q_1\cdot\vec q_2)+q_{1t}\vec q_2+q_{2t}\vec q_1+\vec q_1\times\vec q_2$,
and its exchange $\tilde q_2\tilde q_1$ differs from it in the sign of the cross term and in the order of
the mixed terms. Subtracting and halving, the symmetric pieces cancel and the operation is the cross
term alone:

$$
\tilde q_1\times\tilde q_2=\vec q_1\times\vec q_2 .
$$

Read on the coordinates,

$$
\tilde q_1\times\tilde q_2=(q_{1y}q_{2z}-q_{1z}q_{2y})\vec e_x+(q_{1z}q_{2x}-q_{1x}q_{2z})\vec e_y+(q_{1x}q_{2y}-q_{1y}q_{2x})\vec e_z .
$$

**Remark (the scalar part is invisible).** The product depends only on the two vector parts, so
**the operation discards both scalar coordinates**: $\tilde q_1\times\tilde q_2$ is unchanged when
$q_{1t}e_t$ or $q_{2t}e_t$ is added to either argument, and every value is a pure element.

### Bilinearity and the Class

**Proposition.** The operation is $\mathbb{R}$-**bilinear**, it is **alternating**,

$$
\tilde q_1\times\tilde q_2=-\tilde q_2\times\tilde q_1,\qquad \tilde q\times\tilde q=0 ,
$$

and it is neither commutative nor associative: at the units $\tilde q_1=\vec e_x$, $\tilde q_2=\vec e_y$ the two
orderings are opposite, and $\tilde q_1\times\tilde q_1=0$ while $(\tilde q_1\times\tilde q_1)\times\tilde q_2=0$
is not $(\tilde q_1\times\tilde q_2)\times\tilde q_1$ at $\tilde q_1=\vec e_x,\tilde q_2=\vec e_y$.

*Proof.* The difference of two biadditive maps is biadditive; the exchange of the arguments
reverses the difference, which is the alternation, and the alternation at equal arguments gives
$\tilde q\times\tilde q=0$. The non-associativity is read on the basis, where
$\vec e_x\times \vec e_y=\vec e_z$ and $(\vec e_x\times \vec e_x)\times \vec e_y=0$, while
$(\vec e_x\times \vec e_y)\times \vec e_x=\vec e_z\times \vec e_x=\vec e_y\neq0$.

## The Identity with the Commutator

**Definition.** The **commutator** of the plain product is

$$
[\tilde q_1,\tilde q_2]=\tilde q_1\tilde q_2-\tilde q_2\tilde q_1 .
$$

**Proposition.** The operation is half the commutator,

$$
[\tilde q_1,\tilde q_2]=2\,(\tilde q_1\times\tilde q_2),
$$

and it is the commutator of the associative product, which is its structural reason: the bracket of
an associative algebra is alternating and satisfies the Jacobi identity.

*Proof.* The identity is the definition of the commutator against the definition of the halved
difference; and the commutator of an associative product is alternating,
$[\tilde q_1,\tilde q_2]=-[\tilde q_2,\tilde q_1]$, so its half is too.

## The Lie Bracket and the Jacobi Identity

**Theorem (the Jacobi identity).** For all $\tilde q_1,\tilde q_2,\tilde q_3\in\mathbb{H}$,

$$
J(\tilde q_1,\tilde q_2,\tilde q_3)=(\tilde q_1\times\tilde q_2)\times\tilde q_3
+(\tilde q_2\times\tilde q_3)\times\tilde q_1+(\tilde q_3\times\tilde q_1)\times\tilde q_2=0 .
$$

*Proof.* Read on the vector parts, the cyclic sum is
$(\vec q_1\times\vec q_2)\times\vec q_3+(\vec q_2\times\vec q_3)\times\vec q_1+(\vec q_3\times\vec q_1)\times\vec q_2$,
which vanishes by the anticommutativity and the Jacobi identity of the vector product of
$\mathbb{R}^3$ (*Quaternion Algebra*); the identity is verified on general elements and on the
$64$ triples of the units. The scalar coordinates do not enter.

**Corollary (the block is a Lie algebra).** The space $\mathbb{H}$ with the operation $\times$,
alternating and satisfying the Jacobi identity, is a real Lie algebra of dimension four. It is
written $\mathfrak{g}=(\mathbb{H},\times)$ and its structure is the subject of *The Lie Algebra of
the Antisymmetric Plain Algebra*, below this article in this category.

## The Sixteen Brackets of the Basis

The scalar direction is killed by the operation on both sides, and the vector units multiply by the
cross product of $\mathbb{R}^3$:

| $\times$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $0$ | $0$ | $0$ | $0$ |
| $\vec e_x$ | $0$ | $0$ | $\vec e_z$ | $-\vec e_y$ |
| $\vec e_y$ | $0$ | $-\vec e_z$ | $0$ | $\vec e_x$ |
| $\vec e_z$ | $0$ | $\vec e_y$ | $-\vec e_x$ | $0$ |

The table has four kinds of entries: the zero diagonal $\tilde q\times\tilde q=0$; the zero first row
and first column; the six unit products $\pm \vec e_k$, which are the structure constants of the cross
product; and nothing else.

## The Image, the Absence of a Unit and the Reconstruction

**Proposition (the image).** The image of the block is the vector subspace,

$$
\mathrm{Vect}(\mathbb{H})=\{\vec q\}=\{q_t=0\},
$$

of real dimension three, and the block is onto it: every pure element is a value, since
$\vec e_x\times \vec e_y=\vec e_z$ and its cyclic images generate the vector subspace.

**Proposition (no unit).** The block has no left unit, no right unit and no two-sided unit. For a
candidate $e_t$ one has $e_t\times\tilde q=0$, which is not $\tilde q$ off the origin;
and no other candidate produces the scalar direction at all, every value being pure.

*Proof.* The values are pure, so a unit $\tilde u$ would give $\tilde u\times\tilde q=\tilde q$ for
all $\tilde q$, in particular a pure right-hand side for $\tilde q=\tilde u$ and a central one for
pure $\tilde q$; the two demands are incompatible off the pure elements. Checked on the four units:
$\vec e_k\times e_t=0\neq \vec e_k$ and $e_t\times e_t=0\neq e_t$.

**Proposition (the reconstruction).** The algebra product is the sum of its two halves,

$$
\tilde q_1\tilde q_2=\tilde q_1\bullet\tilde q_2+\tilde q_1\times\tilde q_2 ,
$$

with $\tilde q_1\bullet\tilde q_2=\tfrac12(\tilde q_1\tilde q_2+\tilde q_2\tilde q_1)$ the symmetric half. The
square map sees only the symmetric half, $\tilde q\tilde q=\tilde q\bullet\tilde q$, so the
antisymmetric half carries no square and no norm; this is why the block is its own product and not a
reading of the algebra product.

## The Placement of the Block among the Companion Products

The space $\mathbb{H}$ carries, beside the algebra product of the *Quaternions* category, the companion products set out in *The 6 Products of the Quaternioid $\mathbb{R}$ Space* and named in *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*. The block of this article is the antisymmetrisation of the algebra product, the one **alternating** structure of the category.

## Summary

The antisymmetric plain multiplication is
$\tilde q_1\times\tilde q_2=\tfrac12(\tilde q_1\tilde q_2-\tilde q_2\tilde q_1)=\vec q_1\times\vec q_2$, the
cross product of the two vector parts, the antisymmetric half of the plain product. It is
$\mathbb{R}$-bilinear and alternating, with $\tilde q\times\tilde q=0$, half the commutator
$[\tilde q_1,\tilde q_2]=2(\tilde q_1\times\tilde q_2)$ of the associative product. It satisfies the Jacobi
identity, so $(\mathbb{H},\times)$ is a real Lie algebra of dimension four; its image is the vector
subspace $\mathrm{Vect}(\mathbb{H})$ of real dimension three; and it has no unit on either side. The
algebra product is reconstructed as $\tilde q_1\tilde q_2=\tilde q_1\bullet\tilde q_2+\tilde q_1\wedge\tilde q_2$, and the square map sees
only the symmetric half, so the block carries no square of its own. Among the companion products of the category the block is the antisymmetrisation of the algebra product, the Lie bracket of the space.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde q_1\times\tilde q_2=\tfrac12(\tilde q_1\tilde q_2-\tilde q_2\tilde q_1)=\vec q_1\times\vec q_2$ | the antisymmetric plain multiplication, the operation $\mathrm{APA}$ |
| $\mathbb{H}^{\times}$ | the quaternion space with the antisymmetric plain product |
| $\vec q_1\times\vec q_2$ | the vector product of the vector parts |
| $[\tilde q_1,\tilde q_2]=\tilde q_1\tilde q_2-\tilde q_2\tilde q_1=2(\tilde q_1\times\tilde q_2)$ | the commutator of the plain product, twice the operation |
| $\tilde q\times\tilde q=0$ | the alternation, the vanishing square |
| $\mathrm{Vect}(\mathbb{H})=\{\vec q\}$ | the image, the vector subspace |
| $\tilde q_1\tilde q_2=\tilde q_1\bullet\tilde q_2+\tilde q_1\wedge\tilde q_2$ | the reconstruction of the algebra product from its two halves |
| $\mathfrak{g}=(\mathbb{H},\times)$ | the real Lie algebra of the block |

## Further Reading

- *Introduction to the Quaternion Algebra*, for the plain product, its scalar–vector rule and its square.
- *The Symmetric and Antisymmetric Parts of an Algebra Product*, for the split, its two projections and the admissibility conditions.
- *The 6 Products of the Quaternioid $\mathbb{R}$ Space* and *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*, for the companion products and their names.
- *Introduction to the Symmetric Plain Algebra*, for the symmetric half of the same product.
- *The Lie Algebra of the Antisymmetric Plain Algebra*, below this article in this category, for the structure of the Lie algebra.
- *The Killing Form of the Antisymmetric Plain Algebra* and *The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra*, both below this article in this category, for the form and the operators.
- *Zero Divisors in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*, *Square Roots of One and the Idempotents in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*, *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* and *The Specificities of the Antisymmetric Plain Algebra*, all below this article in this category, for the element theory.
