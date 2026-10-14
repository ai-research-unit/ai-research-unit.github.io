# __Introduction to the Antisymmetric Plain Algebra of Quaternions__

## Introduction

The underlying real space of the quaternion algebra $\mathbb{H}$ carries the general plain bilinear
product $\tilde p\tilde q$, the multiplication of *Introduction to the General Plain Algebra of
Quaternions*. The exchange of the two arguments splits that product into a symmetric and an
antisymmetric part, and each part is again a real bilinear product of the same space. This article
reads the **antisymmetric part** as a multiplication in its own right:

$$
\tilde p\times\tilde q=\tfrac12\bigl(\tilde p\tilde q-\tilde q\tilde p\bigr)=\vec p\times\vec q,
$$

the cross product of the two vector parts. The space $\mathbb{H}$ with this operation is written
$\mathbb{H}^{\times}$ and is the **antisymmetric plain algebra** of the block, the operation named
$\mathrm{APA}$ in *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*.

**This is not the algebra $\mathbb{H}$.** The two share the space, the addition and the real
scalars, but $\times$ is a different multiplication from $\tilde p\tilde q$: it is alternating, it
is not associative, and $e_0$ is not a unit. Throughout, the natural sign ${}^{\natural}$ is the
quaternion conjugation, the bar is the identity because $\mathbb{R}$ has no nontrivial involution,
and the star coincides with the natural sign and gives nothing new.

The article owns the operation as a multiplication: the rule, the class, the laws, the sixteen
products of the basis, the image, the absence of a unit and the reconstruction of the plain product
from its two halves. The element theory of the block is the companion articles of the same section,
all below this article in this category — *Zero Divisors of the Antisymmetric Plain Algebra*,
*Square Roots of One and the Idempotents of the Antisymmetric Plain Algebra*, *Square Roots of Zero
and the Nilpotents of the Antisymmetric Plain Algebra* and *The
Specificities of the Antisymmetric Plain Algebra*; the Lie theory is
*The Lie Algebra of the Antisymmetric Plain Algebra*, *The Killing Form of the Antisymmetric Plain
Algebra* and *The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra*, and
the matrix readings are its two representation articles, also below this article in this category.
The split that produces the block, with its two projections, is *The Symmetric and Antisymmetric
Parts of an Algebra Product*; the symmetric half is *Introduction to the Symmetric Plain Algebra of
Quaternions*.

**Conventions.** The algebra is $\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$ and $e_1e_2=e_3$, so
that $e_1^2=e_2^2=e_3^2=-e_0$ and $e_je_k=-e_ke_j$ for $j\neq k$. A generic element is
$\tilde q=q_0e_0+\vec q$ with $\vec q=\sum_{k=1}^{3}q_ke_k$ and $q_\mu\in\mathbb{R}$;
$\vec p\cdot\vec q$ is the Euclidean dot product and $\vec p\times\vec q$ the vector
product of the vector parts. The plain product is $\tilde p\tilde q$, its scalar–vector rule is
$\tilde p\tilde q=(p_0q_0-\vec p\cdot\vec q)+p_0\vec q+q_0\vec p+\vec p\times\vec q$,
and the symbol $\circ$ is reserved for the composition of maps.

## The Antisymmetric Part of the Plain Product

### The Rule

**Definition.** The **antisymmetric plain product** of two quaternions is

$$
\tilde p\times\tilde q=\tfrac12\bigl(\tilde p\tilde q-\tilde q\tilde p\bigr).
$$

It is the **antisymmetrisation** of the general plain bilinear product $\tilde p\tilde q$, the
operation called the antisymmetric part of the product in *The Symmetric and Antisymmetric Parts of
an Algebra Product*, and the operation named $\mathrm{APA}$ in *The 6 Algebraic Structures over the
Quaternion $\mathbb{R}$ Space*. The space $\mathbb{H}$ with the product $\times$ is written
$\mathbb{H}^{\times}$ and is the **antisymmetric plain algebra** of the block.

### The Coordinate and Scalar–Vector Forms

The plain product reads $\tilde p\tilde q=(p_0q_0-\vec p\cdot\vec q)+p_0\vec q+q_0\vec p+\vec p\times\vec q$,
and its exchange $\tilde q\tilde p$ differs from it in the sign of the cross term and in the order of
the mixed terms. Subtracting and halving, the symmetric pieces cancel and the operation is the cross
term alone:

