# __Introduction to the Antisymmetric Plain Algebra__

## Introduction

The plain product of the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ splits into a symmetric half and an antisymmetric half,

$$
\tilde Q_1\tilde Q_2=\tilde Q_1\bullet\tilde Q_2+\tilde Q_1\wedge\tilde Q_2,\qquad
\tilde Q_1\bullet\tilde Q_2=\tfrac12\bigl(\tilde Q_1\tilde Q_2+\tilde Q_2\tilde Q_1\bigr),\qquad
\tilde Q_1\wedge\tilde Q_2=\tfrac12\bigl(\tilde Q_1\tilde Q_2-\tilde Q_2\tilde Q_1\bigr),
$$

and the two halves are independent data. The symmetric half is the subject of *Introduction to the Symmetric Plain Algebra*; this article introduces the antisymmetric half, the operation

$$
\tilde Q_1\wedge\tilde Q_2=\vec Q_1\times\vec Q_2,
$$

the cross product of the two vector parts. The operation is the antisymmetric plain bilinear entry of the table of *The 12 Products of the Biquaternion Complex Space*, and it is the table's Lie product: it alone of the twelve operations satisfies the Jacobi identity. This article establishes the class of the operation, its alternation, its image, the absence of a unit, the Jacobi identity with the cyclic sum recomputed on the units, the sixteen brackets of the basis, the reconstruction of the plain product from its two halves, and the placement of the block among the twelve.

The article is the common theory of the block: the Lie algebra it makes of $\mathbb{B}$ is *The Lie Algebra of the Antisymmetric Plain Algebra*, the invariant form it carries is *The Killing Form of the Antisymmetric Plain Algebra*, its reading on the remarkable subspaces is *Remarkable Subspaces under the Antisymmetric Plain Algebra*, its adjoints and derivations are *The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra*, and its two matrix models are *Introduction to the Symmetric Plain Algebra*.

The general construction of the two halves of a product is not repeated here: it is *The Symmetric and Antisymmetric Parts of an Algebra Product*, whose definitions of the commutator $[\tilde Q_1,\tilde Q_2]=\tilde Q_1\tilde Q_2-\tilde Q_2\tilde Q_1$, of the outer product $\tilde Q_1\wedge\tilde Q_2=\tfrac12[\tilde Q_1,\tilde Q_2]$ and of the symmetrised product $\tilde Q_1\bullet\tilde Q_2$ are the ones used throughout. The plain product and its pairings are *Introduction to the Biquaternion Algebra* and *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*; the two halves of the other three products of the algebra are the other rows of *The 12 Products of the Biquaternion Complex Space*. Everything below is algebra: the Lie algebra of the block is a module with an alternating bracket, and no group and no analytic notion enters.

## The Antisymmetric Part of the Plain Product

### The Operation

**Definition.** For $\tilde Q_1=\sum_\mu Q_{1\mu} e_\mu$ and $\tilde Q_2=\sum_\mu Q_{2\mu} e_\mu$ in $\mathbb{B}$ put

$$
\tilde Q_1\wedge\tilde Q_2=\tfrac12\bigl(\tilde Q_1\tilde Q_2-\tilde Q_2\tilde Q_1\bigr).
$$

The **antisymmetric plain algebra** of the biquaternions is the operation $\wedge$ on $\mathbb{B}$, and it is the block denoted $\mathrm{APA}$ in the table of the twelve.

**Proposition (the cross product of the vector parts).** For all $\tilde Q_1,\tilde Q_2$,

$$
\tilde Q_1\wedge\tilde Q_2=\vec Q_1\times\vec Q_2,
$$

where $\vec Q_1=(Q_{1x},Q_{1y},Q_{1z})$ and $\vec Q_2=(Q_{2x},Q_{2y},Q_{2z})$ are the vector parts, and the scalar part of the product is zero, $\operatorname{Sc}(\tilde Q_1\wedge\tilde Q_2)=0$.