$$
\tilde p\times\tilde q=\vec p\times\vec q .
$$

Read on the coordinates,

$$
\tilde p\times\tilde q=(p_2q_3-p_3q_2)e_1+(p_3q_1-p_1q_3)e_2+(p_1q_2-p_2q_1)e_3 .
$$

**Remark (the scalar part is invisible).** The product depends only on the two vector parts, so
**the operation discards both scalar coordinates**: $\tilde p\times\tilde q$ is unchanged when
$p_0e_0$ or $q_0e_0$ is added to either argument, and every value is a pure element.

### Bilinearity and the Class

**Proposition.** The operation is $\mathbb{R}$-**bilinear**, it is **alternating**,

$$
\tilde p\times\tilde q=-\tilde q\times\tilde p,\qquad \tilde p\times\tilde p=0 ,
$$

and it is neither commutative nor associative: at the units $\tilde p=e_1$, $\tilde q=e_2$ the two
orderings are opposite, and $\tilde p\times\tilde p=0$ while $(\tilde p\times\tilde p)\times\tilde q=0$
is not $(\tilde p\times\tilde q)\times\tilde p$ at $\tilde p=e_1,\tilde q=e_2$.

*Proof.* The difference of two biadditive maps is biadditive; the exchange of the arguments
reverses the difference, which is the alternation, and the alternation at equal arguments gives
$\tilde p\times\tilde p=0$. The non-associativity is read on the basis, where
$e_1\times e_2=e_3$ and $(e_1\times e_1)\times e_2=0$, while
$(e_1\times e_2)\times e_1=e_3\times e_1=e_2\neq0$.

## The Identity with the Commutator

**Definition.** The **commutator** of the plain product is

$$
[\tilde p,\tilde q]=\tilde p\tilde q-\tilde q\tilde p .
$$

**Proposition.** The operation is half the commutator,

$$
[\tilde p,\tilde q]=2\,(\tilde p\times\tilde q),
$$

and it is the commutator of the associative product, which is its structural reason: the bracket of
an associative algebra is alternating and satisfies the Jacobi identity.

*Proof.* The identity is the definition of the commutator against the definition of the halved
difference; and the commutator of an associative product is alternating,
$[\tilde p,\tilde q]=-[\tilde q,\tilde p]$, so its half is too.

## The Lie Bracket and the Jacobi Identity

**Theorem (the Jacobi identity).** For all $\tilde p,\tilde q,\tilde r\in\mathbb{H}$,

$$
J(\tilde p,\tilde q,\tilde r)=(\tilde p\times\tilde q)\times\tilde r
+(\tilde q\times\tilde r)\times\tilde p+(\tilde r\times\tilde p)\times\tilde q=0 .
$$

*Proof.* Read on the vector parts, the cyclic sum is
$(\vec p\times\vec q)\times\vec r+(\vec q\times\vec r)\times\vec p+(\vec r\times\vec p)\times\vec q$,
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

| $\times$ | $e_0$ | $e_1$ | $e_2$ | $e_3$ |
|---|---|---|---|---|
| $e_0$ | $0$ | $0$ | $0$ | $0$ |
| $e_1$ | $0$ | $0$ | $e_3$ | $-e_2$ |
| $e_2$ | $0$ | $-e_3$ | $0$ | $e_1$ |
| $e_3$ | $0$ | $e_2$ | $-e_1$ | $0$ |

The table has four kinds of entries: the zero diagonal $\tilde p\times\tilde p=0$; the zero first row
and first column; the six unit products $\pm e_k$, which are the structure constants of the cross
product; and nothing else.

## The Image, the Absence of a Unit and the Reconstruction

**Proposition (the image).** The image of the block is the vector subspace,

$$
\mathrm{Vect}(\mathbb{H})=\{\vec q\}=\{q_0=0\},
$$

of real dimension three, and the block is onto it: every pure element is a value, since
$e_1\times e_2=e_3$ and its cyclic images generate the vector subspace.

**Proposition (no unit).** The block has no left unit, no right unit and no two-sided unit. For a
candidate unit $\tilde e=e_0$ one has $e_0\times\tilde q=0$, which is not $\tilde q$ off the origin;
and no other candidate produces the scalar direction at all, every value being pure.

*Proof.* The values are pure, so a unit $\tilde e$ would give $\tilde e\times\tilde q=\tilde q$ for
all $\tilde q$, in particular a pure right-hand side for $\tilde q=\tilde e$ and a central one for
pure $\tilde q$; the two demands are incompatible off the pure elements. Checked on the four units:
$e_k\times e_0=0\neq e_k$ and $e_0\times e_0=0\neq e_0$.