*Proof.* The scalar parts of $\tilde Q_1\tilde Q_2$ and of $\tilde Q_2\tilde Q_1$ are equal, both being $Q_{1t}Q_{2t}-\vec Q_1\cdot\vec Q_2$, so they cancel in the difference and the scalar part of the half-difference is zero. The vector part of $\tilde Q_1\tilde Q_2$ is $Q_{1t}\vec Q_2+Q_{2t}\vec Q_1+\vec Q_1\times\vec Q_2$ and the vector part of $\tilde Q_2\tilde Q_1$ is $Q_{2t}\vec Q_1+Q_{1t}\vec Q_2+\vec Q_2\times\vec Q_1$, so the half-difference is $\tfrac12(\vec Q_1\times\vec Q_2-\vec Q_2\times\vec Q_1)=\vec Q_1\times\vec Q_2$.

**Corollary (the class).** The operation is $\mathbb{C}$-bilinear, and it is alternating, $\tilde Q_1\wedge\tilde Q_1=0$ and $\tilde Q_1\wedge\tilde Q_2=-\tilde Q_2\wedge\tilde Q_1$ for all $\tilde Q_1,\tilde Q_2$.

*Proof.* The cross product of vector parts is $\mathbb{C}$-bilinear because the plain product is, and it is alternating because $\vec Q_1\times\vec Q_1=0$.

**Remark.** The operation is therefore of the class $\mathbb{C}$-bilinear and alternating, and its values lie in the vector subspace $\mathrm{Vect}(\mathbb{B})$: **the image of the antisymmetric plain algebra is the vector subspace**, of complex dimension three and real dimension six. The scalar direction is invisible to the operation, and the three complex coordinate directions $\vec e_x,\vec e_y,\vec e_z$ carry the whole of it.

### The Absence of a Unit

**Proposition.** The operation has no unit: there is no $\tilde U\in\mathbb{B}$ with $\tilde U\wedge\tilde Q_1=\tilde Q_1$ for all $\tilde Q_1$, and there is no $\tilde U$ with $\tilde Q_1\wedge\tilde U=\tilde Q_1$ for all $\tilde Q_1$.

*Proof.* Every value of the operation has scalar part zero, whereas $\tilde Q_1$ has scalar part $Q_{1t}$ in general; a unit would have to satisfy $\operatorname{Sc}(\tilde U\wedge\tilde Q_1)=Q_{1t}$ for all $\tilde Q_1$, and the left side is zero while the right side is not.

**Remark.** The absence of a unit is the first of the two structural differences from the symmetric half: the antisymmetric half is a multiplication without an identity and with values in a proper subspace, and it is the reason the operation generates a Lie algebra rather than an associative or a Jordan algebra. **The half is a bracket and not a product.**

### The Relation to the Commutator

**Proposition.** The operation is half the commutator of the algebra,

$$
[\tilde Q_1,\tilde Q_2]=\tilde Q_1\tilde Q_2-\tilde Q_2\tilde Q_1=2\,(\tilde Q_1\wedge\tilde Q_2),
$$

and the commutator is the cross product of the vector parts with the factor two, $[\tilde Q_1,\tilde Q_2]=2\,\vec Q_1\times\vec Q_2$.

*Proof.* The commutator is the difference of the two products, which is twice their half-difference; the value is twice the cross product of the previous proposition.

**Remark.** The commutator is alternating and $\mathbb{C}$-bilinear as well, and the two operations carry the same Lie algebra up to the scalar factor $2$: the assignment $\tilde Q_1\mapsto2\tilde Q_1$ is an isomorphism of $(\mathbb{B},[\ ,\ ])$ onto $(\mathbb{B},\wedge)$ read with the factor. The block uses the halved form $\wedge$, which is the form in which the structure constants are the signs of the cross product; the commutator is used in *The Unitary Lie Algebra*, where the bracket of the skew-Hermitian elements is the unhalved difference.

## The Jacobi Identity

### The Cyclic Sum

**Definition.** The **cyclic sum** of the operation on a triple $\tilde Q_1,\tilde Q_2,\tilde Q_3$ is

$$
J(\tilde Q_1,\tilde Q_2,\tilde Q_3)=(\tilde Q_1\wedge\tilde Q_2)\wedge\tilde Q_3+(\tilde Q_2\wedge\tilde Q_3)\wedge\tilde Q_1+(\tilde Q_3\wedge\tilde Q_1)\wedge\tilde Q_2.
$$

**Theorem (the Jacobi identity).** The operation satisfies

$$
(\tilde Q_1\wedge\tilde Q_2)\wedge\tilde Q_3+(\tilde Q_2\wedge\tilde Q_3)\wedge\tilde Q_1+(\tilde Q_3\wedge\tilde Q_1)\wedge\tilde Q_2=0
$$

for all $\tilde Q_1,\tilde Q_2,\tilde Q_3\in\mathbb{B}$.

*Proof.* Write the operation as the cross product of the vector parts, $\tilde Q_1\wedge\tilde Q_2=\vec Q_1\times\vec Q_2$. The three terms are $(\vec Q_1\times\vec Q_2)\times\vec Q_3$, $(\vec Q_2\times\vec Q_3)\times\vec Q_1$ and $(\vec Q_3\times\vec Q_1)\times\vec Q_2$, and the vector triple product gives

$$
(\vec Q_1\times\vec Q_2)\times\vec Q_3=\vec Q_2(\vec Q_1\cdot\vec Q_3)-\vec Q_1(\vec Q_2\cdot\vec Q_3),
$$

with the two cyclic analogues. The six terms cancel in pairs, since $\vec Q_2(\vec Q_1\cdot\vec Q_3)$ from the first term cancels $-\vec Q_2(\vec Q_3\cdot\vec Q_1)$ from the second, and similarly for the other two pairs, using the symmetry of the scalar product of vectors. The identity therefore holds on arbitrary arguments; it was also verified on all sixty-four triples of the units and on general elements of $\mathbb{Q}(i)$ coefficients, where the cyclic sum vanishes identically.

**Remark.** The cyclic sum on the units is zero, and the vanishing is the whole content of the theorem: it is not a numerical accident of the basis but the Jacobi identity of the cross product, and it is inherited by the vector subspace, which is where the values lie. **The operation is a Lie bracket.**

### The Uniqueness among the Twelve

**Theorem (the only Lie product of the twelve).** Of the twelve operations $f_{+},f_{-}$ of the four general products of *The 12 Products of the Biquaternion Complex Space*, the antisymmetric plain algebra is the only one that satisfies the Jacobi identity.

*Proof.* The verification is the table of that article, computed there on the basis. Of the four
antisymmetric parts, $\mathrm{AQA}$, $\mathrm{APS}$ and $\mathrm{AQS}$ fail the identity, with the
witnesses $(e_t,\vec e_x,\vec e_y)$, $(e_t,\vec e_x,\vec e_y)$ and $(\vec e_x,\vec e_x,i\vec e_y)$ and the cyclic sums $-\vec e_z$, $\vec e_z$
and $-2i\vec e_y$; the witnesses were recomputed here, and the first of them, $\mathrm{AQA}$, is the
failure nearest to the present block. Of the four symmetric parts, $\mathrm{SPA}$ alone satisfies
the Jordan identity, and all four fail the cyclic sum, $\mathrm{SPA}$ giving $3e_t$ at
$(e_t,e_t,e_t)$, where its unit sits, and the other three $e_t$ at $(e_t,\vec e_x,\vec e_x)$, so none of them
is a Lie product. Only $\mathrm{APA}$ remains, and the cyclic sum of the previous theorem shows
that it passes.

**Remark.** The uniqueness is the reason the present block is the Lie Theory block of the row: the antisymmetric part of the plain product is the one place in the batch where a classical non-associative algebra, a Lie algebra, appears. The other three antisymmetric parts are brackets that fail their defining identity, and their failure is the subject of the corresponding blocks of the batch.

## The Sixteen Brackets of the Basis