**Proposition (the reconstruction).** The plain product is the sum of its two halves,

$$
\mathrm{GPA}=\mathrm{SPA}+\mathrm{APA},\qquad
\tilde p\tilde q=\tilde p\bullet\tilde q+\tilde p\times\tilde q ,
$$

with $\tilde p\bullet\tilde q=\tfrac12(\tilde p\tilde q+\tilde q\tilde p)$ the symmetric half. The
square map sees only the symmetric half, $\tilde q\tilde q=\tilde q\bullet\tilde q$, so the
antisymmetric half carries no square and no norm; this is why the block is its own product and not a
reading of the plain one.

## The Placement of the Block among the Six

The space $\mathbb{H}$ carries six bilinear products, set out in *The 6 Products of the Quaternion
$\mathbb{R}$ Space* and structured in *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$
Space*: the two general products, their symmetrisations and their antisymmetrisations. The block of
this article is the antisymmetrisation of the plain product. It is the one **alternating** product of
the plain row; the other antisymmetric operation of the six, the antisymmetrisation of the
quaternionic product, is *Introduction to the Antisymmetric Quaternionic Algebra of Quaternions*,
below this article in this category.

## Summary

The antisymmetric plain multiplication is
$\tilde p\times\tilde q=\tfrac12(\tilde p\tilde q-\tilde q\tilde p)=\vec p\times\vec q$, the
cross product of the two vector parts, the antisymmetric half of the plain product. It is
$\mathbb{R}$-bilinear and alternating, with $\tilde p\times\tilde p=0$, half the commutator
$[\tilde p,\tilde q]=2(\tilde p\times\tilde q)$ of the associative product. It satisfies the Jacobi
identity, so $(\mathbb{H},\times)$ is a real Lie algebra of dimension four; its image is the vector
subspace $\mathrm{Vect}(\mathbb{H})$ of real dimension three; and it has no unit on either side. The
plain product is reconstructed as $\mathrm{GPA}=\mathrm{SPA}+\mathrm{APA}$, and the square map sees
only the symmetric half, so the block carries no square of its own. Among the six products the block
is one of the two antisymmetrisations, the plain one; the quaternionic one fails the Jacobi identity
and is the neighbouring block.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde p\times\tilde q=\tfrac12(\tilde p\tilde q-\tilde q\tilde p)=\vec p\times\vec q$ | the antisymmetric plain multiplication, the operation $\mathrm{APA}$ |
| $\mathbb{H}^{\times}$ | the quaternion space with the antisymmetric plain product |
| $\vec p\times\vec q$ | the vector product of the vector parts |
| $[\tilde p,\tilde q]=\tilde p\tilde q-\tilde q\tilde p=2(\tilde p\times\tilde q)$ | the commutator of the plain product, twice the operation |
| $\tilde p\times\tilde p=0$ | the alternation, the vanishing square |
| $\mathrm{Vect}(\mathbb{H})=\{\vec q\}$ | the image, the vector subspace |
| $\mathrm{GPA}=\mathrm{SPA}+\mathrm{APA}$ | the reconstruction of the plain product from its two halves |
| $\mathfrak{g}=(\mathbb{H},\times)$ | the real Lie algebra of the block |

## Further Reading

- *Introduction to the General Plain Algebra of Quaternions*, for the plain product, its scalar–vector rule and its square.
- *The Symmetric and Antisymmetric Parts of an Algebra Product*, for the split, its two projections and the admissibility conditions.
- *The 6 Products of the Quaternion $\mathbb{R}$ Space* and *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, for the six products and their names.
- *Introduction to the Symmetric Plain Algebra of Quaternions*, for the symmetric half of the same product.
- *The Lie Algebra of the Antisymmetric Plain Algebra*, below this article in this category, for the structure of the Lie algebra.
- *The Killing Form of the Antisymmetric Plain Algebra* and *The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra*, both below this article in this category, for the form and the operators.
- *Zero Divisors of the Antisymmetric Plain Algebra*, *Square Roots of One and the Idempotents of the Antisymmetric Plain Algebra*, *Square Roots of Zero and the Nilpotents of the Antisymmetric Plain Algebra* and *The Specificities of the Antisymmetric Plain Algebra*, all below this article in this category, for the element theory.