The units $e_t,\vec e_x,\vec e_y,\vec e_z$ satisfy $\vec e_x \vec e_y=\vec e_z$, $\vec e_y \vec e_z=\vec e_x$, $\vec e_z \vec e_x=\vec e_y$ and $\vec e_k^2=-e_t$, and the operation is read on them from the cross product of their vector parts.

**Theorem.** On the units,

$$
e_t\wedge e_\nu=0,\qquad e_\mu\wedge e_t=0,\qquad \vec e_x\wedge \vec e_y=\vec e_z,\qquad \vec e_y\wedge \vec e_z=\vec e_x,\qquad \vec e_z\wedge \vec e_x=\vec e_y,
$$

with the alternating relations $\vec e_y\wedge \vec e_x=-\vec e_z$, $\vec e_z\wedge \vec e_y=-\vec e_x$, $\vec e_x\wedge \vec e_z=-\vec e_y$, and $\vec e_k\wedge \vec e_k=0$; the sixteen brackets are the table

| $\wedge$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $0$ | $0$ | $0$ | $0$ |
| $\vec e_x$ | $0$ | $0$ | $\vec e_z$ | $-\vec e_y$ |
| $\vec e_y$ | $0$ | $-\vec e_z$ | $0$ | $\vec e_x$ |
| $\vec e_z$ | $0$ | $\vec e_y$ | $-\vec e_x$ | $0$ |

*Proof.* Each entry is the cross product of the vector parts of the two units. The unit $e_t$ has vector part zero, so its row and its column vanish; on $\vec e_x,\vec e_y,\vec e_z$ the cross product reproduces the quaternion units, $\vec e_x\times \vec e_y=\vec e_z$ and its cyclic analogues, and is alternating. Computed exactly on the sixteen pairs.

**Remark.** The table is the structure-constant table of the block, and it is the single table of the block that cannot be shortened: the seven entries of the first row and column are zero (the corner counted once), the three cyclic entries above the diagonal are the units, the three below are their negatives, and the three further diagonal entries vanish. **The tail of the table, on $\vec e_x,\vec e_y,\vec e_z$, is the cross-product table of $\mathbb{C}^3$ and hence that of $\mathfrak{sl}(2,\mathbb{C})$**; the block is thus the complexification of the cross product, read inside the biquaternions.

## The Two Halves of the Plain Product

### The Reconstruction

**Theorem (the reconstruction).** The plain product is the sum of its two halves,

$$
\tilde Q_1\tilde Q_2=\tilde Q_1\bullet\tilde Q_2+\tilde Q_1\wedge\tilde Q_2=\tfrac12\bigl(\tilde Q_1\tilde Q_2+\tilde Q_2\tilde Q_1\bigr)+\tfrac12\bigl(\tilde Q_1\tilde Q_2-\tilde Q_2\tilde Q_1\bigr),
$$

and the two halves determine one another's complement: the plain product is recovered from the symmetric plain algebra and the antisymmetric plain algebra together.

*Proof.* Adding the two halves gives $\tilde Q_1\tilde Q_2$. The two are the symmetrisation and the antisymmetrisation of the same product, and the uniqueness of the split, *The Symmetric and Antisymmetric Parts of an Algebra Product*, says that no other pair of a symmetric and an antisymmetric operation has the same sum.

**Remark.** The two halves are the SPA block and the APA block, and the reconstruction is the statement that the general plain algebra $\mathrm{GPA}$ is the sum $\mathrm{SPA}+\mathrm{APA}$ of its two parts, read as operations on the same space.

### What the Square Sees

**Proposition (the square is the symmetric half).** The diagonal of the antisymmetric half is zero, $\tilde Q_1\wedge\tilde Q_1=0$, and the polarisation of the square of the algebra involves only the symmetric half:

$$
(\tilde Q_1+\tilde Q_2)^2-\tilde Q_1^2-\tilde Q_2^2=\tilde Q_1\tilde Q_2+\tilde Q_2\tilde Q_1=2\,(\tilde Q_1\bullet\tilde Q_2).
$$

*Proof.* The first statement is the alternation of the previous section. The second is the polarisation identity of *The Symmetric and Antisymmetric Parts of an Algebra Product*, and it is displayed here only to record its consequence.

**Remark.** **The square map is invisible to the antisymmetric half.** The symmetrisation and the square determine one another, by the polarisation and by the identity $\tilde Q_1\bullet\tilde Q_1=\tilde Q_1^2$, whereas the square of an element carries no information about the antisymmetric half; the plain product and its opposite have the same square and the same symmetric half, and differ exactly in the sign of the antisymmetric half. The antisymmetric plain algebra is therefore the half of the plain product that the power maps of the algebra cannot see, and it is recovered from the product only through the commutator.

## Worked Examples

**Two pure units.** $\vec e_x\wedge \vec e_y=\vec e_z$ and $\vec e_y\wedge \vec e_x=-\vec e_z$: the value is a pure vector, the scalar part is zero, and the reversal of the arguments reverses the value.

**A unit with the identity.** $e_t\wedge \vec e_x=0$: the identity of the algebra has vector part zero and is annihilated by the operation, on both sides.

**The central element.** $(e_t+ie_t)\wedge \vec e_x=0$: both scalar parts have no vector component, and the central element brackets to zero with everything.

**A scalar part that cancels.** For $\tilde Q_1=e_t+\vec e_x$ and $\tilde Q_2=e_t+\vec e_y$, the plain products are $\tilde Q_1\tilde Q_2=e_t+\vec e_x+\vec e_y+\vec e_z$ and $\tilde Q_2\tilde Q_1=e_t+\vec e_x+\vec e_y-\vec e_z$, whose scalar parts and whose $\vec e_x$ and $\vec e_y$ coefficients agree, so the half-difference is $\vec e_z$: $\tilde Q_1\wedge\tilde Q_2=\vec e_z$, and the scalar parts that agree have cancelled, as the first proposition predicts.

**A cyclic sum on the units.** For $\tilde Q_1=\vec e_x,\tilde Q_2=\vec e_y,\tilde Q_3=\vec e_z$ the three terms are $(\vec e_x\wedge \vec e_y)\wedge \vec e_z=\vec e_z\wedge \vec e_z=0$, $(\vec e_y\wedge \vec e_z)\wedge \vec e_x=\vec e_x\wedge \vec e_x=0$ and $(\vec e_z\wedge \vec e_x)\wedge \vec e_y=\vec e_y\wedge \vec e_y=0$: the cyclic sum is zero, the basis instance of the Jacobi identity.

**A witness of the neighbouring failure.** For the antisymmetric quaternionic algebra $\mathrm{AQA}$ the same triple $(e_t,\vec e_x,\vec e_y)$ gives the cyclic sum $-\vec e_z$, as recomputed here from its definition $\tfrac12(\tilde Q_1^{\natural}\tilde Q_2-\tilde Q_2^{\natural}\tilde Q_1)$. On the pure units $\vec e_x,\vec e_y,\vec e_z$ the two brackets are the negatives of one another, since the natural conjugation reverses each factor and contributes a sign, while on $e_t$ they separate outright: $\mathrm{APA}(e_t,\vec e_x)=0$ and $\mathrm{AQA}(e_t,\vec e_x)=\vec e_x$. It is the scalar direction, invisible to the block and visible to its sibling, that carries the failure.

## The Placement of the Block among the Twelve

The twelve operations decompose by product and by half, and the present block is the antisymmetric half of the plain product.

| product | symmetric half | antisymmetric half |
|---|---|---|
| plain $\tilde Q_1\tilde Q_2$ | $\mathrm{SPA}$: the Jordan product on $\mathbb{B}$ | $\mathrm{APA}$: the bracket $\vec Q_1\times\vec Q_2$ |
| quaternionic $\tilde Q_1^{\natural}\tilde Q_2$ | $\mathrm{SQA}$ | $\mathrm{AQA}$, no Jacobi |
| plain sesquilinear $\tilde Q_1\tilde Q_2^{*}$ | $\mathrm{SPS}$ | $\mathrm{APS}$, no Jacobi |
| quaternionic sesquilinear $\tilde Q_1^{\natural}\tilde Q_2^{*}$ | $\mathrm{SQS}$ | $\mathrm{AQS}$, no Jacobi |

**Remark.** The block is the second of the twelve blocks of the batch and it sits immediately after the SPA block in the menu. Its own Lie structure is developed in the rest of the block; its relation to the symmetric half is the reconstruction above; and its relation to the other three antisymmetric parts is the table, in which it is the row that passes the identity the other three fail. **The block owns the reading of the plain product as a bracket, and nothing of the general plain product or of its operators, which remain with the $\mathrm{GPA}$ articles.**

The Lie algebra that the operation makes of $\mathbb{B}$ is *The Lie Algebra of the Antisymmetric Plain Algebra*: its centre is the centre $\mathbb{C}_{\mathbb{B}}$ of the algebra, its image $\mathrm{Vect}(\mathbb{B})$ is a Lie subalgebra isomorphic to $\mathfrak{sl}(2,\mathbb{C})$, and on the real forms the quaternion subspace carries $\mathbb{R}e_t\oplus\mathfrak{su}(2)$ and the anti-Hermitian subspace carries $\mathfrak{u}(2)$. The invariant form of the operation is *The Killing Form of the Antisymmetric Plain Algebra*, its reading on the remarkable subspaces is *Remarkable Subspaces under the Antisymmetric Plain Algebra*, its adjoints and derivations are *The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra*, and its two matrix models are *Introduction to the Symmetric Plain Algebra*.

The element theory of the operation is the five articles that follow it along its own product: *Norm and Invertibility in the Antisymmetric Plain Algebra*, *Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, *Square Roots of One and the Idempotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* and *Square Roots of a General Element in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*. All five are consequences of the alternation established above: the square of every element of the block vanishes, so the block has no norm, no unit and no inverse, every nonzero element is a zero divisor and a nilpotent of index two, its roots of $0$ are the whole punctured space and its roots of $-1$ and $+1$ are empty, and its only idempotent is the origin. The law that separates the block from the other eleven structures, and the reason the Lie theory above is available on it alone, is *The Specificities of the Antisymmetric Plain Algebra*.

## Summary

The antisymmetric part of the plain product of the biquaternions is the operation $\tilde Q_1\wedge\tilde Q_2=\tfrac12(\tilde Q_1\tilde Q_2-\tilde Q_2\tilde Q_1)$, equal to the cross product $\vec Q_1\times\vec Q_2$ of the two vector parts, of scalar part zero, $\mathbb{C}$-bilinear and alternating, with image the vector subspace $\mathrm{Vect}(\mathbb{B})$ and without a unit. It is half the commutator, $[\tilde Q_1,\tilde Q_2]=2(\tilde Q_1\wedge\tilde Q_2)$, and it satisfies the Jacobi identity, with the cyclic sum recomputed as zero on the sixty-four triples of the units; of the twelve operations of the batch it is the only one that does, so it is the only Lie product among them. Its sixteen brackets on the basis have the seven vanishing entries of the identity row and column and, on $\vec e_x,\vec e_y,\vec e_z$, the cross-product table of $\mathbb{C}^3$ and hence of $\mathfrak{sl}(2,\mathbb{C})$. The plain product is reconstructed as $\mathrm{GPA}=\mathrm{SPA}+\mathrm{APA}$, and the square map sees only the symmetric half, so the antisymmetric half is recovered from the product only through the commutator.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde Q_1\wedge\tilde Q_2=\tfrac12(\tilde Q_1\tilde Q_2-\tilde Q_2\tilde Q_1)$ | the antisymmetric plain algebra, $\mathrm{APA}$, the operation of the block |
| $\tilde Q_1\wedge\tilde Q_2=\vec Q_1\times\vec Q_2$ | its value, the cross product of the vector parts |
| $\operatorname{Sc}(\tilde Q_1\wedge\tilde Q_2)=0$ | the scalar part of every value vanishes |
| $[\tilde Q_1,\tilde Q_2]=\tilde Q_1\tilde Q_2-\tilde Q_2\tilde Q_1=2(\tilde Q_1\wedge\tilde Q_2)$ | the commutator of the algebra, twice the operation |
| $\tilde Q_1\bullet\tilde Q_2=\tfrac12(\tilde Q_1\tilde Q_2+\tilde Q_2\tilde Q_1)$ | the symmetric plain algebra, $\mathrm{SPA}$, the other half |
| $\mathrm{GPA}=\mathrm{SPA}+\mathrm{APA}$ | the reconstruction of the plain product from its two halves |
| $\mathrm{Vect}(\mathbb{B})=\mathbb{C}\vec e_x\oplus\mathbb{C}\vec e_y\oplus\mathbb{C}\vec e_z$ | the image of the operation, the vector subspace |
| $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_t$ | the centre of the algebra, annihilated by the operation |
| $\vec e_x\wedge \vec e_y=\vec e_z$, $\vec e_y\wedge \vec e_z=\vec e_x$, $\vec e_z\wedge \vec e_x=\vec e_y$ | the three non-trivial brackets of the units |
| $J(\tilde Q_1,\tilde Q_2,\tilde Q_3)=0$ | the cyclic sum, the Jacobi identity of the block |

## Further Reading

- *The Symmetric and Antisymmetric Parts of an Algebra Product* (`articles_maths/the-symmetric-and-antisymmetric-parts-of-an-algebra-product.md`), for the split of a product into its two halves, its uniqueness and the admissibility conditions
- *The 12 Products of the Biquaternion Complex Space* (`articles_maths/the-12-products-of-the-biquaternion-complex-space.md`), for the table of the twelve operations, the witnesses of the three failing Jacobi identities and the two that pass, and for the same twelve operations read from the side of the order symmetry
- *The Lie Algebra of the Antisymmetric Plain Algebra* (`articles_maths/the-lie-algebra-of-the-antisymmetric-plain-algebra.md`), for the centre, the image, the identifications with $\mathfrak{sl}(2,\mathbb{C})$, $\mathfrak{su}(2)$ and $\mathfrak{u}(2)$, and the enveloping algebra
- *The Unitary Lie Algebra* (`articles_maths/the-unitary-lie-algebra.md`), for the bracket of the skew-Hermitian elements, the unhalved commutator and the group of linear maps preserving the form
- *Introduction to the Biquaternion Algebra* (`articles_maths/introduction-to-the-biquaternion-algebra.md`), for the plain product and the group it defines
- *Introduction to the Remarkable Subspaces* (`articles_maths/introduction-to-the-remarkable-subspaces.md`), for the remarkable subspaces on which the block is read
- *Norm and Invertibility in the Antisymmetric Plain Algebra* (`articles_maths/norm-and-invertibility-in-the-antisymmetric-plain-algebra.md`), for the absence of a unit, of an inverse and of a norm, and for the operator trace form and the scalar-part form
- *Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/zero-divisors-in-the-algebraic-structures-over-the-biquaternion-c-space.md`) and *Annihilators in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/annihilators-in-the-algebraic-structures-over-the-biquaternion-c-space.md`), for the totality of the zero-divisor set and for the annihilator of the left multiplication operator with its rank
- *Square Roots of One and the Idempotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/square-roots-of-one-and-the-idempotents-in-the-algebraic-structures-over-the-biquaternion-c-space.md`), for the empty root set of $+1$ and the origin alone as the idempotent
- *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/square-roots-of-zero-and-the-nilpotents-in-the-algebraic-structures-over-the-biquaternion-c-space.md`), for the root set of $0$ and the totality of the nilpotent class
- *Square Roots of a General Element in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/square-roots-of-a-general-element-in-the-algebraic-structures-over-the-biquaternion-c-space.md`), for the zero square map and the image and kernel of the square
- *The Specificities of the Antisymmetric Plain Algebra* (`articles_maths/the-specificities-of-the-antisymmetric-plain-algebra.md`), for the Leibniz identity, its equivalence with the Jacobi identity for an alternating product and the isolation of the block among the twelve
